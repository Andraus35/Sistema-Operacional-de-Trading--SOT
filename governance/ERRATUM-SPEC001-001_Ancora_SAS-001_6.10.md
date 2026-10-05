# ERRATUM-SPEC001-001 — Âncora de fonte: SAS-001 §6.7 → §6.10 (metadados de transporte) — erratum ADITIVO

| Campo | Valor |
|---|---|
| Spec afetada | SPEC-001 v1.1 (HOMOLOGADA — BASELINE, 2026-09-15) — **não reescrita** (INV-09); erratum aditivo (padrão ERRATUM-SPEC019-001 / ERRATUM-SPEC020-001). |
| Fundamento | Achado A-CK-09 do parecer do Revisor sobre a SPEC-005 (CONFORME, 2026-10-05) + ordem direta de Andraus (chat, 2026-10-05, "resolver"). |
| Data | 2026-10-05 |
| Compatibilidade | **Patch** (correção de âncora de citação; nenhum comportamento, BASpec, regra ou decisão alterado). |

## Texto do erratum
`specs/features/SPEC-001/plan.md` l.75 (tabela de fronteiras, linha "Orçamento de latência e entrega do Event Bus") cita `[FONTE: SAS-001 §6.7]` para a afirmação de que o produtor não tem autoridade para definir metadados de transporte (Latency/Freshness/Reliability/Expiration). A âncora correta é **`canon/SAS-001-structural-agent-spec.md` §6.10 — "Metadados Operacionais de Infraestrutura"** (l.917-918). O §6.7 é "Integração com o Cognitive Budget (CEE-001)" (l.908) e o §6.9 é "Integração com o Event Bus" (l.914). O conteúdo da afirmação (e a delegação à SPEC-005) permanece **correto**.

**Leitura vigente:** onde o `plan.md` da SPEC-001 diz "SAS-001 §6.7" nesse ponto, ler **SAS-001 §6.10** (e §6.9 para a integração com o Event Bus). O texto original não é alterado (INV-09).

## O que NÃO muda (CONS-01)
- Nenhuma BASpec, EARS, Enforcement Contract ou decisão aberta da SPEC-001 é alterada. A SPEC-005 (BASELINE v1.0, DHR-SPEC005-002) já cita as seções corretas (§6.9/§6.10).
- J-001, N-001, M-001, H-001, G-001, WF-D03, ECC-03-001 permanecem abertas.

## Rastreabilidade
`governance/DHR-SPEC005-002_Ata_Homologacao_SPEC-005.md` (§3, A-CK-09) · `specs/features/SPEC-005/plan.md` (CK-09/CEB-010) · `canon/SAS-001-structural-agent-spec.md` §6.7/§6.9/§6.10.
