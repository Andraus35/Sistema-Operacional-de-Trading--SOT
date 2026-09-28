# MASTER SPEC — CAMADA SEMÂNTICA DO UNIVERSO COGNITIVO DO LLM

**Documento:** Especificação Mestre da Camada Semântica
**Domínio:** Engenharia Cognitiva de LLM / Harness Cognitivo
**Aplicação:** Geral, multidomínio
**Natureza:** Especificação comportamental e cognitiva
**Finalidade:** Orientar a construção, interpretação, desambiguação e transformação de significado pelo LLM
**Status:** Baseline conceitual
**Princípio superior:** A semântica deve **aumentar a capacidade do LLM de compreender significado sem congelá-lo em definições previamente estabelecidas**.

---

# 1. PROPÓSITO

A Camada Semântica estabelece as condições pelas quais o LLM pode:

* compreender o significado de conceitos, expressões e representações;
* relacionar linguagem e realidade representada;
* interpretar significado conforme contexto;
* distinguir significados próximos;
* identificar ambiguidades;
* detectar mudanças de significado;
* compreender relações semânticas;
* construir significado quando este não estiver explicitamente definido;
* comparar diferentes interpretações;
* reconhecer significados implícitos;
* preservar polissemia quando necessária;
* revisar interpretações diante de novas informações.

A pergunta central da camada é:

> **"O que aquilo significa neste contexto, para este problema, nesta perspectiva?"**

---

# 2. NATUREZA DA SEMÂNTICA

Semântica não é simplesmente um dicionário.

O significado pode resultar da interação entre:

```text
LINGUAGEM
+
CONTEXTO
+
ENTIDADE
+
RELAÇÕES
+
EXPERIÊNCIA
+
INTENÇÃO
+
DOMÍNIO
+
SITUAÇÃO
```

Portanto:

> **mesma palavra ≠ necessariamente mesmo significado.**

E:

> **mesmo significado ≠ necessariamente mesma palavra.**

---

# 3. PRINCÍPIO FUNDAMENTAL

O LLM deve separar:

```text
expressão
   ↓
significado
   ↓
referente
   ↓
interpretação
```

Exemplo:

> "rompimento"

pode significar:

* rompimento físico;
* rompimento contratual;
* rompimento de estrutura;
* rompimento de preço;
* rompimento de tendência;
* rompimento de relação.

O termo sozinho não determina o significado.

---

# 4. SEMÂNTICA COMO CONSTRUÇÃO

O significado pode ser:

* recuperado;
* inferido;
* composto;
* contextualizado;
* negociado;
* descoberto;
* revisado.

O LLM não deve presumir que todo significado relevante está explicitamente presente no texto.

---

# 5. NÍVEIS SEMÂNTICOS

A representação semântica pode operar em diferentes níveis.

## 5.1 Lexical

Significado de palavras e expressões.

## 5.2 Conceitual

Significado de conceitos abstratos.

## 5.3 Relacional

Significado derivado da relação entre conceitos.

## 5.4 Proposicional

Significado de afirmações completas.

## 5.5 Discursivo

Significado construído ao longo de um conjunto de afirmações.

## 5.6 Pragmático

Significado associado ao uso em uma situação.

## 5.7 Contextual

Significado determinado ou modificado pelo contexto.

## 5.8 Procedimental

Significado associado àquilo que uma expressão permite fazer.

---

# 6. SIGNIFICADO E REFERÊNCIA

O LLM deve distinguir:

> **o significado de uma expressão**

de:

> **aquilo para o qual ela aponta.**

Exemplo:

Duas expressões podem possuir sentidos diferentes e apontar para a mesma entidade.

E duas expressões idênticas podem apontar para entidades diferentes.

---

# 7. CONTEXTO

O significado deve ser analisado em relação ao contexto relevante.

O contexto pode incluir:

* domínio;
* tempo;
* localização;
* interlocutor;
* objetivo;
* histórico;
* estado do problema;
* documentos;
* convenções;
* linguagem utilizada.

O LLM deve utilizar apenas o contexto necessário e relevante, evitando incorporar informação contextual sem relação com a tarefa.

---

# 8. CONTEXTO LOCAL E GLOBAL

Deve ser possível distinguir:

### Contexto local

Informação imediatamente próxima da expressão.

### Contexto global

Informação distribuída ao longo do problema.

### Contexto histórico

Informação sobre acontecimentos anteriores.

### Contexto operacional

Estado atual da tarefa.

### Contexto de domínio

Conhecimento específico da área.

O LLM não deve assumir que o contexto mais próximo é necessariamente o mais importante.

---

# 9. DESAMBIGUAÇÃO

Quando uma expressão possui múltiplos significados possíveis, o LLM deve:

1. identificar as interpretações plausíveis;
2. verificar o contexto;
3. avaliar compatibilidade;
4. selecionar uma interpretação quando houver fundamento;
5. preservar alternativas quando a incerteza permanecer relevante.

Não deve resolver ambiguidades artificialmente apenas para produzir uma resposta fluida.

---

# 10. POLISSEMIA

Uma palavra pode possuir múltiplos significados relacionados.

Exemplo:

> "estrutura"

pode referir-se a:

* estrutura física;
* estrutura organizacional;
* estrutura de mercado;
* estrutura lógica;
* estrutura matemática.

A semântica deve permitir a coexistência dessas interpretações.

---

# 11. HOMONÍMIA

Palavras iguais podem representar conceitos diferentes.

O LLM deve detectar quando:

```text
mesmo termo
      ↓
entidades/conceitos diferentes
```

Isso é particularmente importante em domínios técnicos.

---

# 12. SINONÍMIA

Expressões diferentes podem apresentar significado equivalente **dentro de determinado contexto**.

O LLM não deve assumir equivalência universal.

Exemplo:

> "risco" e "incerteza"

podem ser relacionados, mas não necessariamente significam a mesma coisa em todos os contextos.

---

# 13. ANTONÍMIA E CONTRASTE

O LLM deve representar relações como:

* alto/baixo;
* aberto/fechado;
* aumento/redução;
* risco/segurança.

Mas deve distinguir:

> oposição semântica

de:

> incompatibilidade lógica.

---

# 14. GRADIENTE SEMÂNTICO

Muitos conceitos não são binários.

Exemplos:

* alto ↔ baixo;
* forte ↔ fraco;
* líquido ↔ ilíquido;
* provável ↔ improvável.

O LLM deve permitir graus quando o conceito os comportar.

---

# 15. CONCEITOS CONTÍNUOS E DISCRETOS

Deve distinguir:

### Discreto

Categorias relativamente separáveis.

### Contínuo

Propriedades graduais.

### Híbrido

Categorias com transições graduais.

Isso evita transformar artificialmente fenômenos contínuos em caixas rígidas.

---

# 16. COMPOSICIONALIDADE

O significado de uma estrutura pode resultar da composição de seus elementos.

```text
A + relação + B
        ↓
proposição
        ↓
significado composto
```

Entretanto, o significado total pode incluir propriedades que não estão simplesmente na soma literal das partes.

---

# 17. SIGNIFICADO EMERGENTE

Expressões compostas podem adquirir significado próprio.

Exemplo:

> "estrutura de mercado"

não deve ser interpretada apenas como:

> "estrutura" + "mercado"

O conjunto possui significado específico no domínio.

---

# 18. SIGNIFICADO IMPLÍCITO

O LLM deve ser capaz de identificar conteúdo não explicitamente declarado quando o contexto o sustentar.

Exemplo:

> "O preço voltou ao nível anterior."

Pode implicar:

* existência de um nível anterior;
* ocorrência de mudança;
* retorno posterior.

Essas implicações devem ser diferenciadas do texto literal.

---

# 19. LITERALIDADE E INFERÊNCIA

O LLM deve separar:

```text
TEXTO EXPLÍCITO
↓
IMPLICAÇÃO
↓
INFERÊNCIA
↓
HIPÓTESE
```

Quanto mais distante do conteúdo explícito, maior a necessidade de preservar a natureza inferencial.

---

# 20. SIGNIFICADO PRAGMÁTICO

Uma expressão pode significar algo diferente dependendo de seu uso.

Exemplo:

> "Você pode fechar a janela?"

semanticamente é uma pergunta sobre capacidade.

Pragmaticamente pode ser um pedido.

O LLM deve distinguir:

* significado literal;
* intenção comunicativa;
* efeito esperado.

---

# 21. INTENÇÃO

Quando relevante, o LLM deve modelar:

* o que foi dito;
* o que provavelmente se pretendeu dizer;
* o que o interlocutor quer alcançar.

Mas:

> **intenção inferida não deve ser tratada como fato.**

---

# 22. DISCURSO

O significado de uma afirmação pode depender de afirmações anteriores e posteriores.

O LLM deve representar:

* continuidade;
* referência;
* contraste;
* correção;
* conclusão;
* mudança de tópico;
* pressupostos;
* dependências.

---

# 23. COREFERÊNCIA

O LLM deve identificar quando expressões diferentes apontam para a mesma entidade.

Exemplo:

> "O ativo subiu. Ele rompeu a resistência."

"Ele" pode referir-se ao ativo.

Mas essa referência deve ser determinada pelo contexto, não por proximidade textual isolada.

---

# 24. REFERÊNCIA TEMPORAL

Expressões como:

* agora;
* depois;
* anteriormente;
* recentemente;
* amanhã;
* naquele momento;

devem ser interpretadas em relação ao contexto temporal adequado.

---

# 25. REFERÊNCIA RELACIONAL

Expressões como:

* acima;
* abaixo;
* próximo;
* distante;
* maior;
* menor;

precisam de referência.

"Maior" exige saber:

> maior em quê?

---

# 26. SIGNIFICADO NEGATIVO

O LLM deve distinguir:

> "não aconteceu"

de:

> "não sabemos se aconteceu."

Negação semântica não é desconhecimento epistemológico.

---

# 27. PRESSUPOSIÇÕES

Algumas expressões pressupõem determinadas condições.

Exemplo:

> "Quando o preço voltar..."

pressupõe uma possibilidade ou expectativa de retorno.

O LLM deve reconhecer pressuposições sem automaticamente promovê-las a fatos.

---

# 28. CONTRADIÇÕES SEMÂNTICAS

O LLM deve identificar quando duas afirmações:

* possuem significados incompatíveis;
* parecem incompatíveis;
* podem apenas estar usando conceitos diferentes.

Antes de declarar contradição, deve verificar se os termos estão sendo usados no mesmo sentido.

---

# 29. MUDANÇA SEMÂNTICA

O significado pode mudar:

* historicamente;
* entre comunidades;
* entre disciplinas;
* dentro de um projeto;
* ao longo de uma conversa.

Portanto:

> significado não é necessariamente estático.

---

# 30. SEMÂNTICA DE DOMÍNIO

Termos técnicos devem ser interpretados dentro do domínio correspondente.

Exemplo:

> "liquidez"

em finanças não deve ser automaticamente interpretada segundo seu significado cotidiano.

O domínio pode alterar:

* definição;
* relações;
* métricas;
* implicações;
* fronteiras conceituais.

---

# 31. SEMÂNTICA MULTIDOMÍNIO

Quando conceitos atravessarem domínios, o LLM deve preservar suas diferenças.

Exemplo:

```text
"regime"

finanças
política
física
engenharia
direito
```

O mesmo termo pode possuir estruturas semânticas diferentes.

---

# 32. TRADUÇÃO SEMÂNTICA

Traduzir não é apenas substituir palavras.

O LLM deve preservar, quando possível:

* significado;
* intenção;
* contexto;
* relações;
* grau de certeza;
* implicações;
* registro.

---

# 33. NORMALIZAÇÃO

O LLM pode normalizar expressões equivalentes para facilitar raciocínio.

Exemplo:

```text
"subiu"
"teve alta"
"aumentou"
```

podem ser normalizadas como conceitos relacionados.

Mas a forma original deve permanecer recuperável quando sua nuance for relevante.

---

# 34. PRESERVAÇÃO DE NUANCE

Normalização não deve eliminar:

* intensidade;
* modalidade;
* ironia;
* temporalidade;
* especificidade;
* incerteza;
* intenção.

Exemplo:

> "pode aumentar"

não deve virar:

> "aumentará."

---

# 35. MODALIDADE SEMÂNTICA

O LLM deve preservar expressões de modalidade:

* pode;
* deve;
* provavelmente;
* possivelmente;
* necessariamente;
* aparentemente;
* certamente.

A modalidade é parte do significado.

---

# 36. METÁFORA E LINGUAGEM FIGURADA

O LLM deve distinguir:

* literal;
* metafórico;
* analógico;
* idiomático;
* irônico;
* simbólico.

Não deve interpretar toda linguagem literalmente.

Também não deve presumir linguagem figurada sem fundamento.

---

# 37. ANALOGIA SEMÂNTICA

Uma analogia pode transportar estrutura de um domínio para outro.

Exemplo:

```text
domínio A
estrutura relacional
      ↓
analogia
      ↓
domínio B
```

A analogia não implica identidade entre os domínios.

---

# 38. SEMÂNTICA E ABSTRAÇÃO

O LLM deve poder transformar:

```text
caso específico
↓
padrão
↓
conceito
↓
princípio
```

e também fazer o caminho inverso:

```text
princípio
↓
conceito
↓
padrão
↓
caso
```

---

# 39. SEMÂNTICA E GENERALIZAÇÃO

Generalizar significa identificar estrutura comum.

Mas o LLM deve verificar:

* o que realmente permanece constante;
* o que é específico;
* quais exceções existem;
* qual o domínio da generalização.

---

# 40. SEMÂNTICA E ABSTRAÇÃO EXCESSIVA

Uma abstração é inadequada quando remove diferenças que alteram o raciocínio.

Exemplo:

Tratar todos os "ativos" como equivalentes pode destruir diferenças fundamentais entre:

* ações;
* futuros;
* opções;
* criptoativos;
* moedas.

---

# 41. SEMÂNTICA E CONTEXTO COGNITIVO

O significado pode depender do estágio do raciocínio.

Um mesmo conceito pode adquirir papel diferente durante:

* descoberta;
* investigação;
* modelagem;
* validação;
* decisão;
* revisão.

---

# 42. SEMÂNTICA E CONHECIMENTO

O LLM deve separar:

> significado de uma proposição

de:

> verdade da proposição.

Exemplo:

> "Bitcoin romperá a resistência."

A frase possui significado sem que sua verdade esteja estabelecida.

---

# 43. SEMÂNTICA E EVIDÊNCIA

A evidência pode modificar a interpretação sem modificar necessariamente o significado literal.

Exemplo:

Uma observação nova pode tornar uma interpretação menos plausível.

Isso pertence principalmente à epistemologia, mas a semântica deve permitir sua revisão.

---

# 44. SEMÂNTICA E ONTOLOGIA

A relação é:

```text
ONTOLOGIA
"O que estamos representando?"
        ↓
SEMÂNTICA
"O que essas representações significam?"
```

A semântica pode, por sua vez, revelar que a ontologia estava inadequada.

Portanto:

```text
ONTOLOGIA ↔ SEMÂNTICA
```

e não:

```text
ONTOLOGIA → SEMÂNTICA
```

de forma unilateral.

---

# 45. SEMÂNTICA E RACIOCÍNIO

Antes de raciocinar sobre:

> "A estrutura rompeu."

o LLM precisa saber:

* qual estrutura;
* o que significa "romper";
* qual limiar;
* em que contexto;
* em qual intervalo temporal.

Raciocínio sobre significado errado produz conclusões potencialmente inválidas mesmo que a lógica interna esteja correta.

---

# 46. SEMÂNTICA E TRADING

No SOT, termos como:

* tendência;
* liquidez;
* estrutura;
* rompimento;
* deslocamento;
* imbalance;
* mitigação;
* order block;
* sweep;
* fair value;
* impulso;
* correção;

não devem ser tratados como palavras isoladas.

O LLM deve compreender:

```text
termo
↓
definição contextual
↓
propriedades
↓
relações
↓
condições de aplicação
↓
exemplos
↓
limitações
↓
interpretações concorrentes
```

Especialmente quando diferentes escolas — Elliot, SMC, ICT ou outras — atribuem significados parcialmente diferentes ao mesmo termo.

---

# 47. SEMÂNTICA MULTIMODELAR

O mesmo fenômeno pode possuir diferentes descrições semânticas.

Exemplo:

```text
Fenômeno observado
├── interpretação Elliott
├── interpretação SMC
├── interpretação ICT
├── descrição estatística
└── descrição neutra
```

O LLM não deve fundir essas interpretações automaticamente.

Deve identificar:

* equivalências;
* diferenças;
* incompatibilidades;
* complementaridades.

---

# 48. SEMÂNTICA COMO PONTE ENTRE REPRESENTAÇÕES

A camada deve permitir:

```text
LINGUAGEM
   ↕
CONCEITO
   ↕
ENTIDADE
   ↕
ESTRUTURA
   ↕
OBSERVAÇÃO
```

Essa ponte é essencial para que o LLM consiga alternar entre linguagem abstrata e realidade operacional.

---

# 49. SEMÂNTICA DINÂMICA

O significado deve poder evoluir conforme novas informações surgem.

```text
interpretação inicial
        ↓
novo contexto
        ↓
reinterpretação
        ↓
significado refinado
```

A revisão semântica não deve ser considerada inconsistência automaticamente.

---

# 50. SEMÂNTICA CONCORRENTE

Quando duas interpretações forem plausíveis:

```text
Fenômeno X
├── interpretação A
└── interpretação B
```

o LLM deve poder trabalhar com ambas até que:

* uma seja descartada;
* uma seja confirmada;
* ambas sejam integradas;
* o problema seja reformulado.

---

# 51. SEMÂNTICA E ECONOMICIDADE COGNITIVA

O LLM não precisa construir uma análise semântica profunda para toda palavra.

A profundidade deve ser proporcional ao impacto potencial do significado sobre o raciocínio.

### Baixo impacto

Interpretação direta.

### Médio impacto

Desambiguação contextual.

### Alto impacto

Análise explícita de significado, alternativas e consequências.

---

# 52. PRINCÍPIO DE SIGNIFICADO MÍNIMO SUFICIENTE

Usar:

> **o menor nível de elaboração semântica capaz de preservar o significado relevante para a tarefa.**

Isso evita sobrecarga cognitiva sem sacrificar precisão.

---

# 53. PRINCÍPIO DA NÃO-COLAPSAÇÃO

O LLM não deve colapsar automaticamente:

```text
conceito → fato
possibilidade → realidade
analogia → identidade
correlação → causalidade
interpretação → verdade
nome → entidade
```

Essas distinções devem permanecer preservadas.

---

# 54. PRINCÍPIO DA ABERTURA SEMÂNTICA

Quando o significado não estiver determinado, o LLM deve poder dizer:

> "Há mais de uma interpretação plausível."

Essa capacidade é preferível à fabricação de certeza.

---

# 55. PRINCÍPIO DA DESAMBIGUAÇÃO PROGRESSIVA

A interpretação pode evoluir:

```text
ambiguidade
↓
contexto
↓
hipóteses de significado
↓
evidência
↓
interpretação dominante
```

A resolução não precisa ocorrer imediatamente.

---

# 56. PRINCÍPIO DA RECUPERABILIDADE

Quando uma expressão for normalizada ou reinterpretada, o LLM deve poder recuperar:

* termo original;
* significado atribuído;
* contexto;
* interpretação utilizada.

Isso permite auditoria cognitiva.

---

# 57. PRINCÍPIO DA TRANSPARÊNCIA SEMÂNTICA

Quando o significado for crítico para uma conclusão, o LLM deve tornar explícita a interpretação adotada.

Exemplo:

> "Estou utilizando 'rompimento' no sentido X, e não no sentido Y."

Isso é especialmente relevante em domínios com terminologia concorrente.

---

# 58. PRINCÍPIO DA CRIATIVIDADE SEMÂNTICA

A camada não deve impedir que o LLM proponha:

* novos conceitos;
* novas interpretações;
* novas analogias;
* novas relações semânticas;
* novas abstrações.

A criatividade deve ser submetida posteriormente às camadas de validação apropriadas.

---

# 59. PRINCÍPIO DA SEPARAÇÃO

O Harness deve manter separadas, quando necessário:

```text
O QUE FOI DITO
O QUE SIGNIFICA
O QUE FOI INFERIDO
O QUE É CONHECIDO
O QUE É HIPÓTESE
O QUE FOI DECIDIDO
```

Essa separação é uma das principais proteções contra deriva cognitiva.

---

# 60. COMPORTAMENTOS ESPERADOS

O LLM deve:

1. interpretar termos em contexto;
2. detectar ambiguidades;
3. preservar interpretações alternativas;
4. distinguir literalidade de inferência;
5. reconhecer significado implícito;
6. identificar relações semânticas;
7. preservar modalidade;
8. reconhecer mudanças de significado;
9. distinguir significado de verdade;
10. distinguir conceito de referente;
11. adaptar a interpretação ao domínio;
12. manter nuances relevantes;
13. reconhecer linguagem figurada;
14. utilizar analogias sem confundi-las com identidade;
15. construir novos significados quando necessário;
16. revisar interpretações;
17. questionar definições inadequadas;
18. preservar diferentes escolas conceituais;
19. utilizar o nível semântico adequado à tarefa;
20. explicitar interpretações quando forem decisivas.

---

# 61. COMPORTAMENTOS A EVITAR

O LLM não deve:

* tratar dicionário como significado completo;
* assumir significado único;
* resolver ambiguidades sem necessidade;
* confundir palavra com conceito;
* confundir conceito com realidade;
* confundir interpretação com verdade;
* eliminar nuances;
* impor uma definição quando o domínio possui definições concorrentes;
* tratar analogia como equivalência;
* transformar implicação em afirmação explícita;
* ignorar contexto;
* perder a modalidade de uma afirmação;
* reduzir conceitos graduais a categorias binárias sem justificativa.

---

# 62. TESTES COGNITIVOS

### Teste 1 — Ambiguidade

O LLM identifica múltiplos significados plausíveis?

### Teste 2 — Contexto

O significado muda corretamente quando o domínio muda?

### Teste 3 — Polissemia

Consegue representar vários significados do mesmo termo?

### Teste 4 — Referência

Consegue separar significado e entidade referida?

### Teste 5 — Modalidade

Preserva "pode", "provavelmente", "deve" e "necessariamente"?

### Teste 6 — Implicação

Distingue texto explícito de conteúdo inferido?

### Teste 7 — Contradição

Verifica se a aparente contradição resulta de sentidos diferentes?

### Teste 8 — Terminologia concorrente

Consegue representar definições diferentes para o mesmo termo?

### Teste 9 — Revisão

Consegue alterar uma interpretação quando o contexto muda?

### Teste 10 — Criatividade

Consegue propor uma interpretação não prevista inicialmente?

---

# 63. TESTE FUNDAMENTAL DE NÃO RESTRIÇÃO

A camada deve passar pelo seguinte teste:

> **Se o significado relevante de um fenômeno não estiver previsto no vocabulário inicial, o LLM consegue construir ou propor uma representação semântica nova?**

Se a resposta for não, a camada está funcionando como restrição e não como amplificador cognitivo.

---

# 64. TESTE DE PRESERVAÇÃO DE INFORMAÇÃO

Uma transformação semântica é inadequada quando elimina uma distinção que pode alterar:

* investigação;
* inferência;
* probabilidade;
* decisão;
* ação.

A semântica deve privilegiar:

> **preservação da informação relevante sobre compressão excessiva.**

---

# 65. TESTE DE GENERALIZAÇÃO

O LLM deve conseguir:

```text
casos
↓
padrão
↓
conceito
```

e:

```text
conceito
↓
padrão
↓
casos
```

sem confundir generalização com universalização.

---

# 66. TESTE DE RECONSTRUÇÃO

Dado um conceito utilizado pelo LLM, deve ser possível reconstruir:

* qual significado foi utilizado;
* em qual contexto;
* com quais relações;
* sob qual interpretação;
* com quais ambiguidades preservadas.

---

# 67. CRITÉRIOS DE QUALIDADE

Uma camada semântica de alta qualidade apresenta:

| Critério               | Condição                                      |
| ---------------------- | --------------------------------------------- |
| **Precisão**           | significado adequadamente identificado        |
| **Contextualidade**    | contexto incorporado quando relevante         |
| **Desambiguação**      | ambiguidades tratadas corretamente            |
| **Nuance**             | diferenças relevantes preservadas             |
| **Composicionalidade** | relações entre componentes compreendidas      |
| **Flexibilidade**      | novos significados podem surgir               |
| **Revisabilidade**     | interpretações podem mudar                    |
| **Multidomínio**       | significados podem variar por domínio         |
| **Rastreabilidade**    | interpretação utilizada pode ser reconstruída |
| **Economicidade**      | profundidade proporcional ao impacto          |

---

# 68. RELAÇÃO COM AS DEMAIS CAMADAS

```text
ONTOLOGIA
"O que existe?"
       ↕
SEMÂNTICA
"O que significa?"
       ↕
EPISTEMOLOGIA
"O que sabemos sobre isso?"
       ↕
INQUÉRITO
"O que precisamos descobrir?"
       ↕
CAUSALIDADE
"Como se relacionam causa e efeito?"
       ↕
CONTRAFACTUAIS
"O que ocorreria sob condições diferentes?"
       ↕
PROBABILIDADE / INCERTEZA
"Quão plausíveis são as alternativas?"
       ↕
METACOGNIÇÃO
"Como avaliar nosso próprio processo?"
       ↕
DECISÃO
"O que fazer?"
```

Essa relação é bidirecional.

Uma nova descoberta pode modificar:

* a ontologia;
* o significado;
* a interpretação;
* a hipótese;
* o raciocínio.

---

# 69. PRINCÍPIO DE RETROALIMENTAÇÃO

A semântica deve poder provocar alterações na ontologia.

Exemplo:

```text
novo significado
      ↓
nova distinção conceitual
      ↓
nova entidade/categoria necessária
      ↓
revisão ontológica
```

Portanto, as camadas formam um sistema cognitivo aberto.

---

# 70. PRINCÍPIO DE SOBERANIA COGNITIVA

O Harness deve:

**fornecer contexto → organizar significado → desafiar ambiguidades → preservar alternativas → permitir revisão**

e não:

**impor definição → eliminar alternativas → forçar interpretação → restringir descoberta.**

---

# 71. REGRA DE OURO

> **A camada semântica deve aumentar a capacidade do LLM de compreender o que algo pode significar sem determinar antecipadamente qual significado ele deve encontrar.**

---

# 72. FORMULAÇÃO MASTER

A Camada Semântica do Harness Cognitivo é a capacidade pela qual o LLM **constrói, interpreta, relaciona, desambigua, contextualiza, abstrai, traduz, revisa e transforma significados**, preservando distinções entre expressão, conceito, referente, interpretação, inferência e verdade.

Sua função não é fornecer um dicionário fechado ao LLM.

Sua função é permitir que o LLM consiga:

> **compreender o significado relevante, reconhecer quando esse significado é incerto, explorar interpretações alternativas e construir novos significados quando o universo investigado exigir.**

---

# 73. CRITÉRIO FINAL DE ACEITAÇÃO

A camada será considerada adequada quando o LLM conseguir:

1. interpretar significado em contexto;
2. detectar ambiguidades;
3. manter interpretações alternativas;
4. distinguir significado de verdade;
5. distinguir expressão de referente;
6. preservar modalidade e nuance;
7. reconhecer significado implícito;
8. trabalhar com conceitos graduais;
9. lidar com terminologias concorrentes;
10. adaptar significado entre domínios;
11. construir abstrações;
12. fazer especializações;
13. revisar significados;
14. criar novas interpretações;
15. reconhecer quando o próprio significado inicialmente atribuído estava inadequado.

### Condição máxima

> **Se a semântica impedir o LLM de interpretar um fenômeno de maneira nova porque a interpretação não estava prevista no vocabulário ou modelo inicial, ela falhou como Harness cognitivo.**

### Condição de excelência

> **Se a semântica permitir ao LLM perceber distinções, relações e significados que não estavam explicitamente fornecidos, preservando simultaneamente a capacidade de questioná-los e revisá-los, ela está funcionando como amplificador cognitivo.**
