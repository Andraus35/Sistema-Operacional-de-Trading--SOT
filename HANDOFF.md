---
handoff_id: HO-2026-10-19-66
previous: HO-2026-10-19-65
data: 2026-10-19
branch: claude/amazing-fermat-dnbjtz
base_commit: 73e5cad
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATAS v1.11/v1.12 HOMOLOGADAS (H-001 FECHADA, DHR-H001-001); SPEC-007 = ABERTURA HOMOLOGADA (DHR-SPEC007-001, 2026-10-19; uma Spec CRITICAL; NÃO é baseline); Plan da SPEC-007 pendente, só por ordem de Andraus
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Frente atual (Andraus, chat 2026-10-18/19)
- **Concluído e mesclado:** Fase 0 (medição hash/carimbo), roteador de modelos por classe (PR #122; `DHR-ROTEAMENTO-003` §7 e §8), H-001 FECHADA + errata v1.12 (PR #123), detector `gate_extra` + selo (PR #124), `spec_delta` no selo + registro de mecanismos verificado ao vivo (PR #125). Uso do roteador: `CLASSE-TAREFA: M|S1|S2|S3|O` no prompt do agente + `ALVO:`/`BASE:`/`PARECER:`/`FICHA:`; o hook DERIVA a classe e nega divergência (Especificador = O·opus; Revisor delta = S2·sonnet; integral CRITICAL = S3·opus; ficha mecânica = M, o Orquestrador executa).
- **Este PR (abertura da SPEC-007):** Dossiê (`specs/features/SPEC-007/ABERTURA.md`, `research.md`, `sources/`), 3 rodadas do Revisor (NÃO CONFORME → CONFORME condicional → CONFORME condicional, "pode seguir a Andraus"), ata `DHR-BENCH-INTEL-001` (Inteligencia-SOT = **Benchmark**: motores/agentes/skills NÃO entram; entregas objeto do SOT Harness analisadas para uso/integração; licença/cópia literal e direito sobre o livro = decisão de Andraus; D7 `AGENTS.md` §7 RULE-REG-001 FECHADA; D8 BL-011/COL-EXP-05 re-apontado à SPEC-007, segue ATIVADO) e ata `DHR-SPEC007-001` (abertura homologada com as respostas Q1–Q8; **Q7(c) o livro: ADIADA**). Edições: ROADMAP, CATALOGO, CONFLICT-MAP (COL-EXP-05), RMR-001 (nota BL-011).
- **Resposta dada a Andraus:** ainda não dá para adicionar conhecimento por RAG — fase de especificação; ordem: abertura homologada → Plan da SPEC-007 → Revisor → homologação → só então BUILD (sem data no ROADMAP). Nada entra no caderno permanente sem carimbo.

## 2. Estado (fatos conferidos em 2026-10-19)
- `main` = `73e5cad` (PRs #122–#126, inclusive a abertura da SPEC-007). Clone somente-leitura do Benchmark em `/home/user/andraus35/inteligencia-sot` (commit `0abd22e`, **DADO**, nada executado; pode não existir em sessão nova — `add_repo` read, repo público).
- Verificadores sem ERRO (`check_refs` 0 ERRO; coesão 0 WARN). `BL-010`, `BL-017`, `BL-035` aparecem como "disparados sem registro" (SPEC-007 em redação): vinculados por regra, **sem promoção** (só Andraus); a Disposição de cada um vai no Plan (`[STRUCT-13]`).
- **Notas obrigatórias para o Plan da SPEC-007 (7 Menores R3-01..R3-07, parecer R3):** alinhar a nota da Q-8 ("sim" decide parte de `SPEC-006 plan.md:482`); separar "já normativo" × "em aberto" no carimbo; precisão do exemplo de citações; "SPEC-018" em linguagem de trader; colchetes INV-07 completos; `[PROPOSTA]` na entrega sobre COL-EXP-05; anti-injeção = "instrução não vira efeito". Também: RULE-CKG-004 (validade nunca automática/cascata) como obrigação/caso D8.

## 3. Lições
Rodar a suíte COMPLETA antes de empurrar; não commitar enquanto o Especificador edita (mapa/gate); arquivar o handoff anterior como **cópia exata** (HO-04); citações do Benchmark sempre `inteligencia-sot@0abd22e:caminho:linha` (senão `check_refs` acusa); decisões fechadas entram no ROADMAP a partir do 2º segmento `·` da linha "Decisões FECHADAS"; guarda pós-revisor: citações do clone não existem no SOT (registrar adendo); o Especificador pode parar por limite de uso — retomar por `SendMessage`.

## 4. Verificado
Suíte completa de testes + `npm test` + hooks, `check_doc_sync`, `check_refs`, `check_coesao`, `check_rpsa`, `check_handoff`, `check_invariants`, `check_repo_research --all`, selo (19 arquivos), mapa — verdes na data.

## 5. Próximo passo único
(a) mesclar o PR de vigência do registro (DHR-COESAO-005) com CI verde; (b) **Plan da SPEC-007 só por ordem de Andraus — Andraus pediu decidir antes as outras pendências e iniciar o Plan depois (próxima sessão)** (Especificador·opus, `CLASSE-TAREFA: O`; incorporar R3-01..07, Disposição de BL-010/017/035, COL-EXP-05, caso D8 da RULE-CKG-004) → Revisor integral S3 → homologação; (c) **registro de mecanismos: VIGENTE desde 2026-10-19 (`DHR-COESAO-005`)** — criar/mover/aposentar mecanismo exige atualizar `MECANISMOS.json` no mesmo PR (COE-14 virou ERRO no CI); (d) livro (Q7c): decisão adiada de Andraus; (e) **backlog: Andraus decidiu NÃO promover BL-010/017/035** (o Plan declara a Disposição de cada um); (f) **piloto de esforço (`effort`): depois do Plan** (mais barato com revisões reais; `effort` segue desligado). **Seguem abertas:** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001, produtor/gatilho de promoção.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
`DHR-H001-001`, `DHR-SPEC006-004`, `DHR-ROTEAMENTO-003` (§7, §8), `DHR-BENCH-INTEL-001`, `DHR-SPEC007-001`, `DHR-COESAO-005`. Decisões abertas/fechadas: ler o `ROADMAP.md`.

## 7. Becos sem saída
Dar Bash ao Revisor (DHR-AUDITOR-EXTERNO-009 §2); refazer a SPEC-006; 4 agentes por modelo; reescrever Specs homologadas antigas que citam H-001 aberta; usar motores/agentes/skills do Inteligencia-SOT (Benchmark apenas); copiar texto/código dele sem decisão de Andraus sobre licença.

## 8. Não tocar
`canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md`, `CONFLICT-MAP`, selo `GATE-MANIFEST.sha256` (só por Andraus).

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (73e5cad) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `gate_manifest.py --check`; `check_refs`/`check_doc_sync`/`check_handoff`/`check_branches`/`check_rpsa`/`check_coesao`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/017/035 vinculados, sem promoção)
- [ ] PRs abertos (esperado: o da abertura da SPEC-007 até mesclar)
- [ ] ROADMAP: SPEC-007 "ABERTURA HOMOLOGADA"; "Decisões abertas ativas" sem H-001
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
Plan da SPEC-007 (ordem) · livro (Q7c) · demais decisões abertas · destino do Auditor Externo (PAUSADO), schemas sem `additionalProperties:false`, piloto de esforço, D-PCC-3/4/5 — ver `docs/handoffs/HO-2026-10-17-34.md` §10.

## 11. Ponteiros
`governance/DHR-COESAO-005_Ata_Registro_de_Mecanismos_VIGENTE.md` · `governance/DHR-SPEC007-001_*` · `governance/DHR-BENCH-INTEL-001_*` · `specs/features/SPEC-007/` · `governance/propostas/SPEC-007/` (pareceres e deltas) · `governance/DHR-H001-001_*` · `governance/DHR-ROTEAMENTO-003_*` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
