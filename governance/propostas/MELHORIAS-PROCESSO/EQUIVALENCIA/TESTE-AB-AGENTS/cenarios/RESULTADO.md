# Teste de cenários (aplicação de regras) — AGENTS.md original (A) × atual (E)

> **Não normativo. Evidência de apoio.** 2026-10-31. Haiku, só `Read` no documento + cenários, 12 cenários de decisão (não de busca de fato), 2 réplicas por variante, gabarito por script (sem juiz de LLM). Ver também `../RESULTADO.md` (teste de achabilidade).

## Por que não testei o Especificador/Revisor de verdade
Qualquer subagente recebe o `AGENTS.md` **atual** injetado no contexto pelo harness, então não dá para isolar a variante antiga numa rodada real dentro desta sessão (viés de contaminação). A versão viável é este teste de **aplicação de regras em cenários**. O teste de comportamento completo exigiria uma sessão separada com o `AGENTS.md` antigo no diretório de trabalho — não feito.

## Resultado
| Variante | Placar com o gabarito pré-registrado (v1) | Placar com o gabarito estrito (v2, pós-hoc) |
|---|---|---|
| A (original, 29.427 B) — réplica 1 e 2 | 12/12 · 12/12 | **11/12 · 11/12** (falha S3) |
| E (atual, 18.803 B) — réplica 1 e 2 | 12/12 · 12/12 | **12/12 · 12/12** |

**Honestidade do método:** o gabarito v1 foi escrito antes e tinha um defeito (o regex da S3 casava "Orquestrador" mesmo em "o Orquestrador **não** corrige"), por isso dava 12/12 a todos. Eu o corrigi **depois** de ver as respostas (v2); os dois placares estão acima, e a mudança só afeta a S3.

## O achado
Na **S3** (quem corrige um achado MENOR mecânico?), a regra vigente do §12 passo 0 (`DHR-ROTEAMENTO-006`) é: o **Orquestrador**, por ficha M. O `AGENTS.md` original ainda trazia, dentro do mesmo item, o texto **superado** (`DHR-ROTEAMENTO-005`: "o Orquestrador NÃO corrige achados do Revisor — de nenhuma severidade"). **As duas réplicas de A seguiram o texto superado e erraram; as duas de E, sem ele, acertaram.** Ou seja, o corte do texto intermediário superado (parte do `DHR-AGENTS-CORTES-001`) **melhorou** a Eficácia neste cenário, em vez de arriscá-la — o texto "preservado por INV-07" funcionava como armadilha para o leitor. (INV-07 segue cumprido pelo arquivo morto e pelo git.)

## Limites
n=2 por variante, um modelo pequeno, 12 cenários escritos por mim, gabarito corrigido pós-hoc. É indício direcional, não prova estatística; a direção (menos texto superado ⇒ menos erro) é plausível e coerente com a causa C01 (contradição interna) do ledger. Mede só leitura do `AGENTS.md`; não mede o Especificador/Revisor completos.
