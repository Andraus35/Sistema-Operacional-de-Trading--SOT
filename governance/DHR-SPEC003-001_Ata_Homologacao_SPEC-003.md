# DHR-SPEC003-001 — Ata de Homologação — SPEC-003 v1.5 (Conviction Vector, Evidence Fusion Engine & Conviction Engine — redige o CCM-001)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Revisor de Especificação do SOT / Controlador |
| Ref | SPEC-003 v1.5 — Parecer do Revisor **CONFORME COM RESSALVAS** de 2026-10-02 (Dossiê+Definição: CONFORME 2026-10-01, research.md §6-bis; Plan/Checks v1.4: CONFORME COM RESSALVAS 2026-10-02) |
| Data | 2026-10-02 |
| Status | **HOMOLOGADA — BASELINE** |
| Compatibilidade | Minor |

---

## 1. Decisão

**A SPEC-003 v1.5 está HOMOLOGADA como baseline, por instrução direta de Andraus em chat (2026-10-02: "vamos fechar a SPEC-003").** É a Spec tecnicamente mais crítica do caminho crítico (FASE 1 — NÚCLEO COGNITIVO, P0 BLOCKER) e **redige o CCM-001 (Canonical Conviction Model)**, canônico até aqui pendente — que passa a **BASELINED** por este ato (ver §5.1).

A SPEC-003 fecha **estrutura/método/mecanismo** do Conviction Vector 8D + Evidence Fusion Engine + Conviction Engine, **mais os limiares-piloto interinos** (≥70% / 7-9, Questionário v1). Os **valores definitivos** de fórmula/pesos/limiares (**J-001**) e de pesos por ativo (**N-001**) **permanecem ABERTOS** (pós-backtest; dona a definir — BL-032). A dimensionalidade = 8 (Questionário v1) e a Separação Tríplice (CHM-001) são preservadas; CEM-001 e CHM-001 (canônicos) **não foram redefinidos** (CC-02). RULE-HV (herança vertical) confirmada **não aplicável** (SPEC-003 deriva de modelos canônicos vizinhos, não de macro-spec).

**Caminho de homologação (caminho oferecido pelo próprio parecer).** O parecer do Revisor ofereceu dois caminhos: (a) incorporar notas mínimas de honestidade e re-submeter, ou (b) homologar por ata registrando os achados. Andraus escolheu o **caminho combinado**: as **notas mínimas de honestidade** foram incorporadas à SPEC-003 como **delta v1.5 text-only** (ACHADO-02/03/N1 → notas incorporadas; ver §3), e a **homologação é por esta ata** — **sem nova rodada do Revisor** (as notas são text-only, sem mudança de mérito, sem renumerar BASpecs, sem decidir nada reservado às donas).

Fluxo cumprido: abertura por Dossiê de Pesquisa (RULE-ECC-01/02/04/05, 1ª aplicação da RULE-ECC-05; captura verbatim de 7 fontes) — CONFORME (2026-10-01, research.md §6-bis); homologação da definição (Q-A1..Q-A8) — 2026-10-01; deltas de propagação v1.1 (reconciliação WORKFLOW.md), v1.2 (DHR-ARQ-001), v1.3 (DHR-DEC-001/Q-A5), v1.4 (DHR-DEC-002/Q-A9); parecer do Revisor sobre o Plan v1.4 — **CONFORME COM RESSALVAS** (2026-10-02); delta v1.5 (notas de honestidade) + esta ata.

---

## 2. Efeitos imediatos desta homologação

1. **CCM-001 (Canonical Conviction Model) — BASELINED v1.0.** Criado em `canon/CCM-001-canonical-conviction-model.md` a partir do esqueleto/esquema homologado no `plan.md` (sem conteúdo além do esqueleto). Cabeçalho de proveniência SPEC-003/DHR-SPEC003-001; dimensão `temporal` hospeda a feature de regime (Q-A9); **J-001/N-001/M-001 declaradas abertas dentro do documento**. **CC-02/CONST-01 passa a incidir sobre o CCM-001** (agora há canônico a proteger). CDM-001 e CNM-001 seguem pendentes (não acionam CONST-01).
2. **RULE-CF-001..012 — FATO NORMATIVO com vigência imediata.** Registro físico em `governance/RULES.md` (nova seção "Regras de Convicção/Fusão — RULE-CF") é **passo diferido do Controlador** — mesmo precedente de SPEC-002 (RULE-EH) e SPEC-020/021 (RULE-EV/MM): vigência imediata, registro físico diferido (RULE-HG-02). Até o registro, as RULE-CF valem por esta ata e pelo `plan.md` homologado.
3. **Conviction/Fusion Engine operacional sobre CEM-001/CHM-001 — vigência imediata.** Fusion Engine = único ENGINE PRODUCER de evidência DERIVED; agregação não-compensatória com precedência estrutural (Elliott-veto); tratamento de ausência/conflito/incerteza (INDETERMINADO); gate Convicção→Decisão E3 fail-closed; guard Separação Tríplice + INV-04.
4. **CC-11 aplicada** — 13 BASpecs (CF-001..013) com Classe declarada (C×7, D×4, P×2, H×1) e critério 4Es. CC-12 N/A homologado (infraestrutura de agregação transversal/domain-agnostic — Q-A3).
5. **Q-A9 — RATIFICADA.** A decisão da SPEC-003 (por delegação de Andraus, DHR-DEC-002) de hospedar o regime de mercado (WF-C04) na dimensão **`temporal`** do Conviction Vector 8D está **ratificada** por esta homologação (regime = dimensão de convicção, não gate/veto; sem 9ª dimensão — INV-01/INV-03; peso do regime = J-001/N-001).
6. **BL-002 (Falso-DENY observável, ENF-07) — gatilho `spec:SPEC-003 homologada` DISPARA.** Tratado no passo 11-bis abaixo (§4).
7. **DHR-SPEC003-001 — este documento.** Registrado no histórico de DHRs (`governance/CATALOGO-OFICIAL.md` §7.3).

---

## 3. Ressalvas do parecer e como cada uma foi tratada (não bloquearam a homologação)

O parecer do Revisor (CONFORME COM RESSALVAS, 2026-10-02) listou 6 achados. Tratamento:

| ID (parecer) | Descrição | Tratamento |
|---|---|---|
| ACHADO-02 | **CC-04 sobreafirma cobertura das Salvaguardas** (afirma "5 preservadas" quando o gate verifica 3) | **Nota de honestidade incorporada (v1.5).** CC-04 reescrita: CF-012 verifica DIRETAMENTE 3 Salvaguardas (convicção ≥70%; score ≥7/9; conflito→NEUTRO); **Salvaguarda 1 NÃO materializada** como pré-condição → [DECISÃO NECESSÁRIA: dona a definir por Andraus; **BL-028**]; Salvaguarda 5 (R:R) = fronteira a jusante (Risk Agent). |
| ACHADO-03 | **Proveniência da entrada do gate** (sobre qual valor o gate opera) | **Nota de honestidade incorporada (v1.5, N3).** A Spec NÃO especifica se o gate opera sobre valores por dimensão persistidos/recomputáveis vs. número agregado proposto; ENF-03 aplica (LLM nunca é o gate); recomputação/proveniência → [DECISÃO NECESSÁRIA: **BL-029**; donas Manager Fase 2/SPEC-004/SPEC-018]. Decisão de Andraus de **não resolver isoladamente**. |
| N1 (score 0–9 sem definição) | O gate usa `score ≥ 7/9` mas a Spec não define a composição dos 9 nem o mapa às 8 dimensões | **Nota de honestidade incorporada (v1.5, N1).** `7/9` = FATO NORMATIVO interino (Questionário v1/CEE-001 §11.2); composição/aposentadoria + calibração definitiva = [DECISÃO NECESSÁRIA: dona **J-001**; **BL-027**/H-16]. |
| ACHADO-04 | Texto do ROADMAP "fecha J-001 e N-001" (impreciso — a Spec não fecha os valores definitivos) | **ROADMAP corrigido** (§4 registro do Controlador): "fecha estrutura/método/mecanismo do CCM-001 + limiares-piloto; J-001/N-001 abertas para valores definitivos pós-backtest". |
| ACHADO-05 | `canon/CCM-001` ausente (canônico redigido mas não materializado como arquivo de canon) | **canon/CCM-001-canonical-conviction-model.md criado** (BASELINE v1.0) a partir do esqueleto homologado (§2 item 1). |
| ACHADO-06 | Risco residual (SRC-R03/R04 — evidência de regime-por-dimensão Moderada/Fraca) | **Risco residual ACEITO.** Já declarado honestamente na própria Spec (RULE-MET-01; Nota WF-C04; §7-bis Bloco C); o peso do regime segue J-001/N-001 (não fixado). Não bloqueia; registrado. |

As notas de honestidade (v1.5) são **text-only**, sem mudança de mérito, sem renumerar BASpecs e sem fechar decisão aberta (CONS-01). **Não houve nova rodada do Revisor** — homologação por esta ata, caminho oferecido pelo parecer.

---

## 4. Registro do Controlador (efeitos aplicados — 2026-10-02)

- [x] `specs/features/SPEC-003/plan.md` — Versão → 1.5; Status → **HOMOLOGADA — BASELINE**; histórico v1.5; CC-04 reescrita; seção "Notas de honestidade (v1.5)" (N1/N2/N3); §7-bis Bloco D + lista final de pendências atualizados.
- [x] `specs/features/SPEC-003/checks.md` — nota de delta v1.5 (0-quinquies).
- [x] `specs/features/SPEC-003/research.md` — nota de delta v1.5 (não reabre o Dossiê).
- [x] `canon/CCM-001-canonical-conviction-model.md` — **criado, BASELINE v1.0** (esqueleto homologado; proveniência SPEC-003/DHR-SPEC003-001; J-001/N-001/M-001 abertas no documento; regime em `temporal`).
- [x] `ROADMAP.md` — SPEC-003 marcada **HOMOLOGADA — BASELINE** (Estado atual + §4/§143/§26); texto "fecha J-001 e N-001" **corrigido** para "fecha estrutura/método/mecanismo do CCM-001 + limiares-piloto; J-001/N-001 abertas p/ valores definitivos pós-backtest"; **próximo trabalho autorizado → SPEC-004** (caminho crítico), com nota da linha paralela autorizada por Andraus (abertura da SPEC-038 — Trading Analysis Tool Harness, com viabilidade como critério — BL-031). Q-A9 registrada como ratificada. Sem renumeração.
- [x] `governance/CATALOGO-OFICIAL.md` — §1 (CCM-001 → BASELINED, localização); nova linha de ata (DHR-SPEC003-001); status §6 atualizado; RULE-CF como baseline por vigência imediata (registro físico diferido — precedente SPEC-002).
- [x] `AGENTS.md` — §2 árvore canon (+CCM-001 baselined); §6 item 12 (CCM-001 agora BASELINED → CONST-01 incide; CDM/CNM seguem pendentes).
- [x] `GLOSSARIO.md` — CCM-001 / Conviction Global marcados baselined (SPEC-003).
- [x] `docs/MATRIZ-WORKFLOW-SPEC.md` — SPEC-003 Candidata → **Homologada** (WF-C01/C02/C03/C04, WF-X03, WF-P02, WF-V02, WF-A01, WF-D03).
- [x] `.claude/agents/especificador.md` e `revisor.md` — `sincronizado-até: DHR-SPEC003-001` + SYNC-DATE 2026-10-02 + nota curta.
- [x] `backlog/RMR-001_Painel_Backlog.md` — passo 11-bis: **BL-002** promovido `Em espera` → **ATIVADO** (gatilho `spec:SPEC-003 homologada`); **BL-004** confirmado `Absorvido`; **BL-012** permanece `ATIVADO` (independente); BL-027/028/029 **não disparam** (gatilhos = `spec:SPEC-014`/`spec:SPEC-004`/`decisao:J-001`, não `spec:SPEC-003 homologada`) — ligados por rastreabilidade, não ativados.
- [ ] `python scripts/build_map.py` (+ `--check`), `check_refs.py`, `check_doc_sync.py`, `backlog_triggers.py`, `validate_spec_sot.py specs/features/SPEC-003/plan.md`, suíte de testes/lint: **a revalidar no ambiente (Andraus/Controlador roda)** — o subagente não executa Bash.

**Decisões: estado após esta ata.**
- **Q-A9 — FECHADA / RATIFICADA** (regime → dimensão `temporal`; DHR-DEC-002, ratificada por esta homologação).
- **ABERTAS (não fechadas por esta Spec — CONS-01):** **J-001** (fórmula/pesos/limiares definitivos — pós-backtest; dona a definir, BL-032), **N-001** (pesos por ativo definitivos), **M-001** (estados do Blackboard p/ objeto não-hipótese — SPEC-004), **SPEC-015-SCOPE**, **WF-D03** (resíduo = J-001/N-001), **D-RISK-SP-001**, **CDM-001**. A Spec fecha estrutura/método/mecanismo + limiares-piloto; os valores definitivos são pós-backtest (BL-032 dona a definir).

**Pendências conhecidas com dono (fora deste registro):** **BL-027** (score/limiares — J-001), **BL-028** (Salvaguarda de Sinal 1 — dona a definir por Andraus), **BL-029** (LLM-propõe/harness-recomputa — Manager Fase 2/SPEC-004/SPEC-018), **BL-030** (ponto de interceptação/campo ENFORCER — método/runtime), **BL-031** (TradingView↔SOT → SPEC-038), **BL-032** (dona do backtest/calibração que alimenta J-001/N-001); registro físico de RULE-CF-001..012 em `RULES.md` (diferido, precedente SPEC-002); BL-012 (MC-COG-001) e BL-002 (falso-DENY) ATIVADOS aguardando decisão de Andraus.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
