---
handoff_id: HO-2026-11-17-d9583a3-2
previous: HO-2026-11-17-d9583a3-1
data: 2026-11-17
branch: ccr-d9583a3d-s5p73b
base_commit: e63e901
spec_autorizada: SPEC-008 = PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC008-005, 2026-11-15; 4 condições na ata §3; sem BUILD); SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-d9583a3d-s5p73b: aplicação das propostas P13–P18 da retrospectiva da SPEC-008)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
P13–P18 aplicadas e **mescladas** (PR #196, `e63e901`, `DHR-RETRO-004`). Em seguida Andraus respondeu a um questionário de boas práticas (AskUserQuestion 2026-11-17): **H1** limpeza do repo (só proposta), **H2** medir detectores na próxima Spec antes de promover, **H3** pauta de decisões abertas com bloqueio/prazo por evento, e **próxima frente = errata das 4 condições do Plan da SPEC-008**. Este PR traz H1–H3 (docs): `governance/propostas/MELHORIAS-PROCESSO/PROPOSTAS-REPO-BOAS-PRATICAS-2026-11-17.md` + quadro na seção C de `governance/PAUTA-DE-DECISOES.md`. Nada aplicado; nenhuma decisão fechada.

## 2. Estado (ao vivo, 2026-11-17, `main` = `263a5a5`)
`gate_manifest` íntegro · `check_rpsa` ok · `check_coesao` ERRO=0 (2 WARN COE-12 antigos no HANDOFF.md raiz) · testes novos: fsm_check 12, historico_do_diff 8, ancora_hash 7, cenario_precondicao 9, fato_locais 24, delta_pacote 6, gate_extra 35, pre_entrega 4 — todos OK. `check_refs` ERRO=4 só por `docs/mapa/MAPA-PROJETO.md` (arquivo gerado, não versionado; some após `build_map.py`).

## 3. Lições
- `ata` no `MECANISMOS.json` é um ID só (schema COE-14); ampliação por outra ata vai em `nota`.
- Todo `tests/test_*.py` novo precisa de passo no `ci.yml` (COE-02).
- Arquivo selado alterado ⇒ `gate_manifest.py --write` + ata citando o diff para o dono em CODEOWNERS.

## 4. Verificado (LOOP-001 passo 4)
Ledger lido na SPEC-008: categorias mais recorrentes C07 (45), C01 (33), C02 (32); lacunas C99, C06, C10, C03 — P14/P16/P17 atacam C07/C06/C10/C03. Medição de ganho fica para a próxima Spec.

## 5. Próximo passo único
Esperar a ordem de Andraus para mesclar o PR de H1–H3 (só docs). **Depois, em PR separado e em sequência (DHR-UM-RAMO-UM-PR-001): errata aditiva das 4 condições do Plan da SPEC-008** (R3-m04/m05/m07/m08; ver `governance/propostas/SPEC-008/PARECER-REVISOR-SPEC008-PLAN-R3-2026-11-15.md`; Especificador classe O, errata não muda a versão se for Patch — CR-001 l.439). Só por ordem expressa: aplicar H1 (selado: `check_refs.py`), promover detectores (regra H2), próxima Spec.

## 6. Decisões
`DHR-RETRO-004` (esta frente); herdadas: DHR-SPEC008-005, DHR-AVALIACAO-002. Abertas (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4. O `ROADMAP.md` prevalece.

## 7. Becos sem saída
Integrar P14(a) direto no `check_refs.py` sem ordem: é selado e bloqueante no CI — por isso o detector é separado.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas, `WORKFLOW.md`, `AGENTS.md`, `.claude/agents/*`, `ROADMAP.md`, handoff de outro ramo.

## 9. Reverificar ao vivo
- [ ] `git fetch origin`; `git log -1 origin/main`; se o ramo foi mesclado, `git checkout -B <ramo> origin/main`
- [ ] `gate_manifest.py --check`, `check_refs.py`, `check_handoff.py`, `check_rpsa.py`, `check_coesao.py`
- [ ] `build_map.py` e `--check` (não commitar `docs/mapa/`)
- [ ] Suíte: `python -m unittest discover -s tests`, `node tests/test-hooks.js`, `node tests/test-ask-guard.js`, `npm test`
- [ ] ROADMAP: decisões abertas/fechadas; versão de `WORKFLOW.md`; `loop_ledger.py --stdout`

## 10. Aguardando Andraus
Ordem de merge deste PR. Pauta: `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`governance/DHR-RETRO-004_Ata_Aplicacao_das_Propostas_P13_a_P18_da_Retrospectiva_SPEC-008.md` · `governance/propostas/MELHORIAS-PROCESSO/PROPOSTAS-RETRO-SPEC-008-2026-11-15.md` · `CONVENCAO-TABELA-FSM.md` (mesma pasta) · `handoffs/ccr-c64455fe-no91eq.md` · `docs/handoffs/`
