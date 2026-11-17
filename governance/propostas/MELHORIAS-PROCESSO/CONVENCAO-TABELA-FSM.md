# Convenção de tabela de estados legível por máquina (P16; BL-045)

> **Procedimento do Especificador, não norma.** Vale para Plan novo que traga máquina de estados; lida por `scripts/fsm_check.py` (Detector informativo, `DHR-RETRO-004`).

1. **Uma tabela D5** com cabeçalho contendo as colunas `ID`, `Estado`, `Evento`, `Próximo` e, quando houver, `Ação` e `Código`. Nome livre depois da primeira palavra (`Guarda (D)`, `Código (…)`).
2. **Estados, eventos e códigos entre crases e em MAIÚSCULAS** (`` `AGUARDANDO` ``, `` `ALARM_EXPIRED` ``, `` `MDC_STOP` ``). Evento com parâmetro: `` `PUB(ESTRUTURAL)` `` (vale o nome antes do `(`). Vários numa célula: separados por `·`.
3. **`—`, `qualquer`, `ENC` e texto livre não são estados.** Linha de início = `Estado` `—`; encerramento = `Próximo` `ENC`; ausência de transição = `(sem transição)`.
4. **Cada linha tem ID `Fnn`** (com sufixo de letra se for desdobrada: `F08a`).
5. **Cenário (`### Cenário-…`) e adversarial (`### ADV-…`)** citam a linha percorrida com `fsm_row` seguido dos IDs (`fsm_row == F15`, `fsm_row: F03`) e os códigos/eventos pelo nome exato da tabela.
6. **Efeito com falha possível** tem linha de falha própria; o Plan declara o par `verbo=EVENTO_DE_FALHA` que o Orquestrador passa a `--efeitos`.
7. **Pré-condição** de cada cenário: linha `DADO` com fixture declarada numa seção `## Fixture …` (`scripts/cenario_precondicao.py`).

Uso pelo Orquestrador: `python scripts/fsm_check.py <plan.md> --efeitos "despacha=DISPATCH_PUBLISH_FAILED" --aciclico`; `python scripts/cenario_precondicao.py <plan.md>`. Achado é matéria do Revisor; o detector não decide.
