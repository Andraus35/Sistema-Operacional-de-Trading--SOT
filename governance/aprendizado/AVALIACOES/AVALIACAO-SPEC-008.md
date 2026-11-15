# AVALIAÇÃO DE DESEMPENHO — SPEC-008 (fim de ciclo) — GERADA por `scripts/avaliacao_spec.py` (DHR-AVALIACAO-001)

> **Detector (ENF-03)**: números extraídos dos pareceres do Revisor; recomendações do catálogo `governance/aprendizado/BOAS-PRATICAS.json` (PROPOSTAS, nunca aplicadas sozinhas). Não decide, não homologa, não fecha decisão aberta (CONS-01). Fontes EXTERNAS são referência geral, não verificada nesta sessão.

| Campo | Valor |
|---|---|
| Spec | SPEC-008 |
| Estado | GERADA |
| Ata de aprovação final | DHR-SPEC008-005 (2026-11-15) |
| Resposta de Andraus | — |
| Ata do registro | — |

## 1. Desempenho (4Es; Economicidade = INDETERMINADO enquanto tokens n/m)

| Linha | Rodada | Crítica | Média | Menor | Veredito | Modo | Tokens | FICHA-M |
|---|---|---|---|---|---|---|---|---|
| SPEC-008 ABERTURA | R1 | 0 | 5 | 7 | NÃO CONFORME | integral | n/m | 2 |
| SPEC-008 ABERTURA | R2 | 0 | 1 | 2 | NÃO CONFORME | integral | n/m | 0 |
| SPEC-008 ABERTURA | R3 | 0 | 0 | 1 | CONFORME CONDICIONAL | delta | n/m | 1 |
| SPEC-008 OUTRO | R1 | 0 | 4 | 8 | NÃO CONFORME | n/d | n/m | 4 |
| SPEC-008 OUTRO | R2 | 0 | 0 | 5 | CONFORME CONDICIONAL | n/d | n/m | 7 |
| SPEC-008 OUTRO | R3 | 0 | 0 | 7 | CONFORME CONDICIONAL | n/d | n/m | 6 |
| SPEC-008 PLAN | R1 | 0 | 5 | 8 | NÃO CONFORME | integral | 258937 | 6 |
| SPEC-008 PLAN | R2 | 0 | 2 | 11 | NÃO CONFORME | integral | 276350 | 11 |
| SPEC-008 PLAN | R3 | 0 | 0 | 9 | CONFORME CONDICIONAL | delta | 296063 | 1 |

| Indicador | Valor |
|---|---|
| Rodadas no total / máx. numa linha | 9 / 3 |
| Médias na 1ª rodada (máx. entre linhas) | 5 |
| Rodadas integrais depois da 1ª | 2 |
| Rodadas sem tokens medidos | 6 |
| Menores resolvidos pela classe M | 38 de 58 (65%) |
| Categorias recorrentes (≥2 rodadas) | C01, C02, C04, C05, C06, C07, C08, C10 |
| …delas, sem prevenção registrada | 1 (C06) |
| Plan: linhas totais / corpo (alerta 1.900, teto 2.000) | 1885 / 1885 |
| Retrospectiva registrada (`FEITA`) | não |

## 2. Recomendações de boas práticas (PROPOSTAS; fontes e 4Es por item)

- **BP-03 — Revisão por delta com versão intermediária commitada** (Eficiência): Commitar cada versão do artefato para o Revisor auditar só o que mudou (delta) em vez de refazer a revisão integral.
  - fonte INTERNA: RETROSPECTIVAS.md (SPEC-007) P1; DHR-DELTA-HASH-001
  - fonte EXTERNA: Revisões pequenas e incrementais (prática geral) — _referência geral; não verificada nesta sessão_
- **BP-04 — Tabela fato→locais gerada por script (contradição interna recorrente)** (Conformidade): Gerar por script a tabela fato→locais e conferi-la antes de reenviar ao Revisor, para propagar cada correção a todos os lugares onde o fato aparece.
  - fonte INTERNA: CAUSAS-PREVENCAO.md C01; RETROSPECTIVAS.md P2/P7 (P7 aprovada como detector informativo, DHR-RETRO-002)
  - fonte EXTERNA: Rastreabilidade requisito→artefato (prática geral de engenharia de requisitos) — _referência geral; não verificada nesta sessão_
- **BP-05 — Âncora por ID+hash em vez de número de linha** (Eficiência): Ancorar citações por ID estável e hash de trecho, não por número de linha que muda a cada edição.
  - fonte INTERNA: CAUSAS-PREVENCAO.md C07 (G-H); RETROSPECTIVAS.md P3
- **BP-06 — Histórico fora do documento principal** (Eficiência): Mover o histórico (texto anterior preservado) para arquivo à parte, com fidelidade conferida, para não inflar o plano nem disparar detectores de contagem.
  - fonte INTERNA: CAUSAS-PREVENCAO.md C06 (G-G/G-I); RULE-ECC-07 (teto de linhas)
- **BP-07 — Máquina de estados em tabela verificável** (Eficácia): Escrever a máquina de estados como tabela estado×evento→estado, verificável por script, em vez de prosa.
  - fonte INTERNA: CAUSAS-PREVENCAO.md C10 (G-F)
  - fonte EXTERNA: Tabelas de transição de estados (prática geral de modelagem) — _referência geral; não verificada nesta sessão_
- **BP-08 — Categoria recorrente sem prevenção registrada** (Efetividade): Para cada categoria recorrente com prevenção AUSENTE, transformar o gate candidato (G-B..G-I) em detector determinístico informativo antes de bloqueante.
  - fonte INTERNA: CAUSAS-PREVENCAO.md (coluna 'Gate/processo candidato'); AGENTS.md §12 passo 3
  - fonte EXTERNA: Shift-left: automatizar a checagem cedo no fluxo (prática geral) — _referência geral; não verificada nesta sessão_
- **BP-10 — Custo por rodada não medido** (Economicidade): Registrar tokens (ou custo) por rodada no cabeçalho do parecer (convenção TOKENS:) para que Economicidade deixe de ser INDETERMINADO. Custo nunca entra no Conviction Vector.
  - fonte INTERNA: DHR-TELEMETRIA-CUSTO-001; loop_ledger.py (metadados_rodada: TOKENS:); CEE-001 §10 (custo fora da convicção)
  - fonte EXTERNA: Medir o que se quer melhorar (métricas de entrega, prática geral) — _referência geral; não verificada nesta sessão_
- **BP-12 — Médias altas na primeira rodada** (Eficácia): Rodar um pré-gate/autopré-check legível por máquina antes de entregar ao Revisor, para tirar defeitos estruturais antes da 1ª rodada.
  - fonte INTERNA: backlog BL-044/BL-045 (pré-gate e autopré-check legível por máquina); AGENTS.md §5
  - fonte EXTERNA: Shift-left (prática geral) — _referência geral; não verificada nesta sessão_
- **BP-01 — Aceitar a avaliação e registrar a retrospectiva** (Efetividade): Fechar o ciclo da Spec com a retrospectiva individual (Especificador, Revisor, Orquestrador) e coletiva (o loop), antes de abrir outra Spec.
  - fonte INTERNA: AGENTS.md §12 passo 5 / DHR-LOOP-002
  - fonte EXTERNA: Retrospectiva de ciclo (prática ágil geral) — _referência geral; não verificada nesta sessão_

## 3. Perguntas automatizadas para Andraus (AskUserQuestion; recomendada em 1º lugar)

```json
[
 [
  {
   "question": "Houve rodada de revisão integral depois da primeira (refazendo tudo em vez de olhar só o que mudou). Quer exigir revisão só do que mudou nas rodadas seguintes?",
   "header": "Revisão",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir a proposta (Recomendado)",
     "description": "Exigir versão commitada e revisão só do delta; sem aplicar."
    },
    {
     "label": "Manter como está",
     "description": "Sem mudança no processo."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-03"
  },
  {
   "question": "O mesmo erro (texto que se contradiz em lugares diferentes) voltou em mais de uma rodada. Quer um conferidor automático que ache todos os lugares de cada fato antes da revisão?",
   "header": "Contradição",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir a proposta do conferidor (Recomendado)",
     "description": "Só a proposta, sem aplicar."
    },
    {
     "label": "Manter como está",
     "description": "O Revisor continua conferindo à mão."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-04"
  },
  {
   "question": "Citações erradas (linha que mudou, referência que não confere) voltaram em mais de uma rodada. Quer trocar a citação por linha por citação por identificador?",
   "header": "Citações",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir a proposta (Recomendado)",
     "description": "Só a proposta, sem aplicar."
    },
    {
     "label": "Manter como está",
     "description": "Sem mudança no processo."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-05"
  },
  {
   "question": "Erros de contagem ou de histórico copiado à mão voltaram. Quer guardar o histórico em arquivo separado, com conferência automática?",
   "header": "Histórico",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir a proposta (Recomendado)",
     "description": "Só a proposta, sem aplicar."
    },
    {
     "label": "Manter como está",
     "description": "Sem mudança no processo."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-06"
  }
 ],
 [
  {
   "question": "Apareceram erros de transição entre estados (uma ação que o sistema não previa). Quer exigir a máquina de estados em tabela conferida por script?",
   "header": "Estados",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir a proposta (Recomendado)",
     "description": "Só a proposta, sem aplicar."
    },
    {
     "label": "Manter como está",
     "description": "Sem mudança no processo."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-07"
  },
  {
   "question": "Há tipos de erro que se repetem e ainda não têm prevenção automática. Quer que eu escreva a proposta de um detector para cada um?",
   "header": "Prevenção",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir as propostas (Recomendado)",
     "description": "Uma proposta por categoria, sem aplicar; você decide uma a uma."
    },
    {
     "label": "Manter como está",
     "description": "As categorias seguem sem prevenção automática."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-08"
  },
  {
   "question": "Não sabemos quanto custou cada rodada de revisão (o custo não foi medido). Quer passar a registrar o custo de cada rodada?",
   "header": "Custo",
   "multiSelect": false,
   "options": [
    {
     "label": "Registrar o custo por rodada (Recomendado)",
     "description": "Convenção TOKENS no parecer; só para acompanhar, nunca entra na convicção."
    },
    {
     "label": "Manter como está",
     "description": "Economicidade segue indeterminada."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-10"
  },
  {
   "question": "A primeira revisão achou 3 ou mais problemas médios. Quer uma checagem automática antes de entregar ao Revisor?",
   "header": "Pré-entrega",
   "multiSelect": false,
   "options": [
    {
     "label": "Redigir a proposta (Recomendado)",
     "description": "Só a proposta, sem aplicar; liga ao backlog BL-044/045."
    },
    {
     "label": "Manter como está",
     "description": "Sem mudança no processo."
    },
    {
     "label": "Adiar",
     "description": "Revê na próxima Spec."
    }
   ],
   "origem": "BP-12"
  }
 ],
 [
  {
   "question": "A avaliação desta Spec está pronta. Aceita os números e quer registrar a retrospectiva agora?",
   "header": "Avaliação",
   "multiSelect": false,
   "options": [
    {
     "label": "Aceitar e registrar a retrospectiva (Recomendado)",
     "description": "Registra a sua análise; libera abrir a próxima Spec."
    },
    {
     "label": "Pedir ajuste na avaliação",
     "description": "Aponte o que está errado; o relatório é regerado antes de seguir."
    },
    {
     "label": "Adiar",
     "description": "Mantém a avaliação pendente; a próxima Spec continua bloqueada."
    }
   ],
   "origem": "BP-01"
  }
 ]
]
```

## 4. Como fechar

1. Apresentar os lotes acima a Andraus por AskUserQuestion (linguagem de trader). 2. Registrar a decisão dele em ata (DHR-…) e rodar `python scripts/avaliacao_spec.py registrar SPEC-008 --ata DHR-… --resposta "<citação>"`. 3. Registrar a retrospectiva (`RETROSPECTIVAS.md`, `FEITA`). Sem isso `loop_ledger.py --retro-check SPEC-008` falha e a próxima Spec não abre (salvo dispensa expressa de Andraus).

<!-- DIGEST:700a01ab3784b45cb405d5ec764e47054e88fc5271b4da022c6a391f5c14bc89 -->
