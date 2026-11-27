---
title: Sponsorkit documentation
description: Check whether the current user sponsors you on GitHub Sponsors or Open Collective, and help them start. No account, no API key, no stored data.
sidebar_label: Introduction
order: 0
---

<!-- OWNERS: platform. -->

Sponsorkit tells your software whether the current user supports you on GitHub Sponsors or Open Collective,
and helps them start. You write the rule; Sponsorkit reports the facts.

:::warning[Project status: pre-release]
- **Only the .NET SDK is published so far.** `Sponsorkit` 0.1.0 is [on NuGet](https://www.nuget.org/packages/Sponsorkit).
  `@sponsorkit/sdk` and `sponsorkit` are not on npm, PyPI or crates.io yet, and some of those names aren't
  reserved yet, so don't install them from a registry: [install from source](install/from-source.md) until
  their first release is announced. (The Go module is fetched straight from GitHub.)
- **The hosted service is live** at `api.sponsorkit.io`. Some provider behaviour has only been tested against
  stubbed provider responses so far; [mock mode](guides/mock-mode.md) needs no network at all.
:::

## Start here

- [Getting started](getting-started/index.md): the four steps of an integration.
- [Quickstart](getting-started/quickstart.md): copy-paste examples for every SDK.
- [Install](install/index.md): packages and supported runtimes.
- [Concepts](concepts/index.md): targets, sessions, the contribution shape and the error contract.
- [Guides](guides/index.md): checkout, nags, mock mode and backend verification.

## SDKs

| Language | Package | Guide | API reference |
|---|---|---|---|
| JavaScript / TypeScript | `@sponsorkit/sdk` | [Guide](languages/js/index.md) | [Reference](/docs/reference/js) |
| .NET | `Sponsorkit` | [Guide](languages/dotnet/index.md) | [Reference](/docs/reference/dotnet) |
| Python | `sponsorkit` | [Guide](languages/python/index.md) | [Reference](/docs/reference/python) |
| Go | `github.com/ffMathy/sponsorkit/sdks/go` | [Guide](languages/go/index.md) | [Reference](/docs/reference/go) |
| Rust | `sponsorkit` | [Guide](languages/rust/index.md) | [Reference](/docs/reference/rust) |

Every SDK has the same behaviour, the same result shape and the same
[error contract](concepts/error-contract.md); only the naming follows each language's conventions.

## Under the hood

The SDKs talk to a small, stateless HTTP API. Its [wire protocol](reference-http/index.md) is public, and you can
[host it yourself](reference-http/self-hosting.md).
