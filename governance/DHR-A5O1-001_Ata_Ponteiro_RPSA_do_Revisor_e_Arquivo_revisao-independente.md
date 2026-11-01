# DHR-A5O1-001 — Ata de Decisão — Ponteiro do carimbo RPSA em `revisor.md` (A5-O1) e arquivamento de `revisao-independente/` (A10)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador / Revisor SOT |
| Ref | Ordem de Andraus (AskUserQuestion, 2026-11-01): "Aplicar A5-O1 e arquivar revisao-independente (Recomendado)" · `governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-A5-LEITURA-OBRIGATORIA-2026-11-01.md` (O1) · `PROPOSTA-A10-FERRAMENTAS-SEM-CONSUMIDOR-2026-11-01.md` · `DHR-RPSA-001` |
| Data | 2026-11-01 |
| Status | **APLICADA por ordem de Andraus** (emenda a arquivo reservado `.claude/agents/revisor.md` — AGENTS.md §10; o modelo curto NÃO se aplica, pois toca agente). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Patch |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Uma frase de `revisor.md` (Short-circuit) passa a apontar o livro-razão RPSA em vez do CATALOGO; sem mudança de método nem de fronteira. |

## 1. Mudança `[FATO]`
1. **`.claude/agents/revisor.md` l.148 (Short-circuit via RPSA):** "compare seu carimbo com a última linha de DHR do `CATALOGO-OFICIAL.md`" → "com a última entrada `"em_escopo": true` do livro-razão `governance/rpsa-ledger.json` (é o que `check_rpsa.py` confere; `DHR-RPSA-001`)". O texto anterior fica citado na própria linha (INV-07). Motivo: o carimbo já é conferido contra o livro-razão; o `CATALOGO-OFICIAL.md` tem ≈ 100 KB (≈ 25 mil tokens) e o ledger ≈ 24 KB. A regra do Short-circuit (sem entrada em escopo mais recente que o carimbo, as atas já estão incorporadas) **não mudou**.
2. **`revisao-independente/` → `docs/_legacy/revisao-independente/`** (`git mv`), com `ARQUIVADO.md` datado. **Conservação provada:** `LEIA-ME.txt` (`534d5325…`) e `PEDIDO-COPILOT-COM-REPO.txt` (`68910a26…`) com o **mesmo sha256** antes e depois. As atas antigas que citam o caminho antigo não foram alteradas (INV-07).

## 2. Ressalvas `[FATO]`
- **Gêmeo não tocado:** `especificador.md` l.109 tem o **mesmo** texto defasado (aponta ao `CATALOGO`). Como o pedido de Andraus foi para o Revisor, **não foi editado**; fica como pedido na `PAUTA-DE-DECISOES.md`.
- **Ganho de tokens não medido:** não se verificou se o Revisor abre o `CATALOGO-OFICIAL.md` para esse fim; o ganho pode ser zero (a proposta já declarava isso). O arquivamento da pasta tem ganho de tokens ≈ 0 (não era leitura obrigatória).
- O Revisor não tem Bash; ele **lê** `governance/rpsa-ledger.json` (Read), sem precisar de comando.
- Nenhuma decisão aberta do ROADMAP foi tocada (CONS-01); `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`, `canon/` e selos **não** foram alterados.

## 3. Registro
- [x] Esta ata · [x] `revisor.md` (1 linha) · [x] pasta arquivada com prova de conservação · [x] carimbo RPSA (`check_rpsa.py --register`) · [ ] merge (só por ordem de Andraus)
