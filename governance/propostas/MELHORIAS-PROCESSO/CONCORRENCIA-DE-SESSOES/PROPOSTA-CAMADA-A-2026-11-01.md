# Proposta pré-testada — Camada A: handoff por ramo (ID único) e mapa fora do Git

> **Não normativo. PROPOSTA — NADA APLICADO.** Desdobra a Camada A de `../PROPOSTA-CONCORRENCIA-DE-SESSOES-2026-11-01.md` (Andraus, chat 2026-11-01: "proposta pré-testada primeiro"). Aplicar exige ordem expressa dele; `AGENTS.md` §5/§11 e BL-019 mudam por ata. Não fecha decisão aberta (CONS-01).

## 1. O que o patch faz (`PATCH-CAMADA-A-handoff-por-ramo-2026-11-01.patch`, 4 scripts)
- `check_handoff.py`: novo `handoff_rel()`. Se existir `handoffs/<ramo>.md`, ele é o handoff da sessão (HO-01..HO-15, incluindo HO-04 via `git show HEAD:<arquivo>`); senão vale o `HANDOFF.md` da raiz. Compatível com o modelo atual.
- `handoff-hook.js`, `check_branches.py` (BR-01 lê todos os handoffs), `check_coesao.py` (COE-12 lê todos).
- Convenção de ID: `HO-<data>-<ramo curto>-<n>`; o arquivo vive em `handoffs/<ramo>.md`; o anterior segue copiado em `docs/handoffs/` (INV-07). Colisão de número deixa de existir, e as pastas `ramo-*/` ficam desnecessárias para novas sessões.

## 2. Pré-teste (cópia isolada via `git worktree`)
| Teste | Resultado |
|---|---|
| `git apply --check` no repositório real | limpo |
| `gate_manifest --check` (selo) com o patch | **íntegro** — nenhum dos 4 scripts é selado |
| `check_handoff` com `handoffs/<ramo>.md` presente | ERRO=0 WARN=0 |
| 2 ramos, cada um com seu `handoffs/<ramo>.md` + doc diferente, mesclados | **0 conflitos** |
| Contra-prova: 2 ramos editando `HANDOFF.md` | `CONFLICT` (o problema atual) |
| `tests.test_gate_manifest/test_revisor_gate_mcp/test_check_handoff/test_check_branches/test_check_coesao` | verdes |
| `tests.test_pre_entrega` | verde após regenerar o mapa (ver §4) |

## 3. Mapa fora do Git — achado e caminho
- **Não editar `scripts/build_map.py`:** ele é **selado** no `GATE-MANIFEST.sha256`; uma versão com `--check --gerado` quebrou 5 testes (`sha256 difere do manifesto`). Descartada.
- **Caminho sem tocar o script:** `.gitignore` de `docs/mapa/MAPA-PROJETO.md` + `git rm --cached`, e o CI/pre-commit trocam `build_map.py --check` por `build_map.py --out "$(mktemp -d)"` (prova que a geração funciona; testado: gera 336+ documentos, exit 0, sem escrever na árvore).
- **Pendências para a ordem de Andraus:** (a) o hook `map-sync.js` e `.stale` assumem mapa versionado; (b) `test_pre_entrega` e `pre_entrega` têm o gate `build_map_check`, que precisaria aceitar mapa ausente; (c) ata alterando BL-019 e `AGENTS.md` §5 ("`--check` bloqueia"). Por isso o mapa **não entra** neste patch.

## 4. Limites
- O `LEDGER-ACHADOS.md` único ainda conflita (teste mostrou `CONFLICT`). Ele é regenerado por `loop_ledger.py`, então `merge=union` duplicaria linhas; o caminho é fragmento por sessão ou regenerar no merge (Camada A, item 3, ainda sem patch).
- Regenerar o mapa na cópia isolada leva ~100 s; o `build_map_check` fica vermelho em qualquer ramo que adicione `.md` e não regenere — comportamento atual, não regressão.
- Nada disto substitui a Camada B (proteção da `main` e merge queue), que continua a primeira da ordem.

## 5. Para aplicar (por ordem de Andraus)
1. `git apply governance/propostas/MELHORIAS-PROCESSO/CONCORRENCIA-DE-SESSOES/PATCH-CAMADA-A-handoff-por-ramo-2026-11-01.patch`; 2. suíte completa + `gate_manifest --check`; 3. atualizar `governance/MECANISMOS.json` (COE-14); 4. texto da regra em `AGENTS.md` §11 por ata; 5. migrar o handoff atual para `handoffs/<ramo>.md` na primeira sessão que adotar.
