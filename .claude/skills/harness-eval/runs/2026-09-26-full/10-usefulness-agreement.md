# Harness Eval: Usefulness Agreement (Track C)

> Run dir: `C:\Users\André\Desktop\SOT ENGINER\SOT-Harness\.claude\skills\harness-eval\runs\2026-09-26-full`
> Trap gate: PASS (misses=0)
> Fan-in gate: PASS (slim-fanin-blocked=0)
> Judges: J1 model=`claude-sonnet-5` · J2 model=`claude-sonnet-5`
> Bands: Slim = dual SLIM/ROUTING + trap PASS + fan-in PASS; Keep-core = dual KEEP-CORE; Mixed = dual MIXED; Hold = disagree / unclear / missing / slim-fanin-blocked
> **Model-sensitive:** re-judge on a second model before large Slim deletes.
> **Fan-in:** another harness surface hard-loads this path as SoT → Hold, not Slim.
> **Mixed apply:** use `11-mixed-apply.md` only — do not re-judge from this table alone.

## What these words mean

| Word | Meaning | You should |
|------|---------|------------|
| **Keep-core** | Most of the file changes agent behavior | Do **not** slim |
| **Mixed** | Real rules + large theory/examples/overlap | Keep rules; cut bulk — follow `11-mixed-apply.md` |
| **Slim** | Mostly theory / repo-demo / overlap, **and** no other harness surface hard-loads it | Compress or delete body |
| **Hold** | Judges disagreed, unclear, or Slim blocked by fan-in | Do nothing yet (or update consumers first) |
| **Trap PASS** | Planted traps scored correctly | Necessary but not sufficient for Slim |
| **Fan-in blocked** | Another harness file mandates loading this path / treats it as SoT | Do **not** stub/delete until consumers are updated |

This track answers: *does deleting this change agent behavior?* Not the same as redundancy (`07-agreement.md`).

## Executive summary

- Real surfaces scored: 22
- Slim: **0**
- Keep-core: **12**
- Mixed: **1** → apply plan: `11-mixed-apply.md`
- Hold: **9** (fan-in blocked: 0)
- Trap misses: none

## Discrimination (plants)

| ID | Expected family | J2 family |
|----|-----------------|-----------|
| S901 | SLIM | SLIM |
| S902 | SLIM | SLIM |
| S903 | KEEP-CORE | KEEP-CORE |

Slim by tier: {}
Keep-core by tier: {'T0': 1, 'T2': 11}
Mixed by tier: {'T1': 1}
Hold by tier: {'T1': 2, 'T2': 7}

## Slim (compress / delete body candidates)

| ID | Tier | Name | Path | J1 | J2 |
|----|------|------|------|----|----|

## Slim fan-in blocked (do not stub/delete)

Dual SLIM/ROUTING-ONLY, but another harness surface hard-loads the path (load/SoT/extract mandate). Update or drop those consumers before Slim apply.

| ID | Path | Citers |
|----|------|--------|
| — | — | none |

## Keep-core

| ID | Tier | Name | Path | J1 | J2 |
|----|------|------|------|----|----|
| S001 | T0 | AGENTS.md | `AGENTS.md` | KEEP-CORE | KEEP-CORE |
| S005 | T2 | especificador.md | `.claude/agents/especificador.md` | KEEP-CORE | KEEP-CORE |
| S006 | T2 | revisor.md | `.claude/agents/revisor.md` | KEEP-CORE | KEEP-CORE |
| S008 | T2 | PROTOCOL.md | `.claude/skills/harness-eval/references/PROTOCOL.md` | KEEP-CORE | KEEP-CORE |
| S009 | T2 | judge-prompts.md | `.claude/skills/harness-eval/references/judge-prompts.md` | KEEP-CORE | KEEP-CORE |
| S013 | T2 | ROADMAP.md | `ROADMAP.md` | KEEP-CORE | KEEP-CORE |
| S014 | T2 | atomic-spec.md | `atomic-spec.md` | KEEP-CORE | KEEP-CORE |
| S017 | T2 | CATALOGO-OFICIAL.md | `governance/CATALOGO-OFICIAL.md` | KEEP-CORE | KEEP-CORE |
| S018 | T2 | CONFLICT-MAP.md | `governance/CONFLICT-MAP.md` | KEEP-CORE | KEEP-CORE |
| S019 | T2 | CONSTITUTION.md | `governance/CONSTITUTION.md` | KEEP-CORE | KEEP-CORE |
| S020 | T2 | GPR-001_Guia_Principios_Relacoes_SOT.md | `governance/GPR-001_Guia_Principios_Relacoes_SOT.md` | KEEP-CORE | KEEP-CORE |
| S022 | T2 | RULES.md | `governance/RULES.md` | KEEP-CORE | KEEP-CORE |

## Mixed (keep core, slim examples/theory)

Path list only. **Apply instructions:** `11-mixed-apply.md` (KEEP/CUT per ID).

| ID | Tier | Name | Path | J1 | J2 |
|----|------|------|------|----|----|
| S003 | T1 | skills | `.claude/skills/SKILL.md` | MIXED | MIXED |

## Hold

| ID | Tier | Reason | J1 | J2 | Path |
|----|------|--------|----|----|------|
| S002 | T1 | disagree | MIXED | KEEP-CORE | `.claude/skills/harness-eval/SKILL.md` |
| S004 | T1 | disagree | KEEP-CORE | UNCLEAR | `.claude/skills/sot-especificador-pap001/SKILL.md` |
| S007 | T2 | disagree | SLIM | UNCLEAR | `.claude/skills/harness-eval/references/GLOSSARY.md` |
| S010 | T2 | disagree | KEEP-CORE | ROUTING-ONLY | `.clinerules/sot-map.md` |
| S011 | T2 | disagree | MIXED | KEEP-CORE | `GLOSSARIO.md` |
| S012 | T2 | disagree | KEEP-CORE | MIXED | `RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md` |
| S015 | T2 | disagree | SLIM | MIXED | `backlog/BL-018-RISK-AGENT-backlog.md` |
| S016 | T2 | disagree | MIXED | SLIM | `docs/mapa/MAPA-PROJETO.md` |
| S021 | T2 | disagree | KEEP-CORE | UNCLEAR | `governance/PP-PAP-001_Pacote_Partida_Protocolo_Adesao_Progressiva.md` |

## Action guidance

- **Slim:** compress only after trap PASS **and** fan-in PASS; still human-approve; prefer re-judge on a second model if deleting >30% of a skill.
- **Slim fan-in blocked:** do **not** stub/delete; either keep the checklist body or update every citing harness surface in the same change, then re-merge.
- **Mixed:** open `11-mixed-apply.md` and execute KEEP/CUT per ID only. Do **not** re-judge. Do **not** replace KEEP snippets with `See app/...` or defer KEEP contracts to AGENTS.md. Empty Keep-core/Slim cells → skip that path.
- **Keep-core:** do not slim for usefulness reasons.
- **Hold:** no usefulness trim.
- See `08-usefulness-j1.md` / `09-usefulness-j2.md` for raw score rows.
- Fan-in detail JSON: `slim-fanin.json`.

