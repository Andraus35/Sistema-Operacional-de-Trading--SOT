# DHR-SPEC002-002 — Ata de Homologação — Plan da SPEC-002 (Evidence & Evidence Provenance Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | SPEC-002 — Parecer do Revisor sobre o **Plan** (`specs/features/SPEC-002/plan.md` + `checks.md`): **CONFORME**, com 1 achado Médio não-bloqueante **ACH-001 (EPH-GMC-001)** |
| Data | 2026-09-29 |
| Status | **PLAN HOMOLOGADO — SPEC-002 v1.1 BASELINE.** Sucede a `DHR-SPEC002-001` (abertura homologada). Este é o gate do Plan (ROADMAP §23, passo 5 em diante). |
| Compatibilidade | Minor (constrói sobre CEM-001 — não redefine, CONST-01; extensão do CEM-001 é Categoria B aditiva/compatível; não fecha decisão aberta de mérito — CONS-01) |
| Convenção | Mesma da `DHR-SPEC046-002` (ata de homologação do Plan separada da ata de abertura). A abertura foi homologada em `DHR-SPEC002-001`. |

---

## 1. Decisão

O **Plan da SPEC-002 — "Evidence & Evidence Provenance Harness" (v1.1) está HOMOLOGADO como BASELINE.**

**Fluxo de autoridade cumprido:**
```
Abertura homologada (DHR-SPEC002-001, 2026-09-29: Dossiê + DN-1/DN-2/DN-3)
   → Especificador escreve o Plan (plan.md v1.0 + checks.md; skill tlc-spec-lean)
   → Revisor audita o Plan (protocolo semântico GRE-001/HRE-001 + Passo 5-bis, obrigatório CRITICAL)
     → parecer CONFORME, com 1 achado Médio não-bloqueante ACH-001 (EPH-GMC-001)
   → Andraus decide o ACH-001 (chat, 2026-09-29): reclassificar a extensão DN-1
     de Categoria A para CATEGORIA B, conduzindo o processo formal do GMC-001 Cap.5
     (proposta + análise de impacto + registro do Controlador), sem exceção/override
   → Especificador aplica a correção (Plan → v1.1; proposta GMC-CEM001-EXT-001 criada)
   → Plan HOMOLOGADO como BASELINE (este ato)
```

---

## 2. Objeto homologado

- **Artefato:** `specs/features/SPEC-002/plan.md` (v1.1) + `specs/features/SPEC-002/checks.md`.
- **Complexidade / profundidade:** **CRITICAL / D0–D8** (DN-2, DHR-SPEC002-001). Maturidade-alvo **L3** (teto spec-first para CRITICAL — RULE-MM-04).
- **Conteúdo:** camada Harness/operacional de proveniência/qualidade/ciclo-de-vida de evidência **sobre CEM-001** (não redefine — CONST-01, INV-10). **12 BASpecs** (EPH-001..012) com Classe declarada (RULE-MECH-01: predominância D, com H em publicação e C em travas constitutivas), profundidade D0–D8 completa, §7-bis (redução de viés) completo (Blocos A–D), Enforcement Contracts EC-EPH-001..004, 10 critérios EARS, máquina de estados operacional sobre CEM-001 Cap.4, Herança/Delta (§8.3, CC-08).
- **Regras propostas:** RULE-EPH-01..10 (passam a FATO NORMATIVO com esta homologação; registro físico em `governance/RULES.md` — seção "Regras de Evidence Harness (RULE-EPH)" — é ato do Controlador).

---

## 3. Resolução do ACH-001 (EPH-GMC-001) — reclassificação Categoria A → Categoria B

**Achado do Revisor (ACH-001, Médio, não-bloqueante):** o Plan (herdando a nomenclatura da abertura/DN-1) modelou a extensão de confiabilidade histórica do produtor como **Categoria A** (aditiva simples via GMC-001). O Revisor conferiu o **GMC-001 Cap.3** e confirmou, pela **classificação literal**:
- **Categoria A** = apenas **novos valores dentro de uma enumeração já existente** (ou novos estados previamente previstos);
- **Categoria B** = **novo campo** (mesmo opcional) / novo relacionamento opcional.

Como **não há hoje nenhuma enumeração compatível pronta no CEM-001** para receber a confiabilidade como mero novo valor, a extensão exige um **campo novo** → **Categoria B**.

**Decisão de Andraus (2026-09-29):** **reclassificar como Categoria B** e **seguir o processo formal que o próprio GMC-001 já prevê** (Cap.5: proposta formal + análise de impacto + registro do Controlador), **em vez de declarar uma exceção/override**.

**Execução:** processo de Categoria B conduzido pelo Especificador (papel Estrategista do GMC-001) na proposta formal `governance/GMC-CEM001-EXT-001_Proposta_Extensao_Confiabilidade_Produtor_CEM-001.md`, contendo:
- objetivo, justificativa arquitetural, impacto esperado, especificação do campo (`Producer Historical Reliability`, opcional, Camada 2/Origem, domínio = Governed Enumeration ordinal);
- **classificação Categoria B** justificada contra a régua literal do Cap.3 (e verificação de que **não** reclassifica para Categoria C — campo opcional, sem alterar produtores/consumidores/comportamento);
- **análise de impacto obrigatória** (5 perguntas do Cap.3): nenhum componente obrigatoriamente afetado; só o CEM-001 evolui (v1.0 → v1.1); **sem quebra de compatibilidade**; alternativas menos invasivas avaliadas; complexidade neutra-a-simplificadora;
- **compatibilidade retroativa** demonstrada (produtores/consumidores/repositórios/modelos dependentes — todos sem impacto obrigatório);
- **trava INV-04** como constraint explícita da extensão (o campo NUNCA entra no Conviction Vector).

**Versionamento:** CEM-001 **v1.0 → v1.1** (incremento **MINOR** — GMC-001 Cap.3, MINOR para Categoria A e B). O **registro** da evolução no Catálogo Oficial e a **incorporação física** do campo opcional em `canon/CEM-001-...md` são atos do **Controlador** (Etapa 4 do fluxo GMC-001 Cap.5).

**Efeito no Plan:** todas as referências a "Categoria A" da extensão DN-1 corrigidas para **Categoria B** (frontmatter, histórico de versões, CC-02, Herança/Delta ADDED/MODIFIED, D0, S3, RULE-EPH-03, BASpec-EPH-003, ADV-EPH-07, I/O Schemas, Bloco B §7-bis, Etiquetagem). Item **EPH-GMC-001** deixou de ser `[DECISÃO NECESSÁRIA]` e passou a **RESOLVIDO**, referenciando a proposta formal (aditivo — registro histórico da discussão A vs B preservado, INV-07). `checks.md` (CK-01 e §5/§8) ajustado.

> **Substância inalterada (confirmada):** a confiabilidade histórica do produtor permanece **metadado descritivo/filtro** e **NUNCA** é dimensão, insumo ou peso do **Conviction Vector** (INV-04). Apenas o **PROCESSO** de extensão do CEM-001 mudou de A para B; o mérito de DN-1 (aditivo, não redefine, nunca no Conviction) é o mesmo homologado na abertura.

---

## 4. Invariantes e salvaguardas preservados

- **CONST-01:** CEM-001 **não redefinido** — a extensão Categoria B é aditiva/compatível (novo campo opcional), conduzida pelo processo formal do GMC-001; não altera campos/estados/transições existentes.
- **INV-04:** custo/qualidade-de-fonte **nunca** no Conviction Vector — reforçado por BASpec-EPH-004 (efeito E3, fail-closed) e como constraint explícita da GMC-CEM001-EXT-001.
- **INV-06:** Evidência (Agente, interpretada) ≠ Observação (Skill) — preservado (EPH-002).
- **INV-07:** versionamento monotônico; registro histórico da discussão A vs B e do Plan v1.0 preservados (nada deletado).
- **INV-10:** CEM-001 = idioma canônico — preservado.
- **Hierarquia analítica (CC-01):** intocada — SPEC-002 é infraestrutural/neutra de domínio.
- **4Es:** ordem respeitada; Economicidade não rebaixa os pisos E2/E3.

---

## 5. Decisões abertas — nenhuma fechada por este ato (CONS-01)

Permanecem **ABERTAS** (apenas referenciadas, não tocadas): **J-001** (fórmula/pesos/limiares definitivos do Conviction Vector), **M-001** (estados do Blackboard p/ objetos não-hipótese — SPEC-004), **H-001** (Knowledge Graph — SPEC-006), **N-001** (pesos por ativo), **K-001** (ciclo P12 — SPEC-018), **G-001** (schema de estado persistente por agente — SPEC-009), **C-001** (granularidade EARS multi-condição), **RISK-CONV-001** ("convicção de risco" vs Conviction Vector 8D), **ECC-VAL-001** (validade/prazo do Dossiê de Pesquisa), **ECC-03-001**, **RISK-ARR-LOC-001** e demais RISK-*.

A extensão DN-1 (confiabilidade) **não** toca J-001 nem INV-04 — é metadado descritivo. A proposta GMC-CEM001-EXT-001 **não** fixa fórmula, peso ou aging (isso é J-001/CCM-001/SPEC-003).

---

## 6. Registro do Controlador (efeitos a aplicar)

- [x] `governance/DHR-SPEC002-002_...md` — este documento.
- [x] `specs/features/SPEC-002/plan.md` — v1.1 (Categoria A → B; EPH-GMC-001 RESOLVIDO; Status → HOMOLOGADA BASELINE).
- [x] `specs/features/SPEC-002/checks.md` — CK-01/§5/§8 ajustados; resultado atualizado.
- [x] `governance/GMC-CEM001-EXT-001_...md` — proposta formal de Categoria B (Estado APPROVED; registro do Controlador no Catálogo).
- [x] `ROADMAP.md` — SPEC-002: "ABERTA — Dossiê homologado, Plan em elaboração" → **HOMOLOGADA — BASELINE**; "Próximo trabalho autorizado" → SPEC-003 (slot indicativo — NÃO abrir sem Dossiê/abertura, RULE-ECC-01/02).
- [x] `governance/CATALOGO-OFICIAL.md` — SPEC-002 HOMOLOGADA (Trilha B); esta ata registrada (§7.3); CEM-001 evolução Categoria B (v1.1) via GMC-CEM001-EXT-001 registrada (§1) — incorporação física do campo opcional em `canon/CEM-001` = ato editorial do Controlador (pendente).
- [x] `backlog/RMR-001_Painel_Backlog.md` — gatilho `spec:SPEC-002 homologada (consolidação cognitiva v1.5)` do **BL-012 (MC-COG-001)** disparado → registrado no passo 11-bis (permanece `Em espera`: promoção `→ ATIVADO`/tratamento é decisão de Andraus/gate futuro; ver §7 abaixo).
- [ ] **Registro físico pelo Controlador (não parte da decisão de mérito):** (a) seção "Regras de Evidence Harness (RULE-EPH-01..10)" em `governance/RULES.md`; (b) incorporação do campo opcional `Producer Historical Reliability` + versão v1.1 em `canon/CEM-001-...md` (Categoria B, GMC-CEM001-EXT-001).
- [ ] **Pendências de execução para o coordenador (sem Bash neste agente — RULE-MET-01):** `python scripts/validate_spec_sot.py specs/features/SPEC-002/plan.md`, `python scripts/check_refs.py`, `python scripts/check_doc_sync.py`, `python scripts/backlog_triggers.py`, `python scripts/build_map.py` (novos/alterados `.md` — GMC-CEM001-EXT-001, DHR-SPEC002-002, plan/checks). Não executei; reporto como pendência.

---

## 7. Efeito no backlog (RMR-001) — gate

**BL-012 (MC-COG-001)** — gatilho `spec:SPEC-002 homologada (consolidação cognitiva v1.5)` **DISPARA com este ato** (homologação do Plan). Registrado no passo 11-bis do RMR-001. Conforme RMR-001 §5, a promoção `Em espera → ATIVADO` e o tratamento (mapeamento COG-SPEC contra N8–N17, sem re-especificar) são **decisão de Andraus** / gate — não promovidos implicitamente por esta ata. O item permanece **`Em espera`** com o disparo do gatilho registrado como achado de gate para encaminhamento de Andraus.

Nenhum outro item entra em `ATIVADO` sem encaminhamento por este ato → gate fecha limpo.

---

## 8. Status final

**SPEC-002 — HOMOLOGADA — BASELINE (v1.1).** FASE 1 (Núcleo Cognitivo), posição 1, concluída. Próximo trabalho autorizado da Trilha B: **SPEC-003** (Conviction Vector, Evidence Fusion Engine & Conviction Engine — slot indicativo; **não abrir** sem Dossiê de Pesquisa e homologação da abertura, RULE-ECC-01/02). SPEC-003 permanece travada no mérito por **J-001** (fórmula/pesos/limiares definitivos do Conviction Vector).

Conforme GMC-001 Cap.5 (Regra de Congelamento): parecer conforme (Revisor) + consenso do Usuário (Andraus) + registro pelo Controlador — os três critérios satisfeitos.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
