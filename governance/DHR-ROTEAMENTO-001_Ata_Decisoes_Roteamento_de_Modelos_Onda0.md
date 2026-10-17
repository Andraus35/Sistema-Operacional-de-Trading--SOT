# DHR-ROTEAMENTO-001 — Ata — Decisões D1–D6 sobre roteamento de modelos dos agentes de construção (onda 0 autorizada)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisões de Andraus registradas (chat, 2026-10-17, respostas às perguntas D1–D6 com sugestão de melhor prática)**. O merge desta ata por Andraus é a ratificação. **Não altera nenhum arquivo de agente nem normativo.** Base: `governance/propostas/ROTEAMENTO-MODELOS/AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md`. |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Registra decisões de procedimento do Orquestrador e autoriza testes; não altera `especificador.md`, `revisor.md`, checklist, método nem regra. |

## 1. Decisões `[FATO]`

| # | Pergunta | Decisão de Andraus | Efeito |
|---|---|---|---|
| **D1** | Onda 0 (pré-gate, `model`/`effort` por invocação só em tarefa operacional não crítica, telemetria por rodada) | **Sim** | Vigora para o Orquestrador a partir desta ata (ver §2) |
| **D2** | Testes de não-inferioridade sobre o gabarito existente | **Sim, ≥3 repetições por braço** | Autoriza a **preparação e, depois de ordem expressa de execução**, a execução da onda 1 (§3) |
| **D3** | Cobrança do ambiente | **Assinatura com limite de uso (cota)** | Métrica-alvo = **tokens/chamadas por defeito confirmado** (US$ só como referência) |
| **D4** | Margem de não-inferioridade | **Zero perda em Crítico/Alto**; sem aumento de falso alarme; tolerância em Menor até 1 de 18 | Critério de aceite de qualquer rebaixamento |
| **D5** | Formalização | **EUA-E24 aditiva** (sucessora da EUA-E19; não toca CEE-001/RULE-CEE-002) | Só após a onda 1 (evidência) |
| **D6** | `effort` explícito no frontmatter | **Depois da varredura de esforço** | Nenhum frontmatter muda agora |

## 2. Onda 0 — o que o Orquestrador passa a fazer `[FATO]`
1. **Pré-gate:** antes de invocar o Revisor, roda `python scripts/revisor_gate.py SPEC-NNN` (ou `run_gates.py`); `REPROVADO_D` volta ao Especificador **sem** invocar o Revisor LLM. O Revisor continua obrigado a chamar o gate (defesa em profundidade; ENF-03).
2. **`model`/`effort` por invocação** apenas em tarefas **N1 não críticas** (busca/exploração, resumo de log de CI, triagem). **Nunca** para Especificador, Revisor ou tarefa N2/N3; nunca como gate (ENF-03).
3. **Telemetria manual** por rodada em `governance/propostas/ROTEAMENTO-MODELOS/TELEMETRIA-ONDA0.md` (tokens/chamadas quando o `Agent` reportar, rodada, resultado). Meta de saída: ≥10 rodadas.
4. Informar Andraus no resumo da sessão sempre que o pré-gate evitar uma revisão.

## 3. Onda 1 — protocolo `[PROPOSTA]` (execução só por ordem expressa)
Testes A (Opus 4.8→5.5 + varredura de esforço), B (tarefas N1/N2 em Sonnet/Haiku), C (revisão por diferença) e D (pré-gate e subagentes auxiliares), conforme §8 da proposta, com: ≥3 repetições; hipótese, margem (D4) e métrica (D3) pré-registradas antes de rodar; juiz = defeitos confirmados no repositório; reprova automática se o braço barato alterar texto normativo fora do pedido. **Limite de consumo da cota a fixar por Andraus na ordem de execução.**

## 4. Reversão `[PROPOSTA]`
`git revert` do commit desta ata; a onda 0 é procedimento do Orquestrador e cessa imediatamente.

## 5. Permanecem ABERTAS (CONS-01)
Conforme `ROADMAP.md`, que prevalece. **Nenhuma fechada ou aberta por este ato.**

## 6. Registro
- [x] Esta ata · [x] `CATALOGO-OFICIAL.md` · [x] `TELEMETRIA-ONDA0.md` (rascunho) · [x] HANDOFF · [x] mapa · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *decisões em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge.*
