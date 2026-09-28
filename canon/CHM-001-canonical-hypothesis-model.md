# CHM-001 — Canonical Hypothesis Model (consolidado)
<!-- Consolidação dos capítulos 1-4 (fonte: DOCUMENTOS INICIAIS/02_Modelos_Canonicos). BASELINED (Q-001). Original intacto no arquivo-fonte. -->


---

# CHM-001 — Canonical Hypothesis Model
## Capítulo 1 — Identidade do Modelo

**Classificação Constitucional:** Nível 1 — Constituição (GES-1, PPQ-001 §10.2)
**Status:** CONSOLIDADO — aprovado por Andraus (Decisor Final) em 12/07/2026
**Rastreabilidade:** extraído literalmente de 6 ADRs Vigentes na MIC-CHM (ADR-CHM-001-001, 002, 003, 004, 005; ADR-CANONICAL-001)
**Auditoria:** 2 rodadas (Obs.CHM-1/2/9/10/11/12 — todas resolvidas ou registradas como não bloqueantes)

---

## 1.1 Propósito

O CHM-001 estabelece o Modelo Canônico de Hipóteses do SOT.

Este modelo define:

- a identidade constitucional de uma hipótese;
- a taxonomia canônica de hipóteses;
- o modelo de Confidence;
- o modelo de Estado Epistêmico;
- a estrutura hierárquica de hipóteses;
- a separação formal entre Hipótese, Evidência e Convicção.

O CHM-001 não define:

- regras de composição por domínio;
- mecanismos de decisão;
- algoritmos de cálculo de Convicção Global;
- comportamento operacional de agentes.

Esses elementos pertencem a documentos específicos de suas respectivas camadas arquiteturais.

---

## 1.2 Identidade Constitucional da Hipótese

Uma hipótese é a melhor representação explicável do estado atual do domínio observado produzida a partir da convergência de evidências independentes e continuamente sujeita à refutação.

Esta definição constitui a identidade canônica da entidade Hipótese dentro da arquitetura ORYX.

`[Origem: ADR-CHM-001-004, Vigente]`

---

## 1.3 Taxonomia Canônica

A taxonomia canônica de hipóteses é composta pelos seguintes tipos canônicos:

- DESCRIPTIVE
- EXPLANATORY
- PREDICTIVE
- DIAGNOSTIC

A inclusão, remoção ou alteração de tipos canônicos deverá seguir GMC-001.

`[Origem: ADR-CHM-001-001, Vigente]`

---

## 1.4 Semântica Canônica da Taxonomia

### DESCRIPTIVE

Hipótese destinada a representar ou descrever um estado observado de um domínio.

Pergunta fundamental: *"O que está acontecendo?"*

Não explica causas. Não identifica anomalias. Não produz projeções futuras.

### EXPLANATORY

Hipótese destinada a explicar relações, mecanismos ou causas associadas a um estado observado de um domínio.

Pergunta fundamental: *"Por que isto está acontecendo?"*

Aplica-se independentemente de o estado observado representar comportamento esperado, normal ou anômalo. Quando os critérios de DIAGNOSTIC forem simultaneamente satisfeitos, a classificação correta deverá ser DIAGNOSTIC. A aplicabilidade de EXPLANATORY a comportamentos anômalos significa apenas ausência de restrição por normalidade, não eliminação da precedência de DIAGNOSTIC.

### PREDICTIVE

Hipótese destinada a representar estados futuros possíveis de um domínio observado.

Pergunta fundamental: *"O que provavelmente acontecerá?"*

Não descreve estados atuais. Não identifica causas. Não diagnostica anomalias.

### DIAGNOSTIC

Hipótese destinada a identificar condições, falhas, anomalias, degradações, inconsistências ou fatores responsáveis por um comportamento observado.

Pergunta fundamental: *"Qual condição específica explica este comportamento?"*

Aplica-se especificamente quando o comportamento observado representa anomalia, degradação, inconsistência, falha ou desvio em relação ao estado esperado. Quando os critérios desta categoria forem satisfeitos, DIAGNOSTIC possui precedência classificatória sobre EXPLANATORY.

`[Origem: ADR-CHM-001-005 REV.2, Vigente]`

---

## 1.5 Critério de Classificação

A classificação de uma hipótese deverá ser determinada exclusivamente pela natureza da afirmação representada.

A classificação não deverá depender:

- do Confidence;
- do Estado Epistêmico;
- da posição hierárquica;
- da Convicção Global do sistema.

Quando houver potencial sobreposição entre categorias, deverá existir regra explícita de desambiguação. A precedência entre DIAGNOSTIC e EXPLANATORY segue o disposto em §1.4.

`[Origem: ADR-CHM-001-005 REV.2, CA-3/CA-6/CA-7, Vigente]`

---

## 1.6 Confidence

Toda hipótese deverá possuir um campo Confidence.

Confidence representa o grau de confiança associado à versão específica da hipótese.

Confidence:

- utiliza escala contínua de 0.0 a 1.0;
- é imutável por versão;
- poderá variar apenas mediante criação de nova versão da hipótese.

Confidence não representa Convicção Global.

`[Origem: ADR-CHM-001-002, Vigente]`

---

## 1.7 Estado Epistêmico

Toda hipótese deverá possuir um Estado Epistêmico.

Os estados canônicos são:

- EMERGENT
- CANDIDATE
- ACTIVE
- DOMINANT
- SUPERSEDED
- REFUTED
- ARCHIVED

O Estado Epistêmico é mutável ao longo do ciclo de vida da hipótese.

Confidence e Estado Epistêmico constituem campos independentes. A alteração de um deles não implica alteração automática do outro.

`[Origem: ADR-CHM-001-002, Vigente]`

---

## 1.8 Estrutura Hierárquica

O contrato canônico de hipótese deverá suportar os seguintes campos relacionais:

- `parent_hypothesis_id`
- `child_hypothesis_ids`
- `sibling_hypothesis_ids`
- `generation`

A estrutura hierárquica possui caráter exclusivamente relacional.

Regras de composição por domínio permanecem fora do escopo do CHM-001.

`[Origem: ADR-CHM-001-003, Vigente]`

---

## 1.9 Separação Tríplice

O ORYX adota separação formal entre:

**Evidência** — Representada exclusivamente pelo CEM-001. Responsável pelo campo Evidence Confidence.

**Hipótese** — Representada exclusivamente pelo CHM-001. Responsável pelo campo Hypothesis Confidence.

**Convicção Global** — Representada exclusivamente pelo CCM-001. Responsável pelo cálculo sistêmico de Conviction.

Nenhum dos três níveis deverá contaminar os demais. O CHM-001 não calcula Convicção Global. O CHM-001 não altera Evidence Confidence. O CCM-001 não redefine Confidence de Hipóteses.

**Nota de Interpretação (Obs.CHM-6):** o termo "domínio observado" utilizado neste capítulo representa um conceito arquitetural genérico. Ele não deve ser interpretado como equivalente ao campo formal `Domain` definido em CEM-001.

`[Origem: ADR-CANONICAL-001, Vigente; verificado contra CEM-001_Versao_Consolidada.md sem conflito]`

---

## 1.10 Definições Fundamentais

| Termo | Definição |
|---|---|
| Hipótese | Melhor representação explicável do estado atual do domínio observado produzida a partir da convergência de evidências independentes e continuamente sujeita à refutação |
| Confidence | Grau de confiança associado a uma versão específica de uma hipótese |
| Estado Epistêmico | Situação atual da hipótese dentro do seu ciclo de vida |
| Taxonomia | Classificação canônica da natureza da hipótese |
| Hierarquia | Estrutura relacional entre hipóteses |
| Convicção Global | Resultado sistêmico calculado pelo CCM-001 |
| Domínio Observado | Contexto observado ao qual a hipótese se refere |

---

## 1.11 Classificação PPQ-001 (5W2H)

| Elemento | Definição |
|---|---|
| What | Modelo Canônico de Hipóteses |
| Why | Padronizar a representação constitucional de hipóteses |
| Who | Todos os componentes arquiteturais que produzem ou consomem hipóteses |
| Where | Camada Canônica do ORYX |
| When | Sempre que uma hipótese for criada, modificada ou utilizada |
| How | Aplicação obrigatória do contrato definido neste capítulo |
| How Much | Não aplicável |

---

## Nota de Auditoria (Obs.CHM-12, não bloqueante)

Pequenas variações de fraseado entre este texto e a redação literal exata dos ADRs de origem (frases introdutórias das definições da taxonomia) foram identificadas e registradas como não bloqueantes — não afetam significado nem reabrem nenhuma ambiguidade resolvida nas rodadas de correção (Obs.CHM-7, Obs.CHM-8). Candidatas a polimento em revisão futura, sem urgência.

---

**Declaração de Consenso:** aprovado por Andraus (Decisor Final) em 12/07/2026, após parecer técnico CONFORME do Analista (2 rodadas de auditoria — Obs.CHM-9/10/11 na primeira submissão, corrigidas na REV.1 aqui consolidada).

---

# CHM-001 — Canonical Hypothesis Model
## Capítulo 2 — Modelo Canônico de Hipóteses

**Classificação Constitucional:** Nível 1 — Constituição (GES-1, PPQ-001 §10.2)
**Status:** CONSOLIDADO — aprovado por Andraus (Decisor Final) em 12/07/2026
**Rastreabilidade:** extraído literalmente de 9 ADRs Vigentes na MIC-CHM (ADR-CHM-001-001 a 008, ADR-CANONICAL-001)
**Auditoria:** 2 rodadas (Obs.CHM-17/18 — resolvidas na REV.2, com transcrição literal integral dos ADR-007/008)
**Regra de processo aplicada:** RCN-001 — toda definição/restrição/CE/RN aprovada por ADR Vigente é incorporada por transcrição literal, não paráfrase

---

## 2.1 Objetivo

Este capítulo define a estrutura canônica mínima que toda Hipótese publicada na arquitetura ORYX deverá respeitar.

O objetivo do modelo é garantir:

- interoperabilidade entre produtores e consumidores;
- rastreabilidade completa da origem da hipótese;
- suporte à coexistência de hipóteses concorrentes;
- compatibilidade com os modelos canônicos vigentes e componentes autorizados da arquitetura;
- independência em relação ao domínio produtor.

---

## 2.2 Princípio da Neutralidade de Domínio

O CHM-001 não contém conhecimento específico de qualquer domínio analítico.

O modelo deverá ser igualmente aplicável a hipóteses estruturais, institucionais, macroeconômicas, comportamentais ou produzidas por Engines especializados.

Todo conteúdo específico de domínio deverá ser armazenado em extensões especializadas definidas pelos produtores autorizados.

---

## 2.3 Estrutura Geral do Contrato

O Contrato Canônico de Hipóteses é composto por três grupos:

**Core Fields** — Campos universais obrigatórios.

**Derived Properties** — Propriedades derivadas calculadas a partir do contrato canônico.

**Extension Fields** — Campos especializados dependentes de domínio.

---

## 2.4 Core Fields

**Identificação** — `hypothesis_id`, `version`, `previous_version_id`. Objetivo: garantir identidade única, versionamento, rastreabilidade e imutabilidade histórica.

**Classificação** — `hypothesis_type`, `generation_mechanism`.

---

## 2.5 hypothesis_type

`hypothesis_type` é uma Governed Enumeration submetida à governança definida pelo GMC-001.

Valores iniciais aprovados: DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC.

A inclusão, remoção ou alteração de valores requer governança formal.

`[Origem: ADR-CHM-001-001, Vigente]`

---

## 2.6 generation_mechanism

Campo opcional.

Representa exclusivamente o mecanismo pelo qual a hipótese foi produzida.

Valores iniciais aprovados: OBSERVATIONAL, INFERENTIAL, SIMULATED, COMPOSITE.

**OBSERVATIONAL** — Hipótese produzida diretamente a partir da observação de evidências disponíveis, sem necessidade de inferência adicional relevante.

**INFERENTIAL** — Hipótese produzida por inferência lógica, analítica ou causal a partir de evidências disponíveis, para estabelecer relações, explicações, diagnósticos ou conclusões não explicitamente presentes nas evidências.

**SIMULATED** — Hipótese produzida por modelos, simulações, projeções ou ambientes simulados.

**COMPOSITE** — Hipótese produzida pela combinação de múltiplos mecanismos de geração.

`generation_mechanism` descreve exclusivamente o mecanismo de geração da hipótese. `generation_mechanism` não descreve o conteúdo da hipótese. `generation_mechanism` não substitui `hypothesis_type`. `generation_mechanism` não altera `confidence`. `generation_mechanism` não altera `epistemic_state`. `generation_mechanism` não altera Internal Strength. `generation_mechanism` não constitui Conviction Global.

Hipóteses com o mesmo conteúdo podem possuir mecanismos de geração diferentes.

`[Origem: ADR-CHM-001-007, Vigente — texto literal completo, incluindo RN-1 a RN-7]`

---

## 2.7 Estado Epistêmico

Campo: `epistemic_state` — Governed Enumeration submetida ao GMC-001.

Valores iniciais: EMERGENT, CANDIDATE, ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED.

**EMERGENT** — Hipótese recém-formulada, ainda sem validação suficiente.
**CANDIDATE** — Hipótese em avaliação com evidências favoráveis parciais.
**ACTIVE** — Hipótese considerada válida e sustentada pelas evidências disponíveis.
**DOMINANT** — Hipótese preferencial entre hipóteses concorrentes compatíveis.
**SUPERSEDED** — Hipótese substituída por versão posterior ou hipótese superior.
**REFUTED** — Hipótese invalidada por critério explícito de refutação.
**ARCHIVED** — Hipótese retirada da camada operacional, preservada historicamente.

As regras formais de transição entre estados são definidas no Capítulo 4.

`[Origem: ADR-CHM-001-002, Vigente + Correção 2 (semântica mínima)]`

---

## 2.8 Confidence

Campo: `confidence` — Float entre 0.0 e 1.0.

Representa a confiança atribuída pelo produtor no momento da publicação.

Confidence é: obrigatório; persistido; imutável por versão; específico daquela versão da hipótese.

Confidence não representa Internal Strength. Confidence não representa Conviction Global. Confidence não altera `epistemic_state`.

`[Origem: ADR-CHM-001-002, Vigente]`

---

## 2.9 Provenance

Campos: `producer_type`, `producer_id`, `created_at`.

Objetivo: garantir rastreabilidade completa da origem da hipótese.

---

## 2.10 Fundamentação por Evidências

Campos: `supporting_evidence_ids`, `refuting_evidence_ids`.

Objetivo: registrar explicitamente as evidências favoráveis e contrárias associadas à hipótese.

Uma hipótese pode ser associada a uma ou mais evidências de suporte e a uma ou mais evidências de refutação. A presença de evidências contrárias não invalida automaticamente a hipótese. Sua função é preservar transparência, auditabilidade e refutabilidade.

### 2.10.1 Hipótese Órfã

Uma Hipótese Canônica que não possua referências válidas em `supporting_evidence_ids` é considerada uma Hipótese Órfã.

Hipóteses Órfãs podem existir temporariamente no estado EMERGENT durante processos exploratórios, investigativos ou de formulação inicial.

Hipóteses Órfãs não poderão atingir os estados ACTIVE ou DOMINANT enquanto permanecerem sem fundamentação por Evidências Canônicas válidas.

A condição de orfandade não constitui refutação. A condição de orfandade não constitui invalidação estrutural da hipótese.

A condição de orfandade não altera: confidence; generation_mechanism; hypothesis_type; Internal Strength; Conviction Global.

**CE-1 — Compatibilidade com a Definição Constitucional**

A definição constitucional de Hipótese estabelecida por ADR-CHM-001-004 descreve a natureza epistemológica da entidade Hipótese e não uma pré-condição de existência formal no contrato canônico.

A expressão *"produzida a partir da convergência de evidências independentes"* deve ser interpretada como a finalidade epistemológica da Hipótese dentro da arquitetura ORYX, representando o estado desejado de maturidade cognitiva da entidade.

Uma Hipótese Órfã é considerada uma Hipótese Canônica formalmente válida cuja convergência evidencial ainda não foi completada. A ausência temporária de referências válidas em `supporting_evidence_ids` não invalida sua identidade constitucional nem sua existência contratual. Entretanto, a condição de orfandade impõe restrições explícitas de progressão epistêmica definidas neste modelo.

A resolução da orfandade ocorre quando pelo menos uma Evidência Canônica válida passa a compor `supporting_evidence_ids`.

`[Origem: ADR-CHM-001-008, Vigente — texto literal completo, incluindo RN-1 a RN-5 e CE-1]`

---

## 2.11 Relações entre Hipóteses

Campos: `depends_on_hypothesis_ids`, `competing_hypothesis_ids`.

**Dependência** — Uma hipótese dependente estabelece relação explícita de dependência com outra hipótese canônica. Os efeitos operacionais dessa dependência são definidos pelos capítulos responsáveis pelo ciclo de vida e pelas regras de transição epistêmica.

**Competição** — Hipóteses concorrentes representam interpretações incompatíveis para um mesmo fenômeno. A coexistência de hipóteses concorrentes é permitida pela arquitetura.

`[Nota: mecanismo operacional de dependência deliberadamente diferido para os capítulos de ciclo de vida/transição — Obs.CHM-18]`

---

## 2.12 Estrutura Hierárquica

Campos: `parent_hypothesis_id`, `child_hypothesis_ids`, `sibling_hypothesis_ids`, `generation`.

Objetivo: representar estruturas compostas e relações hierárquicas entre hipóteses.

As regras específicas de composição permanecem responsabilidade dos domínios produtores.

`[Origem: ADR-CHM-001-003, Vigente]`

---

## 2.13 Derived Properties

As propriedades derivadas não integram o contrato persistido. São calculadas pelos consumidores quando necessário.

**Internal Strength** — propriedade derivada, calculada exclusivamente a partir da relação entre `supporting_evidence_ids` e `refuting_evidence_ids`. Objetivo: representar a robustez interna demonstrada pela hipótese ao longo de seu ciclo de vida.

Internal Strength: não é armazenada; não integra o contrato persistido; é recalculável; não altera a hipótese; não altera confidence; não altera epistemic_state; não substitui hypothesis_type; não substitui generation_mechanism; não constitui Conviction Global.

`[Origem: ADR-CHM-001-006, Vigente]`

---

## 2.14 Princípio da Não Equivalência

Os seguintes conceitos são distintos e não podem ser utilizados como substitutos entre si:

- **Evidence Confidence** — Definido pelo CEM-001.
- **Hypothesis Confidence** — Definido pelo CHM-001.
- **Internal Strength** — Propriedade derivada definida pelo CHM-001.
- **Global Conviction** — Definida pelo futuro CCM-001.

Nenhum destes níveis poderá substituir, sobrescrever ou inferir automaticamente qualquer outro.

`[Origem: ADR-CANONICAL-001, Vigente]`

---

## 2.15 Extension Fields

Campos específicos de domínio deverão ser armazenados em `domain_payload`.

O CHM-001 não define a estrutura interna do payload. Cada domínio é responsável por sua própria extensão especializada.

---

## 2.16 Produtores Autorizados

Podem publicar hipóteses compatíveis com o CHM-001: AGENTS autorizados; ENGINES autorizados.

A autorização é definida pelos contratos de governança vigentes.

---

## 2.17 Consumidores Esperados

O Contrato Canônico de Hipóteses poderá ser consumido por componentes autorizados da arquitetura responsáveis por: consolidação de estado cognitivo; avaliação de convicção; execução de missão; explicabilidade; aprendizado; coordenação cognitiva; demais processos aprovados pela governança arquitetural vigente.

O CHM-001 não estabelece dependência obrigatória de qualquer componente específico da arquitetura.

`[Correção 1 aplicada — linguagem agnóstica, sem nomear SSE-001 diretamente]`

---

## 2.18 Critério de Conformidade

Uma hipótese será considerada compatível com o CHM-001 quando:

- respeitar todos os Core Fields obrigatórios;
- manter rastreabilidade completa;
- preservar versionamento histórico;
- registrar fundamentação por evidências;
- respeitar a Separação Tríplice definida pela arquitetura;
- preservar a distinção entre Confidence, Internal Strength e Conviction Global;
- respeitar as restrições associadas à condição de Hipótese Órfã;
- permanecer independente de qualquer domínio específico.

---

## Regra de Processo Aplicada — RCN-001

> Toda definição, restrição normativa, cláusula de desambiguação, regra de precedência, CE, RN, critério operacional ou texto constitucional aprovado por ADR Vigente deverá ser incorporado aos capítulos por transcrição literal da MIC-CHM. Consolidações futuras não poderão resumir, simplificar ou parafrasear conteúdo normativo já constitucionalizado.

Adotada nesta rodada para eliminar a recorrência de perda de cláusulas de desambiguação (Obs.CHM-10, Obs.CHM-17).

---

**Declaração de Consenso:** aprovado por Andraus (Decisor Final) em 12/07/2026, após parecer técnico CONFORME do Analista (2 rodadas de auditoria — Obs.CHM-17/18 na primeira submissão, corrigidas na REV.2 aqui consolidada).

---

# CHM-001 — Canonical Hypothesis Model
## Capítulo 3 — Ciclo de Vida da Hipótese Canônica

**Classificação Constitucional:** Nível 1 — Constituição (GES-1, PPQ-001 §10.2)
**Status:** CONSOLIDADO — aprovado por Andraus (Decisor Final) em 12/07/2026
**Rastreabilidade:** extraído literalmente de 5 ADRs Vigentes (ADR-CHM-001-002, 008, 011, 012, 013)
**Auditoria:** 2 rodadas (Obs.CHM-25 Crítica e Obs.CHM-26 Menor — ambas resolvidas na REV.1)
**Regra de processo aplicada:** RCN-001 — transcrição literal obrigatória de conteúdo já constitucionalizado

---

## 3.1 Criação da Hipótese

O ciclo de vida de uma Hipótese Canônica inicia-se quando um produtor autorizado publica uma nova hipótese compatível com os requisitos definidos pelo CHM-001.

Toda hipótese criada deverá possuir identidade própria, produtor identificável, estado epistêmico e rastreabilidade histórica compatíveis com os requisitos do modelo.

Uma hipótese pode ser criada antes da existência de Evidências Canônicas associadas.

Uma Hipótese Canônica que não possua referências válidas em `supporting_evidence_ids` é considerada uma Hipótese Órfã.

Hipóteses Órfãs podem existir temporariamente durante:

- exploração analítica;
- investigação inicial;
- formulação preliminar;
- descoberta de padrões;
- geração inicial de hipóteses.

A condição de Hipótese Órfã não constitui defeito estrutural do contrato canônico.

Hipóteses Órfãs não poderão atingir os estados ACTIVE ou DOMINANT enquanto permanecerem sem fundamentação por Evidências Canônicas válidas.

A condição de Hipótese Órfã é automaticamente removida quando pelo menos uma Evidência Canônica válida passa a compor `supporting_evidence_ids`.

A definição constitucional de Hipótese como entidade produzida a partir da convergência de evidências independentes deve ser interpretada como a finalidade epistemológica da Hipótese dentro da arquitetura ORYX, representando o estado desejado de maturidade cognitiva da entidade.

A ausência de evidências no momento da criação não invalida a identidade constitucional da hipótese.

Uma Hipótese Órfã representa uma hipótese formalmente válida cuja convergência evidencial ainda está incompleta.

`[Origem: ADR-CHM-001-002, ADR-CHM-001-008 (CE-1 integral), Vigentes]`

---

## 3.2 Evolução e Versionamento

A evolução de uma hipótese ocorre por meio da publicação de novas versões ou da criação de novas hipóteses.

Refinamentos que preservam a identidade semântica da afirmação central da hipótese constituem novas versões.

Mudanças que alteram a interpretação fundamental do fenômeno observado constituem novas hipóteses.

O Teste da Identidade Semântica deverá ser utilizado para distinguir os dois casos.

Se a remoção de detalhes secundários preservar a afirmação central originalmente representada, a alteração caracteriza uma Nova Versão.

Se a remoção de detalhes secundários alterar a afirmação central originalmente representada, a alteração caracteriza uma Nova Hipótese.

Mudanças de dominância entre hipóteses concorrentes não criam novas versões nem novas hipóteses.

Mudanças de estado epistêmico não criam novas versões automaticamente.

Mudanças de `hypothesis_type` para o mesmo fenômeno observado caracterizam obrigatoriamente uma Nova Hipótese.

A aplicação do Teste da Identidade Semântica é responsabilidade do produtor da hipótese.

A classificação resultante permanece sujeita a auditoria e questionamento retroativo pela Governança.

Questionamentos posteriores não alteram registros históricos já produzidos, preservando a integridade da rastreabilidade histórica.

`[Origem: ADR-CHM-001-011 (R1-R7, N1), Vigente]`

---

## 3.3 Monotonicidade Histórica de Versionamento

A linhagem histórica de versões de uma Hipótese Canônica deverá ser monotônica, acumulativa e preservada integralmente.

Uma nova versão sempre amplia a cadeia histórica existente.

Nenhuma versão anterior poderá ser removida, reordenada ou substituída retroativamente.

Toda nova versão deverá referenciar exatamente uma versão anterior por meio de `previous_version_id`.

A primeira versão de uma hipótese não possui predecessor.

Após publicada, a relação entre uma versão e seu predecessor torna-se parte permanente da linhagem histórica e não poderá ser alterada.

Não é permitido modificar a ordem histórica das versões já publicadas.

Não é permitido remover versões intermediárias da cadeia histórica.

A evolução histórica ocorre exclusivamente por adição de novas versões.

O histórico é append-only.

Versionamento e estado epistêmico são mecanismos independentes.

A transição de estado não altera a cadeia histórica.

A cadeia histórica constitui parte permanente da memória cognitiva da arquitetura.

`[Origem: ADR-CHM-001-013 (R1-R8), Vigente]`

---

## 3.4 Refutação

Uma hipótese é considerada REFUTED quando for invalidada por critério explícito de refutação definido pelos mecanismos autorizados da arquitetura.

A refutação altera exclusivamente o estado epistêmico da hipótese.

A refutação não remove a hipótese.

A refutação não remove versões históricas.

A refutação não interrompe a cadeia de rastreabilidade.

REFUTED não é equivalente a DELETE.

Hipóteses refutadas permanecem disponíveis para auditoria, explicabilidade, aprendizado e reconstrução histórica.

A condição de REFUTED não se propaga automaticamente para hipóteses relacionadas.

`[Origem: ADR-CHM-001-002, ADR-CHM-001-012 (R6), Vigentes]`

---

## 3.5 Substituição e Arquivamento

Uma hipótese é considerada SUPERSEDED quando for substituída por hipótese posterior considerada superior para representar determinado fenômeno.

SUPERSEDED não é equivalente a REFUTED.

Uma hipótese SUPERSEDED permanece historicamente válida como registro de estado cognitivo anterior.

A substituição de uma hipótese não remove seu histórico.

A substituição não remove hipóteses dependentes.

Quando uma hipótese referenciada por `depends_on_hypothesis_ids` atingir REFUTED ou SUPERSEDED, as hipóteses dependentes tornam-se elegíveis para revisão pelo respectivo produtor.

A revisão não implica alteração automática de estado.

Uma hipótese é considerada ARCHIVED quando for retirada da camada operacional da arquitetura.

ARCHIVED não implica remoção histórica.

ARCHIVED não implica invalidação.

ARCHIVED preserva integralmente a rastreabilidade histórica da hipótese.

Hipóteses arquivadas permanecem disponíveis para processos de Explainability, Learning e Auditoria.

`[Origem: ADR-CHM-001-002, ADR-CHM-001-011 (R5), ADR-CHM-001-012 (R3-R5), Vigentes]`

---

## 3.6 Princípio da Não Cascata

Mudanças de estado epistêmico não se propagam automaticamente entre hipóteses relacionadas.

A alteração de estado de uma hipótese afeta exclusivamente a própria hipótese.

A ocorrência de REFUTED não refuta automaticamente hipóteses dependentes.
A ocorrência de REFUTED não refuta automaticamente hipóteses concorrentes.
A ocorrência de REFUTED não refuta automaticamente hipóteses hierarquicamente relacionadas.

A ocorrência de SUPERSEDED não substitui automaticamente hipóteses dependentes.
A ocorrência de SUPERSEDED não substitui automaticamente hipóteses concorrentes.
A ocorrência de SUPERSEDED não substitui automaticamente hipóteses hierarquicamente relacionadas.

A ocorrência de ARCHIVED não arquiva automaticamente hipóteses dependentes.
A ocorrência de ARCHIVED não arquiva automaticamente hipóteses concorrentes.
A ocorrência de ARCHIVED não arquiva automaticamente hipóteses hierarquicamente relacionadas.

Dependências estruturais representam relações de análise e rastreabilidade, não mecanismos automáticos de propagação de estado.

Qualquer alteração em hipóteses relacionadas exige avaliação explícita realizada por produtor autorizado.

O modelo canônico adota o Princípio da Não Cascata como mecanismo obrigatório de preservação da autonomia analítica entre hipóteses.

`[Origem: ADR-CHM-001-012 (R1-R4), Vigente — granularidade completa]`

---

## Nota Editorial

A estrutura 3.1–3.6 (com Monotonicidade Histórica como seção própria e Substituição+Arquivamento fundidos) foi fixada como definitiva nesta consolidação, por decisão do Estrategista sem objeção de Andraus. ADR-013 ganhou peso suficiente para seção independente; Substituição e Arquivamento compartilham o mesmo momento tardio do ciclo de vida e possuem forte acoplamento semântico, sem perda de nenhuma regra normativa pela fusão.

---

**Declaração de Consenso:** aprovado por Andraus (Decisor Final) em 12/07/2026, após parecer técnico CONFORME do Analista (2 rodadas de auditoria — Obs.CHM-25 [Crítica] e Obs.CHM-26 [Menor] na primeira submissão, corrigidas na REV.1 aqui consolidada).

---

# CHM-001 — Canonical Hypothesis Model
## Capítulo 4 — Máquina de Estados Epistêmicos

**Classificação Constitucional:** Nível 1 — Constituição (GES-1, PPQ-001 §10.2)
**Status:** CONSOLIDADO — aprovado por Andraus (Decisor Final) em 12/07/2026
**Rastreabilidade:** extraído literalmente de 8 ADRs Vigentes (ADR-CHM-001-002, 008, 011, 013, 014, 015, 016, 017)
**Auditoria:** 3 rodadas (Obs.CHM-38 Crítica, Obs.CHM-39 Menor, Obs.CHM-40 Crítica, Obs.CHM-41 Menor — todas resolvidas)
**Regra de processo aplicada:** RCN-001 — transcrição literal obrigatória de conteúdo já constitucionalizado

---

## 4.1 Finalidade

A Máquina de Estados Epistêmicos define as transições permitidas e proibidas entre os Estados Epistêmicos Canônicos do CHM-001.

Sua finalidade é garantir consistência operacional, rastreabilidade histórica, governança auditável e evolução controlada do conhecimento ao longo do ciclo de vida das hipóteses.

Este capítulo regula exclusivamente:

- transições entre estados;
- elegibilidade para transições;
- autoridade para executar transições;
- histórico das transições realizadas.

A criação, versionamento, refutação, substituição, arquivamento e demais aspectos do ciclo de vida permanecem definidos pelo Capítulo 3.

---

## 4.2 Estados Epistêmicos Canônicos

Conforme ADR-CHM-001-002, os Estados Epistêmicos Canônicos são: EMERGENT, CANDIDATE, ACTIVE, DOMINANT, REFUTED, SUPERSEDED, ARCHIVED.

Nenhum outro estado é reconhecido pelo CHM-001.

---

## 4.3 Grafo Canônico de Transições

As seguintes transições são permitidas:

| Origem | Destino |
|---|---|
| EMERGENT | CANDIDATE |
| EMERGENT | ARCHIVED |
| CANDIDATE | ACTIVE |
| CANDIDATE | REFUTED |
| CANDIDATE | ARCHIVED |
| ACTIVE | DOMINANT |
| ACTIVE | REFUTED |
| ACTIVE | SUPERSEDED |
| ACTIVE | ARCHIVED |
| DOMINANT | REFUTED |
| DOMINANT | SUPERSEDED |
| DOMINANT | ARCHIVED |
| REFUTED | ARCHIVED |
| SUPERSEDED | ARCHIVED |

Todas as demais transições são proibidas.

`[Origem: ADR-CHM-001-014, R1-R6, Vigente — 14/14 transições]`

---

## 4.4 Terminalidade dos Estados

ARCHIVED constitui estado terminal. Após atingir ARCHIVED, nenhuma transição adicional é permitida.

REFUTED e SUPERSEDED constituem estados terminais operacionais. As únicas transições permitidas a partir desses estados são para ARCHIVED.

`[Origem: ADR-CHM-001-014, R7]`

---

## 4.5 Proibição de Regressão Epistêmica

São proibidas transições para estados anteriores da trajetória já percorrida.

Exemplos: DOMINANT → ACTIVE; ACTIVE → CANDIDATE; CANDIDATE → EMERGENT.

Resultado: ✗ Não permitido.

O conhecimento pode ser substituído, refutado ou arquivado, mas não regressa a estados epistêmicos anteriores.

`[Origem: ADR-CHM-001-014, R10]`

---

## 4.6 Elegibilidade para Transições

Uma transição permitida pelo Grafo Canônico não implica autorização automática para sua execução. As regras de elegibilidade permanecem aplicáveis.

Conforme ADR-CHM-001-008: *"Hipóteses Órfãs não poderão atingir os estados ACTIVE ou DOMINANT enquanto permanecerem sem fundamentação por Evidências Canônicas válidas."*

Esta regra permanece vigente e não é redefinida por este capítulo.

`[Origem: ADR-CHM-001-008, RN-3, Vigente]`

---

## 4.7 Elegibilidade de Revisão por Dependência

Quando uma hipótese referenciada por `depends_on_hypothesis_ids` transitar para REFUTED, SUPERSEDED ou ARCHIVED, as hipóteses dependentes tornam-se elegíveis para revisão.

A elegibilidade para revisão não constitui transição automática de estado. Nenhuma alteração epistêmica é propagada automaticamente.

`[Origem: ADR-CHM-001-012 (R5), ADR-CHM-001-015 (R1), Vigentes]`

---

## 4.8 Princípio da Não Cascata

Mudanças de estado não se propagam automaticamente para hipóteses relacionadas.

A transição de uma hipótese para REFUTED, SUPERSEDED ou ARCHIVED não produz automaticamente alteração de estado em hipóteses dependentes, concorrentes ou hierarquicamente relacionadas.

Toda hipótese mantém sua trajetória epistêmica própria.

`[Origem: ADR-CHM-001-012, R1-R4, Vigente — granularidade completa]`

---

## 4.9 Autoridade de Transição

Transições epistêmicas válidas podem ser executadas por produtores autorizados.

A autoridade operacional para executar uma transição não implica autoridade para redefinir estados canônicos, regras do grafo, critérios de elegibilidade ou princípios arquiteturais do CHM-001.

`[Origem: ADR-CHM-001-016, R1, R5]`

---

## 4.10 Contestação Retrospectiva

A Governança (papel de Analista, mesma convenção estabelecida por ADR-CHM-001-011/R7) pode contestar retrospectivamente a adequação de uma transição realizada.

A contestação retrospectiva: não invalida registros históricos já produzidos; não altera automaticamente estados históricos; não remove eventos previamente registrados.

Correções futuras deverão ocorrer por novos eventos válidos.

`[Origem: ADR-CHM-001-016, R3-R4, Vigente]`

---

## 4.11 Separação de Responsabilidades

Esta decisão preserva a separação entre Produção, Auditoria, Aprovação e Registro.

No contexto específico das transições epistêmicas individuais reguladas por este capítulo: Produção e Auditoria possuem atuação operacional direta; Aprovação e Registro permanecem responsabilidades arquiteturais externas à transição individual.

`[Origem: ADR-CHM-001-016, CE-5, Vigente — corrigido na Obs.CHM-38]`

---

## 4.12 Histórico de Transições

Toda transição epistêmica válida deverá gerar registro histórico correspondente.

Resultado: ✓ Obrigatório.

`[Origem: ADR-CHM-001-017, R1, Vigente]`

---

## 4.13 Monotonicidade do Histórico

O histórico de transições é append-only. Novos eventos podem ser adicionados. Eventos existentes não podem ser removidos, reordenados ou sobrescritos.

Correções posteriores deverão ocorrer exclusivamente por adição de novos registros.

`[Origem: ADR-CHM-001-017, R2-R4, Vigente]`

---

## 4.14 Preservação da Trajetória Epistêmica

O estado atual representa apenas a posição mais recente da trajetória epistêmica. Os estados anteriormente percorridos permanecem preservados. O estado atual não substitui o histórico.

`[Origem: ADR-CHM-001-017, R5, Vigente]`

---

## 4.15 Contestação e Histórico

Contestação retrospectiva realizada pela Governança (papel de Analista) não modifica registros históricos já produzidos.

Caso auditoria futura determine necessidade de correção operacional, a correção deverá ocorrer por novo evento histórico.

Resultado: ✓ Histórico preservado. ✓ Novo evento obrigatório.

`[Origem: ADR-CHM-001-017, R6-R7, Vigente]`

---

## 4.16 Independência entre Estado e Histórico

Versionamento e transições epistêmicas são dimensões independentes. Uma nova versão não implica nova transição. Uma transição não implica nova versão.

Os princípios de Monotonicidade Histórica definidos no Capítulo 3 permanecem integralmente vigentes.

`[Origem: ADR-CHM-001-013, ADR-CHM-001-017 (R8), Vigentes]`

---

## 4.17 Disponibilidade para Auditoria

O histórico de transições permanece disponível para auditoria mesmo quando a hipótese estiver REFUTED, SUPERSEDED ou ARCHIVED.

`[Origem: ADR-CHM-001-017, R9, Vigente — corrigido na Obs.CHM-39]`

---

## 4.18 CN-1 — Escopo do Histórico de Transições

Esta decisão registra exclusivamente transições de Estado Epistêmico definidas pela Máquina de Estados Epistêmicos.

Eventos de elegibilidade para revisão definidos pelos mecanismos de dependência não constituem transições de Estado Epistêmico e, portanto, não são registrados pelo mecanismo estabelecido neste capítulo.

A rastreabilidade desses eventos pode ser inferida a partir da correlação entre: histórico de transições da hipótese ancestral; relações definidas por `depends_on_hypothesis_ids`; regras de elegibilidade vigentes.

Caso futuras necessidades de Auditoria, Explainability ou Governança exijam rastreabilidade explícita de eventos de elegibilidade para revisão, esta decisão deverá ser revisada ou complementada por ADR específico.

`[Origem: ADR-CHM-001-017, CN-1, Vigente]`

---

## 4.19 Compatibilidades Normativas

Este capítulo:

- complementa ADR-CHM-001-014 (Grafo Canônico de Transições);
- complementa ADR-CHM-001-015 (Elegibilidade de Transições);
- complementa ADR-CHM-001-016 (Autoridade de Transição);
- complementa ADR-CHM-001-017 (Histórico de Transições);
- preserva integralmente ADR-CHM-001-002;
- preserva integralmente ADR-CHM-001-008;
- preserva integralmente ADR-CHM-001-011;
- preserva integralmente ADR-CHM-001-013.

Nenhuma regra previamente vigente é redefinida por este capítulo.

---

**Declaração de Consenso:** aprovado por Andraus (Decisor Final) em 12/07/2026, após parecer técnico CONFORME do Analista (3 rodadas de auditoria — Obs.CHM-38 [Crítica], Obs.CHM-39 [Menor], Obs.CHM-40 [Crítica], Obs.CHM-41 [Menor], todas resolvidas nesta versão consolidada).
