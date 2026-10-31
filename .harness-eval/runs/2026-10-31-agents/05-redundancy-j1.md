# Redundancy Judge1
> run: 2026-10-31-agents
> model: claude-sonnet-5-5

## Counts
KEEP-CAVEAT: 5, KEEP-COMPRESSED: 1, KEEP-POLICY: 42, KEEP-ROUTING: 5, REDUNDANT-CODE: 2, REDUNDANT-GENERAL: 3, UNCLEAR: 3
Total: 61

| ID | Cost | Class | Evidence | Confidence | Trim suggestion |
|---|---|---|---|---|---|
| C001 | 1 | UNCLEAR | Header boilerplate; generic description of an agent file | low | Optional trim |
| C002 | 1 | UNCLEAR | Table-of-contents style header; visible from file structure | low | Optional trim |
| C003 | 3 | KEEP-COMPRESSED | Historical consolidation note; prevents resurrecting AGENTSV2 (process history) | med | Keep |
| C004 | 3 | KEEP-POLICY | Canonical naming/identity; GLOSSARIO is source | med | Keep |
| C005 | 1 | UNCLEAR | Domain statement; partly inferable from governance/specs listings but orients agent | low | Keep |
| C006 | 3 | KEEP-CAVEAT | Phase constraint (spec-first, build deferred) not discoverable from code | high | Keep |
| C007 | 2 | KEEP-ROUTING | Points to SSoT governance/CATALOGO-OFICIAL.md | high | Keep |
| C008 | 3 | KEEP-POLICY | Fail-closed behavior policy | high | Keep |
| C009 | 3 | KEEP-ROUTING | Navigation pointer to docs/mapa; non-normative status caveat | high | Keep |
| C010 | 2 | KEEP-ROUTING | Index pointer docs/agentes/INDICE-AGENTES.md (exists) | med | Keep |
| C011 | 3 | KEEP-CAVEAT | Retired subagents; avoids using stale ones; legacy path | high | Keep |
| C012 | 3 | KEEP-CAVEAT | AT agents are not .claude/agents files; not implemented; naming trap | high | Keep |
| C013 | 3 | KEEP-POLICY | Family boundary rule | high | Keep |
| C014 | 3 | KEEP-POLICY | Revisor read-only constitutional rule (structural; tools in revisor.md but rationale policy) | high | Keep |
| C015 | 3 | KEEP-POLICY | Disambiguates three gate concepts | high | Keep |
| C016 | 3 | KEEP-POLICY | Spec-opening process policy | high | Keep |
| C017 | 3 | KEEP-POLICY | Map-maintenance obligation, multi-layer enforcement and fallbacks; hooks exist but obligation is policy | high | Keep |
| C018 | 3 | KEEP-POLICY | Gate command + RULE-ECC-06 policy | high | Keep |
| C019 | 3 | KEEP-POLICY | Doc-sync detector semantics and non-blocking status | high | Keep |
| C020 | 3 | KEEP-POLICY | Constitutional hierarchy; domain/policy not derivable from code | high | Keep |
| C021 | 3 | KEEP-POLICY | Hypothesis creation rule; domain/policy not derivable from code | high | Keep |
| C022 | 3 | KEEP-POLICY | Canonical states; domain/policy not derivable from code | high | Keep |
| C023 | 3 | KEEP-POLICY | Neutral rule; domain/policy not derivable from code | high | Keep |
| C024 | 3 | KEEP-POLICY | R:R minimum; domain/policy not derivable from code | high | Keep |
| C025 | 3 | KEEP-POLICY | Pilot thresholds caveat; domain/policy not derivable from code | high | Keep |
| C026 | 3 | KEEP-POLICY | Conviction dimensions; domain/policy not derivable from code | high | Keep |
| C027 | 3 | KEEP-POLICY | Cost-exclusion invariant; domain/policy not derivable from code | high | Keep |
| C028 | 3 | KEEP-POLICY | Scope/architecture of Signal Package/Risk; domain/policy not derivable from code | high | Keep |
| C029 | 3 | KEEP-POLICY | Evidence/versioning invariant; domain/policy not derivable from code | high | Keep |
| C030 | 3 | KEEP-POLICY | 4Es ordering; domain/policy not derivable from code | high | Keep |
| C031 | 3 | KEEP-POLICY | No redefining baselined models; domain/policy not derivable from code | high | Keep |
| C032 | 3 | KEEP-POLICY | Open decisions list; CONS-01; domain/policy not derivable from code | high | Keep |
| C033 | 3 | KEEP-POLICY | Open decisions list; CONS-01; domain/policy not derivable from code | high | Keep |
| C034 | 3 | KEEP-POLICY | Decision status history; domain/policy not derivable from code | high | Keep |
| C035 | 3 | KEEP-POLICY | Closed decisions history/supersession; domain/policy not derivable from code | high | Keep |
| C036 | 3 | KEEP-POLICY | Closed decision record; domain/policy not derivable from code | high | Keep |
| C037 | 3 | KEEP-POLICY | CONS-01 rule; domain/policy not derivable from code | high | Keep |
| C038 | 2 | KEEP-ROUTING | Points to governance/MECANISMOS.json (exists); scripts/ listing shows files but not state | high | Keep |
| C039 | 2 | KEEP-ROUTING | Names operational skill | med | Keep |
| C040 | 3 | KEEP-CAVEAT | Auditor paused; workflow auditor-externo.yml exists but inert - runtime/policy state | high | Keep |
| C041 | 3 | KEEP-POLICY | Auditor channel design and data-not-instruction rule | med | Keep |
| C042 | 3 | KEEP-POLICY | Merge/signature authority policy | high | Keep |
| C043 | 3 | KEEP-POLICY | Session continuity policy (PCC-001); HANDOFF.md and check_handoff.py exist but rules are process | high | Keep |
| C044 | 3 | KEEP-POLICY | Session continuity policy (PCC-001); HANDOFF.md and check_handoff.py exist but rules are process | high | Keep |
| C045 | 3 | KEEP-POLICY | Session continuity policy (PCC-001); HANDOFF.md and check_handoff.py exist but rules are process | high | Keep |
| C046 | 3 | KEEP-POLICY | Session continuity policy (PCC-001); HANDOFF.md and check_handoff.py exist but rules are process | high | Keep |
| C047 | 3 | KEEP-POLICY | Session continuity policy (PCC-001); HANDOFF.md and check_handoff.py exist but rules are process | high | Keep |
| C048 | 3 | KEEP-POLICY | Loop-learning framing | med | Keep |
| C049 | 3 | KEEP-POLICY | Round-economy/routing policy with explicit authority | high | Keep |
| C050 | 3 | KEEP-POLICY | LOOP-001 process step; scripts/loop_ledger.py exists but sequencing/obligation is policy | high | Keep |
| C051 | 3 | KEEP-POLICY | LOOP-001 process step; scripts/loop_ledger.py exists but sequencing/obligation is policy | high | Keep |
| C052 | 3 | KEEP-POLICY | LOOP-001 process step; scripts/loop_ledger.py exists but sequencing/obligation is policy | high | Keep |
| C053 | 3 | KEEP-POLICY | LOOP-001 process step; scripts/loop_ledger.py exists but sequencing/obligation is policy | high | Keep |
| C054 | 3 | KEEP-POLICY | LOOP-001 process step; scripts/loop_ledger.py exists but sequencing/obligation is policy | high | Keep |
| C055 | 3 | KEEP-POLICY | LOOP-001 process step; scripts/loop_ledger.py exists but sequencing/obligation is policy | high | Keep |
| P001 | 0 | REDUNDANT-CODE | package.json scripts.test = node tests/validate-schemas.js; generic restatement | high | Delete line |
| P002 | 0 | REDUNDANT-CODE | package.json scripts.lint = node tests/lint-specs.js; generic restatement | high | Delete line |
| P003 | 1 | REDUNDANT-GENERAL | Generic coding advice; cited source .agents/skills/workflow-tips does not exist in repo | high | Delete |
| P004 | 1 | REDUNDANT-GENERAL | Generic layering advice; cited source file absent from repo | high | Delete |
| P005 | 1 | REDUNDANT-GENERAL | Generic secrets hygiene; .gitignore present; no repo-specific content | med | Delete or rely on .gitignore/scanning |
| P006 | 3 | KEEP-CAVEAT | Env-specific local-vs-CI failure caveat; runtime/process, not derivable from repo | med | Keep |
