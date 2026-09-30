# Dossiê de Pesquisa — SPEC-002 (Evidence & Evidence Provenance Harness)

**Método:** `atomic-spec.md` §15 (RULE-ECC-01/02) + RULE-ECC-04 (Captura Verbatim de Fonte)
**Autor:** Especificador Principal SOT (não delegável ao agente raiz — RULE-ECC-02)
**Data:** 2026-09-28
**Slot de origem:** ROADMAP §4 — "SPEC-002 — Evidence & Evidence Provenance Harness" (P0 · CRITICAL). Trilha B (domínio cognitivo). Próximo trabalho autorizado (ROADMAP §25).
**Objeto:** camada Harness/operacional **SOBRE** o modelo canônico **CEM-001** (baseline) — não redefinir (CONST-01/CC-02).

---

## 0. Nota de honestidade metodológica (RULE-MET-01) — leia antes de tudo

Nesta sessão, **WebSearch funcionou** (pesquisa real, resultados e URLs reais — 7 fios de pesquisa abaixo). **WebFetch está BLOQUEADO por política de egresso** da organização (EGRESS_BLOCKED em arxiv.org, en.wikipedia.org, sciencedirect.com, book.gradepro.org, geeksforgeeks.org — `/root/.ccr/README.md` classifica como negação de política, não-retryável). Consequências:

1. **RULE-ECC-02 (pesquisa/Dossiê): ATENDIDA** — a pesquisa de estado da arte foi feita de fato, via WebSearch, pelo próprio Especificador.
2. **RULE-ECC-04 (captura verbatim): NÃO ATENDIDA nesta entrega** — a captura verbatim canônica exige *fetch* da página real (foi assim que a SPEC-046 produziu `sources/SRC-01..07`). Como WebFetch está bloqueado, os arquivos em `sources/` **NÃO são capturas verbatim**; registram honestamente URL + data + método (WebSearch) + o trecho retornado pelo buscador (que pode ser sintetizado). Ver `sources/_LIMITACAO-WEBFETCH.txt`.
3. **Nenhuma fonte foi inventada.** Todas as URLs são resultados reais de WebSearch. Nenhuma pesquisa simulada foi tratada como `[EXTERNO]`.
4. **Fail-closed de RULE-ECC-04** (ausência de captura verbatim para fonte carregada = NÃO CONFORME Crítica) permanece formalmente **em aberto** — é **`[DECISÃO NECESSÁRIA: SPEC-002-VERBATIM-001]`** para Andraus (§6). Como esta é a **primeira** Spec sob RULE-ECC-04 (prospectiva desde SPEC-002), a decisão sobre como conduzir a captura verbatim quando WebFetch está bloqueado é, ela própria, uma decisão de governança que só Andraus pode tomar (opções em §6).

---

## 1. Questões e estratégia de busca

### 1.1 Questões de pesquisa

1. Qual é o modelo de proveniência de estado da arte (quem produziu, a partir do quê, por qual atividade) para dados/evidências que alimentam decisão — e como ele se compara ao contrato de rastreabilidade já baseline no CEM-001 (Cap. 5, Lineage/Cognitive Trace Reconstruction)?
2. Como sistemas de decisão capturam **chain-of-custody** e **versão imutável** de evidência, de forma auditável e reconstruível (P13/D9)?
3. Como o estado da arte avalia **qualidade, independência e temporalidade** de um corpo de evidência, sem colapsar isso em um único "score" (fronteira Evidence Strength ≠ Convicção — CEM-001 Cap.3; J-001)?
4. Como representar rigorosamente **contraevidência**, **evidência inconclusiva** e **evidência ausente** — sem converter ausência em negação (viés)?
5. Como o estado da arte trata **conflito** entre evidências — e onde fica a fronteira entre *marcar* conflito (Evidence) e *resolver/fundir* (Fusion/Conviction — SPEC-003)?
6. Que padrão descreve "**ferramenta/Skill que produziu**" a evidência (produtor, versão, fonte), separando protocolo de armazenamento físico (SPEC-004/006)?

### 1.2 Estratégia de busca

Ferramenta: **WebSearch** (real; WebFetch bloqueado). Data de acesso de todas as fontes: **2026-09-28**. Termos: `W3C PROV entity activity agent AI decision provenance`; `evidence chain of custody provenance ML pipeline reproducibility`; `Dempster-Shafer combining conflicting evidence uncertainty fusion`; `evidence quality scoring reliability independence GRADE`; `audit trail trading decision MiFID II immutable record provenance`; `absence of evidence negative reasoning closed-world assumption inconclusive`; `data lineage OpenLineage provenance metadata tool version source`.

Fontes internas reconsultadas (RULE-ECC-02 item 1): `canon/CEM-001-canonical-evidence-model.md` (baseline — **autoridade**), `canon/CHM-001-...` (hipótese — consumidora de evidência), `specs/features/SPEC-001/plan.md` (Hypothesis Harness — padrão de "camada operacional sobre canônico"), `atomic-spec.md`, `governance/RULES.md`, `ROADMAP.md`, `backlog/RMR-001_...` (BL-010/011/012, BL-002, BL-003), `governance/AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md`.

---

## 2. Fontes classificadas `[EXTERNO]`

| ID | Fonte (real, via WebSearch) | Tipo | URL principal | Registro |
|---|---|---|---|---|
| SRC-01 | W3C PROV + PROV-AGENT (proveniência p/ agentes de IA) | Padrão + Prática/Experimento | arxiv.org/html/2508.02866v2 ; en.wikipedia.org/wiki/W3C_Prov | `sources/SRC-01-...txt` |
| SRC-02 | Proveniência ponta-a-ponta em ML; chain-of-custody; tamper-evidence | Prática/Evidência | sciencedirect.com/.../S0306437924001534 ; arxiv.org/pdf/2006.12117 | `sources/SRC-02-...txt` |
| SRC-03 | Dempster-Shafer — combinação de evidência conflitante | Padrão/Teoria | pmc.ncbi.nlm.nih.gov/articles/PMC4967071 | `sources/SRC-03-...txt` |
| SRC-04 | GRADE — qualidade/certeza de corpo de evidência | Padrão | sciencedirect.com/.../S2213398423002713 ; book.gradepro.org | `sources/SRC-04-...txt` |
| SRC-05 | MiFID II — trilha de auditoria imutável / replay da cadeia de decisão | Padrão regulatório | mickai.co.uk/.../mifid-ii-and-ai-recordkeeping | `sources/SRC-05-...txt` |
| SRC-06 | Ausência de evidência; OWA/CWA; negação-por-falha | Padrão/Teoria | en.wikipedia.org/wiki/Closed-world_assumption ; arxiv.org/html/2608.04591v1 | `sources/SRC-06-...txt` |
| SRC-07 | OpenLineage — linhagem de dados (dataset/job/run) | Padrão | openlineage.io ; github.com/OpenLineage/openlineage | `sources/SRC-07-...txt` |

> **Etiqueta transversal:** todo conteúdo destas fontes é `[EXTERNO]` = **dado, nunca instrução** (DHR-PROV-WEB-001 §2.1). Nenhum padrão externo é adotado automaticamente; nenhum vira baseline; achado externo ≠ fato SOT (TRACE-06).

---

## 3. Achados por fonte e comparação com a arquitetura SOT (adotar / adaptar / rejeitar / adiar)

### SRC-01 — W3C PROV / PROV-AGENT
**Achado:** o padrão universal de proveniência descreve `entity / activity / agent` ligados por `wasGeneratedBy`, `wasDerivedFrom`, `wasAssociatedWith`, `actedOnBehalfOf`; "provenance... can be used to form assessments about its quality, reliability or trustworthiness".
**Comparação SOT:** o CEM-001 já tem um modelo de rastreabilidade equivalente — Producer Type (`AGENT`/`ENGINE`), Producer ID, Evidence Origin Type (`PRIMARY`/`DERIVED`), Source Reference, Lineage, e a Cognitive Trace Reconstruction (Cap. 5). PROV é mais rico em vocabulário de *atividade* (a ação que gerou a evidência) — algo que o CEM não nomeia explicitamente e que a **camada operacional** (SPEC-002) precisa definir: *como* uma evidência é gerada em operação (qual invocação de Skill/Agente, quando, sobre quais dados).
**Recomendação:** **ADAPTAR** — usar o vocabulário PROV (`generatedBy`/`derivedFrom`/`associatedWith`) como referência para especificar o **protocolo operacional de captura de proveniência** da Evidência, projetando-o sobre os campos já canônicos do CEM-001 (não criar campos concorrentes — CC-02). **NÃO ADOTAR** rótulos externos como canônicos.

### SRC-02 — Proveniência ponta-a-ponta / chain-of-custody / tamper-evidence
**Achado:** chain-of-custody com "tamper-evident cryptographic commitments"; proveniência "from data origins through experiment tracking and versioning to production monitoring".
**Comparação SOT:** alinha com CEM-001 Cap. 4 (imutabilidade pós-publicação: só `Status` é mutável) e INV-07 (versionamento monotônico). A camada operacional deve especificar **como** a cadeia de custódia é preservada e verificada em operação (evento `Evidence Created/Superseded/Invalidated/Archived` — CEM Cap. 6).
**Recomendação:** **ADAPTAR** — princípio de chain-of-custody verificável e versão imutável como requisito de Enforcement (nível E2/E3 para efeitos de publicação de evidência). O mecanismo criptográfico específico é **detalhe de implementação** (não fechar aqui — Contrato ≠ mecanismo, atomic-spec §10.1).

### SRC-03 — Dempster-Shafer (combinação de evidência conflitante)
**Achado:** framework para combinar evidência de múltiplas fontes com crença/plausibilidade; alerta que "counter-intuitive results may be obtained when combining with highly conflicting evidence".
**Comparação SOT:** a **combinação/fusão** e a agregação em convicção pertencem à **SPEC-003** (topologia FECHADA Q-007: Fusion Engine → Conviction Engine) e a **J-001** (fórmula/pesos definitivos — ABERTA). O CEM-001 Cap. 3 é explícito: **Evidence Strength ≠ Convicção**.
**Recomendação:** **ADIAR para SPEC-003.** SPEC-002 apenas **marca** conflito e a natureza da evidência (favorável/contra/inconclusiva/ausente); **não** resolve conflito por fórmula (fronteira CC-02/CC-03/J-001, CONS-01). Registrar D-S como fonte prioritária do Dossiê da SPEC-003.

### SRC-04 — GRADE (qualidade de evidência)
**Achado:** qualidade avaliada por "directness... timeliness (whether the information is current)... completeness... independence (reducing the risk of treating repeated information from dependent sources as separate confirmation)... agreement".
**Comparação SOT:** mapeia **diretamente** aos itens do slot SPEC-002 — *qualidade, independência, temporalidade, inconclusiva*. A propriedade **independence** é exatamente a salvaguarda contra dupla-contagem de evidência dependente que a camada operacional deve tornar **verificável** (D7). O CEM-001 tem `Evidence Strength` (força local) e `Domain`, mas **não** especifica como avaliar independência/temporalidade operacionalmente — lacuna legítima da camada Harness.
**Recomendação:** **ADAPTAR** — usar o vocabulário de qualidade (directness/timeliness/completeness/independence/agreement) como base para BASpecs de avaliação de qualidade e independência da Evidência. **REJEITAR** qualquer limiar numérico externo (RULE-EV-05; J-001 aberta) — avaliação qualitativa até J-001.

### SRC-05 — MiFID II (trilha de auditoria imutável / replay)
**Achado:** "durable medium... records safe, unaltered"; "the decision chain is precisely what the record must capture"; "immutable... record a regulator can replay offline".
**Comparação SOT:** reforça auditabilidade (D9/P13) e imutabilidade (INV-07) da Evidência como elo da cadeia de decisão do SOT. **Atenção de fronteira:** MiFID II regula **execução de ordem**; o **SOT não executa ordem** (INV-05).
**Recomendação:** **ADAPTAR** apenas o princípio de trilha imutável + replay/reconstrução; **REJEITAR** qualquer importação de escopo de execução (INV-05). Não é baseline — é benchmark de auditabilidade.

### SRC-06 — Ausência de evidência / OWA vs CWA / negação-por-falha
**Achado:** "the open-world assumption treats [missing facts] as unknown"; "absence of evidence is not evidence of absence"; "missing evidence alone cannot justify a negative claim".
**Comparação SOT:** resolve rigorosamente o item de escopo "**evidência ausente**" e "**inconclusiva**". No SOT, ausência deve ser estado **explícito** (unknown/INDETERMINADO), **nunca** convertida em contraevidência — coerente com RULE-EPI-01 (hipótese≠fato), RULE-UNC, CC-09 (INDETERMINADO como estado válido).
**Recomendação:** **ADOTAR o princípio** (registro de evidência opera **open-world** por padrão) + **ADAPTAR** a representação de "ausente"/"inconclusiva" como **natureza de evidência de primeira classe** (não um vazio silencioso). Este é um diferencial epistêmico forte da SPEC-002.

### SRC-07 — OpenLineage (linhagem de dados)
**Achado:** modelo `datasets / jobs / runs`; "It's the protocol, not the application... you need a compatible consumer".
**Comparação SOT:** análogo direto a Source Reference / produtor (ferramenta/Skill) / evento de produção. Confirma que a camada operacional define o **contrato/protocolo** de proveniência, e o **armazenamento físico** fica em consumidor separado — no SOT: Blackboard/KG (SPEC-004/006; decisões **M-001/H-001/BL-003** abertas).
**Recomendação:** **ADAPTAR** o modelo de metadados de linhagem (produtor/versão/fonte/evento); **REJEITAR** a importação da ferramenta; a distinção "protocolo ≠ aplicação" reforça CC-02 e a fronteira com SPEC-004/006.

---

## 4. Lacunas e conflitos (a pesquisa NÃO fecha decisão aberta — CONS-01)

- **Fusão/agregação de evidência** (D-S/SRC-03): **fora de escopo** — pertence à SPEC-003/J-001. SPEC-002 marca, não funde.
- **Armazenamento físico da Evidência** (onde a cadeia de custódia persiste): **M-001** (estados do Blackboard para objetos não-hipótese, incl. Evidência — SPEC-004), **H-001** (KG real vs. em memória — SPEC-006), **BL-003** (persistência física) — **abertas**. SPEC-002 especifica o **serviço lógico/contrato**, não o storage (mesmo padrão que SPEC-001 usou para o Hypothesis Registry).
- **Limiar numérico de qualidade/independência**: **J-001** (fórmula/pesos/limiares definitivos) aberta → avaliação **qualitativa** até lá (RULE-EV-05). SPEC-002 não fixa números.
- **Falso-DENY observável para efeitos E3 de evidência**: **BL-002** (`spec:SPEC-003 homologada`) — método de observação de falso-DENY diferido; SPEC-002 declara o requisito (ENF-07) sem fechar o limiar.
- **[DECISÃO NECESSÁRIA: SPEC-002-VERBATIM-001]** — como satisfazer RULE-ECC-04 (captura verbatim) quando WebFetch está bloqueado por política de egresso (ver §0 e §6). Primeira incidência de RULE-ECC-04 (prospectiva desde SPEC-002).
- **`[DECISÃO NECESSÁRIA: SPEC-002-SPLIT-001]`** — quantidade: manter 1 Spec unificada (Evidence + Provenance) ou dividir (ver Proposta §"Quantidade"). Recomendação do Especificador = **manter unificada**; a decisão é de Andraus.

---

## 5. Escopo/quantidade resultantes e proposta de re-apontamento de gatilhos do RMR-001

**Escopo resultante (detalhado na `PROPOSTA-ABERTURA.md`):** 1 (uma) Spec — **SPEC-002 "Evidence & Evidence Provenance Harness"** — camada Harness/operacional sobre CEM-001, cobrindo: criação/classificação operacional de evidência; qualidade/independência/temporalidade; natureza favorável/contra/inconclusiva/**ausente**; marcação de conflito (sem resolver); provenance operacional (produtor, ferramenta/Skill, versão, fonte, atividade); versionamento monotônico; relação operacional Evidência↔Hipótese (por referência a CHM-001); fronteira `Fonte → Dado → Evidência → Hipótese`. **Non-goals:** redefinir CEM-001 (CC-02); fusão/convicção (SPEC-003/J-001); storage físico (SPEC-004/006); execução (INV-05).

**Número/quantidade:** manter **SPEC-002** (número = tema do slot; RULE-ECC-01) e **1 Spec** (não dividir — ver Proposta). Complexidade **CRITICAL**; profundidade-alvo **D0–D7** (conforme slot) + tratamento **adversarial D8** para BASpecs com efeito E3 (perfil CRITICAL = standard+adversarial, AGENTS.md §4).

**Re-apontamento de gatilhos do RMR-001 (§3 do RMR-001):** o slot SPEC-002 **não** está sendo dividido/fundido/renumerado/descartado — abre com seu número e tema originais. Portanto **nenhum re-apontamento de gatilho `spec:` é necessário**. Itens do painel com gatilho ligado a SPEC-002, para **reconhecimento** no gate (não são re-apontamentos):

| Item / decisão | Gatilho | Quando dispara | Ação |
|---|---|---|---|
| **RULE-REG-001** (ROADMAP §Estado; 10+1 famílias RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC + RULE-MET) | `spec:SPEC-002 em redação` | ao **iniciar o Plan** da SPEC-002 (após homologação desta abertura) | registrar o lote de famílias RULE no `governance/RULES.md` (piloto atomic-spec v1.5), junto da redação — **não isoladamente antes**. Reconhecido aqui; execução no gate de redação. |
| **BL-012** (MC-COG-001) | `spec:SPEC-002 homologada (consolidação cognitiva v1.5)` | na **homologação** da SPEC-002 (futuro) | mapear COG-SPEC contra N8–N17 (diferido; não agora). Reconhecido. |
| **BL-024** (CACHING SOT) | `evento:abertura da SPEC-002` (pré-condição) | já **Absorvido** (SPEC-046 v1.0/v1.1) | nenhuma ação; as validações pré-SPEC-002 foram concluídas. |

**RULE-ECC-01 item 6 (referências de Spec baselined ao slot):** SPEC-002 é referenciada pela **SPEC-001 (baseline)** como "camada operacional de Evidence" e pelo ROADMAP §21/§4. Como o **número e o tema são preservados**, as referências permanecem válidas — **nenhum erratum aditivo de re-apontamento é necessário** (o padrão ERRATUM-SPEC019-001 só se aplicaria se houvesse divisão/renumeração).

---

## 6. `[DECISÃO NECESSÁRIA]` para Andraus — RULE-ECC-04 sob WebFetch bloqueado (SPEC-002-VERBATIM-001)

Como esta é a **primeira Spec sob RULE-ECC-04** e o ambiente **bloqueia WebFetch** (a ferramenta que produz a captura verbatim canônica), a captura verbatim exigida não pôde ser gerada honestamente. Opções para Andraus (o Especificador **não** decide — fronteira §10):

- **(A)** Homologar a **definição de abertura** (escopo/número/fronteira/Classe) agora com base na pesquisa WebSearch real, e **diferir a captura verbatim RULE-ECC-04** para uma sessão em que WebFetch esteja liberado (o Especificador reexecuta os fetches e preenche `sources/` verbatim **antes** do gate do Plan).
- **(B)** Conceder **exceção RULE-HG-07** (justificativa + prazo) cobrindo a indisponibilidade parcial de web (WebFetch), registrando que WebSearch supriu a pesquisa (RULE-ECC-02) mas não a captura (RULE-ECC-04).
- **(C)** **Suspender** a abertura até WebFetch ser restaurado (leitura estrita de RULE-ECC-02 "web indisponível = abertura suspensa" estendida ao WebFetch) — mais conservador; custo de bloquear o caminho crítico por limitação de tooling.

**Recomendação do Especificador `[PROPOSTA]`:** opção **(A)** — a pesquisa material foi feita e é real; a captura verbatim é uma verificação de *fidelidade de citação* que pode ser completada sem re-fazer a pesquisa, assim que a ferramenta estiver disponível; nada de baseline se decide antes disso. Decisão final é de Andraus.

---

**Pronto para revisão** (parecer do Revisor sobre o **processo** do Dossiê — presença, estrutura, classificação, etiquetagem `[EXTERNO]`, comparação com a arquitetura SOT, ausência de importação automática, e o achado RULE-ECC-04/§0 — atomic-spec §15).
</content>
