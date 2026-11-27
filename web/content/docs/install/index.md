---
title: Install
description: Packages, supported runtimes and how to add Sponsorkit to your project, plus how to use the Rust crate before it is published.
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

:::danger[Rust isn't on crates.io yet]
The JavaScript, .NET, Python and Go SDKs are published. The Rust crate `sponsorkit` is **not** on crates.io
yet, and a crate someone else publishes under that name would not be this project. Until its first release is
announced in the [repository](https://github.com/ffMathy/sponsorkit), depend on the Git repository as shown
below.
:::

## Install

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
go get github.com/ffMathy/sponsorkit/sdks/go@v0.1.0
```

```bash tab="Rust" key="rust"
cargo add sponsorkit --git https://github.com/ffMathy/sponsorkit
```
:::

Run each command in your project's folder. [Package managers & CDNs](package-managers.md) has the commands for
pnpm, Yarn, Bun, Deno, uv, Poetry, Paket and more. Once the crate is on crates.io, Rust becomes
`cargo add sponsorkit`.

## In this section

- [Package managers & CDNs](package-managers.md): npm, pnpm, Yarn, Bun, Deno and browser CDNs; `dotnet`,
  `PackageReference` and Paket; pip, uv and Poetry; Go modules; Cargo.
- [Supported platforms](supported-platforms.md): runtime versions, sign-in methods and where state is stored on
  each operating system.
- [Verify the install](verify.md): print the installed version and run a smoke test without signing in.
- [Versions & pinning](versions.md): how SDK versions and release tags work, and how to pin one.
- [Build from source](from-source.md): use an unreleased SDK or change from this monorepo.

Once installed, continue with the [quickstart](../getting-started/quickstart.md).
