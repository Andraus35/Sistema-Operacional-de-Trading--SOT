# DHR-SPEC007-005 — Ata de Homologação — Plan reduzido da SPEC-007 v2.3 (formação + selo)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-007/plan.md` v2.3 + `checks.md` · pareceres do Revisor R1-R6 em `governance/propostas/SPEC-007/` (R6: **CONFORME condicional**, 0 Críticas, 0 Médias; condição "gate" cumprida pelo Orquestrador: `revisor_gate.py` completo = PASSOU_D) · `DHR-SPEC007-002/003/004` |
| Data | 2026-10-24 |
| Status | **PLAN REDUZIDO v2.3 HOMOLOGADO — BASELINE** (decisão direta de Andraus em chat, 2026-10-24, por AskUserQuestion: "Homologar o Plan reduzido v2.3"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). Homologação **CONDICIONADA** (§4). *[Estado anterior preservado — INV-07: "PROPOSTA — NÃO HOMOLOGADA … aguardando confirmação de Andraus"]* |
| Compatibilidade | Minor (não toca modelo canônico baselined nem Spec baselined) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de Plan de Spec em redação: não altera texto de agente nem método. |

## 1. Pontos decididos por Andraus `[FATO]` (chat, 2026-10-24, opções recomendadas)
| # | Ponto | Decisão |
|---|---|---|
| H-1 | Texto solto de fonte | **Vale a regra mais estrita do Plan**: nenhum modelo (em casa ou fora) recebe texto fora de `template_id` + referências registradas (RULE-KFH-019 (f3)); fecha o registro "mais estrita que a letra da ata" (r5-n2) |
| H-2 | Errata aditiva à SPEC-006 (E-1..E-4, P-13) | **Segue só como proposta**; redigida e homologada em passo à parte. Nenhum baseline tocado |
| H-3 | Emenda de fidelidade à SPEC-020 (metade F1) | **Fica para depois, em passo à parte**; só vale com ato de Andraus |
| H-4 | Invalidar conhecimento carimbado (INVALIDATION, r4-n8) | **Só Andraus**, como a troca (validade nunca muda sozinha nem em cascata); a [PROPOSTA] do Plan passa a decidida |

## 2. Efeitos da homologação
- Plan reduzido v2.3 da SPEC-007 (12 RULE-KFH, 2 INV, 12 BASpec, 12 EARS, 9 EC, 18 cenários, 22 ADV) é **BASELINE** da SPEC-007 reduzida (formação + selo); `specs/features/SPEC-007/plan.md` com Anexos T/R/H preservados (INV-07).
- `ROADMAP.md` (l.34 e tabela do §25), `governance/CATALOGO-OFICIAL.md` e `plan.md` (cabeçalho) atualizados, texto anterior preservado. BL-010/017/035: as Disposições [STRUCT-13] estão declaradas no Plan; os estados no painel **não mudam** (`Em espera`, sem promoção — só Andraus); BL-011 segue `ATIVADO`.

## 3. O que NÃO muda (mesmo se homologado)
- **Fail-closed continua a regra**: sem registro de ato de Andraus (ACTREC/LOCAL_EXECUTOR/RIGHTS/EXT_TRANSMISSION/ISSUER_LIST) nada é liberado, carimbado nem trocado; **a linha de montagem segue parada até a 1ª liberação real** e depende de BUILD (forma de confirmar a identidade de Andraus).
- **Não há BUILD** (fase spec-first). A SPEC-048 segue NÃO aberta. A errata à SPEC-006 e a emenda à SPEC-020 não são aplicadas. O Anexo T (parte da SPEC-048) é insumo, não vigente.

## 4. Condições de conformidade (o que a homologação NÃO afirma)
- O Revisor não executou o gate dentro da sessão dele (teto CONFORME condicional); o Orquestrador rodou o gate completo = PASSOU_D. 7 citações `inteligencia-sot@0abd22e` do Plan **não foram conferidas** (clone ausente) e a fidelidade dos Anexos ao v2.0/v2.1 não foi verificável sem git pelo Revisor (o Orquestrador conferiu a cópia do ADV-28 contra o commit anterior).
- Positivos de selo e CIM dependem da Fixture F0 (estado injetado), dos atos de Andraus e da forma de confirmar a identidade dele (BUILD).

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · "produtor/gatilho de promoção" (SPEC-006 `plan.md` l.976) · direito de uso do livro (Q7c) · forma de confirmar a identidade de Andraus (BUILD). **Nenhuma decisão aberta é fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] Confirmação de Andraus (chat 2026-10-24) · [x] ROADMAP · [x] CATALOGO · [x] plan.md (cabeçalho) · [ ] merge (assinatura) · [ ] errata SPEC-006 e emenda SPEC-020 (passos à parte) · [ ] abertura da SPEC-048 (só por ordem de Andraus)

---

**Andraus** — *4 pontos decididos e homologação dada em chat, 2026-10-24; registro pelo Orquestrador.*
