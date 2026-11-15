# TELEMETRIA DE TOKENS DOS CONSTRUTORES — retrato (gerado por `python scripts/telemetria_tokens.py snapshot`)

> Dado de estado, NÃO normativo (BL-036 / DHR-TELEMETRIA-CUSTO-001). **Detector (ENF-03)**: não bloqueia, não fecha decisão aberta. Custo fora do Conviction Vector (INV-04). Tokens ≠ qualidade (CEE-001): ler junto de Eficácia, nunca isolado. Retrato de 10 chamada(s) em 2026-11-15; custo = EQUIVALENTE a preço de tabela da API, NÃO cobrança (no plano Pro o custo marginal é zero); preços em `governance/telemetria/PRECOS-MODELOS.json` (null => INDETERMINADO).

| Agente | Modelo | Classe | Chamadas | Tokens total | Tokens/chamada | in | out | cache lido | cache criado | Custo equivalente API (USD) |
|---|---|---|---|---|---|---|---|---|---|---|
| Especificador SOT | opus | O | 5 | 10497207 | 2099441 | 656 | 470715 | 72005015 | 10025836 | 73.9471 |
| Revisor SOT | opus | S3 | 4 | 777825 | 194456 | 194 | 120975 | 13180445 | 656656 | 8.3396 |
| Revisor SOT | sonnet | S2 | 1 | 296063 | 296063 | 40 | 53037 | 2952404 | 242986 | 1.4332 |
