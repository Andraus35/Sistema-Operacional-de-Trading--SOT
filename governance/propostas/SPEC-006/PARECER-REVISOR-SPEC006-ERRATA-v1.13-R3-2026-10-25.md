# Parecer do Revisor — Errata aditiva v1.13 à SPEC-006 (R3, v1.2, delta com B1 integral) — 2026-10-25

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `specs/features/SPEC-006/errata-v1.13.md` v1.2 (commit `f01189d`). Gates do Orquestrador: check_refs 0 ERRO, check_invariants 0, revisor_gate PASSOU_D, suíte completa OK, mapa em dia, `plan.md` intacto (`dd5a609f3007…`). Revisor abriu ROADMAP, atomic-spec, RULES e RMR-001 (G1); `revisor_gate`/hash/git não disponíveis a ele.

**VEREDITO: CONFORME condicional.** Condições: Q-10 (b) e Q-11 (decisões de Andraus) e o gate não reproduzido pelo Revisor. Não é homologação. B1 e B2–B5 do R2 **resolvidos**; sem violação de invariante, salvaguarda ou CONS-01; aditividade confirmada (75 ocorrências, todas em `errata-v1.13.md`).

- **N1 MENOR (C01)** — "a ordem pode ser refeita" contradiz SPEC-007 RULE-KFH-007 (ix) (consumo FALHOU exige novo selo → `SEAL_ALREADY_CONSUMED`); submissão parcial de selo multi-registro não declarada como risco. Trocar por "falha ⇒ consumo FALHOU ⇒ novo selo" e registrar o risco/pergunta para futura errata da SPEC-007. Não mecânico.
- **N2 MENOR (C02)** — regra (2) do Mapa: "veio de outra origem" → "não veio no mesmo selo". Mecânico (FICHA-M).
- **N3 MENOR (C06)** — tabela fato→locais omite propagação ao PRECOND do EC-CKG-001 na linha dos campos-ponteiro. Mecânico (FICHA-M).
- **N4 MENOR (C01/C08)** — Q-10 (c) põe `valid_from` fora de M/atribuído pelo KG, mas SPEC-007 RULE-KFH-007 (vii) usa `valid_from` na chave natural da relação antes da submissão; registrar a dependência para a futura errata da SPEC-007. Não bloqueia. Não mecânico.

<!-- ACHADOS-ESTRUTURADOS
N1|MENOR|C01|Texto diz que a ordem pode ser refeita; SPEC-007 RULE-KFH-007 (ix) diz falha FALHOU exige novo selo; submissão parcial de selo multi-registro não declarada como risco|Ao declarar pré-condição de ordem, conferir o efeito na máquina de estados do consumo do selo da outra Spec
N2|MENOR|C02|Regra (2) do Mapa usa 'outra origem'; deveria ser o complemento de (1), 'não veio no mesmo selo'|Escrever o ramo complementar de uma regra com o mesmo predicado da condição principal
N3|MENOR|C06|Tabela fato→locais omite a nota de propagação ao PRECOND do EC-CKG-001 na linha dos campos-ponteiro|Ao adicionar regra, varrer todos os locais onde o fato se repete, incluindo as notas de propagação
N4|MENOR|C08|Q-10(c) põe valid_from fora de M e atribuído pelo KG, mas SPEC-007 (vii) usa valid_from na chave natural da relação antes da submissão; dependência não registrada|Cruzar decisão que muda a origem de um campo com os consumidores desse campo na Spec vizinha
-->

<!-- FICHA-M
{"achados":[
{"id":"N2","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"(2) Se Y existe e veio de outra origem, o valor em M é o id de Y no KG, literal.","novo":"(2) Se Y existe e não veio no mesmo selo (outro selo ou ciclo de vida canônico), o valor em M é o id de Y no KG, literal.","condicao":"texto antigo ocorre uma única vez, na linha do Mapa de formato 'Campos-ponteiro em M'"},
{"id":"N3","sev":"MENOR","arquivo":"specs/features/SPEC-006/errata-v1.13.md","antigo":"E-3 item 3; Herança (tabela); T09 (e)/(g)","novo":"E-3 item 3; propagação (EC-CKG-001 PRECOND); Herança (tabela); T09 (e)/(g)","condicao":"texto antigo ocorre uma única vez, na linha da tabela fato→locais 'Campos-ponteiro em M'"}
]}
-->
