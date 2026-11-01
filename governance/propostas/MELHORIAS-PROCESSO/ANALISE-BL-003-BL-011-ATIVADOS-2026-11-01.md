# Análise — BL-003 e BL-011 "ATIVADOS" (nada promovido, nada alterado)

> **Não normativo.** Pedido por Andraus (AskUserQuestion, 2026-11-01: "Analisar e propor"). **Não promove nem descarta nenhum item** (`Absorvido`/`Descartado` são só de Andraus, RMR-001 §5). Não fecha decisão aberta (CONS-01).

## 1. Achado principal
O aviso "ATIVADOS (2) — exigem encaminhamento no gate" do `backlog_triggers.py` aparece em todo gate desde 2026-10-17, **mas o encaminhamento já foi feito**: Andraus ativou os dois (DHR-BACKLOG-001, chat 2026-10-17) mandando tratá-los no gate da SPEC-006, e a SPEC-006 (**BASELINE**, DHR-SPEC006-002; v1.7 + erratas) os tratou com Disposição declarada no Plan, como o `[STRUCT-13]` exige. O que resta não é encaminhamento: é o **Estado final** do item, que é de Andraus.

## 2. Situação por item (fontes lidas nesta sessão)
| Item | Disposição no Plan da SPEC-006 | O que sobra | Gatilhos ainda pendentes |
|---|---|---|---|
| **BL-003** persistência física de hipótese/estado | **PARCIAL** — incorporado o contrato LÓGICO do KG (RULE-CKG-*); **fora** a parte física | Mecanismo físico do KG: **FECHADO** (H-001, Opção C, DHR-H001-001). **Estado persistente por agente: G-001 ABERTA** | `spec:SPEC-009 em redação` |
| **BL-011** MC-EXP-001 | **PARCIAL** — incorporado o que é memória semântica permanente (por referência a RULE-CKG); **fora** memória episódica/experiência | COL-EXP-05 / R-07 **ADIADOS** para SPEC-007/009; episódica → SPEC-018/K-001 | `spec:SPEC-009 em redação`, `milestone:FASE 3 iniciada` (já ocorrida) |

## 3. Proposta (decisão de Andraus)
1. **Manter os dois `ATIVADO`** por enquanto: a parte que ficou "fora" depende de G-001 (aberta), da SPEC-009 e da SPEC-018/K-001. Marcar `Absorvido` agora seria fechar por inferência (o enum do painel não tem "parcialmente absorvido").
2. **Nenhuma ação nova** sobre BL-003/BL-011 até a SPEC-009 entrar em redação; nesse gate eles voltam por regra (`DHR-BACKLOG-ABERTURA-001`).
3. **Opcional (ruído, mesma lição do A6.4):** o `backlog_triggers.py` poderia listar "ATIVADO com Disposição já declarada em Plan homologado" numa seção à parte, em vez de repetir "exigem encaminhamento". Exige mexer em arquivo selado (`GATE-MANIFEST`, CODEOWNERS); **ganho pequeno, não recomendo agora**.

## 4. O que isto NÃO diz
Não fechei G-001, K-001 nem qualquer decisão aberta; não avaliei se a Disposição PARCIAL de cada item foi a melhor (foi homologada pelo Revisor e por Andraus); BL-010/015/017/035 ("disparados sem registro") **não** foram analisados aqui.
