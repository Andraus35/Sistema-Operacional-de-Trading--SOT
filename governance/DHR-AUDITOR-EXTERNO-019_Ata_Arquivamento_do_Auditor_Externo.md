# DHR-AUDITOR-EXTERNO-019 — Ata — Arquivamento do Auditor Externo (A6.3)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-11-01 |
| Status | **VIGENTE no ramo; mescla do PR só por ordem de Andraus.** Decisão: chat 2026-11-01 — "Ativar arquivamento" (após a pauta A3, item 4, "Aposentar e arquivar"). Antes, na mesma data: "Não ativar auditor externo" (o piloto NÃO é reativado). |
| Compatibilidade | Complementa a DHR-AUDITOR-EXTERNO-007 (pausa). Não revoga as atas 001..018 (INV-07); o piloto continua reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Move para docs/_legacy/ o workflow, o roteador e as propostas do piloto pausado; nao altera checklist, metodo nem regra dos agentes de construcao. |

## 1. O que foi feito
Patch pré-testado `EQUIVALENCIA/A6/PATCH-ARQUIVAR-AUDITOR-EXTERNO-2026-11-01.patch` (40 renomeações, nada deletado): `auditor-externo.yml`, `route_aex.py`, `test_route_aex.py` e a pasta `propostas/AUDITOR-EXTERNO/` foram para `docs/_legacy/auditor-externo/`; o passo "AEX router tests" saiu do `ci.yml`; `util.route-aex` e `wf.auditor-externo` viraram `legado` em `MECANISMOS.json`. Nenhum selo de gate mudou.

## 2. O que NÃO foi feito (reservado)
`AGENTS.md` §9, `GLOSSARIO.md` e `governance/CATALOGO-OFICIAL.md` continuam apontando os caminhos antigos; o `check_refs` mostra isso como WARN de caminho desatualizado (ERRO=0). Editá-los exige ordem expressa de Andraus.

## 3. Reversão
`git revert` do commit do arquivamento; o piloto só volta a rodar por decisão expressa dele.
