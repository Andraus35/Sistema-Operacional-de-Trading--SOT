# DHR-REAPONT-001 — Ata de Homologação — ERRATUM-REAPONT-001 (re-apontamento SPEC-007 → SPEC-048)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Regra de busca: `DHR-SPEC048-001` §1 Q-7. Divisão: `DHR-SPEC007-002` §3/§4; `DHR-SPEC007-004` P-14. Plan: `DHR-SPEC048-002`. Ordem e respostas: `DHR-RETRO-001` §1, §2 (item 3), §8, §9, §10. Artefato: `governance/ERRATUM-REAPONT-001_Re-apontamento_SPEC-007_para_SPEC-048.md` (v1.4). Pareceres: `governance/propostas/REAPONT/PARECER-REVISOR-ERRATUM-REAPONT-001-R1..R4-*.md` (R1 e R3 NÃO CONFORME; R2 e R4 **CONFORME condicional**) |
| Data | 2026-10-31 |
| Status | **HOMOLOGADO — ERRATUM-REAPONT-001 (Patch, editorial, aditivo, complexidade LOW).** Decisão direta de Andraus em chat (2026-10-31, AskUserQuestion): "Homologar como Patch (Recomendado)"; assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Homologação CONDICIONADA** (§3). |
| Compatibilidade | **Patch** (ajuste editorial; Q-2, DHR-RETRO-001 §8). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de errata de endereço: não altera texto de agente. |

## 1. Decisões de Andraus `[FATO]`
| # | Item | Decisão |
|---|---|---|
| D1 | Homologar o erratum (v1.4) | **Sim**, como **Patch** (LOW) |
| D2 | Forma (Q-1) | Arquivo único + **uma linha de ponteiro no fim** de cada plan.md afetado (SPEC-002, 003, 006, 007, 021, 038), uma linha por alvo com só as notas dele |
| D3 | Extensão (Q-3/Q-4) | Inclui a SPEC-021 e o trecho da SPEC-006 sobre a duplicação adiada |
| D4 | ROADMAP (Q-8) | **Duas notas aditivas** (§12 dimensões B; caminho crítico), texto anterior preservado. **CONFLICT-MAP não tocado** (só por ordem de Andraus) |
| D5 | Experiência (Q-9) | Recuperação de experiência (EXP-SPEC-015..020, 022) → **SPEC-009/017, endereço indicativo** (nota N-G na SPEC-006); não abre Spec nem decide G-001 |
| D6 | SPEC-020 / SPEC-007 (Q-5, Q-6) | SPEC-020 e ERRATUM-SPEC020-001 **sem nota nova**; SPEC-007 recebe a nota N-F (referência de linhas da nota C-3 atualizada 1:1; texto antigo preservado) |

## 2. Evidência amarrada `[FATO]` (sha256 antes → depois; difere só pela linha de ponteiro / nota aditiva)
| Arquivo | antes | depois |
|---|---|---|
| SPEC-002 | `04b9361ba7d3bdd7b47f05aeb798b3f85e40729116a62e70a3f27bc415c6bee8` | `372808de15bf6b51f17854e18c26f9aecc73346e6ecb2bbde73b357f5d2fced6` |
| SPEC-003 | `2faca8c1ce75b8ce2e61640336e88c42c2ac6f90a9c888259f3cbb46db7971cf` | `e023a7ca6c870b737451e74a67f7b0e578095097e28b441efa00346f90865895` |
| SPEC-006 | `c68c5e2f778995f87a6fc36800afcf338300618c78099b99692336a54c77a098` | `f4addd7d727304200d210f2ab5d1250524caf85305337ed2e10dce748e629a73` |
| SPEC-007 | `d711f9e69ddbe35f10436188b3a998e60d2316729b9b006de54c5931f56cf68c` | `d6f66b079a8d2330339e03c98dc373e8619d325d80a48b67c28a2190bda4aaa7` |
| SPEC-021 | `7c3f504fff6917f438634e184b1065d43f0654cea89a40123f941b591d1fe1ec` | `4d405d305ab0c1de279b97b41f215e66052d8149a8282674613a155d6998d870` |
| SPEC-038 | `cd83dae3cc4b4d201c7b80a97b1703059fdb8f4fa2f723b267ab5ddf011145cb` | `18f7ffc8cb6101718af2751a9211e6d0dea0ea99e90a42deb641cbb7b58e45b1` |
| ROADMAP | `4b76257489e4563781cff45d3593c412f16e1105a49a246d733d9e0a92339733` | `d09023a32ad4f7006313d99547d3e385df12be36311382347d92fde089ae0e33` |

Erratum (v1.4 + Natureza): sha256 `ce5786a2b4a3ef2eb4bd8e90ae38c82cd160cf433811efea8475d55af610b280` (antes do marcador de homologação desta ata). Gates (Orquestrador): `check_refs` 0 ERRO · `check_doc_sync` ERRO=0 · `check_invariants` 0 · `revisor_gate` PASSOU_D · coesão 0 ERRO · mapa em dia.

## 3. Condição de conformidade (o que esta homologação NÃO afirma)
Parecer **CONFORME condicional**: o `revisor_gate` não foi reproduzido pelo Revisor (rodou o Orquestrador); sha256 não recalculados por ele; CONFLICT-MAP/MAN-001/CATALOGO não reabertos no R4; L-19..L-30 e contagens R2 do §6 não reconferidos no R4 (não tocados pela v1.4). Nenhuma conformidade plena é afirmada. Esta ata **não** abre SPEC-009/017, **não** decide G-001 e **não** altera regra nenhuma.

## 4. Não aplicado (passos à parte, só por ordem de Andraus)
CONFLICT-MAP (COL-EXP-05 e entrada da SPEC-020); atualização do `CATALOGO-OFICIAL.md` e do `RMR-001` (BL-017); erratum da metade F2 (junto da SPEC-048); errata da SPEC-007 (calibração do F1, `valid_from` na chave natural, submissão parcial de selo, texto de (ix)); revisão futura das Specs pretéritas (intenção de Andraus, sem ordem).

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WORKFLOW-SOT-001 (residual WF-D03) · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção. **Nenhuma fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] ponteiros nos 6 plan.md · [x] 2 notas aditivas no ROADMAP · [x] Natureza do erratum · [ ] merge do PR (assinatura)
