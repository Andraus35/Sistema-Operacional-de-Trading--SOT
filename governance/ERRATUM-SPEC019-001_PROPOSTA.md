# ERRATUM-SPEC019-001 — Correção aditiva do status de L-001 na SPEC-019 homologada (PROPOSTA)

> **Nota de higiene (2026-10-31, `DHR-HIGIENE-002`; ordem de Andraus no chat):** *status de homologação NÃO CONFIRMADO* neste repositório — não localizei ata nem registro no `CATALOGO-OFICIAL.md` que o homologue ou o descarte; ele é citado por outros errata apenas como "padrão" de erratum aditivo. Conferir com Andraus antes de tratá-lo como vigente ou descartado. Esta nota não altera o texto abaixo.

| Campo | Valor |
|---|---|
| Código | **ERRATUM-SPEC019-001** (candidato — atribuição final = Controlador) |
| Versão | v1 |
| Natureza | **Erratum editorial e aditivo** a uma Spec **HOMOLOGADA — BASELINE**. Não reabre a Spec, não altera obrigação, invariante, BASpec nem critério de aceite. |
| Compatibilidade | **Patch / editorial** (nenhum objeto removido ou reescrito — INV-07). Classificação final = parecer do Revisor. |
| Status epistemológico | **PROPOSTA — nada aplicado.** Nenhum arquivo de baseline foi alterado. `[FATO]` = verificado nos arquivos citados; `[PROPOSTA]` = o que se pede. |
| Autoria | Especificador (Claude Code), 2026-09-27 |
| Alvo | `specs/features/SPEC-019/plan.md` (apêndice ao final; `checks.md` **não** é editado) |
| Fundamento | RULE-HG-01 (trio) · RULE-HG-05 (versionamento monotônico) · RULE-HG-08 (registro por DHR) · INV-07 · INV-09 · CONS-01 · DHR-SPEC019-001 |

---

## 0. Origem e diagnóstico `[FATO]`

A SPEC-019 foi homologada em 2026-09-22 (DHR-SPEC019-001), fechando a decisão **L-001** na dimensão spec-time. O cabeçalho do `plan.md` já foi atualizado (linha 13: "**FECHADA na homologação**"), mas **o corpo manteve enunciados do estágio de proposta**, criando **contradição interna** no baseline e com o ROADMAP, o AGENTS.md §7 e a ata:

- `plan.md`:76, :593, :595, :673, :695, :736, :743 dizem que a resolução é "proposta" / "em aberto" / "não fechada aqui".
- `checks.md`:90 e :129 idem (o primeiro era verdadeiro *à data da entrega*).
- Foi detectado (a) pelo verificador de referências/estrutura durante a sessão de 2026-09-26 e (b) pelo parecer do Revisor sobre a EUA-E22 (OBS-01, relativa ao AGENTS.md §7, já corrigida). O `validate_spec_sot.py` (STRUCT-10) agora **passa** na SPEC-019 (corrigido em 2026-09-26); o erratum trata apenas da incoerência **textual** remanescente.

Por RULE-HG-01, baseline não é editado diretamente: a correção percorre o trio e é **aditiva**.

## 1. Texto proposto (apêndice ao final de `plan.md`) `[PROPOSTA]`

---

## Erratum pós-homologação — ERRATUM-SPEC019-001 (status de L-001)

[FONTE: DHR-SPEC019-001 (2026-09-22); ROADMAP.md — linha "Decisões FECHADAS"; AGENTS.md §7]

**Natureza:** erratum **aditivo e editorial** (INV-07; RULE-HG-05). O texto acima **permanece intacto** como registro do estágio de proposta e **não é reescrito**. Nenhuma obrigação, invariante, BASpec ou critério de aceite é alterado.

**Leitura vigente:** a decisão **L-001** foi **FECHADA** na homologação desta Spec (Andraus, 2026-09-22, DHR-SPEC019-001), na dimensão **spec-time**. A governança de **runtime** não é resíduo de L-001: pertence à SPEC-018 e à decisão K-001 (decisão aberta). A decisão L-001-b (fronteira spec-time × runtime) foi **resolvida por Andraus em 2026-09-22**.

**Enunciados de estado superados por esta leitura** (todos do estágio de proposta; ler "resolução proposta" como "resolução efetivada na homologação"):

| Local | Enunciado original (resumo) | Leitura vigente |
|---|---|---|
| `plan.md`, escopo NEW (linha 76) | "Resolução (proposta) de L-001" | Resolução efetivada na homologação |
| `plan.md`, "Resolução de L-001" (linhas 593 e 595) | "propõe sua resolução"; "até lá, L-001 permanece formalmente em aberto" | Efetivada em 2026-09-22 (DHR-SPEC019-001) |
| `plan.md`, tabela de decisões (linha 673) | L-001 "EM ABERTO — esta Spec propõe resolução" | **FECHADA** (spec-time) |
| `plan.md`, tabela de status (linha 695) | "Resolução de L-001 — [PROPOSTA] — efetiva na homologação" | Efetivada; deixa de ser [PROPOSTA] |
| `plan.md`, Bloco D e decisões registradas (linhas 736 e 743) | "resolução PROPOSTA … não fechada aqui" | **FECHADA** na homologação |
| `checks.md` (linha 90) | "L-001 NÃO declarada fechada (só proposta …)" ✔ | Verdadeiro **à data da entrega**; após a homologação, L-001 está FECHADA |
| `checks.md`, CK-01 (linha 129) | L-001-b [DECISÃO NECESSÁRIA] | Resolvida por Andraus (2026-09-22) |

**Registros de estágio preservados (não são erros):** o Autopré-check da entrega (linha 715, "L-001 NÃO declarada fechada") e o risco "Fechar L-001 sem homologação" (linha 618) descrevem o estado e a regra **à data da entrega**; continuam corretos como registro histórico.

**Histórico de versões:** nova linha `1.0-E1 | data da homologação do erratum | ERRATUM-SPEC019-001 — status de L-001 (aditivo; sem alteração normativa)`. O arquivo `checks.md` **não é editado**: este erratum o cobre.

## 2. O que NÃO muda `[FONTE]`

- Nenhuma obrigação, RULE-HG/HV, invariante, BASpec, critério de aceite ou decisão aberta é alterado.
- **O texto original não é reescrito** — permanece como registro do estágio de proposta.
- **CONS-01:** nenhuma decisão aberta é fechada por este erratum. K-001 e demais permanecem abertas; L-001 já estava fechada (DHR-SPEC019-001).
- SPEC-001 e demais Specs: intocadas.

## 3. Verificação de segurança executada `[FATO]`

Sem tocar no baseline, o texto da §1 foi anexado a uma **cópia** do `plan.md`:

| Verificação | Resultado |
|---|---|
| `python scripts/validate_spec_sot.py` (cópia com o apêndice) | **PASS — 10/10 checks estruturais** (inclui STRUCT-10/CONS-01) |
| `scripts/gate-check.js` (hook constitucional) sobre o texto do apêndice | **exit 0** (nenhuma violação) |

## 4. Riscos residuais

1. **Números de linha** do erratum referem-se ao `plan.md` **atual**; o apêndice fica ao **final**, então não os desloca. Se o arquivo for editado antes da aplicação, os números devem ser reconferidos.
2. **Leitura fora do apêndice:** quem lê só o corpo, sem chegar ao fim do arquivo, ainda vê os enunciados antigos. Mitigação: o cabeçalho (linha 13) já declara "FECHADA"; opcionalmente o Controlador pode acrescentar ao cabeçalho a referência "ver Erratum ao final" (Q2).
3. **Precedente:** primeiro erratum sobre Spec homologada — fixa o padrão (apêndice aditivo, sem reescrita, por trio).

## 5. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Aprovar o erratum aditivo (§1) no `plan.md` da SPEC-019? | Sim |
| Q2 | Registrar no "Histórico de versões" a linha `1.0-E1` (sem incremento de versão) **e** acrescentar ao cabeçalho a remissão "ver Erratum ao final"? | Sim (só a linha do histórico é estritamente necessária; a remissão é opcional) |
| Q3 | Cobrir `checks.md` **apenas por referência** (sem editá-lo)? | Sim |
| Q4 | Confirmar o código **ERRATUM-SPEC019-001** para o registro (DHR) | Sim |

## 6. Fluxo de autoridade (RULE-HG-01 / RULE-HG-08)

```
Etapa 1 — Achado (verificação de 2026-09-26/27) ......................... ✅
Etapa 2 — Formalização (esta proposta v1 — NADA aplicado) ............... ✅
Etapa 3 — Parecer do Revisor ............................................ ⏳
Etapa 4 — Consenso de Andraus (Q1–Q4) ................................... ⏳
Etapa 5 — Aplicação (Controlador): apêndice no plan.md + linha no histórico + DHR + CATALOGO + RCH + regenerar mapa ... ⏳ (só após a Etapa 4)
```

## 7. Evidências

`specs/features/SPEC-019/plan.md` (:13, :76, :593, :595, :618, :673, :695, :715, :736, :743) · `specs/features/SPEC-019/checks.md` (:90, :129) · `governance/DHR-SPEC019-001_Ata_Homologacao_SPEC-019.md` · `ROADMAP.md` (linha "Decisões FECHADAS") · `AGENTS.md` §7 · `governance/RULES.md` (RULE-HG-01/05/08) · `scripts/validate_spec_sot.py`.
