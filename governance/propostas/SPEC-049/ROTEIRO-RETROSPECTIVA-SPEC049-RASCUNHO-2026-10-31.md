# Roteiro (RASCUNHO) — retrospectiva de fechamento da SPEC-049

> **Não normativo. NÃO é a retrospectiva.** Andraus decidiu "**aguardar rodada real**" (HANDOFF; ata `DHR-SPEC049-002` §3): a retrospectiva da SPEC-049 **não foi feita** e **não está marcada `FEITA`** — `python scripts/loop_ledger.py --retro-check SPEC-049` segue acusando PENDENTE. Este arquivo só adianta o **item 1 (dados)** do roteiro de `governance/aprendizado/RETROSPECTIVAS.md` e deixa os itens 2–6 como perguntas com ponteiro de evidência, para quando houver a rodada real. Nada aqui fecha decisão (CONS-01) nem vira mecanismo sem ordem de Andraus.

## 1. Dados (fatos, do ledger e do HANDOFF)
| Fase | Rodadas | Médias por rodada | Menores por rodada | Observação |
|---|---|---|---|---|
| Abertura | 3 | 1 → 0 → 0 | 8 → 2 → 1 | R1 integral, R2 integral (15/20 blocos mudaram), R3 delta |
| Plan v1.2 | 3 | 3 → 0 → 0 | 8 → 7 → 4 | corpo **1.583 linhas** (teto RULE-ECC-07: alerta 1.900 / teto 2.000); 0,19 Médias por 100 linhas; R2 e R3 por delta |
- **Tokens de subagentes** (HANDOFF/telemetria): abertura **906.237** (Esp. 250.105+132.967+110.274; Rev. 172.341+134.928+105.622); Plan **1.389.735** (Esp. 408.246+222.488+156.058; Rev. 234.891+188.916+179.136); **total ≈ 2,30 M**. Delta custou 20–40% menos que integral (n pequeno).
- **Categorias recorrentes (ledger global na época):** C07 citação/âncora (39) · C01 contradição interna (28) · C02 ambiguidade (24). Lacunas de prevenção abertas: C99, C01, C06, C03, C10.
- **Classe M** (economia de rodada): uso nesta Spec = **a levantar** no parecer/`ficha M` (o ledger não o consolida; marcar "n/m" se não houver registro).
- **Fecho:** Plan v1.2 BASELINE (`DHR-SPEC049-002`) com 3 Menores (R3-m01, m03, m04) deixados "**na construção**" por decisão de Andraus — ou seja, a regra "Menores não abrem rodada" já foi praticada de fato no fim.

## 2–5. Perguntas para a rodada real (preencher só com evidência do ledger/parecer)
2. **Especificador:** quais categorias reincidiram da abertura para o Plan (C07/C01)? A tabela fato→locais (P2) foi usada na ordem de serviço? Quanto do custo de 408 mil tokens do Plan R1 foi redação nova vs. correção?
3. **Revisor:** alguma severidade desalinhada entre R1 do Plan (3 Médias) e R2/R3 (0)? Algum achado reabriu decisão já tomada? O delta com `SHA256-ALVO` foi declarado nas 3 rodadas do Plan (ledger 2-ter)?
4. **Orquestrador:** o que escapou aos gates e foi achado tarde? Houve colisão de cadeia de handoff entre sessões em paralelo (sim: HO-110..122 duplicados com o ramo da auditoria; resolvido por `docs/handoffs/ramo-*`)?
5. **Coletivo:** 3 rodadas por fase foi o mínimo viável? A regra de parada proposta (`PROPOSTA-EXPERIMENTO-REGRA-DE-PARADA-2026-10-31.md`) teria mudado alguma coisa aqui — o fim já foi praticamente esse comportamento.
6. **Propostas:** só depois dos itens 2–5; cada uma com problema → evidência → proposta → 4Es → custo; decisão de Andraus registrada.

## 7. Para fechar
Quando Andraus liberar: preencher 2–6 em `RETROSPECTIVAS.md` (seção "Retrospectiva SPEC-049"), atualizar `CAUSAS-PREVENCAO.md`, marcar a linha-índice `FEITA` com a data e rodar `loop_ledger.py --retro-check SPEC-049` (deve sair OK).
