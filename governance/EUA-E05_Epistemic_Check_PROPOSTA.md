# EUA-E05 — Epistemic Check no atomic-spec §11 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E05** (emenda ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx ao `atomic-spec.md` + registro do nó N8 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E05`). Vigência imediata; incorporação ao `atomic-spec` v1.5 e à seção RULE-EPI do RULES.md diferida ao piloto SPEC-002 (Q5), junto com a EUA-E04. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `atomic-spec.md` §11 (Etiquetagem e status epistemológico → +Epistemic Check) e §10.5 (Constitution Check → +CC-09) |
| Origem conceitual | MEG-001 (`CAMADA EPISTÊMICA.MD`) §13, §60, §67 — importada **só a mecânica**; **sem** rótulos de maturidade Nível 0–6 (§106, colidem) e sem recriar unidade EPI-ID (§100, já coberta por BASpec/Enforcement Contract) |
| Fundamento no baseline | atomic-spec v1.4 §11 (TRACE-06); INV-06/PC-03 (Evidência≠Observação); GPR-001 v1.0 PB-10/PCO-01/PCO-02/PCO-04; CEM-001 v1.0 / CHM-001 v1.0; INV-07; MAN-001 v1.0 (registro do nó) |
| Precedência | Não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4, TRACE-06 existente, nem cria classe/rótulo de maturidade. |

---

## 1. Justificativa `[INFERÊNCIA]`

O SOT já governa epistemologia de forma **dispersa** (TRACE-06 §11; INV-06/PC-03; PB-10; PCO-01/02; hierarquia cognitiva do SAS-001; CEM/CHM). Faltam **5 mecanismos de verificação** que o MEG-001 explicita e que hoje o Revisor não tem como cobrar de forma uniforme — entre eles a **formalização do estado "Indeterminado/HOLD"**, adiado duas vezes. Esta emenda integra **só esse delta**, reusando o que já existe.

---

## 2. Classificação do MEG-001 (Q1) `[DECISÃO — a homologar]`

**MEG-001 (`CAMADA EPISTÊMICA.MD`) = referência externa não-normativa** (mesmo status de HCH-001, CMHP-001, GEH-001). Dele importa-se apenas a mecânica de verificação epistêmica (esta emenda). **Fora de adoção:** maturidade "Nível 0–6" (§106, colide com Quality Gates L1–L4 / harness-score L0–L4 / maturidade GPR-001 §11 L0–L5) e a unidade EPI-ID (§100, já coberta por BASpec + Enforcement Contract). Registro K-MAN-03-ep no CONFLICT-MAP.

---

## 3. Registro do nó N8 — Epistêmico (no MAN-001) (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2:

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N8 — Epistêmico** | atomic-spec v1.4 §11 (TRACE-06) + EUA-E05 | Status epistemológico das afirmações; anti-conversão; incerteza/abstenção | `atomic-spec.md` |

**Interface (MAN-001 §3):** Fornece — etiquetas/estados epistêmicos, regra anti-conversão, INV-EPI. Recebe — PC-03/INV-06 (N1), PB-10/PCO (N2), CEM/CHM (N3). Compartilha — "coerência ≠ validade". Converge com — N2, N3, N4. Referência externa: MEG-001.

---

## 4. Epistemic Check — acréscimo ao §11 do atomic-spec `[PROPOSTA]`

### 4.1 Regra contra conversão silenciosa (MEG-001 §13)

Nenhuma afirmação material pode **subir de status** sem justificativa proporcional registrada. Transições proibidas quando implícitas:

```
suposição → fato          possibilidade → probabilidade → certeza
inferência → observação    hipótese → conclusão
memória → evidência        coerência → validade
correlação → causalidade   fonte → verdade    retrieved → verdade    consenso → validado
```

| ID | Regra |
|---|---|
| **RULE-EPI-01** | Afirmação material NÃO DEVE subir de status epistêmico sem justificativa proporcional explícita (evidência/método). Transição silenciosa = achado. |
| **RULE-EPI-02** | Afirmação causal exige método compatível com causalidade; correlação/associação NÃO basta (alinha AP-02, RULE-004). |
| **RULE-EPI-03** | Conclusão NÃO DEVE exceder o escopo da evidência (scope overreach); generalização declara seu limite (alinha SES-001 §36). |

### 4.2 Estados de gate epistêmico (MEG-001 §60) — mapeados ao fluxo vigente

| Estado epistêmico | Equivalente no SOT |
|---|---|
| PASS | CONFORME |
| PASS-COM-INCERTEZA | CONFORME com incerteza declarada (PB-10) |
| INVESTIGAR / PEDIR INFORMAÇÃO / EXIGE TESTE | HOLD operacional |
| **INDETERMINADO** | HOLD de 1ª classe = `[DECISÃO NECESSÁRIA]` / Decisão Aberta (formaliza o HOLD adiado) |
| REWORK / BLOCK | NÃO CONFORME |

> **INDETERMINADO** passa a ser estado explícito: ausência de evidência suficiente **não** vira PASS nem NÃO CONFORME automático — vira HOLD registrado. Fecha a lacuna recorrente.

### 4.3 Invariantes epistêmicos (INV-EPI) — consolidação (MEG-001 §67)

| ID | Invariante | Âncora no baseline |
|---|---|---|
| INV-EPI-01 | Hipótese não é apresentada como fato | PC-03 / INV-06 / CHM |
| INV-EPI-02 | Inferência não é apresentada como observação | INV-06 / PC-03 |
| INV-EPI-03 | Confiança não substitui evidência | **net-new** (parcial PB-10) |
| INV-EPI-04 | Incerteza material é declarada | PB-10 |
| INV-EPI-05 | Conflitos relevantes são preservados | PCO-01 / CONFLICT-MAP |
| INV-EPI-06 | Conclusão não excede o escopo da evidência | **net-new** (RULE-EPI-03) |
| INV-EPI-07 | Proveniência de evidência crítica é rastreável | PB-05 / SES-001 §60 |
| INV-EPI-08 | O sistema pode declarar desconhecimento/abster-se | **net-new** (estado INDETERMINADO) |
| INV-EPI-09 | Conclusão é revisável diante de nova evidência | PCO-04 / INV-07 |
| INV-EPI-10 | Mudança de status epistêmico é justificável | **net-new** (RULE-EPI-01) |

Net-new: INV-EPI-03, 06, 08, 10. Os demais re-ancoram invariantes vigentes (não duplicam — referenciam).

---

## 5. Constitution Check §10.5 — novo CC-09 `[PROPOSTA]`

| ID | Item | Severidade |
|---|---|---|
| **CC-09** | Afirmações materiais com status epistêmico correto (TRACE-06); sem conversão silenciosa (RULE-EPI-01..03); incerteza declarada quando material; estado INDETERMINADO usado no lugar de PASS/FAIL forçado | **Média** (Crítica se converter causalidade/fato sem base em comportamento com efeito E3) |

**Destino no RULES.md:** nova seção "Regras Epistêmicas (RULE-EPI)", após RULE-HD, com `[Fonte: atomic-spec §11 / EUA-E05]`.

---

## 6. Escopo e diferimento (Q4) `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para as homologadas (igual D-DHR-PAP-001-01 e EUA-E04).
- **Guardrails de contaminação** (MEG-001 §48–53: memória≠evidência, retrieved≠verdade, consenso≠validado) ficam **diferidos** às specs de RAG/Knowledge Graph/multiagente (SPEC-006 e correlatas), onde têm objeto concreto. Não entram nesta emenda.
- **Incorporação ao atomic-spec v1.5** junto com a EUA-E04, no mesmo piloto (SPEC-002).

---

## 7. Non-goals `[FONTE]`

- Não adota maturidade Nível 0–6 (§106) nem cria unidade EPI-ID (§100).
- Não altera TRACE-06 existente (estende); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.
- Não cria autoridade nova: homologação = Andraus; verificação = Revisor; registro = Controlador.

---

## 8. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MEG-001 = referência externa não-normativa | **Sim** |
| Q2 | Registrar nó **N8 (Epistêmico)** no MAN-001 | **Sim** |
| Q3 | Emenda EUA-E05 (Epistemic Check §11 + CC-09 + RULE-EPI + INV-EPI) | **Sim** |
| Q4 | Diferir guardrails de contaminação (RAG/multiagente) às specs correspondentes | **Sim** |
| Q5 | Incorporar ao atomic-spec v1.5 junto com EUA-E04 no piloto SPEC-002 | **Sim** |

---

## 9. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra atomic-spec §11, GPR-001, CEM/CHM, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto em SPEC-002 (Herança/Delta + Epistemic Check juntos)
   ↓
Controlador incorpora ao atomic-spec v1.5 + seção RULE-EPI no RULES.md + N8 no MAN-001 + classifica MEG-001
```

---

*HOMOLOGADA (DHR-EUA-E05, 2026-09-20). Vigência imediata; incorporação ao atomic-spec v1.5 diferida ao piloto SPEC-002. Referências por ID+versão (RULE-HD-04).*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (§11 TRACE-06, CC-01..08) · GPR-001 v1.0 (PB-10, PCO, PC-03) · CEM-001 v1.0 · CHM-001 v1.0 · CATALOGO-OFICIAL · CONFLICT-MAP · MAN-001 v1.0 (homologado) · MEG-001 (ref. externa).

**Resumo (8 passos):** encaixe de §11/CC-09 sem contradizer TRACE-06/CC-01..08 — PASS; INV-EPI-01..10 com âncoras corretas e 4 net-new (03/06/08/10) genuínos — PASS; estados de gate (INDETERMINADO = HOLD 1ª classe) coerentes — PASS; RULE-EPI-01..03 coerentes com AP-02/RULE-004/SES-001 §36 — PASS; sem colisão (evita maturidade Nível 0–6 e unidade EPI-ID; não recria TRACE-06) — PASS; nó N8 no MAN-001 com interface correta — PASS; escopo híbrido + diferimento coerentes com D-DHR-PAP-001-01 — PASS; TRACE-06/CONS-01 OK.

**Achados Menores e tratamento:**

| ID | Achado | Tratamento |
|---|---|---|
| A-01 | Nó N8 sem versão inline | **Acatado** — `atomic-spec v1.4 §11 (TRACE-06) + EUA-E05` |
| A-02 | "SES §60" ambíguo | **Acatado** — INV-EPI-07 agora cita `SES-001 §60` |

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
