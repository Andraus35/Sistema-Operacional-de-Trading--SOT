# Redundancy Judge1
> run: 2026-09-26-full
> model: claude-sonnet-5

Counts: KEEP-CAVEAT=6, KEEP-COMPRESSED=22, KEEP-POLICY=193, KEEP-ROUTING=65, REDUNDANT-CODE=13, REDUNDANT-GENERAL=13, UNCLEAR=7 (total 319)

| ID | Cost | Class | Evidence | Confidence | Trim suggestion |
|---|---|---|---|---|---|
| C001 | 1 | REDUNDANT-GENERAL | Self-describing header of AGENTS.md; no behavior | medium | drop meta line |
| C002 | 1 | REDUNDANT-GENERAL | Self-describing header of AGENTS.md; no behavior | medium | drop meta line |
| C003 | 1 | REDUNDANT-GENERAL | Changelog note; AGENTSV2.md absence visible from directory listing | low | drop history note |
| C004 | 3 | KEEP-POLICY | Naming/identity policy; GLOSSARIO.md not code-derivable | high | none |
| C005 | 2 | KEEP-POLICY | Domain scope of project; only partly visible from spec dirs | medium | none |
| C006 | 3 | KEEP-CAVEAT | Phase caveat (spec-first, no code) is process/policy | high | none |
| C007 | 2 | KEEP-ROUTING | Points to SSoT catalog governance/CATALOGO-OFICIAL.md | high | none |
| C008 | 3 | KEEP-POLICY | Fail-closed policy for missing required reads | high | none |
| C009 | 2 | KEEP-ROUTING | Routing to docs/mapa/MAPA-PROJETO.md, non-normative | high | none |
| C010 | 3 | KEEP-POLICY | Rationale for tool restriction; revisor.md frontmatter shows tools but not intent | medium | none |
| C011 | 3 | KEEP-POLICY | Terminology distinction among gates | high | none |
| C012 | 3 | KEEP-POLICY | Process policy (Dossie, fail-closed) | high | none |
| C013 | 3 | KEEP-POLICY | Hook/CI layering and fallback policy; runtime behavior | high | none |
| C014 | 2 | KEEP-ROUTING | Command exists in scripts/validate_spec_sot.py; exit semantics need reading script | high | none |
| C015 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C016 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C017 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C018 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C019 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C020 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C021 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C022 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C023 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C024 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C025 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C026 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C027 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C028 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C029 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C030 | 3 | KEEP-POLICY | Constitutional/domain policy; not derivable from code | high | none |
| C031 | 1 | KEEP-ROUTING | .claude/skills/tlc-spec-lean pointer; skill listing shows name | medium | none |
| C032 | 1 | KEEP-ROUTING | Skill frontmatter description used for triggering | high | none |
| C033 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C034 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C035 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C036 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C037 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C038 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C039 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C040 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C041 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C042 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C043 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C044 | 3 | KEEP-POLICY | Skill process/gate policy for user approvals and tracks | high | none |
| C045 | 3 | KEEP-POLICY | Self-containment/path resolution policy | high | none |
| C046 | 1 | KEEP-ROUTING | Pointer to reference file in skill dir | high | none |
| C047 | 1 | KEEP-ROUTING | Pointer to reference file in skill dir | high | none |
| C048 | 1 | KEEP-ROUTING | Pointer to reference file in skill dir | high | none |
| C049 | 1 | KEEP-ROUTING | Pointer to reference file in skill dir | high | none |
| C050 | 1 | KEEP-ROUTING | Invocation form of scripts in skill dir | medium | none |
| C051 | 1 | KEEP-ROUTING | Output location convention | medium | none |
| C052 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C053 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C054 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C055 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C056 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C057 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C058 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C059 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C060 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C061 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C062 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C063 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C064 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C065 | 3 | KEEP-POLICY | Skill policy/guardrail, process-level | high | none |
| C066 | 1 | KEEP-ROUTING | Instruction to set SKILL_DIR | medium | none |
| C067 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C068 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C069 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C070 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C071 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C072 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C073 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C074 | 1 | REDUNDANT-CODE | File-existence check listing derivable from directory listing of skill scripts/references | medium | drop list; one-line 'verify skill dir intact' |
| C075 | 3 | KEEP-CAVEAT | Stop condition on broken install | medium | none |
| C076 | 1 | UNCLEAR | Fragment; context-dependent | low | none |
| C077 | 2 | KEEP-ROUTING | Expected output file list; needs reading scripts | medium | none |
| C078 | 3 | KEEP-ROUTING | Workflow step routing with gating | high | none |
| C079 | 3 | KEEP-ROUTING | Workflow step routing with gating | high | none |
| C080 | 3 | KEEP-ROUTING | Workflow step routing with gating | high | none |
| C081 | 3 | KEEP-ROUTING | Workflow step routing with gating | high | none |
| C082 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C083 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C084 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C085 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C086 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C087 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C088 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C089 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C090 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C091 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C092 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C093 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C094 | 3 | KEEP-ROUTING | Judge dispatch routing and blindness constraints (process) | high | none |
| C095 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C096 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C097 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C098 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C099 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C100 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C101 | 3 | KEEP-ROUTING | Reporting workflow step | medium | none |
| C102 | 3 | KEEP-POLICY | Apply policy guardrails | high | none |
| C103 | 3 | KEEP-POLICY | Apply policy guardrails | high | none |
| C104 | 3 | KEEP-POLICY | Apply policy guardrails | high | none |
| C105 | 1 | KEEP-ROUTING | Skill description frontmatter | high | none |
| C106 | 3 | KEEP-COMPRESSED | Compressed authority chain of sources | medium | none |
| C107 | 3 | KEEP-COMPRESSED | Continuation of compressed source hierarchy | medium | none |
| C108 | 3 | KEEP-POLICY | Header of inviolable principles | medium | none |
| C109 | 3 | KEEP-POLICY | Project-specific 4Es maxims sourced to CEE-001 | medium | none |
| C110 | 3 | KEEP-POLICY | Project-specific 4Es maxims sourced to CEE-001 | medium | none |
| C111 | 3 | KEEP-POLICY | Project-specific 4Es maxims sourced to CEE-001 | medium | none |
| C112 | 3 | KEEP-POLICY | Project-specific 4Es maxims sourced to CEE-001 | medium | none |
| C113 | 1 | REDUNDANT-GENERAL | Generic LLM context/tool advice, not project-specific | medium | drop; standard guidance |
| C114 | 1 | REDUNDANT-GENERAL | Generic LLM context/tool advice, not project-specific | medium | drop; standard guidance |
| C115 | 1 | REDUNDANT-GENERAL | Generic LLM context/tool advice, not project-specific | medium | drop; standard guidance |
| C116 | 1 | REDUNDANT-GENERAL | Generic LLM context/tool advice, not project-specific | medium | drop; standard guidance |
| C117 | 1 | REDUNDANT-GENERAL | Generic centralize-first multi-agent advice | medium | drop or shrink to a pointer |
| C118 | 1 | REDUNDANT-GENERAL | Generic centralize-first multi-agent advice | medium | drop or shrink to a pointer |
| C119 | 2 | UNCLEAR | Generic topology triggers but framed as project policy | low | none |
| C120 | 2 | UNCLEAR | Generic topology triggers but framed as project policy | low | none |
| C121 | 2 | UNCLEAR | Generic topology triggers but framed as project policy | low | none |
| C122 | 2 | UNCLEAR | Generic topology triggers but framed as project policy | low | none |
| C123 | 3 | KEEP-POLICY | Never-decentralize policy for SOT decisions | medium | none |
| C124 | 3 | KEEP-POLICY | Never-decentralize policy for SOT decisions | medium | none |
| C125 | 3 | KEEP-POLICY | Never-decentralize policy for SOT decisions | medium | none |
| C126 | 3 | KEEP-POLICY | Never-decentralize policy for SOT decisions | medium | none |
| C127 | 3 | KEEP-POLICY | Never-decentralize policy for SOT decisions | medium | none |
| C128 | 1 | UNCLEAR | Heading of read/write heuristic | low | none |
| C129 | 3 | KEEP-POLICY | Mandatory gate header | high | none |
| C130 | 3 | KEEP-POLICY | Topology gate checklist item | medium | none |
| C131 | 3 | KEEP-POLICY | Topology gate checklist item | medium | none |
| C132 | 3 | KEEP-POLICY | Topology gate checklist item | medium | none |
| C133 | 3 | KEEP-POLICY | Topology gate checklist item | medium | none |
| C134 | 3 | KEEP-POLICY | Topology gate checklist item | medium | none |
| C135 | 3 | KEEP-POLICY | Topology gate checklist item | medium | none |
| C136 | 3 | KEEP-POLICY | SOT-specific directive | high | none |
| C137 | 3 | KEEP-CAVEAT | Pilot-phase caveat on thresholds; duplicates AGENTS.md but carries caveat | medium | none |
| C138 | 3 | KEEP-COMPRESSED | Compressed 4Es rationale tied to CEE-001 | medium | none |
| C139 | 3 | KEEP-POLICY | Definition of BASpec as minimal unit | medium | none |
| C140 | 1 | REDUNDANT-GENERAL | Generic statement on EARS traceability | low | drop |
| C141 | 2 | KEEP-ROUTING | Points to canonical example | medium | none |
| C142 | 3 | KEEP-POLICY | Header of well-formedness rules | high | none |
| C143 | 3 | KEEP-POLICY | BASpec well-formedness rule | high | none |
| C144 | 3 | KEEP-POLICY | BASpec well-formedness rule | high | none |
| C145 | 3 | KEEP-POLICY | BASpec well-formedness rule | high | none |
| C146 | 3 | KEEP-POLICY | BASpec well-formedness rule | high | none |
| C147 | 3 | KEEP-POLICY | Adaptive rigor rule cited to PPQ-001 | medium | none |
| C148 | 3 | KEEP-COMPRESSED | Compressed depth/gate mapping D2..D7 | medium | none |
| C149 | 3 | KEEP-COMPRESSED | Compressed depth/gate mapping D2..D7 | medium | none |
| C150 | 3 | KEEP-COMPRESSED | Compressed depth/gate mapping D2..D7 | medium | none |
| C151 | 3 | KEEP-COMPRESSED | Compressed depth/gate mapping D2..D7 | medium | none |
| C152 | 3 | KEEP-COMPRESSED | Compressed depth/gate mapping D2..D7 | medium | none |
| C153 | 3 | KEEP-POLICY | Labeling policy for agent content | high | none |
| C154 | 3 | KEEP-POLICY | Conflict / open-decision stop rule | high | none |
| C155 | 3 | KEEP-POLICY | Conflict / open-decision stop rule | high | none |
| C156 | 3 | KEEP-POLICY | Conflict / open-decision stop rule | high | none |
| C157 | 3 | KEEP-POLICY | Conflict / open-decision stop rule | high | none |
| C158 | 3 | KEEP-POLICY | Conflict / open-decision stop rule | high | none |
| C159 | 1 | KEEP-ROUTING | Trigger header for validation steps | medium | none |
| C160 | 2 | KEEP-ROUTING | Trigger conditions for validation | medium | none |
| C161 | 2 | KEEP-ROUTING | Trigger conditions for validation | medium | none |
| C162 | 2 | KEEP-ROUTING | Trigger conditions for validation | medium | none |
| C163 | 2 | KEEP-ROUTING | Trigger conditions for validation | medium | none |
| C164 | 2 | KEEP-ROUTING | Trigger conditions for validation | medium | none |
| C165 | 0 | REDUNDANT-CODE | package.json scripts.test = node tests/validate-schemas.js | high | cite `npm test` only |
| C166 | 0 | REDUNDANT-CODE | package.json scripts.lint = node tests/lint-specs.js | high | cite `npm run lint` only |
| C167 | 3 | KEEP-POLICY | Cross-agent consistency check requiring reading schemas/specs | medium | none |
| C168 | 2 | KEEP-POLICY | Specific I/O field consistency requirement across specs/schemas | medium | none |
| C169 | 2 | KEEP-POLICY | Specific I/O field consistency requirement across specs/schemas | medium | none |
| C170 | 2 | KEEP-POLICY | Specific I/O field consistency requirement across specs/schemas | medium | none |
| C171 | 2 | KEEP-POLICY | Specific I/O field consistency requirement across specs/schemas | medium | none |
| C172 | 3 | KEEP-POLICY | Constitutional guard check header | medium | none |
| C173 | 3 | KEEP-POLICY | Constitutional guard verification item | medium | none |
| C174 | 3 | KEEP-POLICY | Constitutional guard verification item | medium | none |
| C175 | 3 | KEEP-POLICY | Constitutional guard verification item | medium | none |
| C176 | 0 | REDUNDANT-CODE | package.json scripts.eval = npx harness-score | high | cite `npm run eval` |
| C177 | 2 | KEEP-COMPRESSED | Compressed validation criteria enforced by tests/scripts | medium | none |
| C178 | 2 | KEEP-COMPRESSED | Compressed validation criteria enforced by tests/scripts | medium | none |
| C179 | 2 | KEEP-CAVEAT | Threshold caveat (L2 min, 85+) version-dependent | medium | none |
| C180 | 2 | KEEP-POLICY | Acceptance criterion using harness-eval Track A | medium | none |
| C181 | 1 | UNCLEAR | Dated status snapshot; may be stale | low | consider dropping if stale |
| C182 | 1 | REDUNDANT-GENERAL | Legend of symbols | medium | drop legend |
| C183 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C184 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C185 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C186 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C187 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C188 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C189 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C190 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C191 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C192 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C193 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C194 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C195 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C196 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C197 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C198 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C199 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C200 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C201 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C202 | 3 | KEEP-POLICY | Spec maturity checklist item (D0-D9), project process | medium | none |
| C203 | 1 | KEEP-ROUTING | Skill frontmatter description | high | none |
| C204 | 2 | KEEP-POLICY | Authority/version metadata of skill | medium | none |
| C205 | 2 | KEEP-POLICY | Authority/version metadata of skill | medium | none |
| C206 | 2 | KEEP-POLICY | Authority/version metadata of skill | medium | none |
| C207 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C208 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C209 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C210 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C211 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C212 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C213 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C214 | 3 | KEEP-POLICY | Role, flow and anti-scope policy for PAP-001 specifier | high | none |
| C215 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C216 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C217 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C218 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C219 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C220 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C221 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C222 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C223 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C224 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C225 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C226 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C227 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C228 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C229 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C230 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C231 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C232 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C233 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C234 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C235 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C236 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C237 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C238 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C239 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C240 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C241 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C242 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C243 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C244 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C245 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C246 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C247 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C248 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C249 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C250 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C251 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C252 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C253 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C254 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C255 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C256 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C257 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C258 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C259 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C260 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C261 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C262 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C263 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C264 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C265 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C266 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C267 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C268 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C269 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C270 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C271 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C272 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C273 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C274 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C275 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C276 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C277 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C278 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C279 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C280 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C281 | 3 | KEEP-COMPRESSED | Compressed source-anchor tag [FONTE: ...] | medium | none |
| C282 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C283 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C284 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C285 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C286 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C287 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C288 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C289 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C290 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C291 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C292 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C293 | 3 | KEEP-POLICY | PAP-001 production requirements, invariants, open decisions, self-check | high | none |
| C294 | 3 | KEEP-CAVEAT | Caveat: GEH-001 location and do-not-substitute rule | high | none |
| C295 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C296 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C297 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C298 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C299 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C300 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C301 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C302 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C303 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C304 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C305 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C306 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C307 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C308 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C309 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C310 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C311 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C312 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| C313 | 1 | KEEP-ROUTING | On-demand load target; existence visible in directory listing, listed as harness-referenced doc | low | none |
| P001 | 0 | REDUNDANT-CODE | package.json scripts.test exists | high | drop |
| P002 | 0 | REDUNDANT-CODE | package.json scripts.lint exists | high | drop |
| P003 | 1 | REDUNDANT-GENERAL | Generic coding advice | high | drop |
| P004 | 1 | REDUNDANT-GENERAL | Generic layering advice; no layers in this spec repo | high | drop |
| P005 | 3 | KEEP-POLICY | Security policy not derivable from code | high | none |
| P006 | 3 | KEEP-CAVEAT | CI vs local env caveat; runtime/environment-specific | high | none |
