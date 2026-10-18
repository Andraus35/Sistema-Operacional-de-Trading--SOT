# DHR-SPEC006-002 — Ata de Homologação — SPEC-006 (Cognitive Knowledge Graph) v1.7 — BASELINE

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Parecer do Revisor sobre o Plan v1.7: **CONFORME COM RESSALVAS** (2026-10-13; 0 Crítico, 0 Maior, 3 Menores m-1..m-3, aplicados em seguida) — `specs/features/SPEC-006/plan.md` + `checks.md`. Pareceres anteriores: NÃO CONFORME v1.3 (9 Maiores), NÃO CONFORME v1.4 (6 Maiores), NÃO CONFORME v1.5 (1 Maior), CONFORME COM RESSALVAS v1.6. Abertura: DHR-SPEC006-001 |
| Data | 2026-10-13 |
| Status | **HOMOLOGADA — BASELINE v1.7** (decisão direta de Andraus em chat, 2026-10-13: "Você homologa agora no chat"; assinatura = decisão registrada no chat e citada nesta ata). |
| Compatibilidade | Minor (não redefine CHM-001/CEM-001/CCM-001/SPEC-004/SPEC-005; não fecha H-001 nem outra decisão aberta) |
| Gates | `validate_spec_sot.py` 13/13 PASS (inclui `[STRUCT-13]`) · `revisor_gate` PASSOU_D · `check_invariants` 0 · `check_doc_sync` ERRO=0 · `check_repo_research` OK · `check_rpsa` OK · `build_map.py --check` em dia · `check_refs`: 1 ERRO pré-existente (CATALOGO l.198 `DHR-010`, fora desta Spec) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de Spec: não altera texto de agente; as mudanças de agente ligadas à SPEC-006 (backlog na abertura) estão na DHR-BACKLOG-ABERTURA-001. |

---

## 1. Decisão de Andraus (chat, 2026-10-13)
Homologar a SPEC-006 v1.7 como **BASELINE**. Ressalva do Revisor sobre a ferramenta `revisor_gate` (não exposta à sessão do Revisor) registrada: o gate determinístico foi rodado pelo ambiente pai e passou.

## 2. O que a SPEC-006 v1.7 estabelece
- **CRITICAL · D0–D7 + D8 adversarial focado**; Classe D/C/H por BASpec (CC-11); **13 BASpecs (CKG-001..013)**; **6 Enforcement Contracts** (escrita permanente e guard confiança×convicção em **E3 fail-closed**); 13 EARS; D7 **T01..T17**; D8 **ADV-CKG-01..22**; INV-CKG-01/02.
- Contrato cognitivo da **memória semântica permanente**: ontologia enxuta + matriz de integridade (§D2.1) e colisão (§D2.2), temporalidade bitemporal, proveniência condicional, versionamento sem fork, confiança de relação ≠ Convicção (nenhuma aresta para `conviction`), causalidade com mecanismo/regime/pós-hoc determinístico, governança de escrita (produtor propõe; runtime/serviço do KG grava), trace completo para evidência.
- **RULE-CKG-001..013 + INV-CKG-01/02 → vigência imediata** por homologação; registro físico em `RULES.md` **diferido** (precedente SPEC-002/003/004/005; RULE-HG-02).
- **Mecanismo físico de armazenamento: INDETERMINADO — H-001 permanece ABERTA.**
- `school`/`hierarchy_role` só para `hypothesis` (decisão de Andraus, chat 2026-10-12); `structure` fora das origens de ORIGINA; pendência registrada como **CKG-STRUCT-ORIGIN-001 / BL-035 (`Em espera`)**.
- Backlog da abertura (DHR-BACKLOG-ABERTURA-001): BL-003 e BL-011 vinculados, ambos `Disposição: PARCIAL`; reconciliação de BL-011/MC-EXP-001 feita na v1.7 (sem regra nova). Estados no painel inalterados.

## 3. Ressalvas e pendências (não bloqueantes)
| ID | Tratamento |
|---|---|
| Volume (1528 linhas) | Dividir a Spec = decisão de Andraus (Q-ABERTURA-5); **não dividida** |
| Critério de decaimento/retenção (EXP-SPEC-023/024/025/028) | → K-001 / SPEC-018 (aberta) |
| Produtor/gatilho de promoção trabalho→permanente | [DECISÃO NECESSÁRIA] (SPEC-018/K-001) — fronteira CKG-010 |
| Allowlist de escritores; host do juízo CKG-008; migração de ontologia; timeout do buffer PENDING_ANCESTOR; escala de confiança | [DECISÃO NECESSÁRIA] / parâmetros a calibrar — nada fechado |
| Consumo/emissão de evento pelo KG | [INFERÊNCIA]/[DECISÃO NECESSÁRIA] dependente da SPEC-005 |
| `school=Fractal` sem produtor de hipótese na SPEC-001 | dobrado em CKG-STRUCT-ORIGIN-001 (BL-035) |

## 4. Permanecem ABERTAS (CONS-01)
**H-001 · M-001 · J-001 · N-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (em BL-035).** Nenhuma decisão aberta foi fechada por este ato.

## 5. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` (estado do slot, próximo trabalho) · [x] `AGENTS.md` §7 · [x] `governance/CATALOGO-OFICIAL.md` · [x] `backlog/RMR-001_Painel_Backlog.md` (11-bis) · [x] `plan.md` (versão/status) · [x] RPSA (ata classificada: sem escopo de agente) · [x] `build_map.py` + `--check`.
- Próximo da sequência: **SPEC-007** (RAG / WikiRAG / Knowledge Formation Harness) — **somente com autorização de Andraus** e passo 1-bis do §23; o BL-035 e o BL-010 têm gatilho em `spec:SPEC-007 em redação` (vinculação automática na abertura — DHR-BACKLOG-ABERTURA-001).

---

**Andraus**
