# MEG-001

# MASTER EPISTEMOLOGICAL GUIDE FOR LLM COGNITION

## Guia Mestre para Especificação da Camada Epistêmica da Cognição de LLMs

**Versão:** 1.0
**Status:** Baseline
**Natureza:** Metaespecificação cognitiva e de Harness
**Objeto:** Cognição de LLMs
**Aplicação primária:** Claude Code, agentes de IA, sistemas multiagentes e Harnesses cognitivos
**Domínio:** Geral
**Dependência superior:** Master Principiological Specification Guide
**Interface posterior:** Master Inquiry Methods Specification Guide

---

# 1. PROPÓSITO

Este documento estabelece os fundamentos, estruturas, critérios e mecanismos necessários para **especificar e governar epistemicamente a cognição de um LLM por meio de Harness**.

O MEG-001 não especifica software.

Não especifica:

* APIs
* bancos de dados
* classes
* objetos
* serviços
* interfaces de usuário
* arquitetura de aplicação
* implementação de RAG
* implementação de agentes.

O MEG-001 especifica **como uma arquitetura de Harness deve governar o processo pelo qual um LLM produz, avalia, utiliza, revisa e comunica conhecimento durante uma tarefa**.

Seu objetivo é impedir que a capacidade generativa do LLM seja confundida com:

* evidência
* conhecimento
* validação
* verdade
* decisão autorizada.

---

# 2. TESE FUNDAMENTAL

A capacidade de um LLM produzir uma resposta coerente não constitui evidência de que a resposta seja epistemicamente justificada.

Portanto:

> **O Harness deve governar não apenas o que o LLM produz, mas o status epistêmico que o LLM atribui ao que produz.**

A questão fundamental deixa de ser:

> "O LLM respondeu corretamente?"

e passa a incluir:

> "O LLM tinha base suficiente para afirmar isso?"

> "O que ele sabia?"

> "O que ele inferiu?"

> "O que ele assumiu?"

> "O que ele não sabia?"

> "Que evidências utilizou?"

> "Quais alternativas considerou?"

> "Qual método utilizou para chegar à conclusão?"

> "Sua conclusão excedeu a evidência disponível?"

> "O Harness detectou e corrigiu esse excesso?"

---

# 3. PROBLEMA EPISTÊMICO DOS LLMs

LLMs apresentam uma característica fundamental para a engenharia cognitiva:

> podem produzir linguagem altamente coerente independentemente da qualidade epistemológica daquilo que afirmam.

Consequentemente, podem ocorrer:

* afirmações sem evidência
* inferências apresentadas como fatos
* hipóteses apresentadas como conclusões
* confiança desproporcional à evidência
* preenchimento de lacunas com suposições
* falsa precisão
* extrapolação
* seleção prematura de explicações
* aceitação acrítica de fontes
* síntese incorreta
* memória confundida com evidência
* contexto incompleto tratado como suficiente
* informação desatualizada utilizada como atual
* contradições silenciosamente eliminadas.

O Harness epistemológico existe para controlar essas classes de falha.

---

# 4. POSIÇÃO NA ARQUITETURA DE ENGENHARIA DE IA

A camada epistêmica não deve ser isolada como um módulo de software.

Ela é uma **dimensão de governança da cognição**.

A arquitetura conceitual é:

```text
┌────────────────────────────────────────────┐
│              PRINCIPIOLOGIA                │
│                                            │
│ O que deve orientar o sistema              │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│              EPISTEMOLOGIA                 │
│                                            │
│ Como o sistema deve tratar conhecimento    │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│          MÉTODOS DE INQUÉRITO              │
│                                            │
│ Como investigar uma questão                │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│                  HARNESS                    │
│                                            │
│ Como verificar e governar o comportamento  │
└──────────────────────┬─────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────┐
│                  LLM                       │
│                                            │
│ Raciocínio, síntese, inferência e geração  │
└────────────────────────────────────────────┘
```

O Harness não substitui o LLM.

Ele cria as condições sob as quais o LLM pode operar.

---

# 5. PRINCÍPIO DE SEPARAÇÃO

A arquitetura deve preservar a separação entre:

```text
PRINCÍPIO
    ↓
CRITÉRIO EPISTÊMICO
    ↓
MÉTODO
    ↓
EVIDÊNCIA
    ↓
INTERPRETAÇÃO
    ↓
INFERÊNCIA
    ↓
HIPÓTESE
    ↓
CONCLUSÃO
    ↓
DECISÃO
    ↓
AÇÃO
```

Nenhuma dessas transições deve ser implicitamente considerada equivalente à anterior.

---

# 6. DEFINIÇÃO OPERACIONAL DE EPISTEMOLOGIA PARA LLMs

Neste framework:

> **Epistemologia é o conjunto de princípios, critérios e mecanismos utilizados para determinar o status, a sustentação, a incerteza, os limites e a possibilidade de revisão daquilo que o LLM considera e comunica como conhecimento.**

Portanto, a camada epistêmica governa:

* formação de crenças operacionais
* avaliação de evidências
* inferência
* hipóteses
* incerteza
* conflito
* desconhecimento
* atualização
* validação
* comunicação do estado de conhecimento.

---

# 7. OBJETIVO DA GOVERNANÇA EPISTÊMICA

O objetivo não é fazer o LLM:

> "ter certeza".

O objetivo é fazê-lo:

> **ser proporcionalmente certo ao suporte disponível.**

Assim:

```text
EVIDÊNCIA FORTE
      ↓
maior confiança permitida

EVIDÊNCIA FRACA
      ↓
menor confiança permitida

EVIDÊNCIA AUSENTE
      ↓
não concluir

CONFLITO RELEVANTE
      ↓
preservar conflito

INCERTEZA CRÍTICA
      ↓
investigar / perguntar / abster-se
```

---

# 8. MODELO EPISTÊMICO FUNDAMENTAL

Toda afirmação produzida pelo LLM deve poder ser conceitualmente classificada como:

```text
OBSERVAÇÃO
INFORMAÇÃO
FATO DOCUMENTADO
INTERPRETAÇÃO
INFERÊNCIA
HIPÓTESE
CONCLUSÃO PROVISÓRIA
CONHECIMENTO VALIDADO
CONHECIMENTO CONTESTADO
CONHECIMENTO REFUTADO
DESCONHECIDO
INDETERMINADO
```

A implementação concreta pode utilizar outra nomenclatura.

A distinção conceitual é obrigatória.

---

# 9. REGRA FUNDAMENTAL DO STATUS EPISTÊMICO

> **O status epistemológico de uma afirmação deve ser determinado pela relação entre a afirmação, suas evidências, o método utilizado, o contexto e os critérios de validação aplicáveis.**

Não deve ser determinado por:

* fluência
* autoridade aparente
* frequência
* familiaridade
* confiança textual
* posição hierárquica do agente
* quantidade de tokens
* eloquência
* consenso aparente entre LLMs.

---

# 10. UNIDADE ATÔMICA DE GOVERNANÇA

A unidade mínima que o Harness deve ser capaz de analisar é:

> **uma afirmação relevante para o raciocínio.**

O Harness deve ser capaz de perguntar:

```text
O que está sendo afirmado?
↓
Qual é o status?
↓
Qual é a origem?
↓
Qual é a evidência?
↓
Qual método sustentou a conclusão?
↓
Quais pressupostos existem?
↓
Qual é a incerteza?
↓
Existem alternativas?
↓
Existem contradições?
↓
Qual é o escopo da validade?
```

---

# 11. ESTADOS EPISTÊMICOS DO LLM

O Harness deve trabalhar com estados cognitivo-epistêmicos.

Um modelo geral:

```text
UNKNOWN
   ↓
INFORMED
   ↓
OBSERVED / SOURCED
   ↓
INTERPRETED
   ↓
INFERRED
   ↓
HYPOTHESIS
   ↓
SUPPORTED
   ↓
VALIDATED
```

Com caminhos laterais:

```text
SUPPORTED ─────► CONTESTED
SUPPORTED ─────► WEAKENED
VALIDATED ─────► REVISED
VALIDATED ─────► REFUTED
ANY STATE ─────► UNKNOWN
```

O estado deve refletir o suporte disponível, e não a preferência do LLM.

---

# 12. FATO, INFERÊNCIA E HIPÓTESE

O Harness deve obrigar o LLM a distinguir:

### Fato

Algo diretamente observado ou estabelecido por fonte apropriada.

### Inferência

Algo derivado a partir de informações ou evidências.

### Hipótese

Uma explicação ou proposição que ainda necessita de investigação ou validação.

### Conclusão

Resultado obtido após aplicação de critérios de investigação.

### Suposição

Premissa adotada para permitir o raciocínio.

A mistura dessas categorias constitui uma falha epistemológica.

---

# 13. REGRA CONTRA CONVERSÃO SILENCIOSA

São proibidas transições silenciosas como:

```text
suposição → fato

possibilidade → probabilidade

probabilidade → certeza

inferência → observação

hipótese → conclusão

fonte → verdade

memória → evidência

coerência → validade

resultado plausível → resultado comprovado
```

Quando uma transição ocorrer, o Harness deve exigir justificativa proporcional.

---

# 14. EVIDÊNCIA

O LLM deve reconhecer diferentes formas de evidência.

Exemplos:

* observação
* documento
* código
* teste
* resultado experimental
* dado quantitativo
* fonte externa
* comparação
* reprodução
* simulação
* análise estatística
* evidência negativa
* contraexemplo.

A presença de uma fonte não significa automaticamente que exista evidência suficiente.

---

# 15. HIERARQUIA DE EVIDÊNCIA

O Harness não deve estabelecer uma hierarquia universal rígida.

A força de uma evidência depende da questão.

Exemplo:

```text
PERGUNTA
   ↓
QUAL MÉTODO É APROPRIADO?
   ↓
QUE EVIDÊNCIA ESSE MÉTODO EXIGE?
   ↓
A EVIDÊNCIA EXISTE?
   ↓
A EVIDÊNCIA É SUFICIENTE?
```

Isso impede que o LLM use a mesma estratégia epistemológica para problemas diferentes.

---

# 16. PROVENIÊNCIA

Sempre que uma afirmação for material para uma decisão, o Harness deve exigir rastreabilidade suficiente para reconstruir:

```text
AFIRMAÇÃO
   ↓
ORIGEM
   ↓
EVIDÊNCIA
   ↓
TRANSFORMAÇÃO
   ↓
INFERÊNCIA
   ↓
VALIDAÇÃO
```

Quando essa cadeia não puder ser estabelecida, o status epistemológico deve ser reduzido proporcionalmente.

---

# 17. INCERTEZA

O LLM deve ser capaz de representar:

* incerteza
* ambiguidade
* insuficiência de evidência
* variabilidade
* limitações de dados
* limitações metodológicas
* conflito
* desconhecimento.

O Harness deve impedir que:

> **ausência de incerteza declarada seja interpretada como ausência de incerteza real.**

---

# 18. CONFIANÇA

Confiança é uma representação do estado epistemológico.

Não é evidência.

Portanto:

```text
LLM diz "tenho alta confiança"
             ≠
evidência forte
```

O Harness deve avaliar se a confiança declarada é proporcional ao suporte.

Quando houver possibilidade de calibração quantitativa, deve-se verificar a correspondência entre confiança declarada e resultados observados.

---

# 19. DESCONHECIMENTO

O sistema deve reconhecer pelo menos quatro situações:

```text
KNOW
KNOW WITH UNCERTAINTY
DO NOT KNOW
CANNOT DETERMINE
```

A diferença é importante.

### Não sei

Falta informação ou conhecimento.

### Não é possível determinar

A informação disponível não permite resolver a questão de maneira adequada.

### Não foi investigado

A questão ainda não passou pelo método apropriado.

### Fora do escopo

O sistema não possui autorização ou capacidade para tratar aquela questão.

---

# 20. ABSTENÇÃO

A abstinência é um comportamento cognitivo válido.

O Harness deve permitir que o LLM diga:

> “Não há evidência suficiente para concluir.”

> “Existem hipóteses concorrentes e não há informação suficiente para diferenciá-las.”

> “Preciso de mais informação.”

> “É necessário executar um teste.”

> “Essa conclusão não pode ser estabelecida com os dados disponíveis.”

O objetivo não é maximizar respostas.

O objetivo é maximizar **conclusões justificáveis**.

---

# 21. HIPÓTESES

Quando houver lacuna de conhecimento, o LLM deve poder formar hipóteses.

Uma hipótese deve ser distinguida de uma conclusão.

Modelo:

```text
PROBLEMA
   ↓
OBSERVAÇÕES
   ↓
HIPÓTESES POSSÍVEIS
   ↓
PREDIÇÕES / CONSEQUÊNCIAS
   ↓
INVESTIGAÇÃO
   ↓
EVIDÊNCIA
   ↓
SUPORTE / ENFRAQUECIMENTO / REFUTAÇÃO
```

---

# 22. MÚLTIPLAS HIPÓTESES

Quando mais de uma explicação for plausível, o Harness deve evitar seleção prematura.

O LLM deve considerar:

```text
H1
H2
H3
...
```

e avaliar:

* evidências favoráveis
* evidências contrárias
* pressupostos
* poder explicativo
* previsões
* inconsistências
* informações necessárias para diferenciação.

---

# 23. ALTERNATIVAS

Uma conclusão relevante deve ser submetida, quando apropriado, à pergunta:

> **“Que outra explicação plausível poderia explicar os mesmos dados?”**

Isso reduz:

* confirmação prematura
* raciocínio circular
* explicação única
* ancoragem
* racionalização pós-hoc.

---

# 24. CONFLITO EPISTÊMICO

Quando fontes ou evidências divergem, o LLM não deve simplesmente escolher uma e descartar a outra.

Deve:

```text
IDENTIFICAR CONFLITO
        ↓
LOCALIZAR ORIGEM
        ↓
COMPARAR CONTEXTO
        ↓
COMPARAR MÉTODOS
        ↓
COMPARAR EVIDÊNCIAS
        ↓
IDENTIFICAR PRESSUPOSTOS
        ↓
DETERMINAR SE É RESOLVÍVEL
        ↓
RESOLVER OU PRESERVAR CONFLITO
```

---

# 25. REGRA DE PRESERVAÇÃO DO CONFLITO

> **Conflito relevante não deve ser apagado para produzir uma resposta mais fluida.**

Quando o conflito não puder ser resolvido, o estado correto pode ser:

```text
CONTESTED
```

ou:

```text
INCONCLUSIVE
```

---

# 26. CONTEXTO

Uma afirmação deve ser interpretada dentro do contexto que a sustenta.

O Harness deve perguntar:

* Onde isso é válido?
* Quando?
* Para quem?
* Sob quais condições?
* Com quais pressupostos?
* Para qual finalidade?

Uma conclusão válida em um contexto pode ser inválida em outro.

---

# 27. TEMPO

Conhecimento pode envelhecer.

O LLM deve considerar:

* data da informação
* data da observação
* mudanças posteriores
* validade temporal
* necessidade de atualização.

O Harness deve detectar situações em que informação antiga está sendo utilizada como se fosse atual.

---

# 28. ESCOPO

O LLM não deve generalizar além daquilo que a evidência sustenta.

Exemplo:

```text
observado em A
        ↓
conclusão sobre A
```

não permite automaticamente:

```text
A
↓
todos os casos
```

O Harness deve detectar **scope overreach**.

---

# 29. CAUSALIDADE

Correlação, associação temporal ou coexistência não devem ser tratadas automaticamente como causalidade.

Quando o LLM fizer afirmação causal, o Harness deve exigir método compatível com causalidade.

A pergunta é:

> **A evidência realmente sustenta causalidade ou apenas associação?**

---

# 30. QUANTIFICAÇÃO

Números aparentam precisão.

Isso cria risco epistemológico.

O Harness deve questionar:

* origem do número
* método de cálculo
* unidade
* população
* período
* precisão justificável
* pressupostos
* margem de erro
* possibilidade de falsa precisão.

Um número preciso pode representar uma estimativa altamente incerta.

---

# 31. INFERÊNCIA

Toda inferência relevante deve possuir:

```text
PREMISSAS
   ↓
MÉTODO DE INFERÊNCIA
   ↓
CONCLUSÃO
```

O Harness deve detectar quando a conclusão não decorre adequadamente das premissas.

---

# 32. RACIOCÍNIO ABDUTIVO

Quando o LLM estiver procurando uma explicação, o Harness deve reconhecer que ele está realizando inferência abdutiva.

Nesse caso:

```text
OBSERVAÇÕES
   ↓
EXPLICAÇÕES POSSÍVEIS
   ↓
MELHOR EXPLICAÇÃO ATUAL
```

não significa:

```text
MELHOR EXPLICAÇÃO ATUAL
=
VERDADE ESTABELECIDA
```

---

# 33. RACIOCÍNIO DEDUTIVO

Quando uma conclusão depender de premissas:

```text
P1
+
P2
↓
C
```

o Harness deve avaliar:

* validade da estrutura
* validade das premissas
* aplicabilidade das premissas ao caso.

Um raciocínio formalmente correto com premissa falsa continua epistemicamente comprometido.

---

# 34. RACIOCÍNIO INDUTIVO

Quando o LLM generalizar a partir de exemplos, o Harness deve verificar:

* tamanho da amostra
* representatividade
* seleção
* exceções
* estabilidade
* possibilidade de generalização.

---

# 35. INVESTIGAÇÃO

O LLM não deve investigar automaticamente da mesma forma em todas as tarefas.

A pergunta deve determinar o método.

```text
TIPO DE QUESTÃO
      ↓
OBJETIVO DE CONHECIMENTO
      ↓
MÉTODO DE INQUÉRITO
      ↓
EVIDÊNCIA NECESSÁRIA
      ↓
VALIDAÇÃO
```

A especificação detalhada dos métodos pertence ao **Master Inquiry Methods Guide**.

---

# 36. CRITÉRIO PARA INVESTIGAR

O Harness deve orientar o LLM a investigar quando:

* a informação disponível é insuficiente
* a afirmação é material para a decisão
* existe conflito relevante
* a informação pode estar desatualizada
* a afirmação é verificável externamente
* o custo de erro é relevante
* a conclusão depende de fato desconhecido.

---

# 37. CRITÉRIO PARA PERGUNTAR

O LLM deve solicitar informação quando:

```text
a resposta depende criticamente
de uma variável desconhecida
```

e essa variável não pode ser determinada com segurança por investigação disponível.

Perguntar não deve ser utilizado para evitar raciocínio que poderia ser realizado com informação já disponível.

---

# 38. CRITÉRIO PARA TESTAR

Quando uma afirmação puder ser validada por teste, o LLM deve preferir:

```text
TESTAR
```

a:

```text
ARGUMENTAR SOBRE O RESULTADO
```

quando o teste possuir custo e risco aceitáveis.

No contexto de Claude Code, isso significa priorizar:

* inspeção
* execução de testes
* reprodução
* verificação
* análise de artefatos
* validação objetiva.

---

# 39. CRITÉRIO PARA CONCLUIR

O LLM pode concluir quando:

1. a pergunta estiver suficientemente definida
2. o método for adequado
3. as evidências forem suficientes para o nível de afirmação
4. conflitos relevantes tiverem sido resolvidos ou explicitados
5. limitações relevantes forem conhecidas
6. a conclusão estiver dentro do escopo da evidência.

---

# 40. CRITÉRIO PARA NÃO CONCLUIR

O LLM deve evitar conclusão definitiva quando:

* evidência insuficiente
* conflito não resolvido
* hipótese não testada
* escopo inadequado
* informação crítica ausente
* método inadequado
* incerteza incompatível com o uso pretendido.

---

# 41. CONHECIMENTO OPERACIONAL

O objetivo da epistemologia aplicada ao LLM não é alcançar certeza filosófica absoluta.

É permitir que o sistema saiba:

```text
O QUE PODE AFIRMAR
O QUE PODE INFERIR
O QUE PODE PROPOR
O QUE DEVE INVESTIGAR
O QUE DEVE TESTAR
O QUE DEVE QUESTIONAR
O QUE DEVE RECUSAR-SE A CONCLUIR
```

---

# 42. FORMAÇÃO DE CONHECIMENTO

O Harness deve distinguir:

```text
ACQUISITION
    ↓
UNDERSTANDING
    ↓
FORMATION
    ↓
VALIDATION
    ↓
USE
```

Aquisição não significa formação.

Formação não significa validação.

Validação não significa autorização universal.

---

# 43. CONHECIMENTO CANDIDATO

Durante o raciocínio, o LLM pode produzir:

> **Conhecimento Candidato**

Esse estado significa:

> proposição considerada suficientemente relevante para investigação ou utilização provisória, mas ainda não necessariamente estabelecida.

Isso é especialmente importante em:

* RAG
* agentes especialistas
* pesquisa
* engenharia
* análise de mercado
* sistemas multiagentes.

---

# 44. ATUALIZAÇÃO

Quando nova evidência surgir, o LLM deve ser capaz de revisar uma conclusão anterior.

O comportamento esperado é:

```text
CONCLUSÃO ANTERIOR
       ↓
NOVA EVIDÊNCIA
       ↓
REAVALIAÇÃO
       ↓
MANTER
REVISAR
ENFRAQUECER
REFUTAR
```

Persistir uma conclusão anterior não deve impedir sua revisão.

---

# 45. ERRO

O erro não deve ser tratado apenas como resultado incorreto.

Existem pelo menos:

```text
ERROR OF FACT
ERROR OF INFERENCE
ERROR OF METHOD
ERROR OF EVIDENCE
ERROR OF SCOPE
ERROR OF CALIBRATION
ERROR OF EPISTEMIC STATUS
ERROR OF DECISION
```

Essa distinção é essencial para diagnóstico do Harness.

---

# 46. FALHA EPISTÊMICA

Uma falha epistemológica ocorre quando o LLM:

> atribui a uma afirmação um status superior ao que suas evidências, método ou contexto permitem.

Exemplos:

```text
HIPÓTESE → FATO
INFERÊNCIA → OBSERVAÇÃO
FONTE NÃO VERIFICADA → EVIDÊNCIA FORTE
CORRELAÇÃO → CAUSALIDADE
POSSIBILIDADE → PROBABILIDADE
PROBABILIDADE → CERTEZA
```

---

# 47. COGNITIVE DRIFT

O Harness deve observar se o LLM começa com:

> “uma possibilidade é X”

e termina com:

> “X é a causa”.

Esse fenômeno representa uma transformação indevida do estado epistêmico durante o raciocínio.

O Harness deve detectar esse tipo de drift.

---

# 48. MEMORY CONTAMINATION

O LLM pode utilizar uma informação anterior como se fosse evidência atual.

O Harness deve distinguir:

```text
MEMÓRIA
≠
EVIDÊNCIA ATUAL
```

Memória pode orientar investigação.

Não deve ser automaticamente promovida a evidência.

---

# 49. CONTEXT CONTAMINATION

Informação presente no contexto pode parecer válida simplesmente por estar presente.

O Harness deve exigir:

> **presença contextual não equivale a validade epistemológica.**

Isso é especialmente relevante em contextos longos e sistemas agentivos.

---

# 50. LOST-IN-THE-MIDDLE E CONTEXT ROT

O Harness deve considerar limitações conhecidas dos LLMs em contextos longos.

Informação importante pode:

* ser perdida
* receber peso inadequado
* ser esquecida
* ser sobreposta por informação posterior
* sofrer competição contextual.

Portanto, o Harness não deve depender exclusivamente de:

> “colocar toda a informação no contexto”.

Quando a informação for epistemicamente crítica, deve haver mecanismos para:

* destacar evidências críticas
* recuperar evidências
* verificar novamente
* reduzir contexto irrelevante
* validar referências
* testar coerência contra fontes primárias.

---

# 51. REGRA DE EVIDÊNCIA CRÍTICA

Quanto mais crítica uma afirmação, menos o Harness deve depender da memória implícita do LLM.

A informação crítica deve ser:

```text
EXPLICITAMENTE DISPONÍVEL
+
LOCALIZÁVEL
+
VERIFICÁVEL
+
RASTREÁVEL
```

---

# 52. RAG

RAG deve ser tratado como mecanismo de recuperação.

Não como autoridade epistemológica.

A sequência correta é:

```text
RAG
 ↓
RECUPERAÇÃO
 ↓
CANDIDATOS DE EVIDÊNCIA
 ↓
AVALIAÇÃO
 ↓
INTERPRETAÇÃO
 ↓
FORMAÇÃO DE CONHECIMENTO
```

O Harness deve impedir:

```text
RETRIEVED
=
TRUE
```

---

# 53. MULTIAGENTE

Em sistemas multiagentes, consenso entre agentes não deve ser tratado automaticamente como verdade.

Exemplo:

```text
Agent A → X
Agent B → X
Agent C → X
```

não implica:

```text
X = VALIDATED
```

O Harness deve investigar:

* independência das análises
* fontes utilizadas
* métodos
* evidências
* possível contaminação entre agentes
* correlação das falhas.

---

# 54. DIVERSIDADE EPISTÊMICA

Quando apropriado, o Harness pode exigir perspectivas independentes.

Exemplo:

```text
HIPÓTESE
   ├── análise favorável
   ├── análise contrária
   ├── análise independente
   └── evidência externa
```

O objetivo não é produzir discordância artificial.

É reduzir o risco de confirmação circular.

---

# 55. ADVERSARIAL EPISTEMICS

Para afirmações críticas, o Harness deve poder solicitar:

> “Tente provar que sua conclusão está errada.”

Ou:

> “Qual evidência faria você abandonar essa hipótese?”

Ou:

> “Qual é a melhor explicação alternativa?”

Isso transforma falsificação em operação cognitiva.

---

# 56. RED TEAM EPISTÊMICO

Uma etapa adversarial pode procurar:

* premissas ocultas
* evidência ausente
* contradições
* generalizações
* causalidade indevida
* dados enviesados
* informação desatualizada
* explicações alternativas
* falsa precisão.

---

# 57. HARNESS EPISTÊMICO

O Harness deve ser composto conceitualmente por:

```text
┌──────────────────────────────────────────┐
│          EPISTEMIC COGNITIVE HARNESS     │
├──────────────────────────────────────────┤
│ Claim Detector                            │
│ Evidence Checker                          │
│ Epistemic State Checker                   │
│ Assumption Detector                       │
│ Inference Checker                         │
│ Uncertainty Checker                       │
│ Conflict Detector                         │
│ Scope Checker                             │
│ Temporal Checker                          │
│ Alternative-Hypothesis Checker            │
│ Provenance Checker                         │
│ Falsification Checker                     │
│ Calibration Checker                       │
│ Cognitive-Drift Detector                  │
│ Adversarial Evaluator                     │
│ Decision Gate                             │
└──────────────────────────────────────────┘
```

Esses elementos são **funções do Harness**, não necessariamente componentes de software.

---

# 58. SENSOR

Um sensor detecta uma condição.

Exemplos:

```text
"Existe uma afirmação factual?"
"Existe uma inferência?"
"Existe evidência?"
"Existe conflito?"
"Existe uma hipótese?"
"Existe incerteza?"
"Existe extrapolação?"
```

---

# 59. VALIDATOR

Um validator compara o comportamento observado com o critério epistemológico.

Exemplo:

```text
Claim:
"X causa Y."

Evidence:
correlation only.

Validator:
CAUSALITY NOT ESTABLISHED
```

---

# 60. GATE

O gate determina se o LLM pode prosseguir.

Estados possíveis:

```text
PASS
PASS WITH UNCERTAINTY
REWORK
INVESTIGATE
REQUEST INFORMATION
TEST REQUIRED
ESCALATE
BLOCK
```

---

# 61. FEEDBACK

O Harness deve preferir feedback acionável.

Em vez de:

> “Raciocínio insuficiente.”

deve produzir:

> “A conclusão causal não está sustentada pela evidência apresentada. Diferencie associação de causalidade e indique qual método permitiria estabelecer a relação causal.”

---

# 62. LOOP DE CORREÇÃO

O modelo geral:

```text
LLM
 ↓
COGNITIVE OUTPUT
 ↓
HARNESS
 ↓
DETECTION
 ↓
DIAGNOSIS
 ↓
FEEDBACK
 ↓
LLM REVISION
 ↓
HARNESS
```

O objetivo é permitir convergência para um estado epistemicamente aceitável.

---

# 63. ESCALADA

O Harness deve poder determinar:

```text
CONTINUE
INVESTIGATE
ASK HUMAN
RUN TEST
SEARCH EXTERNAL SOURCE
REQUEST SPECIALIST
REVIEW PREVIOUS WORK
BLOCK
```

A escolha depende do impacto, incerteza e custo.

---

# 64. PRINCÍPIO DA PROPORCIONALIDADE

Nem toda tarefa necessita do mesmo rigor.

```text
BAIXO IMPACTO
→ verificação simples

MÉDIO IMPACTO
→ evidência + validação

ALTO IMPACTO
→ investigação + validação + adversarial review

CRÍTICO
→ múltiplas evidências + validação independente +
   Harness + possibilidade de intervenção humana
```

---

# 65. ECONOMICIDADE COGNITIVA

O Harness não deve transformar toda operação em auditoria pesada.

Deve otimizar:

**rigor necessário / custo cognitivo**

Assim:

> **quanto maior o impacto potencial de uma conclusão, maior o rigor exigido.**

Quanto menor o impacto:

> **maior liberdade cognitiva, desde que não haja violação de invariantes fundamentais.**

---

# 66. EPISTEMIC QUALITY GATES

A especificação pode derivar gates como:

```text
GATE-EPI-01
Claim Identification

GATE-EPI-02
Evidence Adequacy

GATE-EPI-03
Epistemic Classification

GATE-EPI-04
Inference Validity

GATE-EPI-05
Uncertainty Disclosure

GATE-EPI-06
Conflict Resolution

GATE-EPI-07
Scope Validation

GATE-EPI-08
Alternative Explanation

GATE-EPI-09
Validation

GATE-EPI-10
Conclusion Authorization
```

Os gates são derivados do MEG.

O MEG não é o gate.

---

# 67. INVARIANTES EPISTÊMICOS

Todo Harness derivado deve considerar pelo menos:

### INV-EPI-001

O LLM não deve apresentar hipótese como fato.

### INV-EPI-002

O LLM não deve apresentar inferência como observação.

### INV-EPI-003

O LLM não deve utilizar confiança como substituto de evidência.

### INV-EPI-004

O LLM deve declarar incerteza material.

### INV-EPI-005

Conflitos relevantes devem ser preservados.

### INV-EPI-006

Conclusões não podem exceder o escopo das evidências.

### INV-EPI-007

A origem de evidências críticas deve ser rastreável.

### INV-EPI-008

O LLM deve poder declarar desconhecimento.

### INV-EPI-009

O LLM deve poder revisar conclusões diante de nova evidência.

### INV-EPI-010

A mudança de status epistemológico deve ser justificável.

---

# 68. COMPORTAMENTOS PROIBIDOS

O Harness deve detectar, no mínimo:

```text
HALLUCINATION
UNSUPPORTED CLAIM
FALSE CERTAINTY
SOURCE FABRICATION
SOURCE MISATTRIBUTION
HIDDEN ASSUMPTION
UNJUSTIFIED INFERENCE
CAUSALITY OVERREACH
SCOPE OVERREACH
TEMPORAL OVERREACH
CONFLICT SUPPRESSION
CONFIRMATION BIAS
PREMATURE CLOSURE
FALSE PRECISION
MEMORY-AS-EVIDENCE
CONSENSUS-AS-TRUTH
RAG-AS-TRUTH
```

---

# 69. COMPORTAMENTOS OBRIGATÓRIOS

Quando aplicável, o LLM deve:

```text
CLASSIFICAR AFIRMAÇÕES
IDENTIFICAR EVIDÊNCIAS
DECLARAR ASSUMPTIONS
DECLARAR INCERTEZA
CONSIDERAR ALTERNATIVAS
IDENTIFICAR CONFLITOS
VERIFICAR ESCOPO
INVESTIGAR QUANDO NECESSÁRIO
TESTAR QUANDO POSSÍVEL
REVISAR QUANDO SURGIR NOVA EVIDÊNCIA
ABSTER-SE QUANDO NECESSÁRIO
```

---

# 70. CRITÉRIO DE SUFICIÊNCIA EPISTÊMICA

Uma conclusão não deve ser avaliada apenas por:

```text
"Está correta?"
```

Mas por:

```text
A questão está bem definida?
+
O método é apropriado?
+
A evidência é suficiente?
+
A inferência é válida?
+
As alternativas foram consideradas?
+
Os conflitos foram tratados?
+
A incerteza foi representada?
+
O escopo foi respeitado?
+
A conclusão é proporcional à evidência?
```

---

# 71. MÉTRICAS DO HARNESS

O Harness pode medir:

### Unsupported Claim Rate

Percentual de afirmações relevantes sem suporte adequado.

### Epistemic Misclassification Rate

Percentual de afirmações classificadas incorretamente.

### Overclaim Rate

Percentual de conclusões que excedem a evidência.

### Calibration

Correspondência entre confiança declarada e resultado.

### Abstention Quality

Qualidade das situações em que o sistema decidiu não concluir.

### Conflict Preservation

Capacidade de preservar conflitos relevantes.

### Revision Quality

Capacidade de atualizar conclusões diante de novas evidências.

### Provenance Coverage

Percentual de afirmações críticas com rastreabilidade adequada.

### Cognitive Drift Rate

Frequência de mudança indevida de status epistemológico durante o raciocínio.

---

# 72. RESULTADO NÃO É SUFICIENTE

Uma conclusão correta pode resultar de raciocínio epistemicamente ruim.

Uma conclusão incorreta pode resultar de investigação epistemicamente adequada.

Portanto:

```text
OUTCOME
  ≠
EPISTEMIC PROCESS
```

O Harness deve avaliar ambos.

---

# 73. QUALIDADE EPISTÊMICA

A qualidade epistemológica de uma operação cognitiva pode ser representada conceitualmente como:

```text
Epistemic Quality
=
Evidence
+
Method
+
Inference
+
Uncertainty
+
Scope
+
Traceability
+
Revision Capacity
```

Não deve ser reduzida a uma única pontuação universal.

---

# 74. RELAÇÃO COM SDD

A camada epistêmica deve ser incorporada ao SDD.

Fluxo:

```text
DISCOVERY
   ↓
EPISTEMIC CLASSIFICATION
   ↓
PROBLEM MODEL
   ↓
HYPOTHESES
   ↓
EVIDENCE
   ↓
SPECIFICATION
   ↓
IMPLEMENTATION
   ↓
VALIDATION
```

Isso impede que uma suposição inicial seja silenciosamente transformada em requisito.

---

# 75. ESPECIFICAÇÃO EPISTÊMICA DURANTE ENGENHARIA

No Claude Code, por exemplo, uma afirmação como:

> “Esse arquivo precisa ser alterado porque a arquitetura exige isso.”

deve poder ser questionada pelo Harness:

```text
Isso é:
[ ] requisito
[ ] evidência observada
[ ] decisão registrada
[ ] inferência
[ ] hipótese
[ ] recomendação
```

O LLM deve então fundamentar a classificação.

---

# 76. REQUISITO COMO OBJETO EPISTÊMICO

Um requisito de engenharia não deve nascer automaticamente de qualquer afirmação.

Fluxo recomendado:

```text
OBSERVAÇÃO
    ↓
PROBLEMA
    ↓
INTERPRETAÇÃO
    ↓
HIPÓTESE
    ↓
VALIDAÇÃO
    ↓
DECISÃO
    ↓
REQUISITO
```

Quando o requisito for baseado em premissa não validada, isso deve permanecer explícito.

---

# 77. CLAUDE CODE

O MEG-001 é particularmente aplicável ao Claude Code porque seu funcionamento envolve:

* leitura de artefatos
* exploração de repositórios
* interpretação de requisitos
* planejamento
* modificação de arquivos
* execução de testes
* análise de resultados
* revisão.

O Harness deve governar essas operações cognitivamente.

Não basta verificar o código produzido.

Deve verificar **por que o agente decidiu produzi-lo**.

---

# 78. PADRÃO COGNITIVO PARA CLAUDE CODE

Antes de uma alteração material:

```text
1. O que sabemos?
2. Como sabemos?
3. O que estamos inferindo?
4. O que ainda não sabemos?
5. Qual evidência sustenta a alteração?
6. Existem alternativas?
7. Qual é o impacto?
8. Como podemos validar?
```

Depois da alteração:

```text
1. O resultado corresponde à intenção?
2. Os testes sustentam a conclusão?
3. Surgiram efeitos colaterais?
4. Alguma premissa foi invalidada?
5. O conhecimento anterior precisa ser revisado?
```

---

# 79. REGRA DE INSPEÇÃO ANTES DE ALTERAÇÃO

Quando uma alteração de código depender de uma afirmação sobre o sistema, o Harness deve favorecer:

```text
INSPECIONAR
   ↓
COMPREENDER
   ↓
FORMAR HIPÓTESE
   ↓
VALIDAR
   ↓
ALTERAR
```

e não:

```text
SUPOR
   ↓
ALTERAR
   ↓
JUSTIFICAR
```

---

# 80. REGRA DE VERIFICAÇÃO PÓS-AÇÃO

Depois de qualquer ação relevante:

```text
AÇÃO
 ↓
OBSERVAÇÃO DO RESULTADO
 ↓
COMPARAÇÃO COM EXPECTATIVA
 ↓
VALIDAÇÃO
 ↓
ATUALIZAÇÃO EPISTÊMICA
```

O sucesso aparente da ação não deve ser tratado automaticamente como prova de que a hipótese original estava correta.

---

# 81. HUMAN-IN-THE-LOOP

Intervenção humana deve ser definida epistemicamente.

O Harness pode exigir intervenção quando:

* impacto alto
* evidência insuficiente
* conflito irreconciliável
* decisão irreversível
* desconhecimento crítico
* mudança arquitetural material
* exceção não prevista.

O humano não deve ser usado simplesmente como substituto de qualquer raciocínio que o LLM poderia executar adequadamente.

---

# 82. ESCALA DE AUTONOMIA

A autonomia do LLM deve ser proporcional à confiança epistemicamente justificada.

```text
LOW EVIDENCE
     ↓
HIGH HUMAN OVERSIGHT

STRONG EVIDENCE
     ↓
GREATER AUTONOMY
```

Porém:

> confiança não deve ser baseada exclusivamente na autodeclaração do LLM.

---

# 83. EPISTEMIC RECOVERY

Quando o Harness detectar erro, deve existir mecanismo de recuperação:

```text
DETECT
 ↓
FREEZE CONCLUSION
 ↓
IDENTIFY ERROR TYPE
 ↓
REOPEN INVESTIGATION
 ↓
REASSESS EVIDENCE
 ↓
REVISE
 ↓
VALIDATE
 ↓
CONTINUE
```

O erro não deve ser simplesmente sobrescrito.

---

# 84. REGRESSÃO EPISTÊMICA

Erros anteriores devem poder alimentar avaliações futuras.

Exemplo:

```text
PAST FAILURE
      ↓
PATTERN
      ↓
HARNESS TEST
      ↓
FUTURE DETECTION
```

Isso transforma experiência em melhoria do Harness.

---

# 85. ADVERSARIAL HARNESS

O Harness deve testar o LLM em situações como:

* informação incompleta
* fonte contraditória
* requisito ambíguo
* evidência falsa
* instrução conflitante
* hipótese sedutora
* contexto excessivo
* contexto insuficiente
* dado desatualizado
* falso consenso
* resultado aparentemente correto obtido por método incorreto.

O objetivo é verificar se o LLM mantém seu estado epistemológico sob pressão.

---

# 86. TESTE DE ESTABILIDADE

Uma propriedade importante:

> **A pressão para produzir uma resposta não deve fazer o LLM abandonar seus critérios epistemológicos.**

Exemplo:

```text
Usuário:
"Não questione, apenas implemente."

Harness:
Existe evidência suficiente?

Se NÃO:
INVESTIGATE / ASK / BLOCK
```

---

# 87. TESTE DE RESISTÊNCIA À AUTORIDADE

O Harness deve avaliar se o LLM aceita uma afirmação apenas porque:

* foi dita por um agente superior
* está em documentação aparentemente oficial
* foi repetida várias vezes
* está no contexto inicial
* foi produzida anteriormente pelo próprio sistema.

Autoridade pode aumentar relevância.

Não substitui avaliação epistemológica.

---

# 88. TESTE DE CONSISTÊNCIA

O LLM deve manter distinções epistemológicas consistentes ao longo da tarefa.

Se disser:

> “X é apenas hipótese”

não deve posteriormente usar X como:

> “fato estabelecido”

sem nova justificativa.

---

# 89. TESTE DE REVERSIBILIDADE COGNITIVA

O Harness deve ser capaz de perguntar:

> “Que evidência faria você mudar de opinião?”

Se o LLM não consegue identificar condições razoáveis de revisão, isso pode indicar:

* fechamento prematuro
* racionalização
* crença rígida
* ausência de falsificabilidade.

---

# 90. FALSIFICABILIDADE OPERACIONAL

Para hipóteses relevantes, o Harness deve procurar:

```text
O que teria que ser observado
para demonstrar que essa hipótese está errada?
```

Quando nenhuma condição puder ser concebida, o sistema deve reconhecer que a proposição pode estar fora de um regime investigável.

---

# 91. PRINCÍPIO DA TRANSPARÊNCIA EPISTÊMICA

O LLM deve tornar explícito, quando material:

```text
FATO
INFERÊNCIA
HIPÓTESE
SUPOSIÇÃO
INCERTEZA
LIMITAÇÃO
CONFLITO
CONCLUSÃO
```

Isso não significa exigir exposição integral do raciocínio interno.

Significa exigir **artefatos verificáveis de justificativa**, suficientes para o Harness avaliar o estado epistemológico.

---

# 92. RASTREABILIDADE SEM DEPENDER DE CHAIN-OF-THOUGHT

O Harness não deve depender da exposição integral do raciocínio privado do modelo.

Pode utilizar:

* evidências citadas
* decisões
* premissas
* resultados de testes
* justificativas resumidas
* artefatos
* referências
* estados epistemológicos
* resultados verificáveis.

O objetivo é governar o processo sem exigir exposição indiscriminada do raciocínio interno.

---

# 93. EPISTEMIC CHECKPOINT

Em tarefas complexas, o Harness deve criar checkpoints:

```text
CHECKPOINT 1
O problema foi corretamente compreendido?

CHECKPOINT 2
As premissas estão sustentadas?

CHECKPOINT 3
A hipótese é necessária?

CHECKPOINT 4
As evidências são suficientes?

CHECKPOINT 5
A conclusão é proporcional?

CHECKPOINT 6
A ação foi validada?
```

---

# 94. CICLO EPISTÊMICO

O ciclo geral é:

```text
┌───────────────┐
│ OBSERVE       │
└───────┬───────┘
        ▼
┌───────────────┐
│ CLASSIFY      │
└───────┬───────┘
        ▼
┌───────────────┐
│ QUESTION      │
└───────┬───────┘
        ▼
┌───────────────┐
│ INVESTIGATE   │
└───────┬───────┘
        ▼
┌───────────────┐
│ EVALUATE      │
└───────┬───────┘
        ▼
┌───────────────┐
│ INFER         │
└───────┬───────┘
        ▼
┌───────────────┐
│ CONCLUDE      │
└───────┬───────┘
        ▼
┌───────────────┐
│ ACT           │
└───────┬───────┘
        ▼
┌───────────────┐
│ OBSERVE RESULT│
└───────┬───────┘
        │
        └──────────────► REVISE
```

---

# 95. RELAÇÃO COM O MASTER PRINCIPIOLOGICAL GUIDE

A relação deve ser:

```text
PRINCIPIOLOGIA
      ↓
define orientação

EPISTEMOLOGIA
      ↓
define critérios de conhecimento

INQUÉRITO
      ↓
define métodos de investigação

HARNESS
      ↓
verifica aplicação

LLM
      ↓
executa cognição
```

Princípios não substituem epistemologia.

Epistemologia não substitui métodos.

Métodos não substituem Harness.

Harness não substitui cognição.

---

# 96. RELAÇÃO COM O MASTER INQUIRY METHODS GUIDE

O MEG-001 responde:

> **O que precisamos considerar conhecimento e que condições justificam uma conclusão?**

O Inquiry Guide responderá:

> **Qual método deve ser utilizado para investigar essa questão?**

Assim:

```text
MEG
↓
CRITÉRIOS EPISTÊMICOS

GMI
↓
MÉTODO DE INVESTIGAÇÃO

HARNESS
↓
VERIFICAÇÃO DA APLICAÇÃO
```

---

# 97. RELAÇÃO COM O SDD

SDD determina como transformar conhecimento governado em especificação.

A epistemologia determina:

> **quão justificada está a informação que originou a especificação.**

Portanto:

```text
EPISTEMOLOGIA
      ↓
VALIDA BASE DE CONHECIMENTO
      ↓
SDD
      ↓
ESPECIFICAÇÃO
      ↓
IMPLEMENTAÇÃO
      ↓
VALIDAÇÃO
```

---

# 98. PRINCÍPIO DE NÃO-PULAR CAMADAS

O LLM não deve fazer:

```text
INFORMAÇÃO
↓
CÓDIGO
```

sem passar por:

```text
COMPREENSÃO
↓
PROBLEMA
↓
HIPÓTESE
↓
VALIDAÇÃO
↓
ESPECIFICAÇÃO
```

Quando a tarefa permitir simplificação, o Harness pode reduzir formalidade.

Mas não deve permitir que uma simplificação elimine um controle epistemicamente necessário.

---

# 99. CRITÉRIO DE NECESSÁRIO E SUFICIENTE

A epistemologia do Harness deve buscar:

> **o menor conjunto de controles capaz de manter a qualidade epistemológica necessária ao risco da tarefa.**

Não deve:

* burocratizar tarefas simples
* exigir documentação excessiva
* exigir investigação desnecessária
* exigir certeza impossível.

Deve:

* impedir erros críticos
* tornar incertezas relevantes visíveis
* preservar rastreabilidade necessária
* exigir validação proporcional.

---

# 100. UNIDADE ATÔMICA DE ESPECIFICAÇÃO

Toda regra derivada do MEG deve poder ser especificada assim:

```text
EPI-ID:
Nome:

Intenção:
Qual comportamento epistemológico deseja-se governar?

Contexto:
Quando se aplica?

Gatilho:
O que ativa o controle?

Objeto:
Qual afirmação, inferência ou decisão está sendo analisada?

Critério:
O que o LLM deve demonstrar?

Evidência:
O que deve sustentar a operação?

Comportamento esperado:
O que o LLM deve fazer?

Comportamento proibido:
O que não deve fazer?

Harness:
Como detectar?

Validator:
Como avaliar?

Gate:
O que acontece se falhar?

Feedback:
Como orientar correção?

Escalonamento:
Quando investigar, perguntar ou envolver humano?

Registro:
O que precisa permanecer rastreável?
```

---

# 101. REQUISITOS PARA UM HARNESS DERIVADO

Todo Harness epistemológico derivado do MEG-001 deve possuir:

```text
OBSERVABILITY
DETECTION
CLASSIFICATION
VALIDATION
FEEDBACK
GATING
RECOVERY
TRACEABILITY
REGRESSION
EVALUATION
```

---

# 102. O QUE O HARNESS NÃO DEVE FAZER

O Harness não deve:

* tentar substituir o LLM
* impor um método único para todos os problemas
* exigir certeza onde ela é impossível
* bloquear toda hipótese
* confundir discordância com erro
* substituir evidência por consenso
* transformar métricas em verdade
* transformar regras em princípios
* criar burocracia sem benefício epistemológico.

---

# 103. O QUE O HARNESS DEVE FAZER

O Harness deve:

* detectar afirmações relevantes
* verificar status epistemológico
* exigir evidência proporcional
* identificar inferências
* detectar extrapolações
* detectar conflito
* exigir incerteza quando necessária
* solicitar investigação quando necessário
* solicitar teste quando possível
* bloquear conclusões inadequadas
* permitir revisão
* registrar falhas
* transformar falhas em testes futuros.

---

# 104. GOVERNANÇA DA PRÓPRIA EPISTEMOLOGIA

A epistemologia do sistema também pode estar errada.

Portanto, o MEG exige:

```text
EPISTEMOLOGIA
      ↓
VALIDAÇÃO
      ↓
OBSERVAÇÃO DE FALHAS
      ↓
REVISÃO
      ↓
NOVA VERSÃO
```

Nenhum conjunto de regras epistemológicas deve ser considerado perfeito ou imutável.

---

# 105. EVOLUÇÃO DO HARNESS

Falhas reais devem alimentar evolução:

```text
INCIDENT
 ↓
ANÁLISE
 ↓
CLASSIFICAÇÃO EPISTÊMICA
 ↓
NOVO TESTE
 ↓
NOVO SENSOR / VALIDATOR / GATE
 ↓
REGRESSÃO
```

Isso transforma o Harness em um sistema de aprendizagem de engenharia, sem necessariamente permitir que o LLM altere autonomamente seus próprios controles.

---

# 106. CRITÉRIO DE MATURIDADE DO HARNESS

### Nível 0 — Sem governança

LLM responde livremente.

### Nível 1 — Instrução

Princípios epistemológicos no prompt.

### Nível 2 — Verificação

Harness verifica comportamentos básicos.

### Nível 3 — Gates

Falhas relevantes interrompem o fluxo.

### Nível 4 — Investigação adaptativa

Harness determina quando pesquisar, perguntar ou testar.

### Nível 5 — Adversarial

Harness procura ativamente falhas epistemológicas.

### Nível 6 — Aprendizado de governança

Falhas reais alimentam regressão e evolução do Harness.

Esses níveis descrevem maturidade da governança, não qualidade de um LLM.

---

# 107. CRITÉRIO DE COMPLETUDE DO MEG-001

O Master Guide será considerado suficiente quando permitir derivar, sem redefinir seus fundamentos:

```text
Epistemic Principles
Epistemic Invariants
Epistemic States
Evidence Rules
Uncertainty Rules
Inference Rules
Hypothesis Rules
Conflict Rules
Abstention Rules
Inquiry Triggers
Validation Gates
Harness Sensors
Harness Validators
Harness Gates
Feedback Patterns
Adversarial Tests
Metrics
Recovery Rules
Regression Tests
```

---

# 108. TESTE FINAL DE COERÊNCIA

Antes de utilizar uma especificação derivada do MEG-001, deve ser possível responder:

### Sobre conhecimento

* O que o LLM sabe?
* Como sabemos que sabe?
* O que apenas acredita?
* O que está inferindo?
* O que é hipótese?
* O que desconhece?

### Sobre evidência

* Qual evidência sustenta a conclusão?
* É suficiente?
* É apropriada ao tipo de questão?
* Existe evidência contrária?

### Sobre raciocínio

* Qual método foi utilizado?
* Existem pressupostos?
* Existem alternativas?
* Houve extrapolação?

### Sobre incerteza

* O que permanece incerto?
* A confiança é proporcional?
* O sistema deveria abster-se?

### Sobre ação

* Qual o impacto de errar?
* O rigor utilizado é proporcional?
* É necessário teste ou aprovação humana?

### Sobre Harness

* Como tudo isso será detectado?
* O que bloqueia?
* O que apenas alerta?
* Como o LLM corrige?
* Como a falha vira regressão?

---

# 109. PRINCÍPIO-MESTRE

O princípio central do MEG-001 é:

> **O LLM não deve ser governado apenas pela obrigação de produzir uma resposta, mas pela obrigação de manter correspondência entre o que afirma, aquilo que pode justificar, o método pelo qual chegou à conclusão, a incerteza existente e os limites do conhecimento disponível.**

---

# 110. FÓRMULA CONCEITUAL

A relação fundamental pode ser expressa como:

```text
AFIRMAÇÃO
+
EVIDÊNCIA
+
MÉTODO
+
JUSTIFICAÇÃO
+
CONTEXTO
+
INCERTEZA
+
VALIDAÇÃO
=
ESTADO EPISTÊMICO
```

E:

```text
ESTADO EPISTÊMICO
+
IMPACTO
+
RISCO
=
NÍVEL DE GOVERNANÇA NECESSÁRIO
```

E:

```text
GOVERNANÇA NECESSÁRIA
+
HARNESS
=
COMPORTAMENTO COGNITIVO CONTROLADO
```

---

# 111. RESULTADO ARQUITETURAL

O resultado final não é um módulo epistemológico.

É uma **disciplina de engenharia da cognição do LLM**.

```text
                 MASTER PRINCIPIOLOGY
                         │
                         ▼
                  MEG-001 EPISTEMOLOGY
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      EPISTEMIC CRITERIA       COGNITIVE STATES
             │                       │
             └───────────┬───────────┘
                         ▼
                 INQUIRY METHODS
                         │
                         ▼
                    COGNITIVE
                     HARNESS
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           SENSORS    VALIDATORS   GATES
              │          │          │
              └──────────┼──────────┘
                         ▼
                        LLM
                         │
                         ▼
                  ENGINEERING WORK
                         │
                         ▼
                     EVIDENCE
                         │
                         ▼
                    VALIDATION
                         │
                         ▼
                     FEEDBACK
                         │
                         └──────────► LLM
```

---

# 112. APLICAÇÃO AO CLAUDE CODE

No contexto do Claude Code, o MEG-001 deve resultar em um Harness capaz de transformar operações como:

```text
"Leia o projeto e implemente X."
```

em um processo cognitivo governado:

```text
ENTENDER
   ↓
INSPECIONAR
   ↓
DISTINGUIR FATO / INFERÊNCIA / HIPÓTESE
   ↓
IDENTIFICAR LACUNAS
   ↓
INVESTIGAR
   ↓
FORMAR MODELO
   ↓
VALIDAR
   ↓
ESPECIFICAR
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
OBSERVAR RESULTADO
   ↓
REVISAR CONCLUSÕES
```

O objetivo não é fazer Claude produzir mais texto.

O objetivo é fazer Claude **errar menos epistemicamente antes de produzir trabalho**.

---

# 113. RELAÇÃO COM OS DEMAIS MASTER GUIDES

A família de documentos deve permanecer:

```text
┌────────────────────────────────────────────┐
│ MASTER PRINCIPIOLOGICAL GUIDE              │
│                                             │
│ Como orientar a cognição                    │
└──────────────────────┬─────────────────────┘
                       ▼
┌────────────────────────────────────────────┐
│ MEG-001                                     │
│ MASTER EPISTEMOLOGICAL GUIDE                │
│                                             │
│ Como governar conhecimento                  │
└──────────────────────┬─────────────────────┘
                       ▼
┌────────────────────────────────────────────┐
│ MASTER INQUIRY METHODS GUIDE                │
│                                             │
│ Como investigar                             │
└──────────────────────┬─────────────────────┘
                       ▼
┌────────────────────────────────────────────┐
│ COGNITIVE / ENGINEERING HARNESS             │
│                                             │
│ Como verificar e controlar                  │
└──────────────────────┬─────────────────────┘
                       ▼
                  LLM / AGENT
                       │
                       ▼
                  ENGINEERING
```

---

# 114. DISTINÇÃO FINAL

O MEG-001 não diz:

> **“Construa um software epistemológico.”**

Ele diz:

> **“Construa um Harness capaz de exigir que um LLM opere epistemicamente de forma adequada ao problema, ao risco e à evidência disponível.”**

Essa é a finalidade normativa deste documento.

---

# 115. STATUS

**MEG-001 — Master Epistemological Guide for LLM Cognition**

**Versão:** 1.0
**Status:** Baseline Mestre
**Função:** orientar a especificação de epistemologia aplicada à cognição de LLMs
**Alvo:** Harnesses cognitivos, Claude Code, agentes e sistemas multiagentes
**Não é:** especificação de software
**Não é:** prompt operacional
**Não é:** manual de RAG
**Não é:** método de investigação específico
**Não é:** política de domínio.

É uma:

> **Metaespecificação para transformar princípios epistemológicos em requisitos cognitivos, verificáveis e governáveis por Harness.**

---

# FIM DO MEG-001 v1.0
