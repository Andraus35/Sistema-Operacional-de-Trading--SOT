# EUA-E20 — FASE RISK: slots-macro indicativos da família RISK-SPEC (PROPOSTA)

| Campo | Valor |
|---|---|
| Código | **EUA-E20** (reservada para a FASE RISK — confirmado, ver §0) |
| Tipo | Emenda de Arquitetura de Especificação — **PROPOSTA** (não aplica slots; não autoriza a família; não fecha decisão) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-01 |
| Status | **PROPOSTA — aguarda parecer do Revisor e homologação de Andraus** |
| Origem | Instrução direta de Andraus (chat, 2026-10-01): a família RISK-SPEC não tem slots numerados no ROADMAP; FASE RISK reservada/futura (EUA-E20); BL-018 guarda 23 RISK-SPEC |
| Autoridade-fonte | `backlog/BL-018-RISK-AGENT-backlog.md`; `reference/SOT-RISK-MASTER-001_Consolidado.md` §3.6/§6.2; `governance/DHR-EUA-E19a_...md`; `ROADMAP.md`; RULE-ECC-01/02 |
| Não fecha | Nenhuma decisão aberta (CONS-01). Não numera/autoriza a família. Não edita `WORKFLOW.md`. |

---

## 0. Confirmação do código EUA

[FONTE: `governance/DHR-EUA-E22_...md` §76 — *"EUA-E20 (FASE RISK) ... permanecem reservadas"*; `ROADMAP.md` §219 e `AUDITORIA-ADIANTAMENTO-SLOTS...md` l.111/l.239 associam a autorização da família RISK à **EUA-E20**.] → **EUA-E20 é o código correto** para esta proposta.

---

## 1. Problema

A família **RISK-SPEC** (Risk Agent, BL-018) está descrita como **23 Specs em 8 Grupos** em `reference/SOT-RISK-MASTER-001_Consolidado.md` §6.2, mas **não tem slots numerados no ROADMAP** (contingente à EUA-E20). [FONTE: BL-018 §Família de Specs; MATRIZ §IDs sem dona clara "WF-07/WF-P01/WF-X01..X03".]

Enumerar **23 slots** antecipadamente **contraria o princípio da Especificação Emergente** (RULE-ECC-01: o ROADMAP não pré-determina quantidade/numeração; slots só se fixam na abertura, com Dossiê). [FONTE: `governance/RULES.md` RULE-ECC-01 l.433-437; ROADMAP banner EUA-E21.] A melhor prática ao repo é propor **poucos SLOTS-MACRO indicativos**, agrupando os 23 por coesão, preservando a rastreabilidade de cada RISK-SPEC e dos invariantes/decisões abertas.

---

## 2. Proposta — 6 slots-macro indicativos (+ Skills diferidas)

> **Natureza:** indicativos (RULE-ECC-01). Número, fronteira e decomposição de cada macro-slot só se fixam na **abertura**, por Dossiê (RULE-ECC-02) + homologação. Os 23 RISK-SPEC do Master são **expectativa de cobertura**, não atribuição baselined. Pré-condição de toda a FASE RISK: **EUA-E19a homologada** (✓, DHR-EUA-E19a) + **milestone FASE 6/Synthesis concluída** (pendente — gatilho de BL-018).

| Slot-macro (indicativo) | Agrupa (Master §6.2) | Coesão | RISK-SPEC mapeados |
|---|---|---|---|
| **RISK-M1 — Fundamento & Cognição de Risco** | Grupos A + B | Princípios + disciplinas epistêmicas/causais/incerteza de risco (herdam N8–N17 via RULE-HV) | RISK-SPEC-001 (Princípios RP1–RP15), 002 (Epistemologia), 003 (Ontologia), 004 (Semântica), 005 (Inquérito), 006 (Causalidade), 007 (Contrafactuais), 008 (Incerteza), 009 (Probabilística) |
| **RISK-M2 — Decisão sob Risco & Risco-Retorno** | Grupo C | Autoridade ACCEPT/WAIT/REJECT/ABSTAIN + deltas genuínos (R:R, exposição, risco de modelo) | **RISK-SPEC-010 (Decisão sob Risco — fecha `RISK-CONV-001`)**, 011 (Risco-Retorno — consolida R:R≥1:3 + institui Heat≤15% + alavancagem), 012 (Exposição e Capital), 013 (Risco de Modelo) |
| **RISK-M3 — Quantificação & Stress** | Grupo D | Toolbox quantitativo determinístico + simulação + calibração | RISK-SPEC-014 (VaR/CVaR/drawdown/correlação), 015 (Stress/Monte Carlo/bootstrap), 016 (Calibração — Brier/log-loss) |
| **RISK-M4 — Memória, Aprendizado & Metacognição de Risco** | Grupo E | Memória de risco + aprendizado (qualidade≠resultado) + metacognição (N17) | RISK-SPEC-017 (Memória), 018 (Aprendizado), 019 (Metacognição) |
| **RISK-M5 — Operacionalização: Risk Harness, RDR & Signal Package** | Grupo F | Gate E3 + objeto de decisão + contrato de fronteira | **RISK-SPEC-020 (Risk Harness — gate E3; cláusula "via Risk Harness" entra em P14/INV-05 aqui)**, 021 (Risk Decision Record — depende CDM-001), **RISK-SPEC-022 (Signal Package — contrato D-RISK-SP-001)** |
| **RISK-M6 — Avaliação & Adversarial de Risco** | Grupo H | Avaliação do próprio Risk Agent; **herda SPEC-020 núcleo A via RULE-HV** | RISK-SPEC-023 |
| **(diferido) RISK-Skills** | Grupo G | Skills de risco | diferidas a **I-001** (FECHADA, DHR-I001-001 — híbrido por Classe) / SPEC-025 |

**Cobertura:** os 23 RISK-SPEC do Master mapeiam integralmente a RISK-M1..M6 (+ Skills diferidas) — nenhuma capacidade descartada (restrição de cobertura, RULE-ECC-01 item 4).

**Preservações exigidas pela instrução de Andraus (✓):** RISK-SPEC-010 (fecha RISK-CONV-001) → RISK-M2; RISK-SPEC-020 (cláusula "via Risk Harness" em P14/INV-05) → RISK-M5; RISK-SPEC-022 (Signal Package) → RISK-M5; **SPEC-016/TMP** permanece slot do ROADMAP (FASE 6, repurposada — TMP interno Synthesis→Risk), **não** absorvido pela família RISK, mas **ancora INV-RISK-00** junto de RISK-M5.

---

## 3. Posição no caminho crítico

```
... FASE 6 (Synthesis/Mission/TMP) concluída → [FASE RISK] RISK-M1 → RISK-M2 → RISK-M3 → RISK-M4 → RISK-M5 → RISK-M6
```
A FASE RISK posiciona-se **após a FASE 6** (sem conflito com a FASE GOV já fixa — F-07/BL-018). [FONTE: BL-018 §F-07; ROADMAP §21.] Depende do **Manager** (WF-06/WF-07) e dos insumos de risco **WF-X01..X04** e **WF-P01** (Portfolio Heat com correlação). [FONTE: `docs/MATRIZ-WORKFLOW-SPEC.md` §8/§7 — WF-07/WF-P01/WF-X01..X03 apontam para a família RISK como "dona a numerar na EUA-E20".]

**Pré-condição dura:** **INV-RISK-00 (isolamento epistêmico)** — verificado por RISK-M5 (Risk Harness) antes de qualquer autorização de Signal Package; input só via handoff tipado imutável do TMP (SPEC-016). [FONTE: BL-018 INV-RISK-00; Master §3.6.]

---

## 4. Invariantes e decisões abertas incidentes (CONS-01 — nenhuma fechada aqui)

**Invariantes de risco (origem EUA-E19a; a serem especializados na família):**
- **INV-RISK-RR** — R:R mínimo 1:3 (risco:retorno = 3:1 retorno:risco); piso soberano (WF-X01). → RISK-M2 (RISK-SPEC-011).
- **INV-RISK-HEAT** — Portfolio Heat ≤ 15% medido com correlação (WF-P01). → RISK-M2 (RISK-SPEC-011/012).
- **INV-RISK-LEV** — alavancagem dinâmica como invariante. → RISK-M2 (RISK-SPEC-011/012).
- **INV-RISK-00** — isolamento epistêmico (pré-condição). → RISK-M5 + SPEC-016.
[FONTE: AGENTS.md §6.9 / EUA-E19a; MEMORY risk-agent-bl018-eua-e19a; Master §3.6 INV-RISK-00..12.]

**Decisões abertas a vigiar (não fechar sem Andraus):**
- **RISK-ARR-LOC-001** (localização/escopo da absorção do ARR — "fantasma" no repo, F-01) — **permanece ABERTA**; a EUA-E19a **não** a fechou. A família **consolida** RULES de R:R existentes, **sem** linguagem de supersedação do ARR enquanto aberta.
- **RISK-CONV-001** ("convicção de risco" × Conviction Vector 8D/J-001) — fecha em **RISK-SPEC-010 (RISK-M2)**, **não antes de J-001**.
- **J-001** (fórmula/pesos/limiares definitivos do Conviction Vector) — trava RISK-SPEC-009/010; a FASE RISK não o fecha.
- **D-RISK-SP-001** (contrato exato do Signal Package) — diferida a RISK-SPEC-022 (RISK-M5).
- **CDM-001** (idioma canônico do RDR) — pendente; trava RISK-SPEC-021 (RISK-M5).
[FONTE: BL-018 §Decisões abertas; Master §ref; ROADMAP §32.]

---

## 5. O que muda se homologada (não aplicado agora)

- **ROADMAP:** inserção de uma **FASE RISK** após a FASE 6 com os 6 slots-macro **indicativos** RISK-M1..M6 (+ linha de Skills diferidas); **sem** enumerar os 23 (RULE-ECC-01). Cada macro-slot abre com Dossiê (RULE-ECC-02) que então propõe sua decomposição fina (pode dividir/fundir/renumerar — INV-07).
- **§26 (capacidades exigidas):** acréscimo das capacidades de risco como restrição de cobertura (nenhuma capacidade de BL-018 descartada em silêncio).
- **BL-018:** permanece a fonte rica; Estado segue `Em espera` até `milestone:FASE 6 concluída` (2ª condição do gatilho composto). Re-apontamento: a "dona" de WF-07/WF-P01/WF-X01..X03 passa dos "sem dona clara" para os macro-slots RISK-M2/M5 na abertura.
- **CONSTITUTION P14 / INV-05:** cláusula "via Risk Harness" entra **apenas** quando **RISK-SPEC-020 (RISK-M5)** for homologada (já previsto por EUA-E19a/C-03) — não nesta proposta.
- **RMR-001:** gatilhos de ativação dos macro-slots a definir na autorização da família.

---

## 6. Recomendação

**Recomendo adotar os 6 slots-macro indicativos (RISK-M1..M6) + linha de Skills diferidas, em vez de 23 slots numerados.** O agrupamento por coesão (fundamento/cognição · decisão/risco-retorno · quantificação · memória/metacognição · operacionalização · avaliação) honra a RULE-ECC-01 (não pré-determinar quantidade), preserva integralmente a cobertura dos 23 RISK-SPEC e os pontos obrigatórios (RISK-SPEC-010/020/022, SPEC-016/TMP, INV-RISK-RR/HEAT/LEV, INV-RISK-00), e mantém abertas J-001/RISK-CONV-001/RISK-ARR-LOC-001/D-RISK-SP-001/CDM-001. A decomposição fina de cada macro-slot fica para a abertura, com Dossiê — que é exatamente onde o método manda decidir número e fronteira. **A FASE RISK permanece não-autorizada até homologação de Andraus** (pré-condição: milestone FASE 6).

---

## 7. Não-objetivos (CONS-01)

Esta proposta **não** autoriza/numera a família RISK, **não** fecha nenhuma decisão aberta (RISK-ARR-LOC-001, RISK-CONV-001, J-001, D-RISK-SP-001, CDM-001), **não** antecipa a FASE 6, **não** introduz a cláusula "via Risk Harness" em P14/INV-05, **não** renumera nem apaga slots existentes (SPEC-016 preservada), e **não** edita o `WORKFLOW.md`. Tudo depende de homologação de Andraus.

---

*EUA-E20 — PROPOSTA. Produzida pelo Especificador (Claude Code) por instrução direta de Andraus, 2026-10-01. Aguarda Revisor + Andraus.*
