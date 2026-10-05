# [EMENDA-PROPOSTA] EMENDA-SPEC001-001 — Re-homologação pontual: campo `hierarchy_role` (separado de `hypothesis_type`)

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-001 v1.1 (HOMOLOGADA — BASELINE, 2026-09-15). Esta é uma **re-homologação pontual** (não erratum aditivo), porque muda o **contrato de campo** da hipótese. |
| Natureza | **Proposta** — pendente de parecer do Revisor e homologação de Andraus. Nada aplicado; nenhum commit. |
| Fundamento | Auditoria semântica (item 1): `hypothesis_type = PRIMARY \| SUB` na SPEC-001 **colide** com `hypothesis_type` do **CHM-001 §2.5**, que é uma *Governed Enumeration* (GMC-001) de valores {DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC}. A SPEC-001 sobrecarregou o nome de um campo canônico com outra semântica (papel hierárquico). Andraus decidiu **Opção A: campo novo `hierarchy_role`**. `[FATO: pauta item 1; CHM-001 l.289–293]` |
| Decisão aplicada | **Opção A (campo novo):** separar `hypothesis_type` (semântica CHM-001, inalterada) de `hierarchy_role ∈ {PRIMARY, SUB}` (dimensão independente, coerente com `parent_hypothesis_id`/`generation` do CHM-001). |
| Data | 2026-10-05 |
| Compatibilidade | **Minor [PROPOSTA]** (justificativa abaixo). |
| Regime | Correção de contrato por re-homologação pontual (Crítico → Especificador → Revisor → Andraus), **não** erratum. A SPEC-001 **não é reescrita unilateralmente**: este documento é a proposta de delta a homologar. |

---

## 1. Natureza do conflito `[FATO]`

- **CHM-001 §2.5** (`canon/CHM-001-canonical-hypothesis-model.md` l.289–293): `hypothesis_type` é *Governed Enumeration* sob GMC-001; valores aprovados = **DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC**. CHM-001 também possui os campos de hierarquia `parent_hypothesis_id`, `child_hypothesis_ids`, `sibling_hypothesis_ids`, `generation` (l.164–168, §1.8/l.415).
- **SPEC-001** usa `hypothesis_type = PRIMARY | SUB` (um conceito de **papel hierárquico**, Q-005), ou seja, reaproveita o nome do campo canônico com significado diferente.
- **Observação CHM-001:** PRIMARY/SUB **não** é um valor de `hypothesis_type` do CHM-001 — é uma decisão operacional do SOT (Q-005). O campo correto para expressar papel hierárquico deve ser **novo** e apoiar-se nos campos de hierarquia já existentes do CHM-001.

**Correção:** introduzir `hierarchy_role ∈ {PRIMARY, SUB}` como **dimensão independente**; `hypothesis_type` volta a carregar exclusivamente a semântica CHM-001 §2.5. Coerência:
- `hierarchy_role = PRIMARY` ⇒ `parent_hypothesis_id = null` **e** `generation = 0`;
- `hierarchy_role = SUB` ⇒ `parent_hypothesis_id != null` (hipótese PRIMARY válida) **e** `generation >= 1`.

---

## 2. Delta ponto a ponto (antes → depois) — `specs/features/SPEC-001/plan.md`

> Regra: todo ponto que hoje usa o **campo** `hypothesis_type` com valor PRIMARY/SUB passa a usar `hierarchy_role`. Narrativa conceitual "hipótese PRIMARY/SUB" (RULE-HH-001..004, títulos, tabelas de papéis) permanece — o conceito Q-005 não muda, só o campo que o carrega.

| # | Linha | Antes | Depois |
|---|---|---|---|
| 1 | l.147 (EARS #1) | "...criar objeto com **hypothesis_type = PRIMARY** e epistemic_state = EMERGENT" | "...criar objeto com **hierarchy_role = PRIMARY**, hypothesis_type = «valor CHM-001 §2.5» [DECISÃO NECESSÁRIA], epistemic_state = EMERGENT" |
| 2 | l.175 (BASpec-HH-001 ENTÃO) | "- **hypothesis_type = PRIMARY**" | "- **hierarchy_role = PRIMARY**" + nova linha "- hypothesis_type = «valor CHM-001 §2.5» [DECISÃO NECESSÁRIA]" |
| 3 | l.179 (BASpec-HH-001 ENTÃO) | "- parent_hypothesis_id = null (PRIMARY não tem parent)" | mantém + acrescenta "- generation = 0 (PRIMARY)" (coerência CHM-001) |
| 4 | l.191 (BASpec-HH-001 VERIFICAÇÃO) | "hypothesis.**hypothesis_type** == PRIMARY; hypothesis.producer_id == ..." | "hypothesis.**hierarchy_role** == PRIMARY; hypothesis.producer_id == ..." |
| 5 | l.201 (BASpec-HH-002 ENTÃO) | "- **hypothesis_type = SUB**" | "- **hierarchy_role = SUB**" |
| 6 | l.212 (BASpec-HH-002 VERIFICADO POR ENTÃO) | "...Hypothesis com parent_hypothesis_id = HYP-A1, **hypothesis_type = SUB**" | "...Hypothesis com parent_hypothesis_id = HYP-A1, **hierarchy_role = SUB**" |
| 7 | l.401 / l.409 (Cenário-HH-T01) | "**hypothesis_type = PRIMARY**" / "**hypothesis_type == PRIMARY**" | "**hierarchy_role = PRIMARY**" / "**hierarchy_role == PRIMARY**" |
| 8 | l.421 / l.425 (Cenário-HH-T02) | "**hypothesis_type = SUB**" / "**hypothesis_type == SUB**" | "**hierarchy_role = SUB**" / "**hierarchy_role == SUB**" |
| 9 | l.712–713 (EC-HH-001 PRECOND) | "(**hypothesis_type == PRIMARY** implies producer_id == \"elliott_specialist\") AND (**hypothesis_type == SUB** implies parent_id != null)" | ver PRECOND reescrita em §3 |
| 10 | l.825 (Apêndice A schema) | `"hypothesis_type": "PRIMARY \| SUB",` | duas chaves: `"hierarchy_role": "PRIMARY \| SUB",` **e** `"hypothesis_type": "DESCRIPTIVE \| EXPLANATORY \| PREDICTIVE \| DIAGNOSTIC",` (CHM-001 §2.5) |

### `specs/features/SPEC-001/checks.md`

| # | Linha | Antes | Depois |
|---|---|---|---|
| 11 | l.105 | "Sistema cria objeto Hypothesis com **hypothesis_type = PRIMARY**" | "...com **hierarchy_role = PRIMARY**" |
| 12 | l.116 | "Sistema cria Hypothesis com **hypothesis_type = SUB**, parent_hypothesis_id = [ID]" | "...com **hierarchy_role = SUB**, parent_hypothesis_id = [ID]" |

> **Não alterados (conceito preservado):** l.39, l.57, RULE-HH-001..004 (l.90–98), títulos de BASpec, tabela de produtores (l.360–362), seção Herança Fractal (l.657–668), tabela de decisões (l.779, l.804), checks.md l.117/l.269 — todos falam do **conceito** PRIMARY/SUB, não do campo. Permanecem como estão.

---

## 3. PRECOND reescrita do EC-HH-001 `[PROPOSTA]`

```
PRECOND : (producer_id in AUTHORIZED_PRODUCERS)                          -- producer_id = identidade
                                                                            AUTENTICADA pelo runtime
                                                                            (ver ERRATUM-SPEC001-002, item 2) AND
          (hierarchy_role == PRIMARY implies
                 producer_id == "elliott_specialist"
                 AND parent_hypothesis_id == null
                 AND generation == 0)                                     AND
          (hierarchy_role == SUB implies
                 parent_hypothesis_id != null
                 AND generation >= 1)                                     AND
          (hypothesis_type in {DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC})   -- CHM-001 §2.5
```

POSTCOND, POLICY, LEVEL (E2), FAILURE-MODE e EVIDENCE do EC-HH-001 **não mudam** — apenas a PRECOND passa a distinguir `hierarchy_role` (papel) de `hypothesis_type` (tipo CHM-001), e a amarrar coerência com `parent_hypothesis_id`/`generation`.

---

## 4. BASpecs / cenários / ADV afetados

- **BASpec-HH-001** (PRIMARY): ENTÃO e VERIFICAÇÃO migram para `hierarchy_role` (deltas #2–#4). PORQUE/REFERÊNCIA inalterados.
- **BASpec-HH-002** (SUB): ENTÃO e VERIFICADO POR migram para `hierarchy_role` (deltas #5–#6).
- **BASpec-HH-003** (bloqueio ICT): usa o **conceito** "hipótese (PRIMARY ou SUB)" (l.220) — **não** o campo; permanece. ICT não cria hipótese de nenhum papel.
- **Cenário-HH-T01 / T02**: deltas #7–#8.
- **ADV-HH-01** (l.505 "createHypothesis(type=PRIMARY | SUB)"): o parâmetro de chamada `type=` é ilustrativo; recomenda-se ler como `hierarchy_role=` após a emenda (ajuste editorial, não normativo). ADV-HH-02..08 não citam o campo `hypothesis_type`; inalterados.
- Nenhuma BASpec de transição de estado (HH-004..007) é afetada — `epistemic_state` é ortogonal a `hierarchy_role`.

---

## 5. Classificação de compatibilidade `[PROPOSTA]`

**Proposta: Minor.** Justificativa:
- **Aditivo + corretivo:** adiciona o campo `hierarchy_role` e realinha `hypothesis_type` ao enum canônico CHM-001 §2.5 — **sana** uma sobrecarga latente de nome de campo canônico (preocupação CC-02).
- **Comportamento preservado:** Elliott cria PRIMARY; SMC/Fibonacci criam SUB; ICT não cria — todas as regras Q-005 permanecem; só muda o campo que carrega o papel.
- **Sem quebra de consumidor `[FATO]`:** Grep em `*.json/*.yaml/*.yml`, em `schemas/` e em `rag/` → **nenhuma** ocorrência de `hypothesis_type`/`hierarchy_role`/`producer_id`; a auditoria confirma que SPEC-002..005 e o CCM-001 **não consomem** o campo. Logo não há contrato externo quebrado.
- **Fronteira (honestidade):** uma leitura estrita trataria "mudança de semântica de um campo existente" como **Major**. Como (a) não há consumidor e (b) o comportamento é preservado, proponho **Minor** — mas a classificação final é de **Andraus** (esta é uma `[PROPOSTA]`, não um fato). Precedente de Minor em re-homologações pontuais: SPEC-019/020/021/002/003/004/005.

---

## 6. Impacto downstream `[FATO/INFERÊNCIA]`

| Alvo | Impacto |
|---|---|
| SPEC-002 (CEM-001 Harness) | Nenhum — não consome `hypothesis_type` (Grep sem match). `[FATO]` |
| SPEC-003 (CCM-001) | Nenhum — convicção referencia a hipótese por ID; não lê o papel pelo campo. `[INFERÊNCIA]` |
| SPEC-004 (Blackboard) | Nenhum contrato quebrado; o objeto Hypothesis ganha um campo a mais, publicado como qualquer atributo de domínio (`domain_state` CHM-001 permanece intocado — CC-02). `[INFERÊNCIA]` |
| SPEC-005 (Event Bus) | Nenhum — transporta eventos, não valida o campo. `[INFERÊNCIA]` |
| `schemas/`, `rag/`, `*.json/*.yaml` | Nenhum — Grep sem ocorrência. `[FATO]` |
| CHM-001 | **Intocado** — não é redefinido (CC-02); a emenda, ao contrário, passa a **respeitar** §2.5. `[FATO]` |

---

## 7. Registro histórico da Q-005 (imutável — INV-07)

A decisão Q-005 (Elliott cria PRIMARY; SMC/Fibonacci criam SUB com `parent_id`; ICT não cria) **permanece registrada e válida**. Esta emenda **não reverte** Q-005 — apenas corrige **onde** o papel é armazenado (campo `hierarchy_role`, não `hypothesis_type`). O registro histórico da Q-005 (questionário v1, l.57/l.779/l.804 da SPEC-001, atas) **não é apagado nem reescrito** (INV-07). A SPEC-001 v1.1 permanece como versão histórica; a re-homologação produz a v1.2.

---

## 8. [DECISÃO NECESSÁRIA] de Andraus — valor de `hypothesis_type`

Separado o campo, **cada hipótese precisa de um valor de `hypothesis_type`** entre {DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC}. **CHM-001 §2.5 NÃO determina** qual valor uma hipótese estrutural de Elliott (ou uma SUB de SMC/Fibonacci) deve receber — é *Governed Enumeration* sob GMC-001, uma **decisão de domínio**. O Especificador **não escolhe**.

> **[DECISÃO NECESSÁRIA — Andraus]:** qual valor de `hypothesis_type` (CHM-001 §2.5) recebe:
> (a) a hipótese estrutural/direcional criada por Elliott (candidatos plausíveis: PREDICTIVE — projeta comportamento futuro — ou EXPLANATORY); e
> (b) as sub-hipóteses de SMC/Fibonacci.
> Enquanto não decidido, os deltas acima marcam o campo como `hypothesis_type = «valor CHM-001 §2.5» [DECISÃO NECESSÁRIA]`; a re-homologação **não** deve ser fechada antes desta decisão (CONS-01). Alternativamente, Andraus pode encaminhar à governança GMC-001.

---

## O que NÃO muda (CONS-01)

- Nenhuma decisão aberta é fechada: **J-001, N-001, M-001, H-001, G-001, K-001, C-001** permanecem ABERTAS.
- CHM-001 não é redefinido (CC-02); INV-01/INV-02 (hierarquia; ICT não cria hipótese) preservados.
- Q-005 preservada (INV-07).

---

## Rastreabilidade

pauta da sessão de auditoria (decisão de Andraus em chat, 2026-10-05; sem arquivo no repositório) (item 1) · `canon/CHM-001-canonical-hypothesis-model.md` §2.5 (l.289–293), §1.8 (l.415), campos de hierarquia (l.164–168) · `specs/features/SPEC-001/plan.md` (l.147,175,179,191,201,212,401,409,421,425,712–713,825) · `specs/features/SPEC-001/checks.md` (l.105,116) · Q-005 (Questionário v1, 2026-09-14) · precedentes de compat. Minor (DHR-SPEC019/020/021/002/003/004/005-00x).

---

**[EMENDA-PROPOSTA] — Pronto para revisão.** Pendente de parecer do Revisor e de homologação de Andraus (incluindo a [DECISÃO NECESSÁRIA] do §8). Não aplicado; nenhum commit. A re-homologação, se homologada, produz a **SPEC-001 v1.2**.
