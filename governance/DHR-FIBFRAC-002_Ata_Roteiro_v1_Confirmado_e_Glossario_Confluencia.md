# DHR-FIBFRAC-002 — Ata — Roteiro v1 do despachante confirmado (DN-3) e glossário de "confluência" (Q5)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | `DHR-FIBFRAC-001` (F-1..F-4) · Plan da SPEC-008 (DN-3; RULE-MDC-002 (f): "só Andraus registra versão do grafo, a versão 1 = DN-3") · `governance/propostas/FIBONACCI-FRACTAL/INVENTARIO-E-TRATAMENTO-FIBONACCI-FRACTAL-2026-11-08.md` §5 (i), Q5 |
| Data | 2026-11-14 |
| Status | **DECISÕES REGISTRADAS** (Andraus, AskUserQuestion, 2026-11-14). Registro de decisão; não edita `WORKFLOW.md`, `GLOSSARIO.md`, baseline nem Plan; não fecha decisão aberta (CONS-01). Assinatura = decisão registrada e citada nesta ata (AGENTS.md §10). |
| Compatibilidade | Minor (confirma versão 1 de um dado versionado; nenhum modelo canônico BASELINED redefinido — CONST-01) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Registro de decisões de especificação; não altera texto de agente de construção nem método. |

## 1. Decisões de Andraus `[FATO]` (AskUserQuestion, 2026-11-14)
| # | Pergunta | Decisão |
|---|---|---|
| DN-3 | Confirmar o roteiro versão 1 do despachante: Elliott, depois SMC (se o Elliott viu oportunidade), depois ICT (se o alarme tocar), com Fibonacci como skill e não como etapa e a confluência fractal ainda sem decisão | **Confirmar o roteiro v1** (opção recomendada) |
| Q5 | Registrar no glossário os vários sentidos de "confluência" | **Sim, registrar os sentidos** (opção recomendada) |

## 2. Leitura e efeitos `[INFERÊNCIA]` do Orquestrador
- **DN-3:** o grafo `dispatch_graph` **versão 1** = ESTRUTURAL (Elliott) →[OPORTUNIDADE_SIM] INSTITUCIONAL (SMC) →[MACRO_CONCLUSIVA_E_DISPARO_NA_JANELA] OPERACIONAL (ICT), sem nó de Fibonacci/Fractal, passa a ser **versão registrada por Andraus** (RULE-MDC-002 (f) do Plan). A DN-3 deixa de ser `[DECISÃO NECESSÁRIA]` no Plan; o texto do Plan será ajustado na próxima rodada de revisão (não é editado por esta ata). **Não** decide a confluência fractal (segue "decidir depois"), nem a skill de Fibonacci.
- **Q5:** a **proposta de texto** dos sentidos de "confluência" é a do inventário §5 (i); **não foi aplicada** ao `GLOSSARIO.md` (documento de governança: edição só por ordem expressa de Andraus). A aplicação (e eventual erratum) é passo à parte.

## 3. O que esta ata NÃO afirma
- Não edita o Plan (o Revisor está na R2 sobre o commit `366af09`), `WORKFLOW.md`, `GLOSSARIO.md` nem baseline. Não decide DN-1 (rótulo do ciclo encerrado, com a SPEC-014), a localização da confluência fractal, a forma da skill de Fibonacci nem a reconciliação de WF-R01 (CF-D).
- A homologação do Plan continua sendo ato de Andraus.

## 4. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4 · BL-026 · P-13 · localização da confluência fractal · DN-1. **Nenhuma decisão aberta é fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] Decisões de Andraus (AskUserQuestion 2026-11-14) · [x] ROADMAP · [x] CATALOGO · [x] RPSA · [ ] Plan (texto da DN-3, na próxima rodada) · [ ] GLOSSARIO (só por ordem de Andraus) · [ ] merge (PR, CI verde — assinatura)

---

**Andraus** — *decisões dadas por AskUserQuestion, 2026-11-14; registro pelo Orquestrador.*
