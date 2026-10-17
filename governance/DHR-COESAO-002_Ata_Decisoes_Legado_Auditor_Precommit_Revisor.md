# DHR-COESAO-002 — Ata — Decisões de Andraus sobre Auditor Externo, pre-commit, camadas do Revisor em nuvem e legado

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisões de Andraus registradas (chat, 2026-10-17, quatro respostas a AskUserQuestion: "Pausado, registrar no AGENTS §9", "Retirar do pre-commit", "Manter e documentar, sem tocar no revisor.md", "Arquivar em docs/_legacy/")**. O merge desta ata por Andraus é a ratificação. Não fecha nem abre decisão aberta (CONS-01). |
| Compatibilidade | Aditiva/reversível (INV-07): nada é apagado; arquivos movidos para `docs/_legacy/`. Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Nenhum arquivo de .claude/agents e alterado; o AGENTS.md ganha so a declaracao de estado PAUSADO do Auditor Externo, ja decidido na DHR-AUDITOR-EXTERNO-007, sem tocar checklist, metodo nem regra. |

## 1. Decisões `[FATO]`
1. **Auditor Externo = PAUSADO.** `AGENTS.md` §9 passa a declarar o estado (PAUSADO desde 2026-10-11, DHR-AUDITOR-EXTERNO-007; reativação só por Andraus). O Status textual da ata -007 deixa de dizer "PROPOSTA" (texto original preservado entre parênteses). Cura o par D1/COE-10 da auditoria de coesão.
2. **`gate-check` retirado do pre-commit.** O `.pre-commit-config.yaml` perdeu a entrada `gate-check` (no-op: lê o payload de hook do Claude Code no stdin). O hook de sessão `PreToolUse` em `.claude/settings.json` permanece; schemas, specs e mapa continuam validados no pre-commit e no CI. Cura O7/COE-03.
3. **Camadas do Revisor inertes em nuvem (MCP `revisor_gate` e `SubagentStop`):** **mantidas e documentadas, sem tocar `revisor.md`**. A guarda pós-Revisor no Orquestrador (DHR-AUDITOR-EXTERNO-018) é a camada que funciona em nuvem; as outras valem em sessão local. O estado `inerte-em-nuvem` está no registro de mecanismos.
4. **Legado arquivado, não apagado:** as 3 skills soltas foram movidas para `docs/_legacy/skills/` (com `LEIA-ME.md`). **Desvio consciente do pedido:** `.eslintrc.json` e `.prettierrc` **não** foram movidos — existem de propósito como sensores SNS-02/SNS-04 do `harness-score` (`docs/_legacy/HARNESS-REPORT.md`, "Para atingir L3"); arquivá-los baixaria o score de maturidade citado no `AGENTS.md` §8. Ficam registrados como `legado` com essa nota. Andraus pode mandar arquivá-los mesmo assim.

## 2. Efeitos
`AGENTS.md` §9 (cabeçalho + aviso de estado); `governance/DHR-AUDITOR-EXTERNO-007_*.md` (linha Status); `.pre-commit-config.yaml`; `docs/_legacy/skills/` (3 skills + LEIA-ME); `governance/MECANISMOS.json` (estados e atas); HANDOFF. **Não tocados:** `.claude/agents/*`, selo `GATE-MANIFEST.sha256`, `CODEOWNERS`, `canon/`, `ROADMAP.md`, `atomic-spec.md`.

## 3. Permanecem ABERTAS (CONS-01)
Nenhuma decisão aberta fechada ou aberta por este ato; o estado é o do `ROADMAP.md`. Seguem sem decisão de Andraus: tabelas do `AGENTS.md` §3/§8 (ferramentas dos agentes e lista de scripts); regras `RULE-COESAO-01..03`; assinar o registro de mecanismos como VIGENTE; proteção da `main` (Settings).

## 4. Registro
- [x] Esta ata · [x] `AGENTS.md` §9 · [x] registro de mecanismos · [ ] merge de Andraus (ratificação) · [ ] `CATALOGO-OFICIAL.md` (governance normativo — só após decisão de Andraus)

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
