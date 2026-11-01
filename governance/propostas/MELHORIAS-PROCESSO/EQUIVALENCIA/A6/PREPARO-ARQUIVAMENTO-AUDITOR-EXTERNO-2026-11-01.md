# Preparo — arquivar o Auditor Externo (A6.3)

> **Não normativo. NADA MOVIDO NEM APLICADO.** Andraus escolheu "Aposentar e arquivar" (AskUserQuestion, 2026-11-01, pauta A3 item 4); eu só **preparo**. Executar exige nova ordem dele. Inclui arquivo reservado (`AGENTS.md` §9) e mecanismo (COE-14).

## 1. O que sairia do uso vivo (medido)
- `.github/workflows/auditor-externo.yml` (326 linhas) → `docs/_legacy/auditor-externo/`.
- `route_aex.py` (115) + `test_route_aex.py` (170) + o passo `unittest` do roteador em `ci.yml` (l.163).
- `governance/propostas/AUDITOR-EXTERNO/` (316 KB, 10 arquivos + `kit/`).
- `MECANISMOS.json`: `util.route-aex` e `wf.auditor-externo` (hoje `pausado`) passam a `legado`.
- `AGENTS.md` §9 (texto lido por todo agente) → uma linha de ponteiro para o arquivo morto, **arquivo reservado: só com ordem expressa**; `GLOSSARIO.md` cita o termo.
- **Fica:** as atas `DHR-AUDITOR-EXTERNO-001..018` (nada é deletado; INV-07) e os pareceres do Revisor que as citam.

## 2. Riscos a tratar antes de mover
1. **Referências quebradas:** ≥30 arquivos citam `auditor-externo`/`route_aex`/`AUDITOR-EXTERNO` (atas, pareceres, `MECANISMOS.json`, `propostas/`). `check_refs.py` precisa ficar com ERRO=0: mover só o que `check_refs` tolera em `_legacy/` (históricos viram INFO) e conferir antes/depois.
2. **Selo/CODEOWNERS:** `route_aex.py` não está no `GATE-MANIFEST` nem no `CODEOWNERS`; nenhum selo muda. `auditor-externo.yml` não é lido por outro workflow.
3. **Reversão:** `git revert` do commit; nada deletado. Reativar = mover de volta + religar o passo do `ci.yml`.
4. **Equivalência:** rodar `equiv_conservacao.py` (em `governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/`, utilitário de proposta) entre a árvore antes/depois, como no corte do `AGENTS.md`.

## 3. Para executar (por ordem de Andraus)
1. Pré-teste em cópia isolada: mover, `check_refs`, `check_coesao`, `build_map`, suíte Python e `npm run test:hooks`. 2. Aplicar no ramo. 3. `AGENTS.md` §9 e `GLOSSARIO.md` só com ordem expressa. 4. Ata curta `DHR-…` com a ordem citada.

## 4. Declarado
Contagem de arquivos vem de `grep` desta sessão; não rodei o pré-teste. Reativar o piloto continua possível por decisão dele.

## 5. Resultado do pré-teste (2026-11-01, cópia isolada de `3501b14`; NADA APLICADO)
Patch: `PATCH-ARQUIVAR-AUDITOR-EXTERNO-2026-11-01.patch` (renomeações `-M`; `git apply --check` limpo no repositório real). Inclui: workflow, `route_aex.py`, teste, pasta `propostas/AUDITOR-EXTERNO` movidos para `docs/_legacy/auditor-externo/`; passo "AEX router tests" removido do `ci.yml` (YAML válido); `util.route-aex` e `wf.auditor-externo` → `legado` em `MECANISMOS.json`.
- Suíte Python **410 testes OK** (= 430 − 20 do `route_aex`); `npm run test:hooks` verde; `gate_manifest` íntegro (nenhum selo muda); `check_coesao` ERRO=0; `build_map --check` ok; `check_refs` **ERRO=0**, mas **+8 WARN** de caminho desatualizado.
- **Os 8 WARN, em arquivos vivos:** `AGENTS.md:137` e `governance/CATALOGO-OFICIAL.md:182,184` (**reservados a Andraus**), 4 em propostas/pareceres da própria frente e 1 em `ROTEAMENTO-MODELOS/AUDITORIA…`. Resolver exige editar esses arquivos (AGENTS §9 e CATALOGO), por ordem expressa, ou aceitar os WARN como INFO históricos.
- Não testado: o CI real; reativação (`git revert`).
- Decisão de Andraus: aplicar o patch (aceitando 8 WARN até ele autorizar `AGENTS.md`/`CATALOGO`), aplicar junto com a edição desses dois arquivos, ou deixar como está.
