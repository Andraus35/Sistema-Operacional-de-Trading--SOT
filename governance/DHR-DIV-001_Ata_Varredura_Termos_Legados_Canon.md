# DHR-DIV-001 — Ata de Varredura DIV: termos legados em documentos CANON BASELINED

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Instrução direta de Andraus (chat, 2026-10-01): autorização da ata de varredura DIV — anotar termos legados no canon baselined (achados H-11/H-12 da `AUDITORIA-HIGIENE-SPECS-2026-10-01.md`) |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA por instrução direta de Andraus em chat** — varredura DIV no molde já usado em `CEM-001` (DIV-CEM-*) e `CONSTITUTION.md` (DHR-TAX-001 Correção 3) |
| Compatibilidade | Minor — **SOMENTE comentários HTML** ao lado dos termos legados; **nenhuma alteração de texto normativo**; **nenhuma redefinição de modelo canônico** (CONST-01); texto histórico integralmente preservado (INV-07) |
| Autoridade-fonte | `governance/AUDITORIA-HIGIENE-SPECS-2026-10-01.md` H-11/H-12; `governance/ADR-MANAGER-001_...md` §2.1 (FATO NORMATIVO: nomes legados não aparecem como componentes independentes); `governance/ADR-CONFLUENCE-001-v3` (FCE extinto → `confluence-elliott`); `governance/DHR-ARQ-001_...md`; `governance/DHR-ARQ-002_...md`; `canon/CEM-001-...md` (molde DIV-CEM-*) |
| Não fecha | Nenhuma decisão aberta (CONS-01). Não reescreve canônico. Não promove item de backlog. |

---

## 1. Problema

O `CEM-001` já foi anotado por DIV (DIV-CEM-3/DIV-CEM-4) porque **cita** componentes legados como produtor/consumidor. `CEE-001`, `SAS-001` e `PPQ-001` têm o mesmo tipo de menção (`Mission Engine`, `Master Orchestrator`, `Conviction Engine` como agente, `Fractal Confluence Engine (FCE)`), supersedidos por **ADR-MANAGER-001** / **ADR-CONFLUENCE-001 v3** / **DHR-ARQ-001/002**, mas **sem anotação DIV** — drift de rótulo entre o baseline de arquitetura e esses canônicos (achados **H-11** e **H-12** da auditoria de higiene, 2026-10-01). [FONTE: AUDITORIA-HIGIENE-SPECS-2026-10-01.md §2.]

## 2. Decisão

Aplica-se uma **varredura DIV** a `CEE-001`, `SAS-001` e `PPQ-001`: inserção de **comentários HTML** `<!-- DIV-xxx (2026-10-01): ... -->` ao lado de cada termo legado, apontando o sucessor canônico (Manager Agent / Fase / mecanismo / skill), **sem tocar o texto normativo** (CONST-01) e **preservando o histórico** (INV-07). Regra de leitura: onde o canônico mencionar o termo legado, o leitor deve substituí-lo pelo sucessor indicado na anotação (idêntico à regra do `GLOSSARIO.md §2-bis` e do `CATALOGO-OFICIAL.md`).

**Sucessores canônicos aplicados (todos já baselined):**
- `Mission Engine` → **Manager Agent — Fase 0 (Mission Lifecycle)** (ADR-MANAGER-001 / DHR-ARQ-002).
- `Master Orchestrator` → **Manager Agent** (ADR-MANAGER-001).
- `Conviction Engine` → **mecanismo legado** (Classe D/H do CCM-001) **invocado pelo Manager Agent — Fase 2** (DHR-ARQ-001) — não é agente/componente independente.
- `Fractal Confluence Engine (FCE)` → **skill `confluence-elliott`** do Structural Agent (ADR-CONFLUENCE-001 v3; FCE extinto).

## 3. Anotações aplicadas (arquivo:linha — texto normativo intocado)

| DIV ID | Arquivo | Linha (aprox.) | Termo legado anotado | Sucessor |
|---|---|---|---|---|
| **DIV-CEE-01** | `canon/CEE-001-cognitive-economy-efficiency-v2.0.md` | ~90 | Mission Engine | Manager Agent — Fase 0/1 |
| **DIV-CEE-02** | `canon/CEE-001-...md` | ~94 | Mission Engine | Manager Agent — Fase 0 |
| **DIV-CEE-03** | `canon/CEE-001-...md` | ~108 | Conviction Engine; Master Orchestrator | mecanismo (Manager Fase 2); Manager Agent |
| **DIV-CEE-04** | `canon/CEE-001-...md` | ~128 | Mission Engine | Manager Agent — Fase 0 |
| **DIV-SAS-01** | `canon/SAS-001-structural-agent-spec.md` | ~64 | Fractal Confluence Engine (FCE) | skill `confluence-elliott` (ADR-CONFLUENCE-001 v3) |
| **DIV-SAS-02** | `canon/SAS-001-...md` | ~866 | Conviction Engine; Mission Engine | mecanismo (Manager Fase 2); Manager Fase 0 |
| **DIV-SAS-03** | `canon/SAS-001-...md` | ~926 (título §6.13) | Conviction Engine | mecanismo (Manager Fase 2) |
| **DIV-SAS-04** | `canon/SAS-001-...md` | ~967 | Conviction Engine | mecanismo (Manager Fase 2) |
| **DIV-SAS-05** | `canon/SAS-001-...md` | ~1035 | Conviction Engine; Mission Engine | mecanismo (Manager Fase 2); Manager Fase 0 |
| **DIV-PPQ-01** | `canon/PPQ-001-project-process-quality.md` | ~35 | Mission Engine | Manager Agent — Fase 0 |
| **DIV-PPQ-02** | `canon/PPQ-001-...md` | ~105 | Mission Engine | Manager Agent — Fase 0 |
| **DIV-PPQ-03** | `canon/PPQ-001-...md` | ~111 | Master Orchestrator | Manager Agent |
| **DIV-PPQ-04** | `canon/PPQ-001-...md` | ~171 (título §6.3) | Mission Engine | Manager Agent — Fase 0 |
| **DIV-PPQ-05** | `canon/PPQ-001-...md` | ~282 (exemplo de prompt) | Master Orchestrator | Manager Agent |
| **DIV-PPQ-06** | `canon/PPQ-001-...md` | ~355 | Mission Engine | Manager Agent — Fase 0 |
| **DIV-PPQ-07** | `canon/PPQ-001-...md` | ~370 | Mission Engine | Manager Agent — Fase 0 |

> **Nota de ajuste (DHR-DEC-001, 2026-10-01):** por decisão de Andraus (chat, 2026-10-01), os comentários **DIV-CEE-04** (`canon/CEE-001`, diagrama `InferenceContextEnvelope` §6.1) e **DIV-PPQ-05** (`canon/PPQ-001`, exemplo de prompt §8.4) foram **movidos para FORA do respectivo bloco de código** (imediatamente acima da cerca ```` ``` ````). Motivo: comentário HTML inserido **dentro** de um bloco de código renderiza como texto literal, não como comentário — ficava visível no diagrama/prompt. O texto normativo/histórico do diagrama e do prompt permanece **intacto** (CONST-01/INV-07); apenas a posição da anotação mudou, com o conteúdo do ponteiro ao sucessor preservado. Os demais 14 DIV deste sweep (inline em prosa ou em notas, onde renderizam corretamente) não foram tocados.

**Escopo deste sweep = achados H-11 (CEE/SAS/PPQ) + H-12 (FCE em SAS-001).** As menções a FCE em `SAS-001` l.178/190/355 já eram **notas de correção** ([Correção 5]) que neutralizam o termo como referência agnóstica — **não re-anotadas** (já tratadas; anotar nota de correção seria redundante). `CEM-001` já estava anotado (DIV-CEM-3/4) — **não tocado**. `CONSTITUTION.md` (Mission Engine/Master Orchestrator) já anotado por **DHR-TAX-001** Correção 3 — **não tocado**. `SDD-001` tratado por DHR-TAX-001 Correção 1 (4D→8D) — fora de escopo DIV.

## 4. Achados de auditoria resolvidos

- **H-11** (termos legados em CEE-001/SAS-001/PPQ-001 sem anotação DIV) → **RESOLVIDO** (16 anotações DIV inseridas acima).
- **H-12** (FCE em SAS-001) → **RESOLVIDO** (DIV-SAS-01; l.178 já neutralizada por [Correção 5], mantida).

## 5. Guardas de sincronização (detector `check_doc_sync.py`)

- **CONST-01:** nenhum modelo canônico redefinido — apenas comentários HTML; todo texto normativo preservado.
- **INV-07:** nenhum texto apagado; nomes legados preservados in-loco como referência histórica com ponteiro ao sucessor.
- **D1/D2/D6:** nenhuma decisão aberta tocada; `WORKFLOW.md` não editado; nenhuma `WF-Dxx` tocada.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
