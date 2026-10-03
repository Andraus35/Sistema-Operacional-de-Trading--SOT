# MASTER — MARKET DATA, ORDER FLOW E INTEGRAÇÃO TRADINGVIEW

**Sistema:** Sistema Operacional de Trading — SOT
**Finalidade:** Documento mestre para entrada em pauta de especificação
**Status:** DISCOVERY / DECISION REQUIRED
**Natureza:** Requisito arquitetural + opções tecnológicas + decisões abertas
**Prioridade:** Alta
**Escopo inicial:** BTC Futures, Nasdaq Futures e Gold Futures
**Princípio central:** Não escolher fornecedor antes de especificar as necessidades informacionais do SOT.

---

# 1. Objetivo

Definir a necessidade de uma camada de **Market Data e Market Microstructure** para o SOT capaz de atender simultaneamente:

1. análise humana no TradingView
2. análise computacional pelo SOT
3. agentes especializados em Elliott, SMC, ICT e Order Flow
4. análise de futuros com alavancagem
5. dados de preço e volume
6. Order Flow
7. Footprint
8. Delta
9. CVD
10. desequilíbrios
11. absorção
12. exaustão
13. liquidez
14. profundidade de mercado
15. Open Interest
16. liquidações quando disponíveis
17. contexto de mercado
18. histórico para backtest/replay
19. dados em tempo real
20. proveniência e rastreabilidade
21. baixo consumo de tokens
22. independência do SOT em relação a um fornecedor específico
23. possibilidade de substituição ou combinação de provedores.

---

# 2. Contexto atual

Atualmente o SOT utiliza o TradingView como principal canal de observação através do:

`tradesdontlie/tradingview-mcp`

O MCP conecta o agente ao TradingView Desktop local através de Chrome DevTools Protocol.

O canal atual permite ao agente consultar e manipular o ambiente TradingView, incluindo:

* símbolo
* timeframe
* preço
* OHLCV
* indicadores
* Pine Script
* linhas
* labels
* boxes
* tabelas
* screenshots
* alertas
* replay
* múltiplos painéis
* múltiplos símbolos
* streaming
* dados de indicadores
* dados de depth disponibilizados pelo ambiente.

O MCP deve ser tratado como uma **camada de interação com o TradingView**, e não automaticamente como a arquitetura definitiva de Market Data do SOT.

---

# 3. Mudança de escopo relevante

O SOT inicialmente não será limitado a cripto.

Os mercados iniciais previstos são:

| Ativo lógico | Mercado pretendido                 | Necessidade                         |
| ------------ | ---------------------------------- | ----------------------------------- |
| BTC          | Futuros / derivativos              | Order Flow + liquidez + derivativos |
| Nasdaq       | Futures, preferencialmente NQ      | Order Flow + microestrutura         |
| XAU          | Gold Futures, preferencialmente GC | Order Flow + microestrutura         |

A especificação deverá confirmar formalmente os instrumentos.

Não assumir que:

`BTC = BTC Spot`

`Nasdaq = ação/ETF`

`XAU = XAUUSD spot`

O instrumento operacional deve ser definido explicitamente.

---

# 4. Problema fundamental

O SOT não necessita simplesmente de um feed de preço.

Necessita de diferentes níveis de observação:

```text
PRICE
  ↓
OHLCV
  ↓
TRADES
  ↓
BBO / L1
  ↓
MARKET DEPTH / L2
  ↓
MARKET BY ORDER / L3
  ↓
ORDER FLOW
  ↓
FOOTPRINT
  ↓
MARKET OBSERVATION
  ↓
EVIDENCE
  ↓
CONVICTION
```

O erro arquitetural a evitar é:

```text
Market Data bruto
       ↓
      LLM
```

O modelo correto é:

```text
Market Data bruto
       ↓
Deterministic Market Data Engine
       ↓
Order Flow / Analytics Engine
       ↓
Market Observation compacta
       ↓
SPEC-002
       ↓
Evidence
       ↓
SPEC-003
```

---

# 5. Princípio Provider ≠ Evidence

Nenhum provedor de dados deve ser tratado diretamente como produtor de Evidence.

O provedor produz **Market Data**.

O SOT transforma Market Data em **Observation**.

A camada de evidência determina se determinada Observation pode participar da formação de Evidence segundo SPEC-002.

Portanto:

```text
Provider
   ≠
Observation
   ≠
Evidence
   ≠
Conviction
```

Essa separação deve ser preservada.

---

# 6. TradingView — papel desejado

O TradingView deve ser considerado prioritariamente como:

## Human Analysis Layer

Responsabilidades potenciais:

* visualização
* gráficos
* contexto
* estrutura de mercado
* múltiplos timeframes
* indicadores
* Pine Script
* níveis
* zonas
* volume
* análise visual
* replay
* validação humana
* comparação visual
* observação de contexto.

O TradingView MCP pode funcionar como:

```text
Human Trading Environment
          ↓
TradingView Desktop
          ↓
TradingView MCP
          ↓
SOT / Agent
```

O TradingView não deve ser considerado automaticamente:

* fonte única da verdade
* backbone institucional de market data
* substituto de um feed L2/L3
* agregador universal de Order Flow.

---

# 7. Necessidade de separar duas perspectivas

O SOT deverá considerar:

## 7.1 Human Observation

Informação observada pelo humano através do TradingView.

Exemplo:

> Estrutura parece apresentar rompimento de máxima anterior.

Isso inicialmente é:

`Observation`

Não é automaticamente:

`Evidence`.

---

## 7.2 Machine Observation

Informação obtida de Market Data estruturado.

Exemplo:

```yaml
instrument: NQ
timestamp: ...
price: ...
volume: ...
delta: ...
cvd: ...
imbalance: ...
open_interest: ...
```

Também é:

`Observation`

e somente posteriormente pode participar da formação de Evidence.

---

# 8. Necessidade específica de BTC

BTC possui uma particularidade importante:

## mercado fragmentado

Não existe um único order book mundial oficial do Bitcoin.

Existem diferentes:

* exchanges
* venues
* contratos
* pares
* mercados spot
* perpetuals
* futures
* derivativos.

Portanto, para BTC, o SOT deverá distinguir:

```text
VENUE-SPECIFIC DATA
```

de:

```text
AGGREGATED MARKET DATA
```

Exemplo:

```text
Binance BTCUSDT
```

não deve ser semanticamente tratado como:

```text
BTC global
```

sem uma metodologia explícita.

---

# 9. Necessidade de BTC agregado

Deverá ser estudada a utilização de um fornecedor que consolide múltiplas exchanges.

O objetivo seria obter uma representação como:

```text
Binance
OKX
Bybit
Coinbase
Kraken
...
        ↓
Normalização
        ↓
Agregação
        ↓
BTC Market State
```

A agregação deve preservar a possibilidade de identificar:

* exchange
* instrumento
* timestamp
* tipo de dado
* metodologia de agregação.

Nunca eliminar a provenance original.

---

# 10. BTC Futures versus BTC Spot

O SOT deverá tratar separadamente:

```text
BTC Spot
BTC Perpetual
BTC Futures com vencimento
BTC CME Futures
```

Não assumir equivalência.

Para futuros/perpetuals, avaliar especialmente:

* preço
* volume
* trades
* order book
* open interest
* funding
* basis
* liquidações
* agressão
* delta
* CVD
* mudanças de liquidez.

---

# 11. Necessidade específica de Nasdaq

Para Nasdaq Futures, avaliar prioritariamente:

`NQ — E-mini Nasdaq-100 Futures`

e eventualmente:

`MNQ — Micro E-mini Nasdaq-100 Futures`

O instrumento deverá ser confirmado na especificação.

Para NQ/MNQ, a existência de uma venue centralizada de futuros permite uma arquitetura diferente da de BTC fragmentado.

Modelo:

```text
CME
 ↓
NQ / MNQ
 ↓
Trades
BBO
L2
MBO/L3
 ↓
Order Flow Engine
```

---

# 12. Necessidade específica de XAU

Para XAU, diferenciar:

```text
XAUUSD Spot
```

de:

```text
Gold Futures — GC
```

e eventualmente:

```text
Micro Gold — MGC
```

Se o objetivo é Order Flow de futuros, GC/MGC deve ser avaliado prioritariamente.

Modelo:

```text
COMEX / CME
 ↓
GC / MGC
 ↓
Trades
BBO
L2
MBO/L3
 ↓
Order Flow Engine
```

---

# 13. Requisito de Order Flow

O SOT deverá definir formalmente quais fenômenos de Order Flow pretende observar.

Lista inicial:

* agressão compradora
* agressão vendedora
* delta
* cumulative delta
* volume por preço
* footprint
* imbalance
* stacked imbalance
* absorção
* exaustão
* liquidez
* retirada de liquidez
* reposicionamento de liquidez
* spread
* profundidade
* desequilíbrio bid/ask
* grandes negócios
* volume anormal
* Open Interest
* liquidações
* mudanças abruptas de liquidez.

Essa lista é uma pauta inicial e não uma decisão definitiva.

---

# 14. Order Book ≠ Order Flow

A especificação deverá preservar essa distinção.

## Order Book

Representa ordens/liquidez disponíveis.

Pode permitir observar:

* bid
* ask
* profundidade
* spread
* níveis
* concentração
* mudanças do book.

## Order Flow

Representa principalmente a atividade efetivamente negociada e sua dinâmica.

Pode permitir derivar:

* delta
* agressão
* CVD
* footprint
* absorção
* exaustão
* imbalance.

Portanto:

```text
Order Book
    +
Trades
    +
Timestamp
    +
Market Structure
    ↓
Order Flow Analytics
```

---

# 15. L1 / L2 / L3

A especificação deverá determinar o nível mínimo necessário.

## L0

Preço/OHLCV/agregados.

Adequado para:

* estrutura
* indicadores
* análise técnica básica.

## L1

BBO/trades/top of book.

Adequado para:

* spread
* melhor bid
* melhor ask
* fluxo básico.

## L2

Profundidade agregada por nível de preço.

Adequado para:

* market depth
* imbalance
* liquidez
* book pressure.

## L3 / MBO

Market By Order.

Permite maior granularidade e reconstrução do livro por ordem.

Adequado para:

* microestrutura avançada
* queue position
* dinâmica de ordens
* reconstrução do book
* pesquisas mais profundas.

Não assumir que L3 é obrigatório.

A especificação deve justificar seu custo-benefício.

---

# 16. Requisito crítico: não enviar dados brutos ao LLM

O SOT deverá evitar:

```text
100.000 eventos de Order Book
          ↓
        LLM
```

O correto é:

```text
100.000 eventos
       ↓
Order Flow Engine
       ↓
Features
       ↓
Detecção determinística
       ↓
Market Observation
       ↓
LLM
```

Exemplo:

```yaml
OrderFlowObservation:
  instrument: NQ
  venue: CME
  timestamp: ...
  timeframe: 5m

  volume: 12543
  delta: 1842
  delta_zscore: 2.1

  cvd:
    direction: positive
    slope: positive

  imbalance:
    detected: true
    strength: high

  absorption:
    detected: true
    price: 24785.25

  liquidity:
    bid_depth: ...
    ask_depth: ...
    imbalance: ...

  provenance:
    provider: ...
    dataset: ...
    source_timestamp: ...
```

O LLM recebe a **interpretação estruturada dos dados**, não necessariamente os dados brutos.

---

# 17. Token Economics

A escolha do provedor deve ser avaliada também pelo custo de contexto.

A métrica não deve ser apenas:

`US$/mês do fornecedor`

Deve ser:

```text
Custo Total de Informação

=
Provider Cost
+
Data Processing Cost
+
Storage
+
Network
+
LLM Tokens
+
Latency
+
Operational Complexity
```

E, para o SOT:

```text
Value / Token
```

deve ser uma preocupação explícita.

---

# 18. Estratégia de compressão epistemicamente segura

Não comprimir simplesmente porque custa tokens.

A compressão deverá preservar:

* provenance
* timestamp
* venue
* instrumento
* timeframe
* método de cálculo
* dados relevantes
* incerteza
* qualidade
* conflitos.

Exemplo ruim:

```text
BTC bullish
```

Exemplo melhor:

```yaml
observation:
  type: ORDER_FLOW
  direction: BUY
  strength: HIGH

evidence:
  delta_zscore: 2.3
  absorption: true

provenance:
  venue_count: 7
  provider: ...
  timestamp: ...

uncertainty:
  level: MODERATE
```

---

# 19. Provedores a avaliar

A especificação deverá manter fornecedores como **opções**, não decisões prévias.

---

## OPÇÃO A — TradingView + TradingView MCP

### Papel

Human Analysis Layer.

### Pontos fortes

* excelente interface humana
* gráficos
* indicadores
* Pine Script
* múltiplos timeframes
* replay
* visualização
* contexto
* integração já existente no SOT
* baixo esforço incremental.

### Limitações

* não deve ser tratado automaticamente como infraestrutura de L2/L3
* MCP depende de interfaces internas do TradingView
* não é um agregador universal de order books
* os dados disponíveis dependem do que o TradingView disponibiliza para determinado mercado/instrumento
* consumo programático deve respeitar termos/licenciamento.

### Encaixe

```text
TRADINGVIEW
     ↓
Human Observation
     +
Visual Context
     ↓
SOT
```

### Status

`MANTER`

Não substituir na primeira etapa.

---

# 20. OPÇÃO B — Databento

### Papel

Machine Market Data Infrastructure.

Especialmente interessante para:

* CME
* NQ
* MNQ
* GC
* MGC
* futures
* trades
* BBO
* MBP
* MBO
* L2
* L3.

Databento disponibiliza schemas incluindo Trades, MBP, TBBO e MBO. O MBO fornece eventos do livro por nível de preço e order ID, incluindo adds, cancels, modifies e fills.

### Pontos fortes

* forte adequação a futures
* acesso a dados CME/COMEX
* granularidade elevada
* MBO/L3
* adequado para construção de Order Flow Engine
* histórico
* possibilidade de reconstrução do book
* arquitetura orientada a dados.

### Limitações

* pode ser overengineering para necessidades simples
* L2/L3 gera grande volume de dados
* custo computacional aumenta
* licenciamento de mercado deve ser considerado
* não fornece a experiência visual do TradingView.

Databento informa cobertura CME, CBOT, NYMEX e COMEX, com schemas L0-L3, incluindo MBO, e possui planos/licenciamento específicos para dados em tempo real.

### Encaixe

```text
Databento
    ↓
Raw Market Data
    ↓
Order Flow Engine
    ↓
Compact Observation
    ↓
SPEC-002
```

### Status

`FORTE CANDIDATO PARA NQ/GC`

---

# 21. OPÇÃO C — Kaiko

### Papel

Crypto Market Data Aggregation.

Especialmente interessante para:

* BTC
* spot
* derivatives
* multi-exchange
* order books
* liquidez agregada.

Kaiko informa cobertura de mais de 100 exchanges e dados spot/derivativos, com dados L1/L2, trades, order books e métricas de liquidez.

Também oferece dados agregados por ativo, permitindo observar liquidez de Bitcoin considerando múltiplos instrumentos e exchanges.

### Pontos fortes

* visão multi-exchange
* normalização
* crypto-native
* spot + derivatives
* order book
* liquidez
* dados históricos
* realtime.

### Limitações

* custo potencialmente elevado para um SOT pessoal
* pode ser excessivo na primeira versão
* agregação não deve eliminar provenance de exchange/instrumento
* necessidade de estudar exatamente quais mercados de futuros/perpetuals estão disponíveis e em que granularidade.

### Encaixe

```text
Kaiko
   ↓
BTC Multi-Exchange
   ↓
Normalized Market Data
   ↓
Aggregation
   ↓
Order Flow / Liquidity Engine
   ↓
SOT
```

### Status

`BENCHMARK INSTITUCIONAL / CANDIDATO BTC`

---

# 22. OPÇÃO D — CoinDesk Data

CoinDesk Data deve ser avaliado como alternativa direta à Kaiko.

A plataforma informa cobertura de centenas de exchanges, dados normalizados de trades, order books, derivados e dados históricos.

Para derivativos, informa dados de:

* trades
* open interest
* funding
* índices
* futuros
* perpetuals
* opções.

Para order book, informa:

* L1
* L2
* snapshots
* depth
* spread
* slippage
* realtime
* histórico.

### Pontos fortes

* forte cobertura crypto
* multi-exchange
* derivados
* order book
* dados normalizados
* histórico
* realtime.

### Limitações

* pricing institucional deve ser levantado
* pode ser excessivo para a primeira versão
* precisa ser comparado com Kaiko em granularidade, cobertura real de BTC futures e custo efetivo.

### Status

`BENCHMARK / ALTERNATIVA KAİKO`

---

# 23. OPÇÃO E — APIs nativas das exchanges

Exemplos:

* Binance
* OKX
* Bybit
* Coinbase
* outras exchanges relevantes.

### Papel

Market Data específica de venue.

### Pontos fortes

* baixo custo relativo
* realtime
* acesso direto
* WebSocket
* order book
* trades
* dados específicos da venue.

### Limitações

* fragmentação
* necessidade de integração individual
* normalização própria
* manutenção
* nenhuma venue isolada representa necessariamente o mercado global BTC
* maior dependência operacional de cada exchange.

### Encaixe

```text
Binance
   +
OKX
   +
Bybit
   +
...
   ↓
SOT Aggregation Layer
```

Pode ser uma solução econômica para MVP.

### Status

`CANDIDATO ECONÔMICO PARA MVP CRIPTO`

---

# 24. OPÇÃO F — Massive

Massive deve permanecer como opção secundária para avaliação.

Pode fornecer APIs, WebSockets e dados históricos para diferentes classes de ativos.

Porém, para o requisito específico:

```text
BTC futures
NQ futures
GC futures
L2/L3
Order Flow
```

deve ser comparado diretamente com Databento e provedores especializados antes de ser escolhido.

### Status

`BENCHMARK`

Não assumir que uma API generalista seja equivalente a um feed de microestrutura.

---

# 25. Arquitetura candidata

A arquitetura desejada deve permitir múltiplos provedores:

```text
                    SOT
                     │
        ┌────────────┴────────────┐
        │                         │
 HUMAN OBSERVATION          MACHINE OBSERVATION
        │                         │
 TradingView MCP             Provider Layer
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
               BTC               NQ                GC
                │                 │                 │
          Crypto Provider      Databento        Databento
                │
        ┌───────┴────────┐
        │                │
     Kaiko          CoinDesk
        │                │
        └───────┬────────┘
                │
       Exchange APIs
                │
                ↓
        MARKET DATA ADAPTER
                ↓
       CANONICAL DATA MODEL
                ↓
       ORDER FLOW ENGINE
                ↓
      MARKET OBSERVATION
                ↓
             SPEC-002
                ↓
             EVIDENCE
                ↓
         SPECIALIST AGENTS
                ↓
         EVIDENCE FUSION
                ↓
       CONVICTION VECTOR
                ↓
          DECISION GATE
```

---

# 26. Requisito de abstração

O SOT não deve codificar sua lógica diretamente contra:

```text
Databento API
```

nem:

```text
Kaiko API
```

nem:

```text
TradingView API/MCP
```

Deve existir uma abstração:

```text
MarketDataProvider
```

e adaptadores:

```text
TradingViewAdapter
DatabentoAdapter
KaikoAdapter
CoinDeskAdapter
ExchangeAdapter
```

Isso permite trocar o fornecedor sem modificar:

* Order Flow Engine
* Evidence Layer
* Conviction Engine
* agentes especializados.

---

# 27. Canonical Market Data Model

A especificação deverá propor um modelo canônico.

Exemplo mínimo:

```yaml
MarketObservation:
  observation_id:
  instrument:
  asset:
  market_type:
  venue:
  provider:

  timestamp:
  event_timestamp:

  price:
  bid:
  ask:
  spread:

  open:
  high:
  low:
  close:
  volume:

  trades:

  order_book:
    depth:
    imbalance:

  order_flow:
    delta:
    cvd:
    aggression:
    absorption:
    exhaustion:
    imbalance:

  derivatives:
    open_interest:
    funding:
    basis:
    liquidations:

  timeframe:

  quality:
  completeness:

  provenance:
    provider:
    dataset:
    venue:
    symbol:
    source_timestamp:
    calculation_version:

  uncertainty:
```

Esse modelo é preliminar e deve ser especificado formalmente.

---

# 28. Market Data Adapter

Cada adapter deve converter o formato do fornecedor para o modelo canônico.

Exemplo:

```text
Databento MBO
     ↓
DatabentoAdapter
     ↓
Canonical Market Event
```

ou:

```text
Kaiko L2
     ↓
KaikoAdapter
     ↓
Canonical Market Event
```

ou:

```text
TradingView MCP
     ↓
TradingViewAdapter
     ↓
Canonical Market Observation
```

---

# 29. Separar Raw Data de Derived Data

O SOT deve preservar a distinção:

```text
RAW MARKET DATA
       ↓
DERIVED MARKET DATA
       ↓
MARKET OBSERVATION
       ↓
EVIDENCE
```

Exemplo:

```text
Trade
```

é raw.

```text
Delta
```

é derived.

```text
"forte agressão compradora"
```

é uma interpretação/Observation.

```text
"há evidência de demanda agressiva"
```

pode ser Evidence, desde que satisfaça SPEC-002.

---

# 30. Provenance

Toda Market Observation relevante deverá permitir responder:

1. de onde veio?
2. qual provider?
3. qual venue?
4. qual instrumento?
5. qual timestamp?
6. qual dataset?
7. qual versão do cálculo?
8. quais dados originaram o cálculo?
9. qual transformação ocorreu?
10. qual nível de confiança/qualidade?

Exemplo:

```yaml
provenance:
  provider: Databento
  dataset: CME
  venue: CME Globex
  instrument: NQ
  schema: MBO
  source_timestamp: ...
  processing_version: OFE-001
```

---

# 31. Agregação não pode destruir provenance

Exemplo:

```text
BTC Aggregated Order Flow
```

não pode esconder:

```text
Binance
OKX
Bybit
Coinbase
...
```

O resultado deve permitir:

```yaml
aggregation:
  venues:
    - Binance
    - OKX
    - Bybit
    - Coinbase

  methodology:
  weighting:
  timestamp_alignment:
  normalization:
```

Se a metodologia de agregação não estiver disponível ou for insuficiente:

`UNCERTAINTY`

e não uma falsa certeza.

---

# 32. Regra de "global BTC"

O termo:

`BTC global`

deve ser proibido como descrição sem metodologia.

Usar:

```text
BTC aggregated market view
```

ou:

```text
BTC multi-venue observation
```

quando houver agregação formal.

Uma Observation de Binance deve continuar identificada como:

```text
BTC / Binance / instrument
```

---

# 33. Order Flow Engine

Deverá ser uma capacidade determinística separada do LLM.

Responsabilidades possíveis:

* construir candles
* construir footprint
* calcular delta
* calcular CVD
* detectar imbalance
* detectar stacked imbalance
* calcular volume profile
* detectar absorção segundo regra definida
* detectar exaustão segundo regra definida
* calcular profundidade
* calcular spread
* calcular mudanças de liquidez
* integrar OI
* integrar funding
* integrar liquidações.

O LLM poderá:

* interpretar
* relacionar
* levantar hipótese
* avaliar contexto
* comparar com outras evidências.

O LLM não deve ser o responsável por cálculos determinísticos quando estes puderem ser executados pelo sistema.

---

# 34. Separação cognitiva

Modelo desejado:

```text
DETERMINISTIC ENGINE
        ↓
"What happened?"
        ↓
LLM
        ↓
"What may it mean?"
        ↓
Evidence formation
        ↓
Fusion
        ↓
Conviction
```

Isso mantém:

**liberdade cognitiva**

sem permitir:

**liberdade para alterar fatos matemáticos.**

---

# 35. Relação com SPEC-002

Market Data deve alimentar SPEC-002 como Observation.

SPEC-002 continuará responsável pela governança de:

* provenance
* evidência
* dependência
* qualidade
* conflito
* ausência
* rastreabilidade
* formação de Evidence.

Não duplicar essas responsabilidades dentro do Market Data Layer.

---

# 36. Relação com SPEC-003

SPEC-003 não deve conhecer diretamente:

* API da Databento
* API da Kaiko
* API da CoinDesk
* Binance API
* TradingView MCP.

SPEC-003 deve consumir:

```text
Governed Evidence
```

e não:

```text
Provider Data
```

Portanto:

```text
Provider
 ↓
Market Data
 ↓
Market Analytics
 ↓
Observation
 ↓
SPEC-002
 ↓
Evidence
 ↓
SPEC-003
```

---

# 37. Requisito de fail-closed

Se houver dúvida sobre:

* timestamp
* venue
* instrumento
* qualidade
* completude
* sincronização
* agregação
* transformação
* cálculo
* independência
* duplicação de dados.

O sistema não deverá fabricar certeza.

Possíveis estados:

```text
VALID
INVALID
INDETERMINADO
PARTIAL
STALE
CONFLICTED
```

---

# 38. Staleness

O SOT deverá detectar dados antigos.

Exemplo:

```yaml
data_quality:
  age_ms: 8500
  max_allowed_age_ms: 2000
  status: STALE
```

Uma Observation stale não deve ser tratada como realtime.

---

# 39. Clock / Timestamp

Order Flow exige atenção especial a timestamp.

O sistema deverá diferenciar quando disponível:

```text
event timestamp
exchange timestamp
provider timestamp
receipt timestamp
processing timestamp
```

Nunca substituir silenciosamente um timestamp por outro.

---

# 40. Sincronização entre mercados

Para análises como:

```text
BTC
NQ
GC
DXY
```

será necessário eventualmente comparar eventos temporais.

Portanto a especificação deverá considerar:

* timezone
* UTC
* session
* exchange session
* event timestamp
* clock drift
* latency
* candle boundary.

---

# 41. Contexto multi-timeframe

O SOT deverá suportar pelo menos:

```text
Macro
 ↓
1D
 ↓
4H
 ↓
1H
 ↓
15m
 ↓
5m
 ↓
1m
 ↓
Tick / Order Flow
```

A necessidade exata deve ser definida pelos agentes Elliott, SMC, ICT e Order Flow.

---

# 42. Contexto humano + máquina

O agente poderá receber:

```text
TradingView:
  chart structure
  levels
  indicators
  visual context

+

Machine:
  order flow
  volume
  delta
  liquidity
  OI
  futures data
```

Isso permite construir uma visão híbrida:

```text
VISUAL MARKET CONTEXT
        +
QUANTITATIVE MARKET STATE
        ↓
LLM ANALYSIS
```

---

# 43. Requisito de replay/backtest

A mesma arquitetura utilizada no realtime deverá ser capaz de consumir dados históricos.

Objetivo:

```text
Historical Data
      ↓
Same Analytics Engine
      ↓
Same Observation Schema
      ↓
Same Evidence Formation
      ↓
Backtest / Replay
```

Evitar uma lógica diferente para:

```text
backtest
```

e:

```text
live
```

quando tecnicamente possível.

---

# 44. Reprodutibilidade

Uma Observation histórica deve poder ser reproduzida.

Para isso registrar:

```yaml
calculation:
  engine_version:
  configuration_version:
  parameters:
  source_dataset:
  source_version:
```

---

# 45. Custo-benefício

A avaliação dos fornecedores deverá usar pelo menos:

### Custo

* assinatura
* consumo
* histórico
* realtime
* licenças
* armazenamento
* infraestrutura
* tokens.

### Eficácia

* cobertura
* granularidade
* qualidade
* Order Flow
* derivativos
* multi-venue
* histórico.

### Eficiência

* API
* WebSocket
* volume
* compressão
* latência
* facilidade de integração.

### Efetividade / economicidade

* quanto da informação realmente melhora a decisão
* quanto dela realmente chega ao LLM
* quanto é descartada
* quanto custa por ciclo de análise.

---

# 46. Critério especial: valor por token

Para cada provider, testar:

```text
Raw Data Volume
       ↓
Processed Data Volume
       ↓
LLM Payload
       ↓
Tokens
       ↓
Useful Information
```

O objetivo não é minimizar tokens a qualquer custo.

O objetivo é:

> maximizar informação útil por token sem perder provenance, contexto ou capacidade de auditoria.

---

# 47. Matriz de avaliação futura

A especificação deverá produzir uma matriz como:

| Critério            | TradingView | Databento | Kaiko | CoinDesk | Exchange API |
| ------------------- | ----------- | --------- | ----- | -------- | ------------ |
| BTC                 |             |           |       |          |              |
| BTC Futures         |             |           |       |          |              |
| Multi-exchange BTC  |             |           |       |          |              |
| NQ                  |             |           |       |          |              |
| GC                  |             |           |       |          |              |
| Realtime            |             |           |       |          |              |
| Histórico           |             |           |       |          |              |
| L1                  |             |           |       |          |              |
| L2                  |             |           |       |          |              |
| L3/MBO              |             |           |       |          |              |
| Trades              |             |           |       |          |              |
| Footprint derivável |             |           |       |          |              |
| Delta derivável     |             |           |       |          |              |
| CVD derivável       |             |           |       |          |              |
| OI                  |             |           |       |          |              |
| Funding             |             |           |       |          |              |
| Liquidations        |             |           |       |          |              |
| Agregação           |             |           |       |          |              |
| Provenance          |             |           |       |          |              |
| API                 |             |           |       |          |              |
| WebSocket           |             |           |       |          |              |
| Custo               |             |           |       |          |              |
| Token efficiency    |             |           |       |          |              |
| Complexidade        |             |           |       |          |              |

A matriz não deve produzir automaticamente um "vencedor".

Ela deve mostrar adequação por necessidade e custo.

---

# 48. Hipóteses arquiteturais iniciais

### Hipótese H1

TradingView permanece como Human Analysis Layer.

### Hipótese H2

Databento é forte candidato para NQ/GC.

### Hipótese H3

Kaiko ou CoinDesk são fortes candidatos para BTC multi-exchange.

### Hipótese H4

APIs nativas podem ser suficientes para MVP de BTC se a visão multi-exchange não for inicialmente necessária.

### Hipótese H5

O Order Flow Engine deve ser propriedade do SOT e não do LLM.

### Hipótese H6

O SOT deve possuir abstração de provider.

### Hipótese H7

Raw Market Data não deve ser enviado diretamente ao LLM como fluxo normal.

### Hipótese H8

Market Observation compacta deve ser a interface entre Market Data Engine e agentes.

### Hipótese H9

SPEC-002 deve governar a passagem de Observation para Evidence.

### Hipótese H10

SPEC-003 deve permanecer independente do provider.

---

# 49. Decisões abertas

O agente de especificação deverá investigar e fechar, entre outras:

## D-001

Qual é exatamente o instrumento de BTC?

* CME BTC Futures
* Binance Futures
* OKX
* Bybit
* perpetual
* combinação.

## D-002

Qual é exatamente o instrumento Nasdaq?

* NQ
* MNQ
* outro.

## D-003

Qual é exatamente o instrumento XAU?

* GC
* MGC
* XAUUSD
* combinação.

## D-004

BTC necessita visão multi-exchange desde V1?

## D-005

Qual nível de Order Book é realmente necessário?

* L1
* L2
* L3/MBO.

## D-006

Footprint será calculado pelo SOT ou fornecido por ferramenta externa?

## D-007

Quais sinais de Order Flow são necessários para V1?

## D-008

Qual frequência máxima de atualização o SOT necessita?

## D-009

Qual latência é aceitável?

## D-010

Qual histórico é necessário?

## D-011

Qual volume de dados pode ser armazenado?

## D-012

Qual parte será processada deterministicamente?

## D-013

Qual parte será entregue ao LLM?

## D-014

Qual é o orçamento mensal aceitável?

## D-015

Qual é o custo máximo aceitável por ciclo de análise?

## D-016

Qual é o custo máximo de tokens por análise?

## D-017

É necessária agregação de exchanges em tempo real ou apenas histórica?

## D-018

A agregação deve ser por:

* volume
* liquidez
* exchange
* instrumento
* peso configurável.

## D-019

Como lidar com discrepâncias entre providers?

## D-020

Como detectar stale data?

## D-021

Como tratar gaps?

## D-022

Como preservar provenance após agregação?

## D-023

Como garantir reprodução histórica?

## D-024

Quais dados são realmente necessários para Elliott?

## D-025

Quais dados são realmente necessários para SMC?

## D-026

Quais dados são realmente necessários para ICT?

## D-027

Quais dados são realmente necessários para Order Flow?

---

# 50. Critério de não overengineering

O SOT não deverá adquirir L3/MBO simplesmente porque existe.

A pergunta correta é:

> Qual hipótese de trading exige essa informação?

Exemplo:

```text
Se L2 resolve a hipótese
        ↓
não comprar L3.

Se L3 não altera a Evidence
        ↓
não enviar L3 ao LLM.

Se Order Flow agregado não altera Conviction
        ↓
não manter o pipeline.
```

A arquitetura deve obedecer:

**necessário e suficiente.**

---

# 51. Critério de evolução

A arquitetura deve permitir evolução:

```text
V1
TradingView MCP
+
provider básico
+
Market Observation
```

↓

```text
V2
Order Flow Engine
+
BTC aggregation
```

↓

```text
V3
L2
+
advanced footprint
```

↓

```text
V4
L3/MBO
+
microstructure
```

Não implementar V4 apenas porque é tecnicamente possível.

---

# 52. Requisito de testes

A futura especificação deverá incluir testes para:

### Provider

* conexão
* autenticação
* símbolo
* timestamp
* stale
* gap.

### Normalização

* preço
* volume
* timestamp
* instrumento
* venue.

### Order Flow

* delta
* CVD
* footprint
* imbalance
* absorção.

### Aggregation

* múltiplas exchanges
* timestamps
* duplicidade
* weighting
* ausência.

### Provenance

* rastreabilidade
* reprodução.

### Token efficiency

* payload máximo
* redução
* informação preservada.

### Failure

* provider offline
* dados incompletos
* conflito
* stale
* schema inválido.

---

# 53. Invariantes iniciais

A futura SPEC deverá considerar:

### INV-MD-001

Provider nunca é Evidence.

### INV-MD-002

Raw Market Data nunca é automaticamente Evidence.

### INV-MD-003

LLM não calcula sozinho métricas determinísticas quando existe engine determinístico disponível.

### INV-MD-004

Agregação nunca elimina provenance.

### INV-MD-005

Venue-specific data nunca deve ser rotulado como global sem metodologia.

### INV-MD-006

Stale data não pode ser tratada como realtime.

### INV-MD-007

Dados de instrumentos diferentes não podem ser fundidos silenciosamente.

### INV-MD-008

BTC Spot não pode ser tratado como BTC Futures sem identificação explícita.

### INV-MD-009

NQ não pode ser tratado como Nasdaq Spot.

### INV-MD-010

GC não pode ser tratado como XAUUSD sem identificação explícita.

### INV-MD-011

Order Book não pode ser tratado como Order Flow.

### INV-MD-012

Order Flow derivado deve possuir provenance do dataset original.

### INV-MD-013

A compressão para LLM não pode destruir provenance essencial.

### INV-MD-014

O provider deve ser substituível sem alterar o contrato cognitivo do SOT.

### INV-MD-015

SPEC-003 não deve depender diretamente de provider.

---

# 54. Autoridade

A camada deve distinguir:

```text
Provider
    → fornece dados

Analytics Engine
    → calcula

Observation Builder
    → estrutura

SPEC-002
    → governa Evidence

LLM
    → interpreta / formula hipóteses

SPEC-003
    → forma Conviction

Decision Gate
    → determina autorização segundo regras
```

Nenhuma dessas camadas deve assumir autoridade de outra.

---

# 55. Proposta de pipeline final

```text
                 MARKET SOURCES
                       │
       ┌───────────────┼────────────────┐
       │               │                │
  TradingView      Crypto Data       Futures Data
       │               │                │
       │           BTC providers      CME/COMEX
       │               │                │
       └───────────────┼────────────────┘
                       ↓
                PROVIDER ADAPTER
                       ↓
              CANONICAL MARKET DATA
                       ↓
             MARKET DATA QUALITY
                       ↓
              ORDER FLOW ENGINE
                       ↓
          MARKET OBSERVATION ENGINE
                       ↓
                    SPEC-002
                       ↓
                    EVIDENCE
                       ↓
          SPECIALIZED MARKET AGENTS
                       ↓
                EVIDENCE FUSION
                       ↓
              CONVICTION VECTOR 8D
                       ↓
              GLOBAL CONVICTION
                       ↓
              DETERMINISTIC GATE
```

---

# 56. Decisão que NÃO deve ser tomada nesta pauta

Não decidir prematuramente:

```text
"Databento será o provider."

ou:

"Kaiko será o provider."

ou:

"TradingView resolve tudo."
```

A decisão deverá resultar da especificação dos requisitos e de benchmark controlado.

---

# 57. Benchmark mínimo obrigatório

Antes da contratação definitiva, comparar pelo menos:

### Cenário 1 — BTC

* preço
* trades
* order book
* multi-exchange
* derivatives
* OI
* funding
* liquidation
* latência
* histórico.

### Cenário 2 — NQ

* trades
* L1
* L2
* MBO
* histórico
* realtime
* footprint.

### Cenário 3 — GC

* trades
* L1
* L2
* MBO
* histórico
* realtime
* footprint.

### Cenário 4 — LLM

Medir:

```text
Raw payload
↓
Processed payload
↓
Tokens
↓
Latency
↓
Cost
↓
Useful observations
```

---

# 58. Resultado esperado da futura especificação

A futura SPEC deverá responder objetivamente:

1. Quais mercados o SOT realmente opera?
2. Quais instrumentos?
3. Qual provider para cada mercado?
4. Qual nível de dados?
5. Qual frequência?
6. Qual histórico?
7. Qual Order Flow?
8. Qual agregação?
9. Qual engine calcula?
10. Qual informação chega ao LLM?
11. Quanto custa?
12. Como funciona a provenance?
13. Como funciona o fallback?
14. Como testar?
15. Como trocar provider?
16. Quais informações são necessárias e quais são desperdício?

---

# 59. Resultado arquitetural desejado

O objetivo final não é:

> "ter acesso ao máximo de dados".

É:

> **fornecer ao SOT a menor quantidade de dados necessária para produzir a maior quantidade de informação epistemicamente útil, rastreável e reproduzível para a decisão de trading.**

Isso deve orientar toda a especificação.

---

# 60. Orientação para o agente de código

O agente deverá:

1. tratar este documento como pauta de Discovery/Specification
2. não implementar imediatamente
3. não escolher provider por preferência
4. não modificar SPEC-002/003 sem identificar impactos
5. mapear dependências existentes
6. pesquisar documentação oficial dos providers
7. identificar cobertura real dos instrumentos
8. identificar custos atuais
9. identificar limitações de licença
10. construir matriz comparativa
11. identificar requisitos mínimos
12. propor arquitetura de abstração
13. identificar decisões abertas
14. propor experimentos de benchmark
15. somente depois produzir a especificação formal.

A primeira entrega do agente deverá ser:

```text
MARKET DATA DISCOVERY REPORT
```

contendo:

* requisitos descobertos
* instrumentos
* fontes
* providers
* arquitetura candidata
* lacunas
* decisões abertas
* benchmark
* riscos
* impacto em SPEC-002
* impacto em SPEC-003
* recomendação de escopo V1.

A decisão final de provider deve ocorrer **depois do Discovery e do benchmark**, não antes.
