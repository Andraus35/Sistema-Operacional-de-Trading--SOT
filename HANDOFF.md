---
handoff_id: HO-2026-11-07-raiz-1
previous: HO-2026-11-01-163
data: 2026-11-07
branch: main
base_commit: 34d9e29
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12/v1.13 HOMOLOGADAS (v1.13 = arquivo à parte, DHR-SPEC006-005); SPEC-007 = Plan reduzido v2.3 HOMOLOGADO — BASELINE (DHR-SPEC007-005; sem BUILD); SPEC-020 = BASELINE + ERRATUM-001 (tool correctness) + ERRATUM-002 (F1 de RAG faithfulness, prospectivo, DHR-SPEC020-002); SPEC-048 = Plan v1.4 HOMOLOGADO — BASELINE (DHR-SPEC048-002; sem BUILD); ERRATUM-REAPONT-001 HOMOLOGADO (DHR-REAPONT-001); SPEC-049 (WikiRAG Reading View) = ABERTURA HOMOLOGADA (DHR-SPEC049-001; HIGH D0–D7, uma Spec); PLAN v1.2 HOMOLOGADO — BASELINE (DHR-SPEC049-002, 2026-10-31; 3 condições na ata §3; sem BUILD)
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT (raiz: texto estático)

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência, a realidade prevalece. **Ninguém edita este arquivo no dia a dia:** o estado de cada frente vive no handoff do próprio ramo (AGENTS.md §11; `DHR-HANDOFF-RAMO-001`).

## 1. Frente atual
Sem frente aqui. Leia o `handoffs/<ramo>.md` da sua frente; em ramo novo, crie o seu com ID `HO-<data>-<ramo curto>-<n>` (ramo curto = 7 primeiros caracteres depois de `ccr-`).

## 2. Estado
Não há estado nesta raiz (uma tabela de frentes conflita entre sessões). O estado de cada frente está no handoff do ramo dela; o do ramo dos logs/pauta/medições A5 é o `handoffs/ccr-a79e19ef-2zl738.md`.

## 3. Lições
No handoff do ramo.

## 4. Verificado
No handoff do ramo (LOOP-001 passo 4).

## 5. Próximo passo único
Ler o `handoffs/<ramo>.md` da sua frente e executar a seção 9. Sem handoff próprio, o aviso HO-03 do `check_handoff` lembra de criá-lo.

## 6. Decisões
Por ID, no handoff do ramo; o `ROADMAP.md` prevalece.

## 7. Becos sem saída
No handoff do ramo.

## 8. Não tocar
`canon/` BASELINED, planos de Specs homologadas (só por erratum), `ROADMAP.md`, `atomic-spec.md`, `AGENTS.md`, `.claude/agents/*`, `CONFLICT-MAP`, `GATE-MANIFEST.sha256` e scripts do CODEOWNERS — só por ordem expressa de Andraus. Handoff de outro ramo.

## 9. Reverificar ao vivo
- [ ] `git fetch origin`; `git log -1 origin/main`; se o ramo foi mesclado, `git checkout -B <ramo> origin/main`
- [ ] `python scripts/gate_manifest.py --check`, `python scripts/check_refs.py`, `python scripts/check_handoff.py`, `python scripts/check_rpsa.py`, `python scripts/check_coesao.py`
- [ ] `python scripts/build_map.py` e `python scripts/build_map.py --check` (mapa não é versionado; não commitar)
- [ ] Suíte: `python -m unittest discover -s tests`, `node tests/test-hooks.js`, `node tests/test-ask-guard.js`, `npm test`
- [ ] ROADMAP: decisões abertas/fechadas; versão vigente de `WORKFLOW.md`
- [ ] Ledger só por `python scripts/loop_ledger.py --stdout` (não gravar em disco)

## 10. Aguardando Andraus
Pauta única: `governance/PAUTA-DE-DECISOES.md`. Ramo novo sem handoff próprio: criar `handoffs/<ramo>.md` antes de entregar.

## 11. Ponteiros
`handoffs/` (um arquivo por ramo ativo) · `docs/handoffs/ramo-<ramo>/` (handoff final de ramo mesclado) · ata `DHR-HANDOFF-RAMO-001` (em `governance/`) · `governance/PAUTA-DE-DECISOES.md`
