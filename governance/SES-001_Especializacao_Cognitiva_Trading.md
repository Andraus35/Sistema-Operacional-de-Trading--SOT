# EMENDA SES-001

## ESPECIALIZAÇÃO COGNITIVA E FUNCIONAL DO SOT PARA ANÁLISE DE TRADING

**Documento de origem:** Unidade Atômica de Especificação do Harness Cognitivo do SOT
**Natureza:** Emenda estrutural de especificação
**Aplicabilidade:** Integral
**Prioridade:** P0 — Obrigatória
**Status:** **HOMOLOGADO — BASELINE** (Andraus, 2026-09-20, DHR-SES-001; parecer Revisor CONFORME condicional → condições C1-C4 resolvidas). Regra superior às especificações individuais (§67). Incorporado ao `atomic-spec.md` v1.4 via emenda EUA-E03 (17 campos §59 + cadeia §60 + Constitution Check CC-06/CC-07).

> **Nota de incorporação C2 (Andraus, 2026-09-20):** a Multimodelagem (§11) opera **SOB** a hierarquia constitucional PC-01 (Elliott→Fibonacci→Fractal→SMC→ICT). A capacidade de processar múltiplos modelos não altera a autoridade: Elliott cria/invalida a hipótese estrutural; SMC/ICT confirmam ou enfraquecem, nunca sobrepõem (CONSTITUTION; INV-01/02; PC-01).
> **Transição C3 (Andraus, 2026-09-20):** a reavaliação das Cards/specs já homologadas sob esta emenda (§67) é diferida via backlog RMR-001 (regime R1, sem reescrita imediata), com gate "antes da redação da 1ª Engineering Card".
**Objetivo:** Determinar que toda especificação, decisão arquitetural, Design Pattern, Engineering Card, contrato cognitivo, mecanismo de Harness, critério de aceitação e mecanismo de avaliação do SOT seja concebido especificamente para sua missão de análise de Trading.

---

# 1. FINALIDADE DA EMENDA

Esta emenda estabelece que o SOT não deve ser especificado como um Harness Cognitivo genérico ao qual posteriormente se adicionam capacidades de Trading.

O SOT deve ser concebido desde a origem como:

> **um sistema cognitivo especializado em análise de mercados financeiros e produção de inteligência analítica para suporte à decisão de Trading.**

Consequentemente, a especialização em Trading não constitui uma camada periférica.

Ela deve atravessar:

* Kernel Cognitivo;
* oito camadas cognitivas;
* Modelos Canônicos;
* Skills;
* Subagentes;
* Engines;
* Design Patterns;
* Engineering Cards;
* RAG;
* indicadores;
* backtests;
* contexto de mercado;
* mecanismos de evidência;
* mecanismos de hipótese;
* mecanismos de incerteza;
* mecanismos decisórios;
* metacognição;
* aprendizagem;
* governança;
* avaliação;
* integração;
* observabilidade.

---

# 2. PRINCÍPIO DE ESPECIALIZAÇÃO TRANSVERSAL

A especialização Trading deve ser tratada como:

> **propriedade transversal da arquitetura cognitiva do SOT.**

Não deve existir a interpretação:

```text
Harness Cognitivo Genérico
        ↓
Módulo Trading
```

A arquitetura desejada é:

```text
MISSÃO DO SOT
      ↓
DOMÍNIO DE TRADING
      ↓
ESPECIALIZAÇÃO COGNITIVA
      ↓
8 CAMADAS COGNITIVAS
      ↓
MODELOS / PADRÕES / CAPACIDADES
      ↓
ENGINEERING CARDS
      ↓
IMPLEMENTAÇÃO
```

Assim, cada decisão de engenharia deve responder:

> **“Como essa capacidade deve existir especificamente em um sistema cognitivo de análise de Trading?”**

---

# 3. MISSÃO SUPERIOR DO SOT

A missão deve ser considerada requisito superior de todas as especificações.

O SOT deve:

> **observar, representar, interpretar, investigar, testar, confrontar, qualificar e sintetizar informações de mercado para produzir inteligência analítica de Trading, preservando hipóteses concorrentes, incertezas, evidências, invalidações e limitações dos modelos utilizados.**

O objetivo primário não é:

* prever obrigatoriamente o próximo movimento;
* gerar sinais a qualquer custo;
* maximizar quantidade de operações;
* escolher sempre uma hipótese;
* produzir uma entrada;
* executar operações.

O objetivo é:

> **produzir a melhor inteligência analítica possível diante das informações disponíveis e das limitações existentes.**

---

# 4. OBJETO DE ANÁLISE

O objeto primário do SOT é:

> **o comportamento observável e inferível do mercado em determinado ativo, contexto, horizonte e regime.**

A especificação deve permitir representar, entre outros:

* preço;
* estrutura;
* movimento;
* temporalidade;
* volatilidade;
* liquidez;
* volume quando disponível;
* contexto;
* sessões;
* regimes;
* relações entre ativos;
* eventos;
* padrões;
* estruturas fractais;
* ondas;
* desequilíbrios;
* zonas;
* comportamento histórico;
* hipóteses de participantes;
* possíveis mecanismos;
* consequências potenciais.

Essa enumeração é **expansível**.

Ela não constitui uma ontologia fechada do mercado.

---

# 5. REGRA DE NÃO CONFUSÃO ENTRE MODELO E REALIDADE

Nenhum modelo de Trading deve possuir autoridade ontológica sobre o mercado.

Devem ser tratados como modelos interpretativos:

* Elliott;
* SMC;
* ICT;
* Fibonacci;
* indicadores;
* padrões;
* estatísticas;
* modelos quantitativos;
* modelos próprios;
* conhecimento recuperado pelo RAG.

Portanto:

```text
MERCADO
   ↓
OBSERVAÇÕES
   ↓
EVIDÊNCIAS
   ↓
MODELOS
   ↓
HIPÓTESES
```

e nunca:

```text
MODELO
   ↓
REALIDADE
```

---

# 6. ESPECIALIZAÇÃO DAS OITO CAMADAS

Todas as oito camadas cognitivas anteriormente especificadas devem possuir uma implementação semântica e comportamental especializada para Trading.

Não se deve criar uma segunda versão genérica delas.

Deve-se especificar:

> **como a mesma capacidade cognitiva se manifesta no domínio de Trading.**

---

# 7. ONTOLOGIA ESPECIALIZADA

A camada ontológica deve permitir ao SOT representar o mercado em níveis múltiplos.

Exemplos:

### Observáveis

* preço;
* candle;
* máxima;
* mínima;
* fechamento;
* volume;
* volatilidade;
* tempo.

### Estruturais

* swing;
* tendência;
* range;
* estrutura;
* fractal;
* onda;
* grau estrutural.

### Institucionais / comportamentais

* liquidez;
* desequilíbrio;
* zonas;
* deslocamentos;
* estruturas interpretadas por SMC/ICT.

### Contextuais

* sessão;
* regime;
* volatilidade;
* ativo;
* timeframe;
* correlação;
* evento externo.

### Cognitivos

* hipótese;
* evidência;
* cenário;
* narrativa;
* invalidação;
* confiança;
* conflito.

A ontologia deve permanecer aberta à descoberta de entidades não previstas.

---

# 8. SEMÂNTICA ESPECIALIZADA

Toda interpretação de termos de Trading deve preservar:

* definição;
* contexto;
* escola/modelo de origem;
* timeframe;
* aplicação;
* significado operacional;
* possíveis ambiguidades.

Termos como:

* BOS;
* CHOCH;
* MSS;
* FVG;
* Order Block;
* Liquidity Sweep;
* Impulse;
* Correction;
* Wave;
* Extension;
* Retracement;

não devem ser tratados como significados universais quando diferentes escolas ou autores utilizarem definições diferentes.

---

# 9. ELLIOTT COMO MODELO ESPECIALIZADO

O conhecimento Elliott deve ser integrado como uma capacidade analítica especializada.

O SOT deve poder:

* construir contagens;
* manter contagens concorrentes;
* avaliar regras;
* avaliar guidelines;
* avaliar proporções;
* considerar graus;
* analisar fractalidade;
* analisar maturidade;
* testar invalidações;
* comparar interpretações.

Mas não deve assumir que:

> todo movimento precisa possuir uma contagem Elliott válida.

---

# 10. SMC E ICT COMO MODELOS ESPECIALIZADOS

SMC e ICT devem ser tratados como corpos de conhecimento e modelos interpretativos especializados.

O SOT deve poder investigar:

* liquidez;
* estrutura;
* deslocamento;
* desequilíbrio;
* zonas;
* mudanças estruturais;
* comportamento contextual;
* relações entre preço e liquidez.

Mas não deve assumir previamente que todo comportamento observado possui uma explicação SMC/ICT.

---

# 11. MULTIMODELAGEM

O SOT deve ser capaz de utilizar simultaneamente:

* Elliott;
* SMC;
* ICT;
* análise estrutural;
* contexto;
* estatística;
* indicadores;
* outros modelos relevantes.

Esses modelos podem:

* convergir;
* divergir;
* complementar-se;
* contradizer-se;
* explicar fenômenos diferentes;
* falhar simultaneamente.

A arquitetura deve preservar essa possibilidade.

---

# 12. CONFLUÊNCIA

Confluência não deve significar:

> quantidade de sinais favoráveis.

Deve representar, quando aplicável:

> **convergência de evidências independentes ou parcialmente independentes para uma hipótese.**

Evidências derivadas da mesma origem não devem receber automaticamente peso independente.

---

# 13. EVIDÊNCIA DE TRADING

Toda evidência relevante deve preservar sua origem.

Exemplos:

* observação direta do gráfico;
* dado de mercado;
* indicador;
* estrutura identificada;
* regra Elliott;
* regra SMC;
* regra ICT;
* backtest;
* estatística;
* conhecimento RAG;
* inferência;
* hipótese de mecanismo.

O SOT deve distinguir:

**observado → interpretado → inferido → hipotetizado.**

---

# 14. INDICADORES

Indicadores utilizados pelo SOT não devem ser tratados simplesmente como sinais.

Devem poder funcionar como:

* evidência;
* variável;
* filtro;
* confirmação;
* divergência;
* contexto;
* medição;
* instrumento de teste de hipótese.

Sua utilidade deve ser determinada empiricamente quando possível.

---

# 15. CALIBRAÇÃO DE INDICADORES

Quando um indicador for utilizado para apoiar uma hipótese de Trading, o SOT deve poder avaliar:

* contexto;
* timeframe;
* ativo;
* regime;
* parâmetros;
* histórico;
* frequência de ocorrência;
* estabilidade;
* sensibilidade;
* false positives;
* false negatives;
* desempenho fora da amostra.

O indicador não deve receber autoridade cognitiva simplesmente por possuir nome ou tradição de uso.

---

# 16. BACKTEST COMO EVIDÊNCIA

Backtests devem ser tratados como evidência condicionada.

A especificação deve considerar:

* período;
* ativo;
* timeframe;
* regime;
* custos;
* liquidez;
* slippage;
* seleção de dados;
* look-ahead;
* overfitting;
* múltiplos testes;
* estabilidade temporal.

Backtest não deve ser tratado como prova automática de validade futura.

---

# 17. CAUSALIDADE DE MERCADO

O SOT deve diferenciar:

* movimento observado;
* correlação;
* associação;
* hipótese causal;
* mecanismo;
* explicação retrospectiva.

O sistema não deve transformar uma narrativa de mercado em causalidade simplesmente porque ela explica bem o gráfico.

---

# 18. CONTRAFACTUAIS DE MERCADO

O SOT deve poder investigar:

* o que ocorreria sem determinado rompimento;
* sem determinado sweep;
* se o FVG não fosse preenchido;
* se uma contagem Elliott alternativa prevalecesse;
* se determinada estrutura falhasse;
* se o regime mudasse;
* se a evidência considerada principal fosse removida.

O objetivo é testar robustez e alternativas.

---

# 19. INCERTEZA DE MERCADO

A incerteza deve ser localizada em:

* dados;
* leitura estrutural;
* interpretação;
* contagem;
* modelo;
* regime;
* contexto;
* causalidade;
* probabilidade;
* cenário;
* decisão.

Não deve existir obrigatoriamente uma única “confidence” global.

---

# 20. PROBABILIDADE DE MERCADO

Quando houver fundamento suficiente, o SOT poderá utilizar:

* frequência;
* probabilidade condicional;
* distribuição;
* intervalos;
* cenários;
* plausibilidade qualitativa.

Mas:

> **nenhum percentual deve ser produzido apenas para conferir aparência quantitativa à análise.**

---

# 21. DECISÃO ESPECIALIZADA

A camada decisional do SOT deve distinguir:

```text
OBSERVAÇÃO
↓
HIPÓTESE
↓
EVIDÊNCIA
↓
CENÁRIO
↓
INVALIDAÇÃO
↓
ANÁLISE DE RISCO
↓
DELIBERAÇÃO
```

Uma hipótese não é automaticamente um sinal.

Um sinal não é automaticamente uma decisão.

Uma decisão analítica não é automaticamente execução financeira.

---

# 22. METACOGNIÇÃO DE TRADING

O SOT deve monitorar especificamente:

* viés de confirmação;
* apego à primeira leitura;
* excesso de confiança;
* narrativa retrospectiva;
* cherry-picking;
* overfitting;
* viés de recência;
* interpretação forçada;
* contagem estrutural excessivamente conveniente;
* confluência artificial;
* dependência entre evidências;
* ignorância de invalidação.

A metacognição não deve ser transformada em checklist obrigatório.

---

# 23. REGIME COMO VARIÁVEL COGNITIVA

Regime deve ser tratado como possível modificador de:

* probabilidade;
* causalidade;
* desempenho de indicadores;
* validade de padrões;
* comportamento estrutural;
* liquidez;
* volatilidade;
* eficácia de estratégias.

Uma relação histórica não deve ser transferida automaticamente entre regimes.

---

# 24. TIMEFRAME COMO CONTEXTO

Timeframe não deve ser apenas parâmetro técnico.

Ele modifica:

* resolução;
* estrutura observável;
* horizonte;
* ruído;
* relevância de eventos;
* interpretação;
* validade de determinadas hipóteses.

O SOT deve preservar essas diferenças.

---

# 25. HIERARQUIA TEMPORAL

O SOT deve ser capaz de analisar relações entre:

* contexto superior;
* contexto intermediário;
* contexto operacional.

Porém, nenhuma regra universal deve determinar que timeframe superior sempre “vence”.

Conflitos temporais devem ser analisados.

---

# 26. TRADINGVIEW COMO AMBIENTE OBSERVACIONAL

O TradingView deve ser considerado fonte/ambiente de observação do mercado, quando utilizado pelo SOT.

A arquitetura deve separar:

**dado observado**

de:

**interpretação produzida pelo SOT.**

O SOT não deve assumir que uma visualização específica corresponde automaticamente à realidade completa do mercado.

---

# 27. RAG ESPECIALIZADO

O RAG do SOT deve priorizar conhecimento relevante para:

* Trading;
* Elliott;
* SMC;
* ICT;
* microestrutura;
* indicadores;
* estatística;
* probabilidade;
* risco;
* comportamento de mercado;
* métodos de validação;
* backtesting;
* TradingView.

Mas o RAG não deve funcionar como autoridade automática.

Conhecimento recuperado deve ser:

**adquirido → formado → validado → contextualizado → utilizado.**

---

# 28. RECUPERAÇÃO CONTEXTUAL

O conhecimento recuperado deve ser selecionado considerando:

* ativo;
* timeframe;
* regime;
* problema;
* hipótese;
* escola;
* objetivo analítico;
* evidência disponível.

Não deve existir recuperação genérica de conhecimento simplesmente porque contém palavras semelhantes.

---

# 29. ESPECIALIZAÇÃO DAS ENGINEERING CARDS

Toda Engineering Card deve possuir obrigatoriamente uma dimensão:

## Contexto de Trading

Essa dimensão deve responder:

1. Qual problema de análise de Trading ela resolve?
2. Em qual contexto de mercado?
3. Qual objeto de mercado envolve?
4. Qual capacidade cognitiva utiliza?
5. Qual impacto possui na análise?
6. Quais modelos de Trading podem consumi-la?
7. Quais evidências utiliza?
8. Quais hipóteses pode apoiar ou refutar?
9. Quais riscos cognitivos introduz?
10. Como sua validade será testada em mercado?

---

# 30. NOVO CAMPO OBRIGATÓRIO — DOMÍNIO DE APLICAÇÃO

Toda Engineering Card deve declarar:

**Domínio de Aplicação**

Exemplos:

* Structural Trading;
* Elliott;
* SMC;
* ICT;
* Market Context;
* Probability;
* Risk;
* Indicator Validation;
* Multi-Timeframe Analysis;
* Hypothesis Testing;
* Evidence Fusion;
* Regime Analysis.

Uma Card sem domínio de aplicação definido não deve avançar para implementação.

---

# 31. NOVO CAMPO — FUNÇÃO COGNITIVA NO SOT

Toda Card deve declarar:

> **Qual capacidade cognitiva do SOT ela amplia?**

Exemplos:

* percepção;
* representação;
* interpretação;
* hipótese;
* evidência;
* causalidade;
* contrafactual;
* incerteza;
* probabilidade;
* decisão;
* metacognição;
* aprendizagem.

---

# 32. NOVO CAMPO — IMPACTO ANALÍTICO

Toda Card deve declarar se afeta:

* descoberta;
* interpretação;
* evidência;
* hipótese;
* cenário;
* invalidação;
* confiança;
* decisão;
* aprendizagem.

---

# 33. NOVO CAMPO — DEPENDÊNCIA DE REGIME

Quando aplicável, toda capacidade deve declarar:

* independente de regime;
* dependente de regime;
* desconhecida.

Não se deve presumir estabilidade universal.

---

# 34. NOVO CAMPO — DEPENDÊNCIA TEMPORAL

A Card deve declarar se seu comportamento depende de:

* timeframe;
* horizonte;
* sessão;
* sequência temporal;
* atraso;
* maturidade estrutural.

---

# 35. NOVO CAMPO — VALIDAÇÃO EMPÍRICA

Quando a capacidade possuir comportamento mensurável, deve declarar como será investigada:

* histórico;
* backtest;
* walk-forward;
* teste fora da amostra;
* análise por regime;
* análise por ativo;
* análise por timeframe;
* teste adversarial;
* comparação contra baseline.

---

# 36. NOVO CAMPO — LIMITES DE GENERALIZAÇÃO

Toda capacidade empiricamente validada deve declarar:

> **Onde a evidência deixa de justificar sua aplicação?**

Exemplos:

* ativo específico;
* período específico;
* regime específico;
* timeframe específico;
* condição específica.

---

# 37. DESIGN PATTERNS DEVEM SER DOMINIAIS

Os Design Patterns do SOT não devem ser apenas padrões genéricos de engenharia.

Devem ser padrões de:

> **engenharia cognitiva aplicada à análise de Trading.**

Os padrões anteriormente previstos — como hipóteses concorrentes, refutação e fusão de evidências — devem ser preservados e especializados ao domínio. O documento original já aponta nessa direção ao propor esses padrões como soluções arquiteturais reutilizáveis.

---

# 38. EXEMPLOS DE PADRÕES DOMINIAIS

Entre os possíveis padrões:

### Concurrent Market Hypotheses

Suportar múltiplas leituras de mercado.

### Market Evidence Provenance

Preservar origem de toda evidência.

### Regime-Aware Analysis

Condicionar interpretações ao regime.

### Multi-Timeframe Context

Preservar relações temporais.

### Model Competition

Permitir Elliott, SMC, ICT e outras hipóteses competirem.

### Market Refutation

Buscar condições que invalidem a leitura.

### Indicator Evidence Pattern

Tratar indicadores como evidência e não como autoridade.

### Backtest Evidence Pattern

Tratar backtest como evidência condicionada.

### Narrative Separation

Separar narrativa explicativa de evidência observada.

### Confidence Calibration

Impedir confiança desproporcional à evidência.

---

# 39. GOVERNANÇA ESPECIALIZADA

Governança do SOT deve considerar riscos próprios de análise financeira:

* overfitting;
* drift;
* falsa estabilidade;
* degradação de regime;
* alteração de mercado;
* mudança de comportamento;
* falsa confiança;
* contaminação de conhecimento;
* validação insuficiente.

---

# 40. LEARNING ESPECIALIZADO

O aprendizado do SOT deve aprender não somente:

> “qual resultado aconteceu?”

mas também:

* qual hipótese estava ativa;
* qual evidência existia;
* qual regime estava presente;
* qual modelo foi utilizado;
* quais alternativas existiam;
* qual premissa falhou;
* qual evidência foi ignorada;
* se houve erro de interpretação;
* se houve mudança estrutural.

---

# 41. PROIBIÇÃO DE APRENDIZADO INGÊNUO

O SOT não deve aprender:

> resultado positivo = estratégia correta.

Nem:

> resultado negativo = estratégia errada.

O resultado deve ser interpretado no contexto probabilístico, causal, temporal e estrutural correspondente.

---

# 42. EXPLAINABILITY ESPECIALIZADA

Toda explicação relevante deve poder distinguir:

### Observado

O que estava efetivamente presente nos dados.

### Interpretado

Como o sistema interpretou.

### Hipotetizado

O que o sistema propôs.

### Evidenciado

O que sustenta a hipótese.

### Inferido

O que foi derivado.

### Incerto

O que permanece desconhecido.

### Invalidado

O que deixou de ser sustentado.

Essa separação é obrigatória para análises de alto impacto.

---

# 43. MÉTRICAS

Métricas do SOT não devem ser limitadas a:

* acurácia;
* win rate;
* precisão de previsão.

Devem considerar também:

* calibração;
* robustez;
* estabilidade;
* qualidade das hipóteses;
* qualidade da evidência;
* qualidade das invalidações;
* detecção de ambiguidades;
* capacidade de reconhecer erro;
* degradação por regime;
* custo cognitivo;
* latência;
* economicidade.

---

# 44. CRITÉRIO DE SUCESSO DO SOT

O sucesso do SOT não deve ser definido simplesmente por:

> “acertar o próximo movimento.”

Deve ser definido pela capacidade de:

> **produzir análises mais informadas, rastreáveis, robustas, calibradas, adaptativas e cognitivamente honestas para apoiar decisões de Trading.**

---

# 45. INTEGRAÇÃO COM EXECUÇÃO

O SOT deve permanecer conceitualmente separado da execução financeira.

TradingView, Bot Finance, Telegram, exchange e wallet podem aparecer como integrações do ecossistema, conforme o documento original já prevê.

Entretanto:

> **integração não significa fusão de responsabilidades cognitivas e financeiras.**

O SOT produz inteligência/sinal conforme sua missão.

O mecanismo financeiro externo permanece responsável por sua própria função.

---

# 46. PRINCÍPIO DE NÃO EXECUÇÃO COGNITIVA

A especialização em Trading não deve transformar o Harness em executor automático de operações.

A cognição deve permanecer separada da execução.

Isso preserva:

* rastreabilidade;
* governança;
* isolamento de responsabilidade;
* possibilidade de revisão;
* segurança arquitetural.

---

# 47. NÃO RESTRIÇÃO COGNITIVA

A especialização Trading não pode transformar:

* Elliott;
* SMC;
* ICT;
* Fibonacci;
* indicadores;
* padrões;
* modelos estatísticos;

em caminhos obrigatórios.

O agente deve poder concluir:

> “Nenhum dos modelos disponíveis explica adequadamente a observação.”

Esse resultado é válido.

---

# 48. PRINCÍPIO DE DESCOBERTA

O SOT deve poder descobrir:

* nova estrutura;
* nova variável;
* novo padrão;
* nova relação;
* novo mecanismo;
* novo regime;
* nova hipótese;
* novo conflito entre modelos.

A especificação deve criar **capacidade de descoberta**, não apenas repertório de técnicas conhecidas.

---

# 49. TESTE DE ESPECIALIZAÇÃO

Nenhuma especificação do SOT será considerada suficientemente especializada se puder ser transplantada para:

> medicina, logística, marketing ou outro domínio

sem mudanças materiais.

O componente pode possuir princípios gerais.

Porém, seu comportamento esperado deve estar contextualizado para análise de Trading.

---

# 50. TESTE DE NÃO REDUÇÃO

Ao mesmo tempo, nenhuma especialização será considerada adequada se transformar o SOT em:

* checklist;
* robô de estratégia;
* árvore fixa;
* sistema de sinais;
* executor de regras;
* classificador fechado.

A especialização deve aumentar:

> **capacidade cognitiva no domínio.**

Não diminuir:

> **liberdade cognitiva.**

---

# 51. TESTE DE MISSÃO

Para cada nova especificação, deve ser possível responder:

> **“Como esta capacidade contribui para a missão do SOT?”**

Se não houver resposta clara:

* a capacidade deve ser questionada;
* ou sua prioridade deve ser reduzida;
* ou deve ser reformulada.

---

# 52. TESTE DE MERCADO

Para cada capacidade analítica, deve ser possível perguntar:

> “Como seu comportamento pode mudar diante de diferentes ativos, timeframes, regimes e condições de mercado?”

Quando relevante, a resposta deve fazer parte da especificação.

---

# 53. TESTE DE MODELO

Para cada capacidade baseada em uma escola ou técnica:

> “O que acontece se o modelo estiver errado?”

A especificação deve prever a possibilidade de:

* conflito;
* redução de confiança;
* hipótese alternativa;
* abandono;
* descoberta.

---

# 54. TESTE DE EVIDÊNCIA

Para cada conclusão material:

> “O que foi observado e o que foi inferido?”

O Harness deve impedir que inferência seja apresentada como observação.

---

# 55. TESTE DE INVALIDAÇÃO

Toda hipótese relevante deve possuir, quando aplicável:

> condição capaz de enfraquecê-la ou invalidá-la.

Isso não significa que toda análise precise produzir uma fórmula rígida de invalidação.

Significa que:

> **nenhuma hipótese deve ser epistemicamente blindada contra refutação.**

---

# 56. TESTE DE ALTERNATIVAS

Quando múltiplas interpretações forem plausíveis, o SOT deve poder preservá-las.

O padrão de hipóteses concorrentes já previsto no documento original deve, portanto, ser entendido como **capacidade cognitiva fundamental do sistema de análise de Trading**, e não apenas como funcionalidade de uma Card específica.

---

# 57. TESTE DE GENERALIZAÇÃO

Uma capacidade validada historicamente deve ser questionada:

> “Em quais condições ela pode deixar de funcionar?”

A generalização deve ser explicitamente condicionada.

---

# 58. TESTE DE SURPRESA

O Harness deve preservar eventos que não se encaixem nos modelos existentes.

Uma observação inesperada deve poder provocar:

```text
SURPRESA
   ↓
INVESTIGAÇÃO
   ↓
REVISÃO DO MODELO
   ↓
NOVA HIPÓTESE
```

e não:

```text
SURPRESA
   ↓
FORÇAR O MODELO EXISTENTE
```

---

# 59. NOVA REGRA PARA TODA ENGINEERING CARD

Toda Engineering Card futura deverá possuir, além dos campos já estabelecidos no documento, no mínimo:

| Campo                     | Obrigatoriedade  |
| ------------------------- | ---------------- |
| Missão SOT atendida       | Obrigatório      |
| Domínio de Trading        | Obrigatório      |
| Função cognitiva          | Obrigatório      |
| Objeto de mercado         | Quando aplicável |
| Contexto de aplicação     | Obrigatório      |
| Timeframe/horizonte       | Quando aplicável |
| Regime                    | Quando aplicável |
| Modelo/escola             | Quando aplicável |
| Evidências                | Obrigatório      |
| Hipóteses suportadas      | Quando aplicável |
| Hipóteses refutáveis      | Quando aplicável |
| Limitações                | Obrigatório      |
| Generalização             | Obrigatório      |
| Validação empírica        | Quando aplicável |
| Risco cognitivo           | Obrigatório      |
| Impacto analítico         | Obrigatório      |
| Critério de não-restrição | Obrigatório      |

---

# 60. REGRA DE DERIVAÇÃO

Toda Engineering Card deve poder ser rastreada:

```text
MISSÃO DO SOT
      ↓
OBJETIVO ANALÍTICO
      ↓
CAPACIDADE COGNITIVA
      ↓
DOMÍNIO DE TRADING
      ↓
DESIGN PATTERN
      ↓
ENGINEERING CARD
      ↓
CONTRATO
      ↓
IMPLEMENTAÇÃO
      ↓
VALIDAÇÃO
```

Nenhuma implementação deve existir sem essa cadeia de derivação.

---

# 61. REGRA DE RETROALIMENTAÇÃO

A cadeia também deve funcionar no sentido inverso:

```text
RESULTADO
   ↓
VALIDAÇÃO
   ↓
APRENDIZADO
   ↓
REVISÃO DA CARD
   ↓
REVISÃO DO PATTERN
   ↓
REVISÃO DA CAPACIDADE
   ↓
REVISÃO DA ESPECIALIZAÇÃO
```

Quando necessário.

---

# 62. ALTERAÇÃO NA DEFINIÇÃO DO SES

O **SOT Engineering Specification** deve ser entendido como:

> **especificação de engenharia de um sistema cognitivo especializado em análise de Trading.**

Não como:

> especificação de um framework genérico de agentes ao qual Trading foi adicionado.

---

# 63. ALTERAÇÃO NA DEFINIÇÃO DO HARNESS

O Harness Cognitivo do SOT deve ser entendido como:

> **o conjunto de capacidades, restrições de segurança, contratos, padrões, mecanismos de avaliação e estruturas de contexto que orientam um LLM a exercer cognição de alta qualidade sobre problemas de análise de Trading.**

---

# 64. DISTINÇÃO FUNDAMENTAL

O SOT deve possuir:

### Especialização forte

em:

* domínio;
* linguagem;
* conhecimento;
* contexto;
* modelos;
* evidência;
* validação;
* avaliação.

### Liberdade forte

em:

* formulação;
* hipótese;
* interpretação;
* descoberta;
* associação;
* investigação;
* refutação;
* reformulação;
* escolha do modelo;
* combinação de modelos.

Essa combinação constitui a especialização cognitiva desejada.

---

# 65. PRINCÍPIO MESTRE DA EMENDA

> **Tudo no SOT deve ser especializado para a missão de análise de Trading; nada no SOT deve ser tão especializado que impeça o sistema de descobrir que sua própria representação, modelo, hipótese ou método de análise está errado.**

---

# 66. CRITÉRIO FINAL DE ACEITAÇÃO

A emenda será considerada corretamente incorporada quando:

1. toda camada cognitiva possuir interpretação específica para Trading;
2. toda Engineering Card declarar sua função na missão do SOT;
3. todo Design Pattern for contextualizado ao domínio;
4. toda capacidade relevante considerar mercado, contexto, regime e horizonte;
5. Elliott, SMC e ICT forem tratados como modelos e não como realidade;
6. indicadores forem tratados como instrumentos de evidência/análise, não como autoridades;
7. backtests forem tratados como evidência condicionada;
8. hipóteses concorrentes forem preservadas;
9. evidências possuírem proveniência;
10. incertezas forem explicitamente representáveis;
11. invalidação permanecer possível;
12. mudanças de regime puderem alterar conclusões;
13. novas hipóteses puderem ser descobertas;
14. modelos existentes puderem ser rejeitados;
15. a execução financeira permanecer separada da cognição;
16. a especificação não possa ser reduzida a um checklist de Trading;
17. o LLM mantenha liberdade cognitiva para produzir análises não previstas;
18. toda capacidade possa ser justificada pela missão do SOT.

---

# 67. DISPOSIÇÃO DE INCORPORAÇÃO

Esta emenda deve ser incorporada **antes da elaboração definitiva das Engineering Cards**, pois altera o critério pelo qual cada Card será especificada.

Ela passa a ser uma regra superior às especificações individuais.

Portanto:

> **nenhuma Engineering Card existente ou futura deve ser considerada definitivamente especificada sem ser reavaliada sob esta emenda.**

---

# 68. RESULTADO ARQUITETURAL

Após a incorporação desta emenda, o SOT deixa de ser conceitualmente:

```text
Cognitive Harness
+
Trading Modules
```

e passa a ser:

```text
                    MISSÃO SOT
                       │
              ANÁLISE DE TRADING
                       │
          ┌────────────┴────────────┐
          │                         │
   DOMÍNIO DE MERCADO        LIBERDADE COGNITIVA
          │                         │
          └────────────┬────────────┘
                       ↓
               COGNITIVE KERNEL
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   ONTOLOGIA       SEMÂNTICA      CAUSALIDADE
        ↓              ↓              ↓
 CONTRAFACTUAL     INCERTEZA       PROBABILIDADE
        ↓              ↓              ↓
       DECISÃO       METACOGNIÇÃO
               ↓
        ESPECIALIZAÇÃO SOT
               ↓
     ┌─────────┼─────────┐
     ↓         ↓         ↓
  ELLIOTT     SMC       ICT
     │         │         │
     └─────────┼─────────┘
               ↓
      EVIDÊNCIAS / MODELOS
               ↓
       HIPÓTESES / CENÁRIOS
               ↓
       TESTE / INVALIDAÇÃO
               ↓
        INTELIGÊNCIA SOT
```

### Princípio definitivo

> **O Trading define o domínio da cognição.
> A missão do SOT define a finalidade da cognição.
> As oito camadas definem as capacidades cognitivas.
> O Harness define como preservar, orientar, avaliar e aprimorar essas capacidades.
> Nenhum desses níveis deve substituir a capacidade do LLM de descobrir algo que não estava previsto.**
