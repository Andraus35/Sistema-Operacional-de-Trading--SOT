# checks.md — Verificação de Spec da SPEC-020 (fase spec-first)

**Objeto:** `specs/features/SPEC-020/plan.md` (Harness Evaluation Specification — núcleo A + 9ª lente principiológica)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §12]
**Método:** atomic-spec v1.4
**Data:** 2026-09-27

---

## 1. Cobertura de profundidade (D0–D8 — alvo ROADMAP §12; CRITICAL)

| Nível | Exigido (CRITICAL, alvo D0–D8) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (meta-harness de avaliação; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S7 + Non-goals (maturidade/classe B/limiares/runtime) |
| D2 Regra | Sim | ✔ | RULE-EV-01..07 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | EV-001..009 (as 9 lentes) |
| D4 Algoritmo | Quando há regra determinística numérica | N/A | Avaliação qualitativa; limiar numérico dependeria de J-001 (justificado) |
| D5 Estado | Sim | ✔ | Máquina de estados da lente (DETECTED/PASS/FAIL/INDETERMINADO/REGRESSED) |
| D6 Protocolo | Sim | ✔ | Protocolo de avaliação (8 passos; acopla RULE-HG-06) |
| D7 Teste | Sim (CRITICAL) | ✔ | Cenários EV-T01..T05 |
| D8 Adversarial | Sim (CRITICAL) | ✔ | ADV-EV-01..07 (7 cenários) |
| D9 Auditoria | Sistema completo | Parcial (por referência) | Reconstrução → SPEC-041; P13 |

**Resultado:** profundidade-alvo D0–D8 atingida. D4 N/A justificado (sem regra determinística numérica; J-001 aberto).

---

## 2. Well-formedness das BASpecs (as 9 lentes)

| BASpec (lente) | QUANDO observável | ENTÃO mensurável | PORQUE | REFERÊNCIA | VERIFICADO POR |
|---|---|---|---|---|---|
| EV-001 correctness | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-002 grounding | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-003 hallucination | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-004 role adherence | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-005 context management | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-006 safety | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-007 regression | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-008 robustness | ✔ | ✔ | ✔ | ✔ | ✔ |
| EV-009 principle consistency | ✔ | ✔ | ✔ | ✔ | ✔ |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário. **PASS.**

---

## 3. Critérios EARS

9 critérios no formato "Quando <condição>, o Harness Evaluation DEVE/NÃO DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-EV-001..004 |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E3 (gate de spec-time) / E2 (detector/regressão) por criticidade |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ RULE-EV-02/03; EC-EV-002; D5 (DETECTED≠veredito); ADV-EV-01 |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ todos os EC declaram fail-closed |
| ENF-05 Policies não auto-aprendidas | ✔ avaliação não homologa; Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-EV-001/004 (amostral; limiar = gap aberto) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-10)

Preenchido no plan.md. CC-02/CC-08/CC-09 = críticos aplicáveis, PASS. CC-01/CC-04 = PASS (lentes protegem a hierarquia/salvaguardas). CC-03 = Conviction pendente (J-001) declarado. CC-05 = CRITICAL/D0–D8. CC-06/CC-07/CC-10 = N/A justificado. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04: atomic-spec v1.4, SPEC-019 v1.0, SPEC-001 v1.1, GPR-001 v1.0). ✔
- REMOVED vazio. ✔
- MODIFIED declarado (RULE-HG-06 estendida em *itens*, sem alterar texto). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (irmã, não filha de SPEC-019) — coerente com ADV-HV-07 da SPEC-019. ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| J-001 NÃO fechada; nenhum limiar numérico de convicção fixado (RULE-EV-05; ADV-EV-07) | ✔ |
| SPEC-020-PRINC-001 NÃO declarada fechada (efetiva na homologação) | ✔ |
| Classe B DIFERIDA (BL-017); não fechada (ADV-EV-06) | ✔ |
| ECC-VAL-001 resolvida só para esta Spec; regra geral permanece aberta | ✔ |
| RULE-EV etiquetadas [PROPOSTA]; ENF-03/RULE-HG-06/RULE-ICT-007/INV-* como FATO NORMATIVO existente | ✔ |
| Fontes externas E1–E13 etiquetadas [EXTERNO]; nada vira baseline | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.**

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| ENF-01..08 (esp. ENF-03) | ✔ | atomic-spec §10.4 |
| RULE-HG-02/03/04/06 | ✔ | RULES.md (SPEC-019) |
| RULE-ICT-007 | ✔ | RULES.md |
| RULE-EPI / RULE-MET-01 / RULE-DEC | ✔ | atas EUA-E05/E13/E14 (RULES até v1.5) |
| INV-04/05/07/09/10 | ✔ | atomic-spec §13 |
| GPR-001 §15 (checklist) / PC-01..PC-08 | ✔ | GPR-001 (baseline) |
| CEE-001 §10/§11 | ✔ | RULES.md (RULE-CEE-001/004) |
| RULE-EV-01..07; EC-EV-001..004; 9 lentes | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **BL-021** ATIVADO por `spec:SPEC-020 em redação` → **tratado** (nota de gate; tooling, cada sub-item exige aprovação própria; não bloqueia). ✔
- **BL-017** (dimensões B) NÃO dispara (gatilho SPEC-007/014/038; não inclui SPEC-020) → permanece `Proposto`. ✔
- **BL-020** (web só-leitura do Revisor) NÃO dispara (só `spec:SPEC-020 homologada`). Registrado. ✔
- **BL-008** independente (`ATIVADO` — auditoria retroativa da SPEC-001). ✔
- Nenhum item ATIVADO pendente sem encaminhamento. **PASS.**

---

## 10. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | ACH-001 (achado Menor do parecer do Revisor sobre o research.md) carregado ao Plan | Menor | Revisor reconfirma/trata na auditoria desta entrega |
| CK-02 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (SPEC-020 irmã de SPEC-019) | Menor | Revisor confirma o eixo de herança (horizontal vs vertical) |
| CK-03 | D9 auditoria apenas por referência (não fechada) | Menor | Consistente com alvo D0–D8; D9 pertence a SPEC-041 |
| CK-04 | Extensão de `validate_spec_sot.py` para check "Dossiê presente" e itens de lente | Menor | Depende de BL-021 (aprovação própria); não bloqueia esta Spec |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (9 lentes), EARS, Enforcement (ENF-03 detector≠gate), Constitution Check, Herança/Delta, CONS-01 e gate RMR-001 satisfeitos. 4 achados não-bloqueantes (CK-01..CK-04) encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `validate_spec_sot.py` + submissão ao Revisor SOT.
