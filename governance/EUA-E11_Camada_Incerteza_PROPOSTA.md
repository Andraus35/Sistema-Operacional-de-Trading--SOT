# EUA-E11 — Camada de Incerteza: RULE-UNC (localizar/tipificar + não-contaminação + incerteza≠probabilidade) + nó N14 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E11** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N14 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E11`). Vigência imediata; incorporação da seção RULE-UNC ao RULES.md diferida ao piloto SPEC-002 (Q5), junto com EUA-E04..E10. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `RULES.md` (+RULE-UNC, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada de Incerteza (`CAMADA INCERTEZA.MD` — MUN-001) §5, §15, §18, §30–31 — importadas só localização/tipificação, não-contaminação e incerteza≠probabilidade |
| Fundamento no baseline | PB-10 (preservação da incerteza); INDETERMINADO (EUA-E05); INV-EPI-03/04/08; PCO-01/04; RULE-EPI (falsa precisão); Conviction Vector (INV-03/J-001 **aberto**); MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade.** Incerteza é núcleo já coberto (PB-10, INDETERMINADO, INV-EPI, PCO, Conviction Vector). Importa-se só o delta; calibração/sensibilidade/quantificação ficam com Conviction/CCM e o nó Probabilística. |

---

## 1. Justificativa `[INFERÊNCIA]`

A incerteza já é núcleo do SOT: PB-10 (preservar), INDETERMINADO (abster), INV-EPI-03/04/08 (confiança≠evidência; declarar incerteza/desconhecimento), PCO-01/04 (hipóteses concorrentes/atualização) e o Conviction Vector (representação multidimensional). O delta real da MUN-001 são **três disciplinas** ainda não formalizadas: **localizar/tipificar** a incerteza (§5/§15), **não deixá-la contaminar o todo** (§18) e **não convertê-la em probabilidade sem base** (§30/§31). Esta emenda integra só isso, por referência.

---

## 2. Classificação do MUN-001 (Q1) `[DECISÃO — a homologar]`

**MUN-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/MCF/GEH). Importadas só localização/tipificação (§5/§15), não-contaminação (§18) e incerteza≠probabilidade (§30/§31). **Não adotar por duplicação/diferimento:** §1/§6/§20 preservar incerteza/abstenção/hipóteses concorrentes (= PB-10/INDETERMINADO/PCO); §47 falsa precisão (= RULE-EPI); §10/§36/§37/§38 calibração/sensibilidade/incerteza crítica (→ **Conviction Engine/CCM-001**, respeitando J-001 aberto); quantificação probabilística (§31/§58) (→ nó futuro **Probabilística**). Sem colisão de rótulos. Registro K-MAN-10 no CONFLICT-MAP.

---

## 3. Registro do nó N14 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2 (preenche o §68 "Incerteza"):

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N14 — Incerteza** | PB-10 + EUA-E11 | Localizar/tipificar a incerteza; não-contaminação; incerteza≠probabilidade. Calibração/sensibilidade → Conviction/CCM; quantificação → Probabilística | `atomic-spec.md` |

**Interface (MAN-001 §3):** Fornece — disciplina de incerteza (localização, tipo, fronteira com probabilidade). Recebe — RULE-EPI/INDETERMINADO (N8), regime/mecanismo (N12), contrafactual (N13). Compartilha — "confiança ≠ verdade". Converge com — N8, N12, N13; **interface com Conviction Engine (J-001 aberto)** e com o nó futuro **Probabilística**. Referência externa: MUN-001.

**Camadas futuras restantes (§68):** Probabilística *(doc)* · Decisional *(doc)* · Metacognição *(sem documento no repo)*.

---

## 4. Regras propostas (RULE-UNC) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras de Incerteza (RULE-UNC)", após RULE-CTF, com `[Fonte: EUA-E11]`.

| ID | Regra |
|---|---|
| **RULE-UNC-01** | Ao declarar incerteza material, a spec DEVE **localizá-la** (onde: dado/modelo/causa/semântica/regime/estrutura/decisão) e **tipificá-la**, em vez de "há incerteza" genérico. Estende PB-10 (preservar → localizar). |
| **RULE-UNC-02** | Incerteza é **localizada**: uma incerteza local NÃO DEVE rebaixar partes bem estabelecidas do raciocínio (nem o inverso — certeza artificial local). Dependências entre incertezas declaradas quando materiais. |
| **RULE-UNC-03** | Incerteza NÃO DEVE ser convertida em probabilidade sem base: "não distingo A de B" ≠ "A e B igualmente prováveis" (anti-falsa-precisão; segue RULE-EPI). Quantificação pertence ao nó Probabilística / Conviction Engine. |

**Verificação:** reusa **CC-09** (status epistemológico). **Sem novo item de Constitution Check.**

> **Fronteira J-001 (INV-03/CONS-01):** RULE-UNC **não** define fórmula, pesos ou limiares do Conviction Vector — esses permanecem em J-001 (aberto). RULE-UNC-03 apenas impede *fabricar* números fora do mecanismo canônico.

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-UNC ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E10.
- **Calibração/sensibilidade/incerteza crítica** (§10/§36/§37/§38) → **Conviction Engine/CCM-001** (SPEC-003), respeitando J-001 aberto.
- **Quantificação probabilística** (§31/§58) → nó futuro **Probabilística**.

---

## 6. Non-goals `[FONTE]`

- Não recria preservação da incerteza/abstenção (= PB-10/INDETERMINADO/PCO) nem falsa precisão (= RULE-EPI).
- Não define fórmula/pesos/limiares do Conviction Vector (J-001 aberto — INV-03/CONS-01).
- Não importa calibração/sensibilidade (→ Conviction/CCM) nem quantificação (→ Probabilística).
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MUN-001 = referência externa | **Sim** |
| Q2 | Nó **N14 (Incerteza)** no MAN-001 | **Sim** |
| Q3 | RULE-UNC-01..03 (localizar/tipificar; não-contaminação; incerteza≠probabilidade), sob CC-09 | **Sim** |
| Q4 | Calibração/sensibilidade → Conviction/CCM (J-001 aberto); quantificação → Probabilística | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E10) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md, PB-10/INV-EPI, PCO, Conviction/J-001, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia + Inquérito + Causal + Contrafactual + Incerteza)
   ↓
Controlador incorpora à v1.5 + seção RULE-UNC no RULES.md + N14 no MAN-001 + classifica MUN-001
```

---

*HOMOLOGADA (DHR-EUA-E11, 2026-09-20). Emenda enxuta por proporcionalidade. Não toca J-001/Conviction. Incorporação à v1.5 diferida ao piloto SPEC-002.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios; **fronteira J-001 verificada** (não fecha/afeta o Conviction Vector). Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (CC-09, RULE-EPI/INDETERMINADO/INV-EPI, INV-03/J-001) · GPR-001 v1.0 (PB-10, PCO-01/04/06, PE-08) · GLOSSARIO (Conviction/J-001) · MAN-001 v1.0 · MUN-001 (ref. externa).

**Resumo:** (Q1) proporcionalidade — RULE-UNC-01 estende PB-10, não recria INDETERMINADO/PCO/RULE-EPI, sem novo CC — PASS; (Q2 crítico) **J-001 permanece aberto** — não define fórmula/pesos/limiares; CONS-01 satisfeito — PASS; (Q3) RULE-UNC-01..03 estendem sem duplicar — PASS; (Q4) diferimentos calibração→Conviction/CCM e quantificação→Probabilística — PASS; (Q5) nó N14 e interfaces corretas — PASS; escopo híbrido + v1.5 + TRACE-06/CONS-01 — PASS.

**Achado Menor:** A-01 (K-MAN-10 registro futuro) — Controlador registra no CONFLICT-MAP na efetivação.

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
