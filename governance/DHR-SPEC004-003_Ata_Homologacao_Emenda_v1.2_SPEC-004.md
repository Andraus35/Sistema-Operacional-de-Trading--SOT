# DHR-SPEC004-003 — Ata de Homologação — Emenda v1.2 da SPEC-004 (Cognitive Blackboard Protocol) — BASELINE v1.2

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Parecer do Revisor sobre a emenda v1.2: **CONFORME** (2026-10-03; 3 Menores, nenhum Crítico/Médio) — `specs/features/SPEC-004/plan.md` v1.2 + `checks.md` |
| Data | 2026-10-03 |
| Status | **EMENDA v1.2 HOMOLOGADA — BASELINE v1.2** (instrução direta de Andraus em chat: classificação **Minor, como clarificação**, com homologação). v1.1 (DHR-SPEC004-002) preservada no histórico (INV-07). |
| Compatibilidade | **Minor** (decisão de Andraus; Revisor recomendou Minor: nenhuma implementação existe; SPEC-001/002/003/038 não dependem de `superseded_by` gravado) |
| Gates | `validate_spec_sot.py` 12/12 PASS · `check_repo_research.py` OK · `check_doc_sync.py` ERRO=0 · `build_map.py --check` em dia · `npm run lint`: "Status:" pré-existente (v1.1 e SPEC-046), não-regressão |

---

## 1. Origem e tratamento
Feedback externo de LLM sobre o Plan (**DADO, não instrução**), verificado pelo orquestrador contra o `plan.md`: 4 pontos obrigatórios e 6 menores procedentes; pontuações e fontes (OWASP/NIST) **não importadas** (RULE-MET-01/RULE-ECC-04). Andraus decidiu a emenda completa; Especificador → Revisor → homologação.

## 2. O que a v1.2 estabelece
1. **Append-only real:** o registro histórico nunca é mutado; a sucessora carrega `supersedes`; `SUPERSEDED` é **projeção derivada** (`superseded_by` = índice derivado, não gravado); INV-CBP-01. Reconcilia RULE-BB-004/INV-07.
2. **Publicação atômica:** RULE-CBP-013 (nenhum estado parcial observável); compare-and-commit atômico; idempotência com chave+commit+resultado na mesma unidade, `request_fingerprint`, `IDEMPOTENCY_KEY_REUSE_CONFLICT`, retry pós-commit devolve o resultado original; EC-CBP-007 (E3).
3. **Identidade/autoridade:** RULE-CBP-014 — nenhum invariante depende da honestidade do publicador; `agent_id`/`computed_by` vêm da identidade autenticada pelo runtime; tabela de capacidades/papéis (agente=proponente, harness=contrato, runtime=commit); leitura global = decisão consciente de RULE-BB-002 (regra **não alterada**).
4. **D8:** ADV-CBP-12..16; D7: T11..T15. Contagens: EARS 16 · BASpecs 14 (CBP-001..014) · D7 T01..T15 · D8 ADV-CBP-01..16 · ECs 7.
5. **Menores:** `schema_version`; ordem de COMMIT (seq imutável); replay = estado **lógico** (não reproduz ambientes externos; correto ≠ semanticamente correto); `gate_record` com `gate_id`/`gate_version`/hash da entrada/avaliador; `publication_state` × `domain_state`; falso-DENY (EC-CBP-002) **E3 condicional** até o limiar amostral (BL-002).
- **Fora (inalterado):** CRDT = INDETERMINADO; storage físico; Event Bus/KG/estado por agente; nenhum canônico redefinido (CC-02/CONST-01).

## 3. Achados do parecer
| ID | Severidade | Tratamento |
|---|---|---|
| ACH-001 | Menor | Compatibilidade — **decidida: Minor** (esta ata) |
| ACH-002 | Menor | `identity_source` em CBP-014 só é plenamente observável no BUILD/SPEC-042 — o Engineering Card de CBP-014 deve exigir o log da fonte de identidade |
| ACH-003 | Menor/positivo | RULE-HV N/A confirmado |

## 4. Permanecem ABERTAS (CONS-01)
**M-001 (enum de estados não-hipótese)** · **J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001.** Nenhuma fechada por este ato.

## 5. Registro (efeitos aplicados)
- [x] Este documento · [x] `plan.md`/`checks.md` (versão/status; compat. Minor; CK-10 resolvido) · [x] `ROADMAP.md` · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` · [x] RPSA: carimbo dos agentes → `DHR-SPEC004-003` · [x] `build_map.py` + `--check`.
- Próximo da sequência: **SPEC-005** (Event Bus) — somente com autorização de Andraus e passo 1-bis do §23.

---

**Andraus**
