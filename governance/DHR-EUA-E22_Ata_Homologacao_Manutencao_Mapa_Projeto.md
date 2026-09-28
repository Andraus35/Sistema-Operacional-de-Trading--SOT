# DHR-EUA-E22 — Ata de Homologação: Manutenção obrigatória do Mapa do Projeto (BL-019) por todos os agentes

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E22** |
| Objeto | Homologação da emenda **EUA-E22 v1** (`governance/EUA-E22_Manutencao_Mapa_Projeto_PROPOSTA.md`) — regra **R-MAPA** + edições já aplicadas nos arquivos de agente e no caminho-quente (regularização retroativa) |
| Natureza | Emenda **operacional / de tooling** (aditiva). Não altera invariante, hierarquia, decisão aberta nem baseline canônico. |
| Compatibilidade | **Minor** (nenhum objeto removido — INV-07) |
| Data | 2026-09-26 |
| Vigência | **Imediata.** |
| Status | **HOMOLOGADA — BASELINE** |

---

## 1. Fluxo de autoridade (GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (2026-09-26) ................ ✅ "todos os agentes devem atualizar o mapa; garanta isso"
Etapa 2 — Implementação + testes (Especificador) ........... ✅ hooks, CI/pre-commit, regra escrita
Etapa 3 — Formalização (EUA-E22 v1) ......................... ✅ Especificador (Claude Code)
Etapa 4 — Parecer do Revisor ................................ ✅ CONFORME (2 Menores + 1 observação, não bloqueantes)
Etapa 5 — Consenso .......................................... ✅ Andraus (Decisor Final), 2026-09-26 — Q1–Q4 = Sim
Etapa 6 — Registro Oficial .................................. ✅ EFETIVADO (Controlador) — esta ata + edições de baseline (§4)
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME + consenso do Usuário + registro pelo Controlador.

## 2. Decisões de Andraus (Q1–Q4)

| # | Questão | Decisão |
|---|---|---|
| **Q1** | Homologar a regra R-MAPA e as edições dos arquivos de agente (regularização retroativa) | **SIM** |
| **Q2** | Atualizar `sincronizado-até` de `especificador.md` e `revisor.md` para esta DHR (RPSA) e encerrar a divergência editorial do RCH-001 | **SIM** |
| **Q3** | Manter `build_map.py --check` **bloqueante** no CI/pre-commit | **SIM** |
| **Q4** | Confirmar o código **EUA-E22** | **SIM** |

*Nota de registro:* a resposta de Andraus foi recebida em chat como uma lista de quatro itens ("Homologar a regra e as edições dos agentes" + três numerados); o mapeamento para Q1–Q4 segue a ordem exata da §6 da EUA-E22.

## 3. Objeto homologado

**Regra R-MAPA:** todo agente que criar, alterar, mover ou remover `.md` no escopo do mapa mantém `docs/mapa/` atualizado. O mapa é **saída gerada, regenerável e NÃO-normativa** (INV-09): nunca editado à mão, não substitui o `CATALOGO-OFICIAL` (locator autoritativo); em conflito vale o documento de origem. A garantia não depende da memória do agente: hooks (`PostToolUse`, `Stop`, `SubagentStop`, `SessionStart`) + marcador `.stale` em falha + `build_map.py --check` bloqueante no CI e no pre-commit + regra escrita (`AGENTS.md`, Autopré-check, `.clinerules/sot-map.md`). O Revisor (somente leitura, ENF-03) apenas observa a declaração — ausência = observação Menor.

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração | Estado |
|---|---|---|
| `.claude/agents/especificador.md` | `sincronizado-até` → **DHR-EUA-E22**; `required_sources` + esta ata; nota R-MAPA no carimbo (RPSA) | ✅ aplicado |
| `.claude/agents/revisor.md` | `sincronizado-até` → **DHR-EUA-E22**; `required_sources` + esta ata; nota R-MAPA no carimbo (RPSA) | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E22 (HOMOLOGADA) na tabela de emendas + linha DHR-EUA-E22 na tabela de atas | ✅ aplicado |
| `governance/EUA-E22_..._PROPOSTA.md` | Status → HOMOLOGADA (referência a esta ata) + notas de homologação (correções editoriais de §7) | ✅ aplicado |
| `governance/RCH-001_Registro_Ciclos_Hygiene.md` | Adendo (aditivo): divergência editorial dos agentes **encerrada** | ✅ aplicado |
| `backlog/RMR-001_Painel_Backlog.md` | Passo 11-bis — gate desta homologação | ✅ aplicado |

Já vigentes desde a implementação (2026-09-26), agora com lastro de DHR: `AGENTS.md` (§2, §5, §8), Autopré-check do `especificador.md`, nota do `revisor.md`, `.claude/settings.json`, `.clinerules/sot-map.md`, `ci.yml`, `.pre-commit-config.yaml`.

## 5. Tratamento do parecer do Revisor

| Achado | Disposição |
|---|---|
| **ACH-01** (Menor) — contagens de testes não auditáveis por leitura | Verificadas por **execução** em 2026-09-26: 47 (Python) · **11** (hooks — a proposta dizia 10; correção editorial) · 18 (map-sync). |
| **ACH-02** (Menor) — hook sem exclusão explícita de `docs/mapa/` | **Esclarecido:** `scripts/map-sync.js` já exclui `docs/mapa/` (regex `EXCLUDED`) e há teste dedicado ("post-edit no próprio mapa é no-op"). Não há laço nem re-disparo. |
| **OBS-01** — `AGENTS.md` §7 ainda lista L-001 como decisão ativa (L-001 FECHADA por DHR-SPEC019-001) | Pré-existente, fora do escopo da EUA-E22. **Diferida ao próximo ciclo de Hygiene** (correção de §7; L-001 não retorna à lista de abertas — CONS-01). |

## 6. Invariantes preservados

- **INV-07 / INV-09:** nada deletado; mapa não-normativo; ata e proposta anteriores intocadas.
- **CONS-01:** nenhuma decisão aberta (J/G/H/I/K/L/C/M/N-001) fechada ou reaberta por esta emenda.
- **ENF-03:** `revisor.md` continua sem Write/Edit.
- **RPSA (EUA-E16):** carimbo `sincronizado-até` agora corresponde à última DHR em escopo dos agentes.
- **RULE-MET-01:** riscos residuais (§5 da EUA-E22) aceitos como decisão consciente — hooks não cobrem agentes fora do Claude Code (mitigação: `.clinerules` + CI); Python ausente (mitigação: `.stale` + `--check`); CI bloqueante é exceção deliberada ao padrão "informativo primeiro".
- **EUA-E19:** roteamento de modelo/esforço e leitura proporcional inalterados.

## 7. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultado `backlog/RMR-001` — esta emenda é o encaminhamento de tooling do **BL-019** (já `ATIVADO`); nenhum item **novo** fica `ATIVADO`. A promoção do BL-019 a `Absorvido` **não foi decidida nesta ata** e permanece com Andraus (RMR-001 §5).
2. **EUA-E20** (FASE RISK) e **EUA-E21** (pesquisa web/RULE-ECC-02) permanecem reservadas; **EUA-E22** é o próximo código disponível e fica confirmado.
3. Próximo trabalho autorizado do caminho crítico **inalterado:** SPEC-020 — núcleo A.

---

*Ata registrada pelo Controlador (Claude Code) a partir da homologação de Andraus (Decisor Final), 2026-09-26, comunicada em chat — a decisão é de Andraus; este registro não a substitui. Parecer do Revisor: CONFORME. Nenhum registro anterior removido — apenas aditado (INV-07/INV-09).*
