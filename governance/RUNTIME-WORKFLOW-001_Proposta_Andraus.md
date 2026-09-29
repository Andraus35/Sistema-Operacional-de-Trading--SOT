# RUNTIME-WORKFLOW-001 — Proposta de Workflow de Runtime do SOT (insumo de Andraus)

| Campo | Valor |
|---|---|
| Código | **RUNTIME-WORKFLOW-001** |
| Versão | **v4 (2026-09-29)** — registro aditivo das decisões de Andraus sobre os identificadores propostos: **RISK-LEV-001** (adiada à Spec do agente de risco — decisão de *timing*) e **RUNTIME-TF-PAIR-001** (resolvida: conjunto inicial **extensível**). Ver §1-quater. Schemas mission-dispatch/conviction-report atualizados só na documentação (`description`/`$comment`) para refletir a extensibilidade. **v1/v2/v3 preservadas integralmente (INV-07 — nada deletado).** ▪ **v3 (2026-09-29)** — complemento de Andraus: tabela fixa de pareamento de timeframes contexto↔entrada (3 pares) + restrição nos schemas. Ver §1 (v1 verbatim), §1-bis (v2 verbatim), §1-ter (v3 verbatim — tabela de pareamento), §1-quater (v4 — decisões de Andraus), §2-bis (decomposição), §6 (schemas). |
| Natureza | **Documento de insumo** (não-normativo) — registro verbatim de uma proposta de **fluxo de acionamento e formação de convicção entre os agentes cognitivos** ("workflow de runtime" no sentido de **orquestração cognitiva do Harness**, não de software — ver §0-bis), trazida por Andraus em chat, com decomposição preliminar mapeada contra o baseline. **NÃO é Spec, NÃO é emenda, NÃO fecha decisão aberta.** |
| Status epistemológico | **INSUMO — `[FONTE]` (registro de diretiva) + `[INFERÊNCIA]` (decomposição/mapeamento) + `[DECISÃO NECESSÁRIA]` (o que depende de Andraus).** Não é baseline. Não é FATO NORMATIVO nem FATO ARQUITETURAL. |
| Origem | Andraus (dono do projeto), chat, 2026-09-29 — mesma diretiva que originou a EUA-E23. |
| Vínculo normativo | **EFETIVO (2026-09-29) — `[FATO NORMATIVO — obrigação de leitura]`.** Com a **homologação da EUA-E23 / RULE-ECC-06** (DHR-EUA-E23, Andraus, 2026-09-29), este documento **é agora leitura obrigatória** do Dossiê de Pesquisa de qualquer Spec futura (SPEC-002 em diante) que abra ou toque **K-001 / SPEC-018 / SPEC-045-RUNTIME-001** ou que seja **Spec de agente operacional, manager/contexto/orquestrador (SPEC-014/023/024) ou de risco (RISK-SPEC-*)**. A obrigação vincula a **leitura/consideração** deste insumo (decisão por etapa E1–E7/E8 no Dossiê), **NÃO** o conteúdo da Spec: o documento permanece **não-normativo** e **não fecha nenhuma decisão aberta** (CONS-01). *[texto anterior preservado — INV-07: era `[PROPOSTA]`, "após homologação da EUA-E23 passará a ser leitura obrigatória"; a condição foi satisfeita.]* |
| Autoria do registro | Especificador (Claude Code), 2026-09-29 |
| Fundamento no baseline | INV-07 (nada deletado; registro aditivo) · CONS-01 (não fecha decisão aberta) · RULE-MET-01 (não-fabricação; o que Andraus não disse não é inferido como fato) · AGENTS.md §9 (SOT não executa ordem; produz Signal Package; TMP interno) · RULE-ECC-02 (Dossiê de Pesquisa) |

---

## 0-bis. Esclarecimento terminológico — "runtime" aqui = orquestração cognitiva, não software (Andraus, 2026-09-29) `[FONTE]`

**"Runtime" neste documento NÃO significa runtime de software/código.** O SOT está em fase **spec-first** (BUILD/VERIFY-de-código adiados — AGENTS.md §1); não há implementação de código a especificar aqui. Quando Andraus fala em "workflow do Trading em runtime", refere-se ao **funcionamento operacional do Harness Cognitivo**: a **sequência de acionamento e a troca de evidência/hipótese/convicção entre os agentes LLM especificados pelas Specs**, quando o SOT estiver "rodando" em uma sessão de trading ao vivo. Portanto este workflow é insumo para a **especificação da orquestração cognitiva dos agentes** — não para arquitetura de software, infraestrutura ou execução técnica.

Consequências de leitura:
- As decisões abertas correlatas — **K-001** (ciclo de evolução do conhecimento), **SPEC-018** (Learning & Knowledge Formation Governance) e **SPEC-045-RUNTIME-001** (caminho de leitura/operação em runtime do harness) — tratam "runtime" como o **caminho de operação do harness já especificado**, não como implementação de código.
- **Achado registrado (não forçar equivalência):** se, na abertura da SPEC-045, a decisão **SPEC-045-RUNTIME-001** vier a ser interpretada como algo mais próximo de runtime técnico/software (carga física de prefixo/guardrails/Skills/memória — ROADMAP §20), essa distinção deve ser **explicitada como achado** na abertura; este insumo **não** afirma equivalência entre "orquestração cognitiva" (sentido de Andraus aqui) e "runtime técnico" (possível leitura da §20). Os dois sentidos coexistem até que a SPEC-045 os separe. `[DECISÃO NECESSÁRIA]` — Andraus/abertura da SPEC-045.

## 0. Aviso de status (CONS-01 / RULE-MET-01) `[FATO]`

Este documento **registra uma proposta de Andraus como insumo** — não a homologa nem a converte em requisito. Nenhuma decisão aberta é fechada aqui (**K-001, SPEC-018, SPEC-045-RUNTIME-001, RISK-CONV-001, RISK-ARR-LOC-001, J-001, G-001, H-001, M-001, N-001, C-001** permanecem abertas). A decomposição da §2 é **`[INFERÊNCIA]` do Especificador** para orientar pesquisa futura; onde o texto de Andraus não sustenta um detalhe, ele é marcado `[DECISÃO NECESSÁRIA]` e **não** preenchido por invenção. Em qualquer conflito entre este insumo e um invariante constitucional (AGENTS.md §6/§9), **o invariante prevalece** e o conflito vira achado a tratar na abertura da Spec correspondente.

## 1. Workflow verbatim (Andraus, 2026-09-29) `[FONTE]`

> "Está é minha proposta de workflow do Trading em runtime com o SOT:
>
> Antes da abertura da Killzone coloco o sistema para rodar. Aponto o Time frame e o tipo de Trading que quero realizar: position, swing ou day Trading. Agente estrutural começará a verificar a estrutura de ondas e após observar, marcar, tratar evidencia, hipótese e formar convicção entrega sua análise e convicção. Se houver oportunidade apontada pelo agente anterior, dispara o agente institucional que fará o mesmo. Após sua análise e entrega, o manager agente formará a convicção macro de contexto e se houver oportunidade conclusiva deverá adicionar um alarme-gatilho no nível de preço a ser ativado ou não após abertura da Killzone. Se ativado agente operacional entra com sua análise do time frame da entrada (difere do de contexto) fazendo o devido tratamento e entrega ao manager. Após colher os dados do operacional o manager formará convicção global e decidirá envio com dados de risco-retorno ao agente de risco que por sua vez fará sua análise e decidirá se envia sinal ou não ao bot finance externo com dados da entrada."

*(Transcrição literal — RCN-001/PC-06. Grafia original preservada, incluindo "Está"/"evidencia".)*

## 1-bis. Workflow verbatim — ATUALIZAÇÃO v2 (Andraus, 2026-09-29) `[FONTE]`

> "Antes da abertura da Killzone coloco o sistema para rodar. Aponto o ativo alvo, o tipo da missão: se de exploração ou de validação, o tipo de Trading: position, swing ou day Trading (Implicação na alavancagem a depender do nível da convicção e tipo da oportunidade) e o time frame de analise O manager agente começara a distribuição da missão com o Agente estrutural que irá verificar a estrutura de ondas no time frame de contexto e no de entrada e após observar, marcar, classificar tratar evidencia, hipótese e formar convicção entrega sua convicção. Se houver oportunidade apontada (a depender da convicção especializada), o agente institucional entra em cena e fará o mesmo procedimento no time frame de contexto apenas. Após sua análise e entrega, o manager agente formará a convicção macro de contexto e se houver oportunidade conclusiva deverá adicionar um alarme-gatilho no nível de preço a ser ativado ou não após abertura da Killzone ou mesmo em outro momento. Se ativado e válido, o agente operacional entra com sua análise do time frame da entrada (difere do de contexto) fazendo o devido tratamento e entrega ao manager. Após colher os dados do operacional o manager formará convicção global e decidirá envio com dados da oportunidade ao agente de risco que por sua vez fará sua análise de risco-retorno e decidirá por convicção se envia sinal ou não ao bot finance externo com dados da entrada."

*(Transcrição literal — RCN-001/PC-06. Grafia original preservada.)*

### Diferenças notáveis v1 → v2 (registro de fato, não resolução) `[FONTE]`/`[DECISÃO NECESSÁRIA]`

| # | Mudança da v2 frente à v1 | Natureza |
|---|---|---|
| Δ1 | Novos parâmetros de missão explícitos: **ativo alvo** e **tipo de missão (exploração vs validação)** | `[FONTE]` — acréscimo de input |
| Δ2 | **Alavancagem** deixa de ser input e passa a ser **implicação** do nível de convicção + tipo de oportunidade | `[DECISÃO NECESSÁRIA]` — fórmula/derivação não dita (ver §3, tensão 8) |
| Δ3 | O **Manager distribui ativamente a missão** ao agente estrutural (na v1 o acionamento do estrutural era implícito) | `[FONTE]` — novo ator/etapa |
| Δ4 | O **agente estrutural analisa dois timeframes** (contexto E entrada), não só um | `[FONTE]` |
| Δ5 | Menção explícita a **classificar** evidência (v1: só "tratar evidência, hipótese") | `[FONTE]` |
| Δ6 | O **agente institucional atua apenas no timeframe de contexto** (explicitado) | `[FONTE]` |
| Δ7 | Alarme-gatilho ativável "após a Killzone **ou mesmo em outro momento**" (v1: só após a Killzone) | `[FONTE]` |
| Δ8 | Alarme ativado exige **"ativado E válido"** antes de acionar o operacional (v2 acrescenta "e válido") | `[FONTE]` |
| Δ9 | Manager envia ao Risk Agent **"dados da oportunidade"** (v1: "dados de risco-retorno") — o risco-retorno passa a ser **análise do próprio Risk Agent** | `[FONTE]` — realoca a análise risco-retorno |
| Δ10 | Risk Agent decide **"por convicção"** se envia sinal (reforça convicção de risco — tensão RISK-CONV-001) | `[DECISÃO NECESSÁRIA]` |

## 1-ter. Complemento v3 — Tabela de pareamento de timeframes contexto↔entrada (Andraus, 2026-09-29) `[FONTE]`

> "Segue tabela de timeframes de Contexto para análise estrutural e institucional, e de entrada para análise de confluência multitimeframe e do operacional
>
> Macro
> D1
> H4
> H1
>
> Micro
> H1
> M15
> M5
>
> Análise macro em D1 entrada em H1
> Análise macro em H4 entrada em M15
> Análise macro em H1 entrada em M5"

*(Transcrição literal — RCN-001/PC-06. Grafia original preservada.)*

### Leitura do dado — 3 pares fixos, não produto cartesiano `[FONTE]`/`[INFERÊNCIA]`

O texto de Andraus é preciso: cada par de contexto→entrada é citado **uma vez**, com "Análise macro em X entrada em Y". Portanto são **exatamente 3 pares fixos** — **não** um produto cartesiano livre entre {D1,H4,H1} e {H1,M15,M5} (que geraria 9 combinações). Registro como fato observado; não há ambiguidade a resolver (RULE-MET-01 — não fabricar combinações não ditas).

| # | Papel Macro (contexto) | Papel Micro (entrada) | Usado por |
|---|---|---|---|
| Par 1 | **D1** | **H1** | Contexto: estrutural (E3) + institucional (E4). Entrada: estrutural (E3) + operacional (E6). |
| Par 2 | **H4** | **M15** | idem |
| Par 3 | **H1** | **M5** | idem |

**Nota sobre o H1 (registro de fato, não contradição) `[FONTE]`:** o H1 aparece em **dois papéis distintos** — como TF de **contexto** no Par 3 (entrada M5) e como TF de **entrada** no Par 1 (contexto D1). São usos distintos do mesmo TF em pares diferentes, **não** uma contradição nem uma quarta combinação. Não colapsar em erro nem inferir par adicional.

### Onde a restrição se aplica na decomposição E1–E8 (mapeamento) `[INFERÊNCIA]`

- **E1 (mission dispatch):** o parâmetro "timeframe de análise" que o operador aponta deixa, na prática, de ser **dois campos livres** (contexto + entrada independentes) e passa a ser a **escolha de UM dos 3 pares**. Nos schemas, `mission_parameters.context_timeframe` + `mission_parameters.entry_timeframe` ficam acoplados por um `oneOf` de 3 pares (ver §6).
- **E3 (agente estrutural — contexto E entrada):** opera dentro do TF de contexto **e** do TF de entrada **do par escolhido** (ex.: par D1→H1 ⇒ analisa D1 e H1).
- **E4 (agente institucional — só contexto):** opera no TF de **contexto** do par escolhido.
- **E6 (agente operacional — só entrada):** opera no TF de **entrada** do par escolhido.

### Achado — M15 ausente dos schemas de 1a geração `[FONTE]`/`[DECISÃO NECESSÁRIA]`

A tabela de Andraus usa **D1/H4/H1/M15/M5**, incluindo **M15**. Os schemas de 1a geração (`elliott-wave.*`, `smc.*`, `ict.*`, `synthesis.*`) usam o conjunto **S1/D1/H4/H1/M5** — **sem M15** (e com S1, que a tabela de Andraus não cita). Isto é uma **lacuna registrada**, não resolvida aqui:

- Os schemas `runtime-workflow.*` (desta proposta) tiveram **M15 adicionado** aos enums de timeframe, com nota de origem.
- Os schemas de 1a geração **NÃO foram tocados** (fora do escopo desta proposta; possuem histórico próprio — RULE-MET-01 / INV-07). Propagar M15 a eles, ou reconciliar o conjunto de TFs (S1 vs M15) entre 1a geração e runtime-workflow, é **`[DECISÃO NECESSÁRIA]`** para a abertura da Spec correspondente (SPEC-010/011/012/013/014). Não inventar M15 nos schemas antigos.

### `[DECISÃO NECESSÁRIA]` nova introduzida pela tabela — exaustividade dos pares

O texto de Andraus lista 3 pares, mas **não declara** se esses 3 pares são **exaustivos e fixos** (lista fechada e definitiva) ou se são os pares **iniciais** de uma lista que pode crescer (ex.: acrescentar W1→H4 ou D1→M15 no futuro). Isto **não está claro** no texto e **não deve ser inventado** (RULE-MET-01 / CONS-01). **Proponho o identificador `RUNTIME-TF-PAIR-001`** (só proposta de identificador — só Andraus cunha/abre) para rastrear: *"a tabela de pareamento contexto↔entrada é uma lista fechada e definitiva de 3 pares, ou um conjunto inicial extensível?"*. Impacto se for lista aberta: o `oneOf` de 3 pares nos schemas precisará virar extensível/versionado. **`[DECISÃO NECESSÁRIA]` — Andraus.** Enquanto isso, os schemas codificam **os 3 pares literais** que Andraus deu (fail-closed: só aceita o que foi dito). **▸ RESOLVIDA em §1-quater (Andraus, 2026-09-29): "EXTENSÍVEL" — conjunto inicial extensível; ver §1-quater para o que permanece em aberto (processo de extensão).**

## 1-quater. Decisões de Andraus sobre os identificadores propostos (chat, 2026-09-29) `[FONTE]`/`[FATO NORMATIVO]`

Os dois identificadores de decisão aberta propostos por este documento — **RISK-LEV-001** (§2-bis E1 / §3 tensão 8) e **RUNTIME-TF-PAIR-001** (§1-ter) — eram, até aqui, **`[PROPOSTA]` de identificador** (só Andraus cunha/abre decisão). Andraus respondeu às duas em chat (2026-09-29). Registro aditivo (INV-07 — nada reescrito; v1/v2/v3 preservadas), verbatim:

### RISK-LEV-001 — alavancagem por convicção `[FATO NORMATIVO — decisão de timing]`

> **Andraus (2026-09-29):** "ADIAR ATÉ SPEC DO AGENTE DE RISK"

**Leitura (RULE-MET-01 — sem inferir além do dito):** Andraus **CONFIRMA e cunha oficialmente** o identificador `RISK-LEV-001` como decisão aberta do projeto. A resposta é uma **decisão de *timing*, NÃO uma resolução do mérito**: a lacuna "alavancagem derivada do nível de convicção + tipo de oportunidade" fica **aberta e deferida** para quando a **Spec do agente de risco (RISK-SPEC-*, BL-018)** for aberta. **Nada do mérito foi fechado** — não há fórmula de alavancagem, nem derivação convicção→alavancagem, nem regra definida; **não inferir nenhuma** (CONS-01 permanece: `RISK-LEV-001` continua decisão ABERTA quanto ao mérito, apenas com o momento de resolução definido). Mantém os vínculos já registrados: toca **J-001** e **RISK-CONV-001**, ambas abertas; segue o padrão RISK-* (como RISK-CONV-001 / RISK-ARR-LOC-001, de BL-018).

### RUNTIME-TF-PAIR-001 — natureza da tabela de 3 pares `[FATO NORMATIVO — pergunta resolvida]`

> **Andraus (2026-09-29):** "EXTENSÍVEL"

**Leitura (RULE-MET-01):** Andraus **CONFIRMA** o identificador `RUNTIME-TF-PAIR-001` e **resolve a pergunta original** do §1-ter ("a tabela de pareamento contexto↔entrada é lista fechada e definitiva, ou conjunto inicial extensível?"): os 3 pares (D1→H1, H4→M15, H1→M5) **NÃO são lista fechada/definitiva** — são um **conjunto inicial extensível** (novos pares podem ser acrescentados no futuro, ex. um hipotético W1→H4). A pergunta "fechada vs. extensível" **deixa de estar em aberto**.

O que Andraus **NÃO** disse (e portanto **não** se infere — RULE-MET-01 / CONS-01):
- **QUAIS** seriam os pares futuros — fora de escopo; não inventar pares (o §1-ter e os schemas continuam codificando **exatamente os 3 pares literais** hoje dados; "extensível" significa que um 4º par será acrescentado por **atualização futura** de schema/documento, não que qualquer combinação seja aceita hoje).
- **QUANDO/COMO** um novo par seria adicionado — a **governança do processo de extensão** (que ciclo? presumivelmente o mesmo Especificador→Revisor→Andraus que gerou os 3 atuais, mas Andraus **não** o especificou) permanece **`[DECISÃO NECESSÁRIA]`** a endereçar quando/se um novo par for proposto. Registro esse resíduo como **`RUNTIME-TF-PAIR-EXT-001`** (`[PROPOSTA]` de identificador — só Andraus cunha; não é fato resolvido). Não bloqueia nada hoje: os 3 pares atuais bastam.

**Impacto nos schemas:** o `oneOf` de 3 pares em `runtime-workflow.mission-dispatch.json` **permanece estruturalmente correto** para o estado atual (fail-closed: só aceita os 3 pares dados). A extensibilidade é agora um **fato de documentação** (a lista crescerá por versionamento futuro do schema), não uma pergunta em aberto — as `description`/`$comment` foram corrigidas para não contradizer a decisão (ver §6 e os arquivos de schema).

## 2. Decomposição preliminar (mapeamento contra o baseline) `[INFERÊNCIA]`

Etapas e atores citados por Andraus, mapeados contra o ROADMAP/AGENTS.md. **A coluna "Baseline correlato" indica onde a etapa provavelmente se especifica; a coluna "Depende de" indica a decisão aberta ou Spot que a governa.**

| # | Etapa (verbatim → paráfrase) | Ator citado | Baseline correlato (slot indicativo) | Depende de |
|---|---|---|---|---|
| E1 | Operador arma o sistema antes da Killzone; aponta **timeframe** e **tipo de trade** (position/swing/day) | Operador (Andraus) | Parâmetros de sessão — sem slot dedicado; toca SPEC-008 (Scheduler), SPEC-009 (Cognitive State) | K-001 · G-001 |
| E2 | **Agente estrutural** verifica estrutura de ondas; observa, marca, trata evidência, forma hipótese e **convicção**; entrega análise+convicção | Agente estrutural | SPEC-010 (Structural/Elliott) · CHM-001 (hipótese PRIMARY, Q-005) · CEM-001 (evidência) · SPEC-011 (Fibonacci/Fractal) | J-001 (convicção) |
| E3 | Se há oportunidade, **dispara agente institucional**, que faz o mesmo | Agente institucional | SPEC-012 (Institutional/SMC) · sub-hipótese com `parent_id` (Q-005) | — |
| E4 | **Manager** forma **convicção macro de contexto**; se conclusiva, adiciona **alarme-gatilho** em nível de preço, ativável após a Killzone | Manager/contexto | SPEC-014 (Synthesis) e/ou SPEC-023/024 (Orchestrator/Meta-Cognitive Supervisor) · Conviction Engine SEPARADO (B-001 fechada: Fusion→Conviction→Synthesis) | J-001 · M-001 · K-001 |
| E5 | Se ativado, **agente operacional** analisa o **timeframe de entrada** (difere do de contexto); trata e entrega ao manager | Agente operacional | SPEC-013 (Execution/ICT) — **INVARIANTE: ICT NÃO cria hipótese** (AGENTS.md §6.2), só executa/confirma entrada | — |
| E6 | Manager forma **convicção global** e decide envio com **dados de risco-retorno** ao **agente de risco** | Manager + Risk Agent | SPEC-014 (Synthesis→Decisão) · Conviction Vector 8D · Risk Agent (BL-018) | J-001 · RISK-CONV-001 |
| E7 | **Agente de risco** analisa e decide se **envia sinal** ao **bot finance externo** com dados de entrada | Risk Agent | RISK-SPEC-* (BL-018) · **Signal Package** para o Bot Trade Finance (AGENTS.md §9) · TMP = artefato interno Synthesis→Risk (EUA-E19a) | RISK-ARR-LOC-001 · RISK-CONV-001 · SPEC-045-RUNTIME-001 |

## 2-bis. Decomposição v2 (renumerada — reflete a atualização) `[INFERÊNCIA]`

A v2 introduz uma etapa nova de **distribuição de missão pelo Manager** (E2) e um passo de **validade do alarme** (E6); as etapas foram renumeradas E1–E8. Cada linha carrega, em `Schema`, o contrato de dados proposto na §6 (insumo estrutural — não homologado).

| # | Etapa (v2) | Ator | Baseline correlato (slot indicativo) | Depende de | Schema (§6) |
|---|---|---|---|---|---|
| E1 | Operador arma o sistema; aponta **ativo alvo**, **tipo de missão** (exploração/validação), **tipo de trade** (position/swing/day) e **timeframes** (contexto e entrada). Alavancagem = implicação, não input | Operador (Andraus) | Parâmetros de sessão — sem slot dedicado; toca SPEC-008/009 | K-001 · G-001 · **RISK-LEV-001 (proposto)** | `runtime-workflow.mission-dispatch` (`mission_parameters`) |
| E2 | **Manager distribui a missão** ao agente estrutural (novo na v2) | Manager | SPEC-014/023 (orquestração) | K-001 | `runtime-workflow.mission-dispatch` (`manager_dispatch`) |
| E3 | **Agente estrutural** verifica ondas no **timeframe de contexto E de entrada**; observa, marca, **classifica**, trata evidência+hipótese, forma convicção; entrega | Agente estrutural | SPEC-010 · SPEC-011 · CHM-001 · CEM-001 | J-001 | `runtime-workflow.conviction-report` (`agent_role=structural`) |
| E4 | Se há oportunidade (a depender da convicção especializada), **agente institucional** faz o mesmo **apenas no timeframe de contexto** | Agente institucional | SPEC-012 · sub-hipótese `parent_id` (Q-005) | J-001 | `runtime-workflow.conviction-report` (`agent_role=institutional`) |
| E5 | **Manager** forma **convicção macro de contexto**; se conclusiva, adiciona **alarme-gatilho** no nível de preço, ativável após a Killzone **ou em outro momento** | Manager | SPEC-014/023 · Conviction Engine (B-001 fechada) · SPEC-008 (Scheduler) | J-001 · M-001 · K-001 | `runtime-workflow.manager-conviction-envelope` (`macro_context`) + `runtime-workflow.alarm-trigger` |
| E6 | Se o alarme é **ativado E válido**, **agente operacional** analisa o **timeframe de entrada** (difere do de contexto); trata e entrega | Agente operacional | SPEC-013 (ICT) — **INVARIANTE: ICT NÃO cria hipótese** | — | `runtime-workflow.conviction-report` (`agent_role=operational`, `hypothesis_ref=null`) |
| E7 | Manager forma **convicção global** e decide envio ao Risk Agent com **dados da oportunidade** (não risco-retorno pré-calculado) | Manager + Risk Agent | SPEC-014 · TMP (SPEC-016 repurposada) · Risk Agent (BL-018) | J-001 · RISK-CONV-001 | `runtime-workflow.manager-conviction-envelope` (`global` + `dispatch_to_risk`) |
| E8 | **Agente de risco** faz **sua própria análise de risco-retorno** e decide **por convicção** se envia sinal ao **bot finance externo** | Risk Agent | RISK-SPEC-* (BL-018) · Signal Package (D-RISK-SP-001, RISK-SPEC-022) · INV-05 | RISK-ARR-LOC-001 · RISK-CONV-001 · SPEC-045-RUNTIME-001 | `runtime-workflow.risk-decision` |

**Atualização v3 — pareamento de timeframes (ver §1-ter):** os TFs de contexto e de entrada citados em **E1** (mission dispatch), **E3** (estrutural, contexto E entrada), **E4** (institucional, só contexto) e **E6** (operacional, só entrada) deixam de ser livres e passam a ser regidos por **um dos 3 pares fixos** de Andraus (D1→H1, H4→M15, H1→M5). E1 aponta o par (não dois campos livres); E3/E4 operam no contexto do par; E3/E6 operam na entrada do par. Restrição codificada por `oneOf` em `runtime-workflow.mission-dispatch.json` (§6). Exaustividade dos pares = `[DECISÃO NECESSÁRIA]` RUNTIME-TF-PAIR-001 (§1-ter).

## 3. Pontos de atenção / tensões com o baseline (a tratar na abertura, não aqui) `[INFERÊNCIA]`/`[DECISÃO NECESSÁRIA]`

1. **Hierarquia analítica.** O fluxo E2→E3→E5 (estrutural→institucional→operacional/ICT) é **coerente** com a hierarquia inviolável Elliott→Fibonacci→Fractal→SMC→ICT (AGENTS.md §6.1) e com "ICT não cria hipótese" (§6.2). `[INFERÊNCIA]` — a confirmar por Spec.
2. **"Convicção" em múltiplos níveis** (estrutural E2, macro de contexto E4, global E6). O baseline tem **um** Conviction Vector 8D com fórmula/pesos/limiares **abertos (J-001)** e a distinção "convicção de risco" vs Conviction Vector é **RISK-CONV-001 (aberta)**. Se o workflow implica convicções distintas por camada, isso é **`[DECISÃO NECESSÁRIA]`** — não resolver aqui; alimenta o Dossiê de SPEC-003/014/RISK-SPEC.
3. **Manager como formador de convicção e decisor de envio.** Toca a fronteira Synthesis→Decisão e o papel de orquestração (SPEC-014/023/024). A separação Conviction Engine × Synthesis (B-001 FECHADA: Fusion→Conviction→Synthesis) deve ser respeitada. `[INFERÊNCIA]`.
4. **"Decidirá se envia sinal ou não ao bot finance externo".** Consistente com AGENTS.md §9: **o SOT produz um Signal Package**; a execução da ordem é do Bot Trade Finance externo. O SOT **não executa ordem** (INV-05). A decisão do Risk Agent é de **emitir/não-emitir sinal**, não de executar. `[FATO]` (âncora: AGENTS.md §9; EUA-E19a).
5. **Alarme-gatilho em nível de preço, ativável após a Killzone.** Mecanismo de runtime (armar/observar/ativar) — pertence a **K-001 / SPEC-018 (governança de runtime) / SPEC-045-RUNTIME-001** e a SPEC-008 (Scheduler). Não especificado hoje (§22 do ROADMAP). `[DECISÃO NECESSÁRIA]`.
6. **Timeframe de contexto ≠ timeframe de entrada** (E4 vs E5). Coerente com herança fractal/multi-timeframe (SPEC-009/010/011). `[INFERÊNCIA]`.
7. **Localização do agente de risco / arranjo (D-ARR-001) permanece RISK-ARR-LOC-001 (aberta).** O workflow não a fecha. `[DECISÃO NECESSÁRIA]`.
8. **Alavancagem como implicação do nível de convicção + tipo de oportunidade (Δ2, v2).** A v2 diz que a alavancagem **decorre** da convicção e do tipo de oportunidade — não é input do operador. Isso cria uma **dependência funcional convicção→alavancagem** que hoje **não tem regra no baseline**: toca **J-001** (fórmula/pesos/limiares da convicção, ABERTA) e **RISK-CONV-001** (convicção de risco ≠ Conviction Vector 8D, ABERTA), e possivelmente o dimensionamento do Risk Agent (BL-018). **Verifiquei o ROADMAP §Decisões abertas e o AGENTS.md §7:** não há decisão aberta que cubra especificamente "alavancagem por convicção". **Proponho o identificador `RISK-LEV-001`** (padrão RISK-*, seguindo RISK-CONV-001/RISK-ARR-LOC-001) para rastrear essa lacuna — **`[DECISÃO NECESSÁRIA]`; é proposta de identificador, não fato**: só Andraus cunha/abre a decisão. Não resolver aqui (CONS-01). **▸ CONFIRMADA/cunhada em §1-quater (Andraus, 2026-09-29): "ADIAR ATÉ SPEC DO AGENTE DE RISK" — decisão de *timing*; o mérito segue ABERTO, deferido a RISK-SPEC-*/BL-018.** Nota constitucional: `sizing_sugerido.alavancagem` já existe em `schemas/synthesis.output.json` como campo, mas **a regra de derivação convicção→alavancagem não está especificada** — o campo existir não fecha a decisão.

## 4. Uso obrigatório deste insumo (vínculo com a EUA-E23 / RULE-ECC-06) `[PROPOSTA→homologação]`

Após homologação da EUA-E23, este documento é **leitura obrigatória do Dossiê de Pesquisa** (RULE-ECC-02) de qualquer Spec cuja abertura:

- abra ou toque **K-001**, **SPEC-018** (Learning & Knowledge Formation Governance) ou **SPEC-045-RUNTIME-001**; ou
- especifique um **agente operacional**, um **agente manager/contexto/orquestrador** (SPEC-014/023/024) ou o **agente de risco** (RISK-SPEC-*, BL-018).

O Dossiê dessas Specs **DEVE** citar este insumo, confrontar a proposta de Andraus com o estado da arte pesquisado (lente arquitetural + lentes de domínio da RULE-ECC-05) e registrar, por etapa E1–E7, uma decisão **adotar / adaptar / rejeitar / adiar** — **sem** fechar nenhuma decisão aberta (CONS-01). Este insumo **não vincula o conteúdo** da Spec; vincula a **obrigação de considerá-lo**.

## 6. Schemas de contrato de dados (v2 — insumo estrutural) `[PROPOSTA]`

Atendendo à diretiva de Andraus (2026-09-29 — "elabore o schema e/ou demais mecanismo de entrega de dados estruturados para facilitar a leitura e especificação tanto do especificador quanto do revisor"), a v2 acompanha **5 JSON Schemas (Draft-07)** que modelam o workflow como **contratos de dados entre os agentes cognitivos**. Ficam em `schemas/`, seguindo a convenção dos schemas de 1a geração (`$id: sot://schemas/<nome>`, enum de symbol `BTCUSDT/XAUUSD/NAS100`, timeframes hierárquicos `S1/D1/H4/H1/M5`).

**Status epistemológico (idêntico ao deste documento e da EUA-E23):** `[PROPOSTA]` — **não homologados**. Cada arquivo carrega o campo `$comment` no topo com `status: PROPOSTA — não homologado; ver governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md`. Aguardam Revisor + homologação de Andraus. **Não fecham** nenhuma decisão aberta (J-001, RISK-CONV-001, RISK-ARR-LOC-001, M-001, K-001, D-RISK-SP-001 permanecem abertas). Não redefinem modelo canônico baselined (CONST-01): a hipótese continua CHM-001, a evidência CEM-001, o Conviction Vector 8D é **referenciado, não redefinido**.

| Schema | Etapa(s) | O que cobre | O que reaproveita / não redefine |
|---|---|---|---|
| `schemas/runtime-workflow.mission-dispatch.json` | E1, E2 | Parâmetros de missão do operador (ativo, tipo de missão, tipo de trade, TFs) + distribuição da missão pelo Manager ao estrutural. **v3:** par contexto/entrada restringido a 3 pares fixos via `oneOf` (D1→H1, H4→M15, H1→M5); M15 adicionado ao enum de TF | enum de symbol e base de TFs dos schemas de 1a geração (S1/D1/H4/H1/M5) + M15 (v3, tabela de Andraus); alavancagem marcada como implicação/`[DECISÃO NECESSÁRIA]` (RISK-LEV-001); exaustividade dos pares = `[DECISÃO NECESSÁRIA]` RUNTIME-TF-PAIR-001 |
| `schemas/runtime-workflow.conviction-report.json` | E3, E4, E6 | Entrega genérica de convicção por agente especializado (estrutural/institucional/operacional): TF analisado, classificação de evidência, ref. de hipótese, convicção. **v3:** M15 adicionado ao enum de `analyzed_timeframes` | reaproveita o conceito `conviction_pct` de `elliott-wave.output.json`; hipótese=CHM-001, evidência=CEM-001; `hypothesis_ref=null` para ICT (invariante); M15 (v3) — TFs devem pertencer ao par fixo da missão |
| `schemas/runtime-workflow.alarm-trigger.json` | E5 | Alarme-gatilho: nível de preço, condição, janela de ativação (após Killzone OU outro momento), status | enum de symbol; máquina de estados definitiva deferida a SPEC-008/M-001 |
| `schemas/runtime-workflow.manager-conviction-envelope.json` | E5, E7 | Dois momentos do Manager (convicção macro de contexto vs global) + payload "dados da oportunidade" ao Risk Agent | referencia Conviction Vector 8D (`synthesis.output.json`) sem redefinir; TMP=SPEC-016 repurposada (não redefinido) |
| `schemas/runtime-workflow.risk-decision.json` | E8 | Saída do Risk Agent: análise risco-retorno própria, convicção de risco, decisão ACCEPT/WAIT/REJECT/ABSTAIN, enviar/não sinal | estados de `SOT-RISK-MASTER-001 §3.5`; **NÃO define o Signal Package** — contrato deferido a RISK-SPEC-022 (`[DECISÃO NECESSÁRIA — D-RISK-SP-001]`) |

**Validação de sintaxe:** o Especificador não tem Bash; a validade sintática JSON não foi executada. **Pendência a confirmar por Andraus/operador:** rodar `python -m json.tool` em cada arquivo novo (ou `npm test`, atento a que o schema-lint do projeto pode tratar todos os schemas de `schemas/` como obrigatórios — os 5 novos são PROPOSTA, não baseline). Nenhum resultado de execução é reportado aqui (RULE-MET-01 — não-fabricação).

## 5. O que este documento NÃO faz `[FONTE]`

- Não fecha K-001, SPEC-018, SPEC-045-RUNTIME-001, RISK-CONV-001, RISK-ARR-LOC-001, J-001, G-001, H-001, M-001, N-001, C-001.
- Não redefine modelo canônico baselined (CONST-01): CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR intocados.
- Não altera a hierarquia analítica, R:R 1:3, convicção ≥70% / score ≥7/9, Conviction Vector 8D, Signal Package, INV-05.
- Não é ordem de implementação nem autorização de abertura de Spec — a abertura segue RULE-ECC-01/02 (passo 1-bis do ROADMAP §23).
- **Não resolve o MÉRITO de `RISK-LEV-001`** (alavancagem por convicção). Estado atualizado (§1-quater, Andraus 2026-09-29): o identificador foi **CONFIRMADO/cunhado**, mas a resolução do mérito foi **ADIADA** para a abertura da Spec do agente de risco (RISK-SPEC-*, BL-018) — decisão de *timing*, não de conteúdo. `RISK-LEV-001` permanece **ABERTA quanto ao mérito** (CONS-01); nenhuma fórmula/derivação de alavancagem é inferida aqui. Também não fecha `D-RISK-SP-001` (contrato do Signal Package). Os schemas da §6 são `[PROPOSTA]`, não baseline.
- **`RUNTIME-TF-PAIR-001` — pergunta original RESOLVIDA** (§1-quater, Andraus 2026-09-29): a tabela de 3 pares é **conjunto inicial EXTENSÍVEL** (não lista fechada/definitiva). Isto **não define** quais pares futuros nem quando/como seriam adicionados — a governança do processo de extensão fica como `[PROPOSTA]` (`RUNTIME-TF-PAIR-EXT-001`, só Andraus cunha). Os schemas codificam **literalmente os 3 pares** hoje dados (extensão = versionamento futuro, não aceitação de qualquer combinação hoje). Não propaga M15 aos schemas de 1a geração (lacuna registrada em §1-ter).

---

*Insumo registrado pelo Especificador (Claude Code), 2026-09-29 (v1), atualizado para v2 (2026-09-29, atualização de workflow + 5 schemas) e para v3 (2026-09-29, complemento: tabela de pareamento de timeframes contexto↔entrada — 3 pares fixos — + restrição `oneOf` nos schemas mission-dispatch/conviction-report e adição de M15), a partir de diretiva de Andraus em chat. Não-normativo; sujeito à homologação da EUA-E23 para adquirir o vínculo de leitura obrigatória da §4. v1 e v2 preservadas integralmente (INV-07 — nada removido).*
