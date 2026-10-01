# DHR-EUA-E20 — Ata de Homologação: FASE RISK (6 macro-slots indicativos da família RISK-SPEC)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Instrução direta de Andraus (chat, 2026-10-01): homologação da **EUA-E20** (FASE RISK com 6 macro-slots indicativos) |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA por instrução direta de Andraus em chat** — adota a `governance/EUA-E20_Fase_RISK_Slots_PROPOSTA.md` (§2/§6) |
| Compatibilidade | Minor — institui uma **FASE RISK** no ROADMAP com **6 macro-slots INDICATIVOS** (RULE-ECC-01/02); **não** enumera/numera as 23 RISK-SPEC; **não** autoriza a família (gatilho composto de BL-018 não disparou); **não** renumera/apaga slots (SPEC-016 preservada); **não** introduz a cláusula "via Risk Harness"; não redefine canônico (CONST-01) |
| Autoridade-fonte | `governance/EUA-E20_Fase_RISK_Slots_PROPOSTA.md`; `backlog/BL-018-RISK-AGENT-backlog.md`; `reference/SOT-RISK-MASTER-001_Consolidado.md` §3.6/§6.2; `governance/DHR-EUA-E19a_...md`; `governance/DHR-ARQ-002_...md`; `ROADMAP.md` §21/§26; `docs/MATRIZ-WORKFLOW-SPEC.md` §1/§7/§8; RULE-ECC-01/02; RULE-HV |
| Não fecha | Nenhuma decisão aberta (CONS-01): **RISK-ARR-LOC-001**, **RISK-CONV-001**, **J-001**, **D-RISK-SP-001**, **CDM-001** seguem **ABERTAS**. Não autoriza/numera a família. Não antecipa a FASE 6. Não edita `WORKFLOW.md`. |

---

## 1. Problema (resumido)

A família **RISK-SPEC** (Risk Agent, BL-018) está descrita como **23 Specs em 8 Grupos** em `reference/SOT-RISK-MASTER-001_Consolidado.md` §6.2, mas **não tem slots numerados no ROADMAP** (contingente à EUA-E20). Enumerar 23 slots antecipadamente contraria a **Especificação Emergente** (RULE-ECC-01: o ROADMAP não pré-determina quantidade/numeração; slots só se fixam na abertura, com Dossiê). A melhor prática é propor **poucos slots-macro indicativos**, agrupando os 23 por coesão, preservando a rastreabilidade de cada RISK-SPEC, dos invariantes e das decisões abertas. [FONTE: EUA-E20 §1; RULES.md RULE-ECC-01.]

## 2. Decisão (institui a FASE RISK — direção, não autorização)

1. **Institui-se a FASE RISK** no ROADMAP, **após a FASE 6** (sem conflito com a FASE GOV, já fixa — F-07/BL-018), com **6 macro-slots INDICATIVOS** (RISK-M1..M6) + linha de **Skills de risco diferidas** (I-001 FECHADA/SPEC-025). Nenhuma das 23 RISK-SPEC é enumerada como slot (RULE-ECC-01):

   | Macro-slot (indicativo) | Agrupa (Master §6.2) | Coesão / natureza cognitiva | RISK-SPEC mapeados (expectativa de cobertura) |
   |---|---|---|---|
   | **RISK-M1 — Fundamento & Cognição de Risco** | Grupos A + B | Princípios + disciplinas epistêmicas/causais/incerteza (herdam N8–N17 via RULE-HV) | RISK-SPEC-001..009 |
   | **RISK-M2 — Decisão sob Risco & Risco-Retorno** | Grupo C | Autoridade ACCEPT/WAIT/REJECT/ABSTAIN + deltas genuínos (R:R, exposição, risco de modelo) | **RISK-SPEC-010 (fecha RISK-CONV-001)**, 011 (R:R≥1:3 + Heat≤15% + alavancagem), 012, 013 |
   | **RISK-M3 — Quantificação & Stress** | Grupo D | Toolbox quantitativo determinístico + simulação + calibração | RISK-SPEC-014, 015, 016 |
   | **RISK-M4 — Memória, Aprendizado & Metacognição de Risco** | Grupo E | Memória + aprendizado (qualidade≠resultado) + metacognição (N17) | RISK-SPEC-017, 018, 019 |
   | **RISK-M5 — Operacionalização: Risk Harness, RDR & Signal Package** | Grupo F | Gate E3 + objeto de decisão + contrato de fronteira | **RISK-SPEC-020 (Risk Harness — gate E3; "via Risk Harness" entra aqui)**, 021 (RDR — depende CDM-001), **RISK-SPEC-022 (Signal Package — D-RISK-SP-001)** |
   | **RISK-M6 — Avaliação & Adversarial de Risco** | Grupo H | Avaliação do próprio Risk Agent; **herda SPEC-020 núcleo A via RULE-HV** | RISK-SPEC-023 |
   | **(diferido) RISK-Skills** | Grupo G | Skills de risco | diferidas a **I-001 (FECHADA, DHR-I001-001)** / SPEC-025 |

2. **Cobertura preservada (RULE-ECC-01, item 4).** Os 23 RISK-SPEC do Master mapeiam integralmente a RISK-M1..M6 (+ Skills diferidas) — **nenhuma capacidade descartada em silêncio**. Os macro-slots são **grão de container**; a decomposição fina de cada um (que pode dividir/fundir/renumerar — INV-07) só ocorre **na abertura**, por Dossiê (RULE-ECC-02) + homologação.

3. **Pontos obrigatórios preservados (instrução de Andraus):** RISK-SPEC-010 (fecha RISK-CONV-001) → RISK-M2; RISK-SPEC-020 (cláusula "via Risk Harness" em P14/INV-05) → RISK-M5; RISK-SPEC-022 (Signal Package) → RISK-M5; **SPEC-016/TMP** permanece **slot próprio do ROADMAP** (FASE 6, repurposada — TMP interno Synthesis→Risk), **não** absorvido pela família, ancorando **INV-RISK-00** junto de RISK-M5.

4. **Coerência de simetria (EUA-E23 §6):** o número **6** destes macro-slots **não muda**. O Risk Agent é um **sub-harness completo** (camadas próprias N8–N17 de risco), análogo ao núcleo cognitivo inteiro — não a um único agente analítico. **Milestone FASE 6:** com a absorção do Synthesis pelo Manager (DHR-ARQ-002), "FASE 6/Synthesis concluída" passa a significar **"Fase 2 do Manager (Convicção & Síntese, SPEC-014 repurposado) homologada"** — gatilho de BL-018 a **re-apontar na autorização da família** (não fechado aqui; CONS-01).

5. **Invariantes de risco incidentes** (origem EUA-E19a, a especializar na família): **INV-RISK-RR** (R:R ≥ 1:3) → RISK-M2; **INV-RISK-HEAT** (Portfolio Heat ≤ 15% com correlação) → RISK-M2; **INV-RISK-LEV** (alavancagem dinâmica) → RISK-M2; **INV-RISK-00** (isolamento epistêmico — pré-condição dura) → RISK-M5 + SPEC-016.

6. **Escopo do que NÃO é decidido aqui (CONS-01):** **não** autoriza/numera a família RISK; **não** fecha RISK-ARR-LOC-001, RISK-CONV-001, J-001, D-RISK-SP-001, CDM-001; **não** antecipa a FASE 6; **não** introduz a cláusula "via Risk Harness" em P14/INV-05 (entra **apenas** com RISK-SPEC-020/RISK-M5, por EUA-E19a/C-03); **não** renumera/apaga slots (SPEC-016 preservada); **não** edita `WORKFLOW.md`. A FASE RISK permanece **não-autorizada** até homologação de abertura, cuja **pré-condição dura** é o milestone FASE 6 (Manager Fase 2 homologada).

## 3. Efeitos aplicados (propagação mínima e rastreável — Controlador, 2026-10-01)

| Arquivo | Mudança | Natureza |
|---|---|---|
| `ROADMAP.md` (nova §10-bis "FASE RISK") | Seção FASE RISK após a FASE 7/antes de FASE 8; 6 macro-slots indicativos RISK-M1..M6 + linha de Skills diferidas; decisões abertas incidentes listadas | Direção/registro |
| `ROADMAP.md` §21 (caminho crítico) | Nota: FASE RISK após FASE 6 (Manager Fase 2); `... → 016 TMP → [FASE RISK] RISK-M1..M6`; sem enumerar os 23 | Direção/registro |
| `ROADMAP.md` §26 (capacidades) | Linha "FASE RISK — Risk Agent (RISK-M1..M6, EUA-E20)" como restrição de cobertura; capacidades de BL-018 não descartadas | Direção/registro |
| `backlog/BL-018-RISK-AGENT-backlog.md` | Nota: família recebe 6 macro-slots indicativos (EUA-E20 homologada); Estado permanece `Em espera`; gatilho `milestone:FASE 6` re-interpretado como "Manager Fase 2 homologada" (DHR-ARQ-002), a re-apontar na autorização | Backlog (fonte rica) |
| `backlog/RMR-001_Painel_Backlog.md` (BL-018 + §6 nota 11-bis) | Nota de gate 11-bis da homologação EUA-E20; BL-018 permanece `Em espera` (NÃO promovido nem fechado); decisões abertas de risco preservadas | Painel vivo |
| `AGENTS.md` §6 item 9 | Parêntese: família RISK = 6 macro-slots indicativos (EUA-E20); cláusula "via Risk Harness" **preservada** (entra só com RISK-SPEC-020) | Operacional (não-baselined) |
| `governance/CATALOGO-OFICIAL.md` §7.3 | Linha DHR-EUA-E20 (REGISTRADO); prefixo **EUA-E20 registrado como usado** | SSoT |
| `.claude/agents/especificador.md` + carimbo | `sincronizado-até` → última DHR; SYNC-DATE 2026-10-01; nota EUA-E20 | RPSA |
| `.claude/agents/revisor.md` + carimbo | `sincronizado-até` → última DHR; SYNC-DATE 2026-10-01; nota EUA-E20 | RPSA |

**Não tocado (baselined / soberano):**
- `CONSTITUTION.md` / `AGENTS.md` §6 item 9 núcleo / `atomic-spec.md` INV-05 — a cláusula **"via Risk Harness"** NÃO entra agora (só com RISK-SPEC-020). INV-05 permanece "SOT não executa — produz Signal Package".
- `WORKFLOW.md` — soberano de Andraus (WF-07/WF-P01/WF-X01..X03 já apontam a família RISK como dona a numerar; consistente).
- `reference/SOT-RISK-MASTER-001_Consolidado.md` — fonte rica, inalterada.

## 4. Guardas de sincronização (detector `check_doc_sync.py`)

- **D1/D2:** nenhuma decisão aberta é fechada nem flipada. RISK-ARR-LOC-001, RISK-CONV-001, J-001, D-RISK-SP-001, CDM-001 seguem **ABERTAS**. BL-018 **não** é promovido (permanece `Em espera`) nem absorvido — o gatilho composto (`milestone:FASE 6 concluída`) **não** disparou.
- **D6 (WORKFLOW.md):** nenhuma `WF-Dxx` aberta declarada fechada; nenhum `WF-xx` inexistente citado; `WORKFLOW.md` não editado.
- **Slots:** nenhum slot renumerado/apagado; SPEC-016 preservada; RISK-M1..M6 são **indicativos** (RULE-ECC-01/02).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
