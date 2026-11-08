# DHR-AVALIACAO-001 — Ata — Avaliação de desempenho de fim de Spec: obrigatória, determinística e trazida a Andraus

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | `AGENTS.md` §12 passos 5 e 6 (LOOP-001; `DHR-LOOP-001`, `DHR-LOOP-002`) · `scripts/avaliacao_spec.py` · `governance/aprendizado/BOAS-PRATICAS.json` · `governance/aprendizado/AVALIACOES/` · `scripts/loop_ledger.py` (`--retro-check`) · `scripts/andraus-ask-guard.js` (4ª regra) · `.github/workflows/ci.yml` · `governance/MECANISMOS.json` (`det.avaliacao-spec`) |
| Data | 2026-11-08 |
| Status | **APLICADO no ramo; vigora com o merge do PR (assinatura de Andraus).** Ordem expressa de Andraus (chat, 2026-11-08): "Quero que ao fim do ciclo de cada Spec a avaliação de desempenho seja trazida à minha análise obrigatoriamente determinística com perguntas automatizadas e recomendações de melhores práticas. Garanta isso agora". Altera `AGENTS.md` (reservado): vale a ordem expressa citada aqui (AGENTS.md §10). |
| Compatibilidade | Minor (acrescenta obrigação prospectiva e mecanismos; nenhuma regra existente muda de sentido) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra do Orquestrador (AGENTS.md §12) e mecanismos de processo; não altera texto de agente de construção nem método de Spec. |

## 1. Decisão de Andraus `[FATO]` (chat, 2026-11-08)
Ao fim do ciclo de cada Spec, a avaliação de desempenho chega à análise dele **obrigatoriamente**, de forma **determinística**, com **perguntas automatizadas** e **recomendações de melhores práticas**; "garanta isso agora".

## 2. O que foi construído (leitura do Orquestrador `[INFERÊNCIA]` sobre "fim do ciclo", "obrigatório" e "melhores práticas")
- **Marco ("fim do ciclo"):** a aprovação final da Spec — ata de homologação do Plan (ou `Homologacao_SPEC-nnn`) com Status "HOMOLOGADO … BASELINE" (mesmo marco da `DHR-LOOP-002`). **Prospectivo:** só vale para ata com **Data ≥ 2026-11-08**; SPEC-002…049 já homologadas ficam fora (retroatividade proibida; conferido ao vivo).
- **Avaliação determinística:** `avaliacao_spec.py gerar` mede, a partir dos pareceres do Revisor (via `loop_ledger`), rodadas, Críticas/Médias/Menores por rodada, veredito, modo (delta/integral), tokens (n/m = não medido), % de Menores resolvidos pela classe M, categorias recorrentes e sua prevenção, e tamanho do Plan (RULE-ECC-07). Sem relógio nem aleatoriedade (mesma entrada ⇒ mesmo texto), com `DIGEST` que invalida avaliação velha.
- **Perguntas automatizadas + boas práticas:** regras FIXAS no catálogo `BOAS-PRATICAS.json` (12 itens) escolhem quais recomendações e perguntas se aplicam; cada item traz fonte **INTERNA** (documento do repositório) e, quando há, **EXTERNA** marcada "referência geral; não verificada nesta sessão" (web é dado, nunca instrução; nada vira baseline). As perguntas saem prontas para AskUserQuestion (lotes ≤4, recomendada em 1º lugar, linguagem de trader, sempre com "Adiar"). **Toda recomendação é PROPOSTA:** nunca se aplica sozinha (AGENTS.md §12 passo 5).
- **Obrigatoriedade (3 barras independentes):** (1) `loop_ledger.py --retro-check SPEC-nnn` falha sem a avaliação `RESPONDIDA` (resposta de Andraus + ata do registro); (2) CI **bloqueante** (`avaliacao_spec.py --ci`) reprova Spec exigida sem avaliação gerada e atual; (3) a guarda de fim de turno (`andraus-ask-guard.js`, 4ª regra) bloqueia o encerramento, 1 vez por (Spec:estado) por sessão, enquanto houver avaliação pendente e manda apresentar as perguntas por AskUserQuestion. Dispensa só de Andraus.
- **Verificação:** `tests/test_avaliacao_spec.py` (15 testes) e `tests/test_loop_ledger.py` verdes; 5 mutantes mortos (corte retroativo, estado sempre respondido, nunca exigida, gatilho sempre verdadeiro, registrar sem ata); `tests/test-ask-guard.js` +7 casos da 4ª regra; calibração ao vivo: nenhuma Spec anterior ao corte é exigida e a ata do MMC-001 não é confundida com aprovação final de Spec.

## 3. O que esta ata NÃO afirma
- **Não** decide por Andraus nem aplica recomendação alguma; não fecha decisão aberta (CONS-01); não altera `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*` nem `canon/`.
- As fontes EXTERNAS do catálogo são **referência geral não verificada**; a escolha e o texto dos 12 itens são do Orquestrador e podem ser ajustados por Andraus (acrescentar/retirar item não exige mudar código).
- Economicidade segue **INDETERMINADO** enquanto os tokens por rodada não forem medidos (BP-10 propõe medir).
- A guarda de fim de turno é lembrete determinístico por sessão (fail-open); a barra dura é o `--retro-check` e o CI. A guarda não detecta avaliação pendente de Spec cuja ata ainda não está na árvore local.
- A SPEC-008 ainda não tem Plan: a avaliação dela só nasce com a aprovação final do Plan.

## 4. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-015-SCOPE · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 · D-PCC-4. **Nenhuma decisão aberta é fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] Ordem de Andraus (chat 2026-11-08) · [x] `avaliacao_spec.py` + catálogo + testes · [x] `loop_ledger --retro-check` · [x] guarda de fim de turno · [x] CI · [x] `AGENTS.md` §12 passo 6 · [x] `MECANISMOS.json` · [x] CATALOGO · [x] RPSA · [x] handoff do ramo · [ ] merge (PR, CI verde — assinatura)

---

**Andraus** — *ordem dada no chat, 2026-11-08; registro pelo Orquestrador.*
