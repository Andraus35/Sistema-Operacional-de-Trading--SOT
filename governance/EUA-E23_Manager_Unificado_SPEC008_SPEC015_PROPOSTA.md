# EUA-E23 — Manager Agent Unificado: simetria camadas×agentes e quantidade de Specs (PROPOSTA v2)

| Campo | Valor |
|---|---|
| Código | **EUA-E23** |
| Tipo | Emenda de Arquitetura de Especificação — **PROPOSTA** (não aplica slots; não fecha decisão; não renumera; não edita WORKFLOW.md) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Versão | **2** (2026-10-01) — incorpora a análise de **simetria camadas×agentes** pedida por Andraus e a absorção do Synthesis Agent pelo Manager (**DHR-ARQ-002**). Histórico v1 preservado no §9 (INV-07). |
| Status | **HOMOLOGADA por instrução direta de Andraus em chat (2026-10-01; ata `DHR-EUA-E23`), Alternativa 3-Specs (v2, §5).** *[texto anterior preservado — INV-07: "PROPOSTA — aguarda parecer do Revisor e homologação de Andraus"]* |
| Origem | Instrução direta de Andraus (chat, 2026-10-01): (a) "Manager dividido entre SPEC-008 e SPEC-015"; (b) "faz sentido 3 Specs — 1ª Orquestração Mecânica, 2ª Missão, 3ª Convicção, dadas as diferenças cognitivas?"; (c) pedido de **simetria** camadas×agentes para definir **quantidades** por melhores práticas |
| Autoridade-fonte | `ADR-MANAGER-001` (HOMOLOGADO §2.1/§2.3/§2.5); `DHR-ARQ-001`; `DHR-ARQ-002` (Synthesis absorvido); `WORKFLOW.md` (soberano — só por ID); `ROADMAP.md` §7/§21/§26; `GLOSSARIO.md`; RULE-ECC-01/02; RULE-MECH-01/CLASSE-MECH-001 |
| Não fecha | Nenhuma decisão aberta (CONS-01): SPEC-015-SCOPE, J-001, N-001, M-001, WF-D03 seguem abertas. Não renumera/apaga slots. Não edita WORKFLOW.md. |

---

## 0. O que mudou da v1 para a v2 (resumo)

- A **v1** recomendava **2 Specs** (Mecânica × Mission&Conviction) sob um "Manager Contract".
- A **v2** incorpora dois fatos novos e **revê a recomendação para 3 Specs**:
  1. **DHR-ARQ-002 (2026-10-01):** o **Manager absorve o Synthesis Agent** (propaga ADR-MANAGER-001 §2.1 l.59 "Agente de Síntese → absorvido (Fase 2)"). O escopo do antigo slot **SPEC-014 (Synthesis)** passa a ser a **Fase 2 (Conviction/Síntese) do Manager** — há agora **três** slots que alimentam o Manager (SPEC-008, SPEC-014, SPEC-015), não dois.
  2. A **simetria** pedida por Andraus (cada agente analítico = 1 Spec = 1 natureza cognitiva) favorece mapear as **3 naturezas cognitivas distintas** do Manager a **3 Specs concretas** — alinhadas 1:1 às 3 Fases do ADR e aos 3 slots existentes, **sem renumerar**.
- O "Manager Contract" (pai de herança vertical) **permanece** — garante o **ator único** (ADR §2.2) sobre as 3 Specs-filhas.

---

## 1. Problema (inalterado da v1, atualizado)

O **Manager Agent** é o **ator único de orquestração** em 3 Fases (ADR-MANAGER-001 §2.3):

```
MANAGER AGENT
├── FASE 0: MISSION LIFECYCLE  (decisório leve — tipo de missão, ciclo de vida, portfólio, Campanha, Plano B)
├── FASE 1: DISPATCH           (mecânico/determinístico — grafo de dependências, despacho, monitorar Blackboard)
└── FASE 2: CONVICTION         (cognitivo leve — lê Vetores de Convicção, arbitra, forma Convicção Global, gera TMP;
                                ABSORVE o antigo Synthesis Agent — DHR-ARQ-002)
```
[FONTE: ADR-MANAGER-001 §2.3/§2.4/§2.5; DHR-ARQ-002]

Mas o ROADMAP mantém **slots indicativos** que, somados, cobrem o Manager sem nomeá-lo como ator único:
- **SPEC-008 — Cognitive Scheduler** (FASE 4): quem pensa/quando/ordem/profundidade/orçamento; ativação progressiva. [FONTE: ROADMAP §7]
- **SPEC-015 — Mission Engine & Mission Lifecycle** (FASE 6): criação/ativação/monitoramento/campanha/plano alternativo. [FONTE: ROADMAP §9]
- **SPEC-014 — Synthesis Agent** (FASE 6): `Evidence→Hypothesis→Conviction→Decision→Mission/TMP`. **Agora absorvido pela Fase 2 do Manager (DHR-ARQ-002).** [FONTE: ROADMAP §9; DHR-ARQ-002]

**Colisões documentais (FONTE):** ADR §4.2 manda a SPEC-015 "especificar o Manager com a arquitetura 3-fases" — colidindo com o dispatch/scheduler que o ROADMAP coloca na SPEC-008; a MATRIZ registra isto como **Conflito C-1** ("Manager dividido entre dois slots"); ADR §7 lista **SPEC-015-SCOPE** como decisão aberta.

---

## 2. Simetria camadas × agente/mecanismo × Classe × Spec dona (matriz)

> **Natureza:** [INFERÊNCIA] derivada de ROADMAP (fases/slots) + ADR-MANAGER-001 + CLASSE-MECH-001 (Classe D/H/P/C) + GLOSSARIO. Slots são **indicativos** (RULE-ECC-01). "Classe predominante" é orientação não-vinculante (declaração normativa é por BASpec — SES-001 §50).

| Camada do SOT (FASE) | Agente / Mecanismo | Natureza cognitiva | Classe predom. | Spec dona (slot indicativo) | Nº de Specs do ator |
|---|---|---|---|---|---|
| Núcleo cognitivo (F1) | Hypothesis Harness | contrato de objeto | C/D | SPEC-001 (baseline) | 1 |
| Núcleo cognitivo (F1) | Evidence Harness | contrato de objeto | D/C/H/P | SPEC-002 (baseline) | 1 |
| Núcleo cognitivo (F1) | **Fusion Engine + Conviction Engine** (mecanismos) | agregação determinística + julgamento c/ gate | D/H/C | SPEC-003 (candidata) | 1 (mecanismo, não agente) |
| Memória trabalho (F2) | Blackboard · Event Bus | infraestrutura | D/C | SPEC-004 · SPEC-005 | 1 cada |
| Memória semântica (F3) | Knowledge Graph · RAG | infraestrutura | D/C/H | SPEC-006 · SPEC-007 | 1 cada |
| Cognição/escalonamento (F4) | **Manager — Dispatch/Scheduler (Fase 1)** + relógio/alarme/FSM | **mecânico/determinístico** | **D/C** | **SPEC-008** | (ver recomendação) |
| Cognição/escalonamento (F4) | Cognitive State & Persistence | infraestrutura de estado | D/C | SPEC-009 | 1 |
| **Agentes analíticos (F5)** | **Structural Agent (Elliott)** | julgamento de 1 escola | **P** (julgamento + gate) | **SPEC-010** | **1** |
| Agentes analíticos (F5) | Fibonacci & Fractal Confluence | validação geométrica | P/H | SPEC-011 | 1 |
| Agentes analíticos (F5) | **Institutional Agent (SMC)** | julgamento de 1 escola | **P** | **SPEC-012** | **1** |
| Agentes analíticos (F5) | **Operational Agent (ICT)** | execução/timing (não cria hipótese) | P/H | **SPEC-013** | **1** |
| Síntese/missão/decisão (F6) | **Manager — Conviction/Síntese (Fase 2)** (absorve Synthesis) | **cognitivo leve — arbitragem** | **H/P** | **SPEC-014** (repurposado) | (ver recomendação) |
| Síntese/missão/decisão (F6) | **Manager — Mission Lifecycle (Fase 0)** | **decisório leve — ciclo de vida** | **H/P** | **SPEC-015** (repurposado) | (ver recomendação) |
| Síntese/missão/decisão (F6) | TMP (handoff interno) | contrato de objeto | C/D | SPEC-016 (repurposada) | 1 |
| Memória/aprendizado (F7) | Pattern Memory · Learning Gov. | memória/aprendizado | H/P | SPEC-017 · SPEC-018 | 1 cada |
| FASE GOV | Governance · Evaluation · Score | meta-harness | C/D | SPEC-019/020/021 (baseline) | 1 cada |
| Integração (F9) | **Cognitive Orchestrator** | coordenação sem análise | D/C | SPEC-023 | 1 |
| Meta (F9) | Meta Cognitive Supervisor | observação de 2ª ordem | H/P | SPEC-024 | 1 |
| **Risco (FASE RISK)** | **Risk Agent** (sub-harness completo) | **harness próprio (N8–N17 de risco)** | D/H/P/C | **RISK-M1..M6** (EUA-E20) | **6 macro-slots** |

### 2.1 Assimetrias detectadas

| # | Assimetria | Severidade | Leitura |
|---|---|---|---|
| **A-1** | Cada **agente analítico** tem **1 Spec** e **1 natureza cognitiva**; o **Manager** tem **3 naturezas distintas** (mecânica, missão, convicção) espalhadas por **2 slots** (008/015) que **não o nomeiam** como ator único. | Média | O Manager está **sub-decomposto por nome legado** e **misturando naturezas** dentro de slots. |
| **A-2** | **SPEC-014 (Synthesis Agent)** era um slot de agente autônomo, mas o Synthesis foi **absorvido** pela Fase 2 do Manager (DHR-ARQ-002) → slot **sem dono autônomo real**. | Média | O escopo de SPEC-014 precisa de destino explícito (esta proposta: Fase 2 do Manager). |
| **A-3** | SPEC-008 (Scheduler) e SPEC-015 (Mission) **misturam** funções mecânicas (relógio/alarme/dispatch/FSM) com funções de julgamento (missão/convicção) — **duas naturezas por Spec**. | Média | Fere "uma fronteira de responsabilidade por Spec". |
| **A-4** | Nomes de slot "Scheduler"/"Mission Engine" são **próximos dos componentes legados eliminados** (ADR §2.1 lista "Mission Engine" como **eliminado**). | Baixa-Média | Drift taxonômico: slot contradiz o ADR que eliminou o nome. |
| **A-5** | **Risk Agent** = 6 macro-slots (EUA-E20) vs 1 Spec por agente analítico. | Baixa | **Não é assimetria indevida:** o Risk Agent é um **sub-harness** com camadas próprias N8–N17 (fundamento/decisão/quantificação/memória/operacionalização/avaliação), análogo ao **núcleo cognitivo inteiro**, não a um único agente analítico. Grão diferente, legítimo (ver §6). |

---

## 3. Critérios de melhores práticas aplicados

| Critério | Fonte | Como incide |
|---|---|---|
| **Coesão por natureza cognitiva/Classe** | CLASSE-MECH-001; ADR §2.5 | Mecânico (D/C) ≠ missão (H/P) ≠ convicção (H/P) têm perfis de teste e enforcement distintos. |
| **Acoplamento mínimo** | ROADMAP §24; GPR-001 | Fronteiras explícitas reduzem dependência cruzada; Fase 1 (dispatch) não depende do julgamento de Fase 0/2. |
| **Atomicidade revisável** | atomic-spec §5 ("cabe numa sessão de revisão") | Spec guarda-chuva com 3 Fases CRITICAL D0–D8 estoura a sessão de revisão. |
| **Separação mecânico × julgamento** | ADR §2.5 (FATO NORMATIVO) | O próprio ADR normatiza que Fase 1 é mecânica e Fases 0/2 são julgamento leve. |
| **Uma fronteira de responsabilidade por Spec** | SES-001; SDD-001 | Corrige A-3 (duas naturezas por slot). |
| **Simetria com os agentes analíticos** | pedido de Andraus | Cada agente = 1 Spec = 1 natureza → o Manager, com 3 naturezas, mapeia naturalmente a 3 Specs. |
| **Ator único preservado** | ADR §2.2 | Garantido pelo "Manager Contract" (pai de herança vertical RULE-HV), não por fundir tudo numa Spec. |
| **Não maximizar volume** | ROADMAP §24 | Contrapeso: só decompor onde há natureza/fronteira genuinamente distinta (há 3, não mais). |

---

## 4. Alternativas: 2 Specs × 3 Specs para o Manager

### Alternativa 2-Specs (recomendação da v1)
- **Spec A — Orquestração Mecânica** (absorve SPEC-008): relógio/Killzone (WF-K), alarme FSM (WF-A), dispatch (Fase 1), FSM do ciclo (WF-F02), orçamento. Classe **D/C**.
- **Spec B — Mission & Conviction** (absorve SPEC-015 + a Fase 2/Synthesis): Fase 0 (missão) **+** Fase 2 (convicção/síntese/TMP). Classe **H/P**.
- **Contra:** a Spec B junta **duas naturezas cognitivas distintas** (gestão de missão no início do ciclo × arbitragem de convicção no fim) — reintroduz A-3 em menor grau; Spec B fica grande (Fase 0 + Fase 2 + geração de TMP + invocação da SPEC-003).

### Alternativa 3-Specs (**recomendada na v2**)
Mapeia 1:1 as 3 Fases do ADR e os 3 slots existentes (sem renumerar):

| Spec (slot repurposado) | Fase | Escopo | Classe predom. | WF-xx tocados |
|---|---|---|---|---|
| **Manager — Orquestração Mecânica** (SPEC-008) | Fase 1 + serviços de tempo | Dispatch/grafo de dependências; relógio/Killzone; alarme FSM; FSM do ciclo; orçamento/ativação progressiva | **D/C** (gates não-LLM, ENF-03) | WF-K01..04, WF-A01..03, WF-F01/F02, WF-02/03 (ordem) |
| **Manager — Missão & Ciclo de Vida** (SPEC-015) | Fase 0 | Tipo de missão (Exploratória/Validação); ciclo de vida; portfólio; Campanha; Plano B; relação hipótese→missão | **H/P** (decisório leve + gate) | WF-01, WF-K04, WF-F01 |
| **Manager — Convicção & Síntese** (SPEC-014, repurposado; absorve Synthesis) | Fase 2 | Ler Vetores de Convicção do Blackboard; **invocar** o mecanismo da SPEC-003/CCM-001; arbitrar conflitos entre agentes; formar **Convicção Global**; gerar **TMP interno** (handoff ao Risco) | **H/P** (cognitivo leve + gate de saída) | WF-04, WF-06, WF-C01, WF-F02 |

- **Prós:** coesão máxima por natureza; cada Spec cabe numa sessão; corrige A-1/A-2/A-3/A-4; simetria perfeita com os agentes analíticos (1 natureza/1 Spec); a absorção do Synthesis (DHR-ARQ-002) encontra **destino natural** na Fase 2 (SPEC-014 repurposado); nenhum slot renumerado/apagado (INV-07).
- **Contra:** 3 Specs em vez de 2 (um artefato a mais); exige que o "Manager Contract" discipline as fronteiras Fase 0↔Fase 1↔Fase 2 para não reintroduzir o paradoxo circular que o ADR resolveu.
- **Risco:** médio-baixo (disciplina do contrato; mitigável por RULE-HV + MAN-001).

### 4.1 "Convicção do Manager" (Fase 2) duplica a SPEC-003? — **NÃO (complementar)**
Fronteira nítida, declarada para evitar double-ownership:

| | **SPEC-003** (Conviction/Fusion Engine) | **Manager — Convicção & Síntese** (Fase 2) |
|---|---|---|
| Objeto | **O mecanismo**: CCM-001, fusão de evidência, cálculo do Conviction Vector 8D | **O invocador/árbitro**: quando/como invocar o mecanismo e decidir |
| Natureza | agregação determinística + julgamento com gate (D/H/C) | arbitragem cognitiva leve + geração de TMP (H/P) |
| Produz | evidência DERIVED + Conviction Vector + Global Conviction (contrato) | decisão de síntese + TMP interno (handoff ao Risco) |
| Fronteira | **não** decide missão, **não** gera TMP, **não** executa | **não** redefine o cálculo do vetor (usa o da SPEC-003) |

A SPEC-003 **redige o motor**; a Spec do Manager-Fase-2 **usa o motor** e decide. Sem duplicação (DHR-ARQ-001: o "Conviction Engine" é mecanismo **invocado pelo** Manager Fase 2).

---

## 5. Recomendação (v2)

**Recomendo a Alternativa 3-Specs**, sob um **"Manager Contract"** comum (pai de herança vertical, RULE-HV), repurposando os três slots existentes **sem renumerar** (INV-07):
- **SPEC-008** → **Manager — Orquestração Mecânica** (Classe D/C)
- **SPEC-015** → **Manager — Missão & Ciclo de Vida** (Classe H/P)
- **SPEC-014** → **Manager — Convicção & Síntese** (Classe H/P; absorve o Synthesis — DHR-ARQ-002)

Justificativa: é a única decomposição que honra simultaneamente (i) o **ator único** do ADR (via contrato), (ii) a **separação mecânico×julgamento** que o ADR §2.5 torna normativa, (iii) a **atomicidade revisável** (cada Spec cabe numa sessão), (iv) a **simetria** com os agentes analíticos (1 natureza / 1 Spec) e (v) o **destino natural** da absorção do Synthesis (Fase 2 = SPEC-014 repurposado). Supera a v1 (2 Specs) precisamente porque DHR-ARQ-002 tornou a Fase 2 substancial o bastante para ser Spec própria, e porque juntar Fase 0+Fase 2 (v1) misturava duas naturezas cognitivas — exatamente a assimetria A-3 que Andraus quer corrigir.

**Se Andraus preferir conservadorismo de volume (ROADMAP §24)**, a Alternativa 2-Specs permanece válida como fallback (Fase 0+Fase 2 juntas), ao custo de A-3 residual. A decisão é de Andraus.

---

## 6. Coerência com a EUA-E20 (nº de macro-slots RISK) — simetria NÃO exige mudança

A matriz (§2, A-5) mostra que o **Risk Agent é um sub-harness completo** (camadas próprias N8–N17 de risco: fundamento, decisão, quantificação, memória, operacionalização, avaliação), análogo ao **núcleo cognitivo inteiro** do SOT, **não** a um único agente analítico. Portanto os **6 macro-slots RISK-M1..M6** (EUA-E20) são **grão de container** (cada um decomposto na abertura, RULE-ECC-01) e **não** colidem com a regra "1 natureza/1 Spec" aplicada ao Manager — que é grão de **Spec concreta**. **Conclusão: a simetria não exige alterar o número 6.** A EUA-E20 recebe apenas uma **nota de coerência** (mesma régua de coesão por natureza cognitiva), sem mudança de número — ver EUA-E20 §2 (nota de simetria v2).

---

## 7. O que muda se homologada (não aplicado agora)

- **ROADMAP:** redefinição, **na abertura** (RULE-ECC-01, com Dossiê RULE-ECC-02), dos slots **SPEC-008/SPEC-014/SPEC-015** como as três Specs do Manager; nomes de slot migram para "Manager — Orquestração Mecânica / Missão & Ciclo de Vida / Convicção & Síntese"; **slots não apagados nem renumerados** (INV-07); re-apontamento de gatilhos RMR-001 (BL-026 etc.) por ato homologado.
- **Novo artefato:** "Manager Contract" (documento de contrato, não agente) — pai de herança vertical das 3 Specs.
- **Decisões abertas:** **SPEC-015-SCOPE** passa a endereçável; **não** fechada aqui. J-001/N-001/M-001/WF-D03 intactas.
- **Fronteiras:** SPEC-003 (mecanismo invocado pela Fase 2), SPEC-004 (Blackboard), SPEC-009 (estado), SPEC-016 (TMP interno), família RISK (recebe o TMP a jusante, WF-07). Nenhuma viola INV-05.

---

## 8. Não-objetivos (CONS-01)

Esta proposta **não** cria agente novo (Manager já é o único orquestrador — ADR §2.2), **não** fecha SPEC-015-SCOPE/J-001/N-001/M-001/WF-D03, **não** renumera nem apaga slots, **não** edita o `WORKFLOW.md`, **não** altera o número de macro-slots RISK, e **não** decide sizing/execução (INV-05). Tudo depende de homologação de Andraus. A absorção do Synthesis é tratada por **DHR-ARQ-002** (propagação de decisão já homologada no ADR); esta EUA-E23 apenas **recebe** esse fato para definir a decomposição.

---

## 9. Histórico — Proposta v1 (preservada, INV-07)

> A v1 (2026-10-01) recomendava a **Alternativa 2** (duas Specs por natureza de Classe — "Manager — Orquestração Mecânica" × "Manager — Mission & Conviction" — sob um "Manager Contract"), com três alternativas consideradas: (1) uma Spec única guarda-chuva (rejeitada por ferir atomicidade); (2) duas Specs (recomendada na v1); (3) manter SPEC-008+SPEC-015 + contrato de reconciliação (rejeitada por perpetuar nome legado). A v2 **mantém o diagnóstico** (C-1, SPEC-015-SCOPE, drift taxonômico) e o **"Manager Contract"**, mas **revê a recomendação para 3 Specs** à luz de DHR-ARQ-002 (Synthesis absorvido → Fase 2 substancial) e do critério de simetria pedido por Andraus. Nenhum conteúdo da v1 é apagado; a mudança é de recomendação, não de supressão.

---

*EUA-E23 — PROPOSTA v2. Produzida pelo Especificador (Claude Code) por instrução direta de Andraus, 2026-10-01. Aguarda Revisor + Andraus.*
