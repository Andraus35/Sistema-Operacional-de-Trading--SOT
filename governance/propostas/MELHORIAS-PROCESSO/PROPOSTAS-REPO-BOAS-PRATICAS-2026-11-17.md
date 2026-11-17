# Propostas de boas práticas para o repositório e o projeto (2026-11-17)

> **PROPOSTAS, NÃO NORMATIVAS.** Nascem das respostas de Andraus ao questionário automatizado do Orquestrador (AskUserQuestion, 2026-11-17, após o merge do PR #196). **Nada é aplicado:** cada item só vira mecanismo por ordem expressa dele, com `governance/MECANISMOS.json` no mesmo PR (COE-14) e ata completa se tocar arquivo selado. Formato: problema → evidência → proposta → 4Es → custo.

## H1 — Higiene do repositório (resposta: "Redigir proposta de limpeza")
- **Problema:** um clone novo reprova o `check_refs` (ERRO=4) porque `AGENTS.md`, `.clinerules/sot-map.md` e dois documentos citam `docs/mapa/MAPA-PROJETO.md`, arquivo gerado e não versionado (DHR-MAPA-GERADO-001); sobram ramos remotos já mesclados e handoffs de frentes encerradas em `handoffs/`.
- **Evidência:** `check_refs.py` na `main` limpa; `check_branches.py` = BR-02 `ccr-7dbcb1d1-e5d5dd` contido na `main`; `handoffs/` com 5 arquivos de ramos anteriores (`ccr-7dbcb1d1`, `a79e19ef`, `b7c09dc1`, `bb493467`, `c64455fe`).
- **Proposta:** (a) acrescentar `docs/mapa/MAPA-PROJETO.md` à lista `GENERATED_LOCAL` de `scripts/check_refs.py` (mesmo padrão já usado para o ledger no PR #170; **arquivo selado** ⇒ ata completa + selo regravado); (b) apagar o ramo remoto contido na `main`; (c) mover para `docs/handoffs/ramo-<ramo>/` os handoffs de frentes que terminaram, conforme AGENTS.md §11 — cada um só depois de Andraus confirmar que a frente acabou.
- **4Es:** Conformidade ↑ (gate verde em clone novo), Eficiência ↑. **Custo:** pequeno; (a) é uma linha mas selada.

## H2 — Regra de promoção de detector a bloqueante (resposta: "Medir na próxima Spec")
- **Problema:** `fsm_check`, `cenario_precondicao`, `ancora_hash` e `fato_locais --blocos` (DHR-RETRO-004) são informativos; sem critério, a promoção vira opinião.
- **Proposta:** na próxima Spec que usar o pré-gate, o Orquestrador registra por rodada, no parecer ou no ledger, (i) achados do detector, (ii) quantos eram falso positivo, (iii) quantas Médias C10/C06/C03/C07 o Revisor ainda achou que o detector não pegou. Critério **sugerido** (a Andraus ajustar): promover só com falso positivo < 10% **e** ao menos 1 Média real prevenida em duas Specs; caso contrário seguir informativo. A promoção é decisão de Andraus (ENF-03), com ata.
- **Evidência de partida:** `contagens_declaradas` teve 2 falsos positivos num Plan (P17(c)); `cenario_precondicao` deu 1 achado plausível (`H7`) no Plan da SPEC-008; `fsm_check` 0 achados (i)/(ii).
- **4Es:** Eficácia ↑ (promove com prova), Economicidade ↑ (evita bloqueio ruidoso). **Custo:** baixo (medição manual até haver script).

## H3 — Decisões abertas com dono e prazo (resposta: "Pauta com dono e prazo")
- **Problema:** 11 decisões abertas sem data nem condição de vencimento; algumas bloqueiam Specs futuras e só aparecem quando a Spec abre.
- **Proposta:** quadro na seção C de `governance/PAUTA-DE-DECISOES.md` (feito neste PR; é documento vivo não normativo) com, por decisão: o que decide, o que bloqueia, recomendação do Orquestrador e **prazo por evento** ("antes de abrir SPEC-xxx"), não por data de calendário, porque a abertura de Spec é decidida por Andraus. Nenhuma decisão é fechada ou reescrita (CONS-01); o ROADMAP prevalece.
- **4Es:** Eficácia ↑ (nenhuma Spec abre sem saber o que depende de decisão). **Custo:** baixo.

## Próxima frente escolhida por Andraus
Errata aditiva das 4 condições do Plan da SPEC-008 (R3-m04/m05/m07/m08) — **em PR separado, em sequência** (DHR-UM-RAMO-UM-PR-001), só depois do merge deste.
