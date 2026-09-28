# MC-RAG-001 — Master Contract da Camada RAG

**Sistema:** SOT — System of Thought  
**Camada:** RAG / Capacidades de Conhecimento  
**Versão:** 1.0  
**Status:** Baseline de especificação  
**Natureza:** Arquitetura, contratos, especificações e Harness  
**Escopo:** Geral, aplicável a LLMs e agentes, sem acoplamento tecnológico

---

## 1. Finalidade

Este Master Contract define a **Camada RAG como uma capacidade transversal de conhecimento** que pode ser invocada por qualquer agente ou capacidade cognitiva que necessite adquirir, formar, localizar, recuperar, selecionar, organizar e entregar conhecimento ou evidência.

A camada deve maximizar:

- **Eficácia:** entregar evidência relevante e suficiente para a tarefa.
- **Eficiência:** minimizar recuperação, processamento e contexto desnecessários.
- **Efetividade:** aumentar a qualidade do resultado produzido pelo consumidor da evidência.
- **Economicidade:** maximizar valor cognitivo por token, chamada, latência e custo.

O RAG não é definido como simples mecanismo de busca. Ele deve controlar o ciclo:

> **Aquisição → Extração → Formação → Validação → Publicação → Recuperação → Composição de Evidência → Controle de Contexto → Feedback**

---

# 2. Identidade da Camada

## 2.1 O que a camada RAG é

Uma capacidade responsável por:

1. adquirir fontes;
2. preservar proveniência;
3. extrair unidades semânticas;
4. formar candidatos de conhecimento;
5. recuperar conhecimento e evidências;
6. localizar evidências favoráveis e contrárias;
7. considerar temporalidade;
8. detectar lacunas de conhecimento;
9. adaptar a estratégia de recuperação;
10. controlar o orçamento de contexto;
11. construir Evidence Packets;
12. fornecer rastreabilidade ao consumidor;
13. medir qualidade, custo e degradação;
14. produzir sinais de melhoria para o ciclo de evolução.

## 2.2 O que a camada não é

A camada RAG não deve se tornar:

- autoridade cognitiva;
- autoridade decisional;
- autoridade de governança;
- memória episódica;
- mecanismo de aprendizado autônomo;
- Knowledge Graph como autoridade semântica;
- banco vetorial como autoridade;
- banco documental como autoridade;
- framework específico de RAG;
- substituto do raciocínio do LLM;
- mecanismo automático de publicação de conhecimento.

---

# 3. Princípios Específicos

### RAG-P01 — Proveniência obrigatória
Toda evidência recuperável deve possuir origem rastreável.

### RAG-P02 — Fonte não é conhecimento
Um documento, registro ou dado bruto não deve ser tratado automaticamente como conhecimento validado.

### RAG-P03 — Aquisição ≠ Formação ≠ Recuperação
São responsabilidades distintas e devem possuir contratos próprios.

### RAG-P04 — Formação ≠ Publicação
A formação produz um **Knowledge Candidate**. A publicação depende de validação e governança.

### RAG-P05 — Evidência antes da conclusão
O RAG deve priorizar evidências que possam sustentar, contrariar ou qualificar uma afirmação.

### RAG-P06 — Contexto mínimo suficiente
Mais contexto não significa necessariamente melhor contexto.

### RAG-P07 — Evidência crítica protegida
Informações críticas não podem ser descartadas apenas por compressão, posição ou orçamento de tokens.

### RAG-P08 — Contradição explícita
Evidências conflitantes devem ser preservadas e sinalizadas.

### RAG-P09 — Incerteza preservada
A recuperação não deve transformar incerteza da fonte em certeza artificial.

### RAG-P10 — Temporalidade explícita
Conhecimento dependente de tempo deve possuir escopo temporal.

### RAG-P11 — Conhecimento e experiência separados
Experiência histórica pode ser recuperada sem ser automaticamente promovida a regra geral.

### RAG-P12 — Neutralidade tecnológica
Tecnologias são meios. O contrato semântico permanece independente de banco, framework ou arquitetura de implementação.

### RAG-P13 — Feedback não é autorização
Feedback pode melhorar a recuperação, mas não pode conceder autoridade para alterar conhecimento governado.

### RAG-P14 — Especialização sem fragmentação
Agentes especializados podem utilizar o mesmo RAG sem criar silos incompatíveis de conhecimento.

---

# 4. Modelo Conceitual

```text
                    ┌──────────────────────┐
                    │ Agente consumidor     │
                    └──────────┬───────────┘
                               │
                         RAG Request
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Classificação da tarefa │
                  │ + objetivo + orçamento  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Retrieval Controller    │
                  └────────────┬────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
         Semântico          Graph           Experiência
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                  ┌─────────────────────────┐
                  │ Avaliação da evidência  │
                  │ relevância / conflito   │
                  │ temporalidade / origem  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Context Optimization    │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Evidence Packet         │
                  └────────────┬────────────┘
                               │
                               ▼
                    Agente consumidor
```

---

# 5. Modelo de Formação de Conhecimento

```text
Source
  ↓
Acquisition
  ↓
Classification
  ↓
Extraction
  ↓
Normalization
  ↓
Semantic Units
  ↓
Formation
  ↓
Knowledge Candidate
  ↓
Validation
  ↓
Governance
  ↓
Publication
```

A camada deve impedir que o caminho abaixo seja considerado válido:

```text
Source → LLM → Knowledge Published
```

---

# 6. Classes de Conhecimento

## 6.1 IMMUTABLE

Conhecimento fundamental, conceitual ou teórico cuja alteração possui alto impacto semântico.

Exemplos:

- definições;
- princípios fundamentais;
- relações teóricas;
- conceitos matemáticos.

Requer controle elevado para publicação.

## 6.2 OPERATIONAL

Conhecimento contextual e sujeito a mudança.

Exemplos:

- parâmetros;
- regimes;
- condições operacionais;
- calibrações;
- regras dependentes de contexto.

## 6.3 EXPERIENTIAL

Conhecimento derivado de experiências observadas.

Exemplos:

- resultados históricos;
- erros;
- sucessos;
- episódios;
- desempenho de hipóteses;
- resultados de experimentos.

Experiência não deve ser automaticamente generalizada.

---

# 7. Knowledge Candidate

A formação deve produzir uma entidade intermediária chamada **Knowledge Candidate**.

```yaml
candidate_id:
source_refs:
extraction_trace:
formation_method:
claims:
relationships:
confidence:
knowledge_class:
impact_class:
conflicts:
validation_status:
provenance:
evidence_spans:
temporal_scope:
version:
derived_from:
publication_status:
```

O Candidate não equivale a conhecimento publicado.

---

# 8. Evidence Packet

A saída primária do RAG para o agente consumidor deve ser um pacote de evidência controlado.

```yaml
evidence_packet_id:
objective:
query:
task_type:
key_evidence:
contrary_evidence:
source_refs:
knowledge_refs:
temporal_scope:
confidence:
relationships:
gaps:
conflicts:
minimal_synthesis:
token_estimate:
selection_rationale:
retrieval_trace:
version:
```

O Evidence Packet deve responder:

1. O que foi recuperado?
2. Por que foi selecionado?
3. De onde veio?
4. Qual sua validade temporal?
5. Existe evidência contrária?
6. O que permanece desconhecido?
7. Quanto contexto foi utilizado?
8. Qual o nível de confiança?
9. O que foi deliberadamente excluído?
10. Qual foi a estratégia de recuperação?

---

# 9. Contrato de Contexto

O RAG deve tratar contexto como **recurso cognitivo limitado**, não como depósito ilimitado de informação.

O orçamento deve considerar:

- tokens disponíveis;
- tokens já ocupados;
- importância da tarefa;
- criticidade das evidências;
- redundância;
- densidade informacional;
- posição das evidências;
- custo da recuperação;
- risco de omissão;
- risco de Context Rot;
- risco de Lost-in-the-Middle.

O objetivo é:

> **maximizar informação útil por unidade de contexto.**

---

# 10. Recuperação Adaptativa

Fluxo mínimo:

```text
Query
 ↓
Classificação da tarefa
 ↓
Recuperação inicial
 ↓
Avaliação de suficiência
 ├── suficiente → Evidence Packet
 └── insuficiente
        ↓
   Recuperação adicional
        ↓
   Contradição / lacuna
        ↓
   Nova avaliação
        ↓
   Evidence Packet
```

A recuperação adicional deve ocorrer somente quando houver justificativa cognitiva, como:

- baixa suficiência;
- conflito relevante;
- ausência de evidência crítica;
- lacuna de conhecimento;
- baixa cobertura;
- incerteza elevada;
- necessidade temporal;
- necessidade de evidência independente.

---

# 11. Especificações a serem desenvolvidas

Esta é a **backlog normativa da camada RAG**. Cada item deve posteriormente possuir sua própria especificação detalhada, critérios de aceitação e Harness.

## Grupo A — Fundamentos

### RAG-SPEC-001 — RAG Capability Contract
Deve definir identidade, entradas, saídas, responsabilidades, limites e invariantes da camada.

**Aceitação:** qualquer consumidor consegue determinar claramente quando e como invocar o RAG.

### RAG-SPEC-002 — RAG Request Model
Deve especificar a estrutura de uma solicitação RAG.

Deve contemplar:

- objetivo;
- pergunta;
- tarefa;
- domínio;
- criticidade;
- temporalidade;
- orçamento;
- profundidade;
- restrições;
- formato de saída.

**Aceitação:** solicitações semanticamente equivalentes devem possuir representação comparável.

### RAG-SPEC-003 — Source Model
Deve especificar identidade, origem, hash, URI, tipo, versão, autor, data e proveniência.

**Aceitação:** qualquer evidência deve poder retornar à fonte original.

### RAG-SPEC-004 — Source Classification
Deve definir classificação por origem, confiabilidade, temporalidade, autoridade e função.

**Aceitação:** fontes distintas devem poder receber tratamento diferenciado de forma determinística.

### RAG-SPEC-005 — Acquisition Pipeline
Deve definir aquisição, ingestão, validação, versionamento e rastreabilidade.

**Aceitação:** aquisição incompleta ou corrompida não pode entrar silenciosamente no conhecimento.

### RAG-SPEC-006 — Document and Artifact Parsing
Deve especificar extração de texto, tabelas, metadados, imagens, estruturas e unidades relevantes.

**Aceitação:** o parsing preserva informação necessária para a posterior formação de conhecimento.

### RAG-SPEC-007 — Semantic Unit Formation
Deve definir como documentos são transformados em unidades semanticamente recuperáveis.

**Aceitação:** unidades devem preservar significado e proveniência.

---

## Grupo B — Formação de Conhecimento

### RAG-SPEC-008 — Knowledge Candidate Formation
Deve definir a transformação de evidências extraídas em candidatos de conhecimento.

**Aceitação:** nenhum candidato pode perder sua origem.

### RAG-SPEC-009 — Formation Fidelity
Deve verificar se a formação preservou o significado original.

**Aceitação:** síntese não pode introduzir afirmação inexistente na fonte sem marcação explícita.

### RAG-SPEC-010 — Knowledge Impact Classification
Deve classificar impacto em:

- Definition;
- Theoretical Rule;
- Operational Rule;
- Parameter/Calibration.

**Aceitação:** incerteza de classificação deve subir para a classe de maior governança.

### RAG-SPEC-011 — Knowledge Publication Contract
Deve definir quando um Candidate pode tornar-se conhecimento publicado.

**Aceitação:** nenhum Candidate é publicado apenas por ter sido formado.

### RAG-SPEC-012 — Knowledge Graph Projection
Deve especificar como conhecimento pode ser projetado para uma representação relacional ou grafada sem transferir autoridade semântica para a tecnologia.

**Aceitação:** o grafo deve preservar identidade, proveniência e versão.

---

## Grupo C — Recuperação

### RAG-SPEC-013 — Retrieval Strategy Contract
Deve definir estratégias possíveis:

- lexical;
- semântica;
- híbrida;
- relacional;
- temporal;
- experiencial;
- baseada em evidência.

**Aceitação:** cada estratégia possui condições de uso e métricas.

### RAG-SPEC-014 — Retrieval Routing
Deve definir como selecionar uma estratégia ou composição de estratégias.

**Aceitação:** a estratégia escolhida deve possuir justificativa rastreável.

### RAG-SPEC-015 — Scheduler/RAG Resource Contract
Deve separar:

- **Scheduler:** autoridade sobre orçamento e recursos;
- **Router:** autoridade sobre estratégia dentro do orçamento.

**Aceitação:** o Router não pode aumentar unilateralmente o orçamento cognitivo.

### RAG-SPEC-016 — Query Decomposition
Deve decompor perguntas complexas em subconsultas recuperáveis.

**Aceitação:** cada subconsulta deve manter relação explícita com o objetivo original.

### RAG-SPEC-017 — Evidence Ranking
Deve especificar ranking por relevância, qualidade, independência, temporalidade e criticidade.

**Aceitação:** ranking não pode depender somente de similaridade semântica.

### RAG-SPEC-018 — Evidence Independence
Deve detectar quando várias evidências são derivadas da mesma origem.

**Aceitação:** fontes duplicadas não podem produzir falsa impressão de confirmação independente.

### RAG-SPEC-019 — Contradiction Retrieval
Deve buscar evidências potencialmente contraditórias.

**Aceitação:** contradições relevantes devem aparecer no Evidence Packet.

### RAG-SPEC-020 — Temporal Retrieval
Deve respeitar validade temporal e contexto histórico.

**Aceitação:** conhecimento temporalmente incompatível não deve ser apresentado como atual sem sinalização.

---

## Grupo D — Contexto

### RAG-SPEC-021 — Context Budgeting
Deve definir orçamento de tokens e recursos por tarefa.

**Aceitação:** o consumo deve ser mensurável e auditável.

### RAG-SPEC-022 — Context Packing
Deve ordenar e estruturar evidências para maximizar compreensão.

**Aceitação:** evidência crítica deve possuir proteção contra posição desfavorável.

### RAG-SPEC-023 — Context Compression
Deve definir compressão sem perda de informação crítica.

**Aceitação:** compressão deve preservar claims, proveniência, contradições e incerteza relevantes.

### RAG-SPEC-024 — Context Rot Detection
Deve detectar degradação causada pelo crescimento do contexto.

**Aceitação:** deve existir mecanismo de identificação de perda de desempenho associada ao excesso de contexto.

### RAG-SPEC-025 — Lost-in-the-Middle Harness
Deve avaliar se evidências posicionadas no meio do contexto são recuperadas adequadamente pelo modelo.

**Aceitação:** a posição da evidência deve ser uma variável mensurada.

### RAG-SPEC-026 — Knowledge Gap Detection
Deve identificar quando o conhecimento recuperado é insuficiente.

**Aceitação:** insuficiência deve gerar sinal explícito, não preenchimento especulativo.

### RAG-SPEC-027 — Adaptive Retrieval Loop
Deve permitir nova recuperação quando a primeira iteração não atingir suficiência.

**Aceitação:** novas chamadas devem possuir justificativa e limite.

### RAG-SPEC-028 — Evidence Sufficiency
Deve definir critérios para determinar quando a evidência disponível é suficiente para a tarefa.

**Aceitação:** suficiência deve ser mensurável.

### RAG-SPEC-029 — Evidence Packet Assembly
Deve definir composição final do pacote de evidência.

**Aceitação:** o consumidor recebe evidência, contraevidência, lacunas, confiança e proveniência.

---

## Grupo E — Integração com outras capacidades

### RAG-SPEC-030 — RAG-to-CEM Mapping
Deve definir a relação entre recuperação e camada cognitiva.

**Aceitação:** RAG fornece evidência e contexto, não conclusões obrigatórias.

### RAG-SPEC-031 — RAG-to-Knowledge-Graph Contract
Deve definir consulta e atualização da projeção semântica.

**Aceitação:** o contrato preserva a autoridade do modelo canônico de conhecimento.

### RAG-SPEC-032 — RAG-to-Experience Contract
Deve permitir recuperação de experiências históricas sem confundir episódio com regra geral.

**Aceitação:** experiências permanecem identificáveis como experienciais.

### RAG-SPEC-033 — RAG-to-Learning Contract
Deve permitir que aprendizado utilize sinais de recuperação sem permitir alteração autônoma de conhecimento governado.

**Aceitação:** Learning pode propor melhoria, mas não contorna publicação e governança.

---

## Grupo F — Feedback e adaptação

### RAG-SPEC-034 — RAG Feedback Model
Deve registrar feedback sobre:

- relevância;
- suficiência;
- precisão;
- omissões;
- contradições;
- custo;
- utilidade.

**Aceitação:** feedback deve ser rastreável à consulta e ao Evidence Packet.

### RAG-SPEC-035 — Retrieval Learning
Deve definir como padrões de sucesso e falha podem melhorar estratégias de recuperação.

**Aceitação:** melhoria deve ocorrer de maneira controlada e versionada.

### RAG-SPEC-036 — Retrieval Regression
Deve detectar quando uma mudança de estratégia reduz desempenho.

**Aceitação:** versões anteriores devem permanecer comparáveis.

---

# 12. Harness da Camada RAG

### RAG-SPEC-037 — RAG Harness

O Harness deve verificar:

#### Sensores determinísticos

- presença de provenance;
- integridade de IDs;
- versionamento;
- cobertura de fontes;
- orçamento de tokens;
- limites de chamadas;
- duplicidade;
- temporalidade;
- estrutura do Evidence Packet;
- rastreabilidade.

#### Sensores inferenciais

- relevância;
- suficiência;
- fidelidade;
- coerência;
- qualidade da síntese;
- preservação de incerteza;
- identificação de contradição.

#### Testes

- retrieval tests;
- adversarial retrieval;
- contradiction tests;
- temporal tests;
- context-position tests;
- Lost-in-the-Middle;
- Context Rot;
- regression;
- stress;
- boundary tests.

#### Invariantes

```text
I-RAG-01: Toda evidência deve possuir proveniência.
I-RAG-02: Candidate não equivale a conhecimento publicado.
I-RAG-03: Contexto maior não pode ser assumido como contexto melhor.
I-RAG-04: Contradição relevante não pode ser silenciosamente descartada.
I-RAG-05: Incerteza não pode ser convertida em certeza sem evidência.
I-RAG-06: Experiência não pode ser promovida automaticamente a regra.
I-RAG-07: Router não pode violar orçamento do Scheduler.
I-RAG-08: Compressão não pode eliminar evidência crítica.
I-RAG-09: Toda publicação deve possuir validação compatível com seu impacto.
I-RAG-10: Toda evolução do mecanismo de recuperação deve ser regressivamente avaliada.
```

---

# 13. Quality Gates

### G0 — Contract Integrity
Contratos fundamentais definidos.

### G1 — Source Integrity
Fontes e proveniência verificáveis.

### G2 — Formation Integrity
Knowledge Candidates rastreáveis e semanticamente fiéis.

### G3 — Retrieval Integrity
Estratégias e ranking mensuráveis.

### G4 — Context Integrity
Orçamento, compressão, posição e degradação controlados.

### G5 — Evidence Integrity
Evidence Packet suficiente, rastreável e contraditoriamente consciente.

### G6 — Adaptation Integrity
Feedback e recuperação adaptativa controlados.

### G7 — Regression Integrity
Mudanças comparadas contra baseline.

### G8 — Operational Readiness
Métricas, observabilidade, segurança, versionamento e governança disponíveis.

---

# 14. Métricas

## Recuperação

- Recall@K
- Precision@K
- MRR
- nDCG
- Evidence Coverage
- Evidence Sufficiency
- Contradiction Coverage
- Independent Evidence Coverage

## Contexto

- tokens utilizados;
- densidade de evidência;
- redundância;
- posição da evidência crítica;
- degradação por contexto;
- taxa de Context Rot;
- taxa de Lost-in-the-Middle.

## Qualidade

- factualidade;
- fidelidade;
- relevância;
- completude;
- preservação de incerteza;
- taxa de omissão;
- taxa de contradição perdida.

## Operação

- latência;
- número de chamadas;
- custo;
- tokens recuperados;
- tokens enviados;
- custo por Evidence Packet.

## Evolução

- taxa de Knowledge Gap;
- tempo até correção;
- ganho após feedback;
- regressões;
- retenção de melhorias;
- estabilidade entre versões.

---

# 15. Taxonomia de Falhas

A camada deve distinguir pelo menos:

1. Source Failure
2. Acquisition Failure
3. Parsing Failure
4. Extraction Failure
5. Formation Failure
6. Provenance Failure
7. Publication Failure
8. Retrieval Failure
9. Ranking Failure
10. Contradiction Failure
11. Temporal Failure
12. Context Overflow
13. Context Rot
14. Lost-in-the-Middle
15. Knowledge Gap
16. Evidence Insufficiency
17. Compression Loss
18. Duplication Bias
19. Feedback Failure
20. Regression

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

# 16. Observabilidade

A camada deve produzir rastreabilidade suficiente para reconstruir:

```text
Request
  ↓
Query
  ↓
Strategy
  ↓
Sources Retrieved
  ↓
Evidence Selected
  ↓
Evidence Rejected
  ↓
Context Built
  ↓
Evidence Packet
  ↓
Consumer Result
  ↓
Feedback
```

A observabilidade deve permitir responder:

- o que foi buscado?
- onde foi buscado?
- por que foi selecionado?
- o que foi descartado?
- quanto custou?
- quanto contexto foi usado?
- que evidência faltou?
- houve contradição?
- houve regressão?

---

# 17. Segurança e Integridade

### RAG-SPEC-045 — RAG Security & Integrity

Deve contemplar:

- prompt injection em fontes;
- conteúdo malicioso;
- adulteração de documentos;
- provenance spoofing;
- dados conflitantes;
- fontes não autorizadas;
- contaminação de conhecimento;
- escalada indevida de autoridade;
- exfiltração;
- isolamento entre domínios;
- integridade de versões.

---

# 18. Benchmark

### RAG-SPEC-043 — RAG Benchmark Suite

O benchmark deve avaliar a camada em condições controladas:

- consultas simples;
- consultas complexas;
- múltiplas fontes;
- fontes conflitantes;
- fontes temporais;
- conhecimento disperso;
- evidência crítica em posições distintas;
- contexto curto;
- contexto longo;
- contexto redundante;
- ausência de resposta;
- conhecimento incompleto.

### RAG-SPEC-044 — RAG Economicity Benchmark

Deve medir:

> **valor cognitivo obtido / recurso consumido**

Incluindo:

- tokens;
- chamadas;
- latência;
- custo;
- profundidade de recuperação;
- tamanho do Evidence Packet.

---

# 19. Versionamento

### RAG-SPEC-042 — RAG Versioning

Toda mudança relevante deve identificar:

- versão;
- baseline;
- alteração;
- hipótese;
- impacto esperado;
- métricas antes;
- métricas depois;
- regressões;
- decisão de promoção.

Nenhuma melhoria deve ser considerada válida somente porque produziu uma saída aparentemente melhor em um caso isolado.

---

# 20. Ciclo de Aprimoramento

```text
Métrica
  ↓
Desvio
  ↓
Diagnóstico
  ↓
Hipótese de melhoria
  ↓
Experimento
  ↓
Comparação com baseline
  ↓
Validação
  ↓
Governança
  ↓
Nova versão
  ↓
Monitoramento
```

---

# 21. Ordem recomendada de desenvolvimento

## Fase A — Fundamentos

- 001 Capability Contract
- 002 Request Model
- 003 Source Model
- 004 Source Classification
- 007 Semantic Unit Formation
- 008 Knowledge Candidate Formation
- 011 Publication Contract

## Fase B — Conhecimento

- 005 Acquisition
- 006 Parsing
- 009 Formation Fidelity
- 010 Impact Classification
- 012 Knowledge Graph Projection

## Fase C — Recuperação

- 013 Retrieval Strategy
- 014 Retrieval Routing
- 016 Query Decomposition
- 017 Evidence Ranking
- 018 Evidence Independence
- 019 Contradiction Retrieval
- 020 Temporal Retrieval

## Fase D — Contexto

- 021 Context Budgeting
- 022 Context Packing
- 023 Context Compression
- 024 Context Rot
- 025 Lost-in-the-Middle
- 026 Knowledge Gap
- 027 Adaptive Retrieval
- 028 Evidence Sufficiency
- 029 Evidence Packet

## Fase E — Adaptação

- 034 Feedback
- 035 Retrieval Learning
- 036 Retrieval Regression

## Fase F — Integração

- 015 Scheduler/RAG Resource Contract
- 030 RAG-to-CEM
- 031 RAG-to-Knowledge-Graph
- 032 RAG-to-Experience
- 033 RAG-to-Learning

## Fase G — Harness e Governança

- 037 RAG Harness
- 038 Quality Gates
- 039 Metrics
- 040 Failure Taxonomy
- 041 Observability
- 042 Versioning
- 043 Benchmark Suite
- 044 Economicity Benchmark
- 045 Security & Integrity
- 046 Lifecycle

---

# 22. Critério de Prontidão da Camada

A camada RAG somente deve ser considerada especificada quando existir definição suficiente para:

- Capability Contract;
- Request Model;
- Source Model;
- Knowledge Candidate;
- Evidence Packet;
- classificação de impacto;
- publicação;
- estratégias de recuperação;
- routing;
- orçamento de contexto;
- Context Rot;
- Lost-in-the-Middle;
- Knowledge Gap;
- recuperação adaptativa;
- integração com cognição;
- integração com Knowledge Graph;
- integração com experiência;
- integração com learning;
- métricas;
- benchmark;
- Harness;
- Quality Gates;
- observabilidade;
- versionamento;
- regressão;
- segurança;
- ciclo de evolução.

---

# 23. Regra Arquitetural Final

O RAG do SOT não deve ser avaliado pela quantidade de documentos recuperados.

Seu critério fundamental é:

> **entregar a evidência certa, no contexto certo, no momento certo, com proveniência, incerteza, contradições e custo controlados, para que a camada consumidora possa pensar melhor.**

O RAG fornece **substrato de conhecimento e evidência**.

Ele não substitui:

- cognição;
- julgamento;
- decisão;
- experiência;
- aprendizado;
- governança.

---

## 24. Registro de Especificações

| ID | Especificação | Estado |
|---|---|---|
| RAG-SPEC-001 | RAG Capability Contract | A desenvolver |
| RAG-SPEC-002 | RAG Request Model | A desenvolver |
| RAG-SPEC-003 | Source Model | A desenvolver |
| RAG-SPEC-004 | Source Classification | A desenvolver |
| RAG-SPEC-005 | Acquisition Pipeline | A desenvolver |
| RAG-SPEC-006 | Document and Artifact Parsing | A desenvolver |
| RAG-SPEC-007 | Semantic Unit Formation | A desenvolver |
| RAG-SPEC-008 | Knowledge Candidate Formation | A desenvolver |
| RAG-SPEC-009 | Formation Fidelity | A desenvolver |
| RAG-SPEC-010 | Knowledge Impact Classification | A desenvolver |
| RAG-SPEC-011 | Knowledge Publication Contract | A desenvolver |
| RAG-SPEC-012 | Knowledge Graph Projection | A desenvolver |
| RAG-SPEC-013 | Retrieval Strategy Contract | A desenvolver |
| RAG-SPEC-014 | Retrieval Routing | A desenvolver |
| RAG-SPEC-015 | Scheduler/RAG Resource Contract | A desenvolver |
| RAG-SPEC-016 | Query Decomposition | A desenvolver |
| RAG-SPEC-017 | Evidence Ranking | A desenvolver |
| RAG-SPEC-018 | Evidence Independence | A desenvolver |
| RAG-SPEC-019 | Contradiction Retrieval | A desenvolver |
| RAG-SPEC-020 | Temporal Retrieval | A desenvolver |
| RAG-SPEC-021 | Context Budgeting | A desenvolver |
| RAG-SPEC-022 | Context Packing | A desenvolver |
| RAG-SPEC-023 | Context Compression | A desenvolver |
| RAG-SPEC-024 | Context Rot Detection | A desenvolver |
| RAG-SPEC-025 | Lost-in-the-Middle Harness | A desenvolver |
| RAG-SPEC-026 | Knowledge Gap Detection | A desenvolver |
| RAG-SPEC-027 | Adaptive Retrieval Loop | A desenvolver |
| RAG-SPEC-028 | Evidence Sufficiency | A desenvolver |
| RAG-SPEC-029 | Evidence Packet Assembly | A desenvolver |
| RAG-SPEC-030 | RAG-to-CEM Mapping | A desenvolver |
| RAG-SPEC-031 | RAG-to-Knowledge-Graph Contract | A desenvolver |
| RAG-SPEC-032 | RAG-to-Experience Contract | A desenvolver |
| RAG-SPEC-033 | RAG-to-Learning Contract | A desenvolver |
| RAG-SPEC-034 | RAG Feedback Model | A desenvolver |
| RAG-SPEC-035 | Retrieval Learning | A desenvolver |
| RAG-SPEC-036 | Retrieval Regression | A desenvolver |
| RAG-SPEC-037 | RAG Harness | A desenvolver |
| RAG-SPEC-038 | RAG Quality Gates | A desenvolver |
| RAG-SPEC-039 | RAG Metrics Model | A desenvolver |
| RAG-SPEC-040 | RAG Failure Taxonomy | A desenvolver |
| RAG-SPEC-041 | RAG Observability Contract | A desenvolver |
| RAG-SPEC-042 | RAG Versioning | A desenvolver |
| RAG-SPEC-043 | RAG Benchmark Suite | A desenvolver |
| RAG-SPEC-044 | RAG Economicity Benchmark | A desenvolver |
| RAG-SPEC-045 | RAG Security & Integrity | A desenvolver |
| RAG-SPEC-046 | RAG Lifecycle | A desenvolver |
