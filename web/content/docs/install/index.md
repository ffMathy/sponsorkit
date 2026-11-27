---
title: Install
description: Packages, supported runtimes and how to add Sponsorkit to your project, plus what to do for the SDKs that aren't published yet.
sidebar_label: Overview
---

Every SDK is one package with the same behaviour and the same result shape. Pick yours:

| Language | Package | Runtime | Dependencies |
|---|---|---|---|
| JavaScript / TypeScript | `@sponsorkit/sdk` | Node 20+, Bun, Deno, evergreen browsers | None |
| .NET | `Sponsorkit` | `netstandard2.0` and `net8.0` builds | `System.Text.Json` (netstandard2.0 only) |
| Python | `sponsorkit` | Python 3.10+ | `httpx` |
| Go | `github.com/ffMathy/sponsorkit/sdks/go` | Go 1.23+ | Standard library only |
| Rust | `sponsorkit` | Rust 1.85+ (MSRV), Tokio | `reqwest` (rustls), `serde`, `tokio` |

Rust apps also need a Tokio runtime, for example `cargo add tokio --features macros,rt-multi-thread`.

:::danger[Only .NET is on a registry so far]
`Sponsorkit` 0.1.0 is [on NuGet](https://www.nuget.org/packages/Sponsorkit). The other SDKs haven't been
released yet: `@sponsorkit/sdk` and `sponsorkit` are **not** on npm, PyPI or crates.io, and some of those names
aren't reserved yet, so a package someone else publishes under that name would not be this project. Until their
first release is announced in the [repository](https://github.com/ffMathy/sponsorkit), install them from Git
or from a local build as shown below, and don't install these names from a registry.
:::

## Install

.NET installs from NuGet. Go fetches the module straight from GitHub. Python and Rust can depend on the Git
repository directly. JavaScript needs a local build first. [Build from source](from-source.md) explains each
recipe, including a local .NET build for unreleased changes.

:::tabs
```bash tab="JavaScript" key="js"
git clone https://github.com/ffMathy/sponsorkit.git
(cd sponsorkit && bun install && bun run --cwd sdks/js build && cd sdks/js && npm pack)
npm install ./sponsorkit/sdks/js/sponsorkit-sdk-0.1.0.tgz
```

```bash tab=".NET" key="dotnet"
dotnet add package Sponsorkit
```

```bash tab="Python" key="python"
python -m pip install "sponsorkit @ git+https://github.com/ffMathy/sponsorkit@main#subdirectory=sdks/python"
```

```bash tab="Go" key="go"
go get github.com/ffMathy/sponsorkit/sdks/go@main
```

```bash tab="Rust" key="rust"
cargo add sponsorkit --git https://github.com/ffMathy/sponsorkit
```
:::

Building the JavaScript SDK needs [Bun](https://bun.sh). Run the .NET `dotnet add package` line in your
project's folder.

## After the first release

Once each SDK is published to its registry, these are the commands to use. The .NET one works today; the npm,
PyPI and crates.io ones fail with "not found" until those releases; see the warning above.

:::tabs
```bash tab="JavaScript" key="js"
npm install @sponsorkit/sdk
```

```bash tab=".NET" key="dotnet"
dotnet add package Sponsorkit
```

```bash tab="Python" key="python"
pip install sponsorkit
```

```bash tab="Go" key="go"
go get github.com/ffMathy/sponsorkit/sdks/go
```

```bash tab="Rust" key="rust"
cargo add sponsorkit
```
:::

## In this section

- [Package managers & CDNs](package-managers.md): npm, pnpm, Yarn, Bun, Deno and browser CDNs; `dotnet`,
  `PackageReference` and Paket; pip, uv and Poetry; Go modules; Cargo.
- [Supported platforms](supported-platforms.md): runtime versions, sign-in methods and where state is stored on
  each operating system.
- [Verify the install](verify.md): print the installed version and run a smoke test without signing in.
- [Versions & pinning](versions.md): how SDK versions and release tags work, and how to pin one.
- [Build from source](from-source.md): use an unreleased SDK or change from this monorepo.

Once installed, continue with the [quickstart](../getting-started/quickstart.md).
