# DHR-SPEC006-001 — Ata de Homologação — Abertura da SPEC-006 (Cognitive Knowledge Graph)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador interno) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-006/ABERTURA.md` + `research.md` + `sources/`; parecer do Revisor sobre o processo do Dossiê: **CONFORME** (commit `1e8e8c7`); DHR-SPEC006-PEND-001 (BL-029 em espera; emenda Minor do `atomic-spec.md` §3 → CRITICAL · D0–D7) |
| Data | 2026-10-11 |
| Status | **ABERTURA HOMOLOGADA** — decisões diretas de Andraus em chat (2026-10-11), respondendo às 5 perguntas do `ABERTURA.md` §12 e confirmando o registro da homologação. **NÃO é baseline**: o Plan (`plan.md` + `checks.md`) não foi escrito e só inicia por ordem de Andraus. |
| Compatibilidade | Minor (não toca modelo canônico baselined nem fecha decisão aberta) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologa a abertura de uma Spec e registra decisoes; nao altera texto de nenhum arquivo de agente. |

## 1. Decisões `[FATO]`
| # | Pergunta | Decisão de Andraus |
|---|---|---|
| Q-ABERTURA-1 | Nome | **Manter "Cognitive Knowledge Graph"** |
| Q-ABERTURA-2 | Peso | **CRITICAL** (D0–D7 + D8 adversarial nos pontos sensíveis: imutabilidade INV-07, confiança ≠ Convicção INV-04, causalidade pós-hoc, colisão de relações), seguindo o ROADMAP §6 |
| Q-ABERTURA-3 | Como guardar (H-001) | **Fechar as REGRAS do contrato cognitivo** (o que guarda, como se consulta, quem escreve, nunca apagar) e **deixar a tecnologia de armazenamento em aberto** (Opção A). **H-001 NÃO é fechada.** |
| Q-ABERTURA-4 | Gramática do conhecimento | **Dentro da SPEC-006**, enxuta, sem componente separado |
| Q-ABERTURA-5 | Quantidade | **Uma Spec só** por enquanto; se o Plan ficar grande demais para revisar de uma vez, o Especificador volta a Andraus para propor divisão |

## 2. Efeitos `[FATO]`
Número SPEC-006 preservado; Classe predominante D (ontologia, catálogo, temporalidade, versionamento, consulta) + C (governança de escrita) + H eventual com gate de saída — declaração **por BASpec** no Plan (CC-11). CC-12 e RULE-ECC-05 não incidem (Spec de infraestrutura de memória). Dossiê com validade de **90 dias** (CRITICAL, ECC-VAL-001): limite **2027-01-03**.

## 3. Permanecem ABERTAS (CONS-01)
**H-001** (mecanismo físico do KG — decisão futura, só de Andraus) · M-001 (enum) · J-001 · N-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 4. Registro (efeitos aplicados)
- [x] Este documento · [x] `ROADMAP.md` ("próximo trabalho" e tabela §6/§5 da fase) · [x] `specs/features/SPEC-006/ABERTURA.md` (linha de Status) · [x] `governance/CATALOGO-OFICIAL.md` · [x] mapa · [ ] merge (assinatura) · [ ] RPSA automático
- Próximo gate: Plan (`plan.md` + `checks.md`, via `tlc-spec-lean`) — **somente por ordem de Andraus**.

---

**Andraus** — *decisões em chat, 2026-10-11; registro feito pelo Orquestrador interno a pedido de Andraus. Assinatura = merge desta ata.*
