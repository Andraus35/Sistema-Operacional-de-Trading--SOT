# EUA-E15 — Redesignação do Piloto de Incorporação para SPEC-001 (auditoria retroativa das 11 emendas) + Plano de Auditoria (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E15** (emenda aditiva de processo/escopo de incorporação) |
| Natureza | Emenda aditiva às atas DHR-EUA-E04..E14 (Q5 "piloto SPEC-002") + Plano de Auditoria Retroativa |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-21; ata `DHR-EUA-E15`). Redesignação aditiva vigente; não altera baseline; não reescreve SPEC-001. |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-21 |
| Alvo | Q5 das atas DHR-EUA-E04..E14 (redesignação aditiva do piloto); `specs/features/SPEC-001/` (auditoria, não reescrita); `atomic-spec.md` (consolidação v1.5); `governance/CIC-001` (Harness Debt) |
| Fundamento no baseline | **D-DHR-PAP-001-01** (regime: PC-* retroativo-como-auditoria; homologadas auditadas, não reescritas); **BL-008** (reavaliação SPEC-001, sem reescrita forçada — R1); INV-07 (nunca deleta), INV-09 (baseline só com homologação); atomic-spec §11 (TRACE-06/CC-09) |
| Princípio-guia | **Auditoria ≠ reescrita.** SPEC-001 é o substrato mais rigoroso para exercitar as 11 emendas (é o Hypothesis Harness). O piloto retroativo produz achados/Harness Debt; SPEC-001 só é re-homologada onde surgir Crítico. |

---

## 1. Justificativa `[INFERÊNCIA]`

As 11 emendas EUA-E04..E14 (Herança/Delta + N8–N17: Epistemic/Semântica/Ontologia/Inquérito/Causal/Contrafactual/Incerteza/Probabilística/Decisional/Metacognição) fixaram na Q5 de cada ata **"incorporar à v1.5 no piloto SPEC-002"** — uma spec nova a redigir. Porém:

1. A **SPEC-001 (Hypothesis Harness, v1.1, HOMOLOGADA — BASELINE)** já existe e é **CRITICAL**. Trata exatamente do que as 11 emendas disciplinam: hipótese≠fato, evidência, invalidação, incerteza, contrafactual, decisão. É o **campo de prova mais rigoroso** possível — testa as emendas contra conteúdo homologado real, não contra uma spec escrita sob medida.
2. O regime **D-DHR-PAP-001-01** já define: specs homologadas recebem princípios/emendas **como auditoria retroativa** (Harness Debt no CIC-001), **não como reescrita**. Logo, retroagir a SPEC-001 é a aplicação *natural* do regime já homologado.
3. Já existe **BL-008** ("Reavaliar SPEC-001 sob SES-001 §67 — sem reescrita forçada, R1"). Este piloto **funde** BL-008 ao exercício das emendas.

**Não é** substituir a Q5 das atas — é **acrescentar** SPEC-001 como piloto de auditoria (INV-07: as atas ficam intactas; adiciona-se uma decisão de redesignação).

---

## 2. Redesignação do piloto (Q1) `[PROPOSTA]`

| Antes (Q5 das atas EUA-E04..E14) | Depois (aditivo — não apaga) |
|---|---|
| Incorporação à v1.5 diferida ao **piloto SPEC-002** | Piloto de incorporação = **auditoria retroativa da SPEC-001** (v1.1 baseline) contra as 11 emendas; SPEC-002 deixa de ser pré-requisito (pode ser aposentada como veículo ou mantida para conteúdo prospectivo futuro) |

- **INV-07:** as atas DHR-EUA-E04..E14 permanecem inalteradas; esta emenda **acrescenta** a decisão de redesignação. A "história" da Q5 original é preservada.
- **Veículo de incorporação:** a própria auditoria de SPEC-001 gera o material para a **atomic-spec v1.5** + seções RULE-* no RULES.md (medindo o gap v1.3→v1.5).

---

## 3. Regime da auditoria retroativa (Q2) `[PROPOSTA]`

Coerente com D-DHR-PAP-001-01 e BL-008 R1:

1. **Modalidade = auditoria, não reescrita.** Exercita-se cada emenda como *pergunta de conformidade* contra a SPEC-001; o resultado é um **achado** (PASS / Harness Debt / Crítico), não uma edição.
2. **Achados não-Críticos → CIC-001 (Harness/Normative Debt)** — registrados, priorizados, tratados no ritmo do backlog. Não bloqueiam.
3. **Achado Crítico → dispara re-homologação de SPEC-001** por emenda (fluxo Especificador→Revisor→Andraus), **nunca** reescrita automática ou silenciosa.
4. **SPEC-001 permanece BASELINE** durante a auditoria (INV-09). Sua versão só muda por homologação explícita, se houver Crítico.
5. **Nota de método:** SPEC-001 usa atomic-spec **v1.3**; as emendas consolidam em **v1.5**. A auditoria mede exatamente o **gap v1.3→v1.5** — este é o produto que alimenta a consolidação.

---

## 4. Plano de Auditoria — mapa Emenda × SPEC-001 (Q3) `[PROPOSTA]`

Cada emenda vira uma **pergunta de conformidade** contra a SPEC-001 (Hypothesis Harness). Saída por linha: `PASS` / `Debt` / `Crítico` / **`N/A (sem superfície na SPEC-001)`** — este último quando a emenda não incide sobre o escopo da SPEC-001 (ex.: RULE-DEC/decisão operacional, que a SPEC-001/Hypothesis Harness não exerce). Toda linha traz âncora `arquivo:§`. *(N/A incorporado por MEN-01, parecer do Revisor.)*

| Emenda | Regra | Pergunta de auditoria à SPEC-001 |
|---|---|---|
| EUA-E04 | RULE-HD (Herança/Delta) | SPEC-001 declara herança de CHM-001/CEM-001 + delta local por referência (ID+versão)? |
| EUA-E05 | RULE-EPI / INDETERMINADO / CC-09 | Hipótese é tratada como hipótese (não fato)? Há estado INDETERMINADO/abstenção? Etiquetagem TRACE-06 presente? |
| EUA-E06 | RULE-SEM | Termos concorrentes (hipótese/evidência/invalidação por escola) têm acepção declarada quando decisivos? |
| EUA-E07 | RULE-ONT | Construções teóricas (ex.: order block, "pressão") são distinguidas de observacional, sem promoção a real? |
| EUA-E08 | RULE-INQ | Evidência que sustenta a hipótese é **discriminante**? Há critério de encerramento (→ INDETERMINADO)? |
| EUA-E09 | RULE-CAU | Asserções causais na hipótese exigem mecanismo + regime; guard pós-hoc presente? |
| EUA-E10 | RULE-CTF | O **contrafactual de invalidação** (INV-02) está ligado ao invalidador declarado da hipótese? |
| EUA-E11 | RULE-UNC | A incerteza da hipótese é localizada/tipificada e não contaminada; incerteza≠probabilidade? |
| EUA-E12 | RULE-PRB | A "probabilidade declarada" da hipótese é evento bem-formado (evento+condição+horizonte)? Não quantifica sem base? |
| EUA-E13 | RULE-DEC | A SPEC distingue hipótese/análise de **decisão/execução** (produz recomendação, não ordem)? Decisão condicional quando falta info? |
| EUA-E14 | RULE-MET | Dependência de evidências não vira falsa confirmação independente? Abstenção é produtiva (localiza)? Revisibilidade da hipótese? |

**Fronteiras a respeitar na auditoria:** J-001 (não fechar Conviction), CC-02 (não redefinir CEM/CHM), INV-09 (não reescrever baseline sem homologação).

**Papéis e saídas:**
- **Especificador** produz o **Mapa de Auditoria** (as 11 linhas acima preenchidas contra a SPEC-001, com âncora `arquivo:§` e veredito por linha).
- **Revisor SOT** audita o mapa (CONFORME/NÃO CONFORME) e valida a classificação dos achados.
- **Achados** → CIC-001 (Debt) ou re-homologação (Crítico).
- **Produto final** → base da **atomic-spec v1.5** + seções RULE-* no RULES.md.

---

## 5. Fusão com BL-008 e consolidação (Q3/Q4) `[PROPOSTA]`

- **BL-008** ("Reavaliar SPEC-001 sob SES-001 §67") é **ativado** e **absorvido** por este piloto (reavaliação SES-001 §59/§60 entra como 12ª linha do mapa). Atualizar seu estado no RMR-001 quando homologado.
- **Consolidação:** os achados PASS/Debt derivam a **atomic-spec v1.5** (incorporação das seções RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET no RULES.md) — objetivo original do "piloto", agora ancorado em substrato real.

---

## 6. Non-goals `[FONTE]`

- **Não reescreve** a SPEC-001 (INV-09); auditoria produz achados, não edições.
- Não altera as atas DHR-EUA-E04..E14 (INV-07); apenas acrescenta a redesignação.
- Não fecha J-001 nem redefine CEM/CHM (CC-02).
- Não obriga SPEC-002; a aposenta como pré-requisito do piloto (pode ser retomada para conteúdo prospectivo).

---

## 7. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Redesignar o piloto de incorporação para **auditoria retroativa da SPEC-001** (aditivo às atas EUA-E04..E14; INV-07) | **Sim** |
| Q2 | Regime = **auditoria, não reescrita** (achados→CIC-001; Crítico→re-homologação; SPEC-001 permanece baseline) | **Sim** |
| Q3 | Executar o **Mapa de Auditoria** (11 emendas + BL-008) e derivar a **atomic-spec v1.5** | **Sim** |
| Q4 | Ativar/absorver **BL-008** neste piloto; aposentar SPEC-002 como pré-requisito | **Sim** |

---

## 8. Fluxo de autoridade

```
[feito] Especificador redige a PROPOSTA (esta redesignação + plano)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra D-DHR-PAP-001-01, BL-008, INV-07/09, atas EUA-E04..E14
   ↓
Andraus homologa (decide Q1–Q4)
   ↓
Especificador produz o Mapa de Auditoria (11 emendas + BL-008 × SPEC-001)
   ↓
Revisor audita o mapa → achados (CIC-001 Debt / Crítico→re-homologação)
   ↓
Controlador: redesignação registrada; BL-008 Absorvido; consolidação atomic-spec v1.5 + RULE-* no RULES.md
```

---

## Anexo A — Autopré-check do Especificador (2026-09-21)

- [x] TRACE-06 aplicado; status = PROPOSTA (CONS-01).
- [x] Não reescreve SPEC-001 (INV-09) nem apaga atas (INV-07) — apenas aditivo.
- [x] Coerente com D-DHR-PAP-001-01 (retroativo-como-auditoria) e BL-008 R1 (sem reescrita forçada).
- [x] Fronteiras preservadas: J-001 (não fecha Conviction), CC-02 (não redefine CEM/CHM).
- [x] Mapa de auditoria = 11 emendas + BL-008, com veredito por linha e âncora arquivo:§.
- [x] SPEC-001 = substrato CRITICAL real (Hypothesis Harness), método v1.3 → gap para v1.5 mensurável.

## Anexo B — Parecer do Revisor SOT (2026-09-21)

**Veredito: CONFORME** — 1 achado Menor (MEN-01, acatado). Acesso ao `RULES.md` v1.1 confirmado (M-02).

**Baselines auditados:** RULES.md v1.1 · DHR-PAP-001 (D-DHR-PAP-001-01) · DHR-EUA-E04..E14 (Q5 SPEC-002) · RMR-001 (BL-008 Em espera) · SPEC-001/plan.md (v1.1 baseline, método v1.3) · atomic-spec v1.4 (§11, CC-02, J-001/INV-03, INV-07/09) · CIC-001 v1.3 (Harness Debt) · CHM-001/CEM-001 (fronteira).

**Resumo por ponto:** (1) INV-07 aditividade — atas preservadas — PASS; (2) INV-09/regime auditoria-não-reescrita coerente com D-DHR-PAP-001-01 — PASS; (3) BL-008 fusão coerente com gatilho/estado (auditoria ocorre antes da 1ª Engineering Card) — PASS; (4) mapa das 11 perguntas verificável e ancorável, sem fechar J-001 nem redefinir CEM/CHM — PASS; (5) fronteiras J-001/CC-02/INV-09 respeitadas — PASS; (6) veículo v1.3→v1.5 válido — PASS com MEN-01; (7) autoridade corretamente encaminhada a Andraus — PASS.

**Achado:**

| ID | Severidade | Constatação | Tratamento |
|---|---|---|---|
| MEN-01 | Menor | Schema de saída do mapa não previa "N/A (sem superfície)" para emenda que não incide sobre SPEC-001 (ex.: RULE-DEC) | **ACATADO** — §4 atualizado com o veredito `N/A`. |

**Recomendação (Q1–Q4):** integridade verificada em todas; autorizar. **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
