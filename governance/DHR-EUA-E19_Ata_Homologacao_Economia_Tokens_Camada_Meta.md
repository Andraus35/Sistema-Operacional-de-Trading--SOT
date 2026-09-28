# DHR-EUA-E19 — Ata de Homologação: Economia de Tokens na Camada Meta (Roteamento de Modelo e Proporcionalidade de Leitura)

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E19** |
| Objeto | Homologação da emenda **EUA-E19 v2** (`governance/EUA-E19_Economia_Tokens_Camada_Meta_PROPOSTA.md`) |
| Natureza | Emenda dual aos arquivos de agente — roteamento de modelo por papel (`especificador.md` mantém `claude-opus-4-8`; `revisor.md` passa a `claude-sonnet-4-6`), nota operacional de esforço (médio/alto, não-persistida — limite de plataforma), extensão do dial GES (RULE-PPQ-001) ao escopo de leitura obrigatória, e short-circuit de releitura de atas via `sincronizado-até` (RPSA). |
| Data | 2026-09-21 |
| Vigência | **Imediata.** |

---

## 1. Fluxo de autoridade (GMC-001 Cap.5)

```
Etapa 1 — Auditoria (Claude Code, mesma sessão) ... ✅ achados #1–#5 sobre economia de tokens/cache
Etapa 2 — Roteamento decidido por Andraus .......... ✅ Especificador→Opus/médio; Revisor→Sonnet/alto
Etapa 3 — Formalização (v1) ........................ ✅ Especificador (Claude Code) — EUA-E19 em governance/
Etapa 4 — 1º parecer formal ......................... ✅ Revisor — NÃO CONFORME RECUPERÁVEL (A-01/A-02; A-03 Menor)
Etapa 5 — Formalização (v2) ........................ ✅ Especificador (Claude Code) — trata A-01/A-02/A-03
Etapa 6 — Re-parecer formal ......................... ✅ Revisor — CONFORME (2 observações Menores, não-bloqueantes)
Etapa 7 — Consenso .................................. ✅ Andraus (Decisor Final), 2026-09-21 — "Sim, homologar e aplicar tudo"; Q1–Q6 = Sim
Etapa 8 — Registro Oficial .......................... ✅ EFETIVADO (Controlador) — este DHR + edições de baseline
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME + consenso do Usuário + registro pelo Controlador.

---

## 2. Decisões de Andraus (Q1–Q6)

| # | Questão | Decisão |
|---|---|---|
| **Q1** | Alterar `model:` do `revisor.md` de `claude-opus-4-8` para `claude-sonnet-4-6` | **SIM** |
| **Q2** | Manter `model:` do `especificador.md` em `claude-opus-4-8` | **SIM** |
| **Q3** | Registrar "esforço médio/alto" como política operacional no corpo dos agentes (não config persistente — limite de plataforma) | **SIM** |
| **Q4** | Aprovar a extensão do dial GES ao escopo de leitura (núcleo sempre obrigatório; lista completa HIGH/CRITICAL; reduzida LOW/MEDIUM) | **SIM** |
| **Q5** | Aprovar o short-circuit de releitura das atas via `sincronizado-até` vs. último DHR do `CATALOGO-OFICIAL` | **SIM** |
| **Q6** | Registrar no CATÁLOGO OFICIAL e no CONFLICT-MAP (K-MAN-22 — CEE-001/RULE-CEE-002/003 citadas por analogia, não estendidas) | **SIM** |

---

## 3. Objeto homologado

- **`especificador.md`** mantém `model: claude-opus-4-8`; ganha nota operacional de **esforço médio** (§4 item 1) e a leitura obrigatória do §4 item 1 passa a ser **proporcional à complexidade**: núcleo sempre obrigatório (ROADMAP + atomic-spec + RULES.md + checagem de `ATIVADO` do RMR-001) · lista completa obrigatória só para HIGH/CRITICAL (CONFLICT-MAP, MAN-001, CATALOGO, leitura integral do RMR-001, atas EUA-E04..E18) · short-circuit via `sincronizado-até`.
- **`revisor.md`** passa `model: claude-opus-4-8` → **`claude-sonnet-4-6`**; ganha novo §0 (nota operacional de **esforço alto**) e o Passo 0 é reescrito com a mesma proporcionalidade (núcleo/lista completa/short-circuit) aplicada ao especificador.md.
- **Risco residual reconhecido e aceito (não é achado, é decisão consciente):** só a redução de modelo do Revisor é garantida por config; a compensação por "esforço alto" é política operacional não-garantível (o frontmatter de subagente do Claude Code não tem campo para "reasoning effort" — confirmado via consulta ao `claude-code-guide`). O gate M-02, os 8 passos e o Passo 5-bis (EUA-E18) permanecem obrigatórios como processo, sem excepcionalidade.
- **CEE-001 / RULE-CEE-002 / RULE-CEE-003 não são alterados** — permanecem escopados ao ORYX AGENT/Trilha B (spec-only). Esta emenda cria uma regra **nova e análoga** para a camada meta (Especificador/Revisor), sem estender aquelas regras.
- **Checagem de `ATIVADO` do RMR-001 é núcleo sempre obrigatório** — é gate (passo 11-bis do ROADMAP §23), não leitura de baseline; nunca dispensada por nenhuma complexidade. Só a leitura *integral* do painel é que pode ser dispensada em LOW.

---

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração | Estado |
|---|---|---|
| `.claude/agents/especificador.md` | §4 item 1 reescrito (leitura proporcional + short-circuit + nota de esforço médio); `sincronizado-até: DHR-EUA-E18` → `DHR-EUA-E19` (RPSA) | ✅ aplicado |
| `.claude/agents/revisor.md` | `model: claude-opus-4-8` → `claude-sonnet-4-6`; novo §0 (nota de esforço alto); Passo 0 reescrito (leitura proporcional + short-circuit); `sincronizado-até: DHR-EUA-E18` → `DHR-EUA-E19` (RPSA) | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E19 (HOMOLOGADA) + linha DHR-EUA-E19 na tabela de atas | ✅ aplicado |
| `governance/CONFLICT-MAP.md` | Emenda K-MAN-22 (CEE-001/RULE-CEE-002/003 citadas por analogia metodológica para a camada meta — não estendidas; escopo original permanece ORYX AGENT/Trilha B) | ✅ aplicado |
| `backlog/RMR-001_Painel_Backlog.md` | Passo 11-bis — gate desta homologação: nenhum item novo `ATIVADO` | ✅ aplicado |
| `governance/EUA-E19_..._PROPOSTA.md` | Status → HOMOLOGADA (referência a este DHR) | ✅ aplicado |

---

## 5. Invariantes preservados

- **INV-07/INV-09:** nenhuma ata anterior alterada; homologação formal registrada.
- **CONS-01:** nenhuma decisão aberta (J/G/H/I/K/L/C/M/N-001) fechada por esta emenda; nenhuma decisão fechada tratada como pendente.
- **RULE-MET-01 (não-fabricação):** nenhum campo de frontmatter inexistente foi declarado como existente — a limitação de plataforma (ausência de campo "reasoning effort") é registrada honestamente, com a política de esforço tratada como orientação de conduta, não configuração.
- **Gate M-02:** preservado sem excepcionalidade, para qualquer complexidade — a proporcionalidade de leitura não o afeta (RULES.md está no núcleo sempre obrigatório).
- **Gate `ATIVADO` do RMR-001 (passo 11-bis):** preservado sem excepcionalidade — movido para o núcleo, não a lista dispensável.
- **Independência estrutural do Revisor (ENF-03):** não tocada — Write/Edit continuam ausentes do `revisor.md`, independentemente do modelo.
- **RPSA (EUA-E16):** agentes re-sincronizados (`sincronizado-até` → DHR-EUA-E19).

---

## 6. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultado `backlog/RMR-001` — nenhum item novo `ATIVADO` por esta homologação (emenda de protocolo/roteamento dos agentes, não de sequência de specs). Gate fecha limpo.
2. **Primeira aplicação:** a partir de agora, toda invocação do Revisor SOT usa `claude-sonnet-4-6` com esforço alto; toda invocação do Especificador usa `claude-opus-4-8` com esforço médio. A leitura proporcional entra em vigor imediatamente — inclusive para o restante do trabalho da FASE GOV (SPEC-019 em diante).
3. **Nota de procedimento (não é item de backlog):** ao resubmeter um artefato corrigido para novo parecer, preferir continuar o mesmo agente (via mecanismo de continuação do orquestrador) em vez de instanciar um agente novo, quando prático — preserva parte do contexto/cache já pago.

---

*Ata registrada pelo Controlador. Homologação por Andraus (Decisor Final), 2026-09-21. Parecer do Revisor: CONFORME (v2, após 1º parecer NÃO CONFORME RECUPERÁVEL sobre a v1). Nenhum registro anterior removido — apenas superseded/aditado (INV-07/INV-09).*
