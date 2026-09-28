---
description: Run full SOT harness validation — checks all specs, schemas, RAG chunks, and cross-agent consistency. Use before publishing harness changes.
---

# Validate SOT Harness

Run the complete validation workflow for the SOT-Harness before any changes are considered complete.

## Steps

1. Run JSON schema validation: `npm test`
2. Run spec linting: `npm run lint`
3. Run harness quality score: `npx harness-score`
4. Check CONSTITUTION.md — all 14 principles present?
5. Check RULES.md — all rule sections present (RULE-*, RULE-EW-*, RULE-FB-*, RULE-SM-*, RULE-ICT-*, RULE-SY-*)?
6. Check all 5 spec files present in specs/
7. Check all 10 schema files present in schemas/ (5 input + 5 output)
8. Check all 4 RAG files present in rag/
9. Verify HARNESS-REPORT.md is up to date
