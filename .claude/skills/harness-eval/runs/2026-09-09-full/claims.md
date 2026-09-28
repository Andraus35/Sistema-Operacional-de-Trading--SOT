# Blind claim deck — run `2026-09-09-full`

> Score every row. Some rows may be synthetic calibration rows.
> Do NOT read trap-key.json, claims.jsonl, Judge1 scores, or prior agreement reports.
> README is out of harness scope — do not cite it as rediscovery evidence.

## Rubric

| Cost | Meaning |
|------|---------|
| 0 | Exact string in a discovered manifest/config |
| 1 | Obvious from one directory listing or one file header |
| 2 | Needs reading implementation across modules |
| 3 | Runtime failure, environment-specific, or process/policy |

Classes: REDUNDANT-CODE | REDUNDANT-GENERAL | KEEP-POLICY | KEEP-CAVEAT | KEEP-ROUTING | KEEP-COMPRESSED | UNCLEAR

**Hard rule:** cost ≥ 2 → never REDUNDANT-*. Default UNCLEAR/KEEP when unsure.

## Claims

| ID | Tier | Source | Quote |
|----|------|--------|-------|
| C001 | T0 | `AGENTS.md` | The SOT-Harness is the formal specification harness for the **Sistema de Operações e Tendências (SOT)** — a multi-agent probabilistic trading system for BTC, XAU, and NASDAQ using Elliott Wave, Fibonacci, SMC, and ICT methodologies. |
| C002 | T0 | `AGENTS.md` | This harness is the source of truth for AI agents implementing or modifying the SOT system. All agent behavior, I/O contracts, rules, and conflict resolution logic are defined here. |
| C003 | T0 | `AGENTS.md` | Lower layers CANNOT override higher layers. ICT never creates hypotheses. SMC never corrects Elliott. |
| C004 | T0 | `AGENTS.md` | ICT Specialist stays INACTIVE unless a structural hypothesis is approved |
| C005 | T0 | `AGENTS.md` | No directional signal when `directional_conflict = true` between Elliott and SMC |
| C006 | T0 | `AGENTS.md` | R:R minimum 2:1 — no exceptions, even at score 9/9 + conviction 100% |
| C007 | T0 | `AGENTS.md` | Conviction global threshold: ≥ 70% for signal, ≥ 60% for bias emission |
| C008 | T0 | `AGENTS.md` | Score matrix: Elliott(0-3) + SMC(0-3) + ICT(0-3) ≥ 7/9 required for signal |
| C009 | T0 | `AGENTS.md` | All acceptance criteria use EARS notation: "Quando <condição>, o agente DEVE <resposta>" |
| C010 | T0 | `AGENTS.md` | Source document must be cited in every rule (format: `<!-- Fonte: DOC §N -->`) |
| C011 | T0 | `AGENTS.md` | Every behavior file must declare: Missão, Escopo, Antiescopo, Comportamentos, Critérios |
| C012 | T0 | `AGENTS.md` | Schema files must be valid JSON Schema Draft-07 with `$schema` and `$id` fields |
| C013 | T0 | `AGENTS.md` | RAG chunks must have YAML frontmatter with: chunk_id, agente, topico, prioridade, quando_consultar |
| C014 | T0 | `AGENTS.md` | Primary: `PLANEJAMENTO/DOCUMENTOS/FUNDAMENTOS/ENGENHARIA GERAL.pdf` (171pp, 10 docs) |
| C015 | T0 | `AGENTS.md` | Architecture: `PLANEJAMENTO/DOCUMENTOS/FUNDAMENTOS/KERNEL V2.docx.pdf` (85pp) |
| C016 | T0 | `AGENTS.md` | Governance: `Projeto 1 - ORYX Agent/01_Governanca_Geral/CEE-001*, GMC-001*, SDD-001*, PPQ-001*` |
| C017 | T1 | `.claude/skills/harness-eval/SKILL.md` | Evaluate a repo agent harness (AGENTS.md, rules, skills, skill refs) for broken paths/commands, redundant instructions, and usefulness using a stack-agnostic dual-judge protocol with planted traps. HIGH PRIORITY questionnaires at top: Q1 optional docs, Q2 B/C budget before Track A (certainty/tokens). A always runs after Q2; B/C opt-in. ADRs/RFCs excluded from T2. Mixed apply uses 11-mixed-apply.md (KEEP/CUT). Use when the user says harness eval, harness-eval, harness debug, audit AGENTS.md, audi |
| C018 | T1 | `.claude/skills/harness-eval/SKILL.md` | Run a full, stack-agnostic harness evaluation and stop at reports. Do not auto-edit AGENTS.md or skills unless the user explicitly asks after reviewing Ship/Slim. |
| C019 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Stop and ask before continuing.** Do not skip these gates. Do not silently include optional docs or spawn B/C judges. |
| C020 | T1 | `.claude/skills/harness-eval/SKILL.md` | Order after inventory: **Q1 (if needed) → Q2 → then Track A** (A always runs) → B/C only if approved. |
| C021 | T1 | `.claude/skills/harness-eval/SKILL.md` | When `optional-docs-candidates.md` lists optional types, ask before Q2 / Track A: |
| C022 | T1 | `.claude/skills/harness-eval/SKILL.md` | Re-run inventory with `--include-doc-type` / `--include-doc` only after the user answers. If no optional types, skip Q1. |
| C023 | T1 | `.claude/skills/harness-eval/SKILL.md` | Ask **before** Track A so the user sets spend up front. Track **A always runs** next (deterministic, ~0 model tokens). B/C run only if approved. |
| C024 | T1 | `.claude/skills/harness-eval/SKILL.md` | Fill claim count from `claims.md` when known; surface count ≈ T0+T1+T2 markdown after extract (or say “after surfaces_extract” if not run yet). |
| C025 | T1 | `.claude/skills/harness-eval/SKILL.md` | **`A only`:** run Track A; present `04`; stop (no B/C judges). |
| C026 | T1 | `.claude/skills/harness-eval/SKILL.md` | **`B`:** Track A, then Steps 4–6. |
| C027 | T1 | `.claude/skills/harness-eval/SKILL.md` | **`C`:** Track A, then Steps 7–10 (C does not need B). |
| C028 | T1 | `.claude/skills/harness-eval/SKILL.md` | **`B+C`:** Track A, then Steps 4–11. |
| C029 | T1 | `.claude/skills/harness-eval/SKILL.md` | If the user already requested B/C/`full eval` in the triggering message, treat as approval — still show the Q2 table once so costs are visible. |
| C030 | T1 | `.claude/skills/harness-eval/SKILL.md` | This skill is **self-contained**. Protocol, scripts, and judge prompts live under this skill directory (the folder that contains this `SKILL.md`). Resolve `SKILL_DIR` as that directory — never assume another install path. |
| C031 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read [references/PROTOCOL.md](references/PROTOCOL.md) **completely** before the first run in a session (and again if scripts fail). |
| C032 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read [references/judge-prompts.md](references/judge-prompts.md) when spawning Track B or Track C judges. |
| C033 | T1 | `.claude/skills/harness-eval/SKILL.md` | Plain-language terms: [references/GLOSSARY.md](references/GLOSSARY.md) (also embedded at the top of `04` / `07` / `10` reports). |
| C034 | T1 | `.claude/skills/harness-eval/SKILL.md` | Claim record shape: [references/claims.schema.json](references/claims.schema.json) (for tooling; agents do not need to load it every run). |
| C035 | T1 | `.claude/skills/harness-eval/SKILL.md` | Run scripts as `python3 "$SKILL_DIR/scripts/<name>.py" ...`. |
| C036 | T1 | `.claude/skills/harness-eval/SKILL.md` | Run **outputs** (not protocol) go to the target repo at `.harness-eval/runs/<run-id>/`. |
| C037 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Report-only by default.** Judgment ≠ remediation. |
| C038 | T1 | `.claude/skills/harness-eval/SKILL.md` | **README out of scope** as harness surface and as rediscovery/usefulness evidence. |
| C039 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Stack-agnostic.** Never hard-code package managers, DBs, frameworks, or folder layouts in prompts or plants. Discover manifests that exist (JS, Python, Make/Task, Rust, Go, PHP, Ruby/Rails, Java/Gradle/Maven, plus `bin/*`). |
| C040 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Doc scope.** T2 always includes agent skill-tree refs (`.agents/skills`, `.cursor/skills`, `.claude/skills`). **ADRs / RFCs (decision-record trees) are always excluded** from T2 surfaces. Other cited project docs are **optional** — default omit; ask via **Q1** at the top of this skill, then re-run with `--include-doc-type` / `--include-doc`. |
| C041 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Track A always runs** after inventory (deterministic, high-precision). Prefer false negatives over false BROKEN. Placeholders (`SPEC_FOLDER`, `{x}`, `[feature]`) are never BROKEN. Never normalize paths with `str.lstrip('./')`. |
| C042 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Tracks B and C require user approval via Q2 before Track A.** Do not spawn B/C judges until the user opts in. User may approve B only, C only, both, or A only. |
| C043 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Track B needs dual judges + plants.** Judge2 is blind (must not read Judge1 scores or `trap-key.json`). Ship only if trap gate PASS and dual REDUNDANT with Judge2 cost ≤ 1. |
| C044 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Track C needs dual judges + plants.** Blind Judge2 must not read `08-usefulness-j1.md` or `usefulness-trap-key.json`. Slim only if trap PASS, dual SLIM/ROUTING-ONLY, **and fan-in PASS** (no other harness surface hard-loads the path as SoT — merge enforces this on the full skill tree, not just `--seed`). **Usefulness is model-sensitive** — record `model: <id>` in both score files; prefer same model within a run; re-judge on a second model before large Slim deletes. |
| C045 | T1 | `.claude/skills/harness-eval/SKILL.md` | **KEEP / KEEP-CORE plants must not be verbatim copies** of claims/surfaces already in the deck. |
| C046 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Subagents:** use an allowlisted non-fast model (prefer the same family as the parent when policy allows). Do not use `*-fast` models. |
| C047 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Do not equate tracks.** Track B Ship ≠ Track C Slim. Rediscoverable ≠ useless; useful ≠ non-redundant. |
| C048 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Slim apply / fan-in.** Never stub or delete a Slim path listed under “Slim fan-in blocked” (or when `python3 "$SKILL_DIR/scripts/slim_fanin.py" --path <P>` reports citers) unless those consumers are updated in the same change. |
| C049 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Mixed/Slim apply stays self-contained.** Cutting REPO-DEMONSTRATED / THEORY means delete or compress that bulk in the harness surface. Never replace a fenced teaching snippet (or the contract it carried) with `See app/...` / `lib/...` / `test/...` — that swaps SoT for a code-tree pointer. Judge evidence paths stay in score tables only; if the behavior-changing contract must survive, keep a short in-skill rule or snippet. |
| C050 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Mixed apply is mechanical.** Dual MIXED alone is not enough. Merge emits `11-mixed-apply.md` with per-ID **KEEP** (from Keep-core columns) and **CUT** (from Slim columns). Apply agents must follow that file only — do not re-judge, redesign, or invent a different pattern than KEEP. Empty Keep-core/Slim cells → skip that path (Hold). |
| C051 | T1 | `.claude/skills/harness-eval/SKILL.md` | Set `SKILL_DIR` to the directory containing this `SKILL.md`. Verify: |
| C052 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/references/PROTOCOL.md` |
| C053 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/inventory_extract.py` |
| C054 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/track_a_correctness.py` |
| C055 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/merge_agreement.py` |
| C056 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/surfaces_extract.py` |
| C057 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/merge_usefulness.py` |
| C058 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/slim_fanin.py` |
| C059 | T1 | `.claude/skills/harness-eval/SKILL.md` | `$SKILL_DIR/scripts/doc_scope.py` |
| C060 | T1 | `.claude/skills/harness-eval/SKILL.md` | If missing, the skill install is broken — stop. |
| C061 | T1 | `.claude/skills/harness-eval/SKILL.md` | From the **target repo root**: |
| C062 | T1 | `.claude/skills/harness-eval/SKILL.md` | Expected under `.harness-eval/runs/$RUN_ID/`: `inventory.json`, `claims.jsonl`, `claims.md`, `trap-key.json`, `optional-docs-candidates.md` (+ `.json`). |
| C063 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read `optional-docs-candidates.md`. If optional types exist, run **Q1** from [User questionnaires](#user-questionnaires-high-priority). Re-run inventory only after approval: |
| C064 | T1 | `.claude/skills/harness-eval/SKILL.md` | Run **Q2** from [User questionnaires](#user-questionnaires-high-priority) **before** Track A. Record the answer (`A only` / `B` / `C` / `B+C`). Do not start Steps 4+ unless B and/or C were approved. |
| C065 | T1 | `.claude/skills/harness-eval/SKILL.md` | Expected: `04-correctness.md` (includes term definitions at top). Spot-check that `.agents/...` cites resolve (not `agents/...`). |
| C066 | T1 | `.claude/skills/harness-eval/SKILL.md` | Summarize Track A (broken count + notable clusters). If Q2 was `A only`, stop. Otherwise continue to the approved B and/or C steps. |
| C067 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read `references/judge-prompts.md` (Track B Judge1). Spawn an independent subagent with an allowlisted model. Point it at `.harness-eval/runs/$RUN_ID/claims.md`. It writes `05-redundancy-j1.md` (include `model: <id>`). |
| C068 | T1 | `.claude/skills/harness-eval/SKILL.md` | Judge1 may read `inventory.json`. Must not read `trap-key.json`. |
| C069 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read `references/judge-prompts.md` (Track B Judge2). Spawn a second subagent. Writes `06-blind-scores.md`. |
| C070 | T1 | `.claude/skills/harness-eval/SKILL.md` | Forbidden for Judge2: `trap-key.json`, `05-redundancy-j1.md`, `07-agreement.md`, prior agreement reports. |
| C071 | T1 | `.claude/skills/harness-eval/SKILL.md` | Prefer Steps 4 and 5 in parallel. |
| C072 | T1 | `.claude/skills/harness-eval/SKILL.md` | Expected: `07-agreement.md` (Ship/Review/Hold + **What these words mean**). On trap FAIL: fix plants per PROTOCOL, rescore P00x, re-merge — do not Ship. |
| C073 | T1 | `.claude/skills/harness-eval/SKILL.md` | Expected: `surfaces.md`, `surfaces.json`, `usefulness-trap-key.json`. |
| C074 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read `references/judge-prompts.md` (Usefulness Judge1). Spawn subagent with allowlisted model (record same id in header). Writes `08-usefulness-j1.md`. |
| C075 | T1 | `.claude/skills/harness-eval/SKILL.md` | Must not read `usefulness-trap-key.json`. |
| C076 | T1 | `.claude/skills/harness-eval/SKILL.md` | Read Usefulness Judge2 prompt. Prefer **same model** as Step 8 for agreement stability. Writes `09-usefulness-j2.md`. |
| C077 | T1 | `.claude/skills/harness-eval/SKILL.md` | Forbidden: `usefulness-trap-key.json`, `08-usefulness-j1.md`, `10-usefulness-agreement.md`, and using Track B 05/06/07 to decide usefulness classes. |
| C078 | T1 | `.claude/skills/harness-eval/SKILL.md` | Prefer Steps 8 and 9 in parallel. |
| C079 | T1 | `.claude/skills/harness-eval/SKILL.md` | Expected: `10-usefulness-agreement.md` (Slim/Keep-core/Mixed/Hold + **What these words mean**), `11-mixed-apply.md` (KEEP/CUT per Mixed ID), plus `slim-fanin.json`. On trap FAIL: do not Slim. Surfaces with `slim-fanin-blocked` are Hold — not Slim apply candidates. |
| C080 | T1 | `.claude/skills/harness-eval/SKILL.md` | Summarize from the agreement reports (each starts with term definitions): |
| C081 | T1 | `.claude/skills/harness-eval/SKILL.md` | Track A broken count → `04-correctness.md` |
| C082 | T1 | `.claude/skills/harness-eval/SKILL.md` | Track B trap + Ship/Review/Hold → `07-agreement.md` |
| C083 | T1 | `.claude/skills/harness-eval/SKILL.md` | Track C trap + fan-in + Slim/Keep-core/Mixed/Hold → `10-usefulness-agreement.md` |
| C084 | T1 | `.claude/skills/harness-eval/SKILL.md` | Call out `11-mixed-apply.md` when Mixed count > 0 (the only Mixed apply path) |
| C085 | T1 | `.claude/skills/harness-eval/SKILL.md` | Call out model ids used for Track C and that Slim is model-sensitive |
| C086 | T1 | `.claude/skills/harness-eval/SKILL.md` | Call out any **Slim fan-in blocked** rows (consumers outside seed may appear here) |
| C087 | T1 | `.claude/skills/harness-eval/SKILL.md` | Stop unless the user asks to apply Ship/Slim/Mixed. When applying: |
| C088 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Slim:** only paths in the Slim table (fan-in PASS); never stub fan-in-blocked paths without updating citers first. |
| C089 | T1 | `.claude/skills/harness-eval/SKILL.md` | **Mixed:** open `11-mixed-apply.md` and execute KEEP/CUT per ID only (rule 12). Never re-judge from the Mixed path list alone. Never add code-tree path pointers as substitutes for cut demos (rule 11). |
| C090 | T1 | `.claude/skills/SKILL.md` | Use when validating SOT harness files for spec completeness, schema correctness, and constitutional compliance. Runs JSON schema validation, spec lint, and cross-agent consistency checks. |
| C091 | T1 | `.claude/skills/SKILL.md` | Use this skill when: |
| C092 | T1 | `.claude/skills/SKILL.md` | A spec file in specs/ has been modified |
| C093 | T1 | `.claude/skills/SKILL.md` | A schema file in schemas/ has been modified |
| C094 | T1 | `.claude/skills/SKILL.md` | A RAG file in rag/ has been modified |
| C095 | T1 | `.claude/skills/SKILL.md` | Before any commit or PR affecting harness files |
| C096 | T1 | `.claude/skills/SKILL.md` | **Validate JSON schemas**: run `node tests/validate-schemas.js` — all 10 schemas must pass |
| C097 | T1 | `.claude/skills/SKILL.md` | **Lint specs**: run `node tests/lint-specs.js` — all 5 specs must pass EARS + sections |
| C098 | T1 | `.claude/skills/SKILL.md` | **Check cross-agent pipeline**: verify the output of each agent matches the input of the next: |
| C099 | T1 | `.claude/skills/SKILL.md` | elliott-wave.output fields referenced in fibonacci.input |
| C100 | T1 | `.claude/skills/SKILL.md` | fibonacci.output fields referenced in smc.input |
| C101 | T1 | `.claude/skills/SKILL.md` | smc.output + all outputs referenced in synthesis.input |
| C102 | T1 | `.claude/skills/SKILL.md` | ict.input `approved_hypothesis` allows null (ICT INACTIVE state) |
| C103 | T1 | `.claude/skills/SKILL.md` | **Check constitutional guards**: for each spec, verify: |
| C104 | T1 | `.claude/skills/SKILL.md` | ICT spec: INACTIVE rule as first behavior |
| C105 | T1 | `.claude/skills/SKILL.md` | Synthesis spec: all 4 signal conditions present (score≥7, R:R≥2:1, conviction≥70%, no conflict) |
| C106 | T1 | `.claude/skills/SKILL.md` | No lower-layer agent overrides higher-layer |
| C107 | T1 | `.claude/skills/SKILL.md` | **Run harness score**: `npx harness-score` — must maintain L2 or above |
| C108 | T1 | `.claude/skills/SKILL.md` | All JSON schemas: valid JSON, have $schema/$id/title/type fields, output schemas have score field |
| C109 | T1 | `.claude/skills/SKILL.md` | All specs: have Missão/Escopo/Comportamentos/Critérios sections, have EARS notation |
| C110 | T1 | `.claude/skills/SKILL.md` | Harness score: L2 minimum (55+ points) |
| C111 | T2 | `.claude/skills/harness-eval/references/GLOSSARY.md` | Harness-referenced document `.claude/skills/harness-eval/references/GLOSSARY.md` is an on-demand load target when linked from always-on rules or skills. |
| C112 | T2 | `.claude/skills/harness-eval/references/PROTOCOL.md` | Harness-referenced document `.claude/skills/harness-eval/references/PROTOCOL.md` is an on-demand load target when linked from always-on rules or skills. |
| C113 | T2 | `.claude/skills/harness-eval/references/claims.schema.json` | Harness-referenced document `.claude/skills/harness-eval/references/claims.schema.json` is an on-demand load target when linked from always-on rules or skills. |
| C114 | T2 | `.claude/skills/harness-eval/references/judge-prompts.md` | Harness-referenced document `.claude/skills/harness-eval/references/judge-prompts.md` is an on-demand load target when linked from always-on rules or skills. |
| P001 | T0 | `AGENTS.md` | Run the project script `test` when you need that workflow. |
| P002 | T0 | `AGENTS.md` | Run the project script `lint` when you need that workflow. |
| P003 | T1 | `.agents/skills/workflow-tips/SKILL.md` | Prefer clear variable names and small functions when writing code. |
| P004 | T1 | `.agents/skills/workflow-tips/SKILL.md` | Keep layers thin and delegate work to the appropriate lower layer. |
| P005 | T0 | `AGENTS.md` | Never commit secrets, API keys, or credentials into the repository; use environment configuration outside version control. |
| P006 | T0 | `AGENTS.md` | Known caveat: commands that pass locally can still fail in CI when they depend on machine-local env vars or secrets that are not present in the pipeline; prefer the project's documented CI entrypoint when validating. |

## Output

Write scores as a table: `| ID | Cost | Class | Evidence | Confidence | Trim suggestion |`

