---
tipo: proposta-pre-testada
status: PROPOSTA (não vigente; nada instalado nem aplicado)
data: 2026-11-01
origem: AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md (itens P-A e P-F)
---
# P-A + P-F — pré-gate unificado e higiene do especificador.md

Decisões de Andraus (chat, 2026-11-01): começar por P-F(1–5)+P-A; o pré-gate é rodado pelo Orquestrador/hook (o Especificador continua sem Bash); detectores informativos até P-E medir falso alarme; PR sem mesclar.

## Conteúdo
| Arquivo | O que é | Estado |
|---|---|---|
| `pre_entrega.py` | Compõe `validate_spec_sot`, `check_repo_research`, `build_map --check` (bloqueantes, como no CI) e `check_invariants`, `check_dimensionamento`, `check_refs`, `backlog_triggers` + 13 detectores de `gate_extra`/`revisor_detectores` (informativos). Emite `pre-entrega.json` com sha256 de plan/checks. Sem lógica nova. | Testado (`test_pre_entrega.py`, 3 testes OK); **não instalado** |
| `PATCH-ESPECIFICADOR-P-F-2026-11-01.patch` | (1) TMP→Signal Package; (2) `AGENTS.md §3`→`§4`; (3) CCM-001 BASELINED e J-001 sem "trava SPEC-003"; (4) CC-01..CC-12; (5) §9 vira ponteiro ao ROADMAP; (6) item do Autopré-check: o Orquestrador roda `pre_entrega.py` e anexa o JSON. | `git apply --check` OK; **não aplicado** |

## Para instalar (só por ordem expressa de Andraus)
1. Mover `pre_entrega.py` para `scripts/` e o teste para `tests/`; registrar em `governance/MECANISMOS.json` (COE-14) e no `GATE-MANIFEST.sha256`.
2. `git apply` do patch (emenda homologada ao `.claude/agents/especificador.md`; carimbo RPSA via `check_rpsa.py --register`).
3. Fluxo: Especificador edita → Orquestrador roda `pre_entrega.py` → devolve o JSON → corrige até zero bloqueante → Revisor recebe o mesmo JSON (casado por `SHA256-ALVO`).

## Medir antes de promover (4Es)
Contar Médias do R1 com e sem pré-gate em 5 rodadas; P-E (mutação) para recall e falso alarme; detectores só viram bloqueantes por ordem de Andraus.

## Limites
O pré-gate não acrescenta recall: o backtest da auditoria deu 0/3 Médias com os detectores atuais. Seu ganho imediato é **prova anexa e antecipação** (o autor vê antes do Revisor). O recall vem de P-B, C-1/C-2 e P-D.
