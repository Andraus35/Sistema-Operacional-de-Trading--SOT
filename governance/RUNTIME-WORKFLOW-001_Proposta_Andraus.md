# RUNTIME-WORKFLOW-001 — Proposta de Workflow de Runtime do SOT (insumo de Andraus)

| Campo | Valor |
|---|---|
| Código | **RUNTIME-WORKFLOW-001** |
| Natureza | **Documento de insumo** (não-normativo) — registro verbatim de uma proposta de **fluxo de acionamento e formação de convicção entre os agentes cognitivos** ("workflow de runtime" no sentido de **orquestração cognitiva do Harness**, não de software — ver §0-bis), trazida por Andraus em chat, com decomposição preliminar mapeada contra o baseline. **NÃO é Spec, NÃO é emenda, NÃO fecha decisão aberta.** |
| Status epistemológico | **INSUMO — `[FONTE]` (registro de diretiva) + `[INFERÊNCIA]` (decomposição/mapeamento) + `[DECISÃO NECESSÁRIA]` (o que depende de Andraus).** Não é baseline. Não é FATO NORMATIVO nem FATO ARQUITETURAL. |
| Origem | Andraus (dono do projeto), chat, 2026-09-29 — mesma diretiva que originou a EUA-E23. |
| Vínculo normativo | `[PROPOSTA]` — **Após homologação da EUA-E23 (RULE-ECC-06)**, este documento **passará a ser leitura obrigatória** do Dossiê de Pesquisa de qualquer Spec futura que abra **K-001 / SPEC-018 / SPEC-045-RUNTIME-001** ou que seja **Spec de agente operacional, manager/contexto ou de risco**. Enquanto a EUA-E23 não for homologada, este é insumo não-normativo sem vínculo de leitura obrigatória. |
| Autoria do registro | Especificador (Claude Code), 2026-09-29 |
| Fundamento no baseline | INV-07 (nada deletado; registro aditivo) · CONS-01 (não fecha decisão aberta) · RULE-MET-01 (não-fabricação; o que Andraus não disse não é inferido como fato) · AGENTS.md §9 (SOT não executa ordem; produz Signal Package; TMP interno) · RULE-ECC-02 (Dossiê de Pesquisa) |

---

## 0-bis. Esclarecimento terminológico — "runtime" aqui = orquestração cognitiva, não software (Andraus, 2026-09-29) `[FONTE]`

**"Runtime" neste documento NÃO significa runtime de software/código.** O SOT está em fase **spec-first** (BUILD/VERIFY-de-código adiados — AGENTS.md §1); não há implementação de código a especificar aqui. Quando Andraus fala em "workflow do Trading em runtime", refere-se ao **funcionamento operacional do Harness Cognitivo**: a **sequência de acionamento e a troca de evidência/hipótese/convicção entre os agentes LLM especificados pelas Specs**, quando o SOT estiver "rodando" em uma sessão de trading ao vivo. Portanto este workflow é insumo para a **especificação da orquestração cognitiva dos agentes** — não para arquitetura de software, infraestrutura ou execução técnica.

Consequências de leitura:
- As decisões abertas correlatas — **K-001** (ciclo de evolução do conhecimento), **SPEC-018** (Learning & Knowledge Formation Governance) e **SPEC-045-RUNTIME-001** (caminho de leitura/operação em runtime do harness) — tratam "runtime" como o **caminho de operação do harness já especificado**, não como implementação de código.
- **Achado registrado (não forçar equivalência):** se, na abertura da SPEC-045, a decisão **SPEC-045-RUNTIME-001** vier a ser interpretada como algo mais próximo de runtime técnico/software (carga física de prefixo/guardrails/Skills/memória — ROADMAP §20), essa distinção deve ser **explicitada como achado** na abertura; este insumo **não** afirma equivalência entre "orquestração cognitiva" (sentido de Andraus aqui) e "runtime técnico" (possível leitura da §20). Os dois sentidos coexistem até que a SPEC-045 os separe. `[DECISÃO NECESSÁRIA]` — Andraus/abertura da SPEC-045.

## 0. Aviso de status (CONS-01 / RULE-MET-01) `[FATO]`

Este documento **registra uma proposta de Andraus como insumo** — não a homologa nem a converte em requisito. Nenhuma decisão aberta é fechada aqui (**K-001, SPEC-018, SPEC-045-RUNTIME-001, RISK-CONV-001, RISK-ARR-LOC-001, J-001, G-001, H-001, M-001, N-001, C-001** permanecem abertas). A decomposição da §2 é **`[INFERÊNCIA]` do Especificador** para orientar pesquisa futura; onde o texto de Andraus não sustenta um detalhe, ele é marcado `[DECISÃO NECESSÁRIA]` e **não** preenchido por invenção. Em qualquer conflito entre este insumo e um invariante constitucional (AGENTS.md §6/§9), **o invariante prevalece** e o conflito vira achado a tratar na abertura da Spec correspondente.

## 1. Workflow verbatim (Andraus, 2026-09-29) `[FONTE]`

> "Está é minha proposta de workflow do Trading em runtime com o SOT:
>
> Antes da abertura da Killzone coloco o sistema para rodar. Aponto o Time frame e o tipo de Trading que quero realizar: position, swing ou day Trading. Agente estrutural começará a verificar a estrutura de ondas e após observar, marcar, tratar evidencia, hipótese e formar convicção entrega sua análise e convicção. Se houver oportunidade apontada pelo agente anterior, dispara o agente institucional que fará o mesmo. Após sua análise e entrega, o manager agente formará a convicção macro de contexto e se houver oportunidade conclusiva deverá adicionar um alarme-gatilho no nível de preço a ser ativado ou não após abertura da Killzone. Se ativado agente operacional entra com sua análise do time frame da entrada (difere do de contexto) fazendo o devido tratamento e entrega ao manager. Após colher os dados do operacional o manager formará convicção global e decidirá envio com dados de risco-retorno ao agente de risco que por sua vez fará sua análise e decidirá se envia sinal ou não ao bot finance externo com dados da entrada."

*(Transcrição literal — RCN-001/PC-06. Grafia original preservada, incluindo "Está"/"evidencia".)*

## 2. Decomposição preliminar (mapeamento contra o baseline) `[INFERÊNCIA]`

Etapas e atores citados por Andraus, mapeados contra o ROADMAP/AGENTS.md. **A coluna "Baseline correlato" indica onde a etapa provavelmente se especifica; a coluna "Depende de" indica a decisão aberta ou Spot que a governa.**

| # | Etapa (verbatim → paráfrase) | Ator citado | Baseline correlato (slot indicativo) | Depende de |
|---|---|---|---|---|
| E1 | Operador arma o sistema antes da Killzone; aponta **timeframe** e **tipo de trade** (position/swing/day) | Operador (Andraus) | Parâmetros de sessão — sem slot dedicado; toca SPEC-008 (Scheduler), SPEC-009 (Cognitive State) | K-001 · G-001 |
| E2 | **Agente estrutural** verifica estrutura de ondas; observa, marca, trata evidência, forma hipótese e **convicção**; entrega análise+convicção | Agente estrutural | SPEC-010 (Structural/Elliott) · CHM-001 (hipótese PRIMARY, Q-005) · CEM-001 (evidência) · SPEC-011 (Fibonacci/Fractal) | J-001 (convicção) |
| E3 | Se há oportunidade, **dispara agente institucional**, que faz o mesmo | Agente institucional | SPEC-012 (Institutional/SMC) · sub-hipótese com `parent_id` (Q-005) | — |
| E4 | **Manager** forma **convicção macro de contexto**; se conclusiva, adiciona **alarme-gatilho** em nível de preço, ativável após a Killzone | Manager/contexto | SPEC-014 (Synthesis) e/ou SPEC-023/024 (Orchestrator/Meta-Cognitive Supervisor) · Conviction Engine SEPARADO (B-001 fechada: Fusion→Conviction→Synthesis) | J-001 · M-001 · K-001 |
| E5 | Se ativado, **agente operacional** analisa o **timeframe de entrada** (difere do de contexto); trata e entrega ao manager | Agente operacional | SPEC-013 (Execution/ICT) — **INVARIANTE: ICT NÃO cria hipótese** (AGENTS.md §6.2), só executa/confirma entrada | — |
| E6 | Manager forma **convicção global** e decide envio com **dados de risco-retorno** ao **agente de risco** | Manager + Risk Agent | SPEC-014 (Synthesis→Decisão) · Conviction Vector 8D · Risk Agent (BL-018) | J-001 · RISK-CONV-001 |
| E7 | **Agente de risco** analisa e decide se **envia sinal** ao **bot finance externo** com dados de entrada | Risk Agent | RISK-SPEC-* (BL-018) · **Signal Package** para o Bot Trade Finance (AGENTS.md §9) · TMP = artefato interno Synthesis→Risk (EUA-E19a) | RISK-ARR-LOC-001 · RISK-CONV-001 · SPEC-045-RUNTIME-001 |

## 3. Pontos de atenção / tensões com o baseline (a tratar na abertura, não aqui) `[INFERÊNCIA]`/`[DECISÃO NECESSÁRIA]`

1. **Hierarquia analítica.** O fluxo E2→E3→E5 (estrutural→institucional→operacional/ICT) é **coerente** com a hierarquia inviolável Elliott→Fibonacci→Fractal→SMC→ICT (AGENTS.md §6.1) e com "ICT não cria hipótese" (§6.2). `[INFERÊNCIA]` — a confirmar por Spec.
2. **"Convicção" em múltiplos níveis** (estrutural E2, macro de contexto E4, global E6). O baseline tem **um** Conviction Vector 8D com fórmula/pesos/limiares **abertos (J-001)** e a distinção "convicção de risco" vs Conviction Vector é **RISK-CONV-001 (aberta)**. Se o workflow implica convicções distintas por camada, isso é **`[DECISÃO NECESSÁRIA]`** — não resolver aqui; alimenta o Dossiê de SPEC-003/014/RISK-SPEC.
3. **Manager como formador de convicção e decisor de envio.** Toca a fronteira Synthesis→Decisão e o papel de orquestração (SPEC-014/023/024). A separação Conviction Engine × Synthesis (B-001 FECHADA: Fusion→Conviction→Synthesis) deve ser respeitada. `[INFERÊNCIA]`.
4. **"Decidirá se envia sinal ou não ao bot finance externo".** Consistente com AGENTS.md §9: **o SOT produz um Signal Package**; a execução da ordem é do Bot Trade Finance externo. O SOT **não executa ordem** (INV-05). A decisão do Risk Agent é de **emitir/não-emitir sinal**, não de executar. `[FATO]` (âncora: AGENTS.md §9; EUA-E19a).
5. **Alarme-gatilho em nível de preço, ativável após a Killzone.** Mecanismo de runtime (armar/observar/ativar) — pertence a **K-001 / SPEC-018 (governança de runtime) / SPEC-045-RUNTIME-001** e a SPEC-008 (Scheduler). Não especificado hoje (§22 do ROADMAP). `[DECISÃO NECESSÁRIA]`.
6. **Timeframe de contexto ≠ timeframe de entrada** (E4 vs E5). Coerente com herança fractal/multi-timeframe (SPEC-009/010/011). `[INFERÊNCIA]`.
7. **Localização do agente de risco / arranjo (D-ARR-001) permanece RISK-ARR-LOC-001 (aberta).** O workflow não a fecha. `[DECISÃO NECESSÁRIA]`.

## 4. Uso obrigatório deste insumo (vínculo com a EUA-E23 / RULE-ECC-06) `[PROPOSTA→homologação]`

Após homologação da EUA-E23, este documento é **leitura obrigatória do Dossiê de Pesquisa** (RULE-ECC-02) de qualquer Spec cuja abertura:

- abra ou toque **K-001**, **SPEC-018** (Learning & Knowledge Formation Governance) ou **SPEC-045-RUNTIME-001**; ou
- especifique um **agente operacional**, um **agente manager/contexto/orquestrador** (SPEC-014/023/024) ou o **agente de risco** (RISK-SPEC-*, BL-018).

O Dossiê dessas Specs **DEVE** citar este insumo, confrontar a proposta de Andraus com o estado da arte pesquisado (lente arquitetural + lentes de domínio da RULE-ECC-05) e registrar, por etapa E1–E7, uma decisão **adotar / adaptar / rejeitar / adiar** — **sem** fechar nenhuma decisão aberta (CONS-01). Este insumo **não vincula o conteúdo** da Spec; vincula a **obrigação de considerá-lo**.

## 5. O que este documento NÃO faz `[FONTE]`

- Não fecha K-001, SPEC-018, SPEC-045-RUNTIME-001, RISK-CONV-001, RISK-ARR-LOC-001, J-001, G-001, H-001, M-001, N-001, C-001.
- Não redefine modelo canônico baselined (CONST-01): CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR intocados.
- Não altera a hierarquia analítica, R:R 1:3, convicção ≥70% / score ≥7/9, Conviction Vector 8D, Signal Package, INV-05.
- Não é ordem de implementação nem autorização de abertura de Spec — a abertura segue RULE-ECC-01/02 (passo 1-bis do ROADMAP §23).

---

*Insumo registrado pelo Especificador (Claude Code), 2026-09-29, a partir de diretiva de Andraus em chat. Não-normativo; sujeito à homologação da EUA-E23 para adquirir o vínculo de leitura obrigatória da §4. Nenhum registro anterior removido (INV-07).*
