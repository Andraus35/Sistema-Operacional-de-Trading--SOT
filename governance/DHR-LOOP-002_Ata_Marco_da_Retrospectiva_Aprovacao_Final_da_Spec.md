# DHR-LOOP-002 — Ata — Marco da retrospectiva do loop: aprovação final da Spec

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT |
| Ref | `AGENTS.md` §12 passo 5 (LOOP-001 / `DHR-LOOP-001`) · `scripts/loop_ledger.py` (`--retro-check`) · `governance/aprendizado/RETROSPECTIVAS.md` |
| Data | 2026-11-08 |
| Status | **APLICADO no ramo; vigora com o merge do PR (assinatura de Andraus).** Decisão de Andraus por AskUserQuestion, 2026-11-08: pedido "Colocar a obrigação da retrospectiva após a homologação da spec"; marco = "Aprovação final da Spec após rodadas de revisão e correções. Quando não houver mais achados"; forma = "Redigir e aplicar agora". Altera `AGENTS.md` (reservado): vale a ordem expressa citada aqui (AGENTS.md §10). |
| Compatibilidade | Minor (muda o momento da obrigação; o mecanismo `--retro-check` e seus testes não mudam de comportamento) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda o marco de uma regra do Orquestrador (AGENTS.md §12); não altera texto de agente de construção nem método. |

## 1. Decisões de Andraus `[FATO]` (AskUserQuestion, 2026-11-08)
| # | Ponto | Decisão |
|---|---|---|
| M-1 | Marco da obrigação | **Aprovação final da Spec**, depois das rodadas de revisão e correção, quando não houver mais achados |
| M-2 | Forma | **Redigir e aplicar agora** (esta ata + edição do `AGENTS.md` §12 e do texto do `loop_ledger.py`) |

## 2. O que mudou
- **`AGENTS.md` §12 passo 5:** "NO FECHAMENTO da Spec" → "**NA APROVAÇÃO FINAL da Spec**". A obrigação nasce no **Plan homologado como baseline** (leitura do Orquestrador do marco M-1: a "aprovação final" de uma Spec em redação é a homologação do Plan por Andraus, `[INFERÊNCIA]`); abertura e documentos intermediários homologados (contrato, errata) **não** a disparam. O resto do passo 5 não muda (retrospectiva individual e coletiva, propostas de gate só por ordem, `--retro-check` antes de abrir outra Spec, dispensa só de Andraus). Texto anterior preservado (INV-07).
- **`scripts/loop_ledger.py`:** só texto (docstring, `--help` e a nota da seção 5 do ledger: "Spec com aprovação final" em vez de "Spec FECHADA"). **Comportamento inalterado** (`--retro-check` continua exit 1 sem retrospectiva `FEITA`); `tests/test_loop_ledger.py`: 11 testes OK. `MECANISMOS.json` não muda (nenhum mecanismo criado, movido ou aposentado).

## 3. Efeito prático `[INFERÊNCIA]`
- **SPEC-008:** abertura e MMC-001 (com errata) estão homologados, mas **não há Plan**; a obrigação da retrospectiva da SPEC-008 **ainda não nasceu**. O handoff do ramo que dizia "antes de outra Spec, retro-check SPEC-008" passa a valer só após a aprovação final do Plan da SPEC-008.
- **Antes de abrir outra Spec:** continua valendo o `--retro-check` da última Spec com aprovação final. Se uma Spec nova for aberta enquanto a SPEC-008 está sem Plan, a SPEC-008 não tem retrospectiva devida.

## 4. O que esta ata NÃO afirma
- Não define "aprovação final" por critério mecânico: "não restam achados" é lido pelo Orquestrador a partir dos pareceres; a homologação do Plan continua sendo ato de Andraus.
- Não fecha decisão aberta (CONS-01), não altera `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*` nem `canon/`. Retrospectivas já feitas (SPEC-006/007/048/049) seguem válidas.

## 5. Registro
- [x] Esta ata · [x] Decisões de Andraus (AskUserQuestion 2026-11-08) · [x] `AGENTS.md` §12 · [x] `loop_ledger.py` (texto) · [x] CATALOGO · [x] RPSA · [x] handoff do ramo · [ ] merge (PR, CI verde — assinatura)

---

**Andraus** — *decisões dadas por AskUserQuestion, 2026-11-08; registro pelo Orquestrador.*
