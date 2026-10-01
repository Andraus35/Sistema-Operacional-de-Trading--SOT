# EUA-E23 — Manager Agent Unificado: fronteira SPEC-008 × SPEC-015 (PROPOSTA)

| Campo | Valor |
|---|---|
| Código | **EUA-E23** (próximo código EUA livre — ver §0) |
| Tipo | Emenda de Arquitetura de Especificação — **PROPOSTA** (não aplica slots; não fecha decisão) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-01 |
| Status | **PROPOSTA — aguarda parecer do Revisor e homologação de Andraus** |
| Origem | Instrução direta de Andraus (chat, 2026-10-01): "Manager está dividido entre SPEC-008 (Cognitive Scheduler) e SPEC-015 (Mission Engine) embora WF-04/WF-06 e o ADR falem de um ator único" |
| Autoridade-fonte | `governance/ADR-MANAGER-001_Manager_Agent_Architecture.md` (HOMOLOGADO); `WORKFLOW.md` (soberano — citado só por ID); `ROADMAP.md` §7/§21/§26; RULE-ECC-01/02 |
| Não fecha | Nenhuma decisão aberta (CONS-01). Não renumera slots. Não edita `WORKFLOW.md`. |

---

## 0. Confirmação do código EUA

[FONTE: `governance/DHR-EUA-E22_...md` §76 — *"EUA-E20 (FASE RISK) e EUA-E21 (pesquisa web/RULE-ECC-02) permanecem reservadas; EUA-E22 é o próximo código disponível e fica confirmado."*]

- **EUA-E20** — RESERVADA para a FASE RISK (objeto da proposta-irmã `EUA-E20_Fase_RISK_Slots_PROPOSTA.md`, Frente C).
- **EUA-E21** — usada/homologada (Especificação Emergente, DHR-EUA-E21).
- **EUA-E22** — usada/homologada (Manutenção do Mapa, DHR-EUA-E22).
- **EUA-E23** — **próximo código livre** → esta proposta. [INFERÊNCIA a partir de FONTE acima + glob de `governance/EUA-E2*`.]

---

## 1. Problema

O **Manager Agent** foi homologado como **ator único de orquestração** em 3 Fases (ADR-MANAGER-001 §2.3):

```
MANAGER AGENT
├── FASE 0: MISSION LIFECYCLE  (decisório leve — tipo de missão, ciclo de vida, portfólio, Campanha, Plano B)
├── FASE 1: DISPATCH           (mecânico/determinístico — grafo de dependências, despacho, monitorar Blackboard)
└── FASE 2: CONVICTION         (cognitivo leve — lê Vetores de Convicção, arbitra, forma Convicção Global, gera TMP)
```
[FONTE: ADR-MANAGER-001 §2.3/§2.4/§2.5]

Mas o ROADMAP mantém **dois slots indicativos** que, somados, cobrem o Manager — sem que nenhum o nomeie como ator único:
- **SPEC-008 — Cognitive Scheduler** (FASE 4): "quem pensa; quando; por quê; em que ordem; profundidade; orçamento; quais Skills despertar; quando interromper/aguardar/escalar/encerrar; ativação progressiva/lazy orchestration". [FONTE: ROADMAP §7/§180-183]
- **SPEC-015 — Mission Engine & Mission Lifecycle** (FASE 6): "criação; ativação; monitoramento; envelhecimento; atualização; suspensão; encerramento; campanha; plano alternativo; relação hipótese→missão". [FONTE: ROADMAP §9/§215-216]

E o ADR-MANAGER-001 §4.2 diz que **SPEC-015** "deve especificar o Manager Agent com esta arquitetura 3-fases" — colidindo com a atribuição de dispatch/scheduler que o ROADMAP coloca na SPEC-008.

**Sintomas no repositório (achados do Especificador, FONTE):**
- `WORKFLOW.md` WF-04/WF-06 falam de "Manager" como ator único que forma convicção e sintetiza; `WF-K02`/`WF-A02`/`WF-F02` atribuem relógio/Killzone, FSM do alarme e FSM do ciclo ao "Manager/Scheduler" (IDs em `docs/MATRIZ-WORKFLOW-SPEC.md`, derivada; fonte de verdade = `WORKFLOW.md`).
- A MATRIZ registra isto como **Conflito C-1** ("Manager dividido entre dois slots"). [FONTE: `docs/MATRIZ-WORKFLOW-SPEC.md` §Conflitos C-1]
- ADR-MANAGER-001 §7 lista **SPEC-015-SCOPE** como decisão aberta. [FONTE: ADR-MANAGER-001 §7]

**Fronteira de responsabilidade por fase (quem é dono de quê — [INFERÊNCIA] a partir de ADR + WORKFLOW IDs):**

| Função | Fase do Manager | ID `WF-xx` associado (fonte: WORKFLOW.md) | Slot atual |
|---|---|---|---|
| Relógio / Killzone (abrir/fechar janela) | — (serviço de tempo, pré-Fase 0) | WF-K01..K04, WF-K02 (pré-aviso 1h) | SPEC-008 |
| Alarme-gatilho de preço (FSM IDLE→ARMED→TRIGGERED…) | Fase 0/1 | WF-A01..A03, WF-A02 (FSM) | SPEC-008 |
| Tipo de missão (Exploratória/Validação), ciclo de vida, portfólio, Campanha, Plano B | Fase 0 | WF-01, WF-K04 | SPEC-015 |
| Dispatch (grafo de dependências, despacho de agentes, monitorar Blackboard) | Fase 1 | WF-02/03 (ordem) | **ambíguo** (SPEC-008 "ordem" × ADR→SPEC-015) |
| Síntese de convicção macro/global; invocar o mecanismo de convicção da SPEC-003; arbitrar; gerar TMP | Fase 2 | WF-04, WF-06 | SPEC-015 + invoca SPEC-003 |
| FSM do ciclo inteiro (determinística, auditável) | transversal | WF-F02 | SPEC-015 |

---

## 2. Alternativas consideradas

### Alternativa 1 — **Uma Spec única "Manager Agent"** (funde SPEC-008 + SPEC-015)

Um único slot (ex.: SPEC-015 repurposada como "Manager Agent", SPEC-008 descartada como slot e absorvida — INV-07, nunca apagada) especifica as 3 Fases num só artefato, espelhando 1:1 o ADR-MANAGER-001.

- **Prós:** coesão máxima com o ADR (um ator = uma Spec); elimina a ambiguidade de dispatch; fronteira interna por Fase, não por Spec; rastreabilidade direta WF-04/WF-06 → uma dona.
- **Contras:** Spec muito grande (3 Fases, CRITICAL, D0–D8) — tensiona a regra "a Spec deve caber numa sessão de revisão" (atomic-spec/§5); mistura um bloco **mecânico/determinístico** (Fase 1 + relógio/alarme) com um bloco **cognitivo leve** (Fase 2), que têm Classe (CLASSE-MECH-001) e perfis de teste distintos; o scheduler (ativação progressiva, orçamento de tokens, lazy orchestration) é tema denso que pode merecer foco próprio.
- **Risco:** alto risco de Spec "guarda-chuva" que fere a atomicidade (RULE-ECC-01 item 4 / princípio §24 do ROADMAP: não maximizar volume).

### Alternativa 2 — **Duas Specs por Fase, sob um "Manager Contract" comum** (RECOMENDADA)

Um **documento de contrato do Manager** (não um agente novo) fixa a identidade única, as 3 Fases, as fronteiras inter-fase e o que cada fase pode/não pode fazer (incl. "Manager não é agente analítico" — ADR §2.5). Sob esse contrato, **duas Specs** decompõem por **natureza de Classe**, não por nome legado:
- **Spec "Manager — Orquestração Mecânica"** (absorve SPEC-008): relógio/Killzone (WF-K), alarme FSM (WF-A), dispatch/grafo de dependências (Fase 1), FSM do ciclo (WF-F02), orçamento/ativação progressiva. Predominantemente **Classe D/C** (determinístico/constitutivo; gates não-LLM, ENF-03).
- **Spec "Manager — Mission & Conviction"** (absorve SPEC-015): ciclo de vida da missão, tipo de missão, portfólio, Campanha, Plano B (Fase 0) + Fase 2 (arbitragem de convicção, invocação do mecanismo de convicção da SPEC-003, Convicção Global, geração do TMP). Predominantemente **Classe H/P** (julgamento leve com gate).

- **Prós:** respeita a **distinção Classe mecânica × cognitiva** do próprio ADR §2.5 (Fases 1 vs 0/2); cada Spec cabe numa sessão de revisão; o "Manager Contract" garante o **ator único** (resolve C-1 sem inchar uma Spec); fronteira explícita e auditável; herança vertical (RULE-HV) do contrato para as duas filhas.
- **Contras:** exige redigir o "Manager Contract" (artefato novo — custo de 1 documento); a fronteira Fase 0 (missão) × Fase 1 (dispatch) precisa ser cuidadosamente desenhada para não reintroduzir o paradoxo circular que o ADR resolveu.
- **Risco:** médio-baixo; o principal é a disciplina de manter o contrato como fonte única (mitigável por RULE-HV + MAN-001 convergência horizontal).

### Alternativa 3 — **Manter SPEC-008 + SPEC-015 como estão + um "Manager Contract" de reconciliação**

Não mexe nos dois slots; adiciona só um contrato que declara que ambos implementam o mesmo ator e fixa a fronteira.

- **Prós:** disrupção mínima ao ROADMAP; rápido.
- **Contras:** mantém a divisão **por nome legado** ("Scheduler" × "Mission Engine") em vez de **por Classe/natureza**; "Scheduler" e "Mission Engine" são justamente nomes próximos dos legados absorvidos (ADR §2.1 lista "Mission Engine" como **eliminado**) — perpetua ambiguidade taxonômica; não resolve a colisão ADR §4.2 (que manda a SPEC-015 conter dispatch) com o escopo de SPEC-008.
- **Risco:** médio; drift taxonômico persiste; "Mission Engine" como nome de slot contradiz o ADR que o eliminou.

---

## 3. Recomendação

**Recomendo a Alternativa 2 (duas Specs por natureza de Classe, sob um "Manager Contract" comum).** Ela é a única que honra simultaneamente (i) o **ator único** do ADR-MANAGER-001 (via contrato), (ii) a **distinção mecânica × cognitiva** que o próprio ADR §2.5 torna normativa (Fase 1 determinística vs Fases 0/2 de julgamento leve) — alinhada à taxonomia Classe D/C vs H/P da CLASSE-MECH-001 —, e (iii) a **atomicidade/revisabilidade** exigida pelo método (cada Spec cabe numa sessão). A decomposição passa a ser **por natureza do trabalho**, não por nome legado, removendo o risco taxonômico que a Alternativa 3 perpetua e o risco de Spec guarda-chuva da Alternativa 1. O "Manager Contract" vira o pai de herança vertical (RULE-HV) das duas Specs-filhas e o ponto de rastreabilidade de WF-04/WF-06/WF-K/WF-A/WF-F.

**Fronteira recomendada (resumo):** relógio/Killzone (WF-K), alarme FSM (WF-A), dispatch + FSM do ciclo (WF-F) e orçamento → Spec mecânica (Classe D/C). Ciclo de vida de missão (Fase 0) + convicção/síntese (Fase 2, invoca o mecanismo da SPEC-003) → Spec cognitiva (Classe H/P). Ambas conformam-se ao `WORKFLOW.md` por ID (RULE-ECC-05 lente 3) e **não** fecham `WF-D03`.

---

## 4. O que muda se homologada (não aplicado agora)

- **ROADMAP:** redefinição dos slots indicativos SPEC-008 e SPEC-015 na **abertura** (RULE-ECC-01), cada uma com Dossiê (RULE-ECC-02); nomes de slot migram de "Cognitive Scheduler"/"Mission Engine" para "Manager — Orquestração Mecânica"/"Manager — Mission & Conviction" (slots **não apagados**, INV-07; re-apontamento de gatilhos do RMR-001 por ato homologado). Capacidades do §26 preservadas (nenhuma capacidade descartada).
- **Novo artefato:** "Manager Contract" (documento de contrato, não agente) — candidato a ser redigido na abertura da primeira das duas Specs ou como peça de governança própria.
- **Decisões abertas:** **SPEC-015-SCOPE** (ADR §7) passa a endereçável; **não** se fecha aqui. J-001/N-001/WF-D03 intactas.
- **Fronteiras com outras Specs:** SPEC-004 (Blackboard — o Manager monitora/publica, não redefine), SPEC-009 (Cognitive State — estado do Manager/missão), SPEC-016 (TMP interno gerado pela Fase 2), **SPEC-003** (mecanismo de convicção invocado pela Fase 2 — DHR-ARQ-001), família **RISK** (Fase 2 entrega TMP interno a jusante; WF-07). Nenhuma viola INV-05 (SOT não executa).
- **RMR-001:** re-apontamento de gatilhos `spec:SPEC-008...`/`spec:SPEC-015...` (ex.: BL-026 valores editáveis WF-R01..R03) para as novas donas.

---

## 5. Não-objetivos (CONS-01)

Esta proposta **não** cria agente novo (ADR §2.2 — Manager já é o único orquestrador), **não** fecha SPEC-015-SCOPE, J-001, N-001, M-001 ou `WF-D03`, **não** renumera nem apaga slots, **não** edita o `WORKFLOW.md`, e **não** decide position sizing/execução (INV-05 — isso é Risk/externo). Tudo depende de homologação de Andraus.

---

*EUA-E23 — PROPOSTA. Produzida pelo Especificador (Claude Code) por instrução direta de Andraus, 2026-10-01. Aguarda Revisor + Andraus.*
