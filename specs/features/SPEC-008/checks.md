# checks.md — Verificação de Spec da SPEC-008 (fase spec-first)

**Objeto:** `specs/features/SPEC-008/plan.md` **v1.1 (CANDIDATA — rodada R2: correção do parecer R1; aguarda Revisor rodada 2 e homologação de Andraus)** (Manager — Despacho e Ciclo, Fase 1).
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe/FSM bem-formados) — **NÃO** é teste de runtime, **NÃO** é parecer do Revisor, **NÃO** é homologação. "VERIFY" interno = feedback. [FONTE: atomic-spec §14]
**Método:** atomic-spec.md v1.5 · tlc-spec-lean (PLAN = Spec; CHECKS = verificação de spec) · overlay GUS-TLC-001
**Data:** 2026-11-14 (v1.0: 2026-11-08)
**Ordem de Andraus:** chat 2026-11-08, "Avançar" (via Orquestrador). Abertura: DHR-SPEC008-001 (CRITICAL D0–D8, um documento). Pai: MMC-001 v1.0 (DHR-SPEC008-002; errata R3-m07, DHR-SPEC008-003). Respostas a DN-1/2/3: AskUserQuestion 2026-11-08 (via Orquestrador).
**Regra deste arquivo (lição SPEC-049 R1-M01 / C05):** nenhum ✔ sem linha de evidência (número de linha do `plan.md` **v1.1** ou resultado de Grep). O que não foi executado aparece como **NÃO VERIFICADO**, nunca como ✔. Histórico de rodadas: `HISTORICO.md` (C06).

**Contagens declaradas (Grep no `plan.md` v1.1, 2026-11-14):** **1** INV-MDC (`^INV-MDC-01:` — l.326), **11** RULE-MDC (`^RULE-MDC-0nn:` — l.358..613), **13** EARS (`^N. (MDC`/`(INV-MDC` — l.643..655), **12** BASpec (`^### BASpec-MDC-` — l.704..927), **9** EC (`^### EC-MDC-` — l.1476..1602), **22** cenários D7 (`^### Cenário-MDC-T` — l.1104..1302), **15** ADV D8 (`^### ADV-MDC-` — l.1320..1452). Soma = 83. Blocos `CLASSE :` = 12 (onze D; uma C l.940).
**Medida do corpo (RULE-ECC-07):** **1.829 linhas** (última linha do arquivo, "Pronto para revisão", l.1829; nenhuma seção `## Anexo`) — > 1.600 (confirmado por Andraus, P-3), < 1.900 (alerta; folga 71), < 2.000 (teto). Linhas citadas neste arquivo = `plan.md` v1.1 final (após o registro de F-1..F-4). **A reconferir** pelo Orquestrador com `scripts/check_dimensionamento.py`.

---

## 0. Tabela fato → locais (C01 — montada antes da redação, conferida por Grep depois)

| Fato | Fonte | Locais no Plan | Conferência pós-redação (Grep no `plan.md` v1.1) |
|---|---|---|---|
| **F1** Encerramento antes de `EM_RISCO` = sem estado novo, sem rótulo final até DN-1; `wf_f02_final_label` = AUSENTE; ciclo encerrado não aceita evento | DHR-SPEC008-001 P-12; MMC-001 §3.2.3; resposta de Andraus 2026-11-08 (DN-1 = decidir depois, com a SPEC-014) | RULE-MDC-007 (d); D5 (leitura + F28); EC-MDC-003 POSTCOND; contrato `cycle_closed`; Perguntas DN-1; R-18; §7-bis | Grep "DN-1" = 19 linhas; todas dizem "rótulo final = decisão de Andraus / decidir depois"; nenhuma atribui RECUSADO/EXPIRADO como fato (a recomendação aparece só na pergunta DN-1) ✔ |
| **F2** θ sem número; limiares-piloto do sinal ≠ θ; campo comparado = `global_conviction` `[INFERÊNCIA]`; `gate_result`/`thresholds_used` ignorados | DHR-SPEC008-001 §3 (ii); P-5; INV-03; CCM-001 Cap.3/Cap.4 e nota N1/N3 | CC-02; CC-03; Termo 4; INHERITS CCM-001; RULE-MDC-005 (c)(d); D4.4; EARS 6; BASpec-005; EC-MDC-009; Fixture CV1; T01; T08 (b); tabela TRACE-06 | Grep "valor agregado" restante só em RULE-MDC-005 (d) (explicação do nome do campo); nenhum dígito associado a θ ✔ |
| **F3** A Fase 1 nunca origina ciclo (nem rearme); ruptura: só detecta e avisa | P-12; MMC-001 §4; DN-2 (Andraus, 2026-11-08) | RULE-MDC-001 (c); INV-MDC-01; RULE-MDC-004 (d); RULE-MDC-007 (e); EARS 5; T13, T18; ADV-10 (i); Perguntas DN-2; Incorporação | mesma afirmação em todos; DN-2 registrada como decisão, sem mudança de comportamento ✔ |
| **F4** Pisos e níveis: despacho/transição/pedido de tempo/pedido de ciclo/entrega/invocação macro E2; livro e aviso E1; trava E3; BASpec-009 = E2 | ABERTURA §4; atomic-spec §10.2; parecer R1 m-07 | cabeçalhos `[E1/E2/E3]` das BASpecs; EC LEVEL; Escala E0–E3; CC-11 | Grep `^### BASpec-MDC-` (l.704..927): 010 = E1; 009 = E2; 012 = E3; demais E2; EC-005/007 = E1; EC-008 = E3; demais (incl. EC-009) E2 — iguais à Escala ✔ |
| **F5** Allowlist = seis capacidades; cada uma com EC | MMC-001 §2.2/§5/§6.4-a/§6.6; parecer R1 m-07 | INV-MDC-01 (l.326); BASpec-012; EC-008; contrato `capability_registry`; tabela "Capacidade da allowlist → EC" (l.1616) | mesma lista; (1) ler = sem efeito, só trava ✔ |
| **F6** `MARK_CONSUMED`: alarme disparado e vivo (F16, F17; F19, F20, F22, F35 em `ATIVADO`; F30 em `ARMADO`/`ATIVADO`); nunca em `CONTEXTO_FORMADO`/`ARMADO` sem disparo, nem em F32/F37 | P-12; WF-A02 | RULE-MDC-006 (d)(f)(g)(h); RULE-MDC-007 (d); D5 (nota + linhas); Interface; EC-MDC-004 PRECOND; T13, T21, ADV-12 (c) | Grep "MARK_CONSUMED" = 29 linhas; Interface e EC-004 PRECOND listam o mesmo conjunto; RULE-MDC-007 (d) é a regra-fonte ✔ |
| **F7** Estados = WF-F02; nenhuma seta de volta | WF-F02; MMC-001 §3.2.3 | RULE-MDC-007 (a)(e); D5; ADV-13 | D5 (l.973–1020): estados ⊆ WF-F02; F30–F37 só ENC ou "sem transição" ✔ |
| **F8** Sem relógio; contagem `clock_reads` vem do runtime | research §3.4/§3.6; P-9 | RULE-MDC-010 (c); INV-MDC-01; D4.2; T-2; ADV-14; EC-005/008 | EC-005 e ADV-14 citam o `capability_audit_record` ✔ |
| **F9** Medida 1.829 / alerta 1.900 / teto 2.000 | RULE-ECC-07; P-3 | Dimensionamento; este checks | mesmos valores ✔ |
| **F10** Disposições do backlog | ABERTURA §9 | "Nota de gate" | cinco Disposições inalteradas (PARCIAL/FORA/REFERÊNCIA ×3); motivo do BL-026 acrescido de F-4/CF-D (HISTORICO) ✔ |
| **F11** (R2) Orçamento de rodadas e de TEMPO no pedido + `budget_ref` | SPEC-048 v1.4 (Requisitos: "SPEC-008: fornecer orçamento (rodadas, tempo) no pedido"; `query_request.budget_ref`) | RULE-MDC-003 (a); RULE-MDC-008 (a); tabela de parâmetros + reconciliação; INHERITS; Requisitos; contrato `dispatch_request`; EC-002; T01; 4Es e latência | Grep "budget" — mesmas duas chaves {`max_rounds`, `stage_deadline`} + `budget_ref` em todos ✔ |
| **F12** (R2) "Invocação" = pedida; sem nova tentativa macro | RULE-CF-010 (2x por ciclo) | RULE-MDC-005 (a)(e); RULE-MDC-003 (f) (última frase); D4.4; D5 F06/F36; EARS 6; BASpec-005; EC-009; T22 (c)(d); ADV-06 | nenhuma linha manda nova tentativa macro (Grep "nova tentativa" — só nó do despacho) ✔ |
| **F14** (R2) Decisões de Andraus de 2026-11-14: F-1 Fibonacci = skill dos agentes analíticos, sem nó; confluência fractal = decidir depois; F-2 só confere/publica zonas, sub-hipótese sem uso; F-3 leitura macro inalterada; F-4 TFs S1/D1/H4/H1/M5 fixos (diverge de WF-R01) | AskUserQuestion 2026-11-14 (via Orquestrador) | Incorporação (linhas P-11, F-1..F-4); CC-01; tabela WORKFLOW (WF-02/03, WF-04, WF-R01); D1 Non-goals; RULE-MDC-001 (a); RULE-MDC-002 (e)(f); BASpec-002; Nota de gate BL-026; T04 (c), T05 (nó fictício NOVO_X); R-13; CF-D; Decisões abertas; TRACE-06; DN-3 | Grep "FIBONACCI" no plan = 0 (nenhum nó/aresta de Fibonacci); "S1/D1/H4/H1/M5" só em texto de decisão/conflito, nunca como parâmetro; DN-3 segue `[DECISÃO NECESSÁRIA]`; J-001, WF-D03, BL-026, N-001 seguem em aberto ✔ |
| **F13** (R2) Contagens da trava = consultas ao `capability_audit_record` do runtime | parecer R1 M-05 | INV-MDC-01; contrato; BASpec-012 GATE; EC-005/008; T01; ADV-10/11/14; Requisitos (Runtime/SPEC-040); R-20 | toda ocorrência de `model_calls`/`external_emissions`/`foreign_publications`/`clock_reads` em POSTCOND/EVIDENCE/VERIFICAÇÃO cita o registro do runtime ou o contrato ✔ |

---

## 1. Condições do Plan (DHR-SPEC008-001 §3 e ordem de serviço)

| # | Condição | Âncora no Plan v1.1 | Estado |
|---|---|---|---|
| 1 | Plan só por ordem expressa; Manager Contract antes | cabeçalho "Ordem de Andraus"; Herança (pai MMC-001 v1.0) | ✔ (registro na ata = Orquestrador) |
| 2 | Gate `validate_spec_sot.py` sobre o `plan.md` | §3 abaixo (conferência manual) | **NÃO VERIFICADO por execução** — sem Bash |
| 3 | J-001/N-001 abertas; "conclusivo" sem número | F2 | ✔ |
| 4 | Teto 2.000 / alerta 1.900 | F9 (1.829) | ✔ (medida a reconferir por script) |
| 5 | Interface com a Spec de Tempo como `[PROPOSTA]` | seção "Interface com a Spec de Tempo" (l.1030); T-9 novo | ✔ |
| 6 | Errata de re-apontamento só aqui, aditiva | "Proposta de errata aditiva" (l.1687) — inalterada na R2 (só m-04 do Orquestrador) | ✔ |
| 7 | FSM em tabela verificável; toda ação mapeada; sem "reset" | D5 (38 linhas: F01..F37 com F08a/F08b); §5 abaixo | ✔ |
| 8 | Herança MMC-001 v1.0; conservação do conjunto | Herança/Delta (l.145) + "Conservação do pai" | ✔ |
| 9 | Nenhuma BASpec H/P | 12 blocos `CLASSE :` — 11 D, 1 C | ✔ |
| 10 | Fronteiras CONF-1/P-12/CONF-5 | D5 coluna Dono; RULE-MDC-011 (c); Interface | ✔ |
| 11 | Respostas homologadas aplicadas; P-11/P-13 sem fechar; respostas DN de 2026-11-08 aplicadas sem fechar DN-1/DN-3 | "Incorporação das decisões" (linha "Respostas de Andraus a DN-1/2/3"); Perguntas | ✔ |
| 12 | Nenhuma decisão aberta fechada | §6 abaixo | ✔ |
| 13 | Todo EC com campo de registro que prove a execução; recusas da trava com código e cenário | Cada EVIDENCE/POSTCOND usa campo do contrato lógico (`cycle_log_entry` com `fsm_row`/`rule_id`/`capability_check_ref`; `dispatch_request.budget`; `macro_invocation`) **ou** a fonte declarada `capability_audit_record` do runtime (contrato l.1077; requisito em "Requisitos a outras Specs"). Contagens `model_calls`/`external_emissions`/`foreign_publications`/`clock_reads` definidas como consultas a esse registro. A prova só é executável quando o runtime gravar o registro — até lá, INDETERMINADO e trava **não** declarada verificada (INV-MDC-01) | ✔ quanto à **especificação** do lastro; a **existência** do registro do runtime é requisito (BUILD/SPEC-040) — **NÃO VERIFICÁVEL** nesta fase |
| 14 | Pesquisa não refeita; fontes do Dossiê citadas por ID | "Classificação das fontes externas" | ✔ |

---

## 2. Código ↔ cenário (C05 — todo caminho fail-closed tem código na §D3.1 e cenário)

| Código (§D3.1) | Cenário com VERIFICAÇÃO | Estado |
|---|---|---|
| `MDC_REQUEST_INCOMPLETE`/`MDC_FIELD_MISSING`, `MDC_REQUEST_ORIGIN_NOT_ALLOWED`, `MDC_LIMITS_NOT_CONFIGURED`, `MDC_GRAPH_VERSION_UNREGISTERED`, `MDC_TIME_SERVICE_UNAVAILABLE` | T02 (a)–(f) | ✔ |
| `MDC_CYCLE_ALREADY_ACTIVE` | T03 (a) | ✔ |
| `MDC_GRAPH_CYCLIC`, `MDC_GRAPH_HIERARCHY_VIOLATION` | T04 | ✔ |
| `MDC_NO_OPPORTUNITY`, `MDC_OPPORTUNITY_UNDETERMINED` | T06 | ✔ |
| `MDC_DIRECTIONAL_CONFLICT_NEUTRAL` | T07 | ✔ |
| `MDC_MACRO_NOT_CONCLUSIVE` (3 subs) | T08 (a)(b)(c) | ✔ |
| `MDC_MACRO_INVOCATION_FAILED` (novo) | T22 (c) | ✔ |
| `MDC_ORIGIN_HYPOTHESIS_NOT_ELIGIBLE` (+ sub `MDC_CONTEXT_LOST`, novo) | T09 (a); T21 (a)–(c); ADV-15 | ✔ |
| `MDC_ALARM_FIELDS_INCOMPLETE` | T09 (b) | ✔ |
| `MDC_TRIGGER_OUTSIDE_WINDOW` | T10 (a) | ✔ |
| `MDC_NOT_PHASE1_TRANSITION` | T11 (b) | ✔ |
| `MDC_SETUP_MISALIGNED` (4 subs) | T12 (a)–(d) | ✔ |
| `MDC_ALARM_EXPIRED`, `MDC_ALARM_CANCELLED` | T13 (a)–(e) (F15, F31, F32) | ✔ |
| `MDC_STAGE_DEADLINE_EXCEEDED` | T14; T22 (d) | ✔ |
| `MDC_LIMIT_EXCEEDED` (3 subs) | T15 (a)–(c) | ✔ |
| `MDC_DISPATCH_PUBLISH_FAILED`, `MDC_AGENT_ERROR` (novos) | T22 (a)(b); T15 (c) | ✔ |
| `MDC_COST_BUDGET_EXCEEDED` | T16; ADV-09 | ✔ |
| `MDC_CYCLE_RECORD_UNAVAILABLE` | T17 (b) | ✔ |
| `MDC_DOMINANT_RUPTURE_DETECTED` | T18 | ✔ |
| `MDC_CYCLE_CLOSED` | T19; ADV-13; ADV-06 (b); T13 (c)(d); T21; ADV-15 | ✔ |
| `MDC_STOP_BY_ANDRAUS`, `MDC_STOP_COMMAND_NOT_AUTHENTICATED` | T20 | ✔ |
| `MDC_DUPLICATE_IGNORED` | ADV-01 | ✔ |
| `MDC_EVENT_FOREIGN_CYCLE` | ADV-03, ADV-05 (a)(c), ADV-07 (disparo e publicação) | ✔ |
| `MDC_EVENT_ENVELOPE_INVALID` | ADV-04 | ✔ |
| `MDC_TRANSITION_NOT_LISTED` | ADV-05 (b) (`ALARM_TRIGGERED` em `CONTEXTO_FORMADO` — passa o passo (2) da D4.2) | ✔ |
| `MDC_MACRO_ALREADY_INVOKED` | ADV-06 (a)(b) | ✔ |
| `MDC_ICT_HYPOTHESIS_REJECTED` | ADV-08 | ✔ |
| `MDC_EFFECT_FORBIDDEN` (10 subs) | ADV-10 (a)–(j) | ✔ |
| `MDC_MODEL_CALL_FORBIDDEN` | ADV-11 | ✔ |
| `MDC_CAPABILITY_CHECK_FAILED` (2 subs) | ADV-12 (a)–(c) (c = meio do ciclo, F37) | ✔ |
| `MDC_CLOCK_READ_FORBIDDEN` | ADV-14 | ✔ |
| Falso-DENY E3 (ENF-07) | ADV-10 (k); EC-MDC-008 FAILURE-MODE | ✔ — taxa INDETERMINADA (gap aberto) |

**Simulação da ordem da D4.2 para cada cenário negativo de evento (m-06):** ADV-03 → passo (2); ADV-04 → (0); ADV-01 → (1); ADV-05 (a)(c) → (2); ADV-05 (b) → (5); ADV-07 → (2) nas duas; T19, ADV-06 (b), ADV-13, T21/ADV-15 (cancelamento tardio) → (3); T11 (b) → (4); T10 (a) → (6) guarda de F14 (linha listada, sem transição); STOP de outra identidade (T20 (b)) → passa (2) só por `cycle_id`, F23. Nenhum cenário espera código de passo posterior ao que o pararia ✔.

---

## 3. Gate estrutural — conferência MANUAL linha a linha contra `scripts/validate_spec_sot.py` (não executado)

| Check | Regra do script | Evidência no `plan.md` v1.1 | Estado (manual) |
|---|---|---|---|
| STRUCT-01 | `complexidade [|:=] CRITICAL` e `profundidade-alvo [|:=] D\d` | tabela do cabeçalho + "Complexidade: CRITICAL. Profundidade-alvo: D0–D8" (l.20) | ✔ (manual) |
| STRUCT-02 | "Constitution Check"; "elliott"; "conviction … (pendente\|J-001\|…\|aberto)" | l.126; CC-01; CC-03 "Conviction Vector (J-001 ABERTA, pendente)" | ✔ (manual) |
| STRUCT-03 | ao menos uma etiqueta | `[FONTE]`, `[INFERÊNCIA]`, `[PROPOSTA]`, `[DECISÃO NECESSÁRIA]`, `[EXTERNO]` | ✔ (manual) |
| STRUCT-04 | EARS "quando …, … DEVE" | EARS 1–13 (l.643..655) | ✔ (manual) |
| STRUCT-05 | QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR | 12 BASpecs | ✔ (manual) |
| STRUCT-06 | efeito ⇒ 8 campos de EC | EC-MDC-001..009 com CAPABILITY…EVIDENCE (EC-009 novo, l.1602) | ✔ (manual) |
| STRUCT-07 | nenhum limiar "estrutural ≥60", "total ≥75", "conviction … 60/75%" | nenhum desses padrões; `thresholds_used` citado só como campo ignorado, sem número | ✔ (manual) |
| STRUCT-08 | marcador de status | "FATO NORMATIVO", "documentado ≠ homologado", `[DECISÃO NECESSÁRIA]` | ✔ (manual) |
| STRUCT-09 | profundidade ≤ teto | D0–D8 com CRITICAL | ✔ (manual) |
| STRUCT-10 | IDs `[A-Z]-\d{3}` abertos com marca de pendência ≤200 chars, sem fechamento colado | novas ocorrências da R2: J-001 em RULE-MDC-005 (d) (com `[DECISÃO NECESSÁRIA]` na mesma alínea) e em "Decisões abertas incidentes" (com "J-001 ABERTA" e `[DECISÃO NECESSÁRIA]`); nenhuma palavra "fechad/resolvid/homologad" colada a ID aberto | ✔ (manual) |
| STRUCT-11 | RULE-ECC-01/02 ⇒ `research.md` com "Dossiê de Pesquisa" | inalterado | ✔ (manual) |
| STRUCT-12 | régua RULE-ECC-06 | inalterado (5 capturas REPO) | **NÃO VERIFICADO por execução** |
| STRUCT-13 | BL-nnn + `Disposição:` | "Nota de gate" inalterada | ✔ (manual) |
| STRUCT-14 | todo `CLASSE : X` com MECANISMO e CRITÉRIO 4Es (C: + GATE DE SAÍDA), antes de VERIFICADO POR | 12 blocos; o C (l.940) tem GATE DE SAÍDA (l.944) | ✔ (manual) |

---

## 4. Matriz de rastreio (regra → EARS → BASpec → EC → cenários)

| Regra | EARS | BASpec | EC | D7 | D8 |
|---|---|---|---|---|---|
| RULE-MDC-001 | 1 | 001 | 001 | T01, T02, T03 | ADV-10 (i), ADV-12 |
| RULE-MDC-002 | 2 | 002 | 002 | T01, T04, T05 | — |
| RULE-MDC-003 | 3 | 003 | 002, 004 | T01, T14, T15 (b)(c), T22 (a)(b) | ADV-01..05 |
| RULE-MDC-004 | 4, 5 | 004 | 002, 007 | T06, T10, T18 | ADV-07 |
| RULE-MDC-005 | 6 | 005 | **009** (invocação), 003 (transição) | T07, T08, T22 (c)(d) | ADV-06 |
| RULE-MDC-006 | 7, 8 | 006 | 004, 003 | T09, T12, T13, T21 | ADV-08, ADV-15 |
| RULE-MDC-007 | 9 | 007 | 003 | T01, T19 | ADV-05, ADV-13 |
| RULE-MDC-008 | 10 | 008 | 002, 007 | T15, T16 | ADV-09 |
| RULE-MDC-009 | 11 | 009 | 003 (ENC por STOP), 007 | T06 (b), T08, T20 | ADV-10 (j) |
| RULE-MDC-010 | 11 | 010 | 005 | T14, T17 | ADV-02, ADV-14 |
| RULE-MDC-011 | 12 | 011 | 006 | T11 | ADV-10 (f)(g)(h) |
| INV-MDC-01 | 13 | 012 | 008 | T01 (contagens) | ADV-10, ADV-11, ADV-12, ADV-14 |

Nenhuma regra sem BASpec, EC e cenário; nenhum cenário órfão. Tasks TK-01..12 → BASpecs (TK-06 → EC-009).

---

## 5. Máquina de estados (C10)

- [x] Tabela estado × evento × guarda → próximo/ENC, com código e dono (D5, l.973–1020).
- [x] **Toda ação de efeito mapeia numa linha** (conferida linha a linha contra a coluna "Ação" e a Interface): despacho (F01, F03, F13), **republicação** (F33), **novo `attempt`** (F34), invocação macro (F06 — uma; nenhuma linha reinvoca), `ARM_ALARM` (F09), `MARK_CONSUMED` (F16, F17; F19, F20, F22, F35 em `ATIVADO`; F30 com alarme disparado), handoff (F16), aviso (F20, F21, F35), timer (F01, F03, F06, F09, F13). Evidência: tabela D5 + Interface (l.1030..) + EC-MDC-004 PRECOND — mesmo conjunto ✔.
- [x] **Todo FAILURE-MODE com "nova tentativa" tem evento + linha + timer:** falha de publicação → `DISPATCH_PUBLISH_FAILED`/F33 (timer da etapa mantido); erro do agente analítico → `PUB_ERROR`/F34 (timer mantido); voltas esgotadas → `PUB_ROUNDS_EXHAUSTED`/F35 (sem nova tentativa); erro do mecanismo macro → `MACRO_ERROR`/F36 (sem nova tentativa — RULE-MDC-005 (a)(e)); silêncio do mecanismo → timer pedido em F06 → F19. Conferido contra a regra de cardinalidade (RULE-MDC-005 (a): invocação = pedida) — sem contradição ✔.
- [x] **Cruzamento alarme (WF-A02) × estado do ciclo** (nota após D5, l.1018): `CONTEXTO_FORMADO` (ARMED F12/F30; EXPIRED/CANCELLED F31; TRIGGERED F29), `ARMADO` (TRIGGERED F13/F14/F30; EXPIRED/CANCELLED F15), `ATIVADO` (EXPIRED/CANCELLED F32), `AGUARDANDO` (D4.2 passo (2)), ENC (F28) ✔.
- [x] Elegibilidade reconferida no consumo de alarme/setup (F12, F13, F16, F17 guarda "elegível"; F30) ✔.
- [x] Nenhuma seta de volta (nota l.1020; ADV-13) ✔. Nenhum estado fora de WF-F02 ✔.
- [x] Dono por linha: F01–F23, F27–F37 = SPEC-008; F24–F25 = SPEC-014; F26 = RISK-SPEC ✔.
- [x] Ramos de WF-F01: 1 = F04; 2 = F08a; 3 = F17 (e F19 em `ATIVADO`); 4 = F26; 5 = F15, F31, F32 (EXPIRED); 6 = fora (P-13) ✔.
- [ ] Rótulo final dos ENC — **pendente de Andraus (DN-1, decidir depois com a SPEC-014)**; decisão aberta declarada, não falha.

---

## 6. CONS-01 — decisões abertas

| Decisão | Como aparece | Estado |
|---|---|---|
| J-001, N-001 | θ sem número; fórmula/pesos/limiares definitivos pendentes; `score` não usado (composição = J-001/BL-027) | ✔ ABERTAS |
| BL-029 (nota do CCM-001) | proveniência da entrada do gate — citada, não resolvida (RULE-MDC-005 (d)) | ✔ `[DECISÃO NECESSÁRIA]` do CCM-001 |
| G-001, M-001 | guarda do livro = SPEC-009; `domain_state` não definido | ✔ ABERTAS |
| SPEC-015-SCOPE, C-001, WF-D03 | origem/repetição na SPEC-015; só redação; só invocação | ✔ ABERTAS |
| K-001, SPEC-045-RUNTIME-001, ECC-03-001, D-PCC-4 | não tocadas | ✔ ABERTAS |
| P-11, P-13 | "decidir depois" | ✔ não fechadas |
| DN-1, DN-3 | `[DECISÃO NECESSÁRIA]` (Andraus 2026-11-08: DN-1 decidir depois com a SPEC-014; DN-3 não confirmada) | ✔ não fechadas |
| DN-2 | decidida por Andraus (2026-11-08): só detecta e avisa — comportamento inalterado | ✔ registrada (não é decisão do ROADMAP) |
| DNs novas na R2 | nenhuma | ✔ |
| F-1..F-4 (Andraus, 2026-11-14) | registradas como decisões; F-1 compatível com o roteiro v1 sem confirmar DN-3; F-4 diverge de WF-R01 → CF-D (só Andraus); J-001, WF-D03, BL-026, N-001, P-11 (fractal) seguem em aberto | ✔ nada fechado |

---

## 7. Herança (CC-08) — ponteiro

Tabela "Conservação do pai" cobre MMC-001 §1, §1-bis, §2.1–§2.6, §3, §3.1.1–§3.1.4, §3.2.1–§3.2.3, as nove linhas do §4, §5.1–§5.6, §6.1–§6.6, §7 e §10 — cada uma com evidência. REMOVED e MODIFIED vazios. INHERITS ganhou SPEC-048 v1.4 e SPEC-007 v2.3 (orçamento). §7-bis Bloco B no Plan. ✔

---

## 8. O que NÃO foi verificado (para o Orquestrador)

- Nenhum script executado (Especificador sem Bash): `validate_spec_sot.py`, `pre_entrega.py`, `check_repo_research.py`, `backlog_triggers.py --abertura SPEC-008`, `check_dimensionamento.py`, `check_refs.py`, `check_doc_sync.py`, `check_invariants.py`, `build_map.py --check`. Contagens e medida = Grep/leitura do Especificador.
- Linhas da SPEC-003 na errata = foto de 2026-11-08.
- Veracidade das fontes web do Dossiê: risco residual declarado na abertura.
- Existência futura do `capability_audit_record` no runtime (requisito; BUILD/SPEC-040).

---

## 9. Varredura de fronteira com Specs BASELINE (C04/M4 — lição R1-M04)

Grep de "SPEC-008:" e de "SPEC-008" nas seções de Requisitos/fronteira das Specs BASELINE (2026-11-14):

| Spec | Ocorrência | Tratamento no Plan v1.1 |
|---|---|---|
| SPEC-048 v1.4 | Requisitos: "**SPEC-008:** fornecer orçamento (rodadas, tempo) no pedido."; contrato `query_request … budget_ref (SPEC-008)`; tabelas "Orçamento de recursos/latência … SPEC-008 / SPEC-043"; RULE-RET-… (d)(f) `max_retrieval_rounds` e LATÊNCIA "orçamento da SPEC-008" | RULE-MDC-003 (a) (`budget`, `budget_ref`); RULE-MDC-008 (a); tabela de parâmetros + reconciliação; INHERITS; Requisitos ✔ |
| SPEC-007 v2.3 | `max_retrieval_rounds` "orçamento da SPEC-008"; "Orçamento de recursos da consulta — SPEC-008"; latência SPEC-008/043 | RULE-MDC-008 (a) `[INFERÊNCIA]`; Requisitos ✔ |
| SPEC-005 v1.0 | "fronteira SPEC-008" (RULE-BB-005); orquestração = SPEC-008; RULE-CEB-010 (latência de transporte) | RULE-MDC-003; reconciliação de latência ✔ |
| SPEC-004 v1.2 | orquestração (quem pensa, quando) = SPEC-008 | RULE-MDC-002/003/007 ✔ |
| SPEC-003 v1.5 | RULE-CF-010 (invocação macro = SPEC-008) | RULE-MDC-005; EC-MDC-009 ✔ |

Nenhuma outra linha "SPEC-008:" em seção de Requisitos de Spec BASELINE (Grep `\*\*SPEC-008[^*]*\*\*|SPEC-008:` em `specs/features/*/plan.md`: só SPEC-048 l.1158 e as fronteiras da SPEC-004/005).
