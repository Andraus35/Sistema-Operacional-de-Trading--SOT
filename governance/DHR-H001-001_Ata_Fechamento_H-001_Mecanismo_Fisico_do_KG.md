# DHR-H001-001 — Ata — Fechamento da decisão H-001 (mecanismo físico de armazenamento do Cognitive Knowledge Graph)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | Estudo `governance/propostas/H001/ESTUDO-TECNOLOGIA-H001-2026-10-18.md` ([PROPOSTA] do Especificador, classe O); SPEC-006 baseline v1.7 + errata v1.11 (DHR-SPEC006-002/-003); `ROADMAP.md` §6 |
| Data | 2026-10-18 |
| Status | **DECISÃO DE ANDRAUS REGISTRADA (chat, 2026-10-18, AskUserQuestion):** escolha da **Opção C**, autorização de edição dos arquivos protegidos listados no §3 e equivalência da licença PostgreSQL à classe BSD/MIT da régua Equilibrada. Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). |
| Compatibilidade | **Minor / aditiva (INV-07).** Escolhe o COMO físico; o QUE (RULE-CKG-001..013, INV-CKG-01/02, EC-CKG-001..006) da SPEC-006 homologada **não muda**. Nada é apagado: o texto "H-001 ABERTA" fica como registro histórico nas atas e no changelog. |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Fecha a decisão H-001: revisor.md §8 e especificador.md deixam de listá-la como bloqueador aberto. |

## 1. Decisões de Andraus `[FATO]` (chat, 2026-10-18)
| # | Item | Decisão |
|---|---|---|
| D1 | Tecnologia do mecanismo físico do KG (H-001) | **Opção C — PostgreSQL como fonte única de verdade**, com registros **só-inserção (append-only)**, colunas **bitemporais** explícitas (`valid_from`/`valid_to`/`recorded_at`/`formulated_at`) e travessia por consultas recursivas no próprio banco |
| D2 | Evolução | Caminho para a **Opção D** (índice de grafo derivado e reconstruível) **desenhado, não ligado**: só entra se a eficiência de consulta multi-salto medida no BUILD exigir |
| D3 | Licença | A *PostgreSQL License* é tratada como **equivalente a BSD/MIT** na régua Equilibrada (RULE-ECC-06); decisão de Andraus, registrada aqui; a régua em si não é alterada |
| D4 | Arquivos protegidos | Autorizados: ROADMAP, `AGENTS.md` §7, `atomic-spec.md` §12, `.claude/agents/revisor.md` §8, `.claude/agents/especificador.md`, CATALOGO, CIC-001, RMR-001 e errata da SPEC-006 (referências ao mecanismo físico) |
| D5 | Cláusula de revisão por gatilho | A escolha é **revisitada no início do BUILD do KG** (medição de consulta multi-salto, licença/manutenção do PostgreSQL, existência do Blackboard em outro motor — G-001/SPEC-004) |

## 2. Descartadas `[FATO — do estudo, §2 da proposta]`
Graphiti/Zep (invalida arestas por chamada a LLM — contradiz RULE-CKG-004 e ENF-03) · grafo nativo Memgraph (BSL) e FalkorDB (SSPL) fora da régua · Kùzu arquivado em 2025-10-10 · XTDB v2 (nota 68,2) · Opção D como ponto de partida (89,0 × 91,0 da C).

## 3. O que muda `[FATO]`
- `ROADMAP.md`: H-001 sai de "Decisões abertas ativas" e entra em "Decisões FECHADAS"; linhas da SPEC-006 (§6 e tabela) passam a referir a escolha.
- `AGENTS.md` §7, `atomic-spec.md` §12, `revisor.md` §8, `especificador.md`: H-001 deixa de ser bloqueador aberto (a SPEC-006 deixa de ter o teto "CONFORME condicional" **por causa da H-001**; a negação de `conviction` por padrão e demais condições da DHR-SPEC006-003 permanecem).
- `CATALOGO-OFICIAL.md`, `CIC-001`, `RMR-001`: registros alinhados.
- SPEC-006 (errata): o estado "mecanismo físico INDETERMINADO" passa a "decidido: Opção C (DHR-H001-001)", sem alterar regra/BASpec/EC do contrato lógico; texto histórico preservado (INV-07). Revisor por delta nos blocos alterados; homologação da errata é ato à parte de Andraus.
- Specs já homologadas que citam H-001 como aberta (SPEC-002/004/038 etc.) **não são reescritas** (INV-07; texto histórico); a fonte de verdade do estado é o ROADMAP.

## 4. Limites honestos `[FATO]`
- O estudo é [PROPOSTA]; a decisão é só a tabela do §1. Incertezas do estudo seguem vivas: qual motor guarda o log do Blackboard (G-001, SPEC-004) e eficiência de consulta multi-salto (medida só no BUILD).
- Não há BUILD nesta fase (spec-first): nenhuma instalação, esquema físico ou código é criado por esta ata.
- Fechar a H-001 **não** fecha G-001 (estado persistente por agente), M-001, J-001, N-001, K-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001 nem BL-003 (`Absorvido` é de Andraus).

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · RULE-REG-001 (conforme ROADMAP). **Fechada por esta ata: H-001.**

## 6. Registro
- [x] Esta ata · [x] ROADMAP · [x] AGENTS §7 · [x] atomic-spec §12 · [x] revisor.md / especificador.md · [x] CATALOGO / CIC / RMR-001 · [ ] errata SPEC-006 + Revisor por delta · [x] RPSA · [ ] merge (assinatura)

---

**Andraus** — *decisão em chat, 2026-10-18; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
