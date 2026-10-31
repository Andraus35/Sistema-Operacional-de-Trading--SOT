# Blind scores Judge2
> run: 2026-10-31-agents
> model: claude-sonnet-5-5

## Counts summary
| Class | Count |
|---|---|
| REDUNDANT-CODE | 2 |
| REDUNDANT-GENERAL | 6 |
| KEEP-POLICY | 36 |
| KEEP-CAVEAT | 7 |
| KEEP-ROUTING | 8 |
| KEEP-COMPRESSED | 0 |
| UNCLEAR | 2 |
| Total | 61 |

Notes: `.agents/skills/workflow-tips/SKILL.md` does not exist in the repo (P003/P004 scored on generic content). package.json has `test` and `lint` scripts (P001/P002). `.gitignore` covers .env*/secrets/ (P005).

| ID | Cost | Class | Evidence | Confidence | Trim suggestion |
|---|---|---|---|---|---|
| C001 | 1 | REDUNDANT-GENERAL | Self-description of the file; agents know AGENTS.md is read at start | med | Cut |
| C002 | 1 | REDUNDANT-GENERAL | Table-of-contents sentence; visible from headings | med | Cut |
| C003 | 1 | REDUNDANT-GENERAL | Changelog of a merge; AGENTSV2.md absent from repo, no action implied | med | Cut |
| C004 | 3 | KEEP-ROUTING | Names canonical project/alias; GLOSSARIO.md exists, not derivable from code | med | Keep |
| C005 | 1 | KEEP-ROUTING | Domain statement, not in manifests; orients specs | low | Keep |
| C006 | 3 | KEEP-CAVEAT | Phase constraint (code deferred) not derivable; prevents wrong work | high | Keep |
| C007 | 3 | KEEP-ROUTING | Points to SSoT governance/CATALOGO-OFICIAL.md | high | Keep |
| C008 | 3 | KEEP-POLICY | Fail-closed behavior on missing ROADMAP/atomic-spec; both exist at root | high | Keep |
| C009 | 2 | KEEP-ROUTING | docs/mapa/MAPA-PROJETO.md exists; non-normative nav pointer with rationale | med | Could shorten |
| C010 | 1 | KEEP-ROUTING | docs/agentes/INDICE-AGENTES.md exists; pointer | med | Keep |
| C011 | 2 | KEEP-CAVEAT | Only especificador.md/revisor.md in .claude/agents; explains absence of retired agents | low | Shorten to one clause |
| C012 | 3 | KEEP-CAVEAT | Clarifies AT are not agent files; prevents misreading; partly visible from listing | med | Keep |
| C013 | 3 | KEEP-POLICY | Boundary rule AC vs AT | high | Keep |
| C014 | 2 | KEEP-POLICY | Revisor tools read-only is in frontmatter, but statement is a constitutional rule | med | Keep |
| C015 | 3 | KEEP-POLICY | Terminology distinction among gates; process | high | Keep |
| C016 | 3 | KEEP-POLICY | Spec opening process, fail-closed Dossier | high | Keep |
| C017 | 3 | KEEP-POLICY | Maintenance duty for map; hooks (map-sync.js) and build_map.py exist but duty on fallback is process | med | Could shorten layers description |
| C018 | 3 | KEEP-POLICY | validate_spec_sot.py, check_repo_research.py exist; rule semantics not derivable | high | Keep |
| C019 | 3 | KEEP-POLICY | check_doc_sync.py exists; detector semantics and policy | med | Shorten (a)-(e) detail to pointer to script |
| C020 | 3 | KEEP-POLICY | Domain hierarchy invariant | high | Keep |
| C021 | 3 | KEEP-POLICY | Domain invariant | high | Keep |
| C022 | 3 | KEEP-POLICY | Domain invariant | high | Keep |
| C023 | 3 | KEEP-POLICY | Domain invariant | high | Keep |
| C024 | 3 | KEEP-POLICY | Domain invariant | high | Keep |
| C025 | 3 | KEEP-CAVEAT | Pilot thresholds, not definitive | high | Keep |
| C026 | 3 | KEEP-POLICY | Domain invariant plus open decision J-001 | high | Keep |
| C027 | 3 | KEEP-POLICY | Domain invariant | high | Keep |
| C028 | 3 | KEEP-POLICY | Architecture boundary (no order execution) with decision history | med | Shorten parentheticals |
| C029 | 3 | KEEP-POLICY | Constitutional invariants | high | Keep |
| C030 | 3 | KEEP-POLICY | Prioritization rule | high | Keep |
| C031 | 3 | KEEP-POLICY | CONST-01 no-redefinition of baselines | high | Keep |
| C032 | 3 | KEEP-POLICY | Open/closed decision state (CONS-01); ROADMAP is source | med | Could point to ROADMAP instead of duplicating |
| C033 | 3 | KEEP-POLICY | Open decision state, with preserved prior text per INV-07 | med | Could shorten |
| C034 | 3 | KEEP-POLICY | Decision state record | med | Could shorten |
| C035 | 3 | KEEP-POLICY | Decision state record | med | Could shorten |
| C036 | 3 | KEEP-POLICY | Decision record | med | Could shorten |
| C037 | 3 | KEEP-POLICY | CONS-01 rule | high | Keep |
| C038 | 3 | KEEP-ROUTING | governance/MECANISMOS.json routing; COE-14 PR requirement; scripts exist | high | Keep |
| C039 | 1 | UNCLEAR | tlc-spec-lean skill pointer; not verified in skill listing here | low | Keep unless skill absent |
| C040 | 3 | KEEP-CAVEAT | Auditor paused; workflow inert, prevents wrong use | high | Keep |
| C041 | 3 | UNCLEAR | Design description of paused pilot; likely long and not in operation | med | Shorten drastically given paused |
| C042 | 3 | KEEP-POLICY | Merge/sign-off authority policy | high | Keep |
| C043 | 3 | KEEP-ROUTING | Session start procedure; HANDOFF.md exists | high | Keep |
| C044 | 3 | KEEP-POLICY | Write-authority rule | high | Keep |
| C045 | 3 | KEEP-POLICY | Delivery-completeness rule | high | Keep |
| C046 | 3 | KEEP-POLICY | Detector vs gate, non-blocking; check_handoff.py and handoff-hook.js exist | med | Keep |
| C047 | 3 | KEEP-POLICY | Attachment process rule | med | Keep |
| C048 | 3 | KEEP-POLICY | Intro to loop rule; framing | med | Keep |
| C049 | 3 | KEEP-POLICY | Process rule with superseded text; aplicar_ficha_m.py exists | med | Remove preserved superseded text |
| C050 | 3 | KEEP-POLICY | Format spec for findings block | high | Keep |
| C051 | 2 | KEEP-ROUTING | loop_ledger.py exists; command plus commit duty | med | Keep |
| C052 | 3 | KEEP-POLICY | Process rule | high | Keep |
| C053 | 3 | KEEP-POLICY | Process rule | high | Keep |
| C054 | 3 | KEEP-POLICY | Process gate before opening next Spec | high | Keep |
| C055 | 3 | KEEP-CAVEAT | Ledger is detector, indicative only | med | Keep |
| P001 | 0 | REDUNDANT-CODE | package.json scripts.test = "node tests/validate-schemas.js" | high | Cut |
| P002 | 0 | REDUNDANT-CODE | package.json scripts.lint = "node tests/lint-specs.js" | high | Cut |
| P003 | 1 | REDUNDANT-GENERAL | Generic coding advice; source SKILL.md absent | high | Cut |
| P004 | 1 | REDUNDANT-GENERAL | Generic layering advice, no repo-specific content | high | Cut |
| P005 | 1 | REDUNDANT-GENERAL | Generic secrets hygiene; .gitignore already ignores .env*/secrets/ | high | Cut |
| P006 | 3 | KEEP-CAVEAT | Environment-specific CI vs local failure caveat; runtime behavior | high | Keep |
