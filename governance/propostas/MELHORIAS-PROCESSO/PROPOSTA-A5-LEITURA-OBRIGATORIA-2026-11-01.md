# Proposta A5 — Leitura obrigatória inflada: medir de novo e cortar só o que prova ser cortável

> **Não normativo. PROPOSTA MEDIDA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A5 e `AUDITORIA-HIGIENE-E-ECONOMICIDADE-2026-10-31.md` (H1–H8). Pedido: nº 4 da `PAUTA-DE-DECISOES.md` (Andraus, AskUserQuestion 2026-11-01). Não decide por Andraus nem fecha decisão aberta (CONS-01). Tokens = **bytes ÷ 4 (estimativa)**; economia por chamada é **INFERÊNCIA**.

## 1. Medido hoje (2026-11-01, `main` em `ef35441`)
| Arquivo | Bytes | Tokens ≈ | Quem lê |
|---|---|---|---|
| `AGENTS.md` | 18.821 | 4,7 mil | toda sessão e subagente |
| `ROADMAP.md` | 79.991 | 20,0 mil | núcleo obrigatório (Especificador e Revisor) |
| `atomic-spec.md` | 39.999 | 10,0 mil | núcleo obrigatório |
| `governance/RULES.md` | 52.751 | 13,2 mil | núcleo do Especificador (`especificador.md` l.97) |
| `backlog/RMR-001_Painel_Backlog.md` | 118.285 | 29,6 mil | checar `ATIVADO` (a leitura **integral** é dispensável; o gate é `backlog_triggers.py`) |
| `governance/CATALOGO-OFICIAL.md` | 100.135 | 25,0 mil | `required_sources` dos dois agentes |
| definição do agente | 40.819 (Esp.) / 50.951 (Rev.) | 10,2 / 12,7 mil | cada chamada |
**Núcleo de abertura** (AGENTS + ROADMAP + atomic-spec + agente) ≈ **45–47 mil tokens por chamada** — bate com a estimativa de 47–49 mil da auditoria, já **descontando o corte do `AGENTS.md`** (29,4 → 18,8 KB, ≈ −2,7 mil). O Especificador soma ainda `RULES.md` (≈ +13 mil).
**ROADMAP por seção:** "Estado atual do ciclo" = **17.695 B (22%, ≈ 4,4 mil tokens)** — é log de homologações, a maior célula tem **9.549 caracteres** (l.37, "Decisões FECHADAS"); "26. Capacidades" = 8.767 B (10%); 11 marcas "preservado" (era 12).
**Custo real por chamada** (campo `subagent_tokens` das notificações de conclusão desta sessão, **n = 7, amostra pequena e de uma só frente**): Especificador 62 mil · 95 mil · 127 mil · 149 mil; Revisor 86 mil · 143 mil · 152 mil. A abertura (≈ 45–60 mil) seria **~35–70% de cada chamada** — **[INFERÊNCIA]**: não há medição que separe abertura de trabalho.
**Limite da medição:** o hook de telemetria gravou **0 tokens em 10/10 chamadas** desta sessão, porque os agentes rodaram em segundo plano e o payload do `PostToolUse` desses lançamentos traz só `agentId`/`status`/`outputFile`, sem `usage`. Por isso a "telemetria por Spec vazia" (BL-047) tem causa conhecida; medir exige rodar a rodada em primeiro plano ou ler o `usage` da notificação.

## 2. O que já foi feito desde a auditoria (H1–H8)
**H2 feito** (§7 do `AGENTS.md` → arquivo morto, `DHR-AGENTS-SEC7-001`). **H3 em parte** (AGENTS 6 → 2 marcas; ROADMAP 12 → 11). **H4 NÃO feito:** `revisor.md` l.148 (Short-circuit) ainda manda comparar o carimbo com "a última linha de DHR do `CATALOGO-OFICIAL.md`" (100 KB ≈ 25 mil tokens), mas o carimbo é conferido contra `governance/rpsa-ledger.json` por `check_rpsa.py`. **H1 e H8 NÃO feitos.**

## 3. Opções (todas pedem ordem dele; nenhuma aplicada)
| # | Opção | Toca | Ganho (estimativa) | Risco / prova exigida | Recomendação |
|---|---|---|---|---|---|
| O1 | **H4:** trocar na l.148 de `revisor.md` "última DHR do CATALOGO" por "`python scripts/check_rpsa.py` / `rpsa-ledger.json`" (1 linha) | `.claude/agents/revisor.md` (**reservado**) | evita até ≈ 25 mil tokens **se** o Revisor lê o catálogo para isso (não medido) | baixíssimo; o RPSA/`test_rpsa` cobrem o carimbo | **Aprovar** |
| O2 | **ROADMAP:** mover o histórico de "Estado atual do ciclo" (17,7 KB) para `docs/_legacy/` (arquivo + hash por seção, INV-07) e deixar só o estado atual por linha | `ROADMAP.md` (**reservado**; l.34/37 exigem julgamento dele) | ≈ 3–4 mil tokens/chamada que lê o ROADMAP | médio: exige script de equivalência (hash por seção) e A/B como o do `AGENTS.md` (`TESTE-AB-AGENTS`) | **Adiar** até ele revisar l.34/37; pedir o script de equivalência antes |
| O3 | **H1:** "fatia quente" do ROADMAP gerada por script (cabeçalho + sequência + decisões + Spec em foco) | muda a regra de leitura em `AGENTS.md` §1 | ≈ 10–14 mil tokens/chamada | **alto:** esconder decisão aberta de uma Spec em revisão (4Es: Economicidade nunca acima de Eficácia) | **Adiar** até haver medição de tokens por rodada (BL-036/047) |
| O4 | `RMR-001` (118 KB): dispensar a leitura integral em favor de `backlog_triggers.py` também para o Especificador em MEDIUM/HIGH | `especificador.md` (**reservado**) | até ≈ 29 mil tokens se hoje se lê inteiro (não medido) | baixo: o gate já é determinístico | **Aprovar uma medição** (quanto o Especificador realmente lê) antes de propor texto |

## 4. Recomendação do Orquestrador
**Aprovar O1** (1 linha, risco mínimo) e **uma medição** de O4 e da abertura real (rodada em primeiro plano com `usage`); **adiar O2 e O3**. Declaro: não verifiquei se o Revisor de fato abre o `CATALOGO-OFICIAL.md` hoje; o ganho de O1 pode ser zero.
