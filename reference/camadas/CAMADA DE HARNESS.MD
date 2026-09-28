# HCH-001

# MASTER SPECIFICATION FOR HIERARCHICAL COGNITIVE HARNESS

**Status:** Master Specification
**Tipo:** Especificação arquitetural e metodológica
**Escopo:** Global / agnóstico de domínio
**Aplicabilidade:** Sistemas LLM, agentes individuais, sistemas multiagente, workflows agentivos, capacidades cognitivas especializadas e sistemas híbridos humano–IA
**Paradigma:** Spec Driven Development + Harness Engineering + Quality Gates
**Princípio central:** **Liberdade Cognitiva + Obrigação de Satisfazer Invariantes**

---

# 1. PROPÓSITO

Esta especificação define um método para **projetar, decompor, especializar, compor, avaliar, validar e evoluir Harnesses cognitivos de forma hierárquica**.

O objetivo não é criar um conjunto rígido de instruções para controlar o raciocínio do LLM.

O objetivo é estabelecer uma arquitetura na qual:

> **o LLM mantenha liberdade para explorar o espaço cognitivo disponível, enquanto o sistema imponha invariantes, contratos, evidências, condições de validade, controles e gates sobre aquilo que precisa ser confiável e observável.**

O HCH estabelece uma relação entre:

```text
MISSÃO
   ↓
ESPECIFICAÇÕES
   ↓
NECESSIDADES COGNITIVAS
   ↓
HARNESS NECESSÁRIO
   ↓
EXECUÇÃO COGNITIVA
   ↓
EVIDÊNCIAS / ARTEFATOS
   ↓
SENSORES
   ↓
VALIDAÇÃO
   ↓
GATES
   ↓
FEEDBACK / RECUPERAÇÃO
   ↓
EVOLUÇÃO
```

A arquitetura deve permitir que um sistema cresça em complexidade **sem transformar o Harness em burocracia cognitiva**.

---

# 2. PROBLEMA QUE O HCH RESOLVE

Em sistemas LLM, especificações normalmente descrevem:

* o que deve ser feito;
* quais capacidades são necessárias;
* quais resultados são esperados;
* quais restrições existem.

Entretanto, isso não determina necessariamente:

* como o contexto será disponibilizado;
* quais invariantes precisam ser preservados;
* como erros serão detectados;
* como evidências serão verificadas;
* como ambiguidades serão tratadas;
* como conflitos serão identificados;
* como o resultado será validado;
* como uma falha será recuperada;
* como mudanças em uma SPEC afetarão o Harness;
* como o Harness será avaliado;
* como regressões serão detectadas.

O HCH resolve esse problema introduzindo uma regra fundamental:

> **Toda SPEC deve carregar consigo a especificação do Harness que governa sua execução.**

Consequentemente:

```text
SPEC
  ├── finalidade
  ├── requisitos
  ├── capacidades
  ├── invariantes
  ├── riscos
  └── Harness aplicável
          ├── contexto
          ├── orientação
          ├── sensores
          ├── guardrails
          ├── validação
          ├── gates
          ├── feedback
          └── recuperação
```

---

# 3. ESCOPO

O HCH é deliberadamente **agnóstico de domínio**.

Pode ser aplicado a:

* agentes de pesquisa;
* agentes de engenharia;
* agentes de análise;
* agentes de planejamento;
* agentes de atendimento;
* agentes científicos;
* agentes financeiros;
* agentes educacionais;
* agentes jurídicos;
* agentes de criação;
* sistemas multiagente;
* copilotos;
* workflows agentivos;
* sistemas de decisão assistida;
* sistemas de produção documental;
* sistemas híbridos LLM + ferramentas;
* outros sistemas cognitivos baseados em modelos generativos.

O domínio específico é introduzido posteriormente por especialização.

Portanto:

> **O HCH não contém a cognição de um domínio. Ele fornece a arquitetura pela qual a cognição de qualquer domínio pode ser governada.**

---

# 4. PRINCÍPIO FUNDAMENTAL

## 4.1 Liberdade Cognitiva

O LLM deve permanecer livre para:

* explorar hipóteses;
* comparar alternativas;
* reconsiderar conclusões;
* buscar relações não previstas;
* identificar padrões;
* gerar hipóteses novas;
* utilizar diferentes estratégias cognitivas;
* mudar de estratégia;
* detectar que uma premissa está errada;
* solicitar informação adicional;
* rejeitar uma hipótese;
* produzir interpretações concorrentes;
* adaptar o caminho cognitivo ao problema.

O Harness não deve presumir que existe apenas uma sequência correta de raciocínio.

---

# 5. OBRIGAÇÃO DE SATISFAZER INVARIANTES

A liberdade cognitiva não significa liberdade para violar requisitos fundamentais.

O sistema deve obrigatoriamente satisfazer:

* invariantes;
* contratos;
* precondições;
* postcondições;
* requisitos de segurança;
* requisitos de integridade;
* requisitos de evidência;
* requisitos de rastreabilidade;
* condições de validade;
* gates aplicáveis.

A fórmula conceitual é:

```text
ESPAÇO COGNITIVO LIVRE
        +
INVARIANTES OBRIGATÓRIOS
        =
LIBERDADE COGNITIVA GOVERNADA
```

O Harness deve controlar principalmente **propriedades observáveis**, e não tentar controlar o conteúdo privado do processo cognitivo.

---

# 6. O QUE O HARNESS É

Harness é a infraestrutura cognitivo-operacional que cria as condições para que um LLM execute uma missão de forma:

* orientada;
* contextualizada;
* verificável;
* observável;
* recuperável;
* governável;
* evolutiva.

Um Harness pode conter:

* contexto;
* instruções;
* contratos;
* schemas;
* skills;
* ferramentas;
* memória;
* mecanismos de recuperação;
* sensores;
* validadores;
* testes;
* hooks;
* guardrails;
* gates;
* mecanismos de feedback;
* mecanismos de recuperação;
* mecanismos de avaliação;
* mecanismos de rastreabilidade.

Portanto:

> **Harness não é sinônimo de prompt.**

Prompt pode ser um componente do Harness.

---

# 7. ARQUITETURA HIERÁRQUICA

A arquitetura global é:

```text
                         ┌──────────────────────┐
                         │      MISSÃO          │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ H0 — GLOBAL /        │
                         │ CONSTITUTIONAL       │
                         │ HARNESS              │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ H1 — DOMAIN          │
                         │ HARNESS              │
                         │       (opcional)     │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ H2 — CAPABILITY      │
                         │ HARNESS              │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ H3 — SPEC            │
                         │ HARNESS              │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ H4 — OPERATIONAL     │
                         │ HARNESS              │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ EXECUÇÃO             │
                         └──────────────────────┘

                    ↕
        ┌───────────────────────────────┐
        │        META-HARNESS           │
        │ Avaliação • Métricas •        │
        │ Regressão • Drift • Evolução  │
        └───────────────────────────────┘
```

---

# 8. H0 — GLOBAL / CONSTITUTIONAL HARNESS

O H0 estabelece as regras que devem permanecer válidas em todo o sistema.

Contém, entre outros:

### 8.1 Identidade

Define:

* identidade do sistema;
* papel;
* escopo;
* autoridade;
* limites de atuação.

### 8.2 Missão

Define:

* finalidade;
* objetivo;
* resultados esperados;
* critérios globais de sucesso.

### 8.3 Integridade

Define requisitos para:

* consistência;
* integridade de dados;
* integridade de estado;
* integridade de artefatos;
* versionamento.

### 8.4 Proveniência

Quando aplicável:

```text
informação
   ↓
origem
   ↓
transformação
   ↓
interpretação
   ↓
artefato
```

### 8.5 Governança

Define:

* autoridade;
* permissões;
* limites;
* aprovação;
* escalonamento;
* auditoria;
* recuperação.

### 8.6 Invariantes globais

São propriedades que nenhuma especialização inferior pode violar.

---

# 9. H1 — DOMAIN HARNESS

H1 é opcional.

Sua finalidade é especializar o H0 para determinado domínio.

Exemplo abstrato:

```text
H0
 │
 ├── H1-A
 ├── H1-B
 └── H1-C
```

Cada domínio pode introduzir:

* terminologia;
* ontologia;
* modelos;
* fontes;
* metodologias;
* riscos;
* critérios;
* ferramentas;
* padrões de evidência;
* requisitos regulatórios;
* práticas específicas.

Porém:

> **H1 não pode contradizer H0.**

A especialização deve adicionar semântica, e não substituir silenciosamente a constituição global.

---

# 10. H2 — CAPABILITY HARNESS

H2 organiza o Harness em torno de capacidades cognitivas ou operacionais.

Exemplos:

* pesquisa;
* recuperação de conhecimento;
* análise;
* planejamento;
* síntese;
* classificação;
* geração;
* verificação;
* decisão assistida;
* explicação;
* programação;
* transformação documental.

Também podem existir capacidades cognitivas transversais:

* ontologia;
* epistemologia;
* semântica;
* causalidade;
* contrafactuais;
* incerteza;
* decisão;
* metacognição;
* raciocínio probabilístico.

Essas capacidades devem ser tratadas como **recursos cognitivos disponíveis**, não como uma sequência obrigatória de pensamento.

---

# 11. H3 — SPEC HARNESS

H3 é o núcleo do modelo.

Cada SPEC deve declarar explicitamente:

> **qual Harness é necessário para que aquela especificação possa ser executada e validada adequadamente.**

Não existe:

```text
SPEC sem Harness
```

Existe:

```text
SPEC
+
Harness correspondente
```

---

# 12. H4 — OPERATIONAL HARNESS

H4 representa a aplicação concreta do Harness durante a operação.

Pode incluir:

* contexto carregado;
* ferramentas disponíveis;
* memória ativa;
* instruções efetivas;
* schemas;
* sensores ativos;
* validadores;
* gates;
* estado operacional;
* telemetria;
* feedback;
* recuperação.

H4 responde:

> **O Harness realmente aplicado na execução corresponde ao Harness especificado?**

Essa distinção é essencial para detectar **Harness Drift**.

---

# 13. META-HARNESS

O Meta-Harness não executa necessariamente a missão principal.

Ele observa o próprio sistema de Harness.

Suas responsabilidades incluem:

* avaliação;
* medição;
* comparação;
* regressão;
* drift;
* dívida;
* coerência;
* evolução;
* impacto de mudanças;
* qualidade dos controles;
* eficácia dos sensores;
* eficácia dos gates.

Assim:

```text
HARNESS
   ↓
governa execução

META-HARNESS
   ↓
governa o Harness
```

---

# 14. REGRA DE HERANÇA

A relação hierárquica deve obedecer:

```text
H(n) =
H(parent)
+
especialização local
```

Nunca:

```text
H(n) =
cópia integral de H(parent)
```

A especialização deve referenciar o que herda e declarar apenas o delta.

Exemplo:

```text
H0:
INV-001
INV-002
INV-003

H2:
HERDA:
INV-001
INV-002
INV-003

ADICIONA:
INV-020
INV-021
```

Isso reduz:

* duplicação;
* divergência;
* manutenção;
* contexto desnecessário;
* risco de contradição.

---

# 15. COERÊNCIA E COESÃO

## 15.1 Coerência vertical

Uma especificação inferior deve permanecer semanticamente compatível com seus ancestrais.

```text
H0
 ↓
H1
 ↓
H2
 ↓
H3
 ↓
H4
```

Cada nível deve responder:

> “Minha especialização continua compatível com aquilo que herdei?”

---

## 15.2 Coesão horizontal

Os componentes de um mesmo Harness devem trabalhar para a mesma finalidade.

Exemplo:

```text
Invariante
   ↓
Sensor
   ↓
Validação
   ↓
Gate
```

Não deve existir:

```text
Invariante X
      ↓
Sensor que mede Y
      ↓
Gate que verifica Z
```

sem justificativa explícita.

---

# 16. HARNESS DELTA

Cada SPEC deve possuir um **Harness Delta**.

Ele responde:

> O que esta SPEC necessita além do Harness herdado?

Estrutura:

```text
HARNESS DELTA

Inherited:
- referência H0
- referência H1
- referência H2

Added:
- novo contexto
- novo sensor
- novo validador
- novo requisito de evidência

Modified:
- regra herdada especializada

Removed:
- somente quando permitido pela governança
```

Remover um requisito herdado deve ser uma operação governada, nunca uma decisão implícita.

---

# 17. CONTRATO MÍNIMO DO HARNESS DE UMA SPEC

Toda SPEC deve conter um:

# SPEC HARNESS CONTRACT

### Identificação

* SPEC_ID
* versão
* status
* parent harness
* domínio
* capability

### Finalidade

* missão local;
* objetivo;
* resultado esperado.

### Herança

* Harness ancestral;
* invariantes herdados;
* contratos herdados;
* gates herdados.

### Especialização

* novos invariantes;
* novos riscos;
* novas capacidades;
* novas ferramentas;
* novos requisitos.

### Cognição

* capacidades cognitivas relevantes;
* grau de autonomia;
* liberdade cognitiva;
* condições para reconsideração;
* necessidade de hipóteses alternativas.

### Evidência

* evidências obrigatórias;
* fontes;
* proveniência;
* requisitos de qualidade;
* rastreabilidade.

### Contexto

* contexto necessário;
* contexto opcional;
* contexto proibido;
* estratégia de carregamento;
* prioridade contextual.

### Sensores

* o que será observado;
* como será observado;
* frequência;
* condição de disparo.

### Guardrails

* condições restritivas;
* limites;
* comportamentos proibidos.

### Validação

* validação determinística;
* validação inferencial;
* validação humana quando necessária.

### Gates

* condições de aprovação;
* condições de HOLD;
* condições de rejeição.

### Estado

* precondições;
* estado durante execução;
* postcondições;
* transições permitidas.

### Falha

* falhas esperadas;
* degradação;
* fallback;
* recuperação;
* escalonamento.

### Output Contract

* formato;
* conteúdo mínimo;
* invariantes;
* evidências;
* metadados.

### Traceability

```text
Missão
 ↓
Requisito
 ↓
Risco
 ↓
Invariante
 ↓
Controle
 ↓
Sensor
 ↓
Evidência
 ↓
Gate
 ↓
Resultado
```

---

# 18. CAMADAS DE CONTROLE

O HCH utiliza diferentes intensidades de controle.

## 18.1 Guidance

Orienta sem obrigar.

Exemplo:

> Considere interpretações alternativas quando houver ambiguidade.

---

## 18.2 Constraint

Define uma condição que deve ser respeitada.

Exemplo:

> Não utilizar informação cuja origem não possa ser identificada quando a rastreabilidade for obrigatória.

---

## 18.3 Sensor

Observa uma propriedade.

Exemplo:

```text
Sensor:
Existe evidência associada a cada afirmação crítica?
```

---

## 18.4 Guardrail

Impede ou limita determinados comportamentos.

---

## 18.5 Gate

Determina se o processo pode prosseguir.

```text
PASS
HOLD
FAIL
```

---

## 18.6 Feedback

Utiliza os resultados dos sensores para orientar nova ação.

---

## 18.7 Recovery

Permite retornar a um estado válido após falha.

---

# 19. PRINCÍPIO DETERMINÍSTICO-FIRST

Sempre que uma propriedade puder ser verificada deterministicamente, essa verificação deve ser preferida à avaliação subjetiva do LLM.

Exemplo:

Se o requisito é:

> “O campo X deve existir.”

utilizar:

```text
schema validator
```

é preferível a:

```text
LLM judge:
"Você acha que X está presente?"
```

O LLM deve ser utilizado para julgamento quando o problema realmente exigir:

* interpretação;
* qualidade;
* coerência;
* utilidade;
* adequação;
* raciocínio contextual.

---

# 20. COGNIÇÃO NÃO DEVE SER MICROGERENCIADA

O Harness deve evitar instruções do tipo:

```text
1. pense X
2. depois pense Y
3. depois pense Z
4. conclua W
```

quando não houver necessidade.

Isso pode reduzir:

* exploração;
* descoberta;
* adaptação;
* criatividade;
* reconsideração;
* capacidade de encontrar estratégias alternativas.

Prefira:

```text
REQUISITO:
avaliar causalidade quando relevante.

INVARIANTE:
não apresentar relação causal como fato sem sustentação suficiente.

LIBERDADE:
o LLM pode escolher como investigar causalidade.

GATE:
a conclusão causal precisa satisfazer o critério de evidência.
```

---

# 21. CAPACIDADES COGNITIVAS COMO RECURSOS

O HCH não exige que toda SPEC utilize todas as camadas cognitivas.

Em vez disso:

```text
GLOBAL COGNITIVE CAPABILITY POOL

Ontology
Epistemology
Semantics
Causality
Counterfactuals
Uncertainty
Decision
Metacognition
Probability
...
```

Cada SPEC declara:

```text
REQUIRED
OPTIONAL
NOT RELEVANT
```

Isso permite aumentar profundidade cognitiva apenas quando necessário.

---

# 22. PROFUNDIDADE ADAPTATIVA

A intensidade do Harness deve ser proporcional ao problema.

Fatores:

* risco;
* ambiguidade;
* incerteza;
* impacto;
* irreversibilidade;
* complexidade;
* dependências;
* propagação de erro;
* criticidade;
* custo de falha.

Modelo conceitual:

```text
RISCO BAIXO
    ↓
HARNESS MÍNIMO

RISCO / INCERTEZA MODERADOS
    ↓
SENSORES + VALIDAÇÃO

RISCO / IMPACTO ELEVADOS
    ↓
VALIDAÇÃO + GATES + EVIDÊNCIA + RECOVERY
```

O objetivo é:

> **Minimum Sufficient Harness**

O menor Harness capaz de satisfazer os requisitos necessários.

---

# 23. CONTEXTO COMO RECURSO COGNITIVO

Contexto não é gratuito.

Adicionar:

* instruções;
* regras;
* documentos;
* exemplos;
* schemas;
* memória;
* histórico;

não significa automaticamente aumentar a inteligência do sistema.

Pode ocorrer:

```text
mais contexto
     ↓
mais carga cognitiva
     ↓
menor relevância relativa
     ↓
maior competição entre informações
     ↓
degradação
```

Portanto, o HCH deve privilegiar:

* contexto relevante;
* escopo local;
* carregamento progressivo;
* referências;
* recuperação seletiva;
* redução de redundância;
* separação entre contexto global e contextual local.

---

# 24. CONTEXT SCOPING

Cada Harness deve definir:

### Global Context

Informações sempre relevantes.

### Domain Context

Informações relevantes ao domínio.

### Capability Context

Informações relevantes à capacidade.

### SPEC Context

Informações específicas da tarefa.

### Operational Context

Estado atual da execução.

Isso evita colocar todo o conhecimento disponível dentro de toda execução.

---

# 25. SENSORES

Todo requisito importante deve responder:

> “Como saberemos que ele foi satisfeito?”

Categorias:

### Structural Sensors

Verificam estrutura.

### Deterministic Sensors

Verificam propriedades objetivas.

### Semantic Sensors

Verificam significado.

### Evidence Sensors

Verificam sustentação.

### Behavioral Sensors

Verificam comportamento observável.

### Performance Sensors

Verificam desempenho.

### Cognitive Quality Sensors

Verificam propriedades cognitivas quando não houver teste determinístico suficiente.

---

# 26. GATES

Gates não devem avaliar apenas “qualidade geral”.

Devem verificar condições específicas.

Exemplo:

```text
GATE-G01

Required:
- invariantes satisfeitos
- evidências mínimas presentes
- output schema válido
- ausência de conflito crítico

Result:
PASS / HOLD / FAIL
```

---

# 27. HOLD COMO ESTADO DE PRIMEIRA CLASSE

Quando a evidência ou condição necessária não existe, o sistema não deve ser forçado a:

```text
PASS
```

nem:

```text
FAIL
```

Pode entrar em:

```text
HOLD
```

Exemplos:

* evidência insuficiente;
* conflito não resolvido;
* contexto incompleto;
* validação inconclusiva;
* sensor indisponível;
* requisito ambíguo.

Isso evita transformar ausência de conhecimento em falsa certeza.

---

# 28. RECOVERY

O Harness deve especificar o que ocorre após falha.

Modelo:

```text
EXECUTE
   ↓
SENSOR
   ↓
FAIL
   ↓
DIAGNOSE
   ↓
RECOVERY ACTION
   ↓
REVALIDATE
   ↓
PASS / HOLD / FAIL
```

Recovery pode envolver:

* buscar informação;
* reduzir escopo;
* reformular hipótese;
* executar nova análise;
* utilizar outra ferramenta;
* solicitar intervenção;
* retornar a estado anterior;
* interromper execução.

---

# 29. HARNESS SCORE

O Harness Score deve ser incorporado ao HCH como **referência de maturidade estrutural do Harness**, e não como medida de inteligência do LLM.

Sua utilidade está em verificar se o sistema possui infraestrutura adequada de Harness.

As dimensões estruturais consideradas pelo modelo incluem aspectos como:

* contexto e guias;
* skills e comandos;
* hooks e guardrails;
* sensores e feedback;
* feedback de integração/CI;
* higiene e segurança.

A progressão conceitual de maturidade é:

```text
L0 — Unharnessed
L1 — Documented
L2 — Guided
L3 — Sensing
L4 — Self-correcting
```

Esses níveis devem ser utilizados como **referência estrutural**, não como ranking de agentes.

Um sistema L4 não é automaticamente cognitivamente superior a um sistema L2.

Ele possui, em princípio, uma infraestrutura de Harness mais madura.

---

# 30. HARNESS SCORE NÃO É OBJETIVO

O HCH proíbe a seguinte lógica:

```text
aumentar score
      =
melhorar sistema
```

A avaliação correta é:

```text
melhoria do Harness
       ↓
efeito sobre
       ├── eficácia
       ├── eficiência
       ├── efetividade
       ├── economicidade
       └── liberdade cognitiva
```

Um controle adicional que:

* aumenta custo;
* aumenta latência;
* duplica validações;
* adiciona contexto irrelevante;
* reduz exploração;

pode representar **piora**, mesmo aumentando uma métrica estrutural.

---

# 31. HARNESS EVAL

Harness Eval deve ser incorporado ao HCH como mecanismo de avaliação da **qualidade real do Harness**, não apenas de sua existência.

A avaliação deve considerar pelo menos três perspectivas:

### A — Correctness

O Harness produz ou induz os comportamentos esperados?

### B — Redundancy

O Harness contém informação, controles ou componentes desnecessariamente duplicados?

### C — Usefulness

Os componentes realmente ajudam a execução?

A distinção é importante:

```text
EXISTE
≠
FUNCIONA
≠
É ÚTIL
```

---

# 32. AVALIAÇÃO ATÔMICA

A avaliação deve decompor julgamentos grandes em propriedades menores sempre que possível.

Em vez de:

> “O Harness é bom?”

avaliar:

```text
H1:
O requisito possui sensor?

H2:
O sensor detecta o comportamento?

H3:
Existe feedback?

H4:
Existe recovery?

H5:
Existe evidência?

H6:
Existe redundância?

H7:
O controle é realmente utilizado?
```

Isso reduz avaliações vagas.

---

# 33. DETERMINÍSTICO + INFERENCIAL

O HCH combina:

```text
DETERMINISTIC EVALUATION
+
INFERENTIAL EVALUATION
```

### Determinística

Preferida para:

* schemas;
* existência;
* formato;
* referências;
* hashes;
* estados;
* limites;
* testes;
* dependências;
* cobertura;
* consistência estrutural.

### Inferencial

Necessária para:

* utilidade;
* adequação;
* coerência;
* qualidade;
* clareza;
* suficiência contextual;
* julgamento semântico.

---

# 34. LLM JUDGE GOVERNANCE

Quando um LLM for utilizado como avaliador, o Harness deve registrar:

* modelo;
* versão;
* protocolo;
* critérios;
* evidências;
* contexto fornecido;
* resultado;
* grau de confiança quando aplicável;
* divergências;
* condições de reprodução.

Sempre que possível:

```text
JUDGE A
   +
JUDGE B
   ↓
COMPARAÇÃO
   ↓
AGREEMENT
```

Divergências importantes podem gerar:

```text
HOLD
```

em vez de uma escolha arbitrária.

---

# 35. BLIND EVALUATION E TRAPS

Quando adequado, avaliações podem utilizar:

* comparação cega;
* casos negativos;
* casos adversariais;
* planted traps;
* exemplos redundantes;
* casos de baixa qualidade;
* entradas ambíguas;
* entradas fora de escopo.

Objetivo:

> verificar se o Harness realmente diferencia situações relevantes.

---

# 36. EVIDENCE OR ZERO

Quando uma SPEC exigir evidência, o Harness deve evitar que uma afirmação seja considerada validada simplesmente porque foi apresentada de forma convincente.

Modelo:

```text
CLAIM
  ↓
REQUIRED EVIDENCE
  ↓
EVIDENCE FOUND?
   ├── YES → VALIDATE
   └── NO  → HOLD / INVALID
```

Isso é especialmente importante quando o custo de uma afirmação incorreta é elevado.

---

# 37. FAN-IN PROTECTION

Quando muitos resultados dependem de uma mesma informação, erro ou componente, o Harness deve reconhecer o risco de propagação.

```text
              ┌── Output A
SOURCE ───────┼── Output B
              ├── Output C
              └── Output D
```

Um erro na fonte pode contaminar todos os resultados.

Quanto maior o fan-in:

> maior deve ser a importância de validar o componente compartilhado.

---

# 38. REGRESSÃO

Qualquer mudança significativa em Harness deve seguir:

```text
BASELINE
   ↓
CHANGE
   ↓
IMPACT ANALYSIS
   ↓
VALIDATION
   ↓
REGRESSION SCAN
   ↓
COMPARE
   ↓
APPROVE / HOLD / REJECT
```

A mudança de H0 pode afetar:

```text
H0
 ↓
H1
 ↓
H2
 ↓
H3
 ↓
H4
```

Portanto, mudanças superiores exigem análise de impacto descendente.

---

# 39. HARNESS DRIFT

Harness Drift ocorre quando:

```text
Harness especificado
        ≠
Harness realmente aplicado
```

Exemplos:

* skill especificada mas não carregada;
* sensor removido;
* gate desativado;
* versão incorreta;
* referência quebrada;
* instrução obsoleta;
* ferramenta indisponível;
* contrato divergente;
* contexto diferente do especificado.

O Meta-Harness deve detectar esse desvio.

---

# 40. HARNESS DEBT

Harness Debt representa controles necessários que ainda não existem ou estão deteriorados.

Exemplos:

* requisito sem sensor;
* sensor sem feedback;
* gate sem critério objetivo;
* referência quebrada;
* avaliação pendente;
* teste ausente;
* documentação duplicada;
* regra obsoleta;
* controle frágil;
* validação exclusivamente inferencial quando existe alternativa determinística.

Harness Debt deve ser rastreada como dívida arquitetural.

---

# 41. TRACEABILITY MATRIX

O HCH recomenda uma matriz:

| Elemento   | Origem     | Controle   | Sensor         | Evidência | Gate            |
| ---------- | ---------- | ---------- | -------------- | --------- | --------------- |
| Missão     | H0         | Invariante | Sensor         | Artefato  | Global          |
| Requisito  | SPEC       | Constraint | Sensor         | Resultado | SPEC            |
| Risco      | Risk Model | Guardrail  | Sensor         | Evento    | Risk Gate       |
| Capacidade | H2         | Guidance   | Quality Sensor | Output    | Capability Gate |
| Output     | SPEC       | Contract   | Schema         | Artefato  | Output Gate     |

A regra é:

> **requisito crítico sem mecanismo de verificação = requisito sem governança suficiente.**

---

# 42. PROPORCIONALIDADE

Nem todo requisito precisa de:

* sensor;
* gate;
* LLM judge;
* múltiplas validações;
* revisão humana.

A arquitetura deve considerar:

```text
Valor do controle
        ÷
Custo do controle
```

O custo inclui:

* latência;
* tokens;
* infraestrutura;
* complexidade;
* manutenção;
* atenção;
* risco de interferência cognitiva.

---

# 43. 3Es + ECONOMICIDADE

O HCH deve avaliar o Harness por quatro dimensões.

## Eficiência

Usa recursos adequadamente?

## Eficácia

Consegue atingir o resultado especificado?

## Efetividade

O resultado realmente resolve o problema no contexto real?

## Economicidade

O benefício obtido justifica os recursos consumidos?

Uma quinta propriedade transversal é:

## Preservação Cognitiva

O Harness melhora confiabilidade sem restringir desnecessariamente a capacidade cognitiva do LLM?

---

# 44. FUNÇÃO DE OTIMIZAÇÃO DO HARNESS

Não se deve buscar:

```text
MAX(HARNESS)
```

Deve-se buscar:

```text
MAX
(
  eficácia
  +
  efetividade
  +
  confiabilidade
  +
  preservação cognitiva
)
```

sob restrições de:

```text
eficiência
economicidade
latência
complexidade
contexto
manutenção
```

---

# 45. PRINCÍPIO DE NECESSIDADE E SUFICIÊNCIA

Todo componente do Harness deve responder:

1. Qual requisito atende?
2. Qual risco reduz?
3. Qual comportamento melhora?
4. Como sabemos que funciona?
5. Qual custo introduz?

Se não houver resposta satisfatória, o componente deve ser questionado.

---

# 46. ANTI-PADRÕES

## 46.1 Prompt Monolítico

Colocar todo o Harness em um único prompt.

---

## 46.2 Over-Harnessing

Adicionar controles indiscriminadamente.

Resultado potencial:

```text
mais regras
↓
mais contexto
↓
menos espaço cognitivo
↓
menor adaptação
```

---

## 46.3 Under-Harnessing

Confiar apenas na capacidade intrínseca do LLM.

---

## 46.4 Controle do Raciocínio Privado

Exigir uma sequência cognitiva fixa sem necessidade.

---

## 46.5 Gate Cosmético

Criar gate sem capacidade real de detectar falhas.

---

## 46.6 Sensor sem Ação

Detectar problema mas não possuir feedback ou recovery.

---

## 46.7 LLM Judge para Tudo

Usar julgamento generativo onde uma validação determinística seria suficiente.

---

## 46.8 Score Chasing

Otimizar pontuação em vez de otimizar o sistema.

---

## 46.9 Duplicação Hierárquica

Copiar H0 para todas as SPECs.

---

## 46.10 Harness Drift

Especificação diferente do Harness realmente carregado.

---

# 47. MÉTODO DE DECOMPOSIÇÃO

A criação de Harness deve acompanhar a decomposição das SPECs.

## Etapa 1 — Decompor a missão

```text
MISSÃO
 ↓
OBJETIVOS
 ↓
REQUISITOS
```

## Etapa 2 — Identificar capacidades

```text
REQUISITO
 ↓
CAPACIDADE NECESSÁRIA
```

## Etapa 3 — Identificar riscos

```text
CAPACIDADE
 ↓
RISCOS
```

## Etapa 4 — Definir invariantes

```text
RISCO
 ↓
INVARIANTE
```

## Etapa 5 — Definir Harness

```text
INVARIANTE
 ↓
CONTROLE
 ↓
SENSOR
 ↓
GATE
```

## Etapa 6 — Definir liberdade cognitiva

Perguntar:

> O que precisa obrigatoriamente acontecer e o que pode permanecer livre para o LLM decidir?

## Etapa 7 — Definir recuperação

Perguntar:

> O que acontece quando o requisito não é satisfeito?

## Etapa 8 — Avaliar o Harness

Aplicar:

```text
Structural Maturity
+
Harness Evaluation
+
Cognitive Quality
+
3Es
+
Economicidade
```

---

# 48. CICLO DE VIDA

```text
DISCOVER
   ↓
SPECIFY
   ↓
DECOMPOSE
   ↓
HARNESS DESIGN
   ↓
IMPLEMENT / COMPOSE
   ↓
VALIDATE
   ↓
EVALUATE
   ↓
OPERATE
   ↓
OBSERVE
   ↓
LEARN
   ↓
EVOLVE
   ↓
REGRESSION
   ↺
```

---

# 49. RELAÇÃO BIDIRECIONAL SPEC ↔ HARNESS

A direção principal é:

```text
SPEC
 ↓
necessidade de Harness
```

Mas o processo também é retroalimentado:

```text
HARNESS
 ↓
descobre lacuna
 ↓
SPEC precisa ser refinada
```

Portanto:

```text
SPEC ─────────→ HARNESS
  ↑                │
  └────────────────┘
       feedback
```

Essa relação impede que a especificação seja considerada completa quando ainda não existe mecanismo adequado para executá-la ou verificá-la.

---

# 50. COMPOSIÇÃO DE HARNESS

Quando duas SPECs são combinadas:

```text
SPEC-A + SPEC-B
        ↓
   COMPOSITE SPEC
        ↓
   COMPOSITE HARNESS
```

O Harness composto deve verificar:

* compatibilidade;
* conflitos;
* duplicação;
* dependências;
* precedência;
* compartilhamento de contexto;
* conflitos de ferramentas;
* conflitos de invariantes;
* propagação de riscos.

---

# 51. REGRA DE PRECEDÊNCIA

Em caso de conflito:

```text
Global Invariant
      >
Domain Constraint
      >
Capability Constraint
      >
SPEC Constraint
      >
Operational Preference
```

Uma camada inferior não pode simplesmente substituir uma regra superior.

Caso seja necessária exceção:

```text
EXCEPTION
 ↓
JUSTIFICATION
 ↓
IMPACT ANALYSIS
 ↓
AUTHORIZATION
 ↓
TEMPORARY / VERSIONED OVERRIDE
```

---

# 52. HARNESS COMO SISTEMA DE FEEDBACK

O Harness deve ser concebido como sistema cibernético:

```text
              ┌──────────────┐
              │   ORIENTAÇÃO │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │   COGNIÇÃO   │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │   ARTEFATO   │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │   SENSOR     │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │   FEEDBACK   │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ CORREÇÃO /   │
              │ RECOVERY     │
              └──────┬───────┘
                     │
                     └────────→ nova ação
```

O Harness não é apenas um conjunto de regras.

É um **sistema de controle adaptativo da execução cognitiva**.

---

# 53. MODELO DE MATURIDADE DO HCH

O HCH pode utilizar uma maturidade composta:

### M0 — Unharnessed

Não existe Harness formal.

### M1 — Specified

Existe Harness documentado.

### M2 — Guided

Existe orientação operacional.

### M3 — Sensing

Existem sensores e validação.

### M4 — Gated

Existem gates efetivos.

### M5 — Feedback

Resultados produzem correções.

### M6 — Self-correcting

O sistema consegue detectar e corrigir classes relevantes de falha.

### M7 — Adaptive Governance

O próprio Harness evolui com base em evidências, regressões e impacto.

Esses níveis são arquiteturais, não uma medida absoluta de inteligência.

---

# 54. CRITÉRIO DE ACEITAÇÃO DE UMA SPEC

Uma SPEC não deve ser considerada plenamente pronta quando apenas sua lógica funcional estiver especificada.

Ela deve possuir:

```text
SPEC
+
RISKS
+
INVARIANTS
+
COGNITIVE CAPABILITIES
+
HARNESS CONTRACT
+
SENSORS
+
VALIDATION
+
GATES
+
RECOVERY
+
TRACEABILITY
```

Quando algum desses elementos não for necessário, a ausência deve ser justificável.

---

# 55. CRITÉRIO DE ACEITAÇÃO DO HARNESS

Um Harness pode ser considerado adequado quando:

* é coerente com seu ancestral;
* é coeso internamente;
* não possui duplicação relevante;
* possui controles proporcionais ao risco;
* preserva liberdade cognitiva;
* possui invariantes claros;
* possui sensores adequados;
* utiliza validação determinística quando possível;
* possui gates para propriedades críticas;
* possui mecanismos de recovery;
* é observável;
* possui rastreabilidade;
* pode ser avaliado;
* pode sofrer regressão;
* possui versionamento;
* seu custo é justificável;
* o Harness efetivamente aplicado corresponde ao Harness especificado.

---

# 56. CRITÉRIO DE QUALIDADE GLOBAL

A qualidade do HCH não deve ser determinada por uma única métrica.

Deve ser avaliada em múltiplos eixos:

```text
                  ┌───────────────┐
                  │  EFICÁCIA     │
                  └───────┬───────┘
                          │
        ┌─────────────────┼─────────────────┐
        ↓                 ↓                 ↓
   EFICIÊNCIA       EFETIVIDADE      ECONOMICIDADE
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ↓
                 PRESERVAÇÃO
                  COGNITIVA
                          ↓
                  CONFIABILIDADE
```

Nenhum eixo isolado deve dominar automaticamente os demais.

---

# 57. MASTER INVARIANTS DO HCH

## HCH-INV-001 — Herança

Nenhum Harness inferior pode violar invariantes superiores.

## HCH-INV-002 — Liberdade Cognitiva

O Harness não deve restringir a cognição além do necessário para satisfazer seus requisitos.

## HCH-INV-003 — Observabilidade

Propriedades críticas devem possuir mecanismo de observação.

## HCH-INV-004 — Verificabilidade

Propriedades críticas devem possuir mecanismo de validação.

## HCH-INV-005 — Proporcionalidade

A intensidade do Harness deve ser proporcional ao risco e impacto.

## HCH-INV-006 — Determinismo Preferencial

Verificações determinísticas devem ser preferidas quando adequadas.

## HCH-INV-007 — Rastreabilidade

Requisitos críticos devem possuir rastreabilidade até seus mecanismos de controle e validação.

## HCH-INV-008 — Recuperabilidade

Falhas relevantes devem possuir estratégia de recuperação ou escalonamento.

## HCH-INV-009 — Não-Duplicação

Informações e controles não devem ser duplicados sem justificativa.

## HCH-INV-010 — Não-Drift

Harness especificado e Harness efetivamente executado devem permanecer alinhados.

## HCH-INV-011 — Evolutividade

Alterações relevantes devem permitir análise de impacto e regressão.

## HCH-INV-012 — Economicidade

Controles devem justificar o custo que introduzem.

## HCH-INV-013 — Utilidade

Componentes do Harness devem demonstrar utilidade ou atender requisito explicitamente justificado.

## HCH-INV-014 — Não-Cosmeticidade

Sensores e gates devem possuir capacidade real de detectar ou impedir as condições que alegam controlar.

## HCH-INV-015 — Incerteza

Ausência de evidência suficiente não deve ser transformada automaticamente em certeza.

---

# 58. REGRA-MESTRA DE ESPECIFICAÇÃO

A regra operacional central deste documento é:

> **Toda SPEC deve especificar, no momento de sua elaboração, o Harness necessário para executá-la, validá-la, observá-la e recuperá-la, declarando explicitamente aquilo que herda do Harness superior e aquilo que adiciona localmente.**

Consequentemente:

```text
SPEC ≠ apenas comportamento desejado

SPEC =
    comportamento
  + invariantes
  + riscos
  + capacidades
  + Harness
  + validação
  + gates
  + recovery
```

---

# 59. REGRA-MESTRA DE COMPOSIÇÃO

O Harness global não deve ser reproduzido em cada SPEC.

Cada SPEC deve declarar:

```text
INHERITS
+
LOCAL DELTA
```

Assim:

```text
GLOBAL HARNESS
       ↓
DOMAIN HARNESS
       ↓
CAPABILITY HARNESS
       ↓
SPEC HARNESS
       ↓
OPERATIONAL HARNESS
```

mantendo:

```text
COERÊNCIA VERTICAL
+
COESÃO HORIZONTAL
```

---

# 60. REGRA-MESTRA DE COGNIÇÃO

O HCH deve sempre distinguir:

```text
O QUE É OBRIGATÓRIO
```

de:

```text
COMO O LLM PODE CHEGAR AO RESULTADO
```

A primeira categoria pertence ao Harness.

A segunda permanece, sempre que possível, aberta à cognição do modelo.

Portanto:

> **O Harness governa o espaço de validade da cognição; não deve, sem necessidade, prescrever a própria cognição.**

---

# 61. REGRA-MESTRA DE AVALIAÇÃO

O HCH deve combinar três perspectivas distintas:

```text
HARNESS SCORE
      ↓
"Quão estruturado/maduro é o Harness?"

HARNESS EVAL
      ↓
"O Harness realmente funciona, é útil e evita redundância?"

COGNITIVE / OUTCOME EVALUATION
      ↓
"A execução cognitiva produz resultados adequados?"
```

Nenhuma dessas perguntas substitui as outras.

---

# 62. REGRA-MESTRA DO META-HARNESS

O Meta-Harness deve observar:

```text
Harness Structure
      +
Harness Behavior
      +
Harness Utility
      +
Cognitive Outcomes
      +
Regression
      +
Drift
      +
Debt
      +
Cost
      +
Evolution
```

Seu objetivo não é maximizar controles.

Seu objetivo é manter o sistema dentro do **ponto ótimo entre liberdade cognitiva e confiabilidade governada**.

---

# 63. MODELO FINAL

A arquitetura completa pode ser resumida assim:

```text
                         MISSÃO
                           │
                           ▼
                ┌─────────────────────┐
                │ H0 GLOBAL           │
                │ Constituição        │
                │ Invariantes         │
                │ Governança          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ H1 DOMAIN           │
                │ Especialização      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ H2 CAPABILITY       │
                │ Capacidades         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ H3 SPEC             │
                │ Harness Contract    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ H4 OPERATIONAL      │
                │ Harness efetivo     │
                └──────────┬──────────┘
                           │
                           ▼
                     EXECUÇÃO LLM
                           │
                           ▼
                ┌─────────────────────┐
                │ SENSORS             │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ VALIDATION          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ QUALITY GATES       │
                └──────────┬──────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
               PASS                HOLD/FAIL
                 │                   │
                 │             RECOVERY
                 │                   │
                 │                   └───────┐
                 ▼                           │
               OUTPUT ◄──────────────────────┘


              ┌──────────────────────────────┐
              │        META-HARNESS          │
              │                              │
              │ Harness Score                │
              │ Harness Eval                 │
              │ Cognitive Evaluation         │
              │ Regression                   │
              │ Drift                        │
              │ Debt                         │
              │ Impact Analysis              │
              │ Evolution                    │
              │ 3Es + Economicidade          │
              └──────────────────────────────┘
```

---

# 64. PRINCÍPIO FINAL

O HCH não existe para tornar o LLM mais obediente.

Ele existe para tornar o sistema **mais confiável sem destruir a capacidade cognitiva que torna o LLM útil**.

A arquitetura fundamental é:

```text
              LIBERDADE COGNITIVA
                       │
                       ▼
             ┌───────────────────┐
             │      LLM          │
             │ explorar          │
             │ raciocinar        │
             │ comparar          │
             │ criar             │
             │ reconsiderar      │
             │ adaptar           │
             └─────────┬─────────┘
                       │
                       ▼
             OBRIGAÇÃO DE
             SATISFAZER
             INVARIANTES
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       SENSORES       GATES      EVIDÊNCIAS
          │            │            │
          └────────────┼────────────┘
                       ▼
                 FEEDBACK
                       │
                       ▼
                  RECOVERY
                       │
                       ▼
                  EVOLUÇÃO
```

Portanto:

> **O Harness não deve substituir a cognição do LLM. Deve construir as condições nas quais essa cognição possa operar livremente dentro de um espaço de validade verificável.**

E, em nível hierárquico:

> **O Global Harness estabelece a constituição. O Domain Harness especializa. O Capability Harness disponibiliza capacidades. Cada SPEC define seu Harness local. O Operational Harness executa. Os sensores observam. Os gates garantem invariantes. O Harness Eval verifica se o Harness funciona e é útil. O Harness Score mede sua maturidade estrutural. O Meta-Harness governa a evolução do conjunto.**

**HCH-001 — Master Specification for Hierarchical Cognitive Harness** estabelece, assim, o princípio de que **a decomposição de especificações deve produzir também uma decomposição correspondente de Harness**, mantendo herança, coerência, coesão, proporcionalidade, observabilidade, verificabilidade, recuperação e preservação da liberdade cognitiva.
