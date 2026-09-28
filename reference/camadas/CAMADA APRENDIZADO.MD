# MC-LRN-001 — MASTER CONTRACT DA CAMADA DE LEARNING

**Sistema:** SOT — System of Thought  
**Camada:** Learning  
**Identificador:** MC-LRN-001  
**Versão:** 1.0  
**Status:** BASELINE  
**Natureza:** Master Contract de Arquitetura, Especificação e Harness  
**Aplicabilidade:** Geral — não restrito a Trading  
**Dependências conceituais:** RAG, Cognição, Experiência e Memória, Skills, Governance  
**Princípio estrutural:** Learning transforma evidência acumulada em melhoria candidata, não em verdade automática.

---

# 1. PROPÓSITO

A Camada de Learning define a capacidade do sistema de utilizar experiências, observações, resultados, métricas e avaliações para identificar oportunidades de melhoria, formular hipóteses de aprendizagem, realizar experimentos, avaliar resultados e propor evolução controlada.

Learning não deve ser confundido com:

- memória
- experiência
- cognição
- conhecimento
- treinamento automático
- adaptação automática
- decisão
- governança.

A camada deve permitir que o sistema melhore sem perder rastreabilidade, sem transformar uma experiência isolada em regra e sem permitir que uma alteração seja promovida sem evidência proporcional ao seu impacto.

---

# 2. MISSÃO

A missão da camada é:

> Transformar evidências provenientes da experiência e da operação em hipóteses de melhoria testáveis, submetê-las a experimentação e validação e produzir candidatos de aprendizagem capazes de alimentar uma evolução controlada do sistema.

O Learning deve responder:

1. O que aconteceu?
2. O que apresentou desempenho inadequado?
3. O que apresentou desempenho superior?
4. Qual padrão pode estar relacionado ao resultado?
5. Qual hipótese de melhoria pode ser formulada?
6. O que deveria mudar?
7. Qual efeito é esperado?
8. Como testar essa hipótese?
9. Quais evidências suportam a mudança?
10. Quais evidências contradizem a mudança?
11. O resultado foi reproduzível?
12. O efeito ocorreu no contexto esperado?
13. A melhoria possui custo aceitável?
14. O aprendizado é suficientemente robusto para ser proposto à Governança?

---

# 3. NÃO OBJETIVOS

Learning NÃO deve possuir autoridade automática para:

- alterar conhecimento canônico
- alterar arquitetura
- alterar princípios fundamentais
- alterar invariantes
- alterar contratos
- alterar políticas
- alterar identidade de uma Skill
- publicar conhecimento imutável
- alterar memória histórica
- substituir a Cognição
- substituir a Governança
- transformar qualquer feedback em aprendizado
- transformar qualquer correlação em causalidade
- promover automaticamente uma hipótese experimental para produção.

---

# 4. PRINCÍPIO CENTRAL

## Learning transforma experiência em hipótese de melhoria, não experiência em verdade.

O fluxo fundamental é:

```text
Observação
↓
Registro
↓
Medição
↓
Diagnóstico
↓
Hipótese de melhoria
↓
Predição
↓
Experimento
↓
Dados
↓
Análise
↓
Evidência
↓
Avaliação
↓
Learning Candidate
↓
Validação
↓
Governança
↓
Evolução controlada

5. PRINCÍPIOS DA CAMADA
LRN-P01 — Evidência antes da alteração

Nenhuma alteração relevante deve ser justificada apenas por intuição ou preferência.

LRN-P02 — Hipótese antes da conclusão

O sistema deve distinguir:

observação

de:

interpretação

e:

hipótese de melhoria.
LRN-P03 — Experimentação

Quando uma hipótese puder ser testada, deve existir preferência por experimentação controlada.

LRN-P04 — Reprodutibilidade

Resultados de aprendizagem devem ser avaliados quanto à capacidade de reprodução.

LRN-P05 — Contexto

Uma melhoria observada em determinado contexto não deve ser generalizada automaticamente para outros contextos.

LRN-P06 — Conservação da incerteza

Incerteza experimental deve permanecer representada.

LRN-P07 — Contraevidência

Evidências que contradizem a hipótese devem ser preservadas.

LRN-P08 — Separação entre aprendizado e promoção

Produzir um Learning Candidate não significa que a alteração esteja autorizada.

LRN-P09 — Evolução proporcional ao impacto

Quanto maior o impacto potencial da mudança, maior deve ser a exigência de evidência e validação.

LRN-P10 — Reversibilidade

Alterações propostas devem ser reversíveis quando tecnicamente possível.

LRN-P11 — Não aprendizagem de ruído

Uma alteração observada em poucos episódios não deve ser tratada automaticamente como padrão robusto.

LRN-P12 — Preservação da causalidade

O Learning deve distinguir associação, correlação e causalidade.

LRN-P13 — Learning não reescreve experiência

A interpretação de uma experiência pode evoluir, mas o histórico original deve permanecer preservado.

LRN-P14 — Learning não possui autoridade de Governança

Learning pode propor.

Governance decide.

6. MODELO CONCEITUAL
EXPERIÊNCIA
     ↓
OBSERVAÇÃO
     ↓
REGISTRO
     ↓
MEDIÇÃO
     ↓
DIAGNÓSTICO
     ↓
HIPÓTESE DE MELHORIA
     ↓
PREDIÇÃO
     ↓
EXPERIMENTO
     ↓
DADOS
     ↓
ANÁLISE
     ↓
EVIDÊNCIA
     ↓
AVALIAÇÃO
     ↓
LEARNING CANDIDATE
     ↓
VALIDAÇÃO
     ↓
GOVERNANÇA
     ↓
EVOLUÇÃO CONTROLADA
7. TIPOS DE LEARNING

A camada deve distinguir diferentes formas de aprendizagem.

7.1 Learning cognitivo

Melhoria na forma como o sistema:

interpreta
raciocina
formula hipóteses
avalia evidências
reconhece incerteza
compara alternativas.
7.2 Learning operacional

Melhoria relacionada à execução:

processo
procedimento
parametrização
roteamento
eficiência
uso de recursos.
7.3 Learning de recuperação

Melhoria relacionada a:

recuperação de conhecimento
seleção de evidências
contexto
relevância
eficiência de recuperação.
7.4 Learning de Skill

Melhorias relacionadas à aplicação de competências específicas.

Exemplos genéricos:

Skill Elliott
Skill SMC
Skill ICT

A existência dessas Skills não autoriza o Learning a alterar suas definições fundamentais sem Governança.

7.5 Learning de estratégia

Melhoria de comportamento estratégico com base em evidências históricas e experimentais.

8. LEARNING CANDIDATE

A unidade fundamental do Learning é o Learning Candidate.

learning_candidate_id:

observation_refs:

experience_refs:

problem:

diagnosis:

hypothesis:

proposed_change:

expected_effect:

scope:

assumptions:

baseline:

experiment_design:

metrics:

success_criteria:

failure_criteria:

evidence:

counterevidence:

results:

confidence:

uncertainty:

regime:

limitations:

regression_risks:

validation_status:

governance_status:

provenance:

version:
9. ESTADOS DO LEARNING CANDIDATE

Um candidato pode seguir:

CREATED
   ↓
ANALYZED
   ↓
HYPOTHESIS_FORMED
   ↓
EXPERIMENT_DESIGNED
   ↓
EXPERIMENT_RUNNING
   ↓
RESULT_OBTAINED
   ↓
EVALUATED

Após avaliação:

SUPPORTED

ou:

PARTIALLY_SUPPORTED

ou:

INCONCLUSIVE

ou:

REFUTED

Um candidato suportado pode seguir:

VALIDATION
↓
GOVERNANCE
↓
PROMOTED
10. OBSERVAÇÃO

O Learning deve começar com observações verificáveis.

Exemplo:

A taxa de falha aumentou de X para Y durante determinado período.

Isso não significa:

A causa foi X.

A segunda afirmação requer investigação.

11. MEDIÇÃO

Toda hipótese relevante deve procurar indicadores mensuráveis.

Exemplos:

precisão
recall
latência
custo
taxa de erro
estabilidade
retorno
perda
eficiência
taxa de recorrência
qualidade de evidência.
12. DIAGNÓSTICO

O diagnóstico deve investigar possíveis causas.

Pode utilizar:

experiência
conhecimento
cognição
métricas
evidências externas
experimentos anteriores.

O diagnóstico não deve ser confundido com certeza causal.

13. HIPÓTESE DE MELHORIA

Uma hipótese deve possuir estrutura explícita.

hypothesis:
  statement:
  mechanism:
  expected_effect:
  scope:
  assumptions:
  confidence:

Exemplo:

Se a recuperação contextual for restringida a evidências
com maior correspondência de regime, então a qualidade
da análise deverá aumentar sob determinado conjunto de condições.
14. PREDIÇÃO

Toda hipótese experimental relevante deve definir o que seria esperado caso fosse verdadeira.

prediction:

expected_direction:

expected_magnitude:

expected_conditions:

expected_failure_modes:
15. EXPERIMENTO

O experimento deve definir:

hipótese
baseline
variável modificada
população
período
condições
métricas
critérios de sucesso
critérios de falha
controles
riscos.
16. BASELINE

Toda alteração experimental relevante deve possuir uma referência comparativa.

BASELINE
vs.
EXPERIMENT

Sem baseline, torna-se mais difícil determinar se houve melhoria real.

17. CONTROLE EXPERIMENTAL

Quando aplicável, devem ser utilizadas:

comparação A/B
conjunto de controle
backtest
replay
simulação
validação histórica
validação fora da amostra
teste prospectivo.

A técnica deve ser proporcional ao problema.

18. RESULTADO EXPERIMENTAL

Resultado deve registrar:

result:

observed_effect:

expected_effect:

difference:

metrics:

confidence:

limitations:

unexpected_effects:

failure_modes:
19. EVIDÊNCIA

A evidência deve ser rastreável às observações e aos dados.

O Learning deve preservar:

fonte
→ dado
→ análise
→ resultado
→ conclusão experimental
20. CONTRAEVIDÊNCIA

A avaliação deve procurar evidências que reduzam a força da hipótese.

Exemplo:

Resultado favorável:
Condição A.

Resultado desfavorável:
Condição B.

Conclusão:
Possível melhoria contextual, não regra universal.
21. CONTEXTO

Toda aprendizagem deve possuir escopo.

Exemplo:

scope:
  market:
  regime:
  timeframe:
  task:
  agent:
  skill:
  period:

Uma melhoria válida em um contexto pode ser inválida em outro.

22. GENERALIZAÇÃO

A generalização deve ser tratada como hipótese adicional.

Fluxo:

Resultado local
↓
Repetição
↓
Validação em contextos diferentes
↓
Avaliação de robustez
↓
Possível generalização

Nunca:

Um resultado
↓
Regra universal
23. REGRESSÃO

Toda mudança proposta deve ser avaliada quanto à possibilidade de degradar capacidades existentes.

Uma alteração pode:

melhorar A

e simultaneamente:

piorar B.

Portanto, Learning deve considerar efeitos positivos e negativos.

24. TRADE-OFFS

Learning deve registrar:

ganho
custo
risco
efeito colateral
latência
consumo de contexto
consumo computacional
perda potencial de capacidade.

Uma melhoria não deve ser considerada apenas pela métrica que motivou sua criação.

25. ECONOMICIDADE

A melhoria deve considerar:

Benefício obtido
/
Custo adicional

O custo pode incluir:

tokens
latência
memória
armazenamento
processamento
complexidade
manutenção
supervisão.
26. APRENDIZADO COGNITIVO

O Learning pode identificar que determinado comportamento cognitivo produz melhores resultados.

Exemplo:

Hipótese:
considerar explicitamente contraevidências melhora a qualidade da análise.

Isso deve ser testado.

O Learning não deve simplesmente ordenar:

sempre faça X.

sem evidência suficiente.

27. APRENDIZADO OPERACIONAL

Pode envolver:

melhor ordem de execução
melhor recuperação
melhor uso de ferramentas
melhor alocação de recursos
melhor configuração.
28. APRENDIZADO DE PARÂMETROS

Parâmetros podem ser calibrados experimentalmente.

O processo deve preservar:

parâmetro anterior
→ novo parâmetro
→ motivo
→ experimento
→ resultado
→ impacto
29. BACKTEST E REPLAY

Quando aplicável, o Learning deve poder utilizar:

backtest
replay histórico
simulação
dados fora da amostra
testes prospectivos.

A finalidade é avaliar se a alteração possui evidência além do conjunto que originou a hipótese.

30. OVERFITTING

O Harness deve procurar sinais de que a melhoria foi ajustada excessivamente ao histórico utilizado.

Possíveis sinais:

excelente resultado apenas no conjunto de desenvolvimento
degradação fora da amostra
dependência de período específico
dependência excessiva de parâmetros
baixa estabilidade em regimes diferentes.
31. LEARNING E TRADING

Quando aplicado ao Trading, Learning pode investigar:

calibração de parâmetros
desempenho por regime
desempenho por timeframe
comportamento de hipóteses
qualidade de sinais
eficácia de filtros
impacto de contexto
recorrência de erros
robustez de estratégias.

Não deve transformar automaticamente:

backtest favorável

em:

regra operacional definitiva.
32. RELAÇÃO COM EXPERIÊNCIA

Experiência fornece matéria-prima.

Experience
↓
Observation
↓
Pattern
↓
Hypothesis

Learning não altera a experiência original.

33. RELAÇÃO COM COGNIÇÃO

Cognição interpreta e analisa.

Learning pode avaliar se determinados padrões cognitivos produziram melhores resultados.

Cognition
↓
Analysis
↓
Outcome
↓
Learning
↓
Improvement Hypothesis
34. RELAÇÃO COM RAG

RAG pode fornecer:

evidências
conhecimento
experiências
referências
documentação.

Learning pode utilizar essas informações para construir hipóteses.

RAG não decide o que deve ser aprendido.

35. RELAÇÃO COM SKILLS

Learning pode propor:

calibração
ajustes
melhorias de aplicação
refinamento operacional.

Não deve alterar automaticamente a identidade fundamental da Skill.

36. RELAÇÃO COM GOVERNANCE

A Governança controla:

promoção
aprovação
escopo
impacto
reversão
versionamento.

Learning é propositor.

Governance é autoridade de evolução.

37. ESPECIFICAÇÕES A SEREM DESENVOLVIDAS
Foundations
LRN-SPEC-001 — Learning Capability Contract

Definir contrato geral da camada.

LRN-SPEC-002 — Learning Task Model

Definir tipos de tarefas de aprendizagem.

LRN-SPEC-003 — Learning State Model

Definir estados dos processos de aprendizagem.

LRN-SPEC-004 — Learning Candidate Model

Definir estrutura formal do candidato.

LRN-SPEC-005 — Learning Provenance

Definir rastreabilidade.

38. OBSERVAÇÃO E DIAGNÓSTICO
LRN-SPEC-006 — Observation Model

Definir observações.

LRN-SPEC-007 — Measurement Model

Definir medições.

LRN-SPEC-008 — Diagnostic Model

Definir diagnóstico.

LRN-SPEC-009 — Pattern Detection

Definir identificação de padrões.

LRN-SPEC-010 — Failure Pattern Analysis

Definir análise de padrões de falha.

LRN-SPEC-011 — Success Pattern Analysis

Definir análise de padrões de sucesso.

39. HIPÓTESES
LRN-SPEC-012 — Improvement Hypothesis

Definir hipótese de melhoria.

LRN-SPEC-013 — Hypothesis Competition

Permitir hipóteses alternativas.

LRN-SPEC-014 — Hypothesis Scope

Definir escopo.

LRN-SPEC-015 — Hypothesis Confidence

Definir confiança.

LRN-SPEC-016 — Hypothesis Counterevidence

Definir contraevidência.

LRN-SPEC-017 — Prediction Model

Definir predições.

40. EXPERIMENTAÇÃO
LRN-SPEC-018 — Experiment Contract

Definir contrato experimental.

LRN-SPEC-019 — Experiment Design

Definir desenho experimental.

LRN-SPEC-020 — Baseline Model

Definir baseline.

LRN-SPEC-021 — Control Model

Definir controle experimental.

LRN-SPEC-022 — A/B Evaluation

Definir comparação A/B.

LRN-SPEC-023 — Backtest Contract

Definir backtests.

LRN-SPEC-024 — Replay Contract

Definir replay.

LRN-SPEC-025 — Simulation Contract

Definir simulação.

LRN-SPEC-026 — Out-of-Sample Validation

Definir validação fora da amostra.

LRN-SPEC-027 — Prospective Validation

Definir validação prospectiva.

41. AVALIAÇÃO
LRN-SPEC-028 — Learning Result Model

Definir resultado experimental.

LRN-SPEC-029 — Effect Measurement

Definir mensuração do efeito.

LRN-SPEC-030 — Statistical Evaluation

Definir avaliação estatística.

LRN-SPEC-031 — Robustness Evaluation

Definir robustez.

LRN-SPEC-032 — Generalization Evaluation

Definir generalização.

LRN-SPEC-033 — Overfitting Detection

Definir detecção de overfitting.

LRN-SPEC-034 — Regression Evaluation

Definir regressão.

LRN-SPEC-035 — Trade-off Evaluation

Definir trade-offs.

42. PROMOÇÃO
LRN-SPEC-036 — Learning Validation

Definir validação do aprendizado.

LRN-SPEC-037 — Learning Candidate Promotion

Definir promoção.

LRN-SPEC-038 — Learning Impact Classification

Classificar impacto.

LRN-SPEC-039 — Learning-to-Governance Contract

Definir integração com Governança.

LRN-SPEC-040 — Rollback Contract

Definir reversão.

43. APRENDIZADO DE PARÂMETROS
LRN-SPEC-041 — Parameter Learning

Definir aprendizado de parâmetros.

LRN-SPEC-042 — Parameter Calibration

Definir calibração.

LRN-SPEC-043 — Parameter Stability

Definir estabilidade.

LRN-SPEC-044 — Parameter Sensitivity

Definir sensibilidade.

LRN-SPEC-045 — Parameter Drift

Definir drift.

44. LEARNING ESTRATÉGICO
LRN-SPEC-046 — Strategy Learning

Definir aprendizagem estratégica.

LRN-SPEC-047 — Regime-Specific Learning

Definir aprendizagem por regime.

LRN-SPEC-048 — Strategy Adaptation

Definir adaptação.

LRN-SPEC-049 — Strategy Regression

Definir regressão estratégica.

45. HARNESS E EVOLUÇÃO
LRN-SPEC-050 — Learning Harness

Definir Harness da camada.

LRN-SPEC-051 — Learning Benchmark Suite

Definir benchmarks.

LRN-SPEC-052 — Learning Economicity Benchmark

Definir economicidade.

LRN-SPEC-053 — Learning Versioning

Definir versionamento.

LRN-SPEC-054 — Learning Regression Memory

Definir memória de regressão.

LRN-SPEC-055 — Learning Audit Trail

Definir trilha de auditoria.

46. HARNESS DA CAMADA

O Harness deve verificar se o sistema realmente aprendeu algo útil ou apenas ajustou seu comportamento ao conjunto de dados utilizado.

O Harness deve separar:

qualidade do processo de aprendizagem

de:

qualidade do resultado experimental.
47. SENSORES DETERMINÍSTICOS

O Harness deve verificar:

integridade do Learning Candidate
presença de baseline
identificação do experimento
identificação das métricas
rastreabilidade das evidências
versionamento
escopo
estado do experimento
registro de resultados
registro de contraevidência
registro de regressões
integridade da trilha de auditoria.
48. SENSORES INFERENCIAIS

Devem avaliar:

qualidade da hipótese
plausibilidade do mecanismo
força da evidência
coerência entre hipótese e experimento
força da conclusão
risco de overfitting
generalização
robustez
relevância contextual
magnitude do efeito
custo-benefício
efeitos colaterais.
49. TESTES

O Harness deve incluir:

Teste de hipótese

A hipótese está explicitamente definida?

Teste de baseline

Existe comparação válida?

Teste experimental

O experimento realmente testa a hipótese?

Teste de contraevidência

Resultados contrários foram considerados?

Teste de reprodução

O resultado se mantém?

Teste fora da amostra

O efeito persiste em dados não utilizados na formulação?

Teste de robustez

O efeito permanece sob variações razoáveis?

Teste de overfitting

A melhoria depende excessivamente do conjunto de desenvolvimento?

Teste de regressão

A alteração prejudica capacidades anteriores?

Teste de economicidade

O ganho compensa o custo?

Teste adversarial

O sistema pode ser induzido a considerar ruído como aprendizado?

50. INVARIANTES
I-LRN-01

Observação não é automaticamente explicação.

I-LRN-02

Correlação não é automaticamente causalidade.

I-LRN-03

Experiência não é automaticamente aprendizado.

I-LRN-04

Learning Candidate não é aprendizado validado.

I-LRN-05

Aprendizado validado não é automaticamente alteração autorizada.

I-LRN-06

Contraevidência relevante não pode ser silenciosamente descartada.

I-LRN-07

Uma melhoria local não pode ser automaticamente generalizada.

I-LRN-08

Alterações relevantes devem possuir baseline.

I-LRN-09

Mudanças relevantes devem ser avaliadas quanto a regressão.

I-LRN-10

O resultado experimental deve permanecer rastreável às evidências.

I-LRN-11

Learning não pode alterar silenciosamente a experiência histórica.

I-LRN-12

Learning não possui autoridade de Governança.

I-LRN-13

A confiança do aprendizado deve ser proporcional à evidência disponível.

I-LRN-14

O custo de uma melhoria deve ser considerado junto ao benefício.

I-LRN-15

Uma alteração experimental não deve ser promovida sem validação proporcional ao impacto.

51. QUALITY GATES
G0 — Learning Contract

Contrato da camada definido.

G1 — Observation Integrity

Observações são rastreáveis.

G2 — Measurement Integrity

Medições são válidas e reproduzíveis.

G3 — Hypothesis Integrity

Hipótese está explicitamente definida.

G4 — Experiment Integrity

Experimento testa efetivamente a hipótese.

G5 — Evidence Integrity

Resultados possuem evidência suficiente.

G6 — Robustness Integrity

Resultado foi avaliado quanto à robustez.

G7 — Regression Integrity

Possíveis efeitos negativos foram avaliados.

G8 — Learning Validation

O candidato atende critérios de validação.

G9 — Governance Readiness

O candidato está suficientemente especificado para avaliação pela Governança.

G10 — Evolution Integrity

A alteração promovida possui versionamento, rastreabilidade e reversibilidade apropriada.

52. MÉTRICAS

A camada deve poder medir:

Hypothesis Quality
Evidence Strength
Experiment Validity
Reproducibility Rate
Out-of-Sample Performance
Robustness
Generalization
Regression Rate
Overfitting Rate
Learning Candidate Precision
Learning Candidate Validation Rate
Improvement Magnitude
Improvement Stability
Error Reduction
Failure Recurrence Reduction
Success Recurrence
Cost per Learning
Token Cost per Learning
Compute Cost per Learning
Latency Cost
Learning Utility
Promotion Rate
Rollback Rate
False Learning Rate.
53. FAILURE TAXONOMY
Observation Failure

Observação incorreta ou incompleta.

Measurement Failure

Medição inadequada.

Diagnostic Failure

Diagnóstico incorreto.

Hypothesis Failure

Hipótese mal formulada.

Experiment Failure

Experimento incapaz de testar adequadamente a hipótese.

Evidence Failure

Evidência insuficiente ou inadequada.

Confirmation Bias

Seleção preferencial de evidências favoráveis.

Overfitting

Aprendizado excessivamente ajustado ao conjunto utilizado.

Generalization Failure

Extensão indevida do resultado.

Regression

Melhoria em uma capacidade acompanhada de degradação em outra.

Attribution Failure

Atribuição incorreta do resultado à mudança.

Measurement Leakage

Informação do conjunto de avaliação contaminando o processo de desenvolvimento.

Data Leakage

Informação futura ou indevida influenciando o aprendizado.

False Learning

O sistema interpreta ruído como melhoria.

Learning Drift

O comportamento aprendido perde validade ao longo do tempo.

Promotion Failure

Learning Candidate promovido sem evidência suficiente.

Governance Failure

Alteração evolutiva sem controle apropriado.

Economic Failure

Custo da melhoria supera seu benefício.

54. OBSERVABILIDADE

O sistema deve permitir reconstruir:

OBSERVAÇÃO
↓
MÉTRICA
↓
DIAGNÓSTICO
↓
HIPÓTESE
↓
PREDIÇÃO
↓
EXPERIMENTO
↓
DADOS
↓
ANÁLISE
↓
RESULTADO
↓
EVIDÊNCIA
↓
LEARNING CANDIDATE
↓
VALIDAÇÃO
↓
GOVERNANÇA
↓
ALTERAÇÃO
↓
RESULTADO PÓS-ALTERAÇÃO
55. BENCHMARK SUITE

Os benchmarks devem testar:

Formulação correta de hipóteses.
Existência de baseline.
Correspondência entre hipótese e experimento.
Preservação de contraevidência.
Reprodutibilidade.
Robustez.
Generalização.
Detecção de overfitting.
Detecção de regressão.
Validação fora da amostra.
Atribuição correta do efeito.
Avaliação de custo.
Capacidade de rollback.
Separação entre Learning Candidate e aprendizado validado.
Separação entre aprendizado e promoção.
Resistência a aprendizado de ruído.
Resistência a data leakage.
Resistência a confirmation bias.
56. ECONOMICIDADE

A avaliação de Learning deve considerar:

Valor da melhoria
/
Custo total do aprendizado

O custo total pode incluir:

dados
tokens
inferência
armazenamento
experimentação
backtests
simulações
validação
supervisão humana
manutenção
complexidade introduzida.

O melhor aprendizado não é necessariamente aquele que produz o maior ganho isolado.

Deve ser considerado também o custo para obter e sustentar esse ganho.

57. VERSIONAMENTO

Toda evolução deve possuir registro:

version:

baseline:

change:

reason:

hypothesis:

experiment:

expected_effect:

observed_effect:

regressions:

integrity_tests:

economic_evaluation:

decision:

rollback_plan:
58. CICLO DE VIDA
OBSERVE
   ↓
MEASURE
   ↓
DIAGNOSE
   ↓
HYPOTHESIZE
   ↓
PREDICT
   ↓
EXPERIMENT
   ↓
MEASURE
   ↓
ANALYZE
   ↓
VALIDATE
   ↓
LEARNING CANDIDATE
   ↓
GOVERNANCE
   ↓
PROMOTE
   ↓
MONITOR
   ↓
REASSESS

O ciclo pode retornar a qualquer estágio quando novas evidências surgirem.

59. CONDIÇÕES DE PRONTIDÃO

A camada somente deve ser considerada pronta quando for capaz de:

registrar observações
medir resultados
diagnosticar problemas
formular hipóteses
formular predições
executar experimentos
comparar com baseline
avaliar resultados
considerar contraevidência
testar robustez
testar generalização
detectar overfitting
detectar regressão
produzir Learning Candidates
preservar incerteza
rastrear evidências
integrar Experiência
integrar Cognição
integrar RAG
integrar Skills
integrar Governance
avaliar economicidade
executar Harness
versionar alterações
permitir rollback.
60. CRITÉRIO FINAL DA CAMADA

A Camada de Learning deve permitir que o sistema:

melhore de maneira experimental, rastreável, mensurável e reversível, transformando experiências e evidências em hipóteses de melhoria sem confundir adaptação local com conhecimento universal e sem conceder ao aprendizado autoridade automática para alterar o sistema.

61. RELAÇÃO COM AS DEMAIS CAMADAS
                    ┌───────────────────┐
                    │    GOVERNANCE     │
                    └─────────▲─────────┘
                              │
                         promoção
                              │
                    ┌─────────┴─────────┐
                    │     LEARNING      │
                    └─────┬─────┬───────┘
                          │     │
                    feedback    │
                          │     │
             ┌────────────┘     └─────────────┐
             ▼                                ▼
┌─────────────────────┐              ┌─────────────────┐
│ EXPERIENCE & MEMORY │              │    COGNITION    │
└──────────┬──────────┘              └────────┬────────┘
           │                                  │
           └──────────────┬───────────────────┘
                          ▼
                     EXPERIMENT
                          │
                          ▼
                      EVIDENCE
                          │
                          ▼
                     VALIDATION
62. BASELINE

MC-LRN-001 — Master Contract da Camada de Learning

Status: BASELINE PROPOSTA

Regra de evolução:

Nenhuma alteração estrutural relevante deve ser incorporada sem:

Especificação
→ Harness
→ Experimento
→ Evidência
→ Validação
→ Avaliação de impacto
→ Governança
→ Versionamento
→ Monitoramento

Fim do Master Contract.