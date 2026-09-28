# Harness Eval: Judge Agreement (Track B)

> Run dir: `C:\Users\André\Desktop\ORYX AGENT\SOT-Harness\.harness-eval\runs\2026-09-11-full`
> Trap gate: FAIL (misses=2)
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

- Real claims scored: 190
- Ship: **0**
- Review: **186**
- Hold: **4**
- Trap misses: [{'id': 'P003', 'expected': 'REDUNDANT', 'got': 'KEEP'}, {'id': 'P004', 'expected': 'REDUNDANT', 'got': 'KEEP'}]

## Discrimination (plants)

| ID | Expected family | J2 family |
|----|-----------------|-----------|
| P001 | REDUNDANT | REDUNDANT |
| P002 | REDUNDANT | REDUNDANT |
| P003 | REDUNDANT | KEEP |
| P004 | REDUNDANT | KEEP |
| P005 | KEEP | KEEP |
| P006 | KEEP | KEEP |

Ship by tier: {}
Hold by tier: {'T1': 4}

## Ship

| ID | Tier | Source | J1 | J2 cost/class | Quote |
|----|------|--------|----|---------------|-------|

## Hold

| ID | Tier | Reason | J1 | J2 | Quote |
|----|------|--------|----|----|-------|
| C098 | T1 | disagree | KEEP-COMPRESSED | 1/REDUNDANT-GENERAL | **Princípio C (contexto):** contexto é recurso escasso. Dê ao modelo exatamente a |
| C099 | T1 | disagree | KEEP-COMPRESSED | 1/REDUNDANT-GENERAL | informação certa em cada passo — posição importa tanto quanto presença. |
| C100 | T1 | disagree | KEEP-COMPRESSED | 1/REDUNDANT-GENERAL | **Princípio T (ferramentas):** "menos ferramentas, porém melhores". Se você não |
| C101 | T1 | disagree | KEEP-COMPRESSED | 1/REDUNDANT-GENERAL | consegue explicar quando uma ferramenta se aplica, o modelo também não conseguirá. |

## Review (KEEP family)

186 claims. See J1/J2 score tables for detail.

## Action guidance

- **T0 Ship:** edit always-on rules now.
- **T1 Ship:** skill cleanup backlog.
- **T2 Ship:** routing/pointer hygiene.
- **Hold:** do not trim.

