# Optional docs (not in eval unless approved)

Non-agent documents cited by T0/T1. **ADRs / RFCs are always excluded.**
Agent skill-tree files (`.agents/skills`, `.cursor/skills`, `.claude/skills`) are always in scope.

## Ask the user

Present the doc **types** below and ask which (if any) to include in this run.
Then re-run inventory with `--include-doc-type <type>` and/or `--include-doc <path>`.

## Always excluded (decision records)

_None discovered in one-hop cites._

## Optional types (default: omitted)

| Type | Count | Example paths |
|------|------:|---------------|
| `.claude` | 2 | `.claude/agents/especificador.md`, `.claude/agents/revisor.md` |
| `.clinerules` | 1 | `.clinerules/sot-map.md` |
| `.github` | 1 | `.github/workflows/auditor-externo.yml` |
| `GLOSSARIO.md` | 1 | `GLOSSARIO.md` |
| `HANDOFF.md` | 1 | `HANDOFF.md` |
| `ROADMAP.md` | 1 | `ROADMAP.md` |
| `WORKFLOW.md` | 1 | `WORKFLOW.md` |
| `atomic-spec.md` | 1 | `atomic-spec.md` |
| `docs/agentes` | 1 | `docs/agentes/INDICE-AGENTES.md` |
| `docs/mapa` | 1 | `docs/mapa/MAPA-PROJETO.md` |
| `governance` | 7 | `governance/CATALOGO-OFICIAL.md`, `governance/MECANISMOS.json`, `governance/RULES.md` (+4) |

### Re-run examples

```bash
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" \
  --include-doc-type docs
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" \
  --include-doc docs/context.md --include-doc docs/infrastructure.md
```

## Included optional docs this run

_None (default)._

