# MC-SKL-001
# MASTER CONTRACT — CAMADA DE SKILLS

Status: MASTER SPECIFICATION
Versão: 1.0
Camada: SKL — Skills
Escopo: Global
Natureza: Especificação de capacidade e governança
Princípio de projeto: Liberdade cognitiva + especialização delimitada + invariantes verificáveis


# 1. PROPÓSITO

Definir a arquitetura conceitual, comportamental, operacional e de Harness da Camada de Skills.

A camada SKL representa competências especializadas que podem ser acionadas por agentes ou processos cognitivos para executar tarefas dentro de um domínio, método, disciplina ou capacidade delimitada.

Uma Skill não é simplesmente um prompt, documento, conjunto de regras ou banco de conhecimento.

Uma Skill é uma unidade de competência especializada capaz de:

- interpretar uma tarefa dentro de seu domínio
- identificar conhecimento necessário
- solicitar conhecimento ao RAG
- aplicar modelos, métodos e procedimentos especializados
- formular hipóteses
- produzir análises especializadas
- identificar evidências relevantes
- representar incertezas
- detectar limites de aplicabilidade
- produzir resultados rastreáveis
- interagir com Cognição, RAG, Experiência, Learning e Governança
- evoluir de forma controlada

A Skill amplia a capacidade cognitiva do sistema sem substituir a cognição geral.


# 2. MISSÃO

Permitir que o sistema utilize competências especializadas profundas sem:

- fragmentar a cognição
- transformar conhecimento especializado em autoridade absoluta
- ocultar incertezas
- misturar domínios indevidamente
- permitir invasão de escopo
- transformar heurísticas em fatos
- converter experiência em regra automaticamente
- permitir evolução não governada
- criar dependência de uma única Skill
- restringir desnecessariamente a liberdade cognitiva do LLM


# 3. NÃO-OBJETIVOS

A camada SKL não deve:

1. substituir a Cognição
2. substituir o RAG
3. substituir a Experiência
4. substituir Learning
5. substituir Governança
6. controlar o raciocínio interno do LLM
7. determinar automaticamente a decisão final
8. declarar uma hipótese como verdade apenas por pertencer ao domínio
9. transformar conhecimento especializado em autoridade universal
10. modificar conhecimento canônico sem Governança
11. modificar contratos fundamentais sem Governança
12. apagar evidências contrárias
13. eliminar hipóteses alternativas sem justificativa
14. transformar correlação em causalidade
15. transformar experiência em regra universal
16. ocultar limitações da própria Skill
17. impedir que outra Skill conteste seus resultados
18. criar conhecimento sem preservar proveniência
19. utilizar conhecimento fora de seu escopo sem sinalização
20. substituir evidência por autoridade nominal


# 4. PRINCÍPIO CENTRAL

> UMA SKILL É UMA COMPETÊNCIA ESPECIALIZADA, NÃO UMA AUTORIDADE COGNITIVA ABSOLUTA.

A Skill deve aumentar a capacidade do sistema de pensar sobre determinado domínio.

Ela não deve reduzir a capacidade do sistema de questionar, comparar, contestar ou abandonar a interpretação produzida pela própria Skill.


# 5. PRINCÍPIOS FUNDAMENTAIS

## SKL-P01 — Especialização sem isolamento

A Skill pode possuir conhecimento profundo de seu domínio, mas permanece integrada ao sistema cognitivo geral.

## SKL-P02 — Escopo explícito

Toda Skill deve possuir limites explícitos de competência.

## SKL-P03 — Uma Skill, uma competência principal

Uma Skill deve possuir uma questão ou conjunto de questões centrais claramente delimitado.

## SKL-P04 — Conhecimento não é competência

Ter acesso a determinado conhecimento não significa possuir competência para utilizá-lo adequadamente.

## SKL-P05 — Competência não é autoridade

Uma Skill especializada pode produzir análise sem possuir autoridade automática para determinar o resultado final.

## SKL-P06 — Evidência antes da afirmação

Afirmações relevantes devem possuir relação rastreável com evidências ou ser explicitamente classificadas como hipótese, inferência, heurística ou suposição.

## SKL-P07 — Incerteza preservada

A Skill não pode transformar incerteza em certeza apenas para produzir uma resposta mais assertiva.

## SKL-P08 — Limites explícitos

Quando uma tarefa ultrapassar sua competência, a Skill deve declarar a limitação.

## SKL-P09 — Contestabilidade

Resultados de uma Skill devem poder ser contestados por outra Skill, pela Cognição ou por evidências externas.

## SKL-P10 — Não invasão de domínio

Uma Skill não deve assumir competência sobre domínio que não pertence ao seu contrato.

## SKL-P11 — Conhecimento compartilhado

Skills devem utilizar a mesma autoridade semântica e de conhecimento definida pelo sistema.

## SKL-P12 — RAG como capacidade compartilhada

Skills podem solicitar recuperação de conhecimento por meio do RAG, sem criar autoridade própria sobre o conhecimento.

## SKL-P13 — Experiência contextual

Experiências anteriores podem subsidiar a Skill, mas não devem ser automaticamente transformadas em regra.

## SKL-P14 — Learning separado da execução

Uma Skill pode gerar evidências de melhoria, mas a evolução de sua competência deve passar pelo processo de Learning e Governança.

## SKL-P15 — Identidade preservada

Uma Skill deve possuir identidade, versão e escopo próprios.

## SKL-P16 — Reprodutibilidade proporcional

Uma Skill deve permitir reproduzir ou auditar suficientemente suas aplicações relevantes.

## SKL-P17 — Contexto obrigatório

Uma Skill não deve interpretar uma situação relevante sem contexto suficiente para sua competência.

## SKL-P18 — Hipótese antes de conclusão

Quando a natureza do domínio exigir interpretação, a Skill deve poder representar hipóteses concorrentes.

## SKL-P19 — Contraprova

Evidências que enfraquecem uma interpretação relevante devem ser preservadas.

## SKL-P20 — Especialização não elimina cognição geral

A Skill deve ampliar a cognição, não substituí-la.

## SKL-P21 — Evolução governada

Mudanças relevantes na Skill devem ser versionadas, avaliadas e governadas proporcionalmente ao impacto.

## SKL-P22 — Economicidade

A profundidade da Skill deve ser proporcional ao valor esperado da tarefa e ao custo cognitivo, computacional e operacional.

## SKL-P23 — Não dependência indevida

O sistema não deve depender de uma única Skill quando múltiplas perspectivas forem relevantes.

## SKL-P24 — Falha explícita

Uma Skill que não consiga produzir resultado confiável deve poder retornar:

- insuficiência
- inconclusividade
- conflito
- fora de escopo
- necessidade de evidência adicional


# 6. MODELO CONCEITUAL

A relação fundamental é:

```text
TAREFA
   ↓
IDENTIFICAÇÃO DA NECESSIDADE
   ↓
SELEÇÃO / ATIVAÇÃO DA SKILL
   ↓
CONTEXTUALIZAÇÃO
   ↓
RECUPERAÇÃO DE CONHECIMENTO
   ↓
APLICAÇÃO DA COMPETÊNCIA
   ↓
HIPÓTESES / ANÁLISE
   ↓
EVIDÊNCIAS / CONTRAEVIDÊNCIAS
   ↓
RESULTADO ESPECIALIZADO
   ↓
COGNIÇÃO GERAL
   ↓
INTEGRAÇÃO / COMPARAÇÃO
   ↓
DECISÃO OU PRÓXIMA AÇÃO

A Skill Unit deve representar a competência sem depender da implementação tecnológica.

8. IDENTIDADE DA SKILL

Toda Skill deve possuir identidade explícita.

A identidade deve permitir responder:

O que esta Skill faz?
Por que ela existe?
Qual problema resolve?
Qual domínio atende?
Qual é sua competência principal?
O que ela não faz?
Quais métodos utiliza?
Quais conhecimentos necessita?
Quais limitações possui?
Como seus resultados são avaliados?
Como evolui?
9. ESCOPO

O escopo deve possuir pelo menos:

domain:
subdomains:
primary_tasks:
supported_questions:
supported_contexts:
excluded_tasks:
excluded_domains:

O escopo deve ser suficientemente preciso para evitar:

invasão de domínio
falsa autoridade
sobreposição não controlada
utilização inadequada
10. CAPACIDADES

Cada Skill deve declarar suas capacidades.

Exemplo:

capabilities:
  - pattern_identification
  - hypothesis_generation
  - evidence_interpretation
  - scenario_analysis
  - parameter_analysis
  - comparative_analysis

Capacidade não significa obrigação de execução em qualquer contexto.

Cada capacidade deve possuir condições de aplicabilidade.

11. LIMITAÇÕES

A Skill deve possuir limitações explícitas.

limitations:
  - insufficient_context
  - insufficient_evidence
  - domain_boundary
  - temporal_invalidity
  - conflicting_sources
  - unsupported_inference

Limitação não deve ser tratada como falha quando representa uma propriedade legítima do domínio.

12. CONHECIMENTO DA SKILL

Uma Skill não deve possuir uma cópia isolada da autoridade de conhecimento.

Sua relação deve ser:

SKILL
  ↓ solicita
RAG
  ↓ recupera
EVIDENCE PACKET
  ↓ fornece
SKILL
  ↓ aplica competência
ANÁLISE

A Skill pode possuir:

modelos especializados
procedimentos
heurísticas
taxonomias
ontologias específicas
padrões de interpretação
critérios de análise

Mas o conhecimento utilizado deve manter:

proveniência
versão
temporalidade
classe
confiança
conflitos
13. SKILL + RAG

O contrato entre Skill e RAG deve definir:

skill_rag_request:
skill_id:
task:
domain:
required_knowledge:
preferred_knowledge_classes:
temporal_scope:
minimum_evidence:
contradiction_requirement:
confidence_requirement:
context_budget:

O RAG deve responder com Evidence Packet.

A Skill não deve tratar qualquer texto recuperado como conhecimento validado.

14. SKILL + COGNIÇÃO

A relação é:

SKILL → competência especializada
COGNIÇÃO → integração e raciocínio

A Skill pode produzir:

observações
interpretações
hipóteses
evidências
contraevidências
relações
cenários
limitações
confiança

A Cognição pode:

comparar Skills
identificar conflitos
questionar premissas
produzir hipóteses alternativas
integrar resultados
rejeitar interpretações
solicitar novas evidências
15. SKILL + EXPERIÊNCIA

Experiência fornece contexto histórico.

EXPERIÊNCIA
      ↓
contexto histórico
      ↓
SKILL
      ↓
interpretação especializada

A Skill não deve:

reescrever experiências
tratar experiência como regra universal
confundir frequência histórica com causalidade
ignorar mudanças de regime
16. SKILL + LEARNING

Learning pode avaliar:

desempenho da Skill
precisão
estabilidade
custo
aplicabilidade
regressões
calibração
adequação por contexto
padrões de falha

Learning pode produzir:

learning_candidate:
  skill_id:
  observation:
  problem:
  hypothesis:
  proposed_change:
  expected_effect:
  experiment:
  evidence:
  validation_status:

A Skill não pode autoautorizar sua própria evolução.

17. SKILL + GOVERNANÇA

Mudanças relevantes devem seguir Governança.

Exemplos:

mudança de parâmetro
mudança de heurística
mudança de método
mudança de escopo
mudança de conhecimento fundamental
mudança de contrato
mudança de identidade
mudança de comportamento

A severidade da governança deve ser proporcional ao impacto.

18. MULTI-SKILL

Quando múltiplas Skills atuarem sobre o mesmo problema:

              ┌── SKILL A
              │
TAREFA ───────┼── SKILL B
              │
              └── SKILL C
                    ↓
              COGNIÇÃO INTEGRADORA
                    ↓
              SÍNTESE / HIPÓTESES

A existência de múltiplas Skills não implica consenso obrigatório.

Conflitos devem permanecer representáveis.

19. SKILL CONFLICT

Conflitos entre Skills devem ser classificados.

conflict_id:
skill_a:
skill_b:

conflict_type:
  - terminology
  - observation
  - interpretation
  - methodology
  - hypothesis
  - evidence
  - temporal
  - domain_boundary

evidence_a:
evidence_b:

resolution_status:
resolution_method:
remaining_uncertainty:

Um conflito não deve ser eliminado apenas para produzir uma resposta única.

20. SKILL INVOCATION

A ativação de uma Skill deve considerar:

task:
objective:
domain:
context:
required_capability:
available_evidence:
required_depth:
time_budget:
resource_budget:
risk:

A seleção deve considerar adequação da competência, não apenas similaridade nominal.

21. SKILL DEPTH

A profundidade da aplicação pode variar:

LEVEL 0 — NÃO NECESSÁRIA

LEVEL 1 — CONSULTA RÁPIDA

LEVEL 2 — ANÁLISE ESPECIALIZADA

LEVEL 3 — ANÁLISE PROFUNDA

LEVEL 4 — ANÁLISE CRÍTICA / MULTI-SKILL

LEVEL 5 — INVESTIGAÇÃO ESPECIALIZADA

O nível deve ser proporcional:

valor esperado
×
risco
×
incerteza
×
complexidade

versus:

latência
+
tokens
+
compute
+
custo operacional
22. SKILL OUTPUT

Toda saída especializada deve permitir distinguir:

skill_id:
task:
scope:

observations:
facts:
assumptions:

knowledge_used:
evidence:

hypotheses:
alternative_hypotheses:

analysis:

confidence:
uncertainty:

limitations:
out_of_scope:

contradictions:

recommendation_for_cognition:
open_questions:

provenance:
version:

A Skill pode produzir uma conclusão especializada, mas deve permitir que o sistema saiba em que condições essa conclusão foi produzida.

23. ESTADOS DA SKILL
DEFINED
   ↓
VALIDATED
   ↓
AVAILABLE
   ↓
ACTIVE
   ↓
MONITORED
   ↓
EVOLVING
   ↓
REVALIDATING
   ↓
SUPERSEDED
   ↓
ARCHIVED

Estados adicionais:

DEGRADED
SUSPENDED
INVALIDATED
OUT_OF_SCOPE

Uma Skill invalidada não deve ser utilizada silenciosamente.

24. ESPECIFICAÇÕES A DESENVOLVER
FUNDAMENTOS

SKL-SPEC-001 — Skill Capability Contract
SKL-SPEC-002 — Skill Identity Model
SKL-SPEC-003 — Skill Mission Model
SKL-SPEC-004 — Skill Scope Model
SKL-SPEC-005 — Skill Domain Model
SKL-SPEC-006 — Skill Capability Model
SKL-SPEC-007 — Skill Limitation Model
SKL-SPEC-008 — Skill State Model
SKL-SPEC-009 — Skill Version Model
SKL-SPEC-010 — Skill Provenance Model

COMPETÊNCIA

SKL-SPEC-011 — Competence Model
SKL-SPEC-012 — Competence Boundary
SKL-SPEC-013 — Capability Applicability
SKL-SPEC-014 — Method Model
SKL-SPEC-015 — Heuristic Model
SKL-SPEC-016 — Procedure Model
SKL-SPEC-017 — Specialized Model Contract
SKL-SPEC-018 — Domain Pattern Model
SKL-SPEC-019 — Skill Depth Model
SKL-SPEC-020 — Skill Specialization Model

CONTEXTO

SKL-SPEC-021 — Skill Context Contract
SKL-SPEC-022 — Context Sufficiency
SKL-SPEC-023 — Context Relevance
SKL-SPEC-024 — Context Completeness
SKL-SPEC-025 — Context Temporal Validity
SKL-SPEC-026 — Context Regime Model
SKL-SPEC-027 — Context Degradation
SKL-SPEC-028 — Context Recovery

RAG

SKL-SPEC-029 — Skill-to-RAG Contract
SKL-SPEC-030 — Knowledge Requirement Model
SKL-SPEC-031 — Evidence Requirement Model
SKL-SPEC-032 — Retrieval Requirement
SKL-SPEC-033 — Evidence Packet Consumption
SKL-SPEC-034 — Knowledge Sufficiency
SKL-SPEC-035 — Knowledge Conflict Handling
SKL-SPEC-036 — Knowledge Gap Escalation

COGNIÇÃO

SKL-SPEC-037 — Skill-to-Cognition Contract
SKL-SPEC-038 — Specialized Hypothesis Model
SKL-SPEC-039 — Alternative Hypothesis
SKL-SPEC-040 — Evidence-to-Interpretation Mapping
SKL-SPEC-041 — Specialized Inference
SKL-SPEC-042 — Counterevidence
SKL-SPEC-043 — Uncertainty Representation
SKL-SPEC-044 — Confidence Calibration
SKL-SPEC-045 — Skill Limitation Reasoning
SKL-SPEC-046 — Skill-to-Cognition Escalation

MULTI-SKILL

SKL-SPEC-047 — Multi-Skill Coordination
SKL-SPEC-048 — Skill Selection
SKL-SPEC-049 — Skill Composition
SKL-SPEC-050 — Skill Redundancy
SKL-SPEC-051 — Skill Complementarity
SKL-SPEC-052 — Skill Conflict
SKL-SPEC-053 — Cross-Skill Evidence Comparison
SKL-SPEC-054 — Cross-Skill Hypothesis Comparison
SKL-SPEC-055 — Multi-Skill Synthesis

EXPERIÊNCIA

SKL-SPEC-056 — Skill-to-Experience Contract
SKL-SPEC-057 — Historical Skill Performance
SKL-SPEC-058 — Regime-Specific Skill Experience
SKL-SPEC-059 — Similar Skill Experience
SKL-SPEC-060 — Contrasting Skill Experience

LEARNING

SKL-SPEC-061 — Skill-to-Learning Contract
SKL-SPEC-062 — Skill Performance Measurement
SKL-SPEC-063 — Skill Improvement Hypothesis
SKL-SPEC-064 — Skill Experimentation
SKL-SPEC-065 — Skill Calibration
SKL-SPEC-066 — Skill Drift Detection
SKL-SPEC-067 — Skill Regression
SKL-SPEC-068 — Skill Learning Candidate

GOVERNANÇA

SKL-SPEC-069 — Skill-to-Governance Contract
SKL-SPEC-070 — Skill Change Classification
SKL-SPEC-071 — Skill Impact Classification
SKL-SPEC-072 — Skill Approval Requirement
SKL-SPEC-073 — Skill Promotion
SKL-SPEC-074 — Skill Rollback
SKL-SPEC-075 — Skill Deprecation
SKL-SPEC-076 — Skill Exception

OUTPUT

SKL-SPEC-077 — Skill Output Contract
SKL-SPEC-078 — Evidence Traceability
SKL-SPEC-079 — Confidence Reporting
SKL-SPEC-080 — Uncertainty Reporting
SKL-SPEC-081 — Limitation Reporting
SKL-SPEC-082 — Conflict Reporting
SKL-SPEC-083 — Provenance Reporting

HARNESS

SKL-SPEC-084 — Skill Harness
SKL-SPEC-085 — Skill Deterministic Sensors
SKL-SPEC-086 — Skill Inferential Sensors
SKL-SPEC-087 — Skill Behavioral Tests
SKL-SPEC-088 — Skill Adversarial Tests
SKL-SPEC-089 — Skill Boundary Tests
SKL-SPEC-090 — Skill Regression Tests
SKL-SPEC-091 — Skill Benchmark Suite
SKL-SPEC-092 — Skill Economicity Benchmark
SKL-SPEC-093 — Skill Observability
SKL-SPEC-094 — Skill Failure Detection
SKL-SPEC-095 — Skill Version Validation

25. HARNESS DA SKILL

O Harness deve avaliar propriedades observáveis da competência.

Não deve exigir uma única forma de raciocínio interno.

Sensores determinísticos

Devem verificar:

identidade
versão
escopo
entradas obrigatórias
saídas obrigatórias
proveniência
referências
estado
integridade estrutural
contratos
invariantes
compatibilidade de versão
limites de domínio
Sensores inferenciais

Devem avaliar:

adequação da Skill ao problema
adequação da competência
suficiência contextual
qualidade das evidências
coerência especializada
qualidade das hipóteses
tratamento de alternativas
tratamento de contraevidências
calibração de confiança
representação de incerteza
respeito aos limites da Skill
qualidade da síntese
adequação da profundidade
26. TESTES DO HARNESS
Testes funcionais
Skill activation
Skill invocation
Skill context
Skill retrieval
Skill analysis
Skill output
Skill failure
Testes de fronteira
tarefa fora do domínio
contexto insuficiente
conhecimento insuficiente
conflito entre fontes
conflito entre Skills
mudança de regime
entrada ambígua
extrapolação indevida
Testes cognitivos
hipótese concorrente
contraevidência
atualização de hipótese
incerteza
confiança
conclusão prematura
falsa certeza
confirmação seletiva
Testes adversariais
prompt tentando expandir escopo
evidência falsa
conhecimento conflitante
instrução de autoridade falsa
contexto contaminado
indução de excesso de confiança
manipulação de prioridade
Testes de regressão

Devem detectar degradação em:

precisão
cobertura
robustez
consistência
calibração
custo
latência
especialização
limites de domínio
27. INVARIANTES
I-SKL-01

Uma Skill não pode atuar fora de seu escopo sem sinalizar a extrapolação.

I-SKL-02

Especialização não confere autoridade absoluta.

I-SKL-03

Conhecimento recuperado não é automaticamente conhecimento validado.

I-SKL-04

Uma hipótese especializada não é automaticamente um fato.

I-SKL-05

Contraevidência relevante não pode ser silenciosamente descartada.

I-SKL-06

Incerteza não pode ser removida apenas para aumentar assertividade.

I-SKL-07

Experiência não pode ser transformada automaticamente em regra.

I-SKL-08

Uma Skill não pode alterar seu próprio contrato fundamental sem Governança.

I-SKL-09

Uma Skill não pode modificar silenciosamente a autoridade semântica do sistema.

I-SKL-10

Conflitos entre Skills não podem ser apagados apenas para produzir consenso.

I-SKL-11

Uma Skill deve poder declarar insuficiência.

I-SKL-12

A Skill não pode substituir a Cognição geral.

I-SKL-13

A Skill não pode substituir Governança.

I-SKL-14

A Skill não pode reescrever Experiência histórica.

I-SKL-15

Learning não possui autorização automática para modificar uma Skill.

I-SKL-16

Mudanças relevantes devem possuir versão e rastreabilidade.

I-SKL-17

A profundidade da Skill deve ser proporcional ao problema.

I-SKL-18

Maior especialização não implica maior certeza.

I-SKL-19

Ausência de conhecimento suficiente deve poder resultar em UNKNOWN ou INCONCLUSIVE.

I-SKL-20

O Harness deve avaliar comportamento observável e não impor uma única estratégia interna de raciocínio.

28. QUALITY GATES
G0 — Skill Contract

Identidade, missão e escopo definidos.

G1 — Competence Integrity

Competência delimitada e verificável.

G2 — Context Integrity

Contexto mínimo definido.

G3 — Knowledge Integrity

Dependências de conhecimento identificadas.

G4 — Evidence Integrity

Evidências rastreáveis.

G5 — Cognitive Integrity

Hipóteses, alternativas e incertezas preservadas.

G6 — Boundary Integrity

Fronteiras da competência verificadas.

G7 — Multi-Skill Integrity

Conflitos e composição controlados.

G8 — Experience Integrity

Uso de experiência contextualizado.

G9 — Learning Integrity

Evolução separada da execução.

G10 — Governance Integrity

Mudanças sujeitas à Governança.

G11 — Harness Integrity

Sensores e testes suficientes.

G12 — Regression Integrity

Ausência de regressões relevantes.

G13 — Economicity Integrity

Valor da especialização proporcional ao custo.

29. MÉTRICAS
Qualidade
Skill Accuracy
Skill Precision
Skill Recall
Skill Coverage
Skill Robustness
Skill Consistency
Skill Calibration
Skill Generalization
Especialização
Domain Relevance
Specialized Reasoning Quality
Boundary Compliance
Out-of-Scope Detection
Skill Applicability
Evidência
Evidence Coverage
Evidence Traceability
Counterevidence Coverage
Evidence Sufficiency
Cognição
Hypothesis Quality
Alternative Coverage
Uncertainty Calibration
Confidence Calibration
Premature Closure Rate
Multi-Skill
Skill Conflict Detection
Cross-Skill Consistency
Cross-Skill Complementarity
False Consensus Rate
Evolução
Skill Improvement Rate
Regression Rate
Drift Rate
Calibration Stability
Version Stability
Operacional
Latency
Token Cost
Compute Cost
Retrieval Cost
Invocation Cost
Economicidade
Skill Utility
Value per Token
Value per Compute
Value per Invocation
Cost per Validated Insight
30. FAILURE TAXONOMY
SKILL FAILURE
│
├── Identity Failure
├── Scope Failure
├── Boundary Failure
├── Context Failure
├── Knowledge Failure
├── Evidence Failure
├── Interpretation Failure
├── Hypothesis Failure
├── Confidence Failure
├── Uncertainty Failure
├── Counterevidence Failure
├── Domain Leakage
├── False Authority
├── Cross-Skill Conflict Failure
├── False Consensus
├── Experience Contamination
├── Learning Failure
├── Regression
├── Version Failure
├── Governance Failure
├── Harness Failure
└── Economic Failure
31. OBSERVABILIDADE

Toda execução relevante de Skill deve permitir reconstruir:

qual Skill
qual versão
qual tarefa
qual contexto
qual conhecimento
quais evidências
quais hipóteses
quais alternativas
qual resultado
qual incerteza
quais limitações
qual custo
qual versão do sistema

A observabilidade deve ser suficiente para auditoria e reprodução proporcional ao impacto.

32. BENCHMARK SUITE

O Benchmark da Skill deve conter pelo menos:

competência
escopo
fora de escopo
contexto suficiente
contexto insuficiente
conhecimento suficiente
conhecimento insuficiente
evidência conflitante
contraevidência
hipótese concorrente
incerteza
calibração
mudança de regime
conflito entre Skills
falsa autoridade
prompt injection de escopo
generalização indevida
experiência enganosa
regressão
custo-benefício
33. BENCHMARK DE ECONOMICIDADE

Uma Skill não deve ser considerada melhor simplesmente porque produz análise mais profunda.

A avaliação deve considerar:

VALOR GERADO
-------------------------------
tokens
compute
latência
complexidade
custo de recuperação
custo de coordenação
custo de validação

Uma Skill deve demonstrar que sua profundidade adicional produz benefício mensurável ou justificável.

34. VERSIONAMENTO
version:
baseline:
skill_change:
reason:
scope_change:
knowledge_change:
method_change:
behavior_change:
expected_effect:
tests:
benchmarks:
regressions:
economic_evaluation:
governance_status:
rollback_plan:

Mudanças devem permitir comparação entre versões.

35. CICLO DE VIDA
IDEA
 ↓
DEFINED
 ↓
SPECIFIED
 ↓
IMPLEMENTED / INSTANTIATED
 ↓
VALIDATED
 ↓
AVAILABLE
 ↓
ACTIVE
 ↓
MONITORED
 ↓
LEARNING
 ↓
PROPOSED CHANGE
 ↓
GOVERNANCE
 ↓
REVALIDATION
 ↓
PROMOTION
 ↓
MONITORING
 ↓
SUPERSESSION / ARCHIVAL
36. CRITÉRIO DE PRONTIDÃO

Uma Skill somente deve ser considerada pronta quando possuir:

identidade
missão
escopo
limites
competência definida
conhecimento necessário
contrato com RAG
contrato com Cognição
contrato com Experiência
contrato com Learning
contrato com Governança
modelo de saída
incerteza
evidências
contraevidências
Harness
testes
benchmarks
métricas
observabilidade
versionamento
regressão
economicidade
37. RELAÇÃO COM AS DEMAIS CAMADAS
                  GOVERNANÇA
                       │
                       ▼
                    SKILL
                  ↙   ↓   ↘
               RAG  COGNIÇÃO  EXPERIÊNCIA
                     │          │
                     └────┬─────┘
                          ▼
                       LEARNING
                          │
                          ▼
                    EVOLUÇÃO DA SKILL
                          │
                          ▼
                     GOVERNANÇA

A Skill funciona como uma camada de competência especializada entre o conhecimento disponível e a cognição aplicada.

38. REGRA ESPECIAL PARA SKILLS DE ALTO RISCO

Quanto maior o impacto potencial da aplicação da Skill:

↑ evidência necessária
↑ validação
↑ cobertura de testes
↑ monitoramento
↑ rastreabilidade
↑ exigência de regressão
↑ revisão proporcional

Não se deve simplesmente aumentar a restrição cognitiva.

O objetivo é aumentar a confiabilidade do ambiente no qual a cognição especializada opera.

39. REGRA FUNDAMENTAL DE LIBERDADE COGNITIVA

A Skill deve fornecer:

conhecimento
+
método
+
contexto
+
evidência
+
restrições de validade

e não:

conclusão obrigatória

O LLM permanece livre para:

concordar
discordar
gerar hipótese alternativa
solicitar mais evidência
identificar conflito
declarar desconhecimento
rejeitar uma interpretação
integrar outra Skill
revisar a própria análise
40. CRITÉRIO FINAL

A Camada de Skills estará adequadamente especificada quando for possível demonstrar simultaneamente que:

o sistema possui competências especializadas profundas
cada competência possui limites explícitos
Skills podem utilizar conhecimento compartilhado
evidências permanecem rastreáveis
hipóteses permanecem distinguíveis de fatos
incerteza é preservada
Skills podem contestar umas às outras
a Cognição permanece integradora
Experiência não vira regra automaticamente
Learning pode melhorar Skills sem autoautoridade
Governança controla mudanças relevantes
o Harness detecta falhas observáveis
regressões podem ser identificadas
o custo da especialização pode ser medido
a especialização aumenta capacidade sem transformar a Skill em autoridade absoluta
41. BASELINE

MC-SKL-001 v1.0

Estado:

MASTER CONTRACT BASELINE

Dependências:

RAG
COG
EXP
LRN
GOV

Dependentes:

Agentes especializados
Skills de domínio
Skills analíticas
Skills operacionais
Skills de investigação
Skills de validação
Skills de suporte cognitivo


### Ponto arquitetural importante

Nesta camada aparece uma distinção que considero **fundamental para o SOT**:

**Skill não deve ser entendida como “agente especialista”.**

O agente pode **usar uma ou várias Skills**.

```text
AGENTE
  │
  ├── Skill A
  ├── Skill B
  ├── Skill C
  │
  ├── RAG
  ├── Experiência
  ├── Cognição
  ├── Learning
  └── Governança

Isso permite, por exemplo, que Elliott, SMC e ICT sejam competências especializadas, sem obrigar que cada uma delas seja um “cérebro independente”. A cognição permanece capaz de comparar, contestar e combinar as perspectivas.