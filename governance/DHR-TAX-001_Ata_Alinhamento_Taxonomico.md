# DHR-TAX-001 — Ata de Alinhamento Taxonômico — 4 Correções de Bloqueadores Críticos

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador / Revisor / Controlador |
| Ref | Auditoria Taxonômica 2026-09-25/26 — correções de alinhamento CRIT-003/CRIT-006/CRIT-007/GOV-005 |
| Data | 2026-09-26 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor (correções de alinhamento; textos históricos preservados inline — INV-07) |

---

## 1. Decisão

Quatro correções de alinhamento taxonômico foram **aplicadas e HOMOLOGADAS** em 2026-09-26. Todos os textos históricos foram preservados inline via comentários HTML (INV-07 respeitado em todas as 4 correções). Os achados de auditoria CRIT-003, CRIT-006, CRIT-007 e GOV-005 (parcial) estão encerrados.

---

## 2. Correção 1 — SDD-001: Conviction Vector 4D → 8D

| Campo | Valor |
|---|---|
| **Artefato** | `canon/SDD-001-spec-driven-development.md`, linha 147 |
| **Emenda** | SDD-001-EMENDA-001 |
| **Problema** | Checklist da SDD-001 referenciava "Conviction Vector 4D (Estrutural≥60%+...≥75% total)" — desatualizado desde Q-008 (dimensionalidade=8 fechada, Questionário v1, 2026-09-14) |
| **Correção** | Texto substituído para: "respeita o Conviction Vector **8D** (convicção ≥ 70%, score ≥ 7/9 — Fase Piloto, Q-008/Q-002)"; texto legado "4D (Estrutural≥60%+...≥75% total)" preservado em comentário HTML inline |
| **Autoridade** | Q-008 (8 dimensões) + Q-002 (limiares Fase Piloto, recalibráveis após backtest) |
| **Achado encerrado** | CRIT-003 |
| **Status** | ✅ APLICADO — verificado em `canon/SDD-001-spec-driven-development.md:147` |

---

## 3. Correção 2 — CATÁLOGO-OFICIAL.md §7: Trilha B SPEC-002 → SPEC-019

| Campo | Valor |
|---|---|
| **Artefato** | `governance/CATALOGO-OFICIAL.md`, §7 tabela modelo arquitetural (Trilha B) |
| **Problema** | Tabela da Trilha B listava "Próximo artefato = SPEC-002" — desatualizado desde DHR-EUA-E17 (2026-09-21) que interpôs a FASE GOV e designou SPEC-019 como próxima |
| **Correção** | Tabela atualizada: "Próximo artefato = **SPEC-019**" refletindo estado pós-DHR-EUA-E17; anotação histórica "LEGADO snapshot anterior = SPEC-002; substituído por DHR-EUA-E17" preservada em comentário HTML inline |
| **Autoridade** | DHR-EUA-E17 (2026-09-21) + ROADMAP.md (SPEC-019 HOMOLOGADA, próximo = SPEC-020 núcleo A) |
| **Achado encerrado** | CRIT-006 |
| **Status** | ✅ APLICADO — verificado em `governance/CATALOGO-OFICIAL.md:38` |

---

## 4. Correção 3 — CONSTITUTION.md: Mission Engine / Master Orchestrator marcados LEGADO

| Campo | Valor |
|---|---|
| **Artefato** | `governance/CONSTITUTION.md`, linhas 93–95 (diagrama de pipeline) |
| **Problema** | Diagrama de pipeline listava "Mission Engine" e "Master Orchestrator" como componentes ativos — eliminados e absorvidos pelo Manager Agent per ADR-MANAGER-001 (HOC-003, 2026-09-26) |
| **Correção** | Duas linhas de comentário HTML inline inseridas: `<!-- [LEGADO 2026-09-26] Mission Engine → ELIMINADO; absorvido pelo Manager Agent Fase 0 (ADR-MANAGER-001, HOC-003) -->` e `<!-- [LEGADO 2026-09-26] Master Orchestrator → ELIMINADO; absorvido pelo Manager Agent (ADR-MANAGER-001, HOC-003) -->` (linhas 93–94); linha 95 atualizada para "Manager Agent (Fase 0: Mission Lifecycle → Fase 1: Dispatch → Fase 2: Conviction)" |
| **Autoridade** | ADR-MANAGER-001 (DHR-ADR-HOC003, 2026-09-26) |
| **Achado encerrado** | CRIT-007 |
| **Status** | ✅ APLICADO — verificado em `governance/CONSTITUTION.md:93-95` |

---

## 5. Correção 4 — synthesis.output.json: score_total com rótulo PILOT e J-001 explicitado

| Campo | Valor |
|---|---|
| **Artefato** | `schemas/synthesis.output.json`, campo `score_total` |
| **Problema** | Campo `score_total` sem rótulo "Fase Piloto" e sem referência explícita à decisão aberta J-001/CCM-001 — criava falsa impressão de que a relação score↔conviction_vector está fechada; guard contra fusão indevida ausente |
| **Correção** | `description` do campo atualizado: rótulo "PILOT (Q-002/Alinhamento Taxonômico 2026-09-26)" + texto completo da relação com conviction_vector + guard "Não substituir nem fundir com conviction_vector sem decisão homologada"; `$comment` adicionado: decisão de precedência score vs conviction_vector = ABERTA (J-001/CCM-001); referência TAX-SCHEMA-001 |
| **Autoridade** | Q-002 (limiares Fase Piloto, recalibráveis) + J-001 (aberta — CONS-01) + Andraus 2026-09-26 |
| **Achado encerrado** | GOV-005 (parcial — modelo de relação score↔conviction pendente de J-001/CCM-001) |
| **Status** | ✅ APLICADO — verificado em `schemas/synthesis.output.json:score_total` |

---

## 6. Sumário de achados encerrados

| Achado | Correção | Status |
|---|---|---|
| CRIT-003: SDD-001 Conviction Vector 4D (desatualizado) | Correção 1 | ✅ ENCERRADO |
| CRIT-006: CATÁLOGO §7 Trilha B SPEC-002 stale | Correção 2 | ✅ ENCERRADO |
| CRIT-007: CONSTITUTION.md Mission Engine/Master Orchestrator ativos | Correção 3 | ✅ ENCERRADO |
| GOV-005: score_total sem rótulo piloto / J-001 implícita | Correção 4 | ✅ ENCERRADO (parcial — relação formal pendente de J-001/CCM-001) |

---

## 7. Decisões que permanecem ABERTAS (CONS-01 — não fechadas por esta ata)

J-001 (Conviction Vector — fórmula/pesos/limiares definitivos) · CCM-001 (modelo de relação score↔conviction — pendente de redação).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
