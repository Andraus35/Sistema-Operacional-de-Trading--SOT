# [EMENDA-PROPOSTA] EMENDA-SPEC001-001 — Re-homologação pontual: campo `hierarchy_role` (separado de `hypothesis_type`)

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-001 v1.1 (HOMOLOGADA — BASELINE, 2026-09-15). Esta é uma **re-homologação pontual** (não erratum aditivo), porque muda o **contrato de campo** da hipótese. |
| Natureza | **Proposta** — pendente de parecer do Revisor e homologação de Andraus. Nada aplicado; nenhum commit. |
| Fundamento | Auditoria semântica (item 1): `hypothesis_type = PRIMARY \| SUB` na SPEC-001 **colide** com `hypothesis_type` do **CHM-001 §2.5**, que é uma *Governed Enumeration* (GMC-001) de valores {DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC}. A SPEC-001 sobrecarregou o nome de um campo canônico com outra semântica (papel hierárquico). Andraus decidiu **Opção A: campo novo `hierarchy_role`**. `[FATO: pauta item 1; CHM-001 l.289–293]`<br/>**Decisões de Andraus na sessão de auditoria (chat, 2026-10-05)** que fundamentam esta emenda e o erratum correlato: (a) Opção A — campo `hierarchy_role`; (b) o **mapeamento produtor→`hypothesis_type` é ADIADO** às Specs dos especialistas (capability **Specialist Harness** — slots indicativos SPEC-010 Elliott, SPEC-011 Fibonacci/Fractal, SPEC-012 SMC; EUA-E21) e **NÃO bloqueia** esta re-homologação; (c) o **erratum de identidade** (ERRATUM-SPEC001-002 item 2) é homologado/aplicado **ANTES** desta emenda (co-dependência — §0); (d) declaração global de status "especificado ≠ implementado ≠ verificado" no `governance/CATALOGO-OFICIAL.md`; (e) compatibilidade **Minor**; (f) **baixa de D-ECC-1 somente APÓS** homologação do erratum. `[FATO: sessão de auditoria em chat, 2026-10-05 — sem arquivo no repositório; DHR de rastreabilidade sugerido no §9]` |
| Decisão aplicada | **Opção A (campo novo):** separar `hypothesis_type` (semântica CHM-001, inalterada) de `hierarchy_role ∈ {PRIMARY, SUB}` (dimensão independente, coerente com `parent_hypothesis_id`/`generation` do CHM-001). |
| Data | 2026-10-05 |
| Compatibilidade | **Minor [PROPOSTA]** (justificativa abaixo). |
| Regime | Correção de contrato por re-homologação pontual (Crítico → Especificador → Revisor → Andraus), **não** erratum. A SPEC-001 **não é reescrita unilateralmente**: este documento é a proposta de delta a homologar. |

---

## 0. Co-dependência e ordem com o ERRATUM-SPEC001-002 `[FATO: decisão de Andraus, 2026-10-05]`

Esta emenda e o `ERRATUM-SPEC001-002_Auditoria_Semantica_Aditivo_PROPOSTO.md` são **co-dependentes em um único ponto** e têm **ordem decidida por Andraus**:

- **O ERRATUM (item 2 — identidade do produtor autenticada pelo runtime, código `PRODUCER_IDENTITY_MISMATCH`) é homologado e aplicado ANTES desta emenda.** Motivo: a PRECOND reescrita do EC-HH-001 (§3) passa a tratar `producer_id` como **identidade AUTENTICADA pelo runtime** — garantia que o erratum item 2 introduz. Sem o erratum item 2 homologado, a PRECOND desta emenda referenciaria uma garantia ainda não declarada.
- **Os itens 3, 5, 6 e 7 do ERRATUM independem desta emenda** (declaração global de status, histórico CCM-001, re-apontamento de refs a slots, nota da BASpec-HH-005) — podem ser homologados sem relação de ordem com a emenda.
- **Nenhuma outra dependência cruzada.** A migração de campo (`hypothesis_type`→`hierarchy_role`) é exclusiva desta emenda; o erratum não a toca.

> Os dois documentos citam-se mutuamente de forma coerente: este §0 ↔ ERRATUM §0 (co-dependência e ordem); §3 (PRECOND) ↔ ERRATUM item 2 (identidade autenticada).

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
| 1 | l.147 (EARS #1) | "...criar objeto com **hypothesis_type = PRIMARY** e epistemic_state = EMERGENT" | "...criar objeto com **hierarchy_role = PRIMARY**, hypothesis_type = «valor CHM-001 §2.5 — pendência herdada §8» [DECISÃO NECESSÁRIA], epistemic_state = EMERGENT" |
| 2 | l.175 (BASpec-HH-001 ENTÃO) | "- **hypothesis_type = PRIMARY**" | "- **hierarchy_role = PRIMARY**" + nova linha "- hypothesis_type = «valor CHM-001 §2.5 — pendência herdada §8» [DECISÃO NECESSÁRIA]" |
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

> **Regra normativa desta emenda quanto a `hypothesis_type` `[PROPOSTA]`:** a única obrigação que esta emenda impõe é **`hypothesis_type ∈ {DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC}` (enum CHM-001 §2.5)** — qualquer dos 4 valores é aceito. A emenda **NÃO impõe default** e **NÃO cria mapeamento produtor→`hypothesis_type`** (ex.: não decide que "Elliott ⇒ PREDICTIVE"). A escolha de *qual* valor cada produtor atribui é **pendência herdada com dono definido** — ver §8. A linha `producer_id` da PRECOND restringe apenas **autorização/identidade** (quem pode criar), não o **tipo** da hipótese.
>
> **Pré-condição de ordem:** a cláusula "`producer_id` = identidade AUTENTICADA pelo runtime" depende da homologação prévia do **ERRATUM-SPEC001-002 item 2** (§0).

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

## 8. Pendência herdada (com dono) — valor de `hypothesis_type` `[DECISÃO NECESSÁRIA]`

**Decisão de Andraus (2026-10-05):** o mapeamento produtor→`hypothesis_type` **NÃO é mais condição de fechamento** desta re-homologação. Esta emenda pode ser homologada; o valor concreto de `hypothesis_type` por produtor torna-se **pendência herdada, com dono definido**.

**Regra normativa que esta emenda fecha (sem pendência):**
> `hypothesis_type` DEVE pertencer ao enum do **CHM-001 §2.5** — {DESCRIPTIVE, EXPLANATORY, PREDICTIVE, DIAGNOSTIC}. **Qualquer** dos 4 valores é aceito pela SPEC-001 v1.2; **nenhum default é imposto** e **nenhum mapeamento produtor→tipo** é criado aqui. (CHM-001 §2.5 é *Governed Enumeration* sob GMC-001; o Especificador não escolhe o valor.)

**Pendência herdada (o que fica em aberto, com dono):**
> **[DECISÃO NECESSÁRIA — Andraus, na ABERTURA das Specs dos especialistas]:** qual valor de `hypothesis_type` (CHM-001 §2.5) cada produtor atribui —
> (a) a hipótese estrutural/direcional criada por Elliott; (b) as sub-hipóteses de SMC/Fibonacci.
> **Dono/momento:** Andraus decide **na abertura** (passo 1-bis do ROADMAP §23, após Dossiê de Pesquisa) das Specs da capability **Specialist Harness** — slots indicativos **SPEC-010 (Elliott)**, **SPEC-011 (Fibonacci/Fractal)**, **SPEC-012 (SMC)** (ROADMAP §SPEC-010..012). A âncora é a **capability "Specialist Harness"**; os números SPEC-010/011/012 indicam o **estado atual** do slot (slots indicativos, não-apagados — EUA-E21/RULE-ECC-01). Alternativamente, Andraus pode encaminhar à governança GMC-001.
> Até lá, os deltas desta emenda marcam o campo como `hypothesis_type = «valor CHM-001 §2.5 — pendência herdada §8» [DECISÃO NECESSÁRIA]`. A SPEC-001 permanece válida com a obrigação de enum acima; o valor concreto é preenchido quando a Spec do especialista correspondente for aberta.

**Condição de fechamento desta re-homologação (reescrita):** a homologação desta emenda **não aguarda** a decisão do valor de `hypothesis_type` — ela apenas **registra** a pendência herdada acima e seu dono. **CONS-01:** esta pendência é uma `[DECISÃO NECESSÁRIA]` **nova/herdada** — não fecha nenhuma decisão aberta e não pode aparecer como invariante fechado; a emenda não atribui valor algum.

---

## 9. Sugestão de rastreabilidade (ACH-005, opcional — Andraus decide) `[PROPOSTA]`

As decisões que fundamentam esta emenda e o erratum correlato foram tomadas **em chat** (sessão de auditoria, 2026-10-05), **sem arquivo no repositório** — o que o Revisor registrou como achado Menor de rastreabilidade (ACH-005). **Sugestão (não vinculante, decisão de Andraus):** abrir uma **ata DHR de sessão de auditoria** que registre, com data e autoria, as decisões de 2026-10-05 (hierarchy_role; erratum de identidade; declaração no CATALOGO; compat. Minor; ordem erratum→emenda; baixa de D-ECC-1 pós-erratum; mapeamento `hypothesis_type` adiado às Specs dos especialistas), à qual esta emenda e o erratum passariam a ancorar o `[FATO]`. O Especificador **não cria** essa ata (ato de Andraus / autoridade de homologação); apenas sugere.

---

## O que NÃO muda (CONS-01)

- Nenhuma decisão aberta é fechada: **J-001, N-001, M-001, H-001, G-001, K-001, C-001** permanecem ABERTAS.
- A **pendência herdada do §8** (valor de `hypothesis_type` por produtor) é uma `[DECISÃO NECESSÁRIA]` **nova/herdada com dono** (Andraus, na abertura das Specs dos especialistas) — **não fecha** decisão alguma e **não** aparece como invariante fechado em nenhuma parte desta entrega.
- CHM-001 não é redefinido (CC-02); INV-01/INV-02 (hierarquia; ICT não cria hipótese) preservados.
- Q-005 preservada (INV-07).

---

## Rastreabilidade

pauta da sessão de auditoria (decisão de Andraus em chat, 2026-10-05; sem arquivo no repositório) (item 1) · `canon/CHM-001-canonical-hypothesis-model.md` §2.5 (l.289–293), §1.8 (l.415), campos de hierarquia (l.164–168) · `specs/features/SPEC-001/plan.md` (l.147,175,179,191,201,212,401,409,421,425,712–713,825) · `specs/features/SPEC-001/checks.md` (l.105,116) · Q-005 (Questionário v1, 2026-09-14) · precedentes de compat. Minor (DHR-SPEC019/020/021/002/003/004/005-00x).

---

**[EMENDA-PROPOSTA] — Pronto para revisão.** Pendente de parecer do Revisor e de homologação de Andraus. A **pendência herdada do §8** (valor de `hypothesis_type`) **NÃO bloqueia** esta re-homologação — é `[DECISÃO NECESSÁRIA]` com dono (Andraus, na abertura das Specs dos especialistas SPEC-010/011/012). **Ordem decidida (§0):** o ERRATUM-SPEC001-002 (item 2) é homologado/aplicado **antes** desta emenda. Não aplicado; nenhum commit. A re-homologação, se homologada, produz a **SPEC-001 v1.2**.
