# ERRATUM-REAPONT-001: errata aditiva de re-apontamento (recuperação e pacote: SPEC-007 → SPEC-048). PROPOSTA

| Campo | Valor |
|---|---|
| Código | **ERRATUM-REAPONT-001**. Número e nome são **propostos**; quem atribui é Andraus, na homologação (Q-1). |
| Versão | **v1.0** (2026-10-30). Primeira entrega. |
| Natureza | **PROPOSTA de errata aditiva e editorial** (só endereço). Espera o Revisor e a homologação de Andraus. **Não é baseline.** Nada aqui vale antes da homologação (RULE-HG-01/02/03). **Não edita** nenhum `plan.md`, `checks.md`, ata, ERRATUM nem o `ROADMAP.md` (INV-07/INV-09). |
| Ordem | Ordem de Andraus transmitida pelo Orquestrador (chat, 2026-10-30: "Seguir com a errata de re-apontamento"). Executa a DHR-RETRO-001 §1 ("Próxima frente", item (3): "errata de re-apontamento (regra de busca da ata `DHR-SPEC048-001`, Q-7)") e §2 ("Uma de cada vez, nesta ordem, cada uma com Revisor e homologação própria de Andraus"). Os itens (1) e (2) já foram homologados (DHR-SPEC006-005; DHR-SPEC020-002). `[FONTE: FATO NORMATIVO, DHR-RETRO-001. A ordem de 2026-10-30 é registro do Orquestrador e ainda não está em ata]` |
| Regra que manda esta errata | DHR-SPEC048-001 §1, linha Q-7: "**A ata registra a REGRA DE BUSCA** (critério 1: "SPEC-007" junto de retrieval/recuperação/evidence candidate/pacote/RAG faithfulness, em Spec baselined ou errata homologada; critério 2: "SPEC-048" junto de WikiRAG/página de leitura, em Spec baselined ou ata → Spec da página) e a errata, proposta no Plan da SPEC-048, corrige o que a busca achar na hora de ser escrita". `[FONTE: FATO NORMATIVO]` |
| Fontes de verdade da divisão | DHR-SPEC007-002 §3 (fronteira: "SPEC-007 (reduzida, formação + selo)" × "SPEC-048 (nova, recuperação + pacote)") e §4 (re-apontamentos "LISTADOS, não executados"); DHR-SPEC007-004 linha P-14 ("Definição de 'mesma origem' na SPEC-007; contagem no pacote na SPEC-048", COL-EXP-05); DHR-SPEC048-002 (Plan v1.4 da SPEC-048 "HOMOLOGADO, BASELINE"; §3: a "errata de re-apontamento SPEC-002/003/006" foi deixada para passo à parte); DHR-SPEC020-002 + ERRATUM-SPEC020-002 (metade F1). `[FONTE: FATO NORMATIVO]` |
| Insumo | `specs/features/SPEC-048/plan.md` (BASELINE v1.4), seção "Proposta de errata aditiva de re-apontamento" (busca de 2026-10-24). **A busca foi refeita agora** (seção 2); a proposta antiga serve só de comparação. |
| Fonte do estado das decisões | **Só o `ROADMAP.md`**, linhas "Decisões abertas ativas" e "Decisões FECHADAS". Cada ID foi conferido ali. |
| Âncoras | **Por texto literal entre aspas, nunca por número de linha** (prática P2; P3 ainda a especificar, DHR-RETRO-001 §1). Os "l.NNN" da seção 2 ajudam só a localizar, conferidos em 2026-10-30. A âncora que vale é o texto. |
| Complexidade declarada | **LOW** (D0–D3, profile light). Motivo: a errata só corrige endereço. Não tem comportamento, efeito, RULE, BASpec, EC nem estado. A complexidade das Specs afetadas (várias CRITICAL) **não é herdada**, porque nada do comportamento delas é tocado. Declarado aqui em vez de elevar em silêncio. Se Andraus ou o Revisor quiserem outra régua, é a Q-7. O §7-bis foi feito mesmo assim (seção 11), de forma voluntária. |
| Status epistemológico | `[FONTE]` = conferido no arquivo citado. `[LITERAL]` = resultado de busca de texto, reproduzível. `[INFERÊNCIA]` = julgamento do Especificador, que o Revisor confere. `[PROPOSTA]` = o que se pede a Andraus. `[DECISÃO NECESSÁRIA]` = lacuna que o Especificador não resolve. |
| Autor · Data | Especificador Principal SOT (Claude Code, Opus 5.5) · 2026-10-30 |

---

## 0. O que esta errata faz, em uma frase

A SPEC-007 foi dividida (DHR-SPEC007-002, Opção C). **Formação e selo continuam na SPEC-007.** **Recuperação, contagem de origens no pacote, pacote de evidência, entrega e fidelidade F2 passaram à SPEC-048**, que já é baseline (DHR-SPEC048-002). Esta errata põe **notas aditivas de endereço** nos trechos de Specs homologadas que a regra de busca da Q-7 encontrou e que ainda mandam "retrieval / recuperação / evidence candidate / pacote" à SPEC-007. `[FONTE: DHR-SPEC007-002 §3/§4; DHR-SPEC048-001 Q-7; DHR-SPEC048-002]`

**Não faz:**
- Não muda regra, BASpec, EARS, EC, cenário, ADV, estado nem schema de nenhuma Spec.
- Não cria ID novo (RULE, BASpec, EC, ADV).
- Não define critério para a metade F2 da "RAG faithfulness". Isso fica para um erratum à parte, da SPEC-048 (DHR-SPEC048-002 §3; ERRATUM-SPEC020-002 §1.9).
- Não altera o CONFLICT-MAP: isso só muda por ato de Andraus.
- Não atualiza o ROADMAP nem o RMR-001. Esses itens vão listados para o Orquestrador e Andraus (seção 7).
- Não fecha nenhuma decisão aberta (seção 14).

---

## 1. Método da busca (a parte LITERAL, reproduzível) `[LITERAL]`

**Critério 1 (exato, conforme a Q-7).** Linha em que "SPEC-007" aparece junto (na mesma linha) de um destes termos: `retrieval`, `recupera…` (recuperação, recuperado), `evidence candidate`, `pacote` ou `RAG faithfulness`. Sem diferença entre maiúscula e minúscula. A expressão usada foi `SPEC-007.*(retrieval|recupera|evidence candidate|pacote|RAG faithfulness)` e também a ordem inversa.

**Critério 1, busca ampliada (só para dar transparência).** O mesmo, trocando "RAG faithfulness" por `RAG` sozinho. Serve para achar vizinhos que o critério exato não pega. **O que só a busca ampliada encontra não entra na errata por força da regra.** Entra só se Andraus decidir, e está marcado `[INFERÊNCIA]`.

**Critério 2.** Linha em que "SPEC-048" aparece junto de `WikiRAG`, `página de leitura` ou `visão de leitura`.

**Universo pesquisado (o que a Q-7 chama de "Spec baselined" e "errata homologada"):**
- `specs/features/*/plan.md` e `checks.md`;
- `specs/features/SPEC-006/errata-v1.13.md` (homologada, DHR-SPEC006-005);
- `governance/ERRATUM-*.md`;
- para o critério 2, também as atas `governance/DHR-*.md`;
- o `ROADMAP.md`, só para registro (seção 7).

**Fora do universo, com motivo:**
- `research.md`, `ABERTURA.md`, `sources/`, pareceres e propostas em `governance/propostas/`. Dossiê e proposta não são "Spec baselined". Mesmo critério da busca de 2026-10-24. `[INFERÊNCIA]`
- Especs GEN-1 `specs/*.spec.md`: zero ocorrências de "SPEC-007".
- **SPEC-007 e SPEC-048** são as duas partes da divisão. Os baselines delas já trazem a divisão no próprio texto: a SPEC-007 v2.3 diz "Recuperação, pacote de evidência, WikiRAG e F2 passam à **SPEC-048**", e a SPEC-048 v1.4 traz o "Termo 1". Logo, ficam fora do critério 1 como alvo. A SPEC-007 entra no critério 2 (seção 6).

---

## 2. Resultado LITERAL e comparação com a busca de 2026-10-24 `[LITERAL]`

Legenda da coluna "Desde 10-24": **mantida** = mesmo texto, já estava na tabela da SPEC-048. **NOVA** = não estava naquela tabela. **ampliada** = só a busca ampliada encontra.

### 2.1 Critério 1: Specs (`plan.md` / `checks.md`)

| # | Documento | Texto literal (âncora) | Desde 10-24 |
|---|---|---|---|
| L-01 | SPEC-002 `plan.md` (l.170) | "\| RAG / evidence candidate a partir de retrieval \| **SPEC-007** \| Fase 3 \|" | mantida |
| L-02 | SPEC-002 `plan.md` (l.848) | "- **RAG:** nenhum; a camada não escreve no KG/RAG (evidence candidate a partir de retrieval → SPEC-007)." | mantida |
| L-03 | SPEC-003 `plan.md` (l.1080) | "- **RAG:** nenhum; a camada não escreve no KG/RAG (evidence candidate a partir de retrieval → SPEC-007)." | mantida |
| L-04 | SPEC-006 `plan.md` (l.12) | "Opera **sobre** conhecimento já validado/publicado; formação/retrieval é SPEC-007 (não absorvida)" | mantida |
| L-05 | SPEC-006 `plan.md` (l.52, BL-011) | "são **FORA** → SPEC-007 (retrieval), SPEC-018/K-001 (aprendizado/evolução)" e, na mesma linha, "dup. EXP-SPEC-021↔RAG-SPEC-018 ADIADA a SPEC-007/009 — COL-EXP-05" | mantida |
| L-06 | SPEC-006 `plan.md` (l.76) | "\| §40 Retrieval — 015-020, 022 (Retrieval/Similar/Contrasting/Temporal/Regime/Relevance/Packet) \| recuperação/relevância/packet \| **FORA** → SPEC-007 (RAG); KG só consulta read-only" | mantida |
| L-07 | SPEC-006 `plan.md` (l.77) | "\| §40 Retrieval — 021 Experience Independence \| independência/duplicação inter-camada \| **ADIADO** (COL-EXP-05/R-07): dup. EXP-SPEC-021↔RAG-SPEC-018 → SPEC-007/009" | **NOVA** |
| L-08 | SPEC-006 `plan.md` (l.98) | "\| R-07 · COL-EXP-05 — EXP-SPEC-021 ↔ RAG-SPEC-018 (dup.) \| ADIAR reconciliação → SPEC-007/009 \| **ADIADO** — fronteira RAG respeitada (retrieval=SPEC-007)" | mantida |
| L-09 | SPEC-006 `plan.md` (l.261) | "> **Termo 4:** \"documento recuperado\" (RAG — SPEC-007) ≠ \"conhecimento validado\" (KG)." | mantida |
| L-10 | SPEC-006 `plan.md` (l.299) | "- Não **forma conhecimento** / não faz retrieval → **SPEC-007**; recebe conhecimento **publicado**." | mantida |
| L-11 | SPEC-006 `plan.md` (l.341) | "\| Formação de conhecimento / retrieval \| **SPEC-007** \| recebe conhecimento publicado \|" | mantida |
| L-12 | SPEC-006 `plan.md` (l.963, BASpec-CKG-010) | "PORQUE:       \"Documento recuperado ≠ validado ≠ publicado\"; formação é SPEC-007" | mantida |
| L-13 | SPEC-006 `plan.md` (l.1309, ADV-CKG-08) | "a Spec tentaria especificar extração/retrieval/validação no KG. … **ENTÃO:** achado de revisão — fora de escopo; formação é SPEC-007. … a Spec não contém comportamento de formação/retrieval (conferível por leitura)." | mantida |
| L-14 | SPEC-006 `plan.md` (l.1578) | "\| Absorver a SPEC-007 (formação/retrieval) \| Non-goal; CKG-010 (selo); ADV-08 \|" | mantida |
| L-15 | SPEC-006 `plan.md` (l.1594) | "- **RAG/KG:** especifica o contrato do próprio KG; formação/retrieval em SPEC-007 (não absorvida)." | mantida |
| L-16 | SPEC-006 `plan.md` (l.103) | "(3) dup. EXP-SPEC-021↔RAG-SPEC-018 → **ADIADA** a SPEC-007/009 (COL-EXP-05)." | **NOVA, ampliada** (sem termo do critério exato) |
| L-17 | SPEC-006 `plan.md` (l.53) | "- **BL-010** (MC-RAG-001) — `Em espera`, gatilho `spec:SPEC-007 em redação` ∨ `milestone:FASE 3 iniciada`. BL-010 é fonte da **SPEC-007**" | **NOVA, ampliada** |
| L-18 | SPEC-006 `checks.md` | **zero** no critério exato e no ampliado | sem mudança |
| L-19 | SPEC-020 `plan.md` (l.116) | "Não fecha as dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability) → **SPEC-007/038/014 (BL-017)**." | mantida |
| L-20 | SPEC-020 `plan.md` (l.144) | "\| Dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability) \| **SPEC-007 / 038 / 014** (BL-017) \| DIFERIDAS por EUA-E17 + BL-017" | mantida |
| L-21 | SPEC-020 `plan.md` (l.515, ADV-EV-06) | "**ENTÃO:** rejeitar `CLASS_B_PREMATURE`; classe B permanece DIFERIDA (SPEC-007/038/014; BL-017)" | mantida. **Atenção:** não tem "RAG faithfulness" na linha, então **não casa com o critério exato**. A tabela de 10-24 a incluiu pela mesma inferência da m-11 ("classe B" contém RAG faithfulness) |
| L-22 | SPEC-020 `plan.md` (l.720) | "- **Classe B** (RAG faithfulness / tool correctness / decision traceability) — DIFERIDA (BL-017); fecha em SPEC-007/038/014." | mantida |
| L-23 | SPEC-020 `plan.md` (l.728) | "**Errata aditiva (2026-10-03, DHR-SPEC038-002):** … RAG faithfulness (SPEC-007) e decision traceability (SPEC-014) permanecem diferidas." | mantida |
| L-24 | SPEC-020 `plan.md` (l.730) | "**Errata aditiva (2026-10-30, DHR-SPEC020-002):** dimensão B \"RAG faithfulness\", **metade F1** … conformidade a F1 da SPEC-007 (RULE-KFH-005/006) … metade F2 (SPEC-048) e decision traceability (SPEC-014) permanecem diferidas." | **NOVA** (é a linha de ponteiro do ERRATUM-SPEC020-002) |
| L-25 | SPEC-020 `checks.md` | zero no critério exato | sem mudança |
| L-26 | SPEC-021 `plan.md` (l.160) | "\| Fechar dimensões **classe B** da SPEC-020 \| **SPEC-007/038/014** (BL-017) \| DIFERIDAS; não antecipadas (CONS-01)" | mantida. **Não casa com o critério exato** (extensão m-11) |
| L-27 | SPEC-021 `plan.md` (l.762) | "- **Classe B da SPEC-020** (BL-017) — **DIFERIDA**; fecha em SPEC-007/038/014; não antecipada." | mantida. **Não casa com o critério exato** (extensão m-11) |
| L-28 | SPEC-038 `plan.md` (l.916) | "Nenhuma dimensão B de outro componente (RAG faithfulness ↔ SPEC-007; decision traceability ↔ SPEC-014) é tocada." (texto de proposta histórica, preservado no baseline) | mantida |

**Na mesma família, mas sem nenhum termo do critério (registros de gatilho do BL-017 ou do BL-010):**
- SPEC-002 `plan.md` "**BL-017** (`spec:SPEC-007/014/038 em redação`)";
- SPEC-003 `plan.md` "**BL-017** (`spec:SPEC-007/014/038 em redação`)";
- SPEC-005 `plan.md` "**BL-017** (dimensões B da SPEC-020) está `Em espera` (gatilho `spec:SPEC-007`/`spec:SPEC-014`)";
- SPEC-020 `plan.md` "gatilho `spec:SPEC-007/014/038 em redação`" e `checks.md` "(gatilho SPEC-007/014/038; não inclui SPEC-020)";
- SPEC-021 `plan.md` "gatilho `spec:SPEC-007/014/038 em redação`" e `checks.md` "(gatilho SPEC-007/014/038; não inclui SPEC-021)".

Esses trechos registram o gatilho do BL-017 como ele era na data de cada entrega. **SPEC-004**: nenhuma ocorrência em `plan.md` nem em `checks.md` (só no `research.md`, que fica fora do universo).

### 2.2 Critério 1: erratas homologadas

| # | Documento | Texto literal (âncora) | Desde 10-24 |
|---|---|---|---|
| L-29 | `governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md` (l.14) | "- **RAG faithfulness ↔ SPEC-007** e **decision traceability ↔ SPEC-014** permanecem **DIFERIDAS** (fecham nos pontos de dependência próprios)." | mantida |
| L-30 | `governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md` | 16 linhas casam (ex.: "F1: critério definido (componente-alvo SPEC-007 homologado). F2: segue DIFERIDA (SPEC-048)") | **NOVA** (o arquivo é de 2026-10-30) |
| L-31 | `specs/features/SPEC-006/errata-v1.13.md` | **zero** no critério exato. As menções a "SPEC-007" tratam de selo e formação (ex.: "ligação com o selo da SPEC-007 (E-1..E-4)") | **NOVA no universo**, sem ocorrência |
| L-32 | Demais `governance/ERRATUM-*` (SPEC001-001/002, SPEC005-001, SPEC019-001) | zero | sem mudança |

### 2.3 Removidas ou deslocadas

- **Removidas:** nenhuma. Todo texto da tabela de 10-24 continua presente e igual (INV-07).
- **Deslocadas:** nenhuma nos `plan.md` listados. Os números de linha da tabela de 10-24 conferem com os de hoje. O único arquivo que cresceu foi o `plan.md` da SPEC-020, que ganhou uma linha **ao final** (L-24). Em ROADMAP, nas atas e no SPEC-007 há números de linha defasados: ver seções 6 e 7.

---

## 3. JULGAMENTO: o que cada ocorrência trata (formação fica; recuperação re-aponta) `[INFERÊNCIA]`

Régua usada, tirada de DHR-SPEC007-002 §3 e DHR-SPEC007-004 P-14:
- **formação, selo, F1 e definição de origem-raiz** ⇒ ficam na SPEC-007;
- **busca/recuperação, evidência candidata (item do pacote), contagem de origens no pacote, entrega e F2** ⇒ vão à SPEC-048.

| Ocorrência | Assunto | Julgamento | Ação |
|---|---|---|---|
| L-01, L-02, L-03 | evidência candidata a partir de recuperação | só recuperação | **Nota N-A** |
| L-04, L-10, L-11, L-14, L-15 | "formação/retrieval" juntos | misto: formação fica, recuperação vai | **Nota N-B** |
| L-13 (ADV-CKG-08) | escopo: "extração/retrieval/validação" fora do KG | misto. A VERIFICAÇÃO ("a Spec não contém comportamento de formação/retrieval") **continua igual** | **Nota N-B** (endereço apenas) |
| L-05 (1ª parte), L-06, L-09 | recuperação, relevância, packet; "documento recuperado" | só recuperação | **Nota N-C** |
| L-05 (2ª parte), L-07, L-08 | COL-EXP-05 (fontes repetidas contam como uma) | dividido pela P-14 | **Nota N-D** |
| L-16 | COL-EXP-05, mesmo fato de L-07/L-08 | dividido pela P-14 | **Nota N-D**, se Andraus aceitar a extensão (Q-3) |
| L-12 | "formação é SPEC-007" | só formação | **Sem nota**: fica |
| L-17 | registro do gatilho do BL-010 | registro de estágio. O gatilho que vale hoje está no RMR-001, e o BL-010 já ganhou o acréscimo "∨ `spec:SPEC-048 em redação`" (DHR-SPEC048-001 Q-6) | **Sem nota** |
| L-19 a L-23 (SPEC-020) | dimensão B "RAG faithfulness" | dividida (F1 → SPEC-007; F2 → SPEC-048) | **Sem nota nova**: já coberta pelo ERRATUM-SPEC020-002 §2 (seção 5) |
| L-24 (SPEC-020) | ponteiro do ERRATUM-SPEC020-002 | já correto ("metade F2 (SPEC-048)") | **Sem nota** |
| L-29 (ERRATUM-SPEC020-001) | dimensão B | dividida | **Sem nota nova**: já coberta pelo ERRATUM-SPEC020-002 §3, "Nota sobre o ERRATUM-SPEC020-001" (seção 5) |
| L-30 (ERRATUM-SPEC020-002) | F1 e F2 já separados | correto | **Sem nota** |
| L-26, L-27 (SPEC-021) | classe B, com "SPEC-007" valendo pela RAG faithfulness | dividida | **Nota N-E**, se Andraus aceitar a extensão m-11 (Q-4) |
| L-28 (SPEC-038) | "RAG faithfulness ↔ SPEC-007" | dividida | **Nota N-E** |
| Registros de gatilho do BL-017 (2.1, fim) | estágio | registro datado | **Sem nota** (mesmo critério de "Registros de estágio preservados" do ERRATUM-SPEC020-002 §2) |

---

## 4. Texto das notas aditivas `[PROPOSTA]`

Regras comuns:
- cada nota se lê **junto** do trecho âncora e não o substitui;
- texto baselined não muda (INV-09);
- nenhuma nota cria obrigação.

**N-A** (SPEC-002, nos trechos L-01 e L-02; SPEC-003, no trecho L-03):
> *"Nota aditiva (ERRATUM-REAPONT-001): a evidência candidata a partir de recuperação (busca e pacote de evidência) é da **SPEC-048** (DHR-SPEC007-002 §3; baseline DHR-SPEC048-002; SPEC-048, 'Termo 1': evidência candidata = item do pacote). Formação e selo seguem na **SPEC-007**. A Evidência (CEM-001) continua produzida pelo agente. Texto acima não alterado (INV-09)."*

**N-B** (SPEC-006, nos trechos L-04, L-10, L-11, L-13, L-14 e L-15):
> *"Nota aditiva (ERRATUM-REAPONT-001): onde se lê 'formação/retrieval … SPEC-007', leia-se: **formação e selo → SPEC-007**; **recuperação (retrieval) → SPEC-048** (DHR-SPEC007-002 §3). O KG não absorve nenhuma das duas. No ADV-CKG-08, a VERIFICAÇÃO não muda (a Spec não contém comportamento de formação nem de recuperação). Texto acima não alterado (INV-09)."*

**N-C** (SPEC-006, nos trechos L-05 (1ª parte, "FORA → SPEC-007 (retrieval)"), L-06 e L-09):
> *"Nota aditiva (ERRATUM-REAPONT-001): recuperação, relevância e pacote (packet) são da **SPEC-048** (DHR-SPEC007-002 §3). O KG segue só com consulta read-only (RULE-CKG-011). A distinção 'documento recuperado ≠ conhecimento validado' não muda. Texto acima não alterado (INV-09)."*

**N-D** (SPEC-006, nos trechos L-05 (2ª parte), L-07, L-08 e, se aceita a Q-3, L-16):
> *"Nota aditiva (ERRATUM-REAPONT-001): COL-EXP-05 foi tratada na SPEC-007 ('Reconciliação COL-EXP-05'; DHR-SPEC007-003 P-6). Por decisão de Andraus (DHR-SPEC007-004 P-14): a **definição de 'mesma origem'** (origem-raiz) é da **SPEC-007** (RULE-KFH-001); a **contagem de origens independentes no pacote** é da **SPEC-048** (RULE-RET-003); a independência de **experiência** (EXP-SPEC-021) é da SPEC-009/SPEC-017 (G-001 segue ABERTA). O `CONFLICT-MAP.md` não é alterado por esta nota (só por ato de Andraus). BL-011 segue `ATIVADO`. Texto acima não alterado (INV-09)."*

**N-E** (SPEC-038, no trecho L-28; SPEC-021, nos trechos L-26 e L-27, se aceita a Q-4). A redação segue a do ERRATUM-SPEC020-002 §1.9 e a ajustada pela Q-5 (DHR-SPEC020-002 D1):
> *"Nota aditiva (ERRATUM-REAPONT-001): na classe B, a dimensão 'RAG faithfulness' divide-se (DHR-SPEC007-002 §4). A **metade F1** (conhecimento formado) é da **SPEC-007**, com critério definido pelo ERRATUM-SPEC020-002 (DHR-SPEC020-002). A **metade F2** (frase/item entregue) é da **SPEC-048** e segue DIFERIDA até a homologação do erratum à parte da metade F2. tool correctness: SPEC-038, encerrada pelo ERRATUM-SPEC020-001. decision traceability: SPEC-014, DIFERIDA. Esta nota só corrige endereço e não antecipa nenhuma dimensão B. Texto acima não alterado (INV-09)."*

---

## 5. SPEC-020 e ERRATUM-SPEC020-001: decisão de coordenação com o ERRATUM-SPEC020-002 `[INFERÊNCIA + PROPOSTA]`

**Decisão proposta: nenhuma nota nova nas linhas da SPEC-020 (L-19 a L-23) nem no ERRATUM-SPEC020-001 (L-29).** Quatro motivos:

1. **O endereço já foi corrigido por texto homologado.** O ERRATUM-SPEC020-002 (homologado, DHR-SPEC020-002 D1) traz no §2, "Leitura vigente", uma linha para cada um destes enunciados:
   - D0, "O que a Missão NÃO é" (= L-19);
   - D1, Non-goals (= L-20);
   - ADV-EV-06 (= L-21);
   - Riscos e Etiquetagem;
   - Lista final "[DECISÃO NECESSÁRIA] em aberto" (= L-22): "'fecha em SPEC-007' lê-se: **metade F1** (este erratum); metade F2 → SPEC-048 (DHR-SPEC007-002 §4)";
   - "Errata aditiva ao fim do plan.md" (= L-23): "F1: critério definido; F2: DIFERIDA (SPEC-048)".

   Para o ERRATUM-SPEC020-001, o §3 ("Nota sobre o ERRATUM-SPEC020-001") já dá a leitura: "a dimensão 'RAG faithfulness' divide-se em F1 (SPEC-007) e F2 (SPEC-048) …". `[FONTE]`
2. **Uma segunda nota duplicaria** o mesmo fato em dois lugares (P2, fato→locais), e as duas poderiam divergir numa correção futura.
3. **O "texto único" da SPEC-048 foi superado.** O texto que o Plan da SPEC-048 propôs para as cinco linhas (seção "Texto único por linha da SPEC-020") diz "F2: na homologação do Plan da SPEC-048". Isso **não aconteceu** (DHR-SPEC048-002 §3). Andraus aceitou o ajuste na homologação (ERRATUM-SPEC020-002 Q-5; DHR-SPEC020-002 D1). Reaplicá-lo agora **contradiria** o texto homologado. Esta errata não o usa. O texto da SPEC-048 continua como está (baseline, INV-09) e vale como registro de estágio.
4. **A metade F2 continua com erratum próprio.** Esta errata não define critério de F2, não mexe no ADV-EV-06 (que continua valendo para F2 e para decision traceability, ERRATUM-SPEC020-002 §1.9) e não fecha o BL-017.

**O que cabe à SPEC-020 nesta errata:** só **registrar**, na tabela fato→locais (seção 8), que o endereço da SPEC-020 está coberto pelo ERRATUM-SPEC020-002 §2 e §3, para que a próxima busca não o trate como pendente. Se Andraus preferir uma nota explícita mesmo assim, é a Q-5.

---

## 6. Critério 2: "SPEC-048" junto de WikiRAG / página de leitura `[LITERAL + INFERÊNCIA]`

**Resultado literal** (Spec baselined ou ata):
- `specs/features/SPEC-007/plan.md`: 12 linhas casam.
- `specs/features/SPEC-048/plan.md`: 3 linhas. A própria Spec registra a separação, então não é alvo.
- DHR-SPEC007-002, l.31: nota C-3 já aplicada.
- DHR-SPEC048-001: é a fonte da separação (Q-2).
- `ROADMAP.md`, l.184: nota C-3 já aplicada.
- DHR-SPEC048-002, linha "A SPEC-049 (WikiRAG Reading View) segue slot indicativo": já correta.

**Julgamento.**
- **SPEC-007.** A nota C-3 no topo do `plan.md` ("onde este Plan e o Anexo T dizem que a visão de leitura WikiRAG / a página de leitura \"vai à SPEC-048\" … leia-se: a página de leitura passa à **SPEC-049**") vale **pelo texto**, e o texto cobre todas as menções de hoje. Mas a lista de linhas dentro da nota, "(menções em l.63, 64, 71, 308, 319, 359, 443, 711, 1731, 1801 e no título do Anexo T)", **está defasada** em relação à v2.3 homologada. As menções de hoje estão em:
  - o campo ID ("Recuperação, pacote de evidência, WikiRAG e F2 passam à **SPEC-048**");
  - o campo de atas ("Q3: WikiRAG = versão de leitura por regra fixa — agora matéria da SPEC-048");
  - a linha de mapa "Recuperação + pacote com citação + independência no pacote + F2 + WikiRAG";
  - "juízo F2, compilação WikiRAG) e o gate de montagem/entrega do pacote são da SPEC-048";
  - "servi-los e exibi-los lado a lado (recuperação e WikiRAG) é requisito à SPEC-048";
  - "\"omitir da recuperação/WikiRAG\" foram à SPEC-048";
  - "EC-KFH-009 WikiRAG … foram à SPEC-048";
  - "*R-3, R-4, R-8 (relevância, falsa independência, WikiRAG)*";
  - "\"lado a lado na WikiRAG\" são da SPEC-048";
  - o título do Anexo T.

  Nada fica descoberto, porque a nota vale pelo texto. **Proposta opcional, nota N-F** (SPEC-007, junto da nota C-3): *"Nota aditiva (ERRATUM-REAPONT-001): os números de linha citados na nota C-3 são da versão de 2026-10-24 e não se aplicam à v2.3. A nota vale pelo texto ('onde este Plan e o Anexo T dizem…'), que cobre todas as menções. Texto acima não alterado (INV-09)."* Andraus decide (Q-6).
- **Atas.** A DHR-SPEC048-001 §2 cita "notas aditivas nas l.189/l.517" do ROADMAP. Hoje a nota de página de leitura do bloco SPEC-007 está na l.184. Ata não se edita (INV-07). Fica **só registrado**: a âncora textual ("Nota aditiva (DHR-SPEC048-001, C-3)") continua localizável.
- **Nada novo** em Spec baselined fora da SPEC-007.

---

## 7. Fora de errata de Spec: itens para o Orquestrador e para Andraus (não aplicados aqui)

| Local | Texto literal | Item |
|---|---|---|
| `ROADMAP.md` §12, linha das dimensões B | "RAG faithfulness (fecha em SPEC-007)" | Atualização aditiva sugerida: "RAG faithfulness: metade F1 com critério (ERRATUM-SPEC020-002, DHR-SPEC020-002); metade F2 → SPEC-048, DIFERIDA". Já estava listada como "não aplicado" na DHR-SPEC020-002 §4. Edição de ROADMAP é só por decisão de Andraus (AGENTS.md §10) |
| `ROADMAP.md`, caminho crítico | "006 Knowledge Graph → 007 RAG (fecha 020: RAG faithfulness) →" | Atualização aditiva sugerida: 007 fecha só a metade F1; a SPEC-048 entra no caminho para a metade F2. Mesma regra de edição |
| `ROADMAP.md`, linha da SPEC-045-RUNTIME-001 | (decisão ABERTA) | **Não tocar.** A decisão segue aberta (CONS-01) |
| `governance/CONFLICT-MAP.md` COL-EXP-05 | "→ **re-apontada à SPEC-007** (Andraus, 2026-10-19, DHR-BENCH-INTEL-001 D8 …)" | Re-apontamento **parcial** à SPEC-048 (contagem no pacote, P-14). **Só por ato de Andraus**. A SPEC-007 já registra isso ("o re-apontamento parcial de COL-EXP-05 à SPEC-048 no CONFLICT-MAP é ato de Andraus") |
| `governance/CONFLICT-MAP.md`, K-MAN da SPEC-020 | "(RAG faithfulness→SPEC-007; tool correctness→SPEC-038; decision traceability→SPEC-014) DIFERIDAS" | Também só por ato de Andraus |
| `backlog/RMR-001` | BL-010 e BL-017 já têm "∨ `spec:SPEC-048 em redação`" | **Nada a fazer.** Estados não mudam (só Andraus promove) |
| `governance/CATALOGO-OFICIAL.md` | n/a | Registrar esta errata **na homologação** (Orquestrador) |

---

## 8. Tabela fato → locais (P2)

Numa correção futura, corrigir **todos** os locais da linha.

| Fato | Locais nesta errata | Âncoras no baseline (não editadas) |
|---|---|---|
| Recuperação e evidência candidata → SPEC-048; formação e selo → SPEC-007 | §0; §3; N-A; N-B; N-C | L-01 a L-04, L-06, L-09 a L-11, L-13 a L-15; SPEC-048 "Termo 1"; DHR-SPEC007-002 §3 |
| COL-EXP-05: origem-raiz na SPEC-007 (RULE-KFH-001); contagem no pacote na SPEC-048 (RULE-RET-003); experiência na SPEC-009/017 | §3; N-D; §7 (CONFLICT-MAP) | L-05 (2ª parte), L-07, L-08, L-16; SPEC-007 "Reconciliação COL-EXP-05" itens 3 e 4; DHR-SPEC007-004 P-14 |
| RAG faithfulness: F1 → SPEC-007 (com critério); F2 → SPEC-048 (DIFERIDA até o erratum próprio) | §0; §3; §5; N-E; §7 (ROADMAP) | L-19 a L-24 e L-29 (cobertos pelo ERRATUM-SPEC020-002 §2/§3); L-26 a L-28; ERRATUM-SPEC020-002 §1.9 |
| Endereço da SPEC-020 coberto pelo ERRATUM-SPEC020-002 | §3; §5 | ERRATUM-SPEC020-002 §2 (tabela "Leitura vigente") e §3 ("Nota sobre o ERRATUM-SPEC020-001") |
| Página de leitura → SPEC-049 (critério 2) | §6; N-F | SPEC-007 nota C-3; ROADMAP nota C-3; DHR-SPEC007-002 §3 nota |
| Registros de gatilho (BL-010, BL-017) ficam sem nota | §2.1 (fim); §3 | L-17; linhas de gatilho do BL-017 em SPEC-002/003/005/020/021 |

---

## 9. Herança/Delta (CC-08; RULE-HD-02/03/04), obrigação a obrigação

- **INHERITS** (ID + versão):
  - DHR-SPEC048-001 Q-7 (regra de busca);
  - DHR-SPEC007-002 §3/§4 (fronteira e lista de re-apontamentos);
  - DHR-SPEC007-004 P-14 (COL-EXP-05);
  - SPEC-048 v1.4 (BASELINE, DHR-SPEC048-002): "Termo 1", RULE-RET-001/003/004;
  - SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005): RULE-KFH-001, "Reconciliação COL-EXP-05";
  - ERRATUM-SPEC020-002 (DHR-SPEC020-002): §1.9, §2, §3, Q-5;
  - ERRATUM-SPEC020-001 (DHR-SPEC038-002);
  - SPEC-006 (BASELINE + erratas até v1.13): RULE-CKG-011, ADV-CKG-08;
  - padrão de forma: ERRATUM-SPEC019-001 (aditivo e editorial) e "arquivo à parte + uma linha" (DHR-SPEC020-002 D4; DHR-RETRO-001 §4 Q-8).
- **ADDED:** notas N-A a N-E (e N-F, se a Q-6 for aceita), que são só leitura de endereço; tabela fato→locais.
- **MODIFIED:** nenhum.
- **REMOVED:** nenhum.

| Obrigação herdada | Onde esta errata a cumpre |
|---|---|
| Q-7: aplicar a regra de busca "na hora de ser escrita" | §1 e §2 (busca refeita em 2026-10-30, com comparação) |
| DHR-SPEC007-002 §4: "As referências ao contrato do selo e à formação continuam na SPEC-007" | §3 (L-12 sem nota; N-B separa formação de recuperação; L-31, a errata v1.13, sem nota) |
| DHR-SPEC007-002 §4: a dimensão B "se divide" | §5 e N-E |
| DHR-SPEC007-004 P-14: definição na SPEC-007, contagem na SPEC-048 | N-D |
| DHR-SPEC007-002 §6 e SPEC-007 "Reconciliação" item 5: CONFLICT-MAP só por ato de Andraus | §0; N-D; §7 |
| DHR-SPEC048-002 §3: F2 é passo à parte | §0; §5 item 4; N-E ("DIFERIDA até … erratum à parte") |
| ERRATUM-SPEC020-002 Q-5: redação ajustada para F2 | §5 item 3; N-E |
| ERRATUM-SPEC020-002 §8: "Re-apontamentos em SPEC-021/SPEC-038 … são da errata de re-apontamento" | N-E (SPEC-038; SPEC-021 pela Q-4) |
| INV-07 / INV-09: baseline e atas não são editados | cabeçalho; §6 (atas); todas as notas terminam com "Texto acima não alterado" |
| SPEC-006 ADV-CKG-08: a VERIFICAÇÃO de escopo | N-B (declara que a VERIFICAÇÃO não muda) |
| SPEC-006 RULE-CKG-011 (KG só consulta read-only) | N-C (mantida) |
| CEM-001 / INV-06: a Evidência é do agente | N-A (mantida) |

Nenhuma obrigação herdada foi removida ou enfraquecida. `[INFERÊNCIA: o Revisor confere]`

---

## 10. Constitution Check (CC-01..CC-12): só o que a errata toca

| CC | Resultado | Por quê |
|---|---|---|
| CC-01 | PASS | Hierarquia intocada. Nenhuma hipótese |
| CC-02 | PASS | Não redefine CEM/CHM/CCM/CDM/CNM. N-A **reafirma** que a Evidência é do agente |
| CC-03 | PASS | Nenhum campo de convicção. J-001 intocada |
| CC-04 | PASS | Nenhuma Salvaguarda tocada |
| CC-05 | PASS | LOW declarado e justificado (cabeçalho; Q-7) |
| CC-06 / CC-07 | N/A | Não é Engineering Card |
| CC-08 | PASS | Seção 9, obrigação a obrigação |
| CC-09 | PASS | Literal separado de julgamento; extensões marcadas `[INFERÊNCIA]`; nenhum número |
| CC-10 | PASS | "evidência candidata" ≠ "Evidência" (SPEC-048 "Termo 1"); F1 ≠ F2 (ERRATUM-SPEC020-002 §3) |
| CC-11 | N/A | Nenhuma BASpec com efeito |
| CC-12 | N/A | Meta-harness, sem escola |

---

## 11. §7-bis (voluntário em LOW)

**Bloco A.**
- *Se a errata estivesse errada, o que se veria?*
  - (1) Uma nota mandando à SPEC-048 algo de **formação** (ex.: L-12). Observável comparando com DHR-SPEC007-002 §3.
  - (2) Uma nota na SPEC-020 que contradiz o ERRATUM-SPEC020-002 (ex.: "F2 na homologação do Plan"). Evitado pela §5.
  - (3) Uma nota lida como fechamento da F2 ou do BL-017. Evitado em N-E ("segue DIFERIDA").
  - (4) Uma ocorrência que casa com o critério exato e ficou sem decisão. Conferível refazendo a busca da §1.
- *O ENTÃO é verificável por terceiro?* A parte literal, sim (§1 é reproduzível). O julgamento formação × recuperação depende do Revisor e de Andraus. Está declarado como `[INFERÊNCIA]`.
- *Existe QUANDO satisfeito sem que o ENTÃO deva acontecer?* Sim, e está coberto: L-12 (formação), L-17 e os gatilhos do BL-017 (registros de estágio), L-24, L-30 e L-31 (já corretos), SPEC-020 e ERRATUM-SPEC020-001 (já cobertos). Nesses casos a busca casa e não há nota.

**Bloco C.** Não há afirmação causal nem número. Premissa que pode estar errada: que Dossiê e ABERTURA não são "Spec baselined". O critério é o mesmo de 10-24 e o Revisor pode contestar.

**Bloco D.** A errata não executa nada (INV-05). As dependências de Andraus estão nas perguntas da §15.

---

## 12. Análise de impacto (RULE-HG-04) e compatibilidade proposta

| Alvo | Impacto |
|---|---|
| Schemas | Nenhum |
| RAG / KG | Nenhum comportamento. Só endereço |
| Skills | Nenhuma |
| Testes | Nenhum teste nem script novo |
| Modelos dependentes | SPEC-002/003/006/038 (e SPEC-021, SPEC-007 se as Q-4/Q-6 forem aceitas): uma linha de ponteiro no fim do `plan.md` (§13); nenhum enunciado muda. SPEC-020 e ERRATUM-SPEC020-001: nada (cobertos). ROADMAP e CONFLICT-MAP: §7, fora desta errata |
| Obrigações | **Nenhuma nova**, para nenhuma Spec nem para o Revisor |

**Compatibilidade proposta: Patch (editorial)**, a decidir por Andraus (Q-2). `[PROPOSTA]`
- *A favor de Patch:*
  - nenhuma regra, obrigação, estado ou critério muda;
  - nada que passava passa a reprovar, e vice-versa;
  - o conteúdo (quem faz o quê) **já foi decidido** por DHR-SPEC007-002, DHR-SPEC007-004 e DHR-SPEC048-002, e a errata só leva o endereço aos textos antigos;
  - precedente: ERRATUM-SPEC019-001, "**Patch / editorial** (nenhum objeto removido ou reescrito)".
- *A favor de Minor (para Andraus pesar):* toca várias Specs ao mesmo tempo e muda o **endereço** de dependências em seções de fronteira (Non-goals, tabelas de fronteira). As homologações de 10-24 e 10-30 desta família foram Minor (DHR-SPEC007-002; DHR-SPEC020-002). A diferença: aquelas decidiram conteúdo (divisão; critério F1), e esta não decide conteúdo nenhum. `[INFERÊNCIA]`

---

## 13. Forma de aplicação (depois da homologação) `[PROPOSTA]`

Mesmo padrão da DHR-SPEC020-002 D4 e da Q-8 da errata v1.13 da SPEC-006: **este arquivo é a errata**, e cada `plan.md` afetado recebe **uma linha de ponteiro** no fim. `checks.md` não é editado. Texto proposto para a linha (o Orquestrador preenche a data e a ata no ato):

> **Errata aditiva (data da homologação, ata a atribuir):** re-apontamento de endereço (recuperação/evidência candidata/pacote → SPEC-048; formação e selo seguem na SPEC-007) — ver `governance/ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md`, notas N-x. Texto acima não alterado (INV-09).

Alvos da linha:
- SPEC-002 (N-A);
- SPEC-003 (N-A);
- SPEC-006 (N-B, N-C, N-D);
- SPEC-038 (N-E);
- SPEC-021 (N-E), se a Q-4 for aceita;
- SPEC-007 (N-F), se a Q-6 for aceita.

**Não recebem linha:** SPEC-020 e ERRATUM-SPEC020-001 (§5).

Alternativa: uma errata por Spec, como dizia a proposta de 10-24 ("uma errata por Spec"). Fica na Q-1.

---

## 14. O que NÃO muda (CONS-01)

- **Permanecem ABERTAS**, conforme o `ROADMAP.md`, linha "Decisões abertas ativas" (nenhuma é fechada aqui): J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WORKFLOW-SOT-001 (residual: só WF-D03). `[FONTE]`
- **Também abertas, registradas em ata:** CKG-STRUCT-ORIGIN-001 (BL-035) e "produtor/gatilho de promoção" `[FONTE: DHR-SPEC048-002 §5; DHR-SPEC020-002 §5]`; o mecanismo da autenticação dos atos de Andraus `[FONTE: ROADMAP "Decisões FECHADAS", item "Autenticação dos atos de Andraus": "o MECANISMO … segue ABERTO"]`.
- A divisão usada aqui é a SPEC-007-SPLIT-001, que o ROADMAP lista em "Decisões FECHADAS" (DHR-SPEC007-002). Esta errata **aplica** essa decisão e não a reabre.
- BL-011 segue `ATIVADO`; BL-010 e BL-017 seguem `Em espera`. O BL-017 não fecha (faltam F2 e decision traceability). Esta errata não promove nada.
- A metade F2 continua num erratum à parte, que não é este.
- CONFLICT-MAP e ROADMAP: §7.

---

## 15. Perguntas para Andraus (cada uma com recomendação)

| # | Pergunta | Recomendação |
|---|---|---|
| Q-1 | Forma e número: **um** arquivo de errata entre Specs (ERRATUM-REAPONT-001) com uma linha de ponteiro em cada `plan.md` afetado, **ou** uma errata por Spec? | **Um arquivo.** O fato é um só, vem de uma só busca e fica numa só tabela fato→locais. Confirmar ou trocar o código |
| Q-2 | Compatibilidade: Patch ou Minor? | **Patch (editorial)**, pela §12 |
| Q-3 | Incluir L-16 (SPEC-006, "(3) dup. … ADIADA a SPEC-007/009 (COL-EXP-05)") na nota N-D? A linha não casa com o critério exato | **Sim.** É o mesmo fato de L-07 e L-08, no mesmo Plan. Deixá-la fora deixaria endereços diferentes para um fato só |
| Q-4 | Estender o critério à SPEC-021 (L-26, L-27: "classe B … SPEC-007/038/014", sem "RAG faithfulness" na linha; extensão m-11)? | **Sim.** O ERRATUM-SPEC020-002 §8 mandou os re-apontamentos da SPEC-021 para esta errata, e "classe B" contém RAG faithfulness (SPEC-020, D0) |
| Q-5 | SPEC-020 e ERRATUM-SPEC020-001: aceitar "sem nota nova, coberto pelo ERRATUM-SPEC020-002 §2/§3" (§5)? | **Sim.** Nota nova duplicaria, e o "texto único" da SPEC-048 foi superado pela Q-5 do ERRATUM-SPEC020-002 |
| Q-6 | Pôr a nota N-F na SPEC-007 (números de linha defasados dentro da nota C-3)? | **Opcional; recomendo sim.** Custo de uma linha, e evita que alguém leia a lista de linhas como exaustiva |
| Q-7 | Complexidade LOW (D0–D3) para esta errata? | **Sim.** Não há comportamento nem efeito. Se preferir MEDIUM, o texto não muda |
| Q-8 | Itens da §7 (ROADMAP §12 e caminho crítico; CONFLICT-MAP COL-EXP-05 e K-MAN da SPEC-020): ordenar a atualização aditiva junto com a homologação desta errata? | **Sim para o ROADMAP**, na mesma homologação (o Orquestrador edita, preservando o texto anterior). **CONFLICT-MAP**: ato seu, quando quiser; recomendo junto, para não deixar COL-EXP-05 com endereço único |

Pronto para revisão.
