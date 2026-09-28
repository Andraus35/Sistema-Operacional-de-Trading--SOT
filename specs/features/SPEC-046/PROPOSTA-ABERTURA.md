# Proposta de Abertura — SPEC-046: Spec-Time Context Caching Harness (Grupo B — Especificador/Revisor)

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02)
**Autor:** Especificador Principal SOT
**Data:** 2026-09-28
**Status:** [PROPOSTA] — aguarda parecer do Revisor sobre o Dossiê + homologação de Andraus, ANTES do Plan (AGENTS.md §5; ROADMAP §23)

---

## 0. Mudança de escopo registrada nesta sessão (decisão de Andraus)

Esta proposta foi **restrita ao Grupo B** de `reference/externo/CACHING SOT.MD` §1.1 (caching de spec-time para Especificador/Revisor), por instrução direta de Andraus recebida durante a produção desta sessão (2026-09-28), substituindo o escopo original de instrução (que cobria Grupo A + Grupo B). Esta seção documenta essa decisão de faseamento — **não é omissão, é escopo deliberado desta rodada.**

### Faseamento explícito A vs. B

| | Grupo A (agentes cognitivos internos — runtime) | Grupo B (Especificador/Revisor — spec-time) — **ESTA ABERTURA** |
|---|---|---|
| Objeto cacheado | Evidências, hipóteses, observações (CHM-001/CEM-001) | Prompt/contexto: leitura repetida de `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `backlog/RMR-001_Painel_Backlog.md`, etc. |
| Risco de staleness | Hipótese/estado epistêmico mudou (CHM-001: EMERGENT→...→ARCHIVED) — servir HIT de hipótese já REFUTED/SUPERSEDED como se fosse válida | Agente trabalha sobre versão desatualizada de um documento-fonte do próprio repositório (Spec, CATALOGO-OFICIAL.md, decisão aberta, família RULE) |
| Dependência estrutural | Existência de agentes analíticos (SPEC-010..014) e/ou emenda de SPEC-001 para expor interface de consulta de estado — ver Passo 0 desta sessão, nota de fundo abaixo | Nenhuma — os agentes Especificador/Revisor já existem e operam hoje |
| ACHADO-M2 (Revisor, parecer 2026-09-28) | **Aplica-se integralmente** — precondição de estado CHM-001 verificável antes de HIT | **Não se aplica** — Grupo B não manipula hipóteses de mercado |
| Quando abre | Fase posterior, explicitamente adiada nesta ata | **Agora** (esta Spec) |

**Justificativa do faseamento:** os dois grupos têm regimes de risco, mecanismo de invalidação e maturidade de dependências completamente diferentes (o próprio `CACHING SOT.MD` §1.1 já recomendava avaliação separada). Abrir os dois juntos misturaria um problema **hoje resolúvel com correspondência exata por hash de conteúdo** (Grupo B) com um problema que depende de infraestrutura ainda não existente — interface de consulta de estado de hipótese em runtime, que hoje só existe como índice lógico do Hypothesis Registry da SPEC-001 (ver nota de fundo abaixo), não como contrato de API formalizado. Nada impede que o Grupo A seja aberto como **SPEC-047** (ou número seguinte disponível) quando SPEC-002 (Evidence Harness) e ao menos parte da FASE 5 (SPEC-010..014, agentes analíticos) estiverem mais avançadas — decisão a ser tomada por Andraus naquele momento, não aqui.

### Nota de fundo — Passo 0 desta sessão (não bloqueante para esta abertura)

Verificação de `specs/features/SPEC-001/plan.md` (Hypothesis Harness, HOMOLOGADA — BASELINE): a SPEC-001 define o **Hypothesis Registry como serviço lógico** com responsabilidades declaradas incluindo "Índice de estado" (catálogo de hipóteses por `epistemic_state`) e "API de consulta" (busca por ID, estado, produtor, parent) — ver `SPEC-001/plan.md:568-573`. Isso é **[FONTE]/FATO ARQUITETURAL** (a SPEC-001 marca o próprio Registry como `[INFERÊNCIA]`/FATO ARQUITETURAL, não FATO NORMATIVO fechado — ver `SPEC-001/plan.md:806`), e o **armazenamento físico é explicitamente não definido** pela SPEC-001 ("O Hypothesis Registry não define onde as hipóteses são armazenadas... Isso pertence a SPEC-004/006" — `SPEC-001/plan.md:585-587`). **Conclusão para o Grupo A (fase futura):** existe uma interface lógica de consulta de estado já baseline (o índice por `epistemic_state`), mas **não existe ainda um contrato de API formalizado e testável** (isso depende de SPEC-004/006 para o armazenamento físico, e possivelmente SPEC-010..014 para os produtores reais). Quando o Grupo A for aberto, o Enforcement Contract de precondição de HIT (ACHADO-M2) poderá se ancorar no índice de estado do Registry **como conceito**, mas precisará declarar explicitamente essa dependência de armazenamento físico como bloqueio de implementação plena (Classe H/P, não D). Este parágrafo não bloqueia a presente abertura (Grupo B) — é registrado como inteligência de fundo para a futura SPEC-047.

---

## 1. Número e nome propostos

**Número:** **SPEC-046**
**Nome:** **Spec-Time Context Caching Harness (Especificador/Revisor)**

### Por que SPEC-046 (fora da faixa 002-045)

Os slots 002-045 do ROADMAP §26 estão todos tematicamente ocupados por capacidades de **domínio de trading** (Evidence, Conviction, Blackboard, Event Bus, Knowledge Graph, RAG, Scheduler, agentes analíticos, Synthesis, Mission, TMP, Learning, Testing, Orchestrator, Skills, Tools, Observability, Runtime, End-to-End) — nenhum é sobre caching/tooling do próprio harness de especificação. Reutilizar um desses números seria incompatível com RULE-ECC-01 item 4 (capacidade declarada na abertura deve corresponder ao tema do slot) e criaria confusão de rastreabilidade. `SPEC-046` é o primeiro número livre após a faixa indicativa hoje documentada.

### SPEC-046 como Spec nova vs. emenda a SPEC-019 (Harness Governance) — decisão explícita, com prós/contras

O coordenador pediu avaliação explícita: esta capacidade (caching de spec-time) é, por natureza, mais próxima de **FASE GOV** (SPEC-019/020/021 — governança e maturidade do próprio harness) do que de um slot de domínio de trading. Avaliei três opções:

| Opção | Descrição | Prós | Contras |
|---|---|---|---|
| **(A) Emendar SPEC-019** (Harness Governance & Evolution) | Tratar caching de spec-time como extensão do escopo já homologado de SPEC-019 | Correção taxonômica máxima — SPEC-019 já "governa o próprio Harness" (quem altera Specs, versionamento, etc.) | SPEC-019 é **baseline fechada** (RULE-HG/HV — DHR-SPEC019-001); reabrir um baseline para acrescentar uma capacidade não prevista no escopo original exige o processo de emenda versionada de SPEC-019 (RULE-HV-01..04) — mais pesado que abrir uma Spec nova, e arrisca conflação de escopo: SPEC-019 trata de "quem pode alterar o quê" (autoridade/processo), não de "como o agente lê/reutiliza conteúdo de arquivo" (mecanismo operacional). Risco de violar RULE-HD-02 (nenhum item ADDED pode contradizer o herdado) se o acoplamento for malfeito. |
| **(B) Nova Spec dentro de uma "FASE GOV" reaberta** | Reabrir a FASE GOV conceitualmente e inserir esta Spec ali, com um número reservado à fase | Mantém a Spec fisicamente próxima de 019/020/021 na leitura do ROADMAP | O ROADMAP já declara explicitamente **"FASE GOV CONCLUÍDA"** (ROADMAP linha 29, 235, 411). Reabrir essa fase é uma alteração de tooling do ROADMAP que exigiria decisão própria de Andraus, e colide com a semântica já fechada (SPEC-019+020+021 homologadas, gate fechado limpo). Maior custo de coordenação do que o benefício de organização visual. |
| **(C) Spec nova, numerada fora de 002-045, explicitamente rotulada como "de natureza FASE-GOV-like" no cabeçalho, sem reabrir SPEC-019 nem a FASE GOV** — **ESCOLHIDA** | Abrir SPEC-046 como Spec independente, com nota explícita de que sua natureza é de tooling do harness (mais parecida com 019/020/021 do que com um slot de domínio), mas sem depender de reabertura de baseline nem de fase concluída | Usa o mecanismo já homologado e mais leve (RULE-ECC-01/02, abertura de Spec nova) — exatamente o mecanismo que RULE-ECC-01 item 5 prevê para revisar ordem/dependência "com justificativa homologada", sem exigir emenda de baseline fechada. Preserva INV-07 (nada é apagado/reaberto sem necessidade) e evita reabrir RULE-HD-02/03 sobre SPEC-019. Se amadurecer, pode ser referenciada por SPEC-019 num ciclo futuro de emenda, sem necessidade de tê-la sido desde o início. | Cria uma Spec "fora da grade" 002-045/019-021 que precisa de nota explícita para não ser mal-lida como slot de domínio esquecido — mitigado pela nota de natureza no cabeçalho (abaixo) e pelo registro no RMR-001. |

**Decisão:** Opção **(C)**. Justificativa consolidada: reabrir um baseline fechado (SPEC-019) para acrescentar escopo não previsto é desproporcional a uma capacidade que pode ser especificada e homologada de forma autônoma; reabrir a FASE GOV contraria uma declaração explícita e recente do ROADMAP ("CONCLUÍDA", homologada há poucas horas nesta mesma linha do tempo — DHR-SPEC021-001, 2026-09-28). Abrir como Spec nova, com natureza declarada, é o caminho de menor acoplamento e menor risco de violação de CC-08 (herança) ou RULE-HD-02/03 (supressão/contradição de obrigação herdada).

**Nota de natureza (não normativa, apenas de leitura):** SPEC-046 é uma Spec de **tooling do próprio harness de especificação** (spec-time), não uma Spec de **domínio de trading**. Recomendação para consolidação futura do ROADMAP (a ser avaliada por Andraus, não decidida aqui): quando o Grupo A (SPEC-047, futura) também estiver homologado, considerar se ambas merecem uma seção própria no ROADMAP (ex.: "FASE GOV (cont.) — Caching & Reuse" ou anexadas como apêndice de SPEC-019), sem que isso seja pré-requisito para a presente homologação.

---

## 2. Fronteira e escopo

### Dentro do escopo (SPEC-046, Grupo B apenas)

- Caching de **prompt/contexto** para os agentes Especificador e Revisor durante produção e auditoria de Specs.
- Documentos-alvo (lista indicativa, não fechada): `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `governance/CONSTITUTION.md`, `governance/CONFLICT-MAP.md`, `backlog/RMR-001_Painel_Backlog.md`, `GLOSSARIO.md`, `AGENTS.md`.
- Precondição verificável de "conteúdo do arquivo-fonte inalterado desde a última leitura/cache" — mecanismo de hash de conteúdo + evento de escrita (mtime/git), não TTL cego (ver EC-SPEC046-01).
- Auditoria de higiene de sessão de prompt caching nativo (ordenação, injeção de mensagem, estabilidade de ferramentas — inspirado em SRC-01/SRC-02, adaptado, não adotado como dependência externa).
- Relação com `ENF-03` (LLM não é seu próprio gate — qualquer verificação de freshness deve ser determinística, não uma auto-avaliação do agente) e com **`scripts/check_doc_sync.py`** (já existente, já verifica drift documental — candidato a veículo de implementação, decisão de Plan, não fechada aqui).

### Fora do escopo desta abertura (Non-goals explícitos)

| Item | Motivo | Pertence a |
|---|---|---|
| Grupo A — caching de evidências/hipóteses (CHM-001/CEM-001) dos agentes cognitivos internos (estrutural/institucional/operacional/manager/risco) | Faseamento deliberado desta sessão (decisão de Andraus) — dependências de SPEC-002/010-014 ainda imaturas | Futura SPEC-047 (ou número seguinte disponível) |
| ACHADO-M2 do parecer do Revisor (2026-09-28) — precondição de estado CHM-001 verificável antes de cache HIT | **Aplica-se ao Grupo A**, fora do escopo desta abertura; será endereçado quando o Grupo A for aberto | SPEC-047 (futura) |
| Aplicação automática de correções de caching ao harness (padrão prompt-cache-skills/SRC-03) sem revisão humana | Colide com ENF-03 e INV-09 | Rejeitado nesta Spec; não é non-goal temporário, é rejeição de padrão |
| Benchmark de False-Hit Rate de cache semântico (CacheEval/SRC-04) | Mede risco de correspondência aproximada; o Grupo B usa correspondência exata | Diferido para quando/se o Grupo A avaliar cache semântico |
| Reabertura de SPEC-019/FASE GOV | Ver §1, Opção (C) — decisão explícita de não reabrir | N/A |

---

## 3. Dependências

- **SPEC-001 (Hypothesis Harness)** — baseline, não bloqueante para o Grupo B (mencionada apenas como nota de fundo para a futura SPEC-047/Grupo A, §0 acima).
- **SPEC-019 (Harness Governance & Evolution)** — baseline, referência de vizinhança conceitual (não é dependência técnica de bloqueio; ver §1 Opção C).
- **SPEC-020 (Harness Evaluation)** — as 9 lentes constitutivas (incluindo `principle consistency`) aplicam-se a esta Spec como a qualquer Spec de SPEC-002 em diante — cobertura verificada no Autopré-check do Plan (gate seguinte), não nesta abertura.
- **SPEC-021 (Harness Score/Maturity Model)** — gate normativo E3 por-Spec (RULE-MM-05) aplica-se a esta Spec como a qualquer Spec a partir de SPEC-002.
- **RULE-MECH-01 (Classe por BASpec)** e **RULE-PD-01 (PD-xx)** — incidem a partir de SPEC-002 (homologadas 2026-09-27); esta Spec, por ser aberta depois de SPEC-002 na numeração porém sem SPEC-002 ainda estar homologada, **cita RULE-MECH-01 no próprio texto** (ver §4) e portanto está sob CC-11. **Não é Spec de especialidade de domínio de trading** (não declara Elliott/SMC/ICT), portanto **RULE-PD-01/CC-12 não se aplica** — nenhum `PD-xx` será proposto nesta Spec.
- **`scripts/check_doc_sync.py`** — candidato técnico a veículo de implementação do mecanismo de hash-de-conteúdo; decisão de Plan (gate seguinte), não fechada nesta abertura.
- **Nenhuma dependência de SPEC-002 estar homologada** — o Grupo B é autocontido (Especificador/Revisor já existem e operam), diferente do Grupo A.

---

## 4. Classe RULE-MECH-01 predominante

Esta Spec **cita RULE-MECH-01** no próprio texto (declaração obrigatória acima, §3) — logo está sob CC-11 (declaração de Classe por BASpec, não por Spec inteira — preserva SES-001 §50).

**Classe predominante (só orientação de leitura — não vinculante, atomic-spec §10.6):** **H (Híbrido)** — a maior parte do comportamento desta Spec é: um mecanismo determinístico de verificação de freshness (hash de conteúdo — isso seria Classe D isoladamente), **acoplado** a uma decisão do agente (Especificador/Revisor) sobre *como reagir* quando a precondição falha (ex.: reler o documento vs. abortar a alegação) — isso é julgamento com gate de saída verificável, portanto Híbrido. Não há Classe C (constitutivo/enforcement de risco alto) nesta Spec — o risco de staleness documental em spec-time, embora real, não tem o mesmo nível de irreversibilidade que um commit de hipótese em CHM-001 (Grupo A). A declaração final por BASpec será feita no Plan (gate seguinte), não nesta abertura.

---

## 5. Justificativa explícita para abrir fora da ordem de dependência do ROADMAP (RULE-ECC-01)

Esta abertura ocorre **antes** de SPEC-002 (próximo trabalho autorizado segundo o ROADMAP, linha 29/411), fora da ordem de dependência declarada no §21 do ROADMAP. Isso é justificado por:

1. **Decisão direta e explícita de Andraus**, registrada nesta sessão (2026-09-28), antes mesmo da abertura de SPEC-002 — Andraus optou conscientemente por abrir esta Spec de caching agora, fora da ordem, e instruiu que essa escolha não seja questionada, apenas executada e documentada sob RULE-ECC-01/02 (conforme mensagem desta sessão).
2. **RULE-ECC-01** permite exatamente isso — a regra não fixa "a lista final de Specs, seus números, a quantidade nem as fronteiras" e prevê explicitamente que os slots SPEC-002…045 podem ser "mantidos, divididos, fundidos, substituídos ou descartados com justificativa; NUNCA apagados" (`governance/RULES.md:426-436`) — não fixa quantidade nem numeração final.
3. **Risco reduzido pelo faseamento (§0 desta proposta):** a tensão arquitetural original (abrir caching de **hipóteses de mercado** antes de existirem os agentes analíticos que as produzem — Grupo A) **não se aplica** a esta abertura, porque o escopo foi restringido ao Grupo B. Caching de spec-time é uma melhoria de tooling do próprio harness, sem dependência de nenhum componente de domínio ainda não especificado — os únicos "produtores" de conteúdo cacheável (ROADMAP.md, atomic-spec.md, RULES.md, CATALOGO-OFICIAL.md, RMR-001) já existem e são reescritos hoje pelo próprio processo de governança do SOT.
4. **BL-024** (RMR-001) já estava `Em espera` com gatilho `evento:abertura da SPEC-002` como pré-condição a validar — as ações de validação (RPIR, correção de ordem dos 4Es, classificação preliminar das 5 ferramentas) já estavam concluídas antes desta sessão (ver histórico do BL-024). Esta abertura formaliza, para o Grupo B, o que o BL-024 já vinha preparando.

---

## 6. Enforcement Contract — EC-SPEC046-01 (resolve o risco real do Grupo B; ACHADO-M2 não se aplica aqui)

**Nota de reformulação (instrução desta sessão):** o Enforcement Contract abaixo **não** trata de "hipótese cujo estado mudou" (CHM-001 — isso é ACHADO-M2, Grupo A, fora de escopo). Trata do risco correto do Grupo B: **o Especificador ou o Revisor trabalha sobre uma versão desatualizada de um documento-fonte do próprio repositório** (Spec, `CATALOGO-OFICIAL.md`, decisão aberta, família RULE) porque um cache (em qualquer forma — literal ou "cópia mantida em contexto de sessão") serviu uma leitura antiga.

```
EC-SPEC046-01 — Precondição de Freshness para Reutilização de Conteúdo de Arquivo-Fonte

CAPABILITY   : Reutilizar (sem reler do disco) o conteúdo de um documento-fonte do
               repositório (ROADMAP.md, atomic-spec.md, governance/RULES.md,
               governance/CATALOGO-OFICIAL.md, backlog/RMR-001_Painel_Backlog.md,
               governance/CONSTITUTION.md, governance/CONFLICT-MAP.md, GLOSSARIO.md,
               AGENTS.md) já lido anteriormente na mesma sessão/turno, para fundamentar
               uma afirmação [FONTE] na Spec/parecer em produção

EFFECT       : Uma afirmação classificada [FONTE] na entrega do Especificador (ou uma
               verificação do Revisor) é fundamentada em conteúdo que pode não ser
               mais idêntico ao estado atual do arquivo no repositório

PRECOND      : (hash de conteúdo do arquivo-fonte no momento do uso == hash de
               conteúdo registrado no momento da leitura que originou a cópia em
               contexto) — hash recomendado: SHA-256 do conteúdo do arquivo.
               ALTERNATIVA aceitável quando hash não estiver disponível operacionalmente:
               mtime do arquivo no filesystem/commit do repositório não avançou desde
               a leitura registrada (git — hash de commit do arquivo, quando aplicável).
               Fail-closed: se a precondição não puder ser verificada (nenhum dos dois
               mecanismos disponível), a reutilização é DESAUTORIZADA — o agente
               DEVE reler o arquivo do disco antes de fundamentar a afirmação.

POSTCOND     : Ou (a) a afirmação [FONTE] é fundamentada em conteúdo comprovadamente
               idêntico ao estado atual do arquivo (hash/mtime confirmados), ou
               (b) o agente relê o arquivo do disco e atualiza sua cópia em contexto
               antes de prosseguir, ou (c) a afirmação é rebaixada para [INFERÊNCIA]
               com nota explícita de que a fonte não pôde ser revalidada no momento do uso

POLICY       : INV-09 (sem baseline informal); TRACE-06 (etiquetagem de origem);
               CONS-01 (nenhuma decisão aberta tratada como fechada por conteúdo
               desatualizado); RULE-ECC-01/02 (Dossiê não fecha decisão aberta —
               mesmo princípio de não presumir estabilidade sem verificação)

LEVEL        : E2 (Operacional) — não é E3, porque o efeito de uma afirmação [FONTE]
               desatualizada em spec-time é corrigível no próprio gate (Revisor audita,
               Andraus homologa ou não) antes de qualquer commit irreversível; distinto
               do Grupo A, onde um cache HIT de hipótese stale poderia sustentar
               diretamente um sinal operacional (lá, E3, por isso ACHADO-M2 é crítico
               naquele escopo — não neste)

FAILURE-MODE : Fail-closed dentro do E2 declarado: precondição não verificável →
               reler do disco (nunca presumir freshness); se a releitura não for
               possível no momento (ex.: arquivo temporariamente inacessível), a
               afirmação correspondente DEVE ser marcada [DECISÃO NECESSÁRIA] ou
               [INFERÊNCIA] com a ressalva de fonte não revalidada — nunca [FONTE]
               sem verificação

EVIDENCE     : Registro do hash (ou mtime/commit) da leitura original + hash (ou
               mtime/commit) no momento do uso, disponível para auditoria do Revisor
               (Detector = script determinístico candidato: scripts/check_doc_sync.py
               estendido, ou script novo dedicado — decisão de Plan)
```

**Classe da BASpec que implementa EC-SPEC046-01 (RULE-MECH-01, CC-11):** **H (Híbrido)** — o cálculo/comparação de hash é determinístico (parte Classe D), mas a decisão de "reler vs. rebaixar para INFERÊNCIA vs. abortar" envolve julgamento do agente sobre o impacto da afirmação na entrega — por isso Híbrido, não Determinístico puro. **Bounded loop:** no máximo 1 releitura automática por arquivo por invocação da precondição (sem retry infinito); se a releitura falhar, cai no FAILURE-MODE declarado. **Gate de saída:** comparação de hash é verificável por código (determinística), não por autoavaliação do LLM — coerente com ENF-03.

**Critério 4Es (por que esta é a precondição certa, não uma alternativa mais barata):** Eficácia primeiro — a comparação de hash é a única forma de garantir, com certeza binária, que o conteúdo não mudou (correspondência exata, sem ambiguidade de "aproximadamente igual"); só depois disso Eficiência (evitar releituras desnecessárias quando o hash bate) e Economicidade (menor custo de token) entram como benefício, nunca como justificativa para pular a verificação (AGENTS.md §6 item 11 — Economicidade nunca acima de Eficácia).

---

## 7. Fontes [EXTERNO] que sustentam esta proposta (RULE-ECC-04)

Ver `specs/features/SPEC-046/sources/` — SRC-01 a SRC-07, cada uma com captura verbatim ≥100 caracteres, URL e data de acesso (2026-09-28). Resumo de recomendação por fonte: SRC-01 adaptar, SRC-02 adaptar, SRC-03 rejeitar (aplicação automática) / adaptar (princípio de verificação), SRC-04 adiar (Grupo A), SRC-05 adaptar (metodologia, não números), SRC-06 adotar (entendimento do mecanismo nativo — redireciona o risco real), SRC-07 adotar-adaptado (padrão de hash-de-conteúdo + dependência, base do EC-SPEC046-01).

---

## 8. Próximo passo

Esta proposta e o Dossiê de Pesquisa (`DOSSIE-PESQUISA.md`) seguem para parecer do Revisor sobre o **processo** do Dossiê (presença, estrutura, classificação, etiquetagem `[EXTERNO]`, comparação com a arquitetura SOT, ausência de importação automática — atomic-spec §15) e, em seguida, para homologação de Andraus da **definição** (número, nome, fronteira, Classe, EC) — **antes** de qualquer `plan.md`/`checks.md` da skill `tlc-spec-lean` (gate seguinte, distinto deste, conforme AGENTS.md §5 e ROADMAP §23 passos 1-bis vs. 5+).

**Pronto para revisão.**
