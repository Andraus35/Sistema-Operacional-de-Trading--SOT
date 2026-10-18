# DHR-SPEC006-003 — Ata de Homologação — Errata v1.11 da SPEC-006 (Cognitive Knowledge Graph)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Baseline: `governance/DHR-SPEC006-002_Ata_Homologacao_SPEC-006.md` (v1.7, 2026-10-13). Artefato: `specs/features/SPEC-006/plan.md` + `checks.md` (errata v1.11). Parecer do Revisor por delta: **CONFORME condicional** (`governance/propostas/PARECER-REVISOR-SPEC006-v1.11-2026-10-18.md`); parecer anterior sobre a v1.10: NÃO CONFORME (N-08 Média, FECHADA). Minuta: `governance/propostas/SPEC-006/MINUTA-ATA-HOMOLOGACAO-ERRATA-v1.11.md` |
| Data | 2026-10-18 |
| Status | **HOMOLOGADA — ERRATA v1.11 (Major, mudança restritiva) sobre a baseline v1.7.** Decisão direta de Andraus em chat (2026-10-18): "Sim, homologo a errata v1.11" (AskUserQuestion); assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Homologação CONDICIONADA** (ver §3). |
| Compatibilidade | **Major (mudança restritiva)** — escolha de Andraus (2026-10-18). A v1.7 admitia `conviction` por estado; a errata a **nega por padrão**, restringindo um contrato baselined. Não redefine CHM-001/CEM-001/CCM-001 e não fecha decisão aberta. A v1.7 permanece como registro histórico (INV-07) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de errata de Spec: não altera texto de agente. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-18)
| # | Item | Decisão |
|---|---|---|
| D1 | Homologar a errata v1.11 | **Sim** |
| D2 | Negação de `conviction` por padrão no KG (`CONVICTION_HISTORY_UNDEFINED`) — decisão de Andraus de 2026-10-17, até aqui sem ata, **registrada por esta ata** | **Registrar, com condição de reversão:** vale até Andraus definir o histórico de estados da convicção (CCM-001 / SPEC-003 / M-001, abertas); a definição desse histórico reabre a regra. Fail-closed e reversível; **não fecha M-001** |
| D3 | Classificação | **Major (mudança restritiva)** |
| D4 | Condição de conformidade | Homologar **com a condição escrita** (§3) |
| D5 | Evidência | Amarrada aos hashes abaixo (§2) |

## 2. Evidência amarrada `[FATO]`
- `specs/features/SPEC-006/plan.md` sha256 `8527addb878d7585dbebdf66d376161af91d217c5f0f26c5355eb94a806beba6` — **idêntico** ao hash auditado pelo Revisor na revisão por delta (base `ae3b819`, v1.10).
- `specs/features/SPEC-006/checks.md` sha256 `239a233e9ba4c2d18b82dfe499abf772553cedc17f8a8ca0a3bb12e17d647f4b` — recebeu **somente a correção editorial n-d** (§17, linha m-A) **depois** do parecer, sem nova auditoria do Revisor (aceito por Andraus, D5).
- Gate de código (rodado pelo Orquestrador): `validate_spec_sot` 13/13 PASS · `revisor_gate` **PASSOU_D**, 0 sinais H · `check_invariants` 0 achados · CI do PR #118 verde (merge `154a7e9`).

## 3. Condição de conformidade (o que esta homologação NÃO afirma)
O parecer do Revisor é **CONFORME condicional**, não pleno: **H-001 segue ABERTA** (divergência `ROADMAP.md:177` "Resolve H-001" × `DHR-SPEC006-001` Q-ABERTURA-3, não resolvida) e o **gate de código foi rodado pelo Orquestrador, não pelo Revisor** (a ferramenta do gate não está exposta ao Revisor em nuvem). Nenhuma conformidade plena é afirmada.

## 4. O que a errata v1.11 estabelece `[FATO]`
- **N-08:** o núcleo causal imutável na cadeia `supersedes` inclui `outcome_ref`/`no_outcome` além de `mechanism`/`direction`/`conditions`/`regime` — RULE-CKG-008, BASpec-CKG-008 (GATE DE SAÍDA), EC-CKG-005 (PRECOND, E3), esquema `causal`, ADV-04(h); m-A/m-B fechados.
- n-a, n-b, n-c, n-d tratados (n-e informativo). Contagens inalteradas: 13 BASpec · 13 EARS · 6 EC · 19 T · 23 ADV.

## 5. Permanecem ABERTAS (CONS-01) — nenhuma fechada por esta ata
**H-001 · M-001 · J-001 · N-001 · G-001 · K-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035)** · histórico de estados da convicção · divergência ROADMAP:177 × Q-ABERTURA-3.

## 6. Pendências (não decididas por esta ata)
- O cabeçalho/Status do `plan.md` ainda diz "ERRATA v1.11 PROPOSTA (aguarda Revisor e Andraus)". A homologação consta **desta ata**; atualizar o texto do cabeçalho muda o hash do `plan.md` e fica para o Especificador, por ordem de Andraus.
- `ROADMAP.md` e `CATALOGO-OFICIAL.md` **não** foram alterados por este ato (só por ordem expressa de Andraus).

## 7. Adendo (2026-10-18) — edição editorial pós-homologação do cabeçalho `[FATO]`
Por decisão de Andraus (chat, 2026-10-18, AskUserQuestion), o Especificador atualizou **somente** o cabeçalho/Status do `plan.md` ("PROPOSTA" → "HOMOLOGADA — ERRATA v1.11 (Major, condicionada)"). Edições: `plan.md` linhas 6, 7, 41, 54 e ~1646 (Versão, Status, histórico v1.11, Nota de gate, anotação de status na tabela de decisões abertas). **Nenhuma regra, BASpec, EARS, D4/D6, EC, T, ADV, schema, contagem ou decisão aberta foi alterada**; verificado por delta (4 de 122 blocos alterados: cabeçalho, histórico, nota de gate, etiquetagem).
- Hash **auditado/homologado** (§2): `plan.md` sha256 `8527addb878d7585dbebdf66d376161af91d217c5f0f26c5355eb94a806beba6`.
- Hash **após a edição editorial**: `plan.md` sha256 `0f461e88b744960a1dab7e8b1d9d6a0a75bd3932d46f8a7a4529761fe3d88155`; `checks.md` sha256 `239a233e9ba4c2d18b82dfe499abf772553cedc17f8a8ca0a3bb12e17d647f4b`.
- Gate sobre o `plan.md` atual: validate_spec_sot 13/13 PASS · revisor_gate PASSOU_D (teto CONFORME condicional) · check_invariants 0.
- Pendência §6 (cabeçalho) **satisfeita**. ROADMAP e CATALOGO registrados no mesmo PR por decisão de Andraus; a linha 177 do ROADMAP passa a dizer que o H-001 permanece ABERTA (texto anterior preservado como histórico, INV-07).
