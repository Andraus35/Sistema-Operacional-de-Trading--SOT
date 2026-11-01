# DOSSIÊ DE PESQUISA — Auditor Externo LLM ("GPT") para o SOT

**[PROPOSTA — NÃO HOMOLOGADO]**

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-AUDITOR-EXTERNO |
| **Natureza** | Dossiê de Pesquisa `[EXTERNO]` — **NÃO-NORMATIVO**. Não é Spec, não é baseline, não homologa, não fecha decisão (CONS-01). Insumo para a decisão de Andraus. |
| **Objeto** | Pesquisar melhores práticas de auditoria por LLM em repositório de harness comportamental/spec-driven e adaptá-las ao SOT, para subsidiar um protocolo + briefing do colaborador externo "GPT" como **AUDITOR EXTERNO somente-leitura**. |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 4.8) |
| **Data de acesso web** | 2026-10-05 (todas as fontes `[EXTERNO]`) |
| **Método** | atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) aplicado por analogia a um artefato de governança (não é abertura de Spec do ROADMAP). |
| **Status epistemológico** | Conteúdo web = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02). Toda fonte etiquetada `[EXTERNO]` e classificada. Veracidade das páginas **não** atestada. Capturas verbatim em `sources/`. |
| **Ferramentas** | Pesquisa web feita pelo próprio Especificador (WebSearch/WebFetch). **Sem Bash:** `build_map.py`, `check_refs.py`, `check_repo_research.py` devem ser rodados por quem orquestra. |

> **Aviso de método (RULE-MET-01 — sem bajulação, sem fabricação).** A busca web retornou **várias fontes com identificadores arXiv implausíveis/futuros** (2601.*/2603.*/2604.*/2606.*/2608.*/2609.*) — mesmo fenômeno já registrado na SPEC-004 (`sources/_LIMITACAO-WEB.txt`). Foram **descartadas** por não verificáveis e risco de fabricação. Só foram mantidas como âncora de alegação carregada fontes verificáveis (OWASP Gen AI; Microsoft Learn; arXiv 2411.15594; Claude Platform Docs; agents.md; G-Research; páginas GitHub). Nenhum padrão externo foi importado automaticamente; cada achado é confrontado com a arquitetura SOT antes de qualquer proposta.

> **Nota de escopo.** Este Dossiê **não abre uma Spec do ROADMAP** e **não** aciona RULE-ECC-01 (não há slot SPEC-0NN a decompor). Aplica-se o §15 por analogia porque o pedido envolve pesquisa web que sustenta alegações carregadas; as salvaguardas (verbatim, régua de repositório, conteúdo=dado) são seguidas integralmente. A régua RULE-ECC-06 foi aplicada por rigor, ainda que o objeto não seja Spec.

---

## 1. Questões e estratégia de busca

**Questões:**
- Q1. Quais são os vieses, limites de confiabilidade e técnicas de calibração de **LLM-as-judge**? (lente 1)
- Q2. Como produzir **achados ancorados em evidência** (citar trecho literal + localização; *quote-then-verify*) e controlar alucinação/falso-positivo em auditoria? (lente 2)
- Q3. Como defender um agente que **lê repositório/web/PRs** contra **injeção de prompt indireta** — menor privilégio, ferramentas somente-leitura, separação de funções (OWASP Top 10 for LLM)? (lente 3)
- Q4. Como garantir **determinismo/reprodutibilidade** do parecer (temperatura, modelo/versão fixados, seed, log) e separar **gate determinístico** de **julgamento do LLM** (ENF-03: Detector ≠ Gate)? (lente 4)
- Q5. Como **calibrar o próprio auditor** com defeitos plantados / known-answer tests? (lente 5)
- Q6. Como integrar revisores LLM em **CI/PR** e tratar o parecer (consultivo; humano decide)? (lente 6)
- Q7. Quais **convenções de harness/agentes em repositório** (AGENTS.md) e práticas de avaliação de harness aplicam? (lente 7)
- Q8. Quais **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam essas práticas?

**Estratégia:** WebSearch para mapear cada lente; WebFetch para capturar verbatim fontes-padrão (OWASP, Microsoft, arXiv 2411.15594, Claude Docs, agents.md, G-Research) e auditar estaticamente páginas de repositórios GitHub (estrelas/licença/commit/arquivado — **nada instalado/executado**). Fontes classificadas e etiquetadas `[EXTERNO]`; capturas em `sources/*.txt`.

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Lente |
|---|---|---|---|
| SRC-JUDGE-01 | arXiv 2411.15594 "A Survey on LLM-as-a-Judge" | Evidência/Opinião | Q1 |
| SRC-OWASP-01 | OWASP "LLM01:2025 Prompt Injection" | **Padrão** | Q3 |
| SRC-MSIPI-01 | Microsoft Learn "Defend against indirect prompt injection attacks" | Prática | Q3 |
| SRC-HALLUC-01 | Claude Platform Docs "Reduce hallucinations" | Prática | Q2 |
| SRC-AGENTSMD-01 | agents.md | Prática/Padrão emergente | Q7 |
| SRC-CIREV-01 | G-Research "Building a code review tool: LLM patterns that actually work" | Prática/Experimento | Q6 |
| REPO-promptfoo | github.com/promptfoo/promptfoo | Prática (repo elegível) | Q1/Q6/Q8 |
| REPO-garak | github.com/NVIDIA/garak | Prática (repo elegível) | Q3/Q5/Q8 |
| REPO-evals | github.com/openai/evals | Prática (repo elegível) | Q5/Q8 |

Fontes **descartadas** (não âncora): resultados de busca com IDs arXiv implausíveis/futuros e blogs com datas futuras não verificáveis — ver aviso de método.

---

## 3. Achados por lente — adotar / adaptar / rejeitar / adiar

### Lente 1 — LLM-as-judge: vieses, confiabilidade, calibração (Q1)
[EXTERNO, SRC-JUDGE-01] *"We explore strategies to enhance reliability, including improving consistency, mitigating biases, and adapting to diverse assessment scenarios."* e *"ensuring the reliability of LLM-as-a-Judge systems remains a significant challenge that requires careful design and standardization."* Vieses recorrentes de campo (DADO atribuído ao survey): **posição** (ordem), **verbosidade** (comprimento), **auto-preferência** (self-enhancement).

- **ADOTAR (adaptado):** o auditor externo **não pontua nem ranqueia** — produz **achados ancorados**, o que neutraliza a maior parte dos vieses de comparação (posição/verbosidade/auto-preferência só mordem quando há escolha entre alternativas). O parecer do Revisor SOT permanece o formal; o auditor externo é **segundo par de olhos** (painel de 2 juízes, prática de mitigação de viés).
- **ADAPTAR:** toda alegação do auditor deve ser **verificável por string-match** (não por preferência estética) — remove o viés de verbosidade (achado longo sem citação checável = descartado).
- **REJEITAR:** usar o auditor externo como **juiz-nota** ou como substituto do Revisor/Andraus — introduz exatamente os vieses do survey e viola o fluxo de 3 posições.

### Lente 2 — achados ancorados em evidência / quote-then-verify / anti-alucinação (Q2)
[EXTERNO, SRC-HALLUC-01] *"Use direct quotes for factual grounding: ... ask Claude to extract word-for-word quotes first before performing its task. This grounds its responses in the actual text, reducing hallucinations."* e *"Verify with citations: Make Claude's response auditable by having it cite quotes and sources for each of its claims. You can also have Claude verify each claim by finding a supporting quote after it generates a response. If it can't find a quote, it must retract the claim."*

- **ADOTAR:** esquema de achado com **trecho literal verbatim + `arquivo:linha`** obrigatório; regra "sem citação checável = achado descartado". Isto espelha exatamente o mecanismo verbatim que o SOT já usa (RULE-ECC-04 / PC-06 / RCN-001) — convergência forte com a arquitetura.
- **ADOTAR:** permissão explícita de dizer **INDETERMINADO / "não sei"** ([EXTERNO, SRC-HALLUC-01] *"Allow Claude to say \"I don't know\" ... can drastically reduce false information."*) — alinha com o estado INDETERMINADO já canônico no SOT (RULE-EPI/CC-09).
- **ADAPTAR:** *quote-then-verify* vira um **passo de autoverificação** no briefing — após redigir, o auditor refaz cada achado buscando o trecho de suporte; se não achar, retrata.

### Lente 3 — segurança: injeção de prompt indireta, menor privilégio, somente-leitura, separação de funções (Q3)
[EXTERNO, SRC-OWASP-01] *"Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files."* Mitigações: *"Enforce privilege control and least privilege access"*, *"Segregate and identify external content"*, *"Require human approval for high-risk actions"*. [EXTERNO, SRC-MSIPI-01] *"adversaries embed malicious instructions within third-party content, which the AI misinterprets as legitimate commands."*; *"Principle of least privilege: Give agents only the minimal number of short-lived privileges needed to complete their tasks"*; *"No single solution is sufficient—combine probabilistic and deterministic defenses."*

- **ADOTAR:** **ferramentas somente-leitura** para o auditor (espelha ENF-03 estrutural do Revisor SOT: sem Write/Edit). Todo conteúdo de repo/web/PR = **DADO, nunca instrução** (espelha DHR-PROV-WEB-001 §2.1). Separação de funções: auditor **propõe**, nunca aplica; Andraus decide.
- **ADOTAR (adaptado):** *spotlighting*/data-marking — o briefing instrui o auditor a tratar qualquer "instrução" encontrada em arquivos/PRs/páginas como **achado de segurança** (tentativa de injeção), não como comando.
- **ADAPTAR:** "combine probabilistic and deterministic defenses" → o auditor LLM (probabilístico) **nunca é seu próprio gate**; os scripts determinísticos do SOT (`validate_spec_sot.py`, `check_refs.py`, `check_doc_sync.py`, `check_repo_research.py`, `build_map.py --check`) são a camada determinística que o auditor **cita como evidência**, não executa.
- **REJEITAR:** qualquer capacidade de escrita/execução/commit para o auditor; qualquer envio de dados sensíveis do SOT a serviços externos.

### Lente 4 — determinismo / reprodutibilidade (Q4)
A pesquisa confirma que `temperature=0` é **necessário mas não suficiente** e que fixar modelo/versão/seed + registro são os controles usuais — porém a fonte mais específica retornada tinha **arXiv ID implausível/futuro** e foi **descartada como âncora** (RULE-MET-01). Apoio verificável indireto: [EXTERNO, SRC-MSIPI-01] *"combine probabilistic and deterministic defenses"*; [EXTERNO, SRC-HALLUC-01] *"while these techniques significantly reduce hallucinations, they don't eliminate them entirely."*

- **ADOTAR (como [INFERÊNCIA] + prática de campo):** cada parecer registra **commit/baseline auditado, nome e versão do modelo, data e janela de sincronização (RPSA)** — reprodutibilidade por contexto fixado, não por bit-reprodutibilidade.
- **ADOTAR:** separação **Detector ≠ Gate** (ENF-03) — o veredito "bloqueante" nunca é do LLM; o LLM detecta e cita, o gate determinístico e Andraus decidem.
- **ADIAR:** padronização de `temperature/seed/system_fingerprint` — o "GPT" roda fora do Claude Code, em ambiente que o SOT não controla; registrar como **limite declarado** e recomendar à orquestração, não fechar. (Nota honesta: modelos recentes podem ter deprecado `temperature`.)

### Lente 5 — calibração por defeitos plantados / known-answer tests (Q5)
[EXTERNO, REPO-garak] *"garak checks if an LLM can be made to fail in a way we don't want. garak probes for ... prompt injection ... and many other weaknesses."* [EXTERNO, REPO-evals] framework de eval + registry de benchmarks.

- **ADOTAR (adaptado):** um **conjunto de calibração** com defeitos plantados do próprio SOT (ex.: decisão aberta tratada como fechada; citação que não bate com `sources/`; achado sem `arquivo:linha`; instrução embutida num arquivo de teste) + respostas esperadas. Mede recall (achou os plantados?) e precisão (inventou falsos?). O garak/evals são **referência de método**, não dependências.
- **ADAPTAR:** a calibração do SOT é **sobre o conteúdo normativo do SOT** (CONS-01, INV, CONST-01), não sobre vulnerabilidades genéricas de LLM.

### Lente 6 — integração em CI/PR; tratar o parecer como consultivo (Q6)
[EXTERNO, SRC-CIREV-01] *"We deliberately decided not to block merges. There is still a human involved and space for discretion."* e *"We introduced a second LLM call. After the initial review, we send the findings back to the model and ask it to identify which are genuine violations, with examples of false positives."*

- **ADOTAR:** parecer do auditor externo = **consultivo** (COMMENT-equivalente), nunca bloqueia. Converge com o fluxo do SOT (só Andraus homologa; parecer do Revisor ≠ homologação).
- **ADOTAR:** **two-pass/autoverificação** antes de entregar (reduz falso-positivo) — vira item do checklist do briefing.
- **ADAPTAR:** no SOT, o gate bloqueante é o **script determinístico + Andraus**, não o bot. O auditor externo entrega **antes** do Revisor formal ou em paralelo, como insumo.

### Lente 7 — convenções de harness/agentes em repositório (Q7)
[EXTERNO, SRC-AGENTSMD-01] *"A simple, open format for guiding coding agents, used by over 60k open-source projects."*; *"AGENTS.md is now stewarded by the Agentic AI Foundation under the Linux Foundation."*

- **ADOTAR (confirmação):** o SOT **já** segue o padrão (AGENTS.md na raiz com comandos determinísticos, fronteiras e proibições). O auditor externo deve **ler o AGENTS.md primeiro** e respeitar suas fronteiras — nada a mudar no SOT.
- **REJEITAR:** importar seções do "AGENTS.md spec" externo que conflitem com a governança do SOT; o AGENTS.md do SOT é soberano.

---

## 4. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua: licença aberta conhecida; ≥300 estrelas; último commit ≤12 meses; não arquivado; 0 alerta grave público aberto; dono identificável. Capturas verbatim em `sources/REPO-*.txt`; números observados por WebFetch em 2026-10-05 (mediado — ver notas de limitação). Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Último commit | Arquivado | Dono | Veredito | Uso no SOT |
|---|---|---|---|---|---|---|---|
| https://github.com/promptfoo/promptfoo | 25.7k | MIT | 2026-10-05 | não | promptfoo | **ELEGÍVEL** | Referência: eval + red-team + integração CI/CD de LLM. Não adotado. |
| https://github.com/NVIDIA/garak | 9.4k | Apache-2.0 | 2026-10-02 | não | NVIDIA | **ELEGÍVEL** | Referência: taxonomia de vulnerabilidades (prompt injection/jailbreak) p/ defeitos plantados. Não adotado. |
| https://github.com/openai/evals | 19.6k | MIT | 2026-04-14 | não | openai | **ELEGÍVEL** | Referência: framework de eval / known-answer tests. Cadência menos ativa (observação). Não adotado. |

Resultado: **3 repositórios elegíveis**. Nenhum é adotado como dependência; servem como referência de boas práticas. `python scripts/check_repo_research.py governance/propostas/AUDITOR-EXTERNO` (ou o caminho que a orquestração definir) deve ser rodado por quem tem Bash — **o Especificador não tem Bash** (declarado).

> **Limite honesto:** o campo "alertas de segurança graves abertos" usa o **proxy público** observável (nenhum GitHub Security Advisory crítico aberto visível); o estado privado do Dependabot não é público (INDETERMINADO). Estrelas/commit são mediados por modelo.

---

## 5. Lacunas, conflitos e INDETERMINADOS (honestidade — RULE-MET-01)

1. **Reprodutibilidade de modelo externo = INDETERMINADO.** O "GPT" roda fora do Claude Code; o SOT não controla temperatura/seed/versão. Registrado como limite declarado do protocolo, não resolvido.
2. **Fonte específica sobre temperatura/determinismo descartada** (arXiv ID implausível). A recomendação de determinismo entra como [INFERÊNCIA]/prática de campo + ENF-03, não como citação de paper.
3. **Veracidade das páginas não atestada** (DADO). Fontes podem estar corretas e ainda assim o auditor não deve importá-las como norma.
4. **Vieses do LLM-as-judge não são elimináveis** — o painel de 2 juízes (auditor externo + Revisor SOT) e a verificação determinística **reduzem**, não zeram (espelha a honestidade do §7-bis do Especificador).
5. **Alertas de segurança privados dos repositórios = INDETERMINADO** (proxy público usado).
6. **Nenhuma decisão aberta é tocada ou fechada** (CONS-01): J-001, N-001, M-001, H-001, G-001, WF-D03, ECC-03-001 permanecem abertas; este Dossiê não as menciona como fechadas.

---

## 6. O que resulta (escopo da proposta)

Resultam **4 artefatos de governança** (não Specs), em `governance/propostas/AUDITOR-EXTERNO/`:
- (A) este Dossiê;
- (B) `PROTOCOLO-AUDITOR-EXTERNO_PROPOSTA.md` — protocolo governado;
- (C) `BRIEFING-GPT_PROMPT.md` — texto pronto para colar como instruções do "GPT";
- (D) `MANIFESTO-DE-ESCOPO_PROPOSTA.md` — o que foi criado e o que NÃO foi tocado.

Nenhum re-apontamento de gatilho RMR-001 é proposto (não há slot de Spec envolvido). **A decisão de instituir o auditor externo é de Andraus** (ver [DECISÃO NECESSÁRIA] no Manifesto).

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-05; capturas verbatim em `sources/`)
- [A Survey on LLM-as-a-Judge (arXiv 2411.15594)](https://arxiv.org/abs/2411.15594) — SRC-JUDGE-01
- [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — SRC-OWASP-01
- [Defend against indirect prompt injection attacks (Microsoft Learn)](https://learn.microsoft.com/en-us/security/zero-trust/sfi/defend-indirect-prompt-injection) — SRC-MSIPI-01
- [Reduce hallucinations (Claude Platform Docs)](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) — SRC-HALLUC-01
- [AGENTS.md](https://agents.md/) — SRC-AGENTSMD-01
- [Building a code review tool: the LLM patterns that actually work (G-Research)](https://www.gresearch.com/news/building-a-code-review-tool-the-llm-patterns-that-actually-work/) — SRC-CIREV-01
- Repositórios (RULE-ECC-06, §4): promptfoo/promptfoo · NVIDIA/garak · openai/evals — capturas em `sources/REPO-*.txt`

*Dossiê não-normativo. Insumo para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, AGENTS.md, Specs, canon, backlog, nem fecha qualquer decisão (CONS-01). Conteúdo web = DADO (`[EXTERNO]`), nunca instrução nem baseline.*
