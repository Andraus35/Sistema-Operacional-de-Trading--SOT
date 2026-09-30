# Dossiê de Pesquisa — SPEC-002 (companion — convenção de nome do gate determinístico)

**Nota de proveniência:** o Dossiê de Pesquisa **autoral e homologado** desta Spec é `specs/features/SPEC-002/DOSSIE-PESQUISA.md` (homologado junto da abertura — DHR-SPEC002-001, 2026-09-28, junto de `PROPOSTA-ABERTURA.md`). Este arquivo `research.md` existe **apenas** para satisfazer a convenção de nome de arquivo que `scripts/validate_spec_sot.py` (check `[STRUCT-11] Dossiê de Pesquisa presente`) procura na mesma pasta de uma Spec que cita `RULE-ECC-01/02` — o script busca literalmente `research.md`. Não há dois Dossiês distintos: este arquivo é um espelho/companion do conteúdo homologado, não um documento concorrente. Em caso de qualquer divergência textual entre os dois (não deveria haver), `DOSSIE-PESQUISA.md` prevalece, por ser o nome citado explicitamente em `DHR-SPEC002-001`. (Mesmo padrão já usado em `specs/features/SPEC-046/research.md`.)

---

## Dossiê de Pesquisa — resumo executivo (ver `DOSSIE-PESQUISA.md` para o texto completo homologado)

**Escopo:** camada Harness/operacional SOBRE o modelo canônico CEM-001 (baseline) — Evidência + Provenance como 1 Spec unificada (`SPEC-002-SPLIT-001` resolvida em DHR-SPEC002-001).

**Fontes classificadas `[EXTERNO]` (7, via WebSearch real — captura verbatim RULE-ECC-04 PENDENTE, ver `sources/_LIMITACAO-WEBFETCH.txt` e a nota de gate no topo de `plan.md`):**

| ID | Fonte | Tipo (R1) | Recomendação |
|---|---|---|---|
| SRC-01 | W3C PROV / PROV-AGENT | Padrão | adaptar (vocabulário entity/activity/agent → provenance operacional) |
| SRC-02 | Proveniência ML / chain-of-custody / tamper-evidence | Prática | adaptar (versão imutável verificável, INV-07) |
| SRC-03 | Dempster-Shafer (fusão de evidência conflitante) | Padrão | adiar para SPEC-003 (fusão/convicção é Q-007/J-001; Evidence Strength ≠ Convicção) |
| SRC-04 | GRADE (directness/timeliness/completeness/independence/agreement) | Prática | adaptar (qualidade/independência/temporalidade; sem limiar numérico — J-001/RULE-EV-05) |
| SRC-05 | MiFID II (trilha imutável/replay) | Padrão | adaptar só o princípio de auditabilidade; rejeitar escopo de execução (INV-05) |
| SRC-06 | OWA/CWA — "ausência de evidência não é evidência de ausência" | Padrão | adotar o princípio (ausência/inconclusiva como estado de 1ª classe, RULE-EPI-01/CC-09) |
| SRC-07 | OpenLineage (dataset/job/run; metadados de proveniência) | Prática | adaptar modelo de metadados; reforça fronteira com storage físico (SPEC-004/006) |

**Achado decisivo (SRC-06):** o CEM-001 já é open-world-compatível em princípio, mas a camada operacional precisa declarar explicitamente que ausência de evidência NUNCA é convertida silenciosamente em contraevidência — isso vira BASpec/Enforcement Contract dedicado no Plan (EC-EV com efeito E3).

**Achado de maior aderência (SRC-01/SRC-07):** vocabulário entity/activity/agent (PROV) + modelo de metadados dataset/job/run (OpenLineage) mapeiam diretamente aos campos de provenance já existentes no CEM-001 (Producer/Origin/Source Reference/Lineage) — não introduzem conceito novo, apenas orientam a operacionalização.

**Lacunas/conflitos (CONS-01 — não fecham decisão aberta):** fusão de evidência conflitante (SRC-03) pertence à SPEC-003 (J-001 aberta); limiares numéricos de qualidade/independência (SRC-04) também dependem de J-001; storage físico (Blackboard/KG) pertence à SPEC-004/006 (M-001/H-001 abertas); escopo de execução regulatória (SRC-05/MiFID) explicitamente fora do SOT (INV-05).

**Texto completo, questões de pesquisa, estratégia de busca, achados por fonte com comparação explícita adotar/adaptar/rejeitar/adiar, e proposta de re-apontamento de gatilhos do RMR-001:** ver `specs/features/SPEC-002/DOSSIE-PESQUISA.md` (documento homologado, DHR-SPEC002-001).
