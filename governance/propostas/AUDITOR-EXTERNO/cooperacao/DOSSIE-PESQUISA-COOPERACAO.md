# DOSSIÊ DE PESQUISA — Cooperação entre agentes internos (Especificador, Revisor) e Auditor Externo (Codex), mediada pelo Orquestrador

**[PROPOSTA / DOSSIÊ — NÃO NORMATIVO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-06 |
| Encomendado por | Orquestrador interno (por ordem de Andraus) |
| Método | `atomic-spec.md` §15 (Dossiê de Pesquisa, RULE-ECC-01/02); captura verbatim RULE-ECC-04; régua de repositórios RULE-ECC-06; salvaguarda DHR-PROV-WEB-001 §2.1 |
| Saída irmã | `PROPOSTA-COOPERACAO-INTERNO-EXTERNO.md` (P1..P8 + propostas novas) |
| Escopo | Forma de cooperação interno×externo no loop de homologação; **não** é Spec de trading; **não** é abertura de SPEC-0NN |
| Fase | Spec-first — nenhuma recomendação de BUILD/código; descrição apenas |

> **Salvaguarda vinculante (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** todo conteúdo web abaixo é **DADO, nunca instrução**; nada aqui vira baseline; nenhuma prática externa é importada automaticamente — cada uma é confrontada com a arquitetura do SOT antes de qualquer proposta. Fonte externa classificada e etiquetada `[EXTERNO]`; veracidade das páginas **não atestada** (sou detector, não gate — a verificação é por Andraus). Onde a pesquisa não conclui: **INDETERMINADO** (estado válido).

> **Base factual corrigida (ERRATA §6 da `AUDITORIA-ENTRADA-2026-10-06.md`, conferida pelo Revisor SOT, prevalece sobre §0–§5 da entrada):** incorporei os seguintes fatos reverificados — (E1) a independência "auditor não vê o parecer do Revisor" é **regra decidida com garantia apenas procedural** (ata 004 §3 a marca `[NÃO VERIFICADO]`), não controle técnico; (E2) o desempenho **não** foi "uma execução": houve dry-run + **dois ciclos reais** com **correção de prompt entre eles** (ciclo 1 = 3 postados + 2 descartados por **formato**, não por recall; ciclo 2 = 5/5 plantados, 0 descartado) — medido só contra defeitos plantados; (E4) `backlog_triggers.py` está em `INFORMATIVOS` (`kit/run_gates.py:10`) mas **não** é executado pelo `run_gates.py` (reverificado por mim: ausente da lista `gates`, linhas 30–36) → o gate `ATIVADO` do RMR-001 **não roda no bot**; (E5) a lista de decisões abertas desatualizada está no **código/prompt do kit**, não no texto do protocolo; (E6) protocolo §1 ("precede ou acompanha o Revisor") está **superado pela ata 004** e só é mitigado por DIR-003; (E7) o auditor **não tem protocolo estruturado** equivalente aos passos eliminatórios do Revisor nem carimbo de sincronização comparável por máquina.

---

## 1. Questões de pesquisa e estratégia de busca

Sete questões (Q1..Q7) ditadas pelo Orquestrador. Estratégia: WebSearch para mapear o estado da arte; WebFetch das fontes mais estáveis/autoritativas para captura **verbatim** (RULE-ECC-04, `sources/`); classificação por nível de evidência. Termos de busca e data de acesso registrados em cada captura `sources/<ID>.txt`. Data de acesso de todas as fontes: **2026-10-06**.

| Q | Tema | Fontes principais |
|---|---|---|
| Q1 | Revisão cruzada entre modelos heterogêneos; debate; LLM-as-judge; ancoragem/viés de concordância; ordem sequencial vs paralela | SRC-JUDGE-01, SRC-CSMAD-01 |
| Q2 | Andaime determinístico em volta de agentes probabilísticos; verificador no loop; derivar veredito dos achados | SRC-HITL-01, SRC-CSMAD-01, REPO-guardrails-01 |
| Q3 | Consenso + escalonamento humano com rodadas limitadas; critério de parada; dissenso registrado; risco de ciclo sem fim / "consenso por cansaço" | SRC-HITL-01 |
| Q4 | Procedência e reprodutibilidade de revisores LLM; pinagem de modelo/versão; limites de temperatura/seed | SRC-REPRO-01 |
| Q5 | Injeção de prompt indireta em agentes que auditam código/documentos; isolamento de segredos | SRC-OWASP-01, SRC-HITL-01 |
| Q6 | Avaliação/calibração de revisores LLM; defeitos plantados; precisão/recall; concordância; tamanho de amostra | SRC-JUDGE-01, SRC-REPRO-01 |
| Q7 | Simetria de regras interno×externo; sincronização das regras entregues ao externo | SRC-OWASP-01, SRC-HITL-01 (síntese; ver §4 conflito/lacuna) |

**Pesquisa Multi-Lente (RULE-ECC-05):** **não incide.** Esta é matéria de **meta-harness/governança** (como as Specs SPEC-019/020/021/002): não define nem toca comportamento de agente analítico, do Conviction/Fusion Engine, do Manager ou do Risk Agent. Nenhuma lente de escola de análise (Elliott/SMC/ICT) nem de `WORKFLOW.md` se aplica. Registrado explicitamente para o Revisor.

---

## 2. Fontes classificadas (todas `[EXTERNO]`, captura verbatim em `sources/`)

| ID | Fonte | Classificação (tipo) | Nível de evidência | Usada em |
|---|---|---|---|---|
| SRC-OWASP-01 | OWASP "LLM01:2025 Prompt Injection" | **Padrão** (standards body) | Documentação oficial de referência de segurança | Q5, Q7 |
| SRC-JUDGE-01 | "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" (arXiv 2410.02736) | **Evidência** (estudo empírico) | Preprint acadêmico (arXiv), não revisado por pares | Q1, Q6 |
| SRC-CSMAD-01 | "CSMAD: ... multi-agent debate with NLI-verified contradictory statements" | **Prática/Experimento** (método+avaliação) | Publicação com venue declarado (SIGIR 2026) | Q1, Q2 |
| SRC-REPRO-01 | "Setting the temperature to zero will make an LLM deterministic?" (zansara) | **Opinião** técnica fundamentada | Blog-prática, não revisado | Q4, Q6 |
| SRC-HITL-01 | AWS Well-Architected Agentic AI Lens — AGENTSEC04-BP02 | **Prática** (padrão de arquitetura de fornecedor) | Documentação oficial de fornecedor | Q2, Q3, Q5, §7 |
| SRC-SYCO-01 | "Towards Understanding Sycophancy in Language Models" (arXiv 2310.13548, Sharma et al.) | **Evidência** (estudo empírico) | Preprint acadêmico (arXiv), não revisado por pares | §7 (modelo de viés) |
| REPO-guardrails-01 | `guardrails-ai/guardrails` (GitHub) | **Prática** (software aberto) | Repositório; elegibilidade **NÃO CONFIRMADA** (ver §5) | Q2 |

**Limites e conflitos entre fontes (declarados):**
- Níveis de evidência **heterogêneos**: um padrão OWASP e uma doc de fornecedor pesam mais que um blog (SRC-REPRO-01) ou um preprint não revisado (SRC-JUDGE-01). Nenhuma conclusão carregada repousa só em blog.
- Dados numéricos vistos em *resultados de busca* mas **não** capturados verbatim de página (ex.: "self-preference +73.3 pontos percentuais"; "Fleiss' kappa = 0.357" de concordância entre juízes) **não** sustentam nenhuma proposta — ficam como contexto `[EXTERNO, não-capturado-verbatim]`, não como alegação carregada (disciplina RULE-ECC-04).
- Vários resultados de busca tinham IDs arXiv e datas posteriores ao meu corte de conhecimento; **não** os usei como fonte carregada. Conforme a instrução do Orquestrador, **nenhuma** fonte foi usada para "fixar" reprodutibilidade por ID implausível; SRC-REPRO-01 é blog assumidamente de prática.

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

> Regra: achado externo ≠ fato SOT (TRACE-06). Abaixo, cada prática é confrontada com invariantes e regras já vigentes.

### Q1 — Revisão cruzada, heterogeneidade, ordem sequencial-cega
- `[EXTERNO, SRC-JUDGE-01]` «Most models rated their outputs more favorably, even when answer sources were anonymized. All judge models are significantly impacted by position bias.»
- **`[INFERÊNCIA]` ADOTAR (confirma desenho vigente):** usar um modelo externo **de fornecedor diferente** (Codex) como auditor do que agentes Claude produziram reduz o viés de auto-preferência medido por SRC-JUDGE-01 (o auditor não avalia a própria saída). E rodar o auditor **sem ver o parecer do Revisor** (DHR-AUDITOR-EXTERNO-004 §1.4) remove a ancoragem/efeito de concordância — o estudo mostra que o juízo é sensível à ordem/contexto. A pesquisa **endossa** a escolha sequencial-cega de Andraus; não propõe mudá-la. **Ressalva (ERRATA E1):** essa independência hoje tem **garantia apenas procedural** — depende de o Orquestrador não commitar o parecer do Revisor no commit auditado (ata 004 §3, `[NÃO VERIFICADO]`); como o viés de concordância é justamente o risco que o desenho combate, a falta de controle técnico é um **risco explícito** → ver PN9 na `PROPOSTA`.
- `[EXTERNO, SRC-CSMAD-01]` «...independent agents to evaluate the claim and the contradictory claim, which encourages different lines of reasoning without assigning preset stances.» → **ADAPTAR** apenas como princípio: manter a independência dos dois pareceres (Revisor × Auditor) e compará-los **depois** (já é o papel do Orquestrador). **REJEITAR** importar "debate multi-agente" como mecanismo: o SOT não quer agentes convergindo por diálogo (risco de colapso de independência); quer dois pareceres independentes + decisão humana.

### Q2 — Andaime determinístico em volta do probabilístico
- `[EXTERNO, SRC-HITL-01]` «Risk classification itself can't rely on an LLM exposed to the same untrusted content... Use deterministic logic (policy engines, rule-based classifiers) as the authoritative signal, with LLM-assisted classification as an optional input that a deterministic layer re-checks.»
- `[EXTERNO, SRC-CSMAD-01]` verificador NLI determinístico que confere se o texto gerado realmente contradiz.
- **ADOTAR (reforça ENF-03):** o **veredito/achado do LLM é insumo; o sinal autoritativo é determinístico**. Isto é exatamente o ENF-03 do SOT ("o LLM nunca é seu próprio gate") e fundamenta as lacunas L1 (veredito não derivado dos achados) e L2 (regra citada não conferida) da auditoria de entrada → ver propostas P4, PN1, PN2 na `PROPOSTA`.
- **ADOTAR** a ideia de "verificador no loop" como *camada determinística que re-checa*: o SOT já tem `validate_finding.py` (citação literal no commit) e os gates `scripts/`. A lacuna é que o **veredito** não passa por essa camada.
- REPO-guardrails-01 (validação de saída por schema/validators): **ADIAR/REFERÊNCIA** — confirma que "validação programática de saída" é prática empacotada; não adotada como dependência (régua não confirmada; o SOT já tem seu próprio validador).

### Q3 — Consenso, rodadas limitadas, escalonamento
- `[EXTERNO, SRC-HITL-01]` anti-padrão: «...approval workflows without timeout policies or escalation paths, so agent execution stalls indefinitely...»
- **ADOTAR (confirma desenho vigente):** `MAX_ROUNDS = 3` (1 auditoria + 2 re-auditorias) + "depois vai a Andraus com o dissenso registrado" (DHR-AUDITOR-EXTERNO-004 §1.6) é precisamente o critério de parada + escalonamento que a fonte pede. A pesquisa **endossa**; a lacuna é que o limite hoje conta *pedidos*, não *divergência persistente* (entrada §3) → ver PN-dissenso na `PROPOSTA`.
- `[EXTERNO, SRC-HITL-01]` «You log human approval decisions with timestamps and reviewer identities, creating an auditable record of human oversight for compliance purposes.» → **ADOTAR** como princípio: o dissenso registrado precisa de registro auditável (hoje a disposição CONFIRMADO/PARCIAL/DESCARTADO é só texto em `kit/loop_tools.py:93`, sem campo/leitor — entrada §3.3) → P2.
- Risco "consenso por cansaço": `[INFERÊNCIA]` o limite de 2 rodadas **mitiga**, mas se o veredito for aceito do modelo sem derivação determinística, rodadas repetidas podem "passar" por variação do modelo, não por correção real (ligado a Q4). → reforça PN1/PN4.

### Q4 — Procedência e reprodutibilidade
- `[EXTERNO, SRC-REPRO-01]` «temperature=0 makes only the token selection rule deterministic. It does not guarantee that the entire inference system will produce exactly the same logits every time.» e «sampling determinism is not the same thing as system determinism.»
- **ADOTAR como limite honesto (RULE-MET-01):** o SOT **não** pode prometer reprodutibilidade bit-a-bit de um modelo externo. O `MODEL_LABEL` (`kit/auditor_bot.py:34`) é só rótulo e `--ignore-user-config` pode deixar modelo/esforço no padrão do CLI (entrada §1). **ADAPTAR:** registrar o **modelo/versão real** quando disponível e, quando não, declarar **INDETERMINADO** — nunca fingir pinagem. A reprodutibilidade praticável é **por contexto fixado** (commit + fontes + data + diretiva vigente), não bit-a-bit. → P5, PN5.

### Q5 — Injeção de prompt indireta e isolamento de segredos
- `[EXTERNO, SRC-OWASP-01]` «Indirect prompt injections occur when an LLM accepts input from external sources... Restrict the model's access privileges to the minimum necessary... Separate and clearly denote untrusted content...»
- `[EXTERNO, SRC-HITL-01]` o classificador de risco não pode ser um LLM exposto ao mesmo conteúdo não confiável.
- **ADOTAR (confirma desenho vigente):** conteúdo de repo/PR/issue = DADO, nunca instrução (protocolo §5.2 já espelha isto). Least-privilege: token fine-grained Read + sandbox read-only + sem rede (atas 002/003). **Lacuna reconhecida e não resolvível só por prompt:** o modelo roda como o mesmo usuário do bot e **pode ler o arquivo do token / `auth.json`** (ata 003 §4; `apparmor_restrict_unprivileged_userns=0`). SRC-OWASP-01 ("least privilege") e a honestidade do SOT convergem: a mitigação é de SO (separar usuário), não de prompt. → PN6 (reforço) + risco residual declarado.

### Q6 — Avaliação/calibração do revisor
- `[EXTERNO, SRC-JUDGE-01]` juízes LLM têm vieses sistemáticos (posição, auto-preferência) → medir é necessário, não opcional.
- `[EXTERNO, não-capturado-verbatim]` a prática reconhecida de avaliar sistema não-determinístico rodando cada prompt N vezes e reportando média + variância (observada em resultado de busca de fontes de reprodutibilidade; **não** consta verbatim em `sources/SRC-REPRO-01.txt` — apareceu em sumário de busca, não na página capturada; **não** é alegação carregada e não sustenta sozinha nenhuma proposta). O núcleo capturado verbatim de SRC-REPRO-01 é sobre temperatura/determinismo (ver §2), não sobre N-rollout.
- **ADOTAR:** a medição disponível (ERRATA E2: dry-run + **dois ciclos reais**, com **correção de prompt entre eles**; ciclo 2 = 5/5 plantados, 0 descartado — tudo contra defeitos plantados) ainda é **insuficiente** como garantia de confiabilidade — um sistema não-determinístico precisa de N execuções + amostra maior + medir precisão **e** recall + falso-positivo no item limpo, e o fato de um ciclo ter exigido ajuste de prompt mostra sensibilidade do resultado ao prompt. **ADAPTAR** para o SOT: ampliar o conjunto de calibração (o protocolo §8 já lista C-1..C-7) e repetir N vezes. → PN4.

### Q7 — Simetria e sincronização de regras interno×externo
- **`[INFERÊNCIA]` + `[EXTERNO, SRC-OWASP-01]` (instruction/data separation) + SRC-HITL-01 (fonte determinística autoritativa):** o kit entrega ao externo um subconjunto de regras (`kit/PROMPT-AUDITOR-CI.md`, lista `CLOSED_CLAIM` em `kit/validate_finding.py`) **fora** do mecanismo RPSA que mantém o Revisor sincronizado. Isso é assimetria de sincronização (entrada §1). O estado da arte não dá uma "regra" pronta para isso; a prática reconhecida é **gerar a lista a partir da fonte de verdade** e **conferir por detector** — mesmo princípio dos scripts `check_doc_sync.py`/`check_rpsa.py` já vigentes. → P6, P7, PN7. **Não há fonte externa dedicada a este ponto específico; a proposta é por analogia interna, declarada `[INFERÊNCIA]`.**

---

## 4. Lacunas e conflitos (a pesquisa NÃO fecha decisão aberta — CONS-01)

- **Lacuna de fonte dedicada a Q7:** não localizei fonte `[EXTERNO]` específica sobre "sincronizar o conjunto de regras entregue a um revisor externo vs interno". Conclusões de Q7 são `[INFERÊNCIA]` por analogia aos mecanismos internos (RPSA, detectores) — declarado, não mascarado. **INDETERMINADO** quanto a um padrão externo nomeado.
- **Conflito de régua (RULE-ECC-06):** o único repositório examinado (`guardrails-ai/guardrails`) teve 2 de 6 critérios **não verificáveis** sem acesso vivo (último commit; alertas graves). Por fail-closed, tratado como **não elegível** → não adotado. Ver §5.
- **Nenhuma decisão aberta é tocada:** J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001 permanecem **ABERTAS**. Nada neste Dossiê as fecha nem as usa como invariante.
- **Limite de detector (igual ao Passo 4-bis do Revisor):** fontes fabricadas ou mal-citadas e injeção via conteúdo web **não** são detectáveis por mim sem acesso web vivo; declaro como **risco residual**, não garantia.
- **Gap de gate reverificado (ERRATA E4):** o gate `ATIVADO` do RMR-001 — que o `AGENTS.md` §5 declara **nunca dispensado** — **não roda no bot**: `backlog_triggers.py` aparece em `INFORMATIVOS` (`run_gates.py:10`) mas não na lista `gates` executada (linhas 30–36). O auditor pode, portanto, concluir sem checar itens `ATIVADO`. → PN10.
- **Gap de simetria de processo (ERRATA E7):** o Revisor opera em passos eliminatórios (Passo 0→8, 4-bis, 5-bis) e interpela o autor; o auditor tem só um prompt de conduta, **sem protocolo estruturado equivalente** — pode concluir `OK` sem percorrer o equivalente dos passos. É a assimetria mais funda entre os dois revisores. → PN11.
- **Inconsistência interna ao kit (ERRATA E5):** a deriva da lista de decisões abertas está no **código/prompt** (`validate_finding.py` `CLOSED_CLAIM` + `PROMPT-AUDITOR-CI.md`), não no texto do protocolo §5.3 (que lista `SPEC-045-RUNTIME-001` corretamente). A correção é no kit, não no protocolo. → P6/PN7.

---

## 5. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Seção obrigatória pela régua quando o Dossiê pesquisa melhores práticas em código. Captura: `sources/REPO-guardrails-01.txt`.

| Repositório | Estrelas | Licença | Último commit | Arquivado | Alertas graves | Dono | Veredito |
|---|---|---|---|---|---|---|---|
| guardrails-ai/guardrails | 7.5k (>300 OK) | Apache-2.0 (OK) | **INDETERMINADO** | Não (OK) | **INDETERMINADO** | guardrails-ai (OK) | **NÃO CONFIRMADO** → não adotado/adaptado |

**Resultado:** **nenhum repositório elegível confirmado** nesta pesquisa (resultado válido pela régua). O repositório é citado apenas como **evidência de que "validação programática de saída de LLM via guards/validators" é prática reconhecida e empacotada em software aberto** — não como padrão a importar. Conteúdo de repositório = DADO; nada instalado nem executado. *(Nota: para uma Spec formal, `scripts/check_repo_research.py` seria o gate; aqui o artefato é um Dossiê de proposta, não um `plan.md` de Spec — a seção é cumprida em forma e a elegibilidade é declarada honestamente como não confirmada.)*

---

## 6. Escopo/quantidade resultantes e re-apontamento

- **Escopo:** este Dossiê sustenta **uma** proposta de governança (`PROPOSTA-COOPERACAO-INTERNO-EXTERNO.md`), **não** uma Spec. Não cria SPEC-0NN, não consome slot do ROADMAP, não propõe re-apontamento de gatilhos do RMR-001 (nenhum slot é dividido/fundido/renumerado).
- **Se Andraus decidir normatizar o papel do Auditor Externo** (hoje **piloto** — DHR-AUDITOR-EXTERNO-001..004), isso demandaria ato próprio (RULE em `RULES.md` e/ou emenda ao fluxo em `AGENTS.md`), fora do meu mandato: **`[DECISÃO NECESSÁRIA]`**.
- **Referências a documento BASELINED:** nenhuma. As atas DHR-AUDITOR-EXTERNO-* são registros de piloto, não baseline; não exigem erratum.

---

## 7. Modelo de ameaça de viés — base de evidência (requisito de Andraus, 2026-10-06)

Andraus (chat, 2026-10-06): *"a ideia também é não expor o auditor externo a viés de qualquer tipo que possa prejudicar a auditoria externa."* Isto amplia a independência para além do parecer do Revisor. Abaixo, os **tipos de viés** com evidência `[EXTERNO]` capturada verbatim; os **canais de exposição** reverificados no kit e as **mitigações** ficam na `PROPOSTA` §2-bis.

| Viés | Evidência `[EXTERNO]` (verbatim em `sources/`) |
|---|---|
| Posição/ordem | SRC-JUDGE-01: «All judge models are significantly impacted by position bias. This bias becomes more pronounced as the number of answers increases.» |
| Autopreferência | SRC-JUDGE-01: «Most models rated their outputs more favorably, even when answer sources were anonymized.» |
| Bandwagon (maioria/consenso) | SRC-JUDGE-01: «The tendency to give stronger preference to the majority's beliefs regardless of whether they are correct or not.» |
| Autoridade | SRC-JUDGE-01: «The tendency to assign more credibility to statements made by authority figures, regardless of actual evidence.» + «when we added automatically generated fake references to Assistant B's answer, the judge model considered Assistant B's quality to be superior.» |
| Verbosidade | SRC-JUDGE-01: «LLM judges favor longer responses, even if they are not as clear, high-quality, or accurate as shorter alternatives.» |
| Sicofância (concordar com a crença dada) | SRC-SYCO-01: «Human feedback may also encourage model responses that match user beliefs over truthful ones, a behaviour known as sycophancy.» |
| Ancoragem/confirmação | `[INFERÊNCIA]` derivada de posição+bandwagon+sicofância aplicadas a re-auditoria com pistas dos achados anteriores; sem fonte dedicada capturada → declarada `[INFERÊNCIA]`, não alegação carregada isolada. |

**Princípio de mitigação com fonte:** SRC-HITL-01 «Risk classification itself can't rely on an LLM exposed to the same untrusted content... Use deterministic logic... as the authoritative signal...» e SRC-OWASP-01 «Separate and clearly denote untrusted content to limit its influence...» fundamentam **barreira de informação** + **sinal autoritativo determinístico** como contramedidas. Detalhe operacional e canais na `PROPOSTA` §2-bis.

---

## 8. Etiquetagem / status epistemológico

- Todas as fontes web: `[EXTERNO]`, veracidade não atestada (TRACE-06), captura em `sources/`.
- Fatos do repositório SOT (atas, kit, invariantes): `[FONTE]`/`[FATO]` quando homologados.
- Derivações minhas: `[INFERÊNCIA]`. Propostas: `[PROPOSTA]`. Dependências de Andraus: `[DECISÃO NECESSÁRIA]`.
- Estado `INDETERMINADO` usado onde a pesquisa não conclui (Q7 fonte dedicada; régua do repositório; reprodutibilidade de modelo externo; fonte dedicada a ancoragem/confirmação em re-auditoria).
- **Correções pós-revisão (NÃO CONFORME do Revisor, 2026-10-06):** C-01 resolvido por **caminho (a)** — a frase de registro auditável existe verbatim na página AWS e foi ampliada em `sources/SRC-HITL-01.txt`, citação corrigida para o literal sem elipse. C-02 resolvido por **caminho (b)** — a frase "N-rollout" **não** está na página de SRC-REPRO-01 (veio de sumário de busca); reescrita como paráfrase `[EXTERNO, não-capturado-verbatim]`, sem « », e não sustenta sozinha nenhuma proposta.
- **CONS-01:** nenhuma decisão aberta aparece como fechada.
