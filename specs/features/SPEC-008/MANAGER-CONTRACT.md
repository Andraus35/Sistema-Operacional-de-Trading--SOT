# Manager Contract — contrato comum do Manager Agent (Fases 0, 1 e 2)

> **PROPOSTA — não é baseline; só vigora com homologação de Andraus.** (INV-09)

| Campo | Valor |
|---|---|
| Versão | v0.1 (proposta) — ID definitivo e versão de baseline = decisão de Andraus (ver §9, ponto A-1) |
| Data | 2026-11-07 |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Origem | P-4 da abertura da SPEC-008 (`specs/features/SPEC-008/ABERTURA.md` §13), recomendação aceita por Andraus (`governance/DHR-SPEC008-001_Ata_Homologacao_Abertura_SPEC-008.md` §1, linha P-4..P-9; §3: "antes, o Manager Contract curto (P-4, recomendação) para homologação conjunta"); ordem de Andraus em chat, 2026-11-07: "Manager Contract primeiro" (via Orquestrador) |
| Instituído como direção por | `governance/DHR-EUA-E23_Ata_Homologacao_Manager_Unificado.md` §2 item 2 |
| Natureza | Documento de **consolidação**. Só junta o que Andraus já decidiu sobre o Manager. **Não** cria regra, campo, estado, transição, ID normativo nem agente. **Não** fecha decisão aberta (CONS-01). **Não** edita `WORKFLOW.md`, `ROADMAP.md`, `AGENTS.md`, `canon/` nem `governance/`. |
| Etiquetas | `[FATO]` = texto de documento homologado, com âncora · `[INFERÊNCIA]` = leitura derivada, com âncora · `[PROPOSTA]` = requer homologação · `[DECISÃO NECESSÁRIA]` = só Andraus |

---

## 1. Para que serve (em uma frase)

O Manager é **um só ator** que trabalha em **três Fases**; este contrato reúne num lugar só o que vale para as três, para que as três Specs do Manager (SPEC-015, SPEC-008, SPEC-014) herdem as mesmas obrigações e não se contradigam. `[FATO]` DHR-EUA-E23 §2 item 2: o contrato "garante o **ator único** (ADR §2.2) e disciplina as fronteiras Fase 0↔Fase 1↔Fase 2 (evitando reintroduzir o paradoxo circular que o ADR resolveu)".

**Regra de leitura** `[PROPOSTA]`: este documento não tem autoridade própria sobre as fontes que junta. Se algum item daqui divergir do texto-fonte citado, vale o texto-fonte e a divergência é achado a corrigir aqui (consequência de RULE-HD-02/RULE-HV-03 — o herdado prevalece sobre o local).

---

## 2. Ator único

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 2.1 | O Manager Agent é o **único componente de orquestração** do SOT. | `[FATO]` ADR-MANAGER-001 v1.0 §2.2 |
| 2.2 | O Manager **não é agente analítico**: não analisa mercado, não formula hipóteses de mercado, não possui skills de análise técnica. Seus domínios são gestão de missões, orquestração de despacho e síntese de convicções. | `[FATO]` ADR-MANAGER-001 v1.0 §2.2 e §2.5 ("FATO NORMATIVO") |
| 2.3 | Master Orchestrator, Mission Engine, Decision Orchestrator, Orchestration Layer, Agente Decisor e Agente de Síntese **não** aparecem em Spec futura como componente independente; foram absorvidos pelo Manager. | `[FATO]` ADR-MANAGER-001 v1.0 §2.1 ("FATO NORMATIVO"); DHR-ARQ-002 §2 item 1 (Synthesis Agent = Fase 2) |
| 2.4 | "Conviction Engine" é rótulo de **mecanismo** (CCM-001, SPEC-003) **invocado** pelo Manager — Fase 2; não é agente nem componente separado. | `[FATO]` DHR-ARQ-001 §2 itens 1 e 3 |
| 2.5 | As três Specs do Manager **não** criam agente adicional; o Manager permanece **um único ator lógico**. | `[FATO]` DHR-EUA-E23 §2 item 2 |
| 2.6 | O "Scheduler" / "Cognitive Scheduler" citado em textos baselined anteriores (CEE-001 §10 S2; CONFLICT-MAP, Inversão #1) designa a função de despacho hoje exercida pelo Manager — não um componente à parte. | `[INFERÊNCIA]` ADR-MANAGER-001 §2.2 (único componente de orquestração) + DHR-EUA-E23 §3 (slot SPEC-008 renomeado de "Cognitive Scheduler"); CONFLICT-MAP l.123 liga a Inversão #1 ao slot SPEC-008 |

---

## 3. Três Fases, natureza e Spec dona

| Fase | Nome normativo (ADR §4.3) | Natureza (ADR §2.5) | O que faz (ADR §2.3) | Spec dona (DHR-EUA-E23 §2 item 1) | Classe predominante — **orientação, não vinculante** |
|---|---|---|---|---|---|
| **Fase 0** | Mission Lifecycle | Decisório leve | Monitora gatilhos de mercado / hipóteses de ciclos anteriores; decide tipo de missão (Exploratória ou Validação); cria e gerencia ciclo de vida e portfólio de missões; Campanhas; Plano B | **SPEC-015** — Manager — Missão & Ciclo de Vida | H/P |
| **Fase 1** | Dispatch | Mecânico/determinístico, "sem julgamento analítico" | Resolve o grafo de dependências; despacha agentes analíticos na ordem; monitora publicações no Blackboard | **SPEC-008** — Manager — Orquestração Mecânica (Fase 1 + serviços de tempo); dividida em SPEC-008 "Despacho e Ciclo" + **Spec de Tempo** (candidata SPEC-050) | D/C |
| **Fase 2** | Conviction | Cognitivo leve | Lê Vetores de Convicção; arbitra conflitos entre agentes; forma Convicção Global; gera o TMP (interno — ver §5) | **SPEC-014** (repurposado; absorve o Synthesis) — Manager — Convicção & Síntese | H/P |

- `[FATO]` Tabela composta de ADR-MANAGER-001 v1.0 §2.3/§2.5/§4.3 e DHR-EUA-E23 §2 item 1. A divisão da SPEC-008 é `[FATO]` DHR-SPEC008-001 §1 (P-2).
- `[FATO]` "Classe predominante" é **orientação não-vinculante**; a declaração normativa de Classe é **por BASpec**, no Plan de cada Spec (DHR-EUA-E23 §2 item 1, nota *; RULE-MECH-01; CC-11).
- `[FATO]` Slots seguem **indicativos**: número, fronteira e decomposição final de cada Spec do Manager só se fixam **na abertura** dela (DHR-EUA-E23 §2 item 3; RULE-ECC-01/02). Este contrato não antecipa a abertura da SPEC-015 nem da SPEC-014.

### 3.1 Fase 1 é mecânica

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 3.1.1 | A Fase 1 é **mecânica/determinística**: resolve grafo de dependências, sem julgamento analítico. | `[FATO]` ADR-MANAGER-001 §2.3 ("DISPATCH (mecânica/determinística)") e §2.5 |
| 3.1.2 | O controle de horário do Manager é determinístico (ENF-03); o gate da FSM do ciclo e o da FSM do alarme **nunca** são LLM. | `[FATO]` WORKFLOW v2.1: WF-K02, WF-F02, WF-A02 |
| 3.1.3 | Na abertura homologada da SPEC-008: Classe **D** em tudo + **C** na trava constitutiva; **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus. | `[FATO]` ABERTURA.md §4, homologada "como está" (DHR-SPEC008-001 §1) — a declaração por BASpec continua sendo do Plan |
| 3.1.4 | Julgamento leve pertence às Fases 0 e 2, não à Fase 1. | `[FATO]` ADR-MANAGER-001 §2.5; ABERTURA.md §4 |

---

## 4. Fronteiras entre as Fases (e com os vizinhos)

| Fronteira | O que passa | Quem é dono de cada lado | Etiqueta e âncora |
|---|---|---|---|
| **Fase 0 → Fase 1** | Pedido de ciclo com os campos de WF-01 (ativo, tipo de trading, TFs de WF-T01, Killzone, assistida/pré-programada — WF-K04) | Fase 0 (SPEC-015) **cria/decide/gerencia** missões; Fase 1 (SPEC-008) **executa** o ciclo de um pedido já definido. Até a SPEC-015 existir, o pedido vem de Andraus (WF-01). | `[FATO]` ABERTURA.md §2 S1 e tabela anti-dupla-posse (homologada, DHR-SPEC008-001) |
| **Anti-paradoxo** | — | Missão **não** exige hipótese prévia como insumo único: quem formula hipótese são os agentes analíticos, depois do despacho. | `[FATO]` ADR-MANAGER-001 §1.2/§1.3 e §5 A1 |
| **Fase 1 → Fase 2** | Caso entregue à Fase 2 | Fronteira = estado `EM_SÍNTESE` de WF-F02. SPEC-008 conduz até a entrada em `EM_SÍNTESE`; a partir dele, SPEC-014; em `EM_RISCO`, família RISK-SPEC. | `[FATO]` ABERTURA.md §2 ("Dono por transição de WF-F02"), CONF-1 aceita (DHR-SPEC008-001 §1) |
| **Fase 2 → Risco** | **TMP interno** | Fase 2 gera o TMP; o Agente de Risco (FASE RISK) decide se o sinal segue ao Bot Trade Finance. Fluxo **unidirecional**: o risco nunca retroalimenta a convicção. | `[FATO]` WORKFLOW WF-06, WF-07, WF-X03, WF-X05; INV-05 (atomic-spec v1.5, emendado por EUA-E19a) |
| **Manager × SPEC-003** | Invocação do mecanismo | SPEC-003/CCM-001 **calcula** o Conviction Vector; o Manager **invoca** — **2x por ciclo**: leitura macro na Fase 1 (estrutural+institucional) e global na Fase 2 (+operacional). Nenhuma Fase redefine o cálculo. | `[FATO]` WF-C01 (Q-A5, DHR-DEC-001); RULE-CF-010 (SPEC-003); DHR-EUA-E23 §2 item 4; DHR-ARQ-001 §2 |
| **Fase 2 × SPEC-016** | Objeto TMP | Contrato do objeto TMP (snapshot imutável, handoff interno) = SPEC-016. | `[FATO]` DHR-ARQ-002 §2 item 2 (tabela de destino) |
| **Manager × agentes analíticos** | Pedidos e publicações | Comunicação **só** via Blackboard; o Manager publica só no próprio espaço; **apenas coordena**, nunca analisa; avisos pelo Event Bus (camada fina; transporte ≠ fonte de verdade). | `[FATO]` RULE-BB-001/002/005; EVENT-BUS-001 FECHADA (DHR-SPEC005-002) |
| **Manager × Spec de Tempo** | Eventos de tempo e estados do alarme | Ator continua sendo o Manager; muda só o documento (abrir/fechar Killzone na Spec de Tempo). | `[FATO]` ABERTURA.md §2 T4 e CONF-5 aceita (DHR-SPEC008-001 §1) |

---

## 5. O Manager nunca executa ordem

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 5.1 | O SOT não executa ordem; produz um **Signal Package** para o Bot Trade Finance. O **TMP** é artefato **interno** de passagem entre a Síntese (= Manager — Fase 2) e o Risk Agent. | `[FATO]` INV-05 (atomic-spec v1.5, emenda EUA-E19a/DHR-EUA-E19a); AGENTS.md §6 item 9; DHR-ARQ-002 §2 item 3 |
| 5.2 | Toda saída decisional material declara que é **recomendação**, não execução, e sob qual autoridade. | `[FATO]` RULE-DEC-01 |
| 5.3 | O alarme-gatilho é gatilho de **análise**, nunca ordem. | `[FATO]` WF-A01 |
| 5.4 | Em missão pré-programada, o Manager roda o ciclo sozinho "até o Signal Package" e o deixa em **fila para revisão**; nunca executa. | `[FATO]` WF-K04 |
| 5.5 | Prevenção de overtrading e execução são do Bot Trade Finance, fora do SOT. | `[FATO]` WF-X04; INV-05 |
| 5.6 | Este contrato **não** atribui a montagem do Signal Package a nenhuma Fase: as fontes lidas fixam o canal de saída (SPEC-005) e a decisão de envio (Agente de Risco, WF-07), não o dono da montagem. | `[INFERÊNCIA]` WF-07; ROADMAP l.33 (SPEC-005: "canal de saída do Signal Package"); ABERTURA.md §2 tabela (P-13: "quem monta o Signal Package (SPEC-014)" listado só como candidato) |

---

## 6. O Manager nunca corta análise por custo

| # | Obrigação | Etiqueta e âncora |
|---|---|---|
| 6.1 | Nunca suprimir a execução de um agente por motivo de custo quando houver evento estruturalmente relevante. Vale para o Manager em qualquer Fase em que ele decida despachar ou não (ator único — §2). | `[FATO]` CEE-001 v2.0 §10 Salvaguarda 2 · aplicação às três Fases = `[INFERÊNCIA]` de ADR §2.2 + §2.6 deste contrato |
| 6.2 | Ruptura de hipótese dominante ⇒ análise completa **independente do custo** (Inversão #1). A mecânica do gatilho é da SPEC-008. | `[FATO]` CONFLICT-MAP, "Inversões contextuais" #1 (HOMOLOGADO 2026-09-20); l.123 (mecânica na SPEC-008 = `[INFERÊNCIA]` do próprio CONFLICT-MAP) |
| 6.3 | Custo **nunca** entra no Conviction Vector (Convicção ≠ Score). | `[FATO]` INV-04; CEE-001 v2.0 §10 Salvaguarda 4 |
| 6.4 | O Manager não reduz sozinho a classe de modelo de nenhum agente; mudança de roteamento é reversível e versionada. | `[FATO]` CEE-001 v2.0 §10 Salvaguardas 1 e 5 |
| 6.5 | Ordem dos 4Es: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade; Economicidade nunca acima de Eficácia. | `[FATO]` AGENTS.md §6 item 11 (Q-009); CEE-001 v2.0 §12 |

---

## 7. Invariantes constitucionais que valem para as três Fases (só referência — não copiados)

`[FATO]` atomic-spec v1.5 §INV e AGENTS.md §6: **INV-01** (hierarquia Elliott → Fibonacci → Fractal → SMC → ICT; posição de Fibonacci/Fractal no roteiro de despacho = "decidir depois", P-11 da DHR-SPEC008-001) · **INV-02** (ICT não cria hipótese; WF-D04 FECHADA) · AGENTS §6 item 2 (só Elliott cria a hipótese primária) · AGENTS §6 item 4 (`directional_conflict = true` ⇒ NEUTRO; WF-F01 ramo 2) · **INV-03** (8 dimensões; limiares-piloto interinos; definitivos = J-001 aberta) · **INV-04** · **INV-05** · **INV-07** · **INV-09** · **INV-10** · estados da hipótese = **CHM-001** (AGENTS §6 item 3) · CEE-001 v2.0 §11 (Salvaguardas de Sinal). O Manager **consome** esses invariantes; não os redefine (CONST-01; CC-02).

---

## 8. Pai de herança vertical (RULE-HV)

### 8.1 Filhas

| Filha | Relação | Etiqueta e âncora |
|---|---|---|
| **SPEC-008** — Despacho e Ciclo (Fase 1) | filha | `[FATO]` DHR-EUA-E23 §2 item 2; ABERTURA.md §6 CC-08 ("Pai vertical = 'Manager Contract' (P-4)") |
| **SPEC-015** — Missão & Ciclo de Vida (Fase 0) | filha | `[FATO]` DHR-EUA-E23 §2 item 2 |
| **SPEC-014** — Convicção & Síntese (Fase 2) | filha | `[FATO]` DHR-EUA-E23 §2 item 2 |
| **Spec de Tempo** (candidata SPEC-050) | filha **proposta** | `[PROPOSTA]` — o ator é o Manager (ABERTURA.md §2 T4), mas a DHR-EUA-E23 nomeia três filhas; incluir é decisão de Andraus (§9, ponto A-2) |

### 8.2 O que cada filha deve fazer (só as regras vigentes, aplicadas)

- `[FATO]` RULE-HV-01: declarar este contrato como pai por **ID + versão baseline** e **conservar o conjunto** das obrigações dos §2–§7.
- `[FATO]` RULE-HV-02 (extensão de RULE-HD-03): nenhuma obrigação daqui é suprimida fora de `REMOVED` com homologação de Andraus; supressão silenciosa = NÃO CONFORME Crítica.
- `[FATO]` RULE-HV-03 (extensão de RULE-HD-02): requisito local da filha não contradiz o pai; precedência pai > filha.
- `[FATO]` RULE-HV-04: o Revisor audita a cobertura **como conjunto**. `[PROPOSTA]` Para isso, cada filha cita os itens deste contrato pelo número de seção/linha (ex.: "MC §6 item 6.1"); os números são **índice de leitura**, não IDs normativos novos.
- `[FATO]` RULE-HD-04: a filha referencia por ID + versão; não copia o conteúdo.

### 8.3 Bloco Herança/Delta deste próprio contrato (CC-08)

```
INHERITS : ADR-MANAGER-001 v1.0 (§1.2–1.3, §2.1–2.5, §4.3, §5)
           DHR-ARQ-001 (2026-10-01) · DHR-ARQ-002 (2026-10-01) · DHR-EUA-E23 (2026-10-01) §2
           DHR-SPEC008-001 (2026-11-07) §1 — só o que fixa fronteira (P-2, CONF-1, CONF-5) e a abertura homologada (ABERTURA.md §2, §4)
           CEE-001 v2.0 §10 (S1, S2, S4, S5), §11, §12
           atomic-spec v1.5 INV-01..INV-05, INV-07, INV-09, INV-10 · RULE-DEC-01 · RULE-BB-001/002/005
           RULE-HV-01..04 (SPEC-019 v1.0) · RULE-HD-02..04
           RULE-CF-010 (SPEC-003, BASELINE) · CONFLICT-MAP "Inversões contextuais" #1 (homologado 2026-09-20)
           WORKFLOW v2.1: WF-01, WF-04, WF-06, WF-07, WF-C01, WF-K02, WF-K04, WF-A01, WF-A02, WF-F02, WF-X03, WF-X04, WF-X05, WF-D04
ADDED    : nenhum requisito novo. Só a regra de leitura do §1 e o uso de números de seção como índice (§8.2) — ambos [PROPOSTA].
MODIFIED : nenhum
REMOVED  : nenhum
```

---

## 9. Pontos que dependem de Andraus

| # | Ponto | Recomendação do Especificador | Etiqueta |
|---|---|---|---|
| **A-1** | **ID e versão** do contrato ao homologar (RULE-HV-01 exige "ID+VERSÃO baseline"; hoje o documento só tem nome). | Dar um ID curto e versão 1.0 na homologação; o Especificador **não** inventa o ID. | `[DECISÃO NECESSÁRIA]` |
| **A-2** | A **Spec de Tempo** (candidata SPEC-050) também herda deste contrato? | Sim — o ator dela é o Manager (ABERTURA.md §2 T4); sem isso, a parte de tempo da Fase 1 ficaria fora da herança. | `[DECISÃO NECESSÁRIA]` |
| **A-3** | **Lugar do arquivo** depois de homologado: hoje em `specs/features/SPEC-008/`, mas é pai de três Specs. | Mover para `governance/` (ou onde Andraus indicar) na homologação, com registro no CATALOGO; o Especificador não move. | `[DECISÃO NECESSÁRIA]` |
| **A-4** | **Divergências de texto já conhecidas** (não resolvidas aqui; nenhuma fonte foi editada): (a) ADR §2.4 desenha "TMP → Bot Trade Finance", anterior à EUA-E19a (TMP interno; Signal Package na fronteira) — lido sob INV-05 emendado; (b) ADR §3.3/§4.2 e WF-F02 apontam a SPEC-015 como Spec do Manager inteiro / da FSM, anteriores à divisão em três (DHR-EUA-E23) e à CONF-1; (c) WF-K02 nomeia "SPEC-008/015" como dona do abrir/fechar Killzone, diferente da CONF-5; (d) ADR §7 lista EVENT-BUS-001 como aberta — hoje FECHADA (DHR-SPEC005-002). | Registrar como leitura (`[INFERÊNCIA]`); correção do texto do ADR/WORKFLOW, se desejada, só por Andraus. A camada de disciplinas cognitivas do Manager (ADR §3.3: "suas camadas serão especificadas na SPEC-015") fica sob **SPEC-015-SCOPE**, aberta. | `[DECISÃO NECESSÁRIA]` (só se Andraus quiser corrigir as fontes) |

---

## 10. Decisões abertas que este contrato toca e **não** fecha (CONS-01)

`[FATO]` DHR-SPEC008-001 §5 e ROADMAP "Decisões abertas ativas": **J-001** (fórmula/pesos/limiares definitivos — limiar "conclusivo" da Fase 1 e decisão de envio da Fase 2 ficam como parâmetro) · **N-001** (pesos por ativo) · **WF-D03** (resíduo J-001) · **G-001** (persistência do estado do ciclo — SPEC-009) · **M-001** (estados não-hipótese no quadro) · **SPEC-015-SCOPE** (fronteira e escopo da Fase 0) · **C-001** · **K-001** · **SPEC-045-RUNTIME-001** · **ECC-03-001** · **D-PCC-4**. Também seguem "decidir depois": P-11 (Fibonacci/Fractal no roteiro) e P-13 (reentrada após stop). Nenhuma aparece aqui como fechada.

---

## 11. Autopré-check (resumido)

- [x] Lidos: ROADMAP.md (linhas de estado/decisões), atomic-spec.md (INV, CC-08), DHR-SPEC008-001, ABERTURA.md (§2, §4, §6, §13 P-4), ADR-MANAGER-001, DHR-EUA-E23, DHR-ARQ-001, DHR-ARQ-002, WORKFLOW.md v2.1 (citado só por ID), CEE-001 §10, CONFLICT-MAP (Inversões), RULES.md (RULE-HV, RULE-HD, RULE-BB, RULE-DEC-01).
- [x] Sem regra, campo, estado, transição ou agente novos; ADDED só com dois itens de leitura marcados `[PROPOSTA]`.
- [x] Nenhuma decisão aberta fechada (§10); P-11/P-13 mantidas "decidir depois".
- [x] Nenhum modelo canônico redefinido (CONST-01/CC-02); WORKFLOW, ADR, ROADMAP, AGENTS, canon e governance **não** editados.
- [x] Toda linha com etiqueta e âncora; `[INFERÊNCIA]` separada de `[FATO]`; documentado ≠ homologado (este arquivo é PROPOSTA).
- [x] Manager nunca executa (§5) e nunca corta análise por custo (§6) ancorados em baseline.
- [ ] Pesquisa web: **não feita** — documento de consolidação interna, sem prática externa adotada; o Dossiê da SPEC-008 (`research.md`) segue sendo a base de pesquisa.
- [ ] Gates mecânicos: ver §12.

## 12. O que NÃO foi verificado

- **Nenhum script foi executado** (o Especificador não tem Bash): `build_map.py`, `check_refs.py`, `check_doc_sync.py`, `pre_entrega.py`, `validate_spec_sot.py` (este último não se aplica — não é `plan.md`). O Orquestrador deve rodar ao menos `python scripts/build_map.py --check` e `python scripts/check_refs.py`.
- Não li por inteiro: `atomic-spec.md`, `ROADMAP.md`, `ABERTURA.md` (li l.1–233 e a P-4), `research.md`, CHM-001, CEM-001, GLOSSARIO, EUA-E19a (só as linhas que citam TMP/Signal Package), SPEC-003/004/005/016 (só as referências usadas).
- Não conferi se `backlog_triggers.py --abertura` lista algo novo para este documento (não é abertura de Spec).
- A afirmação de que a Spec de Tempo usa o Manager como ator vem da ABERTURA.md §2 T4; a nomeação "SPEC-050" segue **candidata**.
- Números de linha citados (ROADMAP l.33, CONFLICT-MAP l.123) valem para a leitura de 2026-11-07.
