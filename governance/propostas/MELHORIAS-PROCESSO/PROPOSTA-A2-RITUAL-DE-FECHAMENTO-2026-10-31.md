# Proposta A2 — Ritual de fechamento manual (medida antes de cortar)

> **Não normativo. PROPOSTA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A2. Escolhida por Andraus (chat, 2026-10-31) como primeiro item da frente. Aplicar exige ordem dele (INV-07, PCC-001, RPSA). Não fecha decisão aberta (CONS-01). Regra dos 4Es: medir antes de cortar.

## 1. Medição ao vivo (main `a62b95e`)

| Item da auditoria | Medido hoje | Leitura |
|---|---|---|
| Cópias em `docs/handoffs/` | 131 entradas, 2,0 MB | cresce 1 arquivo por entrega |
| `HANDOFF.md` | 62 linhas (teto 150, HO-05) | já está curto; "≤40 linhas" rende pouco |
| Commits (sem merge) que tocam `HANDOFF.md` | 65 de 211 | ritual real |
| Commits que tocam `mapa-projeto.json` | 126 de 211 (1,66 MB) | **maior churn do repositório** |
| Commits que tocam `rpsa-ledger.json` | 29 | já automatizado (ver 2.2) |
| Tags git | 0 | não há hoje substituto para a cópia |

## 2. Achado por sub-item

**2.1 Mapa fora da árvore (`mapa-projeto.json`) — ganho alto, risco baixo.** É o maior ruído de diff. Consumidores a ajustar antes (lista conferida): `scripts/build_map.py`, `tests/test_build_map.py`, `tests/test-map-sync.js`, `.gitattributes`, `.rgignore`, `.clinerules/sot-map.md`, `AGENTS.md` §5 (hooks/CI/pre-commit usam `build_map --check`). O `MAPA-PROJETO.md` (120 KB) continua versionado (leitura humana). Gate de CI passa a gerar o `.json` como artefato e `--check` compara só o `.md`.

**2.2 RPSA "derivado do git" — NÃO recomendado como está na auditoria.** A premissa está parcialmente desatualizada: `rpsa_auto.py` + `rpsa-auto.yml` (DHR-RPSA-002) já registram a classificação após o merge; o workflow está **inerte** até Andraus definir `RPSA_AUTO_ENABLED=true`. E o carimbo não é um hash: `em_escopo` e `sync` são **julgamento** (EUA-E16 §4.1) declarado na ata. Derivar do hash do último commit tocaria arquivos monitorados mas apagaria esse julgamento (a DHR-X mexeu em `governance/` e não é escopo dos agentes). Alternativa de menor risco: **só ligar o que já existe** (`RPSA_AUTO_ENABLED`), decisão operacional dele, medindo se o ritual manual some.

**2.3 Handoff com tag em vez de cópia — ganho médio, risco médio.** Troca 131 arquivos por tags `HO-<id>`. Exige: `check_handoff` HO-04 passar a verificar "tag existe e aponta commit cujo `HANDOFF.md` é o substituído"; tags precisam ser empurradas (verificar se o proxy deste ambiente e o fluxo de PR as aceitam — **não testado**, hoje há 0 tags); migração das 131 cópias existentes para `docs/_legacy/` (INV-07: nada deletado). Interage com o P11 (cadeias por ramo): com tags, colisão de número entre ramos viraria colisão de tag — precisa de regra própria. **Recomendo adiar 2.3 até o P11 ser aplicado**, para não desenhar duas vezes.

**2.4 Ata curta em tabela única** — depende do A7; fora deste item.

## 3. Ordem sugerida (cada passo só por ordem de Andraus)

1. **2.1** mapa `.json` fora da árvore (pré-teste: `build_map --check` e `test_build_map` em cópia isolada; patch não aplicado em `EQUIVALENCIA/A2/`).
2. **2.2** Andraus decide ligar `RPSA_AUTO_ENABLED` (nenhum código novo).
3. **P11** (já pré-testado) e depois **2.3**.

## 4. Perguntas a Andraus
- Autoriza eu pré-testar o **2.1** (patch em cópia isolada, sem aplicar)?
- Concorda em **não** derivar o RPSA do hash e, em vez disso, avaliar ligar `RPSA_AUTO_ENABLED`?
- **2.3** fica depois do P11?

## 5. Declarado
Não rodei a suíte nem testei empurrar tags; números vêm de `git log`, `wc`, `du` e `grep` desta sessão. Contagem da auditoria (98/233 commits no mapa) difere da atual (126/211): metodologia distinta (esta exclui merges e conta o `.json`); a tendência é a mesma.
