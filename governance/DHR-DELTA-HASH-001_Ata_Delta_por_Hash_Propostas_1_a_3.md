# DHR-DELTA-HASH-001 — Ata de Decisão — Delta por hash: pacote gravado, SHA256-ALVO no pedido e instrumentação do ledger

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Revisor SOT / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31): "Aplique as propostas 1 a 3 do delta por hash" · `DHR-REVISOR-DELTA-001` · `governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-HIGIENE-E-ECONOMICIDADE-2026-10-31.md` |
| Data | 2026-10-31 |
| Status | **DECISÃO REGISTRADA** (ordem direta em chat; AGENTS.md §10). Toca `.claude/agents/revisor.md` **por ordem expressa dele**. Aditiva (INV-07); reversível por `git revert`. |
| Compatibilidade | Minor (acrescenta ao §3-bis; não altera o Passo 5-bis, o teto de veredito nem o gate determinístico). |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Acrescenta ao `revisor.md` §3-bis item 7 a origem do `sha256` (entregue pelo Orquestrador) e o formato de cabeçalho do parecer. |

## 1. Decisões `[FATO]`
| # | Proposta | O que passou a valer |
|---|---|---|
| 1 | Orquestrador sempre gera e **grava** o delta | `scripts/delta_pacote.py <plan.md> --base <ref> --out <pasta do parecer>` grava `DELTA-*.txt` (blocos alterados/adicionados/removidos, `SHA256-ALVO`, `SHA256-BASE`, fontes com sha256) e imprime as linhas do pedido. Reaproveita `spec_delta.py` (selado) sem alterá-lo. Mecanismo `util.delta-pacote` em `MECANISMOS.json`; teste em CI. |
| 2 | `SHA256-ALVO` no prompt do Revisor | O Revisor (sem Bash) declara o valor recebido no cabeçalho do parecer (`MODO:`, `SHA256-ALVO:`); sem a linha, escreve `não recebido` — nunca estima (revisor.md §3-bis item 7). |
| 3 | Ledger registra modo, hash e tokens | `loop_ledger.py` seção **2-ter**: modo (delta/integral/inferido/n-d), SHA256-ALVO declarado e `TOKENS:` (n/m quando o ambiente não informa). Linha de base: 0 de 32 rodadas com hash declarado. |

## 2. Ressalvas `[FATO]`
- **Não instituído:** o hook R-AC7 (`roteador_modelos.py`, selado) **não** passou a exigir `SHA256-ALVO`/`DELTA:`; a prática é do Orquestrador e a cobrança é do ledger (Detector). Exigir no hook é decisão e selo próprios.
- A proposta 4 da auditoria (cobrar tabela por bloco) **não** foi aplicada.
- O modo inferido por palavra-chave é indicativo (a convenção `MODO:` prevalece). Tokens nunca são estimados.
- Nenhuma decisão aberta foi fechada (CONS-01); regra de equilíbrio dos 4Es mantida (nenhum corte de leitura do Revisor: só origem do hash e registro).

## 3. Registro
- [x] Esta ata · [x] `scripts/delta_pacote.py` + `tests/test_delta_pacote.py` · [x] `revisor.md` §3-bis.7 · [x] `MECANISMOS.json` · [x] CI · [x] `loop_ledger.py` 2-ter · [ ] merge (assinatura)
