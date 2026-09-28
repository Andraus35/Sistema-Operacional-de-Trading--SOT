# SOT-Harness

Harness de especificação do **SOT — Sistema Operacional de Trading**: sistema multiagente probabilístico de análise institucional para BTC, XAU e NASDAQ (Elliott Wave · Fibonacci · SMC · ICT).

Este repositório é a fonte de verdade da arquitetura cognitiva do SOT — organizado em pastas documentais para navegação e busca por agentes de IA.

> **Estado:** Spec-first (sem código). Decisões do **Questionário de Resolução v1** homologadas por Andraus em 2026-09-14 e incorporadas. Próximo trabalho autorizado: **SPEC-001 — Hypothesis Harness** (ver `ROADMAP.md`).

---

## Mapa do repositório

| Pasta / arquivo | O que contém | Comece por |
|---|---|---|
| **`ROADMAP.md`** | Sequência oficial de Specs, decisões abertas, caminho crítico | Leitura obrigatória |
| **`ATOMIC-SPEC.md`** | Método vigente (BASpec, D0–D9, Enforcement, etiquetagem) | Leitura obrigatória |
| **`AGENTS.md`** | Configuração/contexto do agente + não-negociáveis + mapa | Leitura obrigatória |
| **`GLOSSARIO.md`** | Identidade do sistema, equivalências de nomes, termos canônicos | Referência |
| **`governance/`** | Autoridade normativa F.1: `CONSTITUTION.md`, `RULES.md`, `CONFLICT-MAP.md`, `CATALOGO-OFICIAL.md` | Autoridade |
| **`canon/`** | Modelos canônicos **baselined** (CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR) — construir SOBRE, nunca redefinir | Contratos |
| **`docs/`** | Documentação de referência e histórica (não essencial à operação diária): `docs/fundamentos/` (KERNEL V2, ENGENHARIA GERAL, ARIA, AUDITORIA — TRACE-06), `docs/arranque/` (questionário + respostas de Andraus + manifesto), `docs/_legacy/` (superseded) | Pesquisa / histórico |
| **`specs/` · `rag/` · `schemas/`** | Harness operacional de 1ª geração dos 5 agentes — **referência**, será substituído pelas SPEC-010…014 | Reference |
| **`.claude/`** | `agents/` (especificador, revisor), `skills/`, `commands/` | Máquina |
| **`scripts/` · `tests/` · `.github/`** | `validate_spec_sot.py` (gate), validadores, CI | Máquina |

---

## Fluxo de especificação

```
ROADMAP + ATOMIC-SPEC → Especificador → Autopré-check → Revisor (gate + semântica) → Andraus homologa → approved/ → próxima Spec
```

## Build e validação

```bash
npm test            # 11 schemas JSON válidos
npm run lint        # EARS das 5 specs
python scripts/validate_spec_sot.py <plan.md>   # gate determinístico
npx harness-score   # maturidade do harness (opcional)
```

---

## Governança canônica

Autoridade única de homologação: **Andraus**. Fluxo de aprovação: **Especificador → Revisor → Andraus** (o fluxo de papéis do PPQ-001 foi supersedido; o dial GES permanece como referência de rigor). Estado/baseline de cada artefato: `governance/CATALOGO-OFICIAL.md`.

*Nada é deletado sem homologação; baselines só existem com registro explícito no Catálogo (INV-09).*
