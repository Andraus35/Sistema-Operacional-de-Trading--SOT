# RCH-001 — Registro de Ciclos de Hygiene de Princípios

**Log corrido dos ciclos de Hygiene (PAP-001 Bloco 4 §6). Cada ciclo registra Plan/Do/Check/Act, disposições e achados. Não deleta (INV-07).**

| Campo | Valor |
|---|---|
| ID | RCH-001 |
| Tipo | Registro operacional (living log) |
| Autoridade | Revisor conduz o Check · Andraus ratifica/homologa emendas |
| Referência | PAP-001 Bloco 4 §6; K-PAP-002 (por milestone + evento) |

---

## Ciclo #1 — 2026-09-19

| Campo | Valor |
|---|---|
| Gatilho | Homologação de CIC-001/PAP-001 v1.2 (evento) + itens RMR-001 `ATIVADO` (BL-005, BL-007) |
| Escopo | Tratar BL-005 (5 FLAGs de conformidade M0) e BL-007 (inversões contextuais no CONFLICT-MAP) |
| Check por | Revisor de Especificação (parecer 2026-09-19) |
| Status | **FECHADO** (2026-09-20): emenda de inversões contextuais do CONFLICT-MAP homologada (DHR-SES-001 / lote); CIC-001 v1.3 = 0 FLAG; BL-005 e BL-007 Absorvidos |

### Plan
Itens `ATIVADO` no RMR-001: BL-005 (5 FLAGs, CIC-001 §4) e BL-007 (CONFLICT-MAP × inversões §3.6). Observação: BL-005 FLAG #5 e BL-007 são o **mesmo objeto**.

### Do / Check — disposições (Revisor, ancoradas em arquivo:§/linha)

| # | FLAG (célula) | Disposição | Justificativa |
|---|---|---|---|
| 1 | atomic-spec × PCO | **RESOLVIDO-BENIGNO** → N/A | PCO-02 incide sobre agentes/hipóteses, não sobre o método de especificação (`GPR-001:139`; `CIC-001:67`) |
| 2 | GEH-001 × PCO | **RESOLVIDO-BENIGNO** → PASS | Cobertura funcional via ETCLOVG (`GEH-001 §5`); GPR-001 (nomenclatura PCO) é posterior ao GEH-001 |
| 3 | ROADMAP × PE | **RESOLVIDO-BENIGNO** → N/A | PE-07 (fronteira de contexto) é declarada por cada Spec (`atomic-spec §4 D1`), não no ROADMAP |
| 4 | CONSTITUTION × PS | **RESOLVIDO-BENIGNO** → N/A | PS-01..04 são situacionais, deferidos às Specs operacionais por design (`GPR-001 §2.6`); CONSTITUTION governa PC-xx |
| 5 | CONFLICT-MAP × PCO/PS | **REQUER EMENDA** | O CONFLICT-MAP não mapeia as 3 inversões contextuais do `GPR-001 §3.6:267-292` (evento crítico: PCO-01>PO-01; efeito irreversível: PB-01>PB-03 via PO-07; regime desconhecido: PS-03/PS-02↑, PC-04 barreira) |

### Achado do ciclo

- **HYG1-F01 — Erro de contagem no CIC-001 v1.0.** O resumo declarava "28 PASS / 5 FLAG / 0 GAP / 3 N/A", mas as 36 células reais somavam **24 PASS / 6 FLAG / 0 GAP / 6 N/A**. Propagado à ata DHR-CIC-001 (histórica, preservada — INV-07). Corrigido no CIC-001 v1.2 (§Resumo). Severidade: Menor (não altera nenhuma disposição de célula; apenas o agregado).

### Act

1. **Aplicado ao CIC-001 (v1.2):** células 1-4 atualizadas (FLAG → N/A/PASS); contagem corrigida (HYG1-F01). Contagem pós-ciclo: **25 PASS / 2 FLAG / 0 GAP / 9 N/A** (as 2 FLAG restantes = CONFLICT-MAP × PCO e × PS, pendentes da emenda).
2. **Emenda em redação (Especificador):** CONFLICT-MAP.md — nova seção "Inversões contextuais (GPR-001 §3.6)" mapeando as 3 inversões. Fluxo: Especificador → Revisor → Andraus.
3. **RMR-001:** BL-005 e BL-007 permanecem `ATIVADO` com encaminhamento "aguardando emenda do CONFLICT-MAP"; viram `Absorvido` só após a homologação da emenda (as células CONFLICT-MAP × PCO/PS → PASS nesse momento).

### Fecho do ciclo #1 (2026-09-20)
- Emenda do CONFLICT-MAP (BL-005#5 / BL-007) **HOMOLOGADA** por Andraus → seção "Inversões contextuais (§3.6)" incorporada; CIC-001 células CONFLICT-MAP×PCO/PS → PASS.
- 4 disposições benignas ratificadas; contagem corrigida (HYG1-F01) → CIC-001 v1.3 = **27 PASS / 0 FLAG / 0 GAP / 9 N/A**.
- BL-005 e BL-007 → **Absorvido** no RMR-001.
- **Resultado: ciclo #1 encerrado com 0 FLAG pendente no M0.**

---

## Ciclo #2 — 2026-09-21 (Higiene e Organização Documental — HOD-001)

| Campo | Valor |
|---|---|
| Gatilho | Homologação do HOD-001 (DHR-HOD-001) — plano de higiene documental |
| Escopo | Reorganizar pastas para findability + 4Es; INV-07 (arquivar, não deletar); reparo de referências |
| Conduzido por | Controlador (execução) · Especificador (plano) · Revisor (parecer CONFORME) |
| Status | **F1 EXECUTADA** (2026-09-21); F2/F3 diferidas (INV-07 vs atas congeladas) |

### Do / Check
- **F1 — root → `reference/camadas/`:** movidas 16 referências externas (12 `CAMADA *.MD` + MC-COG/MC-RAG + CAMADA MEMÓRIA/GOVERNANÇA). Raiz reduzida a whitelist (AGENTS, atomic-spec, ROADMAP, GLOSSARIO, README) + `CAMADA APRENDIZADO.MD` (intake pendente, BL-014). **PASS.**
- **F5 — índice:** CATALOGO §0 "Mapa de Pastas" criado (locator autoritativo). Índices vivos reparados (CATALOGO ext-refs, MAN-001, RMR-001). **PASS.**
- **Reparo de referências (interpretação HOD §4.2):** referências navegáveis vivas atualizadas; **citações históricas em atas DHR preservadas (INV-07)** e resolvidas pelo Mapa de Pastas — atas congeladas não são reescritas.

### Achado do ciclo
- **HYG2-F01 — F2/F3 diferidas.** Mover EUA/DHR dentro de `governance/` e GEH-001 (de `RETOMADA/`) exigiria tocar/roteirizar ~24–30 referências, muitas em **atas congeladas (INV-07)**. Custo desproporcional ao ganho (o clutter era da raiz, resolvido por F1). **Disposição:** manter em `governance/`/`RETOMADA/`; o Mapa de Pastas (CATALOGO §0) resolve localização. Reavaliar em ciclo futuro se necessário. Severidade: Menor (organizacional).

### Act
1. **RPIR ativa** (RCH-001 passo 8): raiz agora auditada a cada ciclo contra o whitelist.
2. **BL-014 ATIVADO:** `CAMADA APRENDIZADO.MD` permanece na raiz até triagem por auditoria; depois → `reference/camadas/`.
3. **Agent-sync:** a lista de leitura dos agentes aponta ao CATALOGO (Mapa de Pastas) — sem mudança de caminho dos baselines que eles leem (governance/ intacto); carimbo `sincronizado-até` mantém-se.

---

---

## Rotina permanente do Check — Convergência Horizontal (MAN-001, DHR-MAN-001 2026-09-20)

A partir do próximo ciclo, todo Check de Hygiene inclui o **passo de Convergência Horizontal** entre Master Contracts (MAN-001 v1.0 §6):

```
Para cada nó normativo (N1..N9 do MAN-001) alterado desde o último ciclo:
  1. conferir se as Invariantes Compartilhadas (MAN-001 §3) continuam consistentes com os pares;
  2. conferir se nenhuma alteração introduziu conflito não governado (MAN-001 §4/§5);
  3. divergência → abrir FLAG neste RCH-001 + item no CIC-001 (Normative/Harness Debt);
  4. colisão de rótulo com baseline → NÃO CONFORME (bloqueia adoção);
  5. drift semântico (EUA-E06, DHR-EUA-E06): para termos do registro de Terminologia
     Concorrente (GLOSSARIO) usados em ≥2 specs, conferir consistência de sentido;
     acepção divergente não declarada → FLAG + item no CIC-001.
     (Opera uma vez populado o registro, a partir da v1.5.)
  6. sensor metacognitivo (EUA-E14, DHR-EUA-E14 — N17 transversal): para specs/cards
     alterados desde o último ciclo, conferir (a) dependência de evidências —
     conclusões distintas ancoradas na mesma premissa apresentadas como confirmações
     independentes (RULE-004/RULE-MET-01); (b) deriva cognitiva — análise afastada do
     objetivo/escopo declarado sem justificativa (MC-001 §74). Sinal → FLAG neste
     RCH-001 + item no CIC-001. (Opera a partir da v1.5.)
  7. sync de agentes (EUA-E16, DHR-EUA-E16 — RPSA): conferir que o carimbo
     `sincronizado-até` de especificador.md e revisor.md corresponde à última DHR em
     escopo (§4.1 da EUA-E16) no CATALOGO-OFICIAL. Divergência → FLAG + item no CIC-001
     (Harness Debt) + item Agent-Sync `ATIVADO` no RMR-001 (a próxima Spec não inicia
     com sync pendente).
  8. higiene da raiz (HOD-001, DHR-HOD-001 — RPIR): conferir que a raiz contém SOMENTE
     o whitelist de caminho-quente (HOD-001 §6b.1). Qualquer doc fora do whitelist → FLAG
     + item no CIC-001: se não-tratado → item de intake `ATIVADO` no RMR-001 (triar);
     se tratado → violação de higiene (arquivar na pasta respectiva ou excluir, HOD-001 §6b.3).
```

Objetivo: detectar **drift horizontal** (master contracts de mesma hierarquia evoluindo de forma incompatível) antes que contamine as Specs. Reusa o mecanismo de Hygiene homologado (economicidade).

---

*RCH-001 — Registro de Ciclos de Hygiene. Ciclo #1 conduzido em 2026-09-19. Rotina de Convergência Horizontal (MAN-001) incorporada em 2026-09-20. Próximos ciclos anexados abaixo (append-only, INV-07).*


---

## Ciclo #3 — 2026-09-26 (achados do verificador de referências — K-REF-01)

> Anexado (append-only, INV-07) a pedido e com aprovação de Andraus (Decisor Final), 2026-09-26. Texto-fonte: `UPGRADES/PROPOSTA-REGISTRO-HYGIENE-2026-09-26.md`. Nenhum registro anterior alterado.

### K-REF-01 — citação sem lastro `DHR-PRA-001` (agentes do trio) — **FECHADO**

| Campo | Valor |
|---|---|
| Origem | `scripts/check_refs.py`, execução 2026-09-26 |
| Objeto | `.claude/agents/especificador.md` (§6.2) e `.claude/agents/revisor.md` (cabeçalho e Passo 7) |
| Achado | Três citações a uma ata de prefixo DHR "PRA-001" sem arquivo, sem linha no CATALOGO-OFICIAL e sem menção em qualquer outro documento (incl. `docs/_legacy/`). |
| Verificação de Andraus | 2026-09-26: **não há** ata, backup ou registro externo com esse nome. |
| Disposição | **FECHADO — citação sem lastro, removida; autoridade = EUA-E02 v1.2 + ENF-01…08 do `atomic-spec.md`.** Nenhuma ata retroativa criada (RULE-MET-01, INV-07). |
| Ação aplicada | Citação removida dos títulos; nota de rastro no cabeçalho do `revisor.md`. Comportamento dos agentes inalterado. |

### Passo 7 (RPSA) — correção de citação nos agentes

`especificador.md` e `revisor.md` editados em 2026-09-26 **apenas para corrigir a citação acima**, sem mudança de comportamento e sem DHR nova. Carimbo `sincronizado-até` **inalterado** (não houve homologação em escopo). Divergência editorial registrada; o Revisor confirma no próximo ciclo, por releitura dos dois arquivos, que o comportamento é o mesmo. Sem FLAG de Harness Debt se a releitura confirmar.

### Ferramental adicionado (informativo)

`scripts/check_refs.py` + `tests/test_check_refs.py`; hooks `gate-check.js`/`post-edit-check.js` corrigidos para o contrato real do Claude Code (stdin JSON, exit 2) + `tests/test-hooks.js`; STRUCT-10 corrigido + `tests/test_struct10.py`; CI com etapa informativa do `check_refs.py` (`continue-on-error`). Promoção a bloqueante (só nível ERRO, nunca `--strict`/`--info`) após período estável.

### RMR-001

BL-019 (mapa de grafo) registrado como `Proposto`. **BL-006 → `ATIVADO`** por Andraus (2026-09-26); encaminhamento pendente = implementar a varredura de gatilhos.


### Adendo (2026-09-26) — BL-006 absorvido

Aditivo ao item "RMR-001" acima (texto original preservado — INV-07). Por decisão de Andraus (2026-09-26): **BL-006 → `Absorvido`** — varredura de gatilhos implementada em `scripts/backlog_triggers.py` (tri-estado; somente leitura; exit 1 só em gatilho disparado sem registro; testes em `tests/test_backlog_triggers.py`; etapa informativa no CI). O encaminhamento pendente citado acima fica **cumprido**; o gate não tem mais `ATIVADO` sem encaminhamento por BL-006. BL-019 segue `Proposto` (não ativado). Estado do painel na data: 0 gatilhos disparados sem registro; ATIVADO = BL-008; 9 itens em verificação manual.


### Adendo (2026-09-26) — BL-019 ativado e mapa gerado

Aditivo (texto anterior preservado — INV-07). Por decisão de Andraus (2026-09-26): **BL-019 → `ATIVADO`** e mapa v0.1 gerado por `scripts/build_map.py` em `docs/mapa/MAPA-PROJETO.md` e `docs/mapa/mapa-projeto.json` (148 documentos; camadas por diretório, hubs de ID com definição, cadeia de Specs, documentos sem referência de entrada — candidatos à triagem RPIR, sem implicar lixo). **NÃO-NORMATIVO** (INV-09): não substitui o CATALOGO-OFICIAL (locator autoritativo) nem fecha decisão aberta (CONS-01); regenerável, `--check` como sensor de defasagem (insumo do sensor de drift MAN-001). Encaminhamento cumprido; aguarda homologação de Andraus para `Absorvido`.


### Adendo (2026-09-26) — manutenção do mapa garantida (diretiva de Andraus)

Aditivo (INV-07). Diretiva de Andraus: **todos os agentes atualizam o mapa (`docs/mapa/`) quando alterarem documentos.** Garantia em camadas, sem depender de memória do agente: (1) hook `PostToolUse` `scripts/map-sync.js post-edit` regenera a cada Write/Edit/MultiEdit em `.md` do escopo; (2) hooks `Stop`/`SubagentStop` `map-sync.js stop` regeneram se houver defasagem (edições via Bash, rename, delete); (3) `python scripts/build_map.py --check` **bloqueante** no CI e no pre-commit; (4) regra escrita em `AGENTS.md` (§5, §8), item no Autopré-check do `especificador.md` (§7) e observação Menor no `revisor.md` (agente somente leitura — apenas verifica a declaração). Hooks nunca bloqueiam o agente (backstop = CI). Agentes editados (`especificador.md`, `revisor.md`): adição de regra operacional sem alterar comportamento normativo; carimbo `sincronizado-até` **inalterado** (sem DHR nova) — divergência editorial registrada para confirmação do Revisor no próximo ciclo (Passo 7 RPSA). `.claude/settings.json` ganhou `MultiEdit` nos matchers e os hooks Stop/SubagentStop.


### Adendo (2026-09-26) — divergência editorial dos agentes ENCERRADA (DHR-EUA-E22)

Aditivo (INV-07). Homologada a **EUA-E22** (DHR-EUA-E22, 2026-09-26; Revisor CONFORME; Q1–Q4 = Sim por Andraus): as edições em `especificador.md`/`revisor.md` (K-REF-01, regra R-MAPA) ganharam lastro de DHR; `sincronizado-até` de ambos → **DHR-EUA-E22** (RPSA). A "divergência editorial conhecida" registrada nos adendos anteriores do Ciclo #3 fica **ENCERRADA** — a confirmação por releitura do Revisor foi cumprida pelo próprio parecer da EUA-E22 (que verificou os arquivos com arquivo:linha). K-REF-01 permanece FECHADO. Pendência encaminhada ao próximo ciclo de Hygiene: OBS-01 (`AGENTS.md` §7 ainda lista L-001 como ativa; FECHADA por DHR-SPEC019-001).


### Adendo (2026-09-26) — BL-019 absorvido; OBS-01 tratada

Aditivo (INV-07). Por decisão de Andraus (2026-09-26): **BL-019 → `Absorvido`** — mapa `docs/mapa/` (gerado por `scripts/build_map.py`) + regra R-MAPA homologada (DHR-EUA-E22). O backlog fica com **BL-008** como único `ATIVADO`. **OBS-01 (parecer da EUA-E22) tratada:** `AGENTS.md` §7 corrigido — **L-001** removida das decisões ativas e registrada como **FECHADA** (DHR-SPEC019-001, 2026-09-22; dimensão spec-time; runtime → SPEC-018/K-001). Nenhuma decisão aberta foi fechada por esta correção: ela apenas alinha o §7 ao fechamento já homologado (CONS-01). Observação remanescente (fora deste escopo): o `ROADMAP.md` lista decisões/itens ativos adicionais (SPEC-020-PRINC-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001) que o §7 do `AGENTS.md` não enumera — o §7 é a lista-base de decisões J/G/H/I/K/C/M/N-001; o ROADMAP segue como fonte completa.

### Adendo (2026-09-26) — `AGENTS.md` §7 completado com os itens do ROADMAP

Aditivo (INV-07). Por decisão de Andraus: o §7 do `AGENTS.md` passou a enumerar também as decisões/itens ativos do `ROADMAP.md` (linha "Decisões abertas ativas") — SPEC-020-PRINC-001, SPEC-045-RUNTIME-001, RISK-ARR-LOC-001, RISK-CONV-001 — todos como **abertos**, com o estado exato do ROADMAP (SPEC-045-RUNTIME-001 = inferência, não baseline; RISK-ARR-LOC-001 = ABERTA, não fechada pela EUA-E19a). Nenhuma decisão foi fechada nem reclassificada (CONS-01); em divergência prevalece o ROADMAP. A observação remanescente do adendo anterior fica **resolvida**.

### Adendo (2026-09-26) — EUA-E21 homologada (Especificação Emergente)

Aditivo (INV-07). **DHR-EUA-E21:** o ROADMAP passa a fixar direção e restrições; as Specs (SPEC-002…045 = slots indicativos) são definidas **na abertura**, após **Dossiê de Pesquisa** web pelo Especificador (RULE-ECC-01/02; fail-closed; Revisor audita o processo — Passo 4-bis). Percurso completo do trio: proposta v1 → Revisor **NÃO CONFORME RECUPERÁVEL** (M-01/02/03) → v2 → Revisor **CONFORME** → consenso de Andraus → aplicação. `sincronizado-até` de `especificador.md` e `revisor.md` → **DHR-EUA-E21** (RPSA). **Novo para o próximo ciclo de Hygiene:** (a) decisões abertas **ECC-VAL-001** (validade do Dossiê) e **ECC-03-001** (escopo da RULE-ECC-03; sigla ECC não expandida no repositório) aguardam Andraus; (b) **BL-020/BL-021** (`Proposto`) — ferramental ainda assume numeração estável (o mapa rotula slots como "Planejada"): aceito até o BL-021; (c) conferir **§26 do ROADMAP** (capacidades exigidas × Specs abertas) quando a SPEC-020 (piloto) abrir. Nenhuma decisão aberta foi fechada.

### Adendo (2026-09-27) — execução do `harness-eval` (run `2026-09-26-full`, escopo completo B+C, todos os tipos opcionais)

Aditivo (INV-07). Saídas em `.claude/skills/harness-eval/runs/2026-09-26-full/` (mesmo local das execuções anteriores; fora do escopo do mapa e do `check_refs`). **Track A (determinístico):** 12 BROKEN → **10** após correção de 2 citações do projeto (`docs/mapa/.stale` em `AGENTS.md` e `.clinerules/sot-map.md` — arquivo *condicional* que só existe em falha; reformulado sem caminho fixo, sem mudança de comportamento); os 10 restantes estão no texto **genérico do skill vendorizado** (`.agents/skills`, `.cursor/skills`, `lib/...`, `bin/console`, exemplos) — não são citações do projeto; **não editados** (skill de terceiros). **Track B:** armadilhas PASS; Ship 20 (AGENTS.md preâmbulo; lista de scripts do skill vendorizado; princípios genéricos e comandos já no `package.json` no `.claude/skills/SKILL.md`), Review 290, Hold 3 — **nenhum corte aplicado** (evidência dos juízes majoritariamente por julgamento do texto; verificação em disco limitada a `package.json`/listagens). **Track C:** armadilhas PASS; fan-in sem bloqueio; **Slim 0**, Keep-core 12 (AGENTS.md, agentes, ROADMAP, atomic-spec, CATALOGO, CONFLICT-MAP, CONSTITUTION, GPR-001, RULES, PROTOCOL/judge-prompts do skill), Mixed 1 (`.claude/skills/SKILL.md`), Hold 9. **Mixed `.claude/skills/SKILL.md` NÃO aplicado:** conflito KEEP×CUT (J1 mantém "4Es hierarchy"; J2 corta "Part 1 (4Es …)") → pular o caminho (regra 3 do `11-mixed-apply.md`); Juiz 2 declarou leitura rasa (deck + trechos). Ambos os juízes usaram o mesmo modelo (`claude-sonnet-5`) e o protocolo pede segunda família de modelo antes de qualquer corte grande. **Nenhum conteúdo normativo foi removido.**

### Adendo (2026-09-27) — CTX-04 do `harness-score` resolvido (frontmatter das regras Cline)

Aditivo (INV-07). **Causa raiz:** para regras Cline o `harness-score` v1.6.5 exige a chave `paths` (texto não vazio, lido linha a linha — lista em bloco resultaria vazia); os 4 arquivos de `.clinerules/` usavam apenas o estilo Cursor (`description`/`globs`/`alwaysApply`). **Correção (aditiva):** acrescentado `paths: [...]` inline, idêntico aos `globs` existentes, em `sot-map.md`, `sot-rag.md`, `sot-schemas.md` e `sot-specs.md`; nenhum campo removido; corpo das regras intacto; YAML validado. **Efeito:** nota 102 → **105/108 (97%)**, Context & Guides 100%. **Efeito comportamental (Cline):** as regras passam a ser de ativação **condicional por caminho** (como suas descrições já indicavam), em vez de dependerem de chaves que o Cline pode ignorar. Restante: HYG-08 (MCP com `${ENV_VAR}`) — **não aplicável** (sem MCP no projeto); não criar configuração só para pontuar.

*Ciclo #3 registrado a pedido de Andraus. INV-07 preservado; nada removido, apenas adicionado.*
