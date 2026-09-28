# EUA-E10 — Camada Contrafactual: RULE-CTF (baseline + intervenção mínima + anti-hindsight) + nó N13 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E10** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N13 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E10`). Vigência imediata; incorporação da seção RULE-CTF ao RULES.md diferida ao piloto SPEC-002 (Q5), junto com EUA-E04..E09. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `RULES.md` (+RULE-CTF, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada Contrafactual (`CAMADA CONFRACTUAL.MD` — MCF-001) §3, §13, §14, §20, §25 — importadas só baseline/intervenção mínima/anti-hindsight, gradação da consequência e contrafactual de invalidação. **Recebe o diferimento da EUA-E09** (§28/§58 do MCC: observar-vs-intervir / intervenção hipotética). |
| Fundamento no baseline | RULE-CAU-03 (guard pós-hoc — EUA-E09); RULE-EPI (contrafactual≠fato — EUA-E05); PCO-01/02; invalidador (INV-02/ICT, CONFLICT-MAP); TRACE-06; CEE-001/GES; MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade.** Anti-hindsight já é RULE-CAU-03; alternativas já são PCO. Importa-se só a disciplina contrafactual, muito aderente ao **backtest**. |

---

## 1. Justificativa `[INFERÊNCIA]`

O anti-hindsight (RULE-CAU-03/AP-10), o "contrafactual≠fato" (RULE-EPI) e as alternativas concorrentes (PCO-01) já estão homologados. O delta real da Camada Contrafactual é a **disciplina de raciocínio contrafactual** — declarar baseline, alterar só a premissa indicada, não vazar o resultado conhecido — diretamente aplicável ao **backtest** e à análise de invalidação (invalidador é conceito central do SOT). Esta emenda integra só isso, por referência.

---

## 2. Classificação do MCF-001 (Q1) `[DECISÃO — a homologar]`

**MCF-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/GEH). Importadas só baseline/intervenção mínima/anti-hindsight (§3/§13/§20), gradação da consequência (§14) e contrafactual de invalidação (§25/§38). **Não adotar por duplicação/diferimento:** §20/§57 anti-hindsight (= RULE-CAU-03); §31/§32 qualificação por incerteza/probabilidade (→ nós futuros **Incerteza**/**Probabilística**); §16–18 propagação/árvores profundas (→ specs de backtest/simulação). Sem colisão de rótulos. Registro K-MAN-09 no CONFLICT-MAP.

---

## 3. Registro do nó N13 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2 (preenche o §68 "Contrafactuais"):

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N13 — Contrafactual** | RULE-CAU-03 + EUA-E10 | Mundos alternativos condicionados: baseline; intervenção mínima; anti-hindsight; invalidação. Qualificação probabilística e árvores diferidas | `atomic-spec.md` |

**Interface (MAN-001 §3):** Fornece — disciplina contrafactual (baseline, intervenção mínima, invalidação). Recebe — mecanismo/regime (N12), RULE-EPI (N8), questão→método (N11). Compartilha — "contrafactual ≠ fato". Converge com — N12, N8, N11. Referência externa: MCF-001.

**Camadas futuras restantes (§68):** Incerteza · Probabilística · Decisional · Metacognição — **todas ainda sem emenda; Metacognição sem documento no repo** até o momento (Incerteza/Probabilística/Decisional têm doc, aguardam processamento).

---

## 4. Regras propostas (RULE-CTF) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras Contrafactuais (RULE-CTF)", após RULE-CAU, com `[Fonte: EUA-E10]`.

| ID | Regra |
|---|---|
| **RULE-CTF-01** | Todo raciocínio contrafactual/backtest DEVE declarar o **baseline** (mundo de referência), alterar **apenas a premissa indicada** (intervenção mínima) e **não usar o resultado conhecido** como premissa (anti-hindsight). Estende RULE-CAU-03; não cria regra paralela. |
| **RULE-CTF-02** | Contrafactual é **condicional**: NÃO DEVE ser apresentado como fato nem convertido em previsão. Consequências DEVEM ser graduadas (necessária / plausível / possível / especulativa), coerente com TRACE-06 e RULE-EPI. |
| **RULE-CTF-03** | Contrafactual de **invalidação** ("que alteração mínima invalida esta leitura?") DEVE conectar-se ao **invalidador** declarado da hipótese (INV-02/Elliott-ICT), não a um invalidador ad hoc. |

**Verificação:** reusa **CC-09** (status epistemológico) e o dial GES (profundidade proporcional). **Sem novo item de Constitution Check.**

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-CTF ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E09.
- **Qualificação por incerteza/probabilidade** (§31/§32) → nós futuros **Incerteza**/**Probabilística** (docs já no repo).
- **Propagação/árvores/simulação** (§16–18) → specs de **backtest** (Fase Piloto), não emenda.

---

## 6. Non-goals `[FONTE]`

- Não recria anti-hindsight (§20/§57 = RULE-CAU-03) nem "contrafactual≠fato" (= RULE-EPI).
- Não importa qualificação probabilística (§31/§32) nem árvores profundas (§16–18) — diferidos.
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.
- Não adota as demais camadas futuras (§68).

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MCF-001 = referência externa | **Sim** |
| Q2 | Nó **N13 (Contrafactual)** no MAN-001 | **Sim** |
| Q3 | RULE-CTF-01..03 (baseline/intervenção mínima/anti-hindsight; condicional+gradação; invalidação), sob CC-09 | **Sim** |
| Q4 | Qualificação probabilística e árvores diferidas (nós Incerteza/Probabilística + backtest) | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E09) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md, RULE-CAU-03/RULE-EPI, PCO, invalidador, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia + Inquérito + Causal + Contrafactual)
   ↓
Controlador incorpora à v1.5 + seção RULE-CTF no RULES.md + N13 no MAN-001 + classifica MCF-001
```

---

*HOMOLOGADA (DHR-EUA-E10, 2026-09-20). Emenda enxuta por proporcionalidade. Incorporação à v1.5 diferida ao piloto SPEC-002.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios; proporcionalidade verificada. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (CC-09, RULE-EPI, RULE-CAU-03, INV-02) · GPR-001 v1.0 (PCO-01/02, AP-10) · CONFLICT-MAP (K-MAN-08) · MAN-001 v1.0 · MCF-001 (ref. externa).

**Resumo:** (Q1) proporcionalidade — não recria anti-hindsight (=RULE-CAU-03) nem contrafactual≠fato (=RULE-EPI); difere qualificação probabilística (nós Incerteza/Probabilística) e árvores (backtest); sem novo CC — PASS; (Q2) RULE-CTF-01 estende RULE-CAU-03, CTF-02 alinha TRACE-06, CTF-03 usa invalidador INV-02 sem redefinir PC-01 — PASS; (Q3) acolhe diferimento da EUA-E09 (§28/§58) — PASS; (Q4) nó N13 coerente (N12/N8/N11) — PASS; (Q5) escopo híbrido + v1.5 — PASS; TRACE-06/CONS-01 — PASS.

**Achado Menor e tratamento:**

| ID | Achado | Tratamento |
|---|---|---|
| A-01 | "esta última sem documento" sugeria só Metacognição; as quatro restantes ainda sem emenda | **Acatado** — nota corrigida (§3) |

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
