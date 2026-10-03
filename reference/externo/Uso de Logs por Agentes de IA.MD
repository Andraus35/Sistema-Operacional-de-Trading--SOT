# MASTER DOCUMENT

# Uso de Logs por Agentes de IA

**Status:** Master Document
**Domínio:** AI Engineering / Agent Engineering / Observability / Harness
**Aplicação:** Agentes individuais, multiagentes, agentes autônomos, workflows agentic, ferramentas, RAG e Harnesses
**Princípio central:** Log não é memória. Log é evidência estruturada da execução.
**Objetivo:** Tornar o comportamento de um agente reconstruível, avaliável, auditável e melhorável sem transformar a execução em burocracia.

---

# 1. Propósito

Este documento estabelece os princípios, arquitetura, semântica, requisitos mínimos e critérios de qualidade para uso de logs por agentes de IA.

O objetivo não é registrar tudo.

O objetivo é registrar **evidência suficiente para explicar e avaliar o comportamento do agente**.

Um sistema de logging de agente deve permitir responder, após uma execução:

1. O que o agente recebeu?
2. Em qual contexto estava?
3. Qual objetivo estava tentando satisfazer?
4. Qual estado possuía?
5. Quais decisões operacionais tomou?
6. Quais ferramentas utilizou?
7. Quais resultados recebeu?
8. Quais informações recuperou?
9. Quais mudanças de estado ocorreram?
10. Quais erros ocorreram?
11. Quantas tentativas/retries foram realizadas?
12. Quais invariantes foram satisfeitos?
13. Quais invariantes foram violados?
14. Qual foi o resultado observável?
15. Quanto custou?
16. Quanto tempo levou?
17. Por que o sistema considerou a execução bem-sucedida ou malsucedida?
18. É possível reproduzir ou investigar a execução posteriormente?

---

# 2. Princípio fundamental

## 2.1 Log não é texto de console

Um log tradicional pode ser:

```text
Agent started
Calling tool
Tool failed
Retrying
Agent finished
```

Isso é insuficiente para engenharia de agentes.

O agente precisa produzir registros estruturados.

Exemplo:

```json
{
  "event": "tool_call",
  "trace_id": "tr_8f31",
  "span_id": "sp_14",
  "agent_id": "researcher",
  "tool": "search_market",
  "arguments_ref": "arg_91",
  "attempt": 1,
  "reason_ref": "decision_32",
  "status": "requested"
}
```

O segundo registro pode ser correlacionado com o primeiro e com todos os demais eventos da execução.

---

# 3. Definição operacional

Para este documento:

> **Log de agente é um registro estruturado de uma ocorrência relevante durante o ciclo de vida de uma execução agentic.**

Um log pode representar:

* evento
* erro
* mudança de estado
* decisão operacional
* chamada de ferramenta
* resultado de ferramenta
* mudança de contexto
* recuperação de conhecimento
* handoff
* geração de modelo
* avaliação
* violação de política
* mudança de configuração
* checkpoint
* resultado operacional

Entretanto, operações com duração própria devem preferencialmente ser representadas como **spans/traces**, e ocorrências pontuais como **events/logs**.

---

# 4. O modelo correto: Logs + Traces + Metrics + Evaluations

Um agente moderno não deve depender de uma única camada de observabilidade.

A arquitetura recomendada é:

```text
                    AGENT RUN
                       │
          ┌────────────┼────────────┐
          │            │            │
        TRACE         LOGS        METRICS
          │            │            │
          └────────────┼────────────┘
                       │
                   EVALUATION
                       │
                       ▼
                KNOWLEDGE / DATASET
                       │
                       ▼
                 IMPROVEMENT LOOP
```

### Trace

Responde:

> Qual foi o caminho completo da execução?

### Log/Event

Responde:

> O que aconteceu neste ponto específico?

### Metric

Responde:

> Com que frequência, custo, latência ou taxa isso acontece?

### Evaluation

Responde:

> Esse comportamento foi bom, ruim ou conforme o critério?

### Dataset/Regression Set

Responde:

> O problema já aconteceu antes e conseguimos impedir sua regressão?

---

# 5. Unidade fundamental: Agent Run

Toda execução relevante deve possuir um identificador único.

```text
agent_run_id
```

Preferencialmente correlacionado com:

```text
trace_id
session_id
parent_run_id
```

Modelo:

```text
Session
   │
   ├── Agent Run
   │      ├── Agent Span
   │      │      ├── LLM Generation
   │      │      ├── Tool Call
   │      │      ├── Retrieval
   │      │      └── Decision Event
   │      │
   │      └── Agent Span
   │             └── ...
   │
   └── Agent Run
```

Essa estrutura é particularmente importante em sistemas multiagentes.

---

# 6. Hierarquia recomendada

## Nível 0 — Session

Agrupa execuções relacionadas.

Exemplo:

```text
session_id = sess_123
```

Pode representar:

* conversa
* projeto
* tarefa longa
* processo de negócio

---

## Nível 1 — Agent Run

Representa uma execução completa do agente.

Exemplo:

```text
run_id = run_782
```

---

## Nível 2 — Agent Span

Representa uma unidade de trabalho do agente.

Exemplos:

```text
planning
retrieval
analysis
tool_execution
validation
handoff
finalization
```

---

## Nível 3 — Generation

Cada chamada individual ao modelo deve ser observável.

Não esconder um loop inteiro dentro de uma única chamada agregada.

Exemplo:

```text
Agent
 ├── Generation #1
 ├── Tool Call
 ├── Tool Result
 ├── Generation #2
 ├── Tool Call
 ├── Tool Result
 └── Generation #3
```

Essa estrutura permite descobrir:

* loops
* retries
* explosão de contexto
* ferramentas problemáticas
* decisões divergentes
* custo por etapa
* latência por etapa

---

# 7. Regra de granularidade

## Registrar como Span quando:

A operação:

* possui duração
* possui início/fim
* representa trabalho
* pode conter operações filhas

Exemplos:

```text
agent.run
llm.generate
tool.execute
retrieval.search
workflow.step
handoff
validation
```

## Registrar como Event quando:

É uma ocorrência pontual.

Exemplos:

```text
state.changed
retry.started
policy.violation
checkpoint.created
approval.requested
handoff.created
evaluation.completed
```

## Registrar como Metric quando:

A informação deve ser agregada.

Exemplos:

```text
agent_run_count
agent_error_rate
tool_failure_rate
token_usage
cost
latency
retry_count
context_utilization
evaluation_score
```

---

# 8. O que todo Agent Run deve registrar

## Identidade

```text
run_id
trace_id
session_id
parent_run_id
agent_id
agent_version
harness_version
environment
```

## Tempo

```text
started_at
ended_at
duration_ms
```

## Objetivo

```text
task_type
task_id
objective
```

## Configuração

```text
model
model_version
temperature
reasoning_configuration
tool_policy
prompt_version
skill_version
```

## Resultado

```text
status
outcome
termination_reason
```

## Recursos

```text
input_tokens
output_tokens
total_tokens
estimated_cost
tool_calls
retrieval_calls
retry_count
```

---

# 9. O que registrar sobre o modelo

Cada geração deve permitir responder:

```text
Qual modelo?
Qual versão?
Qual configuração?
Qual entrada?
Qual saída?
Quanto tempo levou?
Quantos tokens consumiu?
Qual foi o custo?
Qual ferramenta solicitou?
```

Exemplo:

```json
{
  "event_type": "generation",
  "model": "MODEL_ID",
  "model_version": "MODEL_VERSION",
  "input_tokens": 4200,
  "output_tokens": 830,
  "latency_ms": 2840,
  "cost": 0.014,
  "status": "completed"
}
```

---

# 10. Captura de prompts e outputs

A captura de conteúdo completo deve ser tratada como **opt-in e governada**, não como obrigação universal.

Motivos:

* PII
* segredos
* credenciais
* informações financeiras
* propriedade intelectual
* dados regulados
* conteúdo sensível
* tamanho excessivo
* custo de armazenamento

O padrão deve ser:

```text
Metadata → obrigatório quando necessário
Content → condicionado à necessidade, risco e política
```

Nunca:

```text
capture tudo indiscriminadamente
```

---

# 11. Referência em vez de duplicação

Quando um payload é grande, o log não precisa necessariamente armazená-lo integralmente.

Pode armazenar:

```json
{
  "content_ref": "artifact://trace/tr_123/input_45",
  "content_hash": "sha256:...",
  "content_size": 182340,
  "content_class": "agent_input"
}
```

Isso permite separar:

```text
Telemetry
    │
    ├── Metadata
    ├── Event
    └── Reference
             │
             ▼
        Content Store
```

Benefícios:

* menor custo
* menor exposição
* melhor controle de acesso
* retenção independente
* auditoria
* integridade por hash

---

# 12. Estado do agente

Agentes são sistemas orientados a estado.

Por isso, mudanças relevantes de estado devem ser observáveis.

Exemplo:

```json
{
  "event": "state.changed",
  "from": "ANALYZING",
  "to": "VALIDATING",
  "reason": "analysis_complete"
}
```

Não é necessário registrar todo estado interno.

Registrar:

> mudanças de estado que possuem significado operacional.

---

# 13. Decisões

Uma decisão relevante deve ser observável.

Não significa necessariamente armazenar raciocínio privado completo.

Registrar o **resultado operacional da decisão**.

Exemplo:

```json
{
  "event": "decision",
  "decision_type": "tool_selection",
  "selected_action": "search_market",
  "basis_refs": [
    "observation_18",
    "policy_07"
  ],
  "confidence": 0.82
}
```

O objetivo é conseguir responder:

> Por que essa ação aconteceu?

sem transformar o sistema em dependente da captura indiscriminada de cadeia de pensamento.

---

# 14. Ferramentas

Toda chamada de ferramenta relevante deve produzir evidência suficiente para reconstrução.

Registrar:

```text
tool_name
tool_version
tool_call_id
arguments
argument_hash
started_at
ended_at
duration
status
result_reference
error
retry_count
authorization_context
```

Exemplo:

```text
Agent
  │
  └── Tool Call
        ├── tool = search
        ├── arguments_ref = arg_92
        ├── authorization = permitted
        ├── status = success
        └── result_ref = result_31
```

---

# 15. Segurança de ferramentas

O log deve permitir detectar:

* ferramenta não autorizada
* ferramenta inesperada
* argumento inválido
* tentativa de escalada
* chamada repetitiva
* loop
* excesso de chamadas
* alteração de estado não prevista

Para agentes com capacidade de ação, logging e monitoramento devem acompanhar a atividade das extensões e sistemas downstream. Logging, entretanto, é uma camada de detecção e resposta e não substitui autorização efetiva no sistema que executa a ação.

---

# 16. RAG e recuperação

Para RAG, registrar:

```text
retrieval.query
retrieval.source
retrieval.index
retrieval.top_k
retrieval.result_count
retrieval.document_ids
retrieval.scores
retrieval.latency
retrieval.filters
```

Quando possível:

```text
document_id
chunk_id
source
version
relevance_score
```

Não é obrigatório copiar todo o conteúdo recuperado.

É frequentemente melhor registrar:

```text
document_ref
chunk_ref
hash
score
metadata
```

e manter o conteúdo em camada apropriada.

---

# 17. Contexto

Uma das funções mais importantes dos logs de agentes é permitir investigar o contexto.

Registrar:

```text
context_version
context_sources
context_size
context_token_count
context_window
context_utilization
truncated
truncation_reason
```

Exemplo:

```json
{
  "context_token_count": 71000,
  "context_window": 100000,
  "utilization": 0.71,
  "truncated": false
}
```

Isso torna possível investigar:

* perda de contexto
* excesso de contexto
* contexto insuficiente
* degradação de performance
* aumento de custo

---

# 18. Handoffs em sistemas multiagentes

Em sistemas multiagentes, o handoff é um evento de primeira classe.

Registrar:

```text
source_agent
target_agent
handoff_id
reason
task_reference
context_reference
state_reference
result
```

Exemplo:

```text
Estrategista
      │
      │ handoff
      ▼
Analista
      │
      │ handoff
      ▼
Controlador
```

O trace deve permitir reconstruir esse fluxo.

---

# 19. Multiagente

O trace de um sistema multiagente deve representar:

```text
ROOT
│
├── Agent A
│    ├── LLM
│    └── Tool
│
├── Agent B
│    ├── Retrieval
│    ├── LLM
│    └── Validation
│
└── Agent C
     ├── LLM
     └── Finalization
```

Nunca reduzir tudo a:

```text
SYSTEM → FINAL ANSWER
```

Isso elimina justamente a evidência necessária para entender o comportamento emergente.

---

# 20. Erros

Erro deve ser estruturado.

Mínimo:

```text
error.type
error.message
error.stage
error.severity
retryable
attempt
recovery_action
```

Exemplo:

```json
{
  "event": "error",
  "error.type": "ToolTimeout",
  "stage": "retrieval",
  "retryable": true,
  "attempt": 2,
  "recovery_action": "retry"
}
```

---

# 21. Retry

Retries devem ser explicitamente observáveis.

Registrar:

```text
retry_count
retry_reason
previous_error
backoff
new_attempt_id
final_outcome
```

Isso permite distinguir:

```text
1 execução lenta
```

de:

```text
1 execução
→ falha
→ retry
→ falha
→ retry
→ sucesso
```

Essa diferença é crítica para custo, latência e confiabilidade.

---

# 22. Loop detection

Agentes podem entrar em loops.

O sistema deve observar padrões como:

```text
same_tool
same_arguments
same_state
same_result
repeated_generation
```

Métricas úteis:

```text
iteration_count
repeated_action_count
max_iterations_reached
loop_detected
```

---

# 23. Invariantes

O log deve registrar violações de invariantes.

Exemplo:

```json
{
  "event": "invariant.violation",
  "invariant_id": "INV-007",
  "severity": "HIGH",
  "observed_value": "...",
  "expected_condition": "...",
  "trace_id": "..."
}
```

Isso é particularmente importante em Harnesses.

O agente pode possuir liberdade cognitiva, mas sua execução continua sujeita a invariantes.

---

# 24. Policy Enforcement

Quando uma regra bloqueia ou permite uma ação, registrar:

```text
policy_id
policy_version
decision
subject
action
resource
reason
enforcement_point
```

Exemplo:

```text
POLICY-003
action = execute_tool
decision = DENY
reason = insufficient_authorization
```

O log torna o enforcement verificável.

---

# 25. Approval Gates

Para agentes com aprovação humana:

```text
approval.requested
approval.pending
approval.approved
approval.rejected
approval.expired
```

Cada evento deve possuir:

```text
approval_id
requested_action
requester
approver
decision
timestamp
policy_reference
```

---

# 26. Observabilidade ≠ vigilância indiscriminada

Um erro comum é interpretar observabilidade como:

> guardar absolutamente tudo.

O princípio correto é:

> registrar a quantidade mínima de evidência necessária para explicar, avaliar, proteger e melhorar o sistema.

Isso reduz:

* custo
* latência
* ruído
* risco de exposição
* complexidade analítica

---

# 27. Cardinalidade

Campos usados para agrupamento e agregação devem possuir cardinalidade controlada.

Evitar transformar identificadores únicos em nomes de métricas.

Ruim:

```text
metric.agent.user_928372.call
```

Melhor:

```text
metric.agent.tool_call
attributes:
    agent_id
    tool_name
```

IDs devem permanecer como atributos/correlação quando apropriado.

---

# 28. Nomenclatura

Os nomes das operações devem representar **o que a operação faz**, e não a implementação momentânea.

Ruim:

```text
claude-sonnet-call
```

Melhor:

```text
agent.generation
```

O modelo é atributo:

```text
model = ...
```

Isso permite trocar o modelo sem destruir dashboards, avaliações ou consultas históricas.

---

# 29. Schema mínimo recomendado

Um evento genérico:

```json
{
  "timestamp": "...",
  "event_type": "...",

  "trace_id": "...",
  "span_id": "...",
  "parent_span_id": "...",
  "session_id": "...",
  "run_id": "...",

  "agent_id": "...",
  "agent_version": "...",
  "harness_version": "...",

  "environment": "...",

  "severity": "...",
  "status": "...",

  "operation": "...",

  "input_ref": "...",
  "output_ref": "...",

  "metadata": {},

  "error": null
}
```

Esse schema é um **modelo conceitual**, não uma tentativa de substituir OpenTelemetry.

---

# 30. OpenTelemetry como camada de interoperabilidade

Quando tecnicamente possível, o sistema deve utilizar OpenTelemetry como camada de telemetria.

Benefícios:

* padrão aberto
* correlação entre logs e traces
* vendor neutrality
* propagação de contexto
* integração com múltiplos backends
* convenções semânticas
* instrumentação distribuída

OpenTelemetry já define convenções específicas para GenAI, incluindo atributos para operações de geração, mensagens, sistemas de modelos e recuperação.

---

# 31. Regra de correlação

Todos os sinais relevantes devem ser correlacionáveis.

Mínimo:

```text
trace_id
span_id
parent_span_id
```

Quando necessário:

```text
session_id
run_id
task_id
request_id
```

A regra:

> Se um operador encontrar um erro em um log, deve conseguir navegar até a operação que o produziu e reconstruir o contexto relevante da execução.

---

# 32. Sampling

Não é necessário manter 100% do conteúdo de todas as execuções indefinidamente.

Estratégias possíveis:

```text
100% metadata
100% errors
100% policy violations
100% critical actions

sampled:
normal successful runs
full content
expensive payloads
```

Uma política madura pode ser:

```text
Erro crítico       → 100%
Violação           → 100%
Ação sensível      → 100%
Execução normal    → sampling
Conteúdo completo  → opt-in/policy
```

---

# 33. Retenção

A retenção deve depender do tipo de evidência.

Exemplo conceitual:

| Dado                | Retenção             |
| ------------------- | -------------------- |
| Métricas agregadas  | longa                |
| Trace metadata      | média/longa          |
| Erros críticos      | longa                |
| Auditoria           | conforme política    |
| Prompt completo     | curta/controlada     |
| Output completo     | curta/controlada     |
| PII                 | mínimo necessário    |
| Dados experimentais | conforme experimento |

A política real deve ser definida pelo risco, finalidade e requisitos legais/organizacionais.

---

# 34. Redaction

Antes de persistir conteúdo, avaliar:

```text
PII
credentials
API keys
tokens
financial data
secrets
personal documents
confidential business data
```

Possíveis estratégias:

```text
remove
mask
hash
tokenize
truncate
reference
encrypt
```

Nunca assumir:

> “é apenas um log”.

Um log pode se tornar uma segunda cópia do banco de dados.

---

# 35. Integridade

Logs de alto valor podem precisar de mecanismos de integridade.

Possibilidades:

```text
hash
checksum
append-only storage
signed records
immutable storage
versioning
timestamping
```

Para evidência crítica:

```text
event
  ↓
canonicalization
  ↓
hash
  ↓
immutable record
```

---

# 36. Log levels

Uma taxonomia simples:

### DEBUG

Detalhes para desenvolvimento.

### INFO

Eventos operacionais normais.

### WARN

Comportamento inesperado sem falha completa.

### ERROR

Falha operacional.

### CRITICAL

Falha que ameaça integridade, segurança ou objetivo crítico.

### AUDIT

Registro destinado à rastreabilidade de ações relevantes.

### EVALUATION

Resultado de avaliação.

Não utilizar níveis de severidade apenas como decoração.

---

# 37. Logs como memória operacional

Logs não devem ser automaticamente tratados como memória do agente.

São coisas diferentes:

```text
LOG
↓
evidência histórica

MEMORY
↓
conhecimento/contexto reutilizável
```

Pode existir um pipeline:

```text
Logs
  ↓
Analysis
  ↓
Pattern Detection
  ↓
Knowledge Candidate
  ↓
Validation
  ↓
Memory / Knowledge Base
```

Portanto:

> Log ≠ Memory.

---

# 38. Logs como fonte de aprendizado

Uma execução problemática pode alimentar um ciclo:

```text
Execution
    ↓
Trace
    ↓
Failure
    ↓
Human/Automated Analysis
    ↓
Failure Taxonomy
    ↓
Evaluation
    ↓
Regression Case
    ↓
Harness Improvement
```

Esse é um dos usos mais valiosos dos logs.

---

# 39. Logs → Evaluation

Um sistema maduro não apenas armazena traces.

Ele utiliza traces para avaliação.

Exemplo:

```text
TRACE
 │
 ├── outcome
 ├── tool selection
 ├── retrieval
 ├── state transitions
 ├── policy compliance
 └── final response
       │
       ▼
     EVAL
       │
       ├── pass
       ├── fail
       └── uncertain
```

A avaliação deve ocorrer no menor nível que contenha evidência suficiente.

```text
Span
Trace
Session
```

---

# 40. Code Evaluation

Usar avaliação determinística quando possível.

Exemplos:

```text
tool correto?
schema válido?
campo obrigatório presente?
invariante satisfeito?
timeout respeitado?
número de retries <= limite?
ação autorizada?
```

Preferir:

```text
if condition:
    PASS
else:
    FAIL
```

em vez de utilizar LLM para algo objetivamente verificável.

---

# 41. LLM-as-Judge

Usar quando o critério é semântico.

Exemplos:

```text
resposta útil?
argumentação coerente?
síntese fiel?
explicação suficiente?
```

O judge também precisa ser avaliado.

Nunca tratar:

```text
LLM judge = verdade
```

como axioma.

---

# 42. Human Review

Para casos de alto impacto:

```text
Trace
  ↓
Automated Eval
  ↓
Human Review
```

A revisão humana pode servir para:

* validar avaliadores
* criar datasets
* resolver casos ambíguos
* identificar novas classes de falha

---

# 43. Failure Taxonomy

O sistema deve evoluir uma taxonomia de falhas.

Exemplo:

```text
F01 Context Failure
F02 Retrieval Failure
F03 Tool Selection Failure
F04 Tool Execution Failure
F05 Reasoning/Decision Failure
F06 Policy Failure
F07 State Failure
F08 Handoff Failure
F09 Loop Failure
F10 Output Failure
F11 Evaluation Failure
F12 Infrastructure Failure
```

A taxonomia deve ser evolutiva.

Não criar dezenas de categorias antes de observar o sistema real.

---

# 44. Logs e Harness

O Harness deve utilizar logs como mecanismo de observação da execução.

Arquitetura:

```text
                HARNESS
                   │
       ┌───────────┼───────────┐
       │           │           │
   Constraints   Tools      Context
       │           │           │
       └───────────┼───────────┘
                   │
                 AGENT
                   │
              TELEMETRY
                   │
       ┌───────────┼───────────┐
       │           │           │
     Trace       Logs       Metrics
       │           │           │
       └───────────┼───────────┘
                   │
                EVALS
                   │
              REGRESSION
                   │
               HARNESS
               IMPROVEMENT
```

---

# 45. Harness deve registrar seu próprio comportamento

Não observar apenas o agente.

Observar também:

```text
prompt loading
skill loading
context assembly
policy application
tool registration
tool authorization
memory retrieval
memory write
validation
quality gates
approval gates
termination
```

Caso contrário, quando o agente falhar, será impossível determinar se o problema veio:

```text
modelo
prompt
skill
contexto
tool
RAG
memory
harness
policy
runtime
```

---

# 46. Log do Harness

Exemplo:

```json
{
  "event": "harness.context.loaded",
  "harness_version": "1.4.0",
  "spec_version": "SPEC-002",
  "skills": [
    "skill-a",
    "skill-b"
  ],
  "policy_set": "policy-v12",
  "context_hash": "sha256:..."
}
```

Esse tipo de registro permite comparar duas execuções.

---

# 47. Reprodutibilidade

Uma execução agentic dificilmente será deterministicamente reproduzível apenas pelo prompt.

Por isso, registrar:

```text
model
model version
prompt version
skill versions
harness version
configuration
tool versions
retrieval sources
context references
policy versions
environment
```

O objetivo é permitir:

> reconstruir as condições da execução.

Não necessariamente reproduzir bit-a-bit o resultado.

---

# 48. Causal reconstruction

O sistema deve permitir reconstruir uma cadeia aproximada:

```text
INPUT
 ↓
CONTEXT
 ↓
MODEL
 ↓
DECISION
 ↓
TOOL
 ↓
RESULT
 ↓
NEW CONTEXT
 ↓
MODEL
 ↓
DECISION
 ↓
OUTCOME
```

Esse é o nível de observabilidade necessário para investigar agentes complexos.

---

# 49. Não registrar chain-of-thought como requisito

O sistema não deve depender da captura de raciocínio privado completo para explicar uma execução.

Priorizar:

```text
decisão operacional
evidência utilizada
ação executada
resultado observado
política aplicável
estado antes/depois
```

Isso fornece explicabilidade operacional sem transformar o sistema em dependente de conteúdo interno de raciocínio.

---

# 50. Event Sourcing parcial

Para workflows críticos, pode ser útil tratar eventos de mudança de estado como uma sequência:

```text
STATE_0
 ↓
event
 ↓
STATE_1
 ↓
event
 ↓
STATE_2
```

Isso permite reconstruir a evolução operacional.

Não significa que todo agente precise implementar Event Sourcing completo.

---

# 51. Logs como contrato observável

Uma especificação de agente pode declarar:

```text
The agent MUST emit:
    agent.run.started
    agent.run.completed
    tool.called
    tool.completed
    error
    state.changed
```

Isso transforma logging em comportamento verificável.

---

# 52. Logging como Acceptance Criterion

Exemplo:

```text
AC-LOG-001

Given an agent execution
When the agent invokes a tool
Then the system MUST emit a structured tool-call record
containing:
- trace correlation
- agent identity
- tool identity
- execution status
- timing
```

Esse AC pode ser testado.

---

# 53. Logging não deve ser critério de qualidade isolado

Evitar:

```text
"tem muitos logs"
=
"agente melhor"
```

A pergunta correta:

> Os logs permitem explicar, detectar, avaliar e melhorar o comportamento?

---

# 54. Métricas essenciais

## Reliability

```text
success_rate
failure_rate
tool_failure_rate
retry_rate
loop_rate
timeout_rate
```

## Performance

```text
latency_p50
latency_p95
latency_p99
tool_latency
model_latency
retrieval_latency
```

## Cost

```text
input_tokens
output_tokens
total_tokens
cost_per_run
cost_per_success
```

## Agent behavior

```text
tool_calls_per_run
iterations_per_run
handoffs_per_run
retrievals_per_run
context_utilization
```

## Quality

```text
evaluation_pass_rate
policy_compliance
invariant_violation_rate
human_review_rate
regression_rate
```

---

# 55. Métrica especialmente importante

Não observar apenas:

```text
cost / run
```

Preferir quando possível:

```text
cost / successful task
```

Porque um agente barato que falha constantemente pode ser economicamente pior que um agente mais caro que conclui corretamente.

---

# 56. Latência também deve ser contextualizada

Não basta:

```text
latency = 30s
```

Deve ser possível saber:

```text
30s
 ├── LLM 1 = 3s
 ├── Tool = 10s
 ├── Retrieval = 2s
 ├── Retry = 8s
 └── LLM 2 = 7s
```

Essa decomposição transforma observabilidade em capacidade de otimização.

---

# 57. Benchmark de maturidade

## Nível 0 — Invisible Agent

```text
final output only
```

Não recomendado para produção relevante.

---

## Nível 1 — Basic Logging

```text
start
error
finish
```

Serve para debugging básico.

---

## Nível 2 — Structured Logging

```text
JSON
timestamps
agent_id
run_id
status
errors
```

Base mínima profissional.

---

## Nível 3 — Distributed Tracing

```text
trace
spans
tool calls
LLM calls
retrieval
handoffs
```

Base recomendada para agentes complexos.

---

## Nível 4 — Evaluated Observability

```text
traces
+
evaluations
+
failure taxonomy
+
datasets
```

Permite melhoria sistemática.

---

## Nível 5 — Governed Agent Observability

```text
observability
+
invariants
+
policies
+
audit
+
security
+
regression
+
continuous improvement
```

É o nível apropriado para Harnesses maduros.

---

# 58. Benchmark de qualidade do log

Um sistema de logs deve ser avaliado por:

| Dimensão     | Pergunta                                  |
| ------------ | ----------------------------------------- |
| Completeness | Temos evidência suficiente?               |
| Correlation  | Conseguimos reconstruir a execução?       |
| Accuracy     | O log representa o que realmente ocorreu? |
| Timeliness   | O evento possui timestamp adequado?       |
| Semantics    | O significado é claro?                    |
| Queryability | Conseguimos pesquisar?                    |
| Security     | Dados sensíveis estão protegidos?         |
| Integrity    | Evidência crítica pode ser adulterada?    |
| Cost         | O valor justifica o armazenamento?        |
| Noise        | Há informação inútil demais?              |
| Evaluation   | O trace pode alimentar avaliações?        |
| Regression   | Falhas podem virar casos de regressão?    |

---

# 59. Critério de Sufficiency

Um bom sistema de logging não precisa registrar tudo.

Deve atingir:

```text
Minimum Sufficient Evidence
```

Definição:

> Conjunto mínimo de evidências capaz de explicar o comportamento relevante, verificar invariantes, diagnosticar falhas e alimentar avaliação.

---

# 60. Anti-patterns

## Anti-pattern 1

```text
print("Agent started")
```

Problema:

Sem estrutura e correlação.

---

## Anti-pattern 2

Registrar apenas o output final.

Problema:

Perde o caminho.

---

## Anti-pattern 3

Um único trace para todo o loop.

Problema:

Esconde decisões intermediárias.

---

## Anti-pattern 4

Registrar absolutamente tudo.

Problema:

Custo + ruído + risco.

---

## Anti-pattern 5

Guardar prompts sem governança.

Problema:

Possível exposição de dados sensíveis.

---

## Anti-pattern 6

Usar LLM para todas as avaliações.

Problema:

Custo + variabilidade + dificuldade de validação.

---

## Anti-pattern 7

Logs sem versionamento.

Problema:

Impossibilidade de interpretar historicamente.

---

## Anti-pattern 8

Logs sem correlação.

Problema:

Não é possível reconstruir causalmente a execução.

---

## Anti-pattern 9

Logs que descrevem intenção mas não ação.

Exemplo:

```text
Agent decided to execute trade
```

sem evidência de:

```text
tool call
authorization
execution result
```

Problema:

intenção não é execução.

---

# 61. Princípio crítico: intenção ≠ ação

Em agentes:

```text
LLM OUTPUT
      ≠
SYSTEM ACTION
```

A ação real deve ser observada no ponto de execução.

Exemplo:

```text
Agent requested:
    execute_operation

Authorization:
    ALLOWED

Tool:
    execute_operation

System:
    SUCCESS
```

Isso é muito mais forte que:

```text
Agent said:
    "Operation executed successfully."
```

---

# 62. Observabilidade de resultado externo

Sempre que possível, validar o resultado no sistema que efetivamente executou a ação.

Exemplo:

```text
Agent
 ↓
Tool
 ↓
External System
 ↓
Actual Result
```

O log deve diferenciar:

```text
requested
accepted
executed
confirmed
failed
unknown
```

---

# 63. Estados de resultado

Recomendação:

```text
REQUESTED
AUTHORIZED
STARTED
SUCCEEDED
FAILED
REJECTED
TIMEOUT
UNKNOWN
```

Isso evita o erro:

```text
tool call returned
=
action succeeded
```

---

# 64. Logs e segurança

Logging deve participar da estratégia de segurança.

Monitorar:

```text
prompt injection indicators
unexpected tool calls
authorization failures
policy violations
credential exposure
data exfiltration indicators
abnormal iteration counts
abnormal tool frequency
unexpected destinations
```

Entretanto:

> observabilidade detecta e evidencia; enforcement deve ocorrer no ponto de controle.

---

# 65. Logs e Prompt Injection

Um evento pode registrar:

```text
security.signal.detected
```

com:

```text
signal_type
source
severity
action_taken
policy_reference
trace_id
```

Não é necessário armazenar todo conteúdo potencialmente sensível.

---

# 66. Logs e mudanças de Harness

Toda mudança relevante deve ser correlacionável:

```text
harness_version
prompt_version
skill_version
policy_version
tool_version
model_version
```

Isso permite comparar:

```text
Before
vs
After
```

---

# 67. Experimentos

Experimentos devem possuir:

```text
experiment_id
variant
baseline
hypothesis
agent_version
harness_version
dataset_version
evaluation_version
```

Assim:

```text
Trace
 ↓
Experiment
 ↓
Evaluation
 ↓
Comparison
```

---

# 68. Regression Loop

Falha observada:

```text
TRACE-123
```

vira:

```text
CASE-123
```

Depois:

```text
REGRESSION-123
```

A melhoria só é considerada consolidada quando:

```text
old failure
↓
harness change
↓
regression test
↓
pass
```

---

# 69. Benchmark operacional

Um Harness maduro deve conseguir responder:

### Antes da mudança

```text
success = 81%
cost/success = X
latency p95 = Y
tool failures = Z
```

### Depois da mudança

```text
success = ...
cost/success = ...
latency p95 = ...
tool failures = ...
```

Sem essa evidência, melhoria de agente vira opinião.

---

# 70. Observability → Evaluation → Improvement

O ciclo recomendado:

```text
1. Instrument
       ↓
2. Observe
       ↓
3. Trace
       ↓
4. Inspect
       ↓
5. Classify failure
       ↓
6. Evaluate
       ↓
7. Create regression case
       ↓
8. Change harness
       ↓
9. Re-run
       ↓
10. Compare
```

---

# 71. Regra de ouro

> **Não adicionar um log porque “pode ser útil”. Adicionar porque existe uma pergunta operacional, de segurança, qualidade ou engenharia que aquele dado permite responder.**

---

# 72. Decision Record

Toda nova categoria de log deveria responder:

```text
WHY:
Qual pergunta este dado responde?

WHAT:
Qual informação será registrada?

WHERE:
Em qual operação?

WHEN:
Em qual evento?

WHO:
Quem pode acessar?

RETENTION:
Por quanto tempo?

RISK:
Qual o risco de registrar?

COST:
Qual o custo?

VALUE:
Qual decisão poderá ser tomada com esse dado?
```

Se não houver resposta clara:

```text
DO NOT LOG
```

---

# 73. Contract de logging

Um agente pode declarar um contrato:

```text
LOGGING CONTRACT

The agent MUST emit:
- run.started
- run.completed
- generation
- tool.call
- tool.result
- state.changed
- error

The agent SHOULD emit:
- decision
- retrieval
- handoff
- checkpoint

The agent MAY emit:
- debug details

The agent MUST NOT emit:
- credentials
- secrets
- prohibited sensitive data
```

---

# 74. Quality Gate

Antes de considerar um agente observável:

### G1 — Correlation

* [ ] run possui ID
* [ ] trace possui ID
* [ ] spans possuem parent
* [ ] logs podem ser correlacionados

### G2 — Execution

* [ ] LLM calls observáveis
* [ ] tool calls observáveis
* [ ] retrieval observável
* [ ] handoffs observáveis

### G3 — State

* [ ] estados críticos observáveis
* [ ] transições críticas observáveis

### G4 — Failure

* [ ] erros estruturados
* [ ] retries observáveis
* [ ] loops detectáveis

### G5 — Security

* [ ] secrets protegidos
* [ ] PII governada
* [ ] autorização observável
* [ ] ações críticas auditáveis

### G6 — Evaluation

* [ ] traces podem alimentar evals
* [ ] failures podem virar datasets
* [ ] regressões podem ser verificadas

### G7 — Economics

* [ ] sampling definido
* [ ] retenção definida
* [ ] custo monitorado
* [ ] ruído controlado

---

# 75. Benchmark contra o estado da arte

A arquitetura deste documento se alinha aos principais padrões observados no ecossistema atual:

```text
OpenTelemetry
    ↓
telemetry standardization

OpenInference / GenAI conventions
    ↓
AI-specific semantics

Langfuse
    ↓
trace → evaluation → dataset → experiment

Arize / Phoenix
    ↓
trace → annotation → hypothesis → experiment

OWASP
    ↓
security monitoring + downstream enforcement

NIST AI RMF
    ↓
risk management + measurement + governance
```

A convergência importante é:

> **Observabilidade deixa de ser uma atividade posterior à construção do agente e passa a fazer parte do próprio Agent Engineering Lifecycle.**

---

# 76. Modelo de referência para AXL/Agent Harness

Para um Harness de engenharia de agentes, recomenda-se:

```text
                HUMAN
                  │
                  ▼
             SPEC / TASK
                  │
                  ▼
              HARNESS
       ┌──────────┼──────────┐
       │          │          │
    Context     Skills     Policies
       │          │          │
       └──────────┼──────────┘
                  ▼
                AGENT
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
       LLM      TOOLS      RAG
        │         │         │
        └─────────┼─────────┘
                  ▼
              TELEMETRY
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      TRACE      LOGS     METRICS
        │         │         │
        └─────────┼─────────┘
                  ▼
                EVAL
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
     PASS                 FAILURE
                            │
                            ▼
                       REGRESSION
                            │
                            ▼
                    HARNESS IMPROVEMENT
```

---

# 77. Princípio arquitetural final

O sistema deve separar quatro coisas:

```text
EXECUTION
    ↓
OBSERVATION
    ↓
EVALUATION
    ↓
GOVERNANCE
```

Não confundir:

```text
log ≠ avaliação
trace ≠ julgamento
evaluation ≠ enforcement
enforcement ≠ logging
```

Cada camada possui função própria.

---

# 78. Definição final

Um sistema de logging de agente é considerado **maduro** quando:

> consegue reconstruir uma execução relevante a partir de evidências estruturadas, correlacionar modelo, contexto, ferramentas, estado e resultado, detectar falhas e violações, alimentar avaliações e regressões, preservar segurança e privacidade, e fazê-lo com custo e volume proporcionais ao valor operacional da informação.

---

# 79. Regra de ouro do Master Document

```text
LOG THE EVIDENCE
NOT THE NOISE.
```

Ou, operacionalmente:

```text
Se o registro não permite:
    explicar
    detectar
    avaliar
    proteger
    ou melhorar

a execução,

questionar se ele precisa existir.
```

---

# 80. Referenciais normativos e benchmarks considerados

Este Master Document deve ser mantido alinhado, quando aplicável, com:

* OpenTelemetry
* OpenTelemetry Semantic Conventions
* OpenTelemetry GenAI Semantic Conventions
* OpenInference
* Langfuse Observability / Evaluation
* Arize Phoenix / Agent Observability
* OWASP GenAI Security
* NIST AI Risk Management Framework
* práticas de Agent Evaluation e Regression Testing
* práticas de Harness Engineering

As tecnologias específicas podem mudar.

Os princípios de:

```text
correlation
structured telemetry
traceability
evaluation
security
regression
cost control
```

devem permanecer independentes do fornecedor.

---

# 81. Status de adoção recomendado

Para um projeto em desenvolvimento:

### Fase 1

```text
run_id
trace_id
agent_id
agent_version
status
duration
errors
```

### Fase 2

```text
LLM spans
tool spans
retrieval spans
state events
token/cost metrics
```

### Fase 3

```text
policy events
invariant violations
handoffs
evaluation
failure taxonomy
```

### Fase 4

```text
regression datasets
continuous evaluation
sampling
retention governance
security monitoring
```

### Fase 5

```text
observability-driven harness improvement
```

A progressão deve ocorrer conforme o valor produzido pela observabilidade, e não por completude burocrática.

---

# 82. Princípio de economicidade

A arquitetura deve obedecer a três critérios:

```text
EFICIÊNCIA
registrar com baixo custo

EFICÁCIA
registrar o que permite investigar

EFETIVIDADE / ECONOMICIDADE
registrar somente o que melhora decisões,
segurança, qualidade ou evolução do agente
```

A meta não é possuir o maior volume de telemetria.

A meta é possuir a **melhor relação entre evidência e custo**.

---

# 83. Resultado esperado

Ao final, diante de qualquer execução relevante, um engenheiro deve conseguir abrir o trace e responder:

```text
O que aconteceu?
        ↓
Onde aconteceu?
        ↓
Quando aconteceu?
        ↓
Qual agente estava executando?
        ↓
Qual Harness estava ativo?
        ↓
Qual contexto estava disponível?
        ↓
Qual modelo foi utilizado?
        ↓
Qual ferramenta foi acionada?
        ↓
Qual resultado foi recebido?
        ↓
Qual estado mudou?
        ↓
Qual política foi aplicada?
        ↓
Qual invariante foi satisfeito/violado?
        ↓
Qual foi o resultado real?
        ↓
O agente atingiu o objetivo?
        ↓
Quanto custou?
        ↓
O comportamento deve ser mantido?
        ↓
Ou deve virar caso de melhoria/regressão?
```

**Esse é o padrão de observabilidade que transforma logs de “mensagens de debug” em infraestrutura de engenharia de agentes.**
