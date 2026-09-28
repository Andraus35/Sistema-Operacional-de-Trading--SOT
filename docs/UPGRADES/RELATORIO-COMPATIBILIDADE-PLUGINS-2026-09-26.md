# Relatório de Auditoria — Compatibilidade do SOT com os plugins/ferramentas em `UPGRADES/`

**Data:** 2026-09-26 · **Natureza:** somente leitura (nenhum arquivo existente foi alterado; este relatório é o único arquivo criado)
**Status normativo:** NÃO-NORMATIVO — insumo para decisão de Andraus. Não fecha decisão aberta (CONS-01), não cria baseline (INV-09).

---

## 1. Veredito executivo

| Candidato | Veredito | Condição |
|---|---|---|
| **claude-mem** (memória persistente) | **NÃO ADOTAR agora** | Compatível tecnicamente, mas sobrepõe a memória nativa já em uso e depende de hooks que o SOT hoje não sustenta (ver B-01). Só após C-01 + política homologada. |
| **Headroom** (compressão de contexto) | **PILOTO EXTERNO isolado** | Nunca sobre conteúdo normativo; sem `headroom learn`; sem MCP até haver spec de compressão. |
| **Understand-Anything** (grafo) | **BAIXO VALOR como está; manter como artefato não-normativo** | Grafo só tem arestas file→função; não captura as relações que definem a complexidade do SOT. |

**Achado transversal mais importante (não está em nenhuma das auditorias anteriores):** os hooks `PreToolUse`/`PostToolUse` do SOT provavelmente **não funcionam** (B-01). Todas as três avaliações partem da premissa "os guardrails existentes devem permanecer ativos" — premissa que precisa ser corrigida antes de qualquer plugin que também registre hooks.

---

## 2. Escopo e método

**Inventário de `UPGRADES/`** (18 arquivos): 3 execuções de auditoria em `claude-code-setup-audit/` (setup geral 09-24; claude-mem 09-24/09-25; Headroom 09-25) + `understand-anything-graph/` (`knowledge-graph.json` 188 KB, `meta.json`).

**Método:** (a) leitura integral dos 18 arquivos; (b) reexecução dos gates no estado de hoje; (c) teste empírico dos hooks; (d) cruzamento com AGENTS.md, RULES/CONFLICT-MAP/CATALOGO, ROADMAP, RMR-001, MC-EXP-001, DHR-EUA-E19; (e) análise estrutural do grafo.

**Limite declarado (RULE-MET-01):** as capacidades upstream de claude-mem e Headroom (README, requisitos, comandos) foram **herdadas das auditorias anteriores, não reverificadas** por mim. Onde uso essas capacidades, marco *[upstream, não reverificado]*.

---

## 3. Verificação independente das auditorias anteriores

| Afirmação das auditorias | Resultado hoje |
|---|---|
| `npm test` 11/11 schemas | ✅ Confirmado (11/11) |
| `npm run lint` 5/5 specs | ✅ Confirmado, agora 9 arquivos: 4 ok, 5 skipped (GEN-1), 0 fail |
| SPEC-001 passa 10 checks | ✅ Confirmado |
| SPEC-019 falha STRUCT-10 (M-04) | ⚠️ **Persiste.** IDs `L-001, K-001, J-001` sem marca de pendência em janela de ±200 chars. Ver §4.4 |
| Sem manifesto de plugin / sem `~/.claude-mem` / sem `~/.headroom` | ✅ Confirmado (nenhum dos dois diretórios existe) |
| Hooks existem e referenciam scripts presentes | ✅ Existem — mas **ver B-01: não é o mesmo que funcionar** |
| `harness-score` 102/108 | Não reexecutado (requer `npx`/rede) |
| Existe doc de camada de memória | ✅ `reference/camadas/CAMADA MEMÓRIA.MD` = **MC-EXP-001**, "Status: BASELINE" no próprio doc, porém **admitido só ao backlog BL-011 (Em espera), referência externa, não-normativo** (DHR-MC-EXP-001). O cabeçalho do doc não deve ser lido como baseline do SOT. |
| Governança de tokens existe | ✅ DHR-EUA-E19 (roteamento de modelo + leitura proporcional + short-circuit `sincronizado-até`) |

---

## 4. Achados

### B-01 — CRÍTICO: os hooks do SOT são, na prática, inertes

Evidência (teste executado):

- `scripts/gate-check.js` lê `process.env.HOOK_TOOL_INPUT`. Alimentado com um payload violador **por stdin** (`{"tool_name":"Write","tool_input":{"file_path":"specs/x.spec.md","content":"ICT pode criar hipótese"}}`) → **exit 0, nenhuma violação detectada**. Alimentado pela variável de ambiente → exit 1, violação detectada.
- Segundo o contrato de hooks do Claude Code *[conhecimento geral, recomendo confirmar na doc oficial da versão instalada]*: o payload chega por **stdin** com o formato `tool_input.file_path` (aninhado), e o bloqueio exige **exit 2** — não exit 1. O script usa env var, campo no nível raiz e `exit(1)`.
- Ainda: `filePath.includes('specs/')` usa barra normal; no Windows o `file_path` chega com `\`. Mesmo corrigindo o canal, o filtro de caminho não casaria.
- `post-edit-check.js` tem o mesmo defeito de canal (lê env var), então não valida JSON pós-edição.

Impacto: o "guardrail constitucional" (ICT não cria hipótese; R:R ≥ 1:3; SMC não sobrepõe Elliott) **não está sendo aplicado por hook**. As auditorias de claude-mem e Headroom exigem "verificar que gate-check.js continua executando" — hoje não há comportamento a preservar. Isso também deixa claude-mem como o único conjunto de hooks realmente ativo, o que inverte a relação de governança pretendida.

Nota: o escopo do gate é regex sobre 3 padrões; mesmo funcionando, é uma rede de segurança, não prova de conformidade. O gate autoritativo continua sendo `validate_spec_sot.py` + Revisor.

### B-02 — ALTO: claude-mem duplicaria a memória nativa já em uso

O projeto já opera memória persistente nativa do Claude Code (`~/.claude/projects/.../memory/MEMORY.md`, ~35 entradas de estado de projeto: homologações, decisões abertas, precedentes). Adicionar claude-mem *[upstream, não reverificado: injeta contexto por hooks de ciclo de vida, SQLite + busca vetorial opcional]* cria **duas fontes de recall concorrentes**, com risco de:

- contradição entre memórias (ex.: uma diz "SPEC-019 homologada", o gate diz FAIL — ver §4.4);
- injeção silenciosa de contexto acima da leitura obrigatória (ROADMAP + atomic-spec), contra a regra de precedência normativa que o próprio rascunho `draft-memory-policy.md` já reconhece;
- crescimento de custo de contexto, oposto ao objetivo de EUA-E19.

A política rascunhada (`draft-memory-policy.md`) é coerente com INV-05/I-EXP-09 ("memória não tem autoridade decisional") e com INV-07 — ponto forte — mas: **retenção de 30/180 dias conflita com INV-07** (versionamento monotônico, "nada é deletado") *se* a memória vier a guardar registros com valor de baseline. A política precisa distinguir **memória de trabalho (descartável)** de **registro histórico (imutável, já coberto por atas DHR)**. Sugiro que memória nunca seja o repositório de decisões; atas DHR são.

### B-03 — ALTO (governança): nenhum dos três está registrado onde a governança exige

- `CATALOGO-OFICIAL.md:27` lista `UPGRADES/` e só o grafo, com "verificar status em RMR-001".
- `RMR-001` **não contém** entrada para Understand-Anything, claude-mem ou Headroom. O "verificar status" aponta para um item inexistente.
- Auditorias de claude-mem e Headroom não constam no CATALOGO.
- Não há Gatilho de Ativação definido → o mecanismo do RMR-001 (item ATIVADO aparece no gate) não consegue surfacear essas decisões.

Recomendação: admitir ao RMR-001 como itens de backlog "Em espera" (padrão BL-010..016), com gatilho explícito, em vez de deixá-los como pasta solta.

### B-04 — MÉDIO: Headroom — bom encaixe, mas o risco crítico (H-02) é real e confirmado pela natureza do corpus

Concordo integralmente com H-01..H-06 do relatório de 09-25. Reforços específicos ao SOT:

- O corpus SOT é **normativo e de precisão lexical**: `DEVE/NÃO DEVE`, IDs (`INV-*`, `RULE-*`, `J-001`), "≥ 3.0" vs "1:3", estados de decisão (ABERTA/FECHADA). Compressão com perda que preserve "sentido médio" pode inverter uma decisão aberta em fechada — exatamente o que CONS-01 proíbe.
- **Contradição interna com a regra de leitura obrigatória:** AGENTS.md exige que agentes *leiam* ROADMAP/atomic-spec; um proxy que comprime o tool-result de `Read` sobre esses arquivos altera o que "leitura obrigatória" significa. A lista de não-comprimíveis (H-02) deve ser mais ampla que a proposta: incluir `governance/*` inteiro (atas DHR, RULES, CONFLICT-MAP, CATALOGO), `canon/`, `schemas/`, `specs/features/*/plan.md|checks.md`, `backlog/`, `reference/camadas/` quando citado como fonte.
- **Espaço de ganho legítimo é estreito e mensurável:** saídas de `npm test`/`lint`/`validate_spec_sot.py`, logs, `.claude/skills/harness-eval/runs/` (27 nós/arquivos de run históricos) e leituras exploratórias de `docs/_legacy/`. Aí a compressão é segura.
- `headroom learn` escrevendo em `AGENTS.md`/`CLAUDE.md` [upstream, não reverificado] colidiria com INV-09 (baseline só por Andraus/Controlador) e com o RPSA (agentes sincronizados por DHR). Proibir, como recomendado em H-05.
- Modo mais seguro: **proxy/wrapper em perfil descartável, medição apenas**; MCP (`headroom_retrieve`) só depois de spec — ele altera o protocolo cognitivo dos agentes, o que seria emenda EUA-E##.
- Coerência com EUA-E19: o SOT já reduz custo por roteamento de modelo e leitura proporcional. Headroom seria uma terceira alavanca; medir o ganho *incremental* sobre E19 antes de acrescentar superfície de manutenção (Python/uv + possivelmente Bun ao lado de Node 20).

### B-05 — MÉDIO: Understand-Anything — o grafo existe, mas não mapeia o que importa

Análise estrutural do `knowledge-graph.json`:

| Métrica | Valor | Leitura |
|---|---|---|
| Nós | 308 (208 file, 97 function, 3 class) | |
| Arestas | 100, **todas** `file→function`/`file→class` | **Zero arestas entre arquivos.** Nenhuma relação RULE/INV/SPEC/DHR/canon |
| Camadas | Core 186 · Data 11 · Test 11 | "Core" contém 90% de tudo — camada não discrimina |
| Nós `.md` com resumo genérico | 164 ("docs file (markdown, N lines)") | Sem conteúdo semântico |
| Nós de `harness-eval/runs/` | 27 | Ruído histórico incluído como "core" |
| Funções/classes | 100, todas dos ~12 arquivos `.py`/`.js` | O SOT é ~85% Markdown |
| Snapshot | 2026-09-24, `gitCommitHash: "uncommitted"`, 208 arquivos | Repositório hoje tem 226 (excl. UPGRADES) → **já defasado** |
| Gerador | "deterministic structural analyzer" | Não é análise semântica |

Conclusão: para um repositório spec-first, a complexidade está nas **referências cruzadas** (atas → RULES → CONSTITUTION → canon; specs → INV/RULE). O grafo não as contém, então não substitui e nem complementa o `CATALOGO-OFICIAL` ("fonte autoritativa de localização"). Risco: passar a ser lido como um segundo locator competindo com o CATALOGO. Recomendações: (1) rotulá-lo formalmente não-normativo; (2) se houver interesse, regerar com extração de referências de tokens `RULE-*/INV-*/SPEC-*/DHR-*/J-001` como arestas — aí passa a ter valor (detecção de órfãos e de drift, complementando MAN-001 §sensor de drift); (3) excluir `runs/` e `docs/_legacy/` da análise.

### B-06 — MÉDIO: SPEC-019 ainda reprova o gate determinístico, contradizendo o baseline

ROADMAP:27 e DHR-SPEC019-001 declaram SPEC-019 **homologada** e L-001 **FECHADA**. O gate `STRUCT-10` reprova a mesma spec. Causa (código, `validate_spec_sot.py:281-323`): o regex de "marcação de pendência" só reconhece *aberta/pendente/bloqueador/não baselined/[DECISÃO NECESSÁRIA]/em aberto*. Uma decisão **legitimamente fechada** (L-001) nunca tem esses termos → falso positivo; J-001/K-001 reprovam por estarem citados fora do raio de 200 chars de um marcador. Isso confirma M-04 do relatório de 09-24, agora com a causa localizada. Correção deve ser via emenda do detector (reconhecer FECHADA/HOMOLOGADA/ID-com-status), **nunca** desabilitando o check. Por que importa aqui: qualquer plugin de memória que registre "SPEC-019 homologada" vs. gate FAIL cria a contradição descrita em B-02.

### B-07 — BAIXO: itens do relatório de setup (09-24) reconfirmados

M-01 (copilot-setup-steps ausente), M-02 (frontmatter Cline), M-03 (`validate-harness.md` referencia `HARNESS-REPORT.md` possivelmente ausente), M-05 (não é plugin distribuível) — sem mudança; nenhum bloqueia os candidatos acima. M-05 tem relevância nova: **o SOT não é um plugin**, então "compatibilidade com plugins" significa *coexistência no ambiente do usuário*, não integração.

---

## 5. Matriz de compatibilidade

| Dimensão | claude-mem | Headroom | Understand-Anything |
|---|---|---|---|
| Runtime (Node 20 / Py / Bun) | Node 20 ✅ + Bun *[upstream]* | Python/uv + Node 20 + talvez Bun *[upstream]* | Já gerado; sem runtime no projeto |
| Coexistência de hooks | ❌ **Bloqueada por B-01** (não há hook funcional de referência) | ⚠️ Proxy/wrapper pode reescrever config do agente | ✅ N/A |
| Colisão com memória/contexto nativo | ❌ Sobrepõe memória nativa (B-02) | ⚠️ Altera o tool-result de leituras obrigatórias | ✅ Nenhuma |
| INV-07 (imutabilidade) | ⚠️ Retenção 30/180d precisa segregar do histórico | ✅ Não apaga originais (cache local) *[upstream]* | ✅ Snapshot |
| INV-09 / CONS-01 (baseline/decisões abertas) | ⚠️ Risco de decisão aberta virar "fato" recuperado | ❌ **H-02**: compressão com perda de estado da decisão | ✅ Só estrutural |
| Escrita fora da governança | ⚠️ Escreve fora do repo (`~/.claude-mem`) | ❌ `headroom learn` → AGENTS/CLAUDE.md *[upstream]* | ✅ Nenhuma |
| Ganho esperado | Médio (continuidade de sessão) | Médio-alto só em saídas de ferramenta/logs | Baixo (B-05) |
| Registro em RMR-001/CATALOGO | ❌ ausente | ❌ ausente | ⚠️ parcial |
| **Recomendação** | Adiar | Piloto isolado | Manter não-normativo; regerar se houver uso |

---

## 6. Plano recomendado (ordem)

1. **C-01 — Corrigir os hooks** (pré-requisito de tudo): ler stdin JSON (`tool_input.file_path` / `tool_input.content|new_string`), usar `exit 2` para bloquear, normalizar `\`→`/`. Testar com o payload acima. *Exige emenda/aprovação — altera arquivos existentes; não executei.*
2. **C-02 — Corrigir STRUCT-10** para reconhecer estados FECHADA/HOMOLOGADA, com fixtures de regressão (SPEC-019 deve passar sem enfraquecer o bloqueio para IDs realmente abertos).
3. **C-03 — Admitir os três ao RMR-001** com gatilhos (padrão BL-010..016): p.ex. claude-mem → gatilho `milestone: FASE 3 (Memória) iniciada` ou decisão SPEC-045-RUNTIME-001; Headroom → `evento: custo de contexto medido acima de limiar`; grafo → `evento: extração de referências cruzadas disponível`.
4. **C-04 — Piloto Headroom** em perfil descartável (nunca no perfil de trabalho): medir tokens/preservação/recall apenas sobre saídas de ferramenta e logs; lista de não-comprimíveis ampliada (B-04); `headroom learn` desligado.
5. **C-05 — claude-mem só após C-01 e política homologada**, com as correções: (a) segregar memória de trabalho vs. registro histórico (INV-07); (b) declarar precedência: memória < leitura obrigatória < atas; (c) decidir explicitamente se substitui ou coexiste com a memória nativa (hoje há duas).
6. **C-06 — Grafo:** rotular não-normativo; regerar com arestas de referência se for usado.

## 7. O que NÃO fazer
- Não desabilitar `STRUCT-10` nem enfraquecer o gate para "passar" SPEC-019.
- Não instalar Headroom/claude-mem no perfil de trabalho antes de C-01.
- Não tratar `CAMADA MEMÓRIA.MD` (MC-EXP-001) como baseline; é referência externa em backlog.
- Não fechar J-001/G-001/SPEC-045-RUNTIME-001 por conveniência de integração de memória.

## 8. Decisões que cabem a Andraus
1. Autorizar C-01/C-02 (alteram `scripts/`)? 
2. Memória: substituir a nativa por claude-mem, coexistir, ou nenhuma?
3. Admitir os três itens ao RMR-001 (C-03)?
4. Autorizar piloto Headroom isolado?
