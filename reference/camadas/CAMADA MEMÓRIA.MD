# MC-EXP-001 — MASTER CONTRACT DA CAMADA DE EXPERIÊNCIA E MEMÓRIA

**Sistema:** SOT — System of Thought  
**Camada:** Experiência e Memória  
**Identificador:** MC-EXP-001  
**Versão:** 1.0  
**Status:** BASELINE  
**Natureza:** Master Contract de Arquitetura, Especificação e Harness  
**Aplicabilidade:** Geral — não restrito a Trading  
**Dependências conceituais:** RAG, Cognição, Learning, Governance, Skills  
**Princípio estrutural:** Memória preserva experiência. Cognição interpreta. Learning procura extrair melhoria. Governança decide o que pode evoluir.

---

# 1. PROPÓSITO

A Camada de Experiência e Memória define a capacidade do sistema de preservar, organizar, contextualizar, recuperar e utilizar experiências passadas sem transformar automaticamente experiências particulares em conhecimento universal, regras ou decisões.

A camada deve permitir que um agente utilize o passado como fonte de contexto sem confundir:

- experiência com conhecimento
- resultado com causalidade
- repetição com evidência independente
- correlação histórica com regra
- interpretação posterior com fato histórico
- memória com verdade
- sucesso com validade universal
- falha com impossibilidade futura

A camada deve preservar a história do sistema e permitir sua utilização cognitiva posterior.

---

# 2. MISSÃO

A missão da camada é:

> Preservar experiências relevantes ao longo do tempo, mantendo contexto, proveniência, temporalidade, resultados, erros, sucessos e interpretações sem corromper o registro histórico, permitindo sua recuperação contextualizada pela Cognição e sua utilização controlada pelo Learning.

A camada deve responder:

1. O que aconteceu?
2. Em que contexto aconteceu?
3. O que foi observado?
4. Qual foi o resultado?
5. Quais erros ocorreram?
6. Quais condições estavam presentes?
7. O que posteriormente foi interpretado?
8. O que permanece apenas como experiência?
9. O que pode ser transformado em candidato a aprendizado?
10. Como recuperar experiências semelhantes, contrastantes ou temporalmente relevantes?
11. Como impedir que a memória seja contaminada?
12. Como preservar a história mesmo quando sua interpretação muda?

---

# 3. NÃO OBJETIVOS

A Camada de Experiência e Memória NÃO deve assumir:

- função de RAG
- autoridade semântica do Knowledge Graph
- função de raciocínio
- função de Learning
- autoridade decisional
- autoridade de Governança
- generalização automática de experiências
- transformação automática de experiência em regra
- substituição da base de conhecimento
- alteração silenciosa do histórico
- fabricação de evidência
- eliminação de experiências desfavoráveis
- seleção manipulativa de experiências
- definição automática de estratégia

A memória deve preservar e disponibilizar experiência.

Ela não deve decidir o que o sistema deve acreditar.

---

# 4. PRINCÍPIO CENTRAL

## Memória preserva experiência. Cognição interpreta. Learning procura extrair melhoria. Governança decide o que pode evoluir.

Essa separação é estrutural.

Uma experiência pode ser:

- registrada
- recuperada
- comparada
- interpretada
- questionada
- utilizada como evidência contextual
- utilizada como fonte para uma hipótese de aprendizagem

sem necessariamente se tornar:

- conhecimento
- regra
- procedimento
- estratégia
- verdade
- política
- decisão.

---

# 5. PRINCÍPIOS DA CAMADA

## EXP-P01 — Preservação do episódio

Experiências relevantes devem ser preservadas como episódios identificáveis.

---

## EXP-P02 — Contexto obrigatório

Uma experiência não deve ser interpretada isoladamente quando seu significado depender de contexto.

---

## EXP-P03 — Experiência não é conhecimento

O fato de algo ter acontecido não implica que exista uma regra geral.

---

## EXP-P04 — Resultado não é causalidade

Um resultado observado não demonstra automaticamente que determinada ação ou condição causou o resultado.

---

## EXP-P05 — Temporalidade

Toda experiência deve possuir referência temporal suficiente para permitir interpretação histórica.

---

## EXP-P06 — Proveniência

A origem dos dados que constituem uma experiência deve ser rastreável.

---

## EXP-P07 — Registro separado de interpretação

O registro original da experiência deve permanecer distinguível das interpretações produzidas posteriormente.

---

## EXP-P08 — Preservação dos erros

Falhas relevantes devem ser preservadas.

O sistema não deve construir uma memória artificialmente otimista.

---

## EXP-P09 — Preservação dos sucessos

Sucessos também devem ser preservados juntamente com as condições em que ocorreram.

---

## EXP-P10 — Retenção proporcional

A retenção deve considerar valor histórico, operacional, analítico e de auditoria.

---

## EXP-P11 — Imutabilidade histórica

O registro do que efetivamente ocorreu não deve ser silenciosamente alterado por interpretações posteriores.

---

## EXP-P12 — Evolução em camadas

O histórico pode receber novas interpretações sem que o episódio original seja reescrito.

---

## EXP-P13 — Recuperação contextual

A experiência deve ser recuperada considerando sua relevância para o contexto atual.

---

## EXP-P14 — Feedback não reescreve história

Um feedback posterior pode alterar uma interpretação, mas não deve alterar retroativamente aquilo que foi registrado como ocorrido.

---

# 6. MODELO CONCEITUAL

```text
EVENTO
  ↓
REGISTRO
  ↓
EXPERIÊNCIA
  ↓
CONTEXTUALIZAÇÃO
  ↓
INDEXAÇÃO
  ↓
RETENÇÃO
  ↓
RECUPERAÇÃO
  ↓
COGNIÇÃO
  ↓
INTERPRETAÇÃO
  ↓
LEARNING
  ↓
CANDIDATO A LIÇÃO
  ↓
VALIDAÇÃO
  ↓
GOVERNANÇA
  ↓
EVOLUÇÃO CONTROLADA

7.2 Memória semântica derivada

Representa conhecimento contextualizado derivado de experiências.

Não deve substituir o Knowledge Graph canônico.

7.3 Memória procedural

Preserva experiências relacionadas à execução de procedimentos.

7.4 Memória estatística

Preserva padrões quantitativos observados ao longo de experiências.

Exemplo:

Condição X
→ 47 ocorrências
→ 31 resultados favoráveis
→ 16 desfavoráveis

Isso não significa automaticamente:

X causa resultado favorável.
7.5 Memória estratégica

Preserva histórico de estratégias, hipóteses e comportamentos estratégicos.

7.6 Working Memory

Mantém informações temporárias necessárias para uma tarefa corrente.

Working Memory não deve ser confundida com memória histórica permanente.

8. MODELO DE EXPERIÊNCIA

A unidade fundamental da camada é o Experience Record.

experience_id:
mission_id:
campaign_id:
hypothesis_id:

context:

knowledge_refs:

skills_used:

decision_trace:

execution_events:

outcome:

errors:

successes:

regime:

temporal_scope:

performance_metrics:

feedback:

lessons_candidate:

retention_policy:

provenance:

version:
9. IDENTIDADE DA EXPERIÊNCIA

Cada experiência deve possuir identidade única.

A identidade deve permitir:

localização
referência
versionamento
auditoria
associação
comparação
recuperação
prevenção de duplicidade.

Uma experiência não deve possuir múltiplas identidades apenas porque foi indexada de maneiras diferentes.

10. CONTEXTO DA EXPERIÊNCIA

O contexto deve representar as condições relevantes existentes durante o episódio.

Pode incluir:

objetivo
ambiente
regime
estado do sistema
hipótese vigente
conhecimento utilizado
skill utilizada
recursos disponíveis
restrições
estado decisional
estado operacional
condições externas.

O contexto não deve ser artificialmente expandido sem necessidade.

11. EVENTOS

Uma experiência pode ser composta por múltiplos eventos.

event_id:
experience_id:
timestamp:
event_type:
source:
observation:
action:
result:
provenance:

A sequência temporal dos eventos deve poder ser reconstruída quando necessário.

12. RESULTADO

O resultado representa o que efetivamente ocorreu após uma ação, hipótese, decisão ou experimento.

Deve ser separado de:

expectativa
interpretação
causalidade
avaliação.

Exemplo:

Expectativa:
Preço deveria continuar subindo.

Resultado:
Preço subiu 0,8% e posteriormente caiu 1,4%.

Interpretação:
A hipótese perdeu suporte.

Causalidade:
Não determinada.
13. ERROS

Erros devem ser registrados como parte legítima da memória.

Um erro pode estar relacionado a:

percepção
interpretação
hipótese
execução
procedimento
informação
contexto
recuperação
decisão
ferramenta
comunicação
governança.
14. SUCESSOS

Sucessos devem ser registrados juntamente com suas condições.

O sistema deve evitar:

Sucesso → regra.

O modelo correto é:

Sucesso
+
Contexto
+
Condições
+
Evidências
+
Repetição independente
→
Possível hipótese de padrão
15. DESEMPENHO

Quando uma experiência possuir resultado mensurável, métricas devem ser preservadas.

Exemplos:

resultado
erro
tempo
custo
precisão
retorno
drawdown
latência
taxa de acerto
taxa de falha
eficiência de recursos.

A métrica deve preservar sua definição e unidade.

16. REGIME

Quando relevante, uma experiência deve possuir representação do regime em que ocorreu.

Exemplos genéricos:

regime:
  type:
  state:
  confidence:
  evidence:

O regime não deve ser tratado como verdade apenas porque foi atribuído.

17. TRACE DE DECISÃO

Quando existir decisão associada, a experiência deve preservar a relação entre:

Contexto
→ Evidências
→ Hipóteses
→ Alternativas
→ Decisão
→ Resultado

Isso permite posteriormente analisar:

decisões corretas
decisões incorretas
decisões sob incerteza
decisões baseadas em evidência insuficiente
decisões que produziram resultados inesperados.
18. TRACE DE EXECUÇÃO

Quando houver execução, a memória deve preservar os eventos relevantes.

O objetivo não é apenas registrar:

resultado = X

mas permitir reconstruir:

o que foi feito
→ quando
→ em qual estado
→ com quais recursos
→ com qual resultado.
19. RECUPERAÇÃO DE EXPERIÊNCIA

A recuperação deve suportar diferentes modos.

19.1 Similaridade

Recuperar experiências semelhantes.

19.2 Contraste

Recuperar experiências em que condições semelhantes produziram resultados diferentes.

19.3 Temporalidade

Recuperar experiências:

recentes
históricas
anteriores a determinado evento
posteriores a determinada mudança
pertencentes a determinado período.
19.4 Regime

Recuperar experiências ocorridas em condições de regime semelhantes.

19.5 Contexto

Recuperar experiências relevantes ao contexto atual.

20. EXPERIENCE PACKET

A memória deve poder entregar à Cognição um pacote contextualizado.

experience_packet_id:

objective:

query:

current_context:

similar_experiences:

contrasting_experiences:

temporal_experiences:

regime_matched_experiences:

relevant_failures:

relevant_successes:

outcomes:

performance:

conflicts:

limitations:

selection_rationale:

retrieval_trace:

version:

O Experience Packet não é uma conclusão.

É material contextual para Cognição.

21. EXPERIÊNCIA SEMELHANTE NÃO É EVIDÊNCIA INDEPENDENTE

Quando múltiplos registros representarem essencialmente o mesmo episódio, eles não devem ser tratados como múltiplas confirmações independentes.

Exemplo:

1 evento
→ 5 registros derivados

não deve ser interpretado como:

5 eventos independentes.
22. EXPERIÊNCIA CONTRASTANTE

A recuperação deve procurar não apenas experiências que confirmem uma hipótese.

Deve ser possível recuperar:

Experiências favoráveis
+
Experiências desfavoráveis
+
Experiências inconclusivas

Essa propriedade reduz risco de memória seletiva.

23. RETENÇÃO

Cada experiência deve possuir política de retenção.

A política pode considerar:

valor operacional
valor histórico
valor de auditoria
valor de aprendizagem
custo
frequência de acesso
criticidade
redundância
idade.
24. DECAIMENTO

O valor operacional de uma experiência pode diminuir com o tempo.

Entretanto:

valor operacional menor
≠
valor histórico menor.

Experiências antigas podem continuar relevantes para:

auditoria
comparação
regime histórico
detecção de recorrência
análise de falhas.
25. EXPERIÊNCIA CRÍTICA

Experiências críticas devem receber proteção adicional.

Exemplos:

falhas graves
decisões de alto impacto
eventos raros
incidentes
experimentos fundamentais
mudanças de regime
eventos utilizados para justificar alterações sistêmicas.
26. ARQUIVAMENTO

Arquivamento deve retirar uma experiência do fluxo operacional sem destruí-la quando sua preservação for necessária.

ACTIVE
→ ARCHIVED

Arquivamento não significa:

DELETED
27. COMPRESSÃO DE MEMÓRIA

A memória pode ser comprimida para reduzir custo.

Porém, a compressão não deve eliminar informações críticas.

Deve preservar pelo menos, quando aplicável:

identidade
temporalidade
proveniência
contexto
resultado
erros
sucessos
conflitos
referências.
28. INTEGRIDADE HISTÓRICA

A memória deve distinguir:

EVENTO ORIGINAL

de:

INTERPRETAÇÃO POSTERIOR

Exemplo:

Registro original:
"Preço caiu 2%."

Interpretação posterior:
"A queda provavelmente ocorreu devido à condição X."

A segunda informação não pode substituir a primeira.

29. VERSIONAMENTO DA INTERPRETAÇÃO

Interpretações podem evoluir.

Exemplo:

Interpretação V1:
Hipótese A parecia explicar o evento.

Interpretação V2:
Novas evidências enfraqueceram A.

Interpretação V3:
Hipótese B passou a explicar melhor o conjunto.

As três versões devem permanecer rastreáveis quando relevantes.

30. CONFLITO DE MEMÓRIA

Quando experiências ou interpretações entrarem em conflito, o sistema deve preservar o conflito.

Não deve resolver automaticamente através da eliminação de uma das experiências.

O conflito pode representar:

contexto diferente
período diferente
regime diferente
dados incompatíveis
interpretação divergente
erro de registro.
31. CONTAMINAÇÃO DA MEMÓRIA

A camada deve detectar tentativas ou ocorrências de introdução de informação não pertencente ao episódio.

Possíveis formas:

fabricação retrospectiva
alteração silenciosa
associação incorreta
atribuição errada
mistura de episódios
inferência registrada como fato
memória externa apresentada como experiência própria.
32. EXPERIÊNCIA → CONHECIMENTO

A transformação deve seguir:

Experiência
→ Observação
→ Padrão candidato
→ Hipótese
→ Evidência adicional
→ Validação
→ Knowledge Candidate
→ Governança
→ Conhecimento publicado

Nunca:

Experiência
→ Regra automática
33. EXPERIENCE → LEARNING

A experiência pode produzir um:

Lesson Candidate
lesson_candidate_id:

experience_refs:

observation:

pattern:

hypothesis:

expected_effect:

evidence:

confidence:

validation_status:

O Lesson Candidate não é ainda aprendizado validado.

34. RELAÇÃO COM COGNIÇÃO

A Cognição recebe experiências contextualizadas.

Experience
↓
Experience Packet
↓
Cognition
↓
Interpretation
↓
Hypothesis

A memória não deve impor uma conclusão à Cognição.

35. RELAÇÃO COM RAG

O RAG pode recuperar experiências quando solicitado.

Porém:

RAG = capacidade de recuperação
Experience = conteúdo experiencial

RAG não deve alterar a autoridade semântica da experiência.

36. RELAÇÃO COM LEARNING

Learning utiliza experiências para:

identificar padrões
gerar hipóteses de melhoria
realizar experimentos
avaliar resultados
propor mudanças.

A memória fornece histórico.

Learning produz transformação controlada.

37. RELAÇÃO COM GOVERNANCE

Governança controla:

mudanças
promoção
validação
versionamento
retenção crítica
evolução
reversão.

Memória não possui autoridade de Governança.

38. ESPECIFICAÇÕES A SEREM DESENVOLVIDAS
Foundations
EXP-SPEC-001 — Experience Capability Contract

Definir contrato funcional da camada.

EXP-SPEC-002 — Experience Record Model

Definir estrutura formal do registro de experiência.

EXP-SPEC-003 — Event Model

Definir representação dos eventos.

EXP-SPEC-004 — Context Model

Definir representação contextual.

EXP-SPEC-005 — Experience Identity

Definir identidade e unicidade.

EXP-SPEC-006 — Experience Provenance

Definir rastreabilidade de origem.

EXP-SPEC-007 — Experience Temporal Model

Definir representação temporal.

39. RESULTADOS
EXP-SPEC-008 — Outcome Model

Definir representação de resultados.

EXP-SPEC-009 — Error Model

Definir representação de erros.

EXP-SPEC-010 — Success Model

Definir representação de sucessos.

EXP-SPEC-011 — Performance Metrics

Definir métricas de desempenho.

EXP-SPEC-012 — Regime Context

Definir representação de regimes.

EXP-SPEC-013 — Decision Trace

Definir rastreabilidade decisional.

EXP-SPEC-014 — Execution Trace

Definir rastreabilidade de execução.

40. RETRIEVAL
EXP-SPEC-015 — Experience Retrieval Contract

Definir contrato de recuperação.

EXP-SPEC-016 — Similar Experience Retrieval

Definir recuperação por similaridade.

EXP-SPEC-017 — Contrasting Experience Retrieval

Definir recuperação de experiências contrastantes.

EXP-SPEC-018 — Temporal Experience Retrieval

Definir recuperação temporal.

EXP-SPEC-019 — Regime-Aware Retrieval

Definir recuperação sensível a regime.

EXP-SPEC-020 — Experience Relevance

Definir relevância contextual.

EXP-SPEC-021 — Experience Independence

Definir independência entre experiências.

EXP-SPEC-022 — Experience Packet

Definir pacote entregue à Cognição.

41. RETENÇÃO E INTEGRIDADE
EXP-SPEC-023 — Retention Policy

Definir políticas de retenção.

EXP-SPEC-024 — Experience Value

Definir valor da experiência.

EXP-SPEC-025 — Experience Decay

Definir decaimento de valor.

EXP-SPEC-026 — Critical Experience Preservation

Definir proteção de experiências críticas.

EXP-SPEC-027 — Archival

Definir arquivamento.

EXP-SPEC-028 — Memory Compression

Definir compressão.

EXP-SPEC-029 — Memory Integrity

Definir integridade.

EXP-SPEC-030 — Historical Immutability

Definir imutabilidade histórica.

EXP-SPEC-031 — Versioned Interpretation

Definir evolução de interpretações.

EXP-SPEC-032 — Memory Conflict

Definir tratamento de conflitos.

EXP-SPEC-033 — Duplicate Detection

Definir detecção de duplicidade.

EXP-SPEC-034 — Memory Contamination

Definir detecção de contaminação.

42. INTEGRAÇÃO COM CONHECIMENTO
EXP-SPEC-035 — Experience-to-Knowledge Contract

Definir transformação controlada de experiência em conhecimento candidato.

EXP-SPEC-036 — Knowledge-to-Experience Mapping

Definir relação entre conhecimento utilizado e experiência resultante.

EXP-SPEC-037 — Hypothesis-to-Experience Mapping

Definir associação entre hipóteses e experiências.

43. INTEGRAÇÃO COM COGNIÇÃO
EXP-SPEC-038 — Experience-to-Cognition Contract

Definir contrato de entrega para Cognição.

EXP-SPEC-039 — Contextual Experience Presentation

Definir apresentação contextual.

EXP-SPEC-040 — Experience Counterevidence

Definir utilização de experiências como contraevidência.

44. INTEGRAÇÃO COM LEARNING
EXP-SPEC-041 — Experience-to-Learning Contract

Definir contrato com Learning.

EXP-SPEC-042 — Lesson Candidate

Definir estrutura formal de candidato a lição.

EXP-SPEC-043 — Learning Feedback

Definir retorno de Learning para a memória.

EXP-SPEC-044 — Experience-Based Experimentation

Definir utilização de experiências na formulação de experimentos.

45. MEMÓRIA ESTRATÉGICA
EXP-SPEC-045 — Strategy Experience

Definir memória de experiências estratégicas.

EXP-SPEC-046 — Strategy Performance History

Definir histórico de desempenho estratégico.

EXP-SPEC-047 — Regime Performance History

Definir desempenho histórico por regime.

EXP-SPEC-048 — Failure Pattern Memory

Definir memória de padrões de falha.

EXP-SPEC-049 — Success Pattern Memory

Definir memória de padrões de sucesso.

46. HARNESS E EVOLUÇÃO
EXP-SPEC-050 — Experience Harness

Definir Harness da camada.

EXP-SPEC-051 — Experience Benchmark Suite

Definir conjunto de benchmarks.

EXP-SPEC-052 — Experience Economicity Benchmark

Definir avaliação de economicidade.

EXP-SPEC-053 — Memory Versioning

Definir versionamento da memória.

47. HARNESS DA CAMADA

O Harness deve avaliar propriedades observáveis da memória sem impor uma única implementação tecnológica.

A arquitetura deve permanecer tecnologicamente neutra.

48. SENSORES DETERMINÍSTICOS

O Harness deve verificar:

Integridade
campos obrigatórios
tipos
referências
identificadores.
Identidade
unicidade
consistência de IDs
referências cruzadas.
Temporalidade
timestamps
ordenação
intervalos
consistência temporal.
Proveniência
origem
rastreabilidade
referência ao evento original.
Duplicidade
registros duplicados
episódios derivados
falsa independência.
Versionamento
versões
histórico
alterações.
Retenção
política aplicável
preservação crítica
arquivamento.
Estrutura
conformidade com schema
integridade referencial.
49. SENSORES INFERENCIAIS

O Harness deve avaliar:

relevância contextual
qualidade da recuperação
similaridade contextual
qualidade de contraste
qualidade da interpretação
preservação do contexto
distinção entre episódio e regra
qualidade de Lesson Candidate
risco de generalização indevida
risco de memória seletiva.
50. TESTES DO HARNESS

O Harness deve incluir, quando aplicável:

Teste de recuperação

A experiência correta deve ser recuperável.

Teste de integridade histórica

A experiência original deve permanecer preservada.

Teste de duplicidade

Registros derivados não devem produzir falsa independência.

Teste de contaminação

Informação externa ou inventada não deve ser registrada como experiência.

Teste temporal

Experiências devem respeitar sua posição temporal.

Teste de contraste

O sistema deve conseguir recuperar experiências divergentes quando relevantes.

Teste de retenção

Experiências críticas não devem desaparecer indevidamente.

Teste de compressão

A compressão não deve eliminar informação crítica.

Teste de regressão

Alterações no sistema de memória não devem degradar capacidades anteriormente válidas.

Teste adversarial

O sistema deve resistir a memória fabricada, manipulada ou contraditória.

51. INVARIANTES
I-EXP-01

Uma experiência registrada não pode ser silenciosamente reescrita.

I-EXP-02

Experiência não pode se transformar automaticamente em conhecimento.

I-EXP-03

Resultado observado não pode ser tratado automaticamente como causalidade.

I-EXP-04

Experiência relevante deve preservar contexto suficiente para interpretação.

I-EXP-05

Erros relevantes devem permanecer recuperáveis.

I-EXP-06

Sucessos relevantes devem preservar as condições em que ocorreram.

I-EXP-07

Uma interpretação posterior não pode alterar o histórico original.

I-EXP-08

Experiências duplicadas não podem gerar falsa independência estatística.

I-EXP-09

Memória não possui autoridade decisional.

I-EXP-10

Experiência utilizada para Learning deve permanecer rastreável.

I-EXP-11

Compressão não pode eliminar informação crítica.

I-EXP-12

Retenção não pode remover silenciosamente experiências necessárias para auditoria.

52. QUALITY GATES
G0 — Memory Contract

O contrato da camada está definido.

G1 — Record Integrity

Os registros são estruturalmente íntegros.

G2 — Historical Integrity

O histórico é preservado.

G3 — Retrieval Integrity

As experiências relevantes podem ser recuperadas.

G4 — Interpretation Integrity

Interpretação não é confundida com histórico.

G5 — Learning Integrity

Experiência não é transformada automaticamente em aprendizado.

G6 — Retention Integrity

A política de retenção preserva experiências críticas.

G7 — Harness Integrity

O Harness cobre os riscos relevantes.

G8 — Regression Integrity

Alterações não degradam capacidades anteriormente validadas.

53. MÉTRICAS

A camada deve poder medir:

Record Integrity Rate
Provenance Coverage
Historical Mutation Rate
Duplicate Rate
Contamination Rate
Experience Recall
Contextual Relevance
Temporal Accuracy
Regime Match Rate
Contrasting Experience Coverage
Experience Utility
Learning Contribution
Decision Context Contribution
Error Recurrence Reduction
Retention Efficiency
Critical Experience Preservation
Compression Loss
Retrieval Latency
Storage Cost
Lesson Candidate Precision
Lesson Validation Rate
Repeated Failure Rate
Repeated Success Rate
Learning Feedback Quality.
54. FAILURE TAXONOMY

A camada deve reconhecer pelo menos:

Record Failure

Registro incompleto ou incorreto.

Context Loss

Perda de contexto relevante.

Provenance Failure

Origem não rastreável.

Historical Mutation

Alteração indevida do histórico.

Duplicate Memory

Duplicação de uma mesma experiência.

Memory Contamination

Introdução de informação que não pertence à experiência.

Retrieval Failure

Experiência relevante não recuperada.

Temporal Failure

Interpretação temporal incorreta.

Regime Misclassification

Classificação contextual inadequada.

Interpretation Drift

Mudança de interpretação sem rastreabilidade.

False Generalization

Experiência particular transformada indevidamente em regra geral.

Retention Failure

Perda indevida de memória.

Compression Loss

Perda de informação crítica durante compressão.

Experience Conflict

Experiências conflitantes.

Learning Attribution Failure

Atribuição incorreta de melhoria a uma experiência.

Experience-to-Knowledge Failure

Transformação indevida em conhecimento.

Feedback Failure

Feedback incorreto ou não rastreável.

Regression

Alteração que degrada uma capacidade previamente validada.

55. OBSERVABILIDADE

A observabilidade deve permitir acompanhar:

EVENTO
↓
EXPERIENCE RECORD
↓
CONTEXT
↓
OUTCOME
↓
INTERPRETATION
↓
RETRIEVAL
↓
CONSUMER
↓
FEEDBACK
↓
LESSON CANDIDATE

Cada transição relevante deve ser rastreável.

56. BENCHMARK SUITE

Os benchmarks devem testar pelo menos:

Recuperação do episódio correto.
Recuperação de experiências semelhantes.
Recuperação de experiências contrastantes.
Recuperação temporal.
Preservação contextual.
Preservação de erros.
Preservação de sucessos.
Detecção de duplicidade.
Detecção de contaminação.
Separação entre experiência e conhecimento.
Separação entre episódio e regra.
Integridade após compressão.
Integridade após arquivamento.
Evolução das interpretações.
Conflitos entre experiências.
Recuperação sob diferentes regimes.
Utilização da memória pela Cognição.
Utilização da memória pelo Learning.
57. ECONOMICIDADE

A camada deve ser avaliada não apenas pela capacidade de armazenar experiências, mas pelo valor obtido por recurso consumido.

Métrica conceitual:

Experience Utility
/
Memory Cost

O custo pode considerar:

armazenamento
processamento
indexação
recuperação
contexto consumido
latência
manutenção
avaliação.

O objetivo não é maximizar memória.

É maximizar:

valor cognitivo e operacional recuperado por unidade de recurso.

58. VERSIONAMENTO

Toda alteração estrutural relevante deve possuir registro.

Modelo:

version:

baseline:

change:

reason:

expected_effect:

integrity_tests:

regressions:

decision:
59. CICLO DE VIDA
EXPERIENCE
    ↓
RECORD
    ↓
VALIDATE
    ↓
STORE
    ↓
INDEX
    ↓
RETRIEVE
    ↓
INTERPRET
    ↓
LESSON CANDIDATE
    ↓
EXPERIMENT
    ↓
VALIDATE
    ↓
LEARNING
    ↓
GOVERNANCE
    ↓
EVOLUTION
60. CONDIÇÕES DE PRONTIDÃO

A camada somente deve ser considerada pronta quando for capaz de:

registrar episódios
preservar contexto
registrar resultados
preservar erros
preservar sucessos
preservar proveniência
preservar temporalidade
recuperar experiências semelhantes
recuperar experiências contrastantes
recuperar experiências temporais
recuperar experiências por regime
distinguir experiência de conhecimento
distinguir experiência de regra
preservar histórico
detectar duplicidade
detectar contaminação
produzir Lesson Candidates
integrar-se à Cognição
integrar-se ao Learning
integrar-se ao RAG
integrar-se ao Knowledge Layer
aplicar retenção
executar Harness
medir desempenho
medir economicidade
executar regressão.
61. CRITÉRIO FINAL DA CAMADA

A Camada de Experiência e Memória deve permitir que o sistema:

aprenda com o passado sem reescrever o passado, utilize experiências sem transformá-las automaticamente em verdades e preserve contexto suficiente para que a Cognição possa reinterpretar o histórico de maneira rastreável.

62. RELAÇÃO COM AS DEMAIS CAMADAS
                         ┌───────────────────┐
                         │    GOVERNANCE     │
                         └─────────┬─────────┘
                                   │
                                   ▼
┌────────────┐             ┌───────────────────┐
│    RAG     │◄───────────►│    EXPERIENCE     │
└─────┬──────┘             │    & MEMORY       │
      │                    └─────────┬─────────┘
      │                              │
      ▼                              ▼
┌────────────┐               ┌───────────────────┐
│ KNOWLEDGE  │               │    COGNITION      │
└────────────┘               └─────────┬─────────┘
                                       │
                                       ▼
                               ┌───────────────────┐
                               │     LEARNING      │
                               └─────────┬─────────┘
                                         │
                                         ▼
                                  CONTROLLED
                                   EVOLUTION

A experiência funciona como ponte temporal entre o que o sistema já vivenciou e o que ele está tentando compreender, aprender ou melhorar.

63. BASELINE

MC-EXP-001 — Master Contract da Camada de Experiência e Memória

Status: BASELINE PROPOSTA

Regra de evolução:

Nenhuma alteração estrutural deve ser incorporada à camada sem:

Especificação
→ Harness
→ Teste
→ Evidência
→ Avaliação
→ Versionamento
→ Governança

Fim do Master Contract.