# checks.md — Verificação de Spec da SPEC-003 (fase spec-first)

**Objeto:** `specs/features/SPEC-003/plan.md` (Conviction Vector, Evidence Fusion Engine & Conviction Engine — redige o CCM-001)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §4]
**Método:** atomic-spec **v1.5**
**Data:** 2026-10-01

---

## 0-ter. Nota de delta v1.3 (propagação DHR-DEC-001 — Q-A5 fechada) [FONTE]

> Esta verificação cobre agora o `plan.md` **v1.3**. O delta v1.3 propaga a decisão direta de Andraus (DHR-DEC-001, chat, 2026-10-01): **Q-A5 FECHADA** — o número de invocações do mecanismo de Conviction Vector é **2x por ciclo** (macro Fase 1 / global Fase 2), declarado em `WORKFLOW.md` WF-C01 (versão vigente, v2.1). **Sem mudança de mérito** — BASpecs (CF-001..013), EARS (10), Enforcement (EC-CF-001..006), Classe/Mecanismo e D0–D8 **inalterados e NÃO renumerados**. Efeitos verificados:
> - **Q-A5 vira dado de entrada herdado de WF-C01:** a Spec **dá o mecanismo** (CF-010) de convicção sobre subconjunto/vetor-completo e **NÃO é dona nem implementa** a invocação — a invocação é do Manager Fase 1 (SPEC-008) / Fase 2 (SPEC-014). O Non-goal correspondente foi reformulado de "não decide 1x/2x" para "não implementa a invocação (2x já decidida)". ✔
> - **WF-D03 permanece ABERTA (residual):** o resíduo passa a ser J-001/N-001 (fórmula/pesos/limiares) e Q-A9 (dimensão do regime). O nº de invocações **sai** do resíduo (fechado). Nenhuma `WF-Dxx` aberta declarada fechada — a palavra ABERTA é preservada na WF-D03. ✔
> - **CONS-01:** nenhuma decisão aberta nova fechada pela Spec; J-001/N-001/M-001/Q-A9 intactas; RISK-CONV-001/RISK-ARR-LOC-001 (fechadas por Andraus) não são escopo desta Spec. ✔
> - **ADV-CF-12 reformulada** (negação coerente: a Spec não implementa a invocação, que é do Manager); §7-bis CF-010 ajustado (`invocation_implemented_here=false`). ✔
> **PASS (delta de propagação).**

---

## 0-bis. Nota de delta v1.2 (propagação DHR-ARQ-001 — unificação Manager/Conviction) [FONTE]

> Esta verificação cobre agora o `plan.md` **v1.2**. O delta v1.2 propaga a instrução direta de Andraus (DHR-ARQ-001, 2026-10-01) e o baseline ADR-MANAGER-001 / CEM-001 DIV-CEM-4: "Conviction Engine" deixa de ser **componente/agente separado** (acepção (a)) e passa a **mecanismo (Classe D/H do CCM-001) INVOCADO pelo Manager Agent — Fase 2 (Conviction)** (acepção (b)). **Sem mudança de mérito** — BASpecs (CF-001..013), EARS (10), Enforcement (EC-CF-001..006), Classe/Mecanismo e D0–D8 **inalterados e NÃO renumerados**; muda o *framing* do termo e as seções de cabeçalho/CC-10/acepção/Missão (D0). Efeitos verificados:
> - **CONFLITO-1 / CC-10 RESOLVIDO** (não é mais reconciliação pendente (a)↔(b)); a Spec adota a acepção (b) explicitamente. ✔
> - **B-001 parcialmente SUPERSEDIDA** na parte "componente separado" (INV-07 — não apagada); separação **lógica** de etapas preservada. ✔
> - **WF-D03 permanece ABERTA** (J-001/N-001/Q-A5/Q-A9); a taxonomia do componente **sai** de WF-D03 (passa a resolvida por DHR-ARQ-001). Nenhuma `WF-Dxx` aberta declarada fechada. ✔
> - **CONS-01:** nenhuma decisão aberta nova fechada; J-001/N-001/M-001 intactas. Unificação do Manager (SPEC-008×SPEC-015) remetida à proposta EUA-E23, **não** fechada aqui. ✔
> **PASS (delta de propagação).**

---

## 0. Nota de delta v1.1 (reconciliação ao `WORKFLOW.md`, versão vigente) [FONTE]

> Esta verificação cobre o `plan.md` **v1.1**. O delta v1.1 é de **conformidade/fronteira ao `WORKFLOW.md`** (versão vigente, DHR-WF-002), **sem mudança de mérito** de BASpecs/EARS/Enforcement/Classe — portanto as seções §1–§10 abaixo permanecem válidas (well-formedness inalterada). O que o delta v1.1 altera e esta nota confirma:
>
> - **Fronteira reclassificada (CONS-01):** `WF-D01` (Killzone), `WF-D02` (alarme-gatilho) e `WF-D04` (papel do ICT) estão **FECHADAS** por Andraus na versão vigente — a SPEC-003 continua **não** as especificando (Manager/Scheduler SPEC-008/015 + agentes SPEC-010..014); deixam de ser pontos abertos. **`WF-D03` permanece ABERTA (residual):** J-001, N-001, invocação 1x/2x (Q-A5) e **dimensão do regime (WF-C04 → Q-A9)**. Nenhuma `WF-Dxx` aberta é tratada como fechada. ✔
> - **Conformidade por ID (lente 3, mecanismo-apenas):** WF-C01→CF-010, WF-C02→CF-002, WF-C03→CF-007, WF-C04→Q-A9, WF-X03/INV-04→CF-008/CF-011, WF-A01→CF-013, WF-V02→CF-011/D9, WF-P02/N-001→CF-009. Todos os `WF-xx` citados **existem** na versão vigente; nenhum contraditado (verificação da lente 3 no plan.md §"Conformidade com o WORKFLOW.md"). ✔ (correspondência string-a-string de ID = mandato do Revisor / detector D6 do `check_doc_sync.py`.)
> - **Citação estável:** o plan.md cita a `WORKFLOW.md` por **"versão vigente"** e por ID `WF-xx`/`WF-Dxx` — nunca por número de versão nem por linha (regra de uso da `WORKFLOW.md`). ✔
> - **Q-A9 (NOVA) — em qual das 8 dimensões entra o regime (WF-C04):** registrada como **[DECISÃO NECESSÁRIA]** (plan.md §D2 Nota WF-C04 + lista final; research.md §8.3, com 4 opções + recomendação Opção A=temporal). **Não decidida** aqui; regime não mapeado a nenhuma dimensão (INDETERMINADO — CONS-01). ✔
> - **BASpecs NÃO renumeradas** (CF-001..013 mantidas); EARS (10), Enforcement (EC-CF-001..006), Classe/Mecanismo e D0–D8/adversariais inalterados. ✔
>
> Histórico v1.1 presente no plan.md (tabela "Histórico de versões", linha 1.1). **PASS (delta de conformidade).**

---

## 1. Cobertura de profundidade (D0–D8 — alvo ROADMAP §4/§143; research.md Q-A2; CRITICAL)

| Nível | Exigido (CRITICAL, alvo D0–D8) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (fusão→convicção 8D; CCM-001; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S8 + Non-goals (J-001/N-001/Synthesis/Risk/M-001/WORKFLOW) |
| D2 Regra | Sim | ✔ | RULE-CF-001..012 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | CF-001..013, cada uma com bloco CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística numérica | Parcial/N/A | Normalização (CF-004), veto (CF-006), gate (CF-012) determinísticos; fórmula/pesos definitivos N/A (J-001/N-001) — justificado |
| D5 Estado | Sim | ✔ | Ciclo do objeto convicção (COMPUTED/GATED_*/SUPERSEDED) + CEM-001 Cap.4 (evidência, não redefinido) |
| D6 Protocolo | Sim | ✔ | Pipeline B-001 (Fusion→Conviction→[Synthesis]); 11 passos; M-001/WORKFLOW referenciados como abertos |
| D7 Teste | Sim (CRITICAL) | ✔ | Cenários CF-T01..T08 |
| D8 Adversarial | Sim (CRITICAL) | ✔ | ADV-CF-01..12 (12 cenários) |
| D9 Auditoria | Sistema completo | Parcial (por referência) | Reconstrução/Cognitive Trace → SPEC-006/H-001; P13/RULE-010 |

**Resultado:** profundidade-alvo D0–D8 atingida. D4 numérico definitivo N/A justificado (J-001/N-001 abertos; a Spec fixa método/mecanismo + limiares-piloto interinos).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO obs. | ENTÃO mens. | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| CF-001 fusão DERIVED | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CF-002 anti-double-counting | ✔ | ✔ | ✔ | ✔ | ✔ | P | bounded loop ✔ (parada "undetermined") |
| CF-003 impacto invalidação | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CF-004 normalização | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CF-005 agregação não-compensatória | ✔ | ✔ | ✔ | ✔ | ✔ | H | bounded loop ✔ + gate de saída ✔ |
| CF-006 veto estrutural/conflito | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CF-007 ausência/incerteza | ✔ | ✔ | ✔ | ✔ | ✔ | P | bounded loop ✔ (parada INDETERMINADO) |
| CF-008 robustez/sensibilidade | ✔ | ✔ | ✔ | ✔ | ✔ | P | bounded loop ✔ (conjunto finito de perturbações) |
| CF-009 aging/pesos | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CF-010 macro/global | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| CF-011 Separação Tríplice/INV-04 | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CF-012 gate Convicção→Decisão (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CF-013 publicação (M-001 aberta) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário; cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); H/P com bounded loop; H/C com gate de saída (RULE-MECH-03). **PASS.**

---

## 3. Critérios EARS

10 critérios no formato "Quando <condição>, o <componente> DEVE/NÃO DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-CF-001..006 (mapeiam as 13 BASpecs) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E2 piso Evidência/Engine; E3 no gate Convicção→Decisão |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ EC-CF-003/005; RULE-CF-009; ADV-CF-08 |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-CF-005 (gate Convicção→Decisão) + todos os EC |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-CF/CCM-001 [PROPOSTA]; só Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-CF-005 (amostral; limiar = gap aberto) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. CC-01 (não-compensatória/veto estrutural), CC-02 (CEM/CHM não redefinidos; CCM-001 é o produto), CC-08 (Herança/Delta), CC-10 (acepção "Conviction Engine" declarada), CC-11 (Classe por BASpec) = críticos aplicáveis, PASS. CC-03 = dimensionalidade=8 fechada; limiares-piloto interinos; definitivos J-001/N-001 pendentes. CC-04 = Salvaguardas §11 preservadas (gate CF-012); INV-04 reforçado. CC-05 = CRITICAL/D0–D8. CC-09 = epistêmico (INDETERMINADO; sem falsa precisão). CC-06/CC-07 = N/A justificado (não é Engineering Card). **CC-12 = N/A homologado** (infraestrutura transversal; research.md §6-bis Q-A3). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED com ID+versão (RULE-HD-04): CEM-001 (Cap.2/3/4/5/6), CHM-001 (§1.9/§2.14), SPEC-001 v1.1, SPEC-002, SPEC-019/020/021 v1.0, atomic-spec v1.5, GPR-001 (PC-04/PCO-06/PB-06). ✔
- REMOVED vazio. ✔
- MODIFIED declarado (RULE-004 estendida em cobertura — mecânica de fusão —, sem alterar texto; RULE-HD-02 respeitada). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (herança sobre canônicos vizinhos, não decomposição pai→filha de macro-spec). ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| J-001 NÃO fechada; nenhum valor/pesos/limiar definitivo de convicção fixado (RULE-CF-003/004/009; ADV-CF-09) | ✔ |
| N-001 NÃO fechada; só o mecanismo de pesos por ativo (CF-009) | ✔ |
| M-001 NÃO fechada; estados do Blackboard para o Conviction Vector não fixados (CF-013; ADV-CF-12) | ✔ |
| WORKFLOW-SOT-001 NÃO fechada; invocação 1x/2x e reconciliação da acepção não fixadas (CF-010; ADV-CF-12) | ✔ |
| B-001 e dimensionalidade=8 citadas como FECHADAS (ROADMAP) — não reabertas | ✔ |
| Limiares-piloto ≥70%/7-9 etiquetados FATO NORMATIVO interino (Q-002), não definitivos | ✔ |
| RULE-CF/CCM-001 etiquetadas [PROPOSTA]; CEM/CHM/INV-*/ENF-*/RULE-* existentes como FATO NORMATIVO | ✔ |
| Fontes SRC-01..07 etiquetadas [EXTERNO]; nada vira baseline (DS/Bayes/TOPSIS/Kelly não importados) | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.** Nota: os limiares usados (70% / 7-9) NÃO coincidem com os padrões proibidos do gate determinístico (60% estrutural / 75% total); PC-04 (60%/75%) não é transcrito como fechado — tratado como superado pelos limiares-piloto interinos e pelos definitivos J-001.

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| CEM-001 (Cap.2/3/4/5/6) | ✔ | canon/CEM-001 (BASELINE) |
| CHM-001 (§1.9/§2.14) | ✔ | canon/CHM-001 (BASELINE) |
| SPEC-001 v1.1; SPEC-002 | ✔ | specs/features/SPEC-001; SPEC-002 (BASELINE) |
| SPEC-019/020/021 v1.0; RULE-HG-*/RULE-EV-*/RULE-MM-* | ✔ | RULES.md (baseline FASE GOV) |
| INV-01/03/04/05/06/07/09/10 | ✔ | atomic-spec §13 |
| ENF-01..08 (esp. ENF-03/04/07) | ✔ | atomic-spec §10.4 |
| RULE-002/003/004/005/008/010; RULE-SY-001/002/003; RULE-CEE-004; RULE-GMC-001..005; RULE-BB-002/004 | ✔ | RULES.md |
| RULE-EPI-01/CAU-01/MET-01/02/UNC-01/03/PRB-01/02/DEC-01/SEM-01/03/04/INQ-03 | ✔ | RULES.md v1.5 |
| RULE-MECH-01..04 (CC-11); RULE-PD-01 (CC-12); RULE-ECC-01/02/04/05 | ✔ | RULES.md |
| GPR-001 PC-04/PCO-06/PB-06/PB-08/PE-08 | ✔ | governance/GPR-001 |
| EC-COG-005 (Cognitive Event Bus) | ✔ | CEM-001 Cap.6; contrato → SPEC-005 |
| SRC-01..07 (fontes externas) | ✔ (verbatim) | specs/features/SPEC-003/sources/SRC-0N.txt (RULE-ECC-04) |
| CCM-001; RULE-CF-001..012; BASpec-CF-001..013; EC-CF-001..006 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **BL-004** (Fórmula/pesos/limiares; `spec:SPEC-003 em redação`) DISPAROU na abertura → **ATIVADO/Absorvido/tratado** (fechamento definitivo de J-001/N-001 na homologação do Plan; valores definitivos pós-backtest). ✔
- **BL-012** (MC-COG-001) **ATIVADO independente** — tratado por Andraus separadamente; não bloqueia/absorvido. ✔
- **BL-002** (Falso-DENY, ENF-07) NÃO dispara na redação; **IMINENTE** na homologação. ✔
- **BL-003/BL-017** NÃO disparam (SPEC-003 não é gatilho). ✔
- Nenhum item ATIVADO pendente sem encaminhamento. **PASS.**

---

## 10. RULE-ECC-04 (Captura Verbatim) e RULE-ECC-05 (Multi-Lente) — verificação de presença

| Fonte carregada | Arquivo companheiro presente | Citação verbatim no Dossiê |
|---|---|---|
| SRC-01 Bayes vs Dempster-Shafer | ✔ sources/SRC-01-bayes-vs-dempster-shafer.txt | ✔ research.md §2.1 |
| SRC-02 Evidence aggregation comparison | ✔ sources/SRC-02-evidence-aggregation-comparison.txt | ✔ |
| SRC-03 Kelly criterion | ✔ sources/SRC-03-kelly-criterion.txt | ✔ |
| SRC-04 Conviction×confidence / fractional Kelly | ✔ sources/SRC-04-conviction-vs-confidence-fractional-kelly.txt | ✔ |
| SRC-05 Confluence signal weighting | ✔ sources/SRC-05-confluence-signal-weighting.txt | ✔ |
| SRC-06 TOPSIS/MCDA | ✔ sources/SRC-06-topsis-mcda-aggregation.txt | ✔ |
| SRC-07 MCDA sensitivity/robustness | ✔ sources/SRC-07-mcda-sensitivity-robustness.txt | ✔ |

- **RULE-ECC-05 (3 lentes):** presentes no Dossiê (research.md) e refletidas no Plan — (1) Arquitetura (§3.1 → CF-004/005/CCM-001); (2) Escola/risco-retorno (§3.2 → Kelly/sizing ADIADO ao Risk Agent, CF-008 non-goal); (3) confronto WORKFLOW.md (§3.3 → macro/global CF-010; motor 1x/2x e acepção abertos). ✔
- As decisões adotar/adaptar/rejeitar/adiar do Dossiê estão materializadas: REJEITAR compensatória pura/votos simétricos (CF-005/ADV-CF-03); ADIAR Kelly/sizing (CF-008/non-goal); ADAPTAR normalização/sensibilidade (CF-004/CF-008); fusão DS/Bayes só referência de método (não baseline). ✔

> A **correspondência verbatim** string-a-string é mandato do Revisor (sem web — ENF-03). Aqui só se verifica **presença** dos 7 arquivos e das citações, e **presença das 3 lentes**. **PASS (presença).**

---

## 11. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (herança sobre canônicos, não macro→micro) | Menor | Revisor confirma o eixo de herança |
| CK-02 | D9 auditoria/Cognitive Trace Reconstruction apenas por referência (H-001/SPEC-006) | Menor | Consistente com alvo D0–D8; delegado ao KG (CEM-001 Cap.5) |
| CK-03 | Acepção "Conviction Engine" (a) declarada (RULE-SEM-01); reconciliação (a)↔(b) deixada a WORKFLOW-SOT-001 | Menor | Revisor confirma CC-10; decisão de reconciliação é de Andraus |
| CK-04 | D4 numérico definitivo N/A (J-001/N-001); a Spec fixa só método/mecanismo + limiares-piloto | Info | Coerente com INV-03/CONS-01/RULE-MM-06/RULE-EV-05 |
| CK-05 | BL-012 (MC-COG-001) ATIVADO independente — não absorvido pela SPEC-003 | Info | Tratado por Andraus separadamente |
| CK-06 | Correspondência verbatim RULE-ECC-04 (string) fica para o Revisor (sem web) | Info | Mandato do Revisor |
| CK-07 | **Q-A9 (NOVA, delta v1.1)** — dimensão das 8 em que entra o regime (WF-C04) | Menor | **[DECISÃO NECESSÁRIA]** de Andraus; 4 opções + recomendação (Opção A=temporal) em research.md §8.3; não decidida (INDETERMINADO — CONS-01) | — Andraus (2026-10-01): decisão da dimensão fica com a SPEC-003, fonte de dados = `research-Q-A9-regime.md`.
| CK-08 | WF-D01/D02/D04 FECHADAS na versão vigente da `WORKFLOW.md`; SPEC-003 não as especifica (fora de escopo) | Info | Reclassificação de fronteira (delta v1.1); sem mudança de mérito |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (CF-001..013) com Classe/Mecanismo (CC-11), EARS (10), Enforcement (EC-CF-001..006; ENF-03 detector≠gate; E3 no gate Convicção→Decisão), Constitution Check CC-01..CC-12, Herança/Delta (CC-08), CONS-01 (J-001/N-001/M-001/WORKFLOW-SOT-001 abertas; dimensionalidade=8/B-001 não reabertas), gate RMR-001, RULE-ECC-04 (presença) e RULE-ECC-05 (3 lentes refletidas) satisfeitos. 6 achados não-bloqueantes (CK-01..CK-06) encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `validate_spec_sot.py` + submissão ao Revisor SOT.
