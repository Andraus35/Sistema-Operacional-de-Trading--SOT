---
handoff_id: HO-2026-11-07-7dbcb1d-1
previous: HO-2026-11-07-bb49346-2
data: 2026-11-07
branch: ccr-7dbcb1d1-e5d5dd
base_commit: ffa37d7
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-7dbcb1d1-e5d5dd: registro da homologação da abertura da SPEC-008)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
Andraus homologou a **abertura da SPEC-008** (chat, 2026-11-07). Este ramo registrou o ato: ata `governance/DHR-SPEC008-001_Ata_Homologacao_Abertura_SPEC-008.md`, `ROADMAP.md` (seção, tabela do §25 e "Decisões FECHADAS" `SPEC-008-ABERTURA`), `CATALOGO-OFICIAL.md`, `rpsa-ledger.json`. **NÃO é baseline; sem Plan.** Material em `specs/features/SPEC-008/`; pareceres em `governance/propostas/SPEC-008/`. Handoff anterior da frente: `handoffs/ccr-bb493467-9zd9m7.md` (HO-2026-11-07-bb49346-2). Nenhum PR aberto por este ramo.

## 2. Estado (conferido ao vivo em 2026-11-07, base `ffa37d7`)
`gate_manifest` íntegro · `check_refs` ERRO=0 · `check_rpsa` OK · `check_coesao` ERRO=0 (COE-12 aponta linha de handoff de **outro** ramo, `handoffs/ccr-b7c09dc1-y4rafd.md`, não tocada) · mapa em dia. Suíte (504 unittest, hooks, ask-guard, npm test) passou no início da sessão; delta posterior só documental.

## 3. Lições
Registrar homologação = ata + ROADMAP (seção, tabela, FECHADAS) + CATALOGO + `check_rpsa.py --register ... --write`; "Próximo trabalho autorizado" não muda (precedente DHR-SPEC049-001).

## 4. Verificado (LOOP-001 passo 4)
Sem parecer novo nesta sessão; ledger e lacunas (C99, C01, C06, C10) como no handoff anterior da frente.

## 5. Próximo passo único
Só por ordem expressa de Andraus: **Manager Contract** curto (P-4) e depois o **Plan da SPEC-008** (Dossiê válido até 2027-02-05; teto 2.000 linhas; gate `validate_spec_sot.py`). A Spec de Tempo tem Plan próprio depois. Antes de outra Spec: `loop_ledger.py --retro-check SPEC-008`.

## 6. Decisões
DHR-SPEC008-001 (P-1..P-13, CONF-1..5). Abertas (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4. Fica a conferir, no Plan: número final da Spec de Tempo (candidato SPEC-050). O `ROADMAP.md` prevalece.

## 7. Becos sem saída
Abertura sem `plan.md` não passa pelo `revisor_gate.py`; o gate vale a partir do Plan.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas, `WORKFLOW.md` (P-11/P-12/P-13/CONF-1/CONF-5 tocam texto dele: só Andraus edita), `AGENTS.md`, `.claude/agents/*`, handoff de outro ramo.

## 9. Reverificar ao vivo
- [ ] `git fetch origin`; `git log -1 origin/main`; se o ramo foi mesclado, `git checkout -B <ramo> origin/main`
- [ ] `gate_manifest.py --check`, `check_refs.py`, `check_handoff.py`, `check_rpsa.py`, `check_coesao.py`
- [ ] `build_map.py` e `--check` (não commitar `docs/mapa/`)
- [ ] Suíte: `python -m unittest discover -s tests`, `node tests/test-hooks.js`, `node tests/test-ask-guard.js`, `npm test`
- [ ] ROADMAP: decisões abertas/fechadas; versão de `WORKFLOW.md`; `loop_ledger.py --stdout`

## 10. Aguardando Andraus
Ordem para abrir o Manager Contract e o Plan da SPEC-008. Pauta: `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`specs/features/SPEC-008/` · `governance/DHR-SPEC008-001_*` · `governance/propostas/SPEC-008/` · `handoffs/` · `docs/handoffs/`
