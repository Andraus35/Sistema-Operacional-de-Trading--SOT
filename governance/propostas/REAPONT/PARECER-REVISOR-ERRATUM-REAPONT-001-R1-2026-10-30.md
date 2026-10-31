# Parecer do Revisor — ERRATUM-REAPONT-001 v1.0 (R1, S2/sonnet) — 2026-10-30

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `governance/ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md` v1.0 (commit `142d29b`). Gates do Orquestrador: check_refs 0 ERRO; check_doc_sync ERRO=0; check_invariants 0; revisor_gate PASSOU_D; coesão 0 ERRO; mapa em dia; nenhum plan.md/checks.md editado. Revisor não abriu `atomic-spec.md`; não reproduziu gate/hash (GATE NÃO VERIFICADO por ele).

**VEREDITO: NÃO CONFORME** — 0 Críticas, 1 Média, 4 Menores. Conferidas e OK: as ocorrências L-01..L-29 (fontes abertas); N-A, N-D (P-14, RULE-KFH-001/RULE-RET-003); decisão de NÃO pôr nota nas 5 linhas da SPEC-020 e no ERRATUM-SPEC020-001 (coerente com ERRATUM-SPEC020-002 §2/§3/§8); CONS-01 (lista de abertas == ROADMAP l.36; SPEC-045-RUNTIME-001 intocada); aditividade; critério 2 (nota C-3 no topo do plan da SPEC-007 e ROADMAP l.184); Q-1..Q-8 claras. Sem omissão do critério 1 em plan/checks fora SPEC-007/048.

- **M-1 (Média, C04)** — N-C/L-06 (e a 1ª parte da linha-base L-05): "§40 Retrieval — 015-020, 022 (Retrieval/Similar/Contrasting/Temporal/Regime/Relevance/Packet)" é recuperação de **EXPERIÊNCIA** (`reference/camadas/CAMADA MEMÓRIA.MD` EXP-SPEC-015..022), não RAG de conhecimento; a SPEC-048 não a cobre (plan: experiência → SPEC-009/017) e nenhuma ata decide esse endereço. Re-apontá-la à SPEC-048 cria, por errata Patch, endereço novo sem ata (a proposta da SPEC-048 já generalizou assim). Limitar N-C ao RAG de conhecimento e declarar a recuperação de experiência como `[DECISÃO NECESSÁRIA]`/fora (ou pergunta nova a Andraus); atualizar §3, N-C e fato→locais.
- **m-1 (Menor, C07)** — SPEC-007 `plan.md` (l.261/268 carregam a divisão; l.2605 e l.2610 citam SPEC-002 sem nota e "RAG faithfulness DIFERIDA para a SPEC-007"): a errata não as menciona nem marca a exclusão como `[INFERÊNCIA]`.
- **m-2 (Menor, C06, mecânico segundo o Revisor)** — L-30 "16 linhas casam" mistura critério exato (13) e ampliado (16). **O Orquestrador não pôde confirmar a contagem** (L-30 conta linhas do ERRATUM-SPEC020-002; não reproduzida por Grep simples) → vai ao Especificador.
- **m-3 (Menor, C06)** — fato→locais omite L-05 (1ª parte); condicionado a M-1 (a redação de L-06 muda).
- **m-4 (Menor, C07)** — §7 omite `governance/CATALOGO-OFICIAL.md` (linha "RAG faithfulness/tool correctness/decision traceability — diferidas a SPEC-007/038/014"); registrar como "sem nota / coberto pelo ERRATUM-SPEC020-002".

Revisão seguinte: por delta (bloco N-C/L-06/§3/§8/§7). Teto: CONFORME condicional (gate não reproduzido pelo Revisor).

<!-- ACHADOS-ESTRUTURADOS
M-1|MEDIA|C04|Re-apontamento generalizado (L-06 EXP-SPEC-015..022 recuperação de experiência tratada como RAG → SPEC-048) herdado da proposta da SPEC-048 sem abrir a série EXP nem ata que a decida|Antes de classificar "só recuperação", abrir o ID de origem da linha (série EXP vs RAG) e conferir contra o escopo declarado da Spec de destino; item sem dono em ata vira [DECISÃO NECESSÁRIA], não re-apontamento
m-1|MENOR|C07|Exclusão da SPEC-007 do critério 1 não marcada [INFERÊNCIA] e ocorrências l.2605/l.2610 não mencionadas|Declarar por documento excluído as linhas-ocorrência e o motivo
m-2|MENOR|C06|Contagem "16 linhas casam" mistura critério exato (13) e ampliado (16)|Toda contagem de busca declara o regex e o universo
m-3|MENOR|C06|Tabela fato→locais omite L-05 (1ª parte)|Gerar a tabela fato→locais a partir da tabela de decisão (§3)
m-4|MENOR|C07|§7 omite CATALOGO-OFICIAL.md (classe B diferida a SPEC-007/038/014)|Estender a busca de registros do §7 aos documentos-registro (CATALOGO, RMR-001, CONFLICT-MAP)
-->
