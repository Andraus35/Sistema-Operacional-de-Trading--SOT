# Proposta pré-testada — mapa do projeto fora do Git (sem tocar script selado)

> **Não normativo. PROPOSTA — NADA APLICADO.** Andraus (chat 2026-11-01): "pré-testar o mapa primeiro". Aplicar exige ata (BL-019 e `AGENTS.md` §5). Não fecha decisão aberta (CONS-01).

## 1. Restrição descoberta
`scripts/pre_entrega.py`, `scripts/run_gates.py` e `scripts/revisor_gate.py` — todos **selados** no `GATE-MANIFEST` — chamam `build_map.py --check`. Mudar a chamada ou o `build_map.py` exige religar o selo (Andraus). O desenho abaixo **não altera nenhum selado**.

## 2. Desenho
1. `.gitignore` de `docs/mapa/MAPA-PROJETO.md` + `git rm --cached` (o `.json` já é ignorado desde a A2.1).
2. Os hooks de sessão (`map-sync.js`, SessionStart/Stop) já geram o mapa localmente; nada muda neles.
3. `ci.yml`: antes do passo "Project map up to date", rodar `python scripts/build_map.py`. O `--check` passa a provar que a geração funciona e que o mapa local é coerente (perde o sentido "mapa commitado reflete os docs", que ninguém consome além de leitores do GitHub).
4. `.pre-commit-config.yaml` (hoje `proposta`): entrada `sh -c "python scripts/build_map.py && python scripts/build_map.py --check"`.
5. `AGENTS.md` §5 e BL-019: "mapa é saída gerada, não versionada" (ata de Andraus).

## 3. Pré-teste (`TESTE-MAPA-fora-do-git.sh`, clone novo da `main` pós-#159)
| # | Verificação | Resultado |
|---|---|---|
| 1 | clone novo, sem mapa: `--check` | rc=2 (ausente), como hoje |
| 2 | após gerar: `--check` | rc=0 |
| 3 | `git status` após gerar | mapa não aparece |
| 4 | `gate_manifest --check` | íntegro |
| 5 | `test_pre_entrega`, `test_gate_manifest`, `test_revisor_gate_mcp` | 22 testes OK |
| 6 | 2 ramos com `.md` novos distintos, mesclados | sem conflito (o mapa não está no Git) |

## 4. Limites
- Não testado no GitHub Actions real (passo 3 do desenho): só equivalente local.
- Sessão sem hooks/Python não terá mapa até gerar; o `Revisor` em nuvem roda `revisor_gate` que chama `--check`: precisa do mapa gerado antes (SessionStart já faz). Se falhar, rc=2 reprova em vez de passar em falso.
- Juntamente com o ledger (`PROPOSTA-LEDGER-2026-11-01.md`) e o handoff por ramo (#159), elimina os 3 arquivos mais disputados.
