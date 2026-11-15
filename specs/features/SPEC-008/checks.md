# checks.md — Verificação de Spec da SPEC-008 (fase spec-first)

**Objeto:** `specs/features/SPEC-008/plan.md` **v1.2 (CANDIDATA — rodada R3: correção do parecer R2; aguarda Revisor rodada 3 e homologação de Andraus)** (Manager — Despacho e Ciclo, Fase 1).
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe/FSM bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-11-15 (v1.0: 2026-11-08; v1.1: 2026-11-14)
**Ordem de Andraus:** chat 2026-11-08, "Avançar" (via Orquestrador). Abertura: DHR-SPEC008-001. Pai: MMC-001 v1.0 (DHR-SPEC008-002; errata R3-m07, DHR-SPEC008-003). Decisões registradas em ata: DN-1/DN-2 — DHR-SPEC008-004; F-1..F-4 — DHR-FIBFRAC-001 §1; DN-3 — DHR-FIBFRAC-002 §1.
**Regra deste arquivo (lição SPEC-049 R1-M01 / C05):** nenhum ✔ sem linha de evidência (número de linha do `plan.md` **v1.2 final** ou resultado de Grep). O que não foi executado aparece como **NÃO VERIFICADO**, nunca como ✔. Histórico de rodadas: `HISTORICO.md` (C06).

**Contagens declaradas (Grep no `plan.md` v1.2, 2026-11-15):** **1** INV-MDC (`^INV-MDC-01:` — l.328), **11** RULE-MDC (`^RULE-MDC-0nn:` — l.360..623), **13** EARS (`^N. (MDC`/`(INV-MDC` — l.653..665), **12** BASpec (`^### BASpec-MDC-` — l.716..939), **9** EC (`^### EC-MDC-` — l.1523..1652), **23** cenários D7 (`^### Cenário-MDC-T` — l.1133..1348), **15** ADV D8 (`^### ADV-MDC-` — l.1364..1499). Soma = 84. Blocos `CLASSE :` = 12 (onze D; uma C l.952).
**Medida do corpo (RULE-ECC-07):** **1.885 linhas** depois dos Menores R3-m01/m02/m03/m06 (ordem de Andraus 2026-11-15; v1.2 do R3 = 1.883; última linha "Pronto para revisão", l.1885; nenhuma seção `## Anexo`; as linhas citadas neste arquivo são as da v1.2 do R3 e se deslocam no máximo +2 depois da l.655) — > 1.600 (confirmado por Andraus, P-3), < 1.900 (alerta; folga 15), < 2.000 (teto). **A reconferir** pelo Orquestrador com `scripts/check_dimensionamento.py`. Atenção: margem pequena — qualquer acréscimo numa R4 passa do alerta.

---

## 0. Tabela fato → locais (C01 — conferida por Grep depois da última edição)

| Fato | Fonte | Locais no Plan | Conferência pós-redação (Grep no `plan.md` v1.2) |
|---|---|---|---|
| **F1** Encerramento antes de `EM_RISCO` = sem estado novo, sem rótulo final até DN-1; ciclo encerrado não aceita evento | DHR-SPEC008-001 P-12; MMC-001 §3.2.3; DHR-SPEC008-004 §1/§2 (DN-1 = decidir depois, com a SPEC-014, não fechada) | RULE-MDC-007 (d); D5 (leitura + F28); EC-MDC-003 POSTCOND; contrato `cycle_closed`; Perguntas DN-1; R-18; §7-bis | Grep "DN-1" = 20 linhas; nenhuma atribui RECUSADO/EXPIRADO como fato (recomendação só na pergunta DN-1) ✔ |
| **F2** θ sem número; campo comparado = `global_conviction` `[INFERÊNCIA]`; `gate_result`/`thresholds_used` ignorados | DHR-SPEC008-001 §3 (ii); P-5; INV-03; CCM-001 Cap.3/Cap.4 e nota N1/N3 | CC-02; CC-03; Termo 4; INHERITS; RULE-MDC-005 (c)(d); D4.4; EARS 6; BASpec-005; EC-009; Fixture CV1; T01; T08 (b); CF-E; TRACE-06 | nenhum dígito associado a θ ✔ |
| **F3** Fase 1 nunca origina ciclo; ruptura: só detecta e avisa | P-12; MMC-001 §4; **DHR-SPEC008-004 §1** (DN-2) | RULE-MDC-001 (c); INV-MDC-01; RULE-MDC-004 (d); EARS 5; T13, T18; ADV-10 (i); Perguntas DN-2; Incorporação; TRACE-06 | DN-2 citada pela ata em Incorporação, Decisões abertas, TRACE-06 e Perguntas ✔ |
| **F4** Níveis: E2 (pedido, despacho, transição, tempo, entrega, macro); E1 (livro, aviso); E3 (trava); BASpec-009 = E2 | atomic-spec §10.2 | cabeçalhos das BASpecs (l.716..939); EC LEVEL; Escala; CC-11 | iguais à Escala ✔ |
| **F5** Allowlist = seis capacidades, enum CAP 1:1, cada uma com EC | MMC-001 §2.2/§5/§6.4-a/§6.6 | INV-MDC-01 (l.328); contrato `capability_audit_record` (l.1091) e `capability_registry`; BASpec-012; EC-008; tabela "Capacidade → EC" (l.1666) | PERMITIDAS = READ_BLACKBOARD, PUBLISH_OWN, WRITE_OWN_LOG, INVOKE_MACRO, TIME_REQUEST, NOTICE_LOCAL — mesma ordem (1)..(6) de INV-MDC-01; NEGADAS = os 10 subs de `MDC_EFFECT_FORBIDDEN` + MODEL_CALL + CLOCK_READ ✔ |
| **F6** `MARK_CONSUMED` só com alarme disparado e vivo; MARK_CONSUMED de ENC que falhe ⇒ sem reenvio | P-12; WF-A02 | RULE-MDC-006 (d)(f)(g)(h); RULE-MDC-007 (d); D5 (nota, F20, nota "Falha de `time_request`"); Interface; EC-004 PRECOND/FAILURE-MODE; T13, T21, T23 (c), ADV-12 (c) | Grep "MARK_CONSUMED" = 35 linhas; Interface e EC-004 PRECOND listam o mesmo conjunto ✔ |
| **F7** Estados = WF-F02; nenhuma seta de volta | WF-F02 | RULE-MDC-007 (a)(e); D5; ADV-13 | D5 (l.992–1030, 39 linhas F01..F38 com F08a/F08b): F30–F38 só ENC ou "sem transição" ✔ |
| **F8** Sem relógio; `clock_reads` do runtime | P-9 | RULE-MDC-010 (c); INV-MDC-01; contrato; ADV-14; EC-005/008 | ✔ |
| **F9** Medida 1.883 / alerta 1.900 / teto 2.000 | RULE-ECC-07 | Dimensionamento; este checks | mesmos valores ✔ |
| **F10** Disposições do backlog | ABERTURA §9 | "Nota de gate" | cinco Disposições inalteradas; motivo do BL-026 acrescido de F-4/CF-D ✔ |
| **F11** Orçamento (rodadas, tempo) + `budget_ref` no pedido | SPEC-048 v1.4 | RULE-MDC-003 (a); RULE-MDC-008 (a); parâmetros + reconciliação; INHERITS; Requisitos; contrato; EC-002; T01 | ✔ |
| **F12** "Invocação" = pedida; sem nova tentativa macro; reinvocação recusada no passo (7) | RULE-CF-010 | RULE-MDC-005 (a)(e); D4.2 (7); D4.4; F06/F36; EC-009; T22 (c)(d); ADV-06 (a)(b) | ✔ |
| **F13** Contagens da trava = predicados sobre o `capability_audit_record` (enum CAP, `target_workspace`, `object_type`, `outcome`) | parecer R2 R2-M-01 | contrato (l.1091); BASpec-012 GATE (l.956); EC-008 POSTCOND/EVIDENCE; T01; ADV-06/10/11/14 | cada predicado (EXECUTED ⊆ allowlist, model_calls, external_emissions = ORDER_EMISSION, foreign_publications por `target_workspace`, clock_reads) usa só campos/enums do contrato; TIME_REQUEST/NOTICE_LOCAL ≠ ORDER_EMISSION (T15/T16/T18 não violam) ✔ |
| **F14** Decisões de Andraus F-1..F-4 e DN-3 | DHR-FIBFRAC-001 §1; DHR-FIBFRAC-002 §1 | Incorporação; CC-01; WORKFLOW (WF-02/03, WF-04, WF-R01); D1; RULE-MDC-001 (a); RULE-MDC-002 (e)(f); BASpec-002; BL-026; T04 (c), T05; R-13; CF-D; Decisões abertas; TRACE-06; Perguntas DN-3 | Grep "FIBONACCI" = 0; citação F-1 idêntica à ata (inclui "Elliot", "servira", sem ponto final); DN-3 = decidida (sem `[DECISÃO NECESSÁRIA]`); parte fractal da P-11, J-001, WF-D03, BL-026, N-001 em aberto ✔ |
| **F15** (R3) Falha de `time_request`: evento `TIME_REQUEST_FAILED`, linha F38, contador `failures[TEMPO]`, teto `max_consecutive_failures`, estouro F20 | parecer R2 R2-M-02 | RULE-MDC-003 (h); RULE-MDC-008 (a); D4.2 (5b); D4.3; D5 F38/F20 + nota; EC-004 FAILURE-MODE; Interface T-10; D3.1; T23 | mesma definição em todos ✔ |
| **F16** (R3) Contadores ANTES da guarda/efeito | parecer R2 R2-m02 | D4.2 (5b)/(6); D4.3; F33/F34/F38 "já incrementado no (5b)"; T15 (a)(c); T23 (b) | simulação na D4.2 e nos cenários dá Fmax + 1 tentativas ✔ |

---

## 1. Condições do Plan (DHR-SPEC008-001 §3 e ordem de serviço)

| # | Condição | Âncora no Plan v1.2 | Estado |
|---|---|---|---|
| 1 | Plan só por ordem expressa; Manager Contract antes | cabeçalho; Herança (l.147) | ✔ (registro na ata = Orquestrador) |
| 2 | Gate `validate_spec_sot.py` | §3 abaixo (conferência manual) | **NÃO VERIFICADO por execução** — sem Bash |
| 3 | J-001/N-001 abertas; "conclusivo" sem número | F2 | ✔ |
| 4 | Teto 2.000 / alerta 1.900 | F9 (1.883) | ✔ (a reconferir por script) |
| 5 | Interface com a Spec de Tempo como `[PROPOSTA]` | seção (l.1044); T-9..T-11 | ✔ |
| 6 | Errata de re-apontamento só aqui, aditiva | "Proposta de errata aditiva" (l.1737) | ✔ |
| 7 | FSM em tabela; toda ação mapeada; sem "reset" | D5 (39 linhas); §5 abaixo | ✔ |
| 8 | Herança MMC-001 v1.0; conservação do conjunto | Herança/Delta (l.147) + "Conservação do pai" | ✔ |
| 9 | Nenhuma BASpec H/P | 12 blocos `CLASSE :` — 11 D, 1 C | ✔ |
| 10 | Fronteiras CONF-1/P-12/CONF-5 | D5 Dono; RULE-MDC-011 (c); Interface | ✔ |
| 11 | Respostas de Andraus aplicadas sem fechar o que segue aberto | Incorporação (DHR-SPEC008-004; DHR-FIBFRAC-001/002); Perguntas | ✔ |
| 12 | Nenhuma decisão aberta fechada | §6 abaixo | ✔ |
| 13 | Todo EC com campo de registro que prove a execução | EVIDENCE/POSTCOND usam só campos do contrato lógico ou do `capability_audit_record` (enum CAP e campos declarados — F13) | ✔ quanto à especificação; existência do registro no runtime = requisito (BUILD/SPEC-040) — **NÃO VERIFICÁVEL** nesta fase |
| 14 | Pesquisa não refeita; fontes por ID | "Classificação das fontes externas" | ✔ |

---

## 2. Código ↔ cenário (C05)

| Código (§D3.1) | Cenário com VERIFICAÇÃO | Estado |
|---|---|---|
| `MDC_REQUEST_INCOMPLETE`/`MDC_FIELD_MISSING`, `MDC_REQUEST_ORIGIN_NOT_ALLOWED`, `MDC_LIMITS_NOT_CONFIGURED`, `MDC_GRAPH_VERSION_UNREGISTERED`, `MDC_TIME_SERVICE_UNAVAILABLE` | T02 (a)–(f) | ✔ |
| `MDC_CYCLE_ALREADY_ACTIVE` | T03 (a) | ✔ |
| `MDC_GRAPH_CYCLIC`, `MDC_GRAPH_HIERARCHY_VIOLATION` | T04 | ✔ |
| `MDC_NO_OPPORTUNITY`, `MDC_OPPORTUNITY_UNDETERMINED` | T06 | ✔ |
| `MDC_DIRECTIONAL_CONFLICT_NEUTRAL` | T07 | ✔ |
| `MDC_MACRO_NOT_CONCLUSIVE` (3 subs) | T08 | ✔ |
| `MDC_MACRO_INVOCATION_FAILED` | T22 (c) | ✔ |
| `MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE` (+ `MDC_CONTEXT_LOST`) | T09 (a); T21; ADV-15 | ✔ |
| `MDC_ALARM_FIELDS_INCOMPLETE` | T09 (b) | ✔ |
| `MDC_TRIGGER_OUTSIDE_WINDOW` | T10 (a) | ✔ |
| `MDC_NOT_PHASE1_TRANSITION` | T11 (b) | ✔ |
| `MDC_SETUP_MISALIGNED` (4 subs; só com hipótese elegível) | T12 (a)–(d) | ✔ |
| `MDC_ALARM_EXPIRED`, `MDC_ALARM_CANCELLED` | T13 (a)–(e) | ✔ |
| `MDC_STAGE_DEADLINE_EXCEEDED` | T14 (a); T22 (d) | ✔ |
| `MDC_GUARD_NOT_SATISFIED` (novo R3) | T14 (b) | ✔ |
| `MDC_LIMIT_EXCEEDED` (3 subs) | T15 (a)–(c); T23 (b) | ✔ |
| `MDC_DISPATCH_PUBLISH_FAILED`, `MDC_AGENT_ERROR` | T22 (a)(b); T15 (c) | ✔ |
| `MDC_TIME_REQUEST_FAILED` (novo R3) | T23 (a)–(c) | ✔ |
| `MDC_COST_BUDGET_EXCEEDED` | T16; ADV-09 | ✔ |
| `MDC_CYCLE_RECORD_UNAVAILABLE` | T17 (b) | ✔ |
| `MDC_DOMINANT_RUPTURE_DETECTED` | T18 | ✔ |
| `MDC_CYCLE_CLOSED` | T19; ADV-13; ADV-06 (b); T13 (c)(d); T21; ADV-15 | ✔ |
| `MDC_STOP_BY_ANDRAUS`, `MDC_STOP_COMMAND_NOT_AUTHENTICATED` | T20; T23 (c) | ✔ |
| `MDC_DUPLICATE_IGNORED` | ADV-01; ADV-06 (c) | ✔ |
| `MDC_EVENT_FOREIGN_CYCLE` | ADV-03, ADV-05 (a)(c), ADV-07 | ✔ |
| `MDC_EVENT_ENVELOPE_INVALID` | ADV-04 | ✔ |
| `MDC_TRANSITION_NOT_LISTED` | ADV-05 (b) | ✔ |
| `MDC_MACRO_ALREADY_INVOKED` | ADV-06 (a)(b) — recusa da ação no passo (7) da D4.2 | ✔ |
| `MDC_ICT_HYPOTHESIS_REJECTED` | ADV-08 | ✔ |
| `MDC_EFFECT_FORBIDDEN` (10 subs) | ADV-10 (a)–(j) | ✔ |
| `MDC_MODEL_CALL_FORBIDDEN` | ADV-11 | ✔ |
| `MDC_CAPABILITY_CHECK_FAILED` (2 subs) | ADV-12 (a)–(c) | ✔ |
| `MDC_CLOCK_READ_FORBIDDEN` | ADV-14 | ✔ |
| Falso-DENY E3 (ENF-07) | ADV-10 (k); EC-008 | ✔ — taxa INDETERMINADA (gap aberto) |

**Simulação passo a passo da D4.2 (R1-m06 / R2-m02 / R2-m03 / R3-m01, refeita em 2026-11-15 sobre TODOS os cenários que citam código de passo):** (0) vale só para notificação do Event Bus; eventos internos não passam por ele (R3-m06). ADV-04 → (0); ADV-01, ADV-06 (c) → (1) (só a 1ª publicação por `dispatch_key`); ADV-03, ADV-05 (a)(c), ADV-07 → (2); T19 (`ALARM_TRIGGERED` e `STAGE_TIMER_FIRED` tardios: `event_id` novo, `request_key` do ciclo — na v1.2 o 2º evento era "PUB(INSTITUCIONAL) atrasada", que pararia no (1) com `MDC_DUPLICATE_IGNORED`: o ✔ abaixo era falso e foi corrigido trocando o evento, R3-m01), T13 (c)(d) (1ª publicação do OPERACIONAL depois do ENC), ADV-06 (b), ADV-13, cancelamentos tardios de T21/ADV-15 → (3); T23 (c): a recusa do `MARK_CONSUMED` do ENC é resultado do efeito da própria F22 (passo (9)), não evento — não passa pelo (3) (R3-m02); T11 (b) → (4); ADV-05 (b) → (5); T15 (c) e T23 (b) → (5b): falha k ⇒ contador = k, k ≤ Fmax ⇒ F33/F38, k = Fmax + 1 ⇒ F20 (tentativas = Fmax + 1); T14 (b) → (6) guarda falsa ⇒ `MDC_GUARD_NOT_SATISFIED`; T15 (a) → (6) `steps` + 1 > Smax ⇒ F20, despacho não ocorre; T10 (a) → (6) guarda de F14 (linha listada, sem transição); ADV-06 (a) e ADV-12 (c) → (7). Depois da correção R3-m01, nenhum cenário espera código de passo posterior ao que o pararia ✔ (conferido cenário a cenário na lista acima).

---

## 3. Gate estrutural — conferência MANUAL contra `scripts/validate_spec_sot.py` (não executado)

| Check | Regra do script | Evidência no `plan.md` v1.2 | Estado (manual) |
|---|---|---|---|
| STRUCT-01 | complexidade CRITICAL + profundidade-alvo | l.20 | ✔ |
| STRUCT-02 | "Constitution Check"; "elliott"; "conviction … J-001/pendente" | l.128; CC-01; CC-03 | ✔ |
| STRUCT-03 | etiquetas | `[FONTE]`, `[INFERÊNCIA]`, `[PROPOSTA]`, `[DECISÃO NECESSÁRIA]`, `[EXTERNO]` | ✔ |
| STRUCT-04 | EARS | EARS 1–13 (l.653..665) | ✔ |
| STRUCT-05 | QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR | 12 BASpecs | ✔ |
| STRUCT-06 | 8 campos de EC | EC-MDC-001..009 (l.1523..1652) | ✔ |
| STRUCT-07 | nenhum limiar "60/75" | nenhum | ✔ |
| STRUCT-08 | marcador de status | "FATO NORMATIVO", "documentado ≠ homologado", `[DECISÃO NECESSÁRIA]` | ✔ |
| STRUCT-09 | profundidade ≤ teto | D0–D8 com CRITICAL | ✔ |
| STRUCT-10 | IDs `[A-Z]-\d{3}` abertos com marca de pendência ≤200 chars, sem fechamento colado | novas ocorrências da R3 não acrescentam ID de decisão aberta; ID de ata (DHR-…) não casa o padrão `\b[A-Z]-\d{3}\b`; "Q-005" não usado | ✔ |
| STRUCT-11 | `research.md` com "Dossiê de Pesquisa" | inalterado | ✔ |
| STRUCT-12 | régua RULE-ECC-06 | inalterado | **NÃO VERIFICADO por execução** |
| STRUCT-13 | BL-nnn + `Disposição:` | "Nota de gate" | ✔ |
| STRUCT-14 | `CLASSE : X` com MECANISMO, CRITÉRIO 4Es (C: + GATE DE SAÍDA) | C em l.952, GATE DE SAÍDA l.956 | ✔ |

---

## 4. Matriz de rastreio (regra → EARS → BASpec → EC → cenários)

| Regra | EARS | BASpec | EC | D7 | D8 |
|---|---|---|---|---|---|
| RULE-MDC-001 | 1 | 001 | 001 | T01, T02, T03 | ADV-10 (i), ADV-12 |
| RULE-MDC-002 | 2 | 002 | 002 | T01, T04, T05 | — |
| RULE-MDC-003 | 3 | 003 | 002, 004 | T01, T14, T15 (b)(c), T22 (a)(b), T23 | ADV-01..05 |
| RULE-MDC-004 | 4, 5 | 004 | 002, 007 | T06, T10, T18 | ADV-07 |
| RULE-MDC-005 | 6 | 005 | 009, 003 | T07, T08, T22 (c)(d) | ADV-06 |
| RULE-MDC-006 | 7, 8 | 006 | 004, 003 | T09, T12, T13, T21 | ADV-08, ADV-15 |
| RULE-MDC-007 | 9 | 007 | 003 | T01, T14 (b), T19 | ADV-05, ADV-13 |
| RULE-MDC-008 | 10 | 008 | 002, 004, 007 | T15, T16, T23 (b) | ADV-09 |
| RULE-MDC-009 | 11 | 009 | 003, 007 | T06 (b), T08, T20, T23 (c) | ADV-10 (j) |
| RULE-MDC-010 | 11 | 010 | 005 | T14, T17 | ADV-02, ADV-14 |
| RULE-MDC-011 | 12 | 011 | 006 | T11 | ADV-10 (f)(g)(h) |
| INV-MDC-01 | 13 | 012 | 008 | T01 | ADV-06 (a), ADV-10, ADV-11, ADV-12, ADV-14 |

Nenhuma regra sem BASpec, EC e cenário; nenhum cenário órfão.

---

## 5. Máquina de estados (C10)

- [x] Tabela estado × evento × guarda → próximo/ENC, com código e dono (D5, l.986–1034).
- [x] Toda ação de efeito mapeia numa linha: despacho (F01, F03, F13), republicação (F33), novo `attempt` (F34), invocação macro (F06), `ARM_ALARM` (F09), reenvio de `time_request` (F38), `MARK_CONSUMED` (F16, F17; F19, F20, F22, F35 em `ATIVADO`; F30 com alarme disparado), handoff (F16), aviso (F20, F21, F35), timer (F01, F03, F06, F09, F13). Conferido contra a Interface (l.1044..) e EC-004 PRECOND ✔.
- [x] **Falha de cada capacidade com efeito (allowlist) tem caminho fechado na D5:** (2) publicação → `DISPATCH_PUBLISH_FAILED`/F33 → F20; resposta de erro do agente analítico → F34 → F20; (3) livro indisponível → sem efeito (RULE-MDC-010 (b); T17 (b)); (4) macro → `MACRO_ERROR`/F36 ou silêncio → F19 (timer de F06); (5) `time_request` → `TIME_REQUEST_FAILED`/F38 → F20, e `MARK_CONSUMED` de ENC sem reenvio (T23 (c)); (6) `notice` → `MDC_NOTICE_PENDING` sem mudar o estado (EC-007); conferência de capacidade falha → F37. Evidência: D5 F20/F33–F38 + notas (l.1032) ✔.
- [x] **Nenhuma espera sem timer:** toda espera pede `STAGE_TIMER` (F01, F03, F06, F09, F13); se o pedido do timer falhar, F38 reenvia na hora até Fmax + 1 tentativas e depois F20 (ENC) — nenhuma espera fica aberta sem timer (RULE-MDC-009 (e)) ✔.
- [x] Cruzamento alarme × estado do ciclo (nota l.1032) ✔. Elegibilidade reconferida em F12/F13/F16/F17 e F30 ✔.
- [x] Guarda falsa em par listado ⇒ `MDC_GUARD_NOT_SATISFIED` (RULE-MDC-007 (b); T14 (b)) ✔.
- [x] Nenhuma seta de volta (nota l.1034; ADV-13); nenhum estado fora de WF-F02 ✔.
- [x] Dono por linha: F01–F23, F27–F38 = SPEC-008; F24–F25 = SPEC-014; F26 = RISK-SPEC ✔.
- [x] Ramos de WF-F01: 1 = F04; 2 = F08a; 3 = F17 (e F19 em `ATIVADO`); 4 = F26; 5 = F15, F31, F32 (EXPIRED); 6 = fora (P-13) ✔.
- [ ] Rótulo final dos ENC — **pendente (DN-1, decidir depois com a SPEC-014 — DHR-SPEC008-004)**; decisão aberta, não falha.

---

## 6. CONS-01 — decisões abertas

| Decisão | Como aparece | Estado |
|---|---|---|
| J-001, N-001 | θ sem número; `score` não usado | ✔ ABERTAS |
| BL-029 (nota do CCM-001) | citada (RULE-MDC-005 (d)); CF-E registra que a precondição GATED_PASS é da Fase 2 | ✔ não resolvida |
| G-001, M-001, SPEC-015-SCOPE, C-001, WF-D03, K-001, SPEC-045-RUNTIME-001, ECC-03-001, D-PCC-4 | como na v1.1 | ✔ ABERTAS |
| P-11 (parte fractal), P-13 | "decidir depois" | ✔ não fechadas |
| DN-1 | `[DECISÃO NECESSÁRIA]` (DHR-SPEC008-004 §2: não fechada) | ✔ aberta |
| DN-2 | decidida — DHR-SPEC008-004 §1 | ✔ registrada com ata |
| DN-3 | decidida — DHR-FIBFRAC-002 §1 (roteiro v1 confirmado) | ✔ registrada com ata |
| F-1..F-4 | DHR-FIBFRAC-001 §1; F-4 diverge de WF-R01 → CF-D (só Andraus) | ✔ nada fechado |
| BL-026 | em espera; CF-B/CF-D | ✔ |
| DNs novas | nenhuma | ✔ |

---

## 7. Herança (CC-08) — ponteiro

Tabela "Conservação do pai" cobre MMC-001 §1–§7 e §10 com evidência. REMOVED e MODIFIED vazios. INHERITS com SPEC-048 v1.4 e SPEC-007 v2.3. §7-bis Bloco B no Plan ✔.

---

## 8. O que NÃO foi verificado (para o Orquestrador)

- Nenhum script executado (Especificador sem Bash): `validate_spec_sot.py`, `revisor_gate.py`, `pre_entrega.py`, `check_repo_research.py`, `backlog_triggers.py --abertura SPEC-008`, `check_dimensionamento.py`, `check_refs.py`, `check_doc_sync.py`, `check_invariants.py`, `build_map.py --check`.
- Linhas da SPEC-003 na errata = foto de 2026-11-08.
- Existência futura do `capability_audit_record` e da confirmação síncrona de `time_request` (T-10) — requisitos ao runtime/Spec de Tempo.

---

## 9. Varredura de fronteira com Specs BASELINE (C04/M4)

| Spec | Ocorrência | Tratamento no Plan |
|---|---|---|
| SPEC-048 v1.4 | "SPEC-008: fornecer orçamento (rodadas, tempo) no pedido"; `query_request.budget_ref (SPEC-008)`; orçamento de recursos/latência = SPEC-008/043 | RULE-MDC-003 (a); RULE-MDC-008 (a); parâmetros + reconciliação; INHERITS; Requisitos ✔ |
| SPEC-007 v2.3 | `max_retrieval_rounds` "orçamento da SPEC-008" | RULE-MDC-008 (a) `[INFERÊNCIA]`; Requisitos ✔ |
| SPEC-005 v1.0 | orquestração = SPEC-008; RULE-CEB-010 | RULE-MDC-003; reconciliação de latência ✔ |
| SPEC-004 v1.2 | orquestração = SPEC-008 | RULE-MDC-002/003/007 ✔ |
| SPEC-003 v1.5 | RULE-CF-010 | RULE-MDC-005; EC-009 ✔ |
