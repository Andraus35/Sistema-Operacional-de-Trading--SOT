# Mixed apply plan (Track C)

> Run dir: `/home/user/Sistema-Operacional-de-Trading--SOT/.harness-eval/runs/2026-10-31-agents`
> Judges: J1 model=`claude-sonnet-5-5` · J2 model=`claude-sonnet-5-5`
> **This file is the only Mixed apply input.** Do not re-judge usefulness.

## What these words mean

| Word | Meaning | Apply must |
|------|---------|------------|
| **KEEP** | Text from judge Keep-core columns | Remain in the harness surface as rule/snippet |
| **CUT** | Text from judge Slim columns | Delete or compress only this bulk |
| **Apply** | Mechanical edit | Not a new design pass |

## Hard rules for apply agents

1. For each Mixed ID below, edit **only** that path.
2. **KEEP** items must survive (same contract — concern/module/section/checklist).
   Do not replace a KEEP teaching snippet with a weaker pattern.
3. **CUT** only what both judges' Slim columns describe (or the union when both
   clearly name the same bulk). If KEEP and CUT conflict, **skip that path** (Hold).
4. Never replace a fenced teaching snippet with `See app/...` / `lib/...` / `test/...`.
5. Never defer KEEP content to AGENTS.md or another surface unless CUT explicitly
   names OVERLAP with that path **and** KEEP still retains the behavior contract.
6. Do not open the repo to invent a different convention than KEEP states.
7. After edits: every KEEP bullet must still be satisfied by the file text.

## Paths (1)

### S001 — `AGENTS.md`

- Tier: `T0` · Name: `AGENTS.md`
- Overall: J1 `MIXED` · J2 `MIXED`

#### KEEP (do not remove or degrade)

- **J1:** BEHAVIOR-CHANGING: KEEP §1 tabela de leitura obrigatória + regra "faltou ROADMAP/atomic-spec -> Especificador para / Revisor NÃO CONFORME Crítica". BEHAVIOR-CHANGING: KEEP §3 (tabela AC com tools, fronteira AC/AT §3.3, ENF-03). BEHAVIOR-CHANGING: KEEP §4 profiles pinados. BEHAVIOR-CHANGING: KEEP §5 fluxo (Especificador->Autopré-check->Revisor->validate_spec_sot.py->Andraus), regra "VERIFY != CONFORME != homologação", Abertura de Spec/Dossiê fail-closed e regra de manter `docs/mapa/` via `build_map.py`. BEHAVIOR-CHANGING: KEEP §6 não-negociáveis 1-12 (R:R, limiares, 8 dimensões, ICT não cria hipótese). BEHAVIOR-CHANGING: KEEP §7 só a lista curta de decisões ATIVAS e a regra "nenhuma decisão aberta como invariante (CONS-01)". BEHAVIOR-CHANGING: KEEP §10 (o que exige decisão expressa de Andraus) e §11 (ler HANDOFF.md antes de agir). KEEP §8 só comandos de uso diário (npm test, validate_spec_sot, check_refs, build_map --check).
- **J2:** BEHAVIOR-CHANGING: KEEP §1 (mandatory reads ROADMAP.md/atomic-spec.md/WORKFLOW.md + fail-closed rule if missing); §3 table (AC tools, Revisor read-only, ENF-03) and §3.3 AC/AT frontier; §4 pinned depth profiles (LOW..CRITICAL, not elevated silently); §5 flow block + validate_spec_sot.py gate + "VERIFY != CONFORME != homologação" + Abertura de Spec/Dossiê fail-closed paragraph; §6 items 1-12 (non-negotiables: R:R, thresholds, 8 dimensions, hierarchy); §7 only the one-line list of ACTIVE open decisions (J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001) + final CONS-01 sentence; §8 command list; §10 merge/assinatura rule; §11 first bullet (read HANDOFF.md, reverify live).

#### CUT (only this bulk)

- **J1:** OVERLAP: CUT §7 histórico narrativo de decisões FECHADAS (H-001, I-001, L-001, Q-A5/Q-A9, SPEC-003/005 homologadas, RULE-REG-001, ECC-VAL-001, etc.); manter só lista de ABERTAS e apontar ao ROADMAP. OVERLAP: CUT §5 parágrafo "Sincronização documental" (detalhes a-e de check_doc_sync) e menção RULE-ECC-06/STRUCT-12; já em `governance/MECANISMOS.json`. OVERLAP: CUT §8 comandos secundários (check_rpsa, check_invariants, revisor_gate*, loop_ledger, check_coesao, check_handoff); `governance/MECANISMOS.json` é registro único de estado. OVERLAP: CUT §2 árvore de diretórios (usar `ls`; `docs/mapa/MAPA-PROJETO.md` já indexa). THEORY/OVERLAP: CUT §9 Auditor Externo PAUSADO (inerte; ver `governance/MECANISMOS.json`). OVERLAP: CUT §12 passos 0-5 do LOOP-001 (detalhe de textos "intermediários preservados"); manter 1 linha-ponteiro. OVERLAP: CUT §3.1 nota dos subagentes aposentados e §6 item 9 parênteses históricos (DHR-ARQ-002, EUA-E19a).
- **J2:** OVERLAP: CUT from §7 the long closed-decision history (H-001, I-001, L-001, Q-A5, Q-A9, RISK-*, REG-001, EVENT-BUS-001, DHR narratives and struck-through preserved text) — ROADMAP.md "Decisões FECHADAS" is the SSoT. THEORY/OVERLAP: CUT §5 "Mapa do projeto (BL-019)" paragraph to one line ("after editing .md run python scripts/build_map.py; never edit docs/mapa/") and §5 "Sincronização documental" paragraph to one line (script name + informative). ROUTING-ONLY/REPO-DEMONSTRATED: CUT §2 directory tree (keep only the docs/mapa/MAPA-PROJETO.md pointer sentence); agent can ls the repo. OVERLAP: CUT §9 Auditor Externo (PAUSADO, inert) to a single "paused, do not use" line. OVERLAP: CUT §12 to items 1-5 headline rules and drop preserved superseded intermediate text ([texto intermediário preservado...]). CUT §11 bullets 4-5 (Fase 2 hooks, anexo de tarefa) to a pointer.

#### Overlap cites (context only; cut OVERLAP here only if listed under CUT)

- **J1:** OVERLAP: `ROADMAP.md` (seção "Decisões FECHADAS" e linha "Decisões abertas ativas" - o próprio §7 declara que o ROADMAP prevalece); `governance/MECANISMOS.json` (estado de scripts/hooks); `docs/mapa/MAPA-PROJETO.md` e `docs/agentes/INDICE-AGENTES.md` (mapa/índice); `governance/RULES.md` RULE-006 (R:R 1:3, confirma §6.5 mas AGENTS.md é o ponto de carga); `.claude/agents/revisor.md` e `.claude/agents/especificador.md` (tools/papéis, parcialmente duplicados em §3)
- **J2:** OVERLAP: governance/MECANISMOS.json (state of scripts/hooks, §8 tail), ROADMAP.md (open/closed decisions §7; Spec sequence), docs/mapa/MAPA-PROJETO.md (repo layout §2), governance/CATALOGO-OFICIAL.md (baseline), .claude/agents/especificador.md and .claude/agents/revisor.md (tool lists in §3), .clinerules/sot-map.md (map rule §5)

---

