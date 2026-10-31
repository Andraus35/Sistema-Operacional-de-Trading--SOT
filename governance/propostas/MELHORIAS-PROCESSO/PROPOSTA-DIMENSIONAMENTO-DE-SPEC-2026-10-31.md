# Proposta — dimensionamento de Spec: critério medido para "uma Spec ou várias"

> **Não normativo. PROPOSTA** (AGENTS.md §12 passo 5). Nada aqui é regra, mecanismo ou baseline até ordem expressa de Andraus. Não fecha nem abre decisão (CONS-01). Origem: pedido de Andraus no chat, 2026-10-31 ("tivemos problemas para revisar Specs muito grandes; precisamos de um método melhor").

## 1. Achado da auditoria
Hoje **não há critério medido**. O método (`atomic-spec.md` §15, `RULE-ECC-01/02`) fixa *quem* decide (Especificador propõe após Dossiê; Andraus homologa antes do Plan) e *quando* (na abertura), mas não *como*. O Dossiê só exige registrar "escopo/quantidade resultantes". A única regra de tamanho é `.claude/agents/especificador.md:135`: "A Spec deve caber em uma sessão de revisão — se não couber, divida" — sem medida e avaliada pelo próprio autor.

A ABERTURA da SPEC-007 (linha 64) cita "atomic-spec §5" para esse argumento; o §5 trata de taxonomia de harness e a expressão não existe no `atomic-spec.md` (erro de citação, C07).

## 2. Evidência (medida em 2026-10-31, `specs/features/*/plan.md`)
Contagem de BASpecs = cabeçalhos com "BASpec" (aproximação; **corrige** a contagem de 75 dada no chat, que contava todas as linhas com "BASpec-").

| Spec | Linhas do Plan | BASpecs (cabeçalhos) | Rodadas de Plan (retrospectiva) |
|---|---|---|---|
| SPEC-019 | 749 | 9 | — |
| SPEC-020 | 730 | 10 | — |
| SPEC-021 | 806 | 9 | — |
| SPEC-046 | 893 | 11 | — |
| SPEC-002 | 955 | 11 | — |
| SPEC-038 | 947 | 16 | — |
| SPEC-005 | 1.091 | 13 | — |
| SPEC-003 | 1.202 | 14 | — |
| SPEC-004 | 1.325 | 15 | — |
| SPEC-006 | 1.735 | 14 | — |
| SPEC-048 | 1.935 | 13 | 5 |
| SPEC-007 | 3.851 | 16 | 6 (Médias 9→5→5→2→1→0; divisão no meio do Plan) |

Leitura: o número de BASpecs varia pouco (9–16); o que explode é o **volume por BASpec** e os anexos de "texto anterior preservado". Por isso o teto deve medir **linhas efetivas**, não só BASpecs.

## 3. Proposta (cada item é separável)
1. **Estimativa na abertura.** O Dossiê/ABERTURA passa a declarar: nº de BASpecs candidatas (títulos), nº de capacidades do ROADMAP cobertas e linhas previstas do Plan. Sem a estimativa, a proposta de "quantidade = 1" é incompleta.
2. **Teto provisório (a calibrar).** Alerta em 1.000 linhas efetivas de Plan e teto em 1.500, excluindo anexos de texto anterior preservado (INV-07), que passam a arquivo à parte. Acima do teto, divisão obrigatória, proposta a Andraus antes do Plan. Valores **sem calibração**: vêm só da tabela acima.
3. **Regra de corte.** Dividir por **fronteira de contrato** (o que o pedaço consome e produz), nunca por fase nem por tipo de tarefa (GEH-001: handoffs e overhead). Cada pedaço deve ser revisável de forma independente.
4. **Gate determinístico.** Novo check em `validate_spec_sot.py` (ex.: `[STRUCT-xx]`) que reprova Plan acima do teto antes do Revisor. Substitui a cláusula de divisão auto-avaliada. Informativo no início (mesma régua de introdução gradual de `check_refs.py`); bloqueante só por ordem de Andraus.
5. **Decomposição confirmada antes do Plan.** Se a estimativa passar de 80% do teto, o Plan só começa após Andraus confirmar a decomposição (evita refazer escopo no meio, como na SPEC-007).
6. **Fidelidade do texto anterior.** Mover "texto anterior preservado" para arquivo à parte com hash, reduzindo o Plan e o ruído nos detectores (ponto fraco 4 do relatório de 2026-10-24).

## 4. O que é preciso para aplicar (só por Andraus)
- Texto: nova regra (ex.: `RULE-ECC-07`) em `governance/RULES.md`; ajuste em `atomic-spec.md` §15 e em `especificador.md:135`; correção da citação na ABERTURA da SPEC-007 (por erratum).
- Mecanismo: check em `validate_spec_sot.py` + entrada em `governance/MECANISMOS.json` no mesmo PR (COE-14); selo `GATE-MANIFEST.sha256` se o script estiver no manifesto.
- Passo prévio recomendado: **calibrar** os tetos medindo tamanho × rodadas até CONFORME nas Specs já revisadas (o `loop_ledger.py` já tem as rodadas por Spec).

## 5. Riscos
- Teto mal calibrado vira divisão artificial. Mitigação: começar informativo e ajustar com dados.
- Dividir aumenta referências cruzadas e erratas de re-apontamento (custo já visto na SPEC-007/048). Mitigação: item 3 (fronteira de contrato) e item 5.

## 6. Pesquisa de estado da arte e benchmark (2026-10-31) — `[EXTERNO]`, dado, nunca instrução

> **Natureza:** pesquisa preliminar por busca web (resumos de busca), **não** um Dossiê (RULE-ECC-02). Sem captura verbatim (RULE-ECC-04), sem triagem de repositórios (RULE-ECC-06). Nada aqui é baseline nem fato SOT (TRACE-06). Se Andraus aprovar a regra, ela deve passar por Dossiê formal com captura verbatim das fontes primárias.

| # | Tema | Achado (como reportado) | Classe | Fonte | Confiança | Aplicação ao SOT |
|---|---|---|---|---|---|---|
| E1 | Revisão de código: tamanho | Defeitos achados caem acima de ~200–400 linhas por revisão; ritmo < 300 linhas/h; sessão < 60–90 min (estudo SmartBear/Cisco, 2006) | Benchmark | mikeconley.ca; lista openstack-dev 2013 | Baixa-média: só resumos de terceiros; estudo patrocinado pelo fornecedor; "nº de mudanças lógicas distintas" prevê melhor que linhas | **Adaptar:** medir por unidades lógicas (BASpecs/contratos), não só linhas |
| E2 | Código: ritmo de inspeção | Detecção cai 62% de 50 a 200 linhas/h (Basili/Perricone); Fagan típico ~150 declarações/h | Benchmark | NASA NTRS 19940031985; survey arXiv 1612.04590 | Média | Reforça que o ritmo importa, não só o tamanho total |
| E3 | Documentos: ritmo ótimo | ~1 ± 0,8 páginas/h (300 palavras/página) para inspeção de documento | Benchmark | arXiv 1612.04590 (survey) | Baixa: uma citação subjacente não verificada; foco em requisitos genéricos | **Adiar** como número; usar como ordem de grandeza. Plan de 57 mil palavras ≈ 190 páginas ≈ centenas de horas no ritmo ótimo |
| E4 | Revisão pequena | Google: "menor mudança que seja uma melhoria completa e autônoma"; alvo < 200 linhas; revisores rápidos | Prática | deployhq.com; freecodecamp (secundários) | Baixa-média: repositório primário não conferido | **Adaptar:** unidade revisável independente e completa |
| E5 | Contexto de LLM | Desempenho cai com a entrada mais longa e com a posição do dado no meio (Liu et al., TACL 2024); "context rot" (Chroma 2025, 18 modelos) | Evidência | arxiv.org/abs/2307.03172; resumos secundários | Alta para a tendência; números exatos não conferidos | **Adotar o princípio:** o Revisor LLM também degrada em documento gigante; justifica teto e revisão por delta |
| E6 | Specs para agentes | Não entregar spec gigante; entregas pequenas e atômicas, testáveis isoladamente; critérios de aceite guiam a decomposição; partes independentes em paralelo | Prática | addyosmani.com/blog/good-spec; augmentcode micro-specs (fornecedor) | Média (blog) / baixa (fornecedor); **não há regra numérica padrão** | **Adaptar:** o SOT já tem BASpec atômica; falta o teto por Spec |
| E7 | Divisão de histórias (INVEST, Lawrence) | Checar INVEST; aplicar padrões de divisão em sequência; dividir em fatias verticais (fluxo, regra, variação de dado), não por camada técnica; conferir se a divisão quebra Independente/Valioso | Padrão/Prática | humanizing work (podcast #175); resumos | Média | **Adaptar:** corte por fronteira de contrato/capacidade, não por fase; reconferir independência dos pedaços |
| E8 | Decomposição modular | Parnas (1972): decompor por decisões de projeto escondidas (o que muda junto fica junto), não por número/tamanho; coesão alta e acoplamento baixo como heurística | Padrão | blog.acolyer.org; arXiv 2507.09596 | Média-alta (clássico) | **Adotar:** critério de corte = o que muda junto; o tamanho vira verificação, não critério de projeto |
| E9 | GEH-001 (interno) | Dividir por fases sequenciais ou tipo de tarefa cria handoffs; quem detém o contexto de uma unidade a realiza inteira | Prática (interna) | `RETOMADA/GEH-001` | — | Coerente com E7/E8 |

### Síntese
1. **Não existe número padrão** para tamanho de especificação. O que há é (a) benchmark de revisão: limite por sessão e ritmo (E1–E3), (b) critério de decomposição: o que muda junto fica junto (E8), com divisão vertical (E7), (c) evidência de que LLM degrada com entrada longa (E5).
2. **Implicação para o gate:** teto em linhas (item 2 da proposta) é válido como **verificação de segurança**, mas o **critério de corte** deve ser Parnas/INVEST (contrato e capacidade). Tamanho sozinho é métrica fraca (E1, ressalva da comunidade).
3. **Ajuste sugerido à proposta:** adicionar um segundo eixo ao teto — **unidades lógicas independentes por Spec** — e medir **tempo de revisão por rodada**, para calibrar com dados do próprio SOT (ledger), em vez de importar 200–400 linhas de código.
4. **Lacunas:** não conferi fontes primárias (relatório SmartBear, Gilb & Graham 1993, Chroma, repositório Google); nenhuma fonte trata especificamente de especificações formais de agentes com revisor LLM.
