---
handoff_id: HO-2026-10-24-73
previous: HO-2026-10-24-72
data: 2026-10-24
branch: ccr-3235944c-duo3sl
base_commit: 74b1de3
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12 HOMOLOGADAS; SPEC-007 = ABERTURA HOMOLOGADA (DHR-SPEC007-001), DIVIDIDA pela Opção C (DHR-SPEC007-002): reduzida a formação + selo; Plan reduzido v2.3 = CANDIDATO, parecer R6 CONFORME condicional, aguarda homologação de Andraus (não é baseline); SPEC-048 = slot indicativo, NÃO aberta
fase: spec-first
autor: Orquestrador
anexo: governance/propostas/SPEC-007/BRIEFING-PLAN-SPEC007-2026-10-19.md
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Frente atual (Andraus, chat 2026-10-23/24)
- **Plan da SPEC-007:** v1.2 (Revisor 3× NÃO CONFORME) → divisão Opção C decidida (`DHR-SPEC007-002`; SPEC-007 = formação + selo; **SPEC-048** = recuperação + pacote, slot indicativo, NÃO aberta) → respostas P-1..P-11 (`DHR-SPEC007-003`) e P-12..P-14 + ordem da rodada 5 (`DHR-SPEC007-004`) → Plan reduzido v2.0 (R4: 2 Médias) → v2.1 (R5: 1 Média) → v2.2 (**R6: CONFORME condicional**, 0 Críticas/Médias, 3 Menores) → **v2.3** (3 Menores editoriais r6-n1..n3 fechados; sem nova rodada, como sugeriu o Revisor). Pareceres R1–R6 em `governance/propostas/SPEC-007/`. Contagens vigentes: 12 RULE-KFH, 2 INV, 12 BASpec, 12 EARS, 9 EC, 18 cenários, 22 ADV. Gates verdes na v2.3 (`revisor_gate` completo = PASSOU_D, que cumpre a condição do Revisor).
- **O Plan v2.3 é CANDIDATO.** Baseline só por homologação de Andraus (ata própria). **A decidir por ele na homologação:** (f3) só a letra da ata (texto solto de fonte) ou a regra mais estrita do Plan; errata aditiva ao caderno SPEC-006 (E-1..E-4, P-13: só proposta); emenda de fidelidade à SPEC-020 (metade F1); INVALIDATION "só Andraus" (r4-n8, [PROPOSTA]); forma de confirmar a identidade de Andraus (BUILD).
- **Nenhuma decisão aberta foi fechada** além das registradas nas atas 002/003/004; K-001, M-001 e demais seguem ABERTAS. Fail-closed vale: sem registro de ato de Andraus nada é carimbado nem liberado, linha parada.

## 2. Estado (fatos conferidos em 2026-10-24)
- `main` = `74b1de3` (PR #129). Ramo `ccr-3235944c-duo3sl` leva Plan v1.2, checks, 3 pareceres e este handoff. Benchmark `/home/user/andraus35/inteligencia-sot@0abd22e` AUSENTE nesta sessão: as 7 citações `inteligencia-sot@0abd22e:` do Plan não foram conferidas (adendo da guarda pós-revisor; `add_repo` read se precisar).
- Verificadores sem ERRO na entrega (`check_refs` 0, `check_doc_sync` 0, `check_repo_research` OK, mapa em dia). BL-010/017/035 vinculados à abertura, sem promoção (só Andraus). BL-029 = `Em espera` no painel (o parecer R1 estava desatualizado).
- O Plan v1.2 preserva v1.0/v1.1 nos Anexos (INV-07). O cabeçalho da SPEC-006 ainda diz "1.12 ERRATA PROPOSTA" (fora do escopo do Especificador).

## 3. Lições
Roteador exige linhas `ALVO:` (um único caminho), `BASE:` e `PARECER:` em linha própria; revisão por delta sem `spec_delta` (v1.x não commitada) vira integral na prática — commitar versões intermediárias do Plan permite delta de verdade. O Especificador parou uma vez por limite de uso: retomar por `SendMessage`. A guarda pós-revisor acusa falso positivo de contagem em texto histórico entre colchetes e caminhos curtos (`SPEC-006/plan.md`): conferir e anotar adendo. Placeholder de ata com formato de ID em texto de Spec quebra `check_refs`. **Rodar a suíte completa (`python -m unittest discover -s tests`) a cada versão do Plan:** o teste de calibração dos detectores reprova se um plan.md tiver "N BASpecs" maior que o nº de cabeçalhos (texto histórico de anexos: escrever "N BASpec" no singular ou por extenso).

## 4. Verificado
`validate_spec_sot` 13/13, `revisor_gate --rapido` PASSOU_D, `check_invariants` 0, `check_refs` 0 ERRO, `check_doc_sync`, `check_repo_research --all`, `backlog_triggers --abertura SPEC-007`, `build_map --check` — verdes na v1.2. Suíte completa de testes NÃO rodada nesta sessão (só documentos).

## 5. Próximo passo único
(a) **Homologação do Plan reduzido da SPEC-007 v2.3 por Andraus** (ou nova rodada, se ele quiser): o Orquestrador prepara a ata (DHR) com os itens de §1; só Andraus homologa. (b) **Abertura da SPEC-048** (só por ordem de Andraus): Dossiê próprio (RULE-ECC-01/02/06, atomic-spec §15; `research.md` da SPEC-007 é insumo), proposta, Revisor, homologação; o Anexo T do plan.md é insumo do Plan dela; o Plan dela propõe a errata aditiva de re-apontamento (ata 002 §4). (c) Livro (Q7c): decisão de Andraus. (d) Piloto de esforço depois do Plan. **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-SPEC007-004`, `DHR-SPEC007-003`, `DHR-SPEC007-002`, `DHR-SPEC007-001`, `DHR-BENCH-INTEL-001`, `DHR-H001-001`, `DHR-SPEC006-004`, `DHR-ROTEAMENTO-003`, `DHR-COESAO-005`, `DHR-PCC-003`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

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
**Só de Andraus:** homologar (ou não) o Plan reduzido v2.3 · ordem para abrir a SPEC-048 · ordens para errata/CONFLICT-MAP decorrentes de `DHR-SPEC007-003/004` · livro (Q7c) · demais decisões abertas (G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001) · destino do Auditor Externo (PAUSADO), D-PCC-3/4/5.

## 11. Ponteiros
`specs/features/SPEC-007/` (ABERTURA, research, plan v1.2, checks) · `governance/propostas/SPEC-007/` (briefing-anexo e pareceres R1–R3) · `governance/DHR-SPEC007-004_*` (P-12..P-14) · `governance/DHR-SPEC007-003_*` (respostas P-1..P-11) · `governance/DHR-SPEC007-002_*` (divisão) · `governance/DHR-SPEC007-001_*` · `governance/DHR-BENCH-INTEL-001_*` · `ROADMAP.md` · `AGENTS.md` §11 · `docs/handoffs/HO-2026-10-24-72.md` · `docs/mapa/MAPA-PROJETO.md`
