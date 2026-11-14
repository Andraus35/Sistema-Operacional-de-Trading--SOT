# DHR-EXPERIMENTO-PARADA-001 — Ata operacional curta — experimento da regra de parada no Plan da SPEC-008
| Campo | Valor |
|---|---|
| De | Andraus (registro pelo Orquestrador) |
| Data | 2026-11-14 |
| Ordem | "Aplicar a partir da rodada 3 (Recomendado)" — AskUserQuestion, 2026-11-14 (aprovação original do experimento: `DHR-RETRO-003`, P10, 2026-10-31) |
| Status | **REGISTRO DE DECISÃO OPERACIONAL**. Não fecha nem abre decisão do ROADMAP (CONS-01); não altera `AGENTS.md` nem agentes. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Aplica experimento de processo já aprovado ao pedido de rodadas de um Plan; não altera texto de agente nem método. |
## Mudança
O experimento da regra de parada (`governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md`) passa a valer no Plan da SPEC-008 **a partir da R3**: (1) parecer só com Menores não abre rodada nova (mecânicos por ficha M; demais viram condição de homologação ou ficam para a construção, à escolha de Andraus); (2) hash do delta (`BASE`/`SHA256-ALVO`/`DELTA`) obrigatório no pedido ao Revisor; (3) teto de **5 rodadas** (CRITICAL): ao chegar nele com Média aberta, escala a Andraus; Crítica e Média **sempre** abrem rodada; (4) métricas de tokens por papel e por rodada registradas. **Falha minha declarada:** o Plan começou (R1, R2) sem a regra no pedido; o baseline é, portanto, parcial.
## Baseline (R1 e R2, sem a regra) — fonte: notificações de tarefa do harness; a telemetria local `.telemetria/` NÃO mede tokens (formato não reconhecido) = **n/m**
Plan: Especificador 1ª entrega 419.289 tokens (≈66 min); Revisor R1 **n/m**; Especificador R1→R2 319.385 (≈73 min); Revisor R2 241.418. Médias por rodada: 5 → 2 (Menores 8 → 11). Plan 1.626 → 1.829 linhas. Rodadas feitas: 2 (ambas NÃO CONFORME).
## Verificação / Não toca
Sem mudança de código. Não toca `AGENTS.md`, `.claude/agents/*`, ROADMAP nem decisões abertas; a retrospectiva da SPEC-008 (aprovação final do Plan, `DHR-LOOP-002`) decide se a regra vira norma.
