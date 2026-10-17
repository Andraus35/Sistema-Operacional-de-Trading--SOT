# DHR-AGENTES-001 — Ata — Separação nominal dos agentes de Construção e dos agentes de Trading

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "Separar agentes de criação do projeto dos agentes de Trading para não confundir"; opção escolhida: "Nomenclatura + índices")**. O merge desta ata por Andraus é a ratificação. Altera `AGENTS.md` (§2 mapa, §3) e `GLOSSARIO.md` (nova §1-bis). Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07): nenhuma regra, arquivo ou nome existente removido ou movido; reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta classificação e vocabulário (famílias AC/AT) em AGENTS.md/GLOSSARIO.md; não altera `especificador.md`, `revisor.md`, checklist, método nem regra. |

## 1. Origem `[FATO]`
O repositório usa "agente" para dois grupos: quem **constrói** o SOT (Orquestrador, Especificador, Revisor, `sot-*`, Auditor Externo) e quem **opera mercado** (Elliott, SMC, Fibonacci, ICT, Manager, Risk). Havia colisões de vocabulário: "Orchestrator" (legado de runtime, hoje Manager Agent) × Orquestrador (sessão de construção); `specs/*.spec.md` (spec de agente de trading) × `specs/features/` (Specs numeradas de construção); "Trilha A/B" (sequenciamento) lido como se fosse a divisão construção/trading; `AGENTS.md` §3 listava só os agentes de construção sob o título genérico "Agentes".

## 2. O que muda `[FATO]`
1. **Nomes canônicos:** *Agentes de Construção (AC)* e *Agentes de Trading (AT)*.
2. `GLOSSARIO.md` §1-bis (nova) define as famílias e cinco regras de leitura; a antiga §2 passa a dizer "agentes de trading" no título (conteúdo intacto).
3. `AGENTS.md` §3 reorganizada em 3.1 (AC), 3.2 (AT), 3.3 (fronteira); §2 (mapa) rotula `specs/*.spec.md` como specs de agentes de trading e `.claude/agents/` como construção.
4. `docs/agentes/INDICE-AGENTES.md` (não-normativo): tabelas AC e AT, armadilhas de vocabulário, regras de fronteira.
5. **Não** move arquivos, **não** renomeia agentes, **não** altera CI, scripts, hashes do gate nem os frontmatters.

## 3. Fora de escopo (decisão explícita)
Separação física em pastas (mover `specs/*.spec.md`, `rag/`, `schemas/`) — **não adotada** nesta ata (impacto em citações, CI, lint, `check_refs` e selo do gate); reavaliável por nova decisão de Andraus. Etiqueta de domínio no gerador do mapa (`scripts/build_map.py`) — não implementada (altera código).

## 4. Reversão `[PROPOSTA]`
`git revert` do commit desta ata restaura `AGENTS.md` e `GLOSSARIO.md`; o índice em `docs/agentes/` pode ser arquivado em `docs/_legacy/` (INV-07).

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · H-001 · K-001 · C-001 · M-001 · N-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001 · RULE-REG-001 · SPEC-020-PRINC-001 (conforme `ROADMAP.md`, que prevalece). **Nenhuma fechada por este ato.**

## 6. Registro
- [x] Esta ata · [x] `AGENTS.md` · [x] `GLOSSARIO.md` · [x] `docs/agentes/INDICE-AGENTES.md` · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *escolha em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge.*
