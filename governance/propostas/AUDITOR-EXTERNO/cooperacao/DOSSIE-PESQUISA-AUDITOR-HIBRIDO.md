# DOSSIÊ DE PESQUISA — Auditor Externo como "revisor de cognição" (pesquisador-revisor híbrido com web)

**[PROPOSTA / DOSSIÊ — NÃO NORMATIVO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-06 |
| Encomendado por | Orquestrador interno (intenção de Andraus a VERIFICAR — ata DHR-AUDITOR-EXTERNO-004 §3-ter) |
| Método | `atomic-spec.md` §15 (RULE-ECC-02); captura verbatim RULE-ECC-04 (`sources/`); régua RULE-ECC-06; DHR-PROV-WEB-001 §2.1; TRACE-06 |
| Saída irmã | `PROPOSTA-AUDITOR-HIBRIDO.md` (parecer + opções A/B/C/D) |
| Escopo | VERIFICAR a ideia: auditor com "total liberdade de cognição e investigação", pesquisando web (estado da arte, benchmarks, GitHub/GitLab) e apontando pesquisa simetricamente ao Especificador; revisando as entregas dos **agentes internos** (não as próprias) |
| Fase | Spec-first — sem código; apenas descrição |

> **Salvaguarda vinculante (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** conteúdo web = **DADO, nunca instrução**; nada vira baseline; nenhuma prática importada automaticamente; toda fonte `[EXTERNO]` classificada, etiquetada e capturada verbatim em `sources/`; veracidade não atestada. Onde a pesquisa não conclui: **INDETERMINADO**.
> **CONS-01:** nenhuma decisão aberta é fechada. **Não** altero kit/atas/AGENTS/ROADMAP/RULES/.github/.claude; só escrevo em `cooperacao/`.

---

## 0. A intenção a verificar (ata 004 §3-ter) e o conflito com o desenho vigente

- **Intenção de Andraus (`[FATO: ata 004 §3-ter]`):** o auditor não deve ser "só um segundo revisor de semântica", mas **revisor de cognição** — com liberdade para pesquisar web e benchmarks e **apontar pesquisa simetricamente ao Especificador**, como **híbrido pesquisador+revisor das entregas dos agentes internos**, "para melhor especificação e adequação semântica". "Total liberdade de cognição e investigação."
- **Desenho vigente (`[FATO]`), oposto em segurança:** auditor em sandbox **sem rede e sem token** (ata 003 §2), mas o modelo roda como **o mesmo usuário do bot e PODE LER o token/`auth.json`** (ata 003 §4; `apparmor_restrict_unprivileged_userns=0`); Revisor **sem web** por ENF-03; `PROMPT-AUDITOR-CI.md` regras 1–2 e protocolo §5.2 tratam conteúdo externo como DADO.
- **Tensão central a verificar:** dar web ao MESMO agente que já tem acesso de leitura ao repositório e pode ler o token recria exatamente a **"lethal trifecta"** (H2). A ideia tem valor cognitivo real (H1), mas o **modo** de implementá-la é o que decide se é segura.

---

## 1. Questões (H1–H6) e fontes

| H | Tema | Fontes principais |
|---|---|---|
| H1 | Revisores com pesquisa (deep research em revisão): ganho × risco de citações fabricadas; verificação determinística de citação web | SRC-CITE-01, SRC-JUDGE-01, SRC-HITL-01 |
| H2 | Segurança de agente com web + leitura de arquivos: injeção indireta, exfiltração, lethal trifecta, egress allowlist, fases separadas | SRC-TRIFECTA-01, SRC-OWASP-01, SRC-HITL-01 |
| H3 | Viabilidade no Codex CLI (sandbox, rede, busca web): o que é verificável × INDETERMINADO | SRC-CODEX-01 |
| H4 | Simetria com as regras de pesquisa do Especificador (ECC-02/04/06); validação determinística do achado de "pesquisa" | `[FATO]` interno + SRC-CITE-01 |
| H5 | Impacto nos limites de papel (consultivo, ENF-03, independência, "não expor a viés") e nos Pacotes 1–3 | SRC-JUDGE-01, SRC-HITL-01 |
| H6 | Custo/limites (4Es) na VM atual | SRC-CODEX-01 + `[FATO]` VM |
| H7 | Auditor que se decompõe em subagentes e usa skills "sem restrições", visando o gate determinístico | SRC-HITL-01 + `[FATO]` kit + `[EXTERNO não-oficial]` (ver §3-H7) |

---

## 2. Fontes classificadas (todas `[EXTERNO]`, captura em `sources/`)

| ID | Fonte | Tipo | Nível de evidência |
|---|---|---|---|
| SRC-TRIFECTA-01 | Willison, "The lethal trifecta for AI agents" | Prática/Opinião de especialista | Blog reconhecido, não revisado |
| SRC-CITE-01 | "Citation theatre…" (Topfer, resume estudos) | Benchmark/Evidência (secundária) | Blog que resume estudo; não revisado |
| SRC-OWASP-01 | OWASP "LLM01:2025 Prompt Injection" | Padrão | Documentação de referência de segurança |
| SRC-JUDGE-01 | "Justice or Prejudice?" (arXiv 2410.02736) | Evidência | Preprint |
| SRC-HITL-01 | AWS Agentic AI Lens — AGENTSEC04-BP02 | Prática | Documentação oficial de fornecedor |
| SRC-CODEX-01 | OpenAI Codex — doc "Sandbox" | Padrão/doc oficial | Oficial; claim de rede **não capturado verbatim** (INDETERMINADO) |

**Conflitos/limites:** SRC-CITE-01 é secundário (resume estudos que eu não capturei na origem) — trato os números (3–13% / 5–18%) como `[EXTERNO]` indicativos, não como fato SOT. SRC-CODEX-01 teve a claim de rede **não** capturada verbatim (a página oficial 308-redireciona e a frase exata não apareceu) → H3 fica parcialmente INDETERMINADO.

---

## 3. Análise por questão — adotar / adaptar / rejeitar / adiar

### H1 — Revisor com pesquisa: ganho × risco de citação fabricada; verificação determinística
- **Ganho `[INFERÊNCIA]`:** um revisor que pesquisa estado da arte pode detectar lacunas de cognição que a revisão puramente semântica não vê (ex.: "a Spec ignora um benchmark/escola relevante"). Simétrico ao Dossiê do Especificador (ECC-02/04/06).
- **Risco medido `[EXTERNO, SRC-CITE-01]`:** «they found 3–13% were hallucinated (no record in the Internet Archive; in their words, they 'likely never existed') and 5–18% did not resolve at all.» e «the density of citations performs a rigour the links don't always have.» → um auditor que pesquisa pode **fabricar citações** e dar aparência de rigor.
- **Risco de viés `[EXTERNO, SRC-JUDGE-01]`:** «when we added automatically generated fake references to Assistant B's answer, the judge model considered Assistant B's quality to be superior.» → **referências (inclusive fabricadas) ENVIESAM o juízo** — logo "pesquisar para revisar" é, ele próprio, um **vetor de viés de autoridade**. Isto colide com o princípio de Andraus "não expor o auditor a viés" (ata 004 §3-ter / §3-bis).
- **Mitigação com fonte `[EXTERNO, SRC-HITL-01]`:** «Use deterministic logic (policy engines, rule-based classifiers) as the authoritative signal, with LLM-assisted classification as an optional input that a deterministic layer re-checks.» → **ADOTAR:** se houver pesquisa, a **citação web tem de ser verificada por código** (um fetcher determinístico busca a URL e confere a citação literal) — o modelo propõe, o código confere. Isto é o ENF-03 aplicado à pesquisa.
- **Lacuna que o híbrido poderia cobrir `[INFERÊNCIA]`:** nesta sessão o Revisor SOT declarou que a veracidade das páginas citadas no Dossiê do Especificador é "não verificável sem web". Um **verificador de fontes ao vivo** (fetcher sem segredos) cobriria essa lacuna — ver Opção C na Proposta. **Importante:** cobrir a lacuna NÃO exige transformar o auditor inteiro em agente com web; basta um passo determinístico de verificação de URL/citação.

### H2 — Segurança: injeção indireta, exfiltração, lethal trifecta
- `[EXTERNO, SRC-TRIFECTA-01]` «If your agent combines these three features, an attacker can easily trick it into accessing your private data and sending it to that attacker.» As três = "Access to your private data" + "Exposure to untrusted content" + "The ability to externally communicate".
- **Confronto com o SOT `[INFERÊNCIA]`:** o auditor já tem (1) dados privados (clone do repo + pode ler o token/`auth.json`, ata 003 §4). Dar-lhe web adiciona (2) conteúdo não confiável **e** (3) comunicação externa de uma só vez → **trifecta completa**. Portanto **REJEITAR** a forma ingênua ("ligar a rede no mesmo agente que hoje roda a auditoria"): seria o pior caso de segurança.
- `[EXTERNO, SRC-OWASP-01]` «Restrict the model's access privileges to the minimum necessary for its intended operations.» + «Separate and clearly denote untrusted content to limit its influence on user prompts.» + `[EXTERNO, SRC-HITL-01]` (não expor o avaliador ao mesmo conteúdo não confiável). → **ADOTAR:** separar **fases** e **privilégios**: pesquisa com rede **sem segredos e sem o token**, idealmente em **outro usuário/contêiner**; auditoria **offline** sobre o commit. Egress allowlist (só domínios de pesquisa) reduz, não elimina, exfiltração. **ADIAR** qualquer desenho que não separe segredo de rede.

### H3 — Viabilidade no Codex CLI (verificável × INDETERMINADO)
- `[EXTERNO, SRC-CODEX-01]` confirmado: a doc oficial descreve modos de sandbox, incluindo `read-only` e `workspace-write`. **INDETERMINADO (não capturado verbatim):** a frase exata de que read-only bloqueia a rede e de que a rede é desabilitada por padrão — consistente com o uso atual do kit (`--sandbox read-only`, ata 003 §2), mas **não** citável como literal até captura da página oficial.
- **`[INFERÊNCIA]`:** habilitar rede no Codex exigiria sair de `read-only` para `workspace-write` **com** `network_access`/`network_proxy` (visto em sumário de busca, não capturado verbatim) → muda a postura de sandbox e exige nova aprovação de ambiente na VM. Ferramenta de busca web nativa do Codex: **INDETERMINADO** (não verifiquei na doc oficial com captura). Nada deve ser afirmado sem captura.

### H4 — Simetria com as regras do Especificador; validação determinística do achado de pesquisa
- **ADAPTAR:** se o auditor pesquisar, aplicam-se a ele as MESMAS regras do Especificador: RULE-ECC-02 (Dossiê, web=dado), RULE-ECC-04 (captura verbatim ≥100 chars em arquivo-fonte), RULE-ECC-06 (régua de repositórios seguros), DHR-PROV-WEB-001 §2.1, TRACE-06 (documentado≠homologado).
- **Validação determinística `[INFERÊNCIA]`:** um **novo tipo de achado** `pesquisa` exigiria campos novos no schema do achado: `url`, `data_de_acesso`, `captura_verbatim` (≥100 chars), `nivel_de_evidencia`, `relevancia`. O validador conferiria: URL bem-formada; citação presente **literalmente** no conteúdo buscado (via fetcher — Opção B); classificação presente. Isto é o análogo de `validate_finding.py` para pesquisa.
- **Interação com PN2 (`rule_source` deve existir):** PN2 confere norma **interna**; o achado de pesquisa confere fonte **externa** — são complementares, mas o validador precisaria distinguir "regra interna existe" de "fonte externa resolve e casa a citação". **Interação com o limite de ~100 KB da Issue `[FATO: kit]`:** capturas verbatim incham a Issue; a captura deveria ir para **arquivo anexo/`sources/` no clone** ou ser truncada com hash, não despejada na Issue. → condição de desenho.

### H5 — Limites de papel, viés e Pacotes 1–3
- **Papel `[FATO]`:** híbrido pesquisador+revisor **não** muda "consultivo, não é gate, responde ao Orquestrador, ENF-03, só Andraus homologa" (ata 001 §1). "Total liberdade de cognição" = liberdade de **investigar e apontar**, não de **decidir/homologar** — o veredito segue derivado deterministicamente (PN1).
- **Viés `[EXTERNO, SRC-JUDGE-01]`:** pesquisa web **traz** risco de viés de autoridade/ referências falsas (quote acima). Logo a ideia de "mais cognição" tem de vir **acoplada** à verificação determinística de citação, senão **aumenta** o viés que Andraus quer evitar. Não é contradição com o Pacote 2 (anti-viés) — é uma **extensão** dele: a pesquisa é mais um canal a blindar.
- **Pacotes já aprovados:** Pacote 1 (coerência do parecer PN1/PN2/PN10), Pacote 2 (anti-viés PN12–PN15), Pacote 3 (rastreio do consenso P1/P2/PN3). **`[INFERÊNCIA]` o que deve entrar ANTES de congelar o esquema do achado:** reservar no schema do achado os **campos opcionais de pesquisa** (acima) já na rodada de reaprovação do manifesto dos Pacotes 1–3 — assim, se Andraus adotar o híbrido depois, **não** é preciso uma segunda reaprovação do schema/manifesto (Economicidade). Reservar campo ≠ ativar o papel.

### H6 — Custo/limites (4Es)
- **`[FATO]` VM:** Oracle E2.1.Micro ~1 GB RAM, timeout 1800 s/chamada, 6 chamadas/dia, limite do plano ChatGPT **não medido**. **`[INFERÊNCIA]`:** pesquisa web ("deep research") é intensiva em tempo/tokens e pode estourar timeout e o limite diário; 1 GB de RAM é apertado. **INDETERMINADO** se a VM comporta pesquisa web significativa — precisa teste. Economicidade: pesquisa cara não pode passar por cima de Eficácia/Efetividade (4Es), mas aqui o risco de segurança (Eficácia de proteção) é o fator dominante, não o custo.

---

### H7 — Subagentes e skills "sem restrições", visando o gate determinístico (acréscimo de Andraus, ata 004 §3-ter)

Andraus (chat, 2026-10-06): *"o auditor poderá quebrar seu próprio trabalho em subagents e usar suas próprias skills sem restrições, visando as entregas conforme as exigências do gate determinístico."*

**H7a — Ganho × risco da decomposição em subagentes/skills.**
- Ganho `[INFERÊNCIA]`: cobertura e paralelismo (dividir a auditoria por arquivo/dimensão); especialização por skill.
- Riscos `[INFERÊNCIA ancorada em EXTERNO]`: (i) **propagação de injeção indireta** entre subagentes — conteúdo malicioso lido por um pode instruir os demais (injeção indireta por conteúdo externo, `[EXTERNO, SRC-OWASP-01, não-capturado-verbatim nesta frase]`; o trecho capturado de SRC-OWASP-01 sobre injeção indireta — «Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files.» — cobre o mecanismo); (ii) **vazamento de segredo** para subagentes (cada subagente roda como o mesmo usuário e pode ler o token/`auth.json` — ata 003 §4); (iii) **perda de rastreabilidade** (quem produziu qual achado); (iv) **viés compartilhado** se todos herdam o mesmo contexto contaminado — e todos são do mesmo modelo (Codex), o que concentra autopreferência/ancoragem (SRC-JUDGE-01) em vez de diversificar; (v) **explosão de custo/tempo** (cada subagente é uma chamada; ver H6).

**H7b — Modelo "liberdade por dentro, gate na fronteira".** A proposta de Andraus é: dentro, liberdade total; a única exigência rígida é que a **saída final** passe pelo gate determinístico (`validate_finding.py`/esquema do achado, citação literal, comandos de reprodução somente-leitura, manifesto). **Avaliação `[INFERÊNCIA]`:** isto é **compatível com ENF-03** e com `[EXTERNO, SRC-HITL-01]` «Use deterministic logic (policy engines, rule-based classifiers) as the authoritative signal, with LLM-assisted classification as an optional input that a deterministic layer re-checks.» — subagentes/skills são todos **insumo**; o sinal autoritativo continua sendo o código de fronteira. **Condição:** o modelo só é válido se o gate **re-checar tudo o que sai** e se nenhum subagente ganhar privilégio (rede/segredo/escrita) que o agente de topo não tem. "Liberdade por dentro" **não** pode significar "rede por dentro" nem "ler segredo por dentro".

**H7c — O que NÃO pode ser "sem restrições", e por quê.**
- **Fronteira de segurança (inegociável):** sandbox, rede e segredos valem para **todos** os subagentes igualmente — a restrição é de **fronteira do processo**, não do agente de topo; um subagente não pode abrir rede nem ler o token. (SRC-TRIFECTA-01 / SRC-OWASP-01.)
- **Orçamento de tempo/memória e chamadas:** a VM é ~1 GB, timeout 1800 s, 6 chamadas/dia (`[FATO]`); subagentes multiplicam chamadas → teto rígido necessário. "Sem restrições" de cognição **não** é "sem restrições" de recursos.
- **Rastreabilidade:** cada subagente precisa registrar o que fez (reprodutibilidade — mesmo princípio do cabeçalho do parecer, protocolo §6).
- **Skills como cadeia de suprimento:** skills têm **procedência** e deveriam ser cobertas por `MANIFEST.sha256` como o resto do kit; uma skill não confiável é um vetor de injeção. `[EXTERNO não-oficial / não-capturado-verbatim]` indícios de que skills do Codex vivem em `~/.codex/skills` e que "subagentes" são `codex exec` aninhados vêm de **fontes comunitárias não-oficiais** (tessl.io, claudeskills.info) — **não** confirmei em documentação oficial da OpenAI → **INDETERMINADO**. **Tensão reverificada `[INFERÊNCIA de FATO]`:** o bot roda `codex exec --ignore-user-config --ignore-rules` (ata 003 §2); se as skills são user-config em `~/.codex/skills`, essas flags **provavelmente as desabilitam** — ou seja, "usar suas próprias skills sem restrições" pode ser **incompatível** com as flags de blindagem atuais, e `~/.codex` é justamente o diretório de segredo que o PROMPT regra 2 proíbe ler. Comportamento exato = **INDETERMINADO** (exige doc oficial/teste).

**H7d — "Tentar atender" o gate sem otimizar-para-passar (Goodhart).**
- Ciclo interno gerar→validar→corrigir antes de postar é saudável e o bot **já limita tentativas** (`MAX_ATTEMPTS`, ata 003 §2). `[INFERÊNCIA]`.
- Risco Goodhart `[INFERÊNCIA]`: o validador mede **forma/ancoragem, não mérito** (o próprio `validate_finding.py` diz "PASS = forma e ancoragem; NÃO é parecer de mérito"). Um auditor "visando o gate" pode **otimizar para passar** (ex.: esticar citação para ≥20 chars, escolher achados fáceis de ancorar) em vez de achar o que importa. Mitigação: o **Revisor semântico independente** + **Andraus** continuam sendo o teste de mérito (o gate é necessário, não suficiente); o veredito derivado deterministicamente (PN1) não premia volume; o **A/B de viés** (PN16) e a calibração N-rollout (PN4) detectam deriva. SRC-HITL-01 sustenta: código é sinal autoritativo, LLM é insumo re-checado — não o contrário.

**H7e — Impacto em A–D e Pacotes 1–3.** Subagentes/skills são **ortogonais à web** (aplicam-se mesmo offline). Reforçam: PN1 (veredito determinístico na fronteira), a reserva de campos no schema do achado (congelar uma vez), e **PN6** (isolamento de usuário de SO) — que passa a ser **mais** crítico, pois cada subagente também pode ler o token. Agravam H7a-v (viés compartilhado) → reforça PN17 (heterogeneidade) e a rastreabilidade por subagente. Não muda o parecer das opções A–D; é uma **camada interna** sob o mesmo princípio "gate na fronteira".

## 4. Lacunas / INDETERMINADO
- Ferramenta de busca web nativa do Codex e semântica exata de rede por modo de sandbox: **INDETERMINADO** (não capturado verbatim da doc oficial).
- Se a VM atual comporta pesquisa web dentro do timeout/limite do plano: **INDETERMINADO** (sem teste; não executei bot/VM).
- Os números de fabricação de citação (SRC-CITE-01) são de fonte **secundária**; a magnitude exata para o modelo específico do auditor é **INDETERMINADA**.
- **H7 — subagentes/skills no Codex exec:** suporte oficial, semântica de `~/.codex/skills` e efeito de `--ignore-user-config/--ignore-rules` sobre skills = **INDETERMINADO** (só encontrei fontes comunitárias não-oficiais, não capturadas verbatim; não confirmei em doc oficial OpenAI). Se a VM de ~1 GB comporta subagentes paralelos dentro do timeout/limite diário = **INDETERMINADO** (sem teste).
- Nenhuma decisão aberta tocada (J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001). SPEC-038-DATASRC-001 = decidida neste recorte com resíduo (BL-033), não re-decidida.

## 5. Etiquetagem
Fontes web = `[EXTERNO]` (captura em `sources/`, veracidade não atestada). Fatos do repo/atas = `[FATO]`. Derivações = `[INFERÊNCIA]`. Propostas e dependências de Andraus = `[PROPOSTA]`/`[DECISÃO NECESSÁRIA]` na Proposta irmã.
