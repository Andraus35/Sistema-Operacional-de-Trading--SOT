# Track C — Surface deck (usefulness)

> run: 2026-09-11-full
> generated: 2026-09-12T03:58:14.961335+00:00
> model note: usefulness is model-sensitive; record judge model ids in score files.

## Rubric (score every surface including S9xx)

Counterfactual: if this surface were deleted, and the agent could still list the repo and open 1–2 canonical examples, would behavior change?

| Overall class | Meaning |
|---------------|---------|
| KEEP-CORE | Majority of substance is BEHAVIOR-CHANGING (wrong file placement, wrong API, skipped gates without it) |
| MIXED | Meaningful keep-core core + large slimable theory/examples/overlap |
| SLIM | Mostly THEORY, REPO-DEMONSTRATED, or OVERLAP — compress or delete body |
| ROUTING-ONLY | Trigger/purpose/pointers only; keep short |
| UNCLEAR | Insufficient evidence (use when model prior is doing the work) |

Section tags to use inside Keep-core / Slim columns: `BEHAVIOR-CHANGING`, `REPO-DEMONSTRATED`, `THEORY`, `OVERLAP`, `ROUTING-ONLY`.

Hard rules:
- Evidence-or-zero: cite paths (harness or example code). No README as evidence.
- OVERLAP must cite the other harness surface path.
- REPO-DEMONSTRATED must cite a concrete example file an agent would open (score Evidence only — not a path to paste into the skill when trimming).
- Default UNCLEAR when unsure. Do not mark SLIM on methodology skills without evidence.
- Score every ID including S9xx with the same rubric.

## Surfaces (9)

### S001 | T0 | AGENTS.md

- path: `AGENTS.md`
- chars: 3682
- outline:
- SOT-Harness — Agent Context
  - What this project is
  - Directory layout
  - Build and validation
- Validate all JSON schemas are valid JSON
- Lint Markdown spec files for EARS notation completeness
- Run full harness quality score
- Run qualitative harness evaluation
- (requires @tech-leads-club/agent-skills installed)
  - Architecture — 5 specialist agents
  - Inviolable methodology hierarchy
  - Constitutional rules agents must never violate
  - Spec conventions agents must follow
  - Source documents

```markdown
# SOT-Harness — Agent Context

## What this project is

The SOT-Harness is the formal specification harness for the **Sistema de Operações e Tendências (SOT)** — a multi-agent probabilistic trading system for BTC, XAU, and NASDAQ using Elliott Wave, Fibonacci, SMC, and ICT methodologies.

This harness is the source of truth for AI agents implementing or modifying the SOT system. All agent behavior, I/O contracts, rules, and conflict resolution logic are defined here.

## Directory layout

```
SOT-Harness/
├── CONSTITUTION.md      — 14 cognitive principles, methodology hierarchy, execution sequence
├── RULES.md             — 40+ numbered rules, each citing its source document
├── CONFLICT-MAP.md      — Directional, fractal, timing, conviction conflict tables
├── specs/               — One spec file per agent (EARS notation, behaviors, acceptance criteria)
├── schemas/             — JSON Schema Draft-07 for all agent I/O (10 files)
├── rag/                 — RAG knowledge bases (chunked Markdown for embedding)
└── HARNESS-REPORT.md    — Audit trail, gaps, source inventory
```

## Build and validation

```bash
# Validate all JSON schemas are valid JSON
npm test

# Lint Markdown spec files for EARS notation completeness
npm run lint

# Run full harness quality score
npx harness-score
npx harness-score --json --diff

# Run qualitative harness evaluation
# (requires @tech-leads-club/agent-skills installed)
npm run eval
```

## Architecture — 5 specialist agents

| Agent | Responsibility | Input | Output |
|---|---|---|---|
| Elliott Specialist | Wave count, bias, regime, invalidation | market_digital_twin + webhook | elliott-wave.output |
| Fibonacci Validator | Geometric validation, OTE, projections | elliott_hypothesis + pivots | fibonacci.output |
| SMC Specialist | Order Blocks, CHoCH, BOS, Dual Narrative | elliott_hypothesis + luxalgo | smc.output |
| ICT Specialist | Killzones, Judas Swing, entry plan | approved_hypothesis + session | ict.output |
| Synthesis Agent | Final arbitration, score 0-9, signal | all 4 specialist outputs | synthesis.output |

## Inviolable methodology hierarchy

```
1. Elliott Wave  (map — always first)
2. Fibonacci     (geometric ruler — validates Elliott)
3. Fractal       (multi-timeframe coherence)
4. SMC           (institutional confirmation only)
5. ICT           (execution only — last, never first)
```

Lower layers CANNOT override higher layers. ICT never creates hypotheses. SMC never corrects Elliott.

## Constitutional rules agents must never violate

1. ICT Specialist stays INACTIVE unless a structural hypothesis is approved
2. No directional signal when `directional_conflict = true` between Elliott and SMC
3. R:R minimum 2:1 — no exceptions, even at score 9/9 + conviction 100%
4. Conviction global threshold: ≥ 70% for signal, ≥ 60% for bias emission
5. Score matrix: Elliott(0-3) + SMC(0-3) + ICT(0-3) ≥ 7/9 required for signal

## Spec conventions agents must follow

- All acceptance criteria use EARS notation: "Quando <condição>, o agente DEVE <resposta>"
- Source document must be cited in every rule (format: `<!-- Fonte: DOC §N -->`)
- Every behavior file must declare: Missão, Escopo, Antiescopo, Comportamentos, Critérios
- Schema files must be valid JSON Schema Draft-07 with `$schema` and `$id` fields
- RAG chunks must have YAML frontmatter with: chunk_id, agente, topico, prioridade, quando_consultar

## Source documents

Primary: `PLANEJAMENTO/DOCUMENTOS/FUNDAMENTOS/ENGENHARIA GERAL.pdf` (171pp, 10 docs)
Architecture: `PLANEJAMENTO/DOCUMENTOS/FUNDAMENTOS/KERNEL V2.docx.pdf` (85pp)
Governance: `Projeto 1 - ORYX Agent/01_Governanca_Geral/CEE-001*, GMC-001*, SDD-001*, PPQ-001*`
```

### S002 | T1 | harness-eval

- path: `.claude/skills/harness-eval/SKILL.md`
- chars: 15459
- outline:
- Harness Eval
  - User questionnaires (HIGH PRIORITY)
    - Q1 — Optional project docs (after inventory)
    - Q2 — Tracks B and C (before Track A — budget)
  - Loading this skill's files
  - Critical rules
  - Instructions
    - Step 1: Resolve SKILL_DIR
    - Step 2: Inventory + claim deck
- Optional scope: AGENTS.md + one-hop related skills only
- python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" --seed AGENTS.md
    - Step 2b: Optional docs — **Q1** (see top)
    - Step 2c: Track budget — **Q2** (see top)
    - Step 3: Track A (deterministic) — always run
    - Step 4: Track B — Judge1
    - Step 5: Track B — Judge2 (blind)
    - Step 6: Merge Track B agreement
    - Step 7: Track C — surface deck
    - Step 8: Track C — Usefulness Judge1
    - Step 9: Track C — Usefulness Judge2 (blind)
    - Step 10: Merge Track C agreement
    - Step 11: Present results
  - Examples
    - Example 1: Full harness eval
    - Example 2: Usefulness only (existing run)
    - Example 3: Wrong skill
  - Troubleshooting
    - Trap gate FAIL (Track B or C)
    - Track A false missing `.agents/...`
    - Subagent blocked
    - Track C Slim looks wrong after model change
    - Mixed apply rewrote conventions / removed modules
    - T2 empty / skill `references/` missing from inventory
    - ADRs appeared in Track C
    - Slim stub broke another skill that loads that file
    - Scripts missing

```markdown
---
name: harness-eval
description: "Evaluate a repo agent harness (AGENTS.md, rules, skills, skill refs) for broken paths/commands, redundant instructions, and usefulness using a stack-agnostic dual-judge protocol with planted traps. HIGH PRIORITY questionnaires at top: Q1 optional docs, Q2 B/C budget before Track A (certainty/tokens). A always runs after Q2; B/C opt-in. ADRs/RFCs excluded from T2. Mixed apply uses 11-mixed-apply.md (KEEP/CUT). Use when the user says harness eval, harness-eval, harness debug, audit AGENTS.md, audit skills/rules, instruction audit, redundancy of agent instructions, usefulness of skills, Ship/Review/Hold/Slim/Keep-core for harness, or wants Track A/B/C harness evaluation. Do NOT use for harness setup or init, feature spec-driven work (tlc-spec-driven), or applying Ship/Slim trims unless the user explicitly asks after the report."
license: CC-BY-4.0
metadata:
  author: Tech Leads Club - github.com/tech-leads-club
  version: 1.8.3
---

# Harness Eval

Run a full, stack-agnostic harness evaluation and stop at reports. Do not auto-edit AGENTS.md or skills unless the user explicitly asks after reviewing Ship/Slim.

## User questionnaires (HIGH PRIORITY)

**Stop and ask before continuing.** Do not skip these gates. Do not silently include optional docs or spawn B/C judges.

Order after inventory: **Q1 (if needed) → Q2 → then Track A** (A always runs) → B/C only if approved.

### Q1 — Optional project docs (after inventory)

When `optional-docs-candidates.md` lists optional types, ask before Q2 / Track A:

```markdown
Inventory found cited project docs outside the agent skill trees.

- **Always in scope:** skill-tree files (`.agents/skills`, `.cursor/skills`, `.claude/skills`)
- **Always excluded:** ADRs / RFCs / decision-record trees (never scored as T2)
- **Optional (default: omit):** see types/paths in `optional-docs-candidates.md`

Include any optional doc types or paths in this run?
Reply with: `none` (default), type ids (e.g. `docs`), and/or specific paths.
```

Re-run inventory with `--include-doc-type` / `--include-doc` only after the user answers. If no optional types, skip Q1.

### Q2 — Tracks B and C (before Track A — budget)

Ask **before** Track A so the user sets spend up front. Track **A always runs** next (deterministic, ~0 model tokens). B/C run only if approved.

```markdown
Choose eval scope for this run (before Track A).

| Track | Question | Certainty | Token consumption |
|-------|----------|-----------|-------------------|
| **A — Correctness** | Cited path/command exists? | **Highest** — script only, no LLM. Prefers false negatives over false BROKEN. | **~0 model tokens** (always runs next) |
| **B — Redundancy** | Would an agent rediscover this cheaply without the harness? | **Medium** — dual LLM + plants; Ship only if trap PASS and both agree. Disagree → Hold. Less model-sensitive than C. | **High** — 2 judges × every claim (~N in this inventory). Each may spot-check the repo. |
| **C — Usefulness** | Does this surface change behavior vs theory/demo/overlap? | **Lowest / most subjective** — dual LLM + plants + fan-in; **model-sensitive**. Slim/Mixed need gates; prefer second-model check before large deletes. | **Highest** — 2 judges × every surface (whole files; often dominates the run). |

Notes: Ship (B) ≠ Slim (C). Rediscoverable ≠ useless. A always runs; B/C are optional.

Reply with one of: `A only`, `B`, `C`, or `B+C`.
```

Fill claim count from `claims.md` when known; surface count ≈ T0+T1+T2 markdown after extract (or say “after surfaces_extract” if not run yet).

- **`A only`:** run Track A; present `04`; stop (no B/C judges).
- **`B`:** Track A, then Steps 4–6.
- **`C`:** Track A, then Steps 7–10 (C does not need B).
- **`B+C`:** Track A, then Steps 4–11.

If the user already requested B/C/`full eval` in the triggering message, treat as approval — still show the Q2 table once so costs are visible.

## Loading this skill's files

This skill is **self-contained**. Protocol, scripts, and judge prompts live under this skill directory (the folder that contains this `SKILL.md`). Resolve `SKILL_DIR` as that directory — never assume another install path.

- Read [references/PROTOCOL.md](references/PROTOCOL.md) **completely** before the first run in a session (and again if scripts fail).
- Read [references/judge-prompts.md](references/judge-prompts.md) when spawning Track B or Track C judges.
- Plain-language terms: [references/GLOSSARY.md](references/GLOSSARY.md) (also embedded at the top of `04` / `07` / `10` reports).
- Claim record shape: [references/claims.schema.json](references/claims.schema.json) (for tooling; agents do not need to load it every run).
- Run scripts as `python3 "$SKILL_DIR/scripts/<name>.py" ...`.

Run **outputs** (not protocol) go to the target repo at `.harness-eval/runs/<run-id>/`.

## Critical rules

1. **Report-only by default.** Judgment ≠ remediation.
2. **README out of scope** as harness surface and as rediscovery/usefulness evidence.
3. **Stack-agnostic.** Never hard-code package managers, DBs, frameworks, or folder layouts in prompts or plants. Discover manifests that exist (JS, Python, Make/Task, Rust, Go, PHP, Ruby/Rails, Java/Gradle/Maven, plus `bin/*`).
4. **Doc scope.** T2 always includes agent skill-tree refs (`.agents/skills`, `.cursor/skills`, `.claude/skills`). **ADRs / RFCs (decision-record trees) are always excluded** from T2 surfaces. Other cited project docs are **optional** — default omit; ask via **Q1** at the top of this skill, then re-run with `--include-doc-type` / `--include-doc`.
5. **Track A always runs** after inventory (deterministic, high-precision). Prefer false negatives over false BROKEN. Placeholders (`SPEC_FOLDER`, `{x}`, `[feature]`) are never BROKEN. Never normalize paths with `str.lstrip('./')`.
6. **Tracks B and C require user approval via Q2 before Track A.** Do not spawn B/C judges until the user opts in. User may approve B only, C only, both, or A only.
7. **Track B needs dual judges + plants.** Judge2 is blind (must not read Judge1 scores or `trap-key.json`). Ship only if trap gate PASS and dual REDUNDANT with Judge2 cost ≤ 1.
8. **Track C needs dual judges + plants.** Blind Judge2 must not read `08-usefulness-j1.md` or `usefulness-trap-key.json`. Slim only if trap PASS, dual SLIM/ROUTING-ONLY, **and fan-in PASS** (no other harness surface hard-loads the path as SoT — merge enforces this on the full skill tree, not just `--seed`). **Usefulness is model-sensitive** — record `model: <id>` in both score files; prefer same model within a run; re-judge on a second model before large Slim deletes.
9. **KEEP / KEEP-CORE plants must not be verbatim copies** of claims/surfaces already in the deck.
10. **Subagents:** use an allowlisted non-fast model (prefer the same family as the parent when policy allows). Do not use `*-fast` models.
11. **Do not equate tracks.** Track B Ship ≠ Track C Slim. Rediscoverable ≠ useless; useful ≠ non-redundant.
12. **Slim apply / fan-in.** Never stub or delete a Slim path listed under “Slim fan-in blocked” (or when `python3 "$SKILL_DIR/scripts/slim_fanin.py" --path <P>` reports citers) unless those consumers are updated in the same change.
13. **Mixed/Slim apply stays self-contained.** Cutting REPO-DEMONSTRATED / THEORY means delete or compress that bulk in the harness surface. Never replace a fenced teaching snippet (or the contract it carried) with `See app/...` / `lib/...` / `test/...` — that swaps SoT for a code-tree pointer. Judge evidence paths stay in score tables only; if the behavior-changing contract must survive, keep a short in-skill rule or snippet.
14. **Mixed apply is mechanical.** Dual MIXED alone is not enough. Merge emits `11-mixed-apply.md` with per-ID **KEEP** (from Keep-core columns) and **CUT** (from Slim columns). Apply agents must follow that file only — do not re-judge, redesign, or invent a different pattern than KEEP. Empty Keep-core/Slim cells → skip that path (Hold).

## Instructions

### Step 1: Resolve SKILL_DIR

Set `SKILL_DIR` to the directory containing this `SKILL.md`. Verify:

- `$SKILL_DIR/references/PROTOCOL.md`
- `$SKILL_DIR/scripts/inventory_extract.py`
- `$SKILL_DIR/scripts/track_a_correctness.py`
- `$SKILL_DIR/scripts/merge_agreement.py`
- `$SKILL_DIR/scripts/surfaces_extract.py`
- `$SKILL_DIR/scripts/merge_usefulness.py`
- `$SKILL_DIR/scripts/slim_fanin.py`
- `$SKILL_DIR/scripts/doc_scope.py`

If missing, the skill install is broken — stop.

### Step 2: Inventory + claim deck

From the **target repo root**:

```bash
RUN_ID=$(date -u +%Y-%m-%d)-full
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID"
# Optional scope: AGENTS.md + one-hop related skills only
# python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" --seed AGENTS.md
```

Expected under `.harness-eval/runs/$RUN_ID/`: `inventory.json`, `claims.jsonl`, `claims.md`, `trap-key.json`, `optional-docs-candidates.md` (+ `.json`).

### Step 2b: Optional docs — **Q1** (see top)

Read `optional-docs-candidates.md`. If optional types exist, run **Q1** from [User questionnaires](#user-questionnaires-high-priority). Re-run inventory only after approval:

```bash
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" \
  --include-doc-type docs   # and/or --include-doc path
```

### Step 2c: Track budget — **Q2** (see top)

Run **Q2** from [User questionnaires](#user-questionnaires-high-priority) **before** Track A. Record the answer (`A only` / `B` / `C` / `B+C`). Do not start Steps 4+ unless B and/or C were approved.

### Step 3: Track A (deterministic) — always run

```bash
python3 "$SKILL_DIR/scripts/track_a_correctness.py" --root . --run-id "$RUN_ID"
```

Expected: `04-correctness.md` (includes term definitions at top). Spot-check that `.agents/...` cites resolve (not `agents/...`).

Summarize Track A (broken count + notable clusters). If Q2 was `A only`, stop. Otherwise continue to the approved B and/or C steps.

### Step 4: Track B — Judge1

Read `references/judge-prompts.md` (Track B Judge1). Spawn an independent subagent with an allowlisted model. Point it at `.harness-eval/runs/$RUN_ID/claims.md`. It writes `05-redundancy-j1.md` (include `model: <id>`).

Judge1 may read `inventory.json`. Must not read `trap-key.json`.

### Step 5: Track B — Judge2 (blind)

Read `references/judge-prompts.md` (Track B Judge2). Spawn a second subagent. Writes `06-blind-scores.md`.

Forbidden for Judge2: `trap-key.json`, `05-redundancy-j1.md`, `07-agreement.md`, prior agreement reports.

Prefer Steps 4 and 5 in parallel.

### Step 6: Merge Track B agreement

```bash
python3 "$SKILL_DIR/scripts/merge_agreement.py" --run-dir .harness-eval/runs/$RUN_ID
```

Expected: `07-agreement.md` (Ship/Review/Hold + **What these words mean**). On trap FAIL: fix plants per PROTOCOL, rescore P00x, re-merge — do not Ship.

### Step 7: Track C — surface deck

```bash
python3 "$SKILL_DIR/scripts/surfaces_extract.py" --root . --run-id "$RUN_ID"
```

Expected: `surfaces.md`, `surfaces.json`, `usefulness-trap-key.json`.

### Step 8: Track C — Usefulness Judge1

Read `references/judge-prompts.md` (Usefulness Judge1). Spawn subagent with allowlisted model (record same id in header). Writes `08-usefulness-j1.md`.

Must not read `usefulness-trap-key.json`.

### Step 9: Track C — Usefulness Judge2 (blind)

Read Usefulness Judge2 prompt. Prefer **same model** as Step 8 for agreement stability. Writes `09-usefulness-j2.md`.

Forbidden: `usefulness-trap-key.json`, `08-usefulness-j1.md`, `10-usefulness-agreement.md`, and using Track B 05/06/07 to decide usefulness classes.

Prefer Steps 8 and 9 in parallel.

### Step 10: Merge Track C agreement

```bash
python3 "$SKILL_DIR/scripts/merge_usefulness.py" --run-dir .harness-eval/runs/$RUN_ID
```

Expected: `10-usefulness-agreement.md` (Slim/Keep-core/Mixed/Hold + **What these words mean**), `11-mixed-apply.md` (KEEP/CUT per Mixed ID), plus `slim-fanin.json`. On t

…[truncated for deck; judge must read full file on disk]…
```

### S003 | T1 | skills

- path: `.claude/skills/SKILL.md`
- chars: 19560
- outline:
- SOT Harness — Referência Mestre de Especificação
  - Parte 1 — Princípios de Arquitetura [GEH-001]
    - 1.1 Os 4Es — Hierarquia inviolável de governança
    - 1.2 Taxonomia ETCLOVG — Anatomia do harness
    - 1.3 Centralizar vs. Descentralizar
    - 1.4 Padrão de ativação preguiçosa (lazy por evidência)
  - Parte 2 — Metodologia de Especificação [UNIDADE-ATÔMICA-SOT]
    - 2.1 Unidade atômica: BASpec (Behavioral Assertion Specification)
    - 2.2 Modelo de profundidade D0-D9
    - 2.3 Calibração por complexidade SOT
    - 2.4 As 5 gramáticas normativas
    - 2.5 Template mestre de spec
- Spec — [Nome do Componente]
  - Missão (D0) [OBRIGATÓRIO]
  - Escopo (D1) [OBRIGATÓRIO]
    - Dentro do escopo
    - Fora do escopo (Non-goals)
  - Regras aplicáveis (D2) [OBRIGATÓRIO]
  - Comportamento situacional (D3) [OBRIGATÓRIO]
  - Algoritmo (D4) [OBRIGATÓRIO para HIGH/CRITICAL]
    - Algoritmo: [nome]
  - Estados (D5) [OBRIGATÓRIO para agentes com P08]
  - Protocolo de Blackboard (D6) [OBRIGATÓRIO para agentes]
  - Cenários de teste (D7) [OBRIGATÓRIO para HIGH/CRITICAL]
    - Cenário [ID]-[nome]
  - Casos adversariais (D8) [OBRIGATÓRIO para CRITICAL]
    - Adversarial [ID]-[nome]
  - Auditabilidade (D9) [OPCIONAL — somente sistema completo]
  - I/O
  - Parte 3 — Etiquetagem obrigatória
  - Parte 4 — Quality Gates L1-L4
    - Gate L1 — Operacional (pré-requisito para qualquer implementação)
    - Gate L2 — Guiado (pré-requisito para integração entre agentes)
    - Gate L3 — Testável (pré-requisito para produção)
    - Gate L4 — Expert (pré-requisito para autonomia completa)
  - Parte 5 — Decisões necessárias (BLOQUEANTES)
  - Parte 6 — Sequência recomendada de sprints
    - Sprint 1 — P0 Blockers (especificar primeiro)
    - Sprint 2 — P1 Agentes críticos
    - Sprint 3 — P2 Infraestrutura cognitiva
- …

```markdown
---
name: sot-harness-spec
description: >
  Referência mestre para especificação e validação do Harness Cognitivo SOT.
  Use quando: especificar um agente novo, aprofundar um spec existente,
  validar harness files para completude, conformidade constitucional e
  maturidade estrutural. Integra GEH-001 (arquitetura de agentes) e
  BASpec/D0-D9 (metodologia de especificação). Contém Quality Gates L1-L4,
  sequência de sprints e bloqueadores de decisão.
---

# SOT Harness — Referência Mestre de Especificação

<!-- Fontes: GEH-001 (Guia Agente Especificações e Harness) + Unidade Atômica SOT v1.0 -->
<!-- Hierarquia de autoridade: decisões homologadas → docs baselined → Kernel →
     Engenharia Geral → modelos canônicos → spec Harness → TLC Spec Driven →
     pesquisa externa → inferências do agente -->

---

## Parte 1 — Princípios de Arquitetura [GEH-001]

### 1.1 Os 4Es — Hierarquia inviolável de governança

```
0. Conformidade / invariantes do domínio   → pré-condição absoluta
1. Eficácia      → o resultado está correto? (medido contra spec/invariantes)
2. Efetividade   → gera valor real no tempo certo? (inclui latência)
3. Eficiência    → menor recurso por execução (subordinado a 1 e 2)
4. Economicidade → menor custo unitário de provisionamento de 3
```

**Máximas invioláveis:**
- "Eficiência sem Eficácia é desperdício disfarçado de economia."
- "Economicidade que compromete Eficiência vira falsa economia."
- "Nenhuma otimização de custo pode subir o degrau da hierarquia."
- "Um modelo mais rápido que gera análise incorreta é pior que um modelo lento que gera análise correta." [CEE-001]

### 1.2 Taxonomia ETCLOVG — Anatomia do harness

| Camada | Nome | O que cobre |
|---|---|---|
| E | Execution Environment | Sandbox, permissões, liveness |
| T | Tool Interface & Protocol | Function-calling, MCP, seleção de ferramentas |
| C | Context & Memory Management | Curto/médio/longo prazo, KV-cache |
| L | Lifecycle & Orchestration | Controle de fluxo, coordenação, pipelines |
| O | Observability | Tracing, custo, sinais de confiabilidade |
| V | Verification | Avaliação, atribuição de falha, testes |
| G | Governance | Permissões, audit trail, gates de aprovação |

**Princípio C (contexto):** contexto é recurso escasso. Dê ao modelo exatamente a
informação certa em cada passo — posição importa tanto quanto presença.

**Princípio T (ferramentas):** "menos ferramentas, porém melhores". Se você não
consegue explicar quando uma ferramenta se aplica, o modelo também não conseguirá.

### 1.3 Centralizar vs. Descentralizar

**Default: centralizar.** Um fluxo único, linear, com contexto compartilhado
resolve a maioria dos problemas sem o custo de 4-15× tokens dos sistemas multiagentes.

**Os 3 (e apenas 3) gatilhos legítimos para descentralizar:**

1. **Proteção de contexto** — subtarefa gera >1.000 tokens irrelevantes para o
   orquestrador E tem critério de extração claro (só a conclusão precisa voltar)
2. **Paralelização de facetas independentes** — domínios ou fontes distintas,
   genuinamente isoláveis, para leitura/análise em paralelo
3. **Especialização de ferramentas/persona** — >20 ferramentas, ou conjuntos
   conflitantes que degradariam uns aos outros

**O que NUNCA descentralizar:**
- Decisões de design que dependem de contexto compartilhado
- Tarefas de escrita/integração cujos resultados precisam de costura coerente
- Consenso, autoridade e declaração de decisão final
- Síntese final e arbitragem de conflitos

**Heurística leitura × escrita:**
```
Leitura / exploração / análise  →  descentralizável
Escrita / decisão / síntese / consenso  →  SEMPRE centralizado
```

**Checklist de topologia (gate obrigatório antes de qualquer decomposição):**
- [ ] O fluxo centralizado resolve? Se sim, NÃO adicione agentes
- [ ] Se contexto estoura, tentei compressor antes de fragmentar?
- [ ] Pelo menos 1 dos 3 gatilhos é satisfeito?
- [ ] As fronteiras são de contexto, não de fase?
- [ ] Toda escrita/decisão/síntese/consenso permanece centralizada?
- [ ] Há critério de aceitação claro para subagente verificador?

### 1.4 Padrão de ativação preguiçosa (lazy por evidência)

Para o SOT: não despertar etapas profundas sem evidência que as justifique.

```
Sinal detectado pelo Orchestrator
  → ativa Elliott Specialist (análise estrutural básica)
     → se convicção estrutural ≥ limiar → ativa Fibonacci Validator
        → se geometria confirma → ativa SMC Specialist
           → se estrutural+institucional convergem → ativa ICT Specialist
              → se condições de execução presentes → ativa Synthesis Agent
                 → se score≥7 + conv≥70% + R:R≥2:1 → gera TMP
```

Isso materializa o CEE-001 Framework 3E: eficiência como consequência de eficácia,
nunca como atalho.

---

## Parte 2 — Metodologia de Especificação [UNIDADE-ATÔMICA-SOT]

### 2.1 Unidade atômica: BASpec (Behavioral Assertion Specification)

A BASpec é a unidade mínima indivisível de especificação do harness cognitivo SOT.
Ela torna o EARS notation plenamente rastreável e testável.

```
BASpec-[ID]:
  QUANDO: <condição observável e verificável>
  ENTÃO:  <comportamento específico e mensurável>
  PORQUE: <princípio ou regra que justifica>
  REFERÊNCIA: <RULE-XX, CONSTITUTION.md §Y, fonte>
  VERIFICADO POR: <cenário de teste com input e expected output>
```

**Exemplo canônico (BASpec-EW-001):**
```
BASpec-EW-001:
  QUANDO: Onda 3 medida resultar em comprimento < comprimento da Onda 1
  ENTÃO:  o agente DEVE descartar a contagem E reiniciar análise com
          novo conjunto de hipóteses E publicar motivo no Blackboard
          workspace "Observations"
  PORQUE: Regra imutável de Elliott — Onda 3 nunca é a mais curta
  REFERÊNCIA: RULE-EW-006, CONSTITUTION.md §Hierarquia metodológica
  VERIFICADO POR:
    DADO: onda1_length=100, onda3_length=80
    QUANDO: validar_contagem(w1=100, w3=80)
    ENTÃO: resultado = {status: DESCARTADO, motivo: "W3_SHORTER_THAN_W1",
           new_hypotheses: [...]}
```

**Regras de boa formação:**
- Cobre UMA condição observável (não múltiplas)
- Produz UM comportamento mensurável
- Mapeia para ≤2 RULES do RULES.md
- Testável com um único cenário input/output

### 2.2 Modelo de profundidade D0-D9

Escala adaptativa: o rigor deve ser proporcional ao impacto [PPQ-001].

| Nível | Nome | Pergunta respondida | Formato | Obrigatório para |
|---|---|---|---|---|
| D0 | Intenção | "O que este componente faz?" | Parágrafo 2-3 frases | Todos |
| D1 | Escopo | "O que está dentro e fora?" | Lista escopo + antiescopo | Todos |
| D2 | Regra nominal | "Que restrições existem?" | RULE-XX em EARS puro | Todos |
| D3 | Comportamental | "Em que situações age como?" | BASpec sem VERIFICADO POR | Agentes e motores |
| D4 | Algoritmo | "Exatamente como calcula?" | Fórmula, pseudocódigo, exemplos numéricos | Componentes det./semi-det. |
| D5 | Estado | "Quais estados e transições?" | Máquina de estados (tabela/diagrama) | Agentes stateful (P08) |
| D6 | Protocolo | "Em que ordem publica no Blackboard?" | Sequência com dependências | Todos os agentes |
| D7 | Teste | "Dado X, espera-se Y?" | BASpec completo com VERIFICADO POR | HIGH e CRITICAL |
| D8 | Adversarial | "O que deve ser rejeitado?" | Casos de falha esperada | CRITICAL |
| D9 | Auditoria | "Como reconstituir a decisão?" | Log schema + cadeia causal | Sistema completo (P13) |

### 2.3 Calibração por complexidade SOT

| Componente | Complexidade | Profundidade mínima |
|---|---|---|
| Conviction Engine | **CRITICAL** | D0-D8 |
| Elliott Specialist | **CRITICAL** | D0-D8 |
| Blackboard Protocol | **CRITICAL** | D0-D7 |
| Synthesis Agent | **HIGH** | D0-D7 |
| SMC Specialist | **HIGH** | D0-D6 |
| Event Bus (EC-COG-005) | **HIGH** | D0-D6 |
| ICT Specialist | **MEDIUM** | D0-D5 |
| Fibonacci Validator | **MEDIUM** | D0-D5 |
| Knowledge Graph (EC-COG-003) | **MEDIUM** | D0-D5 |
| Pattern Memory | **MEDIUM** | D0-D4 |
| Learning Governance (P12) | **LOW** | D0-D3 |

### 2.4 As 5 gramáticas normativas

**G1 — Normativa (D2):** para regras
```
RULE-XX: <sujeito> DEVE/NÃO DEVE/PODE <ação>
         [Fonte: documento §seção]
```

**G2 — Comportamental (D3):** para specs situacionais (EARS)
```
**Quando** <condição observável>, o agente DEVE <resposta>
```

**G3 — Operacional (D4):** para algoritmos
```
ALGORITMO: <nome>
  ENTRADA: <variáveis tipadas>
  PROCESSO:
    1. <passo com fórmula explícita>
    2. <passo com fórmula explícita>
  SAÍDA: <variável tipada + range válido>
  EXEMPLO: entrada={...} → saída={...}
```

**G4 — Cognitiva (D5):** para máquinas de estados
```
Estado: <NOME_ESTADO>
  → Transição para <OUTRO_ESTADO> quando <condição>
  → Emite <publicação_blackboard> ao entrar
  → Aguarda <evento> antes de transitar
```

**G5 — Avaliativa (D7):** para cenários de teste (Gherkin adaptado)
```
DADO: <estado inicial com valores concretos>
QUANDO: <evento ou input específico>
ENTÃO: <expected output com valores concretos>
VERIFICAÇÃO: campo_x = valor_esperado
```

### 2.5 Template mestre de spec

```markdown
# Spec — [Nome do Componente]
<!-- Fonte: [documentos fonte] | Versão: [X.Y] | Profundidade: D[nível] -->
<!-- Complexidade: CRITICAL | HIGH | MEDIUM | LOW -->

## Missão (D0) [OBRIGATÓRIO]
[2-3 frases. Qual pergunta este componente responde?]

## Escopo (D1) [OBRIGATÓRIO]
### Dentro do escopo
- [item]
### Fora do escopo (Non-goals)
- [item]

## Regras aplicáveis (D2) [OBRIGATÓRIO]
- RULE-XX: [texto resumido] [Fonte: §]

## Comportamento situacional (D3) [OBRIGATÓRIO]
**Quando** [condição observável], o agente DEVE:
- [ação 1]
- [ação 2]

## Algoritmo (D4) [OBRIGATÓRIO para HIGH/CRITICAL]
### Algoritmo: [nome]
**Entrada:** [variáveis tipadas]
**Processo:**
  1. [passo com fórmula]
**Saída:** [variável tipada + range]
**Exemplo:** entrada={...} → saída={...}

## Estados (D5) [OBRIGATÓRIO para agentes com P08]
| Estado | Descrição | Entra quando | Sai quando | Publica no Blackboard |
|---|---|---|---|---|
| IDLE | ... | ... | ... | nada |
| ANALYZING | ... | ... | ... | workspace/Observations |

## Protocolo de Blackboard (D6) [OBRIGATÓRIO para agentes]
Sequência de publicação:
1. [condição] → publica em [workspace] → mensagem: [schema]
Dependências: [aguarda workspace/X ter estado Y]

## Cenários de teste (D7) [OBRIGATÓRIO para HIGH/CRITICAL]
### Cenário [ID]-[nome]
**DADO:** [estado inicial com valores concretos]
**QUANDO:** [evento ou input]
**ENTÃO:** [expected output com valores concretos]
**VERIFICAÇÃO:** campo_x = valor_esperado

## Casos adversariais (D8) [OBRIGATÓRIO para CRITICAL]
### Adversarial [ID]-[nome]
**DADO:** [estado que deve ser rejeitado]
**QUANDO:** [evento]
**ENTÃO:** sistema DEVE rejeitar com: [erro específico]

## Auditabilidade (D9) [OPCIONAL — somente sistema completo]
[Como reconstituir esta decisão 48h depois]

## I/O
- Input: `schemas/[nome].input.json`
- Output: `schemas/[nome].output.json`
```

---

## Parte 3 — Etiquetagem obrigatória

Todo conteúdo novo produzido por agentes deve usar as etiquetas:

| Etiqueta | Significado |
|---|---|
| **[FONTE]** | Extraído diretamente de documento do projeto |
| **[INFERÊNCIA]** | Derivado por análise — pode estar errado |
| **[PROPOSTA]** | Novo conteúdo — requer homologação |
| **[DECISÃO NECESSÁRIA]** | Conflito ou lacuna — PARAR e reportar |
| **[EXTERNO]** | TLC Spec Driven, harness-score, pesquisa externa |

**Regra de conflito:** quando houver conflito entre fontes, NÃO resolver
silenciosamente. Registrar o conflito, explicar o impacto, marcar como
[DECISÃO NECESSÁRIA] e aguardar instrução.

---

## Parte 4 — Quality Gates L1-L4

### Gate L1 — Operacional (pré-requisito para qualquer implementação)

| Gate | Critério | Ferramenta |
|---|---|---|
| D0-PRESENT | Missão clara em ≤3 frases | lint-specs.js |
| D1-PRESENT | Antiescopo declarado explicitamente | lint-specs.js |
| D2-TRACED | Toda RULE tem fonte documentada | RULES.md review |
| D3-EARS | ≥3 situações em BASpec/EARS | lint-specs.js |
| SCHEMA-VALID | Schema JSON válido Draft-07 | validate-schemas.js |

### Gate L2 —

…[truncated for deck; judge must read full file on disk]…
```

### S004 | T2 | GLOSSARY.md

- path: `.claude/skills/harness-eval/references/GLOSSARY.md`
- chars: 3789
- outline:
- Harness Eval — plain-language glossary
  - The three tracks
  - Shared terms
  - Track A
  - Track B (redundancy)
  - Track C (usefulness)

```markdown
# Harness Eval — plain-language glossary

Embedded at the top of `04-correctness.md`, `07-agreement.md`, and `10-usefulness-agreement.md`. Prefer verbs over jargon when talking to humans.

## The three tracks

| Track | Question it answers | Certainty | Tokens | Main report |
|-------|---------------------|-----------|--------|-------------|
| **A — Correctness** | Is a cited path or command broken? | Highest (script, no LLM) | ~0 model | `04-correctness.md` |
| **B — Redundancy** | Would an agent rediscover this cheaply without the harness text? | Medium (dual LLM + plants) | High (2 × claims) | `07-agreement.md` |
| **C — Usefulness** | Does this surface change agent behavior, or is it theory / demo / overlap? | Lowest / model-sensitive | Highest (2 × surfaces) | `10-usefulness-agreement.md` |

**Run gating:** After inventory → Q1 (optional docs) → Q2 (B/C budget) → A always → B/C if approved.

**Do not equate tracks:** Ship (B) ≠ Slim (C). Rediscoverable ≠ useless. Useful ≠ non-redundant.

## Shared terms

| Term | Meaning | What you should do |
|------|---------|-------------------|
| **Trap gate PASS** | Planted fake claims/surfaces were scored correctly — judges are calibrated | Trust Ship / Slim bands |
| **Trap gate FAIL** | Judges failed discrimination plants | **Ignore** Ship / Slim; fix plants and re-run |
| **Hold** | Judges disagreed, score missing, or both unclear | **Do nothing** until you decide manually |
| **T0 / T1 / T2** | Always-on rules / skills / cited harness refs | Priority: edit T0 first (always loaded) |
| **`--seed`** | Scope inventory to a starting file + one-hop related skills/refs | Only that subgraph was evaluated |
| **Optional docs** | Cited project docs outside skill trees (not ADRs/RFCs) | Default off; approve types via `optional-docs-candidates.md` |
| **ADR / RFC** | Decision-record docs | **Never** scored as T2 surfaces |

## Track A

| Term | Meaning | What you should do |
|------|---------|-------------------|
| **BROKEN** | Cited file/command does not exist (high-precision check) | Fix the cite or restore the file |

## Track B (redundancy)

| Term | Meaning | What you should do |
|------|---------|-------------------|
| **Ship** | Both judges: redundant **and** cheap to rediscover (cost ≤ 1) | **Safe to delete / trim** |
| **Review** | Both judges: keep (not redundant) | **Leave alone** for redundancy reasons |
| **REDUNDANT-CODE** | Echoes manifests/code layout | Candidate delete (only if Ship) |
| **REDUNDANT-GENERAL** | Generic advice, no repo-specific signal | Candidate delete (only if Ship) |
| **KEEP-POLICY / KEEP-CAVEAT / KEEP-ROUTING / KEEP-COMPRESSED** | Keep families | Leave alone |

## Track C (usefulness)

| Term | Meaning | What you should do |
|------|---------|-------------------|
| **Keep-core** | Most of the file **changes agent behavior** | **Do not slim** |
| **Mixed** | Real behavior-changing core **plus** large theory/examples/overlap | Follow **`11-mixed-apply.md`** (KEEP vs CUT) — do not re-judge |
| **Slim** | Mostly theory, repo-demo fluff, or overlap — **and** fan-in PASS | **Compress or delete body** (model-sensitive) |
| **Fan-in blocked** | Another harness surface hard-loads this path as SoT / required load | **Do not stub/delete** until those consumers are updated |
| **BEHAVIOR-CHANGING** | Without this text, agents likely do the wrong thing | Preserve |
| **REPO-DEMONSTRATED** | Already taught by opening 1–2 example files (judge cites those paths as evidence) | Safe to **cut** from the skill — do **not** replace with a `See app/...` pointer |
| **THEORY** | General software advice | Safe to cut |
| **OVERLAP** | Same rule already in another harness file | Cut here; keep the canonical copy |
| **ROUTING-ONLY** | Triggers / pointers | Keep short |
```

### S005 | T2 | PROTOCOL.md

- path: `.claude/skills/harness-eval/references/PROTOCOL.md`
- chars: 11295
- outline:
- Harness Evaluation Protocol
  - Purpose
  - Surface inventory (tiers)
    - Doc scope (T2)
  - Agnostic constraints
  - Track A — Correctness
  - Track B — Redundancy
  - Track C — Usefulness
    - Model sensitivity (Track C)
  - Operator flow
- After optional-docs-candidates.md: ask user, then e.g.:
- python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" --include-doc-type docs
- Scope to AGENTS.md + one-hop related skills/refs:
- python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" --seed AGENTS.md
- STOP: Q1 optional docs (if candidates), then Q2 approve B/C (see skill questionnaires)
- If B approved:
- Track B judges → 05-redundancy-j1.md, 06-blind-scores.md
- If C approved:
- Track C judges → 08-usefulness-j1.md, 09-usefulness-j2.md
    - Certainty and token consumption
  - Safety

```markdown
# Harness Evaluation Protocol

> Platform- and codebase-agnostic. Version: 1.8.3
> Scripts and this file live inside the `harness-eval` skill. Run outputs go to the target repo under `.harness-eval/runs/<id>/`.

## Purpose

Evaluate a repository’s **agent harness** for:

- **Track A — Correctness:** broken paths, missing commands, dead links (deterministic).
- **Track B — Redundancy:** instructions rediscoverable cheaply without harness text (dual LLM judge + plants).
- **Track C — Usefulness:** which surfaces change agent behavior vs restating theory, repo demos, or overlapping harness text (dual LLM judge + plants; **model-sensitive**).

Judgment is separate from remediation. Reports suggest; humans approve Slim/Ship edits.

**Run gating (HIGH PRIORITY — skill opens with questionnaires):** After inventory: **Q1** (optional docs) → **Q2** (B/C budget, certainty + tokens) → **Track A always** → B/C only if approved. Do not spawn B/C judges until Q2 is answered (unless the user already requested those tracks — still show Q2 once).

## Surface inventory (tiers)

| Tier | Name | Discovery |
|------|------|-----------|
| **T0** | Always-on rules | `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/**`, `*.mdc` under repo / `.agents/` / `.cursor/` |
| **T1** | Skills | `SKILL.md` under `.agents/skills`, `.cursor/skills`, `.claude/skills` (presence-based) |
| **T2** | Referenced harness files | One-hop cites from T0/T1 after **doc scope** (below) |

**Out of scope:** `README*`, app source as instruction surface (evidence only), user-global rules outside the repo, recursive crawl of all project docs, **ADRs / RFCs / decision-record trees**.

### Doc scope (T2)

Stack-agnostic path policy (see `scripts/doc_scope.py`):

| Class | Rule |
|-------|------|
| **Agent harness refs** | Always T2 if cited — files under `.agents/skills/`, `.cursor/skills/`, `.claude/skills/` (including skill `references/`). Wins even if a skill folder is named `adr` (that is harness SoT for writing ADRs, not the decision-record corpus). |
| **Decision records** | **Never** T2 outside skill trees — path segments like `adr` / `adrs` / `rfc` / `rfcs` / `architecture-decision-records` / `request-for-comments`, or filenames `adr-*` / `rfc-*` (e.g. `docs/adr/**`) |
| **Other cited docs** | **Opt-in** — default omitted. Inventory writes `optional-docs-candidates.md`. Orchestrator **asks the user** which types/paths to include, then re-runs with `--include-doc-type` / `--include-doc` |

Track A may still flag a broken cite *to* an ADR path from AGENTS.md (correctness of the link). The ADR body is not scored as a harness surface.

## Agnostic constraints

- Do not hard-code package managers, databases, frameworks, or folder layouts.
- Discover manifests that exist across stacks (presence-based, no assumed runtime):
  - JS: `package.json`
  - Python: `pyproject.toml`
  - Make / Task: `Makefile`, `Taskfile.yml`
  - Rust: `Cargo.toml` (`[[bin]]`)
  - Go: `go.mod`, plus `bin/*` / Make / Taskfile
  - PHP: `composer.json`, `artisan`, `bin/console`
  - Ruby / Rails: `Gemfile`, `Rakefile`, `bin/*`
  - Java / JVM: `pom.xml`, `build.gradle(.kts)`, `settings.gradle(.kts)`
- Plants echo discovered script/task names or fixed stack-agnostic KEEP / usefulness templates.
- Track A command checks cover `yarn|npm|pnpm|bun`, `make`, `task`, `rake`/`rails`, `mvn`/`gradlew`, `go`, `composer`, `artisan`/`console`, and `bin/*`. Framework CLIs prefer false negatives over false BROKEN.

## Track A — Correctness

1. Path cites → case-sensitive existence (repo root or skill-relative).
2. Command cites → must exist in discovered manifest scripts when presented as runnable.
3. Skill-relative `references/` must resolve.
4. Dead skill names → BROKEN.

**Precision (prefer false negatives):**

- Never normalize with `str.lstrip('./')` — it turns a leading-dot dir like ".agents/…" into "agents/…". Strip only a "./" prefix.
- Skip placeholders: `SPEC_FOLDER`, `{module}`, `[feature]`, `path/to/...`, globs, `<angle>`.
- Only check concrete prefixes: `.agents/`, `.cursor/`, `docs/`, `.harness-eval/`, `.tlc/`, `references/`, `package/`, `app/`, `scripts/`.
- Skip package-manager builtins (`install`, `add`, …).
- Do not scan fenced code blocks for path cites (teaching examples stay in fences).
- Skill-relative `references/` may resolve under another skill named in the same surface (e.g. “load the `dev` skill and read `references/view.md`”).
- Missing `app/` / `lib/` / `test/` (and similar code-tree) cites are BROKEN only when mandate language (`load`, `open`, `must`, `required`, …) appears in the same paragraph — bare naming examples are not BROKEN.

## Track B — Redundancy

**Unit:** atomic claims (`claims.md`).

**Discovery cost:** 0 = exact manifest/config string; 1 = one listing/header; 2 = cross-module read; 3 = runtime/env/policy.

**Classes:** REDUNDANT-CODE | REDUNDANT-GENERAL | KEEP-POLICY | KEEP-CAVEAT | KEEP-ROUTING | KEEP-COMPRESSED | UNCLEAR.

**Hard rule:** cost ≥ 2 → never REDUNDANT-*.

**Plants (unlabeled in deck; orchestrator keeps `trap-key.json` private):**

| Template | Expected family |
|----------|-----------------|
| Manifest echo ×2 | REDUNDANT |
| Generic fluff ×2 | REDUNDANT |
| Fixed secrets policy | KEEP |
| Fixed local-vs-CI env caveat | KEEP |

KEEP plants must **not** be verbatim copies of claims already in the deck.

**Trap gate:** miss ≤ 1 plant family → PASS; else discard Ship band.

**Bands:** Ship = dual REDUNDANT + Judge2 cost≤1 + trap PASS; Review = dual KEEP; Hold = disagree.

## Track C — Usefulness

**Unit:** whole surfaces (`surfaces.md` from T0 + T1 + markdown T2), not atomic claims.

**Question:** If this surface were deleted, and the agent could still list the repo and open 1–2 canonical examples — **and any other harness surface that mandates loading this path still runs** — would behavior change?

**Overall classes:** KEEP-CORE | MIXED | SLIM | ROUTING-ONLY | UNCLEAR.

**Section tags (inside Keep-core / Slim columns):** BEHAVIOR-CHANGING | REPO-DEMONSTRATED | THEORY | OVERLAP | ROUTING-ONLY.

| Tag | Meaning |
|-----|---------|
| BEHAVIOR-CHANGING | Without it, wrong paths/APIs/gates are likely |
| REPO-DEMONSTRATED | Already taught by 1–2 concrete example files (judge evidence only — not a reason to add those paths into the skill) |
| THEORY | General SE knowledge; no repo-specific delta |
| OVERLAP | Same rule already in another harness surface (must cite path) |
| ROUTING-ONLY | Triggers / purpose / load pointers |

**Plants (`usefulness-trap-key.json`, private):**

| Template | Expected family |
|----------|-----------------|
| Generic clean-code theory surface | SLIM |
| Product-fluff surface | SLIM |
| Cross-module boundary / public-API policy surface | KEEP-CORE |

**Trap gate:** miss ≤ 1 plant family on Judge2 → PASS; else discard Slim band.

**Fan-in gate (deterministic, at merge — not judge-scored):** Before a dual SLIM/ROUTING-ONLY surface enters the Slim band, scan the **full** harness markdown corpus (T0 + all skill-tree `*.md` under `.agents/skills`, `.cursor/skills`, `.claude/skills` — not limited to `--seed` inventory). If another surface **hard-loads** the path (load/read/open mandate, “source of truth”, “extract … from”, Phase 0 load lists, etc.), move it to **Hold** with reason `slim-fanin-blocked`. Mere index-table mentions without mandate language do not block. Detail: `slim-fanin.json`.

**Bands:** Slim = dual SLIM/ROUTING-ONLY + trap PASS + fan-in PASS; Keep-core = dual KEEP-CORE; Mixed = dual MIXED; Hold = disagree / unclear / missing / slim-fanin-blocked.

**Mixed apply plan (deterministic, at merge):** For every dual-MIXED surface, `merge_usefulness.py` writes `11-mixed-apply.md` copying each judge’s Keep-core → **KEEP** and Slim → **CUT**. That file is the **only** Mixed apply input. Apply agents must not re-judge usefulness, redesign conventions, or invent cuts beyond CUT. If Keep-core/Slim cells are empty, skip the path (treat as Hold for apply).

### Model sensitivity (Track C)

Usefulness judgments depend on what the judge model treats as “general knowledge” vs repo-specific skill.

- **Always record** judge model ids in `08-usefulness-j1.md` and `09-usefulness-j2.md` headers (`model: <id>`).
- Prefer the **same allowlisted non-fast model** for C1 and C2 within one run (agreement stability).
- Before deleting large Slim bodies, **re-run Track C with a second model family** when available; treat cross-model disagreement as Hold.
- Track B (rediscovery cost) is less model-sensitive than Track C; never equate Ship (B) with Slim (C).

## Operator flow

Resolve `SKILL_DIR` = directory containing this skill’s `SKILL.md`.

```bash
RUN_ID=$(date -u +%Y-%m-%d)-full
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID"
# After optional-docs-candidates.md: ask user, then e.g.:
# python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" --include-doc-type docs
# Scope to AGENTS.md + one-hop related skills/refs:
# python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" --seed AGENTS.md
# STOP: Q1 optional docs (if candidates), then Q2 approve B/C (see skill questionnaires)
python3 "$SKILL_DIR/scripts/track_a_correctness.py" --root . --run-id "$RUN_ID"
# If B approved:
# Track B judges → 05-redundancy-j1.md, 06-blind-scores.md
python3 "$SKILL_DIR/scripts/merge_agreement.py" --run-dir .harness-eval/runs/$RUN_ID
# If C approved:
python3 "$SKILL_DIR/scripts/surfaces_extract.py" --root . --run-id "$RUN_ID"
# Track C judges → 08-usefulness-j1.md, 09-usefulness-j2.md
python3 "$SKILL_DIR/scripts/merge_usefulness.py" --run-dir .harness-eval/runs/$RUN_ID
```

### Certainty and token consumption

| Track | Certainty | Token consumption |
|-------|-----------|-------------------|
| **A** | Highest — deterministic script; no LLM | ~0 model tokens |
| **B** | Medium — dual LLM + plants; trap gate; disagree → Hold | High — 2 × every claim |
| **C** | Lowest / model-sensitive — dual LLM + plants + fan-in | Highest — 2 × every surface (whole files) |

Human-facing reports: `04-correctness.md`, `07-agreement.md`, `10-usefulness-agreement.md` — each starts with **What these words mean**. Mixed apply plan: `11-mixed-apply.md`. Full glossary: skill `references/GLOSSARY.md`.

## Safety

Evidence-or-zero for BROKEN, REDUNDANT, and SLIM/THEORY; author ≠ blind judges; plants before Ship/Slim; disagree → Hold; no auto-edit.

**Slim apply:** never stub/delete a path in the Slim band if `10-usefulness-agreement.md` lists it under fan-in blocked, or if a fresh `slim_fanin.py --path <P>` reports citers — update consumers in the same change first.

**Mixed apply:** follow `11-mixed-apply.md` only (KEEP/CUT per ID). Do not re-judge from the Mixed path table in `10`. KEEP contracts must survive as in-skill rules/snippets; CUT is the only removable bulk.

**Mixed/Slim apply (self-contained):** When cutting REPO-DEMONSTRATED, THEORY, or OVERLAP bulk, leave the remaining BEHAVIOR-CHANGING text self-contained in the harness surface. Never replace a fenced teaching snippet (or the contract it carried) with a soft/hard pointer into `app/`, `lib/`, `test/`, or other non-harness trees. Paths cited in usefulness Evidence / REPO-DEMONSTRATED tags are for judges only.
```

### S006 | T2 | judge-prompts.md

- path: `.claude/skills/harness-eval/references/judge-prompts.md`
- chars: 6236
- outline:
- Judge spawn prompts
- Track B — Redundancy
  - Judge1 prompt (Track B)
- Redundancy Judge1
  - Judge2 prompt (Track B, blind)
- Blind scores Judge2
- Track C — Usefulness
  - Usefulness Judge1 prompt
- Usefulness Judge1
  - Usefulness Judge2 prompt (blind)
- Usefulness Judge2 (blind)

```markdown
# Judge spawn prompts

Load when dispatching Track B or Track C judges. Substitute:

- `REPO` = target repository root
- `RUN_DIR` = `$REPO/.harness-eval/runs/<run-id>`
- `MODEL_ID` = allowlisted non-fast model id used for this judge (required in output headers)

---

# Track B — Redundancy

Score table header (required by `merge_agreement.py`):

```markdown
| ID | Cost | Class | Evidence | Confidence | Trim suggestion |
```

Allowed Class values: `REDUNDANT-CODE`, `REDUNDANT-GENERAL`, `KEEP-POLICY`, `KEEP-CAVEAT`, `KEEP-ROUTING`, `KEEP-COMPRESSED`, `UNCLEAR`.

Hard rubric: cost ≥ 2 → never REDUNDANT-*. README out of scope. Default KEEP/UNCLEAR when unsure. Score every ID in `claims.md` including `P00x`.

## Judge1 prompt (Track B)

```
You are Judge1 for a stack-agnostic harness redundancy audit.

Score EVERY claim row in:
<RUN_DIR>/claims.md

Follow the rubric in that file exactly.

Rules:
- Verify rediscovery against the live repo. Do not assume a stack beyond what exists.
- README is OUT OF SCOPE — never cite README as evidence.
- Hard rule: cost ≥ 2 → never REDUNDANT-*.
- Default KEEP/UNCLEAR when unsure.
- Score ALL IDs including P00x (you do not know which are plants).
- You MAY read <RUN_DIR>/inventory.json. Do NOT read trap-key.json or claims.jsonl.

Write ONLY to:
<RUN_DIR>/05-redundancy-j1.md

Start with:
# Redundancy Judge1
> run: <run-id>
> model: <MODEL_ID>

Then a short counts summary, then the full table covering every ID from claims.md.
```

## Judge2 prompt (Track B, blind)

```
You are Judge2 (BLIND second scorer) for a stack-agnostic harness redundancy audit.

Score EVERY claim row in:
<RUN_DIR>/claims.md

Follow the rubric in that file exactly.

Hard blind constraints — do NOT read:
- trap-key.json
- claims.jsonl
- 05-redundancy-j1.md
- 07-agreement.md
- any prior harness-eval agreement/redundancy reports outside this claims.md + inventory.json

Rules:
- Verify rediscovery against the live repo. No stack assumptions.
- README out of scope — never cite it.
- cost ≥ 2 → never REDUNDANT-*.
- Default KEEP/UNCLEAR when unsure.
- Score ALL IDs including P00x.

Write ONLY to:
<RUN_DIR>/06-blind-scores.md

Start with:
# Blind scores Judge2
> run: <run-id>
> model: <MODEL_ID>

Then counts summary, then the full table.
```

---

# Track C — Usefulness

Score **surfaces** in `<RUN_DIR>/surfaces.md` (not claims.md).

Required table header (parsed by `merge_usefulness.py`):

```markdown
| ID | Overall | Keep-core | Slim | Overlap cites | Evidence | Confidence |
```

Allowed Overall values: `KEEP-CORE`, `MIXED`, `SLIM`, `ROUTING-ONLY`, `UNCLEAR`.

Section tags inside Keep-core / Slim cells: `BEHAVIOR-CHANGING`, `REPO-DEMONSTRATED`, `THEORY`, `OVERLAP`, `ROUTING-ONLY`.

**Keep-core / Slim cells must be actionable** (especially when Overall is MIXED): name the concrete sections, patterns, modules, or checklist items to keep vs cut (e.g. `KEEP: ApiErrors concern + error envelope`; `CUT: long BoardsController fences`). Vague cells block Mixed apply. Merge copies these cells into `11-mixed-apply.md`.

**Model sensitivity:** Your prior about “general knowledge” affects THEORY vs BEHAVIOR-CHANGING. Prefer UNCLEAR over SLIM when the call is mostly your prior. Always put `model: <MODEL_ID>` in the header.

## Usefulness Judge1 prompt

```
You are Usefulness Judge1 for a stack-agnostic harness audit (Track C).

Score EVERY surface in:
<RUN_DIR>/surfaces.md

Read the rubric at the top of that file. For each surface, open the real file on disk when the deck preview is truncated. If the path does not exist on disk, score from the fenced body only.

Question: if this surface were deleted, and an agent could still list the repo and open 1–2 canonical examples — and any other harness surface that mandates loading this path still runs — would behavior change?

Rules:
- Evidence-or-zero. Cite harness paths and/or example code paths.
- README out of scope — never cite it.
- OVERLAP must cite another harness surface path.
- REPO-DEMONSTRATED must cite a concrete example file in the Evidence / Overlap columns of the score table only. Do not recommend adding that path into the harness surface as a `See …` replacement when trimming.
- If another harness skill/doc hard-loads this path as source of truth or required Phase-0/load reading, prefer KEEP-CORE or MIXED (keep the checklist body) over SLIM — do not assume seed inventory is the full consumer set; search skill trees when unsure.
- Default UNCLEAR when unsure (especially when relying on model general knowledge).
- Score ALL IDs including S9xx (you do not know which are plants).
- Do NOT read usefulness-trap-key.json, surfaces.json, 09-usefulness-j2.md, or 10-usefulness-agreement.md.
- You MAY read inventory.json and other harness files for overlap checks.
- A merge-time fan-in gate also blocks Slim apply when mandate citers exist; still score honestly.
- For MIXED rows, Keep-core and Slim cells must name what to preserve vs remove so merge can build `11-mixed-apply.md`.

Write ONLY to:
<RUN_DIR>/08-usefulness-j1.md

Start with:
# Usefulness Judge1
> run: <run-id>
> model: <MODEL_ID>

Then a counts summary by Overall class, then the full table covering every surface ID.
```

## Usefulness Judge2 prompt (blind)

```
You are Usefulness Judge2 (BLIND) for a stack-agnostic harness audit (Track C).

Score EVERY surface in:
<RUN_DIR>/surfaces.md

Read the rubric at the top of that file. Open real files when previews are truncated; if a path is missing on disk, score from the fenced body only.

Hard blind constraints — do NOT read:
- usefulness-trap-key.json
- surfaces.json
- 08-usefulness-j1.md
- 10-usefulness-agreement.md
- Track B score/agreement files (05/06/07) for deciding usefulness classes

Rules:
- Same counterfactual and evidence rules as Judge1 (including hard-load / SoT consumers outside a seeded inventory).
- README out of scope.
- Default UNCLEAR when unsure.
- Score ALL IDs including S9xx.
- Record your model id.
- For MIXED rows, Keep-core and Slim cells must be actionable (named keep vs cut) like Judge1.

Write ONLY to:
<RUN_DIR>/09-usefulness-j2.md

Start with:
# Usefulness Judge2 (blind)
> run: <run-id>
> model: <MODEL_ID>

Then counts summary, then the full table.
```
```

### S901 | T1 | Clean coding tips

- path: `(deck)/S901.md`
- chars: 202
- outline:
- Clean Coding Tips

```markdown
# Clean Coding Tips

- Prefer clear variable names and small functions.
- Follow SOLID and keep layers thin.
- Write readable comments when needed.
- Prefer composition over inheritance when practical.
```

### S902 | T1 | Assistant highlights

- path: `(deck)/S902.md`
- chars: 133
- outline:
- Assistant Highlights

```markdown
# Assistant Highlights

- Works with natural language.
- Returns relevant results quickly.
- Most efficient first step for any task.
```

### S903 | T1 | Module boundary rule

- path: `(deck)/S903.md`
- chars: 489
- outline:
- Module Boundary Rule
  - Critical

```markdown
# Module Boundary Rule

## Critical

- Never reach into another module's private storage or internal data access layer.
- Call only that module's documented public API or exported interface.
- Writes that span modules must use the project's declared transaction or unit-of-work boundary for the owning module — do not open a second write path around it.
- If you need data owned elsewhere, go through that owner module; do not import its internal repositories, tables, or storage helpers.
```

