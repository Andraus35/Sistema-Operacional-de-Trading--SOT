---
name: update-harness
description: Use when a source document changes or a new governance document is added and the SOT harness needs to be updated. Extracts relevant content and propagates changes to CONSTITUTION, RULES, specs, schemas, and RAG files.
---

# Update SOT Harness from Source Document

## Purpose

Propagates new or updated source document content into the harness files systematically.

## Steps

1. **Classify the source content** using the Part 1 classification table format:
   | Documento | Seção/Trecho | Categoria | Destino |
   Categories: SP (Spec-level), SC (Schema-level), RG (RAG-level), RL (Rules-level), CF (Conflict-level), GO (Governance-only/discard)

2. **CONSTITUTION.md updates**: for SP-classified content — add to relevant principle or create new P-series principle. Never renumber existing principles.

3. **RULES.md updates**: for RL-classified content — add new numbered rule in the correct section (RULE-001 universal, RULE-EW-* Elliott, RULE-FB-* Fibonacci, RULE-SM-* SMC, RULE-ICT-* ICT, RULE-SY-* Synthesis). Always cite source.

4. **Schema updates**: for SC-classified content — modify the relevant .input.json or .output.json. Validate the result is valid JSON Schema Draft-07. Never remove required fields.

5. **RAG updates**: for RG-classified content — add new chunk to the relevant knowledge base. Use the correct chunk_id prefix. Add YAML frontmatter.

6. **CONFLICT-MAP updates**: for CF-classified content — add row to the appropriate conflict table.

7. **HARNESS-REPORT updates**: update the source inventory in §4.1 and remove resolved gaps from §4.2.
