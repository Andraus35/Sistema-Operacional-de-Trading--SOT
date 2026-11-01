# PAUTA DE DECISÕES DE ANDRAUS — uma página, uma sessão (A3; DHR-A3-001)

> **Documento vivo, NÃO normativo.** Só reúne o que depende de Andraus, com a recomendação do Orquestrador marcada. Não decide, não homologa, não fecha decisão aberta (CONS-01). Cada pedido responde em uma palavra (**aprovar · recusar · adiar**); a decisão dele vira ata curta (`MODELO-ATA-OPERACIONAL-CURTA.md`) ou ata completa (se normativa). Estado de **2026-11-01** (conferido ao vivo; o PR #157 já foi mesclado por Andraus às 14:55); em divergência, valem o `ROADMAP.md` e o `RMR-001`. **Validade (A3, regra 2):** pedido sem decisão volta ao topo com a *recomendação padrão* — vencimento no `HANDOFF.md` (`[PRAZO]`, detector HO-10).

## A. Para decidir
| # | Pedido | Classe | Recomendação |
|---|---|---|---|
| 1 | Texto da regra "classes de decisão" (operacional × normativa) no `AGENTS.md` §10 (A3, regra 1) — reservado | normativa | **Aprovar que o Orquestrador só REDIJA** a proposta de texto; a aplicação é dele |
| 2 | `RPSA_AUTO_ENABLED=true` (A2): o workflow grava direto na `main`, fora de "PR é o meio" | operacional, com risco | **Adiar** até ele aceitar (ou recusar) essa exceção |
| 3 | Promover os `ATIVADOS` BL-003 e BL-011 e os 4 "disparados sem registro" (BL-010, 015, 017, 035) | normativa | **Adiar**: cada um precisa de proposta própria |
| 4 | **A5-O1 (Revisor e Especificador) e A10 APLICADOS** (`DHR-A5O1-001` e `DHR-A5O1-002`, ordens de Andraus 2026-11-01). **Resta (decidir):** (b) **A5-O4** — medir quanto o Especificador realmente lê do `RMR-001` (118 KB); (c) **A5-O2/O3** — cortar o ROADMAP (adiar até medir e até ele revisar l.34/37) | operacional (b) / normativa (c) | **(b) aprovar a medição** · **(c) adiar** |
| 5 | A8 = BL-047 (modelo fixo por agente) | normativa | **Adiar** até medir não-inferioridade |
| 6 | Pendências de Spec: erratum F2 da SPEC-020 (registrado PENDENTE no BL-017, `DHR-SPEC020-003`), `CATALOGO`/RMR-001, `CONFLICT-MAP`, status do `ERRATUM-SPEC019-001` (NÃO CONFIRMADO) | normativa | **Adiar** (exigem julgamento dele) |
| 7 | Higiene de nomes em `reference/` e subpastas de `governance/` (B7, B9) | normativa, risco médio-alto | **Adiar**: só com script e prova de referências |

## B. Esperando evento (nada a decidir agora)
P10 (experimento da regra de parada) — no **próximo Plan** que ele mandar abrir. **BL-043** (F2b do log dos Construtores, auditoria do código da F2a, decisões (e)/(g)/(l)) e **BL-044..047** — voltam quando a **SPEC-008** abrir. Mecanismo de assinatura antes de BUILD (`DHR-SPEC007-007`).

## C. Fora desta pauta (decisões abertas do ROADMAP — NÃO tocadas)
J-001 (reduzido) · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03.

## D. Já decidido (ponteiros; histórico curto)
higiene pós-arquivamento e errata da SPEC-007 (PR #157) · A5-O1 em `revisor.md` e `especificador.md` e arquivo de `revisao-independente/` (`DHR-A5O1-001/002`) · Auditor Externo **arquivado** (`DHR-AUDITOR-EXTERNO-019`) · A6.1/A6.4, A2.1 e P11 na `main` · A7-lite, A4-b e A9-teste (`DHR-A7A4-001`, `DHR-A9TESTE-001`) · log dos Construtores F2a (`DHR-LOGS-AC-001`) e pendências baratas (PR #161) · A6.2 medido e reformulado.
