# Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R2, por delta) — 2026-10-25

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `specs/features/SPEC-006/errata-v1.13.md` v1.1 (commit `e060f57`). Gates do Orquestrador: check_refs 0 ERRO, check_invariants 0, revisor_gate PASSOU_D, suíte OK, mapa em dia, plan.md da SPEC-006 intacto (`dd5a609f3007…`). Revisor abriu ROADMAP, atomic-spec e RULES (G1); não rodou gate/hash/git.

**VEREDICTO: NÃO CONFORME** — 1 Média nova (B1), 4 Menores (B2–B5). A1, A2, A3 e A4 do R1 estão **resolvidos**; A5, A6b e A7 também. Sem violação de invariante, salvaguarda ou CONS-01. Aditividade confirmada (plan.md/checks.md sem ocorrência da errata).

- **B1 MÉDIA** — Mapa de formato cobre só `from`/`to`; `causal.outcome_ref` entra em M sem regra de forma (`record_ref` × id do KG): M(r) de CAUSA com desfecho não é reconstruível de forma determinística (falso-DENY). Ação: estender o Mapa/Tabela a `outcome_ref` (ligado à Q-10 (b)) + caso T09/ADV com CAUSA e `outcome_ref`.
- **B2 MENOR** — Ponta inexistente (relação antes do nó) recebe `SEAL_CONTENT_MISMATCH`; o que falhou é a ordem de commit. Declarar ordem (nó antes de relação) ou nomear o motivo.
- **B3 MENOR** — Cabeçalho desatualizado (Q-1..Q-9; ata §4 já traz) e `SEAL_RECORD_NOT_IN_SEAL` atribuído a Andraus sem constar na ata → marcar `[PROPOSTA]` ou registrar fonte. Parte mecânica por FICHA-M (B3a, B3b).
- **B4 MENOR** — Item 4 (b) é leitura da errata além da Q-3 da ata; listar em PENDENTE com premissa.
- **B5 MENOR** — Tabela M da `relation_record` sem linha `publication.*` (fora de M).

Não verificável pelo Revisor: contagens 13/6/13/19/23 e fidelidade do Anexo V1.0 ao commit `ee50ecb`. Encaminhamento: Especificador (classe O); nova revisão por delta, integral só sobre B1.

<!-- ACHADOS-ESTRUTURADOS
B1|MEDIA|C04|Mapa de formato cobre só from/to; causal.outcome_ref entra em M sem regra de forma (record_ref x id do KG); M(r) de CAUSA com desfecho não reconstruível de forma determinística|Ao fechar achado de projeção M, listar TODOS os campos-ponteiro (from, to, target_relation_id, outcome_ref) e conferir cada um contra o Mapa de formato
B2|MENOR|C02|Ponta inexistente (relação antes do nó) recebe SEAL_CONTENT_MISMATCH, contrariando 'código diz o que falhou'; ordem de commit nó antes de relação não declarada|Declarar pré-condição de ordem de commit e nomear o motivo por código ou log
B3|MENOR|C07|Cabeçalho cita só Q-1/2/3/8/9 e diz que a ata não traz Q-1..Q-9 (obsoleto, ata §4 traz); SEAL_RECORD_NOT_IN_SEAL atribuído a Andraus sem constar na ata|Conferir a ata vigente antes de afirmar o que ela traz ou não traz; marcar PROPOSTA o que não consta
B4|MENOR|C08|Item 4(b) é leitura da errata além de Q-3 da ata mas fica em Decididas, com condicional na nota|Listar leituras ampliadas de decisão de Andraus em PENDENTE com premissa
B5|MENOR|C04|Tabela M da relation_record sem linha para publication.* criado pela E-2(b)|Ao criar campo novo num registro, incluí-lo na tabela de projeção desse registro
-->

<!-- FICHA-M
{"achados":[
{"id":"B3a","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"Incorpora as respostas de Andraus a Q-1, Q-2, Q-3, Q-8 e Q-9.","novo":"Incorpora as respostas de Andraus a Q-1..Q-9 (Q-4..Q-7 em mensagem posterior do mesmo dia; ata DHR-RETRO-001 §4).","condicao":"texto antigo ocorre uma única vez, no cabeçalho (linha Versão desta errata)"},
{"id":"B3b","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"**Falta registrar em ata:** o texto atual de DHR-RETRO-001 (§1–§3) não traz Q-1..Q-9. Registrar essas respostas em ata antes da homologação cabe ao Orquestrador (AGENTS.md §10). `[INFERÊNCIA — achado desta redação]`","novo":"**Registrado em ata:** DHR-RETRO-001 §4 traz Q-1..Q-9; Q-10 e o código `SEAL_SUCCESSION_MISMATCH` seguem pendentes. `[FONTE]`","condicao":"texto antigo ocorre uma única vez, na linha Decisões de Andraus incorporadas"}
]}
-->
