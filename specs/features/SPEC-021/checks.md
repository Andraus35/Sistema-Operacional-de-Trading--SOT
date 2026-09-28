# checks.md — Verificação de Spec da SPEC-021 (fase spec-first)

**Objeto:** `specs/features/SPEC-021/plan.md` (Harness Score / Maturity Model — escada canônica por-Spec L0–L4)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §12]
**Método:** atomic-spec v1.4
**Data:** 2026-09-28

---

## 1. Cobertura de profundidade (D0–D7 — alvo ROADMAP §12; HIGH)

| Nível | Exigido (HIGH, alvo D0–D7) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (meta-harness de maturidade; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas S1–S9 + Non-goals (SPEC-020/classe B/limiares/GPR §11/runtime) |
| D2 Regra | Sim | ✔ | RULE-MM-01..07 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | HS-001..008 com Classe declarada (RULE-MECH-01) |
| D4 Algoritmo | Quando há regra determinística numérica | N/A justif. + procedimento não-numérico | Atribuição ordinal; limiar numérico dependeria de J-001 (justificado); ALGORITMO não-numérico presente |
| D5 Estado | Sim | ✔ | Máquina de estados (NOT_SCORED/DETECTED/LEVELED/ELIGIBLE/BLOCKED/INDETERMINADO) |
| D6 Protocolo | Sim | ✔ | Protocolo de atribuição (9 passos; acopla RULE-HG-06 + lentes SPEC-020) |
| D7 Teste | Sim (HIGH) | ✔ | Cenários HS-T01..T05 |
| D8 Adversarial | Reforço §7-bis (obrigatório HIGH) / alimenta L3 | ✔ | ADV-HS-01..08 (8 cenários) |
| D9 Auditoria | Sistema completo | Parcial (por referência) | Reconstrução → SPEC-041; P13; L4 só na implementação |

**Resultado:** profundidade-alvo D0–D7 atingida (teto HIGH respeitado; D8 via §7-bis, não elevação de profile). D4 N/A numérico justificado + procedimento determinístico não-numérico.

---

## 2. Well-formedness das BASpecs (HS-001..008) + Classe (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE + 4Es | Bounded loop/Gate (H/C) |
|---|---|---|---|---|---|---|---|
| HS-001 critérios de nível | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| HS-002 atribuição determinística | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| HS-003 staged | ✔ | ✔ | ✔ | ✔ | ✔ | D · Eficácia | N/A (D) |
| HS-004 nível-alvo | ✔ | ✔ | ✔ | ✔ | ✔ | D · Efetividade | N/A (D) |
| HS-005 gate normativo E3 | ✔ | ✔ | ✔ | ✔ | ✔ | C · Conformidade | Gate de saída (comparação atingido≥alvo) ✔ |
| HS-006 anti-gaming | ✔ | ✔ | ✔ | ✔ | ✔ | H · Eficácia | Bounded loop (1/submissão) + gate de saída (recomputo) ✔ |
| HS-007 rejeição limiar convicção | ✔ | ✔ | ✔ | ✔ | ✔ | C · Conformidade | Gate de saída (ausência de limiar) ✔ |
| HS-008 coexistência de scores | ✔ | ✔ | ✔ | ✔ | ✔ | D · Efetividade | N/A (D) |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário. Classe declarada por BASpec (não por Spec — SES-001 §50). Nenhuma Classe C em risco baixo (HS-005/007 são E3). **PASS.**

---

## 3. Critérios EARS

8 critérios no formato "Quando <condição>, o Harness Score DEVE/NÃO DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-HS-001..003 |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ E3 (atribuição/gate) / E2 (detector) por criticidade |
| ENF-03 Gate determinístico; Detector ≠ Gate; LLM nunca é seu próprio gate | ✔ RULE-MM-02; EC-HS-003; D5 (DETECTED≠veredito); ADV-HS-02 |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-HS-001/002 declaram fail-closed |
| ENF-05 Policies não auto-aprendidas | ✔ maturidade não homologa; Andraus homologa (RULE-HG-03) |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-HS-001/002 (amostral; limiar = gap aberto) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12)

Preenchido no plan.md. CC-02/CC-08/CC-11 = críticos aplicáveis, PASS. CC-01/CC-04 = PASS (maturidade protege hierarquia/salvaguardas). CC-03 = Conviction pendente (J-001) declarado. CC-05 = HIGH/D0–D7. CC-06/CC-07 = N/A justificado (não é Engineering Card). CC-09/CC-10 = PASS/N/A justificado. **CC-11 INCIDE** (Classe por BASpec — RULE-MECH-01, citada no texto). **CC-12 = N/A justificado** (meta-harness, sem escopo de especialidade de mercado; atomic-spec §10.7 nomeia a SPEC-021). **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04: atomic-spec v1.4, SPEC-019 v1.0, SPEC-020 v1.0, GPR-001 v1.0). ✔
- REMOVED vazio. ✔
- MODIFIED declarado (RULE-HG-06 estendida em *itens*, sem alterar texto; Quality Gates §7 não modificadas — reusadas). ✔
- Eixo VERTICAL (RULE-HV) avaliado e declarado **não aplicável** (irmã, não filha de SPEC-019/SPEC-020) — coerente com o precedente da SPEC-020 e o ADV-HV-07 da SPEC-019. ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| J-001 NÃO fechada; nenhum limiar numérico de convicção fixado (RULE-MM-06; ADV-HS-04) | ✔ |
| Escada GPR-001 §11 (L0–L5) NÃO redefinida (eixo diferente; ADV-HS-05) | ✔ |
| Quality Gates L1–L4 NÃO redefinidas (reusadas como tabela de critérios) | ✔ |
| 9 lentes da SPEC-020 NÃO redefinidas/duplicadas (RULE-MM-07; ADV-HS-06) | ✔ |
| Classe B DIFERIDA (BL-017); não fechada | ✔ |
| SPEC-045-RUNTIME-001 / tooling de runtime NÃO antecipado (Non-goal) | ✔ |
| ECC-VAL-001 resolvida só para esta Spec; regra geral permanece aberta | ✔ |
| RULE-MM etiquetadas [PROPOSTA]; ENF-03/04, RULE-HG-06, RULE-MECH-01..04, RULE-EV-01, INV-* como FATO NORMATIVO existente | ✔ |
| Fontes externas M1–M11 etiquetadas [EXTERNO]; nada vira baseline | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.**

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| ENF-01..08 (esp. ENF-03/04) | ✔ | atomic-spec §10.4 |
| RULE-HG-02/03/04/06/08 | ✔ | RULES.md (SPEC-019) |
| RULE-HV-01..04 | ✔ | RULES.md (SPEC-019) |
| RULE-MECH-01..04 (CC-11) | ✔ | RULES.md; atomic-spec §9/§10.5/§10.6 |
| RULE-PD-01..03 (CC-12) | ✔ | RULES.md; atomic-spec §10.7 |
| RULE-EV-01..07 (9 lentes SPEC-020) | ✔ | SPEC-020/plan.md (baseline) |
| RULE-ECC-01/02 | ✔ | RULES.md |
| Quality Gates L1–L4 (§7) | ✔ | atomic-spec §7 |
| GPR-001 §11 (L0–L5) / §15 / PC/PB/PE-04 | ✔ | GPR-001 (baseline) |
| RULE-EPI / RULE-MET-01 / RULE-DEC | ✔ | atas EUA-E05/E13/E14 (RULES até v1.5) |
| INV-03/05/07/09 | ✔ | atomic-spec §13 |
| RULE-MM-01..07; EC-HS-001..003; BASpec-HS-001..008 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- Nenhum gatilho novo disparado por `spec:SPEC-021 em redação`. ✔
- **BL-020** (web só-leitura do Revisor) `ATIVADO` desde 2026-09-27 (independente; pendente de Andraus) → registrado, não bloqueia. ✔
- **BL-017** (dimensões B) NÃO dispara (gatilho SPEC-007/014/038; não inclui SPEC-021) → permanece `Proposto`. ✔
- **BL-021** (ferramental EUA-E21) Absorvido; STRUCT-11 (Dossiê presente) satisfeito (research.md na pasta). ✔
- **BL-008** independente (`ATIVADO`). ✔
- **BL-022/023** (PRINC-BID-001/CLASSE-MECH-001) Absorvidos; RULE vigentes e aplicadas. ✔
- Nenhum item ATIVADO pendente sem encaminhamento por esta redação. **PASS.**

---

## 10. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | Nota de reconciliação "D4 numérico N/A não rebaixa nível" é [PROPOSTA] de tratamento de D-levels N/A na atribuição | Menor | Revisor/Andraus confirmam o tratamento (não redefine Quality Gates) |
| CK-02 | Eixo VERTICAL (RULE-HV) declarado não aplicável por [INFERÊNCIA] (SPEC-021 irmã de SPEC-019/020) | Menor | Revisor confirma o eixo de herança (horizontal vs vertical) |
| CK-03 | D9 auditoria apenas por referência; critério L4 só atingível na implementação | Menor | Consistente com alvo D0–D7; D9 → SPEC-041; L4 → runtime (RULE-MM-04) |
| CK-04 | Achado Menor A-01 do parecer do Revisor sobre o research.md (fontes pós-treino) | Menor | Já registrado no §7-bis do Dossiê; Revisor reconfirma |
| CK-05 | EUA-E18 Q7 — checagem de proporcionalidade do protocolo §7-bis/Passo 5-bis (3ª spec) | Procedimental | Conduzida no relatório de revisão semântica desta Spec (Q-A7) |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (HS-001..008 com Classe), EARS (8), Enforcement (ENF-03 detector≠gate; EC-HS-001..003), Constitution Check (CC-01..12; CC-11 incide, CC-12 N/A justificado), Herança/Delta, CONS-01 e gate RMR-001 satisfeitos. 5 achados não-bloqueantes (CK-01..CK-05) encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: gate determinístico `python scripts/validate_spec_sot.py specs/features/SPEC-021/plan.md` + submissão ao Revisor SOT.
