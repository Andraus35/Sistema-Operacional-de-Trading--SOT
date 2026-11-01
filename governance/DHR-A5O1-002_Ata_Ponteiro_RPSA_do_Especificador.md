# DHR-A5O1-002 — Ata de Decisão — Ponteiro do carimbo RPSA em `especificador.md` (gêmeo do A5-O1)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador / Especificador SOT |
| Ref | Ordem de Andraus (AskUserQuestion, 2026-11-01): "Aplicar o ponteiro gêmeo no especificador.md (Recomendado)" · `DHR-A5O1-001` (mesma correção no Revisor) · `PROPOSTA-A5-LEITURA-OBRIGATORIA-2026-11-01.md` (O1) · `DHR-RPSA-001` |
| Data | 2026-11-01 |
| Status | **APLICADA por ordem de Andraus** (emenda a arquivo reservado `.claude/agents/especificador.md` — AGENTS.md §10; modelo curto NÃO se aplica, pois toca agente). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Patch |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Uma frase de `especificador.md` (Short-circuit) passa a apontar o livro-razão RPSA em vez do CATALOGO; mesma correção já aplicada ao Revisor; sem mudança de método nem de fronteira. |

## 1. Mudança `[FATO]`
**`.claude/agents/especificador.md` l.109 (Short-circuit via RPSA):** "compare seu carimbo com a última linha de DHR do `CATALOGO-OFICIAL.md`" → "com a última entrada `"em_escopo": true` do livro-razão `governance/rpsa-ledger.json` (é o que `check_rpsa.py` confere; `DHR-RPSA-001`)". O texto anterior fica citado na própria linha (INV-07). A regra do Short-circuit (sem entrada em escopo mais recente que o carimbo, as atas já estão incorporadas) **não mudou**. Efeito: os dois agentes passam a apontar a mesma fonte, e o `CATALOGO-OFICIAL.md` (≈ 100 KB) deixa de ser o ponteiro do carimbo.

## 2. Ressalvas `[FATO]`
- O Especificador não tem Bash; ele **lê** `governance/rpsa-ledger.json` (Read). O ganho de tokens **não foi medido** (pode ser zero se o catálogo não era aberto para isso).
- Nenhuma decisão aberta do ROADMAP foi tocada (CONS-01); `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`, `canon/` e selos **não** foram alterados.

## 3. Registro
- [x] Esta ata · [x] `especificador.md` (1 linha) · [x] carimbo RPSA (`check_rpsa.py --register`) · [ ] merge (só por ordem de Andraus)
