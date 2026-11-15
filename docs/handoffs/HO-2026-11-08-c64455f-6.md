---
handoff_id: HO-2026-11-08-c64455f-6
previous: HO-2026-11-08-c64455f-5
data: 2026-11-08
branch: ccr-c64455fe-no91eq
base_commit: 84ed193
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-c64455fe-no91eq: minuta de homologação do MMC-001)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
**AVALIAÇÃO DE DESEMPENHO DE FIM DE SPEC (`DHR-AVALIACAO-001`) — aplicada no ramo, PR ainda não aberto.** Ordem de Andraus (chat 2026-11-08): avaliação obrigatória, determinística, com perguntas automatizadas e boas práticas. Entregue: `scripts/avaliacao_spec.py`, catálogo `governance/aprendizado/BOAS-PRATICAS.json` (12 itens, propostas), `loop_ledger --retro-check` exigindo avaliação RESPONDIDA, passo de CI bloqueante, 4ª regra da guarda de fim de turno, `AGENTS.md` §12 passo 6, `MECANISMOS.json` (`det.avaliacao-spec`), testes (15 + 7 JS; 5 mutantes mortos). **Prospectivo:** só Spec com ata de aprovação final de Data ≥ 2026-11-08. A SPEC-008 (sem Plan) ainda não é exigida. Estado anterior da frente: MMC-001, errata R3-m07 e marco da retrospectiva já na `main` (#190–#193).

## 2. Estado (ao vivo, 2026-11-08, `main` = `2b54aa9`)
`gate_manifest` íntegro · `check_refs` ERRO=0 · `check_rpsa` ok · `check_doc_sync` 0 · `check_invariants` 0 · `check_coesao` ERRO=0 (2 WARN COE-12 antigos no HANDOFF.md raiz) · mapa em dia · `unittest` 504 OK (CI verde nos 3 PRs). Contrato `governance/MMC-001_Manager_Contract.md` segue v1.0 (errata in loco, `[antes]` preservado).

## 3. Lições
- Homologar = ata + `git mv` + ROADMAP (seção, tabela §25, FECHADAS) + CATALOGO + `check_rpsa --register ... --write`; "Próximo trabalho autorizado" não muda.
- Roteador: o Revisor só deriva classe com `ALVO` que traga `Complexidade` (usar `specs/features/SPEC-008/ABERTURA.md`, CRITICAL → classe S3, `model: opus`); sem isso o hook nega (R-AC4). Especificador = classe O, opus, com `PARECER:` + `FICHA:` (esqueleto via `roteador_modelos.py esqueleto`).
- CR-001 l.439: Patch NÃO muda a versão (não existe "v1.0.1"); cheque a taxonomia antes de oferecer opções de versão a Andraus.
- Citar o arquivo futuro de uma ata com caminho/ID inexistente dá ERRO em `check_refs`/HO-06; citar sem extensão ou só depois de criada.
- Guarda G1 pós-Revisor: o Orquestrador abre `backlog/RMR-001` e `atomic-spec.md` (Grep) e anota adendo no parecer.

## 4. Verificado (LOOP-001 passo 4)
3 categorias mais recorrentes: C07 citação/âncora (45), C01 contradição interna (33), C02 ambiguidade/vocabulário (32). Lacunas abertas: C99, C06, C10, C03. Causas das Médias do R1 do contrato em `CAUSAS-PREVENCAO.md`; a Média ER1-M01 da errata (classificação de versão) registrada em `CAUSAS-PREVENCAO.md`.

## 5. Próximo passo único
Andraus mandar abrir/mesclar o PR do `DHR-AVALIACAO-001` (mexe no `AGENTS.md` e no CI: só por ordem expressa, já dada no chat). Depois, por ordem expressa: Plan da SPEC-008. **Ao aprovar o Plan da SPEC-008:** `python scripts/avaliacao_spec.py gerar SPEC-008 --write`, apresentar `perguntas SPEC-008` a Andraus por AskUserQuestion, ata da decisão, `registrar SPEC-008 --ata DHR-… --resposta "…"`, retrospectiva `FEITA`; só então `loop_ledger.py --retro-check SPEC-008` passa e outra Spec pode abrir. Roteiro do Plan: ver seção 9 do HO anterior em `docs/handoffs/HO-2026-11-08-c64455f-5.md` (teto 2.000 linhas, Dossiê até 2027-02-05, BL-026/043..046, pai MMC-001 v1.0, J-001/N-001 abertas).

## 6. Decisões
DHR-SPEC008-001; DHR-SPEC008-002 (homologação do MMC-001); DHR-SPEC008-003 (errata R3-m07, Patch); DHR-LOOP-002 (marco da retrospectiva); DHR-AVALIACAO-001 (avaliação de fim de Spec); A-1..A-5 e recorte da P-7 (chat 2026-11-07, só como dado — a ata é dele). Abertas (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4. O `ROADMAP.md` prevalece.

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
Ordem expressa para o PR do `DHR-AVALIACAO-001` e para o Plan da SPEC-008. Pauta (vencimento 2026-11-15; lembrete 2026-11-14 da regra um-ramo-um-PR): `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`governance/propostas/SPEC-008/` (minuta histórica `MINUTA-ATA-*`, proposta e pareceres da errata R1–R2) · `governance/MMC-001_Manager_Contract.md` · `governance/DHR-SPEC008-001_Ata_Homologacao_Abertura_SPEC-008.md` · `handoffs/ccr-7dbcb1d1-e5d5dd.md` · `handoffs/` · `docs/handoffs/`
