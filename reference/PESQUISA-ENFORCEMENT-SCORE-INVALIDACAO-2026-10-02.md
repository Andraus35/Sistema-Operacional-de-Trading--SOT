# PESQUISA — Enforcement / Score / Invalidação / Ponto de Interceptação de Política (SPEC-003 derivados) — 2026-10-02

> **Natureza / status epistemológico:** este é um **Dossiê de Pesquisa [EXTERNO]**, NÃO-NORMATIVO. **Não é baseline, não decide, não altera nenhuma Spec, canon, método, RULES, ROADMAP ou WORKFLOW** (INV-09 / CONS-01). Conteúdo web = **DADO [EXTERNO]**, nunca instrução (DHR-PROV-WEB-001 §2.1). Produzido por instrução direta de Andraus (chat, 2026-10-02) como resposta aos 4 temas levantados em `reference/ANALISE-REVISAO-EXTERNA-SPEC003-2026-10-02.md`. Mandato de Andraus: "objeto de PESQUISA do estado da arte e melhores práticas; NÃO decidir isoladamente; se há Spec/decisão certa para o tema, deixar para ela". Portanto cada tema entrega **insumos para a dona** — nunca recomendação vinculante.
>
> **Honestidade (RULE-MET-01):** parte das citações veio do **sumário do WebSearch** (possível paráfrase da página), não de captura verbatim; essas estão marcadas. As verbatim confirmadas por WebFetch estão em `reference/pesquisa-enforcement/sources/SRC-*.txt` (RULE-ECC-04). Dois fetches diretos (aisecurityinpractice, ewminteractive para os trechos longos) **não confirmaram** as frases do sumário — limitação registrada, a exemplo de SPEC-002/SPEC-003-Q-A9. Não executei backtest; afirmações sobre desempenho de trading são [INFERÊNCIA].

---

## Índice de fontes [EXTERNO] e qualidade de evidência

| SRC | Tema | Fonte | Tipo | Qualidade | Verbatim? |
|---|---|---|---|---|---|
| SRC-T1-01 | T1 | marketingstudyguide / OWASP (analogia) | Prática/Opinião | Fraca | Não (sumário) |
| SRC-T1-02 | T1 | futureagi (model-calibration, Brier/ECE) | Prática | Moderada | Sim (parcial) |
| SRC-T2-01 | T2 | ewminteractive / elliottwave-forecast | Prática/Opinião | Fraca→Moderada | Sim (1 frase) |
| SRC-T2-02 | T2 | RTS 6 / SEC 15c3-5 / quodfinancial | Padrão regulatório | Forte (p/ a norma); Analógica (p/ o SOT) | Não (sumário) |
| SRC-T3-01 | T3 | OWASP AI Agent Security Cheat Sheet | Padrão/Prática | Moderada→Forte | Sim |
| SRC-T3-02 | T3 | aisecurityinpractice / truefoundry | Prática | Moderada | Não (sumário) |
| SRC-T4-01 | T4 | NIST SP 800-162 (glossário PEP) | Padrão | Forte | Sim |
| SRC-T4-02 | T4 | XACML / NIST SP 800-162 (arquitetura) | Padrão | Forte | Não (sumário) |

Classificação de qualidade: **Forte** = padrão/norma estabelecida; **Moderada** = prática de engenharia consolidada com fonte técnica; **Fraca** = material didático/opinião; **Anedótica** = relato isolado.

---

## T1 — Composição e limiar do "score" de qualidade de setup (gate `score ≥ 7/9`)

**Pergunta:** como compor e calibrar um score/checklist de qualidade de decisão de trade para servir de gate, e o que a literatura diz sobre a escolha do limiar.

**Achados [EXTERNO]:**
- **Gating não-compensatório vs compensatório** (SRC-T1-01, qualidade Fraca): regra não-compensatória exige que **cada critério relevante** seja satisfeito — um critério bom não "compensa" outro ruim; regra compensatória soma/pondera e permite compensação. Analogia de engenharia citada: "a knowledge score would not offset granting write access during a read-only task" [EXTERNO, paráfrase de sumário].
- **Calibração e escolha de limiar** (SRC-T1-02, qualidade Moderada): o **Brier score** é "mean squared error between confidence and one-hot correctness; lower is better" [verbatim]; **reliability diagrams/ECE** exigem amostra grande — "ECE needs >=1,000 samples per confidence bucket to be stable" [verbatim]. A direção recorrente das fontes é **separar calibração (probabilidade confiável) da escolha do ponto de corte (decisão de custo)** [paráfrase].
- **Risco de overfitting de limiar** (SRC-T1-02): calibração em holdout pequeno degrada probabilidades; limiar escolhido em amostra pequena é instável.
- **Scorecards binários de N itens em finanças** (ex.: Piotroski F-Score 0–9) existem como **analogia metodológica** — contagem não-compensatória de condições binárias. Citar com cautela: é analogia de forma, não evidência de eficácia no SOT.

**O que o repo JÁ tem:**
- `GLOSSARIO.md:94` — Score 0–9 declarado **PILOT** ("cada layer até 3 pontos"; "NÃO substitui o Conviction Vector 8D"; limiar Fase Piloto, recalibrável).
- `specs/features/SPEC-003/plan.md:604,658` — gate CF-012 usa `score ≥ 7/9` como **limiar interino** (Questionário v1); `:661` fixa que a Spec dá **método, não números** — definitivos = J-001/N-001.
- `governance/AUDITORIA-HIGIENE-SPECS-2026-10-01.md` H-16 — vigiar aposentadoria do Score PILOT ao homologar SPEC-003.
- `canon/CEE-001...v2.0.md:325` — Salvaguarda de Sinal 2 (score < 7/9 → bloqueado), limiar Fase Piloto.
- Já rastreado no backlog: **BL-004** (Absorvido — método/limiares-piloto fixados na abertura da SPEC-003; **J-001/N-001 permanecem abertas** para os definitivos) e **BL-002** (falso-DENY, dispara em J-001 resolvida).

**DONA CORRETA:** **J-001** (fórmula/pesos/limiares definitivos do Conviction Vector) + **N-001** (pesos por ativo), materializadas no **CCM-001** quando redigido; a **aposentadoria do Score 0–9 PILOT** é o achado **H-16**, cuja decisão Andraus já reservou para "ao homologar SPEC-003 / quando CCM-001-J-001 existirem". Justificativa: a composição do "9" e o corte 7/9 são exatamente os valores definitivos que o projeto congelou como abertos (CONS-01); fixá-los agora violaria INV-03/CONS-01.

**Insumos para a dona (quando abrir):** (a) decidir entre **manter** 0–3 por agente analítico somado deterministicamente a partir do vetor, **aposentar** o score em favor de critério do vetor 8D (H-16), ou **deixar explícito em J-001**; (b) se o score/convicção virar gate, **calibrar o corte por custo assimétrico** (custo de falso-sinal vs. perda de oportunidade), não pela métrica, e só **após** calibração de probabilidade; (c) usar Brier/reliability diagram com **amostra suficiente** (≥1.000/bucket) no backtest; (d) tratar o gate como **não-compensatório** (coerente com a Salvaguarda de Sinal e com a agregação estrutural-primeiro já especificada em CF-006) — a compensação entre dimensões é justamente o que INV-04/§11 proíbem.

**Riscos:** overfitting de limiar em amostra pequena; ler "70%"/"7/9" como probabilidade calibrada antes de haver calibração (ver N4 da análise); importar o Piotroski F-Score como se fosse evidência de eficácia (é só analogia de forma).

---

## T2 — Pré-requisito de "nível de invalidação explícito" antes de habilitar sinal

**Pergunta:** a literatura/ regulação sustenta exigir completude (stop/invalidação) antes de habilitar uma ordem? E a hipótese Elliott exige nível de invalidação?

**Achados [EXTERNO]:**
- **Controles pré-trade regulatórios** (SRC-T2-02, qualidade Forte p/ a norma): MiFID II **RTS 6** exige limites pré-trade (preço, volume, valor, mensagens, kill-switch); **SEC Rule 15c3-5** (Market Access Rule) exige controles de risco pré-trade e **proíbe acesso "naked/unfiltered"** [paráfrase de sumário]. **Importante:** essas normas tratam de **limites quantitativos de ordem**, não de "nível de invalidação de hipótese" — a ligação ao SOT é **analogia metodológica** (nenhuma ordem/sinal passa sem controle pré-trade completo), não equivalência regulatória.
- **Falseabilidade / invalidação em Elliott** (SRC-T2-01, qualidade Fraca→Moderada): "the Elliott Wave Principle comes with a specific invalidation level attached to each trade setup" [verbatim]. A direção das fontes: um wave count é tratado como **hipótese com invalidação explícita**; "a hypothesis must be disprovable" [paráfrase]; count sem invalidação/alternativa/plano de risco é "storytelling" [paráfrase].

**O que o repo JÁ tem:**
- `canon/CEE-001...v2.0.md:324` — **Salvaguarda de Sinal 1 (inviolável): "Hipótese sem nível de invalidação explícito → bloqueada."** Já é FATO NORMATIVO constitucional.
- `specs/features/SPEC-001/plan.md:284,291-293` — hipótese carrega **invalidador declarado** usado na transição para REFUTED (BASpec-HH-006); `:662` — SUB herda/refina "Nível de invalidação" da PRIMARY.
- **Lacuna real (N2 da análise):** SPEC-001 **modela** o invalidador e o usa para refutar, mas **não há precondição verificável que BLOQUEIE** uma hipótese/sinal sem `invalidation_level` (a Salvaguarda 1 não está materializada como gate). Busca por `invalidation_level`/`Salvaguarda 1`/`sem nível` em SPEC-001 = **0 resultados**. O gate CF-012 (SPEC-003) checa 3 condições (convicção, score, conflito) — a Salvaguarda 1 **não** está entre elas, embora CC-04 afirme preservar as 5.

**DONA CORRETA: [DECISÃO NECESSÁRIA: dona a definir por Andraus].** A Salvaguarda 1 é constitucional (CEE-001 §11), mas **onde ela vira precondição verificável** não está decidido. Duas candidatas:
- **Candidata A — SPEC-001 (Hypothesis Harness, baselined v1.1):** precondição de que uma hipótese não alcance ACTIVE/DOMINANT (ou não seja elegível a sinal) sem `invalidation_level` preenchido. Custo: **emenda a Spec baselined** (INV-07; exige EUA/ato de Andraus) — a auditoria BL-008 adotou regime "auditoria-não-reescrita", então uma emenda aditiva seria o caminho.
- **Candidata B — Manager Fase 2 / SPEC-014 (consumidor do gate) ou a própria SPEC-003 (gate CF-012):** adicionar a precondição `hypothesis_ref com invalidation_level explícito` ao gate que habilita o sinal. Custo baixo, mas SPEC-003 está fora do escopo deste trabalho (instrução de Andraus) e SPEC-014 ainda não está em redação.

**Insumos para a dona:** materializar a Salvaguarda 1 como **precondição de Enforcement Contract** (PRECOND fail-closed) e não como cláusula declarativa; alinhar com a prática Elliott de "escrever a invalidação antes de entrar"; decidir se corrige CC-04 da SPEC-003 (afirmação de que o gate preserva as 5) ou se inclui a 1ª Salvaguarda no gate — mas isso é decisão da dona, não deste Dossiê.

**Riscos:** deixar a afirmação CC-04 (preserva 5 Salvaguardas) sem a precondição correspondente é uma inconsistência latente entre canon e Spec candidata (apontada como N2 "Maior"); por outro lado, mover a precondição para o lugar errado duplicaria enforcement (ver T4).

---

## T3 — "LLM propõe, harness verifica/recomputa"

**Pergunta:** como garantir que o número que o gate avalia não seja apenas o que o LLM propôs, e como validar saída de LLM antes do consumo downstream.

**Achados [EXTERNO]:**
- **OWASP AI Agent Security** (SRC-T3-01, Moderada→Forte): "Grant agents the minimum tools required for their specific task" [verbatim]; "Prevent privilege escalation through agent chains" [verbatim]; "Validate agent outputs before execution or display" [verbatim].
- **Structured outputs / validação determinística** (SRC-T3-02, Moderada): saída estruturada é "a boundary where a probabilistic model meets deterministic software"; validação determinística (cross-field/range/format/reconciliation) deve rodar **como código, não como outra chamada de modelo**; validação de aplicação cobre regras que o schema não expressa (ownership, **freshness**) [todos paráfrase de sumário — não confirmados verbatim; limitação registrada].
- **Recomputação verificável** (sumário de busca): "a recompute-verifiable hash chain ... verification re-derives every hash from the persisted record" — recomputar agregados a partir do registro persistido, em vez de confiar no valor reportado [paráfrase].

**O que o repo JÁ tem:**
- `specs/features/SPEC-003/plan.md:606-607` (CF-012: "LLM nunca é o gate, ENF-03"); `:840-843` (ADV-CF-08 `LLM_IS_NOT_GATE`); `canon`/`RULES` Classe H exige gate determinístico.
- `atomic-spec.md:219,266` — princípio ENF-03 ("O LLM não é seu próprio gate; checagem semântica = detector").
- `plan.md:917-950` — objeto Conviction Vector com `status`, `thresholds_used`, reconstrução, `source_evidence_ids`.
- **Lacuna real (N3 da análise, Médio):** não está dito que o gate **recomputa/valida** `global_conviction`/`score` a partir das notas por dimensão persistidas; não há campo `computed_by` nem `gate_record` explícito no objeto; não há **precondição de consumidor** ("só consumir vetor `status == GATED_PASS`").

**DONA CORRETA (múltipla, por camada):**
- **Mecanismo de recomputação** (o gate recalcula o agregado a partir das notas persistidas; LLM só propõe notas) → **SPEC-003** (mecanismo CCM-001) — **fora do escopo agora** por instrução de Andraus; fica como insumo para quando a SPEC-003 for revisitada ou herdada.
- **Precondição do consumidor** ("Manager só consome `GATED_PASS`") + campos de proveniência `computed_by`/`gate_record` na síntese → **Manager Contract / SPEC-014 (Fase 2 Convicção & Síntese)** (DHR-EUA-E23).
- **Proveniência no objeto publicado** (quem computou cada campo; append-only) → **SPEC-004 (Blackboard)** — depende de **M-001** (aberta).
- **Capability boundary / least privilege / declaração negativa** (o que o mecanismo NÃO pode chamar; allowlist por agente) → **runtime: SPEC-018/K-001 e SPEC-045**.

**Insumos para a dona:** adotar o padrão "structured output = fronteira probabilístico↔determinístico"; recomputar agregados em código a partir do registro persistido (hash/reconstrução já previstos em P13); precondição de consumidor fail-closed; `computed_by`/`gate_record` para rastrear origem de cada campo. **A revisão externa tem razão neste ponto** (N3) — mas a materialização é da dona.

**Riscos:** sem recomputação, "gate determinístico" pode apenas comparar um número proposto pelo LLM (o gate seria sintaticamente determinístico, mas semanticamente dependente do LLM); excesso de validação redundante por Spec (ver T4).

---

## T4 — Ponto de interceptação de política e "contrato comum de enforcement"

**Pergunta:** como centralizar a aplicação de política para não ter um validador por Spec.

**Achados [EXTERNO]:**
- **NIST SP 800-162 / XACML** (SRC-T4-01 verbatim, SRC-T4-02 sumário, qualidade Forte): PEP "Enforces policy decisions in response to a request from a subject requesting access to a protected object; the access control decisions are made by the policy decision point" [verbatim NIST]. A arquitetura de referência separa **PDP** (decide), **PEP** (aplica), **PAP** (administra políticas), **PIP** (fornece atributos) [paráfrase]. Padrão consolidado: **separar decisão de política (PDP) de aplicação (PEP)**, com políticas centralizadas em vez de embutidas em cada serviço.
- OPA (Open Policy Agent), citado no mandato, **não** retornou fonte específica nesta rodada — registrado como lacuna de pesquisa.

**O que o repo JÁ tem:**
- `atomic-spec.md` §10 (§10.1–§10.4) — camada de Enforcement E0–E3 e **template do Enforcement Contract** (CAPABILITY/EFFECT/PRECOND/POSTCOND/POLICY/LEVEL/FAILURE-MODE/EVIDENCE). **Não há** hoje um campo **ENFORCER / ponto de interceptação** (quem aplica o contrato em runtime).
- Donas de runtime já previstas: **SPEC-019** (policy, baselined, spec-time), **SPEC-018/K-001** (governança runtime), **SPEC-045** (caminho de leitura runtime), **BL-013** (MC-GOV-001 — camada de governança, `Em espera`).

**DONA CORRETA (dupla):**
- **Método (template do Enforcement Contract):** emenda **única** ao `atomic-spec.md` §10 adicionando campo `ENFORCER / PONTO DE INTERCEPTAÇÃO` — é alteração de **método**, homologável por **EUA/ato de Andraus** (fora do escopo deste trabalho: não altero atomic-spec).
- **Runtime (contrato comum de enforcement):** **SPEC-018/K-001** com insumo do **BL-013 (MC-GOV-001)** — especificar um PEP/PDP comum (schema/guard/state/capability aplicados em um ponto), em vez de 1 validador por Spec.

**Insumos para a dona:** mapear o par PEP/PDP do NIST/XACML para a arquitetura SOT (o gate determinístico = PEP; a política constitucional/CEE-001/§11 = PDP; o Blackboard/estado = PIP); evitar "floresta de validadores" com um ponto de interceptação comum em runtime; manter ENF-03 (detector ≠ gate) e fail-closed. Corresponde a R5 da análise (emenda única de método + insumo do Dossiê da SPEC-018).

**Riscos:** criar uma 2ª taxonomia de autoridade (AUTHORITY MODE) **duplicaria** a Classe D/H/P/C + ENF-03 (E3 da análise) — a análise já recomenda **não** adotar; o campo ENFORCER é aditivo ao template, não uma taxonomia nova.

---

## O que NÃO é lacuna de Spec (já coberto)

- **"LLM é detector, nunca gate"** — já normativo: ENF-03 (`atomic-spec.md:266`), CF-012/ADV-CF-08 (SPEC-003). T3 só acrescenta o *como recomputar*, não o princípio.
- **"Falta Output Contract único"** (E2 da análise) — o objeto Conviction Vector/CCM-001 já é o contrato de saída; lacuna é menor (`computed_by`/`gate_record`), tratada em T3.
- **"Harness global para evitar floresta de validadores"** (E5) — já tem donas no repo (atomic-spec §10 Enforcement, SPEC-018/019/045, BL-013). T4 só acrescenta o campo ENFORCER e o insumo PEP/PDP.
- **Taxonomia AUTHORITY MODE** (E3) — rejeitada; duplicaria Classe D/H/P/C.
- **Implementação física adiada** (E7) — deliberada (spec-first, AGENTS.md §1), não é defeito.
- **Salvaguarda 1 como princípio** — já é constitucional (CEE-001 §11.1); a lacuna (T2) é só a *materialização como precondição verificável*, não o princípio.

---

## Encaminhamento (ver Entrega B)

Itens de backlog criados (mecanismo RMR-001): **BL-027** (T1), **BL-028** (T2), **BL-029** (T3), **BL-030** (T4). Todos `Em espera`, gatilho `spec:/decisao:`; ação ao ativar = a dona recoloca o tema no Dossiê de abertura usando esta pesquisa como fonte de dados. Nada aplicado às Specs (CONS-01).

---

*Dossiê [EXTERNO] não-normativo. Fontes verbatim em `reference/pesquisa-enforcement/sources/`. Produzido por instrução de Andraus (2026-10-02). Não baseline, não decide.*
