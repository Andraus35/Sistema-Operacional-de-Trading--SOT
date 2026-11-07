# Proposta — Handoff: ponto de entrada, formato do ID e ciclo de vida (nada aplicado)

> **Não normativo. PROPOSTA — NADA APLICADO.** Pedido de Andraus (chat, 2026-11-06: "proposta de regra do handoff"). O `AGENTS.md` §11 é arquivo reservado: qualquer texto abaixo só vale com ordem expressa dele e ata. Não fecha decisão aberta (CONS-01). Contexto: `PROPOSTA-CONCORRENCIA-DE-SESSOES-2026-11-01.md` (Camada A).

## 1. O problema, medido na `origin/main` em 2026-11-06
| # | Fato | Onde se vê |
|---|---|---|
| 1 | O `HANDOFF.md` da raiz é o HO-2026-11-01-163 do ramo `ccr-a79e19ef-2zl738` (logs, pauta, medições A5). Ele **não menciona** a frente de concorrência nem os handoffs por ramo | `HANDOFF.md` |
| 2 | Existe `handoffs/<ramo>.md` (PR #159), mas só 2 arquivos, ambos de ramos **já mesclados e apagados**: `ccr-4bd4e8a0-d92lc7.md` (HO-152) e `ccr-b7c09dc1-y4rafd.md` (HO-157) | `handoffs/` |
| 3 | O `check_handoff` e o hook só leem `handoffs/<ramo>.md` quando o nome do ramo **atual** é igual; sessão nova com ramo novo cai na raiz e não vê esses arquivos | `scripts/check_handoff.py` (`handoff_rel`) |
| 4 | `AGENTS.md` §11 e a `PAUTA-DE-DECISOES.md` **não citam** `handoffs/<ramo>.md` nem o formato do ID | `AGENTS.md`, `governance/PAUTA-DE-DECISOES.md` |
| 5 | **Colisão de ID vigente:** `docs/handoffs/HO-2026-11-01-157.md` (ramo `ccr-a79e19ef-2zl738`) e `handoffs/ccr-b7c09dc1-y4rafd.md` (HO-2026-11-01-157, outro conteúdo) | `git show origin/main:...` |
| 6 | `docs/handoffs/` tem ~157 arquivos e 7 pastas `ramo-<ramo>/` criadas à mão; IDs HO-148, 149 e 150 colidiram entre sessões | `docs/handoffs/` |

**Causa:** o mecanismo (código) existe, mas as **regras de uso** não foram escritas: não está definido qual arquivo é a entrada, como numerar e o que fazer com o handoff quando o ramo morre.

## 2. Regras propostas
**R1 — Entrada de uma sessão nova.** O `HANDOFF.md` da raiz vira **índice curto e estável** (≤40 linhas): (a) o passo "Reverificar ao vivo" comum; (b) uma tabela "frentes ativas" com o caminho de cada `handoffs/<ramo>.md`; (c) ponteiro para a `PAUTA-DE-DECISOES.md`. O estado detalhado de cada frente fica **só** em `handoffs/<ramo>.md`. Quem abre ramo novo cria o próprio arquivo.
**R2 — ID.** `HO-<AAAA-MM-DD>-<ramo curto>-<n>`, com `ramo curto` = os 7 primeiros caracteres depois de `ccr-` e `n` contado por ramo. Único por construção (ramo é único). IDs antigos permanecem como estão (INV-07).
**R3 — Ciclo de vida.** Enquanto o ramo existe: `handoffs/<ramo>.md` é o handoff vivo. No merge do PR do ramo, o arquivo final é **movido** para `docs/handoffs/ramo-<ramo>/` (cópia exata, INV-07) e sai de `handoffs/`. A tabela de frentes ativas da raiz perde a linha.
**R4 — Quem escreve.** Só o Orquestrador da frente escreve o próprio `handoffs/<ramo>.md`. O índice da raiz só recebe linha nova/removida (conflito trivial de uma linha) ou, melhor, passa a ser **gerado** (ver §4).
**R5 — Sem DHR sem ata.** Mantém HO-06: o handoff não cita DHR cuja ata ainda não está na `main`.

## 3. Texto candidato para `AGENTS.md` §11 (arquivo reservado; NÃO aplicar sem ordem)
> - Cada ramo tem **seu** handoff em `handoffs/<ramo>.md`, com ID `HO-<data>-<ramo curto>-<n>`; o `HANDOFF.md` da raiz é só o índice das frentes ativas e o roteiro "Reverificar ao vivo". Antes de agir, ler o índice e o handoff da frente.
> - Ao mesclar o PR do ramo, mover seu handoff final para `docs/handoffs/ramo-<ramo>/` (INV-07).
> - *[texto anterior preservado — INV-07: "Antes de agir, o Orquestrador lê `HANDOFF.md` e executa sua seção 'Reverificar ao vivo'…"]*

## 4. Mecanismos que isto exigiria (propostos, não instalados; cada um com ordem de Andraus e `MECANISMOS.json`, COE-14)
- **M1 `check_handoff` HO-16 (Detector, informativo):** `handoffs/<ramo>.md` cujo ramo não existe no remoto → "arquivar em `docs/handoffs/ramo-<ramo>/`". Hoje acusaria os 2 arquivos mortos.
- **M2 `check_handoff` HO-17 (Detector):** ID fora do formato R2 em arquivo **novo**; IDs antigos isentos.
- **M3 índice gerado** (`handoffs/INDEX.md`, não versionado, gerado no SessionStart): lista cada `handoffs/*.md` com id, ramo, data e linha de "Frente atual". Evita editar a raiz. **Atenção:** o `build_map` indexa arquivos do disco; um índice local mudaria o resumo do mapa (lição do ledger) — precisa ficar fora do que o mapa indexa ou ser gerado só em memória.
Nada disto é necessário para R1–R3 funcionarem: eles funcionam só com disciplina e o mecanismo já na `main`.

## 5. Pré-teste proposto (antes de aplicar qualquer coisa)
1. Clone isolado: rodar o `check_handoff` com (a) raiz-índice + 2 `handoffs/*.md` vivos, (b) arquivo de ramo morto, (c) ID no formato novo e no antigo. Esperado: ERRO=0; HO-16 só no caso (b).
2. Dois ramos novos, cada um criando só o próprio `handoffs/<ramo>.md` e uma linha na tabela da raiz, mesclados: esperado 0 conflito (a linha da tabela é a única superfície compartilhada).
3. Teste de unidade para HO-16/HO-17 com mutantes (aceitar tudo; recusar tudo).

## 6. Limites e riscos
- A raiz como índice **ainda é um arquivo compartilhado** (1 linha por frente). Só a geração (M3) o elimina. Aceitável no início.
- Não verifiquei como o hook do SessionStart se comporta em ramo novo na prática além de ler o código; vale testar no pré-teste.
- Migrar o conteúdo atual do `HANDOFF.md` da raiz (HO-163, frente de logs/pauta) para `handoffs/ccr-a79e19ef-2zl738.md` mexe no trabalho de outra sessão: combinar antes.

## 7. Decisões que cabem a Andraus
1. Aprovar R1–R5 como direção (sim / ajustar / adiar). 2. Autorizar o pré-teste da §5. 3. Autorizar o texto da §3 no `AGENTS.md` §11 (ata). 4. Decidir M1–M3 só depois do pré-teste.
