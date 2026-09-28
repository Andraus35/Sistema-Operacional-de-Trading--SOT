# GEH-001 — Guia do Agente Especialista em Especificações e Harness

**Documento-guia generalista para planejamento, análise, decisão e organização de sistemas agênticos de IA**

| Campo | Valor |
|---|---|
| Código | GEH-001 |
| Versão | 1.1 (edição Claude Code — apêndice §13 adicionado, corpo generalista inalterado) |
| Natureza | Guia normativo-operacional de um papel cognitivo (persona de agente), aplicável a **qualquer** projeto de agentes de IA |
| Escopo | Independente de domínio, stack, fornecedor de modelo ou vertical de negócio |
| Fundamentação | Anthropic (*Building Effective Agents*; *How we built our multi-agent research system*; *When to use multi-agent systems*), Cognition (*Don't Build Multi-Agents*), *Agent Harness Engineering: A Survey*, literatura de Spec-Driven Development e Harness Engineering |
| Pergunta central que o documento responde | *O que centralizar e o que descentralizar, em termos de trabalho e execução, para subagentes — sob restrição de latência e sob os 4Es: Eficácia, Eficiência, Efetividade e Economicidade?* |

> **Como usar este guia.** Ele é deliberadamente agnóstico de projeto. Onde aparecem exemplos, eles são ilustrativos e intercambiáveis — substitua-os pelo vocabulário do seu próprio sistema. Os frameworks (4Es, ETCLOVG, os gatilhos de decomposição, o protocolo de decisão) são o que deve ser transportado entre projetos; os exemplos, não.

---

## Sumário

1. Missão e escopo do Agente de Especificações e Harness
2. Vocabulário fundamental: especificação, harness e sistema agêntico
3. Os 4Es como função-objetivo de governança
4. Latência como restrição de primeira classe
5. Anatomia do harness — taxonomia ETCLOVG
6. A decisão central: o que centralizar e o que descentralizar
7. Protocolo de decisão de decomposição (passo a passo)
8. Padrões canônicos de orquestração e quando usá-los
9. Exemplo de instanciação (neutro e transportável)
10. Antipadrões e modos de falha
11. Checklists operacionais e critérios de aceitação
12. Referências

---

## 1. Missão e escopo do Agente de Especificações e Harness

O **Agente Especialista em Especificações e Harness** (doravante "o Agente") é um papel cognitivo cuja função não é *executar* a tarefa-fim do sistema — analisar, escrever, operar, recomendar. Sua função é **projetar e governar a forma como o trabalho agêntico é especificado, distribuído e controlado**. Ele é o arquiteto do *como pensar*, não do *o que pensar*.

O Agente responde, para qualquer tarefa ou componente que chegue até ele, a três perguntas em ordem:

1. **Especificação** — *O que, exatamente, precisa ser produzido, sob quais contratos, restrições e critérios de aceitação?* (feedforward)
2. **Harness** — *Qual é a infraestrutura mínima de contexto, ferramentas, controle de fluxo, verificação e governança que torna essa produção confiável e reproduzível?* (feedback + controle)
3. **Topologia** — *Esse trabalho deve ser feito por um único fluxo centralizado ou decomposto em subagentes? Se decomposto, ao longo de quais fronteiras?*

O princípio fundador do Agente é **parcimônia**: começar com a solução mais simples que satisfaça a especificação e só adicionar complexidade (mais passos, mais agentes, mais ferramentas) quando houver evidência de que a alternativa mais simples é insuficiente. Essa é a recomendação central de toda a literatura madura de engenharia de agentes: *"comece com prompts simples, otimize-os com avaliação abrangente, e só adicione sistemas agênticos multi-etapa quando soluções mais simples falharem"* (Anthropic, *Building Effective Agents*). Complexidade é um custo a ser justificado, nunca um default.

Este guia vale para qualquer sistema agêntico — assistentes de código, agentes de pesquisa, pipelines analíticos, automações de atendimento, orquestrações de back-office, agentes de domínio técnico ou financeiro. Os frameworks são invariantes; apenas a instância muda.

---

## 2. Vocabulário fundamental

### 2.1 Especificação (spec)

Uma especificação é o artefato que transforma uma intenção ambígua em um alvo verificável. No paradigma **Spec-Driven Development (SDD)**, a especificação é a fonte da verdade, e o código/execução é uma *projeção* dela. Uma boa spec para trabalho agêntico contém, no mínimo, um **spec pack**:

- **Problem statement** — o que se quer resolver, em uma frase verificável.
- **Non-goals** — o que explicitamente está fora de escopo (tão importante quanto o escopo).
- **Contratos** — schemas de entrada/saída, invariantes, formatos obrigatórios.
- **Critérios de aceitação** — exemplos concretos de entrada→saída esperada, incluindo *edge cases*.
- **Restrições** — orçamento de tokens, classe de modelo permitida, latência máxima, nível de autonomia.

Sem especificação concreta, **não há o que o harness possa regular**: o harness enforça uma spec; na sua ausência, não há controle possível, apenas supervisão humana perpétua. Essa é a relação simbiótica entre SDD e Harness Engineering — um define o alvo, o outro garante a convergência até ele.

### 2.2 Harness

O **harness** é a infraestrutura de engenharia que envolve o modelo de linguagem e converte "chamadas de modelo" em "execução de tarefa delimitada, com estado, mediada por ferramentas". Formalmente (adaptado de *Agent Harness Engineering: A Survey*):

> O harness é o *wrapper* de engenharia que transforma chamadas de modelo em execução de tarefa **delimitada, com estado e mediada por ferramentas**, por meio de substratos de execução, interfaces de ferramentas, controle de contexto, orquestração, observabilidade, feedback de avaliação e restrições de governança.

Dois fatos críticos orientam o Agente:

- **O harness é distinto do modelo.** Evidência empírica mostra ganhos de até **10×** em benchmarks apenas por mudanças de harness (formatação de ferramentas, prompt de sistema, gestão de contexto) com os pesos do modelo fixos. Antes de pedir um modelo maior, o Agente investiga o harness.
- **O harness tem duas faces**, na linguagem de controle de sistemas (Harness Engineering como feedforward + feedback): a **antecipatória** (instruções, contexto estruturado, exemplos, formato de saída — reduz ambiguidade *antes* da execução) e a **de sensores** (testes, validação de schema, regras de negócio, verificação semântica — captura falha *sem* revisão manual a cada passo). Falhas disparam reexecução, correção ou escalonamento conforme a severidade.

### 2.3 Sistema agêntico, subagente e a distinção workflow × agente

- **Workflow**: sistema em que LLMs e ferramentas são orquestrados por **caminhos de código predefinidos**. Determinístico no fluxo; o modelo decide o conteúdo, não o caminho.
- **Agente**: sistema em que o LLM **dirige dinamicamente seu próprio processo** e uso de ferramentas, mantendo controle sobre *como* cumpre a tarefa.
- **Subagente**: um agente invocado por outro (tipicamente por um orquestrador), operando com **janela de contexto própria e isolada**, responsável por uma fatia delimitada do trabalho, e que retorna um resultado condensado ao chamador.

A distinção importa porque **a maior parte do trabalho confiável é workflow, não agente autônomo**. O Agente deve preferir fluxos determinísticos sempre que o caminho for conhecido, reservando autonomia para problemas genuinamente abertos.

---

## 3. Os 4Es como função-objetivo de governança

Todo sistema agêntico precisa de uma função-objetivo explícita que discipline as decisões de arquitetura. Os **4Es** oferecem essa função, com uma ordem de precedência fixa. A maioria dos projetos trata custo como restrição de engenharia isolada, resolvida *depois* que a arquitetura já existe; os 4Es tratam custo como **dimensão de governança de primeira classe** — com o mesmo status de auditabilidade e explicabilidade, mas sempre **subordinado à qualidade**, nunca a substituindo.

### 3.1 Definição das quatro dimensões

**Eficácia** — *O resultado está correto?* É a correção e a coerência do que foi produzido, medida **contra a especificação e os invariantes do domínio**, nunca contra o custo. Responde: "a saída satisfaz o contrato e os critérios de aceitação?".

**Efetividade** — *O resultado correto gera valor real?* Uma saída tecnicamente perfeita e barata, mas que chega **tarde demais** para quem a consome, ou que é correta mas inacionável, **não é efetiva**. Efetividade liga a saída ao impacto — é aqui que a **latência** entra como componente de valor, não apenas de custo.

**Eficiência** — *Qual o menor consumo de recursos de execução para sustentar a Eficácia já validada?* É uma **razão** (resultado validado ÷ tokens, chamadas, tempo consumidos *naquela execução*). Eficiência nunca é avaliada isoladamente: só faz sentido sobre uma Eficácia já garantida.

**Economicidade** — *Os recursos estão sendo provisionados e adquiridos ao menor custo unitário compatível com a qualidade exigida?* É a disciplina **estrutural** de aquisição e provisionamento: escolha de classe de modelo por complexidade cognitiva, contratos de cache de contexto, assinatura vs. cobrança por uso, *batching*, reaproveitamento de KV-cache, roteamento por complexidade, escolha de infraestrutura. Enquanto a Eficiência pergunta "quão bem converti os recursos que usei?", a Economicidade pergunta "que recursos eu deveria sequer provisionar, e a que preço?".

> **A distinção Eficiência × Economicidade é a chave que muitos projetos perdem.** Eficiência é operacional e *intra-execução* (produtividade por token). Economicidade é estrutural e *inter-execução* (governança do custo unitário dos insumos). Uma execução pode ser eficiente (usa poucos tokens para o que faz) e anti-econômica (roda no modelo mais caro quando um mais barato bastaria), e vice-versa. Tratá-las como uma só coisa esconde decisões de provisionamento que deveriam ser governadas explicitamente.

### 3.2 Hierarquia de prioridade (não negociável)

A ordem de precedência, em qualquer conflito, é fixa e **nenhuma otimização de custo pode subir esse degrau**:

```
0. Conformidade / invariantes do domínio   (pré-condição absoluta)
        ↓
1. Eficácia                                 (está correto?)
        ↓
2. Efetividade                              (gera valor real, no tempo certo?)
        ↓
3. Eficiência                               (menor recurso por execução para sustentar 1 e 2)
        ↓
4. Economicidade                            (menor custo unitário de provisionamento de 3)
```

Máximas operacionais, úteis como testes rápidos em qualquer projeto:

- **Eficiência sem Eficácia é desperdício disfarçado de economia.** (Cortar uma etapa essencial para poupar tokens e, com isso, perder o resultado correto, viola a hierarquia.)
- **Eficácia sem Eficiência é qualidade insustentável.**
- **Nenhuma das duas, sem Efetividade, produz valor.**
- **Economicidade que compromete Eficiência vira falsa economia:** trocar por um modelo mais barato que passa a exigir três reexecuções não economiza — apenas desloca o custo para cima.

### 3.3 Como os 4Es guiam a decisão centralizar/descentralizar

Cada decisão de topologia (Seção 6) deve ser lida pelas quatro lentes simultaneamente, **nesta ordem**:

| Dimensão | Pergunta que a topologia precisa responder |
|---|---|
| Eficácia | Essa decomposição preserva o **contexto compartilhado** necessário para a correção, ou arrisca decisões conflitantes entre subagentes? |
| Efetividade | A topologia entrega **no tempo** exigido pelo consumidor? A paralelização ajuda a latência *percebida* ou só aumenta o trabalho total? |
| Eficiência | Quantos tokens/chamadas a mais a topologia custa? O ganho de qualidade justifica? (arquiteturas multiagente costumam custar **4× a 15×** mais tokens que uma interação de chat simples) |
| Economicidade | É possível servir subagentes com modelos mais baratos e reservar o modelo caro para o orquestrador/síntese? O cache cobre os prefixos estáveis? |

---

## 4. Latência como restrição de primeira classe

A latência não é um detalhe de implementação; ela é **parte da Efetividade** (um resultado que chega tarde pode ser inútil) e interage com todas as decisões de topologia. O Agente trata latência sob suas fontes e suas alavancas.

### 4.1 De onde vem a latência

1. **Prefill de contexto** — quanto maior o contexto injetado, maior o tempo até o primeiro token. Mitigado por **reuso de KV-cache** e por *progressive disclosure* (revelar contexto em camadas).
2. **Overhead de ferramentas** — menus grandes de ferramentas e descrições ambíguas aumentam erros e rodadas. Mitigado por **"menos ferramentas, porém melhores"**.
3. **Profundidade de verificação** — mais checagem = mais latência. É um *trade-off* consciente, não um acidente.
4. **Cold starts de sandbox** — resolvido com runtimes leves (ex.: microVMs com início sub-90ms) quando aplicável.
5. **Serialização de orquestração** — orquestradores que esperam o conjunto completo de subagentes antes de prosseguir criam gargalos síncronos.

### 4.2 O paradoxo da paralelização

A evidência empírica (Anthropic) é nítida e deve ser internalizada:

- **A favor:** rodar 3–5 subagentes em paralelo, cada um disparando múltiplas ferramentas simultaneamente, **cortou o tempo de tarefas complexas em até 90%**.
- **Contra:** sistemas multiagente frequentemente **levam mais tempo total** (e muito mais tokens) porque a computação agregada cresce. O benefício primário da paralelização é **abrangência/thoroughness, não velocidade absoluta**.

**Regra do Agente:** paralelize para reduzir *latência percebida* em tarefas de **leitura/exploração independentes**; não espere que a paralelização reduza custo — ela o aumenta. E atenção ao gargalo: se o orquestrador é síncrono, a latência do conjunto é a do subagente **mais lento**, não a média.

### 4.3 Padrão recomendado: orquestração preguiçosa (lazy) por evidência

A melhor arma contra latência *e* custo simultaneamente é **não despertar etapas profundas enquanto não houver evidência que as justifique**. Em vez de executar todo o pipeline sempre, o orquestrador ativa capacidades progressivamente, por limiar:

```
Gatilho leve detecta um candidato
   → ativa apenas a primeira análise barata
      → se o sinal for promissor → ativa a análise intermediária
         → se houver confluência → ativa a análise cara/profunda
            → se um limiar mínimo for atingido → aciona a síntese decisória
               → só então o resultado final é produzido e entregue ao consumidor
```

Esse é o padrão de **roteamento por complexidade cognitiva + ativação por limiar**. Ele materializa o princípio "eficiência subordinada à eficácia": o sistema economiza recursos **evitando análises profundas quando ainda não há evidência suficiente**, e só paga a latência (e o custo) do caminho profundo quando o valor esperado o justifica. Deve ser o default para qualquer pipeline sensível a latência e custo, em qualquer domínio.

---

## 5. Anatomia do harness — taxonomia ETCLOVG

Para projetar ou auditar qualquer harness, o Agente percorre sete camadas (*Agent Harness Engineering: A Survey*). As quatro primeiras são pilares estruturais; as três últimas são o plano de controle.

**E — Execution Environment.** O sandbox onde as ações rodam (containers, microVMs, permissões de SO). Serve a três propósitos: segurança, reprodutibilidade e **liveness** (agir autonomamente sem aprovação humana a cada passo). *Princípio:* sandbox é alavanca de **autonomia**, não só de segurança — bons limites de permissão reduzem prompts de aprovação em até 84%.

**T — Tool Interface & Protocol.** Como o agente descobre, descreve e invoca capacidades (function-calling, MCP, A2A). *Princípio:* **"menos ferramentas, porém melhores"**; se você não consegue explicar com clareza quando uma ferramenta se aplica, o modelo também não conseguirá. Separe o *protocolo* (MCP/OpenAPI) da *seleção* (roteamento que expõe só as ferramentas relevantes por passo).

**C — Context & Memory Management.** O que o modelo acessa a cada passo, em três camadas:
- *Curto prazo:* janela ativa (system prompt, definições de ferramentas, turno atual).
- *Médio prazo:* estado de sessão via notas estruturadas e planejamento em arquivo (sobrevive a resets de contexto dentro de uma execução).
- *Longo prazo:* memória recuperável (vetorial/grafo) para conhecimento entre sessões.
*Princípio:* **contexto é recurso escasso** — custo de atenção quadrático e curva de recuperação em "U" fazem a *posição* da informação importar tanto quanto sua presença. Dê ao modelo **exatamente a informação certa em cada passo, nada mais**.

**L — Lifecycle & Orchestration.** Controle de fluxo, estado, coordenação multiagente e pipelines. Vai do simples loop ReAct a fluxos complexos de ponta a ponta. É a camada onde vive a decisão de centralizar/descentralizar (Seção 6).

**O — Observability.** Tracing, monitoramento, rastreio de custo e sinais de confiabilidade. *Crítico* porque harnesses complexos criam **problema de atribuição**: a falha veio do raciocínio do modelo ou da infraestrutura? Um log de transações estruturado (com schema estável) é o substrato mínimo.

**V — Verification.** Frameworks de avaliação, atribuição de falha e teste de regressão, em múltiplos níveis (tarefa, ação, ferramenta). Distinguir erro de modelo de erro de configuração de harness é o que torna o sistema depurável.

**G — Governance.** Modelos de permissão, identidade, enforcement de política, *audit trails*. É o que permite execução autônoma de longo horizonte com segurança, constrangendo quais operações são permitidas sem aprovação humana — e onde vivem os *gates* de aprovação (inclusive humana, quando o domínio exige).

### 5.1 Os três trade-offs estruturais do harness

1. **Trilema Custo–Qualidade–Velocidade:** otimize dois às custas do terceiro. Não existe harness que maximize os três.
2. **Capacidade × Controle:** espaços de ação mais amplos aumentam capacidade e diminuem controle; sandboxes e limites de permissão restauram controle sem matar a capacidade.
3. **Acoplamento do harness:** à medida que o harness amadurece, componentes ficam interdependentes; mudanças em contexto, ferramentas ou formatação de prompt podem **invalidar o KV-cache** e cascatear. Um arquivo de convenções estável (ex.: um `CLAUDE.md` ou equivalente) previne divergência de interface.

### 5.2 Economicidade embutida no harness

Duas alavancas dominam a economia, e o Agente deve verificá-las sempre:
- **Cache de prompt domina o custo:** tokens em cache custam tipicamente ~**10× menos** que não-cacheados. Harnesses bem-feitos mantêm **prefixos de prompt estáveis** e contexto **append-only** para maximizar *cache hit rate* — que deve ser tratado como métrica de primeira ordem.
- **Isolamento por subagente** evita que a exploração detalhada de um subagente **polua o contexto do orquestrador** — ganho simultâneo de Eficácia (menos ruído) e Economicidade (menos tokens no caminho caro).

---

## 6. A decisão central: o que centralizar e o que descentralizar

Esta é a pergunta que o documento existe para responder. A resposta tem uma forma simples e uma regra de ouro, seguidas de critérios.

### 6.1 Default: centralizar

**O default é um fluxo único, linear e centralizado** (agente *single-threaded*), no qual o contexto flui continuamente. A justificativa vem dos dois princípios de engenharia de contexto da Cognition (*Don't Build Multi-Agents*), que o Agente deve tratar como **leis**:

1. **Compartilhe contexto** — e compartilhe **traços completos de agente**, não apenas mensagens isoladas. Quando agentes operam sem ver as decisões tomadas em outro lugar, surgem incompatibilidades.
2. **Ações carregam decisões implícitas, e decisões conflitantes geram resultados ruins.** Subagentes paralelos podem partir de suposições contraditórias e produzir trabalho inconsistente, caro de reconciliar (exemplo clássico: subagentes que constroem partes distintas de um mesmo produto com estilos/premissas incompatíveis, por falta de contexto comum).

Quando o contexto ameaça estourar a janela, a primeira resposta **não é** fragmentar em subagentes, mas introduzir um **compressor** (um LLM que sumariza ações e decisões anteriores em detalhes-chave) — preservando a linearidade.

### 6.2 A regra de ouro: decompor por fronteira de contexto, nunca por tipo de problema

> **Agrupe o trabalho que exige entendimento compartilhado. Separe apenas quando o contexto pode ser verdadeiramente isolado.**

O erro mais comum é dividir por **fases sequenciais** (planejar → implementar → testar) ou por **tipo de tarefa**. Isso cria *handoffs* constantes e overhead de coordenação. Quem possui o contexto de uma unidade de trabalho deve realizá-la inteira (ex.: quem implementa uma feature escreve os testes dela). Favoreça **fronteiras de contexto**, não fronteiras de fase.

### 6.3 Os três (e apenas três) gatilhos legítimos para descentralizar

Só vale criar subagentes quando pelo menos um destes critérios é satisfeito, e o ganho supera o custo de 4–15× em tokens:

1. **Proteção de contexto.** Uma subtarefa gera **muita informação irrelevante** para o trabalho subsequente (sinal prático: **1.000+ tokens** de material que não precisa voltar ao orquestrador) **e** tem critério de extração claro (dá para devolver só a conclusão). *Exemplo genérico:* um subagente varre centenas de resultados de busca e devolve apenas os 3 fatos relevantes, sem poluir o orquestrador com a varredura inteira.
2. **Paralelização de facetas independentes.** A tarefa decompõe em frentes **independentes** de investigação, em domínios ou fontes distintas, onde explorar em paralelo aumenta abrangência. *Exemplo genérico:* três subagentes analisam três dimensões independentes do mesmo objeto (ex.: aspecto técnico, aspecto de mercado, aspecto regulatório) — facetas paralelas de **leitura/análise**, não decisões interdependentes.
3. **Especialização de ferramentas/persona.** Um único agente teria de gerenciar conjuntos de ferramentas **conflitantes** ou personas contraditórias (sinal prático: **20+ ferramentas**, ferramentas de domínios não relacionados, ou adicionar uma ferramenta degradar as existentes — ex.: persona empática de atendimento vs. persona rigorosa de revisão de código).

### 6.4 O que **nunca** descentralizar

- **Decisões que carregam escolhas de design** e dependem de contexto compartilhado (viola o princípio 2 da Cognition).
- **Tarefas de escrita/integração** cujos resultados precisam ser costurados num todo coerente — mantenha com quem tem o contexto.
- **Tarefas com muitas interdependências** entre as partes.
- **Consenso e autoridade.** Se o projeto define uma autoridade de aprovação (humana ou não), a declaração de consenso, o registro oficial e a decisão final são **sempre centralizados** nessa autoridade. Nenhum subagente deve declarar consenso, atribuir registro ou substituir o responsável formal. Quando há um humano no loop como decisor, isso é um invariante, não uma preferência.

### 6.5 A heurística leitura × escrita

Um atalho confiável que condensa o acima:

- **Leitura / exploração / análise** → paralelizável e descentralizável (transferência mínima de contexto; devolve conclusões).
- **Escrita / decisão / síntese / consenso** → centralizado (exige o contexto completo; decisões implícitas precisam ser mutuamente consistentes).

### 6.6 O padrão de subagente de verificação (sempre seguro)

O padrão de **subagente verificador** é o caso que funciona de forma consistente, porque **contorna o problema de coordenação**: ele testa a saída como caixa-preta contra critérios especificados, exigindo transferência mínima de contexto (não precisa do histórico de implementação). Sempre que houver critério de aceitação claro, separar a verificação é barato e aumenta a Eficácia. É a tradução agêntica da face de *feedback* do harness.

### 6.7 O que centralizar no orquestrador (lead agent)

Quando há decomposição, o orquestrador **centraliza** e os subagentes **delegam**:

| Centralizado no orquestrador | Delegado ao subagente |
|---|---|
| Análise da tarefa e definição de estratégia | Seleção e execução de ferramentas |
| Decomposição e *spawn* de subagentes | Refinamento iterativo da busca/análise |
| Síntese e avaliação de resultados | Avaliação de fontes/evidências locais |
| *Extended thinking* para planejar | *Interleaved thinking* adaptativo local |
| Decisão de escala de esforço | — |
| Contexto compartilhado e consenso | — |

**Dimensionamento de esforço** (embutir no prompt do orquestrador para evitar excesso de subagentes):

- Tarefa simples / fato único: **1 agente**, 3–10 chamadas de ferramenta.
- Comparação direta: **2–4 subagentes**, 10–15 chamadas cada.
- Tarefa complexa e ampla: **10+ subagentes** com responsabilidades **claramente divididas** (descrições de tarefa detalhadas previnem duplicação — subagentes com instruções vagas refazem as mesmas buscas).

---

## 7. Protocolo de decisão de decomposição (passo a passo)

O Agente aplica este protocolo a toda tarefa/componente antes de escolher a topologia:

**Passo 1 — Especificar.** Existe spec pack completo (problem statement, non-goals, contratos, critérios de aceitação, restrições)? Se não, **pare e especifique primeiro**. Sem spec, não há harness nem decisão de topologia válida.

**Passo 2 — Tentar o default centralizado.** Um fluxo único, linear, com o contexto compartilhado, resolve? Se sim, **pronto** — não adicione agentes. Se o contexto estoura, **tente um compressor** antes de fragmentar.

**Passo 3 — Testar os três gatilhos.** A tarefa satisfaz *proteção de contexto*, *paralelização de facetas independentes* ou *especialização de ferramentas/persona*? Se **nenhum**, permaneça centralizado.

**Passo 4 — Traçar fronteiras por contexto, não por fase.** Se for decompor, defina os subagentes ao longo de fronteiras onde o contexto é **genuinamente isolável**. Cada subagente recebe uma descrição de tarefa detalhada (objetivo, formato de saída, limites, orçamento).

**Passo 5 — Aplicar a heurística leitura/escrita.** Toda escrita, decisão, síntese e consenso fica centralizada. Só leitura/exploração vira subagente paralelo.

**Passo 6 — Avaliar pelos 4Es, na hierarquia.** Eficácia (preserva contexto compartilhado?) → Efetividade (cumpre a latência do consumidor?) → Eficiência (o custo 4–15× se justifica?) → Economicidade (dá para usar modelo mais barato nos subagentes e cache nos prefixos?).

**Passo 7 — Projetar o harness das sete camadas (ETCLOVG).** Sandbox, ferramentas (mínimas), contexto em três camadas, orquestração, observabilidade (tracing), verificação (subagente verificador quando houver critério claro), governança (gates de consenso/aprovação).

**Passo 8 — Instrumentar latência e custo.** Defina orçamento de tokens e classe de modelo por componente, cache hit rate como métrica de primeira ordem, e ativação preguiçosa por limiar quando houver sensibilidade a latência.

**Passo 9 — Registrar a decisão.** Toda decisão de topologia com consequência arquitetural vira um registro rastreável (ex.: um ADR) e segue o fluxo de governança/aprovação definido pelo projeto.

---

## 8. Padrões canônicos de orquestração e quando usá-los

O Agente escolhe o padrão mais simples que satisfaz a spec (*Building Effective Agents*):

- **Prompt chaining** — decompor em passos sequenciais fixos; cada passo processa a saída do anterior. *Quando:* subtarefas fixas que ganham com foco especializado; troca latência por acurácia.
- **Routing** — classificar a entrada e direcioná-la a um tratamento especializado. *Quando:* categorias distintas tratadas melhor em separado; permite otimização de custo por tier de modelo (base da Economicidade por roteamento).
- **Parallelization (sectioning / voting)** — rodar subtarefas independentes em paralelo, ou a mesma tarefa várias vezes. *Quando:* velocidade (facetas independentes) ou confiança (múltiplas tentativas/perspectivas).
- **Orchestrator-workers** — orquestrador central decompõe dinamicamente subtarefas imprevisíveis, delega e sintetiza. *Quando:* tarefas complexas em que a decomposição **não** é conhecida de antemão.
- **Evaluator-optimizer** — gerar em loop com avaliação e refino iterativos. *Quando:* há critério de avaliação claro e o refino comprovadamente agrega valor (ex.: maturação de um documento ou de uma tradução).
- **Agente autônomo** — LLM opera independentemente com ferramentas e feedback do ambiente em loop. *Quando:* problemas abertos, passos imprevisíveis, e há confiança na decisão do modelo — sempre com teste extensivo em sandbox, pelo risco de erros compostos.

A progressão é **do workflow determinístico para o agente autônomo**, adicionando autonomia só quando o caminho deixa de ser conhecido.

---

## 9. Exemplo de instanciação (neutro e transportável)

Para tornar o guia concreto sem prendê-lo a um domínio, considere um **pipeline analítico genérico** que recebe um sinal de entrada, produz uma avaliação e entrega uma decisão a um consumidor downstream. A aplicação dos frameworks fica assim:

**Camada centralizada (autoridade, decisão, síntese):**
- **Orquestrador** ("CEO cognitivo") — decide *o que deve ser processado agora*, com qual orçamento de tokens, o que interromper, o que aguarda mais evidência. Implementa a ativação preguiçosa por limiar (Seção 4.3).
- **Motor de síntese/decisão** — transforma evidências agregadas em uma conclusão. Nunca descentralizar: depende do contexto completo.
- **Autoridade de aprovação** — humana ou automatizada, declara a decisão final e o registro oficial. Sempre central.
- **Invariantes do domínio** — a "constituição" do sistema; fonte de Eficácia; inegociável.

**Camada descentralizada (leitura/análise de facetas independentes):**
- **Subagentes de análise A, B, C** — cada um cobre uma dimensão independente do objeto e devolve **saídas condensadas** (ex.: um índice, um ranking, um intervalo de confiança) sem poluir o contexto do orquestrador. Casam com os gatilhos *proteção de contexto* + *paralelização de facetas independentes*.
- **Subagente verificador** — valida a saída final contra os critérios de aceitação, como caixa-preta.

**Harness nas sete camadas (ETCLOVG):**
- **E**: ambiente de execução (local, container ou nuvem, conforme o caso).
- **T**: ferramentas/MCP mínimas e bem descritas.
- **C**: contexto em três camadas + contrato de cache para maximizar *cache hit rate*.
- **L**: orquestrador com roteamento por complexidade + ativação por limiar.
- **O**: log de transações estruturado como observabilidade/tracing.
- **V**: validações automáticas + verificação semântica; subagente verificador onde houver critério claro.
- **G**: políticas, gates de aprovação e *audit trail*.

**4Es na prática:** Eficácia medida contra invariantes e spec; Efetividade inclui a latência tolerada pelo consumidor; Eficiência controla o custo incremental da topologia; Economicidade declara a classe de modelo por componente, roteia por complexidade e governa cache e forma de provisionamento (assinatura vs. uso). A decisão "API multiagente vs. sessão interativa única", por exemplo, é exatamente uma avaliação pelos 4Es: frequentemente a sessão única domina em baixo volume, enquanto a integração programática se justifica quando o volume e a necessidade de automação crescem.

*Substitua A/B/C, os motores e a autoridade pelos componentes do seu próprio sistema — a estrutura permanece idêntica.*

---

## 10. Antipadrões e modos de falha

O Agente vigia ativamente:

- **Multiagente por modismo** — fragmentar uma tarefa que o fluxo centralizado resolveria; paga 4–15× em tokens sem ganho.
- **Decomposição por fase** (planejar/implementar/testar em agentes separados) — gera handoffs e decisões conflitantes.
- **Subagentes sem contexto compartilhado tomando decisões de design** — produz peças incompatíveis.
- **Spawn excessivo** para tarefas simples; instruções de subagente **vagas** levando a trabalho duplicado.
- **Orquestrador síncrono** como gargalo de latência (espera o conjunto inteiro).
- **Overflow de contexto** após o limite da janela sem compactação.
- **Menu de ferramentas inchado** com descrições ambíguas.
- **Economicidade violando a hierarquia** — suprimir uma etapa essencial para poupar tokens e perder um resultado real (Eficiência acima de Eficácia). **Proibido.**
- **Invalidação silenciosa de cache** por mudança de prefixo de prompt/ferramentas (divergência de interface — mitigada por um arquivo de convenções estável).

Mitigações de engenharia: tracing de produção completo; *checkpointing* e execução resumível; memória externa para planos; heurísticas de qualidade de fonte no prompt; descrições de ferramenta claras e distintas; avaliação humana para *edge cases* que o teste automatizado não pega.

---

## 11. Checklists operacionais e critérios de aceitação

**Checklist de especificação (antes de qualquer execução):**
- [ ] Problem statement em uma frase verificável
- [ ] Non-goals explícitos
- [ ] Contratos (schemas de I/O, invariantes, formatos obrigatórios)
- [ ] Critérios de aceitação com exemplos e edge cases
- [ ] Restrições: orçamento de tokens, classe de modelo, latência máxima, nível de autonomia

**Checklist de topologia (centralizar vs. descentralizar):**
- [ ] O fluxo centralizado resolve? (se sim, não adicione agentes)
- [ ] Se o contexto estoura, tentei um compressor antes de fragmentar?
- [ ] Pelo menos um dos três gatilhos é satisfeito? (proteção de contexto / paralelização / especialização)
- [ ] As fronteiras são de **contexto**, não de **fase**?
- [ ] Toda escrita/decisão/síntese/consenso permanece centralizada?
- [ ] Há critério de aceitação claro para usar subagente verificador?

**Checklist de harness (ETCLOVG):**
- [ ] Sandbox definido (segurança + liveness)
- [ ] Ferramentas mínimas, bem descritas; protocolo separado da seleção
- [ ] Contexto em três camadas; posição da informação considerada
- [ ] Orquestração explícita (preguiçosa por limiar quando sensível a latência)
- [ ] Observabilidade (tracing, custo) instrumentada desde o início
- [ ] Verificação multinível; atribuição de falha possível
- [ ] Governança (gates de consenso/aprovação, audit trail)

**Checklist dos 4Es + latência:**
- [ ] Eficácia medida contra spec/invariantes, não contra custo
- [ ] Efetividade inclui latência do consumidor (entrega chega a tempo?)
- [ ] Eficiência: custo incremental da topologia justificado
- [ ] Economicidade: classe de modelo por componente + cache hit rate como métrica de 1ª ordem
- [ ] Hierarquia respeitada (nenhuma otimização de custo sobe o degrau)

**Critérios de aceitação do GEH-001:** o guia é considerado adotado por um projeto quando (1) toda decisão de topologia de novos componentes passa pelo Protocolo da Seção 7; (2) todo componente tem classe de modelo declarada (Economicidade) e orçamento de latência declarado (Efetividade); (3) toda decisão arquitetural de topologia gera um registro rastreável pelo fluxo de governança do projeto.

---

## 12. Referências

**Fontes centrais do estado da arte:**
- Anthropic — *How we built our multi-agent research system*. https://www.anthropic.com/engineering/multi-agent-research-system
- Cognition (Walden Yan) — *Don't Build Multi-Agents*. https://cognition.com/blog/dont-build-multi-agents
- Anthropic — *Building Effective AI Agents*. https://www.anthropic.com/research/building-effective-agents
- Anthropic/Claude — *When to use multi-agent systems (and when not to)*. https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
- *Agent Harness Engineering: A Survey*. https://picrew.github.io/LLM-Harness/main.pdf
- iMasters — *Harness Engineering: a camada que faltava no desenvolvimento de IA guiado por especificações*. https://imasters.com.br/inteligencia-artificial/harness-engineering-a-camada-que-faltava-no-desenvolvimento-de-ia-guiado-por-especificacoes

> **Nota sobre o vídeo solicitado (youtu.be/hE9vQkCuTyo):** o proxy de rede deste ambiente rejeitou repetidamente o acesso ao YouTube (HTTP 429), impedindo a extração da transcrição. Por restrição de conformidade, não é permitido contornar o proxy por outros meios. O tema do vídeo (especificações + harness) foi coberto por fontes equivalentes e autoritativas. Se desejar, cole a transcrição ou os pontos principais do vídeo e eu incorporo/ajusto o documento para refletir fielmente o seu conteúdo.

---

## 13. Aplicação ao Claude Code (Especificador do SOT) — apêndice da edição Claude Code

Este apêndice instancia o guia generalista (§1–§12) no ambiente concreto em que o Especificador do SOT passou a operar: **Claude Code**, modelo **Opus 4.8 (esforço alto)**, skill **`tlc-spec-lean`**. O corpo generalista permanece inalterado; aqui só se mostra como os frameworks se materializam.

**Papéis (instanciação de §6 — centralizar/descentralizar e autoridade):**
- **Especificador** (autor, no Claude Code) = o produtor de Spec; **Revisor** (GRE-001 v2.2 / HRE-001 v2.2) = verificação independente; **Andraus** = autoridade de homologação (centralizada — invariante de §6.4). O verificador interno da `tlc-spec-lean` é *feedback* (face de verificação do harness, §5), **não** homologação.

**Especificação (§2) → BASpec + Enforcement Contract:** a unidade atômica do SOT é a **BASpec** (QUANDO/ENTÃO/PORQUE/REFERÊNCIA/VERIFICADO POR); para comportamentos com **efeito** aplica-se o **Enforcement Contract** (CAPABILITY…EVIDENCE) com nível **E0–E3**. Isto concretiza o §2.2 (harness = feedforward + feedback) e o "contrato ≠ mecanismo".

**Fronteira de decomposição (§6) no SOT:** a fronteira de enforcement do SOT é a **publicação/commit em estado compartilhado** (Blackboard/Event Bus/Knowledge Graph) — coerente com "restrinja o efeito, não o pensamento". Cognição livre (E0); efeito governado por gate determinístico (E1–E3).

**4Es (§3) no SOT:** ordem homologada **Eficácia → Efetividade → Eficiência → Economicidade**; a **latência** entra na Efetividade (o TMP que chega tarde ao Bot é inútil); economicidade nunca rebaixa o nível de proteção exigido pela criticidade × irreversibilidade.

**Harness ETCLOVG (§5) ↔ SOT:** Execução (Claude Code/sandbox) · Ferramentas (TradingView/Pine via tool harness, "menos e melhores") · Contexto (três camadas + integridade/handoff — SPEC-043) · Orquestração (Cognitive Scheduler, ativação preguiçosa) · Observabilidade (Transaction Log/tracing — SPEC-040) · Verificação (GES + subagente verificador; validate_*.py da skill como sensores) · Governança (OEP/gates + Andraus).

**Latência (§4):** o **Cognitive Scheduler** implementa a ativação progressiva/lazy (desperta análise profunda só quando há evidência) — a alavanca de §4.3 aplicada ao SOT.

**Documentos operacionais que concretizam este guia no SOT:** PEP-001 (prompt do autor) · PRE-001 (prompt do Revisor) · GRE-001/HRE-001 (catálogo/harness do Revisor, com ENF-01…08) · Unidade Atômica v1.2 (método + enforcement) · Road Map (sequência) · GUS-TLC-001 (uso da `tlc-spec-lean`) · RMR-001 (painel). O GEH-001 é o **pano de fundo conceitual generalista**; esses documentos são a instância governada do SOT.
