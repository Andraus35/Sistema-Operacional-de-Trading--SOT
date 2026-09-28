# MANUAL UNIVERSAL DE ENGENHARIA DE PRINCÍPIOS, PONDERAÇÃO E DINÂMICA PARA SISTEMAS AGÊNTICOS DE IA

**Versão:** 2.0\
**Status:** Proposta para validação\
**Escopo:** Universal --- sistemas de agente único, multiagentes,
workflows agenticos, sistemas híbridos humano-IA e arquiteturas
distribuídas\
**Natureza:** Manual de especificação e governança cognitiva\
**Não substitui:** Constituição do sistema, especificação de agentes,
contratos de dados, políticas de segurança, avaliação, testes ou
arquitetura de execução

------------------------------------------------------------------------

## 0. Propósito

Este manual define uma disciplina para **projetar, especificar, governar
e avaliar agentes de IA a partir de princípios que interagem entre si**.

A proposta central é simples:

> Um agente não deve ser especificado apenas por regras isoladas. Deve
> saber quais princípios orientam seu comportamento, como esses
> princípios se relacionam, em quais contextos mudam de importância,
> como lidar com tensão entre eles e como justificar a ponderação
> realizada.

O manual é universal. Ele não pertence ao SOT, ao AXL ou a qualquer
domínio específico.

Ele pode ser aplicado a:

-   agentes de pesquisa;
-   agentes de diagnóstico;
-   agentes de documentação;
-   agentes de planejamento;
-   agentes de programação;
-   agentes financeiros;
-   agentes administrativos;
-   agentes jurídicos;
-   agentes de atendimento;
-   agentes de governança;
-   agentes supervisores;
-   agentes multiagentes;
-   orquestradores;
-   sistemas com humanos no circuito;
-   sistemas autônomos;
-   sistemas híbridos determinísticos e probabilísticos.

------------------------------------------------------------------------

# 1. Por que este manual é necessário

As especificações tradicionais de agentes tendem a responder:

-   qual é o objetivo?
-   quais ferramentas o agente pode usar?
-   quais regras deve seguir?
-   qual saída deve produzir?
-   quando deve parar?

Essas perguntas são necessárias, mas insuficientes para agentes capazes
de deliberar.

Um agente real frequentemente encontra situações como:

-   autonomia versus controle;
-   velocidade versus profundidade;
-   eficiência versus qualidade;
-   exploração versus conservação;
-   especialização versus generalização;
-   centralização versus descentralização;
-   padronização versus diversidade;
-   estabilidade versus adaptação;
-   objetividade formal versus interpretação contextual;
-   convergência versus divergência;
-   consistência global versus adequação local;
-   memória versus esquecimento;
-   segurança versus utilidade;
-   privacidade versus disponibilidade de contexto;
-   custo versus cobertura;
-   explicabilidade versus complexidade;
-   precisão versus oportunidade.

Não existe uma regra simples que resolva todas essas situações.

Portanto, a engenharia de agentes precisa especificar não apenas **o que
fazer**, mas também **como ponderar princípios quando eles coexistem**.

------------------------------------------------------------------------

# 2. Estado da arte e posição deste manual

A pesquisa de referências atuais mostra convergência em alguns pontos
importantes.

## 2.1 NIST --- governança, risco e confiabilidade

O NIST AI RMF organiza a gestão de risco de IA nas funções **Govern,
Map, Measure e Manage**, e considera características como validade e
confiabilidade, segurança, resiliência, responsabilidade, transparência,
explicabilidade, interpretabilidade, privacidade e justiça.

A contribuição relevante para este manual é:

> princípios não devem ser tratados apenas como declarações abstratas;
> precisam aparecer no desenho, avaliação, operação e gestão do sistema.

Fonte de referência: NIST AI RMF / Playbook.

## 2.2 Anthropic --- autonomia versus controle humano

A Anthropic explicita a tensão entre autonomia do agente e supervisão
humana como um problema central de sistemas agenticos.

A contribuição relevante:

> autonomia não é ausência de governança. O desenho precisa definir o
> espaço de autonomia e os limites de intervenção.

## 2.3 Microsoft --- padrões de orquestração e complexidade

A documentação atual da Microsoft destaca:

-   agentes especializados;
-   orquestração sequencial;
-   execução concorrente;
-   handoff;
-   padrões magentic;
-   contratos entre agentes;
-   governança;
-   least privilege;
-   simplicidade;
-   auditabilidade;
-   escolha do menor nível de complexidade que atende ao requisito.

A contribuição relevante:

> princípios de coordenação também são decisões arquiteturais.

## 2.4 Google Cloud --- escolha de padrões agenticos

A orientação arquitetural da Google enfatiza que sistemas agenticos
devem escolher padrões de arquitetura de acordo com o problema, em vez
de aplicar multiagentes por padrão.

A contribuição relevante:

> a complexidade da arquitetura deve ser proporcional à necessidade
> cognitiva e operacional.

## 2.5 OWASP --- governança específica para agentes

A literatura OWASP sobre Agentic AI amplia o foco de segurança para:

-   raciocínio;
-   memória;
-   ferramentas;
-   identidade;
-   supervisão humana;
-   interações entre agentes;
-   delegação;
-   autonomia;
-   ameaças emergentes.

A contribuição relevante:

> quanto maior a autonomia e a conectividade, maior a necessidade de
> limites explícitos, observabilidade e governança.

## 2.6 Síntese do benchmark

O estado da arte converge em:

1.  autonomia precisa de limites;
2.  especialização pode aumentar qualidade;
3.  multiagentes aumentam coordenação e complexidade;
4.  contratos e interfaces reduzem acoplamento;
5.  segurança deve considerar ferramentas, memória, identidade e
    agentes;
6.  supervisão deve ser proporcional ao risco;
7.  avaliação precisa ocorrer durante todo o ciclo de vida;
8.  a arquitetura deve usar a menor complexidade que resolva o problema.

**Lacuna identificada:** essas referências tratam extensivamente de
governança, risco, autonomia, orquestração e segurança, mas não
oferecem, em conjunto, uma teoria geral operacional para **relações
entre princípios, ponderação contextual, confluência, antagonismo,
compensação, precedência e dinâmica cognitiva**.

Este manual ocupa deliberadamente esse espaço.

------------------------------------------------------------------------

# 3. Princípio fundamental

## 3.1 Um princípio não é uma regra

### Princípio

Orientação de comportamento relativamente estável.

Exemplo:

> Preservar auditabilidade.

### Regra

Determinação operacional específica.

Exemplo:

> Toda decisão crítica deve possuir registro de justificativa.

### Parâmetro

Valor ajustável.

Exemplo:

> Limite máximo de custo por tarefa = X.

### Política

Conjunto organizado de regras, limites e critérios.

### Estratégia

Forma escolhida para alcançar um objetivo.

### Procedimento

Sequência operacional.

### Preferência

Orientação desejável, mas não necessariamente obrigatória.

### Heurística

Atalho ou método aproximativo usado sob incerteza.

### Evidência

Informação que sustenta, enfraquece ou modifica uma avaliação.

**Erro grave:** transformar toda preferência em princípio.

------------------------------------------------------------------------

# 4. Ontologia universal dos princípios

Todo princípio utilizado na especificação de um agente deve possuir:

  Campo             Pergunta
  ----------------- ------------------------------------------------------------
  ID                Como será identificado?
  Nome              Como é chamado?
  Definição         O que significa exatamente?
  Finalidade        Para que existe?
  Escopo            Onde se aplica?
  Nível             Constitucional, estrutural, comportamental ou situacional?
  Polaridade        Existe princípio complementar ou antagonista?
  Dependências      De quais princípios depende?
  Evidências        Por que foi adotado?
  Prioridade        Qual sua precedência?
  Elasticidade      Pode ser relativizado?
  Limites           Até onde pode ser aplicado?
  Contexto          Em quais condições muda de peso?
  Reversibilidade   O comportamento resultante pode ser desfeito?
  Impacto           Qual o impacto sistêmico?
  Temporalidade     É permanente ou temporário?
  Observabilidade   Como verificar sua aplicação?
  Auditoria         Como reconstruir sua influência?
  Evolução          Como pode mudar?

------------------------------------------------------------------------

# 5. Classes de princípios

## 5.1 Constitucionais

Definem identidade e limites fundamentais.

Exemplos:

-   segurança;
-   integridade;
-   não ultrapassar autoridade;
-   preservação de direitos;
-   impossibilidade de alterar a própria constituição sem governança
    autorizada.

São os mais resistentes à adaptação.

## 5.2 Basilares

Sustentam o funcionamento do sistema.

Exemplos:

-   coerência;
-   rastreabilidade;
-   explicabilidade;
-   proporcionalidade;
-   auditabilidade.

## 5.3 Estruturais

Definem como o sistema se organiza.

Exemplos:

-   centralização;
-   descentralização;
-   especialização;
-   modularidade;
-   independência;
-   integração.

## 5.4 Cognitivos

Definem como o agente raciocina.

Exemplos:

-   manter hipóteses concorrentes;
-   procurar contraevidência;
-   preservar incerteza;
-   distinguir observação de interpretação;
-   atualizar crenças diante de evidência.

## 5.5 Operacionais

Definem comportamento durante a execução.

Exemplos:

-   velocidade;
-   profundidade;
-   economia de recursos;
-   escalonamento;
-   interrupção.

## 5.6 Situacionais

Dependem fortemente do contexto.

Exemplos:

-   urgência;
-   cautela;
-   exploração;
-   profundidade;
-   autonomia.

------------------------------------------------------------------------

# 6. Dinâmicas entre princípios

Princípios não existem apenas isoladamente.

A engenharia deve identificar explicitamente suas relações.

## 6.1 Complementaridade

Dois princípios aumentam o valor um do outro.

Exemplo:

**Explicabilidade + Auditabilidade**

Um explica o comportamento; o outro permite reconstruí-lo.

### Uso

Quando ambos devem coexistir.

### Risco

Presumir complementaridade sem testar se existe custo ou interferência.

------------------------------------------------------------------------

## 6.2 Fundação

Um princípio sustenta outro.

Exemplo:

**Integridade → Auditabilidade**

Sem integridade dos registros, a auditabilidade perde valor.

------------------------------------------------------------------------

## 6.3 Hierarquia

Um princípio possui precedência sobre outro.

Exemplo:

**Segurança \> velocidade**

### Uso

Quando a resolução do conflito precisa ser determinística.

### Risco

Criar hierarquia excessiva e transformar o sistema em uma lista rígida
de comandos.

------------------------------------------------------------------------

## 6.4 Dependência

Um princípio somente funciona quando outro está presente.

Exemplo:

**Autonomia depende de autoridade delimitada.**

------------------------------------------------------------------------

## 6.5 Reforço

A aplicação de um princípio aumenta a eficácia de outro.

Exemplo:

**Especialização + modularidade**

------------------------------------------------------------------------

## 6.6 Convergência

Princípios diferentes apontam para o mesmo resultado.

Exemplo:

-   eficiência;
-   simplicidade;
-   economia computacional.

Podem convergir para redução de complexidade.

**Importante:** confluência não significa necessariamente independência.
Muitos princípios podem derivar da mesma causa.

------------------------------------------------------------------------

## 6.7 Divergência

Princípios conduzem a resultados diferentes.

Exemplo:

**Exploração ↔ Conservação**

A divergência é útil quando preserva alternativas.

Não deve ser eliminada automaticamente.

------------------------------------------------------------------------

## 6.8 Antagonismo

A realização de um princípio reduz a realização de outro.

Exemplo:

**Autonomia ↔ Enforcement**

### Uso

É uma relação fundamental em agentes.

### Boa prática

Especificar o espaço no qual cada polo prevalece.

------------------------------------------------------------------------

## 6.9 Conflito

Dois princípios exigem comportamentos incompatíveis em um contexto
específico.

Antagonismo é estrutural.

Conflito é situacional.

------------------------------------------------------------------------

## 6.10 Compensação

Um princípio pode compensar parcialmente a limitação de outro.

Exemplo:

**Maior autonomia + maior observabilidade**

A observabilidade não elimina o risco da autonomia, mas pode
compensá-lo.

------------------------------------------------------------------------

## 6.11 Balanço

O sistema procura uma combinação adequada entre princípios.

Exemplo:

**Profundidade ↔ Custo**

Não existe necessariamente um vencedor absoluto.

------------------------------------------------------------------------

## 6.12 Contenção

Um princípio limita a expansão de outro.

Exemplo:

**Autonomia contida por autoridade.**

------------------------------------------------------------------------

## 6.13 Limitação

Define uma fronteira explícita.

Exemplo:

> O agente pode adaptar parâmetros, mas não pode alterar princípios
> constitucionais.

------------------------------------------------------------------------

## 6.14 Precedência

Um princípio vence em determinadas condições.

Exemplo:

> Em risco crítico, segurança precede eficiência.

------------------------------------------------------------------------

## 6.15 Subordinação

Um princípio é deliberadamente colocado sob outro.

Exemplo:

> Eficiência subordinada à eficácia.

Essa relação já aparece em arquiteturas cognitivas como o SOT:
economizar recursos não pode significar sacrificar a qualidade analítica
necessária.

------------------------------------------------------------------------

## 6.16 Condicionamento

Um princípio só se aplica quando determinada condição existe.

Exemplo:

> Profundidade cognitiva aumenta somente quando a hipótese apresenta
> evidência suficiente.

------------------------------------------------------------------------

## 6.17 Contextualização

O peso de um princípio depende do contexto.

Exemplo:

A velocidade pode ser secundária em pesquisa profunda e crítica em
resposta a eventos urgentes.

------------------------------------------------------------------------

## 6.18 Especialização

Um princípio domina em determinado domínio.

Exemplo:

Um agente jurídico pode priorizar conformidade normativa; um agente de
descoberta pode priorizar exploração.

------------------------------------------------------------------------

## 6.19 Composição

Vários princípios formam uma política comportamental.

Exemplo:

**Segurança + autoridade + auditabilidade + reversibilidade**

formam uma política de execução controlada.

------------------------------------------------------------------------

## 6.20 Decomposição

Um princípio amplo é dividido em princípios operacionais.

Exemplo:

**Confiabilidade**

→ validade\
→ consistência\
→ rastreabilidade\
→ robustez\
→ recuperação.

------------------------------------------------------------------------

## 6.21 Substituição

Um princípio pode ser substituído por outro mecanismo equivalente em
determinado contexto.

Deve ser usada com cautela.

------------------------------------------------------------------------

## 6.22 Redundância

Dois princípios produzem proteção semelhante.

Pode ser:

-   deliberada;
-   acidental.

Redundância deliberada pode aumentar robustez.

Redundância acidental pode criar complexidade inútil.

------------------------------------------------------------------------

## 6.23 Independência

Um princípio não depende significativamente dos demais.

É importante para avaliar confluência.

------------------------------------------------------------------------

## 6.24 Competição

Dois princípios competem pelo mesmo recurso.

Exemplo:

-   custo computacional;
-   tempo;
-   contexto;
-   atenção do agente;
-   capacidade de execução.

------------------------------------------------------------------------

## 6.25 Trade-off

Aumentar um objetivo implica aceitar redução em outro.

Exemplo:

**Velocidade ↔ Profundidade**

O trade-off deve ser explicitado, nunca escondido.

------------------------------------------------------------------------

## 6.26 Amplificação

Uma decisão aumenta o efeito de um princípio.

Exemplo:

Maior autonomia pode amplificar simultaneamente produtividade e risco.

------------------------------------------------------------------------

## 6.27 Amortecimento

Um princípio reduz a intensidade de outro.

Exemplo:

Limites de autoridade amortecem a autonomia.

------------------------------------------------------------------------

## 6.28 Inversão contextual

O princípio que normalmente possui menor peso passa a dominar em outro
contexto.

Exemplo:

Em operação normal:

**Eficiência \> profundidade**

Em situação crítica:

**Profundidade \> eficiência**

Isso não é incoerência se a regra de inversão estiver especificada.

------------------------------------------------------------------------

## 6.29 Emergência

A interação entre princípios produz comportamento não especificado
diretamente por nenhum deles.

Exemplo:

Autonomia + memória + aprendizagem + adaptação podem produzir estratégia
emergente.

Sistemas complexos devem monitorar emergência.

------------------------------------------------------------------------

## 6.30 Degeneração

Uma relação originalmente útil passa a produzir comportamento
indesejado.

Exemplo:

Confluência inicialmente melhora a decisão, mas excesso de sinais
correlacionados cria falsa confiança.

------------------------------------------------------------------------

# 7. Dinâmicas adicionais obrigatórias

Para tornar o modelo realmente universal, acrescentam-se relações que
frequentemente aparecem em sistemas agenticos complexos.

## 7.1 Escalonamento

A intensidade de um princípio aumenta ou diminui conforme o risco,
complexidade ou criticidade.

Exemplo:

Quanto maior o impacto da decisão, maior a exigência de validação.

------------------------------------------------------------------------

## 7.2 De-escalonamento

O sistema reduz esforço ou controle quando o contexto se torna seguro.

Exemplo:

Uma tarefa rotineira pode operar com menor profundidade.

------------------------------------------------------------------------

## 7.3 Gating

Um princípio atua como condição de passagem.

Exemplo:

Sem evidência mínima, não avançar para execução.

------------------------------------------------------------------------

## 7.4 Veto

Um princípio pode bloquear uma ação.

Exemplo:

Falha de segurança impede execução mesmo quando todos os outros
critérios são favoráveis.

------------------------------------------------------------------------

## 7.5 Quórum

Uma decisão exige participação mínima de perspectivas independentes.

Útil em:

-   multiagentes;
-   validação;
-   decisões críticas.

Não deve ser confundido com consenso.

------------------------------------------------------------------------

## 7.6 Consenso

Perspectivas convergem para uma conclusão compartilhada.

Consenso é resultado de deliberação.

Não deve ser imposto como objetivo universal.

------------------------------------------------------------------------

## 7.7 Contestação

O sistema mantém deliberadamente um agente, processo ou mecanismo
responsável por desafiar a conclusão dominante.

Útil contra:

-   confirmação;
-   pensamento de grupo;
-   excesso de confluência;
-   dominância de um agente.

------------------------------------------------------------------------

## 7.8 Arbitragem

Um componente autorizado resolve conflitos entre perspectivas.

Pode ser:

-   humano;
-   agente supervisor;
-   política determinística;
-   mecanismo de decisão.

------------------------------------------------------------------------

## 7.9 Delegação

Um agente transfere uma decisão ou tarefa para outro componente.

A delegação deve preservar:

-   autoridade;
-   contexto necessário;
-   rastreabilidade;
-   limites;
-   responsabilidade.

------------------------------------------------------------------------

## 7.10 Escopo

Um princípio pode prevalecer apenas dentro de determinado domínio.

Isso evita que uma regra local se torne uma verdade global.

------------------------------------------------------------------------

## 7.11 Persistência

Alguns princípios devem permanecer ativos ao longo de todo o ciclo de
vida.

Outros são temporários.

------------------------------------------------------------------------

## 7.12 Expiração

Uma ponderação pode deixar de ser válida após:

-   mudança de contexto;
-   passagem de tempo;
-   mudança de regime;
-   alteração de evidência.

------------------------------------------------------------------------

## 7.13 Memória e esquecimento

Memória preserva experiência.

Esquecimento controla obsolescência e evita que informação antiga domine
o presente.

O agente deve especificar:

-   o que lembrar;
-   por quanto tempo;
-   com que peso;
-   quando reduzir peso;
-   quando arquivar;
-   quando invalidar.

------------------------------------------------------------------------

## 7.14 Aprendizagem

A experiência pode alterar pesos operacionais sem necessariamente
alterar princípios constitucionais.

Essa separação é essencial para sistemas governáveis.

------------------------------------------------------------------------

# 8. Eixos universais de tensão

Todo projeto agentico deve avaliar, no mínimo, os seguintes eixos quando
forem relevantes.

  ---------------------------------------------------------------------------
  Eixo               Polo A             Polo B              Pergunta
  ------------------ ------------------ ------------------- -----------------
  Governança         Enforcement        Autonomia           Quanto o agente
                                                            pode decidir
                                                            sozinho?

  Formalidade        Formalização       Interpretação       Quanto depende de
                                                            regras
                                                            explícitas?

  Estabilidade       Estabilidade       Adaptabilidade      Quanto pode
                                                            mudar?

  Conhecimento       Conservação        Exploração          Preservar ou
                                                            descobrir?

  Decisão            Determinismo       Probabilismo        Regra ou
                                                            incerteza?

  Cognição           Reatividade        Deliberação         Responder ou
                                                            analisar?

  Especialização     Especialização     Generalização       Foco ou
                                                            amplitude?

  Escopo             Local              Global              Priorizar
                                                            contexto ou
                                                            coerência
                                                            sistêmica?

  Organização        Centralização      Descentralização    Onde está a
                                                            autoridade?

  Coordenação        Independência      Integração          Componentes
                                                            separados ou
                                                            fortemente
                                                            coordenados?

  Informação         Memória            Esquecimento        Quanto preservar?

  Raciocínio         Convergência       Divergência         Fechar ou manter
                                                            alternativas?

  Qualidade          Consistência       Contextualidade     Uniformidade ou
                                                            adequação?

  Recursos           Eficiência         Profundidade        Economizar ou
                                                            investigar?

  Tempo              Velocidade         Prudência           Agir rapidamente
                                                            ou reduzir
                                                            incerteza?

  Evidência          Certeza            Incerteza           Quanto sabemos?

  Evolução           Conservação        Inovação            Preservar ou
                                                            experimentar?

  Organização        Uniformidade       Diversidade         Padronizar ou
                                                            permitir
                                                            perspectivas?

  Estrutura          Determinação       Emergência          Comportamento
                                                            previsto ou
                                                            emergente?

  Controle           Centralização      Distribuição        Um centro ou
                                                            vários centros?

  Responsabilidade   Individualização   Compartilhamento    Quem responde
                                                            pela decisão?

  Transparência      Explicabilidade    Opacidade funcional Quanto deve ser
                                                            explicado?

  Segurança          Restrição          Utilidade           Quanto limitar
                                                            para reduzir
                                                            risco?

  Contexto           Isolamento         Enriquecimento      Quanto contexto
                                                            fornecer?

  Custo              Frugalidade        Cobertura           Quanto
                                                            investigar?

  Diversidade        Independência      Confluência         Perspectivas
                                                            separadas ou
                                                            integradas?

  Execução           Reversibilidade    Irreversibilidade   Quanto custa
                                                            errar?
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

# 9. Os 4Es como princípio universal

Os 4Es devem ser tratados como uma família de princípios de gestão de
valor:

1.  **Eficiência**
2.  **Eficácia**
3.  **Efetividade**
4.  **Economicidade**

## Eficiência

Fazer bem utilizando recursos de forma adequada.

Pergunta:

> O agente utiliza seus recursos de maneira racional?

## Eficácia

Alcançar o resultado planejado.

Pergunta:

> O objetivo foi atingido?

## Efetividade

Produzir impacto real e útil.

Pergunta:

> O resultado gerou a mudança desejada?

## Economicidade

Obter o valor necessário com uso racional de recursos.

Pergunta:

> O benefício justifica o custo?

## Relação dinâmica

Os 4Es não devem ser simplesmente somados.

Um agente pode:

-   ser eficiente e ineficaz;
-   eficaz e antieconômico;
-   eficaz e pouco efetivo;
-   econômico e insuficiente;
-   efetivo e excessivamente caro.

### Regra universal

> Nenhum E deve ser maximizado isoladamente.

A ponderação depende do contexto.

------------------------------------------------------------------------

# 10. Centralização e descentralização

Centralização e descentralização são princípios estruturais, não dogmas.

## Centralização favorece

-   consistência;
-   controle;
-   política uniforme;
-   decisões críticas;
-   coordenação;
-   governança.

## Descentralização favorece

-   especialização;
-   paralelismo;
-   autonomia;
-   resiliência;
-   velocidade local;
-   diversidade de perspectivas.

## Arquitetura híbrida

Sistemas agenticos maduros frequentemente se beneficiam de:

> autoridade centralizada + execução especializada distribuída.

Exemplo conceitual:

-   Constituição central;
-   políticas centrais;
-   agentes especializados descentralizados;
-   comunicação por contratos;
-   supervisão central;
-   aprendizagem distribuída;
-   arbitragem definida.

A arquitetura não precisa escolher um polo absoluto.

------------------------------------------------------------------------

# 11. Autonomia e Enforcement

Autonomia deve ser especificada como contrato.

## Níveis sugeridos

  Nível   Característica
  ------- -----------------------------------------------
  A0      Observa
  A1      Analisa
  A2      Recomenda
  A3      Delibera
  A4      Executa dentro de limites
  A5      Executa e adapta parâmetros autorizados
  A6      Opera autonomamente dentro de política formal

A existência de A6 não implica liberdade constitucional.

### Regra

> Autonomia aumenta dentro de um espaço de autoridade explicitamente
> definido.

------------------------------------------------------------------------

# 12. Formalidade e interpretação

Sistemas agenticos precisam separar:

-   regras rígidas;
-   conhecimento certificado;
-   heurísticas;
-   interpretação;
-   inferência;
-   opinião;
-   hipótese.

Um modelo de linguagem é particularmente útil quando existe ambiguidade.

Isso não significa permitir que interpretação substitua regras
determinísticas onde estas são obrigatórias.

------------------------------------------------------------------------

# 13. Estabilidade e adaptabilidade

Um agente adaptativo precisa declarar:

### O que pode mudar

-   parâmetros;
-   prioridades operacionais;
-   profundidade;
-   seleção de ferramentas;
-   estratégia de investigação;
-   memória operacional.

### O que não pode mudar autonomamente

-   identidade;
-   autoridade;
-   limites de segurança;
-   princípios constitucionais;
-   contratos fundamentais.

A adaptabilidade deve existir dentro de fronteiras.

------------------------------------------------------------------------

# 14. Divergência, confluência e consenso

Esses conceitos não são sinônimos.

## Divergência

Perspectivas permanecem diferentes.

## Confluência

Perspectivas independentes fornecem suporte para uma mesma
interpretação.

## Consenso

Os participantes chegam a uma conclusão comum.

## Quórum

Existe participação mínima suficiente para uma decisão.

## Unanimidade

Todos concordam.

### Regra importante

> Um sistema não deve forçar consenso quando a divergência representa
> informação válida.

Em sistemas cognitivos, preservar divergência pode ser mais valioso que
produzir uma resposta única prematuramente.

------------------------------------------------------------------------

# 15. Confluência de evidências

Confluência não deve significar quantidade de sinais.

A qualidade da confluência depende de:

-   independência;
-   diversidade metodológica;
-   qualidade da fonte;
-   confiabilidade;
-   relevância;
-   temporalidade;
-   coerência;
-   ausência de dependência causal oculta.

Cinco sinais derivados da mesma fonte não equivalem a cinco evidências
independentes.

------------------------------------------------------------------------

# 16. Teoria universal de ponderação

Ponderação é o processo pelo qual o agente determina **quanto cada
princípio deve influenciar uma decisão em determinado contexto**.

Não é simplesmente atribuir notas.

## 16.1 Variáveis de ponderação

O agente pode considerar:

-   prioridade constitucional;
-   relevância contextual;
-   criticidade;
-   risco;
-   evidência;
-   urgência;
-   impacto;
-   reversibilidade;
-   custo;
-   dependência;
-   temporalidade;
-   confiabilidade;
-   autoridade;
-   incerteza;
-   histórico;
-   sensibilidade;
-   alcance sistêmico.

------------------------------------------------------------------------

# 17. Modelo de ponderação contextual

Uma representação genérica:

> **Peso efetivo = prioridade estrutural × relevância contextual ×
> evidência × criticidade × confiabilidade × fator temporal**

Essa expressão é conceitual.

Não deve ser implementada como fórmula universal.

O agente deve especificar quando:

-   pesos são qualitativos;
-   pesos são quantitativos;
-   pesos são ordenados;
-   existe veto;
-   existe limiar;
-   existe compensação;
-   existe inversão contextual.

------------------------------------------------------------------------

# 18. Formas de ponderação

## 18.1 Hierárquica

Um princípio sempre precede outro.

## 18.2 Condicional

A prioridade depende de uma condição.

## 18.3 Proporcional

O peso varia continuamente.

## 18.4 Qualitativa

Alta, média, baixa.

## 18.5 Quantitativa

Valores numéricos.

## 18.6 Limiar

Abaixo de determinado nível, a ação é bloqueada.

## 18.7 Veto

Uma condição impede a decisão.

## 18.8 Lexicográfica

Primeiro resolve o princípio mais importante; apenas depois considera os
demais.

## 18.9 Multiobjetivo

O agente procura uma solução que atenda simultaneamente vários
objetivos.

## 18.10 Pareto

Nenhum princípio pode melhorar sem piorar outro relevante.

## 18.11 Contextual

Os pesos mudam conforme o contexto.

## 18.12 Temporal

O peso muda ao longo do tempo.

## 18.13 Adaptativa

O sistema aprende ajustes de peso sob governança.

------------------------------------------------------------------------

# 19. Ponderação não é votação

Uma decisão 7 × 3 não significa necessariamente que 7 perspectivas devem
vencer 3.

Uma perspectiva pode ter:

-   maior autoridade;
-   maior independência;
-   maior evidência;
-   maior relevância;
-   menor incerteza.

Logo:

> quantidade de agentes não é equivalente a força epistemológica.

------------------------------------------------------------------------

# 20. Ponderação e autoridade

Toda ponderação deve responder:

-   quem pode influenciar?
-   quem pode bloquear?
-   quem pode recomendar?
-   quem pode decidir?
-   quem pode revisar?
-   quem pode alterar o princípio?

Isso evita confundir:

**opinião → influência → autoridade → decisão.**

------------------------------------------------------------------------

# 21. Contexto

A ponderação só pode ser compreendida dentro do contexto.

O contexto mínimo deve considerar, quando aplicável:

### Contexto operacional

O que está acontecendo agora?

### Contexto temporal

Há urgência? Prazo? Expiração?

### Contexto cognitivo

Qual o estado atual do raciocínio?

### Contexto de risco

Qual o dano potencial?

### Contexto de autoridade

Quem pode decidir?

### Contexto de recursos

Quanto tempo, tokens, memória e ferramentas existem?

### Contexto sistêmico

Qual o impacto sobre outros agentes?

### Contexto histórico

O que aconteceu anteriormente?

### Contexto epistemológico

Quanto sabemos e quanto é incerto?

------------------------------------------------------------------------

# 22. Princípios de economia cognitiva

Agentes devem evitar pensar profundamente quando não existe motivo
suficiente.

O princípio é:

> **A profundidade cognitiva deve ser proporcional à necessidade
> decisória.**

Isso pode ser implementado por:

-   escalonamento;
-   orçamento cognitivo;
-   orçamento de tokens;
-   prioridades;
-   interrupção;
-   execução concorrente;
-   investigação progressiva.

O sistema deve economizar recursos **sem economizar a qualidade
necessária**.

------------------------------------------------------------------------

# 23. Especialização e generalização

## Especialização

Aumenta:

-   profundidade;
-   precisão de domínio;
-   responsabilidade;
-   auditabilidade local.

Pode reduzir:

-   visão global;
-   capacidade de integração.

## Generalização

Aumenta:

-   flexibilidade;
-   integração;
-   cobertura.

Pode reduzir:

-   profundidade;
-   clareza de responsabilidade.

### Boa prática

Especialização local + integração sistêmica.

------------------------------------------------------------------------

# 24. Local e global

Uma decisão local pode ser ótima para um agente e ruim para o sistema.

O agente deve considerar:

> benefício local × consequência sistêmica.

Esse princípio é especialmente importante em multiagentes.

------------------------------------------------------------------------

# 25. Independência e integração

Agentes independentes produzem diversidade.

Agentes integrados produzem coordenação.

Arquitetura recomendada:

> independência na formação de perspectivas + integração na deliberação.

Essa separação reduz pensamento de grupo e mantém especialização.

------------------------------------------------------------------------

# 26. Determinismo e probabilismo

Use determinismo quando:

-   regras são claras;
-   risco é elevado;
-   comportamento deve ser reproduzível;
-   há requisito legal ou de segurança.

Use probabilismo quando:

-   o problema é inerentemente incerto;
-   múltiplas hipóteses são plausíveis;
-   dados são incompletos.

Arquiteturas híbridas são normalmente mais adequadas.

------------------------------------------------------------------------

# 27. Reatividade e deliberação

Um agente precisa saber quando:

### Reagir

-   evento crítico;
-   condição previamente definida;
-   baixo espaço para deliberação.

### Deliberar

-   alta incerteza;
-   conflito de princípios;
-   impacto elevado;
-   irreversibilidade;
-   múltiplas alternativas.

------------------------------------------------------------------------

# 28. Reversibilidade

A reversibilidade deve influenciar fortemente a ponderação.

Quanto mais irreversível a ação:

-   maior validação;
-   maior supervisão;
-   maior explicabilidade;
-   maior exigência de evidência;
-   menor autonomia.

Uma ação facilmente reversível pode tolerar maior autonomia.

------------------------------------------------------------------------

# 29. Proporcionalidade

Governança deve ser proporcional ao risco.

Não aplicar:

> governança máxima para tudo.

Nem:

> autonomia máxima para tudo.

O correto é:

> risco → impacto → autoridade → controles.

------------------------------------------------------------------------

# 30. Segurança e utilidade

Segurança excessiva pode tornar o sistema inútil.

Autonomia excessiva pode torná-lo perigoso.

O objetivo é construir um espaço operacional em que:

-   o agente tenha capacidade suficiente;
-   os limites sejam claros;
-   o risco seja observável;
-   a autoridade seja proporcional;
-   exista recuperação.

------------------------------------------------------------------------

# 31. Comunicação entre agentes

Uma arquitetura multiagente deve definir:

-   quem publica;
-   quem consome;
-   quais contratos existem;
-   qual contexto acompanha a mensagem;
-   como versões são tratadas;
-   como conflitos são registrados;
-   como alterações são auditadas.

A comunicação declarativa é particularmente útil:

> agentes declaram o que observaram, inferiram, mudaram, esperam ou
> invalidaram; o consumidor decide como reagir dentro de sua autoridade.

------------------------------------------------------------------------

# 32. Memória, conhecimento e aprendizagem

Separar:

-   memória de trabalho;
-   memória operacional;
-   memória episódica;
-   memória semântica;
-   memória estatística;
-   memória estratégica;
-   conhecimento protegido;
-   conhecimento adaptativo.

Uma arquitetura governável deve declarar:

> o que o agente pode aprender e o que ele nunca pode alterar
> autonomamente.

------------------------------------------------------------------------

# 33. Meta-cognição

Todo sistema agentico suficientemente complexo deve considerar uma
camada que observe:

-   qualidade do raciocínio;
-   vieses;
-   conflitos;
-   dominância de agentes;
-   excesso de confirmação;
-   consumo de recursos;
-   instabilidade;
-   excesso de confiança;
-   baixa diversidade;
-   degradação.

A meta-cognição não deve necessariamente decidir o problema.

Sua função principal pode ser:

> observar como o sistema está pensando.

------------------------------------------------------------------------

# 34. Harness e enforcement

Princípios precisam existir em diferentes níveis.

## Nível declarativo

Documentação.

## Nível instrucional

Prompts e instruções.

## Nível contratual

Schemas e contratos.

## Nível operacional

Orquestração e políticas.

## Nível de enforcement

Mecanismos que impedem violações.

## Nível de avaliação

Testes e métricas.

## Nível de auditoria

Registro e reconstrução.

Uma boa arquitetura não confia exclusivamente na interpretação do LLM.

------------------------------------------------------------------------

# 35. Quando um princípio deve virar enforcement

Pergunte:

1.  A violação causa dano relevante?
2.  O comportamento é verificável?
3.  A regra é suficientemente objetiva?
4.  O custo do enforcement é justificável?
5.  O enforcement pode gerar efeitos indesejados?
6.  Existe alternativa menos rígida?

Se sim, considerar enforcement.

Se não, manter como orientação deliberativa.

------------------------------------------------------------------------

# 36. PDCA aplicado aos princípios

## PLAN

Definir:

-   princípios;
-   relações;
-   conflitos;
-   pesos;
-   limites;
-   critérios.

## DO

Executar o comportamento especificado.

## CHECK

Medir:

-   resultados;
-   violações;
-   conflitos;
-   eficiência;
-   qualidade;
-   efeitos emergentes.

## ACT

Ajustar:

-   parâmetros;
-   pesos;
-   procedimentos;
-   relações;
-   mecanismos de governança.

Alterações constitucionais devem seguir processo próprio.

------------------------------------------------------------------------

# 37. Princípios de evolução

## Evolução conservadora

Mudanças devem demonstrar benefício sem degradar:

-   coerência;
-   estabilidade;
-   auditabilidade;
-   explicabilidade;
-   reprodutibilidade.

## Evolução experimental

Novos princípios ou estratégias podem ser testados em:

-   sandbox;
-   simulação;
-   avaliação;
-   piloto;
-   comparação.

Nunca assumir que uma ideia nova é melhor apenas por ser nova.

------------------------------------------------------------------------

# 38. Princípio da não dominação

Nenhum agente especializado deve dominar permanentemente a decisão
apenas porque:

-   produz mais mensagens;
-   possui mais ferramentas;
-   tem maior frequência;
-   é mais eloquente;
-   gera maior volume de evidências.

Influência deve depender de:

-   competência;
-   relevância;
-   evidência;
-   independência;
-   contexto.

------------------------------------------------------------------------

# 39. Princípio da não redução

Não reduzir fenômenos complexos a uma única dimensão quando múltiplas
dimensões forem relevantes.

Exemplo:

Não substituir:

-   qualidade;
-   risco;
-   contexto;
-   incerteza;

por apenas uma pontuação.

------------------------------------------------------------------------

# 40. Princípio da preservação da incerteza

Quando a evidência não permite conclusão segura:

> o agente deve preservar a incerteza em vez de fabricar certeza.

Isso pode resultar em:

-   hipóteses concorrentes;
-   baixa convicção;
-   solicitação de informação;
-   adiamento;
-   ação conservadora.

------------------------------------------------------------------------

# 41. Princípio da suficiência

O objetivo não é maximizar análise.

É alcançar o nível de análise necessário para a decisão.

> suficiente ≠ máximo.

Esse princípio é essencial para controlar custo cognitivo.

------------------------------------------------------------------------

# 42. Princípio da rastreabilidade

Toda decisão relevante deve permitir reconstrução:

**contexto → princípios → evidências → ponderação → conflito → decisão →
consequência.**

------------------------------------------------------------------------

# 43. Princípio da explicabilidade da ponderação

Não basta explicar a decisão.

Quando princípios conflitarem, o sistema deve ser capaz de explicar:

> por que determinado princípio recebeu maior peso naquele contexto.

------------------------------------------------------------------------

# 44. Princípio da separação de perspectivas

Em sistemas multiagentes:

> formar perspectivas separadamente pode ser mais importante que
> integrá-las cedo.

Evita:

-   contaminação;
-   ancoragem;
-   confirmação;
-   pensamento de grupo.

------------------------------------------------------------------------

# 45. Princípio da confluência qualificada

Confluência forte exige:

-   independência;
-   relevância;
-   qualidade;
-   coerência;
-   ausência de dependência oculta.

------------------------------------------------------------------------

# 46. Princípio da contestação

Toda decisão de alto impacto deve considerar, quando viável:

-   contraevidência;
-   hipótese alternativa;
-   agente crítico;
-   teste de falsificação;
-   cenário adverso.

------------------------------------------------------------------------

# 47. Princípio da proporcionalidade de governança

Quanto maior:

-   risco;
-   impacto;
-   irreversibilidade;
-   autonomia;
-   conectividade;

maior deve ser a governança.

------------------------------------------------------------------------

# 48. Princípio da simplicidade suficiente

Toda complexidade deve justificar sua existência.

Antes de criar:

-   novo agente;
-   novo princípio;
-   novo engine;
-   novo protocolo;
-   nova camada;

perguntar:

> A capacidade já existe em outro mecanismo?

Isso evita duplicação e múltiplas fontes de verdade.

------------------------------------------------------------------------

# 49. Matriz Universal de Princípios

Cada agente deve possuir uma matriz como:

  -------------------------------------------------------------------------------------------------------------------------------------------------
  ID    Princípio    Classe           Complementa      Antagoniza     Depende       Precede      Contexto   Peso    Limite       Veto   Evidência
  ----- ------------ ---------------- ---------------- -------------- ------------- ------------ ---------- ------- ------------ ------ -----------
  P01   Segurança    Constitucional   Integridade      Utilidade      Autoridade    Velocidade   Alto risco Muito   Não absoluto Sim    Alta
                                                       irrestrita                                           alto                        

  P02   Eficiência   Basilar          Economicidade    Profundidade   Suficiência   ---          Rotina     Médio   Contextual   Não    Alta
                                                       excessiva                                                                        

  P03   Autonomia    Estrutural       Especialização   Enforcement    Autoridade    ---          Baixo      Médio   Delimitada   Não    Alta
                                                       excessivo                                 risco                                  
  -------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 50. Ficha universal de princípio

``` text
PRINCIPLE ID:
NAME:

CLASS:
CONTEXT:

PURPOSE:
DEFINITION:

APPLIES WHEN:
DOES NOT APPLY WHEN:

COMPLEMENTS:
ANTAGONISTS:
DEPENDENCIES:
REINFORCEMENTS:
CONTAINMENTS:

PRECEDENCE:
WEIGHTING MODE:

TRIGGERS:
THRESHOLDS:
VETO CONDITIONS:

EVIDENCE:
UNCERTAINTY:

REVERSIBILITY:
SYSTEMIC IMPACT:
TEMPORALITY:

OBSERVABILITY:
AUDITABILITY:

WHAT THE AGENT MAY ADAPT:
WHAT THE AGENT MUST NEVER CHANGE:

SUCCESS CRITERIA:
FAILURE MODES:

GOVERNANCE OWNER:
VERSION:
STATUS:
```

------------------------------------------------------------------------

# 51. Matriz de conflito

  --------------------------------------------------------------------------------------------------
  Princípio A  Princípio B    Tipo          Contexto       Quem prevalece Condição       Evidência
  ------------ -------------- ------------- -------------- -------------- -------------- -----------
  Autonomia    Enforcement    Antagonismo   Alto risco     Enforcement    Risco crítico  Política

  Eficiência   Profundidade   Trade-off     Investigação   Profundidade   Alto impacto   Resultado

  Exploração   Conservação    Divergência   Aprendizagem   Contextual     Fase           Avaliação
                                                                          experimental   
  --------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 52. Matriz de decisão

Antes de uma decisão relevante, o agente deve responder:

1.  Qual é o contexto?
2.  Quais princípios se aplicam?
3.  Quais são complementares?
4.  Quais são antagonistas?
5.  Existe conflito?
6.  Existe veto?
7.  Qual é a hierarquia?
8.  Qual é a evidência?
9.  Qual é a incerteza?
10. Qual é a reversibilidade?
11. Qual é o impacto?
12. Qual é o custo?
13. Qual é o peso contextual?
14. Quais alternativas existem?
15. Qual é a consequência de cada alternativa?
16. Qual princípio foi sacrificado?
17. Por quê?
18. Como a decisão será monitorada?
19. Quando deverá ser reavaliada?

------------------------------------------------------------------------

# 53. Algoritmo cognitivo universal

``` text
1. PERCEBER
      ↓
2. CONSTRUIR CONTEXTO
      ↓
3. IDENTIFICAR OBJETIVO
      ↓
4. IDENTIFICAR PRINCÍPIOS
      ↓
5. CLASSIFICAR RELAÇÕES
      ↓
6. IDENTIFICAR CONFLITOS
      ↓
7. IDENTIFICAR RESTRIÇÕES E VETOS
      ↓
8. COLETAR EVIDÊNCIAS
      ↓
9. AVALIAR INCERTEZA
      ↓
10. PONDERAR
      ↓
11. GERAR ALTERNATIVAS
      ↓
12. SIMULAR CONSEQUÊNCIAS
      ↓
13. DELIBERAR
      ↓
14. DECIDIR
      ↓
15. EXPLICAR
      ↓
16. EXECUTAR OU RECOMENDAR
      ↓
17. OBSERVAR RESULTADO
      ↓
18. APRENDER
      ↓
19. REAVALIAR PRINCÍPIOS OPERACIONAIS
```

------------------------------------------------------------------------

# 54. Arquitetura de uso em sistemas multiagentes

A matriz de princípios pode existir em três níveis.

## Nível 1 --- Sistema

Define princípios globais.

## Nível 2 --- Agente

Define como cada agente interpreta os princípios dentro de seu domínio.

## Nível 3 --- Tarefa

Define a ponderação específica daquela missão.

Exemplo:

``` text
Constituição do Sistema
        ↓
Princípios Globais
        ↓
Políticas do Agente
        ↓
Contexto da Missão
        ↓
Ponderação Local
        ↓
Decisão
```

------------------------------------------------------------------------

# 55. Orquestração e princípios

O orquestrador pode usar a matriz para decidir:

-   qual agente chamar;
-   quando chamar;
-   quantos agentes chamar;
-   em paralelo ou sequência;
-   com qual profundidade;
-   com qual orçamento;
-   quando interromper;
-   quando escalar;
-   quando solicitar humano.

Assim, a ponderação de princípios deixa de ser apenas textual e
influencia o fluxo cognitivo.

------------------------------------------------------------------------

# 56. Agentes especializados

Cada agente deve declarar:

### Identidade

Quem sou?

### Domínio

O que conheço?

### Responsabilidade

O que devo produzir?

### Limites

O que não posso fazer?

### Autoridade

O que posso decidir?

### Princípios locais

Quais princípios têm maior peso no meu domínio?

### Princípios globais

Quais princípios nunca posso violar?

### Relações

Com quais agentes tenho dependência, complementaridade ou conflito?

### Comunicação

O que publico?

### Consumo

O que posso consumir?

------------------------------------------------------------------------

# 57. Agente supervisor

O supervisor pode observar:

-   violações;
-   ponderações anômalas;
-   conflitos repetitivos;
-   dominância;
-   custo;
-   instabilidade;
-   deriva;
-   excesso de autonomia;
-   excesso de bloqueio.

O supervisor não deve necessariamente substituir o agente.

------------------------------------------------------------------------

# 58. Harness cognitivo

O Harness pode testar:

## Testes de princípio

O agente respeita o princípio?

## Testes de conflito

Como reage quando dois princípios entram em oposição?

## Testes de inversão

O agente altera a prioridade quando o contexto muda?

## Testes de veto

Respeita bloqueios?

## Testes de autonomia

Opera dentro de sua autoridade?

## Testes de emergência

Detecta comportamentos inesperados?

## Testes de deriva

Os pesos mudam indevidamente ao longo do tempo?

## Testes de confluência

Confunde quantidade com independência?

## Testes de explicabilidade

Consegue explicar a ponderação?

------------------------------------------------------------------------

# 59. Anti-padrões

## 59.1 Princípio decorativo

O princípio existe no documento, mas nunca influencia comportamento.

## 59.2 Princípio absoluto indevido

Toda regra vira prioridade máxima.

## 59.3 Pontuação simplista

Toda decisão vira soma de pontos.

## 59.4 Consensus washing

O sistema chama de consenso uma simples maioria.

## 59.5 Confluência falsa

Múltiplas evidências dependentes são tratadas como independentes.

## 59.6 Autonomia sem autoridade

O agente pode fazer coisas que ninguém explicitamente autorizou.

## 59.7 Flexibilidade sem limites

O agente pode alterar regras fundamentais.

## 59.8 Governança excessiva

Controles impedem o agente de cumprir sua função.

## 59.9 Complexidade ornamental

Criam-se camadas sem necessidade real.

## 59.10 Explicação pós-hoc

A justificativa é produzida depois apenas para racionalizar a decisão.

## 59.11 Colapso prematuro

O sistema elimina hipóteses concorrentes cedo demais.

## 59.12 Dominância de ferramenta

O agente confunde informação disponível com informação verdadeira.

------------------------------------------------------------------------

# 60. Critérios de qualidade

Uma especificação de princípios é madura quando:

-   os princípios têm definição clara;
-   as classes estão identificadas;
-   relações estão explicitadas;
-   conflitos são conhecidos;
-   prioridades são justificadas;
-   contexto altera pesos quando necessário;
-   vetos estão definidos;
-   autoridade está definida;
-   reversibilidade é considerada;
-   evidências são rastreáveis;
-   decisões podem ser auditadas;
-   aprendizagem não rompe a constituição;
-   o sistema preserva incerteza;
-   a complexidade é proporcional ao problema.

------------------------------------------------------------------------

# 61. Checklist universal

## Princípios

-   [ ] Objetivo definido
-   [ ] Princípios identificados
-   [ ] Classes definidas
-   [ ] Limites definidos
-   [ ] Evidências registradas

## Dinâmica

-   [ ] Complementaridade
-   [ ] Dependência
-   [ ] Hierarquia
-   [ ] Antagonismo
-   [ ] Conflito
-   [ ] Compensação
-   [ ] Trade-off
-   [ ] Convergência
-   [ ] Divergência
-   [ ] Contestação
-   [ ] Arbitragem
-   [ ] Gating
-   [ ] Veto
-   [ ] Escalonamento
-   [ ] Inversão contextual
-   [ ] Emergência
-   [ ] Degeneração
-   [ ] Expiração

## Ponderação

-   [ ] Contexto
-   [ ] Criticidade
-   [ ] Evidência
-   [ ] Risco
-   [ ] Reversibilidade
-   [ ] Autoridade
-   [ ] Custo
-   [ ] Temporalidade
-   [ ] Incerteza

## Arquitetura

-   [ ] Centralização
-   [ ] Descentralização
-   [ ] Especialização
-   [ ] Integração
-   [ ] Independência
-   [ ] Comunicação
-   [ ] Memória
-   [ ] Aprendizagem
-   [ ] Supervisão

## Governança

-   [ ] Enforcement
-   [ ] Auditoria
-   [ ] Observabilidade
-   [ ] Explicabilidade
-   [ ] Versionamento
-   [ ] Recuperação
-   [ ] Evolução
-   [ ] Human-in-the-loop quando necessário

------------------------------------------------------------------------

# 62. Procedimento para construção de um novo agente

## Etapa 1 --- Definir finalidade

Não começar pelos princípios.

Começar por:

> qual problema o agente existe para resolver?

## Etapa 2 --- Mapear autoridade

Definir:

-   o que pode fazer;
-   o que pode recomendar;
-   o que pode decidir;
-   o que não pode fazer.

## Etapa 3 --- Identificar princípios

Separar:

-   globais;
-   locais;
-   constitucionais;
-   operacionais;
-   situacionais.

## Etapa 4 --- Mapear relações

Para cada princípio:

-   complementa;
-   depende;
-   reforça;
-   antagoniza;
-   limita;
-   compete;
-   substitui;
-   converge;
-   diverge.

## Etapa 5 --- Mapear contexto

Identificar quando os pesos mudam.

## Etapa 6 --- Definir ponderação

Escolher:

-   hierárquica;
-   condicional;
-   proporcional;
-   limiar;
-   veto;
-   multiobjetivo;
-   adaptativa.

## Etapa 7 --- Definir comportamento

Converter princípios em:

-   regras;
-   políticas;
-   heurísticas;
-   mecanismos;
-   contratos.

## Etapa 8 --- Definir observabilidade

Registrar:

-   contexto;
-   princípios considerados;
-   conflitos;
-   peso;
-   decisão;
-   resultado.

## Etapa 9 --- Testar

Testar:

-   normal;
-   conflito;
-   adversarial;
-   ambíguo;
-   extremo;
-   mudança de contexto.

## Etapa 10 --- Governar

Definir:

-   quem pode alterar;
-   como altera;
-   evidência necessária;
-   critérios de aceitação;
-   rollback.

------------------------------------------------------------------------

# 63. Princípios mínimos universais recomendados

Nem todo sistema precisa de todos.

Porém, a especificação deve avaliar explicitamente:

1.  propósito;
2.  autoridade;
3.  segurança;
4.  proporcionalidade;
5.  contexto;
6.  rastreabilidade;
7.  explicabilidade;
8.  incerteza;
9.  reversibilidade;
10. eficiência;
11. eficácia;
12. efetividade;
13. economicidade;
14. autonomia;
15. enforcement;
16. estabilidade;
17. adaptabilidade;
18. especialização;
19. integração;
20. centralização;
21. descentralização;
22. convergência;
23. divergência;
24. contestação;
25. memória;
26. esquecimento;
27. exploração;
28. conservação;
29. determinismo;
30. probabilismo;
31. velocidade;
32. prudência;
33. simplicidade;
34. evolução;
35. auditabilidade.

A lista é um **catálogo de análise**, não uma obrigação de implementar
todos.

------------------------------------------------------------------------

# 64. Regra contra universalização indevida

Este manual é universal.

Isso não significa que todos os princípios devam existir em todos os
agentes.

A regra é:

> **Universalizar o método de análise, não o conteúdo da decisão.**

Um agente médico, documental, financeiro e educacional podem usar a
mesma engenharia de princípios e chegar a matrizes completamente
diferentes.

------------------------------------------------------------------------

# 65. Relação com documentação de governança

O manual deve funcionar como uma camada anterior às especificações
específicas.

Arquitetura documental recomendada:

``` text
MANUAL UNIVERSAL
      ↓
CONSTITUIÇÃO DO SISTEMA
      ↓
ARQUITETURA
      ↓
ESPECIFICAÇÃO DO AGENTE
      ↓
CONTRATOS
      ↓
POLÍTICAS
      ↓
HARNESS
      ↓
AVALIAÇÃO
      ↓
IMPLEMENTAÇÃO
```

Assim, o manual não cria uma segunda constituição.

Ele ensina **como construir a constituição e as especificações de
maneira ponderada**.

------------------------------------------------------------------------

# 66. Aplicação dentro do ciclo PDCA

## PLAN

Engenharia dos princípios.

## DO

Execução das políticas e comportamentos.

## CHECK

Verificação da qualidade da ponderação.

## ACT

Evolução controlada dos pesos, mecanismos e relações.

Esse desenho permite que a dimensão de princípios atravesse todo o ciclo
sem se transformar em um componente isolado.

------------------------------------------------------------------------

# 67. Aplicação à documentação produzida por LLM

Quando uma LLM recebe a tarefa de especificar um agente, ela não deve
imediatamente escrever a solução.

Deve primeiro executar:

``` text
ENTENDER
↓
IDENTIFICAR OBJETIVO
↓
IDENTIFICAR CONTEXTO
↓
LEVANTAR PRINCÍPIOS
↓
AUDITAR PRINCÍPIOS EXISTENTES
↓
IDENTIFICAR RELAÇÕES
↓
IDENTIFICAR TENSÕES
↓
IDENTIFICAR DUPLICAÇÕES
↓
IDENTIFICAR CONFLITOS
↓
DEFINIR PONDERAÇÃO
↓
DEFINIR LIMITES
↓
DEFINIR COMPORTAMENTO
↓
DEFINIR OBSERVABILIDADE
↓
VALIDAR
↓
DOCUMENTAR
```

------------------------------------------------------------------------

# 68. Protocolo obrigatório para LLM

Antes de propor um novo princípio:

### Pergunta 1

Esse princípio já existe?

### Pergunta 2

É apenas outra formulação de um princípio existente?

### Pergunta 3

É uma regra derivada?

### Pergunta 4

É uma política?

### Pergunta 5

É um parâmetro?

### Pergunta 6

É uma tensão entre princípios já existentes?

### Pergunta 7

É um mecanismo para resolver essa tensão?

### Pergunta 8

É realmente uma nova capacidade?

### Pergunta 9

Qual o impacto sobre princípios existentes?

### Pergunta 10

Existe evidência suficiente para incorporá-lo?

Isso evita que a documentação cresça por duplicação semântica.

------------------------------------------------------------------------

# 69. Registro de decisão de princípio

Toda alteração relevante deve possuir:

``` text
DECISION ID:
DATE:
PROPOSAL:
CURRENT PRINCIPLES:
NEW PRINCIPLE:
RELATIONSHIP:
RATIONALE:
EVIDENCE:
RISKS:
TRADE-OFFS:
EXPECTED BENEFIT:
ALTERNATIVES:
REJECTED ALTERNATIVES:
IMPACT:
REVERSIBILITY:
APPROVAL:
VERSION:
STATUS:
```

------------------------------------------------------------------------

# 70. Benchmark interno para novos princípios

Antes de incorporar uma nova ideia, classificá-la:

### NOVA CONTRIBUIÇÃO

Não existe equivalente relevante.

### JÁ CONTEMPLADA

Já existe no acervo.

### REFINAMENTO

Existe, mas a nova formulação adiciona precisão.

### REORGANIZAÇÃO

Não adiciona capacidade; apenas reorganiza.

### DUPLICAÇÃO

Cria segunda fonte de verdade.

### CONFLITO

Contradiz princípio existente.

### NÃO JUSTIFICADA

Interessante, mas sem evidência ou necessidade suficiente.

Essa classificação deve ser obrigatória em projetos com documentação
extensa.

------------------------------------------------------------------------

# 71. Relação entre princípio, mecanismo e instrumento

## Princípio

> O que deve orientar.

## Mecanismo

> Como o sistema implementa a orientação.

## Instrumento

> Qual ferramenta ou componente materializa o mecanismo.

Exemplo:

**Princípio:** proporcionalidade.

**Mecanismo:** escalonamento de governança conforme risco.

**Instrumento:** policy engine.

Outro exemplo:

**Princípio:** independência de perspectivas.

**Mecanismo:** análise paralela.

**Instrumento:** orquestrador concorrente.

Essa separação é essencial para evitar confusão arquitetural.

------------------------------------------------------------------------

# 72. Organicidade

A organicidade de um sistema agentico não significa fazê-lo comportar-se
como um organismo biológico.

Significa permitir:

-   percepção;
-   interpretação;
-   diferenciação;
-   interação;
-   adaptação;
-   preservação de identidade;
-   memória;
-   esquecimento;
-   feedback;
-   autorregulação;
-   recuperação;
-   evolução.

Uma formulação operacional:

``` text
PERCEBER
↓
INTERPRETAR
↓
DIVERGIR
↓
PONDERAR
↓
CONFLUIR
↓
DECIDIR
↓
AGIR
↓
OBSERVAR CONSEQUÊNCIA
↓
APRENDER
↓
ADAPTAR
↓
PRESERVAR IDENTIDADE
```

Organicidade, portanto, não é ausência de regras.

É **capacidade de manter identidade enquanto adapta comportamento**.

------------------------------------------------------------------------

# 73. O que este manual não deve fazer

Este manual não deve:

-   definir a arquitetura de um sistema específico;
-   substituir uma constituição;
-   definir prompts concretos;
-   escolher modelos LLM;
-   impor multiagentes;
-   impor centralização;
-   impor descentralização;
-   impor consenso;
-   impor autonomia;
-   impor uma fórmula universal de pontuação;
-   substituir avaliação;
-   substituir segurança;
-   substituir contratos;
-   transformar todos os princípios em regras rígidas.

------------------------------------------------------------------------

# 74. Critério de maturidade do agente

### Nível 0 --- Regra

O agente apenas segue instruções.

### Nível 1 --- Contexto

O agente adapta comportamento ao contexto.

### Nível 2 --- Ponderação

O agente reconhece conflitos entre princípios.

### Nível 3 --- Deliberação

O agente compara alternativas segundo princípios.

### Nível 4 --- Metacognição

O agente avalia a qualidade da própria ponderação.

### Nível 5 --- Evolução governada

O sistema aprende quais estratégias de ponderação funcionam melhor sem
alterar autonomamente sua identidade constitucional.

------------------------------------------------------------------------

# 75. Critério final de excelência

Um sistema agentico maduro não é aquele que possui mais princípios.

É aquele que consegue:

> **identificar quais princípios importam, compreender como eles se
> relacionam, reconhecer quando entram em tensão, ponderá-los
> proporcionalmente ao contexto, preservar incerteza quando necessário,
> agir dentro de sua autoridade e explicar por que tomou determinada
> decisão.**

------------------------------------------------------------------------

# 76. Referências de benchmark

## NIST

**AI Risk Management Framework / Playbook**

https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook

Uso neste manual: - governança; - risco; - avaliação; -
confiabilidade; - ciclo de vida.

## NIST CAISI

**Guidelines / AI Agent Standards Initiative**

https://www.nist.gov/caisi/guidelines

Uso: - evolução das práticas de padronização e avaliação de agentes.

## Anthropic

**Framework for Developing Safe and Trustworthy Agents**

https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents

Uso: - autonomia; - controle humano; - confiança; - governança de
agentes.

## Microsoft

**Multi-agent patterns**

https://learn.microsoft.com/en-us/agents/architecture/multi-agent-patterns

Uso: - orquestração; - contratos; - MCP; - A2A; - least privilege; -
simplicidade; - auditabilidade.

## Microsoft Azure Architecture Center

**AI Agent Orchestration Patterns**

https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns

Uso: - sequencial; - concorrente; - handoff; - magentic; - escolha
proporcional da complexidade.

## Google Cloud

**Design patterns for agentic AI systems**

https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

Uso: - seleção de padrões; - adequação arquitetural; - organização de
agentes e workflows.

## OWASP

**Agentic AI Threats and Mitigations**

https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/

Uso: - ameaças; - autonomia; - memória; - ferramentas; - identidade; -
supervisão; - interação entre agentes.

## OWASP

**State of Agentic AI Security and Governance**

https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/

Uso: - panorama contemporâneo de segurança e governança agentica.

------------------------------------------------------------------------

# 77. Referências internas utilizadas na construção

Este manual também foi confrontado com o acervo arquitetural do projeto.

Foram considerados especialmente:

-   **ENGENHARIA GERAL.pdf**
-   **KERNEL V2.docx.pdf**
-   **AUDITORIA DE IDEIAS NÃO IMPLEMENTADAS.pdf**
-   **Unidade Atômica de Especificação do Harness Cognitivo do SOT**

Do acervo interno foram preservados, entre outros:

-   separação entre constituição, conhecimento, operação e aprendizagem;
-   autonomia delimitada;
-   evolução conservadora;
-   explicabilidade;
-   auditabilidade;
-   comunicação declarativa;
-   especialização;
-   desacoplamento;
-   Event Bus;
-   Blackboard;
-   Knowledge Graph;
-   hipóteses concorrentes;
-   confluência;
-   contraevidência;
-   metacognição;
-   Cognitive Scheduler;
-   orçamento cognitivo;
-   eficiência subordinada à qualidade necessária;
-   separação entre conhecimento protegido e conhecimento adaptativo;
-   versionamento;
-   rastreabilidade;
-   critérios de aceitação.

No SOT, por exemplo, a arquitetura já explicita que eficiência não deve
economizar recursos sacrificando qualidade e que a execução cognitiva
deve ser escalonada conforme prioridade, dependência, custo, urgência,
maturidade da hipótese e orçamento cognitivo.

Também já existe uma concepção de autonomia graduada para Skills, com
limites explícitos e proibição de alteração autônoma da Constituição.

A arquitetura interna ainda estabelece comunicação desacoplada,
versionada e auditável, em vez de dependências diretas entre Skills.

Esses elementos não são recriados como novas verdades pelo presente
manual. Eles são tratados como **casos concretos de aplicação da teoria
universal de princípios**.

------------------------------------------------------------------------

# 78. Regra de governança deste manual

Este documento deve permanecer **metodológico**.

Se um projeto específico criar:

-   uma Constituição;
-   uma política;
-   um princípio especializado;
-   uma regra operacional;
-   um mecanismo;
-   um contrato;

essas definições pertencem ao projeto específico.

O manual apenas fornece a linguagem e o método para construí-las.

------------------------------------------------------------------------

# 79. Fórmula conceitual final

A engenharia universal de agentes pode ser resumida como:

> **Objetivo + Contexto + Princípios + Relações + Evidências +
> Ponderação + Autoridade + Ação + Feedback + Governança**

E a qualidade do agente pode ser entendida como:

> **capacidade de adaptar o comportamento sem perder identidade,
> deliberar sem fabricar certeza, exercer autonomia sem ultrapassar
> autoridade e evoluir sem destruir a coerência do sistema.**

------------------------------------------------------------------------

# 80. Status recomendado

**Este manual deve ser tratado inicialmente como BASE METODOLÓGICA
UNIVERSAL --- versão proposta.**

Antes de congelá-lo:

1.  realizar auditoria contra todo o acervo de governança do projeto;
2.  identificar duplicações semânticas;
3.  validar o catálogo de dinâmicas;
4.  testar o manual em pelo menos três arquiteturas agenticas
    diferentes;
5.  testar aplicação em agente único, multiagente e workflow híbrido;
6.  testar conflitos de princípios;
7.  testar ponderação contextual;
8.  testar o manual contra cenários adversariais;
9.  validar sua utilidade para geração de documentação por LLM;
10. somente então congelar uma versão normativa.

**Princípio final:**

> O manual deve ensinar o agente a raciocinar sobre princípios; não deve
> tentar pensar pelo agente.
