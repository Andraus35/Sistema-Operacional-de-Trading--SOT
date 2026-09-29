> **SUPERSEDIDO pela decisão de Andraus (Q6 — "INTEGRAR E UNIFICAR EM WORKFLOW.MD", DHR-EUA-E24, 2026-09-29):** o `/WORKFLOW.md` efetivamente criado **unifica também** o conteúdo integral de `RUNTIME-WORKFLOW-001` (v1→v4, decomposição E1–E8, tabela de pares, 5 schemas, decisões abertas), indo **além** desta proposta de síntese-que-aponta-para-o-insumo. Ver `/WORKFLOW.md` (raiz) para o conteúdo vigente. Este anexo é preservado como registro do processo (INV-07 — não deletado).

# EUA-E24 — Anexo A: conteúdo proposto de `/WORKFLOW.md`

> **STATUS DESTE ARQUIVO:** `[PROPOSTA]` — anexo da emenda `EUA-E24`. O texto abaixo (da linha `================ INÍCIO DO CONTEÚDO DE /WORKFLOW.md ================` em diante) é o **conteúdo integral proposto** para o futuro `/WORKFLOW.md` na raiz. **Nada é promovido para a raiz até a homologação da EUA-E24** (Q1/Q2/Q5). Enquanto não homologado, este anexo vive em `governance/` (não viola o whitelist HOD-001 §6b.1, pois não está na raiz). Na Etapa 5 da EUA-E24, o bloco abaixo é copiado para `/WORKFLOW.md` (sem esta cabeça de anexo).

---

================ INÍCIO DO CONTEÚDO DE /WORKFLOW.md ================

# WORKFLOW.md — Orquestração Cognitiva do SOT em Runtime (síntese canônica)

> Documento de raiz, **leitura obrigatória** por todo agente (ao lado de `ROADMAP.md`, `atomic-spec.md` e `AGENTS.md`).
> Descreve **como os agentes cognitivos já especificados operam juntos** durante uma sessão de trading ao vivo (runtime cognitivo).
> É o **4º pilar** de leitura: `ROADMAP.md` fixa a SEQUÊNCIA de Specs · `atomic-spec.md` fixa o MÉTODO de produzir Specs · `AGENTS.md` fixa IDENTIDADE/CONFIG · **`WORKFLOW.md` fixa a ORQUESTRAÇÃO COGNITIVA em runtime**.

## 0. Status e natureza deste documento `[FATO]`

- **Não-normativo e descritivo.** Este documento **descreve** a orquestração vigente; **não** cria invariante, **não** fecha decisão aberta, **não** redefine modelo canônico. Ele **herda o status não-normativo** e **todas as decisões abertas** da sua fonte, o insumo `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md`.
- **"Runtime" = orquestração cognitiva do Harness**, não runtime de software. O SOT está em fase spec-first (`AGENTS.md` §1). "Runtime" aqui é a **sequência de acionamento e troca de evidência/hipótese/convicção entre os agentes LLM especificados** quando o SOT estiver operando numa sessão ao vivo. Não se infere daqui arquitetura de código, infraestrutura ou execução técnica (`RUNTIME-WORKFLOW-001` §0-bis).
- **Fonte de verdade dos invariantes = `AGENTS.md` §6.** Onde este documento menciona hierarquia analítica, R:R, convicção ou Signal Package, ele **remete** ao `AGENTS.md` §6 — **não** os redefine.
- **Trilha histórica/verbatim = `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md`** (v1→v4). Esta é uma **síntese legível**, não a cópia verbatim das versões. O registro completo de como o workflow evoluiu (diretivas verbatim de Andraus, diferenças v1→v2→v3→v4, decomposição, tensões, schemas) vive **lá** — não é duplicado aqui (INV-07: nada foi apagado; o insumo permanece).
- **Vínculo com a RULE-ECC-06 (EUA-E23):** para Specs de K-001/SPEC-018/SPEC-045-RUNTIME-001 ou de agente operacional/manager/risco, o **Dossiê de Pesquisa** deve considerar o `RUNTIME-WORKFLOW-001` decisão-a-decisão por etapa (E1–E8). Este `WORKFLOW.md` é a **orientação geral de leitura**; **não substitui** aquela obrigação de Dossiê.

## 1. Parâmetros de missão (o operador arma o sistema antes da Killzone) `[FONTE]`

O operador (Andraus) arma o sistema antes da abertura da Killzone e aponta:
- **ativo alvo** (BTC / XAU / NASDAQ — enum `BTCUSDT / XAUUSD / NAS100`);
- **tipo de missão:** exploração ou validação;
- **tipo de trade:** position / swing / day (implica na alavancagem conforme convicção + tipo de oportunidade — a **regra de derivação convicção→alavancagem NÃO está especificada**: `[DECISÃO NECESSÁRIA]` **RISK-LEV-001**, mérito adiado à Spec do agente de risco, RISK-SPEC-*/BL-018);
- **par de timeframes** (contexto ↔ entrada) — ver §3.

## 2. O fluxo de 8 etapas (E1–E8) `[FONTE]` (paráfrase) / `[INFERÊNCIA]` (mapeamento a slots)

Consolidado da decomposição v4 do `RUNTIME-WORKFLOW-001` (§2-bis). A coluna "slot" é **indicativa** (`[INFERÊNCIA]`); a coluna "depende de" lista decisões abertas que a governam (`[DECISÃO NECESSÁRIA]`, não fechadas aqui).

| # | Etapa | Ator | Slot indicativo | Depende de (aberta) |
|---|---|---|---|---|
| **E1** | Operador arma o sistema; aponta ativo, tipo de missão, tipo de trade, par de timeframes. Alavancagem = **implicação**, não input. | Operador | SPEC-008/009 | K-001 · G-001 · **RISK-LEV-001** |
| **E2** | **Manager distribui a missão** ao agente estrutural. | Manager | SPEC-014/023 | K-001 |
| **E3** | **Agente estrutural** verifica estrutura de ondas no TF de **contexto E de entrada**; observa, marca, classifica, trata evidência+hipótese, forma convicção; entrega. | Estrutural | SPEC-010 · SPEC-011 · CHM-001 · CEM-001 | J-001 |
| **E4** | Se há oportunidade (conforme convicção especializada), **agente institucional** faz o mesmo **apenas no TF de contexto**. | Institucional | SPEC-012 · sub-hipótese `parent_id` | J-001 |
| **E5** | **Manager** forma **convicção macro de contexto**; se conclusiva, adiciona **alarme-gatilho** em nível de preço, ativável após a Killzone **ou em outro momento**. | Manager | SPEC-014/023 · Conviction Engine (B-001 fechada: Fusion→Conviction→Synthesis) · SPEC-008 | J-001 · M-001 · K-001 |
| **E6** | Se o alarme é **ativado E válido**, **agente operacional** analisa o **TF de entrada** (difere do de contexto); trata e entrega. **ICT NÃO cria hipótese** (`AGENTS.md` §6.2) — só executa/confirma. | Operacional | SPEC-013 (ICT) | — |
| **E7** | **Manager** forma **convicção global** e decide envio ao Risk Agent com **dados da oportunidade** (não risco-retorno pré-calculado). | Manager | SPEC-014 · TMP (artefato interno Synthesis→Risk, EUA-E19a) | J-001 · RISK-CONV-001 |
| **E8** | **Agente de risco** faz **sua própria análise de risco-retorno** e decide **por convicção** se envia o **Signal Package** ao **bot finance externo**. O SOT **não executa ordem** (INV-05). | Risk Agent | RISK-SPEC-* (BL-018) · Signal Package | RISK-ARR-LOC-001 · RISK-CONV-001 · SPEC-045-RUNTIME-001 |

**Hierarquia analítica preservada:** o encadeamento E3→E4→E6 (estrutural → institucional → operacional/ICT) é coerente com a hierarquia inviolável **Elliott → Fibonacci → Fractal → SMC → ICT** (`AGENTS.md` §6.1) e com "ICT não cria hipótese" (§6.2). Camada inferior não sobrepõe superior.

**Convicção em camadas — atenção.** O fluxo menciona convicção em vários momentos (estrutural E3, macro de contexto E5, global E7, de risco E8). O baseline tem **um** Conviction Vector 8D com fórmula/pesos/limiares **abertos (J-001)**, e a distinção "convicção de risco" vs. Conviction Vector é **RISK-CONV-001 (aberta)**. Se o workflow implica convicções distintas por camada, isso é **`[DECISÃO NECESSÁRIA]`** — **não** resolvido aqui; matéria de Dossiê das Specs correspondentes.

## 3. Pareamento de timeframes contexto ↔ entrada (3 pares, extensível) `[FONTE]`

O TF de **contexto** (análise estrutural E3 + institucional E4) e o TF de **entrada** (confluência multi-timeframe + operacional E6) são acoplados em **3 pares fixos** (não produto cartesiano):

| Par | Macro (contexto) | Micro (entrada) |
|---|---|---|
| 1 | **D1** | **H1** |
| 2 | **H4** | **M15** |
| 3 | **H1** | **M5** |

- O H1 aparece em **dois papéis** (contexto no Par 3, entrada no Par 1) — usos distintos do mesmo TF, **não** contradição nem par adicional.
- O conjunto é **extensível** (RUNTIME-TF-PAIR-001, resolvida por Andraus: "conjunto inicial extensível"). Novos pares entram por **versionamento futuro** de schema/documento — **não** significa aceitar qualquer combinação hoje (os schemas codificam **literalmente os 3 pares**). O **processo de extensão** (quando/como) permanece `[DECISÃO NECESSÁRIA]` **RUNTIME-TF-PAIR-EXT-001** (só Andraus cunha).
- **Lacuna registrada (não resolvida):** os schemas de 1ª geração (`elliott-wave.*`, `smc.*`, `ict.*`, `synthesis.*`) usam S1/D1/H4/H1/M5 — **sem M15** e **com S1** (que a tabela de Andraus não cita). Reconciliar o conjunto de TFs entre 1ª geração e `runtime-workflow.*` é `[DECISÃO NECESSÁRIA]` para a abertura das Specs SPEC-010/011/012/013/014 (`RUNTIME-WORKFLOW-001` §1-ter).

## 4. Contrato de dados — schemas de referência `[PROPOSTA]`

Os 5 JSON Schemas (Draft-07) que modelam o workflow como contratos de dados entre os agentes cognitivos são **`[PROPOSTA]` — não homologados** (aguardam Revisor + Andraus; não fecham decisão aberta; não redefinem canônico):

| Schema | Etapa(s) | Cobre |
|---|---|---|
| `schemas/runtime-workflow.mission-dispatch.json` | E1, E2 | Parâmetros de missão + distribuição pelo Manager; par contexto/entrada por `oneOf` de 3 pares. |
| `schemas/runtime-workflow.conviction-report.json` | E3, E4, E6 | Entrega de convicção por agente especializado; `hypothesis_ref=null` para ICT (invariante). |
| `schemas/runtime-workflow.alarm-trigger.json` | E5 | Alarme-gatilho: nível de preço, condição, janela de ativação, status. |
| `schemas/runtime-workflow.manager-conviction-envelope.json` | E5, E7 | Convicção macro de contexto vs. global + "dados da oportunidade" ao Risk Agent. |
| `schemas/runtime-workflow.risk-decision.json` | E8 | Saída do Risk Agent: análise risco-retorno, convicção de risco, decisão, enviar/não sinal. |

## 5. Decisões abertas que este documento NÃO fecha (CONS-01) `[DECISÃO NECESSÁRIA]`

`J-001` (fórmula/pesos/limiares definitivos da convicção) · `G-001` · `H-001` · `K-001` · `C-001` · `M-001` · `N-001` · `SPEC-045-RUNTIME-001` · `RISK-ARR-LOC-001` · `RISK-CONV-001` · `RISK-LEV-001` (mérito adiado à Spec de risco) · `RUNTIME-TF-PAIR-EXT-001` (processo de extensão dos pares). A separação Conviction Engine × Synthesis é **B-001 (FECHADA:** Fusion→Conviction→Synthesis). Nenhuma leitura deste documento pode tratar qualquer item acima como fechado.

## 6. O que este documento NÃO faz `[FONTE]`

- **Não define a sequência de Specs** — isso é só o `ROADMAP.md`.
- **Não define o método de produzir Specs** (BASpec, D0–D9, Enforcement Contract, etiquetagem) — isso é só o `atomic-spec.md`.
- **Não redefine identidade/config, papéis, profiles nem os não-negociáveis constitucionais** — isso é só o `AGENTS.md` (§6 é a fonte de verdade dos invariantes).
- **Não fecha decisão aberta** (CONS-01) **nem redefine canônico** (CONST-01).
- **Não substitui** o insumo `RUNTIME-WORKFLOW-001` nem a obrigação de Dossiê da RULE-ECC-06 — é síntese de orientação, complementar.

## 7. Referências

`AGENTS.md` (§1 leitura obrigatória; §6 invariantes; §9 Signal Package/INV-05) · `ROADMAP.md` · `atomic-spec.md` · `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` (fonte verbatim; §0-bis; §1-ter; §1-quater; §2-bis; §6) · `governance/EUA-E23_Lentes_Dominio_Dossie_Pesquisa_PROPOSTA.md` (RULE-ECC-05/06) · `governance/EUA-E24_WORKFLOW_Raiz_Orquestracao_Cognitiva_PROPOSTA.md` (emenda que criou este documento) · `schemas/runtime-workflow.*.json` (5 schemas, PROPOSTA) · `canon/CHM-001` (hipótese) · `canon/CEM-001` (evidência) · `canon/CEE-001` v2.0 (economia/4Es/salvaguardas).

---

*Síntese canônica não-normativa da orquestração cognitiva do SOT. Criado pela EUA-E24 (2026-09-29). Herda o status não-normativo e as decisões abertas do insumo `RUNTIME-WORKFLOW-001` (v4). Trilha verbatim/histórica preservada nesse insumo (INV-07). Fonte de verdade dos invariantes = `AGENTS.md` §6.*

================ FIM DO CONTEÚDO DE /WORKFLOW.md ================
