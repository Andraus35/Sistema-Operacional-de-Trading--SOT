---
handoff_id: HO-2026-10-24-70
previous: HO-2026-10-19-69
data: 2026-10-24
branch: ccr-3235944c-duo3sl
base_commit: 74b1de3
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12 HOMOLOGADAS; SPEC-007 = ABERTURA HOMOLOGADA (DHR-SPEC007-001); Plan v1.2 CANDIDATO, NÃO CONFORME em 3 rodadas (não é baseline); Andraus decidiu DIVIDIR a Spec (Opção C da ABERTURA §3) — ata e reabertura pendentes
fase: spec-first
autor: Orquestrador
anexo: governance/propostas/SPEC-007/BRIEFING-PLAN-SPEC007-2026-10-19.md
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Frente atual (Andraus, chat 2026-10-23/24)
- **Ordem do Plan da SPEC-007 dada** (chat 2026-10-23, "Sim, abrir o Plan"). Especificador (opus) produziu `specs/features/SPEC-007/plan.md` + `checks.md`; Revisor (opus integral R1; sonnet R2/R3) reprovou 3 vezes: **R1** 9 Médias (`PARECER-...-PLAN-R1-2026-10-23.md`), **R2** 5 Médias (`...-R2-...`), **R3** 5 Médias R3-M1..M5 (`...-R3-2026-10-24.md`), todos em `governance/propostas/SPEC-007/`. 0 Críticas em todas; Plan v1.2 = 20 RULE-KFH, 20 BASpec, 13 EC, 26 cenários, 29 ADV. Gates determinísticos verdes na v1.2.
- **Decisão de Andraus (chat 2026-10-24):** após a R3, escolheu **dividir a Spec** e, perguntado, o desenho = **Opção C** (`ABERTURA.md` §3 e `SPEC-007-SPLIT-001`): a SPEC-007 fica com formação + selo (o que a SPEC-006 referencia); a recuperação/pacote de evidência vira Spec nova, com erratum de re-apontamento (`research.md` §8.1). **Isto altera a abertura homologada (DHR-SPEC007-001): ainda NÃO há ata, ROADMAP/CATALOGO não foram editados, número e Dossiê da Spec nova não existem.** Não é baseline.
- **Nada foi homologado, nenhuma decisão aberta foi fechada.** Novas [DECISÃO NECESSÁRIA] propostas pelo Plan (IDs só propostos): SPEC-007-NODETYPE-001, SUCC-001, RIGHTS-001, EXTTX-001, BBTYPE-001, ACTREC-001, DERIVTX-001; perguntas P-1..P-11 ao fim do Plan. Pelo fail-closed, até Andraus decidir a linha de montagem fica parada.

## 2. Estado (fatos conferidos em 2026-10-24)
- `main` = `74b1de3` (PR #129). Ramo `ccr-3235944c-duo3sl` leva Plan v1.2, checks, 3 pareceres e este handoff. Benchmark `/home/user/andraus35/inteligencia-sot@0abd22e` AUSENTE nesta sessão: as 7 citações `inteligencia-sot@0abd22e:` do Plan não foram conferidas (adendo da guarda pós-revisor; `add_repo` read se precisar).
- Verificadores sem ERRO na entrega (`check_refs` 0, `check_doc_sync` 0, `check_repo_research` OK, mapa em dia). BL-010/017/035 vinculados à abertura, sem promoção (só Andraus). BL-029 = `Em espera` no painel (o parecer R1 estava desatualizado).
- O Plan v1.2 preserva v1.0/v1.1 nos Anexos (INV-07). O cabeçalho da SPEC-006 ainda diz "1.12 ERRATA PROPOSTA" (fora do escopo do Especificador).

## 3. Lições
Roteador exige linhas `ALVO:` (um único caminho), `BASE:` e `PARECER:` em linha própria; revisão por delta sem `spec_delta` (v1.x não commitada) vira integral na prática — commitar versões intermediárias do Plan permite delta de verdade. O Especificador parou uma vez por limite de uso: retomar por `SendMessage`. A guarda pós-revisor acusa falso positivo de contagem em texto histórico entre colchetes e caminhos curtos (`SPEC-006/plan.md`): conferir e anotar adendo. Placeholder de ata com formato de ID em texto de Spec quebra `check_refs`.

## 4. Verificado
`validate_spec_sot` 13/13, `revisor_gate --rapido` PASSOU_D, `check_invariants` 0, `check_refs` 0 ERRO, `check_doc_sync`, `check_repo_research --all`, `backlog_triggers --abertura SPEC-007`, `build_map --check` — verdes na v1.2. Suíte completa de testes NÃO rodada nesta sessão (só documentos).

## 5. Próximo passo único
(a) **Andraus formaliza a divisão (Opção C)**: o Orquestrador propõe uma ata (DHR) de reabertura/divisão — número e nome da Spec nova (recuperação + pacote de evidência + fidelidade), Dossiê de abertura próprio (RULE-ECC-01/02, atomic-spec §15), erratum de re-apontamento (`research.md` §8.1: SPEC-006 e referências), edição de ROADMAP/CATALOGO só por ordem expressa dele. (b) Depois: Plan enxuto da SPEC-007 (formação + selo + atos + envio externo) reaproveitando o v1.2 como base, tratando R3-M1..M5 nas partes que ficarem (M1 pré-condições por cenário; M2 `material_hash`/`record_hash`; M3 quadro de pré-requisitos mínimos P-1/P-3/P-10/P-4a/P-4b; M4 `knowledge_kind` no hash; M5 envelope da CIM por `content_ref`), e a parte de consulta migra para o Plan da Spec nova. (c) Revisor rodada por delta com versões commitadas. (d) Piloto de esforço depois do Plan; livro (Q7c) segue adiado. **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-SPEC007-001`, `DHR-BENCH-INTEL-001`, `DHR-H001-001`, `DHR-SPEC006-004`, `DHR-ROTEAMENTO-003`, `DHR-COESAO-005`, `DHR-PCC-003`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
Dar Bash ao Revisor; refazer a SPEC-006; usar motores/agentes/skills do Inteligencia-SOT (Benchmark apenas); copiar texto/código dele; incluir o livro como fonte; tratar o Plan v1.2 como pronto (3× NÃO CONFORME); editar ROADMAP/CATALOGO para a divisão sem ordem expressa e ata.

## 8. Não tocar
`canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md`, `CONFLICT-MAP`, selo `GATE-MANIFEST.sha256` (só por Andraus).

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (74b1de3) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `gate_manifest.py --check`; `check_refs`/`check_doc_sync`/`check_handoff`/`check_rpsa`/`check_coesao`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/017/035 vinculados, sem promoção)
- [ ] PRs abertos; se o ramo `ccr-3235944c-duo3sl` já foi mesclado, tratar follow-up como mudança nova
- [ ] ROADMAP: SPEC-007 "ABERTURA HOMOLOGADA" (divisão ainda não registrada); "Decisões abertas ativas" sem H-001
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
**Só de Andraus:** ata/ordem expressa para formalizar a divisão (número e nome da Spec nova) · perguntas P-1..P-11 do Plan (emissores, tipo de nó, direitos de uso, envio externo, quem aprova atos, derivação, emenda à SPEC-020 etc.) · livro (Q7c) · demais decisões abertas (G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001) · destino do Auditor Externo (PAUSADO), D-PCC-3/4/5.

## 11. Ponteiros
`specs/features/SPEC-007/` (ABERTURA, research, plan v1.2, checks) · `governance/propostas/SPEC-007/` (briefing-anexo e pareceres R1–R3) · `governance/DHR-SPEC007-001_*` · `governance/DHR-BENCH-INTEL-001_*` · `ROADMAP.md` · `AGENTS.md` §11 · `docs/handoffs/HO-2026-10-19-69.md` · `docs/mapa/MAPA-PROJETO.md`
