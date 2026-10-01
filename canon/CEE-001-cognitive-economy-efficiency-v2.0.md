# CEE-001 — Cognitive Economy & Efficiency Specification

**Especificação de Economia e Eficiência Cognitiva do ORYX AGENT**

| Campo | Valor |
|---|---|
| Versão | **2.0** (v1.1 + emenda de 2026-09-14; ver seção EMENDA v2.0 ao final) |
| Status | **BASELINED — Andraus, 2026-09-14.** Emenda v2.0 adiciona §11 (Salvaguardas de Sinal, Q-003) e §12 (Framework 4Es, Q-009). |
| Camada | Governança (Layer 1) — documento transversal |
| Referenciado por | GAS, GMC-001, GES (Doc. 12), DCEBS (Doc. 13), Cognitive Scheduler (EC-COG) |
| Papéis envolvidos nesta versão | ESTRATEGISTA (políticas, regramentos e disciplinas — fechados nesta revisão) / ANALISTA (auditoria de conformidade arquitetural — versão anterior) |
| Fundamentação | ENGENHARIA_GERAL, AUDITORIA_DE_IDEIAS_NÃO_IMPLEMENTADAS, KERNEL V2 |

## Sumário

1. Missão
2. Filosofia — O Framework 3E
3. Princípio Fundamental — Hierarquia de Prioridade
4. Onde a Economia Já Está Embutida na Arquitetura
5. Roteamento por Complexidade Cognitiva
6. Cache de Contexto Cognitivo — Contrato Formal (DCEBS)
7. Métricas de Governança Econômica — Limiares Numéricos (Fase Piloto)
8. Certificação Econômica — Extensão do Pipeline GES
9. Autoridade de Homologação de Roteamento
10. Salvaguardas Constitucionais
11. Papel no Ciclo de Vida
12. Critérios de Aceitação
13. Registro para o CONTROLADOR
14. Histórico de Versões

---

## 1. Missão

O CEE-001 estabelece o padrão obrigatório de uso econômico de inferência de IA (chamadas de API, tokens, escolha de modelo) para todos os componentes do ORYX AGENT, garantindo que a busca por eficiência de custo **nunca** degrade a qualidade analítica que a arquitetura foi construída para proteger.

Sua missão é responder, para cada componente do sistema:

> "Este componente está gastando o recurso computacional mínimo necessário para cumprir sua missão cognitiva com o padrão de qualidade exigido pela Constituição do ORYX?"

Este documento não define *o que* os agentes pensam — isso é papel do GMC-001, do CEM-001 e das especificações verticais (SAS, IIES, etc.). Ele define *quanto custa* pensar, e como esse custo é governado.

---

## 2. Filosofia — O Framework 3E

> **Atualização v2.0 (Q-009):** este framework foi **estendido para 4Es** com a adição de **Economicidade** como 4º nível — ver **§12** (Emenda v2.0). A hierarquia vigente é: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade. As subseções §2-3 abaixo descrevem os 3 primeiros Es (redação original v1.1, preservada).

A maioria dos projetos de IA trata custo como uma restrição de engenharia isolada, resolvida depois que a arquitetura já existe. No ORYX, o custo é tratado como uma **dimensão de governança de primeira classe**, com o mesmo status que auditabilidade ou explicabilidade — mas sempre subordinada à qualidade, nunca substituindo-a.

O framework distingue três conceitos que costumam ser confundidos:

**Eficácia** — o agente chega ao resultado analítico correto? A hipótese estrutural respeita Elliott, o Conviction Vector reflete corretamente a coerência entre narrativas, o TMP gerado é tecnicamente válido. Eficácia é medida contra a Constituição Cognitiva (Nível 1 do GES), não contra o custo.

**Eficiência** — qual o menor custo de tokens, chamadas de API e modelo necessário para produzir esse mesmo resultado? Eficiência nunca é avaliada isoladamente; só faz sentido como razão sobre uma Eficácia já validada.

**Efetividade** — o resultado, entregue com essa eficácia e a esse custo, gera valor operacional real? Um TMP tecnicamente perfeito e barato, mas que chega tarde demais para o Bot Trade Finance, ou que dispara Convicção alta sistematicamente em cenários que depois se invalidam, não é efetivo.

Princípio central:

> **Eficiência sem Eficácia é desperdício disfarçado de economia. Eficácia sem Eficiência é qualidade insustentável. Nenhuma das duas, sem Efetividade, produz valor.**

---

## 3. Princípio Fundamental — Hierarquia de Prioridade

Em qualquer conflito entre custo e qualidade, a ordem de prioridade é fixa e não negociável por nenhum agente, Skill ou processo automático:

```
1. Conformidade Constitucional (Nível 1 do GES — Elliott, Fibonacci,
   Fractalidade, SMC, ICT, hierarquia metodológica)
        ↓
2. Eficácia (correção analítica e coerência do Conviction Vector)
        ↓
3. Efetividade (valor operacional do resultado entregue)
        ↓
4. Eficiência (custo mínimo para sustentar os três níveis acima)
```

Nenhuma otimização de custo pode subir esse degrau. Um Scheduler que suprime a execução do Structural Agent para economizar tokens, mas perde uma mudança estrutural real, viola o princípio — porque sacrificou Eficácia por Eficiência, na ordem inversa da hierarquia.

---

## 4. Onde a Economia Já Está Embutida na Arquitetura

Antes de propor mecanismos novos, é preciso reconhecer que o ORYX já foi desenhado com eficiência estrutural embutida — isso deve ser preservado e formalizado, não reinventado:

| Mecanismo já definido | Documento de origem | Efeito econômico |
|---|---|---|
| Scheduler Inteligente (execução orientada a evento, não polling) | ENGENHARIA GERAL, Doc. 03 §16 / Mission Engine §9 | Elimina chamadas de API em candles sem mudança relevante | <!-- DIV-CEE-01 (2026-10-01): "Mission Engine" = termo legado; absorvido pelo Manager Agent — Fase 0 (Mission Lifecycle) / Fase 1 (Dispatch, scheduler) — ADR-MANAGER-001 / DHR-ARQ-002. Texto preservado (INV-07/CONST-01). -->
| Blackboard Cognitivo (comunicação indireta, nunca agente-a-agente) | ENGENHARIA GERAL §9 | Evita N×N chamadas redundantes entre agentes |
| Persistência Cognitiva (agentes mantêm modelo mental, não recomeçam a cada candle) | ENGENHARIA GERAL, Princípio 17 | Reduz reprocessamento de contexto completo |
| Especialização Máxima (Skill nunca cresce indefinidamente) | ENGENHARIA GERAL §26 | Mantém prompts pequenos e focados por Skill |
| Missões com prioridade dinâmica | ENGENHARIA GERAL, Mission Engine §8 | Evita gastar recursos em hipóteses de baixa relevância | <!-- DIV-CEE-02 (2026-10-01): "Mission Engine" = termo legado; absorvido pelo Manager Agent — Fase 0 (Mission Lifecycle) — ADR-MANAGER-001 / DHR-ARQ-002. Texto preservado (INV-07/CONST-01). -->

O CEE-001 não substitui esses mecanismos — ele os torna **mensuráveis e auditáveis**, e adiciona a camada que faltava: **roteamento de modelo por complexidade cognitiva**.

---

## 5. Roteamento por Complexidade Cognitiva

Nem toda unidade de trabalho do ORYX exige o mesmo grau de julgamento. A taxonomia vertical já aprovada (Tipos I–V) é o critério natural de roteamento — reutilizá-la para custo evita criar uma segunda classificação paralela.

| Tipo cognitivo (taxonomia vertical) | Natureza do trabalho | Classe de modelo recomendada | Exemplos |
|---|---|---|---|
| Execução de regra determinística | Aplica algoritmo conhecido sem ambiguidade | Modelo econômico (tier Haiku) | Trend Skill, Canal Skill, extração de eventos BOS/FVG, formatação de Evidência no formato EC-COG |
| Síntese e julgamento especializado | Pondera interpretações concorrentes dentro de um domínio | Modelo intermediário (tier Sonnet) | Structural Agent, Institutional Agent, Execution Agent, Narrativa Institucional |
| Convergência multi-narrativa e arbitragem de conflito | Resolve conflito entre narrativas independentes, decide sobre a Constituição | Modelo de fronteira (tier Opus), uso reservado | Conviction Engine em estado de conflito alto, Meta-Cognitive Supervisor, Master Orchestrator em decisão de missão crítica | <!-- DIV-CEE-03 (2026-10-01): "Conviction Engine" = mecanismo legado (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (DHR-ARQ-001); "Master Orchestrator" = absorvido pelo Manager Agent (ADR-MANAGER-001). Não são componentes/agentes independentes. Texto preservado (INV-07/CONST-01). -->
| Metacognição e auditoria de qualidade | Avalia a qualidade do próprio raciocínio do sistema | Modelo de fronteira, uso esporádico e batelado | Meta-Cognitive Supervisor, Governance Agent em homologação |

**Regra de roteamento:** um componente só pode ser promovido a uma classe de modelo superior mediante evidência registrada de que a classe inferior produz erro de julgamento mensurável (não por precaução genérica). Essa evidência entra no Knowledge Graph como métrica de calibração do próprio componente — o sistema aprende, com o tempo, qual classe de modelo cada Skill realmente precisa.

Isso está alinhado com a Ideia 141 (Inteligência Distribuída) já registrada na auditoria: "cada componente sabe pouco, o conjunto sabe muito" — o corolário econômico é que cada componente também deve *custar* pouco, e é o conjunto que produz valor caro.

---

## 6. Cache de Contexto Cognitivo — Contrato Formal (DCEBS)

O Blackboard e o Market Digital Twin são, por definição, estado compartilhado e persistente. Isso os torna candidatos naturais a cache de prompt — mas isso só funciona se o contrato de dados for desenhado para isso desde a origem. Esta seção fecha a pendência de alinhamento com o DCEBS (Documento 13), formalizando o objeto de dados que deve ser incorporado ao schema oficial do Event Bus.

### 6.1 Novo objeto de contrato: `InferenceContextEnvelope`

Todo payload enviado a um modelo, por qualquer Agente ou Skill, deve ser estruturado como um envelope com duas partições nomeadas — não como um bloco de texto único:

<!-- DIV-CEE-04 (2026-10-01; ajustada por DHR-DEC-001, 2026-10-01): no diagrama abaixo, "Mission Engine" (campo mission_id) = termo legado; absorvido pelo Manager Agent — Fase 0 (Mission Lifecycle) — ADR-MANAGER-001 / DHR-ARQ-002. Comentário movido para FORA do bloco de código (antes era inline no diagrama, onde não renderiza como comentário). Texto normativo preservado (INV-07/CONST-01). -->
```
InferenceContextEnvelope
├── stable_prefix
│   ├── mission_id            (referência à Missão ativa — Mission Engine)
│   ├── blackboard_snapshot_ref  (referência versionada, não o conteúdo bruto)
│   ├── market_digital_twin_ref  (referência versionada)
│   ├── contract_version       (versão do CEM/CCM/CDM/CNM em uso)
│   └── prefix_hash            (hash do conteúdo — chave de invalidação de cache)
├── variable_payload
│   ├── event_type             (ex: candle_close, structural_break, evidence_new)
│   ├── event_data              (conteúdo específico do evento)
│   └── requested_output_schema (contrato de saída esperado, ex: EC-COG-002 Hypothesis)
└── cache_control
    ├── ttl                     (tempo de vida do prefixo cacheado)
    └── invalidation_trigger    (lista de eventos que forçam recomputo do prefixo)
```

### 6.2 Regras de contrato

1. `stable_prefix` deve ser posicionado no início do contexto enviado ao modelo e reaproveitado entre chamadas consecutivas do mesmo ciclo de missão.
2. `prefix_hash` muda se e somente se um campo do Blackboard relevante para aquele Agente for alterado — atualizações no Blackboard não relacionadas ao domínio do Agente (ex: uma atualização do Execution Agent não deve invalidar o cache do Structural Agent) **não** alteram o hash.
3. O Blackboard nunca é reescrito integralmente a cada evento menor — apenas os campos afetados são atualizados, preservando o `prefix_hash` sempre que possível.
4. `invalidation_trigger` é obrigatório e explícito por tipo de Agente — cada Agente declara, na sua Skill Development Specification, quais eventos do Blackboard invalidam seu próprio cache.

Esse requisito não é opcional: sem ele, a arquitetura de Blackboard — que é uma virtude cognitiva — se torna um ônus econômico, porque cada agente reenviaria o estado inteiro do mercado a cada chamada.

**Ação de integração:** esta subseção (6.1–6.2) deve ser incorporada literalmente ao DCEBS (Documento 13) como parte do schema oficial de objetos trocados no Event Bus, na próxima revisão desse documento.

---

## 7. Métricas de Governança Econômica — Limiares Numéricos (Fase Piloto)

Esta seção fecha a pendência de calibração numérica. Como ainda não existe telemetria real de operação, os limiares abaixo são **provisórios de Fase Piloto** — adotados desde o primeiro dia de operação para permitir auditoria, mas com recalibração obrigatória agendada (§7.3).

### 7.1 Definições e limiares iniciais

| Métrica | Definição | Limiar provisório (Fase Piloto) | Ação ao ultrapassar |
|---|---|---|---|
| Custo por Missão | Soma de tokens (input+output, ponderados por preço do modelo) até o fechamento da missão | > 2× a mediana móvel das últimas 30 missões do mesmo tipo (mesmo Agente/Skill/ativo) | Alerta ao Learning & Governance Agent |
| Custo Anormal Confirmado | Repetição do alerta acima | 3 ocorrências consecutivas no mesmo componente | Escalação ao Meta-Cognitive Supervisor para investigação |
| Custo por TMP emitido | Custo total do ciclo ÷ número de Trading Mission Packages efetivamente gerados | > 1,5× a média móvel de 30 dias | Revisão de eficiência do funil completo (não apenas do componente isolado) |
| Razão Convicção/Custo | Convicção Global final ÷ custo da missão | Queda > 25% em relação à média móvel de 30 missões | Alerta — possível gasto sem ganho de certeza |
| Deriva de Custo sem Ganho de Qualidade | Custo médio por missão sobe, enquanto Convicção Global média e Estabilidade (Structural Timeline) não acompanham | Custo médio sobe > 15% em janela de 30 missões **enquanto** Convicção Global média varia menos de ±3 pontos percentuais | Escalação obrigatória ao Meta-Cognitive Supervisor |
| Taxa de Chamadas Redundantes | Chamadas cujo resultado não alterou o Blackboard | > 10% das chamadas de um componente em janela de 7 dias | Auditoria do Scheduler Inteligente daquele componente |

### 7.2 Método de cálculo

Todos os limiares usam **janela móvel**, não valores fixos globais, porque o custo esperado varia por ativo (BTC, XAU, NASDAQ), por tipo de missão e por regime de mercado (missões em regime de alta volatilidade legitimamente geram mais eventos e mais chamadas). Um limiar fixo trataria isso como anomalia incorretamente. A mediana/média móvel de 30 missões do **mesmo tipo** é o denominador — nunca uma média global do sistema.

### 7.3 Recalibração obrigatória

Estes limiares são explicitamente marcados como **provisórios** e devem ser recalibrados:

- Após as primeiras **200 missões reais** acumuladas em operação piloto (não em sandbox/backtest), ou
- Após **60 dias corridos** de operação piloto, o que ocorrer primeiro.

A recalibração é conduzida pelo Learning & Governance Agent, usando a distribuição real observada (não mais um valor arbitrário), e passa pelo mesmo pipeline de homologação definido no §9. Até a recalibração, os limiares desta seção são a referência oficial e vinculante.

---

## 8. Certificação Econômica — Extensão do Pipeline GES

O GES (Documento 12) já define cinco validações obrigatórias para qualquer Skill: Técnica, Teórica, Estatística, Operacional e Cognitiva. Este documento adiciona uma sexta, sem alterar a ordem nem a prioridade das anteriores:

```
Validação Técnica → Validação Teórica → Validação Estatística →
Validação Operacional → Validação Cognitiva → Validação Econômica
```

**Validação Econômica** responde: dado que a Skill já passou por todas as validações anteriores (ou seja, já é eficaz e efetiva), ela está usando a classe de modelo e o volume de chamadas mínimos necessários para se manter assim?

Uma Skill nunca pode pular direto para a Validação Econômica, nem a Validação Econômica pode reverter uma aprovação já concedida pelas cinco anteriores — ela só pode recomendar uma mudança de classe de modelo ou de frequência de wake-up, sujeita a novo teste completo se a mudança for material.

---

## 9. Autoridade de Homologação de Roteamento

Esta seção fecha a pendência de definição de autoridade dentro da estrutura de três papéis (Estrategista / Analista / Controlador), sem criar um quarto papel ou uma exceção ao fluxo já estabelecido.

### 9.1 Regra de equivalência

Mudança de roteamento de modelo (promover ou rebaixar a classe de modelo de um Agente/Skill) é tratada com a **mesma autoridade de aprovação já usada para mudanças de Framework Oficial — Nível 2 da Constituição do SOT (GES §3)**. Não se cria uma nova instância de governança: reutiliza-se a existente, porque roteamento de modelo é, por definição, uma mudança de Framework Oficial (afeta como uma Skill/Agente opera, não a Constituição em si).

### 9.2 Fluxo de aprovação

```
1. ESTRATEGISTA formula a proposta de mudança de roteamento,
   com a evidência de calibração exigida no §5 (erro de julgamento
   mensurável na classe atual)
        ↓
2. ANALISTA audita a proposta contra o CEE-001 e demais documentos
   congelados (conformidade arquitetural, não decide sozinho)
        ↓
3. Consenso explícito de Andraus (mesma autoridade humana que
   homologa qualquer mudança de Nível 2 — Framework Oficial)
        ↓
4. CONTROLADOR registra a decisão, versiona o roteamento no
   Capability Graph e arquiva a evidência que a motivou
```

### 9.3 O que este fluxo NÃO permite

- Nenhum papel decide sozinho — nem Estrategista, nem Analista, nem Controlador, isoladamente, aprovam uma mudança de roteamento.
- Nenhuma mudança de roteamento entra em produção sem passar pelo pipeline Sandbox → Backtest → Forward Test → Homologação (GES), mesmo já tendo consenso de Andraus — consenso autoriza o teste, não substitui o teste.
- Mudanças emergenciais de custo (ex: pico de gasto inesperado) podem pausar um componente via Scheduler (kill-switch operacional), mas **não podem alterar permanentemente sua classe de modelo** sem passar por este fluxo completo.

---

## 10. Salvaguardas Constitucionais

1. **Nenhum agente pode reduzir sua própria classe de modelo autonomamente.** Mudança de roteamento segue o fluxo do §9, nunca uma otimização silenciosa do próprio componente.
2. **O Scheduler nunca pode suprimir a execução de um agente por motivo de custo quando houver evento estruturalmente relevante.** Economia de tokens é subproduto de bom design de eventos, não de supressão de análise.
3. **Cache nunca pode servir contexto desatualizado como se fosse atual.** Qualquer mudança de regime, estrutura ou convicção invalida o cache correspondente imediatamente (ver `invalidation_trigger`, §6.2).
4. **Métricas de custo nunca entram no Conviction Vector.** O quanto uma hipótese custou para ser formada é irrelevante para o quanto ela é confiável — misturar as duas coisas corromperia a Ideia 057 (Conviction não é Score).
5. **Toda alteração de roteamento de modelo é reversível e versionada**, seguindo o pipeline do §9.2.

---

## 11. Papel no Ciclo de Vida

```
Nova Skill/Agente projetado
        ↓
Validações 1–5 do GES (Eficácia)
        ↓
Roteamento inicial por Tipo Cognitivo (§5)
        ↓
Operação monitorada — métricas de custo com limiares de Fase Piloto (§7)
        ↓
Validação Econômica periódica (§8)
        ↓
Proposta de ajuste de classe de modelo, se justificado por evidência
        ↓
Fluxo de Autoridade de Homologação (§9) — Estrategista → Analista →
Consenso Andraus → Controlador
        ↓
Novo ciclo de homologação técnica (Sandbox → Backtest → Forward Test)
```

---

## 12. Critérios de Aceitação

O CEE-001 será considerado implementado quando:

1. Todo Agente, Skill e Engine do ORYX possuir uma classe de modelo declarada explicitamente (Haiku/Sonnet/Opus ou equivalente), rastreável no Capability Graph (Doc. 03 §25).
2. O Learning & Governance Agent registrar, para cada missão encerrada, as seis métricas definidas no §7.1, calculadas pelo método de janela móvel do §7.2.
3. Nenhuma mudança de roteamento de modelo tiver ocorrido fora do fluxo do §9.2.
4. O Meta-Cognitive Supervisor tiver acesso às métricas de custo como insumo formal de sua auditoria de qualidade de raciocínio — não como fonte informal.
5. O objeto `InferenceContextEnvelope` (§6.1) estiver incorporado ao schema oficial do DCEBS (Doc. 13).
6. A recalibração de limiares (§7.3) estiver agendada e rastreável — não apenas prevista em texto.
7. Nenhuma das cinco Salvaguardas Constitucionais (§10) tiver sido violada em auditoria de consenso.

Este documento não é considerado "implementado" apenas por existir — a implementação se mede pela presença desses sete critérios no sistema em operação, não na especificação em si.

---

## 13. Registro para o CONTROLADOR

Entrada de backlog sugerida, no formato usado pelo repositório de arquitetura aprovada por consenso:

| Campo | Valor |
|---|---|
| ID do Documento | CEE-001 |
| Nome | Cognitive Economy & Efficiency Specification |
| Tipo | Documento de Governança (Layer 1) — transversal |
| Versão proposta para consenso | 1.1 |
| Dependências | GES (Doc. 12), DCEBS (Doc. 13), GMC-001, Taxonomia de Agentes (Tipos I–V) |
| Impacto em documentos existentes | DCEBS (Doc. 13) — requer incorporação do `InferenceContextEnvelope` (§6.1); GES (Doc. 12) — requer incorporação da Validação Econômica (§8) |
| Status | Fechado para consenso — pronto para deliberação de Andraus |
| Prioridade sugerida | P1 — não bloqueia Skills já em auditoria (SAS-001 Cap.2), mas deve ser consensuado antes da primeira Skill entrar em operação piloto real, já que define os limiares que passam a valer desde o primeiro dia |
| Ação seguinte | Aguardar declaração de consenso; após consenso, abrir tarefas derivadas para revisão do DCEBS e do GES incorporando as seções §6 e §8 |

---

## 14. Histórico de Versões

| Versão | Status | Mudança |
|---|---|---|
| 1.0 | Candidata | Primeira consolidação — framework 3E, roteamento por tipo cognitivo, métricas qualitativas, quatro pendências abertas |
| 1.1 | Fechada para Consenso | Resolução das quatro pendências: limiares numéricos de Fase Piloto (§7), contrato formal `InferenceContextEnvelope` para o DCEBS (§6), fluxo de Autoridade de Homologação de Roteamento (§9), registro de backlog formatado para o CONTROLADOR (§13) |

---

*Fim do Documento CEE-001 v1.1 (Fechada para Consenso)*

---

# EMENDA v2.0 — Andraus, 2026-09-14 (Respostas ao Questionário de Resolução v1)

> Esta emenda promove o CEE-001 de v1.1 para **v2.0**. Ela ADICIONA duas seções e NÃO altera o §10 original (Salvaguardas de Economia/Roteamento), que permanece íntegro. Homologada por Andraus (Q-003, Q-009).
> **Nota de numeração:** as Salvaguardas de Sinal são rotuladas **§11 (Salvaguardas de Sinal)** — sempre citadas com o qualificador entre parênteses para não colidir com a seção "11. Papel no Ciclo de Vida" da v1.1. O Framework 4Es é **§12**.

## §11 — Salvaguardas de Sinal de Trading (Q-003)

Conjunto constitucional distinto das Salvaguardas de Economia/Roteamento (§10). Antes atribuído por engano ao "§10"; agora formalizado com identidade própria. Referenciado por `RULES.md` RULE-CEE-004.

As **5 Salvaguardas de Sinal** são invioláveis:
1. Hipótese sem nível de invalidação explícito → **bloqueada**.
2. Score total < 7/9 → sinal operacional **bloqueado**. *(Limiar de Fase Piloto — recalibrável após backtest, Q-002.)*
3. `directional_conflict = true` → output **NEUTRO** obrigatório.
4. Convicção global < 70% → **sem sinal** COMPRA/VENDA. *(Limiar de Fase Piloto — recalibrável, Q-002.)*
5. R:R calculado < 1:3 (risco:retorno; = 3:1 retorno:risco) → **sem execução**. *(Regra única — Q-004.)*

> **Distinção crítica (evita a misatribuição histórica):** a Salvaguarda 4 do **§10** (Economia) — "métricas de custo nunca entram no Conviction Vector" = **INV-04** — é DIFERENTE da Salvaguarda 4 deste §11 (convicção < 70%). Ambas invioláveis; fontes distintas.

## §12 — Framework 4Es (Q-009)

O antigo "Framework 3E" (§2-3) é estendido para **4Es** com a adição de **Economicidade** como 4º nível.

**Hierarquia inviolável:** `Conformidade Constitucional > Eficácia > Efetividade > Eficiência > Economicidade`.

- **Eficiência** (intra-execução): quão bem os recursos usados foram convertidos em resultado (tokens/chamadas/tempo por execução).
- **Economicidade** (inter-execução / estrutural): menor custo unitário de provisionamento — classe de modelo por complexidade, cache de contexto, roteamento, batching, reuso de KV-cache.

Nenhuma otimização de custo (Eficiência ou Economicidade) sobe acima de Eficácia. Economicidade que compromete Eficiência (ex.: modelo mais barato que exige 3 reexecuções) é falsa economia. Fonte metodológica: GEH-001 §3.

## Histórico de Versões (emenda)

| Versão | Status | Mudança |
|---|---|---|
| 2.0 | Homologada (Andraus 2026-09-14) | +§11 (Salvaguardas de Sinal, Q-003); +§12 (Framework 4Es, Q-009). §10 e demais seções da v1.1 inalterados. |
