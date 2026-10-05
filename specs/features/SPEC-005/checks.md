# checks.md — Verificação de Spec da SPEC-005 (fase spec-first)

**Objeto:** `specs/features/SPEC-005/plan.md` **v1.0 (candidato)** (Cognitive Event Bus — camada fina de notificação de mudança sobre o log append-only da SPEC-004 + canal de saída da notificação do Signal Package)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §5]
**Método:** atomic-spec **v1.5**
**Data:** 2026-10-04

---

## 1. Cobertura de profundidade (D0–D7 — alvo ROADMAP §5; HIGH, sem D8 pinado)

| Nível | Exigido (HIGH, alvo D0–D7) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (notificação de mudança; envelope/propagação/entrega/subscrição/saída externa/observabilidade; transporte≠fonte de verdade; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S12 + Non-goals (SPEC-004/broker-Opção C/KG/estado-agente/Signal Package/mecanismo físico/latência) |
| D2 Regra | Sim | ✔ | RULE-CEB-001..012 [PROPOSTA]; INV-CEB-01 |
| D3 Comportamento (BASpec) | Sim | ✔ | CEB-001..012, cada uma com bloco CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | Cursor/catch-up, dedupe de consumo, correlation/causation, ordering observado, retry bounded+dead-letter, orçamento de latência (parâmetro) |
| D5 Estado | Sim | ✔ | `delivery_state` (EMITTED/DELIVERING/RETRYING/ACKED/DEAD_LETTERED/REJECTED) — ciclo do EVENTO, separado de publication_state/domain_state (SPEC-004) e de CHM-001 |
| D6 Protocolo | Sim | ✔ | Sequência de notificação (10 passos) sobre o log; fronteiras Manager (controle) / SPEC-004 (estado) |
| D7 Teste | Sim (HIGH; ≥3 cenários) | ✔ | Cenários CEB-T01..T10 (10 — inclui WF-A03/T02, fail-safe/T07, saída externa E3/T09, EVENT-BUS-001/T10) |
| D8 Adversarial | Rigor adversarial focado (sem profile elevado) | ✔ | ADV-CEB-01..08 (envelope, perda≠estado, duplicata, retry infinito, descarte silencioso, armazém de estado, saída externa, absorver vizinhos/fechar decisão) |
| D9 Auditoria | Por referência | Parcial (por referência) | Trilha de notificação/entrega reconstruível; reconstrução de ESTADO = SPEC-004 (replay); observabilidade agregada = SPEC-040/KG |

**Resultado:** profundidade-alvo D0–D7 atingida; rigor adversarial focado (D8) **sem elevar o profile** (HIGH standard; DHR-SPEC005-001 §2). D9 por referência (coerente com alvo e com H-001 ABERTA / SPEC-040).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO obs. | ENTÃO mens. | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| CEB-001 envelope de evento | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-002 correlation/causation | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-003 cursor de consumo | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-004 idempotência de consumo | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-005 ordem observada | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-006 at-least-once/retry/dead-letter | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ + bounded loop ✔ |
| CEB-007 transporte≠fonte de verdade | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CEB-008 entrega a consumidor autorizado | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CEB-009 saída externa Signal Package (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CEB-010 metadados/latência (parâmetro) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-011 observabilidade | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CEB-012 distinção Blackboard↔Event Bus | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário; cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); Classes C declaram gate de saída (RULE-MECH-03); CEB-006 (C) declara **bounded loop** (retry limitado, sem retry infinito). Nenhuma H/P normativa (gates determinísticos C/D; eventual Classe H "evento bem-formado" = orientação de BUILD/detector, não BASpec normativa). **PASS.**

---

## 3. Critérios EARS

12 critérios no formato "Quando <condição>, o Event Bus DEVE/NÃO DEVE <resposta>" (envelope, causalidade, cursor, dedupe de consumo, ordem observada, at-least-once/retry/dead-letter, fail-safe, entrega autorizada, saída externa E3, latência-parâmetro, observabilidade, distinção). Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-CEB-001..005 (mapeiam as 12 BASpecs: 001=entrega/envelope; 002=retry/dead-letter; 003=fail-safe; 004=entrega autorizada; 005=saída externa E3) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E1 (notificação observável); E2 (entrega/dead-letter/fail-safe/autorização); **E3 na saída externa do Signal Package** (irreversível) |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ EC-CEB-004; RULE-CEB-008; roteamento de modelo (LLM só detector) |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-CEB-005 (saída externa E3 fail-closed) + EC-CEB-002 (dead-letter, não descarte) + todos os EC |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-CEB/contrato [PROPOSTA]; só Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-CEB-005 (amostral; **enforcement E3 CONDICIONAL até o limiar** — gap aberto, atomic-spec §12) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. **Críticos aplicáveis:** CC-02 (CHM/CEM/CCM/SPEC-004 não redefinidos — só propaga/notifica), CC-08 (Herança/Delta + cobertura×lacuna SPEC-004), CC-10 (acepções "evento" vs "objeto"; "entrega" vs "publicação"; idempotência de consumo vs escrita), CC-11 (Classe por BASpec) = PASS. CC-01 (agnóstico de escola; hierarquia intocada). CC-03 (não computa convicção; dimensionalidade=8; J-001/N-001 abertas). CC-04 (nenhuma Salvaguarda violada; INV-04 preservado). CC-05 (HIGH/D0–D7). CC-09 (EVENT-BUS-001 ABERTA; INDETERMINADO sobre mecanismo físico; latência=parâmetro; sem falsa precisão). CC-06/CC-07 = N/A justificado (não é Engineering Card). **CC-12 = N/A** (infraestrutura agnóstica de escola; DHR-SPEC005-001 §2). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED com ID+versão/linha (RULE-HD-04): **SPEC-004 v1.2** (RULE-CBP-001/003/005/006/011/013/014), RULE-BB-001/004/005, CHM-001, CEM-001 (l.717-727), CCM-001, SPEC-001 v1.1 (EARS 8 l.159; l.75), SAS-001 §6.9/§6.10, CONSTITUTION l.235, GPR-001 l.457, atomic-spec v1.5, SPEC-019/020/021 v1.0, INV-05/06/07/09/10, ENF-01..08. ✔
- **Mapa de cobertura × lacuna da SPEC-004 v1.2 presente** (arquivo:linha): ordem de commit/seq, idempotência de escrita, replay, identidade autenticada, supersessão, schema_version, atomicidade = **herdados, não duplicados**; lacuna real = contrato de evento/propagação/entrega/subscrição/saída externa/latência. ✔
- REMOVED vazio. ✔
- MODIFIED vazio (RULE-BB-001/004/005 operacionalizadas no eixo de transporte, não alteradas; SPEC-004 não tocada — INV-09; RULE-HD-02 respeitada). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (herança sobre a SPEC-004/regras/canônicos vizinhos, não decomposição pai→filha de macro-spec). ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| EVENT-BUS-001 NÃO fechada — CEB-012 só PROPÕE a distinção; decisão de Andraus (ADV-CEB-08) | ✔ |
| Mecanismo físico (push/poll/LISTEN-NOTIFY) = INDETERMINADO (não presumir) | ✔ |
| Broker Opção C = ADIADO (registrado, não apagado; INV-07) | ✔ |
| Orçamento de latência = PARÂMETRO a calibrar (INDETERMINADO; sem número arbitrário — RULE-MET-01) | ✔ |
| M-001 NÃO tocada (fronteira SPEC-004) — permanece ABERTA | ✔ |
| J-001 / N-001 NÃO tocadas; o Event Bus não computa convicção | ✔ |
| H-001 / G-001 NÃO tocadas; KG/estado-agente por fronteira | ✔ |
| WF-D03 NÃO tocada (não computa convicção) | ✔ |
| SPEC-004 NÃO reaberta/duplicada (CC-02/INV-09; cobertura×lacuna) | ✔ |
| Doc 13 = histórico não-normativo (RULE-BB-001 prevalece; TRACE-06) — não fecha conflito pela Spec | ✔ |
| RULE-CEB/contrato etiquetadas [PROPOSTA]; SPEC-004/RULE-BB-*/CHM/CEM/CCM/INV-*/ENF-* existentes como FATO NORMATIVO | ✔ |
| Fontes SRC-*/REPO-* etiquetadas [EXTERNO]; nada vira baseline (outbox/CDC/broker/LangGraph não importados) | ✔ |
| Menor A4 (research.md §6.4) corrigido — nome mantido; condicional obsoleta removida | ✔ |
| Nenhuma decisão aberta usada como invariante fechado (STRUCT-10: EVENT-BUS-001 não casa `[A-Z]-\d{3}`; M/J/N/H/G-001 marcadas ABERTAS em contexto) | ✔ |

**PASS.** Nota: nenhum limiar numérico de convicção (60%/75%) nem de latência é declarado — STRUCT-07 não incide (o Event Bus não computa convicção; latência é parâmetro, não invariante fechado).

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| SPEC-004 v1.2 (RULE-CBP-001/003/005/006/011/013/014; INV-CBP-01) | ✔ | specs/features/SPEC-004/plan.md (BASELINE, DHR-SPEC004-003) |
| RULE-BB-001/004/005 | ✔ | governance/RULES.md l.308–329 |
| CHM-001; CEM-001 (l.717-727); CCM-001 | ✔ | canon/ (BASELINE) |
| SPEC-001 v1.1 (EARS 8 l.159/l.367; l.75); SPEC-019/020/021 v1.0 | ✔ | specs/features/ (BASELINE) |
| SAS-001 §6.9 (Integração Event Bus) / §6.10 (Metadados de transporte) | ✔ | canon/SAS-001-structural-agent-spec.md l.914/l.917-918 |
| CONSTITUTION l.235 (EC-COG-005); GPR-001 l.457 | ✔ | governance/ |
| INV-05/06/07/09/10 | ✔ | atomic-spec §13 |
| ENF-01..08 (esp. ENF-03/04/07) | ✔ | atomic-spec §10.4 |
| RULE-MECH-01..04 (CC-11); RULE-PD-01 (CC-12); RULE-ECC-01/02/04/06 | ✔ | RULES.md |
| RULE-HD-02/03/04 (CC-08); RULE-HV-01..04 | ✔ | RULES.md (SPEC-019 baseline) |
| RULE-EPI-01/MET-01/UNC-01..03/SEM-01/04/DEC-01 | ✔ | RULES.md v1.5 |
| EVENT-BUS-001 (dona=SPEC-005); M-001; H-001; G-001; J-001; N-001; WF-D03; ECC-03-001 | ✔ (abertas) | ROADMAP §7 / AGENTS §7 / WORKFLOW.md |
| WF-A03 (morte do alarme); WF-F02 (FSM); WF-F01 (reset) | ✔ | WORKFLOW.md l.55/l.71/l.70 |
| REPO-debezium/langgraph (elegíveis); REPO-postgresql-event-sourcing (NÃO ELEGÍVEL) | ✔ (verbatim) | specs/features/SPEC-005/sources/ (RULE-ECC-04/06) |
| RULE-CEB-001..012; INV-CEB-01; contrato de evento; BASpec-CEB-001..012; EC-CEB-001..005 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **Nenhum item com gatilho `spec:SPEC-005`** — a abertura/Plan **não dispara item novo** (`backlog_triggers.py` a rodar). ✔
- **BL-008** (auditoria retroativa SPEC-001) e **BL-003** (persistência física) ATIVADO/pré-existentes, **independentes** — não absorvidos nem promovidos por esta Spec. ✔
- **BL-017** (dimensões B SPEC-020) `Em espera`, independente — não promovido. ✔
- Nenhum item ATIVADO pendente sem encaminhamento por esta redação. **PASS** (passo 11-bis pleno na homologação do Plan).

---

## 10. RULE-ECC-04 (Captura Verbatim) e RULE-ECC-06 (Repositórios) — verificação de presença

| Fonte carregada | Arquivo companheiro presente | Citação verbatim no Dossiê |
|---|---|---|
| SRC-OUTBOX-01 (outbox) | ✔ sources/SRC-OUTBOX-01.txt | ✔ research.md §3.2 |
| SRC-ES-01 (event sourcing/cursor) | ✔ sources/SRC-ES-01.txt | ✔ research.md §3.3 |
| SRC-NOTIFY-01 (LISTEN/NOTIFY best-effort) | ✔ sources/SRC-NOTIFY-01.txt | ✔ research.md §3.4 |
| SRC-BROKER-01 (broker over-engineering) | ✔ sources/SRC-BROKER-01.txt | ✔ research.md §3.6 |
| SRC-BB-01 (blackboard↔controle/notificação) | ✔ sources/SRC-BB-01.txt | ✔ research.md §3.1 |
| SRC-LLM-01 (orquestração sem broker) | ✔ sources/SRC-LLM-01.txt | ✔ research.md §3.5 |
| REPO-debezium / REPO-langgraph / REPO-postgresql-event-sourcing | ✔ sources/REPO-*.txt | ✔ research.md §5 (régua Equilibrada) |

- **RULE-ECC-06 (repositórios seguros):** seção "Pesquisa em repositórios" presente (research.md §5); **2 ELEGÍVEIS** (debezium, langgraph) sob régua Equilibrada + **1 NÃO ELEGÍVEL** (postgresql-event-sourcing, arquivado) registrado, não adotado; capturas REPO-*.txt presentes; conteúdo = DADO (nada instalado/executado). SPEC-005 **não** é grandfathered → STRUCT-12 incide. `python scripts/check_repo_research.py specs/features/SPEC-005` esperado OK (sem web — ENF-03). ✔
- **RULE-ECC-05 (Multi-Lente):** **NÃO incide** (DHR-SPEC005-001 §2 — infra, não toca comportamento de trading); conformidade com WORKFLOW.md confirmada por prudência (WF-A03/WF-F02; não fecha WF-D03). ✔
- **Nota de honestidade (DHR-SPEC005-001 §4):** os valores de estrelas/licença/último-commit dos repositórios foram, em parte, preenchidos pela API pública do GitHub (orquestrador, 2026-10-04) — não reproduzíveis pelo Revisor sem rede (ENF-03). Vereditos ELEGÍVEL/NÃO ELEGÍVEL são o que o gate confere; risco residual registrado em `sources/_LIMITACAO-WEB.txt`.

> A **correspondência verbatim** string-a-string e a régua de repositório são mandato do Revisor / gate determinístico (sem web — ENF-03). Aqui só se verifica **presença**. **PASS (presença).**

---

## 11. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (herança sobre SPEC-004/regras/canônicos, não macro→micro) | Menor | Revisor confirma o eixo de herança |
| CK-02 | D9 auditoria/reconstrução de ESTADO por referência (SPEC-004 replay; observabilidade agregada = SPEC-040/KG) | Menor | Consistente com alvo D0–D7 |
| CK-03 | **EVENT-BUS-001 apresentada como [PROPOSTA]** (CEB-012: Blackboard guarda estado / Event Bus transporta), **não** fechada — decisão de Andraus na homologação | Info | Andraus decide (CONS-01) |
| CK-04 | **Mecanismo físico de transporte = INDETERMINADO**; Opção C (broker) ADIADA com condição de reavaliação registrada | Info | Coerente com RULE-MET-01/EPI; BUILD |
| CK-05 | **Orçamento de latência = PARÂMETRO a calibrar** (INDETERMINADO; sem número); SPEC-005 dona dos metadados (SAS-001 §6.10; SPEC-001 l.75) | Info | Calibração pós-medição (SPEC-040); não toca J-001/N-001 |
| CK-06 | **Menor A4 corrigido** — research.md §6.4: condicional obsoleta sobre rename removida (nome "Cognitive Event Bus" mantido por Andraus) | Resolvido | Revisor confirma o alinhamento do texto não-normativo |
| CK-07 | Baselines que citam o Event Bus tratadas **sem erratum** (número preservado): SPEC-001 EARS 8/l.75, CEM-001 l.725, CONSTITUTION l.235, GPR-001 l.457, SAS-001 §6.9/§6.10 | Info | Revisor confirma inexistência de erratum necessário (INV-09) |
| CK-08 | Saída externa do Signal Package = **E3 fail-closed** (EC-CEB-005); falso-DENY E3 CONDICIONAL até o limiar (gap aberto) | Info | Revisor audita ENF-04/07; limiar não fixado (atomic-spec §12) |
| CK-09 | SAS-001: o Dossiê/abertura citam "§6.7" para metadados de transporte; a lista Freshness/Latency/Reliability/Expiration está de fato em **SAS-001 §6.10** (e a Integração Event Bus em §6.9). O Plan cita §6.9/§6.10 (anchors reais); SPEC-001 l.75 (que diz "§6.7") é citação herdada da baseline, não reescrita (INV-09) | Menor | Revisor confirma os anchors; sem reescrita de baseline |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (CEB-001..012) com Classe/Mecanismo (CC-11; D determinístico + C constitutivo; CEB-006 com bounded loop), EARS (12), Enforcement (EC-CEB-001..005; ENF-03 detector≠gate; **E3 fail-closed na saída externa do Signal Package**; E3 falso-DENY CONDICIONAL até limiar), Constitution Check CC-01..CC-12 (CC-02/CC-08/CC-10/CC-11 incidem e aplicados; CC-12 N/A), Herança/Delta (CC-08 + cobertura×lacuna SPEC-004), CONS-01 (EVENT-BUS-001/M-001/J-001/N-001/H-001/G-001/WF-D03/ECC-03-001 abertas; mecanismo físico INDETERMINADO; Opção C adiada; latência parâmetro), gate RMR-001 (nenhum gatilho spec:SPEC-005), RULE-ECC-04 (presença verbatim) e RULE-ECC-06 (repositórios, régua Equilibrada — 2 elegíveis + 1 não elegível) satisfeitos. **Menor A4 corrigido** (CK-06). Achados não-bloqueantes CK-01..CK-09 encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + `check_doc_sync.py` + submissão ao Revisor SOT.
