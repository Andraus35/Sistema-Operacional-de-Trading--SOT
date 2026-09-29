# SPEC-002 — Evidence & Evidence Provenance Harness

| Campo | Valor |
|---|---|
| ID | SPEC-002 — Evidence & Evidence Provenance Harness (camada Harness/operacional sobre CEM-001) |
| Versão | 1.0 (candidata — NÃO baseline) |
| Status | **PROPOSTA** — Plan candidato. Abertura HOMOLOGADA (DHR-SPEC002-001, 2026-09-29); o Plan ainda não foi homologado (próximo gate: `DHR-SPEC002-002`). Documentado ≠ homologado (TRACE-06). |
| Fonte | ROADMAP §4 (SPEC-002, linhas 138-142); `specs/features/SPEC-002/research.md` (Dossiê de abertura HOMOLOGADO 2026-09-29); DHR-SPEC002-001; atomic-spec.md **v1.5**; **RULE-ECC-01/02** (Especificação Emergente) |
| Complexidade | **CRITICAL** [FONTE: ROADMAP §4 linha 139; DHR-SPEC002-001 §2 DN-2] |
| Profundidade-alvo | **D0–D8** (standard + adversarial — CRITICAL) [FONTE: DHR-SPEC002-001 §2 DN-2; AGENTS.md §4 tabela PINADA] |
| Profile (Claude Code) | standard + adversarial (CRITICAL) — §7-bis aplicado (obrigatório CRITICAL), D8 pleno |
| Nível de maturidade-alvo (desta Spec) | **L3 Testável** — teto de spec-first para CRITICAL (RULE-MM-04; atomic-spec §7) |
| Método | atomic-spec.md **v1.5** (LOTE RULE-REG-001 incorporado; DHR-SPEC002-001 §5) |
| Regime normativo citado | **RULE-ECC-01/02** (abertura/Dossiê), **RULE-ECC-04** (captura verbatim), **RULE-MECH-01..04** (Classe por BASpec — INCIDE), **RULE-PD-01** (PD-xx — NÃO incide, infraestrutural), **RULE-HD-01..04** (Herança/Delta), **GMC-001** (evolução Categoria A do CEM-001 — DN-1) |
| Classe predominante (orientação de leitura — não vinculante; §10.6) | **D** (Determinístico), com **H** em publicação (gate de conformidade de contrato) e **C** em travas constitutivas (anti-INV-04, invalidação irreversível) |
| Posição no caminho crítico | FASE 1 — Núcleo Cognitivo, posição 1; após FASE GOV concluída (019/020/021 homologadas), antes de SPEC-003 [FONTE: ROADMAP §21; §4 linha 239] |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-09-29 |
| Abertura | Dossiê de Pesquisa homologado por Andraus em **2026-09-29** (research.md; DHR-SPEC002-001); Plan iniciado no mesmo dia, dentro da validade do Dossiê (ECC-VAL-001 permanece **aberta** — sem prazo geral fixado; ver Decisões abertas) |

Status: **PROPOSTA** (candidata a baseline). Complexidade: CRITICAL. Profundidade-alvo: D0–D8. [FONTE: ROADMAP §4; DHR-SPEC002-001; AGENTS.md §4]

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-29 | Plan candidato inicial. Camada Harness/operacional de proveniência/qualidade/ciclo-de-vida de evidência SOBRE CEM-001 (não redefine — CONST-01). Incorpora DN-1 (confiabilidade histórica do produtor = extensão Categoria A do CEM-001 via GMC-001), DN-2 (D0–D8), DN-3 (gancho "ausente", semântica deferida). 12 BASpecs (EPH-001..012) com Classe (RULE-MECH-01). §7-bis completo (CRITICAL). |

---

## Nota de gate (passo 11-bis / RMR-001) — itens verificados nesta redação

[FONTE: RMR-001 §6; ROADMAP §23 passo 11-bis]

- **RULE-REG-001** — gatilho `spec:SPEC-002 em redação` **já disparado e SANADO** pela abertura (DHR-SPEC002-001 §5): as 10+1 famílias RULE (RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET) estão registradas fisicamente em `governance/RULES.md` e o método subiu a **v1.5**. Sem ação nova desta redação. [FONTE: DHR-SPEC002-001 §5]
- **BL-012 (MC-COG-001)** — gatilho `spec:SPEC-002 homologada (consolidação cognitiva v1.5)` dispara **na homologação deste Plan** (não agora). Registrado como **IMINENTE**, não ATIVADO por esta redação. [FONTE: DHR-SPEC002-001 §3 item 4]
- **BL-008** — auditoria retroativa da SPEC-001 — segue `ATIVADO`, independente desta redação; não bloqueia. [FONTE: RMR-001]
- **STRUCT-11 (`validate_spec_sot.py`)** — a SPEC-002 cita RULE-ECC-01/02; `research.md` (Dossiê) está presente na pasta com a seção "Dossiê de Pesquisa" — check determinístico satisfeito. [FONTE: research.md]
- Nenhum item `ATIVADO` fica sem encaminhamento por esta redação. Painel §6 no ato da abertura: "Itens em ATIVADO: nenhum pendente para a SPEC-002". [INFERÊNCIA — coerente com RMR-001 §4]

> **Pendências de execução para o coordenador (sem Bash neste agente — RULE-MET-01, não fabrico resultado):** `python scripts/validate_spec_sot.py specs/features/SPEC-002/plan.md`, `python scripts/check_refs.py`, `python scripts/check_doc_sync.py`, `python scripts/backlog_triggers.py`, `python scripts/build_map.py` (novos `.md` em `specs/features/SPEC-002/`). Não executei; reporto como pendência.

---

## Constitution Check (CC-01..CC-12 — atomic-spec §10.5 v1.5)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** a SPEC-002 é **infraestrutural/neutra de domínio** — carrega o *envelope* de proveniência de evidência produzida por qualquer escola, sem realizar análise de nenhuma escola nem inverter a hierarquia. Não cria hipótese estrutural (isso é do Structural Agent/Elliott, SPEC-010) nem executa (ICT/SPEC-013, INV-02). O metadado de conflito (EPH-009) apenas **registra** o substrato para que `directional_conflict` (RULE-005, Elliott×SMC) seja detectável downstream; **não resolve** conflito (Synthesis). A camada **protege** a hierarquia; não a toca. [INFERÊNCIA; FONTE: CEM-001 Princípio 1; INV-01/INV-02]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** **CONST-01 preservado.** A SPEC-002 constrói **SOBRE** CEM-001 (idioma canônico, INV-10) — não redefine nenhum de seus campos, estados ou transições. A confiabilidade histórica do produtor (DN-1) entra como **extensão Categoria A (aditiva)** do CEM-001 **via GMC-001**, sem alterar semântica existente. CCM-001 permanece **pendente (SPEC-003)** — nenhum limiar/fórmula de convicção é fixado aqui. Ver Herança/Delta e EPH-003. [FONTE: CONST-01; CEM-001; GMC-001 Cap.3; DHR-SPEC002-001 §2 DN-1]
- [x] **CC-03 — Conviction Vector:** dimensionalidade=8 permanece **fechada**; fórmula/pesos/limiares definitivos = **J-001 (aberto/pendente)**. A SPEC-002 **não** computa convicção nem fixa qualquer limiar numérico ligado a convicção. A confiabilidade-de-fonte (DN-1/EPH-003) é **metadado descritivo/filtro** e **NUNCA** entra como dimensão do Conviction Vector — trava explícita em EPH-004 (**INV-04**). [FONTE: INV-03; INV-04; J-001 pendente]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada. Custo/qualidade-de-fonte não entram em nada análogo a convicção (INV-04 = Salvaguarda 4 do §10, honrada por EPH-004). Nenhuma salvaguarda de Sinal (§11: invalidação, score, conflito direcional, convicção, R:R) é tocada — a SPEC-002 não emite sinal. Economicidade (4Es) nunca rebaixa os pisos de enforcement E2/E3. [FONTE: INV-04; CEE-001 §10/§11]
- [x] **CC-05 — Complexidade declarada:** **CRITICAL, D0–D8** (DHR-SPEC002-001 §2 DN-2). Maturidade-alvo = L3 (teto spec-first).
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan, não Engineering Card. Os campos §59 e a cadeia §60 tornam-se obrigatórios quando as Tasks/Engineering Cards forem produzidas (BUILD adiado — atomic-spec §14). Omissão justificada. [FONTE: atomic-spec §8.1/§14]
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem provida pela cadeia ROADMAP §4 → Dossiê (research.md, homologado) → esta Spec.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver "Herança / Delta"); INHERITS/ADDED preenchidos com ID+versão (RULE-HD-04); REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). Eixo **VERTICAL (RULE-HV)** avaliado: a SPEC-002 herda de um **modelo canônico** (CEM-001), não é decomposição *micro* de um *macro* pai — herança obrigação-a-obrigação sobre o contrato canônico; ver nota na seção de Herança. [FONTE: EUA-E04 §8.3; RULE-HD-01..04; RULE-HV]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI, INDETERMINADO, INV-EPI):** aplicado integralmente (ver §7-bis Bloco C, completo — não resumido). Distinção FATO NORMATIVO / FATO ARQUITETURAL / PROPOSTA / INFERÊNCIA / EXTERNO explícita; fontes web = DADO ([EXTERNO], research.md), nunca baseline; nenhuma hipótese tratada como fato; afirmações causais com mecanismo (RULE-CAU-01); sem falsa precisão; INDETERMINADO usado onde a pesquisa foi inconclusiva. [FONTE: RULE-EPI-01..03; RULE-CAU-01; research.md §2 nota RULE-MET-01]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM):** **N/A justificado** — o domínio da SPEC-002 é proveniência/qualidade/ciclo-de-vida de evidência (infraestrutura), sem terminologia concorrente por escola de análise técnica. Onde termos externos colidem (Admiralty "reliability/credibility", W3C PROV "Entity/Activity/Agent", MiFID "bitemporal"), a colisão é registrada e o rótulo **rejeitado como baseline** (research.md §6.3), não adotado — só o **princípio** é adaptado. Nenhum termo canônico do GLOSSARIO/CEM-001 redefinido (RULE-SEM-04). [FONTE: RULE-SEM-01/04; research.md §6.3]
- [x] **CC-11 — Classe/Mecanismo por BASpec (RULE-MECH-01, §10.6):** **INCIDE** (SPEC-002 ≥ SPEC-002; a Spec cita RULE-MECH-01 no próprio texto — ver D2/D3). Cada BASpec com efeito declara **Classe (D/H/P/C)**, **Mecanismo**, **critério 4Es** (RULE-MECH-02) e **bounded loop + gate de saída** onde H/C (RULE-MECH-03). Nenhuma Classe C em BASpec de risco baixo (EPH-004/007 são E3). [FONTE: RULES.md RULE-MECH-01..04; atomic-spec §10.6]
- [x] **CC-12 — Princípios de Domínio (RULE-PD-01, §10.7):** **N/A justificado** — a SPEC-002 é **infraestrutural/neutra de domínio** (CEM-001 Princípio 1), **não** define escopo de especialidade de mercado (Elliott/Fibonacci/SMC/ICT). Coerente com o quadro das 6 lentes do Dossiê (research.md §3: todas não-aplicáveis com justificativa). Nenhum `PD-xx` proposto. [FONTE: atomic-spec §10.7; RULE-PD-01; research.md §3/§7.5]

**Checklist de consistência principiológica (GPR-001 §15):** PC-01 (hierarquia) protegida, não tocada; PC-02/INV-05 (SOT não executa) reforçada (a camada **representa/versiona** evidência, não decide nem executa — RULE-DEC-01); piso de convicção não tocado (nenhum limiar de convicção — J-001 aberto); 4Es na ordem (Conformidade>Eficácia>Efetividade>Eficiência>Economicidade; Economicidade não rebaixa E2/E3); rastreabilidade e explicabilidade (toda publicação/transição registra origem, timestamp e justificativa — CEM-001 Cap.4/5); preservação da incerteza honrada por INDETERMINADO e pelo gancho "ausente" (EPH-005). Item CLASSE-MECH-001 do §15: Classe por BASpec (CC-11). Item PRINC-BID-001 do §15: N/A (infraestrutural, CC-12).

**Disciplinas cognitivas N8–N17 incidentes:** RULE-EPI (hipótese≠fato; INDETERMINADO), RULE-MET-01 (não-fabricação — nenhum resultado de execução inventado; nenhuma decisão fechada que não é minha), RULE-DEC-01 (decisão≠execução — a camada de evidência não decide sinal), RULE-CAU-01 (afirmações causais com mecanismo), RULE-SEM (terminologia concorrente rejeitada como baseline), RULE-UNC (incerteza localizada, não contaminante).

---

## Herança / Delta (§8.3 — EUA-E04)

```
HERANÇA / DELTA — SPEC-002

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO — RULE-HD-04):
  - Modelo canônico: CEM-001 v1.0 (BASELINE — Canonical Evidence Model) — em particular:
      • Contrato de 4 camadas (Identidade / Origem / Conteúdo Cognitivo / Rastreabilidade) — Cap.3
      • Campos: Evidence ID/Version, Creation Timestamp, Status; Producer Type (AGENT/ENGINE),
        Producer ID, Evidence Origin Type (PRIMARY/DERIVED); Domain (Governed Enum GMC-001),
        Observation, Interpretation, Technical Rationale, Evidence Strength (float 0-1, ≠ Convicção),
        Timeframe Reference (enum estático), Market Context (Governed Enum); Source Reference, Lineage
      • Ciclo de vida: estados ACTIVE/SUPERSEDED/INVALIDATED/ARCHIVED + transições permitidas/proibidas
        (INVALIDATED/ARCHIVED/SUPERSEDED → ACTIVE PROIBIDAS) — Cap.4
      • Imutabilidade pós-publicação (Status = único campo mutável) — Cap.4
      • Evento *Evidence Invalidated* + avaliação de impacto pelo Fusion Engine (sem cascata
        automática) — Cap.4/5; propagação via EC-COG-005 (Cognitive Event Bus) — Cap.6
      • Cognitive Trace Reconstruction / Cognitive Depth = capacidades do Knowledge Graph (não campos) — Cap.5
      • Níveis de conformidade Producer/Consumer/Repository — Cap.8; princípios de Neutralidade (1),
        Objetividade (2), Explicabilidade (3), Rastreabilidade (4), Independência (5), Reutilização (6),
        Refutabilidade (7), Interoperabilidade (8) — Cap.1
  - Governança de evolução do canônico: GMC-001 v1.0 (BASELINE) — Categorias A/B/C (Cap.3);
      Governed Enumerations sob GMC-001; processo formal de proposição/auditoria/homologação (Cap.5)
  - Método: atomic-spec.md v1.5 — BASpec (§1), D0–D9 (§2), EARS (§4), F.1–F.4 (§5), Enforcement
      E0–E3 (§10), Classe/Mecanismo (§9/§10.6), TRACE-06 (§11), Dossiê/lentes (§15)
  - Modelo de hipótese (referência de fronteira): CHM-001 v1.0 (BASELINE) — vínculo evidência→hipótese
      por REFERÊNCIA (a SPEC-002 não redefine a hipótese; INV-06/INV-10)
  - Enforcement: ENF-01..08 — ênfase em ENF-03 (Detector ≠ Gate), ENF-04 (fail-closed E3 irreversível)
  - Invariantes: INV-04 (custo/qualidade-de-fonte nunca no Conviction), INV-06 (Evidência ≠ Observação),
      INV-07 (versionamento monotônico — nada deletado), INV-09 (sem baseline informal),
      INV-10 (CEM-001 = idioma canônico), INV-03 (Conviction 8D fechada; definitivos = J-001 aberto)
  - Regras: RULE-004 (evidências causalmente relacionadas contadas como uma — substrato downstream),
      RULE-005 (conflito direcional — substrato downstream), RULE-009 (resposta não é só "comprar/vender")

ADDED (delta local — o que esta spec acrescenta como camada Harness/operacional):
  - Protocolo OPERACIONAL de proveniência: criar/publicar/superseder/invalidar/arquivar evidência
    com gate determinístico de conformidade de contrato CEM-001 (EPH-001, EPH-006, EPH-007)
  - Proveniência da transformação `Fonte → Dado → Evidência`: granularidade ferramenta/Skill produtora
    + fronteira operacional Observação(Skill) ≠ Evidência(Agente) (EPH-002; INV-06)
  - Dois eixos independentes de qualidade (princípio Admiralty ADAPTADO, não os códigos A-F/1-6):
    confiabilidade histórica do produtor (DN-1, extensão Categoria A do CEM-001 via GMC-001) SEPARADA
    da força do relato (Evidence Strength, já em CEM-001) (EPH-003)
  - Trava constitutiva anti-INV-04: confiabilidade-de-fonte NUNCA entra no Conviction Vector (EPH-004)
  - Taxonomia operacional favorável / contraevidência / inconclusiva + gancho "ausente" (DN-3, semântica
    DEFERIDA a SPEC-010+) (EPH-005)
  - Metadado de independência/correlação (substrato de RULE-004 para SPEC-003; NÃO computa confluência) (EPH-008)
  - Metadado de conflito (substrato de RULE-005; NÃO resolve conflito) (EPH-009)
  - Metadado de temporalidade/staleness (DEFERE fórmula de decaimento a J-001/SPEC-003) (EPH-010)
  - Vínculo operacional evidência→hipótese POR REFERÊNCIA (CHM-001) (EPH-011)
  - Suporte à auditabilidade/reconstrução bitemporal ("o que se sabia e quando") append-only
    (DEFERE mecanismo físico a KG/SPEC-006 e auditoria/SPEC-041) (EPH-012)
  - Declaração de Classe (D/H/P/C) por BASpec com efeito (RULE-MECH-01/CC-11)

MODIFIED (especialização de regra herdada):
  - (nenhuma regra herdada é modificada em texto) — a SPEC-002 ESPECIALIZA operacionalmente o CEM-001
    sem alterar seu contrato. A extensão DN-1 é ADITIVA (Categoria A, GMC-001), não modificação.

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

> **Nota de eixo de herança (CC-08 vs RULE-HV — [INFERÊNCIA]):** o bloco acima é herança **obrigação-a-obrigação** (EUA-E04 §8.3) sobre um **modelo canônico** (CEM-001). O eixo VERTICAL macro→micro (RULE-HV, conservação-como-conjunto) é o caso de decomposição de um componente-pai em filhas; aqui a relação é "camada Harness operacional constrói sobre contrato canônico" — o dever é **conservar cada obrigação do CEM-001** (nenhuma suprimida/enfraquecida — RULE-HD-03) e **não contradizê-la** (RULE-HD-02). A conservação-como-conjunto (Contrato de Herança Vertical) só será redigida como norma escrita junto da SPEC-019 (escopo já homologado, conteúdo pendente — não é decisão em aberto, é conteúdo futuro; §7-bis Bloco B). [INFERÊNCIA — a confirmar pelo Revisor]

---

## D0 — Missão (Intenção)

A SPEC-002 especifica **a camada Harness/operacional que opera o ciclo de vida, a proveniência e a qualidade intrínseca das Evidências Cognitivas do SOT**, construindo **sobre** o CEM-001 (idioma canônico, baseline — INV-10/CONST-01) sem redefini-lo. Define: (1) o **protocolo operacional** de criar, publicar, superseder, invalidar e arquivar evidência, com gate determinístico de conformidade ao contrato CEM-001 e produtor autorizado (fail-closed em publicação incompleta); (2) a **proveniência da transformação** `Fonte → Dado → Evidência` — qual ferramenta/Skill produziu, preservando a fronteira Observação(Skill) ≠ Evidência(Agente) (INV-06); (3) os **dois eixos independentes de qualidade** — confiabilidade histórica do produtor (metadado descritivo, extensão Categoria A do CEM-001 via GMC-001 — DN-1) SEPARADA da força do relato específico (Evidence Strength, já canônico) — com a **trava** de que a confiabilidade da fonte **nunca** entra no Conviction Vector (INV-04); (4) a **taxonomia operacional** favorável / contraevidência / inconclusiva, mais o **gancho** "ausente" cuja semântica é DEFERIDA (DN-3); (5) os **metadados de substrato** — independência/correlação (para RULE-004 downstream), conflito (para RULE-005 downstream) e temporalidade/staleness — que a camada **registra** mas **não interpreta**; (6) o **vínculo evidência→hipótese por referência** (CHM-001) e o **suporte à auditabilidade/reconstrução bitemporal** append-only (delegando o mecanismo físico ao KG/SPEC-006 e à auditoria/SPEC-041). [FONTE: ROADMAP §4 linhas 138-142; research.md §6.2/§7.2; DHR-SPEC002-001]

A SPEC-002 é o **envelope** da evidência; o **conteúdo** analítico (a interpretação de escola) pertence aos agentes produtores (SPEC-010..014); a **fusão/convicção** pertence à SPEC-003. É a camada que todo agente downstream consome — seu *blast radius* motiva o alvo D0–D8 (integridade/anti-adulteração de proveniência — DN-2).

**O que a Missão NÃO é (fronteira):**
- Não **redefine** o CEM-001 (CONST-01) — constrói sobre ele. [FONTE: CONST-01]
- Não realiza **fusão multi-fonte** nem calcula **convicção** → SPEC-003 (Fusion Engine → Conviction Engine; B-001 fechada). A camada **prepara** evidência com proveniência completa; não funde. [FONTE: ROADMAP §4 linha 149]
- Não define **armazenamento físico** (Blackboard/KG) → SPEC-004 (M-001 aberta) / SPEC-006 (H-001 aberta). [FONTE: J-001/M-001/H-001 pendentes]
- Não define **fórmula de qualidade/aging/peso numérico** → CCM-001/J-001 (SPEC-003, aberto). [FONTE: J-001 pendente]
- Não especifica os **agentes que produzem evidência** → SPEC-010..014.
- Não emite **Signal Package**/risco (INV-05) → família RISK-SPEC. [FONTE: INV-05]
- Não define **mecanismos criptográficos/on-chain** de tamper-evidence (rejeitados como baseline — Economicidade; research.md §6.3).

**Status epistemológico:** a SPEC-002 é FATO ARQUITETURAL candidato a baseline. CEM-001 v1.0, GMC-001 v1.0, CHM-001 v1.0, atomic-spec v1.5, INV-*, ENF-*, RULE-MECH-01..04, RULE-HD-01..04, RULE-004/005/009 são FATO NORMATIVO. As RULE-EPH-* propostas abaixo são **[PROPOSTA]**. Fontes externas (research.md §2, SRC-01..05) são **[EXTERNO]** — DADO, nunca baseline; documentado ≠ homologado (TRACE-06).

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| S1 | **Protocolo operacional** de criar/publicar/superseder/invalidar/arquivar evidência sobre o ciclo de vida CEM-001 (gate de conformidade + produtor autorizado; fail-closed incompleto) | CEM-001 Cap.4/6; research.md §6.2 |
| S2 | **Proveniência da transformação** `Fonte → Dado → Evidência` — ferramenta/Skill produtora; fronteira Observação(Skill) ≠ Evidência(Agente) | INV-06; ROADMAP §4 linha 142; SRC-04 |
| S3 | **Dois eixos independentes de qualidade**: confiabilidade histórica do produtor (DN-1, extensão Categoria A CEM via GMC-001) × força do relato (Evidence Strength) | DHR-SPEC002-001 §2 DN-1; SRC-02 |
| S4 | **Trava anti-INV-04**: confiabilidade-de-fonte NUNCA entra no Conviction Vector | INV-04; DHR-SPEC002-001 §2 DN-1 |
| S5 | **Taxonomia operacional** favorável / contraevidência / inconclusiva + **gancho "ausente"** (semântica deferida) | RULE-009; DHR-SPEC002-001 §2 DN-3 |
| S6 | **Metadado de independência/correlação** (substrato de RULE-004 para SPEC-003; NÃO computa confluência) | RULE-004; SRC-05; research.md §6.2 |
| S7 | **Metadado de conflito** (substrato de RULE-005 para detecção downstream; NÃO resolve conflito) | RULE-005; research.md §6.2 |
| S8 | **Metadado de temporalidade/staleness** (DEFERE fórmula de decaimento) | J-001; SRC-05 (temporal decay) |
| S9 | **Vínculo evidência→hipótese por referência** (CHM-001; INV-06/INV-10) | CHM-001; ROADMAP §4 linha 142 |
| S10 | **Suporte à auditabilidade/reconstrução bitemporal** append-only (mecanismo físico delegado a KG/SPEC-006, auditoria/SPEC-041) | INV-07; SRC-03; CEM-001 Cap.5 |
| S11 | **Enforcement Contracts** por comportamento com efeito + **Classe por BASpec** (RULE-MECH-01) | atomic-spec §10; RULE-MECH-01 |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Redefinir CEM-001 (campos/estados/transições/contrato) | **CEM-001** (BASELINE) | CONST-01; construir sobre, não redefinir; INV-10 |
| Fusão multi-fonte + fórmula de convicção | **SPEC-003 / J-001 / CCM-001** | B-001 fechada (Fusion→Conviction→Synthesis); J-001 aberto — não fixar |
| Armazenamento físico (Blackboard / KG) | **SPEC-004 (M-001) / SPEC-006 (H-001)** | Decisões abertas; não antecipadas (CONS-01) |
| Fórmula de aging/peso/confiabilidade numérica | **CCM-001 / J-001 (SPEC-003)** | J-001 aberto — metadado, não fórmula |
| Semântica de "quando a ausência de evidência é significativa" | **SPEC-010+ (Dossiê de cada consumidora)** | DN-3: só o gancho agora; decisão de timing (padrão RISK-LEV-001) |
| Agentes produtores de evidência | **SPEC-010..014** | Conteúdo de escola ≠ envelope de proveniência |
| Signal Package / risco / sizing / R:R | **família RISK-SPEC** | INV-05; evidência não contém decisão/execução (CEM restrição) |
| Mecanismos on-chain / hash-chain criptográfico como baseline | — | Economicidade (4Es); append-only + KG já entregam auditabilidade (research.md §6.3) |
| Reconstrução expandida da cadeia cognitiva (Cognitive Trace Reconstruction) e Cognitive Depth | **Knowledge Graph / SPEC-006** | CEM-001 Cap.5: capacidades do KG, não campos armazenados |

---

## D2 — Regras

> **Etiqueta:** as RULE-EPH-* abaixo são **[PROPOSTA]** — tornam-se normativas apenas na homologação de Andraus + registro no `governance/RULES.md` pelo Controlador (nova seção "Regras de Evidence Harness (RULE-EPH)"). Até lá, não são invocáveis como FATO NORMATIVO (RULE-HG-02). As RULE/INV/ENF citadas como fundamento (**CEM-001**, **GMC-001**, **CHM-001**, **RULE-MECH-01..04**, RULE-004/005/009, ENF-01..08, INV-04/06/07/10) **já existem** e são FATO NORMATIVO.

```
RULE-EPH-01: Toda publicação de Evidência pela camada Harness DEVE passar por gate determinístico de
             conformidade ao contrato CEM-001 (Cap.3: identidade, origem, conteúdo, rastreabilidade
             completos) e de produtor autorizado (CEM-001 Cap.2/6). Publicação incompleta é REJEITADA
             (fail-closed). [Fonte: CEM-001 Cap.3/6 "proibido publicar Evidências incompletas"; ENF-04]  [PROPOSTA]

RULE-EPH-02: A camada Harness DEVE registrar a proveniência operacional da transformação
             Fonte→Dado→Evidência, incluindo a ferramenta/Skill produtora, preservando a fronteira
             Observação(Skill) ≠ Evidência(Agente). Uma Observação de Skill NÃO DEVE ser publicada
             como Evidência sem interpretação de Agente. [Fonte: INV-06; CEM-001 Cap.2; SRC-04]  [PROPOSTA]

RULE-EPH-03: A camada Harness DEVE tratar confiabilidade histórica do produtor e força do relato
             (Evidence Strength) como DOIS EIXOS INDEPENDENTES; um não DEVE influenciar o outro. A
             confiabilidade histórica é modelada como extensão Categoria A do CEM-001 via GMC-001
             (aditiva, sem alterar semântica existente). [Fonte: DHR-SPEC002-001 §2 DN-1; SRC-02; GMC-001 Cap.3]  [PROPOSTA]

RULE-EPH-04: A confiabilidade histórica do produtor é metadado descritivo/filtro e NUNCA DEVE entrar
             como dimensão, insumo ou peso do Conviction Vector (INV-04). [Fonte: INV-04; DHR-SPEC002-001 §2 DN-1; CONS-01]  [PROPOSTA]

RULE-EPH-05: A taxonomia operacional de evidência DEVE distinguir favorável / contraevidência /
             inconclusiva e DEVE prover um tipo/estado "ausente" como gancho de extensibilidade; a
             semântica de quando a ausência é significativa NÃO DEVE ser fixada nesta Spec (deferida a
             SPEC-010+). [Fonte: RULE-009; DHR-SPEC002-001 §2 DN-3]  [PROPOSTA]

RULE-EPH-06: Evidência é APPEND-ONLY: atualização de conhecimento cria NOVA evidência e transita a
             anterior para SUPERSEDED, preservando Lineage; NENHUMA evidência DEVE ser deletada
             (INV-07; CEM-001 Cap.4). [Fonte: INV-07; CEM-001 Cap.4]  [PROPOSTA]

RULE-EPH-07: A invalidação de Evidência DEVE seguir as transições permitidas do CEM-001 (ACTIVE→
             INVALIDATED; INVALIDATED→ACTIVE PROIBIDA), emitir o evento *Evidence Invalidated* e
             INICIAR (não executar em cascata automática) avaliação de impacto sobre derivadas pelo
             Fusion Engine. Detector ≠ Gate. [Fonte: CEM-001 Cap.4/5; ENF-03]  [PROPOSTA]

RULE-EPH-08: A camada Harness DEVE registrar metadados de independência/correlação (substrato de
             RULE-004) e de conflito (substrato de RULE-005) com granularidade suficiente para
             detecção DOWNSTREAM, sem computar confluência nem resolver conflito nesta Spec.
             [Fonte: RULE-004; RULE-005; RULE-SY-001; research.md §6.2]  [PROPOSTA]

RULE-EPH-09: A camada Harness DEVE suportar temporalidade/staleness como metadado, sem fixar qualquer
             fórmula de decaimento/aging (deferida a J-001/SPEC-003). [Fonte: J-001; SRC-05; CONS-01]  [PROPOSTA]

RULE-EPH-10: O vínculo evidência→hipótese DEVE ser por REFERÊNCIA (CHM-001), preservando a
             independência da evidência (uma evidência pode sustentar múltiplas hipóteses — CEM-001
             Princípio 5). A camada NÃO DEVE redefinir a hipótese. [Fonte: CHM-001; CEM-001 Princípio 5; INV-10]  [PROPOSTA]
```

---

## Critérios de Aceitação (EARS)

1. Quando um produtor tenta publicar uma Evidência com qualquer camada do contrato CEM-001 incompleta, a camada Harness DEVE rejeitar a publicação (fail-closed) e registrar o motivo.
2. Quando uma Observação de Skill é submetida como Evidência sem interpretação de Agente, a camada Harness DEVE recusar a publicação (fronteira INV-06 preservada).
3. Quando uma Evidência é publicada, a camada Harness DEVE registrar sua proveniência operacional (Fonte→Dado→Evidência, ferramenta/Skill produtora) de forma imutável após a publicação.
4. Quando a confiabilidade histórica do produtor é atribuída a uma Evidência, a camada Harness DEVE mantê-la como metadado descritivo independente da Evidence Strength e NÃO DEVE roteá-la para nenhum cálculo de convicção.
5. Quando qualquer rotina tenta usar a confiabilidade-de-fonte como dimensão/insumo/peso do Conviction Vector, a camada Harness DEVE bloquear o uso (trava INV-04, efeito E3).
6. Quando o conhecimento de uma Evidência precisa ser atualizado, a camada Harness DEVE criar uma nova Evidência e transitar a anterior para SUPERSEDED preservando a Lineage — NUNCA deletar (INV-07).
7. Quando uma Evidência ancestral é invalidada, a camada Harness DEVE emitir o evento *Evidence Invalidated* e iniciar (não executar em cascata automática) a avaliação de impacto sobre derivadas.
8. Quando uma tentativa de transição de estado proibida pelo CEM-001 (ex.: INVALIDATED→ACTIVE) é submetida, a camada Harness DEVE rejeitá-la (fail-closed, integridade histórica).
9. Quando uma Evidência é registrada, a camada Harness DEVE gravar os metadados de independência/correlação e de conflito necessários à detecção downstream, sem computar confluência nem resolver conflito.
10. Quando a taxonomia operacional é aplicada, a camada Harness DEVE permitir representar evidência favorável, contraevidência, inconclusiva e "ausente" — sem interpretar a significância da ausência (deferida).

---

## D3 — Comportamento (BASpecs com Classe/Mecanismo — RULE-MECH-01/CC-11)

> Toda BASpec com efeito declara **Classe (D/H/P/C)** (RULE-MECH-01), **Mecanismo**, **critério 4Es** (RULE-MECH-02) e — onde H/C — **bounded loop** e **gate de saída** (RULE-MECH-03).

### BASpec-EPH-001 — Publicar Evidência com gate de conformidade de contrato (fail-closed)

```
BASpec-EPH-001:
  QUANDO:       Um produtor autorizado submete uma Evidência para publicação na camada Harness
  ENTÃO:        A camada valida a completude das 4 camadas do contrato CEM-001 (Cap.3) e a autorização
                do produtor (Cap.2/6); se completa e autorizada → publica (evento *Evidence Created*);
                se incompleta ou produtor não autorizado → REJEITA a publicação (fail-closed) e registra o motivo
  PORQUE:       CEM-001 proíbe publicar Evidências incompletas/sem rastreabilidade; a integridade do
                idioma canônico (INV-10) exige gate determinístico de conformidade antes do efeito
  REFERÊNCIA:   RULE-EPH-01; CEM-001 Cap.3/6; ENF-04
  CLASSE:       H (Híbrido — o produtor/Agente pode ter raciocínio; a publicação passa por gate de saída determinístico)
  MECANISMO:    Gate determinístico verifica presença de todos os campos obrigatórios do contrato + produtor ∈ conjunto autorizado
  CRITÉRIO 4Es: Conformidade/Eficácia — evidência inválida no idioma canônico contamina todo downstream; o gate prevalece sobre conveniência
  BOUNDED LOOP: 1 tentativa de validação por submissão; sem retry automático — nova submissão exige nova versão (INV-07)
  GATE DE SAÍDA: verificação booleana de completude do contrato + autorização (é o gate; ENF-03)
  VERIFICADO POR:
    DADO        Evidência sem Technical Rationale (Camada 3 incompleta), produtor autorizado
    QUANDO      a camada aplica o gate de publicação
    ENTÃO       publicação REJEITADA, código "CEM_CONTRACT_INCOMPLETE (technical_rationale ausente)"
    VERIFICAÇÃO nenhuma evidência publicada; motivo registrado
```

### BASpec-EPH-002 — Registrar proveniência da transformação Fonte→Dado→Evidência (Observação ≠ Evidência)

```
BASpec-EPH-002:
  QUANDO:       Uma Evidência é publicada a partir de observações de mercado ou de Skills
  ENTÃO:        A camada registra a proveniência operacional — origem informacional (Source Reference),
                ferramenta/Skill produtora e o Agente interpretante — preservando a fronteira
                Observação(Skill) ≠ Evidência(Agente); uma Observação de Skill sem interpretação de
                Agente NÃO é publicada como Evidência
  PORQUE:       INV-06: Evidência (Agente, interpretada) ≠ Observação (Skill, determinística); a
                rastreabilidade (CEM Princípio 4) exige saber qual ferramenta/Skill produziu o insumo
  REFERÊNCIA:   RULE-EPH-02; INV-06; CEM-001 Cap.2/Princípio 4
  CLASSE:       D (Determinístico — registro estruturado de proveniência)
  MECANISMO:    Regra: grava campos de proveniência operacional (imutáveis pós-publicação — CEM Cap.4); rejeita Observação-como-Evidência
  CRITÉRIO 4Es: Eficácia — proveniência incorreta impede reconstrução; determinismo garante rastreabilidade fiel
  VERIFICADO POR:
    DADO        uma Observação de Skill (stateless, sem interpretação de Agente) submetida como Evidência
    QUANDO      a camada avalia a fronteira INV-06
    ENTÃO       submissão recusada; a Observação permanece Observação (não vira Evidência)
    VERIFICAÇÃO log distingue Observação (Skill) de Evidência (Agente); nenhuma Evidência criada
```

### BASpec-EPH-003 — Dois eixos independentes: confiabilidade do produtor × força do relato

```
BASpec-EPH-003:
  QUANDO:       Uma Evidência é publicada por um produtor com histórico registrado
  ENTÃO:        A camada associa à Evidência a confiabilidade histórica do produtor como metadado
                descritivo (extensão Categoria A do CEM-001 via GMC-001), MANTIDA SEPARADA e
                independente da Evidence Strength (força do relato específico); um eixo não altera o outro
  PORQUE:       Doutrina Admiralty (SRC-02): "the reliability of the source does not influence the
                assessed accuracy of the report" — confiabilidade de fonte é propriedade intrínseca da
                evidência (pertence ao CEM-001), eixo independente da acurácia do conteúdo (DN-1)
  REFERÊNCIA:   RULE-EPH-03; DHR-SPEC002-001 §2 DN-1; SRC-02; GMC-001 Cap.3 (Categoria A)
  CLASSE:       D (Determinístico — associação de metadado governado)
  MECANISMO:    Regra: grava o tier de confiabilidade (Governed Enumeration sob GMC-001) sem acoplar ao valor de Evidence Strength
  CRITÉRIO 4Es: Eficácia — a separação de eixos preserva a semântica da doutrina; misturá-los degradaria a interpretação
  VERIFICADO POR:
    DADO        produtor de baixa confiabilidade histórica publica Evidência com Evidence Strength alta
    QUANDO      a camada registra os dois eixos
    ENTÃO       confiabilidade = baixa E Evidence Strength = alta, ambas preservadas sem interferência mútua
    VERIFICAÇÃO os dois campos coexistem independentes; nenhum recalcula o outro
```

### BASpec-EPH-004 — Trava constitutiva: confiabilidade-de-fonte NUNCA no Conviction Vector (INV-04)

```
BASpec-EPH-004:
  QUANDO:       Qualquer rotina/consumidor tenta usar a confiabilidade histórica do produtor como
                dimensão, insumo ou peso do Conviction Vector
  ENTÃO:        A camada bloqueia o uso (trava constitutiva, efeito E3) e registra a violação; o campo
                permanece disponível apenas como metadado descritivo/filtro
  PORQUE:       INV-04: custo/qualidade-de-fonte NUNCA entra no Conviction Vector — Convicção ≠ Score;
                a homologação DN-1 é explícita ("só metadado descritivo/filtro; NUNCA dimensão")
  REFERÊNCIA:   RULE-EPH-04; INV-04; DHR-SPEC002-001 §2 DN-1; CONS-01
  CLASSE:       C (Constitutivo — enforcement de invariante de alto risco; o próprio gate)
  MECANISMO:    Gate determinístico: presença de confiabilidade-de-fonte em qualquer entrada do cálculo de convicção ⇒ rejeição
  CRITÉRIO 4Es: Conformidade — proteger INV-04 prevalece sobre qualquer conveniência analítica (E3, Economicidade não rebaixa)
  GATE DE SAÍDA: verificação determinística de ausência do campo de confiabilidade nos insumos de convicção (é o gate)
  VERIFICADO POR:
    DADO        uma rotina que inclui o tier de confiabilidade do produtor entre os insumos do Conviction Vector
    QUANDO      a camada aplica a trava
    ENTÃO       uso REJEITADO, código "INV04_SOURCE_RELIABILITY_IN_CONVICTION"; convicção não computada com esse campo
    VERIFICAÇÃO nenhum insumo de convicção contém confiabilidade-de-fonte; INV-04 preservado
```

### BASpec-EPH-005 — Taxonomia operacional (favorável / contra / inconclusiva + gancho "ausente")

```
BASpec-EPH-005:
  QUANDO:       Uma Evidência é classificada quanto ao seu papel operacional em relação a hipóteses
  ENTÃO:        A camada permite representar favorável, contraevidência, inconclusiva e "ausente"
                (gancho de extensibilidade); a SIGNIFICÂNCIA de "ausente" NÃO é interpretada aqui
                (deferida ao Dossiê de cada Spec consumidora — SPEC-010+)
  PORQUE:       RULE-009 (resposta inclui evidência favorável/contra); DN-3 homologada: só o gancho
                agora, semântica de ausência é decisão de timing (padrão RISK-LEV-001), não de mérito
  REFERÊNCIA:   RULE-EPH-05; RULE-009; DHR-SPEC002-001 §2 DN-3
  CLASSE:       D (Determinístico — atribuição de rótulo taxonômico)
  MECANISMO:    Regra: enum taxonômica {favorável, contra, inconclusiva, ausente}; "ausente" é tipo válido sem regra de interpretação
  CRITÉRIO 4Es: Efetividade — a taxonomia certa serve o consumidor downstream sem sobre-especificar (Economicidade: não fixar semântica prematura)
  VERIFICADO POR:
    DADO        um consumidor precisa representar a ausência de uma evidência esperada
    QUANDO      a camada aplica a taxonomia
    ENTÃO       tipo "ausente" registrável; nenhuma regra de "quando ausência importa" é aplicada
    VERIFICAÇÃO o tipo "ausente" existe; a Spec não fixa sua significância (CONS-01 — DN-3)
```

### BASpec-EPH-006 — Supersessão append-only (INV-07)

```
BASpec-EPH-006:
  QUANDO:       O conhecimento de uma Evidência ACTIVE precisa ser atualizado
  ENTÃO:        A camada cria uma NOVA Evidência e transita a anterior para SUPERSEDED, preservando a
                Lineage e a referência sucessora; a Evidência anterior permanece armazenada e auditável;
                NENHUMA evidência é deletada
  PORQUE:       INV-07 (versionamento monotônico — nada deletado); CEM-001 Cap.4 (evolução de
                conhecimento por substituição, não modificação retroativa)
  REFERÊNCIA:   RULE-EPH-06; INV-07; CEM-001 Cap.4
  CLASSE:       D (Determinístico — criação de versão + transição de estado)
  MECANISMO:    Regra: publica nova evidência (via EPH-001) + Status anterior ACTIVE→SUPERSEDED (transição permitida); preserva Lineage
  CRITÉRIO 4Es: Eficácia — preservar histórico é integridade; determinismo garante que nada se perde
  VERIFICADO POR:
    DADO        Evidence-A ACTIVE cuja interpretação foi superada por Evidence-B
    QUANDO      a camada executa a supersessão
    ENTÃO       Evidence-A → SUPERSEDED (auditável), Evidence-B → ACTIVE, cadeia A→B íntegra
    VERIFICAÇÃO Evidence-A não deletada; Lineage preservada; INV-07 honrado
```

### BASpec-EPH-007 — Invalidação + evento + avaliação de impacto (Detector ≠ Gate) — E3

```
BASpec-EPH-007:
  QUANDO:       Uma Evidência é considerada incorreta e deve ser invalidada
  ENTÃO:        A camada transita ACTIVE→INVALIDATED (transição permitida; INVALIDATED→ACTIVE PROIBIDA),
                emite o evento *Evidence Invalidated* (via EC-COG-005) e INICIA a avaliação de impacto
                sobre derivadas pelo Fusion Engine — SEM cascata automática de invalidação
  PORQUE:       CEM-001 Cap.4/5: invalidação preserva histórico, não implica remoção nem cascata
                automática; o Fusion Engine INICIA a avaliação (Detector ≠ Gate — ENF-03); integridade
                histórica é irreversível (fail-closed em transição proibida — ENF-04)
  REFERÊNCIA:   RULE-EPH-07; CEM-001 Cap.4/5; ENF-03; ENF-04
  CLASSE:       C (Constitutivo — enforcement de transição irreversível de alto risco)
  MECANISMO:    Gate determinístico: valida transição permitida; emite evento; dispara início de avaliação (não executa cascata)
  CRITÉRIO 4Es: Conformidade — integridade do ciclo de vida canônico prevalece; irreversibilidade exige E3 fail-closed
  GATE DE SAÍDA: verificação determinística de que a transição pertence ao conjunto permitido do CEM-001 (é o gate)
  VERIFICADO POR:
    DADO        Evidence-C (ancestral em Lineage de Evidence-D) é invalidada
    QUANDO      a camada executa a invalidação
    ENTÃO       Evidence-C → INVALIDATED, evento *Evidence Invalidated* emitido, avaliação de impacto sobre D INICIADA (não cascateada)
    VERIFICAÇÃO Evidence-D não é invalidada automaticamente; decisão fica com Fusion Engine (Detector ≠ Gate)
```

### BASpec-EPH-008 — Metadado de independência/correlação (substrato de RULE-004; não computa confluência)

```
BASpec-EPH-008:
  QUANDO:       Uma Evidência é registrada
  ENTÃO:        A camada grava metadados de origem/linhagem/ferramenta/Skill com granularidade
                suficiente para que a dedução de dupla-contagem (RULE-004) e a confluência sejam
                COMPUTÁVEIS DOWNSTREAM (SPEC-003); a camada NÃO computa confluência nem aplica desconto
  PORQUE:       RULE-004 (evidências causalmente relacionadas contadas como uma única) exige substrato
                de independência; SRC-05: independência de evidência pode ser violada por correlação de
                indicadores — o registro precisa habilitar a detecção sem executá-la aqui
  REFERÊNCIA:   RULE-EPH-08; RULE-004; SRC-05
  CLASSE:       D (Determinístico — registro estruturado de metadado)
  MECANISMO:    Regra: grava chaves de proveniência/linhagem que permitem a jusante inferir correlação; nenhuma fórmula de fusão
  CRITÉRIO 4Es: Efetividade — o metadado certo habilita SPEC-003 no momento útil sem antecipar J-001 (Economicidade)
  VERIFICADO POR:
    DADO        duas Evidências derivadas da mesma origem/ferramenta
    QUANDO      a camada registra seus metadados de independência
    ENTÃO       a origem comum fica registrada e recuperável; nenhuma confluência é computada nesta camada
    VERIFICAÇÃO SPEC-003 pode detectar a não-independência a partir dos metadados; SPEC-002 não a resolve
```

### BASpec-EPH-009 — Metadado de conflito (substrato de RULE-005; não resolve conflito)

```
BASpec-EPH-009:
  QUANDO:       Uma Evidência é registrada
  ENTÃO:        A camada grava o metadado (domínio, direção implícita, referência de hipótese) que
                permite a detecção downstream de conflito direcional (RULE-005, Elliott×SMC); a camada
                NÃO resolve conflito nem produz veredito de `directional_conflict`
  PORQUE:       RULE-005 (conflito direcional aberto → sinal inválido) é resolvido pela Síntese
                (RULE-SY-001), não pela camada de evidência; a SPEC-002 apenas provê o substrato
  REFERÊNCIA:   RULE-EPH-08; RULE-005; RULE-SY-001; INV-01
  CLASSE:       D (Determinístico — registro estruturado de metadado)
  MECANISMO:    Regra: grava atributos que downstream compara para detectar conflito; nenhuma resolução aqui
  CRITÉRIO 4Es: Eficácia — o substrato correto preserva a hierarquia analítica (Elliott×SMC) para a Síntese
  VERIFICADO POR:
    DADO        Evidência estrutural (bullish, Elliott) e Evidência institucional (bearish, SMC) sobre o mesmo ativo/TF
    QUANDO      a camada registra os metadados de conflito
    ENTÃO       ambos os atributos direcionais ficam registrados; nenhum veredito de conflito é emitido
    VERIFICAÇÃO a detecção de `directional_conflict` permanece possível downstream; SPEC-002 não a executa
```

### BASpec-EPH-010 — Metadado de temporalidade/staleness (defere fórmula de aging)

```
BASpec-EPH-010:
  QUANDO:       Uma Evidência é registrada com referência temporal
  ENTÃO:        A camada grava metadados de temporalidade/validade (a partir de Creation Timestamp e
                Timeframe Reference do CEM-001) que permitem avaliar staleness downstream; NENHUMA
                fórmula de decaimento/aging é fixada nesta Spec
  PORQUE:       Aging/decaimento numérico toca J-001/N-001/SPEC-003 (aberto) — fixá-lo aqui violaria
                CONS-01; SRC-05 trata temporal decay como matéria de fusão, não de envelope
  REFERÊNCIA:   RULE-EPH-09; J-001; SRC-05; CONS-01
  CLASSE:       D (Determinístico — registro de metadado temporal)
  MECANISMO:    Regra: grava atributos temporais; nenhuma função de decaimento
  CRITÉRIO 4Es: Economicidade/Efetividade — registrar o mínimo suficiente sem antecipar J-001
  VERIFICADO POR:
    DADO        uma proposta de fixar "peso decai X% por período" na camada de evidência
    QUANDO      a camada avalia o escopo
    ENTÃO       a fórmula é recusada (deferida a J-001/SPEC-003); apenas o metadado temporal é gravado
    VERIFICAÇÃO nenhum decaimento numérico fixado; J-001 preservado (CONS-01)
```

### BASpec-EPH-011 — Vínculo evidência→hipótese por referência (CHM-001)

```
BASpec-EPH-011:
  QUANDO:       Uma Evidência precisa ser associada a uma ou mais hipóteses
  ENTÃO:        A camada registra o vínculo POR REFERÊNCIA (ID da hipótese, CHM-001), preservando a
                independência da evidência (uma evidência pode sustentar múltiplas hipóteses); a camada
                NÃO redefine nem altera a hipótese
  PORQUE:       CEM-001 Princípio 5 (Independência: evidência existe independentemente das hipóteses);
                INV-10 (comunicação por contrato canônico); a hipótese é do CHM-001, não da SPEC-002
  REFERÊNCIA:   RULE-EPH-10; CHM-001; CEM-001 Princípio 5; INV-06/INV-10
  CLASSE:       D (Determinístico — registro de referência)
  MECANISMO:    Regra: grava referência(s) de hipótese; nenhuma cópia/redefinição do objeto hipótese
  CRITÉRIO 4Es: Eficácia — vínculo por referência preserva reutilização e independência (CEM Princípio 5/6)
  VERIFICADO POR:
    DADO        uma Evidência que sustenta duas hipóteses distintas
    QUANDO      a camada registra os vínculos
    ENTÃO       ambas as referências coexistem; a Evidência permanece uma só (não duplicada)
    VERIFICAÇÃO independência preservada; nenhuma hipótese redefinida pela camada de evidência
```

### BASpec-EPH-012 — Suporte à auditabilidade/reconstrução bitemporal append-only (defere mecanismo físico)

```
BASpec-EPH-012:
  QUANDO:       Uma mudança de estado ou publicação de Evidência ocorre
  ENTÃO:        A camada registra timestamp, origem e justificativa da mudança (append-only,
                tamper-evident por construção — INV-07), habilitando reconstrução bitemporal ("o que se
                sabia e quando"); o MECANISMO FÍSICO de armazenamento/reconstrução é delegado ao
                Knowledge Graph (SPEC-006) e à auditoria (SPEC-041)
  PORQUE:       CEM-001 Cap.4/5 (toda mudança de estado registra timestamp/origem/justificativa;
                Cognitive Trace Reconstruction é capacidade do KG); INV-07; SRC-03 (lineage bitemporal
                MiFID); mecanismo físico é de outra Spec (H-001 aberta)
  REFERÊNCIA:   RULE-EPH-06; CEM-001 Cap.4/5; INV-07; SRC-03
  CLASSE:       D (Determinístico — registro de trilha de auditoria)
  MECANISMO:    Regra: grava trilha imutável de mudanças; referencia (não implementa) KG/SPEC-006, auditoria/SPEC-041
  CRITÉRIO 4Es: Eficácia — trilha completa é pré-condição de auditabilidade; append-only garante integridade
  VERIFICADO POR:
    DADO        uma sequência publicar→superseder→invalidar de uma Evidência
    QUANDO      a camada registra a trilha
    ENTÃO       cada mudança tem timestamp/origem/justificativa; a reconstrução bitemporal é possível
    VERIFICAÇÃO trilha append-only íntegra; mecanismo físico referenciado a SPEC-006/041 (não implementado aqui)
```

---

## D4 — Algoritmo

**D4 numérico N/A justificado.** A SPEC-002 é uma camada de **envelope/proveniência** — determinística mas **não-numérica**: não há fórmula de agregação (isso é SPEC-003/J-001, aberto — RULE-EPH-09). O comportamento determinístico é de **validação estrutural e registro**, expresso como procedimento (sem números):

```
ALGORITMO: publicar_evidencia_com_proveniencia
ENTRADA:   candidata C (campos do contrato CEM-001); produtor P; proveniência operacional (ferramenta/Skill, origem);
           confiabilidade histórica de P (Governed Enum); metadados de independência/conflito/temporalidade; vínculos de hipótese (refs)
PROCESSO:  1. gate_conformidade(C) := todas as 4 camadas CEM-001 presentes E completas   (EPH-001)
           2. gate_autorizacao(P) := P ∈ produtores autorizados (CEM-001 Cap.2/6)         (EPH-001)
           3. gate_fronteira := C é interpretação de Agente, não Observação-de-Skill crua (EPH-002; INV-06)
           4. se ¬(1 ∧ 2 ∧ 3) ⇒ REJEITAR (fail-closed), registrar motivo; FIM
           5. gravar proveniência operacional (imutável pós-publicação — CEM Cap.4)        (EPH-002)
           6. associar confiabilidade histórica de P como metadado descritivo, SEPARADO de Evidence Strength (EPH-003)
           7. bloquear qualquer roteamento de (6) a insumo de convicção                    (EPH-004; INV-04)
           8. gravar taxonomia {favorável|contra|inconclusiva|ausente} (ausente sem semântica) (EPH-005; DN-3)
           9. gravar metadados de independência/correlação, conflito e temporalidade (substrato downstream) (EPH-008/009/010)
          10. gravar vínculos de hipótese por referência (EPH-011); iniciar trilha de auditoria append-only (EPH-012)
          11. publicar (evento *Evidence Created*); Status = ACTIVE
SAÍDA:     Evidência publicada (ACTIVE) OU rejeição com motivo. NENHUM valor numérico de convicção/fusão é produzido.
EXEMPLO (não-numérico): C sem Technical Rationale ⇒ passo 1 falha ⇒ REJEITAR "CEM_CONTRACT_INCOMPLETE"; nada publicado.
```

> Transições de estado (superseder/invalidar/arquivar) seguem a máquina do CEM-001 Cap.4 (D5 abaixo) — determinísticas, sem números.

---

## D5 — Máquina de estados (operacional, SOBRE o ciclo de vida CEM-001 Cap.4)

> A SPEC-002 **não redefine** os estados do CEM-001 — **opera** sobre eles. Estados canônicos (CEM-001 Cap.4): ACTIVE / SUPERSEDED / INVALIDATED / ARCHIVED. A camada adiciona apenas o estado operacional **pré-publicação** (`DRAFT_CANDIDATE`) e o resultado de gate **`REJECTED_INCOMPLETE`**, que **não** são estados da Evidência publicada (a Evidência só existe canônica após passar no gate).

| Estado | Significado |
|---|---|
| DRAFT_CANDIDATE | Candidata submetida, ainda não validada pelo gate de conformidade (não é Evidência CEM-001 ainda) |
| REJECTED_INCOMPLETE | Candidata reprovada no gate (contrato incompleto / produtor não autorizado / fronteira INV-06) — não publicada |
| ACTIVE | (CEM-001) Evidência válida, disponível para consumo/fusão |
| SUPERSEDED | (CEM-001) Substituída por versão mais recente; auditável; não usada em novas inferências |
| INVALIDATED | (CEM-001) Considerada incorreta; histórico preservado; não sustenta novas hipóteses |
| ARCHIVED | (CEM-001) Removida da camada ativa; apenas consulta histórica |

### Transições (as de ACTIVE em diante são as do CEM-001 Cap.4 — não redefinidas)

```
DRAFT_CANDIDATE     -> REJECTED_INCOMPLETE  (gate EPH-001/EPH-002 falha — fail-closed)
DRAFT_CANDIDATE     -> ACTIVE               (gate passa; evento *Evidence Created*)
ACTIVE              -> SUPERSEDED            (EPH-006; nova versão; Lineage preservada)
ACTIVE              -> INVALIDATED           (EPH-007; evento *Evidence Invalidated*; avaliação de impacto iniciada)
ACTIVE              -> ARCHIVED              (CEM-001 Cap.4)
SUPERSEDED          -> ARCHIVED              (CEM-001 Cap.4)
INVALIDATED         -> ARCHIVED              (CEM-001 Cap.4)
```

**Transições PROIBIDAS (CEM-001 Cap.4 — fail-closed, EPH-007):** INVALIDATED→ACTIVE, ARCHIVED→ACTIVE, SUPERSEDED→ACTIVE. Qualquer tentativa é rejeitada (integridade histórica; INV-07).

**Invariante de estado (ENF-03/ENF-04):** nenhuma transição para ACTIVE a partir de estado terminal; nenhuma publicação a partir de DRAFT_CANDIDATE sem passar no gate determinístico. O LLM/Agente produz o conteúdo; o gate (determinístico) decide a publicação.

---

## D6 — Protocolo de publicação/consumo no Blackboard (D6)

> Ordem canônica de publicação e consumo (acoplada ao Blackboard/SPEC-004 — M-001 aberta — e ao Event Bus EC-COG-005). O **armazenamento físico** é de SPEC-004/006 (não fixado aqui); a SPEC-002 define o **protocolo lógico**.

```
1. Agente produtor interpreta observações → monta candidata no contrato CEM-001 (idioma canônico, INV-10).
2. Camada Harness aplica gate (EPH-001/EPH-002): conformidade + autorização + fronteira Observação≠Evidência.
   - falha ⇒ REJECTED_INCOMPLETE (fail-closed); nada publicado; motivo registrado.
3. Camada grava proveniência (EPH-002), dois eixos de qualidade (EPH-003) com trava INV-04 (EPH-004),
   taxonomia (EPH-005), metadados de independência/conflito/temporalidade (EPH-008/009/010),
   vínculos de hipótese por referência (EPH-011), trilha de auditoria append-only (EPH-012).
4. Camada publica no Blackboard (Status=ACTIVE) e emite *Evidence Created* via EC-COG-005.
5. Consumidores (Fusion Engine/Manager — CEM-001 Cap.6) leem apenas ACTIVE; NÃO alteram/reinterpretam (CEM Cap.6).
6. Atualização de conhecimento ⇒ EPH-006 (nova versão; anterior→SUPERSEDED; evento *Evidence Superseded*).
7. Erro cognitivo detectado ⇒ EPH-007 (ACTIVE→INVALIDATED; *Evidence Invalidated*; Fusion Engine INICIA avaliação de impacto).
8. Reconstrução/auditoria ⇒ Knowledge Graph (SPEC-006) via Cognitive Trace Reconstruction; auditoria formal ⇒ SPEC-041.
```

O protocolo **não cria autoridade nova** sobre o objeto Evidência — reutiliza o contrato, o ciclo de vida e os eventos do CEM-001 (Cap.3/4/6). [FONTE: CEM-001 Cap.6; EC-COG-005]

---

## D7 — Cenários de Teste

### Cenário-EPH-T01 — Publicação rejeitada por contrato incompleto (fail-closed)

```
DADO        Evidência com Camada 3 (Conteúdo) sem Technical Rationale; produtor autorizado
QUANDO      a camada aplica o gate de publicação (EPH-001)
ENTÃO       publicação REJEITADA, "CEM_CONTRACT_INCOMPLETE"; estado REJECTED_INCOMPLETE
VERIFICAÇÃO nenhuma Evidência ACTIVE criada; motivo registrado
```

### Cenário-EPH-T02 — Fronteira Observação ≠ Evidência (INV-06)

```
DADO        uma Observação de Skill (stateless, sem interpretação) submetida como Evidência
QUANDO      a camada avalia a fronteira (EPH-002)
ENTÃO       submissão recusada; a Observação não vira Evidência
VERIFICAÇÃO INV-06 preservado; nenhuma Evidência criada a partir de Observação crua
```

### Cenário-EPH-T03 — Dois eixos independentes preservados

```
DADO        produtor de baixa confiabilidade histórica publica Evidência com Evidence Strength alta
QUANDO      a camada registra confiabilidade (EPH-003) e força do relato
ENTÃO       confiabilidade=baixa E Evidence Strength=alta coexistem sem interferência
VERIFICAÇÃO nenhum eixo recalcula o outro (SRC-02: reliability ≠ credibility)
```

### Cenário-EPH-T04 — Trava INV-04 bloqueia confiabilidade no Conviction Vector

```
DADO        rotina que inclui o tier de confiabilidade do produtor como insumo do Conviction Vector
QUANDO      a camada aplica a trava (EPH-004)
ENTÃO       uso REJEITADO, "INV04_SOURCE_RELIABILITY_IN_CONVICTION"
VERIFICAÇÃO INV-04 preservado; convicção não computada com confiabilidade-de-fonte
```

### Cenário-EPH-T05 — Supersessão append-only (INV-07)

```
DADO        Evidence-A ACTIVE superada por Evidence-B
QUANDO      a camada executa a supersessão (EPH-006)
ENTÃO       Evidence-A→SUPERSEDED (auditável), Evidence-B→ACTIVE, cadeia A→B íntegra
VERIFICAÇÃO Evidence-A não deletada; Lineage preservada
```

### Cenário-EPH-T06 — Invalidação sem cascata automática (Detector ≠ Gate)

```
DADO        Evidence-C (ancestral de Evidence-D) invalidada
QUANDO      a camada executa a invalidação (EPH-007)
ENTÃO       Evidence-C→INVALIDATED, *Evidence Invalidated* emitido, avaliação de impacto sobre D INICIADA
VERIFICAÇÃO Evidence-D NÃO invalidada automaticamente; decisão fica com Fusion Engine
```

### Cenário-EPH-T07 — Gancho "ausente" sem semântica (DN-3)

```
DADO        consumidor precisa representar ausência de evidência esperada
QUANDO      a camada aplica a taxonomia (EPH-005)
ENTÃO       tipo "ausente" registrável; nenhuma regra de significância aplicada
VERIFICAÇÃO DN-3 honrada — só o gancho; semântica deferida a SPEC-010+
```

---

## D8 — Cenários Adversariais [casos de negação — CRITICAL / §7-bis Bloco A]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre conformidade, autorização, transição de estado ou integridade de proveniência, a camada NÃO publica/NÃO transita e retorna código específico. O *blast radius* (evidência consumida por todo agente downstream) justifica o rigor D8 (DN-2).

### ADV-EPH-01 — Produtor não autorizado tenta publicar

```
DADO        um componente não listado como produtor autorizado (CEM-001 Cap.2/6) submete Evidência completa
QUANDO      a camada aplica o gate de autorização (EPH-001)
ENTÃO       publicação REJEITADA, "PRODUCER_NOT_AUTHORIZED"; nada publicado
VERIFICAÇÃO conformidade de contrato NÃO basta — autorização é gate independente (fail-closed)
```

### ADV-EPH-02 — Tentativa de mutar campo imutável pós-publicação

```
DADO        uma rotina tenta alterar Observation/Interpretation/Lineage de uma Evidência já ACTIVE
QUANDO      a camada avalia a mutação (CEM-001 Cap.4: Status é o único campo mutável)
ENTÃO       mutação REJEITADA, "IMMUTABLE_FIELD_AFTER_PUBLICATION"
VERIFICAÇÃO integridade histórica preservada; correção só via nova versão (EPH-006)
```

### ADV-EPH-03 — Transição de estado proibida (ressurreição)

```
DADO        tentativa de transitar uma Evidência INVALIDATED (ou ARCHIVED/SUPERSEDED) de volta a ACTIVE
QUANDO      a camada valida a transição (EPH-007; CEM-001 Cap.4)
ENTÃO       transição REJEITADA, "FORBIDDEN_TRANSITION_TO_ACTIVE"
VERIFICAÇÃO INV-07/integridade histórica preservados; nenhuma ressurreição de evidência
```

### ADV-EPH-04 — Confiabilidade-de-fonte disfarçada de Evidence Strength (burlar INV-04)

```
DADO        rotina que injeta o tier de confiabilidade do produtor DENTRO do campo Evidence Strength para
            fazê-lo chegar ao Conviction Vector indiretamente
QUANDO      a camada verifica a separação de eixos (EPH-003/EPH-004)
ENTÃO       operação REJEITADA, "AXIS_CONTAMINATION"; os dois eixos permanecem separados
VERIFICAÇÃO INV-04 preservado mesmo contra contaminação indireta (SRC-02: eixos independentes)
```

### ADV-EPH-05 — Cascata automática de invalidação (violar Detector ≠ Gate)

```
DADO        invalidação de Evidence-C com rotina que tenta invalidar automaticamente todas as derivadas D..N
QUANDO      a camada processa a invalidação (EPH-007)
ENTÃO       cascata automática RECUSADA; apenas a AVALIAÇÃO de impacto é iniciada (Fusion Engine decide)
VERIFICAÇÃO CEM-001 Cap.5 ("invalidação não implica cascata automática") e ENF-03 preservados
```

### ADV-EPH-06 — Deleção de evidência (violar INV-07)

```
DADO        tentativa de deletar fisicamente uma Evidência SUPERSEDED/INVALIDATED
QUANDO      a camada avalia a operação (EPH-006; INV-07)
ENTÃO       deleção RECUSADA, "APPEND_ONLY_VIOLATION"; a Evidência permanece auditável
VERIFICAÇÃO INV-07 preservado; ARCHIVED é o único caminho de "saída" da camada ativa (não deleção)
```

### ADV-EPH-07 — Redefinição implícita do CEM-001 (violar CONST-01)

```
DADO        a camada tenta introduzir um novo estado de ciclo de vida ou renomear um campo canônico do CEM-001
QUANDO      o gate de conformidade avalia contra o contrato canônico (CEM-001)
ENTÃO       operação RECUSADA, "CANONICAL_MODEL_REDEFINITION"; extensões só via GMC-001 (Categoria A/B)
VERIFICAÇÃO CONST-01 preservado; DN-1 entrou como extensão Categoria A via GMC-001, não como redefinição
```

### ADV-EPH-08 — Fixar fórmula de aging/convicção na camada de evidência (violar CONS-01/J-001)

```
DADO        proposta de fixar decaimento numérico de peso ("−X%/período") ou limiar de convicção na SPEC-002
QUANDO      a camada avalia o escopo (EPH-009/EPH-010; CONS-01)
ENTÃO       proposta RECUSADA; deferida a J-001/CCM-001/SPEC-003
VERIFICAÇÃO nenhum número de convicção/aging fixado; J-001 preservado (CONS-01)
```

### ADV-EPH-09 — Interpretar significância de "ausente" (violar DN-3)

```
DADO        proposta de fixar "ausência de evidência institucional ⇒ enfraquece hipótese" na SPEC-002
QUANDO      a camada avalia o escopo (EPH-005; DN-3)
ENTÃO       regra de significância RECUSADA; só o gancho "ausente" permanece
VERIFICAÇÃO DN-3 honrada; semântica deferida ao Dossiê de SPEC-010+ (CONS-01)
```

---

## D9 — Auditabilidade (por referência)

A reconstrução completa da decisão (P13) é **capacidade do Knowledge Graph** (Cognitive Trace Reconstruction — CEM-001 Cap.5) e da auditoria formal (SPEC-041). A SPEC-002 garante o **substrato**: trilha append-only de mudanças (timestamp/origem/justificativa — EPH-012), Lineage íntegra (EPH-006), eventos canônicos (*Evidence Created/Superseded/Invalidated/Archived* via EC-COG-005). O mecanismo físico é delegado (H-001 aberta / SPEC-006; SPEC-041). L4 (auditoria D9 completa + backtest) só é atingível na fase de implementação (RULE-MM-04) — teto spec-first = L3.

---

## I/O Schemas (por referência — não redefinir)

- **Contrato da Evidência:** CEM-001 Cap.3 (idioma canônico — INV-10). A SPEC-002 **não** cria schema de Evidência concorrente; usa o contrato canônico.
- **Extensão DN-1:** confiabilidade histórica do produtor como **Governed Enumeration** sob GMC-001 (Categoria A) — o artefato formal de evolução do CEM-001 (proposta + análise de impacto GMC-001 Cap.3/5) é ato de governança do Controlador/GMC-001, **não** fechado por este Plan (ver Decisões abertas / EPH-GMC-001).
- **Consumo em runtime:** os schemas `runtime-workflow.conviction-report.json` (E3/E4/E6, campos `evidence_ref`/`evidence_classification`) são **preenchidos** com a proveniência/classificação definidas aqui — o **consumo** é dos agentes (SPEC-010/012/013), adiado (research.md §4). [FONTE: WORKFLOW.md §5/§7-bis.2]

---

## Enforcement Contracts (ENF-01..08)

> Pisos por tipo (atomic-spec §10.2): Evidência/Hipótese de Agente → E2 mínimo; commit crítico/irreversível → E3. Economicidade nunca rebaixa (ENF-02).

### EC-EPH-001 — Publicação de Evidência (EPH-001/EPH-002)

```
CAPABILITY   : validar e publicar Evidência conforme contrato CEM-001
EFFECT       : publicação no Blackboard (Status=ACTIVE) + evento *Evidence Created* (EC-COG-005)
PRECOND      : contrato CEM-001 completo (4 camadas) ∧ produtor autorizado ∧ fronteira Observação≠Evidência (INV-06)
POSTCOND     : Evidência ACTIVE com proveniência completa e imutável (Status = único mutável); OU nada publicado
POLICY       : CEM-001 Cap.3/6 (proibido publicar Evidências incompletas); INV-06; INV-10
LEVEL        : E2 (operacional — piso Evidência; precond/postcond/capabilities)
FAILURE-MODE : fail-closed — publicação incompleta/não autorizada REJEITADA (REJECTED_INCOMPLETE); motivo registrado
EVIDENCE     : log do gate (campos verificados × presentes); ausência de Evidência publicada quando rejeitada
```

### EC-EPH-002 — Supersessão de Evidência (EPH-006)

```
CAPABILITY   : criar nova versão e transitar a anterior para SUPERSEDED
EFFECT       : nova Evidência ACTIVE + anterior SUPERSEDED + evento *Evidence Superseded*
PRECOND      : Evidência anterior em ACTIVE; nova Evidência válida (EC-EPH-001); Lineage preservável
POSTCOND     : histórico íntegro (anterior auditável, não deletada — INV-07); cadeia de versões explícita
POLICY       : INV-07 (versionamento monotônico); CEM-001 Cap.4
LEVEL        : E2 (operacional)
FAILURE-MODE : fail-closed — se a nova versão não valida ou a Lineage se perderia, supersessão NÃO ocorre
EVIDENCE     : cadeia A→B auditável; anterior presente em estado SUPERSEDED
```

### EC-EPH-003 — Invalidação de Evidência (EPH-007) — irreversível

```
CAPABILITY   : transitar ACTIVE→INVALIDATED e iniciar avaliação de impacto
EFFECT       : Status INVALIDATED + evento *Evidence Invalidated* + INÍCIO de avaliação de impacto (Fusion Engine)
PRECOND      : transição pertence ao conjunto permitido (CEM-001 Cap.4); INVALIDATED→ACTIVE PROIBIDA
POSTCOND     : Evidência INVALIDATED (histórico preservado); derivadas NÃO invalidadas automaticamente
POLICY       : CEM-001 Cap.4/5 (sem cascata automática); ENF-03 (Detector ≠ Gate); INV-07
LEVEL        : E3 (crítico/irreversível — transição de estado terminal)
FAILURE-MODE : fail-closed — transição proibida REJEITADA (FORBIDDEN_TRANSITION_TO_ACTIVE); nenhuma ressurreição
EVIDENCE     : evento emitido; avaliação de impacto registrada como INICIADA (não cascateada); método de observação de falso-DENY (amostral; limiar = gap aberto, ENF-07)
```

### EC-EPH-004 — Trava anti-INV-04 (EPH-004) — constitutiva

```
CAPABILITY   : bloquear roteamento de confiabilidade-de-fonte a insumo de convicção
EFFECT       : rejeição de qualquer uso da confiabilidade do produtor no Conviction Vector
PRECOND      : detecção de confiabilidade-de-fonte entre insumos/pesos/dimensões de convicção
POSTCOND     : nenhum insumo de convicção contém confiabilidade-de-fonte (INV-04 preservado)
POLICY       : INV-04 (custo/qualidade-de-fonte nunca no Conviction — Salvaguarda 4 CEE-001 §10)
LEVEL        : E3 (crítico — protege invariante constitucional)
FAILURE-MODE : fail-closed — uso REJEITADO (INV04_SOURCE_RELIABILITY_IN_CONVICTION)
EVIDENCE     : log da trava; verificação amostral de insumos de convicção livres de confiabilidade-de-fonte (ENF-07)
```

**ENF-08 (escala E0–E3):** referenciada em atomic-spec §10.2. **ENF-06:** não há comportamento E0 nesta Spec (todos os efeitos são ≥ E2). **ENF-05:** nenhuma policy é auto-aprendida — extensões (DN-1) passam pelo GMC-001; regras RULE-EPH-* só vigem por homologação de Andraus.

---

## §7-bis — Autopré-check de Redução de Viés (CRITICAL — obrigatório)

Executado após o §7 e antes de submeter ao Revisor. Propósito: identificar o que a Spec poderia ter errado.

### Bloco A — Pergunta adversarial por BASpec (D8 aplicado à auto-revisão)

Para cada BASpec CRITICAL/HIGH desta entrega (todas as EPH-001..012 são de alta criticidade — camada consumida por todo downstream):

| BASpec | "Se estivesse errada, o que seria observável?" (caso de negação) | ENTÃO verificável por observador independente? | Condição em que QUANDO se satisfaz mas ENTÃO não deve ocorrer? |
|---|---|---|---|
| EPH-001 | evidência incompleta publicada contaminaria downstream → ADV-EPH-01 (produtor não autorizado) e T01 | Sim — presença/ausência de Evidência ACTIVE + código de rejeição | se produtor autorizado mas contrato completo → publica (correto); nenhuma negação espúria |
| EPH-002 | Observação de Skill vira Evidência sem interpretação → T02; INV-06 violado | Sim — log distingue Observação de Evidência | Agente que já interpretou não deve ser barrado (não é Observação crua) |
| EPH-003 | eixos misturados → ADV-EPH-04 (contaminação); T03 | Sim — dois campos coexistem independentes | produtor sem histórico registrado → confiabilidade "ausente/indeterminada", não força valor |
| EPH-004 | confiabilidade entra no Conviction → T04, ADV-EPH-04; INV-04 violado | Sim — insumos de convicção auditáveis | uso da confiabilidade como FILTRO/metadado (não convicção) é permitido — não deve ser barrado |
| EPH-005 | semântica de "ausente" fixada aqui → ADV-EPH-09; DN-3 violado | Sim — ausência de regra de significância | representar "ausente" é permitido; só interpretá-lo é vedado |
| EPH-006 | evidência deletada → ADV-EPH-06; INV-07 violado | Sim — anterior presente em SUPERSEDED | ARCHIVED (não deleção) é caminho legítimo |
| EPH-007 | cascata automática → ADV-EPH-05; ressurreição → ADV-EPH-03 | Sim — derivadas não invalidadas; evento emitido | avaliação de impacto INICIADA é correta; não confundir com cascata |
| EPH-008 | confluência computada aqui → invadir SPEC-003/J-001 | Sim — nenhum valor de fusão produzido | registrar metadado é correto; computar desconto não |
| EPH-009 | conflito resolvido aqui → invadir Synthesis (RULE-SY-001) | Sim — nenhum veredito de conflito emitido | registrar substrato é correto; emitir `directional_conflict` não |
| EPH-010 | fórmula de aging fixada → ADV-EPH-08; J-001 violado | Sim — nenhum número de decaimento | registrar metadado temporal é correto |
| EPH-011 | hipótese redefinida/copiada → CHM-001 violado; INV-10 | Sim — vínculo por referência, não cópia | múltiplas referências (independência) é correto (CEM Princípio 5) |
| EPH-012 | mecanismo físico implementado aqui → invadir SPEC-006/041 | Sim — trilha lógica, referência a KG/041 | registrar trilha append-only é correto; implementar KG não |

Todas as três perguntas foram respondidas com âncora de fonte; nenhuma BASpec restou como [DECISÃO NECESSÁRIA] por falta de resposta adversarial.

### Bloco B — Viés de confirmação na herança obrigação-a-obrigação (CC-08 / CEM-001 v1.0)

[Delimitação: verifica a herança obrigação-a-obrigação já declarada por CC-08 (EUA-E04). NÃO antecipa a regra escrita de conservação-como-conjunto (Contrato de Herança Vertical), cujo conteúdo será redigido junto da SPEC-019 (escopo homologado, conteúdo pendente — não é decisão em aberto).]

Obrigações herdadas do CEM-001 v1.0 e evidência de satisfação nesta Spec:

| Obrigação herdada (CEM-001) | Evidência de satisfação nesta Spec |
|---|---|
| Contrato de 4 camadas obrigatório (Cap.3) | EPH-001 exige as 4 camadas completas no gate (fail-closed) |
| Producer Type/ID; Origin Type PRIMARY/DERIVED (Cap.3) | EPH-002 registra produtor/proveniência; EPH-008 usa Lineage (DERIVED) |
| Evidence Strength = float 0-1, ≠ Convicção (Cap.3) | EPH-003 mantém Evidence Strength como eixo de conteúdo; EPH-004 impede confusão com convicção |
| Status = único campo mutável; demais imutáveis (Cap.4) | ADV-EPH-02 rejeita mutação de campo imutável; D5 restringe transições |
| Estados/transições canônicos; proibidas → ACTIVE (Cap.4) | D5 e EPH-007 preservam transições permitidas/proibidas (fail-closed) |
| Evolução por substituição, não modificação retroativa (Cap.4) | EPH-006 (append-only; nova versão + SUPERSEDED) |
| *Evidence Invalidated* + avaliação de impacto sem cascata (Cap.4/5) | EPH-007 emite evento + INICIA avaliação (Detector ≠ Gate); ADV-EPH-05 |
| Lineage íntegra; sem remover/adicionar ancestrais pós-publicação (Cap.5) | EPH-006/EPH-012 preservam Lineage; ADV-EPH-02 |
| Cognitive Trace Reconstruction/Depth = capacidades do KG, não campos (Cap.5) | D9/EPH-012 delegam ao KG (SPEC-006); não implementam campo |
| Consumidor não altera/reinterpreta (Cap.6) | D6 passo 5; EPH-011 (vínculo por referência, não redefinição) |
| Neutralidade de domínio (Princípio 1) | CC-01/CC-12: infraestrutural; nenhuma análise de escola |
| Independência da evidência (Princípio 5) | EPH-011 (uma evidência sustenta múltiplas hipóteses) |
| Evolução só via GMC-001 (Cap.7) | DN-1 como extensão Categoria A via GMC-001; ADV-EPH-07 |

Nenhuma obrigação herdada foi silenciosamente removida/enfraquecida (RULE-HD-03) nem contradita por ADDED/MODIFIED (RULE-HD-02). REMOVED vazio. Nenhuma obrigação ficou sem evidência de satisfação.

### Bloco C — Verificação epistêmica (RULE-EPI-01..03 / RULE-CAU / RULE-PRB / CC-09) — completa

Executada integralmente (aprendendo com o achado F-01 de rodadas anteriores — Bloco C não pode ser resumido em CRITICAL):

1. **Afirmações causais com mecanismo (RULE-CAU-01 / RULE-EPI-02).** As poucas afirmações causais desta Spec são de mecanismo declarado, não correlação:
   - "publicar evidência incompleta contaminaria downstream" — mecanismo: o idioma canônico (CEM-001) é consumido literalmente por Fusion/Manager; um campo obrigatório ausente quebra a interpretação garantida (CEM Cap.6/8). É consequência contratual, não correlação estatística.
   - "confiabilidade-de-fonte no Conviction Vector violaria INV-04" — mecanismo: INV-04 define custo/qualidade-de-fonte fora do Conviction por construção; o efeito é normativo (violação de invariante), não empírico.
   - Nenhuma afirmação do tipo "X causa melhora de Y%" é feita (não há alegação de desempenho).
2. **Hipótese ≠ fato (RULE-EPI-01).** Fontes externas (SRC-01..05) são [EXTERNO]/DADO, nunca fato SOT. SRC-04/SRC-05 são surveys/evidência de artefato, não endosso de correção (IDs arXiv pós-treino tratados como DADO não verificado — research.md §2). As RULE-EPH-* são [PROPOSTA], não FATO NORMATIVO. A SPEC-002 é FATO ARQUITETURAL candidato, não baseline.
3. **INDETERMINADO onde há incerteza material.** A significância da "ausência de evidência" é declarada INDETERMINADA/deferida (DN-3), não forçada a PASS/FAIL. A classificação de confiabilidade de um produtor sem histórico registrado é "ausente/indeterminada", não um valor default arbitrário (Bloco A, EPH-003). E6 (Dempster-Shafer) é INDETERMINADO (fetch sem trecho limpo — research.md §2), e nenhuma alegação carregada repousa nele.
4. **Probabilidade bem-formada (RULE-PRB-01).** Nenhuma probabilidade é declarada nesta Spec — a camada de evidência não produz probabilidade/convicção (isso é SPEC-003/J-001). Portanto não há evento probabilístico mal-formado.
5. **Sem falsa precisão (CC-09).** Nenhum número (limiar, peso, decaimento, percentual) é fixado. Evidence Strength permanece o campo canônico do CEM-001 (não redefinido); a confiabilidade é uma Governed Enumeration ordinal (tiers), não um score numérico com falsa precisão. Aging/pesos deferidos a J-001 (ADV-EPH-08).
6. **Modalidade preservada (RULE-SEM-03).** "DEVE/NÃO DEVE" usados conforme EARS/RULE; "PODE" (ex.: uma evidência PODE sustentar múltiplas hipóteses) não é convertido em obrigação.

### Bloco D — Reforço de escopo (ponteiro de reconfirmação — §7)

- [x] A Spec **representa/versiona/classifica** evidência — **não** decide sinal nem executa (INV-05 / RULE-DEC-01) — reconfirmado (D0/CC-01).
- [x] Nenhuma BASpec cruza a fronteira SOT→execução downstream (nenhum Signal Package/ordem — INV-05).
- [x] Toda dependência de decisão de Andraus/governança está marcada [DECISÃO NECESSÁRIA]/[PROPOSTA], não como fato (DN-1 homologado é exceção — é FATO NORMATIVO desta abertura).

---

## Decisões abertas incidentes (CONS-01 — não fechadas por este Plan)

Nenhuma decisão aberta é fechada por esta entrega. Permanecem **ABERTAS/pendentes** e apenas referenciadas:

| ID | Questão | Relação com a SPEC-002 |
|---|---|---|
| **J-001** | Fórmula/pesos/limiares definitivos do Conviction Vector (pendente/aberta) | A SPEC-002 defere aging/peso/decaimento (EPH-009/010) e não fixa limiar — **não fecha J-001** |
| **M-001** | Estados do Blackboard para objetos não-hipótese (aberta — SPEC-004) | Armazenamento físico de evidência é da SPEC-004 — **não antecipado** (pendente) |
| **H-001** | Knowledge Graph: grafo real ou em memória? (aberta — SPEC-006) | Mecanismo físico de reconstrução delegado — **não antecipado** (pendente) |
| **N-001** | Pesos por ativo do Conviction Vector (aberta — parte de J-001) | Fora de escopo — **não tocada** (pendente) |
| **K-001** | Ciclo P12 de evolução do conhecimento (aberta — SPEC-018) | Fora de escopo — **não tocada** (pendente) |
| **G-001** | Schema de estado persistente por agente (aberta — SPEC-009) | Fora de escopo — **não tocada** (pendente) |
| **C-001** | Granularidade EARS multi-condição (aberta) | Padrão de BASpec — **não tocada** (pendente) |
| **RISK-CONV-001** | "convicção de risco" vs Conviction Vector 8D (aberta) | Fora de escopo — a SPEC-002 não computa convicção (pendente) |
| **ECC-VAL-001** | Validade/prazo do Dossiê de Pesquisa (aberta) | Plan iniciado no mesmo dia da abertura; regra geral permanece aberta (pendente) |

**Nova decisão revelada por este Plan (para Andraus/Controlador):**

| ID | Questão | Encaminhamento |
|---|---|---|
| **EPH-GMC-001** `[DECISÃO NECESSÁRIA]` | A homologação DN-1 nomeia a extensão como **Categoria A** ("aditiva, sem mudar semântica existente"). Pelas definições do **GMC-001 Cap.3**, novos **valores de Governed Enumeration** são Categoria A, mas um **novo campo** (mesmo opcional) reclassificaria para **Categoria B**. Modelar a confiabilidade histórica como valor de Governed Enumeration mantém-na Categoria A; se exigir um novo campo-container, a mecânica formal (proposta + análise de impacto + classificação A/B) é ato do processo GMC-001 (Cap.3/5). **Não fecho** a mecânica (RULE-MET-01) — a substância homologada (aditiva, não redefine, nunca no Conviction) é preservada; a classificação física exata é do Controlador/GMC-001. | Andraus/Controlador confirmam a via GMC-001 (valor de enum governada vs. novo campo opcional) antes/na homologação do Plan |

---

## Etiquetagem e status epistemológico (TRACE-06)

- **FATO NORMATIVO:** CEM-001 v1.0, GMC-001 v1.0, CHM-001 v1.0 (baselined); atomic-spec v1.5; INV-01..10 + INV-RISK-*; ENF-01..08; RULE-MECH-01..04; RULE-HD-01..04; RULE-004/005/009; DN-1/DN-2/DN-3 (homologadas — DHR-SPEC002-001).
- **FATO ARQUITETURAL:** esta SPEC-002 (candidata a baseline); a topologia Fusion→Conviction→Synthesis (B-001 fechada).
- **PROPOSTA:** RULE-EPH-01..10; EC-EPH-001..004; BASpec-EPH-001..012; escada de estados operacionais DRAFT_CANDIDATE/REJECTED_INCOMPLETE.
- **INFERÊNCIA:** determinação infraestrutural (CC-01/CC-12); nota de eixo de herança (CC-08 vs RULE-HV); mapeamento de consumo em runtime (E3/E4/E6).
- **DECISÃO NECESSÁRIA:** EPH-GMC-001 (mecânica GMC-001 da extensão DN-1); J-001/M-001/H-001/N-001/K-001/G-001/C-001/RISK-CONV-001/ECC-VAL-001 (referenciadas como pendentes).
- **EXTERNO:** SRC-01..05 (research.md §2) — DADO, nunca baseline; documentado ≠ homologado.

---

*SPEC-002 — Plan candidato (PROPOSTA). Método: atomic-spec.md v1.5. Constrói SOBRE CEM-001 (CONST-01) — não redefine. Não fecha decisão aberta (CONS-01). Não fabrica resultado de execução (RULE-MET-01). Pronto para verificação de spec (checks.md) e submissão ao Revisor após o gate determinístico.*
