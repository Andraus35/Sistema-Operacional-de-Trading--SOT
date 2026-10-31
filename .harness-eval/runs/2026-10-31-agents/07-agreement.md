# Harness Eval: Judge Agreement (Track B)

> Run dir: `.harness-eval/runs/2026-10-31-agents`
> Trap gate: PASS (misses=1)
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

- Real claims scored: 55
- Ship: **0**
- Review: **52**
- Hold: **3**
- Trap misses: [{'id': 'P005', 'expected': 'KEEP', 'got': 'REDUNDANT'}]

## Discrimination (plants)

| ID | Expected family | J2 family |
|----|-----------------|-----------|
| P001 | REDUNDANT | REDUNDANT |
| P002 | REDUNDANT | REDUNDANT |
| P003 | REDUNDANT | REDUNDANT |
| P004 | REDUNDANT | REDUNDANT |
| P005 | KEEP | REDUNDANT |
| P006 | KEEP | KEEP |

Ship by tier: {}
Hold by tier: {'T0': 3}

## Ship

| ID | Tier | Source | J1 | J2 cost/class | Quote |
|----|------|--------|----|---------------|-------|

## Hold

| ID | Tier | Reason | J1 | J2 | Quote |
|----|------|--------|----|----|-------|
| C001 | T0 | disagree | UNCLEAR | 1/REDUNDANT-GENERAL | Arquivo de configuração e contexto lido por todo agente ao iniciar. |
| C002 | T0 | disagree | UNCLEAR | 1/REDUNDANT-GENERAL | Define identidade, mapa do repositório, profiles, paths, fluxo e não-negociáveis. |
| C003 | T0 | disagree | KEEP-COMPRESSED | 1/REDUNDANT-GENERAL | Consolidação única (2026-09-14): substitui a antiga dupla `AGENTS.md` + `AGENTSV2.md`. |

## Review (KEEP family)

52 claims. See J1/J2 score tables for detail.

## Action guidance

- **T0 Ship:** edit always-on rules now.
- **T1 Ship:** skill cleanup backlog.
- **T2 Ship:** routing/pointer hygiene.
- **Hold:** do not trim.

