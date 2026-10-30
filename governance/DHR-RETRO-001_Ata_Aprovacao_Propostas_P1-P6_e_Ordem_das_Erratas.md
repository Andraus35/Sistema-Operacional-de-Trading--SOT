# DHR-RETRO-001 — Ata de Decisão — Propostas P1–P6 das retrospectivas e ordem das erratas/emenda

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | Respostas de Andraus às perguntas do Orquestrador (chat, 2026-10-25) · `governance/aprendizado/RETROSPECTIVAS.md` (P1–P6) · `DHR-SPEC007-005` (H-2) · `DHR-SPEC048-001` (Q-7) · `AGENTS.md` §10, §12 |
| Data | 2026-10-25 |
| Status | **DECISÃO REGISTRADA** (decisão direta de Andraus em chat; AGENTS.md §10). Não homologa nenhuma errata/emenda: cada uma segue o fluxo Especificador → Revisor → homologação. |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Decisão de processo e ordem de serviço: não altera texto de agente de construção nem método. |

## 1. Decisões de Andraus `[FATO]`
| Item | Decisão |
|---|---|
| P1–P6 (retrospectivas SPEC-007/SPEC-048) | **Aprovadas todas.** Entram em vigor como prática do Orquestrador nas ordens de serviço (P1, P2, P5, P6) ; P3 (âncora por ID+hash) e P4 (histórico em arquivo à parte) que exigem mecanismo/gate seguem como **proposta a especificar**, com `governance/MECANISMOS.json` no mesmo PR, quando executadas |
| Próxima frente | **Todas as erratas:** (1) errata aditiva à SPEC-006 (E-1..E-4); (2) emenda à SPEC-020 (metade F1; F2 vai com a SPEC-048); (3) errata de re-apontamento (regra de busca da ata `DHR-SPEC048-001`, Q-7) |

## 2. Execução `[FATO]`
Uma de cada vez, nesta ordem, cada uma com Revisor e homologação própria de Andraus. Nenhum baseline é editado antes da homologação da respectiva errata. A SPEC-049 não é aberta.

## 3. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. Nenhuma foi fechada.

## 4. Adendo — respostas de Andraus sobre a errata da SPEC-006 (chat, 2026-10-25) `[FATO]`
| Pergunta | Resposta |
|---|---|
| Q-1 (E-1) | Só o caminho (b) (conhecimento formado via selo) |
| Q-2 | Incluir `publication` no registro de relação |
| Q-3 | Conferir `supersedes` contra o selo |
| Q-4 | Não exigir selo ainda RESERVADO |
| Q-5 | `SEAL_REF_UNRESOLVABLE` (selo não resolvido) + `SEAL_CONTENT_MISMATCH` (reaproveitado da SPEC-007) |
| Q-6 | `content_claim_ids[]` fora do hash (ponteiro de auditoria) |
| Q-7 | Marca de inferência na consulta: não nesta errata |
| Q-8 | Arquivo à parte + ponteiro de uma linha |
| Q-9 | Major |
Q-10 (inclusão de `relation_type`/formato `from`/`to`/`natural_key`/`valid_from` em M) e o código `SEAL_SUCCESSION_MISMATCH` (proposta do Especificador) **seguem pendentes**. Nenhuma errata está homologada; K-001 e demais decisões abertas seguem abertas (CONS-01).

## 5. Adendo 2 — Q-10 e código de troca (chat, 2026-10-25) `[FATO]`
**Q-10:** `relation_type` entra em M; `natural_key` e `valid_from` ficam fora de M (atribuídos pelo KG). **Código de troca:** adotar `SEAL_SUCCESSION_MISMATCH` para `supersedes` divergente do selo. Efeito na errata: v1.1 em revisão será ajustada (v1.2) após o parecer; nenhuma errata homologada; decisões abertas seguem abertas (CONS-01).

## 6. Adendo 3 — Q-10 (b), Q-11 e nome do código (chat, 2026-10-25) `[FATO]`
**Q-10 (b):** forma dos campos-ponteiro em M = regra do Mapa de formato (mesmo selo → `formation.record_ref` do alvo; alvo já no grafo → id do grafo literal; alvo ausente → recusa). **Q-11:** item 4 (b) adotado — selo que declara troca que o registro não traz ⇒ recusa. **Código:** `SEAL_RECORD_NOT_IN_SEAL` confirmado. Errata em v1.2 com parecer R3 CONFORME condicional; ajustes N1/N4 e atualização dos pendentes seguem para a v1.3; **nenhuma errata homologada**; decisões abertas seguem abertas (CONS-01).

## 7. Adendo 4 — respostas sobre o ERRATUM-SPEC020-002 (chat, 2026-10-30) `[FATO]`
| Pergunta | Resposta de Andraus |
|---|---|
| Q-3 (alcance / Minor×Major) | **Só daqui em diante** (prospectiva): "Teremos uma etapa futura de revisão das specs pretéritas." Classificação proposta pelo Especificador: Minor (a confirmar na homologação). A revisão das Specs já homologadas é intenção futura de Andraus, **sem ordem nem escopo definidos** — não é decisão aberta nova, nem foi ordenada |
| Q-2 (estado do F1) | Critério definido, limiares em aberto (INDETERMINADO); o Revisor dá o veredito como detector até existir gate |
| Q-4 (forma de aplicação) | Arquivo à parte + uma linha no plano da SPEC-020 |
| Q-7 (calibração do F1) | Só registrar a lacuna (dependência de futura errata da SPEC-007) |
Q-1, Q-5, Q-6, Q-9 seguem para a homologação. **Nenhuma errata/emenda homologada por este adendo**; decisões abertas seguem abertas (CONS-01).

## 8. Adendo 5 — respostas sobre o ERRATUM-REAPONT-001 (chat, 2026-10-30) `[FATO]`
| Pergunta | Resposta de Andraus |
|---|---|
| Q-2 (classificação) | **Patch** (ajuste editorial) |
| Q-1 (forma) | **Um arquivo único**, com uma linha de ponteiro no fim de cada plan.md afetado |
| Q-3/Q-4 (extensão) | **Incluir** a SPEC-021 (leitura estendida da regra de busca) e o trecho da SPEC-006 sobre a duplicação EXP-SPEC-021↔RAG-SPEC-018 (adiada) |
| Q-8 (ROADMAP) | **Sim**: nota aditiva no ROADMAP na mesma homologação (duas linhas, texto anterior preservado); CONFLICT-MAP só por ordem dele |
Q-5, Q-6, Q-7 seguem com a premissa do texto até a homologação. **Nenhuma errata homologada por este adendo**; decisões abertas seguem abertas (CONS-01).
