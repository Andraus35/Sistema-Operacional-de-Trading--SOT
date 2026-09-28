# EUA-E07 — Camada Ontológica: RULE-ONT (observacional vs teórico) + nó N10 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E07** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N10 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E07`). Vigência imediata; incorporação da seção RULE-ONT ao RULES.md diferida ao piloto SPEC-002 (Q5), junto com EUA-E04/E05/E06. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `RULES.md` (+RULE-ONT, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada Ontológica (`CAMADA ONTOLÓGICA.MD`) §20–21, §34, §48 — importada **só** a distinção observacional/teórico e a autoexpansão governada |
| Fundamento no baseline | INV-06/PC-03 (Evidência≠Observação); RULE-EPI (EUA-E05); RULE-SEM (EUA-E06); CEM-001/CHM-001; PO-05/PC-08 (learning propõe, governança decide); MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade / minimum-sufficient-harness.** A substância ontológica pertence aos Modelos Canônicos (CEM/CHM/CCM/CDM/CNM) e aos schemas — não a esta emenda. |

---

## 1. Justificativa `[INFERÊNCIA]`

A ontologia do SOT já está instanciada nos Modelos Canônicos (CEM/CHM), no SAS-001, no GLOSSARIO, no SES-001 e nos schemas; e os princípios ontológicos gerais (nome≠entidade, relação≠causa, incerteza, concorrência) já foram homologados nesta sessão (RULE-EPI/RULE-SEM). O delta real da Camada Ontológica é **uma distinção** ainda não formalizada e de alto valor para SMC/ICT: **entidade observacional vs construção teórica** (§20–21). Esta emenda integra **só isso**, por referência, sem recriar taxonomia ontológica.

---

## 2. Classificação da Camada Ontológica (Q1) `[DECISÃO — a homologar]`

**Camada Ontológica = MOC-001 (Master Ontological Contract), referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/GEH). Importada só a distinção observacional/teórico + autoexpansão governada. **Não adotar por duplicação/redundância:** §3/§24 (nome≠entidade) = RULE-SEM/RULE-EPI; §13–14 (relação≠causa) = RULE-EPI-02; §5 catálogo genérico de tipos e §57 maturidade = já cobertos por CEM/CHM/SAS. Sem colisão de rótulos. Registro K-MAN-06 no CONFLICT-MAP.

---

## 3. Registro do nó N10 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2 (preenche o 1º dos nós futuros §68):

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N10 — Ontológico** | CEM-001 v1.0 / CHM-001 v1.0 + EUA-E07 | O que existe no domínio; observacional vs teórico; autoexpansão governada | `canon/` |

**Interface (MAN-001 §3):** Fornece — objetos do domínio (Evidência/Hipótese/…), distinção observacional/teórico. Recebe — RULE-EPI (N8), terminologia (N9), overlay SES (N6). Compartilha — "representação ≠ realidade". Converge com — N3, N6, N8, N9. Referência externa: MOC-001.

> **Nota:** o grosso da ontologia é responsabilidade dos Modelos Canônicos no ROADMAP (**CCM-001/SPEC-003, CDM-001, CNM-001**), não desta emenda.

---

## 4. Regra proposta (RULE-ONT) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras Ontológicas (RULE-ONT)", após RULE-SEM, com `[Fonte: EUA-E07]`.

| ID | Regra |
|---|---|
| **RULE-ONT-01** | A spec DEVE distinguir **entidade observacional** (diretamente medida/observada) de **construção teórica** (postulada para explicar — ex.: order block, liquidez, "pressão compradora"). Entidade latente/teórica NÃO DEVE ser promovida a real sem tratamento epistêmico (segue RULE-EPI; não cria regra paralela). Alinha INV-06/PC-03. |
| **RULE-ONT-02** | Nova entidade/categoria ontológica é resultado cognitivo válido, mas entra por **governança** (propõe → homologa): segue PO-05/PC-08. NÃO DEVE ser auto-adotada como baseline (INV-09). |

**Verificação:** reusa **CC-09** (status epistemológico) — observacional↔observação, teórico↔hipótese/inferência. **Sem novo item de Constitution Check** (proporcionalidade).

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-ONT ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04/E05/E06.
- **Substância ontológica** (tipos de objeto, ciclos de vida, categorias) permanece nos Modelos Canônicos (CCM/CDM/CNM) — trabalho já sequenciado no ROADMAP.

---

## 6. Non-goals `[FONTE]`

- Não recria o catálogo genérico de tipos ontológicos (§5) nem os estados de maturidade (§57 = CHM).
- Não duplica relação≠causa (§13–14 = RULE-EPI-02) nem nome≠entidade (§3/§24 = RULE-SEM/RULE-EPI).
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.
- Não adota as demais camadas futuras (§68) — permanecem nós pendentes no MAN-001.

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Camada Ontológica = MOC-001, referência externa | **Sim** |
| Q2 | Nó **N10 (Ontológico)** no MAN-001 | **Sim** |
| Q3 | RULE-ONT-01/02 (observacional vs teórico; autoexpansão governada), verificada sob CC-09 | **Sim** |
| Q4 | Substância ontológica diferida aos Modelos Canônicos (CCM/CDM/CNM) | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04/E05/E06) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md, INV-06, RULE-EPI/SEM, CEM/CHM, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia)
   ↓
Controlador incorpora à v1.5 + seção RULE-ONT no RULES.md + N10 no MAN-001 + classifica MOC-001
```

---

*HOMOLOGADA (DHR-EUA-E07, 2026-09-20). Emenda enxuta por proporcionalidade (o próprio MOC-001 §45 alerta contra over-harnessing). Incorporação à v1.5 diferida ao piloto SPEC-002.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios; **proporcionalidade confirmada**. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (§9, §11 CC-09, INV-06) · EUA-E05 (RULE-EPI) · EUA-E06 (RULE-SEM) · CEM-001 v1.0 · CHM-001 v1.0 · GPR-001 v1.0 (PC-03/PO-05/PC-08/INV-09) · MAN-001 v1.0 · MOC-001 (ref. externa).

**Resumo (8 passos):** proporcionalidade — importa só observacional/teórico (§20–21) + autoexpansão governada (§34/§48); não duplica RULE-EPI/RULE-SEM/CHM/CEM; reusa CC-09 sem novo Constitution Check — PASS; RULE-ONT-01 alinha INV-06 e referencia RULE-EPI — PASS; RULE-ONT-02 referencia PO-05/PC-08/INV-09 — PASS; nó N10 ancorado em CEM/CHM, substância diferida aos CCM/CDM/CNM — PASS; escopo híbrido + diferimento à v1.5 — PASS; TRACE-06/CONS-01 OK. **Nota:** nada precisa ser diferido por inteiro — as RULE-ONT são distinções verificáveis de alto valor.

**Achado Menor e tratamento:**

| ID | Achado | Tratamento |
|---|---|---|
| A-01 | K-MAN-06 mencionado como registro existente (CONFLICT-MAP tem só K-MAN-01..05) | **Resolvido na efetivação** — Controlador registra K-MAN-06 no CONFLICT-MAP. |

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
