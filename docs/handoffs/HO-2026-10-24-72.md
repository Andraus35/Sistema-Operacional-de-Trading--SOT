---
handoff_id: HO-2026-10-24-72
previous: HO-2026-10-24-71
data: 2026-10-24
branch: ccr-3235944c-duo3sl
base_commit: 74b1de3
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12 HOMOLOGADAS; SPEC-007 = ABERTURA HOMOLOGADA (DHR-SPEC007-001), DIVIDIDA pela Opção C (DHR-SPEC007-002): reduzida a formação + selo, Plan v1.2 candidato NÃO CONFORME (não é baseline); SPEC-048 = slot indicativo, NÃO aberta
fase: spec-first
autor: Orquestrador
anexo: governance/propostas/SPEC-007/BRIEFING-PLAN-SPEC007-2026-10-19.md
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Frente atual (Andraus, chat 2026-10-23/24)
- **Plan da SPEC-007 (ordem de Andraus 2026-10-23):** Plan v1.2 + checks em `specs/features/SPEC-007/`; Revisor reprovou 3× (R1 9 Médias, R2 5, R3 5; 0 Críticas; pareceres R1–R3 em `governance/propostas/SPEC-007/`). Plan v1.2 = 20 RULE-KFH, 20 BASpec, 13 EC, 26 cenários, 29 ADV; gates determinísticos verdes.
- **Divisão decidida e ATA REGISTRADA (chat 2026-10-24, `DHR-SPEC007-002`):** Opção C. SPEC-007 = formação + selo + atos de autorização + trava de envio externo; **SPEC-048 — RAG Retrieval & Evidence Packet Harness** = recuperação + pacote com citação + WikiRAG + F2 + defesa da consulta (slot indicativo, **NÃO aberta**). Re-apontamentos em SPEC-002/003/006/020 só **listados** (errata aditiva depois, no Plan da SPEC-048); BL-017 ganhou nota aditiva (gatilho extra `spec:SPEC-048 em redação`, estado `Em espera`); `SPEC-007-SPLIT-001` FECHADA; ROADMAP e CATALOGO atualizados com texto anterior preservado; CONFLICT-MAP não alterado. Correção: SPEC-047 está reservado a Runtime Cognitive Caching (a abertura errou); SPEC-048 estava livre.
- **Perguntas P-1..P-11 respondidas por Andraus (chat 2026-10-24) e REGISTRADAS em `DHR-SPEC007-003`** (todas na opção recomendada): só a identidade confirmada de Andraus grava atos (ACTREC); só ele libera uso (RIGHTS) e envio externo (EXTTX; modelo de terceiro contratado = "fora"); derivado herda a restrição (DERIVTX); conhecimento de fontes entra como `learning` (NODETYPE); troca de carimbado só por ele, em lote (SUCC); pacote de evidência direto ao analista, só leitura (BBTYPE → SPEC-048); lista de carimbadores aprovada por ele + conferência por modelo diferente e separada + visto por lote só de definições e regras (P-1/P-2 — decide parte de `SPEC-006 plan.md` l.482; **K-001 segue ABERTA**); emenda de fidelidade à SPEC-020 por metade; COL-EXP-05 reconciliado (BL-011 segue ATIVADO). São decisões de política: viram texto normativo só nos Plans homologados. ROADMAP "Decisões FECHADAS" e CATALOGO atualizados; CONFLICT-MAP, SPEC-006 l.482, SPEC-020 e RMR-001 **não** alterados (sem ordem).
- **Nada foi homologado como baseline.** Fail-closed do Plan v1.2 agora é a regra: sem registro de ato de Andraus nada vale, linha parada até a 1ª liberação real. Livro (Q7c) segue adiado.

## 2. Estado (fatos conferidos em 2026-10-24)
- `main` = `74b1de3` (PR #129). Ramo `ccr-3235944c-duo3sl` leva Plan v1.2, checks, 3 pareceres e este handoff. Benchmark `/home/user/andraus35/inteligencia-sot@0abd22e` AUSENTE nesta sessão: as 7 citações `inteligencia-sot@0abd22e:` do Plan não foram conferidas (adendo da guarda pós-revisor; `add_repo` read se precisar).
- Verificadores sem ERRO na entrega (`check_refs` 0, `check_doc_sync` 0, `check_repo_research` OK, mapa em dia). BL-010/017/035 vinculados à abertura, sem promoção (só Andraus). BL-029 = `Em espera` no painel (o parecer R1 estava desatualizado).
- O Plan v1.2 preserva v1.0/v1.1 nos Anexos (INV-07). O cabeçalho da SPEC-006 ainda diz "1.12 ERRATA PROPOSTA" (fora do escopo do Especificador).

## 3. Lições
Roteador exige linhas `ALVO:` (um único caminho), `BASE:` e `PARECER:` em linha própria; revisão por delta sem `spec_delta` (v1.x não commitada) vira integral na prática — commitar versões intermediárias do Plan permite delta de verdade. O Especificador parou uma vez por limite de uso: retomar por `SendMessage`. A guarda pós-revisor acusa falso positivo de contagem em texto histórico entre colchetes e caminhos curtos (`SPEC-006/plan.md`): conferir e anotar adendo. Placeholder de ata com formato de ID em texto de Spec quebra `check_refs`.

## 4. Verificado
`validate_spec_sot` 13/13, `revisor_gate --rapido` PASSOU_D, `check_invariants` 0, `check_refs` 0 ERRO, `check_doc_sync`, `check_repo_research --all`, `backlog_triggers --abertura SPEC-007`, `build_map --check` — verdes na v1.2. Suíte completa de testes NÃO rodada nesta sessão (só documentos).

## 5. Próximo passo único
(a) **Abertura da SPEC-048** (só por ordem de Andraus): Especificador faz Dossiê próprio (RULE-ECC-01/02/06, atomic-spec §15; `research.md` da SPEC-007 é insumo), proposta de abertura com perguntas, Revisor, homologação de Andraus; o Plan da SPEC-048 propõe a errata aditiva de re-apontamento (lista na ata §4). (b) **Plan reduzido da SPEC-007** (só por ordem de Andraus): partir do v1.2 e tratar R3-M1..M5 nas partes que ficarem (M1 pré-condições por cenário P-1+VALIDADO+P-3; M2 `material_hash`/`record_hash`; M3 quadro de pré-requisitos mínimos P-1/P-3/P-10/P-4a/P-4b; M4 `knowledge_kind` no hash; M5 envelope da CIM por `content_ref`); **commitar cada versão do Plan** para o Revisor poder fazer delta de verdade; redeclarar Disposição de BL-010/017/035. (c) Plan reduzido e Plan da SPEC-048 devem incorporar `DHR-SPEC007-003` (marcas [DECISÃO NECESSÁRIA] → decididas) e propor a errata aditiva à SPEC-006 l.482; livro (Q7c): decisão de Andraus. (d) Piloto de esforço depois do Plan. **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-SPEC007-003`, `DHR-SPEC007-002`, `DHR-SPEC007-001`, `DHR-BENCH-INTEL-001`, `DHR-H001-001`, `DHR-SPEC006-004`, `DHR-ROTEAMENTO-003`, `DHR-COESAO-005`, `DHR-PCC-003`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
Dar Bash ao Revisor; refazer a SPEC-006; usar motores/agentes/skills do Inteligencia-SOT (Benchmark apenas); copiar texto/código dele; incluir o livro como fonte; tratar o Plan v1.2 como pronto (3× NÃO CONFORME); abrir a SPEC-048 ou escrever Plan de qualquer das duas sem ordem expressa; editar baselines (SPEC-002/003/006/020) antes da errata homologada.

## 8. Não tocar
`canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md`, `CONFLICT-MAP`, selo `GATE-MANIFEST.sha256` (só por Andraus).

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (74b1de3) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `gate_manifest.py --check`; `check_refs`/`check_doc_sync`/`check_handoff`/`check_rpsa`/`check_coesao`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/017/035 vinculados, sem promoção)
- [ ] PRs abertos; se o ramo `ccr-3235944c-duo3sl` já foi mesclado, tratar follow-up como mudança nova
- [ ] ROADMAP: SPEC-007 "ABERTURA HOMOLOGADA" + divisão (DHR-SPEC007-002); SPEC-048 indicativa; "Decisões abertas ativas" sem H-001
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
**Só de Andraus:** ordem para abrir a SPEC-048 e para o Plan reduzido da SPEC-007 · ordens para errata/CONFLICT-MAP decorrentes de `DHR-SPEC007-003` · livro (Q7c) · demais decisões abertas (G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001) · destino do Auditor Externo (PAUSADO), D-PCC-3/4/5.

## 11. Ponteiros
`specs/features/SPEC-007/` (ABERTURA, research, plan v1.2, checks) · `governance/propostas/SPEC-007/` (briefing-anexo e pareceres R1–R3) · `governance/DHR-SPEC007-003_*` (respostas P-1..P-11) · `governance/DHR-SPEC007-002_*` (divisão) · `governance/DHR-SPEC007-001_*` · `governance/DHR-BENCH-INTEL-001_*` · `ROADMAP.md` · `AGENTS.md` §11 · `docs/handoffs/HO-2026-10-24-71.md` · `docs/mapa/MAPA-PROJETO.md`
