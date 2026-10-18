# DHR-SPEC006-004 — Ata de Homologação — Errata v1.12 da SPEC-006 (Cognitive Knowledge Graph)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Baseline: `DHR-SPEC006-002` (v1.7) + `DHR-SPEC006-003` (errata v1.11). Decisão que a errata propaga: `governance/DHR-H001-001_Ata_Fechamento_H-001_Mecanismo_Fisico_do_KG.md`. Artefato: `specs/features/SPEC-006/plan.md` + `checks.md` (errata v1.12). Parecer do Revisor por delta: **CONFORME condicional** (`governance/propostas/PARECER-REVISOR-SPEC006-v1.12-2026-10-18.md`). Delta: `governance/propostas/SPEC-006/DELTA-ERRATA-v1.12-2026-10-18.txt` |
| Data | 2026-10-18 |
| Status | **HOMOLOGADA — ERRATA v1.12 (Minor/aditiva).** Decisão direta de Andraus em chat (2026-10-18, AskUserQuestion): "Homologar como Minor/aditiva"; assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Homologação CONDICIONADA** (§3). |
| Compatibilidade | **Minor / aditiva** — escolha de Andraus (classificação proposta pelo Revisor). Atualiza o estado do COMO (H-001 fechada por Andraus fora da Spec); o QUE (RULE-CKG-001..013, INV-CKG-01/02, 13 BASpecs, 6 EC, 13 EARS, 19 cenários, 23 ADV, esquema, negação de `conviction`) não muda. A v1.11 permanece como registro histórico (INV-07). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de errata de Spec: não altera texto de agente. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-18)
| # | Item | Decisão |
|---|---|---|
| D1 | Homologar a errata v1.12 | **Sim** |
| D2 | Classificação | **Minor/aditiva** |
| D3 | Ciência do achado m3 (ADV-09) | A verificação spec-time do ADV-09 passa de "grep de fechamento = 0" para "toda menção ao fechamento atribui a Andraus/DHR-H001-001" — consequência necessária do fato novo; texto antigo preservado |
| D5 | Achado m6 do adendo do Revisor (Média, **pré-existente**, não introduzido pela v1.12): o plan dizia BL-003/BL-011 `Em espera`, mas o painel RMR-001 os registra `ATIVADO` (DHR-BACKLOG-001, 2026-10-17) | **Corrigir agora, uma linha** (plan.md l.51 e l.52, texto anterior preservado; classe M; sem regra nova). Aceita sem nova auditoria; o Revisor deixou a decisão (aceitar × reabrir) a Andraus |
| D4 | Correções pós-parecer (m1, m2, m4, m5) | Aceitas **sem nova auditoria** do Revisor (precedente: DHR-SPEC006-003 D5); texto prescrito pelo próprio parecer, aplicado pelo Orquestrador como classe M, sem regra/campo/mecanismo novo |

## 2. Evidência amarrada `[FATO]`
- `specs/features/SPEC-006/plan.md` sha256 `dd5a609f30078515c673a9e66990c54ee0c5e2ab881b6bcc51d6a573579b6255` — **difere** do auditado pelo Revisor (`479baab6…`): diferença = correções m1/m2/m4/m5 (9 linhas) **mais** o marcador de homologação no Status (edição editorial só dessa célula, feita por esta ata) **e a correção m6** (D5). Não reauditada.
- `specs/features/SPEC-006/checks.md` sha256 `1ee11bb7652f59dc5560bf115f78746b4cb3453c33971dcb605443e84b9506b5` — difere do auditado (`1081a4f2…`) pelas correções m1/m5 (4 linhas). Não reauditado.
- Gate de código (rodado pelo Orquestrador, não pelo Revisor): `validate_spec_sot` 13/13 PASS · `revisor_gate` **PASSOU_D** · `check_invariants` 0 achados.

## 3. Condição de conformidade (o que esta homologação NÃO afirma)
O parecer é **CONFORME condicional**, não pleno: o gate de código foi rodado pelo Orquestrador, não pelo Revisor; o detector `decisoes_abertas_fechadas` (`gate_extra.py`) não consulta o ROADMAP e foi contornado por reescrita neutra de 15 linhas (correção do detector autorizada por Andraus em PR à parte); os hashes finais não foram reauditados. A **eficiência de consulta multi-salto** da Opção C segue INDETERMINADA até o BUILD medir (DHR-H001-001 D5). Nenhuma conformidade plena é afirmada.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · timeout `PENDING_ANCESTOR`. **Nenhuma fechada por esta ata** (a H-001 foi fechada pela `DHR-H001-001`). A condição de reversão da negação de `conviction` (DHR-SPEC006-003 D2) permanece.

## 5. Registro
- [x] Esta ata · [x] plan.md Status (marcador) · [x] ROADMAP/CATALOGO · [ ] merge do PR (assinatura)

---

**Andraus** — *decisão em chat, 2026-10-18; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
