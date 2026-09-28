# SPEC-019 — Harness Governance & Evolution (+ Contrato de Herança Vertical)

Versão: 1.0
Status: **HOMOLOGADA — BASELINE** (Andraus, 2026-09-22, DHR-SPEC019-001; parecer Revisor CONFORME; compat. Minor). RULE-HG-01..08 + RULE-HV-01..04 → `governance/RULES.md`. Achados Menores M-01/M-02 diferidos para emenda futura.
Complexidade: HIGH (declarada — ROADMAP §11)
Profundidade-alvo: D0–D8 (ROADMAP §11)
Profile (Claude Code): standard + adversarial (D8)
Posição no caminho crítico: FASE GOV, posição 1 — logo após SPEC-001 (HOMOLOGADA), precede SPEC-002 [FONTE: ROADMAP §21; DHR-EUA-E17 §3]
Nível de maturidade-alvo: L3 (Testável) — D5 + ≥3 cenários D7 + ≥1 adversarial D8 + revisão independente
Método: atomic-spec.md **v1.4** (vigente na data — DHR-EUA-E17 §3 fixa v1.4 para a FASE GOV, ou v1.5 se homologada antes do início; v1.5 não homologada até 2026-09-22)
Autor: Especificador Principal (Claude Code, Opus 4.8)
Data: 2026-09-22
Resolve: **L-001** (Governança do próprio harness / policy versionada) — **FECHADA na homologação (2026-09-22)**; escopo spec-time (§ "Resolução de L-001")

### Histórico de versões

| Versão | Data | Alterações |
|---|---|---|
| 1.0 | 2026-09-22 | Entrega candidata inicial. Escopo baseline (§11) + Contrato de Herança Vertical macro→micro (EUA-E17 Q1, homologado). D0–D8. |

---

## Nota de gate (passo 11-bis / RMR-001) — item ATIVADO por esta redação

[FONTE: RMR-001 §6 BL-013; DHR-EUA-E17 §6.3]

O início da redação da SPEC-019 dispara o Gatilho de Ativação de **BL-013 — MC-GOV-001** (`spec:SPEC-019 em redação`). Tratamento nesta entrega:

- **MC-GOV-001** (Master Contract da Camada de Governança) é **referência externa não-normativa** (admissão homologada 2026-09-21, DHR-MC-GOV-001; K-MAN-17). Seu escopo é **governança de runtime** (governança viva do conhecimento em operação), **SUBORDINADA** à governança já operante — NÃO substitui GMC-001, PAP-001, o trio Especificador→Revisor→Andraus, nem esta SPEC-019 (achado R-06 resolvido). [FONTE: memória MC-GOV-001/BL-013; DHR-MC-GOV-001]
- **Fronteira desta Spec × MC-GOV-001:** a SPEC-019 governa o **Harness de Especificação** (processo spec-time: quem altera Specs/RULEs, homologação, versionamento, emenda, rollback, exceção, auditoria). MC-GOV-001 é governança **runtime** e permanece **diferido** (ativa em SPEC-018/019-runtime/L-001-runtime). Esta Spec **não adota** rótulos do MC-GOV-001 (G-gates, I-GOV/GOV-P, estados §7) — respeita J-001/CC-02/INV-05/INV-09. [INFERÊNCIA]
- **Encaminhamento:** BL-013 permanece tratado-como-consultado (fonte de requisitos runtime, diferida); não há reescrita nem adoção normativa. O gate fecha limpo quanto a BL-013 desde que este tratamento seja registrado. **BL-015 (MC-LRN-001)** NÃO dispara aqui (gatilho = `spec:SPEC-018 em redação` ∨ `decisao:K-001`), permanece `Em espera`. [FONTE: RMR-001 §6 BL-015]

---

## Constitution Check (CC-01..CC-10 — atomic-spec §10.5 + EUA-E04..E14)

- [x] **CC-01 — Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT respeitada:** N/A quanto a conteúdo analítico; a SPEC-019 é governança de processo, não toca a hierarquia. Ao contrário, o Contrato de Herança Vertical **protege** a hierarquia contra supressão silenciosa entre níveis (RULE-HV-02). [INFERÊNCIA]
- [x] **CC-02 — Não redefine Modelo Canônico baselined (CEM/CHM/CCM/CDM/CNM):** a SPEC-019 não redefine nenhum modelo canônico; **constrói SOBRE** GMC-001 (governança de modelos canônicos, GOVERNANCE_MODEL, Baseline 1.0) sem alterá-lo, e não toca CCM-001 (pendente — SPEC-003). [FONTE: GMC-001; CONST-01]
- [x] **CC-03 — Conviction Vector:** N/A — a SPEC-019 não computa nem parametriza convicção. Dimensionalidade=8 permanece fechada; limiares definitivos = J-001 em aberto (não fechado aqui, CONS-01). [FONTE: INV-03]
- [x] **CC-04 — Salvaguardas Constitucionais (CEE-001 §10/§11):** nenhuma violada; a SPEC-019 não altera salvaguardas de economia/roteamento (§10) nem de sinal de trading (§11). [FONTE: INV-04; CEE-001]
- [x] **CC-05 — Complexidade declarada:** HIGH (ROADMAP §11), D0–D8.
- [x] **CC-06 — Campos SES-001 §59 (Engineering Card):** **N/A nesta entrega** — o artefato é Spec/Plan (plan.md), não uma Engineering Card. Os campos §59 e a cadeia §60 tornam-se obrigatórios quando as Tasks/Engineering Cards forem produzidas (fase de implementação; BUILD adiado — atomic-spec §14). Omissão justificada. [FONTE: atomic-spec §8.1; SDD-001 §9]
- [x] **CC-07 — Cadeia de derivação SES-001 §60:** N/A nesta entrega (idem CC-06); rastreabilidade de origem provida pela cadeia ROADMAP §11 → EUA-E17 Q1 → esta Spec.
- [x] **CC-08 — Bloco Herança/Delta (§8.3, EUA-E04):** presente (ver seção "Herança / Delta"); INHERITS/ADDED preenchidos com ID+versão; REMOVED vazio; nenhum item ADDED/MODIFIED contradiz o herdado (RULE-HD-02). [FONTE: EUA-E04 §8.3; regime prospectivo-obrigatório §6]
- [x] **CC-09 — Status epistemológico / Epistemic Check (RULE-EPI, INDETERMINADO, INV-EPI):** aplicado — distinção explícita entre FATO NORMATIVO (GMC-001 Cap., SDD-001, RULES.md, INV-07/09, EUA-E04) e FATO ARQUITETURAL (CR-001 Cap.7 candidato + Cap.8 não-congelado; GEH-001 pano-de-fundo). Nenhuma hipótese tratada como fato; sem falsa precisão. [FONTE: EUA-E05/MEG-001; RULE-EPI]
- [x] **CC-10 — Terminologia concorrente por escola (RULE-SEM):** N/A — o domínio desta Spec é governança de processo, sem terminologia concorrente por escola de análise técnica. [FONTE: EUA-E06/MSC-001]

**Disciplinas cognitivas N8–N17 incidentes:** RULE-DEC (decisão≠execução — reforçada, ver RULE-HG-03), RULE-MET-01 (não-fabricação — nenhum registro/DHR/RULE inventado), RULE-EPI (hipótese≠fato). INDETERMINADO usado onde há incerteza material (ver Decisões Incidentes).

---

## Herança / Delta (§8.3 — EUA-E04)

```
HERANÇA / DELTA — SPEC-019

INHERITS (herdado — a spec NÃO redefine; referência por ID + VERSÃO):
  - Método: atomic-spec.md v1.4 (BASpec, D0–D9, Enforcement E0–E3, F.1–F.4, EARS, TRACE-06)
  - Modelos Canônicos de governança:
      • GMC-001 Baseline 1.0 (GOVERNANCE_MODEL) — papéis, estados de governança, versionamento
        Categoria A/B/C, Catálogo Oficial, segregação de responsabilidades
  - Governança spec-driven: SDD-001 Baseline 1.1 (Spec/Plan/Tasks; Constitution Check; Living Spec)
  - Regras vigentes: RULES.md v1.1 — RULE-GMC-001..005; RULE-SDD-001/002; RULE-PPQ-001 (dial GES);
                     RULE-HD-01..04 (EUA-E04, Herança/Delta horizontal)
  - Invariantes: INV-07 (versionamento monotônico), INV-08 (RCN-001), INV-09 (sem baseline informal),
                 INV-05 (SOT não executa — reforçado por RULE-DEC)
  - Enforcement: ENF-01..08; ENF-05 (policies não auto-aprendidas) como fundamento de RULE-HG-02
  - Processo vigente: PAP-001 (regime por classe; D-DHR-PAP-001-01); RMR-001 (backlog/passo 11-bis);
                      EUA-E16 (RPSA); DHR como registro oficial de homologação

ADDED (delta local — o que esta spec acrescenta):
  - Modelo de governança do HARNESS DE ESPECIFICAÇÃO como Spec formal (não só método): RULE-HG-01..08
  - Contrato de Herança Vertical macro→micro (Harness Inheritance Contract): RULE-HV-01..04
  - Verificação de conformidade inter-nível (conservação-como-conjunto) — elo vertical ausente
  - Enforcement Contracts de atos de governança (EC-HG-001..004, EC-HV-001)
  - Resolução (proposta) de L-001

MODIFIED (especialização de regra herdada):
  - RULE-HD-02/03 (coerência/supressão HORIZONTAL, spec↔canon) → estendidas ao eixo VERTICAL
    (spec-pai↔spec-filha) como RULE-HV-03/RULE-HV-02, sem alterar o texto das RULE-HD originais.
    [Justificativa: a herança vertical é um eixo distinto; a mecânica de delta é reutilizada.]

REMOVED (só com governança — nunca implícito):
  - (vazio)
```

---

## D0 — Missão (Intenção)

A SPEC-019 especifica o comportamento do **Harness Governance & Evolution**: a camada que **governa o próprio Harness de Especificação do SOT** — como Specs e RULEs são criadas, alteradas, versionadas, homologadas, revertidas e auditadas, sob quais autoridades e com que garantias de compatibilidade e conservação de requisitos. [FONTE: ROADMAP §11]

A Spec cobre duas responsabilidades acopladas:

**A) Governança & Evolução (baseline §11):** quem pode alterar Specs; quem cria RULE; quem aprova; versionamento; emendas; Constitution Check; análise de impacto (schemas/RAG/Skills/testes); compatibilidade; rollback; exceções; auditoria. **Resolve L-001.**

**B) Contrato de Herança Vertical macro→micro (EUA-E17 Q1, homologado):** normativiza a mecânica conceitual de decomposição pai→filho do GEH-001 §6 como regra formal de **conservação de requisitos entre harnesses** de níveis diferentes + **verificação de conformidade inter-nível**. É o elo vertical que o MAN-001 (convergência horizontal entre Master Contracts) não cobre. [FONTE: DHR-EUA-E17 §2 Q1; EUA-E17 §3.3]

**O que a Missão NÃO é (fronteira):** a SPEC-019 governa o **processo de especificação** (spec-time). Não é governança de runtime cognitivo (MC-GOV-001, diferido), não redefine o trio de agentes nem a hierarquia analítica, e não cria autoridade nova — a única autoridade de homologação permanece Andraus. [FONTE: EUA-E17 §0, §3.4; DHR-EUA-E17]

**Status epistemológico:** a SPEC-019 é FATO ARQUITETURAL candidato a baseline. GMC-001, SDD-001, RULES.md, INV-07/09 são FATO NORMATIVO. CR-001 Cap.7 (candidato) e Cap.8 (não-congelado) são FATO ARQUITETURAL — usados como convergência, não como baseline. GEH-001 é pano-de-fundo não-normativo.

---

## D1 — Escopo e Non-goals

### Dentro do escopo

| # | Item | Fonte |
|---|---|---|
| A1 | **Autoridade de alteração:** quem pode propor/verificar/homologar alteração de Spec e RULE (trio) | ROADMAP §11; GMC-001 Cap.2/5; SDD-001 §7 |
| A2 | **Ciclo de vida de RULE:** proposta (EUA-Exx) → verificação → homologação → registro em RULES.md | RULES.md; EUA-E04..E14 (padrão); GMC-001 Cap.5 |
| A3 | **Versionamento** de Specs/método/RULES: monotônico, MAJOR.MINOR, baseline único vigente | GMC-001 Cap.3; CR-001 Cap.7 (cand.); INV-07 |
| A4 | **Emendas** (EUA-Exx) e sua ata de homologação (DHR) | Prática EUA/DHR (FATO NORMATIVO observado) |
| A5 | **Constitution Check** como gate obrigatório (CC-01..CC-10) antes de Plan/homologação | SDD-001 §4; atomic-spec §10.5 |
| A6 | **Análise de Impacto** obrigatória: schemas / RAG / Skills / testes / modelos dependentes | GMC-001 Cap.3; CR-001 Cap.7 (cand.) |
| A7 | **Compatibilidade:** classificação Patch/Minor/Major + declaração explícita de quebra | CR-001 Cap.7 (cand.); GMC-001 Cap.3 (Categoria A/B/C) |
| A8 | **Rollback:** reversão declarada a baseline anterior registrado, sem deleção | INV-07; GMC-001 Cap.3/5 (reabertura BASELINED→DRAFT) |
| A9 | **Exceções:** desvio temporário com prazo, autoridade e encerramento formal | CR-001 Cap.8 (não-congelado — FATO ARQUITETURAL) |
| A10 | **Auditoria:** todo ato de governança reconstruível (DHR + trilha) | GMC-001 Cap.5; CONSTITUTION P13; CR-001 Cap.8 CRR86 (cand.) |
| B1 | **Contrato de Herança Vertical:** declaração pai→filho por ID+versão | GEH-001 §6; EUA-E04 (CC-08); EUA-E17 Q1 |
| B2 | **Conservação de requisitos** (conjunto do pai preservado na filha) | EUA-E17 §1.1 Dep.3; GEH-001 §6.4/§6.7 |
| B3 | **Verificação de conformidade inter-nível** (conservação-como-conjunto) | AUDITORIA §12/Q14; MAN-001 (fronteira horizontal) |

### Fora do escopo (Non-goals)

| Item | Pertence a | Justificativa |
|---|---|---|
| Governança de runtime cognitivo / policy runtime | MC-GOV-001 (BL-013) / SPEC-018 runtime | Referência externa diferida; escopo runtime ≠ spec-time [FONTE: DHR-MC-GOV-001] |
| Re-especificar o trio de agentes ou a hierarquia | — | Vedado por EUA-E17 §0/§3.4 (T-08) |
| Critérios de avaliação constitutivos (correctness, grounding, …) | SPEC-020 (núcleo A) | Antecipada, mas independente; apenas gancho de dependência aqui |
| Modelo de maturidade L0–L4 por spec | SPEC-021 | Segue o núcleo A da SPEC-020 |
| Redefinir GMC-001 / CR-001 / SDD-001 | GMC-001/CR-001/SDD-001 (governança canônica) | CONST-01; a SPEC-019 constrói SOBRE eles |
| Ciclo P12 de evolução do conhecimento (Learning) | SPEC-018 | K-001 em aberto |
| Fórmula/pesos/limiares do Conviction Vector | SPEC-003 (CCM-001) | J-001 em aberto — [DECISÃO NECESSÁRIA] |

---

## D2 — Regras

> **Etiqueta:** RULE-HG-* e RULE-HV-* abaixo são **[PROPOSTA]** — tornam-se normativas apenas na homologação de Andraus + registro no RULES.md pelo Controlador (nova seção "Regras de Governança do Harness (RULE-HG)" e "Regras de Herança Vertical (RULE-HV)"). Até lá, não são invocáveis como FATO NORMATIVO. As RULE-HD-01..04, RULE-GMC-*, RULE-SDD-*, RULE-PPQ-001 citadas **já existem** (RULES.md v1.1 / EUA-E04).

### Governança & Evolução (RULE-HG) — [PROPOSTA]

```
RULE-HG-01: Toda alteração de Spec/RULE/método homologado DEVE percorrer o trio
            (Especificador propõe → Revisor verifica → Andraus homologa → Controlador registra).
            Edição direta de baseline sem esse fluxo é violação de INV-09.
            [Fonte: SDD-001 §7; GMC-001 Cap.5; INV-09]

RULE-HG-02: RULE nova (ou emenda de RULE) SÓ é normativa após homologação de Andraus e registro
            no RULES.md pelo Controlador. RULE em proposta permanece [PROPOSTA] — não vinculante.
            Policies/RULEs NÃO são auto-aprovadas.
            [Fonte: ENF-05; GMC-001 Cap.5 "nenhuma alteração produz efeito antes do registro"]

RULE-HG-03: Parecer CONFORME do Revisor NÃO autoriza vigência; apenas atesta integridade.
            A vigência decorre exclusivamente da homologação de Andraus (decisão ≠ execução).
            [Fonte: RULE-DEC-01 (EUA-E13); GMC-001 Cap.5 (segregação); PAP-001]

RULE-HG-04: Toda proposta de alteração DEVE conter Análise de Impacto explícita sobre
            schemas, RAG, Skills, testes e modelos dependentes, e classificação de compatibilidade
            (Patch/Minor/Major). Proposta sem Análise de Impacto NÃO avança para verificação.
            [Fonte: GMC-001 Cap.3 (Análise de Impacto Obrigatória); CR-001 Cap.7 (cand.)]

RULE-HG-05: Versionamento é monotônico. Baseline anterior é preservado (SUPERSEDED, nunca deletado).
            Rollback é reversão DECLARADA e registrada a um baseline anterior — nunca deleção nem
            reescrita retroativa de identificador Vigente.
            [Fonte: INV-07; CR-001 Cap.7 CRR36/CRR47 (cand.); GMC-001 Cap.4]

RULE-HG-06: O Constitution Check (CC-01..CC-10) é gate obrigatório ANTES do Plan e ANTES da
            homologação. Falha em item de severidade Crítica = rejeição antes do Plan.
            [Fonte: SDD-001 §4; atomic-spec §10.5]

RULE-HG-07: Exceção arquitetural DEVE possuir justificativa, prazo/condição de encerramento e
            autoridade responsável. Exceção permanente ou implícita é proibida; encerramento é
            ato formal registrado.
            [Fonte: CR-001 Cap.8 CRR58/59/85 (FATO ARQUITETURAL — não-congelado); PPQ-001 dial GES]

RULE-HG-08: Todo ato de governança (homologação, emenda, rollback, exceção) DEVE produzir registro
            DHR auditável e reconstruível (gatilho → autoridade → decisão → artefato → registro).
            [Fonte: CONSTITUTION P13; GMC-001 Cap.5 (auditabilidade); CR-001 Cap.8 CRR86 (cand.)]
```

### Herança Vertical macro→micro (RULE-HV) — [PROPOSTA]

```
RULE-HV-01: Toda spec-filha (micro-harness) derivada de uma spec-pai (macro-harness) DEVE declarar
            o pai por ID+VERSÃO baseline e CONSERVAR o conjunto de requisitos/invariantes do pai
            (conservação-como-conjunto), estendendo o bloco §8.3/INHERITS ao eixo VERTICAL.
            [Fonte: EUA-E04 §8.3; GEH-001 §6; EUA-E17 Q1]

RULE-HV-02: Requisito herdado do pai NÃO PODE ser suprimido na filha fora do campo REMOVED com
            referência de homologação de Andraus. Supressão silenciosa entre níveis =
            NÃO CONFORME Crítica. (Extensão vertical de RULE-HD-03.)
            [Fonte: RULE-HD-03; EUA-E17 §1.1 Dep.3]

RULE-HV-03: Requisito local da filha NÃO PODE contradizer requisito do pai (coerência vertical).
            Precedência em conflito: pai (macro) > filha (micro); PC > PB/PE > regra local.
            (Extensão vertical de RULE-HD-02.)
            [Fonte: RULE-HD-02; INV-01]

RULE-HV-04: A conformidade inter-nível DEVE ser verificável: a cobertura do CONJUNTO de obrigações
            do pai pelo conjunto conservado da filha é auditável pelo Revisor como conjunto (não
            apenas obrigação-a-obrigação). Distingue-se da convergência HORIZONTAL do MAN-001.
            [Fonte: MAN-001 (horizontal); AUDITORIA §12/Q14; EUA-E17 §3.3]
```

---

## Critérios de Aceitação (EARS)

1. Quando um agente tenta alterar uma Spec homologada sem o fluxo do trio, o Harness Governance DEVE rejeitar a alteração como violação de INV-09.
2. Quando uma RULE é proposta mas ainda não homologada, o Harness Governance DEVE tratá-la como [PROPOSTA] não-vinculante, nunca como FATO NORMATIVO.
3. Quando o Revisor emite parecer CONFORME, o Harness Governance NÃO DEVE tratar isso como autorização de vigência — só a homologação de Andraus a confere.
4. Quando uma proposta de alteração não inclui Análise de Impacto (schemas/RAG/Skills/testes), o Harness Governance DEVE bloquear o avanço para verificação.
5. Quando uma mudança é classificada Major (quebra de compatibilidade), o Harness Governance DEVE exigir declaração explícita de quebra e nova baseline major.
6. Quando um rollback é solicitado, o Harness Governance DEVE reverter a um baseline anterior registrado sem deletar nem reescrever o histórico (INV-07).
7. Quando uma exceção é concedida, o Harness Governance DEVE exigir prazo/condição de encerramento e autoridade responsável; exceção sem prazo é rejeitada.
8. Quando uma spec-filha é derivada de uma spec-pai, o Harness Governance DEVE exigir declaração do pai (ID+versão) e conservação do conjunto de requisitos do pai.
9. Quando uma spec-filha suprime um requisito do pai fora do campo REMOVED homologado, a verificação inter-nível DEVE reprovar (NÃO CONFORME Crítica).
10. Quando um requisito local da filha contradiz um requisito do pai, a verificação inter-nível DEVE reprovar por incoerência vertical (precedência pai > filha).

---

## D3 — Comportamento (BASpecs)

### BASpec-HG-001 — Alteração de Spec exige o trio

```
BASpec-HG-001:
  QUANDO:       Uma alteração é proposta sobre uma Spec/RULE/método em estado BASELINED
  ENTÃO:        Harness Governance exige o fluxo Especificador→Revisor→Andraus→Controlador;
                rejeita qualquer efetivação que não tenha registro de homologação de Andraus
  PORQUE:       "Congelado/Baseline" só muda por homologação explícita (INV-09); segregação de
                responsabilidades (GMC-001 Cap.5)
  REFERÊNCIA:   RULE-HG-01; INV-09; GMC-001 Cap.5; SDD-001 §7
  VERIFICADO POR:
    DADO        SPEC-001 em estado BASELINED
    QUANDO      um ator tenta editar o baseline sem DHR de homologação
    ENTÃO       Harness Governance rejeita com "BASELINE_CHANGE_REQUIRES_HOMOLOGATION"
    VERIFICAÇÃO estado do baseline inalterado; nenhum registro de vigência criado
```

### BASpec-HG-002 — RULE só é normativa após homologação + registro

```
BASpec-HG-002:
  QUANDO:       Uma RULE nova (ou emenda) é proposta via EUA-Exx e recebe parecer CONFORME
  ENTÃO:        Harness Governance mantém a RULE como [PROPOSTA] até a homologação de Andraus e o
                registro no RULES.md pelo Controlador; só então a marca como FATO NORMATIVO
  PORQUE:       Policies/RULEs não são auto-aprovadas (ENF-05); nenhuma alteração produz efeito
                antes do registro (GMC-001 Cap.5)
  REFERÊNCIA:   RULE-HG-02; RULE-HG-03; ENF-05
  VERIFICADO POR:
    DADO        RULE-XYZ proposta com parecer CONFORME e sem homologação
    QUANDO      um consumidor consulta o status normativo de RULE-XYZ
    ENTÃO       Harness Governance retorna status = [PROPOSTA] (não-vinculante)
    VERIFICAÇÃO RULE-XYZ ausente do RULES.md vigente; status != FATO NORMATIVO
```

### BASpec-HG-003 — Análise de Impacto obrigatória

```
BASpec-HG-003:
  QUANDO:       Uma proposta de alteração de Spec/RULE é submetida à verificação
  ENTÃO         Harness Governance exige Análise de Impacto (schemas, RAG, Skills, testes, modelos
                dependentes) + classificação de compatibilidade (Patch/Minor/Major); ausência bloqueia
  PORQUE:       Compatibilidade retroativa é objetivo prioritário; proposta sem impacto não avança
                (GMC-001 Cap.3)
  REFERÊNCIA:   RULE-HG-04; GMC-001 Cap.3; CR-001 Cap.7 (cand.)
  VERIFICADO POR:
    DADO        Proposta de emenda sem seção de Análise de Impacto
    QUANDO      Harness Governance avalia elegibilidade para verificação
    ENTÃO       proposta rejeitada com "IMPACT_ANALYSIS_REQUIRED"; não avança ao Revisor
    VERIFICAÇÃO proposta.status == BLOQUEADA; motivo registrado
```

### BASpec-HG-004 — Rollback preserva histórico (INV-07)

```
BASpec-HG-004:
  QUANDO:       Um rollback a baseline anterior é homologado
  ENTÃO         Harness Governance reverte a vigência ao baseline anterior REGISTRADO, marcando o
                baseline revertido como SUPERSEDED; nenhum identificador é deletado ou reescrito
  PORQUE:       Versionamento monotônico (INV-07); baseline anterior permanece recuperável
                (CR-001 Cap.7 CRR47, cand.)
  REFERÊNCIA:   RULE-HG-05; INV-07; GMC-001 Cap.4
  VERIFICADO POR:
    DADO        Método atomic-spec em v1.5 (hipotético) com v1.4 registrada
    QUANDO      Andraus homologa rollback para v1.4
    ENTÃO       vigência = v1.4; v1.5 marcada SUPERSEDED e preservada; histórico intacto
    VERIFICAÇÃO catálogo contém v1.4 (BASELINED) e v1.5 (SUPERSEDED); nada deletado
```

### BASpec-HG-005 — Exceção exige prazo e encerramento

```
BASpec-HG-005:
  QUANDO:       Uma exceção (desvio temporário do fluxo/regra) é concedida
  ENTÃO         Harness Governance exige justificativa + prazo/condição de encerramento + autoridade
                responsável; registra a exceção; rejeita exceção sem prazo (proibida permanente/implícita)
  PORQUE:       Não existem exceções implícitas; exceção deve possuir condição de encerramento
                (CR-001 Cap.8 CRR58/59, FATO ARQUITETURAL — não-congelado)
  REFERÊNCIA:   RULE-HG-07; CR-001 Cap.8 (cand.); PPQ-001 dial GES
  VERIFICADO POR:
    DADO        Solicitação de exceção sem prazo de encerramento
    QUANDO      Harness Governance avalia a concessão
    ENTÃO       exceção rejeitada com "EXCEPTION_REQUIRES_DEADLINE"
    VERIFICAÇÃO nenhuma exceção permanente registrada
```

### BASpec-HV-001 — Declaração e conservação vertical pai→filha

```
BASpec-HV-001:
  QUANDO:       Uma spec-filha (micro-harness) é derivada de uma spec-pai (macro-harness)
  ENTÃO         Harness Governance exige que a filha declare o pai por ID+VERSÃO e conserve o
                conjunto de requisitos/invariantes do pai (INHERITS estendido ao eixo vertical)
  PORQUE:       Falta o elo vertical (conservação entre níveis) que o MAN-001 horizontal não cobre;
                herança-por-delta declarada e auditável (EUA-E04)
  REFERÊNCIA:   RULE-HV-01; GEH-001 §6; EUA-E04 §8.3; EUA-E17 Q1
  VERIFICADO POR:
    DADO        Spec-filha SPEC-F derivada de spec-pai SPEC-P v1.0
    QUANDO      Harness Governance verifica o bloco Herança/Delta de SPEC-F
    ENTÃO       exige INHERITS: SPEC-P v1.0 + conjunto de requisitos conservado
    VERIFICAÇÃO SPEC-F.INHERITS referencia "SPEC-P v1.0"; conjunto-pai coberto
```

### BASpec-HV-002 — Bloqueio de supressão silenciosa entre níveis

```
BASpec-HV-002:
  QUANDO:       Uma spec-filha omite/suprime um requisito herdado do pai fora do campo REMOVED
                homologado
  ENTÃO         Verificação inter-nível REPROVA com "VERTICAL_REQUIREMENT_DROPPED" (NÃO CONFORME Crítica)
  PORQUE         Nenhum requisito herdado pode ser suprimido fora de REMOVED com homologação
                (extensão vertical de RULE-HD-03); previne Harness Drift/Debt
  REFERÊNCIA:   RULE-HV-02; RULE-HD-03; EUA-E17 §1.1 Dep.3
  VERIFICADO POR:
    DADO        SPEC-F herda de SPEC-P um invariante I; SPEC-F não o conserva e REMOVED está vazio
    QUANDO      Revisor executa a verificação de conformidade inter-nível
    ENTÃO         resultado = NÃO CONFORME Crítica, código "VERTICAL_REQUIREMENT_DROPPED"
    VERIFICAÇÃO conjunto-conservado(SPEC-F) ⊉ conjunto-obrigações(SPEC-P); REMOVED vazio → reprova
```

### BASpec-HV-003 — Coerência vertical (filha não contradiz pai)

```
BASpec-HV-003:
  QUANDO:       Um requisito local (ADDED/MODIFIED) da filha contradiz um requisito do pai
  ENTÃO         Verificação inter-nível REPROVA com "VERTICAL_INCOHERENCE"; precedência pai > filha
  PORQUE         Coerência vertical: micro não pode contradizer macro (extensão vertical de RULE-HD-02)
  REFERÊNCIA:   RULE-HV-03; RULE-HD-02; INV-01
  VERIFICADO POR:
    DADO        SPEC-P exige "X DEVE"; SPEC-F ADDED declara "X NÃO DEVE"
    QUANDO      Revisor executa a verificação inter-nível
    ENTÃO         resultado = NÃO CONFORME Crítica, código "VERTICAL_INCOHERENCE"
    VERIFICAÇÃO conflito detectado; precedência aplicada = pai
```

---

## D5 — Máquina de Estados de Governança (aplica GMC-001 — NÃO redefine)

A SPEC-019 **não cria** estados próprios: aplica os estados de governança do GMC-001 Cap.2/4 (e o modelo de duas dimensões do CR-001 Cap.7, candidato) aos artefatos do Harness de Especificação (Spec, RULE, método). [FONTE: GMC-001 Cap.2; CR-001 Cap.7 (cand.)]

### Estados do artefato normativo [FONTE: GMC-001 Cap.2/4]

| Estado | Significado no Harness de Especificação |
|---|---|
| DRAFT | Spec/RULE/emenda em elaboração |
| UNDER_REVIEW | Em verificação pelo Revisor |
| APPROVED | Parecer CONFORME (técnico) — transitório; NÃO é vigência |
| BASELINED | Homologado por Andraus + registrado (Controlador) — vigente |
| SUPERSEDED | Substituído por versão posterior (rastreabilidade) |
| DEPRECATED | Em descontinuação (ainda válido, não recomendado) |
| RETIRED | Retirado oficialmente |
| REJECTED | Encerrado sem aprovação |

### Transições relevantes

```
DRAFT        -> UNDER_REVIEW        (submissão ao Revisor)
UNDER_REVIEW -> APPROVED            (parecer CONFORME — técnico, NÃO vigência)
UNDER_REVIEW -> DRAFT              (NÃO CONFORME — retorno com achados)
APPROVED     -> BASELINED           (homologação de Andraus + registro do Controlador)
BASELINED    -> SUPERSEDED          (nova versão homologada)
BASELINED    -> DRAFT               (reabertura formal — inicia novo ciclo; histórico preservado)
BASELINED    -> DEPRECATED -> RETIRED (descontinuação governada)
qualquer      -> REJECTED           (encerramento sem aprovação)
```

**Invariante de estado (reforço):** APPROVED ≠ vigência. Só BASELINED (pós-homologação de Andraus) confere efeito normativo (RULE-HG-03). O rollback é a transição declarada `BASELINED(vN) → SUPERSEDED` + reativação de `vN-1` como vigente, sem deleção (RULE-HG-05).

---

## D6 — Protocolo de Governança (sequência de emenda/homologação)

Sequência canônica de alteração do Harness de Especificação [FONTE: fluxo EUA-Exx/DHR observado; GMC-001 Cap.5; ROADMAP §23]:

```
1. Especificador redige a PROPOSTA (EUA-Exx ou nova Spec) — inclui Análise de Impacto (RULE-HG-04)
   e, se decompõe pai→filho, o bloco Herança/Delta vertical (RULE-HV-01).
2. Constitution Check (CC-01..CC-10) — gate antes do Plan (RULE-HG-06).
3. Revisor (GRE-001/HRE-001) verifica → parecer CONFORME / CONFORME condicional / NÃO CONFORME.
   Inclui verificação de conformidade inter-nível quando há herança vertical (RULE-HV-04).
4. Andraus homologa (única autoridade de vigência) — decide questões abertas.
5. Controlador registra: DHR (ata) + edição de baseline + Catálogo Oficial + CONFLICT-MAP (se colisão).
6. Passo 11-bis (ROADMAP §23): consultar RMR-001 — tratar itens ATIVADOS pelo gatilho.
7. RPSA (EUA-E16): re-sincronizar especificador.md/revisor.md (carimbo `sincronizado-até`).
8. Só então: próxima Spec / vigência plena.
```

Rollback e exceção seguem o mesmo protocolo (proposta → verificação → homologação → registro), com o artefato específico (declaração de rollback / registro de exceção com prazo).

---

## D7 — Cenários de Teste

### Cenário-HG-T01 — RULE proposta não é vinculante antes da homologação

```
DADO        RULE-HV-01 em estado [PROPOSTA] com parecer CONFORME do Revisor
QUANDO      um consumidor pergunta se RULE-HV-01 é FATO NORMATIVO
ENTÃO       Harness Governance responde status = [PROPOSTA]; não vinculante
VERIFICAÇÃO RULES.md vigente não contém RULE-HV-01; status != FATO NORMATIVO
```

### Cenário-HG-T02 — Bloqueio de proposta sem Análise de Impacto

```
DADO        Emenda EUA-Ezz submetida sem seção de Análise de Impacto
QUANDO      Harness Governance avalia elegibilidade para verificação
ENTÃO       proposta bloqueada; código "IMPACT_ANALYSIS_REQUIRED"
VERIFICAÇÃO proposta não encaminhada ao Revisor; motivo registrado
```

### Cenário-HG-T03 — Rollback preserva histórico

```
DADO        método em v1.5 com v1.4 registrada (BASELINED anterior)
QUANDO      Andraus homologa rollback para v1.4
ENTÃO       v1.4 volta a VIGENTE; v1.5 -> SUPERSEDED (preservada)
VERIFICAÇÃO catálogo: v1.4 BASELINED + v1.5 SUPERSEDED; nenhuma deleção (INV-07)
```

### Cenário-HV-T04 — Conservação vertical bem-sucedida

```
DADO        SPEC-F declara INHERITS: SPEC-P v1.0 e conserva os 3 invariantes do pai
QUANDO      Revisor executa verificação de conformidade inter-nível
ENTÃO       conjunto-conservado(SPEC-F) ⊇ conjunto-obrigações(SPEC-P) → PASS
VERIFICAÇÃO cobertura do conjunto-pai = 100%; nenhum requisito órfão
```

---

## D8 — Cenários Adversariais [reforço de integridade de governança]

Princípio transversal: **fail-closed** — em qualquer ambiguidade sobre autoridade/vigência, o Harness Governance NÃO confere efeito normativo e retorna erro específico.

### ADV-HG-01 — RULE auto-aprovada (sem homologação de Andraus)
**DADO:** RULE proposta com parecer CONFORME, sem homologação de Andraus
**QUANDO:** um ator tenta marcá-la como FATO NORMATIVO / registrá-la no RULES.md
**ENTÃO:** rejeitar (fail-closed) com `RULE_NOT_HOMOLOGATED`; RULE permanece [PROPOSTA]
**PORQUE:** policies não são auto-aprovadas (ENF-05; RULE-HG-02); CONFORME ≠ vigência (RULE-HG-03)
**VERIFICAÇÃO:** RULES.md inalterado; nenhum status FATO NORMATIVO atribuído

### ADV-HG-02 — Edição direta de baseline sem trio
**DADO:** Spec em BASELINED
**QUANDO:** um ator edita o baseline sem DHR de homologação
**ENTÃO:** rejeitar com `BASELINE_CHANGE_REQUIRES_HOMOLOGATION`; estado inalterado
**PORQUE:** INV-09 (sem baseline informal); RULE-HG-01
**VERIFICAÇÃO:** baseline inalterado; nenhum registro de vigência

### ADV-HG-03 — Exceção permanente / sem prazo
**DADO:** solicitação de exceção sem condição de encerramento
**QUANDO:** Harness Governance avalia a concessão
**ENTÃO:** rejeitar com `EXCEPTION_REQUIRES_DEADLINE`
**PORQUE:** exceções implícitas/permanentes proibidas (RULE-HG-07; CR-001 Cap.8 CRR59, cand.)
**VERIFICAÇÃO:** nenhuma exceção permanente registrada

### ADV-HG-04 — Mudança Major sem declaração de quebra
**DADO:** alteração que remove/altera comportamento normativo vigente, rotulada como Minor
**QUANDO:** Harness Governance/Revisor classifica a compatibilidade
**ENTÃO:** reclassificar para Major; exigir declaração explícita de quebra + nova baseline major
**PORQUE:** quebra de compatibilidade não pode ser implícita (RULE-HG-04; CR-001 Cap.7 CRR56, cand.)
**VERIFICAÇÃO:** proposta não avança como Minor; exige declaração Major

### ADV-HV-05 — Supressão silenciosa de requisito do pai
**DADO:** SPEC-F herda invariante I de SPEC-P; SPEC-F não conserva I e REMOVED está vazio
**QUANDO:** Revisor executa verificação inter-nível
**ENTÃO:** NÃO CONFORME Crítica, `VERTICAL_REQUIREMENT_DROPPED`
**PORQUE:** supressão fora de REMOVED homologado é vedada (RULE-HV-02; RULE-HD-03)
**VERIFICAÇÃO:** conjunto-conservado ⊉ conjunto-pai; reprova

### ADV-HV-06 — Contradição vertical (filha nega pai)
**DADO:** SPEC-P exige "X DEVE"; SPEC-F ADDED declara "X NÃO DEVE"
**QUANDO:** Revisor executa verificação inter-nível
**ENTÃO:** NÃO CONFORME Crítica, `VERTICAL_INCOHERENCE`; precedência pai > filha
**PORQUE:** coerência vertical (RULE-HV-03; RULE-HD-02; INV-01)
**VERIFICAÇÃO:** conflito detectado; precedência = pai

### ADV-HV-07 — Confundir herança vertical com convergência horizontal (MAN-001)
**DADO:** proposta trata conservação pai→filha como se fosse convergência horizontal entre Master Contracts
**QUANDO:** verificação inter-nível é solicitada
**ENTÃO:** Harness Governance distingue os eixos; aplica RULE-HV-04 (vertical), não MAN-001 (horizontal)
**PORQUE:** MAN-001 cobre convergência horizontal; o elo vertical é distinto (EUA-E17 §3.3)
**VERIFICAÇÃO:** verificação aplicada = conservação-como-conjunto vertical; MAN-001 não substitui

> **Cobertura:** 7 cenários adversariais (mínimo para HIGH cumprido; casos de negação de governança e de herança vertical).

---

## Enforcement Contracts

### EC-HG-001 — Homologação/alteração de baseline (Spec/RULE/método)

```
CAPABILITY   : Conferir/alterar vigência normativa de um artefato do Harness de Especificação
EFFECT       : Transição para BASELINED (efeito normativo) + registro DHR + edição de baseline
PRECOND      : (proposta percorreu o trio) AND (parecer do Revisor emitido) AND
               (homologação explícita de Andraus registrada) AND (Constitution Check PASS)
POSTCOND     : Artefato em BASELINED; versão anterior SUPERSEDED e preservada; DHR registrado
POLICY       : RULE-HG-01, RULE-HG-03, RULE-HG-06; INV-09; GMC-001 Cap.5
LEVEL        : E3 (Crítico — efeito normativo; alta criticidade × irreversibilidade prática)
FAILURE-MODE : Fail-closed — sem homologação registrada, nenhum efeito normativo; artefato permanece
               em APPROVED/DRAFT; log de rejeição
EVIDENCE     : DHR (ata) com autoridade, decisão, artefato; entrada no Catálogo Oficial
             + método de observação de falso-DENY: amostragem de propostas rejeitadas por
               "falta de homologação" que possuíam homologação válida (limiar = gap aberto, ENF-07)
```

### EC-HG-002 — Criação/emenda de RULE

```
CAPABILITY   : Tornar uma RULE normativa (registro no RULES.md)
EFFECT       : RULE passa de [PROPOSTA] a FATO NORMATIVO no RULES.md
PRECOND      : (homologação de Andraus) AND (registro pelo Controlador)
POSTCOND     : RULE vigente no RULES.md; seção RULE-HG/RULE-HV criada se inexistente
POLICY       : RULE-HG-02; ENF-05
LEVEL        : E3 (Crítico — efeito normativo)
FAILURE-MODE : Fail-closed — RULE não-homologada permanece [PROPOSTA] não-vinculante
EVIDENCE     : Diff do RULES.md + DHR; método de falso-DENY amostral (ENF-07 — gap aberto)
```

### EC-HG-003 — Rollback de baseline

```
CAPABILITY   : Reverter a vigência a um baseline anterior registrado
EFFECT       : Baseline anterior volta a VIGENTE; baseline atual → SUPERSEDED
PRECOND      : (baseline anterior existe e está registrado) AND (rollback homologado por Andraus)
POSTCOND     : Vigência revertida; histórico integralmente preservado (INV-07); DHR registrado
POLICY       : RULE-HG-05; INV-07; CR-001 Cap.7 (cand.)
LEVEL        : E3 (Crítico — reversão de vigência normativa)
FAILURE-MODE : Fail-closed — sem baseline anterior registrado, rollback é rejeitado (nunca deleta)
EVIDENCE     : Registro de rollback + estados de catálogo (BASELINED/SUPERSEDED)
```

### EC-HG-004 — Concessão de exceção

```
CAPABILITY   : Autorizar desvio temporário do fluxo/regra
EFFECT       : Exceção registrada, com prazo e autoridade
PRECOND      : (justificativa) AND (prazo/condição de encerramento) AND (autoridade responsável)
POSTCOND     : Exceção rastreável com condição de encerramento formal
POLICY       : RULE-HG-07; CR-001 Cap.8 (cand., não-congelado)
LEVEL        : E3 (Crítico — desvio de norma vigente)
FAILURE-MODE : Fail-closed — exceção sem prazo é rejeitada; nenhuma exceção permanente/implícita
EVIDENCE     : Registro de exceção (gatilho, prazo, autoridade, encerramento)
```

### EC-HV-001 — Verificação de conformidade inter-nível (gate de herança vertical)

```
CAPABILITY   : Verificar conservação do conjunto de requisitos do pai pela filha
EFFECT       : Gate de homologação da spec-filha (bloqueia se conjunto-pai não coberto)
PRECOND      : (filha declara pai por ID+versão) AND (conjunto-conservado(filha) ⊇ conjunto-obrigações(pai))
               AND (nenhum ADDED/MODIFIED contradiz o pai) AND (supressão só via REMOVED homologado)
POSTCOND     : Filha elegível a homologação apenas se a conservação-como-conjunto é satisfeita
POLICY       : RULE-HV-01..04; RULE-HD-02/03
LEVEL        : E3 (Crítico — integridade de herança entre níveis; previne Harness Drift)
FAILURE-MODE : Fail-closed — cobertura incompleta ou contradição → NÃO CONFORME Crítica; filha não homologa
EVIDENCE     : Relatório de cobertura do conjunto-pai; achados VERTICAL_REQUIREMENT_DROPPED/INCOHERENCE
```

---

## Resolução de L-001 (rastreabilidade)

[FONTE: atomic-spec §12 (L-001); ROADMAP §11; DHR-EUA-E17 §3]

- **O quê:** L-001 = "Governança do próprio harness / policy versionada". A SPEC-019 **propõe sua resolução** definindo o modelo de governança do Harness de Especificação.
- **Onde/como resolvida:** modelo de autoridade (trio — RULE-HG-01/03) · ciclo de vida e versionamento de RULE/Spec/método (D5; RULE-HG-02/05) · emenda EUA-Exx + DHR (D6) · Constitution Check como gate (RULE-HG-06) · Análise de Impacto + compatibilidade (RULE-HG-04) · rollback (EC-HG-003) · exceção (EC-HG-004) · auditoria (RULE-HG-08) · herança vertical (RULE-HV-*).
- **Efetivação:** a resolução de L-001 torna-se efetiva **na homologação de Andraus** desta Spec — não antes (CONS-01). Até lá, L-001 permanece formalmente **em aberto**, e esta Spec é a proposta de fechamento.
- **Fronteira de escopo de L-001 — RESOLVIDA (Andraus, 2026-09-22):** *"L-001 fecha integralmente na dimensão spec-time. Governança de runtime (como agentes vivos adotam políticas novas em operação) é escopo distinto — pertence à SPEC-018/K-001 e não é resíduo de L-001."* [FONTE: Decisão de Andraus sobre L-001-b, 2026-09-22]. A antiga decisão aberta L-001-b fica assim **encerrada**: não há resíduo runtime pendente de roteamento sob L-001; MC-GOV-001/BL-013 permanece diferida por seu próprio mérito, não como resto de L-001.

---

## Plan — arquitetura de processo (derivado da Spec)

### Natureza do componente
O Harness Governance & Evolution é um **processo de governança spec-time**, executado por papéis de autoridade (Andraus = homologação; Revisor = verificação; Especificador = proposta; Controlador = registro), não um componente cognitivo de runtime. [FONTE: GMC-001 Cap.2; SDD-001 §7]

### Roteamento de modelo (CEE-001 §5 / EUA-E19)
**N/A como chamada de LLM de runtime** — a SPEC-019 não descreve um agente cognitivo que roteia por Tipo I–V. Onde Especificador/Revisor são apoiados por LLM, o roteamento é governado pelas próprias configs de agente (EUA-E19: Especificador = claude-opus-4-8; Revisor = claude-sonnet-4-6) — fora do escopo desta Spec. [FONTE: EUA-E19; RMR-001 §6 nota]

### Dependências técnicas
GMC-001 (Baseline 1.0) · SDD-001 (Baseline 1.1) · RULES.md (v1.1) · atomic-spec (v1.4) · EUA-E04 (CC-08/RULE-HD) · PAP-001 · RMR-001 · EUA-E16 (RPSA). Convergência (não-baseline): CR-001 Cap.7/8 (candidato/não-congelado). Pano-de-fundo: GEH-001 §6 (não-normativo).

### Riscos técnicos e Salvaguardas
| Risco | Salvaguarda |
|---|---|
| Governança auto-aprovar RULE (bypass de Andraus) | ENF-05; RULE-HG-02/03; EC-HG-002 fail-closed |
| Rollback deletar histórico | INV-07; RULE-HG-05; EC-HG-003 fail-closed |
| Herança vertical mascarar supressão de requisito | RULE-HV-02; EC-HV-001 fail-closed |
| Confundir governança spec-time com runtime (MC-GOV) | Non-goal explícito; nota de gate BL-013 |
| Fechar L-001 sem homologação | CONS-01; resolução condicionada à homologação |

### Impacto (Análise de Impacto — RULE-HG-04 aplicada a esta própria Spec)
- **Schemas:** nenhum schema de runtime alterado; introduz o schema lógico de "registro de governança" (DHR) já praticado.
- **RAG:** nenhum; governança não escreve no KG/RAG.
- **Skills:** nenhuma Skill afetada.
- **Testes:** adiciona cenários D7/D8 de governança e herança vertical (checks.md).
- **Modelos dependentes:** GMC-001/SDD-001/CR-001 não alterados (construção SOBRE).
- **Compatibilidade:** **Minor** — adiciona comportamento (RULE-HG/HV) sem invalidar comportamento vigente; RULE-HD-01..04 preservadas; nenhuma RULE existente redefinida.

### Tasks (adiadas — fase spec-first)
BUILD/Tasks/Engineering Cards adiados (atomic-spec §14). Quando produzidas, aplicam SES-001 §59/§60 (CC-06/CC-07).

---

## Apêndice A — Schemas de referência (lógicos)

### Registro de governança (DHR) — schema lógico
```json
{
  "dhr_id": "DHR-EUA-Exx | DHR-SPEC-0xx",
  "objeto": "<artefato homologado>",
  "gatilho": "<proposta/decisão>",
  "autoridade": "Andraus",
  "parecer_revisor": "CONFORME | CONFORME condicional | NÃO CONFORME",
  "decisao": "<Q/A homologadas>",
  "compatibilidade": "Patch | Minor | Major",
  "estado_resultante": "BASELINED | SUPERSEDED | REJECTED",
  "preserva_historico": true
}
```

### Bloco de Herança Vertical (extensão do §8.3)
```
INHERITS (vertical):
  - Pai (macro-harness): <SPEC-P vX.Y>
  - Conjunto de requisitos conservados: [<req/invariante do pai>...]
ADDED (delta local da filha): [...]
MODIFIED (especialização): [...]
REMOVED (só com homologação de Andraus): [...]   # vazio por padrão
```

---

## Decisões Incidentes

### Fechadas / não incidentes
| Decisão | Status |
|---|---|
| B-001 (Conviction≠Synthesis) | FECHADA (não incidente) |
| EUA-E17 Q1 (herança vertical no escopo) | HOMOLOGADA — FATO NORMATIVO |

### Abertas — [DECISÃO NECESSÁRIA]
| ID | Descrição | Status | Impacto nesta Spec |
|---|---|---|---|
| **L-001** | Governança do próprio harness / policy versionada | EM ABERTO — **esta Spec propõe resolução; efetiva na homologação** | Núcleo da Spec; não declarado fechado (CONS-01) |
| **L-001-b** | Fronteira: L-001 cobre também policy de runtime? | **RESOLVIDA (Andraus, 2026-09-22)** — L-001 fecha integralmente em spec-time; runtime ≠ resíduo de L-001 (pertence a SPEC-018/K-001) | Sem resíduo runtime sob L-001 |
| **J-001** | Fórmula/pesos/limiares definitivos do Conviction Vector | EM ABERTO — pendente | Non-goal; não tocado |
| **K-DRIFT-GEH-01** | ROADMAP/EUA-E17 citam "GEH-001 §6 (Herança Vertical)", mas o §6 real do GEH-001 é "centralizar/descentralizar". A mecânica de conservação vertical está em §6.4/§6.7 (autoridade central, o que nunca descentralizar). | [INFERÊNCIA] resolvida por conteúdo; registrada para o Controlador confirmar/ajustar a referência | Não bloqueia; a normativização usa o conteúdo de §6, não o rótulo |

---

## Etiquetagem e Status Epistemológico (TRACE-06)

| Item | Etiqueta | Status |
|---|---|---|
| GMC-001 (papéis, estados, versionamento) | [FONTE] | FATO NORMATIVO (Baseline 1.0) |
| SDD-001 (Spec/Plan/Tasks, Constitution Check) | [FONTE] | FATO NORMATIVO (Baseline 1.1) |
| RULES.md (RULE-GMC/SDD/PPQ/HD) | [FONTE] | FATO NORMATIVO (v1.1) |
| INV-07/INV-09; ENF-05 | [FONTE] | FATO NORMATIVO |
| EUA-E04 (CC-08 / RULE-HD-01..04) | [FONTE] | FATO NORMATIVO (homologada) |
| EUA-E17 Q1 (herança vertical no escopo) | [FONTE] | FATO NORMATIVO (DHR-EUA-E17) |
| CR-001 Cap.7 (Patch/Minor/Major, compatibilidade) | [FONTE] | FATO ARQUITETURAL (candidato — não congelado) |
| CR-001 Cap.8 (exceções, encerramento formal) | [FONTE] | FATO ARQUITETURAL (fundação encerrada — não congelado) |
| GEH-001 §6 (decomposição macro→micro) | [FONTE] | Pano-de-fundo não-normativo |
| MC-GOV-001 (governança runtime) | [EXTERNO] | Referência externa — diferida (BL-013) |
| RULE-HG-01..08; RULE-HV-01..04 | [PROPOSTA] | Requer homologação para virar FATO NORMATIVO |
| Resolução de L-001 | [PROPOSTA] | Efetiva na homologação |
| L-001-b (fronteira runtime) | [DECISÃO — RESOLVIDA] | Fechada por Andraus 2026-09-22 (spec-time integral; runtime → SPEC-018/K-001) |
| K-DRIFT-GEH-01 (drift de referência §6) | [INFERÊNCIA] | Registrado para o Controlador |

---

## Autopré-check do Especificador (§7 do PEP-001)

```
[x] roadmap.md lido: SPEC-019 confirmada como próximo autorizado (§11/§21/§25); FASE GOV posição 1.
[x] atomic-spec.md lido: método v1.4 confirmado (v1.5 não homologada até 2026-09-22 — DHR-EUA-E17 §3).
[x] Nenhum invariante congelado violado (INV-01..10). INV-05/09 reforçados (RULE-DEC, RULE-HG).
[x] Constitution Check CC-01..CC-10 preenchido (N/A justificados em CC-01/03/06/07/10).
[x] Disciplinas N8–N17: RULE-DEC (decisão≠execução), RULE-MET-01 (não-fabricação), RULE-EPI. INDETERMINADO usado (L-001-b) — desde então RESOLVIDA por Andraus (2026-09-22).
[x] Referências externas: MC-GOV-001 [EXTERNO] não adotada (rótulos G-gates/I-GOV rejeitados); GEH-001 pano-de-fundo; CR-001 Cap.7/8 rotulados FATO ARQUITETURAL, não baseline.
[x] Spec sem implementação; Plan derivado; Tasks adiadas (spec-first).
[x] Critérios em EARS (10); BASpecs completas (HG-001..005, HV-001..003); RULEs citadas existentes (HD/GMC/SDD/PPQ) x propostas (HG/HV) claramente etiquetadas.
[x] Profundidade D0–D8 atingida (D5 estados; D6 protocolo; D7 cenários; D8 adversarial x7).
[x] Enforcement Contract em todo ato com efeito (EC-HG-001..004, EC-HV-001); nível E3; fail-closed.
[x] Status epistemológico aplicado (FATO NORMATIVO vs FATO ARQUITETURAL vs PROPOSTA); documentado ≠ homologado.
[x] CONS-01 respeitado: L-001 NÃO declarada fechada; J-001 intocada; nenhuma decisão aberta usada como invariante.
[x] Etiquetagem [FONTE]/[INFERÊNCIA]/[PROPOSTA]/[DECISÃO NECESSÁRIA]/[EXTERNO] aplicada.
[x] Conflitos registrados: K-DRIFT-GEH-01 (drift §6 — para o Controlador) e L-001-b (fronteira — RESOLVIDA por Andraus 2026-09-22) — não resolvidos em silêncio.
[x] Integridade: nenhuma fonte inventada; nenhum DHR/RULE fabricado; sem baseline informal.
[x] 4Es na ordem; latência N/A (governança spec-time, não sensível a latência de runtime).
[x] Dependências a montante homologadas (GMC/SDD/RULES/EUA-E04/E17); não downstream de bloqueador aberto.
[x] "VERIFY" da skill não apresentado como CONFORME nem homologação.
[x] Passo 11-bis: BL-013 ATIVADO tratado (nota de gate); BL-015 não dispara; BL-017 não incidente.
```

## Autopré-check de Redução de Viés (§7-bis — EUA-E18, obrigatório HIGH)

**Bloco A — pergunta adversarial por BASpec CRITICAL/HIGH:**
- BASpec-HG-002 (RULE não-vinculante): se errada, observável = uma RULE proposta sendo tratada como norma sem DHR → detectável por ausência de entrada no RULES.md. ENTÃO verificável por observador independente (consulta ao RULES.md). Negação coberta por ADV-HG-01.
- BASpec-HV-001/002 (conservação vertical): se errada, observável = filha homologada sem cobrir o conjunto-pai → detectável por diff de conjunto (cobertura < 100% com REMOVED vazio). Negação coberta por ADV-HV-05. Condição QUANDO-satisfeito-mas-ENTÃO-não-deve: filha que legitimamente remove requisito via REMOVED homologado → não reprova (tratado: REMOVED com homologação é exceção válida).
- BASpec-HG-004 (rollback): se errada, observável = histórico deletado → detectável por ausência do identificador anterior no catálogo. Negação: ADV — deleção proibida (INV-07).

**Bloco B — herança obrigação-a-obrigação (CC-08):** INHERITS lista GMC-001 v1.0, SDD-001 v1.1, RULES.md v1.1, atomic-spec v1.4, EUA-E04, INV-07/09, ENF-05 (ID+versão — RULE-HD-04). Evidência de satisfação: cada RULE-HG/HV ancora a uma obrigação herdada (RULE-HG-02←ENF-05; RULE-HG-05←INV-07; RULE-HG-01←INV-09; RULE-HV-02←RULE-HD-03; RULE-HV-03←RULE-HD-02). Nenhuma obrigação herdada suprimida (REMOVED vazio) nem contradita (RULE-HD-02: MODIFIED apenas estende RULE-HD ao eixo vertical, sem alterar seu texto). *(Nota de delimitação §7-bis Bloco B: a regra escrita de conservação-como-conjunto é criada AQUI — é o objeto homologado da SPEC-019, EUA-E17 §2 Q1=SIM; não é decisão de escopo em aberto.)*

**Bloco C — epistêmico (RULE-EPI/CAU/PRB):** nenhuma afirmação causal forte não-fundamentada; nenhuma hipótese como fato (CR-001 Cap.7/8 rotulados candidato/não-congelado, não baseline); INDETERMINADO usado em L-001-b (desde então RESOLVIDA por Andraus 2026-09-22); nenhuma probabilidade/precisão numérica declarada sem base.

**Bloco D — reforço de escopo:** a Spec produz governança de processo (não executa runtime); INV-05/RULE-DEC reconfirmados (§7); nenhuma BASpec cruza a fronteira SOT→execução; dependência de Andraus em L-001 (resolução PROPOSTA, efetiva na homologação) marcada [DECISÃO NECESSÁRIA], não como fato; L-001-b já RESOLVIDA (Andraus 2026-09-22).

---

**Pronto para revisão.**

[DECISÃO NECESSÁRIA] em aberto nesta Spec:
- **L-001** — resolução PROPOSTA por esta Spec; efetiva na homologação de Andraus (não fechada aqui).

RESOLVIDAS antes da revisão:
- **L-001-b** — fronteira runtime: **RESOLVIDA por Andraus (2026-09-22)** — L-001 fecha integralmente em spec-time; governança de runtime pertence à SPEC-018/K-001 e não é resíduo de L-001.

Registrado para o Controlador (não bloqueia):
- **K-DRIFT-GEH-01** — referência "GEH-001 §6" (rótulo "Herança Vertical") vs conteúdo real do §6; ajustar as instâncias pertinentes do ROADMAP e da EUA-E17 para "GEH-001 §6.4/§6.7". Conteúdo usado está correto; apenas o rótulo de seção diverge.
