# Auditoria: Claude Memory (Claude Mem) — execução 2026-09-24 23:35:14 -0400

**Escopo:** levantamento somente leitura para localizar evidências de plugin/manifest de "Claude Mem" (memória) e avaliar integração com o harness existente. Nenhum arquivo do repositório foi alterado.

## Resumo executivo

- Não foi encontrado um manifesto explícito de plugin chamado `claude-mem`, `claude-memory` ou `memory-plugin` no repositório.
- Há documentação e artefatos que tratam da camada de memória/camada memória:
  - [CAMADA MEMÓRIA.MD](C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/reference/camadas/CAMADA%20MEM%C3%93RIA.MD)
  - referências transversais em `atomic-spec.md`, `ROADMAP.md` e em skills/agents (`.claude/agents/especificador.md`, `.claude/skills/SKILL.md`).
- Hooks, skills e gate scripts existem (`.claude/settings.json`, `scripts/gate-check.js`, `scripts/validate_spec_sot.py`) mas não foi detectado hook ou script específico para persistência/evicção de memória.
- Recomenda-se documentar e, se necessário, adicionar um manifesto/contrato de memória com políticas de retenção, I/O schema e testes antes de habilitar qualquer "memory" plugin para agentes.

## Files/paths of interest (search hits)
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/reference/camadas/CAMADA%20MEM%C3%93RIA.MD
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/.claude/agents/especificador.md
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/.claude/agents/revisor.md
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/.claude/skills/SKILL.md
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/specs/features/SPEC-019/plan.md
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md
- C:/Users/Andr%C3%A9/Desktop/SOT%20ENGINER/SOT-Harness/atomic-spec.md

(Note: paths above are exact matches from repository search; open them to review details.)

## Key findings

1) No explicit Claude Memory plugin manifest

   - Evidence: repository-wide search did not show files named `claude-mem*`, `memory-plugin.*`, `.claude-plugin` manifest, or similar.
   - Impact: there is no packaged memory plugin to install or to import by the current Claude Code harness; memory functionality appears to be specified conceptually in docs and harness specs rather than packaged.

2) Memory layer documented but not operationalized

   - Evidence: `reference/camadas/CAMADA MEMÓRIA.MD` exists and is clearly the canonical doc for memory layer; however no plugin or schema files were found that implement runtime memory persistence or retrieval APIs.
   - Impact: agents may refer to memory as a concept but will not have a standardized, testable memory service without additional artifacts.

3) Hooks and guardrails present, but no memory-specific hooks

   - Evidence: `.claude/settings.json` defines PreToolUse/PostToolUse hooks; hook scripts exist (gate-check, post-edit-check). No hook referencing memory storage or memory eviction policies was found.
   - Impact: enabling a memory plugin later should be accompanied by additional guardrail hooks (e.g., pre-write consent, PI/secret filter, retention checks).

4) Schemas and synthesis inputs/outputs exist

   - Evidence: `schemas/synthesis.input.json` and `schemas/synthesis.output.json` are present. These can be extended or referenced by a memory plugin to ensure consistent I/O between memory and agents.
   - Impact: good base for integration tests and schema-driven memory records.

## Recommended immediate (non-destructive) next steps

- Document the intended memory plugin contract (manifest) in `reference/` and in `.claude/` (SKILL.md or a new command) before implementing any runtime memory plugin.
- Create a small `memory-spec.md` (D2–D4) that includes: memory record schema, retention policy, access control rules, and enforcement contract (preconditions/postconditions) — use `atomic-spec.md` template.
- Add memory-related hooks to `.claude/settings.json` only after the contract is agreed; hooks should call scripts that validate memory writes for PII, retention, and policy.
- Add unit tests that exercise memory I/O using existing `npm test` or a small test harness referencing `schemas/`.

## Security & privacy notes

- Any memory persistence must follow repository-wide rules on secrets and environment variables. Do not commit secrets in memory artifacts. Consider encryption-at-rest and access controls for persisted memories.

## Conclusion

No changes were made to the repo. There is clear conceptual coverage of memory in documentation, but no packaged Claude Memory plugin found. Recommend formalizing the memory contract and adding tests and guardrail hooks before enabling runtime memory features.
