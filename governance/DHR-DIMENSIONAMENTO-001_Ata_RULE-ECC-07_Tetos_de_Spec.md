# DHR-DIMENSIONAMENTO-001 — Ata de Decisão — RULE-ECC-07: dimensionamento de Spec (tetos medidos)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31): "Aplique os tetos ao método e abra um PR" · `governance/propostas/MELHORIAS-PROCESSO/PROPOSTA-DIMENSIONAMENTO-DE-SPEC-2026-10-31.md` §6 (pesquisa) e §7 (calibração com o ledger) |
| Data | 2026-10-31 |
| Status | **DECISÃO REGISTRADA** (ordem direta de Andraus em chat; AGENTS.md §10). Toca `atomic-spec.md`, `.claude/agents/especificador.md` e `governance/RULES.md` **por ordem expressa dele**. Prospectiva (INV-07). |
| Compatibilidade | Minor (acréscimo ao método de abertura; não toca modelo canônico nem decisão aberta). |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Altera o texto do agente Especificador (§5, regra de tamanho da Spec) e o método (atomic-spec §15). |

## 1. Decisão `[FATO]`
Passa a vigorar **RULE-ECC-07** (RULES.md), espelhada em `atomic-spec.md` §15 e em `especificador.md` §5:
| Parâmetro | Valor |
|---|---|
| Medida | linhas do **corpo normativo** do Plan (sem anexos de texto anterior, transferência e tabelas de rodada) |
| Alerta / teto | **1.900 / 2.000** linhas; acima do teto, divisão proposta a Andraus **antes do Plan**, por fronteira de contrato/capacidade |
| Confirmação prévia | estimativa > **1.600** linhas: Andraus confirma a decomposição antes do Plan |
| Gatilho processual | mudança de escopo/divisão depois de o Plan começar = nova abertura (Plan antigo congelado) |
| Referências | ~16 BASpecs por Spec; > 4 rodadas até 0 Média = revisão de processo no fechamento |
| Vigência | prospectiva, **desde a SPEC-049**; não retroage sobre Specs homologadas |

## 2. Ressalvas `[FATO]`
- Valores calibrados com **n=2 Plans** (SPEC-007, SPEC-048): marcos observados, não limiares estatísticos; alteráveis por emenda aditiva após 4–5 Specs medidas.
- **Não instituído:** check determinístico em `validate_spec_sot.py` e registro em `governance/MECANISMOS.json` (exigiria selo `GATE-MANIFEST` e ordem própria). Hoje a verificação é do Revisor (Detector, ENF-03).
- Não fechou nem abriu decisão alguma (CONS-01). A pesquisa externa (§6 da proposta) é preliminar, sem Dossiê formal (RULE-ECC-02/04); não é baseline.

## 3. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001.

## 4. Registro
- [x] Esta ata · [x] RULES.md · [x] atomic-spec.md · [x] especificador.md · [x] carimbo RPSA do Especificador · [ ] merge (assinatura)
