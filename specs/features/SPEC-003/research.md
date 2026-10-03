# SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine — DOSSIÊ DE PESQUISA (ABERTURA)

> **Artefato de ABERTURA de Spec** (RULE-ECC-01/02 — EUA-E21; método em `atomic-spec.md` §15).
> Este documento é o Dossiê de Pesquisa + a Proposta de Definição da SPEC-003.
> **NÃO é o `plan.md`.** O Plan só é escrito após a HOMOLOGAÇÃO de Andraus da definição (ROADMAP §23, passo 1-bis).
> **1ª aplicação da RULE-ECC-05** (Pesquisa Multi-Lente, DHR-ECC05-001) — Dossiê com 3 lentes: Arquitetura + Escola/risco-retorno + confronto com `WORKFLOW.md`.
> **Aplicação da RULE-ECC-04** (Captura Verbatim de Fonte) — arquivos companheiros em `sources/SRC-01..07.txt`.
>
> **NOTA DE DELTA v1.2 (DHR-ARQ-001, 2026-10-01) — não reabre o Dossiê:** o **CONFLITO-1** aqui descrito (acepção concorrente de "Conviction Engine": (a) componente separado × (b) Fase 2 do Manager) foi **dirimido por instrução direta de Andraus** em favor da acepção **(b)**: "Conviction Engine" = **mecanismo (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (Conviction)** (propaga ADR-MANAGER-001 / CEM-001 DIV-CEM-4). Onde este Dossiê discutir o CONFLITO-1 como "reconciliação pendente" ou a SPEC-003 adotando a acepção (a), leia-se: **CONFLITO-1 resolvido pela acepção (b); B-001 parcialmente SUPERSEDIDA na parte "componente separado" (INV-07)**. As recomendações de método/pesquisa (adotar/adaptar/rejeitar/adiar) e Q-A9 **permanecem inalteradas**. Ver `plan.md` v1.2 (CC-10 / Declaração de acepção semântica) e `governance/DHR-ARQ-001`.
>
> **NOTA DE DELTA v1.5 (homologação — DHR-SPEC003-001, 2026-10-02) — não reabre o Dossiê:** na homologação, três **notas de honestidade** (text-only) foram incorporadas ao `plan.md` (ressalvas do parecer do Revisor CONFORME COM RESSALVAS): **N1** composição do Score 0–9 não definida (dona J-001/BL-027); **N2** Salvaguarda de Sinal 1 não materializada como pré-condição do gate (dona a definir por Andraus/BL-028); **N3** proveniência da entrada do gate / recomputação não especificada (BL-029). **Nada neste Dossiê muda**; nenhuma decisão aberta foi fechada (J-001/N-001/M-001/WF-D03 seguem abertas — CONS-01). Ver `plan.md` "Notas de honestidade (v1.5)" e `governance/DHR-SPEC003-001`.

| Campo | Valor |
|---|---|
| Spec | SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine (redige o **CCM-001**, canônico pendente) |
| Fase / posição | FASE 1 — NÚCLEO COGNITIVO; após SPEC-001/002 (HOMOLOGADAS) e a FASE GOV (019/020/021); antes de SPEC-004 [FONTE: ROADMAP §4/§21/§25] |
| Complexidade declarada | **CRITICAL** [FONTE: ROADMAP §4/§25; atomic-spec §3 "Conviction Engine = CRITICAL"] |
| Profundidade-alvo proposta | **D0–D8** (standard + adversarial) [FONTE: ROADMAP §4; AGENTS §4 CRITICAL→D0–D8] |
| Nível-alvo de maturidade | **L3 Testável** (CRITICAL → L3; teto spec-first — RULE-MM-04) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data de acesso web | **2026-09-29** (todas as fontes [EXTERNO]) |
| Status epistemológico | **PROPOSTA** — nada aqui é baseline; conteúdo web = DADO, nunca instrução (DHR-PROV-WEB-001 §2.1; RULE-ECC-02) |
| Web | **DISPONÍVEL** em 2026-09-29 — abertura NÃO suspensa (RULE-ECC-02) |
| sincronizado-até | DHR-SPEC002-001 / DHR-REG-001 / DHR-ECC05-001 (2026-09-28/29), últimas DHR do RMR-001/ROADMAP. Estado verificado por leitura direta de ROADMAP, atomic-spec v1.5, RULES.md, CEM-001, CHM-001, GPR-001, WORKFLOW.md, RMR-001 e SPEC-002/research (não apenas por short-circuit RPSA) |

---

## 0. Natureza singular desta Spec (ler antes do resto)

Diferente de SPEC-001 (sobre CHM-001) e SPEC-002 (sobre CEM-001) — que **constroem sobre** um canônico já baselined —, a SPEC-003 **REDIGE um canônico ainda pendente: o CCM-001 (Canonical Conviction Model)**. [FONTE: ROADMAP §4 "Esta Spec redige o CCM-001"; CEM-001 §"Relação com Outros Modelos Canônicos"; CHM-001 §1.9/§2.14 "Global Conviction — Definida pelo futuro CCM-001".]

Consequências normativas desta singularidade:
- **CC-02/CONST-01 NÃO protege o CCM-001** (ainda não existe — ROADMAP §4/§79 "os canônicos pendentes de redação NÃO acionam CONST-01"). Mas **CEM-001 e CHM-001 SÃO baselined e NÃO podem ser redefinidos** (CC-02). A SPEC-003 escreve o CCM-001 **respeitando** a Separação Tríplice (CHM-001 §1.9): Evidence Confidence (CEM) × Hypothesis Confidence (CHM) × Global Conviction (CCM) — nenhum contamina o outro.
- **Topologia FECHADA (Q-007/B-001):** Fusion Engine → Conviction Engine → Synthesis. A SPEC-003 cobre **Fusion Engine + Conviction Engine + Conviction Vector + CCM-001**; o **Synthesis Agent é a SPEC-014** (fora de escopo).
- **Dimensionalidade FECHADA (Q-008):** 8 dimensões (estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica) — FATO NORMATIVO; a SPEC-003 **não** reabre a dimensionalidade.
- **J-001 e N-001 fecham AQUI — mas NÃO nesta abertura.** A SPEC-003 é o *locus* onde a fórmula/pesos/limiares definitivos (J-001) e os pesos por ativo (N-001) se resolvem; o **fechamento ocorre na homologação do Plan, com prova** — jamais no Dossiê (CONS-01). Ver §4 (GAP-J/GAP-N) e §6 Q-A4.

---

## 1. Questões de pesquisa e estratégia de busca

### 1.1 Questões (o que o Dossiê precisa responder para abrir a SPEC-003)

- **Q-R1 (Arquitetura/método):** Como o estado da arte **funde evidências multi-fonte** e **agrega múltiplas dimensões em um score único** de forma explicável e robusta? (multi-sensor fusion, Dempster-Shafer, Bayes/BMA, ensemble, MCDA/TOPSIS.) O que serve de *referência de método* — sem virar baseline (CCM-001 é o contrato a redigir)?
- **Q-R2 (Escola/risco-retorno):** Como a literatura separa **força/qualidade** e **confiança/calibração** de **convicção**? Como convicção se liga (ou NÃO) a **position sizing/risco-retorno** (Kelly, R-multiple)? (Confronto com INV-04, PC-04, CHM-001 Separação Tríplice.)
- **Q-R3 (Escola técnica):** Como sistemas de trading **ponderam sinais por escola/indicador** (confluência) — e o que colide com a **hierarquia inviolável** Elliott→…→ICT (PC-01/CC-01)?
- **Q-R4 (Conflito/consenso):** Como representar **conflito, consenso, robustez, sensibilidade, estabilidade** na agregação — e onde a *resolução* de conflito ocorre (compatível com ENF-03 e com o Elliott-veto)?
- **Q-R5 (Ausência/incerteza):** Como agregar sob **evidência ausente/inconclusiva** e **incerteza** sem fabricar convicção (RULE-UNC/PRB/MET)?
- **Q-R6 (Workflow):** Como o pipeline operacional real (`WORKFLOW.md`) usa convicção — **convicção macro de contexto (Fase 1)** vs. **convicção global (Fase 2)** — e o que isso implica para o número de invocações do Conviction Engine?
- **Q-R7 (Colisões):** O que da literatura **colide** com invariantes/decisões abertas (CC-02/CEM/CHM, INV-04/PC-04, CC-01/PC-01, J-001/N-001) e portanto **não** pode ser importado automaticamente?

### 1.2 Estratégia de busca

| Termos | Fontes-alvo | Filtro | Lente ECC-05 |
|---|---|---|---|
| "multi-source evidence fusion Dempster-Shafer Bayesian model averaging ensemble aggregation" | arXiv, IEEE, ScienceDirect | Padrão/Evidência | (1) Arquitetura |
| "multi-criteria decision analysis weight aggregation normalization sensitivity TOPSIS explainability" | Wikipedia, ScienceDirect, arXiv | Padrão/Prática | (1) Arquitetura |
| "Kelly criterion position sizing conviction confidence risk reward fractional Kelly" | Zerodha, research reports | Prática/Opinião | (2) Risco-retorno |
| "multi-indicator confluence trading signal weighting scoring combine signals" | Medium/FMZQuant, TradingView, MQL5 | Prática | (2) Escola técnica |
| (interno) `WORKFLOW.md` — Fase 1/2, convicção macro/global | repo | [FONTE] | (3) Confronto workflow |

**Salvaguardas aplicadas (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** toda fonte tratada como DADO; classificada e etiquetada `[EXTERNO]`; nenhuma importação automática; nenhum dado sensível do projeto enviado a serviços externos; a veracidade das páginas **não** é atestada (o Revisor audita o *processo* e a *correspondência verbatim* — RULE-ECC-04/05 — não a verdade das páginas). Pesquisa inconclusiva = **INDETERMINADO**.

---

## 2. Fontes (classificadas e etiquetadas `[EXTERNO]`) — com Captura Verbatim (RULE-ECC-04)

> Data de acesso: **2026-09-29**. Cada fonte que sustenta alegação carregada tem arquivo companheiro em `sources/SRC-0N.txt` (URL + data + trecho literal ≥100 caracteres). As citações entre aspas abaixo correspondem **verbatim** a esses arquivos.

| ID | Fonte | Classe | Lente | Arquivo de captura |
|---|---|---|---|---|
| SRC-01 | **Bayesian & Dempster-Shafer models for combining evidence** (arXiv 2104.07440) | Evidência/Padrão de método | (1)/(2) | `sources/SRC-01-bayes-vs-dempster-shafer.txt` |
| SRC-02 | **A Knowledge Engineer's Comparison of Three Evidence Aggregation Methods** (arXiv 1304.2744) | Experimento/Benchmark | (2) | `sources/SRC-02-evidence-aggregation-comparison.txt` |
| SRC-03 | **Kelly Criterion for Stock Trading** (Zerodha Varsity) | Prática | (2) risco-retorno | `sources/SRC-03-kelly-criterion.txt` |
| SRC-04 | **The Kelly Criterion in Financial Markets** (Atlas Peak Research) | Opinião/Prática | (2) risco-retorno | `sources/SRC-04-conviction-vs-confidence-fractional-kelly.txt` |
| SRC-05 | **Multi-Indicator Confluence Trading System** (FMZQuant/TradingView) | Prática | (2) escola técnica | `sources/SRC-05-confluence-signal-weighting.txt` |
| SRC-06 | **TOPSIS** — MCDA (Wikipedia) | Padrão/Prática | (1) arquitetura | `sources/SRC-06-topsis-mcda-aggregation.txt` |
| SRC-07 | **Sensitivity analysis in MCDA: systematic review** (ScienceDirect) | Padrão/Prática | (1) arquitetura | `sources/SRC-07-mcda-sensitivity-robustness.txt` |

### 2.1 Citações verbatim das fontes carregadas

- **SRC-01 (Bayes vs. Dempster-Shafer) [EXTERNO, Evidência]:** *"The first requires an estimate of the priors and likelihoods while the second only needs an estimate of the posterior probabilities and enables reasoning with uncertain information due to imprecision of the sources and with the degree of conflict between them."*
- **SRC-02 (Comparison of aggregation methods) [EXTERNO, Experimento]:** *"When subjects were performing significantly better than chance, the Dempster-Shafer and Mycin systems performed better than the Bayes systems (95%, 93%, and 85% correct respectively)."*
- **SRC-03 (Kelly) [EXTERNO, Prática]:** *"Kelly % = W – [(1-W)/R] Where, W = Winning probability, R = Win/Loss ratio."*
- **SRC-04 (Convicção × confiança) [EXTERNO, Opinião/Prática]:** *"Confidence is calibration quality, sample size, information advantage, payoff observability, and edge stability; it is not the same as thesis conviction."* — e *"Almost no one takes 100% Kelly—the most successful use 25-50%, balancing math and psychology. Apply a fractional multiplier based on conviction quality, calibration, regime, skew, liquidity, and survivability."*
- **SRC-05 (Confluência ponderada) [EXTERNO, Prática]:** *"Each component votes bullish or bearish with a 0-100 score, the votes are weighted by user-defined importance, and the result is a single confidence percentage."* — e *"In different market environments, some indicators may be more effective than others, necessitating a dynamic weighting mechanism."*
- **SRC-06 (TOPSIS/MCDA) [EXTERNO, Padrão]:** *"It is a method of compensatory aggregation that compares a set of alternatives, normalising scores for each criterion, and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion."*
- **SRC-07 (Sensibilidade MCDA) [EXTERNO, Padrão]:** *"Sensitivity analysis examines how changes in criteria weights or alternative evaluations affect the final ranking. Robustness analysis assesses the stability of the ranking under different scenarios or assumptions."*

---

## 3. Comparação com a arquitetura SOT e os modelos canônicos (adotar / adaptar / rejeitar / adiar)

> Regra: nada entra como baseline; cada item confronta a arquitetura homologada. **CEM-001 e CHM-001 são BASELINE e NÃO podem ser redefinidos (CC-02/CONST-01).** O **CCM-001 é o produto** desta Spec — não há canônico a proteger nele (ROADMAP §79), mas ele deve respeitar as fronteiras dos canônicos vizinhos. Cobertura interna existente é preservada; só se aprofunda o insuficiente (ROADMAP R1/R4/§24).

### 3.1 Lente (1) — ARQUITETURA: o que a arquitetura SOT já fixa (não redefinir) [FONTE]

- **Separação Tríplice (CHM-001 §1.9/§2.14):** Evidence Confidence (CEM) ≠ Hypothesis Confidence (CHM) ≠ Global Conviction (CCM). O CCM-001 calcula a **Global Conviction** e **não** redefine Confidence de hipótese nem Evidence Strength. [FONTE: CHM-001 §1.9, §2.14]
- **CEM-001 já define a entrada do Fusion Engine:** o Fusion Engine é o **único ENGINE PRODUCER** de evidência `DERIVED` (CEM-001 Cap.2/Cap.6), consome apenas evidência `ACTIVE`, usa `Evidence Strength` (peso LOCAL do produtor, 0.0–1.0, ≠ Convicção), `Lineage`/`Cognitive Depth`. [FONTE: CEM-001 Cap.3/Cap.5/Cap.6]
- **SPEC-002 (baseline) já entrega ao Fusion Engine:** provenance, força/qualidade operacional, (in)dependência representada (anti-double-counting, RULE-004), tipologia favorável/contra/inconclusiva/ausente, **detecção e registro de conflito** (nunca resolução). A **resolução/agregação** é da SPEC-003. [FONTE: ROADMAP §4 SPEC-002; SPEC-002/research §5.3]
- **Conviction Vector 8D + PCO-06 (não-redução):** convicção é multidimensional por design; não colapsar em pontuação única quando múltiplas dimensões são relevantes. [FONTE: GPR-001 §2.4 PCO-06; INV-03]
- **PC-04 (piso de convicção) + Salvaguardas de Sinal (CEE-001 §11):** gates NÃO-compensatórios (convicção ≥ 70%, score 7/9, conflito direcional → NEUTRO, R:R 1:3 — limiares de Fase Piloto). [FONTE: GPR-001 §2.1 PC-04; RULE-CEE-004; AGENTS §6]

**Decisão de referência de método (Lente 1):**

| Tema (slot §4) | Fonte externa | Decisão | Porquê |
|---|---|---|---|
| Fusão de evidência multi-fonte (Fusion Engine) | SRC-01, SRC-02 | **ADAPTAR** (método de referência: fusão com conflito/incerteza) + **REJEITAR** adoção automática de DS/Bayes como baseline | SRC-02 mostra que nenhum método é universalmente superior (depende do regime); CCM-001 fixa o CONTRATO, não um algoritmo externo. Calibração numérica → J-001 |
| Agregação multidimensional (8D → convicção) | SRC-06 (TOPSIS/MCDA) | **ADAPTAR** (normalizar por dimensão + ponderar + agregar; explicabilidade) + **REJEITAR** agregação puramente compensatória | TOPSIS é "compensatory aggregation"; o SOT tem gates NÃO-compensatórios (CC-01, CEE-001 §11). O tipo de agregação e os pesos = J-001 |
| Robustez / sensibilidade / estabilidade | SRC-07 | **ADAPTAR** (tratar robustez/sensibilidade/estabilidade como propriedades explícitas e explicáveis — PB-06/PB-08) | Temas listados no slot §4; a métrica definitiva de robustez → J-001 |

### 3.2 Lente (2) — ESCOLA / RISCO-RETORNO

| Tema | Cobertura SOT já existente [FONTE] | Fonte externa | Decisão | Porquê |
|---|---|---|---|---|
| **Força/qualidade vs. convicção** | CEM-001 `Evidence Strength` (local, ≠ Convicção); CHM-001 Separação Tríplice; INV-04 | SRC-04 ("confidence ≠ thesis conviction") | **ADAPTAR** (multidimensionalidade sensível a regime) | Corrobora a Separação Tríplice; nenhuma escala numérica adotada (J-001) |
| **Ponderação de sinais por escola/confluência** | PC-01/CC-01 hierarquia; PCO-06 não-redução; PE-08 independência; AP-02 confluência falsa | SRC-05 (confluência ponderada, pesos dinâmicos) | **ADAPTAR** (agregação ponderada + pesos por regime/ativo = N-001) + **REJEITAR** "votos" simétricos | Hierarquia inviolável: Estrutural (Elliott) tem precedência/veto; dimensões inferiores NÃO sobrepõem a superior (INV-01). Pesos = J-001/N-001 |
| **Position sizing / risco-retorno (Kelly, R-multiple)** | INV-04 (custo NUNCA no Conviction Vector); INV-RISK-RR/HEAT/LEV; família RISK-SPEC (BL-018) | SRC-03 (Kelly), SRC-04 (Kelly fracionário) | **ADIAR** (sizing/alavancagem/R:R → Risk Agent, não Conviction Engine) | INV-04: convicção ≠ score/custo. A convicção 8D é INSUMO do Risco; o dimensionamento é a jusante (RISK-SPEC), fora do escopo da SPEC-003 |

### 3.3 Lente (3) — CONFRONTO COM `WORKFLOW.md` [FONTE]

O pipeline declarado por Andraus usa convicção em **dois momentos**:
- **Fase 1 — convicção macro de contexto** (Manager, após Agente Estrutural + Institucional): Estrutural + Institucional. [FONTE: WORKFLOW.md WF-04]
- **Fase 2 — convicção global** (Manager, após Agente Operacional na Killzone): + Operacional; decide envio e monta risco-retorno. [FONTE: WORKFLOW.md WF-06]

**Onde a SPEC-003 toca o workflow (identificado, NÃO resolvido — WORKFLOW-SOT-001):**
1. A SPEC-003 é o motor que **forma ambas** as convicções (macro e global). **Ponto de atenção central desta abertura → §5.7 e Q-A5.**
2. A relação **convicção-macro/convicção-global ↔ Conviction Vector 8D/J-001** é um dos 4 pontos abertos de **WORKFLOW-SOT-001** — a SPEC-003 o **toca diretamente** (as duas convicções são subconjuntos/instâncias do vetor 8D?), mas **não o fecha** (decisão de Andraus; ROADMAP §32).
3. **Killzone** e **alarme-gatilho de preço** (mecanismos ainda não formais — WORKFLOW-SOT-001): a SPEC-003 **não** os especifica (são do Manager/Scheduler — SPEC-008/015); apenas reconhece que a convicção macro é pré-condição do alarme-gatilho. **Mantidos abertos.**
4. **Papel do ICT** no pipeline (WORKFLOW-SOT-001): irrelevante para a agregação de convicção em si (ICT não cria hipótese — INV-02; ICT executa), mas a **dimensão operacional** da convicção global relaciona-se ao Agente Operacional (M5). **Mantido aberto** — a SPEC-003 não decide onde ICT entra.
5. **Tensão terminológica [DECISÃO NECESSÁRIA]:** CEM-001 (notas DIV-CEM-3/4, ADR-MANAGER-001) diz que o "Conviction Engine" foi **absorvido pelo Manager Agent (Fase 2)**; o ROADMAP/B-001 trata o **Conviction Engine como componente SEPARADO** (Fusion→Conviction→Synthesis). O nome "Conviction Engine" tem **acepção concorrente** (RULE-SEM-01): (a) motor autônomo do Kernel (ROADMAP); (b) Fase 2 do Manager (ADR-MANAGER-001). A SPEC-003 **não** reconcilia isso sozinha → §4 CONFLITO-1 / Q-A6.

---

## 4. Lacunas, conflitos e INDETERMINADOS (NÃO fecham decisão aberta — CONS-01)

- **CONFLITO-1 — "Conviction Engine" separado (ROADMAP/B-001) vs. absorvido pelo Manager Fase 2 (CEM-001/ADR-MANAGER-001).** Acepção concorrente (RULE-SEM-01). **Não resolver na abertura** — é matéria de WORKFLOW-SOT-001 + de como a SPEC-003 nomeia o componente. **[DECISÃO NECESSÁRIA — Q-A6]**. Registrado, não suprimido (PB-09).
- **CONFLITO-2 — agregação compensatória (TOPSIS/confluência ponderada) vs. gates não-compensatórios do SOT.** SRC-05/SRC-06 sugerem agregação compensatória e "votos" simétricos; o SOT impõe hierarquia (CC-01/PC-01) e Salvaguardas (CEE-001 §11). **Resolução na Spec:** a agregação do Conviction Vector deve preservar precedência estrutural e os gates de sinal — **rejeitar** compensação pura. Não é decisão aberta nova (já normado por CC-01/CEE-001 §11). [FONTE: RULE-CEE-004; INV-01]
- **CONFLITO-3 — importar framework externo (DS/Bayes/MCDA) como baseline vs. CCM-001 canônico a redigir.** **Rejeitar** adoção automática; admitir só como **referência de método**. O CCM-001 é o contrato canônico (redigido pela SPEC-003, sob GMC-001). [FONTE: SRC-02; GMC-001; CC-02 vizinhos]
- **CONFLITO-4 — position sizing por convicção (Kelly) vs. INV-04.** Ligar convicção a dimensionamento/custo dentro do Conviction Vector violaria INV-04. **Rejeitar**; sizing → Risk Agent (RISK-SPEC). [FONTE: INV-04; SRC-03/04]
- **GAP-J (J-001) — fórmula/pesos/limiares DEFINITIVOS.** A SPEC-003 é o *locus* de fechamento, mas os **definitivos são pós-backtest** (fase de implementação; BUILD/VERIFY adiados — ROADMAP §22). **[DECISÃO NECESSÁRIA: J-001]** — a abertura NÃO fecha; ver Q-A4 (o que "fechar J-001" significa em spec-first: estrutura+método+limiares-piloto interinos vs. números definitivos). INDETERMINADO quanto aos números definitivos. [FONTE: J-001; RULE-EV-05; RULE-MM-06]
- **GAP-N (N-001) — pesos por ativo (BTC/XAU/NASDAQ).** Parte de J-001 pós-backtest. **[DECISÃO NECESSÁRIA: N-001]** — a SPEC-003 especifica o **mecanismo** de pesos por ativo (que o CCM-001 deve suportar), não os **valores** (backtest). Não fechada na abertura. [FONTE: N-001; atomic-spec §12]
- **GAP-M (M-001) — estados do Blackboard para objetos não-hipótese** (Evidência/Convicção): a publicação do Conviction Vector no Blackboard depende de M-001 (SPEC-004, aberta). A SPEC-003 referencia; não fecha. **[DECISÃO NECESSÁRIA: M-001]** [FONTE: atomic-spec §12; RULE-BB-003]
- **GAP-FUSION-DEP — mecânica de desconto de evidências dependentes.** SPEC-002 representa a (in)dependência; a **mecânica** de fusão de dependentes (evitar double-counting) é do Fusion Engine (SPEC-003). A SPEC-003 especifica o **contrato**; a **calibração** do desconto → J-001. [FONTE: SPEC-002/research GAP-2; RULE-004]
- **GAP-WORKFLOW (WORKFLOW-SOT-001) — 4 pontos** (Killzone, alarme-gatilho, relação convicção-macro/global↔8D, papel do ICT): a SPEC-003 **toca** o 3º ponto (convicção macro/global ↔ 8D) e o motor 1x/2x (§5.7); **não fecha nenhum**. [FONTE: WORKFLOW.md §"Termos que precisam de reconciliação"; ROADMAP §32]

Nenhuma decisão aberta é fechada por esta pesquisa (RULE-ECC-02 / CONS-01).

---

## 5. Proposta de Definição da SPEC-003 (para homologação de Andraus)

### 5.1 Número, nome, quantidade, decomposição — [PROPOSTA]

- **Número:** **SPEC-003** (slot mantido; número monotônico, não reutilizado — RULE-ECC-01).
- **Nome:** **Conviction Vector, Evidence Fusion Engine & Conviction Engine** (mantido) — a Spec **redige o CCM-001**.
- **Quantidade / decomposição:** **decisão material para Andraus.** Duas opções [PROPOSTA]:
  - **Opção A (recomendada): 1 (uma) Spec CRITICAL não decomposta.** Fusion Engine, Conviction Engine, Conviction Vector 8D e CCM-001 formam **um contrato de convicção coeso** — a fusão produz o insumo (evidência DERIVED) que o Conviction Engine agrega no vetor 8D; separá-los fragmentaria o mesmo objeto canônico (CCM-001) e multiplicaria fronteiras internas sem ganho de atomicidade (ROADMAP §24). A topologia B-001 (Fusion→Conviction) é sequencial e fortemente acoplada.
  - **Opção B: 2 Specs** (SPEC-003 Fusion Engine + evidência DERIVED; SPEC-003b Conviction Engine + Conviction Vector + CCM-001). *Contra:* o CCM-001 precisaria ser referenciado por ambas antes de existir; a fusão sem o modelo de convicção fica sem consumidor especificado. **Não recomendada.**
  - *Recomendação do Especificador:* **Opção A.** Ver Q-A1.

### 5.2 Missão (comportamental, sem implementação) — [PROPOSTA]

Especificar **como o SOT funde evidências independentes/dependentes em evidência derivada e agrega a convicção em um Conviction Vector de 8 dimensões explicável, robusto e auditável** — redigindo o **CCM-001 (Canonical Conviction Model)** como contrato canônico da Convicção Global —, preservando a Separação Tríplice (Evidence Strength × Hypothesis Confidence × Global Conviction), a hierarquia analítica inviolável (Estrutural tem precedência/veto), as Salvaguardas de Sinal não-compensatórias (CEE-001 §11), e a fronteira INV-04 (custo/dimensionamento NUNCA entram na convicção), entregando o vetor de convicção ao Synthesis Agent (SPEC-014) sem executar decisão nem dimensionar risco.

### 5.3 Escopo (dentro) — [PROPOSTA]

1. **CCM-001 (Canonical Conviction Model):** redigir o contrato canônico da Convicção Global (identidade, campos, imutabilidade/versionamento, relação com CEM/CHM via Separação Tríplice, governança GMC-001). É o produto central.
2. **Evidence Fusion Engine (contrato operacional):** como o Fusion Engine consome evidência `ACTIVE` (CEM-001), produz evidência `DERIVED` (único ENGINE PRODUCER autorizado), trata (in)dependência/desconto (anti-double-counting, RULE-004 — mecânica; calibração → J-001), avaliação de impacto de invalidação (CEM-001 Cap.4/5), Cognitive Depth.
3. **Conviction Engine (contrato operacional):** como o Conviction Engine agrega em **Conviction Vector 8D** (estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica): escalas, normalização, pesos (mecanismo; valores → J-001/N-001), independência/correlação, ausência/contraevidência/conflito/consenso, robustez/sensibilidade/aging/estabilidade, agregação, limites, incerteza, cálculo da convicção global, **explicabilidade** (PB-06).
4. **Preservação da hierarquia e das Salvaguardas:** agregação **não-compensatória** onde CC-01/CEE-001 §11 exigem (Estrutural precede; conflito direcional → NEUTRO; gates de sinal). Elliott-veto preservado (RULE-SY-001).
5. **Fronteira de convicção macro vs. global** (WORKFLOW.md): o CCM-001 deve suportar convicção computada sobre **subconjuntos de dimensões** (macro: Estrutural+Institucional) e sobre o **vetor completo** (global: +Operacional) — **o mecanismo**, deixando a decisão 1x/2x e o mapeamento definitivo para WORKFLOW-SOT-001/Q-A5.
6. **Enforcement Contracts** dos atos com efeito (publicação do vetor; commit de convicção que habilita Decision): piso **E2** (Evidência/Engine — atomic-spec §10.2); **E3** no gate Convicção→Decisão (crítico; fail-closed — trava J-001, ver §5.6).
7. **Classe/Mecanismo por BASpec** (RULE-MECH-01/CC-11) e **Auditabilidade (D9 por referência)** para reconstrução da convicção (P13).

### 5.4 Fora do escopo (Non-goals) — [PROPOSTA]

- Redefinir **CEM-001** ou **CHM-001** (estrutura, campos, ciclo de vida, Separação Tríplice) — **CC-02/CONST-01**.
- **Synthesis Agent / árbitro / TMP** → **SPEC-014** (a jusante do Conviction Engine — B-001).
- **Fechar os valores definitivos** de fórmula/pesos/limiares (J-001) e pesos por ativo (N-001) — dependem de backtest (implementação); a Spec fixa **estrutura/mecanismo/limiares-piloto interinos**, não os números definitivos. Ver Q-A4.
- **Position sizing, alavancagem, R:R, Portfolio Heat** → **Risk Agent / família RISK-SPEC** (INV-04/INV-RISK-*).
- **Estados do Blackboard** para objetos não-hipótese → **M-001 / SPEC-004**. **Storage físico / Knowledge Graph** → **SPEC-004/006 (H-001)**.
- **Killzone, alarme-gatilho de preço, decisão 1x/2x, papel do ICT no pipeline** → **WORKFLOW-SOT-001** (Manager/Scheduler — SPEC-008/015) — a SPEC-003 apenas dá suporte de mecanismo, não decide.
- Método de observação de **falso-DENY** (ENF-07) — a especificar no CCM-001 (BL-002), mas o **fechamento** só se dá na homologação (não na abertura).

### 5.5 Capacidades §26 cobertas

- Cobre integralmente a capacidade **"SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine"** (ROADMAP §26). Capacidades a jusante (síntese/TMP → SPEC-014; risco/sizing → RISK-SPEC; storage → SPEC-004/006) permanecem em seus slots — **não** são achados de gate.

### 5.6 Herança prevista (a declarar no Plan — CC-08 / RULE-HV / RULE-HD) — [PROPOSTA]

- **INHERITS (por ID+versão baseline — RULE-HD-04):** **CEM-001** (baseline, DHR-TAX-001 — evidência de entrada; Fusion Engine como ENGINE PRODUCER); **CHM-001** (baseline — Separação Tríplice, Global Conviction "definida pelo futuro CCM-001", Hypothesis Confidence intocada); **SPEC-001 v1.1** (slot de convicção referenciado pela hipótese); **SPEC-002 baseline** (evidência operacional, conflito/independência detectados que alimentam a fusão); **atomic-spec v1.5**; **ENF-01..08** (ênfase ENF-03/ENF-04/ENF-07); **GPR-001** (PC-01, PC-04, PCO-06, PB-06/08); **INV-01/03/04/06/07/09/10**; **4Es** (CEE-001 §12); **Salvaguardas CEE-001 §11**.
- **ADDED:** o CCM-001 (novo canônico) + a camada operacional Fusion/Conviction (itens §5.3).
- **REMOVED:** vazio (nada suprimido do herdado — RULE-HD-03).
- Eixo vertical (RULE-HV): a SPEC-003 não é filha direta de macro-spec da FASE GOV; herança é sobre modelos canônicos vizinhos (CC-08) — a confirmar no Plan.

### 5.7 PONTO DE ATENÇÃO CENTRAL — o Conviction Engine roda 1x ou 2x? [DECISÃO NECESSÁRIA]

O `WORKFLOW.md` mostra convicção sendo formada em **dois momentos** (macro de contexto na Fase 1; global na Fase 2). Isto suscita uma pergunta arquitetural que a SPEC-003 **toca mas não pode fechar** (é parte de WORKFLOW-SOT-001):

- **Interpretação (a):** **um único** Conviction Engine / CCM-001, **consumido em 2 momentos** — a convicção macro é o vetor 8D calculado sobre o **subconjunto** de dimensões disponíveis na Fase 1 (Estrutural+Institucional); a convicção global é o **mesmo** motor sobre o vetor completo (+Operacional). Vantagem: um só contrato canônico; consistência; explicabilidade única.
- **Interpretação (b):** **dois** cálculos/instâncias distintos de convicção (macro ≠ global como objetos separados), possivelmente com pesos/limiares diferentes por fase.

**Recomendação do Especificador [INFERÊNCIA]:** a interpretação (a) — motor/CCM-001 único, invocado em 2 momentos sobre subconjuntos de dimensões — é a mais coerente com PCO-06 (não-redução), com a dimensionalidade fechada de 8 (Q-008) e com a Separação Tríplice. Mas **isto não é fechado aqui**: é uma decisão de Andraus (WORKFLOW-SOT-001), registrada em Q-A5. A SPEC-003 deve, no mínimo, **especificar o mecanismo** que suporta convicção sobre subconjuntos e sobre o vetor completo, sem petrificar a decisão de invocação (que pertence ao Manager/Scheduler).

### 5.8 Avaliação de aplicabilidade das regras de método (explícita — não em silêncio)

**(1) RULE-ECC-05 / Pesquisa Multi-Lente — INCIDE (1ª aplicação).** [FONTE: RULES RULE-ECC-05; atomic-spec §15]
- A SPEC-003 é explicitamente citada na RULE-ECC-05 (Conviction/Fusion Engine que agrega convicção estrutural/institucional/operacional e fecha J-001/N-001). Dossiê com 3 lentes: (1) Arquitetura §3.1; (2) Escola/risco-retorno §3.2; (3) confronto com WORKFLOW.md §3.3. **Aplicada.**

**(2) RULE-MECH-01 / CC-11 (Classe D/H/P/C por BASpec) — INCIDE.** [FONTE: RULES RULE-MECH-01; ROADMAP §33]
- SPEC-003 é "SPEC-002 em diante". Cada BASpec com efeito declara Classe no Plan. **Preview [INFERÊNCIA, a confirmar no Plan]:** normalização/agregação determinística do vetor = **Classe D**; gate Convicção→Decisão (piso de convicção, conflito direcional→NEUTRO, score 7/9) = **Classe C** (constitutivo, fail-closed, E3); fusão de evidências dependentes / cálculo de convicção com julgamento = **Classe H** (LLM+gate determinístico) ou **P** (julgamento qualitativo + bounded loop). Declaração por BASpec, nunca por Spec (SES-001 §50).

**(3) RULE-PD-01 / CC-12 (PD-xx por Spec de especialidade) — PROPOSTA de N/A, mas com nuance — CONFIRMAR Q-A3.** [FONTE: RULES RULE-PD-01; atomic-spec §10.7]
- **Justificativa de N/A [PROPOSTA]:** RULE-PD-01 incide quando a Spec **define escopo de especialidade** (Elliott/SMC/ICT — julgamento de uma escola de mercado). O Conviction/Fusion Engine é **infraestrutura de agregação transversal e domain-agnostic** — agrega convicções produzidas pelas escolas, mas **não é** uma escola analítica. Análogo a SPEC-002 (camada operacional domain-agnostic). Os `PD-xx` serão declarados pelas Specs analíticas SPEC-010..014.
- **Nuance honesta para o Revisor/Andraus (RULE-MET-01):** a RULE-ECC-05 aplicar-se à SPEC-003 (por "tocar comportamento de trading") **não** implica automaticamente que RULE-PD-01 aplique — são gatilhos distintos (ECC-05 = "toca comportamento de trading/agrega convicção"; PD-01 = "define escopo de especialidade"). Contudo, como a SPEC-003 introduz metodologia de convicção/fusão com escolhas de domínio (agregação não-compensatória, pesos por ativo), há um argumento para `PD-xx` de "metodologia de convicção" (não de escola de mercado). **Deixo como decisão de Andraus (Q-A3)**, recomendando N/A pela natureza transversal.

**(4) RULE-MM-01 (escada de maturidade L0–L4, gate normativo E3) — INCIDE.** [FONTE: RULES RULE-MM-01/04/05]
- SPEC-003 declara **nível-alvo L3 Testável** (CRITICAL → L3; teto spec-first — RULE-MM-04). Gate E3 na homologação (RULE-MM-05); progressão staged (RULE-MM-03); atribuição determinística (RULE-MM-02); **sem limiar numérico dependente de convicção** (RULE-MM-06 — coerente com J-001 aberto).

**(5) RULE-ECC-04 (Captura Verbatim) — INCIDE e JÁ APLICADA.** [FONTE: RULES RULE-ECC-04]
- 7 fontes carregadas → 7 arquivos `sources/SRC-01..07.txt` (URL + data 2026-09-29 + trecho ≥100 chars); citações verbatim no §2.1; método honesto onde WebFetch falhou (SRC-02 PDF binário; SRC-05 Medium 403; SRC-07 ScienceDirect 403 — RULE-MET-01). O Revisor verifica correspondência de string (sem web).

**(6) RULE-REG-001 (registro físico das 11 famílias) — NÃO INCIDE / JÁ RESOLVIDA.** As 11 famílias RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET já foram **registradas fisicamente** em `RULES.md` na abertura da SPEC-002 (DHR-REG-001, 2026-09-28; atomic-spec v1.5 consolidado). Nada a propor aqui.

### 5.9 Re-apontamento de gatilhos RMR-001 (passo 11-bis / RULE-ECC-01)

- **Nenhum re-apontamento de slot necessário:** o slot SPEC-003 é **mantido** (não dividido/fundido/renumerado/descartado) — RULE-ECC-01 não exige re-apontamento. *(Se Andraus escolher a Opção B do §5.1 — 2 Specs —, então há divisão de slot e ESTE Dossiê propõe re-apontamento aditivo do gatilho de BL-004 para ambas; registrar via Controlador. Sob a Opção A recomendada, nada muda.)*
- **Itens do RMR-001 e o efeito desta ABERTURA (redação da SPEC-003):**
  - **BL-004** (Fórmula/pesos/limiares do Conviction Vector; gatilho `spec:SPEC-003 em redação`): **DISPARA com esta abertura** → **ATIVADO**. Encaminhamento: **absorvido pela SPEC-003** — o item descreve exatamente o trabalho da Spec (redigir CCM-001; fechar J-001/N-001). O **fechamento** de J-001/N-001 ocorre na **homologação do Plan** (não na abertura — CONS-01). Registrar no gate: BL-004 tratado, não pendente.
  - **BL-002** (Falso-DENY observável, ENF-07; gatilho `spec:SPEC-003 homologada` ∨ `decisao:J-001 resolvida`): **não dispara na abertura**; **IMINENTE** — dispara na **homologação** da SPEC-003. Encaminhamento previsto: definir método de observação de falso-DENY no CCM-001 (a tratar no Plan/homologação).
  - **BL-003** (`spec:SPEC-004 em redação`): **não dispara**.
  - **BL-012** (MC-COG-001; gatilho `spec:SPEC-002 homologada`): **já tratado** na homologação da SPEC-002 (fora do escopo desta abertura).
  - **BL-017** (`spec:SPEC-007/014/038 em redação`): **não dispara** (não inclui SPEC-003).
  - Nenhum item fica `ATIVADO` sem encaminhamento por esta abertura (BL-004 tratado como absorvido; a abertura não é homologação de Spec — o passo 11-bis pleno ocorre na homologação da SPEC-003).

---

## 6. Perguntas que Andraus precisa decidir (homologação da definição — ROADMAP §23 passo 1-bis)

- **Q-A1 (quantidade/decomposição):** Aprova **SPEC-003 como 1 Spec CRITICAL não decomposta** (Opção A — Fusion Engine + Conviction Engine + Conviction Vector 8D + CCM-001 num contrato coeso), com o escopo §5.3 e os non-goals §5.4? Ou prefere a Opção B (2 Specs)? **[DECISÃO NECESSÁRIA]**
- **Q-A2 (profundidade-alvo):** Confirma **D0–D8** (CRITICAL, tratamento adversarial de conflito/ausência/robustez/agregação não-compensatória — AGENTS §4)? **[DECISÃO NECESSÁRIA]**
- **Q-A3 (RULE-PD-01/CC-12):** Confirma que a SPEC-003 **NÃO declara `PD-xx`** por ser infraestrutura de agregação transversal/domain-agnostic (mesmo padrão de SPEC-002), deixando `PD-xx` para SPEC-010..014 — apesar de RULE-ECC-05 incidir? Ou entende que a metodologia de convicção justifica `PD-xx` de "convicção/fusão"? (ver nuance §5.8-3) **[DECISÃO NECESSÁRIA]**
- **Q-A4 (escopo de J-001/N-001 em spec-first):** O que significa "a SPEC-003 **fecha** J-001 e N-001" na fase spec-first (BUILD/VERIFY adiados — ROADMAP §22)? Proposta do Especificador: a SPEC-003 fecha a **estrutura/método de agregação + os limiares-piloto interinos** (≥70%, 7/9 — já FATO NORMATIVO interino) e especifica o **mecanismo** de pesos/robustez/pesos-por-ativo, mas os **valores/pesos definitivos** permanecem **[DECISÃO NECESSÁRIA]** pós-backtest (implementação). Confirma este recorte, ou exige mais/menos? **[DECISÃO NECESSÁRIA — não fecho J-001/N-001 nesta abertura, CONS-01]**
- **Q-A5 (motor 1x ou 2x — WORKFLOW-SOT-001):** Reconhece o ponto de atenção §5.7 (convicção macro de contexto vs. convicção global) como parte de WORKFLOW-SOT-001, a **permanecer aberto**, com a SPEC-003 apenas fornecendo o **mecanismo** de convicção sobre subconjuntos e sobre o vetor completo (sem decidir a invocação, que é do Manager/Scheduler)? **[DECISÃO NECESSÁRIA — mantido aberto]**
- **Q-A6 (terminologia "Conviction Engine" — CONFLITO-1):** Como a SPEC-003 deve nomear/posicionar o componente, dada a acepção concorrente (motor separado do Kernel — ROADMAP/B-001 × Fase 2 do Manager Agent — CEM-001/ADR-MANAGER-001)? A reconciliação é parte de WORKFLOW-SOT-001 — confirma que a SPEC-003 **declara a acepção que usa (RULE-SEM-01)** sem fechar a reconciliação global? **[DECISÃO NECESSÁRIA — mantido aberto]**
- **Q-A7 (ECC-VAL-001):** Validade deste Dossiê (acesso 2026-09-29) antes da redação do Plan? (Precedente SPEC-002/020: 30 dias corridos OU início do Plan, o que ocorrer primeiro — só para esta Spec; ECC-VAL-001 permanece aberta como regra geral.) **[DECISÃO NECESSÁRIA]**
- **Q-A8 (M-001):** Confirma que o protocolo de publicação do Conviction Vector no Blackboard **referencia M-001 como aberta** (não fecha estados do Blackboard para não-hipótese), a fechar em SPEC-004? **[DECISÃO NECESSÁRIA]**

---

## 6-bis. Registro de Homologação da Definição de Abertura (Andraus, 2026-10-01)

Todas as 8 perguntas APROVADAS por Andraus. Parecer do Revisor: **CONFORME** (0 Crítico/Médio, 1 Menor não-bloqueante — A-01, linguagem imprecisa sobre BL-012, corrigida abaixo).

- **Q-A1 — RESOLVIDA:** Opção A aprovada. 1 Spec CRITICAL, não decomposta.
- **Q-A2 — RESOLVIDA:** D0–D8 confirmado.
- **Q-A3 — RESOLVIDA:** Confirmado N/A. `PD-xx` não incide (infraestrutura de agregação transversal).
- **Q-A4 — RESOLVIDA:** Recorte aprovado. SPEC-003 fecha estrutura/método + limiares-piloto interinos; valores/pesos definitivos permanecem `[DECISÃO NECESSÁRIA]` pós-backtest.
- **Q-A5 — RESOLVIDA (abertura) e depois FECHADA por Andraus (DHR-DEC-001, 2026-10-01):** na abertura, o nº de invocações ficou aberto (parte de `WORKFLOW-SOT-001`), com a SPEC-003 só fornecendo o mecanismo. **Atualização (delta v1.3):** por decisão direta de Andraus, **Q-A5 está FECHADA — 2x por ciclo** (macro Fase 1 / global Fase 2; WF-C01 v2.1). Para a SPEC-003 isso é **dado de entrada herdado de WF-C01**: a Spec continua só fornecendo o mecanismo (CF-010) e **não** implementa nem é dona da invocação (é do Manager — SPEC-008 Fase 1 / SPEC-014 Fase 2). `WF-D03` segue ABERTA no resíduo J-001/N-001 + Q-A9; a invocação sai do resíduo.
- **Q-A6 — RESOLVIDA:** Confirmado. SPEC-003 declara a acepção que usa (RULE-SEM-01) sem fechar CONFLITO-1; reconciliação permanece em `WORKFLOW-SOT-001`.
- **Q-A7 — RESOLVIDA:** Confirmado. 30 dias/início do Plan — Plan inicia hoje, dentro da validade.
- **Q-A8 — RESOLVIDA:** Confirmado. M-001 referenciada como aberta.

**Correção do achado A-01:** `BL-004` (gatilho `spec:SPEC-003 em redação`) é absorvido por esta abertura — fecha definitivamente na homologação do Plan. `BL-012` permanece `ATIVADO`, tratado separadamente por Andraus (não bloqueia esta Spec).

**Abertura da SPEC-003 HOMOLOGADA.** Próximo passo: Especificador redige `plan.md`/`checks.md`.

---

## 7. Autoverificação da abertura (RULE-ECC-02/04/05 — parte determinística)

```
[x] Web disponível em 2026-09-29 → abertura NÃO suspensa (RULE-ECC-02).
[x] Dossiê presente e completo (CRITICAL): questões+estratégia; fontes classificadas e [EXTERNO]; data de acesso; comparação adotar/adaptar/rejeitar/adiar; lacunas/conflitos; escopo/quantidade/número; re-apontamento avaliado (BL-004 ATIVADO/absorvido).
[x] RULE-ECC-05 (3 lentes) aplicada: (1) Arquitetura §3.1; (2) Escola/risco-retorno §3.2; (3) confronto WORKFLOW.md §3.3. 1ª aplicação da regra.
[x] RULE-ECC-04 aplicada: 7 arquivos sources/SRC-01..07.txt (URL+data+trecho ≥100 chars); citações verbatim no §2.1; método de captura honesto onde WebFetch falhou (RULE-MET-01).
[x] Conteúdo web tratado como DADO; nenhuma importação automática; nada vira baseline (DHR-PROV-WEB-001 §2.1).
[x] CC-02/CONST-01: CEM-001 e CHM-001 NÃO redefinidos; CCM-001 é o produto (canônico pendente, não protegido — ROADMAP §79) e respeita a Separação Tríplice.
[x] Nenhuma decisão aberta fechada (CONS-01): J-001, N-001, M-001, WORKFLOW-SOT-001, ECC-VAL-001, ECC-03-001 permanecem abertas; INDETERMINADO usado (GAP-J/N/WORKFLOW).
[x] Fronteiras SOT respeitadas: CC-01/PC-01 (hierarquia — Estrutural precede/veto; agregação não-compensatória), INV-04 (convicção ≠ custo/sizing), INV-06 (Evidência≠Observação), INV-10 (CEM idioma), ENF-03 (LLM detector≠gate), 4Es, CEE-001 §11.
[x] Regras de método avaliadas explicitamente (§5.8): ECC-05 INCIDE (1ª); MECH-01 INCIDE; PD-01 N/A proposto (Q-A3); MM-01 INCIDE (alvo L3); ECC-04 INCIDE+aplicada; REG-001 já resolvida (SPEC-002).
[x] Etiquetagem aplicada: [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO].
[x] RULES.md / ROADMAP / atomic-spec NÃO editados (RULE-HG-01/02) — abertura só propõe; homologação é de Andraus.
[x] NÃO é o Plan — Plan adiado à homologação da definição (ROADMAP §23 passo 1-bis).
```

**Pronto para revisão (do Dossiê de abertura).** O Revisor audita presença/estrutura/classificação/etiquetagem/comparação/ausência de importação automática + **presença das 3 lentes (RULE-ECC-05)** + **correspondência verbatim** das citações com `sources/` (RULE-ECC-04, sem web) — não a veracidade das páginas (atomic-spec §15). A homologação da definição é de Andraus, antes do Plan. **Nenhuma decisão aberta (J-001/N-001/WORKFLOW-SOT-001) é fechada por esta abertura.**

---

## 8. Nota de delta v1.1 — reconciliação ao `WORKFLOW.md` (versão vigente) [FONTE]

> **Natureza:** este Dossiê foi homologado (§6-bis) quando o setup operacional ainda estava sob a forma anterior (quatro pontos abertos em `WORKFLOW-SOT-001`). Posteriormente, Andraus **fechou** três desses pontos e **declarou a direção** do quarto (DHR-WF-002, versão vigente da `WORKFLOW.md`). Esta nota registra o delta **sem reescrever** §0–§7 (artefato de abertura, histórico/imutável — RCN-001/INV-07) e **sem fechar** nenhuma decisão aberta (CONS-01). É o insumo de abertura do delta `plan.md`/`checks.md` v1.1. Nada aqui é baseline novo.

### 8.1 O que mudou no setup operacional (fonte soberana = `WORKFLOW.md`, versão vigente)

| Ponto de `WORKFLOW-SOT-001` (como o Dossiê §3.3/§4 o via) | Estado na versão vigente da `WORKFLOW.md` | Efeito na SPEC-003 |
|---|---|---|
| Killzone como mecanismo formal | **WF-D01 FECHADA** (WF-K01..K04; tabelas WF-R02/R03 editáveis) | **Fora do escopo** — Manager/Scheduler (SPEC-008/015). A SPEC-003 **não** especifica Killzone. Deixa de ser "ponto aberto". |
| Alarme-gatilho de preço como mecanismo formal | **WF-D02 FECHADA** (WF-A01..A03, FSM determinística) | **Fora do escopo** — Manager (SPEC-008/015). O `parent_id`/objeto do alarme é **consumido**, não produzido (CF-013/WF-A01). |
| Papel do ICT no pipeline | **WF-D04 FECHADA** (ICT = Agente Operacional, WF-05; produz **setup operacional**, não hipótese — INV-02) | **Fora do escopo** — agentes (SPEC-010..014). A SPEC-003 não decide onde o ICT entra. |
| Relação convicção-macro/global ↔ Conviction Vector 8D | **WF-D03 ABERTA (residual)** — direção declarada em **WF-C01** (um vetor 8D, duas leituras) | A SPEC-003 **toca** e fornece o **mecanismo** (CF-010), **sem** fechar fórmula/pesos/limiares (J-001), nº de invocações 1x/2x (Q-A5) nem a dimensão do regime (Q-A9). |

**Consequência de escopo (CONS-01):** `WF-D01/D02/D04` deixam de ser tratadas como pontos abertos de `WORKFLOW-SOT-001`; **`WF-D03` permanece a única aberta (residual)**. A reclassificação é de *fronteira*, **não** de mérito: as BASpecs/EARS/Enforcement/Classe da SPEC-003 **não mudam** (o delta v1.1 é declarativo).

### 8.2 IDs `WF-xx` que a SPEC-003 passa a citar por ID (mecanismo-apenas — RULE-ECC-05 lente 3)

A versão vigente acrescentou regras operacionais nomeadas que o Dossiê original (§3.3) só descrevia como "Fase 1/Fase 2". O delta v1.1 do `plan.md` incorpora-as **por ID, sem invadir** Manager/Risk/J-001: **WF-C01** (macro×global = um vetor, duas leituras → CF-010), **WF-C02** (confluência por independência → CF-002), **WF-C03** (order flow → dimensão de volume, INDETERMINADO → CF-007), **WF-C04** (regime = dimensão, não gate → Q-A9), **WF-X03**/INV-04 (fluxo unidirecional convicção→risco → CF-008/CF-011), **WF-A01** (parent_id consumido → CF-013), **WF-V02** (rótulo de evidência por escola preservado → CF-011/D9), **WF-P02**/N-001 (parâmetros por ativo = mecanismo → CF-009). Todos **existem** na versão vigente; nenhum é contraditado; nenhuma `WF-Dxx` aberta é tratada como fechada.

### 8.3 Q-A9 (NOVA) — em qual das 8 dimensões entra o **regime** (WF-C04)? [DECISÃO NECESSÁRIA — mantida aberta]

**Contexto [FONTE]:** `WF-C04` (versão vigente) declara que o **regime** (tendência / range / alta volatilidade) é **dimensão de convicção, não gate**, e **deixa para a SPEC-003** definir **em qual das 8 dimensões fechadas** (estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica — Questionário v1) ele entra. A SPEC-003 **conforma-se ao princípio** (regime não é gate; não cria 9ª dimensão — INV-03/PCO-06) mas **não decide** a dimensão-alvo: é decisão de Andraus. Enquanto não decidida, o mapeamento é **INDETERMINADO** (não fabricar — RULE-MET-01/CONS-01).

> **Delimitação honesta (RULE-MET-01):** "regime" **não é** a dimensão `volume`. A dimensão `volume` é especificamente order flow (CVD/delta/absorção) por **WF-C03/CF-007**; mapear regime a `volume` confundiria dois conceitos distintos. Por isso `volume` não figura entre as opções abaixo.

| Opção | Dimensão-alvo | Argumento a favor | Risco / contra |
|---|---|---|---|
| **A** | **temporal** | Regime é o **estado/fase de mercado vigente no tempo** em que a estrutura se desenrola — contexto temporal, não hipótese estrutural. Preserva INV-01 (regime não afeta o veto de Elliott). | Pode confundir "fase temporal da onda" (Elliott) com "regime de mercado"; exige definição clara de `temporal`. |
| **B** | **histórica** | Regime é frequentemente **inferido do comportamento histórico/estatístico** do ativo (persistência de tendência, vol. realizada). Encaixa em "dimensão histórica". | Regime é um estado **corrente**, não só histórico; pode subrepresentar o regime intradiário. |
| **C** | **estrutural** | Regime (tendência vs. range) correlaciona-se com a leitura estrutural (impulso vs. correção). | **Rejeitada como recomendação:** arriscaria contaminar a dimensão que detém precedência/veto (INV-01/CC-01) — regime passaria indevidamente a influenciar o veto de Elliott. |
| **D** | **esclarecimento** (nenhuma única — modulador transversal) | Regime poderia **modular pesos/normalização** de várias dimensões, não ser uma única. | **Exige decisão de Andraus**: `WF-C04` pede "em qual das 8"; um modulador transversal extrapola o enunciado e aproxima-se de J-001/N-001 (pesos) — fora do que a Spec pode fixar. |

**Recomendação do Especificador [INFERÊNCIA — não decisão]:** **Opção A (temporal)** — é o mapeamento que melhor preserva a hierarquia inviolável (regime como contexto temporal, jamais como fonte de veto direcional, INV-01) e evita contaminar a dimensão estrutural. A decisão é de Andraus (WF-C04/WF-D03). Até lá, **INDETERMINADO** (CONS-01); o `plan.md` registra Q-A9 como `[DECISÃO NECESSÁRIA]` e **não** mapeia o regime a nenhuma dimensão.

> **Aprofundamento de pesquisa (2026-10-01, instrução de Andraus):** o dossiê dedicado **`research-Q-A9-regime.md`** (não-normativo) aprofunda Q-A9 com estado da arte e melhor prática de trading (classificação de regime, ADX/ATR/HMM/MS-GARCH, uso como filtro×sizing×feature, regime em Elliott/SMC-ICT, MTF, evidência empírica em BTC/ouro/Nasdaq, armadilhas de lag/overfitting/double-counting) e fontes `sources/SRC-R01..R04` (RULE-ECC-04). Conclusão convergente: **Opção A (temporal) recomendada**, Opção B (histórica) alternativa, Opção C (estrutural) rejeitada (contamina o veto INV-01), Opção D (modulador transversal) só mediante reinterpretação de WF-C04 por Andraus. **Q-A9 permanece ABERTA** — decisão de Andraus (CONS-01). **Decisão de Andraus (chat, 2026-10-01):** Q-A9 **permanece ABERTA e fica a cargo da SPEC-003** (a Spec decide em qual das 8 dimensões entra o regime), usando `research-Q-A9-regime.md` (não-normativo, [EXTERNO]) como **fonte de dados**; a recomendação do dossiê (temporal) é insumo, não decisão.

### 8.4 Gatilhos RMR-001 e validade do Dossiê

- **Sem re-apontamento de slot:** o slot SPEC-003 permanece **mantido** (não dividido/fundido/renumerado) — RULE-ECC-01 não exige re-apontamento. O delta v1.1 é de conformidade a `WORKFLOW.md`, não de redefinição de escopo.
- **BL-026** (`Em espera`; valores editáveis WF-R01..R03; gatilho `spec:SPEC-008 em redação ∨ spec:SPEC-010..015 em redação`): **não dispara** pela SPEC-003 (esta Spec não consome WF-R01..R03 — Killzone/TFs são do Manager/agentes). Registrado para visibilidade. [FONTE: DHR-WF-002 §1/§4]
- **Validade do Dossiê (Q-A7):** o `plan.md` já estava dentro da validade (Plan iniciado 2026-10-01). O delta v1.1 ocorre no **mesmo dia** — dentro da validade; nenhuma re-pesquisa web é exigida (o delta é reconciliação a fonte interna soberana, não novo estado da arte). ECC-VAL-001 permanece aberta como regra geral.

### 8.5 Status epistemológico desta nota

[FONTE]: a reclassificação WF-D01/D02/D04 FECHADAS, WF-D03 ABERTA e os conteúdos WF-C/X/A/V/P citados — origem `WORKFLOW.md` (versão vigente) e DHR-WF-002. [PROPOSTA]: o mapeamento recomendado de Q-A9 (Opção A). [DECISÃO NECESSÁRIA]: Q-A9 (dimensão do regime), Q-A5 (invocação 1x/2x), J-001, N-001 — **nenhuma fechada aqui**. [INFERÊNCIA]: a recomendação Opção A e a coerência (a)↔WF-C01.

---

## 9. Nota de delta v1.4 — Q-A9 (dimensão do regime) DECIDIDA pela SPEC-003 [FONTE]

> **Natureza:** este Dossiê de abertura (§0–§8) é **histórico/imutável** (RCN-001/INV-07) e **não é reescrito**. Esta nota registra apenas que a questão **Q-A9**, que §8.3 deixou como `[DECISÃO NECESSÁRIA — a cargo da SPEC-003]`, foi **decidida pela SPEC-003** no `plan.md`/`checks.md` **v1.4**, por delegação direta de Andraus (chat, 2026-10-01: "Spec decide: temporal + corrigir F-01"), em resposta à interpelação **I-01** do Revisor (parecer **CONFORME** v1.3). Nada aqui fecha outra decisão aberta (CONS-01).

- **Q-A9 — decidida:** o **regime de mercado** (tendência/range/alta volatilidade, WF-C04) é hospedado na dimensão **`temporal`** do Conviction Vector 8D (**Opção A** de §8.3 e de `research-Q-A9-regime.md` §7). É **dimensão de convicção, não gate, não veto** (WF-C04/INV-01), **não** cria 9ª dimensão (INV-03), **não** toca custo/sizing (INV-04). **Opção C (estrutural) rejeitada** (contaminaria o veto de Elliott — INV-01; double-counting tendência×estrutural). **Opção D (modulador transversal) não adotada** (extrapolaria WF-C04; só com reinterpretação de Andraus).
- **Status:** decidida **por delegação**; **ratifica na homologação** da SPEC-003 (ata `governance/DHR-DEC-002`). Enquanto não homologada, não é escrita como "FECHADA" (CONS-01).
- **Limitação declarada (RULE-MET-01):** a evidência [EXTERNO] de regime-por-dimensão é **Moderada/Fraca** — `research-Q-A9-regime.md` rebaixou SRC-R03 (abstracts; Springer 303 não-fetchada) e SRC-R04 (snippets de WebSearch). A decisão é **arquiteturalmente defensável**, não forte-empírica.
- **Resíduo que permanece ABERTO (CONS-01):** o **peso/limiar** do regime na dimensão `temporal` = **J-001/N-001** (pós-backtest); **WF-D03** permanece ABERTA no resíduo **J-001/N-001** (regime sai do resíduo — a dimensão foi decidida; a invocação já saíra por Q-A5/DHR-DEC-001). **M-001** (estados do Blackboard) e **SPEC-015-SCOPE** seguem abertas.
- **Materialização no Plan v1.4 (sem renumerar BASpecs):** RULE-CF-003 estendida (regime→temporal); CCM-001 skeleton + I/O (campo de regime dentro da `temporal`; INDETERMINADO se não classificável — nunca zero); CF-004/CF-007/CF-009 ajustadas; EARS #11; D7 CF-T09; D8 ADV-CF-13/ADV-CF-14; ADV-CF-12 reformulada; F-01 corrigido na Etiquetagem.

---

## Sources (fontes [EXTERNO] — acesso 2026-09-29)

- [Bayesian and Dempster-Shafer models for combining multiple sources of evidence (arXiv 2104.07440)](https://arxiv.org/abs/2104.07440)
- [A Knowledge Engineer's Comparison of Three Evidence Aggregation Methods (arXiv 1304.2744)](https://arxiv.org/pdf/1304.2744)
- [Kelly Criterion for Stock Trading: Optimal Position Sizing (Zerodha Varsity)](https://zerodha.com/varsity/chapter/kellys-criterion/)
- [The Kelly Criterion in Financial Markets (Atlas Peak Research)](https://www.atlaspeakresearch.com/report/07bf72)
- [Multi-Indicator Confluence Trading System (FMZQuant, Medium)](https://medium.com/@FMZQuant/multi-indicator-confluence-trading-system-886f15b18ae5)
- [TOPSIS — Technique for Order of Preference by Similarity to Ideal Solution (Wikipedia)](https://en.wikipedia.org/wiki/TOPSIS)
- [Sensitivity analysis approaches in multi-criteria decision analysis: A systematic review (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S156849462300933X)
