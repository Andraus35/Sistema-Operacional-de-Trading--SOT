# Auditoria profunda — higiene de leitura e economicidade (4Es) do repositório

> **Não normativo. PROPOSTA/RELATÓRIO** (AGENTS.md §12 passo 5). Nada aqui foi aplicado. Não fecha nem abre decisão (CONS-01). Pedido de Andraus (chat, 2026-10-31). Base: `main` em `bd6679d`. Tokens = **bytes ÷ 4 (estimativa)**; tokens reais não são medidos pelo repositório (Economicidade = INDETERMINADO no ledger).

## 1. Resumo executivo
1. **Cada chamada de agente paga ~47–49 mil tokens só de leitura de abertura** (AGENTS.md + definição do agente + ROADMAP + atomic-spec), e o Revisor é um subagente novo a cada rodada. Nas erratas recentes (≈11 rodadas de Revisor) isso soma ~0,5 milhão de tokens só de abertura.
2. **O maior bloco único é o ROADMAP (78 KB ≈ 19,6 mil tokens)**, dos quais ~17 KB são "Estado atual do ciclo" e ~8 KB a lista de capacidades; a maior parte é de fases futuras irrelevantes para uma Spec em revisão.
3. **Mecanismos de economia foram desenhados mas não medem nem acionam**: leitura proporcional (EUA-E19), roteamento de modelo (revertido e reajustado várias vezes), telemetria da onda 0 (2 linhas), caching (SPEC-046/CACHE-ISS-001, só como Spec). Economicidade segue sem número.
4. **Há mecanismos inertes que ainda custam** (chamada ao gate MCP que não carrega em nuvem, workflow pausado, CI que roda detectores informativos lentos).
5. **Nomes enganam** (17 emendas homologadas ainda chamadas `_PROPOSTA`) e texto histórico fica embutido nos arquivos quentes.

## 2. Leitura obrigatória por chamada (medido)
| Item | Bytes | Tokens ≈ | Quem lê |
|---|---|---|---|
| `AGENTS.md` | 29.427 | 7,4 mil | toda sessão e subagente |
| `ROADMAP.md` | 78.543 | 19,6 mil | Especificador e Revisor |
| `atomic-spec.md` | 39.999 | 10,0 mil | Especificador e Revisor |
| `especificador.md` | 41.127 | 10,3 mil | Especificador |
| `revisor.md` | 49.049 | 12,3 mil | Revisor |
| **Abertura Especificador** | | **≈ 47 mil** | |
| **Abertura Revisor** | | **≈ 49 mil** | |
| `WORKFLOW.md` (condicional) | 15.506 | 3,9 mil | quando a Spec toca o pipeline |
| `HANDOFF.md` | ~7,9 mil | 2,0 mil | Orquestrador |
Hooks de início de sessão injetam pouco (≈ 1 mil bytes). Não são o problema.

## 3. Oportunidades de higiene de leitura (ordenadas por ganho)
| # | Oportunidade | Ganho estimado | Quem decide | 4Es / risco |
|---|---|---|---|---|
| H1 | **Fatia quente do ROADMAP gerada por script** (cabeçalho + sequência + decisões abertas/fechadas + seção da Spec em foco), não-normativa como o mapa; o ROADMAP segue íntegro e prevalece | ~10–14 mil tokens por chamada (≈ 60–70% do ROADMAP) | Andraus (muda o que "leitura obrigatória" significa, AGENTS.md §1) | Eficiência ↑; risco Eficácia se a fatia omitir restrição → exige check de equivalência (hash por seção) |
| H2 | **AGENTS.md §7 (decisões):** 5,9 KB, boa parte histórico de decisões fechadas com "texto anterior preservado". Mover o histórico para arquivo e deixar só abertas + ponteiro | ~1,2–1,5 mil tokens em **toda** sessão e subagente | Andraus (AGENTS.md) | INV-07 permite arquivar (não apagar); ROADMAP já é a fonte do estado |
| H3 | **Marcas de texto superado inline** nos arquivos quentes (AGENTS 5, ROADMAP 6, especificador 3, revisor 2, atomic-spec 2): migrar para arquivo de histórico | ~1–3 mil tokens/chamada | Andraus | INV-07 cumprido por arquivo à parte com hash |
| H4 | **Ponteiro quebrado de economia:** `revisor.md` §Short-circuit manda comparar o carimbo com "última DHR do `CATALOGO-OFICIAL.md`" (95 KB ≈ 24 mil tokens), mas o carimbo agora é conferido contra `governance/rpsa-ledger.json` (`check_rpsa.py`) | evita abrir o CATALOGO inteiro; ~0–24 mil por rodada | Andraus (`.claude/agents/revisor.md`) | Corrigir C01 (contradição interna) |
| H5 | **`.rgignore`/`.ignore`** excluindo `docs/mapa/mapa-projeto.json` (1,29 MB), `docs/handoffs/` (1,28 MB, 97 arquivos), `docs/_legacy/`, `docs/UPGRADES/` das buscas Grep/Glob dos agentes | menos ruído e menos resultados irrelevantes por busca; nenhuma mudança normativa | Orquestrador (arquivo novo; checar whitelist de raiz HOD-001 §6b.1) | só Eficiência |
| H6 | **Status no nome:** 17 `EUA-E04..E19a_*_PROPOSTA.md` já HOMOLOGADAS induzem a ler/duvidar. Não renomear (referências por caminho); marcar o status na primeira linha ou no índice | evita releitura/dúvida | Andraus (governança) | C02 ambiguidade |
| H7 | **`governance/` com 210 arquivos (145 DHR):** para consulta de agente, índice por tópico já existe no mapa; reforçar o ponteiro "abrir só se o núcleo indicar" também no `especificador.md` | marginal | — | — |
| H8 | **`CATALOGO-OFICIAL.md` 95 KB:** 11 mil palavras; seções "Registro (data)" longas. Ler só pelo mapa/âncora; considerar fatia por estado (vigente/histórico) | só se algum agente o lê inteiro (H4) | Andraus | — |

## 4. Mecanismos obsoletos, desligados ou que custam sem entregar (Economicidade)
Fonte: `governance/MECANISMOS.json` (51: 40 ativos, 6 legados, 2 inertes em nuvem, 2 pausados, 1 proposta) + configuração real em `.claude/settings.json`, `.github/workflows/`.

| # | Item | Situação | Custo/problema | Recomendação (decisão de Andraus) |
|---|---|---|---|---|
| M1 | `mcp.revisor-gate` + `hook.revisor-guard` | **inertes em nuvem** (MCP inline não carrega; `exit 2` não é honrado em SubagentHandback) | o Revisor é instruído a chamar `revisor_gate` toda rodada e a chamada falha; G1/G2 "sempre pendentes" (retrospectiva, P8) | ou tornar o gate acessível ao Revisor (P8) ou **parar de instruir a chamada em nuvem** e mover a conferência ao Orquestrador (`revisor_gate.py` já roda via Bash) |
| M2 | `wf.auditor-externo` + `util.route-aex` + `tests/test_route_aex.py` + AGENTS.md §9 | **PAUSADO** desde 2026-10-11 | workflow roda e termina "skipped"; ~260 linhas + testes mantidos; §9 no AGENTS.md (leitura de toda sessão) | decidir destino (D-PCC-3 já em aberto): arquivar kit e reduzir §9 a uma linha, ou reativar |
| M3 | `cfg.pre-commit` (proposta), `hook.gate-check.precommit` (legado), `cfg.eslintrc`, `cfg.prettierrc` | nunca instalados / só marcadores de sensor do `harness-score` | arquivos de raiz sem uso real | manter só se o `harness-score` for usado; senão arquivar |
| M4 | **CI informativo caro:** 5 passos `continue-on-error` (`check_refs`, `backlog_triggers`, `check_doc_sync`, `check_handoff`, `check_invariants`); `check_invariants.py` levou >2 min localmente (varre o repo todo) | tempo de CI sem poder de bloqueio; os mesmos detectores já rodam em hooks | rodar `check_invariants` só nos `.md` alterados no PR, ou promover/arquivar cada detector |
| M5 | **Suíte:** 367 testes em ~71 s localmente; CI repete `actions/setup` e roda ~9 passos `unittest` separados | tempo | agrupar em um `unittest discover` |
| M6 | **9 hooks Stop/SubagentStop** em todo fim de turno (map-sync, doc-sync, handoff, ask-guard, revisor-posguarda, + 4 em SubagentStop) | cada um sobe Python/Node; o `doc-sync` emite o mesmo WARN em todo SessionStart (1 WARN permanente) | latência e tokens de aviso repetido | deduplicar aviso por commit (como o aviso do `merge_ready`) |
| M7 | `.agents/.skill-lock.json` | sem uso identificado | resíduo | verificar e arquivar |
| M8 | `docs/mapa/mapa-projeto.json` 1,29 MB versionado e regenerado a cada `.md` | cresce o diff de todo PR | ruído de PR (não de leitura) | manter só o `.md` no repositório e gerar o `.json` em CI, se nenhum script o exige (verificar) |

## 5. Ideias cogitadas e não levadas adiante, sob os 4Es
| Ideia | Origem | Estado real | Leitura 4Es |
|---|---|---|---|
| **Roteamento econômico de modelo (Revisor em modelo menor)** | EUA-E19 (2026-09-21) | Revisor revertido para `sonnet-5-5` (DHR-AUDITOR-EXTERNO-014); Especificador elevado a `opus-5-5` "sem teste prévio" (DHR-ROTEAMENTO-002); teste de não-inferioridade autorizado em ROTEAMENTO-001 | **sem resultado registrado**: Economicidade perdeu, sem medição que sustente |
| **Telemetria de tokens por rodada** | onda 0 (DHR-ROTEAMENTO-001) | `TELEMETRIA-ONDA0.md`: **2 linhas**, tokens `n/m` em uma | sem dado não há 4º E; a decisão de roteamento segue por opinião |
| **Leitura proporcional à complexidade (dial GES) e short-circuit RPSA** | EUA-E19 | descrito nos agentes; o AGENTS.md §1 continua exigindo ROADMAP+atomic-spec **integrais** | contradição prática: a regra existe e o requisito de abertura a anula |
| **Caching de contexto** | BL-024/BL-025, SPEC-046 (HOMOLOGADA) | só especificação; sem build (fase spec-first); o ganho de cache entre subagentes não é medido | candidato a ganho grande, mas só após BUILD |
| **Revisão por delta com hash** | DHR-REVISOR-DELTA-001, `spec_delta` | existe e foi usada; o Revisor ainda lê integral quando falta git/hash (retrospectiva) | melhorar com tamanho por rodada no ledger |
| **Dimensionamento de Spec** | RULE-ECC-07 (hoje) | só texto; check determinístico **não instituído** | ver proposta anterior |
| **`pre-commit`** | `cfg.pre-commit` | proposta nunca instalada | arquivar ou instalar |
| **Backlog:** 4 itens "disparados sem registro" (BL-010, BL-015, BL-017, BL-035) e 2 ATIVADOS sem encaminhamento (BL-003, BL-011) | `backlog_triggers.py` | aguardam Andraus | custo de atenção/leitura repetida em todo gate |
| Backlog "hygiene:próximo ciclo" (BL-005, BL-007) | RMR-001 | encerrados, mas o gatilho "próximo ciclo de higiene" nunca teve ciclo formal | esta auditoria pode servir de ciclo |

## 6. Proposta de ordem de ataque
1. **Medir antes de cortar (E1):** gravar no ledger tamanho do alvo e tokens por rodada (hoje `n/m`); sem isso H1–H3 não têm contrafactual. Sem custo normativo.
2. **Ganhos sem mudança normativa (Orquestrador):** H5 (`.rgignore`), M4/M5 (CI), M6 (aviso único), M8 (se nada lê o `.json`).
3. **Ganhos com ordem de Andraus (normativos):** H4 (ponteiro do `revisor.md`), H2/H3 (higiene de AGENTS.md e arquivos quentes), H1 (fatia quente do ROADMAP com check de equivalência), M1 (decisão sobre o gate do Revisor em nuvem), M2 (destino do Auditor Externo).
4. **Fechar com retrospectiva** no mesmo molde do LOOP-001 passo 5.

## 7. O que NÃO verifiquei
- Tokens reais: usei bytes÷4; o consumo real por chamada (cache de prompt, subagentes) não é medido.
- Se o agente realmente lê o ROADMAP inteiro quando a regra de leitura proporcional se aplica (li só o texto dos agentes, não rodadas reais).
- Se algum script lê `mapa-projeto.json` (M8) ou `.agents/` (M7).
- Conteúdo interno de `reference/` (1 MB), `docs/UPGRADES/` e `rag/` além do tamanho.
- Resultado do teste de não-inferioridade (se foi executado fora do repositório).
