# EUA-E08 — Camada de Inquérito: RULE-INQ (classificação de questão + evidência discriminante) + nó N11 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E08** (emenda enxuta ao `atomic-spec.md`) |
| Natureza | Emenda EUA-Exx enxuta ao `atomic-spec.md` + registro do nó N11 no MAN-001 + correção da lista §68 |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-20; ata `DHR-EUA-E08`). Vigência imediata; incorporação da seção RULE-INQ ao RULES.md diferida ao piloto SPEC-002 (Q5), junto com EUA-E04/E05/E06/E07. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-20 |
| Alvo | `RULES.md` (+RULE-INQ, diferida); `atomic-spec.md` §11 (verificação sob CC-09, sem novo CC) |
| Origem conceitual | Camada de Inquérito (`CAMADA INQUÉRITO.MD` — MIQG-001) §9, §14, §20, §37 — importada **só** classificação de questão→método, evidência discriminante e critério de encerramento |
| Fundamento no baseline | PCO-01/PCO-02 (hipóteses concorrentes, contraevidência); RULE-EPI (EUA-E05, incl. INDETERMINADO); CEE-001 v2.0 / dial GES / D0–D9 (proporcionalidade); GEH-001 v1.1 (decomposição/inquérito); Cognitive Scheduler; MAN-001 v1.0 |
| Princípio-guia | **Proporcionalidade / minimum-sufficient-harness.** O grosso do "como investigar" já está em GEH-001, PCO, RULE-EPI, CEE e no Cognitive Scheduler — esta emenda importa só o delta. |

---

## 1. Justificativa `[INFERÊNCIA]`

O "como investigar" do SOT já está distribuído (GEH-001, PCO-01/02, RULE-EPI, CEE-001/GES, Cognitive Scheduler, padrão Revisor/verificador). O delta real do MIQG-001 são **três disciplinas** ainda não formalizadas e de alto valor para um sistema de análise probabilística: **classificar o tipo de questão para escolher o método (§9/§14)**, **buscar evidência discriminante entre hipóteses (§20)** e **declarar critério de encerramento (§37)**. Esta emenda integra **só isso**, por referência.

---

## 2. Classificação do MIQG-001 (Q1) `[DECISÃO — a homologar]`

**MIQG-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/GEH). Importada só a classificação de questão→método, evidência discriminante e critério de encerramento. **Não adotar:** o catálogo operacional INV-INQ-01..15 / INQ-S01..15 / GATE-INQ-01..10 (§62–66) — são **sensores de runtime** (pertencem ao harness-eval/GEH, não a emenda de spec); e a **ordem "3Es" do §87** (Eficácia→Eficiência→Efetividade), que **conflita** com os 4Es homologados (Eficácia→Efetividade→Eficiência→Economicidade, CEE-001 §12). Registro K-MAN-07 no CONFLICT-MAP.

---

## 3. Registro do nó N11 + correção da lista §68 (Q2) `[PROPOSTA]`

Acrescentar ao MAN-001 v1.0 §2:

| Nó | ID + versão | Domínio / Responsabilidade | Localização |
|---|---|---|---|
| **N11 — Inquérito** | GEH-001 v1.1 + EUA-E08 | Como investigar: questão→método, evidência discriminante, critério de encerramento | `atomic-spec.md` / `RETOMADA/GEH-001…md` |

**Interface (MAN-001 §3):** Fornece — disciplina de inquérito (classificação de questão, discriminação, closure). Recebe — RULE-EPI/INDETERMINADO (N8), objetos (N10), overlay SES (N6), economia (N5). Compartilha — "método deve seguir a questão". Converge com — N4, N5, N8, N10. Referência externa: MIQG-001.

**Correção da lista §68 (MSC-001):** a lista de camadas futuras havia omitido **Inquérito**. Lista corrigida de nós futuros pendentes: Causalidade · Contrafactuais · Probabilidade/Incerteza · Metacognição · Decisão. (Ontologia = N10; Inquérito = N11; Semântica = N9; Epistemologia = N8 — já registrados.)

---

## 4. Regras propostas (RULE-INQ) `[PROPOSTA]`

**Destino no RULES.md:** seção "Regras de Inquérito (RULE-INQ)", após RULE-ONT, com `[Fonte: EUA-E08]`.

| ID | Regra |
|---|---|
| **RULE-INQ-01** | Antes de investigar/especificar comportamento com incerteza material, a spec DEVE classificar o **tipo de questão** (factual/descritiva/explicativa/preditiva/diagnóstica/verificação/comparativa) e usar **método compatível** (§9/§14). Método escolhido antes da pergunta = achado. |
| **RULE-INQ-02** | Havendo hipóteses concorrentes (PCO-01), a investigação DEVE buscar **evidência discriminante** ("que observação diferencia H1 de H2?"), não apenas confirmatória. Estende PCO-02; não cria regra paralela. |
| **RULE-INQ-03** | Toda investigação material DEVE declarar **critério de encerramento** (suficiência proporcional ao risco — GES/D0–D9). Sem suficiência → estado **INDETERMINADO** (RULE-EPI), não conclusão forçada nem investigação infinita. |

**Verificação:** reusa **CC-09** (status epistemológico) e o dial GES (proporcionalidade). **Sem novo item de Constitution Check.**

---

## 5. Escopo e diferimento `[PROPOSTA]`

- **Prospectivo-obrigatório** para specs novas (SPEC-002+); **retroativo-como-auditoria** para homologadas (D-DHR-PAP-001-01).
- **Incorporação** da seção RULE-INQ ao `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04/E05/E06/E07.
- **Sensores operacionais** (INV-INQ/INQ-S/GATE-INQ) → diferidos ao **harness-eval/GEH-001** (Track A/B), onde são runtime; não entram nesta emenda.

---

## 6. Non-goals `[FONTE]`

- Não importa o catálogo operacional (§62–66) nem a ordem "3Es" do §87 (conflita com 4Es).
- Não duplica PCO-02 (§29 contraevidência), RULE-EPI (§34/§47/§53), economia (CEE/GES).
- Não cria novo Constitution Check (usa CC-09); não altera 4Es, E0–E3, F.1–F.4, Quality Gates L1–L4.
- Não adota as demais camadas futuras (§68) — permanecem nós pendentes no MAN-001.

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | MIQG-001 = referência externa | **Sim** |
| Q2 | Nó **N11 (Inquérito)** no MAN-001 + correção da lista §68 | **Sim** |
| Q3 | RULE-INQ-01..03 (questão→método; evidência discriminante; critério de encerramento), sob CC-09 | **Sim** |
| Q4 | Sensores INV-INQ/INQ-S/GATE-INQ diferidos ao harness-eval/GEH | **Sim** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04/E05/E06/E07) | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (este arquivo)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra RULES.md, PCO, RULE-EPI, CEE/GES, GEH-001, MAN-001
   ↓
Andraus homologa (decide Q1–Q5)
   ↓
Piloto SPEC-002 (Herança/Delta + Epistemic + Semântica + Ontologia + Inquérito)
   ↓
Controlador incorpora à v1.5 + seção RULE-INQ no RULES.md + N11 no MAN-001 + classifica MIQG-001
```

---

*HOMOLOGADA (DHR-EUA-E08, 2026-09-20). Emenda enxuta por proporcionalidade (o próprio MIQG-001 §88 pede suficiência necessária). Incorporação à v1.5 diferida ao piloto SPEC-002.*

---

## Anexo A — Parecer do Revisor SOT (2026-09-20)

**Veredito: CONFORME** — sem achados Críticos ou Médios; proporcionalidade e conflito 4Es verificados. Acesso ao `RULES.md` v1.1 confirmado.

**Baselines auditados:** RULES.md v1.1 · atomic-spec v1.4 (CC-09, RULE-EPI/INDETERMINADO) · GPR-001 v1.0 (PCO-01/02) · CEE-001 v2.0 (§12 4Es) · GEH-001 v1.1 · MAN-001 v1.0 · CONFLICT-MAP · MIQG-001 (ref. externa).

**Resumo (7 checks):** (1) proporcionalidade — 3 disciplinas, não recria GEH/PCO/RULE-EPI/CEE, difere catálogo §62–66, sem novo CC — PASS; (2) conflito 4Es — rejeita ordem "3Es" §87, registra K-MAN-07 — PASS; (3) RULE-INQ-01..03 coerentes e verificáveis (INQ-02 estende PCO-02; INQ-03 amarra INDETERMINADO+GES) — PASS; (4) nó N11 + correção da lista §68 — PASS; (5) sensores diferidos ao harness-eval/GEH — PASS; (6) escopo híbrido + v1.5 — PASS; (7) TRACE-06/CONS-01 — PASS. **Diferimento por inteiro?** Não necessário.

**Achado Menor:** A-01 (versão da EUA-E08 não explícita no nó N11) — aceitável pré-homologação; formato uniforme mantido.

**Recomendação do Revisor:** concorda com Q1–Q5. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
