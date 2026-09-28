# checks.md — Verificação de Spec da SPEC-046 (fase spec-first)

**Objeto:** `specs/features/SPEC-046/plan.md` (Spec-Time Context Caching Harness — Grupo B, Especificador/Revisor)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; AGENTS.md §5]
**Método:** atomic-spec v1.4
**Data:** 2026-09-28

---

## 1. Cobertura de profundidade (D0–D7 — alvo HIGH; D8 de reforço para L3)

| Nível | Exigido (HIGH, alvo D0–D7 + reforço L3) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão — precondição de freshness, distinta do cache HTTP do provedor |
| D1 Escopo/Non-goals | Sim | ✔ | Tabela dentro-do-escopo + Non-goals (Grupo A/ACHADO-M2/cache_control/patches automáticos/cache semântico/Blackboard/veículo técnico) + Limitações declaradas |
| D2 Regra | Sim | ✔ | RULE-C46-001..005 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | BASpec-C46-001..004 com Classe declarada (RULE-MECH-01) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | `verify_freshness` (SHA-256, com exemplo numérico ilustrativo e nota de efeito avalanche) |
| D5 Estado | Sim | ✔ | Máquina de estados NÃO-REGISTRADO/REGISTRADO/FRESH/STALE/UNVERIFIABLE |
| D6 Protocolo | Sim (todos os agentes) | N/A justificado | Especificador/Revisor não publicam no Blackboard — declarado explicitamente, não omitido |
| D7 Teste | Sim (HIGH) | ✔ | Cenários C46-T01..T04 (4, ≥3 exigidos) |
| D8 Adversarial | Reforço (obrigatório p/ gate L3, não pela tabela D0-D9 pois não é CRITICAL) | ✔ | ADV-C46-01..04 (4 cenários, ≥1 exigido) |
| D9 Auditoria | Sistema completo | N/A (fora do alvo HIGH) | EVIDENCE de EC-SPEC046-01 supre auditoria pontual; reconstrução plena não é objetivo desta Spec |

**Resultado:** profundidade-alvo D0–D7 atingida; D6 N/A justificado (não omisso); D8 presente como reforço (satisfaz gate L3 e §7-bis Bloco A, mesmo padrão do precedente SPEC-021). **PASS.**

---

## 2. Well-formedness das BASpecs (C46-001..004) + Classe (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE + 4Es | Bounded loop/Gate (H/P/C) |
|---|---|---|---|---|---|---|---|
| C46-001 captura de hash | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| C46-002 verificação de freshness | ✔ | ✔ | ✔ | ✔ | ✔ | H · Eficácia | Bounded loop (1 releitura) + gate de saída (comparação de hash) ✔ |
| C46-003 rebaixamento de etiqueta | ✔ | ✔ | ✔ | ✔ | ✔ | P · Conformidade/Eficácia | Bounded loop (herdado de C46-002; decisão imediata) ✔ (sem gate de saída binário — julgamento qualitativo, conforme mínimo de Classe P) |
| C46-004 higiene de sessão | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficiência | N/A (D) |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário. Classe declarada por BASpec (não por Spec — SES-001 §50, CC-11). Nenhuma Classe C proposta (risco E2, não E3 — Classe C reservada a enforcement de risco alto; ver RULE-C46-005, tratada como regra transversal, não BASpec própria com Classe C — evita violação de Economicidade por sobre-classificação). **PASS.**

---

## 3. Critérios EARS

Formato-base "Quando <condição>, o componente DEVE <resposta>" verificável nas 4 BASpecs (QUANDO/ENTÃO) e nos 4 adversariais (DADO/QUANDO/ENTÃO). Sem multi-outcome não-decomposto — cada BASpec tem 1 condição observável e 1 comportamento mensurável. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-SPEC046-01 (E2) + EC-SPEC046-02 (E1) |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E2 para verificação de freshness (acima do piso E1 de "Observação/Skill"; justificado por criticidade epistêmica, não por trading); E1 para auditoria de higiene (F.3, não operacional) |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ comparação de hash é código, não autoavaliação (BASpec-C46-002 GATE DE SAÍDA); ADV-C46-04 reforça explicitamente para aplicação automática de correções |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-SPEC046-01 FAILURE-MODE — reler ou rebaixar, nunca presumir freshness |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-C46-001..005 são [PROPOSTA] até homologação; nenhuma regra se autoaplica sem gate |
| ENF-06 E0 declarado como orientação | N/A (não há E0 nesta Spec — mínimo declarado é E1) |
| ENF-07 E3 declara método de falso-DENY | N/A (nenhum EC desta Spec é E3 — maior nível é E2, que não exige método de falso-DENY pelo mínimo do atomic-spec §10.3) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2, citada nos dois ECs |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12)

Preenchido no plan.md. CC-01/CC-02/CC-04 = PASS (hierarquia/canônicos/salvaguardas protegidos, não tocados — Spec de tooling spec-time). CC-03 = N/A (sem Conviction Vector). CC-05 = HIGH/D0–D7. CC-06/CC-07 = N/A justificado (não é Engineering Card, mesmo tratamento de SPEC-019/020/021). CC-08 = Bloco Herança/Delta presente, eixo VERTICAL declarado não aplicável (linha nova paralela, não filha). CC-09 = aplicado (etiquetagem completa, veículo técnico mantido [PROPOSTA]). CC-10 = N/A quanto a escola de mercado; aplicado de forma análoga à distinção cache semântico/exato/HTTP-provedor. **CC-11 INCIDE** (Classe por BASpec — RULE-MECH-01 citada no texto; 4/4 BASpecs classificadas D/H/P, nenhuma C). **CC-12 = N/A confirmado pelo Revisor no parecer de abertura** (não é Spec de especialidade de domínio de mercado). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS preenchido com ID+versão (atomic-spec v1.4; PROPOSTA-ABERTURA.md v1.0 + DOSSIE-PESQUISA.md v1.0, DHR-SPEC046-001; RULE-ECC-01/02/04; ENF-01..08; RULE-MECH-01..04; INV-09; TRACE-06; CONS-01). ✔
- ADDED preenchido (4 BASpecs, D4/D5, D7/D8, schema I/O, EC-SPEC046-02). ✔
- MODIFIED declarado (formalização dos 8 campos de EC-SPEC046-01 sem alteração de substância já homologada). ✔
- REMOVED vazio. ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** — SPEC-046 não decompõe nenhum macro-Spec já homologado (linha nova/paralela, não filha de SPEC-019/020/021). ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| Grupo A NÃO tratado como aberto por esta Spec (é non-goal deliberado, não decisão aberta bloqueadora) | ✔ |
| ACHADO-M2 explicitamente marcado como aplicável ao Grupo A, fora de escopo aqui | ✔ |
| J-001/M-001/demais decisões abertas do SOT não tocadas nem fechadas | ✔ (N/A — Spec não as referencia) |
| ECC-VAL-001 permanece aberta (não fechada por esta Spec) | ✔ |
| Veículo técnico de implementação mantido [PROPOSTA]/[DECISÃO NECESSÁRIA], não apresentado como fechado | ✔ |
| RULE-C46-001..005 etiquetadas [PROPOSTA]; SRC-01..07 etiquetadas [EXTERNO]; nada vira baseline | ✔ |
| Mecanismo nativo do provedor (SRC-06) tratado como FATO NORMATIVO (documentação oficial), distinto da precondição de freshness desta Spec (que é [PROPOSTA]) | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.**

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| ENF-01..08 | ✔ | atomic-spec §10.4 |
| RULE-ECC-01/02/04 | ✔ | governance/RULES.md:426-465 |
| RULE-MECH-01..04 | ✔ | RULES.md; atomic-spec §9/§10.5/§10.6 |
| INV-09 | ✔ | atomic-spec §13 |
| TRACE-06 | ✔ | atomic-spec §11 |
| CONS-01 | ✔ | atomic-spec §11 |
| RULE-EPI-01/RULE-CAU-01/RULE-PRB-01/RULE-MET-01/RULE-DEC/RULE-UNC | ✔ | atas EUA-E05/E09/E12/E13/E14 (RULES até v1.5, citadas como vigentes conforme RMR-EST/RULE-REG-001) |
| DHR-SPEC046-001 | ✔ | governance/DHR-SPEC046-001_...md |
| DHR-VERBATIM-SRC-001 | ✔ | RMR-001 §6 BL-020 |
| RULE-C46-001..005; BASpec-C46-001..004; EC-SPEC046-01/02 | [PROPOSTA] | esta Spec — não citadas como já existentes/vigentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **BL-024** — gatilho original preservado (`evento:abertura da SPEC-002`), não alterado por este Plan; este Plan é continuação registrada da linha aditiva já aberta por DHR-SPEC046-001. ✔
- **BL-008** — independente, segue `ATIVADO`. ✔
- **ACH-OBS-01** (status de BL-008) — não resolvido por este Plan, fora de escopo declarado. ✔
- Nenhum item `ATIVADO` novo disparado pela redação deste Plan. **PASS.**

---

## 10. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Veículo técnico de implementação (script novo vs. `check_doc_sync.py` estendido) permanece [PROPOSTA]/[DECISÃO NECESSÁRIA] | Menor | Revisor/Andraus confirmam se deve ser resolvido neste gate ou diferido a Tasks/BUILD |
| CK-02 | Nível E2 (não E1) atribuído à precondição de freshness, acima do piso mínimo — justificado por criticidade epistêmica de TRACE-06/[FONTE], não por efeito irreversível clássico | Menor | Revisor confirma a justificativa do nível (ENF-02) |
| CK-03 | D9 (auditoria completa) declarado N/A/fora do alvo — apenas EVIDENCE pontual de EC-SPEC046-01 | Menor | Consistente com alvo D0–D7 (HIGH); reconstrução plena não é objetivo desta Spec |
| CK-04 | Limitação declarada (hash não garante imutabilidade histórica, só identidade no momento da checagem) — aceita explicitamente, não escondida | Observação | Revisor confirma que a limitação é proporcional ao objetivo da Spec |
| CK-05 | Classe P de BASpec-C46-003 não tem GATE DE SAÍDA binário (mínimo de Classe P permite isso — GATE DE SAÍDA é opcional em P, atomic-spec §10.6) | Observação | Revisor confirma leitura do mínimo por Classe |

---

## 11. Verificação estrutural da EMENDA v1.1 — Caching Inter-Sessão (EC-SPEC046-03 + BASpecs CISS-001..004)

**Natureza:** verificação estrutural do bloco aditivo v1.1 (não altera as seções 1–10, que auditam v1.0 baseline). [FONTE: plan.md §"EXTENSÃO v1.1"]

### 11.1 Aditividade e versionamento monotônico (INV-07)
| Check | Resultado |
|---|---|
| v1.0 (D0–D8, EC-SPEC046-01/02, BASpec-C46-001..004) preservado sem exclusão/alteração de substância | ✔ bloco v1.1 é apêndice; nenhuma seção v1.0 removida |
| Histórico de versões acrescenta linha 1.1 sem apagar 1.0 | ✔ |
| Escopo/fronteira/Classe predominante (H)/EC-SPEC046-01 de v1.0 não alterados | ✔ v1.1 é dimensão de persistência inter-sessão, aditiva (INV-07) |

### 11.2 EC-SPEC046-03 (8 campos + E3)
| Check | Resultado |
|---|---|
| 8 campos presentes (CAPABILITY/EFFECT/PRECOND/POSTCOND/POLICY/LEVEL/FAILURE-MODE/EVIDENCE) | ✔ |
| Nível REAVALIADO (não herdado do E2 de EC-SPEC046-01) | ✔ **E3** justificado: remoção do backstop de leitura intra-sessão + persistência = superfície durável |
| Mínimos E3: PRECOND+POSTCOND+POLICY+FAILURE-MODE + método de falso-DENY (ENF-07) | ✔ método de falso-DENY declarado (falso-DENY degrada para releitura segura; assimetria por construção) |
| Aditivo a EC-SPEC046-01, não o contradiz (intra vs. inter-sessão) | ✔ |
| Fail-closed obrigatório (ENF-04) em manifesto ausente/corrompido/divergente | ✔ |

### 11.3 Well-formedness BASpecs CISS-001..004 + Classe (CC-11)
| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE + 4Es | Bounded loop/Gate (H/C) |
|---|---|---|---|---|---|---|---|
| CISS-001 persistência do manifesto | ✔ | ✔ | ✔ | ✔ | ✔ | D · Economicidade | N/A (D) |
| CISS-002 validação início + skip | ✔ | ✔ | ✔ | ✔ | ✔ | H · Eficiência | Bounded loop (1 releitura) + gate de saída por código ✔ |
| CISS-003 fail-closed (ausente/corrompido) | ✔ | ✔ | ✔ | ✔ | ✔ | C · Conformidade/Eficácia | Gate de saída (permit/deny) ✔; justificativa Classe C (risco não-baixo) presente |
| CISS-004 autoridade ENF-03 | ✔ | ✔ | ✔ | ✔ | ✔ | C · Eficácia | Gate de saída (código é o gate) ✔ |

**Decisão sobre fundir CISS-003/004:** MANTIDAS SEPARADAS (4 BASpecs), justificada (ENF-04 default vs. ENF-03 autoridade auditáveis independentemente; RULE-MECH-02, risco não-baixo). Nenhum Classe C sobre risco baixo. **PASS.**

### 11.4 D4-ISS/D5-ISS/D7-ISS/D8-ISS
| Nível | Presente | Evidência |
|---|---|---|
| D4-ISS Algoritmo | ✔ | `validate_session_manifest`, reuso de `build_map.py:81,341-342` (verificado nesta redação); manifesto em `docs/cache/` (não-normativo, INV-09) |
| D5-ISS Estado | ✔ | Máquina do manifesto (AUSENTE/PRESENTE-íntegro/CORROMPIDO/generated_by≠code) + por-arquivo (FRESH/STALE/ABSENT/CORROMPIDO); fail-closed sem regressão silenciosa |
| D7-ISS Teste | ✔ | Cenários CISS-T01..T03 (3, ≥3 exigido) |
| D8-ISS Adversarial | ✔ | ADV-CISS-01 (manifesto adulterado entre sessões — falso-FRESH; ≥1 exigido) com nota de robustez (recomputação por código, não confiança no campo) |

### 11.5 Honestidade (RULE-MET-01) e ENF-03
| Check | Resultado |
|---|---|
| L-ISS-01 no corpo (D1) — economia de tokens condicionada a substrato de reuso cross-sessão; declarada como limitação/Non-goal, não promessa | ✔ (também linha nos Non-goals + EC-SPEC046-03 D0-delta) |
| ENF-03 — manifesto escrito/validado só por código; agente consome veredito, nunca autocertifica | ✔ CISS-004; campo `generated_by=="code"` |
| `build_map.py` hashing citado como reuso (não hashing novo), com linha verificada | ✔ build_map.py:81 (SHA-256/arquivo), :341-342 (--check) |

**PASS (v1.1).**

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (C46-001..004 com Classe), EARS (4 BASpecs + 4 adversariais), Enforcement (EC-SPEC046-01 E2 + EC-SPEC046-02 E1; ENF-03 detector≠gate reforçado por ADV-C46-04), Constitution Check (CC-01..12; CC-11 incide, CC-12 N/A confirmado), Herança/Delta, CONS-01 e gate RMR-001 satisfeitos. Achados Menores de abertura (ACH-MEN-01/02) confirmados sanados antes deste Plan. 5 achados não-bloqueantes (CK-01..CK-05) encaminhados.

**Emenda v1.1 (Caching Inter-Sessão) — estruturalmente CONFORME** (seção 11): EC-SPEC046-03 (8 campos, E3 reavaliado com método de falso-DENY ENF-07), BASpecs CISS-001..004 (Classes D/H/C/C, CISS-003/004 mantidas separadas com justificativa), D4-ISS/D5-ISS/D7-ISS/D8-ISS presentes, aditividade INV-07 preservada, honestidade L-ISS-01 (RULE-MET-01) no corpo, ENF-03 (manifesto só por código). Achado observacional CK-06: veículo técnico definitivo (script novo vs. extensão de `build_map.py`) permanece [PROPOSTA]/BUILD.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `python scripts/validate_spec_sot.py specs/features/SPEC-046/plan.md` + submissão ao Revisor SOT.
