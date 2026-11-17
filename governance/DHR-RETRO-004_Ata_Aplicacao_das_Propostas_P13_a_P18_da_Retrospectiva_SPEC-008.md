# DHR-RETRO-004 — Ata de Decisão — Aplicação das propostas P13–P18 da retrospectiva da SPEC-008

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordem de Andraus (AskUserQuestion, 2026-11-17: "Aplicar propostas P13–P18") · `AGENTS.md` §10 e §12 passo 5 · `governance/propostas/MELHORIAS-PROCESSO/PROPOSTAS-RETRO-SPEC-008-2026-11-15.md` · `DHR-AVALIACAO-002` · `DHR-RETRO-002` |
| Data | 2026-11-17 |
| Status | **APLICADA por ordem de Andraus; assinatura = merge do PR.** Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Detectores e geradores informativos do Orquestrador, experimento de processo e regravação de selo de dois scripts de gate; não altera agente, Spec nem canon. |

## 1. Decisão de Andraus `[FATO]`
Andraus respondeu **"Aplicar propostas P13–P18"** à pergunta do Orquestrador sobre o próximo passo após a SPEC-008. A ordem de aplicação seguiu a sugerida na proposta (`[INFERÊNCIA]` do Orquestrador): P16 e P14(b) primeiro, depois P13 e P15, P17, P18.

## 2. O que foi aplicado `[FATO]` (tudo informativo; nenhum bloqueio novo)
| Proposta | Aplicação | Arquivo | Teste |
|---|---|---|---|
| P13 | modo `--blocos` (fato → blocos do Plan por tipo; `--exigir` destaca quem não traz a alínea nova) | `scripts/fato_locais.py` | `tests/test_fato_locais.py` |
| P14(a) | âncora `ID#hhhh` (hash curto do bloco, o de `spec_delta.py`) — `hash` e `conferir` | `scripts/ancora_hash.py` (novo) | `tests/test_ancora_hash.py` |
| P14(b) | tabela "texto anterior" do HISTORICO.md gerada do diff | `scripts/historico_do_diff.py` (novo) | `tests/test_historico_do_diff.py` |
| P15 | fração de blocos alterados no pacote do delta; > 50% ⇒ dividir a correção em duas entregas (`--strict` reprova); `SHA256-ALVO` da rodada 2 em diante em todo Plan novo, pelo veículo já existente | `scripts/delta_pacote.py`; experimento `P15-REVISAO-DO-DELTA` em `governance/EXPERIMENTOS-ATIVOS.json` (escopo "próximo Plan", após 2026-11-15) | `tests/test_delta_pacote.py` |
| P16 | confere a tabela D5 contra cenários/ADV (linha, evento, código; alcançabilidade; ciclos; efeito sem falha; cobertura) + convenção de tabela | `scripts/fsm_check.py` (novo); `governance/propostas/MELHORIAS-PROCESSO/CONVENCAO-TABELA-FSM.md` | `tests/test_fsm_check.py` |
| P17(b) | todo cenário cita pré-condição/fixture declarada | `scripts/cenario_precondicao.py` (novo) | `tests/test_cenario_precondicao.py` |
| P17(c) | `contagens_declaradas` ignora aproximação/estimativa e número de seção (**arquivo selado**) | `scripts/gate_extra.py` | `tests/test_gate_extra.py` (3 testes novos) |
| P18 | `pre_entrega.py` passa a compor `fsm_check` e `cenario_precondicao` como detectores informativos (**arquivo selado**) | `scripts/pre_entrega.py` | `tests/test_pre_entrega.py` |

P17(a) já é coberto por P14(b), como a própria proposta previa. Registro: `governance/MECANISMOS.json` no mesmo PR (COE-14).

## 3. Arquivos selados `[FATO]`
`scripts/gate_extra.py` e `scripts/pre_entrega.py` estão em `GATE-MANIFEST.sha256` e em `CODEOWNERS`: o selo foi **regravado** (`python scripts/gate_manifest.py --write`; `--check` = íntegro). A mudança nos dois é pequena e aditiva (P17(c): uma função auxiliar e um `continue`; P18: dois itens no lote de detectores informativos). Cabe ao dono em CODEOWNERS revisar esse diff antes do merge.

## 4. Limites e pendências `[FATO]`
- **Não feito (decisão à parte):** integrar a âncora `ID#hhhh` ao `check_refs.py` (selado, bloqueante no CI) e avisar citação por linha em Plan novo — P14(a) entrega o detector separado; **P18** ficou sem a "checklist D/H legível por máquina" (BL-046/A9) por não existir ainda: só compõe P16/P17(b). **P13** não entra no `pre_entrega` (exige o ID do fato como entrada).
- `fsm_check` acha texto e estrutura; não entende guarda semântica. `cenario_precondicao` acha nomes. Falso positivo é esperado (informativo).
- O experimento `P15-REVISAO-DO-DELTA` passa a negar, pelo hook, o pedido ao Revisor sobre o próximo Plan sem `EXPERIMENTO: P15-REVISAO-DO-DELTA` e, da rodada 2, sem `SHA256-ALVO`. Encerrar = ata + registro.
- Medição de ganho: a primeira Spec que usar os detectores vira a evidência para a retrospectiva seguinte (taxa de Médias C10/C06/C03 por rodada).

## 5. Registro
- [x] Esta ata · [x] scripts + testes · [x] `MECANISMOS.json` · [x] selo regravado · [x] experimento registrado · [ ] merge (assinatura de Andraus)
