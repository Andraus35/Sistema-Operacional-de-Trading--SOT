---
description: Update a specific SOT agent spec when source documents change. Provide the agent name (elliott-wave, fibonacci, smc, ict, or synthesis) and the new requirement.
---

# Update SOT Agent Spec

Update a specific agent spec file with new requirements from source documents.

## Arguments

- Agent name: one of `elliott-wave`, `fibonacci`, `smc`, `ict`, `synthesis`
- Source: which document section contains the new requirement

## Steps

1. Classify the new requirement (SP/SC/RG/RL/CF/GO)
2. If SP: update the relevant section of the spec file in specs/
3. If RL: add a new RULE in RULES.md under the correct agent section
4. If SC: update the corresponding schema file
5. If RG: add a new chunk to the RAG knowledge base
6. Validate the updated file using the `validate-sot-spec` skill
7. Update HARNESS-REPORT.md §4.1 source inventory
