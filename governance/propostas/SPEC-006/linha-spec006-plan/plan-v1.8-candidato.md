# SPEC-006 — Cognitive Knowledge Graph

| Campo | Valor |
|---|---|
| ID | SPEC-006 — Cognitive Knowledge Graph — **etapa v1.0 "núcleo"** (Opção 2 — DHR-SPEC006-002 D1): contrato cognitivo da **memória semântica permanente** do SOT (registro, ontologia, versões, consulta, causalidade, colisão, governança de escrita) com **UMA regra de admissão que nega por padrão toda escrita de conhecimento**; os contratos dos caminhos de entrada são **emendas aditivas futuras** (fora de escopo). **Mecanismo físico de armazenamento INDETERMINADO — H-001 ABERTA** |
| Versão | 1.8 (candidato — rodada 9; etapa v1.0 "núcleo") |
| Status | **CANDIDATO — aguarda verificação de spec (checks.md), gate determinístico, parecer do Revisor e homologação de Andraus.** NÃO é baseline (INV-09). **Por desenho, o núcleo não admite nenhum registro de conhecimento** (D4.15); só o log de decisões dos gates é gravado (D4.5). RULE-CKG-* e o contrato de nó/relação são **[PROPOSTA]** até homologação. **H-001 (mecanismo físico do KG) permanece ABERTA — este Plan NÃO a fecha** (CONS-01; só Andraus). M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 seguem ABERTAS. |
| Fonte | ROADMAP §6 (FASE 3); `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/` (Dossiê — RULE-ECC-01/02/04/06; validade CRITICAL 90 dias, limite 2027-01-03); DHR-SPEC006-001 (abertura); **DHR-SPEC006-002** (Opção 2 em etapas; nota aditiva ao RMR-001); atomic-spec **v1.5**; `governance/RULES.md` (RULE-BB-004, RULE-CAU-01/02/03, RULE-INQ-03, RULE-MECH-01, RULE-HD-02/03/04, RULE-ONT-01); `canon/CEM-001`, `canon/CHM-001`, `canon/CCM-001`, `canon/CEE-001` l.111, `canon/SAS-001` §6.12; `WORKFLOW.md` (conformidade, não editada) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §6 "P0 — CRITICAL"; atomic-spec §3 (emenda SPEC006-MATRIZ) "Knowledge Graph \| CRITICAL \| D0–D7"; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profundidade-alvo | **D0–D7 + D8 adversarial focado** (imutabilidade INV-07, confiança ≠ Convicção INV-04, causalidade pós-hoc RULE-CAU, colisão, governança de escrita), **sem elevar o profile em silêncio** — mesma reconciliação da SPEC-004 [FONTE: ROADMAP §6; AGENTS.md §4; DHR-SPEC006-001 Q-ABERTURA-2] |
| Profile (Claude Code) | standard + adversarial (D8) |
| Posição no caminho crítico | FASE 3 — MEMÓRIA SEMÂNTICA E RAG; após SPEC-005 (BASELINE v1.0, DHR-SPEC005-002); antes da SPEC-007 (formação/retrieval — não absorvida) [FONTE: ROADMAP §6/§21] |
| Nível de maturidade-alvo | **L3 (Testável)** — CRITICAL → L3 teto spec-first; gate normativo E3 por-Spec (RULE-MM-05, SPEC-021) |
| Método | atomic-spec.md **v1.5**; CC-11/RULE-MECH-01 (Classe por BASpec); RULE-PD-01/CC-12 **(N/A — infraestrutura agnóstica de escola)**; RULE-ECC-04/06; RULE-ECC-05 **(N/A — não toca comportamento de trading)**; RULE-MM |
| Classe predominante (orientação não-vinculante, §10.6) | Mista — **D** (catálogo, temporalidade, versionamento, consulta, trace) + **C** (admissão, governança, imutabilidade, proveniência, guard INV-04, colisão) + **H** (juízo de similaridade/causalidade com gate de saída) — declaração normativa **por BASpec** (SES-001 §50) |
| Autor | Especificador Principal (Claude Code; v1.0–v1.5 Opus 4.8; v1.6–v1.8 Opus 5.5) |
| Data | 2026-10-18 (rodada 9; ordem de Andraus no chat; após parecer NÃO CONFORME da rodada 8 — `parecer-revisor-rodada8.md`, 0 Críticas · 4 Médias) |
| Abertura | Dossiê de Pesquisa aprovado por Andraus na abertura (DHR-SPEC006-001, `research.md`); Plan dentro da validade do Dossiê (CRITICAL → 90 dias; limite 2027-01-03; ECC-VAL-001 decidida em DHR-DEC-003) |

Complexidade: CRITICAL. Profundidade-alvo: D0–D7 + D8 adversarial focado (standard + adversarial).

**Princípio fundador (transversal):** **MEMÓRIA PERMANENTE ≠ MEMÓRIA DE TRABALHO.** *"Blackboard ↓ memória de trabalho. Knowledge Graph ↓ memória permanente. Nunca misturar."* (KERNEL-V2; ROADMAP §5/§6). O KG é a representação semântica permanente do conhecimento já validado e de suas relações auditáveis — não é "banco de grafos" (research.md §0) nem memória de trabalho (SPEC-004). Este Plan define **o QUE**; o mecanismo físico é **INDETERMINADO = H-001 (ABERTA)**. [FONTE: ROADMAP §6; DHR-SPEC006-001 Q-ABERTURA-3; research.md §0/§8]

**Status epistemológico de cabeçalho:** a SPEC-006 é a camada Harness/operacional sobre responsabilidades que os canônicos BASELINED já atribuem ao KG (CEM-001 l.494, l.562-565, l.608-615, l.699; CONSTITUTION l.233 EC-COG-003; SAS-001 §6.12; CEE-001 l.111). **NÃO redefine** CHM-001, CEM-001, CCM-001 nem reabre SPEC-004/005 (CC-02/CONST-01/INV-09). [FONTE: ROADMAP §6/§7; atomic-spec §12; DHR-SPEC006-001 §3]

**Convenção de fonte única "dura" (v1.7; mantida na v1.8):** **D4 (D4.0–D4.20) é o ÚNICO lugar de predicado, de obrigatoriedade de campo (de TODO `record_kind` — D4.19), de classe de operação, de ordem/precedência e de código de rejeição ou de desfecho.** §D2.1 e §D2.2 são tabelas de DADOS lidas por D4.1/D4.13. O I/O Schema lista **só campos e tipos** (sem "obrigatório", sem código). RULE, BASpec, EARS, D6, EC, cenários, ADV e §7-bis **citam o item de D4** e não reenunciam o predicado. Em divergência aparente, prevalece D4.

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-10-11 | Entrega candidata inicial (Opção A; mecanismo físico INDETERMINADO = H-001). |
| 1.1 | 2026-10-12 | Rodada 2 (achados do gate e do Revisor). |
| 1.2 | 2026-10-12 | Rodada 3 (revisão independente). |
| 1.3 | 2026-10-12 | Rodada 4 (6 Maiores do controle). |
| 1.4 | 2026-10-17 | Rodada 5 (retomada por Andraus). |
| 1.5 | 2026-10-17 | Rodada 6 (parecer NÃO CONFORME da rodada 5). |
| 1.6 | 2026-10-17 | Rodada 7 (parecer NÃO CONFORME da rodada 6; fonte única D4.1–D4.18). |
| 1.7 | 2026-10-18 | Rodada 8 — Opção 2 (DHR-SPEC006-002): núcleo com regra única de admissão (D4.15); D4.0/D4.5/D4.19/D4.20; contratos de caminho = emendas E-a..E-e. |
| 1.8 | 2026-10-18 | **Rodada 9 (parecer NÃO CONFORME da rodada 8 — 0 Críticas, 4 Médias).** **R8-1:** D4.0 ganha **classes de operação** (MUTAR, ALTERAR_CATÁLOGO, ANEXAR_LOG, CONSULTAR, SUBMETER) avaliadas antes de qualquer predicado — dá posição a `RECORD_MUTATION_FORBIDDEN`, `QUERY_WRITE_FORBIDDEN`, `ONTOLOGY_CHANGE_NOT_GOVERNED`; atos de governança de ontologia em runtime = conjunto vazio na v1.0 (K-001 ABERTA, não decidida); consulta read-only não grava nem no log, tentativa de gravação é negada e registrada sob EC-CKG-003 (E3); EC-006 permanece E1 (justificado); T23; ADV-07/14 com `reason`. **R8-2:** D4.19 cobre todos os `record_kind` (inclui `transition_timestamp`/`transition_origin`/`justification` — CEM-001 l.428 —, `from_node`, `relation_type`, `reason`/`relevance`, campos de `collision`, `canonical_status` vindo de D4.16 — r8-m); T20 (h)–(m); ADV-25. **R8-3:** registros derivados (`collision`, `DERIVA_DE` materializada; `publication.origin = kg_internal`, atribuído pelo KG) — herdam a admissão da submissão (D4.15), proveniência própria (D4.2), validação no passo 11 (D4.18); "Escopo em etapas" e Bloco B ajustados; ADV-26. **R8-4:** `GATE_RECORD_UNRESOLVED` (D4.2, passo 11) + `collision_pair` na decisão de CKG-013 (distingue PASS com/sem colisão); T17 com negativo; T24; ADV-27. Menores r8-a..r8-k e r8-m; r8-l registrado como [DECISÃO NECESSÁRIA] (Andraus). Contagem: 13 BASpecs; 6 EC; 24 EARS; 26 cenários (T01..T26); 27 adversariais (ADV-CKG-01..27); 2 invariantes locais. Rastreabilidade: checks.md §13. |

> O detalhe das linhas 1.0–1.7 foi **transferido sem alteração** para `checks.md`, Apêndice H (INV-07: preservado, não apagado; versões integrais no histórico git do ramo `spec006-plan`). Motivo: o changelog reenunciava regras e gerava cópia extra a manter coerente (`PROPOSTA-DIVISAO-2026-10-17.md` §1.4).

---

## Escopo em etapas (Opção 2 — DHR-SPEC006-002)

[FONTE: DHR-SPEC006-002 §1 D1–D3; `governance/propostas/SPEC-006/PROPOSTA-DIVISAO-2026-10-17.md` §2 Opção 2 ([PROPOSTA] escolhida por Andraus)]

- **v1.0 (este Plan) = núcleo:** CKG-001..013 — ontologia e matriz, entidades por referência, relações tipadas, bitemporal, proveniência, envelope append-only e log imutável, guard de custo e confiança, causalidade/similaridade, governança de escrita, consulta e trace completo, lifecycle, colisão — **e uma porta de admissão única** (RULE-CKG-010; D4.15): sem contrato de admissão homologado aplicável ⇒ DENY. **Na v1.0 o conjunto de contratos de admissão é vazio.**
- **Fora de escopo — emendas aditivas futuras (listadas SEM contrato; cada uma só após decisão de Andraus):**
  - **E-a** — caminho do ciclo de vida canônico (hipótese/evidência/convicção e suas transições): critério, produtor, gatilho; coincidência `producer_id` ↔ objeto canônico; preservação de estados de hipótese/convicção; reconciliação de transição canônica perdida; critério de promoção trabalho→permanente (S14).
  - **E-b** — conhecimento formado com selo da SPEC-007: contrato do selo, tratamento de selo ausente e sua precedência.
  - **E-c** — relações registradas por produtor (SAS-001 l.924).
  - **E-d** — nós de referência (asset, timeframe, regime, observation, calibration_metric, structure, narrative, mission).
  - **E-e** — consumo de `Evidence.Invalidated` (SPEC-005) e emissão de evento pelo KG.
  - Cada emenda de caminho define também os registros subsequentes do sujeito que admitir (invalidation, archival, canonical_state_transition) e quem pratica esses atos.
- **Registros derivados — DENTRO do núcleo, sem caminho próprio (R8-3):** `collision` (D4.13) e a `creation` de `DERIVA_DE` materializada (D4.17) são gerados pelo próprio KG (`publication.origin = kg_internal`, atribuído pelo KG — D4.2) dentro da unidade D4.18 de uma submissão que passou D4.15; **herdam a admissão e a autorização dessa submissão** (D4.15), têm proveniência própria (D4.2, `GATE_RECORD_UNRESOLVED`) e são validados no passo 11 (D4.0/D4.18). Não são caminho de entrada nem submissíveis de fora; **toda emenda fica proibida de criar contrato de admissão para `collision` ou `DERIVA_DE` submetidos externamente** [PROPOSTA]. Na v1.0 são inalcançáveis em runtime (nenhuma submissão passa D4.15) — verificáveis só por predicado e fixture (T17, T19, T24).
- **Restrição a toda emenda (leitura única da herança — R7-4) [INFERÊNCIA de RULE-HD-03 + CEM-001]:** nenhuma emenda pode restringir **quais estados ou versões de uma Evidência admitida** o KG preserva — CEM-001 l.494 ("Knowledge Graph | Todos os estados") e l.611-614 atribuem ao KG toda a linhagem, todas as versões e todos os estados. Restringi-los seria supressão de obrigação herdada fora de REMOVED (RULE-HD-03) e exigiria REMOVED governado. A v1.0 entrega o **mecanismo** (D4.16; `canonical_state_transition`); a satisfação ponta-a-ponta fica **PARCIAL** até E-a — **bloqueada a montante por desenho, não enfraquecida**.
- **Governança das emendas:** aditivas (INV-07), mesmo número SPEC-006, ciclo Especificador → Revisor → Andraus. Não reabrem o núcleo, salvo por emenda declarada. Os gatilhos `spec:SPEC-006` de BL-003/BL-011 não mudam (DHR-SPEC006-002 D2 — nota aditiva, sem re-apontamento formal).
- **Pendências que NÃO são emendas de caminho** (seguem [DECISÃO NECESSÁRIA] na tabela de etiquetagem): mantenedor da allowlist; host do juízo; mapeamento `producer_id` → `school` para SMC/Fibonacci/ICT/Fractal; migração de ontologia; escala de confiança; limiar de falso-DENY; autorização de leitura.

---

## Nota de gate (passo 11-bis / RMR-001)

[FONTE: ROADMAP §23 passo 11-bis; `governance/DHR-BACKLOG-001_Ata_Promocao_BL003_BL011_ATIVADO.md` §1-§2; DHR-SPEC006-002 D2; `backlog/RMR-001_Painel_Backlog.md` l.102 (BL-003), l.110 (BL-011), l.128 (BL-029), l.191-192; `governance/CLASSIFICACAO-COLISOES-BL010-011-012.md` l.23/l.51-62; `governance/CONFLICT-MAP.md` l.143-147]

- **BL-003 e BL-011 estão `ATIVADO`** (ata DHR-BACKLOG-001 §1; RMR-001 l.102/l.110/l.191), com encaminhamento ao gate da SPEC-006. A entrega em etapas **não** é divisão para o RMR-001 (DHR-SPEC006-002 D2): gatilhos inalterados. O Especificador não edita o RMR-001.
- **BL-003** (persistência física de hipótese/estado): a camada LÓGICA da persistência permanente é este núcleo (D4.3/D4.4/D4.7); a admissão de hipótese/estado é E-a (fora de escopo); a parte FÍSICA é H-001/G-001 (ABERTAS — ata §2). Estado do BL-003 após a homologação = **[DECISÃO NECESSÁRIA]** (Andraus).
- **BL-011** (MC-EXP-001, ref. externa K-MAN-15): rótulos R-xx/X-xx não são catálogo fechado (CLASSIFICACAO l.23); R-04..R-06 = residuais de aplicação (CLASSIFICACAO l.58-62; RMR-001 l.110) — **[INFERÊNCIA]** por conteúdo. Pela ata §2, R-04..R-06 e COL-EXP-05 são **decididos no gate** (Andraus); por isso cada linha abaixo é **encaminhamento com tratamento proposto**, não tratamento decidido (r7-f):

| Rótulo | Conteúdo (fonte) | Classificação | Encaminhamento — tratamento proposto |
|---|---|---|---|
| X-01 | COL-EXP-01 — status "BASELINE" do MC-EXP-001 (CONFLICT-MAP l.143) | REJEITAR efeito | nenhum texto do MC-EXP-001 citado como norma (INV-09) |
| R-01 | COL-EXP-02 — Quality Gates G0–G8 (l.144) | gate LOCAL | nenhum rótulo G-xx; maturidade L3 (RULE-MM) |
| R-02/R-03 | COL-EXP-03 — I-EXP-01..12 / EXP-P01..P14 (l.145) | ADAPTAR como LOCAIS | nenhum ID importado; equivalências só por âncora SOT (RULE-BB-004/INV-07; RULE-CAU-03) |
| R-04 [INFERÊNCIA] | `confidence` ≠ Conviction Vector (CLASSIFICACAO l.59) | fronteira CONFORME (l.59) × residual ADIADO (l.62) — **leitura em divergência, [DECISÃO NECESSÁRIA]** | guard D4.12 (CKG-007); J-001 não tocada |
| R-05 [INFERÊNCIA] | Experience Record/Packet projeta CEM/CHM (l.58) | fronteira CONFORME (l.58) × residual ADIADO (l.62) — idem | nó referencia o canônico por id@version (CKG-002) |
| R-06 [INFERÊNCIA] | memória sem autoridade decisional; imutabilidade (l.60) | fronteira CONFORME (l.60) × residual ADIADO (l.62) — idem | D0/D1 (KG não decide); CKG-006 |
| X-04 | COL-EXP-04 — Working Memory §7.6 (l.146) | RELOCAR a SPEC-004 | fronteira: memória de trabalho = SPEC-004 (Non-goals) |
| R-07 | COL-EXP-05 — EXP-SPEC-021 ↔ RAG-SPEC-018 (l.147) | ADIAR reconciliação | **não executado**; onde reconciliar (gate desta Spec, SPEC-009 ou SPEC-007) e a fila EXP-SPEC-001..053 = **[DECISÃO NECESSÁRIA]** |

- **Pendência R-04..R-06 (r8-l) — [DECISÃO NECESSÁRIA], de Andraus; não decidida aqui:** a CLASSIFICACAO marca as três linhas de fronteira l.58-60 como "CONFORME" e, em l.62, declara os "Tratamentos residuais (`R-04..R-06` de aplicação) → **ADIADOS** à ativação (SPEC-006/009)". A identificação R-04..R-06 = fronteiras l.58-60 é **inferência** deste Plan. Leitura 1: são as fronteiras ⇒ o tratamento proposto apenas confirma a conformidade já classificada. Leitura 2: são tratamentos residuais distintos ⇒ seguem ADIADOS e esta tabela só os encaminha. Qual leitura vale, e se a ativação é esta Spec ou a SPEC-009, cabe a Andraus no gate (ata DHR-BACKLOG-001 §2).
- **BL-010** (MC-RAG-001) — `Em espera`; fonte de requisitos da SPEC-007 → tangente; não promovo. **BL-029** — `Em espera` (RMR-001 l.128); independente desta Spec.

---

## Constitution Check (CC-01..CC-12 — atomic-spec v1.5 §10.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** o KG é infraestrutura agnóstica de escola: armazena relações (inclusive HERDA/HIERARQUIA_DE) sem alterar a hierarquia nem a autoridade de criação de hipótese (Elliott cria a primária; ICT não cria — INV-01/INV-02). `school` (5 camadas) é DERIVADO (D4.14); espelhos: `hypothesis.school ≠ ICT` (RULE-HH-004) e PRIMARY ⇒ Elliott (RULE-HH-002). [FONTE: INV-01/02; SPEC-001 l.100/l.108]
- [x] **CC-02 — Não redefine CEM/CHM/CCM/CDM/CNM nem SPEC-004/005:** entidades por ID+versão; campos espelhados (`producer_*`, `evidence_origin_type`, elos de versão) são cópias de referência. CDM-001/CNM-001 pendentes não acionam CONST-01. [FONTE: CEM-001 l.608-615; CHM-001; CCM-001]
- [x] **CC-03 — Conviction Vector:** o KG não computa convicção; "confiança de relação" ≠ Conviction Vector; dimensionalidade=8 intocada; fórmula/pesos/limiares definitivos do Conviction Vector **pendentes (J-001 ABERTA)**; nenhum limiar de convicção declarado. [FONTE: INV-03; J-001/N-001 ABERTAS]
- [x] **CC-04 — Salvaguardas CEE-001 §10/§11:** nenhuma violada; o KG não emite sinal nem dimensiona risco; INV-04 preservado pelo guard D4.12 (CKG-007). [FONTE: CEE-001 §10/§11]
- [x] **CC-05 — Complexidade:** CRITICAL, D0–D7 + D8 focado.
- [x] **CC-06/CC-07 — SES-001 §59/§60:** N/A nesta entrega (Spec/Plan, não Engineering Card; BUILD adiado — atomic-spec §14). Rastreabilidade: ROADMAP §6 → Dossiê → DHR-SPEC006-001/002 → este Plan.
- [x] **CC-08 — Herança/Delta:** presente; INHERITS com ID+versão (RULE-HD-04); REMOVED vazio; MODIFIED só RULE-BB-004 reforçada (RULE-HD-02). Eixo VERTICAL (RULE-HV) não aplicável.
- [x] **CC-09 — Status epistemológico:** mecanismo físico = INDETERMINADO (H-001 ABERTA); admissão positiva = fora de escopo da v1.0 (não INDETERMINADO convertido em PASS); presença ≠ veracidade declarada (D4.2/D4.10/D4.14); fontes web = DADO [EXTERNO].
- [x] **CC-10 — Terminologia concorrente:** INCIDE — ver "Declaração de acepção semântica".
- [x] **CC-11 — Classe por BASpec com efeito:** cada BASpec declara D/C/H com critério 4Es; C/H com gate de saída; H (CKG-008) com bounded loop (D4.11).
- [x] **CC-12 — `PD-xx`:** N/A (infraestrutura agnóstica de escola — DHR-SPEC006-001 §2; ABERTURA §6). Registrado, não suprimido.

**Disciplinas N8–N17 incidentes:** RULE-EPI (H-001 ≠ fato), RULE-CAU-01/02/03 (CKG-008), RULE-MET-01 (não-fabricação), RULE-UNC-01..03 (eficiência de consulta ampla até H-001), RULE-SEM-01/04, RULE-ONT-01/02, RULE-INQ-03 (D4.11), RULE-DEC-01 (o KG não decide nem executa — INV-05). Detalhe: §7-bis Bloco C.

---

## Herança / Delta (§8.3 — EUA-E04 / RULE-HD)

```
HERANÇA / DELTA — SPEC-006 (etapa v1.0 "núcleo")

INHERITS (referência por ID + VERSÃO baseline — RULE-HD-04; NÃO redefinidos):
  - canon/CEM-001 (BASELINE) — Responsabilidades do KG sobre a EVIDÊNCIA (l.608-615): toda a linhagem, TODAS as versões,
    TODOS os estados (também l.494), Cognitive Trace Reconstruction COMPLETA (l.562-565, l.699). Campos espelhados:
    Producer Type/ID (l.271-278), Evidence Origin Type e seu acoplamento PRIMARY⇒AGENT / DERIVED⇒ENGINE (l.280-283),
    Lineage (l.351-355), sucessora em SUPERSEDED (l.450); registro de timestamp, origem e justificativa de toda alteração
    de Status (l.428 — presença exigida em D4.19). Satisfação ponta-a-ponta PARCIAL até a emenda E-a (Bloco B)
  - canon/CHM-001 (BASELINE) — estados da hipótese; `previous_version_id` obrigatório em nova versão (l.283/l.588);
    `producer_type`/`producer_id` (l.361); grafo de transições (l.744-757). O KG relaciona por referência; não transiciona
  - canon/CCM-001 (BASELINE) — objeto Conviction Vector 8D; `previous_version_id`, `status` (l.58). O nó `conviction` só
    REFERENCIA o objeto (payload fechado — D4.12); confiança de relação nunca é o Conviction Vector
  - specs/features/SPEC-004 v1.2 (BASELINE) — append-only real (INV-CBP-01); publicação atômica tudo-ou-nada, sem
    "publicação sem registro de auditoria" (plan l.381/l.689); proveniência condicional (RULE-CBP-007, plan l.264-267);
    identidade autenticada pelo runtime (RULE-CBP-014; plan l.338). FRONTEIRA "Nunca misturar": herda a mecânica por referência
  - specs/features/SPEC-005 v1.0 (BASELINE) — TRANSPORTA eventos canônicos, inclusive `Evidence.Invalidated` (CEM-001
    l.600/l.722; SPEC-005 plan l.88/l.859), e NÃO escreve no KG (plan l.971). Consumo/emissão pelo KG = emenda E-e
  - canon/CEE-001 (BASELINE) l.111 — a métrica de calibração "entra no Knowledge Graph": o KG prevê `calibration_metric`
    isolado da convicção (D4.12); o caminho de entrada é E-d ⇒ evidência PARCIAL (Bloco B)
  - canon/SAS-001 §6.12 (l.923-924; l.163 EC-COG-003) — produtor registra relações, NÃO redefine ontologias (CKG-009);
    consulta "não é pré-requisito obrigatório"; contrato de registro por produtor = emenda E-c
  - governance/CONSTITUTION.md l.233 (EC-COG-003); l.191-192 (workspaces Observations × Evidence)
  - governance/RULES.md: RULE-BB-004 (l.324) — REFORÇADO (INV-07); RULE-CAU-01/02/03 (l.681-683); RULE-INQ-03 (l.678);
    RULE-ONT-01 (l.672)
  - Método: atomic-spec v1.5 (§10.2 l.238 "KG publicado → E3 mínimo"; §10.6 l.315; ENF-01..08; L3; §3 CRITICAL·D0–D7)
  - SPEC-019 v1.0 (RULE-HG; [INFERÊNCIA] alteração de ontologia = ato análogo; runtime = K-001 [DECISÃO NECESSÁRIA]);
    SPEC-020 v1.0; SPEC-021 v1.0 (RULE-MM)
  - Invariantes: INV-04 (CUSTO nunca no Conviction Vector — atomic-spec l.404; extensão à CONFIANÇA é LOCAL [PROPOSTA]),
    INV-05, INV-06, INV-07, INV-09, INV-10
  - WORKFLOW.md (fronteira soberana): não contradiz nenhum WF-xx; não fecha WF-D03

ADDED (delta local [PROPOSTA]):
  - Ontologia ENXUTA + matriz de integridade (§D2.1); catálogo de entidades por referência e de relações tipadas
  - Temporalidade bitemporal (D4.6); proveniência condicional com discriminantes fixos (D4.2); presença de campos (D4.19)
  - Imutabilidade append-only de conhecimento E log (D4.3/D4.5); estado = projeção (D4.7); admissão atômica (D4.18)
  - Guard de custo E confiança (D4.12); causalidade/similaridade com gate + bounded loop (D4.10/D4.11)
  - Governança de escrita E3 (D4.20) e do log (D4.5); PORTA DE ADMISSÃO única fail-closed (D4.15)
  - Consulta read-only + Cognitive Trace Reconstruction completa (D4.8); lifecycle; colisão (D4.13)
  - [PROPOSTA de recorte] contrato cognitivo com mecanismo físico INDETERMINADO — NÃO fecha H-001

MODIFIED:
  - RULE-BB-004 REFORÇADA como imutabilidade PERMANENTE do KG (INV-07) — texto/significado inalterados (RULE-HD-02)

REMOVED:
  - (vazio)
```

> **Eixo VERTICAL (RULE-HV):** avaliado e não aplicável — a SPEC-006 deriva de canônicos, Specs vizinhas e regras; não é decomposição micro de macro-spec. [INFERÊNCIA]

### Cobertura × lacuna (não duplicar — CC-02/INV-09)

| Capacidade | Coberta por baseline? | Tratamento na v1.0 |
|---|---|---|
| Linhagem/versões/estados da Evidência; trace completo | SIM (responsabilidade atribuída — CEM-001 l.494/608-615) | ESPECIFICADA como mecanismo verificável (CKG-002/011/012); ponta-a-ponta PARCIAL até E-a |
| Máquina de estados da hipótese | SIM — CHM-001 | HERDADA por referência; o KG não transiciona |
| Append-only; publicação atômica | SIM — SPEC-004 v1.2 | HERDADA a mecânica (CKG-006; D4.18) |
| Memória de trabalho; transporte de eventos | SIM — SPEC-004 / SPEC-005 | FRONTEIRA |
| Ontologia + matriz; entidades/relações tipadas | NÃO | ADDED (CKG-001/002/003) |
| Bitemporal; confiança ≠ Convicção; causalidade; consulta; lifecycle; colisão; governança | NÃO/Parcial | ADDED (CKG-004..013) |
| Admissão por caminho (a)/(b)/(c); nós de referência; consumo/emissão de eventos | NÃO | **Fora de escopo — emendas E-a..E-e**; núcleo nega por padrão (D4.15) |
| Mecanismo físico de armazenamento | NÃO — H-001 ABERTA | NÃO fixado (INDETERMINADO) |

---

## Declaração de acepção semântica (RULE-SEM-01 — CC-10)

> **Termo 1:** "Conhecimento permanente" (KG) = conhecimento já validado/publicado e suas relações auditáveis ≠ "memória de trabalho" (Blackboard — SPEC-004).
> **Termo 2:** "confiança de relação" (KG) = escala PRÓPRIA ≠ "Convicção" (CCM-001); nunca retroalimenta o Conviction Vector (INV-04).
> **Termo 3:** "esquecimento" (research.md §3.6) = arquivamento versionado, NUNCA deleção (INV-07).
> **Termo 4:** "documento recuperado" (RAG — SPEC-007) ≠ "conhecimento validado" (KG); "Observação" (Skill — INV-06; nó `observation`) ≠ "Evidência" (Agente/Engine; nó `evidence`).
> **Termo 5:** `hierarchy_role=PRIMARY` (hipótese primária — SPEC-001) ≠ `evidence_origin_type=PRIMARY` (evidência sem ancestral — CEM-001 l.282).
> **Termo 6:** estados do KG (projeção D4.7: ACTIVE_KNOWLEDGE/SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED) são HOMÔNIMOS ≠ estados canônicos (rastreados à parte em `canonical_status`).
> **Termo 7:** "admissão" (KG) = gravação de registro de conhecimento sob contrato de caminho ≠ "publicação" (Blackboard — SPEC-004).
> [FONTE: RULE-SEM-01/04; INV-04/06/07; GLOSSARIO; CEM-001 l.280-283; SPEC-001/004/005/007]

---

## Conformidade com o `WORKFLOW.md` (RULE-ECC-05 — NÃO-incidência)

> **RULE-ECC-05 NÃO INCIDE** [FONTE: DHR-SPEC006-001 §2; ABERTURA §1/§6; research.md §7]: a SPEC-006 não define comportamento de agente analítico, Conviction/Fusion, Manager ou Risk Agent — é infraestrutura de memória (como SPEC-002/004/005). Por prudência: o KG é consultado "quando necessário" (SAS-001 l.163); cita WF-xx só por ID, não contradiz nenhum e não fecha WF-D03.

## Princípios de Domínio (§10.7 — RULE-PD-01)

**N/A — não incide** (DHR-SPEC006-001 §2; ABERTURA §6; research.md §7). Nenhum `PD-xx` proposto. Registrado explicitamente.

---

## D0 — Missão (Intenção)

A SPEC-006 especifica **como o SOT preserva, relaciona e consulta o conhecimento permanente já validado** — ontologia e matriz, entidades e relações tipadas, temporalidade bitemporal, proveniência por referência, imutabilidade append-only, confiança de relação ≠ Convicção, governança de escrita E3, consulta e **Cognitive Trace Reconstruction COMPLETA** (CEM-001 l.608-615) — com **uma porta de admissão que nega por padrão** enquanto não houver contrato de caminho homologado, e com o **mecanismo físico INDETERMINADO (H-001 ABERTA)**. [FONTE: ROADMAP §6; CEM-001 l.608-615; SAS-001 §6.12; DHR-SPEC006-001/002]

**O que a Missão NÃO é:** memória de trabalho (SPEC-004); transporte/notificação (SPEC-005); formação/retrieval (SPEC-007); estado por agente (SPEC-009; G-001 ABERTA); ciclo P12 (SPEC-018; K-001 ABERTA); cálculo de convicção (SPEC-003/CCM-001; J-001/N-001 ABERTAS); redefinição de canônico (CC-02); escolha do mecanismo físico (H-001 ABERTA); decisão ou execução de ordem (INV-05/RULE-DEC-01); contratos de admissão por caminho (emendas E-a..E-e).

**Status epistemológico:** RULE-CKG-* e o contrato de nó/relação = **[PROPOSTA]**. CEM-001, CHM-001, CCM-001, CEE-001, SAS-001, SPEC-001/004/005/019/020/021, RULE-BB-004, RULE-CAU-01/02/03, atomic-spec v1.5, INV-*, ENF-* = FATO NORMATIVO. Fontes externas = [EXTERNO], DADO, nunca baseline (TRACE-06; documentado ≠ homologado).

---

## D1 — Escopo e Non-goals

### Dentro do escopo (v1.0)

| # | Item | Fonte |
|---|---|---|
| S1 | Ontologia enxuta + matriz de integridade (§D2.1; D4.1) | KERNEL-V2 l.1488-1507 (research.md §0/§3.6); DHR-SPEC006-001 Q-ABERTURA-4 |
| S2 | Entidades por referência: hypothesis (CHM-001), evidence (CEM-001), observation (INV-06), conviction (CCM-001), narrative, mission, learning, asset, timeframe, regime, structure, calibration_metric (CEE-001 l.111); `ontological_status` em nós teóricos (RULE-ONT-01) | CEM/CHM/CCM-001; CEE-001 l.111; RULES.md l.672 |
| S3 | Relações tipadas: CONFIRMA, REFUTA, DEPENDE_DE, HERDA, PERTENCE_A, INVALIDA, ORIGINA, DERIVA_DE, SIMILAR_A, CAUSA, HIERARQUIA_DE, ESTATISTICA_DE | ROADMAP §6; research.md §4; CEM-001 Cap.5 |
| S4 | Temporalidade bitemporal (D4.6) | research.md §3.1; INV-07 |
| S5 | Proveniência exigível (D4.2) | CEM-001 Cap.5; SPEC-004 RULE-CBP-007 |
| S6 | Imutabilidade append-only de conhecimento e log (D4.3/D4.5); "esquecimento" = arquivamento | INV-07; RULE-BB-004 |
| S7 | Confiança de relação ≠ Convicção (D4.12) | INV-04 |
| S8 | Similaridade/causalidade com gate de saída e bounded loop (D4.10/D4.11) | RULE-CAU-01/02/03; RULE-INQ-03 |
| S9 | Governança de escrita E3 (D4.20), do log (D4.5) e da ontologia | SAS-001 §6.12; SPEC-004; SPEC-019; atomic-spec §10.2 |
| S10 | **Porta de admissão única, fail-closed** (D4.15); contratos por caminho = emendas futuras | DHR-SPEC006-002 D1; ENF-04 |
| S11 | Consulta read-only + Cognitive Trace Reconstruction completa (D4.8) | CEM-001 l.608-615; SAS-001 §6.12 |
| S12 | Lifecycle derivado: SUPERSEDED / INVALIDATED_IN_TIME / ARCHIVED; correção por novo registro (D4.7) | CHM-001; INV-07 |
| S13 | Detecção e registro de colisão (D4.13; §D2.2) | research.md §8 |
| S14 | Permanente × temporário (ROADMAP §6): "temporário" = janela de validade (`valid_to`) ou arquivamento — nunca deleção. **Entrega parcial declarada:** o critério de promoção trabalho→permanente é E-a; atribuí-lo à SPEC-018/K-001 = **[DECISÃO NECESSÁRIA]** | ROADMAP §6; ABERTURA §35; K-001 (ABERTA) |

### Fora do escopo (Non-goals)

| Item | Pertence a |
|---|---|
| Mecanismo físico de armazenamento / tecnologia de banco de grafos | **H-001 (ABERTA — só Andraus)** |
| Memória de trabalho | SPEC-004 (BASELINE) |
| Notificação/transporte; consumo e emissão de evento pelo KG | SPEC-005 (BASELINE); emenda E-e |
| Formação de conhecimento / retrieval / selo | SPEC-007; emenda E-b |
| Contratos de admissão por caminho; nós de referência; critério de promoção | emendas E-a, E-c, E-d |
| Estado persistente por agente | SPEC-009 — G-001 (ABERTA) |
| Ciclo de evolução do conhecimento (P12) | SPEC-018 — K-001 (ABERTA) |
| Fórmula/pesos/limiares de convicção | SPEC-003/CCM-001 — J-001/N-001 (ABERTAS) |
| Redefinir CHM/CEM/CCM/SPEC-004/005 | CC-02/CONST-01/INV-09 |
| Componente "Cognitive Ontology" separado | ontologia DENTRO da SPEC-006 (Q-ABERTURA-4) |

---

## D2 — Regras

> **Etiqueta:** RULE-CKG-* e o contrato de nó/relação são **[PROPOSTA]** — normativos só na homologação de Andraus + registro do Controlador (RULE-HG-02). As RULE/INV/ENF citadas como fundamento já existem (FATO NORMATIVO). **Cada RULE enuncia a obrigação e aponta o item de D4 (fonte única).**

```
RULE-CKG-001: Todo nó e toda relação DEVEM pertencer à ontologia (§D2.1) e satisfazer a matriz e as regras de nó;
              violação é rejeitada sem escrita. Ontologia ENXUTA, DENTRO da SPEC-006. → D4.1, D4.14, D4.19
              [Fonte: KERNEL-V2 l.1488-1507; DHR-SPEC006-001 Q-ABERTURA-4]  [PROPOSTA]

RULE-CKG-002: Toda entidade que corresponde a objeto canônico DEVE referenciá-lo por ID+versão, sem redefinir contrato,
              campos ou máquina de estados; observation NÃO é evidence. → D4.1, D4.16
              [Fonte: CEM-001; CHM-001; CCM-001; CC-02; INV-06; INV-10]  [PROPOSTA]

RULE-CKG-003: Toda relação DEVE ser tipada, armazenada direcionada e ter proveniência; simetria é semântica de consulta;
              contradição não é resolvida em silêncio. → D4.1, D4.2, D4.17, RULE-CKG-013
              [Fonte: ROADMAP §6; research.md §4/§8; INV-07]  [PROPOSTA]

RULE-CKG-004: Mudança de validade é ATO AUTORIZADO por novo registro `invalidation`, nunca mutação nem cascata
              automática (CEM-001 l.602; impacto é de CHM/CCM — l.503/606; CHM-001 l.672-676). → D4.6, D4.3
              [Fonte: research.md §3.1; INV-07; SPEC-004 INV-CBP-01]  [PROPOSTA]

RULE-CKG-005: Nenhuma entidade/relação existe sem proveniência exigível, espelhando a condicionalidade de SPEC-004
              RULE-CBP-007 (sem regra mais forte); não fabricar proveniência (RULE-MET-01). → D4.2
              [Fonte: CEM-001 l.271-283/l.351-355; SPEC-004 RULE-CBP-007/014]  [PROPOSTA]

RULE-CKG-006: O KG é APPEND-ONLY PERMANENTE — nenhum `kg_record` nem `kg_gate_decision` é deletado ou mutado; todo
              registro de conhecimento usa o envelope único; a admissão é unidade atômica. → D4.3, D4.4, D4.5, D4.18
              [Fonte: INV-07; RULE-BB-004 (l.324); SPEC-004 INV-CBP-01, plan l.381/l.689]  [PROPOSTA]

RULE-CKG-007: A confiança de relação é escala PRÓPRIA do KG e NÃO é a Convicção; custo e confiança nunca chegam ao nó
              `conviction`. INV-04 cobre o CUSTO; a extensão à CONFIANÇA é LOCAL. Que a SPEC-003 não consuma a
              confiança = requisito endereçado a ela / [DECISÃO NECESSÁRIA]. → D4.12
              [Fonte: INV-04 (atomic-spec l.404); CCM-001; CEE-001 l.111]  [PROPOSTA]

RULE-CKG-008: Toda CAUSA DEVE declarar mecanismo, direção, condições, regime e `posthoc_flag` explícito; toda SIMILAR_A
              DEVE declarar base de similaridade; o gate verifica PRESENÇA; o juízo tem bounded loop. → D4.10, D4.11
              [Fonte: RULE-CAU-01/02/03 (l.681-683); RULE-INQ-03 (l.678); atomic-spec §10.6 l.315]  [PROPOSTA]

RULE-CKG-009: A escrita no KG é GOVERNADA e E3, fail-closed: registro de conhecimento (`kg_record`) só de escritor da
              allowlist com identidade autenticada (→ D4.20); registro de decisão (`kg_gate_decision`) só da identidade
              de serviço autenticada dos gates do KG (→ D4.5); produtor NÃO redefine ontologia/taxonomia.
              [Fonte: SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04]  [PROPOSTA]

RULE-CKG-010: PORTA DE ADMISSÃO ÚNICA: um registro de conhecimento só é admissível sob contrato de admissão homologado
              aplicável a ele; sem contrato, DENY e nada persistido. Na v1.0 não há contrato (emendas futuras). O KG
              não forma, extrai nem recupera conhecimento. → D4.15
              [Fonte: DHR-SPEC006-002 D1; ROADMAP §6/§7; ENF-04]  [PROPOSTA]

RULE-CKG-011: O KG DEVE oferecer consulta read-only e Cognitive Trace Reconstruction COMPLETA; a completude é obrigação
              (não rebaixada por H-001); a consulta é opcional/não-bloqueante. → D4.8
              [Fonte: CEM-001 l.608-615; SAS-001 §6.12/l.163]  [PROPOSTA]

RULE-CKG-012: O estado de nó/relação é PROJEÇÃO DERIVADA dos registros; correção/reativação = novo registro; nenhuma
              transição remove registro. → D4.7, D4.4
              [Fonte: CHM-001; INV-07; SPEC-004 INV-CBP-01]  [PROPOSTA]

RULE-CKG-013: O KG DETECTA e REGISTRA colisões entre relações contraditórias, na mesma unidade atômica da admissão,
              preservando ambas; a resolução é de SPEC-007/SPEC-018 ou governança. → D4.13, D4.18, §D2.2
              [Fonte: INV-07; research.md §8]  [PROPOSTA]
```

### D2.1 — Matriz de integridade da ontologia (dados de D4.1) [PROPOSTA]

> **Atributo `school`:** NÃO é campo canônico nem campo de submissão; é atributo LOCAL [PROPOSTA] **derivado** pelo KG do `producer_id` declarado (D4.14), que espelha a proveniência canônica (CHM-001 l.361; CEM-001 l.276-278). `school` ∈ {Elliott, Fibonacci, Fractal, SMC, ICT} (5 camadas — CC-01). Só o `producer_id` do Elliott é conhecido (`elliott_specialist`, SPEC-001 l.203); os de SMC/Fibonacci/ICT ficam com as Specs dos especialistas e o produtor → Fractal não existe (AGENTS.md §3.2) — **[DECISÃO NECESSÁRIA]**. `school` ≠ `Domain` do CEM-001 (l.290-301). **Limite:** o KG verifica o `producer_id` declarado, sem lookup ao canônico — espelho de FORMA de INV-02. "Família estrutural" = nós de mesma `school` que `PERTENCE_A` o mesmo par (asset, timeframe); restringe só herança fractal intra-escola; HERDA entre escolas (SMC/Fibonacci SUB → Elliott PRIMARY) é normal (SPEC-001 RULE-HH-003 l.104; CHM-001 l.165/415; CONSTITUTION l.193).

| Relação | Origem (node_type) | Destino | Simétrica (consulta) |
|---|---|---|---|
| CONFIRMA | evidence (não observation — INV-06; CONSTITUTION l.191-192) | hypothesis | não |
| REFUTA | evidence (não observation) | hypothesis | não |
| DEPENDE_DE | hypothesis, mission | hypothesis, evidence | não |
| HERDA | hypothesis (`hierarchy_role=SUB`) | hypothesis (`hierarchy_role=PRIMARY`), via `parent_id`/`parent_hypothesis_id`; entre escolas permitido | não |
| PERTENCE_A | hypothesis, evidence, structure, observation | asset, timeframe, regime, mission | não |
| INVALIDA | evidence, learning | nó `evidence` (`to_node`) ou relação-alvo por `target_relation_id` (`to_node = null`) — afirmação sobre o alvo; não altera a validade do alvo; não é par de colisão | não |
| ORIGINA | structure ou hypothesis — **em ambos os casos com `school ≠ ICT`** (r8-j) | hypothesis | não |
| DERIVA_DE | evidence com `evidence_origin_type=DERIVED` | evidence **pertencente ao `Lineage` da origem** (destino fora do `Lineage` viola a linha — T19 (g)) | não — aresta de Lineage; base do trace (D4.8); só materializada pelo KG (D4.15/D4.17) |
| SIMILAR_A | qualquer | mesmo node_type, outro nó | **sim** (D4.10) |
| CAUSA | qualquer | qualquer | não (D4.10) |
| HIERARQUIA_DE | structure, timeframe | structure, timeframe | não |
| ESTATISTICA_DE | learning | hypothesis, structure, asset | não |

> Todas as relações são armazenadas direcionadas. Restrição transversal: nenhuma relação com destino `conviction` a partir de outro node_type, e nenhuma `relation_confidence` em relação com extremidade `conviction` (D4.12 (ii)/(iii) — r8-i). `DERIVA_DE` (aresta navegável) ≠ `provenance_ref.lineage` (campo de proveniência do registro); coexistem.

> **INV-CKG-01 (Memória permanente imutável) [PROPOSTA]:** nenhum registro do KG — `kg_record` ou `kg_gate_decision` — é deletado ou mutado; estado = projeção; "esquecimento" = arquivamento versionado; todo registro de conhecimento usa o envelope único. Reforça RULE-BB-004, INV-07 e SPEC-004 INV-CBP-01 no eixo permanente. (D4.3/D4.5/D4.7)

> **INV-CKG-02 (Completude e aciclicidade da linhagem) [PROPOSTA]:** evidência DERIVED só é admissível com uma aresta `DERIVA_DE` para cada ancestral do `Lineage`, todos já no KG; nenhuma `DERIVA_DE` aponta para fora do `Lineage` (D4.1/D4.17); o grafo de `DERIVA_DE` é acíclico; o trace ignora validade. Torna **verificável por predicado**, independente de H-001, a completude exigida por CEM-001 l.612-614 **sobre o que for admitido**; não garante que algo seja admitido (E-a — r8-h). (D4.17/D4.8)

### D2.2 — Tabela de contradição (dados de D4.13) [PROPOSTA]

| Tipo A | Tipo B (contradiz A) | Simétrico? |
|---|---|---|
| CONFIRMA | REFUTA | sim |

> Pares não listados não são contradição estrutural (INVALIDA × relação-alvo não é par). Tabela extensível só por governança (RULE-ONT-02).

---

## Critérios de Aceitação (EARS)

> **Leitura (r8-a):** cada critério enuncia o desfecho do seu predicado **avaliado isoladamente** (convenção D7 (i)). Numa operação completa vale a classe e a ordem de **D4.0**: o primeiro predicado reprovado define o código. **Na v1.0, toda operação SUBMETER termina no EARS 10** (`ADMISSION_CONTRACT_UNDEFINED`, passo 2), qualquer que seja o defeito adicional da entrada; os demais critérios de submissão são verificáveis só como predicado ou sobre fixture.

1. Quando um nó ou relação é submetido, o KG DEVE aplicar D4.1, D4.14 e D4.19 e rejeitar a violação com o código ali definido, sem escrever.
2. Quando um nó corresponde a objeto canônico, o KG DEVE referenciá-lo por ID+versão (D4.16) e NÃO DEVE redefinir seu contrato; quando um objeto de Skill é submetido como `evidence`, o KG DEVE rejeitá-lo (D4.1).
3. Quando uma relação é submetida, o KG DEVE exigir tipo do catálogo, direção e proveniência (D4.1/D4.2), e NÃO DEVE tratar a simetria de SIMILAR_A como ausência de direção.
4. Quando a validade de um nó ou relação muda por ato autorizado, o KG DEVE gravar um novo registro `invalidation` (D4.6) e NÃO DEVE mutar nem deletar o registro existente.
5. Quando qualquer registro de conhecimento é avaliado, o KG DEVE aplicar D4.2 e rejeitá-lo com o código ali definido se faltar proveniência exigível ou se os discriminantes forem inconsistentes.
6. Quando um "esquecimento" é solicitado, o KG DEVE arquivar por novo registro versionado (D4.7), e quando qualquer DELETE ou UPDATE de `kg_record` ou `kg_gate_decision` é tentado, o KG DEVE negá-lo com `RECORD_MUTATION_FORBIDDEN` antes de qualquer outro predicado (classe MUTAR — D4.0/D4.3) e registrar a negação no log (D4.5).
7. Quando um nó `conviction` ou relação com destino `conviction` é submetido, o KG DEVE aplicar D4.12 e rejeitar a violação sem escrever.
8. Quando uma relação CAUSA ou SIMILAR_A é submetida, de qualquer produtor, o KG DEVE aplicar D4.10, e quando a proposta vem de juízo, o KG DEVE aplicar D4.11 (no máximo uma invocação por submissão, sem re-tentativa, desfecho INDETERMINADO se reprovada).
9. Quando um registro de conhecimento é submetido, o KG DEVE aceitá-lo somente de escritor autorizado e autenticado segundo D4.20 (E3), e NÃO DEVE permitir que o produtor altere ontologia/taxonomia.
10. Quando qualquer registro de conhecimento é submetido sem contrato de admissão homologado aplicável a ele, o KG DEVE rejeitá-lo com `ADMISSION_CONTRACT_UNDEFINED` (D4.15), sem persistir nada.
11. Quando um consumidor consulta o KG, o KG DEVE responder read-only e devolver o trace completo (D4.8), sem criar nem alterar registro algum (nem `kg_record` nem `kg_gate_decision`); e quando uma operação de consulta tenta gravar, o KG DEVE negá-la com `QUERY_WRITE_FORBIDDEN` (classe CONSULTAR — D4.0) e registrar a negação no log (D4.5).
12. Quando um nó ou relação transita (SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED), o KG DEVE representar a transição por novo registro (D4.4/D4.7) e NÃO DEVE remover nem mutar a versão anterior.
13. Quando uma relação em admissão e uma relação vigente satisfazem `colide` (D4.13), o KG DEVE gravar um registro `collision` na mesma unidade atômica (D4.18), preservando ambas, e NÃO DEVE deixar `collision` gravado se a unidade falhar.
14. Quando, em registro de qualquer `record_kind`, um campo exigido por D4.19 está ausente, ou um campo proibido por D4.19 está presente, o KG DEVE rejeitar com `FIELD_PRESENCE_VIOLATION`, sem persistir nada.
15. Quando um nó hypothesis ou structure é submetido com `producer_id` sem mapeamento para `school`, o KG DEVE rejeitá-lo com `SCHOOL_UNDERIVABLE` (D4.14), sem persistir nada.
16. Quando uma evidência DERIVED é submetida com ancestral do `Lineage` ausente do KG, o KG DEVE rejeitá-la com `ANCESTOR_NOT_ADMITTED` (D4.17), sem estado de espera.
17. Quando um nó canônico ou transição canônica é submetido sem o elo de versão exigido por D4.16, ou com elo que não resolve no KG, o KG DEVE rejeitá-lo com `VERSION_LINK_MISSING`.
18. Quando uma `canonical_state_transition` é submetida fora do grafo canônico ou com `status_from` diferente do status corrente, o KG DEVE rejeitá-la com `CANONICAL_TRANSITION_ILLEGAL` (D4.16).
19. Quando um registro `invalidation` é submetido com `valid_to` anterior ao `valid_from` do alvo, ou uma `creation` com `valid_to ≤ valid_from`, o KG DEVE rejeitá-lo com `VALIDITY_WINDOW_INVALID` (D4.3).
20. Quando um registro é submetido com `version`, `supersedes` ou `recorded_at` em desacordo com D4.4, o KG DEVE rejeitá-lo com `RECORD_VERSION_INVALID`.
21. Quando o registro de decisão de uma submissão não pode ser anexado ao log pela identidade de serviço autenticada (D4.5), o KG NÃO DEVE gravar nenhum registro de conhecimento dessa submissão, e quando qualquer operação externa tenta anexar ao log, o KG DEVE negar com `LOG_WRITER_UNAUTHORIZED` (classe ANEXAR_LOG — D4.0).
22. Quando uma operação de alteração do catálogo de ontologia/taxonomia é solicitada em runtime, o KG DEVE negá-la com `ONTOLOGY_CHANGE_NOT_GOVERNED` (classe ALTERAR_CATÁLOGO — D4.0/D4.20) e registrar a negação no log.
23. Quando um registro derivado da unidade (`collision` ou `DERIVA_DE` materializada) tem `gate_record` que não resolve segundo D4.2, o KG DEVE rejeitar a unidade inteira com `GATE_RECORD_UNRESOLVED` (passo 11), sem gravar nenhum registro de conhecimento.
24. Quando uma submissão é duplicata segundo D4.9 ou D4.10, o KG DEVE encerrá-la com o desfecho `NO_OP` (`DUPLICATE_NO_OP`), sem gravar registro de conhecimento, e registrar a decisão no log.

---

## D3 — Comportamento (BASpecs) — com Classe/Mecanismo (CC-11)

> D = determinístico; C = constitutivo (é o gate); H = híbrido (juízo + gate de saída + bounded loop). A escrita no KG permanente é **E3** (atomic-spec §10.2 l.238); consulta é E1. O ENTÃO cita o item de D4 (fonte única); a ordem de avaliação e a precedência de códigos são D4.0.

### BASpec-CKG-001 — Ontologia enxuta + matriz de integridade
```
BASpec-CKG-001:
  QUANDO:       Um nó ou relação é submetido para escrita no KG
  ENTÃO:        O KG aplica D4.19, D4.1 e D4.14 (nessa ordem — D4.0) e rejeita a violação sem escrever; apenas ESPELHA
                os vínculos criados pelos agentes, sem decidir autoridade de criação (CC-01)
  PORQUE:       Sem gramática enxuta + integridade, a memória permanente acumula conhecimento incoerente (research.md §8)
  REFERÊNCIA:   RULE-CKG-001; D4.1/D4.14/D4.19; INV-02; RULE-HH-002/003/004 (SPEC-001); CONSTITUTION l.193
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico D4.19 ∧ D4.1 ∧ D4.14
    GATE DE SAÍDA: o próprio predicado
    CRITÉRIO 4Es: Conformidade > Eficácia — coerência da ontologia é inviolável
  VERIFICADO POR:
    DADO        (= T01) relação ORIGINA cuja origem é um nó structure com producer_id mapeado para ICT (mapeamento
                presumido — convenção D7 (v)) e cujo destino é hypothesis; predicado isolado (convenção D7 (i))
    QUANDO      o gate de integridade roda
    ENTÃO       rejeitada; nada persistido
    VERIFICAÇÃO written == false; rejected_reason == "ONTOLOGY_INTEGRITY_VIOLATION"
```

### BASpec-CKG-002 — Entidade por referência ao canônico (não redefine; observation ≠ evidence)
```
BASpec-CKG-002:
  QUANDO:       Um nó corresponde a objeto canônico (hypothesis/evidence/conviction), ou um objeto de Skill é submetido
  ENTÃO:        O KG referencia o canônico por ID+versão, mantém `canonical_status` e registros `canonical_state_transition`
                sob D4.16; NÃO redefine contrato/campos; objeto de Skill rotulado `evidence` é rejeitado (D4.1)
  PORQUE:       Redefinir canônico viola CC-02/CONST-01; o Status é o único campo mutável do canônico (CEM-001 l.264), logo
                o KG precisa de snapshot + transições para preservar estados; Observação ≠ Evidência (INV-06)
  REFERÊNCIA:   RULE-CKG-002; D4.1/D4.16; CEM-001 l.264/l.271-275/l.428/l.450; CHM-001 l.283/l.588/l.744-757; CCM-001 l.58
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : referência canonical_id@version + D4.16 + D4.1
    CRITÉRIO 4Es: Eficácia — integridade referencial e preservação dos estados canônicos admitidos
  VERIFICADO POR:
    DADO        nó node_type=evidence com producer_type fora de {AGENT, ENGINE} (objeto de Skill)
    QUANDO      o gate de integridade roda
    ENTÃO       rejeitado
    VERIFICAÇÃO written == false; rejected_reason == "OBSERVATION_IS_NOT_EVIDENCE"
```

### BASpec-CKG-003 — Relação tipada, direcionada, com proveniência e linhagem completa
```
BASpec-CKG-003:
  QUANDO:       Uma relação é submetida, ou uma evidência DERIVED é admitida
  ENTÃO:        O KG exige tipo do catálogo e direção (D4.1) e proveniência (D4.2); para evidência DERIVED materializa uma
                DERIVA_DE por ancestral do Lineage (D4.17); contradição segue CKG-013
  PORQUE:       Relação sem tipo/direção/proveniência não é auditável (P13); sem a aresta por ancestral o trace completo
                (CEM-001 l.612-614) não é garantido
  REFERÊNCIA:   RULE-CKG-003; D4.1/D4.2/D4.17; INV-CKG-02; CEM-001 l.565
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : validação D4.1 ∧ D4.2 ∧ D4.17
    CRITÉRIO 4Es: Eficácia — relações auditáveis e navegáveis
  VERIFICADO POR:
    DADO        (= T03) relação com relation_type fora do catálogo
    QUANDO      a validação roda
    ENTÃO       rejeitada; nada escrito
    VERIFICAÇÃO relation_written == false; rejected_reason == "RELATION_TYPE_INVALID"
```

### BASpec-CKG-004 — Temporalidade bitemporal (invalidar por novo registro)
```
BASpec-CKG-004:
  QUANDO:       Um ato autorizado determina que a validade de um nó/relação mudou (nunca cascata automática — CEM-001 l.602)
  ENTÃO:        O KG grava um novo registro `invalidation` (D4.6; janela D4.3), preserva o registro de criação intacto e
                responde por valid-time e transaction-time (D4.6)
  PORQUE:       Invalidar por novo registro preserva a reconstrução histórica (INV-07); "invalidação não implica cascata"
  REFERÊNCIA:   RULE-CKG-004; D4.3/D4.6; INV-07; SPEC-004 INV-CBP-01; CEM-001 l.602/l.503
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : novo registro de invalidação; validade por projeção D4.6
    CRITÉRIO 4Es: Eficácia — nenhuma verdade histórica perdida nem reescrita
  VERIFICADO POR:
    DADO        (fixture) relação R0 válida desde T0; registro invalidation R1 com target_record_ref=R0 e valid_to=T1
    QUANDO      consulta-se a validade em T0 e "agora"
    ENTÃO       R0 intacto; válida em T0; não válida agora
    VERIFICAÇÃO existing_record_mutated == false; existing_record_deleted == false; historical_query_consistent == true
```

### BASpec-CKG-005 — Proveniência exigível
```
BASpec-CKG-005:
  QUANDO:       Qualquer registro de conhecimento é avaliado
  ENTÃO:        O KG aplica D4.2; falta do exigível ou discriminante inconsistente ⇒ rejeitado com o código de D4.2
  PORQUE:       Conhecimento sem origem autenticada não é reconstruível (CEM-001 Cap.5; P13); exigir gate_record/lineage de
                quem não tem gate/ancestral fabricaria dado (RULE-MET-01)
  REFERÊNCIA:   RULE-CKG-005; D4.2; SPEC-004 RULE-CBP-007/014; CEM-001 l.280-283/l.351-355
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico D4.2
    GATE DE SAÍDA: o próprio predicado
    CRITÉRIO 4Es: Conformidade > Eficácia — identidade autenticada inviolável; sem fabricar proveniência
  VERIFICADO POR:
    DADO        (a) (= T12) hypothesis PRIMARY com computed_by, produced_by_gate=false, lineage=[]; (b) (= T14) sem computed_by
    QUANDO      o predicado D4.2 roda
    ENTÃO       (a) aprova sem exigir gate_record nem lineage; (b) reprova
    VERIFICAÇÃO case_a == PASS; case_a_gate_record_required == false; case_b == FAIL; case_b_reason == "COMPUTED_BY_MISSING"
```

### BASpec-CKG-006 — Imutabilidade / append-only (conhecimento e log) [INV-CKG-01]
```
BASpec-CKG-006:
  QUANDO:       Uma deleção ou mutação de `kg_record` ou de `kg_gate_decision` é tentada (inclusive como "esquecimento")
  ENTÃO:        O KG nega com RECORD_MUTATION_FORBIDDEN antes de qualquer outro predicado (classe MUTAR — D4.0; D4.3);
                a negação é nova decisão no log (D4.5); "esquecimento" só por arquivamento (D4.7)
  PORQUE:       A memória permanente nunca apaga nem reescreve (INV-07/RULE-BB-004/INV-CBP-01); o log é a EVIDENCE dos EC
                E3 (ENF-07) — mutá-lo apagaria a prova de conformidade
  REFERÊNCIA:   RULE-CKG-006; D4.3/D4.4/D4.5; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico — só APPEND (D4.3)
    GATE DE SAÍDA: o próprio predicado
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de histórico acima de economia de espaço
  VERIFICADO POR:
    DADO        (= T05) (a) DELETE físico de registro arquivado; (b) UPDATE do campo `result` de um kg_gate_decision
    QUANDO      o gate roda
    ENTÃO       ambas negadas; registros íntegros
    VERIFICAÇÃO reason(a) == reason(b) == "RECORD_MUTATION_FORBIDDEN"; record_mutated == false; gate_decision_mutated == false
```

### BASpec-CKG-007 — Confiança de relação ≠ Convicção; custo e confiança fora do nó `conviction`
```
BASpec-CKG-007:
  QUANDO:       Um nó `conviction`, uma relação com destino `conviction` ou uma confiança de relação é submetido
  ENTÃO:        O KG aplica D4.12 e rejeita a violação
  PORQUE:       INV-04 proíbe CUSTO no Conviction Vector; a extensão à confiança é regra LOCAL [PROPOSTA]
  REFERÊNCIA:   RULE-CKG-007; D4.12; INV-04 (custo); CCM-001
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : guard determinístico D4.12 (por campo/node_type; sem juízo)
    GATE DE SAÍDA: o próprio predicado
    CRITÉRIO 4Es: Conformidade > Eficácia — INV-04 inviolável
  VERIFICADO POR:
    DADO        (a) CAUSA(calibration_metric → conviction); (b) nó conviction com campo além da allowlist de D4.12
    QUANDO      o guard roda
    ENTÃO       (a) e (b) rejeitados
    VERIFICAÇÃO reason(a) == "ONTOLOGY_INTEGRITY_VIOLATION"; reason(b) == "CONFIDENCE_IS_NOT_CONVICTION"
```

### BASpec-CKG-008 — Causalidade e similaridade (RULE-CAU-01/02/03)
```
BASpec-CKG-008:
  QUANDO:       Uma relação CAUSA ou SIMILAR_A é submetida (qualquer produtor), eventualmente proposta por juízo
  ENTÃO:        O KG aplica D4.10 (presença) e, se há juízo, D4.11 (bounded loop)
  PORQUE:       Correlação não é causalidade (RULE-CAU-01); causa muda entre regimes (RULE-CAU-02); explicação pós-resultado
                é viés se não marcada (RULE-CAU-03); investigação sem encerramento é proibida (RULE-INQ-03)
  REFERÊNCIA:   RULE-CKG-008; D4.10/D4.11; RULE-CAU-01/02/03; RULE-INQ-03; atomic-spec §10.6 l.315
  CLASSE/MECANISMO:
    CLASSE      : H (Híbrido)
    MECANISMO   : juízo (apoio semântico) só PROPÕE; gate de saída determinístico D4.10
    BOUNDED LOOP: D4.11 — ≤1 invocação por submissão; sem retry; reprovada ⇒ INDETERMINADO; host pendente ⇒ 0 invocações
    GATE DE SAÍDA: D4.10
    CRITÉRIO 4Es: Eficácia (causalidade válida) > Eficiência; LLM é detector, nunca gate (ENF-03)
  VERIFICADO POR:
    DADO        (= T07) CAUSA proposta pelo juízo sem mechanism/regime
    QUANDO      o gate de saída roda
    ENTÃO       rejeitada; sem re-tentativa; desfecho INDETERMINADO
    VERIFICAÇÃO causal_written == false; rejected_reason == "CAUSAL_FIELDS_MISSING"; judgment_invocations_per_submission <= 1;
                kg_generated_retries == 0; proposal_outcome == "INDETERMINADO"
```

### BASpec-CKG-009 — Governança de escrita E3 (conhecimento e log) [E3]
```
BASpec-CKG-009:
  QUANDO:       Um registro de conhecimento é submetido, um registro de decisão é anexado ao log, ou uma alteração do
                catálogo de ontologia/taxonomia é solicitada
  ENTÃO:        Conhecimento: o KG aplica D4.20 (i)/(ii) (allowlist definida e disjunta da identidade de serviço; escritor
                autenticado). Log: o KG aplica D4.5 (só o pipeline de gates, sob a identidade de serviço autenticada, anexa;
                operação externa ANEXAR_LOG negada). Catálogo: D4.20 (iii) (classe ALTERAR_CATÁLOGO negada na v1.0)
  PORQUE:       Escrita em memória permanente é commit crítico/irreversível (E3 — atomic-spec §10.2); autorização não pode
                vir do payload nem falhar-aberto; um PASS forjado no log daria proveniência falsa a uma colisão
  REFERÊNCIA:   RULE-CKG-009; D4.5/D4.20; SAS-001 §6.12; SPEC-004 RULE-CBP-014 (plan l.338); ENF-03/04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate E3 por identidade autenticada (runtime, não payload); LLM não é gate
    GATE DE SAÍDA: D4.20 / D4.5
    CRITÉRIO 4Es: Conformidade > Eficácia — escrita só sob autorização (ENF-04)
  VERIFICADO POR:
    DADO        (a) (= T08) escrita de conhecimento com a autenticação indisponível (allowlist de fixture — D7 (v));
                (b) escritor da allowlist de conhecimento tenta anexar kg_gate_decision{result=PASS}
    QUANDO      o gate E3 roda
    ENTÃO       ambas negadas (fail-closed)
    VERIFICAÇÃO reason(a) == "WRITER_UNAUTHORIZED"; reason(b) == "LOG_WRITER_UNAUTHORIZED"; written == false
```

### BASpec-CKG-010 — Porta de admissão única (nega por padrão)
```
BASpec-CKG-010:
  QUANDO:       Qualquer registro de conhecimento (`kg_record`, qualquer record_kind, qualquer origem) é submetido
  ENTÃO:        O KG aplica D4.15: sem contrato de admissão homologado aplicável ⇒ DENY `ADMISSION_CONTRACT_UNDEFINED`;
                nada persistido; decisão no log. Na v1.0 nenhum contrato existe. O KG não forma/extrai/recupera
  PORQUE:       "Documento recuperado ≠ conhecimento validado"; admitir sem contrato contaminaria a memória permanente (E3
                irreversível); os contratos por caminho dependem de decisões de Andraus (emendas E-a..E-e)
  REFERÊNCIA:   RULE-CKG-010; D4.15; DHR-SPEC006-002 D1; ENF-04
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : gate determinístico D4.15 (primeiro na ordem — D4.0)
    GATE DE SAÍDA: o próprio predicado
    CRITÉRIO 4Es: Conformidade > Eficácia — não contaminar; o custo (nenhuma admissão na v1.0) é declarado
  VERIFICADO POR:
    DADO        (= T09) (i) hypothesis canônica; (ii) learning com selo declarado; (iii) CAUSA registrada por produtor;
                (iv) nó asset; (v) invalidation sobre sujeito de fixture
    QUANDO      o gate de admissão roda
    ENTÃO       todos rejeitados; nada persistido
    VERIFICAÇÃO reason(i..v) == "ADMISSION_CONTRACT_UNDEFINED"; written(i..v) == false; positive_admission_in_scope == false
```

### BASpec-CKG-011 — Consulta read-only + Cognitive Trace Reconstruction completa
```
BASpec-CKG-011:
  QUANDO:       Um consumidor consulta o KG ou pede o trace de uma evidência
  ENTÃO:        O KG responde read-only e devolve o trace D4.8 (fecho transitivo completo de DERIVA_DE, ignorando
                validade), sem gravar registro algum, nem no log; a completude não é rebaixada por H-001 (só a eficiência de
                consultas amplas é INDETERMINADA). Tentativa de gravar pela consulta = classe CONSULTAR negada (D4.0/D4.8),
                efeito governado por EC-CKG-003
  PORQUE:       Reconstrução completa é responsabilidade canônica do KG (CEM-001 l.562-565/l.699); consulta não muta
  REFERÊNCIA:   RULE-CKG-011; D4.8; INV-CKG-02; CEM-001 l.608-615; SAS-001 §6.12
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : travessia determinística D4.8; read-only
    CRITÉRIO 4Es: Eficácia (completude — obrigação) > Eficiência (consulta ampla = H-001)
  VERIFICADO POR:
    DADO        (= T10) fixture: E deriva de D; D de C; C de A e B
    QUANDO      pede-se o trace de E
    ENTÃO       fecho completo, em ordem de ancestralidade; nenhum registro criado
    VERIFICAÇÃO trace == ["A","B","C","D"]; trace_complete == true; records_created_by_query == 0 (kg_record e kg_gate_decision)
```

### BASpec-CKG-012 — Lifecycle (estado = projeção derivada)
```
BASpec-CKG-012:
  QUANDO:       Um nó/relação é corrigido, invalidado no tempo ou arquivado
  ENTÃO:        O KG grava novo registro (D4.4) e o estado é a projeção D4.7; nenhuma versão é removida/mutada
  PORQUE:       Conhecimento permanente/temporário se opera por lifecycle versionado (INV-07; INV-CBP-01)
  REFERÊNCIA:   RULE-CKG-012; D4.4/D4.7; CHM-001; INV-07
  CLASSE/MECANISMO:
    CLASSE      : D (Determinístico)
    MECANISMO   : transições append-only; projeção D4.7
    CRITÉRIO 4Es: Eficácia — reconstrução íntegra do histórico
  VERIFICADO POR:
    DADO        (= T13) fixture: creation v1 e creation v2 com supersedes→v1
    QUANDO      projeta-se o estado de v1
    ENTÃO       v1 íntegra; estado SUPERSEDED derivado
    VERIFICAÇÃO old_version_preserved == true; old_version_mutated == false; projected_state(v1) == "SUPERSEDED"
```

### BASpec-CKG-013 — Colisão (detecta e registra; não resolve em silêncio)
```
BASpec-CKG-013:
  QUANDO:       Uma relação em admissão e uma relação vigente satisfazem `colide` (D4.13)
  ENTÃO:        O KG grava UM registro `collision` (D4.13) na mesma unidade atômica da admissão (D4.18), com `gate_record`
                que resolve para a PASS de CKG-013 cujo `collision_pair` é o par (D4.2 — senão GATE_RECORD_UNRESOLVED);
                ambas preservadas; sem `colide`, nenhum collision (PASS de CKG-013 com collision_pair = null); a resolução
                da contradição é de SPEC-007/SPEC-018 ou governança
  PORQUE:       Preservar a contradição auditável respeita INV-07; a atomicidade evita collision com referência pendurada
  REFERÊNCIA:   RULE-CKG-013; §D2.2; D4.13/D4.18; INV-07; SPEC-004 plan l.381/l.689
  CLASSE/MECANISMO:
    CLASSE      : C (Constitutivo)
    MECANISMO   : detecção D4.13 + gravação atômica D4.18
    GATE DE SAÍDA: D4.13 ∧ D4.18
    CRITÉRIO 4Es: Conformidade > Eficácia — não-perda de conhecimento
  VERIFICADO POR:
    DADO        (= T11) CONFIRMA(A→B) vigente e REFUTA(A→B) com janela efetiva sobreposta (fixture — D7 (iv))
    QUANDO      detector e commit rodam
    ENTÃO       ambas preservadas; um collision gravado na unidade; seu gate_record resolve para a PASS de CKG-013 com
                o mesmo par; nenhuma apagada
    VERIFICAÇÃO both_relations_present == true; collisions_for_pair == 1; silent_overwrite == false;
                collision_gate_record_resolves == true; decision(gate_record).collision_pair == {relation_a_ref, relation_b_ref}
```

---

## D4 — Algoritmo (FONTE ÚNICA de predicados, obrigatoriedade, ordem e códigos)

Mecânicas determinísticas reais (atomic-spec §2). Mecanismo físico = **INDETERMINADO = H-001 (ABERTA)**; abaixo está a lógica, não a tecnologia. Todo item é [PROPOSTA].

- **D4.0 Classes de operação, ordem e precedência (fonte única; R8-1):** a interface do KG expõe **cinco operações** [PROPOSTA]. A **classe** é dada pela operação invocada (não pelo conteúdo do payload) e é determinada **antes de qualquer predicado**; as classes são mutuamente exclusivas e uma operação só é avaliada pelos predicados da sua classe (ex.: UPDATE vindo de identidade não autenticada ⇒ `RECORD_MUTATION_FORBIDDEN`, não `WRITER_UNAUTHORIZED`). Não há outra operação; a identidade de serviço não invoca operações — ela só executa o pipeline (D4.5).

| Classe | Predicado (único) | Desfecho | Log (D4.5) |
|---|---|---|---|
| **MUTAR** — DELETE ou UPDATE de `kg_record` ou `kg_gate_decision` | D4.3 (imutabilidade) | sempre DENY `RECORD_MUTATION_FORBIDDEN` | 1 DENY (`gate_id`=CKG-006) |
| **ALTERAR_CATÁLOGO** — alteração de §D2.1, §D2.2, `mapa_produtor` (D4.14) ou da `schema_version` vigente | D4.20 (iii) | na v1.0, sempre DENY `ONTOLOGY_CHANGE_NOT_GOVERNED` | 1 DENY (`gate_id`=CKG-009) |
| **ANEXAR_LOG** — append direto em `kg_gate_decision` por operação externa | D4.5 (escritor) | sempre DENY `LOG_WRITER_UNAUTHORIZED`, qualquer que seja a identidade | 1 DENY (`gate_id`=CKG-009) |
| **CONSULTAR** — leitura/trace | D4.8 | read-only: resposta; operação de consulta que tente gravar: DENY `QUERY_WRITE_FORBIDDEN` | read-only: **0 registros**; tentativa de gravação: 1 DENY (`gate_id`=CKG-011) |
| **SUBMETER** — append de `kg_record` | sequência abaixo | PASS (unidade D4.18) / DENY / INDETERMINADO / NO_OP | D4.5 (i)–(iv) |

  **Sequência SUBMETER:** (1) recebimento; (2) D4.15 admissão; (3) D4.20 (i)/(ii) autorização; (4) D4.19 → D4.1 → D4.14 → D4.12; (5) D4.2; (6) D4.17; (7) D4.16; (8) D4.10, e D4.11 se há juízo; (9) D4.9 (dedupe) → D4.3 → D4.4; (10) D4.13 (detecção, sem gravar); (11) D4.18 — montagem da unidade, validação dos registros derivados (D4.19 → D4.1 → D4.2 regime `kg_internal` → D4.3 → D4.4) e commit. **O primeiro predicado reprovado define o código**; os seguintes não são avaliados na sequência (cada um continua testável como predicado isolado — convenção D7 (i)). **NO_OP (r8-b):** desfecho não-rejeição, alcançado só no passo 8 (SIMILAR_A já vigente — D4.10) ou no início do passo 9 (reescrita idêntica — D4.9); encerra a sequência com `result=NO_OP`, `reason=DUPLICATE_NO_OP`, sem gravar conhecimento. Toda decisão vai ao log (D4.5). **Na v1.0 a sequência SUBMETER sempre termina no passo 2.**
- **D4.1 Integridade (CKG-001/002/003):** `node_type ∉ catálogo (§D2.1/S2) ⇒ ONTOLOGY_INTEGRITY_VIOLATION`; `relation_type ∉ catálogo ⇒ RELATION_TYPE_INVALID`; `(from.node_type, destino) ∉ matriz[relation_type]` ou restrição da linha violada ⇒ `ONTOLOGY_INTEGRITY_VIOLATION`; `node_type=evidence ∧ producer_type ∉ {AGENT, ENGINE}` ⇒ `OBSERVATION_IS_NOT_EVIDENCE` (Evidência é de Agente/Engine — CEM-001 l.271-275; Observação é de Skill — INV-06). Limite: verifica o valor declarado (forma).
- **D4.2 Proveniência (CKG-005):** `computed_by` ausente ⇒ `COMPUTED_BY_MISSING`; `produced_by_gate ∉ {true,false}` ⇒ `PROVENANCE_INCONSISTENT`; `produced_by_gate=true ∧ gate_record ausente` ⇒ `GATE_RECORD_MISSING`; `produced_by_gate=false ∧ gate_record presente` ⇒ `PROVENANCE_INCONSISTENT`. **Evidência:** `node_type=evidence ∧ evidence_origin_type ∉ {PRIMARY, DERIVED}` ⇒ `PROVENANCE_INCONSISTENT`; `node_type≠evidence ∧ evidence_origin_type presente` ⇒ `PROVENANCE_INCONSISTENT`; `PRIMARY ∧ producer_type≠AGENT` ou `DERIVED ∧ producer_type≠ENGINE` ⇒ `PROVENANCE_INCONSISTENT` ([FONTE] CEM-001 l.282-283); `DERIVED ∧ lineage=[]` ⇒ `LINEAGE_MISSING`; `PRIMARY ∧ lineage≠[]` ⇒ `PROVENANCE_INCONSISTENT` (CEM-001 l.354). Demais node_types e relações: `lineage` opcional. `computed_by`/`writer_id` vêm da autenticação do runtime, não do payload (SPEC-004 plan l.338). **`publication.origin` (r8-g)** é atribuído pelo KG, nunca pelo payload (presença na submissão = D4.19): `kg_internal` só para registro derivado; para registro submetido, o caminho do contrato aplicável (emenda — na v1.0 inexistente). **Registro derivado (`publication.origin = kg_internal`; D4.15 — R8-3/R8-4), avaliado no passo 11:** `computed_by = writer_id =` identidade de serviço; `produced_by_gate = true`; `lineage = []`; `gate_record` DEVE resolver para um `kg_gate_decision` **da mesma unidade** com `result = PASS ∧ writer_id = identidade de serviço ∧ submission_id = o da submissão em admissão ∧` — para `collision`: `gate_id = CKG-013 ∧ collision_pair = {relation_a_ref, relation_b_ref}`; para `DERIVA_DE` materializada: `gate_id = CKG-003` (D4.17) — senão `GATE_RECORD_UNRESOLVED` (a unidade inteira falha — D4.18). Uma PASS de CKG-013 com `collision_pair = null` (detector rodou, sem colisão) **nunca** resolve um `collision`. Os demais casos deste item valem também para o derivado (ex.: `produced_by_gate=true` sem `gate_record` ⇒ `GATE_RECORD_MISSING`). O `gate_record` de objeto a montante (registro submetido) é referência à SPEC-004 — sua resolução fica fora do KG (limite). **Limite:** verifica a CONSISTÊNCIA dos discriminantes declarados, não sua veracidade frente ao objeto a montante — um `produced_by_gate=false` declarado falsamente por quem passou por gate não é detectável aqui (ENF-03); a coincidência com o canônico é matéria da emenda E-a.
- **D4.3 Envelope e imutabilidade (CKG-004/006/013):** `envelope_completo(r) = record_id ∧ record_kind ∈ {creation, invalidation, archival, canonical_state_transition, collision} ∧ subject_kind ∧ subject_id ∧ version ∧ supersedes declarado (valor ou null) ∧ schema_version ∧ writer_id ∧ recorded_at ∧ publication.origin (atribuído pelo KG — D4.2) ∧ (creation ⇒ valid_from) ∧ (invalidation ⇒ valid_to) ∧ (record_kind ∈ {invalidation, archival, canonical_state_transition} ⇒ target_record_ref resolve) ∧ (collision ⇒ relation_a_ref ∧ relation_b_ref resolvem)`; senão `RECORD_ENVELOPE_INCOMPLETE`. **`provenance_ref` não é avaliado aqui** — só em D4.2, antes (passo 5), de modo que cada campo ausente tem UM código (r7-b). Janela: `invalidation.valid_to < alvo.valid_from` ⇒ `VALIDITY_WINDOW_INVALID`; `creation` com `valid_to` declarado (janela temporária — S14) e `valid_to ≤ valid_from` ⇒ `VALIDITY_WINDOW_INVALID` (r8-c). **Imutabilidade:** sobre `kg_record` e `kg_gate_decision` a única operação é APPEND; `DELETE` ou `UPDATE` de registro (classe MUTAR — D4.0) ⇒ `RECORD_MUTATION_FORBIDDEN` (decisão registrada). **Limite (m3/r7-g):** sem digest/hash encadeado — a regra proíbe a mutação in-place, não a detecta fisicamente (detecção = H-001/BUILD).
- **D4.4 Versão/sucessão de todo `record_kind`:** `subject_id` de invalidation/archival/canonical_state_transition = o do sujeito-alvo; `version(r) = 1 + max(version dos registros já gravados do sujeito)` (1 se nenhum); `recorded_at(r) ≥ recorded_at` do registro `version(r)−1` do sujeito; **`creation` (r8-c):** `supersedes = null` sse é a 1ª creation do sujeito; toda creation seguinte do mesmo sujeito (reescrita divergente — D4.9) DEVE ter `supersedes` = `record_id` da creation mais recente do sujeito (por `version`) — creation seguinte com `supersedes = null` ou apontando outra ⇒ violação. **`invalidation`:** `supersedes` ≠ null só quando corrige invalidação anterior do mesmo alvo (→ essa invalidação). Demais `record_kind`: `supersedes = null`. Collision: sujeito próprio, `version=1`. Violação ⇒ `RECORD_VERSION_INVALID`. Replay: registros do sujeito ordenados por `version`.
- **D4.5 Log `kg_gate_decision` (R7-1):** campos no schema; `decision_id` único e imutável; append-only (D4.3). **Escritor único:** só o pipeline de gates do KG anexa, sob a identidade de serviço autenticada pelo runtime (reuso por referência da autenticação de SPEC-004 RULE-CBP-014 — [PROPOSTA]); toda operação externa de append (classe ANEXAR_LOG — D4.0), de qualquer identidade, inclusive escritor da allowlist de conhecimento ⇒ `LOG_WRITER_UNAUTHORIZED` (a negação é registrada pela identidade de serviço). **Separação de funções (r8-d):** a identidade de serviço não pertence à allowlist de conhecimento (D4.20 (ii)). **Ordem e falha:** (i) submissão aprovada nos passos 2–10: as decisões PASS dessa submissão integram a unidade atômica D4.18 — conhecimento e decisões são gravados juntos ou nenhum (espelha SPEC-004 plan l.381: sem "publicação sem registro de auditoria"); (ii) submissão reprovada, INDETERMINADO ou unidade D4.18 falha: a única escrita é a decisão (DENY/INDETERMINADO, com o código); se esse append falha, nada de conhecimento é gravado de qualquer modo, e a ausência do registro é limite declarado (observabilidade de falha de log = H-001/BUILD); (iii) identidade de serviço não autenticável ⇒ nenhum log e, por (i), nenhum commit de conhecimento (fail-closed); (iv) **completude (r8-e):** toda operação, exceto CONSULTAR read-only, gera decisão — DENY, INDETERMINADO ou NO_OP ⇒ exatamente **uma** decisão terminal; SUBMETER aprovada ⇒ uma PASS por BASpec-gate avaliado nos passos 2–10 e, para CKG-013, uma PASS **por par detectado** com `collision_pair` = o par, ou uma única PASS com `collision_pair = null` se não houve colisão; as derivações materializadas (D4.17) têm a PASS de CKG-003. **Entrada (r8-f):** toda decisão guarda `input_digest` e `input_snapshot` (cópia da operação recebida — dado de auditoria, NÃO conhecimento: não passa por D4.15, não é devolvido por D4.8 nem navegável como KG), de modo que a reexecução ENF-07 do gate é executável a partir do próprio log. **Volume (r8-e):** a v1.0 não descarta nem agrega decisões (descartar violaria a completude e INV-07); política de volume do log (limitação na origem, alertas — SPEC-040) = [DECISÃO NECESSÁRIA], nunca por deleção. **Resolução de `gate_record`:** predicado e código em D4.2 (`GATE_RECORD_UNRESOLVED`). **Escopo:** o log não é conhecimento — não passa por D4.15 nem D4.20 (por isso registra também os DENY). **Redução a `record_kind`, avaliada e rejeitada:** um DENY seria escrita de conhecimento sujeita aos gates que registra (circular com D4.15).
- **D4.6 Validade bitemporal (CKG-004):** criação `R0{creation, valid_from}`; mudança `R1{invalidation, target_record_ref=R0, valid_to}` — R0 nunca mutado; vale para nó e relação. Invalidações efetivas de `v` = as que miram `v` e não foram supersedidas; `valid_to_efetivo(v) = min(valid_to da creation de v, se declarado; valid_to das invalidações efetivas)`, ou `+∞` se nenhum (r8-c: a janela temporária da creation — S14 — entra na validade). **valid-time** `válida_em(v,T) = valid_from(v) ≤ T < valid_to_efetivo(v)`; **transaction-time** `conforme_registrado_em(R)` = a mesma função restrita aos registros com `recorded_at ≤ R`.
- **D4.7 Projeção de estado (CKG-006/012):** definida para `T ≥ valid_from(v)` (antes disso `v` não existe em valid-time): `estado(v,T) = ARCHIVED se ∃ archival com target_record_ref=v; senão SUPERSEDED se ∃ creation c' com c'.supersedes=v; senão INVALIDATED_IN_TIME se ¬válida_em(v,T); senão ACTIVE_KNOWLEDGE` — precedência fixa nessa ordem (archival é terminal para a versão; reativação = nova versão — análogo a CHM-001 l.767). `canonical_status(v)` = `status_to` da última `canonical_state_transition` do sujeito por `version` (ou o snapshot de criação) — trilha separada. Mesmos registros ⇒ mesmo estado em qualquer implementação conforme.
- **D4.8 Cognitive Trace Reconstruction (CKG-011):** `trace(x)` = fecho transitivo de `DERIVA_DE` a partir de `x`, completo (INV-CKG-02), ignorando validade (CEM-001 l.602); saída em ordem de ancestralidade (primários → derivados — CEM-001 l.567-577). Consulta read-only cria zero registros — nem `kg_record` nem `kg_gate_decision`; operação de consulta que tente gravar (classe CONSULTAR — D4.0) ⇒ `QUERY_WRITE_FORBIDDEN`, e **essa negação é registrada** (1 DENY): não contradiz o "zero registros", porque a operação deixou de ser read-only — o efeito negado é de escrita e é governado por EC-CKG-003 (E3). Eficiência de travessia ampla = H-001.
- **D4.9 Dedupe:** chave de nó = `(node_type, canonical_ref)` se canônico, `(node_type, natural_key)` se não; chave de relação = `(relation_type, from_node, to_node | target_relation_id, valid_from)`; chave de collision = par não-ordenado `{relation_a_ref, relation_b_ref}`. Avaliado no início do passo 9 (D4.0): reescrita idêntica (mesma chave e mesmo payload) ⇒ desfecho `NO_OP` (`DUPLICATE_NO_OP`), nada gravado, decisão no log (r8-b); divergente (mesma chave, payload diferente) = nova creation do mesmo sujeito com `supersedes` (D4.4) — nunca sobrescreve.
- **D4.10 Gate causal/similaridade (CKG-008; toda CAUSA/SIMILAR_A):** `CAUSA ⇒ mechanism, direction, conditions, regime ≠ ∅ ∧ posthoc_flag ∈ {true,false}` (ausência ≠ false); senão `CAUSAL_FIELDS_MISSING`. `SIMILAR_A ⇒ similarity_basis ≠ ∅` (senão `SIMILARITY_BASIS_MISSING`) `∧ from.node_type = to.node_type ∧ from ≠ to` (senão `ONTOLOGY_INTEGRITY_VIOLATION`); `∃ SIMILAR_A vigente entre {from,to} em qualquer direção ⇒ NO_OP (DUPLICATE_NO_OP; passo 8 — D4.0)`. Verifica PRESENÇA, não veracidade (ENF-03): `posthoc_flag=false` declarado falsamente não é detectável.
- **D4.11 Bounded loop do juízo (CKG-008):** por submissão, `invocações(juízo) ≤ 1`; se a proposta não passa D4.10 ⇒ desfecho `INDETERMINADO`, nada escrito, `judgment_invocations` no log; o KG nunca gera re-tentativa nem nova submissão; sem memoização (re-submissão de produtor = outra submissão, frequência fora do KG). Host do juízo pendente ([DECISÃO NECESSÁRIA]) ⇒ 0 invocações. Proposta aprovada é submissão de conhecimento sujeita a D4.15. Limite versionado com RULE-CKG-008 (alteração só por emenda spec-time). [FONTE: atomic-spec l.315; RULE-INQ-03]
- **D4.12 Guard de custo E confiança (CKG-007; INV-04):** (i) payload de nó `conviction` FECHADO — admite só `{node_type, canonical_ref, canonical_status, canonical_predecessor_ref}` (`additionalProperties:false`); qualquer outro campo (custo, confiança, score, `relation_confidence` ou outro) ⇒ `CONFIDENCE_IS_NOT_CONVICTION`. O elo de sucessora fica no payload de `canonical_state_transition`, não no nó (r7-i). (ii) relação de qualquer tipo com `to.node_type=conviction ∧ from.node_type≠conviction` ⇒ `ONTOLOGY_INTEGRITY_VIOLATION` (r8-i: cobre `calibration_metric`→`conviction` e qualquer outra origem, inclusive CAUSA, que a matriz admite com "qualquer"). (iii) `relation_confidence` só no payload de relação (escala = PARÂMETRO INDETERMINADO) e **proibida** em relação com extremidade `conviction` (`from` ou `to`) ⇒ `CONFIDENCE_IS_NOT_CONVICTION`. Limite: semântica de custo/confiança em texto livre de outros node_types não é detectada (ENF-03).
- **D4.13 Colisão (CKG-013; §D2.2):** `colide(r1,r2) sse (r1.type, r2.type) ∈ §D2.2 ∧ r1.from=r2.from ∧ r1.to=r2.to ∧ [valid_from(r1), valid_to_efetivo(r1)) ∩ [valid_from(r2), valid_to_efetivo(r2)) ≠ ∅`, avaliado com `conforme_registrado_em(recorded_at da admissão)` (D4.6). Detectado no passo 10 sem gravar; cada par detectado gera a PASS de CKG-013 com `collision_pair` (D4.5 (iv)); gravado só em D4.18. **Payload calculado pelo KG, não recebido:** `relation_a_ref` = creation vigente, `relation_b_ref` = creation em admissão, `contradiction_pair` = (tipo de a, tipo de b), `overlap_window` = a interseção como-registrada acima, `detected_at` = `recorded_at` da unidade; presença = D4.19. **Multiplicidade (r7-h):** exatamente um `collision` por par (chave D4.9); na admissão o par é sempre novo (a creation em admissão é nova; reescrita idêntica encerra em NO_OP no passo 9), logo a unicidade é propriedade auditada, não desfecho de submissão. **Auditoria (r7-h):** o replay reaplica `colide` a todo par de creations do histórico, cada um como-registrado no `recorded_at` da creation mais recente do par; o conjunto recomputado — e os valores de `contradiction_pair`/`overlap_window` — DEVEM igualar os `collision` gravados, e todo `gate_record` de `collision` DEVE resolver por D4.2 (T17).
- **D4.14 Regras de nó hypothesis/structure (CKG-001):** `school = mapa_produtor(producer_id)` (tabela [PROPOSTA] — §D2.1); sem mapeamento ⇒ `SCHOOL_UNDERIVABLE`; `node_type=hypothesis ∧ school=ICT` ⇒ `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN` (INV-02/RULE-HH-004); `hierarchy_role=PRIMARY ∧ school≠Elliott` ⇒ `ONTOLOGY_INTEGRITY_VIOLATION` (RULE-HH-002); `HERDA ∧ pai.hierarchy_role≠PRIMARY` ⇒ `ONTOLOGY_INTEGRITY_VIOLATION` (RULE-HH-003). A presença de `hierarchy_role` é garantida antes por D4.19 (sem bypass por ausência — R7-2).
- **D4.15 Admissão — regra única (CKG-010; R7-3):** `admissível(r) sse ∃ contrato de admissão homologado aplicável a r` (por caminho de entrada e `record_kind`). **Na v1.0 o conjunto de contratos é vazio** ⇒ todo `kg_record`, de qualquer `record_kind` e origem ⇒ `ADMISSION_CONTRACT_UNDEFINED`; nada persistido; decisão no log. Avaliado primeiro na classe SUBMETER (D4.0), logo este código prevalece sobre qualquer outro **dessa classe** (as classes MUTAR/ALTERAR_CATÁLOGO/ANEXAR_LOG/CONSULTAR têm predicado próprio — D4.0). Contratos entram só por emenda aditiva homologada ("Escopo em etapas"). **Registros derivados (R8-3):** `collision` (D4.13) e a `creation` de `DERIVA_DE` materializada (D4.17) — `publication.origin = kg_internal` — não são submissões: existem só dentro da unidade D4.18 de uma submissão que passou este predicado e **herdam a admissão e a autorização (D4.20) dessa submissão**, sem reavaliá-las; sua proveniência é D4.2 (regime `kg_internal`) e sua validação é o passo 11. `collision` ou `DERIVA_DE` submetidos de fora são SUBMETER comuns (na v1.0, `ADMISSION_CONTRACT_UNDEFINED`) e nenhum contrato futuro pode admiti-los [PROPOSTA].
- **D4.16 Elos de versão e legalidade canônica (CKG-002):** `canonical_model` fixo pelo node_type (hypothesis→CHM-001, evidence→CEM-001, conviction→CCM-001). **hypothesis:** `canonical_ref.version > 1 ⇒ canonical_predecessor_ref` exigido ([FONTE] CHM-001 l.588). **conviction:** idem ([INFERÊNCIA] de `previous_version_id`, CCM-001 l.58, + INV-07). **evidence:** `canonical_state_transition.status_to=SUPERSEDED ⇒ successor_ref` exigido ([FONTE] CEM-001 l.450); `canonical_predecessor_ref` opcional. `successor_ref` em CHM/CCM = opcional, [PROPOSTA] local. Todo elo presente DEVE resolver para nó já no KG; ausente-quando-exigido ou não resolvido ⇒ `VERSION_LINK_MISSING`. **Legalidade:** `canonical_model ∈ {CHM-001, CEM-001} ∧ (status_from, status_to) ∉ grafo canônico (CHM-001 l.744-757; CEM-001 l.460-466)` ⇒ `CANONICAL_TRANSITION_ILLEGAL`; `status_from ≠ canonical_status corrente` ⇒ idem; CCM-001: só `status_to ∈ enum` (sem tabela). Presença e domínio de `canonical_status` e dos campos de `canonical_state_transition` = D4.19 (r8-m: D4.16 não emite `FIELD_PRESENCE_VIOLATION`). **Limite:** transição perdida trava as seguintes do mesmo sujeito (fail-closed); reconciliação = emenda E-a.
- **D4.17 Ancestrais e aciclicidade (INV-CKG-02):** evidência `d` com `evidence_origin_type=DERIVED`: `∀a ∈ Lineage(d): a ∈ KG ⇒ DERIVA_DE(d→a)` materializada na unidade D4.18 como registro derivado (D4.15; `gate_record` = PASS de CKG-003 — D4.2); `∃a ∉ KG ⇒ ANCESTOR_NOT_ADMITTED` (sem estado de espera). `DERIVA_DE(d→x)` com `x ∉ Lineage(d)` viola a linha da matriz ⇒ `ONTOLOGY_INTEGRITY_VIOLATION` (D4.1; T19 (g) — r8-h). **Aciclicidade (r7-e):** toda aresta `DERIVA_DE` vai do nó em admissão para nó já admitido; logo a ordem de admissão é uma ordem topológica e nenhum ciclo é formável; auto-referência (`d ∈ Lineage(d)`) cai em `ANCESTOR_NOT_ADMITTED` porque `d` ainda não está no KG. [INFERÊNCIA — derivação do predicado, verificada em T19]
- **D4.18 Unidade atômica tudo-ou-nada (CKG-006/013) [espelha SPEC-004 plan l.381/l.689]:** após os passos 2–10 aprovarem, a unidade = registro submetido + registros derivados (`creation` de cada `DERIVA_DE` — D4.17; `collision` por par que `colide` — D4.13) + as decisões PASS da submissão (D4.5 (iv)). Validação (passo 11): o registro submetido já passou D4.3/D4.4 no passo 9 e é revalidado por D4.4 no commit (concorrência — T21); cada registro derivado passa D4.19 → D4.1 → D4.2 (regime `kg_internal`, inclusive `GATE_RECORD_UNRESOLVED`) → D4.3 → D4.4; D4.15 e D4.20 **não** são reavaliados para derivados (herdados — D4.15). Todos gravados juntos; se qualquer um falha, NENHUM é gravado (sem collision pendurado, sem PASS órfão) e a falha vai ao log como DENY com o código (D4.5 (ii)). Mecanismo físico da atomicidade = H-001/BUILD.
- **D4.19 Presença de campos de payload, em TODO `record_kind` (R7-2/R8-2 — única fonte de obrigatoriedade fora de D4.2/D4.3/D4.10/D4.12/D4.16):** todo payload é FECHADO aos campos do schema do seu par (`subject_kind`, `record_kind`) — campo desconhecido ⇒ violação; para `node_type=conviction`, D4.19 avalia as linhas `canonical_ref` e `canonical_status` — os demais campos são da allowlist de D4.12 (código próprio). Avaliado no passo 4 para o registro submetido e no passo 11 para os derivados (D4.0). Violação ⇒ `FIELD_PRESENCE_VIOLATION`. Um campo cuja exigência é **condicional a outro predicado** (ex.: `successor_ref` — D4.16; `causal` — D4.10) tem a condição e o código naquele item; aqui só a proibição de presença fora do contexto.

| Campo | Exigido sse | Proibido sse |
|---|---|---|
| **Nó (`creation`)** | | |
| `canonical_ref` | node_type ∈ {hypothesis, evidence, conviction} | node_type ∉ {hypothesis, evidence, conviction} |
| `canonical_status` ∈ enum do modelo de `node_type` (D4.16) | `canonical_ref ≠ null` | `canonical_ref = null` (r8-m) |
| `canonical_predecessor_ref` | (condicional = D4.16) | `canonical_ref = null` |
| `natural_key` | `canonical_ref = null` | `canonical_ref ≠ null` |
| `hierarchy_role` ∈ {PRIMARY, SUB} | node_type = hypothesis | node_type ≠ hypothesis |
| `producer_type`, `producer_id` | node_type ∈ {hypothesis, evidence, structure} | — (opcionais nos demais, exceto conviction — D4.12) |
| `ontological_status` ∈ {observational, theoretical} | node_type ∈ {structure, regime, narrative} | demais node_types |
| `school` | — (derivado pelo KG, D4.14) | sempre, na submissão (r7-i) |
| **Relação (`creation`)** | | |
| `relation_type`, `from_node` | toda relação | — |
| exatamente um de `to_node` / `target_relation_id` | toda relação | `target_relation_id` com relation_type ≠ INVALIDA |
| `causal` | (presença interna = D4.10) | relation_type ≠ CAUSA |
| `similarity_basis` | (presença interna = D4.10) | relation_type ≠ SIMILAR_A |
| `relation_confidence` | — (opcional) | extremidade `conviction` = D4.12 (iii) (código próprio) |
| **`invalidation`** | | |
| `reason` | sempre | — |
| **`archival`** | | |
| `relevance`, `reason` | sempre | — |
| **`canonical_state_transition`** | | |
| `canonical_model`, `canonical_ref`, `status_from`, `status_to` (∈ enum do modelo) | sempre | — |
| `transition_timestamp`, `transition_origin`, `justification` | sempre — [FONTE] CEM-001 l.428 ("registrar: timestamp, origem e justificativa") para evidence; uniformidade para CHM-001/CCM-001 = [PROPOSTA] local | — |
| `successor_ref` | (condicional = D4.16) | — |
| **`collision`** (derivado — D4.13) | | |
| `contradiction_pair`, `overlap_window`, `detected_at` | sempre | — |
| **Envelope (qualquer `record_kind`)** | | |
| `publication.origin` | — (atribuído pelo KG, D4.2; presença no envelope final = D4.3) | sempre, na submissão (r8-g) |

- **D4.20 Autorização de escrita de conhecimento e do catálogo (CKG-009):** (i) `allowlist == INDEFINIDA` (mantenedor = [DECISÃO NECESSÁRIA]) ⇒ `WRITER_ALLOWLIST_UNDEFINED`. (ii) **Separação de funções (r8-d):** allowlist que contenha a identidade de serviço dos gates é tratada como INDEFINIDA (mesmo código — fail-closed); `writer_id ∉ allowlist`, `writer_id` = identidade de serviço, ou autenticação falha/indisponível ⇒ `WRITER_UNAUTHORIZED`. (i)/(ii) valem para a classe SUBMETER (`kg_record`); o log tem regra própria (D4.5). (iii) **Catálogo (R8-1):** "ato de governança de ontologia **em runtime**" = conjunto **vazio na v1.0** — sua definição depende de K-001 (ABERTA; **não decidida aqui**) e entra só por emenda; logo toda operação da classe ALTERAR_CATÁLOGO (D4.0), de qualquer identidade, ⇒ `ONTOLOGY_CHANGE_NOT_GOVERNED`. Alteração legítima de ontologia/taxonomia = só **emenda spec-time homologada** desta Spec (RULE-HG [INFERÊNCIA]), que publica nova `schema_version`, prospectiva e backward-compatible (INV-07). Uma SUBMETER com tipo fora do catálogo não altera o catálogo — é rejeitada por D4.1.

Nenhuma fórmula computa convicção. Nenhum limiar de convicção nem escala numérica de confiança é fixado (RULE-MET-01).
[FONTE: atomic-spec §2; CEM-001 Cap.5/l.271-283/l.351-355/l.450; CHM-001 l.361/l.588/l.744-757; CCM-001 l.58; SPEC-004 INV-CBP-01, plan l.338/l.381/l.689; research.md §3.1/§4]

---

## D5 — Máquina de estados (lifecycle do conhecimento — projeção)

> Lifecycle do conhecimento no KG, separado da máquina da hipótese (CHM-001) e do estado no Blackboard (SPEC-004). **O estado não é campo mutado: é a projeção D4.7** — definição e precedência estão SÓ lá (r7-a). Os nomes são homônimos ≠ estados canônicos (Termo 6).

| Estado (derivado) | Definição | Origem |
|---|---|---|
| ACTIVE_KNOWLEDGE | D4.7 (último ramo) | creation |
| SUPERSEDED | D4.7 | creation com `supersedes` (CKG-012) |
| INVALIDATED_IN_TIME | D4.7 | invalidation (CKG-004) |
| ARCHIVED | D4.7 | archival (CKG-012; autorização D4.20) |

> **Estados transitórios de admissão (não persistidos):** `CANDIDATE_WRITE` (sob os gates de D4.0) e `REJECTED` (primeiro predicado reprovado ou unidade D4.18 falhou; só a decisão vai ao log); desfecho `NO_OP` (duplicata — D4.0 passos 8/9; só a decisão vai ao log) não é estado de conhecimento. `CANDIDATE_WRITE → ACTIVE_KNOWLEDGE` exige a unidade D4.18 gravada — **inalcançável na v1.0** (D4.15). Mecanismo físico = INDETERMINADO (H-001 ABERTA); Opção B (banco de grafos) registrada e adiada (research.md §3.5).

---

## D6 — Protocolo de escrita/consulta

- **Classe de operação:** toda operação é classificada primeiro (**D4.0**: MUTAR, ALTERAR_CATÁLOGO, ANEXAR_LOG, CONSULTAR, SUBMETER); MUTAR, ALTERAR_CATÁLOGO e ANEXAR_LOG são sempre negadas na v1.0, com a negação no log.
- **Escrita:** uma SUBMETER segue a sequência de **D4.0** (passos 1–11). Na v1.0 toda submissão de conhecimento termina no passo 2 (`ADMISSION_CONTRACT_UNDEFINED`) e a única escrita é a decisão no log (D4.5).
- **Atos sobre sujeito admitido** (invalidation, archival, correção, canonical_state_transition) são novas submissões pela mesma ordem — nunca automáticas nem em cascata (CEM-001 l.602; CHM-001 l.672-676). Quem os pratica e por qual gatilho = emendas de caminho.
- **Produtor** (SAS-001 §6.12) registra relações (emenda E-c) e não redefine ontologia (D4.20).
- **Eventos:** consumo de `Evidence.Invalidated` (transportado pela SPEC-005) e emissão pelo KG = emenda E-e; se vierem, só disparam ato autorizado, nunca invalidação automática (CEM-001 l.602) [INFERÊNCIA].
- **Consulta:** read-only, opcional/não-bloqueante (SAS-001 l.163); D4.8; não grava nem no log; tentativa de gravação = DENY registrado (D4.0).

> Fronteira: trabalho = SPEC-004; notificação = SPEC-005; formação = SPEC-007. A SPEC-006 só preserva, relaciona e consulta. [FONTE: ROADMAP §5/§6/§7]

---

## D7 — Cenários de Teste

> **Convenção:** (i) cenário de **gate** verifica o PREDICADO sobre a entrada, isolado dos demais gates; (ii) consulta/lifecycle/colisão usam **fixture** de registros já no KG; (iii) persistência fim a fim na v1.0 = só o DENY de D4.15; (iv) o detector de colisão é predicado sobre relação de fixture tratada como aprovada nos passos 2–9; (v) um fixture pode PRESUMIR, declarando-o, um contrato ou decisão pendente (contrato de admissão, allowlist com o escritor do teste, mapeamento `producer_id`→`school`) só para o predicado sob teste, **nunca concluindo admissão positiva**. Cenário idêntico ao VERIFICADO POR de uma BASpec o referencia. Fixtures de tempo usam `T0 < T1 < T2 < …` (r8-j). 26 cenários.

### Cenário-CKG-T01 — Integridade: ORIGINA com origem ICT
= VERIFICADO POR de BASpec-CKG-001.

### Cenário-CKG-T02 — Objeto de Skill rotulado evidence
= VERIFICADO POR de BASpec-CKG-002.

### Cenário-CKG-T03 — Relação fora do catálogo
= VERIFICADO POR de BASpec-CKG-003.

### Cenário-CKG-T04 — Validade muda por novo registro
= VERIFICADO POR de BASpec-CKG-004.

### Cenário-CKG-T05 — DELETE/UPDATE negados (conhecimento e log)
= VERIFICADO POR de BASpec-CKG-006.

### Cenário-CKG-T06 — Guard D4.12 por node_type/campo
```
DADO        (predicado do passo 4) (a) CAUSA(calibration_metric → conviction); (b) PERTENCE_A(calibration_metric → conviction);
            (c) nó conviction com campo "cost"; (d) relação com relation_confidence entre nós que não são conviction;
            (e) nó conviction com successor_ref; (f) CAUSA(learning → conviction); (g) SIMILAR_A(conviction → conviction) com
            relation_confidence
QUANDO      o guard D4.12 roda
ENTÃO       (a),(b),(f) rejeitadas; (c),(e),(g) rejeitados; (d) aprovada pelo guard
VERIFICAÇÃO reason(a) == reason(b) == reason(f) == "ONTOLOGY_INTEGRITY_VIOLATION"; reason(c) == reason(e) == reason(g) ==
            "CONFIDENCE_IS_NOT_CONVICTION"; guard(d) == PASS
```

### Cenário-CKG-T07 — CAUSA sem mecanismo/regime
= VERIFICADO POR de BASpec-CKG-008.

### Cenário-CKG-T08 — Autenticação indisponível
= VERIFICADO POR de BASpec-CKG-009, caso (a).

### Cenário-CKG-T09 — Porta de admissão nega por padrão
= VERIFICADO POR de BASpec-CKG-010 (casos (i)–(v)).

### Cenário-CKG-T10 — Trace completo (3 saltos)
= VERIFICADO POR de BASpec-CKG-011.

### Cenário-CKG-T11 — Colisão registrada
= VERIFICADO POR de BASpec-CKG-013.

### Cenário-CKG-T12 — PRIMARY sem gate nem ancestral passa em D4.2
= VERIFICADO POR de BASpec-CKG-005, caso (a).

### Cenário-CKG-T13 — Correção = nova versão
= VERIFICADO POR de BASpec-CKG-012.

### Cenário-CKG-T14 — Sem `computed_by`
= VERIFICADO POR de BASpec-CKG-005, caso (b).

### Cenário-CKG-T15 — HERDA SMC-SUB → Elliott-PRIMARY (positivo)
```
DADO        hipótese SUB de school=SMC (mapeamento SMC presumido — convenção (v)) com parent_id para hipótese PRIMARY de school=Elliott
QUANDO      D4.1 ∧ D4.14 avaliam a relação HERDA (predicado — convenção (i))
ENTÃO       aprova (entre escolas é permitido — RULE-HH-003); a persistência continua barrada por D4.15 (T16)
VERIFICAÇÃO integrity_gate == PASS; parent_hierarchy_role == "PRIMARY"; parent_school == "Elliott"
```

### Cenário-CKG-T16 — Sequência D4.0 para PRIMARY sem gate e sem ancestral
```
DADO        nó hypothesis PRIMARY (producer_id="elliott_specialist" ⇒ school=Elliott), lineage=[], produced_by_gate=false,
            computed_by/writer_id autenticados
QUANDO      a sequência D4.0 roda e, à parte, os passos 3–5 são avaliados como predicados (allowlist de fixture — convenção (v))
ENTÃO       a sequência para no passo 2; nada persistido; os predicados dos passos 3, 4 e 5 aprovam
VERIFICAÇÃO sequence_stop_step == 2; rejected_reason == "ADMISSION_CONTRACT_UNDEFINED"; written == false;
            step3 == PASS; step4 == PASS; step5 == PASS; step5_required_gate_record == false
```

### Cenário-CKG-T17 — Reconstrução/auditoria a partir dos registros
```
DADO        fixture append-only (T0 < T1 < T2 < T3 < T4 = "agora"):
            relação R = CONFIRMA(A→B): creation R0 {valid_from=T0, recorded_at=T0}; invalidation R1 → R0 {valid_to=T3, recorded_at=T3};
            relação R' = REFUTA(A→B): creation R2 {valid_from=T1, recorded_at=T1};
            collision C1 {relation_a_ref=R0, relation_b_ref=R2, contradiction_pair=CONFIRMA×REFUTA, overlap_window=[T1,+∞) como-registrado
            em T1, detected_at=T1, gate_record=DEC-1}; log com DEC-1 {gate_id=CKG-013, result=PASS, writer_id=identidade de serviço,
            submission_id = o de R2, collision_pair={R0,R2}} e DEC-0 {gate_id=CKG-013, result=PASS, collision_pair=null, submission_id = o de R0};
            nó H@1 com canonical_state_transition S1 (ACTIVE→DOMINANT, transition_timestamp=T1) e S2 (DOMINANT→SUPERSEDED,
            transition_timestamp=T2), ambas com transition_origin e justification; nó H@2 com canonical_predecessor_ref=H@1;
            caso negativo: collision adulterado C2 (fixture) com gate_record=DEC-0
QUANDO      um auditor independente reconstrói o histórico só a partir dos registros (replay por sujeito e version — D4.4)
ENTÃO       todo registro satisfaz D4.3/D4.4/D4.19; toda referência resolve; o gate_record de C1 resolve por D4.2; o de C2 NÃO resolve
            (PASS sem colisão); estado(R,T4) = INVALIDATED_IN_TIME; histórico canônico de H@1 = [S1,S2]; cadeia H@1→H@2 navegável;
            o recálculo de colide (D4.13) reproduz exatamente {C1}, com os mesmos contradiction_pair e overlap_window
VERIFICAÇÃO envelope_complete_all(C2 excluído) == true; orphan_refs == 0; collision_gate_record_resolves(C1) == true;
            collision_gate_record_resolves(C2) == false; distinct_knowledge_record_formats == 1; projected_state(R,T4) == "INVALIDATED_IN_TIME";
            version_chain(H) == ["H@1","H@2"]; recomputed_collisions == {C1}; recomputed_overlap_window(C1) == [T1,+∞)
```

### Cenário-CKG-T18 — SIMILAR_A: gate de saída
```
DADO        (a) SIMILAR_A(P1→P2) do juízo sem similarity_basis; (b) SIMILAR_A(P1→P1); (c) com base e mesmo node_type; (d) SIMILAR_A(P2→P1)
            com SIMILAR_A(P1→P2) vigente
QUANDO      D4.10 roda
ENTÃO       (a),(b) rejeitadas; (c) aprovada; (d) NO_OP (T26)
VERIFICAÇÃO reason(a) == "SIMILARITY_BASIS_MISSING"; reason(b) == "ONTOLOGY_INTEGRITY_VIOLATION"; gate(c) == PASS; result(d) == "NO_OP";
            new_record(d) == false
```

### Cenário-CKG-T19 — Ancestrais sem estado de espera; aciclicidade
```
DADO        fixture: A e Y (evidence PRIMARY) no KG; C (DERIVED, Lineage=[A]); D (DERIVED, Lineage=[X]), X ausente; F (DERIVED,
            Lineage=[F]); (g) relação DERIVA_DE(C→Y) com Y ∉ Lineage(C)
QUANDO      D4.17 avalia C, D e F, e D4.1 avalia (g) (predicados)
ENTÃO       C passa com DERIVA_DE(C→A) materializada (registro derivado, gate_record = PASS de CKG-003); D e F rejeitadas; (g)
            rejeitada; nenhum estado de espera; nenhum ciclo formável
VERIFICAÇÃO step(C) == PASS; deriva_de(C→A).publication_origin == "kg_internal"; reason(D) == reason(F) == "ANCESTOR_NOT_ADMITTED";
            reason(g) == "ONTOLOGY_INTEGRITY_VIOLATION"; waiting_states == 0; deriva_de_cycles == 0
```

### Cenário-CKG-T20 — Presença de campos, escola não derivável e allowlist indefinida
```
DADO        (a) hypothesis com producer_id do SMC Specialist (não fixado); (b) escrita qualquer com o mantenedor da allowlist pendente;
            (c) hypothesis SEM hierarchy_role; (d) structure SEM ontological_status; (e) hypothesis com `school` informado na submissão;
            (f) evidence PRIMARY com producer_type=ENGINE; (g) nó asset com evidence_origin_type; (h) invalidation sem reason;
            (i) canonical_state_transition de evidence sem justification (CEM-001 l.428); (j) relação sem from_node; (k) archival sem
            relevance; (l) submissão com publication.origin informado; (m) nó hypothesis com canonical_ref e sem canonical_status;
            (n) allowlist de fixture que contém a identidade de serviço
QUANDO      os predicados D4.14 (a), D4.20 (b, n), D4.19 (c, d, e, h–m) e D4.2 (f, g) rodam
ENTÃO       todos rejeitados
VERIFICAÇÃO reason(a) == "SCHOOL_UNDERIVABLE"; reason(b) == reason(n) == "WRITER_ALLOWLIST_UNDEFINED"; reason(c) == reason(d) ==
            reason(e) == reason(h) == reason(i) == reason(j) == reason(k) == reason(l) == reason(m) == "FIELD_PRESENCE_VIOLATION";
            reason(f) == reason(g) == "PROVENANCE_INCONSISTENT"; written(a..n) == false
```

### Cenário-CKG-T21 — Unidade reprovada não deixa `collision` pendurado (identidades explícitas; concorrência — r8-k)
```
DADO        fixture: CONFIRMA(A→B) vigente; REFUTA(A→B) aprovada nos passos 2–10 (contrato presumido — convenção (v)); colide = true;
            identidade de serviço do KG AUTENTICADA e disponível; entre o passo 10 e o commit, outra unidade grava a creation de uma
            REFUTA(A→B) com a mesma chave D4.9 (mesmo valid_from) — o sujeito passa a ter version 1 gravada
QUANDO      o commit D4.18 roda (revalidação D4.4 da creation em admissão: version = 1 ≠ 1 + max = 2)
ENTÃO       a unidade não é gravada (nem a creation de REFUTA, nem o collision, nem o PASS); a falha é registrada como DENY pela
            identidade de serviço
VERIFICAÇÃO reason == "RECORD_VERSION_INVALID"; refuta_written == false; collision_written == false; pass_decisions_written == false;
            dangling_collision_refs == 0; deny_logged_by_service_identity == true
```

### Cenário-CKG-T22 — Regra de escrita do log (R7-1)
```
DADO        (a) submissão aprovada nos passos 2–10 (contrato presumido — convenção (v)), mas o append das decisões PASS falha no commit;
            (b) escritor da allowlist de conhecimento tenta anexar kg_gate_decision{gate_id=CKG-013, result=PASS};
            (c) identidade de serviço do KG não autenticável, com submissão qualquer
QUANDO      D4.5/D4.18 são aplicados
ENTÃO       (a) nenhum registro de conhecimento gravado; (b) negado; (c) nenhum registro de conhecimento comitável
VERIFICAÇÃO knowledge_written(a) == false; reason(b) == "LOG_WRITER_UNAUTHORIZED"; forged_pass_present(b) == false;
            knowledge_written(c) == false
```

### Cenário-CKG-T23 — Classes de operação: posição e log (R8-1)
```
DADO        (a) UPDATE de um kg_record vindo de identidade NÃO autenticada; (b) escritor da allowlist (fixture — convenção (v)) solicita
            acrescentar um relation_type ao catálogo §D2.1; (c) operação de consulta que tenta gravar uma relação; (d) consulta read-only
            do trace de uma evidência de fixture
QUANDO      D4.0 classifica e avalia cada operação
ENTÃO       (a) negada pela classe MUTAR antes de qualquer autenticação; (b) negada pela classe ALTERAR_CATÁLOGO; (c) negada pela classe
            CONSULTAR; (a)–(c) registram exatamente uma decisão DENY cada, pela identidade de serviço; (d) responde sem gravar nada
VERIFICAÇÃO reason(a) == "RECORD_MUTATION_FORBIDDEN"; reason(b) == "ONTOLOGY_CHANGE_NOT_GOVERNED"; reason(c) == "QUERY_WRITE_FORBIDDEN";
            deny_decisions_logged(a) == deny_decisions_logged(b) == deny_decisions_logged(c) == 1; operation_class(a,b,c) ==
            ["MUTAR","ALTERAR_CATÁLOGO","CONSULTAR"]; knowledge_written(a..d) == false; log_records_created(d) == 0
```

### Cenário-CKG-T24 — Registro derivado inválido derruba a unidade (R8-3/R8-4)
```
DADO        fixture: unidade D4.18 montada para REFUTA(A→B) aprovada nos passos 2–10 (contrato presumido — convenção (v)), com colide = true;
            (a) o collision da unidade tem gate_record = PASS de CKG-013 com collision_pair = null; (b) o collision da unidade tem
            gate_record = PASS de CKG-013 de OUTRA submissão; (c) o collision da unidade não tem overlap_window
QUANDO      o passo 11 valida os registros derivados
ENTÃO       (a),(b) unidade inteira rejeitada por proveniência; (c) unidade inteira rejeitada por presença; nada gravado; DENY no log
VERIFICAÇÃO reason(a) == reason(b) == "GATE_RECORD_UNRESOLVED"; reason(c) == "FIELD_PRESENCE_VIOLATION"; refuta_written(a..c) == false;
            collision_written(a..c) == false; pass_decisions_written(a..c) == false; deny_logged(a..c) == true
```

### Cenário-CKG-T25 — Janela temporária e 2ª creation (r8-c)
```
DADO        fixture: (a) creation C1 de relação com valid_from=T0 e valid_to=T5 (temporária — S14), sem invalidação; (b) creation com
            valid_from=T2 e valid_to=T1; (c) 2ª creation do sujeito de C1 (mesma chave D4.9, payload diferente) com supersedes = null;
            (d) idem com supersedes = C1
QUANDO      D4.6/D4.7 projetam (a) em T1 e T6; D4.3 avalia (b); D4.4 avalia (c) e (d)
ENTÃO       (a) válida em T1 e não válida em T6; (b) rejeitada; (c) rejeitada; (d) aprovada pelo predicado e C1 projeta SUPERSEDED
VERIFICAÇÃO valid_at(C1,T1) == true; valid_at(C1,T6) == false; projected_state(C1,T6) == "INVALIDATED_IN_TIME" (antes de (d));
            reason(b) == "VALIDITY_WINDOW_INVALID"; reason(c) == "RECORD_VERSION_INVALID"; step(d) == PASS;
            projected_state(C1) == "SUPERSEDED" (após (d), fixture)
```

### Cenário-CKG-T26 — Desfecho NO_OP (r8-b)
```
DADO        fixture (passos 2–7 presumidos aprovados — convenção (v)): (a) reescrita idêntica de uma creation já gravada (mesma chave
            D4.9 e mesmo payload); (b) SIMILAR_A(P2→P1) com SIMILAR_A(P1→P2) vigente
QUANDO      a sequência SUBMETER segue dos passos 8–9
ENTÃO       ambas encerram em NO_OP; nenhum kg_record gravado; uma decisão no log por operação
VERIFICAÇÃO result(a) == result(b) == "NO_OP"; reason(a) == reason(b) == "DUPLICATE_NO_OP"; stop_step(a) == 9; stop_step(b) == 8;
            knowledge_written(a,b) == false; decisions_logged(a) == decisions_logged(b) == 1
```

---

## D8 — Rigor adversarial focado

> Alvo D0–D7 + D8 focado. **27 casos**, cobrindo as 13 BASpecs e as fronteiras. Princípios: fail-closed; nunca deletar/mutar; H-001 INDETERMINADO. ADV-08/09/10 são verificações **spec-time** (sobre o texto do Plan), não códigos de runtime.

### ADV-CKG-01 — Deleção disfarçada de "esquecimento" (CKG-006)
**DADO:** "esquecer" como DELETE físico ou UPDATE de `kg_gate_decision`. **QUANDO:** D4.3. **ENTÃO:** negar `RECORD_MUTATION_FORBIDDEN`; só arquivamento. **PORQUE:** INV-07. **VERIFICAÇÃO:** physical_delete == false; gate_decision_mutated == false.

### ADV-CKG-02 — Sobrescrita silenciosa de relação contraditória (CKG-013)
**DADO:** REFUTA(A→B) sobre CONFIRMA(A→B) (fixture — D7 (iv)). **QUANDO:** D4.13/D4.18. **ENTÃO:** registrar colisão; preservar ambas. **PORQUE:** perder a contradição apaga conhecimento. **VERIFICAÇÃO:** silent_overwrite == false; both_relations_present == true.

### ADV-CKG-03 — Confiança vira dimensão de convicção (CKG-007)
**DADO:** confiança exposta no nó `conviction` ou somada como 9ª dimensão. **QUANDO:** D4.12. **ENTÃO:** `CONFIDENCE_IS_NOT_CONVICTION`. **PORQUE:** INV-04 (custo) + extensão local; dimensionalidade=8 fechada. **VERIFICAÇÃO:** confidence_exposed_in_conviction_object == false.

### ADV-CKG-04 — CAUSA pós-hoc sem marcador (CKG-008)
**DADO:** (a) CAUSA só por co-ocorrência; (b) CAUSA completa mas sem `posthoc_flag`. **QUANDO:** D4.10. **ENTÃO:** ambas `CAUSAL_FIELDS_MISSING` (ausência ≠ false). **Limite:** `posthoc_flag=false` falso não é detectável (ENF-03). **VERIFICAÇÃO:** causal_written(a) == causal_written(b) == false.

### ADV-CKG-05 — Métrica de custo/calibração ligada à convicção (CKG-007)
**DADO:** (a) relação `calibration_metric`→`conviction`; (b) nó `conviction` com campo de custo. **QUANDO:** D4.12. **ENTÃO:** (a) `ONTOLOGY_INTEGRITY_VIOLATION`; (b) `CONFIDENCE_IS_NOT_CONVICTION`. O ARMAZENAMENTO da métrica (CEE-001 l.111) não é demonstrável na v1.0 (D4.15; emenda E-d) — Bloco B PARCIAL. **VERIFICAÇÃO:** cost_or_confidence_to_conviction_edge == false.

### ADV-CKG-06 — Proveniência exigível ausente ou incoerente (CKG-005; r7-c)
**DADO:** (a) sem `computed_by`; (b) evidence DERIVED com `lineage=[]`; (c) `produced_by_gate=true` sem `gate_record`; (d) `produced_by_gate` ausente; (e) evidence sem `evidence_origin_type`; (f) evidence DERIVED com `producer_type=AGENT`. **QUANDO:** D4.2. **ENTÃO:** (a) `COMPUTED_BY_MISSING`, (b) `LINEAGE_MISSING`, (c) `GATE_RECORD_MISSING`, (d)/(e)/(f) `PROVENANCE_INCONSISTENT`. **Limite declarado:** a condicionalidade de `gate_record` depende de `produced_by_gate` DECLARADO; um objeto que passou por gate e declara `false` não é detectável pelo KG (consistência ≠ veracidade — D4.2; coincidência com o canônico = emenda E-a). **VERIFICAÇÃO:** written(a..f) == false.

### ADV-CKG-07 — Produtor redefine ontologia (CKG-009)
**DADO:** produtor autenticado (inclusive da allowlist) solicita alteração do catálogo §D2.1. **QUANDO:** D4.0 (classe ALTERAR_CATÁLOGO) / D4.20 (iii). **ENTÃO:** negado; negação no log. **PORQUE:** SAS-001 §6.12; atos de governança de runtime = conjunto vazio na v1.0 (K-001 ABERTA). **VERIFICAÇÃO:** reason == "ONTOLOGY_CHANGE_NOT_GOVERNED"; ontology_redefined_by_producer == false; deny_logged == true (T23 b).

### ADV-CKG-08 — KG forma conhecimento / absorve a SPEC-007 (spec-time)
**DADO:** texto do Plan que atribua ao KG extração, retrieval, validação ou selo. **QUANDO:** revisão do escopo. **ENTÃO:** ausente — formação é SPEC-007; selo é emenda E-b. **VERIFICAÇÃO:** formation_in_kg_spec == false.

### ADV-CKG-09 — Mecanismo físico fixado por inércia (spec-time; CONS-01)
**DADO:** pressão para fixar "grafo real" ou um engine. **QUANDO:** revisão das decisões. **ENTÃO:** mecanismo permanece INDETERMINADO; Opção B adiada. **PORQUE:** H-001 é de Andraus. **VERIFICAÇÃO:** h001_decided_by_spec == false.

### ADV-CKG-10 — Absorver vizinhos, tocar decisão aberta ou antecipar emenda (spec-time)
**DADO:** o Plan virar memória de trabalho, transporte, estado por agente ou ciclo de aprendizado; tocar M-001/J-001/N-001/G-001/K-001/C-001/WF-D03; executar R-07; ou trazer para o núcleo contrato de caminho (a)/(b)/(c). **QUANDO:** revisão do escopo. **ENTÃO:** ausente; decisões abertas permanecem ABERTAS; contratos ficam para emendas. **VERIFICAÇÃO:** neighbors_absorbed == false; open_decisions_touched == false; path_contracts_in_core == false.

### ADV-CKG-11 — Nó redefine contrato canônico (CKG-002)
**DADO:** (a) nó-hipótese cujo payload traz campos do contrato CHM-001 (ex.: `states`, `parent_hypothesis_id`) fora do schema do KG; (b) mudança de Status canônico por transição fora do grafo CHM-001. **QUANDO:** D4.19 / D4.16. **ENTÃO:** (a) `FIELD_PRESENCE_VIOLATION` (payload fechado); (b) `CANONICAL_TRANSITION_ILLEGAL`. **PORQUE:** CC-02/CONST-01; o nó referencia por id@version. **VERIFICAÇÃO:** canonical_contract_redefined == false; written(a) == written(b) == false.

### ADV-CKG-12 — Matriz violada (CKG-001/003)
**DADO:** ORIGINA com origem ICT, ou SIMILAR_A entre tipos diferentes. **QUANDO:** D4.1/D4.10. **ENTÃO:** `ONTOLOGY_INTEGRITY_VIOLATION`. **VERIFICAÇÃO:** written == false.

### ADV-CKG-13 — Invalidação mutando o registro existente (CKG-004)
**DADO:** `valid_to` escrito sobre a creation. **QUANDO:** D4.3. **ENTÃO:** `RECORD_MUTATION_FORBIDDEN`; invalidação só por novo registro. **VERIFICAÇÃO:** existing_record_mutated == false.

### ADV-CKG-14 — Trace incompleto ou consulta que grava (CKG-011)
**DADO:** (a) reconstrução que para no 1º salto; (b) consulta que grava. **QUANDO:** D4.8 / D4.0 (classe CONSULTAR). **ENTÃO:** (a) exigir fecho completo; (b) negada, negação no log; nenhum kg_record. **VERIFICAÇÃO:** trace_complete(a) == true; records_created_by_query(a) == 0; reason(b) == "QUERY_WRITE_FORBIDDEN"; knowledge_written(b) == false; deny_logged(b) == true (T23 c).

### ADV-CKG-15 — Transição remove/reescreve a versão anterior (CKG-012)
**DADO:** SUPERSEDED implementado apagando a versão anterior. **QUANDO:** D4.3/D4.7. **ENTÃO:** negar; anterior preservada. **VERIFICAÇÃO:** old_version_preserved == true.

### ADV-CKG-16 — DERIVED sem DERIVA_DE por ancestral (CKG-003)
**DADO:** evidence DERIVED com Lineage=[C] e C ausente. **QUANDO:** D4.17. **ENTÃO:** `ANCESTOR_NOT_ADMITTED`. **VERIFICAÇÃO:** written == false.

### ADV-CKG-17 — hypothesis com school=ICT (CKG-001)
**DADO:** hypothesis cujo `producer_id` mapeia para ICT (mapeamento presumido — D7 (v)). **QUANDO:** D4.14. **ENTÃO:** `HYPOTHESIS_SCHOOL_ICT_FORBIDDEN`; ICT nunca cria hipótese (INV-02). **VERIFICAÇÃO:** written == false.

### ADV-CKG-18 — Colisão falsamente detectada/ignorada (CKG-013)
**DADO (fixtures):** (a) A1 CONFIRMA B e A2 REFUTA B; (b) CONFIRMA(A→B) invalidada em T1 e REFUTA(A→B) com `valid_from ≥ T1`; (c) janelas efetivas sobrepostas; (d) INVALIDA(E→R por `target_relation_id`); (e) re-submissão idêntica da REFUTA de (c). **QUANDO:** D4.13 (a–d); D4.9 (e). **ENTÃO:** só (c) colide; (d) não é par; (e) NO_OP no passo 9, sem segundo collision. **VERIFICAÇÃO:** colide(a)==colide(b)==colide(d)==false; colide(c)==true; result(e) == "NO_OP"; collisions_for_pair(c) == 1.

### ADV-CKG-19 — Envelope/versão/elo/janela inválidos ou formato paralelo (CKG-002/004/006/013)
**DADO:** (a) collision sem `record_id`/`version`; (b) `canonical_state_transition` com `target_record_ref` inexistente; (c) colisão em formato avulso; (d) evidence → SUPERSEDED sem `successor_ref`, ou hipótese version=2 com predecessor ausente; (e) CHM REFUTED→ACTIVE; (f) `valid_to` < `valid_from` do alvo; (g) `version` repetida ou `recorded_at` regressivo. **QUANDO:** passos 7/9. **ENTÃO:** (a)(b)(c) `RECORD_ENVELOPE_INCOMPLETE`; (d) `VERSION_LINK_MISSING`; (e) `CANONICAL_TRANSITION_ILLEGAL`; (f) `VALIDITY_WINDOW_INVALID`; (g) `RECORD_VERSION_INVALID`. **VERIFICAÇÃO:** written(a..g) == false; distinct_knowledge_record_formats == 1.

### ADV-CKG-20 — Juízo em laço de re-tentativa (CKG-008)
**DADO:** CAUSA do juízo reprovada; implementação tentaria re-invocar ou gerar nova submissão. **QUANDO:** D4.11. **ENTÃO:** ≤1 invocação, sem retry, INDETERMINADO. **VERIFICAÇÃO:** judgment_invocations_per_submission <= 1; kg_generated_retries == 0; kg_generated_submissions == 0.

### ADV-CKG-21 — Admissão "porque a origem parece legítima" (CKG-010)
**DADO:** evidência ACTIVE "vinda do ciclo de vida canônico", ou learning "com selo da SPEC-007", ou relação "de produtor autorizado". **QUANDO:** D4.15. **ENTÃO:** todas `ADMISSION_CONTRACT_UNDEFINED`; a origem declarada não substitui contrato homologado. **PORQUE:** precondição inexistente = não satisfeita (ENF-04); E3 irreversível. **VERIFICAÇÃO:** written == false (todas).

### ADV-CKG-22 — SIMILAR_A aceita só pelo escore (CKG-008)
**DADO:** escore alto do juízo sem `similarity_basis`. **QUANDO:** D4.10. **ENTÃO:** `SIMILARITY_BASIS_MISSING`; escore não é critério (ENF-03). **VERIFICAÇÃO:** acceptance_by_score == false.

### ADV-CKG-23 — PASS forjado no log / commit sem registro de decisão (CKG-009/006; R7-1)
**DADO:** (a) escritor de conhecimento anexa um PASS de CKG-013 para dar `gate_record` válido a um collision; (b) implementação comita conhecimento e anexa o PASS depois, fora da unidade. **QUANDO:** D4.5/D4.18. **ENTÃO:** (a) `LOG_WRITER_UNAUTHORIZED`; (b) proibido — as decisões PASS integram a unidade; falha do append ⇒ nada gravado (T22). **PORQUE:** SPEC-004 plan l.381; ENF-04. **VERIFICAÇÃO:** forged_pass_present == false; knowledge_without_decision == 0.

### ADV-CKG-24 — Bypass de regra por campo ausente ou informado (CKG-001; R7-2)
**DADO:** (a) hypothesis com `producer_id` não-Elliott e SEM `hierarchy_role` (escaparia de RULE-HH-002); (b) structure sem `ontological_status`; (c) submissão com `school=Elliott` e `producer_id` de outra escola. **QUANDO:** D4.19 (antes de D4.14). **ENTÃO:** todos `FIELD_PRESENCE_VIOLATION`. **VERIFICAÇÃO:** written(a..c) == false; rule_hh002_bypass == false.

### ADV-CKG-25 — Transição canônica sem timestamp/origem/justificativa (CKG-002; R8-2)
**DADO:** `canonical_state_transition` de evidence (a) sem `transition_timestamp`, (b) sem `transition_origin`, (c) sem `justification`. **QUANDO:** D4.19. **ENTÃO:** todas `FIELD_PRESENCE_VIOLATION`. **PORQUE:** CEM-001 l.428 ("Toda alteração de Status deverá … registrar: timestamp, origem e justificativa"). **VERIFICAÇÃO:** written(a..c) == false; reason(a..c) == "FIELD_PRESENCE_VIOLATION" (T20 i).

### ADV-CKG-26 — Registro derivado forjado de fora (CKG-010/013/003; R8-3)
**DADO:** produtor submete (a) um `collision` pronto; (b) uma `DERIVA_DE` com `publication.origin = kg_internal`. **QUANDO:** sequência D4.0; predicado D4.19 isolado. **ENTÃO:** na sequência, ambos `ADMISSION_CONTRACT_UNDEFINED` (passo 2); como predicado, (b) `FIELD_PRESENCE_VIOLATION` (`publication.origin` proibido na submissão); nenhuma emenda pode admiti-los (D4.15). **VERIFICAÇÃO:** written(a) == written(b) == false; reason_seq(a) == reason_seq(b) == "ADMISSION_CONTRACT_UNDEFINED"; reason_pred(b) == "FIELD_PRESENCE_VIOLATION".

### ADV-CKG-27 — PASS "sem colisão" reaproveitada como `gate_record` (CKG-013; R8-4)
**DADO:** implementação que referencia, no `collision`, a PASS de CKG-013 com `collision_pair = null` ou de outra submissão. **QUANDO:** D4.2 (passo 11). **ENTÃO:** `GATE_RECORD_UNRESOLVED`; unidade inteira não gravada. **PORQUE:** sem o par na decisão, a proveniência do collision não distingue "detectou" de "rodou". **VERIFICAÇÃO:** collision_written == false; reason == "GATE_RECORD_UNRESOLVED" (T24 a/b; T17 C2).

> **Cobertura (toda BASpec com ≥1 negação):** CKG-001→ADV-12/17/24, T20; 002→ADV-11/19(d,e)/25; 003→ADV-12/16/26, T19(g); 004→ADV-13/19(f), T25(b); 005→ADV-06, T20(f,g); 006→ADV-01/15/19(a–c,g), T23(a), T25(c); 007→ADV-03/05, T06(f,g); 008→ADV-04/20/22; 009→ADV-07/23, T20(b,n), T22, T23(b); 010→ADV-21/26, T09; 011→ADV-14, T23(c); 012→ADV-15; 013→ADV-02/18/27, T21, T24, T17(C2). Desfecho NO_OP: T26, ADV-18(e). Spec-time: ADV-08/09/10. Mapeiam para EC-CKG-001..006.

---

## D9 — Auditabilidade (por referência)

Todo registro de conhecimento é reconstruível (P13) e satisfaz D4.3/D4.4; a colisão tem um só formato (D4.13). As decisões ficam no log (D4.5) — segundo formato, papel distinto, igualmente imutável, com escritor único, completude (D4.5 (iv)) e `input_snapshot` para reexecução (ENF-07). Replay, recálculo de colisões e resolução de `gate_record`: T17. Trace: D4.8. Observabilidade agregada: SPEC-040/SPEC-004, por referência. Limite: sem digest (D4.3). [FONTE: CONSTITUTION P13; CEM-001 l.608-615; H-001 ABERTA]

---

## Contrato do nó/relação — esqueleto [PROPOSTA]

> Produto central da SPEC-006. Referencia os canônicos por `canonical_ref`; não os redefine (CC-02). Mecanismo físico = INDETERMINADO (H-001 ABERTA). **Esta seção lista campos e tipos; obrigatoriedade, predicados e códigos estão SÓ em D4** (D4.2, D4.3, D4.4, D4.5, D4.10, D4.12, D4.16, D4.19).

### I/O Schema (lógico — referência; não redefine CHM-001/CEM-001/CCM-001)
```json
{
  "kg_record": {
    "_comentario": "ENVELOPE ÚNICO append-only de conhecimento — regras: D4.3/D4.4; sem digest (limite D4.3)",
    "record_id": "string única",
    "record_kind": "creation | invalidation | archival | canonical_state_transition | collision",
    "subject_kind": "node | relation | collision",
    "subject_id": "KG-N-... | KG-R-... | KG-C-...",
    "version": "inteiro ≥ 1",
    "supersedes": "record_id | null",
    "target_record_ref": "record_id | null",
    "schema_version": "inteiro (migração de ontologia/schema = [DECISÃO NECESSÁRIA])",
    "provenance_ref": { "computed_by": "identidade autenticada (runtime)", "produced_by_gate": "true | false", "gate_record": "ref | null", "lineage": "[ref ao Lineage CEM-001 / derived_from[] SPEC-004]" },
    "writer_id": "identidade autenticada (runtime)",
    "publication": { "origin": "kg_internal | <valor de caminho a definir por emenda E-a..E-c> — atribuído pelo KG (D4.2)" },
    "recorded_at": "timestamp (transaction-time)",
    "valid_from": "timestamp | null",
    "valid_to": "timestamp | null",
    "payload": "um dos payloads abaixo, conforme (subject_kind, record_kind)"
  },
  "payload.node.creation": {
    "node_type": "hypothesis | evidence | observation | conviction | narrative | mission | learning | asset | timeframe | regime | structure | calibration_metric",
    "canonical_ref": "canonical_id@version | null",
    "canonical_status": "CHM-001 l.329: EMERGENT|CANDIDATE|ACTIVE|DOMINANT|SUPERSEDED|REFUTED|ARCHIVED; CEM-001 l.258-262: ACTIVE|SUPERSEDED|INVALIDATED|ARCHIVED; CCM-001 l.58: COMPUTED|GATED_PASS|GATED_BLOCK|SUPERSEDED",
    "canonical_predecessor_ref": "canonical_id@version | null",
    "producer_type": "AGENT | ENGINE (espelho CEM-001 l.271-275 / CHM-001 l.361)",
    "producer_id": "string (espelho CHM-001 l.361 / CEM-001 l.276-278)",
    "evidence_origin_type": "PRIMARY | DERIVED (espelho CEM-001 l.280-283)",
    "natural_key": "string (ex.: asset='BTC')",
    "hierarchy_role": "PRIMARY | SUB (ref. SPEC-001)",
    "ontological_status": "observational | theoretical (RULE-ONT-01)"
  },
  "payload.node.creation[node_type=conviction]": {
    "_comentario": "FECHADO — D4.12",
    "additionalProperties": false,
    "properties": ["node_type", "canonical_ref", "canonical_status", "canonical_predecessor_ref"]
  },
  "atributo_derivado_pelo_KG": { "school": "Elliott | Fibonacci | Fractal | SMC | ICT — LOCAL [PROPOSTA], calculado por D4.14; não é campo de submissão" },
  "payload.relation.creation": {
    "relation_type": "CONFIRMA | REFUTA | DEPENDE_DE | HERDA | PERTENCE_A | INVALIDA | ORIGINA | DERIVA_DE | SIMILAR_A | CAUSA | HIERARQUIA_DE | ESTATISTICA_DE",
    "from_node": "KG-N-...",
    "to_node": "KG-N-... | null",
    "target_relation_id": "KG-R-... | null",
    "relation_confidence": "escala PRÓPRIA — PARÂMETRO INDETERMINADO; ≠ Convicção; não toca J-001/N-001 (abertas)",
    "causal": "{ mechanism, direction, conditions, regime, posthoc_flag: true|false }",
    "similarity_basis": "[atributos/critério comparados]"
  },
  "payload.invalidation": { "reason": "string" },
  "payload.archival": { "relevance": "string", "reason": "string" },
  "payload.canonical_state_transition": {
    "canonical_model": "CHM-001 | CEM-001 | CCM-001",
    "canonical_ref": "canonical_id@version",
    "status_from": "enum do modelo",
    "status_to": "enum do modelo",
    "successor_ref": "canonical_id@version | null",
    "transition_timestamp": "timestamp", "transition_origin": "string", "justification": "string (CEM-001 l.428)"
  },
  "payload.collision": {
    "relation_a_ref": "record_id", "relation_b_ref": "record_id",
    "contradiction_pair": "CONFIRMA×REFUTA", "overlap_window": "[início, fim)", "detected_at": "timestamp"
  },
  "kg_gate_decision": {
    "_comentario": "LOG de decisões — formato próprio, fora do kg_record; regras: D4.5",
    "decision_id": "string única", "submission_id": "string",
    "operation_class": "MUTAR | ALTERAR_CATÁLOGO | ANEXAR_LOG | CONSULTAR | SUBMETER (D4.0)",
    "gate_id": "CKG-001..013", "gate_version": "string",
    "input_digest": "string", "input_snapshot": "cópia da operação recebida — dado de auditoria, não conhecimento (D4.5)",
    "result": "PASS | DENY | INDETERMINADO | NO_OP", "reason": "código de D4 | null (PASS)",
    "collision_pair": "[record_id, record_id] | null (só gate_id = CKG-013 — D4.5 (iv))",
    "judgment_invocations": "0 | 1", "writer_id": "identidade de serviço dos gates do KG", "decided_at": "timestamp"
  }
}
```
> Nenhum campo computa convicção nem deriva de custo (INV-04). `knowledge_state` não é campo: é a projeção D4.7.

---

## Enforcement Contracts

### EC-CKG-001 — Escrita de registro de conhecimento no KG permanente [E3]
```
CAPABILITY   : Gravar um registro de conhecimento válido no KG permanente
EFFECT       : Persistência permanente (commit crítico/irreversível; append-only; unidade atômica)
PRECOND      : classe SUBMETER (D4.0) AND D4.15 (na v1.0 nunca satisfeita) AND D4.20 (i)/(ii) AND D4.19 AND D4.1 AND D4.14
               AND D4.12 AND D4.2 AND D4.17 AND D4.16 AND D4.10/D4.11 AND D4.9 (não-duplicata) AND D4.3/D4.4 AND registros
               derivados válidos no passo 11 (D4.18; D4.2 regime kg_internal) AND D4.5(i) — na ordem D4.0
POSTCOND     : unidade D4.18 gravada (registro submetido + derivados [DERIVA_DE, collision] + decisões PASS) ou nada; NO_OP ⇒ nada
POLICY       : RULE-CKG-001/002/003/005/006/008/010/013; INV-CKG-02; CEM-001 l.608-615; CC-02; ENF-04
LEVEL        : E3 (Crítico — "KG publicado → E3 mínimo", atomic-spec l.238; irreversível)
FAILURE-MODE : Fail-closed — primeiro predicado reprovado ⇒ REJECTED com o código (D4.0); nada persistido; decisão no log.
               DENY por ausência de contrato (D4.15) é DENY por desenho, não falso-DENY. Limiar de falso-DENY = gap aberto
               (atomic-spec l.273/l.393) — CONDICIONAL
EVIDENCE     : kg_record conformes a D4.3/D4.4; método ENF-07: amostra de DENY do log reavaliada por re-execução determinística
               do gate (gate_id@gate_version) sobre `input_snapshot`, cuja integridade se confere pelo `input_digest` (D4.5 —
               r8-f) + revisão humana; tamanho/limiar = gap aberto
```

### EC-CKG-002 — Imutabilidade / append-only / versionamento (conhecimento e log) [E3]
```
CAPABILITY   : Impedir DELETE/UPDATE de kg_record e kg_gate_decision; transições só por novo registro
EFFECT       : Histórico só cresce
PRECOND      : D4.3 (só APPEND; classe MUTAR sempre negada antes de qualquer outro predicado — D4.0) AND D4.4 (kg_record)
               AND decision_id único (D4.5)
POSTCOND     : histórico de conhecimento e de decisões reconstruível por replay (T17); estado = D4.7; um só formato de
               registro de conhecimento (INV-07; INV-CBP-01)
POLICY       : RULE-CKG-004/006/012; INV-07; RULE-BB-004; SPEC-004 INV-CBP-01; INV-CKG-01
LEVEL        : E3 (perda/reescrita de histórico é irreversível; o log é a EVIDENCE dos EC E3 — ENF-02 impede rebaixar)
FAILURE-MODE : Fail-closed — DELETE/UPDATE ⇒ RECORD_MUTATION_FORBIDDEN; a negação é nova decisão no log. Falso-DENY E3 CONDICIONAL
EVIDENCE     : decisões de bloqueio no log; gate_decision_mutated == false (T05). Limite (r7-g): a prova é LÓGICA — lida do próprio
               log, sem digest; a integridade FÍSICA contra mutação abaixo da camada lógica não é provada (H-001/BUILD)
```

### EC-CKG-003 — Governança de escrita (conhecimento e log) [E3]
```
CAPABILITY   : Admitir escrita só de identidade autorizada e autenticada; negar alteração de catálogo em runtime, append
               externo ao log e gravação pelo canal de consulta
EFFECT       : Autorização (ou recusa) de escrita permanente no KG, de anexação ao log e de alteração do catálogo
PRECOND      : SUBMETER → D4.20 (i)/(ii) (allowlist definida e disjunta da identidade de serviço); log → D4.5 (só o pipeline,
               sob a identidade de serviço autenticada; ANEXAR_LOG externa negada); ALTERAR_CATÁLOGO → D4.20 (iii) (negada na
               v1.0); CONSULTAR que grava → negada (D4.8). Classes e precedência: D4.0. Gate determinístico (ENF-03)
POSTCOND     : só escritor autorizado grava conhecimento; só a identidade de serviço anexa ao log; catálogo inalterado em runtime;
               nenhuma gravação por consulta
POLICY       : RULE-CKG-009/011; SAS-001 §6.12; SPEC-004 RULE-CBP-014; atomic-spec §10.2; ENF-03/04
LEVEL        : E3 (escrita em memória permanente e no catálogo; cruza fronteira de confiança)
FAILURE-MODE : Fail-closed — WRITER_ALLOWLIST_UNDEFINED / WRITER_UNAUTHORIZED / LOG_WRITER_UNAUTHORIZED /
               ONTOLOGY_CHANGE_NOT_GOVERNED / QUERY_WRITE_FORBIDDEN (D4.0, D4.5, D4.8, D4.20), cada negação registrada no log;
               auth indisponível ⇒ não-autorizado; identidade de serviço indisponível ⇒ nenhum commit de conhecimento
               (D4.5 (iii)). Falso-DENY E3 CONDICIONAL (ENF-07)
EVIDENCE     : decisão no log (operation_class, identidade, motivo, input_snapshot) + amostragem ENF-07 (método do EC-CKG-001)
```

### EC-CKG-004 — Guard de custo E confiança [E3]
```
CAPABILITY   : Manter a confiança de relação em namespace próprio e o custo fora do nó/arestas de conviction
EFFECT       : Guard sobre a escrita permanente
PRECOND      : D4.12
POSTCOND     : nenhum campo fora da allowlist no nó conviction; nenhuma relação calibration_metric→conviction
POLICY       : RULE-CKG-007; INV-04 (custo); CCM-001
LEVEL        : E3 (decide admitir/recusar escrita permanente — atomic-spec l.238; ENF-02)
FAILURE-MODE : Fail-closed — códigos de D4.12; decisão no log. Falso-DENY E3 CONDICIONAL
EVIDENCE     : decisões com reason ∈ {CONFIDENCE_IS_NOT_CONVICTION, ONTOLOGY_INTEGRITY_VIOLATION} + amostragem ENF-07. Que o CÁLCULO
               de convicção (SPEC-003) não consuma a confiança = requisito à SPEC-003 / [DECISÃO NECESSÁRIA] — fora do KG
```

### EC-CKG-005 — Registro de relação causal/de similaridade [E3]
```
CAPABILITY   : Admitir CAUSA/SIMILAR_A só com os campos de D4.10; limitar o juízo a D4.11
EFFECT       : Escrita (ou recusa) de toda CAUSA/SIMILAR_A, qualquer produtor
PRECOND      : D4.10 AND (se há juízo) D4.11
POSTCOND     : campos auditáveis presentes (presença, não veracidade); ≤1 invocação por submissão; host pendente ⇒ 0
POLICY       : RULE-CKG-008; RULE-CAU-01/02/03; RULE-INQ-03; atomic-spec §10.6 l.315; ENF-03
LEVEL        : E3 (escrita permanente; herda EC-CKG-001)
FAILURE-MODE : Fail-closed — código de D4.10; desfecho INDETERMINADO; sem retry. Falso-DENY E3 CONDICIONAL
EVIDENCE     : judgment_invocations ≤ 1 e retries = 0 no log; amostragem ENF-07
```

### EC-CKG-006 — Consulta / Cognitive Trace Reconstruction (read-only)
```
CAPABILITY   : Responder consultas e reconstruir a cadeia cognitiva completa sem alterar estado
EFFECT       : Leitura/navegação (sem escrita)
PRECOND      : operação de consulta (D4.8). Autorização de LEITURA: política não definida = [DECISÃO NECESSÁRIA]; não declarada
               como precondição verificada
POSTCOND     : trace completo (D4.8); nenhum registro criado/alterado — nem kg_record nem kg_gate_decision
POLICY       : RULE-CKG-011; CEM-001 l.608-615; SAS-001 §6.12
LEVEL        : E1 — reavaliado na v1.8 (R8-1): a consulta read-only não tem efeito externo (não grava, não publica, não transiciona);
               o piso aplicável é o contratual (atomic-spec §10.2: E1 = schema + evidência observável). A NEGAÇÃO de uma tentativa de
               gravação pelo canal de consulta não é efeito desta capacidade: é efeito de escrita, governado por EC-CKG-003 (E3, com
               registro no log). Elevar este EC a E3 duplicaria aquele gate sem proteger nada a mais
FAILURE-MODE : tentativa de gravação ⇒ fora desta capacidade (classe CONSULTAR negada — D4.0; EC-CKG-003); eficiência de consulta
               ampla = INDETERMINADO até H-001
EVIDENCE     : contagem de registros antes/depois (records_created_by_query == 0, kg_record e kg_gate_decision); trace = fecho D4.8
```

---

## Plan — arquitetura de processo (derivado da Spec)

**Natureza:** serviço lógico de memória semântica permanente (Opção A — camada sobre conhecimento já validado): gates Classe C (admissão, autorização, ontologia, proveniência, imutabilidade, guard INV-04, colisão) + mecânica Classe D (catálogo, bitemporal, lifecycle, trace) + juízo Classe H com gate de saída. Não guarda trabalho, não transporta, não forma conhecimento, não decide, não computa convicção, não executa ordem, não escolhe o mecanismo físico (H-001 ABERTA). [FONTE: ROADMAP §6; CEM-001 l.608-615; SAS-001 §6.12]

**Roteamento de modelo (CEE-001 §5):** gates C/D não requerem LLM; o juízo (CKG-008) usa apoio semântico só como detector; gate de saída determinístico (ENF-03); host do juízo = [DECISÃO NECESSÁRIA] (até lá, 0 invocações).

**Dependências técnicas:** baselines do bloco INHERITS; atomic-spec v1.5; ENF-01..08. Emendas E-a..E-e dependem de decisões de Andraus (E-b também da SPEC-007). Referências [EXTERNO], não-baseline: research.md §2 (SRC-ZEP-01, SRC-PROV-01, SRC-MEMVSKG-01; SRC-FORGET-01 = DADO não-verbatim) e §5 (REPO-graphiti/graphrag/cognee/mem0 — elegíveis, nenhum adotado).

**Riscos e salvaguardas** (detalhe por caso: cobertura D8):

| Risco | Salvaguarda |
|---|---|
| Banco de grafos por inércia / H-001 fixada por engano | Opção A; Opção B adiada; ADV-09; CONS-01 |
| Contaminar a memória permanente por admissão sem contrato | D4.15 (nega por padrão); EC-001; ADV-21. **Custo declarado:** a v1.0 não admite conhecimento — escolha de Andraus (DHR-SPEC006-002) em favor de Conformidade/Eficácia |
| Deleção/mutação (conhecimento ou log); PASS forjado; commit sem decisão | D4.3/D4.5/D4.18; EC-002/003; ADV-01/13/15/23; T22 |
| Bypass por campo ausente | D4.19 antes de D4.14 (D4.0); ADV-24 |
| Confiança vira Convicção / custo no nó conviction | D4.12; EC-004; ADV-03/05 |
| Causalidade pós-hoc; juízo em laço | D4.10/D4.11; EC-005; ADV-04/20/22 |
| Colisão silenciada ou pendurada | D4.13/D4.18; ADV-02/18; T21 |
| Discriminantes declarados falsamente a montante | limite declarado (D4.2/D4.14 — forma); coincidência com o canônico = E-a |
| Mutação física abaixo da camada lógica | limite declarado (D4.3, sem digest); H-001/BUILD |
| Operação fora da sequência de submissão (mutação, alteração de catálogo, append externo ao log, consulta que grava) | classes de D4.0; EC-002/003; T23; ADV-01/07/14 |
| Registro derivado forjado ou com proveniência vazia (PASS "sem colisão") | D4.2 `GATE_RECORD_UNRESOLVED` + `collision_pair`; D4.15 (derivados não submissíveis); T17/T24; ADV-26/27 |
| Inundação do log por DENY | limite declarado: completude sem descarte (D4.5 (iv)); política de volume = [DECISÃO NECESSÁRIA] |
| `input_snapshot` guarda conteúdo não admitido | dado de auditoria fora do KG (não consultável por D4.8, não passa por D4.15) — D4.5 |

**Impacto (RULE-HG-04):** introduz o schema lógico de `kg_record` e `kg_gate_decision`; nenhum schema canônico nem das SPEC-004/005 alterado; nenhuma Skill afetada (INV-06); adiciona `checks.md`; compatibilidade Minor; não fecha decisão aberta (H-001 ABERTA).

**Tasks:** adiadas (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60, a Classe por BASpec e o mecanismo físico (hoje INDETERMINADO, H-001).

---

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório CRITICAL)

**Bloco A — "se estivesse errada, o que seria observável?"** (as negações estão na cobertura D8; aqui só o caso QUANDO-sim-ENTÃO-não e o limite de cada BASpec):
- **CKG-001:** observável por D4.19/D4.1/D4.14. QUANDO-sim-ENTÃO-não: `producer_id` declarado falso — não observável (limite de forma).
- **CKG-002:** observável (T02, T17, ADV-11/19). QUANDO-sim-ENTÃO-não: transição de conviction fora de tabela — não rejeitar por legalidade (CCM-001 sem tabela).
- **CKG-003/004/006/011/012:** observáveis por predicado ou fixture (`deriva_de_cycles`, `existing_record_mutated`, `records_created_by_query`, `old_version_preserved`). Sem caso QUANDO-sim-ENTÃO-não identificado além dos limites de D4.3 (sem digest).
- **CKG-005:** QUANDO-sim-ENTÃO-não: PRIMARY sem gate — D4.2 NÃO deve exigir gate_record/lineage (T12/T16). Limite: `produced_by_gate=false` falso (ADV-06).
- **CKG-007:** limite: texto livre de outros node_types (D4.12).
- **CKG-008:** QUANDO-sim-ENTÃO-não: SIMILAR_A inversa duplicada — NO_OP (T18 d; T26 b).
- **CKG-009:** QUANDO-sim-ENTÃO-não: DENY de submissão é registrado mesmo sem allowlist — o log não passa por D4.20 (D4.5 escopo). Caso de negação novo: allowlist que contém a identidade de serviço ⇒ tratada como indefinida (T20 n). Alteração de catálogo: observável (T23 b).
- **CKG-010:** observável por predicado (T09, ADV-21/26). Admissão positiva: **fora de escopo da v1.0** (não INDETERMINADO convertido em PASS). QUANDO-sim-ENTÃO-não: registro derivado não reavalia D4.15 (herda a admissão) — observável em fixture (T19, T24).
- **CKG-011:** QUANDO-sim-ENTÃO-não: a tentativa de gravação pela consulta GERA um registro no log — não contradiz "zero registros", porque a operação deixou de ser read-only (D4.8; T23 c/d).
- **CKG-013:** QUANDO-sim-ENTÃO-não: re-submissão idêntica — NO_OP antes da detecção (ADV-18 e; T26); PASS de CKG-013 existe mas `collision_pair = null` — não resolve um collision (T24, ADV-27).

**Cobertura de verificabilidade:** as 13 BASpecs têm ENTÃO verificável como predicado ou sobre fixture, com ≥1 negação. Nenhuma admissão positiva fim a fim é afirmada.

**Bloco B — herança obrigação-a-obrigação (CC-08):**
- CEM-001 "trace completo" (l.614) → D4.8 + D4.17 + D4.2 (regime `kg_internal` das `DERIVA_DE` materializadas — R8-3) (T10, T19, T24). **Mecanismo especificado e verificável por predicado/fixture; satisfação ponta-a-ponta PARCIAL até E-a** (na v1.0 nenhuma evidência DERIVED é admitida, logo nenhuma `DERIVA_DE` é materializada). A v1.7 dizia "Satisfeita no mecanismo" — superestimado (R8-3), corrigido.
- CEM-001 l.428 (timestamp, origem e justificativa de toda alteração de Status) → D4.19 (`canonical_state_transition`; T20 i; ADV-25). Mecanismo verificável; ponta-a-ponta PARCIAL até E-a.
- CEM-001 "todos os estados" (l.494/l.613) e "todas as versões" (l.612; sucessora l.450) → **PARCIAL**: mecanismo verificável (D4.16, `canonical_state_transition`; T17, ADV-19 d/e); admissão ponta-a-ponta depende de E-a. **Leitura única (R7-4):** não há supressão — a v1.0 não restringe estados de Evidência, e toda emenda fica proibida de restringi-los sem REMOVED governado ("Escopo em etapas"; RULE-HD-03). **[DECISÃO NECESSÁRIA]** quanto à emenda E-a, não quanto à obrigação.
- CEM-001 Cap.5 (`Lineage`, `Evidence Origin Type` e acoplamento com `Producer Type`) → D4.2/D4.17 — espelho de forma (limite declarado).
- CHM-001 (estados/versões) → D4.16 (l.588) por referência; o KG não transiciona.
- CCM-001 → D4.12 (payload fechado); elo de versão por [INFERÊNCIA] (l.58).
- SPEC-004 INV-CBP-01 + atomicidade sem "publicação sem registro de auditoria" (plan l.381/l.689) → D4.3/D4.18 + D4.5 (i) (decisões PASS dentro da unidade).
- SPEC-005 → consumo/emissão = E-e. SAS-001 §6.12/l.924 → D4.20; registro por produtor = E-c.
- RULE-BB-004/INV-07 → D4.3 (conhecimento e log); RULE-CAU-01/02/03 → D4.10.
- CEE-001 l.111 → **PARCIAL**: isolamento verificável (D4.12; ADV-05; T06); armazenamento = E-d.
- atomic-spec §10.2 → EC-001..005 em E3; §10.6 l.315 + RULE-INQ-03 → D4.11.
Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (único MODIFIED = RULE-BB-004 reforçada). Eixo VERTICAL não aplicável.

**Bloco C — epistêmico / N8–N17:**
- **RULE-EPI-01..03:** achado corrigido na v1.7 — a v1.6 tratava R-04..R-06 como "TRATADO" quando a ata §2 reserva a decisão ao gate (r7-f); agora "encaminhado — tratamento proposto". Na v1.8: a coluna "Classificação" deixa de afirmar "CONFORME" para R-04..R-06 — a leitura (fronteira CONFORME l.58-60 × residual ADIADO l.62) é [DECISÃO NECESSÁRIA] (r8-l); o Bloco B deixa de dizer "Satisfeita no mecanismo" para o trace (R8-3); INV-CKG-02 deixa de dizer "Garante" (r8-h). H-001 = INDETERMINADO; nenhuma hipótese como fato.
- **RULE-SEM-01/04:** acepções declaradas (Termos 1–7).
- **RULE-ONT-01/02:** ontologia explícita (§D2.1); `ontological_status` agora exigido por predicado (D4.19) — a v1.6 dizia "sem achado residual" sem predicado (R7-2), corrigido.
- **RULE-INQ:** questões abertas como [DECISÃO NECESSÁRIA]; RULE-INQ-03 em D4.11.
- **RULE-CAU-01/02/03:** D4.10; presença ≠ veracidade.
- **RULE-CTF:** nenhuma afirmação contrafactual carregada.
- **RULE-UNC-01..03:** incerteza localizada (eficiência de consulta ampla até H-001); a completude do trace não é incerta.
- **RULE-PRB:** nenhuma probabilidade ou precisão numérica; confiança = PARÂMETRO a calibrar.
- **RULE-DEC-01:** o KG armazena/relaciona/consulta; não decide nem executa (INV-05).
- **RULE-MET-01:** nenhuma proveniência fabricada; nenhum `producer_id` inventado (só o do Elliott, SPEC-001 l.203); SRC-FORGET-01 não sustenta sozinha alegação carregada; aciclicidade de D4.17 é derivação [INFERÊNCIA] declarada.

**Bloco D — reforço de escopo:** a Spec preserva/relaciona/consulta; não guarda trabalho (SPEC-004), não transporta (SPEC-005), não forma conhecimento (SPEC-007), não executa ordem (INV-05/RULE-DEC-01), não decide nem computa convicção. Nenhuma BASpec cruza a fronteira SOT→execução. Toda dependência de Andraus está na tabela de etiquetagem.

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| CEM-001; CHM-001; CCM-001; CEE-001; SAS-001; SPEC-004 v1.2; SPEC-005 v1.0; SPEC-001/019/020/021 v1.0 | [FONTE] | FATO NORMATIVO (BASELINE) |
| atomic-spec v1.5; RULES v1.5 (RULE-BB-004, RULE-CAU-01/02/03, RULE-INQ-03, RULE-MECH-01, RULE-HD-*, RULE-ONT-01); INV-*; ENF-*; CONSTITUTION l.191-192/l.233 | [FONTE] | FATO NORMATIVO |
| DHR-SPEC006-002 (Opção 2 em etapas; nota aditiva; ordem "Avançar") | [FONTE] | Decisão de Andraus registrada — não é baseline nem homologação do Plan |
| DHR-BACKLOG-001: BL-003/BL-011 `ATIVADO`, encaminhados ao gate da SPEC-006 | [FONTE] | Decisão de Andraus registrada (chat 2026-10-17) |
| CLASSIFICACAO-COLISOES-BL010-011-012; CONFLICT-MAP l.143-147 | [FONTE] | FATO NORMATIVO (DHR-BL010-011-012-001) |
| Correspondência R-04..R-06 → conteúdo; tratamentos propostos da Nota de gate | [INFERÊNCIA] / [PROPOSTA] | Decisão no gate (ata DHR-BACKLOG-001 §2) |
| RULE-CKG-001..013; INV-CKG-01/02; §D2.1/§D2.2; D4.0–D4.20 (inclui as cinco classes de operação, o regime `kg_internal` dos registros derivados, `input_snapshot`, `collision_pair`, desfecho NO_OP); `kg_record`; `kg_gate_decision`; campos locais; BASpec-CKG-001..013; EC-CKG-001..006 | [PROPOSTA] | Requer homologação |
| Uniformidade de `transition_timestamp`/`transition_origin`/`justification` para CHM-001/CCM-001 (para CEM-001 é [FONTE] l.428) | [PROPOSTA] | Local; não redefine CHM/CCM |
| Restrição a toda emenda: nenhum contrato admite `collision`/`DERIVA_DE` submetidos de fora | [PROPOSTA] | D4.15 |
| Restrição a toda emenda (não restringir estados/versões de Evidência) | [INFERÊNCIA] | De RULE-HD-03 + CEM-001 l.494/l.611-614 |
| Fontes SRC-ZEP-01/PROV-01/MEMVSKG-01; REPO-graphiti/graphrag/cognee/mem0 | [EXTERNO] | DADO, nunca baseline |
| SRC-FORGET-01 | [EXTERNO] | DADO não-verbatim |
| Mecanismo físico de armazenamento | [DECISÃO NECESSÁRIA] | **H-001 — EM ABERTO — não fechar** |
| Divergência ROADMAP l.177 ("Resolve H-001") × DHR-SPEC006-001 Q-ABERTURA-3 (H-001 não fechada) | [DECISÃO NECESSÁRIA] | Andraus; teto do parecer = CONFORME condicional (DHR-SPEC006-002 §2) |
| Banco de grafos dedicado (Opção B) | [DECISÃO NECESSÁRIA] | Adiado — registrado (INV-07) |
| Emendas E-a..E-e (contratos de caminho; promoção trabalho→permanente e sua atribuição à SPEC-018/K-001; selo; registro por produtor; nós de referência; consumo/emissão de eventos) | [DECISÃO NECESSÁRIA] | **Fora de escopo da v1.0** — sem contrato aqui |
| Mantenedor da allowlist; host do juízo; migração de ontologia | [DECISÃO NECESSÁRIA] | DENY `WRITER_ALLOWLIST_UNDEFINED`; host pendente ⇒ 0 invocações |
| Mapeamento `producer_id` → `school` (SMC/Fibonacci/ICT/Fractal) | [PROPOSTA] (tabela) / [DECISÃO NECESSÁRIA] (ids) | Só Elliott conhecido ⇒ demais `SCHOOL_UNDERIVABLE` |
| Escala numérica de confiança de relação | [DECISÃO NECESSÁRIA] | PARÂMETRO a calibrar (não toca J-001/N-001) |
| Limiar/amostra de falso-DENY (ENF-07) | [DECISÃO NECESSÁRIA] | Gap aberto (atomic-spec l.273/l.393) |
| Política de autorização de LEITURA | [DECISÃO NECESSÁRIA] | Não especificada |
| Requisito à SPEC-003: não consumir a confiança de relação | [DECISÃO NECESSÁRIA] | Endereçado à SPEC-003 na integração |
| R-07 / COL-EXP-05 e fila EXP-SPEC-001..053 | [DECISÃO NECESSÁRIA] | Onde reconciliar (Andraus) |
| Leitura de R-04..R-06: fronteiras CONFORMES (CLASSIFICACAO l.58-60) × tratamentos residuais ADIADOS à ativação (l.62) | [DECISÃO NECESSÁRIA] | Andraus no gate (r8-l); o Plan não decide |
| Atos de governança de ontologia em runtime | [DECISÃO NECESSÁRIA] | Dependem de K-001 (ABERTA); v1.0: conjunto vazio ⇒ `ONTOLOGY_CHANGE_NOT_GOVERNED` (fail-closed, não fecha K-001) |
| Política de volume do log `kg_gate_decision` | [DECISÃO NECESSÁRIA] | v1.0: sem descarte (completude); nunca por deleção |
| Estado do BL-003 após este Plan | [DECISÃO NECESSÁRIA] | Andraus; RMR-001 não editado |
| Componente "Cognitive Ontology" separado | [DECISÃO NECESSÁRIA] | Ontologia DENTRO da SPEC-006 (Q-ABERTURA-4) |
| Estados do Blackboard p/ não-hipótese; fórmula/pesos/limiares e pesos por ativo do Conviction Vector; estado por agente; ciclo P12; EARS multi-condição; convicção macro-global | [DECISÃO NECESSÁRIA] | **M-001, J-001, N-001, G-001, K-001, C-001, WF-D03 — EM ABERTO** — não tocadas |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] ROADMAP.md lido: SPEC-006 em §6/§21/§26; FASE 3; após SPEC-005 BASELINE; l.177 "Resolve H-001" registrada como divergência.
[x] atomic-spec.md lido: v1.5 (§3 CRITICAL·D0–D7; §10.2 l.238 E3; §10.6 l.315; ENF-07 l.273; gaps l.393; INV-04 l.404; §15).
[x] RMR-001: itens ATIVADO = BL-003/BL-011 (l.102/l.110), encaminhados ao gate desta Spec — Nota de gate; RMR-001 não editado.
[x] DHR-SPEC006-002 aplicada: Opção 2; núcleo com regra única de admissão; contratos (a)/(b)/(c), critério de (a) e selo fora de escopo.
[x] Nenhum invariante congelado violado; INV-04/05/06/07/09/10 reforçados.
[x] Constitution Check CC-01..CC-12 (N/A justificados CC-06/07/12).
[x] Disciplinas N8–N17: §7-bis Bloco C.
[x] [EXTERNO] classificadas; nenhuma adotada; sem pesquisa web nova nesta rodada (correções internas ancoradas no repositório).
[x] RULE-ECC-05: não-incidência; WF-D03 não tocada.
[x] Spec sem implementação; Tasks adiadas.
[x] Critérios em EARS (24; leitura sob D4.0 declarada — r8-a); 13 BASpecs com Classe (CC-11); toda RULE citada existe ou é
    [PROPOSTA]; todo código (27 de rejeição + `DUPLICATE_NO_OP`) definido em D4 e posicionado em D4.0.
[x] Fonte única dura: obrigatoriedade (todo record_kind)/predicado/classe/ordem/código só em D4; schema só com campos e tipos.
[x] Profundidade D0–D7 + D8: D4.0–D4.20; D5; D6; D7 x26; D8 x27; D9.
[x] Enforcement Contract em todo efeito (EC-CKG-001..006); E3 em 001..005; E1 em 006 (reavaliado — R8-1: negação de gravação
    por consulta governada por EC-003 E3); ENF-07 executável por input_snapshot, limiar = gap aberto.
[x] Etiquetagem e status epistemológico aplicados; documentado ≠ homologado.
[x] CONS-01: H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001 permanecem ABERTAS.
[x] Achados da rodada 7 (checks.md §11) e da rodada 8 (R8-1..R8-4; r8-a..r8-m; 11 interpelações — checks.md §13) tratados;
    r8-l registrado como [DECISÃO NECESSÁRIA] (não decidido).
[x] Integridade: linhas reverificadas nesta rodada — CEM-001 l.428 (texto citado em ADV-25), l.446-456; atomic-spec §10.2
    l.228-240 (E1/E3; base da reavaliação do EC-006); CLASSIFICACAO-COLISOES l.58-62 (r8-l); DHR-SPEC006-002 §1-§3; RMR-001
    ATIVADO = BL-003/BL-011 (l.191). Citações herdadas da v1.7 (CEM-001 l.257-283/494/608-615; SPEC-004 plan l.338/381/689;
    SPEC-005 plan l.88/859/971) não alteradas.
[x] 4Es na ordem; Conformidade > Eficácia. Latência não material (consulta opcional/não-bloqueante).
[x] "VERIFY" ≠ CONFORME ≠ homologação. §7-bis preenchido (Blocos A–D).
[ ] Gate determinístico e demais scripts: NÃO executados por mim (sem Bash) — checks.md §12 para o Orquestrador.
```

---

**Pronto para revisão.**

**[DECISÃO NECESSÁRIA] / abertas (não fechadas — CONS-01):** lista única na tabela "Etiquetagem e Status Epistemológico". H-001 permanece ABERTA; J-001/N-001/M-001/G-001/K-001/C-001/WF-D03/ECC-03-001 não tocadas.

Carregado para o Revisor (rodada 9):
- **Desenho declarado:** a v1.0 não admite conhecimento (D4.15); verificáveis são predicados e fixtures; admissão positiva = fora de escopo (emendas E-a..E-e). Toda operação tem classe e posição em D4.0.
- **Fonte única dura:** D4.0–D4.20; o schema não declara obrigatoriedade. Rastreabilidade de R8-1..R8-4, r8-a..r8-m e das 11 interpelações: checks.md §13 (rodada 7: §11).
- **Pendência de Andraus (r8-l):** leitura de R-04..R-06 (CONFORME × ADIADOS) — registrada, não decidida.
