---
handoff_id: HO-2026-11-08-c64455f-4
previous: HO-2026-11-08-c64455f-3
data: 2026-11-08
branch: ccr-c64455fe-no91eq
base_commit: eaa1a1c
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-c64455fe-no91eq: minuta de homologação do MMC-001)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
**MMC-001 + errata R3-m07 na `main`** (PRs #190 `13c3516` e #191 `eaa1a1c`). Nova ordem de Andraus (AskUserQuestion 2026-11-08): **marco da retrospectiva = aprovação final da Spec** (Plan homologado, sem achados). Aplicado no ramo, **PR ainda não aberto**: `AGENTS.md` §12 passo 5 (texto anterior preservado), texto do `loop_ledger.py` (comportamento inalterado, 11 testes OK), ata `DHR-LOOP-002`, CATALOGO, RPSA. Efeito: a retrospectiva da SPEC-008 **só nasce com o Plan aprovado**.

## 2. Estado (ao vivo, 2026-11-08)
`gate_manifest` íntegro · `check_refs` ERRO=0 · `check_rpsa` ok · `check_coesao` ERRO=0 · mapa em dia · `unittest` 504 OK · hooks e `npm test` OK. Ramo = `origin/main` (97703af) ao iniciar.

## 3. Lições
Roteador: Revisor só deriva classe com `ALVO` que traga `Complexidade` (usar `ABERTURA.md`); `Patch` na CR-001 não muda a versão (não existe "v1.0.1"). Homologação = ata + `git mv` + ROADMAP (seção, tabela, FECHADAS) + CATALOGO + `check_rpsa --register`. Minuta que cita o arquivo futuro da ata com caminho completo gera ERRO no `check_refs`: citar sem extensão/caminho.

## 4. Verificado (LOOP-001 passo 4)
3 categorias mais recorrentes do ledger: C07 (45), C01 (33), C02 (32). Lacunas abertas: C99, C06, C10, C03.

## 5. Próximo passo único
Andraus mandar abrir/mesclar o PR do `DHR-LOOP-002` (mexe no `AGENTS.md`: só por ordem expressa, já dada). Depois, por ordem expressa: Plan da SPEC-008; só com o Plan aprovado vence a retrospectiva da SPEC-008. Ao terminar a frente, mover este handoff para `docs/handoffs/ramo-ccr-c64455fe-no91eq/`.

## 6. Decisões
DHR-SPEC008-001; DHR-SPEC008-002 (homologação do MMC-001); DHR-SPEC008-003 (errata R3-m07, Patch); DHR-LOOP-002 (marco da retrospectiva); A-1..A-5 e recorte da P-7 (chat 2026-11-07, só como dado — a ata é dele). Abertas (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4. O `ROADMAP.md` prevalece.

## 7. Becos sem saída
Gate determinístico não vale para o contrato (não é plan.md; `revisor_gate` inerte em nuvem).

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas, `WORKFLOW.md`, `AGENTS.md`, `.claude/agents/*`, `ROADMAP.md`, handoff de outro ramo.

## 9. Reverificar ao vivo
- [ ] `git fetch origin`; `git log -1 origin/main`; se o ramo foi mesclado, `git checkout -B <ramo> origin/main`
- [ ] `gate_manifest.py --check`, `check_refs.py`, `check_handoff.py`, `check_rpsa.py`, `check_coesao.py`
- [ ] `build_map.py` e `--check` (não commitar `docs/mapa/`)
- [ ] Suíte: `python -m unittest discover -s tests`, `node tests/test-hooks.js`, `node tests/test-ask-guard.js`, `npm test`
- [ ] ROADMAP: decisões abertas/fechadas; versão de `WORKFLOW.md`; `loop_ledger.py --stdout`

## 10. Aguardando Andraus
Ordem para o PR/merge; ordem para o Plan da SPEC-008. Pauta: `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`governance/propostas/SPEC-008/` (minuta histórica `MINUTA-ATA-*` e pareceres R1–R3) · `governance/MMC-001_Manager_Contract.md` · `governance/DHR-SPEC008-001_Ata_Homologacao_Abertura_SPEC-008.md` · `handoffs/ccr-7dbcb1d1-e5d5dd.md` · `handoffs/` · `docs/handoffs/`
