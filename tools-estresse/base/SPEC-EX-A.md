# SPEC-EX-A — Porta de Risco do Signal Package (documento de teste)

| Campo | Valor |
|---|---|
| Complexidade | HIGH |
| Profundidade | <<REG-01|D0–D7|D0–D5>> |
| Profile | standard |
| Baselines de referência | CEE-001 v2.0, CHM-001, CCM-001 |
| Fonte de regras | governance/CONSTITUTION.md |

## 1. Objetivo
O Risk Agent recebe o TMP produzido pelo Manager Agent e decide se o sinal pode virar Signal Package. O SOT <<REG-02|não executa ordens; entrega o Signal Package ao Bot Trade Finance.|executa a ordem diretamente na corretora depois que o Risk Agent aprova.>>

O Risk Agent é acionado <<SEM-02|depois que o Manager emite o TMP|antes que o Manager emita o TMP>>, e nunca reescreve o TMP.

## 2. Requisitos (EARS)
- **R1.** WHEN o TMP chega, the Risk Agent SHALL rejeitar o sinal com R:R <<NUM-01|inferior a 3.0 (mínimo 1:3, sem exceção)|inferior a 2.0 (mínimo 1:2)>>.
- **R2.** IF `directional_conflict = true` entre Elliott e SMC, THEN o resultado SHALL ser <<REG-03|NEUTRO|o sinal do SMC, por ser a evidência mais recente>>.
- **R3.** WHEN a convicção for <<NUM-02|≥ 70%|≥ 60%>> e o score for <<NUM-03|≥ 7/9|≥ 5/9>>, o sinal SHALL ser elegível. Ambos são limiares de Fase Piloto, recalibráveis após backtest.
- **R4.** The Risk Agent SHALL expressar sua escala própria como <<SEM-01|"avaliação de risco", sem somar nem retroalimentar o Conviction Vector|"convicção de risco", somada ao Conviction Vector para ajustar o peso final>>.
- **R5.** O custo de execução <<REG-04|NUNCA entra|entra com peso de 5%>> no Conviction Vector (CEE-001 §10, Salvaguarda 4).
- **R6.** As salvaguardas de sinal estão em <<REF-01|CEE-001 §11|CEE-007 §11>>.

## 3. Decisões abertas relevantes
- A fórmula e os pesos definitivos do Conviction Vector <<REG-05|seguem em aberto (J-001)|estão fechados em 0,4/0,3/0,3 (J-001)>>.
- Esta Spec não fecha nenhuma decisão aberta.

## 4. Critérios de aceite
| Critério | Valor |
|---|---|
| R:R mínimo | <<NUM-04|3.0|2.5>> |
| Conviction Vector calculado | <<SEM-03|duas vezes por ciclo (macro na Fase 1, global na Fase 2)|uma única vez, ao final da Fase 2>> |
| Evidência (Agentes) e Observação (Skills) | <<REG-06|são coisas distintas|são tratadas como equivalentes>> |
| Validade do Dossiê de Pesquisa (HIGH) | <<NUM-06|90 dias|180 dias>> |
| Texto de regras | ver <<REF-02|governance/CONSTITUTION.md|governance/CONSTITUTION-V3.md>> |

## 5. Fora de escopo
Execução de ordem, gestão de conta e qualquer integração com corretora.
