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
| `GLOSSARIO.md` | 1 | `GLOSSARIO.md` |
| `RETOMADA` | 1 | `RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md` |
| `ROADMAP.md` | 1 | `ROADMAP.md` |
| `atomic-spec.md` | 1 | `atomic-spec.md` |
| `backlog` | 1 | `backlog/BL-018-RISK-AGENT-backlog.md` |
| `docs/mapa` | 1 | `docs/mapa/MAPA-PROJETO.md` |
| `governance` | 6 | `governance/CATALOGO-OFICIAL.md`, `governance/CONFLICT-MAP.md`, `governance/CONSTITUTION.md` (+3) |

### Re-run examples

```bash
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" \
  --include-doc-type docs
python3 "$SKILL_DIR/scripts/inventory_extract.py" --root . --run-id "$RUN_ID" \
  --include-doc docs/context.md --include-doc docs/infrastructure.md
```

## Included optional docs this run

- `.claude/agents/especificador.md`
- `.claude/agents/revisor.md`
- `.clinerules/sot-map.md`
- `GLOSSARIO.md`
- `RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md`
- `ROADMAP.md`
- `atomic-spec.md`
- `backlog/BL-018-RISK-AGENT-backlog.md`
- `docs/mapa/MAPA-PROJETO.md`
- `governance/CATALOGO-OFICIAL.md`
- `governance/CONFLICT-MAP.md`
- `governance/CONSTITUTION.md`
- `governance/GPR-001_Guia_Principios_Relacoes_SOT.md`
- `governance/PP-PAP-001_Pacote_Partida_Protocolo_Adesao_Progressiva.md`
- `governance/RULES.md`

