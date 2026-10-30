# DHR-SPEC006-005 — Ata de Homologação — Errata aditiva v1.13 da SPEC-006 (ligação com o selo da SPEC-007)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Baseline: `DHR-SPEC006-002` (v1.7) + `DHR-SPEC006-003` (v1.11) + `DHR-SPEC006-004` (v1.12). Ordem e respostas Q-1..Q-11: `DHR-RETRO-001` §1, §4, §5, §6. Origem: SPEC-007 plan v2.3 (`DHR-SPEC007-005` H-2; `DHR-SPEC007-004` P-13). Artefato: `specs/features/SPEC-006/errata-v1.13.md` (texto v1.3 + N5). Pareceres: `governance/propostas/SPEC-006/PARECER-REVISOR-SPEC006-ERRATA-v1.13-R1..R4-2026-10-25.md` (R1 e R2 NÃO CONFORME; R3 e R4 **CONFORME condicional**) |
| Data | 2026-10-25 |
| Status | **HOMOLOGADA — ERRATA v1.13 (Major, aditiva).** Decisão direta de Andraus em chat (2026-10-25, AskUserQuestion): "Homologar a errata (Recomendado)"; assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Homologação CONDICIONADA** (§3). |
| Compatibilidade | **Major** (Q-9; precedente DHR-SPEC006-003 D3): a errata restringe o que o KG aceita para registros vindos do selo. Aditiva: não altera texto baselined do plan.md/checks.md; contagens 13/6/13/19/23 sem ID novo. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de errata de Spec: não altera texto de agente. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-25)
| # | Item | Decisão |
|---|---|---|
| D1 | Homologar a errata v1.13 (E-1..E-4) | **Sim** |
| D2 | Forma de aplicação (Q-8) | Arquivo à parte (`errata-v1.13.md`) + ponteiro de uma linha no Status do `plan.md` (editorial; nenhuma regra/BASpec/EARS/EC/T/ADV/contagem alterada) |
| D3 | Ratificação do Revisor (R4) | `SEAL_SUCCESSION_MISMATCH` aplicado também ao item 4(b) (troca declarada pelo selo e omitida pelo registro): coberto por Q-11 e D1 |
| D4 | Dependências para futura errata da SPEC-007 | **Anotadas, não resolvidas:** submissão parcial de selo multi-registro; `valid_from` na chave natural da relação (SPEC-007 RULE-KFH-007 (vii)) × Q-10 (c); alinhamento do texto de (ix)/EC-KFH-004 (ii). Dependem de ordem futura de Andraus |

## 2. Evidência amarrada `[FATO]`
- `specs/features/SPEC-006/plan.md` sha256 **antes** do ponteiro: `dd5a609f30078515c673a9e66990c54ee0c5e2ab881b6bcc51d6a573579b6255` (igual à DHR-SPEC006-004 §2). Depois: difere só no marcador de Status.
- `specs/features/SPEC-006/checks.md` sha256 `1ee11bb7652f59dc5560bf115f78746b4cb3453c33971dcb605443e84b9506b5` (inalterado).
- `specs/features/SPEC-006/errata-v1.13.md` sha256 `eaed2401e43c465368cb60a3aae895154708ca26c91327c86b13c982ae0c9e32` (v1.3; N5 e Status editorial aplicados depois: hash final no commit desta ata).
- Gates (Orquestrador): `check_refs` 0 ERRO · `check_invariants` 0 · `revisor_gate` PASSOU_D · suíte completa OK · mapa em dia.

## 3. Condição de conformidade (o que esta homologação NÃO afirma)
Parecer **CONFORME condicional**, não pleno: o `revisor_gate` não foi reproduzido pelo Revisor (rodou o Orquestrador); o painel RMR-001 não foi reconferido no R4 (herdado do R3); contagens 13/6/13/19/23 e fidelidade do Anexo V1.0 não verificáveis pelo Revisor. A taxa de amostragem de auditoria segue INDETERMINADA. Nenhuma conformidade plena é afirmada.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 (host do juízo CKG-008 e lista de escritores do caminho (a) inclusive) · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. **Nenhuma fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] ponteiro no Status do plan.md · [x] Status da errata · [ ] merge do PR (assinatura)
