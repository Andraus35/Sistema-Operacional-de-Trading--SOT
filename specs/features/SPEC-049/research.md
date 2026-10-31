# Dossiê de Pesquisa — SPEC-049: WikiRAG Reading View (slot ROADMAP §6, FASE 3)

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-049 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06/07) + DHR-BACKLOG-ABERTURA-001 |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 5.5) |
| **Data de acesso web** | 2026-10-31 (todas as fontes `[EXTERNO]` e repositórios) |
| **Complexidade** | **HIGH D0–D7 — decidida por Andraus (P-1, chat 2026-10-31; a registrar na ata; MEDIUM rejeitada)** — validade do Dossiê **2027-01-29**. *[antes: "PROPOSTA — a confirmar por Andraus (ABERTURA §1, P-1)"; texto da revisão 2 a seguir:]* O slot traz "MEDIUM D0–D5 e Classe D — apenas proposta, a confirmar na abertura dela (C-2)" (`ROADMAP.md` l.193). Recomendo **HIGH D0–D7** (motivo em §8.1); alternativa MEDIUM D0–D5 registrada. Dossiê feito em profundidade HIGH (cobre as duas opções). |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | Data de acesso 2026-10-31. **HIGH decidido (P-1; DHR-SPEC049-001 §1) → 90 dias → validade 2027-01-29.** *[antes: "Se Andraus confirmar **MEDIUM** → 120 dias → **data-limite 2027-02-28**. Se confirmar **HIGH** → 90 dias → **data-limite 2027-01-29**. Vale a data da complexidade homologada; antes disso," — condicional superado pela decisão de Andraus (R3-m01)]* Antes da data-limite, a validade cai se o contexto mudar materialmente (ex.: errata à SPEC-007 que mude o que é "item carimbado", ou decisão sobre CKG-STRUCT-ORIGIN-001 que mude o campo de escola). Dossiê vencido não dispensa reabrir a pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). Tudo o que propõe é `[PROPOSTA]`. |
| **Status epistemológico** | Conteúdo web e de repositórios = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1; RULE-ECC-02). Fontes classificadas e etiquetadas; veracidade das páginas não atestada. Capturas literais em `sources/` (RULE-ECC-04); limitações em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Ordem do Orquestrador por decisão de Andraus (chat, 2026-10-31): "ABRIR a SPEC-049 — WikiRAG Reading View … ETAPA DE ABERTURA … Dossiê de Pesquisa + Proposta de Abertura. NÃO escreva Plan nem checks." Base: DHR-SPEC048-001 Q-2 (slot criado) e C-2 (peso só como proposta até a abertura dela, depois do Dossiê próprio). |
| **Insumos internos (não substituem o Dossiê)** | `specs/features/SPEC-048/research.md` §3.5 e as capturas SRC-LLMWIKI-01 / SRC-GRAPHRAG-01 / REPO-graphrag de lá (2026-10-24) — **recapturadas aqui** com data própria; `specs/features/SPEC-007/plan.md` v2.3 BASELINE (INV-KFH-02; Interface pontos 1, 2, 5; Anexo T — texto v1.2 transferido, insumo **não vigente**). |
| **Fronteiras respeitadas** | INV-04 (nada da página entra no Conviction Vector), INV-05 (a página não recomenda nem decide), INV-06/INV-10 (página ≠ Evidência ≠ Observação), INV-07 (nada é apagado), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001 nem SPEC-006/007/048 (CC-02). |

> **Aviso de método (RULE-MET-01).** (1) Métricas de repositório vieram da página HTML pública; alertas de segurança = INDETERMINADO, registrados como 0 pelo critério das SPEC-006/007/048 (`_LIMITACAO-WEB.txt`). (2) A ferramenta de leitura web limita a citação literal a cerca de 125 caracteres — os trechos são literais (≥100 caracteres), às vezes recorte de frase maior, anotados como tal. (3) O Benchmark Inteligencia-SOT **não** foi lido: nenhuma citação nova (§5). (4) Sem Bash: os gates (`check_repo_research`, `backlog_triggers --abertura`, `build_map`, `check_dimensionamento`) são do Orquestrador (ABERTURA §12). Distingo **[FONTE]** (documento do SOT) de **[INFERÊNCIA]** e de **[EXTERNO]**.

---

## 0. Auditoria de entrada — o que é a SPEC-049 no SOT hoje

| Âncora | Verificação (lida em 2026-10-31) | Resultado |
|---|---|---|
| (a) Slot | `ROADMAP.md` l.192-193: "Visão de leitura montada por regra fixa a partir de itens carimbados da SPEC-007, sem autoridade própria (Q3 da DHR-SPEC007-001); herda a trava "compilação WikiRAG" (INV-KFH-02, E3). Dossiê próprio e homologação de abertura antes de qualquer Plan." | `[FONTE]`, FATO ARQUITETURAL (slot indicativo, NÃO aberto). |
| (b) Origem do slot | DHR-SPEC048-001 §1: Q-2 ("Separar já a página de leitura (WikiRAG) numa Spec própria: SPEC-049 — WikiRAG Reading View (número e nome decididos por Andraus …)"); C-1 (corte do Anexo T confirmado); C-2 ("Só como proposta (MEDIUM D0–D5, Classe D) até a abertura dela, depois do Dossiê próprio; atenção registrada: ela herda a trava "compilação WikiRAG" (E3 na SPEC-007)"). | **FATO NORMATIVO** (ata). Número e nome **não** são reabertos; peso, fronteira fina e quantidade são desta abertura. |
| (c) Sentido já decidido | DHR-SPEC007-001 Q3: "**Versão de leitura** do que já foi carimbado, **montada por regra fixa** (Classe D), refeita a qualquer momento, **sem autoridade própria**; o pacote de evidência **cita só itens carimbados e fontes originais, nunca a página**". | **FATO NORMATIVO** (política). Vira texto normativo só no Plan homologado. Nada a reabrir. |
| (d) Montante baselined | SPEC-007 v2.3 BASELINE (DHR-SPEC007-005): itens carimbados via selo, lidos do KG por consulta read-only (Interface ponto 1, `plan.md` l.1224); fontes/unidades com `rights_status`/permissão de envio efetivos e origem-raiz (ponto 2, l.1225); marcas `revalidation_mark`/`contradiction_mark` — "expor "a revalidar"; servir os dois lados de uma contradição, lado a lado" (ponto 5, l.1228). SPEC-006 v1.7 + erratas: consulta read-only (RULE-CKG-011, `plan.md` l.544), bitemporal `valid_from`/`valid_to` + `recorded_at` (RULE-CKG-004, l.397-399). | **FATO NORMATIVO** (baseline). A SPEC-049 **usa**; não redefine (CC-02). A Interface da SPEC-007 foi escrita para a SPEC-048; os pontos 1, 2 e 5 valem **por analogia** para a página (`[INFERÊNCIA]`; ver §6). |
| (e) Trava herdada | SPEC-007 INV-KFH-02 (vigente, l.432-449) — "as etapas da trilha de consulta (recuperação adaptativa, redação de síntese, juízo F2, compilação WikiRAG) e o gate de montagem/entrega do pacote são da SPEC-048 … estender esta invariante à trilha de consulta é requisito à SPEC-048"; com a C-3 (nota aditiva, l.3) a "compilação WikiRAG" passa à SPEC-049. Texto v1.2 da cláusula no Anexo T, T.1 (l.1959-1960). | **FATO NORMATIVO** (invariante vigente com piso E3 nos seus caminhos de efeito) + **[INFERÊNCIA]** de que a extensão à compilação é requisito à SPEC-049 (a SPEC-048 estendeu só à trilha de consulta — INV-RET-01, `SPEC-048/plan.md` l.421-433, sem citar compilação). |
| (f) Insumo transferido (não vigente) | Corte C-1 (DHR-SPEC048-001): RULE-KFH-015 (`SPEC-007/plan.md` l.2058-2062); EARS 15 (l.2098); BASpec-KFH-015 (l.2225-2239); códigos `WIKI_PAGE_NOT_DETERMINISTIC`/`WIKI_MODEL_TEXT_FORBIDDEN` (l.2115); cenário T21 (l.2365-2371); EC-KFH-009 E1 (l.2461-2471); parte "compilação" da ADV-KFH-11 (l.2406-2407); parte "lado a lado na WikiRAG" da RULE-KFH-016 (l.2064-2068) e da ADV-KFH-25 (l.2428-2429); cláusula "compilação WikiRAG" da INV-KFH-02 (l.1960); parte "página como 2ª verdade" do risco R-8 do Anexo T. | **Texto v1.2, insumo** — não vincula (DHR-SPEC007-005 §3). Os IDs `*-KFH-*` **não** são reutilizados; numeração própria no Plan (prefixo `WRV` proposto, como a SPEC-048 usou `RET`). |
| (g) Requisito que a SPEC-048 já fez à SPEC-049 | `SPEC-048/plan.md` l.1149-1151: "Requisito proposto à SPEC-049 (a confirmar na abertura dela): a página deve ter identificador **distinguível** de citação válida (ex.: um tipo de referência próprio), para que o gate D do pacote possa recusá-la (`WIKI_PAGE_CITED_AS_SOURCE`)". Os testes da SPEC-048 já usam o nome `reading_view_ref` (l.1267, l.1439). | **FATO NORMATIVO** (baseline da SPEC-048, DHR-SPEC048-002) — requisito **proposto**, que esta abertura pode aceitar. Proposta: **aceitar com o mesmo nome** `reading_view_ref` (evita errata à SPEC-048). |
| (h) Fail-closed vigente a montante | DHR-SPEC048-002 §3: "sem atos de Andraus registrados (RIGHTS / EXT_TRANSMISSION / LOCAL_EXECUTOR) todo pedido recebe pacote vazio com a falta declarada"; DHR-SPEC007-005 §3: a linha de montagem segue parada até a 1ª liberação real. | **FATO NORMATIVO.** Enquanto não houver itens carimbados, toda compilação gera **página vazia com a falta declarada** — comportamento correto, não falha. |
| (i) Regras citadas pelo slot | `governance/RULES.md` **não** contém `RULE-KFH-*` (busca 2026-10-31: zero ocorrências): as KFH são regras **locais** do Plan da SPEC-007. RULE-HV-01..04 (l.412-430) regem herança **vertical** macro→micro. | `[FONTE]`. A relação SPEC-049 ↔ SPEC-007/006/048 é **horizontal** (consumo), como a SPEC-048 declarou (`plan.md` l.302) — RULE-HV **não se aplica**; herança obrigação-a-obrigação via CC-08/RULE-HD (`[INFERÊNCIA]`). |
| (j) Fluxo operacional | A página não roda no ciclo de trading; não é lida por agente analítico nem pelo Manager (proposta §3.9). | RULE-ECC-05 **não incide** (§9). |

**Conclusão.** A SPEC-049 é a **visão de leitura**: dado um momento de corte (e uma data de referência da validade — §3.1), montar, **por regra fixa e sem redigir nada**, páginas legíveis a partir dos itens **já carimbados** (SPEC-007), com a citação que permite conferir cada um, as contradições **lado a lado** sem escolher lado, as marcas "a revalidar" e o tempo de validade visíveis — página **reconstruível** (mesma entrada ⇒ mesma página), **sem autoridade**, **nunca** fonte do pacote (SPEC-048) e **nunca** submetida ao KG (SPEC-006). Ela **não** forma nem carimba (SPEC-007), **não** busca para os analistas (SPEC-048), **não** é o KG e **não** chama modelo.

---

## 1. Questões e estratégia de busca

- **Q1.** O que torna uma saída derivada **reconstruível** de forma verificável (mesma entrada ⇒ mesma saída)?
- **Q2.** Como o estado da arte separa uma **visão de leitura** da **fonte de verdade** sem criar segunda verdade?
- **Q3.** Como reconstruir a visão **"como estava em uma data"** num registro só-inserção bitemporal?
- **Q4.** Que regras editoriais maduras impedem uma página de **acrescentar** conteúdo ou **sintetizar** conclusão?
- **Q5.** Como mostrar **afirmações em conflito** sem escolher verdade nem dar destaque a um lado?
- **Q6.** Como declarar que a página é **derivada** (proveniência) sem redefinir o modelo de proveniência do SOT?
- **Q7.** Como exibir texto de terceiros **como dado** (sem conteúdo ativo) e com modelo de página **sem lógica**?
- **Q8.** O que o padrão de mercado "wiki de LLM" / resumo pré-gerado ensina — e por que o SOT faz o contrário?
- **Q9.** Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam "página gerada de fonte por regra"?

**Estratégia:** WebFetch direto de fontes primárias conhecidas para capturar trechos literais; páginas públicas de repositórios e de commits para a régua. Sem envio de dado do projeto. Endereços usados (acesso 2026-10-31):
- `reproducible-builds.org/docs/definition/`; `reproducible-builds.org/specs/source-date-epoch/`.
- `martinfowler.com/bliki/CQRS.html`; `martinfowler.com/eaaDev/EventSourcing.html`; `martinfowler.com/articles/bitemporal-history.html`.
- `en.wikipedia.org/wiki/Wikipedia:No_original_research`; `…:Verifiability`; `…:Neutral_point_of_view`; `www.wikidata.org/wiki/Help:Ranking`.
- `www.w3.org/TR/prov-o/`; `cheatsheetseries.owasp.org/…/Cross_Site_Scripting_Prevention_Cheat_Sheet.html`; `mustache.github.io/mustache.5.html`.
- Recaptura: `gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`; `arxiv.org/abs/2404.16130`.
- Repositórios (página + commits do branch padrão): `gohugoio/hugo`, `sphinx-doc/sphinx`, `mkdocs/mkdocs`, `simonw/datasette`, `jackyzha0/quartz`, `microsoft/graphrag`. Consultada também a página de configuração do Sphinx (sem achado — `_LIMITACAO-WEB.txt` item 5).
- Leitura interna (somente leitura): HANDOFF; ROADMAP (l.179-193, l.523); atomic-spec §15; especificador.md; RULES.md (RULE-ECC-01..07, RULE-HV-01..04); SPEC-048 ABERTURA/research/plan (Interface com a SPEC-049; INV-RET-01; T04; ADV-RET-11); SPEC-007 plan (INV-KFH-02; Interface; Anexo T); SPEC-006 plan (RULE-CKG-004/011); DHR-SPEC007-001 (Q3); DHR-SPEC048-001/002; ERRATUM-REAPONT-001 (N-F); RMR-001 (gatilhos; BL-010/011/017/029/035); `scripts/backlog_triggers.py` (`abertura_scope`); `scripts/check_repo_research.py` (régua); MC-RAG-001 (RAG-P08/P10/P12, RAG-SPEC-020); WORKFLOW.md v2.1 (WF-D03); LEDGER-ACHADOS §2-bis.

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-REPRO-01 | Reproducible Builds — definição | Padrão (de facto, comunitário) + Prática | Q1 — definição de reprodutível |
| SRC-SDE-01 | Reproducible Builds — SOURCE_DATE_EPOCH | Padrão (especificação comunitária) + Prática | Q1 — nada de "hora atual" na saída |
| SRC-CQRS-01 | Fowler — CQRS | Prática + Opinião (de especialista) | Q2 — modelo de exibição separado; aviso de complexidade |
| SRC-EVSRC-01 | Fowler — Event Sourcing | Prática | Q2/Q3 — estado descartável, refeito do registro; consulta "até um momento" |
| SRC-BITEMP-01 | Fowler — Bitemporal History | Prática | Q3 — "o que o sistema sabia em X" |
| SRC-WPNOR-01 | Wikipedia — No original research (inclui Synthesis) | Prática (política editorial comunitária) | Q4 — não acrescentar; não sintetizar conclusão |
| SRC-WPV-01 | Wikipedia — Verifiability | Prática (política editorial comunitária) | Q4 — cada afirmação conferível na fonte |
| SRC-WPNPOV-01 | Wikipedia — Neutral point of view | Prática (política editorial comunitária) | Q5 — conflito não é apresentado como fato |
| SRC-WDRANK-01 | Wikidata — Help:Ranking | Prática (contraste) | Q5 — vários valores convivem; posto "preferido" rejeitado |
| SRC-PROVO-01 | W3C PROV-O | Padrão (Recomendação W3C) | Q6 — página como entidade derivada |
| SRC-OWASP-XSS-01 | OWASP — XSS Prevention Cheat Sheet | Prática (de facto, segurança) | Q7 — texto de terceiro codificado na saída |
| SRC-MUSTACHE-01 | mustache(5) — logic-less templates | Prática | Q7 — modelo de página sem lógica |
| SRC-LLMWIKI-01 | Karpathy — gist "llm-wiki.md" | Opinião + Prática emergente | Q8 — contraste (wiki escrito pelo modelo) |
| SRC-GRAPHRAG-01 | arXiv 2404.16130 — GraphRAG | Experimento + Prática | Q8 — contraste (resumos pré-gerados) |
| REPO-hugo / REPO-sphinx / REPO-datasette / REPO-quartz / REPO-graphrag | repositórios **elegíveis** (§4) | Prática | Q9 |
| REPO-mkdocs | repositório **NÃO ELEGÍVEL** (§4) | — (registrado, não adotado) | transparência da régua |

Fontes internas de requisitos (não `[EXTERNO]`): MC-RAG-001 (BL-010; referência externa classificada) e o Anexo T do plano da SPEC-007 (insumo).

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Reconstrução verificável (Q1) — **ADAPTAR a definição; ADOTAR "sem hora atual"**
[EXTERNO, SRC-REPRO-01 — verbatim] *"A build is reproducible if given the same source code, build environment and build instructions, any party can recreate"*. [EXTERNO, SRC-SDE-01 — verbatim] *"Build processes MUST use this variable for embedded timestamps in place of the "current" date and time."*
**Comparação SOT:** a Q3 da DHR-SPEC007-001 já exige página "refeita a qualquer momento" e o insumo RULE-KFH-015 diz "mesma entrada publicada ⇒ mesma página" (T21: `hash(page_1) == hash(page_2)`). O que falta no insumo é dizer **o que é "a mesma entrada"**. **Adaptar** `[PROPOSTA]`: entrada = (i) o **momento de corte** (tempo de registro do KG — `recorded_at`, SPEC-006 RULE-CKG-004); (ii) o conjunto de itens carimbados e de marcas lido **até** esse corte; (iii) a **versão da regra de compilação** (agrupamento, ordem, modelo de página). (iv) a **data de referência da validade** (`valid_at`, nome proposto — tempo de **validade**, distinto do corte, CC-10), contra a qual cada item é julgado vigente/encerrado (§3.3); se o pedido não a declarar, a regra de compilação a preenche **com o mesmo instante do corte**, antes de compilar, e grava o valor na entrada (ABERTURA S1 (iv), C-4). A página traz os quatro campos e o hash da **entrada**; o hash da **saída** fica só no **registro de compilação** (§3.6; ABERTURA S7) — um hash não pode estar dentro do que mede. *[antes: "(i)-(iii) … A página traz os três e o hash da entrada e da saída" — circular e sem referência de validade (R1-m03, R1-M01)]* **Adotar** o análogo do SOURCE_DATE_EPOCH: **nenhuma hora do relógio** na página nem no julgamento de validade — os únicos tempos são os da entrada (corte e `valid_at`) e a janela de validade dos itens (derivada — §3.3) *[antes: "os campos de validade dos itens"]*; mesmo corte com `valid_at` diferente = outra entrada. *[antes: "o único tempo impresso é o do corte"]* Sem isso, duas compilações da mesma entrada já dariam hashes diferentes e o teste T21 seria impossível de cumprir por construção. Classe **D**.

### 3.2 Visão de leitura ≠ fonte de verdade (Q2) — **ADAPTAR a separação; REJEITAR adotar CQRS como arquitetura**
[EXTERNO, SRC-CQRS-01 — verbatim] *"The change that CQRS introduces is to split that conceptual model into separate models for update and display"* — e o aviso, também literal: *"For some situations, this separation can be valuable, but beware that for most systems CQRS adds risky complexity."* [EXTERNO, SRC-EVSRC-01 — verbatim] *"We can discard the application state completely and rebuild it by re-running the events from the event log"*.
**Comparação SOT:** casa com o que já está decidido: a verdade permanente é o KG (SPEC-006, só-inserção — H-001 FECHADA, Opção C); a página é **exibição**, descartável e refeita do registro. **Adaptar** `[PROPOSTA]`: a página **não é guardada como verdade**; o que fica registrado é a **compilação** (entrada, versão da regra, hashes) em registro só-inserção do próprio componente; a página pode ser descartada e refeita idêntica. **Rejeitar** adotar CQRS/event sourcing como mecanismo: complexidade sem ganho de Eficácia para uma visão sem efeito; motor = BUILD.

### 3.3 "Como estava em uma data" (Q3) — **ADOTAR o sentido bitemporal já homologado**
[EXTERNO, SRC-BITEMP-01 — verbatim] *"I find I can make sense of much of this tangle by thinking of time as two dimensions - hence the term “bitemporal”."* [EXTERNO, SRC-EVSRC-01 — verbatim] *"Notionally we do this by starting with a blank state and rerunning the events up to a particular time or event."*
**Comparação SOT:** a SPEC-006 já é bitemporal (`valid_from`/`valid_to` + `recorded_at`, RULE-CKG-004) — mas, na regra normativa, `valid_from`/`valid_to` são campos de **relação** (`SPEC-006/plan.md` l.322, l.395-400, l.710; SPEC-007 RULE-KFH-009 l.683-685). **Premissa `[INFERÊNCIA]`:** o item carimbado (nó `learning`, SPEC-007 l.1224) tem janela de validade, vinda de (1) o esquema lógico de `node_record` (SPEC-006 l.1419-1420, "nós também têm validade — CKG-012"), (2) o registro de invalidação que gera `INVALIDATED_IN_TIME` (l.718, l.1073) ou (3) a extensão local `[PROPOSTA]` RULE-KFH-009 a nós; o Plan escolhe e ancora, sem inventar campo (ABERTURA §15 cond. 13). *[antes: janela atribuída ao item sem etiqueta (R2-m01)]* **Adotar** `[PROPOSTA]`: a página é "o que o SOT tinha carimbado no corte X" (tempo de registro), e cada bloco mostra o período de **validade** do item (tempo de validade) e o seu estado **em relação à data de referência da validade `valid_at`** da entrada (§3.1 (iv)) — vigente / encerrada / ainda não vigente / validade não informada. Sem `valid_at` na entrada, "encerrada" exigiria o relógio (proibido, §3.1) ou confundiria corte com validade (CC-10) — por isso é campo próprio, derivado do corte só por regra declarada. *[antes: sem data de referência (R1-M01)]* Item com validade encerrada em `valid_at` **não** aparece como atual sem sinal — é o critério de aceitação de RAG-SPEC-020 (MC-RAG-001 l.510: "conhecimento temporalmente incompatível não deve ser apresentado como atual sem sinalização"). Nada redefinido: só leitura pela consulta read-only (RULE-CKG-011).

### 3.4 Não acrescentar, não sintetizar (Q4) — **ADOTAR, e tornar mecânico**
[EXTERNO, SRC-WPNOR-01 — verbatim] *"original research means material—such as facts, allegations, and ideas—for which no reliable source has ever been published."* e *"Do not synthesize meaning from multiple sources to state or imply a conclusion not explicitly stated by any of those sources."* [EXTERNO, SRC-WPV-01 — verbatim] *"In the English Wikipedia, verifiability means that people can check that facts or claims correspond to reliable sources."*
**Comparação SOT:** a Wikipedia aplica isso por **juízo editorial** de pessoas; o SOT pode aplicar **por construção**: na compilação **ninguém redige nada**. **Adotar** `[PROPOSTA]`: o texto da página é só (a) campos dos itens carimbados, copiados como estão; (b) texto **fixo** da regra de compilação (rótulos, títulos de seção — parte da versão da regra, revisada e homologada com o Plan); (c) citações e identificadores. Qualquer outro texto ⇒ página não emitida (`WIKI_MODEL_TEXT_FORBIDDEN` do insumo). Cada bloco leva a **citação conferível**: `published_item_ref@version` e a cadeia selo → validação → candidato → unidade → fonte@hash (SPEC-007 ponto 1, D9). "Fonte confiável" no SOT = **item sob selo**, não reputação.
**Acepção a fixar no Plan (CC-10) — `[INFERÊNCIA]`, confirmação C-1 da ABERTURA:** o texto de um item carimbado foi, na origem, formado por modelo (formação Classe H da SPEC-007) e depois validado (F1) e carimbado. A frase do insumo "Texto redigido por modelo NÃO compõe página" só faz sentido como "**nenhum texto novo** de modelo **na compilação**"; o texto **já carimbado** é exatamente o que a Q3 manda exibir ("versão de leitura do que já foi carimbado").

### 3.5 Conflito lado a lado, sem escolha (Q5) — **ADOTAR neutralidade; REJEITAR posto "preferido" e destaque proporcional**
[EXTERNO, SRC-WPNPOV-01 — verbatim] *"representing fairly, proportionately, and, as far as possible, without editorial bias, all the significant views"* e *"If different reliable sources make conflicting assertions about a matter, treat these assertions as opinions."* [EXTERNO, SRC-WDRANK-01 — verbatim] *"Ranks are therefore used in order to allow users to easily differentiate between the multiple values of a statement."* e *"The preferred rank is assigned to the most current statement or statements that best represent consensus"*.
**Comparação SOT:** a SPEC-007 registra a contradição (`contradiction_mark`, RULE-KFH-016 v2.0) e pede "servir os dois lados de uma contradição, lado a lado" (ponto 5); a parte "lado a lado **na página**" é desta Spec (C-1). **Adotar** `[PROPOSTA]`: os dois (ou mais) lados de cada `contradiction_mark` aparecem **no mesmo bloco**, cada um com sua citação, **sem** escolha de verdade, **sem** posto "preferido", **sem** destaque por peso ("proporcionalmente" é rejeitado: no SOT nenhum lado ganha espaço ou posição). **A ordem dos lados também é neutra e fixa** (ex.: pelo identificador do item) — ordem por escola, data, número de fontes ou hierarquia analítica insinuaria preferência; a hierarquia Elliott→…→ICT (CC-01) é regra da **análise**, não da página. Omitir um lado **que está na entrada** ⇒ a página inteira não é emitida, com o código `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN` da SPEC-007 (`plan.md` l.1678) usado **por referência**, não redefinido (ou código próprio `WRV`, a declarar no Plan); lado **ausente da entrada** (não carimbado até o corte) ⇒ bloco emitido com "lado não exibível" (ABERTURA S5 (a)/(b)); parte transferida da RULE-KFH-016. *[antes: "Omitir um lado ⇒ página não emitida (análogo a `CONTRADICTION_SILENT_RESOLUTION_FORBIDDEN` …)" (R2-m02)]* É a aplicação de RAG-P08 ("Evidências conflitantes devem ser preservadas e sinalizadas", MC-RAG-001 l.91-92).

### 3.6 A página declara que é derivada (Q6) — **ADAPTAR o conceito; não adotar o vocabulário**
[EXTERNO, SRC-PROVO-01 — verbatim] *"A derivation is a transformation of an entity into another, an update of an entity resulting in a new one,"*
**Comparação SOT:** proveniência no SOT é CEM-001/SPEC-002 (não redefinidos — CC-02). **Adaptar** `[PROPOSTA]`: a página é entidade **derivada** e diz isso no cabeçalho (corte, data de referência da validade, versão da regra, hash da entrada, lista dos itens usados); o hash da saída fica só no registro de compilação. **Identificador próprio**: aceitar o requisito inverso da SPEC-048 com o nome que os testes de lá já usam — **`reading_view_ref`**, tipo de referência **disjunto** de `published_item_ref@version` e de `source_id@hash`, para que o gate D do pacote o recuse (`WIKI_PAGE_CITED_AS_SOURCE`, `SPEC-048/plan.md` l.789, T04, ADV-RET-11). Usar outro nome exigiria errata à SPEC-048. **Não** adotar PROV-O como esquema.

### 3.7 Texto de terceiro como dado; modelo de página sem lógica (Q7) — **ADAPTAR**
[EXTERNO, SRC-OWASP-XSS-01 — verbatim] *"The purpose of output encoding (as it relates to Cross Site Scripting) is to convert untrusted input into a safe form"*. [EXTERNO, SRC-MUSTACHE-01 — verbatim] *"We call it "logic-less" because there are no if statements, else clauses, or for loops. Instead there are only tags."*
**Comparação SOT:** o texto de um item carimbado veio, na origem, de fonte externa; pode conter instrução embutida ou marcação ativa (a SPEC-007 garante "instrução embutida não vira efeito" — INV-KFH-02 —, **não** que o texto saia limpo). **Adaptar** `[PROPOSTA]`: (i) o texto do item é **DADO** ao ser exibido — codificado na saída, nunca interpretado como marcação ativa, link executável ou instrução (mesmo princípio de `content_role = DATA` da SPEC-048); (ii) o **modelo de página não tem lógica**: só encaixa campos em lugares fixos; filtro, agrupamento e ordem ficam na regra de compilação versionada. A técnica concreta (formato, biblioteca) = BUILD.
**Agrupamento por regra fixa** `[PROPOSTA]` (D4 no Plan): chave de agrupamento só por **campos de lista fechada** do item (ex.: ativo, tipo de nó, assunto do vocabulário do sistema — mesma lógica da P-2 da DHR-SPEC048-002); item sem o campo vai a um grupo "sem classificação" declarado, **nunca** a um grupo adivinhado. O campo **escola de `structure`** depende de **CKG-STRUCT-ORIGIN-001 (ABERTA, BL-035)**: a página não infere escola; ausente ⇒ grupo "escola INDETERMINADA".

### 3.8 "Wiki de LLM" e resumo pré-gerado (Q8) — **REJEITAR como conteúdo; ADAPTAR a lista de saúde**
[EXTERNO, SRC-LLMWIKI-01 — verbatim] *"Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki"* e *"The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references,"*. [EXTERNO, SRC-GRAPHRAG-01 — verbatim] *"graph from the source documents, then to pregenerate community summaries for all groups of closely related entities."*
**Comparação SOT:** o padrão de mercado é o **oposto** do decidido: o modelo escreve e mantém as páginas. No SOT isso seria conhecimento **sem selo** servido como leitura (SPEC-006 RULE-CKG-010 `FORMED_WITHOUT_SEAL`). **Rejeitar** como conteúdo e como agrupamento (comunidades detectadas por modelo). **Adaptar** a lista de saúde do próprio gist — [EXTERNO, SRC-LLMWIKI-01 — verbatim] *"Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links,"* — como **checagens determinísticas** da compilação, **sem** consertar nada: lado de contradição que está na entrada omitido ⇒ a página inteira não sai; lado ausente da entrada ⇒ "lado não exibível" + "contradição incompleta" no relatório (ABERTURA S5 (a)/(b)) *[antes: "contradição sem os dois lados ⇒ não emite" (R2-m02)]*; item com validade vencida ou "a revalidar" ⇒ sinal visível; página órfã ⇒ registrada no relatório da compilação. Reconfirma a SPEC-048 §3.5 (insumo).

### 3.9 Quem lê a página — **PROPOSTA a decidir por Andraus (P-2 da ABERTURA)**
`[INFERÊNCIA]` das decisões vigentes: o caminho de conhecimento para **agentes** já é o pacote da SPEC-048 (direto ao analista, só leitura — P-9), e o pacote nunca cita a página (Q3). Se um agente lesse a página, receberia texto **sem autoridade** por uma porta lateral à SPEC-048 (sem as travas de locus, envio e F2 de lá). **Proposta:** a página é para **leitura humana** (Andraus, auditoria); agente analítico e Manager **não** a consomem (requisito às Specs deles, `[INFERÊNCIA]`). Isso também afasta a SPEC-049 do caminho de leitura em runtime (SPEC-045-RUNTIME-001, **ABERTA** — não decidida aqui).

### 3.10 Trecho de fonte e direitos — **PROPOSTA a decidir por Andraus (P-3 da ABERTURA)**
`[FONTE]` SPEC-007 ponto 2 (`rights_status`/permissão de envio efetivos) e P-11 (derivado herda restrição, DHR-SPEC007-003/004). **Opções:** (A) a página mostra só o **item carimbado** + a **citação** (endereço da fonte), **sem copiar trecho** da fonte original — `[PROPOSTA recomendada]`: mantém a página dentro de "versão de leitura do que já foi carimbado" e evita que um trecho **não carimbado** apareça numa página sem autoridade; (B) mostra também o trecho citado, só de fonte com uso liberado (`rights_status` efetivo ≠ INDETERMINADO). Em ambas, a página exibe a **restrição de uso mais restritiva** dos itens que contém e **não sai da casa**: enviar a página a modelo de terceiro ou a outra pessoa = **fora do escopo** (a trava de envio da SPEC-007 — CIM — cobre chamada de **modelo**; distribuição a pessoas de fora não é regida hoje — lacuna registrada §7, item 6).

### 3.11 Contexto, latência — **ADIAR / declarar não aplicável**
A página está **fora do ciclo** de trading: latência-alvo **não** é requisito (`[INFERÊNCIA]`); custo de compilação sob demanda vs. guardada = BUILD (P-5 da ABERTURA só decide o comportamento). Orçamento de contexto (SPEC-043) não se aplica: ninguém põe a página em contexto de modelo (§3.9).

---

## 4. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua: licença aberta conhecida; ≥300 estrelas; último commit ≤12 meses antes do acesso; não arquivado; 0 alerta grave público aberto; dono identificável. Uma captura por repositório em `sources/REPO-*.txt`. Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Último commit | Veredito | Uso no SOT |
|---|---|---|---|---|---|
| https://github.com/gohugoio/hugo | 90300 | Apache-2.0 | 2026-10-30 | **ELEGÍVEL** | Referência — página gerada de arquivos-fonte por modelo fixo, refeita a qualquer momento; nenhuma alegação de reprodutibilidade byte a byte do Hugo (não verificada); não é dependência. |
| https://github.com/sphinx-doc/sphinx | 8100 | BSD-2-Clause | 2026-10-29 | **ELEGÍVEL** | Referência — documentação compilada com referências cruzadas resolvidas na compilação (análogo a "citação resolvível"); não é dependência. |
| https://github.com/simonw/datasette | 11500 | Apache-2.0 | 2026-10-22 | **ELEGÍVEL** | Referência — publicar dados para leitura, separado de quem escreve os dados; não é dependência. |
| https://github.com/jackyzha0/quartz | 13500 | MIT | 2026-04-20 | **ELEGÍVEL** | Referência de contraste — notas escritas pela pessoa viram site com ligações; aqui ninguém escreve na compilação; só a ideia de ligações e de página órfã. |
| https://github.com/microsoft/graphrag | 36500 | MIT | 2026-10-20 | **ELEGÍVEL** | Referência de contraste — resumo pré-gerado por modelo **não** compõe a página; só a ideia de visão pré-compilada por regra fixa. |
| https://github.com/mkdocs/mkdocs | 22500 | BSD-2-Clause | 2025-10-20 | **NÃO ELEGÍVEL** (commit > 12 meses: 376 dias) | Registrado e descartado — nada aproveitado do repositório. |

Resultado: **5 repositórios elegíveis** (referência; **nenhum** adotado como dependência — motor = BUILD); **1 não elegível** registrado. Comando a rodar pelo Orquestrador: `python scripts/check_repo_research.py specs/features/SPEC-049` e `--all`.

---

## 5. Benchmark Inteligencia-SOT (DHR-BENCH-INTEL-001) — sem leitura nova

Motores, agentes e skills do projeto paralelo **não** são usados; só ideias de controle, reescritas pelo SOT. Nesta sessão nada foi lido, **nenhuma citação nova**. Do já registrado no Dossiê da SPEC-007 (§5.2), toca a página **só** a linha **B10** (conflito mostrado, não resolvido — serve a §3.5), por número de linha da tabela de lá, sem reconferência. Nenhum texto/código copiado.

---

## 6. Cobertura × lacuna × dono

| Capacidade | Já coberto? | Tratamento proposto |
|---|---|---|
| Itens carimbados, cadeia até fonte@hash, marcas, restrição de uso efetiva | **SIM** — SPEC-007 v2.3 | **Consumir** (pontos 1, 2, 5 por analogia); não redefinir (CC-02) |
| Consulta read-only ao KG; bitemporal | **SIM** — SPEC-006 RULE-CKG-011/004 | Usar por referência |
| Recusa de página como citação no pacote | **SIM** — SPEC-048 RULE-RET-004 (`WIKI_PAGE_CITED_AS_SOURCE`) | Aqui só o identificador disjunto `reading_view_ref` (requisito inverso) |
| Compilação por regra fixa (entrada, agrupamento, ordem, modelo de página) | **NÃO** | **Lacuna central** (insumo RULE-KFH-015; §3.1/§3.7) |
| Reconstrução (mesma entrada — corte, itens/marcas, versão da regra, `valid_at` — ⇒ mesma página) | **NÃO** | **Lacuna central** (insumo T21; §3.1) |
| Nenhum texto novo na compilação | **NÃO** | **Lacuna central** (insumo `WIKI_MODEL_TEXT_FORBIDDEN`; §3.4) |
| Contradição lado a lado na página | **NÃO** (registro na 007; pacote na 048) | **Lacuna central** (parte transferida da RULE-KFH-016; §3.5) |
| Marcas e tempo visíveis | **NÃO** na página | **Lacuna** (ponto 5; RAG-SPEC-020; §3.3) |
| Compilador sem capacidade de efeito (trava E3) | **SIM** para formação/F1 (007) e consulta (048); **NÃO** para a compilação | **Lacuna central** (cláusula "compilação WikiRAG" da INV-KFH-02; §0 e) |
| Exibição como dado | **NÃO** | Lacuna (§3.7) |
| Quem lê; trecho de fonte; distribuição fora | **NÃO** | Decisão de Andraus (P-2, P-3, P-6) |

**Invariantes de fronteira (reafirmados):** INV-04 (nada da página vira convicção); INV-05 (página não recomenda); INV-06/INV-10 (página ≠ Evidência ≠ Observação); INV-07 (registro de compilação append-only; nada apagado); CC-02.

---

## 7. Lacunas, conflitos e INDETERMINADOS (RULE-MET-01)

1. **"Texto de modelo" × texto carimbado** (§3.4) — acepção `[INFERÊNCIA]`; confirmação C-1 da ABERTURA.
2. **Extensão da INV-KFH-02 à compilação** — a SPEC-048 estendeu à consulta (INV-RET-01) e não citou a compilação; a SPEC-007 l.444-447 diz "requisito à SPEC-048" e a nota C-3 move a página à SPEC-049. `[INFERÊNCIA]`: o requisito cabe aqui. Conflito de redação registrado, não resolvido em silêncio; nenhum baseline editado.
3. **Interface da SPEC-007 escrita para a SPEC-048** — os pontos 1, 2 e 5 valem para a página **por analogia** `[INFERÊNCIA]`; se Andraus quiser, uma nota aditiva à SPEC-007 ("os pontos 1, 2 e 5 valem também para a SPEC-049") pode ser proposta no Plan (passo à parte, não executado).
4. **Peso** — o slot propõe MEDIUM D0–D5; o perfil MEDIUM não tem D7 (BASpec com VERIFICADO POR), e o insumo traz teste (T21) e caso adversarial (ADV-11 parte compilação) ligados a uma trava E3. Ver §8.1 e P-1.
5. **Campo de escola para agrupar** — CKG-STRUCT-ORIGIN-001 **ABERTA** (BL-035); ausente ⇒ "escola INDETERMINADA".
6. **Distribuição da página a pessoas de fora** — não regida por nenhuma Spec baselined (a CIM rege chamada de modelo); proposta: fora do escopo (P-6).
7. **Alertas de segurança dos repositórios** = INDETERMINADO (registrados como 0).
8. **Benchmark** sem reconferência (§5).

**Permanecem abertas (CONS-01):** J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WORKFLOW-SOT-001 (WF-D03), CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção, forma de confirmar a identidade de Andraus (BUILD). Este Dossiê não fecha nenhuma.

---

## 8. Escopo, quantidade, decomposição e re-apontamento

### 8.1 Peso — opções
- **(A) HIGH D0–D7 — RECOMENDADA; ESCOLHIDA por Andraus (P-1, chat 2026-10-31)** `[PROPOSTA]` até a homologação. *[antes: "RECOMENDADA"]* Motivo (Eficácia primeiro): o perfil MEDIUM pára em D5 e **não** tem D7 ("BASpec completo com VERIFICADO POR — HIGH e CRITICAL", atomic-spec l.52). Sem D7, a trava E3 herdada (compilador sem capacidade de efeito) e a reconstrução (T21) ficariam **sem teste** — mais fraco do que o insumo, que vinha de Spec CRITICAL com teste. A C-2 já avisava: "Peso médio só se sustenta se essa trava continuar valendo do mesmo jeito". D6 (protocolo do Blackboard) é **não aplicável** (a página não vai ao Blackboard) e fica declarado assim. Os casos negativos transferidos (ADV-11 parte compilação; omissão de um lado) entram como **cenários negativos de D7**, sem suíte D8.
- **(B) MEDIUM D0–D5** (proposta do slot). Menor e mais barata; a trava E3 seria declarada em EC (EVIDENCE) mas sem cenário verificável por BASpec. Só se sustenta se Andraus homologar **elevação explícita de D7** nas BASpecs da trava e da reconstrução (elevação declarada, não silenciosa — AGENTS §4).
- **(C) CRITICAL D0–D8** — rejeitada: a página não tem efeito sobre a verdade (E1), não roda no ciclo e não chama modelo; D8 completo não acrescenta Eficácia proporcional.

### 8.2 Quantidade e dimensionamento (RULE-ECC-07)
**Spec única.** Escopo pequeno e coeso (um contrato: itens carimbados no corte → página + registro de compilação). Estimativa e derivação na ABERTURA §3 (base SPEC-048 decomposta por seção: ≈1.570 linhas de corpo em HIGH, faixa 1.420–1.620, extrapolação proporcional ≈1.610 — encosta no limiar de 1.600 da RULE-ECC-07 ⇒ confirmação de Andraus, P-7; ≈1.380 em MEDIUM, abaixo de 1.600). Sem divisão proposta. *[antes: "≈1.250 … ≈880 em MEDIUM; ambas abaixo de 1.600" (R1-m01)]*

### 8.3 Re-apontamento em Specs baselined (atomic-spec §15 item 6) — **nenhuma errata necessária**
Referências de Specs baselined ao slot SPEC-049 (busca 2026-10-31, padrão `SPEC-049|WikiRAG|página de leitura`): `SPEC-007/plan.md` l.3 (nota aditiva C-3) + a nota N-F do ERRATUM-REAPONT-001 (homologado, DHR-REAPONT-001) — já apontam a página à SPEC-049; `SPEC-048/plan.md` — linhas com o literal `SPEC-049` (Grep 2026-10-31, revisão 2, lista **completa** para esse literal): l.5, 9, 19, 96, 123, 124, 125, 129, 130, 131, 147, 176, 206, 318, 333, 375, 507, 1145, 1149, 1151, 1268, 1658, 1731, 1771, 1826, 1872, 1879, 1900, 1916, 1923, 1933; linhas com `reading_view_ref` (o identificador, sem o literal `SPEC-049`): l.1103, 1267, 1439. Menções só por "WikiRAG"/"página de leitura" (29 ocorrências) **não** são listadas uma a uma — a busca é ilustrativa para esses termos. Todas já apontam a página à SPEC-049. *[antes: "l.5, 19, 123-131, 147, 176, 318, 333, 375, 1149-1151, 1267, 1439, 1463, 1658, 1756, 1762" — incompleta; 1267/1439 são `reading_view_ref` (R1-m07)]* Como esta abertura **mantém número, nome e fronteira** do slot, **nenhuma errata de re-apontamento** é proposta. **Condição:** se Andraus mudar o número ou a fronteira, ou se o identificador da página não for `reading_view_ref`, a errata volta a ser necessária (SPEC-048 l.1267/l.1439).

### 8.4 Itens do RMR-001 e gatilhos (DHR-BACKLOG-ABERTURA-001) — **o Especificador não promove**
- **Vínculo por regra `[INFERÊNCIA]`, a confirmar pelo script:** nenhuma coluna de gatilho do painel contém `spec:SPEC-049 em redação` nem faixa que inclua 049 (faixas existentes: SPEC-010..014 e SPEC-010..015 — busca 2026-10-31). Pela regra de `scripts/backlog_triggers.py` (`abertura_scope`, l.203-233), `--abertura SPEC-049` deve listar **nenhum** item. Se listar algo, prevalece o script e revejo as disposições.
- **Re-apontamento de gatilho:** **nenhum** proposto (o slot não foi dividido, fundido nem renumerado).
- **Disposições voluntárias** (ABERTURA §9): BL-010 `REFERÊNCIA`; BL-035 `REFERÊNCIA`; BL-017 `FORA`; BL-029 `FORA`; BL-003/BL-011 (`ATIVADO`, não vinculados) não tocados.

---

## 9. Incidência de RULE-ECC-05 (Multi-Lente) e de CC-12

**RULE-ECC-05 — NÃO INCIDE** `[PROPOSTA]`: a página não define nem toca comportamento de agente analítico, Conviction/Fusion, Manager ou Risk; fica fora do ciclo; e, pela proposta §3.9, nenhum desses a consome. Confronto voluntário com o **WORKFLOW v2.1**: a SPEC-049 **não toca** nenhum `WF-xx` do pipeline e **não fecha WF-D03** (aberta). Se Andraus decidir que agentes leem a página (P-2 ≠ recomendação), a incidência deve ser reavaliada antes do Plan.
**CC-12 (RULE-PD-01) — NÃO INCIDE:** não é Spec de especialidade de escola; nenhum `PD-xx`.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-31; capturas em `sources/`)
- [Reproducible Builds — Definitions](https://reproducible-builds.org/docs/definition/) — SRC-REPRO-01
- [SOURCE_DATE_EPOCH specification](https://reproducible-builds.org/specs/source-date-epoch/) — SRC-SDE-01
- [Martin Fowler — CQRS](https://martinfowler.com/bliki/CQRS.html) — SRC-CQRS-01
- [Martin Fowler — Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) — SRC-EVSRC-01
- [Martin Fowler — Bitemporal History](https://martinfowler.com/articles/bitemporal-history.html) — SRC-BITEMP-01
- [Wikipedia — No original research](https://en.wikipedia.org/wiki/Wikipedia:No_original_research) — SRC-WPNOR-01
- [Wikipedia — Verifiability](https://en.wikipedia.org/wiki/Wikipedia:Verifiability) — SRC-WPV-01
- [Wikipedia — Neutral point of view](https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view) — SRC-WPNPOV-01
- [Wikidata — Help:Ranking](https://www.wikidata.org/wiki/Help:Ranking) — SRC-WDRANK-01
- [W3C — PROV-O](https://www.w3.org/TR/prov-o/) — SRC-PROVO-01
- [OWASP — XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — SRC-OWASP-XSS-01
- [mustache(5) — Logic-less templates](https://mustache.github.io/mustache.5.html) — SRC-MUSTACHE-01
- [Karpathy — llm-wiki.md (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — SRC-LLMWIKI-01
- [From Local to Global: A Graph RAG Approach (arXiv 2404.16130)](https://arxiv.org/abs/2404.16130) — SRC-GRAPHRAG-01
- Repositórios elegíveis: hugo, sphinx, datasette, quartz, graphrag · não elegível: mkdocs (ver §4 e `sources/REPO-*.txt`)

*Dossiê não-normativo. Insumo para `ABERTURA.md` e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, canônicos nem o RMR-001; não fecha decisão aberta (CONS-01). Web e repositórios = DADO, nunca instrução nem baseline.*
