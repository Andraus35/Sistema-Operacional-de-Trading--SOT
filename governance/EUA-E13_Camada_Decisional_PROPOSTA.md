# EUA-E13 — Camada Decisional: RULE-DEC (decisão≠execução+autoridade · condicional/INDETERMINADO · processo≠resultado) + nó N16 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E13** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N16 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-21; ata `DHR-EUA-E13`). Vigência imediata; incorporação da seção RULE-DEC ao `RULES.md` diferida ao piloto SPEC-002 (v1.5), junto com EUA-E04..E12. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-21 |
| Alvo | `RULES.md` (+RULE-DEC, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada Decisional (`CAMADA DECISIONAL.MD` — MDC-001) §52, §53, §54, §63, §64, §65, §66 — importadas só decisão≠execução+autoridade, decisão condicional e processo≠resultado |
| Fundamento no baseline | **INV-05** (SOT produz TMP, não executa — atomic-spec §… l.336); **P14** (SOT nunca executa ordens diretamente — CONSTITUTION); **B-001 fechada** (Synthesis Agent = árbitro/TMP); Andraus = autoridade homologadora; INDETERMINADO (EUA-E05); RULE-CTF-03/INV-02 (invalidação — EUA-E10); RULE-UNC/PB-10 (incerteza — EUA-E11); RULE-CAU-03/AP-10 (anti pós-hoc — EUA-E09); MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade + blindagem do invariante mais importante do SOT.** A *modelagem* de decisão (multicritério, utilidade, opcionalidade, risco) **é** o CDM-001 (Canonical Decision Model, pendente) + Synthesis Agent. Esta emenda importa só três disciplinas de spec-time; todo o resto difere ao CDM-001/Synthesis (decisão) e à Metacognição (vieses). |

---

## 1. Justificativa `[INFERÊNCIA]`

O ponto central da Camada Decisional — **decisão ≠ execução** e **autoridade decisional** (§52/§53/§54) — já é o invariante mais forte do SOT (**INV-05**, **P14**, Synthesis como árbitro/TMP, Andraus como homologador). A substância de *modelagem* de decisão (multicritério §32, utilidade/pesos §74, opcionalidade §68/§69, risco §46) **é o CDM-001 / Synthesis Agent** e é diferida para lá. Os vieses/metacognição (§58/§59) pertencem ao nó futuro **Metacognição**. O delta real de spec-time da MDC-001 são **três disciplinas** genéricas, todas de baixo risco e alto valor de blindagem: (1) toda saída decisional declara que produz **recomendação/TMP, não execução**, e sob **qual autoridade**; (2) sob informação faltante, produzir **decisão condicional** (incl. ramo `desconhecido → INDETERMINADO`) em vez de forçar decisão única; (3) separar **qualidade do processo** da **qualidade do resultado** (anti-hindsight decisório). Esta emenda integra só isso, por referência.

Esta é a **última camada com documento** do §68: após a Decisional, resta apenas **Metacognição (sem documento no repo)**.

---

## 2. Classificação do MDC-001 (Q1) `[DECISÃO — a homologar]`

**MDC-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/MCF/MUN/MPB/GEH). Importadas só decisão≠execução+autoridade (§52/§53/§54), decisão condicional (§63/§66) e processo≠resultado (§64/§65).

**Não adotar — por DUPLICAÇÃO com o baseline:**

| Do MDC-001 | Já coberto por |
|---|---|
| §27 decisão ≠ previsão | RULE-UNC/PB-10 + RULE-EPI (afirmação ≠ certeza; previsão incerta ainda apoia decisão) |
| §28 decisão ≠ causalidade | **RULE-CAU** (EUA-E09) |
| §40/§41 contrafactuais decisórios / cenários | **RULE-CTF** (EUA-E10) |
| §18/§19 decisão sob incerteza vs risco | **RULE-UNC** (EUA-E11) + PB-10 + INDETERMINADO |
| §50 invalidação | **RULE-CTF-03 / INV-02** (invalidador Elliott-ICT) |
| §14/§15/§16/§17 valor/suficiência/parada de informação | **RULE-INQ** (EUA-E08, critério de encerramento → INDETERMINADO) |
| §55/§56/§57 explicabilidade/rastreabilidade decisional | TRACE-06 + RULE-010 (rastreabilidade da convicção) + PB-05..07 |
| §44/§45/§71/§85 proporcionalidade cognitiva | dial GES (PPQ-001), D0–D9, CEE-001 §12 (4Es), CC-05 |
| §5 possibilidade/probabilidade | RULE-PRB (EUA-E12) |

**Não adotar — por DIFERIMENTO:**

| Do MDC-001 | Diferido a |
|---|---|
| §30–32 multicritério; §74 pesos/utilidade; §46 risco multidimensional; §67/§68/§69 robustez/sequencial/**opcionalidade**; §20/§21 robustez/sensibilidade | **CDM-001 (Canonical Decision Model, pendente)** + **Synthesis Agent** (árbitro/TMP — B-001) |
| §58/§59/§60 vieses cognitivos e anti-viés | nó futuro **Metacognição** (sem documento) |
| §38/§39 agentes adaptativos/adversarialidade; §36/§37 efeitos de 2ª ordem/externalidades | Modelos Canônicos + specs de domínio (fora do delta de spec-time) |

Sem colisão de rótulos (prefixo **RULE-DEC** inédito; não há `DEC-xx` em uso). Registro **K-MAN-12** no CONFLICT-MAP.

> **Fronteira J-001/CDM-001 (INV-03/CONS-01):** RULE-DEC **não** define função de utilidade, pesos, critérios de comparação, ponderação multicritério nem cálculo de robustez/opcionalidade — tudo isso é CDM-001 (pendente) e Conviction/CCM-001 (J-001 aberto). RULE-DEC-01/02/03 disciplinam apenas a **forma** e a **autoridade** da saída decisional em spec-time, fora do mecanismo canônico de decisão.

---

## 3. Registro do nó N16 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2 (preenche o §68 "Decisional"; fecha o ciclo de camadas com documento):

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N16 — Decisional** | INV-05 + EUA-E13 | Decisão ≠ execução + autoridade declarada; decisão condicional (→ INDETERMINADO); qualidade do processo ≠ resultado. **Modelagem decisional (multicritério/utilidade/opcionalidade/robustez) → CDM-001 (pendente) + Synthesis Agent**; vieses → Metacognição | `atomic-spec.md` |

**Interface (MAN-001 §3):** Fornece — disciplina de forma decisional (recomendação/TMP≠execução; autoridade explícita; ramo condicional/INDETERMINADO; processo≠resultado). Recebe — INV-05/P14 (N1), Synthesis/B-001, RULE-UNC/INDETERMINADO (N14/N8), RULE-CTF/invalidação (N13/INV-02), RULE-CAU-03 (N12), RULE-INQ (N11), RULE-PRB (N15). Compartilha — "SOT produz TMP, não executa"; anti-hindsight; incerteza preservada. Converge com — N1, N8, N11, N12, N13, N14, N15; **interface com CDM-001 (pendente), Synthesis Agent e o nó futuro Metacognição**. Referência externa: MDC-001.

**Camadas futuras restantes (§68):** ~~Decisional (→ N16)~~ · **Metacognição** *(sem documento no repo)* — único nó restante.

---

## 4. Regras propostas (RULE-DEC) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras Decisionais (RULE-DEC)", após RULE-PRB, com `[Fonte: EUA-E13]`.

| ID | Regra |
|---|---|
| **RULE-DEC-01** | Toda saída decisional material DEVE declarar que produz **recomendação/orientação decisional (TMP), não execução**, e sob **qual autoridade** ela é emitida (o SOT recomenda; a execução e a decisão final permanecem na camada/autoridade competente — Andraus/humano). **Reforça e referencia INV-05, P14 e a topologia Synthesis/B-001 — não os redefine.** Confundir recomendação com autoridade, ou apresentar análise como ação automática, é achado. |
| **RULE-DEC-02** | Sob informação faltante ou preferência não disponível, o LLM DEVE poder produzir **decisão condicional** — `se X → A / se ¬X → B / se X permanecer desconhecido → INDETERMINADO/HOLD` — em vez de fabricar uma decisão única ou inventar a preferência ausente. Estende INDETERMINADO (EUA-E05) e RULE-UNC (EUA-E11) ao plano decisional. |
| **RULE-DEC-03** | **Qualidade do processo decisional ≠ qualidade do resultado.** Uma decisão bem fundamentada pode produzir resultado ruim e vice-versa; a avaliação retrospectiva NÃO DEVE julgar o processo apenas pelo resultado (anti-hindsight). Estende RULE-CAU-03/AP-10; crítico para avaliação de backtest e revisão de sinais. |

**Verificação:** reusa **CC-09** (status epistemológico / disciplina de forma). **Sem novo item de Constitution Check.**

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-DEC ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E12.
- **Diferidos ao CDM-001 (pendente) / Synthesis Agent:** multicritério, função de utilidade/pesos, robustez, sensibilidade, valor da opcionalidade, decisão sequencial, risco multidimensional.
- **Vieses/metacognição** → nó futuro **Metacognição**; **agentes adaptativos/externalidades/2ª ordem** → Modelos Canônicos + specs de domínio.

---

## 6. Non-goals `[FONTE]`

- Não recria decisão≠previsão/causalidade/incerteza/invalidação (= RULE-UNC/EPI/CAU/CTF), valor da informação (= RULE-INQ), proporcionalidade (= GES/D0–D9/4Es) nem rastreabilidade (= TRACE-06/RULE-010).
- **Não define modelo de decisão** — função de utilidade, pesos, critérios de comparação, robustez, opcionalidade (→ CDM-001 pendente / Synthesis; INV-03/J-001 aberto — CONS-01).
- Não importa vieses (→ Metacognição) nem efeitos de 2ª ordem/adversarialidade (→ Modelos Canônicos).
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4, nem a topologia de 3 componentes (Fusion→Conviction→Synthesis).

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MDC-001 = referência externa não-normativa | **Sim** |
| Q2 | Nó **N16 (Decisional)** no MAN-001 (fecha as camadas §68 com documento) | **Sim** |
| Q3 | RULE-DEC-01/02/03 (decisão≠execução+autoridade; condicional/INDETERMINADO; processo≠resultado), sob CC-09 | **Sim** |
| Q4 | Diferir ao CDM-001/Synthesis: multicritério/utilidade/robustez/opcionalidade/risco; vieses → Metacognição; 2ª ordem/adversarialidade → Modelos Canônicos | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E12) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md v1.1, INV-05/P14, B-001/Synthesis,
        RULE-UNC/EPI/CAU/CTF/INQ, CDM-001/J-001, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia + Inquérito + Causal +
        Contrafactual + Incerteza + Probabilística + Decisional)
   ↓
Controlador incorpora à v1.5 + seção RULE-DEC no RULES.md + N16 no MAN-001 + classifica MDC-001 (K-MAN-12)
```

---

*PROPOSTA não-homologada. Emenda enxuta por proporcionalidade. Reforça INV-05/P14 — NÃO os redefine; NÃO define modelo de decisão (CDM-001 pendente / J-001 aberto). Incorporação à v1.5 diferida ao piloto SPEC-002. Última camada com documento; após ela resta só a Metacognição.*

---

## Anexo A — Autopré-check do Especificador (2026-09-21)

- [x] Etiquetagem TRACE-06 aplicada; status epistemológico = PROPOSTA (CONS-01: nenhum item aberto declarado como fechado).
- [x] Fronteira J-001/CDM-001 preservada — RULE-DEC não define utilidade/pesos/critérios/robustez/opcionalidade.
- [x] RULE-DEC-01 **reforça e referencia** INV-05/P14/B-001 — não redefine invariante (conflito D-01 tratado).
- [x] Sem colisão de rótulos (RULE-DEC inédito); K-MAN-12 registrado no CONFLICT-MAP.
- [x] Sem novo Constitution Check (reusa CC-09); não altera 4Es/E0–E3/F.1–F.4/Quality Gates/topologia de 3 componentes.
- [x] Diferimentos explícitos (CDM-001/Synthesis; Metacognição; Modelos Canônicos) — proporcionalidade.
- [x] Ancoragem verificada contra `CAMADA DECISIONAL.MD` (§52 l.951-961; §53 l.965-975; §54 l.979-990; §63 l.1135-1141; §64 l.1145-1169; §65 l.1173-1185; §66 l.1189-1203).

## Anexo B — Parecer do Revisor SOT (2026-09-21)

**Veredito: CONFORME** — todos os 8 passos PASS; **fronteira J-001/CDM-001 preservada**; INV-05/P14/B-001 reforçados sem redefinição; CONS-01 respeitado; consistência de método com EUA-E04..E12 verificada. Acesso ao `RULES.md` v1.1 confirmado (regra M-02).

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (INV-05 l.336, CC-01..07, §11 TRACE-06/CC-09, J-001/INV-03, B-001 fechada) · CONSTITUTION v1.1 (P14, Synthesis árbitro) · MAN-001 (homologado, N1..N15) · CONFLICT-MAP v1.1 (K-MAN-01..11) · EUA-E11/E12 (homologadas) · CAMADA DECISIONAL.MD (MDC-001, ref. externa).

**Resumo dos pontos críticos:** (1) Fronteira — §2/§6 diferem multicritério/utilidade/pesos/robustez/opcionalidade ao CDM-001/Synthesis; J-001 aberto; CONS-01 OK — PASS; (2) D-01 — RULE-DEC-01 reforça/referencia INV-05/P14/B-001 sem redefinir — PASS; (3) os 9 mapeamentos de duplicação conferem com o baseline — PASS; (4) 3 regras verificáveis, estendem sem duplicar, reusam CC-09 — PASS; (5) nó N16 com formato/interfaces idênticos a N8..N15, §68 atualizado (resta só Metacognição) — PASS; (6) RULE-DEC inédito, K-MAN-12 válido — PASS; (7) âncoras de linha do Anexo A conferem com CAMADA DECISIONAL.MD — PASS.

**Achados:**

| ID | Severidade | Constatação | Tratamento |
|---|---|---|---|
| A-01 | **Menor** | K-MAN-12 citado como registro no CONFLICT-MAP, ainda não efetivado | Registro pelo **Controlador** na efetivação (padrão K-MAN-10/11). Não bloqueia. |

Nenhum achado Crítico ou Médio.

**Recomendação do Revisor (Q1–Q5):** concorda com todas. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
