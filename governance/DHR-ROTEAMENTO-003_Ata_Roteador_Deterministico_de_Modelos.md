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

## 7. Emenda 1 (2026-10-18) — modelo por classe de tarefa, fail-closed `[FATO]`
Ordem expressa de Andraus (chat, 2026-10-18): executar a Fase 1 do plano `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md`, autorizando os arquivos protegidos (esta emenda, `scripts/roteador_modelos.py` + testes, detector de ramos, `governance/MECANISMOS.json`, regravação do selo) e **vedando** mexer em agentes (`.claude/agents/*`), `AGENTS.md` e H-001. Esta emenda **substitui o §2 apenas na regra R-AC**; R-GATE, R-N4 e R-ALLOW seguem como estão. Nada do §2 é apagado (INV-07).
- **Classes (tabela estática):** `M` Orquestrador (sem agente) · `S1`/`S2` Revisor SOT → `sonnet` · `S3` Revisor SOT → `opus` (revisão integral de Spec CRITICAL) · `O` Especificador SOT → `opus`.
- **R-AC1:** `effort` por invocação segue **negado** (coluna reservada e desligada até um piloto de esforço, à parte; motivo: DHR-AUDITOR-EXTERNO-014).
- **R-AC2:** `model` por invocação a `Especificador SOT`/`Revisor SOT` só passa se o prompt traz uma linha `CLASSE-TAREFA: <classe>` única e válida, a classe é do agente e o `model` é **igual** ao da tabela. Sem classe, ambígua, incompatível ou modelo diferente ⇒ **nega**; sem `model`, vale o frontmatter. Falha interna com override ⇒ **nega** (fail-closed; antes era fail-open).
- **R-AC3:** `CLASSE-TAREFA: M` enviada a agente ⇒ nega.
- **R-AC4 (classe derivada, não só declarada):** o hook recalcula a classe a partir de fatos do repositório e nega se divergir da declarada ou se não for derivável. Entradas em linha própria do prompt: `ALVO: <plan.md>`, `BASE: <ref|arquivo>` + `PARECER: <arquivo>` (delta), `FICHA: <json>`. **Especificador** (abertura de Spec, Plan, errata, dossiê) ⇒ `O`; com ficha toda mecânica ⇒ `M` (negado). **Revisor**: ficha só de `conferencia` ⇒ `S1`; delta aplicável (base + parecer anterior, ≤ metade dos blocos alterados, Complexidade igual — `revisor.md` §3-bis.6) ⇒ `S2`; revisão integral ⇒ `S3` se Complexidade CRITICAL, senão `S2`. Assim o Orquestrador não consegue rebaixar o Revisor (declarar S2 numa Spec CRITICAL integral é negado) nem gastar Opus à toa.
- **Classe M (rotina do Orquestrador, em código):** `python scripts/roteador_modelos.py classificar <ficha.json>` agrupa os achados por classe (M exige arquivo:linha, texto antigo→novo, condição verificável, sem criar regra/campo/mecanismo/ID normativo novo; teto de 10 linhas e 2 arquivos por lote, o excedente escala a `O`); `conferir <ficha.json>` confere que o diff mostra **só** as linhas listadas e que o texto novo está nelas — qualquer divergência ⇒ **escala** (o Orquestrador não improvisa). **Regra de congelamento:** correção M/S não cria mecanismo; se precisar, vira lote `O` e vai a Andraus.
- **Detector de ramos órfãos:** `scripts/check_branches.py` + hook `SessionStart` (`scripts/branches-hook.js`), informativo (BR-01 ramo à frente da main e não citado no HANDOFF; BR-02 ramo contido na main). Não apaga ramo.
- **Limites honestos:** a classe é derivada de fatos (R-AC4), mas os próprios fatos são apontados pelo Orquestrador (qual `ALVO`/`BASE`/`FICHA` informa) e a derivação não julga o mérito — por isso o Revisor segue independente e a classe M é auditada no delta da rodada seguinte; a independência do Revisor se mantém (nunca revisa o que ele próprio corrigiu; a classe M é auditada no delta da rodada seguinte; ENF-03/ENF-07); o Orquestrador **não** altera semântica de Spec — só aplica a ficha do Revisor.
- **Não muda:** texto dos agentes, `AGENTS.md`, método, regra, decisão aberta (RPSA `nao` preservado). **Permanecem ABERTAS (CONS-01):** o mesmo conjunto do §5, incluindo H-001. Selo regravado nesta emenda (autorizado). Testes: `tests/test_roteador_modelos.py`, `tests/test_check_branches.py` (CI).

## 8. Emenda 2 (2026-10-18) — `gate_extra.py` entra no selo `[FATO]`
Decisão de Andraus (chat, 2026-10-18, AskUserQuestion): **incluir o detector `scripts/gate_extra.py` no selo** (`GATE-MANIFEST.sha256`, lista `ARQUIVOS` de `scripts/gate_manifest.py`) e dar-lhe dono em `.github/CODEOWNERS` — são os detectores D que julgam o trabalho do Especificador (DHR-AUDITOR-EXTERNO-015). O selo foi regravado (18 arquivos) no mesmo PR que ajusta o detector para subtrair as decisões FECHADAS do ROADMAP (autorizado por Andraus no mesmo dia). `spec_delta.py` **não** entrou nesse PR; entrou depois, por decisão de Andraus no chat (2026-10-18, AskUserQuestion "Incluir no selo"), no PR de manutenção seguinte (selo de 19 arquivos; CODEOWNERS). *[Texto anterior preservado — INV-07: "`spec_delta.py` não entra no selo (não foi decidido)."]* Nenhuma decisão aberta fechada; RPSA `nao` preservado.

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
