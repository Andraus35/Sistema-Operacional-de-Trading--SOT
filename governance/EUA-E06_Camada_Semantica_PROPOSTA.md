# EUA-E06 — Camada Semântica: Terminologia Concorrente + RULE-SEM (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E06** (emenda ao `GLOSSARIO.md` + `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx ao `GLOSSARIO.md` + `atomic-spec.md` + registro do nó N9 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E06`). Vigência imediata; incorporação ao GLOSSARIO/atomic-spec v1.5 e à seção RULE-SEM do RULES.md diferida ao piloto SPEC-002 (Q6), junto com EUA-E04/E05. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `GLOSSARIO.md` (+seção "Terminologia Concorrente por Escola"); `atomic-spec.md` §10.5 (+CC-10); `RULES.md` (+seção RULE-SEM, diferida) |
| Origem conceitual | Camada Semântica (`CAMADA SEMÂNTICA.MD`) §46, §47, §57, §29, §49 — importada **só a mecânica**; **não** duplica a não-colapsação (§53 = RULE-EPI, EUA-E05) |
| Fundamento no baseline | GLOSSARIO v (FATO NORMATIVO 2026-09-14); SES-001 v1.0 §11 (multimodelagem); CONFLICT-MAP (conflitos por escola); EUA-E05 (RULE-EPI); MAN-001 v1.0; CEE-001 v2.0 (economicidade) |
| Precedência | Não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4, TRACE-06, RULE-EPI. Não redefine termos já canônicos do GLOSSARIO. |

---

## 1. Justificativa `[INFERÊNCIA]`

A semântica do SOT já existe dispersa (GLOSSARIO para léxico; SES-001 §11 para multimodelagem; CONFLICT-MAP para conflitos de escola; EUA-E05/RULE-EPI para não-colapsação). Falta **um mecanismo**: registrar que um mesmo termo tem **acepções concorrentes por escola** (Elliott/SMC/ICT) e obrigar a spec a **declarar qual acepção usa** quando o sentido for decisivo. Hoje o GLOSSARIO registra equivalência de **nomes**, não de **sentidos concorrentes**. Esta emenda integra só esse delta, reusando o que já temos.

---

## 2. Classificação da Camada Semântica (Q1) `[DECISÃO — a homologar]`

**Camada Semântica = MSC-001 (Master Semantic Contract), referência externa não-normativa** (igual HCH-001/CMHP-001/MEG-001/GEH-001). Importada só a mecânica de terminologia concorrente/transparência semântica. **Não adotar por duplicação:** §53 Não-colapsação (já é RULE-EPI-01..03, EUA-E05). Sem colisão de rótulos (o doc não traz escala de maturidade própria). Registro K-MAN-05 no CONFLICT-MAP.

---

## 3. Registro do nó N9 + camadas futuras (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2:

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N9 — Semântico** | GLOSSARIO v1.0 (FATO NORMATIVO 2026-09-14) + EUA-E06 (SES-001 §11) | Sentido dos termos; terminologia concorrente por escola; transparência semântica | `GLOSSARIO.md` |

**Interface (MAN-001 §3):** Fornece — registro de terminologia concorrente, RULE-SEM. Recebe — PC-05/INV-10 (N3, idioma canônico), overlay SES-001 §11 (N6), RULE-EPI (N8). Compartilha — "interpretação ≠ verdade". Converge com — N3, N6, N8. Referência externa: MSC-001.

**Camadas futuras (MSC-001 §68) — nós pendentes no MAN-001** (registrar como trajetória, não adoção): Ontologia, Causalidade, Contrafactuais, Probabilidade/Incerteza, Metacognição, Decisão. Cada uma, ao chegar, entra como novo nó com interface e sensor de drift.

---

## 4. Emenda ao GLOSSARIO — Terminologia Concorrente por Escola `[PROPOSTA]`

Nova seção no `GLOSSARIO.md`. **Formato do registro** (entradas exigem fonte — não se inventa acepção):

```
| Termo | Escola/Domínio | Acepção (sentido nessa escola) | Relação/Conflito | FONTE |
```

**Regra de preenchimento:** cada linha DEVE citar FONTE (SES-001 §, CONFLICT-MAP, doc de escola). Linhas sem fonte = `[PROPOSTA]`, não normativas.

**Linha ILUSTRATIVA (estrutura; `[EXEMPLO — a preencher/validar por spec com FONTE]`):**

| Termo | Escola/Domínio | Acepção | Relação/Conflito | FONTE |
|---|---|---|---|---|
| rompimento | Elliott | fim/invalidação de contagem estrutural | vs. SMC (ver CONFLICT-MAP) | *[a validar]* |
| rompimento | SMC | BOS/CHoCH (quebra de estrutura institucional) | subordinado a Elliott (PC-01) | *[a validar]* |

> As acepções reais são preenchidas pelas specs de domínio (SES-001/CONFLICT-MAP) com FONTE; esta emenda entrega o **formato e a regra**, não o conteúdo.

---

## 5. Regras semânticas propostas (RULE-SEM) `[PROPOSTA]`

**Destino no RULES.md:** nova seção "Regras Semânticas (RULE-SEM)", após RULE-EPI, com `[Fonte: GLOSSARIO / EUA-E06]`.

| ID | Regra |
|---|---|
| **RULE-SEM-01** | Quando um termo tem acepção concorrente por escola (registro §4) e o sentido é **decisivo** para o comportamento, a spec DEVE declarar explicitamente qual acepção usa (transparência semântica). |
| **RULE-SEM-02** | Não-colapsação semântica (conceito→fato, correlação→causa, interpretação→verdade, nome→entidade) segue **RULE-EPI-01..03** (EUA-E05). Esta emenda NÃO cria regra paralela. |
| **RULE-SEM-03** | Transformação semântica (normalização/tradução) NÃO DEVE eliminar modalidade/nuance material ("pode" ≠ "será"); a forma original permanece recuperável (alinha PB-10, TRACE-06). |
| **RULE-SEM-04** | Termo já canônico no GLOSSARIO NÃO DEVE ser redefinido por spec; acepção de escola é adição contextual, não substituição (alinha PC-05/INV-10, RULE-HD-02). |

---

## 6. Constitution Check §10.5 — novo CC-10 `[PROPOSTA]`

| ID | Item | Severidade |
|---|---|---|
| **CC-10** | Termos com acepção concorrente usados com sentido decisivo têm acepção declarada (RULE-SEM-01); nenhum termo canônico do GLOSSARIO redefinido (RULE-SEM-04); modalidade preservada (RULE-SEM-03) | **Média** |

---

## 7. Drift semântico no Hygiene (Q5) `[PROPOSTA]`

Acrescentar ao passo de Convergência do RCH-001 (rotina permanente, MAN-001 §6):

```
5. Drift semântico: para termos do registro §4 usados em ≥2 specs, conferir
   se o sentido permanece consistente entre elas; divergência de acepção
   não declarada → FLAG no RCH-001 + item no CIC-001.
```

Reusa o mecanismo de Hygiene já homologado (economicidade).

---

## 8. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para as homologadas (D-DHR-PAP-001-01).
- **Incorporação ao atomic-spec/RULES.md/GLOSSARIO** consolidada na **v1.5**, no piloto SPEC-002, junto com EUA-E04 e EUA-E05. Até lá, autoridade literal = esta proposta + ata.

---

## 9. Non-goals `[FONTE]`

- Não duplica a não-colapsação (§53 = RULE-EPI); referencia.
- Não inventa acepções de trading — o registro exige FONTE por linha.
- Não redefine termos canônicos do GLOSSARIO; não altera 4Es, E0–E3, F.1–F.4, TRACE-06, Quality Gates L1–L4.
- Não adota as camadas futuras (§68) — apenas as registra como nós pendentes no MAN-001.

---

## 10. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Camada Semântica = MSC-001, referência externa não-normativa | **Sim** |
| Q2 | Nó **N9 (Semântico)** no MAN-001 + registrar camadas futuras (§68) | **Sim** |
| Q3 | Emenda: GLOSSARIO (Terminologia Concorrente) + RULE-SEM-01..04 + CC-10 | **Sim** |
| Q4 | Não-colapsação por **referência a RULE-EPI** (sem duplicar) | **Sim** |
| Q5 | Drift semântico no Hygiene (RCH-001) | **Sim** |
| Q6 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04/E05) | **Sim** |

---

## 11. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra GLOSSARIO, SES-001, atomic-spec, EUA-E05, MAN-001
   ↓
Andraus homologa (decide Q1–Q6)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic Check + Semântica juntos)
   ↓
Controlador incorpora à v1.5 + seção RULE-SEM no RULES.md + N9 no MAN-001 + classifica MSC-001
```

---

*HOMOLOGADA (DHR-EUA-E06, 2026-09-20). Vigência imediata; incorporação ao GLOSSARIO/atomic-spec v1.5 diferida ao piloto SPEC-002. Referências por ID+versão (RULE-HD-04). Não-colapsação por referência a RULE-EPI (EUA-E05); acepções exigem FONTE (sem fabricação).*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · GLOSSARIO (FATO NORMATIVO 2026-09-14) · SES-001 v1.0 (§11, PC-01) · atomic-spec v1.4 (§10.5 CC, §11 TRACE-06, EUA-E05 RULE-EPI) · EUA-E05 (homologada) · MAN-001 v1.0 (homologado) · CONFLICT-MAP · RCH-001 · MSC-001 (ref. externa).

**Resumo (8 checks):** CK-01 não-duplicação (RULE-SEM-02 referencia RULE-EPI, sem sobrepor CC-09) — PASS; CK-02 não-fabricação (registro exige FONTE por linha; "rompimento" = [EXEMPLO — a validar]) — PASS; CK-03 não-redefinição de canônico (RULE-SEM-04 preserva GLOSSARIO, PC-05/INV-10) — PASS; CK-04 RULE-SEM-01..04/CC-10 coerentes (SES §11, PB-10, RULE-HD-02) — PASS; CK-05 nó N9 + camadas futuras pendentes — PASS; CK-06 drift semântico proporcional no Hygiene — PASS; CK-07 escopo híbrido + diferimento à v1.5 — PASS; CK-08 TRACE-06/CONS-01 — PASS.

**Achado Menor e tratamento:**

| ID | Achado | Tratamento |
|---|---|---|
| A-01 | Versão do GLOSSARIO não explícita no nó N9 | **Acatado** — `GLOSSARIO v1.0 (FATO NORMATIVO 2026-09-14) + EUA-E06` |

**Recomendação do Revisor:** concorda com Q1–Q6. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
