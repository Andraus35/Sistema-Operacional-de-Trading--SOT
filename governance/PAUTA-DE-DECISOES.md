# PAUTA DE DECISÕES DE ANDRAUS — uma página, uma sessão (A3; DHR-A3-001)

> **Documento vivo, NÃO normativo.** Só reúne o que depende de Andraus, com a recomendação do Orquestrador marcada. Não decide, não homologa, não fecha decisão aberta (CONS-01). Cada pedido responde em uma palavra (**aprovar · recusar · adiar**); a decisão dele vira ata curta (`MODELO-ATA-OPERACIONAL-CURTA.md`) ou ata completa (se normativa). Estado de **2026-11-01** (conferido ao vivo; o PR #157 já foi mesclado por Andraus às 14:55); em divergência, valem o `ROADMAP.md` e o `RMR-001`. **Validade (A3, regra 2):** pedido sem decisão volta ao topo com a *recomendação padrão* — vencimento no handoff do ramo (`handoffs/ccr-a79e19ef-2zl738.md`; `[PRAZO]`, detector HO-10).

## A. Para decidir
| # | Pedido | Classe | Recomendação |
|---|---|---|---|
| 1 | Texto da regra "classes de decisão" (operacional × normativa) no `AGENTS.md` §10 (A3, regra 1) — reservado | normativa | **Aprovar que o Orquestrador só REDIJA** a proposta de texto; a aplicação é dele |
| 2 | `RPSA_AUTO_ENABLED=true` (A2): o workflow grava direto na `main`, fora de "PR é o meio" | operacional, com risco | **Adiar** até ele aceitar (ou recusar) essa exceção |
| 3 | Promover os `ATIVADOS` BL-003 e BL-011 e os 4 "disparados sem registro" (BL-010, 015, 017, 035) | normativa | **Adiar**: cada um precisa de proposta própria. **BL-003 e BL-011 analisados** (`ANALISE-BL-003-BL-011-ATIVADOS-2026-11-01.md`): já ativados por Andraus e tratados na SPEC-006 (Disposição PARCIAL); recomendação = **manter `ATIVADO`**, sem ação até a SPEC-009. Os 4 "disparados sem registro" seguem sem análise |
| 4 | **A5-O1 (os dois agentes), A10 e A5-O4 FEITOS** (`DHR-A5O1-001/002`; medição em `PROPOSTA-A5` §5, ordem de Andraus 2026-11-01). **Achado da medição:** em 9 agentes, **nenhum leu `RMR-001`, `ROADMAP`, `atomic-spec` ou `RULES` inteiros** (Grep + trechos; o `CATALOGO` nunca foi aberto): a economia esperada de cortar o ROADMAP é **incerta** e a "leitura obrigatória" não é cumprida literalmente (Revisor declara Passo 0 parcial). **Resta (decidir):** (b) o que fazer com esse descumprimento — **flexibilizar o texto** (leitura dirigida por Grep/âncora, pedido normativo em `.claude/agents/*`) ou **manter e cobrar**; (c) A5-O2/O3 (cortar o ROADMAP) | normativa | **(b) aprovar que eu só REDIJA** a proposta de texto da leitura dirigida (sem aplicar); **(c) adiar** até medir a abertura de uma Spec HIGH (`BL-044`) |
| 4b | **RESOLVIDO pelo PR #170 (`check_refs` ERRO 2→0).** Antes: `check_refs` com 2 ERROs na `main`** (4 documentos ainda citam o `LEDGER-ACHADOS.md`, agora gerado e fora do git desde o PR #164). **Proposta pré-testada:** acrescentar o caminho à lista `GENERATED_LOCAL` de `scripts/check_refs.py` (1 linha; **script selado** → regravar o selo + ata completa) → ERRO 2→0, WARN 3→1 (`PROPOSTA-REFS-LEDGER-GERADO-2026-11-01.md`). Alternativa B (editar os documentos) exigiria erratum de baseline | operacional com selo (ordem expressa) | **Aprovar a opção A** |
| 5 | A8 = BL-047 (modelo fixo por agente) | normativa | **Adiar** até medir não-inferioridade |
| 6 | Pendências de Spec: erratum F2 da SPEC-020 (registrado PENDENTE no BL-017, `DHR-SPEC020-003`), `CATALOGO`/RMR-001, `CONFLICT-MAP`, status do `ERRATUM-SPEC019-001` (NÃO CONFIRMADO) | normativa | **Adiar** (exigem julgamento dele) |
| 7 | Higiene de nomes em `reference/` e subpastas de `governance/` (B7, B9) | normativa, risco médio-alto | **Adiar**: só com script e prova de referências |
| 8 | A2.3: tags git por handoff no lugar das cópias (`PROPOSTA-A2-3-TAGS-DE-HANDOFF-2026-11-01.md`) | operacional, risco médio | **Recusar tags** (clone raso quebra o HO-04). O utilitário `novo_handoff` **já está PRÉ-TESTADO** (8 testes; 4/5 mutantes mortos, 1 equivalente; `EQUIVALENCIA/A2/novo_handoff/`), **não instalado** — **aprovar** instalar (entra com `MECANISMOS.json`, COE-14) ou adiar |

## B. Esperando evento (nada a decidir agora)
P10 (experimento da regra de parada) — no **próximo Plan** que ele mandar abrir. **BL-043** (F2b do log dos Construtores, auditoria do código da F2a, decisões (e)/(g)/(l)) e **BL-044..047** — voltam quando a **SPEC-008** abrir. Mecanismo de assinatura antes de BUILD (`DHR-SPEC007-007`).

## C. Decisões abertas do ROADMAP — quadro com bloqueio e prazo por evento (2026-11-17; `PROPOSTAS-REPO-BOAS-PRATICAS-2026-11-17.md` H3)
> **NÃO tocadas nem fechadas** (CONS-01): o quadro só organiza. O estado vive no `ROADMAP.md` ("Decisões abertas ativas"), que prevalece. "Prazo" = evento, não data; `[a confirmar]` = o Orquestrador não achou o enunciado exato no repositório e não o inventa.

| ID | O que decide | Bloqueia / vence quando | Recomendação do Orquestrador |
|---|---|---|---|
| J-001 | Fórmula, pesos e limiares **definitivos** do Conviction Vector (dimensionalidade 8 e limiares-piloto já fechados) | Fim da fase piloto: precisa de backtest (dona do backtest = BL-032) | **Adiar** até haver backtest; nada a fazer na fase spec-first |
| N-001 | Pesos por ativo do Conviction Vector | Junto com J-001 | **Adiar** com J-001 |
| M-001 | Estados de objeto não-hipótese no quadro (Blackboard) — SPEC-004 / SPEC-009 | **Antes de abrir a SPEC-009** (e referenciada pelo Plan da SPEC-008) | **Decidir** na abertura da SPEC-009, com o Dossiê |
| G-001 | Estado cognitivo e persistência — o ROADMAP diz que a SPEC-009 o resolve | **Antes de abrir a SPEC-009** | **Decidir** na abertura da SPEC-009 |
| K-001 | Ciclo de aprendizado de estratégia — o ROADMAP diz que a SPEC-018 o resolve | **Antes de abrir a SPEC-018** | **Adiar** até a SPEC-018 |
| SPEC-015-SCOPE | Escopo detalhado da SPEC-015 (Manager — Fase 0) | **Antes de abrir a SPEC-015** | **Decidir** na abertura da SPEC-015 |
| SPEC-045-RUNTIME-001 | Caminho de leitura em runtime → baseline na SPEC-045 | **Antes de abrir a SPEC-045** | **Adiar** até a SPEC-045 |
| ECC-03-001 | Escopo da RULE-ECC-03 ("modelo de especialização"; RULE-ECC-03 RESERVADA) | Ao precisar da RULE-ECC-03 numa abertura de Spec | **Adiar** |
| WF-D03 | Relação convicção-macro × convicção-global com o Conviction Vector 8D (resíduo de WORKFLOW-SOT-001) | **Antes do Plan da SPEC-014** (Manager — Fase 2) | **Decidir** junto com J-001 na abertura da SPEC-014 |
| C-001 | `[a confirmar]` — enunciado não localizado no ROADMAP/CATALOGO vigentes | Não determinado | **Pedir a Andraus** o enunciado ou o fechamento formal |
| D-PCC-4 | Promover `check_handoff.py` de informativo a bloqueante (PCC-001) | Quando houver evidência de ruído baixo | **Adiar**; aplicar a regra H2 (medir antes de promover) |

## D. Já decidido (ponteiros; histórico curto)
higiene pós-arquivamento e errata da SPEC-007 (PR #157) · A5-O1 em `revisor.md` e `especificador.md` e arquivo de `revisao-independente/` (`DHR-A5O1-001/002`) · Auditor Externo **arquivado** (`DHR-AUDITOR-EXTERNO-019`) · A6.1/A6.4, A2.1 e P11 na `main` · A7-lite, A4-b e A9-teste (`DHR-A7A4-001`, `DHR-A9TESTE-001`) · log dos Construtores F2a (`DHR-LOGS-AC-001`) e pendências baratas (PR #161) · A6.2 medido e reformulado.
· **Proteção da `main` LIGADA por Andraus (2026-11-17, rodou `proteger_main.sh --aplicar` no Termux; conferida pelo próprio script):** CI obrigatório (`Validate SOT Harness`, branch em dia), PR obrigatório, revisão de Code Owners, `enforce_admins=false`, sem force-push nem exclusão. Efeito: PR que toca arquivo selado só mescla por bypass de admin (o autor não aprova o próprio PR). Configuração do GitHub, fora do repositório; desfazer = `gh api -X DELETE repos/<dono>/<repo>/branches/main/protection`.
