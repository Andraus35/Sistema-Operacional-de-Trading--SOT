# DHR-REVISOR-DELTA-001 — Ata — Revisor SOT passa a revisar por delta (hash por bloco) nas rodadas seguintes

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada no chat** (2026-10-17: "Ajustar o prompt do Revisor para usar o delta"; antes, "Sim, script de delta por hash + evidência amarrada à versão"). Entra no repositório por PR; não fecha nem abre decisão aberta. |
| Compatibilidade | Aditiva (INV-07). Reversível por `git revert`. Não altera o Passo 5-bis, o teto de veredito (§3/§8) nem o gate determinístico. |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Acrescenta a seção §3-bis (revisão por delta com hash) ao `.claude/agents/revisor.md`; o carimbo dos agentes é alinhado. |

## 1. Origem `[FATO]`
Auditoria de custo (2026-10-17): sessão com ~600 mil tokens de contexto, subagentes de 120–360 mil tokens por rodada relendo `plan.md` (~1,7 mil linhas), `checks.md` e as fontes do zero. Medição: entre a v1.9 e a v1.10 da SPEC-006, **103 de 122 blocos (84%)** ficaram idênticos (`scripts/spec_delta.py`). Ferramentas entregues antes desta ata: `spec_delta.py`, `documento_sha256` na evidência do gate e `revisor_gate.py --verificar` (AGENTS.md §8).

## 2. Mudança no `revisor.md` `[DECISÃO DE ANDRAUS]`
Nova seção **§3-bis**: com o delta e o parecer anterior em arquivo, o Revisor (1) revisa integralmente os blocos alterados/adicionados/removidos; (2) revisa também os **dependentes** (todo bloco que cita um ID alterado — causa-raiz das rodadas lentas); (3) pode marcar **HERDADO** o bloco inalterado já conferido, com fonte de mesmo `sha256`; (4) reconfere **≥5 blocos inalterados** por amostra anti-leniência; (5) mantém integral cabeçalho/Status, contagens, decisões abertas, Constitution Check, Herança/Delta e §8; (6) **não usa delta** na primeira rodada, sem parecer anterior/delta, com >50% de blocos alterados, mudança de Complexidade/Profundidade, parecer anterior Crítico ou hash da evidência divergente; (7) entrega tabela de cobertura por bloco e o `sha256` do documento. O delta diz *o que mudou* (Classe D); o *sentido* segue sendo do Revisor (Classe P).

## 3. Como o orquestrador aciona `[FATO]`
`python scripts/spec_delta.py specs/features/SPEC-nnn/plan.md --base <commit-da-versão-revisada> --json` (+ `python scripts/revisor_gate.py <plan.md> --out evidence.json`) e passa ao Revisor o delta, o parecer anterior em arquivo e o `evidence.json`.

## 4. Permanecem ABERTAS (CONS-01)
H-001, M-001, J-001, N-001, G-001, K-001, C-001, WF-D03, ECC-03-001, CKG-STRUCT-ORIGIN-001. Nada foi fechado. Roteamento de modelos por complexidade (Opus 4.8 / Sonnet 5.5 / Sonnet 4.6) continua **adiado** por decisão de Andraus (2026-10-17).
