# DHR-TELEMETRIA-CUSTO-001 — Ata de Decisão — Telemetria de tokens dos agentes Construtores (BL-036, 1ª fatia)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Revisor SOT / Controlador |
| Ref | Resposta de Andraus (chat, 2026-10-31, AskUserQuestion): "Medir tokens nos pareceres (Recomendado)" · BL-036 · `governance/propostas/TELEMETRIA-CUSTO/PESQUISA-TELEMETRIA-CUSTO-TOKENS-2026-10-31.md` |
| Data | 2026-10-31 |
| Status | **DECISÃO REGISTRADA** (decisão direta de Andraus em chat; AGENTS.md §10). Aditiva (INV-07); reversível por `git revert`. |
| Compatibilidade | Patch (novo detector; não altera método, agentes nem arquivo selado). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Novo script detector, hook PostToolUse e tabela de preços; não altera texto de agente de construção nem método. |

## 1. Decisão `[FATO]`
Implementar já a medição de tokens dos agentes **Construtores (AC)**. Agentes de Trading (AT) não existem (spec-first) e ficam para a SPEC-040.
1. `scripts/telemetria_tokens.py` + wrapper `scripts/telemetria-tokens.js` (PostToolUse/Agent): grava metadados por chamada (agente, modelo, classe de tarefa, tokens in/out/cache, duração) em `.telemetria/uso-tokens.jsonl` (gitignored). **Não grava texto de prompt nem de resposta.** CLI `resumo` agrega por agente/modelo/classe.
2. `governance/telemetria/PRECOS-MODELOS.json` (versionada): **todos os preços `null`** — custo = INDETERMINADO até Andraus (ou fonte oficial citada) preencher. Nenhum preço foi inventado.
3. `MECANISMOS.json` (`hook.telemetria-tokens`, `lib.telemetria-tokens`), CI (`tests/test_telemetria_tokens.py`), `.gitignore`.

## 2. Ressalvas `[FATO]`
- **Detector (ENF-03):** nunca nega nem altera a chamada; falha = silêncio. Não é gate.
- `roteador_modelos.py` (selado em `GATE-MANIFEST.sha256`) **não foi alterado**; a coleta é um script novo e separado.
- Custo fora do Conviction Vector (INV-04; RULE-KFH-014). Tokens ≠ qualidade: Economicidade nunca acima de Eficácia (4Es).
- **Validado ao vivo (2026-10-31):** uma chamada real de agente (Explore/haiku) gravou in=2, out=221, cache_read=40828, cache_create=535, total=41586 e 9,5 s; o subagente aparece como linha própria. Ainda não testado com Especificador/Revisor SOT.
- Teste pai-filho (2026-10-31): subagente sem ferramenta Agent => sem aninhamento, sem contagem dupla nesta configuração. `resumo --por-spec` liga tokens à Spec (campos `spec`/`alvo` extraídos do prompt).
- 3ª fatia: CLI `custo-beneficio` (tokens × rodadas/achados por Spec, via `loop_ledger.coletar`); sem telemetria da Spec => n/m. Menos tokens por achado não é melhor por si (Eficiência só sobre Eficácia válida).
- Integrado ao `loop_ledger.py` (2ª fatia): CLI `snapshot` + `governance/aprendizado/TELEMETRIA-TOKENS.md`; Economicidade = PARCIAL (custo USD segue INDETERMINADO). Nenhuma decisão aberta foi fechada (CONS-01); BL-036 segue `Em espera`.

## 3. Registro
- [x] Esta ata · [x] script + wrapper + teste · [x] `MECANISMOS.json` · [x] CI · [x] settings.json · [ ] merge (assinatura)
