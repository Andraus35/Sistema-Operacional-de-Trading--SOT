# DHR-SPEC048-002 — Ata de Homologação — Plan da SPEC-048 v1.4 (RAG Retrieval & Evidence Packet Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-048/plan.md` v1.4 + `checks.md` · pareceres do Revisor R1–R5 em `governance/propostas/SPEC-048/` (R5: **CONFORME condicional**, 0 Críticas, 0 Médias, 0 Menores novas; gate do Orquestrador PASSOU_D, suíte verde) · `DHR-SPEC048-001` (abertura) · `DHR-SPEC007-002/003/005` |
| Data | 2026-10-25 |
| Status | **PLAN v1.4 HOMOLOGADO — BASELINE** (decisão direta de Andraus em chat, 2026-10-25, por AskUserQuestion: "Homologar e mesclar"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). Homologação **CONDICIONADA** (§4). *[Estado anterior preservado — INV-07: "PROPOSTA — CANDIDATA; aguarda Revisor (rodada 5) e homologação de Andraus. NÃO é baseline"]* |
| Compatibilidade | Minor (não toca modelo canônico baselined nem Spec baselined) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de Plan de Spec em redação: não altera texto de agente nem método. |

## 1. Pontos decididos por Andraus `[FATO]`
| # | Ponto | Decisão |
|---|---|---|
| P-1 | Quem confirma em que modelo cada analista roda | **Só Andraus, analista por analista**, no mesmo momento em que confirma um modelo como "de casa". Até lá todo analista segue "fora" (fail-closed; Q-3) |
| P-2 | Como o pedido do analista chega aos modelos de busca | **Só como campos de lista fechada** (ativo, prazo, período, assunto do vocabulário do sistema), nunca frase livre. Até a errata correspondente, a busca por significado depende do desenho de BUILD do catálogo de templates |
| P-3 | Como ligar o resumo curto | **Fica para quando Andraus quiser ligar**; resumo segue DESLIGADO (RULE-RET-010). Forma do ato = errata aditiva à SPEC-007, em passo à parte |
| O-1 | Ordem do Plan | **Registrada nesta ata**: Andraus ordenou o Plan da SPEC-048 em chat, 2026-10-24 ("Plan da SPEC-048"); a correção das rodadas 1–4 foi coberta pela mesma ordem (m-12 do R1 atendido) |
| O-2 | REMOVED de RULE-CBP-002/004/005 | **Aceitos** como Herança/Delta, fundamentados na P-9 (DHR-SPEC007-003); formas remanescentes locais na SPEC-048. Nenhuma Spec baselined é editada: a SPEC-004 não muda |

## 2. Efeitos da homologação
- Plan v1.4 da SPEC-048 (12 RULE-RET, 1 INV, 12 BASpec, 12 EARS, 8 EC, 14 cenários, 23 ADV) é **BASELINE** da SPEC-048 (recuperação + contagem + pacote + entrega + F2); `plan.md` e `checks.md` com histórico e anexos preservados (INV-07).
- `ROADMAP.md` (slot da SPEC-048 e tabela do §25), `governance/CATALOGO-OFICIAL.md` e `plan.md` (cabeçalho) atualizados, texto anterior preservado. Estados do painel de backlog **não mudam** (sem promoção — só Andraus).

## 3. O que NÃO muda
- **Fail-closed continua**: sem atos de Andraus registrados (RIGHTS / EXT_TRANSMISSION / LOCAL_EXECUTOR) todo pedido recebe pacote vazio com a falta declarada; depende de BUILD (forma de confirmar a identidade de Andraus).
- **Não há BUILD** (fase spec-first). A SPEC-049 (WikiRAG Reading View) segue slot indicativo, NÃO aberta.
- **Não aplicados nesta ata** (passos à parte, por ordem expressa de Andraus): errata aditiva à SPEC-006 (E-1..E-4); emenda de fidelidade F2 à SPEC-020; errata de re-apontamento SPEC-002/003/006; errata à SPEC-007 (E7-1..E7-3: campos de lista fechada, forma do ato do resumo, vínculo analista↔modelo).

## 4. Condições de conformidade (o que a homologação NÃO afirma)
- O Revisor não executou o gate dentro da sessão (teto CONFORME condicional); o Orquestrador rodou os gates (exit 0, PASSOU_D) e a suíte. Citações `inteligencia-sot@0abd22e` e fontes web do Dossiê não foram conferidas pelo Revisor (clone/web fora da sessão).
- Positivos dependem de Fixture F0, dos atos de Andraus e do BUILD da autenticação.
- Seguem **sem resposta de Andraus** (não decididas aqui): confirmar que o Manager Agent conta como "quem pediu" a consulta.

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · "produtor/gatilho de promoção" · mecanismo da autenticação dos atos de Andraus (BUILD). **Nenhuma decisão aberta é fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] Confirmação de Andraus (chat 2026-10-25) · [x] ROADMAP · [x] CATALOGO · [x] plan.md (cabeçalho) · [ ] merge (PR, CI verde) · [ ] retrospectiva de fechamento SPEC-007/SPEC-048 (antes de abrir outra Spec) · [ ] errata SPEC-006 / emenda SPEC-020 / errata SPEC-007 (passos à parte) · [ ] abertura da SPEC-049 (só por ordem de Andraus)

---

**Andraus** — *homologação dada em chat, 2026-10-25; registro pelo Orquestrador.*
