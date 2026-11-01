# DHR-A3-001 — Ata operacional curta — Pauta única de decisões (A3)
| Campo | Valor |
|---|---|
| De | Andraus (registro pelo Orquestrador) |
| Data | 2026-11-01 |
| Ordem | "A3 — pauta de decisões (Recomendado)" — AskUserQuestion, chat 2026-11-01 |
| Status | **REGISTRO DE DECISÃO OPERACIONAL**. Não fecha nem abre decisão do ROADMAP (CONS-01). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Documento novo e não normativo (pauta); não altera texto de agente nem método. |
## Mudança
- Cria `governance/PAUTA-DE-DECISOES.md` (uma página; 8 pedidos com recomendação marcada; eventos esperados; decisões abertas só listadas). Substitui a prosa de `HANDOFF.md` §10 por ponteiro; vencimento de 14 dias no HANDOFF (`[PRAZO]`, HO-10) = A3 regra 2.
- Marca `PROPOSTA-A3` como aplicada em parte (aditivo).
## Verificação
`check_handoff`, `check_refs`, `check_coesao`, `check_doc_sync`, `check_rpsa`, `build_map --check` e suíte, no commit do PR.
## Não toca
`AGENTS.md` (a regra 1, classes de decisão, vira o pedido nº 2 da pauta e **não** foi aplicada), `ROADMAP.md`, `.claude/agents/*`, selos, decisões abertas.
