# SPEC-038 — Trading Analysis Tool Harness (Checks — verificação de spec)

| Campo | Valor |
|---|---|
| Artefato verificado | `specs/features/SPEC-038/plan.md` (v1.0 candidato) |
| Natureza | **Verificação de SPEC** na fase spec-first (BASpec/EARS/Enforcement bem-formados; rastreabilidade; casos adversariais). **NÃO** é teste de runtime nem BUILD/VERIFY-de-código (ROADMAP §22). |
| Método | atomic-spec.md v1.5 §6 (CHECKS); overlay GUS-TLC-001 |
| Status epistemológico | Feedback interno do autor. **Não** é parecer CONFORME (Revisor) nem homologação (Andraus). |

> **Lembrete (ENF-03):** o gate determinístico é `python scripts/validate_spec_sot.py specs/features/SPEC-038/plan.md` (o agente raiz o executa). "VERIFY passou" aqui ≠ CONFORME ≠ homologação.

---

## 1. Gate determinístico esperado (validate_spec_sot.py) — autoverificação estrutural

| Check | O que exige | Onde o Plan satisfaz | Esperado |
|---|---|---|---|
| STRUCT-01 Cabeçalho | Complexidade + Profundidade-alvo D<n> | Cabeçalho + restatement em prose ("Complexidade: HIGH. Profundidade-alvo: D0–D7.") | PASS |
| STRUCT-02 Constitution Check | bloco + "Elliott" + Conviction pendente/J-001 | §Constitution Check CC-01 (Elliott) + CC-03 ("Conviction Vector não tocado; J-001 permanece ABERTA") | PASS |
| STRUCT-03 Etiquetagem | ≥1 etiqueta de fonte | [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] em todo o Plan | PASS |
| STRUCT-04 EARS | ≥1 "Quando …, … DEVE" | §Critérios de Aceitação (10 itens EARS) | PASS |
| STRUCT-05 BASpec | QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR | BASpec-TH-001..013 | PASS |
| STRUCT-06 Enforcement | 8 campos se há efeito | EC-TH-01..06 (CAPABILITY/EFFECT/PRECOND/POSTCOND/POLICY/LEVEL/FAILURE-MODE/EVIDENCE) | PASS |
| STRUCT-07 Conviction não fechado | sem limiar 60/75% solto | nenhum limiar de convicção declarado (CC-03) | PASS |
| STRUCT-08 Status epistemológico | ≥1 marcador | FATO NORMATIVO / FATO ARQUITETURAL / [DECISÃO NECESSÁRIA] presentes | PASS |
| STRUCT-09 Profundidade compat | D≤teto(HIGH=7) | D0–D7 (prose) → 7≤7 | PASS |
| STRUCT-10 CONS-01 | decisão aberta não vira invariante | J-001/N-001/M-001/H-001/D-001..D-027 sempre com "ABERTA/pendente/[DECISÃO NECESSÁRIA]" próximo | PASS |
| STRUCT-11 Dossiê | research.md com "Dossiê de Pesquisa" | `research.md` presente (cita RULE-ECC-01/02); seção "Dossiê de Pesquisa" | PASS |

**Ponto de atenção (dúvida de formato honesta — RULE-MET-01):** STRUCT-01 depende de a regex casar "Complexidade"/"Profundidade-alvo"; por isso o Plan traz **tanto a tabela quanto a prose redundante**. Se o gate acusar FAIL em STRUCT-01/09, a causa provável é a forma do cabeçalho — não o conteúdo.

---

## 2. BASpecs bem-formadas (atomic-spec §1 + CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REFERÊNCIA | VERIFICADO POR | CLASSE | ≤1 cond/≤1 comport./≤2 RULES |
|---|---|---|---|---|---|---|---|
| TH-001 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-002 | ✔ | ✔ | ✔ | ✔ | ✔ | D | ✔ |
| TH-003 | ✔ | ✔ | ✔ | ✔ | ✔ | D | ✔ |
| TH-004 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-005 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-006 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-007 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-008 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-009 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-010 | ✔ | ✔ | ✔ | ✔ | ✔ | C | ✔ |
| TH-011 | ✔ | ✔ | ✔ | ✔ | ✔ | D | ✔ |
| TH-012 | ✔ | ✔ | ✔ | ✔ | ✔ | C/D | ✔ (4 sub-ferramentas) |
| TH-013 | ✔ | ✔ | ✔ | ✔ | ✔ | D | ✔ |

**CC-11 (RULE-MECH-01..04):** toda BASpec com efeito declara Classe + critério 4Es; nenhuma Classe H/P usada (sem bounded loop a declarar — mecanismos são determinísticos ou enforcement constitutivo); Classe C sempre em risco alto (E2/E3) — RULE-MECH-02 respeitada (nenhuma Classe C em risco baixo).

---

## 3. EARS bem-formados (rastreabilidade EARS → RULE → BASpec → EC)

| EARS # | RULE | BASpec | EC | ADV |
|---|---|---|---|---|
| 1 (contrato completo) | RULE-TH-001 | TH-001 | EC-TH-01 | ADV-TH-07 |
| 2 (proveniência) | RULE-TH-002 | TH-002/TH-013 | EC-TH-02 | — |
| 3 (barra em formação) | RULE-TH-003 | TH-003 | EC-TH-02 | ADV-TH-01 |
| 4 (fail-closed) | RULE-TH-004 | TH-004 | EC-TH-02 | ADV-TH-01/03 |
| 5 (Observação≠Evidência) | RULE-TH-005 | TH-005 | EC-TH-05 | ADV-TH-02 |
| 6 (gate de confirmação) | RULE-TH-007/008 | TH-007/008/012 | EC-TH-03 | ADV-TH-03 |
| 7 (sem ordem/replay) | RULE-TH-009 | TH-009 | EC-TH-04 | ADV-TH-04 |
| 8 (provider abstrato) | RULE-TH-010 | TH-010 | EC-TH-05 | ADV-TH-05 |
| 9 (timestamp → ISO) | RULE-TH-011 | TH-011 | — (Classe D, E1 implícito) | — |
| 10 (estados da chamada) | RULE-TH-012 | TH-013 | EC-TH-06 | — |
| — (tool poisoning) | RULE-TH-006 | TH-006 | — (marcação; política SPEC-039) | ADV-TH-06 |

Nenhuma BASpec órfã; nenhuma RULE citada inexistente (RULE-TH-* são locais [PROPOSTA]; RULE-MECH/ECC/HD/EPI/MET/UNC/PRB/CAU existem em `governance/RULES.md`; INV-05/06/09 em atomic-spec §13; CEM-001 linhas verificadas).

---

## 4. Enforcement Contracts bem-formados (atomic-spec §10.3/§10.4)

| EC | 8 campos | LEVEL | Mínimos por nível | fail-closed | ENF-07 (falso-DENY) |
|---|---|---|---|---|---|
| EC-TH-01 | ✔ | E2 | PRECOND+POSTCOND+FAILURE-MODE ✔ | ✔ | N/A (E2) |
| EC-TH-02 | ✔ | E2 | ✔ | ✔ | N/A (E2) |
| EC-TH-03 | ✔ | E3 | +POLICY +falso-DENY ✔ | ✔ | declarado (amostral; limiar = gap aberto) |
| EC-TH-04 | ✔ | E3 | +POLICY +nota falso-DENY ✔ | ✔ (absoluto) | N/A justificado (nenhum DENY legítimo) |
| EC-TH-05 | ✔ | E2 | ✔ | ✔ | N/A (E2) |
| EC-TH-06 | ✔ | E1 | CAPABILITY+EFFECT+LEVEL+EVIDENCE ✔ | N/A (E1) | N/A (E1) |

**ENF-02:** nível ≥ piso do tipo — Observação/Skill → E1 mínimo (EC-TH-06 E1); efeito crítico/irreversível → E3 (EC-TH-03/04). Economicidade não rebaixou nenhum nível. **ENF-04:** fail-closed presente em todo efeito crítico irreversível (EC-TH-03/04).

---

## 5. Casos adversariais (D8) — ≥1 negação por BASpec Classe C

| ADV | Nega | Classe C coberta |
|---|---|---|
| ADV-TH-01 | barra em formação como fato | (reforça TH-003 D; e TH-004 C) |
| ADV-TH-02 | promoção direta a Evidência | TH-005 C |
| ADV-TH-03 | efeito sem confirmação | TH-007 C / TH-008 C |
| ADV-TH-04 | ordem/replay_trade | TH-009 C |
| ADV-TH-05 | fonte única TradingView | TH-010 C |
| ADV-TH-06 | saída como instrução | TH-006 C |
| ADV-TH-07 | contrato incompleto admitido | TH-001 C |

Cobertura: TH-001, TH-005, TH-006, TH-007, TH-008, TH-009, TH-010 (todas as Classe C) têm ≥1 caso de negação. TH-004 (C) é coberta por ADV-TH-01/03. **Exigência da entrega satisfeita.**

---

## 6. Constitution Check — verificação cruzada

CC-01..CC-12 preenchidos no Plan; CC-06/CC-07 N/A justificado (não é Engineering Card); CC-12 N/A justificado (tooling agnóstico). CC-08 Herança/Delta presente com INHERITS/ADDED/REMOVED (vazio)/MODIFIED (nenhuma); evidência obrigação-a-obrigação no §7-bis Bloco B. CC-02 confirmado: nenhuma redefinição de CEM-001 (projeção por referência). CC-03/CC-04 confirmam J-001/INV-04 intocados.

**§7-bis (EUA-E18):** Blocos A/B/C/D presentes e preenchidos (obrigatório HIGH). Nenhuma BASpec restou [DECISÃO NECESSÁRIA] por falta de resposta adversarial.

---

## 7. CONS-01 e decisões abertas

- IDs de decisão aberta citados (J-001, N-001, M-001, H-001, D-001..D-027) sempre acompanhados de marcador de pendência no raio do contexto. [verificar no gate STRUCT-10]
- Nenhuma decisão aberta aparece como invariante fechado.
- A emenda à SPEC-020 (BL-017/tool correctness) está como **[PROPOSTA]**, não aplicada; fechamento diferido à homologação (de Andraus).
- WF-D03 não fechada; nenhum WF-xx contrariado (lente 3 do research.md §8).

---

## 8. Dossiê de Pesquisa (RULE-ECC-02/04/05)

- `research.md` presente, com seção "Dossiê de Pesquisa", fontes [EXTERNO] classificadas, capturas em `sources/`, comparação adotar/adaptar/rejeitar/adiar, 3 lentes (RULE-ECC-05). ECC-VAL-001: validade HIGH 90 dias (limite 2026-12-31). O Revisor audita o **processo** do Dossiê, não a veracidade das páginas.

---

## 9. O que este checks NÃO verifica (honestidade — RULE-MET-01)

- **Não** executa código, API, nem valida comportamento em runtime (spec-first — ROADMAP §22).
- **Não** atesta a veracidade das fontes [EXTERNO] nem a conformidade jurídica do canal TradingView (risco assumido por Andraus — fora do mandato).
- **Não** confirma o exit-code real de `validate_spec_sot.py` — a tabela §1 é a *expectativa* do autor; o agente raiz roda o gate. Se divergir, o achado é do gate/Revisor.
- **Não** fecha nenhuma decisão aberta (J-001/N-001/M-001/H-001/DATASRC provedor de máquina).
- **Não** valida os números do tutorial-Pine (buy_hold_return, in_2/in_4, janela treino/teste) — marcados [INFERÊNCIA]/INDETERMINADO.

**Verificação de spec concluída (feedback interno). Pronto para revisão.**
