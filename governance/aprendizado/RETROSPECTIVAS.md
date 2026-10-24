# RETROSPECTIVAS DE FECHAMENTO DO LOOP DOS CONSTRUTORES (LOOP-001 / DHR-LOOP-001)

> **Regra (ordem de Andraus, 2026-10-24):** o tratamento de melhoria — **individual** (Especificador, Revisor, Orquestrador) e **coletivo** (o loop entre eles) — ocorre **ao fim do trabalho completo de uma Spec e ANTES de abrir outra Spec** (Dossiê/abertura/Plan). A coleta de dados (ledger, causas, prevenção) é contínua; o **tratamento** é aqui. Append-only (INV-07). O Orquestrador roda `python scripts/loop_ledger.py --retro-check SPEC-nnn` de cada Spec fechada antes de abrir outra; sem `FEITA`, não abre (salvo dispensa expressa de Andraus).

Linha-índice (lida pelo script; Estado `FEITA` só quando a seção correspondente abaixo estiver completa): `| SPEC-nnn | resumo | data | FEITA |`

| Spec | Escopo | Data | Estado |
|---|---|---|---|
| SPEC-007 | Plan reduzido homologado (DHR-SPEC007-005); 6 rodadas de Plan + 3 de abertura | 2026-10-24 | PENDENTE |
| SPEC-048 | Abertura homologada (DHR-SPEC048-001); Plan em revisão | 2026-10-24 | PENDENTE |

## Roteiro de cada retrospectiva (checklist; todo item exige evidência do ledger ou do parecer)
1. **Dados:** rodar `loop_ledger.py`; copiar Médias por rodada, rodadas até 0 Média, categorias recorrentes e lacunas de prevenção da Spec; % de achados resolvidos por classe M (economia de rodada).
2. **Individual — Especificador:** padrões de erro próprios (categorias C01..C10), o que o fez reincidir, o que teria evitado (instrução de serviço, checklist, gate).
3. **Individual — Revisor:** severidades desalinhadas, achados reabertos de decisão já tomada, o que não pôde verificar (gate, git, web), tempo/rodadas.
4. **Individual — Orquestrador:** o que escapou aos gates e foi achado tarde, classe M não usada, estados perdidos entre sessões, ordens ambíguas.
5. **Coletivo — o loop:** nº de rodadas, cascatas de correção, handoffs entre agentes, custo evitável (4Es: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade).
6. **Propostas de melhoria** (gates/processo/instruções), cada uma com: problema → evidência → proposta → 4Es afetados → custo; **só viram mecanismo por ordem expressa de Andraus** (com `governance/MECANISMOS.json`). Registrar a decisão dele (aprovada/adiada/rejeitada).
7. Atualizar `CAUSAS-PREVENCAO.md` e marcar a linha-índice como `FEITA` com a data.

<!-- Entradas de retrospectiva abaixo (uma seção por Spec), append-only -->
