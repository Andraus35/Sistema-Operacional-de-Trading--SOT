# Proposta — Concorrência de sessões: fim dos conflitos de docs, ramos, PRs e merges

> **Não normativo. PROPOSTA — NADA APLICADO.** Pedido de Andraus (chat, 2026-11-01): diagnosticar e recomendar solução definitiva. Aplicar qualquer item exige ordem expressa dele (AGENTS.md §10). Não fecha decisão aberta (CONS-01).

## 1. Diagnóstico (medido em 2026-11-01)

| Fato | Medida | Fonte |
|---|---|---|
| Arquivos únicos tocados por toda sessão | `MAPA-PROJETO.md` 214 · `mapa-projeto.json` 198 · `HANDOFF.md` 124 · `rpsa-ledger.json` 38 · `MECANISMOS.json` 34 · `LEDGER-ACHADOS.md` 27 alterações em 30 dias | `git log origin/main --since=30.days --name-only` |
| Numeração sequencial do handoff colide | HO-110..127 repetidos; 5 pastas `docs/handoffs/ramo-*/` (30 arquivos) preservadas à mão | `docs/handoffs/` |
| Carga paralela | 16 merges em 2026-10-31, de 5 ramos `ccr-*`; 40 PRs recentes, todos mesclados, nenhum descartado | PRs #116–#156 |
| Ramos parados | 9 de 17 sem commit há 7–34 dias, 120–276 commits atrás da `main` (alguns com commits próprios: 1–175 à frente) | `git rev-list --count` |
| PR aberta atrasada | #155 está 34 commits atrás da `main` | `list_pull_requests` |
| Conflito resolvido à mão | 6 commits "Merge origin/main" em 30 dias | `git log` |
| Controles atuais só avisam | `branches-hook`, `merge_ready`, `check_handoff` HO-04 (aviso "esperado") | `governance/MECANISMOS.json` |
| Proteção da `main` | **NÃO VERIFICADO** (a sessão não lê as configurações do GitHub). O próprio `CODEOWNERS` diz que o bloqueio depende de "Require review from Code Owners", que é configuração do repositório | `.github/CODEOWNERS` |

**Causa-raiz:** o desenho tem estado compartilhado mutável (um `HANDOFF.md`, um mapa commitado, livros-razão únicos, contador sequencial) e nenhuma serialização no servidor. Cada sessão nova gera conflito por construção; os avisos locais não impedem.

## 2. Solução em 3 camadas

### Camada B — Serialização no servidor (aplicar primeiro; reversível; só configuração)
Checklist para Andraus em *Settings → Branches/Rules → `main`*:
1. Exigir PR (sem push direto) e CI `Validate SOT Harness` aprovado.
2. Exigir "branch up to date before merging".
3. Exigir "Code Owners review" (ativa o `CODEOWNERS` existente).
4. Ligar **Merge queue**: cada PR é testado contra a `main` já atualizada.
5. Ligar "Automatically delete head branches".
6. Ressalva: o workflow `rpsa-auto.yml` faz `git push origin HEAD:main` com `GITHUB_TOKEN`; com "exigir PR" ligado ele precisa de exceção (bypass do `github-actions`) ou passa a abrir PR. Conferir antes de ligar.

### Camada A — Eliminar o estado compartilhado (causa-raiz)
| Hoje | Proposto | Efeito |
|---|---|---|
| `HANDOFF.md` único + HO sequencial | `handoffs/<ramo>.md` por ramo; ID `HO-<data>-<ramo curto>-<n>` | colisão impossível; some `ramo-*/` |
| `docs/mapa/*` commitado (500+ toques/30d) | gerado e ignorado (`.gitignore`); CI e hooks seguem usando `build_map.py` | some o hotspot nº 1 |
| Livros-razão/ledgers append-only | um fragmento por sessão em `*.d/`, consolidado por script; onde restar arquivo único, `.gitattributes merge=union` | append concorrente não conflita |

Mudanças de código implicadas: `check_handoff.py`, `handoff-hook.js`, `check_branches.py`, `check_coesao.py` (COE-12 lê `HANDOFF.md`), `build_map.py --check` no CI/pre-commit, `loop_ledger.py`, `rpsa_auto.py`. Nenhuma é implementada aqui.

### Camada C — Posse explícita (lock leve)
- Ao iniciar, a sessão declara a frente (Spec/pasta) em PR de rascunho ou em `locks/<frente>`.
- `SessionStart` **falha** (não só avisa) se outro ramo aberto toca a mesma Spec ou caminho normativo; saída: falar com Andraus.
- Regra operacional: 1 sessão = 1 PR pequeno; `git merge origin/main` ao começar e antes de cada push.

## 3. Pré-teste (cópia isolada, `git` real)
Três sessões acrescentando linhas ao mesmo registro e criando um fragmento cada:
- **com `merge=union`:** `ledger.log` = `a s1 s2 s3`, 0 conflitos, `git status` limpo;
- **fragmentos por sessão:** 3 arquivos distintos, 0 conflitos;
- **contra-prova (sem union):** o mesmo append concorrente dá `Automatic merge failed`.
Não testados (dependem do GitHub): merge queue, regras da `main`, bypass do `rpsa-auto`.

## 4. Limites e riscos
- `merge=union` serve só para texto append-only; **não** usar em JSON (`rpsa-ledger.json`, `MECANISMOS.json`) — por isso o fragmento por sessão.
- Tirar o mapa do Git muda o contrato do BL-019 e do AGENTS.md §5 ("`--check` bloqueia"): exige ata de Andraus.
- Ramos antigos: triagem individual antes de apagar (têm commits que a `main` não tem). Esta proposta não apaga nada.
- Economicidade: a Camada B custa minutos; a A é a de maior retorno (remove ~60% dos toques em arquivos compartilhados); a C é a de maior atrito — adiar até A e B estarem de pé.

## 5. Ordem sugerida (por ordem expressa de Andraus)
1. Camada B (configuração, minutos). 2. Camada A: handoff por ramo, depois mapa, depois ledgers. 3. Triagem dos 9 ramos antigos. 4. Camada C.
