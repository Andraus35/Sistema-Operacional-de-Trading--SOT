# Mixed apply plan (Track C)

> Run dir: `C:\Users\André\Desktop\ORYX AGENT\SOT-Harness\.harness-eval\runs\2026-09-11-full`
> Judges: J1 model=`copilot-default` · J2 model=`copilot-default`
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

### S003 — `.claude/skills/SKILL.md`

- Tier: `T1` · Name: `skills`
- Overall: J1 `MIXED` · J2 `MIXED`

#### KEEP (do not remove or degrade)

- **J1:** `KEEP: 4E/ETCLOVG governance constraints, lazy activation hierarchy, BASpec and D0-D9 requirements, quality gates, constitutional guards, and validation criteria (BEHAVIOR-CHANGING)`
- **J2:** [BEHAVIOR-CHANGING] Keep the 4Es hierarchy, lazy-by-evidence activation rule, BASpec fields, D0-D9 requirements by complexity, mandatory spec template sections, quality gates L1-L4, blockers, and validation criteria.

#### CUT (only this bulk)

- **J1:** `CUT: explanatory quotations, extended generic architecture exposition, sprint roadmap, coverage snapshot, and repeated examples after the normative template/checklists remain (THEORY; OVERLAP)`
- **J2:** [THEORY] Cut the extended conceptual exposition, repeated maturity explanations, illustrative sprint prose, and coverage/status tables that do not add a new enforceable checklist item.

#### Overlap cites (context only; cut OVERLAP here only if listed under CUT)

- **J1:** `.claude/skills/harness-eval/SKILL.md`
- **J2:** `AGENTS.md`; `.claude/skills/harness-eval/SKILL.md`

---

