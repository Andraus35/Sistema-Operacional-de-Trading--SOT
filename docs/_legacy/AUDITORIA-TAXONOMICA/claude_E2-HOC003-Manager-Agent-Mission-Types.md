# ENTREGA 2 — Instrução a Claude Code: Manager Agent + Tipos de Missão
**De:** Andraus (via AEH HOC-003)  
**Para:** Claude Code (Especificador / agentes de pipeline)  
**Data:** 2026-09-26  
**Referência:** ADR-MANAGER-001 + ADR-MISSION-TYPES-001 + ADR-CONFLUENCE-001 v3  
**Assunto:** Decisões arquiteturais do cluster GOV-ORCH-001 — normalização obrigatória

---

## CONTEXTO DESTA INSTRUÇÃO

Esta instrução registra um conjunto de decisões arquiteturais tomadas em revisão com o AEH (HOC-003) que resolvem o cluster de achados GOV-ORCH-001 (CRIT-004). As decisões são **normativas e imediatas** — specs futuras e qualquer documentação revisional devem conformar a este baseline.

Esta instrução não é uma solicitação de análise. É um conjunto de decisões já homologadas que o agente deve incorporar em seu modelo de trabalho.

---

## PARTE 1 — COMPONENTES LEGADOS ELIMINADOS

Os seguintes componentes **não existem mais** como entidades arquiteturais independentes no SOT SISTEMA TRADING:

| Componente eliminado | Não deve aparecer em specs como |
|---|---|
| Master Orchestrator | componente independente |
| Mission Engine | componente independente |
| Decision Orchestrator | componente independente |
| Orchestration Layer | camada independente |
| Agente Decisor | agente independente |
| Agente de Síntese | agente independente |

Estes componentes foram identificados em documentos legados (GAS Doc 03, MOES Doc 09, DCEBS Doc 13) mas **nunca foram reconciliados** entre si e criavam ambiguidade taxonômica. Estão todos absorvidos pelo Manager Agent (ver Parte 2).

**Se qualquer spec vigente mencionar estes componentes como entidades independentes, a spec está desatualizada e deve ser corrigida.**

---

## PARTE 2 — MANAGER AGENT (novo componente canônico)

### 2.1 Identidade

O **Manager Agent** é o único componente de orquestração do SOT. Não é um agente analítico de mercado. Não possui skills de análise técnica. Seus três domínios:

1. Gestão do ciclo de vida de missões (Mission Lifecycle)
2. Despacho determinístico de agentes analíticos (Dispatch)
3. Síntese de convicções e geração do TMP (Conviction)

### 2.2 Arquitetura em 3 Fases

```
MANAGER AGENT
├── FASE 0: MISSION LIFECYCLE
│   - Monitora triggers de mercado e hipóteses de ciclos anteriores
│   - Decide o tipo de missão: Exploratória ou Validação (ver Parte 3)
│   - Cria e gerencia o ciclo de vida de cada missão
│   - Gerencia portfólio de missões paralelas (quando aplicável)
│   - Cria Campanhas Operacionais
│   - Gera Plano B quando hipótese é invalidada
│
├── FASE 1: DISPATCH (mecânica / determinística)
│   - Resolve o grafo de dependências entre submissões
│   - Despacha agentes analíticos na ordem correta
│   - Monitora publicações no Blackboard
│   - SEM julgamento analítico — puramente determinístico
│
└── FASE 2: CONVICTION (cognitiva leve)
    - Lê Vetores de Convicção do Blackboard (publicados pelos agentes analíticos)
    - Arbitra conflitos entre agentes quando há divergência
    - Forma Convicção Global
    - Gera Trading Mission Package (TMP) → entregue ao Bot Trade Finance
```

### 2.3 Posição no fluxo arquitetural

```
Market Digital Twin
      ↓
MANAGER AGENT (Fase 0: Mission Lifecycle)
      ↓
┌──────────────────────────────────────────┐
│  Structural Agent   [MTF: S1/D1/H4/H1]  │ → publica Conviction Vector no Blackboard
│  Institutional Agent [MTF: S1/D1/H4/H1] │ → publica Conviction Vector no Blackboard
│  Operational Agent  [Single TF: M5]     │ → publica Conviction Vector no Blackboard
└──────────────────────────────────────────┘
      ↓
BLACKBOARD ────────→ Manager Agent (Fase 1: Dispatch + Fase 2: Conviction)
      ↓
Trading Mission Package (TMP)
      ↓
Bot Trade Finance
```

### 2.4 O que Manager Agent NÃO faz

- NÃO analisa mercado
- NÃO formula hipóteses de mercado por conta própria
- NÃO possui skills das camadas N8-N17 de análise técnica
- NÃO é um agente de síntese analítica — é um agente de síntese de convicções (meta-nível)
- NÃO escreve de volta no Blackboard analítico (Blackboard é unidirecional: agentes → Manager)

### 2.5 Spec de referência

A SPEC-015 será a especificação formal do Manager Agent. O escopo da SPEC-015 é determinado por esta instrução.

---

## PARTE 3 — TIPOS DE MISSÃO

### 3.1 Dois tipos canônicos

Existem **exatamente dois tipos** de missão:

#### MISSÃO EXPLORATÓRIA
- **Hipótese de entrada:** nenhuma (`null`)
- **Trigger:** evento de mercado / abertura de sessão / invalidação de hipótese anterior / ciclo inicial
- **Comportamento:** Manager Agent despacha agentes SEM hipótese prévia
- **Output dos agentes:** formulam hipóteses locais livremente → publicam Conviction Vectors
- **Output do Manager:** hipótese dominante emerge da Fase 2 → TMP
- **Papel:** ponto de partida de qualquer ciclo

#### MISSÃO DE VALIDAÇÃO
- **Hipótese de entrada:** hipótese dominante do ciclo anterior
- **Trigger:** conclusão de Missão Exploratória com hipótese dominante estabelecida
- **Comportamento:** Manager Agent despacha agentes COM hipótese como contexto
- **Output dos agentes:** validam ou refutam a tese → publicam Conviction Vectors
- **Output do Manager:** TMP atualizado com convicção consolidada
- **Se hipótese refutada:** Manager Agent (Fase 0) gera Plano B → nova Missão Exploratória

### 3.2 Ciclo completo

```
Trigger inicial / invalidação
      ↓
MISSÃO EXPLORATÓRIA (sem hipótese)
      ↓
Hipótese dominante emerge?
  ├── SIM → MISSÃO DE VALIDAÇÃO (com hipótese)
  │         ├── Hipótese mantida → TMP → Bot
  │         └── Hipótese refutada → Plano B → nova MISSÃO EXPLORATÓRIA
  └── NÃO → nova MISSÃO EXPLORATÓRIA
```

### 3.3 Por que dois tipos (nota para o agente)

O design legado exigia hipótese prévia para qualquer missão — criando dependência circular: missão exige hipótese; hipótese exige análise; análise exige missão. Os dois tipos resolvem isso:
- Missão Exploratória quebra o paradoxo no ciclo inicial (sem hipótese)
- Missão de Validação aproveita informação de ciclos anteriores (com hipótese como contexto, não restrição)

### 3.4 Schema do objeto Missão (normalizado)

```json
{
  "ID": "string",
  "Tipo": "Exploratória | Validação",
  "Objetivo": "string",
  "Hipotese_entrada": "null | HypothesisObject",
  "Estado": "Criada | Planejada | Delegada | Executada | Validada | Consolidada | Encerrada | Cancelada",
  "Dependencias": ["MissionID"],
  "Agentes_envolvidos": ["AgentID"],
  "Prioridade": "Alta | Média | Baixa",
  "Prazo": "timestamp",
  "Resultado": "null | TMP"
}
```

`Hipotese_entrada` é obrigatoriamente `null` para Missões Exploratórias.

---

## PARTE 4 — ESCOPO DE TIMEFRAME POR AGENTE ANALÍTICO

Decisão complementar registrada nesta sessão:

| Agente | Escopo de timeframe | Justificativa |
|---|---|---|
| Structural Agent | MTF: S1 / D1 / H4 / H1 | Contexto macro estrutural |
| Institutional Agent | MTF: S1 / D1 / H4 / H1 | Contexto macro institucional |
| Operational Agent | Single TF: M5 apenas | Timeframe de entrada operacional |

**Regra normativa:** Skills de confluência multi-timeframe (confluence-fibonacci-skill, confluence-elliott, confluence-smc) são aplicáveis **apenas** ao Structural Agent e ao Institutional Agent. O Operational Agent não possui confluência MTF em suas skills.

---

## PARTE 5 — RESOLUÇÃO DO CLUSTER GOV-ORCH-001

Para fins de registro e rastreabilidade:

| Achado de auditoria | Status após estas decisões |
|---|---|
| GOV-ORCH-001: Master Orchestrator (LEGACY) | ✅ RESOLVIDO — eliminado; absorvido pelo Manager Agent |
| GOV-ORCH-001: Mission Engine (LEGACY) | ✅ RESOLVIDO — eliminado; absorvido pela Fase 0 |
| GOV-ORCH-001: Decision Orchestrator (LEGACY) | ✅ RESOLVIDO — eliminado; absorvido pelo Manager Agent |
| GOV-ORCH-001: Orchestration Layer (LEGACY) | ✅ RESOLVIDO — eliminado; absorvido pela Fase 1 |
| GOV-006: Orchestrator sem identidade taxonômica | ✅ RESOLVIDO — Manager Agent tem identidade precisa |
| GOV-007: Fronteiras Blackboard/Orchestrator incompletas | ⚠️ PARCIAL — fronteira Manager ↔ Blackboard definida aqui |

---

## PARTE 6 — DOCUMENTOS DE REFERÊNCIA

| Documento | Conteúdo |
|---|---|
| `claude_ADR-MANAGER-001_Manager_Agent_Architecture.md` | ADR formal do Manager Agent |
| `claude_ADR-MISSION-TYPES-001_Mission_Types.md` | ADR formal dos tipos de missão |
| `claude_ADR-CONFLUENCE-001_v3_Homologado.md` | ADR das confluence-skills (sessão anterior) |
| `AUDITORIA-ALINHAMENTO-GOVERNANCE-HARNESS.md` | Origem dos achados GOV-006, GOV-007 |
| `AUDITORIA-ALINHAMENTO-CANON-HARNESS.md` | Origem dos achados GOV-ORCH-001 |

---

## PARTE 7 — DECISÕES ABERTAS (NÃO INFERIR)

As seguintes decisões permanecem abertas e **não devem ser inferidas** pelo agente:

| ID | Descrição |
|---|---|
| J-001 | Conviction Vector — fórmula, pesos, thresholds |
| SPEC-015-SCOPE | Escopo detalhado e timing da SPEC-015 |
| EVENT-BUS-001 | Event Bus: existe? Como se distingue do Blackboard? |
| MISSION-TRIGGER-001 | Eventos de mercado específicos que disparam Missão Exploratória |
| MISSION-PLANB-001 | Estrutura e escopo do Plano B |
| MISSION-CAMPAIGN-001 | Definição formal de Campanha Operacional |
| ARR-ALAVANCAGEM-001 | Sugestão vs. parâmetro mandatório de alavancagem |

---

*ENTREGA 2 · HOC-003 · AEH · SOT SISTEMA TRADING · 2026-09-26*
