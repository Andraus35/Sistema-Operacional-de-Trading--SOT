# Diagnóstico Executivo: Dependências Críticas e Risco de Propagação de Erros
**Data:** 2026-09-25  
**Scope:** Síntese das 4 auditorias taxonômicas + matriz de impacto em Specs futuras  
**Propósito:** Identificar bloqueadores urgentes antes de SPEC-002, SPEC-020 e família RISK-SPEC

---

## 1. BLOQUEADORES CRÍTICOS (Risco ALTO de contaminação para próximas Specs)

| ID | Bloco | Severidade | Loci Afetados | Impacto em Specs | Ação Urgente |
|---|---|---|---|---|---|
| **CRIT-001** | CEM-001: status contradictório (Catálogo=BASELINED, arquivo="Candidato") | CRITICAL | `canon/CEM-001`, `governance/CATALOGO-OFICIAL` | SPEC-001/002/019 herdam modelo de evidência ambíguo | **Unificar status CEM-001 no Catálogo e no arquivo; emenda de compatibilidade** |
| **CRIT-002** | GPR-001: preserva Conviction 4D, thresholds antigos (60%/75%), TMP de fronteira | CRITICAL | `governance/GPR-001`, gates PAP/CIC | Próximas Specs leem GPR como norma; herdam requisitos obsoletos | **Emenda compatibilidade GPR-001 com D0–D9, Conviction 8D, Q-008/Q-009** |
| **CRIT-003** | SDD-001: Conviction Vector 4D no checklist | CRITICAL | `canon/SDD-001`, testes/lint | Specs que implementarem conforme SDD terão gating 4D | **Substituir referência 4D por 8D; preservar histórico de obsolescência** |
| **CRIT-004** | Master Orchestrator + Mission Engine: sem decisão, aparecem em Constituição como norma | CRITICAL | `governance/CONSTITUTION.md`, CEE-001, PPQ-001, SES-001 | Novo componente de orquestração pode ser criado por analogia sem Spec | **Marcar como LEGACY/UNRESOLVED na Constituição; criar decisão GOV-ORCH-001** |
| **CRIT-005** | RAG chunks: score 0–9, TMP de fronteira, score estrutural ≥60% — sem metadados de status | CRITICAL | `rag/synthesis.knowledge.md`, agente runtime | Agente lê RAG como instrução vigente, ignora cabeçalho de emenda | **Adicionar a cada chunk: `status`, `authority`, `effective_from`, `supersedes`, `do_not_use_if`** |
| **CRIT-006** | Schema Synthesis: mantém score_total 0–9, convicção_global e conviction_vector 8D (3 métricas sem contrato) | CRITICAL | `schemas/synthesis.output.json`, tests | Síntese produz 3 saídas; contrato de precedência desconhecido | **Documentar relação formal em CCM-001 ou decisão; marcar como PILOT até resolução** |
| **CRIT-007** | Catálogo: próximo passo contraditório (Trilha B = "SPEC-002" vs "SPEC-019") | CRITICAL | `governance/CATALOGO-OFICIAL.md` | Especificador não sabe qual Spec ativar | **Manter único campo vivo "próximo_artefato_por_trilha"; mover históricos para snapshot** |
| **CRIT-008** | Specs soltas (GEN-1): síntese.spec.md ainda calcula Conviction apesar de Q-007 separar Fusion/Conviction/Synthesis | CRITICAL | `specs/synthesis.spec.md`, `specs/features/` | Nova SPEC-003/CCM-001 pode duplicar cálculo ou fundir engines | **Marcar GEN-1 como `GEN-1_REFERENCE`; apontar somente a arbitragem autorizada** |
| **CRIT-009** | Carimbos de sincronização divergentes: Especificador=DHR-PROV-WEB-001, Revisor=DHR-EUA-E19, Catálogo=E19a | CRITICAL | `.claude/agents/especificador.md`, `.claude/agents/revisor.md` | Agentes operam com versões diferentes da norma | **Substituir carimbo único por: `last_sync_dhr`, `last_sync_catalog_date`, `required_sources`** |
| **CRIT-010** | Fractal: não está claro se é agente, subfunção, dimensão ou etapa futura — input/output incompletos | CRITICAL | `schemas/synthesis.input.json`, `CHM-001`, `CONSTITUTION.md` | Próxima Spec que tocar Elliott pode recriar ou absorver Fractal sem decisão | **Registrar como TAX-SPEC-003 / CAN-009: perguntar AGORA antes de Specs futuras** |

---

## 2. RISCOS ALTOS de contaminação transversal

| ID | Risco | Documentos | Propagação | Mitigação |
|---|---|---|---|---|
| **ALT-001** | Coexistência GEN-1 (software/score) + nova geração (harness/conviction) sem separação física clara | `specs/`, `schemas/`, `rag/`, tests | Lint de Specs ignora `features/`; RAG sem versioning de chunks | Marcar GEN-1 como `REFERENCE`; criar lint recursivo para `features/` |
| **ALT-002** | TMP confundido com Signal Package (interno vs fronteira) | síntese.spec.md, RAG, CEE-001, EUA-E19a | Risco Agent especificado sem saber se produz TMP ou Signal | Separar schemas: `tmp.internal`, `signal-package.frontier`; bloquear confusão |
| **ALT-003** | Decisões abertas usadas como invariantes (J-001, G-001, N-001, M-001) | ROADMAP, múltiplas Specs, RAG | Specs que fecham J-001 por inferência | Validar em PAP/CIC: nenhuma decisão aberta pode entrar como NORMA em Spec |
| **ALT-004** | Score 0–9 como filtro independente vs derivação do Conviction Vector | schemas, RAG, síntese.spec.md | CCM-001/J-001 podem não resolver | Marcar score como PILOT; criar teste que falhe se score divergir de vetor |
| **ALT-005** | Violações de hierarquia (SMC sobre Elliott, ICT cria hipótese) — detector fraco (regex) | `scripts/gate-check.js` | Variações linguísticas passam; historicamente inválidos não são pegos | Complementar gate com vocabulário controlado + IDs de regra |
| **ALT-006** | Obsolescência sem sucessão explícita (Structural Agent, Institutional Agent vs nomes atuais) | canon, RAG, prompts de agentes | Novo agente lê "Structural Agent" e não sabe se é Elliott Specialist | Criar matriz de aliases vigentes no GLOSSARIO |

---

## 3. Decisões Abertas que DEVEM ser Reabertas/Confirmadas ANTES de Specs futuras

| ID | Decisão | Status Atual | Impacto | Prazo Sugerido |
|---|---|---|---|---|
| **J-001** | Fórmula/pesos/limiares do Conviction Vector (8D confirmado, mas fórmula aberta) | OPEN | CCM-001, scores de gates, agente Conviction | **ANTES de SPEC-003 (Conviction Engine)** |
| **N-001** | Pesos por ativo (BTC/XAU/NASDAQ diferente?) | OPEN | Synthesis, Conviction | **Antes de SPEC-014 (Synthesis final)** |
| **M-001** | Estados do Blackboard p/ objetos não-hipótese | OPEN | Pipeline cognitivo, estado persistente | **Antes de implementação runtime** |
| **GOV-ORCH-001** | Identidade de Orchestrator (Master/Decision/Cognitive) | **NÃO EXISTE** | Constituição, Rules, CEE, PPQ | **ANTES de qualquer nova Spec de orquestração** |
| **RISK-ARR-LOC-001** | Localização de Risk Agent no pipeline; TMP vs Signal | OPEN | EUA-E19a restaurou Signal de fronteira, mas Risk Harness não especificado | **ANTES de RISK-SPEC-020** |
| **FRACTAL-ARCH-001** | Fractal como agente, skill, subfunção ou dimensão | **NÃO EXISTE** | Hierarquia, input/output, schemas | **ANTES de SPEC-001/002 (Elliott)** |

---

## 4. Matriz de Alcance: Qual artefato contamina qual Spec

```
GPR-001 (4D, score antigo)  ──→  gates PAP/CIC  ──→  SPEC-001/002/019/020
   │                                      │
   └──→ SDD-001 (4D checklist)  ──→  lint de Specs  ──→  SPEC-001/002/RMR
                                         │
CONSTITUTION (Master Orch.) ──→ Rules (Orchestrator) ──→ SPEC-004 (Blackboard)
   │
   └──→ CEE-001, PPQ-001 ──→ runtime proposals  ──→ SPEC-010-014 (agentes)

CEM-001 (status ambíguo)  ──→  canonicity check  ──→  SPEC-001/002/009
   │
RAG (chunks sem versioning) ──→ agente (lê como instrução)  ──→  runtime

Specs GEN-1 (síntese.spec.md)  ──→  features/SPEC-001  ──→  CCM-001/CDM-001
   │                                     │
   └──→ schemas (score, TMP)  ──→  validate-schemas  ──→  contrato inválido
```

**Cada Spec futura pode herdar camada de contaminação + adicionar suas próprias ambiguidades.**

---

## 5. Ordem Crítica de Alinhamento (próximos 7 dias)

### FASE 1: Bloqueadores imediatos (afetam gate PAP/CIC/RMR)
1. ✅ **Ler as 4 auditorias (já feito)**
2. 🔴 **ENTREVISTA ESTRUTURADA com Andraus:**
   - Visão original do SOT: era software ou sempre harness cognitivo?
   - Quando começou a migração para spec-first?
   - Score 0–9 continuará ou será substituído por CCM-001?
   - Master Orchestrator: legado do produto ou será especificado?
   - Fractal: prioridade arquitetural ou pode ser diferido?
   - Decisões J-001, N-001, FRACTAL-ARCH-001: podem aguardar ou bloqueiam SPEC-002?

3. 🔴 **Emenda de compatibilidade GPR-001** (preservar histórico, marcar obsolescências)
4. 🔴 **Resolver status CEM-001 no Catálogo** (alinhamento com BASELINED autorizado)
5. 🔴 **Corrigir carimbos de sincronização em .claude/agents/**

### FASE 2: Separação física de gerações (afeta validação)
6. 🔴 **Marcar Specs GEN-1 como `GEN-1_REFERENCE`** em heads; apontar sucessores
7. 🔴 **Adicionar versionamento a RAG chunks** (`status`, `authority`, `supersedes`)
8. 🔴 **Corrigir lint-specs.js** para cobrir recursivamente `features/`

### FASE 3: Decisões que não podem ser inferidas
9. 🔴 **Abrir decisão GOV-ORCH-001** (identidade de Orchestrator; NÃO usar Constituição como norma até resolução)
10. 🔴 **Abrir decisão FRACTAL-ARCH-001** (antes de Elliott Spec)
11. 🔴 **Tabela de aliases vigentes** (Structural Agent → Elliott Specialist, etc.)

---

## 6. Perguntas de Entrevista Estruturada (confronto com intenções iniciais)

### A. Migração software → harness cognitivo

**P.1:** O SOT foi originalmente especificado como um software (backend, API, bot)? Ou começou como descrição de agentes?

**P.2:** Quando você decidiu que seria spec-first + harness cognitivo em vez de implementação?

**P.3:** O que precisa continuar funcionando a partir da primeira geração (GEN-1) e o que pode ser descartado?

### B. Decisões abertas com risco de bloqueio

**P.4:** Qual é a prioridade de J-001 (fórmula Conviction Vector)? Bloqueia SPEC-003 ou pode ser piloto inicial?

**P.5:** Master Orchestrator era um componente de software real ou era um nome de um padrão de coordenação?

**P.6:** Fractal foi sempre uma camada entre Elliott e SMC, ou foi adicionado posteriormente? Precisa estar em SPEC-002 ou pode aguardar SPEC-010-014?

**P.7:** Score 0–9 será substituído por CCM-001, ou será mantido como filtro piloto paralelo?

### C. Conformidade com harness vigente

**P.8:** Você esperava que os canônicos (CEM, SDD, PPQ, CEE, GPR) tivessem status de BASELINED quando leu CATALOGO-OFICIAL? Ou via eles como ainda-em-formação?

**P.9:** Quando uma Spec futura encontrar "TMP" em um canônico antigo, pode assumir que EUA-E19a sobrepõe a definição anterior?

**P.10:** Se uma regra está em Rules como NORMATIVE mas a correspondente DHR foi diferida, qual prevalece?

### D. Rastreabilidade de autoridade

**P.11:** Você acha que um agente deve validar CADA regra que lê contra a cadeia governance/ → ROADMAP → ATOMIC-SPEC, ou assumir que tudo no repo está alinhado?

**P.12:** Qual é o "Single Source of Truth" para prioridade de Specs? ROADMAP ou Catálogo?

**P.13:** Se um chunk de RAG diz "score estrutural ≥60%" e o ATOMIC-SPEC diz "convicção ≥70%", qual regra prevalece?

---

## 7. Recomendação Executiva

| Ação | Prazo | Autoridade | Bloqueia |
|---|---|---|---|
| **Entrevista com Andraus sobre 13 perguntas acima** | Hoje/amanhã | Andraus | Todas as Specs futuras |
| **Emenda GPR-001 + resolve status CEM-001** | 2–3 dias | Especificador → Revisor → Andraus | PAP/CIC, SPEC-001/002 |
| **Sincronizar carimbos .claude/agents/** | 1 dia | Controloador (RMR passo 7) | Próxima DHR |
| **Marcar GEN-1 + criar lint recursivo** | 3–5 dias | Especificador/tooling | Validação de Specs futuras |
| **Criar tabela de aliases e sucessão** | 3–5 dias | Especificador | Consistência semântica |
| **Abrir decisões GOV-ORCH-001, FRACTAL-ARCH-001** | 1–2 dias | Revisor (proposta) → Andraus | SPEC-004, Elliott-related Specs |

---

## 8. Ganho de mitigação

Se fizer isto **AGORA:**
- ✅ Bloqueia contaminação de GPR-001 em SPEC-002, SPEC-019, SPEC-020
- ✅ Evita duplicação de Conviction Engine por malinterpretação de síntese.spec.md
- ✅ Não cria novo Master Orchestrator por analogia
- ✅ Fractal fica decidido antes de Elliott Spec
- ✅ RAG não propaga chunks obsoletos para runtime futuro

Se **DEIXAR PASSAR:**
- ❌ Cada nova Spec herda uma camada de ambiguidade
- ❌ Revisor gasta 30–50% do tempo em auditorias de compatibilidade em vez de conteúdo
- ❌ Risco de retrabalho em homologação (Andraus pede reescrita)
- ❌ Risk Harness (RISK-SPEC-020) entrega com contrapartida não-rastreável

---

## 9. Próximos passos desta sessão

1. **Você responde as 13 perguntas** (entrevista rápida 10–15 min)
2. **Sistematizamos respostas em decisão** (documento)
3. **Criamos emendas** ou abrimos tickets de decisão
4. **Atualizar carimbos + metadados** (tooling)
5. **Gerar relatório de conformidade** (o que ficou resolvido vs aberto)

---
