---
handoff_id: HO-2026-10-24-75
previous: HO-2026-10-24-74
data: 2026-10-24
branch: ccr-3235944c-duo3sl
base_commit: 74b1de3
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12 HOMOLOGADAS; SPEC-007 = ABERTURA HOMOLOGADA (DHR-SPEC007-001), DIVIDIDA pela Opção C (DHR-SPEC007-002): reduzida a formação + selo; Plan reduzido v2.3 = HOMOLOGADO — BASELINE (DHR-SPEC007-005, Andraus 2026-10-24; Revisor R6 CONFORME condicional; sem BUILD); SPEC-048 = ABERTURA HOMOLOGADA (DHR-SPEC048-001; Plan pendente; não é baseline); SPEC-049 (WikiRAG Reading View) = slot indicativo, NÃO aberta
fase: spec-first
autor: Orquestrador
anexo: null
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Frente atual (Andraus, chat 2026-10-23/24)
- **SPEC-007 reduzida (formação + selo): Plan v2.3 HOMOLOGADO — BASELINE** (`DHR-SPEC007-005`), depois de divisão (`002`) e respostas P-1..P-14 (`003`, `004`). Sem BUILD; fail-closed: nada é liberado ou carimbado sem ato de Andraus. Errata SPEC-006 (E-1..E-4) e emenda SPEC-020 (metade F1): passos à parte, não redigidos. Anexo de tarefa AT-SPEC007-PLAN CONSUMIDO (movido para `docs/handoffs/anexos/`).
- **SPEC-048 (RAG Retrieval & Evidence Packet Harness): ABERTURA HOMOLOGADA** (Andraus, chat 2026-10-24, `DHR-SPEC048-001`; Revisor R1 e R2 CONFORME condicional; gate PASSOU_D). Decididos: CRITICAL D0–D8; **página de leitura WikiRAG separada na SPEC-049 (slot indicativo, NÃO aberta; peso MEDIUM D0–D5/Classe D só proposta até a abertura dela)**; todo analista conta como "fora" até Andraus confirmar modelos de casa; rótulo carimbado × trecho de fonte; resumo desligado até Andraus ligar; gatilho aditivo `∨ spec:SPEC-048 em redação` em BL-017/BL-010 (Estado inalterado, `backlog_triggers --abertura SPEC-048` lista os dois); regra de busca para a errata; confronto com WORKFLOW sem pesquisar escolas; notas aditivas de endereço na SPEC-007 plan e na ata 002. SPEC-047 estava reservado a Runtime Cognitive Caching (a abertura da SPEC-007 errou).
- **Nada foi homologado como Plan da SPEC-048 nem da SPEC-049 (só a abertura da 048, DHR-SPEC048-001).** Condições do Plan da SPEC-048 em `ABERTURA.md` §15 (literal do ponto 3 da Interface; dispor CBP-002/004/005 e RULE-BB-001 por causa da P-9 — silêncio = Crítica; amostragem de falso-ACEITE do juiz F2; coordenar a errata com a metade F1 da SPEC-020; Disposição de BL-017/BL-010; lacuna analista↔modelo; errata por critério de busca).

## 2. Estado (fatos conferidos em 2026-10-24)
- `main` = `74b1de3` (PR #129). Ramo `ccr-3235944c-duo3sl` leva Plan v1.2, checks, 3 pareceres e este handoff. Benchmark `/home/user/andraus35/inteligencia-sot@0abd22e` AUSENTE nesta sessão: as 7 citações `inteligencia-sot@0abd22e:` do Plan não foram conferidas (adendo da guarda pós-revisor; `add_repo` read se precisar).
- Verificadores sem ERRO na entrega (`check_refs` 0, `check_doc_sync` 0, `check_repo_research` OK, mapa em dia). BL-010/017/035 vinculados à abertura, sem promoção (só Andraus). BL-029 = `Em espera` no painel (o parecer R1 estava desatualizado).
- O Plan v1.2 preserva v1.0/v1.1 nos Anexos (INV-07). O cabeçalho da SPEC-006 ainda diz "1.12 ERRATA PROPOSTA" (fora do escopo do Especificador).

## 3. Lições
Roteador exige linhas `ALVO:` (um único caminho), `BASE:` e `PARECER:` em linha própria; revisão por delta sem `spec_delta` (v1.x não commitada) vira integral na prática — commitar versões intermediárias do Plan permite delta de verdade. O Especificador parou uma vez por limite de uso: retomar por `SendMessage`. A guarda pós-revisor acusa falso positivo de contagem em texto histórico entre colchetes e caminhos curtos (`SPEC-006/plan.md`): conferir e anotar adendo. Placeholder de ata com formato de ID em texto de Spec quebra `check_refs`. **Rodar a suíte completa (`python -m unittest discover -s tests`) a cada versão do Plan:** o teste de calibração dos detectores reprova se um plan.md tiver "N BASpecs" maior que o nº de cabeçalhos (texto histórico de anexos: escrever "N BASpec" no singular ou por extenso).

## 4. Verificado
`validate_spec_sot` 13/13, `revisor_gate --rapido` PASSOU_D, `check_invariants` 0, `check_refs` 0 ERRO, `check_doc_sync`, `check_repo_research --all`, `backlog_triggers --abertura SPEC-007`, `build_map --check` — verdes na v1.2. Suíte completa de testes NÃO rodada nesta sessão (só documentos).

## 5. Próximo passo único
(a) **Plan da SPEC-048** (só por ordem de Andraus): Especificador (opus) com `ABERTURA.md` Revisão 4 §15, o Anexo T da SPEC-007 plan.md (partes que ficam) e `research.md`; Revisor; **commitar cada versão do Plan** para delta real. (b) **Abertura da SPEC-049** (só por ordem de Andraus): Dossiê próprio (insumo: SRC-LLMWIKI, SRC-GRAPHRAG, REPO-graphrag), proposta, Revisor, homologação. (c) Passos à parte, cada um só por ordem: errata aditiva à SPEC-006 (E-1..E-4), emenda à SPEC-020 (metade F1; F2 vai com a SPEC-048), errata de re-apontamento (critério de busca da ata 048-001). (d) Antes de qualquer BUILD: Andraus registrar as primeiras liberações (ACTREC/RIGHTS/EXT/LOCAL_EXECUTOR) e definir a forma de confirmar sua identidade; fase spec-first. (e) Livro (Q7c): decisão de Andraus. (f) Piloto de esforço depois do Plan. **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-SPEC048-001`, `DHR-SPEC007-005`, `DHR-SPEC007-004`, `DHR-SPEC007-003`, `DHR-SPEC007-002`, `DHR-SPEC007-001`, `DHR-BENCH-INTEL-001`, `DHR-H001-001`, `DHR-SPEC006-004`, `DHR-ROTEAMENTO-003`, `DHR-COESAO-005`, `DHR-PCC-003`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
Dar Bash ao Revisor; refazer a SPEC-006; usar motores/agentes/skills do Inteligencia-SOT (Benchmark apenas); copiar texto/código dele; incluir o livro como fonte; tratar o Plan v1.2 como pronto (3× NÃO CONFORME); abrir a SPEC-048 ou escrever Plan de qualquer das duas sem ordem expressa; editar baselines (SPEC-002/003/006/020) antes da errata homologada.

## 8. Não tocar
`canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md`, `CONFLICT-MAP`, selo `GATE-MANIFEST.sha256` (só por Andraus).

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (74b1de3) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `gate_manifest.py --check`; `check_refs`/`check_doc_sync`/`check_handoff`/`check_rpsa`/`check_coesao`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/017 também vinculados à SPEC-048 e BL-035 à SPEC-007, sem promoção)
- [ ] PRs abertos; se o ramo `ccr-3235944c-duo3sl` já foi mesclado, tratar follow-up como mudança nova
- [ ] ROADMAP: SPEC-007 reduzida baseline (DHR-SPEC007-005); SPEC-048 abertura homologada (DHR-SPEC048-001); SPEC-049 indicativa; "Decisões abertas ativas" sem H-001
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
**Só de Andraus:** ordem para o Plan da SPEC-048 e para a abertura da SPEC-049 · ordem para a errata SPEC-006, a emenda SPEC-020 e a errata de re-apontamento · ordens para errata/CONFLICT-MAP decorrentes de `DHR-SPEC007-003/004` · livro (Q7c) · demais decisões abertas (G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001) · destino do Auditor Externo (PAUSADO), D-PCC-3/4/5.

## 11. Ponteiros
`specs/features/SPEC-007/` (ABERTURA, research, plan v1.2, checks) · `governance/propostas/SPEC-007/` (briefing-anexo e pareceres R1–R3) · `governance/DHR-SPEC048-001_*` (abertura SPEC-048) · `specs/features/SPEC-048/` (ABERTURA, research, sources) · `governance/propostas/SPEC-048/` (pareceres) · `governance/DHR-SPEC007-005_*` (homologação) · `governance/DHR-SPEC007-004_*` (P-12..P-14) · `governance/DHR-SPEC007-003_*` (respostas P-1..P-11) · `governance/DHR-SPEC007-002_*` (divisão) · `governance/DHR-SPEC007-001_*` · `governance/DHR-BENCH-INTEL-001_*` · `ROADMAP.md` · `AGENTS.md` §11 · `docs/handoffs/HO-2026-10-24-74.md` · `docs/mapa/MAPA-PROJETO.md`
