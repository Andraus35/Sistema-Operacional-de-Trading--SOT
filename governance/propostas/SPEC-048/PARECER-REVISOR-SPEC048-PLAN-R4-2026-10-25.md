# Parecer do Revisor — Plan da SPEC-048 v1.3 (CANDIDATO), rodada 4 (S2, por delta contra 51e20e3) — 2026-10-25

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura; recuperado do transcrito do agente após reinício do contêiner). **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 2 Menores novas (n-10, n-11). Teto: M-001, K-001, J-001 e demais decisões abertas, e o registro em ata das respostas de Andraus a P-1..P-3. Não é homologação. Gate não executado pelo Revisor (o Orquestrador rodou: PASSOU_D, 13/13, suíte completa verde); sem `git diff` (leitura direta dos blocos tocados e Grep das ocorrências dependentes).

## Conferido
**n-07 corrigido no essencial:** RULE-RET-005 (l.558-576) define a "consulta de referência" como a que gravou o pacote ENTREGUE mais recente do par (request_id, fingerprint); R1 = SEMPRE REENVIO (reentrega do pacote da referência, passando de novo pela guarda, nunca nova recuperação; segundo packet_id só pelo caso (ii) com `supersedes_packet`); R2 = par sem entrega e última consulta em `Q_NEGADA` ⇒ pedido novo; R3 = consulta em curso (`Q_RECUPERANDO`/`Q_VALIDANDO`) ⇒ `REQUEST_IN_PROGRESS`; R4 = `REQUEST_ID_REUSE_CONFLICT` sem reabrir nem criar referência; reenvio negado não muda a referência. Sem estado novo (D5 l.1097 só reescreve "Sai para"). Campos: `replay_of` (T13(c)), `packets_created == 1` (T13(a)(c)), T13(d)(e)(f), ADV-RET-23 (acréscimo v1.3), §D3.1 l.772-773, D4.4 (7) l.1085, contrato `query_record`. **n-09(b) corrigido:** RU-10 em §7-bis Bloco C (l.1776); contenção por `packet_assembled_at`/`guard_evaluated_at` visíveis, guarda sempre atual, estado atual só por pedido novo; RU-1..RU-10 batem (l.222 e l.1853). **6 linhas classe M** (FICHA-M-PLAN-R3.json) presentes e intactas (6 ocorrências esperadas, 6 encontradas). Contagens inalteradas (12 RULE, 1 INV, 12 BASpec, 12 EARS, 8 EC, 14 cenários, 23 ADV); T13 ganhou subcasos (c)-(f) sem criar cenário. CONS-01 respeitado ("a registrar na ata de homologação"; texto de P-1..P-3 preservado, INV-07). Bloco C sem achados novos; amostra anti-leniência (RULE-RET-006 (d), BASpec-RET-006, EC-RET-002, §D3.1, D5, Bloco C) sem achado além de n-11.

## Menores novas (não bloqueiam)
- **n-10 (C01/C10)** Precedência entre R1, R2 e R3 não declarada; resíduo de duplicidade de pacote. (a) C1 em curso e um repetido terminado `Q_NEGADA` com `REQUEST_IN_PROGRESS`: um segundo repetido, com C1 ainda em curso, cai na letra de R2 ("par sem consulta de referência e a última consulta do par terminou Q_NEGADA") — abre segunda recuperação concorrente e, se ambas entregarem, dois packet_id para o mesmo par (o defeito do n-07 por outra via). (b) Par COM referência e reenvio já em curso (`Q_VALIDANDO`): R1 diz "sempre reenvio" e R3 "em curso sem entrega" — indefinido; dois reenvios simultâneos no caso (ii) gerariam dois pacotes novos com `supersedes_packet` para o mesmo antigo. T13(d) cobre um repetido e só com `Q_RECUPERANDO`. Fonte: plan.md l.559-573 e l.1351-1353. Ação: R3 como primeira checagem (consulta do par em curso, com ou sem referência); R2 considera só consultas terminadas com desfecho substantivo (ignora negações por `REQUEST_IN_PROGRESS`); subcaso em T13(d) com segundo repetido e com `Q_VALIDANDO`.
- **n-11 (C06/C02)** Resíduos de vocabulário e histórico: D5 l.1097 ("replay_of = consulta anterior") e contrato l.1148 ("query_id anterior") divergem da definição da RULE-RET-005 (referência ou, sem ela, a última consulta do par); linha de correção n-04 (l.55) e checks.md l.30 não carregam a ressalva de que "repetição após Q_NEGADA = pedido novo" só vale sem referência (R2); EC-RET-002 FAILURE-MODE (l.1495-1498) não lista `REQUEST_IN_PROGRESS` nem `REQUEST_ID_REUSE_CONFLICT`. Ação: alinhar ao texto da RULE-RET-005 e anotar a ressalva.

## Não verificável
Gates do Orquestrador (não reexecutados pelo Revisor); fontes web e repositórios do Dossiê; sha256/delta por hash; comparação linha a linha com 51e20e3 (números de linha da ficha M são os de 51e20e3 e já deslocados).

## Pendências (atos de Andraus)
Respostas a P-1, P-2, P-3 (dadas em chat: P-1 só ele analista por analista; P-2 só campos de lista fechada; P-3 resumo para quando ele quiser — a registrar na ata de homologação); emenda metade F2 à SPEC-020; errata de re-apontamento; REMOVED de RULE-CBP-002/004/005 (valem na homologação, RULE-HD-03); registro em ata da ordem de 2026-10-24 para o Plan; confirmar que o Manager conta como "quem pediu".

## Encaminhamento
CONFORME condicional, aguardando Andraus. n-10 e n-11 podem ser corrigidas numa v1.4 curta ou ficar como condição da homologação, à escolha do Orquestrador/Andraus; o Revisor recomenda ao menos n-10 (defeito de idempotência por outra via).

## Achados estruturados (LOOP-001)
<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
n-10|MENOR|C01|Três regras de idempotência (R1/R2/R3) escritas sem ordem de precedência; a correção do n-07 abriu uma via equivalente|G-C matriz de rastreio + G-F tabela de estados: toda regra de decisão sobre o mesmo par declara precedência e tem cenário para cada interseção
n-11|MENOR|C06|Correção do n-07 não propagou o vocabulário (referência × consulta anterior) a D5, contrato, histórico e EC|G-D varredura de impacto: listar todas as ocorrências de termo/predicado redefinido
-->

## Adendo da guarda pós-revisor (Orquestrador, 2026-10-25; DHR-AUDITOR-EXTERNO-018)
- **G2:** `revisor_gate.py` sobre o plan.md = `PASSOU_D`, 0 sinais H, **nenhum achado a confirmar ou descartar** (as 4 verificações informativas apontam para outros arquivos, fora do escopo desta Spec).
