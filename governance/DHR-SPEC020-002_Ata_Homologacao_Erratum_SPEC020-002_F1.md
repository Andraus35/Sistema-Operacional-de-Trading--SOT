# DHR-SPEC020-002 — Ata de Homologação — ERRATUM-SPEC020-002 (dimensão B "RAG faithfulness", metade F1)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Baseline: `DHR-SPEC020-001` (SPEC-020) + `ERRATUM-SPEC020-001` (DHR-SPEC038-002). Ordem e respostas: `DHR-RETRO-001` §1, §2, §7. Origem: SPEC-007 plan v2.3 (`DHR-SPEC007-005` H-3; `DHR-SPEC007-003` P-5). Artefato: `governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md` (v1.2 + r3-1..r3-3). Pareceres: `governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R1..R3-2026-10-30.md` (R1 e R2 NÃO CONFORME; R3 **CONFORME condicional**) |
| Data | 2026-10-30 |
| Status | **HOMOLOGADO — ERRATUM-SPEC020-002 (Minor, prospectivo, aditivo).** Decisão direta de Andraus em chat (2026-10-30, AskUserQuestion): "Homologar como Minor (Recomendado)"; assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Homologação CONDICIONADA** (§3). |
| Compatibilidade | **Minor**, aplicação **prospectiva** (só Specs novas; molde CLASSE-MECH-001 / PRINC-BID-001 e CC-11/CC-12). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de erratum de Spec: não altera texto de agente. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-30)
| # | Item | Decisão |
|---|---|---|
| D1 | Homologar o erratum (inclui Q-1 texto do §1, Q-5 nota compartilhada com a F2, Q-6 número ERRATUM-SPEC020-002) | **Sim**, como **Minor** |
| D2 | Alcance (Q-3) | **Só daqui em diante.** "Teremos uma etapa futura de revisão das specs pretéritas" = intenção de Andraus, **sem ordem nem escopo**; não é decisão aberta nova |
| D3 | Estado do F1 (Q-2) | Critério definido; limiares INDETERMINADO; o Revisor dá o veredito como detector até existir gate |
| D4 | Forma de aplicação (Q-4) | Arquivo à parte + uma linha no fim do `plan.md` da SPEC-020 (editorial; nenhum enunciado, regra, BASpec, EC ou contagem alterado) |
| D5 | Gate determinístico para a parte literal do F1 (Q-9) | **Só registrar a lacuna** agora; propor em MELHORIAS-PROCESSO quando aparecer a primeira Spec que forma conhecimento |
| D6 | Calibração do F1 (Q-7) | Só registrar a lacuna (dependência de futura errata da SPEC-007) |

## 2. Evidência amarrada `[FATO]`
- `specs/features/SPEC-020/plan.md` sha256 **antes** da linha de ponteiro: `34fd309c755f656a8fc11ffdb3db078fbe3db9b251927cb6109012a47a6963fe`. Depois: `0737d7a45e9d0cd21c1e802192bf0577111207062fe1674ba97fb044d69d9b79` (difere só pela linha final, marcador editorial).
- `specs/features/SPEC-020/checks.md` — não editado.
- Erratum (v1.2 + r3-1..r3-3): sha256 `17a6e2a7b93e7b54580a8a616292c3cc46d5ce98e2a33645ae0b98d89ac7a1db`; após o marcador de Natureza desta ata: `d1728e44b3dbc6e31ad6a7e22b203adab7e5f94173cbe48da809245979bfb842`.
- Gates (Orquestrador): `check_doc_sync` ERRO=0 · `check_refs` 0 ERRO · `check_invariants` 0 · `revisor_gate` PASSOU_D · `validate_spec_sot` da SPEC-020 verde · coesão 0 ERRO · mapa em dia.

## 3. Condição de conformidade (o que esta homologação NÃO afirma)
Parecer **CONFORME condicional**: o `revisor_gate` não foi reproduzido pelo Revisor (rodou o Orquestrador); sha256 não recalculados por ele. Não há gate determinístico para a parte literal do F1 em tempo de Spec (lacuna registrada). Nenhuma conformidade plena é afirmada. Esta ata **não aplica** a metade F2 nem a rastreabilidade de decisão, e **não fecha** BL-017 (segue PARCIAL / `Em espera`).

## 4. Não aplicado nesta ata (passos à parte, só por ordem de Andraus)
Atualizações aditivas em `ROADMAP.md` §12 (linha da dimensão B / caminho crítico), nota em BL-017 no `RMR-001` e `CATALOGO-OFICIAL.md`; erratum da metade F2 (junto da SPEC-048); errata de re-apontamento; errata da SPEC-007 (calibração do F1 e itens anotados); etapa futura de revisão das Specs pretéritas.

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WORKFLOW-SOT-001 (residual WF-D03) · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção. **Nenhuma fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] linha de ponteiro no plan.md da SPEC-020 · [x] Natureza do erratum · [ ] merge do PR (assinatura)
