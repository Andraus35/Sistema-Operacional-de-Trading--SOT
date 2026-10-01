# checks.md — Verificação de Spec da SPEC-002 (fase spec-first)

**Objeto:** `specs/features/SPEC-002/plan.md` (Evidence & Evidence Provenance Harness — camada Harness/operacional sobre CEM-001)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §4]
**Método:** atomic-spec **v1.5**
**Data:** 2026-09-28

---

## 1. Cobertura de profundidade (D0–D8 — alvo ROADMAP §4/research.md Q-A2; CRITICAL)

| Nível | Exigido (CRITICAL, alvo D0–D8) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (camada operacional sobre CEM-001; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S12 + Non-goals (fusão/storage/M-001/RAG/resolução) |
| D2 Regra | Sim | ✔ | RULE-EH-001..008 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | EH-001..010, cada uma com bloco CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística numérica | Parcial/N/A | EH-001 (ID/versão) e EH-009 (idade relativa) determinísticos; escore de qualidade/desconto N/A (J-001) — justificado |
| D5 Estado | Sim | ✔ | Ciclo de vida CEM-001 Cap.4 (ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED) — referenciado, não redefinido |
| D6 Protocolo | Sim | ✔ | Protocolo de publicação (8 passos; gates; M-001 referenciada como aberta) |
| D7 Teste | Sim (CRITICAL) | ✔ | Cenários EH-T01..T07 |
| D8 Adversarial | Sim (CRITICAL) | ✔ | ADV-EH-01..10 (10 cenários) |
| D9 Auditoria | Sistema completo | Parcial (por referência) | Reconstrução/Cognitive Trace → SPEC-006/H-001; P13 |

**Resultado:** profundidade-alvo D0–D8 atingida. D4 numérico de qualidade/desconto N/A justificado (J-001 aberto; mecânica de fusão → SPEC-003).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO obs. | ENTÃO mens. | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| EH-001 alocação ID/versão | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| EH-002 gate contrato CEM | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| EH-003 INV-06 (Skill≠Evid.) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| EH-004 provenance | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| EH-005 guard INV-04 | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| EH-006 (in)dependência | ✔ | ✔ | ✔ | ✔ | ✔ | P | bounded loop ✔ (parada em "undetermined") |
| EH-007 tipologia/AUSENTE | ✔ | ✔ | ✔ | ✔ | ✔ | H | bounded loop ✔ + gate de saída ✔ |
| EH-008 conflito | ✔ | ✔ | ✔ | ✔ | ✔ | P | bounded loop ✔ (registra e encerra) |
| EH-009 aging | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A (determinístico) |
| EH-010 ciclo de vida | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ (grafo CEM-001) |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário; cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); H/P com bounded loop; H/C com gate de saída (RULE-MECH-03). **PASS.**

---

## 3. Critérios EARS

9 critérios no formato "Quando <condição>, o Evidence Harness DEVE/NÃO DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-EH-001..005 (mapeiam as 10 BASpecs) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E2 piso Evidência/Agente; E3 na invalidação irreversível |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ EC-EH-003 (detector); RULE-EH-006; ADV-EH-04; SRC-03 [EXTERNO] |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-EH-005 (transição irreversível) + todos os EC |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-EH [PROPOSTA]; só Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-EH-005 (amostral; limiar = gap aberto) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. CC-02/CC-08/CC-11 = críticos aplicáveis, PASS. CC-01/CC-04 = PASS (camada neutra; INV-04 reforçado). CC-03 = Conviction pendente (J-001) declarado. CC-05 = CRITICAL/D0–D8. CC-09/CC-10 = aplicados (epistêmico; termo CEM não redefinido). CC-06/CC-07 = N/A justificado (não é Engineering Card). **CC-12 = N/A** (domain-agnostic; homologado research.md §6-bis Q-A3). **CC-11 = INCIDE e aplicada** (Classe por BASpec). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04): CEM-001 (Cap.3/4/5/6), CHM-001, SPEC-001 v1.1, SPEC-019/020/021 v1.0, atomic-spec v1.5. ✔
- REMOVED vazio. ✔
- MODIFIED declarado (RULE-004 estendida em cobertura, sem alterar texto — RULE-HD-02 respeitada). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (herança sobre modelo canônico, não decomposição pai→filha de macro-spec). ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| J-001 NÃO fechada; nenhum limiar numérico de convicção fixado (RULE-EH-003; ADV-EH-03) | ✔ |
| M-001 NÃO fechada; estados do Blackboard para Evidência não fixados (ADV-EH-09; D6) | ✔ |
| H-001 NÃO fechada; storage/Cognitive Trace Reconstruction referenciados como abertos | ✔ |
| Mecânica de fusão/DERIVED DIFERIDA a SPEC-003 (ADV-EH-10); só fronteira aqui | ✔ |
| RULE-EH etiquetadas [PROPOSTA]; CEM-001/INV-*/ENF-03/RULE-004/RULE-EPI... como FATO NORMATIVO existente | ✔ |
| Fontes SRC-01..06 etiquetadas [EXTERNO]; nada vira baseline | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.**

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| CEM-001 (Cap.3/4/5/6) | ✔ | canon/CEM-001 (BASELINE) |
| CHM-001; SPEC-001 v1.1 | ✔ | canon/CHM-001; specs/features/SPEC-001 (BASELINE) |
| SPEC-019/020/021 v1.0; RULE-HG-*/RULE-EV-*/RULE-MM-* | ✔ | RULES.md (baseline FASE GOV) |
| INV-04/06/07/09/10 | ✔ | atomic-spec §13 |
| ENF-01..08 (esp. ENF-03) | ✔ | atomic-spec §10.4 |
| RULE-004; RULE-BB-002/003/004 | ✔ | RULES.md |
| RULE-EPI-01/RULE-CAU-01/RULE-MET-01/RULE-UNC-03/RULE-PRB-02/RULE-SEM-01/04/RULE-DEC-01 | ✔ | RULES.md v1.5 (DHR-REG-001) |
| RULE-MECH-01..04 (CC-11); RULE-PD-01 (CC-12) | ✔ | RULES.md |
| RULE-ECC-01/02/04 | ✔ | RULES.md |
| EC-COG-005 (Cognitive Event Bus) | ✔ | CEM-001 Cap.6; contrato → SPEC-005 |
| SRC-01..06 (fontes externas) | ✔ (verbatim) | specs/features/SPEC-002/sources/SRC-0N.txt (RULE-ECC-04) |
| RULE-EH-001..008; BASpec-EH-001..010; EC-EH-001..005 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **RULE-REG-001** DISPAROU na abertura e foi **HOMOLOGADO** (research.md §6-bis Q-A4; RULES.md v1.5 / atomic-spec v1.5) → **tratado**. ✔
- **BL-012** (MC-COG-001) NÃO dispara nesta redação; **IMINENTE** na homologação da SPEC-002 (registrado). ✔
- **BL-002/003/004/017** NÃO disparam (SPEC-002 não é gatilho). ✔
- **BL-024** Absorvido (pré-condição satisfeita na abertura). ✔
- **BL-008** independente (já `Absorvido` — auditoria retroativa da SPEC-001 concluída). ✔
- Nenhum item ATIVADO pendente sem encaminhamento. **PASS.**

---

## 10. RULE-ECC-04 (Captura Verbatim de Fonte) — verificação de presença

| Fonte carregada | Arquivo companheiro presente | Citação verbatim no Dossiê |
|---|---|---|
| SRC-01 W3C PROV | ✔ sources/SRC-01-w3c-prov.txt | ✔ research.md §2.1 |
| SRC-02 GRADE | ✔ sources/SRC-02-grade-evidence-quality.txt | ✔ |
| SRC-03 ECon | ✔ sources/SRC-03-econ-evidence-conflict.txt | ✔ |
| SRC-04 OpenLineage | ✔ sources/SRC-04-openlineage.txt | ✔ |
| SRC-05 Evidence of absence | ✔ sources/SRC-05-evidence-of-absence.txt | ✔ |
| SRC-06 Dependent Fusion | ✔ sources/SRC-06-dependent-evidence-fusion.txt | ✔ |

> A **correspondência verbatim** string-a-string é mandato do Revisor (sem web — ENF-03). Aqui só se verifica **presença** dos 6 arquivos e das citações. **PASS (presença).**

---

## 11. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (herança sobre canônico, não macro→micro) | Menor | Revisor confirma o eixo de herança |
| CK-02 | D9 auditoria/Cognitive Trace Reconstruction apenas por referência (H-001/SPEC-006) | Menor | Consistente com alvo D0–D8; delegado ao KG (CEM-001 Cap.5) |
| CK-03 | 3 achados Menores do parecer do Revisor sobre o research.md (§6-bis) carregados ao Plan | Menor | Revisor reconfirma/trata na auditoria desta entrega |
| CK-04 | BL-012 (MC-COG-001) IMINENTE na homologação — usar estados CEM-001/CHM-001 (COL-COG-01) | Menor | Tratado no gate de homologação (não desta redação) |
| CK-05 | Correspondência verbatim RULE-ECC-04 (string) fica para o Revisor | Info | Mandato do Revisor (sem web) |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (EH-001..010) com Classe/Mecanismo (CC-11), EARS (9), Enforcement (EC-EH-001..005; ENF-03 detector≠gate; E3 na invalidação), Constitution Check CC-01..CC-12, Herança/Delta (CC-08), CONS-01 (J-001/M-001/H-001 abertas), gate RMR-001 e RULE-ECC-04 (presença) satisfeitos. 5 achados não-bloqueantes (CK-01..CK-05) encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `validate_spec_sot.py` + submissão ao Revisor SOT.
