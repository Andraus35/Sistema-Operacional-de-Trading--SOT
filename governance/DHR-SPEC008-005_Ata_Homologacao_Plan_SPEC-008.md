# DHR-SPEC008-005 — Ata de Homologação — Plan da SPEC-008 v1.2 (Manager — Despacho e Ciclo, Fase 1)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-008/plan.md` v1.2 (1.885 linhas de corpo; SHA256 `21a52c6b015cbcb875521f6ff5a23eb0745252379f407a5e3fcf92d28dc73df8`) + `checks.md` + `HISTORICO.md` · pareceres do Revisor em `governance/propostas/SPEC-008/`: R1 (NÃO CONFORME, 5 Médias, 8 Menores), R2 (NÃO CONFORME, 2 Médias, 11 Menores) e R3 (**CONFORME condicional**, 0 Críticas, 0 Médias, 9 Menores; por delta) · gates do Orquestrador: `validate_spec_sot` 14/14, `revisor_gate` PASSOU_D (0 sinais H), `pre_entrega` 0 bloqueantes · `DHR-SPEC008-001` (abertura) · `DHR-SPEC008-002/003` (MMC-001 v1.0 + errata) · `DHR-SPEC008-004` (DN-1/DN-2) · `DHR-FIBFRAC-001/002` · `DHR-EXPERIMENTO-PARADA-001` · `DHR-PROCESSO-EXPERIMENTOS-001` |
| Data | 2026-11-15 |
| Status | **PLAN v1.2 HOMOLOGADO — BASELINE** (decisão direta de Andraus por AskUserQuestion, 2026-11-15: "Homologar com os 4 como condição (Recomendado)"). Assinatura = decisão registrada e citada nesta ata (AGENTS.md §10). Homologação **CONDICIONADA** (§3). Sem BUILD (fase spec-first). *[Estado anterior preservado — INV-07: "PROPOSTA — CANDIDATA; aguarda Revisor (rodada 3) e homologação de Andraus. NÃO é baseline"]* |
| Compatibilidade | Minor (não toca modelo canônico baselined nem Spec baselined) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de Plan de Spec em redação: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]`
| # | Ponto | Decisão |
|---|---|---|
| O-1 | Ordem do Plan | **Registrada nesta ata**: Andraus ordenou o Plan da SPEC-008 em chat, 2026-11-08 ("Avançar"), depois da abertura (`DHR-SPEC008-001`) e do MMC-001 (`DHR-SPEC008-002/003`); as rodadas R1–R3 e as correções foram cobertas pela mesma ordem |
| DN-1 / DN-2 | Rótulo do ciclo encerrado; quem abre ciclo em ruptura de hipótese dominante | `DHR-SPEC008-004`: DN-1 = **decidir depois, com a SPEC-014** (segue aberta); DN-2 = a Fase 1 só detecta e avisa |
| F-1..F-4, DN-3, Q5 | Fibonacci = skill dos agentes; confluência fractal não decidida; Fibonacci só confere; leitura macro inalterada; TFs S1/D1/H4/H1/M5 fixos (diverge de WF-R01); roteiro v1 Elliott → SMC → ICT confirmado; glossário de "confluência" só como proposta | `DHR-FIBFRAC-001` e `DHR-FIBFRAC-002` |
| R3 | O que fazer com os 9 Menores do parecer R3 | **Corrigir já os 4 de redação (R3-m01, m02, m03, m06) sem nova rodada do Revisor** (AskUserQuestion 2026-11-15; teto de 3 rodadas do experimento P10) e **homologar com os outros 4 como condição**; R3-m09 (data) aplicado pelo Orquestrador (classe M) |
| Homologação | Plan v1.2 | **Homologar com os 4 como condição** |

## 2. Efeitos da homologação
- Plan v1.2 da SPEC-008 (1 INV, 11 RULE, 13 EARS, 12 BASpec — 11 Classe D e 1 Classe C, a trava E3 —, 9 EC, 23 cenários, 15 ADV; D5 com 39 linhas; CRITICAL D0–D8; nenhuma BASpec H/P) é **BASELINE** da SPEC-008; `plan.md` e `checks.md` com histórico preservado (INV-07; `HISTORICO.md`). Pai de herança: MMC-001 v1.0 (RULE-HV-01).
- `ROADMAP.md` (seção da SPEC-008, tabela do §25 e "Decisões FECHADAS"), `governance/CATALOGO-OFICIAL.md`, `governance/rpsa-ledger.json` e `plan.md`/`checks.md` (cabeçalho de status) atualizados, texto anterior preservado. "Próximo trabalho autorizado" **não** muda (precedente `DHR-SPEC049-002`). Estados do painel de backlog **não mudam** (sem promoção — só Andraus; as Disposições BL-026 PARCIAL, BL-043 FORA, BL-044/045/046 REFERÊNCIA seguem as da abertura).
- **Experimento da regra de parada (P10): ENCERRADO para este Plan** (`governance/EXPERIMENTOS-ATIVOS.json`, `estado: encerrado`); a retrospectiva da SPEC-008 decide se a regra vira norma. Resultado bruto: 3 rodadas de revisão (Médias 5 → 2 → 0; Menores 8 → 11 → 9), correções finais sem nova rodada por escolha de Andraus.
- **Avaliação de desempenho de fim de Spec (`DHR-AVALIACAO-001`): a aprovação final nasce com esta ata.** `avaliacao_spec.py gerar SPEC-008 --write` foi rodado (Estado GERADA); as perguntas automatizadas vão a Andraus por AskUserQuestion; sem a avaliação `RESPONDIDA` e a retrospectiva `FEITA`, `loop_ledger.py --retro-check SPEC-008` falha e nenhuma outra Spec abre.

## 3. Condições da homologação (Menores R3 deixados como condição — a cumprir por errata aditiva ao Plan, em passo à parte por ordem de Andraus, ou na construção/Tasks, o que vier primeiro)
1. **R3-m04 [C10]:** a falha do `MARK_CONSUMED` pedido por F16, já em `EM_SÍNTESE`, cai em F27 (`MDC_NOT_PHASE1_TRANSITION`) sem reenvio e sem cenário; o ✔ do `checks.md` §5 é amplo demais. Declarar a ordem (confirmação antes da transição) ou o desfecho aceito, com cenário.
2. **R3-m05 [C05]:** falha parcial na 2ª conferência de F01 (`TIME_REQUEST` do `STAGE_TIMER`) com o ciclo já aberto sem cenário; INV-MDC-01 diz "no pedido nada é aberto". Acrescentar a variante em ADV-12 ou uma frase em D4.1 SAÍDA.
3. **R3-m07 [C01]:** `notice.kind = CAPABILITY` inalcançável (F37/ADV-12 exigem "nenhum aviso") e destinatário `to = Andraus` × "Andraus/Fase 0" em RULE-MDC-004 (d), EARS 5 e T18. Alinhar o enum e o destinatário.
4. **R3-m08 [C06]:** `HISTORICO.md` R2→R3 sem linhas de BASpec-MDC-003 e T22 e sem ponteiro à FICHA-M do parecer R2 para o texto anterior das edições de classe M.
O Plan **não** é editado por esta ata além do cabeçalho de status (INV-09 vale daqui em diante).

## 4. Condições de conformidade (o que esta homologação NÃO afirma)
- O Revisor não executou o gate dentro da sessão (teto CONFORME condicional); o Orquestrador rodou os gates sobre a versão final (14/14; PASSOU_D; pre_entrega 0 bloqueantes). Veracidade das fontes `[EXTERNO]` e adulteração de `sources/` são risco residual declarado.
- **Edições sem revisão:** o parecer R3 cobre a v1.2 no commit `28eb871` (SHA256-ALVO `44e6131f…`). Depois dele entraram **só** as 4 correções de redação (R3-m01, m02, m03, m06) e R3-m09 (data), **sem nova rodada do Revisor, por escolha expressa de Andraus** (teto de 3 rodadas). O Orquestrador conferiu o diff (mínimo, +2 linhas líquidas; idêntico à ação pedida no parecer; texto anterior em `HISTORICO.md`), por Grep, e pelos gates; **não** reexecutou a simulação da D4.2 por revisão independente. Isso é risco residual declarado (a categoria C01 cenário × algoritmo reapareceu em R1, R2 e R3).
- As **errata propostas** no Plan (E-1: nota aditiva à SPEC-003 com 9 linhas de re-apontamento; E-2: gatilho do BL-026; E-3: SPEC-002/006/020 e BL-017 não citam "SPEC-008") **não foram aplicadas**: só por errata homologada a Spec baselined (CONST-01).
- Divergências registradas e não resolvidas: CF-A (CCM-001 × RULE-CF-010), CF-B/CF-D (WF-R01 × tempos gráficos fixos — reconciliação do WORKFLOW só de Andraus), CF-C, CF-E (precondição `GATED_PASS` do BL-029 escopo Fase 2), CF-F.
- Os positivos dependem de **BUILD** (fase spec-first): o contrato `capability_audit_record` independente do runtime, o relógio/Spec de Tempo (candidata SPEC-050, Plan próprio depois) e a persistência do estado do ciclo (G-001/SPEC-009). **Não há BUILD.** Dossiê válido até 2027-02-05.

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 (residual) · D-PCC-4 · BL-026 · P-13 (reentrada após stop) · DN-1 (rótulo do ciclo encerrado, com a SPEC-014) · localização da confluência fractal (parte fractal da P-11) · limiar de "conclusiva" θ (J-001/N-001: sem número). **Nenhuma decisão aberta é fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] Confirmação de Andraus (AskUserQuestion 2026-11-15) · [x] ROADMAP · [x] CATALOGO · [x] RPSA · [x] plan.md/checks.md (cabeçalho) · [x] experimento P10 encerrado · [x] avaliação de desempenho gerada · [ ] merge (PR, CI verde — assinatura) · [ ] **avaliação de desempenho RESPONDIDA e retrospectiva de fechamento da SPEC-008 (LOOP-001 passo 5; antes de abrir outra Spec)** · [ ] errata aditiva com as 4 condições (passo à parte, por ordem de Andraus) · [ ] Plan da Spec de Tempo (SPEC-050, por ordem de Andraus)

---

**Andraus** — *homologação dada por AskUserQuestion, 2026-11-15; registro pelo Orquestrador.*
