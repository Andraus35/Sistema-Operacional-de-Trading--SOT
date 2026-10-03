# ERRATUM-SPEC020-001 — Fechamento da dimensão B "tool correctness" (BL-017) — erratum ADITIVO

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-020 (HOMOLOGADA — BASELINE, DHR-SPEC020-001) — **não reescrita** (INV-09); este erratum é aditivo (padrão ERRATUM-SPEC019-001). |
| Fundamento | Homologação da SPEC-038 (DHR-SPEC038-002, Andraus, 2026-10-03) + decisão direta de Andraus de fechar o item "no mesmo ato". |
| Item de backlog | BL-017 (`ATIVADO` — DHR-DEC-004 §1.1). |
| Data | 2026-10-03 |

## Texto do erratum
A dimensão B **`tool correctness`** (classe dependente-de-upstream; SPEC-020 plan.md "Classe B", ROADMAP §12/BL-017) passa a **FECHÁVEL e FECHADA**: o critério verificável de correção de ferramenta é a **conformidade ao contrato por-ferramenta da SPEC-038** — 10 campos (`Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas`); Observação com proveniência (nunca Evidência — INV-06); determinismo (barra em formação = INDETERMINADO); fail-closed; Enforcement Contracts **EC-TH-01..07**; casos adversariais **ADV-TH-01..07**.

## O que NÃO muda (CONS-01)
- **RAG faithfulness ↔ SPEC-007** e **decision traceability ↔ SPEC-014** permanecem **DIFERIDAS** (fecham nos pontos de dependência próprios).
- Nenhuma lente nem BASpec da SPEC-020 é alterada; o núcleo A e a 9ª lente `principle consistency` seguem como homologados.
- J-001, N-001, M-001, H-001, WF-D03, ECC-03-001 permanecem abertas.

## Rastreabilidade
`specs/features/SPEC-038/plan.md` (§ Plano de re-apontamento / erratum e emenda à SPEC-020) · `governance/DHR-SPEC038-002_Ata_Homologacao_SPEC-038.md` · `backlog/RMR-001_Painel_Backlog.md` (BL-017).
