# Harness Eval: Judge Agreement (Track B)

> Run dir: `.claude\skills\harness-eval\runs\2026-09-26-full`
> Trap gate: PASS (misses=0)
> Bands: Ship = dual REDUNDANT + J2 cost≤1; Review = dual KEEP; Hold = disagree / missing

## What these words mean

| Word | Meaning | You should |
|------|---------|------------|
| **Ship** | Both judges: text is redundant and cheap to rediscover | Delete / trim |
| **Review** | Both judges: keep (not redundant) | Leave alone |
| **Hold** | Judges disagreed or score missing | Do nothing yet |
| **Trap PASS** | Planted traps scored correctly | Trust Ship |

This track answers: *would an agent rediscover this without the harness?* Not the same as usefulness (`10-usefulness-agreement.md`).

## Executive summary

- Real claims scored: 313
- Ship: **20**
- Review: **290**
- Hold: **3**
- Trap misses: none

## Discrimination (plants)

| ID | Expected family | J2 family |
|----|-----------------|-----------|
| P001 | REDUNDANT | REDUNDANT |
| P002 | REDUNDANT | REDUNDANT |
| P003 | REDUNDANT | REDUNDANT |
| P004 | REDUNDANT | REDUNDANT |
| P005 | KEEP | KEEP |
| P006 | KEEP | KEEP |

Ship by tier: {'T0': 2, 'T1': 18}
Hold by tier: {'T0': 1, 'T1': 2}

## Ship

| ID | Tier | Source | J1 | J2 cost/class | Quote |
|----|------|--------|----|---------------|-------|
| C001 | T0 | `AGENTS.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | Arquivo de configuração e contexto lido por todo agente ao iniciar. |
| C002 | T0 | `AGENTS.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | Define identidade, mapa do repositório, profiles, paths, fluxo e não-negociáveis. |
| C067 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/references/PROTOCOL.md` |
| C068 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/inventory_extract.py` |
| C069 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/track_a_correctness.py` |
| C070 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/merge_agreement.py` |
| C071 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/surfaces_extract.py` |
| C072 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/merge_usefulness.py` |
| C073 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/slim_fanin.py` |
| C074 | T1 | `.claude/skills/harness-eval/SKILL.md` | REDUNDANT-CODE | 1/REDUNDANT-CODE | `$SKILL_DIR/scripts/doc_scope.py` |
| C113 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | **Princípio C (contexto):** contexto é recurso escasso. Dê ao modelo exatamente a |
| C114 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | informação certa em cada passo — posição importa tanto quanto presença. |
| C115 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | **Princípio T (ferramentas):** "menos ferramentas, porém melhores". Se você não |
| C116 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | consegue explicar quando uma ferramenta se aplica, o modelo também não conseguirá. |
| C117 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | **Default: centralizar.** Um fluxo único, linear, com contexto compartilhado |
| C118 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | resolve a maioria dos problemas sem o custo de 4-15× tokens dos sistemas multiagentes. |
| C165 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-CODE | 0/REDUNDANT-CODE | **Validar JSON schemas**: `node tests/validate-schemas.js` — todos os schemas devem passar |
| C166 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-CODE | 0/REDUNDANT-CODE | **Lint specs**: `node tests/lint-specs.js` — todos os 5 specs devem passar EARS + sections |
| C176 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-CODE | 0/REDUNDANT-CODE | **Rodar harness-score**: `npx harness-score` — manter L2 ou superior |
| C182 | T1 | `.claude/skills/SKILL.md` | REDUNDANT-GENERAL | 1/REDUNDANT-GENERAL | ✓ completo \| △ parcial \| ✗ ausente \| N/A não aplicável \| **✗** crítico ausente |

## Hold

| ID | Tier | Reason | J1 | J2 | Quote |
|----|------|--------|----|----|-------|
| C003 | T0 | disagree | REDUNDANT-GENERAL | 1/UNCLEAR | Consolidação única (2026-09-14): substitui a antiga dupla `AGENTS.md` + `AGENTSV2.md`. |
| C066 | T1 | disagree | KEEP-ROUTING | 1/REDUNDANT-GENERAL | Set `SKILL_DIR` to the directory containing this `SKILL.md`. Verify: |
| C140 | T1 | disagree | REDUNDANT-GENERAL | 1/KEEP-COMPRESSED | Ela torna o EARS notation plenamente rastreável e testável. |

## Review (KEEP family)

290 claims. See J1/J2 score tables for detail.

## Action guidance

- **T0 Ship:** edit always-on rules now.
- **T1 Ship:** skill cleanup backlog.
- **T2 Ship:** routing/pointer hygiene.
- **Hold:** do not trim.

