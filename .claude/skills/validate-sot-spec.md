---
name: validate-sot-spec
description: Use when you need to validate a SOT agent spec file for completeness, EARS notation compliance, and constitutional rule adherence. Checks mandatory sections, source citations, and antiescopo declarations.
---

# Validate SOT Agent Spec

## Purpose

Validates that a spec file in `specs/` conforms to the SOT harness standards.

## Steps

1. **Check mandatory sections**: verify the file has Missão, Escopo, Antiescopo, Comportamentos, and Critérios de aceitação.

2. **Check EARS notation**: every acceptance criterion must match the pattern:
   `Quando <condição>, o agente DEVE <resposta>.`

3. **Check source citations**: every rule reference must cite source document.

4. **Check constitutional compliance**:
   - If the agent is ICT Specialist: verify ICT INACTIVE rule is listed as first behavior
   - If the agent is Synthesis Agent: verify signal conditions include all 4 guards (score≥7/9, R:R≥1:3, conviction≥70%, no directional conflict). Note: 70%/7-9 are Pilot-Phase thresholds (Q-002); R:R is 1:3 (Q-004).
   - No spec behavior may override a higher-layer agent in the methodology hierarchy

5. **Check antiescopo**: the Antiescopo section must explicitly list at least 5 things the agent never does, with "→ responsabilidade de [other agent]" attribution.

6. **Report**: for each failed check, state the section, the rule violated, and the fix required.
