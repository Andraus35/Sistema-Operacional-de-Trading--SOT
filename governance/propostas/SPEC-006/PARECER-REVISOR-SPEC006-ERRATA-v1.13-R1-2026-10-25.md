# Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R1) — 2026-10-25

> Transcrição pelo Orquestrador (o Revisor não tem Write). Alvo: `specs/features/SPEC-006/errata-v1.13.md` v1.0 (commit `ee50ecb`). Gates informados pelo Orquestrador: check_refs 0 ERRO, check_invariants 0, revisor_gate PASSOU_D, suíte 353 OK; o Revisor não rodou gate (GATE NÃO VERIFICADO por ele). Aditividade confirmada por Grep (plan.md/checks.md da SPEC-006 sem "Errata v1.13", `SEAL_REF_UNRESOLVABLE`, `formation`).

**VEREDICTO: NÃO CONFORME** — 4 Médias, 3 Menores, 0 Críticas. Nenhuma violação de invariante, salvaguarda ou CONS-01 (K-001, host do CKG-008, lista do caminho (a) seguem abertos).

## Achados
- **A1 MÉDIA** — E-3 itens 2 e 4 e ADV (j)(n): a junção depende de `record_ref`, que o esquema do registro da SPEC-006 não tem (0 ocorrências). `supersedes` do KG (`KG-N-…-v0`) vs `published_ref@version` do selo sem mapa de formato; ADV (n) usa um terceiro (`KG-N-X@2`). Ação: declarar em que campo (ex.: dentro de `publication`) chega o `record_ref` e fixar o mapa de formato.
- **A2 MÉDIA** — E-3 item 3 / "Lista de exclusão completa" / Herança linha 2: "excluir tudo o que M exclui" ≠ projeção M (que é por inclusão). O `node_record` (plan l.1398-1422) tem campos em nenhuma das listas (`provenance_ref.*`, `schema_version`, `canonical_*`, `natural_key`, `valid_from`); `relation_record` tem `from_node`/`to_node`. Risco: falso-DENY em todo registro selado. Ação: tabela campo a campo (entra em M / fica fora) para `node_record` e `relation_record`; trocar "completa"; estender ADV (m); registrar que a auditoria amostral da SPEC-007 (EC-KFH-004 (ii)) usa lista mais estreita.
- **A3 MÉDIA** — E-2(b)+E-3 para relações: relação selada não tem campo de conteúdo nem marca de inferência (`formation` só em `node_record`); o hash de relação nunca bate; "RU-3 fecha também para relações" não se sustenta. Ação: estender `formation` (ou equivalente) a `relation_record` ou mapear a campos existentes; atualizar tabela fato→locais.
- **A4 MÉDIA** — O texto mantém ramos condicionais já decididos por Andraus (Q-1, Q-2, Q-3, Q-8, Q-9) e não explicita premissa de Q-4..Q-7 (assume Q-4 não, Q-5 sim, Q-6 fora do hash, Q-7 não). Ação: v1.1 incondicional nas decididas (Major com precedente DHR-SPEC006-003 D3; forma A com ponteiro); Q-4..Q-7 pendentes com premissa declarada.
- **A5 MENOR** — ADV (l) sem pré-condição de que N1 tem ≥1 afirmação `formed_inference=true` (C03). Não mecânico.
- **A6 MENOR** — cita P3/P4 como vigentes; a DHR-RETRO-001 §1 diz que são proposta a especificar (C07). Mecânico (FICHA-M).
- **A7 MENOR** — `SEAL_REF_UNRESOLVABLE` usado também para `record_ref` fora do selo (selo resolve); alinhar com Q-5 (C02).

## Encaminhamento
Ordem classe O ao Especificador com PARECER + FICHA; A1–A4 exigem v1.1, A5 e A7 no mesmo envio, A6 por Ficha-M. Revisão da v1.1 por delta permitida, reverificando A1–A4 integralmente. Condição: tabela M por campo + posição do `record_ref`; conteúdo de relação coberto; texto sem ramos condicionais decididos; Q-4..Q-7 pendentes explícitas; sha256 do plan.md da SPEC-006 conferido pelo Orquestrador (`dd5a609f3007…` conferido em 2026-10-25).

<!-- ACHADOS-ESTRUTURADOS
A1|MEDIA|C04|record_ref ausente do esquema SPEC-006 (0 ocorrências); E-3 itens 2 e 4 não representáveis; formato supersedes KG-N-…-v0 vs published_ref@version|Checar, por obrigação herdada, que o campo usado pelo gate existe no esquema do contrato antes de declarar a herança satisfeita
A2|MEDIA|C01|E-3 item 3 'excluir tudo o que M exclui' não equivale à projeção M (inclusão); lista 'completa' omite campos do node_record/relation_record (provenance_ref.*, schema_version, from_node/to_node)|Escrever tabela de projeção M campo a campo; não afirmar 'completo' sem fonte aberta
A3|MEDIA|C04|Relação selada sem campo de conteúdo/marca de inferência (formation só em node_record) com Q-2 aprovada; hash de relação nunca bate|Ao estender escopo (nó para relação), reconferir cada campo que entra no hash também no registro novo
A4|MEDIA|C08|Texto da errata mantém ramos condicionais Q-1/2/3/8/9 já respondidos por Andraus; Q-4..Q-7 sem premissa explícita|Ao receber respostas de Andraus, emitir versão que resolve os condicionais e deixa só o pendente com premissa declarada
A5|MENOR|C03|ADV (l) sem pré-condição de que N1 tem afirmação formed_inference=true|Declarar no ponto de partida do cenário os dados que fazem o caso discriminar
A6|MENOR|C07|Cita P3 e P4 como prática vigente; ata DHR-RETRO-001 §1 diz proposta a especificar|Conferir status de cada P-n na ata antes de citar como vigente
A7|MENOR|C02|SEAL_REF_UNRESOLVABLE usado para record_ref fora do selo; lista de exclusão mais larga que a de SPEC-007 EC-KFH-004 (ii)|Nomear códigos pelo que falhou; declarar divergência com a auditoria amostral da SPEC-007
-->

<!-- FICHA-M
{"achados":[
{"id":"A6a","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"(P3, DHR-RETRO-001)","novo":"(alinhado à proposta P3 — ainda proposta a especificar, DHR-RETRO-001 §1)","condicao":"texto antigo ocorre uma única vez, no cabeçalho (linha Âncoras)"},
{"id":"A6b","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"(P2/P4)","novo":"(P2 em vigor; P4 ainda proposta — DHR-RETRO-001 §1)","condicao":"texto antigo ocorre uma única vez, na seção Forma de aplicação, opção (A)"}
]}
-->
