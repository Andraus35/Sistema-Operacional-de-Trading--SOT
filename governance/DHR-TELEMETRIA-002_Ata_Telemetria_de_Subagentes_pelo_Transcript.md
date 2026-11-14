# DHR-TELEMETRIA-002 — Ata — Telemetria de subagentes pelo transcript (correção determinística)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | `DHR-TELEMETRIA-CUSTO-001` (BL-036) · `scripts/telemetria_tokens.py` · `scripts/telemetria-tokens.js` · `tests/test_telemetria_reconciliar.py` · `governance/MECANISMOS.json` (`hook.telemetria-tokens`) · `DHR-PROCESSO-EXPERIMENTOS-001` |
| Data | 2026-11-14 |
| Status | **APLICADO no ramo; vigora com o merge do PR (assinatura de Andraus).** Ordem expressa de Andraus (chat, 2026-11-14): "Corrigir deterministicamente a telemetria". Altera `.claude/settings.json` (hooks) e o registro de mecanismos: vale a ordem expressa citada aqui (AGENTS.md §10). |
| Compatibilidade | Patch/Minor (corrige a medição; o registro antigo continua legível; custo segue INDETERMINADO sem preço) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Correção de mecanismo de medição; não altera texto de agente de construção nem método. |

## 1. Decisão de Andraus `[FATO]` (chat, 2026-11-14)
"Corrigir deterministicamente a telemetria" — a telemetria local mostrava 9 chamadas de agente **sem tokens** ("formato do tool_response não reconhecido") e as retrospectivas ficavam com Economicidade INDETERMINADO.

## 2. Causa-raiz `[FATO]` (medida) e correção `[INFERÊNCIA]` do Orquestrador
- **Causa:** agente em segundo plano devolve o uso só no **fim**, como notificação de tarefa, **fora de qualquer chamada de ferramenta**; o `PostToolUse/Agent` só vê o "lançado". Não era formato desconhecido: o dado não existe naquele evento.
- **Fonte real:** o transcript de cada subagente (`subagents/agent-<id>.jsonl` + `.meta.json` com tipo, modelo, descrição, `finished`). **Armadilha medida:** o transcript repete a mesma resposta em várias linhas com o mesmo `message.id` (ex.: 61 linhas para 27 respostas únicas); somar linhas multiplicaria o consumo. A leitura é **deduplicada por id de resposta**.
- **Correção:** `telemetria_tokens.py reconciliar` (idempotente; chave `agent_id`, `bytes` e `v` de formato) lê os transcripts e mantém **1 registro por agente**; roda sozinho no `SubagentStop` e no `Stop` via `telemetria-tokens.js`. Substitui os stubs de lançamento da sessão; o `resumo` não conta stub como chamada. `total` = tokens **novos** (in + out + cache criado); cache lido à parte (re-leitura do contexto a cada turno, só entra no custo); **tempo ativo** = soma de intervalos ≤ 30 min (a janela total, que inclui retomadas e noites, fica em `janela_ms`). `tokens <agent_id>` imprime o valor para a convenção `TOKENS:` do parecer.
- **Resultado ao vivo:** os 9 subagentes da sessão foram medidos (antes: 9 sem tokens); `.telemetria/` não é versionado, o retrato datado vai para `governance/aprendizado/TELEMETRIA-TOKENS.md`.

## 3. O que esta ata NÃO afirma
- Os totais **não coincidem** com o número que o harness mostra na notificação de tarefa (e não conseguimos reproduzi-lo); a fonte adotada é o transcript. Custo em USD é equivalente de tabela, **não cobrança** (plano com assinatura); preço ausente continua INDETERMINADO. Custo fora do Conviction Vector (INV-04).
- Cobre agentes cujo transcript existe na máquina da sessão (`~/.claude/projects/...`); em container reiniciado o transcript some e o registro local também (a telemetria é dado de estado local, não versionado).
- Não altera `AGENTS.md`, agentes, ROADMAP nem decisões abertas.

## 4. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4 · BL-026 · P-13 · localização da confluência fractal · DN-1. **Nenhuma decisão aberta é fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] Ordem de Andraus (chat 2026-11-14) · [x] `telemetria_tokens.py` + hook + testes (10; 5 mutantes mortos) · [x] `MECANISMOS.json` · [x] CATALOGO · [x] RPSA · [ ] merge (PR, CI verde — assinatura)

---

**Andraus** — *ordem dada no chat, 2026-11-14; registro pelo Orquestrador.*
