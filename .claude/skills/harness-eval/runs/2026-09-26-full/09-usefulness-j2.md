# Usefulness Judge2 (blind)
> run: 2026-09-26-full
> model: claude-sonnet-5

## Counts
- KEEP-CORE: 15
- MIXED: 3
- SLIM: 3
- ROUTING-ONLY: 1
- UNCLEAR: 3
- Total: 25

Note: read-depth was limited (deck previews plus targeted reads of S010, S015, S016, S003 and S901-S903). Rows with no confirmed body read carry Low or Medium confidence.

| ID | Overall | Keep-core | Slim | Overlap cites | Evidence | Confidence |
|---|---|---|---|---|---|---|
| S001 | KEEP-CORE | BEHAVIOR-CHANGING: §1 mandatory reading, §3 agent tools (ENF-03), §4 pinned profiles, §5 flow and determinístico gate, §6 non-negociáveis, §7 open decisions | none | none | AGENTS.md is the entry file; the hard rules (R:R, ICT creates no hypothesis, profile pinning) are not derivable from the repo listing | High |
| S002 | KEEP-CORE | BEHAVIOR-CHANGING: track protocol, Q1/Q2 budget gates, dual-judge rules | none | none | Methodology skill; its gates and rules change the agent's path (evidence-or-zero, opt-in B/C) | Medium |
| S003 | MIXED | BEHAVIOR-CHANGING: Part 2 (BASpec, D0-D9 depth, calibration), Part 3 (mandatory tagging), Part 4 (Quality Gates L1-L4), template master D0-D9 | THEORY: Part 1 (4Es, ETCLOVG, centralize vs decentralize, lazy activation) | OVERLAP: AGENTS.md §6 item 11 (4Es), atomic-spec.md (BASpec, D0-D9), RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md (Part 1 source) | Part 1 restates GEH-001 and the AGENTS.md §6 items; Part 2 restates atomic-spec.md; the template and gates operationalize the spec | Medium |
| S004 | UNCLEAR | none confirmed | none confirmed | none | Task-specific skill for producing PAP-001, which memory says was homologated 2026-09-15; unclear whether it is still triggered. No body read | Low |
| S005 | KEEP-CORE | BEHAVIOR-CHANGING: role, tool grant (RW), autopré-check, deliverable format, mandatory ROADMAP/atomic-spec reads | none | none | AGENTS.md §3 and §5 mandate this file as the Especificador definition, so the counterfactual changes behavior | High |
| S006 | KEEP-CORE | BEHAVIOR-CHANGING: read-only tool restriction, Passo 0, gate invocation, GRE-001/HRE-001 protocol, parecer format | none | none | AGENTS.md §3 (ENF-03) and §5 depend on this file; the structural read-only guarantee lives in its frontmatter | High |
| S007 | UNCLEAR | none confirmed | none confirmed | none | Harness-eval glossary of terms (3.8k chars); it may be the source of definitions for the judges, but model prior may cover it | Low |
| S008 | KEEP-CORE | BEHAVIOR-CHANGING: Track A/B/C procedures, artifacts and numbering, agreement rules | none | none | Protocol referenced by the harness-eval skill (S002) as source of truth; without it the run structure is lost | Medium |
| S009 | KEEP-CORE | BEHAVIOR-CHANGING: judge prompt contracts, table header, allowed classes, output file rules | none | none | Judge prompts are hard-loaded by the eval flow; the exact table format is enforced downstream | Medium |
| S010 | ROUTING-ONLY | ROUTING-ONLY: glob trigger plus the 3-step regenerate/check/include rule (`python scripts/build_map.py`, `--check`) | OVERLAP: the prose restating why the map is non-normative | OVERLAP: AGENTS.md §5 (Mapa do projeto BL-019) | This is the only way Cline learns the rule, since Cline does not run Claude Code hooks; AGENTS.md §5 carries the same content. The file is short (976 chars) | Medium |
| S011 | KEEP-CORE | BEHAVIOR-CHANGING: canonical terms, name equivalences (ORYX = SOT), term definitions | none | none | AGENTS.md §1 and §2 point to it as the identity and terminology authority; equivalences are not derivable from the listing | High |
| S012 | MIXED | BEHAVIOR-CHANGING: operative method rules that the Especificador applies (4Es, ETCLOVG anatomy used as a checklist, harness-coverage rules) | THEORY: methodology rationale and exposition; OVERLAP with the master reference | OVERLAP: .claude/skills/SKILL.md (Part 1: 4Es, ETCLOVG), governance/CONSTITUTION.md (4Es) | The memory index confirms it is the K-PEPR-001 source living in RETOMADA/; large size (39k) with a partial duplicate in S003 Part 1. Not read in full, so no cut is recommended without a full read | Low |
| S013 | KEEP-CORE | BEHAVIOR-CHANGING: Spec sequence, authorized Spec, slots and opening procedure (§23), active open decisions | none | none | Mandatory reading per AGENTS.md §1; omitting it makes the Revisor issue NÃO CONFORME Crítica | High |
| S014 | KEEP-CORE | BEHAVIOR-CHANGING: BASpec, D0-D9, Enforcement Contract, tagging, Dossiê method §15, INV-* invariants | none | none | Mandatory reading per AGENTS.md §1; the gate scripts/validate_spec_sot.py enforces its structure | High |
| S015 | MIXED | BEHAVIOR-CHANGING: registry row (ID, Gatilho de Ativação, Ação ao ativar), decisions to watch (J-001, CDM-001, I-001, M-001), pre-requisite EUA-E19a | THEORY: descriptive context of what the Risk Agent is; admission act template (filled after homologation) | OVERLAP: governance/CATALOGO-OFICIAL.md and ROADMAP.md (state and baseline of artifacts); memory says the BL row also lives in backlog/RMR-001 | Backlog item with a deferred trigger (FASE 6); behavior changes only when it activates. Renumbering note BL-017 to BL-018 is behavior-relevant | Medium |
| S016 | SLIM | none | REPO-DEMONSTRATED: layers, hub counts and document index are derivable by listing and opening the repo; generated output that must not be hand-edited | OVERLAP: governance/CATALOGO-OFICIAL.md (authoritative locator), AGENTS.md §2 (repo map) | It states itself as NON-NORMATIVE and regenerable; AGENTS.md §2 says it is not mandatory reading. A Cut here only affects navigation speed. Do not remove the regeneration hooks (AGENTS.md §5) | Medium |
| S017 | KEEP-CORE | BEHAVIOR-CHANGING: state and baseline of every artifact (SSoT) | none | none | AGENTS.md §1 names it "Fonte de verdade de baseline"; MAPA-PROJETO.md itself defers to it | High |
| S018 | KEEP-CORE | BEHAVIOR-CHANGING: conflict resolution rules between sources | none | none | Listed in AGENTS.md §2 under governance authority; 66 inbound refs per MAPA-PROJETO.md §1 | Medium |
| S019 | KEEP-CORE | BEHAVIOR-CHANGING: 14 principles, hierarchy, Blackboard, 4Es | none | OVERLAP (partial): AGENTS.md §6 restates a subset of the non-negociáveis | Normative constitution, which is source of the AGENTS.md §6 list; deleting it would remove authority for CONST-01 and P14 | High |
| S020 | KEEP-CORE | BEHAVIOR-CHANGING: principle relations, hierarchy of principles (GPR-001) that specs must cite | THEORY: explanatory narrative parts (unverified) | OVERLAP (partial): governance/CONSTITUTION.md | Referenced by the flow (Especificador overlay GUS-TLC-001 and inheritance via RULE-HV); not read in full, so no cut is proposed | Low |
| S021 | UNCLEAR | none confirmed | none confirmed | none | Starting package for PAP-001, which was homologated 2026-09-15; may now be historical. No body read | Low |
| S022 | KEEP-CORE | BEHAVIOR-CHANGING: numbered rules with sources (RULE-BB, RULE-HG/HV, INV-*), cited by every Spec | none | none | 96 inbound refs per MAPA-PROJETO.md §1; the Revisor cannot start without it per the memory index | High |
| S901 | SLIM | none | THEORY: generic clean-code advice (names, SOLID, composition) | none | Nothing project-specific; the repo has no application code, so the advice cannot change behavior and any model already follows it | High |
| S902 | SLIM | none | THEORY: marketing-style claims about the assistant ("works with natural language", "most efficient first step") | none | Contains no instruction, path, or command; zero behavior change | High |
| S903 | KEEP-CORE | BEHAVIOR-CHANGING: never touch another module's private storage; call only the public API; cross-module writes go through the owner's transaction boundary | none | none | Concrete, prohibitive Critical rule that changes where code goes; note this repo (Spec-first, no application code) has no modules to apply it to, hence Medium | Medium |
