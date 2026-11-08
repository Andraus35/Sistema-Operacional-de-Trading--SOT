# checks.md — Verificação de Spec da SPEC-008 (fase spec-first)

**Objeto:** `specs/features/SPEC-008/plan.md` **v1.0 (CANDIDATA — primeira entrega do Plan; aguarda Revisor rodada 1, integral, e homologação de Andraus)** (Manager — Despacho e Ciclo, Fase 1).
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe/FSM bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-11-08
**Ordem de Andraus:** chat 2026-11-08, "Avançar" (via Orquestrador). Abertura: DHR-SPEC008-001 (CRITICAL D0–D8, um documento). Pai: MMC-001 v1.0 (DHR-SPEC008-002; errata R3-m07, DHR-SPEC008-003).
**Regra deste arquivo (lição SPEC-049 R1-M01 / C05):** nenhum ✔ sem linha de evidência (número de linha do `plan.md` v1.0 ou resultado de Grep). O que não foi executado aparece como **NÃO VERIFICADO**, nunca como ✔.

**Contagens declaradas (Grep no `plan.md` após a redação, 2026-11-08):** **1** INV-MDC (`^INV-MDC-01:` — l.313), **11** RULE-MDC (`^RULE-MDC-0nn:` — l.337..533), **13** EARS (`^N. (MDC`/`(INV-MDC` — l.560..572), **12** BASpec (`^### BASpec-MDC-` — l.619..836), **8** EC (`^### EC-MDC-` — l.1306..1403), **20** cenários D7 (`^### Cenário-MDC-T` — l.983..1155), **14** ADV D8 (`^### ADV-MDC-` — l.1167..1283). Soma dos padrões = 79 (Grep de contagem). Blocos `CLASSE :` = 12 (onze D, uma C — l.629..848).
**Medida do corpo (RULE-ECC-07):** **1.626 linhas** (arquivo inteiro; contagem de linhas por Grep; nenhuma seção `## Anexo`) — > 1.600 (confirmado por Andraus, P-3), < 1.900 (alerta), < 2.000 (teto). **A reconferir** pelo Orquestrador com `scripts/check_dimensionamento.py`.

---

## 0. Tabela fato → locais (C01 — montada antes da redação, conferida por Grep depois)

| Fato | Fonte | Locais no Plan | Conferência pós-redação (Grep no `plan.md`) |
|---|---|---|---|
| **F1** Encerramento antes de `EM_RISCO` = sem estado novo, sem rótulo final até DN-1; `wf_f02_final_label` = AUSENTE; ciclo encerrado não aceita evento | DHR-SPEC008-001 P-12; MMC-001 §3.2.3; ABERTURA §13 P-12 (contexto) | RULE-MDC-007 (d); D5 (leitura + F28); EC-MDC-003 POSTCOND; contrato `cycle_closed`; T06/T19; Perguntas DN-1; riscos R-18; §7-bis B | "DN-1": l.98, 200, 478, 746, 880, 909, 946, 962, 1341, 1476, 1527, 1537, 1559, 1562, 1571, 1584, 1590 — todos dizem "rótulo final = decisão de Andraus"; nenhuma linha atribui RECUSADO/EXPIRADO como fato ✔ |
| **F2** θ = `macro_conclusive_threshold`, parâmetro por ativo, **sem número**; limiares-piloto do sinal ≠ θ | DHR-SPEC008-001 §3 (ii); P-5; INV-03 | CC-03 (l.122); Acepção Termo 4; RULE-MDC-005 (c); tabela de parâmetros (l.545+); D4.4; T08; Fixture (símbolo θ) | nenhum dígito associado a θ (Grep "θ" — só símbolos `θ`, `θ + δ`, `θ − δ`) ✔ |
| **F3** A Fase 1 nunca origina ciclo (nem rearme) | P-12; MMC-001 §4 | RULE-MDC-001 (c); INV-MDC-01 (sub `CYCLE_ORIGINATION`); RULE-MDC-004 (d); RULE-MDC-007 (e); T13, T18; ADV-10 (i); DN-2 | por leitura nos locais citados — mesma afirmação; DN-2 pergunta exceção sem decidi-la ✔ |
| **F4** Pisos: despacho/transição/pedido de tempo/pedido de ciclo/entrega E2; livro e aviso E1; trava E3 | ABERTURA §4 (orientação); atomic-spec §10.2 | cabeçalho dos BASpecs `[E1/E2/E3]` (l.619..836); EC-MDC-001..008 LEVEL; Escala E0–E3 (l.1422); CC-11 | BASpec-009/010 = E1; 012 = E3; demais E2; EC-005/007 = E1; EC-008 = E3; demais E2 — iguais à Escala ✔ |
| **F5** Allowlist da trava = seis capacidades (ler; publicar no próprio workspace; gravar o próprio livro; invocar leitura macro; pedir à Spec de Tempo; avisar Andraus) | MMC-001 §2.2/§5/§6.4-a/§6.6 | INV-MDC-01 (l.313); BASpec-MDC-012 (l.849 "seis capacidades"); EC-MDC-008 CAPABILITY/PRECOND; contrato `capability_registry` (allowlist[6]) | "allowlist": l.314, 331, 572, 839, 849, 851, 967, 977, 1254, 1407, 1408, 1410 — mesma lista ✔ |
| **F6** `MARK_CONSUMED`: em F16, F17 e em todo ENC em `ATIVADO` (F19, F20, F22); nunca em `ARMADO` | P-12 ("usado") | RULE-MDC-006 (d)(f); RULE-MDC-007 (d) (acrescentado na redação); D5 (nota + linhas); Interface (tabela); EC-MDC-004 PRECOND; EC-MDC-006; T01, T12, T20 | Grep "MARK_CONSUMED": 18 linhas; a regra-fonte de ENC em `ATIVADO` foi **acrescentada** à RULE-MDC-007 (d) após o Grep mostrar que só D5 a dizia (correção C01 feita antes da entrega) ✔ |
| **F7** Estados = exatamente os de WF-F02; nenhuma seta de volta | WF-F02; MMC-001 §3.2.3 | RULE-MDC-007 (a)(e); D5; ADV-13; CC-02 | D5 (l.878–917): estados usados ⊆ {AGUARDANDO, CONTEXTO_FORMADO, ARMADO, ATIVADO, EM_SÍNTESE, EM_RISCO, SINAL_ENVIADO, RECUSADO, EXPIRADO}; nenhuma linha com "Próximo" = ARMADO a partir de ATIVADO/ENC (nota l.917) ✔ |
| **F8** Sem relógio: instantes só de evento/timer da Spec de Tempo | research §3.4/§3.6; P-9 | RULE-MDC-010 (c); INV-MDC-01 (`MDC_CLOCK_READ_FORBIDDEN`); D4.2; Interface T-2; T14, T17; ADV-14; EC-MDC-005/008 | por leitura nos locais citados ✔ |
| **F9** Medida 1.626 / alerta 1.900 / teto 2.000 / estimativa ≈1.895 | RULES.md RULE-ECC-07; ABERTURA §3; P-3 | Dimensionamento (l.36+); este checks | mesmos valores ✔ |
| **F10** Disposições do backlog: BL-026 PARCIAL; BL-043 FORA; BL-044/045/046 REFERÊNCIA | ABERTURA §9; DHR-SPEC008-001 §2 | "Nota de gate" (l.103+) — uma linha por BL com `Disposição:` | cinco linhas, cada uma com BL-nnn + `Disposição: <valor>` + motivo (formato de `plan_declara`) ✔ |

---

## 1. Condições do Plan (DHR-SPEC008-001 §3 e ordem de serviço)

| # | Condição | Âncora no Plan v1.0 | Estado |
|---|---|---|---|
| 1 | Plan só por ordem expressa; Manager Contract antes | cabeçalho "Ordem de Andraus"; Herança (pai MMC-001 v1.0) | ✔ (registro na ata = Orquestrador) |
| 2 | Gate `validate_spec_sot.py` sobre o `plan.md` | §3 abaixo (conferência manual) | **NÃO VERIFICADO por execução** — sem Bash |
| 3 | J-001/N-001 abertas; "conclusivo" sem número | F2 | ✔ |
| 4 | Teto 2.000 / alerta 1.900; acima, parar | F9 (1.626) | ✔ (medida a reconferir por script) |
| 5 | Interface com a Spec de Tempo como `[PROPOSTA]`; relógio não especificado | seção "Interface com a Spec de Tempo" (l.925); D1 Non-goals | ✔ |
| 6 | Errata de re-apontamento só aqui, aditiva, texto antigo→novo | "Proposta de errata aditiva" (l.1489): E-1 (9 linhas da SPEC-003, ocorrência literal → leitura), E-2 (BL-026), E-3 (SPEC-002/006/020 e BL-017: zero ocorrências) | ✔ — Grep de "SPEC-008/015" na SPEC-003 em 2026-11-08 = as 11 linhas da tabela do research §8.3 (9 RE + 2 HIST com essa grafia) |
| 7 | FSM em tabela verificável; toda ação mapeada; sem "reset" | D5 (30 linhas: F01..F29, com F08a/F08b); §5 abaixo | ✔ |
| 8 | Herança MMC-001 v1.0 por ID+versão; conservação do conjunto; Classe D/C = orientação | Herança/Delta (l.137) + tabela "Conservação do pai" (l.187) | ✔ |
| 9 | Nenhuma BASpec H/P | 12 blocos `CLASSE :` — 11 D, 1 C (l.629..848) | ✔ |
| 10 | Fronteiras CONF-1/P-12/CONF-5 como decisões desta Spec (fronteira vigente para SPEC-014/015) | D5 coluna Dono; RULE-MDC-011 (c); Interface | ✔ |
| 11 | Respostas homologadas aplicadas como estão; P-11/P-13 sem fechar | "Incorporação das decisões" (l.49); RULE-MDC-002 (e); D1 Non-goals | ✔ |
| 12 | Nenhuma decisão aberta fechada | §6 abaixo | ✔ |
| 13 | Todo EC com campo de registro que prove a execução; recusas da trava com código e cenário | EC EVIDENCE citam campos do contrato (`cycle_log_entry`, `capability_check_ref`, contagens); §2 abaixo | ✔ |
| 14 | Pesquisa não refeita; fontes do Dossiê citadas por ID | tabela "Classificação das fontes externas" (l.1444) | ✔ |

---

## 2. Código ↔ cenário (C05 — todo caminho fail-closed tem código na §D3.1 e cenário)

> Conferido por Grep de `"MDC_[A-Z_]+"` nas linhas VERIFICAÇÃO de D7/D8 (47 ocorrências) + leitura das subs abreviadas de ADV-10.

| Código (§D3.1) | Cenário com VERIFICAÇÃO | Estado |
|---|---|---|
| `MDC_REQUEST_INCOMPLETE`/`MDC_FIELD_MISSING`, `MDC_REQUEST_ORIGIN_NOT_ALLOWED`, `MDC_LIMITS_NOT_CONFIGURED`, `MDC_GRAPH_VERSION_UNREGISTERED`, `MDC_TIME_SERVICE_UNAVAILABLE` | T02 (a)–(f) | ✔ |
| `MDC_CYCLE_ALREADY_ACTIVE` | T03 (a) | ✔ |
| `MDC_GRAPH_CYCLIC`, `MDC_GRAPH_HIERARCHY_VIOLATION` | T04 | ✔ |
| `MDC_NO_OPPORTUNITY`, `MDC_OPPORTUNITY_UNDETERMINED` | T06 | ✔ |
| `MDC_DIRECTIONAL_CONFLICT_NEUTRAL` | T07 | ✔ |
| `MDC_MACRO_NOT_CONCLUSIVE` (3 subs) | T08 (a)(b)(c) | ✔ |
| `MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE`, `MDC_ALARM_FIELDS_INCOMPLETE` | T09 | ✔ |
| `MDC_TRIGGER_OUTSIDE_WINDOW` | T10 (a) | ✔ |
| `MDC_NOT_PHASE1_TRANSITION` | T11 (b) | ✔ |
| `MDC_SETUP_MISALIGNED` (4 subs) | T12 (a)–(d) | ✔ |
| `MDC_ALARM_EXPIRED`, `MDC_ALARM_CANCELLED` | T13 | ✔ |
| `MDC_STAGE_DEADLINE_EXCEEDED` | T14 | ✔ |
| `MDC_LIMIT_EXCEEDED` (3 subs) | T15 | ✔ |
| `MDC_COST_BUDGET_EXCEEDED` | T16; ADV-09 | ✔ |
| `MDC_CYCLE_RECORD_UNAVAILABLE` | T17 (b) | ✔ |
| `MDC_DOMINANT_RUPTURE_DETECTED` | T18 | ✔ |
| `MDC_CYCLE_CLOSED` | T19; ADV-13 | ✔ |
| `MDC_STOP_BY_ANDRAUS`, `MDC_STOP_COMMAND_NOT_AUTHENTICATED` | T20 | ✔ |
| `MDC_DUPLICATE_IGNORED` | ADV-01 | ✔ |
| `MDC_EVENT_FOREIGN_CYCLE` | ADV-03, ADV-05 (a), ADV-07 | ✔ |
| `MDC_EVENT_ENVELOPE_INVALID` | ADV-04 | ✔ |
| `MDC_TRANSITION_NOT_LISTED` | ADV-05 (b), ADV-07 | ✔ |
| `MDC_MACRO_ALREADY_INVOKED` | ADV-06 | ✔ |
| `MDC_ICT_HYPOTHESIS_REJECTED` | ADV-08 | ✔ |
| `MDC_EFFECT_FORBIDDEN` (10 subs) | ADV-10 (a)–(j) | ✔ |
| `MDC_MODEL_CALL_FORBIDDEN` | ADV-11 | ✔ |
| `MDC_CAPABILITY_CHECK_FAILED` (2 subs) | ADV-12 (a)(b) | ✔ |
| `MDC_CLOCK_READ_FORBIDDEN` | ADV-14 | ✔ |
| Falso-DENY E3 (ENF-07) | ADV-10 (k); EC-MDC-008 FAILURE-MODE (referência independente: lista fechada de INV-MDC-01 + ciclo T01) | ✔ — taxa INDETERMINADA (gap aberto) |

---

## 3. Gate estrutural — conferência MANUAL linha a linha contra `scripts/validate_spec_sot.py` (não executado)

| Check | Regra do script | Evidência no `plan.md` | Estado (manual) |
|---|---|---|---|
| STRUCT-01 | `complexidade [|:=] CRITICAL` e `profundidade-alvo [|:=] D\d` | tabela do cabeçalho + linha "Complexidade: CRITICAL. Profundidade-alvo: D0–D8" (l.20) | ✔ (manual) |
| STRUCT-02 | "Constitution Check"; "elliott"; "conviction … (pendente\|J-001\|…\|aberto)" | l.118; CC-01 cita Elliott; CC-03 "Conviction Vector (J-001 ABERTA, pendente)" | ✔ (manual) |
| STRUCT-03 | ao menos uma etiqueta | `[FONTE]`, `[INFERÊNCIA]`, `[PROPOSTA]`, `[DECISÃO NECESSÁRIA]`, `[EXTERNO]` presentes | ✔ (manual) |
| STRUCT-04 | EARS "quando …, … DEVE" | EARS 1–13 (l.560..572) | ✔ (manual) |
| STRUCT-05 | QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR | 12 BASpecs | ✔ (manual) |
| STRUCT-06 | efeito ⇒ 8 campos de EC | EC-MDC-001..008 com CAPABILITY…EVIDENCE | ✔ (manual) |
| STRUCT-07 | nenhum limiar "estrutural ≥60", "total ≥75", "conviction … 60/75%" | Grep: nenhum desses padrões | ✔ (manual) |
| STRUCT-08 | marcador de status | "FATO NORMATIVO", "documentado ≠ homologado", `[DECISÃO NECESSÁRIA]` | ✔ (manual) |
| STRUCT-09 | profundidade ≤ teto da complexidade | D0–D8 com CRITICAL (teto D8) | ✔ (manual) |
| STRUCT-10 | IDs `[A-Z]-\d{3}` abertos com marca de pendência ≤200 chars, sem "fechada" colada | Grep: só J-001, N-001, G-001, M-001, C-001, K-001 (todas com "ABERTA(S)" no contexto — ex.: l.13, 26, 56–57, 82, 122, 433, 547, 556, 1531–1534) e I-001 (FECHADA no ROADMAP — livre). Nenhum ID `Q-00n`/`B-001`/`H-001` usado; IDs próprios (DN-n, CF-A/B/C, TK-nn) fora do padrão | ✔ (manual) |
| STRUCT-11 | cita RULE-ECC-01/02 ⇒ `research.md` com "Dossiê de Pesquisa" | `research.md` na pasta; Grep "Dossiê de Pesquisa" = 1 | ✔ (manual) |
| STRUCT-12 | régua RULE-ECC-06 sobre `sources/REPO-*.txt` | 5 capturas REPO no Dossiê (4 elegíveis, 1 não) — homologadas com a abertura | **NÃO VERIFICADO por execução** (`check_repo_research.py`) |
| STRUCT-13 | linha com BL-nnn + `Disposição: (INCORPORADO\|PARCIAL\|REFERÊNCIA\|FORA)` para BL-026/043/044/045/046 | "Nota de gate" — uma linha por item | ✔ (manual); escopo a reconferir com `backlog_triggers.py --abertura SPEC-008` |
| STRUCT-14 | todo `CLASSE : X` com MECANISMO e CRITÉRIO 4Es (C: + GATE DE SAÍDA), antes de VERIFICADO POR | 12 blocos; o único C (l.848) tem GATE DE SAÍDA (l.851) | ✔ (manual) |

---

## 4. Matriz de rastreio (regra → EARS → BASpec → EC → cenários)

| Regra | EARS | BASpec | EC | D7 | D8 |
|---|---|---|---|---|---|
| RULE-MDC-001 | 1 | 001 | 001 | T01, T02, T03 | ADV-10 (i), ADV-12 |
| RULE-MDC-002 | 2 | 002 | 002 | T01, T04, T05 | — |
| RULE-MDC-003 | 3 | 003 | 002 | T01, T14 | ADV-01..05 |
| RULE-MDC-004 | 4, 5 | 004 | 002, 007 | T06, T10, T18 | ADV-07 |
| RULE-MDC-005 | 6 | 005 | 003 | T07, T08 | ADV-06 |
| RULE-MDC-006 | 7, 8 | 006 | 004 | T09, T12, T13 | ADV-08 |
| RULE-MDC-007 | 9 | 007 | 003 | T01, T19 | ADV-05, ADV-13 |
| RULE-MDC-008 | 10 | 008 | 002, 007 | T15, T16 | ADV-09 |
| RULE-MDC-009 | 11 | 009 | 007 | T06 (b), T08, T20 | ADV-10 (j) |
| RULE-MDC-010 | 11 | 010 | 005 | T14, T17 | ADV-02, ADV-14 |
| RULE-MDC-011 | 12 | 011 | 006 | T11 | ADV-10 (f)(g)(h) |
| INV-MDC-01 | 13 | 012 | 008 | — | ADV-10, ADV-11, ADV-12, ADV-14 |

Nenhuma regra sem BASpec, EC e cenário; nenhum cenário órfão (cada um cita a regra no título). Tasks TK-01..12 → BASpecs (Plan, "Tasks").

---

## 5. Máquina de estados (C10)

- [x] Tabela estado × evento × guarda → próximo/ENC, com código e dono (D5, l.878–917).
- [x] Toda ação de efeito mapeia numa linha: despacho (F01, F03, F13), invocação macro (F06), `ARM_ALARM` (F09), `MARK_CONSUMED` (F16, F17, F19, F20, F22), handoff (F16), aviso (F20, F21), timer (F01, F03, F09, F13) — conferido contra a tabela "Interface com a Spec de Tempo" (coluna "Uso") ✔.
- [x] Nenhuma seta de volta (nota l.917; ADV-13) ✔. Nenhum estado fora de WF-F02 (F7) ✔.
- [x] Dono por linha: F01–F23, F27–F29 = SPEC-008; F24–F25 = SPEC-014; F26 = RISK-SPEC (CONF-1) ✔.
- [x] Os seis ramos de WF-F01: 1 = F04; 2 = F08a; 3 = F17 (e F19 em `ATIVADO`); 4 = F26 (RISK-SPEC); 5 = F15; 6 = fora (P-13) ✔.
- [ ] Rótulo final dos ENC — **pendente de Andraus (DN-1)**; não é falha da tabela, é decisão aberta declarada.

---

## 6. CONS-01 — decisões abertas

| Decisão | Como aparece | Estado |
|---|---|---|
| J-001, N-001 | θ sem número; fórmula/pesos/limiares definitivos pendentes | ✔ ABERTAS |
| G-001, M-001 | guarda do livro = SPEC-009; `domain_state` não definido | ✔ ABERTAS |
| SPEC-015-SCOPE, C-001, WF-D03 | origem/repetição na SPEC-015; só redação; só invocação | ✔ ABERTAS |
| K-001, SPEC-045-RUNTIME-001, ECC-03-001, D-PCC-4 | não tocadas | ✔ ABERTAS |
| P-11, P-13 | "decidir depois" (grafo como dado; ramo 6 fora) | ✔ não fechadas |
| DN-1, DN-2, DN-3 (novas) | `[DECISÃO NECESSÁRIA]` com recomendação; fail-closed até a decisão | ✔ não fechadas |

---

## 7. Herança (CC-08) — ponteiro

Tabela "Conservação do pai" (l.187) cobre MMC-001 §1, §1-bis, §2.1–§2.6, §3, §3.1.1–§3.1.4, §3.2.1–§3.2.3, as nove linhas do §4, §5.1–§5.6, §6.1–§6.6 (com §6.4-a e as duas partes do §6.6), §7 e §10 — cada uma com evidência. REMOVED e MODIFIED vazios. §7-bis Bloco B no Plan. ✔

---

## 8. O que NÃO foi verificado (para o Orquestrador)

- Nenhum script foi executado (Especificador sem Bash): `validate_spec_sot.py`, `pre_entrega.py`, `check_repo_research.py`, `backlog_triggers.py --abertura SPEC-008`, `check_dimensionamento.py`, `check_refs.py`, `check_doc_sync.py`, `check_invariants.py`, `build_map.py --check`. As contagens e a medida acima são de Grep do próprio Especificador.
- Os números de linha da SPEC-003 na errata são foto de 2026-11-08 (Grep); a regra de busca do research §8.3 manda refazer a busca ao aplicar a errata.
- Veracidade das fontes web do Dossiê: risco residual já declarado na abertura (DHR-SPEC008-001 §4).
