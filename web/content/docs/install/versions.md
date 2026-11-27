---
title: Versions & pinning
description: How the SDKs are versioned and released, how the wire protocol is versioned, and how to pin a version in each package manager.
order: 40
---

## How versions work

- **Each SDK has its own version**, released independently from this monorepo by pushing a tag named
  `sdks/<sdk>/v<version>`: `sdks/js/v1.0.0`, `sdks/dotnet/v1.0.0`, `sdks/python/v1.0.0`, `sdks/go/v1.0.0`,
  `sdks/rust/v1.0.0`. For the registry packages, the release workflow refuses a tag that doesn't match the
  version in the package manifest.
- **Every SDK is at 1.0.0** and follows semantic versioning: minor and patch releases are backwards compatible,
  and a breaking change bumps the major version. Pin to a major version ("1.x") and let minor and patch updates
  in.
- **Use 1.0.0 or later.** Releases before 1.0.0 (0.1.0, and anything 0.x) used an older spelling of Open
  Collective on the wire (`opencollective` instead of `open-collective`) and don't work with the hosted API.
  1.0.0 also names the option `openCollective` (JavaScript) and `open_collective` (Python, Rust).
- **The HTTP API is versioned separately** under `/api/v1`. Every SDK from 1.0.0 on speaks `v1`, and their
  behaviour is pinned by the shared conformance suite, so different SDKs (or SDK versions) agree on the result shape and the
  [stored state](supported-platforms.md#where-state-is-stored).
- **Registries publish through trusted publishing** (OIDC from GitHub Actions): npm, NuGet, PyPI and crates.io.
  Go needs no publish step; the module proxy picks up the tag.

## Pinning

The quickest safe choice is "this major version, any minor or patch". Lock files (`package-lock.json`, `packages.lock.json`,
`uv.lock`, `poetry.lock`, `go.sum`, `Cargo.lock`) then make builds reproducible.

### JavaScript {#javascript}

```bash title="Terminal"
npm install @sponsorkit/sdk@1.0.0 --save-exact   # exactly 1.0.0
```

In `package.json`, `"^1.0.0"` means "1.x", `"~1.0.0"` means "1.0.x", and `"1.0.0"` is exact. pnpm, Yarn
and Bun read the same ranges.

### .NET {#dotnet}

```xml title="MyApp.csproj"
<PackageReference Include="Sponsorkit" Version="[1.0.0,2.0.0)" />
```

`[1.0.0,2.0.0)` accepts any 1.x release. A plain `Version="1.0.0"` is a minimum: NuGet resolves the lowest
version that satisfies every constraint, so in practice you get exactly 1.0.0 until you change it, and
`[1.0.0]` is an exact pin. Paket uses `nuget Sponsorkit ~> 1.0` in `paket.dependencies` for "1.x".

### Python {#python}

```toml title="pyproject.toml"
dependencies = ["sponsorkit~=1.0"]   # >=1.0, <2
```

`sponsorkit==1.0.0` pins exactly. `sponsorkit.__version__` reports what is installed.

### Go {#go}

```bash title="Terminal"
go get github.com/ffMathy/sponsorkit/sdks/go@v1.0.0
```

`go.mod` always records an exact version, and Go's minimal version selection never upgrades it on its own. The
tag in the repository is `sdks/go/v1.0.0` (Go's convention for a module in a subdirectory), but you ask for
`@v1.0.0`. For an unreleased change, ask for a branch or commit: `@main` resolves to a pseudo-version.

### Rust {#rust}

```toml title="Cargo.toml"
[dependencies]
sponsorkit = "1"   # >=1.0.0, <2.0.0; "=1.0.0" pins exactly
```

## Upgrading

The session token, cache and nag counters are stored in a versioned format (`"v": 1`) shared by every SDK. The
SDKs read stored documents leniently: a document or field they can't parse counts as absent (at worst the user
signs in again) instead of crashing your app.
