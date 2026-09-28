# Usefulness Judge2 (blind)
> run: 2026-09-11-full
> model: copilot-default

## Counts

- KEEP-CORE: 5
- MIXED: 1
- SLIM: 3
- ROUTING-ONLY: 0
- UNCLEAR: 0

| ID | Overall | Keep-core | Slim | Overlap cites | Evidence | Confidence |
|---|---|---|---|---|---|---|
| S001 | KEEP-CORE | [BEHAVIOR-CHANGING] Keep the constitutional rules, methodology hierarchy, agent responsibilities, validation commands, and spec conventions in AGENTS.md. | [REPO-DEMONSTRATED] Cut the directory-layout summary and generic command descriptions that are directly discoverable from the repository manifest and files. | — | `AGENTS.md` | high |
| S002 | KEEP-CORE | [BEHAVIOR-CHANGING] Keep the Q1/Q2 gates, track-specific operating steps, judge-output contracts, blind constraints, and failure-safety rules that control how harness evaluation is run. | [OVERLAP] Cut duplicated explanatory examples and troubleshooting prose once the canonical protocol and scripts remain linked. | `.claude/skills/harness-eval/references/PROTOCOL.md`; `.claude/skills/harness-eval/references/judge-prompts.md` | `.claude/skills/harness-eval/SKILL.md` | high |
| S003 | MIXED | [BEHAVIOR-CHANGING] Keep the 4Es hierarchy, lazy-by-evidence activation rule, BASpec fields, D0-D9 requirements by complexity, mandatory spec template sections, quality gates L1-L4, blockers, and validation criteria. | [THEORY] Cut the extended conceptual exposition, repeated maturity explanations, illustrative sprint prose, and coverage/status tables that do not add a new enforceable checklist item. | `AGENTS.md`; `.claude/skills/harness-eval/SKILL.md` | `.claude/skills/SKILL.md` | high |
| S004 | SLIM | [ROUTING-ONLY] Keep only the short definitions needed to interpret Track A/B/C reports and the Ship/Review/Hold/Slim/Keep-core distinctions. | [OVERLAP] Cut the expanded glossary entries and repeated track explanations; those definitions are already embedded in the evaluation skill and reports. | `.claude/skills/harness-eval/SKILL.md`; `.claude/skills/harness-eval/references/PROTOCOL.md` | `.claude/skills/harness-eval/references/GLOSSARY.md` | high |
| S005 | KEEP-CORE | [BEHAVIOR-CHANGING] Keep the agnostic constraints, inventory/doc-scope rules, correctness/redundancy/usefulness rubrics, model-sensitivity guidance, operator flow, fan-in safeguards, and safety constraints. | [OVERLAP] Cut duplicated command snippets and report terminology that can remain in the harness-eval skill or judge prompts. | `.claude/skills/harness-eval/SKILL.md`; `.claude/skills/harness-eval/references/judge-prompts.md` | `.claude/skills/harness-eval/references/PROTOCOL.md` | high |
| S006 | KEEP-CORE | [BEHAVIOR-CHANGING] Keep the exact Judge1/Judge2 prompts, blind exclusions, required headers, table schemas, allowed classes, evidence rules, and actionable MIXED-cell requirements. | [OVERLAP] Cut the duplicated Track B prompt material when only Track C judging is being invoked, while preserving the Track C prompts and parser contract. | `.claude/skills/harness-eval/SKILL.md`; `.claude/skills/harness-eval/references/PROTOCOL.md` | `.claude/skills/harness-eval/references/judge-prompts.md` | high |
| S901 | SLIM | [ROUTING-ONLY] No substantive behavior-changing core; retain at most a one-line reminder if this deck entry is used for routing. | [THEORY] Cut the generic naming, SOLID, comments, and composition advice; it supplies no SOT-specific decision rule or cited repository evidence. | — | `.harness-eval/runs/2026-09-11-full/surfaces.md` (S901 fenced body) | high |
| S902 | SLIM | [ROUTING-ONLY] Nothing here changes repository behavior; no core needs preservation. | [THEORY] Cut the generic natural-language and speed claims entirely. | — | `.harness-eval/runs/2026-09-11-full/surfaces.md` (S902 fenced body) | high |
| S903 | KEEP-CORE | [BEHAVIOR-CHANGING] Keep the prohibition on private cross-module access, the documented-public-API requirement, and the owner-module transaction/write-boundary rule. | [THEORY] Cut only the heading/formatting; do not remove the boundary policy itself. | — | `.harness-eval/runs/2026-09-11-full/surfaces.md` (S903 fenced body); `.claude/skills/harness-eval/references/PROTOCOL.md` (cross-module boundary policy rubric) | high |
