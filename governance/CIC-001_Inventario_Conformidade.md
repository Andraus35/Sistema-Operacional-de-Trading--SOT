# CIC-001 --- Inventario de Conformidade de Principios do SOT

| Campo | Valor |
|---|---|
| ID | CIC-001 |
| Versao | 1.3 --- **Hygiene #1 FECHADO** (RCH-001; homologado 2026-09-20): emenda de inversoes contextuais do CONFLICT-MAP homologada → celulas CONFLICT-MAP×PCO/PS = PASS; **0 FLAG restante**. Inclui as 4 disposicoes benignas e a correcao de contagem (HYG1-F01) do v1.2. v1.0/v1.1/v1.2 preservadas (INV-07). |
| Tipo | Living Document de Governanca de Principios |
| Autor | Especificador Principal do SOT |
| Autoridade normativa | PAP-001 v1.1 (BASELINE) ss5 (schema); GPR-001 v1.0 (44 principios); atomic-spec v1.3; DHR-PAP-001-B (K-PAP-001 e K-PAP-005) |
| Data | 2026-09-15 |
| Fluxo | Especificador (autor) -> Revisor -> Andraus (homologa) |

> **Status epistemologico global (TRACE-06):** este inventario e BASELINE HOMOLOGADO a partir de 2026-09-15 (DHR-CIC-001). E um living document: novas linhas (specs futuras) entram por milestone + evento (K-PAP-002). As celulas `[INFERENCIA]` remanescentes (FLAGs) sao itens de atencao para o proximo ciclo de Hygiene, nao FATO.

---

## 1. Proposito e referencia normativa

O CIC-001 e o **Inventario de Conformidade de Principios** do SOT, instituido como documento separado (K-PAP-001, DHR-PAP-001-B) com ciclo de versao proprio, mantendo o GPR-001 estavel (PC-07). `[FATO NORMATIVO]`

Este inventario:
1. Mapeia cada documento M0 contra as **6 classes de principio** do GPR-001 ss2 (PC-01..08, PB-01..10, PE-01..08, PCO-01..07, PO-01..07, PS-01..04). `[FONTE: GPR-001 ss2]`
2. Registra **GAPs** como open decisions (INV-GAP-nnn), sem reescrita automatica (PAP-001 ss1.2). `[FONTE: PAP-001 ss5.3]`
3. Inclui **mapeamento seletivo** das open decisions existentes -> apenas as que tocam um principio (K-PAP-005). `[FATO NORMATIVO: DHR-PAP-001-B ss3]`

---

## 2. Schema de status (PAP-001 ss5.2)

| Status | Definicao operacional |
|---|---|
| **PASS** | O documento atende os principios da classe aplicaveis ao seu escopo; nenhuma tensao aberta. |
| **FLAG** | Tensao identificada; nao invalida o documento, mas registra item de atencao para o proximo ciclo de Hygiene. |
| **GAP** | Principio aplicavel da classe nao coberto; gera open decision INV-GAP-nnn. |
| **N/A** | A classe nao incide sobre o escopo do documento. Justificativa registrada. |

`[FONTE: PAP-001 ss5.2]`

---

## 3. Matriz de Conformidade M0

Documentos M0 auditados: `atomic-spec.md` v1.3, `RETOMADA/GEH-001...` v1.1, `ROADMAP.md`, `governance/CONSTITUTION.md`, `governance/RULES.md`, `governance/CONFLICT-MAP.md`.

**RULES.md e CONFLICT-MAP.md foram auditados integralmente** (fecha achado M-01 do Revisor; nao mais `[INFERENCIA]` de cabecalho).

| Documento M0 | PC | PB | PE | PCO | PO | PS | Base da avaliacao |
|---|---|---|---|---|---|---|---|
| **atomic-spec v1.3** | PASS | PASS | PASS | N/A | PASS | N/A | Ver ss3.1; PCO→N/A (Hygiene #1) |
| **GEH-001 v1.1** | PASS | PASS | PASS | PASS | PASS | N/A | Ver ss3.2; PCO→PASS (Hygiene #1) |
| **ROADMAP.md** | PASS | PASS | N/A | N/A | PASS | N/A | Ver ss3.3; PE→N/A (Hygiene #1) |
| **CONSTITUTION v1.1** | PASS | PASS | PASS | PASS | PASS | N/A | Ver ss3.4; PS→N/A (Hygiene #1) |
| **RULES.md** | PASS | PASS | PASS | PASS | PASS | N/A | Ver ss3.5 |
| **CONFLICT-MAP.md** | PASS | PASS | PASS | PASS | N/A | PASS | Ver ss3.6; inversoes §3.6 mapeadas (emenda homologada 2026-09-20) |

**Resumo (v1.3, Hygiene #1 FECHADO):** 36 celulas = **27 PASS, 0 FLAG, 0 GAP, 9 N/A**. Todos os FLAGs do M0 dispostos: 4 benignos (→ N/A/PASS) + 2 CONFLICT-MAP (→ PASS via emenda de inversoes contextuais homologada 2026-09-20).
> **Correcao HYG1-F01:** o resumo do v1.0 dizia "28 PASS / 5 FLAG / 3 N/A" — contagem incorreta. As 36 celulas do v1.0 somavam de fato **24 PASS / 6 FLAG / 6 N/A** (erro aritmetico, sem impacto em disposicao de celula; ata DHR-CIC-001 preservada como historico — INV-07). O valor acima ja reflete as disposicoes do Hygiene #1 sobre a contagem corrigida.

---

### 3.1 atomic-spec v1.3 --- Auditoria detalhada

| Classe | Status | Ancora |
|---|---|---|
| **PC** | PASS | ss13 INV-01..10 codificam PC-01..08 (hierarquia, idioma canonico, versionamento, baseline informal). `[FONTE: atomic-spec.md:254-271]` |
| **PB** | PASS | ss11 TRACE-06 -> PB-05 (rastreabilidade); ss10 Enforcement -> PB-08 (proporcionalidade); ss6 BASpec PORQUE -> PB-06 (explicabilidade). `[FONTE: atomic-spec.md:206-228, :89-94]` |
| **PE** | PASS | ss9 Skills x Engines -> PE-04; ss10 E0-E3 -> PE-07 (modularidade por contrato). `[FONTE: atomic-spec.md:133-138, :142-203]` |
| **PCO** | FLAG | Metodo nao formaliza contraevidencia (PCO-02) como gate de spec; contraevidencia e criterio cognitivo aplicado aos componentes, nao ao metodo de especificacao. `[INFERENCIA]` |
| **PO** | PASS | ss10.1 ENF-01..08 -> PO-02, PO-03, PO-04; ss10.3 fail-closed -> PO-02. `[FONTE: atomic-spec.md:191-202]` |
| **PS** | N/A | Documento de metodo; situacionais (urgencia/cautela) nao incidem. `[INFERENCIA]` |

---

### 3.2 GEH-001 v1.1 --- Auditoria detalhada

| Classe | Status | Ancora |
|---|---|---|
| **PC** | PASS | ss6.4 autoridade centralizada -> PC-08 (sem baseline informal); ss6 centralizar/descentralizar respeita hierarquia de decisao. `[FONTE: GEH-001:239-244]` |
| **PB** | PASS | ss3 4Es com hierarquia fixa -> PB-01>PB-02>PB-03>PB-04; ss3.2 "nenhuma otimizacao de custo sobe o degrau". `[FONTE: GEH-001:86-124]` |
| **PE** | PASS | ss6 centralizar vs descentralizar -> PE-02 (sintese centralizada), PE-03 (analise descentralizada); ss7 protocolo de decomposicao. `[FONTE: GEH-001:215-299]` |
| **PCO** | FLAG | Cobre cognicao via ETCLOVG (ss5) mas nao nomeia PCO-01..07 explicitamente; cobertura e funcional, nao nominal. `[INFERENCIA]` |
| **PO** | PASS | ss4 latencia como restricao de primeira classe -> PO-06; ss4.3 ativacao preguicosa -> PO-01 (economia cognitiva). `[FONTE: GEH-001:138-173]` |
| **PS** | N/A | Guia generalista; nao define contextos situacionais especificos do SOT. `[INFERENCIA]` |

---

### 3.3 ROADMAP.md --- Auditoria detalhada

| Classe | Status | Ancora |
|---|---|---|
| **PC** | PASS | Caminho critico respeita hierarquia (SPEC-001 Hypothesis antes de SPEC-012 Institutional); nenhuma Spec redefine modelo canonico baselined. `[FONTE: ROADMAP.md:84-199]` |
| **PB** | PASS | ss24 "Eficacia -> Efetividade -> Eficiencia -> Economicidade" explicito; ss23 gate entre specs -> PB-05 (rastreabilidade). `[FONTE: ROADMAP.md:359-366]` |
| **PE** | FLAG | Sequencia de Specs nao declara fronteira de contexto por componente (PE-07 modularidade). Cada Spec devera declarar sua fronteira em tempo de especificacao. `[INFERENCIA]` |
| **PCO** | N/A | Roadmap e sequencia de trabalho; nao governa cognicao de agentes. `[INFERENCIA]` |
| **PO** | PASS | ss23 gate por spec materializa PO-04 (escalonamento por criticidade). `[FONTE: ROADMAP.md:340-354]` |
| **PS** | N/A | Roadmap nao define contextos situacionais. `[INFERENCIA]` |

---

### 3.4 CONSTITUTION v1.1 --- Auditoria detalhada

| Classe | Status | Ancora |
|---|---|---|
| **PC** | PASS | Hierarquia metodologica inviolavel -> PC-01; "SOT nao executa ordem" -> PC-02; P02 Conviccao multidimensional -> PC-04 (piso referenciado); P07 -> PC-07. `[FONTE: CONSTITUTION.md:16-27, :33-78]` |
| **PB** | PASS | Framework 4Es ss -> PB-01..04; P01 Explicabilidade -> PB-06; P13 Auditabilidade -> PB-07; P03 Hipoteses multiplas -> PB-10. `[FONTE: CONSTITUTION.md:159-175]` |
| **PE** | PASS | P06 Separacao de responsabilidades -> PE-01; Blackboard 8 workspaces -> PE-05; Nenhum agente faz funcao de outro. `[FONTE: CONSTITUTION.md:119-129, :178-200]` |
| **PCO** | PASS | P03 Hipoteses multiplas -> PCO-01; P04 Refutacao antes de confirmacao -> PCO-02; P11 Evidencias independentes -> PCO-03. `[FONTE: CONSTITUTION.md:41-71]` |
| **PO** | PASS | P12 Governanca da evolucao -> PO-05 (policies nao auto-aprendidas); Framework 4Es nao inverte hierarquia. `[FONTE: CONSTITUTION.md:72-74]` |
| **PS** | FLAG | PS-01 (urgencia), PS-02 (cautela), PS-03 (exploracao) nao normatizados na Constituicao; contextos situacionais deferidos as Specs operacionais. `[INFERENCIA]` |

---

### 3.5 RULES.md --- Auditoria INTEGRAL (fecha M-01)

| Classe | Status | Ancora |
|---|---|---|
| **PC** | PASS | RULE-001: Elliott primeiro -> PC-01 `:10`; RULE-002: ICT sem hipotese -> PC-01 `:13`; RULE-008: camada inferior nao invalida superior -> PC-01 `:31`; RULE-003 + RULE-CEE-004: conviccao >=70% -> PC-04 `:15-16, :250-256`; RULE-BB-003: CHM-001 estados -> PC-07 `:299-304`; RULE-BB-004: append-only -> PC-07 `:306-308`. `[FONTE: RULES.md linhas citadas]` |
| **PB** | PASS | RULE-010: rastreabilidade de conviccao -> PB-05 `:38-39`; RULE-009: hipotese+evidencias+contraevidencias obrigatorios -> PB-05, PB-06, PB-07 `:34-36`; RULE-004: evidencias correlacionadas -> PB-10 `:18-19`; RULE-007: 2 hipoteses -> PB-10 `:27-28`; RULE-CEE-001: hierarquia 4Es -> PB-01..04 `:232-235`; RULE-PPQ-001: rigor proporcional -> PB-08 `:333-340`. `[FONTE: RULES.md linhas citadas]` |
| **PE** | PASS | RULE-BB-001: comunicacao via Blackboard -> PE-05 `:290-292`; RULE-BB-002: workspaces -> PE-05 `:294-296`; RULE-EW-009: Elliott nao faz analise institucional -> PE-01 `:83-85`; RULE-FB-001: Fibonacci nao cria contagens -> PE-01 `:95-96`; RULE-CEE-002: roteamento por tipo cognitivo -> PE-04 `:237-241`; RULE-GMC-001..005: modelos canonicos -> PE-07 `:266-284`. `[FONTE: RULES.md linhas citadas]` |
| **PCO** | PASS | RULE-007 + RULE-EW-001: 2 hipoteses concorrentes -> PCO-01 `:27-28, :49-51`; RULE-009: contraevidencias exigidas -> PCO-02 `:34-36`; RULE-004: evidencias correlacionadas = uma -> PCO-03 `:18-19`. `[FONTE: RULES.md linhas citadas]` |
| **PO** | PASS | RULE-CEE-001: 4Es -> PO-04 `:232-235`; RULE-ICT-006: bloqueio em condicoes -> PO-02 `:165-169`; RULE-PPQ-001: rigor GES -> PO-04 `:333-340`. PO-03 (gate deterministico) e PO-05 (policies nao auto-aprendidas) estao no atomic-spec ENF-03/ENF-05, nao duplicados no RULES. `[FONTE: RULES.md + atomic-spec.md]` |
| **PS** | N/A | RULES.md contem regras fixas; situacionais (urgencia/cautela/exploracao) nao incidem sobre regras invariantes. `[INFERENCIA]` |

---

### 3.6 CONFLICT-MAP.md --- Auditoria INTEGRAL (fecha M-01)

| Classe | Status | Ancora |
|---|---|---|
| **PC** | PASS | Todas as resolucoes respeitam Elliott veto (PC-01): "Output = NEUTRO" em conflito Elliott x SMC `:9-16`; limiares de conviccao referenciados (PC-04) `:44-50`. `[FONTE: CONFLICT-MAP.md linhas citadas]` |
| **PB** | PASS | Conflitos registrados, nao suprimidos -> PB-09 (coerencia) `:9-16`; ambiguidade -> AGUARDAR_SETUP -> PB-10 (preservacao da incerteza) `:50`. `[FONTE: CONFLICT-MAP.md linhas citadas]` |
| **PE** | PASS | Fibonacci informa, Elliott decide -> PE-01 (especializacao) `:13`; resolucoes respeitam fronteiras de agente. `[FONTE: CONFLICT-MAP.md]` |
| **PCO** | PASS | Inversoes contextuais (GPR-001 §3.6) agora mapeadas no CONFLICT-MAP (secao "Inversoes contextuais", emenda homologada 2026-09-20); PCO-01/PCO-02 cobertos. |
| **PO** | N/A | CONFLICT-MAP governa resolucao de conflitos analiticos, nao operacao runtime. `[INFERENCIA]` |
| **PS** | PASS | Inversao "regime desconhecido" (PS-03/PS-02) mapeada no CONFLICT-MAP (emenda homologada 2026-09-20). |

---

## 3-bis. Registro VPD --- Vinculo em Tempo de Decisao (PAP-001 Bloco 7)
`[FONTE: PAP-001 v1.2 Bloco 7; DHR-PAP-001-C]`

Coluna de conformidade decision-time para specs que produzem Decisao/Conviccao/Sintese/ponderacao de agente. Status: `PRESENTE` / `AUSENTE` / `N/A`. Especificacoes de 1a geracao entram como `VPD-AUSENTE (gap conhecido)` sob regime R1 (sem reescrita forcada); o VPD torna-se gate quando forem redigidas sob o roadmap (rastreado em RMR-001 BL-001).

| Spec de decisao | VPD | Observacao |
|---|---|---|
| `specs/features/SPEC-001/plan.md` (Hypothesis Harness) | **AUSENTE** | 0 refs a GPR-001 (prova 2026-09-16). Auditoria de classes PC/PB/PE/PCO/PO/PS pendente do 1o ciclo de Hygiene `[INFERENCIA]`. Gatilho de correcao: emenda ou substituicao. |
| `specs/synthesis.spec.md` (arbitro) | **AUSENTE** | 1a geracao; sera substituido por SPEC-014. VPD vira gate na redacao do SPEC-014. |
| `specs/elliott-wave.spec.md` | **AUSENTE** | 1a geracao; VPD gate na redacao do SPEC-010. |
| `specs/fibonacci.spec.md` | **AUSENTE** | 1a geracao; VPD gate na redacao do SPEC-011. |
| `specs/smc.spec.md` | **AUSENTE** | 1a geracao; VPD gate na redacao do SPEC-012. |
| `specs/ict.spec.md` | **AUSENTE** | 1a geracao; VPD gate na redacao do SPEC-013. |

**Encaminhamento:** rastreado como **BL-001** no RMR-001 (`spec:SPEC-010..014 em redacao` ∨ `evento:emenda dos *.spec.md`). Nao forca reescrita agora (R1); ao ativar, o Revisor exige VPD-1..5 (PAP-001 Bloco 7).

---

## 4. Registro de GAPs

**Nenhum GAP identificado na auditoria M0.**

Todos os 6 documentos apresentam cobertura PASS ou FLAG (tensao menor) ou N/A (classe nao aplicavel). Nenhum principio aplicavel ficou sem cobertura a ponto de exigir open decision INV-GAP-nnn.

Os FLAGs registrados sao itens de atencao para ciclos futuros de Hygiene, nao gaps bloqueantes:
- atomic-spec.md PCO: contraevidencia nao e gate de spec (comportamento esperado para documento de metodo)
- GEH-001 PCO: cobertura funcional, nao nominal
- ROADMAP.md PE: fronteiras de contexto a declarar por Spec
- CONSTITUTION PS: situacionais deferidos as Specs
- CONFLICT-MAP PCO/PS: inversoes contextuais a mapear

**Harness Debt — piloto EUA-E15 / BL-008 (Mapa de Auditoria da SPEC-001, homologado 2026-09-28):** 3 achados leves, nenhum bloqueante, encaminhados aqui pelo Revisor/Andraus na homologação do `governance/MAPA-AUDITORIA-SPEC-001.md`:
- **D-HD-1** (EUA-E04/RULE-HD): SPEC-001 sem bloco §8.3 Herança/Delta nomeado; refs a CHM-001/CEM-001 sem pin de versão. Substância presente, sem contradição vertical. Ação: ao tocar a SPEC-001 (emenda futura), inserir §8.3 com INHERITS/ADDED por ID+versão.
- **D-SES-1** (SES-001 §59/§60, BL-008 original): os 17 campos + cadeia incidem sobre a 1ª Engineering Card da SPEC-001, não sobre a Spec. Complementa VPD-AUSENTE (§3-bis:146). Ação: a 1ª Engineering Card derivada da SPEC-001 carrega §59/§60.
- **D-ECC-1** (EUA-E21/RULE-ECC-01): refs baselined da SPEC-001 a slots SPEC-002..005 podem apontar para identificador alterado na abertura. Ação: sanada por emenda aditiva já homologada (RULE-ECC-01/RULES.md; atomic-spec §15, 2026-09-28) — na abertura de cada slot referenciado, o Dossiê lista as refs e propõe erratum aditivo. **BAIXADO (2026-10-05, DHR-AUDIT-SPEC001-001):** sanado para a SPEC-001 pelo ERRATUM-SPEC001-002 (item 6, âncoras por capability/contrato) — SPEC-001 v1.2; registro histórico preservado.

**Harness Debt — BL-009 (Mapa de Auditoria do SAS-001, homologado 2026-09-28, DHR-BL009-001):**
- **D-SAS-1** (SES-001 §59 campo 13/§60, mesma razão de D-SES-1): SAS-001 sem campo "Generalização" nomeado (substância presente — reprodutibilidade/independência, SAS-001:762,766) e sem elos DESIGN PATTERN/ENGINEERING CARD nomeados na cadeia §60. §59/§60 incidem sobre a Engineering Card, não sobre a spec de agente; SAS-001 é anterior à EUA-E03/SES-001. Ação: a 1ª Engineering Card derivada do SAS-001 carrega §59/§60.

---

## 5. Mapa seletivo Open Decision <-> Principio (K-PAP-005)

Conforme K-PAP-005 (DHR-PAP-001-B ss3), apenas as open decisions que tocam um principio sao mapeadas. Decisoes sem vinculo principiologico nao sao mapeadas (economia --- 4Es).

### 5.1 Open decisions MAPEADAS

| Open Decision | Questao | Principios tocados | Ancora GPR-001 | Ancora fonte |
|---|---|---|---|---|
| **J-001** | Formula/pesos/limiares definitivos do Conviction Vector | PC-04 (piso de conviccao), PCO-06 (nao-reducao) | GPR-001 ss2.1 PC-04, ss2.4 PCO-06 | atomic-spec.md ss12 |
| **G-001** | Schema de estado persistente por agente | PE-07 (modularidade), PB-07 (auditabilidade) | GPR-001 ss2.3 PE-07, ss2.2 PB-07 | atomic-spec.md ss12 |
| **H-001** | Knowledge Graph: grafo real ou estrutura em memoria? | PE-05 (Blackboard vs KG), PB-05 (rastreabilidade) | GPR-001 ss2.3 PE-05, ss2.2 PB-05 | atomic-spec.md ss12 |
| **K-001** | Ciclo P12 detalhado (evolucao do conhecimento) | PO-05 (policies nao auto-aprendidas), PB-05 (rastreabilidade) | GPR-001 ss2.5 PO-05, ss2.2 PB-05 | atomic-spec.md ss12 |
| **M-001** | Estados do Blackboard para objetos NAO-hipotese | PE-05 (Blackboard como memoria de trabalho) | GPR-001 ss2.3 PE-05 | atomic-spec.md ss12 |
| **N-001** | Pesos por ativo do Conviction Vector | PC-04, PCO-06 (mesmo vinculo de J-001) | GPR-001 ss2.1 PC-04, ss2.4 PCO-06 | atomic-spec.md ss12 |

### 5.2 Open decisions NAO MAPEADAS (sem vinculo principiologico)

| Open Decision | Questao | Justificativa |
|---|---|---|
| **C-001** | Granularidade EARS multi-condicao | Decisao de formato de especificacao (notacao); nao toca principio do GPR-001. `[INFERENCIA]` |

### 5.3 Open decisions FECHADAS (registro historico)

| Open Decision | Questao | Resolucao | Data |
|---|---|---|---|
| **B-001** | Conviction Engine separado do Synthesis? | FECHADA (Q-007): Conviction Engine e SEPARADO. Topologia Fusion -> Conviction -> Synthesis. | 2026-09-14 |
| **L-001** | Governanca do proprio harness / policy versionada | FECHADA (DHR-SPEC019-001): homologacao da SPEC-019 fecha L-001 na dimensao spec-time. Governanca de runtime NAO e residuo de L-001 -- pertence a SPEC-018/K-001 (K-001 segue aberta em ss5.1). | 2026-09-22 |
| **RMR-EST-001** | Estado `Diferido` do BL-013 fora do enum de 5 valores do RMR-001 ss2 | FECHADA (DHR-DOCSYNC-002): nao era estado formal novo, era a palavra de encaminhamento do gate (Passo 11-bis); Estado do BL-013 corrigido para `Em espera` (definicao do ss2 ja descrevia a situacao). | 2026-09-28 |
| **I-001** | Skills como unidades formais separadas? | FECHADA (Andraus, 2026-09-28, DHR-I001-001): Skills = hibrido por Classe (Opcao C) -- Classe D formaliza como Skill separada, Classe P permanece comportamento interno do agente; CC-01 intocada; criterio de corte exato diferido ao Dossie de abertura da SPEC-025. | 2026-09-28 |
| **RULE-REG-001** | 10+1 familias RULE (RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET, EUA-E04-E14) ja FATO NORMATIVO, incorporacao ao RULES.md diferida ao piloto SPEC-002 | FECHADA (Andraus, 2026-09-28, DHR-REG-001): registro fisico concluido (transcricao literal RCN-001); consolida atomic-spec v1.5. | 2026-09-28 |

`[FONTE: atomic-spec.md ss12; roadmap.md "Estado atual do ciclo"]`

---

## 6. Instrucoes de manutencao do living document

### 6.1 Quem preenche

- **Especificador:** ao entregar spec nova, preenche a linha correspondente da Matriz.
- **Revisor:** durante revisao de spec, verifica/ajusta celulas e registra FLAGs/GAPs.
- **Andraus:** homologa atualizacoes; resolve GAPs que exigem decisao de governanca.

`[FONTE: PAP-001 ss5.3]`

### 6.2 Quando atualiza

Conforme K-PAP-002 (DHR-PAP-001-B ss3):
- **Por milestone homologada** (ex.: ao homologar SPEC-001, adicionar linha SPEC-001 a Matriz).
- **Por gatilho de evento:**
  - Nova spec homologada
  - Open decision J-xxx resolvida que afete um principio
  - Proposta de principio novo (Bloco 5 do PAP-001)
  - Ciclo de Hygiene extraordinario

`[FATO NORMATIVO: DHR-PAP-001-B ss3 K-PAP-002]`

### 6.3 Como registrar GAP

Todo GAP cria uma linha de open decision `INV-GAP-nnn` com:
- Documento
- Classe
- Principio nao coberto
- Descricao do gap
- Encaminhamento: auditoria / emenda futura por decisao de Andraus

GAP **nao** dispara reescrita automatica (PAP-001 ss1.2). `[FATO NORMATIVO: PAP-001 ss5.3]`

---

## 7. Classificacao das fontes

| Fonte | Classificacao |
|---|---|
| PAP-001 v1.1 (BASELINE) | `[FATO NORMATIVO]` |
| GPR-001 v1.0 | `[FATO ARQUITETURAL]` --- proposta aguardando homologacao |
| DHR-PAP-001-B | `[FATO NORMATIVO]` |
| atomic-spec v1.3 | `[FATO NORMATIVO]` |
| RULES.md, CONFLICT-MAP.md, CONSTITUTION.md | `[FATO NORMATIVO]` |
| GEH-001 v1.1, ROADMAP.md | `[FATO NORMATIVO]` |

---

## 8. Resumo quantitativo

| Metrica | Valor |
|---|---|
| Documentos M0 auditados | 6 |
| Total de celulas | 36 |
| PASS | 28 (77.8%) |
| FLAG | 5 (13.9%) |
| GAP | 0 (0%) |
| N/A | 3 (8.3%) |
| Open decisions mapeadas | 8 |
| Open decisions nao mapeadas | 1 (C-001) |
| Open decisions fechadas | 1 (B-001) |

**Atualização posterior (2026-09-22, DHR-SPEC019-001):** L-001 fechada (governança do próprio harness, dimensão spec-time) — sai de "Open decisions mapeadas" (7 remanescentes em §5.1) e entra em "Open decisions fechadas" (2: B-001, L-001, §5.3). Tabela acima preservada como registro histórico na data de autoria do CIC-001 (INV-07).

**Atualização posterior (2026-09-28, achado do Revisor):** +1 "Open decisions não mapeada" em §5.2 — RULE-REG-001 (total: 2, com C-001). +1 "Open decisions fechada" em §5.3 — RMR-EST-001, corrigida no mesmo dia (total: 3, com B-001/L-001). Ver `ROADMAP.md` "Decisões abertas ativas".

---

## 9. Declaracao

**Autopre-check satisfeito:**
- [x] roadmap.md lido: posicao do CIC-001 confirmada (artefato subsequente ao PAP-001).
- [x] atomic-spec.md lido: metodo vigente confirmado.
- [x] PAP-001 ss5 lido: schema do Inventario seguido.
- [x] RULES.md e CONFLICT-MAP.md auditados integralmente (fecha M-01).
- [x] Nenhum GAP aberto; 5 FLAGs registrados como itens de atencao.
- [x] Mapeamento seletivo K-PAP-005: 8 decisoes mapeadas, 1 nao mapeada, 1 fechada. *(Na data de autoria — INV-07. Atualização posterior: 7 mapeadas, 1 não mapeada, 2 fechadas — ver §8.)*
- [x] Etiquetagem TRACE-06 aplicada.
- [x] Nenhuma decisao aberta usada como invariante fechado (CONS-01).
- [x] 4Es na hierarquia correta.

**Pronto para revisao.**

---

*CIC-001 v1.0 --- **HOMOLOGADO --- BASELINE** (Andraus, 2026-09-15, DHR-CIC-001). Produzido pelo Especificador; auditado pelo Revisor (CONFORME); schema conforme PAP-001 ss5. Auditoria integral de RULES.md e CONFLICT-MAP.md fechou o achado M-01. Living document: proxima atualizacao por milestone + evento (K-PAP-002).*
