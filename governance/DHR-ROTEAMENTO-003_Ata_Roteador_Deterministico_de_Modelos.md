# DHR-ROTEAMENTO-003 — Ata — Roteador determinístico de modelo por tarefa (hook PreToolUse/Agent)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "Vamos a isso")**. O merge por Andraus é a ratificação. **Não altera `revisor.md`, `especificador.md`, `AGENTS.md`, `canon/`, método, regra nem decisão aberta.** Implementa a MRM R1/R2/R4/R12 da proposta e a D1 da DHR-ROTEAMENTO-001 em código. |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta um hook de codigo que confere model/effort por invocacao do Agent; nao altera o texto do Revisor nem do Especificador, checklist, metodo nem regra. |

## 1. Origem `[FATO]`
Não existia roteamento por código: a regra "Revisor e Especificador nunca por parâmetro de invocação; Haiku nunca como gate" era só disciplina do Orquestrador (DHR-ROTEAMENTO-001 §2). Andraus ordenou construir o roteador determinístico.

## 2. O que muda `[FATO]`
`scripts/roteador_modelos.py` + `scripts/roteador-modelos.js` (hook **PreToolUse**, matcher `Agent`), tabela estática versionada (MRM R1, sem roteador aprendido):
- **R-AC:** `Especificador SOT`/`Revisor SOT` com `model` ou `effort` por invocação ⇒ **nega** (modelo só pelo frontmatter + ata).
- **R-GATE:** gate/revisão/parecer/conformidade em `haiku` ⇒ nega (ENF-03; MRM R4).
- **R-N4:** homologação/decisão/baseline em `haiku` ⇒ nega.
- **R-ALLOW:** `model` fora de `opus|sonnet|haiku|fable|claude-*` ⇒ nega; sem `model` herda o da sessão (permitido).
- Telemetria mínima (R8): uma linha JSON por invocação em `<tmp>/sot-roteador/uso.jsonl` (decisão + motivo; não normativo, não persiste no repositório).
- `tests/test_roteador_modelos.py` (6 testes) no CI.

## 3. Limites honestos `[FATO]`
- **Forma, não mérito:** a classificação da tarefa (gate/soberana) é por palavras-chave em `description`/`prompt`; um prompt que esconda a natureza da tarefa passa. É Detector de regra de forma (ENF-03), não julga se o modelo escolhido é bom.
- Cobre o Agent do Orquestrador; não cobre troca de modelo da própria sessão nem o `effort` fora do Agent.
- Não mede tokens (o `Agent` só os reporta no retorno); a telemetria de tokens segue manual (TELEMETRIA-ONDA0).
- Fail-open: erro no script libera.

## 4. Pendências que exigem Andraus `[FATO]`
- **Hook registrado e selo regravado (17 arquivos)** após autorização de Andraus no chat; confirmado ao vivo: `Agent` com `Revisor SOT` + `model=haiku` foi negado pelo hook.
- Emenda EUA-E24 (D5) segue só após evidência da onda 1.

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 6. Registro
- [x] Esta ata · [x] script + wrapper + testes · [ ] hook registrado no settings · [ ] selo regravado · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
