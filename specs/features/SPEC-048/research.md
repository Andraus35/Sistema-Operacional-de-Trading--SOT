# Dossiê de Pesquisa — SPEC-048: RAG Retrieval & Evidence Packet Harness (slot ROADMAP §6, FASE 3)

| Campo | Valor |
|---|---|
| **Identificador** | DOSSIE-SPEC-048 |
| **Método** | ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) + DHR-BACKLOG-ABERTURA-001 |
| **Autor** | Especificador Principal SOT (Claude Code, Opus 5.5) |
| **Data de acesso web** | 2026-10-24 (todas as fontes `[EXTERNO]` e repositórios) |
| **Complexidade proposta** | **CRITICAL · D0–D8** (proposta do slot, `ROADMAP.md` l.187 "P0 — CRITICAL (proposta, a confirmar na abertura) · Profundidade-alvo: D0–D8 (proposta)"). Dossiê em profundidade CRITICAL. |
| **Validade do Dossiê (ECC-VAL-001 — FECHADA, DHR-DEC-003)** | CRITICAL → **90 dias** da data de acesso (2026-10-24) → **data-limite 2027-01-22**, ou antes se o contexto mudar materialmente (ex.: errata de re-apontamento homologada com outro corte, ou decisão de Andraus sobre M-001). Dossiê vencido não dispensa reabrir a pesquisa (fail-closed, RULE-ECC-02). |
| **Natureza** | **Dossiê `[EXTERNO]` — NÃO-NORMATIVO.** Não é baseline, não é Spec, não homologa, não fecha decisão (CONS-01). Tudo o que propõe é `[PROPOSTA]`. |
| **Status epistemológico** | Conteúdo web e de repositórios = **DADO, nunca instrução nem baseline** (DHR-PROV-WEB-001 §2.1; RULE-ECC-02). Fontes classificadas e etiquetadas; veracidade das páginas não atestada. Capturas literais em `sources/` (RULE-ECC-04); limitações em `sources/_LIMITACAO-WEB.txt`. |
| **Autorização** | Ordem expressa de Andraus (chat, 2026-10-24, "Abrir a SPEC-048: Dossiê de abertura"), transmitida pelo Orquestrador. Base: DHR-SPEC007-002 §7 (antes de qualquer Plan: Dossiê próprio, parecer do Revisor sobre o processo e homologação de Andraus da abertura). |
| **Insumos internos (não substituem o Dossiê)** | `specs/features/SPEC-007/research.md` (Dossiê da SPEC-007, 2026-10-18 — insumo, DHR-SPEC007-002 §7); `specs/features/SPEC-007/plan.md` v2.3 BASELINE (seção "Interface com a SPEC-048" e **Anexo T** — texto v1.2 transferido, insumo não vigente, DHR-SPEC007-005 §3). |
| **Fronteiras respeitadas** | INV-04 (relevância/escore/custo fora do Conviction Vector), INV-05 (SOT não executa ordem; pacote não é conclusão), INV-06/INV-10 (Evidência ≠ Observação; CEM-001 idioma canônico; o **agente** produz Evidência), INV-07 (nada é apagado), INV-09 (sem baseline informal). Não redefine CHM-001/CEM-001/CCM-001 nem SPEC-002/004/005/006/**007** (CC-02). |

> **Aviso de método (RULE-MET-01).** (1) Métricas de repositório vieram da página HTML pública; alertas de segurança = INDETERMINADO, registrados como 0 pelo critério das SPEC-006/007 (ver `_LIMITACAO-WEB.txt`). (2) A ferramenta de leitura web limita a citação literal a cerca de 125 caracteres — os trechos são literais (≥100 caracteres), às vezes recorte de frase maior, anotados como tal; trechos menores que 100 caracteres aparecem só como apoio. (3) O clone do Benchmark Inteligencia-SOT **não existe nesta sessão**: nenhuma leitura nova foi feita e **nenhuma citação `inteligencia-sot@…` é acrescentada** — o Dossiê só remete às linhas B1..B14 do Dossiê da SPEC-007 (§5). (4) Sem Bash: os gates (`check_repo_research`, `backlog_triggers --abertura`, `build_map`) são do Orquestrador (ABERTURA §11). Distingo **[FONTE]** (documento do SOT) de **[INFERÊNCIA]** e de **[EXTERNO]**.

---

## 0. Auditoria de entrada — o que é a SPEC-048 no SOT hoje

| Âncora | Verificação (lida em 2026-10-24) | Resultado |
|---|---|---|
| (a) Slot | `ROADMAP.md` l.186-189: "Recuperação sobre conhecimento carimbado e fontes originais; pacote de evidência com citação; visão de leitura WikiRAG por regra fixa; 2ª fidelidade (F2); defesa da trilha de consulta. Número, fronteira e quantidade são definidos na abertura (Dossiê + homologação de Andraus — RULE-ECC-01/02)." | `[FONTE]`, FATO ARQUITETURAL (slot indicativo, NÃO aberto). |
| (b) Origem do slot | DHR-SPEC007-002 D1–D5: divisão Opção C; **número e nome decididos (D3)**; fronteira §3 (tabela); re-apontamentos só **listados** §4; correção SPEC-047→SPEC-048 §5; condições §7. | **FATO NORMATIVO** (ata de Andraus). Número e nome **não** são reabertos aqui — a abertura confirma peso, fronteira fina e quantidade. |
| (c) Decisões de política já tomadas que caem aqui | DHR-SPEC007-003 **P-9** ("Direto ao analista que pediu, só leitura, registrada, sem ir ao quadro compartilhado; tipo no quadro só por emenda à parte (M-001 segue ABERTA)" — destino SPEC-048); **P-5** (emenda à SPEC-020 por metade; F2 → SPEC-048; sem números de corte até calibrar). DHR-SPEC007-004 **P-14** ("Definição de 'mesma origem' na SPEC-007; contagem no pacote na SPEC-048"). DHR-SPEC007-001 **Q3** (WikiRAG = versão de leitura por regra fixa, sem autoridade; o pacote não cita a página). | **FATO NORMATIVO** por ata (política); vira texto normativo só no Plan homologado. |
| (d) Montante já baselined | SPEC-007 v2.3 **HOMOLOGADA — BASELINE** (DHR-SPEC007-005): oferece itens carimbados, fontes/unidades com `rights_status`/permissão de envio efetivos e origem-raiz, a **CIM** (trava de envio, por `content_ref`), atos de Andraus, marcas, IDs de modelo — `specs/features/SPEC-007/plan.md` seção "Interface com a SPEC-048", pontos 1–6 (l.1216-1230). | **FATO NORMATIVO** (baseline). A SPEC-048 **usa** a trava e os atos; **não** os redefine (DHR-SPEC007-002 §3, última linha). |
| (e) Insumo herdado (não vigente) | Anexo T do plano da SPEC-007 (l.1948-2519): [RULE-KFH-010..015, 017, 018 + cláusulas transferidas de INV-KFH-02, RULE-KFH-001, 016 e 019 (T.1); EARS 10–15, 17, 18 (T.2); códigos de §D3.1 (T.3); BASpec 010–015, 017, 018 (T.4); D4.3 independência e D4.5 recuperação adaptativa (T.5); D6 "Consulta" (T.6); contratos `evidence_packet` e `feedback_record` (T.7); cenários T16–T22, T26 + parte de entrega da T25 (T.8); ADV-06, 09–12, 14, 15, 23, 26, 29 + partes de ADV-05/25/28 (T.9); EC-KFH-007/008/009/013 + **parte "feedback" do EC-KFH-010** (T.10); **métricas** F2, independência, lacuna por limite, log de entrega (T.11); **metade F2 da emenda à SPEC-020** (T.12); riscos R-3/R-4/R-8, Bloco B, etiquetagem e roteamento (T.13)] *[texto anterior — INV-07 (correção m-07): "[RULE-KFH-010..015, 017, 018; EARS 10–15, 17, 18; EC-KFH-007/008/009/013; cenários T16–T22, T26; ADV-06, 09–12, 14, 15, 23, 26, 29 + partes de ADV-05/25/28 (e parte de entrega da T25); contratos `evidence_packet` e `feedback_record`]"]*. Pendências listadas no próprio Anexo T (l.1952): R3-M5 parte entrega (`consumer_locus` sem âncora); r3-n6 (BBTYPE); F2; contagem por origem-raiz; errata de re-apontamento; requisitos de interface. | **Texto v1.2, insumo** — não é baseline, não vincula (DHR-SPEC007-005 §3). Os IDs `RULE-KFH-*` transferidos **não** foram reutilizados na SPEC-007; a numeração própria da SPEC-048 é do Plan dela. |
| (f) Fail-closed vigente a montante | DHR-SPEC007-005 §3: "a linha de montagem segue parada até a 1ª liberação real"; SPEC-007 `plan.md` l.394: "a etapa de consulta, quando existir, só poderá devolver pacote vazio com a falta declarada". | **FATO NORMATIVO.** Enquanto não houver itens carimbados nem fontes liberadas, toda consulta da SPEC-048 devolve **pacote vazio com lacuna declarada** — comportamento correto, não falha. |
| (g) Specs baselined que apontam "retrieval → SPEC-007" | Conferido por busca hoje: `SPEC-002/plan.md` l.170 e l.848; `SPEC-003/plan.md` l.1080; `SPEC-006/plan.md` l.299, l.341, l.1594 (as da ata) **e também** l.12, **l.52**, l.76, **l.98**, l.261, l.1309, l.1578; `SPEC-020/plan.md` l.116, l.144, l.515, l.720, l.728; `SPEC-021/plan.md` l.160, l.762; **`SPEC-038/plan.md` l.916**; **`governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md` l.14** ("RAG faithfulness ↔ SPEC-007"); `ROADMAP.md` l.298 (a ata citou "l.291" — linha deslocou) e l.400 (caminho crítico "007 RAG (fecha 020: RAG faithfulness)"). *[acréscimos em negrito — correção m-01 do parecer R1; SPEC-006 l.52/l.98 e SPEC-038 l.916 apontados pelo Revisor; ERRATUM l.14 conferido por mim]* | **Conflito registrado** (não resolvido): a lista da DHR-SPEC007-002 §4 é **menor** que o conjunto atual; a própria ata manda "reconferir no momento do erratum". Proposta em §8.2. |
| (h) Vizinhança de slots | `ROADMAP.md` l.377-378 (SPEC-043: "compressão; progressive disclosure; recuperação; … contexto contaminado"), l.380-381 (SPEC-044: "Afirmação sem fonte; conflito com fonte"), l.390 (SPEC-045-RUNTIME-001 cita "memória cognitiva (SPEC-004/006/007/009/017)"). | **Fronteiras a declarar**: "recuperação" aparece também no slot da SPEC-043 (recuperação de **contexto**, não de conhecimento); "afirmação sem fonte" na SPEC-044 (qualquer saída do sistema, não só o pacote). SPEC-045-RUNTIME-001 **aberta** — não decidida aqui. |
| (i) Fluxo operacional | `WORKFLOW.md` v2.1: consumidores do pacote são agentes das fases WF-02/WF-03/WF-05 e o Manager (WF-04/WF-06); WF-C02 "Confluência vale por independência dos sinais, não por contagem"; WF-V02 rótulo de qualidade de evidência por escola; WF-K02 controle rigoroso de horário. | Diferente da SPEC-007 (fora do ciclo), a **consulta roda dentro do ciclo de trading** → latência importa e a conformidade com o WORKFLOW é declarada (§9). |

**Conclusão.** A SPEC-048 é a **trilha de consulta**: dado um pedido autenticado de um analista (ou do Manager), buscar só o que pode ser servido (itens carimbados e trechos de fontes liberadas), contar independência pela origem-raiz definida na SPEC-007, montar o **pacote de evidência candidata** com citação resolvível, contraevidência e lacunas, conferir a fidelidade de cada frase entregue (F2), entregá-lo **direto ao analista, só leitura, registrado** (P-9) e manter a página WikiRAG como **visão de leitura sem autoridade**. Ela **não** forma nem carimba conhecimento (SPEC-007), **não** é o KG (SPEC-006), **não** gere janela de contexto (SPEC-043), **não** detecta alucinação em qualquer saída (SPEC-044), **não** aprende com feedback (SPEC-018) e **não** produz Evidência (o agente produz — CEM-001).

---

## 1. Questões e estratégia de busca

- **Q1.** Como o estado da arte torna a **citação** obrigatória e verificável na resposta de um RAG?
- **Q2.** Como medir a **fidelidade da frase entregue** (F2) — e qual o limite honesto dessa medida (citação correta ≠ fidelidade)?
- **Q3.** Que ameaças são próprias da **trilha de consulta** (injeção indireta, envenenamento do corpus) e que defesas são **por arquitetura** × **por detecção**?
- **Q4.** **Recuperação híbrida e reordenação**: quando valem, e o que não deve virar meta?
- **Q5.** "Wiki" de leitura **derivada** (resumos pré-compilados): o que adotar sem criar segunda verdade?
- **Q6.** Que **repositórios seguros e bem avaliados** (RULE-ECC-06) exemplificam essas práticas?
- **Q7.** O que muda, para o SOT, o fato de a consulta rodar **dentro do ciclo** (WORKFLOW, latência)?

**Estratégia:** WebFetch direto de fontes primárias conhecidas (arXiv, OWASP, Anthropic, documentação TruLens, gist de Karpathy) para capturar trechos literais; páginas públicas de repositórios e de commits para a régua. Sem envio de dado do projeto nas consultas. Termos e endereços usados (acesso 2026-10-24):
- arXiv (abstract): `2412.18004` (citação correta ≠ fiel), `2305.14627` (ALCE), `2112.12870` (AIS), `2305.14251` (FActScore), `2408.08067` (RAGChecker), `2505.04847` (fidelidade em RAG), `2302.12173` (injeção indireta), `2403.14720` (spotlighting), `2503.18813` (CaMeL), `2402.07867` (PoisonedRAG), `2104.08663` (BEIR), `2404.16130` (GraphRAG).
- Páginas: `genai.owasp.org/llmrisk/llm01-prompt-injection/`; `anthropic.com/news/contextual-retrieval`; `trulens.org/getting_started/core_concepts/rag_triad/`; `gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`.
- Repositórios (página + commits do `main`): `vibrantlabsai/ragas`, `deepset-ai/haystack`, `truera/trulens`, `microsoft/graphrag`, `stanford-futuredata/ColBERT`, `amazon-science/RAGChecker`, `protectai/llm-guard`, `meta-llama/PurpleLlama`.
- Leitura interna (somente leitura): ROADMAP, atomic-spec §15, DHR-SPEC007-001..005, plano da SPEC-007 (cabeçalho, Interface, Anexo T), pareceres da abertura da SPEC-007, RMR-001 (BL-010/011/017), `scripts/backlog_triggers.py` (regra de vínculo), `scripts/check_repo_research.py` (régua), WORKFLOW.md v2.1, CONFLICT-MAP (COL-RAG-04, COL-EXP-05), MC-RAG-001 (cabeçalhos RAG-SPEC-013..034).

---

## 2. Fontes classificadas `[EXTERNO]`

| ID (sources/) | Fonte | Classificação | Papel |
|---|---|---|---|
| SRC-ALCE-01 | arXiv 2305.14627 — texto com citações | Benchmark + Evidência | Q1 — citação como requisito verificável |
| SRC-AIS-01 | arXiv 2112.12870 — Attributable to Identified Sources | Padrão (de facto, de avaliação) + Prática | Q2 — "atribuível à fonte identificada" como definição de suporte |
| SRC-FACTSCORE-01 | arXiv 2305.14251 — FActScore | Benchmark + Prática | Q2 — unidade de verificação = afirmação atômica |
| SRC-RAGCHECKER-01 | arXiv 2408.08067 — RAGChecker | Benchmark + Evidência | Q2 — diagnóstico separado de recuperação e geração |
| SRC-TRULENS-TRIAD-01 | TruLens — documentação "RAG Triad" | Prática | Q2 — separar a resposta em afirmações e verificar cada uma |
| SRC-FAITHJUDGE-01 | arXiv 2505.04847 — fidelidade em RAG | Benchmark + Evidência | Q2 — contexto certo não garante frase fiel |
| SRC-WALLAT-01 | arXiv 2412.18004 — citação correta ≠ fidelidade | Evidência + Experimento | Q2 — limite honesto da F2 |
| SRC-GRESHAKE-01 | arXiv 2302.12173 — injeção indireta | Evidência + Experimento | Q3 — o recuperado é superfície de ataque |
| SRC-OWASP-LLM01-01 | OWASP LLM01:2025 Prompt Injection | Padrão (de facto) + Prática | Q3 — separar e marcar conteúdo externo |
| SRC-SPOTLIGHT-01 | arXiv 2403.14720 — spotlighting | Experimento + Prática | Q3 — marcação de proveniência (defesa probabilística) |
| SRC-CAMEL-01 | arXiv 2503.18813 — CaMeL | Experimento + Prática | Q3 — controle do fluxo pelo pedido confiável (defesa por projeto) |
| SRC-POISONEDRAG-01 | arXiv 2402.07867 — PoisonedRAG | Evidência + Experimento | Q3 — envenenamento do corpus |
| SRC-CTXRET-01 | Anthropic — Contextual Retrieval | Prática + Experimento (do fornecedor) | Q4 — híbrida + reordenação |
| SRC-BEIR-01 | arXiv 2104.08663 — BEIR | Benchmark + Evidência | Q4 — busca lexical como base robusta |
| SRC-GRAPHRAG-01 | arXiv 2404.16130 — GraphRAG | Experimento + Prática | Q5 — resumos pré-gerados por modelo (contraste) |
| SRC-LLMWIKI-01 | Karpathy — gist "llm-wiki.md" | Opinião + Prática emergente | Q5 — wiki compilado sobre fontes imutáveis (contraste) |
| REPO-ragas / REPO-haystack / REPO-trulens / REPO-graphrag | repositórios **elegíveis** (§4) | Prática | Q2/Q4/Q5/Q6 |
| REPO-ColBERT / REPO-RAGChecker / REPO-llm-guard / REPO-PurpleLlama | repositórios **NÃO ELEGÍVEIS** (§4) | — (registrados, não adotados) | transparência da régua |

Fontes internas de requisitos (não `[EXTERNO]`): MC-RAG-001 (BL-010, referência externa classificada — K-MAN-14) e o Anexo T do plano da SPEC-007 (insumo).

---

## 3. Comparação com a arquitetura SOT — adotar / adaptar / rejeitar / adiar

### 3.1 Citação obrigatória e resolvível (Q1) — **ADOTAR**
[EXTERNO, SRC-ALCE-01 — verbatim] *"our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability."* **Comparação SOT:** casa com CEM-001 (Lineage), SPEC-002 (proveniência) e com o insumo RULE-KFH-012 do Anexo T (citação `source_id@hash + span_locator` ou `published_item_ref@version`). **Adotar:** todo item do pacote cita algo que **resolve** — item carimbado (via `publication.seal_ref`, ponto 1 da Interface) ou trecho de fonte registrada (ponto 2). A checagem "a citação resolve e o trecho existe" é **Classe D** e roda antes de qualquer juízo por modelo. **Regra de consumo já decidida (Q3):** o pacote nunca cita a página WikiRAG.

### 3.2 Fidelidade F2 — frase entregue × trecho citado (Q2) — **ADAPTAR a definição; declarar o limite**
[EXTERNO, SRC-AIS-01 — verbatim] *"we present a new evaluation framework entitled Attributable to Identified Sources (AIS) for assessing the output of"*. [EXTERNO, SRC-FACTSCORE-01 — verbatim] *"breaks a generation into a series of atomic facts and computes the percentage of atomic facts supported by a reliable"*. [EXTERNO, SRC-TRULENS-TRIAD-01 — verbatim] *"To verify the groundedness of our application, we can separate the response into individual claims and independently search"*. [EXTERNO, SRC-RAGCHECKER-01 — verbatim] *"Meta evaluation verifies that RAGChecker has significantly better correlations with human judgments than other"*. [EXTERNO, SRC-FAITHJUDGE-01 — verbatim] *"yet large language models (LLMs) still frequently introduce unsupported information or contradictions"*.
**Comparação SOT:** o campo converge em (i) **atribuição** a uma fonte identificada, (ii) **afirmação atômica** como unidade e (iii) verificação de cada afirmação contra o contexto. Isso coincide com o insumo RULE-KFH-013 (F2 "incide sobre cada afirmação de `minimal_synthesis` … e, na falta dela, sobre a correspondência item↔citação") e com o método "D primeiro, H depois" já homologado para a F1 na SPEC-007. **Adaptar** `[PROPOSTA]`: F2 = cada afirmação entregue tem **suporte** no trecho que cita — parte D (citação resolve, trecho existe, números/sinais/negação literais) e parte H (juiz por afirmação, **modelo distinto do redator**, IDs gravados pela CIM). **Rejeitar** escores e percentuais como meta ou limiar: **limiares = INDETERMINADO** até calibração com amostra (CC-09; P-5). Que RAGChecker "verifica por afirmação" é `[INFERÊNCIA]` — o trecho capturado só sustenta a correlação com juízo humano e, no apoio, "diagnostic metrics for both the retrieval and generation modules" (recuperação ≠ geração).
**Limite honesto (RULE-MET-01).** [EXTERNO, SRC-WALLAT-01 — verbatim] *"Prior work largely evaluates citation correctness - whether cited documents support the corresponding statements."* — e, logo em seguida, "But citation correctness alone is insufficient." **Comparação SOT:** a F2 verifica **suporte** (o trecho sustenta a frase), **não** que o modelo "dependeu" do trecho ao escrever. `[PROPOSTA]` declarar isso no Plan e compensar por arquitetura: o redator da síntese só recebe os itens do próprio pacote (via CIM, por `content_ref`), e afirmação sem `attributed_to` válido é descartada por gate D (insumo RULE-KFH-018). O que sobra — "frase sustentada por acaso" — é risco residual localizado em **modelo/semântica** (RULE-UNC-01), sem número.
**Opção de economia com Eficácia primeiro** `[PROPOSTA]`: como a síntese é **acessória** (os itens com `source_text` sempre acompanham) e é onde mora o risco residual de "conclusão disfarçada de descrição" (Anexo T, RULE-KFH-012 "RISCO RESIDUAL"), propõe-se que o Plan a especifique como **opcional e desligada por padrão**, ligável só por ato de Andraus — Q-ABERTURA-5.

### 3.3 Defesa da trilha de consulta (Q3) — **ADOTAR controle pelo harness; ADAPTAR marcação; REJEITAR detector como gate**
[EXTERNO, SRC-GRESHAKE-01 — verbatim] *"using Indirect Prompt Injection, that enable adversaries to remotely (without a direct interface) exploit LLM-integrated"*. [EXTERNO, SRC-OWASP-LLM01-01 — verbatim] *"Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files."* e *"Segregate and identify external content Separate and clearly denote untrusted content to limit its influence on user prompts."* [EXTERNO, SRC-SPOTLIGHT-01 — verbatim] *"The key insight is to utilize transformations of an input to provide a reliable and continuous signal of its provenance."* [EXTERNO, SRC-CAMEL-01 — verbatim] *"explicitly extracts the control and data flows from the (trusted) query; therefore, the untrusted data retrieved by the LLM can never impact the program flow."* [EXTERNO, SRC-POISONEDRAG-01 — verbatim] *"an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM"*.
**Comparação SOT:**
- **Adotar (garantia por projeto):** o **fluxo** da consulta — estratégias, número de rodadas, filtros, o que entra no pacote e a quem é entregue — é decidido pelo harness a partir do **pedido autenticado** e da política, **nunca** pelo texto recuperado; reordenação, síntese e juízo F2 devolvem **dado** conferido por gate. Isso estende à consulta a garantia já homologada da SPEC-007 (INV-KFH-02: etapa que lê fonte não tem capacidade de efeito; único acesso a modelo pela CIM). Alcance honesto, como na SPEC-007 (R3-07): a garantia é "**instrução embutida não vira efeito**" — **não** "o pacote sai limpo".
- **Adaptar (camada auxiliar):** texto de fonte vai em `source_text` com `content_role = DATA`, separado dos campos de controle, até o consumidor (insumo RULE-KFH-012 "DADO, NUNCA INSTRUÇÃO"). A marcação **reduz** influência; é probabilística (SRC-SPOTLIGHT-01; números do paper não importados).
- **Rejeitar:** detector/classificador de injeção como **gate** (Detector ≠ Gate — ENF-03); no máximo sinal auxiliar registrado. Os repositórios desse tipo avaliados aqui ficaram NÃO ELEGÍVEIS (§4).
- **Envenenamento do corpus:** a recuperação só lê itens **carimbados** e trechos de fontes **registradas com uso liberado por Andraus** (pontos 1–2 da Interface; DHR-SPEC007-003 P-4a); a defesa na **entrada** do corpus é da SPEC-007 (registro, direitos, selo). `[PROPOSTA]`: cada item do pacote diz se é **conhecimento carimbado** ou **trecho de fonte não carimbado** — o analista não confunde os dois (Q-ABERTURA-4).
- **Resíduo fora do pipeline (já registrado no Anexo T, ADV-23):** o agente consumidor pode obedecer ao texto se não respeitar `DATA` — requisito às Specs dos agentes (SPEC-010..013), `[INFERÊNCIA]` de que hoje não está escrito.

### 3.4 Recuperação híbrida, reordenação e laço adaptativo (Q4) — **ADAPTAR como estratégias declaradas; números não viram meta**
[EXTERNO, SRC-CTXRET-01 — verbatim] *"Combining Contextual Embeddings and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 49%"*. [EXTERNO, SRC-BEIR-01 — verbatim] *"BM25 is a robust baseline and re-ranking and late-interaction-based models on average achieve the best zero-shot"*.
**Comparação SOT:** sustenta manter **lexical + semântica** como estratégias declaradas e a **reordenação** como etapa opcional com custo (insumo RULE-KFH-010 (a)/(b)). No domínio do SOT a busca lexical importa para termos exatos (ticker, nome de padrão, nível numérico) — `[INFERÊNCIA]`. **Adaptar** com condição de uso declarada; motor (índice, embeddings, reordenador) = BUILD; o percentual da Anthropic é do corpus dela (CC-09). Ranking não só por similaridade (independência e escopo temporal entram — MC-RAG-001 RAG-SPEC-017, l.492). O **laço adaptativo** (insumo RULE-KFH-010 (f)) segue Classe H com limite e parada; o recurso que vale o laço continua sendo o já registrado no Dossiê da SPEC-007 (§3.3, SRC-SELFRAG-01) — não recapturado aqui porque nada novo se apoia nele. Reordenador que roda em modelo passa pela CIM — ponto 3 da Interface, literal: "toda chamada de modelo da consulta (reranker, embeddings, redator, juiz F2) passa pela CIM, sem texto solto e com uso liberado para qualquer executor" (`specs/features/SPEC-007/plan.md` l.1224; correção m-03) — e só **reordena** — não adiciona, não remove por conta própria, não muda rodadas (§3.3).

### 3.5 "Wiki" de leitura derivada (Q5) — **REJEITAR resumo de modelo como fonte; manter a WikiRAG da Q3**
[EXTERNO, SRC-GRAPHRAG-01 — verbatim] *"graph from the source documents, then to pregenerate community summaries for all groups of closely related entities."* [EXTERNO, SRC-LLMWIKI-01 — verbatim] *"Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki"*.
**Comparação SOT:** o estado da arte pré-compila **resumos escritos por modelo** e os serve na consulta. No SOT isso seria **conhecimento formado sem selo** servido como fonte (SPEC-006 RULE-CKG-010 `FORMED_WITHOUT_SEAL`). **Rejeitar** como autoridade. **Já decidido por Andraus (DHR-SPEC007-001 Q3):** WikiRAG = versão de leitura montada **por regra fixa** a partir de itens carimbados, reconstruível, sem autoridade, nunca citada pelo pacote — insumo RULE-KFH-015 e EC-KFH-009 (E1). Nada a reabrir; o Dossiê só confirma que o padrão de mercado é o contrário e registra o porquê.

### 3.6 Independência por origem-raiz no pacote — **ADOTAR (FONTE interna; sem `[EXTERNO]` novo)**
`[FONTE]` RULE-004 (`RULES.md` l.36); RULE-MET-01 (l.705); COL-RAG-04 (`CONFLICT-MAP.md` l.142, CONFORME); WF-C02 ("Confluência vale por independência dos sinais, não por contagem"); DHR-SPEC007-004 P-14 (definição na SPEC-007, contagem aqui). **Comparação SOT:** a contagem aplica a definição **única** de origem-raiz da SPEC-007 (RULE-KFH-001) — cadeia irresolúvel ⇒ `INDETERMINADO`, nunca "independente" (insumo RULE-KFH-011, D4.3, T16, ADV-09). Sem segunda regra. COL-EXP-05: a parte "contagem no pacote" muda de dono para cá por P-14; o CONFLICT-MAP (l.147) segue apontando à SPEC-007 até ato de Andraus.

### 3.7 Entrega do pacote (P-9) — **ADOTAR a decisão de Andraus**
`[FONTE]` DHR-SPEC007-003 P-9. **Comparação SOT:** entrega como **resposta só-leitura** ao analista que pediu (identidade autenticada — SPEC-004 RULE-CBP-014, por referência), **registrada** no log da trilha; **não** publica no Blackboard; tipo no Blackboard só por emenda à SPEC-004 em passo à parte (M-001 **ABERTA**). Fecha a pendência r3-n6 do Anexo T: o cenário de entrega positivo (insumo T17) passa a ter a pré-condição P-9 explícita; não há "intervalo" — é a regra até nova decisão.
**`consumer_locus` (pendência R3-M5 parte entrega) — `[INFERÊNCIA]` + `[PROPOSTA]`:** pelas decisões já tomadas, entregar texto a um analista que roda em **modelo de terceiro** é enviar para "fora" (P-4b), e um modelo só conta como "de casa" com ato LOCAL_EXECUTOR de Andraus (P-12). Logo o `consumer_locus` deve vir do **registro de provedores da SPEC-007** (`provider_registry`, ausência ⇒ EXTERNO), não de registro novo nem do pedido — sem autoridade nova. **Consequência prática** (para Andraus, Q-ABERTURA-3): se os analistas rodarem em modelo de terceiro, trechos de fontes **sem liberação de envio** não chegam a eles — o pacote vem com a lacuna declarada.
**Lacuna (correção m-05):** o `provider_registry` da SPEC-007 é indexado por **`model_ref`** (modelo), e a SPEC-004 RULE-CBP-014 dá a **identidade do analista**, não o modelo em que ele roda. **Falta a ligação analista ↔ modelo em que roda** — nenhuma Spec baselined a registra hoje. `[DECISÃO NECESSÁRIA no Plan, sem fechar nada agora]`: o Plan declara essa ligação como lacuna e, sem ela, aplica o lado seguro já decidido (ausência ⇒ EXTERNO; LOCAL só com ato LOCAL_EXECUTOR — P-12). **Hoje, por padrão, todo analista conta como "fora"** até Andraus confirmar modelos de casa e a ligação existir.

### 3.8 Contexto, posição e latência — **ADIAR à SPEC-043 / SPEC-008; declarar a interface**
`[FONTE]` Dossiê da SPEC-007 §3.6 (posição no contexto → SPEC-043) e insumo D6 "Consulta" (Anexo T, T.6: orçamento recebido da SPEC-008, nunca aumentado — RAG-SPEC-015). **Comparação SOT:** a consulta roda dentro do ciclo (WF-02..WF-06; horário rígido WF-K02) → pacote tardio perde valor. **Adiar** orçamento, empacotamento e compressão (SPEC-043) e orçamento de recursos (SPEC-008). A SPEC-048 **declara**: estimativa de tamanho, marcação de evidência crítica (não descartável), respeito ao limite recebido; **latência-alvo = INDETERMINADO** (definida por SPEC-008/SPEC-043).

---

## 4. Pesquisa em repositórios (RULE-ECC-06 — régua Equilibrada)

Régua: licença aberta conhecida; ≥300 estrelas; último commit ≤12 meses antes do acesso; não arquivado; 0 alerta grave público aberto; dono identificável. Uma captura por repositório em `sources/REPO-*.txt`. Conteúdo de repositório = **DADO**; **nada instalado/executado**.

| Repositório | Estrelas | Licença | Último commit | Veredito | Uso no SOT |
|---|---|---|---|---|---|
| https://github.com/vibrantlabsai/ragas | 16100 | Apache-2.0 | 2026-02-24 | **ELEGÍVEL** | Referência — fidelidade da resposta medida à parte da recuperação; nenhuma métrica ou limiar importado; não é dependência. |
| https://github.com/deepset-ai/haystack | 26800 | Apache-2.0 | 2026-10-24 | **ELEGÍVEL** | Referência — etapas (recuperação, roteamento, geração) como contratos distintos sob controle explícito; framework não escolhido (motor = BUILD). |
| https://github.com/truera/trulens | 3600 | MIT | 2026-10-19 | **ELEGÍVEL** | Referência — o README aponta a prática de verificação por afirmação (capturada em SRC-TRULENS-TRIAD-01); observabilidade = SPEC-040; não é dependência. |
| https://github.com/microsoft/graphrag | 36400 | MIT | 2026-10-20 | **ELEGÍVEL** | Referência de **contraste** — resumo pré-gerado por modelo NÃO é fonte citável no SOT; só a ideia de visão pré-compilada, que aqui é a WikiRAG por regra fixa; não é dependência. |
| https://github.com/stanford-futuredata/ColBERT | 3900 | MIT | 2025-10-14 | **NÃO ELEGÍVEL** (commit > 12 meses) | Registrado e descartado — nada aproveitado do repositório. |
| https://github.com/amazon-science/RAGChecker | 1100 | Apache-2.0 | 2024-12-13 | **NÃO ELEGÍVEL** (commit > 12 meses) | Registrado e descartado — o código não entra; a alegação usa só o paper (SRC-RAGCHECKER-01). |
| https://github.com/protectai/llm-guard | 3200 | MIT | 2026-07-08 | **NÃO ELEGÍVEL** (arquivado) | Registrado e descartado — nada aproveitado; detector de injeção não seria gate de qualquer forma (ENF-03). |
| https://github.com/meta-llama/PurpleLlama | 4400 | mista | 2026-10-12 | **NÃO ELEGÍVEL** (licença não é aberta única) | Registrado e descartado — nada aproveitado; premissa de ameaça vem de fontes não-repositório. |

Resultado: **4 repositórios elegíveis** (referência; nenhum adotado como dependência); **4 não elegíveis** registrados. Comando a rodar pelo Orquestrador: `python scripts/check_repo_research.py specs/features/SPEC-048` e `--all`.

---

## 5. Benchmark Inteligencia-SOT (DHR-BENCH-INTEL-001) — sem leitura nova

**Política (de Andraus):** motores, agentes e skills do projeto paralelo **não** são usados; só ideias de controle, reescritas pelo SOT (DHR-BENCH-INTEL-001 D1–D6). **Nesta sessão o clone está ausente**: nada foi lido, nada reconferido, **nenhuma citação nova**. O que já está registrado no Dossiê da SPEC-007 (§5.2) e toca a trilha de consulta, **só por número de linha da tabela de lá**: B3 (duas traduções do mesmo bloco não são duas evidências; fonte com comando é texto — serve aqui à contagem por origem-raiz e à defesa da consulta), B8 (eixos de fidelidade como taxonomia **candidata**, a confrontar com SPEC-020/022/044 — serve à F2), B10 (conflito mostrado, não resolvido — serve a "servir os dois lados"). Nenhum texto/código copiado; licença: ver Dossiê da SPEC-007 (`NOTICE` sem licença de reutilização).

---

## 6. Cobertura × lacuna × dono

| Capacidade | Já coberto? | Tratamento proposto |
|---|---|---|
| Itens carimbados, fontes/unidades com direitos, origem-raiz, CIM, atos, marcas | **SIM** — SPEC-007 v2.3 (BASELINE) | **Consumir** pela Interface (pontos 1–6); não redefinir (CC-02) |
| Consulta read-only ao KG | **SIM** — SPEC-006 RULE-CKG-011 | Usar por referência |
| Identidade autenticada do consumidor | **SIM** — SPEC-004 RULE-CBP-014 | Usar por referência |
| Recuperação declarada, temporal, híbrida, limitada | **NÃO** | **Lacuna central** (insumo RULE-KFH-010) |
| Contagem de independência no pacote | **NÃO** (definição na SPEC-007) | **Lacuna central** (insumo RULE-KFH-011; P-14) |
| Pacote com citação, contraevidência, lacunas, `DATA`, sem conclusão | **NÃO** | **Lacuna central** (insumo RULE-KFH-012) |
| Entrega ao analista (P-9) e `consumer_locus` | **NÃO** | **Lacuna central** (§3.7) |
| F2 + metade F2 da emenda à SPEC-020 | **NÃO** (diferida — BL-017; P-5) | **Lacuna central** (insumo RULE-KFH-013/018) |
| Relevância ≠ convicção | princípio INV-04 | Guard E3 (insumo RULE-KFH-014, EC-KFH-008) |
| WikiRAG | **NÃO** (sentido decidido — Q3) | Visão D, E1 (insumo RULE-KFH-015, EC-KFH-009) |
| Feedback da consulta | **NÃO** | Só registro (insumo RULE-KFH-017); aprender = SPEC-018 (K-001 **ABERTA**) |
| Orçamento/empacotamento/compressão | **NÃO** | **SPEC-043** / **SPEC-008** (fora) |
| Alucinação em qualquer saída | **NÃO** | **SPEC-044** (fora) |
| Tipo do pacote no Blackboard | **NÃO** | Emenda à SPEC-004 em passo à parte (P-9); **M-001 ABERTA** |

**Invariantes de fronteira (reafirmados):** INV-04 (relevância/escore/custo nunca são convicção); INV-05 (pacote ≠ conclusão/decisão; RULE-DEC-01); INV-06/INV-10 (pacote = **evidência candidata**; o agente produz Evidência); INV-07 (feedback e logs append-only; nada apagado); CC-02.

---

## 7. MC-RAG-001 (BL-010) — parte que cabe à SPEC-048

Destino proposto (o restante segue como no Dossiê da SPEC-007 §7 e na Disposição da SPEC-007): RAG-SPEC-013 (estratégia, l.461), 014 (roteamento, l.474), 016 (decomposição de consulta, l.487), 017 (ranking, l.492), 018 (independência, l.497 — conforme RULE-004, COL-RAG-04), 019 (recuperação de contradição, l.502), 020 (temporal, l.507), 026 (lacuna, l.541), 027 (laço adaptativo, l.546), 028 (suficiência, l.551), 029 (montagem do pacote, l.556), 030 (RAG→CEM, l.565 — só por referência: pacote **projeta** evidência candidata, não redefine CEM), 034 (feedback, l.589 — só registro) → **SPEC-048**. Fora: 015 (recurso) → SPEC-008; 021–025 (contexto) → SPEC-043; 031 (RAG→KG) → SPEC-006/007; aprendizado → SPEC-018. G-gates rejeitados (COL-RAG-01), 4Es na ordem do SOT (COL-RAG-02), I-RAG/RAG-P locais (COL-RAG-03).

---

## 8. Escopo, quantidade, decomposição e re-apontamento

### 8.1 Opções
- **(A) Uma Spec — RECOMENDADA:** recuperação + contagem + pacote + entrega (P-9) + F2 (com redator opcional) + relevância≠convicção + WikiRAG + feedback (registro) + defesa da consulta. Tamanho do insumo transferido: [8 regras inteiras + cláusulas de 4, 8 EARS, 8 BASpec, 4 EC inteiros + parte "feedback" do EC-KFH-010, D4.3/D4.5, 8 cenários + parte da T25, 10 ADV inteiros + partes de 3 (ADV-05, ADV-25, ADV-28), métricas (T.11), metade F2 da emenda (T.12)] *[texto anterior — INV-07 (correção m-07): "[8 regras, 8 EARS, 8 BASpec, 4 EC, 8 cenários, 10 ADV inteiros + partes de 3 (ADV-05, ADV-25, ADV-28)]"]* — menor que a SPEC-007 reduzida [12 BASpec]. Cabe numa sessão de revisão. **Cláusula de divisão:** se o Plan passar de uma revisão, a **WikiRAG** sai para Spec própria (menor acoplamento: visão E1, sem efeito sobre a verdade).
- **(B) Duas Specs agora** (consulta+pacote | WikiRAG) — rejeitada por ora: WikiRAG é pequena e já decidida (Q3); dividir agora custa mais uma abertura sem ganho de Eficácia.
- **(C) Fundir a WikiRAG na SPEC-043** — rejeitada: SPEC-043 é contexto de trabalho, não visão de leitura de conhecimento.

### 8.2 Re-apontamento em Specs baselined (atomic-spec §15 item 6) — **só proposto; errata no Plan (DHR-SPEC007-002 D5)**
Conjunto a cobrir pela **errata aditiva** (padrão ERRATUM-SPEC019-001 / ERRATUM-SPEC020-001; nenhum baseline editado agora — INV-09), linhas conferidas em 2026-10-24:
- **SPEC-002** `plan.md` l.170, l.848 — "evidence candidate a partir de retrieval → SPEC-007" → SPEC-048.
- **SPEC-003** `plan.md` l.1080 — idem.
- **Critério de busca (vinculante para a errata — correção m-01):** toda ocorrência de **"SPEC-007" junto de retrieval / recuperação / evidence candidate / pacote / RAG faithfulness** em **Specs baselined e erratas homologadas**, reconferida por busca no momento de redigir a errata. A lista abaixo é o **resultado da busca em 2026-10-24**, não uma lista fechada; o que a busca achar a mais entra pelo critério. *[texto anterior — INV-07: sem critério; só a lista]*
- **SPEC-006** `plan.md` l.299, l.341, l.1594 (lista da ata) **+ l.12, l.52, l.76, l.98, l.261, l.1309, l.1578** (mencionam "retrieval/recuperação → SPEC-007"; l.52 e l.98 apontadas pelo Revisor, m-01) — nessas linhas a **formação** segue na SPEC-007; só a parte "retrieval" re-aponta. *[texto anterior — INV-07: "+ l.12, l.76, l.261, l.1309, l.1578 (achadas hoje; …)"]*
- **SPEC-020** `plan.md` l.116, l.144, l.515, l.720, l.728 — "RAG faithfulness → SPEC-007" vira "F1 → SPEC-007; F2 → SPEC-048" (P-5).
- **SPEC-021** `plan.md` l.160, l.762 — mesma divisão (achado A-12 do 1º parecer da abertura da SPEC-007; não está na lista da ata).
- **SPEC-038** `plan.md` l.916 — mesma divisão (apontada pelo Revisor, m-01).
- **ERRATUM-SPEC020-001** (`governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md` l.14: "RAG faithfulness ↔ SPEC-007 … permanecem DIFERIDAS") — mesma divisão; a errata da SPEC-048 só **acrescenta** nota, sem editar a errata homologada (INV-09).
- **Coordenação obrigatória (m-10):** a metade F1 da emenda à SPEC-020 (proposta no plano da SPEC-007, passo à parte — DHR-SPEC007-005 H-3) e a errata/metade F2 da SPEC-048 tocam **as mesmas linhas** da SPEC-020 (l.116/144/515/720/728); o Plan da SPEC-048 deve propor texto **coordenado** com a metade F1 (um só texto final por linha, ou duas notas aditivas que não se contradizem), para homologação de Andraus.
- **ROADMAP.md** l.298 (dimensão B — a ata citou l.291) e l.400 (caminho crítico) — edição do ROADMAP é de Andraus/Orquestrador, não errata de Spec.
- **Não incluído (decisão aberta):** ROADMAP l.390 (SPEC-045-RUNTIME-001 lista "SPEC-004/006/007/009/017" como memória cognitiva) — a decisão segue **ABERTA**; só registrar que a SPEC-048 é caminho de leitura e deixar para a SPEC-045.

### 8.3 Itens do RMR-001 e gatilhos (DHR-BACKLOG-ABERTURA-001) — **o Especificador não promove**
- **Achado `[FONTE]` (causa confirmada pelo Revisor no parecer R1 — `scripts/backlog_triggers.py` `abertura_scope` lê só a coluna de gatilho; o resultado do comando segue a rodar pelo Orquestrador)** *[etiqueta anterior — INV-07: "Achado `[INFERÊNCIA]` (a confirmar pelo Orquestrador)"]*: pela regra do script (`scripts/backlog_triggers.py`, função `abertura_scope`, l.203-233, que lê **só a coluna de gatilho** do painel), `--abertura SPEC-048` deve listar **nenhum** item: o "gatilho adicional `spec:SPEC-048 em redação`" do BL-017 foi registrado na **coluna de notas**, não na coluna de gatilho (`backlog/RMR-001_Painel_Backlog.md` l.124). Conflito registrado, não resolvido.
- **Proposta de re-apontamento (aditivo, ato de Andraus/Orquestrador):** acrescentar `∨ spec:SPEC-048 em redação` à **coluna de gatilho** do **BL-017** (parte F2) e do **BL-010** (parte recuperação/pacote), preservando o gatilho original (INV-07) — Q-ABERTURA-6.
- **Vínculo de fato (m-02):** até Andraus decidir a Q-ABERTURA-6, **BL-017 e BL-010 são tratados como vinculados à SPEC-048 de fato** — o Plan declara `Disposição:` para os dois como se o vínculo por regra existisse; o Estado no painel não muda.
- **Disposições propostas** (a declarar no Plan, `[STRUCT-13]`; vínculo por regra ou, se a regra não vincular, declaração voluntária): **BL-017** `Disposição: PARCIAL` — metade F2 aqui; F1 na SPEC-007; decision traceability na SPEC-014. **BL-010** `Disposição: PARCIAL` — RAG-SPEC listados em §7. **BL-011** (`ATIVADO`, não vinculado) `Disposição: PARCIAL` — só a contagem no pacote (COL-EXP-05 por P-14); segue `ATIVADO`. **BL-029** (não vinculado) `Disposição: REFERÊNCIA` — gates D recomputam o que o modelo propõe (citação, atribuição). **BL-035** — não tocado (a SPEC-048 não admite nada no KG).

---

## 9. Incidência de RULE-ECC-05 (Multi-Lente) e de CC-12

**RULE-ECC-05 — NÃO INCIDE; confronto VOLUNTÁRIO com o WORKFLOW** `[PROPOSTA — palavra final de Andraus na Q-ABERTURA-8]` (correção m-06: "incidência parcial" não é categoria da regra). *[texto anterior — INV-07: "RULE-ECC-05 — incidência PARCIAL proposta `[PROPOSTA — a confirmar pelo Revisor e por Andraus]`." e "Proposta: (1) Arquitetura — feita (§3, §6); (2) Escola — não aplicável …; (3) WORKFLOW v2.1 — conformidade declarada por ID:"]* A SPEC-048 **serve** agentes analíticos e o Manager **dentro do ciclo**, mas não define o comportamento deles. Por prudência, sem que a regra o exija: o pipeline é agnóstico de escola e não cria hipótese; **não apaga** o rótulo de qualidade por escola que o agente usa (WF-V02) e não ordena itens por escola; e o confronto voluntário com o **WORKFLOW v2.1** é declarado por ID: WF-02/WF-03/WF-05 (consumidores), WF-04/WF-06 (Manager), **WF-C02** (independência, não contagem — a contagem por origem-raiz o realiza), **WF-V02** (rótulo preservado), **WF-K02** (horário rígido → latência declarada, valor INDETERMINADO); **não contradiz** nenhum `WF-xx`; **não fecha WF-D03** (aberta).
**CC-12 (RULE-PD-01) — NÃO INCIDE:** não é Spec de especialidade; nenhum `PD-xx`.

---

## 10. Lacunas, conflitos e INDETERMINADOS (RULE-MET-01)

1. **Lista de re-apontamento da ata × conjunto atual** (§0 g, §8.2) — conflito registrado; errata a propor no Plan.
2. **Vínculo do backlog por regra provavelmente vazio** (§8.3) — conflito registrado; proposta Q-ABERTURA-6.
3. **`consumer_locus`** — derivação proposta do registro de provedores da SPEC-007 (§3.7) é `[INFERÊNCIA]` das decisões P-4b/P-12; consequência prática a confirmar (Q-ABERTURA-3). **Lacuna (m-05):** falta a ligação **analista ↔ modelo em que roda** (o registro de provedores é por modelo; RULE-CBP-014 dá só a identidade do analista); até existir, todo analista conta como "fora".
3-bis. **Herança do Blackboard após a P-9 (m-04)** — SPEC-004 RULE-CBP-002/004/005 e RULE-BB-001 regiam a entrega no Blackboard que a P-9 eliminou; o Plan **deve** dispor cada uma explicitamente (REMOVED fundamentado na P-9 com referência à ata, ou a forma que permanece — ex.: identidade autenticada e registro). Silêncio = herança não demonstrada (achado Crítico pelo Revisor).
3-ter. **Falso-ACEITE do juiz F2 (m-08)** — com limiares INDETERMINADO, um juiz que aprovasse tudo não seria percebido; o Plan **deve** trazer método amostral de falso-ACEITE (análogo ao ENF-07), sem número de corte.
4. **F2 mede suporte, não dependência** (§3.2) — limite declarado; risco residual em modelo/semântica (RULE-UNC-01).
5. **Síntese do redator** — opcional e desligada por padrão é `[PROPOSTA]` (Q-ABERTURA-5).
6. **Tipo do pacote no Blackboard** — emenda à SPEC-004 em passo à parte; **M-001 ABERTA**.
7. **Limiares de F2, `max_retrieval_rounds`, `max_synthesis_attempts`, latência-alvo** = **INDETERMINADO** até calibração/SPEC-008/SPEC-043 (CC-09).
8. **Obrigação do agente de tratar `DATA` como dado** — requisito às Specs dos agentes; `[INFERÊNCIA]` de que hoje não está escrito.
9. **Fronteira com SPEC-043/044** — "recuperação de contexto" (043) ≠ recuperação de conhecimento (048); "afirmação sem fonte em qualquer saída" (044) ≠ F2 do pacote (048).
10. **Repositórios:** alertas de segurança = INDETERMINADO (registrados como 0); limite da ferramenta (`_LIMITACAO-WEB.txt`).
11. **Benchmark** sem reconferência nesta sessão (§5).

**Permanecem abertas (CONS-01):** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03 (residual), ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001 (BL-035), "produtor/gatilho de promoção" (SPEC-006 `plan.md` l.976), direito de uso do livro (Q7c), forma de confirmar a identidade de Andraus (BUILD). Este Dossiê não fecha nenhuma.

---

## Sources (fontes `[EXTERNO]` — acesso 2026-10-24; capturas em `sources/`)
- [Enabling Large Language Models to Generate Text with Citations (arXiv 2305.14627)](https://arxiv.org/abs/2305.14627) — SRC-ALCE-01
- [Measuring Attribution in Natural Language Generation Models (arXiv 2112.12870)](https://arxiv.org/abs/2112.12870) — SRC-AIS-01
- [FActScore (arXiv 2305.14251)](https://arxiv.org/abs/2305.14251) — SRC-FACTSCORE-01
- [RAGChecker (arXiv 2408.08067)](https://arxiv.org/abs/2408.08067) — SRC-RAGCHECKER-01
- [TruLens — RAG Triad](https://www.trulens.org/getting_started/core_concepts/rag_triad/) — SRC-TRULENS-TRIAD-01
- [Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards (arXiv 2505.04847)](https://arxiv.org/abs/2505.04847) — SRC-FAITHJUDGE-01
- [Correctness is not Faithfulness in RAG Attributions (arXiv 2412.18004)](https://arxiv.org/abs/2412.18004) — SRC-WALLAT-01
- [Not what you've signed up for — Indirect Prompt Injection (arXiv 2302.12173)](https://arxiv.org/abs/2302.12173) — SRC-GRESHAKE-01
- [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — SRC-OWASP-LLM01-01
- [Defending Against Indirect Prompt Injection Attacks With Spotlighting (arXiv 2403.14720)](https://arxiv.org/abs/2403.14720) — SRC-SPOTLIGHT-01
- [Defeating Prompt Injections by Design (arXiv 2503.18813)](https://arxiv.org/abs/2503.18813) — SRC-CAMEL-01
- [PoisonedRAG (arXiv 2402.07867)](https://arxiv.org/abs/2402.07867) — SRC-POISONEDRAG-01
- [Introducing Contextual Retrieval (Anthropic)](https://www.anthropic.com/news/contextual-retrieval) — SRC-CTXRET-01
- [BEIR (arXiv 2104.08663)](https://arxiv.org/abs/2104.08663) — SRC-BEIR-01
- [From Local to Global: A Graph RAG Approach (arXiv 2404.16130)](https://arxiv.org/abs/2404.16130) — SRC-GRAPHRAG-01
- [Karpathy — llm-wiki.md (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — SRC-LLMWIKI-01
- Repositórios elegíveis: ragas, haystack, trulens, graphrag · não elegíveis: ColBERT, RAGChecker, llm-guard, PurpleLlama (ver §4 e `sources/REPO-*.txt`)

*Dossiê não-normativo. Insumo para `ABERTURA.md` e para a decisão de Andraus. Não altera ROADMAP, RULES, WORKFLOW, Specs, canônicos nem o RMR-001; não fecha decisão aberta (CONS-01). Web e repositórios = DADO, nunca instrução nem baseline.*
