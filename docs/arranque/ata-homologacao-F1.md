# ATA DE HOMOLOGAÇÃO — Baseline F.1 do Harness SOT

**Data:** 2026-09-15
**Autoridade de homologação:** Andraus (Decisor Final / Consensus Authority)
**Registro:** Controlador (via Especificador — Claude Code)
**Instrução de origem:** "Homologar repo" (Andraus, 2026-09-15)

---

## 1. Objeto homologado

Estado do repositório após incorporação das 15 decisões do **Questionário de Resolução v1** (Andraus, 2026-09-14) e reorganização documental:

- **Camada F.1 (feedforward):** `governance/CONSTITUTION.md`, `governance/RULES.md`, `governance/CONFLICT-MAP.md`.
- **Emenda canônica:** `canon/CEE-001-cognitive-economy-efficiency-v2.0.md` (v2.0 — §11 Salvaguardas de Sinal + §12 Framework 4Es).
- **Documentos-raiz de método:** `ROADMAP.md`, `ATOMIC-SPEC.md` (v1.3), `GLOSSARIO.md`, `AGENTS.md`.
- **Modelos canônicos reconhecidos BASELINED:** CHM-001, CEM-001 (Q-001).
- **Catálogo:** `governance/CATALOGO-OFICIAL.md` (§6 Registro de Homologação).

## 2. Cadeia de aprovação (GMC-001 Cap.5)

| Etapa | Responsável | Estado |
|---|---|---|
| 1. Aplicação das decisões (Q-001…Q-015) | Especificador | ✅ Concluída |
| 2. Parecer de integridade | Revisor (independente, autor≠verificador) | ✅ **CONFORME** (2026-09-15) |
| 3. Consenso | Andraus (Decisor Final) | ✅ 2026-09-15 |
| 4. Registro Oficial | Controlador | ✅ Efetivado (Catálogo §6) |

## 3. Evidência de conformidade

- **Parecer do Revisor:** CONFORME — `docs/arranque/parecer-revisor-F1.md` (15/15 decisões CONFORME; CONS-01 respeitado; achado A01 corrigido e reverificado).
- **Conformidade mecânica:** `npm test` 11/11 schemas · `npm run lint` 5/5 specs · 0 required-files faltando · 0 referências quebradas · 0 resíduos de valores antigos em arquivos ativos.
- **Maturidade:** harness-score v1.6.5 — **L4 · Self-correcting · 102/108 (94%)**.

## 4. Decisões abertas remanescentes (não homologadas — seguem rastreadas)

J-001 (fórmula/pesos/limiares definitivos do Conviction Vector), G-001, H-001, I-001, K-001, L-001, C-001, M-001 (estados Blackboard p/ objetos não-hipótese), N-001 (pesos por ativo). Cada uma gateia a sua Spec futura (ver `ROADMAP.md`).

## 5. Efeito

O **gate de arranque BLOCO 4 / Q-011 está satisfeito**. A **SPEC-001 — Hypothesis Harness (sobre CHM-001)** fica **autorizada a iniciar** pelo fluxo Especificador → Revisor → Andraus. Nenhuma Spec posterior avança sem homologação individual.

## 6. Ressalvas registradas (não bloqueantes)

- `.harness-eval/runs/*` contêm valores pré-correção (histórico não normativo — A03).
- `canon/PPQ-001` referencia "Framework 3E do CEE-001" (texto de doc baselined; 4Es fixado por CEE-001 §12 e GLOSSARIO).
- CTX-04 do harness-score (frontmatter das `.clinerules/*`): quirk de detecção do scorer; regras já têm metadado válido — não corrigido deliberadamente para evitar duplicação/drift.
- Legados em `docs/_legacy/` preservados (exclusão adiada por decisão do usuário).

---

*Baseline F.1 homologada. Append-only: este registro não é removido, apenas superseded por versão futura.*
