---
description: Mantém o mapa do projeto (docs/mapa/) atualizado. Aplique ao alterar, criar, mover ou remover documentos .md — o Cline não executa os hooks do Claude Code.
globs: ["**/*.md", "**/*.MD"]
paths: ["**/*.md", "**/*.MD"]
alwaysApply: false
---

# Mapa do projeto (BL-019)

Depois de alterar, criar, mover ou remover qualquer `.md` (fora de `docs/mapa/`, `UPGRADES/`, `docs/_legacy/`):

1. Rode `python scripts/build_map.py` (regenera `docs/mapa/MAPA-PROJETO.md` e `mapa-projeto.json`).
2. Confirme com `python scripts/build_map.py --check` → "Mapa em dia".
3. Inclua `docs/mapa/` na mesma entrega.

Regras:

- **Nunca edite `docs/mapa/` à mão** — é saída gerada e NÃO-normativa (INV-09). Em conflito, vale o documento de origem; o locator autoritativo é `governance/CATALOGO-OFICIAL.md`.
- Este ambiente não roda os hooks do Claude Code; o backstop é o CI (`--check` bloqueante) e o pre-commit.
- Se aparecer um marcador `.stale` dentro da pasta do mapa, o mapa está defasado (a regeneração automática falhou): regenere. (Arquivo condicional — só existe em caso de falha.)
