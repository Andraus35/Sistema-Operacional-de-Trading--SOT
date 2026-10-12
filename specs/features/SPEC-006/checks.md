# checks.md — Verificação de Spec da SPEC-006 (fase spec-first)

**Objeto:** `specs/features/SPEC-006/plan.md` **v1.1 (candidato)** (Cognitive Knowledge Graph — contrato cognitivo da memória semântica permanente; mecanismo físico de armazenamento INDETERMINADO = H-001 ABERTA)
**Natureza:** verificação estrutural da Spec (BASpec/EARS/Enforcement/Classe bem-formados) — NÃO é teste de runtime, NÃO é o parecer do Revisor, NÃO é homologação. [FONTE: atomic-spec §14; ROADMAP §6]
**Método:** atomic-spec.md **v1.5**
**Data:** 2026-10-12 (Rodada 2)

> **Nota de honestidade (RULE-MET-01):** vários itens permanecem **em aberto** e estão marcados [DECISÃO NECESSÁRIA] no plan.md — NÃO são marcados ✔ aqui. São: mecanismo físico (H-001), contrato do selo de publicação (SPEC-007), allowlist de escritores autorizados, host do juízo de CKG-008, migração de ontologia, emissão de evento pelo KG, escala numérica de confiança de relação. A verificação abaixo confere **well-formedness estrutural**, não a resolução dessas decisões.

---

## 1. Cobertura de profundidade (D0–D7 + D8 adversarial focado — alvo ROADMAP §6; CRITICAL)

| Nível | Exigido | Presente | Evidência |
|---|---|---|---|
| D0 Intenção | Sim | ✔ | Missão (preservar/relacionar/consultar; memória permanente ≠ trabalho; mecanismo físico INDETERMINADO; fronteiras) |
| D1 Escopo/Non-goals | Sim | ✔ | S1–S13 + Non-goals (H-001/SPEC-004/005/007/009/018; emissão pelo KG; ontologia-componente) |
| D2 Regra | Sim | ✔ | RULE-CKG-001..013 [PROPOSTA]; **matriz de integridade §D2.1**; INV-CKG-01 |
| D3 Comportamento (BASpec) | Sim | ✔ | CKG-001..013, cada uma com CLASSE/MECANISMO (CC-11) |
| D4 Algoritmo | Quando há regra determinística real | ✔ | Integridade, validade bitemporal (novo registro), imutabilidade/estado derivado, trace completo, dedupe, gate causal, isolamento confiança |
| D5 Estado | Sim | ✔ | `knowledge_state` como **projeção derivada** (ACTIVE/SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED); transitórios CANDIDATE_WRITE/REJECTED não persistidos |
| D6 Protocolo | Sim | ✔ | Sequência de escrita (10 passos; duas fontes/uma governança); consumo de evento; emissão = [DECISÃO NECESSÁRIA] |
| D7 Teste | Sim (CRITICAL; ≥3) | ✔ | **T01..T13 (13)** — um por BASpec (inclui caso-feliz T12 e supersessão-por-novo-registro T13; T10 ampliado a 3 saltos) |
| D8 Adversarial | Sim (CRITICAL, focado) | ✔ | **ADV-CKG-01..15 (15)** — cobre as 13 BASpecs + fronteiras/decisões abertas |
| D9 Auditoria | Por referência | Parcial (por referência) | registro reconstruível (version/supersedes/proveniência/validade/colisão); trace **completo** (CKG-011); observabilidade agregada = SPEC-040 |

**Resultado:** profundidade-alvo D0–D7 atingida; D8 focado nos pontos sensíveis. D9 por referência (coerente com alvo e H-001 ABERTA).

---

## 2. Well-formedness das BASpecs + Classe/Mecanismo (CC-11)

| BASpec | QUANDO | ENTÃO | PORQUE | REF | VERIF. POR | CLASSE | Bounded loop / Gate saída |
|---|---|---|---|---|---|---|---|
| CKG-001 ontologia + matriz | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-002 ref canônica (obs≠evid) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-003 relação tipada/direção/proveniência | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-004 temporalidade (novo registro) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-005 proveniência obrigatória | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-006 imutabilidade/append-only (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-007 confiança ≠ Convicção | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-008 causal (mecanismo+regime+posthoc) | ✔ | ✔ | ✔ | ✔ | ✔ | H | bounded loop ✔ + gate de saída ✔ |
| CKG-009 governança de escrita (E3) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-010 fronteira (canônico + selo SPEC-007) | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |
| CKG-011 consulta/trace completo (read-only) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-012 lifecycle (estado derivado) | ✔ | ✔ | ✔ | ✔ | ✔ | D | N/A |
| CKG-013 colisão de relações | ✔ | ✔ | ✔ | ✔ | ✔ | C | gate de saída ✔ |

Cada BASpec com efeito declara Classe + critério 4Es (RULE-MECH-02); Classes C declaram gate de saída; Classe H (CKG-008) declara **bounded loop + gate de saída** determinístico (verifica presença dos campos CAU-01/02/03, não veracidade — ENF-03). **PASS.**

---

## 3. Critérios EARS

13 critérios "Quando <condição>, o KG DEVE/NÃO DEVE <resposta>" (ontologia/integridade, ref canônica+obs≠evid, relação tipada, temporalidade por novo registro, proveniência, imutabilidade, confiança≠convicção, causal+regime, governança E3, fronteira+selo, consulta/trace completo, lifecycle, colisão). Sem multi-outcome não-decomposto. **PASS.**

---

## 4. Enforcement Contracts (ENF-01..08)

| Check | Resultado |
|---|---|
| ENF-01 Contract em todo comportamento com efeito | ✔ EC-CKG-001..006 cobrem as 13 BASpecs: write (001: RULE-CKG-001/002/003/005/008/010/013); imutabilidade/versionamento (002: RULE-CKG-004/006/012); governança (003: RULE-CKG-009); isolamento (004: RULE-CKG-007); causal (005: RULE-CKG-008); consulta (006: RULE-CKG-011). **Toda RULE-CKG tem EC.** |
| ENF-02 Nível ≥ piso; economicidade não rebaixa | ✔ **escrita permanente = E3** (atomic-spec §10.2 "KG publicado → E3 mínimo"); E2 (guard de isolamento); E1 (consulta). "piso E2" da v1.0 **eliminado** (achado C1). |
| ENF-03 Gate determinístico; Detector ≠ Gate | ✔ EC-CKG-003/005; juízo de CKG-008 é detector, gate de saída determinístico |
| ENF-04 Fail-closed em efeito crítico irreversível | ✔ EC-CKG-001/002/003/005 (E3 fail-closed) |
| ENF-05 Policies não auto-aprendidas | ✔ RULE-CKG/contrato [PROPOSTA]; só Andraus homologa |
| ENF-06 E0 declarado como orientação | N/A (não há E0) |
| ENF-07 E3 declara método de falso-DENY | ✔ EC-CKG-001/002/003/005 (amostral; **CONDICIONAL até o limiar** — gap aberto, atomic-spec §12) |
| ENF-08 Escala E0–E3 referenciada | ✔ via atomic-spec §10.2 |

**PASS.**

---

## 5. Constitution Check (CC-01..CC-12 — atomic-spec v1.5)

Preenchido no plan.md. **Críticos aplicáveis:** CC-02 (CHM/CEM/CCM/SPEC-004/005 não redefinidos), CC-08 (Herança/Delta + cobertura×lacuna; **append-only como novos registros alinhado à SPEC-004 INV-CBP-01**; `gate_record` reatribuído à SPEC-004), CC-09 (H-001 ABERTA; mecanismo físico INDETERMINADO; causal c/ mecanismo+regime+posthoc; trace completo não rebaixado por H-001), CC-10 (acepções; observation≠evidence), CC-11 (Classe por BASpec, incl. H) = PASS. CC-01 (agnóstico de escola; INV-02 na matriz — ICT não origina). CC-03 (não computa convicção; J-001/N-001 abertas). CC-04 (INV-04 preservado). CC-05 (CRITICAL/D0–D7+D8). CC-06/CC-07 = N/A justificado. **CC-12 = N/A**. **PASS.**

---

## 6. Herança/Delta (§8.3 — CC-08)

- Bloco §8.3 presente; INHERITS/ADDED com ID+versão/linha (RULE-HD-04): CEM-001 (l.494/608-615/562-565/699), CHM-001, CCM-001, CEE-001 l.111, SAS-001 §6.12, **SPEC-004 v1.2 (INV-CBP-01 append-only; `gate_record`)**, SPEC-005 v1.0, RULE-BB-004, **RULE-CAU-01/02/03**, CONSTITUTION l.233, atomic-spec v1.5 (§10.2 E3), INV-04/05/06/07/09/10, ENF-01..08. ✔
- **Mapa de cobertura × lacuna** (arquivo:linha): preservação de linhagem/versões/**todos os estados**, trace completo, proveniência, append-only-por-novos-registros = herdados/reforçados, não duplicados; lacuna = ontologia+matriz, catálogo (+DERIVA_DE, observation), temporalidade bitemporal, confiança de relação, consulta, governança. ✔
- REMOVED vazio. ✔
- MODIFIED = só RULE-BB-004 **reforçada** (RULE-HD-02 respeitada; SPEC-004/005 não tocadas — INV-09). ✔
- **`gate_record` reatribuído à SPEC-004** (não CEM-001) em toda a Spec (achado Extra). ✔
- Eixo VERTICAL (RULE-HV) avaliado e **não aplicável**. ✔

**PASS.**

---

## 7. Consistência interna (CONS-01) e etiquetagem (TRACE-06)

| Check | Resultado |
|---|---|
| H-001 NÃO decidida — contrato cognitivo independe do mecanismo físico (ADV-CKG-09) | ✔ |
| Opção B (banco de grafos) = ADIADA (registrada, não apagada; INV-07) | ✔ |
| Escala de confiança de relação = PARÂMETRO a calibrar (INDETERMINADO) | ✔ |
| Confiança de relação ≠ Convicção; nunca retroalimenta o Conviction Vector (INV-04; CKG-007/EC-CKG-004) | ✔ |
| Contrato do **selo de publicação** = dependência da SPEC-007 (ainda não especificada) — [DECISÃO NECESSÁRIA], **não** ✔ fechado | aberto (declarado) |
| **Allowlist de escritores / host do juízo CKG-008 / migração de ontologia** = [DECISÃO NECESSÁRIA] (runtime/governança) — **não** ✔ fechado | aberto (declarado) |
| **Emissão de evento pelo KG** — removida como afirmação; [DECISÃO NECESSÁRIA] dependente da SPEC-005 (achado C21) | aberto (declarado) |
| M-001 / J-001 / N-001 / G-001 / K-001 / C-001 / WF-D03 / ECC-03-001 NÃO tocadas — permanecem ABERTAS | ✔ |
| SPEC-004/005 NÃO reabertas/duplicadas (CC-02/INV-09) | ✔ |
| SPEC-007 (formação) NÃO absorvida (CKG-010; ADV-CKG-08) | ✔ |
| Append-only = **novos registros** (estado = projeção derivada) alinhado à SPEC-004 INV-CBP-01 (achado C6) | ✔ |
| RULE-CKG/contrato/matriz etiquetadas [PROPOSTA]; canônicos/RULE-CAU/INV-* = FATO NORMATIVO | ✔ |
| Fontes SRC-*/REPO-* [EXTERNO]; **SRC-FORGET-01 = DADO não-verbatim**, não sustenta alegação carregada (achado B2) | ✔ |
| Nenhuma decisão aberta usada como invariante fechado; nenhuma forma `fechad*/resolvid*/homologad*` colada a ID de decisão aberta (achado A) | ✔ |

**PASS (com itens explicitamente em aberto, não marcados ✔).** Nenhum limiar de convicção nem escala numérica de confiança declarado — STRUCT-07 não incide.

---

## 8. Verificação de RULEs/IDs citados (existência real)

| Citado | Existe? | Fonte |
|---|---|---|
| CEM-001 (l.494/562-565/608-615/612-614/699) | ✔ | canon/CEM-001 (BASELINE) |
| CHM-001; CCM-001 | ✔ | canon/ (BASELINE) |
| CEE-001 l.111 | ✔ | canon/CEE-001 l.111 |
| SAS-001 §6.12 (l.923-924); l.163 (EC-COG-003) | ✔ | canon/SAS-001 |
| SPEC-004 v1.2 (INV-CBP-01 append-only; `gate_record`/identidade — RULE-CBP-014); SPEC-005 v1.0 | ✔ | specs/features/ (BASELINE) |
| CONSTITUTION l.233 (EC-COG-003) | ✔ | governance/CONSTITUTION.md l.233 |
| RULE-BB-004 (l.323); **RULE-CAU-01 (l.680), RULE-CAU-02 (l.681), RULE-CAU-03 (l.682)** | ✔ | governance/RULES.md |
| atomic-spec §10.2 ("KG publicado → E3 mínimo"); §3 CRITICAL·D0–D7; §10.6 Classe | ✔ | atomic-spec.md |
| INV-04/05/06/07/09/10; ENF-01..08 | ✔ | atomic-spec §13/§10.4 |
| RULE-MECH-01..04; RULE-PD-01; RULE-ECC-01/02/04/06; RULE-HD-02/03/04; RULE-HV | ✔ | RULES.md |
| RULE-EPI/ONT/INQ/CAU/CTF/UNC/PRB/DEC/SEM/MET | ✔ | RULES.md v1.5 |
| H-001; M-001; J-001; N-001; G-001; K-001; C-001; WF-D03; ECC-03-001 | ✔ (abertas) | ROADMAP §7 / atomic-spec §12 |
| SPEC-001/019/020/021 v1.0; SPEC-007/009/018/040 (slots) | ✔ | specs/features/ · ROADMAP |
| REPO-graphiti/graphrag/cognee/mem0 (elegíveis) | ✔ (verbatim) | specs/features/SPEC-006/sources/ (RULE-ECC-04/06) |
| RULE-CKG-001..013; INV-CKG-01; matriz §D2.1; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | esta Spec — não citadas como existentes |

Nenhuma referência a RULE inexistente apresentada como vigente. **PASS.**

---

## 9. Gate RMR-001 (passo 11-bis)

- **Nenhum item com gatilho `spec:SPEC-006` homologado isoladamente** — a redação satisfaz ramos de gatilho de BL-003 (`spec:SPEC-006`), BL-011 (`spec:SPEC-006`) e possivelmente BL-010 (`milestone:FASE 3`). ✔
- **BL-003** (persistência física) — parte física = H-001 (ABERTA)/G-001 (ABERTA) → referenciado, não absorvido. ✔
- **BL-011** (MC-EXP-001) — insumo de requisitos (COL-EXP-01..05); não promovido. ✔
- **BL-010** (MC-RAG-001) — fonte da SPEC-007; tangente; não promovido. ✔
- **BL-029** — **`Em espera`** (Andraus, DHR-SPEC006-PEND-001; RMR-001 l.128/l.191; `ATIVADO` riscado), gatilho `spec:SPEC-014`/`SPEC-018`/`SPEC-045` (SPEC-004 consumido). **Independente** desta Spec; não promovido. **[CORRIGIDO na v1.1 — achado C8]** (a v1.0 dizia `ATIVADO`). ✔
- Promoção/encaminhamento é do gate e de Andraus; passo 11-bis pleno na homologação. **PASS.**

---

## 10. RULE-ECC-04 (Captura Verbatim) e RULE-ECC-06 (Repositórios) — verificação de presença

| Fonte carregada | Arquivo companheiro | Citação verbatim no Dossiê |
|---|---|---|
| SRC-ZEP-01 (KG temporal) | ✔ sources/ | ✔ research.md §3.1 |
| SRC-PROV-01 (W3C PROV) | ✔ sources/ | ✔ research.md §3.2 |
| SRC-MEMVSKG-01 (KG × RAG) | ✔ sources/ | ✔ research.md §3.4/§3.5 |
| SRC-FORGET-01 | N/A (sumário WebSearch — **DADO não-verbatim**) | research.md §3.5/§3.6 (não sustenta alegação carregada — §7-bis Bloco C) |
| REPO-graphiti / graphrag / cognee / mem0 | ✔ sources/REPO-*.txt | ✔ research.md §5 (régua Equilibrada) |

- **RULE-ECC-06:** seção "Pesquisa em repositórios" (research.md §5); **4 ELEGÍVEIS**; nenhum adotado; capturas presentes; conteúdo = DADO. SPEC-006 não é grandfathered → STRUCT-12 incide. `python scripts/check_repo_research.py specs/features/SPEC-006` esperado OK (sem web — ENF-03). ✔
- **RULE-ECC-05:** **NÃO incide** (infra de memória; DHR-SPEC006-001 §2); conformidade WORKFLOW por prudência; não fecha WF-D03. ✔
- **Nota de honestidade:** metadados de repositório vêm de WebFetch da API pública (research.md §5/§8) — não reproduzíveis pelo Revisor sem rede (ENF-03). Risco residual em `sources/_LIMITACAO-WEB.txt`.

> Correspondência verbatim e régua = mandato do Revisor/gate (sem web). Aqui só **presença**. **PASS (presença).**

---

## 11. Achados desta verificação (Rodada 2) — rastreabilidade dos itens tratados

| ID | Item da Rodada 2 | Situação |
|---|---|---|
| CK-A | STRUCT-10: formas `fechad*/resolvid*/homologad*` coladas a ID de decisão aberta | **Resolvido** — reescrito; as 2 adjacências residuais têm pendência (`[DECISÃO NECESSÁRIA]`/`bloqueador`) em ≤200 chars (short-circuit `marcada`) |
| CK-B1 | §7-bis Bloco C cobria só EPI/CAU/PRB | **Resolvido** — Bloco C trata EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET ("verificado/sem achado") |
| CK-B2 | SRC-FORGET-01 (DADO não-verbatim) | **Resolvido** — declarado que não sustenta sozinha alegação carregada; "esquecimento=arquivamento" apoia-se em INV-07/RULE-BB-004 |
| CK-B3 | EC-CKG-002 EVIDENCE | **Resolvido** — registra tentativas de DELETE/UPDATE bloqueadas (observabilidade do gate) |
| CK-B4 | CKG-009/EC-CKG-003: falha de auth da SPEC-004 | **Resolvido** — falha de auth ⇒ não-autorizado (fail-closed); T08 cobre |
| CK-C1 | ENF-02: escrita no KG deve ser E3 | **Resolvido** — EC-CKG-001/002/003/005 em E3; "piso E2" eliminado; checks §4 ajustado |
| CK-C2 | "publicado" × preservar estados canônicos | **Resolvido** — CKG-010 admite canônicos por ciclo de vida preservando REFUTED/SUPERSEDED/ARCHIVED (CEM-001 l.494) |
| CK-C3 | Trace multi-salto não pode rebaixar obrigação canônica | **Resolvido** — trace COMPLETO é obrigação; só eficiência de consulta ampla = INDETERMINADO; T10 ampliado a 3 saltos |
| CK-C4 | Tipo de relação Lineage ausente | **Resolvido** — tipo **DERIVA_DE** (aresta de Lineage) + domínio/contradomínio + ordem de saída; separado de `provenance_ref.lineage_ref` |
| CK-C5 | Ontologia sem regras de integridade | **Resolvido** — matriz §D2.1 (tipo×origem/destino×direcionalidade/simetria); "família estrutural" definida; SIMILAR_A simétrica na consulta; T01/ADV-12 de violação |
| CK-C6 | Mutação do histórico × append-only | **Resolvido** — invalidação/supersessão como **novos registros**; estado = projeção derivada (espelha SPEC-004 INV-CBP-01); ADV-13 |
| CK-C7 | Schema sem supersedes/version/selo/escritor/colisão | **Resolvido** — campos adicionados; REJECTED/CANDIDATE_WRITE = transitórios (não persistidos) |
| CK-C8 | BL-029 `ATIVADO` × registro oficial | **Resolvido** — corrigido para `Em espera` (plan §gate; checks §9) |
| CK-C13 | Critérios de estados terminais | **Resolvido** — SUPERSEDED×INVALIDATED_IN_TIME×ARCHIVED distinguidos; correção/reativação; `relevance`; autoridade = gate E3 (CKG-009) |
| CK-C14 | "bitemporal" sem sustentação | **Resolvido** — `recorded_at` acrescentado à relação (valid-time + transaction-time) |
| CK-C17 | RULE-CAU-02/03 ausentes; atribuição pós-hoc | **Resolvido** — CKG-008 exige regime (CAU-02) e marcador pós-hoc (CAU-03); gate verifica presença; ADV-CKG-04 corrigido |
| CK-C18 | node_type sem observation | **Resolvido** — `observation` no catálogo; INV-06 (observation≠evidence); CKG-002/T02 |
| CK-C21 | KG "pode emitir eventos" × SPEC-005 | **Resolvido** — emissão removida como afirmação; o KG só consome; emissão = [DECISÃO NECESSÁRIA] |
| CK-C22 | Governança/versionamento da ontologia | **Resolvido (com [DECISÃO NECESSÁRIA])** — spec-time SPEC-019; runtime K-001 [DECISÃO NECESSÁRIA]; backward-compatible; migração de schema [DECISÃO NECESSÁRIA] |
| CK-C9 | Trilha de escrita incoerente | **Resolvido** — uma governança (CKG-009), duas fontes (canônico/ciclo de vida + formado/selo SPEC-007 [DECISÃO NECESSÁRIA]); allowlist e host do juízo = [DECISÃO NECESSÁRIA] |
| CK-C10 | Cobertura D7/D8 falsa | **Resolvido** — 13 T (um por BASpec) + 15 ADV (todas as BASpecs cobertas); Bloco A e §1/§2 corrigidos |
| CK-C11 | ECs não cobriam CKG-002/004/012/013 | **Resolvido** — POLICY de EC-CKG-001 cita RULE-CKG-002/013; EC-CKG-002 cita RULE-CKG-004/012; toda RULE-CKG tem EC |
| CK-Extra | `gate_record` atribuído ao CEM-001 | **Resolvido** — reatribuído à SPEC-004 em toda a Spec |

---

## Resultado da verificação de spec

**Estruturalmente CONFORME** (well-formedness). BASpecs (CKG-001..013) com Classe/Mecanismo (CC-11; D+C+H com bounded loop/gate em CKG-008), EARS (13), Enforcement (EC-CKG-001..006; **escrita = E3 fail-closed**; ENF-07 falso-DENY CONDICIONAL até limiar; toda RULE-CKG com EC), Constitution Check CC-01..CC-12 (CC-02/CC-08/CC-09/CC-10/CC-11 incidem; CC-12 N/A), Herança/Delta (CC-08 + cobertura×lacuna; `gate_record` reatribuído à SPEC-004), matriz de integridade §D2.1, append-only por novos registros (INV-CBP-01), trace completo, CONS-01 (H-001/selo SPEC-007/allowlist/emissão/M/J/N/G/K/C-001/WF-D03/ECC-03-001 abertas), gate RMR-001 (BL-029 = `Em espera`), RULE-ECC-04/06 satisfeitos. Rastreabilidade dos 24 achados da Rodada 2 em §11.

> Feedback interno de verificação de spec — **NÃO** é o parecer do Revisor nem homologação. Próximo passo: gate determinístico `validate_spec_sot.py` + `check_repo_research.py` + `build_map.py --check` + `check_doc_sync.py` (ambiente pai — Especificador sem Bash) + submissão ao Revisor SOT.
