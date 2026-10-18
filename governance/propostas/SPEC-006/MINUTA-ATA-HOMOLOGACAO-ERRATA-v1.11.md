# MINUTA — Ata de homologação da errata v1.11 da SPEC-006 (Cognitive Knowledge Graph)

> **[PROPOSTA] — minuta para Andraus. NÃO é ata, NÃO homologa nada, NÃO é baseline.** Só vale se Andraus a assinar no chat (AGENTS.md §10: a assinatura é a decisão dele registrada no chat e citada na ata). O número da ata é atribuído por quem registrar (não usar um id antes de a ata existir). Preparada pelo Orquestrador a pedido de Andraus (chat, 2026-10-18).

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-006/plan.md` + `checks.md` (errata **v1.11 PROPOSTA** sobre a baseline v1.7 — `DHR-SPEC006-002_Ata_Homologacao_SPEC-006.md`); parecer do Revisor por delta: **CONFORME condicional** (`governance/propostas/PARECER-REVISOR-SPEC006-v1.11-2026-10-18.md`, `plan.md` sha256 `8527addb…` na revisão; n-d corrigido depois); parecer anterior sobre a v1.10: NÃO CONFORME (N-08 Média, agora FECHADA) |
| Data | a preencher na assinatura |
| Status | **a preencher: HOMOLOGADA — ERRATA v1.11 (Minor/aditiva)** *ou* **NÃO HOMOLOGADA** |
| Compatibilidade | **Major (mudança restritiva)** — escolha de Andraus no chat (2026-10-18): a v1.7 já admitia `conviction` por estado e a errata passa a **negá-la por padrão**, restringindo um contrato baselined (não é "aditiva"). Não redefine CHM-001/CEM-001/CCM-001 e não fecha decisão aberta. Homologada como errata com ata própria e ressalva expressa; a v1.7 permanece como registro histórico (INV-07) |
| RPSA-escopo | nao *(proposta: a errata não altera texto de agente)* |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de errata de Spec; não altera texto de agente. |

## 1. Decisão a registrar (preencher)
| # | Item | Decisão de Andraus |
|---|---|---|
| D1 | Homologar a errata v1.11 como errata da baseline v1.7 | ☐ sim ☐ não ☐ adiar *(falta a assinatura expressa de Andraus no chat)* |
| D2 | **Negação de `conviction` por padrão no KG** (`CONVICTION_HISTORY_UNDEFINED`) — decisão de Andraus no chat de **2026-10-17**, até então sem ata; esta ata a registra (n-c do parecer). **Condição de reversão:** vale até Andraus definir o histórico de estados da convicção (CCM-001/SPEC-003/M-001, abertas); a definição desse histórico reabre a regra. Fail-closed e reversível; **não fecha M-001** | ☑ registrar com condição de reversão *(escolha de Andraus, 2026-10-18)* |
| D3 | Classificação da errata | ☑ **Major (mudança restritiva)** *(escolha de Andraus, 2026-10-18)* |
| D4 | Condição de conformidade | ☑ homologar **com a condição escrita**: o parecer do Revisor é **CONFORME condicional**; **H-001 segue ABERTA** (divergência ROADMAP:177 × Q-ABERTURA-3 não resolvida); o gate de código foi rodado pelo **Orquestrador**, não pelo Revisor (a ferramenta do gate não está exposta ao Revisor em nuvem). Nada é apresentado como conformidade plena *(escolha de Andraus, 2026-10-18)* |

## 1-bis. Evidência amarrada (escolha de Andraus, 2026-10-18)
- `specs/features/SPEC-006/plan.md` sha256 `8527addb878d7585dbebdf66d376161af91d217c5f0f26c5355eb94a806beba6` — **idêntico** ao hash que o Revisor auditou por delta (base `ae3b819`, v1.10).
- Gate de código sobre esse `plan.md`: validate_spec_sot 13/13 PASS · revisor_gate **PASSOU_D**, 0 sinais H · check_invariants 0 achados (rodados pelo Orquestrador).
- `specs/features/SPEC-006/checks.md`: recebeu **somente a correção editorial n-d** (§17, linha m-A) **depois** do parecer; não foi reauditado pelo Revisor. Hash e commit a preencher na assinatura (`sha256sum`, commit `0e4275f` na linha de trabalho).

## 2. O que a errata v1.11 estabelece `[FATO, se assinada]`
- **N-08 (Média):** o núcleo causal imutável na cadeia `supersedes` inclui `outcome_ref`/`no_outcome` além de `mechanism`/`direction`/`conditions`/`regime` — em RULE-CKG-008, BASpec-CKG-008 (GATE DE SAÍDA), EC-CKG-005 (PRECOND, E3), esquema `causal` e ADV-04(h); m-A/m-B fechados.
- Menores n-a (assertivas do checks §17/§18 com limitação declarada), n-b (ADV-21(f) × CEM-001 l.460-466), n-c (procedência da negação de `conviction`), n-d (checks §17 sobre o D6) tratados.
- Contagens inalteradas: 13 BASpec · 13 EARS · 6 EC · 19 T · 23 ADV.

## 3. Permanecem ABERTAS (CONS-01) — nenhuma fechada por esta ata
**H-001** (mecanismo físico do KG; divergência ROADMAP:177 "Resolve H-001" × ata de abertura Q-ABERTURA-3 — decisão de Andraus: adiar/manter aberta, 2026-10-18) · M-001 · J-001 · N-001 · G-001 · K-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · histórico de estados da convicção. O teto de veredito do Revisor continua **CONFORME condicional** enquanto H-001 estiver aberta.

## 4. Depois da assinatura (para o Controlador)
Registrar a ata em `governance/`, classificá-la no RPSA (`check_rpsa.py --register`), atualizar a linha da SPEC-006 no `CATALOGO-OFICIAL.md`/`ROADMAP.md` **somente por ordem expressa de Andraus**, e regenerar o mapa (`build_map.py`).
