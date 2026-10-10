# DHR-AUDITOR-EXTERNO-005 — Ata — Roteamento determinístico de achados do Auditor Externo em duas faixas (Opção B)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-10 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-10: "Opção B")**; implementação em validação (ver `OPERACAO.md` §10). Não altera o Revisor, o ROADMAP, o método nem decisão aberta. |
| Compatibilidade | n/a (aditiva — INV-07) |
| Regime | Piloto controlado do Auditor Externo; o auditor segue subordinado ao Orquestrador (DIR-002). |

## 1. Decisão de Andraus `[FATO: chat, 2026-10-10]`
Entre (A) canal único manual pelo Orquestrador, (B) roteamento em **duas faixas** e (C) achados direto ao Especificador, Andraus escolheu a **Opção B**. A Opção C **não** foi adotada: texto de modelo externo não vira instrução para um agente com Write/Edit sobre as Specs.

## 2. Desenho `[INFERÊNCIA do orquestrador]`
- `scripts/route_aex.py` (determinístico, fail-closed, sem LLM) classifica cada achado **já validado** em `rapida` ou `andraus` usando só campos de máquina (`severity`, `type`, `proposal.type`, `modifies_baselined_text`, `treats_open_decision_as_closed`, `open_decisions_referenced`, `proposal.touches`). O texto livre do auditor não influencia a rota.
- Faixa rápida = P2 · `drift` · `ERRATUM_ADITIVO` · sem texto baselined · sem decisão aberta · alvos apenas em `governance/CATALOGO-OFICIAL.md`. Qualquer dúvida, ausência ou falha ⇒ `andraus`.
- Rótulos `aex-rota-rapida` / `aex-rota-andraus`, linha de rota no comentário da Issue e no aviso do PR. Testes em CI (bloqueante).
- Faixa rápida **não** mescla nada: gera, no máximo, tarefa limitada ao Especificador → PR → Revisor → **Andraus mescla**. O encaminhamento automático pela rotina do Orquestrador só será ligado **depois** da validação ao vivo (V3–V7), a pedido de Andraus.
- Fora do manifesto do bot (`scripts/` e workflow): a VM **não** precisa de nova aprovação.

## 3. Limites `[FATO/INFERÊNCIA]`
Allowlist inicial mínima (um arquivo); ampliar exige nova ata. O validador garante forma e citação literal, **não mérito**: um achado errado na faixa rápida ainda passa pelo Revisor e por Andraus. Roteamento ao vivo, fluxo por PR, despertar da sessão e `fechamento` ainda **não** foram exercitados (ver `OPERACAO.md` §10). Modos de falha da VM e custo do plano ChatGPT seguem sem medição.

## 4. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
Fora de escopo dos agentes (EUA-E16 §4.1): muda a operação do piloto, não checklist, método nem regra. Registrada em `rpsa-ledger.json` como `em_escopo=false`, `sync=fonte-unica`.

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 6. Registro
- [x] Esta ata · [x] `scripts/route_aex.py` + `tests/test_route_aex.py` · [x] workflow (`achado`) · [x] CI · [x] `OPERACAO.md` §9–10 · [x] `rpsa-ledger.json` · [x] `CATALOGO-OFICIAL.md` · [x] mapa

---

**Andraus** — *decisão direta em chat, 2026-10-10 ("Opção B"); registro feito pelo Orquestrador interno a pedido de Andraus.*
