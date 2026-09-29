# DHR-EUA-E23 — Ata de Homologação: Lentes de domínio obrigatórias no Dossiê de Pesquisa (6 lentes) + insumo de orquestração cognitiva (RUNTIME-WORKFLOW-001)

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E23** |
| Objeto | Homologação da emenda **EUA-E23** (`governance/EUA-E23_Lentes_Dominio_Dossie_Pesquisa_PROPOSTA.md`) — **RULE-ECC-05** (lentes de domínio obrigatórias no Dossiê de Pesquisa, com proporcionalidade e fail-closed seletivo) e **RULE-ECC-06** (`RUNTIME-WORKFLOW-001` como insumo obrigatório de leitura do Dossiê) |
| Natureza | Emenda **normativa de método** — amplia o conteúdo mínimo do Dossiê de Pesquisa (RULE-ECC-02 / `atomic-spec.md` §15). **Nenhuma Spec homologada é reescrita.** |
| Compatibilidade | **Minor** (aditiva; nenhum objeto removido, nenhum identificador reutilizado — INV-07) |
| Data | 2026-09-29 |
| Vigência | **Imediata.** Prospectiva — incide a partir de **SPEC-002**; não retroage sobre SPEC-020/021/046. |
| Status | **HOMOLOGADA — BASELINE** |

---

## 1. Fluxo de autoridade (RULE-HG-01 / RULE-HG-08; GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (chat, 2026-09-29) ........... ✅ pesquisa que guia a especificação só usa a lente arquitetural; Andraus quer também o workflow dele + estado da arte do Trading (Elliott/SMC/ICT/risco-retorno)
Etapa 2 — Formalização (EUA-E23 v1) ........................ ✅ Especificador — NADA aplicado a baseline
Etapa 3 — Parecer do Revisor (v1) .......................... ✅ NÃO CONFORME RECUPERÁVEL (F-01 §7-bis Bloco C incompleto [N8–N17] · F-02 Vínculo normativo sem `[PROPOSTA]` · F-03 I-001 listada como aberta · F-04 RULE-REG-001 ausente da lista de abertas · F-05 referência informal "N3 da EUA-E21"; nenhum Crítico)
Etapa 3b — v2 (F-01..F-05 corrigidos) + revisão focada ..... ✅ CONFORME (Revisor, 2026-09-29)
Etapa 4 — Consenso de Andraus (Q1–Q7) ...................... ✅ 2026-09-29 (ver §2 — Q2 MODIFICADO)
Etapa 5 — Registro Oficial / aplicação ..................... ✅ EFETIVADO — esta ata + edições de baseline (§4) + v3 da EUA-E23 (RULE-ECC-05 = 6 lentes)
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME + consenso do Usuário + registro pelo Controlador. **Ordem respeitada: nada foi aplicado antes do parecer CONFORME e da homologação.**

## 2. Decisões de Andraus (Q1–Q7)

| # | Questão | Decisão registrada |
|---|---|---|
| **Q1** | Adotar RULE-ECC-05 (lentes de domínio obrigatórias no Dossiê, com proporcionalidade e fail-closed seletivo) | **SIM** |
| **Q2** | As 4 lentes propostas (Elliott/Fibonacci · SMC · ICT · risco-retorno) são a decomposição correta, ou separar Elliott de Fibonacci, ou adicionar uma 5ª? | **MODIFICADO — 6 LENTES** (ver verbatim abaixo) |
| **Q3** | Adotar RULE-ECC-06 (RUNTIME-WORKFLOW-001 como insumo obrigatório de leitura) | **SIM** |
| **Q4** | Registrar `RUNTIME-WORKFLOW-001` em `governance/` como insumo não-normativo | **SIM** (fica em `governance/` como está) |
| **Q5** | Incidência prospectiva a partir de SPEC-002 (não retroage sobre SPEC-020/021/046) | **SIM** |
| **Q6** | Distinção "runtime = orquestração cognitiva" registrada como achado, sem forçar equivalência com a leitura técnica de SPEC-045-RUNTIME-001 | **SIM** |
| **Q7** | Confirmar código EUA-E23 e identificadores RULE-ECC-05 / RULE-ECC-06 | **SIM** |

### Q2 — decisão verbatim de Andraus (2026-09-29) `[FONTE]`

> "ORDEM ELLIOTT, FIBONACCI (SEPARADA), SMC, ICT E CONFLUENCE (AQUI SERIA A CONFLUENCIA DENTRO DO CAMPO DE ANALISE DA ESCOLA E NÃO ENTRE AS ESCOLAS) DEMAIS PODE APROVAR"

Esclarecimento sobre a lente de risco-retorno, quando perguntado se ela permanecia (não foi citada na primeira resposta por lapso):

> **Andraus:** "Mantém como 6ª lente"

**Leitura registrada (RULE-MET-01 — sem inferir além do dito).** As lentes passam de 4 para **6**, nesta ordem obrigatória:

1. **Elliott** — estrutura de ondas.
2. **Fibonacci** — **SEPARADA** da Elliott (na v2 eram uma lente combinada).
3. **SMC** — Smart Money Concepts.
4. **ICT** — timing/execução (ICT não cria hipótese — AGENTS.md §6.2).
5. **Confluência** — **INTRA-escola**: convergência de sinais **DENTRO** do campo de análise de uma mesma escola (ex.: múltiplos fibos/graus de onda dentro da própria Elliott/Fibonacci; múltiplos padrões SMC dentro da própria SMC). **NÃO** é a confluência **entre** escolas — esta última já é tratada pela **hierarquia analítica** (Elliott→Fibonacci→Fractal→SMC→ICT) e pela **síntese do Manager/Synthesis**. A distinção é normativa e obrigatória no texto do Dossiê (a confusão entre as duas é achado de coerência do Revisor).
6. **Risco-retorno** — sizing, R:R ≥ 1:3 (invariante), heat/exposição. Confirmada como 6ª lente.

## 3. Objeto homologado

- **RULE-ECC-05:** além da lente arquitetural (RULE-ECC-02 item 3), o Dossiê de qualquer Spec que toque o domínio de trading pesquisa, com **proporcionalidade e fail-closed seletivo**, as **6 lentes de domínio** aplicáveis (ordem acima). Declaração obrigatória em quadro próprio de quais se aplicam/não se aplicam e por quê. Lente declarada aplicável mas não pesquisada = NÃO CONFORME Crítica; declaração ausente = Médio; ausência justificada das 6 lentes (Spec fora do domínio) = correto. Reaproveitada como fundamentação dos `PD-xx` (RULE-PD-01), sem pesquisa duplicada. Salvaguardas DHR-PROV-WEB-001 §2.1 mantidas; nenhuma lente fecha decisão aberta (CONS-01); pesquisa inconclusiva = INDETERMINADO.
- **RULE-ECC-06:** `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` é leitura obrigatória do Dossiê de qualquer Spec que abra/toque K-001, SPEC-018 ou SPEC-045-RUNTIME-001, ou que especifique agente operacional, manager/contexto/orquestrador (SPEC-014/023/024) ou agente de risco (RISK-SPEC-*). Decisão por etapa E1–E7/E8 (adotar/adaptar/rejeitar/adiar), sem fechar decisão aberta (CONS-01). Vincula a obrigação de considerá-lo, não o conteúdo da Spec. Ausência da consideração = Médio; tratar o insumo como decisão fechada = Crítico.

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração (aditiva) | Estado |
|---|---|---|
| `governance/EUA-E23_..._PROPOSTA.md` | Status → HOMOLOGADA; **v3** — RULE-ECC-05 reescrita para 6 lentes (Q2 modificado); todas as menções a "4 lentes" → 6; §9 Etapas 3b/4/5 concluídas; v1/v2 preservadas (INV-07) | ✅ aplicado |
| `atomic-spec.md` | §15: parágrafos "Lentes de domínio (EUA-E23/RULE-ECC-05)" (6 lentes, ordem, proporcionalidade, fail-closed seletivo, desambiguação intra-escola) e "Insumo de orquestração (EUA-E23/RULE-ECC-06)"; nota de versão no rodapé | ✅ aplicado |
| `governance/RULES.md` | **RULE-ECC-05** e **RULE-ECC-06** registradas na seção "Regras de Especificação Emergente" (após RULE-ECC-04), com `[Fonte: DHR-EUA-E23; ...]`. RULE-ECC-03 (RESERVADA) intocada | ✅ aplicado |
| `ROADMAP.md` | Linha "Emenda vigente adicional" EUA-E23 (cabeçalho) + nota no §23 passo 1-bis (6 lentes + insumo de orquestração) | ✅ aplicado |
| `.claude/agents/especificador.md` | §4 item 2 (6 lentes + RUNTIME-WORKFLOW-001) + 2 itens no Autopré-check §7; `sincronizado-até` → DHR-EUA-E23; `required_sources` (+DHR-EUA-E23, +RUNTIME-WORKFLOW-001); `last_sync_catalog_date` → 2026-09-29 | ✅ aplicado |
| `.claude/agents/revisor.md` | Passo 4-bis ampliado (lentes de domínio: aplicável-não-pesquisada = Crítica, declaração ausente = Médio, confusão intra/inter-escola = coerência; insumo de orquestração: ausência = Médio, decisão fechada = Crítico); `sincronizado-até` → DHR-EUA-E23; `required_sources`; `last_sync_catalog_date` → 2026-09-29 | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E23 (emendas) + linha `RUNTIME-WORKFLOW-001` (insumo, não-normativo) + linha DHR-EUA-E23 (atas) | ✅ aplicado |
| `governance/RUNTIME-WORKFLOW-001_Proposta_Andraus.md` | Campo "Vínculo normativo": `[PROPOSTA]`/condicional → **EFETIVO (FATO NORMATIVO — obrigação de leitura)**; texto anterior preservado (INV-07). Restante do documento intocado (v1/v2/v3/v4 preservadas) | ✅ aplicado |

## 5. NÃO aplicado / NÃO tocado (deliberadamente)

- **Nenhuma Spec homologada** (SPEC-001/019/020/021) reescrita ou reaberta.
- **Nenhuma decisão aberta fechada** (CONS-01): J-001, G-001, H-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001, RISK-LEV-001, RUNTIME-TF-PAIR-EXT-001, ECC-VAL-001, ECC-03-001, RULE-REG-001 — todas permanecem abertas. **RULE-ECC-03 permanece RESERVADA.**
- **Os 5 schemas `runtime-workflow.*.json`** permanecem `[PROPOSTA]` não-normativa — a homologação torna obrigatória a **leitura** do `RUNTIME-WORKFLOW-001`, **não** os schemas em si baseline.
- **Ferramental** (`validate_spec_sot.py` check estrutural de "quadro de lentes"; GLOSSARIO) = acompanhamento sugerido (§7 da proposta), exige aprovação própria — não aplicado aqui.
- **RULE-ECC-01/02/03/04, RULE-PD-01/02/03, RULE-MECH** não alterados — apenas estendidos por cobertura aditiva.

## 6. Invariantes preservados

- **CONS-01:** nenhuma decisão aberta fechada; nenhuma nova aberta por esta emenda.
- **INV-07/INV-09:** nada deletado; v1/v2 da EUA-E23 e o texto anterior do "Vínculo normativo" do RUNTIME-WORKFLOW-001 preservados; a pesquisa nunca vira baseline.
- **CONST-01:** nenhum modelo canônico baselined redefinido (CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR).
- **Hierarquia analítica, R:R 1:3, convicção ≥70%/score ≥7/9, Conviction Vector 8D, Signal Package, INV-05:** intocados. A lente (5) Confluência **intra-escola** é distinta da confluência **entre** escolas (hierarquia + síntese) — a distinção protege a hierarquia.
- **ENF-03:** `revisor.md` continua sem Write/Edit e sem acesso web; audita a **coerência** da declaração de lentes, não a veracidade das páginas.
- **RPSA (EUA-E16):** `sincronizado-até` de ambos os agentes → **DHR-EUA-E23**.
- **RULE-MET-01:** riscos residuais da EUA-E23 (§6 da proposta) aceitos — o Revisor não verifica a veracidade das fontes de escola; injeção via web e viés de escola mitigados, não eliminados; a pesquisa é probabilística (só a estrutura do Dossiê é verificável).

## 7. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultar `backlog/RMR-001_Painel_Backlog.md` — nenhum item existente é disparado por esta homologação (a confirmar pelo coordenador via `python scripts/backlog_triggers.py`).
2. **Próximo trabalho autorizado:** SPEC-002 — 1ª Spec sob RULE-ECC-05/06 (Dossiê com as 6 lentes de domínio aplicáveis + insumo de orquestração quando aplicável).
3. **Pendências de validação (o Especificador não tem Bash — para o coordenador rodar):** `python scripts/build_map.py` + `--check` (mapa BL-019); `python scripts/check_refs.py`; `python scripts/check_doc_sync.py`; `python scripts/backlog_triggers.py`.

---

*Ata registrada pelo Controlador (Claude Code) a partir da homologação de Andraus (Decisor Final), 2026-09-29, comunicada em chat — a decisão é de Andraus; este registro não a substitui. Parecer do Revisor: CONFORME (v2). Q2 modificado por Andraus para 6 lentes (Elliott · Fibonacci SEPARADA · SMC · ICT · Confluência intra-escola · risco-retorno). Nenhum registro anterior removido — apenas aditado (INV-07/INV-09).*
