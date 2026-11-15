# DHR-AVALIACAO-002 — Ata operacional curta — respostas de Andraus à avaliação de desempenho da SPEC-008
| Campo | Valor |
|---|---|
| De | Andraus (registro pelo Orquestrador) |
| Data | 2026-11-15 |
| Ordem | AskUserQuestion, 2026-11-15, lotes 1 e 2 da avaliação gerada por `avaliacao_spec.py` (`DHR-AVALIACAO-001`): todas as opções recomendadas |
| Status | **REGISTRO DE DECISÃO OPERACIONAL**. Não fecha nem abre decisão do ROADMAP (CONS-01); nenhuma proposta é aplicada. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Registro das respostas a uma avaliação de fim de Spec; não altera texto de agente nem método. |
## Mudança
Respostas `[FATO]`: **redigir** as propostas de (BP-04) conferidor fato→locais, (BP-05) citação por identificador, (BP-06) histórico em arquivo separado com conferência, (BP-03) revisão só do delta, (BP-07) máquina de estados em tabela conferida por script, (BP-08) detectores para categorias sem prevenção e (BP-12) checagem de pré-entrega — **só propostas, sem aplicar** (`governance/propostas/MELHORIAS-PROCESSO/PROPOSTAS-RETRO-SPEC-008-2026-11-15.md`); **registrar o custo de cada rodada** (BP-10; procedimento do Orquestrador desde já: `TOKENS:` no parecer via `telemetria_tokens.py tokens`); **aceitar a avaliação e registrar a retrospectiva da SPEC-008** (BP-01). A avaliação passa a `RESPONDIDA`.
## Verificação
`avaliacao_spec.py registrar SPEC-008 --ata DHR-AVALIACAO-002`; retrospectiva em `RETROSPECTIVAS.md`; `loop_ledger.py --retro-check SPEC-008` passa.
## Não toca
`AGENTS.md`, agentes, ROADMAP, decisões abertas. Cada proposta só vira mecanismo por ordem expressa de Andraus, com `MECANISMOS.json` no mesmo PR (COE-14).
