---
handoff_id: HO-2026-11-07-7dbcb1d-3
previous: HO-2026-11-07-7dbcb1d-2
data: 2026-11-07
branch: ccr-7dbcb1d1-e5d5dd
base_commit: 615d0f5
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-008 = ABERTURA HOMOLOGADA (DHR-SPEC008-001, 2026-11-07; CRITICAL D0–D8, dividida com a Spec de Tempo [candidata SPEC-050]; Plan pendente; sem BUILD); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (ramo ccr-7dbcb1d1-e5d5dd: Manager Contract da SPEC-008)

> Dado de estado (PCC-001), não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece.

## 1. Frente atual
**MANAGER CONTRACT (P-4 da SPEC-008) — PROPOSTA v0.3, CONFORME condicional (R3), AGUARDANDO homologação de Andraus. NÃO é baseline.** PRs #187 (ata DHR-SPEC008-001) e #188 (contrato v0.2 + R1/R2) mesclados (`615d0f5`). Neste ramo, após o #188: Andraus decidiu **A-1..A-5** (chat 2026-11-07) → contrato v0.3; **R3** do Revisor: só Menores, FICHA-M R3-m01..m06 aplicada pelo Orquestrador; resta **R3-m07** (classe O, não bloqueante: Classe D/C como "orientação" × obrigação, §3.1.3/§8.2-bis). Pareceres em `governance/propostas/SPEC-008/` (R1, R2, R3). Nenhum PR aberto.

## 2. Estado (ao vivo, 2026-11-07)
`gate_manifest` íntegro · `check_refs` ERRO=0 · `check_doc_sync` ERRO=0 · `check_invariants` 0 · mapa em dia. Gate determinístico NÃO verificado (contrato não é plan.md).

## 3. Lições
Registrar homologação = ata + ROADMAP (seção, tabela, FECHADAS) + CATALOGO + `check_rpsa.py --register ... --write`; "Próximo trabalho autorizado" não muda (precedente DHR-SPEC049-001).

## 4. Verificado (LOOP-001 passo 4)
Médias do R1 (M-01..M-04) em `CAUSAS-PREVENCAO.md`; R2 e R3 sem Média. Achados M aplicados: R1 4, R2 7, R3 6 (17 de 28 itens). Lacunas abertas: C99, C01, C06, C10.

## 5. Próximo passo único
Andraus **homologar o Manager Contract** (ordem expressa). A ata deve citar: A-1..A-5, o recorte da P-7 (só "parada por gasto só por Andraus" nas três Fases; "orçamento avisa e escala" só SPEC-008/Spec de Tempo — confirmado por Andraus em chat) e o registro no CATALOGO (A-3). Na homologação o Orquestrador move o arquivo para `governance/` com ID **MMC-001 v1.0**. Opcional antes: R3-m07 ao Especificador. Depois: Plan da SPEC-008 só por ordem expressa; antes de outra Spec, `loop_ledger.py --retro-check SPEC-008`.

## 6. Decisões
DHR-SPEC008-001. Em chat (2026-11-07): A-1 = MMC-001 v1.0 (a vigorar na homologação; hash da ABERTURA `8ea5d9a` só contexto); A-2 = Spec de Tempo herda (SPEC-050 segue candidata); A-3 = mora em `governance/` após homologar; A-4 = contrato declara precedência, fontes não editadas; A-5 = CONF-1/P-12/CONF-5 fronteira vigente e P-7 (parada por gasto) nas três Fases. Abertas (CONS-01): J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4. O `ROADMAP.md` prevalece.

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
Ordem para homologar o Manager Contract (MMC-001 v1.0) e, depois, para o Plan da SPEC-008. Pauta: `governance/PAUTA-DE-DECISOES.md`.

## 11. Ponteiros
`specs/features/SPEC-008/` · `governance/DHR-SPEC008-001_*` · `specs/features/SPEC-008/MANAGER-CONTRACT.md` · `governance/propostas/SPEC-008/` · `handoffs/` · `docs/handoffs/`
