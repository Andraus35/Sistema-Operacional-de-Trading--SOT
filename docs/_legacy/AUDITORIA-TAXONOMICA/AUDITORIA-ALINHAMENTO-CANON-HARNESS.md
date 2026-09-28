# Auditoria de alinhamento do cânone ao Harness Cognitivo

**Data:** 2026-09-25  
**Escopo:** diretório [`canon/`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon), confrontado com [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md), [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md) e os três anexos do diretório `INQUÉRITO SOT`.  
**Natureza:** relatório local de achados e sugestões. Não é baseline, não é Spec, não fecha decisões abertas e não altera a autoridade dos documentos homologados.

## 1. Conclusão executiva

O cânone contém material valioso, mas foi formado em camadas de maturidade diferentes. Parte dele ainda descreve um produto/software de trading; a baseline atual descreve um **harness cognitivo de agentes**, operado por especificações, gates, evidências, hipóteses e homologação humana.

O principal risco não é um termo isolado. É a possibilidade de um agente ler, como se fossem equivalentes:

- arquitetura de runtime e workflow de especificação;
- agente, engine, scheduler, orquestrador e repositório de estado;
- score operacional e Conviction Vector;
- estado operacional de um agente e estado epistêmico de uma hipótese;
- TMP interno e Signal Package de fronteira;
- referência histórica/proposta e componente homologado.

**Recomendação geral:** preservar os documentos como histórico auditável, mas introduzir uma camada explícita de classificação e vocabulário controlado antes de qualquer nova expansão do cânone. A correção deve ser feita por emendas rastreáveis, não por substituição silenciosa de termos.

## 2. Autoridade usada para a leitura

Quando houve conflito, foi aplicada esta ordem:

1. decisão humana homologada e emenda homologada;
2. Constituição, Rules e Catálogo Oficial;
3. [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md) e [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md);
4. modelos canônicos baselined;
5. Specs homologadas;
6. referência, proposta, avaliação e legado.

O relatório não trata uma ocorrência num documento antigo como autorização arquitetural.

## 3. Achados dentro de `canon/`

### CAN-001 — O próprio cânone mistura maturidades de autoridade

**Severidade:** CRITICAL  
**Evidência:**

- [`CEM-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/CEM-001-canonical-evidence-model.md) declara “Candidato a baseline oficial”, mas o baseline operacional trata CEM-001 como baselined.
- [`SAS-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/SAS-001-structural-agent-spec.md) alterna “consolidado”, “Candidato a congelamento” e referências a contratos futuros.
- [`GMC-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/GMC-001-governance-canonical-models.md) registra estados de governança que não estão uniformemente refletidos nos cabeçalhos.

**Risco:** um agente não consegue saber se deve construir sobre o documento, revisá-lo ou tratá-lo como proposta.

**Sugestão:** criar um bloco obrigatório e uniforme de `Status de autoridade` em todos os canônicos, distinguindo pelo menos `DRAFT`, `CANDIDATE`, `HOMOLOGATED`, `BASELINED`, `SUPERSEDED` e `LEGACY`. O status do cabeçalho deve apontar para o registro de autoridade, não apenas para uma descrição narrativa.

### CAN-002 — `Structural Agent` permanece como nome principal, enquanto a taxonomia operacional migrou para especialista de domínio

**Severidade:** HIGH  
**Evidência:**

- [`SAS-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/SAS-001-structural-agent-spec.md) usa `Structural Agent` como nome oficial.
- O glossário/baseline atual usa a equivalência operacional `Structural Agent = Elliott Specialist`, mas essa equivalência não é propagada de modo uniforme no cânone.
- [`CEM-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/CEM-001-canonical-evidence-model.md) lista `Structural Agent`, `Institutional Agent`, `Macro Agent`, `Sentiment Agent`, `Risk Agent` e `Context Agent` como produtores, uma taxonomia mais ampla e anterior à sequência canônica atual.

**Risco:** “Structural” pode ser interpretado como camada arquitetural, agente, domínio Elliott ou agregador de Fibonacci/Fractal.

**Sugestão:** separar explicitamente:

- `AGENT`: especialista cognitivo;
- `DOMAIN`: Elliott, Fibonacci, Fractal, SMC, ICT;
- `ARCHITECTURAL ROLE`: produtor/consumidor/coordenador;
- `LEGACY ALIAS`: nome histórico.

Não apagar o nome histórico do CEM/SAS; marcar a equivalência autorizada e a data de vigência.

### CAN-003 — CEM-001 autoriza consumidores que não estão posicionados no runtime atual

**Severidade:** HIGH  
**Evidência:** [`CEM-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/CEM-001-canonical-evidence-model.md) lista `Hypothesis Engine`, `Conviction Engine` e `Decision Orchestrator` como consumidores.

`Decision Orchestrator` aparece como consumidor autorizado, enquanto o roadmap atual separa `Fusion → Conviction → Synthesis` e trata o Synthesis como árbitro/saída da decisão.

**Risco:** uma nova Spec pode recriar um componente antigo por interpretar “consumidor autorizado” como “componente runtime obrigatório”.

**Sugestão:** adicionar ao CEM uma distinção entre:

- consumidor conceitualmente compatível com o modelo;
- consumidor presente no runtime autorizado;
- consumidor futuro;
- nome legado absorvido por outro componente.

Como o CEM é modelo canônico, não remover a relação sem uma emenda de sucessão e compatibilidade.

### CAN-004 — `Fusion Engine`, `Evidence Fusion Engine` e `Conviction Engine` precisam de glossário normativo

**Severidade:** HIGH  
**Evidência:** o CEM autoriza `Fusion Engine` como produtor de evidência derivada; o roadmap usa também `Evidence Fusion Engine` e `Conviction Engine`; o baseline afirma que a Conviction é separada da Synthesis.

**Risco:** fusion pode ser implementada como cálculo de convicção, ou Conviction pode ser absorvida na Synthesis, contrariando B-001/Q-007.

**Sugestão de separação mínima:**

| Termo | Tipo | Responsabilidade |
|---|---|---|
| Fusion Engine | ENGINE | combinar evidências autorizadas e produzir evidência derivada |
| Evidence Fusion Engine | ALIAS CONTROLADO | nome expandido de Fusion Engine, se essa for a decisão homologada |
| Conviction Engine | ENGINE | calcular/avaliar o Conviction Vector e seus gates |
| Synthesis Agent | AGENT | integrar resultados, arbitrar hipóteses e produzir o artefato autorizado |

Se `Evidence Fusion Engine` não for apenas alias, a diferença precisa ser uma decisão humana explícita.

### CAN-005 — SDD-001 contém resíduo normativo de `Conviction Vector 4D`

**Severidade:** CRITICAL  
**Evidência:** [`SDD-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/SDD-001-spec-driven-development.md) mantém no checklist constitucional a referência ao modelo “4D”, enquanto a baseline atual fixa Conviction Vector de 8 dimensões.

**Risco:** o documento de governança pode gerar Specs estruturalmente incompatíveis com a decisão Q-008.

**Sugestão:** em uma emenda, substituir a referência operacional por `Conviction Vector 8D`, preservando no histórico a indicação de que a formulação 4D é obsoleta. Também pesquisar a mesma cadeia em RAG, schemas, specs e documentos de primeira geração.

### CAN-006 — CEE-001 usa a hierarquia atual, mas conserva moldura e vocabulário de 3E/software

**Severidade:** HIGH  
**Evidência:** [`CEE-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/CEE-001-cognitive-economy-efficiency-v2.0.md):

- o sumário ainda chama a seção de “Framework 3E”;
- a redação explica a extensão para 4Es;
- a tabela de roteamento usa `Master Orchestrator`;
- a economia é descrita em termos de chamadas de API, tokens e classes de modelo;
- o documento referencia `Mission Engine` e `Cognitive Scheduler`.

**Risco:** o agente entende economia como otimização de um software em execução, em vez de governança de custo/qualidade do harness.

**Sugestão:** reclassificar a redação em três camadas:

1. princípios normativos do harness;
2. mecanismos de runtime ainda não homologados;
3. exemplos históricos de implementação.

O título e as referências a 3E devem ser marcados como histórico, e os nomes de runtime devem receber status explícito (`homologado`, `planejado`, `legado` ou `não resolvido`).

### CAN-007 — PPQ-001 trata `Master Orchestrator` e `Mission Engine` como resolvidos sem autoridade equivalente no baseline atual

**Severidade:** HIGH  
**Evidência:** [`PPQ-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/PPQ-001-project-process-quality.md) afirma que a integração está “resolvida — Master Orchestrator” e mapeia uma camada operacional para “Mission Engine”.

**Risco:** transforma uma proposta de arquitetura de produto em fato canônico do harness, além de conflitar com a separação entre especificação, revisão, homologação e runtime futuro.

**Sugestão:** substituir futuramente a afirmação de “resolvido” por uma classificação de maturidade e por um link para a Spec que autoriza o componente. Até existir essa Spec, tratar os termos como `REFERENCE/LEGACY` ou `UNRESOLVED`, não como componente canônico.

### CAN-008 — SAS-001 mistura hipótese, evidência e contrato futuro

**Severidade:** HIGH  
**Evidência:** [`SAS-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/SAS-001-structural-agent-spec.md) descreve produção de hipóteses, mas contém correções que tornam o contrato de hipótese “agnóstico” e remetem a um CHM futuro, embora o CHM-001 já esteja baselined no estado atual.

**Risco:** o agente pode concluir que o SAS pode definir livremente a estrutura da hipótese ou que o CHM ainda não é vinculante.

**Sugestão:** emenda de compatibilidade: declarar que SAS-001 consome e produz objetos conformes ao CHM-001 vigente; a especificação do agente só pode definir comportamento e evidências do domínio. Correções históricas devem permanecer em histórico, não no corpo normativo ativo.

### CAN-009 — Fractal e Fibonacci aparecem como domínio, dimensão e etapa, mas não como categoria uniforme

**Severidade:** HIGH  
**Evidência:**

- [`SAS-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/SAS-001-structural-agent-spec.md) inclui Fibonacci e Fractal no escopo estrutural.
- [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md) lista Elliott, Fibonacci, Fractal, SMC e ICT na matriz de complexidade.
- Os anexos apontam que o fluxo principal e os schemas nem sempre têm entradas independentes para Fractal/Fibonacci.

**Risco:** um agente não sabe se Fractal/Fibonacci são agentes, engines, skills, subfunções ou dimensões do vetor.

**Sugestão:** publicar uma matriz de classificação, sem decidir silenciosamente a arquitetura:

| Objeto | Pergunta a fechar |
|---|---|
| Fibonacci | especialista independente, skill do Structural Agent ou evidência auxiliar? |
| Fractal | componente operacional atual ou etapa futura? |
| Dimensão fractal | saída própria ou dimensão calculada por outro componente? |

Até a decisão, usar `UNRESOLVED` em vez de inventar uma camada.

### CAN-010 — SDD-001 e PPQ-001 ainda descrevem um workflow de software, enquanto o método vigente é spec-first de harness

**Severidade:** HIGH  
**Evidência:**

- [`SDD-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/SDD-001-spec-driven-development.md) deriva de Spec Kit e fala em implementação/Plan/Tasks como sequência de produto.
- [`PPQ-001`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/canon/PPQ-001-project-process-quality.md) usa Sandbox, Backtest, Forward Test, Produção e Learning Agent.
- [`ROADMAP.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ROADMAP.md) estabelece Especificador → Revisor → Andraus → próxima Spec, com BUILD/VERIFY de código adiados.
- [`ATOMIC-SPEC.md`](C:/Users/André/Desktop/SOT%20ENGINER/SOT-Harness/ATOMIC-SPEC.md) formaliza BASpec, D0–D9, Enforcement Contract e gates L1–L4.

**Risco:** o workflow de implementação é iniciado antes da homologação da Spec, ou uma avaliação de código é confundida com verificação do harness.

**Sugestão:** manter SDD/PPQ como referências históricas/operacionais, mas inserir em cada um um “adaptador de workflow” que declare:

`documentar → especificar → revisar → homologar → autorizar → só então implementar/avaliar runtime`.

O vocabulário `BUILD` e `VERIFY` deve ser rotulado como futuro quando se referir a código.

## 4. Matriz consolidada de termos

| Termo | Classificação provisória | Situação de alinhamento |
|---|---|---|
| Structural Agent | AGENT / LEGACY ALIAS | preservar, mas mapear para o nome operacional vigente |
| Elliott Specialist | AGENT | nome operacional preferível, sujeito ao glossário |
| Institutional Agent | AGENT / LEGACY ALIAS | não tratar automaticamente como SMC Specialist sem referência de autoridade |
| Execution Agent | AGENT / LEGACY ALIAS | não tratar automaticamente como ICT Specialist sem referência de autoridade |
| Fusion Engine | ENGINE | produtor de evidência derivada no CEM |
| Evidence Fusion Engine | UNRESOLVED ou alias | decisão lexical ainda precisa ser explicitada |
| Conviction Engine | ENGINE | separado de Synthesis; trabalha sobre Conviction Vector |
| Synthesis Agent | AGENT | integra/arbitra conforme Spec autorizada; não executar ordens |
| Decision Orchestrator | LEGACY/UNRESOLVED | aparece no CEM, mas sem posicionamento runtime atual |
| Master Orchestrator | LEGACY/UNRESOLVED | presente em PPQ/CEE, não deve ser assumido canônico |
| Cognitive Orchestrator | UNRESOLVED/FUTURE | não promover sem Spec/decisão |
| Mission Engine | LEGACY/UNRESOLVED | separar missão de pesquisa, decisão e operação |
| Cognitive Scheduler | REFERENCE/FUTURE | não confundir com workflow de homologação |
| Event Bus | EVENT_BUS | transporte de eventos; não é repositório de estado |
| Blackboard | STATE_REPOSITORY | estado/publicações conforme protocolo; não é orquestrador |
| Hypothesis | MODEL | conforme CHM-001 |
| Evidence | MODEL | conforme CEM-001 |
| TMP | ARTIFACT | handoff interno; não é fronteira externa |
| Signal Package | ARTIFACT | fronteira para downstream; SOT não executa ordem |
| Risk Agent | FUTURE/UNRESOLVED | fora do runtime atual até especificação própria |
| Bot Trade Finance | INTEGRATION | consumidor downstream; não é agente do SOT |

## 5. Decisões que devem permanecer abertas

Os anexos formulam perguntas úteis, mas elas não devem ser respondidas por inferência documental:

1. `Master Orchestrator` e `Cognitive Orchestrator` são o mesmo componente?
2. `Decision Orchestrator` é um componente, uma função absorvida ou apenas um consumidor conceitual do CEM?
3. `Mission Engine` é missão de investigação, decisão, operação ou legado de runtime?
4. `Cognitive Scheduler` é componente independente ou apenas mecanismo futuro de ativação?
5. `Evidence Fusion Engine` é alias de `Fusion Engine`?
6. Fibonacci e Fractal são agentes, skills, subfunções ou etapas ainda não operacionalizadas?
7. O score 0–9 é filtro independente, derivação do vetor ou resíduo legado?
8. Qual documento deve ser o sucessor normativo dos canônicos com status “candidato”?

Cada pergunta deve virar decisão rastreável, com impacto, autoridade, artefatos afetados e data de vigência. Até lá, o termo deve ser marcado como `UNRESOLVED`, nunca usado como invariante.

## 6. Ordem sugerida de alinhamento futuro

1. **Governança de status:** uniformizar cabeçalhos e Catálogo Oficial.
2. **Vocabulário controlado:** publicar tabela de termos, aliases, sucessores e termos proibidos.
3. **Fronteiras de responsabilidade:** distinguir Agent, Engine, Scheduler, Event Bus, Blackboard, Artifact e Integration.
4. **Pipeline cognitivo:** fixar, por Spec, `Evidence → Hypothesis → Fusion → Conviction → Synthesis → TMP/Signal Package`.
5. **Workflow do harness:** separar explicitamente spec-time, homologação e runtime futuro.
6. **Compatibilidade:** emendar CEM/SDD/SAS/CEE/PPQ sem apagar histórico.
7. **Auditoria automatizada:** criar uma verificação de vocabulário/status contra aliases antigos e contra a lista de decisões abertas.

## 7. Regra de segurança documental

Até que as emendas sejam homologadas:

- documentos legados continuam úteis como evidência histórica, não como autoridade;
- propostas não são componentes;
- “documentado” não significa “homologado”;
- um nome encontrado em um canônico não prova que o componente pertence ao runtime atual;
- nenhuma correção deve apagar texto histórico sem preservar sucessão e rastreabilidade;
- o relatório não deve ser usado como fonte normativa para criar Specs.

**Resultado:** o cânone pode ser alinhado ao harness cognitivo sem reescrita destrutiva. A estratégia correta é classificar, declarar sucessão, separar spec-time de runtime e submeter as ambiguidades arquiteturais à decisão humana antes de consolidar novos invariantes.
