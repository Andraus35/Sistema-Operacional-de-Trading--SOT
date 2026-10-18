# MINUTA — Ata de homologação da errata v1.11 da SPEC-006 (Cognitive Knowledge Graph)

> **[PROPOSTA] — minuta para Andraus. NÃO é ata, NÃO homologa nada, NÃO é baseline.** Só vale se Andraus a assinar no chat (AGENTS.md §10: a assinatura é a decisão dele registrada no chat e citada na ata). O número da ata é atribuído por quem registrar (não usar um id antes de a ata existir). Preparada pelo Orquestrador a pedido de Andraus (chat, 2026-10-18).

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-006/plan.md` + `checks.md` (errata **v1.11 PROPOSTA** sobre a baseline v1.7 — `DHR-SPEC006-002_Ata_Homologacao_SPEC-006.md`); parecer do Revisor por delta: **CONFORME condicional** (`governance/propostas/PARECER-REVISOR-SPEC006-v1.11-2026-10-18.md`, `plan.md` sha256 `8527addb…` na revisão; n-d corrigido depois); parecer anterior sobre a v1.10: NÃO CONFORME (N-08 Média, agora FECHADA) |
| Data | a preencher na assinatura |
| Status | **a preencher: HOMOLOGADA — ERRATA v1.11 (Minor/aditiva)** *ou* **NÃO HOMOLOGADA** |
| Compatibilidade | **Decisão de Andraus** — proposta: Minor/aditiva (não redefine CHM-001/CEM-001/CCM-001; não fecha decisão aberta). Observação do Revisor: a v1.7 já admitia `conviction` por estado; a negação por padrão **restringe** isso — se Andraus considerar que isso não é aditivo, classificar como Major e tratar como Plan novo |
| RPSA-escopo | nao *(proposta: a errata não altera texto de agente)* |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de errata de Spec; não altera texto de agente. |

## 1. Decisão a registrar (preencher)
| # | Item | Decisão de Andraus |
|---|---|---|
| D1 | Homologar a errata v1.11 como errata da baseline v1.7 | ☐ sim ☐ não ☐ adiar |
| D2 | **Negação de `conviction` por padrão no KG** (`CONVICTION_HISTORY_UNDEFINED`) até Andraus definir o histórico de estados da convicção (CCM-001/SPEC-003/M-001, abertas) — decisão de Andraus no chat de **2026-10-17**, hoje **sem ata**; esta ata a registraria (n-c do parecer) | ☐ registrar ☐ não |
| D3 | Classificação Minor/aditiva (ver "Compatibilidade") | ☐ Minor ☐ Major |

## 2. O que a errata v1.11 estabelece `[FATO, se assinada]`
- **N-08 (Média):** o núcleo causal imutável na cadeia `supersedes` inclui `outcome_ref`/`no_outcome` além de `mechanism`/`direction`/`conditions`/`regime` — em RULE-CKG-008, BASpec-CKG-008 (GATE DE SAÍDA), EC-CKG-005 (PRECOND, E3), esquema `causal` e ADV-04(h); m-A/m-B fechados.
- Menores n-a (assertivas do checks §17/§18 com limitação declarada), n-b (ADV-21(f) × CEM-001 l.460-466), n-c (procedência da negação de `conviction`), n-d (checks §17 sobre o D6) tratados.
- Contagens inalteradas: 13 BASpec · 13 EARS · 6 EC · 19 T · 23 ADV.

## 3. Permanecem ABERTAS (CONS-01) — nenhuma fechada por esta ata
**H-001** (mecanismo físico do KG; divergência ROADMAP:177 "Resolve H-001" × ata de abertura Q-ABERTURA-3 — decisão de Andraus: adiar/manter aberta, 2026-10-18) · M-001 · J-001 · N-001 · G-001 · K-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · histórico de estados da convicção. O teto de veredito do Revisor continua **CONFORME condicional** enquanto H-001 estiver aberta.

## 4. Depois da assinatura (para o Controlador)
Registrar a ata em `governance/`, classificá-la no RPSA (`check_rpsa.py --register`), atualizar a linha da SPEC-006 no `CATALOGO-OFICIAL.md`/`ROADMAP.md` **somente por ordem expressa de Andraus**, e regenerar o mapa (`build_map.py`).
