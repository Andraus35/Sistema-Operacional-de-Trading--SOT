# MINUTA — Ata de vigência do registro de mecanismos (`governance/MECANISMOS.json`)

> **[PROPOSTA] — minuta preparada pelo Orquestrador a pedido de Andraus (chat, 2026-10-18). NÃO é ata, NÃO torna o registro vigente.** Só vale com a decisão de Andraus registrada no chat e citada na ata final (AGENTS.md §10). Prazo do lembrete: **2026-10-24** (HANDOFF §10). Número sugerido da ata: `DHR-COESAO-005`.

## 1. O que a decisão faria
Mudar `status_do_registro` de `PROPOSTA` para `VIGENTE` e trocar o texto de `aviso`. Nada mais: o registro continua **dado de estado, não autoridade** (não homologa nada nem fecha decisão aberta — CONS-01); o detector COE-14 continua acusando divergência com a realidade; a realidade prevalece sobre o registro.

## 2. Estado do registro (conferido em 2026-10-18)
| Estado | Qtde | Exemplos |
|---|---|---|
| ativo | 37 | hooks de sessão, gates, detectores, `gate_extra`, `spec_delta`, `roteador_modelos`, `check_branches` |
| legado | 6 | `gate-check` no pre-commit (retirado), `.eslintrc`/`.prettierrc` (marcadores de sensor), 3 skills arquivadas |
| inerte-em-nuvem | 2 | `revisor-guard` (exit 2 não honrado em SubagentHandback), `revisor_gate_mcp` (servidor inline não carrega em pasta não confiável) |
| pausado | 2 | `route_aex`, `auditor-externo.yml` (DHR-AUDITOR-EXTERNO-007) |
| proposta | 1 | `.pre-commit-config.yaml` (só vale após `pre-commit install`) |
| **Total** | **48** | `check_coesao`: ERRO=0 WARN=0 INFO=5 |

## 3. Ressalvas honestas a ler antes de assinar
- **Verificação ao vivo feita em 2026-10-18** (pedida por Andraus): dos 36 itens que estavam `inferido-do-codigo`, **34** foram exercitados (hooks com payload real/vazio, gates e detectores com exit 0 e saída conferida, testes de unidade no CI, acionamento observado nesta sessão) e têm `verificado_em` atualizado; **2** seguem sem exercício ao vivo: `wf.auditor-externo` (pausado) e `cfg.pre-commit` (só vale após `pre-commit install`). Os `skill.*` legados e `cfg.eslintrc/prettierrc` foram só conferidos por existência/validade. "VIGENTE" significa *registro de referência aceito, com evidência por item*; o limite de cada verificação está escrito no próprio `verificado_em` (ex.: `post-edit-check` só provado fail-open, sem teste de conteúdo).
- Os 2 itens `inerte-em-nuvem` e os 2 `pausado` são honestamente classificados; assinar não os reativa.
- Escopo do registro: quem cria/altera um mecanismo atualiza o registro no mesmo PR (COE-14 acusa omissão ou item órfão).

## 4. Mudança prevista (se Andraus assinar)
`governance/MECANISMOS.json`: `"status_do_registro": "VIGENTE"`; `"aviso": "VIGENTE desde <data> (DHR-COESAO-005, decisão de Andraus). Dado de estado, não autoridade: não homologa nem fecha decisão aberta (CONS-01). Em divergência com a realidade, a realidade prevalece; o detector COE-14 acusa a divergência."`; `AGENTS.md` §8 (nota "PROPOSTA até Andraus assinar") passa a "VIGENTE" — **arquivo protegido, exige a ordem expressa de Andraus**; `HANDOFF` remove o lembrete `[PRAZO]`; RPSA `nao`.

## 5. Opções de Andraus
(a) **Assinar agora** (recomendado, com as ressalvas do §3 aceitas) · (b) adiar além de 24/10 (o lembrete reagenda) · (c) revisar item a item antes.
