# DHR-EUA-E25 — Ata de Homologação: Enforcement do fluxo de orquestração cognitiva (E1→E8) — Tabela vinculante + `RULE-ECC-07`

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E25** |
| Objeto | Homologação da emenda **EUA-E25** (`governance/EUA-E25_Enforcement_Fluxo_Runtime_PROPOSTA.md`) — criação da regra normativa **`RULE-ECC-07`** (Enforcement do fluxo de runtime) e reconhecimento da **força vinculante** da Tabela de Enforcement de **`WORKFLOW.md §7-bis.2`** (adotar/adaptar/justificar desvio de Enforcement Contract por Specs de agente/transição do fluxo, SPEC-002 em diante) |
| Natureza | Emenda **de método** (mesmo padrão EUA-E21..E24) — **aditiva**; cria uma RULE nova (RULE-ECC-07, família ECC já registrada); **não** redefine canônico; **não** fecha decisão aberta |
| Compatibilidade (RULE-HG-04) | **Minor** (aditiva; nenhum documento removido, nenhuma norma reescrita, nenhum identificador reutilizado — INV-07/INV-09; nenhuma decisão aberta fechada — CONS-01) |
| Data | 2026-09-29 |
| Vigência | **Imediata e prospectiva.** RULE-ECC-07 incide a partir de SPEC-002; não retroage sobre SPEC-001/019/020/021/046. |
| Status | **HOMOLOGADA — BASELINE** |

---

## 1. Fluxo de autoridade (RULE-HG-01 / RULE-HG-08; GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (chat, 2026-09-29) ........... ✅ "SIM POIS O WORKFLOW PODE SER ATUALIZADO ATÉ O FIM DO
                                                               PROJETO. IMPORTANTE AGORA MESMO É CONDUZIR O DOSSIE POR
                                                               ESSAS LENTES. PODE RASCUNHAR E VINCULAR."
Etapa 2 — Formalização (EUA-E25 + §7-bis rascunhada no /WORKFLOW.md) .... ✅ Especificador — NADA aplicado a baseline
Etapa 3 — Parecer do Revisor .............................. ✅ CONFORME condicional (0 achados Crítico/Médio;
                                                               1 Menor F-01 não-bloqueante — ver §2)
Etapa 4 — Decisão de Andraus (pergunta única da emenda) .... ✅ "SIM" (2026-09-29) — homologar RULE-ECC-07 e a
                                                               §7-bis.2 do WORKFLOW.md como baseline normativo
Etapa 5 — Registro Oficial / aplicação .................... ✅ EFETIVADO — esta ata + edições de baseline (§4)
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME (condicional) + consenso do Usuário + registro pelo Controlador. **Ordem respeitada: nada foi aplicado a baseline antes do parecer e da homologação.**

## 2. Parecer do Revisor e decisão de Andraus

- **Parecer do Revisor:** **CONFORME condicional** — 0 achados Crítico/Médio; **1 Menor F-01 não-bloqueante**: WARNs de `python scripts/check_refs.py` decorrentes de `INV-RISK-08`/`INV-RISK-12` citados de `reference/SOT-RISK-MASTER-001_Consolidado.md` — **não fabricados** (existem na fonte de risco), apenas **fora da cobertura do script** de checagem de referências. Não exige ação nesta aplicação (matéria de auditoria/encaminhamento, não de correção de conteúdo).
- **Pergunta única da emenda a Andraus:** homologar `RULE-ECC-07` e a §7-bis.2 do `WORKFLOW.md` como baseline normativo?
- **Decisão de Andraus (2026-09-29):** **"SIM"**.

## 3. Objeto homologado

- **`RULE-ECC-07`** (inserida em `governance/RULES.md`, seção "Regras de Especificação Emergente (RULE-ECC)", após RULE-ECC-06): toda Spec (SPEC-002 em diante) que especifique um **agente do fluxo de runtime** (estrutural/institucional/operacional/manager/contexto/orquestrador ou de risco) ou uma **transição E1→E8** (`WORKFLOW.md §3`) DEVE declarar seu próprio **Enforcement Contract** (`atomic-spec §10.3`, ENF-01..08) para cada handoff/efeito e esse contrato DEVE ser **COMPATÍVEL** com a Tabela de Enforcement de `WORKFLOW.md §7-bis.2` — **adotar / adaptar / justificar desvio — nunca ignorar em silêncio**. A compatibilidade preserva, no mínimo: (i) **Detector ≠ Gate** (ENF-03); (ii) **as duas classes de falha** (forma = hard-stop determinístico; ausência de oportunidade/convicção insuficiente = fluxo normal, não falha); (iii) **fail-closed** em efeito crítico irreversível (ENF-04; emissão externa E8 = E3). A regra vincula a **obrigação de declarar enforcement compatível**, não o conteúdo substantivo da Spec. Verificação do Revisor: ausência onde exigível = **NÃO CONFORME Crítica** (fail-closed); desvio sem justificativa = **Médio**.
- **Status vinculante da `WORKFLOW.md §7-bis.2`:** o `WORKFLOW.md` permanece **não-normativo e descritivo por natureza** (§0), MAS a **exigência de compatibilidade de Enforcement Contract da §7-bis.2** passa a ser **efetiva/vinculante** para Specs de agente/transição do fluxo por força da **RULE-ECC-07** (mesmo padrão de vínculo da RULE-ECC-06). O restante da §7-bis e do documento segue descritivo/`[INFERÊNCIA]`.

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração | Estado |
|---|---|---|
| `governance/RULES.md` | **RULE-ECC-07** inserida na seção RULE-ECC (após RULE-ECC-06), `[Fonte: DHR-EUA-E25; ...]` no padrão das RULE-ECC-05/06 | ✅ aplicado |
| `atomic-spec.md` | §15: nota "Enforcement de orquestração (EUA-E25 / RULE-ECC-07)" após o parágrafo do Insumo de orquestração (RULE-ECC-06) | ✅ aplicado |
| `WORKFLOW.md` | §7-bis: título e nota de status atualizados — §7-bis.2 agora **vinculante via RULE-ECC-07 (HOMOLOGADA)**; §7-bis.5 atualizada (proposta → homologada). Restante do documento intocado (segue descritivo) | ✅ aplicado |
| `governance/EUA-E25_Enforcement_Fluxo_Runtime_PROPOSTA.md` | Status → **HOMOLOGADA — BASELINE**; §7 fluxo de autoridade com Etapas 1–5 concluídas; rodapé atualizado. Corpo da proposta preservado (INV-07) | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | §4: linha **EUA-E25** (emenda, HOMOLOGADA) + nota na linha do `WORKFLOW.md` (§7-bis.2 vinculante via RULE-ECC-07); §7.3: linha **DHR-EUA-E25** (ata, REGISTRADO) | ✅ aplicado |
| `.claude/agents/especificador.md` | `sincronizado-até` → DHR-EUA-E25; nota DHR-EUA-E25 no carimbo; `required_sources` (+DHR-EUA-E25); item RULE-ECC-07 no Autopré-check §7; ponteiro RULE-ECC-06 atualizado para `WORKFLOW.md` | ✅ aplicado |
| `.claude/agents/revisor.md` | `sincronizado-até` → DHR-EUA-E25; nota DHR-EUA-E25 no carimbo; `required_sources` (+DHR-EUA-E25); Passo 4-bis ampliado com auditoria da RULE-ECC-07 (mesma lógica de severidade de RULE-ECC-05/06) | ✅ aplicado |
| `ROADMAP.md` | Cabeçalho: "Emenda vigente adicional: EUA-E25"; §23 passo 1-bis: nota de que Specs de agente do fluxo declaram Enforcement Contract compatível com `WORKFLOW.md §7-bis.2` (RULE-ECC-07) | ✅ aplicado |
| `docs/mapa/` (BL-019/R-MAPA) | Regenerar via `python scripts/build_map.py` após estas edições `.md` (não editar à mão). **Pendência de execução** — Especificador não tem Bash (reportado ao coordenador) | ⏳ pendente |

## 5. NÃO aplicado / NÃO tocado (deliberadamente)

- **Nenhuma Spec homologada** (SPEC-001/019/020/021/046) reescrita ou reaberta. RULE-ECC-07 é **prospectiva** (SPEC-002 em diante).
- **Nenhuma decisão aberta fechada** (CONS-01): **J-001** (limiares de convicção usados nos gates de fluxo — Fase Piloto interino), **M-001** (estados do alarme), **K-001**, **SPEC-045-RUNTIME-001**, **SPEC-008**, **RISK-CONV-001**, **RISK-LEV-001**, **D-RISK-SP-001**, **RISK-ARR-LOC-001**, **ENF-LOC-001** (`[PROPOSTA]` de identificador — só Andraus cunha), **RUNTIME-TF-PAIR-EXT-001**, **RULE-REG-001**, **ECC-VAL-001**, **ECC-03-001**, G-001, H-001, C-001, N-001, SPEC-020-PRINC-001 — todas permanecem abertas. **RULE-ECC-03 permanece RESERVADA.**
- **Reconciliação editorial dos rótulos E-antigos** nos `$comment` dos 5 schemas `runtime-workflow.*.json` permanece `[DECISÃO NECESSÁRIA]` editorial (não desta emenda).
- **Os 5 schemas `runtime-workflow.*.json`** permanecem `[PROPOSTA]` não-normativa.
- **RULE-ECC-05 e RULE-ECC-06 não reabertas nem alteradas em mérito** — apenas o ponteiro de fonte do Insumo (RULE-ECC-06) já apontava a `/WORKFLOW.md` desde DHR-EUA-E24; reafirmado.

## 6. Invariantes preservados

- **CONS-01:** nenhuma decisão aberta fechada; nenhuma nova aberta por esta emenda.
- **INV-07:** **nada deletado.** Corpo da proposta EUA-E25 preservado; `RUNTIME-WORKFLOW-001` (SUPERSEDIDO) intocado; nenhuma versão apagada.
- **INV-09:** nenhuma norma reescrita — RULE-ECC-07 é **aditiva**; a §7-bis.2 do WORKFLOW.md não foi reescrita, apenas teve sua **força vinculante reconhecida** pela regra.
- **CONST-01:** nenhum modelo canônico baselined redefinido (CHM-001, CEM-001, CEE-001 v2.0, GMC/SDD/PPQ/SAS/CR). A RULE-ECC-07 deriva de `atomic-spec §10` (ENF-01..08), que não é redefinido.
- **Hierarquia analítica, R:R 1:3, convicção ≥70%/score ≥7/9, Conviction Vector 8D, Signal Package, INV-05:** intocados. A Tabela §7-bis.2 os **cita** como fonte de verdade (`AGENTS.md §6`), não os redefine.
- **ENF-03:** `revisor.md` continua sem Write/Edit e sem acesso web — verifica presença/compatibilidade declarada (Detector), não o mérito de runtime.
- **RPSA (EUA-E16):** `sincronizado-até` de ambos os agentes → **DHR-EUA-E25**.
- **RULE-MET-01:** nenhuma afirmação fabricada; regeneração do mapa e execução dos validadores não realizadas (Especificador sem Bash) — reportadas como pendência, não como fato concluído.

## 7. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultar `backlog/RMR-001_Painel_Backlog.md` — a confirmar pelo coordenador via `python scripts/backlog_triggers.py` se algum item é disparado por esta homologação.
2. **Próximo trabalho autorizado:** **SPEC-002** — 1ª Spec de domínio da fase (Trilha B), sob RULE-ECC-01/02/05/06 e, quando for Spec de agente do fluxo, também sob **RULE-ECC-07** (Enforcement Contract compatível com `WORKFLOW.md §7-bis.2`).
3. **Pendências de validação (o Especificador não tem Bash — para o coordenador rodar):** `python scripts/build_map.py` + `--check` (mapa BL-019, obrigatório após alterar `.md`); `python scripts/check_refs.py` (integridade de referências — incl. o F-01 residual dos WARNs INV-RISK-08/12); `python scripts/check_doc_sync.py` (drift de sincronização; RULE-ECC-07 agora registrada em RULES.md); `python scripts/validate_spec_sot.py` (N/A — esta emenda não é plan.md); `python scripts/backlog_triggers.py`.

---

*Ata registrada pelo Controlador (Claude Code) a partir da homologação de Andraus (Decisor Final), 2026-09-29, comunicada em chat — a decisão é de Andraus; este registro não a substitui. Parecer do Revisor: CONFORME condicional (0 Crítico/Médio, 1 Menor F-01 não-bloqueante). Decisão de Andraus à pergunta única: "SIM". Nenhum registro anterior removido — apenas aditado (INV-07/INV-09). Nenhuma decisão aberta fechada (CONS-01); nenhum canônico redefinido (CONST-01).*
