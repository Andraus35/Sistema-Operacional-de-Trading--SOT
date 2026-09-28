# EUA-E22 — Manutenção obrigatória do Mapa do Projeto (BL-019) por todos os agentes (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **EUA-E22** — *sugestão*: EUA-E20 e EUA-E21 estão reservadas (FASE RISK; normatização de pesquisa web). **Atribuição final = Controlador.** |
| Versão | v1 |
| Natureza | Emenda **operacional / de tooling** aos agentes e ao caminho-quente (`AGENTS.md`). **Não altera invariante, hierarquia, decisão aberta nem baseline canônico.** Compatibilidade: **Minor** (aditiva; nenhum objeto removido — INV-07). |
| Status epistemológico | **HOMOLOGADA — vigência imediata** (DHR-EUA-E22, Andraus, 2026-09-26; Q1–Q4 = Sim; parecer do Revisor CONFORME). *[texto original abaixo preservado — INV-07]* Estado original: PROPOSTA — aguardava parecer do Revisor e homologação de Andraus. Regulariza retroativamente edições **já aplicadas em 2026-09-26** por diretiva direta de Andraus (§0). `[FATO]` para o que está implementado e testado; `[PROPOSTA]` para a vigência normativa. |
| Autoria | Especificador (Claude Code), 2026-09-26 |
| Alvo | `AGENTS.md` (§2, §5, §8) · `.claude/agents/especificador.md` (§7 Autopré-check) · `.claude/agents/revisor.md` (nota antes do Passo 5) · `.claude/settings.json` (hooks) · `.clinerules/sot-map.md` · `governance/CATALOGO-OFICIAL.md` (linha de locator) · `.github/workflows/ci.yml` e `.pre-commit-config.yaml` |
| Fundamento | BL-019 (RMR-001, ATIVADO por Andraus em 2026-09-26) · BL-006 (Absorvido) · INV-09 (o mapa não é baseline) · INV-07 (nada deletado; saída regenerável) · CONS-01 · RULE-MET-01 (não-fabricação) |

---

## 0. Origem e regularização `[FATO]`

Em 2026-09-26, Andraus (Decisor Final) ativou o BL-019 e determinou, em conversa: *"todos os agentes devem atualizar o mapa quando fizerem alterações — garanta isso"*. A implementação foi aplicada **antes** desta formalização. Esta emenda a **regulariza**: descreve o que foi feito, submete a parecer e, se homologada, dá lastro de DHR às edições nos arquivos de agente (e permite atualizar o carimbo `sincronizado-até` — RPSA/EUA-E16 — com uma DHR real, em vez de deixar divergência editorial registrada no RCH-001, Ciclo #3).

## 1. Regra proposta

> **R-MAPA.** Todo agente que criar, alterar, mover ou remover documento `.md` no escopo do mapa mantém `docs/mapa/` atualizado. O mapa é **saída gerada e NÃO-normativa** (INV-09): nunca é editado à mão, não substitui o `CATALOGO-OFICIAL` (locator autoritativo) e, em conflito, vale o documento de origem. A garantia **não depende da memória do agente**: é aplicada por hooks e verificada por CI.

Camadas de garantia (`[FATO]` — implementadas e testadas):

| # | Camada | Cobre | Bloqueia agente? |
|---|---|---|---|
| 1 | `PostToolUse` → `map-sync.js post-edit` | Write/Edit/MultiEdit em `.md` do escopo (inclui subagentes) | Não — regenera |
| 2 | `Stop` / `SubagentStop` / `SessionStart` → `map-sync.js` | Edições via Bash, rename, delete; hooks desativados; outra ferramenta; fora do repositório | Não — autocorrige |
| 3 | Falha de geração (ex.: Python ausente) | — | Não — grava `docs/mapa/.stale`; `build_map.py --check` falha até regenerar (falha **nunca silenciosa**) |
| 4 | CI e pre-commit → `build_map.py --check` | Backstop final | **Sim** (CI/commit) |
| 5 | Regra escrita | `AGENTS.md` §5/§8; Autopré-check do Especificador; `.clinerules/sot-map.md` (Cline não executa hooks) | Não |

O **Revisor** (somente leitura, ENF-03) **não regenera**: apenas verifica se a entrega declara o mapa atualizado; ausência = observação **Menor**, não altera o veredicto.

## 2. Mudanças nos arquivos `[FATO]`

| Arquivo | Alteração (aditiva) |
|---|---|
| `AGENTS.md` | Parágrafo "Mapa do projeto" em §5; comandos em §8; `docs/mapa/` no mapa do repositório (§2) |
| `especificador.md` | 1 item no Autopré-check (§7): `build_map.py --check` = "Mapa em dia" |
| `revisor.md` | Nota de observação de integridade antes do Passo 5; correção de citação sem lastro no cabeçalho/Passo 7 (registrada em RCH-001 Ciclo #3, K-REF-01) |
| `.claude/settings.json` | `MultiEdit` nos matchers; hooks `PostToolUse`(+map-sync), `Stop`, `SubagentStop`, `SessionStart` |
| `.clinerules/sot-map.md` | Regra equivalente para Cline (com frontmatter) |
| `CATALOGO-OFICIAL.md` | Linha de locator "Mapa do projeto (gerado)" |
| `ci.yml` / `.pre-commit-config.yaml` | `build_map.py --check` bloqueante com mensagem de correção |

## 3. O que NÃO muda `[FONTE]`

- Hierarquia Elliott→Fibonacci→Fractal→SMC→ICT, R:R, convicção, Conviction Vector, custo × Conviction, Signal Package: **intocados**.
- Decisões abertas (J-001, G-001, H-001, I-001, K-001, C-001, M-001, N-001): **nenhuma fechada** (CONS-01).
- Roteamento de modelo/esforço (EUA-E19), leitura proporcional, gates M-02 e de `ATIVADO`: **intocados**.
- ENF-03: o Revisor continua sem Write/Edit.

## 4. Non-goals

- Não torna o mapa fonte de verdade nem fonte de leitura obrigatória dos agentes.
- Não substitui o CATALOGO, o `check_refs.py` nem o `backlog_triggers.py`.
- Não exige que agentes rodem o gerador manualmente quando os hooks funcionam.

## 5. Riscos residuais (RULE-MET-01 — honestidade)

1. **Hooks não são invocados fora do Claude Code.** Mitigação: `.clinerules/sot-map.md` + CI/pre-commit. Um agente que edite fora do repositório e faça commit sem regenerar é barrado pelo CI, não pelo hook.
2. **Python ausente** impede a regeneração local; mitigado pelo marcador `.stale` (visível) e pelo `--check` bloqueante. Não elimina a necessidade de Python em CI/dev.
3. **Custo por edição** (~2–5 s por Write/Edit em `.md`): aceito; a geração é atômica (arquivo temporário + replace) contra edições concorrentes.
4. **CI bloqueante** é exceção deliberada ao padrão "informativo primeiro" dos demais verificadores (`check_refs`, `backlog_triggers`), por exigência da garantia pedida. Reversível em uma linha.
5. **A garantia é sobre a atualização do mapa, não sobre a correção dele:** o mapa reflete referências textuais; pode conter falsos "sem referência de entrada" (só `.md` é varrido).

## 6. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Homologar retroativamente a regra R-MAPA e as edições dos arquivos de agente (§2)? | Sim |
| Q2 | Ao homologar, atualizar `sincronizado-até` de `especificador.md` e `revisor.md` para a DHR desta emenda (RPSA) e encerrar a divergência editorial do RCH-001? | Sim |
| Q3 | Manter `build_map.py --check` **bloqueante** no CI/pre-commit? | Sim |
| Q4 | Confirmar o código **EUA-E22** (ou outro, a critério do Controlador)? | Sim |

## 7. Fluxo de autoridade (GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (2026-09-26) ................. ✅
Etapa 2 — Implementação + testes (Especificador) ............ ✅ (47 testes Python · 10 hooks · 18 map-sync)
Etapa 3 — Formalização (esta proposta) ...................... ✅ v1
Etapa 4 — Parecer do Revisor ................................ ⏳
Etapa 5 — Consenso de Andraus (Q1–Q4) ....................... ⏳
Etapa 6 — Registro Oficial (Controlador): DHR + `sincronizado-até` + CATALOGO + RMR-001 (passo 11-bis) ⏳
```

## 8. Evidências

- `scripts/map-sync.js` · `scripts/build_map.py` · `scripts/hook-io.js` · `tests/test-map-sync.js` · `tests/test_build_map.py`.
- Prova ao vivo (2026-09-26): edição de `AGENTS.md` → `docs/mapa/mapa-projeto.json` regravado automaticamente ~10 s depois, sem intervenção.
- `governance/RCH-001_Registro_Ciclos_Hygiene.md` — Ciclo #3 e adendos (BL-006/BL-019/manutenção do mapa).

---

## 9. Notas de homologação (Controlador, 2026-09-26)

- §7 (Etapa 2): a contagem de testes de hook correta é **11** (a v1 dizia 10) — 47 Python · 11 hooks · 18 map-sync, verificados por execução (ACH-01 do parecer).
- Etapas 4–6 do §7 cumpridas: parecer CONFORME; consenso de Andraus; registro em `governance/DHR-EUA-E22_Ata_Homologacao_Manutencao_Mapa_Projeto.md`.
- ACH-02: `scripts/map-sync.js` já exclui `docs/mapa/` (não há re-disparo); OBS-01 (`AGENTS.md` §7, L-001) diferida ao próximo ciclo de Hygiene.
