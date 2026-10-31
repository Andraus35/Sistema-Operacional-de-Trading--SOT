# DHR-HIGIENE-001 — Ata de Decisão — Pendências baratas de higiene (status de atas e referências)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador |
| Ref | Ordem de Andraus (chat, 2026-10-31): "Aplicar as pendências baratas agora" · `AGENTS.md` §10 · `governance/propostas/MELHORIAS-PROCESSO/AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (B4, B10) |
| Data | 2026-10-31 |
| Status | **APLICADA por ordem de Andraus** (AGENTS.md §10). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Edita status/texto de atas e registros de governança; não toca agentes de construção, método nem AGENTS.md. |

## 1. Escopo `[FATO]`
1. **COE-11 (3 atas):** `DHR-ASK-002`, `DHR-AUDITOR-EXTERNO-008` e `DHR-AUDITOR-EXTERNO-009` tinham Status "PROPOSTA — vira vigente só com o merge de Andraus", mas já estão na `main` por merge de Andraus (PR #111 e PR #103, conferido no `git log`). O Status passou a "MESCLADA na `main` por Andraus — vigente", com o **texto anterior preservado entre aspas** (INV-07). Em 008 e 009 a nota mantém que os itens que a própria ata declara diferidos (ex.: R4, emenda F3 do `revisor.md`) **seguem diferidos** — nada foi promovido além do que foi mesclado.
2. **check_refs (2 avisos reais):** em `AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md` a menção a `RULE-REV-01..03` passou a dizer que é proposta sem registro em `RULES.md` (RULE-HG-02); em `PCC-001_..._PROPOSTA.md` o caminho histórico `docs/handoff/HANDOFF.md` (opção não adotada) deixou de estar entre crases e ganhou a nota "o handoff vive na raiz".

## 2. Fora do escopo (permanecem como estão) `[FATO]`
Status dos 33 arquivos `_PROPOSTA` (exige conferir um a um), configs órfãs da raiz, `revisao-independente/`, nomes de `reference/`, subpastas de `governance/`, aviso de `SPEC-007/plan.md:2650` (baseline: só por erratum), e os cortes do ROADMAP.

## 3. Efeito medido `[FATO]`
`check_coesao`: INFO 5→2 (some COE-11; ficam 2 COE-09). `check_refs`: WARN 2→0, ERRO=0.

## 4. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 5. Registro
- [x] Esta ata · [x] texto anterior preservado nos 3 status · [ ] merge (assinatura de Andraus)
