# DHR-A9TESTE-001 — Ata de Decisão — Correção de fatos defasados em `revisor.md` e `especificador.md` e teste de guarda (A9-teste)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador / Especificador SOT / Revisor SOT |
| Ref | Ordem de Andraus (AskUserQuestion, 2026-11-01): "Sim, aplicar" · `governance/propostas/MELHORIAS-PROCESSO/A9/PROPOSTA-A9-CHECKLIST-UNICO-2026-11-01.md` · `AGENTS.md` §6.9 e §10 · `DHR-PRE-ENTREGA-001` |
| Data | 2026-11-01 |
| Status | **APLICADA por ordem de Andraus** (emenda a arquivos reservados `.claude/agents/*` — AGENTS.md §10; modelo curto NÃO se aplica, pois toca agente). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Duas linhas de fato defasado corrigidas nos agentes (Signal Package; CC-01..CC-12); sem mudança de método nem de fronteira. |

## 1. Problema `[FATO]`
A auditoria do Autopré-check (A9) achou fatos que o repositório já tinha corrigido ainda vivos nos agentes: `revisor.md:162` "SOT não executa ordem — produz TMP" (AGENTS.md §6.9/EUA-E19a: o produto é o Signal Package) e `especificador.md:96` "Constitution Check (CC-01..CC-10)" (vai até CC-12; escapou à correção anterior, `DHR-PRE-ENTREGA-001`).

## 2. Decisão de Andraus `[FATO]`
Aplicar o **A9-teste**: corrigir as duas linhas e instalar um teste que impede a reincidência dos cinco fatos defasados conhecidos. O **A9-completo** (checklist único D/H que os agentes citam por ID) **não** é decidido aqui: fica para depois da medição do próximo Plan.

## 3. Mudança `[FATO]`
- `.claude/agents/revisor.md` (Passo 2) e `.claude/agents/especificador.md` (§4, item 1): uma linha cada, texto do patch pré-testado. Carimbos RPSA alinhados por `check_rpsa.py --register`.
- `tests/test_agentes_sem_fatos_defasados.py` (novo, 2 testes) e passo no CI. Lista **fechada** de 5 frases, cada uma com a autoridade que a corrigiu; inclui teste de mutação (o detector não pode ficar mudo).
- Limite honesto: só pega deriva **conhecida**; deriva nova exige acrescentar a frase ao teste.

## 4. Pré-teste `[FATO]`
Antes da aplicação o teste falhava exatamente nas duas linhas; com o patch numa cópia passou (`git apply --check` OK). Resultado após aplicar: ver o registro no `HANDOFF.md`.

## 5. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 6. Registro
- [x] Esta ata · [x] emenda nos dois agentes · [x] teste e CI · [x] carimbo RPSA · [ ] merge (ordem de Andraus)
