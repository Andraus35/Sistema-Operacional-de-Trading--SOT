# DHR-EUA-E24 — Ata de Homologação: criação do `/WORKFLOW.md` na raiz (4º documento de leitura obrigatória) unificando o conteúdo do RUNTIME-WORKFLOW-001

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E24** |
| Objeto | Homologação da emenda **EUA-E24** (`governance/EUA-E24_WORKFLOW_Raiz_Orquestracao_Cognitiva_PROPOSTA.md` + `governance/EUA-E24_ANEXO_A_WORKFLOW_conteudo_proposto.md`) — criação de **`/WORKFLOW.md`** na raiz como **4º documento de leitura obrigatória** (núcleo sempre-obrigatório), **unificando e absorvendo o conteúdo integral** do insumo `RUNTIME-WORKFLOW-001` (v1→v4); emenda ao whitelist de raiz do HOD-001 (§2/§3/§6b.1) |
| Natureza | Emenda **de organização documental + método de leitura** — aditiva; não cria RULE nova, não redefine canônico, não fecha decisão aberta |
| Compatibilidade | **Minor** (aditiva; nenhum documento removido, nenhuma norma reescrita, nenhum identificador reutilizado — INV-07/INV-09; nenhuma decisão aberta fechada — CONS-01) |
| Data | 2026-09-29 |
| Vigência | **Imediata.** `/WORKFLOW.md` passa a ser leitura obrigatória (núcleo sempre-obrigatório) de todo agente a partir desta homologação. |
| Status | **HOMOLOGADA — BASELINE** |

---

## 1. Fluxo de autoridade (RULE-HG-01 / RULE-HG-08; GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (chat, 2026-09-29) ........... ✅ "CRIAR O WORKFLOW.MD NA RAIZ DO REPO EM PÉ DE
                                                               IGUALDADE HIERÁRQUICA QUE AGENTS.MD..." + "Emendar o HOD-001"
Etapa 2 — Formalização (EUA-E24 v1 + Anexo A) .............. ✅ Especificador — NADA aplicado a baseline
Etapa 3 — Parecer do Revisor .............................. ✅ CONFORME condicional (0 achados Crítico/Médio;
                                                               1 Menor F-01 — LICENSE ausente da tabela §3 do HOD-001,
                                                               pré-existente, a corrigir na aplicação)
Etapa 4 — Consenso de Andraus (Q1–Q6) ..................... ✅ 2026-09-29 (ver §2 — Q1 e Q6 MODIFICADOS)
Etapa 5 — Registro Oficial / aplicação .................... ✅ EFETIVADO — esta ata + edições de baseline (§4),
                                                               incl. criação física de /WORKFLOW.md unificado (Q6) e
                                                               correção do F-01 do Revisor
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME (condicional) + consenso do Usuário + registro pelo Controlador. **Ordem respeitada: nada foi aplicado antes do parecer e da homologação.**

## 2. Decisões de Andraus (Q1–Q6)

| # | Questão | Decisão registrada |
|---|---|---|
| **Q1** | Criar `/WORKFLOW.md` na raiz como 4º documento de leitura obrigatória, com o conteúdo do Anexo A? | **SIM, MODIFICADO** (ênfase reforçada para o Especificador na "first spec" — ver verbatim abaixo) |
| **Q2** | Emendar o HOD-001 §6b.1 (e espelhos §2/§3) acrescentando `WORKFLOW.md` ao whitelist de raiz? | **SIM** (+ correção do F-01: reconciliar LICENSE nas três listas) |
| **Q3** | `WORKFLOW.md` é núcleo sempre-obrigatório (igualdade plena) ou entra no dial GES/EUA-E19? | **SIM — núcleo sempre-obrigatório** (lido em toda sessão, independente do dial de complexidade) |
| **Q4** | Atualizar `sincronizado-até` de ambos os agentes → DHR-EUA-E24? | **SIM** |
| **Q5** | Confirmar o código EUA-E24? | **SIM** |
| **Q6** | O `RUNTIME-WORKFLOW-001` permanece como insumo verbatim/histórico separado (síntese só aponta pra ele)? | **MODIFICADO — "INTEGRAR E UNIFICAR EM WORKFLOW.MD"** (ver verbatim abaixo) |

### Q1 — decisão verbatim de Andraus (2026-09-29) `[FONTE]`

> "SIM E PRINCIPALMENTE PARA O ESPECIFICADOR NESSA PRIMEIRA FASE DE FIRST SPEC"

**Leitura registrada (RULE-MET-01 — sem inferir além do dito).** A leitura de `/WORKFLOW.md` é **obrigatória para todo agente** (Q1 = SIM), mas tem **prioridade/peso reforçado especificamente para o Especificador na abertura da SPEC-002** (a "first spec" — primeira Spec de domínio desta fase, retomada da Trilha B conforme ROADMAP). Registrado textualmente em `.claude/agents/especificador.md`: na abertura da SPEC-002 e Specs de domínio subsequentes, a leitura de `/WORKFLOW.md` é **passo obrigatório reforçado do Dossiê de Pesquisa** (ligado à RULE-ECC-06), não apenas mais uma fonte de contexto geral.

### Q6 — decisão verbatim de Andraus (2026-09-29) `[FONTE]`

> "INTEGRAR E UNIFICAR EM WORKFLOW.MD"

**Leitura registrada (RULE-MET-01).** Andraus **NÃO** quis manter `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` como o insumo verbatim separado, com `/WORKFLOW.md` sendo apenas uma síntese-que-aponta-para-ele (como o Anexo A originalmente propôs). Andraus quis o **conteúdo integral unificado dentro do `/WORKFLOW.md`**: os 4 blocos verbatim (v1, v2, v3-tabela de timeframes, v4-decisões RISK-LEV-001/RUNTIME-TF-PAIR-001), a decomposição E1–E8 completa, a tabela de pares de timeframe (D1→H1, H4→M15, H1→M5, extensível), as referências aos 5 schemas `runtime-workflow.*.json`, a lista de decisões abertas correlatas — tudo movido/consolidado para dentro do `/WORKFLOW.md` na raiz. Consequentemente: (a) `RUNTIME-WORKFLOW-001` é marcado **SUPERSEDIDO** (banner no topo), preservado em `governance/` como registro histórico do processo de elaboração (INV-07 — não deletado, mantém valor de auditoria; é citado em DHR-EUA-E23 como fonte da RULE-ECC-06); (b) o **Anexo A** da EUA-E24 é marcado SUPERSEDIDO (o `/WORKFLOW.md` real vai além da síntese que ele propunha); (c) a referência da **RULE-ECC-06** (em `RULES.md` e `atomic-spec.md` §15) é atualizada para apontar `/WORKFLOW.md` como fonte vigente — correção consequente, não reabertura da RULE-ECC-06.

## 3. Objeto homologado

- **`/WORKFLOW.md`** (raiz): documento único e canônico da orquestração cognitiva do SOT em runtime, **não-normativo e descritivo**, **núcleo sempre-obrigatório** de leitura por todo agente (4º pilar, ao lado de ROADMAP/atomic-spec/AGENTS). Unifica e absorve integralmente o conteúdo do `RUNTIME-WORKFLOW-001` (v1→v4): histórico verbatim das diretivas de Andraus, decomposição E1–E8, tabela de 3 pares de timeframe (extensível), 5 schemas `runtime-workflow.*` (PROPOSTA), tensões com o baseline, decisões abertas. Herda o status não-normativo e **todas** as decisões abertas do insumo; NÃO fecha decisão aberta (CONS-01), NÃO redefine canônico (CONST-01). Fonte de verdade dos invariantes = `AGENTS.md` §6.
- **Emenda ao HOD-001** (§2 taxonomia, §3 tabela "Caminho-quente (raiz)", §6b.1 whitelist): o whitelist de documentos `.md` da raiz passa de 6 para 7 — `AGENTS.md · atomic-spec.md · ROADMAP.md · WORKFLOW.md · GLOSSARIO.md · README.md · LICENSE` — **idêntico nos três pontos** (F-01 do Revisor reconciliado: LICENSE, que faltava só na tabela §3, agora presente nas três listas). RPIR, sensor RCH-001 passo 8 e detecção determinística §6b.5 permanecem íntegros — apenas o conjunto permitido foi ampliado.
- **Ênfase de leitura reforçada** (Q1): para o Especificador, na abertura da SPEC-002 e Specs de domínio subsequentes, a leitura de `/WORKFLOW.md` é passo obrigatório reforçado do Dossiê (RULE-ECC-06), registrado em `.claude/agents/especificador.md`.

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração | Estado |
|---|---|---|
| **`WORKFLOW.md`** *(novo — raiz)* | **Criado** com o conteúdo unificado (absorve integralmente RUNTIME-WORKFLOW-001 v1→v4 + decomposição E1–E8 + tabela de pares + 5 schemas + decisões abertas), conforme Q6. Cabeçalho declara status não-normativo, decisões abertas herdadas, delimitação dos 4 pilares, ênfase Q1 | ✅ aplicado |
| `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` | Banner **SUPERSEDIDO** no topo (conteúdo integrado/unificado em /WORKFLOW.md); corpo intocado (v1→v4 preservadas — INV-07); permanece em `governance/` por valor de auditoria | ✅ aplicado |
| `governance/EUA-E24_ANEXO_A_WORKFLOW_conteudo_proposto.md` | Banner **SUPERSEDIDO** no topo (Q6: /WORKFLOW.md real vai além da síntese proposta); corpo intocado (INV-07) | ✅ aplicado |
| `governance/EUA-E24_..._PROPOSTA.md` | Emenda homologada (registrada nesta ata e no CATALOGO); corpo da proposta preservado | ✅ registrado |
| `governance/HOD-001_..._PROPOSTA.md` | §2 (taxonomia), §3 (tabela — +WORKFLOW e **+LICENSE**, F-01), §6b.1 (whitelist Docs 6→7) — três listas idênticas | ✅ aplicado |
| `AGENTS.md` | §1 (linha `WORKFLOW.md` na tabela de leitura obrigatória + nota "núcleo sempre-obrigatório" e ênfase SPEC-002) + §2 (árvore ASCII da raiz +WORKFLOW.md) | ✅ aplicado |
| `governance/RULES.md` | RULE-ECC-06: referência atualizada de `RUNTIME-WORKFLOW-001` → `/WORKFLOW.md` (fonte vigente); nota do histórico superseded; `[Fonte: +DHR-EUA-E24]` | ✅ aplicado |
| `atomic-spec.md` | §15 (Insumo de orquestração): referência atualizada → `/WORKFLOW.md`; ênfase Q1 (passo reforçado SPEC-002); nota do histórico superseded | ✅ aplicado |
| `.claude/agents/especificador.md` | `sincronizado-até` → DHR-EUA-E24; `required_sources` (+WORKFLOW.md, +DHR-EUA-E24); WORKFLOW.md no núcleo sempre-obrigatório (§4 item 1) com ênfase Q1 textual | ✅ aplicado |
| `.claude/agents/revisor.md` | `sincronizado-até` → DHR-EUA-E24; `required_sources` (+WORKFLOW.md, +DHR-EUA-E24); nota da emenda no carimbo | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E24 (emendas) + linha `/WORKFLOW.md` (documento de raiz) + linha RUNTIME-WORKFLOW-001 atualizada para SUPERSEDIDO/histórico + linha DHR-EUA-E24 (atas) | ✅ aplicado |
| `docs/mapa/` (BL-019/R-MAPA) | Regenerar via `python scripts/build_map.py` após criar `/WORKFLOW.md` (não editar à mão). **Pendência de execução** — Especificador não tem Bash (reportado ao coordenador) | ⏳ pendente |

## 5. NÃO aplicado / NÃO tocado (deliberadamente)

- **Nenhuma Spec homologada** (SPEC-001/019/020/021) reescrita ou reaberta.
- **Nenhuma decisão aberta fechada** (CONS-01): J-001, G-001, H-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001, RISK-LEV-001, RUNTIME-TF-PAIR-EXT-001, D-RISK-SP-001, ECC-VAL-001, ECC-03-001, RULE-REG-001, SPEC-020-PRINC-001 — todas permanecem abertas. **RULE-ECC-03 permanece RESERVADA.**
- **RULE-ECC-06 não é reaberta nem alterada em mérito** — apenas sua **referência de fonte** é atualizada (RUNTIME-WORKFLOW-001 → /WORKFLOW.md), correção consequente à decisão Q6 de Andraus.
- **Os 5 schemas `runtime-workflow.*.json`** permanecem `[PROPOSTA]` não-normativa (não homologados por esta ata).
- **Nenhuma RULE nova** criada (organização documental; não incide RULE-REG-001 nem o piloto SPEC-002).
- **RPIR / sensor RCH-001 passo 8 / detecção §6b.5 / whitelist de config-dotfiles** do HOD-001 intocados — apenas o conjunto de docs `.md` permitidos na raiz foi ampliado de 6 para 7.

## 6. Invariantes preservados

- **CONS-01:** nenhuma decisão aberta fechada; nenhuma nova aberta por esta emenda.
- **INV-07:** **nada deletado.** `RUNTIME-WORKFLOW-001` preservado integralmente em `governance/` com banner de superseded (não movido para `docs/_legacy/` por valor de auditoria/rastreabilidade — é fonte citada da RULE-ECC-06); Anexo A da EUA-E24 preservado com banner; nenhuma versão (v1→v4) apagada.
- **INV-09:** nenhuma norma reescrita — o whitelist do HOD-001 foi **ampliado** (aditivo), não reescrito; a RULE-ECC-06 teve só a referência de fonte atualizada, não o mérito.
- **CONST-01:** nenhum modelo canônico baselined redefinido (CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR).
- **Hierarquia analítica, R:R 1:3, convicção ≥70%/score ≥7/9, Conviction Vector 8D, Signal Package, INV-05:** intocados. `/WORKFLOW.md` os cita como fonte de verdade `AGENTS.md` §6, não os redefine.
- **ENF-03:** `revisor.md` continua sem Write/Edit e sem acesso web.
- **RPSA (EUA-E16):** `sincronizado-até` de ambos os agentes → **DHR-EUA-E24** (Q4).
- **RULE-MET-01:** nenhuma afirmação fabricada; validação de sintaxe dos schemas e regeneração do mapa não executadas (Especificador sem Bash) — reportadas como pendência, não como fato concluído.

## 7. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultar `backlog/RMR-001_Painel_Backlog.md` — a confirmar pelo coordenador via `python scripts/backlog_triggers.py` se algum item é disparado por esta homologação.
2. **Próximo trabalho autorizado:** SPEC-002 — 1ª Spec de domínio da fase (Trilha B), sob RULE-ECC-05/06, com `/WORKFLOW.md` como leitura reforçada do Dossiê (Q1).
3. **Pendências de validação (o Especificador não tem Bash — para o coordenador rodar):** `python scripts/build_map.py` + `--check` (mapa BL-019, obrigatório após criar /WORKFLOW.md); `python scripts/check_refs.py` (integridade de referências, incl. as novas para /WORKFLOW.md e as atualizadas de RUNTIME-WORKFLOW-001); `python scripts/check_doc_sync.py` (drift do whitelist em 3 pontos); `python scripts/backlog_triggers.py`. Validação de sintaxe dos 5 schemas `runtime-workflow.*` permanece pendência anterior (não desta emenda).

---

*Ata registrada pelo Controlador (Claude Code) a partir da homologação de Andraus (Decisor Final), 2026-09-29, comunicada em chat — a decisão é de Andraus; este registro não a substitui. Parecer do Revisor: CONFORME condicional (0 Crítico/Médio, 1 Menor F-01 corrigido na aplicação). Q1 e Q6 MODIFICADOS por Andraus (ênfase SPEC-002; unificação total em /WORKFLOW.md). Nenhum registro anterior removido — apenas aditado; RUNTIME-WORKFLOW-001 e Anexo A preservados com banner (INV-07/INV-09).*
