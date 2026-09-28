# checks.md — Verificação de Spec da SPEC-019 (fase spec-first)

**Objeto:** `specs/features/SPEC-019/plan.md` (Harness Governance & Evolution + Contrato de Herança Vertical)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §12]
**Método:** atomic-spec v1.4
**Data:** 2026-09-22

---

## 1. Cobertura de profundidade (D0–D8 — alvo ROADMAP §11)

| Nível | Exigido (HIGH, alvo D0–D8) | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (A + B) |
| D1 Escopo/Non-goals | Sim | ✔ | Tabelas de escopo A1–A10/B1–B3 + Non-goals |
| D2 Regra | Sim | ✔ | RULE-HG-01..08 · RULE-HV-01..04 [PROPOSTA] |
| D3 Comportamento (BASpec) | Sim | ✔ | HG-001..005 · HV-001..003 |
| D4 Algoritmo | Quando há regra determinística | N/A | Governança de processo; sem fórmula numérica (justificado) |
| D5 Estado | Sim (estado persistente/governança) | ✔ | Máquina de estados (aplica GMC-001, não redefine) |
| D6 Protocolo | Sim | ✔ | Protocolo de emenda/homologação (8 passos) |
| D7 Teste | Sim (HIGH) | ✔ | Cenários HG-T01..T03 · HV-T04 |
| D8 Adversarial | Alvo D0–D8 | ✔ | ADV-HG-01..04 · ADV-HV-05..07 (7 cenários) |
| D9 Auditoria | Sistema completo | Parcial (por referência) | RULE-HG-08; schema DHR; P13 |

**Resultado:** profundidade-alvo D0–D8 atingida. D4 N/A justificado (sem regra determinística numérica).

---

## 2. Well-formedness das BASpecs

| BASpec | QUANDO observável | ENTÃO mensurável | PORQUE | REFERÊNCIA | VERIFICADO POR |
|---|---|---|---|---|---|
| HG-001 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HG-002 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HG-003 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HG-004 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HG-005 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HV-001 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HV-002 | ✔ | ✔ | ✔ | ✔ | ✔ |
| HV-003 | ✔ | ✔ | ✔ | ✔ | ✔ |

Todas com 1 condição · 1 comportamento · ≤2 RULES · 1 cenário. **PASS.**

---

## 3. Critérios EARS

10 critérios no formato "Quando <condição>, o componente DEVE <resposta>". Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract presente em todo comportamento com efeito | ✔ EC-HG-001..004, EC-HV-001 |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ todos E3 (efeito normativo/irreversível) |
| ENF-03 Gate determinístico; Detector ≠ Gate | ✔ homologação de Andraus = gate; Revisor = detector |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ todos declaram fail-closed |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-HG-02; EC-HG-002 |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-HG-001/002 (amostral; limiar = gap aberto) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-10)

Preenchido no plan.md. CC-02/CC-08/CC-09 = críticos aplicáveis, PASS. CC-01/CC-03/CC-06/CC-07/CC-10 = N/A justificado. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08) e Herança Vertical

- Bloco §8.3 presente; INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04). ✔
- REMOVED vazio. ✔
- MODIFIED declarado (RULE-HD-02/03 estendidas ao eixo vertical, sem alterar texto original). ✔
- Auto-referência: a Spec que normativiza herança vertical declara a própria herança. ✔ (coerência)

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| L-001 NÃO declarada fechada (só proposta; efetiva na homologação) | ✔ |
| J-001 intocada; dimensionalidade=8 não usada como alavanca | ✔ |
| RULE-HG/HV etiquetadas [PROPOSTA]; RULE-HD/GMC/SDD/PPQ como FATO NORMATIVO existente | ✔ |
| CR-001 Cap.7/8 etiquetados FATO ARQUITETURAL (não baseline) | ✔ (CC-09) |
| MC-GOV-001 [EXTERNO] não adotada | ✔ |
| Nenhuma decisão aberta usada como invariante fechado | ✔ |

**PASS.**

---

## 8. Verificação de RULEs citadas (existência real)

| RULE citada | Existe? | Fonte |
|---|---|---|
| RULE-HD-01..04 | ✔ | RULES.md (via EUA-E04) |
| RULE-GMC-001..005 | ✔ | RULES.md |
| RULE-SDD-001/002; RULE-PPQ-001 | ✔ | RULES.md |
| RULE-DEC-01 | ✔ | EUA-E13 (ata; RULES.md até v1.5) |
| INV-05/07/09; ENF-05 | ✔ | atomic-spec §13/§10 |
| RULE-HG-01..08; RULE-HV-01..04 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- BL-013 (MC-GOV-001) ATIVADO por `spec:SPEC-019 em redação` → **tratado** (nota de gate; ref. externa diferida, não adotada). ✔
- BL-015 (MC-LRN-001) NÃO dispara (gatilho SPEC-018/K-001). ✔
- BL-017 (dimensões B SPEC-020) não incidente. ✔
- Nenhum item ATIVADO pendente sem encaminhamento. **PASS.**

---

## 10. Achados desta verificação (não-bloqueantes → Revisor/Andraus)

| ID | Achado | Severidade | Encaminhamento |
|---|---|---|---|
| CK-01 | L-001-b (fronteira spec-time vs runtime de "policy versionada") | [DECISÃO NECESSÁRIA] | Andraus decide o alcance de L-001 |
| CK-02 | K-DRIFT-GEH-01 — "GEH-001 §6" rotulado "Herança Vertical" ≠ título real do §6 | Menor (INFERÊNCIA resolvida) | Controlador confirma/ajusta a referência no ROADMAP/EUA-E17 |
| CK-03 | D9 auditoria apenas por referência (não fechada) | Menor | Consistente com alvo D0–D8; D9 pertence a SPEC-041 |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs, EARS, Enforcement, Constitution Check, Herança/Delta, CONS-01 e gate RMR-001 satisfeitos. 3 achados não-bloqueantes (CK-01..CK-03) encaminhados.

> Este resultado é **feedback interno de verificação de spec** — NÃO é o parecer do Revisor (GRE-001/HRE-001) nem homologação de Andraus. Próximo passo: submissão ao Revisor SOT.
