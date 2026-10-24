# checks.md — Verificação de Spec da SPEC-048 (fase spec-first)

**Objeto:** `specs/features/SPEC-048/plan.md` **v1.2 (CANDIDATA — correção da rodada 2; aguarda Revisor rodada 3, por delta contra o commit 0c5adfd, e homologação de Andraus)** (RAG Retrieval & Evidence Packet Harness). *[v1.1: "v1.1 (CANDIDATA — correção da rodada 1; aguarda Revisor rodada 2, por delta contra o commit b1a0231, e homologação de Andraus)"]*
**Parecer tratado na v1.2:** R2 `governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R2-2026-10-24.md` (NÃO CONFORME — 1 Média N-01, 5 Menores n-02..n-06). Contagens inalteradas. *[v1.0: "v1.0 (CANDIDATA — primeira entrega do Plan; aguarda Revisor rodada 1, integral, e homologação de Andraus)"]*
**Parecer tratado:** R1 `governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-PLAN-R1-2026-10-24.md` (NÃO CONFORME — 3 Médias M-01..M-03, 14 Menores m-01..m-14, adendo m-15).
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-10-24
**Ordem de Andraus:** chat 2026-10-24, "Plan da SPEC-048" (transmitida pelo Orquestrador). Decisões posteriores refletidas: DHR-SPEC007-006 (Q7(c) FECHADA — livro só por ato de liberação) e DHR-SPEC007-007 (princípio de autenticação criptográfica dos atos; mecanismo = BUILD).
**Contagens declaradas (por cabeçalho/linha em coluna 0 — contadas na redação; a reconferir no ambiente pai):** **12** RULE-RET (`^RULE-RET-` em bloco: 001–012), **1** INV-RET (`^INV-RET-01`), **12** BASpec (`^### BASpec-RET-`), **12** EARS (`^N. (RET-`), **8** EC (`^### EC-RET-`: 001–008), **14 cenários** (`^### Cenário-RET-T`: T01–T14), **23 ADV** (`^### ADV-RET-`: 01–23) *[v1.0: "vinte e dois ADV (01–22)"; ADV-RET-23 acrescentado na v1.1 — M-01]*. Estados locais de D5: `Q_RECEBIDA`, `Q_RECUPERANDO`, `Q_VALIDANDO`, `Q_ENTREGUE`, `Q_NEGADA` (`Q_MONTADO` da v1.0 substituído — M-02).

---

## R2 — verificação das correções (v1.2)

| Achado | Âncora no Plan v1.2 | Positivo / negativo | Estado |
|---|---|---|---|
| **N-01** desfecho duplo da síntese sem rótulo | RULE-RET-004 "AFIRMAÇÕES DA SÍNTESE" (a) gate / (b) rede de segurança; RULE-RET-010 GATE; BASpec-RET-010; EARS 10; §D3.1; EC-RET-006 | ADV-RET-04 positivo / (a)(b) `SYNTHESIS_CLAIM_INVALID` com entrada injetável; (c) `SYNTHESIS_CLAIM_UNLABELED`, não entregue | ✔ — conferir por leitura: cada condição tem um código e um efeito, iguais nos cinco lugares |
| n-02 | contrato `delivery_record` (`guard_run_ref`, `acts_snapshot_ref`, `guard_evaluated_at`); EC-RET-002/003 EVIDENCE | T13(a); ADV-RET-23 | ✔ |
| n-03 | RULE-RET-005 "FRESCOR DO REENVIO"; `packet_assembled_at` | T13(a) | ✔ (escolha declarada: "como montado em t0") |
| n-04 | D5 (`Q_RECUPERANDO → Q_NEGADA`; novo `query_id` por pedido; repetição após `Q_NEGADA`); `query_record.replay_of` | T13(a) | ✔ |
| n-05 | Termo 9 da acepção; linha das lições reescrita | — | ✔ |
| n-06 | RULE-RET-005 "RECÁLCULO NO PACOTE NOVO"; D4.4 (7); BASpec-RET-006 QUANDO e VERIFICADO POR | ADV-RET-23 | ✔ |

## R1 — verificação das correções (v1.1)

| Achado | Âncora no Plan v1.1 | Positivo / negativo | Estado |
|---|---|---|---|
| **M-01** reenvio contornava a guarda | RULE-RET-005 "REENVIO" (i)(ii)(iii); RULE-RET-006 (d); EARS 5; BASpec-RET-005; D4.4 (7); D5; EC-RET-002/003; contrato `delivery_kind`/`supersedes_packet` | T13(a) / ADV-RET-23 | ✔ estrutural — reenvio = nova transmissão sob a guarda E3 |
| **M-02** D5 contraditório | D5 com `Q_VALIDANDO` (entra antes da aprovação); RULE-RET-004; T04 | T03 / T04 | ✔ — toda transição tem origem e destino coerentes; T04 alcançável |
| **M-03** síntese sem rótulo | RULE-RET-004 "AFIRMAÇÕES DA SÍNTESE"; RULE-RET-010 GATE; BASpec-RET-010; EARS 10; contrato; EC-RET-006 | ADV-RET-05(d) / ADV-RET-04 | ✔ |
| m-01..m-15 | tabela "Correções da rodada 1" do Plan | — | ✔ |

> **Natureza dos ✔ abaixo:** estruturais e condicionados. O que depende de Andraus aparece como "Aberto"; os positivos com estado partem da **Fixture Q0** (estado injetado, D7), que não afirma que esse estado já exista (hoje: T01, pacote vazio).

---

## 1. Condições obrigatórias do Plan (ABERTURA §15; DHR-SPEC048-001 §3)

| # | Condição | Âncora no Plan v1.0 | Estado |
|---|---|---|---|
| 1 | Ponto 3 da Interface transcrito literal | RULE-RET-007 "TRANSCRIÇÃO LITERAL"; "Contrato com a SPEC-007" ponto 3. Âncora: SPEC-007 `plan.md` l.1226 (l.1224 antes da nota C-3) | ✔ — comparar caractere a caractere com a célula da SPEC-007 |
| 2 | RULE-CBP-002/004/005 e RULE-BB-001 dispostas uma a uma | Herança/Delta REMOVED (3, fundamento P-9 — DHR-SPEC007-003, com forma remanescente) + "NÃO REMOVIDO" (RULE-BB-001 em INHERITS); §7-bis Bloco B | ✔ estrutural; vigência só na homologação (RULE-HD-03) |
| 3 | Falso-ACEITE do juiz F2 por amostragem, sem número | RULE-RET-011; BASpec-RET-011; EC-RET-007; D4.5; T14; ADV-RET-18 | ✔ (taxa INDETERMINADA) |
| 4 | Errata/metade F2 coordenada com a F1 da SPEC-020 | "Texto único por linha da SPEC-020"; seção da emenda metade F2 | ✔ (um texto por linha, válido para as duas metades) |
| 5 | Disposição de BL-017 e BL-010 | Nota de gate `[STRUCT-13]` (+ BL-011, BL-029) | ✔ — conferir com `backlog_triggers --abertura SPEC-048` |
| 6 | Lacuna analista↔modelo; padrão "fora" | RULE-RET-006 (a); contrato `consumer_binding`; P-1; T10; ADV-RET-16 | ✔ (Aberto: P-1) |
| 7 | Errata pelos critérios 1 e 2, reconferidos | seção da errata (busca de 2026-10-24; critério 2 sem novidade além das notas C-3) | ✔ |
| 8 | Página de leitura só como regra de consumo | Non-goals; RULE-RET-004; "Interface com a SPEC-049" (requisito inverso); ADV-RET-19 | ✔ |

## 2. Mapeamento do Anexo T

| Verificação | Estado |
|---|---|
| Todo item de T.1–T.13 tem destino (048 com ID novo, ou 049) | ✔ tabela "Mapeamento do Anexo T" |
| Nenhum ID `RULE-KFH-*`/`BASpec-KFH-*`/`EC-KFH-*`/`Cenário-KFH-*`/`ADV-KFH-*` reutilizado como ID vigente | ✔ (IDs KFH aparecem só como origem/fonte) |
| Partes só da página de leitura (RULE-KFH-015, EARS 15, BASpec-KFH-015, EC-KFH-009, T21, partes de ADV-11/25, cláusulas de INV-KFH-02/RULE-KFH-016, R-8 "2ª verdade", 2 códigos) → SPEC-049 | ✔ (C-1) |
| Pendências (a)–(f) do Anexo T (l.1954) dispostas | ✔ parágrafo após a tabela |

## 3. Constitution Check e herança

| Item | Verificação | Estado |
|---|---|---|
| CC-01..CC-12 | presentes; N/A justificados (CC-06/07/12) | ✔ |
| CC-03 | Conviction Vector pendente (J-001 ABERTA); nada da trilha entra nele (RULE-RET-008) | ✔ |
| CC-08 | INHERITS por ID+versão; REMOVED com referência a decisão de Andraus; MODIFIED vazio | ✔ estrutural |
| CC-11 | Classe por BASpec: D = 002, 003, 004, 005, 012; C = 006, 007, 008; H = 001, 009, 010, 011 *[v1.0: 011 era D — m-10]* | ✔ |
| H com BOUNDED LOOP + GATE DE SAÍDA | 001 (`max_retrieval_rounds`), 009 (`max_f2_judge_attempts`), 010 (`max_synthesis_attempts`), 011 (`max_audit_rejudge_attempts`) | ✔ |
| C com GATE DE SAÍDA | 006, 007, 008 | ✔ |
| Mesma expressão de manutenção da F2 | RULE-RET-009, BASpec-RET-009 GATE DE SAÍDA, EC-RET-006 PRECOND — cinco conjunções, mesma ordem | ✔ — conferir por leitura |

## 4. BASpecs, EARS, EC

| BASpec | Regra | EARS | Classe | EC | Positivo | Negativo próprio |
|---|---|---|---|---|---|---|
| 001 | RULE-RET-001 | 1 | H | EC-RET-001 (E2) | — | T07; permutação inválida (na BASpec); ADV-RET-02/03 |
| 002 | RULE-RET-002 | 2 | D | EC-RET-001 (E2) | P1/U1 (na BASpec) | U3/U9 (na BASpec); T11; ADV-RET-11/12/14 |
| 003 | RULE-RET-003 | 3 | D | (sem efeito próprio — compõe o pacote, EC-RET-002) | T02 | ADV-RET-09 |
| 004 | RULE-RET-004 | 4 | D | EC-RET-002 (E2) | T01, T03 | T04; ADV-RET-05(a)/12 |
| 005 | RULE-RET-005 | 5 | D | EC-RET-002 (E2) + EC-RET-003 no reenvio | T03, T13(a) | T13(b); ADV-RET-06; ADV-RET-23 |
| 006 | RULE-RET-006 | 6 | C | EC-RET-003 (E3) | T10, T13(a) | ADV-RET-16; ADV-RET-23 |
| 007 | RULE-RET-007 / INV-RET-01 | 7 | C | EC-RET-004 (E3) | caso próprio na BASpec | ADV-RET-01/02/22 |
| 008 | RULE-RET-008 | 8 | C | EC-RET-005 (E3) | T03 | ADV-RET-10 |
| 009 | RULE-RET-009 | 9 | H | EC-RET-006 (E2) | T06 (c1/c2) | T05; ADV-RET-07/08/15 |
| 010 | RULE-RET-010 | 10 | H | EC-RET-006 (E2) | T03 (desligada), T09, ADV-RET-05(d) | ADV-RET-04/15/21 |
| 011 | RULE-RET-011 | 11 | H *[v1.0: D]* | EC-RET-007 (E2) | T14 | ADV-RET-18 |
| 012 | RULE-RET-012 | 12 | D | EC-RET-008 (E2) | T08 | ADV-RET-13 |

- Todo EC tem os 8 campos; os E3 (003, 004, 005) declaram POLICY e falso-DENY amostral (ENF-07); escala E0–E3 em seção própria (ENF-08). ✔
- Pisos: entrega do pacote E2; guardas E3 (ABERTURA §4). ✔

## 5. CONS-01 e decisões

| Item | Estado |
|---|---|
| M-001, K-001, G-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção | Abertas — nenhuma tratada como fechada ✔ |
| Mecanismo de autenticação dos atos | Aberto (BUILD); princípio decidido (DHR-SPEC007-007) citado, não especificado ✔ |
| Q7(c) | FECHADA (DHR-SPEC007-006); o livro entra só por ato RIGHTS + EXT_TRANSMISSION de Andraus ✔ |
| P-1, P-2, P-3 (novas) | [DECISÃO NECESSÁRIA] com fail-closed no intervalo e pergunta em linguagem de trader ✔ |

## 6. Gates a rodar pelo Orquestrador (sem Bash aqui)

```
python scripts/validate_spec_sot.py specs/features/SPEC-048/plan.md
python scripts/revisor_gate.py specs/features/SPEC-048/plan.md
python scripts/check_invariants.py specs/features/SPEC-048/plan.md
python scripts/check_refs.py
python scripts/check_doc_sync.py
python scripts/check_repo_research.py --all
python scripts/backlog_triggers.py --abertura SPEC-048     # esperado: BL-010 e BL-017
python scripts/build_map.py && python scripts/build_map.py --check
python -m unittest discover -s tests     # inclui a calibração dos detectores (contagens)
npm test && npm run lint
```
