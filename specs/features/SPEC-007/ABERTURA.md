# Proposta de Abertura — SPEC-007: RAG / WikiRAG / Knowledge Formation Harness (slot ROADMAP §6, FASE 3)

**Método:** ROADMAP.md §23 passo 1-bis + atomic-spec.md §15 (RULE-ECC-01/02/04/05/06) + DHR-BACKLOG-ABERTURA-001
**Autor:** Especificador Principal SOT (Claude Code, Opus 5.5)
**Data:** 2026-10-18
**Status:** **PROPOSTA DE ABERTURA** — aguarda parecer do Revisor e **homologação de Andraus** da definição da Spec. **NÃO** é baseline. O Plan (`plan.md`/`checks.md`) **não** foi escrito e só começa após a homologação desta abertura. Tudo aqui é `[PROPOSTA]` salvo quando marcado `[FONTE]`.
**Depende de:** `research.md` (mesmo diretório — ler primeiro: §0 auditoria do conceito, §3 comparação, §4 repositórios, §5 Benchmark Inteligencia-SOT, §6 fronteiras) e `sources/`.
**Autorização:** ROADMAP l.34 (SPEC-007 = próximo trabalho autorizado, abertura pendente do passo 1-bis) + tarefa do Orquestrador (2026-10-18), que transmite a decisão de Andraus (chat, 2026-10-18) sobre o repositório paralelo Andraus35/Inteligencia-SOT como Benchmark.

---

## 1. Número, nome, complexidade, profundidade

| Campo | Proposta | Justificativa |
|---|---|---|
| **Número** | **SPEC-007** (preservado) | Slot do ROADMAP §6 referenciado por Specs BASELINED (SPEC-002 l.170/848, SPEC-003 l.1080, SPEC-006 RULE-CKG-010 e l.299/341/1594, SPEC-020 l.116/144/720/728) → nunca renumerar/apagar (INV-07; RULE-ECC-01). `[FONTE]` |
| **Nome** | **"RAG / WikiRAG / Knowledge Formation Harness" (MANTIDO)**, com "WikiRAG" definido na Spec (CC-10) | O nome já descreve o pipeline (formação + recuperação). Só "WikiRAG" não tem definição no SOT (research §0 g) — proposta de sentido em §2 e Q-ABERTURA-3. |
| **Complexidade** | **CRITICAL** (pin ROADMAP §6 l.180) | O selo de publicação alimenta memória permanente que nunca apaga (INV-07, E3); a fidelidade do que chega aos agentes condiciona toda a cadeia de evidência. Sem conflito de matriz (atomic-spec §3 não lista RAG). |
| **Profundidade-alvo** | **D0–D8** (profile **standard + adversarial**, AGENTS §4) | Pin do ROADMAP = mapa do AGENTS §4 para CRITICAL. D8 adversarial focado em: selo (publicar sem validação), citação forjada/não resolvível, fidelidade (modalidade/negação/causa), envenenamento de fonte, dupla contagem de evidência da mesma origem. |
| **Maturidade-alvo** | L3 (Testável) na baseline; gate E3 por-Spec (RULE-MM-05, SPEC-021) | Mesmo regime das SPEC-004/005/006. |
| **Classe predominante** (orientação, não vinculante — CC-11 por BASpec) | **D** (proveniência/hash, checagem de citação, montagem do pacote, filtros temporais); **C** (selo de publicação — E3 fail-closed); **H** (formação de candidato, reranking/recuperação adaptativa, juízo de fidelidade — sempre com gate de saída, limite e parada) | Ver §5. |

**Natureza:** Spec de **infraestrutura cognitiva de conhecimento** (Trilha B). Não é de especialidade de escola (CC-12 N/A) nem de comportamento de trading (RULE-ECC-05 não incide — research §9).

---

## 2. Fronteira e escopo

### Dentro do escopo (recomendação: Opção B, §3)
- **Fonte e aquisição com proveniência:** modelo de fonte (identidade, versão/hash, localizador, cadeia de transformação), classificação de fonte antes da formação, **por referência** a CEM-001/SPEC-002 (CC-02). Fonte com instrução embutida = dado (DHR-PROV-WEB-001; SRC-OWASP-LLM08-01).
- **Unidade semântica (chunk) com contexto de origem** — o trecho sabe de onde veio (research §3.2).
- **Formação → Knowledge Candidate** (estados locais `[PROPOSTA]`; ver §8 M-001).
- **Validação → Governança → Selo de publicação** — o **contrato do selo** de que a SPEC-006 depende (RULE-CKG-010 b; `FORMED_WITHOUT_SEAL`; hipótese nunca via selo — `HYPOTHESIS_VIA_SEAL_FORBIDDEN`). O selo é **gate não-LLM**, vinculado ao hash do material validado, **E3 fail-closed**; sem prova ⇒ INDETERMINADO ⇒ não publica.
- **Recuperação:** contrato de estratégias (lexical/semântica/híbrida/relacional via consulta read-only ao KG/temporal), reranking como filtro, recuperação adaptativa em laço limitado; ranking não só por similaridade; **independência de evidência** (RULE-004; RAG-SPEC-018).
- **Evidence Packet** (saída aos agentes): evidência + **contraevidência** + lacunas + proveniência + **citação obrigatória e resolvível** + escopo temporal + marcação de evidência crítica. O agente consumidor é quem produz a **Evidência** (CEM-001; INV-06): o pacote entrega **evidência candidata**, não conclusão (INV-05).
- **RAG faithfulness** (dimensão B da SPEC-020): F1 fidelidade de formação + F2 fidelidade do pacote; método D primeiro, H depois; limiares INDETERMINADOS até calibração; fecha por emenda pontual à SPEC-020 na homologação (BL-017).
- **"WikiRAG"** = **visão compilada e legível do conhecimento já publicado** (páginas por conceito com citações às fontes imutáveis), reconstruível e **sem autoridade própria**; varredura de contradição/obsolescência só **detecta e registra** (research §3.8). `[PROPOSTA]` — Q-ABERTURA-3.
- **Atualização sem apagar:** fonte nova ⇒ derivados marcados para revalidação; publicado é superado/invalidado, nunca removido (INV-07).
- **Registro de feedback rastreável** à consulta e ao pacote (sem autoalteração — RAG-P13).

### Fora do escopo (Non-goals)
| Item | Motivo | Pertence a |
|---|---|---|
| Memória permanente, admissão por tipo, imutabilidade, contrato CKG, projeção no grafo, mecanismo físico (PostgreSQL só-inserção bitemporal) | BASELINE + H-001 FECHADA (DHR-H001-001) — não redefinir (CC-02) | **SPEC-006** |
| Memória de trabalho / enum de estados de objetos não-hipótese | BASELINE; **M-001 ABERTA** | **SPEC-004** / Andraus |
| Transporte/notificação | BASELINE (só consumir/emitir) | **SPEC-005** |
| Orçamento, empacotamento, compressão, "context rot", "lost-in-the-middle" | tema do slot de contexto | **SPEC-043** |
| Detecção de alucinação em qualquer saída do sistema | tema do slot de integridade | **SPEC-044** |
| Aprendizado a partir de feedback, governança de runtime, ciclo P12, critérios de decaimento/retenção | **K-001 ABERTA** | **SPEC-018** |
| Estado por agente / continuidade de runtime entre sessões | **G-001 ABERTA** | **SPEC-009** |
| Episódios/experiência | — | **SPEC-017** (+SPEC-009) |
| Orçamento de recursos da consulta | — | **SPEC-008** (Manager) |
| Escolha de motor (índice, embeddings, reranker, framework), OCR/parsing concreto | neutralidade tecnológica (RAG-P12) | BUILD |
| Convicção, pesos, limiares; relevância/confiança como convicção | **J-001/N-001 ABERTAS**; INV-04 | SPEC-003/CCM-001 |
| Usar motores, agentes ou skills do Inteligencia-SOT | decisão de Andraus (2026-10-18) | — (só Benchmark) |

---

## 3. Opções de decomposição — decisão explícita

| Opção | Descrição | Prós | Contras | 4Es |
|---|---|---|---|---|
| (A) Uma Spec "MC-RAG-001 inteiro" | Os 46 RAG-SPEC, incluindo contexto, aprendizado e benchmark | Uma só peça | Invade SPEC-043/018/044; não cabe numa sessão de revisão (atomic-spec §5); duplicação | Fere Efetividade e Eficiência — **rejeitada** |
| **(B) Uma Spec núcleo — RECOMENDADA** | SPEC-007 = fonte/proveniência + formação + validação + **selo** + recuperação + pacote com citação + fidelidade F1/F2 + segurança; contexto→043, aprendizado→018, alucinação sistêmica→044 | Entrega o selo que a SPEC-006 espera **e** o que os agentes vão consumir; respeita todas as referências baselined ao número (zero errata); fidelidade fecha numa só Spec (BL-017) | Spec grande para CRITICAL D0–D8 — exige corte disciplinado | Eficácia e Efetividade altas; Economicidade alta (sem errata) |
| (C) Duas Specs agora | SPEC-007 = formação + selo; Spec nova = recuperação + pacote (número na abertura dela; SPEC-047 reservado — ROADMAP l.538) | Revisões menores; o selo sai antes | **Erratum aditivo** em SPEC-002/003/006 (que mandam "retrieval → SPEC-007"); fidelidade dividida entre duas Specs; re-apontamento do BL-017 | Boa Eficiência; pior Economicidade |

**Decisão proposta: (B), com cláusula de divisão.** Se, ao redigir o Plan, o volume passar de uma sessão de revisão, volto a Andraus propondo (C) — o número 007 fica com formação + selo (o que a SPEC-006 referencia) e a recuperação vai para Spec nova, com o erratum de re-apontamento listado em research §8.1. `SPEC-007-SPLIT-001`: **não dividir agora** (Q-ABERTURA-2).

---

## 4. Quantidade

**1 Spec** (SPEC-007) sob a Opção B. Avaliei e rejeitei separar "segurança" ou "WikiRAG" em Specs próprias: segurança é requisito transversal das etapas (não componente), e o WikiRAG proposto é só uma **visão** do publicado (sem estado próprio).

---

## 5. Classe RULE-MECH-01 (CC-11) — orientação por tipo de BASpec

- **Classe D:** modelo de fonte e hash; checagem "a citação resolve?" e "o trecho existe?"; preservação literal de números/sinais; montagem do pacote; filtro temporal; independência por origem declarada; registro de feedback.
- **Classe C (E3 fail-closed):** **selo de publicação** (efeito permanente via SPEC-006; sem validação/prova ⇒ não publica); regra "conteúdo de fonte nunca é instrução".
- **Classe H (gate de saída + limite + parada — RULE-MECH-03):** formação do candidato por modelo; reranking/recuperação adaptativa; juízo de suporte por afirmação (F1/F2). O modelo **propõe**; o harness **verifica** (ENF-03).
- **Pisos de nível (D2):** publicação de evidência candidata ao Blackboard ≥ **E2**; selo/escrita permanente = **E3**. Economicidade nunca rebaixa nível.

**Critério 4Es:** Eficácia primeiro — publicar algo não validado contaminaria memória que não se apaga (INV-07); por isso o selo é Classe C/E3 e o juízo por modelo nunca é o gate final.

---

## 6. Princípios de Domínio (RULE-PD-01 / CC-12) — **NÃO incide**
Não é Spec de especialidade de escola; pipeline agnóstico de escola. Nenhum `PD-xx`.

---

## 7. Constitution Check preliminar (CC-01..CC-12) — a completar no Plan

| ID | Situação | Nota |
|---|---|---|
| CC-01 | OK | Agnóstica de escola; não cria hipótese (hipótese via selo é proibida — SPEC-006); ICT intocado. |
| CC-02 | **Aplica — foco** | Não redefine CEM/CHM/CCM nem SPEC-002/004/005/006; o selo é **interface** para RULE-CKG-010, sem alterá-la. |
| CC-03 | OK | Relevância/confiança do pacote ≠ Convicção (INV-04); J-001/N-001 intocadas. |
| CC-04 | OK | Nenhuma Salvaguarda tocada; custo de recuperação nunca entra em convicção. |
| CC-05 | Aplica | CRITICAL declarado (pin ROADMAP). |
| CC-06/07 | Diferido ao Plan | Engineering Cards. |
| CC-08 | **Aplica — foco** | Herança: CEM-001 (Lineage; Evidence Candidate projeta CEM), SPEC-002 (proveniência), SPEC-006 (RULE-CKG-010/011/013 — selo, consulta read-only, contradição), SPEC-005 (eventos), SPEC-020 (dimensão B). REMOVED vazio. |
| CC-09 | **Aplica** | Limiares de fidelidade = INDETERMINADO; números de fornecedor não viram meta; causa exige mecanismo (RULE-CAU/EPI-02). |
| CC-10 | **Aplica** | Acepções a declarar: **documento recuperado** (dado) ≠ **evidência candidata** (pacote) ≠ **Evidência** (agente, CEM) ≠ **Observação** (Skill, INV-06); **Knowledge Candidate** ≠ **conhecimento publicado**; **WikiRAG** (visão) ≠ KG (verdade permanente); **INDETERMINADO** (SOT) — não importar "UNPROVEN/BLOCKED" do Benchmark como vocabulário paralelo. |
| CC-11 | Aplica (§5) | Por BASpec. |
| CC-12 | **NÃO incide** (§6) | — |

---

## 8. Dependências, decisões abertas e backlog vinculado (CONS-01 — não fechar)

**Upstream homologado (construir sobre):** SPEC-002, SPEC-004 v1.2, SPEC-005 v1.0, SPEC-006 v1.7 (+errata v1.11/v1.12), H-001 FECHADA (DHR-H001-001), SPEC-020 (núcleo A). Nenhum bloqueador a montante aberto **para a abertura**.

**Decisões abertas que a SPEC-007 toca e NÃO fecha:**
- **M-001** — se o Knowledge Candidate é objeto do Blackboard, seus estados tocam o enum aberto. **[DECISÃO NECESSÁRIA]** — proposta: estados locais `[PROPOSTA]`, M-001 segue aberta.
- **Produtor/gatilho de promoção** (SPEC-006 l.976) — **[DECISÃO NECESSÁRIA]**; proposta: SPEC-007 produz só o conhecimento **formado** (caminho b); promoção de canônicos (caminho a) segue para SPEC-018/K-001.
- **CKG-STRUCT-ORIGIN-001** (BL-035) — aberta; a SPEC-007 não decide.
- **K-001, G-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, RULE-REG-001** — permanecem abertas.

**Itens do RMR-001 vinculados por regra (DHR-BACKLOG-ABERTURA-001) — disposições PROPOSTAS (serão declaradas no Plan; o Especificador não promove):**
- **BL-010** (MC-RAG-001) — `Disposição: PARCIAL` *(proposta)* — motivo: núcleo de RAG-SPEC-001..046 incorporado (fundamentos, formação, publicação, recuperação, pacote, fidelidade, segurança — research §7) com COL-RAG-01..04 aplicados (G-gates rejeitados; 4Es na ordem do SOT; I-RAG/RAG-P locais; RAG-SPEC-018 conforme RULE-004); Grupo D → SPEC-043, aprendizado → SPEC-018, experiência → SPEC-009/017, projeção no KG → SPEC-006.
- **BL-017** (dimensões B da SPEC-020) — `Disposição: PARCIAL` *(proposta)* — motivo: a dimensão **RAG faithfulness** é INCORPORADA (F1/F2, emenda pontual à SPEC-020 na homologação); **decision traceability** permanece com SPEC-014.
- **BL-035** (CKG-STRUCT-ORIGIN-001) — `Disposição: REFERÊNCIA` *(proposta)* — motivo: o selo carrega a identidade do produtor (insumo para a decisão), mas a decisão é de Andraus e a emenda é da SPEC-006; conhecimento formado nunca origina `hypothesis` (já proibido).
- **Conflito registrado:** ROADMAP l.34 cita só BL-010 e BL-035; pela regra do `backlog_triggers.py --abertura`, o BL-017 também vincula (research §8.3). Não resolvo em silêncio — confirmar pelo script.
- **BL-011** — não vincula por regra (gatilho `milestone:`/`spec:SPEC-006/009`); resíduo COL-EXP-05 tratado como fronteira (research §6).

---

## 9. Benchmark Inteligencia-SOT — síntese para a decisão (detalhe em research §5)
- **[FATO]** O paralelo ainda **não tem RAG implementado** (`inteligencia-sot@0abd22e:README.md:35`, `inteligencia-sot@0abd22e:ROADMAP.md:116` @0abd22e); a entrega efetiva é governança e controles determinísticos de preparação documental (tradução/OCR) + desenho de contratos RAG.
- **Objeto do SOT Harness (só referência ou integrar em parte, sempre reescrito pelo SOT):** separação formação/liberação com aprovação vinculada a hash (B1); lista de proveniência mínima (B2); casos de teste — chunk sem referência resolvível bloqueia, duas traduções do mesmo bloco não são duas evidências, fonte com comando é texto (B3); fidelidade de modalidade/causa (B4); **padrão de selo com digest confiável separado e "sem prova ⇒ bloqueia"** (B6); eixos do revisor híbrido D/P como taxonomia candidata de falhas de fidelidade (B8); conflito mostrado, não resolvido (B10).
- **Objeto do SOT, mas de outras Specs:** memória entre sessões CTX-01 → SPEC-046/PCC-001 (spec-time) ou SPEC-009/043 (runtime) (B11).
- **Só da tradução (descartar):** motores, OCR, 3 papéis, skills, Harness Score vendorizado, guarda de publicação Git (B12/B13).
- **Insumo de dados:** o livro traduzido como **fonte candidata** do corpus (B14) — só após direitos de uso, revisão humana e entrada pelo pipeline da SPEC-007.
- **Licença:** `inteligencia-sot@0abd22e:NOTICE.md:4-5` — nenhuma licença de reutilização. **Nada foi copiado.** Reuso literal de texto/código = **[DECISÃO NECESSÁRIA — titular]**.

---

## 10. Riscos

- **R-1 (publicar sem validar):** atalho "fonte → modelo → publicado". Contenção: selo Classe C/E3, gate não-LLM, hash do validado; D8 adversarial.
- **R-2 (redefinir o KG):** especificar admissão/imutabilidade/grafo na SPEC-007. Contenção: CC-02; o selo é só interface para RULE-CKG-010.
- **R-3 (relevância virar convicção):** escore de recuperação influenciar o Conviction Vector. Contenção: INV-04 explícito em BASpec de negação.
- **R-4 (falsa independência):** várias evidências da mesma origem parecerem confirmação. Contenção: RULE-004/RULE-MET-01; independência só declarada quando verificada.
- **R-5 (fidelidade com número inventado):** importar limiares de fornecedor. Contenção: INDETERMINADO até calibração (CC-09).
- **R-6 (invadir SPEC-043/044/018):** duplicar contexto, alucinação sistêmica ou aprendizado. Contenção: Non-goals §2; interfaces declaradas.
- **R-7 (envenenamento/injeção por fonte):** Contenção: fonte = dado; classificação antes da formação; publicação só sob selo.
- **R-8 (WikiRAG virar 2ª verdade):** Contenção: visão reconstruível do publicado, sem autoridade; contradição só detectada e registrada.
- **R-9 (Benchmark contaminar a soberania ou a licença):** copiar texto/código, adotar vocabulário ("UNPROVEN", "liberação de corpus") como se fosse do SOT, ou tratar corpus aprovado lá como publicado aqui. Contenção: reescrita pelo SOT; [DECISÃO NECESSÁRIA] de licença; interface só como fonte classificada (research §5.3).
- **R-10 (Spec grande demais):** Contenção: cláusula de divisão (§3).

---

## 11. Edições a documentos de governança — NÃO executadas
O Especificador **não** edita ROADMAP/CATALOGO/RMR-001/WORKFLOW/agentes/SPEC-006/SPEC-020. Após homologação, o Controlador/Andraus registram o estado e as disposições dos BL. Nenhum canônico tocado (CONST-01); nenhuma Spec baselined reescrita (INV-09); nenhuma decisão aberta fechada (CONS-01).

**Comandos a rodar (não tenho Bash — para o Orquestrador):**
- `python scripts/backlog_triggers.py --abertura SPEC-007` (confirmar BL-010/BL-017/BL-035)
- `python scripts/check_repo_research.py specs/features/SPEC-007` e `--all` (RULE-ECC-06 — esperado OK: 3 elegíveis, 2 não elegíveis com veredito coerente)
- `python scripts/build_map.py` e `python scripts/build_map.py --check` (BL-019)
- `python scripts/check_refs.py` · `python scripts/check_doc_sync.py` (informativo)

---

## 12. Perguntas a Andraus (decisão de abertura) — recomendação primeiro, em linguagem de trader

> **Contexto em uma frase:** o "caderno permanente" do sistema (SPEC-006) já existe, mas só aceita conhecimento novo se vier com um **carimbo de aprovado**. A SPEC-007 é a **linha de montagem** que pega material de leitura (livros, documentos, notas), separa os trechos com a origem anotada, propõe o que vale virar conhecimento, confere, **carimba** e, depois, entrega aos analistas os trechos certos **com a fonte citada** e com o que contradiz.

1. **Q-ABERTURA-1 (nome e peso).** *Recomendação: manter o número e o nome, e tratar como crítica (D0–D8).* Outras Specs já aprovadas apontam para "SPEC-007"; mudar custaria correções nelas. **Confirma?**

2. **Q-ABERTURA-2 (uma Spec ou duas).** *Recomendação: uma Spec só (Opção B) — linha de montagem + carimbo + entrega com citação + medida de fidelidade —, deixando "tamanho da memória de curto prazo do analista" para a SPEC-043, "detector de invenção em qualquer saída" para a SPEC-044 e "aprender com o uso" para a SPEC-018.* Se ficar grande demais para revisar de uma vez, volto propondo dividir em duas. **Confirma?**

3. **Q-ABERTURA-3 (o que é "WikiRAG").** *Recomendação: WikiRAG = uma **versão de leitura** do que já foi carimbado (uma página por assunto, com as fontes citadas), que pode ser refeita a qualquer momento e **não manda em nada** — quem manda é o caderno permanente.* A alternativa da moda (o modelo escreve e mantém o wiki sozinho) seria publicar sem carimbo, o que o sistema proíbe. **Aceita esse sentido?**

4. **Q-ABERTURA-4 (dono do carimbo).** *Recomendação: a SPEC-007 define o carimbo do conhecimento **formado a partir de fontes**; a promoção de hipóteses/evidências do próprio sistema para o caderno continua uma decisão em aberto, a tratar na SPEC-018.* **Confirma essa divisão?**

5. **Q-ABERTURA-5 (fidelidade — fechar a pendência da SPEC-020).** *Recomendação: medir fidelidade em duas partes — (1) o conhecimento formado não inventa nada que a fonte não diga (nem troca "pode" por "vai", nem associação por causa); (2) cada frase entregue ao analista tem apoio no trecho que cita. Primeiro checagens automáticas, depois juízo do modelo com conferência. **Sem números de corte agora** — só depois de calibrar com amostra.* Fechamos essa pendência da SPEC-020 quando a SPEC-007 for aprovada. **Aceita?**

6. **Q-ABERTURA-6 (o material antigo em `rag/`).** *Recomendação: os 5 arquivos `rag/*.knowledge.md` ficam como estão (nada é apagado), tratados como **material de leitura** que precisa passar pela linha de montagem e receber carimbo antes de valer como conhecimento publicado.* **Confirma?**

7. **Q-ABERTURA-7 (projeto paralelo Inteligencia-SOT).** *Recomendação: (a) usar dele só **ideias de controle** (carimbo ligado ao hash do material aprovado; "sem prova, bloqueia"; casos de teste de fidelidade), **reescritas pelo SOT**, sem copiar texto nem código — então hoje **não** é preciso dar licença; (b) se um dia quisermos copiar algo literal, você, como titular, decide a licença/atribuição; (c) o livro traduzido pode virar **fonte** do SOT, mas só depois que você decidir o direito de uso da obra (é de terceiro), houver revisão humana da tradução e ele entrar pela linha de montagem.* **Aceita (a), e registra como decisões suas (b) e (c)?** *(Itens (b) e (c) = [DECISÃO NECESSÁRIA] — não posso decidir.)*

> **Estas 7 perguntas aguardam Andraus na homologação da abertura.** Nenhuma decisão aberta é fechada aqui (CONS-01): M-001, K-001, G-001, J-001, N-001, C-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção e as demais seguem abertas.

---

## 13. Próximo passo
`research.md` + `sources/` + esta Proposta seguem para **parecer do Revisor** sobre o processo do Dossiê (RULE-ECC-02/04/06; não incidência de ECC-05/CC-12; disposições propostas dos BL; tratamento do Benchmark) e, depois, **homologação de Andraus** da definição da Spec (número, nome, CRITICAL D0–D8, quantidade = 1 com cláusula de divisão, fronteiras, Classe orientativa, sentido de WikiRAG) e das 7 perguntas — **antes** de qualquer `plan.md`/`checks.md`.

**Pronto para revisão.**
