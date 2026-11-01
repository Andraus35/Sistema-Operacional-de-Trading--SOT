# Proposta A4 — Proporcionalidade: abertura e Plan em ciclo único (medida antes de cortar)

> **Não normativo. PROPOSTA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A4. Mexer em `atomic-spec.md §15` ou `ROADMAP.md §23` (reservados) exige ordem de Andraus. Não fecha decisão aberta (CONS-01).

## 1. Medição ao vivo (HEAD `f1f3339`)
| Item | Dado | Fonte |
|---|---|---|
| Complexidade das 14 Specs em `specs/features/` | **14 de 14 são HIGH ou CRITICAL** (CRITICAL: 001, 002, 003, 004, 006, 007, 020, 048; HIGH: 005, 019, 021, 038, 046, 049); **0 LOW, 0 MEDIUM** | cabeçalho de cada `plan.md` |
| Slots futuros do ROADMAP com perfil declarado | **1 MEDIUM** (linha 254, D0–D5), **0 LOW**, 15 HIGH/CRITICAL (3 CRITICAL D0–D7 · 3 CRITICAL D0–D8 · 1 CRITICAL D0–D9 · 5 HIGH D0–D7 · 3 HIGH D0–D8). Slots são **indicativos** (RULE-ECC-01) | `grep` no ROADMAP |
| Custo SPEC-049 (tokens de subagentes) | abertura **906.237** (≈ 39 %) · Plan **1.389.735** (≈ 61 %) | HANDOFF HO-131 §2 |
| Achados da abertura por rodada | SPEC-049: Médias 1→0→0, Menores 8→2→1 · SPEC-048: 0 Médias, Menores 10→7 · SPEC-007: 3 rodadas, 0/0/0 no ledger | `LEDGER-ACHADOS.md`, retrospectiva SPEC-049 |
| Telemetria por rodada | **n/m** (arquivo local sem registro por Spec neste ambiente) | `telemetria_tokens.py custo-beneficio` |

## 2. Achados
1. **A premissa do A4 quase não tem população.** Proporcionalidade para LOW/MEDIUM beneficiaria **≈ 1 de 16** Specs (a única MEDIUM do ROADMAP), e nenhuma das 14 já feitas. A mudança exigiria emenda em dois arquivos reservados para poupar uma Spec indicativa.
2. **Já é possível sem regra nova.** Número, fronteira e perfil são definidos **na abertura**, por proposta do Especificador e homologação de Andraus (RULE-ECC-01/02). Para a Spec MEDIUM, Andraus pode escolher ali um Dossiê enxuto e o perfil D0–D5 sem alterar `atomic-spec`.
3. **O custo concentra-se em HIGH/CRITICAL, não em LOW/MEDIUM.** Nas três aberturas medidas, só a **R1** achou Média (1 na SPEC-049); as rodadas seguintes trouxeram Menores. A economia plausível está em **parar a abertura quando uma rodada fecha com 0 Média**, não em fundir abertura e Plan. Isso é exatamente a **regra de parada do P10** (experimento já aprovado por Andraus, a rodar no próximo Plan).
4. **Fundir abertura e Plan tem risco de Eficácia**: a abertura existe para Andraus decidir escopo e perguntas (ex.: P-1..P-7 da SPEC-049) **antes** de gastar o Plan; achados do Revisor não medem esse valor. Cascata observada: a divisão da SPEC-007 (Opção C) mudou o escopo no meio do Plan — o contrário do que se quer fundir.

## 3. Opções
| Opção | Ganho medido | Risco |
|---|---|---|
| A4 como na auditoria (LOW/MEDIUM em ciclo único) | ≈ 1 Spec em 16, não medido | Emenda a `atomic-spec §15` e ROADMAP §23 (reservados) por ganho marginal |
| **A4-b: tratar no P10** — estender a regra de parada à abertura e medir tokens por rodada de abertura no próximo Plan | Atinge as Specs que de fato custam (HIGH/CRITICAL; abertura ≈ 39 % dos tokens na SPEC-049) | Baixo: já aprovado como experimento; sem mudança de norma até haver dado |
| Não fazer | 0 | Custo atual permanece |

## 4. Recomendação
**A4-b.** Não alterar norma agora: registrar a abertura como alvo de medição do experimento P10 (tokens por rodada, Médias por rodada, decisão de parar em 0 Média) e, se a Spec MEDIUM do ROADMAP vier a ser aberta, Andraus escolhe o perfil enxuto na própria abertura. Depende de ordem dele; nada foi criado.

## 5. Declarado
Complexidade lida do cabeçalho de cada `plan.md` (primeira ocorrência de "Complexidade"); para SPEC-004/005 e outras, confiei nessa leitura e não reabri o texto. O 0/0/0 da abertura da SPEC-007 vem do ledger e pode refletir pareceres antigos sem bloco estruturado (não conferi). Tokens por rodada não medidos (telemetria local vazia); só os dois totais do HANDOFF. n pequeno (3 aberturas).
