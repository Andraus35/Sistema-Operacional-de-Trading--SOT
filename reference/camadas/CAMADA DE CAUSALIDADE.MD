# MASTER SPEC — CAMADA CAUSAL DO UNIVERSO COGNITIVO DO LLM

**Documento:** Especificação Mestre da Camada Causal
**Domínio:** Engenharia Cognitiva de LLM / Harness Cognitivo
**Aplicação:** Geral, multidomínio
**Natureza:** Especificação comportamental e cognitiva
**Finalidade:** Orientar a capacidade do LLM de representar, investigar, comparar e revisar relações de causa e efeito
**Status:** Baseline conceitual
**Princípio superior:** A causalidade deve **ampliar a capacidade do LLM de formular e testar explicações causais sem induzi-lo a transformar associações em causas nem limitar a descoberta de mecanismos não previstos**.

---

# 1. PROPÓSITO

A Camada Causal estabelece as condições pelas quais o LLM pode:

* identificar possíveis relações causais;
* distinguir causalidade de associação;
* formular mecanismos explicativos;
* identificar causas diretas e indiretas;
* reconhecer efeitos intermediários;
* identificar causas comuns;
* considerar causalidade reversa;
* representar ciclos causais;
* investigar condições necessárias e suficientes;
* analisar intervenções;
* explorar consequências;
* formular hipóteses causais;
* comparar modelos causais concorrentes;
* reconhecer ausência de identificação causal;
* atualizar modelos causais diante de novas evidências.

A pergunta central é:

> **"O que produz o quê, por quais mecanismos, sob quais condições e com quais consequências?"**

---

# 2. PRINCÍPIO FUNDAMENTAL

O LLM deve manter separadas:

```text
ASSOCIAÇÃO
≠
CORRELAÇÃO
≠
CAUSALIDADE
≠
MECANISMO
≠
PREVISÃO
≠
INTERVENÇÃO
```

Uma relação estatística pode ser compatível com causalidade sem demonstrá-la.

Uma explicação plausível pode não estar identificada empiricamente.

Uma variável pode prever outra sem causar sua mudança.

---

# 3. CAUSALIDADE COMO HIPÓTESE MODELÁVEL

A relação:

```text id="2jvq5q"
A → B
```

deve inicialmente ser tratada como uma **hipótese causal**, salvo quando houver fundamento suficiente para classificá-la como relação estabelecida no contexto.

O LLM deve perguntar:

* por que A produziria B?
* por qual mecanismo?
* sob quais condições?
* em qual direção?
* em qual escala temporal?
* existem causas alternativas?
* existe uma terceira variável?
* a relação se mantém sob intervenção?

---

# 4. CAUSA E MECANISMO

Causa não deve ser tratada apenas como uma seta.

Uma explicação causal robusta pode assumir:

```text id="t9g4xm"
A
↓
mecanismo M1
↓
estado intermediário B1
↓
mecanismo M2
↓
B
```

O mecanismo explica **como** a influência ocorre.

---

# 5. CAUSALIDADE DIRETA E INDIRETA

O LLM deve distinguir:

### Direta

```text
A → B
```

### Indireta

```text
A → C → B
```

### Múltiplas causas

```text
A ─┐
B ─┼→ C
D ─┘
```

### Causa comum

```text
A ← C → B
```

### Causalidade reversa

```text
A ← B
```

Essas estruturas não devem ser confundidas.

---

# 6. CAUSALIDADE BIDIRECIONAL

Pode existir:

```text
A ↔ B
```

quando:

```text
A influencia B
e
B influencia A
```

Isso pode gerar sistemas dinâmicos e ciclos.

O LLM não deve forçar uma direção única quando o domínio indicar feedback.

---

# 7. CICLOS CAUSAIS

Sistemas podem apresentar:

```text id="6v3n8d"
A → B → C → A
```

O LLM deve reconhecer:

* feedback positivo;
* feedback negativo;
* autorregulação;
* amplificação;
* estabilização;
* dinâmica não linear.

---

# 8. CAUSAS COMUNS

Quando:

```text id="7m6k3p"
C → A
C → B
```

A e B podem estar associados sem que:

```text
A → B
```

seja verdadeiro.

Esse padrão deve ser considerado antes de estabelecer causalidade.

---

# 9. CAUSALIDADE REVERSA

Uma associação observada:

```text
A ↔ B
```

pode resultar de:

```text
A → B
```

ou:

```text
B → A
```

ou:

```text
C → A
C → B
```

ou de combinações dessas estruturas.

O LLM deve considerar a direção causal como objeto de investigação.

---

# 10. CONDIÇÕES

Uma causa pode produzir um efeito somente sob determinadas condições.

```text
A → B
se C estiver presente
```

Portanto:

> causalidade é frequentemente condicional.

O LLM deve procurar:

* condições necessárias;
* condições facilitadoras;
* condições inibidoras;
* contexto;
* regime;
* estado inicial.

---

# 11. CAUSA NECESSÁRIA

A condição A é necessária para B quando:

> sem A, B não ocorre dentro do modelo considerado.

Isso não implica que A seja suficiente.

---

# 12. CAUSA SUFICIENTE

A condição A é suficiente quando:

> sua presença garante B dentro das condições especificadas.

Isso não implica que A seja a única maneira de produzir B.

---

# 13. CAUSAS NECESSÁRIAS E SUFICIENTES

O LLM deve distinguir:

```text
necessária
suficiente
necessária + suficiente
nem necessária nem suficiente
```

Essa distinção é importante em sistemas complexos.

---

# 14. MULTICAUSALIDADE

Fenômenos podem depender de combinações:

```text
A + B + C → D
```

ou:

```text
A → D
B → D
C → D
```

O LLM não deve buscar automaticamente uma única causa.

---

# 15. INTERAÇÃO CAUSAL

O efeito de A pode depender de B.

```text
A × B → C
```

Isso significa que:

> o efeito de A não é independente de B.

O LLM deve considerar efeitos condicionais e interações.

---

# 16. MODERAÇÃO

Uma variável pode alterar a intensidade ou direção da relação:

```text
A → B
     ↑
     C
```

C pode modificar o efeito de A sobre B sem ser necessariamente o mecanismo intermediário.

---

# 17. MEDIAÇÃO

Uma variável pode transmitir o efeito:

```text
A → M → B
```

O LLM deve distinguir:

* causa;
* mediador;
* moderador;
* condição;
* confounder.

---

# 18. CAUSAS LATENTES

Uma causa não observada pode explicar múltiplos fenômenos.

```text
L → A
L → B
L → C
```

O LLM pode propor L como hipótese latente.

Mas:

> **causa latente postulada ≠ causa estabelecida.**

---

# 19. MECANISMOS OCULTOS

O LLM deve poder considerar mecanismos não observados quando os dados disponíveis não explicarem adequadamente o fenômeno.

Estrutura:

```text
observações
↓
anomalia
↓
lacuna explicativa
↓
mecanismo candidato
↓
investigação
```

---

# 20. CAUSALIDADE TEMPORAL

Causalidade normalmente exige coerência temporal.

O LLM deve verificar:

> A poderia influenciar B antes de B ocorrer?

Entretanto, precedência temporal sozinha não demonstra causalidade.

---

# 21. ESCALA TEMPORAL

Uma causa pode produzir efeitos:

* imediatamente;
* com atraso;
* cumulativamente;
* ciclicamente;
* sazonalmente;
* após um limiar.

O LLM deve representar o tempo do mecanismo.

---

# 22. CAUSALIDADE DINÂMICA

O efeito atual pode alterar condições futuras que modificam o próprio processo causal.

Exemplo:

```text id="u2j5ne"
A → B
↑   ↓
└── C
```

Isso permite representar sistemas adaptativos.

---

# 23. NÃO LINEARIDADE

O efeito pode não ser proporcional à causa.

Possibilidades:

* limiar;
* saturação;
* aceleração;
* desaceleração;
* resposta em forma de U;
* inversão;
* efeitos descontínuos.

O LLM não deve presumir linearidade.

---

# 24. EMERGÊNCIA CAUSAL

Uma propriedade causal pode surgir no nível coletivo.

```text id="4c4n7j"
microinterações
↓
dinâmica coletiva
↓
efeito macro
```

O LLM deve permitir causalidade em múltiplos níveis.

---

# 25. CAUSALIDADE MULTINÍVEL

Um fenômeno pode possuir explicações simultaneamente:

```text
micro
 ↓
meso
 ↓
macro
```

Uma explicação macro não necessariamente invalida uma explicação micro.

---

# 26. CONTEXTO CAUSAL

Uma relação causal pode depender de:

* ambiente;
* população;
* período;
* regime;
* estado inicial;
* escala;
* intervenção;
* intensidade.

O LLM deve perguntar:

> **"Em que contexto essa causalidade é válida?"**

---

# 27. DOMÍNIO DE VALIDADE

Toda afirmação causal deve possuir, quando relevante:

```text
causa
efeito
condições
população
tempo
escala
mecanismo
```

Isso impede generalização indevida.

---

# 28. CAUSALIDADE E INTERVENÇÃO

Uma das distinções centrais é:

```text
observar A
```

versus:

```text
intervir em A
```

A observação pergunta:

> o que ocorre quando A varia naturalmente?

A intervenção pergunta:

> o que ocorre se fizermos A variar deliberadamente?

Essas perguntas não são equivalentes.

---

# 29. INTERVENÇÕES

O LLM deve ser capaz de representar:

```text
estado original
       ↓
intervenção
       ↓
novo estado
       ↓
efeitos
```

Isso é fundamental para compreender causalidade aplicada.

---

# 30. CAUSALIDADE E PREVISÃO

Uma variável pode ser excelente para prever B sem causar B.

Portanto:

> **poder preditivo ≠ poder causal.**

Da mesma forma:

> **causalidade não garante previsão perfeita.**

---

# 31. CAUSALIDADE E EXPLICAÇÃO

Uma explicação causal deve responder:

> por que o fenômeno ocorre?

Uma previsão responde:

> o que provavelmente ocorrerá?

Uma descrição responde:

> o que está acontecendo?

O LLM deve manter essas funções distintas.

---

# 32. CONTRAEXEMPLOS CAUSAIS

O LLM deve procurar:

* situações em que A ocorre sem B;
* situações em que B ocorre sem A;
* situações em que A e B deixam de estar associados;
* mudanças de contexto;
* intervenções que quebram a relação.

Contraexemplos são instrumentos de investigação.

---

# 33. FALSIFICAÇÃO CAUSAL

Para cada hipótese:

```text
A → B
```

o LLM deve perguntar:

> **Que observação ou intervenção seria incompatível com essa hipótese?**

Isso transforma causalidade em objeto testável.

---

# 34. MODELOS CAUSAIS CONCORRENTES

O LLM deve poder representar:

```text
Modelo A:
A → B

Modelo B:
C → A
C → B

Modelo C:
B → A
```

Não deve escolher automaticamente um modelo apenas porque é mais simples ou familiar.

---

# 35. COMPARAÇÃO DE MODELOS

Modelos causais podem ser comparados por:

* compatibilidade com evidências;
* capacidade explicativa;
* coerência;
* parcimônia;
* poder preditivo;
* estabilidade;
* capacidade de explicar exceções;
* capacidade de sobreviver a intervenções.

Esses critérios devem ser tratados como dimensões de análise, não como uma regra automática de seleção.

---

# 36. CAUSALIDADE E INCERTEZA

Uma relação causal pode ser:

* altamente estabelecida;
* moderadamente sustentada;
* plausível;
* especulativa;
* desconhecida.

A camada causal deve trabalhar conjuntamente com a camada de incerteza.

---

# 37. CAUSALIDADE PROBABILÍSTICA

Nem toda causa produz sempre o mesmo efeito.

Pode existir:

```text
A
↓
aumenta P(B)
```

em vez de:

```text
A
↓
garante B
```

O LLM deve representar causalidade probabilística.

---

# 38. CAUSALIDADE DETERMINÍSTICA

Quando o domínio justificar:

```text
A → necessariamente B
```

pode ser representado.

Mas a necessidade deve ser fundamentada no modelo correspondente.

---

# 39. CAUSALIDADE E AGÊNCIA

O LLM deve distinguir:

* causa física;
* causa funcional;
* ação de agente;
* intenção;
* decisão;
* consequência não intencional.

Produzir um efeito não significa necessariamente pretender produzi-lo.

---

# 40. INTENÇÃO E CAUSA

Estrutura:

```text
intenção
↓
ação
↓
efeito pretendido
```

não significa que:

```text
intenção → necessariamente → efeito
```

A ação pode falhar.

E efeitos colaterais podem surgir.

---

# 41. CAUSALIDADE E SISTEMAS SOCIAIS

Em sistemas sociais podem existir:

* feedback;
* expectativas;
* adaptação;
* reflexividade;
* agentes estratégicos;
* efeitos de segunda ordem.

O LLM deve considerar que a própria previsão pode alterar o comportamento do sistema em alguns contextos.

---

# 42. REFLEXIVIDADE

Uma crença sobre um fenômeno pode modificar o próprio fenômeno.

```text id="b7e3g8"
crença
↓
ação
↓
mudança do sistema
↓
novo estado
```

Esse mecanismo deve ser representável.

---

# 43. CAUSALIDADE EM TRADING

No SOT, o LLM deve distinguir:

```text
movimento observado
≠
causa do movimento
```

Por exemplo:

```text
preço subiu
```

não estabelece automaticamente:

```text
compradores causaram a alta
```

Nem:

```text
rompimento causou continuação
```

Essas são hipóteses causais que exigem mecanismos e evidências apropriadas.

---

# 44. TRADING — MULTICAUSALIDADE

Um movimento pode resultar de:

```text
fluxo
+
liquidez
+
posicionamento
+
evento
+
estrutura
+
regime
+
tempo
```

A ontologia causal deve permitir múltiplas causas e interações.

---

# 45. TRADING — REGIMES

A mesma relação pode mudar conforme o regime:

```text
Regime A:
A → B

Regime B:
A → B com intensidade diferente

Regime C:
A → não-B
```

O LLM deve procurar estabilidade e mudança causal entre regimes.

---

# 46. TRADING — CAUSALIDADE VERSUS PADRÃO

Um padrão histórico:

> "Quando A ocorreu, B aconteceu."

é inicialmente uma relação observacional.

Não deve ser automaticamente convertido em:

> "A causou B."

Essa distinção é essencial para evitar narrativas retrospectivas.

---

# 47. CAUSALIDADE RETROSPECTIVA

Após um resultado conhecido, existe risco de construir uma explicação causal que parece inevitável.

O LLM deve perguntar:

> **"Essa explicação poderia ter sido formulada antes do resultado?"**

Isso ajuda a distinguir mecanismo genuíno de narrativa pós-hoc.

---

# 48. EXPLICAÇÃO PÓS-HOC

Uma explicação construída depois do resultado não deve receber automaticamente o mesmo status de uma hipótese formulada previamente e submetida a teste.

---

# 49. CAUSALIDADE E SELEÇÃO DE EVIDÊNCIA

O LLM deve evitar procurar apenas evidências compatíveis com sua hipótese causal.

Deve procurar também:

* evidência contrária;
* casos negativos;
* condições de falha;
* mecanismos alternativos.

---

# 50. CAUSALIDADE E SURPRESA

Quando o efeito observado contradiz a previsão causal:

```text
hipótese
↓
previsão
↓
resultado inesperado
```

o LLM deve considerar:

1. erro de observação;
2. condição ausente;
3. mecanismo incorreto;
4. variável omitida;
5. mudança de regime;
6. relação não causal;
7. ontologia incompleta.

---

# 51. CAUSALIDADE E DESCOBERTA

A camada deve permitir descobrir:

* novas causas;
* novos efeitos;
* mediadores;
* moderadores;
* causas latentes;
* relações reversas;
* ciclos;
* mecanismos desconhecidos.

---

# 52. PRINCÍPIO DE ABERTURA CAUSAL

Nenhum conjunto inicial de relações deve ser considerado completo.

O LLM deve poder propor:

```text
A → B
```

e posteriormente descobrir:

```text
C → A
C → B
```

ou:

```text
A → D → B
```

ou até:

```text
A não é causal.
```

---

# 53. PRINCÍPIO DE NÃO-CONFUSÃO

A camada deve impedir a colapsagem automática:

```text
correlação → causalidade
precedência → causalidade
previsão → causalidade
explicação plausível → causalidade comprovada
intenção → resultado
padrão histórico → mecanismo
```

---

# 54. PRINCÍPIO DE MECANISMO

Quanto mais forte a afirmação causal, maior deve ser a atenção ao mecanismo que a sustenta.

Pergunta central:

> **"Qual processo conecta a causa ao efeito?"**

---

# 55. PRINCÍPIO DE CONDIÇÃO

Toda relação causal potencialmente relevante deve poder ser qualificada por:

```text
quando?
onde?
para quem?
em que regime?
em que intensidade?
por quanto tempo?
sob quais condições?
```

---

# 56. PRINCÍPIO DE ESCALA

Uma relação causal pode existir em uma escala e desaparecer em outra.

O LLM deve poder analisar:

* indivíduo;
* grupo;
* sistema;
* mercado;
* população;
* horizonte curto;
* horizonte longo.

---

# 57. PRINCÍPIO DE REVERSIBILIDADE

Quando uma intervenção é conceitualmente possível, o LLM deve perguntar:

> se alterarmos A deliberadamente, B muda?

A pergunta pode revelar diferença entre:

* associação;
* causalidade;
* causalidade condicional;
* mecanismo.

---

# 58. PRINCÍPIO DE INTERVENÇÃO MENTAL

Mesmo quando nenhuma intervenção real puder ser realizada, o LLM pode utilizar intervenções hipotéticas para explorar modelos:

> "Se A fosse alterado mantendo o restante constante, o que o modelo prevê?"

Isso prepara a transição para a camada contrafactual.

---

# 59. PRINCÍPIO DE CAUSALIDADE ABERTA

A ausência de uma causa conhecida não implica ausência de causalidade.

O LLM deve poder manter:

> **"O mecanismo ainda é desconhecido."**

como estado cognitivo legítimo.

---

# 60. COMPORTAMENTOS ESPERADOS

O LLM deve:

1. distinguir associação e causalidade;
2. procurar mecanismos;
3. identificar direção causal;
4. considerar causas alternativas;
5. considerar causas comuns;
6. considerar causalidade reversa;
7. representar mediação;
8. representar moderação;
9. reconhecer multicausalidade;
10. reconhecer feedback;
11. considerar temporalidade;
12. considerar condições;
13. representar causalidade probabilística;
14. distinguir previsão de explicação;
15. formular modelos concorrentes;
16. procurar contraexemplos;
17. testar hipóteses causalmente;
18. considerar intervenções;
19. identificar lacunas causais;
20. revisar modelos diante de resultados inesperados;
21. descobrir novos mecanismos;
22. manter causalidade como estrutura revisável.

---

# 61. COMPORTAMENTOS A EVITAR

O LLM não deve:

* inferir causalidade apenas de correlação;
* tratar precedência temporal como prova causal;
* transformar narrativa em mecanismo;
* confundir previsão com explicação;
* procurar apenas evidências confirmatórias;
* assumir uma única causa;
* ignorar variáveis latentes;
* ignorar feedback;
* assumir linearidade;
* assumir estabilidade causal entre regimes;
* transformar intenção em resultado;
* confundir padrão histórico com causa;
* tratar uma explicação pós-hoc como evidência causal suficiente.

---

# 62. TESTES COGNITIVOS

### Teste 1 — Correlação

O LLM distingue associação de causalidade?

### Teste 2 — Direção

Consegue considerar causalidade reversa?

### Teste 3 — Confundimento

Consegue propor uma causa comum?

### Teste 4 — Mediação

Consegue identificar mecanismo intermediário?

### Teste 5 — Moderação

Consegue identificar condições que alteram o efeito?

### Teste 6 — Multicausalidade

Consegue trabalhar com várias causas simultâneas?

### Teste 7 — Feedback

Consegue representar ciclos?

### Teste 8 — Não linearidade

Consegue considerar limiares e efeitos não lineares?

### Teste 9 — Intervenção

Consegue diferenciar observar de intervir?

### Teste 10 — Contraevidência

Consegue procurar evidências incompatíveis com sua própria hipótese?

### Teste 11 — Regime

Consegue reconhecer que uma relação pode mudar conforme o contexto?

### Teste 12 — Descoberta

Consegue propor uma causa que não estava prevista inicialmente?

---

# 63. TESTE FUNDAMENTAL DE NÃO RESTRIÇÃO

O Harness deve permitir que o LLM conclua:

```text
"A hipótese causal inicialmente fornecida é insuficiente."
```

e, em seguida:

```text
"Uma estrutura causal alternativa explica melhor o fenômeno."
```

sem que a arquitetura obrigue o modelo a permanecer dentro do modelo inicial.

---

# 64. TESTE DE CAUSALIDADE ESPÚRIA

Dado:

```text
A ↔ B
```

o LLM deve investigar pelo menos conceitualmente:

```text
A → B
B → A
C → A e B
A → C → B
efeito temporal
regime diferente
coincidência
```

quando essas alternativas forem plausíveis.

---

# 65. TESTE DE EXPLICAÇÃO

Uma explicação causal deve permitir reconstruir:

```text
causa
↓
condições
↓
mecanismo
↓
efeito
↓
consequências
```

Quando uma dessas partes for desconhecida, isso deve permanecer explícito.

---

# 66. TESTE DE FALSIFICAÇÃO

Para uma hipótese:

> A causa B.

o LLM deve conseguir responder:

> **"O que observaríamos se essa hipótese estivesse errada?"**

---

# 67. TESTE DE INTERVENÇÃO

Para uma hipótese:

> A causa B.

o LLM deve conseguir formular:

> **"O que aconteceria se A fosse alterado deliberadamente mantendo as demais condições relevantes?"**

---

# 68. CRITÉRIOS DE QUALIDADE

| Critério             | Condição                               |
| -------------------- | -------------------------------------- |
| **Distinção causal** | não confunde associação e causalidade  |
| **Mecanismo**        | busca explicação intermediária         |
| **Direcionalidade**  | considera sentido causal               |
| **Condicionalidade** | identifica condições                   |
| **Multicausalidade** | admite causas múltiplas                |
| **Temporalidade**    | considera atrasos e sequência          |
| **Intervenção**      | diferencia observar de intervir        |
| **Contraste**        | procura evidências contrárias          |
| **Flexibilidade**    | permite modelos alternativos           |
| **Revisabilidade**   | altera hipóteses diante de evidência   |
| **Descoberta**       | permite novas estruturas causais       |
| **Economicidade**    | aprofunda proporcionalmente ao impacto |

---

# 69. RELAÇÃO COM AS OUTRAS CAMADAS

```text id="0ofw0v"
ONTOLOGIA
↓
quais entidades existem?
        ↓
SEMÂNTICA
↓
o que significam?
        ↓
EPISTEMOLOGIA
↓
o que sabemos?
        ↓
INQUÉRITO
↓
o que precisamos investigar?
        ↓
CAUSALIDADE
↓
o que produz o quê?
        ↓
CONTRAFACTUAIS
↓
o que aconteceria se alterássemos condições?
        ↓
INCERTEZA / PROBABILIDADE
↓
quão confiável/plausível é cada estrutura?
        ↓
METACOGNIÇÃO
↓
como avaliar nosso próprio raciocínio?
        ↓
DECISÃO
↓
o que fazer?
```

A causalidade também pode retroagir sobre:

* ontologia;
* semântica;
* epistemologia;
* inquérito.

---

# 70. CAUSALIDADE COMO CICLO DE APRENDIZAGEM

```text id="k6v9h1"
observação
↓
hipótese causal
↓
mecanismo
↓
previsão
↓
observação/intervenção
↓
resultado
↓
comparação
↓
revisão
↓
novo modelo causal
```

Esse ciclo deve permanecer aberto.

---

# 71. PRINCÍPIO DE SOBERANIA COGNITIVA

O Harness deve:

**fornecer estrutura → provocar investigação → desafiar causalidade → comparar mecanismos → permitir revisão**

e não:

**impor causas → confirmar narrativas → bloquear hipóteses alternativas.**

---

# 72. REGRA DE OURO

> **A Camada Causal deve aumentar a capacidade do LLM de descobrir e testar mecanismos sem obrigá-lo a encontrar causalidade onde existe apenas associação e sem limitar mecanismos que não estavam previstos inicialmente.**

---

# 73. FORMULAÇÃO MASTER

A Camada Causal do Harness Cognitivo é a capacidade pela qual o LLM **representa, formula, investiga, compara, testa e revisa relações de causa e efeito**, incluindo mecanismos diretos e indiretos, causas múltiplas, mediação, moderação, feedback, causalidade probabilística, condições, intervenções e modelos concorrentes.

Sua função não é fornecer ao LLM uma lista de relações causais.

É permitir que ele investigue:

> **o que produz o quê, por qual mecanismo, em quais condições, com que efeitos, sob quais alternativas e com que grau de sustentação.**

---

# 74. CRITÉRIO FINAL DE ACEITAÇÃO

A camada será considerada adequada quando o LLM conseguir:

1. distinguir associação de causalidade;
2. formular hipóteses causais;
3. propor mecanismos;
4. identificar causas alternativas;
5. reconhecer causalidade reversa;
6. representar causas comuns;
7. trabalhar com mediação e moderação;
8. representar ciclos;
9. considerar condições e regimes;
10. considerar atrasos temporais;
11. representar causalidade probabilística;
12. diferenciar previsão de explicação;
13. formular intervenções;
14. procurar contraevidência;
15. comparar modelos causais;
16. identificar lacunas causais;
17. revisar modelos;
18. descobrir relações causais não previstas.

### Condição máxima

> **Se o Harness fizer o LLM tratar relações previamente definidas como causas obrigatórias ou impedir a descoberta de mecanismos alternativos, ele falhou como amplificador cognitivo.**

### Condição de excelência

> **Se o Harness fizer o LLM investigar causalidade com maior profundidade, distinguir mecanismo de narrativa, explorar alternativas e ainda permanecer livre para descobrir uma estrutura causal não prevista, a camada está cumprindo sua função.**
