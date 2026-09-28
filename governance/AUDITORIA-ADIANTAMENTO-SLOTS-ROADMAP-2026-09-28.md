# AUDITORIA DE ADIANTAMENTO DE ABERTURA — Slots Indicativos do ROADMAP

| Campo | Valor |
|---|---|
| Documento | AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28 |
| Tipo | Auditoria / Proposta (**NÃO-normativa**; NÃO abre Spec; NÃO homologa; NÃO renumera; NÃO fecha decisão) |
| Autor | Especificador SOT (souza.merchan@gmail.com como identificação de autoria) |
| Data | 2026-09-28 |
| Objeto | Classificar todo slot indicativo do ROADMAP **ainda não aberto** por candidatura de **adiantamento de ABERTURA** (Dossiê de Pesquisa + proposta — não a homologação da Spec), sob critério **4Es × Risco**. |
| Excluídos do escopo (já homologados) | SPEC-001, SPEC-019, SPEC-020 (núcleo A), SPEC-021, SPEC-046. |
| Complementa | `backlog/ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md` (priorização de itens do RMR-001, entregue hoje). |
| Fontes | `ROADMAP.md`, `governance/RULES.md`, `atomic-spec.md` (§5 F.1–F.4, §9 Skill×Engine, §10.6/§10.7, §15), `backlog/RMR-001_Painel_Backlog.md`, `backlog/ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md`. |
| Vínculo ao ROADMAP | `ROADMAP.md` §25-ter (Análises de priorização e adiantamento). **Subordinada** à ordem de prioridade do §21 e ao "próximo trabalho autorizado" do §25/§25-bis — não os substitui nem os condiciona (CONS-01/INV-09). Consultar §25-ter para o status de execução corrente antes de tratar qualquer linha abaixo como já encaminhada. |

> **Nota de proveniência (transparência).** Este mandato chegou colado por Andraus, apresentando-se como emitido por uma entidade **"AEH (HOC-003 v3.4)"** com cláusula de retenção **"I-AEH-11"**. Verificação: "AEH"/"I-AEH-11" **não existem** em `AGENTS.md` §3 (que lista apenas Especificador e Revisor) nem em nenhum invariante ativo (só em ADR legado desativado). Andraus decidiu **ignorar a cláusula de retenção**; o resultado é entregue direto, sem retenção e sem destinatário "AEH". Registro feito por honestidade metodológica (RULE-MET-01). Isto não altera o conteúdo técnico do mandato, que é acatado.

> **Status epistemológico (TRACE-06).** O estado de abertura de cada slot é **[FATO NORMATIVO]** (verificado em `ROADMAP.md` §26 e "Estado atual"). A classificação Bloco/Risco/Condições é **[INFERÊNCIA]** derivada das fontes citadas. Toda recomendação ADIANTAR/MANTER é **[PROPOSTA]** — só Andraus homologa (INV-09). Nenhuma linha fecha decisão aberta (CONS-01), renumera/funde/descarta slot (INV-07) ou trata slot como Spec (RULE-ECC-01).

---

## 0. Método de classificação

**Bloco S (Spec-time).** Ancorado em `atomic-spec.md` §5 (**F.1 Feedforward** — autoridade/orientação; **F.4 Evaluation** — meta-harness). São padrões de gate, protocolos epistêmicos, critérios de avaliação, taxonomias e constraints que o **próprio Especificador/Revisor aplicam ao redigir/auditar outras Specs**. Ganham Economicidade/Eficiência se abertos antes das Specs dependentes. Precedente de abertura fora de ordem: **SPEC-046** (caching de spec-time) e a FASE GOV (SPEC-019/020/021 — meta-harness, abertas antes de SPEC-002).

**Bloco R (Runtime/agentes).** Ancorado em `atomic-spec.md` §9 (Engine/Agent stateful, produz Evidência) e §5 (F.2 Guardrails/F.3 Feedback em operação). São comportamentos de agentes cognitivos (estrutural, institucional, operacional, manager, risco) ou infraestrutura de execução (Blackboard, Event Bus, Scheduler, KG, tooling runtime). Obedecem à ordem de dependência do ROADMAP §21; adiantar cria risco MÉDIO/CRÍTICO.

**Critérios (C-ATx).** C-AT1 (Spec-time direto → Economicidade); C-AT2 (ponderação universal: pesos/limiares/taxonomias que informam múltiplos slots → Eficácia); C-AT3 (sem dependência bloqueante confirmada: depende do slot upstream existir, não do seu resultado → Eficiência); C-AT4 (risco de divergência crescente: cada Spec homologada sem o slot aumenta custo de reconciliação → Efetividade).

**Níveis de risco.** NULO (só análise/proposta retida) · BAIXO (Dossiê parcial/rascunho não-normativo) · MÉDIO (depende de decisão aberta não resolvível ou de resultado de Spec upstream) · CRÍTICO (exige Spec upstream homologada; dependência circular ou reescrita garantida).

**Regra de corte (do mandato).** Só slots com risco **NULO** ou **BAIXO** são recomendados para **ADIANTAR**. MÉDIO/CRÍTICO → **MANTER** (aguardam ordem nominal).

**Ordem protegida (invariante do mandato).** **SPEC-002 é o próximo passo regular.** Nenhuma recomendação aqui bloqueia, atrasa ou condiciona SPEC-002. Adiantamentos são **linhas paralelas** (modelo SPEC-046).

---

## PARTE 1 — Classificação por slot

### FASE 1 — Núcleo Cognitivo

**SPEC-002 — Evidence & Evidence Provenance Harness.**
- **Bloco:** R (predominante) + S (marginal). O objeto "Evidência" é produzido por Engines/Agentes em runtime sobre **CEM-001** (baselined, disponível — reduz risco do Dossiê). A disciplina de *provenance*/classificação de evidência tem um resíduo S (informa como o próprio Especificador raciocina sobre evidência), mas o núcleo é contrato de objeto runtime.
- **Risco:** **BAIXO** — CEM-001 baselined (não redefinir, CONST-01); nenhuma decisão aberta bloqueia a camada de provenance (J-001 é downstream, na convicção). MC-EXP-001 (BL-011) disponível como fonte, embora seu gatilho próprio seja SPEC-006/009.
- **Condições:** C-AT3 satisfeito (CEM-001 existe). C-AT4 alto (é fundação de quase tudo).
- **Recomendação:** **ABRIR pela ordem regular** — *não é adiantamento*. Por restrição 2 do mandato: **a abertura completa de SPEC-002 já é o adiantamento máximo possível** deste slot; não há parte S isolável que justifique abertura parcial separada. É o "próximo trabalho autorizado" (ROADMAP §25). **[PROPOSTA]**

**SPEC-003 — Conviction Vector, Evidence Fusion & Conviction Engine.**
- **Bloco:** R. Engine de runtime; redige o CCM-001.
- **Risco:** **CRÍTICO** — é o próprio conteúdo de **J-001** (aberto) + **N-001** (aberto); trava E3 do gate Convicção→Decisão; fórmula/pesos/limiares definitivos exigem backtest. Adiantar = fechar J-001 sem base (proibido, CONS-01; espelha BL-004).
- **Condições:** nenhuma satisfeita para adiantar.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 2 — Memória de Trabalho e Comunicação

**SPEC-004 — Cognitive Blackboard Protocol.**
- **Bloco:** R (memória de trabalho runtime).
- **Risco:** **MÉDIO** — depende de **M-001** (aberto: estados do Blackboard para objetos não-hipótese). Espelha BL-003 (persistência física bloqueada por SPEC-004).
- **Condições:** C-AT4 alto, mas bloqueado por M-001.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-005 — Cognitive Event Bus.**
- **Bloco:** R (infra de transporte runtime).
- **Risco:** **MÉDIO** — semântica depende de SPEC-004 existir (`Blackboard guarda estado; Event Bus transporta mudanças`). Sem o Blackboard definido, o contrato de eventos fica sem contraparte.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 3 — Memória Semântica e RAG

**SPEC-006 — Cognitive Knowledge Graph.**
- **Bloco:** R (memória permanente runtime).
- **Risco:** **MÉDIO/CRÍTICO** — resolve **H-001** (aberto: grafo real vs. estrutura em memória). MC-RAG-001/MC-EXP-001 disponíveis como fonte (reduzem risco do Dossiê, não a dependência estrutural).
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-007 — RAG / WikiRAG / Knowledge Formation Harness.**
- **Bloco:** R (predominante) + S (marginal: as regras `documento recuperado ≠ verdade` / `candidato ≠ publicado` são disciplina epistêmica, mas já cobertas por TRACE-06/RULE-MET/RULE-EPI vigentes — pouco delta S isolável).
- **Risco:** **CRÍTICO** — depende de SPEC-006 (KG) homologada. **MC-RAG-001 (BL-010) disponível** como fonte de requisitos. Fecha a dimensão B `RAG faithfulness` da SPEC-020 (BL-017) — mas só quando SPEC-007 entra em redação (não antes).
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 4 — Cognição e Escalonamento

**SPEC-008 — Cognitive Scheduler.**
- **Bloco:** R (orquestração de raciocínio runtime).
- **Risco:** **CRÍTICO** — depende do kernel cognitivo (Blackboard/Event Bus/State) especificado.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-009 — Cognitive State & Persistence Model.**
- **Bloco:** R (estado/persistência runtime).
- **Risco:** **MÉDIO** — resolve **G-001** (aberto: schema do estado persistente por agente).
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 5 — Agentes Analíticos

**SPEC-010 (Structural/Elliott) · SPEC-011 (Fibonacci/Fractal) · SPEC-012 (Institutional/SMC) · SPEC-013 (Execution/ICT).**
- **Bloco:** R (agentes cognitivos — coração da Trilha B runtime).
- **Risco:** **CRÍTICO** — dependem do kernel cognitivo inteiro (FASES 1–4) + hierarquia CC-01. Gatilho de BL-001 (VPD) aponta para `spec:SPEC-010..014 em redação`. SPEC-013 carrega o invariante "ICT não cria hipótese".
- **Recomendação:** **MANTER** (as quatro). **[PROPOSTA]**

### FASE 6 — Síntese, Missão e Decisão

**SPEC-014 — Synthesis Agent.**
- **Bloco:** R (agente).
- **Risco:** **CRÍTICO** — só após **J-001** (Conviction). B-001 já fechada (Conviction≠Synthesis). Fecha a dimensão B `decision traceability` da SPEC-020 (BL-017). Gatilho `milestone:FASE 6 concluída` é a 2ª condição do BL-018 (Risk Agent).
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-015 — Mission Engine & Mission Lifecycle.**
- **Bloco:** R.
- **Risco:** **CRÍTICO** — depende de SPEC-014.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-016 — Trading Mission Package (TMP) — REPURPOSADA.**
- **Bloco:** R (contrato de handoff interno Synthesis→Risk; snapshot imutável runtime).
- **Risco:** **CRÍTICO** — escopo efetiva-se quando a família RISK for autorizada (EUA-E19a/EUA-E20); ancora INV-RISK-00. Depende de SPEC-014.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 7 — Memória e Aprendizado

**SPEC-017 — Pattern Memory.**
- **Bloco:** R (memória episódica runtime; win rate, RR, amostra).
- **Risco:** **MÉDIO/CRÍTICO** — depende de agentes/missões produzirem episódios; estatística de convicção toca J-001.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-018 — Learning & Knowledge Formation Governance.**
- **Bloco:** R (governança de **runtime** — ciclo Extração→…→Produção). Apesar do rótulo "governança", é governança de aprendizado em operação, não spec-time (a spec-time foi resolvida na SPEC-019/L-001).
- **Risco:** **MÉDIO/CRÍTICO** — resolve **K-001** (aberto). Gatilho de ativação de BL-013 (MC-GOV) e BL-015 (MC-LRN). MC-LRN/GOV disponíveis como fonte.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 8 — Teste Cognitivo Integrado

**SPEC-022 — Cognitive Test & Adversarial Test Specification.**
- **Bloco:** **S + R** — e é o **candidato mais forte a Bloco S isolável** fora da FASE GOV. A parte **R** (executar os testes contra os agentes: hipótese concorrente, conflito Elliott×SMC, corrupção de memória, evento duplicado…) exige os agentes das FASES 5/6. A parte **S** é uma **taxonomia de modos-de-falha cognitiva** (16 cenários nomeados no ROADMAP §13) + protocolo de teste adversarial — um artefato de spec-time que o Especificador/Revisor aplicam ao avaliar SPEC-002+ (parente direto da 8ª lente `robustness/adversarial` da SPEC-020 e do §7-bis/D8).
- **Risco (parte S):** **BAIXO** — a taxonomia é rascunho não-normativo, sem dependência de resultado de Spec upstream; não fecha decisão aberta. **Risco (parte R):** **CRÍTICO** (aguarda agentes).
- **Condições (parte S):** **C-AT2** (taxonomia de ponderação universal — informa a cobertura adversarial de todos os agentes das FASES 5/6 → Eficácia) e **C-AT4** (cada agente redigido sem catálogo compartilhado de falhas diverge na cobertura adversarial → custo de reconciliação crescente). C-AT3 satisfeito (não depende de resultado, só de existir método — o método D8/§7-bis já existe).
- **Recomendação:** **ADIANTAR (parcial, parte S)** — candidato a **linha paralela modelo SPEC-046**: produzir Dossiê de Pesquisa + proposta de abertura restrita ao **catálogo adversarial/taxonomia de modos-de-falha como referência de spec-time não-normativa**, deixando a suíte executável (R) para quando os agentes existirem. Ressalva de Economicidade (PB-04/RULE-MECH-02): confirmar no Dossiê o *delta real* sobre o que SPEC-020 (lente 8) + §7-bis + RULE-EV-04 já cobrem, para não duplicar. Parte R: **MANTER**. **[PROPOSTA]**

### FASE 9 — Integração Cognitiva

**SPEC-023 — Cognitive Orchestrator.**
- **Bloco:** R (coordenação runtime).
- **Risco:** **CRÍTICO** — só após Scheduler+Blackboard+Event Bus+Agents+Mission+Conviction.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-024 — Meta Cognitive Supervisor.**
- **Bloco:** R (supervisor runtime — observa qualidade do raciocínio, viés, tokens, divergência entre agentes). Seus critérios ecoam a avaliação da SPEC-020, mas o objeto é um agente supervisor em operação.
- **Risco:** **CRÍTICO** — precisa de agentes em operação para supervisionar.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 10 — Skills

**SPEC-025 — Skill Development Specification.**
- **Bloco:** **S + R** — tem um núcleo S atraente (plataforma/template/certificação/versionamento/governança de Skills = metodologia de spec-time que o Especificador aplica ao redigir specs de Skill, análogo à intenção meta-harness da FASE GOV).
- **Risco:** **MÉDIO** — resolve **I-001** (aberto: "Skills como unidades formais separadas?"), e o **R-ARCH** (Skill-vs-agente) está diferido a esta Spec (BL-016). A questão definitória (I-001) governa se as Skills existem como unidade formal — sem ela, o template não tem objeto estável. O sliver S (esqueleto de template de Skill-spec) é conceitualmente isolável, mas depende da decisão I-001 para não nascer obsoleto.
- **Condições:** C-AT1/C-AT2 atrativos, **anulados pela dependência de I-001** (decisão aberta não resolvível nesta auditoria).
- **Recomendação:** **MANTER** (risco MÉDIO → corte). Registro: se Andraus resolver I-001, o sliver S de SPEC-025 sobe a candidato BAIXO de adiantamento parcial. **[PROPOSTA]**

### FASE 11 — Skills Analíticas

**SPEC-026 (Elliott) · 027 (Fibonacci) · 028 (Fractal/Confluence) · 029 (Liquidity) · 030 (BOS/CHOCH/MSS) · 031 (FVG/Order Block) · 032 (Volume) · 033 (AO/Divergence) · 034 (Trend/Channel) · 035 (ICT Execution) · 036 (Market Regime) · 037 (Volatility/Context).**
- **Escopo:** *escopo não detalhado no ROADMAP* (§16 lista apenas os títulos) — **auditoria de conteúdo inconclusiva por slot**; classificação estrutural mesmo assim:
- **Bloco:** R (Skills = competências runtime).
- **Risco:** **CRÍTICO** — "somente após SPEC-025" + dependência de I-001 + dos agentes. 12 slots.
- **Recomendação:** **MANTER** (todos). **[PROPOSTA]**

### FASE 12 — Ferramentas e Analytical Tooling

**SPEC-038 — Trading Analysis Tool Harness.**
- **Bloco:** R (predominante: contrato de ferramentas runtime — TradingView/Pine/OHLC) + S marginal (o esquema declarativo `Finalidade→Input→Output→Precisão→…` é um template, mas serve objetos runtime).
- **Risco:** **CRÍTICO/MÉDIO** — fecha a dimensão B `tool correctness` da SPEC-020 (BL-017), mas só na sua redação; depende dos agentes que consomem ferramentas.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-039 — Tool Selection & Tool Governance.**
- **Bloco:** R. **Risco:** **CRÍTICO** — depende de SPEC-038.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 13 — Observabilidade e Auditoria

**SPEC-040 — Cognitive Observability.**
- **Bloco:** R (tracing de runtime end-to-end). **Risco:** **CRÍTICO** — precisa do fluxo cognitivo existir para observar.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-041 — Cognitive Audit & Decision Reconstruction.**
- **Bloco:** R (predominante: reconstrói decisões runtime, D9) + S marginal (critérios de auditabilidade ecoam RULE-HG-08/D9, já vigentes).
- **Risco:** **CRÍTICO** — não há decisão runtime a reconstruir antes do fluxo existir.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 14 — Harness de Produção

**SPEC-042 — Runtime Guardrails.**
- **Bloco:** R (guardrails em operação — F.2). **Risco:** **CRÍTICO** — objeto de runtime; componente do caminho de leitura SPEC-045-RUNTIME-001 (aberto).
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-043 — Context Window & Context Integrity Harness.**
- **Bloco:** R (integridade de contexto em runtime). Análogo runtime da SPEC-046 (caching de spec-time, já homologada) — mas para os agentes cognitivos, não para o Especificador/Revisor.
- **Risco:** **CRÍTICO** — depende dos agentes/fluxo runtime.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

**SPEC-044 — Hallucination Detection & Integrity Harness.**
- **Bloco:** R (detector runtime) + S marginal (a taxonomia de tipos de alucinação já está coberta por TRACE-06/RULE-MET-01/lente `hallucination` da SPEC-020 — pouco delta S novo).
- **Risco:** **CRÍTICO** — o detector opera sobre saídas de agentes runtime.
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### FASE 15 — Integração Final

**SPEC-045 — SOT End-to-End Cognitive Flow.**
- **Bloco:** R (integração de todo o fluxo runtime).
- **Risco:** **CRÍTICO** — depende de todas as anteriores; carrega a decisão aberta **SPEC-045-RUNTIME-001** (caminho de leitura em runtime → baseline só nesta Spec).
- **Recomendação:** **MANTER**. **[PROPOSTA]**

### Fora da faixa 002–045

**SPEC-047 (reservado) — Runtime Cognitive Caching Harness (Grupo A).**
- **Escopo:** *não detalhado* — placeholder de rastreabilidade (ROADMAP §26; BL-024 faseamento). **Auditoria inconclusiva por escopo.**
- **Bloco:** R (agentes cognitivos Grupo A, regidos por CHM-001/CEM-001).
- **Risco:** **CRÍTICO** — deliberadamente adiado: depende de SPEC-002/010–014 existirem; sem número atribuído.
- **Recomendação:** **MANTER** (placeholder). **[PROPOSTA]**

---

## PARTE 2 — Tabela-resumo (ordenada por prioridade: maior ganho 4Es / menor risco primeiro)

| # | Slot | Nome | Bloco | Risco | Condições (C-ATx) | Recomendação | Escopo antecipável |
|---|---|---|---|---|---|---|---|
| 1 | SPEC-022 | Cognitive/Adversarial Test Spec | **S**+R | **BAIXO** (S) / CRÍTICO (R) | C-AT2, C-AT4, C-AT3 | **ADIANTAR (parte S)** | Taxonomia de modos-de-falha cognitiva + protocolo adversarial como referência de spec-time não-normativa (linha paralela SPEC-046); suíte executável fica para os agentes |
| 2 | SPEC-002 | Evidence & Provenance | R(+s) | **BAIXO** | C-AT3, C-AT4 | **ABRIR (ordem regular)** | Abertura completa = adiantamento máximo; sem parte S isolável separada. É o próximo trabalho autorizado |
| 3 | SPEC-025 | Skill Development Spec | **S**+R | **MÉDIO** | C-AT1/C-AT2 anulados por I-001 | **MANTER** | Sliver S (template Skill-spec) só sobe a candidato se I-001 for resolvida |
| 4 | SPEC-009 | Cognitive State & Persistence | R | **MÉDIO** | — (G-001 aberto) | MANTER | — |
| 5 | SPEC-004 | Cognitive Blackboard | R | **MÉDIO** | — (M-001 aberto) | MANTER | — |
| 6 | SPEC-005 | Cognitive Event Bus | R | **MÉDIO** | — (depende SPEC-004) | MANTER | — |
| 7 | SPEC-006 | Knowledge Graph | R | **MÉDIO/CRÍTICO** | — (H-001 aberto) | MANTER | — |
| 8 | SPEC-018 | Learning Governance (runtime) | R | **MÉDIO/CRÍTICO** | — (K-001 aberto) | MANTER | — |
| 9 | SPEC-017 | Pattern Memory | R | **MÉDIO/CRÍTICO** | — | MANTER | — |
| 10 | SPEC-003 | Conviction Vector/Engine | R | **CRÍTICO** | — (J-001, N-001) | MANTER | — |
| 11 | SPEC-007 | RAG / Knowledge Formation | R(+s) | **CRÍTICO** | — (SPEC-006) | MANTER | — |
| 12 | SPEC-008 | Cognitive Scheduler | R | **CRÍTICO** | — (kernel) | MANTER | — |
| 13 | SPEC-010 | Structural / Elliott | R | **CRÍTICO** | — | MANTER | — |
| 14 | SPEC-011 | Fibonacci / Fractal | R | **CRÍTICO** | — | MANTER | — |
| 15 | SPEC-012 | Institutional / SMC | R | **CRÍTICO** | — | MANTER | — |
| 16 | SPEC-013 | Execution / ICT | R | **CRÍTICO** | — | MANTER | — |
| 17 | SPEC-014 | Synthesis Agent | R | **CRÍTICO** | — (J-001) | MANTER | — |
| 18 | SPEC-015 | Mission Engine | R | **CRÍTICO** | — (SPEC-014) | MANTER | — |
| 19 | SPEC-016 | Trading Mission Package | R | **CRÍTICO** | — (SPEC-014; EUA-E20) | MANTER | — |
| 20 | SPEC-023 | Cognitive Orchestrator | R | **CRÍTICO** | — | MANTER | — |
| 21 | SPEC-024 | Meta Cognitive Supervisor | R | **CRÍTICO** | — | MANTER | — |
| 22 | SPEC-038 | Tool Harness | R(+s) | **CRÍTICO/MÉDIO** | — | MANTER | — |
| 23 | SPEC-039 | Tool Selection/Governance | R | **CRÍTICO** | — (SPEC-038) | MANTER | — |
| 24 | SPEC-040 | Cognitive Observability | R | **CRÍTICO** | — | MANTER | — |
| 25 | SPEC-041 | Audit & Decision Reconstruction | R(+s) | **CRÍTICO** | — | MANTER | — |
| 26 | SPEC-042 | Runtime Guardrails | R | **CRÍTICO** | — | MANTER | — |
| 27 | SPEC-043 | Context Integrity Harness | R | **CRÍTICO** | — | MANTER | — |
| 28 | SPEC-044 | Hallucination Detection | R(+s) | **CRÍTICO** | — | MANTER | — |
| 29 | SPEC-045 | End-to-End Cognitive Flow | R | **CRÍTICO** | — (SPEC-045-RUNTIME-001) | MANTER | — |
| 30–41 | SPEC-026…037 | Skills Analíticas (12) | R | **CRÍTICO** | — (SPEC-025/I-001) | MANTER | Escopo não detalhado — inconclusivo por slot |
| 42 | SPEC-047 | Runtime Caching (Grupo A) | R | **CRÍTICO** | — | MANTER | Placeholder; escopo não detalhado |

**Contagem:** 1 slot **ADIANTAR** (parte S) — SPEC-022. 1 slot **ABRIR pela ordem regular** — SPEC-002 (não é adiantamento). Os demais **~41 slots** (contando os 12 de 026–037 e o placeholder 047) → **MANTER**.

**Slots com Bloco S isolável identificado:** SPEC-022 (taxonomia adversarial — **BAIXO, adiantável**); SPEC-025 (template de Skill-spec — **MÉDIO, bloqueado por I-001**). Slivers S *marginais e já cobertos* pelo baseline vigente (sem delta que justifique abertura): SPEC-007, SPEC-038, SPEC-041, SPEC-044.

---

## PARTE 3 — Mapa de dependências críticas

Slots MÉDIO/CRÍTICO agrupados pela dependência exata que os bloqueia, para Andraus ver **quais decisões/homologações destravam mais da fila**.

| Dependência bloqueadora | Tipo | Slots bloqueados | Efeito de destravar |
|---|---|---|---|
| **J-001** (fórmula/pesos/limiares definitivos do Conviction Vector) | Decisão aberta (exige backtest) | SPEC-003 (direto) → cascata a SPEC-014, 015, 016, 017; fecha dim. B `decision traceability` da SPEC-020 | Destrava a **espinha vertical de decisão** (o eixo Convicção→Decisão→Missão) |
| **I-001** (Skills como unidades formais?) | Decisão aberta | SPEC-025 + SPEC-026…037 (12) = **13 slots** | Destrava a **maior banda horizontal** em contagem de slots (toda a fila de Skills) |
| **M-001** (estados do Blackboard p/ objetos não-hipótese) | Decisão aberta | SPEC-004 → SPEC-005 (semântica de eventos) | Destrava a FASE 2 (memória de trabalho + transporte) |
| **H-001** (KG: grafo real vs. memória) | Decisão aberta | SPEC-006 → SPEC-007 (RAG) | Destrava a FASE 3 (memória semântica) |
| **G-001** (schema do estado persistente por agente) | Decisão aberta | SPEC-009 | Destrava persistência cognitiva (FASE 4) |
| **K-001** (ciclo de evolução do conhecimento) | Decisão aberta | SPEC-018; ativa BL-013/BL-015 | Destrava governança de aprendizado runtime (FASE 7) |
| **Kernel cognitivo homologado** (FASES 1–4) | Homologação upstream | SPEC-008, 010–013, 023, 024, 040–045 | Pré-condição estrutural de todos os agentes e da produção |
| **SPEC-014 homologada** (`milestone:FASE 6`) | Homologação upstream | SPEC-015, 016; 2ª condição de BL-018 (Risk Agent) | Destrava missão + o Risk Agent (23 RISK-SPEC) |
| **SPEC-045-RUNTIME-001** | Decisão aberta | SPEC-045 (só baseline nela) | Destrava a integração final |

**Achado mais importante (Parte 3).** Há **duas alavancas de destravamento de naturezas distintas**, e elas não competem:

1. **J-001 destrava a *profundidade* (o eixo crítico vertical).** É o gargalo do caminho crítico: SPEC-003 é a dobradiça de onde cascateia toda a cadeia Convicção→Decisão→Missão (014/015/016) e o fechamento da dimensão B `decision traceability` da SPEC-020. Poucos slots em contagem, mas é a coluna vertebral — e **J-001 exige backtest**, logo não é destravável por decisão administrativa (é o mais "caro" de resolver).

2. **I-001 destrava a *largura* (a maior banda horizontal): 13 slots** (SPEC-025 + as 12 Skills analíticas 026–037). É a decisão que, resolvida, libera o **maior número de slots** da fila. Diferente de J-001, I-001 é uma decisão de **arquitetura** (Skills como unidade formal + R-ARCH Skill-vs-agente), não depende de backtest — em tese destravável por deliberação de Andraus sobre a arquitetura, sem esperar dados de mercado.

**Recomendação de leitura para Andraus (não vinculante, [PROPOSTA]):** se o objetivo for **maximizar slots destravados por decisão**, **I-001** é a alavanca de maior retorno (13 slots) e a mais tratável (arquitetural, sem backtest) — embora seus slots estejam distantes (FASES 10–11). Se o objetivo for **destravar o caminho crítico**, **J-001** é imperativo, porém represado por backtest (não acelerável por decisão isolada). **Nenhuma destas decisões é fechada por esta auditoria (CONS-01)** — o mapa apenas expõe a alavancagem.

---

## Notas de conformidade

- Documento **[PROPOSTA]**/auditoria: **não abre Spec, não homologa, não edita ROADMAP/RMR-001, não renumera slot** (INV-07, INV-09). SPEC-002 permanece o próximo trabalho autorizado, **inalterada e não condicionada** por qualquer linha acima.
- Nenhuma decisão aberta foi fechada (CONS-01): J-001, N-001, M-001, H-001, G-001, I-001, K-001, C-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001, ECC-VAL-001, ECC-03-001 permanecem abertas.
- Slots tratados como **slots indicativos**, não Specs (RULE-ECC-01); a classificação não os congela nem lhes atribui número definitivo.
- Cruzamento com backlog: SPEC-002 é pré-condição de BL-024 (absorvido/SPEC-046); SPEC-003=BL-004; SPEC-004=BL-003; SPEC-007/014/038 fecham BL-017; SPEC-010–014=BL-001; SPEC-018=gatilho BL-013/BL-015; SPEC-014(FASE 6)=2ª condição BL-018; SPEC-025=BL-016. Nenhum desses BL é Bloco S adiantável de forma que altere a régua de corte (todos R-dependentes) — consistente com `ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md`.
- RULE-ECC-04 (captura verbatim de fonte externa): **não incide** — esta auditoria não cita fonte `[EXTERNO]` nem sustenta alegação carregada em pesquisa web; todas as âncoras são documentos internos do repositório.
- Adiantar = produzir Dossiê de Pesquisa + proposta de abertura antes do gatilho nominal, ou identificar candidato a linha paralela (modelo SPEC-046) — **nunca homologar a Spec**.

---

*Auditoria de adiantamento de slots — Especificador SOT, 2026-09-28. NÃO-normativa (INV-09). Complementa a priorização de backlog do mesmo dia. Homologação/encaminhamento: Andraus.*
