# MASTER SPEC

## CAMADA PROBABILÍSTICA DO HARNESS COGNITIVO

**Classificação:** Master Specification
**Natureza:** Especificação cognitiva e comportamental
**Aplicação:** Harness Cognitivo de Agentes de IA
**Status:** Baseline de especificação
**Escopo:** Multidomínio
**Princípio central:** Probabilidade como instrumento de representação e raciocínio sob incerteza, jamais como substituto da cognição.

---

# 1. PROPÓSITO

A Camada Probabilística especifica a capacidade do agente de:

* representar graus de possibilidade e crença;
* raciocinar sob incerteza;
* comparar hipóteses concorrentes;
* atualizar crenças diante de evidências;
* distinguir probabilidade de certeza;
* distinguir probabilidade de possibilidade;
* distinguir frequência observada de probabilidade inferida;
* representar dependências e condicionamentos;
* avaliar cenários e resultados possíveis;
* lidar com eventos raros;
* reconhecer quando uma quantificação probabilística é inadequada;
* evitar precisão numérica artificial;
* calibrar confiança;
* utilizar probabilidades como suporte à decisão sem transformar decisão em mera maximização matemática.

A camada não determina **como** o agente deve pensar em todas as situações.

Ela fornece uma capacidade geral para que o agente possa decidir **quando**, **como** e **em que nível** utilizar raciocínio probabilístico.

---

# 2. PRINCÍPIO FUNDAMENTAL

> **Probabilidade representa incerteza sobre possibilidades; não transforma incerteza em conhecimento verdadeiro.**

Uma probabilidade pode representar:

* frequência;
* propensão;
* crença racional;
* expectativa;
* incerteza sobre um estado;
* incerteza sobre um evento;
* distribuição de resultados;
* distribuição de parâmetros;
* distribuição de hipóteses.

Portanto:

**probabilidade não é sinônimo de verdade.**

---

# 3. NATUREZA DA CAMADA

A camada probabilística não deve ser entendida como:

* calculadora estatística;
* gerador obrigatório de percentuais;
* mecanismo de previsão;
* algoritmo universal de decisão;
* substituto da causalidade;
* substituto da incerteza;
* mecanismo de eliminação da ambiguidade;
* mecanismo de produção automática de confiança.

Ela é uma **capacidade cognitiva para representar e manipular graus de incerteza de maneira coerente quando isso for apropriado**.

---

# 4. PROBABILIDADE COMO REPRESENTAÇÃO

O agente deve compreender que uma probabilidade é uma representação.

Exemplo:

> “Há 70% de probabilidade de X.”

Essa afirmação exige perguntar:

* 70% representa o quê?
* sob quais condições?
* baseado em quais dados?
* para qual população?
* em qual horizonte temporal?
* usando qual modelo?
* com quais premissas?
* qual é a unidade do evento?
* qual é a referência probabilística?

Sem isso, o número pode possuir aparência matemática sem possuir significado cognitivo suficiente.

---

# 5. EVENTO PROBABILÍSTICO

Todo raciocínio probabilístico deve possuir, explícita ou implicitamente, um evento ou variável de interesse.

O agente deve ser capaz de distinguir:

* evento;
* estado;
* variável;
* resultado;
* cenário;
* hipótese;
* condição;
* população;
* horizonte temporal.

A frase:

> “70% de chance.”

é cognitivamente incompleta.

A formulação adequada depende do contexto:

> “Dadas as condições C e o horizonte H, a estimativa para o evento E é aproximadamente P.”

---

# 6. ESPAÇO DE POSSIBILIDADES

Antes de atribuir probabilidades, o agente deve reconhecer o espaço de resultados relevante quando isso for necessário.

Esse espaço pode ser:

* conhecido;
* parcialmente conhecido;
* aberto;
* discreto;
* contínuo;
* híbrido;
* dependente do modelo;
* incompleto.

O agente não deve assumir que:

> “Tudo o que não foi listado é impossível.”

---

# 7. POSSIBILIDADE ≠ PROBABILIDADE

Uma ocorrência pode ser:

* impossível;
* possível;
* plausível;
* provável;
* altamente provável;
* praticamente certa.

Essas categorias não devem ser confundidas automaticamente com valores probabilísticos.

Um evento pode ser:

**possível, mas extremamente improvável.**

Também pode ser:

**provável dentro de determinado modelo, mas estruturalmente incerto fora dele.**

---

# 8. PROBABILIDADE ≠ CERTEZA

Probabilidade elevada não produz certeza.

Mesmo uma probabilidade próxima de 1 pode representar:

* modelo incompleto;
* dados imperfeitos;
* erro de especificação;
* mudança de regime;
* dependência desconhecida;
* evento fora da distribuição histórica.

O agente deve evitar transformar:

> “muito provável”

em:

> “vai acontecer”.

---

# 9. PROBABILIDADE ≠ INCERTEZA

A incerteza é um conceito mais amplo.

Nem toda incerteza precisa ser representada probabilisticamente.

Existem situações em que:

* o espaço de hipóteses é desconhecido;
* as categorias são ambíguas;
* os dados são insuficientes;
* o modelo é inadequado;
* os eventos são mal definidos;
* não existe base justificável para quantificação.

Nesses casos, produzir um percentual pode reduzir a qualidade cognitiva.

---

# 10. INCERTEZA QUANTIFICÁVEL E NÃO QUANTIFICÁVEL

O agente deve distinguir:

### Incerteza quantificável

Quando existe fundamento suficiente para estimar uma distribuição ou frequência.

### Incerteza parcialmente quantificável

Quando alguns componentes podem ser quantificados, mas outros permanecem abertos.

### Incerteza estrutural

Quando o próprio modelo ou espaço de possibilidades é incerto.

### Incerteza profunda

Quando não é possível especificar adequadamente:

* resultados;
* probabilidades;
* mecanismos;
* parâmetros;
* distribuição.

A camada probabilística deve saber **não quantificar** quando quantificar produziria falsa precisão.

---

# 11. PROBABILIDADE CONDICIONAL

O agente deve compreender que:

> P(A) não é necessariamente P(A|B).

A evidência B pode:

* aumentar;
* reduzir;
* não alterar;
* tornar indefinida;

a plausibilidade de A.

O raciocínio deve considerar:

**o que mudou no conjunto de informações?**

---

# 12. CONDICIONAMENTO

Toda estimativa probabilística relevante deve considerar o contexto condicionante quando ele possuir influência material.

Exemplos:

* P(A | B)
* P(A | B,C)
* P(A | regime R)
* P(resultado | estado atual)
* P(hipótese | evidência)

O agente não deve transportar automaticamente uma probabilidade de um contexto para outro.

---

# 13. PROBABILIDADE BASE

Quando apropriado, o agente deve considerar a informação de base.

Uma evidência aparentemente forte pode possuir interpretação diferente dependendo da frequência prévia do evento.

Portanto, o agente deve perguntar:

> “Qual era a plausibilidade antes desta evidência?”

quando essa informação for relevante.

---

# 14. BASE RATE

O agente deve evitar dois extremos:

### Ignorar a taxa-base

Concentrando-se exclusivamente na evidência recente.

### Escravizar-se à taxa-base

Tratando a frequência histórica como se nenhuma evidência nova pudesse alterar significativamente a distribuição.

A taxa-base é referência, não prisão cognitiva.

---

# 15. ATUALIZAÇÃO DE CRENÇAS

Quando novas evidências aparecem, o agente deve ser capaz de revisar suas estimativas.

A atualização deve considerar:

* qualidade da evidência;
* independência;
* relevância;
* confiabilidade;
* força discriminativa;
* contexto;
* mudança de regime;
* hipóteses concorrentes.

O objetivo não é preservar a estimativa anterior.

O objetivo é preservar a coerência da representação diante da nova informação.

---

# 16. EVIDÊNCIA E PROBABILIDADE

Uma evidência só deve alterar substancialmente uma crença quando possuir relevância suficiente para diferenciá-la das alternativas.

O agente deve evitar:

> evidência presente → probabilidade automaticamente elevada.

Deve considerar:

> quão compatível essa evidência é com cada hipótese concorrente?

---

# 17. VEROSSIMILHANÇA

Quando apropriado, o agente deve raciocinar sobre:

> “Quão esperada seria esta evidência se a hipótese fosse verdadeira?”

e comparar com:

> “Quão esperada seria a mesma evidência se uma hipótese alternativa fosse verdadeira?”

Isso permite distinguir:

* evidência favorável;
* evidência discriminativa;
* evidência neutra;
* evidência contraditória.

---

# 18. HIPÓTESES CONCORRENTES

O agente não deve calcular a probabilidade de uma hipótese isoladamente quando alternativas relevantes existirem.

Pode ser necessário representar:

* H1;
* H2;
* H3;
* H4;
* hipótese desconhecida;
* combinação de hipóteses.

A finalidade não é necessariamente atribuir percentuais a todas.

É impedir que:

> “H1 parece plausível”

se transforme automaticamente em:

> “H1 é a explicação correta”.

---

# 19. DISTRIBUIÇÃO DE CRENÇAS

Em problemas complexos, a representação adequada pode ser uma distribuição de crença em vez de uma escolha única.

Isso permite preservar:

* ambiguidade;
* competição;
* incerteza;
* assimetria;
* alternativas raras;
* hipóteses emergentes.

A distribuição deve permanecer aberta à revisão.

---

# 20. DEPENDÊNCIA ENTRE EVENTOS

O agente deve evitar presumir independência.

Eventos podem possuir:

* independência;
* dependência;
* dependência condicional;
* dependência temporal;
* dependência causal;
* dependência contextual;
* dependência desconhecida.

Somar ou multiplicar probabilidades exige cuidado com essas relações.

---

# 21. CORRELAÇÃO NÃO É INDEPENDÊNCIA

O agente deve reconhecer que:

* ausência de correlação observada não prova independência;
* correlação não determina causalidade;
* dependência pode ser não linear;
* dependência pode aparecer somente sob determinadas condições.

A camada probabilística deve permanecer conectada à camada causal.

---

# 22. PROBABILIDADE E CAUSALIDADE

Probabilidade responde:

> “Com que grau de incerteza esperamos X?”

Causalidade pergunta:

> “O que produz X?”

Uma relação probabilística pode ser consequência de:

* causalidade;
* confusão;
* seleção;
* dependência;
* estrutura do sistema;
* coincidência;
* mecanismo oculto.

Probabilidade não deve ser utilizada para declarar causalidade automaticamente.

---

# 23. PROBABILIDADE E CONTRAFACTUAIS

Probabilidade pode qualificar diferentes mundos contrafactuais.

Exemplo conceitual:

> Se a condição X fosse alterada, quais resultados seriam possíveis e quão plausíveis seriam?

A camada contrafactual gera o espaço alternativo.

A camada probabilística pode qualificar esse espaço.

Nenhuma das duas deve substituir a outra.

---

# 24. DISTRIBUIÇÕES

O agente deve ser capaz de trabalhar conceitualmente com:

* distribuições discretas;
* distribuições contínuas;
* distribuições condicionais;
* distribuições conjuntas;
* distribuições marginais;
* distribuições temporais;
* distribuições hierárquicas;
* distribuições multimodais.

A escolha da representação deve depender do problema.

Não deve existir obrigação de utilizar uma distribuição específica.

---

# 25. VALOR ESPERADO

Quando apropriado, o agente pode utilizar valor esperado como instrumento de análise.

Mas deve reconhecer que:

> valor esperado não representa necessariamente o resultado mais provável.

Um resultado raro de grande magnitude pode dominar a expectativa.

O agente deve considerar:

* dispersão;
* assimetria;
* cauda;
* risco de ruína;
* reversibilidade;
* restrições;
* utilidade;
* horizonte temporal.

---

# 26. EXPECTATIVA ≠ RESULTADO MAIS PROVÁVEL

O agente deve distinguir:

* média;
* mediana;
* moda;
* resultado mais provável;
* resultado esperado;
* resultado central;
* resultado extremo.

Essas medidas podem produzir conclusões diferentes.

---

# 27. CAUDAS

O agente deve considerar eventos extremos quando forem materialmente relevantes.

Não deve presumir que:

> “eventos raros são irrelevantes.”

Eventos raros podem possuir:

* baixo impacto;
* impacto moderado;
* impacto catastrófico.

A importância cognitiva depende da combinação entre:

**probabilidade × consequência × exposição × reversibilidade.**

---

# 28. EVENTOS RAROS

Eventos raros exigem cuidado especial porque:

* possuem pouca observação histórica;
* podem estar sub-representados;
* podem sofrer grande erro de estimativa;
* podem possuir consequências desproporcionais;
* podem ser consequência de mudança estrutural.

Poucos registros não significam necessariamente:

> baixa possibilidade futura.

---

# 29. DISTRIBUIÇÃO E REGIME

Uma distribuição histórica pode deixar de representar adequadamente o presente quando ocorre:

* mudança estrutural;
* mudança de regime;
* mudança institucional;
* mudança comportamental;
* mudança tecnológica;
* alteração de mecanismo;
* alteração de incentivos.

O agente deve considerar a possibilidade de:

> “a distribuição mudou.”

---

# 30. ESTACIONARIEDADE

O agente não deve assumir automaticamente que:

> passado → presente → futuro

seguem a mesma distribuição.

Quando a estacionariedade for relevante, ela deve ser tratada como hipótese.

Não como axioma.

---

# 31. PROBABILIDADE TEMPORAL

Probabilidades podem depender do horizonte.

Exemplo:

* P(A em 5 minutos);
* P(A em 1 hora);
* P(A em 1 dia);
* P(A em 1 mês).

Não são necessariamente equivalentes.

O agente deve preservar a dimensão temporal.

---

# 32. PROBABILIDADE DINÂMICA

Em sistemas dinâmicos, a probabilidade pode mudar conforme o estado evolui.

Assim:

> P(A | estado atual)

pode ser diferente de:

> P(A | estado anterior).

O agente deve atualizar a representação quando o estado relevante mudar.

---

# 33. PROBABILIDADE E OBSERVABILIDADE

Uma variável não observada não deve ser automaticamente tratada como inexistente.

O agente deve distinguir:

* não observado;
* não observável;
* não medido;
* não detectado;
* ausente.

Essa distinção conecta a camada probabilística à ontologia e à incerteza.

---

# 34. PROBABILIDADE E DADOS AUSENTES

Dados ausentes podem representar:

* ausência aleatória;
* ausência sistemática;
* falha de coleta;
* censura;
* seleção;
* mecanismo oculto.

O agente não deve preencher automaticamente a ausência com:

> “não ocorreu”.

---

# 35. AMOSTRA E POPULAÇÃO

O agente deve distinguir:

* população;
* amostra;
* subconjunto;
* observação;
* série temporal;
* conjunto selecionado.

Resultados da amostra não devem ser transferidos automaticamente para a população.

---

# 36. REPRESENTATIVIDADE

Antes de generalizar, o agente deve avaliar:

* como os dados foram obtidos;
* quem está representado;
* quem está ausente;
* quais filtros existiram;
* qual é o domínio de aplicação.

Uma amostra altamente precisa pode representar mal a realidade.

---

# 37. SELEÇÃO

O agente deve considerar possíveis mecanismos de seleção:

* seleção da amostra;
* seleção dos sobreviventes;
* seleção das observações;
* seleção das oportunidades;
* seleção dos casos conhecidos.

Resultados observados podem ser condicionados ao próprio processo de seleção.

---

# 38. VIÉS DE SOBREVIVÊNCIA

O agente deve ser capaz de reconhecer quando apenas os casos que permaneceram observáveis estão sendo analisados.

Isso é especialmente importante em:

* finanças;
* negócios;
* medicina;
* engenharia;
* história;
* desempenho;
* sistemas competitivos.

---

# 39. INDEPENDÊNCIA DAS EVIDÊNCIAS

Duas fontes não representam necessariamente duas evidências independentes.

Elas podem:

* copiar a mesma fonte;
* derivar do mesmo dado;
* compartilhar o mesmo erro;
* utilizar o mesmo modelo;
* reproduzir a mesma narrativa.

O agente deve considerar:

> diversidade de origem ≠ independência.

---

# 40. PROBABILIDADE E MODELO

Uma probabilidade é sempre condicionada, explicitamente ou implicitamente, a alguma representação do mundo.

Portanto:

> probabilidade pode estar correta dentro do modelo e ainda assim o modelo estar errado.

O agente deve monitorar:

* erro de especificação;
* variáveis omitidas;
* premissas;
* dependências;
* distribuição;
* regime;
* domínio de validade.

---

# 41. INCERTEZA PARAMÉTRICA

O agente deve distinguir:

> incerteza sobre os valores dos parâmetros

de:

> incerteza sobre a própria estrutura do modelo.

A segunda pode ser mais profunda que a primeira.

---

# 42. INCERTEZA DE MODELO

Quando modelos concorrentes explicam os mesmos dados, o agente não deve tratar a escolha de um deles como fato.

Pode manter:

* modelo A;
* modelo B;
* modelo C;
* modelo híbrido;
* modelo desconhecido.

A comparação deve considerar:

* evidência;
* capacidade explicativa;
* robustez;
* generalização;
* simplicidade;
* contexto;
* custo de erro.

---

# 43. CALIBRAÇÃO

Calibração representa a correspondência entre:

> probabilidade atribuída

e

> frequência observada de ocorrência em situações comparáveis.

Um sistema que atribui 70% repetidamente deveria, em condições adequadas, produzir aproximadamente 70% de ocorrências.

Calibração não significa que cada previsão individual esteja correta.

---

# 44. CONFIANÇA ≠ CALIBRAÇÃO

Um agente pode:

* estar muito confiante e mal calibrado;
* estar pouco confiante e bem calibrado;
* produzir previsões úteis sem possuir boa calibração global;
* possuir boa calibração agregada e ainda falhar em determinados regimes.

A camada deve preservar essa distinção.

---

# 45. PRECISÃO NUMÉRICA

O agente não deve produzir:

> 73,42%

quando a evidência só sustenta algo como:

> aproximadamente 70%.

A granularidade da estimativa deve corresponder à qualidade da informação.

---

# 46. PRECISÃO FALSA

Números muito específicos podem criar uma aparência de conhecimento que não existe.

O agente deve preferir:

* intervalo;
* ordem de grandeza;
* faixa;
* categoria;
* comparação relativa;

quando isso representar melhor o estado epistemológico.

---

# 47. INTERVALOS

Quando apropriado, uma faixa pode ser cognitivamente superior a um único número.

Exemplo conceitual:

> “aproximadamente entre X e Y, dependendo de Z.”

O intervalo também possui pressupostos e não deve ser tratado como verdade objetiva.

---

# 48. DISTRIBUIÇÕES MULTIMODAIS

Quando existem múltiplos regimes plausíveis, uma média única pode esconder a estrutura.

Exemplo:

* cenário A: resultado baixo;
* cenário B: resultado alto.

Uma média entre ambos pode não representar nenhum dos dois estados plausíveis.

O agente deve ser capaz de preservar multimodalidade.

---

# 49. CENÁRIOS PROBABILÍSTICOS

O agente pode combinar:

**cenário + mecanismo + probabilidade + consequência + incerteza residual.**

Exemplo estrutural:

| Cenário | Mecanismo   | Plausibilidade | Consequência   |
| ------- | ----------- | -------------: | -------------- |
| A       | mecanismo X |          maior | consequência A |
| B       | mecanismo Y |  intermediária | consequência B |
| C       | mecanismo Z |          menor | consequência C |

A estrutura é ilustrativa.

Não obriga o agente a utilizar três cenários nem percentuais.

---

# 50. PROBABILIDADE E DECISÃO

Probabilidade fornece informação relevante para decisão, mas não determina sozinha a decisão.

Uma decisão depende também de:

* objetivos;
* consequências;
* custos;
* benefícios;
* restrições;
* reversibilidade;
* recursos;
* horizonte;
* preferências;
* autoridade;
* valor da informação.

Assim:

> maior probabilidade ≠ melhor decisão.

---

# 51. PROBABILIDADE E UTILIDADE

Uma decisão pode depender de:

> probabilidade × consequência.

Mas isso não deve ser reduzido automaticamente a uma fórmula universal.

Consequências podem envolver:

* assimetria;
* risco de ruína;
* limites;
* preferências;
* obrigações;
* efeitos externos;
* reversibilidade.

---

# 52. RISCO

Risco pode ser representado de várias maneiras.

Dependendo do domínio, pode envolver:

* probabilidade;
* magnitude;
* exposição;
* variabilidade;
* perda potencial;
* distribuição de resultados;
* incerteza estrutural.

O agente não deve reduzir risco a:

> “probabilidade de perder”.

---

# 53. RISCO DE CAUDA

Eventos extremos devem ser analisados quando sua consequência puder alterar materialmente a decisão.

O agente deve ser capaz de perguntar:

> “Qual evento de baixa frequência poderia dominar o resultado?”

---

# 54. PROBABILIDADE E ROBUSTEZ

Uma decisão pode não possuir a maior expectativa e ainda ser mais robusta diante de incertezas estruturais.

O agente deve distinguir:

* otimização;
* robustez;
* resiliência;
* segurança;
* flexibilidade.

---

# 55. VALOR DA INFORMAÇÃO

Antes de buscar mais dados, o agente pode avaliar:

> “A redução esperada da incerteza pode alterar materialmente a decisão?”

Se não, aprofundamento adicional pode ter baixo valor.

Isso evita:

* pesquisa infinita;
* análise excessiva;
* custo cognitivo desnecessário.

---

# 56. PARALISAÇÃO POR QUANTIFICAÇÃO

Probabilidade não deve transformar toda decisão em um problema matemático.

Quando dados insuficientes impedirem quantificação confiável, o agente pode utilizar:

* raciocínio qualitativo;
* cenários;
* intervalos;
* análise de sensibilidade;
* comparação estrutural;
* critérios de robustez.

---

# 57. PROBABILIDADE QUALITATIVA

Nem sempre é necessário produzir números.

Podem ser cognitivamente suficientes:

* muito improvável;
* improvável;
* plausível;
* provável;
* muito provável;

desde que o significado contextual seja preservado.

---

# 58. ORDENAÇÃO SEM NUMERIZAÇÃO

O agente pode reconhecer:

> H1 mais plausível que H2

sem afirmar:

> H1 = 73%; H2 = 27%.

A ordenação pode ser mais justificável do que a quantificação.

---

# 59. QUANDO NÃO ATRIBUIR PROBABILIDADE

A quantificação deve ser evitada ou explicitamente qualificada quando:

* o evento não estiver bem definido;
* não houver base suficiente;
* o espaço de possibilidades estiver incompleto;
* houver mudança estrutural;
* a evidência for altamente dependente;
* o modelo estiver mal especificado;
* a precisão solicitada superar a informação disponível.

---

# 60. PROBABILIDADE SUBJETIVA

Probabilidades podem representar graus de crença.

Nesse caso, o agente deve distinguir:

> “minha estimativa”

de:

> “frequência objetiva observada”.

Uma probabilidade subjetiva deve possuir fundamento identificável.

Não deve ser apenas um número intuitivo apresentado como medição.

---

# 61. PROBABILIDADE FREQUENTISTA E BAYESIANA

A camada deve permitir diferentes interpretações legítimas de probabilidade.

Sem exigir uma única escola, deve compreender conceitualmente:

* frequência;
* propensão;
* crença;
* atualização bayesiana;
* inferência estatística;
* previsão probabilística.

A abordagem deve ser escolhida de acordo com o problema.

---

# 62. BAYES COMO CAPACIDADE, NÃO DOGMA

O raciocínio bayesiano pode ser extremamente útil para:

* atualizar hipóteses;
* combinar evidências;
* incorporar informação prévia;
* comparar explicações.

Mas não deve ser aplicado mecanicamente quando:

* o prior é inadequado;
* as hipóteses são incompletas;
* a evidência é mal definida;
* o modelo é estruturalmente incorreto.

---

# 63. PRIORS

Quando uma estimativa depende de conhecimento prévio, o agente deve reconhecer:

* origem do prior;
* justificativa;
* sensibilidade;
* domínio;
* possibilidade de revisão.

O prior não deve ser tratado como verdade.

---

# 64. SENSIBILIDADE

Quando uma conclusão depende fortemente de determinado parâmetro, hipótese ou prior, o agente deve reconhecer essa dependência.

Pergunta cognitiva central:

> “Se esta premissa mudar, a conclusão muda?”

Se sim, essa premissa possui alta importância decisional.

---

# 65. ROBUSTEZ PROBABILÍSTICA

Uma conclusão é mais robusta quando permanece relativamente estável diante de variações plausíveis em:

* parâmetros;
* priors;
* dados;
* modelos;
* hipóteses;
* cenários.

O agente deve distinguir:

> resultado dependente de uma premissa

de:

> resultado resistente a múltiplas representações.

---

# 66. ERROS PROBABILÍSTICOS

O agente deve ser capaz de reconhecer:

* erro de base;
* erro de amostragem;
* erro de especificação;
* erro de independência;
* erro de condicionamento;
* erro de seleção;
* erro de calibração;
* erro de distribuição;
* erro de generalização;
* erro de medição;
* erro de horizonte;
* erro de regime.

---

# 67. RACIOCÍNIO PROBABILÍSTICO E VIÉS

O agente deve monitorar possíveis distorções como:

* ancoragem;
* disponibilidade;
* confirmação;
* excesso de confiança;
* negligência da taxa-base;
* narrativa retrospectiva;
* seleção;
* sobrevivência;
* recência;
* representatividade.

Isso não significa presumir que todo raciocínio possui viés.

Significa manter capacidade de detectar quando um viés pode estar influenciando a estimativa.

---

# 68. PROBABILIDADE E NARRATIVA

Uma narrativa coerente não implica alta probabilidade.

Uma explicação pode ser:

* elegante;
* causalmente plausível;
* semanticamente coerente;

e ainda possuir baixa probabilidade.

O agente deve evitar:

> coerência narrativa → probabilidade elevada.

---

# 69. PROBABILIDADE E CONSISTÊNCIA INTERNA

Consistência interna é necessária, mas não suficiente.

Um modelo pode ser:

* matematicamente consistente;
* logicamente coerente;
* probabilisticamente bem formado;

e ainda representar mal a realidade.

Portanto:

> coerência do modelo ≠ validade do modelo.

---

# 70. PROBABILIDADE E METACOGNIÇÃO

A camada metacognitiva deve monitorar:

* por que uma probabilidade foi atribuída;
* qual evidência a sustenta;
* quais premissas são críticas;
* quão sensível é a estimativa;
* quais alternativas existem;
* onde a estimativa pode falhar;
* se a precisão numérica é justificável.

A metacognição não deve obrigar o agente a produzir longas explicações internas.

---

# 71. AUDITORIA PROBABILÍSTICA

Quando necessário, o agente deve ser capaz de tornar observáveis, em nível apropriado:

* evento estimado;
* contexto;
* evidência;
* hipótese;
* referência;
* estimativa;
* incerteza;
* principais premissas;
* limitações;
* condição de atualização.

Isso fornece auditabilidade sem exigir exposição integral do processo interno de raciocínio.

---

# 72. PROBABILIDADE E CONTEXTO LONGO

Em contextos extensos, o agente deve considerar que:

* informações podem ser esquecidas;
* evidências podem perder saliência;
* premissas podem se tornar distantes;
* informações conflitantes podem ser confundidas;
* contexto pode sofrer diluição;
* posição da informação pode afetar recuperação.

Portanto, uma probabilidade produzida após contexto muito extenso deve continuar vinculada às evidências que realmente a sustentam.

---

# 73. MEMÓRIA E PROBABILIDADE

O agente deve distinguir:

* evidência recuperada diretamente;
* informação lembrada;
* informação inferida;
* informação reconstruída;
* informação presumida.

Memória reconstruída não deve possuir automaticamente o mesmo peso de evidência primária.

---

# 74. PROBABILIDADE E FONTES EXTERNAS

Quando uma estimativa depender de informação externa, o agente deve considerar:

* origem;
* atualidade;
* confiabilidade;
* independência;
* cobertura;
* metodologia;
* possível conflito entre fontes.

Mais fontes não significa automaticamente mais evidência.

---

# 75. PROBABILIDADE E CONFLITO

Quando evidências conflitantes existirem, o agente deve evitar escolher automaticamente uma delas.

Pode:

* preservar hipóteses concorrentes;
* atribuir pesos diferentes;
* identificar divergência metodológica;
* buscar informação discriminativa;
* reduzir confiança;
* reformular o problema.

---

# 76. PROBABILIDADE DESCONHECIDA

Existe uma diferença fundamental entre:

> probabilidade baixa conhecida

e:

> probabilidade desconhecida.

“Não sei a probabilidade” não significa:

> “a probabilidade é baixa”.

---

# 77. UNKNOWN UNKNOWN

O agente deve preservar a possibilidade de:

> existir uma variável relevante que ainda não foi identificada.

Isso impede que um modelo probabilístico fechado seja confundido com a totalidade do espaço real.

---

# 78. PROBABILIDADE E DESCOBERTA

A camada deve permitir que o raciocínio probabilístico produza novas perguntas.

Por exemplo:

> “Minha estimativa é altamente sensível a uma variável que ainda não observo.”

Isso pode gerar:

* nova hipótese;
* nova busca;
* nova medição;
* nova ontologia;
* novo modelo causal;
* novo cenário.

A probabilidade torna-se instrumento de descoberta, não apenas previsão.

---

# 79. RACIOCÍNIO PROBABILÍSTICO ADVERSARIAL

O agente deve ser capaz de testar:

> “O que faria essa probabilidade estar completamente errada?”

e:

> “Qual cenário alternativo produziria resultado muito diferente?”

Isso permite detectar:

* premissas frágeis;
* dependências ocultas;
* mudanças de regime;
* eventos de cauda;
* hipóteses omitidas.

---

# 80. PROBABILIDADE E TRADING

No domínio de trading, a camada probabilística deve apoiar:

* comparação de hipóteses;
* avaliação de cenários;
* análise de evidências;
* atualização diante de novos dados;
* análise de regimes;
* avaliação de invalidação;
* análise de distribuição de resultados;
* avaliação de assimetria;
* análise de risco;
* calibração histórica.

Ela não deve transformar:

> padrão visual

em:

> probabilidade objetiva de movimento.

---

# 81. TRADING — SEPARAÇÃO COGNITIVA

Uma estrutura possível é:

**Observação**

→ **Interpretação**

→ **Hipóteses**

→ **Evidências**

→ **Cenários**

→ **Probabilidades ou plausibilidades**

→ **Invalidação**

→ **Consequências**

→ **Decisão**

A sequência é uma arquitetura cognitiva possível, não uma sequência obrigatória.

O agente pode descobrir que determinada situação exige outra decomposição.

---

# 82. TRADING — REGIME

Uma probabilidade histórica pode perder validade quando:

* volatilidade muda;
* liquidez muda;
* sessão muda;
* estrutura de mercado muda;
* comportamento dos participantes muda;
* regime macro muda;
* mecanismo subjacente muda.

O agente deve perguntar, quando pertinente:

> “A distribuição que sustenta essa estimativa ainda é representativa?”

---

# 83. TRADING — BACKTEST

Backtest pode fornecer evidência probabilística, mas não garante equivalência futura.

O agente deve considerar:

* overfitting;
* seleção do período;
* seleção de ativos;
* custos;
* liquidez;
* regime;
* look-ahead bias;
* sobrevivência;
* múltiplos testes;
* degradação temporal.

---

# 84. TRADING — PROBABILIDADE NÃO É SINAL

Um sinal pode indicar:

> “há evidência compatível com H.”

Isso não significa:

> “H ocorrerá com probabilidade X.”

A probabilidade depende do conjunto de condições, histórico, modelo e evidências utilizados.

---

# 85. TRADING — INVALidação

Uma estimativa probabilística deve permanecer aberta à invalidação.

Se uma premissa crítica for quebrada, o agente deve poder:

* reduzir confiança;
* alterar distribuição;
* eliminar cenário;
* criar novo cenário;
* interromper análise;
* buscar informação adicional.

---

# 86. MULTIAGENTE

Em sistemas com múltiplos agentes, diferentes agentes podem produzir:

* estimativas diferentes;
* modelos diferentes;
* hipóteses diferentes;
* distribuições diferentes.

Discordância não deve ser automaticamente resolvida por consenso.

Ela pode indicar:

* diferença de evidência;
* diferença semântica;
* diferença ontológica;
* diferença causal;
* diferença de regime;
* diferença de prior;
* erro de um ou mais agentes.

---

# 87. AGREGAÇÃO

Quando necessário, estimativas podem ser comparadas ou agregadas.

Mas o agente deve considerar:

* dependência entre agentes;
* origem comum das informações;
* especialização;
* qualidade;
* calibração;
* contexto.

Cinco agentes que utilizaram a mesma evidência não equivalem necessariamente a cinco evidências independentes.

---

# 88. DIVERGÊNCIA COMO INFORMAÇÃO

Uma divergência significativa entre modelos pode ser mais informativa que uma falsa convergência.

O agente deve ser capaz de perguntar:

> “O que explica a divergência?”

Essa pergunta pode revelar:

* premissa oculta;
* variável omitida;
* diferença semântica;
* diferença temporal;
* diferença de regime;
* erro de dados.

---

# 89. HORIZONTE

Toda probabilidade relevante deve preservar o horizonte quando este alterar materialmente o resultado.

Uma estimativa sem horizonte pode ser semanticamente incompleta.

---

# 90. ATUALIZAÇÃO CONTÍNUA

Probabilidades não devem ser tratadas como estados permanentes.

Quando novas informações relevantes aparecem, o agente pode:

* atualizar;
* reduzir;
* aumentar;
* redistribuir;
* abandonar;
* criar novas hipóteses.

A atualização deve ser proporcional à força da nova evidência.

---

# 91. PERSISTÊNCIA DE CRENÇA

O agente não deve alterar uma estimativa simplesmente porque recebeu qualquer informação nova.

Informação nova precisa ser:

* relevante;
* suficientemente confiável;
* interpretável;
* capaz de alterar a hipótese.

Isso evita volatilidade cognitiva.

---

# 92. ESTABILIDADE E ADAPTABILIDADE

Um bom sistema probabilístico deve equilibrar:

**estabilidade**

e

**capacidade de atualização.**

Atualizar demais gera instabilidade.

Atualizar de menos gera rigidez.

---

# 93. PROBABILIDADE E APRENDIZADO

Após resultados observados, o agente deve ser capaz de comparar:

> previsão probabilística

com

> resultado real.

Isso permite identificar:

* calibração;
* erro sistemático;
* viés;
* mudança de regime;
* inadequação do modelo.

---

# 94. RESULTADO NÃO VALIDA AUTOMATICAMENTE A ESTIMATIVA

Se um evento de 10% acontecer, isso não significa que a estimativa estava errada.

Se um evento de 90% não acontecer, isso também não significa automaticamente que a estimativa estava errada.

A avaliação deve ocorrer em séries de casos comparáveis.

---

# 95. QUALIDADE PROBABILÍSTICA

A qualidade de uma representação probabilística deve considerar:

1. definição do evento;
2. adequação do contexto;
3. qualidade da evidência;
4. adequação do modelo;
5. calibração;
6. coerência;
7. sensibilidade;
8. robustez;
9. transparência;
10. capacidade de atualização;
11. adequação da precisão;
12. utilidade decisional.

---

# 96. ECONOMICIDADE

O raciocínio probabilístico deve utilizar profundidade proporcional ao valor da decisão.

Não é necessário construir um modelo probabilístico sofisticado para uma decisão trivial.

Da mesma forma, uma decisão de alto impacto pode justificar:

* múltiplos modelos;
* cenários;
* análise de sensibilidade;
* testes adversariais;
* validação externa;
* avaliação de cauda;
* calibração histórica.

---

# 97. EFICIÊNCIA

A camada deve evitar:

* cálculo desnecessário;
* falsa precisão;
* modelagem excessiva;
* atualização irrelevante;
* exploração infinita de cenários.

A pergunta orientadora é:

> “Qual representação probabilística adicional realmente melhora a qualidade cognitiva?”

---

# 98. EFICÁCIA

Uma representação probabilística é eficaz quando melhora:

* diferenciação entre hipóteses;
* avaliação de alternativas;
* atualização de crenças;
* percepção de risco;
* identificação de incertezas;
* qualidade da decisão.

Complexidade matemática sem ganho cognitivo não representa eficácia.

---

# 99. EFETIVIDADE

A efetividade deve ser avaliada pelo comportamento do sistema ao longo do tempo.

O agente deve aprender com:

* previsões;
* resultados;
* erros;
* mudanças de regime;
* falhas de modelo;
* calibração.

A pergunta não é apenas:

> “O cálculo estava correto?”

Mas:

> “O uso da probabilidade melhorou o comportamento cognitivo?”

---

# 100. ANTIPADRÕES FUNDAMENTAIS

O Harness deve detectar ou reduzir:

### 100.1 Percentual ornamental

Número produzido apenas para parecer rigoroso.

### 100.2 Precisão fictícia

Estimativa mais precisa do que os dados permitem.

### 100.3 Certeza probabilística

Transformar alta probabilidade em certeza.

### 100.4 Probabilidade sem evento

Percentual sem definir o que está sendo estimado.

### 100.5 Probabilidade sem horizonte

Estimativa temporalmente ambígua.

### 100.6 Probabilidade sem condicionamento

Ignorar contexto relevante.

### 100.7 Independência presumida

Tratar evidências dependentes como independentes.

### 100.8 Modelo fechado

Assumir que todas as possibilidades relevantes foram identificadas.

### 100.9 Taxa-base rígida

Ignorar evidência nova.

### 100.10 Evidência dominante

Ignorar taxa-base e alternativas.

### 100.11 Narrativa probabilística

Confundir história convincente com probabilidade elevada.

### 100.12 Resultado retrospectivo

Avaliar uma probabilidade individual apenas pelo resultado posterior.

### 100.13 Quantificação obrigatória

Forçar percentual onde não existe fundamento.

### 100.14 Paralisia probabilística

Continuar analisando indefinidamente sem ganho decisional.

### 100.15 Probabilidade como decisão

Tratar maior probabilidade como escolha automaticamente correta.

---

# 101. TESTES COGNITIVOS

O Harness deve ser capaz de testar:

### Teste 1 — Definição

O evento probabilístico está definido?

### Teste 2 — Contexto

A estimativa depende de condições específicas?

### Teste 3 — Base

Existe referência ou taxa-base relevante?

### Teste 4 — Evidência

Qual evidência sustenta a estimativa?

### Teste 5 — Independência

As evidências são realmente independentes?

### Teste 6 — Modelo

Qual modelo sustenta a estimativa?

### Teste 7 — Alternativas

Existem hipóteses concorrentes?

### Teste 8 — Sensibilidade

Quais premissas alteram significativamente o resultado?

### Teste 9 — Regime

O contexto atual é comparável ao histórico?

### Teste 10 — Precisão

A precisão apresentada é justificável?

### Teste 11 — Cauda

Existe resultado raro materialmente relevante?

### Teste 12 — Atualização

Que evidência faria a estimativa mudar?

### Teste 13 — Calibração

A estimativa pode ser posteriormente confrontada com resultados?

### Teste 14 — Utilidade

A quantificação realmente melhora a decisão?

---

# 102. TESTE DE NÃO RESTRIÇÃO COGNITIVA

Este é um teste fundamental do Harness.

A especificação deve permitir que o agente:

* descubra novas variáveis;
* crie novas hipóteses;
* rejeite o espaço probabilístico inicial;
* proponha novas categorias;
* reconheça que probabilidades não são aplicáveis;
* substitua um modelo;
* crie modelos concorrentes;
* reformule o evento;
* altere o horizonte;
* descubra dependências;
* identifique mudança de regime;
* abandone uma quantificação;
* introduza cenários não previstos;
* conclua que o espaço de possibilidades está incompleto.

Se o Harness impedir essas operações, ele não está ampliando a cognição.

Está restringindo-a.

---

# 103. TESTE DE DESCOBERTA

O agente deve poder chegar a:

> “A variável mais importante não estava originalmente no modelo.”

Essa possibilidade deve ser considerada sinal de capacidade cognitiva, não falha automática.

---

# 104. TESTE DE REFORMULAÇÃO

O agente deve poder concluir:

> “A pergunta probabilística original estava mal formulada.”

Nesse caso, deve ser capaz de reformular:

* evento;
* variável;
* população;
* horizonte;
* hipótese;
* condição.

---

# 105. TESTE DE NÃO QUANTIFICAÇÃO

O agente deve poder concluir:

> “Não há base suficiente para fornecer uma probabilidade numérica confiável.”

Isso não representa falha.

Pode representar boa calibração epistemológica.

---

# 106. TESTE DE CONFLITO

O agente deve poder manter simultaneamente:

* hipótese A;
* hipótese B;
* hipótese C;

quando as evidências não permitirem resolução adequada.

Não deve fabricar convergência.

---

# 107. TESTE DE MUDANÇA DE MODELO

Quando novas evidências contradizem estruturalmente o modelo, o agente deve poder substituir o modelo em vez de apenas ajustar seus parâmetros.

---

# 108. TESTE DE SURPRESA

Quando ocorrer resultado incompatível com as expectativas, o agente deve perguntar:

> “Foi apenas um evento raro ou existe evidência de que meu modelo está errado?”

Essa distinção é fundamental.

---

# 109. RELAÇÃO COM A ONTOLOGIA

A ontologia define:

> o que existe ou pode ser representado.

A probabilidade qualifica:

> quão plausível é determinado estado/evento dentro do espaço representado.

Se a ontologia estiver incompleta, o modelo probabilístico também poderá estar incompleto.

---

# 110. RELAÇÃO COM A SEMÂNTICA

A semântica determina:

> o que significa o evento probabilístico.

Sem semântica adequada:

> “70%”

pode ser matematicamente correto e cognitivamente vazio.

---

# 111. RELAÇÃO COM A CAUSALIDADE

A causalidade procura mecanismos.

A probabilidade qualifica incertezas sobre eventos e estados.

Uma não substitui a outra.

---

# 112. RELAÇÃO COM CONTRAFACTUAIS

O contrafactual expande:

> “o que poderia ocorrer se...”

A probabilidade pode qualificar:

> “quão plausível é cada alternativa sob determinadas condições?”

---

# 113. RELAÇÃO COM INCERTEZA

A incerteza determina:

> onde o conhecimento é limitado.

A probabilidade fornece, quando possível:

> uma representação quantitativa ou qualitativa dessa limitação.

Nem toda incerteza deve ser probabilizada.

---

# 114. RELAÇÃO COM DECISÃO

A probabilidade fornece informação sobre alternativas e consequências.

A decisão integra essa informação com:

* objetivos;
* consequências;
* restrições;
* preferências;
* risco;
* reversibilidade;
* autoridade.

---

# 115. RELAÇÃO COM METACOGNIÇÃO

A metacognição monitora:

* qualidade da estimativa;
* confiança;
* premissas;
* sensibilidade;
* limitações;
* necessidade de atualização.

A probabilidade fornece uma das representações que a metacognição pode avaliar.

---

# 116. ARQUITETURA COGNITIVA INTEGRADA

As camadas podem ser compreendidas como capacidades complementares:

**Ontologia**
→ O que está sendo representado?

**Semântica**
→ O que isso significa?

**Causalidade**
→ O que pode produzir o quê?

**Contrafactuais**
→ O que poderia acontecer sob outras condições?

**Incerteza**
→ O que não sabemos e por quê?

**Probabilidade**
→ Como podemos representar quantitativa ou qualitativamente essa incerteza?

**Decisão**
→ O que fazer diante dessas possibilidades?

**Metacognição**
→ Quão confiável é o próprio processo utilizado?

A sequência não deve ser interpretada como pipeline rígido.

As capacidades podem operar:

* simultaneamente;
* iterativamente;
* recursivamente;
* em ordens diferentes;
* de forma parcial.

---

# 117. PRINCÍPIO DE SOBERANIA COGNITIVA

Nenhuma fórmula probabilística deve possuir autoridade absoluta sobre a cognição.

O agente pode:

* rejeitar o modelo;
* questionar os dados;
* reformular o evento;
* descobrir uma variável;
* contestar a distribuição;
* abandonar a quantificação;
* criar outra representação.

---

# 118. PRINCÍPIO DA PROPORCIONALIDADE

Quanto maior:

* impacto;
* irreversibilidade;
* exposição;
* incerteza;
* consequência potencial;

maior pode ser a necessidade de análise probabilística aprofundada.

Mas complexidade adicional somente deve ser utilizada quando possuir valor cognitivo.

---

# 119. PRINCÍPIO DA TRANSPARÊNCIA

Quando uma probabilidade for material para uma decisão, deve ser possível identificar, em nível adequado:

* o que está sendo estimado;
* sob quais condições;
* qual evidência sustenta;
* quais são as principais premissas;
* quais são as principais limitações;
* o que poderia alterar a estimativa.

---

# 120. PRINCÍPIO DA REVERSIBILIDADE

Estimativas devem permanecer revisáveis.

Nenhuma probabilidade deve tornar-se uma crença permanente simplesmente porque foi registrada anteriormente.

---

# 121. PRINCÍPIO DA ECONOMICIDADE COGNITIVA

O agente deve buscar:

> **a menor complexidade probabilística capaz de produzir representação suficientemente boa para a finalidade.**

Nem simplificação excessiva.

Nem sofisticação ornamental.

---

# 122. PRINCÍPIO DA SUFICIÊNCIA

A análise deve parar quando a informação probabilística adicional não possuir valor material suficiente para:

* melhorar compreensão;
* diferenciar hipóteses;
* alterar decisão;
* reduzir risco;
* melhorar robustez.

---

# 123. PRINCÍPIO DA ABERTURA

O espaço probabilístico deve permanecer aberto à descoberta.

O agente pode descobrir:

* novo evento;
* nova variável;
* nova dependência;
* novo regime;
* novo modelo;
* novo cenário;
* nova hipótese.

---

# 124. PRINCÍPIO DA CALIBRAÇÃO

A intensidade da confiança deve ser proporcional à qualidade da evidência e à estabilidade do modelo.

Quanto mais frágil:

* evidência;
* modelo;
* generalização;
* regime;

menor deve ser a confiança injustificada.

---

# 125. PRINCÍPIO DA MODÉSTIA MATEMÁTICA

Matemática sofisticada não deve ser utilizada para esconder ignorância.

Um modelo simples e explicitamente limitado pode ser cognitivamente superior a um modelo complexo cuja validade não possa ser defendida.

---

# 126. PRINCÍPIO DA FLEXIBILIDADE REPRESENTACIONAL

O agente pode utilizar:

* números;
* intervalos;
* distribuições;
* rankings;
* categorias qualitativas;
* cenários;
* árvores;
* comparações;
* representações híbridas.

A representação deve ser escolhida pela adequação ao problema.

---

# 127. PRINCÍPIO DA NÃO FETICHIZAÇÃO DO NÚMERO

O número não possui autoridade simplesmente por ser número.

Uma afirmação qualitativa bem fundamentada pode ser superior a uma porcentagem arbitrária.

---

# 128. PRINCÍPIO DA CONSEQUÊNCIA

A importância de uma probabilidade não depende apenas de seu valor.

Deve-se considerar:

> probabilidade × consequência × exposição × reversibilidade.

Uma probabilidade pequena pode ser decisionalmente relevante.

---

# 129. PRINCÍPIO DA APRENDIZAGEM

Toda previsão probabilística suficientemente importante deve, quando possível, permitir comparação posterior entre:

* expectativa;
* evidência;
* resultado.

Isso permite melhorar:

* modelo;
* calibração;
* estratégia;
* seleção de evidências;
* reconhecimento de regimes.

---

# 130. PRINCÍPIO DA AUTO-INVALIDAÇÃO

O agente deve conseguir responder:

> “O que precisaria ser observado para que eu abandonasse essa estimativa?”

Uma probabilidade sem possibilidade de revisão pode transformar-se em racionalização.

---

# 131. PRINCÍPIO DA COGNIÇÃO ABERTA

O Harness não deve estabelecer previamente:

* número máximo de hipóteses;
* número obrigatório de cenários;
* distribuição obrigatória;
* percentual obrigatório;
* fórmula universal;
* fonte obrigatória;
* método único de inferência.

Esses elementos devem permanecer disponíveis como capacidades.

---

# 132. O QUE O HARNESS DEVE GARANTIR

O Harness deve garantir capacidade para:

* representar incerteza probabilisticamente quando apropriado;
* não probabilizar quando inadequado;
* comparar hipóteses;
* atualizar crenças;
* detectar dependências;
* considerar taxas-base;
* avaliar sensibilidade;
* reconhecer mudanças de regime;
* representar caudas;
* preservar alternativas;
* reconhecer limitações;
* calibrar confiança;
* revisar modelos;
* aprender com resultados;
* preservar descoberta.

---

# 133. O QUE O HARNESS NÃO DEVE DETERMINAR

O Harness não deve determinar:

* qual hipótese acreditar;
* qual probabilidade atribuir em toda situação;
* qual modelo utilizar universalmente;
* qual distribuição usar sempre;
* qual decisão tomar;
* qual estratégia de raciocínio seguir;
* quantos cenários gerar;
* qual resultado “deve” ocorrer.

---

# 134. CRITÉRIOS DE QUALIDADE

A Camada Probabilística deve ser avaliada por:

| Critério       | Pergunta                                    |
| -------------- | ------------------------------------------- |
| Definição      | O evento está claro?                        |
| Contexto       | As condições relevantes foram preservadas?  |
| Evidência      | Existe fundamento suficiente?               |
| Dependência    | As evidências são realmente independentes?  |
| Modelo         | O modelo é adequado ao problema?            |
| Calibração     | Confiança e frequência são compatíveis?     |
| Robustez       | A conclusão resiste a variações plausíveis? |
| Sensibilidade  | As premissas críticas são conhecidas?       |
| Adaptabilidade | O modelo pode mudar?                        |
| Descoberta     | Novas hipóteses podem surgir?               |
| Economicidade  | A complexidade é justificável?              |
| Utilidade      | A probabilidade melhora a cognição?         |

---

# 135. TESTE MÁXIMO DE QUALIDADE

A camada deve conseguir responder simultaneamente:

> **“Qual é a melhor representação probabilística que consigo construir com as informações disponíveis?”**

e:

> **“Quais são as razões para acreditar que essa própria representação pode estar errada?”**

A segunda pergunta impede que o modelo se transforme em dogma.

---

# 136. TESTE MÁXIMO DE COGNIÇÃO

O agente deve poder concluir:

> “Não existe fundamento suficiente para uma probabilidade confiável.”

Ou:

> “O evento está mal definido.”

Ou:

> “O modelo está errado.”

Ou:

> “Existe uma variável desconhecida.”

Ou:

> “Existem múltiplos regimes.”

Ou:

> “A melhor representação é qualitativa.”

Ou:

> “Precisamos descobrir mais antes de quantificar.”

Essas conclusões devem ser consideradas manifestações legítimas de cognição.

---

# 137. TESTE MÁXIMO DE LIBERDADE

Se uma situação nova surgir e não estiver contemplada nesta especificação, o agente deve poder:

1. identificar a novidade;
2. criar uma representação adequada;
3. formular hipóteses;
4. determinar se probabilização é apropriada;
5. escolher a representação;
6. testar suas próprias premissas;
7. revisar o modelo;
8. produzir uma nova abordagem.

A especificação não pode impedir esse comportamento.

---

# 138. REGRA DE OURO

> **A probabilidade deve ampliar a capacidade do agente de raciocinar sob incerteza, e nunca transformar incerteza em falsa precisão.**

---

# 139. PRINCÍPIO MESTRE

> **A Camada Probabilística deve permitir que o agente represente, compare, atualize e comunique graus de possibilidade e crença de maneira contextualizada, calibrada, revisável e proporcional à qualidade da informação, preservando hipóteses concorrentes, dependências, mudanças de regime, consequências e incertezas estruturais, sem impor quantificação obrigatória, modelos universais ou decisões predeterminadas.**

---

# 140. CRITÉRIO FINAL DE ACEITAÇÃO

A especificação será considerada cognitivamente adequada somente se o Harness permitir que o agente:

* quantifique quando houver fundamento;
* não quantifique quando não houver;
* diferencie possibilidade de probabilidade;
* diferencie probabilidade de certeza;
* diferencie probabilidade de decisão;
* diferencie evidência de interpretação;
* compare hipóteses concorrentes;
* reconheça dependências;
* considere taxa-base;
* atualize crenças;
* reconheça mudanças de regime;
* considere eventos raros e caudas;
* avalie sensibilidade;
* reconheça incerteza estrutural;
* preserve alternativas;
* revise modelos;
* aprenda com resultados;
* descubra novas variáveis;
* reformule o problema;
* abandone modelos inadequados;
* preserve sua capacidade cognitiva diante de situações não previstas.

### Condição fundamental

> **O Harness deve aumentar a qualidade do raciocínio probabilístico do LLM sem reduzir a liberdade do LLM para descobrir que o problema não é, afinal, um problema probabilístico.**

Essa é a fronteira entre:

**um Harness que ensina o agente a pensar melhor**

e

**um Harness que apenas obriga o agente a seguir uma fórmula.**
