# Proposta A3 — Pauta única de decisões de Andraus (decisão em lote)

> **Não normativo. PROPOSTA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A3 ("o gargalo é a fila de decisões"). "Avançar" lido como seguir para o A3. Não decide por Andraus nem fecha decisão aberta (CONS-01). Recomendação do Orquestrador marcada; a decisão é dele.

## 1. Diagnóstico medido (2026-11-01)
Pedidos em aberto só de Andraus, lidos de `HANDOFF.md` §10, `backlog_triggers.py` e `ROADMAP.md`: **~20 itens** em 4 grupos (abaixo). Backlog: **2 ATIVADOS** (BL-003, BL-011) e **4 "disparados sem registro"** (BL-010, 015, 017, 035). Decisões abertas do ROADMAP: J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03 (nenhuma tocada aqui).

## 2. Pauta (um formulário por sessão: aprovar / recusar / adiar)
| # | Item | Classe | Recomendação do Orquestrador |
|---|---|---|---|
| 1 | Abrir PR do ramo `ccr-d7f01e4e-c5qpb1` (A2.1 e A6.4/A6.1 aplicados, propostas A2/A6/A3) — sem mesclar | operacional | **Aprovar** |
| 2 | Aplicar patches P11 (handoff por ramo, pré-testados) | operacional | **Aprovar** (4 mutantes mortos) |
| 3 | `RPSA_AUTO_ENABLED=true` | operacional, com risco | **Adiar:** o workflow faz commit direto na `main` com o token do GitHub, o que foge de "PR é o meio" (AGENTS §10). Antes: Andraus decidir se aceita essa exceção |
| 4 | Destino do Auditor Externo (A6.3): aposentar ou reativar | normativa | **Aposentar** (arquivar em `docs/_legacy/` com prova de conservação), pausado desde 2026-10-11 e lido por todo agente em AGENTS §9 |
| 5 | A6.2: contador "última vez que achou" nos detectores | operacional | **Aprovar** (só leitura, informativo) |
| 6 | A4 / A7 / A8 / A9 da auditoria (proporcionalidade, log de decisões, modelo fixo, checklist D/H) | normativa | **Adiar** até medir A1 na próxima Spec (P10) |
| 7 | Backlog: promover BL-003/011 e os 4 disparados | normativa | **Adiar:** não analisei item a item; cada um precisa de proposta própria |
| 8 | Pendências de Specs: erratum F2 da SPEC-020, errata da SPEC-007, CATALOGO/RMR-001, CONFLICT-MAP | normativa | **Adiar** (exigem julgamento; fora desta frente) |
| 9 | P10: experimento da regra de parada no próximo Plan | já aprovado | nada a decidir até ele mandar abrir Plan |

## 3. As duas regras de A3 (precisam de ordem dele para valer)
1. **Classes de decisão:** *operacional* (script, detector informativo, higiene não normativa) = Orquestrador decide e informa depois, **sempre citando a ordem de Andraus** (AGENTS §10 já permite o operacional que ele aprovou no chat); *normativa* = só Andraus. Mudar isso é mudar o `AGENTS.md` §10, arquivo reservado: **não proponho texto nem aplico**.
2. **Validade da proposta:** proposta sem decisão em 14 dias reaparece na pauta com a recomendação padrão explícita. Já existe parecido (P12, prazo-teto de 14 dias na retomada); reaproveitaria o `[PRAZO: AAAA-MM-DD]` do handoff (HO-10).

## 4. Declarado
A pauta mede quantidade, não esforço. A classe de cada item é minha leitura; item 3 e 4 são os de maior efeito e maior risco. Não verifiquei se o workflow `rpsa-auto` consegue empurrar para a `main` com a proteção de branch atual.
