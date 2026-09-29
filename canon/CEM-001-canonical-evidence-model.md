# CEM-001 — Canonical Evidence Model Specification
## Versão Consolidada Pós-Auditoria
**Status:** BASELINED — divergências DIV-CEM-2..6 corrigidas inline (2026-09-26, DHR-TAX-001). Texto histórico preservado (INV-07).
**Versão:** v1.1 (2026-09-29) — evolução **Categoria B** (GMC-001 Cap.3/5): campo opcional `Producer Historical Reliability` acrescentado à Camada 2. Aditiva/compatível — nenhum campo, estado ou transição existente foi alterado (INV-07/CONST-01). Ver `governance/GMC-CEM001-EXT-001_Proposta_Extensao_Confiabilidade_Produtor_CEM-001.md` e `governance/DHR-SPEC002-002_Ata_Homologacao_Plan_SPEC-002.md`.
**Projeto:** SOT SISTEMA TRADING  <!-- DIV-CEM-6 corrigida: "ORYX AGENT" era nome histórico; nome canônico = SOT SISTEMA TRADING (GLOSSÁRIO) -->  
**Categoria:** Modelo Canônico  
**Governança:** GMC-001

---

## Capítulo 1 — Identidade do Modelo

### Documento
CEM-001 — Canonical Evidence Model Specification

### Categoria
Modelo Canônico do Kernel Cognitivo

### Código
CEM-001

### Nome Oficial
Canonical Evidence Model

### Missão
Definir o padrão universal para representação, armazenamento, compartilhamento e utilização de evidências cognitivas produzidas pelos agentes especializados do SOT.

O Canonical Evidence Model estabelece uma linguagem comum para que todos os componentes do sistema possam interpretar evidências de forma consistente, independente do agente que as produziu.

### Objetivo Estratégico
Padronizar a representação das evidências cognitivas utilizadas pelo SOT, garantindo:

- interoperabilidade entre agentes;
- rastreabilidade completa;
- consistência arquitetural;
- auditabilidade;
- reutilização do conhecimento;
- independência entre domínios especializados.

### Escopo
O CEM aplica-se a toda evidência publicada no ecossistema do SOT.

Inclui evidências produzidas por:

- Structural Agent;
- Institutional Agent;
- futuros agentes especializados;
- motores cognitivos autorizados;
- componentes do Kernel autorizados.

### Fora do Escopo
O CEM não define:

- hipóteses;
- decisões;
- convicção;
- missões;
- execução operacional;
- estratégias de trading;
- regras específicas de Elliott;
- regras específicas de ICT;
- regras específicas de qualquer domínio especializado.

Esses conceitos pertencem aos seus respectivos modelos canônicos ou às especificações dos agentes.

### Definição Canônica de Evidência
Uma Evidência Cognitiva é uma observação objetiva produzida por um agente especializado, fundamentada em conhecimento técnico do seu domínio, capaz de sustentar, fortalecer, enfraquecer ou refutar hipóteses cognitivas.

Uma evidência não representa uma conclusão.

Ela representa um fato interpretado segundo um conhecimento especializado e preparado para ser utilizado por outros componentes do sistema.

### Princípios Fundamentais

**Princípio 1 — Neutralidade**
O modelo deverá ser independente de qualquer disciplina específica. Uma evidência estrutural, institucional ou macroeconômica deverá utilizar exatamente o mesmo padrão de representação.

**Princípio 2 — Objetividade**
Toda evidência deverá representar um fato observável segundo o domínio do agente produtor. Opiniões ou previsões não constituem evidências.

**Princípio 3 — Explicabilidade**
Toda evidência deverá possuir justificativa técnica suficiente para permitir auditoria humana e computacional.

**Princípio 4 — Rastreabilidade**
Toda evidência deverá permitir identificar: agente produtor, origem, contexto, momento da geração e conhecimento utilizado.

**Princípio 5 — Independência**
Cada evidência deverá existir independentemente das hipóteses construídas a partir dela. Uma mesma evidência poderá sustentar múltiplas hipóteses.

**Princípio 6 — Reutilização**
Evidências poderão ser reutilizadas por múltiplos agentes sem necessidade de reconstrução.

**Princípio 7 — Refutabilidade**
Toda evidência poderá ser posteriormente fortalecida, enfraquecida ou invalidada conforme novas observações. O modelo deverá permitir essa evolução sem perda do histórico.

**Princípio 8 — Interoperabilidade**
Todos os componentes do SOT deverão interpretar evidências utilizando exatamente a mesma linguagem conceitual.

### Papel do CEM na Arquitetura
O Canonical Evidence Model ocupa posição central no Kernel Cognitivo.

Ele atua como contrato universal entre: agentes produtores, Blackboard, Knowledge Graph, ~~Fractal Confluence Engine~~ <!-- DIV-CEM-2 (2026-09-26): FCE extinto — ADR-CONFLUENCE-001 v3; substituído por `confluence-elliott` (skill do Structural Agent) -->, ~~Conviction Engine~~ <!-- DIV-CEM-4: absorvido pelo Manager Agent Fase 2 -->, ~~Decision Orchestrator~~ <!-- DIV-CEM-3: eliminado — ADR-MANAGER-001 (2026-09-26); absorvido pelo Manager Agent -->, Manager Agent e demais componentes do ecossistema.

Nenhum agente deverá consumir evidências fora do padrão estabelecido pelo CEM.

### Relação com Outros Modelos Canônicos
O CEM fornece a base para:

- Canonical Hypothesis Model (CHM);
- Canonical Conviction Model (CCM);
- Canonical Decision Model (CDM);
- Canonical Narrative Model (CNM).

Esses modelos especializam e utilizam as evidências produzidas conforme este padrão.

### Critérios de Aceitação
O Canonical Evidence Model será considerado conforme quando:

- qualquer agente especializado puder produzir evidências utilizando este padrão;
- qualquer componente do Kernel puder consumir evidências sem adaptações específicas por domínio;
- a origem e o significado de cada evidência puderem ser compreendidos independentemente do agente produtor;
- a evolução futura do sistema puder ocorrer sem necessidade de redefinir o conceito de evidência.

---

## Capítulo 2 — Responsabilidade Arquitetural

### Objetivo do Capítulo
Definir o papel arquitetural do Canonical Evidence Model dentro do ecossistema do SOT, estabelecendo claramente: o que o modelo representa, quais responsabilidades lhe pertencem, quais responsabilidades não lhe pertencem, quais componentes produzem Evidências, quais componentes consomem Evidências e como o CEM se relaciona com os demais elementos da arquitetura.

### Papel Arquitetural
O Canonical Evidence Model constitui o contrato universal para representação de conhecimento especializado produzido pelos agentes do SOT.

Seu propósito é permitir que diferentes componentes do ecossistema possam produzir, compartilhar, armazenar, relacionar e consumir Evidências Cognitivas utilizando uma linguagem comum e independente de domínio.

O CEM atua como mecanismo de interoperabilidade cognitiva entre os diversos componentes da arquitetura.

### Responsabilidade Principal
A responsabilidade fundamental do CEM é definir:

> Como uma Evidência Cognitiva deve ser representada para que qualquer componente autorizado do SOT possa compreendê-la sem depender do agente que a produziu.

### O Que o CEM Representa
O CEM representa conhecimento especializado. Mais especificamente:

> Uma observação interpretada por um agente especializado, fundamentada em conhecimento técnico do seu domínio e preparada para utilização por outros componentes cognitivos.

O CEM não representa: dados brutos, medições isoladas, sinais, indicadores ou eventos de mercado sem interpretação.

Esses elementos pertencem às camadas inferiores de observação e análise.

### O Que o CEM Não Representa

- **Hipóteses** — pertencem ao CHM.
- **Convicções** — pertencem ao CCM.
- **Decisões** — pertencem ao CDM.
- **Narrativas** — pertencem ao CNM.
- **Estratégias** — pertencem às especificações dos agentes.
- **Conhecimento de Domínio** — pertence aos agentes e às suas Skills. O CEM apenas representa o resultado desse conhecimento.

### Produtores de Evidências
Somente componentes autorizados poderão produzir Evidências Cognitivas.

**Agentes Especializados (produtores primários):**
- Structural Agent
- Institutional Agent
- Operational Agent  <!-- DIV-CEM-5 (2026-09-26): adicionado — agente analítico confirmado por ADR-MANAGER-001; escopo M5 single-TF -->
- Macro Agent
- Sentiment Agent
- Risk Agent
- Context Agent

**Motores Cognitivos Autorizados:**
- Fusion Engine *(único motor cognitivo atualmente confirmado como produtor autorizado)*

Novos motores cognitivos somente poderão ser autorizados como produtores mediante processo formal de governança definido pelo GMC-001.

### Consumidores de Evidências
As Evidências produzidas conforme o CEM poderão ser consumidas por:

- **Blackboard** — compartilhamento cognitivo.
- **Knowledge Graph** — relacionamento semântico.
- **Hypothesis Engine** — construção de hipóteses.
- **Manager Agent (Fase 2: Conviction)** — avaliação de força cognitiva. <!-- DIV-CEM-4 (2026-09-26): "Conviction Engine" eliminado; absorvido pelo Manager Agent Fase 2 — ADR-MANAGER-001 -->
- **Manager Agent** — tomada de decisão. <!-- DIV-CEM-3 (2026-09-26): "Decision Orchestrator" eliminado; absorvido pelo Manager Agent — ADR-MANAGER-001 -->
- **Componentes de Explicabilidade autorizados** — construção de justificativas.
- **Outros agentes autorizados** — reutilização de conhecimento.

### Independência Cognitiva
Uma Evidência deverá existir independentemente de: hipóteses, convicções, decisões e missões.

Uma Evidência não depende de nenhum desses objetos para existir. Entretanto, todos eles poderão depender da Evidência.

### Reutilização Cognitiva
Uma mesma Evidência poderá ser utilizada simultaneamente por múltiplas hipóteses, convicções, decisões e agentes, sem necessidade de duplicação.

### Neutralidade de Domínio
O CEM deverá permanecer completamente neutro em relação ao domínio do conhecimento produzido. O modelo não poderá conter conceitos específicos de Elliott, ICT, SMC, Macroeconomia, Sentimento, Gestão de Risco ou qualquer outro domínio especializado.

Todo conhecimento específico permanece encapsulado nos agentes produtores.

### Relação com o Kernel Cognitivo
O Kernel Cognitivo utiliza Evidências definidas pelo CEM. O Kernel não redefine: estrutura, significado, ciclo de vida ou representação da Evidência. Essas responsabilidades pertencem exclusivamente ao CEM.

### Relação com a Governança
O CEM é governado pelo GMC-001 — Governança dos Modelos Canônicos. Toda alteração estrutural no modelo deverá obedecer às regras estabelecidas por esse documento.

### Relação com Futuros Modelos Canônicos
O CEM constitui a base cognitiva para: CHM, CCM, CDM e CNM. Esses modelos utilizam Evidências definidas pelo CEM, mas não alteram sua estrutura.

### Critério Arquitetural de Conformidade
O CEM será considerado arquiteturalmente conforme quando:

- qualquer agente puder produzir Evidências utilizando o modelo;
- qualquer componente puder consumir Evidências sem adaptações específicas;
- Evidências puderem ser compartilhadas entre domínios distintos;
- a interpretação de uma Evidência não depender do agente produtor;
- a evolução dos agentes não exigir alterações no conceito de Evidência.

---

## Capítulo 3 — Contrato Canônico da Evidência

### Objetivo do Capítulo
Definir a estrutura universal que toda Evidência Cognitiva deverá possuir para circular no ecossistema do SOT.

Este contrato é obrigatório para todos os produtores e consumidores autorizados. Nenhum agente, motor ou componente poderá publicar Evidências fora deste padrão.

### Definição Arquitetural
Uma Evidência Cognitiva é composta por quatro camadas conceituais:

```
IDENTIDADE
    ↓
ORIGEM
    ↓
CONTEÚDO COGNITIVO
    ↓
RASTREABILIDADE
```

Cada camada possui responsabilidades próprias.

---

### Camada 1 — Identidade
Responsável por identificar unicamente a Evidência.

**Evidence ID**
Identificador único e imutável. Permite referência universal.

**Evidence Version**
Versão da Evidência. Permite evolução sem perda de histórico.

**Creation Timestamp**
Momento da criação da Evidência.

**Status**
Estado atual da Evidência. Valores válidos:
- ACTIVE
- SUPERSEDED
- INVALIDATED
- ARCHIVED

> **Regra:** Status é o único campo mutável após publicação. Todo campo restante é imutável após a publicação da Evidência.

---

### Camada 2 — Origem
Responsável por identificar quem produziu a Evidência.

**Producer Type**
Categoria do produtor. Valores válidos:
- `AGENT`
- `ENGINE`

**Producer ID**
Identificação do produtor.
Exemplos: Structural Agent, Institutional Agent, Fusion Engine.

**Evidence Origin Type**
Natureza da origem cognitiva. Valores válidos:
- `PRIMARY` — produzida diretamente a partir de observações do mercado. Permitido apenas para `AGENT`.
- `DERIVED` — produzida a partir de outras Evidências. Permitido apenas para `ENGINE`.

**Producer Historical Reliability** *(campo opcional — v1.1, Categoria B, GMC-CEM001-EXT-001)*
Confiabilidade histórica (track-record) do produtor — eixo **independente** da força do relato específico (`Evidence Strength`, Camada 3): reliability da fonte ≠ credibility do relato (doutrina Admiralty/NATO AJP-2.1, adotada como princípio, não como códigos literais).
- **Opcional/nullable.** Ausência = `INDETERMINADO` (produtor sem histórico registrado) — nunca um default arbitrário.
- **Domínio:** Governed Enumeration (tiers ordinais de confiabilidade), valores governados por GMC-001.
- **Mutabilidade:** segue a regra geral da Camada 1/Cap.4 — imutável após publicação da Evidência; atualização de track-record só em nova Evidência/versão, nunca por mutação retroativa.
- **Trava constitucional (INV-04):** este campo é metadado descritivo/filtro — **NUNCA** entra como dimensão, insumo ou peso do Conviction Vector. Enforcement na camada consumidora (SPEC-002, BASpec-EPH-004, efeito E3).

---

### Camada 3 — Conteúdo Cognitivo
Representa o conhecimento especializado. Esta é a essência da Evidência.

**Domain**
Domínio cognitivo do produtor.

> **Governed Enumeration:** Domain é uma enumeração governada pelo GMC-001. Novos valores podem ser adicionados mediante aprovação formal sem necessidade de alteração estrutural do contrato.

Valores atuais aprovados:
- STRUCTURAL
- INSTITUTIONAL
- MACRO
- SENTIMENT
- RISK
- CONTEXT

**Observation**
Descrição objetiva da observação realizada. Representa: *o que foi observado.*
Exemplo: "Preço reagiu em Fibo 61.8%"

**Interpretation**
Interpretação especializada produzida pelo agente. Representa: *o que a observação significa.*
Exemplo: "Correção provavelmente concluída."

**Technical Rationale**
Justificativa técnica. Representa: *por que essa interpretação foi produzida.*
Exemplo: "Confluência entre Fibo, AO e estrutura impulsiva."

**Evidence Strength**
Força intrínseca da Evidência.

> **Tipo:** Float no intervalo `0.0 → 1.0`
> - `0.0` = sem relevância cognitiva atribuída pelo produtor
> - `1.0` = força máxima atribuída pelo produtor

> **Importante:** Evidence Strength representa o peso cognitivo da interpretação local. Não representa Convicção. Convicção pertence ao CCM e é calculada globalmente.

**Timeframe Reference**
Horizonte temporal utilizado pelo produtor na observação.

Valores válidos (enumeração estática):
- M5, M15, H1, H4, D1, W1, MN

**Market Context**
Regime ou condição de mercado vigente no momento da observação.

> **Governed Enumeration:** Market Context é uma enumeração governada pelo GMC-001. Novos valores podem ser adicionados mediante aprovação formal.

Valores atuais aprovados:
- BULL_MARKET
- BEAR_MARKET
- RANGE
- RISK_ON
- RISK_OFF

---

### Camada 4 — Rastreabilidade
Permite reconstruir a origem completa da Evidência.

**Source Reference**
Origem informacional utilizada.
Exemplos: Market Data, Economic Calendar, On-Chain Data.

**Lineage**
Lista de Evidências ancestrais diretas.

- Para `PRIMARY`: obrigatoriamente vazia `[]`
- Para `DERIVED`: obrigatória, contendo as referências das Evidências que originaram esta

Exemplo para `DERIVED`:
```
Lineage: [Evidence-A, Evidence-B]
```

> **Nota arquitetural:** A reconstrução expandida da cadeia cognitiva completa (além dos ancestrais diretos) é uma capacidade do Knowledge Graph, denominada *Cognitive Trace Reconstruction*, e não constitui campo armazenado na Evidência.

> **Nota arquitetural:** A profundidade cognitiva (*Cognitive Depth*) — número de níveis entre a Evidência e suas origens primárias — é uma métrica derivada calculada a partir da Lineage pelo Knowledge Graph ou pelo Fusion Engine quando necessário. Não constitui campo armazenado na Evidência.

---

### Invariantes do Modelo
Toda Evidência deverá possuir:

- identidade única;
- produtor identificável;
- observação;
- interpretação;
- justificativa técnica;
- rastreabilidade completa.

Caso qualquer desses elementos esteja ausente, a Evidência não estará em conformidade com o CEM.

### Restrições Arquiteturais
Uma Evidência não poderá conter: ordens, decisões, convicções, missões ou execução operacional.

Esses elementos pertencem a outros modelos canônicos.

### Compatibilidade Universal
Qualquer componente autorizado deverá conseguir compreender uma Evidência sem conhecer o agente produtor. Essa é a principal razão de existência do CEM.

---

## Capítulo 4 — Ciclo de Vida da Evidência

### Objetivo do Capítulo
Definir os estados, transições e regras que governam a existência de uma Evidência Cognitiva dentro do ecossistema do SOT.

O ciclo de vida garante: rastreabilidade, auditabilidade, consistência histórica, preservação do conhecimento e evolução controlada.

### Princípio Fundamental
Uma Evidência é um registro histórico de conhecimento produzido em determinado contexto.

> Evidências não devem ser modificadas retroativamente. Quando necessário, deverão ser substituídas ou invalidadas.

### Imutabilidade Pós-Publicação
Após publicação, os seguintes campos tornam-se imutáveis e não poderão ser alterados por nenhum componente do sistema:

**Camada de Identidade:**
- Evidence ID
- Evidence Version
- Creation Timestamp

**Camada de Origem:**
- Producer Type
- Producer ID
- Evidence Origin Type

**Camada de Conteúdo Cognitivo:**
- Domain
- Observation
- Interpretation
- Technical Rationale
- Evidence Strength
- Timeframe Reference
- Market Context

**Camada de Rastreabilidade:**
- Source Reference
- Lineage

> **Regra:** Status é o único campo mutável após publicação. Toda alteração de Status deverá respeitar as transições permitidas e registrar: timestamp, origem e justificativa.

### Evolução de Conhecimento
Caso qualquer elemento cognitivo precise ser atualizado, não se modifica a Evidência existente. Cria-se uma nova Evidência, e a anterior transita para o estado SUPERSEDED.

Exemplo:
```
Evidence-A
    ↓
Nova interpretação necessária
    ↓
Evidence-B (nova)
    ↓
Evidence-A → SUPERSEDED
```

### Estados Canônicos

**ACTIVE**
Estado padrão. A Evidência é considerada válida e disponível para consumo. Pode ser utilizada por hipóteses, convicções e motores cognitivos. Permanece elegível para fusão.

**SUPERSEDED**
A Evidência foi substituída por uma versão mais recente. Permanece armazenada e auditável. Não deve ser utilizada em novas inferências. Referencia a Evidência sucessora.

**INVALIDATED**
A Evidência foi considerada incorreta ou deixou de representar adequadamente a realidade observada. Preserva histórico de erro cognitivo. Permanece armazenada e auditável. Não pode sustentar novas hipóteses ou convicções.

**ARCHIVED**
A Evidência foi removida da camada operacional ativa. Disponível apenas para consulta histórica. Não participa de inferência ou fusão. Preserva rastreabilidade.

### Transições Permitidas

| De | Para |
|---|---|
| ACTIVE | SUPERSEDED |
| ACTIVE | INVALIDATED |
| ACTIVE | ARCHIVED |
| SUPERSEDED | ARCHIVED |
| INVALIDATED | ARCHIVED |

### Transições Proibidas
As seguintes transições são expressamente proibidas, para preservação da integridade histórica:

| De | Para |
|---|---|
| INVALIDATED | ACTIVE |
| ARCHIVED | ACTIVE |
| SUPERSEDED | ACTIVE |

### Relação com Lineage
Toda substituição deverá preservar rastreabilidade. A cadeia histórica deverá permanecer íntegra.

Exemplo:
```
Evidence-A → SUPERSEDED
Evidence-B → SUPERSEDED
Evidence-C → ACTIVE (versão atual)

Cadeia: A → B → C (íntegra e auditável)
```

### Consumo pelos Componentes

| Componente | Estados permitidos |
|---|---|
| Blackboard | Todos os estados (armazenamento) |
| Knowledge Graph | Todos os estados (preservação permanente) |
| Fusion Engine | Apenas ACTIVE |
| Manager Agent (Fase 2: Conviction) | Apenas ACTIVE | <!-- DIV-CEM-4: era "Conviction Engine" -->
| Manager Agent | Apenas ACTIVE | <!-- DIV-CEM-3: era "Decision Orchestrator" -->

### Auditabilidade
Toda mudança de estado deverá registrar: timestamp, origem da mudança e justificativa da mudança.

### Avaliação de Impacto em Evidências Derivadas
Quando uma Evidência utilizada na Lineage de uma Evidência Derivada for invalidada, o Fusion Engine deverá iniciar uma avaliação de impacto sobre os objetos derivados relacionados.

A invalidação da Evidência ancestral não implica invalidação automática das Evidências derivadas. A decisão sobre manutenção, substituição ou invalidação deverá ser tomada conforme as regras de rastreabilidade e linhagem definidas pelo CEM.

A invalidação gera um evento cognitivo (*Evidence Invalidated*) propagado através da infraestrutura de eventos cognitivos do Kernel. A avaliação de impacto sobre outros objetos cognitivos — hipóteses, convicções e decisões — é responsabilidade dos respectivos modelos canônicos (CHM, CCM, CDM).

---

## Capítulo 5 — Rastreabilidade e Linhagem Cognitiva

### Objetivo do Capítulo
Definir os mecanismos que permitem reconstruir integralmente a origem, evolução e relacionamento de uma Evidência Cognitiva dentro do ecossistema do SOT.

O objetivo é garantir: auditabilidade completa, explicabilidade, reconstrução histórica, análise de impacto e interoperabilidade cognitiva.

### Princípio Fundamental
Todo conhecimento produzido pelo SOT deverá ser rastreável até sua origem.

Nenhuma Evidência poderá existir sem que seja possível responder:

- quem a produziu;
- quando foi produzida;
- por que foi produzida;
- de onde surgiu;
- quais conhecimentos anteriores contribuíram para sua existência.

### Conceito de Linhagem Cognitiva
A Linhagem Cognitiva representa a cadeia de ancestralidade direta de uma Evidência. Ela descreve quais Evidências imediatamente antecedentes contribuíram para sua geração, permitindo que qualquer componente autorizado reconstrua o caminho do raciocínio.

### Tipos de Linhagem

**Linhagem Primária**
Aplicável a Evidências `PRIMARY`.

Regra: Evidências Primárias não possuem ancestrais cognitivos, pois sua origem é diretamente o processo analítico do agente.

Representação: `Lineage = []`

**Linhagem Derivada**
Aplicável a Evidências `DERIVED`.

Regra: Toda Evidência Derivada deverá declarar explicitamente suas Evidências ancestrais diretas.

Exemplo:
```
Evidence-A + Evidence-B
        ↓
    Fusion Engine
        ↓
    Evidence-C

Lineage de Evidence-C: [Evidence-A, Evidence-B]
```

### Integridade da Linhagem
A linhagem deverá preservar: completude, consistência e unicidade das referências.

Não é permitido remover ancestrais após publicação. Não é permitido adicionar ancestrais após publicação. A linhagem compõe o registro histórico imutável da Evidência.

### Cognitive Trace Reconstruction
A reconstrução da cadeia cognitiva completa — incluindo todos os ancestrais diretos e indiretos de uma Evidência — é uma capacidade do **Knowledge Graph**, denominada *Cognitive Trace Reconstruction*.

Esta capacidade não constitui campo armazenado na Evidência. O Knowledge Graph reconstrói a cadeia completa navegando as relações de Lineage armazenadas em cada Evidência.

Exemplo de reconstrução para Evidence-D:
```
Evidence-A (PRIMARY)
Evidence-B (PRIMARY)
        ↓
Evidence-C (DERIVED — Lineage: [A, B])
        ↓
Evidence-D (DERIVED — Lineage: [C])

Cognitive Trace Reconstruction de Evidence-D
= [Evidence-A, Evidence-B, Evidence-C]
```

### Cognitive Depth
A profundidade cognitiva (*Cognitive Depth*) representa o número de níveis de derivação existentes entre a Evidência e suas origens primárias.

> **Cognitive Depth não é um campo armazenado na Evidência.** É uma métrica derivada, calculada pelo Knowledge Graph ou pelo Fusion Engine quando necessário, a partir das relações de Lineage.

Exemplo:
```
Primary-A       → Cognitive Depth: 0
Derived-B (de A)→ Cognitive Depth: 1
Derived-C (de B)→ Cognitive Depth: 2
```

O Cognitive Depth permite que Conviction Engine, Fusion Engine e Knowledge Graph avaliem distância cognitiva em relação à observação original.

### Rastreabilidade de Versões
Quando ocorrer substituição (SUPERSEDED), a relação entre versões deverá permanecer explícita e a cadeia histórica deverá permanecer acessível para reconstrução.

### Impacto de Invalidação
Quando uma Evidência for invalidada (*Evidence Invalidated*), o sistema deverá ser capaz de identificar as Evidências Derivadas afetadas e suas dependências cognitivas baseadas em Evidências.

A invalidação gera um evento cognitivo (*Evidence Invalidated*) que será propagado através da infraestrutura de eventos cognitivos do Kernel para que os componentes consumidores possam reagir conforme suas responsabilidades.

> **Importante:** A invalidação não implica remoção. A invalidação não implica cascata automática.

O Fusion Engine é responsável por iniciar a avaliação de impacto sobre Evidências Derivadas relacionadas.

A avaliação de impacto sobre outros objetos cognitivos — hipóteses, convicções e decisões — não pertence ao CEM. Essa responsabilidade pertence aos respectivos modelos canônicos (CHM, CCM, CDM).

### Responsabilidades do Knowledge Graph
O Knowledge Graph deverá:

- preservar toda a linhagem;
- preservar todas as versões;
- preservar todos os estados;
- fornecer *Cognitive Trace Reconstruction* completa a partir das relações de Lineage;
- permitir navegação completa da cadeia cognitiva.

### Responsabilidades do Blackboard
O Blackboard poderá utilizar apenas Evidências em estado `ACTIVE` como conhecimento operacional.

### Reconstrução Cognitiva
O sistema deverá ser capaz de responder:

- Qual evidência originou esta decisão?
- Quais evidências contribuíram para esta hipótese?
- Qual foi a cadeia completa de raciocínio?
- Qual evidência foi invalidada?
- Quais objetos dependiam dela?

### Critério de Conformidade
O mecanismo de rastreabilidade será considerado conforme quando:

- toda Evidência possuir origem identificável;
- toda Evidência Derivada possuir linhagem completa;
- toda cadeia cognitiva puder ser reconstruída pelo Knowledge Graph;
- invalidações puderem ser analisadas;
- versões puderem ser rastreadas.

---

## Capítulo 6 — Integração Arquitetural e Regras de Consumo

### Objetivo do Capítulo
Definir as regras que governam a interação dos componentes do ecossistema ORYX/SOT com Evidências Cognitivas representadas pelo Canonical Evidence Model.

### Princípio Fundamental
Nenhum componente do sistema possui autoridade para reinterpretar ou modificar uma Evidência publicada. Os consumidores podem utilizar esse conhecimento. Não podem reescrevê-lo.

### Categorias de Interação
Todo componente interage com Evidências assumindo um ou mais dos seguintes papéis arquiteturais:

- **PRODUCER** — responsável por publicar Evidências
- **CONSUMER** — responsável por utilizar Evidências produzidas por terceiros
- **REPOSITORY** — responsável por armazenamento e preservação

> **Regra:** Um componente pode exercer múltiplos papéis arquiteturais perante o contrato. Nesse caso, deverá satisfazer os requisitos de conformidade de todos os papéis exercidos simultaneamente.

---

### PRODUCER

**Agentes Especializados (AGENT PRODUCERS):**
- Structural Agent, Institutional Agent, Macro Agent, Sentiment Agent, Risk Agent, Context Agent
- Produzem Evidências `PRIMARY`

**Motores Cognitivos (ENGINE PRODUCERS):**
- Fusion Engine *(único ENGINE PRODUCER atualmente autorizado)*
- Produz Evidências `DERIVED`
- Responsabilidades adicionais: produzir Evidências DERIVED, iniciar avaliação de impacto de invalidações sobre derivadas, respeitar regras de linhagem e de rastreabilidade

**Regras para PRODUCERS:**
Todo produtor deverá: obedecer integralmente ao contrato do Capítulo 3, obedecer ao ciclo de vida do Capítulo 4 e obedecer às regras de linhagem do Capítulo 5.

É proibido publicar Evidências incompletas, sem justificativa ou sem rastreabilidade.

---

### CONSUMER

**Componentes autorizados:** Manager Agent (Fase 2: Conviction), Manager Agent <!-- DIV-CEM-3/DIV-CEM-4 (2026-09-26): "Conviction Engine" e "Decision Orchestrator" absorvidos pelo Manager Agent — ADR-MANAGER-001 -->, futuros componentes cognitivos autorizados.

**Regras para CONSUMERS:**
Consumidores podem: ler Evidências, relacionar Evidências e ponderar Evidências.

Consumidores não podem: alterar Evidências, reinterpretar Evidências, modificar origem ou modificar linhagem.

> A interpretação pertence exclusivamente ao produtor.

---

### REPOSITORY

**Blackboard**
- Responsabilidade: compartilhamento cognitivo operacional
- Regra: opera apenas com Evidências em estado `ACTIVE`

**Knowledge Graph**
- Responsabilidade: memória cognitiva permanente
- Regra: preserva todos os estados, versões, linhagem e referências históricas
- Responsabilidade adicional: fornecer *Cognitive Trace Reconstruction* — reconstrução da cadeia cognitiva completa de qualquer Evidência a partir das relações de Lineage preservadas. Esta capacidade constitui o mecanismo oficial de Cognitive Trace Reconstruction do ecossistema ORYX/SOT.

---

### Integridade Cognitiva
Nenhum componente poderá alterar após publicação: Observation, Interpretation, Technical Rationale, Evidence Strength ou Lineage. A Evidência torna-se registro histórico imutável.

### Regra de Encapsulamento
Consumidores não devem depender de detalhes internos do produtor.

Exemplo — Conviction Engine:

- **Correto:** Interpretation, Evidence Strength, Domain
- **Incorreto:** Regras Elliott internas, lógica interna do Structural Agent, configuração de Skill

### Compatibilidade Futura
Novos componentes poderão ser adicionados ao ecossistema sem alteração estrutural do CEM, desde que respeitem o contrato canônico, a governança GMC-001 e as regras deste capítulo.

### Eventos Cognitivos
As seguintes mudanças no ciclo de vida de Evidências constituem eventos cognitivos canônicos:

- **Evidence Created**
- **Evidence Superseded**
- **Evidence Invalidated**
- **Evidence Archived**

> **Propagação:** Os eventos cognitivos produzidos por mudanças no ciclo de vida das Evidências serão propagados através da infraestrutura oficial de eventos cognitivos do Kernel, atualmente representada pelo **EC-COG-005 — Cognitive Event Bus**. O CEM não define o comportamento interno dessa infraestrutura. Define apenas que ela é o mecanismo oficial de propagação dos eventos canônicos relacionados às Evidências.

O CEM apenas reconhece a existência desses eventos. O tratamento dos eventos pertence aos componentes consumidores.

### Fronteira Arquitetural
O CEM define exclusivamente Evidências. Não define hipóteses, convicções, decisões, missões ou estratégias.

---

## Capítulo 7 — Governança e Evolução do Modelo

### Objetivo do Capítulo
Definir as regras que governam a evolução do Canonical Evidence Model ao longo do ciclo de vida do ecossistema ORYX/SOT.

### Princípio Fundamental
O Canonical Evidence Model constitui um contrato arquitetural compartilhado. Alterações no CEM devem ser tratadas como alterações de contrato. Nenhuma modificação poderá comprometer a interoperabilidade entre produtores e consumidores.

### Autoridade de Governança
A governança do CEM é subordinada ao **GMC-001 — Governança dos Modelos Canônicos**.

O CEM não possui governança própria. Toda evolução deverá obedecer às regras estabelecidas pelo GMC-001.

### Autoridade para Iniciar Evoluções
A autoridade para iniciar propostas de alteração do Canonical Evidence Model é definida exclusivamente pelo GMC-001.

O CEM não estabelece papéis de aprovação, revisão ou proposição. Essas responsabilidades pertencem integralmente ao processo de governança definido pelo GMC-001.

### Princípio de Estabilidade
Uma vez aprovado, o contrato canônico deverá permanecer estável. Mudanças frequentes são consideradas risco arquitetural, dado que o CEM é utilizado por múltiplos agentes, engines, repositórios e futuros Modelos Canônicos.

### Tipos de Evolução Permitidos

**Categoria A — Extensão**
Adição de capacidades sem quebra de compatibilidade.
- Exemplos: Novo Domain, Novo Market Context, Novo valor governado
- Não altera a estrutura do contrato
- Permitida via GMC-001

**Categoria B — Ampliação Estrutural**
Adição de novos elementos ao contrato.
- Exemplos: Novo campo canônico, Nova regra de rastreabilidade
- Expande o modelo

> **Regra de compatibilidade:** Uma Ampliação Estrutural somente será classificada como Categoria B quando preservar compatibilidade com produtores e consumidores existentes. Novos campos adicionados ao contrato deverão ser **opcionais** para implementações existentes.

**Reclassificação automática para Categoria C:** Uma proposta será automaticamente classificada como Categoria C quando: introduzir campo obrigatório, exigir alteração em produtores existentes, exigir alteração em consumidores existentes ou modificar comportamento previamente válido.

**Categoria C — Alteração Incompatível**
Mudança que rompe consumidores existentes.
- Exemplos: Remover campo obrigatório, alterar significado de campo existente, modificar semântica do contrato
- Desencorajada
- Exige nova versão principal do modelo (ex.: CEM v1.x → CEM v2.0)

### Compatibilidade Retroativa
O CEM deverá priorizar compatibilidade retroativa sempre que possível. Uma evolução não deverá obrigar consumidores existentes a serem reescritos.

### Versionamento do Modelo
Toda alteração aprovada deverá resultar em incremento de versão.

Exemplo conceitual:
```
CEM v1.0 → CEM v1.1 (Categoria A ou B)
CEM v1.x → CEM v2.0 (Categoria C)
```

### Mecanismo Deprecated
**Deprecated Field:** Campo do contrato canônico que permanece válido, porém encontra-se oficialmente marcado para descontinuação futura.

Regras:
- Um campo Deprecated continua sendo suportado e considerado válido
- Não pode ser removido imediatamente
- Deve permanecer documentado no modelo

Registro obrigatório: toda marcação Deprecated deverá ser registrada no **Histórico Oficial de Versões do Modelo**.

Prazo mínimo: nenhum campo poderá ser removido antes de uma versão principal subsequente.

Exemplo:
```
CEM v1.3 → Campo X marcado como Deprecated
CEM v2.0 → Campo X removido
```

### Critério para Novos Campos
Um novo campo somente poderá ser incorporado ao contrato quando: representar conhecimento reutilizável, beneficiar múltiplos consumidores, não puder ser tratado como metadado externo e justificar o aumento de complexidade.

### Critério para Remoção
Campos existentes não deverão ser removidos sem antes serem marcados como Deprecated. O processo de remoção segue o mecanismo Deprecated descrito acima.

### Relação com Outros Modelos Canônicos
O CEM não possui autoridade sobre CHM, CCM, CDM e CNM. Da mesma forma, esses modelos não possuem autoridade para alterar o contrato do CEM.

A evolução de modelos canônicos interdependentes deverá ocorrer por coordenação arquitetural via GMC-001.

### Princípio da Simplicidade
O CEM deverá permanecer o menor contrato capaz de representar Evidências Cognitivas de forma universal. Novos elementos somente serão aceitos quando simplificarem mais a arquitetura do que a tornarem complexa.

---

## Capítulo 8 — Conformidade e Certificação Arquitetural

### Objetivo do Capítulo
Definir os critérios formais utilizados para verificar se um componente do ecossistema ORYX/SOT está em conformidade com o Canonical Evidence Model.

### Princípio Fundamental
A conformidade com o CEM não é determinada pela intenção do componente. Ela é determinada pela aderência verificável ao contrato canônico.

### Escopo de Certificação
A certificação aplica-se a qualquer componente que interaja com Evidências Cognitivas, incluindo: AGENTS, ENGINES, REPOSITORIES e futuros componentes cognitivos autorizados.

### Regra de Multi-Role Compliance
Componentes que exercem múltiplos papéis arquiteturais perante o contrato devem satisfazer simultaneamente os requisitos de conformidade de todos os papéis exercidos.

Exemplo:
```
Fusion Engine
= Producer Compliance (produz Evidências DERIVED)
+ Consumer Compliance (consome Evidências ancestrais como insumo)
```

### Níveis de Conformidade

**Nível 1 — Producer Compliance**
Aplicável a componentes que produzem Evidências.

Requisitos obrigatórios:
- Gerar Evidências válidas e completas
- Obedecer ao contrato do Capítulo 3
- Obedecer ao ciclo de vida do Capítulo 4
- Obedecer às regras de linhagem do Capítulo 5
- Obedecer às regras de integração do Capítulo 6

Certificação: **CEM Producer Compliant**

**Nível 2 — Consumer Compliance**
Aplicável a componentes que consomem Evidências.

Requisitos obrigatórios:
- Consumir Evidências sem alterar seu conteúdo
- Respeitar estados válidos (apenas ACTIVE para inferência)
- Respeitar rastreabilidade
- Respeitar integridade cognitiva
- Não depender de detalhes internos do produtor

Certificação: **CEM Consumer Compliant**

**Nível 3 — Repository Compliance**
Aplicável a componentes responsáveis por armazenamento ou preservação.

Requisitos obrigatórios:
- Preservar integridade das Evidências
- Preservar histórico, estados, versões e linhagem

Requisitos adicionais para Knowledge Graph:
- Fornecer *Cognitive Trace Reconstruction* conforme definido no Capítulo 5

Certificação: **CEM Repository Compliant**

### Critérios de Não Conformidade
Um componente será considerado não conforme quando: alterar Evidências publicadas, remover rastreabilidade, quebrar regras de linhagem, ignorar estados do ciclo de vida ou violar regras de governança.

### Evidências de Conformidade
A conformidade deverá ser demonstrável por: testes de integração, validações de contrato, auditorias arquiteturais ou verificações automatizadas. O CEM não define a ferramenta de validação — define apenas os critérios.

### Declaração de Versão do CEM
Todo componente que interaja com Evidências deverá declarar explicitamente a versão do CEM suportada.

> **Regra:** A versão suportada do CEM é um atributo da especificação arquitetural do componente. Não constitui campo armazenado na Evidência. A governança e o processo formal de declaração e registro de versão são definidos pelo GMC-001.

### Compatibilidade entre Componentes
Dois componentes serão considerados interoperáveis quando ambos estiverem conformes ao CEM e utilizarem a mesma versão compatível do modelo.

### Critério para Certificação Arquitetural
Um componente será considerado certificado quando: satisfizer todos os requisitos aplicáveis ao seu papel arquitetural, demonstrar conformidade verificável e não possuir violações conhecidas do contrato.

### Suspensão de Certificação
A certificação deverá ser considerada suspensa quando: o componente deixar de obedecer ao contrato, utilizar versão incompatível, produzir Evidências inválidas ou comprometer rastreabilidade.

> **Propagação:** A suspensão de certificação constitui evento arquitetural relevante. Sua comunicação ao ecossistema deverá ocorrer através da infraestrutura de eventos cognitivos do Kernel (EC-COG-005), seguindo o mesmo padrão dos Cognitive Events definidos no Capítulo 6.

### Revalidação
Mudanças significativas no componente deverão resultar em nova verificação de conformidade. Exemplos: mudança de versão do CEM suportada, mudança de contrato ou mudança estrutural relevante no componente.

### Relação com GMC-001
O processo formal de aprovação, auditoria e governança da certificação é definido pelo GMC-001.

O presente capítulo define: o que significa estar conforme.

Não define: quem aprova, quem audita, quem certifica.

### Critério de Conclusão do Modelo
O Canonical Evidence Model será considerado completo quando: todos os capítulos obrigatórios estiverem aprovados, o contrato estiver estável, os critérios de conformidade estiverem definidos e a governança estiver estabelecida.

---

## Registro de Decisões Incorporadas

| Decisão | Capítulo Afetado | Origem |
|---|---|---|
| Fusion Engine: único ENGINE producer confirmado | 2, 6 | Auditoria Cap. 2 |
| Learning Engine e Pattern Engine: removidos como produtores | 2 | Auditoria Cap. 2 |
| Explainability Layer → "Componentes de Explicabilidade autorizados" | 2 | Auditoria Cap. 2 |
| Evidence Strength: Float 0.0→1.0 (imutável) | 3, 4 | Adendo Cap. 3 |
| Domain: Governed Enumeration sob GMC-001 | 3 | Adendo Cap. 3 |
| Context Reference removido | 3 | Adendo Cap. 3 |
| Timeframe Reference adicionado (enumeração estática) | 3, 4 | Adendo Cap. 3 |
| Market Context adicionado (Governed Enumeration GMC-001) | 3, 4 | Adendo Cap. 3 |
| Trace Chain removida do contrato | 3, 4, 5 | Decisão Cap. 5 |
| Cognitive Depth: métrica derivada, não campo | 3, 5 | Decisão Cap. 5 |
| Lista de campos imutáveis completa | 4 | Adendo Cap. 4 |
| Status: único campo mutável (explícito) | 3, 4 | Adendo Cap. 4 |
| Fusion Engine: responsabilidade de avaliação de impacto | 4 | Adendo Cap. 4 |
| Cognitive Trace Reconstruction: capacidade do Knowledge Graph | 5, 6 | Decisão Cap. 5 |
| Evidence Invalidated: nomenclatura canônica (substituiu Cognitive Invalidation Event) | 5, 6 | Consistência cruzada |
| Taxonomia: PROCESSOR removido | 6 | Adendo Cap. 6 |
| Knowledge Graph: Cognitive Trace Reconstruction como responsabilidade | 6, 8 | Adendo Cap. 6 |
| EC-COG-005 como mecanismo de propagação de eventos | 6 | Adendo Cap. 6 |
| Fronteira B/C: opcional vs. obrigatório | 7 | Adendo Cap. 7 |
| Deprecated Field: definição formal | 7 | Adendo Cap. 7 |
| Autoridade de proposição: delegação explícita ao GMC-001 | 7 | Adendo Cap. 7 |
| Multi-Role Compliance | 8 | Auditoria Cap. 8 |
| Declaração de versão: atributo arquitetural, não campo da Evidência | 8 | Auditoria Cap. 8 |
| Suspensão de certificação: propagação via EC-COG-005 | 8 | Auditoria Cap. 8 |
