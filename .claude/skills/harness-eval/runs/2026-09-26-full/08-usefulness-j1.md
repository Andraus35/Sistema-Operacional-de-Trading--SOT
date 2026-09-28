# Usefulness Judge1
> run: 2026-09-26-full
> model: claude-sonnet-5

## Counts by Overall class
- KEEP-CORE: 16 (S001, S004, S005, S006, S013, S014, S017, S018, S019, S020, S021, S022, S010, S012, S008, S009)
- MIXED: 4 (S002, S003, S011, S016)
- SLIM: 4 (S015, S901, S902, S007)
- ROUTING-ONLY: 0
- UNCLEAR: 1 (S903)

(Total 25. S903 is UNCLEAR: generic rule with no repo module evidence; S902 is SLIM.)

| ID | Overall | Keep-core | Slim | Overlap cites | Evidence | Confidence |
|---|---|---|---|---|---|---|
| S001 | KEEP-CORE | BEHAVIOR-CHANGING: mandatory-reading gate (ROADMAP/atomic-spec), profiles pinados, flow with validate_spec_sot.py, non-negotiables 1-12, open decisions | none | - | AGENTS.md is the entry point; .claude/agents/especificador.md and revisor.md cite ROADMAP.md/atomic-spec.md/CATALOGO-OFICIAL | high |
| S002 | MIXED | BEHAVIOR-CHANGING: Q1/Q2 questionnaires, Critical rules, Steps 1-10 | THEORY/OVERLAP: prose duplicating references/PROTOCOL.md | .claude/skills/harness-eval/references/PROTOCOL.md | Loads PROTOCOL.md, judge-prompts, GLOSSARY.md (SKILL.md refs) | medium |
| S003 | MIXED | BEHAVIOR-CHANGING: 4Es hierarchy, BASpec/D0-D9 depth model, grammars, spec template | OVERLAP: 4Es/D0-D9/profiles restated from atomic-spec.md and GEH-001; THEORY: ETCLOVG taxonomy, centralize-vs-decentralize essays | atomic-spec.md; RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md; AGENTS.md sec.4 | Cites GEH-001 and CONFLICT-MAP; profiles repeated in AGENTS.md sec.4 | medium |
| S004 | KEEP-CORE | BEHAVIOR-CHANGING: PAP-001 mission, context table with corrected paths, 6 blocks, K-PAP decisions, autopre-check | none | - | Skill cites GEH-001, GPR-001, PP-PAP-001, RULES.md, CONSTITUTION as required loads; task-specific | medium |
| S005 | KEEP-CORE | BEHAVIOR-CHANGING: Especificador role, RW tools, load order, autopre-check, spec obligations | none (large but normative agent definition) | Some restatement of AGENTS.md sec.6 (partial OVERLAP, not slimmable without evidence) | Agent file is what runtime loads; cites CATALOGO-OFICIAL, RULES.md, ROADMAP.md | medium |
| S006 | KEEP-CORE | BEHAVIOR-CHANGING: Revisor RO protocol, Passo 0, validator gate, parecer format, RULES.md access requirement (memory: revisor-requer-rules-md-completo) | none | - | AGENTS.md sec.3 ENF-03; agent file is the runtime definition | medium |
| S007 | SLIM | ROUTING-ONLY: term list needed by judges | THEORY: definitions of general audit terms, likely restated in PROTOCOL.md | .claude/skills/harness-eval/references/PROTOCOL.md | Mandated by harness-eval/SKILL.md and PROTOCOL.md load list, so keep short rather than delete | low |
| S008 | KEEP-CORE | BEHAVIOR-CHANGING: track protocol, scoring rules, merge steps | none | Partly summarized in harness-eval/SKILL.md | Hard-loaded by .claude/skills/harness-eval/SKILL.md | medium |
| S009 | KEEP-CORE | BEHAVIOR-CHANGING: judge prompt templates (exact output format) | none | - | Hard-loaded by .claude/skills/harness-eval/SKILL.md | medium |
| S010 | KEEP-CORE | BEHAVIOR-CHANGING: rule to run build_map.py and --check after md edits, never hand-edit docs/mapa | none | AGENTS.md sec.2 mentions the map (does not carry the regeneration steps) | Cline-only rule; hooks not run in Cline; scripts/build_map.py | medium |
| S011 | MIXED | BEHAVIOR-CHANGING: canonical term equivalences, ORYX=SOT, terms used by agents | THEORY: historical naming narrative | AGENTS.md sec.1 partially restates name | Cited by AGENTS.md as canonical glossary; no other harness surface hard-loads it | low |
| S012 | KEEP-CORE | BEHAVIOR-CHANGING: GEH-001 methodology (4Es, ETCLOVG, harness coverage) as normative source | none proven | Overlaps in part with .claude/skills/SKILL.md (S003) which derives from it; direction ambiguous | Cited by sot-especificador-pap001/SKILL.md and .claude/skills/SKILL.md as source of truth | medium |
| S013 | KEEP-CORE | BEHAVIOR-CHANGING: Spec sequence, authorized Spec, open decisions | none | - | Mandatory read per AGENTS.md sec.1; cited by both agents and pap001 skill | high |
| S014 | KEEP-CORE | BEHAVIOR-CHANGING: BASpec, D0-D9, Enforcement Contract, labeling | none | S003 restates parts (S003 is the overlapping side) | Mandatory read per AGENTS.md sec.1; cited by both agents | high |
| S015 | SLIM | ROUTING-ONLY: RMR-001 register line and activation trigger (Em espera) | THEORY/OVERLAP: rich context on Risk Agent already normative in RULES/EUA-E19a; admission-act template | governance/RULES.md; governance/CATALOGO-OFICIAL.md (memory: EUA-E19a homologated, BL-018 Em espera) | Backlog item, not consumed by any agent or skill (grep: only AGENTS.md mentions BL-018 marginally); deferred until FASE 6 | low |
| S016 | MIXED | ROUTING-ONLY: hub of IDs to defining doc and title index (locator) | OVERLAP: lists of doc titles regenerable via scripts/build_map.py; generated, non-normative | governance/CATALOGO-OFICIAL.md (authoritative locator); .clinerules/sot-map.md | AGENTS.md sec.2 states non-normative and generated | medium |
| S017 | KEEP-CORE | BEHAVIOR-CHANGING: SSoT of baseline state per artifact | none | - | AGENTS.md sec.1 names it source of truth; cited by both agents | high |
| S018 | KEEP-CORE | BEHAVIOR-CHANGING: conflict resolution rules | none proven | - | Cited by AGENTS.md, both agents, pap001 skill, S003 | high |
| S019 | KEEP-CORE | BEHAVIOR-CHANGING: 14 principles, hierarchy, Blackboard, 4Es | none (AGENTS.md sec.6 is a digest, not a replacement) | AGENTS.md sec.6 partial digest | Cited by AGENTS.md, sot-spec-reviewer.md, pap001 skill | high |
| S020 | KEEP-CORE | BEHAVIOR-CHANGING: principles and relations guide GPR-001 (Especificador/Revisor reference) | none proven | - | Cited by AGENTS.md and sot-especificador-pap001/SKILL.md; PAP-001 adheres to it | medium |
| S021 | KEEP-CORE | BEHAVIOR-CHANGING: PAP-001 starter package | none proven (PAP-001 homologated, memory) | Possible historical overlap with the homologated PAP-001 itself | Hard-cited by sot-especificador-pap001/SKILL.md | low |
| S022 | KEEP-CORE | BEHAVIOR-CHANGING: numbered rules with sources (RULE-BB, RULE-HG/HV, etc.) | none | - | Revisor cannot review without it (memory: revisor-requer-rules-md-completo); cited by agents, AGENTS.md, skills | high |
| S901 | SLIM | none | THEORY: generic clean-coding advice (SOLID, small functions); model prior | none in harness | No repo code; nothing project-specific; behavior unchanged if deleted | high |
| S902 | SLIM | none | THEORY: marketing-style claims ("Works with natural language", "most efficient first step") | none in harness | No actionable instruction; no path or command | high |
| S903 | UNCLEAR | BEHAVIOR-CHANGING in principle: module boundary / public API only rule | possibly THEORY if no modules exist | none | Repo is spec-only with no application modules (AGENTS.md sec.1 Fase: Spec-first); rule cannot be verified against any code | medium |
