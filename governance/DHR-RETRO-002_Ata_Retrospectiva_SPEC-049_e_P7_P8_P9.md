# DHR-RETRO-002 — Ata de Decisão — Retrospectiva da SPEC-049 feita agora; propostas P7, P8 e P9

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordens de Andraus (chat, 2026-10-31, respostas ao AskUserQuestion do Orquestrador) · `AGENTS.md` §10 e §12 passo 5 · `DHR-RETRO-001` · `DHR-SPEC049-002` · `governance/aprendizado/RETROSPECTIVAS.md` |
| Data | 2026-10-31 |
| Status | **APLICADA por ordem de Andraus** (AGENTS.md §10). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Registra retrospectiva e um detector informativo do Orquestrador; a emenda ao `revisor.md` (P8) tem ata própria (`DHR-AGENTS-P8-001`, escopo sim). |

## 1. Decisões de Andraus `[FATO]`
1. **Retrospectiva da SPEC-049: "Fazer a retrospectiva agora com os dados disponíveis"** — em vez de aguardar a "rodada real" (decisão anterior dele no HANDOFF). Feita em `RETROSPECTIVAS.md` (linha-índice SPEC-049 = `FEITA`; `loop_ledger.py --retro-check SPEC-049` = FEITA). O que não foi levantado está marcado **n/m** na seção; as propostas P10–P12 ficam **pendentes de Andraus**.
2. **P7 — aprovada como detector informativo:** `scripts/fato_locais.py` (tabela fato→locais; conferência de listas de linhas; `--base` para propagação parcial). Sem hook, sem bloqueio; teste bloqueante no CI; registrado em `MECANISMOS.json` (`det.fato-locais`, COE-14). 20 testes; 8 mutantes mortos.
3. **P8 — aprovada:** o Orquestrador roda o gate e entrega `GATE-D:` ao Revisor em nuvem — aplicada pela ata `DHR-AGENTS-P8-001` (emenda ao `revisor.md`; pré-teste adversarial achou e corrigiu a falha "REPROVADO_D descartado por formato").
4. **P9 — dada por atendida na origem** pelo corte do `AGENTS.md` §7 (`DHR-AGENTS-SEC7-001`): o §7 aponta ao ROADMAP; sem mecanismo novo.

## 2. Não fechado `[FATO]`
Nenhuma decisão aberta do ROADMAP foi fechada. A "dispensa de rodada real" aplica-se só à retrospectiva da SPEC-049 e **não** autoriza abrir outra Spec: o plano do próximo Plan/Spec segue só por ordem de Andraus.

## 3. Registro
- [x] Esta ata · [x] retrospectiva escrita e índice `FEITA` · [x] detector + testes + CI + MECANISMOS.json · [ ] merge (assinatura de Andraus)
