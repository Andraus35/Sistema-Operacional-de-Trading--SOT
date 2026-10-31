# Parecer do Revisor — ERRATUM-REAPONT-001 v1.3 — R3 delta curta (S2, sonnet) — 2026-10-31

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `governance/ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md` v1.3 (commit `f5265ee`; base v1.2 `8798701`). Gates do Orquestrador: check_refs 0 ERRO; check_doc_sync ERRO=0; check_invariants 0; revisor_gate PASSOU_D; coesão 0 ERRO; mapa em dia; RPSA ok. Revisor consultou por Grep só o ROADMAP nesta rodada (limite declarado); não reproduziu gate/sha256.

**VEREDITO: NÃO CONFORME** — 0 Críticas, 1 Média, 1 Menor. m-6 e m-7 do R2 **resolvidos**; Adendo 7 (Q-5/Q-6/Q-7) aderente, sem pergunta pendente nem ramo morto; CONS-01 e aditividade preservados; amostra anti-leniência (L-01..L-06, L-09, L-26..L-28) conferida. As 10 linhas citadas pela N-F conferem por texto (l.7, 21, 310, 445, 713, 1538, 1733, 1803, 1950, 2068) e a C-3 (l.3) segue intacta.

- **M-A (Média, C07)** — a lista da N-F (§4/§6) NÃO reproduz as 10 menções da nota C-3 do plan da SPEC-007 ("l.63, 64, 71, 308, 319, 359, 443, 711, 1731, 1801"): omite 5 que existem hoje (≈ +2: **l.65** RULE-KFH-015 WikiRAG | 048; **l.66** RULE-KFH-016 WikiRAG; **l.73** §D3.1 códigos … 048; **l.321** Termo 3 — WikiRAG … SPEC-048; **l.361** linha de transferência … WikiRAG, F2 → SPEC-048) e acrescenta 4 (l.7, 21, 1538, 2068) sem declarar que amplia. Isso torna inexata a afirmação de §8/§13 de que a referência foi "atualizada para a v2.3". Reconstruir ponto a ponto a partir da lista da C-3 e declarar toda adição; contar contra o Grep de "SPEC-048"/WikiRAG no plan da SPEC-007; ajustar a nota, o ponteiro da SPEC-007 (§13) e a linha da §8.
- **m-8 (Menor, C07)** — a N-F não declara se a lista atualizada é 1:1 ou ampliação; coberto pela correção do M-A (sem FICHA-M: exige redação).

Próxima revisão: delta curta sobre a N-F. Condição: cada uma das 10 menções da C-3 aparece na N-F com a linha atual (por texto) e toda linha a mais é declarada como adicional.

<!-- ACHADOS-ESTRUTURADOS
M-A|MEDIA|C07|Lista de linhas da N-F nao reproduz as 10 mencoes da nota C-3 (omite l.65, 66, 73, 321, 361 e acrescenta l.7, 21, 1538, 2068 sem declarar)|Ao atualizar uma lista de referencias, reconstruir ponto a ponto a partir da lista antiga e declarar toda adicao ou remocao
m-8|MENOR|C07|N-F nao declara que a lista atualizada difere em conteudo da lista antiga da C-3|Declarar na propria nota o criterio de composicao da lista (atualizacao 1:1 versus ampliacao)
-->

<!-- FICHA-M {"achados":[]} -->
