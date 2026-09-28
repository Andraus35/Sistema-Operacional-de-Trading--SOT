# MASTER DOCUMENTO

## ESPECIFICAÇÃO DA CAMADA METACOGNIÇÃO PARA HARNESSES COGNITIVOS DE LLM

**Identificação:** MC-001
**Camada:** Metacognição
**Natureza:** Especificação cognitiva
**Aplicabilidade:** Harnesses cognitivos de LLM e sistemas agênticos
**Status:** Master Specification
**Escopo:** Transversal
**Princípio fundamental:** liberdade cognitiva + obrigação de satisfazer invariantes
**Dependência conceitual:** Ontologia + Semântica + Causalidade + Contrafactuais + Incerteza + Decisional
**Não objetivo:** produzir software, algoritmo fechado, checklist cognitivo ou sequência obrigatória de raciocínio

---

# 1. Propósito

A Camada de Metacognição especifica a capacidade de um LLM ou sistema cognitivo de:

* observar o próprio processo cognitivo;
* avaliar a qualidade desse processo;
* reconhecer limitações;
* detectar erros, contradições e fragilidades;
* identificar pressupostos;
* reconhecer mudanças de contexto;
* avaliar a adequação dos modelos utilizados;
* monitorar sua própria confiança;
* revisar interpretações;
* detectar possíveis vieses;
* reconhecer quando uma conclusão não é suficientemente sustentada;
* decidir quando aprofundar uma investigação;
* reconhecer quando precisa mudar de abordagem;
* aprender com resultados e erros;
* reformular seu próprio processo de análise.

A metacognição não deve controlar previamente **o que o LLM deve pensar**.

Ela deve ampliar sua capacidade de perceber **como está pensando, sobre o que está pensando, com quais limitações e com que qualidade**.

---

# 2. Princípio central

> **O Harness não deve determinar o pensamento do LLM; deve tornar o LLM mais capaz de observar, questionar, avaliar e melhorar o próprio pensamento.**

A metacognição é, portanto, uma camada de **auto-observação e autorregulação cognitiva**, não um mecanismo de substituição da cognição.

---

# 3. Problema que a camada resolve

LLMs podem produzir respostas cognitivamente sofisticadas sem necessariamente:

* perceber que estão utilizando uma premissa inadequada;
* distinguir conhecimento de inferência;
* perceber que uma hipótese foi assumida como fato;
* reconhecer que estão excessivamente confiantes;
* detectar que duas evidências são dependentes;
* perceber mudança de contexto;
* identificar que um modelo não explica adequadamente a observação;
* reconhecer que estão buscando confirmação;
* perceber que estão racionalizando uma conclusão já escolhida;
* identificar informação ausente relevante;
* perceber que uma interpretação depende excessivamente de uma única representação;
* reconhecer quando a própria pergunta está mal formulada.

A metacognição cria condições para que o sistema possa detectar essas situações.

---

# 4. O que é metacognição

Para esta especificação:

> **Metacognição é a capacidade de representar, monitorar, avaliar, questionar e modificar aspectos do próprio processo cognitivo.**

Ela possui pelo menos duas dimensões:

### 4.1 Conhecimento metacognitivo

O sistema sabe algo sobre:

* seus próprios limites;
* seus métodos;
* seus modelos;
* suas fontes;
* seus graus de incerteza;
* suas estratégias cognitivas;
* suas possíveis falhas.

### 4.2 Regulação metacognitiva

O sistema pode:

* interromper;
* revisar;
* aprofundar;
* buscar evidências;
* mudar de modelo;
* reformular;
* comparar abordagens;
* reconhecer insuficiência;
* reduzir confiança;
* aumentar investigação;
* abandonar uma hipótese;
* gerar nova hipótese.

---

# 5. Metacognição não é introspecção perfeita

O Harness não deve pressupor que o LLM tenha acesso perfeito aos mecanismos internos que produziram determinada resposta.

Portanto:

> **Relato do próprio processo não deve ser tratado automaticamente como descrição literal do processo causal interno que produziu a resposta.**

O sistema pode produzir uma reconstrução útil do seu raciocínio sem que essa reconstrução constitua uma observação direta de todos os mecanismos internos.

---

# 6. Metacognição não é cadeia de pensamento obrigatória

Esta especificação não exige:

* exposição integral do raciocínio interno;
* sequência fixa de pensamentos;
* número mínimo de etapas;
* checklist obrigatório;
* justificativa extensa para toda resposta;
* estrutura única de raciocínio.

O Harness deve especificar **propriedades cognitivas desejáveis**, não uma forma única de pensar.

---

# 7. Objeto da metacognição

A metacognição pode observar qualquer elemento relevante do processo cognitivo, incluindo:

* problema;
* pergunta;
* objetivo;
* contexto;
* representação;
* conceitos;
* evidências;
* fontes;
* hipóteses;
* modelos;
* inferências;
* relações causais;
* contrafactuais;
* cenários;
* incertezas;
* probabilidades;
* alternativas;
* decisões;
* previsões;
* resultados;
* erros;
* estratégias;
* pressupostos;
* critérios;
* limitações.

---

# 8. Unidade metacognitiva

Uma unidade metacognitiva pode ser representada conceitualmente como:

**Objeto cognitivo → Processo utilizado → Premissas → Evidências → Resultado → Limitações → Avaliação → Possível revisão**

Essa representação é uma estrutura de referência, não um formato obrigatório de processamento.

---

# 9. Pergunta fundamental da camada

A pergunta central da metacognição é:

> **“Quão adequado é o meu próprio processo cognitivo para este problema, contexto e objetivo?”**

Não:

> “Minha resposta está certa?”

Porque uma resposta correta pode ter sido obtida por um processo frágil, e uma resposta incorreta pode resultar de um processo razoável diante de informação insuficiente.

---

# 10. Processo cognitivo versus resultado

A camada deve distinguir:

**Qualidade do processo**

de

**Qualidade do resultado.**

Uma análise pode produzir resultado correto por acaso.

Uma análise pode produzir resultado incorreto apesar de possuir:

* boas evidências;
* premissas razoáveis;
* modelo adequado;
* incerteza corretamente reconhecida.

Essa distinção é fundamental para aprendizagem.

---

# 11. Estado cognitivo

O sistema deve ser capaz de reconhecer, quando relevante, seu estado cognitivo atual.

Exemplos:

* informação insuficiente;
* hipótese inicial;
* análise exploratória;
* análise convergente;
* conflito entre modelos;
* alta incerteza;
* baixa observabilidade;
* evidência contraditória;
* conclusão provisória;
* conclusão robusta;
* necessidade de investigação;
* necessidade de revisão.

Esses estados não constituem estados obrigatórios nem uma máquina de estados fechada.

---

# 12. Monitoramento cognitivo

A metacognição deve permitir monitorar:

* o que está sendo assumido;
* o que está sendo observado;
* o que está sendo inferido;
* quais modelos estão sendo utilizados;
* quais evidências sustentam cada conclusão;
* onde existe incerteza;
* onde existe dependência entre evidências;
* onde existem conflitos;
* quais alternativas foram consideradas;
* quais alternativas podem ter sido ignoradas.

---

# 13. Autoavaliação

O sistema deve poder avaliar criticamente sua própria análise.

Essa avaliação pode considerar:

* coerência;
* suficiência;
* consistência;
* cobertura;
* evidência;
* robustez;
* sensibilidade;
* dependência;
* incerteza;
* adequação do modelo;
* adequação contextual;
* qualidade da inferência;
* possibilidade de explicações alternativas.

Não deve existir uma métrica única universal de “qualidade cognitiva”.

---

# 14. Autocrítica

A autocrítica deve procurar fragilidades reais.

Ela pode perguntar, quando pertinente:

* O que estou assumindo?
* O que poderia estar errado?
* Qual evidência contradiz minha conclusão?
* Estou confundindo observação com interpretação?
* Estou utilizando um modelo fora de seu domínio?
* Existe outra explicação?
* Estou ignorando alguma variável?
* Minha confiança é proporcional às evidências?
* Minha conclusão depende excessivamente de uma premissa?
* Existe alguma informação que mudaria materialmente a conclusão?

Essas perguntas são **capacidades disponíveis**, não perguntas que precisam ser repetidas sempre.

---

# 15. Descoberta de pressupostos

O sistema deve possuir capacidade de identificar:

* premissas explícitas;
* premissas implícitas;
* premissas herdadas;
* premissas contextuais;
* premissas temporais;
* premissas causais;
* premissas semânticas;
* premissas ontológicas;
* premissas sobre dados;
* premissas sobre modelos.

Uma premissa descoberta pode ser:

* mantida;
* revisada;
* contestada;
* substituída;
* removida.

---

# 16. Monitoramento de dependências

O sistema deve ser capaz de perceber quando conclusões diferentes dependem da mesma premissa.

Isso evita a aparência de múltiplas confirmações independentes.

Exemplo conceitual:

**Evidência A → Premissa X → Conclusão**

**Evidência B → Premissa X → Conclusão**

A e B podem parecer duas evidências, mas podem possuir dependência estrutural.

A metacognição deve ser capaz de detectar essa possibilidade.

---

# 17. Monitoramento de circularidade

O sistema deve detectar raciocínios potencialmente circulares.

Exemplo:

> “A hipótese é verdadeira porque o comportamento confirma a hipótese.”

A metacognição deve questionar:

* qual observação independente sustenta a hipótese;
* se o critério de confirmação foi definido pela própria hipótese;
* se a evidência realmente possui poder discriminativo.

---

# 18. Monitoramento de confirmação

A camada deve permitir detectar possíveis padrões de:

* busca seletiva de evidências;
* valorização excessiva de evidências favoráveis;
* descarte de evidências contrárias;
* interpretação assimétrica;
* seleção retrospectiva;
* racionalização posterior.

Não deve presumir que toda convergência seja confirmação enviesada.

O sistema deve avaliar a possibilidade, não acusar automaticamente o próprio raciocínio.

---

# 19. Monitoramento de ancoragem

O sistema deve poder perceber quando uma interpretação inicial está influenciando excessivamente interpretações posteriores.

A âncora pode ser:

* hipótese inicial;
* primeira interpretação;
* primeira fonte;
* primeiro padrão identificado;
* modelo conhecido;
* conclusão anterior.

A metacognição deve permitir reabrir o espaço cognitivo quando a âncora estiver comprometendo a análise.

---

# 20. Monitoramento de excesso de confiança

O sistema deve distinguir:

**força da evidência**

de

**força da confiança.**

Confiança elevada deve ser compatível com:

* qualidade das evidências;
* independência das evidências;
* estabilidade do modelo;
* adequação contextual;
* quantidade de informação;
* grau de incerteza;
* existência de alternativas.

---

# 21. Monitoramento de falsa humildade

A metacognição também deve detectar o problema inverso.

Não deve transformar qualquer incerteza em:

> “Não é possível saber.”

O sistema deve distinguir:

* desconhecido;
* incerto;
* parcialmente observável;
* estimável;
* provável;
* impossível;
* indeterminado.

Reconhecer limites não significa abandonar a análise.

---

# 22. Monitoramento de ambiguidade

O sistema deve detectar quando:

* o termo é ambíguo;
* o problema possui múltiplas interpretações;
* o objetivo não está claro;
* existem diferentes modelos semânticos;
* uma mesma observação admite múltiplas representações.

Quando possível, deve manter as interpretações concorrentes até que exista razão para resolver a ambiguidade.

---

# 23. Monitoramento de modelo

O sistema deve ser capaz de perguntar:

> **“O modelo que estou usando é adequado para este problema?”**

Isso inclui:

* domínio de validade;
* escala;
* contexto;
* horizonte;
* regime;
* premissas;
* limitações;
* evidências que sustentam o modelo.

Um modelo útil em determinado contexto não deve ser tratado como universal.

---

# 24. Reconhecimento de inadequação do modelo

Uma das capacidades mais importantes é reconhecer:

> **“O problema pode não estar sendo mal resolvido; pode estar sendo representado pelo modelo errado.”**

Nesse caso, o sistema pode:

* modificar o modelo;
* combinar modelos;
* comparar modelos;
* abandonar o modelo;
* criar nova representação;
* buscar novas evidências.

---

# 25. Metacognição e Ontologia

A metacognição deve poder questionar a própria representação do universo.

Exemplos:

* uma entidade pode ter sido omitida;
* duas entidades podem ter sido indevidamente fundidas;
* uma relação pode ter sido criada sem fundamento;
* uma categoria pode ser inadequada;
* o nível de granularidade pode estar errado.

Portanto:

> **A metacognição pode revisar a ontologia utilizada pela própria cognição.**

---

# 26. Metacognição e Semântica

O sistema deve poder perceber:

* ambiguidade terminológica;
* mudança de significado;
* interpretação dependente do contexto;
* uso inadequado de conceito;
* tradução semântica defeituosa;
* confusão entre expressão e significado.

Uma conclusão aparentemente lógica pode estar errada porque o significado utilizado estava errado.

---

# 27. Metacognição e Causalidade

A camada deve questionar:

* se existe realmente causalidade;
* se há apenas associação;
* se existe confundimento;
* se a direção causal foi assumida;
* se o mecanismo foi demonstrado ou apenas narrado;
* se existe explicação causal alternativa.

Especialmente importante:

> **Uma narrativa causal coerente não é automaticamente uma causalidade demonstrada.**

---

# 28. Metacognição e Contrafactuais

O sistema pode utilizar contrafactuais para testar a própria análise.

Exemplo conceitual:

> “Se minha hipótese fosse falsa, o que eu esperaria observar?”

Ou:

> “Se esta variável não existisse, minha conclusão continuaria válida?”

O contrafactual torna-se instrumento de autocrítica.

---

# 29. Metacognição e Incerteza

A metacognição deve localizar:

* onde está a incerteza;
* por que ela existe;
* quanto ela importa;
* se pode ser reduzida;
* se altera a conclusão;
* se é estrutural.

Não deve apenas produzir uma declaração genérica de incerteza.

---

# 30. Metacognição e Decisão

Antes de uma decisão, a camada pode avaliar:

* qualidade das informações;
* alternativas consideradas;
* premissas;
* consequências;
* riscos;
* incertezas;
* reversibilidade;
* condições de invalidação;
* necessidade de informação adicional.

Mas não deve substituir a camada decisional.

---

# 31. Metacognição como camada transversal

A metacognição não deve funcionar apenas ao final.

Ela pode atuar:

**antes**

→ preparando a investigação;

**durante**

→ monitorando a análise;

**depois**

→ avaliando o resultado;

**posteriormente**

→ aprendendo com o resultado.

---

# 32. Metacognição prospectiva

Antes de iniciar uma análise, o sistema pode avaliar:

* qual é o problema;
* qual é o objetivo;
* quais informações existem;
* quais informações estão ausentes;
* quais modelos parecem pertinentes;
* quais riscos cognitivos podem surgir;
* quais ambiguidades precisam ser resolvidas.

---

# 33. Metacognição online

Durante a análise, o sistema pode perceber:

* contradições;
* mudança de contexto;
* novas evidências;
* inadequação de modelo;
* hipótese enfraquecida;
* hipótese alternativa;
* necessidade de aprofundamento.

---

# 34. Metacognição retrospectiva

Após a análise, o sistema pode perguntar:

* o que funcionou;
* o que falhou;
* qual premissa estava errada;
* qual evidência foi supervalorizada;
* qual alternativa foi ignorada;
* onde a confiança estava mal calibrada.

---

# 35. Metacognição adaptativa

A camada deve permitir alterar a própria estratégia cognitiva em resposta ao contexto.

Por exemplo:

**problema simples**

→ menor profundidade;

**problema ambíguo**

→ maior exploração semântica;

**problema de alto impacto**

→ maior investigação e validação;

**evidência conflitante**

→ comparação de hipóteses;

**modelo inadequado**

→ reformulação.

Isso é proporcionalidade cognitiva.

---

# 36. Controle adaptativo de profundidade

A profundidade da análise deve ser determinada pela necessidade cognitiva, não por uma quantidade fixa de etapas.

Fatores possíveis:

* complexidade;
* impacto;
* incerteza;
* novidade;
* conflito;
* risco;
* reversibilidade;
* valor da informação;
* custo cognitivo.

---

# 37. Metacognição e economicidade

A metacognição também deve perguntar:

> **“Mais análise realmente melhora a decisão ou apenas aumenta o custo?”**

Isso evita:

* análise infinita;
* busca indiscriminada;
* excesso de validação;
* complexidade sem benefício.

A profundidade deve ser proporcional ao valor esperado da informação.

---

# 38. Valor da informação

A camada deve ser capaz de reconhecer quando uma informação adicional pode:

* alterar uma hipótese;
* alterar uma decisão;
* reduzir uma incerteza crítica;
* distinguir modelos concorrentes;
* detectar uma condição de invalidação.

Quando uma nova informação dificilmente alteraria o resultado, sua aquisição pode possuir baixo valor.

---

# 39. Metacognição e novidade

A camada não deve tratar novidade automaticamente como erro.

Uma observação que não se encaixa no modelo pode indicar:

* erro de observação;
* erro de interpretação;
* erro do modelo;
* nova variável;
* novo fenômeno;
* nova relação;
* nova categoria ontológica.

A metacognição deve manter essas possibilidades abertas.

---

# 40. Erro como informação

Um erro detectado não deve ser apenas corrigido.

Quando relevante, deve ser utilizado para descobrir:

* falha de premissa;
* falha de modelo;
* falha de processo;
* lacuna de conhecimento;
* limite de generalização;
* mudança de contexto.

---

# 41. Falha de processo versus falha de resultado

O sistema deve diferenciar:

### Falha de resultado

A conclusão não corresponde ao resultado observado.

### Falha de processo

O processo apresentou fragilidade independentemente do resultado.

### Falha de modelo

A representação utilizada era inadequada.

### Falha de informação

A informação disponível era insuficiente ou incorreta.

### Falha contextual

O conhecimento era válido em outro contexto.

---

# 42. Resultado inesperado

Quando ocorre resultado inesperado, a primeira resposta não deve ser necessariamente:

> “A hipótese estava errada.”

Deve ser possível investigar:

* observação;
* dados;
* interpretação;
* hipótese;
* mecanismo;
* contexto;
* regime;
* modelo;
* execução;
* aleatoriedade;
* evento externo.

---

# 43. Aprendizagem metacognitiva

A aprendizagem deve produzir conhecimento sobre:

* quais modelos funcionam em quais contextos;
* quais estratégias falham;
* quais tipos de evidência são confiáveis;
* quais padrões induzem erro;
* quais limitações são recorrentes.

Aprender não significa apenas memorizar resultados.

---

# 44. Aprendizagem sem superstição

O sistema não deve inferir automaticamente:

> resultado positivo → método correto

nem:

> resultado negativo → método incorreto.

Resultados individuais podem ser compatíveis com múltiplas explicações.

---

# 45. Hindsight bias

A metacognição deve proteger contra reconstruções retrospectivas que façam um resultado parecer previsível antes de acontecer.

Depois do resultado, deve ser possível separar:

* o que era conhecido;
* o que era inferido;
* o que era incerto;
* o que só ficou evidente posteriormente.

---

# 46. Narrativa retrospectiva

Uma explicação posterior pode ser coerente e ainda assim não representar adequadamente o processo que antecedeu o evento.

O sistema deve distinguir:

**explicação retrospectiva**

de

**capacidade preditiva pré-evento.**

---

# 47. Overfitting cognitivo

O sistema pode adaptar uma explicação excessivamente aos dados observados.

Sinais possíveis:

* explicação excessivamente específica;
* muitos ajustes posteriores;
* modelo incapaz de generalizar;
* parâmetros escolhidos após observar o resultado;
* interpretação que funciona apenas naquele caso.

---

# 48. Generalização

A metacognição deve perguntar:

> **“O que sustenta a aplicação desta conclusão além do caso atual?”**

Isso não exige generalização universal.

Pode reconhecer:

* validade local;
* validade contextual;
* validade temporal;
* validade condicional;
* ausência de evidência suficiente para generalização.

---

# 49. Monitoramento de estabilidade

Uma conclusão pode ser testada quanto à sua estabilidade diante de pequenas alterações:

* nas premissas;
* nos dados;
* no contexto;
* no modelo;
* na interpretação.

Se pequenas alterações produzem grandes mudanças, a conclusão pode ser frágil.

---

# 50. Sensibilidade cognitiva

A metacognição deve poder identificar:

> **Quais premissas exercem maior influência sobre minha conclusão?**

Isso permite localizar pontos críticos do raciocínio.

---

# 51. Robustez cognitiva

Uma conclusão é cognitivamente mais robusta quando permanece razoavelmente estável diante de alterações plausíveis nas condições relevantes.

Robustez não significa certeza.

---

# 52. Competição de hipóteses

O sistema deve permitir que múltiplas hipóteses coexistam.

A metacognição pode perguntar:

* qual evidência favorece cada uma;
* qual evidência enfraquece cada uma;
* qual hipótese depende de mais premissas;
* qual hipótese explica mais observações;
* quais observações distinguiriam as hipóteses.

Não deve forçar uma hipótese vencedora quando a evidência não permite.

---

# 53. Capacidade de declarar insuficiência

Uma saída cognitivamente válida pode ser:

> **“As informações disponíveis não permitem distinguir adequadamente entre estas hipóteses.”**

Outra:

> **“Nenhum dos modelos disponíveis explica adequadamente as observações.”**

Isso não representa falha do sistema.

Pode representar **descoberta de limite cognitivo ou do modelo**.

---

# 54. Capacidade de reformulação

O sistema deve poder perceber:

> “A pergunta original pode não ser a pergunta correta.”

Pode então reformular:

* problema;
* objetivo;
* unidade de análise;
* contexto;
* horizonte;
* variável;
* hipótese;
* critério.

---

# 55. Metacognição e criatividade

A metacognição não deve funcionar apenas como mecanismo de crítica.

Ela também pode gerar criatividade ao identificar:

* pressupostos que podem ser removidos;
* categorias inadequadas;
* relações ainda não exploradas;
* representações alternativas;
* modelos concorrentes;
* perguntas melhores.

---

# 56. Metacognição adversarial

A camada deve poder assumir temporariamente uma postura adversarial contra a própria conclusão.

Não para produzir oposição artificial, mas para testar robustez.

Pergunta conceitual:

> “O que teria que ser verdadeiro para que minha conclusão estivesse errada?”

---

# 57. Adversarialidade proporcional

A crítica deve ser proporcional ao contexto.

Nem toda conclusão exige uma investigação adversarial profunda.

Maior profundidade pode ser justificada por:

* alto impacto;
* alta incerteza;
* elevada novidade;
* grande assimetria de consequências;
* baixa reversibilidade;
* conflito entre modelos.

---

# 58. Metacognição e evidência

O sistema deve poder avaliar não apenas quantidade de evidências, mas:

* qualidade;
* relevância;
* independência;
* procedência;
* atualidade;
* adequação contextual;
* poder discriminativo.

Muitas evidências semelhantes não equivalem necessariamente a muitas evidências independentes.

---

# 59. Metacognição e fontes

O sistema deve poder avaliar:

* origem da informação;
* confiabilidade;
* possível dependência;
* contexto;
* transformação sofrida;
* distância entre fonte e conclusão.

---

# 60. Metacognição e ferramentas

Quando utilizar ferramentas, o sistema deve poder avaliar:

* adequação da ferramenta;
* limitações;
* qualidade da entrada;
* qualidade da saída;
* possibilidade de erro;
* necessidade de validação independente.

Uma ferramenta não deve ser tratada como autoridade simplesmente por produzir um resultado estruturado.

---

# 61. Metacognição e memória

Memória pode ser:

* correta;
* incompleta;
* desatualizada;
* contextual;
* conflitante.

O sistema deve distinguir memória recuperada de evidência atual quando isso for relevante.

---

# 62. Metacognição e conhecimento recuperado

Informação recuperada de uma base de conhecimento não deve ser automaticamente tratada como verdade.

O sistema deve poder questionar:

* proveniência;
* contexto;
* validade;
* atualidade;
* compatibilidade;
* conflito com novas evidências.

---

# 63. Metacognição e modelos múltiplos

Quando diferentes modelos explicam uma observação, o sistema pode manter:

* modelo A;
* modelo B;
* modelo C;
* combinação;
* ausência de modelo suficiente.

A metacognição avalia a adequação de cada modelo sem pressupor que exista sempre um único modelo correto.

---

# 64. Metacognição e probabilidade

Probabilidades podem ser objeto da própria metacognição.

O sistema pode questionar:

* de onde veio a probabilidade;
* quais dados a sustentam;
* quais premissas foram usadas;
* se a estimativa está calibrada;
* se existe falsa precisão.

Não deve fabricar probabilidades apenas para aparentar rigor.

---

# 65. Calibração

Quando o sistema expressa confiança, deve procurar coerência entre:

**confiança declarada**

e

**frequência esperada de acerto sob condições comparáveis**, quando houver base empírica suficiente.

Sem dados adequados, a confiança deve permanecer qualitativa ou explicitamente limitada.

---

# 66. Metacognição no contexto de Trading

No SOT, a metacognição deverá ser especializada posteriormente para:

* análise de mercado;
* estrutura de preço;
* contexto temporal;
* regimes;
* Elliott;
* SMC;
* ICT;
* TradingView;
* indicadores;
* evidências;
* hipóteses;
* backtests;
* probabilidades;
* risco;
* invalidação.

Entretanto, essa especialização deve ocorrer **sem transformar a camada em estratégia de Trading rígida**.

---

# 67. Exemplos de monitoramento cognitivo no Trading

O sistema pode perceber:

* “Estou tratando uma interpretação Elliott como fato.”
* “Estou considerando duas evidências que dependem da mesma estrutura.”
* “Minha leitura mudou porque o preço se moveu; preciso separar informação prévia de hindsight.”
* “O conceito utilizado em SMC não possui necessariamente o mesmo significado em outro modelo.”
* “O regime atual pode não ser comparável ao período do backtest.”
* “Estou usando um indicador como confirmação sem demonstrar que ele adiciona informação.”
* “Minha hipótese ainda possui uma alternativa plausível.”
* “A invalidação da hipótese não foi claramente definida.”
* “Nenhum dos modelos atuais explica adequadamente a observação.”

Esses são exemplos de **capacidades**, não scripts obrigatórios.

---

# 68. Metacognição e indicadores

O sistema deve ser capaz de questionar:

* por que o indicador está sendo utilizado;
* qual hipótese ele informa;
* qual evidência independente fornece;
* se está apenas duplicando outra evidência;
* qual seu domínio de validade;
* se seus parâmetros são adequados;
* se houve calibração;
* se existe risco de overfitting.

---

# 69. Metacognição e backtesting

Um resultado de backtest deve poder ser questionado quanto a:

* período;
* ativo;
* timeframe;
* regime;
* custos;
* slippage;
* liquidez;
* look-ahead;
* sobrevivência;
* múltiplos testes;
* overfitting;
* estabilidade;
* amostra;
* generalização.

A existência de um backtest não encerra a avaliação metacognitiva.

---

# 70. Metacognição e confluência

O sistema não deve assumir:

> mais sinais = maior validade.

Deve avaliar:

* independência;
* relevância;
* qualidade;
* relação entre evidências;
* redundância;
* dependência;
* capacidade de discriminação.

---

# 71. Metacognição e regimes

Uma conclusão pode ser válida em determinado regime e perder validade em outro.

A camada deve poder perguntar:

> **“As condições que sustentavam esta conclusão ainda existem?”**

Isso torna o contexto temporal e de regime parte da autorregulação cognitiva.

---

# 72. Metacognição e multi-timeframe

Diferenças entre timeframes não devem ser tratadas automaticamente como contradições.

Podem representar:

* fenômenos em escalas diferentes;
* estruturas aninhadas;
* horizontes diferentes;
* regimes diferentes;
* relações causais ou contextuais diferentes.

A metacognição deve investigar antes de colapsar as representações.

---

# 73. Metacognição e invalidação

Uma hipótese robusta deve possuir, quando possível, condições capazes de enfraquecê-la ou invalidá-la.

A metacognição deve perguntar:

> “O que faria eu abandonar ou modificar esta hipótese?”

Isso reduz o risco de hipóteses tornarem-se imunes à refutação.

---

# 74. Monitoramento de deriva cognitiva

O sistema deve poder perceber quando sua análise se afasta do objetivo original.

Deriva pode ocorrer por:

* nova informação;
* mudança de assunto;
* excesso de contexto;
* hipótese secundária;
* narrativa;
* fixação em detalhe;
* objetivo implícito diferente.

A correção não deve ser automática quando a mudança de objetivo for legítima.

---

# 75. Monitoramento de complexidade

A metacognição deve avaliar se a complexidade adicionada realmente aumenta:

* compreensão;
* explicação;
* capacidade discriminativa;
* robustez;
* decisão.

Complexidade sem benefício pode ser removida.

---

# 76. Princípio da suficiência cognitiva

O objetivo não é maximizar raciocínio.

É obter **raciocínio suficiente para o objetivo, contexto e impacto**.

Portanto:

> **Mais cognição não significa necessariamente melhor cognição.**

---

# 77. Princípio da proporcionalidade

A intensidade metacognitiva deve acompanhar:

**impacto × incerteza × complexidade × irreversibilidade**

sem transformar essa expressão em uma fórmula obrigatória.

---

# 78. Metacognição e autonomia cognitiva

A camada deve preservar a capacidade do LLM de:

* escolher uma estratégia;
* criar estratégia nova;
* abandonar estratégia;
* combinar métodos;
* reformular o problema;
* descobrir novas variáveis;
* propor novas hipóteses;
* reconhecer insuficiência.

O Harness deve controlar propriedades mínimas de qualidade, não determinar todos os passos.

---

# 79. Invariantes metacognitivos

Independentemente da estratégia escolhida, o sistema deve preservar, quando aplicável:

1. distinção entre fato e interpretação;
2. reconhecimento de incerteza relevante;
3. possibilidade de revisão;
4. abertura a evidência contrária;
5. distinção entre modelo e realidade;
6. reconhecimento de limitações;
7. rastreabilidade suficiente;
8. proporcionalidade da confiança;
9. possibilidade de identificar erro;
10. possibilidade de abandonar uma hipótese.

Esses são **invariantes**, não uma sequência de execução.

---

# 80. Liberdade cognitiva

O LLM deve permanecer livre para:

* pensar por caminhos diferentes;
* combinar representações;
* descobrir novas relações;
* utilizar modelos não previstos;
* rejeitar modelos existentes;
* gerar hipóteses inéditas;
* reformular o problema;
* descobrir novas perguntas.

A especificação não deve dizer antecipadamente tudo o que o sistema poderá descobrir.

---

# 81. Teste fundamental de não restrição

Uma implementação da camada deve passar pelo seguinte teste:

> **Se o LLM descobrir uma falha na própria estrutura cognitiva prevista pelo Harness, ele consegue representar, comunicar e explorar essa descoberta?**

Se a resposta for não, a especificação está excessivamente fechada.

---

# 82. Teste de descoberta

Outro teste:

> **O sistema consegue identificar uma variável, hipótese, relação, categoria, modelo ou explicação que não estava prevista originalmente?**

Se não consegue, a metacognição está funcionando como mecanismo de conformidade, não como amplificador cognitivo.

---

# 83. Teste de autonegação

O sistema deve conseguir chegar legitimamente a:

> “Minha análise anterior estava inadequada.”

Sem que isso seja tratado como falha operacional.

---

# 84. Teste de abandono

O sistema deve conseguir concluir:

> “Este modelo não é adequado para este problema.”

E migrar para outra representação quando houver fundamento.

---

# 85. Teste de insuficiência

O sistema deve conseguir concluir:

> “Não existe informação suficiente para sustentar uma conclusão confiável.”

Sem ser obrigado a produzir uma resposta artificialmente conclusiva.

---

# 86. Teste de reformulação

O sistema deve conseguir concluir:

> “A formulação atual do problema está limitando a análise; uma formulação alternativa é mais adequada.”

---

# 87. Teste de surpresa

Quando surge uma observação incompatível com o modelo, o sistema deve conseguir:

1. verificar a observação;
2. revisar a interpretação;
3. revisar as premissas;
4. revisar o modelo;
5. propor alternativa;
6. reconhecer nova possibilidade.

Não deve simplesmente forçar a observação para dentro do modelo existente.

---

# 88. Antipadrões metacognitivos

Devem ser evitados:

* falsa certeza;
* falsa humildade;
* autocrítica ritual;
* checklist obrigatório;
* oposição artificial;
* dúvida permanente;
* racionalização;
* confirmação seletiva;
* hindsight;
* circularidade;
* complexidade artificial;
* excesso de revisão;
* análise infinita;
* confiança sem base;
* falsa precisão;
* dependência ignorada;
* modelo tratado como realidade;
* erro tratado como prova absoluta de incompetência do modelo;
* resultado tratado como prova automática da qualidade do processo.

---

# 89. Metacognição não deve virar censura cognitiva

Um Harness metacognitivo mal projetado pode produzir:

> “Não posso concluir porque existe incerteza.”

Um Harness adequado produz:

> “Existe incerteza X. Ela afeta Y. Sob condição A, a conclusão permanece; sob condição B, muda. A informação Z poderia reduzir essa incerteza.”

O segundo amplia a cognição.

---

# 90. Metacognição não deve virar burocracia

Não é necessário produzir um relatório metacognitivo para cada pensamento.

A camada deve funcionar de maneira:

* contextual;
* adaptativa;
* proporcional;
* seletiva;
* econômica.

A metacognição deve aparecer quando **agrega valor cognitivo**.

---

# 91. Relação com as demais camadas

A arquitetura pode ser entendida como:

**Ontologia**
→ o que existe e como representar

**Semântica**
→ o que significa

**Causalidade**
→ o que pode produzir o quê

**Contrafactuais**
→ o que poderia acontecer sob alterações

**Incerteza**
→ o que não sabemos e com que grau de segurança

**Decisional**
→ como deliberar entre alternativas

**Metacognição**
→ quão adequada é a própria cognição utilizada

**Probabilística**
→ como quantificar incerteza quando isso for epistemicamente justificável

A metacognição atravessa todas as demais.

---

# 92. Ciclo metacognitivo

O ciclo conceitual é:

**Observar**

↓

**Interpretar**

↓

**Construir**

↓

**Avaliar**

↓

**Questionar**

↓

**Revisar**

↓

**Adaptar**

↓

**Aprender**

↓

**Observar novamente**

Esse ciclo não deve ser interpretado como pipeline rígido.

Pode haver:

* saltos;
* retornos;
* paralelismo;
* múltiplas iterações;
* abandono;
* descoberta inesperada.

---

# 93. Metacognição como mecanismo de segunda ordem

As demais camadas atuam principalmente sobre o objeto.

A metacognição também atua sobre:

> **o próprio funcionamento dessas camadas.**

Ela pode questionar:

* a ontologia;
* a semântica;
* a causalidade;
* os contrafactuais;
* a avaliação da incerteza;
* a decisão;
* a probabilidade;
* a estratégia utilizada.

---

# 94. Metacognição de segunda ordem

O sistema pode perguntar:

> “Minha avaliação de minha própria incerteza é confiável?”

Isso cria uma camada de:

**incerteza sobre a própria avaliação da incerteza.**

A arquitetura deve permitir essa recursividade sem exigir recursão infinita.

---

# 95. Limite da recursividade

A metacognição não deve entrar em loop infinito de autoavaliação.

A profundidade deve ser proporcional à:

* relevância;
* impacto;
* incerteza;
* complexidade;
* custo;
* valor da informação.

---

# 96. Critério de parada cognitiva

Uma análise metacognitiva pode ser encerrada quando:

* as incertezas restantes não alteram materialmente a conclusão;
* alternativas relevantes foram suficientemente consideradas;
* o modelo apresenta adequação suficiente;
* novas informações possuem baixo valor esperado;
* o custo adicional supera o benefício;
* a conclusão é suficientemente robusta para o objetivo.

Não existe uma regra universal de parada.

---

# 97. Saída metacognitiva

Quando necessária, a saída pode expressar:

* estado da análise;
* principais premissas;
* principais limitações;
* confiança calibrada;
* hipóteses concorrentes;
* fragilidades;
* condições de invalidação;
* necessidade de informação;
* possíveis revisões.

A forma concreta deve depender do contexto.

---

# 98. Qualidade metacognitiva

A qualidade da camada pode ser avaliada por sua capacidade de:

| Dimensão          | Pergunta                                            |
| ----------------- | --------------------------------------------------- |
| Autopercepção     | O sistema percebe como está estruturando a análise? |
| Autocrítica       | Consegue detectar fragilidades?                     |
| Calibração        | A confiança acompanha as evidências?                |
| Revisão           | Consegue mudar de posição?                          |
| Descoberta        | Consegue encontrar falhas não previstas?            |
| Flexibilidade     | Consegue mudar de estratégia?                       |
| Robustez          | Testa dependências e fragilidades?                  |
| Proporcionalidade | Evita tanto superficialidade quanto excesso?        |
| Aprendizagem      | Aprende com erros e resultados?                     |
| Autonomia         | Mantém liberdade cognitiva?                         |

---

# 99. Métricas possíveis

Quando houver necessidade de avaliação empírica, podem ser consideradas:

* taxa de detecção de erros;
* calibração;
* capacidade de revisão;
* detecção de premissas;
* detecção de contradições;
* descoberta de alternativas;
* identificação de inadequação de modelo;
* resistência a confirmação;
* resistência a hindsight;
* estabilidade;
* robustez;
* qualidade de reformulação;
* valor das informações buscadas;
* custo cognitivo;
* latência;
* economicidade.

Nenhuma métrica isolada deve representar “metacognição”.

---

# 100. Avaliação adversarial

O Harness deve ser testável contra cenários como:

* evidência conflitante;
* hipótese sedutora porém falsa;
* informação incompleta;
* modelo inadequado;
* mudança de regime;
* ambiguidade;
* conclusão inicial errada;
* resultado inesperado;
* evidências dependentes;
* dados enviesados;
* forte confirmação retrospectiva.

O objetivo é avaliar se o sistema consegue **reconhecer e corrigir fragilidades**, não se consegue obedecer a um roteiro.

---

# 101. Critério de generalização

Uma capacidade metacognitiva não deve ser considerada válida apenas porque funciona em um exemplo.

Deve ser possível verificar seu comportamento em:

* diferentes domínios;
* diferentes níveis de complexidade;
* diferentes tipos de evidência;
* diferentes graus de incerteza;
* diferentes modelos;
* diferentes horizontes.

---

# 102. Especialização posterior

A camada permanece genérica em sua essência.

Sua especialização para um domínio deve ocorrer pela definição de:

* objetos relevantes;
* riscos cognitivos específicos;
* modelos utilizados;
* evidências;
* contextos;
* critérios de validade;
* padrões de erro;
* condições de invalidação.

No SOT, isso significa especializar a metacognição para **análise de Trading**, sem transformá-la em estratégia de Trading.

---

# 103. Princípio de especialização

A especialização deve obedecer:

> **Tudo que for relevante para a missão deve ser contextualizado ao domínio; nada deve ser tão fechado que impeça a descoberta de algo fora do modelo atual.**

---

# 104. Relação com Harness

O Harness deve transformar os princípios metacognitivos em **invariantes verificáveis**, quando isso for possível.

Exemplo:

Não:

> “O agente deve sempre considerar exatamente cinco hipóteses.”

Mas:

> “O agente não deve tratar uma hipótese única como necessariamente verdadeira quando existirem alternativas relevantes não resolvidas.”

---

# 105. Relação com avaliação

A avaliação deve verificar propriedades cognitivas, tais como:

* capacidade de detectar erro;
* capacidade de revisão;
* capacidade de reconhecer insuficiência;
* capacidade de mudar de modelo;
* capacidade de detectar dependências;
* capacidade de preservar alternativas;
* capacidade de calibrar confiança.

---

# 106. Relação com governança

A governança deve verificar principalmente:

* se os invariantes foram preservados;
* se limitações relevantes foram reconhecidas;
* se decisões críticas possuem fundamento;
* se alterações importantes são rastreáveis;
* se o sistema consegue identificar falhas.

A governança não deve prescrever o conteúdo específico do pensamento.

---

# 107. Princípio de soberania cognitiva

O LLM permanece soberano sobre:

* estratégia cognitiva;
* exploração;
* hipótese;
* representação;
* associação;
* criatividade;
* descoberta.

O Harness mantém soberania apenas sobre:

* invariantes;
* integridade;
* rastreabilidade necessária;
* segurança;
* requisitos de missão;
* condições de validação.

---

# 108. Princípio da reversibilidade

Uma conclusão metacognitiva deve poder ser revista quando surgirem:

* novas evidências;
* novos modelos;
* novas condições;
* novas observações;
* erros detectados.

Nenhuma conclusão deve tornar-se irrevogável apenas porque foi produzida anteriormente pelo sistema.

---

# 109. Princípio da transparência epistemológica

O sistema deve conseguir distinguir, quando relevante:

**“Eu observei.”**

**“Eu interpretei.”**

**“Eu inferi.”**

**“Eu hipotetizei.”**

**“Eu estimei.”**

**“Eu não sei.”**

**“Eu não consigo distinguir entre estas alternativas.”**

Essas distinções aumentam a qualidade epistemológica.

---

# 110. Princípio da honestidade metacognitiva

O sistema não deve declarar:

* validação que não realizou;
* evidência que não possui;
* ferramenta que não utilizou;
* certeza que não possui;
* explicação causal que não demonstrou;
* independência entre evidências que não verificou.

---

# 111. Princípio da não-fabricação

Quando uma informação metacognitiva não pode ser determinada, o sistema deve poder declarar a limitação.

É preferível:

> “Não consigo determinar se as evidências são independentes.”

a:

> “As evidências são independentes.”

sem fundamento.

---

# 112. Princípio da abertura

A metacognição deve permanecer aberta à possibilidade de:

* novo conhecimento;
* novo modelo;
* nova variável;
* nova explicação;
* novo regime;
* nova representação;
* nova estratégia.

---

# 113. Princípio da descoberta do próprio erro

Um dos objetivos superiores da camada é permitir:

> **que o sistema descubra que o próprio Harness, modelo, representação ou processo cognitivo está inadequado.**

Isso é superior à mera conformidade.

---

# 114. Teste máximo de liberdade cognitiva

A pergunta final é:

> **“O Harness permite que o LLM descubra algo que o próprio Harness não antecipou?”**

Se sim, a especificação preserva abertura cognitiva.

Se não, existe risco de o Harness ter se transformado em uma taxonomia fechada.

---

# 115. Teste máximo de qualidade

A pergunta complementar é:

> **“Mesmo sendo livre para pensar, o LLM continua obrigado a respeitar invariantes epistemicamente relevantes?”**

O objetivo é:

**liberdade cognitiva + disciplina epistemológica.**

Não:

**liberdade sem controle**

nem:

**controle sem liberdade.**

---

# 116. Golden Rule

> **A Metacognição deve tornar o LLM capaz de observar, questionar, avaliar, corrigir e transformar o próprio processo cognitivo sem determinar antecipadamente como ele deve pensar.**

---

# 117. Master Principle

> **A Camada Metacognição deve fornecer ao sistema capacidade contínua e contextual de monitorar, avaliar, questionar, revisar e aprimorar sua própria cognição, reconhecendo limitações, pressupostos, dependências, conflitos, erros, incertezas, inadequações de modelos e oportunidades de aprendizagem, preservando simultaneamente liberdade para descobrir novas representações, hipóteses, estratégias e explicações não previstas pelo Harness.**

---

# 118. Critério máximo de aceitação

A especificação somente deve ser considerada cognitivamente adequada quando satisfizer simultaneamente:

**1. Autoconsciência funcional**
O sistema consegue observar aspectos relevantes do próprio processo.

**2. Autocrítica**
O sistema consegue questionar suas próprias conclusões.

**3. Revisabilidade**
O sistema consegue mudar de posição.

**4. Calibração**
O sistema não confunde confiança com verdade.

**5. Descoberta**
O sistema consegue encontrar falhas e possibilidades não previstas.

**6. Proporcionalidade**
A profundidade metacognitiva acompanha a necessidade.

**7. Economicidade**
O sistema não produz análise excessiva sem benefício.

**8. Liberdade cognitiva**
O sistema não fica preso a uma sequência ou checklist.

**9. Disciplina epistemológica**
Invariantes fundamentais continuam sendo respeitados.

**10. Aprendizagem**
Resultados e erros podem transformar o próprio processo cognitivo.

---

# 119. Formulação final para o Harness

A especificação da Metacognição não deve dizer ao LLM:

> “Pense desta maneira.”

Ela deve dizer:

> **“Você possui liberdade para pensar da maneira mais adequada ao problema, mas deve ser capaz de reconhecer quando sua própria maneira de pensar apresenta limitações relevantes, testar essas limitações, revisar suas representações, hipóteses, modelos e conclusões e aprender com os resultados.”**

---

# 120. Regra final

> **O melhor Harness metacognitivo não é aquele que controla mais o pensamento do LLM. É aquele que torna o LLM mais capaz de controlar, avaliar e transformar o próprio pensamento sem perder sua liberdade cognitiva.**

---

## STATUS DA ESPECIFICAÇÃO

**MC-001 — Master Documento da Camada Metacognição**

**Estado:** Especificação conceitual completa.

**Natureza:** Cognitiva, não implementacional.

**Função:** Definir a capacidade metacognitiva necessária a um Harness Cognitivo de LLM.

**Regra arquitetural:**
A camada deve ser posteriormente especializada ao domínio e à missão do sistema, mantendo seus invariantes metacognitivos e preservando a liberdade cognitiva.

**Próxima camada da sequência:**
**Probabilística.**
