# Harness Eval: Correctness (Track A)

> Generated: 2026-09-12T03:58:14.076242+00:00
> Method: deterministic path/command checks (no README)

## What these words mean

| Word | Meaning | You should |
|------|---------|------------|
| **BROKEN** | A cited path or command does not exist (high-precision check) | Fix the cite or restore the file |
| **OK path-cites** | Concrete path cites that resolved | No action |
| **T0 / T1 / T2** | Always-on rules / skills / cited harness refs | Fix T0 cites first (always loaded) |

This track answers: *is the harness factually wrong about paths/commands?* Not redundancy (`07`) or usefulness (`10`).

## Executive summary

- T0: 1 · T1: 2 · T2: 4
- Manifests: package.json
- Findings: **10 broken** · 9 path-cites ok

## Inventory

### T0

Always-on rules (always loaded).

- `AGENTS.md`

### T1

Skills.

- `.claude/skills/harness-eval/SKILL.md`
- `.claude/skills/SKILL.md`

### T2

Cited harness refs.

- `.claude/skills/harness-eval/references/GLOSSARY.md`
- `.claude/skills/harness-eval/references/PROTOCOL.md`
- `.claude/skills/harness-eval/references/claims.schema.json`
- `.claude/skills/harness-eval/references/judge-prompts.md`

## Findings

### [A001] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/SKILL.md`
- **The instruction cites:** `.agents/skills`
- **Looked for:** `.agents/skills` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A002] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/SKILL.md`
- **The instruction cites:** `.cursor/skills`
- **Looked for:** `.cursor/skills` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A003] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/SKILL.md`
- **The instruction cites:** `lib/...`
- **Looked for:** `lib/...` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A004] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/SKILL.md`
- **The instruction cites:** `test/...`
- **Looked for:** `test/...` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A005] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/SKILL.md`
- **The instruction cites:** `.agents/...`
- **Looked for:** `.agents/...` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A007] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/SKILL.md`
- **The instruction cites:** `.agents/…`
- **Looked for:** `.agents/…` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A008] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/references/PROTOCOL.md`
- **The instruction cites:** `.agents/skills`
- **Looked for:** `.agents/skills` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A009] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/references/PROTOCOL.md`
- **The instruction cites:** `.cursor/skills`
- **Looked for:** `.cursor/skills` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A010] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/references/PROTOCOL.md`
- **The instruction cites:** `bin/console`
- **Looked for:** `bin/console` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

### [A011] BROKEN — missing file

- **In:** `.claude/skills/harness-eval/references/PROTOCOL.md`
- **The instruction cites:** `references/view.md`
- **Looked for:** `references/view.md` at the repo root (case-sensitive)
- **Fix:** Point the cite at a path that exists, or restore the missing file.

## Notes

- Path normalization preserves `.agents` (never `str.lstrip('./')`).
- Placeholders and bare example filenames are skipped.
- Fenced code blocks are not scanned for path cites.
- `references/` may resolve under a skill named in the same surface (e.g. load `dev`).
- Missing `app/`/`lib/`/`test/` cites are BROKEN only when mandate language is nearby.
