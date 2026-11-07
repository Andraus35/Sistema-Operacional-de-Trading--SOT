# Manager Contract — contrato comum do Manager Agent (Fases 0, 1 e 2)

> **PROPOSTA — não é baseline; só vigora com homologação de Andraus.** (INV-09)

| Campo | Valor |
|---|---|
| Versão | v0.2 (proposta; revisão R1→R2) — ID definitivo e versão de baseline = decisão de Andraus (ver §9, ponto A-1) *[antes: "v0.1 (proposta) — ID definitivo e versão de baseline = decisão de Andraus (ver §9, ponto A-1)"]* |
| Data | 2026-11-07 |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Origem | P-4 da abertura da SPEC-008 (`specs/features/SPEC-008/ABERTURA.md` §13), recomendação aceita por Andraus (`governance/DHR-SPEC008-001_Ata_Homologacao_Abertura_SPEC-008.md` §1, linha P-4..P-9; §3: "antes, o **Manager Contract** curto (P-4, recomendação) para homologação conjunta"); ordem de Andraus em chat, 2026-11-07: "Manager Contract primeiro" (via Orquestrador) |
| Instituído como direção por | `governance/DHR-EUA-E23_Ata_Homologacao_Manager_Unificado.md` §2 item 2 |
| Natureza | Documento de **consolidação**. Só junta o que Andraus já decidiu sobre o Manager. **Não** cria regra, campo, estado, transição, ID normativo nem agente de trading. **Não** fecha decisão aberta (CONS-01). **Não** edita `WORKFLOW.md`, `ROADMAP.md`, `AGENTS.md`, `canon/` nem `governance/`. |
| Etiquetas | `[FATO]` = texto de documento homologado, com âncora · `[INFERÊNCIA]` = leitura derivada, com âncora · `[PROPOSTA]` = requer homologação · `[DECISÃO NECESSÁRIA]` = só Andraus |
| Referência não-baseline (R1-M03) | As decisões da abertura da SPEC-008 são citadas pela **linha de decisão da ata** `DHR-SPEC008-001` (2026-11-07) §1. O **conteúdo** de cada decisão (ex.: o texto da CONF-1) só existe em `ABERTURA.md`, na **redação homologada "como está" em 2026-11-07** (DHR-SPEC008-001 §1, frase de abertura; Ref: "com §16/§16-bis"; parecer R3). Essa redação **não é baseline** (DHR-SPEC008-001, Status: "NÃO é baseline") e não tem número de versão; o hash do commit **não** foi fixado pelo Especificador (sem Bash). Toda citação de `ABERTURA.md` neste documento é **contexto não-baseline**, nunca herança (RULE-HD-04). Versão formal, se Andraus exigir: ponto A-1. |

---

## 1. Para que serve (em uma frase)

O Manager é **um só ator** que trabalha em **três Fases**; este contrato reúne num lugar só o que vale para as três, para que as três Specs do Manager (SPEC-015, SPEC-008, SPEC-014) herdem as mesmas obrigações e não se contradigam. `[FATO]` DHR-EUA-E23 §2 item 2: o contrato "garante o **ator único** (ADR §2.2) e disciplina as fronteiras Fase 0↔Fase 1↔Fase 2 (evitando reintroduzir o paradoxo circular que o ADR resolveu)".

**Regra de leitura** `[PROPOSTA]`: este documento não tem autoridade própria sobre as fontes que junta. Se algum item daqui divergir do texto-fonte citado, vale o texto-fonte e a divergência é achado a corrigir aqui (consequência de RULE-HD-02/RULE-HV-03 — o herdado prevalece sobre o local). **Exceção:** nos trechos de fonte que o §8.3 marca como "não herdado — prevalece X", o texto-fonte divergente **não** é herdado; vale a decisão homologada posterior ali citada, até Andraus corrigir a fonte (§9, A-4). *[antes: "…(consequência de RULE-HD-02/RULE-HV-03 — o herdado prevalece sobre o local)." — sem a exceção; a regra mandava prevalecer textos que o próprio A-4 declara divergentes (R1-M02)]*

### 1-bis. Vocabulário: "Fase" tem três acepções (CC-10 / RULE-SEM) — R1-m02

| Acepção | Onde aparece | O que designa | Etiqueta e âncora |
|---|---|---|---|
| **Fase 0 / 1 / 2 do Manager** — **sentido usado neste contrato** | ADR-MANAGER-001 §4.3; GLOSSARIO, "Manager Agent — nomenclatura normativa das 3 fases" | Modo de trabalho do **Manager**: 0 = Mission Lifecycle, 1 = Dispatch, 2 = Conviction | `[FATO]` ADR §4.3 |
| **"Fase 1" / "Fase 2" do pipeline** | WORKFLOW WF-02, WF-03, WF-04, WF-06 | Trecho do **ciclo operacional**. WF-02/WF-03 chamam de "Fase 1" o trabalho dos **agentes analíticos** (Estrutural, Institucional); WF-04 e WF-06 se mapeiam explicitamente à Fase 1/Dispatch e à Fase 2/Conviction do ADR. | `[FATO]` texto de WF-02..WF-06 · a distinção = `[INFERÊNCIA]`: a análise de WF-02/WF-03 **não** é trabalho do Manager-Fase-1 (ADR §2.2, §2.5: o Manager não analisa mercado); o Manager-Fase-1 só **despacha** essa análise |
| **FASE do ROADMAP** (ex.: FASE 4, FASE 6, FASE RISK) | `ROADMAP.md` | Etapa do **caminho de especificação** (grupo de Specs); "FASE RISK" = família RISK-SPEC do Risk Agent | `[FATO]` ROADMAP §7/§10-bis; AGENTS.md §6 item 9 |

Neste contrato, "Fase" sem qualificador = **Fase do Manager** (1ª linha). Quando se fala do pipeline, escreve-se "passo WF-xx"; do ROADMAP, "FASE" em maiúsculas.

---

## 2. Ator único

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 2.1 | O Manager Agent é o **único componente de orquestração** do SOT. | `[FATO]` ADR-MANAGER-001 v1.0 §2.2 |
| 2.2 | O Manager **não é agente analítico**: não analisa mercado, não formula hipóteses de mercado, não possui skills de análise técnica. Seus domínios são gestão de missões, orquestração de despacho e síntese de convicções. | `[FATO]` ADR-MANAGER-001 v1.0 §2.2 e §2.5 ("FATO NORMATIVO") |
| 2.3 | Master Orchestrator, Mission Engine, Decision Orchestrator, Orchestration Layer, Agente Decisor e Agente de Síntese **não** aparecem em Spec futura como componente independente; foram absorvidos pelo Manager. | `[FATO]` ADR-MANAGER-001 v1.0 §2.1 ("FATO NORMATIVO"); DHR-ARQ-002 §2 item 1 (Synthesis Agent = Fase 2) |
| 2.4 | "Conviction Engine" é rótulo de **mecanismo** (CCM-001, SPEC-003) **invocado** pelo Manager — Fase 2; não é agente de trading nem componente separado. | `[FATO]` DHR-ARQ-001 §2 itens 1 e 3 |
| 2.5 | As três Specs do Manager **não** criam agente de trading adicional; o Manager permanece **um único ator lógico**. | `[FATO]` DHR-EUA-E23 §2 item 2 |
| 2.6 | O "Scheduler" / "Cognitive Scheduler" citado em textos baselined anteriores (CEE-001 §9.3 e §10 S2; CONFLICT-MAP, Inversão #1) designa a função de despacho hoje exercida pelo Manager — não um componente à parte. | `[INFERÊNCIA]` ADR-MANAGER-001 §2.2 (único componente de orquestração) + DHR-EUA-E23 §1 (slot SPEC-008 antes chamado "Cognitive Scheduler") e §3 (renomeação do slot no ROADMAP §7); CONFLICT-MAP l.123 liga a Inversão #1 ao slot SPEC-008 *[antes: "(CEE-001 §10 S2; CONFLICT-MAP, Inversão #1)" e "DHR-EUA-E23 §3 (slot SPEC-008 renomeado de 'Cognitive Scheduler')" — o nome antigo está no §1 da ata, não no §3]* |

---

## 3. Três Fases, natureza e Spec dona

| Fase | Nome normativo (ADR §4.3) | Natureza (ADR §2.5) | O que faz (ADR §2.3) | Spec dona (DHR-EUA-E23 §2 item 1) | Classe predominante — **orientação, não vinculante; não herdável (§8.2-bis)** |
|---|---|---|---|---|---|
| **Fase 0** | Mission Lifecycle | Decisório leve | Monitora gatilhos de mercado / hipóteses de ciclos anteriores; decide tipo de missão (Exploratória ou Validação); cria e gerencia ciclo de vida e portfólio de missões; Campanhas; Plano B | **SPEC-015** — Manager — Missão & Ciclo de Vida | H/P |
| **Fase 1** | Dispatch | Mecânico/determinístico, "sem julgamento analítico" | Resolve o grafo de dependências; despacha agentes analíticos na ordem; monitora publicações no Blackboard | **SPEC-008** — Manager — Orquestração Mecânica (Fase 1 + serviços de tempo); dividida em SPEC-008 "Despacho e Ciclo" + **Spec de Tempo** (candidata SPEC-050) | D/C |
| **Fase 2** | Conviction | Cognitivo leve | Lê Vetores de Convicção; arbitra conflitos entre agentes; forma Convicção Global; gera o TMP (interno — ver §5) | **SPEC-014** (repurposado; absorve o Synthesis) — Manager — Convicção & Síntese | H/P |

- `[FATO]` Tabela composta de ADR-MANAGER-001 v1.0 §2.3/§2.5/§4.3 e DHR-EUA-E23 §2 item 1. A divisão da SPEC-008 é `[FATO]` DHR-SPEC008-001 §1, linha **P-2**.
- `[FATO]` "Classe predominante" é **orientação não-vinculante**; a declaração normativa de Classe é **por BASpec**, no Plan de cada Spec (DHR-EUA-E23 §2 item 1, nota *; RULE-MECH-01; CC-11).
- `[FATO]` Slots seguem **indicativos**: número, fronteira e decomposição final de cada Spec do Manager só se fixam **na abertura** dela (DHR-EUA-E23 §2 item 3; RULE-ECC-01/02). Este contrato não antecipa a abertura da SPEC-015 nem da SPEC-014 — o efeito vertical das decisões locais da abertura da SPEC-008 está declarado no §8.2-bis.

### 3.1 Fase 1 é mecânica

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 3.1.1 | A Fase 1 é **mecânica/determinística**: resolve grafo de dependências, sem julgamento analítico. | `[FATO]` ADR-MANAGER-001 §2.3 ("DISPATCH (mecânica/determinística)") e §2.5 |
| 3.1.2 | O controle de horário do Manager é determinístico (ENF-03); o gate da FSM do alarme **nunca** é LLM. (A FSM do **ciclo** é obrigação transversal às Fases — §3.2.) | `[FATO]` WORKFLOW v2.1: WF-K02, WF-A02 *[antes: "O controle de horário do Manager é determinístico (ENF-03); o gate da FSM do ciclo e o da FSM do alarme **nunca** são LLM." — âncora "WF-K02, WF-F02, WF-A02"; a FSM do ciclo atravessa a Fase 2 (R1-m03)]* |
| 3.1.3 | Na abertura homologada da SPEC-008: Classe **D** em tudo + **C** na trava constitutiva; **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus. **Alcance:** só SPEC-008 e, se A-2 = sim, Spec de Tempo (§8.2-bis). | `[FATO]` DHR-SPEC008-001 §1 (frase de abertura: respostas "confirmadas pela homologação da `ABERTURA.md` como está") e §4 (homologa a abertura); texto em ABERTURA.md §4 (não-baseline — ver cabeçalho) — a declaração por BASpec continua sendo do Plan *[antes: "`[FATO]` ABERTURA.md §4, homologada 'como está' (DHR-SPEC008-001 §1) — a declaração por BASpec continua sendo do Plan" (R1-M03)]* |
| 3.1.4 | Julgamento leve pertence às Fases 0 e 2, não à Fase 1. | `[FATO]` ADR-MANAGER-001 §2.5 (Fase 0 "Decisório leve", Fase 2 "Cognitivo leve", Fase 1 "sem julgamento analítico"); mesma leitura em ABERTURA.md §4 (não-baseline) *[antes: "`[FATO]` ADR-MANAGER-001 §2.5; ABERTURA.md §4"]* |

### 3.2 FSM do ciclo — obrigação **transversal** às Fases (R1-m03)

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 3.2.1 | "**FSM do ciclo inteiro** (determinística, auditável): `AGUARDANDO → CONTEXTO_FORMADO → ARMADO → ATIVADO → EM_SÍNTESE → EM_RISCO → {SINAL_ENVIADO \| RECUSADO \| EXPIRADO}`. O gate nunca é LLM (ENF-03)." | `[FATO]` WF-F02 (transcrição; a frase final do item, "implementação no Plan do Manager (SPEC-015)", **não** é herdada — §8.3) |
| 3.2.2 | O "gate nunca é LLM" vale para **todos os trechos** da FSM, qualquer que seja a Fase dona: Fase 1 (SPEC-008, até a entrada em `EM_SÍNTESE`), Fase 2 (SPEC-014, Classe predominante H/P, a partir de `EM_SÍNTESE`) e `EM_RISCO` (família RISK-SPEC). Na Fase 2, o julgamento leve pode **produzir** a decisão (ex.: enviar ao Risco; a saída por "não enviar" em `EM_SÍNTESE` não é seta escrita em WF-F02 — §3.2.3, P-12), mas a **transição de estado** que a registra passa por gate determinístico. | `[INFERÊNCIA]` WF-F02 ("ciclo **inteiro**") + divisão por trecho da CONF-1 (DHR-SPEC008-001 §1, linha CONF-1..5); ADR §2.5 (Fase 2 cognitivo leve) |
| 3.2.3 | Nenhuma Fase cria, renomeia ou remove estado ou transição da FSM; setas não escritas em WF-F02 só com decisão de Andraus. | `[FATO]` DHR-SPEC008-001 §4 ("nenhum estado/transição foi criado; só Andraus decide e edita"); WORKFLOW, regra de uso 1 e 3 |

---

## 4. Fronteiras entre as Fases (e com os vizinhos)

| Fronteira | O que passa | Quem é dono de cada lado | Etiqueta e âncora |
|---|---|---|---|
| **Fase 0 → Fase 1** | Pedido de ciclo com os campos de WF-01 (ativo, tipo de trading, TFs de WF-T01, Killzone, assistida/pré-programada — WF-K04) | Fase 0 (SPEC-015) **cria/decide/gerencia** missões; Fase 1 (SPEC-008) **executa** o ciclo de um pedido já definido. Até a SPEC-015 existir, o pedido vem de Andraus (WF-01). | `[FATO]` DHR-SPEC008-001 §1 (abertura homologada "como está") e §4; ADR §2.3 (Fase 0 cria missão; Fase 1 despacha); WF-01. Texto da fronteira: ABERTURA.md §2 S1 e tabela anti-dupla-posse (não-baseline) *[antes: "`[FATO]` ABERTURA.md §2 S1 e tabela anti-dupla-posse (homologada, DHR-SPEC008-001)" (R1-M03)]* |
| **Fase 1 → Fase 0 (depois de encerrar) — R1-m04** | Nada é pedido; só registro do encerramento | "Resetar o alarme" = **só encerrar**: o alarme termina "usado"/"vencido" e o ciclo termina registrado; a Fase 1 **não** abre ciclo novo. Tentar de novo é decisão de **quem pede ciclos** (Fase 0 ou Andraus). | `[FATO]` DHR-SPEC008-001 §1, linha **P-12** ("Só encerrar (opção C) … P-12.1 não se aplica") · que "quantas vezes tentar" vire requisito à SPEC-015 = `[PROPOSTA]` (texto da opção C em ABERTURA.md §13 P-12, não-baseline) — **não** é obrigação herdada pela SPEC-015 (§8.2-bis) |
| **Anti-paradoxo** | — | Missão **não** exige hipótese prévia como insumo único: quem formula hipótese são os agentes analíticos, depois do despacho. | `[FATO]` ADR-MANAGER-001 §1.2/§1.3 e §5 A1 |
| **Fase 1 → Fase 2** | Caso entregue à Fase 2 | Fronteira = estado `EM_SÍNTESE` de WF-F02. SPEC-008 conduz até a entrada em `EM_SÍNTESE`; a partir dele, SPEC-014; em `EM_RISCO`, família RISK-SPEC. | `[FATO]` DHR-SPEC008-001 §1, linha **CONF-1..5** ("Seguir as recomendações do Especificador"); texto da CONF-1 em ABERTURA.md §13 e §2 "Dono por transição de WF-F02" (não-baseline). Efeito sobre a SPEC-014: §8.2-bis *[antes: "`[FATO]` ABERTURA.md §2 ('Dono por transição de WF-F02'), CONF-1 aceita (DHR-SPEC008-001 §1)" (R1-M03)]* |
| **Fase 2 → Risco** | **TMP interno** | Fase 2 gera o TMP; o Agente de Risco (FASE RISK) decide se o sinal segue ao Bot Trade Finance. Fluxo **unidirecional**: o risco nunca retroalimenta a convicção. | `[FATO]` WORKFLOW WF-06, WF-07, WF-X03, WF-X05; INV-05 (atomic-spec v1.5, emendado por EUA-E19a) |
| **Manager × SPEC-003** | Invocação do mecanismo | SPEC-003/CCM-001 **calcula** o Conviction Vector; o Manager **invoca** — **2x por ciclo**: leitura macro na Fase 1 (estrutural+institucional) e global na Fase 2 (+operacional). Nenhuma Fase redefine o cálculo. | `[FATO]` WF-C01 (Q-A5, DHR-DEC-001); RULE-CF-010 (SPEC-003); DHR-EUA-E23 §2 item 4; DHR-ARQ-001 §2 |
| **Fase 2 × SPEC-016** | Objeto TMP | Contrato do objeto TMP (snapshot imutável, handoff interno) = SPEC-016. | `[FATO]` DHR-ARQ-002 §2 item 2 (tabela de destino) |
| **Manager × agentes analíticos** | Pedidos e publicações | Comunicação **só** via Blackboard; o Manager publica só no próprio espaço; **apenas coordena**, nunca analisa; avisos pelo Event Bus (camada fina; transporte ≠ fonte de verdade). | `[FATO]` RULE-BB-001/002/005; EVENT-BUS-001 FECHADA (DHR-SPEC005-002) |
| **Manager × Spec de Tempo** | Eventos de tempo e estados do alarme | Ator continua sendo o Manager; muda só o documento (abrir/fechar Killzone na Spec de Tempo). | `[FATO]` DHR-SPEC008-001 §1, linhas **P-2** e **CONF-1..5**; texto da CONF-5 e de T4 em ABERTURA.md §13 e §2 (não-baseline) *[antes: "`[FATO]` ABERTURA.md §2 T4 e CONF-5 aceita (DHR-SPEC008-001 §1)" (R1-M03)]* |

---

## 5. O Manager nunca executa ordem

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 5.1 | O SOT não executa ordem; produz um **Signal Package** para o Bot Trade Finance. O **TMP** é artefato **interno** de passagem entre a Síntese (= Manager — Fase 2) e o Risk Agent. | `[FATO]` INV-05 (atomic-spec v1.5, emenda EUA-E19a/DHR-EUA-E19a); AGENTS.md §6 item 9; DHR-ARQ-002 §2 item 3 |
| 5.2 | Toda saída decisional material declara que é **recomendação**, não execução, e sob qual autoridade. | `[FATO]` RULE-DEC-01 (lida sob INV-05 emendado quanto ao TMP e à topologia Synthesis/B-001 — §8.3 e §9 A-4 (e)) |
| 5.3 | O alarme-gatilho é gatilho de **análise**, nunca ordem. | `[FATO]` WF-A01 |
| 5.4 | Em missão pré-programada, o Manager roda o ciclo sozinho "até o Signal Package" e o deixa em **fila para revisão**; nunca executa. | `[FATO]` WF-K04 |
| 5.5 | Prevenção de overtrading e execução são do Bot Trade Finance, fora do SOT. | `[FATO]` WF-X04; INV-05 |
| 5.6 | Este contrato **não** atribui a montagem do Signal Package a nenhuma Fase. As fontes apontam em direções diferentes e nenhuma fixa o dono da montagem: (i) o **contrato** do Signal Package como objeto de fronteira externa passa à **RISK-SPEC-022** (FASE RISK); (ii) WF-06 diz que a Fase 2 "decide se envia, e monta o pacote de **risco-retorno**" — sem chamá-lo de Signal Package; (iii) WF-K04 diz que o Manager roda o ciclo "até o **Signal Package**" — o que inclui a etapa do Risco, sem dizer quem o monta; (iv) WF-07 dá ao Agente de Risco a decisão de enviar "o sinal ao Bot Trade Finance … com os dados de entrada"; (v) o canal de saída é da SPEC-005. Leitura mais provável: a Fase 2 entrega insumo (TMP / pacote de risco-retorno) e o objeto Signal Package nasce na fronteira governada pela FASE RISK — **não** fixada aqui; decisão na abertura da SPEC-014 / RISK-SPEC-022 ou por Andraus. | `[INFERÊNCIA]` ROADMAP l.247 (SPEC-016: "Deixa de ser o contrato de fronteira externa (esse papel passa a RISK-SPEC-022 — Signal Package)"); WF-06; WF-K04; WF-07; ROADMAP l.33 (SPEC-005: "canal de saída do Signal Package"); P-13 em ABERTURA.md §2/§13 lista "quem monta o Signal Package (SPEC-014)" só como **candidato** (não-baseline). Ver §9, A-4 (i). *[antes: "Este contrato **não** atribui a montagem do Signal Package a nenhuma Fase: as fontes lidas fixam o canal de saída (SPEC-005) e a decisão de envio (Agente de Risco, WF-07), não o dono da montagem." — âncora "WF-07; ROADMAP l.33 …; ABERTURA.md §2 tabela (P-13 …)"; sem ponderar ROADMAP l.247, WF-K04 e WF-06 (R1-m06)]* |

---

## 6. Custo × análise: o Manager não suprime execução por custo diante de evento estruturalmente relevante, e custo não entra na convicção

*[antes (título): "6. O Manager nunca corta análise por custo" — mais amplo que a Salvaguarda 2, que se limita a "quando houver evento estruturalmente relevante" (R1-m07)]*

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 6.1 | CEE-001 §10, Salvaguarda 2 (literal): "**O Scheduler nunca pode suprimir a execução de um agente por motivo de custo quando houver evento estruturalmente relevante.** Economia de tokens é subproduto de bom design de eventos, não de supressão de análise." Aplicação: vale para o Manager em qualquer Fase em que ele decida despachar ou não (ator único — §2). | `[FATO]` CEE-001 v2.0 §10 S2 (transcrição, RCN-001) · aplicação ao Manager nas três Fases = `[INFERÊNCIA]` de ADR §2.2 + §2.6 deste contrato *[antes: "Nunca suprimir a execução de um agente por motivo de custo quando houver evento estruturalmente relevante. Vale para o Manager em qualquer Fase em que ele decida despachar ou não (ator único — §2)." — paráfrase sem o sujeito literal "O Scheduler"]* |
| 6.2 | Ruptura de hipótese dominante ⇒ análise completa **independente do custo** (Inversão #1). A mecânica do gatilho é da SPEC-008. | `[FATO]` CONFLICT-MAP, "Inversões contextuais" #1 (HOMOLOGADO 2026-09-20); l.123 (mecânica na SPEC-008 = `[INFERÊNCIA]` do próprio CONFLICT-MAP) |
| 6.3 | Custo **nunca** entra no Conviction Vector (Convicção ≠ Score). | `[FATO]` INV-04; CEE-001 v2.0 §10 Salvaguarda 4 |
| 6.4 | CEE-001 §10, Salvaguarda 1 (literal): "**Nenhum agente pode reduzir sua própria classe de modelo autonomamente.** Mudança de roteamento segue o fluxo do §9, nunca uma otimização silenciosa do próprio componente." · Salvaguarda 5 (literal): "**Toda alteração de roteamento de modelo é reversível e versionada**, seguindo o pipeline do §9.2." | `[FATO]` CEE-001 v2.0 §10 S1 e S5 (transcrição, RCN-001; "agente" é termo do canon, não reescrito — CONST-01) |
| 6.4-a | O Manager, como despachante, também **não altera permanentemente** a classe de modelo de **outro** componente: mudança de roteamento exige o fluxo completo do §9.2 (proposta → auditoria → consenso de Andraus → registro), e "nenhum papel decide sozinho". A única ação de custo que o canon admite fora desse fluxo é a **pausa emergencial**: "Mudanças emergenciais de custo (ex: pico de gasto inesperado) podem pausar um componente via Scheduler (kill-switch operacional), mas **não podem alterar permanentemente sua classe de modelo** sem passar por este fluxo completo." | `[INFERÊNCIA]` CEE-001 v2.0 §9.2 e §9.3 (trecho final transcrito literal) + §2.6 deste contrato (Scheduler = função do Manager). A S1 sozinha **não** diz isso — fala só da **própria** classe do agente. Mesma leitura, para a Fase 1, em ABERTURA.md §2 S12 (não-baseline) |
| 6.5 | Ordem dos 4Es: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade; Economicidade nunca acima de Eficácia. | `[FATO]` AGENTS.md §6 item 11 (Q-009); CEE-001 v2.0 §12 |
| 6.6 | **Tensão no canon, registrada e não resolvida aqui (CONST-01):** a pausa emergencial do CEE §9.3 ("pausar um componente via Scheduler") pode, se aplicada durante evento estruturalmente relevante, suprimir execução por custo — o que a S2 proíbe. **Alcance da P-7:** na abertura da SPEC-008, Andraus aceitou a recomendação de que "o orçamento do ciclo **avisa e escala** quando estoura; **nunca** pula o Elliott (nem outra etapa com evento estrutural relevante) para economizar; o 'botão de parada por gasto' … só é apertado **por você** [Andraus], nunca automaticamente". Isso vale para a **SPEC-008** (orçamento do ciclo da Fase 1); estender a regra da pausa às Fases 0 e 2 **não** foi decidido. | `[FATO]` CEE-001 v2.0 §9.3 e §10 S2; DHR-SPEC008-001 §1, linha **P-4..P-9**; texto da P-7 em ABERTURA.md §13 (não-baseline; a nota técnica da P-7 já registrava "CEE-001 §10 S2 × §9.3 (tensão no canon …)") · extensão às Fases 0/2 = `[DECISÃO NECESSÁRIA]` (§9, A-5) |

*[antes (6.4): "| 6.4 | O Manager não reduz sozinho a classe de modelo de nenhum agente; mudança de roteamento é reversível e versionada. | `[FATO]` CEE-001 v2.0 §10 Salvaguardas 1 e 5 |" — sujeito da S1 alterado ("própria classe" → "de nenhum agente") com etiqueta [FATO] (R1-M01)]*

---

## 7. Invariantes constitucionais que valem para as três Fases (só referência — não copiados)

`[FATO]` atomic-spec v1.5 §INV e AGENTS.md §6: **INV-01** (hierarquia Elliott → Fibonacci → Fractal → SMC → ICT; posição de Fibonacci/Fractal no roteiro de despacho = "decidir depois", P-11 da DHR-SPEC008-001) · **INV-02** (ICT não cria hipótese; WF-D04 FECHADA) · AGENTS §6 item 2 (só Elliott cria a hipótese primária) · AGENTS §6 item 4 (`directional_conflict = true` ⇒ NEUTRO; WF-F01 ramo 2) · **INV-03** (8 dimensões; limiares-piloto interinos; definitivos = J-001 aberta) · **INV-04** · **INV-05** · **INV-07** · **INV-09** · **INV-10** · estados da hipótese = **CHM-001** (AGENTS §6 item 3) · CEE-001 v2.0 §11 (Salvaguardas de Sinal). O Manager **consome** esses invariantes; não os redefine (CONST-01; CC-02).

---

## 8. Pai de herança vertical (RULE-HV)

### 8.1 Filhas

| Filha | Relação | Etiqueta e âncora |
|---|---|---|
| **SPEC-008** — Despacho e Ciclo (Fase 1) | filha | `[FATO]` DHR-EUA-E23 §2 item 2; DHR-SPEC008-001 §1, linha **P-4..P-9** (escolhida a recomendação: o contrato, não o ADR, como pai); texto em ABERTURA.md §6 CC-08 ("Pai vertical = 'Manager Contract' (P-4) ou ADR-MANAGER-001 v1.0" — não-baseline) *[antes: "ABERTURA.md §6 CC-08 ('Pai vertical = \"Manager Contract\" (P-4)')" — citação truncada sem a alternativa "ou ADR-MANAGER-001 v1.0"]* |
| **SPEC-015** — Missão & Ciclo de Vida (Fase 0) | filha | `[FATO]` DHR-EUA-E23 §2 item 2 |
| **SPEC-014** — Convicção & Síntese (Fase 2) | filha | `[FATO]` DHR-EUA-E23 §2 item 2 |
| **Spec de Tempo** (candidata SPEC-050) | filha **proposta** | `[PROPOSTA]` — o ator é o Manager (texto de T4/CONF-5 em ABERTURA.md, não-baseline; DHR-SPEC008-001 §1 linhas P-2 e CONF-1..5), mas a DHR-EUA-E23 nomeia três filhas; incluir é decisão de Andraus (§9, ponto A-2) |

### 8.2 O que cada filha deve fazer (só as regras vigentes, aplicadas)

- `[FATO]` RULE-HV-01: declarar este contrato como pai por **ID + versão baseline** e **conservar o conjunto** das obrigações dos §2–§7, **no alcance declarado no §8.2-bis**.
- `[FATO]` RULE-HV-02 (extensão de RULE-HD-03): nenhuma obrigação daqui é suprimida fora de `REMOVED` com homologação de Andraus; supressão silenciosa = NÃO CONFORME Crítica.
- `[FATO]` RULE-HV-03 (extensão de RULE-HD-02): requisito local da filha não contradiz o pai; precedência pai > filha.
- `[FATO]` RULE-HV-04: o Revisor audita a cobertura **como conjunto**. `[PROPOSTA]` Para isso, cada filha cita os itens deste contrato pelo número de seção/linha (ex.: "MC §6 item 6.1"); os números são **índice de leitura**, não IDs normativos novos.
- `[FATO]` RULE-HD-04: a filha referencia por ID + versão; não copia o conteúdo.

### 8.2-bis Alcance vertical de cada item (R1-m08)

As decisões tomadas **na abertura da SPEC-008** (DHR-SPEC008-001) são decisões locais de uma filha. Promovê-las ao pai sem declarar o alcance as tornaria obrigação das SPEC-014/015 antes da abertura delas, contra DHR-EUA-E23 §2 item 3 ("número, fronteira e decomposição final … só se fixam **na abertura**"; "a decomposição pode ainda ser revista … na abertura, com justificativa homologada"). Por isso:

| Item(ns) | Origem | Alcance vertical | Etiqueta |
|---|---|---|---|
| §2, §3 (tabela, exceto a coluna "Classe predominante"), §3.1.1, §3.1.2, §3.1.4, §3.2, §4 (linhas Anti-paradoxo, Fase 2 → Risco, Manager × SPEC-003, Fase 2 × SPEC-016, Manager × agentes analíticos), §5.1–§5.5, §6.1–§6.5, §7 | ADR, DHR-ARQ-001/002, DHR-EUA-E23, CEE-001, INV, RULE-*, WORKFLOW | **todas as filhas** (conservação-como-conjunto, RULE-HV-01) | etiqueta própria de cada linha (`[FATO]` ou `[INFERÊNCIA]` — §2.6, §3.2.2, aplicação do 6.1 e 6.4-a são `[INFERÊNCIA]`); alcance = RULE-HV-01 |
| Coluna "Classe predominante" (§3) | DHR-EUA-E23 §2 item 1, nota * | **nenhuma** — orientação não-vinculante, não entra na conservação | `[FATO]` DHR-EUA-E23 §2 item 1, nota * |
| §3.1.3 (Classe D/C da Fase 1) · §6.6 (P-7) | DHR-SPEC008-001 §1 (abertura "como está"; P-4..P-9) | **SPEC-008 e Spec de Tempo** (esta, se A-2 = sim). Para SPEC-014/015: só o limite que já decorre do ADR §2.5 (não levar julgamento para a Fase 1), não as Classes de suas próprias BASpecs | `[INFERÊNCIA]` DHR-EUA-E23 §2 item 3 + DHR-SPEC008-001 §4 ("homologa a **abertura**" da SPEC-008) |
| §4 Fase 0 → Fase 1 · Fase 1 → Fase 0 (P-12) · Fase 1 → Fase 2 (CONF-1) · Manager × Spec de Tempo (CONF-5) | DHR-SPEC008-001 §1 (abertura; P-2, P-12, CONF-1..5) | **SPEC-008/Spec de Tempo** (esta, se A-2 = sim): obrigação. **SPEC-014/015**: fronteira **vigente** do lado da SPEC-008, que a abertura delas parte de; mudá-la na abertura delas é revisão de decomposição com homologação de Andraus (DHR-EUA-E23 §2 item 3), não supressão silenciosa | `[INFERÊNCIA]` DHR-EUA-E23 §2 item 3 · se Andraus quer que essas fronteiras sejam herança fixa das SPEC-014/015 = `[DECISÃO NECESSÁRIA]` (§9, A-5) |
| "Quantas vezes tentar" como requisito à SPEC-015 (§4, P-12) | texto da opção C (ABERTURA.md §13, não-baseline) | **nenhuma** — `[PROPOSTA]` à abertura da SPEC-015 | `[PROPOSTA]` |

### 8.3 Bloco Herança/Delta deste próprio contrato (CC-08)

```
INHERITS : ADR-MANAGER-001 v1.0 (§1.2–1.3, §2.1–2.3, §2.5, §4.3, §5)
             — NÃO herdado: §2.4 (fluxo "TMP → Bot Trade Finance") → prevalece INV-05
               (atomic-spec v1.5, emenda EUA-E19a/DHR-EUA-E19a 2026-09-22), reafirmado por
               DHR-ARQ-002 (2026-10-01, posterior ao ADR) §2 item 3: "O TMP permanece artefato
               interno (EUA-E19a); o Signal Package segue sendo o artefato de fronteira"
             — NÃO herdados (citados só como divergência, §9 A-4): §3.3, §4.1, §4.2, §6, §7
           DHR-ARQ-001 (2026-10-01) · DHR-ARQ-002 (2026-10-01) · DHR-EUA-E23 (2026-10-01) §1, §2
           DHR-EUA-E19a (2026-09-22) — via INV-05
           DHR-SPEC008-001 (2026-11-07) §1 (linhas P-2, P-4..P-9, P-11, P-12, P-13, CONF-1..5),
             §3, §4, §5 — alcance vertical conforme §8.2-bis
           DHR-DEC-001 (2026-10-01) — Q-A5 (via WF-C01)
           DHR-SPEC005-002 (2026-10-05) — EVENT-BUS-001 FECHADA
           CEE-001 v2.0 §9.2, §9.3, §10 (S1, S2, S4, S5), §11, §12
           CHM-001 (BASELINED, Q-001; arquivo consolidado sem número de versão) — estados da hipótese
           atomic-spec v1.5 INV-01..INV-05, INV-07, INV-09, INV-10 · RULE-DEC-01 · RULE-BB-001/002/005
           RULE-HV-01..04 (SPEC-019 v1.0) · RULE-HD-02..04 · RULE-MECH-01 · RULE-ECC-01/02
           RULE-CF-010 (SPEC-003 v1.5, BASELINE) · CONFLICT-MAP "Inversões contextuais" #1 (homologado 2026-09-20)
           AGENTS.md §6 (itens 2, 3, 4, 9, 11 — Questionário v1, 2026-09-14)
           WORKFLOW v2.1: regras de uso 1 e 3, WF-01, WF-04, WF-06, WF-07, WF-C01, WF-T01, WF-K02, WF-K04, WF-A01,
             WF-A02, WF-F01, WF-F02, WF-X03, WF-X04, WF-X05, WF-D04
             — WF-F02: NÃO herdada a frase "implementação no Plan do Manager (SPEC-015)" → prevalece
               CONF-1 (DHR-SPEC008-001 §1, linha CONF-1..5: dono por trecho), até Andraus corrigir o texto
             — WF-K02: NÃO herdado o parêntese "(SPEC-008/015)" → prevalece CONF-5 (DHR-SPEC008-001 §1,
               linha CONF-1..5: regra na Spec de Tempo; ator = Manager), até Andraus corrigir o texto
             — WF-F01 ramos 3 e 5: NÃO herdado "reset" → prevalece P-12 (DHR-SPEC008-001 §1: "Só encerrar")
CONTEXTO (citado, NÃO herdado — RULE-HD-04):
           ABERTURA.md da SPEC-008 (redação homologada 2026-11-07; não-baseline; sem versão — cabeçalho)
           ROADMAP.md (l.33, l.35, l.36, l.247, §7, §10-bis — estado, não baseline versionado) · GLOSSARIO (Fase; §1-bis)
           WORKFLOW WF-02, WF-03, WF-05 (só para o vocabulário do §1-bis)
ADDED    : nenhum requisito novo. Só a regra de leitura do §1 e o uso de números de seção como índice (§8.2) — ambos [PROPOSTA]. Filiação da Spec de Tempo (§8.1) = [PROPOSTA], pendente de A-2. "Quantas vezes tentar" como requisito à SPEC-015 (§4/§8.2-bis) = [PROPOSTA], transcrita da opção C da P-12.
MODIFIED : nenhum
REMOVED  : nenhum
```

*[antes (INHERITS): "ADR-MANAGER-001 v1.0 (§1.2–1.3, §2.1–2.5, §4.3, §5) / DHR-ARQ-001 (2026-10-01) · DHR-ARQ-002 (2026-10-01) · DHR-EUA-E23 (2026-10-01) §2 / DHR-SPEC008-001 (2026-11-07) §1 — só o que fixa fronteira (P-2, CONF-1, CONF-5) e a abertura homologada (ABERTURA.md §2, §4) / CEE-001 v2.0 §10 (S1, S2, S4, S5), §11, §12 / atomic-spec v1.5 INV-01..INV-05, INV-07, INV-09, INV-10 · RULE-DEC-01 · RULE-BB-001/002/005 / RULE-HV-01..04 (SPEC-019 v1.0) · RULE-HD-02..04 / RULE-CF-010 (SPEC-003, BASELINE) · CONFLICT-MAP 'Inversões contextuais' #1 (homologado 2026-09-20) / WORKFLOW v2.1: WF-01, WF-04, WF-06, WF-07, WF-C01, WF-K02, WF-K04, WF-A01, WF-A02, WF-F02, WF-X03, WF-X04, WF-X05, WF-D04" — herdava ADR §2.4, WF-F02 e WF-K02 inteiros (R1-M02), herdava de ABERTURA.md sem versão baseline (R1-M03) e não cobria WF-F01, WF-T01, DHR-SPEC005-002, DHR-DEC-001, CHM-001, AGENTS §6 (R1-m05)]*
*[antes (ADDED, após a classe M do Orquestrador): "nenhum requisito novo. Só a regra de leitura do §1 e o uso de números de seção como índice (§8.2) — ambos [PROPOSTA]. Filiação da Spec de Tempo (§8.1) = [PROPOSTA], pendente de A-2."]*

---

## 9. Pontos que dependem de Andraus

| # | Ponto | Recomendação do Especificador | Etiqueta |
|---|---|---|---|
| **A-1** | **ID e versão** do contrato ao homologar (RULE-HV-01 exige "ID+VERSÃO baseline"; hoje o documento só tem nome). Mesmo ponto para a **redação de `ABERTURA.md`** citada como contexto: ela não tem versão nem é baseline (cabeçalho). | Dar um ID curto e versão 1.0 na homologação; o Especificador **não** inventa o ID. Para a ABERTURA, basta o Orquestrador fixar o hash do commit homologado no registro; dar-lhe versão é opcional, porque aqui ela só é contexto. | `[DECISÃO NECESSÁRIA]` |
| **A-2** | A **Spec de Tempo** (candidata SPEC-050) também herda deste contrato? | Sim — o ator dela é o Manager (T4/CONF-5); sem isso, a parte de tempo da Fase 1 ficaria fora da herança. | `[DECISÃO NECESSÁRIA]` |
| **A-3** | **Lugar do arquivo** depois de homologado: hoje em `specs/features/SPEC-008/`, mas é pai de três Specs. | Mover para `governance/` (ou onde Andraus indicar) na homologação, com registro no CATALOGO; o Especificador não move. | `[DECISÃO NECESSÁRIA]` |
| **A-4** | **Divergências de texto já conhecidas** (não resolvidas aqui; nenhuma fonte foi editada; o §8.3 declara qual texto prevalece em cada uma): (a) ADR §2.4 (v1.0, 2026-09-26) desenha "TMP → Bot Trade Finance" e não cita a emenda EUA-E19a (2026-09-22) — prevalece INV-05, reafirmado por DHR-ARQ-002 §2 item 3 (2026-10-01); (b) ADR §3.3/§4.2 (anteriores à DHR-EUA-E23) e WF-F02 (não editado depois da CONF-1 — DHR-SPEC008-001 §4) apontam a SPEC-015 como Spec do Manager inteiro / da FSM — prevalece a divisão em três (DHR-EUA-E23 §2 item 1) e a CONF-1; (c) WF-K02 nomeia "SPEC-008/015" como dona do abrir/fechar Killzone — prevalece a CONF-5; (d) ADR §4.1 ("Event Bus = decisão aberta"), §6 (GOV-007 "Event Bus pendente") e §7 (EVENT-BUS-001 "Aberta") — hoje FECHADA (DHR-SPEC005-002); (e) RULE-DEC-01 (EUA-E13, anterior à EUA-E19a e às DHR-ARQ-001/002) fala em "recomendação/orientação decisional (TMP)" e "topologia Synthesis/B-001" — lida sob INV-05 emendado (TMP interno; Signal Package na fronteira), DHR-ARQ-002 (Synthesis = Manager Fase 2) e DHR-ARQ-001 (B-001 supersedida na parte "componente separado"); (f) ADR §7 põe J-001 como "Aberta (SPEC-015)" — hoje J-001 é matéria de backtest/calibração com dona a definir (ROADMAP l.35, BL-032); este contrato não atribui J-001 a nenhuma Fase; (g) WF-F01 ramos 3 e 5 dizem "reset do alarme"/"reset" — a P-12 decidiu "só encerrar" (DHR-SPEC008-001 §1) e o WORKFLOW não foi editado (§4 da ata); (h) WF-02/WF-03 chamam de "Fase 1" o trabalho dos agentes analíticos — homônimo tratado no §1-bis, sem editar a fonte; (i) dono da **montagem** do Signal Package: WF-06 ("monta o pacote de risco-retorno"), WF-K04 ("até o Signal Package") e ROADMAP l.247 (contrato → RISK-SPEC-022) não fixam o mesmo dono — §5.6. | Registrar como leitura (`[INFERÊNCIA]`); correção do texto do ADR/WORKFLOW/RULES, se desejada, só por Andraus. A camada de disciplinas cognitivas do Manager (ADR §3.3: "suas camadas serão especificadas na SPEC-015") fica sob **SPEC-015-SCOPE**, aberta. O ponto (i) vai à abertura da SPEC-014 / RISK-SPEC-022. | `[DECISÃO NECESSÁRIA]` (só se Andraus quiser corrigir as fontes; (i) também quanto ao dono) |
| **A-5** — novo (R1-m07/m08) | **Efeito vertical das decisões locais da abertura da SPEC-008** sobre a SPEC-014 e a SPEC-015: (1) as fronteiras CONF-1 (`EM_SÍNTESE`), P-12 (Fase 1 não abre ciclo) e CONF-5 viram herança **fixa** delas, ou ficam como fronteira **vigente** revisável na abertura delas (como propõe o §8.2-bis)? (2) a regra da P-7 (pausa por gasto só por Andraus, nunca automática) se estende às Fases 0 e 2? | (1) Fronteira vigente, revisável só com homologação na abertura delas — respeita DHR-EUA-E23 §2 item 3. (2) Estender, porque a pausa emergencial do CEE §9.3 é ação do "Scheduler" (= Manager, §2.6) em qualquer Fase; mas a extensão é decisão sua, não do contrato. | `[DECISÃO NECESSÁRIA]` |

*[antes (A-4): "**Divergências de texto já conhecidas** (não resolvidas aqui; nenhuma fonte foi editada): (a) ADR §2.4 desenha 'TMP → Bot Trade Finance', anterior à EUA-E19a (TMP interno; Signal Package na fronteira) — lido sob INV-05 emendado; (b) ADR §3.3/§4.2 e WF-F02 apontam a SPEC-015 como Spec do Manager inteiro / da FSM, anteriores à divisão em três (DHR-EUA-E23) e à CONF-1; (c) WF-K02 nomeia 'SPEC-008/015' como dona do abrir/fechar Killzone, diferente da CONF-5; (d) ADR §7 lista EVENT-BUS-001 como aberta — hoje FECHADA (DHR-SPEC005-002)." — (a) dizia "anterior à EUA-E19a", mas o ADR é de 2026-09-26 e a EUA-E19a de 2026-09-22; omitia RULE-DEC-01, ADR §7 J-001, ADR §4.1/§6, WF-F01 "reset" (R1-m04)]*
*[antes (A-2, recomendação): "Sim — o ator dela é o Manager (ABERTURA.md §2 T4); …"]*

---

## 10. Decisões abertas que este contrato toca e **não** fecha (CONS-01)

- `[FATO]` DHR-SPEC008-001 §5 ("Permanecem ABERTAS"): **J-001** · **G-001** · **K-001** · **C-001** · **M-001** · **N-001** · **SPEC-015-SCOPE** · **SPEC-045-RUNTIME-001** · **ECC-03-001** · **WF-D03** · **D-PCC-4**. A linha "Decisões abertas ativas" do ROADMAP (l.36) traz J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001 e WORKFLOW-SOT-001 residual (= WF-D03).
- `[FATO]` DHR-SPEC008-001 §3 (ii): "**J-001/N-001** abertas — o limiar de contexto 'conclusivo' fica como parâmetro a preencher, sem número inventado" (Fase 1).
- `[FATO]` INV-03: "limiares de Fase Piloto (≥70%, 7/9) = FATO NORMATIVO interino, recalibrável após backtest (Q-002); fórmula/pesos/limiares **definitivos** = J-001 em aberto". CEE-001 v2.0 §11 S2 (score < 7/9 → bloqueado) e S4 (convicção global < 70% → sem sinal COMPRA/VENDA) são "invioláveis".
- `[INFERÊNCIA]` A decisão de envio da Fase 2 (WF-06: "decide se envia"; WF-C01: leitura global "→ decide o envio") **não** é parâmetro vazio: enquanto J-001 estiver aberta, todo sinal está sujeito aos limiares-piloto interinos acima (INV-03; CEE §11 S2/S4). **Quem** os aplica no fluxo (Fase 2, FASE RISK ou ambos) não é fixado aqui — é da abertura da SPEC-014 / FASE RISK.
- `[FATO]` Também seguem "decidir depois" (DHR-SPEC008-001 §1): **P-11** (Fibonacci/Fractal no roteiro) e **P-13** (reentrada após stop). Nenhuma aparece aqui como fechada.

*[antes: "`[FATO]` DHR-SPEC008-001 §5 e ROADMAP 'Decisões abertas ativas': **J-001** (fórmula/pesos/limiares definitivos — limiar 'conclusivo' da Fase 1 e decisão de envio da Fase 2 ficam como parâmetro) · **N-001** (pesos por ativo) · **WF-D03** (resíduo J-001) · **G-001** (persistência do estado do ciclo — SPEC-009) · **M-001** (estados não-hipótese no quadro) · **SPEC-015-SCOPE** (fronteira e escopo da Fase 0) · **C-001** · **K-001** · **SPEC-045-RUNTIME-001** · **ECC-03-001** · **D-PCC-4**. Também seguem 'decidir depois': P-11 (Fibonacci/Fractal no roteiro) e P-13 (reentrada após stop). Nenhuma aparece aqui como fechada." — a ata não diz que a decisão de envio da Fase 2 fica como parâmetro, e os limiares-piloto interinos foram omitidos (R1-M04)]*

---

## 11. Autopré-check (resumido)

- [x] Lidos: ROADMAP.md (linhas de estado/decisões, l.33–37, l.239–247), atomic-spec.md (INV, CC-08), DHR-SPEC008-001 (inteira), ABERTURA.md (§2, §4, §6, §13 inteira), ADR-MANAGER-001 (§1–§7), DHR-EUA-E23 (§1–§3), DHR-ARQ-001, DHR-ARQ-002 (§2), WORKFLOW.md v2.1 (citado só por ID), CEE-001 §9–§12 (literal), CONFLICT-MAP (Inversões), RULES.md (RULE-HV, RULE-HD, RULE-BB, RULE-DEC-01), GLOSSARIO (Fases; §1-bis).
- [x] R1: S1, S2 e S5 transcritas literalmente; regra sobre outros componentes só como `[INFERÊNCIA]` ancorada em CEE §9.2/§9.3 (M-01).
- [x] R1: INHERITS sem fonte divergente sem precedência — ADR §2.4, frase final de WF-F02, parêntese de WF-K02 e "reset" de WF-F01 excluídos com o texto que prevalece citado (M-02); nenhuma regra nova.
- [x] R1: ABERTURA.md fora do INHERITS; decisões ancoradas nas linhas da ata DHR-SPEC008-001 §1; ABERTURA declarada não-baseline (M-03).
- [x] R1: §10 sem atribuição falsa à ata; limiares-piloto interinos (INV-03) citados (M-04).
- [x] Sem regra, campo, estado, transição ou agente de trading novos; ADDED só com itens de leitura/filiação/requisito marcados `[PROPOSTA]`.
- [x] Nenhuma decisão aberta fechada (§10); P-11/P-13 mantidas "decidir depois"; A-1..A-5 `[DECISÃO NECESSÁRIA]`.
- [x] Nenhum modelo canônico redefinido (CONST-01/CC-02); WORKFLOW, ADR, ROADMAP, AGENTS, RULES, canon e governance **não** editados.
- [x] Toda linha com etiqueta e âncora; `[INFERÊNCIA]` separada de `[FATO]`; documentado ≠ homologado (este arquivo é PROPOSTA).
- [x] Classe M do Orquestrador (m-01a/b/c, m-05a) preservada.
- [ ] Pesquisa web: **não feita** — documento de consolidação interna, sem prática externa adotada; o Dossiê da SPEC-008 (`research.md`) segue sendo a base de pesquisa.
- [ ] Gates mecânicos: ver §12.

## 12. O que NÃO foi verificado

- **Nenhum script foi executado** (o Especificador não tem Bash): `build_map.py`, `check_refs.py`, `check_doc_sync.py`, `pre_entrega.py`, `validate_spec_sot.py` (este último não se aplica — não é `plan.md`). O Orquestrador deve rodar ao menos `python scripts/build_map.py --check` e `python scripts/check_refs.py`.
- Hash do commit da redação homologada de `ABERTURA.md` **não fixado** (sem Bash) — A-1.
- Não li por inteiro: `atomic-spec.md`, `ROADMAP.md`, `research.md`, CHM-001, CEM-001, GLOSSARIO, EUA-E19a (só data e as linhas que citam TMP/Signal Package), SPEC-003/004/005/016 (só as referências usadas), CONFLICT-MAP (só Inversões).
- Não conferi se `backlog_triggers.py --abertura` lista algo novo para este documento (não é abertura de Spec).
- A afirmação de que a Spec de Tempo usa o Manager como ator vem do texto de T4/CONF-5 da ABERTURA (não-baseline); a nomeação "SPEC-050" segue **candidata**.
- Números de linha citados (ROADMAP l.33, l.35, l.36, l.247; CONFLICT-MAP l.123) valem para a leitura de 2026-11-07; o WORKFLOW é citado só por ID.
- O chat de Andraus não está no repositório; as decisões valem pela ata.

---

## 13. Resposta ao parecer R1 (2026-11-07) — rodada R1→R2

Parecer: `governance/propostas/SPEC-008/PARECER-REVISOR-MANAGER-CONTRACT-R1-2026-11-07.md` (NÃO CONFORME). Classe M (m-01a/b/c, m-05a) aplicada pelo Orquestrador e **não** desfeita. Texto anterior de cada trecho alterado preservado em `[antes: …]` no próprio lugar (INV-07).

| Achado | Sev. | O que mudou | Onde |
|---|---|---|---|
| **M-01** S1 com sujeito alterado como [FATO] | Média | S1 e S5 transcritas literalmente (e S2, pela mesma razão, no 6.1); a regra sobre a classe de **outros** componentes virou o item 6.4-a `[INFERÊNCIA]`, ancorado em CEE §9.2/§9.3, com a pausa emergencial transcrita | §6 (6.1, 6.4, 6.4-a) |
| **M-02** INHERITS herdava textos divergentes | Média | ADR §2.4 excluído do INHERITS (prevalece INV-05 + DHR-ARQ-002 §2 item 3, posterior ao ADR); WF-F02 sem a frase "implementação no Plan do Manager (SPEC-015)" (prevalece CONF-1); WF-K02 sem "(SPEC-008/015)" (prevalece CONF-5); WF-F01 sem "reset" (prevalece P-12); regra de leitura do §1 ganha a exceção correspondente. Nenhuma regra nova: só se diz qual decisão homologada, já existente, vale no trecho. Corrigido também o erro de data do A-4 (a): o ADR (2026-09-26) é **posterior** à EUA-E19a (2026-09-22), não anterior | §1, §8.3, §9 A-4 |
| **M-03** herança de ABERTURA.md sem versão baseline | Média | ABERTURA.md saiu do INHERITS e foi para "CONTEXTO (não herdado)"; cada decisão é ancorada na linha da ata DHR-SPEC008-001 §1 (P-2, P-4..P-9, P-12, CONF-1..5); cabeçalho declara a redação de 2026-11-07 não-baseline, sem versão e sem hash fixado; versão formal → A-1 | cabeçalho, §3, §3.1.3, §3.1.4, §4, §8.1, §8.3, §9 A-1 |
| **M-04** §10 atribuía à ata o que ela não diz | Média | Frase removida; §10 reescrito: lista literal da ata §5, condição §3 (ii) da ata (só o limiar "conclusivo" da Fase 1), INV-03 e CEE §11 S2/S4 citados; a sujeição da decisão de envio aos limiares-piloto ficou como `[INFERÊNCIA]`, sem fixar quem os aplica | §10 |
| m-01 "agente" sem qualificador | Menor | Classe M do Orquestrador, mantida; trechos novos usam "agente de trading"/"agentes analíticos"/"componente"; "agente" só dentro de transcrição literal do canon | cabeçalho, §2, §6.4 |
| **m-02** homônimo "Fase" | Menor | Nova seção §1-bis com as três acepções (Fase do Manager; "Fase" do pipeline WF-02..06; FASE do ROADMAP) e convenção de escrita | §1-bis; A-4 (h) |
| **m-03** FSM do ciclo sob "Fase 1" | Menor | FSM do alarme ficou no 3.1.2; FSM do ciclo virou obrigação transversal no novo §3.2 (gate nunca LLM em todos os trechos, inclusive Fase 2/H-P e `EM_RISCO`) | §3.1.2, §3.2 |
| **m-04** A-4 incompleto; fronteira P-12 C ausente | Menor | A-4 ganhou (d) ampliado (ADR §4.1/§6), (e) RULE-DEC-01, (f) ADR §7 J-001, (g) WF-F01 "reset" × P-12, (h) homônimo "Fase", (i) montagem do Signal Package; §4 ganhou a linha "Fase 1 → Fase 0 (depois de encerrar)" com a P-12 opção C | §4, §9 A-4 |
| **m-05** INHERITS × fontes do corpo; ADDED × [PROPOSTA] | Menor | INHERITS passou a cobrir WF-F01, WF-T01, DHR-SPEC005-002, DHR-DEC-001, DHR-EUA-E19a, CHM-001, AGENTS §6, CEE §9.2/§9.3, RULE-MECH-01, RULE-ECC-01/02; fontes só de contexto (ABERTURA, ROADMAP, GLOSSARIO, WF-02/03/05) listadas à parte; ADDED (com a parte de classe M do Orquestrador mantida) ganhou o `[PROPOSTA]` novo do §4/§8.2-bis | §8.3 |
| **m-06** §5.6 sem ponderar ROADMAP l.247, WF-K04, WF-06 | Menor | §5.6 reescrito pesando as cinco fontes; conclusão continua "não fixado aqui", com a leitura mais provável declarada como `[INFERÊNCIA]` e o ponto levado ao A-4 (i) | §5.6, §9 A-4 (i) |
| **m-07** §6 sem a tensão §9.3 × S2 e o alcance de P-7; título largo | Menor | Título do §6 restrito ao que S2/S4 dizem; novo 6.6 registra a tensão (sem reescrever o canon) e o alcance da P-7 (SPEC-008); extensão às Fases 0/2 → A-5 | §6 (título, 6.6), §9 A-5 |
| **m-08** decisões locais viram herança das SPEC-014/015 | Menor | Novo §8.2-bis declara o alcance vertical de cada item: Classe orientativa não herdável; §3.1.3 e P-7 só SPEC-008/Spec de Tempo; fronteiras CONF-1/CONF-5/P-12 = fronteira vigente revisável na abertura das irmãs (DHR-EUA-E23 §2 item 3); a escolha final é A-5 | §3, §3.1.3, §8.2, §8.2-bis, §9 A-5 |

**Outros ajustes da rodada** (não pedidos, descobertos ao reabrir as fontes): §2.6 — o nome antigo "Cognitive Scheduler" está no §1 da DHR-EUA-E23, não no §3; §8.1 — a citação do CC-08 da ABERTURA estava truncada (faltava "ou ADR-MANAGER-001 v1.0"); versão passa a v0.2 (proposta).

**Pendências para Andraus:** A-1..A-5, todas `[DECISÃO NECESSÁRIA]`. Nenhuma decisão aberta foi fechada (CONS-01).

Pronto para revisão.
