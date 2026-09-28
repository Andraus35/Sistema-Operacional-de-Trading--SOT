# DHR-ADR-HOC003 — Ata de Homologação — Cluster HOC-003 (Auditoria Taxonômica 2026-09-25/26)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador / Revisor / Controlador |
| Ref | AEH HOC-003 — ADR-MANAGER-001 + ADR-MISSION-TYPES-001 + ADR-CONFLUENCE-001 v3 |
| Data | 2026-09-26 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | MAJOR (arquitetura de orquestração; nomenclatura normativa; GOV-ORCH-001 RESOLVIDA) |

---

## 1. Decisão

O cluster **HOC-003** está **HOMOLOGADO**. Três ADRs foram aprovadas por Andraus em 2026-09-25/26 como resultado da Auditoria Taxonômica (achado GOV-ORCH-001/CRIT-004). Estas decisões são **normativas e de vigência imediata** — specs futuras e documentação revisional devem conformar a este baseline.

---

## 2. ADR-MANAGER-001 — Manager Agent: Arquitetura Unificada de Orquestração

### 2.1 Componentes legados eliminados

Os seguintes componentes são eliminados como entidades arquiteturais independentes; suas responsabilidades são absorvidas pelo Manager Agent:

| Componente eliminado | Absorvido por |
|---|---|
| Master Orchestrator | Manager Agent |
| Mission Engine | Manager Agent Fase 0 (Mission Lifecycle) |
| Decision Orchestrator | Manager Agent |
| Orchestration Layer | Manager Agent Fase 1 (Dispatch) |
| Agente Decisor | Manager Agent Fase 2 (Conviction) |
| Agente de Síntese | Manager Agent Fase 2 (Conviction) |

**FATO NORMATIVO:** Nenhum destes nomes deve aparecer em specs futuras como componente independente.

### 2.2 Manager Agent — arquitetura em 3 Fases

```
MANAGER AGENT
├── FASE 0: MISSION LIFECYCLE
│   Monitora triggers; decide tipo de missão; cria/gerencia ciclo de vida; Plano B
│
├── FASE 1: DISPATCH (mecânica/determinística)
│   Resolve grafo de dependências; despacha agentes analíticos; sem julgamento analítico
│
└── FASE 2: CONVICTION (cognitiva leve)
    Lê Vetores de Convicção do Blackboard; arbitra conflitos; forma Convicção Global; gera TMP
```

**Fluxo arquitetural completo:**
```
Market Digital Twin → Manager Agent (F0) → Agentes Analíticos → Blackboard
                                                                      ↓
                          Bot Trade Finance ← TMP ← Manager Agent (F1 + F2)
```

**Manager Agent NÃO:** analisa mercado · formula hipóteses de mercado · possui skills N8-N17 de análise técnica.

**SPEC de referência:** SPEC-015.

---

## 3. ADR-MISSION-TYPES-001 — Dois Tipos de Missão

Existem exatamente **dois tipos** de missão no SOT:

| Tipo | Hipótese entrada | Trigger | Comportamento agentes | Output |
|---|---|---|---|---|
| **Missão Exploratória** | `null` (nenhuma) | Evento de mercado / abertura de sessão / invalidação de hipótese anterior | Formulam hipóteses livremente | Hipótese dominante emerge da Fase 2 → TMP |
| **Missão de Validação** | SIM (hipótese dominante do ciclo anterior) | Conclusão de Missão Exploratória com hipótese dominante | Validam ou refutam a tese | TMP atualizado; se refutada → Plano B → nova Missão Exploratória |

**Resolução do paradoxo circular (identificado por Andraus):** o design legado exigia hipótese antes da análise; a análise é que gera hipóteses → dependência circular. Missão Exploratória quebra o ciclo inicial (sem hipótese). Missão de Validação aproveita informação de ciclos anteriores (hipótese como contexto, não restrição).

**Extensão normativa do schema Missão:** campos `Tipo: "Exploratória | Validação"` e `Hipotese_entrada: null | HypothesisObject` adicionados ao schema legado (DCEBS Doc 13). `Hipotese_entrada` é obrigatoriamente `null` para Missões Exploratórias.

---

## 4. ADR-CONFLUENCE-001 v3 — Skills de Confluência e Nomenclatura do Structural Agent

### 4.1 Skills extintas / renomeadas

| Elemento legado | Situação | Substituto normativo |
|---|---|---|
| `fractal-skill` | **EXTINTA** | `confluence-elliott` |
| `fibonacci-skill` (skill única) | **EXTINTA** | `level-fibonacci-skill` + `confluence-fibonacci-skill` |
| FCE (Fractal Confluence Engine) | Conceito absorvido | `confluence-elliott` |

### 4.2 Catálogo normativo do Structural Agent (4 skills)

| Skill | Função |
|---|---|
| `elliott-skill` | Contagem e score Elliott por grade (MTF: S1/D1/H4/H1) |
| `level-fibonacci-skill` | Valida Elliott com níveis Fibonacci; extensível a outras matérias futuras |
| `confluence-fibonacci-skill` | Mede confluência de níveis Fibonacci entre timeframes (MTF: S1/D1/H4/H1) |
| `confluence-elliott` | Mede confluência das hipóteses Elliott entre timeframes (MTF: S1/D1/H4/H1) |

### 4.3 Confluence-skills por agente (regra de escopo)

| Skill | Agente | Escopo |
|---|---|---|
| `confluence-elliott` | Structural Agent | MTF: S1/D1/H4/H1 |
| `confluence-smc` | Institutional Agent | MTF: S1/D1/H4/H1 |
| `confluence-ict` | Operational Agent | Single TF: M5 (confluência intra-M5, não MTF) |

**Regra normativa:** confluência é interna à matéria de cada agente. Nenhuma confluence-skill cruza matérias de agentes distintos. Confluence-skills MTF são exclusivas do Structural e Institutional Agent — o Operational Agent não possui confluência MTF em suas skills.

---

## 5. Achados de auditoria resolvidos

| Achado (GOV-ORCH-001) | Status após HOC-003 |
|---|---|
| Master Orchestrator LEGACY | ✅ RESOLVIDO — eliminado; absorvido pelo Manager Agent |
| Mission Engine LEGACY | ✅ RESOLVIDO — eliminado; absorvido pela Fase 0 |
| Decision Orchestrator LEGACY | ✅ RESOLVIDO — eliminado; absorvido pelo Manager Agent |
| Orchestration Layer LEGACY | ✅ RESOLVIDO — eliminado; absorvido pela Fase 1 |
| Agente Decisor LEGACY | ✅ RESOLVIDO — eliminado; absorvido pela Fase 2 |
| Agente de Síntese LEGACY | ✅ RESOLVIDO — eliminado; absorvido pela Fase 2 |
| GOV-006: Orchestrator sem identidade taxonômica | ✅ RESOLVIDO — Manager Agent tem identidade precisa (3-fases) |
| GOV-007: Fronteiras Blackboard/Orchestrator incompletas | ⚠️ PARCIAL — fronteira Manager Agent ↔ Blackboard definida aqui; EVENT-BUS-001 = decisão aberta |

---

## 6. Nota de nomenclatura (ADR-CONFLUENCE-001 v3 × ADR-MANAGER-001)

ADR-CONFLUENCE-001 v3 foi redigida antes de ADR-MANAGER-001 e usa o termo "Agente Decisor" para o componente de síntese de convicções. ADR-MANAGER-001 consolidou este componente como **Manager Agent Fase 2 (Conviction)**. O termo normativo vigente é "Manager Agent Fase 2 (Conviction)" per ADR-MANAGER-001 — "Agente Decisor" é histórico/legado (INV-07).

---

## 7. Documentos-fonte desta ata

| Documento | Localização |
|---|---|
| ADR-MANAGER-001 | `governance/ADR-MANAGER-001_Manager_Agent_Architecture.md` |
| ADR-MISSION-TYPES-001 | `governance/ADR-MISSION-TYPES-001_Mission_Types.md` |
| ADR-CONFLUENCE-001 v3 | `governance/ADR-CONFLUENCE-001-v3_Skills_Confluence_Architecture.md` |
| Instrução Entrega 2 (E2-HOC003) | `docs/_legacy/claude_E2-HOC003-Manager-Agent-Mission-Types.md` |
| Material da Auditoria Taxonômica | `docs/_legacy/AUDITORIA-TAXONOMICA/` |

---

## 8. Decisões que permanecem ABERTAS (CONS-01 — não fechadas por esta ata)

J-001 · SPEC-015-SCOPE · EVENT-BUS-001 · MISSION-TRIGGER-001 · MISSION-PLANB-001 · MISSION-CAMPAIGN-001 · ARR-ALAVANCAGEM-001.

---

## 9. Próximo passo

Specs futuras (a partir de SPEC-015) devem implementar a arquitetura Manager Agent 3-fases e os dois tipos de missão. O caminho crítico imediato é **SPEC-020 (núcleo A)** — não alterado por estas decisões.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
