# Tutorial técnico — Pine Script, backtest e calibração como suplemento do SOT

> **Destinatário:** o Claude Code que mantém este repositório (SOT‑Harness).
> **Status:** referência **NÃO‑normativa** (`reference/externo/`). Não é baseline, não fecha decisão aberta, não autoriza implementação. Escrito em 2026‑10‑03 a partir de uma execução **real** no gráfico BTCUSDT (H4), descrita na §3.
> **Pré‑requisito:** leia antes `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` (como conectar ao TradingView). Este documento assume a conexão pronta e trata do que vem depois: **criar, editar, backtestar e calibrar Pine Script** e **onde isso serve ao SOT**.

---

## 0. Leia antes de usar (limites que não se negociam)

| # | Limite | Fonte |
|---|---|---|
| L1 | O `ROADMAP.md` §22 proíbe especificar agora código, APIs e implementação; BUILD/VERIFY‑de‑código estão adiados. Um script Pine, hoje, é **evidência exploratória de viabilidade**, nunca artefato de Spec nem baseline. | `ROADMAP.md` §22; `AGENTS.md` cabeçalho "Fase atual" |
| L2 | **Dono do backtest/calibração = BL‑032, ABERTO.** Opções registradas: ampliar a SPEC‑018 **ou** criar slot novo "Backtest & Calibração". Não escolha; proponha. | `specs/features/SPEC-038/research.md` §7 |
| L3 | **J‑001** (fórmula/pesos/limiares definitivos do Conviction Vector) e **N‑001** (pesos por ativo) seguem abertas. Nenhum número deste tutorial vira limiar. | `AGENTS.md` §7; `SPEC-003/plan.md` |
| L4 | **Termos de uso do TradingView:** o Dossiê da SPEC‑038 propõe **rejeitar** a conexão automatizada (dados licenciados só para exibição; "algorithmic decision‑making" vedado). `SPEC-038-TVMCP-001` e `SPEC-038-DATASRC-001` estão **abertas**, decisão de Andraus. Ler resultados do Strategy Tester por CDP é coleta automatizada: cai na mesma objeção. | `SPEC-038/ABERTURA.md` §4 e §8 |
| L5 | Backtest é **evidência condicionada**, nunca prova (período, ativo, timeframe, regime, custos, slippage, look‑ahead, overfitting, múltiplos testes, estabilidade temporal). | `governance/SES-001_Especializacao_Cognitiva_Trading.md` §16 |
| L6 | Antes de qualquer calibração: `RULE‑CTF‑01` (declarar baseline, intervenção mínima, **anti‑hindsight**) e `WF‑V01` (**walk‑forward + Deflated Sharpe/PBO por regra**). | `governance/RULES.md`; `WORKFLOW.md` WF‑V01 |
| L7 | Você (Claude Code) **não edita** `ROADMAP.md`, `CATALOGO-OFICIAL.md`, `RMR-001` nem Specs baselined. Encaminhamentos saem como `[PROPOSTA]` para Andraus. | `AGENTS.md` §5 |

> **Honestidade de leitura:** este mapa foi montado lendo `ROADMAP.md`, `SPEC-038/{ABERTURA,research}.md`, trechos de `SPEC-003/plan.md`, `SES-001` §16, `WORKFLOW.md` WF‑V01/V02, `RULES.md` e `docs/fundamentos/ARIA-plano-mestre.md`. Para **SPEC‑017, 018, 021, 022, 025, 039, 040, 041, 042** li apenas o resumo do slot no `ROADMAP.md`; o encaixe nelas está marcado como **[INFERÊNCIA]**.

---

## 1. Onde Pine Script suplementa o SOT (mapa por Spec, backlog e função)

Legenda: **[LIDO]** = confirmado em texto do repositório · **[INFERÊNCIA]** = deduzido do slot no ROADMAP.

### 1.1 SPEC‑038 — Trading Analysis Tool Harness [LIDO]
Slot: "TradingView; Pine Script; OHLC; volume; indicadores; gráficos; dados derivados; cálculo". Cada ferramenta declara `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas`.

**O que o teste real entrega aqui:** a prova de que existem **quatro "ferramentas Pine" distintas**, cada uma pedindo um contrato próprio (§5):

| Ferramenta (tipo SPEC‑038) | Natureza | Risco |
|---|---|---|
| Injetar código no editor | **efeito** (sobrescreve o editor) | Classe C, fail‑closed |
| Compilar / adicionar ao gráfico | **efeito** (altera o layout do usuário; pode abrir diálogo de salvar) | Classe C |
| Ler métricas do Strategy Tester | **leitura** (Observação) | Classe D |
| Alterar entradas do script | **efeito leve** (reversível) | Classe D/C |

Mapeia a BL‑017 (*tool correctness ↔ SPEC‑038*; fecha por emenda à SPEC‑020 **na homologação** da SPEC‑038 — `ABERTURA.md` §9) e a BL‑031 (viabilidade do TradingView↔SOT).

### 1.2 BL‑032 → J‑001 / N‑001 (SPEC‑003 / CCM‑001) [LIDO]
`SPEC-003/plan.md` diz que a calibração numérica é **condição de BUILD (backtest)**, não de homologação. Os limiares‑piloto (`≥70%` convicção, `≥7/9` score) e as regras `RULE‑003`, `RULE‑EW‑002`, `RULE‑SY‑003` são "recalibráveis após backtest".

**Como o Pine ajuda:** é o **ambiente de experimento** onde se codificam as regras de cada escola e se mede o efeito de cada parâmetro. **Como NÃO ajuda:** o Strategy Tester não calcula DSR/PBO nem separa treino/teste sozinho (§4).

### 1.3 SPEC‑018 — Learning & Knowledge Formation Governance [INFERÊNCIA]
Ciclo do slot: `Extração → Formalização → Validação → Backtest → Stress Test → Sandbox → Aprovação → Produção`. O fluxo executado (§3) cobre quatro etapas:

| Etapa SPEC‑018 | O que foi feito de fato |
|---|---|
| Formalização | Regra escrita como código Pine v6 |
| Validação | Compilação sem erros; leitura das métricas |
| Backtest | Strategy Tester, 187 operações |
| Stress Test (embrião) | Variação de EMAs e do múltiplo de ATR |

Faltam Sandbox/Aprovação/Produção, e faltou o rigor de §4.

### 1.4 SPEC‑010 / 011 / 012 / 013 — Elliott, Fibonacci/Fractal, SMC, ICT [LIDO em WF‑V01/V02; INFERÊNCIA nas Specs]
`WF‑V01`: ao codificar regras de Elliott/SMC/ICT, exigir walk‑forward + DSR/PBO **por regra**. `WF‑V02`: rótulo de qualidade de evidência por escola (Elliott: regras falseáveis, contagem subjetiva; Fibonacci: só em confluência; SMC/ICT: fraca/anedótica).

**Uso do Pine:** transformar a parte **falseável** de cada escola em estratégia isolada, por camada. O próprio `docs/fundamentos/ARIA-plano-mestre.md` (fonte documentada, **não homologada** — TRACE‑06) já propõe estratégias separadas (Elliott, SMC, combinada com score 0‑9) e uma "arquitetura de backtesting em 3 camadas": Pine Strategy → simulação de score em Python → walk‑forward real. Trate como **referência de desenho**, não decisão.

### 1.5 SPEC‑017 — Pattern Memory [INFERÊNCIA]
Campos do slot: episódio, setup, contexto, resultado, win rate, R:R, amostra, confiança estatística, segmentação por ativo/regime/timeframe. As métricas do tester (`total_trades`, `percent_profitable`, `profit_factor`, `max_drawdown`) são **candidatas a alimentar episódios**, sempre com o rótulo "Observação de backtest, janela X, parâmetros Y".

### 1.6 SPEC‑022 — Cognitive & Adversarial Test [LIDO no slot; INFERÊNCIA no encaixe]
Casos do slot: "ferramenta indisponível", "erro de ferramenta", "Conviction excessiva". Os incidentes reais da §3.4 são **casos de teste prontos** (diálogo inesperado, falha de abertura do editor, histórico variável).

### 1.7 SPEC‑039 / 042 / 040 / 041 / 044 [INFERÊNCIA]
- **039** (seleção/governança de ferramenta): decidir *quando* usar Pine; dado de ferramenta é não‑confiável.
- **042** (guardrails de runtime): o "injetar código" e o "adicionar ao gráfico" exigem **gate de confirmação** (alteram o ambiente do usuário).
- **040/041** (observabilidade, auditoria/reconstrução): backtest só é reconstruível se o **código, as entradas e a janela** forem registrados (§6).
- **044** (alucinação/integridade): número de backtest citado sem proveniência é afirmação sem fonte.

### 1.8 SPEC‑025 — Skills [LIDO em §22; INFERÊNCIA no resto]
"Skills individuais antes da SPEC‑025" não são especificadas agora. Uma skill de "Pine+backtest" só existe depois; o que vale hoje é o **procedimento** desta referência.

### 1.9 Restrições constitucionais que o Pine **não** pode violar [LIDO — `AGENTS.md` §6]
1. Hierarquia Elliott → Fibonacci → Fractal → SMC → ICT: estratégia de camada inferior não sobrepõe a superior.
2. `directional_conflict = true` (Elliott × SMC) ⇒ NEUTRO.
3. **R:R mínimo 1:3**. O exemplo da §3 fixou `rr = 3.0` por isso.
4. **Custo nunca entra no Conviction Vector** (INV‑04). Comissão e slippage entram no P&L do backtest (para validar), **não** na convicção.
5. SOT **não executa ordem** (INV‑05). Estratégia Pine é instrumento de medição, jamais de envio.

---

## 2. O que foi comprovado (capacidade)

Todas as etapas abaixo foram executadas no TradingView Desktop via MCP:

| Capacidade | Ferramenta MCP | Resultado |
|---|---|---|
| Abrir o Pine Editor | `ui_open_panel(panel="pine-editor", action="open")` | ok |
| Criar script novo (estratégia) | `pine_new(type="strategy")` | ok (**só depois** do painel aberto) |
| Escrever o código | `pine_set_source(source=…)` | ok, 43 linhas |
| Compilar | `pine_smart_compile` + `pine_get_errors` | 0 erros |
| Adicionar ao gráfico | `ui_keyboard(key="Enter", modifiers=["ctrl"])` | estratégia no gráfico (`DlY7FU`) |
| Ler backtest | `data_get_strategy_results` | 19 métricas |
| Calibrar | `indicator_set_inputs(entity_id, inputs)` + nova leitura | 5 combinações |
| Restaurar | `indicator_set_inputs` com os valores originais | ok |

Não executei: `data_get_trades`, `data_get_equity`, `pine_save`, walk‑forward, DSR/PBO.

---

## 3. O exemplo real executado (BTCUSDT · H4 · 2026‑10‑03)

### 3.1 Objetivo
Testar o **fluxo** (criar → compilar → backtestar → calibrar), não achar uma estratégia lucrativa.

### 3.2 O código injetado (Pine v6, verbatim)

```pine
//@version=6
strategy("SOT Teste EMA+ATR (calibração)", overlay=true, initial_capital=10000,
     default_qty_type=strategy.percent_of_equity, default_qty_value=10,
     commission_type=strategy.commission.percent, commission_value=0.05, slippage=2,
     calc_on_every_tick=false, process_orders_on_close=false)

// ── Parâmetros calibráveis ───────────────────────────────────────────────
fastLen = input.int(20, "EMA rápida", minval=2)
slowLen = input.int(50, "EMA lenta", minval=3)
atrLen  = input.int(14, "Período ATR", minval=1)
atrMult = input.float(2.0, "Stop = ATR x", minval=0.5, step=0.25)
rr      = input.float(3.0, "Alvo R:R", minval=0.5, step=0.5)

// ── Cálculo (sinais só em barra fechada: calc_on_every_tick=false) ───────
fast = ta.ema(close, fastLen)
slow = ta.ema(close, slowLen)
atr  = ta.atr(atrLen)

longSig  = ta.crossover(fast, slow)
shortSig = ta.crossunder(fast, slow)

// ATR congelado no sinal: o stop não "anda" com a volatilidade depois da entrada
var float eAtr = na
if longSig or shortSig
    eAtr := atr

if longSig
    strategy.entry("L", strategy.long)
if shortSig
    strategy.entry("S", strategy.short)

if strategy.position_size > 0
    strategy.exit("xL", "L",
         stop  = strategy.position_avg_price - atrMult * eAtr,
         limit = strategy.position_avg_price + atrMult * eAtr * rr)
if strategy.position_size < 0
    strategy.exit("xS", "S",
         stop  = strategy.position_avg_price + atrMult * eAtr,
         limit = strategy.position_avg_price - atrMult * eAtr * rr)

plot(fast, "EMA rápida", color=color.new(color.teal, 0))
plot(slow, "EMA lenta",  color=color.new(color.orange, 0))
```

Decisões de projeto que importam para o SOT: sinais **só em barra fechada** (`calc_on_every_tick=false`), custos declarados (0,05% de comissão, 2 ticks de slippage), `rr=3` (regra do SOT), ATR **congelado no sinal** (evita stop que muda depois da entrada).

### 3.3 Resultado (cinco execuções, mesma janela carregada, capital 10.000)

| # | EMA rápida/lenta | Stop (× ATR) | Operações | Fator de lucro | Resultado | Acerto | Drawdown máx. | Sharpe |
|---|---|---|---|---|---|---|---|---|
| 1 | 20 / 50 | 2,0 | 187 | 1,025 | +86,56 (+0,87%) | 28,9% | 3,38% | −0,184 |
| 2 | 10 / 30 | 2,0 | 388 | 0,769 | −1.375,62 (−13,76%) | 24,5% | 14,26% | −0,448 |
| 3 | 30 / 100 | 2,0 | 119 | 0,871 | −313,89 (−3,14%) | 25,2% | 7,80% | −0,358 |
| 4 | 20 / 50 | 3,0 | 186 | 0,923 | −288,20 (−2,88%) | 28,5% | 8,47% | −0,193 |
| 5 | 20 / 50 | **1,5** | 187 | **1,102** | **+292,03 (+2,92%)** | 29,9% | 3,16% | −0,194 |

Depois da grade, os parâmetros foram **restaurados** para a execução 1 (20/50, 2,0).

### 3.4 Leitura crítica (o que este exemplo ensina)

1. **A "melhor" combinação (nº 5) não é descoberta, é seleção.** Cinco tentativas, sem separar treino de teste, na amostra inteira. Isso é o sobreajuste que o `SES-001` §16 descreve. O fator de lucro 1,10 **não** valida o parâmetro.
2. **Sharpe negativo em todas** as execuções de 187 operações: não há edge demonstrado.
3. **Sensibilidade enorme**: o mesmo código foi de PF 0,77 a 1,10 só mudando parâmetros. Para o SOT, isso é o sinal de que um limiar calibrado assim seria frágil.
4. **A janela mudou entre execuções.** O campo `buy_hold_return` variou de 9.418,6 a 11.990,0 (USDT) porque a janela do tester depende do histórico carregado e da primeira operação. (Interpretei esse campo como o retorno de comprar e segurar em USDT; **não conferi** a base de cálculo do campo.) Conclusão operacional: **registre sempre a janela** (§6).
5. **Incidentes reais** (use como casos da SPEC‑022):

| Incidente | O que ocorreu | Como contornei |
|---|---|---|
| `pine_new` falhou | "Could not open Pine Editor" | Abrir o painel antes: `ui_open_panel(pine-editor, open)` |
| `pine_smart_compile` clicou "Pine Save" | Abriu o diálogo **"Salvar script"** (script sem título), não adicionou ao gráfico (`study_added:false`) | `ui_click(by=text, value="Cancelar")` e depois **Ctrl+Enter** (adicionar ao gráfico) |
| `indicator_add` não achou o script | Script não salvo não aparece na busca | Não usar; adicionar pelo atalho do editor |
| Chaves de `indicator_set_inputs` | São `in_0, in_1, …` na **ordem de declaração** dos `input.*` | Confirmei `in_0` (EMA rápida), `in_1` (EMA lenta), `in_3` (múltiplo ATR). `in_2` (ATR) e `in_4` (R:R) são **inferência** |
| `pine_get_console` | Devolve o **texto do editor inteiro** várias vezes (ruído, custa contexto) | Preferir `pine_get_errors` |

### 3.5 Nada foi salvo na conta
O script ficou como "Script sem título". **Não houve `pine_save`.** Se o editor for fechado, ele se perde. A estratégia ficou no gráfico do usuário até pedido de remoção.

---

## 4. Como calibrar certo (o que faltou no exemplo)

A grade da §3.3 mostra o **mecanismo**. Para virar evidência aceitável ao SOT (WF‑V01, SES‑001 §16, RULE‑CTF‑01), siga este protocolo.

### 4.1 Antes de rodar
1. **Declare o baseline** (RULE‑CTF‑01): o que é "sem a regra"? (ex.: comprar e segurar; ou a mesma estratégia com parâmetros‑padrão). Altere **uma** premissa por vez.
2. **Registre a hipótese antes de ver o resultado** (anti‑hindsight): "o stop de 1,5×ATR reduz o drawdown" é testável; "vamos ver o que dá" não é.
3. **Conte as tentativas.** O número de combinações testadas entra na correção de múltiplos testes.

### 4.2 Durante: separar treino e teste dentro do Pine
**Esboço NÃO executado** (escrito a partir da documentação do Pine; compile e valide antes de confiar). Adiciona janelas de data como entradas e só opera dentro delas:

```pine
// Esboço — não testado
trainStart = input.time(timestamp("2026-01-01"), "Início treino")
trainEnd   = input.time(timestamp("2026-07-01"), "Fim treino / início teste")
testEnd    = input.time(timestamp("2026-10-01"), "Fim teste")
phase      = input.string("treino", "Fase", options=["treino", "teste"])

inWindow = phase == "treino" ? (time >= trainStart and time < trainEnd)
                             : (time >= trainEnd and time < testEnd)
// ... e envolver as ordens: if longSig and inWindow ...
```

Fluxo: escolher parâmetros **só** na fase `treino`; congelá‑los; ler **uma vez** a fase `teste`. Se o desempenho cair muito, é sobreajuste.

### 4.3 Depois: o que o Strategy Tester não faz
- **Deflated Sharpe Ratio / PBO (CSCV):** exigidos por WF‑V01. Calcule **fora** do TradingView (Python), a partir da lista de operações (`data_get_trades`) e do número de tentativas. A fonte do Dossiê (`reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md`) aponta a base metodológica; não invente fórmula, cite a fonte.
- **Estabilidade temporal e regimes:** rode por sub‑períodos e registre.
- **Custos:** a comissão/slippage do script são hipóteses; declare‑as no registro.

### 4.4 Armadilhas de Pine que quebram a validade
- `calc_on_every_tick=true` ou `request.security` sem cuidado ⇒ **repaint/look‑ahead** (a fonte `SRC-REPAINT-01` do Dossiê: mais de 95% dos indicadores repintam).
- Parâmetro "ótimo" escolhido na amostra inteira ⇒ sobreajuste.
- Janela do tester variável (§3.4) ⇒ resultados não comparáveis.
- Estratégia que usa indicador de terceiros "protegido" ⇒ não auditável (o código‑fonte não é legível).

---

## 5. Contrato de ferramenta (modelo SPEC‑038) — PROPOSTA de preenchimento

> **[PROPOSTA]** para o Especificador usar como rascunho em pesquisa; **não** é Spec. Formato do slot: `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas`.

| Campo | `pine_set_source` (injetar) | `pine_smart_compile` / Ctrl+Enter | `data_get_strategy_results` | `indicator_set_inputs` |
|---|---|---|---|---|
| Finalidade | Escrever o script no editor | Compilar e adicionar ao gráfico | Ler métricas do Strategy Tester | Alterar parâmetros |
| Input | Código‑fonte (texto) | — | — | `entity_id`, JSON `in_N` |
| Output | `lines_set` | erros; `study_added` | 19 métricas numéricas | `updated_inputs` |
| Precisão | Exata | Exata | Dado do TradingView, não verificado de forma independente | Exata |
| Determinismo | Sim | Sim (mesmo código ⇒ mesmos erros) | **Condicionado** à janela carregada (§3.4) | Sim |
| Limitações | **Sobrescreve** o editor | Pode abrir diálogo "Salvar script" | Janela variável; sem DSR/PBO; sem divisão treino/teste | Chaves `in_N` por ordem de declaração |
| Custo / Latência | Baixo / ~segundos | Baixo / ~segundos | Baixo / depende do cálculo da estratégia | Baixo / recalcula o backtest |
| Provenance | hash do código | versão do Pine, data | símbolo, tf, janela, parâmetros, custos | valores antes/depois |
| Falhas | Editor não abre | Diálogo inesperado; `study_added:false` | Painel fechado; estratégia oculta | `entity_id` inexistente |
| Classe (CC‑11) | **C** (efeito) | **C** (efeito) | **D** (leitura) | **D/C** |

---

## 6. Proveniência mínima de um backtest (registre sempre)

Sem estes campos, o backtest **não é reconstruível** (SPEC‑041) e não pode virar Evidência:

```
script_sha256     : hash do código‑fonte injetado
script_versao_pine: "6"
entradas          : {in_0:20, in_1:50, in_2:14, in_3:2.0, in_4:3.0}
simbolo / tf      : "BINANCE:BTCUSDT" / "240"
janela            : primeira e última barra efetivamente usadas pelo tester
custos            : comissão 0,05% · slippage 2 ticks
capital / tamanho : 10000 · 10% do patrimônio
n_tentativas      : quantas combinações já foram testadas (para DSR/PBO)
fase              : treino | teste | inteira
capturado_em_utc  : timestamp
metricas          : {total_trades, profit_factor, net_profit, percent_profitable, max_drawdown_percent, sharpe_ratio}
status            : OK | FAILED | STALE | INDETERMINADO
rotulo_qualidade  : (WF‑V02) "Observação de backtest — amostra única, sem DSR/PBO"
```

**Cadeia de promoção:** Observação (saída do tester) → Evidência (só após interpretação por agente, com lineage; INV‑06) → Hipótese (CHM‑001) → Convicção (CCM‑001, pelo Manager). Backtest de **uma** estratégia nunca sobe sozinho a Convicção.

---

## 7. Onde isso entra no backlog (encaminhamentos como `[PROPOSTA]`)

| Item | Estado conhecido | O que este material oferece | O que **não** faz |
|---|---|---|---|
| **BL‑032** (dona do backtest/calibração) | Aberto | Evidência exploratória de viabilidade e o protocolo da §4 como insumo para escolher entre ampliar a SPEC‑018 ou criar slot novo | Não escolhe a dona |
| **BL‑031** (TradingView↔SOT) | Ativado pela abertura da SPEC‑038 | Exemplo concreto de quatro ferramentas Pine (§1.1) | Não fecha o veredito de Termos de Uso |
| **BL‑017** (tool correctness ↔ SPEC‑038) | Ativado | Contratos da §5 como rascunho | Não emenda a SPEC‑020 |
| **J‑001 / N‑001** | Abertas | Mecanismo para medir sensibilidade de limiares | Nenhum valor definitivo |
| **K‑001** (governança de runtime, resolvida por SPEC‑018) | Ativa | Casos para o ciclo Formalização→Backtest | — |

**Modelo de proposta** (para Andraus decidir; você só redige):

> `[PROPOSTA]` Registrar em BL‑032 que o fluxo Pine (criar → compilar → backtestar → recalibrar) foi comprovado tecnicamente em 2026‑10‑03 (BTCUSDT H4), com 5 execuções e sem validação estatística. Opção A: ampliar SPEC‑018 com etapas de Backtest/Stress Test sob WF‑V01. Opção B: novo slot "Backtest & Calibração". Pré‑condição para ambas: decisão `SPEC-038-TVMCP-001` (canal lícito de dados). Evidência: `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` §3.

---

## 8. Segundo exemplo real: análise de Elliott no H4 com ferramentas **nativas**

Mesma sessão, mesmas regras de honestidade. Ferramentas nativas usadas: Zigzag, Awesome Oscillator e Fibonacci retracement (desenho), mais cálculo dos pivôs nos candles brutos (`data_get_ohlcv`).

**Fatos conferidos nos candles H4:**
- Início do impulso: 74.967,97 (15/09 16h UTC). Topo da onda 5: **87.395,67** (21/09 20h UTC). Zigzag nativo: impulso de +12.427,70; onda A de −4.832,67 (até 82.563); onda B de +4.657 (até 87.220, 96% de A).
- Regras duras do impulso (onda 2 não passa do início; onda 3 não é a menor; onda 4 sem sobreposição à onda 1): **passam**.
- O gráfico está em **escala logarítmica**; o Fibonacci nativo tem `fibLevelsBasedOnLogScale: true`. Retrocessos em escala log: 38,2% ≈ 82.422, 50% ≈ 80.943, 61,8% ≈ 79.491. Em escala linear seriam outros (82.648 / 81.182 / 79.716). **Declare a escala.**

**Duas contagens que se excluem** (decisão por fechamento H4, não por opinião):

| | Contagem A | Contagem B |
|---|---|---|
| Leitura | Impulso 0‑5 completo; correção A‑B‑C em curso | 87.396 é onda 3 de impulso maior; A‑B‑C é a onda 4; vem onda 5 |
| Morre se | fechamento acima de **87.395,67** | fechamento abaixo de **81.951** |
| Confiança (julgamento, **não** é Conviction Vector) | ~35% | ~40% |

**Duas correções que fiz no meio da sessão** (lição de método):
1. Eu havia dado 87.278 como topo, valor lido de um indicador de terceiros. Os candles brutos mostram o topo real em **87.395,67**. *Conferir o dado bruto antes de citar.*
2. Eu havia afirmado "divergência de baixa no momento". O Awesome Oscillator nativo mostrou o **maior pico justamente no topo**, ou seja, **sem** divergência. Isso enfraqueceu a contagem A. *Não afirmar divergência sem comparar os picos.*

Encaixe no SOT: é um exemplo de **Observação → Evidência → Hipótese** com invalidação falseável (WF‑V02: Elliott = regras falseáveis, contagem subjetiva). O schema `schemas/elliott-wave.input.json` espera OHLCV por grau e `invalidation_level`; ambos saíram dessa análise.

---

## 9. Procedimento passo a passo para o Claude Code

1. **Conexão:** `tv_health_check` (ver o tutorial do TradingView). Se falhar, pare.
2. **Pedir confirmação** ao usuário antes de qualquer efeito (injetar código, adicionar estratégia ao gráfico, desenhar). Anuncie o que vai mudar.
3. `ui_open_panel(pine-editor, open)` → `pine_new(strategy)`.
4. Escreva o código (inclua custos, `calc_on_every_tick=false`, entradas nomeadas).
5. `pine_set_source` → `pine_get_errors`. Se houver erro, corrija e repita.
6. Adicionar ao gráfico: **Ctrl+Enter** (`ui_keyboard`). Se aparecer o diálogo "Salvar script", cancele. **Não salve** sem pedido.
7. `chart_get_state` para obter o `entity_id`. `data_get_strategy_results`.
8. Calibre **seguindo a §4** (treino/teste; contar tentativas).
9. Restaure os parâmetros originais; pergunte se remove a estratégia do gráfico.
10. Registre proveniência (§6) e entregue como **Observação**, com o rótulo de qualidade.
11. Se alterou algum `.md` do repositório: `python scripts/build_map.py` e `python scripts/build_map.py --check` (`AGENTS.md` §5).

---

## 10. Checklist de anti‑padrões

- [ ] Não usei resultado de uma grade na amostra inteira como parâmetro "ótimo".
- [ ] Não escrevi nenhum número deste tutorial como limiar de J‑001/N‑001/convicção.
- [ ] Declarei janela, custos, escala (linear/log) e número de tentativas.
- [ ] Separei treino de teste ou marquei explicitamente "amostra única".
- [ ] Não tratei saída do tester como Evidência sem agente e sem lineage.
- [ ] Não deixei estratégia/desenho/alerta no gráfico do usuário sem avisar.
- [ ] Não salvei script na conta sem pedido.
- [ ] Lembrei que o canal tem pendência de Termos de Uso (`SPEC-038-TVMCP-001`).
- [ ] Apresentei encaminhamentos como `[PROPOSTA]`, sem editar ROADMAP/CATÁLOGO/RMR‑001.

---

*Fontes locais: `ROADMAP.md`, `AGENTS.md`, `WORKFLOW.md`, `governance/RULES.md`, `governance/SES-001_Especializacao_Cognitiva_Trading.md`, `specs/features/SPEC-038/{ABERTURA.md,research.md}`, `specs/features/SPEC-003/plan.md`, `docs/fundamentos/ARIA-plano-mestre.md`, `reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md`, `schemas/elliott-wave.input.json`. Execução real: TradingView Desktop 3.4.1, BINANCE:BTCUSDT, H4, 2026‑10‑03.*
