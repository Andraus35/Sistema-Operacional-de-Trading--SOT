# roadmap.md — SOT: Road Map Sequencial de Especificação do Harness Cognitivo

**Versão:** baseline homologado (2026-09-12) + atualização de arranque SPEC-001 (2026-09-14)  
**Status:** HOMOLOGADO — Andraus  
**Edição operacional:** Claude Code (Opus 4.8, esforço alto, skill `tlc-spec-lean`)  
**Método vigente:** `atomic-spec.md` (raiz do repositório)  
**Painel vivo:** RMR-001  
**Emenda vigente:** **EUA-E17** (DHR-EUA-E17, 2026-09-21) — interpõe a **FASE GOV** (SPEC-019 integral + SPEC-020 núcleo A + SPEC-021) entre SPEC-001 e SPEC-002; renumera Fases 10–17→8–15 (números de Specs inalterados). Ordem autoritativa: `governance/EUA-E17_…_PROPOSTA.md` §3.2. Renumeração editorial cabeçalho-a-cabeçalho = passo diferido.
**Emenda vigente adicional:** **EUA-E21** (DHR-EUA-E21, 2026-09-26) — **Especificação Emergente:** este ROADMAP fixa **direção e restrições**; a lista de Specs (SPEC-002…045), seus números, a quantidade e as fronteiras são **indicativos** e só se definem **na abertura de cada Spec**, após Dossiê de Pesquisa (estado da arte e melhores práticas na web) pelo Especificador — RULE-ECC-01/02. SPEC-001 e SPEC-019 (homologadas) inalteradas.  
**Emendas vigentes adicionais (2026-10-01):** **EUA-E23** (DHR-EUA-E23) — **Manager Agent Unificado:** SPEC-008/015/014 são as 3 Specs do Manager sob um "Manager Contract" (ator único, RULE-HV); slots renomeados, **não renumerados** (INV-07), permanecem indicativos. **EUA-E20** (DHR-EUA-E20) — **FASE RISK** (§10-bis): família RISK-SPEC = 6 macro-slots indicativos RISK-M1..M6, após a FASE 6, não-autorizada até `milestone:FASE 6 concluída`. Nenhuma decisão aberta fechada por estes atos (CONS-01).  

> **Como usar.** Leia este arquivo **antes de iniciar qualquer Spec**. Ele define qual Spec está autorizada, sua posição no caminho crítico e as decisões abertas que a impactam. Nenhuma Spec inicia sem consultar este arquivo.

> **Vigência EUA-E21 (DHR-EUA-E21, 2026-09-26) — leia antes das seções de FASE/SPEC abaixo.** Todas as seções `### SPEC-…` de SPEC-002 a SPEC-045 descrevem **slots indicativos** (tema + posição provável + dependências), **não** Specs obrigatórias. Número, quantidade, fronteira e decomposição de cada Spec são definidos **na sua abertura** (passo 1-bis do §23) por proposta do Especificador, após **Dossiê de Pesquisa** (estado da arte e melhores práticas na web — RULE-ECC-02) e **homologação de Andraus**. Um slot pode ser mantido, dividido, fundido, substituído ou descartado (**nunca apagado** — INV-07); gatilhos do RMR-001 acompanham por **re-apontamento homologado**. **Dependências, invariantes, decisões abertas e o §22 continuam vinculantes.** SPEC-001 e SPEC-019 (HOMOLOGADAS) permanecem baseline, sem reabertura.

> **Operação no Claude Code:** o fluxo do §23 (gate por Spec) mapeia para a skill `tlc-spec-lean` (PLAN → CHECKS → [BUILD → VERIFY]). Use PLAN como Spec e CHECKS como verificação de spec na fase spec-first; adie BUILD/VERIFY-de-código. O verificador interno da skill é feedback — não é o Revisor nem homologação. Sequência: Especificador → Revisor (GRE-001/HRE-001) → Andraus homologa → `.md` → próxima Spec.

---

## Estado atual do ciclo

| Item | Status |
|---|---|
| M0 — Unidade Atômica | **HOMOLOGADO** (v1.2; EUA-E01 + EUA-E02) |
| Baseline F.1 + Questionário v1 | **HOMOLOGADO** — Andraus, 2026-09-15 (parecer Revisor CONFORME; harness L4/94%). Ver `docs/arranque/ata-homologacao-F1.md`. |
| SPEC-001 — Hypothesis Harness | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-15). Ver `specs/features/SPEC-001/plan.md`. |
| SPEC-019 — Harness Governance & Evolution | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-22, DHR-SPEC019-001; compat. Minor). RULE-HG-01..08 + RULE-HV-01..04 → RULES.md. Fecha L-001. Ver `specs/features/SPEC-019/plan.md`. |
| SPEC-020 — Harness Evaluation Specification (núcleo A) | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-27, DHR-SPEC020-001; compat. Minor). 9 lentes constitutivas (EV-001..009, incl. 9ª lente `principle consistency` — efetiva `SPEC-020-PRINC-001`); 4 Enforcement Contracts; RULE-EV-01..07 → vigência imediata (registro formal em RULES.md diferido). 1ª aplicação do Dossiê de Pesquisa (EUA-E21) e do §7-bis/Passo 5-bis (EUA-E18). 2 achados não-bloqueantes registrados para emenda futura (DHR-SPEC020-001 §3). Ver `specs/features/SPEC-020/plan.md`. |
| SPEC-021 — Harness Score / Maturity Model | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-28, DHR-SPEC021-001; compat. Minor). Escada canônica por-Spec `L0→L4` (rótulo L3 harmonizado com Quality Gates); gate normativo E3 (RULE-MM-05); staged; anti-gaming (RULE-MM-02); RULE-MM-01..07 → vigência imediata. 3ª spec sob §7-bis/Passo 5-bis — checagem de proporcionalidade EUA-E18 Q7 concluída: **PROPORCIONAL**. **Fecha a FASE GOV** (019+020+021). Ver `specs/features/SPEC-021/plan.md`. |
| SPEC-002 — Evidence & Evidence Provenance Harness | **HOMOLOGADA — BASELINE** (Andraus, 2026-09-28, DHR-SPEC002-001; compat. Minor). Camada Harness/operacional sobre CEM-001 (não redefinido); 10 BASpecs (EH-001..010) com Classe D/C/H/P (CC-11, 1ª aplicação); 5 Enforcement Contracts; RULE-EH-001..008 → vigência imediata (registro físico em RULES.md diferido). 1ª Spec sob atomic-spec v1.5. Ver `specs/features/SPEC-002/plan.md`. |
| SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine | **HOMOLOGADA — BASELINE** (Andraus, 2026-10-02, DHR-SPEC003-001; compat. Minor; parecer Revisor CONFORME COM RESSALVAS — notas de honestidade text-only incorporadas na v1.5). Redige o **CCM-001** (agora BASELINED). Fecha **estrutura/método/mecanismo** do Conviction Vector 8D + Fusion/Conviction Engine + **limiares-piloto interinos**; **J-001/N-001 permanecem ABERTAS** (valores definitivos pós-backtest). 13 BASpecs (CF-001..013, Classe C/D/P/H); RULE-CF-001..012 → vigência imediata (registro físico em RULES.md diferido). Q-A9 ratificada (regime → dimensão `temporal`). Ver `specs/features/SPEC-003/plan.md`. |
| Próximo trabalho autorizado | **SPEC-004** — Cognitive Blackboard Protocol (caminho crítico; FASE 2). *(SPEC-003 homologada — DHR-SPEC003-001.)* **Linha paralela autorizada por Andraus (chat, 2026-10-02):** abertura da **SPEC-038** (Trading Analysis Tool Harness) com **viabilidade como critério** — avaliação da conexão TradingView↔SOT (BL-031). Abertura de qualquer Spec segue o passo 1-bis do §23 (Dossiê de Pesquisa, RULE-ECC-01/02). |
| Bloqueador principal (resolvido quanto à estrutura) | **J-001** (fórmula/pesos/limiares **definitivos** do Conviction Vector) permanece ABERTA — agora é matéria de **backtest/calibração pós-homologação** (dona a definir — BL-032), não mais trava da homologação da SPEC-003 (estrutura/método + limiares-piloto já fechados). |
| Decisões abertas ativas | J-001 (reduzido), G-001, H-001, K-001, C-001, M-001, N-001 · **SPEC-045-RUNTIME-001** (caminho de leitura em runtime → baseline na SPEC-045; ver §20) · **ECC-03-001** (escopo da RULE-ECC-03 / "modelo de especialização" — a sigla ECC não é expandida no repositório; RULE-ECC-03 RESERVADA; DHR-EUA-E21 Q6) · **WORKFLOW-SOT-001** (**residual** — DHR-WF-002, 2026-10-01: Killzone [WF-D01], alarme-gatilho [WF-D02] e papel do ICT [WF-D04] **FECHADOS por Andraus** em `WORKFLOW.md`; permanece **aberto** só **WF-D03**: relação convicção-macro/convicção-global com Conviction Vector 8D — direção declarada [um vetor, duas leituras] e nº de invocações **já fixado em 2x** por Andraus [WF-C01, Q-A5 — DHR-DEC-001, 2026-10-01]; a dimensão do regime [WF-C04/Q-A9] foi **decidida pela SPEC-003** — dimensão `temporal` [v1.4; **RATIFICADA na homologação da SPEC-003 — DHR-SPEC003-001, 2026-10-02**]; resíduo aberto = fórmula/pesos/limiares = J-001/N-001; origem DHR-ECC05-001, 2026-09-29) |
| Decisões FECHADAS | **ECC-VAL-001 — FECHADA (Andraus, 2026-10-03, DHR-DEC-003): validade do Dossiê por complexidade — LOW 180 / MEDIUM 120 / HIGH-CRITICAL 90 dias, ou antes se o contexto mudar** · **SPEC-038-TVMCP-001 — DECIDIDA (Andraus, 2026-10-03, DHR-DEC-003): canal CDP como perfil exploratório supervisionado; risco de Termos de Uso assumido por Andraus; SPEC-038-DATASRC-001 permanece ABERTA (aguardar TradingView)** · B-001 (Conviction≠Synthesis) — **SUPERSEDIDA na parte "componente/agente separado" por ADR-MANAGER-001 (DHR-ARQ-001, 2026-10-01):** "Conviction Engine" é taxonomia legada → **mecanismo (Classe D/H do CCM-001) invocado pelo Manager Agent — Fase 2 (Conviction)**; preservada a separação **lógica** de etapas (Fusão→cálculo do Conviction Vector→síntese); INV-07 (não apagada) —; dimensionalidade=8; CHM-001/CEM-001 baselined (Questionário v1, 2026-09-14) · **I-001 — FECHADA (Andraus, 2026-09-28, DHR-I001-001): Skills = híbrido por Classe (Opção C) — Classe D formaliza como Skill separada, Classe P permanece comportamento interno do agente; CC-01 intocada; critério de corte exato diferido ao Dossiê de abertura da SPEC-025 (não fechado agora)** · **L-001 — FECHADA (SPEC-019 homologada, 2026-09-22): governança spec-time resolvida; runtime ≠ resíduo de L-001 → SPEC-018/K-001)** · **SPEC-020-PRINC-001 — FECHADA (SPEC-020 homologada, 2026-09-27, DHR-SPEC020-001): consistência principiológica GPR-001 §15 é agora critério constitutivo verificável — 9ª lente `principle consistency` (BASpec-EV-009)** · **CLASSE-MECH-001 — FECHADA (Andraus, 2026-09-27, DHR-CLASSE-MECH-001): taxonomia Classe D/H/P/C, emenda de refinamento a PE-04, declaração por BASpec — RULE-MECH-01..04, CC-11, atomic-spec §10.6; prospectiva, incide a partir de SPEC-002** · **PRINC-BID-001 — FECHADA (Andraus, 2026-09-27, DHR-PRINC-BID-001): herança principiológica bidirecional — declaração de `PD-xx` por Spec de especialidade (§2.7 GPR-001), fundamentação por pesquisa `[EXTERNO]`, ordenada após a Classe (RULE-MECH-01) — RULE-PD-01..03, CC-12, atomic-spec §10.7; prospectiva, incide a partir de SPEC-002** · **RMR-EST-001 — FECHADA (Andraus, 2026-09-28, DHR-DOCSYNC-002): `Diferido` não era estado formal do RMR-001 §2 — era a palavra de encaminhamento do gate (Passo 11-bis); Estado do BL-013 corrigido para `Em espera` (definição do §2 já descrevia essa situação: "validado, gatilho ainda não disparou"), narrativa preservada** · **RULE-REG-001 — FECHADA (Andraus, 2026-09-28, DHR-REG-001): 11 famílias RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET registradas fisicamente em `RULES.md` (transcrição literal das atas EUA-E04..E14, RCN-001); consolida `atomic-spec.md` v1.5** · **Q-A5 — FECHADA (Andraus, chat, 2026-10-01, DHR-DEC-001): o mecanismo de cálculo do Conviction Vector é invocado 2x por ciclo — macro (Fase 1: estrutural+institucional → registra o alarme) e global (Fase 2: +operacional → decide envio); um vetor 8D, duas leituras (WF-C01 v2.1). Invocação é do Manager (SPEC-008/014); SPEC-003 dá o mecanismo. Não fecha a decisão de fórmula/pesos do Conviction Vector (aberta).** · **Q-A9 — FECHADA / RATIFICADA (Andraus, 2026-10-02, DHR-SPEC003-001; delegada à SPEC-003 por DHR-DEC-002): dimensão do regime de mercado (WF-C04) = dimensão `temporal` do Conviction Vector 8D — dimensão de convicção, não gate/veto, sem 9ª dimensão (INV-01/INV-03), dimensionalidade=8 intocada; o peso/limiar do regime permanece em aberto (não fechado por Q-A9).** · **RISK-CONV-001 — FECHADA (Andraus, chat, 2026-10-01, DHR-DEC-001): "convicção de risco" renomeada para "avaliação de risco" = escala própria do Risk Agent; NUNCA soma nem retroalimenta o Conviction Vector 8D (INV-04, WF-X03/WF-X05 v2.1). Detalhe operacional segue em RISK-SPEC-010 (implementa, não reabre).** · **RISK-ARR-LOC-001 — FECHADA (Andraus, chat, 2026-10-01, DHR-DEC-001): D-ARR-001 declarado AUSENTE do repo; a verdade do Risk Agent = EUA-E19a + INV-RISK-* + BL-018 + FASE RISK (EUA-E20). Se o arquivo aparecer, entra por RPIR/HOD-001 — não é fonte hoje.** |

---

## 1. Objetivo

Estabelecer a sequência oficial para transformar o estado arquitetural atual do SOT em especificações de Harness Cognitivo suficientemente precisas para permitir posterior implementação, verificação e avaliação.

O Road Map não substitui as Specs. Cada item representa uma futura unidade de especificação que deverá ser produzida individualmente, verificada, submetida à homologação de Andraus e entregue em Markdown antes do início do item seguinte.

**Fluxo obrigatório por Spec:**
```
Leitura de roadmap.md + atomic-spec.md → Pesquisa Benchmark → Análise RAG →
Especificação → Autopré-check → Revisor → Homologação (Andraus) → Entrega .md → Próxima Spec
```

---

## 2. Regras de execução

### R0 — Leitura obrigatória antes de qualquer escrita
Antes de iniciar qualquer Spec, ler:
- `roadmap.md` — confirmar Spec autorizada, sequência, decisões abertas incidentes.
- `atomic-spec.md` — confirmar método vigente (BASpec, profundidade, Enforcement Contract, etiquetagem).

Se qualquer um dos arquivos estiver ausente: parar e reportar a Andraus.

### R1 — Pesquisa prévia obrigatória
1. Reconsultar a documentação interna pertinente — incluindo modelos canônicos **baselined** (CHM-001, CEM-001). CCM-001/CDM-001/CNM-001 = **pendentes de redação** (não invocar CONST-01 para eles). [Q-001]
2. Identificar o estado atual do componente e cobertura já existente.
3. Identificar lacunas, conflitos e decisões necessárias.
4. Pesquisar estado da arte e benchmarks especializados.
5. Comparar práticas externas com a arquitetura SOT.
6. Preservar o que já estiver suficiente. Aprofundar somente o que estiver insuficiente.
7. Não importar padrões externos automaticamente.

Fontes externas classificadas como: `Padrão / Prática / Benchmark / Evidência / Experimento / Opinião`.

### R2 — Unidade atômica
Unidade padrão: BASpec `QUANDO → ENTÃO → PORQUE → REFERÊNCIA → VERIFICADO POR`.  
Granularidade: 1 condição observável + 1 comportamento mensurável + 1 rastreabilidade + 1 verificação.

### R3 — Profundidade adaptativa
Determinada por risco e complexidade. Ver `atomic-spec.md §2` para a tabela D0–D9 completa.

### R4 — Não duplicar modelos canônicos baselined
Quando um modelo canônico já existe como baseline (**CHM-001, CEM-001** — Q-001), a Spec constrói **sobre** ele — especificando apenas a camada Harness/operacional ainda não coberta. Redefinir um modelo canônico baselined é violação de CONST-01. Os canônicos **pendentes de redação** (CCM-001 = SPEC-003; CDM-001, CNM-001) NÃO acionam CONST-01 — não há canônico a proteger até que sejam redigidos e baselined.

---

## 3. FASE 0 — HOMOLOGAÇÃO METODOLÓGICA

### M0 — Unidade Atômica do Harness Cognitivo
**Status: HOMOLOGADO** (v1.2; Andraus, 2026-09-14)

Método homologado: BASpec; D0–D9; linguagem normativa/comportamental/cognitiva/algorítmica/avaliativa; distinção Skill/Engine/Agent/Harness; ciclo Specify→Design→Tasks→Verify; Quality Gates; Enforcement Contract E0–E3; ENF-01…08.

---

## 4. FASE 1 — NÚCLEO COGNITIVO

*Esta fase vem primeiro porque seus componentes alimentam praticamente todos os demais.*

### SPEC-001 — Hypothesis Harness (sobre CHM-001)
**Prioridade:** P0 — CRITICAL · **Profundidade-alvo:** D0–D8 · **Status:** **HOMOLOGADO — BASELINE** (v1.1, Andraus 2026-09-15) → `specs/features/SPEC-001/`

#### Contexto (observação de arranque — Claude Code, 2026-09-14)
O modelo canônico de hipótese **CHM-001** já existe como baseline no projeto (`DOCUMENTOS INICIAIS/02_Modelos_Canonicos/CHM-001_Baseline_1.0`). O CHM-001 cobre constitucionalmente: identidade, taxonomia, confidence, estado epistêmico, hierarquia, ciclo de vida, versionamento append-only, refutação/substituição/arquivamento e a máquina de estados completa.

Pela mesma lógica que se aplica à SPEC-002/CEM-001 ("não duplicar o modelo canônico; especificar só a camada Harness/operacional"), a SPEC-001 **constrói sobre o CHM-001** — não redefine a hipótese.

#### Escopo da SPEC-001 (camada Harness/operacional sobre CHM-001)
O que a SPEC-001 DEVE cobrir — e que o CHM-001 como modelo canônico não cobre sozinho:

**Harness operacional:**
- Como o SOT cria, atualiza, promove, refuta e arquiva hipóteses **em operação** — os protocolos e regras de transição, não a estrutura do objeto (que é o CHM-001).
- **Hypothesis Registry como serviço lógico:** alocação de ID, versionamento monotônico operacional, índice de estado ativo, API de consulta/reconstrução histórica. (Armazenamento físico — Blackboard vs. KG — pertence às SPEC-004/006.)
- **Protocolo de publicação no Blackboard** (D6): o que publicar, quando, em que ordem, com que versionamento — referenciando o contrato do CHM-001.
- **Integração com evidências (por referência a CEM-001):** como evidências e contraevidências transitam para/da hipótese operacionalmente; fronteira `Fonte → Dado → Evidência → Hipótese`.
- **Slot de convicção operacional:** como a hipótese referencia o objeto de convicção sem fechar fórmula/pesos (J-001 em aberto).
- **Herança fractal operacional:** regras de propagação parent/child em operação (graus/timeframes).
- **Auditabilidade (D9 por referência):** o que o modelo deve suportar para permitir reconstrução (P13) — sem fechar o mecanismo de persistência.

#### O que a SPEC-001 NÃO cobre (pertence a outras Specs ou decisões abertas)
- Redefinir a estrutura do CHM-001 — viola CONST-01.
- Fórmula/pesos/limiares do Conviction Vector — J-001 em aberto.
- Separação Conviction Engine × Synthesis Agent — B-001 em aberto.
- Schema de armazenamento físico (Blackboard/KG) — SPEC-004/006/009.
- Camada operacional de Evidence (provenance, qualidade, fusão) — SPEC-002.

#### Invariantes incidentes
- INV-01/02: hipótese tem origem na hierarquia Elliott→…→ICT; ICT não cria hipótese (de nenhum tipo).
- **Hipótese PRIMARY/SUB (Q-005):** SPEC-001 especifica a distinção — Elliott cria a hipótese primária/direcional; SMC/Fibonacci criam sub-hipóteses com `parent_id` obrigatório (herança fractal do CHM-001).
- **Estados canônicos (Q-006):** a máquina de estados é a do CHM-001 (EMERGENT→CANDIDATE→ACTIVE→DOMINANT→SUPERSEDED→REFUTED→ARCHIVED); RULE-BB-003 (PROPOSED/VALIDATED) foi descontinuada; o Blackboard não define estado próprio de hipótese.
- INV-06: evidências são Evidência (CEM-001), não Observação de Skill.
- INV-07: versionamento monotônico — refutação/arquivamento nunca deletam.
- INV-03: convicção é slot referenciado; dimensionalidade=8 (fechada); limiares definitivos = J-001 aberto.

#### Fontes prioritárias a consultar
`CHM-001_Baseline_1.0` (modelo canônico — autoridade) · `KERNEL V2` (hipótese como entidade, pertence ao Blackboard) · `Engenharia Geral` · `CEM-001` (contrato de Evidência) · `Auditoria de Ideias Não Implementadas` (Structural State Engine, ciclo de vida).

---

### SPEC-002 — Evidence & Evidence Provenance Harness
**HOMOLOGADA — BASELINE (Andraus, 2026-09-28, DHR-SPEC002-001).** P0 — CRITICAL · Profundidade-alvo **D0–D8** (elevada de D0–D7 na abertura, Q-A2 — CRITICAL exige D0–D8 por AGENTS.md §4).

Formaliza: camada Harness/operacional sobre **CEM-001** (baseline — não redefinido). Escopo: origem da evidência; tipo; qualidade/força operacional ≠ Convicção (INV-04); independência (anti-double-counting); temporalidade/aging; tipologia favorável/contraevidência/inconclusiva/**ausente**; detecção e **registro** de conflito (nunca resolução — SPEC-003); provenance; versão; ferramenta/Skill que produziu; ciclo de vida (CEM-001 Cap.4). Fronteira: `Fonte → Dado → Evidência` (Evidência→Hipótese já coberta pela SPEC-001). Ver `specs/features/SPEC-002/plan.md`.

---

### SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine (mecanismo invocado pelo Manager Fase 2)
**Prioridade:** P0 — BLOCKER · **Profundidade-alvo:** D0–D8 · **Estado: HOMOLOGADA — BASELINE** (Andraus, 2026-10-02, DHR-SPEC003-001)

> **HOMOLOGADA — BASELINE (2026-10-02, DHR-SPEC003-001).** Redige o **CCM-001** (agora BASELINED — `canon/CCM-001-canonical-conviction-model.md`). A Spec fecha **estrutura/método/mecanismo** do Conviction Vector 8D + Fusion/Conviction Engine + **limiares-piloto interinos** (≥70% / 7-9); **J-001 (fórmula/pesos/limiares definitivos) e N-001 (pesos por ativo) PERMANECEM ABERTAS** — valores definitivos pós-backtest (dona do backtest/calibração a definir — BL-032). Q-A9 ratificada (regime → dimensão `temporal`). Ressalvas de honestidade (BL-027 score, BL-028 Salvaguarda 1, BL-029 proveniência do gate) registradas, não fechadas.

> **Nota DHR-ARQ-001 (2026-10-01):** "Conviction Engine" no título é **rótulo de MECANISMO legado** (Classe D/H do CCM-001), **invocado pelo Manager Agent — Fase 2 (Conviction)** (ADR-MANAGER-001 / CEM-001 DIV-CEM-4) — **não** é um agente/componente separado. B-001 parcialmente SUPERSEDIDA (parte componente-separado); separação **lógica** de etapas preservada. Slot **não renumerado**.

Especificação tecnicamente mais crítica. Pipeline de MECANISMOS (B-001, Q-007 — parte componente-separado SUPERSEDIDA por DHR-ARQ-001): **Fusão de evidência (ACTIVE→DERIVED) → cálculo do Conviction Vector 8D → síntese**, etapas **invocadas pelo Manager Agent — Fase 2**, não agentes autônomos. Dimensionalidade FECHADA (Q-008): **8 dimensões** (estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica). Esta Spec **redige o CCM-001** (Canonical Conviction Model, hoje pendente). Resolver: escalas; normalização; pesos; independência; correlação; ausência de evidência; contraevidência; conflito; consenso; robustez; sensibilidade; aging; estabilidade; agregação; limites; incerteza; cálculo da convicção global; explicabilidade. **Fecha estrutura/método/mecanismo do CCM-001 + limiares-piloto interinos; J-001 (fórmula/pesos/limiares definitivos) e N-001 (pesos por ativo) permanecem ABERTAS para os valores definitivos pós-backtest** (CONS-01; dona do backtest a definir — BL-032). B-001 FECHADA (Q-007) e parcialmente SUPERSEDIDA por ADR-MANAGER-001 (DHR-ARQ-001): o "Conviction Engine" é **mecanismo invocado pelo Manager Agent — Fase 2**, não agente separado; preservada a separação **lógica** de etapas. **Nenhuma implementação downstream de decisão é suficientemente especificada antes desta etapa.**

---

## 5. FASE 2 — MEMÓRIA DE TRABALHO E COMUNICAÇÃO

### SPEC-004 — Cognitive Blackboard Protocol
**Prioridade:** P0 — CRITICAL · **Profundidade-alvo:** D0–D7

Definir: Blackboard como memória de trabalho; objetos publicados; versões; estados; namespaces/workspaces; mensagens; lifecycle; atualização; expiração; invalidação; concorrência; ordenação; idempotência; provenance; permissões; leitura/escrita/publicação; reconstrução histórica. O Blackboard é memória de trabalho; o Knowledge Graph é memória permanente.

### SPEC-005 — Cognitive Event Bus
**Prioridade:** P0 — HIGH · **Profundidade-alvo:** D0–D7

Definir: evento; envelope; origem; destino/subscrição; prioridade; timestamp; TTL; correlation ID; causation ID; retry; idempotência; ordering; delivery; falha; replay; dead-letter; observabilidade; relação com Blackboard. Princípio: `Blackboard guarda estado. Event Bus transporta mudanças.`

---

## 6. FASE 3 — MEMÓRIA SEMÂNTICA E RAG

### SPEC-006 — Cognitive Knowledge Graph
**Prioridade:** P0 — CRITICAL · **Profundidade-alvo:** D0–D7

Definir: ontologia; entidades; relações; temporalidade; provenance; versionamento; confiança; conhecimento permanente/temporário; causalidade; similaridade; relações estatísticas/hierárquicas/de hipótese/de evidência/de missão/de aprendizado; lifecycle; consulta cognitiva; governança de escrita. Resolve H-001.

### SPEC-007 — RAG / WikiRAG / Knowledge Formation Harness
**Prioridade:** P0 — CRITICAL · **Profundidade-alvo:** D0–D8

Formalizar: `Retrieval → Evidence Candidate → Knowledge Formation → Knowledge Candidate → Validation → Governance → Published Knowledge → Knowledge Graph / RAG`. Regras: `Documento recuperado ≠ verdade` · `Trecho recuperado ≠ conhecimento validado` · `Conhecimento candidato ≠ conhecimento publicado`.

---

## 7. FASE 4 — COGNIÇÃO E ESCALONAMENTO

### SPEC-008 — Manager — Orquestração Mecânica (Fase 1 + serviços de tempo) <!-- renomeado de "Cognitive Scheduler" por EUA-E23/DHR-EUA-E23, 2026-10-01; slot NÃO renumerado (INV-07) -->
**Prioridade:** P0 — CRITICAL · **Profundidade-alvo:** D0–D8

> **Nota DHR-EUA-E23 (2026-10-01):** slot repurposado como a **1ª das 3 Specs do Manager Agent** (Fase 1 — Dispatch + serviços de tempo), sob um **"Manager Contract"** comum (pai de herança vertical RULE-HV; ator único — ADR-MANAGER-001 §2.2). Classe predominante **D/C** (gates não-LLM, ENF-03) é orientação não-vinculante (declaração por BASpec — RULE-MECH-01). Slot **indicativo** (RULE-ECC-01/02): fronteira/decomposição final só na abertura.

Decidir: quem pensa; quando; por que; em que ordem; com qual profundidade; com qual orçamento; quais Skills despertar/não despertar; quando interromper/aguardar/escalar/encerrar. Incorpora ativação progressiva/lazy orchestration; dispatch/grafo de dependências; relógio/Killzone; alarme FSM; FSM do ciclo; orçamento.

### SPEC-009 — Cognitive State & Persistence Model
**Prioridade:** P0 — CRITICAL · **Profundidade-alvo:** D0–D7

Resolver: estado cognitivo; memória operacional; persistência; atualização; serialização; recuperação; expiração; compactação; continuidade entre candles e entre sessões; contexto ativo; recuperação após falha. **Resolve G-001.**

---

## 8. FASE 5 — AGENTES ANALÍTICOS

*Somente após o Kernel Cognitivo suficientemente especificado.*

### SPEC-010 — Structural Agent / Elliott Harness
P0 — CRITICAL · D0–D8. Elliott; múltiplas contagens; hipóteses concorrentes; Wave State; maturidade; energia; proporcionalidade; simetria; complexidade; ambiguidade; continuidade fractal; elasticidade; forecast; Structural Narrative; refutação; memória estrutural; protocolo Blackboard; Event Bus; estado persistente.

### SPEC-011 — Fibonacci & Fractal Confluence Harness
P1 — HIGH · D0–D7. Retrações; extensões; projeções; clusters; confluência; relações entre graus e timeframes; zonas; invalidações; dependência da hipótese estrutural.

### SPEC-012 — Institutional Agent / SMC Harness
P1 — HIGH · D0–D8. Liquidity; BOS; CHOCH; MSS; FVG; Order Blocks; Volume; Institutional Intent/Regime/Pressure/Efficiency/Narrative; causalidade; continuidade; forecast; refutação; Conviction Vector institucional.

### SPEC-013 — Execution / ICT Harness
P1 — HIGH · D0–D7. Exclusivamente: entrada; timing; stop; targets; invalidação operacional; OTE/FVG quando aplicável; condições de execução; risco; confirmação operacional. **Invariante: ICT não cria a hipótese estrutural.**

---

## 9. FASE 6 — SÍNTESE, MISSÃO E DECISÃO

### SPEC-014 — Manager — Convicção & Síntese (Fase 2; absorve o Synthesis Agent) <!-- renomeado de "Synthesis Agent" por EUA-E23/DHR-EUA-E23, consolidando DHR-ARQ-002; slot NÃO renumerado (INV-07) -->
P0 — CRITICAL · D0–D8. Somente após resolução de J-001 (mecanismo de convicção — SPEC-003). `Evidence → Hypothesis → Conviction → Decision → Mission / Trading Mission Package`.

> **Nota DHR-EUA-E23 (2026-10-01):** slot repurposado como a **3ª das 3 Specs do Manager Agent** — **Fase 2 (Convicção & Síntese)**, sob o "Manager Contract" comum. Classe predominante **H/P** (cognitivo leve + gate de saída), orientação não-vinculante (RULE-MECH-01). Fronteira anti-double-ownership com a SPEC-003 (EUA-E23 §4.1): a Fase 2 **invoca** o mecanismo (CCM-001/Conviction Vector 8D) e **decide**; **não** redefine o cálculo do vetor (DHR-ARQ-001).
> **Nota DHR-ARQ-002 (2026-10-01):** o **Synthesis Agent deixa de ser agente autônomo** — suas responsabilidades (arbitragem final; `Conviction→Decision→Mission/TMP`; geração do TMP interno) **são a Fase 2 do Manager Agent** (propaga ADR-MANAGER-001 §2.1 "Agente de Síntese → absorvido (Fase 2)"). O cálculo do Conviction Vector é o **mecanismo da SPEC-003** invocado pela Fase 2 (DHR-ARQ-001); o contrato do objeto TMP é a **SPEC-016** (repurposada). Slot SPEC-014 **repurposado, NÃO renumerado nem apagado** (INV-07). Nenhuma decisão aberta fechada (SPEC-015-SCOPE/J-001/N-001/WF-D03 seguem abertas — CONS-01).

### SPEC-015 — Manager — Missão & Ciclo de Vida (Fase 0) <!-- renomeado de "Mission Engine & Mission Lifecycle" por EUA-E23/DHR-EUA-E23, 2026-10-01; slot NÃO renumerado (INV-07) -->
P1 — HIGH · D0–D7.

> **Nota DHR-EUA-E23 (2026-10-01):** slot repurposado como a **2ª das 3 Specs do Manager Agent** — **Fase 0 (Mission Lifecycle)**, sob o "Manager Contract" comum. Classe predominante **H/P** (decisório leve + gate), orientação não-vinculante (RULE-MECH-01). O nome de slot legado "Mission Engine" é anotado como termo absorvido pelo Manager (ADR-MANAGER-001). Slot **indicativo** (RULE-ECC-01/02). **SPEC-015-SCOPE** (ADR §7) passa a endereçável, mas **não** é fechada aqui (CONS-01).

Criação; ativação; monitoramento; envelhecimento; atualização; suspensão; encerramento; invalidação; cancelamento; campanha; plano alternativo; relação hipótese→missão; relação missão→resultado.

### SPEC-016 — Trading Mission Package (TMP) — **REPURPOSADA** (Andraus 2026-09-22, C-04 Opção A; contingente à EUA-E19a/E20)
P1 — CRITICAL · D0–D7. **Novo escopo:** contrato de **handoff INTERNO** entre o Synthesis Agent e o Risk Agent — o TMP como **snapshot imutável, versionado, tipado, com timestamp** (ancora INV-RISK-00 — isolamento epistêmico). **Deixa de ser** o contrato de fronteira externa (esse papel passa a RISK-SPEC-022 — Signal Package). **Invariante: SOT não executa ordem.** *(Revisão substancial de escopo autorizada; efetiva quando a família RISK for autorizada via EUA-E20. Ver `reference/SOT-RISK-MASTER-001_Consolidado.md`.)*

---

## 10. FASE 7 — MEMÓRIA E APRENDIZADO

### SPEC-017 — Pattern Memory
P1 — MEDIUM · D0–D5. Episódio; setup; contexto; resultado; win rate; RR; amostra; confiança estatística; atualização; aging; segmentação por ativo/regime/timeframe.
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` — métricas de backtest como candidatas a episódios, sempre rotuladas 'Observação de backtest'. Possibilidade de fonte/ferramenta, não entrega de calibração; não fecha decisão aberta.*

### SPEC-018 — Learning & Knowledge Formation Governance
P1 — HIGH · D0–D8. Ciclo `Extração → Formalização → Validação → Backtest → Stress Test → Sandbox → Aprovação → Produção`. Resolve K-001.
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` — fluxo Pine (criar→compilar→backtestar→recalibrar) comprovado tecnicamente, sem validação estatística; insumo ao ciclo e ao BL-032. Possibilidade de fonte/ferramenta, não entrega de calibração; não fecha decisão aberta.*
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` — leituras do gráfico como Observação com proveniência alimentam o ciclo de aprendizado. Não é baseline nem fecha decisão aberta.*

---

## 10-bis. FASE RISK — RISK AGENT (família RISK-SPEC)
<!-- Instituída por EUA-E20/DHR-EUA-E20 (2026-10-01). -->

> **Posição lógica (EUA-E20):** a FASE RISK vem **após a FASE 6** (Síntese/Missão/TMP) no caminho crítico (ver §21) — depende do **Manager** (Fase 2) e do TMP interno (SPEC-016). Posicionada fisicamente aqui por disrupção mínima. **Não-autorizada** até homologação de abertura, cuja **pré-condição dura** é o `milestone:FASE 6 concluída` (= Manager — Fase 2 / SPEC-014 repurposado homologada, após DHR-ARQ-002). Rastreada por `backlog/BL-018-RISK-AGENT-backlog.md`.

**6 macro-slots INDICATIVOS (RULE-ECC-01/02) — não enumeram as 23 RISK-SPEC do `reference/SOT-RISK-MASTER-001_Consolidado.md` §6.2; cada macro-slot abre com Dossiê, que então propõe sua decomposição fina (pode dividir/fundir/renumerar — INV-07):**

- **RISK-M1 — Fundamento & Cognição de Risco** (Grupos A+B; princípios RP1–RP15 + disciplinas epistêmicas/causais/incerteza de risco, herdam N8–N17 via RULE-HV). Mapeia RISK-SPEC-001..009.
- **RISK-M2 — Decisão sob Risco & Risco-Retorno** (Grupo C; autoridade ACCEPT/WAIT/REJECT/ABSTAIN + deltas genuínos). Mapeia RISK-SPEC-010 (**RISK-CONV-001 já FECHADA por DHR-DEC-001, 2026-10-01: avaliação de risco = escala própria, nunca retroalimenta o Conviction Vector — WF-X05; a Spec implementa, não reabre**), 011 (R:R≥1:3 + Portfolio Heat≤15% + alavancagem), 012, 013. Ancora INV-RISK-RR/HEAT/LEV.
- **RISK-M3 — Quantificação & Stress** (Grupo D; VaR/CVaR/drawdown/correlação, Monte Carlo/bootstrap, calibração Brier/log-loss). Mapeia RISK-SPEC-014, 015, 016.
- **RISK-M4 — Memória, Aprendizado & Metacognição de Risco** (Grupo E; qualidade≠resultado; N17). Mapeia RISK-SPEC-017, 018, 019.
- **RISK-M5 — Operacionalização: Risk Harness, RDR & Signal Package** (Grupo F). Mapeia RISK-SPEC-020 (**Risk Harness — gate E3; a cláusula "via Risk Harness" em P14/INV-05 entra AQUI**), 021 (RDR — depende CDM-001), 022 (**Signal Package — D-RISK-SP-001**). Ancora INV-RISK-00 (isolamento epistêmico) junto da SPEC-016 (TMP interno, preservada).
- **RISK-M6 — Avaliação & Adversarial de Risco** (Grupo H; **herda SPEC-020 núcleo A via RULE-HV**). Mapeia RISK-SPEC-023.
- **(diferido) RISK-Skills** (Grupo G) — diferidas a **I-001 (FECHADA, DHR-I001-001 — híbrido por Classe)** / SPEC-025.

**Cobertura (RULE-ECC-01, item 4):** os 23 RISK-SPEC mapeiam integralmente RISK-M1..M6 (+ Skills diferidas) — nenhuma capacidade descartada em silêncio. **Decisões abertas incidentes (CONS-01 — nenhuma fechada aqui):** J-001, D-RISK-SP-001, CDM-001. *(RISK-ARR-LOC-001 e RISK-CONV-001 **FECHADAS** por DHR-DEC-001, 2026-10-01 — ver "Decisões FECHADAS" no topo.)*

---

## 11. FASE GOV — GOVERNANÇA DO HARNESS DE ESPECIFICAÇÃO
<!-- Reposicionada de "FASE 8" por EUA-E17/DHR-EUA-E17 (2026-09-21). -->

> **Posição lógica (EUA-E17):** esta FASE GOV **precede SPEC-002** no caminho crítico (ver §21) — vem logo após SPEC-001. A seção permanece nesta posição física do documento por disrupção mínima (renumeração editorial); a ordem autoritativa de execução é a do §21 e do banner do topo. **SPEC-019 HOMOLOGADA (2026-09-22). SPEC-020 núcleo A HOMOLOGADA (2026-09-27, DHR-SPEC020-001). SPEC-021 HOMOLOGADA (2026-09-28, DHR-SPEC021-001). FASE GOV CONCLUÍDA. Próximo trabalho autorizado: SPEC-002.**

### SPEC-019 — Harness Governance & Evolution — **HOMOLOGADA — BASELINE** (Andraus, 2026-09-22, DHR-SPEC019-001)
P0 — HIGH · D0–D8. Governa o próprio Harness: quem pode alterar Specs; quem cria RULE; quem aprova; versionamento; emendas; Constitution Check; impacto em schemas/RAG/Skills/testes; compatibilidade; rollback; exceções; auditoria. **Resolveu L-001** (FECHADA). RULE-HG-01..08 + RULE-HV-01..04 registradas em `governance/RULES.md`.
**Acréscimo de escopo (EUA-E17 Q1 — homologado):** **Contrato de Herança Vertical macro→micro (Harness Inheritance Contract)** — normativiza GEH-001 §6.4/§6.7 como spec formal: regra de conservação de requisitos entre harnesses pai/filho + verificação de conformidade inter-nível. (É o elo vertical que o MAN-001 — convergência horizontal — não cobre.) Método aplicado: atomic-spec v1.4.
*(Achados Menores M-01/M-02 do Revisor — sem BASpec dedicada para RULE-HG-08; critério objetivo de "spec-filha derivada" em RULE-HV-01 — diferidos para emenda futura como delta menor, por decisão de Andraus. Não bloqueiam a baseline.)*

---

## 12. FASE GOV (cont.) — META-HARNESS: AVALIAÇÃO & MATURIDADE
<!-- Reposicionada de "FASE 9" por EUA-E17/DHR-EUA-E17 (2026-09-21). Segue a SPEC-019 na FASE GOV, antes de SPEC-002. -->

### SPEC-020 — Harness Evaluation Specification
**HOMOLOGADA — BASELINE (Andraus, 2026-09-27, DHR-SPEC020-001).** P0 — CRITICAL · D0–D8. Define como o SOT Harness é avaliado. **Faseada por EUA-E17 (Q6 — homologado):**
- **Núcleo constitutivo (classe A — homologado nesta FASE GOV):** correctness; grounding; hallucination; role adherence; context management; safety; regression; robustness/adversarial (como método); **+ 9ª lente `principle consistency`** (SPEC-020-PRINC-001, efetiva nesta homologação). Estes são **critérios constitutivos** que SPEC-002+ devem satisfazer durante a produção (não apenas sensores posteriores).
- **Dimensões dependentes-de-upstream (classe B — DIFERIDAS, ver RMR-001/BL-017):** RAG faithfulness (fecha em SPEC-007); tool correctness (fecha em SPEC-038); decision traceability (fecha em SPEC-014). *(hypothesis consistency já fechável — SPEC-001 homologada.)* As dimensões B NÃO são tratadas como fechadas antes do seu componente-alvo (CONS-01).
- **SPEC-020-PRINC-001 — FECHADA (efetiva nesta homologação):** a SPEC-020 incorpora a **consistência principiológica do GPR-001 §15** como critério constitutivo verificável (BASpec-EV-009) — operacionalizando o enforcement de precedência e conflito de princípios (GPR-001 §3.2/§6), antes **declarativo** (L0–L1). Ver `specs/features/SPEC-020/plan.md`.

### SPEC-021 — Harness Score / Maturity Model
**HOMOLOGADA — BASELINE (Andraus, 2026-09-28, DHR-SPEC021-001).** P1 — HIGH · D0–D7. Escada canônica **por-Spec** (reconciliação Q-A2, resolveu CONFLITO-1): `L0 Declarativo → L1 Especificado → L2 Guiado → L3 Testável → L4 Autocontrolado` — 5 níveis, rótulo L3 harmonizado com Quality Gates (atomic-spec §7, que descreve os critérios de cada nível: D5+≥3 D7+≥1 D8+revisão independente). Maturidade não se confunde com volume de documentação. Segue o núcleo A da SPEC-020; torna o harness-score **normativo por spec** (gate E3 na homologação — abaixo do nível-alvo bloqueia, RULE-MM-05). **GPR-001 §11 (L0–L5) é eixo diferente** — maturidade do SOT como sistema agêntico inteiro, não por componente; não é substituído por esta escada. Ver `specs/features/SPEC-021/plan.md`. **FASE GOV concluída.**

---

## 13. FASE 8 — TESTE COGNITIVO INTEGRADO  <!-- renumerada de FASE 10 · EUA-E17 -->

### SPEC-022 — Cognitive Test & Adversarial Test Specification
P0 — CRITICAL · D0–D9. Hipótese concorrente; contraevidência; hipótese dominante instável; conflito Elliott×SMC; divergência temporal; RAG contraditório; fonte não confiável; ferramenta indisponível; contexto insuficiente; Conviction excessiva; confirmation/recency bias; alucinação; perda de contexto; erro de ferramenta; corrupção de memória; evento duplicado.

---

## 14. FASE 9 — INTEGRAÇÃO COGNITIVA  <!-- renumerada de FASE 11 · EUA-E17 -->

### SPEC-023 — Cognitive Orchestrator
P1 — CRITICAL. Somente após `Scheduler + Blackboard + Event Bus + Agents + Mission + Conviction`. Coordena sem assumir responsabilidades analíticas dos especialistas.

### SPEC-024 — Meta Cognitive Supervisor
P2 — HIGH. Observa: qualidade do raciocínio; estabilidade; mudanças excessivas de hipótese; viés; consumo de tokens; comportamento das Skills; divergência entre agentes; degradação de qualidade; falhas recorrentes; maturidade cognitiva.

---

## 15. FASE 10 — SKILLS  <!-- renumerada de FASE 12 · EUA-E17 -->

### SPEC-025 — Skill Development Specification
P1 — HIGH. Plataforma para todas as Skills: definição; atomicidade; input/output; pré/pós-condições; ferramentas; conhecimento; RAG; evidência; eventos; Blackboard; testes; adversarial; versionamento; certificação; performance; custo; autonomia; governança. **I-001 FECHADA (DHR-I001-001, 2026-09-28) — direção híbrida por Classe (Opção C): esta Spec formaliza como Skill separada só as competências Classe D; o critério de corte exato é matéria do Dossiê de abertura desta própria Spec.**
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` — possível Skill 'Pine+backtest' só após esta Spec. Possibilidade de fonte/ferramenta, não entrega de calibração; não fecha decisão aberta.*
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` — leitura top-down e checklist como base de futuras Skills de coleta. Não é baseline nem fecha decisão aberta.*

---

## 16. FASE 11 — SKILLS ANALÍTICAS  <!-- renumerada de FASE 13 · EUA-E17 -->

*Somente após SPEC-025.*

SPEC-026 Elliott · SPEC-027 Fibonacci · SPEC-028 Fractal/Confluence · SPEC-029 Liquidity · SPEC-030 BOS/CHOCH/MSS · SPEC-031 FVG/Order Block · SPEC-032 Volume · SPEC-033 AO/Divergence · SPEC-034 Trend/Channel · SPEC-035 ICT Execution · SPEC-036 Market Regime · SPEC-037 Volatility/Context.

Cada Skill só criada quando houver responsabilidade realmente atômica e independente. Não criar Skills apenas para aumentar a quantidade de componentes.

---

## 17. FASE 12 — FERRAMENTAS E ANALYTICAL TOOLING  <!-- renumerada de FASE 14 · EUA-E17 -->

### SPEC-038 — Trading Analysis Tool Harness
Contrato de ferramentas: TradingView; Pine Script; OHLC; volume; indicadores; gráficos; dados derivados; cálculo; ferramentas externas. Cada ferramenta declara: `Finalidade → Input → Output → Precisão → Determinismo → Limitações → Custo → Latência → Provenance → Falhas`.
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` — quatro ferramentas Pine (injetar, compilar, ler Strategy Tester, alterar entradas) como rascunho de contrato. Possibilidade de fonte/ferramenta, não entrega de calibração; não fecha decisão aberta.*
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` — mecânica MCP+CDP, contrato mínimo §9 e armadilhas A1–A9 como rascunho; NÃO autoriza o canal (Termos de Uso abertos). Não é baseline nem fecha decisão aberta.*

### SPEC-039 — Tool Selection & Tool Governance
Quando utilizar/não utilizar ferramenta; ferramenta preferencial; fallback; validação; segurança; custo; limite; tool poisoning; dados não confiáveis; resultado contraditório.
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-PINE-BACKTEST-CALIBRACAO-SOT.md` — injetar código/adicionar ao gráfico exigem gate de confirmação; saída de ferramenta é dado não-confiável. Possibilidade de fonte/ferramenta, não entrega de calibração; não fecha decisão aberta.*
*Ref. não-normativa (2026-10-03): `reference/externo/TUTORIAL-TRADINGVIEW-MCP-CLAUDE-CODE.md` — perfil exploratório supervisionado, confirmação antes de efeitos e saída de ferramenta como dado não-confiável. Não é baseline nem fecha decisão aberta.*

---

## 18. FASE 13 — OBSERVABILIDADE E AUDITORIA  <!-- renumerada de FASE 15 · EUA-E17 -->

### SPEC-040 — Cognitive Observability
`Evento → Evidência → Hipótese → Conviction → Decisão → Missão → Resultado → Aprendizado`. Tracing; correlation/causation ID; custo; tokens; latência; ferramentas; fontes; versões; Skills; estados.

### SPEC-041 — Cognitive Audit & Decision Reconstruction
Profundidade D9. "Conseguimos reconstruir exatamente por que o SOT chegou a essa decisão?"

---

## 19. FASE 14 — HARNESS DE PRODUÇÃO  <!-- renumerada de FASE 16 · EUA-E17 -->

### SPEC-042 — Runtime Guardrails
Allow; deny; limites; permissões; gates; enforcement; sandbox; operações críticas; escalonamento humano.

### SPEC-043 — Context Window & Context Integrity Harness
Crescimento de contexto; compressão; progressive disclosure; recuperação; handoff; perda de contexto; contexto contaminado; duplicação; contexto obsoleto. Regra: `detecção de risco de estouro → alerta → preservação → handoff completo → continuidade segura`.

### SPEC-044 — Hallucination Detection & Integrity Harness
Afirmação sem fonte; conflito com fonte; invenção de artefato/decisão; extrapolação não autorizada; falsa certeza; referência inexistente; alteração silenciosa de baseline; mistura de inferência com fato.

---

## 20. FASE 15 — INTEGRAÇÃO FINAL  <!-- renumerada de FASE 17 · EUA-E17 -->

### SPEC-045 — SOT End-to-End Cognitive Flow
`Market Data → Context → Evidence → Hypothesis → Structural Analysis → Fibonacci/Fractal → Institutional Narrative → Conviction → Decision → Mission → ICT Execution Plan → Trading Mission Package → Execução downstream → Outcome → Learning → Knowledge → Governance`.

**Decisão aberta incidente — `[DECISÃO NECESSÁRIA: SPEC-045-RUNTIME-001]`** (registrada por Andraus, 2026-09-22): Formalizar o **caminho de leitura em runtime** (spec → compilação → **prefixo estável (RULE-CEE-003) + guardrails (SPEC-042) + Skills certificadas (SPEC-025) + memória cognitiva (SPEC-004/006/007/009/017)**) como **baseline arquitetural** na SPEC-045. Hoje vive como inferência coerente (síntese 2026-09-22) — **não é baseline**; o mecanismo físico de carga permanece deliberadamente não-especificado por decisão (§22). **Efetiva na homologação da SPEC-045.** Distinta de: BL-013/SPEC-018 (governança de runtime = adoção de políticas em operação) e BL-006 (automação de gates por código) — problemas separados, inalterados por esta decisão.

---

## 21. Ordem de prioridade — caminho crítico

```
M0 → 001 Hypothesis Harness →
[FASE GOV] 019 Harness Governance (+ Herança Vertical) → 020 Harness Evaluation (núcleo A) → 021 Harness Score →
002 Evidence → 003 Conviction Vector → 004 Blackboard → 005 Event Bus →
006 Knowledge Graph → 007 RAG (fecha 020: RAG faithfulness) →
008 Manager — Orquestração Mecânica [Fase 1] → 009 Cognitive State → 010 Structural → 011 Fibonacci/Fractal →
012 Institutional → 013 ICT → 014 Manager — Convicção & Síntese [Fase 2; absorve Synthesis — DHR-ARQ-002/EUA-E23] (fecha 020: decision traceability) →
015 Manager — Missão & Ciclo de Vida [Fase 0] → 016 Trading Mission Package →
[FASE RISK — EUA-E20] RISK-M1 → RISK-M2 → RISK-M3 → RISK-M4 → RISK-M5 → RISK-M6  (após a FASE 6; macro-slots indicativos)
```

*(Ordem atualizada por EUA-E17/DHR-EUA-E17: a FASE GOV — 019 → 020 núcleo A → 021 — precede 002. Dimensões B da SPEC-020 fecham no ponto de dependência: 007, 014, 038 — ver RMR-001/BL-017. `038 Tool Selection/Tooling` fecha `tool correctness` na FASE 12.)*
*(EUA-E23/DHR-EUA-E23: SPEC-008/014/015 = as 3 Specs do **Manager Agent** sob um "Manager Contract" comum — ator único, RULE-HV; slots não renumerados. EUA-E20/DHR-EUA-E20: a **FASE RISK** (RISK-M1..M6, indicativos) vem após a FASE 6, não-autorizada até `milestone:FASE 6 concluída` = Manager Fase 2 homologada.)*

Depois: Learning → Testing → Meta-Cognition → Skills → Tools → Observability → Runtime Harness → End-to-End. *(Governance/Evaluation/Maturity já realizadas na FASE GOV, no início.)*

> **EUA-E21 (DHR-EUA-E21):** a ordem acima é **orientação de dependência** entre slots indicativos, revisável na abertura de cada Spec com justificativa homologada (RULE-ECC-01, item 5); **não** fixa a quantidade nem a numeração final das Specs.

---

## 22. O que não será especificado agora

Não iniciar: implementação; código; APIs; banco de dados; framework de agentes; escolha definitiva de LLM; infraestrutura de produção; microserviços; deployment; Skills individuais antes da SPEC-025; componentes redundantes já cobertos por modelos canônicos baselined.

A arquitetura deve permanecer independente da implementação. No Claude Code: usar PLAN/CHECKS da skill como spec/verificação-de-spec; BUILD/VERIFY-de-código só na fase de implementação.

**Quantidade de Specs não pré-determinada (EUA-E21):** não se fixa antecipadamente quantas Specs existirão nem sua numeração final; ver o banner de vigência e o §26 (capacidades exigidas).

---

## 23. Gate entre cada Spec

Nenhuma Spec seguinte inicia enquanto a anterior não passar por:

```
1. Leitura de roadmap.md + atomic-spec.md
1-bis. ABERTURA DA SPEC (RULE-ECC-01/02 — EUA-E21): Dossiê de Pesquisa (estado da arte e melhores práticas na web, pelo próprio Especificador) + proposta de escopo/quantidade/fronteira/número + proposta de re-apontamento de gatilhos do RMR-001 (se dividir/fundir/renumerar/descartar slot) → parecer do Revisor sobre o Dossiê → HOMOLOGAÇÃO de Andraus da definição, ANTES de escrever o Plan. Sem Dossiê: fail-closed (NÃO CONFORME Crítica). Web indisponível: abertura suspensa (exceção só por RULE-HG-07)
2. Pesquisa especializada (incluindo modelos canônicos baselined)
3. RAG do projeto
4. Análise de cobertura (o que já existe; o que falta)
5. Especificação BASpec (camada Harness/operacional — não redefinir canônicos)
6. Design D4–D6 (quando aplicável)
7. Testes D7–D8 (quando aplicável)
8. Auditoria D9 (quando aplicável)
9. Autopré-check do Especificador
10. Verificação — Revisor (GRE-001/HRE-001)
11. HOMOLOGAÇÃO — Andraus
11-bis. Consultar RMR-001 — verificar itens cujo Gatilho de Ativação (`spec:`/`milestone:`/`decisao:`) disparou com esta homologação e tratá-los; nenhum item `ATIVADO` pode ficar sem encaminhamento
12. Geração do .md
13. Entrega em approved/
14. Somente então: próxima Spec
```

> **Passo 11-bis — HOMOLOGADO (Andraus, 2026-09-19, DHR-PAP-001-C).** Materializa o "o sistema informa" do RMR-001 §4: após a HOMOLOGAÇÃO (passo 11), consultar `backlog/RMR-001_Painel_Backlog.md`, tratar os itens ativados por esta homologação, e só então avançar (passo 14). Agora **vinculante** — um item `ATIVADO` sem encaminhamento é achado de gate.

---

## 24. Princípio central

O Road Map não pretende maximizar quantidade de documentos. Pretende maximizar:

`Eficácia → Efetividade → Eficiência → Economicidade`

sob a restrição `governança + rastreabilidade + verificabilidade + explicabilidade`.

**Regra fundamental:** especificar somente aquilo que precisa existir como unidade arquitetural ou comportamental independente; aprofundar somente até o nível necessário para tornar o comportamento verificável; construir sobre modelos canônicos baselined — nunca redefini-los.

---

## 25. Primeiro ponto de execução

O próximo trabalho autorizado é:

```
SPEC-004 — Cognitive Blackboard Protocol (P0 CRITICAL, D0–D7)   [caminho crítico — FASE 2]
+ linha paralela autorizada: SPEC-038 — Trading Analysis Tool Harness (viabilidade como critério; BL-031)
```

*(Atualizado por DHR-SPEC003-001, 2026-10-02. SPEC-001, SPEC-019, SPEC-020 núcleo A, SPEC-021, SPEC-002 e **SPEC-003** já homologadas — BASELINE. **FASE GOV CONCLUÍDA**; FASE 1 — NÚCLEO COGNITIVO concluída com a SPEC-003.)*  
A **SPEC-003 homologada** redige o **CCM-001** (agora BASELINED) e torna o Conviction/Fusion Engine camada operacional vigente sobre CEM-001/CHM-001: fecha **estrutura/método/mecanismo** do Conviction Vector 8D + **limiares-piloto interinos**. **J-001** (fórmula/pesos/limiares definitivos) e **N-001** (pesos por ativo) **permanecem ABERTAS** — valores definitivos pós-backtest (dona do backtest/calibração a definir — BL-032). **Linha paralela (chat Andraus, 2026-10-02):** abertura da **SPEC-038** (Trading Analysis Tool Harness) com viabilidade como critério — avaliação da conexão TradingView↔SOT (BL-031). Abertura de qualquer Spec segue o passo 1-bis do §23 (Dossiê de Pesquisa, RULE-ECC-01/02/04).

---

*Road Map SOT — baseline homologado (2026-09-12) + observação de arranque SPEC-001 (2026-09-14: CHM-001 como base, não redefinir). Método vigente: `atomic-spec.md`. Painel vivo: RMR-001.*

---

## 25-bis. Exceção de ordem — SPEC-046 (Spec-Time Context Caching Harness)

Aberta **fora da ordem de dependência** acima, por decisão direta de Andraus (2026-09-28, DHR-SPEC046-001), sob a faculdade de RULE-ECC-01 de rever a ordem entre slots indicativos com justificativa homologada (governance/RULES.md, RULE-ECC-01). **Não substitui nem adia SPEC-002** — que continua sendo o "próximo trabalho autorizado" pela ordem regular (§25). A SPEC-046 é uma linha paralela: tooling de caching do próprio harness de especificação (Especificador/Revisor, spec-time), restrita ao **Grupo B** da proposta de origem (`reference/externo/CACHING SOT.MD` §1.1) — o Grupo A (agentes cognitivos internos, regidos por CHM-001/CEM-001) permanece fora de escopo, adiado para quando os agentes analíticos (SPEC-010..014) existirem.

Origem: `reference/externo/CACHING SOT.MD` (RPIR/HOD-001) → parecer de auditoria do Revisor (CONFORME COM RESSALVAS, ACHADO-C1/M1/M2) → BL-024 (RMR-001) → Dossiê de Pesquisa + Proposta de Abertura do Especificador (`specs/features/SPEC-046/`) → parecer do Revisor sobre o gate de abertura (CONFORME) → **DHR-SPEC046-001** (homologação da abertura) → Plan (`plan.md`/`checks.md`, protocolo semântico GRE-001/HRE-001) → parecer do Revisor: CONFORME → **DHR-SPEC046-002** (homologação de baseline v1.0, 2026-09-28). **Status: HOMOLOGADA — BASELINE.** BL-024 → `Absorvido`. BL-025 (CACHE-ISS-001, extensão de inter-sessão) teve gatilho `spec:SPEC-046 homologada` disparado por este ato — **emenda aditiva v1.1 formalizada** (`EC-SPEC046-03` + BASpecs CISS-001..004), parecer do Revisor CONFORME (8 passos + 5-bis, 2 achados Menores não-bloqueantes), **homologada por Andraus, 2026-09-28 — DHR-SPEC046-003**. BL-025 → `Absorvido`. v1.0 permanece intacta (INV-07).

---

## 25-ter. Análises de priorização e adiantamento (não-normativas)

Duas análises do Especificador (2026-09-28) avaliam ganho/risco 4Es sobre itens do RMR-001 e sobre os slots indicativos deste ROADMAP. **Nenhuma das duas é normativa, abre Spec, promove item ou altera a ordem dos §21/§25/§25-bis** — são `[PROPOSTA]` de leitura auxiliar (TRACE-06); só passam a fato normativo quando um ato de Andraus/DHR específico as executa, registrado no RMR-001 ou neste ROADMAP. Vinculadas aqui para que nenhum agente as leia como sequência autoritativa paralela ao §21 (ordem de prioridade) ou ao §25 (próximo trabalho autorizado).

| Documento | Escopo | Relação com este ROADMAP | Status de execução (verificar RMR-001 para o estado corrente) |
|---|---|---|---|
| `backlog/ANALISE-PRIORIZACAO-BACKLOG-2026-09-28.md` | 13 itens `Em espera`/`Proposto` do RMR-001 (BL-001..018), ordenados por ganho 4Es × risco | Não re-sequencia Specs; só recomenda trabalho preparatório de spec-time (classificação, auditoria, promoção administrativa) que **não** promove nem abre nada por si | **Parcial**: BL-009 e BL-010/011/012 executados e homologados (`Absorvido`/DHR-BL010-011-012-001); BL-017 (promoção `Proposto`→`Em espera`) e BL-018 (análise preparatória RISK-MASTER×N8–N17) seguem pendentes de ato de Andraus; BL-015 opcional, não feito |
| `governance/AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md` | Todo slot indicativo SPEC-002..047 ainda não aberto, classificado Bloco S/R × Risco NULO–CRÍTICO | Explicitamente subordinada ao §21/§25/§25-bis (mesmo texto do documento, §0: "SPEC-002 é o próximo passo regular... nenhuma recomendação aqui bloqueia, atrasa ou condiciona SPEC-002") | **Parcial**: SPEC-002 — **abertura homologada** (DHR-SPEC002-001, 2026-09-28; Plan ainda não iniciado); SPEC-022 (parte S — taxonomia adversarial) recomendada ADIANTAR, sem Dossiê produzido; SPEC-025 (sliver S) tinha a condição de bloqueio (I-001) satisfeita em 2026-09-28 (DHR-I001-001) — decisão de abrir Dossiê antecipado permanece separada e pendente |

**Regra de leitura:** consultar sempre o §21 (ordem de prioridade) e o §25/§25-bis (próximo trabalho autorizado + exceções homologadas) como a sequência vigente; as duas análises acima são material de apoio para a decisão de Andraus, não substituem nem prevalecem sobre eles (CONS-01/INV-09).

---

## 26. Capacidades exigidas (cobertura) — EUA-E21

Lista **derivada dos títulos dos slots** acima (nenhuma capacidade foi inventada) e mantida como **restrição de cobertura** (RULE-ECC-01, item 4): cada Spec, ao ser aberta, declara quais capacidades cobre; **capacidade sem Spec ao fim de uma fase = achado de gate** (nada é descartado em silêncio). Só SPEC-001 e SPEC-019 estão abertas; as demais linhas são **indicativas** até a abertura. Atualizada por registro aditivo (INV-07).

| Capacidade exigida (tema do slot) | Seção/FASE do ROADMAP | Estado de abertura |
|---|---|---|
| SPEC-001 — Hypothesis Harness (sobre CHM-001) | 4. FASE 1 — NÚCLEO COGNITIVO | Aberta — HOMOLOGADA (baseline) |
| SPEC-002 — Evidence & Evidence Provenance Harness | 4. FASE 1 — NÚCLEO COGNITIVO | **Aberta — HOMOLOGADA (baseline)** |
| SPEC-003 — Conviction Vector, Evidence Fusion Engine & Conviction Engine | 4. FASE 1 — NÚCLEO COGNITIVO | **Aberta — HOMOLOGADA (baseline)** |
| SPEC-004 — Cognitive Blackboard Protocol | 5. FASE 2 — MEMÓRIA DE TRABALHO E COMUNICAÇÃO | Indicativo — não aberta |
| SPEC-005 — Cognitive Event Bus | 5. FASE 2 — MEMÓRIA DE TRABALHO E COMUNICAÇÃO | Indicativo — não aberta |
| SPEC-006 — Cognitive Knowledge Graph | 6. FASE 3 — MEMÓRIA SEMÂNTICA E RAG | Indicativo — não aberta |
| SPEC-007 — RAG / WikiRAG / Knowledge Formation Harness | 6. FASE 3 — MEMÓRIA SEMÂNTICA E RAG | Indicativo — não aberta |
| SPEC-008 — **Manager — Orquestração Mecânica** (Fase 1; ex-"Cognitive Scheduler"; EUA-E23) | 7. FASE 4 — COGNIÇÃO E ESCALONAMENTO | Indicativo — não aberta |
| SPEC-009 — Cognitive State & Persistence Model | 7. FASE 4 — COGNIÇÃO E ESCALONAMENTO | Indicativo — não aberta |
| SPEC-010 — Structural Agent / Elliott Harness | 8. FASE 5 — AGENTES ANALÍTICOS | Indicativo — não aberta |
| SPEC-011 — Fibonacci & Fractal Confluence Harness | 8. FASE 5 — AGENTES ANALÍTICOS | Indicativo — não aberta |
| SPEC-012 — Institutional Agent / SMC Harness | 8. FASE 5 — AGENTES ANALÍTICOS | Indicativo — não aberta |
| SPEC-013 — Execution / ICT Harness | 8. FASE 5 — AGENTES ANALÍTICOS | Indicativo — não aberta |
| SPEC-014 — **Manager — Convicção & Síntese** (Fase 2; absorve o Synthesis Agent — DHR-ARQ-002; nome de slot fixado por EUA-E23/DHR-EUA-E23); capacidade preservada | 9. FASE 6 — SÍNTESE, MISSÃO E DECISÃO | Indicativo — não aberta |
| SPEC-015 — **Manager — Missão & Ciclo de Vida** (Fase 0; ex-"Mission Engine & Mission Lifecycle"; EUA-E23) | 9. FASE 6 — SÍNTESE, MISSÃO E DECISÃO | Indicativo — não aberta |
| SPEC-016 — Trading Mission Package (TMP) — **REPURPOSADA** (Andraus 2026-09-22, C-04 Opção A; contingente à EUA-E19a/E20) | 9. FASE 6 — SÍNTESE, MISSÃO E DECISÃO | Indicativo — não aberta |
| SPEC-017 — Pattern Memory | 10. FASE 7 — MEMÓRIA E APRENDIZADO | Indicativo — não aberta |
| SPEC-018 — Learning & Knowledge Formation Governance | 10. FASE 7 — MEMÓRIA E APRENDIZADO | Indicativo — não aberta |
| **FASE RISK — Risk Agent** (RISK-M1..M6, 6 macro-slots indicativos + Skills diferidas; cobre 23 RISK-SPEC de BL-018 — EUA-E20/DHR-EUA-E20) | 10-bis. FASE RISK — RISK AGENT | Indicativo — não aberta (pré-condição: `milestone:FASE 6 concluída`) |
| SPEC-019 — Harness Governance & Evolution — **HOMOLOGADA — BASELINE** (Andraus, 2026-09-22, DHR-SPEC019-001) | 11. FASE GOV — GOVERNANÇA DO HARNESS DE ESPECIFICAÇÃO | Aberta — HOMOLOGADA (baseline) |
| SPEC-020 — Harness Evaluation Specification | 12. FASE GOV (cont.) — META-HARNESS: AVALIAÇÃO & MATURIDADE | **Aberta — HOMOLOGADA (baseline, núcleo A)** |
| SPEC-021 — Harness Score / Maturity Model | 12. FASE GOV (cont.) — META-HARNESS: AVALIAÇÃO & MATURIDADE | **Aberta — HOMOLOGADA (baseline)** |
| SPEC-022 — Cognitive Test & Adversarial Test Specification | 13. FASE 8 — TESTE COGNITIVO INTEGRADO | Indicativo — não aberta |
| SPEC-023 — Cognitive Orchestrator | 14. FASE 9 — INTEGRAÇÃO COGNITIVA | Indicativo — não aberta |
| SPEC-024 — Meta Cognitive Supervisor | 14. FASE 9 — INTEGRAÇÃO COGNITIVA | Indicativo — não aberta |
| SPEC-025 — Skill Development Specification | 15. FASE 10 — SKILLS | Indicativo — não aberta |
| SPEC-046 — Spec-Time Context Caching Harness (Especificador/Revisor) — **HOMOLOGADA FORA DE ORDEM** (Andraus, 2026-09-28, DHR-SPEC046-001 abertura + DHR-SPEC046-002 baseline v1.0 + DHR-SPEC046-003 emenda v1.1; ver §25-bis) | Fora da sequência de FASEs — linha paralela, tooling do próprio harness, não domínio de trading | **HOMOLOGADA — BASELINE v1.1** |
| SPEC-038 — Trading Analysis Tool Harness | 17. FASE 12 — FERRAMENTAS E ANALYTICAL TOOLING | Indicativo — não aberta |
| SPEC-039 — Tool Selection & Tool Governance | 17. FASE 12 — FERRAMENTAS E ANALYTICAL TOOLING | Indicativo — não aberta |
| SPEC-040 — Cognitive Observability | 18. FASE 13 — OBSERVABILIDADE E AUDITORIA | Indicativo — não aberta |
| SPEC-041 — Cognitive Audit & Decision Reconstruction | 18. FASE 13 — OBSERVABILIDADE E AUDITORIA | Indicativo — não aberta |
| SPEC-042 — Runtime Guardrails | 19. FASE 14 — HARNESS DE PRODUÇÃO | Indicativo — não aberta |
| SPEC-043 — Context Window & Context Integrity Harness | 19. FASE 14 — HARNESS DE PRODUÇÃO | Indicativo — não aberta |
| SPEC-044 — Hallucination Detection & Integrity Harness | 19. FASE 14 — HARNESS DE PRODUÇÃO | Indicativo — não aberta |
| SPEC-045 — SOT End-to-End Cognitive Flow | 20. FASE 15 — INTEGRAÇÃO FINAL | Indicativo — não aberta |
| (reservado) SPEC-047 — Runtime Cognitive Caching Harness (Grupo A — agentes estruturais/institucionais/operacionais/manager/risco, CHM-001/CEM-001) | Deliberadamente ADIADA — dependência de SPEC-002/010-014 (BL-024 §0 do faseamento) | Não proposta — placeholder de rastreabilidade apenas |
