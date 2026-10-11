# SPEC-EX-C — Manager Agent, Conviction e Síntese (documento de teste)

| Campo | Valor |
|---|---|
| Complexidade | HIGH |
| Profundidade | D0–D7 |
| Profile | standard |
| Referências | <<REF-05|DHR-SPEC003-001|DHR-SPEC030-001>>, <<REF-06|DHR-ARQ-002|DHR-ARQ-020>> |

## 1. Papel do Manager
O Synthesis Agent <<SEM-08|foi absorvido pelo Manager Agent|permanece como agente separado, depois do Conviction Engine>>. O Manager invoca o mecanismo de cálculo do Conviction Vector; a SPEC-003 <<SEM-11|fornece o mecanismo e não o invoca|invoca o mecanismo a cada candle>>.

## 2. Conviction Vector
O vetor tem <<NUM-10|8|9>> dimensões: <<REG-14|estrutural, geométrica, fractal, institucional, operacional, temporal, volume, histórica|estrutural, geométrica, fractal, institucional, operacional, temporal, volume, custo>>.

O regime de mercado <<SEM-09|é a dimensão temporal; não é gate nem veto|é um gate: regime adverso veta o sinal>>.

O CCM-001 foi baselined em <<NUM-12|2026-10-02|2026-09-02>>. Os pesos por ativo (N-001) <<REG-15|seguem em aberto|foram fechados com pesos iguais para BTC, XAU e NASDAQ>>. Os limiares de Fase Piloto são <<SEM-12|recalibráveis após backtest|definitivos e imutáveis>>.

## 3. Prioridade dos 4Es
<<REG-16|Conformidade > Eficácia > Efetividade > Eficiência > Economicidade|Economicidade > Eficiência > Efetividade > Eficácia > Conformidade>>. Economicidade nunca fica acima de Eficácia.

## 4. Blackboard e Event Bus
O Event Bus <<SEM-10|é uma camada fina de notificação de mudança; o Blackboard guarda o estado|é a fonte de verdade do estado, e o Blackboard apenas replica>>. A SPEC-005 está em baseline <<NUM-13|v1.0|v2.0>>.

## 5. Fora de escopo
Cálculo definitivo de pesos (J-001) e execução de ordem.
