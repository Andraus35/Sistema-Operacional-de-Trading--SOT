---
handoff_id: HO-2026-11-01-157
previous: HO-2026-11-01-156
data: 2026-11-01
branch: ccr-b7c09dc1-y4rafd
base_commit: b1b0e1b
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-b7c09dc1-y4rafd: concorrência entre sessões)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece. Reescrito limpo em HO-157: o texto acumulado de outras sessões foi arquivado em `docs/handoffs/HO-2026-11-01-156.md`.

## 1. Frente atual
**Problema (ordem de Andraus, chat 2026-11-01):** várias sessões mexem no repositório ao mesmo tempo e geram docs, ramos, PRs e merges conflitantes. **Causa-raiz medida:** arquivos únicos e gerados tocados por toda sessão (mapa 214 toques/30 dias, `HANDOFF.md` 124, ledgers), numeração sequencial de handoff e nenhuma serialização no servidor.
**Solução em 3 camadas** (`governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-CONCORRENCIA-DE-SESSOES-2026-11-01.md` + pasta `CONCORRENCIA-DE-SESSOES/`):
- **B (servidor):** ruleset `proteger-main` + merge queue + bypass só do bot do `rpsa-auto`. **Falta Andraus criar no GitHub** (guia passo a passo já dado no chat; começar em *Evaluate*).
- **A (estado compartilhado):** handoff por ramo `handoffs/<ramo>.md` **na `main` (PR #159)**; ledger gerado e não versionado **na `main` (PR #164, `DHR-LEDGER-GERADO-001`)**; mapa gerado e não versionado **no PR #169 (aberto, CI verde)**.
- **C (lock por frente):** só desenhada; adiar até A e B estarem de pé.
**PRs deste trabalho:** #169 (ata e aplicação do mapa gerado) e #167 (só documentos: propostas, rascunhos, cadeia deste ramo). **Nenhum mesclado sem ordem de Andraus.**

## 2. Estado (fatos conferidos em 2026-11-01)
- `main` em `b1b0e1b`. PRs abertos de outras sessões que tocam o mesmo terreno: **#170** (`check_refs` trata o ledger como artefato local: ERRO 2→0, selo regravado só nessa linha), **#168** (medição A5-O4). Eles editam a pauta e handoffs: esperar conflito trivial.
- Testes: suíte completa 503 OK em clone novo com a ata do mapa aplicada; `gate_manifest` íntegro.
- O `build_map.py` indexa arquivos do **disco**, não do Git. `pre_entrega.py`, `run_gates.py` e `revisor_gate.py` (selados) chamam `build_map --check`; por isso o CI do #169 gera o mapa antes de qualquer passo.
- Ramos remotos sem nada exclusivo (apagáveis, só Andraus: 403 para mim): `ccr-4bd4e8a0-d92lc7`, `ccr-599f6762-60qbvg`, `claude/amazing-fermat-dnbjtz`, `ccr-b7c09dc1-y4rafd-ledger`, e `ccr-b7c09dc1-y4rafd-camada-a`/`-mapa` depois dos merges. Nove históricos grandes (setembro/outubro) pedem triagem antes de apagar; sugestão: tag `arquivo/<nome>` por ramo.

## 3. Lições (repetir o que funcionou)
- Merge da `main` no ramo: o **mapa** conflita sempre → `git checkout --theirs docs/mapa/MAPA-PROJETO.md` e `python scripts/build_map.py` (leva ~2 min; rodar em segundo plano). O `HANDOFF.md` da raiz fica o da `main`; o handoff do ramo vive em `handoffs/<ramo>.md`.
- `check_handoff` HO-06: **não citar no handoff uma DHR cuja ata ainda não está na `main`** (usar texto livre). HO-04: **toda edição do handoff troca o ID** e o anterior vai, cópia exata, para `docs/handoffs/`.
- **Nunca gravar `LEDGER-ACHADOS.md` em disco** (usar `python scripts/loop_ledger.py --stdout`): o arquivo local muda o resumo do mapa e o CI reprova.
- Comandos longos (mapa, suíte): em segundo plano; um `Monitor` espera o arquivo de saída.
- Antes de afirmar "não há chamada de X no CI", buscar por **todos** os nomes (errei com `loop_ledger --check` no `ci.yml`).

## 4. Verificado (LOOP-001 passo 4)
Sem parecer novo nesta frente; categorias recorrentes e lacunas: rodar `python scripts/loop_ledger.py --stdout` ao receber o próximo parecer.

## 5. Próximo passo único
**Aguardar ordem de Andraus** para mesclar **#169 e depois #167** (nessa ordem: o #167 já nasce sem conflito de mapa). Em seguida, conferir a Camada B com um PR de teste (ele deve exigir CI verde, ramo atualizado e fila).

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-LEDGER-GERADO-001`. A ata do mapa gerado está no PR #169. Decisões abertas do ROADMAP: nenhuma tocada.

## 7. Becos sem saída
Editar `scripts/build_map.py` ou os 3 scripts selados que o chamam; gravar o ledger em disco; `merge=union` em JSON (`rpsa-ledger.json`, `MECANISMOS.json`); apagar ramo remoto por `git push --delete` ou `gh` (403; o `gh` só serve para busca); mesclar sem ordem de Andraus.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas (só por erratum), `ROADMAP.md`, `atomic-spec.md`, `AGENTS.md`, `.claude/agents/*`, `GATE-MANIFEST.sha256` e scripts do CODEOWNERS: só por ordem expressa de Andraus.

## 9. Reverificar ao vivo
- [ ] `git fetch origin main`; `git log -1` == `base_commit` ou posterior (ler o diff); `list_pull_requests`: #167, #169, #170, #168 e o que mais surgir; se #169 ou #164 mudou de estado, ajustar.
- [ ] `python scripts/gate_manifest.py --check`, `check_refs`, `check_handoff`, `check_rpsa`, `check_coesao`, `build_map --check` (gerar o mapa antes se o clone for novo).
- [ ] `python scripts/check_branches.py` (órfãos e apagáveis).
- [ ] Suíte: `python -m unittest discover -s tests` (503 no último teste), `node tests/test-hooks.js`.
- *Avisos esperados:* BR-01 dos ramos históricos; `check_refs` WARN de outra sessão.

## 10. Aguardando Andraus
1. **Mesclar #169 (mapa gerado) e depois #167 (documentos)** — recomendação: mesclar nessa ordem.
2. **Camada B no GitHub:** criar o ruleset `proteger-main` (Evaluate → Active) — recomendação: criar hoje.
3. **Apagar os ramos contidos na `main`** em Branches no GitHub — recomendação: apagar; eu confiro com `check_branches`.
4. **Camada C (lock por frente):** adiar até A e B estarem ativas — recomendação: adiar.
5. **Triagem dos nove ramos históricos** — recomendação: tag `arquivo/<nome>` antes de qualquer remoção.

## 11. Ponteiros
`governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-CONCORRENCIA-DE-SESSOES-2026-11-01.md` · `.../CONCORRENCIA-DE-SESSOES/` (PROPOSTA-CAMADA-A, PROPOSTA-LEDGER, PROPOSTA-MAPA, rascunhos das atas, patch e scripts de teste) · `governance/PAUTA-DE-DECISOES.md` (pauta única de Andraus; acrescentar aqui os itens 1–5 depois de #167/#170/#168 mesclados, para não conflitar) · `docs/handoffs/ramo-ccr-b7c09dc1-y4rafd/` (cadeia deste ramo) · PRs #159, #164 (mesclados), #169, #167 (abertos).
