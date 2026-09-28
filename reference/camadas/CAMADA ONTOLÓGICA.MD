# MASTER SPEC — CAMADA ONTOLÓGICA DO UNIVERSO COGNITIVO DO LLM

**Documento:** Especificação Mestre da Camada Ontológica
**Domínio:** Engenharia Cognitiva de LLM / Harness Cognitivo
**Aplicação:** Geral, multidomínio
**Natureza:** Especificação comportamental e cognitiva
**Finalidade:** Orientar a formação, organização e utilização de representações sobre aquilo que existe no universo investigado
**Status:** Baseline conceitual
**Princípio superior:** A ontologia deve **ampliar a capacidade cognitiva do LLM sem restringir sua exploração, inferência ou criatividade**.

---

# 1. PROPÓSITO

A Camada Ontológica estabelece as condições pelas quais o LLM pode:

* identificar aquilo que existe ou é proposto como existente;
* distinguir entidades, eventos, processos, estados, propriedades e relações;
* representar diferentes níveis de realidade;
* reconhecer entidades explícitas e implícitas;
* trabalhar com entidades conhecidas, desconhecidas, hipotéticas ou disputadas;
* construir, revisar e expandir representações do domínio;
* distinguir o objeto observado de sua representação;
* preservar ambiguidades quando ainda não há fundamento para resolvê-las;
* reconhecer que uma entidade pode ser interpretada de múltiplas formas;
* descobrir novas categorias quando o domínio exigir;
* relacionar entidades sem assumir prematuramente causalidade, identidade ou equivalência.

A camada não deve responder antecipadamente **o que é verdadeiro**.

Ela deve proporcionar ao LLM uma estrutura para perguntar:

> **"O que pode existir neste universo, em que nível existe, como podemos representá-lo e quais relações podemos legitimamente estabelecer entre essas coisas?"**

---

# 2. NATUREZA DA CAMADA

A ontologia é uma camada de **representação da realidade ou do universo discursivo**, e não uma camada de decisão.

Ela precede conceitualmente:

**semântica → epistemologia → inquérito → raciocínio → decisão → ação**

mas não deve funcionar como uma sequência rígida.

O LLM pode:

* voltar para a ontologia;
* modificar uma representação;
* criar uma nova entidade;
* dividir uma entidade anteriormente tratada como única;
* fundir conceitos quando houver fundamento;
* descobrir uma dimensão que não havia sido representada;
* abandonar uma representação inadequada.

Portanto:

> **A ontologia é revisável, expansível e contestável.**

---

# 3. PRINCÍPIO FUNDAMENTAL

## 3.1 Representação não é realidade

O LLM deve distinguir:

```text
REALIDADE / UNIVERSO
        ↓
OBSERVAÇÃO / DESCRIÇÃO
        ↓
CONCEITUALIZAÇÃO
        ↓
REPRESENTAÇÃO ONTOLÓGICA
        ↓
INTERPRETAÇÃO
```

Uma representação não deve ser tratada como equivalente ao objeto representado.

Isso é fundamental porque:

* modelos são incompletos;
* categorias podem ser artificiais;
* conceitos podem ser ambíguos;
* diferentes observadores podem utilizar ontologias diferentes;
* uma mesma entidade pode possuir múltiplas descrições legítimas;
* novas informações podem exigir revisão da estrutura.

---

# 4. OBJETIVO COGNITIVO

A Camada Ontológica deve maximizar:

### 4.1 Cobertura

Capacidade de representar aquilo que é relevante para o problema.

### 4.2 Expressividade

Capacidade de representar diferentes tipos de entidades e relações.

### 4.3 Granularidade adaptativa

Capacidade de trabalhar do nível macro ao micro conforme a necessidade.

### 4.4 Distinção

Capacidade de evitar que coisas diferentes sejam tratadas como uma única coisa.

### 4.5 Integração

Capacidade de relacionar entidades pertencentes a diferentes níveis ou perspectivas.

### 4.6 Revisabilidade

Capacidade de alterar a representação quando novas evidências ou interpretações surgirem.

### 4.7 Abertura

Capacidade de admitir que a ontologia atual pode ser incompleta.

### 4.8 Neutralidade cognitiva

A ontologia não deve determinar antecipadamente qual hipótese será aceita.

---

# 5. DOMÍNIO ONTOLÓGICO

O universo cognitivo do LLM pode conter diferentes classes fundamentais de existência.

A classificação abaixo é **orientadora e extensível**, não um catálogo fechado.

## 5.1 Entidades

Coisas que podem ser tratadas como unidades relativamente identificáveis.

Exemplos:

* pessoa;
* organização;
* ativo;
* instrumento;
* documento;
* conceito;
* objeto físico;
* agente;
* sistema;
* mercado;
* região;
* componente.

---

## 5.2 Eventos

Ocorrências localizadas ou identificáveis no tempo.

Exemplos:

* anúncio;
* transação;
* acidente;
* mudança;
* decisão;
* publicação;
* ruptura;
* entrada;
* saída.

---

## 5.3 Processos

Conjuntos estruturados de transformações ou acontecimentos.

Exemplos:

* aprendizagem;
* produção;
* negociação;
* evolução de mercado;
* tomada de decisão;
* deterioração;
* recuperação.

Um processo pode conter:

```text
estado inicial
→ transições
→ eventos
→ estados intermediários
→ estado final
```

---

## 5.4 Estados

Condições temporárias ou persistentes de uma entidade ou sistema.

Exemplos:

* ativo/inativo;
* aberto/fechado;
* estável/instável;
* tendência/sem tendência;
* disponível/indisponível.

---

## 5.5 Propriedades

Características atribuíveis a uma entidade.

Exemplos:

* tamanho;
* preço;
* velocidade;
* idade;
* liquidez;
* temperatura;
* complexidade.

A propriedade não deve ser confundida com a entidade.

---

## 5.6 Atributos dinâmicos

Características que variam no tempo.

Exemplo:

```text
Ativo X
Preço:
t1 = 100
t2 = 103
t3 = 98
```

A propriedade "preço" permanece como dimensão representacional, enquanto seu valor muda.

---

## 5.7 Relações

Conexões entre entidades.

Exemplos:

* pertence a;
* contém;
* precede;
* sucede;
* depende de;
* influencia;
* é semelhante a;
* é parte de;
* é instância de.

Uma relação não deve ser confundida automaticamente com causalidade.

---

## 5.8 Estruturas

Conjuntos organizados de entidades e relações.

Exemplos:

* organização;
* mercado;
* sistema;
* cadeia de suprimentos;
* arquitetura;
* ecossistema.

---

## 5.9 Agentes

Entidades capazes de produzir ações ou comportamentos.

Podem incluir:

* pessoas;
* organizações;
* sistemas;
* agentes artificiais;
* organismos;
* agentes coletivos.

Atribuir agência exige cuidado.

O simples fato de algo produzir um efeito não significa necessariamente que possua intenção.

---

## 5.10 Ações

Atos realizados por agentes ou sistemas.

Exemplos:

* comprar;
* vender;
* modificar;
* comunicar;
* investigar;
* decidir.

Ação deve ser distinguida de evento.

---

## 5.11 Objetivos

Estados desejados ou condições pretendidas.

Exemplos:

* maximizar retorno;
* reduzir risco;
* solucionar problema;
* preservar capital.

Objetivo não é necessariamente resultado.

---

## 5.12 Restrições

Condições que limitam o espaço de possibilidades.

Exemplos:

* orçamento;
* tempo;
* legislação;
* capacidade;
* disponibilidade;
* regras operacionais.

Restrições pertencem ao universo representacional, mas não devem ser confundidas com impossibilidade ontológica.

---

## 5.13 Recursos

Elementos utilizáveis para realizar ações ou alcançar estados.

Exemplos:

* capital;
* tempo;
* informação;
* energia;
* ferramentas;
* conhecimento;
* capacidade computacional.

---

## 5.14 Conceitos

Representações abstratas utilizadas para organizar entidades ou fenômenos.

Exemplos:

* risco;
* tendência;
* eficiência;
* confiança;
* valor;
* qualidade.

Conceito não deve ser automaticamente tratado como objeto físico.

---

## 5.15 Categorias

Agrupamentos conceituais utilizados para organizar entidades.

Exemplo:

```text
Instrumento
├── Ação
├── Futuro
├── Opção
└── Criptoativo
```

Categorias são instrumentos cognitivos e podem ser revisadas.

---

## 5.16 Hipóteses ontológicas

Possíveis entidades ou estruturas cuja existência ainda não foi estabelecida.

Exemplo:

> "Pode existir uma variável latente responsável pela relação observada."

A hipótese deve permanecer como hipótese.

---

## 5.17 Entidades abstratas

Elementos que não precisam possuir existência física.

Exemplos:

* números;
* regras;
* contratos;
* instituições;
* algoritmos;
* conceitos;
* direitos;
* estruturas matemáticas.

---

# 6. NÍVEIS DE EXISTÊNCIA

O LLM deve evitar reduzir todo o universo a uma única ontologia.

Pode existir uma hierarquia:

```text
REALIDADE FÍSICA
        ↓
SISTEMAS
        ↓
PROCESSOS
        ↓
EVENTOS
        ↓
ESTADOS
        ↓
PROPRIEDADES
        ↓
REPRESENTAÇÕES
        ↓
CONCEITOS
        ↓
HIPÓTESES
```

Esses níveis não constituem uma hierarquia universal obrigatória.

Em determinados domínios, a ordem pode mudar.

O LLM deve perguntar:

> **"Qual nível de descrição é adequado ao problema atual?"**

---

# 7. MICRO, MESO E MACRO

Uma entidade pode ser analisada em múltiplas escalas.

### Micro

Componentes e detalhes.

### Meso

Interações entre componentes.

### Macro

Sistema ou ambiente.

Exemplo:

```text
Micro:
ordens individuais

Meso:
fluxo de participantes

Macro:
estrutura do mercado
```

O LLM não deve assumir que a explicação válida em uma escala é necessariamente válida em outra.

---

# 8. IDENTIDADE

O LLM deve distinguir:

* entidade;
* nome da entidade;
* representação da entidade;
* instância da categoria;
* ocorrência da entidade;
* estado da entidade.

Duas descrições diferentes podem referir-se à mesma entidade.

Duas descrições semelhantes podem referir-se a entidades diferentes.

Portanto:

> **similaridade semântica ≠ identidade ontológica.**

---

# 9. INDIVIDUAÇÃO

Quando necessário, o LLM deve determinar quais características permitem distinguir uma entidade de outra.

Exemplo:

```text
"empresa A"
≠
"empresa B"
```

mesmo que tenham:

* mesma indústria;
* mesmo tamanho;
* mesma localização;
* produtos semelhantes.

A individuação deve ser orientada pelo contexto.

---

# 10. PARTE E TODO

O LLM deve representar relações mereológicas:

```text
TODO
├── Parte A
├── Parte B
└── Parte C
```

Mas deve reconhecer que:

> parte ≠ simples atributo.

Exemplo:

* motor é parte do veículo;
* cor é propriedade do veículo.

---

# 11. TIPO E INSTÂNCIA

Distinguir:

```text
TIPO
   ↓
INSTÂNCIA
```

Exemplo:

```text
"Criptoativo" → tipo
"Bitcoin específico" → instância
```

A classificação pode ser:

* múltipla;
* hierárquica;
* contextual;
* contestável.

---

# 12. CATEGORIZAÇÃO DINÂMICA

O LLM não deve ser obrigado a utilizar categorias fornecidas inicialmente quando elas forem insuficientes.

Pode:

1. identificar uma categoria existente;
2. perceber que ela é inadequada;
3. subdividi-la;
4. combinar categorias;
5. criar uma nova categoria;
6. abandonar uma categoria.

Isso é essencial para preservar cognição aberta.

---

# 13. RELAÇÕES ONTOLÓGICAS

As relações podem incluir:

### Estruturais

* é parte de;
* contém;
* pertence a;
* é componente de.

### Taxonômicas

* é um tipo de;
* é instância de;
* pertence à classe.

### Temporais

* precede;
* sucede;
* ocorre durante;
* coincide com.

### Espaciais

* está em;
* contém;
* está próximo de;
* atravessa.

### Funcionais

* serve para;
* utiliza;
* fornece;
* depende de.

### Associativas

* relacionado a;
* semelhante a;
* correlacionado a.

### Causais

* causa;
* contribui para;
* impede;
* aumenta a probabilidade de.

**A relação causal deve ser tratada pela camada causal, não presumida simplesmente porque duas entidades estão relacionadas.**

---

# 14. DISTINÇÃO ENTRE RELAÇÃO E CAUSA

Regra fundamental:

```text
A relacionado a B
        ≠
A causa B
```

O LLM deve manter aberta a possibilidade de:

* correlação;
* coincidência;
* causa comum;
* causalidade reversa;
* mediação;
* relação indireta;
* relação espúria.

---

# 15. TEMPO E ONTOLOGIA

Toda entidade relevante pode possuir:

* existência;
* início;
* duração;
* término;
* estados sucessivos;
* eventos associados.

O LLM deve evitar tratar estados temporais como entidades independentes sem necessidade.

Exemplo:

```text
Empresa X
    ├── estado em 2024
    ├── estado em 2025
    └── estado em 2026
```

---

# 16. CONTEXTO ONTOLÓGICO

Uma mesma expressão pode representar entidades diferentes dependendo do domínio.

Exemplo:

> "liquidez"

pode representar conceitos diferentes em:

* finanças;
* economia;
* engenharia;
* física.

O LLM deve estabelecer o contexto antes de assumir identidade conceitual.

---

# 17. MULTIPLICIDADE DE PERSPECTIVAS

Uma mesma entidade pode possuir múltiplas representações legítimas.

Exemplo:

```text
EMPRESA X

perspectiva jurídica
perspectiva econômica
perspectiva operacional
perspectiva financeira
perspectiva social
perspectiva estratégica
```

Essas perspectivas não precisam ser reduzidas a uma única descrição.

---

# 18. ONTOLOGIAS CONCORRENTES

Quando existem modelos ontológicos incompatíveis, o LLM deve preservar a possibilidade de coexistência.

Estrutura:

```text
Fenômeno
├── Modelo A
├── Modelo B
└── Modelo C
```

Enquanto não houver fundamento suficiente para escolher entre eles, a representação deve preservar a pluralidade.

---

# 19. ONTOLOGIA EPISTEMICAMENTE INCERTA

O LLM deve diferenciar:

```text
EXISTE
PROVAVELMENTE EXISTE
POSTULADO
HIPOTÉTICO
POSSÍVEL
DESCONHECIDO
NEGADO
INCOMPATÍVEL
```

Essas categorias não são equivalentes.

Particularmente:

> **não identificado ≠ inexistente.**

E:

> **não demonstrado ≠ falso.**

---

# 20. ENTIDADES LATENTES

O LLM pode considerar entidades não diretamente observáveis quando forem necessárias para explicar o fenômeno.

Exemplos:

* variável latente;
* estado oculto;
* mecanismo não observado;
* fator subjacente;
* estrutura implícita.

Entretanto:

> entidade latente não deve ser promovida automaticamente a entidade real.

Ela deve permanecer como construção explicativa até que o tratamento epistemológico posterior estabeleça seu status.

---

# 21. ONTOLOGIA OBSERVACIONAL E ONTOLOGIA TEÓRICA

Distinguem-se:

### Observacional

Aquilo diretamente identificável ou mensurável no contexto.

### Teórica

Entidades postuladas para explicar fenômenos.

Exemplo:

```text
Observação:
movimento de preço

Construção teórica:
pressão compradora

Hipótese:
determinado mecanismo produziu o movimento
```

Essa separação reduz confusão entre fenômeno e interpretação.

---

# 22. AUSÊNCIA

Ausência deve ser representada com cuidado.

Possibilidades:

* entidade não observada;
* entidade procurada e não encontrada;
* entidade não disponível;
* entidade inexistente;
* informação ausente;
* informação desconhecida.

Não são equivalentes.

---

# 23. NEGATIVA ONTOLÓGICA

Quando uma afirmação diz:

> "X não existe"

o LLM deve distinguir:

1. inexistência demonstrada;
2. inexistência dentro de determinado modelo;
3. inexistência no contexto analisado;
4. ausência de evidência;
5. impossibilidade lógica;
6. impossibilidade física;
7. impossibilidade prática.

---

# 24. ONTOLOGIA E LINGUAGEM

Palavras não devem ser confundidas com entidades.

Uma mesma entidade pode possuir:

* múltiplos nomes;
* abreviações;
* sinônimos;
* traduções;
* códigos;
* identificadores.

E uma mesma palavra pode representar múltiplas entidades.

Portanto:

> **token ≠ conceito ≠ entidade.**

---

# 25. ONTOLOGIA E AMBIGUIDADE

Quando a ambiguidade for relevante, o LLM deve preservá-la temporariamente.

Exemplo:

```text
Termo X
├── interpretação A
├── interpretação B
└── interpretação C
```

A resolução prematura pode destruir informação.

O LLM deve resolver apenas quando:

* houver evidência;
* o contexto for suficiente;
* a resolução for necessária;
* ou o usuário determinar explicitamente.

---

# 26. ONTOLOGIA E GRANULARIDADE

O nível de detalhamento deve ser adaptativo.

Não deve haver:

* decomposição excessiva;
* simplificação excessiva.

O LLM deve escolher a granularidade necessária para a tarefa.

Princípio:

> **representar o suficiente para preservar as propriedades relevantes do problema.**

---

# 27. ONTOLOGIA E COMPLEXIDADE

Sistemas complexos podem possuir:

* múltiplos níveis;
* propriedades emergentes;
* relações não lineares;
* interdependências;
* comportamentos coletivos.

O LLM não deve assumir que:

> conhecimento das partes = conhecimento suficiente do todo.

---

# 28. EMERGÊNCIA

Uma propriedade pode surgir no nível do sistema sem estar presente isoladamente nos componentes.

Exemplo:

```text
agentes individuais
        ↓
interações
        ↓
padrão coletivo
```

A propriedade emergente deve ser representável como objeto de investigação sem necessariamente ser reduzida aos componentes.

---

# 29. FRONTEIRAS DO SISTEMA

Para qualquer sistema analisado, o LLM deve poder perguntar:

* o que está dentro?
* o que está fora?
* o que é ambiente?
* quais elementos atravessam a fronteira?
* quais relações dependem do exterior?

A fronteira deve ser tratada como **modelagem**, não como fato absoluto.

---

# 30. AMBIENTE

Toda entidade ou sistema pode ser analisado em relação ao seu ambiente.

```text
AMBIENTE
   ↓
SISTEMA
   ↓
SUBSISTEMAS
```

O ambiente pode tornar-se parte do objeto de análise caso influencie significativamente o fenômeno.

---

# 31. ESCOPOS ONTOLÓGICOS

A representação deve declarar implicitamente ou explicitamente seu escopo quando necessário:

* domínio;
* espaço;
* tempo;
* população;
* nível de análise;
* perspectiva;
* finalidade.

Isso reduz generalizações indevidas.

---

# 32. ONTOLOGIA E CONTRADIÇÃO

Contradições entre representações não devem ser eliminadas automaticamente.

Podem indicar:

* erro;
* ambiguidade;
* mudança temporal;
* perspectivas diferentes;
* entidades diferentes;
* modelos incompatíveis;
* informação conflitante;
* verdadeira inconsistência.

A contradição é também um **sinal cognitivo**.

---

# 33. ONTOLOGIA E REVISÃO

A representação deve permitir:

```text
representação inicial
        ↓
nova informação
        ↓
tensão
        ↓
reavaliação
        ↓
refinamento
```

A revisão não deve ser considerada falha.

É comportamento cognitivo desejável.

---

# 34. AUTOEXPANSÃO ONTOLÓGICA

Quando o problema exigir uma entidade, relação ou categoria ausente, o LLM deve poder introduzi-la.

Processo cognitivo:

```text
problema
↓
representação insuficiente
↓
detecção da lacuna
↓
proposição ontológica
↓
avaliação
↓
incorporação provisória
```

Isso é fundamental para impedir que o Harness transforme a ontologia em uma taxonomia rígida.

---

# 35. ONTOLOGIA MÍNIMA E ONTOLOGIA EXPLORATÓRIA

Devem coexistir dois modos.

### Ontologia mínima

Representação suficiente para executar a tarefa atual.

### Ontologia exploratória

Expansão deliberada do espaço representacional para descobrir estruturas ainda não consideradas.

O LLM deve poder alternar entre os dois.

---

# 36. PRINCÍPIO DE NÃO-ENCAPSULAMENTO

Nenhuma ontologia previamente definida deve encapsular completamente o universo cognitivo do LLM.

Portanto, não se deve exigir:

> "Tudo deve pertencer a uma das categorias previamente definidas."

Preferível:

> "Utilize as categorias existentes quando adequadas e expanda ou questione a estrutura quando ela não representar adequadamente o fenômeno."

---

# 37. DOMÍNIOS DE APLICAÇÃO

A camada deve ser capaz de representar, entre outros:

### Ciências naturais

* objetos;
* organismos;
* fenômenos;
* partículas;
* sistemas;
* estados físicos.

### Medicina

* pacientes;
* condições;
* sintomas;
* exames;
* tratamentos;
* eventos clínicos.

### Engenharia

* componentes;
* sistemas;
* requisitos;
* estados;
* falhas;
* interfaces.

### Economia

* agentes;
* mercados;
* recursos;
* incentivos;
* fluxos;
* instituições.

### Finanças e trading

* ativos;
* participantes;
* ordens;
* preço;
* liquidez;
* volatilidade;
* estrutura de mercado;
* sessões;
* eventos;
* regimes;
* padrões;
* hipóteses de comportamento.

### Direito

* pessoas;
* entidades;
* contratos;
* obrigações;
* direitos;
* eventos jurídicos;
* normas.

### Gestão

* organizações;
* processos;
* recursos;
* objetivos;
* indicadores;
* decisões;
* riscos.

### Ciência de dados

* dados;
* variáveis;
* observações;
* modelos;
* features;
* distribuições;
* eventos.

### Inteligência artificial

* modelos;
* agentes;
* ferramentas;
* contexto;
* memória;
* tarefas;
* estados;
* artefatos.

### Ciências humanas

* indivíduos;
* grupos;
* instituições;
* culturas;
* comportamentos;
* relações;
* fenômenos sociais.

### Conhecimento abstrato

* conceitos;
* teorias;
* axiomas;
* hipóteses;
* argumentos;
* estruturas matemáticas.

---

# 38. DOMÍNIO DE TRADING — EXEMPLO DE APLICAÇÃO

Para o SOT, a ontologia deve permitir representar simultaneamente:

```text
MERCADO
│
├── Ativos
│
├── Participantes
│
├── Ordens
│
├── Transações
│
├── Preço
│
├── Volume
│
├── Liquidez
│
├── Tempo
│
├── Estrutura
│
├── Regimes
│
├── Eventos
│
├── Padrões
│
├── Hipóteses
│
└── Observações
```

E distinguir:

```text
OBSERVAÇÃO
"o preço rompeu determinado nível"

REPRESENTAÇÃO
"há uma ruptura estrutural"

HIPÓTESE
"o movimento pode indicar continuação"

INFERÊNCIA
"determinadas evidências aumentam a plausibilidade"

DECISÃO
"executar / não executar"
```

A ontologia não deve determinar a decisão.

Ela apenas garante que os objetos envolvidos possam ser representados adequadamente.

---

# 39. RELAÇÃO COM AS OUTRAS CAMADAS

A camada ontológica fornece matéria-prima para as demais.

```text
ONTOLOGIA
"O que existe?"
       ↓
SEMÂNTICA
"O que significa?"
       ↓
EPISTEMOLOGIA
"O que sabemos?"
       ↓
INQUÉRITO
"O que precisamos descobrir?"
       ↓
CAUSALIDADE
"O que produz o quê?"
       ↓
CONTRAFACTUAL
"O que aconteceria se...?"
       ↓
PROBABILIDADE / INCERTEZA
"Quão plausível é?"
       ↓
METACOGNIÇÃO
"Como avaliar nosso próprio processo?"
       ↓
DECISÃO
"O que fazer?"
```

Essas camadas podem retroalimentar a ontologia.

---

# 40. FEEDBACK COGNITIVO

A arquitetura deve permitir:

```text
DECISÃO
   ↓
RESULTADO
   ↓
ERRO / SURPRESA
   ↓
REVISÃO EPISTEMOLÓGICA
   ↓
REVISÃO ONTOLÓGICA
```

Uma surpresa significativa pode indicar não apenas erro de raciocínio, mas:

> **a representação do próprio universo estava incompleta.**

Esse é um princípio de alto valor para sistemas cognitivos.

---

# 41. PRINCÍPIOS COMPORTAMENTAIS DO LLM

O LLM deve:

1. identificar as entidades relevantes;
2. distinguir entidades de propriedades;
3. distinguir entidades de conceitos;
4. distinguir eventos de estados;
5. distinguir relações de causalidade;
6. considerar múltiplos níveis de abstração;
7. preservar ambiguidades relevantes;
8. reconhecer entidades hipotéticas;
9. distinguir desconhecimento de inexistência;
10. revisar categorias quando inadequadas;
11. criar novas categorias quando necessário;
12. considerar múltiplas perspectivas;
13. reconhecer limites da representação;
14. evitar assumir que sua primeira ontologia é definitiva;
15. adaptar a granularidade à tarefa;
16. preservar estruturas alternativas quando necessário;
17. investigar lacunas ontológicas;
18. manter separação entre representação e realidade;
19. permitir que novas evidências alterem a representação;
20. utilizar a ontologia como **meio de expansão cognitiva**.

---

# 42. COMPORTAMENTOS A EVITAR

O LLM não deve:

* tratar a taxonomia inicial como universo completo;
* confundir nome com entidade;
* confundir conceito com realidade;
* transformar associação em causalidade;
* transformar ausência de evidência em inexistência;
* eliminar automaticamente contradições;
* forçar toda entidade para categorias existentes;
* congelar a ontologia;
* confundir hipótese com entidade estabelecida;
* assumir uma única perspectiva;
* reduzir sistemas complexos às suas partes sem análise;
* assumir que a representação é a realidade;
* limitar novas hipóteses por categorias previamente definidas.

---

# 43. PRINCÍPIO DA LIBERDADE COGNITIVA

A especificação deve funcionar como **andaime cognitivo**, não como trilho cognitivo.

O LLM deve poder:

```text
seguir a estrutura
        +
questionar a estrutura
        +
expandir a estrutura
        +
substituir a estrutura
```

quando o problema justificar.

A existência de uma ontologia previamente definida deve aumentar a capacidade de raciocínio, e não reduzir o espaço de hipóteses.

---

# 44. PRINCÍPIO DA REPRESENTAÇÃO MÚLTIPLA

Quando um fenômeno puder ser representado de formas diferentes, o LLM deve poder manter múltiplas representações concorrentes.

Exemplo:

```text
Fenômeno X

Modelo estrutural
Modelo funcional
Modelo temporal
Modelo probabilístico
Modelo causal
Modelo baseado em agentes
```

A escolha da representação deve depender do problema.

---

# 45. PRINCÍPIO DA ECONOMICIDADE COGNITIVA

A representação deve ser:

> **tão simples quanto possível, mas tão expressiva quanto necessário.**

Evitar:

* ontologias excessivamente detalhadas;
* categorias inúteis;
* relações sem função cognitiva;
* burocratização da representação.

Mas evitar também:

* simplificação que destrua informação;
* categorias excessivamente genéricas;
* perda de distinções relevantes.

---

# 46. PRINCÍPIO DA SUFICIÊNCIA

Uma representação ontológica é suficiente quando preserva as distinções necessárias para:

* compreender;
* investigar;
* raciocinar;
* comparar;
* prever;
* decidir;
* agir;
* aprender.

Não existe necessidade de representar tudo.

Existe necessidade de representar **o que pode alterar o raciocínio**.

---

# 47. PRINCÍPIO DA SURPRESA

Quando um fenômeno não puder ser adequadamente explicado pela ontologia atual, o LLM deve considerar:

> **"Talvez o problema não esteja apenas no raciocínio; talvez esteja faltando algo na representação do universo."**

Esse princípio protege contra raciocínio excessivamente fechado.

---

# 48. PRINCÍPIO DA DESCoberta ONTOLÓGICA

A descoberta de uma nova entidade, relação ou categoria deve ser considerada um resultado cognitivo válido.

Exemplo:

```text
Problema
↓
Análise
↓
anomalia
↓
lacuna representacional
↓
nova entidade candidata
↓
investigação
↓
validação epistemológica
```

---

# 49. PRINCÍPIO DA REVERSIBILIDADE

Quando possível, o LLM deve conseguir retornar a níveis anteriores da representação.

Exemplo:

```text
categoria
↓
subcategoria
↓
entidade
↓
evento
↓
observação
```

E também:

```text
observação
↓
evento
↓
entidade
↓
sistema
```

Isso permite alternar entre abstração e concretude.

---

# 50. CRITÉRIOS DE QUALIDADE

Uma representação ontológica deve ser avaliada por:

### Cobertura

Representa os elementos relevantes?

### Distinção

Evita confundir entidades diferentes?

### Coerência

As relações são compatíveis?

### Expressividade

Consegue representar o fenômeno adequadamente?

### Flexibilidade

Pode ser expandida?

### Revisabilidade

Pode ser corrigida?

### Rastreabilidade

É possível compreender por que determinada entidade foi representada daquela maneira?

### Economicidade

Evita complexidade desnecessária?

### Utilidade cognitiva

Melhora efetivamente o raciocínio?

---

# 51. TESTES COGNITIVOS DA CAMADA

A especificação pode ser submetida a perguntas como:

### Teste 1 — Entidade desconhecida

> O modelo consegue reconhecer que algo relevante ainda não possui representação?

### Teste 2 — Categoria inexistente

> Consegue propor uma nova categoria?

### Teste 3 — Ambiguidade

> Consegue manter duas interpretações sem escolher prematuramente?

### Teste 4 — Contradição

> Consegue preservar duas representações conflitantes enquanto investiga?

### Teste 5 — Multiescalaridade

> Consegue representar micro, meso e macro simultaneamente?

### Teste 6 — Temporalidade

> Consegue distinguir entidade de seus diferentes estados temporais?

### Teste 7 — Latência

> Consegue trabalhar com entidades não observáveis sem tratá-las como fatos?

### Teste 8 — Emergência

> Consegue representar propriedades que surgem no nível coletivo?

### Teste 9 — Revisão

> Consegue modificar sua ontologia após uma nova informação?

### Teste 10 — Liberdade cognitiva

> A estrutura permite ao modelo chegar a uma categoria que não estava prevista originalmente?

---

# 52. TESTE FUNDAMENTAL DE NÃO RESTRIÇÃO

A camada será considerada cognitivamente saudável somente se:

> **um resultado não previsto pela ontologia inicial puder ser representado sem que o Harness force sua exclusão ou classificação inadequada.**

Esse teste é obrigatório.

---

# 53. ANTI-OVERFITTING ONTOLÓGICO

A ontologia não deve ser construída exclusivamente a partir de exemplos conhecidos.

Caso contrário:

```text
experiências passadas
        ↓
categorias fixas
        ↓
novos fenômenos
        ↓
forçamento de classificação
```

O comportamento desejável é:

```text
experiências passadas
        ↓
estrutura inicial
        ↓
novos fenômenos
        ↓
comparação
        ↓
adaptação / expansão
```

---

# 54. ANTI-REDUCIONISMO

O LLM deve poder reconhecer que diferentes níveis de descrição podem ser simultaneamente válidos.

Não deve assumir automaticamente:

> "Tudo pode ser explicado apenas pelos componentes."

Nem:

> "O todo é completamente independente das partes."

A relação deve ser investigada.

---

# 55. ANTI-ESSENCIALISMO

Uma classificação não implica necessariamente que uma entidade possua uma essência fixa.

Categorias podem ser:

* funcionais;
* contextuais;
* convencionais;
* temporárias;
* graduais;
* multidimensionais.

---

# 56. ONTOLOGIA COMO HIPÓTESE DE TRABALHO

Em contextos complexos, a ontologia deve ser tratada como:

> **modelo operacional provisório do universo relevante.**

Ela pode possuir:

* alto grau de estabilidade;
* partes estáveis;
* partes experimentais;
* partes desconhecidas.

---

# 57. ESTADOS DE MATURIDADE ONTOLÓGICA

Uma representação pode estar:

```text
NÃO REPRESENTADA
      ↓
CANDIDATA
      ↓
PROVISÓRIA
      ↓
UTILIZADA
      ↓
VALIDADA NO CONTEXTO
      ↓
ESTABILIZADA
```

"Estabilizada" não significa "imutável".

---

# 58. RELAÇÃO COM CONHECIMENTO

A ontologia responde:

> **quais coisas estão sendo consideradas?**

A epistemologia responde:

> **qual é o status do nosso conhecimento sobre essas coisas?**

Exemplo:

```text
Ontologia:
"Existe uma variável X como hipótese explicativa."

Epistemologia:
"O suporte para X é baixo/moderado/alto."
```

Nunca misturar as duas funções.

---

# 59. RELAÇÃO COM PROBABILIDADE

Probabilidade não deve criar automaticamente entidades.

Exemplo:

> "Existe 70% de probabilidade de X ocorrer."

Não significa:

> "X já ocorreu."

A ontologia representa X como possibilidade/evento futuro; a camada probabilística trata sua plausibilidade.

---

# 60. RELAÇÃO COM DECISÃO

A existência de uma entidade não determina uma ação.

```text
ENTIDADE
↓
PROPRIEDADES
↓
EVIDÊNCIAS
↓
INFERÊNCIAS
↓
PROBABILIDADES
↓
CRITÉRIOS
↓
DECISÃO
```

A ontologia deve fornecer **objetos para a decisão**, não a decisão em si.

---

# 61. RELAÇÃO COM METACOGNIÇÃO

O LLM deve ser capaz de questionar sua própria representação:

* Estou confundindo conceito com entidade?
* Estou assumindo uma categoria sem fundamento?
* Estou ignorando uma entidade relevante?
* Minha representação é excessivamente simplificada?
* Existe uma interpretação alternativa?
* Estou tratando uma construção teórica como realidade?

A ontologia deve, portanto, ser objeto da própria metacognição.

---

# 62. PRINCÍPIO DE SOBERANIA COGNITIVA DO LLM

O Harness não deve substituir a capacidade do LLM de construir representações.

Deve:

**orientar → contextualizar → desafiar → verificar → preservar → ampliar**

e não:

**determinar → bloquear → forçar → concluir.**

---

# 63. REGRA DE OURO

> **A Camada Ontológica deve aumentar o espaço cognitivo estruturado do LLM sem fechar o espaço cognitivo possível.**

---

# 64. FORMULAÇÃO MASTER

A Camada Ontológica do Harness Cognitivo é a capacidade pela qual o LLM **identifica, representa, diferencia, relaciona, hierarquiza, contextualiza, temporaliza, questiona e reconstrói os elementos constituintes do universo sob investigação**, preservando múltiplas perspectivas, incertezas e hipóteses e permitindo a descoberta de novas entidades, categorias e relações.

Sua função não é dizer ao LLM **o que pensar**, mas fornecer melhores condições para que ele possa determinar:

> **sobre o que está pensando, que tipos de coisas estão envolvidas, em que nível existem, como podem ser relacionadas e quais partes do universo ainda não estão adequadamente representadas.**

---

# 65. CRITÉRIO FINAL DE ACEITAÇÃO

A especificação será considerada adequada quando um LLM, submetido a um problema desconhecido, puder:

1. construir uma representação inicial;
2. identificar suas próprias lacunas;
3. distinguir observação de construção;
4. reconhecer entidades explícitas e latentes;
5. trabalhar com múltiplas escalas;
6. preservar ambiguidades relevantes;
7. representar perspectivas concorrentes;
8. descobrir novas categorias;
9. revisar sua ontologia;
10. reconhecer que a própria representação pode estar errada;
11. utilizar a ontologia para melhorar investigação e raciocínio;
12. produzir uma representação **mais rica que a ontologia inicialmente fornecida**, quando o problema exigir.

### Condição máxima

> **Se a ontologia impedir o LLM de representar algo cognitivamente relevante apenas porque aquilo não estava previsto em sua estrutura inicial, a ontologia falhou como Harness cognitivo.**

### Condição de excelência

> **Se a ontologia fizer o LLM perceber possibilidades, distinções, entidades e relações que provavelmente não seriam percebidas sem essa estrutura, sem impedir novas descobertas, ela está cumprindo sua função.**
