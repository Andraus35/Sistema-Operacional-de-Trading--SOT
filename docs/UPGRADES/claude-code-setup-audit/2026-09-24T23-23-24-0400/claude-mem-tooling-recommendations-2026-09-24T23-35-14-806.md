# Ferramentas e recomendações — Claude Memory (Claude Mem)

Execução: 2026-09-24 23:35:14 -0400

Este documento propõe ferramentas e passos a adotar para operacionalizar uma camada de memória segura e testável no SOT Harness. Nenhuma alteração foi feita no repositório.

## Objetivos do plugin de memória
- Persistir fatos relevantes (evidências, hipóteses aprovadas/refutadas, eventos de Blackboard) de forma versionada e audível.
- Expor APIs de consulta com filtros por namespace, timescale e propósito (Synthesis, Hypothesis Registry, RAG).
- Aplicar políticas de retenção, anonimização, e expurgo programático.
- Integrar com schemas já existentes (`schemas/*.json`) para garantir compatibilidade.

## Componentes recomendados

1) Manifesto do plugin (ex.: `.claude/plugins/claude-mem.json`)
   - Campos: name, version, description, author, entry_point, required_env, permissions, retention_defaults
   - Permite discovery e instalação controlada.

2) Memory schema(s)
   - Reuse `schemas/` folder. Add `schemas/memory.record.json` with draft-07 JSON Schema describing record shape, required fields (id, type, source, timestamp, payload, metadata), and `additionalProperties: false`.
   - Provide `schemas/memory.query.json` for query params and response shape.

3) Guardrail hooks
   - Extend `.claude/settings.json` hooks with memory-specific PreToolUse handler to inspect writes and a PostToolUse handler to run quick scans (PII detection, retention ranges).
   - Hook scripts: `scripts/memory-gate.js` and `scripts/memory-post-check.js`.

4) CLI commands / skills
   - Add `.claude/commands/memory-manage.md` with workflows to seed, purge, and export memory slices for audits.
   - Expose a SKILL.md under `.claude/skills/memory/SKILL.md` describing human-triggered memory operations.

5) Tests and CI
   - Add unit tests under `tests/memory/` that use existing `npm test` runner or a small test runner to validate schema conformance and retention behaviors.
   - Add a CI job that runs memory tests and a quick smoke integration test using a local ephemeral store (e.g., file-backed JSONL) to avoid external service dependencies.

6) Storage backend options (choose one depending on infra)
   - Minimal dev: file-backed append-only JSONL in `data/memory/` (access restricted in .gitignore).
   - Productionable option: Postgres (table memory_records) or vector DB (for semantic retrieval) + metadata in SQL.
   - If vector DB used: store vectors separately and reference canonical JSON record ids for auditability.

7) Privacy and encryption
   - Require `node_extra_ca_certs` or env var driven certificate paths if operating behind enterprise proxies.
   - Enforce at-rest encryption and role-based access control in production backends.

## Suggested priorities (minimal safe rollout)
1. Draft `memory.record` and `memory.query` schemas and add tests.
2. Add a manifest file and a SKILL.md describing the plugin and its allowed operations.
3. Implement file-backed dev memory store + CLI to seed/purge/export; wire PreToolUse/PostToolUse hooks to validate writes.
4. Add CI job that runs memory unit tests and smoke integration.
5. If stable, implement production backend (Postgres or managed vector DB) and migration tooling.

## Example minimal manifest fields
```
{
  "name": "claude-mem",
  "version": "0.1.0",
  "description": "Local memory plugin for SOT Claude agents (dev only)",
  "entry_point": "./plugins/claude-mem/index.js",
  "permissions": ["read:memory", "write:memory", "delete:memory"],
  "retention_defaults": {"default_days": 365, "pii_masking": true}
}
```

## Tests to include
- Schema validation for memory records and queries.
- Hooks: memory-gate blocks records with forbidden fields or secrets.
- Retention: records older than retention policy are purged by purge job.
- Access control: enforce read/write/delete permission checks.

## Operational notes
- Do not commit actual memory data to Git. Add `data/memory/` to `.gitignore` and store dumps only in secure artifact storage.
- Add documentation in `reference/camadas/CAMADA MEMÓRIA.MD` referencing the manifest and schemas.

## Decision guide
- If the team wants an operational memory for local testing only: implement minimal file-backed store and CI smoke tests.
- If the team needs production-grade memory: design schema-first, choose a backing store, and ensure encryption and RBAC are included in the first PR.

---

End of recommendations. No repository files were changed by this audit.
