# DHR-PRE-ENTREGA-001 — Ata de Decisão — Pré-gate unificado antes do Revisor (P-A) e higiene do `especificador.md` (P-F)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador / Especificador SOT / Revisor SOT |
| Ref | Ordem de Andraus (chat, 2026-11-01): respostas "P-F(1–5)+P-A", "Orquestrador/hook roda", "informativos primeiro", e a ordem **"Instalar"** · `governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md` · `.../PRE-ENTREGA/PROPOSTA-PRE-ENTREGA-2026-11-01.md` · `governance/MECANISMOS.json` |
| Data | 2026-11-01 |
| Status | **APLICADA por ordem de Andraus** (emenda ao `.claude/agents/especificador.md`, arquivo reservado — AGENTS.md §10; novo script selado). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Emenda ao Autopré-check (§7) e correções de fatos defasados no Especificador; a lista de decisões abertas (§9) passa a ponteiro ao ROADMAP (fonte única). |

## 1. Problema `[FATO]`
Auditoria de 2026-11-01: o §7 do Especificador mandava "rodar" scripts, mas o Especificador não tem `Bash` (A-1); os detectores `gate_extra`/`revisor_detectores` só rodavam do lado do Revisor (A-2); o Autopré-check não deixava rastro verificável (A-3); e o próprio arquivo tinha fatos defasados (A-5: TMP×Signal Package, `AGENTS.md §3`, CCM-001 "pendente", CC-01..CC-10, lista de decisões abertas copiada).

## 2. Decisão de Andraus `[FATO]`
Instalar **P-A** (pré-gate unificado) e **P-F(1–5)+(6)** (higiene do `especificador.md`). O pré-gate é rodado pelo **Orquestrador/hook**; o Especificador **continua sem `Bash`**. Detectores **informativos** até promoção por ordem de Andraus.

## 3. Mudança `[FATO]`
- `scripts/pre_entrega.py` (novo) + `tests/test_pre_entrega.py` (3 testes): compõe `validate_spec_sot`, `check_repo_research`, `build_map --check` (**bloqueantes**, como no CI) e `check_invariants`, `check_dimensionamento`, `check_refs`, `backlog_triggers` + 13 detectores de `gate_extra`/`revisor_detectores` (**informativos**); grava `pre-entrega.json` com sha256 de `plan.md`/`checks.md`. **Nenhuma lógica nova de detecção.**
- **Selo:** `scripts/pre_entrega.py` entra em `ARQUIVOS` de `gate_manifest.py` (manifesto regravado — o diff aparece para revisão de Andraus) e em `.github/CODEOWNERS`; o autor da Spec tem Write/Edit e não pode enfraquecer o próprio pré-gate sem aparecer no diff.
- `.claude/agents/especificador.md`: (1) TMP→Signal Package; (2) `AGENTS.md §3`→`§4`; (3) CCM-001 BASELINED e J-001 sem "trava SPEC-003"; (4) CC-01..CC-12; (5) §9 vira ponteiro ao `ROADMAP.md`; (6) novo item do Autopré-check: o Orquestrador roda `python scripts/pre_entrega.py specs/features/<SPEC>` e anexa o JSON; o Especificador não declara "rodei" sem ele. Carimbo RPSA alinhado por `check_rpsa.py --register`.
- `governance/MECANISMOS.json` (COE-14): `util.pre-entrega` novo; `agent.especificador` atualizado. CI: passo do teste.
- **Fluxo:** Especificador edita → Orquestrador roda o pré-gate → devolve o JSON → corrige até zero bloqueante vermelho → só então "Pronto para revisão"; o Revisor recebe o mesmo JSON (casado por `SHA256-ALVO`).

## 4. Limites honestos `[FATO]`
- O pré-gate **não aumenta o recall**: o backtest da auditoria deu **0/3 Médias** do Plan v1.0 da SPEC-049 com os detectores atuais. O ganho é **prova anexa e antecipação**.
- Fora desta ata (permanecem **propostas, não instaladas**): `detectores_novos.py` (C-1a/C-1b/C-2; C-2 **não viável**), `mutacao_pe.py`, P-B, C-3..C-6, P-D.
- Fluxo não testado com um Especificador real nesta sessão; medir Médias do R1 com/sem pré-gate em 5 rodadas antes de qualquer promoção.

## 5. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 6. Registro
- [x] Esta ata · [x] script e teste · [x] selo (manifesto + CODEOWNERS) · [x] emenda no `especificador.md` · [x] `MECANISMOS.json` · [x] carimbo RPSA · [ ] merge (ordem de Andraus)
