# DHR-A7A4-001 — Ata operacional curta — A7-lite (modelo de ata curta) e A4-b (abertura dentro do P10)
| Campo | Valor |
|---|---|
| De | Andraus (registro pelo Orquestrador) |
| Data | 2026-11-01 |
| Ordem | "A7-lite: modelo de ata curta" e "A4-b: medir dentro do P10" — AskUserQuestion, 2026-11-01 |
| Status | **REGISTRO DE DECISÃO OPERACIONAL**. Não fecha nem abre decisão do ROADMAP (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Modelo de texto e anexo de medição; não toca agente, `AGENTS.md`, método nem detector. |

## Mudança
- **A7-lite:** novo `governance/MODELO-ATA-OPERACIONAL-CURTA.md` (ata de até 15 linhas para mudança puramente operacional). Esta ata já o usa. Log único (A7-log) **não** adotado. Base: `PROPOSTA-A7-LOG-UNICO-DE-DECISOES-2026-11-01.md`.
- **A4-b:** o experimento P10 passa a medir também a **abertura** (tokens e Médias por rodada; parar em 0 Média), no próximo Plan que Andraus mandar abrir; adendo em `PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md`. Nenhuma norma muda; A4 como na auditoria **não** adotado. Base: `PROPOSTA-A4-PROPORCIONALIDADE-ABERTURA-PLAN-2026-11-01.md`.
## Verificação
`check_handoff`, `check_refs`, `check_coesao`, `check_rpsa`, `build_map --check` (resultado no HANDOFF HO-145).
## Não toca
`AGENTS.md`, `.claude/agents/*`, `atomic-spec.md`, `ROADMAP.md`, `check_handoff` (HO-06) e decisões abertas.
