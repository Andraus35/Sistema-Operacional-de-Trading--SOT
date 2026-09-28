# ADR-MANAGER-001 — Manager Agent: Arquitetura Unificada de Orquestração
**Versão:** 1.0  
**Status:** HOMOLOGADO  
**Data:** 2026-09-26  
**Decisor:** Andraus  
**AEH:** HOC-003  
**Resolve:** GOV-ORCH-001 (CRIT-004)

---

## 1. CONTEXTO

### 1.1 Problema identificado

A auditoria GOV-ORCH-001 (CRIT-004) identificou o seguinte cluster de componentes com status `LEGACY/UNRESOLVED`:

| Componente legado | Status anterior |
|---|---|
| Master Orchestrator | LEGACY/UNRESOLVED |
| Mission Engine | LEGACY/UNRESOLVED |
| Decision Orchestrator | LEGACY/UNRESOLVED |
| Orchestration Layer | LEGACY/UNRESOLVED |
| Agente Decisor | LEGACY/UNRESOLVED |
| Agente de Síntese | LEGACY/UNRESOLVED |

Estes componentes surgiram em documentos de engenharia distintos (GAS Doc 03, MOES Doc 09, DCEBS Doc 13) ao longo do desenvolvimento do SOT, mas nunca foram reconciliados entre si nem alinhados ao paradigma do Harness Cognitivo por Especificação.

### 1.2 Tensão central

O paradigma legado assumia que:
- Uma **hipótese prévia** dispara uma missão
- O Mission Engine gerencia o ciclo de missões
- Um agente separado (Agente Decisor / Agente de Síntese) consolida os outputs analíticos

O paradigma atual (Harness Cognitivo) exige:
- Agentes analíticos **formulam** hipóteses como parte da análise — não recebem hipótese como input único
- Orquestração é determinística / mecânica — não cognitiva adicional
- Ciclo de missões deve ser gerenciado sem criar um novo agente cognitivo pesado

### 1.3 Paradoxo circular (identificado por Andraus)

> "Qual a razão de ter hipótese antes de haver análise dos agentes? Não são os agentes que tratarão evidências, formularão hipóteses e formarão convicção?"

O design legado criava dependência circular: para criar missão → precisa de hipótese; para formular hipótese → precisa dos agentes; para despachar agentes → precisa de missão. Esse paradoxo foi o motivador central desta ADR.

---

## 2. DECISÃO

### 2.1 Componentes absorvidos (eliminados como entidades separadas)

Os seguintes componentes são **eliminados** como entidades arquiteturais independentes e suas responsabilidades são **absorvidas** pelo Manager Agent:

- ~~Master Orchestrator~~ → absorvido
- ~~Mission Engine~~ → absorvido (Fase 0)
- ~~Decision Orchestrator~~ → absorvido
- ~~Orchestration Layer~~ → absorvido (Fase 1)
- ~~Agente Decisor~~ → absorvido (Fase 2)
- ~~Agente de Síntese~~ → absorvido (Fase 2)

**FATO NORMATIVO:** Nenhum destes nomes deve aparecer em specs futuras como componente independente.

### 2.2 Manager Agent — Definição

O **Manager Agent** é o único componente de orquestração do SOT SISTEMA TRADING. Não é um agente cognitivo analítico — não analisa mercado, não formula hipóteses de mercado. É um agente de **gestão de missões e convicções**.

### 2.3 Arquitetura em 3 Fases

```
MANAGER AGENT
├── FASE 0: MISSION LIFECYCLE
│   Monitora: triggers de mercado / hipóteses de ciclos anteriores
│   Decide: tipo de missão (Exploratória ou Validação)
│   Cria e gerencia: ciclo de vida de missões
│   Gerencia: portfólio de missões paralelas
│   Cria: Campanhas Operacionais quando aplicável
│   Gera: Plano B quando hipótese é invalidada
│
├── FASE 1: DISPATCH (mecânica/determinística)
│   Resolve: grafo de dependências entre submissões
│   Despacha: agentes analíticos na ordem correta
│   Monitora: publicações no Blackboard
│
└── FASE 2: CONVICTION (cognitiva — leve)
    Lê: Vetores de Convicção do Blackboard
    Arbitra: conflitos entre agentes
    Forma: Convicção Global
    Gera: Trading Mission Package (TMP)
```

### 2.4 Fluxo arquitetural completo

```
Market Digital Twin
      ↓
MANAGER AGENT (Fase 0: Mission Lifecycle)
      ↓
┌─────────────────────────────────────┐
│  Structural Agent   [MTF: S1/D1/H4/H1] → Blackboard
│  Institutional Agent [MTF: S1/D1/H4/H1] → Blackboard
│  Operational Agent  [Single TF: M5]    → Blackboard
└─────────────────────────────────────┘
      ↓
BLACKBOARD ──────────→ Manager Agent (Fase 1 + Fase 2)
      ↓
Trading Mission Package (TMP)
      ↓
Bot Trade Finance
```

### 2.5 Distinção crítica: cognitivo vs. mecânico

| Fase | Tipo | Justificativa |
|---|---|---|
| Fase 0 — Mission Lifecycle | Decisório leve | Decide tipo de missão com base em estado de mercado; não analisa mercado diretamente |
| Fase 1 — Dispatch | Mecânico/determinístico | Resolve grafo de dependências; sem julgamento analítico |
| Fase 2 — Conviction | Cognitivo leve | Arbitra convicções; não formula hipóteses de mercado |

**FATO NORMATIVO:** Manager Agent **não** é um agente analítico. Não analisa mercado. Não possui skills de análise técnica. Seus domínios são: gestão de missões, orquestração de despacho, síntese de convicções.

---

## 3. JUSTIFICATIVA

### 3.1 Por que unificar em um único componente

- Elimina ambiguidade taxonômica entre 6 componentes legados
- Mantém separação clara entre *orquestração* (Manager) e *análise* (agentes analíticos)
- Permite gestão coesa do ciclo de missões sem dependências circulares
- Alinha com o princípio do Harness Cognitivo: agentes analíticos são autônomos em sua análise

### 3.2 Por que manter cognição leve na Fase 2

A síntese de Vetores de Convicção não é mecânica — requer arbitragem quando há conflito entre agentes. Porém, esta cognição é restrita ao meta-nível (quem tem mais convicção, com quais evidências) e nunca desce ao nível de análise de mercado. Por isso: cognitivo *leve*, não um novo agente analítico completo.

### 3.3 Alinhamento com Harness Cognitivo

O Harness Cognitivo exige que cada agente analítico tenha N8-N17 especializadas por seu domínio. O Manager Agent **não** está sujeito às mesmas camadas analíticas — suas camadas serão especificadas na SPEC-015 em conformidade com seu papel de orquestração.

---

## 4. CONSEQUÊNCIAS

### 4.1 Consequências imediatas

- GOV-ORCH-001 (CRIT-004) → **RESOLVIDO** por esta ADR
- GOV-006 (Orchestrator sem identidade taxonômica estável) → **RESOLVIDO**
- GOV-007 (fronteiras Blackboard/Event Bus/Orchestrator incompletas) → **PARCIALMENTE RESOLVIDO** (fronteira Manager Agent ↔ Blackboard definida aqui; Event Bus = decisão aberta)

### 4.2 Specs afetadas

| Spec | Impacto |
|---|---|
| SPEC-015 | Deve especificar Manager Agent com esta arquitetura 3-fases |
| Qualquer spec que mencionasse componentes legados | Deve referenciar Manager Agent |

### 4.3 Nomenclatura normalizada

A partir desta ADR, a nomenclatura normativa é:

| Fase | Nome normativo |
|---|---|
| Manager Agent Fase 0 | Mission Lifecycle |
| Manager Agent Fase 1 | Dispatch |
| Manager Agent Fase 2 | Conviction |

---

## 5. ALTERNATIVAS CONSIDERADAS E REJEITADAS

### A1: Manter Mission Engine como componente separado
**Rejeitada.** Criaria dependência circular (missão precede análise; análise gera hipótese; hipótese dispara missão). Identificado por Andraus.

### A2: Criar novo agente cognitivo pesado para síntese
**Rejeitada.** "Não deve ser um agente cognitivo. Já há muitos." (Andraus, 2026-09-26). Parcimônia arquitetural.

### A3: Manter Agente Decisor separado do orquestrador
**Rejeitada.** "Se substituirmos o Agente Decisor por Manager Agent ele poderia tanto distribuir as missões quanto recolher as convicções." (Andraus, 2026-09-26). Fusão é mais coesa.

---

## 6. ESTADO DOS ACHADOS DE AUDITORIA RESOLVIDOS

| Achado | Status anterior | Status após esta ADR |
|---|---|---|
| GOV-ORCH-001 Master Orchestrator | LEGACY/UNRESOLVED | ✅ RESOLVIDO — eliminado; absorvido pelo Manager Agent |
| GOV-ORCH-001 Mission Engine | LEGACY/UNRESOLVED | ✅ RESOLVIDO — eliminado; absorvido pela Fase 0 |
| GOV-ORCH-001 Decision Orchestrator | LEGACY/UNRESOLVED | ✅ RESOLVIDO — eliminado; absorvido pelo Manager Agent |
| GOV-ORCH-001 Orchestration Layer | LEGACY/UNRESOLVED | ✅ RESOLVIDO — eliminado; absorvido pela Fase 1 |
| GOV-006 (Orchestrator sem identidade) | ABERTO | ✅ RESOLVIDO — Manager Agent tem identidade precisa |
| GOV-007 (fronteiras incompletas) | ABERTO | ⚠️ PARCIAL — Blackboard ↔ Manager Agent definido; Event Bus pendente |

---

## 7. DECISÕES ABERTAS RELACIONADAS

| ID | Descrição | Status |
|---|---|---|
| J-001 | Conviction Vector — fórmula, pesos, thresholds | Aberta (SPEC-015) |
| SPEC-015-SCOPE | Escopo detalhado da SPEC-015 para Manager Agent | Aberta |
| EVENT-BUS-001 | Event Bus: existe? Como se distingue do Blackboard? | Aberta |

---

*ADR-MANAGER-001 v1.0 · HOMOLOGADO por Andraus · 2026-09-26 · HOC-003*
