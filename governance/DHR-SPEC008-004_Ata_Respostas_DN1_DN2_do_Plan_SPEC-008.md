# DHR-SPEC008-004 — Ata — Respostas de Andraus às DN-1 e DN-2 do Plan da SPEC-008

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | Plan da SPEC-008 (`specs/features/SPEC-008/plan.md`; DN-1, DN-2) · parecer R2 do Revisor, achado R2-m06 (`governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R2-2026-11-14.md`) · `DHR-SPEC008-001` (P-12 "só encerrar") · `DHR-FIBFRAC-002` (DN-3) |
| Data | 2026-11-14 (registro; as respostas foram dadas por AskUserQuestion em 2026-11-08, na sessão da primeira rodada do Plan) |
| Status | **RESPOSTAS REGISTRADAS** (Andraus, AskUserQuestion, 2026-11-08). Registro de decisão; não edita o Plan nem baseline; não fecha decisão aberta (CONS-01). Assinatura = decisão registrada e citada nesta ata (AGENTS.md §10). |
| Compatibilidade | Patch (registro; nenhum comportamento novo) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Registro de decisões de especificação; não altera texto de agente de construção nem método. |

## 1. Respostas de Andraus `[FATO]` (AskUserQuestion, 2026-11-08)
| # | Pergunta (DN do Plan) | Resposta |
|---|---|---|
| DN-1 | Com qual rótulo final termina um ciclo encerrado antes de chegar ao Risco (por exemplo, a Fase 2 decide não enviar)? | **"Decidir depois, com a SPEC-014 (Recomendado)"** — o ciclo encerra registrado e não aceita mais evento, sem rótulo final de WF-F02 até a SPEC-014 |
| DN-2 | Quando uma hipótese dominante é rompida (inversão de estrutura), quem abre um novo ciclo completo de análise? | **"A Fase 1 só detecta e avisa (Recomendado)"** — registra a ruptura e avisa Andraus/Fase 0; não abre ciclo por conta própria (coerente com P-12). Quem abre = SPEC-015 |
| DN-3 | (Não respondida em 2026-11-08) | Ver `DHR-FIBFRAC-002` (confirmada em 2026-11-14) |

## 2. Leitura `[INFERÊNCIA]` do Orquestrador
- **DN-1** segue **pendente por decisão de Andraus** ("decidir depois"): continua `[DECISÃO NECESSÁRIA]`/pendência registrada no Plan; **não** está fechada.
- **DN-2** está **decidida**: o comportamento já escrito no Plan (RULE-MDC-004 (d)) é o decidido; só muda a etiqueta, de `[FATO]` sem ata para `[FATO]` com esta ata.

## 3. O que esta ata NÃO afirma
- Não edita o Plan (a correção da etiqueta é do Especificador, achado R2-m06), `WORKFLOW.md` nem baseline. Não decide o rótulo final do ciclo encerrado, quem abre o ciclo completo (SPEC-015), a confluência fractal nem a reentrada após stop (P-13).

## 4. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4 · BL-026 · P-13 · localização da confluência fractal · DN-1. **Nenhuma decisão aberta é fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] Respostas de Andraus (AskUserQuestion 2026-11-08) · [x] CATALOGO · [x] RPSA · [ ] Plan (etiqueta, próxima rodada) · [ ] merge (PR, CI verde — assinatura)

---

**Andraus** — *respostas dadas por AskUserQuestion, 2026-11-08; registro pelo Orquestrador.*
