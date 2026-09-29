# WORKFLOW.md — Orquestração Cognitiva do SOT em Runtime (documento único e canônico)

> **Documento de raiz — leitura obrigatória por todo agente** (ao lado de `ROADMAP.md`, `atomic-spec.md` e `AGENTS.md`), **núcleo sempre-obrigatório** (lido em toda sessão, em qualquer complexidade — não sujeito ao dial GES/EUA-E19).
> Descreve **como os agentes cognitivos já especificados operam juntos** durante uma sessão de trading ao vivo (runtime cognitivo).
> **4º pilar de leitura:** `ROADMAP.md` fixa a SEQUÊNCIA de Specs · `atomic-spec.md` fixa o MÉTODO de produzir Specs · `AGENTS.md` fixa IDENTIDADE/CONFIG · **`WORKFLOW.md` fixa a ORQUESTRAÇÃO COGNITIVA em runtime** — sem sobreposição entre eles.

| Campo | Valor |
|---|---|
| Documento | **`WORKFLOW.md`** (raiz) |
| Propósito | Orquestração cognitiva dos agentes especificados durante uma **sessão de trading ao vivo** (sequência de acionamento, formação de convicção em camadas, alarme-gatilho, pareamento de timeframes, decisão de sinal) |
| Natureza | **Não-normativo e descritivo.** Contém decisões abertas; **não** é comportamento de agente baselined — é o **contrato de orquestração vigente**. Não cria invariante, não fecha decisão aberta, não redefine canônico. |
| Status epistemológico | `[FONTE]` (registro verbatim de diretivas de Andraus) + `[INFERÊNCIA]` (decomposição/mapeamento contra o baseline) + `[DECISÃO NECESSÁRIA]` (o que depende de Andraus). Herda o status não-normativo e **todas** as decisões abertas do insumo que absorveu. |
| Origem do conteúdo | **Unifica e absorve** `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (v1→v4, SUPERSEDIDO — permanece como registro histórico do processo de elaboração, INV-07). Criado pela **EUA-E24** (DHR-EUA-E24, Andraus, 2026-09-29). |
| Fonte de verdade dos invariantes | **`AGENTS.md` §6.** Onde este documento menciona hierarquia analítica, R:R, convicção ou Signal Package, ele **remete** ao `AGENTS.md` §6 — **não** os redefine. |
| Ênfase de leitura (Q1, DHR-EUA-E24) | Leitura obrigatória de todo agente; **prioridade/peso reforçados para o Especificador na abertura da SPEC-002 e Specs de domínio subsequentes** — passo obrigatório reforçado do Dossiê de Pesquisa (RULE-ECC-06). |

---

## 0. Status e natureza `[FATO]`

- **Não-normativo e descritivo.** Este documento **descreve** a orquestração vigente; **não** cria invariante, **não** fecha decisão aberta, **não** redefine modelo canônico. Herda o status não-normativo e **todas** as decisões abertas do insumo `RUNTIME-WORKFLOW-001` (v1→v4), cujo conteúdo aqui unifica.
- **"Runtime" = orquestração cognitiva do Harness**, não runtime de software. O SOT está em fase spec-first (`AGENTS.md` §1); não há implementação de código a especificar aqui. "Runtime" é a **sequência de acionamento e a troca de evidência/hipótese/convicção entre os agentes LLM especificados** quando o SOT estiver operando em uma sessão de trading ao vivo. Não se infere daqui arquitetura de código, infraestrutura ou execução técnica.
  - **Achado registrado (não forçar equivalência):** se, na abertura da SPEC-045, a decisão **SPEC-045-RUNTIME-001** vier a ser interpretada como algo mais próximo de runtime técnico/software (carga física de prefixo/guardrails/Skills/memória — ROADMAP §20), essa distinção deve ser **explicitada como achado** na abertura; este documento **não** afirma equivalência entre "orquestração cognitiva" (sentido de Andraus aqui) e "runtime técnico" (possível leitura da §20). Os dois sentidos coexistem até que a SPEC-045 os separe. `[DECISÃO NECESSÁRIA]` — Andraus / abertura da SPEC-045.
- **Fonte de verdade dos invariantes = `AGENTS.md` §6.** Onde este documento menciona hierarquia analítica, R:R, convicção ou Signal Package, ele **remete** — não redefine.
- **Trilha histórica/processo de elaboração:** o registro de como o workflow evoluiu (v1→v4) está **integrado abaixo** (§1) e permanece **também** preservado em `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (SUPERSEDIDO por este documento, mas **não deletado** — INV-07).
- **Vínculo com a RULE-ECC-06 (EUA-E23):** para Specs de K-001/SPEC-018/SPEC-045-RUNTIME-001 ou de agente operacional/manager/risco, o **Dossiê de Pesquisa** deve considerar este workflow decisão-a-decisão por etapa (E1–E8). **Após a EUA-E24, este `WORKFLOW.md` é a fonte vigente dessa obrigação de leitura** (o histórico de elaboração permanece em `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md`, superseded).
- **Em qualquer conflito** entre este documento e um invariante constitucional (`AGENTS.md` §6/§9), **o invariante prevalece** e o conflito vira achado a tratar na abertura da Spec correspondente.

---

## 1. Histórico verbatim das diretivas de Andraus (v1→v4) `[FONTE]`

> Transcrição literal — RCN-001/PC-06. A citação **é** a evidência da diretiva de Andraus; grafia original preservada (incluindo "Está"/"evidencia").

### v1 — workflow inicial (Andraus, 2026-09-29) `[FONTE]`

> "Está é minha proposta de workflow do Trading em runtime com o SOT:
>
> Antes da abertura da Killzone coloco o sistema para rodar. Aponto o Time frame e o tipo de Trading que quero realizar: position, swing ou day Trading. Agente estrutural começará a verificar a estrutura de ondas e após observar, marcar, tratar evidencia, hipótese e formar convicção entrega sua análise e convicção. Se houver oportunidade apontada pelo agente anterior, dispara o agente institucional que fará o mesmo. Após sua análise e entrega, o manager agente formará a convicção macro de contexto e se houver oportunidade conclusiva deverá adicionar um alarme-gatilho no nível de preço a ser ativado ou não após abertura da Killzone. Se ativado agente operacional entra com sua análise do time frame da entrada (difere do de contexto) fazendo o devido tratamento e entrega ao manager. Após colher os dados do operacional o manager formará convicção global e decidirá envio com dados de risco-retorno ao agente de risco que por sua vez fará sua análise e decidirá se envia sinal ou não ao bot finance externo com dados da entrada."

### v2 — workflow atualizado (Andraus, 2026-09-29) `[FONTE]`

> "Antes da abertura da Killzone coloco o sistema para rodar. Aponto o ativo alvo, o tipo da missão: se de exploração ou de validação, o tipo de Trading: position, swing ou day Trading (Implicação na alavancagem a depender do nível da convicção e tipo da oportunidade) e o time frame de analise O manager agente começara a distribuição da missão com o Agente estrutural que irá verificar a estrutura de ondas no time frame de contexto e no de entrada e após observar, marcar, classificar tratar evidencia, hipótese e formar convicção entrega sua convicção. Se houver oportunidade apontada (a depender da convicção especializada), o agente institucional entra em cena e fará o mesmo procedimento no time frame de contexto apenas. Após sua análise e entrega, o manager agente formará a convicção macro de contexto e se houver oportunidade conclusiva deverá adicionar um alarme-gatilho no nível de preço a ser ativado ou não após abertura da Killzone ou mesmo em outro momento. Se ativado e válido, o agente operacional entra com sua análise do time frame da entrada (difere do de contexto) fazendo o devido tratamento e entrega ao manager. Após colher os dados do operacional o manager formará convicção global e decidirá envio com dados da oportunidade ao agente de risco que por sua vez fará sua análise de risco-retorno e decidirá por convicção se envia sinal ou não ao bot finance externo com dados da entrada."

**Diferenças notáveis v1 → v2 (registro de fato, não resolução) `[FONTE]`/`[DECISÃO NECESSÁRIA]`:**

| # | Mudança da v2 frente à v1 | Natureza |
|---|---|---|
| Δ1 | Novos parâmetros de missão explícitos: **ativo alvo** e **tipo de missão (exploração vs validação)** | `[FONTE]` — acréscimo de input |
| Δ2 | **Alavancagem** deixa de ser input e passa a ser **implicação** do nível de convicção + tipo de oportunidade | `[DECISÃO NECESSÁRIA]` — fórmula/derivação não dita (ver §6, tensão 8) |
| Δ3 | O **Manager distribui ativamente a missão** ao agente estrutural (na v1 o acionamento era implícito) | `[FONTE]` — novo ator/etapa |
| Δ4 | O **agente estrutural analisa dois timeframes** (contexto E entrada), não só um | `[FONTE]` |
| Δ5 | Menção explícita a **classificar** evidência (v1: só "tratar evidência, hipótese") | `[FONTE]` |
| Δ6 | O **agente institucional atua apenas no timeframe de contexto** (explicitado) | `[FONTE]` |
| Δ7 | Alarme-gatilho ativável "após a Killzone **ou mesmo em outro momento**" (v1: só após a Killzone) | `[FONTE]` |
| Δ8 | Alarme ativado exige **"ativado E válido"** antes de acionar o operacional (v2 acrescenta "e válido") | `[FONTE]` |
| Δ9 | Manager envia ao Risk Agent **"dados da oportunidade"** (v1: "dados de risco-retorno") — o risco-retorno passa a ser **análise do próprio Risk Agent** | `[FONTE]` — realoca a análise risco-retorno |
| Δ10 | Risk Agent decide **"por convicção"** se envia sinal (reforça convicção de risco — tensão RISK-CONV-001) | `[DECISÃO NECESSÁRIA]` |

### v3 — tabela de pareamento de timeframes contexto↔entrada (Andraus, 2026-09-29) `[FONTE]`

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

**Leitura do dado — 3 pares fixos, não produto cartesiano `[FONTE]`/`[INFERÊNCIA]`:** o texto cita cada par contexto→entrada **uma vez**, com "Análise macro em X entrada em Y". São **exatamente 3 pares fixos** — **não** um produto cartesiano entre {D1,H4,H1} e {H1,M15,M5} (que geraria 9 combinações). Registro como fato observado; não há ambiguidade a resolver (RULE-MET-01 — não fabricar combinações não ditas). Detalhamento na §4.

### v4 — decisões de Andraus sobre os identificadores propostos (Andraus, 2026-09-29) `[FONTE]`/`[FATO NORMATIVO]`

Os dois identificadores de decisão aberta propostos — **RISK-LEV-001** (alavancagem por convicção) e **RUNTIME-TF-PAIR-001** (natureza da tabela de 3 pares) — eram `[PROPOSTA]` de identificador (só Andraus cunha/abre decisão). Andraus respondeu às duas em chat, verbatim:

**RISK-LEV-001 — alavancagem por convicção `[FATO NORMATIVO — decisão de timing]`:**

> **Andraus (2026-09-29):** "ADIAR ATÉ SPEC DO AGENTE DE RISK"

**Leitura (RULE-MET-01 — sem inferir além do dito):** Andraus **CONFIRMA e cunha oficialmente** o identificador `RISK-LEV-001` como decisão aberta. A resposta é uma **decisão de *timing*, NÃO uma resolução do mérito**: a lacuna "alavancagem derivada do nível de convicção + tipo de oportunidade" fica **aberta e deferida** para a abertura da **Spec do agente de risco (RISK-SPEC-*, BL-018)**. Nenhuma fórmula/derivação convicção→alavancagem é definida ou inferida (CONS-01: `RISK-LEV-001` continua ABERTA quanto ao mérito, apenas com o momento de resolução definido). Toca **J-001** e **RISK-CONV-001**, ambas abertas.

**RUNTIME-TF-PAIR-001 — natureza da tabela de 3 pares `[FATO NORMATIVO — pergunta resolvida]`:**

> **Andraus (2026-09-29):** "EXTENSÍVEL"

**Leitura (RULE-MET-01):** Andraus **CONFIRMA** o identificador `RUNTIME-TF-PAIR-001` e **resolve a pergunta original** ("a tabela de pareamento é lista fechada/definitiva ou conjunto inicial extensível?"): os 3 pares (D1→H1, H4→M15, H1→M5) **NÃO são lista fechada** — são um **conjunto inicial extensível** (novos pares podem ser acrescentados no futuro). O que Andraus **NÃO** disse (e portanto **não** se infere): **QUAIS** seriam os pares futuros e **QUANDO/COMO** um novo par seria adicionado — a governança do processo de extensão permanece `[DECISÃO NECESSÁRIA]`, registrada como **`RUNTIME-TF-PAIR-EXT-001`** (`[PROPOSTA]` de identificador — só Andraus cunha). Enquanto isso, os schemas codificam **exatamente os 3 pares literais** (fail-closed: extensão = versionamento futuro, não aceitação de qualquer combinação hoje).

---

## 2. Parâmetros de missão (o operador arma o sistema antes da Killzone) `[FONTE]`

O operador (Andraus) arma o sistema antes da abertura da Killzone e aponta:
- **ativo alvo** (BTC / XAU / NASDAQ — enum `BTCUSDT / XAUUSD / NAS100`);
- **tipo de missão:** exploração ou validação;
- **tipo de trade:** position / swing / day (implica na alavancagem conforme convicção + tipo de oportunidade — a **regra de derivação convicção→alavancagem NÃO está especificada**: `[DECISÃO NECESSÁRIA]` **RISK-LEV-001**, mérito adiado à Spec do agente de risco, RISK-SPEC-*/BL-018);
- **par de timeframes** (contexto ↔ entrada) — ver §4.

---

## 3. O fluxo de 8 etapas (E1–E8) `[FONTE]` (paráfrase) / `[INFERÊNCIA]` (mapeamento a slots)

Consolidado da decomposição v4. A coluna "slot" é **indicativa** (`[INFERÊNCIA]`); a coluna "depende de" lista decisões abertas que a governam (`[DECISÃO NECESSÁRIA]`, não fechadas aqui). A coluna `Schema` aponta ao contrato de dados proposto na §5 (insumo estrutural — `[PROPOSTA]`, não homologado).

| # | Etapa | Ator | Slot indicativo | Depende de (aberta) | Schema (§5) |
|---|---|---|---|---|---|
| **E1** | Operador arma o sistema; aponta **ativo alvo**, **tipo de missão** (exploração/validação), **tipo de trade** (position/swing/day) e **par de timeframes**. Alavancagem = **implicação**, não input. | Operador | SPEC-008/009 | K-001 · G-001 · **RISK-LEV-001** | `runtime-workflow.mission-dispatch` (`mission_parameters`) |
| **E2** | **Manager distribui a missão** ao agente estrutural (novo na v2). | Manager | SPEC-014/023 | K-001 | `runtime-workflow.mission-dispatch` (`manager_dispatch`) |
| **E3** | **Agente estrutural** verifica estrutura de ondas no TF de **contexto E de entrada**; observa, marca, **classifica**, trata evidência+hipótese, forma convicção; entrega. | Estrutural | SPEC-010 · SPEC-011 · CHM-001 · CEM-001 | J-001 | `runtime-workflow.conviction-report` (`agent_role=structural`) |
| **E4** | Se há oportunidade (conforme convicção especializada), **agente institucional** faz o mesmo **apenas no TF de contexto**. | Institucional | SPEC-012 · sub-hipótese `parent_id` (Q-005) | J-001 | `runtime-workflow.conviction-report` (`agent_role=institutional`) |
| **E5** | **Manager** forma **convicção macro de contexto**; se conclusiva, adiciona **alarme-gatilho** em nível de preço, ativável após a Killzone **ou em outro momento**. | Manager | SPEC-014/023 · Conviction Engine (B-001 fechada: Fusion→Conviction→Synthesis) · SPEC-008 | J-001 · M-001 · K-001 | `runtime-workflow.manager-conviction-envelope` (`macro_context`) + `runtime-workflow.alarm-trigger` |
| **E6** | Se o alarme é **ativado E válido**, **agente operacional** analisa o **TF de entrada** (difere do de contexto); trata e entrega. **ICT NÃO cria hipótese** (`AGENTS.md` §6.2) — só executa/confirma. | Operacional | SPEC-013 (ICT) | — | `runtime-workflow.conviction-report` (`agent_role=operational`, `hypothesis_ref=null`) |
| **E7** | **Manager** forma **convicção global** e decide envio ao Risk Agent com **dados da oportunidade** (não risco-retorno pré-calculado). | Manager | SPEC-014 · TMP (artefato interno Synthesis→Risk, EUA-E19a) · Risk Agent (BL-018) | J-001 · RISK-CONV-001 | `runtime-workflow.manager-conviction-envelope` (`global` + `dispatch_to_risk`) |
| **E8** | **Agente de risco** faz **sua própria análise de risco-retorno** e decide **por convicção** se envia o **Signal Package** ao **bot finance externo**. O SOT **não executa ordem** (INV-05). | Risk Agent | RISK-SPEC-* (BL-018) · Signal Package (D-RISK-SP-001, RISK-SPEC-022) | RISK-ARR-LOC-001 · RISK-CONV-001 · SPEC-045-RUNTIME-001 | `runtime-workflow.risk-decision` |

**Hierarquia analítica preservada:** o encadeamento E3→E4→E6 (estrutural → institucional → operacional/ICT) é coerente com a hierarquia inviolável **Elliott → Fibonacci → Fractal → SMC → ICT** (`AGENTS.md` §6.1) e com "ICT não cria hipótese" (§6.2). Camada inferior não sobrepõe superior. `[INFERÊNCIA]` — a confirmar por Spec.

**Convicção em camadas — atenção.** O fluxo menciona convicção em vários momentos (estrutural E3, macro de contexto E5, global E7, de risco E8). O baseline tem **um** Conviction Vector 8D com fórmula/pesos/limiares **abertos (J-001)**, e a distinção "convicção de risco" vs. Conviction Vector é **RISK-CONV-001 (aberta)**. Se o workflow implica convicções distintas por camada, isso é **`[DECISÃO NECESSÁRIA]`** — **não** resolvido aqui; matéria de Dossiê das Specs correspondentes.

---

## 4. Pareamento de timeframes contexto ↔ entrada (3 pares, extensível) `[FONTE]`

O TF de **contexto** (análise estrutural E3 + institucional E4) e o TF de **entrada** (confluência multi-timeframe + operacional E6) são acoplados em **3 pares fixos** (não produto cartesiano):

| Par | Macro (contexto) | Micro (entrada) | Usado por |
|---|---|---|---|
| 1 | **D1** | **H1** | Contexto: estrutural (E3) + institucional (E4). Entrada: estrutural (E3) + operacional (E6). |
| 2 | **H4** | **M15** | idem |
| 3 | **H1** | **M5** | idem |

- O **H1 aparece em dois papéis** — como TF de **contexto** no Par 3 (entrada M5) e como TF de **entrada** no Par 1 (contexto D1). São usos distintos do mesmo TF em pares diferentes, **não** uma contradição nem uma quarta combinação. Não colapsar em erro nem inferir par adicional.
- Onde a restrição incide: **E1** (mission dispatch aponta UM dos 3 pares, não dois campos livres); **E3** opera no contexto E na entrada do par; **E4** opera só no contexto do par; **E6** opera só na entrada do par. Restrição codificada por `oneOf` de 3 pares em `runtime-workflow.mission-dispatch.json` (§5).
- O conjunto é **extensível** (RUNTIME-TF-PAIR-001, resolvida por Andraus: "conjunto inicial extensível"). Novos pares entram por **versionamento futuro** de schema/documento — **não** significa aceitar qualquer combinação hoje (os schemas codificam **literalmente os 3 pares**). O **processo de extensão** (quando/como) permanece `[DECISÃO NECESSÁRIA]` **RUNTIME-TF-PAIR-EXT-001** (só Andraus cunha).
- **Lacuna registrada (não resolvida) — M15 vs S1 `[FONTE]`/`[DECISÃO NECESSÁRIA]`:** a tabela de Andraus usa **D1/H4/H1/M15/M5**, incluindo **M15**. Os schemas de 1ª geração (`elliott-wave.*`, `smc.*`, `ict.*`, `synthesis.*`) usam **S1/D1/H4/H1/M5** — **sem M15** e **com S1** (que a tabela de Andraus não cita). Os schemas `runtime-workflow.*` tiveram **M15 adicionado** aos enums; os schemas de 1ª geração **NÃO foram tocados** (fora de escopo; história própria — RULE-MET-01/INV-07). Reconciliar o conjunto de TFs entre 1ª geração e `runtime-workflow.*` é `[DECISÃO NECESSÁRIA]` para a abertura das Specs SPEC-010/011/012/013/014. Não inventar M15 nos schemas antigos.

---

## 5. Contrato de dados — 5 schemas de referência `[PROPOSTA]`

Atendendo à diretiva de Andraus (2026-09-29 — "elabore o schema e/ou demais mecanismo de entrega de dados estruturados para facilitar a leitura e especificação tanto do especificador quanto do revisor"), o workflow é acompanhado de **5 JSON Schemas (Draft-07)** que o modelam como **contratos de dados entre os agentes cognitivos**. Ficam em `schemas/`, seguindo a convenção dos schemas de 1ª geração (`$id: sot://schemas/<nome>`, enum de symbol `BTCUSDT/XAUUSD/NAS100`, timeframes hierárquicos).

**Status epistemológico:** `[PROPOSTA]` — **não homologados**. Cada arquivo carrega `$comment` no topo com `status: PROPOSTA — não homologado`. Aguardam Revisor + homologação de Andraus. **Não fecham** nenhuma decisão aberta (J-001, RISK-CONV-001, RISK-ARR-LOC-001, M-001, K-001, D-RISK-SP-001 permanecem abertas). Não redefinem modelo canônico baselined (CONST-01): a hipótese continua CHM-001, a evidência CEM-001, o Conviction Vector 8D é **referenciado, não redefinido**.

| Schema | Etapa(s) | O que cobre | O que reaproveita / não redefine |
|---|---|---|---|
| `schemas/runtime-workflow.mission-dispatch.json` | E1, E2 | Parâmetros de missão do operador (ativo, tipo de missão, tipo de trade, TFs) + distribuição da missão pelo Manager ao estrutural. Par contexto/entrada restringido a 3 pares fixos via `oneOf` (D1→H1, H4→M15, H1→M5); M15 no enum de TF. | enum de symbol e base de TFs de 1ª geração + M15; alavancagem = implicação/`[DECISÃO NECESSÁRIA]` (RISK-LEV-001); extensibilidade dos pares = fato de documentação (RUNTIME-TF-PAIR-001 resolvida) |
| `schemas/runtime-workflow.conviction-report.json` | E3, E4, E6 | Entrega genérica de convicção por agente especializado (estrutural/institucional/operacional): TF analisado, classificação de evidência, ref. de hipótese, convicção. | `conviction_pct` de `elliott-wave.output.json`; hipótese=CHM-001, evidência=CEM-001; `hypothesis_ref=null` para ICT (invariante); M15 no enum — TFs devem pertencer ao par fixo da missão |
| `schemas/runtime-workflow.alarm-trigger.json` | E5 | Alarme-gatilho: nível de preço, condição, janela de ativação (após Killzone OU outro momento), status. | enum de symbol; máquina de estados definitiva deferida a SPEC-008/M-001 |
| `schemas/runtime-workflow.manager-conviction-envelope.json` | E5, E7 | Dois momentos do Manager (convicção macro de contexto vs global) + payload "dados da oportunidade" ao Risk Agent. | referencia Conviction Vector 8D (`synthesis.output.json`) sem redefinir; TMP = SPEC-016 repurposada (não redefinido) |
| `schemas/runtime-workflow.risk-decision.json` | E8 | Saída do Risk Agent: análise risco-retorno própria, convicção de risco, decisão ACCEPT/WAIT/REJECT/ABSTAIN, enviar/não sinal. | estados de `SOT-RISK-MASTER-001 §3.5`; **NÃO define o Signal Package** — contrato deferido a RISK-SPEC-022 (`[DECISÃO NECESSÁRIA — D-RISK-SP-001]`) |

**Validação de sintaxe:** pendência de execução por quem tem Bash (`python -m json.tool` em cada arquivo, ou `npm test` — atento a que o schema-lint pode tratar todos os schemas de `schemas/` como obrigatórios; os 5 são PROPOSTA, não baseline). Nenhum resultado de execução é reportado aqui (RULE-MET-01 — não-fabricação).

---

## 6. Pontos de atenção / tensões com o baseline (a tratar na abertura, não aqui) `[INFERÊNCIA]`/`[DECISÃO NECESSÁRIA]`

1. **Hierarquia analítica.** O fluxo E3→E4→E6 (estrutural→institucional→operacional/ICT) é **coerente** com a hierarquia inviolável Elliott→Fibonacci→Fractal→SMC→ICT (`AGENTS.md` §6.1) e com "ICT não cria hipótese" (§6.2). `[INFERÊNCIA]` — a confirmar por Spec.
2. **"Convicção" em múltiplos níveis** (estrutural E3, macro de contexto E5, global E7, de risco E8). O baseline tem **um** Conviction Vector 8D com fórmula/pesos/limiares **abertos (J-001)** e a distinção "convicção de risco" vs Conviction Vector é **RISK-CONV-001 (aberta)**. Convicções distintas por camada = `[DECISÃO NECESSÁRIA]`.
3. **Manager como formador de convicção e decisor de envio.** Toca a fronteira Synthesis→Decisão e o papel de orquestração (SPEC-014/023/024). A separação Conviction Engine × Synthesis (B-001 FECHADA: Fusion→Conviction→Synthesis) deve ser respeitada. `[INFERÊNCIA]`.
4. **"Decidirá se envia sinal ou não ao bot finance externo".** Consistente com `AGENTS.md` §9: o SOT produz um **Signal Package**; a execução da ordem é do Bot Trade Finance externo. O SOT **não executa ordem** (INV-05). A decisão do Risk Agent é de **emitir/não-emitir sinal**, não de executar. `[FATO]` (âncora: AGENTS.md §9; EUA-E19a).
5. **Alarme-gatilho em nível de preço, ativável após a Killzone.** Mecanismo de runtime (armar/observar/ativar) — pertence a **K-001 / SPEC-018 / SPEC-045-RUNTIME-001** e a SPEC-008 (Scheduler). Não especificado hoje. `[DECISÃO NECESSÁRIA]`.
6. **Timeframe de contexto ≠ timeframe de entrada** (E4 vs E6). Coerente com herança fractal/multi-timeframe (SPEC-009/010/011) e com os 3 pares da §4. `[INFERÊNCIA]`.
7. **Localização do agente de risco / arranjo (D-ARR-001) permanece RISK-ARR-LOC-001 (aberta).** O workflow não a fecha. `[DECISÃO NECESSÁRIA]`.
8. **Alavancagem como implicação do nível de convicção + tipo de oportunidade (Δ2, v2).** Cria dependência funcional convicção→alavancagem que **não tem regra no baseline**: toca **J-001** e **RISK-CONV-001**, e possivelmente o dimensionamento do Risk Agent (BL-018). Identificador cunhado por Andraus: **`RISK-LEV-001`** — "ADIAR ATÉ SPEC DO AGENTE DE RISK" (§1 v4): decisão de *timing*; o mérito segue ABERTO, deferido a RISK-SPEC-*/BL-018. Nota constitucional: `sizing_sugerido.alavancagem` já existe em `schemas/synthesis.output.json` como campo, mas **a regra de derivação convicção→alavancagem não está especificada** — o campo existir não fecha a decisão.

---

## 7. Vínculo com a RULE-ECC-06 — obrigação de leitura no Dossiê `[FATO NORMATIVO — obrigação de leitura]`

Com a homologação da EUA-E23/RULE-ECC-06 (DHR-EUA-E23, 2026-09-29) e sua consequente atualização de referência pela EUA-E24 (DHR-EUA-E24, 2026-09-29), **este `WORKFLOW.md` é leitura obrigatória do Dossiê de Pesquisa** (RULE-ECC-02) de qualquer Spec (SPEC-002 em diante) cuja abertura:

- abra ou toque **K-001**, **SPEC-018** (Learning & Knowledge Formation Governance) ou **SPEC-045-RUNTIME-001**; ou
- especifique um **agente operacional**, um **agente manager/contexto/orquestrador** (SPEC-014/023/024) ou o **agente de risco** (RISK-SPEC-*, BL-018).

O Dossiê dessas Specs **DEVE** citar este documento, confrontar a proposta de Andraus com o estado da arte pesquisado (lente arquitetural + 6 lentes de domínio da RULE-ECC-05) e registrar, por etapa **E1–E8**, uma decisão **adotar / adaptar / rejeitar / adiar** — **sem** fechar nenhuma decisão aberta (CONS-01). Este documento **não vincula o conteúdo** da Spec; vincula a **obrigação de considerá-lo**. Ausência da consideração numa Spec aplicável = **Médio** (Dossiê incompleto); tratar o workflow como decisão fechada = **Crítico** (viola CONS-01/RULE-MET-01).

> **Ênfase (Q1, DHR-EUA-E24):** para o **Especificador**, na abertura da **SPEC-002** (primeira Spec de domínio desta fase — Trilha B) e nas Specs de domínio subsequentes, a leitura deste `WORKFLOW.md` é **passo obrigatório reforçado** do Dossiê de Pesquisa, não apenas mais uma fonte de contexto geral.

---

## 8. Decisões abertas que este documento NÃO fecha (CONS-01) `[DECISÃO NECESSÁRIA]`

`J-001` (fórmula/pesos/limiares definitivos da convicção) · `G-001` · `H-001` · `K-001` · `C-001` · `M-001` · `N-001` · `SPEC-045-RUNTIME-001` · `RISK-ARR-LOC-001` · `RISK-CONV-001` · `RISK-LEV-001` (mérito adiado à Spec de risco) · `RUNTIME-TF-PAIR-EXT-001` (processo de extensão dos pares) · `D-RISK-SP-001` (contrato do Signal Package).

Fechadas (não reabrir, mas registradas para leitura): **B-001** (Conviction Engine SEPARADO do Synthesis: Fusion→Conviction→Synthesis) · **RUNTIME-TF-PAIR-001** (pergunta original resolvida: 3 pares = conjunto extensível — o *processo* de extensão é RUNTIME-TF-PAIR-EXT-001, ainda aberto).

Nenhuma leitura deste documento pode tratar qualquer item **aberto** acima como fechado.

---

## 9. O que este documento NÃO faz `[FONTE]`

- **Não define a sequência de Specs** — isso é só o `ROADMAP.md`.
- **Não define o método de produzir Specs** (BASpec, D0–D9, Enforcement Contract, etiquetagem) — isso é só o `atomic-spec.md`.
- **Não redefine identidade/config, papéis, profiles nem os não-negociáveis constitucionais** — isso é só o `AGENTS.md` (§6 é a fonte de verdade dos invariantes).
- **Não fecha decisão aberta** (CONS-01) **nem redefine canônico** (CONST-01): CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR intocados.
- **Não altera** a hierarquia analítica, R:R 1:3, convicção ≥70%/score ≥7/9, Conviction Vector 8D, Signal Package, INV-05.
- **Não é ordem de implementação nem autorização de abertura de Spec** — a abertura segue RULE-ECC-01/02 (passo 1-bis do ROADMAP §23).
- **Não substitui** a obrigação de Dossiê da RULE-ECC-06 — é a fonte vigente dessa obrigação (o histórico de elaboração permanece em `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md`, superseded, INV-07).

---

## 10. Referências

`AGENTS.md` (§1 leitura obrigatória; §6 invariantes; §9 Signal Package/INV-05) · `ROADMAP.md` · `atomic-spec.md` (§15 Dossiê / RULE-ECC-05/06) · `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (SUPERSEDIDO — registro histórico do processo de elaboração v1→v4, INV-07) · `governance/EUA-E23_Lentes_Dominio_Dossie_Pesquisa_PROPOSTA.md` (RULE-ECC-05/06) · `governance/EUA-E24_WORKFLOW_Raiz_Orquestracao_Cognitiva_PROPOSTA.md` + `governance/DHR-EUA-E24_Ata_Homologacao_WORKFLOW_Raiz.md` (emenda/ata que criaram este documento) · `schemas/runtime-workflow.*.json` (5 schemas, PROPOSTA) · `canon/CHM-001` (hipótese) · `canon/CEM-001` (evidência) · `canon/CEE-001` v2.0 (economia/4Es/salvaguardas).

---

*Documento único e canônico da orquestração cognitiva do SOT em runtime. Criado pela EUA-E24 (DHR-EUA-E24, 2026-09-29), unificando e absorvendo o conteúdo integral do insumo `RUNTIME-WORKFLOW-001` (v1→v4). Não-normativo; herda o status não-normativo e as decisões abertas do insumo. Trilha histórica do processo de elaboração preservada em `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (SUPERSEDIDO, não deletado — INV-07). Fonte de verdade dos invariantes = `AGENTS.md` §6.*
