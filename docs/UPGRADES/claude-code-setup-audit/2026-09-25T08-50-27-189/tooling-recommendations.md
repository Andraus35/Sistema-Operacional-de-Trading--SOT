# Recommendations — Claude Mem for this repo

Date/time: 2026-09-25 08:50:27 -0400

## Recommended tool stack

| Capability | Recommendation | Why |
| --- | --- | --- |
| Session memory | `claude-mem` | Best fit for Claude Code persistent context across sessions |
| Repo guardrails | existing `.claude/settings.json` hooks + `scripts/gate-check.js` | Keeps memory from bypassing governance |
| Project validation | `npm test`, `npm run lint`, `python scripts/validate_spec_sot.py ...` | Ensures spec and schema guardrails remain intact |
| Memory safety review | manual policy doc + optional retention script | Prevents secret or sensitive data capture |
| Agent support | existing `.claude/agents` and `.claude/skills` | Plugin complements the harness, not replaces it |

## Recommended operating model

- Keep the plugin installed at the user/IDE level, not as a repo dependency.
- Use it strictly for long-lived context under a project-specific policy.
- Do not let memory records override constitutional or rule-based decisions in the repo.
- Keep raw memory data out of the Git working tree and out of generated artifacts.

## Minimal policy checklist before enabling

- [ ] Decide what types of data are allowed in memory (project decisions, bug fixes, rationale, not secrets)
- [ ] Define what is excluded (API keys, tokens, private URLs, user-specific secrets)
- [ ] Set retention period and purge policy
- [ ] Define whether memory applies project-wide or only to this repo
- [ ] Confirm plugins do not rewrite or disable existing repo hooks

## Suggested tooling additions

1. Add a project policy document:
   - `docs/memory-policy.md` or equivalent
   - include allowed sources, excluded sources, retention, and review cadence

2. Add a memory-safe hook script (optional, future):
   - inspect tool observations before writing to memory
   - block secrets and private data by regex/keys

3. Add a minimal audit checklist:
   - before/after plugin install log verification
   - check that `.claude/settings.json` still resolves and guardrails remain active

## Decision

For this repo, the best fit is: use the plugin only as an optional session continuity layer for the local Claude Code environment, not as a required repository feature. It is useful, but only with explicit governance and privacy boundaries.
