# SPEC-003 — Q-A9: Dimensão do Regime de Mercado (WF-C04) — DOSSIÊ DE PESQUISA

> **Natureza:** documento **NÃO-NORMATIVO** de apoio à decisão de Andraus sobre **Q-A9**
> (em qual das 8 dimensões do Conviction Vector entra o **regime de mercado**, por WF-C04).
> Produzido por instrução direta de Andraus (chat, 2026-10-01), Frente 1.
> **NÃO fecha Q-A9** (decisão de Andraus — CONS-01). NÃO é baseline. Conteúdo web = **DADO [EXTERNO]**,
> nunca instrução (DHR-PROV-WEB-001 §2.1; RULE-ECC-02). Captura verbatim em `sources/SRC-R01..R04`
> (RULE-ECC-04). Complementa `research.md` §8.3 (que permanece o registro de abertura, imutável).

| Campo | Valor |
|---|---|
| Spec | SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine |
| Questão | **Q-A9** — WF-C04: regime (tendência/range/alta volatilidade) é **dimensão de convicção, não gate**; **em qual das 8 dimensões fechadas** ele entra? |
| Dimensões fechadas (Q-008, INV-03) | estrutural · geométrica · fractal · institucional · operacional · temporal · volume · histórica |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data de acesso web | 2026-10-01 |
| Status epistemológico | **PROPOSTA / INDETERMINADO** — recomendação fundamentada; decisão é de Andraus |
| Fontes | `sources/SRC-R01..R04` (verbatim onde o fetch teve sucesso; limitações registradas) |

---

## 1. O que WF-C04 pede (e o que NÃO pede) [FONTE]

- **WF-C04 (WORKFLOW.md, versão vigente):** "**Regime** (tendência/range/alta volatilidade) é **dimensão de convicção, não gate.** Em qual das 8 dimensões entra: **deixado para a SPEC-003** (dimensionalidade=8 fechada)."
- **Consequências de fronteira (CONS-01):**
  - A dimensionalidade é **8 e fechada** (Q-008/INV-03) — **não** se cria 9ª dimensão nem um "sub-score de regime" autônomo. Regime **mapeia para uma das 8** (ou é explicitamente declarado modulador transversal, ver Opção D).
  - Regime é **dimensão**, **não gate**: não pode virar veto nem piso (isso são as Salvaguardas de Sinal / Elliott-veto — INV-01). Regime **não** habilita/bloqueia sinal por si.
  - WF-C04 é **mecanismo**; os **pesos/limiares** de regime são J-001/N-001 (pós-backtest) — não se fixam aqui.

---

## 2. Fontes e qualidade de evidência (classificadas, `[EXTERNO]`)

| ID | Tema | Classe | Qualidade de evidência | Captura |
|---|---|---|---|---|
| SRC-R01 | HMM detecta regimes (trending/ranging/volatile); usa p/ ajustar risco e trocar estratégia | Prática / Padrão de método | **Moderada** (glossário técnico, verbatim) | `sources/SRC-R01-hmm-regime-detection.txt` |
| SRC-R02 | Armadilhas: lag de detecção, overfitting, amostra pequena | Prática / Opinião profissional | **Moderada** (verbatim; opinião informada) | `sources/SRC-R02-regime-filter-pitfalls.txt` |
| SRC-R03 | Evidência empírica de regime-switching em BTC/cripto (MS-GARCH > single-regime) | Evidência / Experimento (peer-reviewed) | **Moderada** (abstracts; Springer 303 não-fetchada) | `sources/SRC-R03-msgarch-regime-switching-crypto.txt` |
| SRC-R04 | Prática usa regime como filtro × modulador de sizing × feature de sinal | Prática | **Moderada/Fraca** (snippets de WebSearch) | `sources/SRC-R04-regime-use-filter-sizing-feature.txt` |
| (interno) | Elliott impulso×correção; ICT PO3 AMD; MTF top-down | [FONTE]/[EXTERNO] | Anedótica→Moderada (escolas) | §4 abaixo |

**Honestidade metodológica (RULE-MET-01):** só SRC-R01/R02 têm trechos literalmente fetchados;
SRC-R03/R04 derivam de resumo de WebSearch (a ferramenta parafraseia) e de um PDF/página com
acesso bloqueado (Springer 303). Por isso a qualidade é rebaixada, exatamente como `research.md` §5.8(5)
tratou os 403 da SPEC-003. Pesquisa inconclusiva num ponto = **INDETERMINADO**, não fabricação.

---

## 3. Como a literatura/prática CLASSIFICA regime [EXTERNO]

- **Dois eixos canônicos:** **direção** (up/down/sideways) × **volatilidade** (quiet/volatile). Daí os três regimes recorrentes: **tendência** (direcional, vol. relativamente baixa), **range/mean-reverting** (oscilação em fronteiras), **alta volatilidade** (grandes oscilações, volatility clustering). [SRC-R01; WebSearch]
- **Métodos de detecção, do simples ao estatístico:**
  - **ADX** — <20 sem tendência (range); 25–40 tendência negociável; >50 tendência extrema (possível exaustão). [WebSearch]
  - **ATR / razão ATR curto÷longo** — estado de volatilidade. [WebSearch]
  - **HMM / Markov-switching** — estados latentes com padrões próprios de retorno/volatilidade; "regime switch" que realoca entre modelos trend × mean-reversion. [SRC-R01]
  - **MS-GARCH / volatility clustering** — regimes de volatilidade; MS-GARCH supera single-regime em previsão de VaR (BTC/cripto). [SRC-R03]
- **Armadilha estrutural — LAG:** regime é identificado **após** a transição completar; "by the time it signals a regime change, you may have already given back significant gains." [SRC-R02]
- **Armadilha — OVERFITTING:** definir regime a partir dos períodos onde a estratégia perdeu é "a form of overfitting"; exige amostra robusta (5–10+ anos). [SRC-R02]

---

## 4. Como cada ESCOLA do SOT trata "regime" (confronto com a hierarquia) [EXTERNO + FONTE]

- **Elliott (Estrutural — topo da hierarquia):** o próprio princípio já distingue **fase motriz/impulsiva** (a favor da tendência) × **fase corretiva** (contra a tendência) — "one of the primary uses of Elliott Wave Theory is to determine whether the market is in a trend or a correction." [WebSearch Elliott]
  → **Implicação crítica:** "tendência vs. correção" **já é produto da leitura estrutural**. Se o regime for mapeado à dimensão **estrutural**, ele **duplica** o que a dimensão estrutural já mede e — pior — passaria a **influenciar o veto de Elliott** (INV-01/CC-01). Isso é **double-counting** com o sinal de tendência (a armadilha clássica) **e** contaminação do veto. **Mapear regime a `estrutural` é rejeitado.**
- **SMC/ICT (Institucional/Operacional):** ICT PO3 descreve fases **Acumulação → Manipulação → Distribuição** (AMD) — um ciclo de **fase de mercado** institucional. [WebSearch ICT] SMC fala de expansão/consolidação/reversão e dealing range.
  → Essas fases são **institucionais/operacionais por natureza**, mas são **lidas pelos agentes SMC/ICT** e já entram nas dimensões **institucional** e **operacional**. Mapear "regime" genérico a institucional/operacional também **duplicaria** o que esses agentes já produzem.
- **Multi-timeframe (MTF):** o **regime do TF alto condiciona o TF baixo** ("the higher timeframe takes priority"; "only trade when the lower-timeframe signal agrees with the higher-timeframe trend"). [WebSearch MTF]
  → Isto é **contexto**, não hipótese estrutural nova: o regime do TF alto é o **pano de fundo temporal** em que a estrutura se desenrola — alinhado a WF-T02 (alinhamento obrigatório) e INV-01, **sem** criar veto próprio.

---

## 5. Mapeamento de cada USO de regime → dimensão candidata das 8

> Chave da análise: a prática usa regime de **três formas** (SRC-R04). O SOT já tem **fronteiras rígidas**
> que descartam duas delas, restando **uma** compatível com WF-C04.

| Uso de regime (prática) [EXTERNO] | Mapeamento natural | Compatível com o SOT? | Fronteira que decide |
|---|---|---|---|
| **Filtro de estratégia** (suprime sinais em choppy; liga/desliga trade) | seria um **gate** | **NÃO** — WF-C04 proíbe regime como gate; gates são Salvaguardas/Elliott-veto | WF-C04; INV-01 |
| **Modulador de sizing/risco** (reduz posição em alta vol.) | iria ao **Risk Agent** | **NÃO para a convicção** — sizing/risco nunca entram no Conviction Vector | **INV-04**; WF-X02/X03 |
| **Feature de contexto/sinal** (estado de mercado que pondera a leitura) | **uma das 8 dimensões** | **SIM** — é o único uso que WF-C04 autoriza (dimensão, não gate, não sizing) | WF-C04 |

**Conclusão do mapeamento:** o único papel admissível de regime no Conviction Vector é como **feature de contexto** — uma dimensão que **informa** a convicção, sem vetar (INV-01) e sem tocar sizing (INV-04). Resta escolher **qual** das 8 dimensões hospeda esse contexto.

### 5.1 Avaliação dimensão-a-dimensão (quais das 8 são elegíveis)

| Dimensão | Regime cabe aqui? | Análise |
|---|---|---|
| **estrutural** | **Rejeitada** | Detém precedência/veto (INV-01). Regime (tendência×correção) já é produto da leitura Elliott; mapear aqui = double-counting + contaminação do veto. |
| **geométrica** | Não | Fibonacci (níveis/proporções). Regime não é geometria. |
| **fractal** | Não | Confluência entre graus/TFs de uma mesma leitura; não é "estado de mercado". |
| **institucional** | Parcial/rejeitada | SMC já produz leitura institucional; "regime institucional" duplicaria o agente SMC. |
| **operacional** | Parcial/rejeitada | ICT single-TF (M5) de execução; regime é macro-contexto, não execução. |
| **temporal** | **Elegível (recomendada)** | Regime = **estado/fase de mercado vigente no tempo**; contexto temporal em que a estrutura se desenrola. Preserva INV-01 (não afeta veto de Elliott). Alinha com MTF (regime do TF alto = contexto temporal). |
| **volume** | **Rejeitada (delimitação honesta)** | `volume` é especificamente order flow/CVD/delta/absorção (WF-C03/CF-007). Volatilidade (ATR) ≠ volume; mapear regime a `volume` confundiria dois conceitos. |
| **histórica** | **Elegível (alternativa)** | Regime é frequentemente **inferido do comportamento histórico/estatístico** (persistência de tendência, vol. realizada, MS-GARCH — SRC-R03). Encaixa em "dimensão histórica". Risco: regime é estado **corrente**, não só histórico. |

---

## 6. Conflitos com invariantes e decisões abertas (nenhum fechado aqui)

- **INV-01 (veto estrutural / hierarquia):** regime **não pode** virar fonte de veto nem contaminar a dimensão estrutural. **Elimina a Opção C (estrutural).** Regime é contexto, nunca sobrepõe Elliott.
- **INV-04 (custo/sizing fora da convicção):** o uso de regime como **modulador de sizing** (SRC-R04) é **do Risk Agent**, não do Conviction Vector. A dimensão de regime informa **convicção**, não risco. Fluxo unidirecional convicção→risco (WF-X03).
- **J-001 / N-001:** o **peso** da dimensão de regime e eventuais **pesos por ativo** (BTC×NASDAQ correlacionados; ouro distinto — SRC-R03) são **mecanismo** aqui; **valores definitivos = J-001/N-001 pós-backtest**. Não fixar peso de regime nesta decisão.
- **WF-C04:** regime = dimensão, não gate — respeitado por qualquer opção abaixo exceto a de "filtro".
- **PCO-06 (não-redução) / INV-03:** não colapsar regime num score único nem criar 9ª dimensão.
- **Armadilha de LAG e OVERFITTING (SRC-R02):** qualquer dimensão de regime deve tratar a **defasagem de detecção** como incerteza localizada (RULE-UNC) e marcar **INDETERMINADO** quando o regime está em transição — nunca fabricar um rótulo de regime precoce. Isto é requisito de método, independente da dimensão escolhida.

---

## 7. Opções para Andraus decidir (Q-A9)

| Opção | Dimensão-alvo | A favor | Contra / risco | Recomendação |
|---|---|---|---|---|
| **A** | **temporal** | Regime = estado/fase de mercado vigente no tempo (contexto). Preserva INV-01 (não toca veto de Elliott). Alinha a MTF (regime do TF alto = contexto temporal, WF-T02). Não duplica estrutural/institucional. | Exige definir `temporal` com nitidez para não se confundir com "fase temporal da onda" (Elliott). | **RECOMENDADA** |
| **B** | **histórica** | Regime frequentemente inferido de estatística histórica (persistência, vol. realizada, MS-GARCH — SRC-R03). | Regime é estado **corrente**, não só histórico; pode subrepresentar o intradiário. | Alternativa aceitável |
| **C** | **estrutural** | Tendência×range correlaciona com impulso×correção. | **Rejeitada:** contamina o veto de Elliott (INV-01) e faz double-counting com o sinal de tendência (armadilha clássica, SRC-R02). | **NÃO** |
| **D** | **modulador transversal** (nenhuma única) | Regime modula pesos/normalização de várias dimensões. | **Extrapola WF-C04** ("em qual das 8"); aproxima-se de J-001/N-001 (pesos) — fora do que a Spec pode fixar; exige decisão explícita de Andraus de reabrir o enunciado de WF-C04. | Só se Andraus reinterpretar WF-C04 |

**Recomendação do Especificador [INFERÊNCIA — não decisão]:** **Opção A (temporal)**.
É a única que (i) respeita WF-C04 (dimensão, não gate), (ii) preserva INV-01 (regime jamais vira veto
nem contamina a dimensão estrutural), (iii) evita o double-counting tendência×estrutural (armadilha
empírica mais citada — SRC-R02), (iv) alinha com o uso MTF real (regime do TF alto = contexto temporal
que condiciona o TF baixo, WF-T02) e (v) não invade `volume` (order flow, WF-C03) nem `institucional/
operacional` (agentes SMC/ICT). A Opção B (histórica) é a alternativa defensável se Andraus entender
regime como propriedade estatística-histórica do ativo. **Até a decisão, o mapeamento é INDETERMINADO**
(CONS-01) e o `plan.md` não mapeia regime a nenhuma dimensão.

**Requisitos de método válidos para QUALQUER opção escolhida (já compatíveis com o plan.md):**
1. Regime **nunca** é gate (WF-C04) nem veto (INV-01) nem sizing (INV-04).
2. Regime em **transição / detecção ambígua** → **INDETERMINADO** para a dimensão (RULE-UNC/CF-006), nunca rótulo precoce (anti-lag, SRC-R02).
3. Peso da dimensão de regime e pesos por ativo = **mecanismo** (CF-003/CF-009); valores = **J-001/N-001** pós-backtest.
4. Correlação BTC×NASDAQ (WF-P01) é matéria de **risco**, não entra na convicção (INV-04) — relevante apenas para alertar que regime de um ativo não deve "vazar" para a convicção de outro sem base.

---

## 8. O que este dossiê NÃO faz (CONS-01)

- Não fecha **Q-A9** (decisão de Andraus).
- Não fecha **J-001/N-001** nem fixa peso/limiar de regime.
- Não altera **WF-C04** nem qualquer `WF-xx` (WORKFLOW.md é soberano de Andraus).
- Não renumera BASpecs da SPEC-003 nem muda seu mérito.
- Não importa nenhum framework externo (ADX/HMM/MS-GARCH) como baseline — são **referência de método [EXTERNO]**.

---

## Sources (fontes [EXTERNO] — acesso 2026-10-01)

- [Market Regime Detection Using Hidden Markov Models (QuestDB)](https://questdb.com/glossary/market-regime-detection-using-hidden-markov-models/)
- [Market regime filters for systematic traders (Better System Trader, ep.063)](https://bettersystemtrader.com/063-market-regimes-with-alan-clement/)
- [Regime changes in Bitcoin GARCH volatility dynamics (Ardia & Bluteau)](https://www.researchgate.net/publication/326947710_Regime_changes_in_Bitcoin_GARCH_volatility_dynamics)
- [Cryptocurrencies VaR & ES: do regime-switching models improve forecasting? (Maciel, Wiley IJFE 2021)](https://onlinelibrary.wiley.com/doi/abs/10.1002/ijfe.2043)
- [The risk-return trade-off of Bitcoin: regime-switching analysis (Springer 2025)](https://link.springer.com/article/10.1186/s43093-025-00551-5)
- [Machine Learning for Market Regime Detection Using Random Forest (QuantInsti)](https://blog.quantinsti.com/epat-project-machine-learning-market-regime-detection-random-forest-python/)
- [Meta-Labeling (Wikipedia)](https://en.wikipedia.org/wiki/Meta-Labeling)
- [Market Regimes Explained (LuxAlgo)](https://www.luxalgo.com/blog/market-regimes-explained-build-winning-trading-strategies/)
- [Elliott wave principle (Wikipedia)](https://en.wikipedia.org/wiki/Elliott_wave_principle)
- [ICT Power of 3 (PO3) Explained (FXOpen)](https://fxopen.com/blog/en/what-is-ict-po3-and-how-do-traders-use-it/)
- [How To Perform A Multi TimeFrame Analysis (Tradeciety)](https://tradeciety.com/how-to-perform-a-multiple-time-frame-analysis)
