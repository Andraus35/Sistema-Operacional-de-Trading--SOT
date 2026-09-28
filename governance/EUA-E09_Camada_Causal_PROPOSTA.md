# EUA-E09 — Camada Causal: RULE-CAU (mecanismo obrigatório + regime + guard pós-hoc) + nó N12 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E09** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N12 no MAN-001 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E09`). Vigência imediata; incorporação da seção RULE-CAU ao RULES.md diferida ao piloto SPEC-002 (Q5), junto com EUA-E04..E08. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `RULES.md` (+RULE-CAU, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada Causal (`CAMADA DE CAUSALIDADE.MD` — MCC-001) §3, §45, §47–48, §54 — importadas só: mecanismo obrigatório, dependência de regime e guard pós-hoc |
| Fundamento no baseline | RULE-EPI-02 (causalidade exige método — EUA-E05); RULE-ONT (relação≠causa — EUA-E07); AP-02/RULE-004 (evidência correlacionada); AP-10 (explicação pós-hoc); SES-001 v1.0 (regime); GPR-001 §3.6 (inversões por regime); PCO-01/02; MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade.** "Correlação≠causa" já é RULE-EPI-02/RULE-ONT/AP-02 — não recriar. Importa-se só o que falta. |

---

## 1. Justificativa `[INFERÊNCIA]`

O "correlação≠causa" já está homologado (RULE-EPI-02, RULE-ONT, AP-02). O delta real da Camada Causal são **três disciplinas** ainda não formalizadas e diretamente ligadas ao risco central do SOT — SMC/ICT afirmam mecanismos causais ("liquidez causou reversão", "rompimento causou continuação", §43): **exigir mecanismo** (§3/§54), **declarar o regime de validade** (§45) e **marcar explicação pós-hoc** (§47–48). Esta emenda integra só isso, por referência.

---

## 2. Classificação do MCC-001 (Q1) `[DECISÃO — a homologar]`

**MCC-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/GEH). Importadas só mecanismo obrigatório, regime e guard pós-hoc. **Não adotar por duplicação/diferimento:** §53 Não-confusão (= RULE-EPI-02/RULE-ONT/AP-02); §28/§58 observar-vs-intervir e intervenção hipotética (→ nó futuro **Contrafactuais** §68 + specs de backtest/CCM); §17 mediação/moderação/confounder (→ CCM-001 se necessário). Sem colisão de rótulos. Registro K-MAN-08 no CONFLICT-MAP.

---

## 3. Registro do nó N12 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2 (preenche o §68 "Causalidade"):

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N12 — Causal** | RULE-EPI-02 + EUA-E09 | Relações causa→efeito: mecanismo obrigatório; regime de validade; guard pós-hoc. Intervenção/contrafactual diferidos | `atomic-spec.md` |

**Interface (MAN-001 §3):** Fornece — disciplina causal (mecanismo, regime, anti-pós-hoc). Recebe — RULE-EPI (N8), objetos observacional/teórico (N10), questão→método (N11), overlay SES/regime (N6). Compartilha — "associação ≠ causa". Converge com — N8, N10, N11, N6. Referência externa: MCC-001.

**Camadas futuras restantes (§68):** Contrafactuais · Probabilidade/Incerteza · Metacognição · Decisão. (Observar-vs-intervir da Camada Causal fica reservado à camada Contrafactuais.)

---

## 4. Regras propostas (RULE-CAU) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras Causais (RULE-CAU)", após RULE-INQ, com `[Fonte: EUA-E09]`.

| ID | Regra |
|---|---|
| **RULE-CAU-01** | Afirmação causal (A→B) é **hipótese** e DEVE declarar o **mecanismo** que a sustenta (como A produz B), além de condições e direção. Correlação/precedência/padrão histórico NÃO bastam (estende RULE-EPI-02; não cria regra paralela). |
| **RULE-CAU-02** | Relação causal material DEVE declarar o **regime/condição de validade** (a mesma relação pode mudar ou desaparecer entre regimes). Alinha SES-001 (regime) e GPR-001 §3.6 (inversões). |
| **RULE-CAU-03** | Explicação causal formulada **após** o resultado DEVE ser marcada como **pós-hoc**, sem o status de hipótese pré-testada. Teste: "poderia ter sido formulada antes do resultado?" (estende AP-10). |

**Verificação:** reusa **CC-09** (status epistemológico) — hipótese causal↔hipótese; pós-hoc↔etiqueta de origem/tempo. **Sem novo item de Constitution Check.**

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-CAU ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04/E05/E06/E07/E08.
- **Observar-vs-intervir / intervenção hipotética** (§28/§58) → diferidos ao nó futuro **Contrafactuais** e às specs de backtest/CCM.
- **Vocabulário estatístico** (mediação/moderação/confounder) → diferido ao CCM-001.

---

## 6. Non-goals `[FONTE]`

- Não recria "correlação≠causa" (§53 = RULE-EPI-02/RULE-ONT/AP-02).
- Não importa intervenção/contrafactual (§28/§58) nem vocabulário estatístico (§17) — diferidos.
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.
- Não adota as demais camadas futuras (§68).

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MCC-001 = referência externa | **Sim** |
| Q2 | Nó **N12 (Causal)** no MAN-001 | **Sim** |
| Q3 | RULE-CAU-01..03 (mecanismo obrigatório; regime; guard pós-hoc), sob CC-09 | **Sim** |
| Q4 | Intervenção/contrafactual e vocabulário estatístico diferidos (nó Contrafactuais / CCM) | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E08) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md, RULE-EPI/ONT, AP-02/AP-10, SES-001, GPR §3.6, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia + Inquérito + Causal)
   ↓
Controlador incorpora à v1.5 + seção RULE-CAU no RULES.md + N12 no MAN-001 + classifica MCC-001
```

---

*HOMOLOGADA (DHR-EUA-E09, 2026-09-20). Emenda enxuta por proporcionalidade. Incorporação à v1.5 diferida ao piloto SPEC-002.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios; proporcionalidade verificada. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (CC-09, RULE-EPI-02) · GPR-001 v1.0 (§3.6 inversões, PCO-01/02, AP-02/AP-10) · SES-001 v1.0 (§33 regime) · CATALOGO/CONFLICT-MAP (K-MAN-01..07) · MAN-001 v1.0 · MCC-001 (ref. externa).

**Resumo:** (Q1) proporcionalidade — não recria correlação≠causa (= RULE-EPI-02/RULE-ONT/AP-02); difere intervenção/contrafactual ao nó futuro e vocabulário estatístico ao CCM; sem novo CC — PASS; (Q2) RULE-CAU-01 estende RULE-EPI-02 (mecanismo), CAU-02 ancora SES-001 §33/GPR §3.6 (regime), CAU-03 estende AP-10 (pós-hoc), sem duplicar — PASS; (Q3) cobre risco SMC/ICT sem violar PC-01 nem redefinir canônicos — PASS; (Q4) nó N12 coerente — PASS; (Q5) escopo híbrido + v1.5 — PASS; invariantes/salvaguardas/CC/TRACE-06 — PASS.

**Achado Menor:** A-01 (K-MAN-08 registro futuro) — Controlador registra no CONFLICT-MAP na efetivação.

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
