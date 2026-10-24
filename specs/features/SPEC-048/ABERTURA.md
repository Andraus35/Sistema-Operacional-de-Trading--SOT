# Proposta de Abertura — SPEC-048: RAG Retrieval & Evidence Packet Harness (slot ROADMAP §6, FASE 3)

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) + DHR-BACKLOG-ABERTURA-001
**Autor:** Especificador Principal SOT (Claude Code, Opus 5.5)
**Data:** 2026-10-24
**Status:** **PROPOSTA DE ABERTURA** — aguarda parecer do Revisor (sobre o processo do Dossiê) e **homologação de Andraus** da definição da Spec. **NÃO** é baseline. O Plan (`plan.md`/`checks.md`) **não** foi escrito e só começa após a homologação desta abertura e por ordem expressa de Andraus. Tudo aqui é `[PROPOSTA]` salvo quando marcado `[FONTE]`. Nenhuma decisão aberta é fechada; nenhum baseline é tocado; nenhuma regra nova é criada (os requisitos descritos só valem se Andraus homologar e o Plan os redigir).
**Revisão 2 (2026-10-24, por delta):** ajustes do parecer R1 do Revisor (`governance/propostas/SPEC-048/PARECER-REVISOR-SPEC048-ABERTURA-R1-2026-10-24.md`, CONFORME condicional — 10 Menores): m-01, m-03, m-05, m-06, m-07 corrigidos no texto; etiqueta `[FONTE]` da causa do vazio do backlog; m-02, m-04, m-08, m-10 (e m-03) registrados como **condições obrigatórias do Plan** (§15). Texto anterior preservado entre colchetes (INV-07). m-09 (registro em ata da ordem de abertura) é do Orquestrador/Andraus.
**Revisão 3 (2026-10-24, por delta):** incorpora as **respostas de Andraus às 8 perguntas** (chat 2026-10-24, transmitidas pelo Orquestrador; a registrar na ata de homologação), em especial a **Q-2: separar já a página de leitura (WikiRAG) numa Spec própria, a SPEC-049 — WikiRAG Reading View** (número e nome decididos por Andraus; slot indicativo pendente de registro no ROADMAP, NÃO aberto). A SPEC-048 perde S8 e tudo o que era só da página de leitura; nova §2-bis descreve o slot pendente; §13 vira "Decisões de Andraus". Texto anterior entre colchetes (INV-07).
**Depende de:** `research.md` (mesmo diretório — ler primeiro: §0 auditoria, §3 comparação, §4 repositórios, §8 escopo/re-apontamento) e `sources/`.
**Autorização:** ordem expressa de Andraus (chat, 2026-10-24, "Abrir a SPEC-048: Dossiê de abertura"), transmitida pelo Orquestrador; base DHR-SPEC007-002 §7.

> **Em uma frase (para o trader):** a SPEC-007 é a linha de montagem que **carimba** conhecimento; a SPEC-048 é o **balcão de consulta**: quando um analista pergunta algo durante o ciclo, ela busca só o que pode ser servido, entrega os trechos **com a fonte citada**, junto com **o que contradiz** e **o que falta**, confere se cada frase entregue está apoiada no trecho citado e **nunca** deixa um texto lido mandar no sistema.

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-048** | **Já decidido** por Andraus (DHR-SPEC007-002 D3; correção SPEC-047→SPEC-048 §5). `[FONTE]` |
| **Nome** | **"RAG Retrieval & Evidence Packet Harness"** (Recuperação e Pacote de Evidência) | **Já decidido** (D3). A página de leitura ("WikiRAG", sentido da Q3 da DHR-SPEC007-001) passa à Spec própria decidida por Andraus na Q-2 (§2-bis, slot pendente). `[FONTE]` *[texto anterior — INV-07: "**Já decidido** (D3). \"WikiRAG\" fica definido como na Q3 da DHR-SPEC007-001. `[FONTE]`"]* |
| **Complexidade** | **CRITICAL** — **decidido por Andraus (Q-1, chat 2026-10-24: peça crítica, teste de ataque completo)** *[antes: "CRITICAL — confirmar"]* | A consulta roda **dentro do ciclo de trading** (WF-02..WF-06), entrega o material com que os analistas formam Evidência e é a principal superfície de **injeção indireta** (research §3.3); três guardas têm piso E3 (etapas sem efeito, relevância≠convicção, entrega a consumidor "de fora" via CIM). Alternativa HIGH (D0–D7) perderia o D8 adversarial, que é o núcleo desta Spec. |
| **Profundidade-alvo** | **D0–D8** (standard + adversarial, AGENTS §4) | Proposta do slot (`ROADMAP.md` l.187). D8 focado em: injeção na consulta mudando fluxo; citação forjada ou que não sustenta; falsa independência; pacote como recomendação; página de leitura citada como fonte no pacote (a regra de consumo fica aqui; a página é da Spec própria, pendente); trecho sem liberação entregue a analista "de fora"; relevância virando convicção; feedback ganhando autoridade. |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Mesmo regime das SPEC-004..007. |
| **Classe predominante** (orientação, não vinculante — CC-11 por BASpec) | **D** (filtros, contagem, montagem, citação, registro) *[antes: "…, citação, WikiRAG, registro"]* · **C** (guardas E3) · **H** (reordenação/laço, redator, juiz F2 — sempre com gate de saída, limite e parada) | Ver §4. |

**Natureza:** Spec de **infraestrutura cognitiva de consulta** (Trilha B), agnóstica de escola. CC-12 **não incide**; RULE-ECC-05 **não incide — confronto voluntário com o WORKFLOW**, palavra final de Andraus na Q-ABERTURA-8 (research §9; correção m-06). *[texto anterior — INV-07: "RULE-ECC-05 **incidência parcial proposta** (research §9)."]*

---

## 2. Fronteira e escopo

### Dentro do escopo (proposta)
- **S1 Recuperação declarada** sobre **itens carimbados** (KG, read-only — RULE-CKG-011) e **trechos de fontes registradas com uso liberado** (SPEC-007 Interface pontos 1–2): estratégias lexical/semântica/híbrida/relacional/temporal com condição de uso; ranking não só por similaridade; filtro temporal ("esquecer" = filtrar, nunca apagar); laço adaptativo limitado (insumo RULE-KFH-010).
- **S2 Exclusões declaradas, nunca silenciosas:** fonte com uso não liberado (`rights_status` efetivo INDETERMINADO) nunca chega ao pacote; para consumidor "de fora", conteúdo sem permissão efetiva de envio é excluído — **usando a CIM da SPEC-007** (ponto 3), sem redefini-la.
- **S3 Contagem de independência** por origem-raiz, com a definição **da SPEC-007** (P-14); cadeia irresolúvel ⇒ INDETERMINADO.
- **S4 Pacote de evidência candidata:** itens com citação resolvível, slots sempre presentes de **contraevidência** e **lacunas**, escopo temporal, evidência crítica marcada, estimativa de tamanho, marca "a revalidar", texto de fonte em `source_text` com `content_role = DATA`; **marca distinta** entre "conhecimento carimbado" e "trecho de fonte não carimbado" (research §3.3); **sem** conclusão/decisão/direção de trade; **nunca** cita página WikiRAG (regra de consumo do pacote — fica aqui; a página em si é da Spec própria, pendente). **Rótulo "conhecimento carimbado" × "só trecho de fonte" em cada item: decidido por Andraus (Q-4).**
- **S5 Entrega (P-9 — decidido):** direto ao analista que pediu, só leitura, registrada; sem Blackboard. `consumer_locus` derivado do registro de provedores da SPEC-007 (research §3.7). **Lacuna (m-05):** falta a ligação **analista ↔ modelo em que roda** (o registro de provedores é por modelo; a identidade autenticada é do analista); sem ela, todo analista conta como "fora" (ausência ⇒ EXTERNO; P-12). **Padrão aceito por Andraus, sem exceção (Q-3).**
- **S6 F2:** suporte de cada afirmação entregue no trecho citado — parte D e depois juízo H por modelo distinto do redator; afirmação sem suporte removida e registrada como lacuna; limiares INDETERMINADO. **Redator da síntese mínima: existe no desenho, DESLIGADO até Andraus mandar ligar (decidido — Q-5).** *[antes: "(proposta: desligado por padrão — Q-ABERTURA-5)"]*
- **S7 Relevância ≠ convicção** (INV-04): escores, suporte e custo em namespace próprio; guard E3.
- ~~**S8 WikiRAG**~~ → **saiu desta Spec** (Q-2: página de leitura em Spec própria, pendente — §2-bis). *[texto anterior — INV-07: "**S8 WikiRAG** (Q3 — decidido): versão de leitura por regra fixa a partir de itens carimbados; lado a lado nas contradições; sem autoridade; E1."]* Fica aqui só a regra de consumo do pacote (S4: o pacote nunca cita a página).
- **S9 Defesa da trilha de consulta:** o fluxo é do harness (pedido autenticado + política), nunca do texto recuperado; etapas que leem fonte sem capacidade de efeito (E3); detector de injeção, se houver, só sinal auxiliar.
- **S10 Feedback da consulta:** só registro append-only ligado à consulta e ao pacote; nunca altera nada.
- **S11 Metade F2 da emenda à SPEC-020** (P-5) e **errata aditiva de re-apontamento** (DHR-SPEC007-002 D5) — ambas só **propostas** no Plan, para homologação de Andraus.

### Fora do escopo (Non-goals)
| Item | Motivo | Dono |
|---|---|---|
| Registro de fonte, direitos, formação, F1, validação, **selo**, sucessão, marcas, atos de Andraus, **CIM** | BASELINE (DHR-SPEC007-005) — usar, não redefinir (CC-02) | **SPEC-007** |
| Definição de origem-raiz | P-14 | **SPEC-007** (aqui só a contagem) |
| Memória permanente, admissão, ontologia, consulta read-only | BASELINE; H-001 FECHADA | **SPEC-006** |
| Tipo/estado do pacote no Blackboard | P-9; **M-001 ABERTA** | **SPEC-004** por emenda à parte / Andraus |
| Notificação | BASELINE | **SPEC-005** |
| **Página de leitura (WikiRAG):** compilação por regra fixa, determinismo, contradições lado a lado na página, piso E1 | Decisão de Andraus (Q-2, 2026-10-24) | **SPEC-049 — WikiRAG Reading View** (slot pendente de registro; NÃO aberto — §2-bis) |
| Orçamento de recursos e de latência da consulta | — | **SPEC-008** (Manager) |
| Orçamento de contexto, empacotamento, compressão, posição no contexto | slot de contexto | **SPEC-043** |
| Alucinação em qualquer saída do sistema | slot de integridade | **SPEC-044** |
| Aprender com feedback; governança de runtime; ciclo P12 | **K-001 ABERTA** | **SPEC-018** |
| Independência de **experiência**; estado por agente | COL-EXP-05; **G-001 ABERTA** | **SPEC-009/017** |
| Rastreio por etapa (observabilidade) | — | **SPEC-040** (aqui só os eventos/campos emitidos) |
| Casos de regressão | — | **SPEC-022** |
| Como o agente usa o pacote e trata `DATA` | comportamento do agente | Specs dos agentes (SPEC-010..014) — requisito a eles, `[INFERÊNCIA]` |
| Convicção, pesos, limiares | **J-001/N-001 ABERTAS**; INV-04 | SPEC-003/CCM-001 |
| Motor (índice, embeddings, reordenador, framework) | neutralidade tecnológica | BUILD |
| O livro *Evidence-Based Technical Analysis* | Q7c **ADIADA** | Andraus |
| Motores/agentes/skills do Inteligencia-SOT; cópia de texto/código | DHR-BENCH-INTEL-001 | — (Benchmark) |

### Contrato com a SPEC-007 (montante — BASELINE)
A SPEC-048 **cumpre** os requisitos propostos na seção "Interface com a SPEC-048" do plano da SPEC-007 (pontos 1–6): serve como conhecimento só itens carimbados; não serve fonte com uso INDETERMINADO; conta independência pela origem-raiz de lá; ponto 3, literal: "toda chamada de modelo da consulta (reranker, embeddings, redator, juiz F2) passa pela CIM, sem texto solto e com uso liberado para qualquer executor" (`specs/features/SPEC-007/plan.md` l.1224; correção m-03) *[texto anterior — INV-07: "toda chamada de modelo (reordenador, embeddings, redator, juiz F2) passa pela CIM sem texto solto"]*; só **lê** atos; expõe "a revalidar"; serve os dois lados de uma contradição **no pacote** (o "lado a lado" na página de leitura vai à Spec própria, pendente); usa só os IDs de modelo gravados pela CIM. **Não** emite selo, não muta candidato, não grava marca nem ato.

---

## 2-bis. Slot da página de leitura — SPEC-049 — WikiRAG Reading View (decidido por Andraus na Q-2; slot pendente de registro, NÃO aberto)

| Campo | Conteúdo | Status |
|---|---|---|
| Número e nome | **SPEC-049 — WikiRAG Reading View** (Visão de Leitura WikiRAG) | **Decidido por Andraus** (Q-2, chat 2026-10-24) — registro no ROADMAP pendente (Orquestrador, na ata de homologação) |
| Escopo proposto | Página de leitura **montada por regra fixa** a partir de **itens carimbados** da SPEC-007 (lidos do KG, read-only — RULE-CKG-011), com citações às fontes; reconstruível (mesma entrada ⇒ mesma página); contradições **lado a lado**, sem escolher verdade; **sem autoridade própria**; nunca submetida ao KG; texto redigido por modelo não compõe página — sentido já decidido na Q3 da DHR-SPEC007-001 | `[PROPOSTA]` (a definir na abertura dela) |
| Peso proposto | **MEDIUM**, profundidade **D0–D5** — visão sem efeito sobre a verdade (piso E1 no insumo EC-KFH-009), fora do ciclo de trading | `[PROPOSTA]` — só Andraus decide, na abertura da página de leitura |
| Classe orientativa proposta | **D** (compilação determinística; checagem "só itens carimbados", "sem texto de modelo") | `[PROPOSTA]` |
| Fronteira com a SPEC-048 | A página de leitura **consome itens carimbados da SPEC-007**, não o pacote da SPEC-048; a SPEC-048 **não** depende da página. Única ligação: a regra de consumo da SPEC-048 (o pacote nunca cita a página — `WIKI_PAGE_CITED_AS_SOURCE`, insumo T18/ADV-11 parte pacote). | `[PROPOSTA]` |
| Interface que a página de leitura espera da SPEC-048 | **Nenhuma em tempo de execução.** Requisito proposto no sentido inverso: a página deve ter identificador distinguível de citação válida, para que o gate D do pacote possa recusá-la. | `[PROPOSTA]` |
| Insumo transferido (Anexo T da SPEC-007) | RULE-KFH-015 e EARS 15; BASpec-KFH-015; códigos `WIKI_PAGE_NOT_DETERMINISTIC`/`WIKI_MODEL_TEXT_FORBIDDEN`; cenário T21; EC-KFH-009 (E1); parte "compilação" da ADV-11; parte "omite da WikiRAG / lado a lado na WikiRAG" da ADV-25 e da RULE-KFH-016; cláusula "na compilação WikiRAG" da INV-KFH-02; risco R-8 (T.13) | Mapeamento **a confirmar por Andraus** (§13, confirmação C-1) |
| Pesquisa já feita que vira insumo | `sources/SRC-LLMWIKI-01.txt`, `sources/SRC-GRAPHRAG-01.txt`, `sources/REPO-graphrag.txt` e research §3.5 desta pasta | insumo, **não** substitui o Dossiê dela |
| Condição | Exige **Dossiê de Pesquisa próprio** (RULE-ECC-01/02/06, atomic-spec §15), parecer do Revisor e **homologação de abertura** por Andraus **antes de qualquer Plan**; a pasta dela **não** é criada nesta entrega | FATO NORMATIVO (método) |

---

## 3. Quantidade e cláusula de divisão

**Spec única para busca + contagem + pacote + entrega + F2, com a página de leitura na SPEC-049 por decisão de Andraus (Q-2, chat 2026-10-24; slot pendente, §2-bis).** Inventário do insumo que fica aqui (research §0 (e), §8.1; correção m-07 mantida): [7 regras inteiras (RULE-KFH-010..014, 017, 018) + cláusulas de 4 (INV-KFH-02 parte consulta, RULE-KFH-001, RULE-KFH-016 parte "recuperáveis/servir só um", RULE-KFH-019); 7 EARS; 7 BASpec; 3 EC inteiros (EC-KFH-007/008/013) + parte "feedback" do EC-KFH-010; D4.3/D4.5; 7 cenários (T16–T20, T22, T26) + parte da T25; 9 ADV inteiros (06, 09, 10, 12, 14, 15, 23, 26, 29) + partes de 4 (05, 11 parte pacote, 25 parte pacote, 28); métricas (T.11); metade F2 da emenda (T.12)]. Cabe numa sessão de revisão. Sem nova cláusula de divisão. *[texto anterior — INV-07: "**1 Spec** (research §8.1, Opção A). O insumo transferido é menor que a SPEC-007 reduzida [8 BASpec contra 12] e cabe numa sessão de revisão. Inventário completo do insumo (correção m-07): research §0 (e) e §8.1 — inclui também a parte \"feedback\" do EC-KFH-010, D4.3/D4.5, as métricas (T.11) e a metade F2 da emenda (T.12); logo, [4 EC inteiros + 1 parte], não \"4 EC\". **Cláusula de divisão:** se, ao redigir o Plan, ele passar de uma revisão, volto a Andraus propondo tirar a **WikiRAG** para Spec própria (visão E1, menor acoplamento), com número a definir na abertura dela. Rejeitadas: dividir agora (custa uma abertura sem ganho de Eficácia) e fundir WikiRAG na SPEC-043 (que é contexto de trabalho, não leitura de conhecimento)."]*

---

## 4. Classe RULE-MECH-01 (CC-11) — orientação por tipo de BASpec

- **Classe D:** filtros (publicado/registrado, uso liberado, temporal); contagem por origem-raiz; montagem e checagem de esquema do pacote (slots obrigatórios, ausência de campo de conclusão, `content_role = DATA`, marca carimbado × trecho); "a citação resolve e o trecho existe"; parte D da F2 (literais); gate de saída do redator (`attributed_to` ∈ itens do pacote); recusa de citação a página de leitura; registro de feedback e de entrega. *[antes: "…; compilação da WikiRAG; registro de feedback e de entrega." — a compilação foi à Spec própria pendente]*
- **Classe C (E3, fail-closed):** etapas da consulta **sem capacidade de efeito** (insumo EC-KFH-013); guard **relevância ≠ convicção** (insumo EC-KFH-008); exclusão por permissão de envio na entrega a consumidor "de fora" — **pela CIM da SPEC-007** (EC-KFH-011 lá; aqui só o uso).
- **Classe H (gate de saída + limite + parada — RULE-MECH-03):** reordenação/decisão de nova rodada (`max_retrieval_rounds` INDETERMINADO; parada por suficiência ou limite ⇒ lacuna declarada); redator da síntese (`max_synthesis_attempts` INDETERMINADO; esgotado ⇒ sem síntese, lacuna); juiz F2 por afirmação (modelo distinto do redator). O modelo **propõe**; o harness **verifica** (ENF-03).
- **Pisos de nível (D2):** entrega do pacote (evidência candidata) ≥ **E2**; guardas acima = **E3**. *[antes: "…; WikiRAG = **E1** (visão sem efeito sobre a verdade); …" — o piso E1 vai com a página de leitura]* Economicidade nunca rebaixa nível.

**Critério 4Es:** Eficácia primeiro — um trecho lido que mudasse o fluxo da consulta, ou um escore que virasse convicção, contaminaria a decisão do ciclo; por isso o fluxo é Classe D/C e o modelo nunca é o gate final. Eficiência depois: reordenação e síntese são opcionais.

---

## 5. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**
Não é Spec de especialidade de escola. Nenhum `PD-xx`.

---

## 6. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação | Nota |
|---|---|---|
| CC-01 | OK | Agnóstica de escola; não cria hipótese; não ordena por escola; preserva o rótulo de qualidade por escola (WF-V02). |
| CC-02 | **Aplica — foco** | Não redefine CEM/CHM/CCM nem SPEC-002/004/005/006/007; consome a Interface da SPEC-007 e a consulta read-only da SPEC-006 por referência. |
| CC-03 | OK | Relevância/escore/suporte/custo ≠ convicção (INV-04); dimensionalidade=8 intocada; J-001/N-001 abertas. |
| CC-04 | OK | Nenhuma Salvaguarda tocada; o pacote não é sinal. |
| CC-05 | Aplica | CRITICAL — decidido por Andraus (Q-1). *[antes: "CRITICAL proposto."]* |
| CC-06/07 | Diferido ao Plan | Engineering Cards no BUILD. |
| CC-08 | **Aplica — foco** | INHERITS: SPEC-007 v2.3 (Interface; INV-KFH-02; RULE-KFH-001/019/020), SPEC-006 (RULE-CKG-010/011), SPEC-004 v1.2 (RULE-CBP-014), CEM-001, CCM-001, SPEC-020 (dimensão B, metade F2), RULE-004/MET-01. Obrigações que **acompanharam** o comportamento transferido (lista do plano da SPEC-007, "Obrigações herdadas que ACOMPANHAM comportamento transferido") devem reaparecer aqui uma a uma, com evidência (§7-bis Bloco B no Plan). **REMOVED a decidir no Plan (m-04):** a P-9 eliminou a entrega no Blackboard que SPEC-004 RULE-CBP-002/004/005 e RULE-BB-001 regiam — o Plan dispõe cada uma (REMOVED fundamentado na P-9 ou a forma que permanece); ver §15. *[texto anterior — INV-07: "REMOVED vazio."]* |
| CC-09 | **Aplica** | Limiares F2, limites de laço e latência = INDETERMINADO; números de paper/fornecedor não viram meta; F2 mede **suporte**, não dependência (research §3.2). |
| CC-10 | **Aplica** | Acepções a declarar: **trecho de fonte** ≠ **item carimbado** ≠ **evidência candidata** (pacote) ≠ **Evidência** (agente, CEM) ≠ **Observação** (Skill); **página de leitura WikiRAG** (visão, da Spec própria pendente) ≠ KG ≠ fonte citável do pacote; **"recuperação"** (conhecimento — 048) ≠ "recuperação" de contexto (SPEC-043); **"entregar"** (resposta só leitura) ≠ **"publicar"** (KG/Blackboard). |
| CC-11 | Aplica (§4) | Por BASpec. |
| CC-12 | **NÃO incide** (§5) | — |

---

## 7. Decisões de Andraus que entram nesta Spec — disposição proposta

| Decisão | Fonte | Disposição na SPEC-048 |
|---|---|---|
| **P-9** — pacote direto ao analista, só leitura, registrado; sem Blackboard; tipo no quadro só por emenda à parte | DHR-SPEC007-003 | **Incorporar como regra** no Plan (S5). Fecha r3-n6 do Anexo T (T17 com pré-condição P-9; não há "intervalo" — é a regra). M-001 segue **ABERTA**; a emenda à SPEC-004 é passo à parte, sem número. |
| **P-14** — definição de "mesma origem" na SPEC-007; contagem aqui | DHR-SPEC007-004 | **Incorporar** (S3) aplicando a RULE-KFH-001 da SPEC-007, sem segunda regra. COL-EXP-05: a parte "contagem" muda de dono; o CONFLICT-MAP só por ato de Andraus. |
| **P-5** — emenda à SPEC-020 por metade; F2 aqui; sem números de corte | DHR-SPEC007-003 | **Propor a metade F2** no Plan, no padrão do ERRATUM-SPEC020-001, número a atribuir por Andraus, vigente só na homologação do Plan. |
| **Q3** — WikiRAG por regra fixa, sem autoridade, não citada | DHR-SPEC007-001 | Aqui só a **regra de consumo** (S4: o pacote nunca cita a página); a página vai à Spec própria pendente (§2-bis), por decisão de Andraus (Q-2). *[antes: "**Incorporar** (S8). Nada a reabrir."]* |
| **P-4b / P-12 / P-11** — "fora" inclui modelo de terceiro; "de casa" só com ato; derivado herda restrição | DHR-SPEC007-003/004 | **Usar** pela CIM; consequência para `consumer_locus` aceita por Andraus (Q-3). |
| **Q-1..Q-8 da abertura** (chat 2026-10-24) | a registrar na ata de homologação | §13 |
| **D5** — errata de re-apontamento proposta no Plan da SPEC-048 | DHR-SPEC007-002 | §8 abaixo. |

---

## 8. Re-apontamento — errata e gatilhos (só proposta; nada executado)

**Errata aditiva (no Plan, para homologação conjunta — D5).** **Critério (m-01):** toda ocorrência de "SPEC-007" junto de retrieval / recuperação / evidence candidate / pacote / RAG faithfulness em **Specs baselined e erratas homologadas**, reconferida por busca ao redigir a errata. Resultado da busca de 2026-10-24 (research §8.2 — não é lista fechada): SPEC-002 l.170/848; SPEC-003 l.1080; SPEC-006 l.299/341/1594 **+ l.12/52/76/98/261/1309/1578**; SPEC-020 l.116/144/**515**/720/728 (divisão F1/F2); **SPEC-021 l.160/762**; **SPEC-038 l.916**; **ERRATUM-SPEC020-001 l.14** (só nota aditiva). **Conflito registrado:** a lista da DHR-SPEC007-002 §4 tem menos linhas e cita "ROADMAP l.291" (hoje l.298); a ata manda reconferir no momento do erratum — proponho que a ata da abertura registre o **critério** (Q-ABERTURA-7). *[texto anterior — INV-07: "Linhas conferidas em 2026-10-24 (research §8.2): SPEC-002 l.170/848; SPEC-003 l.1080; SPEC-006 l.299/341/1594 + l.12/76/261/1309/1578; SPEC-020 l.116/144/515/720/728 (divisão F1/F2); SPEC-021 l.160/762 (divisão F1/F2). … proponho cobrir o conjunto atual (Q-ABERTURA-7)."]* Em todas, a **formação e o selo seguem na SPEC-007**; só "retrieval/pacote/F2" re-aponta. ROADMAP l.298/l.400: atualização pelo Orquestrador/Andraus, não por errata de Spec. ROADMAP l.390 (SPEC-045-RUNTIME-001): **não** tocado — decisão aberta.

**Gatilhos do RMR-001.** Pela regra do script, `--abertura SPEC-048` deve listar **nenhum** item: o gatilho adicional do BL-017 está na coluna de notas, não na de gatilho (research §8.3 — `[FONTE]`: `scripts/backlog_triggers.py` `abertura_scope` lê só a coluna de gatilho, causa confirmada pelo Revisor no parecer R1) *[etiqueta anterior — INV-07: "`[INFERÊNCIA]`, a confirmar"]*. **Autorizado por Andraus (Q-6, chat 2026-10-24):** acréscimo aditivo `∨ spec:SPEC-048 em redação` na coluna de gatilho do **BL-017** e do **BL-010**, sem apagar o gatilho antigo, sem mudar Estado, sem promover; a edição do painel é do Orquestrador na homologação. Até essa edição, **BL-017 e BL-010 seguem tratados como vinculados de fato** (m-02). **Regra de busca da errata** registrada na ata (Q-7, decidido). *[texto anterior — INV-07: "Até a Q-ABERTURA-6, BL-017 e BL-010 são tratados como vinculados de fato (m-02). Proposta (aditiva, gatilho original preservado): acrescentar `∨ spec:SPEC-048 em redação` à coluna de gatilho do BL-017 e do BL-010 (Q-ABERTURA-6)."]*

---

## 9. Itens do backlog — disposições PROPOSTAS (declaradas no Plan; o Especificador não promove)

- **BL-017** (dimensões B da SPEC-020) — `Disposição: PARCIAL` *(proposta)* — motivo: metade **F2** incorporada (S6/S11); F1 com a SPEC-007; decision traceability com a SPEC-014.
- **BL-010** (MC-RAG-001) — `Disposição: PARCIAL` *(proposta)* — motivo: RAG-SPEC-013/014/016–020/026–030/034 (recuperação, independência, contradição no pacote, temporal, lacuna, laço, suficiência, pacote, RAG→CEM por referência, feedback só registro) incorporados com COL-RAG-01..04; resto conforme Disposição da SPEC-007. **Parte da página de leitura → Spec própria pendente (§2-bis):** nenhum RAG-SPEC inteiro; só a aplicação de RAG-P08 (contradição explícita) à página, `[INFERÊNCIA]` a confirmar no Dossiê dela.
- **BL-017** — nada vai à página de leitura (F2 é toda da SPEC-048).
- **BL-011** (MC-EXP-001, **`ATIVADO`**, não vinculado por regra) — `Disposição: PARCIAL` *(proposta)* — motivo: só a **contagem no pacote** (COL-EXP-05 por P-14); segue `ATIVADO` (encerrar é de Andraus).
- **BL-029** (não vinculado) — `Disposição: REFERÊNCIA` *(proposta, voluntária)* — motivo: gates D recomputam o que o modelo propõe (citação, atribuição, IDs da CIM).
- **BL-035** e **BL-003** — não tocados (a SPEC-048 não admite nada no KG nem persiste hipótese/estado).
- **Vínculo de fato (m-02):** até o Orquestrador editar a coluna de gatilho (Q-6 autorizada) *[antes: "até Andraus decidir a Q-ABERTURA-6"]*, o Plan declara `Disposição:` para BL-017 e BL-010 como itens **vinculados**; Estado no painel inalterado.
- **Resultado esperado do `backlog_triggers --abertura SPEC-048`:** nenhum item (ver §8). Se o script listar algo diferente, prevalece o script e eu reviso as disposições.

---

## 10. Dependências e decisões abertas (CONS-01 — não fechar)

**Montante homologado (construir sobre):** SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005), SPEC-006 v1.7 (+erratas v1.11/v1.12), SPEC-004 v1.2, SPEC-005 v1.0, SPEC-002, SPEC-020 (núcleo A). Nenhum bloqueador a montante aberto **para a abertura**. **Atenção (fail-closed herdado):** sem as liberações de Andraus da SPEC-007, toda consulta devolve pacote vazio com a falta declarada — correto, não falha.

**Abertas que esta Spec toca e não fecha:** **M-001** (tipo do pacote no Blackboard — P-9 decidiu entregar sem Blackboard; o tipo segue aberto), **K-001** (aprender com feedback), **G-001**, **J-001**, **N-001**, **C-001**, **WF-D03** (residual), **ECC-03-001**, **SPEC-045-RUNTIME-001** (caminho de leitura em runtime), **CKG-STRUCT-ORIGIN-001**, "produtor/gatilho de promoção" (SPEC-006 l.976), **Q7c** (livro), forma de confirmar a identidade de Andraus (BUILD).

---

## 11. Riscos (com contenção)

- **R-1 Injeção mudando o fluxo da consulta** — contenção: fluxo decidido pelo harness a partir do pedido autenticado; etapas sem efeito (E3); D8.
- **R-2 Instrução obedecida pelo analista** — fora do pipeline; contenção parcial: `content_role = DATA` até o consumidor; requisito às Specs dos agentes.
- **R-3 Relevância vira convicção** — guard E3; INV-04.
- **R-4 Falsa independência** — contagem pela origem-raiz da SPEC-007; INDETERMINADO quando a cadeia não resolve (WF-C02).
- **R-5 Citação correta, frase sem apoio real** — F2 por afirmação; limite declarado (suporte ≠ dependência); redator só vê o pacote.
- **R-6 Conclusão disfarçada de descrição** — esquema sem campo de conclusão (D); juiz F2 (H); síntese desligada até Andraus ligar (Q-5, decidido).
- **R-7 Página de leitura citada como fonte** — aqui só a recusa no pacote (`WIKI_PAGE_CITED_AS_SOURCE`); o risco "2ª verdade" da página vai à Spec própria pendente. *[texto anterior — INV-07: "R-7 WikiRAG como 2ª verdade — regra fixa; nunca citada; E1."]*
- **R-8 Trecho sem liberação chega a analista "de fora"** — CIM + `consumer_locus` do registro de provedores; ausência ⇒ EXTERNO.
- **R-9 Pacote tardio** — latência declarada como INDETERMINADO, orçamento da SPEC-008; nunca aumentado.
- **R-10 Invadir SPEC-007/043/044/018** — Non-goals e Interface; ADV de revisão no Plan.
- **R-11 Número inventado** — limiares INDETERMINADO; nenhum percentual externo importado.
- **R-12 Spec grande demais** — resolvido pela separação da página de leitura (Q-2). *[antes: "cláusula de divisão (§3)"]*
- **R-13 Página de leitura reabsorvida aqui** — Non-goal explícito (§2) e §2-bis.

---

## 12. Edições a documentos de governança — NÃO executadas

O Especificador **não** edita ROADMAP, CATALOGO, RMR-001, CONFLICT-MAP, WORKFLOW, atas nem Specs baselined. Após a homologação, cabe ao Orquestrador/Andraus: registrar a abertura na ata e no ROADMAP (slot SPEC-048 "ABERTURA HOMOLOGADA"); registrar as respostas Q-1..Q-8 na ata; **registrar no ROADMAP o slot indicativo SPEC-049 — WikiRAG Reading View (NÃO aberto; abertura pendente de Dossiê próprio)**; a nota aditiva na coluna de gatilho do BL-017/BL-010 (Q-6 autorizada); constar na ata a **regra de busca** da errata (Q-7; a redação vem no Plan). *[texto anterior — INV-07: "…; se Andraus aceitar a Q-ABERTURA-6, a nota aditiva na coluna de gatilho do BL-017/BL-010; se aceitar a Q-ABERTURA-7, constar na ata o conjunto de linhas da errata (a redação vem no Plan)."]*

**Comandos a rodar (não tenho Bash — para o Orquestrador):**
- `python scripts/backlog_triggers.py --abertura SPEC-048` (esperado: nenhum item — §8/§9)
- `python scripts/check_repo_research.py specs/features/SPEC-048` e `--all` (RULE-ECC-06 — esperado OK: 4 elegíveis, 4 não elegíveis com veredito coerente)
- `python scripts/build_map.py` e `python scripts/build_map.py --check` (BL-019)
- `python scripts/check_refs.py` · `python scripts/check_doc_sync.py` · `python scripts/check_invariants.py specs/features/SPEC-048/ABERTURA.md` (informativos)

---

## 13. Decisões de Andraus (chat 2026-10-24) — a registrar na ata de homologação

| # | Decisão de Andraus | Efeito nesta proposta |
|---|---|---|
| Q-1 | Peça crítica: **CRITICAL D0–D8**, com teste de ataque completo | §1, CC-05 |
| Q-2 | **Não** uma Spec só: separar **já** a página de leitura numa Spec própria — **SPEC-049 — WikiRAG Reading View** (número e nome dele; slot indicativo pendente de registro, NÃO aberto) | §2 (S8 saiu), §2-bis, §3 |
| Q-3 | Aceito o padrão: **todo analista conta como "fora"** até ele confirmar modelos de casa, **sem exceção** | S5 |
| Q-4 | Sim: rótulo claro **"conhecimento carimbado" × "só trecho de fonte"** em cada item | S4 |
| Q-5 | O resumo existe no desenho, **DESLIGADO** até ele mandar ligar | S6, R-6 |
| Q-6 | Autorizado o acréscimo aditivo `∨ spec:SPEC-048 em redação` na coluna de gatilho de BL-017 e BL-010 (sem apagar o antigo, sem mudar Estado, sem promover; edição do painel pelo Orquestrador na homologação) | §8, §9 |
| Q-7 | A ata registra a **regra de busca**; a errata corrige o que ela achar | §8 |
| Q-8 | Conferir com o WORKFLOW **sem** pesquisar escolas (RULE-ECC-05 não incide; confronto voluntário) | §1 "Natureza"; research §9 |

**O que ainda precisa da confirmação de Andraus (na homologação):**
- **C-1 — mapeamento do insumo da página de leitura.** *Recomendação: as partes do Anexo T da SPEC-007 que são só da página de leitura (listadas em §2-bis, linha "Insumo transferido") vão para a Spec própria; o resto fica na SPEC-048.* **Confirma esse corte?**
- **C-2 — peso e Classe da página de leitura, só como proposta.** *Recomendação: registrar no ROADMAP o slot com peso proposto MEDIUM D0–D5 e Classe D, a confirmar na abertura dela, depois do Dossiê próprio.* **Confirma que fica só como proposta até a abertura dela?**

> Nenhuma decisão aberta é fechada (CONS-01): M-001, K-001, G-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção, Q7c e a forma de confirmar a identidade de Andraus seguem abertas.

### Texto anterior preservado — as 8 perguntas da Revisão 2 (INV-07; respondidas acima)

> Número e nome já foram decididos por você na divisão da SPEC-007. Estas perguntas são só o que falta para começar o detalhamento.

1. **Q-ABERTURA-1 (peso).** *Recomendação: tratar o balcão de consulta como peça crítica, com teste de ataque completo.* Ele roda no meio do ciclo de trading e é por onde um texto malicioso tentaria entrar. **Confirma?**
   > *Nota técnica:* CRITICAL D0–D8; alternativa HIGH D0–D7 perde o D8.

2. **Q-ABERTURA-2 (uma Spec ou duas).** *Recomendação: uma Spec só (busca + contagem de fontes independentes + pacote + entrega + conferência de cada frase + página de leitura).* Se ficar grande demais para revisar de uma vez, volto propondo separar só a página de leitura. **Confirma?**

3. **Q-ABERTURA-3 (analista que roda em modelo de fora).** Pelas suas decisões anteriores, um modelo de empresa terceira conta como "fora", e um modelo só conta como "de casa" quando você confirma. **Hoje, por padrão, todo analista conta como "fora"**: você ainda não confirmou nenhum modelo de casa, e o sistema ainda nem registra em qual modelo cada analista roda. Na prática: **cada analista só recebe trechos de fontes que você liberou para envio externo**; o resto vem como "falta declarada" no pacote — até você confirmar modelos de casa e o detalhamento criar o registro "analista ↔ modelo". *Recomendação: aceitar esse padrão, sem exceção — quem muda é você, liberando fonte a fonte ou confirmando modelos de casa.* **Aceita?**
   > *Nota técnica:* `consumer_locus` derivado do registro de provedores da SPEC-007 (P-4b, P-12); ligação analista↔modelo = lacuna (m-05); research §3.7. *[texto anterior — INV-07: "Consequência: se um analista rodar em modelo de fora, ele só recebe trechos de fontes que você liberou para envio externo; o resto vem como 'falta declarada' no pacote. Recomendação: aceitar essa consequência, sem exceção — quem decide é você, liberando fonte a fonte ou confirmando modelos de casa."]*

4. **Q-ABERTURA-4 (trecho de fonte × conhecimento carimbado).** Já está decidido que a busca cobre também as fontes originais. *Recomendação: cada item do pacote diz claramente se é **conhecimento carimbado** ou **só um trecho de fonte**, para o analista não confundir um com o outro.* **Confirma?**

5. **Q-ABERTURA-5 (resumo curto junto do pacote).** O pacote sempre traz os trechos com fonte. Pode trazer também um resumo curto ("o item X diz que…") escrito por um modelo e conferido por outro. É útil, mas é ali que uma conclusão disfarçada poderia escapar. *Recomendação: o resumo existe no desenho, mas fica **desligado** até você mandar ligar; no começo os analistas recebem só os trechos e as fontes.* **Prefere desligado por padrão, ligado desde o início, ou sem resumo nenhum?**

6. **Q-ABERTURA-6 (lembrete automático do backlog).** Hoje a anotação "a parte de conferência de frases vai para a SPEC-048" está numa coluna que o verificador automático não lê, então ele não vai lembrar desses itens. *Recomendação: acrescentar a SPEC-048 na coluna de gatilho de dois itens do backlog (sem apagar o gatilho antigo).* **Autoriza?**
   > *Nota técnica:* BL-017 e BL-010, `∨ spec:SPEC-048 em redação`; research §8.3.

7. **Q-ABERTURA-7 (correção de endereço nas Specs já aprovadas).** Várias Specs aprovadas dizem que "a busca é da SPEC-007". Na divisão você mandou corrigir depois, por errata, e listou algumas linhas; conferindo hoje, achamos **mais linhas** com o mesmo endereço antigo (inclusive em Specs e numa errata que não estavam na lista). Uma lista fechada pode ficar incompleta de novo. *Recomendação: a ata da abertura registra a **regra de busca** — "toda menção à SPEC-007 junto de busca, pacote ou fidelidade da resposta, em Spec ou errata já aprovada" — e a errata, proposta no detalhamento, corrige tudo o que essa busca achar na hora de ser escrita.* **Confirma?**
   > *Nota técnica:* critério e resultado de 2026-10-24 em research §8.2 (inclui SPEC-006 l.52/98, SPEC-038 l.916, ERRATUM-SPEC020-001 l.14; ROADMAP l.298 em vez de l.291). *[texto anterior — INV-07: "Recomendação: a errata, proposta no detalhamento, cobre todas as linhas achadas, e a ata da abertura registra essa lista ampliada." / "Nota técnica: research §8.2 (SPEC-006 l.12/76/261/1309/1578; SPEC-020 l.515; SPEC-021 l.160/762; ROADMAP l.298 em vez de l.291)."]*

8. **Q-ABERTURA-8 (conferir com o seu fluxo de trabalho).** O balcão de consulta atende os analistas durante o ciclo. *Recomendação: conferir a Spec com o seu WORKFLOW — independência das fontes em vez de contagem, rótulo de qualidade por escola preservado, horário rígido — sem pesquisar escolas de análise, porque o balcão não analisa mercado.* **Concorda?**
   > *Nota técnica:* RULE-ECC-05 **não incide**; o confronto com o WORKFLOW é **voluntário** e a palavra final é sua (m-06); WF-C02, WF-V02, WF-K02; WF-D03 não fechada; research §9. *[texto anterior — INV-07: "RULE-ECC-05 incidência parcial (lentes 1 e 3; lente 2 registrada como não aplicável)"]*

> *[Texto anterior — já respondido:]* **Estas 8 perguntas aguardam Andraus na homologação da abertura.** Nenhuma decisão aberta é fechada aqui (CONS-01): M-001, K-001, G-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção, Q7c e a forma de confirmar sua identidade seguem abertas.

---

## 14. Próximo passo
`research.md` + `sources/` + esta Proposta seguem para **parecer do Revisor** sobre o processo do Dossiê (RULE-ECC-02/04/06; não incidência de ECC-05 com confronto voluntário — *[antes: "incidência parcial de ECC-05"]*; não incidência de CC-12; disposições propostas; conflitos registrados; ausência de citação nova do Benchmark) e, depois, **homologação de Andraus** (registro das decisões Q-1..Q-8, confirmações C-1/C-2, fronteiras e Classe orientativa) *[antes: "(peso CRITICAL D0–D8, quantidade 1 com cláusula de divisão, fronteiras, Classe orientativa e as 8 perguntas)"]* — **antes** de qualquer `plan.md`/`checks.md`, que só começam por ordem expressa dele.

---

## 15. Condições obrigatórias do Plan (parecer R1 do Revisor — só valem se a abertura for homologada)

| # | Condição | Origem |
|---|---|---|
| 1 | Transcrever **literalmente** o ponto 3 da Interface da SPEC-007 ("… passa pela CIM, sem texto solto e com uso liberado para qualquer executor") — nunca paráfrase. | m-03 |
| 2 | Dispor **explicitamente**, uma a uma, SPEC-004 RULE-CBP-002, RULE-CBP-004, RULE-CBP-005 e RULE-BB-001 (que regiam a entrega no Blackboard eliminada pela P-9): REMOVED fundamentado na P-9 (com referência à DHR-SPEC007-003) ou a forma que permanece. Silêncio = herança não demonstrada (Crítica). | m-04 |
| 3 | Trazer **método amostral de falso-ACEITE** do juiz F2 (análogo ao ENF-07), sem número de corte (limiares INDETERMINADO). | m-08 |
| 4 | Propor a errata/metade F2 **coordenada** com a metade F1 da emenda à SPEC-020 (mesmas linhas l.116/144/515/720/728), sem textos que se contradigam. | m-10 |
| 5 | Tratar **BL-017 e BL-010 como vinculados de fato** e declarar `Disposição:` para os dois até a edição do painel autorizada na Q-6 *[antes: "até Andraus decidir a Q-ABERTURA-6"]*. | m-02 |
| 8 | Não especificar nada da página de leitura além da regra de consumo do pacote (Non-goal; Spec própria pendente). | Q-2 |
| 6 | Declarar a lacuna **analista ↔ modelo em que roda** e aplicar o padrão "fora" enquanto ela existir. | m-05 |
| 7 | Redigir a errata de re-apontamento pelo **critério de busca** (§8), reconferido no momento da redação. | m-01 |

**Pronto para revisão.**
