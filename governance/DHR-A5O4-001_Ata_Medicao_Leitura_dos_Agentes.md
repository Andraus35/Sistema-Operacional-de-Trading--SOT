# DHR-A5O4-001 — Ata operacional curta — Medição da leitura dos agentes (A5-O4)
| Campo | Valor |
|---|---|
| De | Andraus (registro pelo Orquestrador) |
| Data | 2026-11-01 |
| Ordem | "Medir quanto o Especificador lê do backlog (Recomendado)" — AskUserQuestion, chat 2026-11-01 |
| Status | **REGISTRO DE DECISÃO OPERACIONAL**. Não fecha nem abre decisão do ROADMAP (CONS-01). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Medição e documentos novos não normativos; não altera texto de agente nem método. |
## Mudança
- `PROPOSTA-A5` §5 + `A5/medir_leituras.py` (artefato de proposta, fora de `scripts/`, não roda no CI) + `A5/MEDICAO-LEITURAS-2026-11-01.txt`; pauta (pedido 4) e HANDOFF HO-161 atualizados.
## Verificação
`check_handoff`, `check_refs`, `check_coesao`, `check_doc_sync`, `check_rpsa`, `build_map --check` no commit do PR.
## Não toca
`AGENTS.md`, `.claude/agents/*`, `ROADMAP.md`, selos, decisões abertas. A amostra (n = 9, uma frente, tarefas de proposta MEDIUM) **não** mede a abertura de uma Spec HIGH.
