# DHR-AUDITOR-EXTERNO-016 — Ata — Fusão do que era útil dos subagentes de 1ª geração no Revisor SOT e aposentadoria deles

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17):** sobre os agentes de revisão que sobraram, "Fundir o que for útil no Revisor e depois aposentar"; sobre o Auditor Externo, "Manter pausado e opcional". O merge desta ata por Andraus é a ratificação. **Não altera `revisor.md`**, método, regra nem decisão aberta. |
| Compatibilidade | Aditiva (INV-07): nada é apagado; os dois arquivos vão para `docs/_legacy/agents/`. Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Aposenta dois subagentes auxiliares fora do fluxo e acrescenta dois detectores ao gate do Revisor (script); nao altera o texto do Revisor nem do Especificador, checklist, metodo nem regra. |

## 1. Origem `[FATO]`
Andraus (chat, 2026-10-17): a ideia era fundir o auditor independente e adversarial no Revisor SOT interpelador; por que ainda existem outros agentes de revisão? Levantamento: (1) o **Revisor SOT** é o único no fluxo (DHR-AUDITOR-EXTERNO-014 o tornou adversarial e independente; DHR-009/011 deram-lhe o gate); (2) o **Auditor Externo** está pausado e opcional desde a DHR-AUDITOR-EXTERNO-007; (3) `sot-spec-reviewer` e `sot-schema-validator` (1ª geração) não aparecem em nenhum workflow, script ou teste do fluxo atual.

## 2. O que foi comparado e o que entrou no Revisor `[FATO]`
| Verificação do subagente antigo | Situação | Destino |
|---|---|---|
| Hierarquia, camada inferior não sobrepõe, condições de sinal (score + R:R + convicção + conflito) | já cobertas: Revisor Passo 2/3 e `check_invariants.py` | nada a fundir |
| Seções Missão/Escopo/Antiescopo e notação EARS "Quando…, o agente DEVE" | já existe código: `tests/lint-specs.js` (CI) | **passa a rodar no gate** (`lint_specs`, informativo) |
| Draft-07, `$id` único, `title`/`type`/`required`; `*_score` inteiro 0–3 e `score_total` 0–9; `sinal` com os 4 estados; `approved_hypothesis` anulável no ICT | `validate-schemas.js` cobria só parte | **novo detector `contrato_schemas`** no gate (informativo; 35 testes passam, com caso negativo) |
| `additionalProperties:false` no topo de todo schema | **10 dos 11 schemas vigentes não cumprem** | **não portado** (falso alarme permanente); fica como achado abaixo |
| "Todo output tem campo de score" | `fibonacci.output.json` não tem | **não portado**; achado abaixo |
| Consistência entre saída de um agente e entrada do próximo (pipeline) | exige mapeamento campo a campo, hoje inexistente em código | **não portado**; fica como proposta |
| "Convicção de 60% para emissão de viés (Fase Piloto)" | **sem âncora** em `AGENTS.md`, `CONSTITUTION.md` nem `CEE-001` (busca por "60%") | **não portado**: valor sem fonte, risco de contaminar baseline |

## 3. O que muda `[FATO]`
1. `.claude/agents/sot-spec-reviewer.md` e `sot-schema-validator.md` → `docs/_legacy/agents/` (git mv; histórico preservado).
2. `scripts/revisor_gate.py`: detectores `contrato_schemas` e `lint_specs` (modo completo, informativos, não bloqueantes); selo `GATE-MANIFEST.sha256` regravado (decisão de Andraus no chat).
3. `tests/test_gate_manifest.py` passa a exigir que todo agente de revisão/validação em `.claude/agents` declare `tools` sem Bash/Write/Edit e que os dois antigos não estejam ativos.
**Não muda:** `revisor.md` (texto/frontmatter), o Auditor Externo (continua pausado e opcional; `AUDITOR_EXTERNO_ENABLED` é ato de Andraus), o Passo 4-ter/5-bis.

## 4. Achados para Andraus (não corrigidos aqui) `[FATO]`
- 10 de 11 schemas de agente não declaram `additionalProperties:false`; `fibonacci.output.json` não declara campo de score. Ou a regra antiga estava errada para o desenho vigente ou os schemas estão frouxos; decidir antes de qualquer correção.
- O valor "60% para viés" estava escrito no subagente antigo sem fonte; ninguém o reconheceu no repositório.
- Continua em aberto o diagnóstico do gate que não carrega no Revisor em nuvem (DHR-AUDITOR-EXTERNO-015).

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 6. Registro
- [x] Esta ata · [x] arquivamento · [x] gate + testes · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
