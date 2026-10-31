# Findings — Claude Mem compatibility audit

Date/time: 2026-09-25 08:50:27 -0400

## Executive summary

The upstream plugin `thedotmack/claude-mem` is a real Claude Code memory plugin designed to persist across sessions, compress context, and inject memory back into future sessions. Based on the public README, the project does the following:

- installs via Claude Code plugin commands (`/plugin marketplace add thedotmack/claude-mem` and `/plugin install claude-mem`)
- installs lifecycle hooks and a worker service
- stores observations in SQLite and optionally vector search data
- runs in the user home profile, not inside the repository itself
- expects Node.js 20+ and Bun

This repository already contains a Claude Code harness structure under `.claude/`, with agents, commands, skills, and hooks, so the plugin is conceptually compatible. However, the repository does not currently install or configure the plugin locally, and there is no repo-scoped memory contract in place.

## What the repo already has

This repo already has the key structural elements that make a memory plugin plausible:

- `.claude/settings.json` with hook configuration
- `.claude/agents` with specialized agents and review roles
- `.claude/commands` with spec and validation workflows
- `.claude/skills` with procedural skills for harness evaluation and spec work
- `.github/workflows/ci.yml` with validation jobs
- `scripts/gate-check.js` and `scripts/post-edit-check.js` as guardrails

This means the repo is already prepared to benefit from a session-memory plugin, but not yet configured to use one.

## What is missing for direct plugin adoption

The upstream plugin is not an in-repo dependency. It is an external installation that configures runtime behavior in the local Claude Code environment. The follow-up gaps in this repo are:

- no repo-local plugin manifest or installation script referencing `claude-mem`
- no local `~/.claude-mem/settings.json` in the current environment (not visible here)
- no persisted memory datastore or memory policy contract in the repo
- no memory retention/privacy caps documented for project artifacts
- no memory-specific schema under `schemas/` or memory-specific tests

## Compatibility assessment

Compatibility verdict: positive, but only at the environment/ops level, not as a repository-native integration.

Why it is compatible:

- the repo is already a Claude Code-specific harness
- the plugin targets Claude Code lifecycle hooks and session continuity
- the repo already has hooks and command flows that would benefit from persistent context continuity

Why it is not repo-native yet:

- this repo is a spec/harness repo, not a deployed app; its memory use should be explicitly policy-bounded
- the plugin writes outside the repo, so the repo alone cannot enforce memory behavior without governance
- without a project-level retention/privacy document, memory can become a compliance risk

## Key risks to flag before installing

1. Memory persistence is outside the repo, so local repo governance does not automatically apply.
2. Sensitive or secret data can be accidentally captured if the plugin stores all tool use without filtering.
3. The plugin can increase context injection silently; it should be scoped by project or by session, not global by default.
4. The repo already has a strong rules layer; memory should not bypass those state/decision controls.

## Recommended safe path

The safest path is not to add the plugin blindly. Prefer this rollout:

1. Review the upstream plugin docs and decide whether memory is desired for this repo.
2. Install it only in a local Claude Code environment used for this repo.
3. Add a project policy describing what should and should not be stored in memory.
4. Keep the repo itself free of raw memory artifacts and runtime state.
5. Use the plugin only as a supplemental context layer, not as an authority over governance decisions.

## Conclusion

The plugin is compatible with the project's Claude Code setup and likely useful for long-lived session continuity, but it should be treated as an environment-level augmentation rather than a repo-native feature. It should be enabled carefully, with an explicit privacy/retention policy and with awareness that the repo's governance and hooks are already strict.
