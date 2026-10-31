# Harness Eval: Correctness (Track A)

> Generated: 2026-10-31T14:29:45.693287+00:00
> Method: deterministic path/command checks (no README)

## What these words mean

| Word | Meaning | You should |
|------|---------|------------|
| **BROKEN** | A cited path or command does not exist (high-precision check) | Fix the cite or restore the file |
| **OK path-cites** | Concrete path cites that resolved | No action |
| **T0 / T1 / T2** | Always-on rules / skills / cited harness refs | Fix T0 cites first (always loaded) |

This track answers: *is the harness factually wrong about paths/commands?* Not redundancy (`07`) or usefulness (`10`).

## Executive summary

- T0: 1 · T1: 0 · T2: 0
- Manifests: package.json
- Findings: **0 broken** · 4 path-cites ok

## Inventory

### T0

Always-on rules (always loaded).

- `AGENTS.md`

### T1

Skills.

_(none)_

### T2

Cited harness refs.

_(none)_

## Findings

_No BROKEN path/command findings._
## Notes

- Path normalization preserves `.agents` (never `str.lstrip('./')`).
- Placeholders and bare example filenames are skipped.
- Fenced code blocks are not scanned for path cites.
- `references/` may resolve under a skill named in the same surface (e.g. load `dev`).
- Missing `app/`/`lib/`/`test/` cites are BROKEN only when mandate language is nearby.
