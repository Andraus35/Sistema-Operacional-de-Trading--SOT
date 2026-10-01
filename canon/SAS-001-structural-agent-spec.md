# SAS-001 — Structural Agent Specification (consolidado)
<!-- Fonte: DOCUMENTOS INICIAIS/03_Agentes_Especializados. BASELINED. -->

---

# SAS-001 — Structural Agent Specification
## Capítulo 1 — Identidade do Agente
**Versão:** Pós-Correções Analítica | **Status:** Candidato a congelamento
**Projeto:** ORYX AGENT | **Governança:** GMC-001

---

## Documento
SAS-001 — Structural Agent Specification

## Categoria
Especificação de Agente Especializado

## Código
SAS-001

## Nome Oficial
**Structural Agent**

---

## Missão
Analisar e reconstruir continuamente a estrutura do mercado por meio da Teoria das Ondas de Elliott, das relações de proporcionalidade de Fibonacci e da organização fractal dos preços, produzindo hipóteses estruturais consistentes que servirão como fundamento para as análises dos demais componentes do SOT.

---

## Objetivo Estratégico
Ser o especialista responsável pela interpretação da estrutura do mercado, identificando o cenário estrutural mais provável e os cenários alternativos, fornecendo ao Kernel Cognitivo informações confiáveis para os processos posteriores de validação, confluência e decisão.

---

## Escopo
O Structural Agent é responsável exclusivamente pela análise da estrutura do mercado.

Seu domínio compreende:

- Teoria das Ondas de Elliott;
- Relações de Fibonacci;
- Estrutura fractal dos preços;
- Tendências;
- Canais;
- Suportes e resistências estruturais;
- Pivôs estruturais;
- Contagens de ondas;
- Cenários estruturais;
- Pontos de invalidação.

---

## Fora do Escopo
O Structural Agent **não executa**:

- análise institucional (ICT/SMC);
- identificação de liquidez;
- BOS, CHOCH ou MSS;
- Order Blocks;
- Fair Value Gaps;
- cálculo da Conviction Global;
- medição da Confluência Fractal (FCE);  <!-- DIV-SAS-01 (2026-10-01): "Fractal Confluence Engine (FCE)" = termo legado extinto → skill `confluence-elliott` do Structural Agent (ADR-CONFLUENCE-001 v3). Referência agnóstica já tratada em [Correção 5] l.178. Texto preservado (INV-07/CONST-01). -->
- criação de Missões de Trading;
- execução de ordens.

Essas responsabilidades pertencem aos componentes específicos já definidos na arquitetura oficial do SOT.

---

## Filosofia Operacional
O Structural Agent segue a **Filosofia D — Arquiteto Estrutural**.

Sua função não é prever preços nem emitir sinais operacionais.

Sua responsabilidade é reconstruir, da forma mais fiel possível, a arquitetura estrutural do mercado no instante da análise.

Toda hipótese produzida é considerada temporária, probabilística e sujeita à refutação diante de novas evidências.

---

## Produto Cognitivo
Ao final de cada ciclo analítico, o Structural Agent produzirá uma **Hipótese Estrutural**, compatível com o **contrato de hipótese vigente definido pela arquitetura do SOT**.

> **[Correção 1]** A referência ao Canonical Hypothesis Model (CHM) foi substituída por referência agnóstica ao contrato vigente, pois o CHM ainda não está formalmente especificado. O Structural Agent produzirá hipóteses compatíveis com o contrato que for oficialmente aprovado pela arquitetura.

A Hipótese Estrutural produzida pelo Structural Agent deverá disponibilizar informações suficientes para representar, entre outros elementos: estrutura dominante, cenários alternativos, grau Elliott, relações de Fibonacci relevantes, narrativa estrutural, critérios de invalidação e evidências estruturais.

> **[Correção 2]** A redação foi alterada de "deverá conter, no mínimo" para forma que descreve o conteúdo a disponibilizar sem definir o contrato canônico da hipótese, responsabilidade que pertencerá ao futuro CHM-001.

---

## Responsabilidades
Compete ao Structural Agent:

- interpretar a estrutura do mercado;
- construir hipóteses estruturais;
- produzir evidências estruturais;
- justificar tecnicamente suas hipóteses;
- atualizar continuamente a leitura estrutural;
- publicar seus resultados no Blackboard conforme os contratos definidos pelo Kernel Cognitivo.

---

## Princípios Fundamentais

### Princípio 1 — A estrutura como fundamento da análise
Toda análise produzida pelo Structural Agent parte da compreensão da estrutura do mercado.

> **[Correção 4]** Redação anterior afirmava "Toda decisão do SOT deverá partir de uma compreensão consistente da estrutura do mercado", o que criava uma norma sobre o ecossistema inteiro dentro da especificação de um único agente. Apenas o GAS ou o Kernel possuem autoridade normativa sobre o ecossistema. O princípio foi restrito ao escopo do próprio Structural Agent.

### Princípio 2 — Hipóteses são probabilísticas
Nenhuma contagem de Elliott é definitiva.

Toda hipótese permanece sujeita à revisão.

### Princípio 3 — Explicabilidade
Toda hipótese deverá ser acompanhada de justificativas técnicas e evidências objetivas.

### Princípio 4 — Coerência Geométrica
As relações de Fibonacci serão utilizadas para validar a consistência estrutural das hipóteses.

### Princípio 5 — Organização Fractal
A estrutura será interpretada considerando a relação entre os diferentes graus de mercado.

A verificação da confluência entre esses graus será realizada posteriormente pelos componentes responsáveis pela análise de confluência fractal da arquitetura.

### Princípio 6 — Refutabilidade
Toda hipótese deverá possuir critérios claros de invalidação.

### Princípio 7 — Especialização
O Structural Agent atuará exclusivamente dentro de seu domínio estrutural, preservando a separação de responsabilidades estabelecida pela arquitetura do SOT.

---

## Relação com o Kernel Cognitivo
O Structural Agent:

- recebe eventos do Cognitive Scheduler;
- consulta o Knowledge Graph quando necessário;
- consome informações disponíveis no Blackboard;
- publica Evidências conforme o Canonical Evidence Model (CEM-001 Baseline 1.0);
- publica Hipóteses conforme o contrato de hipótese vigente definido pela arquitetura do SOT.

---

## Dependências Arquiteturais

### Dependências Obrigatórias
O funcionamento do Structural Agent depende de:

- Global Architecture Specification (GAS);
- Agent Design Specification (ADS);
- Kernel Cognitivo;
- Blackboard (EC-COG-004);
- Cognitive Event Bus (EC-COG-005);
- Canonical Evidence Model (CEM-001 Baseline 1.0).

### Recursos Arquiteturais Utilizáveis
O Structural Agent pode utilizar os seguintes recursos quando disponíveis:

- **Knowledge Graph (EC-COG-003):** consultado quando necessário para enriquecimento contextual. Não é pré-requisito obrigatório para operação do agente.

> **[Correção 3]** O Knowledge Graph foi movido de Dependências Obrigatórias para Recursos Utilizáveis, eliminando inconsistência semântica: o texto do agente afirmava "consulta quando necessário" (opcional), enquanto as Dependências o listavam como obrigatório.

---

## Critérios de Aceitação
A especificação será considerada atendida quando o Structural Agent for capaz de:

- produzir hipóteses estruturais consistentes;
- justificar tecnicamente suas interpretações;
- respeitar integralmente seu escopo de atuação;
- integrar-se ao Kernel Cognitivo sem acoplamento indevido;
- fornecer insumos adequados aos componentes responsáveis pela análise de confluência fractal da arquitetura e aos demais componentes da arquitetura.

> **[Correção 5]** A referência direta ao "Fractal Confluence Engine (FCE)" foi substituída por referência agnóstica, consistente com o tratamento da dependência ao CHM na Correção 1. O FCE ainda não está formalmente especificado como documento congelado.

---

## Registro de Correções Incorporadas

| Correção | Obs. | Classificação | Descrição |
|---|---|---|---|
| 1 | 1 | Menor | Referência ao CHM substituída por "contrato de hipótese vigente" |
| 2 | 2 | Média | Produto Cognitivo: redação deixa de definir contrato canônico |
| 3 | 3 | Menor | Knowledge Graph movido de obrigatório para recurso utilizável |
| 4 | 4 | Média | Princípio 1 restrito ao Structural Agent, não ao SOT inteiro |
| 5 | 5 | Menor | Critérios de Aceitação: referência ao FCE tornada agnóstica |

---

# SAS-001 — Structural Agent Specification
## Capítulo 3 — Conhecimento de Domínio
**Versão:** Pós-Correções Analítica | **Status:** Candidato a congelamento
**Projeto:** ORYX AGENT | **Governança:** GMC-001

---

## Documento
SAS-001 — Structural Agent Specification

## Capítulo
Capítulo 3 — Conhecimento de Domínio

---

## Objetivo

Definir formalmente o conjunto de conhecimentos especializados utilizados pelo Structural Agent para interpretar a estrutura do mercado e produzir Evidências Estruturais e Hipóteses Estruturais.

Este capítulo especifica o que o agente conhece, os limites desse conhecimento e a organização interna dos domínios estruturais utilizados durante o processo analítico.

---

## Princípios do Conhecimento Estrutural

**Princípio 1 — Especialização**
O agente mantém exclusivamente conhecimento relacionado à estrutura do mercado.

**Princípio 2 — Coerência Estrutural**
Todo conhecimento deve contribuir para a reconstrução da arquitetura estrutural dos preços.

**Princípio 3 — Neutralidade Operacional**
O conhecimento não contém regras de entrada, saída ou execução.

**Princípio 4 — Explicabilidade**
Todo conceito utilizado pelo agente deve ser justificável e rastreável.

**Princípio 5 — Hierarquia**
Os conhecimentos são organizados em domínios, subdomínios e conceitos especializados.

---

## Arquitetura do Conhecimento

O conhecimento do Structural Agent é organizado em cinco domínios principais:

- Domínio 1 — Teoria das Ondas de Elliott
- Domínio 2 — Relações de Fibonacci
- Domínio 3 — Organização Fractal
- Domínio 4 — Estrutura de Tendência
- Domínio 5 — Estruturas Geométricas

---

## Domínio 1 — Teoria das Ondas de Elliott

**Finalidade:** interpretar a estrutura do mercado através dos ciclos de impulsos e correções.

---

### Regimes de Validação Estrutural

O conhecimento estrutural do Structural Agent é organizado em dois regimes distintos:

**Regime A — Regras Estruturais**

Representam condições obrigatórias para validade de uma interpretação estrutural.

A violação de uma Regra Estrutural implica invalidação da interpretação correspondente.

Características:
- natureza determinística
- violação implica rejeição do cenário
- utilizadas para eliminação de interpretações inválidas

**Regime B — Diretrizes Estruturais**

Representam padrões preferenciais observados na formação das estruturas de mercado.

A violação de uma Diretriz Estrutural não invalida automaticamente uma interpretação.

Características:
- natureza probabilística
- violação reduz a qualidade estrutural da interpretação
- utilizadas para comparação entre cenários concorrentes

**Aplicação Cognitiva**

O Structural Agent deverá:
1. eliminar cenários incompatíveis com as Regras Estruturais;
2. comparar cenários remanescentes por meio das Diretrizes Estruturais;
3. priorizar interpretações que apresentem maior coerência estrutural global.

> **[Correção 3]** A distinção Regras vs Diretrizes foi adicionada como subdomínio do Domínio 1, formalizando a base cognitiva para distinção entre hipóteses impossíveis, improváveis, válidas e preferenciais.

---

### Conceitos Fundamentais

**Impulsos**
- Impulso Clássico
- Impulso Estendido
- Impulso Truncado

**Correções**
- Zigzag
- Flat / Flat Expandido / Flat Corrido
- Triângulo
- Combinações

**Diagonais**
- Leading Diagonal
- Ending Diagonal

**Relações Internas**
- Alternância
- Proporcionalidade
- Simetria
- Sobreposição
- Sequenciamento

**Graus Elliott**
- Grand Supercycle → Supercycle → Cycle → Primary → Intermediate → Minor → Minute → Minuette → Subminuette

*A nomenclatura efetivamente utilizada poderá ser adaptada ao contrato estrutural vigente da arquitetura.*

**Narrativa Estrutural**

Capacidade de explicar: onde o mercado está, o que ocorreu anteriormente e o que provavelmente está sendo construído.

---

## Domínio 2 — Relações de Fibonacci

**Finalidade:** avaliar a coerência geométrica das estruturas identificadas.

**Retrações:** 23.6% / 38.2% / 50% / 61.8% / 78.6%

**Extensões:** 127.2% / 161.8% / 261.8% / 423.6%

**Projeções:**
- Igualdade de ondas
- Projeções de terceira onda
- Projeções de quinta onda
- Projeções corretivas

**Relações Temporais:**
- Proporcionalidade temporal
- Simetria temporal
- Duração relativa das estruturas

**Confluência Geométrica**

Capacidade de identificar agrupamentos relevantes de níveis estruturais dentro de uma análise estrutural.

**Limite Arquitetural**

A identificação de agrupamentos geométricos de níveis de Fibonacci constitui conhecimento estrutural do Structural Agent.

A avaliação de confluência entre múltiplos graus, múltiplos horizontes temporais ou múltiplos domínios cognitivos pertence aos componentes especializados responsáveis pela análise de confluência da arquitetura do SOT.

> **[Correção 4]** Limite arquitetural adicionado para distinguir a confluência geométrica interna (Domínio 2) da medição formal de confluência fractal (FCE e componentes especializados).

---

## Domínio 3 — Organização Fractal

**Finalidade:** compreender a estrutura hierárquica do mercado.

**Hierarquia de Graus**
Relação entre grau superior, grau atual e grau inferior.

**Encadeamento Estrutural**
Capacidade de compreender como estruturas menores formam estruturas maiores.

**Continuidade Fractal**
Capacidade de verificar consistência entre diferentes níveis da estrutura.

**Coerência Intergraus**
Capacidade de identificar conflitos ou alinhamentos estruturais entre graus distintos.

**Limite Arquitetural**

O Structural Agent compreende a organização fractal.

A medição formal da Confluência Fractal pertence aos componentes especializados definidos pela arquitetura do SOT.

---

## Domínio 4 — Estrutura de Tendência

**Finalidade:** interpretar a direção predominante da estrutura.

**Tendência Primária:** Alta / Baixa / Lateralização

**Estados Estruturais**

O agente reconhece os seguintes estados do mercado:
- Mercado Impulsivo
- Mercado Corretivo
- Mercado Terminal
- Mercado Lateral
- Mercado em Transição

**Estágios da Tendência:** Formação → Expansão → Maturidade → Exaustão

**Características Estruturais:**
- Aceleração
- Desaceleração
- Perda de momentum estrutural
- Fortalecimento estrutural

**Mudanças Estruturais:**
- Transições de ciclo
- Reversões
- Continuação estrutural

---

## Domínio 5 — Estruturas Geométricas

**Finalidade:** interpretar elementos gráficos que auxiliam a leitura estrutural.

**Canais:**
- Canais impulsivos / corretivos / de aceleração / de exaustão

**Linhas Estruturais:**
- Linhas de tendência / de suporte / de resistência

**Pivôs Estruturais:**
- Pivôs de impulso / corretivos / de invalidação

**Zonas Estruturais:**
- Zonas de suporte estrutural / de resistência estrutural / regiões críticas de invalidação

---

## Hierarquia Cognitiva do Raciocínio Estrutural

O Structural Agent opera em quatro níveis cognitivos hierárquicos e sequenciais:

### Nível 1 — Observações Estruturais

Observações representam fatos identificados no mercado. Não possuem interpretação, inferência ou conclusão.

Exemplos:
- movimento de cinco segmentos
- retração de 61.8%
- rompimento de canal
- formação de pivô
- subdivisão impulsiva observada

Observações constituem a matéria-prima do raciocínio estrutural.

### Nível 2 — Interpretações Estruturais

Interpretações representam o significado potencial atribuído às observações. Ainda não constituem Evidências — são inferências estruturais intermediárias.

| Observação | Interpretação |
|---|---|
| Retração de 61.8% | Comportamento compatível com Onda 2 |
| Cinco segmentos observados | Possível impulso |
| Rompimento de canal corretivo | Possível encerramento da correção |

### Nível 3 — Evidências Estruturais

Uma Evidência Estrutural surge quando uma interpretação possui justificativa técnica suficiente para ser formalizada conforme o Canonical Evidence Model vigente.

As Evidências representam conhecimento explicitável e auditável, publicável no Blackboard e reutilizável pelos componentes do ecossistema.

### Nível 4 — Hipóteses Estruturais

Hipóteses representam explicações estruturais construídas a partir da consolidação de múltiplas Evidências.

A hipótese nunca é produzida diretamente das observações. Ela sempre emerge da consolidação de Evidências Estruturais.

---

## Taxonomia de Ambiguidades Estruturais

O Structural Agent deverá reconhecer explicitamente situações de ambiguidade estrutural, distinguindo-as de interpretações válidas com menor qualidade.

**Ambiguidade de Grau**
Dúvida sobre o grau Elliott correto para a estrutura identificada.

**Ambiguidade de Extensão**
Dúvida sobre qual onda está estendida dentro de um impulso.

**Ambiguidade Corretiva**
Existência de múltiplas estruturas corretivas plausíveis.

**Ambiguidade de Diagonal**
Incerteza entre diagonal e impulso convencional.

**Ambiguidade de Alternância**
Conflito entre cenários compatíveis com o princípio da alternância.

*A existência de ambiguidade estrutural reconhecida deverá ser declarada explicitamente nas Evidências e Hipóteses produzidas, contribuindo para a avaliação de qualidade e convicção pelos componentes especializados da arquitetura.*

---

## Protocolo de Refutação Estrutural

Toda hipótese estrutural deverá ser submetida a tentativa ativa de refutação antes da publicação.

O Structural Agent reconhece as seguintes categorias de invalidação:

**Refutação Tipo A — Violação de Regra Estrutural**
Violação de condição obrigatória do Regime A. Implica rejeição imediata da interpretação.

**Refutação Tipo B — Incompatibilidade de Fibonacci**
As relações geométricas da estrutura são incompatíveis com os padrões esperados para a interpretação proposta.

**Refutação Tipo C — Inconsistência Fractal**
Conflito irreconciliável entre a interpretação do grau atual e a estrutura do grau superior ou inferior.

**Refutação Tipo D — Invalidação por Preço**
O movimento de preço subsequente violou o nível crítico de invalidação da hipótese.

> **[Correção 2]** O Tipo E (surgimento de hipótese estrutural superior) foi movido para o SAS-001 Capítulo 5 — Produção de Hipóteses Estruturais, onde a comparação entre hipóteses concorrentes será formalmente especificada.

---

## Qualidade Estrutural

O Structural Agent poderá classificar internamente a robustez de uma interpretação estrutural conforme os seguintes níveis:

| Nível | Significado |
|---|---|
| Excelente | Regras e Diretrizes amplamente satisfeitas; estrutura excepcional |
| Forte | Estrutura consistente com poucas ambiguidades relevantes |
| Aceitável | Estrutura válida com ambiguidades relevantes |
| Fraca | Estrutura válida, porém pouco sustentada pelas Diretrizes |
| Especulativa | Estrutura possível, porém altamente incerta |

Os critérios de classificação consideram: conformidade com Regras Estruturais, conformidade com Diretrizes Estruturais, coerência fractal e suporte geométrico de Fibonacci.

> Esta classificação representa avaliação estrutural interna do Structural Agent. Não constitui Conviction Global nem substitui os componentes especializados da arquitetura responsáveis pela avaliação de convicção.

---

## Conhecimentos Explicitamente Excluídos

O Structural Agent não mantém conhecimento especializado sobre:

- ICT
- SMC (Smart Money Concepts)
- Liquidez
- BOS / CHOCH / MSS
- Fair Value Gaps / Order Blocks / Breakers
- Volume Profile / Footprint / Fluxo de Ordens
- Macroeconomia / Notícias / Sentimento
- Gestão de Risco / Execução de Ordens

Esses conhecimentos pertencem aos agentes especializados correspondentes.

---

## Atualização do Conhecimento

O conhecimento do Structural Agent poderá evoluir por meio do processo formal de governança definido pela arquitetura do SOT.

Nenhuma ampliação de domínio poderá ocorrer sem revisão e aprovação arquitetural conforme os processos definidos pelo GMC-001.

O agente não modifica autonomamente sua base de conhecimento.

---

## Relação com Evidências e Hipóteses

O conhecimento definido neste capítulo constitui a base conceitual utilizada pelo Structural Agent para:

- produzir Evidências Estruturais;
- construir Hipóteses Estruturais;
- justificar tecnicamente suas conclusões.

Este capítulo não define os contratos de Evidência nem os contratos de Hipótese, que permanecem sob responsabilidade dos Modelos Canônicos vigentes.

> **[Correção 1]** A Taxonomia de Evidências Estruturais (Elliott Evidence, Fibonacci Evidence, Fractal Evidence, Trend Evidence, Channel Evidence, Structural Pivot Evidence, Structural Invalidation Evidence) foi removida deste capítulo e transferida para o SAS-001 Capítulo 4 — Produção de Evidências Estruturais, onde constitui a abertura natural do capítulo de output, não de knowledge.

---

## Critérios de Aceitação

O capítulo será considerado atendido quando:

- os domínios de conhecimento estiverem claramente definidos;
- os regimes de validação (Regras vs Diretrizes) estiverem formalizados;
- os limites do conhecimento forem explícitos e não houver sobreposição com outros agentes;
- a hierarquia cognitiva 4 níveis estiver definida;
- as ambiguidades estruturais forem reconhecidas explicitamente;
- o protocolo de refutação (Tipos A-D) estiver formalizado;
- a qualidade estrutural estiver discriminada por níveis;
- o conhecimento suportar a produção de Evidências e Hipóteses Estruturais;
- a separação de responsabilidades da arquitetura permanecer preservada.

---

## Registro de Correções Incorporadas

| Obs. | Classificação | Correção Aplicada |
|---|---|---|
| 1 | Média | Taxonomia de Evidências removida — transferida para Cap.4 |
| 2 | Menor | Refutação Tipo E removida — transferida para Cap.5 |
| 3 | Média | Regimes de Validação A/B adicionados ao Domínio 1 |
| 4 | Menor | Limite Arquitetural adicionado ao Domínio 2 (Fibonacci) |

---

# SAS-001 — Structural Agent Specification
## Capítulos 2, 4, 5, 6 e 7 — Versão Pós-Correções
**Status:** CONGELADOS por consenso de Andraus
**Projeto:** ORYX AGENT

> **Nota:** Os Capítulos 1 e 3 possuem arquivos individuais:
> - Cap.1: `SAS-001_Cap1_Pos_Correcoes.md`
> - Cap.3: `SAS-001_Cap3_Pos_Correcoes.md`

---

# Capítulo 2 — Modelo Cognitivo do Structural Agent

## Objetivo do Capítulo
Definir o modelo cognitivo utilizado pelo Structural Agent para transformar observações estruturais do mercado em conhecimento reutilizável pelo ecossistema do SOT. Este capítulo estabelece: o papel cognitivo do agente; os objetos cognitivos consumidos; os objetos cognitivos produzidos; os limites de atuação cognitiva; o fluxo conceitual de raciocínio. Não define: algoritmos de implementação; regras específicas de Elliott ou Fibonacci; prompts; estratégias operacionais; critérios de decisão.

## Princípio Geral
O raciocínio do Structural Agent deverá seguir uma sequência determinística. Cada etapa depende da conclusão da etapa anterior. Não será permitido construir hipóteses sem evidências estruturais suficientes.

## 2.1 Papel Cognitivo
O Structural Agent é o especialista cognitivo responsável pela interpretação da estrutura do mercado. Sua função consiste em transformar observações estruturais em conhecimento estruturado, permitindo que os demais componentes do SOT utilizem esse conhecimento em processos posteriores de validação, confluência, convicção e decisão.

Seu papel cognitivo:
```
Observação Estrutural → Interpretação Estrutural → Evidência Estrutural → Hipótese Estrutural
```

O Structural Agent não executa validações globais nem produz decisões operacionais.

## 2.2 Natureza Cognitiva
O Structural Agent opera segundo um modelo cognitivo interpretativo. Sua atividade consiste em: observar; interpretar; produzir evidências; formular hipóteses; revisar hipóteses diante de novas observações. O agente não opera segundo modelos determinísticos. Nenhuma interpretação produzida é considerada definitiva. Toda hipótese permanece sujeita à revisão, substituição ou invalidação. O agente não produz: previsões determinísticas; sinais operacionais; recomendações de execução; decisões de trading.

## 2.3 Objetos Cognitivos Consumidos
O Structural Agent poderá consumir informações disponibilizadas pelos mecanismos oficiais do Kernel Cognitivo. Essas informações poderão incluir:

**Dados de Mercado:** OHLC; séries temporais de preços; timeframes disponíveis para análise.

**Objetos Cognitivos Compartilhados:** o agente poderá utilizar informações cognitivas compartilhadas por outros componentes autorizados do ecossistema. O consumo desses objetos deverá obedecer integralmente às regras estabelecidas pelos Modelos Canônicos vigentes. Esta especificação não redefine regras de consumo, interpretação, rastreabilidade ou ciclo de vida desses objetos.

## 2.4 Objetos Cognitivos Produzidos

**Evidências Estruturais:** representam observações estruturais interpretadas pelo agente. Todas deverão obedecer integralmente ao Canonical Evidence Model vigente.

Classificação arquitetural:
- Producer Type: AGENT
- Producer: Structural Agent
- Origin Type: PRIMARY
- Domain: STRUCTURAL

**Hipóteses Estruturais:** representam a interpretação estrutural consolidada produzida pelo agente a partir do conjunto de Evidências Estruturais disponíveis. As Hipóteses Estruturais deverão obedecer ao contrato de hipótese vigente definido pela arquitetura do SOT.

## 2.5 Processo Cognitivo Abstrato

```
Observação → Análise Estrutural → Produção de Evidências → Construção de Hipóteses → Publicação
```

Este fluxo representa apenas uma abstração arquitetural. A implementação interna utilizada pelo agente não é definida por este capítulo.

## 2.6 Limites Cognitivos
O Structural Agent possui responsabilidade exclusiva sobre interpretação estrutural. Consequentemente, não lhe compete: validar confluência entre domínios; calcular convicção global; produzir decisões; produzir missões operacionais; determinar entradas; determinar saídas; executar operações; produzir análises institucionais; produzir análises macroeconômicas; produzir análises de sentimento.

## 2.7 Relação com o Canonical Evidence Model
Toda Evidência Estrutural produzida pelo Structural Agent deverá obedecer integralmente ao Canonical Evidence Model vigente. O Structural Agent não possui autoridade para: redefinir o conceito de Evidência; redefinir campos do modelo; redefinir estados; redefinir regras de rastreabilidade; redefinir regras de ciclo de vida.

## 2.8 Relação entre Evidências e Hipóteses
O Structural Agent constrói Hipóteses Estruturais a partir das Evidências Estruturais produzidas durante o processo analítico. Esta direção — Evidência como fundamento da Hipótese — está alinhada aos contratos cognitivos vigentes da arquitetura do SOT.

## 2.9 Princípios Cognitivos

**Princípio 1 — Especialização Estrutural:** o Structural Agent interpreta exclusivamente aspectos estruturais do mercado.

**Princípio 2 — Explicabilidade:** toda hipótese deverá ser sustentada por Evidências Estruturais e justificativas técnicas rastreáveis.

**Princípio 3 — Refutabilidade:** toda hipótese deverá admitir invalidação diante de novas observações ou novas Evidências.

**Princípio 4 — Consistência Fractal:** a interpretação estrutural deverá considerar a relação entre diferentes graus estruturais do mercado.

**Princípio 5 — Independência Cognitiva:** a produção de Evidências e Hipóteses Estruturais pelo Structural Agent não depende de validação prévia por outros domínios cognitivos. A avaliação global da convicção e a integração com outros domínios pertencem aos componentes especializados da arquitetura.

**Princípio 6 — Subordinação aos Modelos Canônicos:** o Structural Agent deverá consumir e produzir objetos cognitivos respeitando integralmente os contratos definidos pelos Modelos Canônicos vigentes.

## Critério de Conformidade do Capítulo
O Modelo Cognitivo do Structural Agent será considerado conforme quando: produzir Evidências Estruturais compatíveis com o CEM; construir Hipóteses Estruturais a partir de Evidências; respeitar os limites cognitivos definidos pela arquitetura; não invadir responsabilidades de outros componentes; permanecer compatível com os Modelos Canônicos vigentes; preservar explicabilidade, rastreabilidade e refutabilidade.

---

# Capítulo 4 — Produção de Evidências Estruturais

## 5W2H (PPQ-001)
- **What:** Definir como o Structural Agent transforma conhecimento estrutural em Evidências compatíveis com o CEM-001.
- **Why:** Sem um processo formal de produção de Evidências, o conhecimento estrutural permanece como observação interna sem capacidade de ser compartilhado, auditado ou reutilizado.
- **Where:** Camada 4 — Agentes Especializados (SAS-001).
- **When:** Durante todo o ciclo analítico do agente. Depende de Cap.3 (Conhecimento) congelado.
- **Who:** Structural Agent.
- **How:** Aplicação dos 5 domínios do Cap.3 sobre observações de mercado, gerando Evidências conformes ao CEM-001 Baseline 1.0.
- **How much:** Impacta Cap.5 (Hipóteses consomem Evidências) e Cap.6 (publicação via Kernel). CEM-001 permanece inalterado — o Cap.4 apenas aplica seu contrato.

**GES Level:** Nível 2 — Framework Oficial | Time-box: 1 a 3 sessões.

## Objetivo
Definir o processo pelo qual o Structural Agent produz Evidências Estruturais compatíveis com os Modelos Canônicos vigentes da arquitetura.

## Princípio Fundamental
O Structural Agent não publica observações brutas. Toda Evidência Estrutural deve resultar de:
```
Observação → Interpretação → Validação Estrutural → Evidência
```

## Fontes das Evidências Estruturais
As Evidências produzidas podem ser fundamentadas pelos 5 domínios definidos no Cap.3: Elliott (impulsos, correções, diagonais, extensões, truncamentos); Fibonacci (retrações, projeções, expansões, extensões); Organização Fractal (alinhamento entre graus, continuidade estrutural); Tendência (direção predominante, aceleração, exaustão); Canais (impulsivos, corretivos, rompimentos).

## Taxonomia das Evidências Estruturais

**Elliott Evidence:** evidência baseada em estruturas Elliott identificadas.
**Fibonacci Evidence:** evidência baseada em proporcionalidades estruturais.
**Fractal Evidence:** evidência baseada em coerência entre graus.
**Trend Evidence:** evidência baseada em contexto direcional.
**Channel Evidence:** evidência baseada em canalização estrutural.
**Structural Pivot Evidence:** evidência baseada em pivôs estruturais relevantes.
**Structural Invalidation Evidence:** evidência relacionada a critérios objetivos de invalidação.

## Critérios de Produção

Uma Evidência Estrutural somente poderá ser publicada quando:

**Critério 1 — Fundamentação:** existir observação estrutural verificável.
**Critério 2 — Consistência:** não existir violação de Regras Estruturais (Regime A, conforme Cap.3).
**Critério 3 — Explicabilidade:** a interpretação puder ser justificada tecnicamente.
**Critério 4 — Rastreabilidade:** a Evidência puder ser rastreada até sua observação original.

## Compatibilidade com o CEM-001
Toda Evidência publicada pelo Structural Agent deverá obedecer ao Canonical Evidence Model vigente.

Campos obrigatórios conforme CEM-001:
- Producer Type = AGENT
- Domain = STRUCTURAL
- Origin = PRIMARY
- Demais campos definidos exclusivamente pelo CEM-001

O SAS-001 não redefine o contrato de Evidência.

## Evidence Strength e Qualidade Estrutural

O Structural Agent deverá traduzir sua avaliação de Qualidade Estrutural para o campo Evidence Strength do CEM-001 (Float 0.0→1.0). A Qualidade Estrutural é um conceito interno do agente. Evidence Strength é um campo obrigatório do CEM-001. A correspondência entre os níveis qualitativos e a escala numérica constitui convenção interna do agente, documentada nos mecanismos de implementação, e não altera o contrato do CEM-001.

## Grau de Determinismo (Classificação Interna)
O Structural Agent poderá classificar internamente cada Evidência Estrutural segundo seu grau de determinismo:
- **DETERMINISTIC:** derivada de violação de Regra Estrutural (Regime A)
- **PROBABILISTIC:** derivada de relações de Fibonacci
- **HEURISTIC:** derivada de Diretriz Estrutural (Regime B)
- **CONTEXTUAL:** derivada de contexto estrutural

Esta classificação é interna ao agente e influencia a atribuição do campo Evidence Strength e a contribuição da Evidência para a avaliação de convicção pelos componentes especializados da arquitetura. Não constitui campo do CEM-001 e não altera seu contrato.

## Princípios de Produção

**Não-Conclusão Prematura:** nenhuma Evidência Estrutural deverá incorporar conclusões que pertençam ao nível de Hipótese. Evidências representam fatos interpretados e verificáveis. A consolidação de múltiplas Evidências em uma narrativa estrutural pertence ao processo de construção de Hipóteses.

**Independência:** cada Evidência deverá preservar significado próprio mesmo quando analisada isoladamente. A validade de uma Evidência não dependerá da existência de outra Evidência específica.

**Evidências de Ausência:** a ausência de um elemento estrutural esperado pode constituir Evidência válida quando possuir significado analítico relevante.

**Reprodutibilidade:** outro agente especializado deverá ser capaz de reproduzir a mesma Evidência a partir das mesmas observações e do mesmo conjunto de regras.

**Evidências Concorrentes:** o Structural Agent poderá produzir Evidências que suportem interpretações concorrentes da estrutura. A existência de Evidências concorrentes não constitui inconsistência arquitetural. A resolução entre interpretações concorrentes pertence ao processo de construção de Hipóteses.

**Conflito de Evidências:** a existência simultânea de Evidências incompatíveis não invalida automaticamente nenhuma delas. Conflitos deverão ser preservados e encaminhados ao processo de construção de Hipóteses.

## Cadeia de Evidência
Toda Evidência deverá permitir rastreamento completo de: Observação Original → Interpretação → Regra/Diretriz Aplicada → Evidência Gerada.

## Contexto Temporal
Toda Evidência Estrutural é válida apenas dentro do contexto temporal em que foi produzida. Evidências podem tornar-se obsoletas sem que estejam incorretas.

## Publicação
Após validação: Structural Agent → Blackboard → Consumidores autorizados. A publicação seguirá os mecanismos definidos pelo Kernel Cognitivo.

## Limites Arquiteturais
O Structural Agent não: calcula Conviction; mede Confluência Global; prioriza Missões; executa Trades; substitui o papel de outros agentes. Sua responsabilidade encerra-se na produção de Evidências Estruturais.

## Critérios de Aceitação
O capítulo será considerado atendido quando: toda Evidência possuir fundamentação estrutural; toda Evidência for compatível com o CEM-001; a rastreabilidade for preservada; a separação de responsabilidades for mantida; não existir redefinição do Canonical Evidence Model.

---

# Capítulo 5 — Structural Hypothesis Generation

## 5W2H (PPQ-001)
- **What:** Definir como hipóteses estruturais são geradas.
- **Why:** Permitir raciocínio estrutural explicável.
- **Who:** Structural Agent.
- **When:** Durante o ciclo contínuo de análise estrutural, após produção de Evidências.
- **Where:** Domínio Structural Intelligence.
- **How:** Transformação de evidências em hipóteses concorrentes.
- **How much:** Consumo sujeito ao orçamento cognitivo vigente (CEE-001). CHM-001 (futuro) deverá acomodar os atributos especializados de Hipótese Estrutural definidos neste capítulo.

**GES Level:** Nível 2 — Framework Oficial | Time-box: 1 a 3 sessões.

## 5.1 Propósito
Este capítulo define como o Structural Agent transforma evidências estruturais em hipóteses formais sobre o estado do mercado. O objetivo é produzir representações explicáveis da realidade estrutural observada — não identificar sinais, não prever preços, não gerar entradas.

## 5.2 Problema Fundamental
Em qualquer instante podem coexistir múltiplas explicações plausíveis para a mesma estrutura observada. O papel do Structural Agent não é escolher arbitrariamente uma delas — é representar explicitamente esse espaço de possibilidades.

## 5.3 Definição Operacional
Para fins do SAS-001: *Uma Hipótese Estrutural é uma representação formal, explicável, rastreável e refutável do estado atual do mercado, construída a partir da convergência de evidências estruturais independentes e continuamente sujeita à revisão.*

Esta definição orienta a geração, manutenção e avaliação de Hipóteses Estruturais no contexto do Structural Agent. A definição universal de Hipótese Cognitiva será estabelecida pelo Canonical Hypothesis Model (CHM). O SAS-001 permanece compatível com esse modelo e não possui autoridade para redefini-lo.

## 5.4 Princípios Fundamentais

**5.4.1 Não-Certeza:** nenhuma hipótese representa verdade. Toda hipótese representa uma explicação candidata.

**5.4.2 Competição:** hipóteses competem. Hipóteses não se excluem automaticamente. O sistema deve preservar hipóteses concorrentes enquanto permanecerem plausíveis.

**5.4.3 Refutabilidade:** nenhuma hipótese pode existir sem mecanismo explícito de invalidação.

**5.4.4 Explicabilidade:** toda hipótese deve responder: Por que existe? Quais evidências a sustentam? Quais evidências a enfraquecem? O que pode destruí-la?

**5.4.5 Rastreabilidade:** toda hipótese deve possuir origem auditável. Deve ser possível reconstruir: Hipótese → Evidências → Observações → Dados.

## 5.5 Papel do Structural Agent
O Structural Agent é responsável por: criar hipóteses (transformar evidências em interpretações estruturais); atualizar hipóteses (incorporar novas evidências); fortalecer hipóteses (aumentar convicção quando suportadas); enfraquecer hipóteses (reduzir convicção quando surgem conflitos); refutar hipóteses (encerrar hipóteses incompatíveis com a realidade observada); arquivar hipóteses (preservar histórico cognitivo).

## 5.6 O Que o Agente Não Faz
O Structural Agent não: executa operações; define stop; define alvo; calcula risco financeiro; seleciona posição; decide entradas. Essas responsabilidades pertencem a outros agentes.

## 5.7 Condições Necessárias para Criação de Hipóteses
Uma hipótese somente poderá ser criada quando existirem simultaneamente: **Observação** (algo detectado); **Interpretação** (significado estrutural); **Fundamentação** (justificativa técnica); **Invalidação** (condição de destruição). Ausência de qualquer um desses elementos proíbe a criação da hipótese.

## 5.8 Estrutura Canônica da Hipótese Estrutural
Toda hipótese produzida pelo Structural Agent deverá obedecer ao contrato de hipótese vigente definido pela arquitetura do SOT. Os atributos universais de uma Hipótese Cognitiva serão definidos pelo CHM. O Structural Agent adiciona apenas atributos especializados do domínio estrutural:
- Narrativa Estrutural
- Narrativa Pai (contexto fractal do grau superior)
- Expectativa Estrutural (desdobramentos plausíveis)
- Contexto Fractal (referência ao grau superior)
- Relações Hierárquicas Estruturais

## 5.9 Multi-Hypothesis Framework
O ORYX adota formalmente um modelo multi-hipótese. O sistema nunca deverá assumir hipótese única quando alternativas compatíveis existirem. Estrutura esperada: Hipótese Principal + Hipótese Alternativa A + Hipótese Alternativa B + Hipótese Alternativa C.

## 5.10 Hierarquia Fractal
Hipóteses existem em uma árvore cognitiva. Cada nível herda contexto do superior.
```
D1 └── H4 └── H1 └── M15
```

## 5.11 Herança Estrutural
Nenhuma hipótese nasce sem ancestralidade. Toda hipótese deve registrar: Root Hypothesis; Parent Hypothesis; Generation Level. Isso permite rastrear evolução estrutural completa.

## 5.12 Competição entre Hipóteses
Hipóteses devem disputar recursos cognitivos. A competição ocorre por: qualidade das evidências; robustez estrutural; continuidade fractal; coerência narrativa; estabilidade temporal. A competição não elimina automaticamente hipóteses perdedoras.

## 5.13 Critérios de Eliminação
Uma hipótese somente poderá ser removida por: **Refutação** (violação estrutural explícita — Tipos A-D do Cap.3); **Obsolescência** (mercado evoluiu além do contexto); **Substituição** (hipótese superior absorveu sua explicação — Tipo E, detalhado neste capítulo).

**Substituição por Hipótese Superior (Tipo E):** quando uma hipótese concorrente demonstrar maior consistência estrutural, maior suporte de evidências e maior coerência fractal, a hipótese inferior poderá ser substituída mediante registro formal da hipótese sucessora e da justificativa de substituição.

## 5.14 Estágios Funcionais Estruturais
O Structural Agent reconhece operacionalmente situações como: **Hipótese Emergente**; **Hipótese Dominante**; **Hipótese Enfraquecida**; **Hipótese Refutada Estruturalmente**. Esses estágios descrevem comportamento interno. Não representam um ciclo de vida canônico — que será definido pelo CHM.

## 5.15 Resultado
O produto final deste capítulo é: conjunto de Hipóteses Estruturais compatíveis com os contratos canônicos vigentes. Consumidores autorizados: componentes autorizados responsáveis pela gestão de hipóteses; Conviction Engine; Mission Engine; componentes de Explainability autorizados. <!-- DIV-SAS-02 (2026-10-01): "Conviction Engine" = mecanismo legado (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (DHR-ARQ-001); "Mission Engine" = absorvido pelo Manager Agent — Fase 0 (ADR-MANAGER-001 / DHR-ARQ-002). Não são componentes independentes. Texto preservado (INV-07/CONST-01). -->

---

# Capítulo 6 — Integração com o Kernel Cognitivo

## 5W2H (PPQ-001)
- **What:** Definir a integração do Structural Agent com o Kernel Cognitivo.
- **Why:** Garantir interoperabilidade, governança, auditabilidade e desacoplamento.
- **Who:** Structural Agent e componentes autorizados do Kernel.
- **When:** Durante todo o ciclo operacional do agente.
- **Where:** Domínio Structural Intelligence e infraestrutura cognitiva do ORYX.
- **How:** Contratos canônicos, Scheduler, Event Bus, Blackboard, Registry de Capacidades e mecanismos oficiais do Kernel.
- **How much:** Impacta diretamente a interoperabilidade do agente com o ecossistema ORYX; serve como pré-requisito para os capítulos de Narrative Engine, State Engine, Forecast Engine e Refutation Engine.

**GES Level:** Nível 2 — Framework Oficial | Time-box: 1 a 3 sessões.

## 6.1 Propósito
Este capítulo define como o Structural Agent interage com a infraestrutura cognitiva do ORYX: recebe estímulos; processa informações; produz artefatos cognitivos; compartilha conhecimento; participa do ecossistema cognitivo. Não define algoritmos internos nem contratos canônicos.

## 6.2 Problema Fundamental
Um agente isolado possui inteligência local. O ORYX busca inteligência sistêmica. Para isso, o conhecimento produzido por um agente deve ser: compartilhável; rastreável; auditável; reutilizável; economicamente sustentável.

## 6.3 Princípios de Integração

**6.3.1 Autonomia Controlada:** o Structural Agent é autônomo para produzir Observações, Interpretações, Evidências e Hipóteses Estruturais. Não possui autoridade para: alterar contratos canônicos; alterar artefatos de terceiros; alterar governança global; modificar políticas do Kernel.

**6.3.2 Comunicação Indireta:** agentes não dependem diretamente de outros agentes. Modelo proibido: Structural Agent → Institutional Agent. Modelo permitido: Structural Agent → Kernel → Institutional Agent.

**6.3.3 Interoperabilidade Contratual:** os agentes interoperam através de contratos — nunca através de implementações.

**6.3.4 Neutralidade de Implementação:** nenhuma integração pode assumir linguagem, banco de dados, framework ou infraestrutura específica.

## 6.4 Registry de Contratos Cognitivos
Objetivo: permitir descoberta formal dos contratos reconhecidos pelo Kernel. Exemplos: CEM-001 (Canonical Evidence Model), CHM-001 (Canonical Hypothesis Model) e futuros Modelos Canônicos aprovados pela Governança Arquitetural. Responsabilidade: o Structural Agent deve consultar contratos oficiais — nunca inferir contratos nem criar versões paralelas.

## 6.5 Registry de Capacidades
Objetivo: permitir descoberta de competências cognitivas por capacidade, não por nome. Exemplos: STRUCTURAL_ANALYSIS; ELLIOTT_ANALYSIS; FRACTAL_ANALYSIS; STRUCTURAL_FORECASTING; STRUCTURAL_REFUTATION.

## 6.6 Integração com o Scheduler
Eventos que podem ativar o agente: Temporais (novo candle); Cognitivos (mudança narrativa); Dependência (nova evidência relevante); Governança (mudança de política). **Regra fundamental:** o Structural Agent não agenda sua própria execução. A responsabilidade pertence exclusivamente ao Scheduler (EC-COG-006).

## 6.7 Integração com o Cognitive Budget (CEE-001)
Objetivo: garantir sustentabilidade econômica. Antes da ativação o Scheduler poderá avaliar: custo esperado; valor esperado; urgência; prioridade. Exemplos: mercado estável → reduz frequência; mercado dinâmico → aumenta frequência. Princípio: recursos cognitivos são limitados; processamento deve gerar valor proporcional.

## 6.8 Priorização de Eventos
Todos os eventos deverão possuir prioridade. Categorias: CRITICAL; HIGH; NORMAL; LOW; BACKGROUND. Exemplos: violação Elliott → CRITICAL; atualização estatística → BACKGROUND.

## 6.9 Integração com Event Bus
Publicações permitidas: Evidência Criada; Evidência Invalidada; Hipótese Criada; Hipótese Refutada; Mudança Narrativa. Consumo permitido: Mudança de Regime; Atualização Contextual; Eventos de Governança; Atualização Institucional. Restrição: eventos transportam fatos — nunca decisões finais.

## 6.10 Metadados Operacionais de Infraestrutura
Os artefatos publicados pelo Structural Agent poderão carregar metadados operacionais conforme definido pelos contratos dos componentes do Kernel responsáveis pelo transporte, armazenamento e distribuição desses artefatos. O Structural Agent não possui autoridade para definir tais metadados. Sua responsabilidade limita-se a produzir artefatos compatíveis com os contratos vigentes dos componentes que os consomem. Exemplos de metadados operacionais, quando definidos pelos componentes apropriados: Freshness; Latency; Reliability; Expiration.

## 6.11 Integração com Blackboard
Publicação permitida: Evidências Estruturais; Hipóteses Estruturais; Narrativas Estruturais; Estados Estruturais. Consulta permitida: Contexto Global; Hipóteses Existentes; Narrativas Existentes; Estado Global. Restrições: o agente não pode sobrescrever conhecimento de terceiros; excluir artefatos globais; alterar governança.

## 6.12 Integração com Knowledge Graph
O Structural Agent atua exclusivamente como produtor. Pode registrar: relações fractais; relações temporais; relações estruturais; relações de causalidade estrutural. Não pode: redefinir ontologias; alterar taxonomias globais.

## 6.13 Integração com Conviction Engine  <!-- DIV-SAS-03 (2026-10-01): "Conviction Engine" = mecanismo legado (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (DHR-ARQ-001). Não é agente/componente separado. Título e texto preservados (INV-07/CONST-01). -->
Responsabilidade: fornecer insumos estruturais. Pode contribuir com: Qualidade Estrutural; Estabilidade Estrutural; Ambiguidade Estrutural; Continuidade Fractal; Robustez Narrativa. Não possui autoridade para calcular Conviction Global.

## 6.14 Resiliência e Tolerância a Falhas
Falha de Event Bus: agente continua produzindo conhecimento local. Falha de Blackboard: produção continua; publicação fica pendente. Falha de Consumidor: não impede produção estrutural. Falha de Contrato: produção deve ser bloqueada até resolução.

## 6.15 Observabilidade e Telemetria
Toda execução deverá registrar: Activation Reason; Processing Time; Evidence Count; Hypothesis Count; Refutations; Resource Usage; Forecasts (quando capacidade de previsão estrutural for formalmente especificada).

## 6.16 Governança e Auditoria
Toda saída deve ser: Rastreável; Reproduzível; Auditável; Explicável. Nenhum artefato pode existir sem: origem; justificativa; timestamp; versão.

## 6.17 Validação Econômica (CEE-001 §8)
Conforme CEE-001, toda expansão estrutural deve responder: o benefício cognitivo supera o custo de manutenção? Nenhuma expansão estrutural deve ser aprovada sem análise econômica. Esta validação se aplica quando o agente entrar em operação piloto real.

## 6.18 Maturidade de Integração
Níveis: 0 (sem integração); 1 (consulta Blackboard); 2 (produz Evidências); 3 (produz Hipóteses); 4 (contribui para Conviction); 5 (participa da Governança Cognitiva).

**Posicionamento Atual:** o Structural Agent especificado pelo SAS-001 opera atualmente nos níveis 1 a 4. O Nível 5 (Participação em Governança Cognitiva) não pertence ao escopo da presente especificação.

## 6.19 Fluxo Operacional Oficial
```
Scheduler → Validação Econômica → Structural Agent
→ Observações → Interpretações → Evidências → Hipóteses
→ Blackboard → Event Bus → Consumidores Autorizados
```

## 6.20 Limites de Responsabilidade
Responsável por: Estrutura; Fractalidade; Narrativas Estruturais; Hipóteses Estruturais; Estados Estruturais. Não responsável por: Execução; Portfólio; Gestão de Capital; Risco Financeiro; Missões; Conviction Global.

---

# Capítulo 7 — Structural Narrative Engine

## 5W2H (PPQ-001)
- **What:** Definir como o Structural Agent constrói Narrativas Estruturais.
- **Why:** Permitir representação coerente da evolução temporal das estruturas de mercado. Hipóteses isoladas descrevem possibilidades; Narrativas explicam evolução causal e temporal.
- **Who:** Structural Agent.
- **When:** Após a geração e avaliação de hipóteses estruturais (Cap.5).
- **Where:** Domínio Structural Intelligence.
- **How:** Organização de hipóteses, evidências e contexto estrutural em representações narrativas coerentes.
- **How much:** Impacta diretamente: Forecast Engine, Conviction Engine, Explainability Framework. <!-- DIV-SAS-04 (2026-10-01): "Conviction Engine" = mecanismo legado (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (DHR-ARQ-001). Texto preservado (INV-07/CONST-01). --> Impacta indiretamente: CNM-001 (futuro), que deverá acomodar os atributos especializados de Narrativa Estrutural definidos neste capítulo, de forma análoga à acomodação dos atributos estruturais de hipótese pelo futuro CHM. As Narrativas Estruturais produzidas por este capítulo constituem insumo do Structural State Engine (SSE-001).

**GES Level:** Nível 2 — Framework Oficial | Time-box: 1 a 3 sessões.

## 7.1 Propósito
Este capítulo define como o Structural Agent constrói, mantém e avalia Narrativas Estruturais. O objetivo é representar a evolução estrutural do mercado de forma coerente, temporal e auditável — não produzir previsões nem gerar explicações para usuários.

## 7.2 Problema Fundamental
Hipóteses isoladas possuem baixo poder explicativo. Uma Narrativa existe para preencher a lacuna: Como chegamos aqui? O que aconteceu antes? O que está acontecendo agora? O que tende a acontecer em seguida?

## 7.3 Definição Operacional
Para fins do SAS-001: *Uma Narrativa Estrutural é uma representação temporal e causal que organiza evidências, hipóteses e estados estruturais em uma explicação coerente da evolução observada do mercado.*

Esta definição orienta exclusivamente o comportamento do Structural Agent. A definição universal de Narrativa Cognitiva pertence ao futuro Canonical Narrative Model (CNM).

## 7.4 Princípios Fundamentais

**7.4.1 Continuidade Temporal:** toda narrativa deve conectar Passado → Presente → Futuro Plausível. Narrativas que descrevem apenas o estado atual são consideradas incompletas.

**7.4.2 Coerência Causal:** os eventos descritos devem possuir relações causais plausíveis.

**7.4.3 Compatibilidade Estrutural:** a narrativa não pode contradizer regras Elliott válidas, evidências aceitas ou hipóteses dominantes.

**7.4.4 Refutabilidade Narrativa:** toda narrativa deve possuir condições explícitas de degradação ou substituição. Narrativas não são permanentes.

**7.4.5 Multiplicidade:** o agente pode manter simultaneamente múltiplas narrativas plausíveis. Não existe obrigação de narrativa única.

## 7.5 O Que a Narrativa Não É
Narrativa não é: Evidência; Hipótese; Forecast; Conviction; Relatório humano. Narrativa é um artefato cognitivo distinto.

## 7.6 Insumos da Narrativa
A construção narrativa poderá utilizar: Evidências Estruturais (Cap.4); Hipóteses Estruturais (Cap.5); Contexto Fractal (múltiplos timeframes); Estado Estrutural Disponível (quando existente).

## 7.7 Gramática Narrativa Estrutural
Para reduzir subjetividade, as narrativas deverão seguir uma gramática mínima: Contexto (situação estrutural anterior) → Evento (mudança estrutural relevante) → Consequência (impacto estrutural observado) → Estado Atual (situação vigente) → Expectativa (desdobramento estrutural plausível) → Condições de Substituição (critérios que tornam outra narrativa mais adequada).

Esta gramática constitui um guia operacional interno utilizado pelo Structural Agent para construção de Narrativas Estruturais. A gramática universal aplicável às Narrativas Cognitivas do ecossistema ORYX será definida pelo Canonical Narrative Model (CNM), quando especificado. O SAS-001 não possui autoridade para definir ou restringir tal gramática universal. O Structural Agent deverá permanecer compatível com o CNM quando este for estabelecido.

## 7.8 Coerência Narrativa
Objetivo: avaliar consistência interna. Critérios possíveis: Consistência Temporal (a sequência faz sentido?); Consistência Fractal (há compatibilidade entre timeframes?); Consistência Estrutural (há compatibilidade com Elliott?); Consistência Causal (os eventos possuem encadeamento plausível?). A metodologia específica de cálculo permanece interna ao agente.

## 7.9 Estabilidade Narrativa
Narrativas excessivamente voláteis indicam baixa robustez cognitiva. Sinais de instabilidade: mudanças frequentes; substituições recorrentes; conflitos persistentes. Consequência: narrativas instáveis podem reduzir sua contribuição para processos posteriores.

## 7.10 Competição entre Narrativas
O Structural Agent poderá manter múltiplas narrativas concorrentes. A competição poderá considerar: qualidade das evidências; robustez das hipóteses; continuidade fractal; coerência estrutural.

O resultado da competição narrativa constitui uma ordenação estrutural interna produzida pelo Structural Agent. Essa ordenação representa apenas o grau relativo de sustentação estrutural das Narrativas Estruturais disponíveis com base nas evidências, hipóteses e contexto estrutural observados. A integração desse resultado com outros domínios cognitivos e qualquer cálculo de Conviction Global pertencem a componentes especializados da arquitetura.

## 7.11 Estágios Funcionais Narrativos
O Structural Agent reconhece operacionalmente situações como: **Narrativa Emergente**; **Narrativa Dominante**; **Narrativa Contestada**; **Narrativa Enfraquecida**. Esses estágios descrevem comportamento interno. Não representam um ciclo de vida canônico.

## 7.12 Substituição Narrativa
Uma narrativa poderá ser substituída quando: surgirem evidências incompatíveis; hipóteses concorrentes tornarem-se superiores; o contexto estrutural evoluir; ocorrer refutação estrutural relevante.

## 7.13 Herança Fractal Narrativa
Narrativas devem respeitar a organização fractal do mercado. Narrativas inferiores devem considerar o contexto narrativo superior.
```
D1 └── H4 └── H1 └── M15
```

## 7.14 Integração com o Kernel
Conforme Cap.6. O Structural Agent poderá: publicar Narrativas Estruturais; consumir Evidências, Hipóteses e Contexto Global. A forma de transporte e armazenamento será definida pelos componentes do Kernel.

## 7.15 Limites de Responsabilidade
O Structural Agent é responsável por: Construção Narrativa Estrutural; Competição Narrativa; Avaliação de Coerência; Avaliação de Estabilidade. Não é responsável por: Narrativa Institucional; Narrativa Fundamentalista; Narrativa Macroeconômica; Narrativa Global Integrada.

## 7.16 Resultado
O resultado deste capítulo é: conjunto de Narrativas Estruturais compatíveis com os contratos canônicos vigentes. As Narrativas Estruturais produzidas constituem insumo primário do Structural State Engine (SSE-001), que consolida Narrativas e Hipóteses Estruturais para consumo pelo Conviction Engine, Mission Engine, Explainability e Learning. <!-- DIV-SAS-05 (2026-10-01): "Conviction Engine" = mecanismo legado invocado pelo Manager Agent — Fase 2 (DHR-ARQ-001); "Mission Engine" = absorvido pelo Manager Agent — Fase 0 (ADR-MANAGER-001 / DHR-ARQ-002). Texto preservado (INV-07/CONST-01). -->

---

## Registro de Congelamento

| Campo | Valor |
|---|---|
| Documento | SAS-001 — Structural Agent Specification |
| Capítulos congelados | 1, 2, 3, 4, 5, 6, 7 |
| Cap.8 | Cancelado — escopo migrado para SSE-001 (ADR-SAS-001-001 ACCEPTED) |
| Status | CONGELADO por consenso de Andraus |
| ADR vigente | ADR-SAS-001-001: SSE é componente arquitetural compartilhado |
