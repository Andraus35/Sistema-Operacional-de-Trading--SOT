---
handoff_id: HO-2026-10-17-07
previous: HO-2026-10-17-06
data: 2026-10-17
branch: ccr-7917ac44-2l55cz
base_commit: 1c6754b
spec_autorizada: SPEC-006 (abertura homologada, DHR-SPEC006-001; Plan pendente — só por ordem de Andraus) — ROADMAP prevalece
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual
Reforçar o Revisor SOT (independente, determinístico + adversarial/probabilístico) sem dar Bash a ele. DHR-AUDITOR-EXTERNO-015 (brechas + medição) está na `main` (PR #103). Agora: fundir no Revisor o que era útil dos 2 subagentes antigos e aposentá-los (DHR-AUDITOR-EXTERNO-016).

## 2. Estado
Fase spec-first; BUILD/VERIFY-de-código adiados. Última Spec homologada: SPEC-005; SPEC-006 com abertura homologada e Plan não iniciado. PCC-001 Fases 1 e 2 em vigor na `main` (D-PCC-3/4/5 em aberto).

## 3. Feito nesta sessão
- **DHR-AUDITOR-EXTERNO-016 (ramo; PR a abrir):** `sot-spec-reviewer`/`sot-schema-validator` → `docs/_legacy/agents/`; gate ganha `contrato_schemas` e `lint_specs`; selo regravado; Auditor Externo mantido pausado/opcional (decisão de Andraus). Não portados: `additionalProperties:false`, score em todo output (schemas vigentes não cumprem) e "60% para viés" (sem fonte) — viraram achados na ata.
- PR #103 (DHR-AUDITOR-EXTERNO-015) mesclado na `main` com CI verde.
- **Auditoria do Revisor:** sem Bash/Write/Edit por decisão de Andraus (DHR-AUDITOR-EXTERNO-009 §1, 2026-10-11; reafirmada na DHR-AUDITOR-EXTERNO-014). Executa só `revisor_gate` (MCP, leitura, 12 verificações D + 10 sinais H). Parte adversarial/probabilística = só prompt (Passos 4-ter/5-bis), 1 passada, sem calibração contínua.
- **Brechas fechadas (DHR-AUDITOR-EXTERNO-015, só no ramo):** `tools: Read, Grep, Glob` em `sot-spec-reviewer`/`sot-schema-validator`; selo `scripts/gate_manifest.py` + `governance/GATE-MANIFEST.sha256` (servidor do Revisor recusa rodar se divergir; passo de CI bloqueante); `.github/CODEOWNERS`. Testes novos: `tests/test_gate_manifest.py` + 2 em `test_revisor_gate_mcp.py` (32 OK).
- **Banco de estresse rodado 2×** (`origin/ferramentas-estresse`, nunca mesclar): 2 sorteios × 30 defeitos plantados × 3 rodadas. `score.py` dá ~30/30 mas é inflado (documentos de 99 linhas); medida adotada (arquivo:linha + texto defeituoso junto) = recall por rodada ≈ 83–100%, 0 falsos alarmes. Gabarito/semente/respostas ficaram no scratchpad (não no repo).

## 4. Verificado
- 32 testes (gate, MCP, manifesto) OK; `gate_manifest.py --check` íntegro; `check_rpsa`: DHR-AUDITOR-EXTERNO-015 sem classificação até o registro automático pós-merge (esperado).
- **Achado:** nas 6 rodadas o `revisor_gate` **não carregou** no Revisor invocado em nuvem ("GATE NÃO VERIFICADO"); servidor funciona fora do agente. Causa não diagnosticada.
- Não conferido nesta sessão: CI da `main`, PRs abertos, `check_refs`.

## 5. Próximo passo único
Ler este handoff, executar §9 e, sem outra ordem de Andraus, **não** iniciar o Plan da SPEC-006; perguntar a prioridade (§10).

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
- DHR-AUDITOR-EXTERNO-015 (na `main`) e -016 (fusão/aposentadoria dos subagentes antigos) — decisões de Andraus em chat, 2026-10-17.
- Decisões abertas/fechadas: ler "Decisões abertas ativas" e "Decisões FECHADAS" do `ROADMAP.md`. Nenhuma alterada.

## 7. Becos sem saída
- Dar Bash ao Revisor: rejeitado (DHR-AUDITOR-EXTERNO-009 §2). Não reabrir sem Andraus.
- Pontuar o banco só com `score.py` em documentos curtos: infla; usar arquivo:linha + texto defeituoso junto da citação (transcrição literal pura subestima).

## 8. Não tocar
- `canon/` BASELINED, specs homologadas, `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/revisor.md`/`especificador.md`, `AGENTS.md` (só por Andraus). Não regravar `GATE-MANIFEST.sha256` sem decisão de Andraus.

## 9. Reverificar ao vivo
- [ ] CI da `main` e do ramo
- [ ] `python scripts/gate_manifest.py --check` e `check_refs.py`/`check_doc_sync.py`
- [ ] PRs abertos (#31 Auditor externo, #2 capturas SPEC-003 na última checagem)
- [ ] `python scripts/backlog_triggers.py`
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)
- [ ] `git log -1` == `base_commit` ou posterior; se posterior, ler o diff

## 10. Aguardando Andraus
- Merge da DHR-AUDITOR-EXTERNO-016 (PR aberto; só mesclar com ordem de Andraus). Decidiu antes: **manter só o selo**.
- Decidir: schemas sem `additionalProperties:false` e `fibonacci.output.json` sem score (ata 016 §4).
- Opcional: escrever 3–5 defeitos próprios (parte livre do viés; o novo sorteio automático já foi feito).
- Diagnosticar por que o MCP do Revisor não carrega em nuvem (testar em sessão local).
- Próximos reforços propostos: verificadores D novos (contagens, cobertura, citação §/linha), ferramenta `verifica_citacao`, k=3 passes adversariais em modo cego.
- D-PCC-3/4/5; prioridade: Plan da SPEC-006 · 2 itens de backlog disparados sem registro.

## 11. Ponteiros
`governance/DHR-AUDITOR-EXTERNO-016_Ata_Fusao_dos_Subagentes_Antigos_no_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-015_Ata_Brechas_de_Ferramenta_e_Medicao_do_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-009_*` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
