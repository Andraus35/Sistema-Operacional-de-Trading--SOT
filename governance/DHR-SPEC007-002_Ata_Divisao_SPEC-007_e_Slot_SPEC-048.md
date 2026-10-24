# DHR-SPEC007-002 — Ata de Decisão — Divisão da SPEC-007 (Opção C) e slot da SPEC-048

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-007/ABERTURA.md` §3-§4 (cláusula de divisão, `SPEC-007-SPLIT-001`) · `specs/features/SPEC-007/research.md` §8.1-§8.2 · `DHR-SPEC007-001` (abertura homologada, Q2) · Plan v1.2 candidato `specs/features/SPEC-007/plan.md` · pareceres do Revisor `governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-PLAN-R1-2026-10-23.md`, `...-R2-2026-10-23.md`, `...-R3-2026-10-24.md` |
| Data | 2026-10-24 |
| Status | **DIVISÃO DECIDIDA** (decisão direta de Andraus em chat, 2026-10-24, por AskUserQuestion). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). A SPEC-007 permanece **sem Plan aprovado e NÃO é baseline**; a **SPEC-048 é slot indicativo — NÃO aberta, NÃO autorizada**. |
| Compatibilidade | Minor (não toca modelo canônico baselined; não edita Spec baselined; não fecha decisão aberta) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Decisão de decomposição de Spec e registro de slot: não altera texto de agente nem método. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-24)
| # | Pergunta | Decisão |
|---|---|---|
| D1 | Dividir a SPEC-007? | **Sim.** Após a 3ª rodada do Revisor sobre o Plan (NÃO CONFORME: 9 → 5 → 5 Médias, 0 Críticas), Andraus escolheu dividir em vez de seguir corrigindo uma Spec só. `SPEC-007-SPLIT-001` (proposta em `ABERTURA.md` §3 como "não dividir agora") passa a **FECHADA: dividir** |
| D2 | Qual desenho? | **Opção C da `ABERTURA.md` §3**: a SPEC-007 fica com formação + selo (o que a SPEC-006 referencia); recuperação + pacote de evidência vão para Spec nova |
| D3 | Número e nome da Spec nova | **SPEC-048 — RAG Retrieval & Evidence Packet Harness** (em português: Recuperação e Pacote de Evidência). Número livre conferido em `ROADMAP.md`/`CATALOGO`/`backlog` |
| D4 | Fronteira | **Corte da Opção C** (§3 abaixo) |
| D5 | Re-apontamentos em Specs baselined | **Só listados nesta ata (§4); errata aditiva depois**, proposta no Plan da SPEC-048 para homologação conjunta. Nenhum baseline é tocado agora |
| D6 | Escopo de edição desta entrega | **Ata + `ROADMAP.md` + `governance/CATALOGO-OFICIAL.md` + `backlog/RMR-001_Painel_Backlog.md` (BL-017)**, texto anterior preservado (INV-07). `CONFLICT-MAP.md` **não** é alterado (§6) |

## 2. Fatos que motivaram `[FATO]`
- O Plan v1.2 da SPEC-007 (20 RULE-KFH, 20 BASpec, 13 EC, 26 cenários, 29 ADV) foi reprovado 3 vezes pelo Revisor, sem Críticas; cada rodada achou camadas mais finas num texto que já excede o que cabe numa revisão (cláusula de divisão da `ABERTURA.md` §3; R-10 da §157).
- Parte dos achados da R3 incide só na trilha de consulta/pacote (R3-M5 em parte, F2, `consumer_locus`, injeção na consulta), outra só na de formação/selo (R3-M1, M2, M4) — a separação reduz o tamanho de cada revisão.

## 3. Fronteira (decisão D4) — o que fica onde
| SPEC-007 (reduzida — formação + selo) | SPEC-048 (nova — recuperação + pacote) |
|---|---|
| Entrada da fonte com proveniência e direito de uso | Busca/recuperação sobre o conhecimento **carimbado** e as fontes originais |
| Formação do candidato de conhecimento | Pacote de evidência **com citação** (cita item carimbado e fonte original, nunca a página) |
| 1ª checagem de fidelidade (F1: o conhecimento formado não inventa o que a fonte não diz) | Visão de leitura "WikiRAG" (montada por regra fixa, sem autoridade própria — Q3) |
| Validação, **selo** de publicação, marca de revalidação, sucessão | 2ª checagem de fidelidade (F2: cada frase entregue tem apoio no trecho citado) |
| Registro dos atos de autorização de Andraus (ACTREC) | Defesa contra instrução escondida no que é buscado (trilha de consulta) |
| Trava de envio de texto para fora (camada de invocação de modelo) e permissão por derivação | **Usa** a trava da SPEC-007; não a redefine |

O **mapeamento fino** de cada RULE-KFH/BASpec do Plan v1.2 a uma das duas Specs é feito nos Plans, não nesta ata. O Plan v1.2 **permanece no repositório intacto** (INV-07) como base de reaproveitamento; não é baseline.

## 4. Re-apontamentos que a divisão exige — **LISTADOS, não executados** (D5)
Conforme `research.md` §8.1-§8.2 (as linhas devem ser reconferidas no momento do erratum):
- `specs/features/SPEC-002/plan.md` (l.170/848), `SPEC-003/plan.md` (l.1080), `SPEC-006/plan.md` (l.299/341/1594): hoje "retrieval → SPEC-007" → passa a SPEC-048. **As referências ao contrato do selo e à formação continuam na SPEC-007.**
- `SPEC-020` e `ROADMAP.md` (dimensão B "RAG faithfulness", `ROADMAP.md` l.291): a dimensão se **divide** — F1 (conhecimento formado) na SPEC-007; F2 (frase entregue × trecho) na SPEC-048. Emenda pontual à SPEC-020 só na homologação do Plan correspondente, por ato de Andraus.
- **BL-017** (`backlog/RMR-001_Painel_Backlog.md`): re-apontamento **aditivo** registrado nesta entrega (§6); o gatilho original é preservado.
- Errata aditiva a SPEC-002/003/006/020: **a ser proposta no Plan da SPEC-048** e homologada por Andraus; até lá as referências antigas valem como estão.

## 5. Correção de dado `[FATO]`
`ABERTURA.md` §3 (tabela da Opção C) e `research.md` §8.1 dizem que o "SPEC-047 está reservado" para a Spec nova (cita `ROADMAP.md` l.538). Conferido: a l.538 reserva **SPEC-047 para "Runtime Cognitive Caching Harness"** (adiada, placeholder). A frase estava incorreta; o número usado para a Spec nova é **SPEC-048** (D3). `ABERTURA.md` e `research.md` **não foram editados** (preservados); esta ata é a correção.

## 6. Efeitos aplicados `[FATO]`
- `ROADMAP.md`: linha "Próximo trabalho autorizado" e tabela do §25 — SPEC-007 reduzida (Plan v1.2 candidato NÃO CONFORME, sem Plan aprovado); **SPEC-048** acrescentada como slot indicativo, abertura pendente; segmento "Decisões FECHADAS": `SPEC-007-SPLIT-001`. Texto anterior preservado.
- `governance/CATALOGO-OFICIAL.md`: registro desta ata.
- `backlog/RMR-001_Painel_Backlog.md`: nota datada em **BL-017** (parte "answer/packet faithfulness" → SPEC-048; gatilho adicional `spec:SPEC-048 em redação`); estado **inalterado** (`Em espera`). BL-010 e BL-035: **inalterados** (vinculados à abertura da SPEC-007; suas Disposições serão redeclaradas no Plan reduzido; a SPEC-048 herda o que lhe couber de BL-010 no seu Dossiê). BL-011 segue `ATIVADO`.
- `governance/CONFLICT-MAP.md` **não alterado** (COL-EXP-05 segue re-apontado à SPEC-007, `DHR-BENCH-INTEL-001` D8; reavaliar no Plan reduzido se a parte "independência de evidência" cabe só na formação).

## 7. Condições (o que esta ata NÃO afirma)
- **SPEC-048 não está aberta nem autorizada.** Antes de qualquer Plan: Dossiê de Pesquisa próprio (RULE-ECC-01/02/06, `atomic-spec.md` §15 — o `research.md` da SPEC-007 é insumo, não substitui), parecer do Revisor sobre o processo e homologação de Andraus da abertura (número, nome, peso, fronteira, perguntas).
- **SPEC-007 (reduzida) não tem Plan aprovado.** Novo Plan só por ordem expressa de Andraus; o v1.2 é o ponto de partida e as Médias R3-M1..M5 devem ser tratadas nas partes que ficarem.
- Nada aqui homologa Plan, baseline ou emenda a Spec baselined.
- O fail-closed do Plan v1.2 (nenhum selo, nenhuma fonte liberada, nenhum envio externo) continua valendo no intervalo até Andraus decidir.

## 8. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 (BL-035) · "produtor/gatilho de promoção" (SPEC-006 `plan.md` l.976) · direito de uso do livro (Q7c). As decisões **propostas** pelo Plan v1.2 como [DECISÃO NECESSÁRIA] (SPEC-007-NODETYPE-001, SUCC-001, RIGHTS-001, EXTTX-001, BBTYPE-001, ACTREC-001, DERIVTX-001) e as perguntas P-1..P-11 **seguem abertas**; esta ata não as responde. **Nenhuma decisão aberta foi fechada por esta ata**, exceto `SPEC-007-SPLIT-001` (D1).

## 9. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [x] RMR-001 (BL-017) · [ ] CONFLICT-MAP (não alterado, por D6) · [ ] merge (assinatura) · [ ] Dossiê e abertura da SPEC-048 (só por ordem de Andraus) · [ ] Plan reduzido da SPEC-007 (só por ordem de Andraus)

---

**Andraus** — *decisão em chat, 2026-10-24; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
