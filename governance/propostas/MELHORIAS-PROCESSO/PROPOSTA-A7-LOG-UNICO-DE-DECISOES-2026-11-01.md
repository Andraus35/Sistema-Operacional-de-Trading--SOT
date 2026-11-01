# Proposta A7 — Log único de decisões operacionais (medida antes de cortar)

> **Não normativo. PROPOSTA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A7. Frente escolhida por Andraus; próximo item após A2, A3 e A6. Mexer em `AGENTS.md` (§10), detectores ou atas exige ordem dele. Não fecha decisão aberta (CONS-01).

## 1. Medição ao vivo (HEAD `5a55ffd`)
| Item | Auditoria (24–31/10) | Hoje |
|---|---|---|
| Atas `governance/DHR-*.md` | 148 | **159** (8.222 linhas; mediana 48; mínima 24; máxima 156) |
| Com `RPSA-escopo: sim` (mudam agente) | — | 14 |
| Passam um filtro fraco de "não homologa Spec/baseline e sem RPSA-escopo" | "muitas" | **43** (1.943 linhas; mediana 37) |
| Dessas 43, operacionais **por leitura do título** | — | **≈ 8** (ex.: `CHECKS-INFO-001`, `MERGE-001`, `COESAO-004`, `TELEMETRIA-CUSTO-001`, `BACKLOG-001`, `DOCSYNC-003`, `RPSA-002`, `PCC-003`) |
| Ritmo de atas novas | — | 58 atas em 7 dias de registro entre 17 e 31/10 (pico de **17 em um dia**, 15 em 31/10); 1 em 01/11 |

**Leitura.** O filtro fraco superestima: a maior parte das 43 altera `AGENTS.md`, `.claude/agents/*` ou mecanismo selado (ex.: `AGENTS-CORTES`, `ROTEAMENTO-004..007`, `LOOP-001`, `AUDITOR-EXTERNO-*`), que o `AGENTS.md §10` reserva a decisão expressa de Andraus — e continuariam exigindo ata completa. O universo realmente "operacional puro" é ≈ 8 atas ≈ 240 linhas, **~3 % do volume**. O histórico não se apaga (INV-07), então o ganho é só para atas **futuras**.

## 2. O que dependeria de arquivo `DHR-*` (risco de trocar ata por log)
- `AGENTS.md §10`: assinatura = "decisão registrada no chat **e citada na ata**" → o log teria de contar como "ata" (emenda a arquivo reservado).
- `check_handoff` **HO-06**: DHR citada precisa ter ata em `governance/` **ou** constar do texto do CATALOGO — o log só funcionaria se cada linha entrasse no CATALOGO ou se o detector fosse alterado (script selado).
- `check_rpsa` **R1**: toda DHR do livro-razão precisa existir como arquivo; itens com `RPSA-escopo: sim` ficariam fora do log por construção.
- `check_coesao` **COE-11/COE-14** e o mapa (`build_map`) indexam as atas; log novo = documento novo a indexar.
- Rastreabilidade por busca (`DHR-ID` → arquivo) usada por `ROADMAP`, `CATALOGO` e pareceres.

## 3. Opções
| Opção | O que é | Ganho medido | Risco/custo |
|---|---|---|---|
| **A7-log** (a da auditoria) | `governance/DECISOES-LOG.md`, 1 linha por decisão operacional; ata completa só para baseline/norma/decisão aberta/arquivo reservado. Um checker garantiria: ordem de Andraus citada, commit existente, **nenhum arquivo reservado** na linha | ≈ 240 linhas históricas equivalentes (~3 %); futuro: só as atas puramente operacionais | Alto para o ganho: emenda ao `AGENTS §10` (reservado), mudança em `check_handoff` (selado), novo detector e registro (COE-14), risco de classificar errado e deixar decisão relevante sem ata |
| **A7-lite** | Modelo de **ata operacional curta** (≤ 15 linhas: ordem citada, arquivos, verificação), no mesmo `DHR-*.md` | Mediana 37 → ~15 linhas nessas atas (≈ 22 linhas por ata) | Baixo: nenhum detector muda; mantém HO-06, RPSA, COE e o mapa. Só texto de orientação (onde? `AGENTS.md` é reservado → ou um modelo em `governance/`) |
| **Não fazer** | Manter como está | 0 | Custo de atas curtas continua ≈ 24–30 linhas; sem risco novo |

## 4. Recomendação
**A7-lite ou nada.** O A7-log troca ~3 % de volume por três mudanças em arquivo reservado/selado e um classificador de "o que é operacional" que pode errar contra o §10. A medição não sustenta esse custo. Se Andraus quiser algo, o modelo curto (sem mecanismo novo) captura a maior parte do ganho. Depende de ordem dele; nada foi criado.

## 5. Declarado
Contagens por `glob`/regex neste commit. "Operacional" por leitura de título (um avaliador, sem abrir as ~35 atas restantes); a heurística de 43 é deliberadamente larga. Não medi custo em tokens de escrever uma ata. A auditoria original citava 148 atas e "muitas" operacionais — este resultado a corrige para baixo.
