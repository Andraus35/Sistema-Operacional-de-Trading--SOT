# AGENTS.md — SOT Sistema Operacional de Trading

> Arquivo de configuração global do projeto para o Claude Code.
> Lido por todo agente ao iniciar. Define profiles, paths e regras de governança.

---

## 1. Projeto

**Nome:** SOT — Sistema Operacional de Trading  
**Domínio:** Spec-driven trading OS para BTC / XAU / NASDAQ  
**Fase atual:** Spec-first (sem código ainda — BUILD/VERIFY-de-código são adiados)  
**Repositório de arquitetura aprovada:** `approved/` (somente Andraus autoriza escrita aqui)

### Arquivos de referência na raiz (obrigatórios)

| Arquivo | Quem lê | Quando |
|---|---|---|
| `roadmap.md` | Especificador + Revisor | **Antes de qualquer entrega ou revisão** — confirma qual Spec está autorizada e as decisões abertas ativas |
| `atomic-spec.md` | Especificador + Revisor | **Antes de qualquer entrega ou revisão** — confirma o método vigente (BASpec, profundidade D0–D9, Enforcement Contract, etiquetagem) |

Se qualquer um desses arquivos estiver ausente da raiz, **nenhum agente inicia trabalho**: o Especificador para e reporta a Andraus; o Revisor emite NÃO CONFORME Crítica.

---

## 2. Agentes disponíveis

| Arquivo | Papel | Tools permitidas |
|---|---|---|
| `.claude/agents/especificador.md` | Produz Specs / Plans / Tasks / BASpecs | Read · Write · Edit · Grep · Glob |
| `.claude/agents/revisor.md` | Audita entregas; emite parecer; força prova | **Somente leitura**: Read · Grep · Glob |

> **Regra arquitetural (ENF-03):** o Revisor NÃO tem Write nem Edit.
> Isso torna estruturalmente impossível o Revisor reescrever a Spec — não é regra de conduta, é restrição de arquitetura.

---

## 3. Profiles de profundidade (PINADOS — nunca elevar em silêncio)

| Complexidade | Profundidade | Profile skill |
|---|---|---|
| LOW | D0–D3 | `light` |
| MEDIUM | D0–D5 | `light` → `standard` |
| HIGH | D0–D7 | `standard` |
| CRITICAL | D0–D8 | `standard` + adversarial (D8 nosso) |

O profile `ui` NÃO se aplica a componentes cognitivos do SOT.

---

## 4. Paths

```
(raiz do repositório)
  ├── roadmap.md                      ← sequência oficial de Specs; leitura obrigatória
  ├── atomic-spec.md                  ← método vigente (BASpec/D0–D9/Enforcement); leitura obrigatória
  ├── AGENTS.md                       ← este arquivo
  └── scripts/
      └── validate_spec_sot.py        ← gate determinístico (Detector ≠ Gate)

.claude/agents/
  ├── especificador.md                ← subagent autor (tools Read/Write/Edit/Grep/Glob)
  └── revisor.md                      ← subagent auditor (tools Read/Grep/Glob apenas)

.specs/features/<SPEC-00x>/          ← artefatos de trabalho (Spec candidata)
  ├── plan.md                         ← Spec (PLAN da skill = Spec do SOT)
  ├── checks.md                       ← verificação de spec (fase spec-first)
  └── review/                         ← parecer do Revisor
      └── parecer-<SPEC-00x>.md

approved/                             ← registro oficial; escrita somente por Andraus
  └── <SPEC-00x>-<nome>.md
```

---

## 5. Fluxo obrigatório por Spec

```
AMBOS os agentes (início obrigatório)
  → leem roadmap.md   (Spec autorizada, sequência, decisões abertas)
  → leem atomic-spec.md (método vigente: BASpec, profundidade, Enforcement Contract)

Especificador
  → [PLAN] roda tlc-spec-lean (plan.md + checks.md)
  → Autopré-check (ver especificador.md §7)
  → [entrega ao Revisor]

Revisor
  → Passo 0: confirma alinhamento com roadmap.md e atomic-spec.md (eliminatório)
  → validate_spec_sot.py (gate determinístico de estrutura — exit-code decide)
  → protocolo semântico GRE-001/HRE-001 (passos 1–8)
  → interpela Especificador: exige prova de conformidade antes de emitir veredicto
  → emite parecer (CONFORME / CONFORME condicional / NÃO CONFORME)

Andraus (gate humano final)
  → homologa → gera .md em approved/ → autoriza próxima Spec
```

**Regras invioláveis do fluxo:**
- "VERIFY" interno da skill ≠ CONFORME do Revisor ≠ homologação de Andraus.
- Nenhuma Spec inicia antes da homologação e entrega `.md` da atual (salvo decisão explícita de Andraus).
- Revisor previne desvios (primário); corrigir é exceção.

---

## 6. Skill instalada

```
tlc-spec-lean  (Tech Leads Club)
npx @tech-leads-club/agent-skills install --skill tlc-spec-lean
```

Overlay de governança: GUS-TLC-001 (adendo ao PEP-001 — não altera baselines).
Referência do método: `atomic-spec.md` (raiz) é a fonte operacional vigente no repositório; GUS-TLC-001 é a fonte normativa formal.

---

## 7. Gate determinístico

```
python scripts/validate_spec_sot.py .specs/features/<SPEC-00x>/plan.md
```

Exit 0 = passa estrutura → Revisor prossegue com protocolo semântico.  
Exit 1 = falha de estrutura → Revisor emite NÃO CONFORME Crítica sem análise semântica.  
O script decide; o LLM não é seu próprio gate (ENF-03).

---

## 8. Decisões abertas que bloqueiam entregas downstream

| ID | Descrição | Bloqueia |
|---|---|---|
| J-001 | Fórmula/pesos/limiares **definitivos** do Conviction Vector (CCM-001 pendente de redação — SPEC-003). Dimensionalidade (8) e limiares de Fase Piloto = FECHADOS (Q-008/Q-002). | E3 do gate Convicção→Decisão; SPEC-003 |
| ~~B-001~~ | **FECHADO (Q-007):** Conviction Engine é SEPARADO do Synthesis. Topologia: Fusion Engine → Conviction Engine → Synthesis. | — |
| G-001 | Schema do estado persistente por agente | SPEC-009 |
| H-001 | Knowledge Graph: grafo real ou estrutura em memória? | SPEC-006 |
| I-001 | Skills como unidades formais separadas? | SPEC-025 |
| K-001 | Ciclo P12 detalhado (evolução do conhecimento) | SPEC-018 |
| L-001 | Governança do próprio harness / policy versionada | Operação E3 |
| C-001 | Granularidade EARS multi-condição | Padrão de BASpec |

Nenhuma decisão aberta pode aparecer como invariante fechado em qualquer entrega (CONS-01).
