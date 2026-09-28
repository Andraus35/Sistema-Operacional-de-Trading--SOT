---
description: Rules for editing SOT JSON schemas. Apply when modifying any file in schemas/ directory.
globs: ["schemas/**/*.json"]
paths: ["schemas/**/*.json"]
alwaysApply: false
---

# SOT Schema Editing Rules

## Required schema envelope

Every schema file must have:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://sot.oryx-agent/schemas/<name>.json",
  "title": "...",
  "type": "object"
}
```

## Naming convention

- Input schemas: `<agent-name>.input.json`
- Output schemas: `<agent-name>.output.json`

## Required output fields

Every agent output schema MUST declare:
- An agent-specific `score` field (0-3 integer)
- An `antiescopo_violation` boolean or equivalent guard
- At minimum one rejection/conflict field

## Type strictness

- Use `enum` for fields with fixed values (e.g. signal states: COMPRA/VENDA/NEUTRO/AGUARDAR_SETUP)
- Use `minimum`/`maximum` constraints on numeric ranges
- Use `format: "date-time"` for timestamp fields
- Set `additionalProperties: false` on top-level objects

## ICT schema special rule

`approved_hypothesis` in `ict.input.json` MUST allow null:
```json
{ "oneOf": [{ "$ref": "#/definitions/Hypothesis" }, { "type": "null" }] }
```
A null value is the ICT INACTIVE state — never remove this.
