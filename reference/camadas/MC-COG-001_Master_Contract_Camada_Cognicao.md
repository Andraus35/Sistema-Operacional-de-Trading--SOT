# MC-COG-001 — Master Contract da Camada de Cognição

**Sistema:** SOT — System of Thought  
**Camada:** Cognição  
**Versão:** 1.0  
**Status:** Baseline de especificação  
**Natureza:** Arquitetura, contratos, especificações e Harness  
**Escopo:** Geral, aplicável a LLMs e agentes, sem acoplamento tecnológico

---

# 1. Finalidade

Este Master Contract define a **Camada de Cognição** como a capacidade responsável por transformar conhecimento, evidências, contexto, experiência e hipóteses em **processos de análise e inferência controláveis**, preservando a liberdade cognitiva do LLM enquanto obriga o atendimento de invariantes.

A camada deve maximizar:

- **Eficácia:** qualidade das inferências e análises.
- **Eficiência:** uso adequado de etapas cognitivas e contexto.
- **Efetividade:** capacidade de produzir entendimento útil para a missão.
- **Economicidade:** qualidade cognitiva obtida por unidade de recurso.

O Harness não deve prescrever uma única forma de pensar. Deve especificar **condições que uma boa cognição deve satisfazer**, permitindo que o modelo escolha a estratégia interna mais adequada.

---

# 2. Identidade da Camada

## 2.1 A Cognição é responsável por

1. interpretar o problema;
2. estruturar o objeto de análise;
3. formular hipóteses;
4. explorar hipóteses concorrentes;
5. relacionar evidências;
6. identificar contraevidências;
7. raciocinar sobre causalidade quando pertinente;
8. trabalhar com incerteza;
9. comparar explicações;
10. atualizar crenças;
11. detectar inconsistências;
12. avaliar consequências;
13. produzir conclusões condicionais;
14. explicitar limitações;
15. registrar traços cognitivos relevantes para auditoria.

## 2.2 A Cognição não é

- banco de conhecimento;
- RAG;
- memória;
- experiência;
- aprendizado;
- governança;
- decisão operacional;
- executor;
- autoridade sobre a realidade externa.

---

# 3. Princípio Central

A arquitetura deve adotar:

> **Liberdade cognitiva + obrigação de satisfazer invariantes.**

O Harness não deve exigir uma sequência rígida de raciocínio interno.

Ele deve exigir propriedades observáveis do resultado cognitivo.

Exemplo:

```text
NÃO:
"o modelo deve pensar em exatamente 7 etapas"

SIM:
"a conclusão deve possuir suporte identificável,
incerteza compatível e ausência de contradição crítica não tratada"
```

---

# 4. Princípios da Cognição

### COG-P01 — Liberdade Cognitiva
O modelo pode escolher a estratégia de raciocínio adequada.

### COG-P02 — Invariantes Cognitivos
A liberdade não elimina condições mínimas de qualidade.

### COG-P03 — Hipótese antes da conclusão
Quando a tarefa for inferencial, hipóteses devem poder ser distinguidas de conclusões.

### COG-P04 — Alternativas
Quando houver ambiguidade material, hipóteses alternativas devem ser consideradas.

### COG-P05 — Evidência
Afirmações relevantes devem possuir suporte apropriado.

### COG-P06 — Contraevidência
Evidência que contradiga uma hipótese relevante não pode ser ignorada silenciosamente.

### COG-P07 — Incerteza
A confiança declarada deve ser compatível com a qualidade da evidência.

### COG-P08 — Atualização
Novas evidências devem poder alterar hipóteses anteriores.

### COG-P09 — Não fechamento prematuro
O sistema deve evitar concluir quando a evidência ainda é insuficiente.

### COG-P10 — Separação
Fato, observação, inferência, hipótese, previsão e decisão devem ser distinguíveis.

### COG-P11 — Coerência
A conclusão não deve contradizer premissas aceitas sem explicação.

### COG-P12 — Rastreabilidade
Inferências críticas devem possuir rastreabilidade suficiente para avaliação.

### COG-P13 — Metacognição
O sistema deve poder avaliar limitações, conflitos e qualidade de sua própria análise.

### COG-P14 — Especialização
Conhecimento especializado deve modificar a análise sem eliminar princípios cognitivos gerais.

### COG-P15 — Conservação da Incerteza
A transformação de evidência em conclusão não deve artificialmente aumentar certeza.

---

# 5. Modelo Cognitivo Geral

```text
Objetivo
   ↓
Interpretação
   ↓
Representação do problema
   ↓
Estado de conhecimento
   ↓
Hipóteses
   ↓
Busca / recuperação de evidências
   ↓
Análise
   ↓
Contraevidência
   ↓
Comparação
   ↓
Atualização
   ↓
Inferência
   ↓
Incerteza
   ↓
Conclusão
   ↓
Metacognição
   ↓
Saída cognitiva
```

A ordem acima é **modelo arquitetural**, não uma obrigação de execução literal.

---

# 6. Unidade Cognitiva

A menor unidade relevante deve ser capaz de representar:

```yaml
cognitive_unit_id:
objective:
question:
context:
observations:
facts:
assumptions:
hypotheses:
evidence:
counterevidence:
relationships:
inferences:
uncertainty:
confidence:
alternatives:
contradictions:
conclusion:
limitations:
metacognitive_assessment:
provenance:
version:
```

---

# 7. Estados Cognitivos

Uma hipótese ou interpretação pode atravessar:

```text
CREATED
   ↓
ANALYZED
   ↓
PARTIALLY_VALIDATED
   ↓
MONITORED
   ↓
STRENGTHENED
   ↓
PRINCIPAL
```

ou:

```text
CREATED → ANALYZED → REFUTED → ARCHIVED
```

ou:

```text
CREATED → ANALYZED → INCONCLUSIVE → MONITORED
```

Nenhum estado deve ser inferido apenas pela passagem do tempo.

---

# 8. Especificações a serem desenvolvidas

## Grupo A — Fundamentos

### COG-SPEC-001 — Cognitive Capability Contract
Deve definir identidade, entradas, saídas, limites, responsabilidades e invariantes.

**Aceitação:** qualquer consumidor consegue determinar o papel da cognição.

### COG-SPEC-002 — Cognitive Task Model
Deve classificar tarefas cognitivas.

Categorias mínimas:

- compreensão;
- explicação;
- comparação;
- diagnóstico;
- inferência;
- previsão;
- planejamento;
- avaliação;
- decisão preparatória.

**Aceitação:** tarefas cognitivamente diferentes podem receber tratamento apropriado.

### COG-SPEC-003 — Problem Representation
Deve definir como o problema é representado antes da inferência.

**Aceitação:** a análise consegue distinguir objetivo, contexto, restrições e incógnitas.

### COG-SPEC-004 — Cognitive State Model
Deve especificar estados e transições cognitivas.

**Aceitação:** hipóteses e conclusões possuem estado identificável.

### COG-SPEC-005 — Cognitive Unit
Deve definir a unidade mínima de representação cognitiva.

**Aceitação:** uma análise relevante pode ser reconstruída a partir de unidades rastreáveis.

---

# 9. Hipóteses e Alternativas

### COG-SPEC-006 — Hypothesis Formation
Deve especificar formação de hipóteses sem confundi-las com fatos.

### COG-SPEC-007 — Hypothesis Competition
Deve permitir hipóteses concorrentes.

### COG-SPEC-008 — Alternative Explanation
Deve exigir alternativas quando a ambiguidade for material.

### COG-SPEC-009 — Hypothesis Evaluation
Deve definir avaliação por evidência, coerência, poder explicativo e incerteza.

### COG-SPEC-010 — Hypothesis Invalidation
Deve definir condições capazes de enfraquecer ou refutar uma hipótese.

**Invariante:**

> Uma hipótese não pode tornar-se verdadeira apenas por repetição dentro do contexto.

---

# 10. Evidência e Inferência

### COG-SPEC-011 — Evidence-to-Inference Mapping
Deve mapear quais evidências sustentam quais inferências.

### COG-SPEC-012 — Counterevidence Handling
Deve representar evidências contrárias.

### COG-SPEC-013 — Evidence Sufficiency
Deve avaliar se existe suporte suficiente para determinada conclusão.

### COG-SPEC-014 — Inference Strength
Deve classificar força inferencial sem transformar classificação em certeza absoluta.

### COG-SPEC-015 — Unsupported Inference Detection
Deve detectar conclusões sem suporte proporcional.

### COG-SPEC-016 — Contradiction Handling
Deve identificar contradições entre:

- fatos;
- premissas;
- hipóteses;
- evidências;
- conclusões.

---

# 11. Causalidade

### COG-SPEC-017 — Causal Reasoning Contract
Deve definir quando uma relação causal pode ser considerada.

### COG-SPEC-018 — Correlation vs Causation
Deve impedir que associação seja automaticamente tratada como causalidade.

### COG-SPEC-019 — Causal Mechanism
Deve representar mecanismo causal quando necessário.

### COG-SPEC-020 — Causal Counterfactual
Deve permitir avaliação de consequências condicionais.

### COG-SPEC-021 — Causal Uncertainty
Deve representar incerteza sobre mecanismos causais.

---

# 12. Contrafactuais

### COG-SPEC-022 — Counterfactual Generation
Deve permitir construção de cenários alternativos.

### COG-SPEC-023 — Counterfactual Validity
Deve verificar compatibilidade do cenário alternativo com as premissas.

### COG-SPEC-024 — Counterfactual Comparison
Deve comparar cenário observado e cenário alternativo.

### COG-SPEC-025 — Counterfactual Boundary
Deve impedir extrapolações incompatíveis com evidência disponível.

---

# 13. Incerteza

### COG-SPEC-026 — Uncertainty Model
Deve representar tipos distintos de incerteza.

Mínimo:

- incerteza factual;
- incerteza epistemológica;
- incerteza causal;
- incerteza temporal;
- incerteza de modelo;
- incerteza de medição;
- incerteza de previsão.

### COG-SPEC-027 — Confidence Calibration
Deve avaliar compatibilidade entre confiança declarada e evidência.

### COG-SPEC-028 — Uncertainty Propagation
Deve impedir que incertezas desapareçam durante a cadeia inferencial.

### COG-SPEC-029 — Unknown State
Deve permitir representar explicitamente:

> desconhecido / insuficiente / não determinável.

### COG-SPEC-030 — Confidence Revision
Deve permitir atualização da confiança diante de novas evidências.

---

# 14. Camada Semântica e Ontológica

### COG-SPEC-031 — Semantic Interpretation
Deve especificar interpretação contextual de termos e relações.

### COG-SPEC-032 — Ontological Alignment
Deve alinhar entidades, propriedades e relações utilizadas pela análise.

### COG-SPEC-033 — Concept Disambiguation
Deve detectar termos semanticamente ambíguos.

### COG-SPEC-034 — Semantic Consistency
Deve detectar mudanças de significado durante o raciocínio.

---

# 15. Raciocínio Probabilístico

### COG-SPEC-035 — Probabilistic Reasoning Contract
Deve definir uso de probabilidades quando apropriado.

### COG-SPEC-036 — Prior and Evidence
Deve distinguir crença prévia de atualização por evidência.

### COG-SPEC-037 — Bayesian Updating
Deve permitir atualização probabilística quando o problema comportar esse modelo.

### COG-SPEC-038 — Probability Calibration
Deve avaliar calibração das probabilidades declaradas.

### COG-SPEC-039 — Probabilistic Dependency
Deve evitar contagem dupla de evidências dependentes.

---

# 16. Cognição Decisional

### COG-SPEC-040 — Decision Preparation
Deve estruturar informações para uma decisão sem confundir análise com autoridade decisional.

### COG-SPEC-041 — Option Evaluation
Deve permitir comparação de alternativas segundo critérios explicitados.

### COG-SPEC-042 — Consequence Analysis
Deve avaliar consequências diretas e de segunda ordem.

### COG-SPEC-043 — Risk Analysis
Deve representar:

- probabilidade;
- impacto;
- exposição;
- incerteza;
- reversibilidade.

### COG-SPEC-044 — Decision Boundary
Deve definir quando a evidência é insuficiente para sustentar uma decisão.

---

# 17. Metacognição

### COG-SPEC-045 — Metacognitive Assessment
Deve avaliar a própria análise.

### COG-SPEC-046 — Blind Spot Detection
Deve procurar:

- premissas ocultas;
- evidências ausentes;
- alternativas não exploradas;
- contradições;
- dependências;
- excesso de confiança.

### COG-SPEC-047 — Cognitive Failure Detection
Deve classificar falhas cognitivas.

### COG-SPEC-048 — Self-Correction
Deve permitir revisão da análise quando um erro for identificado.

### COG-SPEC-049 — Epistemic Status
Deve identificar o status de cada elemento:

- observado;
- informado;
- inferido;
- hipotético;
- previsto;
- desconhecido.

---

# 18. Integração

### COG-SPEC-050 — Cognition-to-RAG Contract
Define como cognição solicita evidências ao RAG.

**Invariante:** cognição pode pedir mais evidência, mas não pode alterar a proveniência.

### COG-SPEC-051 — Cognition-to-Experience Contract
Define uso de experiências históricas.

### COG-SPEC-052 — Cognition-to-Learning Contract
Define como erros e descobertas podem gerar candidatos de aprendizado.

### COG-SPEC-053 — Cognition-to-Governance Contract
Define quais resultados cognitivos podem gerar propostas de mudança.

### COG-SPEC-054 — Skill-to-Cognition Contract
Define como habilidades especializadas introduzem conhecimento de domínio sem dominar a cognição geral.

---

# 19. Saída Cognitiva

### COG-SPEC-055 — Cognitive Output Contract
Deve definir a estrutura mínima da saída.

```yaml
objective:
interpretation:
observations:
assumptions:
hypotheses:
evidence:
counterevidence:
analysis:
alternatives:
uncertainty:
confidence:
conclusion:
limitations:
open_questions:
metacognitive_assessment:
provenance:
version:
```

A saída não precisa expor o raciocínio interno completo do modelo. Deve expor **informações suficientes para avaliar a qualidade cognitiva**.

---

# 20. Harness da Cognição

### COG-SPEC-056 — Cognitive Harness

O Harness deve testar propriedades cognitivas, não impor uma cadeia única de pensamento.

## Sensores determinísticos

- presença de hipóteses;
- presença de evidência;
- presença de incerteza;
- identificação de contradições;
- consistência estrutural;
- rastreabilidade;
- separação entre fato e inferência;
- estado cognitivo;
- versão.

## Sensores inferenciais

- coerência;
- suficiência;
- qualidade da hipótese;
- consideração de alternativas;
- tratamento de contraevidência;
- calibração de confiança;
- consistência causal;
- consistência probabilística;
- qualidade metacognitiva.

## Testes

- hypothesis tests;
- counterevidence tests;
- contradiction tests;
- uncertainty tests;
- calibration tests;
- causal reasoning tests;
- counterfactual tests;
- semantic consistency tests;
- adversarial reasoning;
- ambiguity tests;
- regression tests.

---

# 21. Invariantes Cognitivos

```text
I-COG-01:
Uma conclusão não pode ser apresentada como fato apenas porque foi inferida.

I-COG-02:
Evidência relevante contra uma hipótese não pode ser silenciosamente descartada.

I-COG-03:
Ausência de evidência não equivale a evidência de ausência.

I-COG-04:
Incerteza não pode ser eliminada apenas para produzir uma resposta mais assertiva.

I-COG-05:
Hipóteses concorrentes devem permanecer possíveis enquanto não forem adequadamente discriminadas.

I-COG-06:
Correlação não deve ser convertida automaticamente em causalidade.

I-COG-07:
Uma mudança de premissa deve poder produzir mudança de conclusão.

I-COG-08:
A cognição deve poder representar desconhecimento.

I-COG-09:
Confiança deve ser proporcional ao suporte disponível.

I-COG-10:
Especialização de domínio não deve eliminar mecanismos cognitivos gerais.

I-COG-11:
Feedback pode provocar revisão, mas não pode fabricar evidência.

I-COG-12:
O Harness deve avaliar propriedades cognitivas sem exigir uma única estratégia interna de raciocínio.
```

---

# 22. Quality Gates

### G0 — Cognitive Contract
Identidade e limites definidos.

### G1 — Representation Integrity
Problema, contexto e objetivo corretamente representados.

### G2 — Hypothesis Integrity
Hipóteses distinguíveis de fatos e conclusões.

### G3 — Evidence Integrity
Evidências e contraevidências rastreáveis.

### G4 — Inference Integrity
Inferências proporcionais ao suporte.

### G5 — Uncertainty Integrity
Incerteza preservada e calibrada.

### G6 — Alternative Integrity
Alternativas relevantes avaliadas.

### G7 — Metacognitive Integrity
Limitações, conflitos e possíveis erros avaliados.

### G8 — Regression Integrity
Alterações cognitivas avaliadas contra baseline.

### G9 — Operational Readiness
Harness, métricas, observabilidade e governança disponíveis.

---

# 23. Métricas

## Qualidade inferencial

- Evidence Support Rate
- Unsupported Inference Rate
- Counterevidence Coverage
- Contradiction Detection Rate
- Hypothesis Coverage
- Alternative Coverage

## Incerteza

- Calibration Error
- Overconfidence Rate
- Underconfidence Rate
- Uncertainty Preservation Rate
- Unknown Recognition Rate

## Causalidade

- Causal Claim Validity
- Correlation/Causation Error Rate
- Mechanism Coverage
- Counterfactual Consistency

## Semântica

- Semantic Consistency
- Entity Consistency
- Concept Drift Detection
- Ambiguity Resolution

## Metacognição

- Blind Spot Detection
- Self-Correction Rate
- Error Detection Rate
- Limitation Disclosure Rate

## Eficiência

- tokens;
- latência;
- chamadas;
- ciclos cognitivos;
- custo por análise;
- ganho de qualidade por recurso.

---

# 24. Taxonomia de Falhas

A camada deve distinguir:

1. Problem Representation Failure
2. Semantic Failure
3. Hypothesis Failure
4. Evidence Failure
5. Counterevidence Failure
6. Contradiction Failure
7. Inference Failure
8. Causal Failure
9. Counterfactual Failure
10. Uncertainty Failure
11. Calibration Failure
12. Probability Failure
13. Premature Closure
14. Alternative Neglect
15. Overconfidence
16. Hallucinated Support
17. Unsupported Conclusion
18. Metacognitive Failure
19. Context Interpretation Failure
20. Domain Leakage
21. Reasoning Regression

Cada falha deve possuir:

```yaml
failure_id:
class:
severity:
detected_by:
evidence:
impact:
containment:
recovery:
root_cause:
corrective_action:
version:
```

---

# 25. Observabilidade

Deve ser possível reconstruir:

```text
Task
 ↓
Problem Representation
 ↓
Knowledge State
 ↓
Hypotheses
 ↓
Evidence Requests
 ↓
Evidence
 ↓
Analysis
 ↓
Alternatives
 ↓
Uncertainty
 ↓
Conclusion
 ↓
Metacognitive Assessment
 ↓
Feedback
```

A observabilidade deve preservar somente o necessário para avaliação, evitando transformar o sistema em dependente de exposição indiscriminada do raciocínio interno.

---

# 26. Benchmark

### COG-SPEC-057 — Cognitive Benchmark Suite

O benchmark deve incluir:

- problemas bem definidos;
- problemas ambíguos;
- evidência incompleta;
- evidência conflitante;
- hipóteses concorrentes;
- relações causais;
- cenários contrafactuais;
- probabilidades;
- mudanças de contexto;
- fatos temporalmente distintos;
- informações enganosas;
- casos em que a resposta correta é reconhecer desconhecimento.

O benchmark deve avaliar **qualidade cognitiva**, não somente acurácia final.

---

# 27. Economicity Benchmark

### COG-SPEC-058 — Cognitive Economicity Benchmark

Deve medir:

> **qualidade cognitiva obtida por unidade de recurso consumido**

Métricas:

- qualidade / token;
- qualidade / segundo;
- qualidade / chamada;
- qualidade / custo;
- ganho marginal de cada etapa cognitiva.

O objetivo não é minimizar raciocínio indiscriminadamente.

O objetivo é identificar o **ponto de suficiência cognitiva**.

---

# 28. Versionamento

### COG-SPEC-059 — Cognitive Versioning

Cada evolução deve registrar:

```yaml
version:
baseline:
change:
hypothesis:
expected_effect:
metrics_before:
metrics_after:
regressions:
decision:
```

Uma alteração não deve ser promovida apenas porque melhora um caso isolado.

---

# 29. Ciclo de Aprimoramento

```text
Observação
   ↓
Medição
   ↓
Diagnóstico
   ↓
Hipótese de melhoria
   ↓
Experimento
   ↓
Benchmark
   ↓
Comparação com baseline
   ↓
Validação
   ↓
Governança
   ↓
Nova versão
```

---

# 30. Ordem Recomendada de Desenvolvimento

## Fase A — Fundamentos

- 001 Cognitive Capability Contract
- 002 Cognitive Task Model
- 003 Problem Representation
- 004 Cognitive State Model
- 005 Cognitive Unit

## Fase B — Hipóteses e evidências

- 006 Hypothesis Formation
- 007 Hypothesis Competition
- 008 Alternative Explanation
- 009 Hypothesis Evaluation
- 010 Hypothesis Invalidation
- 011 Evidence-to-Inference Mapping
- 012 Counterevidence Handling
- 013 Evidence Sufficiency
- 014 Inference Strength
- 015 Unsupported Inference Detection
- 016 Contradiction Handling

## Fase C — Causalidade e contrafactuais

- 017 Causal Reasoning
- 018 Correlation vs Causation
- 019 Causal Mechanism
- 020 Causal Counterfactual
- 021 Causal Uncertainty
- 022 Counterfactual Generation
- 023 Counterfactual Validity
- 024 Counterfactual Comparison
- 025 Counterfactual Boundary

## Fase D — Incerteza e probabilidade

- 026 Uncertainty Model
- 027 Confidence Calibration
- 028 Uncertainty Propagation
- 029 Unknown State
- 030 Confidence Revision
- 035 Probabilistic Reasoning
- 036 Prior and Evidence
- 037 Bayesian Updating
- 038 Probability Calibration
- 039 Probabilistic Dependency

## Fase E — Semântica e decisão

- 031 Semantic Interpretation
- 032 Ontological Alignment
- 033 Concept Disambiguation
- 034 Semantic Consistency
- 040 Decision Preparation
- 041 Option Evaluation
- 042 Consequence Analysis
- 043 Risk Analysis
- 044 Decision Boundary

## Fase F — Metacognição

- 045 Metacognitive Assessment
- 046 Blind Spot Detection
- 047 Cognitive Failure Detection
- 048 Self-Correction
- 049 Epistemic Status

## Fase G — Integração e saída

- 050 Cognition-to-RAG
- 051 Cognition-to-Experience
- 052 Cognition-to-Learning
- 053 Cognition-to-Governance
- 054 Skill-to-Cognition
- 055 Cognitive Output Contract

## Fase H — Harness e evolução

- 056 Cognitive Harness
- 057 Cognitive Benchmark Suite
- 058 Cognitive Economicity Benchmark
- 059 Cognitive Versioning
- Quality Gates
- Metrics
- Failure Taxonomy
- Observability

---

# 31. Critério de Prontidão

A camada de Cognição somente deve ser considerada suficientemente especificada quando for possível verificar:

- representação correta do problema;
- distinção entre fato, hipótese e inferência;
- competição entre hipóteses quando necessária;
- tratamento de contraevidência;
- tratamento de contradições;
- raciocínio causal;
- raciocínio contrafactual;
- representação de incerteza;
- calibração de confiança;
- raciocínio probabilístico quando pertinente;
- consistência semântica;
- análise decisional;
- metacognição;
- autocorreção;
- integração com RAG, Experience, Learning, Governance e Skills;
- Harness;
- Quality Gates;
- benchmark;
- métricas;
- regressão;
- observabilidade.

---

# 32. Regra Arquitetural Final

A camada de Cognição não deve tentar construir um LLM artificialmente rígido.

Seu objetivo é:

> **preservar a liberdade do modelo para descobrir como pensar, enquanto o Harness garante que o resultado satisfaça invariantes de evidência, coerência, incerteza, alternativas, rastreabilidade e autocorreção.**

O Harness controla **qualidade cognitiva observável**.

Ele não deve tentar substituir a própria cognição do LLM.

---

## 33. Registro de Especificações

| ID | Especificação | Estado |
|---|---|---|
| COG-SPEC-001 | Cognitive Capability Contract | A desenvolver |
| COG-SPEC-002 | Cognitive Task Model | A desenvolver |
| COG-SPEC-003 | Problem Representation | A desenvolver |
| COG-SPEC-004 | Cognitive State Model | A desenvolver |
| COG-SPEC-005 | Cognitive Unit | A desenvolver |
| COG-SPEC-006 | Hypothesis Formation | A desenvolver |
| COG-SPEC-007 | Hypothesis Competition | A desenvolver |
| COG-SPEC-008 | Alternative Explanation | A desenvolver |
| COG-SPEC-009 | Hypothesis Evaluation | A desenvolver |
| COG-SPEC-010 | Hypothesis Invalidation | A desenvolver |
| COG-SPEC-011 | Evidence-to-Inference Mapping | A desenvolver |
| COG-SPEC-012 | Counterevidence Handling | A desenvolver |
| COG-SPEC-013 | Evidence Sufficiency | A desenvolver |
| COG-SPEC-014 | Inference Strength | A desenvolver |
| COG-SPEC-015 | Unsupported Inference Detection | A desenvolver |
| COG-SPEC-016 | Contradiction Handling | A desenvolver |
| COG-SPEC-017 | Causal Reasoning Contract | A desenvolver |
| COG-SPEC-018 | Correlation vs Causation | A desenvolver |
| COG-SPEC-019 | Causal Mechanism | A desenvolver |
| COG-SPEC-020 | Causal Counterfactual | A desenvolver |
| COG-SPEC-021 | Causal Uncertainty | A desenvolver |
| COG-SPEC-022 | Counterfactual Generation | A desenvolver |
| COG-SPEC-023 | Counterfactual Validity | A desenvolver |
| COG-SPEC-024 | Counterfactual Comparison | A desenvolver |
| COG-SPEC-025 | Counterfactual Boundary | A desenvolver |
| COG-SPEC-026 | Uncertainty Model | A desenvolver |
| COG-SPEC-027 | Confidence Calibration | A desenvolver |
| COG-SPEC-028 | Uncertainty Propagation | A desenvolver |
| COG-SPEC-029 | Unknown State | A desenvolver |
| COG-SPEC-030 | Confidence Revision | A desenvolver |
| COG-SPEC-031 | Semantic Interpretation | A desenvolver |
| COG-SPEC-032 | Ontological Alignment | A desenvolver |
| COG-SPEC-033 | Concept Disambiguation | A desenvolver |
| COG-SPEC-034 | Semantic Consistency | A desenvolver |
| COG-SPEC-035 | Probabilistic Reasoning Contract | A desenvolver |
| COG-SPEC-036 | Prior and Evidence | A desenvolver |
| COG-SPEC-037 | Bayesian Updating | A desenvolver |
| COG-SPEC-038 | Probability Calibration | A desenvolver |
| COG-SPEC-039 | Probabilistic Dependency | A desenvolver |
| COG-SPEC-040 | Decision Preparation | A desenvolver |
| COG-SPEC-041 | Option Evaluation | A desenvolver |
| COG-SPEC-042 | Consequence Analysis | A desenvolver |
| COG-SPEC-043 | Risk Analysis | A desenvolver |
| COG-SPEC-044 | Decision Boundary | A desenvolver |
| COG-SPEC-045 | Metacognitive Assessment | A desenvolver |
| COG-SPEC-046 | Blind Spot Detection | A desenvolver |
| COG-SPEC-047 | Cognitive Failure Detection | A desenvolver |
| COG-SPEC-048 | Self-Correction | A desenvolver |
| COG-SPEC-049 | Epistemic Status | A desenvolver |
| COG-SPEC-050 | Cognition-to-RAG Contract | A desenvolver |
| COG-SPEC-051 | Cognition-to-Experience Contract | A desenvolver |
| COG-SPEC-052 | Cognition-to-Learning Contract | A desenvolver |
| COG-SPEC-053 | Cognition-to-Governance Contract | A desenvolver |
| COG-SPEC-054 | Skill-to-Cognition Contract | A desenvolver |
| COG-SPEC-055 | Cognitive Output Contract | A desenvolver |
| COG-SPEC-056 | Cognitive Harness | A desenvolver |
| COG-SPEC-057 | Cognitive Benchmark Suite | A desenvolver |
| COG-SPEC-058 | Cognitive Economicity Benchmark | A desenvolver |
| COG-SPEC-059 | Cognitive Versioning | A desenvolver |
