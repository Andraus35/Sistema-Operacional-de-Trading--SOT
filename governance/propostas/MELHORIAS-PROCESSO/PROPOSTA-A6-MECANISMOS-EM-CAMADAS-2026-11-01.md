# Proposta A6 — Mecanismos em camadas e caducidade (medida antes de cortar)

> **Não normativo. PROPOSTA — NADA APLICADO.** Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A6. Frente escolhida por Andraus; "Avançar" lido como seguir para o A6 (só a proposta). Mexer em `MECANISMOS.json`, `AGENTS.md` ou hooks exige ordem dele (COE-14). Não fecha decisão aberta (CONS-01). 4Es: medir antes de cortar.

## 1. Medição ao vivo (HEAD `742072e`)
| Item | Auditoria | Hoje |
|---|---|---|
| Mecanismos em `MECANISMOS.json` | 53 | **56** (45 ativo · 6 legado · 2 inerte-em-nuvem · 2 pausado · 1 proposta) |
| Tipos | — | 16 detectores · 13 hooks · 7 utilitários · 5 gates · 4 guardas · 3 workflows |
| Hooks em `Stop` / `SubagentStop` | 9 | **9** (5 + 4) a cada fim de turno/subagente |
| Passos `continue-on-error` no CI | 7 | **10** (maioria "informative") |
| Custo medido dos hooks de Stop (cada) | — | `doc-sync-check` **2,44 s**; `map-sync` 0,39 s; `handoff-hook` 0,16 s; `revisor-posguarda` 0,10 s; `andraus-ask-guard` 0,04 s |
| Auditor Externo (PAUSADO) | — | `auditor-externo.yml` 326 linhas, `route_aex.py` + teste, 18 atas |
| Selo `GATE-MANIFEST` | regravado 18× | CODEOWNERS já existe |

## 2. Achado por sub-item
- **A6.1 (3 camadas):** o custo por turno é pequeno (~3,2 s somando os 5 hooks de Stop; o `doc-sync-check` é 76% disso). O ganho de Economicidade é real mas modesto; o risco de Eficácia está em escolher mal a camada (i). **Recomendo medir primeiro** quais detectores já deram achado novo (ver A6.2) antes de rebaixar qualquer um. Mover o `doc-sync-check` do Stop para "uma vez antes de PR" é o corte de maior retorno e menor risco.
- **A6.2 (caducidade por detector):** exige um dado que **não existe hoje**: histórico de "execuções sem achado novo". Sem ele, qualquer N seria chute. Passo seguinte barato: um contador informativo (`--ultima-vez-achou`) em `run_gates.py`, só leitura.
- **A6.3 (Auditor Externo e inertes):** é decisão de Andraus (D-PCC-3 / destino do Auditor Externo): aposentar ou reativar. Dois inertes (`mcp.revisor-gate`, `hook.revisor-guard`) são usados via `GATE-D` em nuvem (DHR-AGENTS-P8-001), então **não são lixo**; o Auditor Externo e `route_aex.py` são o candidato real, e `AGENTS.md` §9 é lido por todo agente.
- **A6.4 (WARN repetido só quando o conjunto muda):** barato e sem perda de visibilidade; afeta `doc-sync-check.js` e `handoff-hook.js` (WARN de `SPEC-007/plan.md:2650` aparece em todo SessionStart).

## 3. Ordem sugerida (cada passo só por ordem de Andraus)
1. **A6.4** (hook mostra só se o conjunto mudou) — pré-testar com patch em cópia isolada.
2. **A6.1 parcial:** tirar o `doc-sync-check` do Stop/SubagentStop e deixá-lo em SessionStart e CI.
3. **A6.3:** Andraus decide o destino do Auditor Externo; eu preparo o arquivamento em `docs/_legacy/` com prova de conservação.
4. **A6.2** só depois de existir o contador.

## 4. Declarado
Tempos medidos uma vez, com entrada `{}` (sem payload real). Não rodei os hooks sob carga nem o CI. Contagens de 10 passos informativos e 56 mecanismos vêm de `grep`/JSON desta sessão; diferem da auditoria (7 e 53) por data.
