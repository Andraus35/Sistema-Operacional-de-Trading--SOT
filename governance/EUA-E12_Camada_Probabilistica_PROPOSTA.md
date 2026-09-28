# EUA-E12 — Camada Probabilística: RULE-PRB (evento bem-formado + não quantificar sem base) + nó N15 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E12** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N15 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E12`). Vigência imediata; incorporação da seção RULE-PRB ao RULES.md diferida ao piloto SPEC-002 (Q5), junto com EUA-E04..E11. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `RULES.md` (+RULE-PRB, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada Probabilística (`CAMADA PROBABILISTICA.MD` — MPB-001) §4, §5, §10, §57, §59 — importadas só evento bem-formado e não-quantificar-sem-base |
| Fundamento no baseline | RULE-UNC-03 (incerteza≠probabilidade — EUA-E11); RULE-EPI (falsa precisão); INDETERMINADO (EUA-E05); PB-10; PCO-01; **Conviction Vector / CCM-001 (INV-03/J-001 ABERTO)**; MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade + fronteira J-001.** A quantificação de crença **é** o Conviction Vector/CCM-001. Esta emenda importa só duas disciplinas de spec-time; todo o resto difere ao CCM-001 (SPEC-003), sem tocar J-001. |

---

## 1. Justificativa `[INFERÊNCIA]`

As distinções probabilidade≠possibilidade≠certeza≠incerteza e a falsa precisão já foram homologadas (RULE-UNC-03, RULE-EPI, PB-10). A quantificação de crença — calibração, distribuição, risco/cauda, priors, valor esperado — **é a substância do Conviction Vector / CCM-001** (SPEC-003, J-001 aberto) e é diferida para lá. O delta de spec-time da MPB-001 são **duas disciplinas** genéricas: exigir **evento probabilístico bem-formado** (§4/§5) e **não quantificar sem base** (§10/§57/§59). Esta emenda integra só isso, por referência.

---

## 2. Classificação do MPB-001 (Q1) `[DECISÃO — a homologar]`

**MPB-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/MCF/MUN/GEH). Importadas só evento bem-formado (§4/§5) e não-quantificar-sem-base (§10/§57/§59). **Não adotar por duplicação/diferimento:** §7–9 distinções (= RULE-UNC-03/RULE-EPI/PB-10); §45/§46 falsa precisão (= RULE-EPI); §43/§124 calibração, §25/§52/§53 valor esperado/risco/cauda, §60–63 bayes/priors, §19/§24 distribuições (→ **Conviction Engine/CCM-001**, J-001 aberto); §50/§133 probabilidade≠decisão (→ nó futuro **Decisional**); §83 backtest (→ specs de backtest). Sem colisão de rótulos. Registro K-MAN-11 no CONFLICT-MAP.

---

## 3. Registro do nó N15 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2 (preenche o §68 "Probabilística"; par de N14):

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N15 — Probabilística** | RULE-UNC-03 + EUA-E12 | Evento probabilístico bem-formado; não quantificar sem base. **Quantificação (calibração/risco/priors/distribuição) → Conviction Engine/CCM-001 (J-001 aberto)**; decisão → Decisional | `atomic-spec.md` |

**Interface (MAN-001 §3):** Fornece — disciplina de forma probabilística (evento+condição+horizonte; quando não numerizar). Recebe — RULE-UNC/INDETERMINADO (N14/N8), regime (N12), contrafactual (N13). Compartilha — "probabilidade ≠ certeza". Converge com — N14, N8, N12, N13; **interface com Conviction Engine/CCM-001 (J-001 aberto)** e com o nó futuro **Decisional**. Referência externa: MPB-001.

**Camadas futuras restantes (§68):** Decisional *(doc)* · Metacognição *(sem documento no repo)*.

---

## 4. Regras propostas (RULE-PRB) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras Probabilísticas (RULE-PRB)", após RULE-UNC, com `[Fonte: EUA-E12]`.

| ID | Regra |
|---|---|
| **RULE-PRB-01** | Afirmação probabilística material DEVE ser **bem-formada**: declarar **evento**, **condição/contexto** e **horizonte**. "X%" isolado (sem evento/condição/horizonte) é achado. Não se aplica ao Conviction Vector, cujo contrato é o CCM-001 (J-001 aberto). |
| **RULE-PRB-02** | **Não quantificar sem base**: quando faltar fundamento (incerteza estrutural/profunda, evento mal definido, modelo inadequado), usar **ordenação qualitativa** ou **INDETERMINADO** em vez de número fabricado. Estende RULE-UNC-03; anti-falsa-precisão (RULE-EPI). |

**Verificação:** reusa **CC-09** (status epistemológico). **Sem novo item de Constitution Check.**

> **Fronteira J-001 (INV-03/CONS-01):** RULE-PRB **não** define fórmula, pesos, limiares, calibração ou distribuição do Conviction Vector — tudo isso é CCM-001/J-001 (aberto). RULE-PRB-01/02 disciplinam apenas afirmações probabilísticas *ad hoc* de spec-time, fora do mecanismo canônico.

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-PRB ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E11.
- **Diferidos ao CCM-001/Conviction Engine** (SPEC-003, J-001 aberto): calibração, valor esperado, risco/cauda, priors, bayes, distribuições, agregação.
- **Probabilidade≠decisão** → nó futuro **Decisional**; **backtest** → specs de backtest.

---

## 6. Non-goals `[FONTE]`

- Não recria distinções possibilidade/probabilidade/certeza/incerteza (= RULE-UNC-03/RULE-EPI/PB-10) nem falsa precisão (= RULE-EPI).
- **Não define fórmula/pesos/limiares/calibração/distribuição do Conviction Vector** (INV-03/J-001 aberto — CONS-01).
- Não importa risco/cauda/valor esperado/priors (→ CCM-001) nem decisão (→ Decisional).
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MPB-001 = referência externa | **Sim** |
| Q2 | Nó **N15 (Probabilística)** no MAN-001 | **Sim** |
| Q3 | RULE-PRB-01/02 (evento bem-formado; não quantificar sem base), sob CC-09 | **Sim** |
| Q4 | Diferir ao CCM-001/Conviction (J-001 aberto): calibração/risco/valor esperado/priors/distribuição; decisão → Decisional; backtest → specs | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E11) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md, RULE-UNC/EPI, Conviction/J-001, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia + Inquérito + Causal + Contrafactual + Incerteza + Probabilística)
   ↓
Controlador incorpora à v1.5 + seção RULE-PRB no RULES.md + N15 no MAN-001 + classifica MPB-001
```

---

*HOMOLOGADA (DHR-EUA-E12, 2026-09-20). Emenda enxuta por proporcionalidade. NÃO toca J-001/Conviction. Incorporação à v1.5 diferida ao piloto SPEC-002.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — **zero achados** (nem Menor); **fronteira J-001/Conviction rigorosamente preservada**. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (CC-09, RULE-UNC-03/RULE-EPI/INDETERMINADO, INV-03/J-001, INV-04) · GLOSSARIO (Conviction/CCM-001) · GPR-001 v1.0 (PB-10, PCO-01, PC-04) · CEE-001 v2.0 · MAN-001 v1.0 · MPB-001 (ref. externa).

**Resumo:** (Q1 crítico) RULE-PRB-01 exclui explicitamente o Conviction Vector; calibração/risco/priors/distribuição diferidos ao CCM-001; J-001 aberto; CONS-01 respeitado — PASS; (Q2) proporcionalidade — não recria RULE-UNC-03/RULE-EPI/PB-10, sem novo CC — PASS; (Q3) RULE-PRB-01/02 verificáveis, estendem sem duplicar — PASS; (Q4) nó N15 par de N14, interfaces corretas — PASS; (Q5) escopo híbrido + v1.5 — PASS; TRACE-06/CONS-01 — PASS. **Diferir por inteiro ao CCM-001? Não** — as disciplinas são genéricas de spec-time; a emenda está bem dimensionada.

**Achados:** nenhum (Crítico/Médio/Menor).

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
