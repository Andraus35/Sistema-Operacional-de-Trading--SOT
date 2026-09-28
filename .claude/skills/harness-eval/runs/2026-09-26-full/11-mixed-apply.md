# Mixed apply plan (Track C)

> Run dir: `C:\Users\André\Desktop\SOT ENGINER\SOT-Harness\.claude\skills\harness-eval\runs\2026-09-26-full`
> Judges: J1 model=`claude-sonnet-5` · J2 model=`claude-sonnet-5`
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

- **J1:** BEHAVIOR-CHANGING: 4Es hierarchy, BASpec/D0-D9 depth model, grammars, spec template
- **J2:** BEHAVIOR-CHANGING: Part 2 (BASpec, D0-D9 depth, calibration), Part 3 (mandatory tagging), Part 4 (Quality Gates L1-L4), template master D0-D9

#### CUT (only this bulk)

- **J1:** OVERLAP: 4Es/D0-D9/profiles restated from atomic-spec.md and GEH-001; THEORY: ETCLOVG taxonomy, centralize-vs-decentralize essays
- **J2:** THEORY: Part 1 (4Es, ETCLOVG, centralize vs decentralize, lazy activation)

#### Overlap cites (context only; cut OVERLAP here only if listed under CUT)

- **J1:** atomic-spec.md; RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md; AGENTS.md sec.4
- **J2:** OVERLAP: AGENTS.md §6 item 11 (4Es), atomic-spec.md (BASpec, D0-D9), RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md (Part 1 source)

---

