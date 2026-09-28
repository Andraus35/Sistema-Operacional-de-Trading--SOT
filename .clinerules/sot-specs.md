---
description: Rules for editing or creating SOT agent spec files. Apply when modifying specs/, governance/RULES.md, governance/CONSTITUTION.md, or governance/CONFLICT-MAP.md.
globs: ["specs/*.spec.md", "governance/RULES.md", "governance/CONSTITUTION.md", "governance/CONFLICT-MAP.md"]
paths: ["specs/*.spec.md", "governance/RULES.md", "governance/CONSTITUTION.md", "governance/CONFLICT-MAP.md"]
alwaysApply: false
---

# SOT Spec Editing Rules

## EARS notation requirement

All behavioral acceptance criteria MUST use EARS notation:
```
Quando <condição observável>, o agente DEVE <resposta específica>.
```

Never use vague language like "should handle" or "may consider".

## Source citation requirement

Every rule in RULES.md must cite its source:
```
<!-- Fonte: ENGENHARIA GERAL Doc01 §3 -->
```

## Methodology hierarchy — never override

When writing spec behaviors, remember the inviolable hierarchy:
1. Elliott Wave (map — always first)
2. Fibonacci (geometric validation)
3. Fractal Confluence (multi-timeframe)
4. SMC (institutional confirmation)
5. ICT (execution only)

A lower-layer agent behavior CANNOT override a higher-layer agent's conclusions.

## Spec structure — mandatory sections

Every file in specs/ must contain:
- `## Missão` — single sentence stating what the agent does
- `## Escopo` — what the agent handles (including "Fora do escopo" non-goals)
- `## Comportamento esperado por situação` — EARS behavioral clauses
- `## Critérios de aceitação` — testable acceptance criteria
- `## Inputs que recebe` — reference to input schema
- `## Outputs que entrega` — reference to output schema

## Constitutional non-negotiables

Never write spec behaviors that would violate these:
- ICT INACTIVE unless `approved_hypothesis` is non-null
- Signal blocked when `directional_conflict = true`
- R:R < 1:3 (risk:reward) always blocks execution (Q-004)
- Conviction global < 70% always blocks signal (Pilot-Phase threshold, recalibrable — Q-002)
