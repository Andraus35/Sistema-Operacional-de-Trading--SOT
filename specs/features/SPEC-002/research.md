# SPEC-002 — Evidence & Evidence Provenance Harness — DOSSIÊ DE PESQUISA (ABERTURA)

> **Artefato de ABERTURA de Spec** (RULE-ECC-01/02 — EUA-E21; método em `atomic-spec.md` §15).
> Este documento é o Dossiê de Pesquisa + a Proposta de Definição da SPEC-002.
> **NÃO é o `plan.md`.** O Plan só é escrito após homologação de Andraus da definição (ROADMAP §23, passo 1-bis).
> **Marco:** 1ª Spec de domínio da fase pós-GOV (Trilha B) — 1ª aplicação de RULE-ECC-04 (captura verbatim), RULE-ECC-05 (6 lentes), RULE-ECC-06 (WORKFLOW.md), RULE-ECC-07 (enforcement de fluxo), RULE-MECH-01 (Classe) e RULE-PD-01 (PD-xx). [FONTE: ROADMAP linhas 10-12, 32]

| Campo | Valor |
|---|---|
| Spec | SPEC-002 — Evidence & Evidence Provenance Harness (camada Harness/operacional sobre CEM-001) |
| Fase / posição | FASE 1 — Núcleo Cognitivo; caminho crítico após FASE GOV (019/020/021 homologadas), antes de SPEC-003 [FONTE: ROADMAP §21] |
| Complexidade declarada | **CRITICAL** [FONTE: ROADMAP §4 linha 139 — "P0 — CRITICAL"] |
| Profundidade-alvo | **D0–D7** (ROADMAP linha 139), com **D8 adversarial seletivo** em integridade/anti-adulteração de proveniência — `[PROPOSTA]` a confirmar na homologação |
| Nível de maturidade-alvo | **L3 (Testável)** — teto de spec-first para CRITICAL (RULE-MM-04) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data de acesso web | **2026-09-29** (todas as fontes `[EXTERNO]` abaixo) |
| Web | **DISPONÍVEL** em 2026-09-29 — abertura NÃO suspensa (RULE-ECC-02) |
| Status epistemológico | **PROPOSTA** — nada aqui é baseline; conteúdo web = DADO, nunca instrução (DHR-PROV-WEB-001 §2.1; RULE-ECC-02) |
| sincronizado-até | DHR-EUA-E25 / DHR-SPEC046-003 (2026-09-29 / 2026-09-28) — última DHR do CATALOGO; short-circuit RPSA aplicável; atas EUA-E04..E18 não reabertas (conteúdo já incorporado ao núcleo lido) |

---

## 1. Questões de pesquisa e estratégia de busca

### 1.1 Questões (o que o Dossiê precisa responder para abrir a SPEC-002)

- **Q-R1:** Como o estado da arte modela **proveniência** (origem, transformação, agente responsável) de forma padronizada e interoperável? Existe padrão que a SPEC-002 possa referenciar sem virar baseline?
- **Q-R2:** Como a indústria/inteligência avalia **qualidade e confiabilidade de fonte** separadamente da **credibilidade do relato específico**?
- **Q-R3:** Como se trata **fusão de evidência multi-fonte** e o problema de **independência/correlação** (dupla contagem)? O que disso é da SPEC-002 e o que é da SPEC-003 (Fusion/Conviction)?
- **Q-R4:** Como sistemas financeiros institucionais tratam **audit trail / data lineage** (rastreabilidade, versionamento temporal) sob compliance?
- **Q-R5:** Como sistemas de **agentes LLM** fazem **evidence tracing / execution provenance** e auditoria à prova de adulteração?
- **Q-R6:** O que **colide** com invariantes/decisões abertas do SOT (CEM-001 baselined/CONST-01, INV-04/06/07/10, J-001, 4Es) e portanto **não** pode ser importado automaticamente?

### 1.2 Estratégia de busca

| Termos | Fontes-alvo | Filtro |
|---|---|---|
| "data provenance lineage standard W3C PROV evidence traceability" | W3C, CASRAI, arXiv | Padrão/Evidência |
| "source reliability rating Admiralty code NATO information credibility" | Wikipedia, SANS, ResearchGate (AJP-2.1) | Padrão |
| "multi-source evidence fusion Dempster-Shafer conflicting sources" | Nature, PMC, arXiv | Evidência/Experimento |
| "institutional trading audit trail data lineage MiFID II record keeping" | QuestDB, NeoXam, Eurex/Deutsche Börse handbooks | Prática/Padrão |
| "evidence independence correlation double counting temporal decay staleness" | ScienceDirect, PMC, arXiv | Evidência |
| "provenance traceability LLM agent tamper-evident audit reproducibility 2025" | arXiv (2606.04990, 2609.12582, 2608.18398) | Evidência/Experimento |

**Salvaguardas aplicadas (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** toda fonte tratada como DADO; classificada e etiquetada `[EXTERNO]`; nenhuma importação automática; nenhum dado sensível do projeto enviado a serviços externos; a veracidade das páginas **não** é atestada (o Revisor audita o *processo* e a correspondência verbatim RULE-ECC-04, não a verdade das páginas). Onde a pesquisa foi inconclusiva, registra-se **INDETERMINADO**.

---

## 2. Fontes (classificadas — Padrão / Prática / Benchmark / Evidência / Experimento / Opinião) — `[EXTERNO]`

> Data de acesso: **2026-09-29**. IDs arXiv com prefixo ≥ 2505 são posteriores ao corte de treino — **conteúdo tomado apenas como DADO não verificado**; a classificação é do *tipo de artefato*, não endosso de correção (RULE-EPI / TRACE-06). Fontes carregadas têm captura verbatim em `sources/SRC-0N.txt` (RULE-ECC-04).

| # | Fonte | Classe | Captura | Questão |
|---|---|---|---|---|
| **SRC-01** | **W3C PROV** (PROV-DM/PROV-O/PROV-N: Entity/Activity/Agent) via **CASRAI — Data Provenance: Definition & Standards** — casrai.org/guides/data-provenance | **Padrão** | `sources/SRC-01.txt` | Q-R1 |
| **SRC-02** | **Admiralty code / NATO AJP-2.1 (STANAG 2511)** — reliability A-F × credibility 1-6 — en.wikipedia.org/wiki/Admiralty_code | **Padrão** | `sources/SRC-02.txt` | Q-R2 |
| **SRC-03** | **Audit Trail and Traceability in Financial Data — NeoXam DataHub** (+ contexto MiFID II/lineage bitemporal, QuestDB/Progress) | **Prática** | `sources/SRC-03.txt` | Q-R4 |
| **SRC-04** | **From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents** (arXiv 2606.04990) | **Evidência** (survey) | `sources/SRC-04.txt` | Q-R5 |
| **SRC-05** | **A New Evidential Reasoning Rule Considering Evidence Correlation…** (PMC12116114) | **Evidência** | `sources/SRC-05.txt` | Q-R3 |
| E6 | **FNBT: Full Negation Belief Transformation… Dempster-Shafer** (arXiv 2508.08075) + **improved D-S / tunnel collapse risk** (Nature s41598-022-07171-x) | **Experimento** | — (não carregada; verbatim INDETERMINADO — fetch sem trecho limpo) | Q-R3 |
| E7 | **NovaFabric: Tamper-Evident, Replayable Evidence for AI Agent Runs** (arXiv 2609.12582); **LEDGER: Claim-to-Evidence Trace Graphs** (2608.18398); **Agent Flight Recorder: on-chain anchoring** (2609.01931); **AuditableLLM: hash-chain audit** (MDPI) | **Experimento** | — (contexto; não carregada isoladamente) | Q-R5 |
| E8 | **Tracing the Data Trail: Survey of Data Provenance… in LLMs** (arXiv 2601.14311) | **Evidência** (survey) | — (contexto) | Q-R1/R5 |

**Nota RULE-MET-01 (não-fabricação):** E6 é citado como classe de artefato; **não** sustenta alegação carregada por trecho verbatim (fetch retornou sem trecho limpo → INDETERMINADO). A decisão sobre fusão (§6) repousa na **arquitetura interna do SOT** (B-001/SPEC-003), não em E6 — logo E6 não exige `sources/*.txt` (RULE-ECC-04 incide só sobre fonte que *sustenta* alegação carregada).

### 2.1 Trechos verbatim das fontes carregadas (RULE-ECC-04 — citação literal entre aspas)

- **SRC-01 (W3C PROV / CASRAI):** "Data provenance is the documented history of a research data object: where it came from, what happened to it, and who or what acted on it" [EXTERNO, acesso 2026-09-29, `sources/SRC-01.txt`].
- **SRC-02 (Admiralty code):** "Each descriptor is considered in isolation to ensure that the reliability of the source does not influence the assessed accuracy of the report." [EXTERNO, `sources/SRC-02.txt`].
- **SRC-03 (NeoXam):** "Audit trail and traceability refer to the systematic logging and historical tracking of data activities within an enterprise system." [EXTERNO, `sources/SRC-03.txt`].
- **SRC-04 (Agent Traces to Trust):** "Evidence tracing and execution provenance address this gap by modeling how retrieved evidence, tool outputs, memory items, environment observations, intermediate claims, actions, and final answers are connected" [EXTERNO, `sources/SRC-04.txt`].
- **SRC-05 (Evidence Correlation ER rule):** "The Bayesian probabilistic foundation of ER rules requires evidence independence, which may be violated in complex systems with inherent indicator correlations." [EXTERNO, `sources/SRC-05.txt`].

---

## 3. Lentes de domínio (RULE-ECC-05 / EUA-E23) — quadro de aplicabilidade

**Determinação central `[INFERÊNCIA]`:** a SPEC-002 é uma **camada infraestrutural de proveniência/qualidade/ciclo-de-vida de evidência sobre CEM-001**, que é por definição **neutro de domínio** — CEM-001 Princípio 1 (Neutralidade): "O modelo deverá ser independente de qualquer disciplina específica. Uma evidência estrutural, institucional ou macroeconômica deverá utilizar exatamente o mesmo padrão de representação." [FONTE: CEM-001 Cap.1]. Logo, a SPEC-002 **carrega** evidência de qualquer escola sem realizar análise de nenhuma escola. As 6 lentes tratam do **conteúdo** analítico da evidência; a SPEC-002 trata do **envelope** (origem, versão, linhagem, qualidade intrínseca, conflito-como-metadado). Portanto, as 6 lentes de domínio **NÃO se aplicam como alvo de pesquisa de escola** — ausência **justificada** (RULE-ECC-05: "ausência justificada das 6 lentes = correto, não é achado").

| Lente | Aplica? | Justificativa (RULE-ECC-05) |
|---|---|---|
| **(1) Elliott** | **Não (infraestrutural)** | SPEC-002 não conta ondas nem cria hipótese estrutural; apenas carrega proveniência de evidência produzida pelo Structural Agent (SPEC-010). Realizar pesquisa Elliott aqui violaria a neutralidade do CEM-001. |
| **(2) Fibonacci** | **Não (infraestrutural)** | idem — proporção geométrica é conteúdo de evidência, não do seu envelope de proveniência. |
| **(3) SMC** | **Não (infraestrutural)** | idem — liquidez/BOS/FVG são conteúdo produzido pelo Institutional Agent (SPEC-012). |
| **(4) ICT** | **Não (infraestrutural)** | idem — timing/killzone é conteúdo operacional (SPEC-013); ICT não cria hipótese (INV-02). |
| **(5) Confluência intra-escola** | **Não como escola; SIM como requisito de metadado** | A SPEC-002 **não** computa confluência (isso é dos agentes/Fusion). Mas o **substrato de independência/correlação** de evidência (SRC-05; RULE-004: "evidências causalmente relacionadas contadas como uma única") **exige** que o envelope de proveniência registre origem/linhagem/ferramenta/Skill produtora com granularidade suficiente para que a confluência e a dedução de dupla-contagem sejam computáveis **downstream** (SPEC-003). Isso é requisito de campo, não pesquisa de escola. |
| **(6) risco-retorno** | **Não** | Sizing/R:R/heat são do agente de risco (BL-018/RISK-SPEC); nada de risco entra em evidência (CEM-001 restrição: evidência não contém decisão/convicção/execução). INV-04 (custo nunca no Conviction) reforça a separação. |

**Conclusão da §3:** nenhuma das 6 lentes é "aplicável mas não pesquisada" (o que seria Crítica). Todas declaradas **não-aplicáveis com justificativa** ancorada em CEM-001 (neutralidade) + INV-06/INV-10. O único resíduo domínio-tocante é o **requisito de campo** da lente (5) — tratado como requisito de metadado de independência, **não** como análise de escola. Coerente com a §7 (SPEC-002 não declara `PD-xx`).

---

## 4. Insumo de orquestração (RULE-ECC-06 / WORKFLOW.md)

**Gatilho da RULE-ECC-06 estritamente aplicável?** A RULE-ECC-06 exige leitura+decisão-por-etapa E1–E8 quando a Spec (a) abre/toca **K-001, SPEC-018 ou SPEC-045-RUNTIME-001**, ou (b) especifica **agente operacional / manager / risco**. A SPEC-002 **não** é agente do fluxo nem toca K-001/018/045-runtime — é **camada de dado/suporte consumida pelos agentes**. Logo, a obrigação estrita da RULE-ECC-06 **não é disparada**.

**Contudo — leitura reforçada cumprida (EUA-E24 Q1):** para o Especificador, na abertura da SPEC-002, a leitura de `WORKFLOW.md` é **passo obrigatório reforçado** independentemente do gatilho. Cumprida. Mapeamento leve (insumo, **nada fechado — CONS-01**):

| Etapa | Papel da proveniência de evidência (SPEC-002) | Decisão |
|---|---|---|
| E3 Estrutural / E4 Institucional / E6 Operacional | Cada agente "observa, marca, **classifica**, trata evidência" e entrega via `runtime-workflow.conviction-report` — que já carrega `evidence_ref`/`evidence_classification` (confirmado em `schemas/runtime-workflow.conviction-report.json`). A SPEC-002 define **o que** é essa evidência classificada e sua proveniência. | **Adiar** o consumo (é dos agentes SPEC-010/012/013); **adotar** como requisito que o envelope de proveniência da SPEC-002 seja suficiente para preencher `evidence_ref`/`evidence_classification`. |
| E5/E7 Manager (convicção macro/global) | Consome evidência ACTIVE (CEM-001) para formar convicção. | **Adiar** (Fusion/Conviction = SPEC-003/014; B-001 fechada). SPEC-002 só entrega evidência com proveniência completa. |
| E8 Risco | Fora de escopo — risco não é evidência. | **Rejeitar** inclusão. |

**Achado:** a distinção "convicção em camadas" (WORKFLOW §6 item 2) e a "convicção de risco" (RISK-CONV-001) permanecem `[DECISÃO NECESSÁRIA]` — a SPEC-002 **não** as toca (não computa convicção). Tratar o WORKFLOW como decisão fechada seria Crítico (CONS-01) — não o faço.

---

## 5. Enforcement (RULE-ECC-07 / WORKFLOW.md §7-bis.2)

**Gatilho da RULE-ECC-07 aplicável?** A RULE-ECC-07 exige Enforcement Contract **compatível com a Tabela §7-bis.2** quando a Spec especifica um **agente do fluxo** ou uma **transição E1→E8**. A SPEC-002 **não** especifica agente do fluxo nem transição E1→E8 — é camada de suporte. Logo a obrigação de compatibilidade com a Tabela §7-bis.2 **não é disparada** (declarado, não ignorado — RULE-ECC-07: "nunca ignora em silêncio").

**Mas Enforcement Contracts ordinários SÃO exigidos (ENF-01):** a SPEC-002 tem **efeitos próprios** — publicar evidência (Blackboard), versionar (SUPERSEDED), invalidar (INVALIDATED + evento *Evidence Invalidated*), arquivar. Cada BASpec com efeito declarará seu Enforcement Contract (§10.3) **no Plan**, não aqui. Antecipação `[PROPOSTA]` de pisos (a confirmar no Plan):
- Publicar evidência (produtor autorizado, contrato CEM-001) → **E1/E2** (piso Evidência = E2; PRECOND = produtor autorizado + contrato completo; FAIL-CLOSED: publicação incompleta rejeitada — CEM-001 "proibido publicar Evidências incompletas").
- Transição de estado / invalidação com propagação a derivadas (linhagem) → **E2/E3** (efeito sobre objetos derivados; POSTCOND = histórico íntegro, INV-07; Detector≠Gate para avaliação de impacto — Fusion Engine inicia avaliação, não cascata automática).
- **Detector ≠ Gate (ENF-03):** qualquer sinal semântico de qualidade/confiabilidade de evidência é **detector/sinal reportado**, nunca gate; o gate de aceitação de evidência é determinístico (conformidade de contrato CEM-001).

---

## 6. Comparação com a arquitetura SOT e CEM-001 — adotar / adaptar / rejeitar / adiar

**Princípio-mãe (CONST-01):** a SPEC-002 **constrói SOBRE** CEM-001 (baselined) — **não o redefine**. CEM-001 já define o *objeto* Evidência (contrato, ciclo de vida, linhagem, conformidade). A SPEC-002 especifica a *camada operacional/Harness* que CEM-001 deixa aberta (ROADMAP linha 123-124/141). CEM-001 é o **idioma canônico** (INV-10).

### 6.1 O que CEM-001 já cobre (NÃO re-especificar — CONST-01)
Contrato de 4 camadas (Identidade/Origem/Conteúdo/Rastreabilidade); `Producer Type` AGENT/ENGINE; `Evidence Origin Type` PRIMARY/DERIVED; `Domain`/`Market Context` (enums governadas GMC-001); `Evidence Strength` (float 0-1, ≠ Convicção); `Timeframe Reference`; `Source Reference`; `Lineage`; estados ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED + transições; imutabilidade pós-publicação (Status = único mutável); evento *Evidence Invalidated* via EC-COG-005; Cognitive Trace Reconstruction (KG); níveis de conformidade Producer/Consumer/Repository.

### 6.2 O que a SPEC-002 ACRESCENTA (camada Harness/operacional — o gap)

| Item de escopo (ROADMAP linha 141) | Coberto por CEM? | Decisão | Fonte/Âncora |
|---|---|---|---|
| **Origem / provenance / versão** | Objeto sim; **operação não** | **ADOTAR** protocolo operacional de proveniência (criar/publicar/superseder), **ADAPTAR** alinhamento conceitual ao triplo PROV Agent/Activity/Entity (CEM já é PROV-shaped: Producer=Agent, produção=Activity, Evidence=Entity) — sem importar vocabulário PROV-O/RO-Crate | SRC-01; CEM-001 Cap.3/5 |
| **Ferramenta / Skill que produziu** | Parcial (`Producer ID`) | **ADAPTAR** — granularidade operacional ferramenta/Skill + fronteira **Observação(Skill)≠Evidência(Agente)** (INV-06) | INV-06; SRC-04 |
| **Tipo / qualidade / independência** | `Evidence Strength` (qualidade intrínseca) sim; **independência não** | **ADAPTAR** — registrar metadado de independência/correlação suficiente para downstream detectar dupla-contagem (RULE-004); **ADIAR** a fórmula de fusão/desconto | SRC-05; RULE-004 |
| **Confiabilidade da FONTE (track-record) × credibilidade do relato** | `Evidence Strength` = relato; **track-record da fonte não** | **ADAPTAR** o **princípio de dois eixos** (Admiralty): separar confiabilidade histórica do produtor da força do relato específico. **`[DECISÃO NECESSÁRIA — DN-1]`**: campo de track-record é metadado da camada-Harness OU extensão Categoria A/B do CEM (via GMC-001)? Não fechar. NÃO importar códigos A-F/1-6 literais (rejeitar). NUNCA colidir com convicção (INV-04). | SRC-02; DN-1 |
| **Temporalidade / aging / staleness** | `Creation Timestamp` sim; **política de aging não** | **ADAPTAR** — suporte a validade temporal/staleness como metadado; **ADIAR** qualquer fórmula de decaimento (toca J-001/N-001/SPEC-003) | SRC-05 (temporal decay); J-001 |
| **Favorável / contraevidência / inconclusiva / ausente** | Parcial (Strength/Interpretation); **taxonomia operacional e "ausente" não** | **ADOTAR** taxonomia operacional favorável/contra/inconclusiva; **`[DECISÃO NECESSÁRIA — DN-3]`**: "evidência de ausência" está no escopo da SPEC-002 ou adiada? | RULE-009; DN-3 |
| **Conflito** | Não (é da síntese) | **ADAPTAR** — SPEC-002 registra o **metadado** que permite detectar `directional_conflict` (RULE-005) downstream; **não** resolve conflito (isso é Synthesis, RULE-SY-001) | RULE-005; INV-01 |
| **Relação com hipótese** | Referência (CHM-001) | **ADOTAR** protocolo operacional de vínculo evidência→hipótese **por referência** (INV-06/INV-10); fronteira `Fonte→Dado→Evidência→Hipótese` | CHM-001; ROADMAP linha 141 |
| **Auditabilidade / reconstrução** | KG Trace Reconstruction (objeto) | **ADAPTAR** — suporte a lineage bitemporal ("o que se sabia e quando", MiFID) + princípio tamper-evident/append-only (SOT já tem: INV-07, RULE-BB-004); **ADIAR** mecanismo físico (KG=SPEC-006; auditoria=SPEC-041) e **REJEITAR** on-chain/cripto como baseline (4Es Economicidade; over-engineering spec-first) | SRC-03; SRC-04; E7; INV-07 |

### 6.3 REJEITAR (não importar como baseline)
- Vocabulário/serialização PROV-O, RO-Crate, SBOM/SLSA como contrato — **CEM-001 é o idioma canônico** (INV-10); importação automática proibida (RULE-ECC-02).
- Códigos literais Admiralty A-F/1-6 como enum — só o **princípio** de dois eixos é adaptável.
- Ancoragem on-chain / hash-chain criptográfico (Agent Flight Recorder / AuditableLLM) como baseline — append-only + KG já entregam auditabilidade; cripto fere Economicidade sem ganho de Eficácia agora (registrar como opção futura, não baseline).

### 6.4 ADIAR (fronteira com outras Specs / decisões abertas)
- **Fusão de evidência multi-fonte** (Dempster-Shafer e derivados) → **SPEC-003** (Fusion Engine → Conviction Engine; B-001 FECHADA). A SPEC-002 prepara evidência com proveniência completa; **não** funde. Preserva **J-001/N-001** (CONS-01).
- **Armazenamento físico** (Blackboard/KG) → **SPEC-004/006** (M-001/H-001 abertas).
- **Fórmula de qualidade/aging/peso numérico** → **CCM-001/J-001** (SPEC-003).
- **Agentes que PRODUZEM evidência** → SPEC-010/011/012/013.

---

## 7. Proposta de escopo / fronteira / número / Classe / PD-xx

### 7.1 Número, nome, complexidade
- **Manter** número **SPEC-002** e nome **"Evidence & Evidence Provenance Harness"** (slot indicativo confirmado; sem divisão/fusão/renome). Sem re-apontamento de gatilhos do RMR-001 necessário por este ato (nenhum slot alterado). **[PROPOSTA]**
- **Complexidade CRITICAL**, profundidade **D0–D7** (ROADMAP) + **D8 adversarial seletivo** para integridade de proveniência/anti-adulteração — **`[DECISÃO NECESSÁRIA — DN-2]`** confirmar D7 vs D0–D8.
- **NÃO dividir.** O escopo é coeso em torno do envelope operacional de CEM-001. Dividir fragmentaria o contrato de proveniência. **[INFERÊNCIA]**

### 7.2 Escopo (IN)
Camada Harness/operacional sobre CEM-001: protocolo de criação/publicação/supersessão/invalidação/arquivamento operacional de evidência; proveniência da transformação `Fonte→Dado→Evidência` (ferramenta/Skill produtora; fronteira Observação≠Evidência); taxonomia operacional favorável/contra/inconclusiva; metadado de independência/correlação (substrato de RULE-004); metadado de conflito (substrato de RULE-005); metadado de temporalidade/staleness; vínculo operacional evidência→hipótese por referência (CHM-001); suporte à auditabilidade/reconstrução bitemporal (por referência ao KG/SPEC-006/041).

### 7.3 Non-goals (OUT — explícitos)
Redefinir CEM-001 (CONST-01); fusão multi-fonte e fórmula de convicção (SPEC-003/J-001); armazenamento físico (SPEC-004/006); fórmula de aging/peso/confiabilidade numérica (CCM-001/J-001); os agentes produtores (SPEC-010-014); Signal Package/risco (RISK); mecanismos criptográficos/on-chain de tamper-evidence.

### 7.4 Classe/Mecanismo (RULE-MECH-01)
Declaração é **por BASpec no Plan**, nunca por Spec (SES-001 §50). Antecipação `[PROPOSTA]`: predominância esperada **Classe D** (proveniência/versionamento/integridade de linhagem = determinístico) e **Classe H** (publicação com gate determinístico de conformidade de contrato CEM-001 + produtor autorizado). Classe P improvável (SPEC-002 não faz julgamento qualitativo — isso é dos agentes). Classe C possível só em invariante de integridade de alto risco (ex.: bloqueio fail-closed de publicação incompleta). **Confirmação no Plan.**

### 7.5 Princípios de Domínio (RULE-PD-01 / CC-12)
**SPEC-002 NÃO declara `PD-xx`.** RULE-PD-01/CC-12 só incidem sobre Spec que define **escopo de especialidade** (Elliott/SMC/ICT). A SPEC-002 é **infraestrutural/neutra de domínio** (CEM-001 Princípio 1) — coerente com a §3 (nenhuma lente de escola aplicável). Não incide (correto, não é achado). **[INFERÊNCIA]**

---

## 8. Decisões abertas, gate e itens `[DECISÃO NECESSÁRIA]` para Andraus

### 8.1 CONS-01 — nada fechado por este Dossiê
Permanecem **ABERTAS** (não tocadas): J-001, G-001, H-001, C-001, K-001, M-001, N-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001, RISK-LEV-001, ECC-VAL-001, ECC-03-001, RUNTIME-TF-PAIR-EXT-001, ENF-LOC-001, D-RISK-SP-001, RULE-REG-001. Nenhum invariante congelado (§13 atomic-spec / AGENTS §6) violado; CEM-001 intocado (CONST-01).

### 8.2 `[DECISÃO NECESSÁRIA]` a resolver por Andraus (antes/na homologação da abertura)
- **DN-1** — Campo de **confiabilidade histórica do produtor** (eixo Admiralty adaptado): metadado da camada-Harness (SPEC-002) OU extensão Categoria A/B do CEM-001 via GMC-001? Deve NÃO colidir com convicção (INV-04). Não fechar aqui.
- **DN-2** — Confirmar profundidade-alvo: **D0–D7** (ROADMAP) ou **D0–D8** (perfil CRITICAL adversarial) para integridade de proveniência.
- **DN-3** — **"Evidência de ausência"** (absent evidence) está no escopo da SPEC-002 ou é adiada?

### 8.3 Itens de gate para o Controlador/coordenador (não executo — sem Bash; não homologo)
- **RULE-REG-001** — gatilho `spec:SPEC-002 em redação` **dispara com a abertura desta Spec**: registrar o lote de **10+1 famílias RULE** (RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC + RULE-MET) em `governance/RULES.md` e promover `atomic-spec` a **v1.5** (incorporação física das atas EUA-E04..E14, hoje `[Fonte: ...]` sem seção). Ação do Controlador na homologação da abertura.
- **BL-012** (MC-COG-001) — gatilho `spec:SPEC-002 homologada (consolidação cognitiva v1.5)` dispara **na homologação do Plan** (não da abertura). Registrar como IMINENTE.
- **Validação pendente (sem Bash):** `python scripts/validate_spec_sot.py` (STRUCT-11 Dossiê presente), `check_refs.py`, `build_map.py --check`, `backlog_triggers.py` — a rodar pelo coordenador; mapa `docs/mapa/` a regenerar (novos arquivos em `specs/features/SPEC-002/`).

---

## 9. Autopré-check (§7 especificador.md) — aplicado a este Dossiê de abertura

- [x] ROADMAP + atomic-spec + WORKFLOW.md + RULES.md + CEM-001 + CATALOGO + RMR-001 lidos (núcleo sempre-obrigatório; WORKFLOW.md com ênfase reforçada, EUA-E24 Q1).
- [x] RMR-001 itens `ATIVADO`: **nenhum** pendente (painel §6: "Itens em ATIVADO: nenhum"). BL-024 (gatilho `evento:abertura da SPEC-002`) já **Absorvido** (SPEC-046). Gate limpo.
- [x] RULE-ECC-01/02: Dossiê presente e completo; escopo/número/fronteira propostos; sem re-apontamento de gatilho (slot inalterado).
- [x] RULE-ECC-04: 5 fontes carregadas com `sources/SRC-0N.txt` + citação verbatim entre aspas (§2.1). E6 não-carregada (INDETERMINADO declarado, RULE-MET-01).
- [x] RULE-ECC-05: quadro das 6 lentes — todas não-aplicáveis com justificativa (ausência justificada = correto). Nenhuma "aplicável não pesquisada".
- [x] RULE-ECC-06: gatilho estrito não disparado (SPEC-002 não é agente/K-001/018/045-runtime); WORKFLOW.md lido (reforçado) + mapeamento E1–E8 leve; nada fechado.
- [x] RULE-ECC-07: gatilho não disparado (não é agente/transição); declarado explicitamente; Enforcement Contracts ordinários (ENF-01) antecipados para o Plan.
- [x] RULE-MECH-01 (Classe) e RULE-PD-01 (PD-xx): incidência determinada — Classe por BASpec no Plan; **PD-xx não incide** (infraestrutural).
- [x] CONST-01/CEM-001: construir sobre, não redefinir — respeitado; gap operacional identificado.
- [x] CONS-01: nenhuma decisão aberta fechada; DN-1/2/3 marcados `[DECISÃO NECESSÁRIA]`.
- [x] Invariantes (INV-01..10, INV-RISK-*): não violados; INV-04/06/07/10 explicitamente preservados.
- [x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada; salvaguardas DHR-PROV-WEB-001 §2.1 mantidas.
- [x] §7-bis (redução de viés): N/A a Dossiê de abertura (aplica-se ao Plan HIGH/CRITICAL com BASpecs); reconfirmado no Plan.
- [ ] **NÃO** escrito o Plan (correto — abertura precede o Plan; ROADMAP §23 passo 1-bis).

**Pronto para revisão.** (Este Dossiê de abertura → parecer do Revisor → homologação de Andraus da definição, ANTES do Plan.)

---

## 10. Fontes `[EXTERNO]` (links)

- W3C PROV / CASRAI — Data Provenance: https://casrai.org/guides/data-provenance
- Admiralty code (NATO AJP-2.1): https://en.wikipedia.org/wiki/Admiralty_code
- NeoXam DataHub — Audit Trail and Traceability in Financial Data: https://www.neoxam.com/datahub/ensure-audit-lineage-data-quality/
- QuestDB — Data Lineage in Financial Systems: https://questdb.com/glossary/data-lineage-in-financial-systems/
- From Agent Traces to Trust (arXiv 2606.04990): https://arxiv.org/html/2606.04990v1
- Evidence Correlation ER rule (PMC12116114): https://pmc.ncbi.nlm.nih.gov/articles/PMC12116114/
- FNBT / Dempster-Shafer (arXiv 2508.08075): https://arxiv.org/abs/2508.08075
- Improved D-S / tunnel collapse risk (Nature): https://www.nature.com/articles/s41598-022-07171-x
- NovaFabric (arXiv 2609.12582): https://arxiv.org/pdf/2609.12582
- Tracing the Data Trail in LLMs (arXiv 2601.14311): https://arxiv.org/pdf/2601.14311

*Dossiê de Pesquisa da SPEC-002 — PROPOSTA. Método: atomic-spec.md §15 (RULE-ECC-01..07). Autor: Especificador Principal. Não é baseline; não fecha decisão aberta; não redefine canônico.*
