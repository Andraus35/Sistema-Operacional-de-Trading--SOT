# Telemetria manual — onda 0 de roteamento (rascunho, não normativo)

> Dado de estado, append-only (INV-07). Autorizada pela ata `governance/DHR-ROTEAMENTO-001_Ata_Decisoes_Roteamento_de_Modelos_Onda0.md`. Métrica-alvo (cota): tokens e chamadas por defeito confirmado. Preencher só com o que o `Agent`/sessão reportar; campo desconhecido = `n/m` (não medido), nunca estimado.

| Data | Tarefa (ID da proposta) | Executor | Modelo / esforço | Tokens (total) | Chamadas | Pré-gate (PASSOU_D / REPROVADO_D / n.a.) | Revisor evitado? | Resultado | Nota |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-17 | G/T/O (sessão de auditoria: roteamento + separação AC×AT) | Orquestrador | sessão (n/m) | n/m | n/m | n.a. (sem Spec em revisão) | n.a. | entregue | linha de abertura; ainda não houve rodada Especificador→Revisor |
| 2026-10-17 | Confirmação da guarda do Revisor (revisão curta SPEC-005) | Revisor SOT (agente de construção, Sonnet 5.5) | sessão (n/m) | 72430 (subagent_tokens) | 18 tool_uses | PASSOU_D (--rapido) | n.a. (observação) | CONFORME condicional; 3 Menores + 1 Info | G1 ok (núcleo aberto); G2 NÃO — ferramenta MCP ausente e hook SubagentStop não forçou retorno ao vivo (reprodução manual do hook: exit 2, funciona); G3 amostra ok |
| 2026-10-31 | Abertura SPEC-049 (Dossiê + ABERTURA; classe O) | Especificador SOT (opus) | opus-5-5 | 250105 (subagent_tokens) | 109 tool_uses (~17 min) | PASSOU_D (--rapido) | n.a. (1ª rodada, integral) | entregue ao Revisor; não é CONFORME | gates do Orquestrador: backlog_triggers --abertura 0 itens, check_repo_research OK, check_refs/doc_sync ERRO=0, check_invariants 0 achados |
| 2026-10-31 | Parecer R1 integral da abertura SPEC-049 (S2) | Revisor SOT (sonnet) | sonnet-5-5 | 172341 (subagent_tokens) | 81 tool_uses (~4,7 min) | PASSOU_D (Orquestrador; Revisor sem MCP) | n.a. (1ª rodada) | NÃO CONFORME (1 Média, 8 Menores); SHA256-ALVO declarado pelo Revisor (1ª vez) | ficha M aplicada (m02); devolver ao Especificador (classe O) |
