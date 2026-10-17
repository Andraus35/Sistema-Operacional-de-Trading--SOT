# Auditoria de tarefas por criticidade e Dossiê de roteamento de modelos (camada meta) — PROPOSTA

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E24** (número a atribuir pelo Controlador; sucessora de EUA-E19, que ela não revoga — INV-07) |
| Status | **PROPOSTA — NÃO NORMATIVA.** Nada aqui altera `AGENTS.md`, `.claude/agents/*.md`, `governance/` normativo, `canon/`, `ROADMAP.md` ou `atomic-spec.md` (AGENTS §10: só por decisão expressa de Andraus). Não abre nem fecha decisão (CONS-01). |
| Origem | Pedido de Andraus (chat, 2026-10-17): lacuna de eficiência — Especificador em modelo caro, Revisor em modelo caro, tarefas simples/operacionais executadas por modelo caro; levantar por auditoria profunda os tipos de tarefa por criticidade, pesquisar estado da arte/benchmarks e aplicar o 4Es. |
| Autoria | Orquestrador (Claude Code), sessão `ccr-d43bf9b0-h336k5`, 2026-10-17 |
| Etiquetas | `[FATO]` verificado no repositório · `[EXTERNO]` dado de fonte web (nunca baseline, RULE-ECC / DHR-PROV-WEB-001) · `[INFERÊNCIA]` dedução minha, a testar · `[PROPOSTA]` recomendação · `[NÃO MEDIDO]` lacuna de dado |
| Princípio-guia | **Conformidade > Eficácia > Efetividade > Eficiência > Economicidade** (RULE-CEE-001). Nenhum roteamento abaixo é aceitável sem prova de não-regressão de Eficácia. Falsa economia (modelo barato que exige reexecução) é perda, não ganho (CEE-001 §12). |

---

## 1. Resumo executivo

**Diagnóstico em uma frase:** o SOT roteia modelo **por papel** (Especificador = Opus 4.8; Revisor = Sonnet 5.5), nunca **por tarefa**, e não mede custo nem eficácia por tarefa; por isso toda tarefa — de redigir uma emenda constitucional a copiar um arquivo de handoff — passa pelo mesmo agente, mesmo prompt (~10 mil tokens) e mesma leitura obrigatória (~55–110 mil tokens).

**Sete achados principais** (detalhe em §3.4):

1. **Não existe tabela de roteamento por tarefa na camada meta.** A EUA-E19 roteou *dois papéis*; a RULE-CEE-002 roteia por tipo cognitivo, mas só na trading (runtime ORYX, ainda spec-only) e sem versões de modelo. `[FATO]`
2. **A premissa de plataforma da EUA-E19 §1 caducou.** Ela afirmou que o frontmatter de subagente "não tem campo de esforço de raciocínio". A documentação atual lista `effort` (`low…max`) no frontmatter, `effort` por invocação e `model` por invocação. O "esforço médio" do Especificador e o "esforço alto" do Revisor hoje **não são aplicados por configuração** — são texto de conduta. `[FATO]` + `[EXTERNO]`
3. **O Especificador está num modelo mais caro e mais antigo que o disponível.** Opus 4.8 custa US$5/US$25 por MTok; Opus 5.5 custa US$4/US$20 (−20%), com cache lido a 0,05× em vez de 0,1×. Se Opus 5.5 é igual ou melhor no trabalho do Especificador é **[NÃO MEDIDO]** — mas o único teste de gerações do repositório (DHR-014) mostrou que a geração do modelo pesou muito mais que o método. `[EXTERNO]` + `[FATO]`
4. **Dois subagentes não declaram `model`** (`sot-spec-reviewer`, `sot-schema-validator`) e herdam o modelo da sessão — hoje o mais caro disponível. Um deles (`sot-schema-validator`) duplica o que `npm test` já faz sem LLM. `[FATO]`
5. **A Eficácia da economia anterior foi medida e falhou:** o roteamento econômico da EUA-E19 (Revisor em Sonnet 4.6) achou **0 de 18** defeitos confirmados; a reversão (Sonnet 5.5) achou 14–16 de 18 e, nas três versões do Plan, ≈79% (33/42) contra ≈2% (1/42). Lição: **cortar custo na verificação sem teste é a pior alavanca**; o corte deve começar onde o erro é barato de detectar. `[FATO]`
6. **A maior alavanca sem risco de Eficácia está fora do LLM:** gates Classe D (código) já existem e já são baratos; faltam (a) o **Orquestrador rodar o gate antes de gastar uma revisão LLM**, (b) **reentregas de rodada ≥2 revisadas por diferença** + passe completo só na rodada final, (c) mover tarefas mecânicas (carimbos, mapa, índices, cópia de handoff) para script ou modelo de baixo custo. `[PROPOSTA]`
7. **Benchmarks externos apontam para a solução mais simples:** roteadores aprendidos frequentemente **não superam** "sempre o melhor modelo único", e a maior parte do ganho de roteamento vem do **tipo de tarefa** (tabela estática) — exatamente o que o SOT já tem como taxonomia (Tipos I–V, Classe D/H/P/C). Não construir roteador aprendido; construir **tabela estática por tarefa + escalonamento por sinal + telemetria**. `[EXTERNO]`

**Recomendação:** adotar uma **Matriz de Roteamento Meta (MRM)** de 5 níveis (§7), implantada em **3 ondas** (§11) — onda 0 sem tocar arquivo normativo; onda 1 por teste de não-inferioridade sobre o banco que o repositório já tem (§8); onda 2 só com telemetria. Estimativa ilustrativa (§9.2, hipótese de 30% do volume do Especificador ser mecânico): **−32% a −43%** do custo do Especificador, **sem mexer no Revisor**. Número real exige a telemetria da onda 0.

**Decisões que dependem de Andraus** (§11): D1–D6.

---

## 2. Escopo, método e limites

- **Escopo:** **Agentes de Construção** (AC: Orquestrador, Especificador, Revisor, subagentes auxiliares, scripts/hooks/CI, Auditor Externo; DHR-AGENTES-001) em profundidade; **Agentes de Trading** (AT, runtime ORYX) só como mapeamento de herança, porque está spec-only (AGENTS §1, CEE-001 §1).
- **Método:** (i) leitura dos agentes, `CEE-001`, `CONSTITUTION`, `RULES`, EUA-E19, DHR-EUA-E19, DHR-AUDITOR-EXTERNO-014/015, `WORKFLOW.md`, ROADMAP §23, scripts, CI, hooks, Auditor Externo; (ii) dimensionamento dos custos de leitura por tamanho de arquivo (≈ bytes/4 — aproximação, não tokenização real); (iii) pesquisa web (14 entradas, §5; fontes em §10), cada uma classificada como Padrão/Prática/Benchmark/Evidência/Opinião; (iv) síntese em matriz e protocolo de teste.
- **Limites declarados:** (a) **não há telemetria de custo por tarefa no repositório** — o único custo medido é o do Revisor na SPEC-006 (DHR-014: ≈275–280 mil tokens e ≈50 chamadas por revisão; original ≈120–138 mil e ≈20); (b) não sei se o ambiente do Andraus cobra por API ou por assinatura com limite de uso — isso muda *o que* otimizar (US$ vs. cota); (c) preços são os da página oficial consultada hoje e podem mudar; (d) benchmarks externos medem roteamento de consultas isoladas, não revisão normativa de especificações — **transferência é `[INFERÊNCIA]`**; (e) todo o gabarito interno vem de uma família de modelos (circularidade já admitida na DHR-014 §2).

---

## 3. Auditoria interna

### 3.1 Quem executa o quê, em que modelo `[FATO]`

| Executor | Modelo / esforço hoje | Onde está definido | Observação |
|---|---|---|---|
| **Orquestrador** (sessão principal) | O da sessão do Claude Code (não declarado no repositório) | — (CONSTITUTION: "roteamento é responsabilidade do Orchestrator") | Faz handoff, mapa, merge, PRs, delegações. Sem política de modelo própria. |
| **Especificador SOT** | `claude-opus-4-8`; esforço "médio" **só como conduta** | `especificador.md` frontmatter + §4 | Escreve Specs, Plans, atas, pesquisa web, autopré-check, correções. Sem Bash. |
| **Revisor SOT** | `claude-sonnet-5-5`; esforço "alto" **só como conduta** | `revisor.md` frontmatter + §0 | Gate MCP `revisor_gate` + 8 passos + 4-ter + 5-bis. Sem Bash/Write/Edit (DHR-AUDITOR-EXTERNO-009/015). |
| `sot-spec-reviewer` | **herda a sessão** (sem `model:`) | `.claude/agents/sot-spec-reviewer.md` | Revisão independente de specs; read-only. |
| `sot-schema-validator` | **herda a sessão** (sem `model:`) | `.claude/agents/sot-schema-validator.md` | Valida Draft-07 — já coberto por `npm test` (`tests/validate-schemas.js`). |
| **Scripts/hooks/CI** | Sem LLM (Classe D) | `scripts/`, `.claude/settings.json`, `.github/workflows/` | 15+ verificadores, mapa, RPSA, roteador AEX, manifesto do gate. |
| **Auditor Externo** | Codex CLI (outra família), 6 chamadas/dia | `governance/propostas/AUDITOR-EXTERNO/OPERACAO.md` | Consultivo; só ao Orquestrador. |
| **Andraus** | Humano | — | Homologa; decisões CONS-01. Não roteável. |

### 3.2 Normas vigentes sobre roteamento `[FATO]`

| Norma | O que diz | Limite |
|---|---|---|
| CEE-001 §5 / RULE-CEE-002 | Tipo I–II → Haiku; III → Sonnet; IV–V → Opus (reservado). Promoção de classe só com **evidência de erro de julgamento mensurável**. | Escopo ORYX/trading. Sem versão de modelo. |
| CEE-001 §9 / §10 | Mudança de roteamento = mesma autoridade de Framework Oficial; **nenhum agente reduz a própria classe**; reversível e versionada. | — |
| CONSTITUTION ("Modelo de roteamento cognitivo") | Tipos I–V; "Orchestrator decide, agentes não escolhem o próprio modelo". | Tabela de 5 tipos ≠ tabela de 4 linhas do CEE-001 §5 (ver A-09). |
| EUA-E19 (DHR-EUA-E19) | Roteamento **por papel** na camada meta; leitura proporcional ao dial GES; short-circuit RPSA; continuar o mesmo agente em re-pareceres. | Premissa de plataforma caducou (A-02); sem roteamento por tarefa. |
| DHR-AUDITOR-EXTERNO-014 | Revisor volta a modelo mais capaz após medição; "4Es: Eficácia > Economicidade". | Mede um papel, uma Spec. |
| RULE-MECH-01..04 (CLASSE-MECH-001) | Classe D/H/P/C **por BASpec**. | Classifica *mecanismos do produto*, não tarefas da camada meta — mas o vocabulário é reaproveitável (§7). |
| ENF-03 | "O LLM nunca é seu próprio gate." | Veda modelo barato como **gate** de qualquer coisa. |

### 3.3 A evidência medida que ancora tudo (DHR-014) `[FATO]`

| Braço | Modelo | Achou (de 18 defeitos confirmados, v1.0) |
|---|---|---|
| Revisor titular (EUA-E19) | Sonnet 4.6 | **0** |
| Modelo mais novo, método antigo | — | 14 |
| Sonnet 5.5 + Passo 4-ter | Sonnet 5.5 | 16 (repetido 3×: 16, 17, 16) |

Três versões do Plan (42 defeitos): original **1 (≈2%)** × novo **33 (≈79%)**; custo ≈2× tokens. Banco de estresse (HANDOFF): recall por rodada ≈83–100%, 0 falso alarme. **Leitura para o roteamento:** (i) o ganho de geração de modelo foi de uma ordem de grandeza maior que o ganho de método; (ii) um revisor "barato" que dá CONFORME é pior que nenhum, porque dá falsa segurança; (iii) existe um **gabarito reutilizável** (SPEC-006 v1.0–1.2 e banco de estresse) — é o ativo que permite testar qualquer roteamento sem inventar benchmark.

### 3.4 Achados da auditoria

| ID | Achado | Evidência | Severidade p/ 4Es |
|---|---|---|---|
| **A-01** | Roteamento por **papel**, não por **tarefa**. Uma emenda constitucional e uma cópia de arquivo de handoff usam o mesmo agente/prompt/leitura. | `especificador.md` §4; EUA-E19 §2 | Alta (Eficiência/Economicidade) |
| **A-02** | Premissa "frontmatter não tem esforço" caducou; esforço dos dois agentes **não é aplicado**, só recomendado. Esforço efetivo = padrão do ambiente `[INFERÊNCIA]`. Para Opus 4.8 o padrão da API é `high` e a própria documentação recomenda `xhigh` para agentic — distinto do "médio" que a EUA-E19 supôs. | EUA-E19 §1; `revisor.md` §0; docs `sub-agents`, `effort` | Alta (Eficácia *e* Economicidade: pode estar gastando mais *ou* menos que o decidido) |
| **A-03** | Opus 4.8 em uso enquanto Opus 5.5 (−20% de preço, cache 0,05×) existe; sem teste de substituição. | `especificador.md`; tabela de preços §6 | Média |
| **A-04** | `sot-spec-reviewer` e `sot-schema-validator` sem `model:` → herdam o mais caro da sessão. Schema-validator duplica script determinístico. | frontmatter dos dois; `npm test` | Média |
| **A-05** | **Sem telemetria de custo/eficácia por tarefa** nos agentes de construção. CEE-001 §7 define métricas só para missões da trading. | grep em `scripts/`, `governance/` | Alta (impede toda decisão baseada em evidência — o próprio CEE-001 §5 exige evidência para mudar classe) |
| **A-06** | Custo de leitura obrigatória é **fixo e alto**: núcleo ≈55 mil tokens (ROADMAP ≈17k, atomic-spec ≈10k, RULES ≈12k, prompt do agente ≈10–11,5k, AGENTS ≈5k); lista HIGH/CRITICAL soma ≈+55k (CATALOGO ≈20k, RMR ≈23k, CONFLICT-MAP ≈8,5k, MAN-001 ≈3,6k) e atas EUA-E04..E18 ≈49k. A proporcionalidade da EUA-E19 é instrução, sem verificação. | `wc -c` dos arquivos (≈bytes/4) | Alta |
| **A-07** | Reentrega **sempre do texto completo** (`especificador.md` §2) e o Revisor relê tudo a cada rodada; um Plan + checks chega a 60–225 KB (≈15–56 mil tokens) por Spec. Não há modo "rodada de correção por diferença". | `specs/features/SPEC-00x/` | Alta |
| **A-08** | O gate Classe D do Revisor **não carregou em nuvem** nas 6 rodadas do banco ("GATE NÃO VERIFICADO"). Sem gate, defeitos *detectáveis por código* são caçados por LLM — a ordem de grandeza mais cara — e o parecer fica limitado a CONFORME condicional. | HANDOFF §4 | Alta |
| **A-09** | Duas taxonomias de roteamento coexistem: CONSTITUTION (Tipos I–V, 5 linhas) e CEE-001 §5 (4 linhas, "taxonomia vertical Tipos I–V"). Mapeamento 1:1 não explícito. | `CONSTITUTION.md`; `CEE-001 §5` | Baixa (deriva documental; achado de Revisor/doc-sync) |
| **A-10** | O Especificador **não tem Bash** e, portanto, não roda o gate antes de entregar; quem pode fazê-lo é o Orquestrador, mas nenhum passo documentado o obriga a rodar `revisor_gate`/`run_gates` **antes** de gastar uma invocação do Revisor. | `especificador.md` frontmatter; fluxo AGENTS §5 | Média (ganho "grátis") |
| **A-11** | Pesquisa web (Dossiê de abertura, RULE-ECC-02) e redação normativa de fronteira rodam no mesmo modelo caro, embora a coleta/classificação de fontes seja trabalho de menor julgamento que a decisão de fronteira. | EUA-E21; `especificador.md` §4 itens 2–3 | Média |
| **A-12** | `Explore`/`general-purpose` nativos herdam o modelo da sessão; buscas de "onde está X" (mapa do projeto já existe) custam o preço do modelo principal. | docs `sub-agents` | Média |

### 3.5 Anatomia do custo de uma rodada Especificador→Revisor `[INFERÊNCIA]` (a medir)

```
Rodada = prompt do agente (10–11,5k) + AGENTS/CLAUDE.md (5k) + núcleo (≈40k) [+ lista HIGH/CRIT ≈55k + atas ≈49k]
         + artefato (15–56k) + trabalho (≈50 chamadas, cada uma relendo o contexto acumulado)
```
O contexto fixo (≥60 mil tokens) é pago **em cada invocação nova**; o cache de prompt reduz o *preço* da releitura (0,1× / 0,05× nos modelos 5.5) mas só dentro do TTL (5 min padrão; 1 h opcional) e só com prefixo estável. Rodadas separadas por revisão humana ou agente diferente tendem a ultrapassar 5 min → **recomeçam o cache** `[INFERÊNCIA]`.

---

## 4. Inventário de tarefas por criticidade

### 4.1 Escala de criticidade (proposta)

Criticidade **não é tamanho nem dificuldade percebida**; é função de quatro eixos: **(a)** raio de impacto/irreversibilidade (toca baseline, canon, invariante, decisão aberta? INV-07 impede apagar, mas o erro se propaga); **(b)** existência de verificador independente e barato a jusante (gate D, Revisor, Andraus); **(c)** grau de julgamento/ambiguidade; **(d)** fan-out (quantas Specs/agentes herdam o resultado).

| Nível | Nome | Critério | Verificador a jusante | Pode usar modelo de baixo custo? |
|---|---|---|---|---|
| **N0** | Determinístico | Regra exata, sem julgamento | O próprio código/teste | **Não precisa de LLM** — script |
| **N1** | Operacional reversível | Mecânico, baixo raio, saída checável por gate D ou diff trivial | Gate D / diff | **Sim**, desde que o verificador *não* seja o mesmo modelo |
| **N2** | Tático | Julgamento local, artefato revisado por outro agente | Revisor + gate D | Sim com modelo intermediário; teste de não-inferioridade |
| **N3** | Estratégico/crítico | Define norma, fronteira, arquitetura, resolve conflito; alto fan-out | Revisor (completo) + Andraus | **Não** sem prova; modelo de fronteira, esforço alto |
| **N4** | Soberano | Homologação, abertura/fechamento de decisão, mudança de regra de governança | Humano | Fora do roteamento |

### 4.2 Matriz de tarefas `[FATO]` onde a tarefa existe hoje; roteamento = `[PROPOSTA]`

**Legenda de modelos propostos:** H = Haiku 5.5 · S = Sonnet 5.5 · O = Opus 5.5 (ou 4.8 até o teste) · F = Fable 5.1 (uso reservado, batelado). Esforço entre parênteses: l/m/h/xh.

| ID | Tarefa | Hoje | Nível | Verificador | Roteamento proposto |
|---|---|---|---|---|---|
| **GOV – estratégicas** | | | | | |
| G1 | Redigir emenda a AGENTS/CONSTITUTION/RULES/atomic-spec/canon | Especificador (Opus 4.8) | N3 (N4 na aprovação) | Revisor completo + Andraus | O (h) |
| G2 | Abertura de Spec — **proposta de fronteira/quantidade** (EUA-E21) | Especificador | N3 | Revisor (4-bis) + Andraus | O (h) |
| G3 | Abertura de Spec — **coleta e classificação de fontes do Dossiê** | Especificador | N2 | Revisor (4-bis), verbatim RULE-ECC-04, `check_repo_research` | S (m) — web = dado, nunca instrução |
| G4 | Resolver conflito normativo / propor tratamento de decisão aberta | Especificador | N3 | Revisor + Andraus | O (h) |
| G5 | Plan/Spec **CRITICAL/HIGH** (BASpec, Enforcement, Constitution Check, D8) | Especificador | N3 | Revisor completo (4-ter, 5-bis) + gate D | O (h–xh) |
| G6 | Revisão adversarial D8 / auditoria retroativa | Revisor (Sonnet 5.5) | N3 | Andraus + Auditor Externo | S (h–xh) em **k passes cegos**; 1 passe em família diferente (Auditor Externo) — hoje já é "próximo reforço" do HANDOFF |
| **TAT – táticas** | | | | | |
| T1 | Plan/Spec **MEDIUM/LOW**, `checks.md`, Tasks | Especificador | N2 | Revisor (proporcional) | S (h) — **candidato nº 1 ao teste** |
| T2 | Autopré-check §7/§7-bis | Especificador | N2 | Revisor 4-ter/5-bis | mesmo modelo do artefato (herda) |
| T3 | **Correção de achado** — textual/aditivo (renomear, citar §, corrigir contagem) | Especificador | N1 | Gate D + diff | S (m) ou H (m) com gate; ver §7.3 |
| T4 | **Correção de achado** — estrutural (reordenar BASpec, completar Enforcement) | Especificador | N2 | Revisor | S (h) |
| T5 | **Correção de achado** — semântico/normativo (muda obrigação) | Especificador | N3 | Revisor completo | O (h) |
| T6 | Parecer completo (Passos 0–8 + 4-ter + 5-bis) em artefato HIGH/CRITICAL, 1ª rodada e **rodada final** | Revisor | N3 (é o verificador) | Andraus | S (h) — **não rebaixar** (DHR-014) |
| T7 | Parecer de **rodada intermediária** (verificar fechamento de achados + regressão nas regiões alteradas) | Revisor (completo) | N2 | Gate D completo + passe final completo | S (h) por **diferença**; teste em §8 |
| T8 | Parecer MEDIUM/LOW, Dossiê (4-bis), emendas simples | Revisor | N2 | Andraus | S (m–h) |
| T9 | Redação de ata DHR / registro em CATALOGO, CONFLICT-MAP, RMR (papel Controlador) | Especificador/Orquestrador | N1–N2 (decisão = N4, redação = mecânica) | Gate D (`check_refs`, `check_doc_sync`, `check_rpsa`) + Andraus | S (m); H para linhas de índice |
| T10 | Resumo a Andraus de achados `aex-rota-andraus` | Orquestrador | N2 | Andraus | S (m) |
| **OPE – operacionais** | | | | | |
| O1 | Gate D: `revisor_gate`, `validate_spec_sot`, `check_*`, `lint`, `npm test` | Código | **N0** | — | script (0 token) |
| O2 | Mapa, carimbos RPSA, router AEX, doc-sync, handoff-check, manifesto do gate, backlog triggers | Código/hook | **N0** | — | script (0 token) |
| O3 | **Pré-gate antes do Revisor** (rodar `revisor_gate`/`run_gates` pelo Orquestrador e devolver `REPROVADO_D` ao Especificador sem invocar o Revisor LLM) | **inexistente** | **N0** | código | script — ganho imediato (A-10) |
| O4 | Reescrever HANDOFF (cópia do anterior → `docs/handoffs/`, estado novo) | Orquestrador | N1–N2 | `check_handoff.py` | S (m); cópia = comando, não LLM |
| O5 | Busca/exploração ("onde está X", checar existência) | Explore/Orquestrador | N1 | — | H (m) via subagente `Explore` redefinido (A-12), ou `docs/mapa/` + Grep sem LLM extra |
| O6 | Erratum aditivo P2 da faixa `aex-rota-rapida` | Orquestrador/Especificador | N1 | `route_aex` + Revisor + Andraus | S (m) com gate; H apenas se verificador for código |
| O7 | Triagem de CI/PR (ler log, resumir causa, reportar) | Orquestrador | N1 | CI | H–S (l–m) |
| O8 | Regenerar índices/tabelas derivadas à mão | Especificador | N1 → candidato a N0 | `build_map --check`, `check_doc_sync` | **converter em script** |
| **EXT – externas** | | | | | |
| E1 | Auditoria consultiva independente (Codex) | Auditor Externo | N3 como *verificador de família diversa* | Revisor + Andraus | manter (valor = diversidade de família) |
| **RUN – trading (herança futura)** | | | | | |
| R1 | Skills/Engines Classe D | produto | N0 | testes | código; LLM só para texto de apoio |
| R2 | Agentes de domínio Classe H | produto | N2 | gate D de saída (ENF-03) | S (m–h) |
| R3 | Classe P / conflito alto / Manager Fase 2 em decisão crítica | produto | N3 | Risk Agent, gate | O (h); F só reservado |
| R4 | Backtests/calibração J-001/N-001, auditoria em lote | produto | N2–N3, **não interativo** | métricas | **Batch API (−50%)** quando fizer sentido |

### 4.3 Distribuição esperada `[INFERÊNCIA]`

Pelos assuntos dos 142 commits do repositório (contagem por palavra-chave, com sobreposição: ≈59 mencionam ata/DHR; ≈24 fix/errata/regeneração; ≈16 RPSA; ≈8 HANDOFF; ≈15 Spec/homologação), **a maior parte das *operações* é N0–N1/N2 (governança de registro, sincronização, correção), enquanto o *valor* e o *risco* concentram-se em poucas tarefas N3 (Plan CRITICAL, emendas, parecer completo)**. Isto é o formato clássico em que roteamento por tarefa paga bem — mas a proporção real de *tokens* por nível é **[NÃO MEDIDA]** (A-05).

---

## 5. Estado da arte e benchmarks `[EXTERNO]`

Classificação por tipo (instrução do Especificador §4 item 3). Nada aqui vira baseline.

| # | Fonte | Tipo | O que estabelece | Aplicação ao SOT | Confiança |
|---|---|---|---|---|---|
| X1 | FrugalGPT (Chen et al., arXiv:2305.05176) | Padrão/Benchmark | Três estratégias: adaptação de prompt, aproximação, **cascata**; reporta até 98% menos custo com desempenho de GPT-4 em tarefas de 2023 | Fundamenta cascata "barato → escala"; **os números são de 2023 e outro regime de preços** | Média |
| X2 | RouteLLM (Ong et al., arXiv:2406.18665) | Padrão/Benchmark | Roteadores leves entre modelo forte/fraco treinados em preferência humana; >2× de redução de custo em certos casos | Referência de que roteamento *por consulta* funciona **onde há muitos exemplos e métrica clara** — não é o caso de revisão normativa | Média |
| X3 | RouterArena (ICLR 2026) e LLMRouterBench (arXiv:2601.07206; 400 mil+ instâncias, 21 datasets, 33 modelos) | Benchmark | Muitos roteadores têm desempenho parecido; **vários (inclusive comerciais) não superam de forma confiável um baseline simples**; grande lacuna até o oráculo; curadoria do conjunto de modelos importa mais que tamanho | Argumento contra construir roteador aprendido; a favor de **conjunto pequeno e curado** (H/S/O) | Alta (benchmark amplo) |
| X4 | "Most of the LLM Routing Gap Is Task Type" (Lee, arXiv:2608.23023) | Evidência (1 estudo, sem holdout) | 14 modelos × 294 questões: **tabela estática por tipo de tarefa** captura a maior parte do ganho (262 acertos a US$3,33 vs. melhor modelo único 245 a US$7,69); reexecução idêntica muda 5,37% dos pares → "ganho pequeno não prova roteamento" | **Valida o desenho da MRM** (tabela por tarefa) e a exigência de **repetir execuções** no teste | Média-baixa (autor reconhece ajuste e avaliação no mesmo conjunto) |
| X5 | TwinRouterBench (arXiv:2605.18859) | Benchmark | Roteamento deve ser avaliado **por passo em agentes** e em execução real (SWE-bench Verified), com sucesso *e* gasto real, sem juiz LLM | Direciona o protocolo §8: medir fim-a-fim (defeitos confirmados por US$), não por chamada | Média |
| X6 | Moslem & Kelleher, survey de roteamento/cascata (TMLR 2026, arXiv:2603.04445) | Prática (revisão) | Sistemas práticos combinam paradigmas; roteamento tem objetivos conflitantes; generalização é problema aberto | Cautela: não prometer roteamento universal | Média |
| X7 | Anthropic, *Building effective agents* | Prática oficial | Comece pelo mais simples; **routing** (fácil→modelo pequeno, difícil→grande), orchestrator-workers, evaluator-optimizer; complexidade só se melhorar resultado medido | Alinha com "tabela estática + medir" e com Detector≠Gate | Alta |
| X8 | Anthropic, *Multi-agent research system* | Prática/Evidência de fabricante | Agentes ≈4×, multiagente ≈15× os tokens de um chat; líder Opus + subagentes Sonnet superou Opus único em +90,2% (eval interno de pesquisa); **ruim para tarefas de contexto compartilhado/dependência forte (a maioria de código)**; avaliar com ~20 consultas reais e juiz com rubrica, resultado final > caminho | Pesquisa web do Dossiê paraleliza bem; **redação de Plan não** (dependência forte). Valida avaliação pequena e realista (§8) | Média-alta (fabricante, eval próprio) |
| X9 | Anthropic, doc *Advisor tool* (`advisor_20260301`, beta) | Padrão oficial | Executor barato + conselheiro mais capaz sob demanda, cobrado à tarifa do conselheiro; `max_uses`; cache do conselheiro compensa a partir de ≈3 chamadas; "bom ajuste" para agentes de horizonte longo, "mau ajuste" para tarefas de uma volta; números internos: ganhos de +7 a +10 pts em casos específicos, **resultados dependem de tarefa — validar na própria carga** | Aplicável à **trading via API**; em Claude Code não há campo de frontmatter para isso `[INFERÊNCIA — verificar]` | Média |
| X10 | Resumos secundários do "advisor" (MindStudio, Builder.io, Developers Digest) | Opinião | ≈11–12% menos custo por tarefa com Sonnet+Opus em SWE-bench Multilingual; um relato contrário (quase nenhuma economia com executor Opus 5.5) | **Não usar como número** — fonte secundária, conflitante, nomes de modelo não confirmados | Baixa |
| X11 | Anthropic, doc *Effort* | Padrão oficial | `effort` `low…max` afeta **todos** os tokens (texto, chamadas de ferramenta, pensamento); `low` recomendado para "subagentes"; Opus 5.5 e Haiku 5.5 padrão `medium`; demais `high`; mudar esforço no meio da conversa só sem perder cache com o recurso por mensagem (beta); **"rode uma varredura de esforço nos seus evals"** | Fecha a lacuna A-02: esforço agora é configurável e deve ser **varrido**, não presumido | Alta |
| X12 | Anthropic, doc *Subagents* (Claude Code) | Padrão oficial | Campos `model` (alias, ID, `inherit`), `effort`, `maxTurns`, `omitClaudeMd`, `experimental.cacheTtl` (5m/1h), `disallowedTools`; precedência: parâmetro da invocação > frontmatter > variável de ambiente > modelo da sessão; `Explore` herda o modelo da sessão (para Haiku, redefinir um subagente `Explore` com `model: haiku`) | Habilita **roteamento sem roteador**: o Orquestrador escolhe `model`/`effort` por invocação (já é atribuição dele, CONSTITUTION) | Alta |
| X13 | Anthropic, doc *Pricing* | Dado | Preços §6; cache lido 0,05× (Opus 5.5/Sonnet 5.5) a 0,1× (demais); escrita 1,25× (5 min) ou 2× (1 h); Batch −50% | Base da §9 | Alta (mas muda) |
| X14 | Blog de roteamento de subagentes (byteiota) | Opinião | Cada subagente tem custo de partida ≈25–35 mil tokens | **Não verificado**; coerente com A-06 (prompt+contexto fixo) — **medir antes de citar** | Baixa |

**Convergência (o que as fontes de confiança alta/média-alta sustentam em conjunto):**
1. **Tabela estática por tipo de tarefa primeiro**; roteador aprendido só se a telemetria mostrar que a tabela deixa dinheiro/qualidade na mesa (X3, X4, X7).
2. **Escalonar por sinal, não por palpite** — cascata/conselheiro com limite de usos (X1, X9).
3. **Medir fim-a-fim em tarefa real, com repetição, sucesso e custo juntos** (X4, X5, X8, X11).
4. **Esforço é um eixo separado do modelo** e precisa de varredura própria (X11).
5. **Multiagente só onde paraleliza** (X8) — não fragmentar a redação normativa em subagentes pequenos.

**Lacuna honesta:** não encontrei benchmark público de **revisão de especificações normativas** nem de custo-por-defeito-confirmado em LLM-como-revisor. O benchmark relevante é o **interno** (§3.3), o que reforça §8.

---

## 6. Preços de referência `[EXTERNO]` (página oficial, consulta de 2026-10-17)

| Modelo | Entrada US$/MTok | Saída US$/MTok | Cache lido (× entrada) | Relação c/ Sonnet 5.5 (entrada) |
|---|---|---|---|---|
| Haiku 5.5 (prompt ≤100 mil tokens)¹ | 0,10 | 0,50 | 0,1× | 0,05× (**20× mais barato**) |
| Sonnet 5.5 | 2 | 10 | **0,05×** | 1× |
| Opus 5.5 | 4 | 20 | **0,05×** | 2× |
| Opus 4.8 (hoje: Especificador) | 5 | 25 | 0,1× | 2,5× |
| Fable 5.1 | 10 | 50 | 0,025× | 5× |

¹ Acima de 100 mil tokens de prompt, Haiku 5.5 passa a US$0,50/US$2,50. A leitura obrigatória HIGH/CRITICAL (≈110 mil tokens) **cruza esse limiar** — por isso Haiku só serve a tarefas N1 com contexto curto, nunca ao fluxo de leitura completa.

**Leituras:** (i) a diferença de preço entre tiers (até 20×) é muito maior que a diferença de esforço; (ii) para os modelos 5.5, **reler contexto estável em cache custa metade** do que custa em Opus 4.8; (iii) preço por token ≠ custo por tarefa — modelos diferem em tokens gastos por tarefa e o esforço muda isso (X11); só o teste da §8 dá o custo real.

---

## 7. Proposta: Matriz de Roteamento Meta (MRM)

### 7.1 Regras `[PROPOSTA]`

- **R1 — Tabela estática por tarefa**, na forma da §4.2, versionada e referenciada por ID `T/G/O…`. Sem roteador aprendido (X3, X4).
- **R2 — Quem decide:** o **Orquestrador** escolhe `model` e `effort` **por invocação** do `Agent`, dentro dos *pisos* da tabela (CONSTITUTION: Orquestrador decide; CEE-001 §10.1: agente não reduz a própria classe). Pisos por papel (Revisor ≥ Sonnet 5.5/h; Especificador N3 ≥ modelo de fronteira) ficam no frontmatter e **o parâmetro por invocação nunca desce abaixo do piso** — registrar isso na emenda, porque a precedência técnica (X12) permitiria contornar o frontmatter.
- **R3 — Escalonamento só para cima e por sinal objetivo**: gate D reprova; Revisor aponta ≥1 achado Crítico; autopré-check do próprio executor marca "incerto"; 2ª tentativa falhou no mesmo verificador. **Rebaixamento permanente** só pelo fluxo CEE-001 §9 com evidência (Salvaguarda 1, 5).
- **R4 — Verificador independente do executor:** a saída de um modelo barato (N1) só é aceita se verificada por **código** (N0) ou por modelo/família de nível ≥ N2 (ENF-03). Haiku **nunca** é gate.
- **R5 — N0 antes de N1:** toda tarefa N1 repetida ≥3 vezes por mês vira candidata a script (mesmo molde do BL-019/`build_map`).
- **R6 — Pré-gate:** o Orquestrador roda o gate Classe D **antes** de invocar o Revisor; `REPROVADO_D` volta ao Especificador sem custo de revisão LLM (A-10). O Revisor continua obrigado a chamar o gate (defesa em profundidade).
- **R7 — Esforço explícito:** `effort` declarado no frontmatter (Revisor `high`; Especificador conforme varredura §8), substituindo a "conduta" não aplicada (A-02). Alterar frontmatter exige Andraus (R12 abaixo).
- **R8 — Telemetria mínima obrigatória** por invocação (§7.4) — sem ela, nenhum rebaixamento é homologável (CEE-001 §5, "evidência registrada").
- **R9 — Rodadas por diferença (a testar, §8):** rodada ≥2 recebe lista de achados da rodada anterior + diff; passe **completo** obrigatório na rodada final antes de Andraus e sempre em CRITICAL.
- **R10 — Não fragmentar redação normativa** em subagentes (X8): paralelizar só coleta (Dossiê, buscas) e verificações independentes (k passes cegos).
- **R11 — Diversidade de família preservada:** o Auditor Externo permanece como verificador de família diferente (corrige a circularidade admitida na DHR-014).
- **R12 — Autoridade:** a MRM e qualquer edição de `.claude/agents/*.md` seguem AGENTS §10 (decisão expressa de Andraus + Revisor); a execução técnica da onda 0 (R2 por invocação, R6) cabe ao Orquestrador sem alterar arquivo normativo.

### 7.2 Mapeamento nível → modelo/esforço (alvo, sujeito a teste)

| Nível | Modelo | Esforço inicial | Condição para vigorar |
|---|---|---|---|
| N0 | script | — | existente |
| N1 | Haiku 5.5 (contexto <100 mil) ou Sonnet 5.5 | `low`–`medium` | verificador código/diff; teste §8.2 |
| N2 | Sonnet 5.5 | `medium`–`high` | teste de não-inferioridade §8.3 |
| N3 | Opus 5.5 (ou 4.8 enquanto não testado) | `high` (`xhigh` em CRITICAL — varrer) | piso; só sobe |
| Verificação completa | Sonnet 5.5 | `high` | **mantido** (DHR-014); k=3 cegos em CRITICAL é proposta do HANDOFF |
| N4 | humano | — | — |

### 7.3 Correções de achado por tipo (alvo de maior volume)

Classificar cada achado do Revisor pelo campo já existente de severidade/tipo do relatório (formato do §6 do `revisor.md`) em **textual-aditivo / estrutural / semântico-normativo** e rotear T3/T4/T5. O Orquestrador classifica; o Revisor da rodada seguinte verifica de qualquer forma. Risco-chave: um achado "textual" que na verdade muda obrigação → o Revisor de rodada seguinte deve tratar mudança de obrigação em região "textual" como achado Crítico (sinal de escalonamento, R3).

### 7.4 Telemetria mínima `[PROPOSTA]` (fonte a confirmar: relatório de uso retornado pelo `Agent`)

`{data, tarefa_id (§4.2), nível, executor, modelo, esforço, tokens_in, tokens_cache_in, tokens_out, chamadas, duração, resultado (PASSOU_D/REPROVADO_D, CONFORME/CONDICIONAL/NÃO CONFORME), rodada, achados_confirmados}` em arquivo versionado de ledger no molde `governance/rpsa-ledger.json` (append-only, INV-07). **Métrica unificada 4Es:**

`Custo por defeito confirmado = US$ da rodada ÷ defeitos confirmados` (Revisor) · `Custo por artefato aceito sem reabertura` (Especificador) · `Taxa de reentrega` (rodadas até CONFORME).

Eficácia é *condição* (não-inferioridade de recall e 0 falso alarme); só então se compara Eficiência/Economicidade — a ordem do RULE-CEE-001 vira procedimento.

---

## 8. Protocolo de validação (Eficácia-first)

Reaproveita o ativo existente: **SPEC-006 v1.0/v1.1/v1.2 (gabarito de 18+13+11 defeitos confirmados)** e o **banco de estresse (2 sorteios × 30 defeitos × 3 rodadas)** da DHR-AUDITOR-EXTERNO-015.

### 8.1 Regras gerais
1. **Repetir:** ≥3 execuções por braço (X4: 5,37% de variação em reexecução; DHR-014: 16/17/16).
2. **Pré-registrar** hipótese, métrica e margem *antes* de rodar (evitar escolher o resultado).
3. **Juiz = defeitos confirmados contra o repositório** (como a DHR-014), nunca "parece bom" por LLM; contar falsos alarmes.
4. **Congelar** o braço de controle (modelo e prompt atuais) e registrar versão do modelo.
5. **Resultado final, não caminho** (X8); medir também tokens, chamadas e US$.

### 8.2 Teste A — Especificador: Opus 4.8 → Opus 5.5 (e varredura de esforço)
- Tarefa: reproduzir Plans/correções com entrada congelada; avaliar com o **Revisor titular** (cego quanto ao braço) e o gate D.
- Braços: 4.8/atual · 5.5/medium · 5.5/high · (opcional) 5.5/xhigh.
- **Aceite:** achados confirmados no artefato ≤ controle (+ margem pré-registrada), mesma taxa de CONFORME na mesma rodada; custo menor.

### 8.3 Teste B — Tarefas N2/N1 do Especificador em Sonnet 5.5 / Haiku 5.5
- Conjunto: 20 correções reais de achados históricos (X8: "comece com ~20"), estratificadas em textual/estrutural/semântico (§7.3), mais tarefas T9/O4/O8.
- **Aceite N1:** 100% passa no verificador código/diff; 0 mudança de obrigação não pedida. **Aceite N2:** não-inferioridade vs. Opus na taxa de reabertura pelo Revisor.
- **Reprova automaticamente** se o executor barato alterou texto normativo fora do pedido (viola INV-07/CONST-01).

### 8.4 Teste C — Revisão por diferença (rodadas ≥2)
- Reexecutar as sequências v1.0→v1.1→v1.2 com R9 e comparar com revisão completa (controle).
- **Aceite:** recall de defeitos *remanescentes e introduzidos* ≥ controle − margem; 0 regressão perdida; custo/tokens menores. **Se falhar, R9 não entra** e fica só o pré-gate (R6).

### 8.5 Teste D — Pré-gate e subagentes auxiliares
- Medir quantas rodadas teriam sido evitadas com R6 (histórico de `REPROVADO_D`).
- `sot-spec-reviewer`: definir `model` explícito e comparar com herança; `sot-schema-validator`: comparar com `npm test` e, se redundante, propor desativação (A-04).

### 8.6 Sondagem de custo do cache
Comparar `cacheTtl` 5m vs. 1h (`experimental`, X12) em uma sessão real de 3 rodadas, medindo escrita/leitura de cache (X13). Hipótese: rodadas espaçadas >5 min pagam nova escrita (1,25×); a 1 h pagam 2× na escrita e 0,05–0,1× nas leituras.

---

## 9. Impacto nos 4Es

### 9.1 Por E

| E | Efeito esperado | Risco | Controle |
|---|---|---|---|
| **Conformidade** | Roteamento versionado, reversível, com autoridade explícita (CEE-001 §9–10); remove inconsistência A-09 | Orquestrador contornar piso via parâmetro por invocação | R2 (piso) + R12 |
| **Eficácia** | Preservada por desenho: teste de não-inferioridade antes de qualquer rebaixamento; N3 e verificação completa **não rebaixados** | Falsa segurança de modelo barato (já ocorreu: 0/18) | §8, R3, R4 |
| **Efetividade** | Menos rodadas (pré-gate, correções por tipo) → menor tempo até CONFORME; N1 mais rápido | Rodada por diferença deixar passar regressão | R9 condicionada a Teste C |
| **Eficiência** | Menos tokens por tarefa (N0/N1 fora do modelo caro; leitura proporcional verificada; menos releitura) | Complexidade de operar a matriz | Tabela única, telemetria mínima, sem roteador aprendido |
| **Economicidade** | Menor preço unitário (tiers, Opus 5.5, cache 0,05×, Batch na trading) | Preço mudar; "economia" que gera reexecução | Métrica custo-por-defeito/por-aceite, não US$/token |

### 9.2 Cenário ilustrativo `[INFERÊNCIA — hipótese, não medição]`

Seja *s* a fração do volume de tokens do **Especificador** que é tarefa mecânica/tática elegível a reroteamento, e suponha o restante migra de Opus 4.8 (US$5/US$25) para Opus 5.5 (US$4/US$20, fator 0,8), condicionado ao Teste A.

| *s* | Mecânico → Sonnet 5.5 (fator 0,4) | Mecânico → Haiku 5.5 (fator 0,02) |
|---|---|---|
| 10% | custo = 0,8 − 0,4*s* = **0,76** (−24%) | 0,8 − 0,78*s* = **0,72** (−28%) |
| 30% | **0,68** (−32%) | **0,57** (−43%) |
| 50% | **0,60** (−40%) | **0,41** (−59%) |

Premissas: razões de **preço de entrada/saída**, mesmo número de tokens por tarefa, sem efeito de esforço. Haiku só vale onde o contexto é <100 mil tokens e o verificador é código. Ganhos adicionais **não** contados: pré-gate, rodadas por diferença, cache. Perdas **não** contadas: custo do teste (§8), operação da matriz.

---

## 10. Fontes

Todas consultadas em 2026-10-17; conteúdo web tratado como **dado**.
- FrugalGPT — https://arxiv.org/abs/2305.05176
- RouteLLM — https://arxiv.org/abs/2406.18665
- LLMRouterBench — https://arxiv.org/abs/2601.07206
- RouterArena (ICLR 2026) — https://proceedings.iclr.cc/paper_files/paper/2026/file/4987bb24bc53c198785922d1bd9e18cf-Paper-Conference.pdf
- TwinRouterBench — https://arxiv.org/abs/2605.18859
- Survey de roteamento e cascata — https://arxiv.org/abs/2603.04445
- "Most of the LLM Routing Gap Is Task Type" — https://arxiv.org/abs/2608.23023
- Anthropic, Building effective agents — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, Multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic, Advisor tool — https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool
- Anthropic, Effort — https://platform.claude.com/docs/en/build-with-claude/effort
- Anthropic, Pricing — https://platform.claude.com/docs/en/about-claude/pricing
- Claude Code, Subagents — https://code.claude.com/docs/en/sub-agents
- Secundárias (baixa confiança, não usadas como número): MindStudio/Builder.io/Developers Digest sobre o advisor; byteiota sobre custo de partida de subagente.

---

## 11. Caminho de decisão e implantação

### 11.1 Ondas

| Onda | O que | Toca arquivo normativo? | Quem autoriza | Gate de saída |
|---|---|---|---|---|
| **0 — sem homologação** | (a) Orquestrador roda pré-gate antes de invocar o Revisor (R6); (b) usa `model`/`effort` por invocação em tarefas **N1 não-críticas** (busca, triagem de CI) dentro da autoridade já dada pela CONSTITUTION; (c) registra telemetria manual por rodada (§7.4) num rascunho; (d) **não** altera Revisor, Especificador nem tarefas N2/N3 | Não | Orquestrador (informa Andraus) | ≥10 rodadas registradas |
| **1 — teste** | Rodar §8.2–8.5 sobre o gabarito existente; resultados em ata | Não (só medição) | Andraus ordena o teste | Relatório com recall, falso alarme, tokens, US$ |
| **2 — homologação** | EUA-E24: MRM + `effort` no frontmatter + `model` nos subagentes + eventual Opus 5.5 + R9 se o Teste C passar; atualiza premissa da EUA-E19 §1 (sem apagá-la — INV-07) | **Sim** (`.claude/agents/*.md`, governance) | Andraus (+ parecer do Revisor, RPSA) | Ata DHR + RPSA |
| **3 — contínuo** | Reavaliação por telemetria (limiar análogo a CEE-001 §7.3: ≈200 unidades de trabalho ou 60 dias); só então considerar roteador aprendido/Batch/advisor na trading | Conforme caso | Andraus | — |

### 11.2 Decisões que preciso de Andraus

| # | Pergunta | Recomendação |
|---|---|---|
| **D1** | Autoriza a **onda 0** (pré-gate + `model`/`effort` por invocação só em N1 não-crítico + telemetria manual)? | **Sim** — não toca baseline, reversível |
| **D2** | Autoriza o **banco de testes da onda 1** (§8) usando o gabarito já existente? | **Sim** — só leitura; custo de execução a limitar |
| **D3** | O ambiente é cobrado **por API (US$) ou por cota de assinatura**? Define se a métrica-alvo é US$ ou tokens/cota. | Informar — muda prioridades, não o desenho |
| **D4** | Margem de não-inferioridade aceitável (ex.: perder até 1 de 18 defeitos? 0?) e número de repetições (≥3) | Margem **0 falso-negativo adicional em Crítico/Alto**; ≥3 repetições |
| **D5** | Tratar a MRM como **EUA-E24** (sucessora aditiva da EUA-E19), sem tocar CEE-001/RULE-CEE-002 (BASELINED; CONST-01)? | **Sim** |
| **D6** | Pode o Orquestrador **propor** o `effort` explícito no frontmatter só depois da varredura §8? | **Sim** — evita fixar valor sem evidência |

### 11.3 O que NÃO fazer (antipadrões)
- **Não** rebaixar o Revisor por custo (DHR-014); **não** usar Haiku como gate (ENF-03).
- **Não** construir roteador aprendido agora (X3/X4) nem fragmentar a redação de Plan em subagentes (X8).
- **Não** fixar `effort` sem varredura (X11).
- **Não** citar os números de blogs secundários do advisor como benefício esperado (X10).
- **Não** tratar "mais barato por token" como "mais barato por aceite" (CEE-001 §12: falsa economia).

---

## 12. Registro e fronteiras

- **Não altera** CEE-001, RULE-CEE-001..004, CONSTITUTION, EUA-E19, DHR-014, `revisor.md`, `especificador.md`, `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`. Qualquer efeito normativo só por decisão expressa de Andraus (AGENTS §10).
- **Decisões abertas** (J-001, G-001, H-001, K-001, C-001, M-001, N-001 etc.): **nenhuma aberta ou fechada** aqui (CONS-01). O roteamento nunca entra no Conviction Vector (INV-04, CEE-001 §10.4).
- **Pendências de verificação:** (i) confirmar fonte de telemetria de tokens no `Agent` do Claude Code; (ii) confirmar se o *advisor tool* é acessível em Claude Code ou só via API; (iii) confirmar versão mínima do Claude Code para `effort`/`omitClaudeMd`/`experimental.cacheTtl` no ambiente de Andraus; (iv) reconferir preços na data de qualquer decisão.
