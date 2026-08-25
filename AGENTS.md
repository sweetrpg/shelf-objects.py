# AGENTS.md

This file provides guidance to Claude Code, Codex, GitHub Copilot, and other coding agents
working in this repository.

## About This Project

`game-room-objects.py` defines the persistence models and API value objects for the Game Room microservice's domain: library, wishlist, table, visibility.

Currently a scaffold; no implementation yet since game-room-api is migrating to Go. This repo mirrors the structure of other language implementations under the `foundational/game-room-objects` umbrella in `sweetrpg/platform` (Go, Rust, Swift) — keep behavior consistent with those where the concept overlaps, but don't assume identical APIs; each follows its language's own conventions.

## Committing Code

[Conventional Commits](https://www.conventionalcommits.org/): `<type>(<scope>): <description>`.

## Branches and Workflow

Git-flow (see `docs/git-flow.md` in `sweetrpg/platform`): `develop` is the integration branch,
`master` reflects the latest release. Feature/fix branches off `develop`, PR back into `develop`.

## Running Checks Locally

```bash
make init
make test
```

Or directly with tox:

```bash
tox
```
