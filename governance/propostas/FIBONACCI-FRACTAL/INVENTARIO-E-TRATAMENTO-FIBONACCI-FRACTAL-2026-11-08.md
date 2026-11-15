# Inventário e proposta de tratamento — FIBONACCI e CONFLUÊNCIA FRACTAL no repositório

| Campo | Valor |
|---|---|
| Autor | Especificador SOT (Agente de Construção) — por ordem de serviço do Orquestrador |
| Origem | Ordem de Andraus (AskUserQuestion, 2026-11-08): "Há bastante formas de usar Fibonacci e confluência fractal espalhadas e desencontradas. Precisamos levantar as citações e tratá-las" · "verifique o que os docs engenharia geral e auditoria de ideias não implementadas preconizam inicialmente" |
| Motivo imediato | Plan candidato da SPEC-008 tem o roteiro v1 = Elliott → SMC → ICT **sem** Fibonacci/Fractal (P-11 "decidir depois", DHR-SPEC008-001 §1); Andraus não confirmou a DN-3 enquanto isto não fosse levantado |
| Data | 2026-11-08 |
| Status | **[PROPOSTA] — documento de trabalho.** Não é norma, não é baseline, não fecha decisão aberta (CONS-01), não redefine modelo canônico (CONST-01), não edita nenhum outro arquivo. Só Andraus decide. |
| Etiquetas | `[FATO]` = está escrito em ata/baseline/norma citada · `[INFERÊNCIA]` = análise do Especificador · `[PROPOSTA]` = sugestão para decisão · `[DECISÃO NECESSÁRIA]` = só Andraus resolve |

---

## 1. Escopo e método

**1.1 Termos buscados (Grep, sem distinção de maiúsculas).**
- Varredura global: `fibonacci|fractal` (resultado do Grep: **902 ocorrências em 174 arquivos**, excluída `docs/mapa/`).
- Varreduras dirigidas: `fibonacci|fractal|conflu` em `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`, `GLOSSARIO.md`, `WORKFLOW.md`, `canon/`, `governance/` (CONSTITUTION, RULES, CONFLICT-MAP, CATALOGO, ADR-*, DHR-*, MMC-001, SES-001, GPR-001, CIC-001, EMENDA-*, EUA-*), `specs/*.spec.md`, `specs/features/*` (plan/ABERTURA/research), `rag/`, `schemas/`, `backlog/`, `docs/fundamentos/` (ENGENHARIA-GERAL, AUDITORIA-ideias, KERNEL-V2, ARIA), `docs/arranque/`, `docs/MATRIZ-WORKFLOW-SPEC.md`, `reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md`, `docs/_legacy/AUDITORIA-TAXONOMICA/`.
- Buscas pontuais: `geom[ée]tric|macro` em CCM-001 e SPEC-003; `herança|timeframe|grau` em CHM-001 (só 2 acertos irrelevantes — "grau de confiança"); `ADR-002` no repositório inteiro (só `docs/fundamentos/ENGENHARIA-GERAL.md`); `CKG-STRUCT-ORIGIN-001` em ROADMAP/backlog/atas; `GEN-1|normative_authority` em `specs/*.spec.md`, `rag/`, schemas.

**1.2 Leitura.** Para cada acerto relevante, li o entorno com Read (âncora por seção/ID). Os dois documentos de fundamentos **não** foram lidos inteiros: ENGENHARIA-GERAL (5.769 linhas) — lidos os trechos Doc01 p.2, lista de ADRs, §17 Skills, Doc05 FCES §1–§14, Doc06 §5–§6 e §16–§18, MOE §4–§7; AUDITORIA-ideias (3.329 linhas) — lidas Auditoria 01 (resumo), Auditoria 02 (IDEIAS 017–032), SSE, IDEIA 051, INE, conclusão geral e BLIND SPOT 018.

**1.3 O que NÃO foi lido / limites.**
- **Sem Bash:** não rodei `validate_spec_sot.py`, `check_refs.py`, `check_doc_sync.py` nem `build_map.py`. O arquivo novo está em `governance/propostas/` (não é Plan; o gate de Spec não se aplica). O Orquestrador deve rodar `python scripts/build_map.py --check` (BL-019) após o commit.
- **Fora da varredura detalhada** (acertos existem, não inventariados um a um): `.harness-eval/`, `.claude/skills/harness-eval/runs/`, `.claude/agents/`, `.claude/commands/`, `.clinerules/`, `tests/`, `scripts/`, `.github/`, `governance/propostas/` (SPEC-006, SPEC-007, MELHORIAS-PROCESSO, AUDITORIA-INDEPENDENTE-SPEC006), `docs/_legacy/` (exceto os 2 citados), `docs/_legacy/UPGRADES/.../knowledge-graph.json`, `reference/externo/` (tutoriais), `specs/features/*/sources/*.txt`. São ferramentas, testes, propostas antigas ou cópias — não fonte de regra.
- Os termos `retra|extens|projeç`, `grau`, `multi-timeframe` **não** tiveram varredura global própria: foram vistos só no entorno dos acertos de Fibonacci/Fractal. Pode haver citação de "grau"/TF sem a palavra Fibonacci/Fractal não inventariada.
- **Não pesquisei na web** (inventário interno; ordem de serviço).
- Cobertura declarada: **todos os arquivos normativos/canônicos da raiz, `canon/`, `governance/` (não-propostas), `specs/`, `rag/`, `schemas/`, `backlog/` com acerto foram vistos**; das fontes históricas, só os trechos listados. Não afirmo "todas as citações do repositório".

---

## 2. Inventário

Legenda de **TIPO**: **DV** = decisão vigente/[FATO] (ata, decisão homologada ou WORKFLOW soberano) · **NB** = norma em Spec/canon/governança baselined · **FH** = fonte histórica ou [PROPOSTA] (inclui GEN-1, slots indicativos do ROADMAP, Plan candidato) · **ID** = ideia não implementada · **MN** = menção neutra.
Legenda de **TEMA**: **T1** valida × cria · **T2** sentido de "confluência" · **T3** posição no roteiro/hierarquia · **T4** dono (dentro do Elliott × etapa/agente próprio × skill) · **T5** dimensões de convicção geométrica/fractal · **T6** timeframes/graus · **T7** Skills/Classe · **T8** outro.

### 2.1 Decisões vigentes (DV)

| ID | Arquivo · âncora | Trecho literal (curto) | Tipo | Tema |
|---|---|---|---|---|
| FF-001 | `AGENTS.md` §6 item 1 (INV-01) | "Hierarquia inviolável: Elliott → Fibonacci → Fractal → SMC → ICT." | DV | T3 |
| FF-002 | `AGENTS.md` §6 item 2 (Q-005) | "SMC/Fibonacci criam sub-hipóteses com `parent_id`." | DV | T1 |
| FF-003 | `AGENTS.md` §6 item 7 (Q-008) | "estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica" | DV | T5 |
| FF-004 | `docs/arranque/respostas-questionario-v1.md` Q-005 | "Sub-hipóteses: criadas pelos demais agentes (SMC/Fibonacci/ICT)" · logo abaixo: "ICT não cria hipótese de nenhum tipo" | DV | T1 |
| FF-005 | `governance/ADR-CONFLUENCE-001-v3` §1 (HOMOLOGADO 2026-09-26) | "`fibonacci-skill` (skill única) → EXTINTA" · "Fractal Confluence Engine (FCE) → CONCEITO ABSORVIDO por `confluence-elliott`" | DV | T4 T7 |
| FF-006 | ADR-CONFLUENCE-001 v3 §2 | "level-fibonacci-skill — valida Elliott com níveis Fibonacci" · "Cada skill produz seu próprio score. O conjunto de scores compõe o Vetor de Convicção Estrutural." | DV | T4 T5 T7 |
| FF-007 | ADR-CONFLUENCE-001 v3 §3 | "Confluência é interna à matéria de cada agente. Nenhuma confluence-skill cruza matérias de agentes distintos." · Operational "single timeframe (M5 apenas)" | DV | T2 T6 |
| FF-008 | ADR-CONFLUENCE-001 v3 §6 | "Conviction Vector 7D/8D \| Revisar dimensões — dimensão 6.3 \"Fractal\" muda de posição/nome" | DV | T5 |
| FF-009 | `governance/DHR-ADR-HOC003` §4.3 | "Confluence-skills MTF são exclusivas do Structural e Institutional Agent" | DV | T2 T6 |
| FF-010 | `governance/DHR-SPEC008-001` §1, linha P-11 | "**Decidir depois** (opção C; roteiro como dado versionado)" | DV | T3 |
| FF-011 | `ROADMAP.md` "Decisões FECHADAS" → SPEC-008-ABERTURA | "Fibonacci/Fractal no roteiro e reentrada após stop = decidir depois (P-11, P-13)" | DV | T3 |
| FF-012 | `WORKFLOW.md` v2.1 WF-02, WF-03, WF-05 | "Agente Estrutural (Elliott …)" · "Agente Institucional (SMC …)" · "Agente Operacional (= ICT …)" — nenhum passo Fibonacci/Fractal | DV | T3 |
| FF-013 | `WORKFLOW.md` WF-C01 | "macro = subconjunto disponível na Fase 1 (estrutural+institucional); global = vetor com +operacional" | DV | T5 |
| FF-014 | `WORKFLOW.md` WF-C02 | "Confluência vale por independência dos sinais, não por contagem" | DV | T2 |
| FF-015 | `WORKFLOW.md` WF-V02 | "Fibonacci: só em confluência" | DV | T1 T2 |
| FF-016 | `WORKFLOW.md` WF-05 e WF-M03 | "`confluence-ict` → `Operational Agent`, single TF — ex. M5" | DV | T6 |
| FF-017 | `WORKFLOW.md` WF-T01 / WF-R01 `[REVISAR · BL-026]` | "swing = Diário / H4 / H1 · day = H4 / H1 / M15" · "reconciliar entrada M5 × tabela" | DV (valor provisório, não baseline) | T6 |
| FF-018 | `WORKFLOW.md` WF-M01 | "Agente Estrutural ↔ `Structural Agent` (Elliott) \| [INFERÊNCIA] — confirmar SPEC-010" | DV | T4 |
| FF-019 | `governance/DHR-I001-001` / `ROADMAP.md` "Decisões FECHADAS" I-001 | "Classe D formaliza como Skill separada, Classe P permanece comportamento interno do agente" | DV | T7 |
| FF-020 | `governance/DHR-SPEC006-002` (tabela de pendências) | "`school=Fractal` sem produtor de hipótese na SPEC-001 \| dobrado em CKG-STRUCT-ORIGIN-001 (BL-035)" | DV | T4 |
| FF-021 | `ROADMAP.md` "Decisões FECHADAS" Q-A9 | "dimensão do regime de mercado (WF-C04) = dimensão `temporal`" | DV | T5 T8 |

### 2.2 Normas em Spec/canon/governança baselined (NB)

| ID | Arquivo · âncora | Trecho literal (curto) | Tipo | Tema |
|---|---|---|---|---|
| FF-022 | `governance/CONSTITUTION.md` "Hierarquia metodológica inviolável" | "Fibonacci → A régua. Valida geometria. Confirma ou rejeita Elliott." · "Confluência Fractal → Mede coerência entre S1/D1/H4/H1/M5." | NB | T1 T3 T6 |
| FF-023 | CONSTITUTION P05 | "A qualidade aumenta com a convergência entre S1, D1, H4, H1, M5." | NB | T2 T6 |
| FF-024 | CONSTITUTION P10 | "Narrativa Estrutural (Elliott + Fibonacci + Fractal)" | NB | T4 |
| FF-025 | CONSTITUTION "Sequência de execução dos agentes" | diagrama com "Fibonacci Validator" despachado pelo Manager · "2. Fibonacci deve completar antes de Fractal poder medir confluência" | NB | T3 T4 |
| FF-026 | CONSTITUTION "O que nenhum agente faz" | "Fibonacci Validator nunca faz: criar contagens Elliott, gerar sinais isoladamente" | NB | T1 |
| FF-027 | CONSTITUTION "Definições canônicas" | "Confluência: Convergência de múltiplas evidências independentes em uma mesma zona de preço ou hipótese." | NB | T2 |
| FF-028 | `governance/RULES.md` RULE-FB-001 | "NÃO DEVE criar contagens Elliott — apenas validar as recebidas. [Fonte: … \"Fibonacci valida, não cria\"]" | NB | T1 |
| FF-029 | RULES.md RULE-FB-002 | "Onda 2: retração 50%, 61.8% ou 76.4% da Onda 1" | NB | T8 |
| FF-030 | RULES.md RULE-FB-003 | "DEVE verificar confluência de níveis entre timeframes. Quanto maior a convergência de níveis relevantes, maior a qualidade da hipótese." | NB | T2 T6 |
| FF-031 | RULES.md RULE-FB-004 | "DEVE reportar conflito geométrico — NÃO DEVE descartar sozinho. A decisão final é do Elliott Specialist." | NB | T1 |
| FF-032 | RULES.md RULE-EW-004 | "DEVE sempre analisar top-down: S1 → D1 → H4 → H1 → M5." | NB | T6 |
| FF-033 | RULES.md RULE-ICT-004 / RULE-ICT-006 | "requer confluência estrutural + institucional + fractal + geométrica" · "confluência fractal insuficiente" (bloqueia) | NB | T2 T3 |
| FF-034 | RULES.md RULE-SM-004 | "Em qual onda ocorreu? Em qual grau? Em qual nível Fibonacci?" | NB | T8 |
| FF-035 | `governance/CONFLICT-MAP.md` "Conflitos direcionais" | "Fibonacci informa, Elliott decide" (RULE-FB-004) | NB | T1 |
| FF-036 | CONFLICT-MAP "Conflitos fractais" | "H4 incompatível com estrutura D1 … invalidador para Elliott. Recontar obrigatório." | NB | T6 |
| FF-037 | CONFLICT-MAP "O que é impossível por definição" | "IMPOSSÍVEL: Fibonacci criando uma contagem de ondas." · "IMPOSSÍVEL: Sinal contra o bias do D1." | NB | T1 T6 |
| FF-038 | `GLOSSARIO.md` §2 | "Fibonacci Agent \| **Fibonacci Validator** \| Validação geométrica (não cria contagem)" | NB | T1 T4 |
| FF-039 | GLOSSARIO §2-bis | "`Fractal Confluence Engine (FCE)` \| Componente legado \| **`confluence-elliott`** (skill do Structural Agent)" | NB | T4 T7 |
| FF-040 | GLOSSARIO "Skills do Structural Agent" | "`confluence-fibonacci-skill` \| Mede confluência de níveis Fibonacci entre timeframes (MTF: S1/D1/H4/H1)" | NB | T2 T6 T7 |
| FF-041 | GLOSSARIO §3 "Hipótese SUB" | "Sub-hipótese de domínio (SMC/Fibonacci) … (herança fractal do CHM-001)" | NB | T1 |
| FF-042 | `AGENTS.md` §3.2 | Agentes de Trading: "… Fibonacci Validator, ICT Specialist …" | NB | T4 |
| FF-043 | `atomic-spec.md` §3 Matriz de complexidade | "ICT · Fibonacci \| MEDIUM \| D0–D5" | NB | T8 |
| FF-044 | `atomic-spec.md` "Nota sobre C2 (multimodelagem)" | "A autoridade de criar/invalidar hipótese estrutural é de Elliott; SMC/ICT confirmam/enfraquecem." | NB | T1 |
| FF-045 | `specs/features/SPEC-001/plan.md` RULE-HH-001 e BASpec-HH-002 (BASELINE) | "Produtores autorizados: Elliott Specialist, SMC Specialist, Fibonacci Validator." · "QUANDO: SMC Specialist ou Fibonacci Validator identifica sub-hipótese de domínio" | NB | T1 T4 |
| FF-046 | SPEC-001 "Herança Fractal Operacional" | "Hipóteses SUB herdam contexto fractal da PRIMARY pai" | NB | T6 |
| FF-047 | `specs/features/SPEC-002/plan.md` Cenário-EH-T02 | "Skill stateless \"confluence-elliott\" tenta publicar objeto como Evidência … `SKILL_NOT_EVIDENCE_PRODUCER`" | NB | T7 |
| FF-048 | `canon/CCM-001` linha "Conviction Vector 8D" · SPEC-003 RULE-CF-003 / RULE-CF-010 | "`{estrutural, geométrica, fractal, …}` — cada dimensão: valor normalizado \| INDETERMINADO" · convicção "sobre SUBCONJUNTO de dimensões (macro)" | NB | T5 |
| FF-049 | SPEC-003 tabela de conformidade WF (WF-C02 → CF-002) | "Fusão conta evidências causalmente relacionadas como **uma**" | NB | T2 |
| FF-050 | `specs/features/SPEC-006/plan.md` §D2.1, nota N-09 | "Fractal (N-09): está na hierarquia analítica (CONSTITUTION) mas NÃO há produtor de hipótese `Fractal`" | NB | T4 |
| FF-051 | `canon/SAS-001` Cap.1 Princípios 4 e 5 | "As relações de Fibonacci serão utilizadas para validar a consistência estrutural das hipóteses." · "A verificação da confluência entre esses graus será realizada posteriormente pelos componentes responsáveis…" | NB | T1 T4 |
| FF-052 | SAS-001 Cap.3 Domínio 2 "Confluência Geométrica" + "Limite Arquitetural" | "A identificação de agrupamentos geométricos de níveis de Fibonacci constitui conhecimento estrutural do Structural Agent." · "A avaliação de confluência entre múltiplos graus … pertence aos componentes especializados" | NB | T2 T4 |
| FF-053 | SAS-001 Domínio 2 (Retrações / Relações Temporais) | "23.6% / 38.2% / 50% / 61.8% / 78.6%" · "Proporcionalidade temporal" | NB | T8 |
| FF-054 | SAS-001 Domínio 3 "Limite Arquitetural" + nota DIV-SAS-01 | "A medição formal da Confluência Fractal pertence aos componentes especializados" · FCE → `confluence-elliott` | NB | T4 |
| FF-055 | SAS-001 §5.10 e §7.13 | "D1 └── H4 └── H1 └── M15" | NB | T6 |
| FF-056 | SAS-001 Cap.5 (refutação) | "Refutação Tipo B — Incompatibilidade de Fibonacci" · "Refutação Tipo C — Inconsistência Fractal" | NB | T1 |
| FF-057 | SAS-001 Cap.4 (taxonomia de evidências) | "Fibonacci Evidence: evidência baseada em proporcionalidades estruturais." · "Fractal Evidence: evidência baseada em coerência entre graus." | NB | T4 T5 |
| FF-058 | `canon/PPQ-001` 5W2H de Missão + linha PDCA "Plan" | "Where → ativo e grau fractal (S1/D1/H4/H1/M5)" · "How → ordem metodológica: Elliott → Fibonacci → Fractal → SMC → ICT" · "submissões Elliott/Fibonacci/Fractal/SMC/ICT" | NB | T3 T6 |
| FF-059 | `canon/CEM-001` "Technical Rationale" + DIV-CEM-2 | "Exemplo: \"Confluência entre Fibo, AO e estrutura impulsiva.\"" | NB | T2 |
| FF-060 | `governance/SES-001` §12 Confluência | "convergência de evidências independentes ou parcialmente independentes para uma hipótese." | NB | T2 |
| FF-061 | `governance/GPR-001` fluxo, passo 4 "IDENTIFICAR HIPÓTESES" | "Fibonacci/Fractal Agent: confluências de nível" | NB | T4 |
| FF-062 | GPR-001 AP-02 | "Confluência falsa \| Elliott + Fibonacci + ICT confirmam — mas todos derivam do mesmo candle" | NB | T2 |
| FF-063 | GPR-001 PC-01 | "Elliott→Fibonacci→Fractal→SMC→ICT é a ordem de autoridade cognitiva" | NB | T3 |
| FF-064 | `governance/MMC-001` §7 | "posição de Fibonacci/Fractal no roteiro de despacho = \"decidir depois\", P-11" | NB | T3 |

### 2.3 Fontes históricas e propostas (FH)

| ID | Arquivo · âncora | Trecho literal (curto) | Tipo | Tema |
|---|---|---|---|---|
| FF-065 | `specs/features/SPEC-008/plan.md` RULE-MDC-002 (a) e (e) (candidato, não homologado) | "Postos de INV-01: Elliott 1, Fibonacci 2, Fractal 3, SMC 4, ICT 5." · "(e) Fibonacci/Fractal: SEM nó na versão 1 (P-11 = decidir depois)." | FH | T3 |
| FF-066 | SPEC-008 plan.md Cenário-MDC-T05 | "ESTRUTURAL(1) →[OPORTUNIDADE_SIM] FIBONACCI(2) →[OPORTUNIDADE_SIM] INSTITUCIONAL(4)" | FH | T3 |
| FF-067 | SPEC-008 plan.md DN-3 | "sem Fibonacci/Fractal (P-11). Versões futuras: ato seu, sem reescrever a Spec." | FH | T3 |
| FF-068 | `specs/features/SPEC-008/ABERTURA.md` §13 P-11 (recomendação) | "C agora, com A como direção provável: o Fibonacci publica sub-hipóteses próprias (AGENTS §6.2), o que é coisa de etapa separada" | FH | T3 T5 |
| FF-069 | `specs/features/SPEC-008/research.md` §3.2 e §6 CF-8 | "Nenhuma fonte diz se o Fibonacci/Fractal é **etapa despachada pelo Manager** ou **parte interna do Estrutural**." | FH | T3 |
| FF-070 | `ROADMAP.md` §8 SPEC-011 (slot indicativo) | "P1 — HIGH · D0–D7. Retrações; extensões; projeções; clusters; confluência; relações entre graus e timeframes; zonas; invalidações; dependência da hipótese estrutural." | FH | T2 T4 |
| FF-071 | ROADMAP §8 SPEC-010 (slot indicativo) | "proporcionalidade; simetria; complexidade; ambiguidade; continuidade fractal; elasticidade" | FH | T4 |
| FF-072 | ROADMAP §16 FASE 11 | "SPEC-027 Fibonacci · SPEC-028 Fractal/Confluence" · "Cada Skill só criada quando houver responsabilidade realmente atômica e independente." | FH | T7 |
| FF-073 | ROADMAP fluxo cognitivo e cadeia de Specs | "Structural Analysis → Fibonacci/Fractal → Institutional Narrative" · "010 Structural → 011 Fibonacci/Fractal →" | FH | T3 |
| FF-074 | `governance/EUA-E23_…_PROPOSTA.md` tabela de slots | "Fibonacci & Fractal Confluence \| validação geométrica \| P/H \| SPEC-011" | FH | T7 |
| FF-075 | `docs/MATRIZ-WORKFLOW-SPEC.md` linha WF-03 (não-normativa) | coadjuvantes: "SPEC-011 (Fibonacci/Fractal), SPEC-015" | FH | T3 |
| FF-076 | `backlog/RMR-001` BL-035 (Em espera) | "CKG-STRUCT-ORIGIN-001 … (+ `school=Fractal` sem produtor, N-09)" | FH | T4 |
| FF-077 | `backlog/BL-016-MC-SKL-001-encaminhamento.md` "Nível-domínio" | "cálculo de retração/extensão Fibonacci … candidatas a **Skill formal (D)**" `[INFERÊNCIA]` | FH | T7 |
| FF-078 | `reference/PESQUISA-WORKFLOW-TRADING-2026-10-01.md` §B.2 e S-13 | "Fibonacci — evidência **Fraca isolado / Moderada em confluência**" · "(Fib e Elliott medem parte da mesma" | FH | T2 |
| FF-079 | `specs/features/SPEC-003/research-Q-A9-regime.md` tabela de dimensões | "fractal \| Não \| Confluência entre graus/TFs de uma mesma leitura" | FH | T2 T5 |
| FF-080 | `specs/fibonacci.spec.md` (GEN-1, `normative_authority: NONE`, cabeçalho "SUPERSEDED_BY=SPEC-002") | "Confluência de níveis entre múltiplos timeframes (H1 + H4 + D1 convergindo)" · Non-goal "Criar contagens de Elliott" · OTE "61.8%–78.6%" | FH | T1 T2 T8 |
| FF-081 | `specs/elliott-wave.spec.md` (GEN-1) Escopo | "Identificação de graus e hierarquia fractal (S1/D1/H4/H1/M5)" · "Confluência fractal multi-timeframe" | FH | T4 T6 |
| FF-082 | `specs/synthesis.spec.md` (GEN-1) Escopo | "Arbitragem de conflitos Elliott×SMC, Elliott×Fibonacci" | FH | T1 |
| FF-083 | `specs/ict.spec.md` (GEN-1) | "Optimal Trade Entry (OTE) dentro do OB + zona Fibonacci" · "OTE nunca usado isoladamente (sempre com confluência estrutural + institucional + fractal)" | FH | T2 T8 |
| FF-084 | `specs/smc.spec.md` (GEN-1) Inputs | "Níveis Fibonacci relevantes (do Fibonacci Validator)" | FH | T4 |
| FF-085 | `rag/fibonacci.knowledge.md` CHUNK-FB-001 / FB-009 | "O Fibonacci Validator NÃO cria hipóteses Elliott." | FH | T1 |
| FF-086 | rag/fibonacci CHUNK "confluencia_multi_timeframe" | "zona de confluência é formada quando múltiplos timeframes convergem no mesmo nível de Fibonacci (tolerância: ±0.5% do preço)" | FH | T2 T6 |
| FF-087 | rag/fibonacci CHUNK-FB-008 | "Confluência multi-TF no nível: +15 pontos bônus" · "alimenta a dimensão `geometrica`" | FH | T2 T5 |
| FF-088 | `rag/synthesis.knowledge.md` CHUNK "conviction_vector_multidimensional" | "geometrica \| Fibonacci" · "fractal \| Elliott + Fibonacci" · "temporal \| ICT \| Killzone ativa" | FH | T5 |
| FF-089 | `rag/elliott-wave.knowledge.md` (score) | "O score 3/3 exige confirmação de fractal em pelo menos 4 dos 5 graus hierárquicos." | FH | T6 |
| FF-090 | `schemas/fibonacci.output.json` | `"required": ["validation_status", "fibonacci_levels", "geometric_conviction_pct"]` · `confluence_zones` — sem campo de hipótese/`parent_id` | FH | T1 T5 |
| FF-091 | `schemas/synthesis.input.json` / `synthesis.output.json` | `"required": ["elliott_output", "fibonacci_output", …]` · dimensões com `"historico"` | FH | T5 |
| FF-092 | `schemas/elliott-wave.output.json` | `fractal_coherence` · "3=estrutura forte com confluência multi-TF" | FH | T6 |
| FF-093 | `docs/fundamentos/ENGENHARIA-GERAL.md` Doc01 (PAGE 2) | "Fibonacci não cria ondas. Ele valida Elliott." | FH | T1 |
| FF-094 | ENGENHARIA-GERAL "Arquitetura de decisões (ADR)" (lista de exemplos) | "ADR-002 — Fibonacci valida, não cria estruturas." — `ADR-002` não existe em `governance/` (Grep) | FH | T1 |
| FF-095 | ENGENHARIA-GERAL §17 "Arquitetura de Skills" | "Structural Agent ├── Elliott Skill ├── Fibonacci Skill ├── Fractal Skill" | FH | T7 |
| FF-096 | ENGENHARIA-GERAL Doc05 FCES §1 e §3 | "Versão 1.0 (Core Architecture - Congelada)" · "Secular S1 … Primário D1 … Intermediário H4 … Operacional H1 … Execução M5" | FH | T6 |
| FF-097 | FCES §5 "Dimensões da Confluência" | "5.4 Confluência Institucional" · "5.5 Confluência de Volume" | FH | T2 |
| FF-098 | FCES §9 "Confluência de Fibonacci" | "retrações do H1; projeções do H4; extensões do D1; objetivos do S1" | FH | T2 T6 |
| FF-099 | ENGENHARIA-GERAL Doc06 §6.2 e §6.3 | "Convicção Geométrica — Produzida pelo Fibonacci Engine" · "Convicção Fractal — Produzida pelo Fractal Confluence Engine" | FH | T5 |
| FF-100 | Doc06 §16 "Governança da Convicção" | "Fibonacci nunca poderá superar Elliott em importância." | FH | T5 |
| FF-101 | ENGENHARIA-GERAL MOE §6 "Missões Geram Submissões" | "Submissão Elliott ↓ Submissão Fibonacci ↓ Submissão Fractal ↓ Submissão SMC ↓ Submissão ICT" | FH | T3 |
| FF-102 | `docs/fundamentos/KERNEL-V2.md` (exemplo do Scheduler) | "Se houver estrutura promissora, desperta o Fibonacci Agent. Havendo confluência, desperta o Institutional Agent." | FH | T3 |
| FF-103 | `docs/_legacy/AUDITORIA-TAXONOMICA/AUDITORIA-ALINHAMENTO-CANON-HARNESS.md` CAN-009 | "Fractal e Fibonacci aparecem como domínio, dimensão e etapa, mas não como categoria uniforme" | FH | T4 |
| FF-104 | `docs/_legacy/AUDITORIA-TAXONOMICA/ALINHAMENTO-TAXONOMIA-WORKFLOW.md` | "Fibonacci Validator \| Produz validação geométrica e SUB quando aplicável" | FH | T1 |

### 2.4 Ideias não implementadas (ID) — `docs/fundamentos/AUDITORIA-ideias-nao-implementadas.md`

| ID | Âncora | Trecho literal (curto) | Tipo | Tema |
|---|---|---|---|---|
| FF-105 | IDEIA 021 | "Falamos muito de Fibonacci. Mas pouco sobre tempo." | ID | T8 |
| FF-106 | IDEIA 022 — Proporcionalidade Fractal | "Mas também. Tempo … Compatível. Ou. Totalmente incompatível." | ID | T8 |
| FF-107 | IDEIA 023 — Índice de Simetria | "Symmetry Index … preço · tempo · ângulo · proporção · ritmo" | ID | T8 |
| FF-108 | IDEIA 027 — Fractal Continuity | "A história do D1 continua coerente no H4?" | ID | T6 |
| FF-109 | IDEIA 028 — Ruptura Fractal | "H1. Para de confirmar. H4. Ainda confirma." | ID | T6 |
| FF-110 | IDEIA 029 — Peso diferente para cada TF | "D1. Nunca muda por causa do M5." | ID | T5 T6 |
| FF-111 | IDEIA 030 — Herança Hierárquica | "D1. Atualiza. Todas hipóteses filhas. Devem ser recalculadas." | ID | T6 |
| FF-112 | IDEIA 031 — Elasticidade Fractal | "Nem toda divergência entre TF significa erro." | ID | T6 |
| FF-113 | Structural State Engine (SSE) | "Continuidade fractal. … Elasticidade fractal." | ID | T4 |
| FF-114 | Auditoria 01, lista final | "⭐ Herança Fractal das Hipóteses." | ID | T6 |
| FF-115 | IDEIA 051 — Confluência Estrutural-Institucional | "Precisamos medir. O alinhamento. Entre ambos." | ID | T2 |
| FF-116 | Institutional Narrative Engine (INE) | "estrutural (Elliott/Fibonacci/Fractais) e outra institucional (SMC/Volume/Liquidez)" | ID | T2 |
| FF-117 | "Minha conclusão geral da auditoria" | "Elliott e Fibonacci constroem a estrutura da hipótese." | ID | T1 |
| FF-118 | BLIND SPOT 018 | "Confluência é. Múltiplos modelos independentes explicando o mesmo fenômeno de mercado." | ID | T2 |

### 2.5 Menções neutras (MN)

| ID | Arquivo · âncora | Trecho literal (curto) | Tipo | Tema |
|---|---|---|---|---|
| FF-119 | Grupo CC-01: SPEC-002/004/005/006/007/019/020/021/038/046/048/049 (Constitution Check CC-01); SPEC-008 research "Fronteiras"; `canon/SDD-001` checklist; EUA-E19a/E21/E22; DHR-I001-001; BRIEFING-DECISAO-I-001; BL-016 l.25; `atomic-spec` CC-01/INV-01 | "Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada" (ou equivalente) | MN | T3 |
| FF-120 | `AGENTS.md` §1 | "(Elliott · Fibonacci · SMC · ICT)" — sem Fractal | MN | T8 |
| FF-121 | `canon/CEE-001` (ordem de prioridade) | "Conformidade Constitucional (Nível 1 do GES — Elliott, Fibonacci, Fractalidade, SMC, ICT" | MN | T3 |
| FF-122 | `ROADMAP.md` §SPEC-001 (bullets) | "Herança fractal operacional: regras de propagação parent/child em operação (graus/timeframes)." · espelho de Q-005 | MN | T6 T1 |
| FF-123 | backlog BL-031 / `specs/features/SPEC-038/research.md` critério 5 | ferramenta de desenho "sem Fibonacci/Elliott" | MN | T8 |
| FF-124 | `specs/features/SPEC-006/ABERTURA.md` · `SPEC-007/ABERTURA.md` e `research.md` | "estruturas (Elliott/Fibonacci/SMC/ICT)" · fichas GEN-1 "ficam como estão" | MN | T8 |
| FF-125 | `SPEC-021/plan.md` e `SPEC-046/plan.md` (CC-12 N/A) | "(não é Elliott/Fibonacci/SMC/ICT/estrutural)" | MN | T8 |

**Contagem por TIPO** (conferida linha a linha nas tabelas acima): DV **21** · NB **43** · FH **40** · ID **14** · MN **7** · **total 125** linhas de inventário (FF-119 agrupa ~20 menções CC-01 iguais em uma linha).

---

## 3. Sentidos de "confluência" encontrados (RULE-SEM-01/03 — acepção declarada)

| Acepção | O que significa | Quem faz (segundo a fonte) | Citações |
|---|---|---|---|
| **CONF-A — entre graus/timeframes da mesma leitura** ("confluência fractal") | As contagens de vários graus contam a mesma história (pai/filho coerentes) | `confluence-elliott`, skill do Structural Agent (DV); antes, o FCE (extinto) | FF-005, FF-007, FF-022, FF-023, FF-079, FF-096, FF-108..FF-112 |
| **CONF-B1 — cluster de níveis de Fibonacci dentro de uma estrutura** | Vários níveis (retração/extensão/projeção) caem na mesma faixa de preço | conhecimento do próprio Structural Agent (SAS-001 "Confluência Geométrica") | FF-052, FF-080 |
| **CONF-B2 — cluster de níveis de Fibonacci entre timeframes** | O mesmo nível aparece em vários TFs (ex.: retração H1 + projeção H4 + extensão D1) | `confluence-fibonacci-skill` (DV); RULE-FB-003 | FF-006, FF-030, FF-040, FF-086, FF-087, FF-098 |
| **CONF-C — entre modelos/escolas independentes** | Elliott, SMC, volume etc. explicam o mesmo fato **de forma independente**; vale por independência, não por contagem | Fusão/Conviction (SPEC-003, mecanismo) invocado pelo Manager Fase 2; nunca por skill (skills não cruzam matérias — FF-007) | FF-014, FF-027, FF-049, FF-059, FF-060, FF-062, FF-078, FF-115, FF-116, FF-118 |
| **CONF-D — entre conceitos de uma mesma escola no mesmo TF** | Ex.: OB + FVG + sweep no M5 | `confluence-smc`, `confluence-ict` (intra-M5) | FF-007, FF-016 |
| **CONF-E — confluência como pré-condição** (de OTE / de execução) | ICT só usa OTE / só executa se as confluências acima estiverem presentes | consumo pelo ICT do que outros mediram (não é medição nova) | FF-033, FF-083 |
| **CONF-F — "Fibonacci só em confluência"** (qualidade da evidência) | Nível de Fibonacci sozinho é evidência fraca; ganha valor só quando coincide com outra evidência | rótulo de qualidade (WF-V02) | FF-015, FF-078 |
| *(legado)* FCES §5 "dimensões da confluência" | Mistura estrutural, geométrica, temporal, **institucional** e **volume** num só motor | FCE — extinto; cruzaria matérias (proibido por FF-007) | FF-097, FF-099 |

`[INFERÊNCIA]` Não há uma contradição única: há **sete usos** sem glossário que os separe. A palavra sozinha não basta; toda Spec precisa dizer qual acepção usa.

---

## 4. Conflitos e lacunas

Autoridade (da maior para a menor): baseline/canon > ata/decisão (inclui WORKFLOW soberano) > Spec/governança > fonte histórica. "Toca" = o tratamento exigiria mexer nesse item.

| # | Conflito / lacuna | Lado A (autoridade) | Lado B (autoridade) | Veredito `[INFERÊNCIA]` | Toca baseline (CONST-01) / decisão aberta |
|---|---|---|---|---|---|
| **C-01** (a) | "Fibonacci valida, não cria" × "Fibonacci cria sub-hipótese" | FF-028 RULE-FB-001, FF-026, FF-037, FF-038 (NB); FF-093/FF-094 (FH — o "ADR-002" nunca foi homologado) | FF-002 (DV, Q-005), FF-045 SPEC-001 RULE-HH-001/HH-002 (NB baseline), FF-041, FF-104 | **Confirmado como conflito aparente + lacuna.** "Não cria **contagem/estrutura/bias**" e "cria **sub-hipótese** com `parent_id`" podem conviver — mas **nenhum documento define o que é uma sub-hipótese do Fibonacci**: o GEN-1 só produz validação (FF-080, FF-090, sem `parent_id`). FF-117 (ideia: "Elliott e Fibonacci constroem a estrutura") contraria RULE-FB-001 → descartar. FF-004 tem tensão interna (lista ICT entre os que criam sub e, na linha seguinte, nega), já resolvida por AGENTS §6.2. | Toca SPEC-001 (baseline) só se Andraus revogar o uso; Q-005 é FECHADA — não reabrir sem ele |
| **C-02** (b) | Fibonacci/Fractal na hierarquia e no fluxo, fora do pipeline do WORKFLOW | FF-001 INV-01 (DV); FF-025 CONSTITUTION, FF-058 PPQ-001 (NB canon); FF-073 ROADMAP fluxo (indicativo); FF-101, FF-102 (FH) | FF-012 WF-02..05 (DV soberano); FF-005/FF-006 ADR-CONFLUENCE (DV: Fibonacci e confluência fractal = skills **dentro** do Structural); FF-051..FF-054 SAS-001 (NB canon: Fibonacci e fractal são domínios do Structural) | **Confirmado, mas com leitura conciliadora.** GPR-001 PC-01 (FF-063) chama a hierarquia de "ordem de **autoridade** cognitiva", não de ordem de etapas despachadas. Duas fontes posteriores e homologadas (ADR-CONFLUENCE, 2026-09-26; SAS-001 baseline) põem Fibonacci/Fractal **dentro** do Estrutural — o que bate com o WORKFLOW. As fontes que pedem etapa separada são o diagrama da CONSTITUTION (pré-ADR), PPQ-001 "submissões" e as históricas. | P-11 "decidir depois" (DV); edição de WORKFLOW só por Andraus; WF-M01 ainda [INFERÊNCIA] |
| **C-03** (c) | Dimensões geométrica/fractal × leitura macro (estrutural+institucional) | FF-003 Q-008, FF-048 CCM-001 (baseline): 8D com geométrica e fractal | FF-013 WF-C01 (DV): macro = estrutural+institucional; FF-006 ADR: scores das 4 skills compõem o "Vetor de Convicção **Estrutural**"; FF-008 ADR §6: "revisar dimensões — Fractal muda de posição/nome" | **Confirmado + lacuna de dono.** O CCM-001 **não diz quem alimenta** cada dimensão; só as fontes GEN-1/históricas dizem (FF-088, FF-099). O pedido do ADR §6 (revisar a dimensão Fractal) não foi executado: o CCM-001 (posterior, baseline) manteve as 8. Na leitura macro, geométrica/fractal ficam fora ou chegam "embutidas" no estrutural — não está escrito. | **Toca CCM-001 (BASELINED) se alguém quiser mudar dimensões → proibido sem Andraus (CONST-01).** Toca WF-D03 e J-001 (ABERTAS) |
| **C-04** (d) | "Fibonacci Skill"/"Fractal Skill" × Classe/mecanismo | FF-019 I-001 (DV): Skill = Classe D; P fica no agente; corte exato → SPEC-025; FF-047 SPEC-002 (NB): skill não produz Evidência | FF-005/FF-006 ADR (DV) chama de "skill" `confluence-elliott` (que compara **hipóteses** entre TFs — julgamento, provável H/P); FF-095 (FH) "Fibonacci Skill / Fractal Skill"; FF-074 EUA-E23 classifica SPEC-011 como P/H | **Confirmado.** Cálculo de retração/extensão é candidato natural a Classe D (FF-077); comparar contagens entre graus é julgamento. Pela I-001, parte do que o ADR chama "skill" seria comportamento interno do agente, não Skill separada. Não há contradição de regra — há **nome** ("skill") que pode não coincidir com a Classe. | Critério da SPEC-025 (diferido por DV); RULE-MECH-01 é por BASpec. Não toca canon |
| **C-05** (e) | Timeframes/graus | FF-022/FF-023 CONSTITUTION, FF-032 RULE-EW-004, FF-058 PPQ-001 (canon): S1/D1/H4/H1/M5; FF-055 SAS-001 (canon): **D1→H4→H1→M15**; FF-007 ADR: MTF S1/D1/H4/H1 + M5; FF-037 CONFLICT-MAP: "Sinal contra o bias do D1" | FF-017 WF-T01/WF-R01 (DV soberano, provisório BL-026): tripla por tipo de trade, editável por missão (day = H4/H1/M15) | **Confirmado, com 4 lados.** Para day trade (contexto H4), "nunca contra o bias do D1" e "top-down começando no S1" ficam sem sentido literal. Há ainda confusão de vocabulário: FCES liga **grau de Elliott a um TF fixo** (Primário = D1, FF-096; `rag/smc` "H4 (grau Intermediate)") — grau de Elliott é tamanho da onda, não gráfico (RULE-SEM). | Toca SAS-001 e PPQ-001 (BASELINED — só errata, não proposta aqui); WF-R01 (Andraus); BL-026; N-001 (pesos por ativo) |
| **C-06** (novo) | Identidade do Fibonacci: agente "Fibonacci Validator" × duas skills do Structural | FF-042 AGENTS §3.2, FF-038 GLOSSARIO §2, FF-025 CONSTITUTION, FF-045 SPEC-001 (produtor autorizado), FF-050 SPEC-006 (`school=Fibonacci`) | FF-005/FF-006 ADR-CONFLUENCE + FF-039/FF-040 GLOSSARIO §2-bis (DV, 2026-09-26: Fibonacci vira `level-fibonacci-skill` + `confluence-fibonacci-skill` do Structural) | **Novo e central — é a raiz da P-11.** Se Fibonacci é skill, ele não produz Evidência nem hipótese (FF-047; INV-06) e o "Fibonacci Validator" produtor da SPEC-001 fica sem agente atrás. O ADR §6 mandou atualizar referências a `fibonacci-skill`, mas não citou o "Fibonacci Validator". Já apontado em 2026-09 (FF-103 CAN-009). | Toca SPEC-001 e SPEC-006 (baselines — errata, não proposta aqui) e AGENTS/GLOSSARIO (só Andraus) |
| **C-07** (novo) | "Confluência é interna à matéria" × confluências que cruzam matérias | FF-007/FF-009 (DV) | FF-033 RULE-ICT-004 (NB), FF-059 CEM-001 exemplo "Fibo, AO e estrutura", FF-097 FCES, FF-115/FF-118 (ID) | **Conflito aparente, resolvido por acepção:** CONF-A/B/D são intra-matéria (skills); CONF-C é inter-matéria e fica na Fusão/Fase 2; CONF-E é consumo. Falta só o glossário (§5 (i)). | Não toca canon |
| **C-08** (novo) | Contar confluências × independência | FF-014 WF-C02, FF-027, FF-060, FF-049 (DV/NB); FF-078 "Fib e Elliott medem parte da mesma" | FF-030 RULE-FB-003 "quanto maior a convergência … maior a qualidade", FF-023 P05, FF-087 "+15 pontos bônus" (GEN-1) | **Tensão parcial.** Níveis de Fibonacci saem dos pivôs do Elliott: não são independentes da dimensão estrutural; somar geométrica + estrutural sem desconto = dupla contagem. O mecanismo da SPEC-003 (CF-002) já trata; a regra de "mais TFs = melhor" precisa ser lida como "mais TFs **independentes**". Pontuação do GEN-1 → descartar. | J-001 (desconto/calibração, ABERTA) |
| **C-09** (novo) | Razão da onda 2: 76.4% × 78.6% | FF-029 RULE-FB-002 (NB): "50%, 61.8% ou 76.4%" | FF-053 SAS-001 (canon): retrações "… 61.8% / 78.6%"; FF-080 OTE 61.8–78.6 | **Divergência numérica.** 76.4% (=1−0.236) e 78.6% (=√0.618) são razões diferentes usadas no mercado; não sei qual é a intenção. | `[DECISÃO NECESSÁRIA]` na abertura da Spec de Fibonacci (PD-xx com pesquisa); RULES.md só por Andraus |
| **C-10** (novo) | Peso da Spec de Fibonacci | FF-043 atomic-spec §3: "ICT · Fibonacci MEDIUM D0–D5" | FF-070 ROADMAP SPEC-011: "HIGH · D0–D7" | **Divergência.** Precedente: a matriz já foi emendada para a SPEC-006 (DHR-SPEC006-PEND-001). Pela RULE-ECC-01, o peso é fixado na abertura. | atomic-spec (só Andraus) |
| **C-11** (novo) | Fractal sem produtor e sem dono | FF-001 (Fractal é camada da hierarquia) | FF-050/FF-020 (sem produtor de hipótese Fractal); FF-005 (FCE absorvido por skill) | **Lacuna.** "Fractal" é camada de autoridade, mas não é agente nem produtor. CKG-STRUCT-ORIGIN-001 está ABERTA na SPEC-006/BL-035, mas **não aparece** na linha "Decisões abertas ativas" do ROADMAP (Grep: só atas SPEC-006 e backlog) — possível dessincronia para o `check_doc_sync.py`. | CKG-STRUCT-ORIGIN-001 (aberta) |
| **C-12** (novo) | ICT bloqueado por "confluência fractal insuficiente" × gatilho do ICT | FF-033 RULE-ICT-006, RULE-002 ("hipótese aprovada pelo Conviction Engine") (NB) | FF-012/FF-013 WF-04/05: ICT dispara pelo alarme vindo da convicção macro (estrutural+institucional) | **Lacuna menor.** Não há leitura fractal explícita antes do ICT, salvo se embutida no estrutural. Some com a resposta à P-11. | WF-D03 (aberta) |
| **C-13** (novo) | Quem arbitra Elliott × Fibonacci | FF-031/FF-035 (NB): "Fibonacci informa, Elliott decide" | FF-082 GEN-1 synthesis: "Arbitragem de conflitos … Elliott×Fibonacci" | **Descartado:** GEN-1 sem autoridade normativa; vale a regra. | — |
| **C-14** (novo) | Três sentidos de "tempo" | FF-021 Q-A9: dimensão `temporal` = regime | FF-088 GEN-1: `temporal` = Killzone; FF-053/FF-105/FF-107: proporção de tempo das ondas (Fibonacci temporal); Spec de Tempo (DHR-SPEC008-001 P-2) = relógio/Killzone/alarme | **Risco de vocabulário.** O tempo das ondas (Fibonacci) não é assunto da Spec de Tempo; a dimensão `temporal` é regime (decidido). GEN-1 superado. | Não toca canon; RULE-SEM |
| **C-15** (novo) | Cabeçalho GEN-1 aponta sucessor errado | FF-080 `fibonacci.spec.md`: "SUPERSEDED_BY=SPEC-002" | FF-070 slot do Fibonacci = SPEC-011 | **Erro de citação (C07).** SPEC-002 é a Spec de Evidência. | Não toca canon |

---

## 5. Proposta de tratamento (tudo `[PROPOSTA]`; nada decidido; nada editado)

### (i) Glossário sugerido (entrada nova no `GLOSSARIO.md`, só por ordem de Andraus)

> **Confluência** — palavra com várias acepções; toda Spec DEVE dizer qual usa:
> - **Confluência entre graus (fractal):** contagens de graus diferentes contam a mesma história. Dono: Structural Agent (`confluence-elliott`, ADR-CONFLUENCE-001 v3).
> - **Cluster de Fibonacci:** níveis de Fibonacci que caem na mesma faixa de preço — dentro de uma estrutura (SAS-001 Domínio 2) ou entre timeframes (`confluence-fibonacci-skill`). Dono: Structural Agent.
> - **Confluência entre escolas:** escolas diferentes explicando o mesmo fato **de forma independente**; vale por independência, não por contagem (WF-C02). Feita na Fusão (SPEC-003), invocada pelo Manager — Fase 2; nunca por skill.
> - **Confluência dentro de uma escola:** conceitos da mesma escola no mesmo TF (ex.: `confluence-ict` no M5).
> - **"Fibonacci só em confluência" (WF-V02):** rótulo de qualidade — nível de Fibonacci sozinho é evidência fraca.
> - *Termo legado:* "Fractal Confluence Engine (FCE/FCES)" → `confluence-elliott`.

> **Fibonacci valida × cria** — **valida:** mede proporções da hipótese Elliott recebida e publica confirmação ou conflito geométrico; nunca descarta sozinho (RULE-FB-004). **Não cria:** contagem, estrutura, direção (bias) nem hipótese primária (RULE-FB-001; AGENTS §6.2). **Pode criar (Q-005):** sub-hipótese com `parent_id` — **conteúdo ainda não definido** `[DECISÃO NECESSÁRIA]`; sugestão a avaliar na Spec de Fibonacci: "zona projetada condicionada à primária" (ex.: alvo 1.618–2.618 se a primária for onda 3), refutável pelo preço.

> **Tempo** — distinguir: (a) relógio/Killzone/alarme (Spec de Tempo); (b) regime = dimensão `temporal` (Q-A9); (c) proporção de tempo entre ondas (Fibonacci temporal, SAS-001 Domínio 2).

### (ii) Matriz "quem faz o quê" — leitura proposta, com fonte

| Saída | Elliott (Structural) | Fibonacci | Fractal | SMC (Institutional) | ICT (Operational) | Manager |
|---|---|---|---|---|---|---|
| Hipótese primária/direcional | **cria** (Q-005; RULE-EW) | nunca (RULE-FB-001) | nunca (sem produtor, FF-050) | nunca (RULE-SM-003) | nunca (INV-02) | nunca |
| Sub-hipótese (`parent_id`) | — | **permitida** (Q-005, SPEC-001); conteúdo `[DECISÃO NECESSÁRIA]` | não (CKG-STRUCT-ORIGIN-001 aberta) | **cria** (Q-005) | nunca (INV-02); produz setup | nunca |
| Evidência (CEM-001) | produz (inclui "Fibonacci Evidence"/"Fractal Evidence", SAS-001 Cap.4) | **se** for agente: produz; **se** for skill: só Observação (SPEC-002 EH-T02) `[DECISÃO NECESSÁRIA — C-06]` | idem (skill `confluence-elliott` → Observação) | produz | produz setup operacional | não produz evidência de mercado |
| Validação | autovalidação/refutação Tipo B/C (SAS-001) | valida proporções; conflito vai ao Elliott (RULE-FB-004) | coerência entre graus (Elliott decide recontagem, CONFLICT-MAP) | confirma/enfraquece (RULE-SM-003) | — | — |
| Contribuição à convicção | dimensão estrutural | dimensão geométrica — **dono não fixado no CCM-001** `[DECISÃO NECESSÁRIA]` | dimensão fractal — idem | institucional (+ volume por WF-C03) | operacional | invoca o mecanismo 2x (WF-C01); decide envio |
| Despacho (roteiro) | nó 1 (WF-02) | posto 2 — **sem nó** (P-11) | posto 3 — **sem nó** (P-11) | nó 4 condicional (WF-03) | nó 5 (WF-05) | despacha só o que está no grafo |

`[INFERÊNCIA]` Se a resposta à P-11 for "dentro do Elliott" (ver Q1), as colunas Fibonacci e Fractal passam a ser **capacidades do Structural Agent** (como dizem ADR-CONFLUENCE e SAS-001), e a linha "Evidência" se resolve: quem publica é o Structural; as skills só calculam.

### (iii) Destino de cada ideia histórica (com motivo)

| Ideia (ID) | Destino proposto | Motivo |
|---|---|---|
| IDEIA 021 tempo × preço (FF-105); IDEIA 022 proporcionalidade (FF-106) | **Spec de Fibonacci (slot SPEC-011)** | Já é "Relações Temporais" do SAS-001 Domínio 2; **não** é a Spec de Tempo (acepção diferente, C-14) |
| IDEIA 023 índice de simetria (FF-107); SSE (FF-113); IDEIA 031 elasticidade (FF-112) | **SPEC-010 (Structural)** | O slot já lista "simetria", "continuidade fractal", "elasticidade" (FF-071) |
| IDEIA 027 continuidade (FF-108), 028 ruptura (FF-109) | **SPEC-010** (leitura) + **Spec de Fibonacci/Fractal** (medida) | Leitura entre graus é do Structural (ADR); medida formal é o "componente especializado" do SAS-001 |
| IDEIA 029 peso por TF (FF-110) | **Mecanismo na Spec de Fractal; valores → N-001/J-001 via backtest (SPEC-018, BL-032)** | Peso é número; sem backtest seria falsa precisão (CC-09) |
| IDEIA 030 herança hierárquica (FF-111); Herança fractal das hipóteses (FF-114) | **Já absorvida em parte** (SPEC-001 "Herança Fractal Operacional"); recálculo automático → SPEC-009 (estado, G-001 aberta) | Não duplicar o que está em baseline |
| IDEIA 051 confluência estrutural-institucional (FF-115); INE (FF-116); BLIND SPOT 018 (FF-118) | **Glossário (i) + SPEC-003 (já tem WF-C02/CF-002) + SPEC-014 (Fase 2)**; INE → SPEC-012 | É confluência entre escolas: não pode ser skill (ADR: skills não cruzam matérias) |
| "Elliott e Fibonacci constroem a estrutura" (FF-117) | **Descartar** | Contraria RULE-FB-001 e CONFLICT-MAP |
| FCES grau = TF fixo (FF-096) | **Descartar como tabela fixa**; substituir por WF-T01 (editável por missão) | Contraria o WORKFLOW soberano; mistura grau de Elliott com gráfico |
| FCES §5 dimensões cruzando matérias (FF-097) | **Descartar** | Proibido pelo ADR-CONFLUENCE (FF-007) |
| FCES §11 memória fractal por ativo | **SPEC-017 (Pattern Memory)** | Calibração por ativo, nunca regra (P07) |
| Pontuação "+15 bônus" (FF-087) | **Descartar** | Contagem, contra WF-C02; números sem base (J-001) |
| Skills SPEC-027/028 (FF-072) | **Só se a SPEC-025 mostrar Classe D** (I-001) | Evitar criar skill por nome |

### (iv) O que muda — e o que NÃO muda

**Plan da SPEC-008 (candidato).**
- **Não muda:** o roteiro como dado versionado; postos 1..5 de INV-01; a guarda posto(u) < posto(v); a lista fechada de condições; a FSM; Killzone, alarme, WF-C01 2x; J-001/N-001. O mecanismo da RULE-MDC-002 já aceita qualquer resposta.
- **Se Andraus escolher "dentro do Elliott" (Q1, recomendada):** a versão 1 do roteiro (DN-3) fica como está; mudam **só textos** do Plan: RULE-MDC-002 (e) e a linha P-11 da tabela passam a registrar "Fibonacci/Fractal dentro do nó ESTRUTURAL; postos 2/3 reservados". Isso **muda o registro da P-11** de "decidir depois" para decidida — ato de Andraus registrado em ata.
- **Se escolher "etapa separada":** precisa de (1) edição do WORKFLOW por Andraus (novo passo entre WF-02 e WF-03); (2) uma **condição nova** para a aresta Fibonacci → SMC — o Cenário-MDC-T05 reaproveita `OPORTUNIDADE_SIM`, mas o Fibonacci não publica "oportunidade", e condição fora da lista fechada exige **errata** (RULE-MDC-002 (e)); (3) decidir se a leitura macro passa a incluir geométrica/fractal (WF-C01 — toca WF-D03 aberta).
- **Se mantiver "decidir depois":** a DN-3 como está é coerente; só falta a confirmação dele.

**Spec de Tempo (candidata SPEC-050).** Não muda. Só recomendo uma nota de vocabulário: "tempo" aqui = relógio/Killzone/alarme; proporção de tempo entre ondas é da Spec de Fibonacci; dimensão `temporal` é regime (C-14). Os TFs da missão (WF-T01) continuam parâmetro.

### (v) Edições que só Andraus pode fazer / que exigiriam errata em baseline (só listagem)

- **Só Andraus (edição direta):** `WORKFLOW.md` (passo novo; WF-C01 macro; WF-R01 × S1..M5; WF-M01 confirmar); `AGENTS.md` §3.2 e `GLOSSARIO.md` §2 (Fibonacci Validator × skills; glossário de acepções); `atomic-spec.md` §3 (MEDIUM × HIGH); `governance/RULES.md` (RULE-FB-002 76.4/78.6; RULE-EW-004 top-down fixo); `CONFLICT-MAP.md` ("bias do D1"); `CONSTITUTION.md` (diagrama com Fibonacci Validator despachado); linha de decisões abertas do ROADMAP (CKG-STRUCT-ORIGIN-001).
- **Exigiriam errata em baseline (não proponho editar):** SPEC-001 RULE-HH-001 (produtores) e SPEC-006 (`school`) — se o Fibonacci deixar de ser agente; SAS-001 §5.10/§7.13 (árvore D1→H4→H1→M15); PPQ-001 5W2H "grau fractal (S1/D1/H4/H1/M5)".
- **Não editar:** CCM-001 — o dono de cada dimensão deve ser dito nas Specs dos analistas (SPEC-010/011/012/013) e na Fase 2 (SPEC-014), **não** no canônico.
- **Higiene sem autoridade normativa (GEN-1):** cabeçalho `SUPERSEDED_BY=SPEC-002` em `specs/fibonacci.spec.md` (C-15).

### (vi) Perguntas a Andraus (linguagem de trader; recomendação em 1º lugar)

1. **Fibonacci e a leitura entre tempos gráficos: são parte do trabalho do analista de Elliott, ou um analista separado que o Manager chama depois dele?**
   - **(Recomendada) Dentro do Elliott:** o Elliott mede as proporções e confere os graus antes de publicar uma análise só. É o que já dizem a sua decisão de 26/09 (ADR-CONFLUENCE: Fibonacci e confluência viram ferramentas do Estrutural) e o SAS-001; o WORKFLOW não muda; o roteiro v1 pode ser confirmado; os postos 2/3 ficam reservados. *Obs.: diverge da recomendação da abertura (C com A provável), que se apoiava na sub-hipótese do Fibonacci — ver pergunta 2.*
   - Separado: o Manager chama Fibonacci/Fractal depois do Elliott e antes do SMC (edição sua no WORKFLOW + condição nova no roteiro).
   - Manter "decidir depois" (confirma a DN-3 como está).
   - **Adiar.**
2. **O Fibonacci pode lançar uma ideia própria pendurada no Elliott (ex.: "se é onda 3, o alvo é a zona 1.618–2.618"), ou só confere as medidas?**
   - **(Recomendada) Por ora, só confere e publica zonas como evidência;** a permissão de sub-hipótese (Q-005) fica valendo, mas sem uso até a Spec de Fibonacci definir o que ela é. Nada muda na SPEC-001.
   - Pode lançar sub-ideia de zona desde já (a Spec de Fibonacci define o formato).
   - **Adiar.**
3. **A primeira leitura de convicção (a que arma o alarme) deve olhar também geometria e alinhamento entre tempos gráficos?**
   - **(Recomendada) Não mexer agora:** continua estrutural + institucional; se Fibonacci/graus ficarem dentro do Elliott, entram pela nota estrutural; o resto fica "sem dado". Fórmula e pesos seguem em aberto (J-001/WF-D03).
   - Sim, incluir geométrica e fractal na leitura macro (edição sua no WF-C01).
   - **Adiar.**
4. **Tempos gráficos: a sua tabela por tipo de trade (com troca por missão) vale mais que a lista fixa S1/D1/H4/H1/M5 dos documentos antigos?**
   - **(Recomendada) Sim:** a tabela editável manda; S1..M5 vira exemplo; as correções dos documentos fixos (SAS-001, PPQ-001, RULE-EW-004, "bias do D1") ficam listadas para quando você quiser.
   - Não: manter S1/D1/H4/H1/M5 fixo e ajustar a tabela.
   - **Adiar.**
5. **Registrar no glossário os sentidos de "confluência" (entre graus, cluster de Fibonacci, entre escolas, dentro da escola, "Fibonacci só em confluência")?**
   - **(Recomendada) Sim**, com o texto do §5 (i) — evita que cada Spec use a palavra de um jeito.
   - Não; cada Spec declara a sua.
   - **Adiar.**

---

## 6. Autopré-check (curto) e limites

- [x] ROADMAP.md e atomic-spec.md lidos nos pontos pertinentes (decisões abertas/fechadas; §3 matriz; CC-01; INV-01).
- [x] Nenhum outro arquivo editado; só este arquivo novo.
- [x] CONS-01: nenhuma decisão aberta tratada como fechada — J-001, N-001, WF-D03, CKG-STRUCT-ORIGIN-001, SPEC-015-SCOPE e P-11/P-13 aparecem como abertas/"decidir depois"; toda escolha está em pergunta.
- [x] CONST-01: nenhum canônico redefinido; CCM-001, SAS-001, PPQ-001, CEM-001, CHM-001 só citados; erratas apenas listadas.
- [x] TRACE-06: ENGENHARIA-GERAL, KERNEL-V2, AUDITORIA-ideias, GEN-1 e `rag/` classificados como FH/ID, nunca norma; "ADR-002" declarado inexistente como ADR homologado.
- [x] WORKFLOW citado só por ID (WF-xx); nenhuma alteração proposta como feita.
- [x] Web não usada (inventário interno).
- [x] Contagem por tipo conferida contra as tabelas (21/43/40/14/7 = 125).
- [ ] Não rodado (sem Bash): `build_map.py --check`, `check_refs.py`, `check_doc_sync.py` — **o Orquestrador deve rodar**.
- **Limites:** cobertura parcial dos 902 acertos (ver §1.3); varredura global própria de `retra|extens|projeç|grau|multi-timeframe` não feita; trechos literais conferidos na leitura, mas não por script de comparação de string; status de "baseline" de CONSTITUTION, RULES.md e CONFLICT-MAP tratado como norma de governança vigente (não canônico), conforme uso no repositório.
