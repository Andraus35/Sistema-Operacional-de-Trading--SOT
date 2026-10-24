# Parecer do Revisor — Plan da SPEC-048 v1.2 (CANDIDATO), rodada 3 (S2, por delta contra 0c5adfd) — 2026-10-24

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 3 Menores novas (n-07..n-09). Não é homologação. O teto vem de M-001, K-001, J-001 e demais decisões abertas e das respostas de Andraus a P-1, P-2 e P-3. Commit revisado: 183c1b4. Gate: Revisor não o executou; o Orquestrador rodou (PASSOU_D, 13/13, suíte completa verde).

## Resolvidos (conferidos)
N-01: um desfecho por condição, igual em todos os lugares — (a) afirmação do modelo com rótulo ou campo fora de {claim_id, attributed_to, text} ⇒ descartada no gate da RULE-RET-010 com `SYNTHESIS_CLAIM_INVALID` e o pacote segue sem ela; (b) afirmação que chega à validação final sem os rótulos gravados pelo harness ⇒ `PACKET_INCOMPLETE/SYNTHESIS_CLAIM_UNLABELED`, pacote não entregue (`Q_VALIDANDO → Q_NEGADA`), declarado como rede de segurança; coerente em RULE-RET-004 (l.494-505), RULE-RET-010 (l.654-662), BASpec-RET-010, EARS 10, §D3.1, EC-RET-006, contrato; ADV-RET-04 com as três entradas injetáveis (a)(b)(c). n-02..n-06: campos `guard_run_ref`/`acts_snapshot_ref`/`guard_evaluated_at` no `delivery_record`; "como montado em t0" com `packet_assembled_at`; D5 com `Q_RECUPERANDO → Q_NEGADA`, `query_id` novo com `replay_of`; Termo 9 dos homônimos (conferidos na SPEC-007 l.1279-1282); recálculo no pacote novo do reenvio (ii); BASpec-RET-006 com reenvio no QUANDO. Contagens 12 RULE-RET, 1 INV-RET, 12 BASpec, 12 EARS, 8 EC, 14 cenários, 23 ADV conferem. Sem regressão; consistente com a SPEC-007 baseline (pontos 3 e 5 literais). CONS-01 respeitado; P-1..P-3 conformes (lado seguro vigente).

## Menores novas (não bloqueiam)
- **n-07** Repetição de pedido: (i) reenvio negado com `Q_NEGADA` (ex.: guarda indisponível, ADV-23(c)) seguido de novo reenvio do mesmo (request_id, fingerprint) segue "consulta anterior em Q_NEGADA → pedido novo" (n-04 c), gerando segundo `packet_id` para o mesmo `request_id` já entregue — contradiz "mesmo par ⇒ mesmo packet_id" e `packets_created == 1` do T13 (defeito de idempotência, sem vazamento); (ii) pedido repetido com a consulta anterior ainda em curso (`Q_RECUPERANDO`/`Q_VALIDANDO`) sem tratamento. Ação: definir "consulta anterior" como a que gravou o pacote do par, ou tratar o reenvio depois de `Q_NEGADA`; caso em T13; dizer se par terminado em `REQUEST_ID_REUSE_CONFLICT` reabre a checagem. **Recomenda ao menos corrigir n-07.**
- **n-08** Mapeamento de verificação incompleto: BASpec-RET-004 (VERIFICADO POR, l.842) não cita ADV-RET-04(c); BASpec-RET-010 (l.996) não cita ADV-RET-04(a)(b); cabeçalho do ADV-RET-04 "(RET-009/010)" omite RET-004; EARS 4 sem a cláusula "afirmação sem rótulos do harness ⇒ não entregue"; RULE-RET-004 (b) diz "SEM os dois rótulos" (convém "sem qualquer um dos dois").
- **n-09** Rastro e riscos: VERIFICAÇÃO do ADV-04 (a)(b) usa `rejected_reason` para pacote entregue, enquanto o EC-RET-006 POSTCOND grava o descarte em `gaps` (alinhar o campo); o reenvio (i) "como montado em t0" não consta como risco residual (entregar de novo item cujo selo, marca de revalidação ou contradição surgiu depois): acrescentar RU-10 ou nota no RU-3/RU-6.

## Não verificável
Gates do Orquestrador (saídas não reexecutadas); veracidade das fontes web e dos repositórios do Dossiê; sha256/delta por hash; varredura completa do RMR-001 por `ATIVADO` além de BL-003 e BL-011 (BL-003: "não tocado, sem disposição" no Plan; encaminhamento original ao gate da SPEC-006). SPEC-002 v1.0 BASELINE confirmada (plan.md l.7/l.19).

## Pendências de Andraus (atos dele)
Respostas a P-1, P-2, P-3; emenda metade F2 à SPEC-020; errata de re-apontamento; REMOVED de RULE-CBP-002/004/005 (RULE-HD-03: valem na homologação); registro em ata da ordem de 2026-10-24 para o Plan; confirmar que o Manager conta como "quem pediu".

## Encaminhamento
CONFORME condicional, aguardando Andraus. As Menores n-07..n-09 podem ser corrigidas na v1.3 ou junto da homologação, à escolha do Orquestrador.

## Achados estruturados (LOOP-001)
<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
n-07|MENOR|C01|Regra de idempotência do reenvio e regra de pedido repetido após Q_NEGADA se contradizem (dois caminhos para o mesmo par)|G-C matriz de rastreio + G-B fechamento de códigos: cada regra de estado tem cenário positivo e negativo e um único desfecho por condição
n-08|MENOR|C04|Correção de um achado (N-01) não propagou as referências cruzadas (BASpec, ADV, EARS) para os demais pontos que restatam a mesma regra|G-D varredura de impacto: listar todas as ocorrências do identificador/predicado alterado
n-09|MENOR|C05|Campo de registro (rejected_reason × gaps) e risco residual da escolha de frescor não declarados; efeito não observável|G-C: EVIDENCE de cada EC cita campos que existem no contrato; risco residual obrigatório por escolha de projeto
-->

## Adendo do Orquestrador (2026-10-24)
Primeiro parecer transcrito sob a regra LOOP-001 (bloco estruturado acima). O ledger `governance/aprendizado/LEDGER-ACHADOS.md` foi regerado no mesmo commit.
