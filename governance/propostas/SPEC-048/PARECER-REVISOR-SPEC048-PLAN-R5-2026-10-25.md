# Parecer do Revisor — Plan da SPEC-048 v1.4, rodada 5 (delta, S2) — 2026-10-25

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). **CONFORME condicional** — não é homologação; nenhuma decisão aberta foi fechada (CONS-01).

RELATÓRIO DE REVISÃO — SPEC-048 Plan v1.4, rodada 5 (S2, por delta contra ece2db1/v1.3) — 2026-10-25 — Revisor SOT

VEREDITO: CONFORME condicional. 0 Críticas, 0 Médias, 0 Menores novas. n-10 e n-11 estão corrigidas, sem regressão visível. Não é homologação. O teto continua o do R4: M-001, K-001, J-001 e demais decisões abertas, mais o registro em ata das respostas de Andraus a P-1..P-3.

1. Gate
- Não executei revisor_gate; a ferramenta não estava disponível nesta sessão (GATE NÃO VERIFICADO por mim).
- Usei o resultado informado pelo Orquestrador (exit 0 em todos os gates, PASSOU_D). Isso mantém o teto de CONFORME condicional.
- Não tive `git diff` nem delta por hash. Li diretamente os blocos tocados e fiz Grep das ocorrências dependentes.

2. n-10 — conferido, corrigido
- Precedência: plan.md l.584-587 fixa R4 → R3 → R1 → R2 → pedido novo. R3 passa a ser a primeira checagem do mesmo par, com ou sem referência (l.578-580).
- R2 só conta desfecho substantivo e ignora negações por `REQUEST_IN_PROGRESS` (l.575-577). R1 exige referência e R2 exige ausência dela, então as duas não se sobrepõem.
- Atomicidade: l.587-590 põe a checagem de R3 e a abertura da consulta na mesma unidade atômica. Daí decorre no máximo uma consulta em curso por par, o que afasta duas recuperações concorrentes e dois reenvios com `supersedes_packet` para o mesmo pacote.
- D5: a linha `Q_RECEBIDA` (l.1119) repete a ordem R4 → R3 → R1 → R2, com R3 inclusive de reenvio e com ou sem referência, e a ressalva de R2 sobre `REQUEST_IN_PROGRESS`. Não há estado novo (5 estados, `Q_`).
- T13 (l.1374-1387):
  - (d2): segundo repetido com a 1ª consulta ainda em `Q_RECUPERANDO` dá `REQUEST_IN_PROGRESS` de novo, com `retrieval_traces == 1` e `packets_created == 1`.
  - (d3): par com referência e reenvio em `Q_VALIDANDO` no caso (ii) dá `REQUEST_IN_PROGRESS` por R3 (que precede R1). Resulta um só pacote com `supersedes_packet == packet_id_1`, com no máximo uma consulta em curso por par.
  - (e) e (f) estão preservados.
  - Os subcasos ficam dentro de T13, que continua sendo um cenário.

3. n-11 — conferido, corrigido
- `replay_of` tem a mesma definição (referência ou, sem ela, a última consulta do par) em l.570, D5 l.1119 e no contrato `query_record` l.1170. O texto anterior está preservado entre colchetes (INV-07).
- Ressalva da n-04: está na l.63 do plan.md (R2 só sem referência, depois de R4 e R3) e na l.38 do checks.md.
- EC-RET-002 FAILURE-MODE (l.1528-1530) lista `REQUEST_IN_PROGRESS` (R3) e `REQUEST_ID_REUSE_CONFLICT` (R4, sem reabrir).
- Grep por "consulta anterior" e "última consulta do par": as ocorrências restantes são o texto novo ou histórico entre colchetes. Não achei resíduo de vocabulário vivo.
- checks.md l.4, l.20-21 e l.38 registram a v1.4. §D3.1 l.795 (`REQUEST_IN_PROGRESS` → RET-005 R3, T13(d)) segue coerente.

4. Contagens revalidadas por Grep (plan.md)
- RULE-RET-001..012: 12.
- INV-RET-01: 1.
- BASpec: 12.
- EC: 8.
- Cenários T: 14 (l.1227 a 1392).
- ADV: 23 (l.1408 a 1474).
- Estados D5: 5.
- Não reconferi os 12 EARS linha a linha; o parecer R4 não os tocou e a v1.4 declara contagens inalteradas.
- Nada foi criado fora do delta: sem ID, regra, estado ou cenário novos. Só texto em RULE-RET-005, D4.4(7), D5, contrato, T13 (subcasos), EC-RET-002 e tabelas de correção e checks.

5. Tabela de cobertura
- Conferido agora, integral: RULE-RET-005 (l.534-606), D5, contrato `query_record`, T13, FAILURE-MODE do EC-RET-002, linhas de correção n-04/n-10/n-11 no plan.md e no checks.md, e contagens.
- Dependentes (Grep): D4.4(7), §D3.1, ADV-RET-23, D6.
- Amostra anti-leniência, reconferida de forma independente: RULE-RET-006 (a)(b), D4.4(7), EC-RET-002 (POSTCOND e EVIDENCE), D5 `Q_RECUPERANDO` e `Q_VALIDANDO`, CONS-01 em P-1..P-3. Sem achado.
- HERDADO (parecer R4, fonte inalterada): os demais blocos, inclusive RU-10 no §7-bis Bloco C (l.1776) e as 6 linhas classe M.
- Não conferido: sha256 do documento, porque não há delta por hash.

6. Bloco C e Passo 5-bis
- EPI, CAU, DEC e as demais disciplinas: sem achados nos blocos tocados. A correção é só de idempotência e vocabulário, sem fronteira de execução.
- Checagem adversarial própria: se duas consultas rodassem em paralelo no mesmo par, a unidade atômica mais o cenário (d2)/(d3) detectariam, via `retrieval_traces == 1` e consultas em curso ≤ 1.
- CONS-01 respeitado: nenhuma decisão aberta foi fechada, e P-1..P-3 seguem "a registrar na ata de homologação".

7. Não verificável por mim
- Gates do Orquestrador, fontes web e repositórios do Dossiê, e o sha256.

8. Pendências de Andraus (inalteradas)
- Respostas a P-1..P-3 em ata.
- Emenda F2 à SPEC-020.
- Errata de re-apontamento.
- REMOVED de RULE-CBP-002/004/005.
- Ata da ordem de 2026-10-24.
- Confirmar que o Manager conta como "quem pediu".

Encaminhamento: CONFORME condicional, aguardando Andraus.

<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
(nenhum achado novo nesta rodada; n-10 e n-11 verificados como corrigidos)
-->

Nenhum FICHA-M: não há achado Menor mecânico.

## Adendo da guarda pós-revisor (Orquestrador, 2026-10-25; DHR-AUDITOR-EXTERNO-018)
- **G2:** `revisor_gate.py` sobre o plan.md = `PASSOU_D`, 0 sinais H, teto CONFORME condicional; **nenhum achado a confirmar ou descartar** (as verificações informativas apontam para outros arquivos, fora do escopo desta Spec).
- **G1:** o Revisor não reabriu o núcleo do Passo 0 nesta rodada por ser **delta** (as rodadas R1–R4 já o auditaram, ver pareceres anteriores). Âncoras dependentes conferidas ao vivo pelo Orquestrador: `ROADMAP.md` (slots SPEC-048/049, l.187-193), `backlog/RMR-001_Painel_Backlog.md` (BL-010/BL-017), `governance/RULES.md` (RULE-ECC-06, RULE-HG-02), `atomic-spec.md` §15 — existem e conferem. Nada a descartar.
