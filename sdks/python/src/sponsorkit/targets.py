"""Targets and target sets (PROTOCOL §1).

A target is an account a maintainer receives sponsorships on: ``github:<login>`` or
``open-collective:<slug>``. A *target set* is canonical: deduplicated, sorted by string form,
with at most one target per provider.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Literal

from .errors import SponsorkitError

__all__ = [
    "PROVIDERS",
    "Provider",
    "Target",
    "canonical_targets",
    "normalize_target",
    "parse_target",
    "targets_from_options",
    "targets_from_param",
    "targets_hash",
    "targets_param",
]

Provider = Literal["github", "open-collective"]
"""A contribution provider."""

PROVIDERS: tuple[Provider, ...] = ("github", "open-collective")

# The keys a targets mapping (verify_session) accepts, like the constructor's keyword arguments.
TARGET_OPTION_KEYS: tuple[str, ...] = ("github", "open_collective")

_GITHUB_LOGIN = re.compile(r"^[a-z0-9](?:[a-z0-9]|-(?=[a-z0-9])){0,38}$")
_OC_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{0,254}$")


@dataclass(frozen=True, order=True)
class Target:
    """A normalized target (lowercased, trimmed account)."""

    provider: Provider
    account: str

    def __str__(self) -> str:
        return f"{self.provider}:{self.account}"


def _invalid(message: str) -> SponsorkitError:
    return SponsorkitError("invalid_config", message)


def normalize_target(provider: str, account: str) -> Target:
    """Validate and normalize one target. Raises ``SponsorkitError("invalid_config")``."""
    if provider not in PROVIDERS:
        raise _invalid(f'Unknown provider "{provider}"')
    if not isinstance(account, str):
        raise _invalid(f"The {provider} account must be a string")
    a = account.strip().lower()
    pattern = _GITHUB_LOGIN if provider == "github" else _OC_SLUG
    if not pattern.fullmatch(a):
        raise _invalid(f'Invalid {provider} account "{account}"')
    return Target(provider, a)


def parse_target(value: str) -> Target:
    """Parse ``"github:octocat"`` into a :class:`Target`."""
    provider, sep, account = value.partition(":")
    if not sep or not provider:
        raise _invalid(f'Invalid target "{value}"')
    return normalize_target(provider, account)


def canonical_targets(targets: Iterable[Target]) -> tuple[Target, ...]:
    """Deduplicate and sort a target set; at least one target, at most one per provider."""
    by_string = {str(t): t for t in targets}
    ordered = tuple(by_string[k] for k in sorted(by_string, key=lambda s: s.encode("ascii")))
    if not ordered:
        raise _invalid("At least one target (github or open_collective) is required")
    if len({t.provider for t in ordered}) != len(ordered):
        raise _invalid("At most one target per provider is supported")
    return ordered


def targets_from_options(github: str | None = None, open_collective: str | None = None) -> tuple[Target, ...]:
    """Build a canonical target set from ``github=`` / ``open_collective=`` handles."""
    out: list[Target] = []
    if github:
        out.append(normalize_target("github", github))
    if open_collective:
        out.append(normalize_target("open-collective", open_collective))
    return canonical_targets(out)


def targets_from_param(param: str) -> tuple[Target, ...]:
    """Parse a target param such as ``"github:x,open-collective:y"``."""
    return canonical_targets(parse_target(p) for p in param.split(",") if p)


def coerce_targets(
    targets: Mapping[str, str | None] | str | Iterable[str | Target],
) -> tuple[Target, ...]:
    """Accept a ``{"github": ..., "open_collective": ...}`` mapping, a target param or a list of targets."""
    if isinstance(targets, Mapping):
        unknown = set(targets) - set(TARGET_OPTION_KEYS)
        if unknown:
            names = ", ".join(sorted(unknown))
            raise _invalid(f"Unknown target option(s): {names}; use github and open_collective")
        return targets_from_options(targets.get("github"), targets.get("open_collective"))
    if isinstance(targets, str):
        return targets_from_param(targets)
    return canonical_targets(t if isinstance(t, Target) else parse_target(t) for t in targets)


def targets_param(targets: Iterable[Target]) -> str:
    """The canonical target param: the canonical set joined with ``,``."""
    return ",".join(str(t) for t in canonical_targets(targets))


def targets_hash(targets: Iterable[Target]) -> str:
    """Lowercase hex SHA-256 of the UTF-8 target param (used for storage keys)."""
    return hashlib.sha256(targets_param(targets).encode("utf-8")).hexdigest()
