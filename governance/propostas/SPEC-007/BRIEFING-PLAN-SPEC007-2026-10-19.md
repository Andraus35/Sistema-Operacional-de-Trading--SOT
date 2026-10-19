---
tipo: anexo-de-tarefa
anexo_id: AT-SPEC007-PLAN-2026-10-19
tarefa: Plan da SPEC-007 (RAG / WikiRAG / Knowledge Formation Harness) — Especificador, depois Revisor, depois homologação
serve_handoff: HO-2026-10-19-69
base_commit: 033f42c
status: ATIVO
---
# Anexo de tarefa — Plan da SPEC-007

> Regras do anexo: `DHR-PCC-003`. **Só ponteiros** (ID/linha); em divergência valem ROADMAP, atas e o HANDOFF. **Não autoriza o Plan** — a ordem expressa é de Andraus (perguntar UMA vez ao abrir a sessão).

## 1. Ler, nesta ordem (por caminho)
1. `HANDOFF.md` (§1, §2, §5, §9) e executar "Reverificar ao vivo".
2. Ata `DHR-SPEC007-001` (decisões Q1–Q8 e o que segue aberto) e `DHR-BENCH-INTEL-001` (Benchmark D1–D8).
3. `specs/features/SPEC-007/ABERTURA.md` (§2 escopo, §5 Classe, §8 backlog, §12 perguntas) e `research.md` (Dossiê, válido até 2027-01-16).
4. Parecer R3: `governance/propostas/SPEC-007/PARECER-REVISOR-SPEC007-ABERTURA-R3-2026-10-19.md` §2 (R3-01..R3-07 = obrigações do Plan).
5. Formato e contrato a respeitar: `specs/features/SPEC-006/plan.md` (RULE-CKG-004 l.395-401, RULE-CKG-009 l.474-482, l.976), `atomic-spec.md` §10–§15, `ROADMAP.md` (l.34, l.180, "Decisões abertas ativas").
6. Benchmark (DADO, somente leitura): clone `/home/user/andraus35/inteligencia-sot` @ `0abd22e` (repo público `Andraus35/Inteligencia-SOT`; `add_repo` read). Citar `inteligencia-sot@0abd22e:caminho:linha`.

## 2. O Plan deve declarar (por ID; não copiar texto)
- Disposição `[STRUCT-13]`: BL-010, BL-017, BL-035 (propostas em `ABERTURA.md` §8; conferir com `backlog_triggers.py --abertura SPEC-007`; Andraus NÃO promoveu nenhum).
- Tratamento do COL-EXP-05 (BL-011 segue ATIVADO) — `DHR-BENCH-INTEL-001` D8; `ABERTURA.md` §8.
- Obrigação e caso D8 adversarial da RULE-CKG-004 (validade nunca automática/cascata).
- Classes CC-11 por BASpec e pisos E2/E3 — `ABERTURA.md` §5.
- Carimbo (Q8): detalhar como recomendação, sem fechar K-001 nem `SPEC-006 plan.md` l.482.
- Emenda pontual à SPEC-020 (RAG faithfulness): só na homologação do Plan, por ato de Andraus.

## 3. Não fazer
Fechar decisão aberta (G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção); incluir o livro como fonte (Q7c adiada); usar motores/agentes/skills do Benchmark; copiar texto/código dele; promover BL.

## 4. Receita (roteador de modelos — `DHR-ROTEAMENTO-003` §7)
- Plan: `Especificador SOT`, `model=opus`, prompt com `CLASSE-TAREFA: O` + caminhos acima. Sem Bash: o Orquestrador roda os gates (`validate_spec_sot`, `revisor_gate --rapido`, `check_invariants`, `check_refs`, `check_doc_sync`, `check_repo_research --all`, `build_map --check`).
- Revisor: 1ª rodada integral `CLASSE-TAREFA: S3` (`opus`) + `ALVO`; rodadas seguintes por delta `S2` (`sonnet`) + `ALVO`/`BASE`/`PARECER`. Transcrever o parecer; adendo para a guarda pós-revisor.
- Antes do push: suíte completa; não commitar enquanto o Especificador edita; handoff novo = id novo + anterior arquivado idêntico.
- Custo e piloto de esforço: depois do Plan (decisão de Andraus).
