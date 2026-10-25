# SPEC-006 — Errata v1.13 (ADITIVA) — ligação com o selo da SPEC-007 (E-1..E-4)

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-006 — Cognitive Knowledge Graph (HOMOLOGADA — BASELINE v1.7 + errata v1.11 [DHR-SPEC006-003] + errata v1.12 [DHR-SPEC006-004]). **Texto baselined NÃO é editado por esta errata** (INV-07/INV-09): `specs/features/SPEC-006/plan.md` e `specs/features/SPEC-006/checks.md` ficam como estão até a homologação; este arquivo é a errata inteira. |
| Natureza | **PROPOSTA de errata aditiva** — aguarda Revisor e homologação de Andraus. Não é baseline (INV-09). Nada nela vale antes da homologação. |
| Ordem | DHR-RETRO-001 §1 "Próxima frente" item (1) e §2 ("uma de cada vez, nesta ordem, cada uma com Revisor e homologação própria de Andraus. Nenhum baseline é editado antes da homologação da respectiva errata") `[FONTE — FATO NORMATIVO: decisão de Andraus registrada em ata]` |
| Origem do conteúdo | `specs/features/SPEC-007/plan.md` v2.3 (BASELINE, DHR-SPEC007-005), seção "Proposta de errata aditiva à SPEC-006", itens E-1..E-4; riscos RU-3 e RU-8 (§7-bis Bloco C, RULE-UNC-01); DHR-SPEC007-003 linha P-1; DHR-SPEC007-004 linha P-13; DHR-SPEC007-005 H-2; DHR-SPEC007-002 §3/§4 `[FONTE]` |
| Base auditável | O plan.md da SPEC-006 homologado na v1.12 tem sha256 registrado na DHR-SPEC006-004 §2 (`dd5a609f…`). **O Especificador não tem Bash e não recalculou o hash atual** — o Orquestrador deve conferir se o arquivo atual ainda é esse; se não for, as âncoras de texto abaixo continuam valendo (P3), mas a divergência deve ser informada ao Revisor. |
| Âncoras | **Por ID + texto literal entre aspas, nunca por número de linha** (alinhado à proposta P3 — ainda proposta a especificar, DHR-RETRO-001 §1). Números de linha que aparecem em citações da SPEC-007 (ex.: "l.482", "l.1415") são do texto de origem e só ajudam a localizar; a âncora que vale é o texto. |
| Complexidade | CRITICAL (a da SPEC-006; não muda) · profundidade D0–D7 + D8 focado · profile standard + adversarial. Esta errata toca só o caminho (b) de admissão (RULE-CKG-010) e o esquema do registro. |
| Compatibilidade proposta | **A decidir por Andraus.** E-1, E-2 e E-4 só acrescentam; **E-3 restringe** (o KG passa a recusar registro selado que hoje aceitaria). Precedente: a errata v1.11, também restritiva, foi classificada **Major** por Andraus (DHR-SPEC006-003 D3). `[INFERÊNCIA]` |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Data | 2026-10-25 |

---

## 0. O que esta errata faz, em uma frase

Hoje a SPEC-006 diz "o selo da SPEC-007 é uma dependência ainda não decidida". A SPEC-007 já foi homologada e definiu o selo. Esta errata **liga as duas pontas**: registra o que Andraus já decidiu sobre a lista de quem grava (E-1), aponta o formato do selo (E-2), faz o KG **conferir o selo** ao gravar (E-3) e dá ao registro do KG um lugar para o **conteúdo formado e a marca de inferência** (E-4). `[INFERÊNCIA — resumo]`

**Não faz:** não decide quem hospeda o juízo CKG-008; não fecha K-001 nem outra decisão aberta; não muda regra, BASpec, EARS, EC, cenário ou ADV no mérito existente; não cria ID novo de RULE/BASpec/EC/T/ADV; não edita o plan.md da SPEC-006 nem o da SPEC-007. `[FONTE: DHR-RETRO-001 §2-§3; DHR-SPEC007-005 H-2]`

---

## E-1 — Lista de quem grava (parte da RULE-CKG-009 decidida pela P-1)

**Âncora (RULE-CKG-009, última frase antes de `[Fonte:`):** "allowlist de escritores e quem hospeda o juízo CKG-008 = [DECISÃO NECESSÁRIA] (runtime; K-001/SPEC-018)." `[FONTE: specs/features/SPEC-006/plan.md, RULE-CKG-009 — FATO NORMATIVO (baseline)]`

**Fato de origem:** a DHR-SPEC007-003, linha P-1, diz: "**Decide parte de `SPEC-006 plan.md` l.482** (quem mantém a lista de quem grava); a governança do aprender-sozinho (K-001) segue ABERTA". `[FONTE — FATO NORMATIVO: decisão de Andraus em ata]`

**Texto aditivo proposto (acrescentado após a âncora, sem alterar a frase baselined):** `[PROPOSTA]`

> *[Errata v1.13 — E-1]* A frase acima tem dois itens. **Item (1) "quem mantém a allowlist de escritores": decidido por Andraus (DHR-SPEC007-003 P-1) — a lista de quem grava é aprovada por Andraus.** No caminho (b) da RULE-CKG-010 (conhecimento formado via selo), essa lista é a **lista de emissores do selo** da SPEC-007 (ato `ISSUER_LIST`, RULE-KFH-020; RULE-KFH-007 (iii)); a escrita no KG continua sob a RULE-CKG-009, feita pelo committer do KG (`computed_by` ≠ `writer_id` — RULE-CKG-005). A lista de emissores é regra LOCAL da SPEC-007, análoga à RULE-CKG-009, e **não** redefine os escritores do caminho (a). **Item (2) "quem hospeda o juízo CKG-008": segue [DECISÃO NECESSÁRIA]** (não é o juiz de fidelidade da SPEC-007). **K-001 segue ABERTA.**

**O que NÃO está decidido e continua aberto** `[DECISÃO NECESSÁRIA]`:
- a **composição concreta** da lista de escritores do caminho (a) (ciclo de vida canônico) e das identidades de committer — P-1 decidiu **quem aprova** a lista, não **quem está nela**; a SPEC-006 D6 ("concreta** de escritores = **[DECISÃO NECESSÁRIA]** (runtime; K-001/SPEC-018)") continua valendo; se Andraus quiser que a errata cubra também o caminho (a), isso é decisão dele na homologação (Pergunta Q-1);
- o **host do juízo CKG-008** (RULE-CKG-008/009);
- **K-001** (governança de runtime / aprender sozinho);
- o **mecanismo** da assinatura dos atos de Andraus (o princípio — assinatura criptográfica com chave em dispositivo dele — está decidido na DHR-SPEC007-007; o mecanismo segue aberto para a construção). `[FONTE: ROADMAP "Decisões FECHADAS", item "Autenticação dos atos de Andraus"]`

**Por que é aditivo:** a frase baselined fica intacta; a nota só registra uma decisão já tomada em ata e separa o decidido do aberto. `[INFERÊNCIA]`

---

## E-2 — Formato do selo (`seal_ref`)

**Âncoras (todas dizem que o contrato do selo ainda não existe):** `[FONTE: specs/features/SPEC-006/plan.md]`
- (a) I/O Schema, `node_record.publication`: `"seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]"`;
- (b) RULE-CKG-010: "(contrato do selo = DEPENDÊNCIA da SPEC-007 = [DECISÃO NECESSÁRIA])";
- (c) D6, 1º item: "(b) formado com selo SPEC-007 (contrato = [DECISÃO NECESSÁRIA])";
- (d) Etiquetagem: "| Contrato do selo de publicação | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007** |";
- (e) lista final de abertas: "**Contrato do selo de publicação** — dependência da **SPEC-007**; [DECISÃO NECESSÁRIA].";
- (f) Autopré-check: "selo SPEC-007 marcado [DECISÃO NECESSÁRIA]";
- (g) `checks.md`, "Itens em aberto": "selo de publicação (SPEC-007);".

**Fato de origem:** a SPEC-007 v2.3 está **homologada** (DHR-SPEC007-005) e a RULE-KFH-007 (ix) define: "o registro submetido = registro materializado + `publication.origin = spec007_seal` + `publication.seal_ref = seal_id@seal_version` (+ `supersedes`/`version`/`expected_version` se sucessora) — esses campos ficam FORA do `record_hash`". O selo (`publication_seal`) traz `seal_id`, `seal_version`, `material_hash`, `sealed_records[{record_ref, record_kind, record_hash}]`, `succession_of[]?` e demais campos (SPEC-007 esquema `publication_seal`). `[FONTE — FATO NORMATIVO]`

**Texto aditivo proposto (uma nota, válida para as sete âncoras):** `[PROPOSTA]`

> *[Errata v1.13 — E-2]* **Dependência satisfeita:** o contrato do selo é o da SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005), RULE-KFH-007 (ix): `publication.seal_ref = seal_id@seal_version`, apontando um `publication_seal` da SPEC-007; `publication.origin = spec007_seal` continua DERIVADO do canal/identidade autenticada (não do payload). A SPEC-006 **não redefine** o selo — só o referencia (CC-02). Onde o texto acima diz "contrato do selo = [DECISÃO NECESSÁRIA]", leia-se "contrato do selo = SPEC-007 RULE-KFH-007 (ix)". A conferência do selo pelo KG é a E-3.

**E-2(b) — achado desta redação: registro de RELAÇÃO não tem campo `publication`** `[INFERÊNCIA — achado]` `[PROPOSTA]`
- O esquema da SPEC-006 põe `publication {origin, seal_ref}` **só** no `node_record`; o `relation_record` não tem esse campo (âncora: I/O Schema, bloco `"relation_record": {` — os campos vão de `relation_id` a `similarity_basis`, sem `publication`).
- A SPEC-007 sela também relações (RULE-KFH-007 (vii): "relação CAUSA ou SIMILAR_A DEVE trazer os campos da RULE-CKG-008") e diz que o registro submetido usa "campos do node_record/relation_record da SPEC-006, NÃO redefinidos" (SPEC-007 esquema "registro submetido"). `[FONTE]`
- **Proposta aditiva:** acrescentar ao `relation_record` o mesmo bloco opcional `publication {origin: "canonical_lifecycle | spec007_seal" (derivado do canal), seal_ref}`, com a mesma semântica do `node_record`.
- **Se Andraus não aprovar a E-2(b):** a E-3 só cobre nós; para relações o risco RU-3 **continua aberto** e a contenção segue sendo a auditoria amostral da SPEC-007 (EC-KFH-004). Isto está além do texto E-1..E-4 da SPEC-007 — é **Pergunta Q-2**.

---

## E-3 — O KG confere o selo ao gravar (fecha RU-3)

**Âncoras:** `[FONTE: specs/features/SPEC-006/plan.md]`
- RULE-CKG-010: "Formado SEM selo é REJEITADO (`FORMED_WITHOUT_SEAL`)";
- BASpec-CKG-010, MECANISMO: "(b) gate (selo SPEC-007 presente)";
- EC-CKG-001, PRECOND: "∨ selo SPEC-007 — CKG-010)";
- D4, item "Admissão (CKG-010)": "`admite(x) sse (x formado ∧ selo SPEC-007) ∨";
- §D3.1, linha "| `ADMISSION_REJECTED` | `FORMED_WITHOUT_SEAL`,".

**Problema (RU-3):** hoje o KG só verifica que o selo **está presente**. A SPEC-007 registra o risco: "o KG hoje aceita registro com `publication.origin = spec007_seal` de escritor autorizado SEM conferir `seal_ref`/hash; um committer autorizado que contorne o pipeline gravaria formado não selado, ou com conteúdo trocado, com rótulo de selado" (RULE-KFH-007 (ix); §7-bis RU-3). `[FONTE — FATO NORMATIVO (baseline SPEC-007)]`

**Texto aditivo proposto — cláusula nova da RULE-CKG-010, caminho (b), sem ID novo:** `[PROPOSTA]`

> *[Errata v1.13 — E-3] Conferência do selo no committer (caminho (b)).* Ao receber registro (nó ou, se a E-2(b) for aprovada, relação) com `publication.origin = spec007_seal`, o committer do KG, **antes de gravar** e sob a RULE-CKG-009, DEVE, nesta ordem, parando no primeiro que falhar:
> 1. **resolver `publication.seal_ref`** para um `publication_seal` existente da SPEC-007 (leitura read-only do registro de selos) — `seal_ref` ausente, mal formado ou que não resolve ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_REF_UNRESOLVABLE`; **registro de selos indisponível ⇒ mesma recusa (fail-closed; nunca grava "por confiança")**;
> 2. **achar o registro no selo:** o `record_ref` do registro recebido DEVE constar de `sealed_records[]` desse selo — senão ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_REF_UNRESOLVABLE`;
> 3. **recalcular o hash:** calcular `record_hash` = H(canon(M(r))) do registro recebido **pela serialização única da RULE-KFH-005 da SPEC-007** (a MESMA função canon/H — uma só, codificação de bytes = BUILD), sobre a projeção M, isto é, **excluindo tudo o que M exclui**: `publication.*` (incl. `seal_ref`), `supersedes`/`version`/`expected_version`, IDs atribuídos pelo KG, `writer_id`, `computed_by` e carimbos de tempo; e comparar com o `record_hash` daquele `record_ref` em `sealed_records[]` — diferente ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_CONTENT_MISMATCH`;
> 4. **[E-3(c) — ver Pergunta Q-3] conferir a sucessão:** se o registro recebido traz `supersedes`, o alvo DEVE ser igual ao par `record_ref → published_ref@version` declarado em `succession_of[]` do mesmo selo; registro com `supersedes` não declarado no selo ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_CONTENT_MISMATCH`.
>
> Passadas as conferências, valem as demais regras de escrita sem mudança (RULE-CKG-001/005/008/009/012/013). Recusa não grava nada; o registro recusado e o motivo ficam no log (EC-CKG-001 FAILURE-MODE). A SPEC-006 não calcula `material_hash`, não reexecuta a validação F1 e não julga fidelidade: **só confere identidade de conteúdo** contra o selo (ENF-03 — gate determinístico).

**Notas de precisão** `[INFERÊNCIA]`:
- **Lista de exclusão completa.** O texto E-3 da SPEC-007 diz "sem `publication.*` e sem campos de sucessão". A definição de M na RULE-KFH-005 exclui também IDs do KG, `writer_id`, `computed_by` e carimbos de tempo. Como o committer acrescenta `writer_id` e o KG atribui IDs e `recorded_at`, conferir só "sem publication.* e sucessão" daria divergência falsa em todo registro. A cláusula acima usa a lista de M (fonte única), sem mudar a SPEC-007.
- **Por que a E-3(c) (item 4).** Os campos de sucessão ficam **fora** do `record_hash` (RULE-KFH-007 (ix)). Sem o item 4, um committer que contorne o pipeline poderia pegar conteúdo selado e validado e pendurar um `supersedes` que Andraus não autorizou. Isso violaria SPEC-007-SUCC-001 ("só Andraus autoriza troca de carimbado, por lote" — ROADMAP "Decisões FECHADAS"), e a RULE-CKG-012 não percebe, porque só confere a ordem das versões. Este item **vai além** do texto E-3 da SPEC-007; por isso é a Pergunta Q-3. Se Andraus não o aprovar, o risco fica declarado como residual (ver §7-bis Bloco C).
- **Repetição do mesmo registro selado** (replay de conteúdo idêntico): a RULE-CKG-012 já trata ("Reescrita idêntica = no-op"). Exigir que o consumo do selo ainda esteja `RESERVADO` seria mais forte, mas é decisão de Andraus (Pergunta Q-4); não entra no texto proposto.
- **Códigos:** `SEAL_CONTENT_MISMATCH` é **o mesmo código** da SPEC-007 RULE-KFH-007 (ix), com o mesmo sentido, agora também do lado do KG; `SEAL_REF_UNRESOLVABLE` é **subcódigo novo** `[PROPOSTA]` sob o pai existente `ADMISSION_REJECTED` (§D3.1). Nenhum pai novo é criado (Pergunta Q-5).

**Texto aditivo proposto — notas de propagação por referência (a regra fica definida UMA vez, na RULE-CKG-010 acima):** `[PROPOSTA]`
- BASpec-CKG-010, MECANISMO, depois de "(b) gate (selo SPEC-007 presente)": *"[v1.13 — E-3] e conferido pelo committer (RULE-CKG-010, conferência do selo)"*.
- EC-CKG-001, PRECOND, depois de "∨ selo SPEC-007 — CKG-010)": *"[v1.13 — E-3] (selo conferido: seal_ref resolve ∧ record_ref ∈ sealed_records ∧ record_hash recalculado = selado [∧ supersedes ∈ succession_of, se Q-3 aprovada])"*.
- D4, item "Admissão (CKG-010)", depois de "(x formado ∧ selo SPEC-007)": *"[v1.13 — E-3] ∧ selo_conferido(x)"*.
- §D3.1, linha `ADMISSION_REJECTED`: acrescentar *"`SEAL_REF_UNRESOLVABLE` (v1.13 — E-3), `SEAL_CONTENT_MISMATCH` (v1.13 — E-3; código da SPEC-007)"*.

### Enforcement Contract — delta da E-3 sobre o EC-CKG-001 (o EC continua um só; nível não muda)
```
CAPABILITY   : Gravar no KG permanente registro formado vindo do selo da SPEC-007 (caminho (b))
EFFECT       : Commit crítico/irreversível de conhecimento formado (append-only)
PRECOND      : PRECOND vigente do EC-CKG-001 AND, se publication.origin = spec007_seal:
               seal_ref resolve para publication_seal existente AND record_ref ∈ sealed_records[] AND
               H(canon(M(r))) do registro recebido == record_hash selado (RULE-KFH-005) AND
               [Q-3 aprovada] supersedes presente ⇒ par declarado em succession_of[] do selo
POSTCOND     : só é gravado registro formado cujo conteúdo é idêntico ao validado e selado; o registro gravado
               mantém publication.seal_ref, permitindo a cadeia de auditoria até o selo (SPEC-007 D9)
POLICY       : RULE-CKG-009/010 (+ cláusula E-3); SPEC-007 RULE-KFH-005/007 (ix), INV-KFH-01; atomic-spec §10.2
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo"; irreversível) — igual ao vigente
FAILURE-MODE : Fail-closed — selo que não resolve, registro ausente do selo, hash diferente, sucessão não declarada
               [Q-3] ou registro de selos indisponível ⇒ ADMISSION_REJECTED (SEAL_REF_UNRESOLVABLE /
               SEAL_CONTENT_MISMATCH); nada gravado; log. Falso-DENY E3 por amostragem (ENF-07; limiar = gap aberto)
EVIDENCE     : por recusa: seal_ref, record_ref, record_hash recalculado × selado, código; por aceite: record_hash
               recalculado gravado junto do log de commit; amostragem de falso-DENY (ENF-07)
```
**Classe/Mecanismo (CC-11, da BASpec-CKG-010, que não muda):** C (Constitutivo) — gate determinístico de igualdade de hash e pertença; LLM não participa; GATE DE SAÍDA = as 3 (ou 4) conferências; CRITÉRIO 4Es: Conformidade > Eficácia — conteúdo trocado na memória permanente é irreversível; o custo de um hash por registro não rebaixa o nível (Economicidade nunca acima de Eficácia). `[INFERÊNCIA]`

### Casos de verificação — letras novas em cenários/ADV que já existem (contagens não mudam) `[PROPOSTA]`
Ponto de partida comum: nó `learning` N1 materializado por M, selado no selo S@1 com `sealed_records = [{N1, creation, h1}]`; committer autorizado e autenticado; demais pré-condições do EC-CKG-001 satisfeitas.
- **Cenário-CKG-T09 (d) — positivo:** **DADO** N1 com `publication.origin = spec007_seal`, `seal_ref = S@1`, conteúdo igual ao selado; **QUANDO** o committer grava; **ENTÃO** admitido; **VERIFICAÇÃO** `seal_checked == true`; `recomputed_record_hash == "h1"`; `admitted == true`.
- **ADV-CKG-21 (i):** `seal_ref` ausente ou `S@9` inexistente ⇒ `SEAL_REF_UNRESOLVABLE`; **VERIFICAÇÃO** `written == false`.
- **ADV-CKG-21 (j):** `seal_ref = S@1`, mas o registro tem `record_ref = N2` (fora de `sealed_records`) ⇒ `SEAL_REF_UNRESOLVABLE`; `written == false`.
- **ADV-CKG-21 (k) — conteúdo trocado:** `seal_ref = S@1`, `record_ref = N1`, texto de conteúdo alterado ⇒ hash ≠ h1 ⇒ `SEAL_CONTENT_MISMATCH`; `written == false`.
- **ADV-CKG-21 (l) — marca de inferência apagada (liga com E-4):** como (k), mas só `formation.formed_inference_claim_ids` esvaziado ⇒ hash ≠ h1 ⇒ `SEAL_CONTENT_MISMATCH`; `written == false`.
- **ADV-CKG-21 (m) — QUANDO se cumpre, mas a recusa NÃO deve ocorrer:** N1 idêntico ao selado, diferindo só em campos fora de M (`writer_id`, `recorded_at`, `publication.seal_ref` válido) ⇒ **admitido** (não há falsa recusa); `recomputed_record_hash == "h1"`; `false_deny == false`.
- **ADV-CKG-21 (n) — [só se Q-3 aprovada]:** N1 idêntico ao selado, com `supersedes = KG-N-X@2` não declarado em `succession_of[]` de S@1 ⇒ `SEAL_CONTENT_MISMATCH`; `written == false`.
- **ADV-CKG-21 (o) — registro de selos indisponível:** ⇒ `SEAL_REF_UNRESOLVABLE` (fail-closed); `written == false`; `fail_closed == true`.

**Efeito sobre RU-3:** com a E-3 aprovada, RU-3 **fecha para nós**; para relações, só se a E-2(b) também for aprovada. O risco que sobra é de **implementação**: um committer que não rode a conferência. Isso é falha de BUILD E3, detectada pela auditoria amostral da SPEC-007 (EC-KFH-004 (ii)), que continua ativa. `[INFERÊNCIA]`

---

## E-4 — Bloco `formation` no registro do KG (reduz RU-8)

**Âncora:** I/O Schema, `node_record` — os campos vão de `"node_id"` a `"recorded_at"`; não há campo para o **conteúdo** materializado por M nem para `formed_inference_claim_ids[]`. `[FONTE: specs/features/SPEC-006/plan.md]`

**Fato de origem:** pela RULE-KFH-005, M produz "campos de CONTEÚDO := texto EXATO das afirmações de `content_claim_ids[]`, na ordem declarada, `formed_inference_claim_ids[]` := os `content_claim_ids` cuja afirmação tem `formed_inference=true` (…a marca de inferência chega ao registro publicado e entra no `record_hash` — RULE-EPI-01…)". RU-8 (SPEC-007 §7-bis): "marca de inferência (`formed_inference_claim_ids`) sem campo próprio no `node_record` da SPEC-006 até a errata E-4 — visível pela cadeia D9 via `seal_ref`, não pela leitura isolada do registro". `[FONTE — FATO NORMATIVO (baseline SPEC-007)]`

**Texto aditivo proposto (campo novo, opcional, no `node_record`):** `[PROPOSTA]`

> *[Errata v1.13 — E-4]* `"formation"`: **opcional; só em registro com `publication.origin = spec007_seal`** (ausente no caminho (a)). Conteúdo: `{ "content": "campos de CONTEÚDO de M (texto exato das afirmações, na ordem declarada — RULE-KFH-005)", "content_claim_ids": ["…"], "formed_inference_claim_ids": ["… (lista vazia quando não há inferência)"] }`. O bloco é **dado de conteúdo do selo**, não regra nova: a SPEC-006 não o interpreta nem o julga; **a conferência da E-3 o cobre**, porque `content` e `formed_inference_claim_ids` estão em M e, portanto, no `record_hash`. O bloco não contém, nem pode receber, campo de convicção ou de custo (INV-04; RULE-CKG-007).

**Notas** `[INFERÊNCIA]`:
- **Na prática é obrigatório no caminho (b):** se o registro selado chegar sem `formation`, o hash recalculado não bate com o selado e a E-3 recusa (`SEAL_CONTENT_MISMATCH`). Por isso a errata não precisa de uma regra "obrigatório" separada (fonte única).
- **Ponto ambíguo — `content_claim_ids[]` dentro do hash.** A RULE-KFH-005 lista como saída de M o **texto** das afirmações e os `formed_inference_claim_ids`, mas não diz claramente se a **lista** `content_claim_ids[]` também é saída de M. Se não for, ela fica no bloco como ponteiro de auditoria **fora** do hash, conferível pela cadeia D9 a partir de `seal_ref`. Fechar isso mexeria na SPEC-007, e esta errata não faz isso: é a **Pergunta Q-6**. Enquanto não houver resposta, a errata **não afirma** que `content_claim_ids[]` está coberto pelo hash.
- **Até a errata (ou se Andraus não a aprovar):** vale o que a SPEC-007 já diz. O mapeamento para campos existentes do `node_record` é BUILD, e a fonte de verdade da marca de inferência continua sendo candidato + `validation_record` + selo, alcançáveis pela cadeia D9 a partir de `publication.seal_ref`. `[FONTE: SPEC-007, E-4]`
- **Efeito sobre RU-8:** com a E-4 aprovada, a marca de inferência fica **no próprio registro do KG** e entra na conferência da E-3 (caso ADV-CKG-21 (l)). Sobra um risco residual: quem lê o registro e **ignora** o bloco `formation`. Expor o bloco obrigatoriamente na consulta (RULE-CKG-011/EC-CKG-006) seria regra nova, e não está proposto aqui (Pergunta Q-7). RU-8 fica **reduzido, não eliminado** (RULE-UNC-01).

---

## Herança/Delta desta errata (CC-08; RULE-HD-02/03/04)

- **INHERITS** (ID + versão): SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005) — RULE-KFH-005 (M, canon, H, `record_hash`; lista de exclusão de M); RULE-KFH-007 (ix) (`publication.origin`, `publication.seal_ref = seal_id@seal_version`, campos fora do hash); esquema `publication_seal` (`sealed_records[]`, `succession_of[]?`); RULE-KFH-020 (ato `ISSUER_LIST`). SPEC-006 v1.12 (DHR-SPEC006-004) — RULE-CKG-005/009/010/012, BASpec-CKG-010, EC-CKG-001, §D3.1.
- **ADDED:** nota E-1; nota E-2; campo `publication` no `relation_record` (E-2(b), se aprovado); cláusula de conferência do selo na RULE-CKG-010 (E-3) e as notas de propagação; subcódigo `SEAL_REF_UNRESOLVABLE`; uso do código `SEAL_CONTENT_MISMATCH` no KG; campo `formation` (E-4); letras T09 (d) e ADV-CKG-21 (i)–(o).
- **MODIFIED:** nenhum. A E-3 **acrescenta** condição ao caminho (b); não muda o texto existente. É restritiva no efeito (ver Compatibilidade).
- **REMOVED:** vazio.

**Evidência obrigação a obrigação (§7-bis Bloco B):**
| Obrigação herdada | Onde esta errata a satisfaz |
|---|---|
| RULE-KFH-005: "UMA serialização canônica para toda a Spec … É UMA função só" | E-3 item 3 usa a MESMA canon/H, sem criar outra |
| RULE-KFH-005: M exclui `publication.*`, sucessão, IDs do KG, `writer_id`, `computed_by`, tempos | E-3 item 3 repete a lista completa de M (nota "Lista de exclusão completa") |
| RULE-KFH-005: hashes "nunca lidos do payload nem de campo de hash armazenado" | E-3 recalcula a partir do registro recebido; o hash de referência vem do selo, nunca do registro |
| RULE-KFH-007 (ix): `seal_ref = seal_id@seal_version`; campos de sucessão fora do hash | E-2 (formato); E-3 itens 1 e 4 |
| RULE-KFH-007 (ix): "A ESCRITA permanece sob RULE-CKG-009 pelo committer do KG" | E-1 e E-3 ("sob a RULE-CKG-009") |
| RULE-CKG-010 (b): formado sem selo ⇒ `FORMED_WITHOUT_SEAL` | mantido; a E-3 só se soma depois dele |
| RULE-CKG-010 (b): hypothesis via selo proibida (`HYPOTHESIS_VIA_SEAL_FORBIDDEN`) | não tocada; a E-3 não abre nenhum tipo novo |
| RULE-CKG-009: falha de auth ⇒ não-autorizado (fail-closed) | E-3 item 1: registro de selos indisponível ⇒ recusa (mesmo espírito) |
| RULE-CKG-012: compare-and-commit, sem fork | não tocada; a E-3(c) só se soma a ela |

Nenhuma obrigação herdada foi removida ou enfraquecida. `[INFERÊNCIA — verificado por leitura dos textos citados]`

---

## Constitution Check (CC-01..CC-12) — só o que a errata toca

| CC | Resultado | Por quê |
|---|---|---|
| CC-01 | PASS | Hierarquia intocada; o selo só admite `learning` (SPEC-007 (iv-bis)); hypothesis via selo segue proibida |
| CC-02 | PASS | Não redefine CHM/CEM/CCM nem o selo; só referencia a SPEC-007 |
| CC-03/CC-04 | PASS | Nenhum campo de convicção nem de custo; `formation` sem convicção (INV-04) |
| CC-05 | PASS | CRITICAL (da SPEC-006) |
| CC-06/CC-07 | N/A | Não é Engineering Card |
| CC-08 | PASS | Herança/Delta acima, com evidência obrigação a obrigação |
| CC-09 | PASS | Riscos RU-3/RU-8 declarados, com o que sobra; ponto ambíguo `content_claim_ids` marcado, não afirmado; nenhum número inventado |
| CC-10 | PASS | "selo", "selado" e "conferência" no sentido da SPEC-007; nenhum termo do GLOSSARIO redefinido |
| CC-11 | PASS | E-3 herda a Classe C da BASpec-CKG-010 (gate determinístico) |
| CC-12 | N/A | Infraestrutura sem escola (como a SPEC-006) |

---

## §7-bis — Redução de viés (CRITICAL)

**Bloco A — pergunta adversarial (E-3, a única parte com efeito):**
- *Se a E-3 estivesse errada, o que se veria?* (1) Recusa falsa de registro selado e válido, se a projeção M do lado do KG for diferente da do pipeline (caso ADV-21 (m)). (2) Aceite de registro trocado, se a conferência olhar campo fora de M (casos (k)/(l)). Os dois casos são observáveis com hash recalculado × selado.
- *O ENTÃO é verificável por observador independente?* Sim. Basta ter o selo e o registro recebido: qualquer um recalcula H(canon(M(r))) e compara.
- *Existe QUANDO satisfeito sem que o ENTÃO deva ocorrer?* Sim: registro que difere só fora de M. Isso está coberto pelo caso (m), que é de negação.

**Bloco C — epistêmico:**
- "Fecha RU-3" é afirmação causal com mecanismo declarado (igualdade de hash de conteúdo sobre a mesma serialização). Não é correlação.
- O que sobra é declarado como risco, não como fato resolvido: committer sem a conferência (implementação); relações sem E-2(b); sucessão sem E-3(c); leitor que ignora `formation` (RU-8 reduzido).
- `content_claim_ids` dentro do hash fica INDETERMINADO até a Q-6.
- Nenhuma probabilidade ou número declarado. Taxa de amostragem continua INDETERMINADA (ENF-07, gap aberto).

**Bloco D:** a errata não executa nada nem cruza para a execução (INV-05). Toda dependência de Andraus está marcada como Pergunta ou [DECISÃO NECESSÁRIA].

---

## CONS-01 — continuam ABERTAS (nenhuma fechada por esta errata)

G-001 · **K-001** · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · **host do juízo CKG-008** `[DECISÃO NECESSÁRIA]` · composição concreta da lista de escritores do caminho (a) `[DECISÃO NECESSÁRIA]` · migração de ontologia `[DECISÃO NECESSÁRIA]` · timeout `PENDING_ANCESTOR` `[DECISÃO NECESSÁRIA]` · "produtor/gatilho de promoção trabalho→permanente" `[DECISÃO NECESSÁRIA]` · mecanismo de assinatura dos atos de Andraus (BUILD). A negação de `conviction` por padrão (DHR-SPEC006-003 D2) **não muda**. `[FONTE: DHR-RETRO-001 §3; DHR-SPEC006-004 §4; DHR-SPEC007-005 §5]`

Passo 11-bis / RMR-001: BL-003 e BL-011 seguem `ATIVADO` com Disposição PARCIAL (plan.md "Nota de gate"); BL-010/BL-029/BL-035 inalterados. A errata não promove nem muda estado no painel. `[FONTE: specs/features/SPEC-006/plan.md "Nota de gate"]`

---

## Forma de aplicação após a homologação — decisão de Andraus (Pergunta Q-8)

- **(A) recomendada:** este arquivo fica como a errata (no padrão de arquivo à parte do `governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md`). O plan.md da SPEC-006 recebe só **uma linha** no Histórico de versões e um marcador no Status apontando para cá, com o texto anterior preservado. Assim, uma correção futura mexe em menos lugares (P2/P4).
- **(B):** as notas são copiadas para dentro do plan.md em cada âncora (padrão v1.11/v1.12), com colchetes de preservação. Isso exige a tabela fato→locais abaixo como lista de conferência.

---

## Perguntas para Andraus

- **Q-1 (E-1):** a errata cobre só o caminho (b) (lista de emissores do selo), como a SPEC-007 propôs, ou também a **lista de escritores do caminho (a)**? *Recomendação: só (b); o caminho (a) fica [DECISÃO NECESSÁRIA].*
- **Q-2 (E-2(b)):** acrescentar o bloco `publication` ao **registro de relação**? Sem isso, a conferência do selo não cobre relações e o RU-3 fica aberto para elas. *Recomendação: sim.*
- **Q-3 (E-3(c)):** o KG também deve conferir que a **troca declarada** (`supersedes`) está no selo? Sem isso, um committer que contorne o pipeline poderia pendurar uma troca não autorizada em conteúdo selado. *Recomendação: sim.*
- **Q-4:** o KG deve também exigir que o **consumo do selo** ainda esteja `RESERVADO` (barrando reuso do selo)? *Recomendação: não agora; a repetição idêntica já é no-op (RULE-CKG-012).*
- **Q-5:** os códigos de recusa ficam como subcódigos de `ADMISSION_REJECTED` (`SEAL_REF_UNRESOLVABLE` novo + `SEAL_CONTENT_MISMATCH` reusado da SPEC-007)? *Recomendação: sim.*
- **Q-6 (E-4):** a lista `content_claim_ids[]` entra no hash do selo? Se a resposta for "sim", a mudança é na SPEC-007 (não nesta errata). *Recomendação: deixar fora do hash por ora, como ponteiro de auditoria.*
- **Q-7 (E-4/RU-8):** a consulta do KG deve **mostrar sempre** a marca de inferência? Seria regra nova. *Recomendação: não nesta errata; registrar como risco RU-8 reduzido.*
- **Q-8:** forma de aplicação (A) arquivo à parte com ponteiro ou (B) cópia em cada âncora. *Recomendação: (A).*
- **Q-9:** classificação: Minor/aditiva ou Major (a E-3 restringe)? *Precedente: v1.11 restritiva = Major (DHR-SPEC006-003 D3).*

---

## Tabela fato → locais (P2) — cada fato que se repete, e onde ele aparece

Locais nesta errata e âncoras (por ID/texto) no baseline. Em correção futura, corrigir **todos** os locais da linha.

| Fato | Locais nesta errata | Âncoras no baseline da SPEC-006 (não editadas) |
|---|---|---|
| "Quem mantém a lista de quem grava" = decidido por Andraus (P-1) | E-1 (texto aditivo); Herança INHERITS (RULE-KFH-020); Q-1 | RULE-CKG-009 ("allowlist de escritores e quem hospeda o juízo CKG-008"); D6 ("concreta** de escritores = **[DECISÃO NECESSÁRIA]**"); Etiquetagem ("Allowlist de escritores / host do juízo CKG-008 / migração de ontologia"); lista final ("**Allowlist de escritores / host do juízo CKG-008 / migração de ontologia**"); §7-bis RULE-INQ ("selo SPEC-007, allowlist, host do juízo"); §7-bis Bloco D ("allowlist/host do juízo"); `checks.md` Itens em aberto ("allowlist de escritores; host do juízo CKG-008;") |
| Host do juízo CKG-008 segue [DECISÃO NECESSÁRIA] | E-1 (texto aditivo e "NÃO está decidido"); CONS-01 | as mesmas sete âncoras da linha acima |
| K-001 segue ABERTA | §0; E-1; CONS-01 | RULE-CKG-009 ("K-001/SPEC-018"); D6; Etiquetagem; lista final ("M-001 / J-001 / N-001 / G-001 / K-001") |
| Contrato do selo = SPEC-007 RULE-KFH-007 (ix), `seal_ref = seal_id@seal_version` | E-2 (nota); E-3 item 1; Herança INHERITS | I/O Schema `node_record.publication.seal_ref`; RULE-CKG-010 ("contrato do selo = DEPENDÊNCIA"); D6 1º item; Etiquetagem ("Contrato do selo de publicação"); lista final ("**Contrato do selo de publicação**"); Autopré-check ("selo SPEC-007 marcado"); `checks.md` Itens em aberto ("selo de publicação (SPEC-007);") |
| `relation_record` sem `publication` | E-2(b); E-3 (abertura "nó ou, se a E-2(b) for aprovada, relação"); "Efeito sobre RU-3"; Herança ADDED; Q-2 | I/O Schema `relation_record` |
| Lista de exclusão de M (`publication.*`, sucessão, IDs do KG, `writer_id`, `computed_by`, tempos) | E-3 item 3; nota "Lista de exclusão completa"; Herança (tabela, 2ª linha); ADV-21 (m) | — (fonte única: SPEC-007 RULE-KFH-005) |
| Conferência do selo (3 passos + 4º se Q-3) | E-3 cláusula; notas de propagação; EC delta PRECOND/FAILURE-MODE; casos T09 (d)/ADV-21 (i)–(o) | BASpec-CKG-010 MECANISMO; EC-CKG-001 PRECOND; D4 "Admissão (CKG-010)" |
| Códigos `SEAL_REF_UNRESOLVABLE` / `SEAL_CONTENT_MISMATCH` sob `ADMISSION_REJECTED` | E-3 cláusula; nota "Códigos"; propagação §D3.1; EC delta FAILURE-MODE; casos ADV-21; Q-5 | §D3.1 linha `ADMISSION_REJECTED` |
| Sucessão conferida contra `succession_of[]` (só se Q-3) | E-3 item 4; nota "Por que a E-3(c)"; EC delta PRECOND; ADV-21 (n); §7-bis Bloco C; Q-3 | RULE-CKG-012 (não editada) |
| RU-3 fecha para nós; para relações só com E-2(b) | E-2(b) último item; "Efeito sobre RU-3"; §7-bis Bloco C | — (RU-3 é da SPEC-007) |
| Bloco `formation` = `content` + `content_claim_ids[]` + `formed_inference_claim_ids[]`, coberto pela E-3 | E-4 texto; notas E-4; ADV-21 (l); Herança ADDED | I/O Schema `node_record` |
| `content_claim_ids[]` no hash = INDETERMINADO | E-4 "Ponto ambíguo"; §7-bis Bloco C; Q-6 | — |
| RU-8 reduzido, não eliminado | E-4 "Efeito sobre RU-8"; §7-bis Bloco C; Q-7 | — (RU-8 é da SPEC-007) |
| Compatibilidade a decidir (E-3 restritiva; precedente v1.11 = Major) | cabeçalho "Compatibilidade proposta"; Herança MODIFIED; Q-9 | Histórico de versões linha 1.11 |
| Nenhum ID novo de RULE/BASpec/EC/T/ADV; contagens 13/6/13/19/23 inalteradas | §0; casos ("letras novas"); Herança ADDED | Histórico de versões linha 1.12 (contagens) |

---

## Verificação de spec desta errata (feedback interno — NÃO é parecer do Revisor nem homologação)

- Âncoras E-1..E-4 conferidas por busca de texto (Grep) no `specs/features/SPEC-006/plan.md` e no `specs/features/SPEC-006/checks.md`: todas presentes literalmente. O Especificador **não** recalculou hashes (sem Bash).
- Assertivas para o Orquestrador/Revisor (plan.md da SPEC-006, **antes** da homologação, deve continuar sem nenhuma destas marcas): assert-absent:"Errata v1.13" · assert-absent:"SEAL_REF_UNRESOLVABLE" · assert-absent:"\"formation\"". Depois de homologada pela forma (A): assert-present de uma linha 1.13 no Histórico de versões apontando para este arquivo.
- **Gates — NÃO executados pelo Especificador (sem Bash):** `python scripts/validate_spec_sot.py` (feito para plan.md; neste arquivo pode reprovar por estrutura — não é um Plan), `python scripts/check_refs.py`, `python scripts/check_invariants.py specs/features/SPEC-006/errata-v1.13.md`, `python scripts/revisor_gate.py specs/features/SPEC-006/errata-v1.13.md`, `python scripts/check_doc_sync.py`, `python scripts/build_map.py --check`, `python -m unittest discover -s tests`. Ficam para o Orquestrador.

"VERIFY" interno ≠ CONFORME ≠ homologação.

**Pronto para revisão.**
