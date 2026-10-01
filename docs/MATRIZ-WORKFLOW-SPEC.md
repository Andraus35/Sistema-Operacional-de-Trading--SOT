# MATRIZ `WF-xx → Spec dona` — WORKFLOW.md × Specs

| Campo | Valor |
|---|---|
| **Natureza** | **NÃO-NORMATIVA · DERIVADA · REGENERÁVEL.** Mapa de rastreabilidade entre os IDs do setup operacional (`WORKFLOW.md`) e os slots de Spec (ROADMAP). Não cria regra, não fecha decisão, não é baseline. |
| **Fonte de verdade** | **`WORKFLOW.md` (versão vigente)** para os IDs `WF-xx`/`WF-Dxx`/`WF-Mxx`; **`ROADMAP.md`** para os slots de Spec e seu estado. Em qualquer divergência, prevalecem esses dois documentos — esta matriz é descartável e re-derivável a partir deles. |
| **Regeneração** | Reconstruir relendo `WORKFLOW.md` (versão vigente) e a tabela de slots do `ROADMAP.md` (§26 / linha "Mapa de capacidades"). Nenhum ID é citado por linha ou por versão numérica (regra de citação estável da `WORKFLOW.md`). |
| **Autor** | Especificador Principal (Claude Code) · 2026-10-01 |
| **Aviso de slot** | Salvo onde marcado **Homologada/Candidata**, **toda "Spec dona" é um slot INDICATIVO** (EUA-E21 / RULE-ECC-01): número, fronteira e decomposição só se fixam na abertura de cada Spec. "Spec dona" = *expectativa de rastreabilidade*, não atribuição baselined. |
| **Higiene de ID (detector D6)** | Todos os IDs abaixo **existem** na versão vigente da `WORKFLOW.md`. ID inexistente = ERRO; versão citada ≠ vigente = WARN — por isso esta matriz escreve **"versão vigente"**, nunca um número de versão. |

**Legenda — Estado:** Homologada (baseline) · Candidata (em revisão) · Indicativa (slot não aberto) · Editável (`[REVISAR · BL-026]`) · Fechada/Aberta (para `WF-Dxx`).
**Legenda — Natureza:** Mecanismo (contrato a especificar) · Parâmetro editável (valor configurável, não baseline) · Decisão (ponto de decisão de Andraus) · Insumo (requisito/fronteira; não é Spec cognitiva do SOT).

---

## 1. Pipeline declarado (WF-01..07)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-01** | Pré-condição: TF + tipo de trading; missão assistida/pré-programada | SPEC-015 (Mission Engine & Lifecycle) | SPEC-008 (Scheduler) | Indicativa | Mecanismo | Config da missão; consome WF-T01/WF-R01. |
| **WF-02** | Fase 1 — contexto estrutural (Agente Estrutural = Elliott) | SPEC-010 (Structural/Elliott) | SPEC-003 (convicção), SPEC-015 (dispatch) | Indicativa | Mecanismo | Elliott cria hipótese primária (INV-02/CC-01). |
| **WF-03** | Fase 1 — confirmação institucional condicional (SMC) | SPEC-012 (Institutional/SMC) | SPEC-011 (Fibonacci/Fractal), SPEC-015 | Indicativa | Mecanismo | SMC cria sub-hipótese (parent_id); não veta Elliott. |
| **WF-04** | Fase 1 — síntese de contexto (Manager): convicção macro + alarme-gatilho | SPEC-015 (Manager/Mission) | SPEC-003 (convicção macro, CF-010), SPEC-008 (alarme/scheduler) | Indicativa | Mecanismo | "Formar convicção" = o Manager invoca o Conviction Engine (SPEC-003); ver §Conflitos C-1. |
| **WF-05** | Ativação na Killzone — Agente Operacional (ICT) produz setup operacional | SPEC-013 (Execution/ICT) | SPEC-008 (gatilho Killzone), SPEC-015 | Indicativa | Mecanismo | ICT **não cria hipótese** (INV-02); setup atrelado por parent_id. |
| **WF-06** | Fase 2 — síntese global (Manager): convicção global + pacote risco-retorno | SPEC-014 (Synthesis Agent) | SPEC-003 (convicção global), SPEC-015 | Indicativa | Mecanismo | TMP interno Synthesis→Risk (SPEC-016 repurposada). Ver §Conflitos C-1. |
| **WF-07** | Gate de Risco → Risk Agent → Bot Trade Finance (externo) | Família **RISK-SPEC** (BL-018) | SPEC-014 (handoff), SPEC-016 (TMP) | Indicativa | Mecanismo | Família RISK ainda não numerada/autorizada (EUA-E20); Bot Trade Finance é externo (WF-X04). |

---

## 2. Killzone, relógio e missão (WF-K01..K04)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-K01** | Killzones ICT em relógio de Nova York; valem p/ os 3 ativos | SPEC-008 (Scheduler) | SPEC-015 | Indicativa | Mecanismo | Horários = WF-R02 (editável). |
| **WF-K02** | Pré-aviso 1h antes; dono do abrir/fechar = Manager/Scheduler | SPEC-008 (Scheduler) | SPEC-015 | Indicativa | Mecanismo | Determinístico (ENF-03), não-LLM. |
| **WF-K03** | Fuso da máquina detectado; cálculo em `America/New_York`; janela fixa | SPEC-008 (Scheduler) | — | Indicativa | Mecanismo | — |
| **WF-K04** | Missão pré-programada (madrugada); fila para revisão; SOT não executa | SPEC-015 (Mission Lifecycle) | SPEC-008 | Indicativa | Mecanismo | Premissa: HITL adiado (WF-J01/SPEC-018); INV-05. |

---

## 3. Time frames e alinhamento (WF-T01..T02)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-T01** | Tabela de TFs por tipo de trading (tripla contexto/confirmação/entrada) | SPEC-015 (Mission) | SPEC-008, agentes SPEC-010..013 | Indicativa | Parâmetro editável | Valores = WF-R01 (`[REVISAR · BL-026]`); sobrescrevível por missão. |
| **WF-T02** | Alinhamento obrigatório entrada↔contexto (desalinhado = sem entrada) | SPEC-013 (Execution/ICT) | SPEC-010, SPEC-015 | Indicativa | Mecanismo | Reforça INV-01. |

---

## 4. Alarme-gatilho (WF-A01..A03)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-A01** | Objeto do alarme (nível/direção/validade/invalidação/parent_id) — gatilho de análise, nunca ordem | SPEC-008/SPEC-015 (Manager/Scheduler) | **SPEC-003** (consome parent_id/hypothesis_ref, CF-013) | Indicativa | Mecanismo | INV-05; a SPEC-003 **não produz** o alarme, só o consome. |
| **WF-A02** | FSM do alarme (`IDLE→ARMED→TRIGGERED→{CONSUMED\|EXPIRED\|CANCELLED}`) | SPEC-008 (Scheduler) | SPEC-015 | Indicativa | Mecanismo | Gate determinístico (ENF-03). |
| **WF-A03** | Morte do alarme: expira por prazo / cancela se hipótese→SUPERSEDED/REFUTED | SPEC-008 (Scheduler) | SPEC-001 (estados CHM-001) | Indicativa | Mecanismo | Estados da hipótese = CHM-001 (baseline). |

---

## 5. Convicção, confluência e dimensões (WF-C01..C04)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-C01** | Convicção macro × global = um Conviction Vector 8D, duas leituras | **SPEC-003** (candidata v1.1) | SPEC-014, SPEC-015 (invocam) | Candidata | Mecanismo + Decisão | Direção declarada; fórmula/pesos/limiares = J-001; 1x/2x = Q-A5 (WF-D03, aberta). |
| **WF-C02** | Confluência por independência, não por contagem (anti double-counting) | **SPEC-003** (CF-002) | SPEC-002 (representa (in)dependência) | Candidata | Mecanismo | Calibração do desconto = J-001. |
| **WF-C03** | Order flow (CVD/delta/absorção) → dimensão de volume; faltante = INDETERMINADO | **SPEC-003** (CF-007) | SPEC-012 (SMC), SPEC-032 (Volume skill) | Candidata | Mecanismo | Nunca zero/fabricado; disponibilidade por ativo declarada. |
| **WF-C04** | Regime = dimensão de convicção, não gate; **em qual das 8 = SPEC-003** | **SPEC-003** (Q-A9) | SPEC-036 (Market Regime skill) | Candidata/**Aberta (Q-A9)** | Decisão + Mecanismo | A dimensão-alvo é **[DECISÃO NECESSÁRIA: Q-A9]** de Andraus; recomendação research.md §8.3 (Opção A=temporal); não decidida. |

---

## 6. Falhas e estados do ciclo (WF-F01..F02)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-F01** | Seis ramos de falha explícitos | SPEC-015 (Manager) | SPEC-003 (NEUTRO via CF-006), RISK-SPEC (veto) | Indicativa | Mecanismo | Overtrading = externo (WF-X04). |
| **WF-F02** | FSM do ciclo inteiro (determinística, auditável) | SPEC-015 (Manager) | SPEC-008 | Indicativa | Mecanismo | Gate nunca LLM (ENF-03). |

---

## 7. Ativos, calibração e validação (WF-P01..P02, WF-V01..V02)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-P01** | BTC/XAU/NASDAQ em paralelo; heat medido com correlação | Família **RISK-SPEC** (heat) | SPEC-008/SPEC-023 (orquestração) | Indicativa | Mecanismo | `INV-RISK-HEAT`; cálculo no Risk Agent. |
| **WF-P02** | Parâmetros por ativo = mecanismo parametrizável; valores → N-001/backtest | **SPEC-003** (mecanismo, CF-009) | RISK-SPEC | Candidata/**Aberta (N-001)** | Parâmetro editável + Decisão | Valores definitivos = N-001 (aberta). |
| **WF-V01** | Walk-forward + Deflated Sharpe/PBO por regra | SPEC-022 (Cognitive/Adversarial Test) | SPEC-010..013 (regras) | Indicativa | Insumo | Requisito herdado pela **implementação** (BUILD adiado). |
| **WF-V02** | Rótulo de qualidade de evidência por escola, visível no raciocínio | Agentes SPEC-010/011/012/013 (produzem) | **SPEC-003** (preserva, CF-011/D9) | Indicativa/Candidata | Mecanismo | A SPEC-003 não sobrescreve o rótulo; evidência fraca ≠ descartada. |

---

## 8. Risco — insumos ao Risk Agent (WF-X01..X04)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-X01** | Expectância = métrica-raiz; R:R mínimo 1:3 = piso soberano | Família **RISK-SPEC** | — | Indicativa | Mecanismo/Insumo | `INV-RISK-RR` (AGENTS §6.5). |
| **WF-X02** | Sizing pela distância do stop; Kelly adiado; sizing ≠ convicção | Família **RISK-SPEC** | — | Indicativa | Mecanismo | INV-04. |
| **WF-X03** | Fluxo unidirecional convicção→risco; risco nunca retroalimenta convicção | **SPEC-003** (guard CF-008/CF-011) + RISK-SPEC | — | Candidata | Mecanismo | INV-04; guard fail-closed na SPEC-003. |
| **WF-X04** | Prevenção de overtrading = Bot Trade Finance (externo) | — (externo ao SOT) | — | — | Insumo/fronteira | **Sem dona de Spec** — fora do escopo do SOT (ver §IDs sem dona clara). |

---

## 9. Adiado (WF-J01)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-J01** | Decision journal imutável + checkpoint humano (HITL) | SPEC-018 (Learning & Knowledge Formation Governance) | — | Indicativa | Insumo (adiado) | Adiado explicitamente; premissa de WF-K04. |

---

## 10. Valores editáveis `[REVISAR · BL-026]` (WF-R01..R03)

| ID | Resumo | Spec dona primária (consumidora) | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-R01** | TFs por tipo (position/swing/day) — valores-padrão provisórios | SPEC-015 (Mission) | SPEC-008 | Editável (BL-026) | Parâmetro editável | Reconciliar entrada M5 × tabela na revisão (nota da própria WF-R01). |
| **WF-R02** | Killzones ICT em horário de NY — [EXTERNO], fontes divergem | SPEC-008 (Scheduler) | SPEC-015 | Editável (BL-026) | Parâmetro editável | Silver Bullet não adotada ainda. |
| **WF-R03** | Quais Killzones valem por ativo | SPEC-008 (Scheduler) | RISK-SPEC | Editável (BL-026) | Parâmetro editável | Padrão provisório = todas p/ os 3 ativos. |

> BL-026 (RMR-001, `Em espera`) recoloca WF-R01..R03 em pauta no gatilho `spec:SPEC-008 em redação ∨ spec:SPEC-010..015 em redação`. Valor `[REVISAR]` **não é baseline**.

---

## 11. Pontos de decisão (WF-D01..D04)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-D01** | Killzone como mecanismo formal | SPEC-008/SPEC-015 (Manager/Scheduler) | — | **FECHADA** (Andraus) | Decisão | Mecanismo → WF-K01..K04; SPEC-003 não especifica. |
| **WF-D02** | Alarme-gatilho de preço como mecanismo formal | SPEC-008/SPEC-015 | SPEC-003 (consome) | **FECHADA** (Andraus) | Decisão | Mecanismo → WF-A01..A03. |
| **WF-D03** | Convicção macro×global ↔ Conviction Vector 8D / J-001 | **SPEC-003** (mecanismo) + **Andraus** (J-001/Q-A5/Q-A9) | SPEC-014, SPEC-015 | **ABERTA (residual)** | Decisão | Direção em WF-C01; fórmula/pesos/limiares (J-001), 1x/2x (Q-A5), dimensão do regime (Q-A9) seguem abertos. |
| **WF-D04** | Papel do ICT no pipeline | SPEC-013 (Execution/ICT) | SPEC-014 | **FECHADA** (Andraus) | Decisão | ICT = Operacional (WF-05); setup, não hipótese (INV-02). |

---

## 12. Mapeamentos agente↔entidade cognitiva (WF-M01..M03)

| ID | Resumo | Spec dona primária | Secundárias | Estado | Natureza | Nota de fronteira |
|---|---|---|---|---|---|---|
| **WF-M01** | Agente Estrutural ↔ `Structural Agent` (Elliott) | SPEC-010 | — | Indicativa | Decisão/mapeamento | `[INFERÊNCIA]` — confirmar em SPEC-010 (nota da própria WF-M01). |
| **WF-M02** | Agente Institucional ↔ `Institutional Agent` (SMC) | SPEC-012 | SPEC-011 | Indicativa | Decisão/mapeamento | `[INFERÊNCIA]` — confirmar em SPEC-011/012. |
| **WF-M03** | Agente Operacional ↔ `Operational Agent` (ICT, single TF) | SPEC-013 | SPEC-014 | Indicativa | Decisão/mapeamento | `confluence-ict → Operational` confirmado por ADR-CONFLUENCE-001-v3; detalhe SPEC-013/014. |

---

## IDs sem dona clara

| ID | Situação | Encaminhamento |
|---|---|---|
| **WF-X04** | Overtrading é responsabilidade do **Bot Trade Finance** (sistema externo) — não há Spec cognitiva do SOT que o implemente. | Permanece como **fronteira externa**; registrado para que o Risk Agent não o assuma por engano. Não é achado de gate. |
| **WF-V01** | Walk-forward + DSR/PBO é requisito de **implementação/BUILD** (adiado — fase spec-first), não de uma Spec cognitiva específica; associado a SPEC-022 por afinidade, não por mandato. | Reavaliar quando BUILD/SPEC-022 abrir. |
| **WF-07 / WF-P01 / WF-X01..X03** | A **família RISK-SPEC** (BL-018) ainda **não tem slots numerados** no ROADMAP (contingente à EUA-E20). A "dona" é a família, não um `SPEC-0NN` específico. | Dona a numerar na autorização da família RISK (EUA-E20); hoje rastreada por BL-018. |

---

## Conflitos / ambiguidades detectados

| # | Descrição | Impacto | Encaminhamento |
|---|---|---|---|
| **C-1** | **"Manager" é dividido entre dois slots** — SPEC-008 (Cognitive Scheduler: quando/abrir/fechar/alarme) e SPEC-015 (Mission Engine & Lifecycle: síntese de contexto/convicção macro/FSM do ciclo). WF-04/WF-06 falam de "Manager" como ator único. | Médio (rastreabilidade) | O ADR-MANAGER-001 é a fonte do "Manager"; a fronteira SPEC-008 × SPEC-015 só se fixa na abertura dessas Specs. Não fechar aqui. |
| **C-2** | **Acepção concorrente de "Conviction Engine"** (CONFLITO-1 da SPEC-003): WF-04/WF-06 atribuem ao **Manager** o ato de *formar* convicção; a SPEC-003 usa a acepção (a) = componente **separado** que o Manager *invoca*. | Médio (semântico) | Matéria de `WF-D03` (aberta) + RULE-SEM-01; a SPEC-003 declara a acepção sem fechar a reconciliação. Decisão de Andraus. |
| **C-3** | **WF-C04 / Q-A9 em aberto** — a dimensão (das 8) em que o regime entra não está decidida; o Market Regime como skill (SPEC-036) existe como slot distante, o que pode gerar dupla-dona. | Médio | `[DECISÃO NECESSÁRIA: Q-A9]` de Andraus (research.md §8.3). Até lá, INDETERMINADO (CONS-01). |
| **C-4** | **Família RISK-SPEC não numerada** — WF-07/WF-P01/WF-X01..X03 apontam para uma família sem slot `SPEC-0NN` no ROADMAP (contingente à EUA-E20). | Baixo (temporal) | Dona a numerar na EUA-E20; rastreada por BL-018. |
| **C-5** | **WF-R01 auto-inconsistência declarada** — entrada single-TF do WF-05 (ex. M5) × tripla da tabela WF-R01 (day = M15) precisa de reconciliação (a própria WF-R01 pede). | Baixo (editável) | Resolvido na revisão BL-026, não nesta matriz. |

---

> **Reafirmação:** esta matriz é um **índice de rastreabilidade derivado**. Não substitui `WORKFLOW.md`, `ROADMAP.md`, `governance/CATALOGO-OFICIAL.md` nem qualquer baseline (INV-09). Qualquer "Spec dona" marcada Indicativa é expectativa, não atribuição homologada. Regenerar a partir das fontes de verdade sempre que elas mudarem.
