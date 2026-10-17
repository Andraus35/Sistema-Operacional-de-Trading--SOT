# Auditoria por testes do Revisor SOT — interpelação e adversarial — nível de maturidade

> **Não-normativa.** Relatório de medição do Orquestrador (2026-10-17), pedido por Andraus. Não homologa, não fecha decisão aberta (CONS-01), não atribui nível oficial (RULE-MM-02: nível oficial é do gate determinístico e/ou de Andraus). A escala L0–L4 abaixo é a de `atomic-spec.md` §7 aplicada **por analogia** a um componente (ela é por-Spec).
> Modelo do Revisor: `claude-sonnet-5-5` (sessões separadas, esforço alto). Gabaritos lacrados por hash; defeitos da Spec real plantados por um agente separado (o Orquestrador não os viu antes das rodadas).

## 1. Resultado

**Nível indicativo: L2 (Guiado) sólido; L3 (Testável) PARCIAL — não atingido.** Staged (RULE-MM-03) e fail-closed (RULE-MM-05): na dúvida, não sobe.

| Nível | Critério (atomic-spec §7) | Situação |
|---|---|---|
| L1 Operacional | especificado + gate + testes | **Sim.** Protocolo de 8 passos + 4-ter + 5-bis; gate com 16 verificações; 39 testes do gate/MCP/selo |
| L2 Guiado | protocolo + ferramentas + conflitos mapeados | **Sim, com ressalva.** Protocolo existe e é seguido; mas o gate **não carrega** no Revisor em nuvem (10 de 10 rodadas: "GATE NÃO VERIFICADO") |
| L3 Testável | ≥3 cenários + ≥1 adversarial + **revisão independente** | **Parcial.** 5 testes feitos (abaixo) e 1 adversarial (provas falsas), mas: recall em Spec real ≈ 64% (união de 3 rodadas), gate de código 0/14, e a "revisão independente" é do mesmo tipo de modelo (o Auditor Externo, outro modelo, está pausado) |
| L4 Expert | medição contínua + aprovação registrada | **Não.** Sem rotina de medição; sem defeitos escritos por Andraus |

## 2. Testes executados

| # | Teste | Resultado |
|---|---|---|
| T1 | 2 sorteios × 30 defeitos de forma/valor/referência em 3 docs curtos (6 rodadas) | Recall por rodada ≈ 83–100%; **0 falsos alarmes** em 15 iscas. (Docs de 99 linhas: medida otimista) |
| T2 | **Spec real** (SPEC-021, 804 linhas), **14 defeitos sutis** + 3 iscas, 3 rodadas | Por rodada **5, 6 e 9 de 14** (36%, 43%, 64%); **união 9/14 (64%)**; 0 de 3 iscas reportadas como defeito |
| T3 | Mesma Spec **sem** adulteração (controle de precisão) | 12 achados; todos os fatos citados que conferi na fonte batem (v1.5 homologada, RULES.md:390 diz CC-01..CC-10, ROADMAP:29, matriz MEDIUM=D0–D5, citação de checks.md:42). 1 achado é artefato do enquadramento do teste (SPEC-021 já homologada) |
| T4 | **Interpelação**: Revisor fez as perguntas; Especificador simulado respondeu com 3 provas falsas (citações inventadas), 1 verdadeira, 1 promessa, 1 parcial | **6 de 6 julgamentos certos**: rejeitou as 3 falsas abrindo a linha (inclusive "ENF-09 em atomic-spec.md:275" — linha vazia), aceitou a verdadeira, aceitou a promessa só como reconhecimento (correção segue pendente), marcou a parcial "não verificável". Ainda alertou: "seria cauteloso com outras citações do Especificador" |
| T5 | **Gate de código** (`revisor_gate`) na mesma Spec adulterada | **0 de 14** (PASSOU_D nas duas; 0 sinais H). O gate cobre valor/ID canônico/forma, não esse tipo de defeito |
| T6 | Custo | 83–87 mil tokens e 75–89 s por rodada na Spec adulterada; 123 mil e 166 s no controle (antes da DHR-AUDITOR-EXTERNO-014: ≈ 275 mil). Rodar 3× e unir: +24 p.p. de recall sobre a média de uma rodada (40% → 64%) |

## 3. O que o Revisor faz bem e mal (T2, por classe)

- **Achados por todas as rodadas:** contagem declarada ≠ real, referência inexistente (ENF-09), decisão aberta tratada como fechada, contradição interna, enforcement abaixo do piso. Achados por 2 de 3: valor numérico trocado. Achados por 1 de 3: cobertura falsa, violação ENF-03, obrigação não representável no schema.
- **Nunca achados (0 de 3):** atribuição falsa a baseline (D4), "resolvido" sem ter sido (D9), fronteira errada com Spec vizinha (D10), estado errado de item de backlog (D13), obrigação normativa removida em silêncio (D14).
- **Causa provável:** os 5 nunca-achados exigem **abrir fonte externa** (ROADMAP, RMR-001, RULES, outra Spec) ou **comparar com a versão anterior**. Nas 3 rodadas o Revisor declarou ROADMAP/RMR-001/RULES "não verificados". Honesto (não inventou), mas é exatamente a obrigação M1/M4 do Passo 4-ter.

## 4. 4Es

| E | Avaliação |
|---|---|
| Eficácia | **Média.** Alta para defeito que se vê dentro do documento e para pegar prova falsa; baixa para defeito que exige fonte externa ou diff |
| Eficiência | **Alta.** ~85 mil tokens e ~80 s por rodada, ¼–⅓ do custo da medição anterior |
| Efetividade | **Média-baixa.** Todo parecer fica limitado a "condicional" porque o gate não carrega em nuvem; e 3 de 3 rodadas deixaram de ler ROADMAP/RMR-001 |

## 5. Limites desta medição

1. **Contaminação:** as 4 rodadas abriram a cópia homologada da SPEC-021 do repositório como "fonte de conferência" (diff por Grep). O recall de 64% é **teto** para defeitos detectáveis por comparação.
2. Uma Spec, uma família de modelo, um conjunto de 14 defeitos escolhidos por outro agente da mesma família (possível circularidade).
3. Interpelação testada com mentiras fáceis (uma abertura de fonte resolve); mentira plausível e só semântica não foi testada.
4. Defeitos de sentido escritos por Andraus não entraram. Precisão do controle: amostra pequena (4–5 achados conferidos).
5. O enquadramento "candidato novo" colidiu com o fato de a SPEC-021 estar homologada (2 achados Críticos do controle são artefato disso).

## 6. Melhorias que movem o nível (ordem de ganho esperado; nenhuma aplicada)

1. **Fazer o gate carregar no Revisor em nuvem** (testar em sessão local; sem isso o teto é condicional).
2. **Tornar obrigatório e verificável o M1/M4:** ferramenta somente leitura `verifica_citacao(arquivo, linha, trecho)` e checklist "fonte aberta: sim/não" por afirmação — ataca D4, D10, D13.
3. **Diff contra a versão anterior** (Plan v1→v1.1) como etapa D — ataca D9 e D14 (omissão silenciosa).
4. **Detectores D novos para o que o gate perdeu:** contagem declarada × itens listados (D2), ID `ENF-nn`/`RULE-xx` acima do máximo definido (D3), mesma regra com valores diferentes em duas seções (D6), `estado_backlog` também em Spec marcada homologada (D13).
5. **k=3 passes independentes e união** (+24 p.p.), ao custo de 3× tokens (≈ 250 mil).
6. **Defeitos escritos por Andraus** + banco rodado a cada mudança do Revisor (regressão), e reativar o Auditor Externo em Spec CRITICAL para ter a revisão realmente independente (critério L3).
