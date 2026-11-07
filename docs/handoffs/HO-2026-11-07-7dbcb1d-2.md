---
handoff_id: HO-2026-11-07-7dbcb1d-2
previous: HO-2026-11-07-7dbcb1d-1
data: 2026-11-07
branch: ccr-7dbcb1d1-e5d5dd
base_commit: 0bdff7b
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-7dbcb1d1-e5d5dd: Manager Contract da SPEC-008)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
**MANAGER CONTRACT (P-4 da SPEC-008) — PROPOSTA v0.2, CONFORME condicional (R2), AGUARDANDO Andraus. NÃO é baseline.** Homologação da abertura registrada e mesclada (PR #187, `0bdff7b`; ata DHR-SPEC008-001). Arquivo: `specs/features/SPEC-008/MANAGER-CONTRACT.md`. Pareceres em `governance/propostas/SPEC-008/`: R1 (NÃO CONFORME, 4 Médias) → v0.2 → **R2 CONFORME condicional** (só Menores; FICHA-M R2-m01..m04 aplicada pelo Orquestrador). Resta **R2-m05** (classe O, não bloqueante: alcance do §8.2-bis, exceção do §1, ADDED). Nenhum PR aberto.

## 2. Estado (ao vivo, 2026-11-07)
`gate_manifest` íntegro · `check_refs` ERRO=0 · `check_doc_sync` ERRO=0 · `check_invariants` 0 · `check_rpsa` OK · mapa em dia. Gate determinístico NÃO verificado (contrato não é plan.md; sem `revisor_gate` em nuvem).

## 3. Lições
Registrar homologação = ata + ROADMAP (seção, tabela, FECHADAS) + CATALOGO + `check_rpsa.py --register ... --write`; "Próximo trabalho autorizado" não muda (precedente DHR-SPEC049-001).

## 4. Verificado (LOOP-001 passo 4)
Médias do R1 (M-01..M-04) em `CAUSAS-PREVENCAO.md`. Achados M aplicados pelo Orquestrador: R1 m-01a/b/c e m-05a; R2 m01..m04 (11 itens de 21 achados). Lacunas abertas: C99, C01, C06, C10.

## 5. Próximo passo único
Andraus decidir **A-1** (ID/versão/hash da ABERTURA aprovada: último commit `8ea5d9a`), **A-2** (Spec de Tempo herda do contrato?), **A-3** (local após homologar; sugerido `governance/`), **A-4** (textos antigos divergentes) e **A-5** (CONF-1/CONF-5/P-12/P-7 viram herança fixa para SPEC-014/015?). Opcional antes: R2-m05 ao Especificador. Depois: Plan da SPEC-008 só por ordem expressa.

## 6. Decisões
DHR-SPEC008-001. Em chat (2026-11-07): A-1..A-5 e R2-m05 → "depois do parecer"; número da Spec de Tempo = candidato SPEC-050. Abertas (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4. O `ROADMAP.md` prevalece.

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
A-1..A-5 do Manager Contract; ordem para o Plan da SPEC-008. Pauta: `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`specs/features/SPEC-008/` · `governance/DHR-SPEC008-001_*` · `specs/features/SPEC-008/MANAGER-CONTRACT.md` · `governance/propostas/SPEC-008/` · `handoffs/` · `docs/handoffs/`
