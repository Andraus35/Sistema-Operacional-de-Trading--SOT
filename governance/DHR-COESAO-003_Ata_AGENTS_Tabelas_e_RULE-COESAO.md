# DHR-COESAO-003 — Ata — AGENTS.md §3/§8 alinhados à realidade e RULE-COESAO-01..03 registradas

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisões de Andraus registradas (chat, 2026-10-17, AskUserQuestion: "Corrigir §3 e apontar §8 ao registro", "Registrar as 3, cada uma com verificador", "Ainda não: observar uma rodada" para assinar o registro VIGENTE)**. O merge desta ata por Andraus é a ratificação e o registro das RULE-COESAO em `RULES.md` (RULE-HG-02). Não fecha nem abre decisão aberta (CONS-01). |
| Compatibilidade | Minor/aditiva (INV-07): nenhuma regra existente é alterada; só se acrescenta uma família e se corrige descrição. Reversível por `git revert`. |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta a familia RULE-COESAO em RULES.md (escopo dos agentes por definicao); os arquivos dos agentes nao mudam e leem a regra da fonte unica. |

## 1. Decisões `[FATO]`
1. **`AGENTS.md` §3:** a coluna Tools passa a refletir os arquivos dos agentes — Especificador com WebSearch/WebFetch (Dossiê; web é dado), Revisor com a ferramenta `mcp__sot-revisor-gate__revisor_gate` (inerte em nuvem). **§8:** acrescenta `check_coesao.py` e aponta os demais scripts/hooks/guardas ao registro `governance/MECANISMOS.json` como fonte única de *estado*; os comandos de uso diário permanecem. Remove os 2 avisos COE-06.
2. **`RULES.md`:** nova família **RULE-COESAO-01..03**, cada uma com verificador determinístico: 01 → COE-14, 02 → COE-02 (já bloqueante), 03 → COE-10/COE-14.
3. **Registro de mecanismos continua PROPOSTA:** observar uma rodada sem falso positivo antes de Andraus assinar como VIGENTE (quando COE-14 passa a ERRO). O `AGENTS.md` o cita como PROPOSTA.

## 2. Efeitos
`AGENTS.md` (§3, §8); `governance/RULES.md` (+ comentário de acréscimo e seção RULE-COESAO); `scripts/check_coesao.py` (COE-06 só acusa a MCP que a tabela não cita) e teste; `governance/MECANISMOS.json` (nota); HANDOFF. **Não tocados:** `.claude/agents/*`, selo, `CODEOWNERS`, `canon/`, `ROADMAP.md`, `atomic-spec.md`, `CONSTITUTION.md`.

## 3. Permanecem ABERTAS (CONS-01)
Nenhuma decisão aberta fechada ou aberta; o estado é o do `ROADMAP.md`. Sem decisão de Andraus: assinar o registro como VIGENTE; proteção da `main` (Settings); camadas inertes do Revisor em nuvem (mantidas, DHR-COESAO-002).

## 4. Registro
- [x] Esta ata · [x] `AGENTS.md` · [x] `RULES.md` (RULE-COESAO) · [ ] merge de Andraus (ratificação) · [ ] `CATALOGO-OFICIAL.md` (governance normativo — só após decisão de Andraus)

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
