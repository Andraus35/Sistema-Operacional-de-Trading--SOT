# QUESTIONÁRIO DE RESOLUÇÃO — SOT Arranque

**Data:** 2026-09-14
**Produzido por:** Especificador Principal (Claude Code — Opus, esforço alto)
**Destino:** Andraus (Consensus Authority)
**Natureza:** Missão de arranque — auditoria de conflitos, inconsistências e ambiguidades. **Não contém Spec.**
**Regra de operação:** nada resolvido em silêncio; cada achado ancorado em arquivo + localização + trecho literal.

---

## Sumário executivo

### Contagem de achados
- **Conflitos entre documentos / inconsistências internas:** 14 (Apêndice A — CONFLITO-001…014)
- **Ambiguidades de fronteira:** 7 (Apêndice B — AMBIGUIDADE-001…007)
- **Termos sem definição canônica:** 8 (Apêndice C — TERMO-001…008)
- **Decisões abertas não rastreadas em `atomic-spec.md §12`:** 11 (Apêndice D — DECISÃO-ABERTA-001…011)
- **Perguntas de resolução para Andraus:** 15 (Q-001…Q-015)

### Specs diretamente impactadas
- **SPEC-001 (Hypothesis Harness):** Q-001, Q-005, Q-006, Q-011, Q-012 — a Spec **próxima autorizada** está bloqueada em sua premissa (CHM-001 como baseline) e em fronteiras não resolvidas.
- **SPEC-002 (Evidence Harness):** Q-001, Q-013.
- **SPEC-003 (Conviction / Evidence Fusion):** Q-002, Q-004, Q-007, Q-008 — além de J-001 já rastreado.
- **SPEC-004 (Blackboard):** Q-005, Q-006.
- **SPEC-013 (ICT) / SPEC-014 (Synthesis):** Q-002, Q-004, Q-007.
- **SPEC-019 (Harness Governance) + operação do Revisor:** Q-009, Q-010, Q-011, Q-012.
- **Toda entrega (Constitution Check):** Q-002, Q-003, Q-009.

### Ordem de prioridade (por desbloqueio)
1. **Bloqueadores diretos da SPEC-001:** Q-001 (baseline dos modelos canônicos / CHM-001), Q-005 (quem cria hipótese), Q-006 (máquina de estados da hipótese), Q-012 (briefing PP-SPEC-001).
2. **Base normativa transversal (afeta o Constitution Check de todas as Specs):** Q-002 (limiares de convicção — abertos ou fechados), Q-003 (as "5 Salvaguardas" — misatribuição), Q-004 (R:R 2:1 vs 3:1), Q-011 (status normativo de CONSTITUTION/RULES/CONFLICT-MAP).
3. **SPEC-003 e cadeia de decisão:** Q-007 (topologia Fusion/Conviction/Synthesis — B-001+), Q-008 (dimensões do Conviction Vector).
4. **Método e governança:** Q-009 (3E vs 4E), Q-010 (PPQ-001 existe?), Q-013 (paths do validador e dos agentes).
5. **Identidade e terminologia:** Q-014 (mapeamento de nomes de agentes), Q-015 (nome/expansão do sistema).

### Nota de transparência metodológica (limitações do ambiente)
- Os **PDFs de FUNDAMENTOS** (`KERNEL V2`, `ENGENHARIA GERAL`, `AUDITORIA DE IDEIAS`) e demais PDFs **não são renderizáveis nativamente** neste ambiente (poppler ausente). O texto foi **extraído via `pypdf`** para o scratchpad e auditado a partir daí; a paginação citada é a do extrator. Os `.docx` de `PLANEJAMENTO/Nova pasta/` **não foram lidos** (sem conversor disponível) — são candidatos a verificação futura, mas aparentam ser versões anteriores dos consolidados.
- Divergência de nomes/caminhos entre o **prompt de arranque** e o repositório real (registrada em CONFLITO/DECISÃO-ABERTA): `roadmap.md`→`ROADMAP.md`; `atomic-spec.md`→`ATOMIC-SPEC.md`; `.claude/agents/especificador.md`→`especificador.md` (raiz); `scripts/validate_spec_sot.py`→`validate_spec_sot.py` (raiz); `claude_GEH-001…`→`RETOMADA/GEH-001…`. O arquivo `claude_PP-SPEC-001_Pacote_Partida_Hypothesis_Model.md` (leitura 11 da Fase 1) **não existe** (ver Q-012).
- A base de conhecimento canônica reside em `DOCUMENTOS INICIAIS/` no **diretório-pai** (`SOT ENGINER/`), fora do working dir do harness.

---

## Perguntas de resolução

─────────────────────────────────────────────────────────
### Q-001 · [CONFLITO] — CHM-001 (e os demais modelos canônicos) é baseline ou não?
─────────────────────────────────────────────────────────
**Contexto:** A SPEC-001 inteira é premissada em "CHM-001 já existe como baseline; construir sobre ele; redefini-lo viola CONST-01". Mas o **Catálogo Oficial ORYX** — declarado *Single Source of Truth* de baseline (autoridade = Controlador, GMC-001) — lista CHM-001 como **não iniciado**. O capítulo do próprio CHM-001 diz "CONSOLIDADO — aprovado por Andraus". Há três estados incompatíveis para o mesmo artefato.

**Referência documental:**
- `ROADMAP.md:20,50,68,85,89` — "CHM-001 já existe como baseline"; R1/R4 listam "modelos canônicos já baselined (CHM-001, CEM-001, CCM-001, CDM-001, CNM-001)".
- `DOCUMENTOS INICIAIS/05_Catalogo_Registros_e_Diretrizes/CATALOGO_OFICIAL_ORYX.md:113` — "CHM-001, CCM-001, CDM-001, CNM-001 | **Não iniciados — sem entrada no Catálogo**". Baselined no §2: apenas GMC-001, CEM-001, SAS-001, PPQ-001, CEE-001, CR-001 (parcial), SDD-001.
- `DOCUMENTOS INICIAIS/02_Modelos_Canonicos/CHM-001_Capitulo1.md:5` — "Status: CONSOLIDADO — aprovado por Andraus (Decisor Final) em 12/07/2026".
- `ATOMIC-SPEC.md:261` (INV-09) — "Sem baseline informal — 'Congelado/Baseline' só com homologação explícita de Andraus".

**Opções:**
- **[A]** Reconhecer CHM-001 como **baselined** e registrá-lo no Catálogo (o arquivo aprovado por Andraus 12/07 supre a Etapa 3; falta a Etapa 4/Controlador). *Implicação:* SPEC-001 procede como escrito — constrói sobre CHM-001 sem redefinir; roadmap R1/R4 permanecem, mas o Catálogo precisa ser atualizado para não violar INV-09.
- **[B]** Tratar CHM-001 como **FATO ARQUITETURAL não baselined**. *Implicação:* SPEC-001 não pode invocar CONST-01 ("redefinir canônico") como bloqueio rígido; a estrutura da hipótese entra como referência sujeita a decisão, e a SPEC-001 deve marcar campos do CHM como pendentes até baseline formal.
- **[C]** **Re-homologar CHM-001 formalmente** (Estrategista→Analista→Andraus→Controlador) **antes** de iniciar a SPEC-001. *Implicação:* SPEC-001 aguarda; o terreno fica limpo e o Catálogo passa a ser fonte confiável.

**Bloqueia:** SPEC-001 (premissa central), SPEC-002 (mesma lógica p/ CEM-001), SPEC-003 (CCM-001).

─────────────────────────────────────────────────────────
### Q-002 · [CONFLITO] — Limiares de convicção: fechados na base normativa vs. abertos por J-001/INV-03
─────────────────────────────────────────────────────────
**Contexto:** A base normativa do repo trata `convicção ≥ 70%`, `bias ≥ 60%`, `score ≥ 7/9` como **fatos fechados**. O método vigente (INV-03/J-001) diz que fórmula/pesos/**limiares** do Conviction Vector são **decisão aberta** e não podem ser invariante fechado. A fonte constitucional (ENGENHARIA GERAL) **defere o limiar à política de governança** e afirma que "convicção não é score" — os números aparecem no ARIA_Plano_Mestre como **alvos de calibração**.

**Referência documental:**
- `CONSTITUTION.md:152` — "Sinal operacional: Output do Synthesis Agent quando convicção global ≥ 70% e R:R ≥ 2:1…"; `AGENTS.md:67` — "Conviction global threshold: ≥ 70% for signal, ≥ 60% for bias".
- `RULES.md:15` (RULE-003) — "Convicção global < 70% NÃO DEVE produzir sinal"; `RULES.md:249-255` (RULE-CEE-004) — "Score total < 7/9 → bloqueado; Convicção < 70% → sem sinal".
- `ATOMIC-SPEC.md:255` (INV-03) — "Conviction Vector NÃO é invariante fechado — fórmula/pesos/limiares = J-001 em aberto"; `ATOMIC-SPEC.md:236` (J-001).
- `scratchpad/enggeral.txt:1337` — "Quando a Convicção Global atingir **o nível exigido pela política de governança**"; `:1733` — "múltiplas dimensões, e não por um único score".
- `DOCUMENTOS INICIAIS/03_Agentes_Especializados/ARIA_Plano_Mestre.md:776` — "Threshold inicial de alerta: 7, 8 ou apenas 9? (recomendo iniciar com 8, **calibrar depois**)".

**Opções:**
- **[A]** Afirmar que os limiares são **abertos (J-001)** e são a autoridade. *Implicação:* RULE-003/RULE-SY-003/RULE-CEE-004, a tabela de "Conflitos de convicção" do CONFLICT-MAP e os `≥70%`/`≥7/9` da `synthesis.spec.md` devem ser **re-etiquetados como pendentes** (não fechados). SPEC-003 fecha J-001; nada downstream usa número fixo antes disso.
- **[B]** Homologar os números do ARIA como **piso interino (FATO NORMATIVO com cláusula de recalibração)**, no molde da "Fase Piloto" do CEE-001 §7. *Implicação:* J-001 é parcialmente fechado; os valores viram vinculantes-mas-provisórios com gatilho de recalibração; INV-03 é emendado para refletir "piloto".
- **[C]** Reconhecer que há **duas camadas** (piso operacional de piloto no ARIA/legacy vs. modelo canônico CCM-001 em aberto) e definir explicitamente qual prevalece por contexto. *Implicação:* exige nota de precedência em CONSTITUTION/RULES; risco de ambiguidade permanente.

**Bloqueia:** SPEC-003, SPEC-014, e o Constitution Check de toda Spec (item "Conviction como pendente").

─────────────────────────────────────────────────────────
### Q-003 · [CONFLITO] — "5 Salvaguardas Constitucionais do CEE-001 §10": duas listas diferentes
─────────────────────────────────────────────────────────
**Contexto:** O repo cita "as 5 Salvaguardas Constitucionais do CEE-001 §10" como um conjunto de salvaguardas de **sinal de trading** (invalidação, 7/9, conflito direcional, 70%, R:R). Mas o **CEE-001 §10 real** (baselined) contém 5 salvaguardas de **economia/roteamento**. Apenas a Salvaguarda 4 (custo não entra no Conviction Vector) coincide. A âncora normativa mais citada do projeto aponta para um conteúdo que não existe na fonte.

**Referência documental:**
- `DOCUMENTOS INICIAIS/01_Governanca_Geral/CEE-001_Versao_Consolidada.md:231-237` (§10) — "1. Nenhum agente pode reduzir sua própria classe de modelo; 2. Scheduler nunca suprime execução por custo…; 3. Cache nunca serve contexto desatualizado; 4. **Métricas de custo nunca entram no Conviction Vector**; 5. Toda alteração de roteamento é reversível e versionada".
- `RULES.md:249-255` (RULE-CEE-004) — "As 5 salvaguardas constitucionais… [Fonte: CEE-001 §10]" seguido de invalidação / 7-9 / directional_conflict / 70% / R:R 2:1.
- `ATOMIC-SPEC.md:264` — "As 5 Salvaguardas Constitucionais do CEE-001 §10 são invioláveis (INV-04 é a Salvaguarda 4)" — nota que só INV-04 casa com o CEE-001 real.
- `revisor.md:113,124` e `especificador.md:165,187` — repetem "5 Salvaguardas (CEE-001 §10)" com o sentido de sinal.

**Opções:**
- **[A]** **Corrigir a atribuição:** reconhecer o CEE-001 §10 real (economia) e reancorar as salvaguardas de sinal à sua fonte verdadeira (ARIA/ENGENHARIA GERAL), com um ID próprio. *Implicação:* RULE-CEE-004, `atomic-spec.md §13`, `revisor.md Passo 2` e `especificador.md §7` reescrevem a referência; INV-04 permanece (é a única que casa).
- **[B]** Reconhecer **dois conjuntos distintos** de salvaguardas ("Salvaguardas de Economia — CEE-001 §10" e "Salvaguardas de Sinal — [fonte X]"), cada um com ID e escopo próprios. *Implicação:* o termo "5 Salvaguardas" deixa de ser ambíguo; toda citação passa a nomear qual conjunto.
- **[C]** Homologar as salvaguardas de sinal como emenda formal ao CEE-001 (novo §), unificando. *Implicação:* CEE-001 (baselined) é reaberto e reversionado.

**Bloqueia:** Constitution Check de toda Spec; Passo 2 do Revisor; integridade documental (Passo 4 do Revisor: "RULES citadas existem de fato").

─────────────────────────────────────────────────────────
### Q-004 · [INCONSISTÊNCIA INTERNA] — R:R mínimo: 2:1 ou 3:1?
─────────────────────────────────────────────────────────
**Contexto:** O RULES.md contém as duas regras ao mesmo tempo: R:R < **3:1** bloqueia (RULE-006) e R:R < **2:1** bloqueia (RULE-ICT-002). Pior: a RULE-ICT-002 **declara "2:1" citando como fonte o ARIA "1:3 mínimo"** (= 3:1) — a regra contradiz a própria fonte. A fonte de origem (ARIA) diz 1:3; o repo introduziu 2:1 em vários lugares.

**Referência documental:**
- `RULES.md:24-25` (RULE-006) — "R:R calculado < **3:1** NÃO DEVE produzir sinal… [Fonte: ARIA §5 '1:3 mínimo'…]".
- `RULES.md:150-151` (RULE-ICT-002) — "NÃO DEVE aceitar R:R < **2:1**… [Fonte: ARIA §5 regra R:R '1:3 mínimo'…]".
- `CONSTITUTION.md:153`, `AGENTS.md:67`, `specs/synthesis.spec.md:22,57` — "R:R ≥ 2:1".
- `DOCUMENTOS INICIAIS/03_Agentes_Especializados/ARIA_Plano_Mestre.md:22,256,339` — "R:R mínimo **1:3**"; "TARGET 2 (1:3) ← mínimo aceito".

**Opções:**
- **[A]** **3:1** (fiel ao ARIA de origem). *Implicação:* corrigir RULE-ICT-002, CONSTITUTION, AGENTS, `synthesis.spec.md`; a SPEC-013/014 usam 3:1.
- **[B]** **2:1** (valor hoje majoritário no repo). *Implicação:* corrigir RULE-006 e as citações que dizem "1:3"; documentar por que se afastou do ARIA.
- **[C]** **Escalonado** (ex.: piso 2:1 dependente de score/killzone) e declarar explicitamente. *Implicação:* nova regra unificada substitui RULE-006 e RULE-ICT-002.

**Bloqueia:** SPEC-013 (ICT), SPEC-014 (Synthesis); integridade do RULES.md.

─────────────────────────────────────────────────────────
### Q-005 · [CONFLITO] — Quem cria hipótese: só o agente estrutural, ou todos os agentes?
─────────────────────────────────────────────────────────
**Contexto:** A CONSTITUTION restringe a publicação de hipóteses ao workspace do **Elliott Specialist** (SMC publica "Narratives", não hipóteses), coerente com INV-01/INV-02. Mas o KERNEL V2 (EC-COG-002) e o CHM-001 dizem que **todos os agentes especializados produzem hipóteses** (estrutural, institucional, contextual…). O objeto "hipótese" tem escopo diferente entre as fontes.

**Referência documental:**
- `CONSTITUTION.md:186` (tabela Blackboard) — "Hypotheses | **Elliott Specialist** | Hipóteses estruturais"; "Narratives | SMC Specialist".
- `ATOMIC-SPEC.md:253-254` (INV-01/INV-02) — hierarquia; "ICT NÃO cria hipótese estrutural".
- `scratchpad/kernel.txt` EC-COG-002 (p.27-28) — "Quem produz hipóteses: **Todos os agentes especializados** (Structural, Institutional, Context, Mission, Learning)".
- `CHM-001_Capitulo1.md:210` — "Who: Todos os componentes arquiteturais que **produzem ou consomem** hipóteses".

**Opções:**
- **[A]** Só o **agente estrutural (Elliott)** cria a hipótese estrutural; os demais produzem **Evidência/Narrativa** (CEM-001/CNM), não "hipótese". *Implicação:* SPEC-001 especifica um único produtor de hipótese; alinha com INV-01/02 e com o Blackboard da CONSTITUTION; contradiz o KERNEL/CHM (que passam a ser lidos como "hipótese" em sentido lato = evidência interpretada).
- **[B]** Cada agente produz **hipóteses de seu domínio** (taxonomia CHM DESCRIPTIVE/EXPLANATORY/PREDICTIVE/DIAGNOSTIC); a hierarquia Elliott→…→ICT governa **precedência**, não exclusividade de criação. *Implicação:* SPEC-001 especifica múltiplos produtores; o Blackboard ganha regra de precedência; a tabela da CONSTITUTION é emendada.
- **[C]** **Híbrido:** só o estrutural cria a hipótese **primária/direcional**; demais criam sub-hipóteses referenciadas à primária. *Implicação:* SPEC-001 define a relação primária↔sub-hipótese (herança fractal).

**Bloqueia:** SPEC-001, SPEC-004 (workspace Hypotheses), SPEC-012 (SMC).

─────────────────────────────────────────────────────────
### Q-006 · [AMBIGUIDADE DE FRONTEIRA] — Máquina de estados da hipótese: qual conjunto canônico governa?
─────────────────────────────────────────────────────────
**Contexto:** Há **quatro** máquinas de estado incompatíveis para o objeto hipótese/objeto-do-Blackboard. A SPEC-001 (D5) precisa de uma; a SPEC-004 (Blackboard) precisa de outra — ou a mesma. Não está definido se o estado epistêmico do CHM e o estado de publicação do Blackboard são a mesma coisa ou camadas distintas.

**Referência documental:**
- `CHM-001_Capitulo1.md:137-147` (baselined) — EMERGENT, CANDIDATE, ACTIVE, DOMINANT, SUPERSEDED, REFUTED, ARCHIVED.
- `CONSTITUTION.md:298` / `RULES.md:297-299` (RULE-BB-003) — PROPOSED → VALIDATED → ACTIVE → SUPERSEDED.
- `scratchpad/kernel.txt` EC-COG-002 (p.34) — Emergente, Em Formação, Confirmada, Dominante, **Exaurindo**, Invalidada, Arquivada; e Blackboard EC-COG-004 (p.58) — Publicado, Atualizado, Confirmado, Contestável, Invalidado, Arquivado.

**Opções observadas:**
- **[A]** **CHM-001 é canônico** para o estado epistêmico; o Blackboard armazena o estado do CHM e as transições PROPOSED/VALIDATED do RULE-BB-003 são descontinuadas. *Implicação:* SPEC-001 usa os 7 estados do CHM; SPEC-004 não define estado próprio de hipótese; RULE-BB-003 é emendada.
- **[B]** **Duas camadas coexistem:** estado epistêmico (CHM) × estado de publicação no Blackboard (PROPOSED/…); a SPEC-001 fornece uma **tabela de mapeamento** entre elas. *Implicação:* SPEC-001 e SPEC-004 compartilham um contrato de mapeamento; maior complexidade, mas separa "o que a hipótese é" de "como ela está publicada".
- **[C]** **Reconciliar tudo em um único conjunto** homologado (descartar KERNEL e RULE-BB-003 divergentes). *Implicação:* emenda a CONSTITUTION/RULES e reafirmação do CHM.

**Impacto se não resolvida:** a SPEC-001 (D5) e a SPEC-004 ficam inválidas ou mutuamente incoerentes.

─────────────────────────────────────────────────────────
### Q-007 · [AMBIGUIDADE DE FRONTEIRA] — Topologia Conviction/Fusion/Synthesis (B-001 + Evidence Fusion)
─────────────────────────────────────────────────────────
**Contexto:** B-001 (Conviction Engine × Synthesis) já é rastreado, mas o problema é maior: há **três** nomes de componente para a camada de decisão e eles não fecham. A CONSTITUTION mostra Conviction Engine **separado** do Synthesis; os `specs/` só têm 5 agentes com a convicção **embutida** no Synthesis; o CEM-001 introduz um **Fusion Engine** (produtor de Evidência DERIVED) distinto do Conviction Engine; e a SPEC-003 do roadmap funde "Conviction Vector **& Evidence Fusion Engine**".

**Referência documental:**
- `CONSTITUTION.md:100-104` — "…Conviction Engine (compara narrativas, calcula convicção) ↓ Synthesis Agent (árbitro final)" (separados).
- `AGENTS.md:42-48` — arquitetura de **5 agentes** (Elliott/Fibonacci/SMC/ICT/Synthesis); sem Conviction Engine; `specs/synthesis.spec.md:1,9` — "Synthesis Agent (Conviction Engine + Árbitro Final)… calcular a convicção global".
- `CEM-001_Versao_Consolidada.md:172,664-667` — "Fusion Engine (único ENGINE producer)… produz Evidências DERIVED" (distinto do Conviction Engine consumidor, `:182,678`).
- `ROADMAP.md:130-133` (SPEC-003) — "Conviction Vector **& Evidence Fusion Engine**".
- `ATOMIC-SPEC.md:237` (B-001).

**Opções observadas:**
- **[A]** **Três componentes:** Fusion Engine (funde evidências → Evidência DERIVED) → Conviction Engine (calcula vetor) → Synthesis (arbitra/decide). *Implicação:* SPEC-003 especifica Fusion+Conviction; SPEC-014 especifica só a arbitragem; `synthesis.spec.md` é decomposta.
- **[B]** **Dois componentes:** Fusion Engine + Synthesis (com a convicção embutida no Synthesis). *Implicação:* B-001 resolvido como "não separado"; SPEC-014 absorve a convicção; SPEC-003 vira só Fusion+Vetor.
- **[C]** **Tudo no Synthesis** (fusão + convicção + arbitragem). *Implicação:* contradiz CEM-001 (Fusion Engine é entidade canônica de produção de Evidência); exigiria emenda ao CEM-001 baselined.

**Impacto se não resolvida:** SPEC-003 e SPEC-014 não têm fronteira definida; risco de duplicar ou omitir o Fusion Engine.

─────────────────────────────────────────────────────────
### Q-008 · [DECISÃO ABERTA NÃO RASTREADA] — Quantas dimensões tem o Conviction Vector, e quais?
─────────────────────────────────────────────────────────
**Contexto:** J-001 rastreia fórmula/pesos/limiares — **não** o número/identidade das dimensões. E as fontes divergem: 7, 5 ou 8 dimensões.

**Referência documental:**
- `CONSTITUTION.md:37-39` (P02) — "estrutural, geométrica, fractal, institucional, operacional, temporal, histórica" (**7**).
- `specs/synthesis.spec.md:18-19` (escopo) — as mesmas **7**; mas `:100` (output `conviction_vector`) — "{estrutural, geométrica, fractal, institucional, operacional}" (**5**).
- `scratchpad/AUDITORIA…txt` (§J.3) — "convicção_global = f(d_estrutural, d_geometrica, d_fractal, d_institucional, d_operacional, d_temporal, d_volume, d_historico)" (**8**, inclui `volume`).

**Opções:**
- **[A]** **7 dimensões** conforme CONSTITUTION P02. *Implicação:* corrigir o `conviction_vector` de 5→7 na `synthesis.spec.md` e no schema; SPEC-003 parte de 7.
- **[B]** **8 dimensões** (inclui `volume`). *Implicação:* emendar P02 e a spec; SPEC-003 parte de 8.
- **[C]** **Deferir a identidade das dimensões à SPEC-003/CCM-001** (só o número mínimo é fixado agora). *Implicação:* a dimensionalidade entra explicitamente no escopo de J-001/SPEC-003.

**Bloqueia:** SPEC-003 (e o schema de saída do Synthesis).

─────────────────────────────────────────────────────────
### Q-009 · [INCONSISTÊNCIA INTERNA] — Framework 3E (baselined) vs 4Es (método vigente)
─────────────────────────────────────────────────────────
**Contexto:** O CEE-001 (baselined) e a CONSTITUTION definem **3E** (Eficácia → Efetividade → Eficiência), com Conformidade no topo, **sem Economicidade**. O método vigente (atomic-spec, especificador, GEH-001) usa **4Es**, adicionando Economicidade como 4º nível inviolável. Há um degrau a mais na hierarquia dependendo do documento.

**Referência documental:**
- `DOCUMENTOS INICIAIS/01_Governanca_Geral/CEE-001_Versao_Consolidada.md:63-76` (§3) — hierarquia "Conformidade > Eficácia > Efetividade > **Eficiência**" (para em Eficiência).
- `CONSTITUTION.md:160-168` — "Framework 3E… Eficácia → Efetividade → Eficiência".
- `ATOMIC-SPEC.md:148` — "4Es: Eficácia → Efetividade → Eficiência → **Economicidade**"; `RETOMADA/GEH-001…md:98-116` (§3) — introduz e distingue Economicidade como 4º E.

**Opções:**
- **[A]** **Adotar 4Es** e emendar CEE-001/CONSTITUTION para incluir Economicidade. *Implicação:* CEE-001 (baselined) reaberto/reversionado; toda declaração de 4Es fica coerente.
- **[B]** Manter **CEE-001 3E** como constitucional; tratar Economicidade como camada **de método** (não constitucional). *Implicação:* atomic-spec/especificador precisam declarar que Economicidade não sobe ao nível das 3E constitucionais; risco de dupla régua.

**Bloqueia:** consistência do item "4Es" em toda entrega (Passo 6 do Revisor).

─────────────────────────────────────────────────────────
### Q-010 · [CONFLITO] — PPQ-001 existe/vigora ou foi extinto?
─────────────────────────────────────────────────────────
**Contexto:** O `revisor.md` afirma categoricamente que **"Não há PPQ-001"**. Mas o Catálogo lista PPQ-001 como **BASELINED v1.2**, o RULES.md tem uma RULE-PPQ-001 ativa, e o AGENTS-pai referencia PPQ-001 como governança.

**Referência documental:**
- `revisor.md:59` — "Não há papéis intermediários. **Não há PPQ-001.** A única aprovação válida é a homologação de Andraus."
- `CATALOGO_OFICIAL_ORYX.md:23` — "PPQ-001 | … | 1.2 | BASELINE 1.2 | **BASELINED**".
- `RULES.md:328-333` (RULE-PPQ-001) — "Nível de rigor proporcional ao impacto (dial GES)… [Fonte: PPQ-001 §10.2]".

**Opções:**
- **[A]** PPQ-001 **vigora** (baselined) e continua fornecendo o GES dial; o `revisor.md` está incorreto e deve ser corrigido (a frase nega o fluxo de *papéis* PPQ, não o documento). *Implicação:* corrigir `revisor.md`; RULE-PPQ-001 e o dial GES permanecem.
- **[B]** PPQ-001 foi **substituído** pelo fluxo de três papéis (Especificador→Revisor→Andraus) para efeito de aprovação, permanecendo apenas como referência de rigor. *Implicação:* declarar explicitamente o escopo remanescente do PPQ-001; ajustar RULES/Catálogo com nota de superseção parcial.

**Bloqueia:** operação do Revisor; SPEC-019 (governança).

─────────────────────────────────────────────────────────
### Q-011 · [DECISÃO ABERTA NÃO RASTREADA] — Status normativo de CONSTITUTION.md, RULES.md e CONFLICT-MAP.md
─────────────────────────────────────────────────────────
**Contexto:** Esses três arquivos são a autoridade F.1 (feedforward) do harness e são citados como fonte por toda parte — mas **não têm entrada no Catálogo Oficial** e não há registro de homologação por Andraus. Eles fixam justamente os fatos contestados (limiares, salvaguardas) e derivam de fontes que são narrativas de proposta (KERNEL/ENGENHARIA GERAL).

**Referência documental:**
- `ATOMIC-SPEC.md:78` — "F.1 Feedforward — prevenção/orientação (CONSTITUTION, RULES, CONFLICT-MAP). **Autoridade**; não se 'testa'."
- `CATALOGO_OFICIAL_ORYX.md:18-26` — Catálogo não lista CONSTITUTION/RULES/CONFLICT-MAP.
- `CONSTITUTION.md:2` / `RULES.md:2` / `CONFLICT-MAP.md:2` — cabeçalho "Fonte: ENGENHARIA GERAL… | Versão 1.0" (sem registro de homologação).
- `ATOMIC-SPEC.md:261` (INV-09) — "Sem baseline informal".

**Opções:**
- **[A]** **Homologar** CONSTITUTION/RULES/CONFLICT-MAP como baseline F.1 — **depois** de aplicadas as correções de Q-002/Q-003/Q-004/Q-008. *Implicação:* passam a ser autoridade formal registrada no Catálogo; as Specs podem citá-los como FATO NORMATIVO.
- **[B]** Tratá-los como **derivados de trabalho não normativos** até reconciliação. *Implicação:* nenhuma Spec pode citá-los como FATO NORMATIVO; só as fontes baselined (CEM/CEE/GMC/SDD/…) valem como autoridade; muito do Constitution Check precisa reancorar.

**Bloqueia:** a autoridade de citação de todas as Specs; o Passo 4 do Revisor (integridade/rastreabilidade).

─────────────────────────────────────────────────────────
### Q-012 · [DECISÃO ABERTA NÃO RASTREADA] — Briefing PP-SPEC-001 citado no roadmap não existe
─────────────────────────────────────────────────────────
**Contexto:** O `ROADMAP.md §25` aponta "PP-SPEC-001 (briefing)" como orientação de escopo da SPEC-001, e a Fase 1 do prompt de arranque lista `claude_PP-SPEC-001_Pacote_Partida_Hypothesis_Model.md`. Nenhum arquivo com esse nome existe (grep em todo o projeto: só o próprio ROADMAP menciona o ID). O Especificador não pode citar fonte inexistente.

**Referência documental:**
- `ROADMAP.md:375` — "Orientação de escopo: **PP-SPEC-001** (briefing; actualizado pela observação de arranque de 2026-09-14)".
- Busca em `SOT ENGINER/` — `PP-SPEC-001` só aparece em `ROADMAP.md`; nenhum arquivo `*PP-SPEC-001*` presente.
- `especificador.md:217` — "Nunca inventa número de registro, decisão, artefato ou **fonte**."

**Opções:**
- **[A]** **Produzir/localizar** o PP-SPEC-001 (pacote de partida da SPEC-001) antes de iniciar a Spec. *Implicação:* SPEC-001 aguarda o briefing formal.
- **[B]** Tratar a **seção de escopo da SPEC-001 no próprio ROADMAP (§4)** como o briefing efetivo e **remover** a referência a PP-SPEC-001. *Implicação:* elimina a fonte-fantasma; o escopo da SPEC-001 passa a ser o texto do roadmap (sujeito a Q-001/Q-005/Q-006).

**Bloqueia:** início da SPEC-001.

─────────────────────────────────────────────────────────
### Q-013 · [INCONSISTÊNCIA INTERNA] — Caminhos do validador e dos arquivos de agente divergem do declarado
─────────────────────────────────────────────────────────
**Contexto:** O gate determinístico obrigatório do Revisor é invocado como `python scripts/validate_spec_sot.py`, mas o arquivo está na **raiz** (`scripts/` contém apenas `gate-check.js` e `post-edit-check.js`). Do mesmo modo, `especificador.md` e `revisor.md` são referenciados em `.claude/agents/` mas residem na **raiz** do repo. O comando do Revisor, como escrito, **falharia**.

**Referência documental:**
- `revisor.md:66` — "`python scripts/validate_spec_sot.py .specs/features/<SPEC-00x>/plan.md`".
- `AGENTS.md` (pai):"scripts/validate_spec_sot.py ← gate determinístico"; `AGENTS.md:32` (repo) referencia `.claude/agents/especificador.md`.
- Estrutura real: `validate_spec_sot.py` na raiz; `scripts/` = `gate-check.js`, `post-edit-check.js`; `.claude/agents/` = `sot-spec-reviewer.md`, `sot-schema-validator.md` (não `especificador.md`/`revisor.md`).

**Opções:**
- **[A]** **Mover os arquivos** para os caminhos declarados (`scripts/validate_spec_sot.py`, `.claude/agents/especificador.md`, `.claude/agents/revisor.md`). *Implicação:* os comandos e referências existentes passam a funcionar sem edição.
- **[B]** **Atualizar as referências** para os caminhos reais (raiz). *Implicação:* edita `revisor.md`, `AGENTS.md` (repo e pai) para apontar à raiz.

**Bloqueia:** o gate determinístico do Revisor em toda revisão (operacional, mas eliminatório).

─────────────────────────────────────────────────────────
### Q-014 · [AMBIGUIDADE DE FRONTEIRA] — Mapeamento de nomes de agentes (canônicos vs repo) e escopo de agentes
─────────────────────────────────────────────────────────
**Contexto:** Os documentos canônicos (CEM-001, KERNEL, SAS-001) nomeiam **Structural Agent, Institutional Agent, Fusion Engine, Macro/Sentiment/Risk/Context Agent**; o repo nomeia **Elliott Specialist, Fibonacci Validator, SMC Specialist, ICT Specialist, Synthesis Agent**. Não há um glossário que declare as equivalências, e o CEM-001 lista produtores (Macro/Sentiment/Risk/Context) que não existem na arquitetura de 5 agentes do repo.

**Referência documental:**
- `CEM-001_Versao_Consolidada.md:163-170,660-661` — produtores "Structural Agent, Institutional Agent, Macro Agent, Sentiment Agent, Risk Agent, Context Agent".
- `AGENTS.md:42-48` — 5 agentes "Elliott/Fibonacci/SMC/ICT/Synthesis".
- `DOCUMENTOS INICIAIS/03_Agentes_Especializados/SAS-001…` — "Structural Agent Specification" (= o agente Elliott).

**Opções observadas:**
- **[A]** Declarar equivalência **Structural Agent ≡ Elliott Specialist**, **Institutional Agent ≡ SMC Specialist**, e que Macro/Sentiment/Risk/Context são **fora do escopo atual do SOT** (herança do ORYX genérico). *Implicação:* SPEC-002 (produtores CEM) restringe a lista aos agentes do SOT; glossário criado.
- **[B]** Manter a **taxonomia canônica ampla** (o SOT terá Macro/Sentiment/Risk/Context no futuro). *Implicação:* roadmap ganha Specs para esses agentes; SPEC-002 mantém a lista ampla.
- **[C]** Adotar **um único vocabulário** (renomear em um dos lados). *Implicação:* edição ampla de specs ou de documentos canônicos (estes baselined — custoso).

**Impacto se não resolvida:** SPEC-002 (quem produz Evidência), SPEC-010/012 (nomes), e todo Constitution Check que cita "não redefinir modelo canônico".

─────────────────────────────────────────────────────────
### Q-015 · [INCONSISTÊNCIA INTERNA] — Identidade do sistema: "SOT" e "ORYX"
─────────────────────────────────────────────────────────
**Contexto:** A sigla SOT é expandida de **duas** formas e o sistema aparece sob **dois** nomes (SOT e ORYX) sem uma relação declarada. Isso é um termo fundacional sem definição canônica única.

**Referência documental:**
- `CONSTITUTION.md:1` — "SOT — **Sistema de Operações e Tendências**".
- `AGENTS.md:5` (repo) / `especificador.md:29` — "SOT (Sistema **Operacional de Trading**)".
- `CATALOGO_OFICIAL_ORYX.md:2` e todos os canônicos — "**ORYX AGENT**" / "ecossistema ORYX/SOT".

**Opções:**
- **[A]** Fixar **uma** expansão canônica de SOT e declarar a relação SOT↔ORYX (ex.: ORYX = ecossistema/produto; SOT = o sistema de trading). *Implicação:* glossário/ontologia oficial; cabeçalhos padronizados.
- **[B]** Consolidar tudo sob **um único nome**. *Implicação:* renomeação ampla (documentos baselined incluídos — custoso).

**Impacto se não resolvida:** ambiguidade de identidade em todos os cabeçalhos e no futuro glossário (o KERNEL já recomendava "Ontologia e Glossário Oficial" como P0 antes das Engineering Cards).

---

## Apêndice A — Inventário de Conflitos e Inconsistências Internas (CONFLITO-NNN)

**CONFLITO-001** · [FONTE] — Baseline do CHM-001
Documentos: ROADMAP vs CATALOGO_OFICIAL vs CHM-001 Cap.1
Loc. A: `ROADMAP.md:85,89` — "O modelo canônico de hipótese CHM-001 já existe como baseline".
Loc. B: `CATALOGO_OFICIAL_ORYX.md:113` — "CHM-001… Não iniciados — sem entrada no Catálogo".
Loc. C: `CHM-001_Capitulo1.md:5` — "CONSOLIDADO — aprovado por Andraus… 12/07/2026".
Natureza: Contraditório. Impacto: SPEC-001 (premissa), INV-09. → Q-001.

**CONFLITO-002** · [FONTE] — "5 modelos canônicos já baselined"
Documentos: ROADMAP vs CATALOGO vs existência de arquivos
Loc. A: `ROADMAP.md:50,68` — "modelos canônicos já baselined (CHM-001, CEM-001, CCM-001, CDM-001, CNM-001)".
Loc. B: `CATALOGO_OFICIAL_ORYX.md:113` — CCM/CDM/CNM "não iniciados"; `ATOMIC-SPEC.md:236` — "CCM-001 não baselined".
Loc. C: busca de arquivos — não existem `CCM-001*`, `CDM-001*`, `CNM-001*`; apenas referências ao ID.
Natureza: Contraditório + Lacuna (artefatos inexistentes). Impacto: SPEC-001/002/003. → Q-001.

**CONFLITO-003** · [FONTE] — Limiares de convicção fechados vs abertos
Documentos: CONSTITUTION/RULES/AGENTS/CONFLICT-MAP/synthesis.spec vs ATOMIC-SPEC(INV-03/J-001) vs ENGENHARIA GERAL
Loc. A: `CONSTITUTION.md:152`; `RULES.md:15,183,253`; `AGENTS.md:67`; `CONFLICT-MAP.md:44-48`; `specs/synthesis.spec.md:21,44,48` — "≥70%", "<70%", "7/9" como fatos fechados.
Loc. B: `ATOMIC-SPEC.md:255` (INV-03) — "fórmula/pesos/limiares = J-001 em aberto".
Loc. C: `scratchpad/enggeral.txt:1337,1733` — limiar "exigido pela política de governança"; "não por um único score".
Natureza: Contraditório. Impacto: SPEC-003/014 + Constitution Check universal. → Q-002.

**CONFLITO-004** · [FONTE][INFERÊNCIA] — Atribuição de fonte dos limiares numéricos
Seções: RULES.md vs conteúdo real de ENGENHARIA GERAL
Loc. A: `RULES.md:15` (RULE-003) — "< 70%… [Fonte: ENGENHARIA GERAL Doc06 §4…]".
Loc. B: `scratchpad/enggeral.txt` — grep de "70%/75%/60%/7-9" não retorna nenhum número; a fonte defere à governança (`:1337`). Os números aparecem em `ARIA_Plano_Mestre.md:22,204,776` como calibração.
Natureza: Citação de fonte imprecisa (documentado ≠ fonte real). Impacto: integridade do RULES (Passo 4 do Revisor). → Q-002.

**CONFLITO-005** · [FONTE] — "5 Salvaguardas Constitucionais do CEE-001 §10"
Documentos: CEE-001 §10 (real) vs RULES/atomic-spec/revisor/especificador
Loc. A: `CEE-001_Versao_Consolidada.md:231-237` — 5 salvaguardas de **economia/roteamento**.
Loc. B: `RULES.md:249-255` (RULE-CEE-004) — 5 salvaguardas de **sinal** "[Fonte: CEE-001 §10]"; `revisor.md:113`; `especificador.md:187`.
Natureza: Misatribuição de fonte / termo com dois sentidos. Impacto: Constitution Check universal. → Q-003.

**CONFLITO-006** · [FONTE] — R:R 3:1 vs 2:1 (e citação auto-contraditória)
Seções: RULES.md (RULE-006 vs RULE-ICT-002) + CONSTITUTION/synthesis
Loc. A: `RULES.md:24` (RULE-006) — "< 3:1".
Loc. B: `RULES.md:150` (RULE-ICT-002) — "< 2:1 … [Fonte: ARIA … '1:3 mínimo']"; `CONSTITUTION.md:153`; `synthesis.spec.md:22`.
Loc. C: `ARIA_Plano_Mestre.md:22` — "R:R mínimo 1:3".
Natureza: Contraditório interno + citação auto-contraditória. Impacto: SPEC-013/014. → Q-004.

**CONFLITO-007** · [FONTE] — Quem cria hipótese
Documentos: CONSTITUTION vs KERNEL/CHM-001
Loc. A: `CONSTITUTION.md:186` — "Hypotheses | Elliott Specialist".
Loc. B: `scratchpad/kernel.txt` EC-COG-002 (p.27) — "Quem produz hipóteses: Todos os agentes especializados"; `CHM-001_Capitulo1.md:210`.
Natureza: Contraditório / escopo do objeto "hipótese". Impacto: SPEC-001/004/012. → Q-005.

**CONFLITO-008** · [FONTE] — PPQ-001 existe vs não existe
Documentos: revisor.md vs CATALOGO/RULES/AGENTS
Loc. A: `revisor.md:59` — "Não há PPQ-001".
Loc. B: `CATALOGO_OFICIAL_ORYX.md:23` — "PPQ-001… BASELINED"; `RULES.md:328` (RULE-PPQ-001).
Natureza: Contraditório. Impacto: governança/Revisor. → Q-010.

**CONFLITO-009** · [FONTE] — 3E vs 4Es
Documentos: CEE-001/CONSTITUTION vs ATOMIC-SPEC/especificador/GEH-001
Loc. A: `CEE-001…md:63-76`; `CONSTITUTION.md:160-168` — 3E (para em Eficiência).
Loc. B: `ATOMIC-SPEC.md:148`; `RETOMADA/GEH-001…md:98-116` — 4Es (+ Economicidade).
Natureza: Sobreposição/lacuna (nível a mais). Impacto: método/Passo 6 do Revisor. → Q-009.

**CONFLITO-010** · [FONTE] — Expansão de "SOT" e nome ORYX
Documentos: CONSTITUTION vs AGENTS/especificador vs canônicos
Loc. A: `CONSTITUTION.md:1` — "Sistema de Operações e Tendências".
Loc. B: `AGENTS.md:5`; `especificador.md:29` — "Sistema Operacional de Trading".
Loc. C: `CATALOGO_OFICIAL_ORYX.md:2` — "ORYX AGENT".
Natureza: Termo fundacional inconsistente. Impacto: identidade/cabeçalhos. → Q-015.

**CONFLITO-011** · [INFERÊNCIA] — Model ID dos agentes
Seções: frontmatter dos agentes vs cabeçalho dos root docs
Loc. A: `especificador.md:8` / `revisor.md:8` — "model: **claude-opus-4-5**".
Loc. B: `ROADMAP.md:5` / `ATOMIC-SPEC.md:5` — "Claude Code (**Opus 4.8**…)".
Natureza: Inconsistência menor de configuração. Impacto: operacional (menor). *(Sem pergunta dedicada — registrar e alinhar na próxima emenda.)*

**CONFLITO-012** · [FONTE] — Dimensionalidade do Conviction Vector (interna)
Seções: CONSTITUTION P02 vs synthesis.spec (escopo vs output) vs AUDITORIA
Loc. A: `CONSTITUTION.md:37-39` — 7 dimensões.
Loc. B: `specs/synthesis.spec.md:18-19` (7) vs `:100` (5).
Loc. C: `scratchpad/AUDITORIA…txt §J.3` — 8.
Natureza: Inconsistência interna numérica. Impacto: SPEC-003. → Q-008.

**CONFLITO-013** · [FONTE] — Specs de agente hardcodam limiares fechados
Seções: specs/*.spec.md vs INV-03
Loc. A: `specs/synthesis.spec.md:21,44,48,57` — "≥70%", "≥7/9", "≥2:1" como critérios de aceitação fechados.
Loc. B: `ATOMIC-SPEC.md:255` (INV-03).
Natureza: As specs legadas precedem o método; contaminam decisão aberta como fechada. Impacto: SPEC-010/012/013/014 (refazem esses agentes). → Q-002.

**CONFLITO-014** · [FONTE] — Estados do objeto do Blackboard divergem entre si
Seções: RULE-BB-003 vs KERNEL EC-COG-004
Loc. A: `RULES.md:297-299` (RULE-BB-003) — PROPOSED→VALIDATED→ACTIVE→SUPERSEDED.
Loc. B: `scratchpad/kernel.txt` (p.58) — Publicado→Atualizado→Confirmado→Contestável→Invalidado→Arquivado.
Natureza: Contraditório (mesma fonte declarada, KERNEL EC-COG-004). Impacto: SPEC-004. → Q-006.

---

## Apêndice B — Inventário de Ambiguidades de Fronteira (AMBIGUIDADE-NNN)

**AMBIGUIDADE-001** — SPEC-001 × CHM-001
Ponto de fronteira: quais campos/comportamentos do CHM-001 a SPEC-001 **consome** vs **redefine**. O CHM-001 (`Cap1 §1.1`) declara que **não** define ciclo de vida operacional, algoritmos nem "comportamento operacional de agentes" — exatamente a camada da SPEC-001. Falta demarcar onde termina o objeto (CHM) e começa o protocolo (SPEC-001).
Evidência: `CHM-001_Capitulo1.md:24-31`; `ROADMAP.md:93-104`.
Opções: [O1] SPEC-001 só protocolos/transições, zero campos novos; [O2] SPEC-001 pode acrescentar campos operacionais (ex.: índice de estado ativo) por referência. Impacto: escopo da SPEC-001. → Q-001, Q-006.

**AMBIGUIDADE-002** — SPEC-001 × SPEC-004 (estado epistêmico vs estado de publicação)
Ponto de fronteira: o estado do CHM (epistêmico) e o estado do Blackboard (publicação) são a mesma máquina ou duas? Ver CONFLITO-014 e Q-006.
Evidência: `CHM-001_Capitulo1.md:137-147` vs `RULES.md:297-299`.
Opções: [O1] uma máquina (CHM); [O2] duas camadas com mapeamento. → Q-006.

**AMBIGUIDADE-003** — SPEC-002 × CEM-001
Ponto de fronteira: a SPEC-002 é a "camada Harness/operacional sobre CEM-001", mas o CEM-001 já especifica ciclo de vida, linhagem, produtores/consumidores e certificação (Caps 4-8). Resta pouca camada operacional não coberta — e ela colide com a lista de produtores (Macro/Sentiment/Risk/Context vs 5 agentes).
Evidência: `CEM-001…md:389-506` (ciclo de vida completo); `ROADMAP.md:123-126`.
Opções: [O1] SPEC-002 = só orquestração de produção/consumo no runtime; [O2] SPEC-002 = provenance/qualidade/fusão operacional. Impacto: escopo SPEC-002. → Q-014.

**AMBIGUIDADE-004** — SPEC-003 × B-001 (Fusion/Conviction/Synthesis)
Ponto de fronteira: ver Q-007. Onde termina o Evidence Fusion Engine e começa o Conviction Engine, e se o Synthesis os absorve.
Evidência: `CEM-001…md:664-667`; `CONSTITUTION.md:100-104`; `ROADMAP.md:130-133`. → Q-007.

**AMBIGUIDADE-005** — SPEC-001 × SPEC-003 (slot de convicção: referência ou valor?)
Ponto de fronteira: o roadmap diz que a hipótese "referencia o objeto de convicção sem fechar fórmula" (INV-03), mas o CHM-001 tem campo `Confidence` (0.0-1.0, imutável por versão) e o KERNEL tem "Conviction Local". A hipótese **carrega** um valor de confiança local **e** referencia a convicção global? A fronteira entre `Hypothesis Confidence` (CHM) e `Conviction Global` (CCM) precisa ser operacionalizada sem fechar J-001.
Evidência: `CHM-001_Capitulo1.md:116-127,180-182`; `ROADMAP.md:101-102,116`.
Opções: [O1] hipótese carrega só `Confidence` local + referência à convicção global; [O2] slot de convicção é pura referência. Impacto: SPEC-001/003. → Q-008 (relacionado).

**AMBIGUIDADE-006** — SPEC-001 × SPEC-004/006 (Hypothesis Registry)
Ponto de fronteira: o roadmap coloca "Hypothesis Registry como serviço lógico" no escopo da SPEC-001, mas no KERNEL o Registry é uma **"Evolução proposta"** (não homologada), e o armazenamento físico pertence a SPEC-004/006. Falta definir o que é "serviço lógico" (SPEC-001) vs "armazenamento" (SPEC-004/006).
Evidência: `scratchpad/kernel.txt` (p.38, "Evolução proposta… Hypothesis Registry"); `ROADMAP.md:98,109`.
Opções: [O1] Registry = contrato lógico na SPEC-001 (ID/versão/índice), storage adiado; [O2] Registry inteiro adiado para SPEC-004/006. Impacto: escopo SPEC-001. → Q-001.

**AMBIGUIDADE-007** — SPEC-014 × SPEC-003 (síntese vs convicção com B-001 aberto)
Ponto de fronteira: como descrever a fronteira Synthesis↔Conviction enquanto B-001 está aberto, sem fechá-lo. O roadmap condiciona SPEC-014 à resolução de B-001/J-001.
Evidência: `ROADMAP.md:199-200`; `ATOMIC-SPEC.md:237`.
Opções: [O1] resolver B-001 agora (Q-007); [O2] especificar SPEC-003 com fronteira condicional e marcar SPEC-014 como bloqueada. → Q-007.

---

## Apêndice C — Termos sem definição canônica (TERMO-NNN)

**TERMO-001** — "SOT" (expansão). Encontrado em: `CONSTITUTION.md:1` ("Sistema de Operações e Tendências") vs `AGENTS.md:5`/`especificador.md:29` ("Sistema Operacional de Trading"). Conflito: duas expansões. → Q-015.

**TERMO-002** — "ORYX" vs "SOT". Encontrado em: `CATALOGO_OFICIAL_ORYX.md:2` ("ORYX AGENT", "ecossistema ORYX/SOT") vs repo ("SOT-Harness"). Lacuna: relação produto↔sistema não declarada. → Q-015.

**TERMO-003** — "Structural Agent" / "Institutional Agent". Encontrado em: `CEM-001…md:163-170`, `SAS-001…` vs `AGENTS.md:42-48` ("Elliott Specialist"/"SMC Specialist"). Lacuna: equivalência não declarada. → Q-014.

**TERMO-004** — "Fusion Engine" / "Evidence Fusion Engine" / "Conviction Engine". Encontrado em: `CEM-001…md:172` (Fusion Engine, produtor DERIVED) vs `ROADMAP.md:130` ("Conviction Vector & Evidence Fusion Engine") vs `CONSTITUTION.md:102` (Conviction Engine). Conflito: três entidades possivelmente sobrepostas. → Q-007.

**TERMO-005** — "Hypothesis Registry" / "Hypothesis Manager" / "Hypothesis Engine". Encontrado em: `scratchpad/kernel.txt` (Hypothesis Manager, p.36; Hypothesis Registry, p.38) vs `CEM-001…md:181` ("Hypothesis Engine") vs `ROADMAP.md:98` ("Hypothesis Registry"). Lacuna: mesmo componente, três nomes; um deles é "evolução proposta". → Q-001.

**TERMO-006** — "5 Salvaguardas Constitucionais". Definições diferentes: economia (`CEE-001 §10`) vs sinal (`RULES.md` RULE-CEE-004). → Q-003.

**TERMO-007** — "dimensões do Conviction Vector". Conjunto varia (7/5/8). Ver CONFLITO-012. → Q-008.

**TERMO-008** — "CCM-001 / CDM-001 / CNM-001" (Canonical Conviction/Decision/Narrative Model). Referenciados como se existissem (`ROADMAP.md:50`, `CHM-001_Capitulo1.md:180`, `CEM-001…md:108-111`), mas **não redigidos** (`CATALOGO_OFICIAL_ORYX.md:113`). Lacuna: termos normativos sem documento-fonte. → Q-001, Q-002 (CCM-001 = J-001).

---

## Apêndice D — Decisões abertas não rastreadas em `atomic-spec.md §12` (DECISÃO-ABERTA-NNN)

> `atomic-spec.md §12` rastreia J-001, B-001, G-001, H-001, I-001, K-001, L-001, C-001. As decisões abaixo **não** estão nessa tabela e emergiram desta auditoria.

**DECISÃO-ABERTA-001** — Status de baseline dos modelos canônicos (CHM/CEM/CCM/CDM/CNM) e reconciliação com o Catálogo. Fonte: `CATALOGO_OFICIAL_ORYX.md:113` vs `ROADMAP.md:50`. Impacto: SPEC-001/002/003. Rastreada? **NÃO**. → Q-001.

**DECISÃO-ABERTA-002** — Qual conjunto de "5 Salvaguardas" é constitucional e sob qual fonte. Fonte: `CEE-001 §10` vs `RULES.md:249`. Impacto: Constitution Check universal. Rastreada? **NÃO**. → Q-003.

**DECISÃO-ABERTA-003** — Proveniência e status (calibrável vs constitucional) dos limiares numéricos. Fonte: `ARIA_Plano_Mestre.md:776` (calibrar) vs `RULES.md`/`CONSTITUTION.md` (fixo). Impacto: SPEC-003/014. Rastreada? Parcial (J-001 cobre fórmula/pesos/limiares do Conviction Vector, **não** a proveniência do R:R/score nem o status "piloto"). → Q-002/Q-004.

**DECISÃO-ABERTA-004** — 3E vs 4Es na hierarquia inviolável. Fonte: `CEE-001 §3` vs `ATOMIC-SPEC.md:148`. Impacto: método. Rastreada? **NÃO**. → Q-009.

**DECISÃO-ABERTA-005** — Status/escopo remanescente do PPQ-001. Fonte: `revisor.md:59` vs `CATALOGO:23`. Impacto: governança/Revisor. Rastreada? **NÃO**. → Q-010.

**DECISÃO-ABERTA-006** — Status normativo de CONSTITUTION/RULES/CONFLICT-MAP (fora do Catálogo). Fonte: `ATOMIC-SPEC.md:78` vs `CATALOGO`. Impacto: autoridade de citação de todas as Specs. Rastreada? **NÃO**. → Q-011.

**DECISÃO-ABERTA-007** — Número/identidade das dimensões do Conviction Vector. Fonte: CONFLITO-012. Impacto: SPEC-003. Rastreada? **NÃO** (J-001 = fórmula/pesos/limiares, não dimensões). → Q-008.

**DECISÃO-ABERTA-008** — Multiplicidade de produtores de hipótese. Fonte: CONFLITO-007. Impacto: SPEC-001/004/012. Rastreada? **NÃO** (INV-01/02 tratam de hierarquia, não de exclusividade de criação). → Q-005.

**DECISÃO-ABERTA-009** — Máquina de estados canônica da hipótese/objeto do Blackboard. Fonte: CONFLITO-014, Q-006. Impacto: SPEC-001/004. Rastreada? **NÃO**. → Q-006.

**DECISÃO-ABERTA-010** — Existência do briefing PP-SPEC-001. Fonte: `ROADMAP.md:375`. Impacto: início SPEC-001. Rastreada? **NÃO**. → Q-012.

**DECISÃO-ABERTA-011** — Integridade de caminhos (validador em raiz vs `scripts/`; agentes em raiz vs `.claude/agents/`). Fonte: `revisor.md:66`; estrutura real. Impacto: gate do Revisor em toda revisão. Rastreada? **NÃO**. → Q-013.

---

## Encaminhamento

Este questionário é o mecanismo de escalada. Nenhum achado foi resolvido pelo Especificador; todos aguardam decisão de Andraus. Após as respostas:
1. O Especificador incorpora as decisões a `ROADMAP.md` e `ATOMIC-SPEC.md` (e às emendas necessárias em CONSTITUTION/RULES/CONFLICT-MAP, CEE-001, Catálogo e agentes conforme cada opção escolhida).
2. Submete as alterações ao Revisor para parecer de integridade (GRE-001/HRE-001).
3. **Só então** arranca a SPEC-001 — terreno limpo.

*Fim do Questionário de Resolução v1 — SOT Arranque.*
