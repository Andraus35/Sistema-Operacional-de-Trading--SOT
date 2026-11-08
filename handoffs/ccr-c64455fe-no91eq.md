---
handoff_id: HO-2026-11-08-c64455f-5
previous: HO-2026-11-08-c64455f-4
data: 2026-11-08
branch: ccr-c64455fe-no91eq
base_commit: 2b54aa9
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-c64455fe-no91eq: minuta de homologação do MMC-001)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
**Frente SPEC-008 (Manager — Despacho e Ciclo): contrato e regra de processo concluídos e na `main`; falta o Plan.** Mesclados nesta sessão (2026-11-08): PR #190 (MMC-001 v1.0, `DHR-SPEC008-002`), #191 (errata R3-m07, Patch, `DHR-SPEC008-003`), #192 (marco da retrospectiva = aprovação final da Spec, `DHR-LOOP-002`, AGENTS.md §12 passo 5). Nenhum PR aberto. **Plan da SPEC-008 não existe** e só inicia por ordem expressa de Andraus.

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
**Só por ordem expressa de Andraus: abrir o Plan da SPEC-008.** Roteiro: (1) `git fetch` e ramo novo/`checkout -B` a partir da `main`; (2) reverificar (seção 9); (3) Plan com teto 2.000 linhas de corpo, alerta em 1.900 (RULE-ECC-07), uma peça só, CRITICAL D0–D8; Dossiê vale até 2027-02-05; (4) declarar `Disposição` de BL-026, BL-043..046 (todos `Em espera`; `backlog_triggers.py --abertura SPEC-008`) e a errata de re-apontamento da ABERTURA §8 só no Plan; (5) filha declara o pai por ID+versão **MMC-001 v1.0** (RULE-HV-01); (6) J-001/N-001 abertas: limiar "conclusiva" é parâmetro, sem número inventado; (7) gate: `validate_spec_sot.py` sobre o `plan.md` da SPEC-008 quando existir. A retrospectiva da SPEC-008 só vence **depois da aprovação final do Plan** (`DHR-LOOP-002`); a Spec de Tempo (candidata SPEC-050) tem Plan próprio depois.

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
Ordem expressa para o Plan da SPEC-008. Nada mais pendente desta frente. Pauta (vencimento 2026-11-15; lembrete 2026-11-14 da regra um-ramo-um-PR): `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`governance/propostas/SPEC-008/` (minuta histórica `MINUTA-ATA-*`, proposta e pareceres da errata R1–R2) · `governance/MMC-001_Manager_Contract.md` · `governance/DHR-SPEC008-001_Ata_Homologacao_Abertura_SPEC-008.md` · `handoffs/ccr-7dbcb1d1-e5d5dd.md` · `handoffs/` · `docs/handoffs/`
