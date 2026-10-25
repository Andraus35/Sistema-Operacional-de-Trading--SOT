# SPEC-006 — Errata v1.13 (ADITIVA) — ligação com o selo da SPEC-007 (E-1..E-4) — texto v1.1

| Campo | Valor |
|---|---|
| Versão desta errata | **v1.1** (2026-10-25). Corrige o parecer R1 (`governance/propostas/SPEC-006/PARECER-REVISOR-SPEC006-ERRATA-v1.13-R1-2026-10-25.md`): A1–A4 (Médias), A5, A6b, A7 (Menores). A6a já foi aplicado pelo Orquestrador por Ficha-M e está mantido. Incorpora as respostas de Andraus a Q-1, Q-2, Q-3, Q-8 e Q-9. **O texto integral da v1.0 está no Anexo V1.0, no fim deste arquivo (INV-07); ele não vale mais.** Mudanças por achado: "Registro de mudanças v1.0 → v1.1". |
| Spec afetada | SPEC-006 — Cognitive Knowledge Graph (HOMOLOGADA — BASELINE v1.7 + errata v1.11 [DHR-SPEC006-003] + errata v1.12 [DHR-SPEC006-004]). **Esta errata NÃO edita texto baselined** (INV-07/INV-09): `specs/features/SPEC-006/plan.md` e `specs/features/SPEC-006/checks.md` ficam como estão até a homologação. |
| Natureza | **PROPOSTA de errata aditiva.** Aguarda o Revisor e a homologação de Andraus. Não é baseline (INV-09). Nada nela vale antes da homologação. |
| Ordem | DHR-RETRO-001 §1 "Próxima frente" item (1) e §2 ("uma de cada vez, nesta ordem, cada uma com Revisor e homologação própria de Andraus. Nenhum baseline é editado antes da homologação da respectiva errata") `[FONTE — FATO NORMATIVO: decisão de Andraus registrada em ata]` |
| Decisões de Andraus incorporadas | Q-1 = só o caminho (b) · Q-2 = incluir `publication` no registro de relação · Q-3 = conferir `supersedes` contra `succession_of[]` do selo · Q-8 = arquivo à parte com ponteiro de uma linha no plan.md (forma A) · Q-9 = Major (precedente DHR-SPEC006-003 D3) · Q-4 = não exigir selo `RESERVADO` · Q-5 = sim (`SEAL_REF_UNRESOLVABLE` para selo não resolvido + `SEAL_CONTENT_MISMATCH` reaproveitado da SPEC-007; caso "`record_ref` fora de `sealed_records`" nomeado pelo que falhou, conforme A7) · Q-6 = `content_claim_ids[]` fora do hash (ponteiro de auditoria) · Q-7 = não nesta errata (marca de inferência na consulta fica fora). `[FONTE — decisões de Andraus no chat, 2026-10-25, passadas pelo Orquestrador (Q-1/2/3/8/9 na ordem de serviço desta v1.1, com referência a DHR-RETRO-001; Q-4..Q-7 em mensagem posterior do mesmo dia)]`. **Registrado em ata:** DHR-RETRO-001 §4 traz Q-1..Q-9; Q-10 e o código `SEAL_SUCCESSION_MISMATCH` seguem pendentes. `[FONTE]` |
| Origem do conteúdo | `specs/features/SPEC-007/plan.md` v2.3 (BASELINE, DHR-SPEC007-005): seção "Proposta de errata aditiva à SPEC-006", itens E-1..E-4; riscos RU-3 e RU-8 (§7-bis Bloco C); RULE-KFH-004 (proposta de registros), RULE-KFH-005 (M, canon, H), RULE-KFH-007 (vii)/(ix), esquemas `publication_seal` e "registro submetido", EC-KFH-004. Também: DHR-SPEC007-003 P-1; DHR-SPEC007-005 H-2. `[FONTE]` |
| Base auditável | sha256 do plan.md da SPEC-006 conferido pelo Orquestrador em 2026-10-25 = `dd5a609f3007…`, igual ao da DHR-SPEC006-004 §2 (parecer R1, "Encaminhamento"). `[FONTE]` |
| Âncoras | **Por ID + texto literal entre aspas, nunca por número de linha** (alinhado à proposta P3 — ainda proposta a especificar, DHR-RETRO-001 §1). Números de linha ("l.1410", "l.526") só ajudam a achar o trecho; o que vale é o texto. |
| Complexidade | CRITICAL (a da SPEC-006; não muda) · D0–D7 + D8 focado · profile standard + adversarial. A errata mexe só no caminho (b) de admissão (RULE-CKG-010) e nos esquemas `node_record` e `relation_record`. |
| Compatibilidade | **Major** — decisão de Andraus (Q-9), no mesmo sentido do precedente DHR-SPEC006-003 D3 (a errata v1.11, restritiva, foi Major). E-1, E-2 e E-4 só acrescentam; **E-3 restringe**: o KG passa a recusar registro selado que hoje aceita. `[FONTE — decisão de Andraus; ver "Decisões de Andraus incorporadas"]` |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Data | 2026-10-25 |

---

## 0. O que esta errata faz, em uma frase

Hoje a SPEC-006 diz que o selo da SPEC-007 é uma dependência ainda não decidida. A SPEC-007 já foi homologada e definiu o selo. Esta errata **liga as duas pontas**. Ela registra o que Andraus já decidiu sobre a lista de quem grava no caminho (b) (E-1). Aponta o formato do selo e põe o bloco `publication` também no registro de relação (E-2). Faz o KG **conferir o selo** ao gravar nó ou relação (E-3). E dá aos dois registros um bloco `formation` com o `record_ref`, o conteúdo formado e a marca de inferência (E-4). `[INFERÊNCIA — resumo]`

**Não faz:** não decide quem hospeda o juízo CKG-008. Não fecha K-001 nem outra decisão aberta. Não muda no mérito nenhuma regra, BASpec, EARS, EC, cenário ou ADV existente. Não cria ID novo de RULE/BASpec/EC/T/ADV. Não edita o plan.md da SPEC-006 nem o da SPEC-007. `[FONTE: DHR-RETRO-001 §2-§3; DHR-SPEC007-005 H-2]`

---

## E-1 — Lista de quem grava no caminho (b) (parte da RULE-CKG-009 decidida pela P-1)

**Âncora (RULE-CKG-009, última frase antes de `[Fonte:`):** "allowlist de escritores e quem hospeda o juízo CKG-008 = [DECISÃO NECESSÁRIA] (runtime; K-001/SPEC-018)." `[FONTE: specs/features/SPEC-006/plan.md, RULE-CKG-009 — FATO NORMATIVO (baseline)]`

**Fato de origem:** a DHR-SPEC007-003, linha P-1, diz: "**Decide parte de `SPEC-006 plan.md` l.482** (quem mantém a lista de quem grava); a governança do aprender-sozinho (K-001) segue ABERTA". `[FONTE — FATO NORMATIVO: decisão de Andraus em ata]`

**Escopo (decisão de Andraus, Q-1):** a errata cobre **só o caminho (b)**. `[FONTE — decisão de Andraus]`

**Texto aditivo proposto (vai depois da âncora; a frase baselined não muda):** `[PROPOSTA]`

> *[Errata v1.13 — E-1]* A frase acima tem dois itens. **Item (1), "quem mantém a allowlist de escritores", está decidido no caminho (b):** pela DHR-SPEC007-003 P-1, a lista é aprovada por Andraus. No caminho (b) da RULE-CKG-010 (conhecimento formado via selo), essa lista é a **lista de emissores do selo** da SPEC-007 (ato `ISSUER_LIST`, RULE-KFH-020; RULE-KFH-007 (iii)). A escrita no KG continua sob a RULE-CKG-009, feita pelo committer do KG (`computed_by` ≠ `writer_id` — RULE-CKG-005). A lista de emissores é regra LOCAL da SPEC-007, análoga à RULE-CKG-009. **Ela não define os escritores do caminho (a)**: a lista do caminho (a) continua [DECISÃO NECESSÁRIA]. **Item (2), "quem hospeda o juízo CKG-008", continua [DECISÃO NECESSÁRIA]** (o juiz de fidelidade da SPEC-007 não é esse host). **K-001 continua ABERTA.**

**O que continua aberto** `[DECISÃO NECESSÁRIA]`:
- a **lista de escritores do caminho (a)** (ciclo de vida canônico) e as identidades de committer, tanto quem aprova quanto quem está nela. Q-1 limitou a errata ao caminho (b), e o texto da SPEC-006 D6 ("concreta** de escritores = **[DECISÃO NECESSÁRIA]** (runtime; K-001/SPEC-018)") continua valendo;
- **quem está** na lista de emissores do caminho (b): P-1 decidiu **quem aprova** a lista; os nomes dependem do ato `ISSUER_LIST` de Andraus (RULE-KFH-020);
- o **host do juízo CKG-008** (RULE-CKG-008/009);
- **K-001** (governança de runtime / aprender sozinho);
- o **mecanismo** da assinatura dos atos de Andraus. O princípio (assinatura criptográfica com chave em dispositivo dele) foi decidido na DHR-SPEC007-007; o mecanismo segue aberto para a construção. `[FONTE: ROADMAP "Decisões FECHADAS", item "Autenticação dos atos de Andraus"]`

**Por que é aditivo:** a frase baselined fica como está. A nota só registra uma decisão já tomada em ata e separa o que está decidido do que está aberto. `[INFERÊNCIA]`

---

## E-2 — Formato do selo (`seal_ref`) e bloco `publication` no registro de relação

**Âncoras (todas dizem que o contrato do selo ainda não existe):** `[FONTE: specs/features/SPEC-006/plan.md]`
- (a) I/O Schema, `node_record.publication`: `"seal_ref": "[DECISÃO NECESSÁRIA — contrato do selo = SPEC-007]"`;
- (b) RULE-CKG-010: "(contrato do selo = DEPENDÊNCIA da SPEC-007 = [DECISÃO NECESSÁRIA])";
- (c) D6, 1º item: "(b) formado com selo SPEC-007 (contrato = [DECISÃO NECESSÁRIA])";
- (d) Etiquetagem: "| Contrato do selo de publicação | [DECISÃO NECESSÁRIA] | Dependência da **SPEC-007** |";
- (e) lista final de abertas: "**Contrato do selo de publicação** — dependência da **SPEC-007**; [DECISÃO NECESSÁRIA].";
- (f) Autopré-check: "selo SPEC-007 marcado [DECISÃO NECESSÁRIA]";
- (g) `checks.md`, "Itens em aberto": "selo de publicação (SPEC-007);".

**Fato de origem:** a SPEC-007 v2.3 está **homologada** (DHR-SPEC007-005). A RULE-KFH-007 (ix) diz: "o registro submetido = registro materializado + `publication.origin = spec007_seal` + `publication.seal_ref = seal_id@seal_version` (+ `supersedes`/`version`/`expected_version` se sucessora) — esses campos ficam FORA do `record_hash`". O selo (`publication_seal`) traz `seal_id`, `seal_version`, `material_hash`, `sealed_records[{record_ref, record_kind, record_hash}]`, `succession_of[]?{record_ref → published_ref@version}` e os demais campos do esquema `publication_seal` da SPEC-007. `[FONTE — FATO NORMATIVO]`

**Texto aditivo proposto (uma nota que vale para as sete âncoras):** `[PROPOSTA]`

> *[Errata v1.13 — E-2]* **Dependência satisfeita:** o contrato do selo é o da SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005), RULE-KFH-007 (ix): `publication.seal_ref = seal_id@seal_version`, que aponta um `publication_seal` da SPEC-007. `publication.origin = spec007_seal` continua DERIVADO do canal e da identidade autenticada, não do payload. A SPEC-006 **não redefine** o selo; só faz referência a ele (CC-02). Onde o texto acima diz "contrato do selo = [DECISÃO NECESSÁRIA]", leia-se "contrato do selo = SPEC-007 RULE-KFH-007 (ix)". A conferência do selo pelo KG está na E-3.

**E-2(b) — `publication` no registro de relação (decisão de Andraus, Q-2)** `[PROPOSTA — escopo decidido por Andraus]`
- **Âncora:** I/O Schema, bloco `"relation_record": {`. Os campos vão de `relation_id` a `similarity_basis` e não há `publication`. `[FONTE]`
- **Por quê:** a SPEC-007 também sela relações. A RULE-KFH-007 (vii) diz: "relação CAUSA ou SIMILAR_A DEVE trazer os campos da RULE-CKG-008". O esquema "registro submetido" da SPEC-007 usa "campos do node_record/relation_record da SPEC-006, NÃO redefinidos". `[FONTE]`
- **Texto aditivo:** o `relation_record` recebe o mesmo bloco opcional `"publication": { "origin": "canonical_lifecycle | spec007_seal — DERIVADO do CANAL/identidade AUTENTICADA (não do payload)", "seal_ref": "seal_id@seal_version (SPEC-007 RULE-KFH-007 (ix)); só se origin = spec007_seal" }`, com a mesma semântica do `node_record`.
- **Ligação:** a relação também recebe o bloco `formation` (E-4). Sem ele não há onde guardar o conteúdo e o `record_ref` da relação, e o hash da relação nunca bateria (parecer R1, A3).

---

## E-3 — O KG confere o selo ao gravar (fecha RU-3 para o que está em M)

**Âncoras:** `[FONTE: specs/features/SPEC-006/plan.md]`
- RULE-CKG-010: "Formado SEM selo é REJEITADO (`FORMED_WITHOUT_SEAL`)";
- BASpec-CKG-010, MECANISMO: "(b) gate (selo SPEC-007 presente)";
- EC-CKG-001, PRECOND: "∨ selo SPEC-007 — CKG-010)";
- D4, item "Admissão (CKG-010)": "`admite(x) sse (x formado ∧ selo SPEC-007) ∨";
- §D3.1, linha "| `ADMISSION_REJECTED` | `FORMED_WITHOUT_SEAL`,".

**Problema (RU-3):** hoje o KG só verifica que o selo **está presente**. A SPEC-007 registra o risco: "o KG hoje aceita registro com `publication.origin = spec007_seal` de escritor autorizado SEM conferir `seal_ref`/hash; um committer autorizado que contorne o pipeline gravaria formado não selado, ou com conteúdo trocado, com rótulo de selado" (RULE-KFH-007 (ix); §7-bis RU-3). `[FONTE — FATO NORMATIVO (baseline SPEC-007)]`

**Texto aditivo proposto: cláusula nova da RULE-CKG-010, caminho (b), sem ID novo** `[PROPOSTA]`

> *[Errata v1.13 — E-3] Conferência do selo no committer (caminho (b)).* Ao receber um registro de nó ou de relação com `publication.origin = spec007_seal`, o committer do KG DEVE, **antes de gravar** e sob a RULE-CKG-009, fazer as conferências abaixo nesta ordem. Ele para na primeira que falhar.
> 1. **Resolver o selo.** `publication.seal_ref` ausente, fora do formato `seal_id@seal_version` ou sem `publication_seal` correspondente na SPEC-007 ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_REF_UNRESOLVABLE`. Se a leitura (read-only) do registro de selos falhar, o selo também não se resolve ⇒ mesma RECUSA `SEAL_REF_UNRESOLVABLE`, com o motivo `registry_unavailable` no log. É fail-closed: o committer nunca grava "por confiança".
> 2. **Achar o registro no selo.** `formation.record_ref` (E-4) DEVE existir e ser igual ao `record_ref` de um item de `sealed_records[]` desse selo. Se faltar ou não estiver no selo ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_RECORD_NOT_IN_SEAL`.
> 3. **Recalcular o hash.** O committer reconstrói M(r) a partir do registro recebido. Usa só os campos que a "Tabela de projeção M" (abaixo) marca **entra**, junto com o "Mapa de formato". M é definida **por inclusão**: campo não marcado fica fora. Calcula H(canon(M(r))) pela **serialização única da RULE-KFH-005 da SPEC-007**, com a mesma função canon/H (uma só; a codificação de bytes é BUILD). Compara o resultado com o `record_hash` daquele `record_ref` em `sealed_records[]`. Hash diferente, ou M(r) impossível de reconstruir (ex.: ponta de relação que não existe no KG) ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_CONTENT_MISMATCH`.
> 4. **Conferir a sucessão (Q-3).** Seja P o par de `succession_of[]` do selo cuja chave é `formation.record_ref`, se existir. (a) O registro traz `supersedes` e P não existe, ou o `supersedes` difere de `P.published_ref@version` pelo "Mapa de formato" ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_SUCCESSION_MISMATCH`. (b) P existe e o registro não traz `supersedes` ⇒ RECUSA `ADMISSION_REJECTED` / `SEAL_SUCCESSION_MISMATCH`.
>
> Depois das conferências, as demais regras de escrita valem sem mudança (RULE-CKG-001/005/008/009/012/013). Uma recusa não grava nada; o registro recusado e o motivo ficam no log (EC-CKG-001 FAILURE-MODE). A SPEC-006 não calcula `material_hash`, não refaz a validação F1 e não julga fidelidade. **Ela só confere identidade de conteúdo** contra o selo (ENF-03 — gate determinístico).

### Mapa de formato (parecer R1, A1) `[PROPOSTA]`
| Elemento | Lado da SPEC-007 (selo / M) | Lado da SPEC-006 (registro do KG) | Regra de ligação |
|---|---|---|---|
| `record_ref` | saída de M (RULE-KFH-005: "cada registro = {`record_ref`, `record_kind`, …}") e chave de `sealed_records[]` e de `succession_of[]` | **`formation.record_ref`** (E-4), no `node_record` e no `relation_record` | igualdade literal. **Não fica dentro de `publication`**: M exclui "`publication.*`", e o `record_ref` está em M. Se ficasse em `publication`, o KG teria que pôr em M um campo que M exclui. |
| `seal_ref` | `seal_id@seal_version` | `publication.seal_ref` | igualdade literal (E-2) |
| `record_kind` de M | `{nó \| relação}` (`record_proposal`, `sealed_records[]`) | não é o campo `record_kind` do KG (`creation \| invalidation \| …`), que fica fora de M | `node_record` ⇒ `"nó"`; `relation_record` ⇒ `"relação"`, tirado do tipo do registro recebido |
| Alvo da sucessão | `succession_of[]`: `record_ref → published_ref@version` | `supersedes`: `"KG-N-...-v0"` (nó) / `"KG-R-...-v0"` (relação) | `published_ref` = `node_id`/`relation_id` do KG; `@version` = o sufixo `-v<n>`. Igualdade = mesmo id **e** mesma versão. Exemplo: `supersedes = "KG-N-X-v2"` ≡ `KG-N-X@2`. A conversão é só de escrita, determinística, sem consulta. `[INFERÊNCIA: o sufixo `-v<n>` é a versão do alvo, porque o esquema diz "aponta p/ ÚLTIMA versão"]` |
| Pontas da relação (`from`/`to` de M) | `record_proposal`: "campos ESTRUTURAIS declarados (`from`/`to`, …)" | `from_node`; `to_node`, ou `target_relation_id` quando `to_node = null` | M.from vem de `from_node` (M.to, do mesmo jeito, de `to_node` ou `target_relation_id`). Se a ponta X existe no KG e tem `publication.seal_ref` igual ao do registro recebido (veio no mesmo selo), M.from := `X.formation.record_ref`. Senão, M.from := o id de X no KG. Se X não existe, M não pode ser reconstruída ⇒ `SEAL_CONTENT_MISMATCH`. **Premissa da Q-10 (b), PENDENTE.** |

### Tabela de projeção M — `node_record` (parecer R1, A2) `[PROPOSTA — leitura da RULE-KFH-005]`
A RULE-KFH-005 define M **por inclusão**: "cada registro = {`record_ref`, `record_kind`, campos estruturais declarados (`node_type` := `target_node_type`; `from`/`to`; campos da RULE-CKG-008 quando CAUSA/SIMILAR_A), campos de CONTEÚDO …, `formed_inference_claim_ids[]` …}". A frase "M EXCLUI …" dá exemplos do que não é material. Ela não é a definição de M. Logo, **campo que não está na lista de inclusão fica fora**, mesmo que não esteja na lista de exclusão. `[INFERÊNCIA]`

| Campo do `node_record` | M | Por quê |
|---|---|---|
| `formation.record_ref` (E-4) | **entra** | `record_ref` de M |
| (derivado) tipo do registro ⇒ `"nó"` | **entra** | `record_kind` de M (Mapa de formato) |
| `node_type` | **entra** | "`node_type` := `target_node_type`" (= `learning`; RULE-KFH-007 (iv-bis)) |
| `formation.content` (E-4) | **entra** | "campos de CONTEÚDO" de M |
| `formation.formed_inference_claim_ids` (E-4) | **entra** | `formed_inference_claim_ids[]` de M ("entra no `record_hash`") |
| `formation.content_claim_ids` (E-4) | fora | **decisão de Andraus (Q-6):** fica fora do hash, como ponteiro de auditoria |
| `node_id` | fora | ID atribuído pelo KG (M exclui) |
| `record_kind` (`creation \| …`) | fora | outro campo, com outro sentido. `[INFERÊNCIA]` No caminho (b) é `creation`; a invalidação vem por ato (SPEC-007 RULE-KFH-009 (b)), não por selo |
| `version`, `expected_version`, `supersedes` | fora | M exclui sucessão; `supersedes` é conferido no item 4 |
| `targets_record_id` | fora | não está na lista de inclusão (null em `creation`) |
| `schema_version` | fora | não está na lista de inclusão |
| `canonical_ref`, `canonical_status`, `canonical_history_ref` | fora | não estão na lista de inclusão; `learning` não é canônico |
| `natural_key` | fora | não está na lista de inclusão. **Fica um risco** (ver Q-10 (c) e "Efeito sobre RU-3") |
| `school`, `hierarchy_role` | fora | só valem para hypothesis, e hypothesis via selo é proibida |
| `ontological_status` | fora | só vale para structure/regime/narrative |
| `provenance_ref.computed_by` | fora | M exclui `computed_by` |
| `provenance_ref.gate_record`, `.lineage`, `.who`, `.when`, `.why`, `.from` | fora | não estão na lista de inclusão |
| `publication.origin`, `publication.seal_ref` | fora | M exclui `publication.*` |
| `writer_id` | fora | M exclui |
| `relevance` | fora | só vale em `archival` |
| `created_at`, `valid_from`, `valid_to`, `recorded_at` | fora | carimbos de tempo (M exclui) |

### Tabela de projeção M — `relation_record` (parecer R1, A2/A3) `[PROPOSTA — leitura da RULE-KFH-005]`
| Campo do `relation_record` | M | Por quê |
|---|---|---|
| `formation.record_ref` (E-4) | **entra** | `record_ref` de M |
| (derivado) tipo do registro ⇒ `"relação"` | **entra** | `record_kind` de M |
| `relation_type` | **entra** | **premissa da Q-10 (a), PENDENTE.** É campo estrutural declarado: sem ele não se sabe se valem os "campos da RULE-CKG-008 quando CAUSA/SIMILAR_A". A RULE-KFH-005 não cita `relation_type` pelo nome. `[INFERÊNCIA]` |
| `from_node` | **entra** (como M.from) | `from` de M, pelo Mapa de formato |
| `to_node` / `target_relation_id` | **entra** (como M.to) | `to` de M, pelo Mapa de formato |
| `causal.mechanism`, `.direction`, `.conditions`, `.regime`, `.posthoc_flag`, `.outcome_ref`, `.no_outcome` (+ justificativa) | **entra** se CAUSA | "campos da RULE-CKG-008 quando CAUSA". São os campos declarados `[INFERÊNCIA]` |
| `causal.outcome_timestamp`, `causal.formulated_at` | fora | a SPEC-006 diz que eles "NÃO vêm do payload": o KG os deriva de `recorded_at`. São tempos atribuídos pelo KG |
| `similarity_basis` | **entra** se SIMILAR_A | campo da RULE-CKG-008 |
| `formation.content`, `formation.formed_inference_claim_ids` (E-4) | **entra** | conteúdo e marca de inferência de M |
| `formation.content_claim_ids` (E-4) | fora | decisão de Andraus (Q-6): ponteiro de auditoria |
| `relation_id` | fora | ID atribuído pelo KG |
| `record_kind` (`creation \| …`) | fora | outro campo (ver nó) |
| `version`, `expected_version`, `supersedes`, `targets_record_id` | fora | sucessão (conferida no item 4) / fora da lista de inclusão |
| `provenance_ref.*`, `writer_id` | fora | M exclui `computed_by` e `writer_id`; o resto não está na lista de inclusão |
| `relation_confidence` | fora | escala própria do KG; não está na lista de inclusão |
| `valid_from`, `valid_to`, `recorded_at` | fora | tempos. `valid_from` faz parte da chave natural da relação, o que gera um risco (Q-10 (c)) |

**Divergência registrada com a SPEC-007 (parecer R1, A2/A7)** `[INFERÊNCIA — achado]`. Dois trechos da SPEC-007 descrevem o recálculo por **exclusão**, com uma lista mais curta que M:
- RULE-KFH-007 (ix): "recalcule o `record_hash` do registro recebido (sem `publication.*` e sem campos de sucessão)";
- EC-KFH-004, EVIDENCE (ii): "recalcula o record_hash do registro gravado no KG (sem publication.* e campos de sucessão)".

Se esses trechos forem lidos como H(canon(M(r))), que é a definição de `record_hash` na RULE-KFH-005, não há conflito. Lidos ao pé da letra, eles poriam no hash campos que estão fora de M, e a auditoria amostral (ii) acharia divergência em **todo** registro gravado. O resultado seria `seal_revocation_request` falso (falso alarme, nunca aceite falso). Esta errata segue a RULE-KFH-005, que é a fonte única. Ela **não edita a SPEC-007** (CC-02; ordem de serviço). O alinhamento desses dois trechos fica registrado para uma errata futura da SPEC-007; se e quando fazer isso é decisão de Andraus.

**Notas de precisão** `[INFERÊNCIA]`:
- **Por que o item 4.** Os campos de sucessão ficam **fora** do `record_hash` (RULE-KFH-007 (ix)). Sem o item 4 (a), um committer que contorne o pipeline poderia pegar conteúdo selado e pendurar nele um `supersedes` que Andraus não autorizou. Isso fere SPEC-007-SUCC-001 ("só Andraus autoriza troca de carimbado, por lote" — ROADMAP "Decisões FECHADAS"), e a RULE-CKG-012 não percebe, porque só confere a ordem das versões. O item 4 (b) é a **leitura desta errata** de "conferir contra" (Q-3) nos dois sentidos. Se o committer tirar o `supersedes` que o selo declarou, nasce um nó paralelo, que a SPEC-007 (vii) proíbe ("impede nó paralelo"). A RULE-CKG-012 ("mesma chave natural sem `supersedes` divergente ⇒ DENY") só barra isso se a `natural_key` não for mexida, e a `natural_key` fica fora de M. Se o Revisor ou Andraus lerem Q-3 só no sentido (a), basta retirar o 4 (b) e o caso ADV-21 (p).
- **Reuso do selo** (o mesmo registro selado enviado de novo): a RULE-CKG-012 já trata ("Reescrita idêntica = no-op"). **Decisão de Andraus (Q-4):** o KG **não** exige que o consumo do selo ainda esteja `RESERVADO`.
- **Códigos (decisão de Andraus, Q-5; parecer R1, A7): subcódigos do pai existente `ADMISSION_REJECTED` (§D3.1), cada um dizendo o que falhou.** `SEAL_REF_UNRESOLVABLE` = o selo não se resolve (ref ausente, mal formada, inexistente ou registro de selos indisponível). `SEAL_CONTENT_MISMATCH` = **o mesmo código** da SPEC-007 RULE-KFH-007 (ix), com o mesmo sentido (conteúdo ≠ selado), agora usado também pelo KG. `SEAL_RECORD_NOT_IN_SEAL` = o selo resolve, mas o `record_ref` não está em `sealed_records[]` (nome dado pelo que falhou, como Andraus mandou em Q-5). `SEAL_SUCCESSION_MISMATCH` = `supersedes` diferente da sucessão declarada no selo `[PROPOSTA — nome pela mesma regra de A7; Q-5 não cita este caso pelo nome]`. Nenhum código pai novo.

**Texto aditivo proposto: notas de propagação por referência (a regra é definida UMA vez, na RULE-CKG-010 acima)** `[PROPOSTA]`
- BASpec-CKG-010, MECANISMO, depois de "(b) gate (selo SPEC-007 presente)": *"[v1.13 — E-3] e conferido pelo committer (RULE-CKG-010, conferência do selo, itens 1–4)"*.
- EC-CKG-001, PRECOND, depois de "∨ selo SPEC-007 — CKG-010)": *"[v1.13 — E-3] (selo conferido: seal_ref resolve ∧ formation.record_ref ∈ sealed_records ∧ H(canon(M(r))) = record_hash selado ∧ supersedes ↔ succession_of do selo)"*.
- D4, item "Admissão (CKG-010)", depois de "(x formado ∧ selo SPEC-007)": *"[v1.13 — E-3] ∧ selo_conferido(x)"*.
- §D3.1, linha `ADMISSION_REJECTED`: acrescentar *"`SEAL_REF_UNRESOLVABLE`, `SEAL_RECORD_NOT_IN_SEAL`, `SEAL_SUCCESSION_MISMATCH` (v1.13 — E-3), `SEAL_CONTENT_MISMATCH` (v1.13 — E-3; código da SPEC-007)"*.
- I/O Schema, `node_record` e `relation_record`: campos `formation` (E-4) e, só no `relation_record`, `publication` (E-2(b)).

### Enforcement Contract — o que a E-3 muda no EC-CKG-001 (continua um EC só; o nível não muda)
```
CAPABILITY   : Gravar no KG permanente registro formado (nó ou relação) vindo do selo da SPEC-007 (caminho (b))
EFFECT       : Commit crítico/irreversível de conhecimento formado (append-only)
PRECOND      : PRECOND vigente do EC-CKG-001 AND, se publication.origin = spec007_seal:
               seal_ref resolve para publication_seal existente AND formation.record_ref ∈ sealed_records[] AND
               H(canon(M(r))) do registro recebido, projetado pela Tabela de projeção M (por inclusão), == record_hash
               selado (RULE-KFH-005) AND (supersedes presente ⇔ par em succession_of[] para o record_ref) AND, se
               presente, supersedes ≡ published_ref@version do par (Mapa de formato)
POSTCOND     : só se grava registro formado cujo conteúdo em M é igual ao validado e selado, com a sucessão que o selo
               declara; o registro gravado guarda publication.seal_ref e formation.record_ref, e a cadeia de
               auditoria vai até o selo (SPEC-007 D9)
POLICY       : RULE-CKG-009/010 (+ cláusula E-3); SPEC-007 RULE-KFH-005/007 (vii)/(ix), INV-KFH-01, SPEC-007-SUCC-001;
               atomic-spec §10.2
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo"; irreversível) — igual ao vigente
FAILURE-MODE : Fail-closed — ADMISSION_REJECTED com SEAL_REF_UNRESOLVABLE (incl. registro de selos indisponível) |
               SEAL_RECORD_NOT_IN_SEAL | SEAL_CONTENT_MISMATCH | SEAL_SUCCESSION_MISMATCH; nada gravado; log.
               Falso-DENY E3 por amostragem (ENF-07; limiar = gap aberto)
EVIDENCE     : por recusa: seal_ref, formation.record_ref, record_hash recalculado × selado, supersedes × par do
               selo, código; por aceite: record_hash recalculado gravado junto do log de commit; amostragem de
               falso-DENY (ENF-07)
```
**Classe/Mecanismo (CC-11; vem da BASpec-CKG-010, que não muda):** C (Constitutivo). É gate determinístico de igualdade de hash, de pertença e de igualdade de par; o LLM não participa. GATE DE SAÍDA = as 4 conferências. CRITÉRIO 4Es: Conformidade > Eficácia. Conteúdo trocado na memória permanente não tem volta, e o custo de um hash por registro não rebaixa o nível (Economicidade nunca acima de Eficácia). `[INFERÊNCIA]`

### Casos de verificação: letras novas em cenários/ADV que já existem (contagens não mudam) `[PROPOSTA]`
**Ponto de partida comum (parecer R1, A5):** candidato com duas afirmações: `c1` (literal da fonte, `formed_inference=false`) e `c2` (`formed_inference=true`). Nó `learning` com `record_ref = N1` e `content_claim_ids = [c1, c2]`, portanto `formed_inference_claim_ids = [c2]` (lista **não vazia**). Relação `CONFIRMA` com `record_ref = R1`, `from = N1` (mesmo selo), `to = KG-N-P` (nó que já está no KG) e `content_claim_ids = [c1]`. Selo `S@1` com `sealed_records = [{N1, nó, h1}, {R1, relação, h2}]` e `succession_of = []`. Committer autorizado e autenticado; as demais pré-condições do EC-CKG-001 estão satisfeitas. Para os casos de sucessão: selo `S2@1` que sela `N1` com `succession_of = [N1 → KG-N-X@2]` e ato SUCCESSION válido.
- **Cenário-CKG-T09 (d) — nó, positivo:** **DADO** N1 com `publication.origin = spec007_seal`, `seal_ref = S@1`, `formation.record_ref = N1` e conteúdo igual ao selado; **QUANDO** o committer grava; **ENTÃO** admitido; **VERIFICAÇÃO** `seal_checked == true`; `recomputed_record_hash == "h1"`; `admitted == true`.
- **Cenário-CKG-T09 (e) — relação, positivo:** **DADO** N1 já gravado como `KG-N-Z` (com `formation.record_ref = N1` e `seal_ref = S@1`) e R1 com `from_node = KG-N-Z`, `to_node = KG-N-P`, `seal_ref = S@1`, `formation.record_ref = R1`, conteúdo igual ao selado, e `relation_id`/`valid_from`/`relation_confidence`/`provenance_ref` livres; **QUANDO** o committer grava R1; **ENTÃO** M.from = `N1` (mesmo selo) e M.to = `KG-N-P`, e a relação é admitida; **VERIFICAÇÃO** `recomputed_record_hash == "h2"`; `admitted == true`.
- **Cenário-CKG-T09 (f) — sucessora declarada, positivo:** **DADO** N1 com `seal_ref = S2@1` e `supersedes = "KG-N-X-v2"`; **QUANDO** o committer grava; **ENTÃO** passa na conferência do selo (as regras RULE-CKG-012 continuam valendo); **VERIFICAÇÃO** `succession_matches_seal == true`.
- **ADV-CKG-21 (i):** `seal_ref` ausente, ou `S@9` que não existe ⇒ `SEAL_REF_UNRESOLVABLE`; **VERIFICAÇÃO** `written == false`.
- **ADV-CKG-21 (j):** `seal_ref = S@1`, mas `formation.record_ref = N2` (fora de `sealed_records`) ou sem `formation.record_ref` ⇒ `SEAL_RECORD_NOT_IN_SEAL`; `written == false`.
- **ADV-CKG-21 (k) — conteúdo trocado:** `seal_ref = S@1`, `formation.record_ref = N1`, texto de `formation.content` alterado ⇒ hash ≠ h1 ⇒ `SEAL_CONTENT_MISMATCH`; `written == false`.
- **ADV-CKG-21 (l) — marca de inferência apagada:** como (k), mas só `formation.formed_inference_claim_ids` muda de `[c2]` para `[]`. Como `c2` tem `formed_inference=true`, a lista selada não é vazia ⇒ hash ≠ h1 ⇒ `SEAL_CONTENT_MISMATCH`; `written == false`.
- **ADV-CKG-21 (m) — o QUANDO vale, mas a recusa NÃO deve acontecer:** N1 igual ao selado em tudo que entra em M. Difere só em campos fora de M: `node_id`, `record_kind = creation`, `schema_version`, `provenance_ref.*` (incl. `who`/`when`/`lineage`), `writer_id`, `created_at`/`valid_from`/`recorded_at`, `publication.seal_ref` válido e `formation.content_claim_ids` (fora do hash — Q-6) ⇒ **admitido** (sem recusa falsa); `recomputed_record_hash == "h1"`; `false_deny == false`. (A `natural_key` fica de fora deste caso de propósito: mudá-la é o risco declarado na Q-10 (c), não um comportamento desejado.)
- **ADV-CKG-21 (n) — sucessão não declarada:** N1 igual ao selado em `S@1`, com `supersedes = "KG-N-X-v2"`, mas `succession_of[]` de S@1 está vazio ⇒ `SEAL_SUCCESSION_MISMATCH`; `written == false`.
- **ADV-CKG-21 (o) — registro de selos indisponível** ⇒ `SEAL_REF_UNRESOLVABLE` com motivo `registry_unavailable` no log (fail-closed); `written == false`; `fail_closed == true`.
- **ADV-CKG-21 (p) — sucessão declarada e omitida:** N1 com `seal_ref = S2@1` e sem `supersedes` ⇒ `SEAL_SUCCESSION_MISMATCH`; `written == false`. O mesmo vale para `supersedes = "KG-N-X-v1"` (versão diferente da do par).
- **ADV-CKG-21 (q) — relação religada:** R1 com `seal_ref = S@1`, mas `to_node = KG-N-Q` ⇒ M.to ≠ selado ⇒ hash ≠ h2 ⇒ `SEAL_CONTENT_MISMATCH`; `written == false`.
- **ADV-CKG-21 (r) — relação sem `formation`:** R1 com `seal_ref = S@1` e sem bloco `formation` ⇒ `SEAL_RECORD_NOT_IN_SEAL` (não há `record_ref`); `written == false`.

**Efeito sobre RU-3:** com a E-3, a E-2(b) e a E-4, RU-3 **fecha para tudo o que está em M**, em nós e em relações. Ficam três riscos declarados `[INFERÊNCIA]`:
1. **Campos de identidade fora de M** (`natural_key` do nó; `valid_from` da relação, que faz parte da chave natural). Um committer que contorne o pipeline poderia mudar esses campos sem mudar o hash. A sucessão declarada continua protegida pelo item 4 (b), mas um nó novo sem sucessão poderia entrar com outra chave. Contenção: cadeia D9 a partir de `seal_ref` + auditoria amostral da SPEC-007. Ver Q-10 (c).
2. **Implementação:** um committer que não rode a conferência. Isso é falha de BUILD E3, que a auditoria amostral da SPEC-007 (EC-KFH-004 (ii)) detecta e que continua ativa. O texto de (ii) é mais estreito que M (ver "Divergência registrada").
3. **Premissas pendentes da Q-10** (a)/(b)/(c). (Q-4..Q-7 já foram decididas por Andraus.)

---

## E-4 — Bloco `formation` nos registros de nó e de relação (reduz RU-8; guarda o `record_ref`)

**Âncoras:** I/O Schema, `node_record` (os campos vão de `"node_id"` a `"recorded_at"`) e `relation_record` (os campos vão de `"relation_id"` a `"similarity_basis"`). Nenhum dos dois tem campo para o `record_ref`, para o conteúdo materializado por M ou para `formed_inference_claim_ids[]`. `[FONTE: specs/features/SPEC-006/plan.md]`

**Fato de origem:** pela RULE-KFH-005, M produz "cada registro = {`record_ref`, `record_kind`, campos estruturais declarados …, campos de CONTEÚDO := texto EXATO das afirmações de `content_claim_ids[]`, na ordem declarada, `formed_inference_claim_ids[]` := os `content_claim_ids` cuja afirmação tem `formed_inference=true` (…a marca de inferência chega ao registro publicado e entra no `record_hash` — RULE-EPI-01…)}". Pela RULE-KFH-005 (d), todo registro, nó ou relação, tem ≥1 `content_claim_id`. Portanto **relação também tem conteúdo**. RU-8 (SPEC-007 §7-bis): "marca de inferência (`formed_inference_claim_ids`) sem campo próprio no `node_record` da SPEC-006 até a errata E-4". `[FONTE — FATO NORMATIVO (baseline SPEC-007)]`

**Texto aditivo proposto (campo novo e opcional no `node_record` e no `relation_record`):** `[PROPOSTA]`

> *[Errata v1.13 — E-4]* `"formation"`: **opcional; só existe em registro com `publication.origin = spec007_seal`** (não aparece no caminho (a)). Vale igual para `node_record` e `relation_record`. Conteúdo: `{ "record_ref": "record_ref do registro em M e no selo (SPEC-007 RULE-KFH-005; sealed_records[])", "content": "campos de CONTEÚDO de M, exatamente como M os produz (texto exato das afirmações, na ordem declarada — RULE-KFH-005); a forma em bytes é a de M (BUILD) e nunca é reformatada", "content_claim_ids": ["…"], "formed_inference_claim_ids": ["… (lista vazia quando não há inferência)"] }`. O bloco é **dado de conteúdo do selo**, não regra nova: a SPEC-006 não o interpreta nem o julga. **A conferência da E-3 o cobre:** `record_ref`, `content` e `formed_inference_claim_ids` estão em M e, portanto, no `record_hash` (Tabelas de projeção M). O bloco não tem nem pode receber campo de convicção ou de custo (INV-04; RULE-CKG-007).

**Notas** `[INFERÊNCIA]`:
- **No caminho (b), na prática, o bloco é obrigatório.** Registro selado sem `formation` não tem `record_ref`, e a E-3 o recusa no item 2 (`SEAL_RECORD_NOT_IN_SEAL`; casos ADV-21 (j)/(r)). Por isso não é preciso uma regra "obrigatório" à parte (fonte única).
- **`content_claim_ids[]` dentro do hash.** A RULE-KFH-005 põe na saída de M o **texto** das afirmações e os `formed_inference_claim_ids`, mas não diz se a **lista** `content_claim_ids[]` também sai de M. **Decisão de Andraus (Q-6): fica fora do hash**, como ponteiro de auditoria, conferível pela cadeia D9 a partir de `seal_ref`. Portanto `content_claim_ids[]` **não** está coberto pelo hash, e a SPEC-007 não muda.
- **Efeito sobre RU-8:** a marca de inferência fica **no próprio registro do KG** (nó e relação) e entra na conferência da E-3 (caso ADV-CKG-21 (l)). Sobra um risco: quem lê o registro e **ignora** o bloco `formation`. **Decisão de Andraus (Q-7): não nesta errata** — a consulta (RULE-CKG-011/EC-CKG-006) não é obrigada a mostrar o bloco; a marca de inferência na consulta fica fora. RU-8 fica **menor, mas não some** (RULE-UNC-01).

---

## Herança/Delta desta errata (CC-08; RULE-HD-02/03/04)

- **INHERITS** (ID + versão): SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005): RULE-KFH-004 (`record_proposal`: `record_ref`, `record_kind{nó|relação}`, `from`/`to`, `content_claim_ids[]`); RULE-KFH-005 (M por inclusão, canon, H, `record_hash`); RULE-KFH-007 (vii) (`succession_of[]` = mapa `record_ref → published_ref@version`; "impede nó paralelo") e (ix) (`publication.origin`, `publication.seal_ref = seal_id@seal_version`, campos fora do hash); esquema `publication_seal` (`sealed_records[]`, `succession_of[]?`); RULE-KFH-020 (ato `ISSUER_LIST`); SPEC-007-SUCC-001. SPEC-006 v1.12 (DHR-SPEC006-004): RULE-CKG-005/008/009/010/012, BASpec-CKG-010, EC-CKG-001, §D3.1, I/O Schema `node_record`/`relation_record`.
- **ADDED:** nota E-1 (só caminho (b)); nota E-2; bloco `publication` no `relation_record` (E-2(b)); cláusula de conferência do selo na RULE-CKG-010 (E-3, itens 1–4), Mapa de formato, Tabelas de projeção M e notas de propagação; subcódigos `SEAL_REF_UNRESOLVABLE`, `SEAL_RECORD_NOT_IN_SEAL`, `SEAL_SUCCESSION_MISMATCH`; uso de `SEAL_CONTENT_MISMATCH` no KG; bloco `formation` no `node_record` e no `relation_record` (E-4); letras T09 (d)–(f) e ADV-CKG-21 (i)–(r).
- **MODIFIED:** nenhum. A E-3 **acrescenta** condição ao caminho (b) sem mudar o texto existente. No efeito ela é restritiva (Compatibilidade = Major).
- **REMOVED:** vazio.

**Evidência obrigação a obrigação (§7-bis Bloco B):**
| Obrigação herdada | Onde esta errata a cumpre |
|---|---|
| RULE-KFH-005: "UMA serialização canônica para toda a Spec … É UMA função só" | E-3 item 3 usa a MESMA canon/H, sem criar outra |
| RULE-KFH-005: M := {`record_ref`, `record_kind`, campos estruturais, conteúdo, `formed_inference_claim_ids`} (por inclusão) | Tabelas de projeção M (nó e relação), campo a campo; Mapa de formato para `record_ref`, `record_kind` e `from`/`to` |
| RULE-KFH-005: `record_ref` é saída de M | `formation.record_ref` (E-4), dentro de M e fora de `publication` (Mapa de formato) |
| RULE-KFH-005: hashes "nunca lidos do payload nem de campo de hash armazenado" | E-3 recalcula a partir do registro recebido; o hash de referência vem do selo, nunca do registro |
| RULE-KFH-005 (d): todo registro tem ≥1 `content_claim_id` (relação também tem conteúdo) | `formation` também no `relation_record` (E-4); casos T09 (e), ADV-21 (q)/(r) |
| RULE-KFH-007 (vii): `succession_of[]` = mapa `record_ref → published_ref@version`; "impede nó paralelo" | Mapa de formato (alvo da sucessão); E-3 item 4 (a) e (b) |
| RULE-KFH-007 (ix): `seal_ref = seal_id@seal_version`; campos de sucessão fora do hash | E-2 (formato); E-3 itens 1 e 4; Tabelas (sucessão = fora) |
| RULE-KFH-007 (ix): "A ESCRITA permanece sob RULE-CKG-009 pelo committer do KG" | E-1 e E-3 ("sob a RULE-CKG-009") |
| RULE-CKG-010 (b): formado sem selo ⇒ `FORMED_WITHOUT_SEAL` | mantido; a E-3 vem depois dele |
| RULE-CKG-010 (b): hypothesis via selo proibida (`HYPOTHESIS_VIA_SEAL_FORBIDDEN`) | não mexida; a E-3 não abre tipo novo |
| RULE-CKG-009: falha de auth ⇒ não autorizado (fail-closed) | E-3 item 1: registro de selos indisponível ⇒ `SEAL_REF_UNRESOLVABLE` (mesmo espírito) |
| RULE-CKG-012: compare-and-commit, sem fork; reescrita idêntica = no-op | não mexida; o item 4 vem antes dela; reuso fica com ela (Q-4) |

Nenhuma obrigação herdada foi removida ou enfraquecida. `[INFERÊNCIA — conferido lendo os textos citados]`

---

## Constitution Check (CC-01..CC-12) — só o que a errata toca

| CC | Resultado | Por quê |
|---|---|---|
| CC-01 | PASS | Hierarquia não muda; o selo só admite `learning` (SPEC-007 (iv-bis)); hypothesis via selo segue proibida |
| CC-02 | PASS | Não redefine CHM/CEM/CCM nem o selo; só faz referência à SPEC-007. A divergência com EC-KFH-004 (ii) fica registrada, sem editar a SPEC-007 |
| CC-03/CC-04 | PASS | Nenhum campo de convicção ou de custo; `formation` não tem convicção (INV-04) |
| CC-05 | PASS | CRITICAL (da SPEC-006) |
| CC-06/CC-07 | N/A | Não é Engineering Card |
| CC-08 | PASS | Herança/Delta acima, com evidência obrigação a obrigação |
| CC-09 | PASS | Riscos RU-3/RU-8 declarados com o que sobra; `content_claim_ids` fora do hash por decisão de Andraus (Q-6); pontos sem texto na SPEC-007 (`relation_type`, formato de `from`/`to`) ficam como premissa da Q-10, pendente, não como fato; nenhum número inventado |
| CC-10 | PASS | "selo", "selado" e "conferência" no sentido da SPEC-007; cada código diz o que falhou (A7); nenhum termo do GLOSSARIO redefinido |
| CC-11 | PASS | E-3 herda a Classe C da BASpec-CKG-010 (gate determinístico) |
| CC-12 | N/A | Infraestrutura sem escola (como a SPEC-006) |

---

## §7-bis — Redução de viés (CRITICAL)

**Bloco A — pergunta adversarial (E-3, a única parte com efeito):**
- *Se a E-3 estivesse errada, o que se veria?* (1) Recusa falsa de registro selado e válido, se a projeção M do KG for diferente da do pipeline: caso ADV-21 (m) para nó, T09 (e) para relação. O Mapa de `from`/`to` errado ou `relation_type` lido de forma diferente da do pipeline dá recusa falsa em **toda** relação (fail-closed, observável no T09 (e)). (2) Aceite de registro trocado, se a conferência deixar de fora campo que está em M: casos (k), (l), (q). (3) Sucessão pendurada ou omitida: casos (n), (p). Tudo isso se observa comparando o hash recalculado com o selado e o `supersedes` com o par do selo.
- *O ENTÃO pode ser conferido por um observador independente?* Sim. Com o selo e o registro recebido, qualquer um aplica as Tabelas de projeção M, recalcula H(canon(M(r))) e compara.
- *Existe QUANDO satisfeito sem que o ENTÃO deva acontecer?* Sim: registro que difere só fora de M. Está coberto pelo caso de negação (m) e pelos campos livres do T09 (e).

**Bloco C — epistêmico:**
- "Fecha RU-3 para o que está em M" é afirmação causal com mecanismo declarado (igualdade de hash sobre a mesma serialização e a mesma projeção). Não é correlação.
- O que sobra fica declarado como risco, não como resolvido: campos de identidade fora de M (`natural_key`, `valid_from` — Q-10 (c)); committer sem a conferência (implementação); leitor que ignora `formation` (RU-8 menor; Q-7 decidida: fora desta errata); divergência de texto com EC-KFH-004 (ii).
- Ficam INDETERMINADOS até a resposta de Andraus: `relation_type` em M e formato de `from`/`to` (Q-10 (a)/(b)). O texto usa premissas declaradas, não fatos.
- Nenhuma probabilidade ou número declarado. A taxa de amostragem continua INDETERMINADA (ENF-07, gap aberto).

**Bloco D:** a errata não executa nada e não cruza para a execução (INV-05). Toda dependência de Andraus ainda aberta está marcada como pergunta pendente com premissa (Q-10) ou como [DECISÃO NECESSÁRIA].

---

## CONS-01 — continuam ABERTAS (esta errata não fecha nenhuma)

G-001 · **K-001** · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · **host do juízo CKG-008** `[DECISÃO NECESSÁRIA]` · lista de escritores do caminho (a) `[DECISÃO NECESSÁRIA]` (fora desta errata por Q-1) · migração de ontologia `[DECISÃO NECESSÁRIA]` · timeout `PENDING_ANCESTOR` `[DECISÃO NECESSÁRIA]` · "produtor/gatilho de promoção trabalho→permanente" `[DECISÃO NECESSÁRIA]` · mecanismo de assinatura dos atos de Andraus (BUILD) · alinhamento do texto de EC-KFH-004 (ii)/RULE-KFH-007 (ix) da SPEC-007 à M por inclusão (encaminhamento de Andraus). A negação de `conviction` por padrão (DHR-SPEC006-003 D2) **não muda**. `[FONTE: DHR-RETRO-001 §3; DHR-SPEC006-004 §4; DHR-SPEC007-005 §5]`

Passo 11-bis / RMR-001: BL-003 e BL-011 seguem `ATIVADO` com Disposição PARCIAL (plan.md "Nota de gate"); BL-010/BL-029/BL-035 não mudam. A errata não promove item nem muda estado no painel. `[FONTE: specs/features/SPEC-006/plan.md "Nota de gate"]`

---

## Forma de aplicação depois da homologação — decidida (Q-8 = forma A)

Este arquivo **é** a errata, no mesmo padrão de arquivo à parte do `governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md`. Depois da homologação, o plan.md da SPEC-006 recebe **um ponteiro de uma linha**: uma linha 1.13 no Histórico de versões, apontando para `specs/features/SPEC-006/errata-v1.13.md`. As âncoras E-1..E-4 não são copiadas para dentro do plan.md e o texto baselined não muda. Assim, uma correção futura mexe em menos lugares (P2 em vigor; P4 ainda proposta — DHR-RETRO-001 §1). `[FONTE — decisão de Andraus, Q-8]`

---

## Perguntas para Andraus

**Decididas (incorporadas acima, sem ramo condicional):**
- **Q-1:** só o caminho (b) → E-1; o caminho (a) fica [DECISÃO NECESSÁRIA].
- **Q-2:** `publication` no registro de relação → E-2(b); com a E-4, a E-3 cobre relações.
- **Q-3:** conferir `supersedes` contra `succession_of[]` do selo → E-3 item 4. O sentido (b) (sucessão declarada e omitida) é leitura desta errata e está marcado na nota "Por que o item 4".
- **Q-8:** forma A → "Forma de aplicação".
- **Q-9:** Major → cabeçalho "Compatibilidade".
- **Q-4:** **não** exigir consumo `RESERVADO` → nota "Reuso do selo"; a repetição idêntica é no-op (RULE-CKG-012).
- **Q-5:** **sim**: subcódigos de `ADMISSION_REJECTED` → `SEAL_REF_UNRESOLVABLE` para selo não resolvido (o registro de selos indisponível entra aqui) e `SEAL_CONTENT_MISMATCH` reusado da SPEC-007. O caso "`record_ref` fora de `sealed_records`" leva o nome do que falhou: `SEAL_RECORD_NOT_IN_SEAL` (A7). Nota "Códigos". `SEAL_SUCCESSION_MISMATCH` segue a mesma regra, mas Q-5 não o cita pelo nome: está marcado `[PROPOSTA]`.
- **Q-6:** `content_claim_ids[]` **fora** do hash (ponteiro de auditoria) → Tabelas de projeção M; nota E-4.
- **Q-7:** **não** nesta errata (a marca de inferência na consulta fica fora) → E-4 "Efeito sobre RU-8".

**PENDENTE — com a premissa que o texto usa até a resposta:**
- **Q-10 (nova, aberta pelos achados A1/A2):** três pontos onde a RULE-KFH-005 não dá o texto exato. (a) `relation_type` entra em M? **Premissa: sim** (campo estrutural declarado). (b) Formato de `from`/`to` em M: `record_ref` para ponta do mesmo selo, id do KG para ponta que já existe? **Premissa: sim** (Mapa de formato). (c) `natural_key` do nó e `valid_from` da relação ficam fora de M? **Premissa: sim**, com o risco declarado em "Efeito sobre RU-3". Se a resposta de Andraus diferir da premissa em (a) ou (b), muda a Tabela de projeção desta errata (e, se preciso, a SPEC-007). Em (c), pôr esses campos em M seria mudança na SPEC-007.

---

## Tabela fato → locais (P2) — cada fato que se repete e onde ele aparece

Locais nesta errata e âncoras (por ID/texto) no baseline. Numa correção futura, corrigir **todos** os locais da linha. (O Anexo V1.0 é texto preservado e não entra nesta tabela.)

| Fato | Locais nesta errata | Âncoras no baseline da SPEC-006 (não editadas) |
|---|---|---|
| Decisões Q-1/2/3/8/9 de Andraus; registro em ata pendente | cabeçalho "Decisões de Andraus incorporadas"; E-1 "Escopo"; E-2(b); E-3 item 4; Compatibilidade; Forma de aplicação; Perguntas "Decididas" | — |
| Lista de quem grava no caminho (b) = aprovada por Andraus (P-1) = lista de emissores do selo | E-1 (texto aditivo); "O que continua aberto"; Herança INHERITS (RULE-KFH-020) | RULE-CKG-009 ("allowlist de escritores e quem hospeda o juízo CKG-008"); D6 ("concreta** de escritores = **[DECISÃO NECESSÁRIA]**"); Etiquetagem ("Allowlist de escritores / host do juízo CKG-008 / migração de ontologia"); lista final ("**Allowlist de escritores / host do juízo CKG-008 / migração de ontologia**"); §7-bis RULE-INQ ("selo SPEC-007, allowlist, host do juízo"); §7-bis Bloco D ("allowlist/host do juízo"); `checks.md` Itens em aberto ("allowlist de escritores; host do juízo CKG-008;") |
| Lista do caminho (a) segue [DECISÃO NECESSÁRIA] (Q-1) | E-1 (texto aditivo e "O que continua aberto"); CONS-01; Perguntas Q-1 | as mesmas sete âncoras da linha acima |
| Host do juízo CKG-008 segue [DECISÃO NECESSÁRIA] | E-1; CONS-01 | as mesmas sete âncoras |
| K-001 segue ABERTA | §0; E-1; CONS-01 | RULE-CKG-009 ("K-001/SPEC-018"); D6; Etiquetagem; lista final ("M-001 / J-001 / N-001 / G-001 / K-001") |
| Contrato do selo = SPEC-007 RULE-KFH-007 (ix), `seal_ref = seal_id@seal_version` | E-2 (nota); E-2(b); E-3 item 1; Mapa de formato (`seal_ref`); Herança INHERITS | I/O Schema `node_record.publication.seal_ref`; RULE-CKG-010 ("contrato do selo = DEPENDÊNCIA"); D6 1º item; Etiquetagem ("Contrato do selo de publicação"); lista final ("**Contrato do selo de publicação**"); Autopré-check ("selo SPEC-007 marcado"); `checks.md` Itens em aberto ("selo de publicação (SPEC-007);") |
| `publication` no `relation_record` (Q-2) | E-2(b); E-3 cláusula ("nó ou de relação"); propagação (I/O Schema); Herança ADDED | I/O Schema `relation_record` |
| `record_ref` mora em `formation.record_ref`, dentro de M, fora de `publication` | Mapa de formato; E-3 item 2; Tabelas (1ª linha); E-4 texto e notas; EC delta PRECOND/EVIDENCE; Herança (tabela); casos (j)/(r) | I/O Schema `node_record`/`relation_record` |
| Alvo da sucessão: `supersedes` `KG-…-v<n>` ≡ `published_ref@<n>` | Mapa de formato; E-3 item 4; EC delta PRECOND; casos T09 (f), ADV-21 (n)/(p) | I/O Schema `supersedes` (nó e relação) |
| M por inclusão; Tabelas de projeção M (nó, relação) | E-3 item 3; Tabelas; Herança (tabela); ADV-21 (m); T09 (e); §7-bis Bloco A | — (fonte única: SPEC-007 RULE-KFH-005) |
| Pontas da relação: M.from/M.to pelo Mapa (premissa da Q-10 (b)) | Mapa de formato; Tabela relação; T09 (e); ADV-21 (q); Q-10 | I/O Schema `relation_record.from_node/to_node/target_relation_id` |
| `relation_type` em M (premissa da Q-10 (a)) | Tabela relação; §7-bis Bloco A/C; CC-09; Q-10 | I/O Schema `relation_record.relation_type` |
| `natural_key`/`valid_from` fora de M = risco (Q-10 (c)) | Tabela nó/relação; "Efeito sobre RU-3" item 1; nota "Por que o item 4"; ADV-21 (m) (exclusão); §7-bis Bloco C; Q-10 | I/O Schema `natural_key`; RULE-CKG-008 (chave natural da relação) |
| Conferência do selo em 4 passos | E-3 cláusula; propagação; EC delta; Classe ("as 4 conferências"); casos T09 (d)–(f)/ADV-21 (i)–(r) | BASpec-CKG-010 MECANISMO; EC-CKG-001 PRECOND; D4 "Admissão (CKG-010)" |
| Códigos (Q-5): `SEAL_REF_UNRESOLVABLE` (incl. registro indisponível), `SEAL_RECORD_NOT_IN_SEAL`, `SEAL_SUCCESSION_MISMATCH` [PROPOSTA] + `SEAL_CONTENT_MISMATCH` reusado, sob `ADMISSION_REJECTED` | E-3 cláusula; nota "Códigos"; propagação §D3.1; EC delta FAILURE-MODE; casos ADV-21; Herança ADDED; Q-5 | §D3.1 linha `ADMISSION_REJECTED` |
| Item 4 (b) = leitura de Q-3 nos dois sentidos | E-3 item 4; nota "Por que o item 4"; ADV-21 (p); Perguntas Q-3 | RULE-CKG-012 (não editada) |
| Divergência com SPEC-007 EC-KFH-004 (ii)/RULE-KFH-007 (ix) (exclusão × inclusão) | "Divergência registrada"; "Efeito sobre RU-3" item 2; CC-02; §7-bis Bloco C; CONS-01 | — (texto da SPEC-007, não editado) |
| RU-3 fecha para o que está em M (nós e relações) | "Efeito sobre RU-3"; E-2(b) "Ligação"; §7-bis Bloco C | — (RU-3 é da SPEC-007) |
| `formation` = `record_ref` + `content` + `content_claim_ids[]` + `formed_inference_claim_ids[]`, em nó e relação | E-4 texto e notas; Tabelas; ADV-21 (l)/(r); Herança ADDED | I/O Schema `node_record`/`relation_record` |
| `content_claim_ids[]` fora do hash (decidido, Q-6) | Tabelas; E-4 nota; ADV-21 (m); §7-bis Bloco C; Q-6 | — |
| RU-8 menor, não eliminado; consulta não obrigada a mostrar `formation` (decidido, Q-7) | E-4 "Efeito sobre RU-8"; §7-bis Bloco C; Q-7 | — (RU-8 é da SPEC-007) |
| Reuso do selo = no-op; sem exigir `RESERVADO` (decidido, Q-4) | nota "Reuso do selo"; Herança (RULE-CKG-012); Q-4 | RULE-CKG-012 ("reescrita idêntica = no-op") |
| Compatibilidade = Major (Q-9) | cabeçalho; Herança MODIFIED; Perguntas Q-9 | Histórico de versões linha 1.11 |
| Forma A: ponteiro de uma linha no plan.md (Q-8) | Forma de aplicação; Verificação (assert-present) | Histórico de versões |
| Nenhum ID novo de RULE/BASpec/EC/T/ADV; contagens 13/6/13/19/23 sem mudança | §0; casos ("letras novas"); Herança ADDED | Histórico de versões linha 1.12 (contagens) |

---

## Registro de mudanças v1.0 → v1.1 (por achado do parecer R1)

| Achado | O que mudou |
|---|---|
| A1 (Média) | `record_ref` passa a morar em `formation.record_ref`, dentro de M (Mapa de formato); E-3 item 2 usa esse campo; mapa `supersedes` ↔ `published_ref@version`; ADV (n) passa a usar `"KG-N-X-v2"` ≡ `KG-N-X@2` (a v1.0 usava `KG-N-X@2` como `supersedes`) |
| A2 (Média) | "excluindo tudo o que M exclui" vira M **por inclusão**; Tabelas de projeção M campo a campo (nó e relação); a nota "Lista de exclusão completa" sai; Herança linha 2 refeita; ADV (m) ampliado; divergência com EC-KFH-004 (ii) registrada |
| A3 (Média) | `formation` vai também para o `relation_record`; Tabela relação; casos T09 (e), ADV (q)/(r); RU-3 "fecha para o que está em M" em nós e relações, com os riscos que sobram |
| A4 (Média) | Q-1..Q-9 todas decididas por Andraus e incorporadas sem ramo condicional (Q-4..Q-7 respondidas no chat de 2026-10-25, depois da primeira redação desta v1.1); só Q-10 (nova, aberta por A1/A2) fica pendente, com premissa |
| A5 (Menor) | ponto de partida com `c2` (`formed_inference=true`) e `formed_inference_claim_ids = [c2]`; ADV (l) discrimina |
| A6a (Menor) | já aplicado pelo Orquestrador (Ficha-M); mantido no cabeçalho "Âncoras" |
| A6b (Menor) | "(P2/P4)" vira "(P2 em vigor; P4 ainda proposta — DHR-RETRO-001 §1)" em "Forma de aplicação" |
| A7 (Menor) | códigos dizem o que falhou: `SEAL_RECORD_NOT_IN_SEAL` (antes `SEAL_REF_UNRESOLVABLE` para registro fora do selo — Q-5), `SEAL_SUCCESSION_MISMATCH` (antes `SEAL_CONTENT_MISMATCH` para sucessão — [PROPOSTA]); registro de selos indisponível continua em `SEAL_REF_UNRESOLVABLE` (Q-5: "selo não resolvido"), com motivo no log; divergência com EC-KFH-004 (ii) registrada |
| Fora do parecer | "Forma de aplicação": a v1.0 previa uma linha no Histórico **e** um marcador no Status. Com Q-8 ("ponteiro de uma linha"), fica só a linha no Histórico |

---

## Verificação de spec desta errata (feedback interno — NÃO é parecer do Revisor nem homologação)

- As âncoras E-1..E-4 foram conferidas por busca de texto (Grep/Read) no `specs/features/SPEC-006/plan.md`: I/O Schema `node_record` e `relation_record` (l.1398-1452), §D3.1 linha `ADMISSION_REJECTED`, Cenário-CKG-T09 (letras (a)–(c) já existem) e ADV-CKG-21 (letras (a)–(h) já existem); na SPEC-007: RULE-KFH-004, RULE-KFH-005 (l.526-546), RULE-KFH-007 (vii)/(ix), esquemas `publication_seal`/"registro submetido" e EC-KFH-004. Os códigos novos não aparecem em nenhum arquivo de `specs/`. O Especificador **não** recalculou hashes (não tem Bash).
- Assertivas para o Orquestrador/Revisor. **Antes** da homologação, o plan.md da SPEC-006 continua sem nenhuma destas marcas: assert-absent:"Errata v1.13" · assert-absent:"SEAL_REF_UNRESOLVABLE" · assert-absent:"SEAL_RECORD_NOT_IN_SEAL" · assert-absent:"\"formation\"". **Depois** da homologação pela forma A: assert-present de uma única linha 1.13 no Histórico de versões apontando para este arquivo.
- **Gates — o Especificador NÃO os executou (não tem Bash):** `python scripts/validate_spec_sot.py specs/features/SPEC-006/plan.md` (o plan não muda; neste arquivo o script pode reprovar por estrutura, porque não é um Plan), `python scripts/check_refs.py`, `python scripts/check_invariants.py specs/features/SPEC-006/errata-v1.13.md`, `python scripts/revisor_gate.py specs/features/SPEC-006/errata-v1.13.md`, `python scripts/check_doc_sync.py`, `python scripts/build_map.py` + `--check`, `python -m unittest discover -s tests`. Ficam para o Orquestrador.

"VERIFY" interno ≠ CONFORME ≠ homologação.

**Pronto para revisão (v1.1).**

---

## Anexo V1.0 — texto integral da v1.0 (preservado — INV-07; NÃO VALE MAIS)

> Abaixo está, literalmente, o arquivo como estava antes desta v1.1: commit `ee50ecb` com a correção A6a aplicada pelo Orquestrador (Ficha-M R1). **Ele não vale; vale a v1.1 acima.** Códigos, casos, ramos condicionais e a forma "(P2/P4)" que aparecem aqui foram substituídos pela v1.1 (ver "Registro de mudanças"). Não use este anexo como âncora.

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
