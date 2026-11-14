# DHR-PROCESSO-EXPERIMENTOS-001 — Ata — Experimentos aprovados entram nos pedidos por código; teto de 3 rodadas

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | `DHR-EXPERIMENTO-PARADA-001` · `DHR-RETRO-003` (P10) · `governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md` · `scripts/experimentos_ativos.py` · `governance/EXPERIMENTOS-ATIVOS.json` · `governance/MECANISMOS.json` (`hook.experimentos-ativos`, `det.experimentos-ativos`) |
| Data | 2026-11-14 |
| Status | **APLICADO no ramo; vigora com o merge do PR (assinatura de Andraus).** Ordem expressa de Andraus (chat, 2026-11-14): "Reduzir teto para 3 rodadas. Prevenir deterministicamente essa falha. Corrigir deterministicamente a telemetria" (a telemetria é a ata `DHR-TELEMETRIA-002`). Altera `governance/` (registro de mecanismos) e `.claude/settings.json` (hook): vale a ordem expressa citada aqui (AGENTS.md §10). |
| Compatibilidade | Minor (acrescenta travas e um registro; nenhuma regra de método é afrouxada) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Mecanismo de processo (pedidos ao Especificador/Revisor e CI); não altera texto de agente de construção nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-11-14)
| # | Ponto | Decisão |
|---|---|---|
| T-1 | Teto de rodadas do experimento da regra de parada | **3 rodadas** (antes: 5 para peça CRITICAL) |
| T-2 | A falha: o experimento P10, aprovado para o "próximo Plan", não entrou nos pedidos das rodadas R1/R2 do Plan da SPEC-008 | **Prevenir deterministicamente** |

## 2. O que foi construído (leitura do Orquestrador `[INFERÊNCIA]`)
- **Teto 3:** `teto_rodadas_revisao = 3` no registro. Lido como **máximo de 3 rodadas de REVISÃO (pareceres do Revisor) do Plan**; o Especificador pode corrigir depois da 3ª, mas **nenhuma 4ª revisão** abre sem escalada a Andraus. Os tetos dos outros perfis do desenho original (LOW 2 · MEDIUM 3 · HIGH 4) **não** foram alterados por esta ordem (o valor 3 vale para este experimento, onde a peça é CRITICAL). Estado hoje: SPEC-008 tem 2 pareceres (R1, R2); a **R3 é a última rodada**; Média aberta depois dela **escala a Andraus**.
- **Prevenção determinística:** registro versionado `governance/EXPERIMENTOS-ATIVOS.json` + hook `PreToolUse Agent|SendMessage` (`experimentos-ativos.js`) que **nega** pedido ao Especificador/Revisor sobre o Plan de uma Spec no escopo de um experimento ativo se: (a) falta a linha `EXPERIMENTO: <id>` (a negação traz o texto das regras a colar); (b) ao Revisor, a rodada seguinte (pareceres existentes + 1) ultrapassa o teto e `escalado_por_andraus` é falso; (c) ao Revisor, da rodada 2 em diante falta `SHA256-ALVO: <64 hex>`. Cobre `Agent`, `Task` e `SendMessage`. Escopo `proximo-plan`: o **CI** (`experimentos_ativos.py --ci`, bloqueante) reprova se existir Plan em redação e o experimento "próximo Plan" ainda não tiver `vinculado_a` — exatamente a falha original.
- **Não foi preciso alterar** `roteador_modelos.py`/`roteador-modelos.js` (selados, CODEOWNERS): o hook é novo e separado.
- **Verificação:** `tests/test_experimentos_ativos.py` (15 testes) e 8 mutantes mortos; teste de fumaça do hook real (`node`) com o Plan da SPEC-008: nega sem cláusula, nega sem hash na rodada 3, libera com ambos, libera outra Spec e agente não construtor.

## 3. Correção do baseline do experimento
O baseline registrado em `DHR-EXPERIMENTO-PARADA-001` usou os números das notificações do harness, **não reproduzíveis** e muito menores que o consumo real. Com a telemetria corrigida (`DHR-TELEMETRIA-002`), consumo real do Plan da SPEC-008 até a R2 (tokens NOVOS = in + out + cache criado; cache lido à parte; tempo ATIVO, intervalos > 30 min não contam):

| Etapa | Tokens novos | Cache lido | Tempo |
|---|---|---|---|
| Plan v1.0 (Especificador) | 989.947 | 19.709.151 | 66 min ativos |
| Revisão R1 do Plan | 258.937 | 6.280.855 | 6 min ativos |
| Correção R1→R2 + decisões F-1..F-4 (Especificador) | 5.700.916 | 19.920.690 | 338 min ativos |
| Revisão R2 do Plan | 276.350 | 4.404.895 | 7 min ativos |

A correção R1→R2 do Especificador consumiu **5,7 milhões** de tokens novos e 338 min ativos (janela de 8.768 min): inclui retomada após limite de uso (o contexto é recriado a cada retomada) e três ordens sucessivas. O custo de **retomar** um agente é material (insumo para a retrospectiva).

## 4. O que esta ata NÃO afirma
- Não altera `AGENTS.md`, `.claude/agents/*`, ROADMAP, `atomic-spec.md` nem decisões abertas (CONS-01); a retrospectiva da SPEC-008 decide se a regra vira norma.
- O hook é trava de forma: não julga se a revisão é boa, nem decide por Andraus. A rodada é contada pelos pareceres existentes (`PARECER*PLAN-Rn` na linha "SPEC-nnn PLAN"); parecer fora desse padrão de nome não é contado.
- A conta de "Menores não abrem rodada" (regra 1 do P10) segue sendo decisão do Orquestrador a cada parecer; o hook garante cláusula, hash e teto, não o mérito.

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4 · BL-026 · P-13 · localização da confluência fractal · DN-1. **Nenhuma decisão aberta é fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] Ordem de Andraus (chat 2026-11-14) · [x] registro + hook + CI + testes · [x] `MECANISMOS.json` · [x] CATALOGO · [x] RPSA · [ ] merge (PR, CI verde — assinatura)

---

**Andraus** — *ordem dada no chat, 2026-11-14; registro pelo Orquestrador.*
