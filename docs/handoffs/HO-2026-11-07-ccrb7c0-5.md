---
handoff_id: HO-2026-11-07-ccrb7c0-5
previous: HO-2026-11-07-ccrb7c0-4
data: 2026-11-07
branch: ccr-b7c09dc1-y4rafd
base_commit: 489494f
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-b7c09dc1-y4rafd: concorrência entre sessões)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece. Este ID usa o formato proposto HO-<data>-<ramo curto>-<n> porque o HO-2026-11-01-157 já existia com outro conteúdo em `docs/handoffs/` (ramo `ccr-a79e19ef-2zl738`); a cópia exata do meu HO-157 está em `docs/handoffs/ramo-ccr-b7c09dc1-y4rafd/`.

## 1. Frente atual

**Fechamento da sessão de 2026-11-07 (ordens de Andraus no chat):** PRs #173, #174 e #175 **mesclados** (o #175 traz o rascunho da ata do handoff por ramo, que **não vigora**). **Limpeza dos ramos A e B feita por Andraus no Termux:** os 7 ramos (4 contidos na `main` + 3 só handoff/mapa) sumiram do remoto; restam só os 6 do grupo C (`ccr-e3c0fb7e-63d2l9`, `spec-006-abertura`, `auditor-externo-integracao`, `ferramentas-estresse`, `ccr-3a0d581c-6cj4ig`, `spec006-plan`), que Andraus roda depois de ler a triagem (`bash ~/arquivar-ramos.sh C`: cria a tag `arquivo/<ramo>`, confere o SHA e só então apaga). O ruleset `proteger-main` passou por 3 merges sem recusa. **Medição do efeito agendada para ~7 dias** (lembrete via `send_later`, ordem de Andraus): contar merges de integração, conflitos em handoff/mapa/ledger e colisões de ID contra a linha de base (6 merges de integração/30 dias; mapa 214 toques; `HANDOFF.md` 124). Nada novo aplicado.

**Decisões de Andraus (chat, 2026-11-07):** PR #174 mesclado; limpeza de ramos **A e B agora, C depois** (ele roda `arquivar-ramos.sh` no Termux; eu não apago: 403); **redigir ata e texto do `AGENTS.md` §11 sem aplicar** → rascunho `CONCORRENCIA-DE-SESSOES/RASCUNHO-ATA-HANDOFF-POR-RAMO-2026-11-07.md` (R1 revista: raiz estática sem tabela; passo de migração do HO-163 da raiz exige combinar com a frente `ccr-a79e19ef-2zl738`). Nada aplicado.

**Sessão de 2026-11-07 (Andraus aprovou a direção da regra do handoff e autorizou pré-teste e triagem):** pré-teste feito (`CONCORRENCIA-DE-SESSOES/PRETESTE-HANDOFF-2026-11-07.md`): a tabela de frentes na raiz AINDA conflita; recomendação revista = raiz estática sem tabela. Protótipo HO-16/HO-17 (31/31 testes, 4 mutantes mortos) em patch, **não instalado**. Triagem de ramos refeita com histórico completo (os "101/175/120 commits" eram de clone raso): grupo A (4 contidos) e B (3 só handoff/mapa) apagáveis; grupo C (6) com tag `arquivo/<ramo>` antes; script `arquivar-ramos.sh` para o Termux de Andraus. Nada apagado nem aplicado.

**Camada B FEITA (2026-11-07, Andraus rodou o script no Termux e mostrou a saída):** ruleset `proteger-main` **id 26739886**, `enforcement: active`, **bypass 0**, regras `deletion`, `non_fast_forward`, `pull_request` (0 aprovações, Code Owners desligado) e `required_status_checks` (`Validate SOT Harness`, ramo atualizado obrigatório). `allow_update_branch=true`; `delete_branch_on_merge` já estava ligado. **Merge queue indisponível** (conta pessoal). Desligar em emergência: `bash ~/proteger-main.sh desligar` (Termux de Andraus). Efeito esperado: nenhum push direto na `main`; PR só mescla com CI verde e ramo em dia, inclusive para agentes. **Ainda não observei uma recusa real**: o PR deste handoff é o primeiro a passar pela regra.

**Estado em 2026-11-06:** os PRs #167, #168, #169, #170 e #171 estão mesclados; nenhum PR aberto. Os comandos do ruleset `proteger-main` (sem bypass) e `allow_update_branch` foram entregues a Andraus para rodar no Termux; **não sei se ele rodou** (a ferramenta não lê rulesets). Esta sessão escreveu a proposta de regra do handoff (`governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-HANDOFF-ENTRADA-E-CICLO-DE-VIDA-2026-11-06.md`): raiz como índice, ID por ramo, arquivar handoff de ramo mesclado. **Nada aplicado.** Colisão viva: dois handoffs com o ID HO-2026-11-01-157 na `main`.
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
Na data do lembrete (~2026-11-14): fazer `git fetch --unshallow` (clone raso infla contagens), medir e relatar a Andraus em AskUserQuestion. Antes disso: aguardar Andraus assinar/editar o rascunho da ata do handoff (só então aplicar em PR separado), e conferir o grupo C com `check_branches.py` se ele rodar o script. Frente do handoff da raiz (HO-163): combinar com `ccr-a79e19ef-2zl738` antes de qualquer migração.

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
