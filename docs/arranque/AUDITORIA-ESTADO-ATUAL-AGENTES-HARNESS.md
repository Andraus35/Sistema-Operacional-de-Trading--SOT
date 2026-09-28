# AUDITORIA DO ESTADO ATUAL DOS AGENTES E HARNESS

> **Natureza:** baseline factual do estado atual (somente leitura). **Não** contém replanejamento, **não** propõe nova arquitetura, **não** altera nenhum artefato existente.
> **Data da auditoria:** 2026-09-21 · **Método:** inspeção documental e estrutural direta do repositório `SOT-Harness`.
> **Regra de evidência:** toda conclusão traz etiqueta — **[FATO DOCUMENTADO]**, **[FATO ESTRUTURAL]**, **[INFERÊNCIA]**, **[NÃO DETERMINADO]**, **[CONFLITO DOCUMENTAL]**.

---

## 1. Escopo

Auditados integralmente (leitura completa): `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`, `governance/CONSTITUTION.md`, `governance/RULES.md`, `governance/CONFLICT-MAP.md`, `governance/CATALOGO-OFICIAL.md`, `.claude/agents/*.md` (4 arquivos), `.claude/settings.json`, `.claude/skills/harness-eval/SKILL.md`, `.claude/skills/SKILL.md` (parcial), `RETOMADA/GEH-001_…md`, `specs/features/SPEC-001/{plan,checks}.md` (checks completo), `docs/_legacy/HARNESS-REPORT.md`, `docs/arranque/auditoria-saude-harness.md`, `scripts/gate-check.js`, `scripts/validate_spec_sot.py`, `package.json`.

Inspecionados por listagem/grep (193 arquivos no total): árvore `governance/` (atas DHR-*, emendas EUA-E*), `canon/`, `reference/camadas/`, `specs/`, `schemas/`, `rag/`, `.harness-eval/runs/`, `.clinerules/`, `.claude/commands/`.

**Não lidos linha a linha** (baixa relevância ao objeto ou redundantes): corpo de `plan.md` da SPEC-001 (só `checks.md`), as 12 `reference/camadas/CAMADA *.MD`, o corpo das 22 atas/emendas DHR/EUA individuais (cobertas pelos índices CATALOGO/CONFLICT-MAP), os 5 `specs/*.spec.md` de 1ª geração, os 11 schemas JSON, os 5 `rag/*.knowledge.md`. Marcados como **[NÃO DETERMINADO]** onde a conclusão dependeria deles.

---

## 2. Método de auditoria

1. Enumeração total da árvore (193 arquivos) → mapa de superfícies.
2. Leitura dos 4 arquivos de agente + `AGENTS.md` (contrato declarado).
3. Leitura dos documentos-raiz normativos e de método (contrato efetivo).
4. Rastreio das Skills/metodologias por grep global (`harness-eval`, `harness-score`, `harness-toolkit`, `tlc-spec-lean`, `GUS-TLC`) — 762 ocorrências em 63 arquivos.
5. Inspeção dos artefatos de execução das Skills (`.harness-eval/runs/`, `package.json`, scripts de hook/gate).
6. Confronto **documentação declarada × configuração efetiva** para cada agente e cada Skill.
7. Classificação de evidência em cada conclusão.

Limite metodológico: a auditoria é estática (nenhum agente foi executado). Comportamento efetivo é inferido da configuração (frontmatter `tools`, hooks, scripts), não observado em runtime. **[FATO ESTRUTURAL]**

---

## 3. Mapa atual dos agentes

O projeto contém **duas gerações/famílias de agentes** mais **uma tríade de pipeline registrada apenas no ambiente**.

### 3.A — Família de Especificação (2ª geração, ATIVA — o trio)

#### Ficha — Especificador SOT

| Campo | Conteúdo |
|---|---|
| Nome | Especificador SOT |
| Arquivo | `.claude/agents/especificador.md` |
| Tipo | Agente (autor de especificação) |
| Responsabilidade declarada | "PRODUZIR especificações do Harness Cognitivo — Spec, Plan, Tasks e BASpecs" (§1). Não implementa, não homologa, não decide sozinho. |
| Responsabilidade efetivamente observada | Frontmatter concede `Read, Write, Edit, Grep, Glob` → **pode criar/alterar arquivos**. Consistente com o papel de autor. **[FATO ESTRUTURAL]** |
| Entradas | Gate de leitura obrigatório: `ROADMAP.md`, `atomic-spec.md`, `governance/RULES.md`, `CONFLICT-MAP.md`, `MAN-001`, `CATALOGO-OFICIAL.md`, `backlog/RMR-001`, atas EUA-E04..E14 (§4.1). |
| Saídas | `specs/features/<SPEC-00x>/plan.md` (Spec) + `checks.md` (verificação de spec); entrega "Pronto para revisão" (§11). |
| Permissões | Read · Write · Edit · Grep · Glob. |
| Restrições | §10: nunca homologa, nunca trata proposta como decidida, nunca resolve conflito crítico sozinho (`[DECISÃO NECESSÁRIA]`), nunca inventa registro/fonte, nunca avança sem homologação. |
| Dependências | Revisor; Andraus; `tlc-spec-lean` + overlay GUS-TLC-001; modelos canônicos `canon/`; decisões abertas J/G/H/I/K/L/C/M/N-001. |
| Handoff | Entrega artefato completo (plan+checks) ao Revisor; se NÃO CONFORME, reentrega texto completo revisado (§2). |
| Verificação | Autopré-check próprio (§7, ~24 itens) → gate determinístico `validate_spec_sot.py` (executado pelo Revisor) → protocolo semântico do Revisor. |
| Aprovação | Somente Andraus homologa (parecer CONFORME do Revisor ≠ autorização). |
| Persistência | Nenhum estado próprio persistente declarado; carimbo `sincronizado-até: DHR-EUA-E16` (RPSA). **[FATO DOCUMENTADO]** |
| Estado | Representado por prosa no system-prompt + carimbo de sincronização no frontmatter. Sem máquina de estados. |
| Harness associado | Harness de especificação (F.1 feedforward + gate F.2/F.3); método `atomic-spec.md`. |
| Especificação associada | Opera sobre toda a fila SPEC-001..045 (ROADMAP); fonte normativa citada: PEP-001 v1.2 + overlay GUS-TLC-001. |
| Evidência | `.claude/agents/especificador.md:1-247`; `AGENTS.md:58-63`. |

#### Ficha — Revisor SOT

| Campo | Conteúdo |
|---|---|
| Nome | Revisor SOT |
| Arquivo | `.claude/agents/revisor.md` |
| Tipo | Agente (auditor/verificador independente) |
| Responsabilidade declarada | "AUDITAR entregas do Especificador e FORÇAR PROVA" antes de emitir veredicto CONFORME / CONFORME condicional / NÃO CONFORME (§1). |
| Responsabilidade efetivamente observada | Frontmatter concede **apenas** `Read, Grep, Glob`; comentário explícito: "Write e Edit são INTENCIONALMENTE AUSENTES … impossível o Revisor reescrever a Spec (ENF-03)". A restrição é **estrutural**, não apenas de conduta. **[FATO ESTRUTURAL]** |
| Entradas | Mesmos baselines do Especificador (Passo 0, §5) + a entrega do Especificador + `scripts/validate_spec_sot.py`. |
| Saídas | Relatório de revisão estruturado (§6) + Anexo A (arquivo formal de correção quando NÃO CONFORME). **Não produz Spec.** |
| Permissões | Read · Grep · Glob (somente leitura). |
| Restrições | §1: nunca escreve/reescreve Spec, nunca homologa, nunca resolve conflito em silêncio, nunca infere aprovação, nunca trata "VERIFY" da skill como CONFORME. |
| Dependências | Especificador (objeto); Andraus (autoridade); GRE-001 v2.2 / HRE-001 v2.2 / PRE-001 v1.1; `validate_spec_sot.py`. |
| Handoff | CONFORME → Andraus; NÃO CONFORME → devolve ao Especificador com Anexo A; nunca → próxima Spec. |
| Verificação | Gate determinístico primeiro (exit 0/1) → protocolo semântico de 8 passos (eliminatórios: 0, 2, 3). |
| Aprovação | Emite parecer; **não** aprova — só Andraus homologa. |
| Persistência | Nenhuma; carimbo `sincronizado-até: DHR-EUA-E16`. |
| Estado | Prosa + tabela de veredicto; sem máquina de estados. |
| Harness associado | Harness de verificação (F.3 feedback) com gate determinístico (F.2). |
| Especificação associada | Toda a fila de Specs; fontes: PRE-001 v1.1, GRE-001/HRE-001 v2.2. |
| Evidência | `.claude/agents/revisor.md:1-278`; `AGENTS.md:58-64`; gate em `scripts/validate_spec_sot.py`. |

#### Andraus (autoridade de homologação)

Não é um agente de software — é o **decisor humano** (`souza.merchan@gmail.com`, "Andraus"). É o único ponto de homologação (`CONSTITUTION`/`GMC-001 Cap.5`; "consenso do Usuário"). Centralização de consenso/autoridade — invariante de topologia (GEH-001 §6.4). **[FATO DOCUMENTADO]**

### 3.B — Família de 1ª geração (subagentes de validação, PARCIALMENTE ATIVA/LEGADA)

#### Ficha — sot-spec-reviewer

| Campo | Conteúdo |
|---|---|
| Nome | sot-spec-reviewer |
| Arquivo | `.claude/agents/sot-spec-reviewer.md` |
| Tipo | Subagent (revisão independente de spec files) |
| Responsabilidade declarada | Revisão de `specs/*.spec.md` contra "SOT Constitution and harness standards"; EARS; consistência entre agentes. |
| Responsabilidade efetivamente observada | Frontmatter: descrição + `Use when a spec has been modified`. **Sem campo `tools` explícito** → herda o conjunto padrão. Checklist embutido opera sobre os `.spec.md` de 1ª geração (Elliott/Fibonacci/SMC/ICT/Synthesis). **[FATO ESTRUTURAL]** |
| Entradas | `specs/*.spec.md`, `CONSTITUTION.md`, schemas `.input/.output.json`. |
| Saídas | Lista numerada de findings (Finding/Location/Fix). |
| Permissões | Não declaradas no frontmatter (na listagem de agentes do ambiente aparece como "All tools"). **[FATO DOCUMENTADO]** |
| Restrições | Implícitas no checklist; sem restrição estrutural de escrita. |
| Dependências | CONSTITUTION, schemas, specs de 1ª geração. |
| Handoff | Não especificado (retorna findings ao chamador). |
| Verificação | É ele próprio um mecanismo de verificação; sem verificador acima. |
| Aprovação | Nenhuma declarada. |
| Persistência | Nenhuma. |
| Estado | Checklist estático. |
| Harness associado | Harness de 1ª geração (specs/schemas/rag dos 5 agentes analíticos). |
| Especificação associada | `elliott-wave/fibonacci/smc/ict/synthesis.spec.md`. |
| Evidência | `.claude/agents/sot-spec-reviewer.md:1-40`. |

#### Ficha — sot-schema-validator

| Campo | Conteúdo |
|---|---|
| Nome | sot-schema-validator |
| Arquivo | `.claude/agents/sot-schema-validator.md` |
| Tipo | Subagent (validação de schemas JSON) |
| Responsabilidade declarada | Valida schemas Draft-07, campos obrigatórios, consistência de contrato I/O ao longo do pipeline Elliott→Fibonacci→SMC→ICT→Synthesis. |
| Responsabilidade efetivamente observada | Regras concretas: `$schema`, `$id`, `additionalProperties:false`, checagem de score (0–3 por agente, 0–9 total), enum de sinal (COMPRA/VENDA/NEUTRO/AGUARDAR_SETUP), `ict.input.approved_hypothesis` permite null. **[FATO DOCUMENTADO]** |
| Entradas | `schemas/*.json`. |
| Saídas | Diagnóstico de conformidade. |
| Permissões | "All tools" na listagem de ambiente; sem `tools` no frontmatter. |
| Restrições | Escopo limitado a schemas. |
| Dependências | 11 schemas; pipeline de 1ª geração. |
| Handoff | Não especificado. |
| Verificação | É mecanismo de verificação. |
| Aprovação | Nenhuma. |
| Persistência | Nenhuma. |
| Estado | Regras estáticas. |
| Harness associado | 1ª geração; espelhado por `tests/validate-schemas.js` (`npm test`). |
| Especificação associada | Schemas dos 5 agentes analíticos. |
| Evidência | `.claude/agents/sot-schema-validator.md:1-38`. |

### 3.C — Tríade AXL (registrada apenas no ambiente — NÃO no repositório)

Os agentes **axl-estrategista**, **axl-analista**, **axl-controlador** aparecem na lista de "Available agent types" do ambiente, com papéis "Estrategista/Analista/Controlador" e estados `WAITING_STRATEGIST/ANALYST/CONTROLLER`. **Não existe arquivo de definição correspondente em `.claude/agents/`** (a árvore contém apenas os 4 agentes acima). **[FATO ESTRUTURAL]**

Mapeamento documental: `RULES.md` **RULE-GMC-005** define exatamente esse fluxo — "Modificação de Modelo Canônico REQUER: Estrategista (propõe) → Analista (audita) → Controlador (registra)" (`RULES.md:280-282`). O `CATALOGO-OFICIAL.md` também nomeia o **Controlador** como autoridade de registro (`:2, :132-140`). **[INFERÊNCIA]** — a tríade AXL é a materialização, em subagentes de ambiente, do fluxo GMC-001 de governança de **modelos canônicos**, distinto do trio Especificador→Revisor→Andraus de governança de **specs**. A definição desses agentes é externa a este repositório (não auditável aqui).

---

## 4. Formatação/configuração dos agentes

### 4.1 Estrutura

Padrão observado nos 4 arquivos: **frontmatter YAML** (`name`, `description`, opcional `model`, opcional `tools`, opcional `sincronizado-até`) + **corpo Markdown** que é o system-prompt.

Seções presentes por agente:

| Seção | Especificador | Revisor | sot-spec-reviewer | sot-schema-validator |
|---|---|---|---|---|
| Identidade/Missão | ✅ (§1) | ✅ (§1) | ✅ (Role) | ✅ (Role) |
| Ecossistema/Cooperação | ✅ (§2) | ✅ (§2) | — | — |
| Skill operacional | ✅ (§3) | — | — | — |
| Workflow/Protocolo | ✅ (§4) | ✅ (§3–5) | ✅ (checklist) | ✅ (steps) |
| Regras de qualidade | ✅ (§6) | ✅ (passos) | ✅ | ✅ |
| Autopré-check/Checklist | ✅ (§7) | ✅ (§5) | ✅ | ✅ |
| Invariantes | ✅ (§8) | ✅ (§2) | parcial | parcial |
| Decisões abertas | ✅ (§9) | ✅ (§8) | — | — |
| Fronteiras/Não-escopo | ✅ (§10) | ✅ (§1) | — (implícito) | — (implícito) |
| Formato de entrega/saída | ✅ (§11) | ✅ (§6) | ✅ | ✅ |
| Enforcement/permissões estruturais | via método | ✅ (Write/Edit ausentes) | — | — |

### 4.2 Consistência

- **Campos comuns a todos:** `name`, `description`, Role/Missão, algum checklist. **[FATO ESTRUTURAL]**
- **Campos só na 2ª geração (trio):** `model: claude-opus-4-8`, `tools:` explícito, `sincronizado-até:`, cabeçalho de fonte normativa (PEP-001/PRE-001), Autopré-check, Invariantes numerados, Decisões abertas.
- **Divergência de padrão:** os dois subagentes de 1ª geração **não declaram `model` nem `tools`** e usam checklist inline curto (inglês), enquanto o trio usa system-prompt longo (português) com fonte normativa versionada. **Dois padrões de definição coexistem.** **[CONFLITO DOCUMENTAL]** (não contraditório em conteúdo, mas inconsistente em forma/rigor).
- **Nomes diferentes para função semelhante:** existem **dois "revisores"** — `Revisor SOT` (spec-driven, RO estrutural) e `sot-spec-reviewer` (1ª geração, sem restrição de tools). Sobreposição parcial de função. **[CONFLITO DOCUMENTAL]**
- **Obrigatórios vs opcionais:** `name`+`description` são os únicos de fato obrigatórios (presentes em todos). `tools`/`model`/`sincronizado-até` são opcionais e presentes só no trio.
- **Duplicidade de verificação:** `sot-schema-validator` (agente) ≈ `tests/validate-schemas.js` (script `npm test`); `sot-spec-reviewer` ≈ `tests/lint-specs.js` (`npm run lint`). Verificação documentada como agente **e** como script. **[FATO ESTRUTURAL]**
- **Lacuna:** nenhum agente declara `Persistência`/`Estado`/`Observabilidade` de forma estruturada — o estado vive só em prosa e no carimbo `sincronizado-até`.

### 4.3 Grau de formalização (usando a taxonomia própria do projeto)

O projeto **já possui** taxonomia própria — não crio nova. Uso o eixo de **linguagem de especificação** (`atomic-spec.md §4`: Normativa/Comportamental/Cognitiva/Operacional/Avaliativa) e o eixo de **função de harness** (`atomic-spec.md §5`: F.1 Feedforward / F.2 Guardrails / F.3 Feedback / F.4 Evaluation). Mapeamento dos elementos dos agentes:

| Elemento | Classificação (taxonomia do projeto) |
|---|---|
| CONSTITUTION/RULES/CONFLICT-MAP citados nos agentes | **Normativo / F.1 Feedforward** |
| Restrição estrutural "Revisor sem Write/Edit" | **F.2 Guardrail** (bloqueio estrutural) |
| `validate_spec_sot.py`, `gate-check.js` (hook) | **F.2 Guardrail** (gate determinístico, ENF-03) |
| Autopré-check do Especificador | **Verificável / F.3** (auto-feedback) |
| Protocolo de 8 passos do Revisor | **Verificável / F.3 Feedback** |
| harness-eval / harness-score | **F.3 (Track A) / F.4 Evaluation** |
| Missão/Ecossistema/Filosofia (prosa) | **Descritivo / Informativo** |
| GEH-001 (ETCLOVG, 4Es, macro/micro) referenciado | **Metodológico** (pano de fundo não-normativo) |
| Trechos "na dúvida, interpele" / julgamento | **Ambíguo** (critério não determinístico) |

**Termo do projeto para "grau de formalização":** o próprio harness usa **Quality Gates L1–L4** (`atomic-spec.md §7`) e **maturidade harness-score L0–L4**. Não invento escala — os elementos verificáveis mapeiam a L1–L4; os informativos/metodológicos ficam fora dos gates.

---

## 5. Topologia entre agentes

### 5.1 Trilha de especificação (ATIVA)

```
ROADMAP.md + atomic-spec.md   (F.1 — leitura obrigatória por AMBOS)
        ↓
ESPECIFICADOR (autor · Write/Edit)
        ↓  artefato: specs/features/SPEC-00x/{plan.md, checks.md}  ·  declara "Pronto para revisão"
        ↓
[gate determinístico]  python scripts/validate_spec_sot.py plan.md   (exit 0/1 · F.2)
        ↓
REVISOR (auditor · Read-only · força prova)
        ↓  parecer: CONFORME | CONFORME condicional | NÃO CONFORME  (Relatório §6)
        ├──NÃO CONFORME──▶ volta ao Especificador (Anexo A, texto completo)
        ↓ CONFORME
ANDRAUS (homologação — único consenso válido)
        ↓  DHR-* (ata) + registro no CATALOGO-OFICIAL + entrega .md
        ↓
[passo 11-bis] consultar backlog/RMR-001 — itens ATIVADO
        ↓
próxima Spec
```

Detalhamento das relações:

| Relação | Origem → Destino | Mecanismo | Artefato | Contrato | Autoridade | Verificação | Retorno? | Bloqueio? | Escalonamento? | Evidência |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Especificador → Revisor | entrega textual + gate script | plan.md+checks.md | PEP-001/atomic-spec | Especificador (autor) | gate + Autopré-check | sim (NÃO CONFORME) | sim (exit 1) | não | `especificador.md:86-93` |
| R2 | Revisor → Andraus | parecer | Relatório de revisão | GRE-001/HRE-001 | Revisor (só verifica) | 8 passos eliminatórios | — | CONFORME condicional trava | → Andraus | `revisor.md:180-253` |
| R3 | Andraus → repo | homologação | DHR-* + CATALOGO | GMC-001 Cap.5 | Andraus (final) | consenso humano | — | sim | — | `CATALOGO-OFICIAL.md:132-149` |
| R4 | Andraus → RMR-001 | passo 11-bis | itens ATIVADO | ROADMAP §23 | Andraus/Especificador | gate de backlog | — | item ATIVADO pendente = achado | — | `ROADMAP.md:353-359` |

### 5.2 Trilha de modelos canônicos (GMC-001 / AXL — parcialmente fora do repo)

```
Estrategista (propõe)  →  Analista (audita)  →  Controlador (registra)  →  Andraus (homologa)
      [RULE-GMC-005; agentes axl-* definidos no ambiente, não no repo]
```

### 5.3 Pipeline analítico (1ª geração — objeto de spec, não agentes de processo)

```
Elliott → Fibonacci → (Fractal) → SMC → ICT → [Blackboard] → Conviction → Synthesis → TMP
```
Esse é o pipeline **especificado** (CONSTITUTION "Sequência de execução"); os `.spec.md`/schemas/rag de 1ª geração o descrevem. Não são agentes de processo do harness de especificação — são o **domínio** que o harness especifica. **[FATO DOCUMENTADO]**

### 5.4 Propriedades estruturais presentes

| Propriedade | Presente? | Evidência |
|---|---|---|
| Separação execução × verificação | **Sim** | Especificador (autor) ≠ Revisor (verifica). |
| Separação geração × avaliação | **Sim** | Autor produz; gate+Revisor avaliam. |
| Separação executor × homologador | **Sim** | Revisor verifica ≠ Andraus homologa. |
| Independência do revisor | **Sim (estrutural)** | Revisor sem Write/Edit (ENF-03). |
| Rastreabilidade requisito→spec→exec→verif | **Parcial** | Spec→Plan→Tasks rastreável; "execução" (runtime) adiada (spec-first) → elo exec ausente. |
| Harness pai → Harness filho | **NÃO (normativamente)** | Ver §12. |

---

## 6. Skills e metodologias encontradas

| Skill/metodologia | Onde aparece | Como aparece | Intenção documentada | Intenção inferida | Uso atual | Status |
|---|---|---|---|---|---|---|
| **tlc-spec-lean** | `especificador.md §3`, `AGENTS.md §5/§8`, `atomic-spec.md §14`, `ROADMAP` | Skill operacional do Especificador; PLAN=Spec, CHECKS=verif-de-spec | "Você usa a skill tlc-spec-lean … a governança do SOT fica por cima" | Motor de artefato de spec, subordinado ao overlay GUS-TLC-001 | Especificador produz plan.md/checks.md | **ATIVO (com overlay)** |
| **GUS-TLC-001** | `especificador.md §3`, `atomic-spec.md` | Overlay de governança sobre a skill | Mapeia PLAN→Spec, CHECKS→verif, "VERIFY"→feedback≠homologação | Camada que impede a skill de virar autoridade | Regra de mapeamento | **ATIVO** |
| **harness-eval** (TLC v1.8.3) | `.claude/skills/harness-eval/` (skill instalada) + `.harness-eval/runs/` (2 execuções) + `atomic-spec §5 (F.3)` | Skill dual-judge instalada; runs reais 2026-09-09 e 2026-09-11 | Avaliar o próprio harness (paths quebrados, redundância, utilidade) | Auditoria de saúde do harness (Track A determinístico usado; B/C opcionais) | Rodado ≥2× (Track A) | **ATIVO (Track A) / PARCIAL (B/C)** |
| **harness-score** (TLC) | `package.json` (`npm run eval/score/score:diff` → `npx harness-score`), `HARNESS-REPORT §2.1`, `auditoria-saude-harness §6` | CLI externo de maturidade L0–L4 | Medir maturidade do harness | Métrica de maturidade + gate de progresso informal | Rodado: L2(66%)→L4(94%) | **ATIVO (diagnóstico/métrica)** |
| **harness-toolkit** | — | **Nenhuma ocorrência no repositório** | — | — | — | **NÃO ENCONTRADO** |
| **tlc-spec-driven** | citado por exclusão em `harness-eval/SKILL.md` | "specify feature → tlc-spec-driven" (skill vizinha) | — | Alternativa mais pesada; não adotada aqui | — | **REFERENCIADO (não usado)** |
| **sot-harness-spec** (skill própria) | `.claude/skills/SKILL.md` | Skill-referência mestre que internaliza GEH-001 (ETCLOVG, 4Es, macro/micro) + BASpec | "Referência mestre para especificação e validação" | Documento-guia interno; não é o motor operacional | Referência de consulta | **REFERENCIADO / PARCIAL** |
| **smart-spec** (skill) | `auditoria-saude-harness.md:2`, memórias | Método de diagnóstico (Parte 8; ETCLOVG; Gates L1-L4) | Diagnóstico de saúde do harness | Usada em auditoria pontual | 1 auditoria | **REFERENCIADO / PARCIAL** |
| **sot-especificador-pap001** (skill) | `.claude/skills/sot-especificador-pap001/SKILL.md` | Skill que assume papel de Especificador do PAP-001 (Trilha A) | Produzir o PAP-001 | Instância do Especificador para governança de princípios | PAP-001 homologado | **ATIVO (Trilha A, concluído)** |
| **update-spec / validate-harness** (commands) | `.claude/commands/*.md` | Workflows de 1ª geração | Atualizar spec / validar harness | Automação de 1ª geração | espelham `npm test/lint` | **PARCIAL / LEGADO** |
| **PEP-001 / PRE-001 / GRE-001 / HRE-001** | cabeçalhos dos agentes do trio | Fontes normativas do system-prompt | Prompt do autor / do revisor / catálogo-harness do revisor | Contratos normativos do trio (versionados) | vigentes | **ATIVO (normativo)** |
| **GEH-001** | `RETOMADA/GEH-001…md`, `SKILL.md`, CATALOGO | Guia generalista de spec+harness+topologia | "pano de fundo conceitual generalista" (não-normativo) | Fonte dos frameworks macro/micro | Referência | **REFERENCIADO (não-normativo)** |

---

## 7. Auditoria específica do `tlc-spec-lean`

1. **Onde aparece:** `especificador.md §3`; `AGENTS.md §5,§8,§128`; `atomic-spec.md §6,§14,§46`; `ROADMAP.md:5,11`. **[FATO DOCUMENTADO]**
2. **Quem deveria usá-lo:** o **Especificador** (autor). O Revisor **não** a usa. **[FATO DOCUMENTADO]**
3. **Fase:** SPECIFY (fase spec-first). BUILD e VERIFY-de-código explicitamente **adiados** (`atomic-spec §14`, `especificador §3`). **[FATO DOCUMENTADO]**
4. **Parte incorporada:** PLAN e CHECKS. BUILD/VERIFY diferidos.
5. **PLAN tratado como SPEC?** **Sim** — "`plan.md` da skill = Spec do SOT" (`especificador §3`). **[FATO DOCUMENTADO]**
6. **CHECKS como verificação?** **Sim, mas como verificação de SPEC** (bem-formação de BASpec/EARS/Enforcement), **não** teste de runtime (`especificador §3`; `checks.md` da SPEC-001 confirma: 38 checks estruturais, zero de runtime). **[FATO DOCUMENTADO]**
7. **Handoff:** PLAN+CHECKS → Autopré-check → Revisor. O "VERIFY" interno da skill é feedback, entregue antes do Revisor. **[FATO DOCUMENTADO]**
8. **Frozen obligations aparecem?** A skill "congela obrigações" por design (descrição da skill), mas no SOT o congelamento efetivo é a **homologação de Andraus / INV-09** ("sem baseline informal"). O mecanismo da skill é subsumido pela governança. **[INFERÊNCIA]**
9. **Checks derivados das obrigações?** **Parcial** — os checks da SPEC-001 derivam do **método** (atomic-spec: BASpec/EARS/Enforcement/Constitution Check), não de uma lista de "obrigações congeladas" no sentido estrito da skill. **[INFERÊNCIA]**
10. **Mutations / adversarial verification aparecem?** No método sim (D8 adversarial, `atomic-spec §2`); **não** como recurso da skill tlc-spec-lean explicitamente. O adversarial é do harness próprio, não importado da skill. **[NÃO DETERMINADO]** (corpo da skill externa não auditável no repo).
11. **Verificador interno da skill confundido com o Revisor?** **Explicitamente NÃO** — três documentos afirmam "VERIFY da skill ≠ CONFORME ≠ homologação" (`AGENTS.md:87`, `especificador §3`, `atomic-spec §14`). Prevenção ativa de confusão. **[FATO DOCUMENTADO]**
12. **A metodologia é usada como:** método de **especificação** (primário) + **verificação-de-spec** (CHECKS). **Não** é usada como método de implementação (adiado) nem de governança (a governança é do trio/Andraus, não da skill). **[FATO DOCUMENTADO]**

**Mistura de responsabilidades identificada:** o único ponto de mistura potencial — "verificador da skill = Revisor" — é **explicitamente neutralizado** pelo overlay GUS-TLC-001. Não há mistura ativa. Ressalva: a skill cobre simultaneamente **spec** e **verificação-de-spec**, e o Especificador é quem roda ambos (autor produz seus próprios CHECKS) — o que **não** substitui o Revisor, mas concentra spec+auto-verificação no autor. **[INFERÊNCIA]**

---

## 8. Auditoria específica do `harness-eval`

1. **Onde aparece:** skill instalada em `.claude/skills/harness-eval/` (SKILL.md v1.8.3 + PROTOCOL/judge-prompts/scripts); execuções em `.harness-eval/runs/2026-09-09-full/` e `2026-09-11-full/`; classificado em `atomic-spec §5` como **F.3 Feedback (Track A)**; citado em `HARNESS-REPORT §2.2`. **[FATO DOCUMENTADO]**
2. **Quem deveria executá-lo:** o **Claude Code** operando o harness (não o trio Especificador/Revisor). É ferramenta de auditoria do harness, à parte do fluxo de spec. **[INFERÊNCIA]**
3. **Momento:** sob demanda (auditoria de saúde), não por Spec. Rodado em 2026-09-09 e 2026-09-11. **[FATO DOCUMENTADO]**
4. **O que avalia hoje:** o **harness** (superfícies AGENTS.md/rules/skills): Track A = paths/comandos citados existem; Track B = redundância; Track C = utilidade. **[FATO DOCUMENTADO]**
5. **Avalia:** o **Harness** (superfícies de instrução). **Não** avalia a SPEC de domínio, nem o agente analítico, nem a execução, nem o "projeto" como um todo. **[FATO DOCUMENTADO]**
6. **Tracks/dimensões:** Track A (Correctness, determinístico), Track B (Redundancy, dual-judge), Track C (Usefulness, dual-judge). Resultado registrado: Track A com 10 BROKEN — **todos internos ao próprio harness-eval**, 0 nas superfícies SOT (`HARNESS-REPORT §2.2`). B/C não executadas (requerem Q2). **[FATO DOCUMENTADO]**
7. **Critérios incorporados à arquitetura:** a **taxonomia F.1–F.4** de `atomic-spec §5` cita harness-eval como F.3; **SPEC-020** (ROADMAP) planeja uma "Harness Evaluation Specification" própria com dimensões (correctness, grounding, RAG faithfulness, hallucination, tool correctness, role adherence, …). **[FATO DOCUMENTADO]**
8. **Como os critérios são usados:** **como avaliação posterior / referência** (F.3), rodada sobre o harness já existente. **Não** como requisito herdado, nem como Quality Gate de spec, nem como validação final de Spec.

**Ponto crítico — uso constitutivo durante a especificação:**

> **Não foi encontrada evidência documental de uso constitutivo do `harness-eval` durante a especificação.** Os `checks.md` da SPEC-001 (38 checks) verificam BASpec/EARS/Enforcement/Constitution Check — nenhuma dimensão de harness-eval é usada como parâmetro de construção da SPEC. O harness-eval avalia superfícies de instrução do repositório (AGENTS.md/rules/skills), **depois**, não a SPEC de domínio **durante**. **[FATO ESTRUTURAL]**

---

## 9. Auditoria específica do `harness-score`

1. **Onde aparece:** `package.json` (`"eval": "npx harness-score"`, `"score": "npx harness-score --json"`, `"score:diff": "npx harness-score --diff"`); `HARNESS-REPORT §2.1`; `auditoria-saude-harness §6`; `AGENTS.md:125` ("npx harness-score — maturidade do harness (opcional)"). **[FATO DOCUMENTADO]**
2. **Quem o utiliza:** operador do harness via npm/npx (não o trio). **[FATO DOCUMENTADO]**
3. **Quando:** sob demanda / snapshot de maturidade. Registrado: L0(13%)→L2(66%) em 2026-09-09; L2→**L4(102/108, 94%)** em 2026-09-15. **[FATO DOCUMENTADO]**
4. **Significado atual do resultado:** **diagnóstico de maturidade** (L0–L4) + **métrica** por dimensão (Context/Skills/Hooks/Sensors/CI/Hygiene). Usado para justificar decisões ("não aplicar CTX-04/HYG-08 deliberadamente"). **[FATO DOCUMENTADO]**
5. **Usado como:** **diagnóstico** + **métrica informativa** + parcialmente **critério de maturidade** (o "L4/94%" é citado como evidência de homologação da baseline F.1, `CATALOGO §6:144`). **Não** é Quality Gate bloqueante de Spec, **não** é condição formal de aprovação, **não** é parâmetro de construção de SPEC, **não** é critério de regressão automatizado (embora `--diff` exista, não há gate que o consuma). **[FATO ESTRUTURAL]**

**Relação Harness-superior → maturidade → SPEC-descendente → Harness-descendente:**

> Existe **maturidade planejada** como **SPEC-021** ("Harness Score / Maturity Model", L0 Declarativo → L4 Autocontrolado) no ROADMAP. Mas **não existe, hoje, mecanismo normativo** que faça requisitos de maturidade de um Harness superior descerem como requisito para uma SPEC descendente ou seu micro-harness. O `harness-score` mede a maturidade **do repositório inteiro**, uma vez, não por nível hierárquico. **Não há herança de requisito de maturidade macro→micro.** **[FATO ESTRUTURAL / NÃO ENCONTRADO]**

---

## 10. Auditoria específica do `harness-toolkit`

- **Conceitos incorporados:** nenhum sob o nome `harness-toolkit` — **grep retorna zero ocorrências** em todo o repositório. **[FATO ESTRUTURAL / NÃO ENCONTRADO]**
- **Hooks/regras/policies existentes (independentemente do nome):** existem sim, sob outros mecanismos:
  - **Hooks:** `.claude/settings.json` registra `PreToolUse`(Write|Edit)→`gate-check.js` e `PostToolUse`(Write|Edit)→`post-edit-check.js`. **[FATO DOCUMENTADO]**
  - **Floor rules:** o conceito existe como **"piso por tipo"** de Enforcement (E1/E2/E3 mínimos, `atomic-spec §10.2`) e **pisos de profundidade** (D-alvo por complexidade). Não sob o rótulo "floor rule". **[INFERÊNCIA]**
  - **Checks:** `validate_spec_sot.py` (10 checks STRUCT-01..10), `tests/validate-schemas.js`, `tests/lint-specs.js`, `checks.md` por Spec. **[FATO DOCUMENTADO]**
  - **Decisões registradas:** atas `DHR-*`, `CATALOGO-OFICIAL`, `backlog/RMR-001`, `CIC-001`. **[FATO DOCUMENTADO]**
  - **Rastreabilidade:** etiquetagem TRACE-06, cadeia Spec→Plan→Tasks, cadeia de derivação SES-001 §60. **[FATO DOCUMENTADO]**
  - **allow/ask/deny:** **planejado** (SPEC-042 "Runtime Guardrails: allow; deny; gates"), não implementado. O `gate-check.js` é um deny binário sobre 3 padrões. **[FATO DOCUMENTADO]**
- **Aparece na SPEC / Harness / runtime?** Os gates aparecem no **harness de spec** (gate-check, validate_spec) e no **método** (Enforcement Contract). O runtime (allow/ask/deny genérico, sandbox) está **adiado** (SPEC-042/043). **[FATO DOCUMENTADO]**

**Separação Especificação ≠ Verificação ≠ Enforcement ≠ Runtime — onde cada um está hoje:**

```
Especificação  → atomic-spec.md (método), specs/features/SPEC-00x/plan.md, ROADMAP (o QUÊ)
      ≠
Verificação    → Revisor (semântico) + validate_spec_sot.py + checks.md + npm test/lint + harness-eval (F.3)
      ≠
Enforcement    → Enforcement Contract E0–E3 (contrato, na Spec) + gate-check.js hook (mecanismo, parcial) + "Revisor sem Write" (estrutural)
      ≠
Runtime        → ADIADO (spec-first). SPEC-042 Runtime Guardrails / SPEC-043 Context Integrity / SPEC-038-039 Tools — todos PLANEJADOS, não implementados.
```
**[FATO ESTRUTURAL]**

---

## 11. Intenção de uso (por Skill)

| Skill | A. Intenção documentada | B. Intenção operacional observável | C. Intenção inferida |
|---|---|---|---|
| tlc-spec-lean | "Você usa a skill … a governança do SOT fica por cima" (`especificador §3`) | Produz plan.md/checks.md da SPEC-001 | — |
| GUS-TLC-001 | Mapeia artefatos da skill ao vocabulário SOT | Regra de tradução PLAN→Spec | INFERÊNCIA: existe para **impedir** que a skill vire autoridade de homologação |
| harness-eval | "Evaluate a repo agent harness … broken paths, redundancy, usefulness" (SKILL.md) | Track A rodado 2×; 0 broken em SOT | INFERÊNCIA: incorporado como **sensor F.3 de saúde do harness de instruções**, não como gate de spec — não encontrado como decisão normativa explícita |
| harness-score | "maturidade do harness (opcional)" (`AGENTS.md:125`) | L2→L4 medido; usado como evidência de baseline | INFERÊNCIA: usado como **régua de maturidade e narrativa de progresso**; a não-aplicação de melhorias (CTX-04/HYG-08) foi decisão consciente registrada — sinal de uso reflexivo, não cego |
| harness-toolkit | — | — | INFERÊNCIA: **nunca incorporado**; possível referência de vocabulário TLC que não chegou a este repo — não encontrado como decisão |
| sot-harness-spec (própria) | "Referência mestre … integra GEH-001 + BASpec" | Documento de consulta | INFERÊNCIA: tentativa de **internalizar o GEH-001** (macro/micro) na skill do projeto, mas o motor operacional migrou para tlc-spec-lean — resíduo de transição parcial |
| GEH-001 | "pano de fundo conceitual generalista" (não-normativo) | Citado como fundamento dos 4Es/ETCLOVG | INFERÊNCIA: fonte-mãe da ideia macro→micro, mantida deliberadamente **fora** do baseline normativo |

> Regra respeitada: onde a intenção é apenas inferida, está marcada **INFERÊNCIA — não encontrada como decisão normativa explícita**.

---

## 12. Macro → Micro (a questão arquitetural central)

**Pergunta:** existe hoje um mecanismo que faça `Master Harness → requisitos herdados → Harness intermediário → SPEC → micro-Harness → checks → verificação`?

### O que existe (conceitualmente)

- **GEH-001** descreve o arcabouço macro/micro (ETCLOVG, 4Es, centralizar/descentralizar, verificador como subagente) — mas é **explicitamente não-normativo** ("pano de fundo conceitual generalista", `GEH-001:9,432`; CATALOGO §4 nota). **[FATO DOCUMENTADO]**
- **MAN-001** (Mapa da Arquitetura Normativa) estabelece **convergência HORIZONTAL** entre nós normativos N1–N17 + sensor de drift — é coordenação entre camadas de mesmo nível, **não** herança vertical macro→micro. **[FATO DOCUMENTADO]**
- **Taxonomia F.1–F.4** (`atomic-spec §5`) organiza funções de harness (feedforward→evaluation) — é uma tipologia funcional, **não** uma cadeia de herança entre harnesses. **[FATO DOCUMENTADO]**
- **Quality Gates L1–L4** e **maturidade L0–L4** existem como escalas, mas medem um harness por vez.

### O que NÃO existe (normativamente)

Não há, em nenhum documento baselined:
- contrato de **herança** de requisitos de um Harness pai para um Harness filho;
- **propagação** normativa de checks/critérios de avaliação/requisitos de maturidade macro→micro;
- **conservação de invariantes** verificada por nível (só há invariantes globais INV-01..10, aplicados igualmente a tudo);
- **rastreabilidade pai→filho** entre harnesses;
- regra de **impossibilidade de enfraquecimento silencioso** entre níveis (existe CONS-01/INV-09 contra enfraquecimento **de decisões**, não entre **harnesses aninhados**);
- **conformance entre níveis**.

**Demonstração documental:**
1. **Existe?** Não como mecanismo normativo; apenas como ideia em documento não-normativo (GEH-001) e skill-referência (sot-harness-spec).
2. **Onde?** A ideia vive em `RETOMADA/GEH-001` e `.claude/skills/SKILL.md`; o normativo (MAN-001) implementa **horizontal**, não vertical.
3. **Como funciona?** Não funciona como herança — funciona como convergência horizontal + gates locais por Spec.
4. **Elementos propagados hoje:** invariantes globais (INV-01..10), Constitution Check (CC-01..CC-10), 4Es, método atomic-spec — mas por **aplicação uniforme a toda Spec**, não por herança pai→filho.
5. **Elementos NÃO propagados:** requisitos de maturidade (harness-score), critérios de harness-eval, checks de um harness superior para um micro-harness.
6. **Propagação é normativa ou conceitual?** **Conceitual** (GEH-001) — **não normativa**.

> **Conclusão §12:** a arquitetura de **Harness Hierárquico macro→micro NÃO está implementada**. Existe apenas o **substrato conceitual** (GEH-001) e um **análogo horizontal** (MAN-001). A propagação vertical é ambição documentada, não regra vigente. **[FATO ESTRUTURAL]**

---

## 13. Simetria Especificação ↔ Verificação

### Nível SPEC ↔ Harness (existe, forte)

Há simetria alta no nível da Spec individual: cada obrigação do método tem verificação correspondente.

| O que a SPEC exige | O que verifica | Simétrico? |
|---|---|---|
| Cabeçalho (complexidade/profundidade) | STRUCT-01/09 (`validate_spec_sot.py`) + checks.md | ✅ |
| Constitution Check CC-01..CC-10 | STRUCT-02 + Passo 3 do Revisor | ✅ |
| Etiquetagem TRACE-06 | STRUCT-03/08 + Passo 4 | ✅ |
| EARS | STRUCT-04 + lint-specs | ✅ |
| BASpec completa | STRUCT-05 + Passo 5 | ✅ |
| Enforcement Contract | STRUCT-06 + Passo 7 (ENF-01..08) | ✅ |
| CONS-01 (decisão aberta ≠ fechada) | STRUCT-07/10 + Passo 4 | ✅ |
| Schemas I/O | validate-schemas.js + sot-schema-validator | ✅ |

### Nível Master Harness ↔ Harness descendente (NÃO existe)

> **Não há simetria macro** porque não há Master Harness normativo do qual descer obrigações a harnesses descendentes (§12). A simetria existente é **intra-Spec**, não **inter-nível**. **[FATO ESTRUTURAL]**

### Assimetrias/anomalias detectadas

- **Verificações sem origem normativa formal rastreável:** o `gate-check.js` bloqueia 3 padrões (ICT cria hipótese / R:R<1:3 / SMC sobrepõe Elliott) por regex — derivam de INV/RULE, mas o mapeamento regex→RULE não é documentado no próprio script. **[INFERÊNCIA]**
- **Obrigações do método sem verificação determinística:** disciplinas cognitivas N8–N17 (RULE-EPI/SEM/…/MET) são exigidas no Autopré-check e no Passo 3, mas **não** têm check determinístico em `validate_spec_sot.py` — dependem do julgamento semântico do Revisor. **[FATO ESTRUTURAL]**
- **Requisitos que desaparecem na decomposição:** as 11 emendas EUA-E04..E14 estão homologadas "vigência imediata" mas **ainda não incorporadas ao RULES.md** (v1.5 diferida ao piloto) — vivem só nas atas, exigindo "ponte via atas" (`especificador §4.1`). Requisito normativo disperso entre RULES.md e 11 atas. **[CONFLITO DOCUMENTAL]**
- **Verificação duplicada:** schema validado por agente (`sot-schema-validator`) **e** por script (`validate-schemas.js`) — mesma obrigação, dois mecanismos.

---

## 14. Conflitos e redundâncias

| # | Ocorrência | Classificação | Arquivos | Evidência |
|---|---|---|---|---|
| C-01 | Dois "revisores": `Revisor SOT` (RO estrutural) vs `sot-spec-reviewer` (1ª ger., sem restrição de tools) | **SOBREPOSIÇÃO / LEGADO** | `.claude/agents/revisor.md`, `sot-spec-reviewer.md` | funções análogas, gerações distintas |
| C-02 | Verificação de schema como agente **e** como script npm | **DUPLICIDADE** | `sot-schema-validator.md`, `tests/validate-schemas.js` | `AGENTS.md`, `package.json` |
| C-03 | Duas famílias de agente com formatos de definição diferentes (com/sem `tools`,`model`) | **AMBIGUIDADE (de padrão)** | `.claude/agents/*` | §4.2 |
| C-04 | RULE-* cognitivas (EPI..MET) homologadas mas fora do RULES.md (só nas atas até v1.5) | **DEPENDÊNCIA IMPLÍCITA** | `RULES.md` vs `governance/EUA-E04..E14` | `especificador §4.1`; `CATALOGO §4` |
| C-05 | Dois eixos de maturidade/gate: Quality Gates L1–L4 (atomic-spec §7) vs harness-score L0–L4 vs maturidade GPR L0–L5 | **SOBREPOSIÇÃO controlada** | `atomic-spec`, `CONFLICT-MAP` K-MAN-01/02 | colisões anotadas, resolvidas por "não adotar rótulos externos" |
| C-06 | Tríade AXL registrada no ambiente sem definição no repo | **LACUNA** | ambiente vs `.claude/agents/` | §3.C |
| C-07 | `harness-toolkit` citado no briefing de auditoria, ausente do repo | **LACUNA / LEGADO** | — | grep-zero |
| C-08 | Duas trilhas (A Principiológica / B Harness) com índices de "próximo passo" separados — risco de colisão de sequência | **DEPENDÊNCIA IMPLÍCITA** | `CATALOGO §0` "regra anti-colisão" | `CATALOGO-OFICIAL.md:41` |
| C-09 | `sot-harness-spec` (skill própria que internaliza GEH) vs `tlc-spec-lean` (motor operacional real) | **REDUNDÂNCIA / LEGADO** | `.claude/skills/SKILL.md` vs `especificador §3` | duas "referências mestre" |
| C-10 | Pipeline analítico de 1ª geração (`specs/*.spec.md`, D0–D3) a ser substituído por SPEC-010..014 | **LEGADO (declarado)** | `specs/`, `auditoria-saude-harness §5` | "thin, serão substituídos" |
| C-11 | Estados cognitivos §7 do MC-COG-001 conflitam com CHM-001 | **CONTRADIÇÃO (rejeitada/gerida)** | `reference/camadas/MC-COG-001`, CONFLICT-MAP K-MAN-16 | rejeitado, prevalece CHM |
| C-12 | Modelos canônicos CCM/CDM/CNM referenciados mas **pendentes de redação** | **LACUNA (planejada)** | `CATALOGO §1` | SPEC-003 redige CCM |
| C-13 | `docs/_legacy/` (AGENTSV2, HARNESS-REPORT, PROMPT_HARNESS…) | **LEGADO (isolado)** | `docs/_legacy/` | superseded, preservado por INV-07 |

Ocorrências **SEM PROBLEMA** relevantes: a separação Especificador/Revisor/Andraus é coerente e reforçada em múltiplos documentos; a distinção Skill≠Engine≠Agent é consistente; INV-01..10 estáveis.

---

## 15. Matriz de rastreabilidade

`NÃO ENCONTRADO` = elo não existe no estado atual.

| Documento normativo | Agente | Skill | SPEC | Harness (F) | Check | Evidence | Verification | Evaluation |
|---|---|---|---|---|---|---|---|---|
| CONSTITUTION.md (P01–P14, INV) | Especificador+Revisor | tlc-spec-lean | todas | F.1 Feedforward | gate-check.js (3 padrões) | atas DHR | Revisor Passo 2 | NÃO ENCONTRADO |
| RULES.md (RULE-*) | ambos | — | por Spec | F.1 | validate_spec_sot STRUCT-02 | checks.md | Revisor Passo 3 | NÃO ENCONTRADO |
| atomic-spec.md (método) | Especificador | tlc-spec-lean | todas | F.1/F.2 | STRUCT-01..10 | checks.md | Revisor 8 passos | harness-score (repo) |
| ROADMAP.md | Especificador | tlc-spec-lean | SPEC-001..045 | — | passo 11-bis (RMR) | CATALOGO | Andraus | NÃO ENCONTRADO |
| CEE-001 (4Es/salvaguardas) | ambos | — | todas | F.1/F.2 | gate-check (R:R) | — | Revisor Passo 2/6 | NÃO ENCONTRADO |
| CHM-001/CEM-001 (canônicos) | Especificador | — | SPEC-001/002 | — | STRUCT (CC-02) | checks.md SPEC-001 | Revisor Passo 3 | NÃO ENCONTRADO |
| GMC-001 (RULE-GMC-005) | AXL (ambiente) | — | — | G (Governança) | — | CATALOGO/Controlador | Analista | NÃO ENCONTRADO |
| EUA-E04..E14 (RULE cognitivas) | ambos (via atas) | — | piloto SPEC-001 (retroativo) | F.1 | NÃO ENCONTRADO (sem check determinístico) | atas | Revisor Passo 3 (semântico) | NÃO ENCONTRADO |
| SPEC-020 (Harness Eval Spec) | — | harness-eval (proxy atual) | PLANEJADO | F.4 | NÃO ENCONTRADO | NÃO ENCONTRADO | NÃO ENCONTRADO | harness-eval (repo-level) |
| SPEC-021 (Harness Score/Maturity) | — | harness-score (proxy atual) | PLANEJADO | F.4 | NÃO ENCONTRADO | HARNESS-REPORT | NÃO ENCONTRADO | harness-score L0–L4 |
| GEH-001 (macro→micro) | conceitual | sot-harness-spec | NÃO ENCONTRADO (não normativo) | conceito ETCLOVG | NÃO ENCONTRADO | NÃO ENCONTRADO | NÃO ENCONTRADO | NÃO ENCONTRADO |

---

## 16. Estado dos componentes

| Componente | Estado atual | Evidência | Papel atual | Papel pretendido aparente | Problema | Confiança |
|---|---|---|---|---|---|---|
| Especificador (trio) | **IMPLEMENTADO** | `especificador.md` | Autor de Spec | Autor sob Harness Hierárquico | concentra spec+auto-check | Alta |
| Revisor (trio) | **IMPLEMENTADO** | `revisor.md` (RO) | Verificador independente | Verificador independente | — | Alta |
| Andraus | **IMPLEMENTADO** (humano) | CATALOGO §6 | Homologador único | Homologador único | gargalo central (por design) | Alta |
| sot-spec-reviewer | **LEGADO/PARCIAL** | `sot-spec-reviewer.md` | Revisão de 1ª ger. | superseded pelo Revisor | sobreposição C-01 | Média |
| sot-schema-validator | **PARCIAL** | `sot-schema-validator.md` | Valida schemas | validação de schema | duplica npm test C-02 | Média |
| Tríade AXL | **REFERENCIADO (ambiente)** | RULE-GMC-005; agent-types | Governança de canônicos | fluxo GMC-001 | sem def. no repo C-06 | Média |
| tlc-spec-lean | **IMPLEMENTADO (uso)** | `especificador §3` | Motor de spec | Motor de spec | externo (não versionado no repo) | Alta |
| harness-eval | **IMPLEMENTADO (Track A)** | `.harness-eval/runs/` | Sensor F.3 do harness | proxy de SPEC-020 | não-constitutivo | Alta |
| harness-score | **IMPLEMENTADO (métrica)** | `package.json`, §6 audit | Maturidade F.4 | proxy de SPEC-021 | não é gate | Alta |
| harness-toolkit | **INDETERMINADO / ausente** | grep-zero | — | — | não existe | Alta |
| gate-check.js (hook) | **IMPLEMENTADO (parcial)** | `settings.json`, script | Guardrail F.2 | enforcement runtime | cobre só 3 padrões | Alta |
| validate_spec_sot.py | **IMPLEMENTADO** | script | Gate determinístico | Gate determinístico | robusto (10 checks) | Alta |
| Harness Hierárquico macro→micro | **DOCUMENTADO (conceito)** | GEH-001, SKILL.md | pano de fundo | arquitetura-alvo | não normativo | Alta |
| MAN-001 (convergência horizontal) | **IMPLEMENTADO (normativo)** | CATALOGO §4 | coordenação horizontal N1–N17 | — | ≠ herança vertical | Alta |
| SPEC-020/021 (meta-harness) | **PLANEJADO** | ROADMAP §13 | — | avaliação/maturidade formal | não iniciado | Alta |
| Pipeline analítico 1ª ger. (specs/schemas/rag) | **DEFINIDO, INSUFICIENTE / LEGADO** | `auditoria-saude-harness §5` | referência corrigida | substituído por SPEC-010..014 | D0–D3 thin | Alta |
| Modelos canônicos CCM/CDM/CNM | **PLANEJADO** | CATALOGO §1 | — | canônicos futuros | pendentes de redação | Alta |
| SPEC-001 (Hypothesis Harness) | **IMPLEMENTADO/HOMOLOGADO** | `specs/features/SPEC-001/` | 1ª Spec baseline | — | — | Alta |

---

## 17. Respostas às 20 questões

**Q1 — Configuração/formatação real dos agentes hoje:** frontmatter YAML (`name`,`description`,±`model`,±`tools`,±`sincronizado-até`) + system-prompt Markdown. **Dois padrões coexistem**: trio de 2ª geração (rico, versionado, com pisos e invariantes) e subagentes de 1ª geração (enxutos, sem `tools`/`model`). **[FATO ESTRUTURAL]**

**Q2 — Contrato atual de cada agente:** Especificador = produzir Spec/Plan/Tasks (RW); Revisor = auditar e forçar prova, emitir parecer (RO estrutural); sot-spec-reviewer = revisão de spec de 1ª ger.; sot-schema-validator = validar schemas. Contratos de I/O são prosa + checklist, não schema formal. **[FATO DOCUMENTADO]**

**Q3 — Responsabilidades realmente separadas:** autor (Especificador) × verificador (Revisor) × homologador (Andraus) — separação **estrutural** (Revisor sem Write/Edit). Governança de canônicos (AXL/GMC) separada da governança de specs (trio). **[FATO ESTRUTURAL]**

**Q4 — Sobreposição entre agentes:** (a) Revisor SOT × sot-spec-reviewer; (b) sot-schema-validator × `validate-schemas.js`; (c) Autopré-check do Especificador × parte do protocolo do Revisor (o autor pré-verifica o que o Revisor re-verifica). **[FATO DOCUMENTADO]**

**Q5 — Papel real do Specifier:** autor único das Specs em fase spec-first, operando `tlc-spec-lean` sob overlay GUS-TLC-001, produzindo plan.md(=Spec)+checks.md(=verif-de-spec), sob gate de leitura obrigatória e Autopré-check; não homologa, não decide conflito crítico. **[FATO DOCUMENTADO]**

**Q6 — Papel real do Reviewer:** auditor independente que roda gate determinístico + 8 passos semânticos, **interpela** o autor exigindo prova (prevenir > corrigir), emite CONFORME/condicional/NÃO CONFORME; impossibilitado estruturalmente de reescrever a Spec. **[FATO DOCUMENTADO]**

**Q7 — Papel real do Executor/ambiente de execução:** **adiado** (spec-first). O "ambiente de execução" hoje é o próprio Claude Code + hooks (gate-check/post-edit) + scripts npm/python. Runtime de trading (SPEC-042/043) não implementado. Camada E do ETCLOVG = N/A declarado. **[FATO DOCUMENTADO]**

**Q8 — Papel reservado à homologação humana:** Andraus é o **único** consenso válido; homologa via ata DHR + registro no CATALOGO; nenhum agente/skill/parecer substitui isso (invariante de centralização de autoridade). **[FATO DOCUMENTADO]**

**Q9 — Como tlc-spec-lean é usado:** como método de **especificação + verificação-de-spec** (PLAN=Spec, CHECKS=verif), com BUILD/VERIFY-de-código adiados e o "VERIFY" interno explicitamente rebaixado a feedback. Ver §7. **[FATO DOCUMENTADO]**

**Q10 — Como harness-eval é usado:** como **sensor F.3 de saúde do harness de instruções** (Track A determinístico rodado 2×; B/C opcionais não executadas). Avalia superfícies AGENTS.md/rules/skills, **não** a SPEC de domínio. Ver §8. **[FATO DOCUMENTADO]**

**Q11 — Como harness-score é usado:** como **diagnóstico/métrica de maturidade L0–L4** do repositório (L2→L4/94%), citado como evidência de baseline; **não** é gate bloqueante nem parâmetro de Spec. Ver §9. **[FATO DOCUMENTADO]**

**Q12 — Como harness-toolkit é usado:** **não é usado** — ausente do repositório (grep-zero). Os conceitos correlatos (hooks, checks, floor/pisos, allow-deny) existem sob outros mecanismos e nomes. Ver §10. **[FATO ESTRUTURAL / NÃO ENCONTRADO]**

**Q13 — Metodologias usadas constitutivamente na criação das SPECs ou só depois?** **tlc-spec-lean = constitutivo** (é o motor de criação). **harness-eval e harness-score = posteriores/avaliativos** — não há evidência de uso constitutivo durante a especificação (os checks.md da SPEC-001 não usam nenhuma dimensão de harness-eval/score). **[FATO ESTRUTURAL]** → **"Não foi encontrada evidência documental de uso constitutivo de harness-eval/harness-score durante a especificação."**

**Q14 — Existe algo equivalente a um Harness Inheritance Contract?** **Não.** Existem: invariantes globais uniformes (INV/CC), convergência horizontal (MAN-001), pisos por tipo de Enforcement (E1–E3) e gates por Spec — mas **nenhum contrato de herança vertical pai→filho** entre harnesses. Ver §12. **[FATO ESTRUTURAL / NÃO ENCONTRADO]**

**Q15 — Conservação de requisitos macro→micro?** Parcial e **por aplicação uniforme**, não por herança: INV-01..10, CC-01..CC-10, 4Es e o método aplicam-se a toda Spec igualmente. Requisitos de maturidade/avaliação (harness-score/eval) **não** descem por nível. **[FATO ESTRUTURAL]**

**Q16 — Simetria especificação↔verificação?** **Alta no nível intra-Spec** (cada obrigação do método tem check/passo correspondente); **inexistente no nível inter-harness** (não há Master Harness do qual descer). Ver §13. **[FATO ESTRUTURAL]**

**Q17 — Onde a arquitetura já suporta Harness Hierárquico:** (a) o **conceito** completo existe em GEH-001 e na skill `sot-harness-spec`; (b) a **separação de papéis** autor/verificador/homologador é a fundação topológica correta (GEH-001 §6); (c) o **verificador independente estrutural** (Revisor RO) é o "subagente verificador sempre seguro" do §6.6; (d) **MAN-001** dá o mecanismo de convergência (adaptável a vertical); (e) o **método por complexidade** (D0–D9, pisos por tipo) já é uma forma de especialização proporcional. **[INFERÊNCIA]**

**Q18 — Onde ainda NÃO suporta:** (a) sem contrato de herança de requisitos entre harnesses; (b) harness-eval/score não-constitutivos e repo-global, não por nível; (c) SPEC-020/021 (meta-harness) apenas planejadas; (d) runtime/enforcement genérico adiado; (e) requisitos cognitivos N8–N17 sem check determinístico; (f) duas gerações de agentes e dois eixos de maturidade ainda coabitam. **[FATO ESTRUTURAL]**

**Q19 — Conceitos incorporados por decisão consciente:** trio Especificador→Revisor→Andraus; Revisor RO estrutural (ENF-03); gate determinístico `validate_spec_sot.py`; Enforcement Contract E0–E3; 4Es (Q-009); Conviction 8D (Q-008); método atomic-spec/BASpec; taxonomia F.1–F.4; harness-eval/score como sensores; overlay GUS-TLC-001 sobre a skill; MAN-001 (convergência horizontal); duas trilhas A/B com regra anti-colisão. **[FATO DOCUMENTADO]**

**Q20 — Prováveis resíduos de versões anteriores:** (a) `sot-spec-reviewer` + `sot-schema-validator` (1ª geração, formato divergente); (b) `specs/*.spec.md` + schemas + rag de 1ª geração (D0–D3, "a substituir"); (c) `docs/_legacy/*` (AGENTSV2, HARNESS-REPORT, PROMPT_HARNESS); (d) skill própria `sot-harness-spec` parcialmente suplantada por tlc-spec-lean; (e) commands `update-spec`/`validate-harness` de 1ª geração; (f) menção a `harness-toolkit` sem lastro. **[INFERÊNCIA]**

---

## 18. Lacunas de informação (o que não pôde ser determinado)

1. **Corpo da skill `tlc-spec-lean`** — não versionada neste repo; "frozen obligations", mutations e adversarial da skill não auditáveis aqui. **[NÃO DETERMINADO]**
2. **Definições dos agentes AXL** (`axl-estrategista/analista/controlador`) — registradas no ambiente, sem arquivo no repo. Tools/prompts reais não auditáveis. **[NÃO DETERMINADO]**
3. **Corpo do `plan.md` da SPEC-001** — lido só o `checks.md`; conteúdo integral das 7 BASpecs/4 ECs inferido pelos checks. **[NÃO DETERMINADO parcial]**
4. **12 `reference/camadas/CAMADA *.MD`** e corpo das 22 atas/emendas — cobertos por índices; conteúdo linha a linha não lido. **[NÃO DETERMINADO parcial]**
5. **`post-edit-check.js`** e os 5 `.spec.md`/11 schemas/5 rag — inspecionados por referência, não linha a linha. **[NÃO DETERMINADO parcial]**
6. **Como o ambiente resolve `sot-especificador-pap001` vs `Especificador SOT`** (duas instâncias de "Especificador") — relação exata entre a skill PAP-001 (Trilha A) e o agente (Trilha B) não totalmente explícita. **[NÃO DETERMINADO]**

---

## 19. Evidências críticas (âncoras que sustentam as conclusões mais importantes)

- **Separação estrutural autor/verificador:** `revisor.md:9-14` ("Write e Edit são INTENCIONALMENTE AUSENTES … ENF-03"); `AGENTS.md:63`.
- **Trio de autoridade:** `especificador.md:43-48`; `revisor.md:55-60`; `CATALOGO-OFICIAL.md:132-149`.
- **Gate determinístico ≠ homologação:** `validate_spec_sot.py:1-16, 370-373`; `AGENTS.md:87-89`.
- **harness-eval/score como F.3/F.4 (não constitutivos):** `atomic-spec.md:79-84`; `checks.md` SPEC-001 (38 checks, nenhum de harness-eval); `HARNESS-REPORT.md:100-109`; `package.json:8-11`.
- **harness-toolkit ausente:** grep global = 0 ocorrências.
- **Macro→micro apenas conceitual:** `GEH-001:9, 432`; `CATALOGO-OFICIAL.md:101-104`; MAN-001 = convergência **horizontal** (`CATALOGO §4`).
- **AXL = GMC-001:** `RULES.md:280-282` (RULE-GMC-005 Estrategista→Analista→Controlador).
- **Emendas cognitivas fora do RULES.md:** `especificador.md:75`; `CATALOGO-OFICIAL.md:84-97`.
- **Maturidade medida (L2→L4):** `auditoria-saude-harness.md:75-90`.
- **Hooks de enforcement:** `.claude/settings.json:1-26`; `gate-check.js:22-35`.

---

## 20. Conclusão factual do estado atual

O SOT-Harness é, hoje, um **harness de especificação spec-first maduro no eixo horizontal**, com três ativos arquiteturais sólidos e uma ambição vertical ainda não construída.

**O que já funciona (preservar):**
1. **Topologia de autoridade correta e estruturalmente reforçada** — Especificador (autor, RW) → Revisor (verificador, **Read-only por design**, ENF-03) → Andraus (homologação humana única). É exatamente a base que GEH-001 §6 prescreve (escrita/consenso centralizados; verificador como subagente seguro).
2. **Gate determinístico real** (`validate_spec_sot.py`, 10 checks) separado do julgamento semântico (Detector ≠ Gate), com hooks de enforcement (`gate-check.js`).
3. **Método atômico verificável** (atomic-spec/BASpec/EARS/Enforcement Contract E0–E3/Constitution Check) com **simetria intra-Spec alta** entre o que a Spec exige e o que se verifica.
4. **Sensores de harness já instalados e exercitados** — harness-eval (Track A, 0 broken em SOT) e harness-score (L4/94%), rodados como **avaliação posterior**, não como parte constitutiva.
5. **Governança rastreável** — CATALOGO (SSoT), atas DHR, backlog RMR-001 com gatilho de ativação, duas trilhas com regra anti-colisão.

**O que ainda não existe (a construir no replanejamento):**
1. **Harness Hierárquico macro→micro** — existe só como **conceito não-normativo** (GEH-001) e skill-referência parcialmente suplantada (`sot-harness-spec`). Não há **Harness Inheritance Contract**, nem propagação/conservação vertical de invariantes, checks, critérios de avaliação ou requisitos de maturidade. MAN-001 resolve o **horizontal**, não o vertical.
2. **Uso constitutivo de harness-eval/harness-score** — hoje são **posteriores**; SPEC-020/021 (as versões normativas próprias) estão **apenas planejadas**.
3. **Simetria inter-nível** (Master Harness ↔ harnesses descendentes) — inexistente porque não há Master Harness normativo.

**Decisões legadas a tratar conscientemente (não carregar sem intenção):** a família de agentes de 1ª geração (`sot-spec-reviewer`, `sot-schema-validator` + `specs/*.spec.md`/schemas/rag D0–D3), a skill própria `sot-harness-spec`, os commands de 1ª geração, `docs/_legacy/*`, a menção órfã a `harness-toolkit`, e o formato divergente entre as duas gerações de definição de agente.

### Resposta à pergunta final

> **Qual é exatamente o ponto de partida arquitetural que temos hoje para replanejar os agentes e incorporar o Harness Hierárquico, preservando o que funciona e evitando legado sem intenção?**

O ponto de partida é um **trio de especificação spec-first sólido e verificável (Especificador RW → Revisor Read-only → Andraus), assentado sobre um método atômico com gate determinístico e simetria intra-Spec forte, e sobre sensores de harness já instalados (harness-eval/harness-score) porém usados apenas como avaliação posterior** — enquanto a ideia de **Harness Hierárquico macro→micro existe somente como pano de fundo conceitual (GEH-001) e um análogo horizontal normativo (MAN-001), sem nenhum contrato de herança vertical, sem propagação de requisitos/maturidade entre níveis e sem as SPEC-020/021 que os tornariam constitutivos.**

Concretamente, replanejar significa: **(a) preservar** o trio, o gate determinístico, o método atomic-spec e a governança rastreável; **(b) promover** GEH-001/`sot-harness-spec` de conceito a normativo, transformando a convergência horizontal do MAN-001 em herança vertical explícita (um Harness Inheritance Contract) e tornando harness-eval/harness-score **constitutivos** (parâmetros herdados de macro para micro, via SPEC-020/021); **(c) desativar ou reescopar deliberadamente** o legado de 1ª geração (subagentes, specs thin, skill-referência duplicada, commands, `harness-toolkit` órfão) para que não seja carregado por inércia.

Esta baseline é factual e destinada ao replanejamento posterior. **Nenhum arquivo existente foi alterado; nenhuma nova arquitetura foi proposta aqui.**

---

*Auditoria de estado atual — somente leitura. Produzida em 2026-09-21. Evidências ancoradas em arquivo:linha. Replanejamento (Master Document do Specifier, do Reviewer, Harness Hierárquico, relação SPEC↔Harness, herança macro→micro, uso constitutivo de Harness Eval/Score) fica para etapa posterior.*
