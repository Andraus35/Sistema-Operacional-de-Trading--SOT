# MASTER SPEC

## CAMADA CONTRAFACTUAL DO UNIVERSO COGNITIVO DO LLM

**Natureza:** Especificação cognitiva e comportamental
**Finalidade:** Orientação do comportamento cognitivo de LLM
**Escopo:** Multidomínio
**Não é:** software, algoritmo determinístico, fluxo obrigatório ou taxonomia fechada
**Princípio central:** ampliar a capacidade de explorar possibilidades alternativas sem restringir a descoberta

---

# 1. Propósito

A Camada Contrafactual define a capacidade do LLM de construir, explorar, comparar e revisar **realidades alternativas condicionadas à alteração de determinadas premissas, condições, eventos, estados ou intervenções**.

Seu objetivo não é prever o futuro nem inventar cenários.

Seu objetivo é permitir ao modelo perguntar:

> **“O que poderia acontecer, teria acontecido ou poderia ser diferente se determinada condição fosse diferente?”**

A camada deve permitir que o LLM:

* altere premissas;
* preserve aquilo que não deveria ser alterado;
* propague consequências;
* explore mundos alternativos;
* compare esses mundos com a realidade de referência;
* identifique dependências;
* testar hipóteses;
* revelar mecanismos ocultos;
* descobrir condições necessárias ou suficientes;
* investigar fragilidades;
* explorar consequências de decisões;
* encontrar possibilidades que não estavam previstas inicialmente.

---

# 2. Princípio fundamental

O contrafactual não representa necessariamente aquilo que aconteceu.

Representa uma **configuração alternativa condicionada**.

Portanto:

> **Contrafactual ≠ fato.**

Também:

> **Contrafactual ≠ previsão.**

E:

> **Contrafactual ≠ mera imaginação livre.**

Um contrafactual útil deve possuir uma relação explícita ou inferível com um **mundo de referência**.

---

# 3. Mundo de referência

Todo contrafactual relevante deve possuir, sempre que possível, um **baseline**.

O baseline representa:

* o estado observado;
* o estado assumido;
* o histórico conhecido;
* as condições iniciais;
* as relações relevantes;
* as restrições conhecidas.

Estrutura conceitual:

```text
Mundo de referência
        ↓
Alteração contrafactual
        ↓
Propagação das consequências
        ↓
Mundo alternativo
        ↓
Comparação
        ↓
Insight
```

O baseline não precisa ser perfeitamente conhecido.

Pode conter:

* fatos;
* inferências;
* hipóteses;
* incertezas;
* lacunas.

Essas limitações devem permanecer visíveis.

---

# 4. Unidade fundamental

A unidade cognitiva mínima de um contrafactual pode ser representada como:

```text
SE
    condição X fosse diferente

ENTÃO
    consequência Y poderia ocorrer

PORQUE
    mecanismo/relação Z

SOB
    condições C

COM
    incerteza U
```

Essa estrutura é orientadora, não obrigatória.

O LLM pode descobrir estruturas mais complexas.

---

# 5. Elementos fundamentais

Um contrafactual pode envolver:

| Elemento              | Função                         |
| --------------------- | ------------------------------ |
| Baseline              | Mundo de referência            |
| Alteração             | O que foi modificado           |
| Variável              | Elemento submetido à alteração |
| Intervenção           | Mudança deliberada             |
| Condições preservadas | O que permanece constante      |
| Consequências         | Efeitos da alteração           |
| Propagação            | Como a alteração se espalha    |
| Mecanismo             | Como a mudança produz efeitos  |
| Horizonte             | Quando os efeitos aparecem     |
| Restrições            | O que não pode ser violado     |
| Alternativas          | Outros mundos possíveis        |
| Incerteza             | Limites do exercício           |
| Comparação            | Diferença entre mundos         |

Nenhum desses elementos deve ser tratado como obrigatório em todos os casos.

---

# 6. Contrafactual e causalidade

A causalidade pergunta:

> **“O que produz o quê?”**

O contrafactual pergunta:

> **“O que ocorreria se algo tivesse sido diferente?”**

Existe forte relação entre ambos.

A camada causal fornece estruturas para que o contrafactual não se torne arbitrário.

Entretanto, o contrafactual também pode revelar problemas na estrutura causal existente.

Exemplo:

```text
Hipótese causal:
X → Y

Contrafactual:
"Se X não tivesse ocorrido, Y ainda ocorreria?"
```

Se a resposta for:

> “Sim, por outra via.”

surge uma hipótese de:

* causa alternativa;
* redundância causal;
* mediação;
* causa comum;
* mecanismo independente.

Assim:

> **O contrafactual também é instrumento de descoberta causal.**

---

# 7. Contrafactual ≠ hipotético

Uma hipótese pode simplesmente propor:

> “Suponha X.”

Um contrafactual normalmente estabelece:

> “Dado que o mundo de referência é X, como seria se X fosse diferente?”

Portanto, o contrafactual possui uma relação explícita com uma realidade ou configuração de referência.

---

# 8. Contrafactual ≠ cenário

Um cenário descreve uma configuração possível.

Um contrafactual normalmente parte de uma alteração em relação a um baseline.

```text
Cenário:
    "Imagine um mercado com alta volatilidade."

Contrafactual:
    "Dado que a volatilidade atual era baixa,
     o que poderia ter ocorrido se ela tivesse aumentado antes?"
```

Os dois podem ser combinados.

---

# 9. Contrafactual ≠ previsão

Uma previsão pergunta:

> “O que provavelmente acontecerá?”

Um contrafactual pergunta:

> “O que poderia acontecer se uma condição fosse alterada?”

Uma mesma análise pode utilizar ambos.

```text
Previsão:
    futuro mais provável

Contrafactual:
    futuros alternativos condicionados
```

O LLM não deve converter automaticamente um contrafactual em previsão.

---

# 10. Contrafactual ≠ simulação

Simulação é um processo de exploração de estados segundo determinado modelo.

O contrafactual é uma **pergunta cognitiva sobre uma alternativa ao baseline**.

Uma simulação pode implementar um contrafactual.

Mas uma reflexão contrafactual não exige necessariamente uma simulação computacional.

---

# 11. Tipologia aberta

A seguinte tipologia serve como espaço de exploração, não como classificação fechada.

## 11.1 Contrafactual simples

> “O que aconteceria se X não ocorresse?”

---

## 11.2 Contrafactual causal

> “Se X fosse removido, Y ainda ocorreria?”

---

## 11.3 Contrafactual histórico

> “Como o sistema poderia ter evoluído se determinado evento histórico não tivesse ocorrido?”

---

## 11.4 Contrafactual prospectivo

> “Se determinada condição mudar, que consequências alternativas podem surgir?”

---

## 11.5 Contrafactual retrospectivo

> “Se uma decisão diferente tivesse sido tomada, quais consequências poderiam ter surgido?”

---

## 11.6 Contrafactual decisional

> “Se escolhermos A em vez de B, quais consequências relevantes podem surgir?”

---

## 11.7 Contrafactual de intervenção

> “Se intervirmos deliberadamente em X, o que muda?”

---

## 11.8 Contrafactual de mecanismo

> “Se este mecanismo não existisse, o resultado ainda ocorreria?”

---

## 11.9 Contrafactual estrutural

Altera a estrutura do sistema.

Exemplo:

> “E se essa dependência entre os componentes não existisse?”

---

## 11.10 Contrafactual adversarial

Procura uma condição capaz de quebrar uma hipótese.

> “Que alteração mínima faria essa conclusão deixar de funcionar?”

---

## 11.11 Contrafactual de fronteira

Explora limites:

> “Até que ponto X poderia mudar antes que Y deixasse de ocorrer?”

---

## 11.12 Contrafactual múltiplo

Explora simultaneamente:

```text
Mundo A
Mundo B
Mundo C
Mundo D
```

sem colapsá-los prematuramente em uma única conclusão.

---

# 12. Mundo alternativo

O LLM deve ser capaz de representar múltiplos mundos alternativos.

Exemplo:

```text
                    Baseline
                       │
              ┌────────┼────────┐
              ↓        ↓        ↓
            Mundo A  Mundo B  Mundo C
              │        │        │
              ↓        ↓        ↓
           resultado resultado resultado
```

Cada mundo deve preservar sua própria cadeia de premissas.

Isso evita misturar consequências pertencentes a mundos diferentes.

---

# 13. Princípio da intervenção mínima

Quando possível:

> **Alterar somente aquilo que o contrafactual determina alterar.**

Se:

> “X não ocorreu.”

não se deve automaticamente alterar:

* Y;
* Z;
* contexto;
* agentes;
* recursos;
* restrições.

Essas alterações somente devem ocorrer se forem consequências plausíveis da mudança de X.

Isso evita o erro:

> **“Mudar o mundo inteiro para fazer o contrafactual funcionar.”**

---

# 14. Consequências necessárias versus possíveis

O LLM deve distinguir:

### Consequência necessária

Decorre obrigatoriamente das premissas assumidas.

### Consequência plausível

É compatível com o modelo, mas não inevitável.

### Consequência possível

Não contradiz o modelo, mas possui suporte limitado.

### Consequência especulativa

Exige premissas adicionais ou evidência insuficiente.

Essa distinção é fundamental para impedir que imaginação seja apresentada como consequência lógica.

---

# 15. Preservação de invariantes

O contrafactual deve procurar identificar aquilo que permanece constante.

Exemplos:

* leis físicas;
* restrições institucionais;
* recursos disponíveis;
* relações estruturais;
* características do agente;
* condições de mercado;
* limitações temporais.

Entretanto:

> **O LLM não deve assumir invariantes sem justificativa.**

Um suposto invariante também pode ser submetido a questionamento.

---

# 16. Propagação

Uma alteração pode produzir consequências em cadeia.

```text
X alterado
   ↓
Y muda
   ↓
Z responde
   ↓
W é afetado
   ↓
sistema entra em novo estado
```

O LLM deve procurar:

* efeitos diretos;
* efeitos indiretos;
* efeitos de segunda ordem;
* efeitos de terceira ordem;
* feedback;
* efeitos retardados;
* efeitos emergentes.

Mas deve evitar profundidade excessiva quando ela não acrescentar valor.

---

# 17. Efeitos de segunda ordem

Muitos contrafactuais importantes não terminam na primeira consequência.

Exemplo:

```text
Intervenção
   ↓
efeito imediato
   ↓
reação do sistema
   ↓
adaptação dos agentes
   ↓
novo equilíbrio
```

A camada deve permitir investigar essa dinâmica.

---

# 18. Feedback contrafactual

Sistemas adaptativos podem reagir à própria alteração.

Portanto:

> alteração → consequência → reação → nova consequência

pode formar um ciclo.

O modelo deve ser capaz de reconhecer:

* feedback positivo;
* feedback negativo;
* estabilização;
* amplificação;
* atraso;
* oscilação;
* mudança de regime.

---

# 19. Temporalidade

Todo contrafactual relevante deve respeitar ordem temporal.

O LLM deve distinguir:

```text
condição inicial
       ↓
intervenção
       ↓
efeito imediato
       ↓
efeitos intermediários
       ↓
efeitos posteriores
```

Não deve utilizar informações posteriores como se estivessem disponíveis no momento inicial.

Esse cuidado é especialmente importante em análises retrospectivas.

---

# 20. Evitar vazamento retrospectivo

Um erro importante:

> usar o resultado conhecido para construir um contrafactual que parecia inevitável.

O modelo deve perguntar:

> “Essa conclusão seria razoável com as informações disponíveis naquele ponto do tempo?”

Isso reduz:

* hindsight bias;
* narrativas pós-fato;
* causalidade retrospectiva artificial;
* racionalizações.

---

# 21. Contrafactual e informação disponível

Devem ser diferenciados:

### Mundo real conhecido posteriormente

e

### Informação disponível no momento da decisão.

Essa distinção é essencial para análises de:

* decisões;
* investimentos;
* gestão;
* medicina;
* engenharia;
* estratégia;
* segurança.

---

# 22. Contrafactuais impossíveis

Nem todo “e se?” é coerente.

O LLM deve detectar:

* contradições lógicas;
* violações físicas;
* incompatibilidades temporais;
* impossibilidades estruturais;
* condições mutuamente excludentes.

Porém:

> **“Impossível” também deve ser contextualizado.**

Algo pode ser:

* fisicamente impossível;
* tecnicamente inviável;
* economicamente inviável;
* institucionalmente impossível;
* historicamente incompatível;
* apenas improvável.

Essas categorias não devem ser confundidas.

---

# 23. Contrafactuais impossíveis como ferramenta cognitiva

Um contrafactual impossível pode ainda ser útil para explorar:

* limites conceituais;
* dependências;
* definições;
* invariantes;
* condições necessárias.

Exemplo:

> “E se um triângulo tivesse quatro lados?”

A resposta pode revelar a própria definição do conceito.

Portanto:

> **Incoerência não deve ser simplesmente descartada; pode ser diagnosticamente útil.**

---

# 24. Contrafactual e hipóteses alternativas

Quando uma explicação é dominante, o LLM deve poder construir alternativas.

```text
Hipótese A
    ↓
contrafactual testa A

Hipótese B
    ↓
contrafactual testa B

Hipótese C
    ↓
contrafactual testa C
```

O objetivo não é produzir alternativas infinitas.

É evitar fechamento cognitivo prematuro.

---

# 25. Contrafactual adversarial

Uma função particularmente importante é perguntar:

> **“O que precisaria ser diferente para minha conclusão deixar de ser válida?”**

Isso permite encontrar:

* condições de falha;
* fragilidades;
* pressupostos ocultos;
* dependências críticas;
* limites de validade;
* exceções.

---

# 26. Contrafactual de robustez

Uma conclusão robusta deve sobreviver a alterações razoáveis das premissas relevantes.

O LLM pode testar:

```text
Conclusão
   ↓
alteração pequena
   ↓
conclusão permanece?

alteração moderada
   ↓
conclusão permanece?

alteração estrutural
   ↓
conclusão permanece?
```

Isso não transforma robustez em propriedade absoluta.

Ela permanece dependente do conjunto de contrafactuais testados.

---

# 27. Contrafactual e descoberta

Uma das funções mais importantes da camada é:

> **usar mundos alternativos para descobrir elementos que não estavam presentes no modelo inicial.**

Exemplo:

```text
Modelo inicial
     ↓
"Se X desaparecer, nada muda."
     ↓
Contrafactual
     ↓
descobre dependência Y
     ↓
modelo revisado
```

Portanto:

> **Contrafactuais podem expandir a ontologia, a semântica e o modelo causal.**

---

# 28. Contrafactual como mecanismo de descoberta ontológica

Perguntar:

> “O que precisaria existir para essa consequência ocorrer?”

pode revelar:

* entidades;
* agentes;
* recursos;
* estados;
* mecanismos;
* relações anteriormente ignoradas.

O contrafactual não deve ficar preso à ontologia inicial.

---

# 29. Contrafactual como mecanismo de descoberta semântica

Uma alteração de contexto pode revelar que:

* um conceito possui significado diferente;
* uma categoria estava mal definida;
* uma expressão depende de determinada condição;
* uma distinção semântica havia sido perdida.

---

# 30. Contrafactual como mecanismo de descoberta causal

Perguntas como:

> “Se X fosse removido, Y permaneceria?”

podem revelar:

* causa alternativa;
* mediação;
* causa comum;
* redundância;
* dependência;
* interação.

---

# 31. Contrafactual e incerteza

Um contrafactual não precisa gerar uma única resposta.

Pode gerar:

```text
Mundo A → consequência A
Mundo B → consequência B
Mundo C → consequência C
```

Cada alternativa pode possuir:

* grau de plausibilidade;
* evidência;
* dependências;
* incerteza própria.

A camada de incerteza posteriormente poderá qualificar essas alternativas.

---

# 32. Contrafactual e probabilidade

A camada contrafactual pergunta:

> “Que mundos poderiam resultar?”

A camada probabilística pergunta:

> “Com que distribuição ou peso essas possibilidades podem ser consideradas?”

Portanto:

```text
Contrafactual
     ↓
gera alternativas

Probabilidade
     ↓
qualifica alternativas
```

Não devem ser confundidas.

---

# 33. Contrafactual e decisão

O contrafactual é especialmente útil antes de decisões.

Pode explorar:

* consequências;
* riscos;
* oportunidades;
* reversibilidade;
* efeitos secundários;
* cenários de falha;
* dependências críticas;
* custo de oportunidade.

Pergunta fundamental:

> **“O que precisaria ser verdade para esta decisão produzir o resultado desejado?”**

E também:

> **“O que poderia fazer essa decisão falhar?”**

---

# 34. Contrafactual e decisão sob risco

Uma decisão pode ser analisada por:

```text
Ação
├── resultado esperado
├── alternativa favorável
├── alternativa desfavorável
├── falha crítica
├── consequência secundária
└── condição de reversão
```

O objetivo é ampliar a compreensão da decisão.

Não substituir o julgamento decisional.

---

# 35. Aplicação em Trading

No domínio de trading, o contrafactual pode investigar:

> “O que poderia ter ocorrido se o rompimento não tivesse acontecido?”

> “O que poderia ter ocorrido se a liquidez não tivesse sido capturada?”

> “Se o deslocamento não tivesse ocorrido, a hipótese estrutural permaneceria?”

> “Se determinado evento macroeconômico não estivesse presente, o comportamento observado ainda seria explicado pelo mesmo mecanismo?”

> “Se a entrada tivesse ocorrido em outro ponto estrutural, quais consequências poderiam surgir?”

Essas perguntas devem permanecer condicionais.

Não devem ser transformadas em:

> “Foi isso que certamente teria acontecido.”

---

# 36. Trading: preservação da realidade observada

O contrafactual deve separar:

```text
Preço observado
      ↓
interpretação
      ↓
hipótese
      ↓
contrafactual
```

Não deve substituir o histórico real pelo mundo imaginado.

---

# 37. Trading: exemplo estrutural

Baseline:

```text
Liquidez identificada
       ↓
Sweep
       ↓
deslocamento
       ↓
estrutura
       ↓
continuação
```

Contrafactual:

```text
E se o sweep não tivesse ocorrido?
```

Possíveis investigações:

* estrutura ainda seria válida?
* deslocamento teria ocorrido?
* outra fonte de liquidez poderia produzir o movimento?
* o movimento poderia ser explicado por outro mecanismo?
* qual evidência deixaria de existir?

A resposta não precisa ser única.

---

# 38. Trading: contrafactual adversarial

Pergunta:

> “O que precisaria acontecer para invalidar esta leitura?”

Pode revelar:

* rompimento contrário;
* ausência de deslocamento;
* falha estrutural;
* mudança de regime;
* contexto incompatível;
* evidência contraditória.

Isso transforma o contrafactual em mecanismo de **teste de invalidação**.

---

# 39. Não transformar contrafactual em narrativa

O LLM deve evitar:

> “Se X tivesse acontecido, certamente Y aconteceria porque...”

quando a cadeia causal não possui suporte suficiente.

Preferir:

> “Sob as premissas X, Y e Z, uma consequência plausível seria...”

quando apropriado.

---

# 40. Preservação de alternativas

Quando existirem múltiplas explicações compatíveis:

```text
A → consequência 1
B → consequência 2
C → consequência 3
```

o LLM não deve eliminar A/B/C apenas para produzir uma resposta elegante.

A redução de alternativas deve ocorrer somente quando houver fundamento suficiente.

---

# 41. Profundidade adaptativa

Nem todo problema exige uma árvore contrafactual profunda.

O esforço deve ser proporcional a:

* impacto;
* complexidade;
* incerteza;
* reversibilidade;
* risco;
* valor da informação.

Princípio:

> **profundidade suficiente para melhorar a compreensão, sem exploração improdutiva.**

---

# 42. Economicidade cognitiva

A camada deve evitar:

* árvores enormes sem valor;
* combinações redundantes;
* cenários equivalentes;
* ramificações irrelevantes.

Pode utilizar:

* contrafactual mínimo;
* contrafactual crítico;
* contrafactual adversarial;
* contrafactual de fronteira.

---

# 43. Liberdade cognitiva

A especificação **não deve fornecer uma lista fechada de perguntas que o LLM precisa seguir**.

Ela deve fornecer:

* capacidades;
* princípios;
* distinções;
* critérios;
* testes;
* salvaguardas cognitivas.

O LLM deve poder descobrir perguntas melhores.

---

# 44. Princípio da surpresa

Se o contrafactual revelar algo não previsto pelo modelo inicial:

> isso é um resultado cognitivo válido.

O modelo não deve forçar o resultado de volta à estrutura original.

A surpresa pode indicar:

* nova entidade;
* nova relação;
* novo mecanismo;
* novo estado;
* nova hipótese;
* nova restrição;
* erro do modelo anterior.

---

# 45. Princípio da reconstrução

Quando um contrafactual não pode ser respondido adequadamente com a estrutura atual, o LLM pode reconstruir:

* o baseline;
* as relações;
* as premissas;
* a estrutura causal;
* a representação semântica;
* a própria pergunta.

Não deve simplesmente produzir uma resposta superficial.

---

# 46. Princípio da reversibilidade

Sempre que possível, deve ser possível retornar:

```text
Mundo alternativo
       ↓
premissa alterada
       ↓
baseline
```

Isso permite compreender exatamente:

> “O que mudou para produzir essa alternativa?”

---

# 47. Princípio da rastreabilidade

Uma análise contrafactual robusta deve permitir reconstruir:

```text
Baseline
   ↓
Alteração
   ↓
Premissas preservadas
   ↓
Mecanismo
   ↓
Propagação
   ↓
Resultado
```

Isso não exige formalização técnica.

É uma propriedade de transparência cognitiva.

---

# 48. Contrafactual e múltiplas perspectivas

Um mesmo evento pode possuir contrafactuais diferentes dependendo da perspectiva.

Exemplo:

* indivíduo;
* organização;
* mercado;
* sistema;
* sociedade.

O LLM deve poder representar perspectivas concorrentes sem misturá-las.

---

# 49. Contrafactual e escala

Uma alteração pode produzir efeitos diferentes em:

* microescala;
* mesoescala;
* macroescala.

Portanto:

> consequência local ≠ necessariamente consequência sistêmica.

---

# 50. Contrafactual e emergência

Uma mudança pequena pode produzir resultado desproporcional.

Ou:

uma mudança grande pode produzir pouco efeito.

O modelo deve permanecer aberto a:

* não linearidade;
* limiares;
* efeitos emergentes;
* cascatas;
* dependências de trajetória.

---

# 51. Contrafactual e dependência de trajetória

Sistemas históricos podem depender do caminho percorrido.

Portanto:

> mudar um evento passado pode alterar não apenas um resultado, mas todo o caminho posterior.

O LLM deve evitar tratar o sistema histórico como se fosse uma fotografia estática.

---

# 52. Contrafactual e regimes

Uma alteração pode fazer o sistema entrar em outro regime.

Exemplo:

```text
Regime A
   ↓
intervenção
   ↓
limiar
   ↓
Regime B
```

As relações válidas no regime A podem deixar de valer no regime B.

---

# 53. Contrafactuais concorrentes

O modelo deve poder manter simultaneamente:

```text
Contrafactual A
Contrafactual B
Contrafactual C
```

e comparar:

* premissas;
* mecanismos;
* consequências;
* evidências;
* inconsistências;
* condições necessárias.

Sem obrigação de escolher imediatamente um único mundo.

---

# 54. Critérios de qualidade

Uma análise contrafactual deve buscar:

| Critério        | Pergunta                                         |
| --------------- | ------------------------------------------------ |
| Baseline        | O mundo de referência está claro?                |
| Alteração       | O que mudou?                                     |
| Coerência       | A alteração é consistente?                       |
| Preservação     | O que permaneceu constante?                      |
| Causalidade     | Existe mecanismo plausível?                      |
| Temporalidade   | A sequência temporal é coerente?                 |
| Propagação      | Consequências foram exploradas adequadamente?    |
| Alternativas    | Outros resultados plausíveis foram considerados? |
| Incerteza       | Limitações foram preservadas?                    |
| Descoberta      | Surgiram elementos novos?                        |
| Rastreabilidade | É possível reconstruir a lógica?                 |
| Economicidade   | A profundidade foi proporcional ao valor?        |

---

# 55. Testes cognitivos

## Teste 1 — Baseline

O modelo consegue estabelecer o mundo de referência?

## Teste 2 — Alteração mínima

Consegue modificar apenas a variável solicitada?

## Teste 3 — Propagação

Consegue identificar consequências diretas e indiretas?

## Teste 4 — Temporalidade

Evita inverter causa e consequência?

## Teste 5 — Alternativas

Consegue gerar mais de um mundo quando necessário?

## Teste 6 — Invalidação

Consegue encontrar condições que quebrariam a conclusão?

## Teste 7 — Impossibilidade

Consegue identificar contrafactuais incoerentes?

## Teste 8 — Descoberta

Consegue encontrar uma variável não prevista inicialmente?

## Teste 9 — Robustez

Consegue testar pequenas alterações das premissas?

## Teste 10 — Não fechamento

Consegue produzir um contrafactual que não estava previsto na estrutura inicial?

---

# 56. TESTE FUNDAMENTAL DE NÃO RESTRIÇÃO

A camada falha se o LLM:

> **somente consegue construir contrafactuais previamente previstos pela ontologia, semântica ou modelo causal inicial.**

A camada passa se o LLM consegue:

1. receber um modelo inicial;
2. alterá-lo;
3. descobrir consequências inesperadas;
4. identificar relações não previstas;
5. propor mundos alternativos;
6. questionar premissas;
7. reconstruir o modelo;
8. voltar a explorar.

---

# 57. Antipadrões cognitivos

A camada deve evitar:

### Contrafactual mágico

Alterar X e produzir Y sem mecanismo.

### Mundo completamente diferente

Modificar X e implicitamente alterar tudo.

### Determinismo artificial

Tratar possibilidade como certeza.

### Hindsight

Usar conhecimento posterior como premissa histórica.

### Resultado único

Forçar uma única consequência.

### Explosão combinatória

Criar infinitas ramificações sem utilidade.

### Narrativa pós-fato

Construir uma explicação apenas porque o resultado é conhecido.

### Invariantes imaginários

Assumir que elementos permaneceriam constantes sem justificativa.

### Vazamento entre mundos

Usar informação ou consequência de um mundo em outro.

### Fechamento prematuro

Eliminar alternativas antes de avaliá-las.

---

# 58. Relação com as demais camadas

```text
ONTOLOGIA
    ↓
o que existe
    ↓
SEMÂNTICA
    ↓
o que significa
    ↓
CAUSALIDADE
    ↓
o que produz o quê
    ↓
CONTRAFACTUAL
    ↓
o que ocorreria se fosse diferente
    ↓
INCERTEZA
    ↓
quão limitada é nossa compreensão
    ↓
PROBABILÍSTICA
    ↓
como qualificar possibilidades
    ↓
DECISIONAL
    ↓
o que fazer diante delas
    ↓
METACOGNIÇÃO
    ↓
quão confiável foi o próprio processo
```

A relação não precisa ser linear.

As camadas devem formar um sistema cognitivo recursivo.

---

# 59. Retroalimentação

Um contrafactual pode modificar:

```text
Ontologia
Semântica
Causalidade
Hipóteses
Incertezas
Probabilidades
Decisões
```

Portanto:

> **A camada contrafactual não é apenas consumidora de conhecimento; também pode produzir conhecimento candidato.**

---

# 60. Contrafactual como mecanismo de aprendizagem

Após comparar mundos:

```text
Modelo inicial
      ↓
Contrafactuais
      ↓
resultado inesperado
      ↓
erro/gap descoberto
      ↓
novo conhecimento
      ↓
modelo revisado
```

Isso permite evolução cognitiva.

---

# 61. Conhecimento versus exploração

O LLM deve distinguir:

### Conhecimento estabelecido

Aquilo que possui suporte suficiente.

### Exploração contrafactual

Aquilo que está sendo investigado.

### Hipótese derivada

Possibilidade produzida pela análise.

### Conclusão condicionada

Resultado válido sob determinadas premissas.

Essa separação evita transformar exploração em fato.

---

# 62. Contrafactual como instrumento epistemológico

Perguntar:

> “O que teria que ser diferente para essa afirmação deixar de ser verdadeira?”

é uma forma poderosa de testar conhecimento.

Assim, o contrafactual pode revelar:

* condições necessárias;
* dependências;
* limites;
* exceções;
* fragilidades;
* generalizações indevidas.

---

# 63. Contrafactual e falsificação

Uma hipótese forte deve poder ser submetida a condições que a desafiem.

O LLM deve procurar:

> “Qual mundo alternativo seria incompatível com minha hipótese?”

e:

> “Qual mudança faria minha explicação falhar?”

Isso fortalece a investigação.

---

# 64. Contrafactual e criatividade

A camada também deve permitir exploração criativa.

O LLM pode perguntar:

* “E se a estrutura fosse invertida?”
* “E se uma restrição desaparecesse?”
* “E se um recurso surgisse?”
* “E se o agente tivesse outro objetivo?”
* “E se o mecanismo dominante fosse substituído?”

Desde que diferencie:

**exploração criativa ≠ afirmação factual.**

---

# 65. Princípio da abertura

Nenhum conjunto inicial de contrafactuais deve ser considerado completo.

O LLM deve poder descobrir:

> “Existe outra alteração mais informativa que ainda não foi considerada.”

Essa capacidade é central para evitar pensamento mecânico.

---

# 66. Princípio da suficiência

A análise não precisa explorar todos os mundos possíveis.

Deve explorar aqueles necessários para responder adequadamente à questão.

Isso preserva:

* eficiência;
* eficácia;
* efetividade;
* economicidade.

---

# 67. Princípio da proporcionalidade

Quanto maior:

* impacto;
* risco;
* irreversibilidade;
* incerteza;
* complexidade;

maior pode ser a profundidade contrafactual necessária.

---

# 68. Princípio da soberania cognitiva

A especificação não determina:

> “O LLM deve sempre gerar exatamente cinco contrafactuais.”

Nem:

> “O LLM deve sempre utilizar esta sequência.”

Ela determina:

> **O LLM deve possuir capacidade para explorar alternativas relevantes e escolher autonomamente a profundidade e a forma adequadas ao problema.**

---

# 69. Formulação comportamental

O LLM deve ser capaz de:

> **estabelecer um mundo de referência, identificar condições relevantes, alterar uma ou mais premissas de forma explícita, preservar aquilo que deve permanecer constante, propagar consequências plausíveis, explorar alternativas, testar mecanismos, identificar limites, reconhecer impossibilidades, preservar incertezas, comparar mundos e revisar o modelo quando o contrafactual revelar informações novas.**

---

# 70. Formulação de segurança cognitiva

O LLM deve evitar:

> **apresentar mundos alternativos como fatos, confundir possibilidade com probabilidade, transformar contrafactuais em previsões, alterar implicitamente múltiplas premissas, utilizar conhecimento retrospectivo indevidamente, misturar mundos alternativos ou eliminar possibilidades sem fundamento.**

---

# 71. Formulação de liberdade cognitiva

O LLM deve permanecer livre para:

* criar novas perguntas;
* descobrir novas variáveis;
* propor novas estruturas;
* gerar contrafactuais inesperados;
* questionar o baseline;
* questionar as próprias premissas;
* reconstruir modelos;
* abandonar uma linha contrafactual;
* criar outra mais informativa.

---

# 72. Golden Rule

> **O Harness deve usar o contrafactual para ampliar o espaço cognitivo do LLM, não para predeterminar quais mundos ele pode imaginar.**

---

# 73. Critério máximo

A Camada Contrafactual estará cognitivamente adequada quando o LLM conseguir:

1. distinguir realidade de mundo alternativo;
2. estabelecer um baseline;
3. alterar condições explicitamente;
4. preservar invariantes justificadas;
5. propagar consequências;
6. respeitar temporalidade;
7. distinguir necessário, plausível, possível e especulativo;
8. explorar múltiplos mundos;
9. testar mecanismos causais;
10. encontrar condições de falha;
11. explorar limites;
12. reconhecer contrafactuais incoerentes;
13. evitar hindsight;
14. detectar efeitos de segunda e terceira ordem;
15. reconhecer feedback;
16. identificar mudança de regime;
17. descobrir variáveis não previstas;
18. revisar a própria representação;
19. preservar incerteza;
20. utilizar o contrafactual para melhorar decisões;
21. adaptar a profundidade ao valor cognitivo;
22. abandonar contrafactuais improdutivos;
23. criar contrafactuais novos quando necessário;
24. jamais ficar limitado aos exemplos ou categorias fornecidos pela especificação.

---

# 74. MASTER PRINCIPLE

> **A Camada Contrafactual é a capacidade cognitiva do LLM de explorar mundos alternativos condicionados a alterações explícitas no mundo de referência, preservando coerência, temporalidade, causalidade, incerteza e rastreabilidade, enquanto mantém liberdade para descobrir novas condições, mecanismos, consequências e estruturas não previstas inicialmente.**

---

# 75. Estado esperado

O Harness não deve produzir um LLM que simplesmente:

> “responde perguntas do tipo e se”.

Deve favorecer um LLM capaz de:

> **pensar por mundos alternativos.**

Isso significa utilizar o contrafactual como instrumento de:

* investigação;
* descoberta;
* crítica;
* falsificação;
* causalidade;
* robustez;
* criatividade;
* aprendizagem;
* decisão.

Sem transformar nenhuma dessas funções em um caminho cognitivo obrigatório.
