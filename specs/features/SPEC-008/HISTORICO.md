# HISTORICO.md — SPEC-008 (Manager — Despacho e Ciclo, Fase 1) — histórico de rodadas do Plan

> Arquivo à parte do corpo do `plan.md` (lição C06 — histórico fora do corpo normativo; não conta para RULE-ECC-07). Preserva o texto trocado de regra/contrato (INV-07) com o motivo. Não é norma; a norma é o `plan.md` vigente.

## Rodadas

| Rodada | Data | Versão do Plan | Parecer | Resultado |
|---|---|---|---|---|
| R1 | 2026-11-08 | v1.0 (commit `55d0989`; correções M do Orquestrador em `5c172dc`) | `governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R1-2026-11-08.md` | NÃO CONFORME — 5 Médias (M-01..M-05), 8 Menores (m-01..m-04 classe M aplicados pelo Orquestrador; m-05..m-08 ao Especificador) |
| R2 | 2026-11-14 | v1.1 | (pendente) | correção de M-01..M-05 e m-05..m-08 |

## R1 → R2 (v1.0 → v1.1) — texto anterior preservado (INV-07)

Contexto novo recebido: respostas de Andraus por AskUserQuestion em 2026-11-08 (via Orquestrador) — DN-1 decidir depois com a SPEC-014; DN-2 a Fase 1 só detecta e avisa; DN-3 não confirmada (inventário de Fibonacci/Fractal antes). Nenhuma decisão aberta fechada; nenhuma DN nova.

| Achado | Local | Texto anterior (v1.0) | Motivo da troca |
|---|---|---|---|
| m-05 | RULE-MDC-001 (d) | "(d) Isolamento (WF-P01): no máximo UM ciclo não encerrado por chave (`asset`, `mission_id`)…" | WF-P01 só diz paralelismo entre ativos; isolamento por (ativo, missão) é `[PROPOSTA]` |
| m-05 | tabela WORKFLOW, linha WF-P01/WF-P02 | "um ciclo por (ativo, missão), isolado; parâmetros por ativo versionados" | idem |
| M-02/M-04 | RULE-MDC-003 (a) | "`dispatch_key` = H(`cycle_id`, `node_id`, `stage_seq`) … referências dos insumos publicados, `tf`, `max_rounds`, `graph_version`}" | nova tentativa por erro do agente exige `attempt`; SPEC-048 exige orçamento (rodadas, tempo) + `budget_ref` no pedido |
| M-02 | RULE-MDC-003 (c) | "cada espera tem timer pedido à Spec de Tempo com o `stage_deadline` do parâmetro" | explicitar timer também após F06 (espera do resultado macro) e que nova tentativa não reinicia o timer |
| M-02 | RULE-MDC-003 (f) | "(f) Falha ao publicar o pedido ou erro do agente analítico conta como falha seguida do nó; novas tentativas limitadas por `max_consecutive_failures`; estouro ⇒ RULE-MDC-008 (b)." | falhas sem evento/linha D5; voltas esgotadas sem evento |
| DN-2 | RULE-MDC-004 (d) | "ABRIR um ciclo completo por causa da ruptura = [DECISÃO NECESSÁRIA] DN-2 (a Fase 1 não origina ciclo — RULE-MDC-001 (c)). … chega como `ALARM_CANCELLED` (D5, F15)." | DN-2 decidida por Andraus (2026-11-08) sem mudar comportamento |
| M-02 | RULE-MDC-005 (a) | "…invoca UMA vez … Segunda invocação macro no mesmo ciclo ⇒ recusada `MDC_MACRO_ALREADY_INVOKED` (2x por ciclo = 1 aqui + 1 na Fase 2)." | definir "invocação" = pedida; eliminar contradição com 005 (e) |
| M-03 | RULE-MDC-005 (c) | "…∧ o valor agregado devolvido não é INDETERMINADO ∧ valor ≥ θ." | nomear o campo |
| M-03 | RULE-MDC-005 (d) | "(d) \"Valor agregado da leitura macro\" = [INFERÊNCIA] o campo agregado do esquema do CCM-001 calculado sobre o subconjunto (RULE-CF-010); o nome exato é lido do contrato da SPEC-003 na construção, sem redefini-lo. Resultado sem valor agregado ou sem `directional_conflict` ⇒ INDETERMINADO ⇒ (c)." | campo adiado ao BUILD; `gate_result`/`thresholds_used` não tratados |
| M-02 | RULE-MDC-005 (e) | "(e) Mecanismo indisponível ou com erro ⇒ falha seguida (RULE-MDC-003 (f))." | contradizia 005 (a) |
| M-01 | RULE-MDC-006 (c) | "(c) `ALARM_ARMED` do alarme pedido ⇒ `CONTEXTO_FORMADO` → `ARMADO`; `ALARM_TRIGGERED` válido (RULE-MDC-004 (b)) ⇒ `ARMADO` → `ATIVADO` + despacho…" | guarda de elegibilidade |
| M-01 | RULE-MDC-006 (d) | "o setup publicado é aceito ⇔ `parent_id` = hipótese de contexto ∧ …" | guarda de elegibilidade no setup |
| M-01 | RULE-MDC-006 (g) | "(g) `ALARM_EXPIRED` ⇒ ramo 5: encerramento `MDC_ALARM_EXPIRED`; `ALARM_CANCELLED` ⇒ encerramento `MDC_ALARM_CANCELLED`. Nenhum rearme, nenhuma volta a `ARMADO` (P-12)." | só cobria `ARMADO`; WF-A02 permite morte após `TRIGGERED` |
| M-01 | RULE-MDC-006 (h) | (não existia) | nova reconferência de elegibilidade |
| M-01 | RULE-MDC-007 (d) | "Encerramento em `ATIVADO` (alarme já disparado) pede `MARK_CONSUMED` à Spec de Tempo (P-12: termina \"usado\"); em `ARMADO`, nenhum pedido ao alarme (requisito T-3 à Spec de Tempo)." | exceções F32/F37 e caso F30 |
| M-04 | RULE-MDC-008 (a) | "`max_rounds_per_agent` (repassado no `dispatch_request`; a ele se referem os pedidos de orçamento da SPEC-007/048, como `max_retrieval_rounds`), `max_consecutive_failures` por nó/mecanismo, `stage_deadline`." | equivalência sem `[INFERÊNCIA]`; tempo não declarado como orçamento |
| M-02 | RULE-MDC-008 (b) | "…+ aviso; a contagem vive no livro de bordo do ciclo." | `ROUNDS` vem do aviso do agente |
| m-08 | RULE-MDC-010 (a) | "Entrada: `cycle_id`, `log_seq`, `entry_type`, `rule_id`, `graph_version`, `limits_version`, `causation_event_id`, `recorded_instant`, `from_state`, `to_state` \| —, `code` \| —, `refs`." | `rule_id` com dois sentidos; falta `capability_check_ref` |
| M-05 | INV-MDC-01 (parágrafo "ANTES de qualquer ação") | "ANTES de qualquer ação de um ciclo, o componente confere o registro de capacidades: … em ambos, nada é despachado nem pedido, e a recusa é gravada no livro de bordo…" | conferência por ação; fonte independente das contagens |
| M-04 | tabela de parâmetros | "\| latência de despacho/notificação \| RULE-CEB-010 (SPEC-005) \| consumidor \| SPEC-005 (parâmetro) \| INDETERMINADO …" | separar latência de transporte (SPEC-005) do orçamento de trabalho da etapa (SPEC-008, SPEC-048) |
| M-02/M-05/m-06 | D4.2 | "(2) `cycle_id` e papel autenticado conferem com o nó/pedido → `MDC_EVENT_FOREIGN_CYCLE`; … (7) grava a entrada (antes do efeito); (8) produz o efeito da linha; (9) atualiza contadores (D4.3)." | pertença por categoria de emissor; conferência de capacidades por ação; simulação dos negativos |
| M-02 | D4.3 | "`rounds[nó]` = `max_rounds_per_agent` repassado no pedido (o laço interno é do agente analítico); `failures[nó]` += 1 a cada falha seguida, zera no sucesso" | Manager não conta voltas; eventos de falha nomeados |
| M-01/M-02/M-05 | D5 | F06 sem timer; F12/F13/F16/F17 sem guarda de elegibilidade; sem F30–F37 | linhas novas e guardas |
| M-02 | Interface `STAGE_TIMER` | "F01, F03, F09, F13" | + F06 |
| m-07 | BASpec-MDC-009 | "[E1]" | contém ENC por STOP (E2) |
| m-07 | EC-MDC-007 FAILURE-MODE | "Canal indisponível ⇒ o aviso fica registrado no livro como pendente" | sem `entry_type` |
| m-08 | EC-MDC-003 EVIDENCE | "rule_id = linha F-nn" | campo `fsm_row` |
| M-05 | EC-MDC-008 POSTCOND/EVIDENCE | "capacidades exercidas ⊆ allowlist; model_calls == 0; …" / "capability_check_ref por ação no livro; contagens … == 0" | contagens sem campo nem fonte |
| m-07 | EC-MDC-009 | (não existia) | capacidade (4) sem EC próprio |
| m-06 | ADV-05 | "(b) chega ALARM_ARMED sem ARM_ALARM pedido … (b) \"MDC_TRANSITION_NOT_LISTED\"" | a D4.2 para antes, no passo (2) |
| m-06 | ADV-07 | "\"MDC_TRANSITION_NOT_LISTED\" para o disparo" | idem |
| M-02 | ADV-06 | "DADO ciclo com CV1 já lido (F07 ou F08)" | cobrir tentativa após erro |
| — | contagens | v1.0: 8 EC, 20 cenários, 14 ADV, 1.626 linhas | v1.1: 9 EC, 22 cenários (T21, T22), 15 ADV (ADV-15), 1.812 linhas |
