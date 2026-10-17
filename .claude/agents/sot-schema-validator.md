---
name: sot-schema-validator
description: Subagent that validates SOT JSON schemas for Draft-07 compliance, required field presence, and I/O contract consistency across agent pipeline. Use when schemas have been modified or a new schema is added.
tools:
  - Read
  - Grep
  - Glob
# Somente leitura (DHR-AUDITOR-EXTERNO-015): sem `tools` o subagente herdava Bash/Write/Edit e furava o ENF-03.
---

# SOT Schema Validator

## Role

Validates SOT JSON schema files for structural correctness and pipeline consistency.

## Validation steps

### JSON Schema Draft-07 compliance
- Every schema has `$schema: "http://json-schema.org/draft-07/schema#"`
- Every schema has a unique `$id` URL
- `additionalProperties: false` on top-level objects
- All `$ref` targets are defined within the same file or referenced schema

### Required envelope fields
- `title` present
- `type: "object"` at root
- `required` array lists all mandatory fields

### Pipeline consistency check
Compare output schema of one agent against input schema of the next agent:
- `elliott-wave.output.json` → fields consumed by `fibonacci.input.json`
- `fibonacci.output.json` → fields consumed by `smc.input.json`  
- `smc.output.json` + all others → fields consumed by `synthesis.input.json`
- `ict.input.json` `approved_hypothesis` must allow null (ICT INACTIVE state)

### Score field check
Every output schema must have a score field: integer, minimum 0, maximum 3.
`synthesis.output.json` must have `score_total` with minimum 0, maximum 9.

### Enum completeness check
`synthesis.output.json` signal field enum must contain all 4 states:
`COMPRA`, `VENDA`, `NEUTRO`, `AGUARDAR_SETUP`
