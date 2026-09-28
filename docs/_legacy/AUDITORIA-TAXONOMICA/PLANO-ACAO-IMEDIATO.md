# Plano de Ação Imediato: Resolução de Dependências (próximos 7 dias)

**Data:** 2026-09-25  
**Status:** PROPOSTA (à espera de suas respostas ao Questionário)  
**Autoridade:** Síntese das 4 auditorias + confronto com intenções iniciais

---

## SEQUÊNCIA DE EXECUÇÃO

### DIA 1 (hoje/amanhã): CAPTURA E SISTEMATIZAÇÃO

**Você faz:**
1. ✏️ Responde **QUESTIONARIO-ENTREVISTA-RAPIDA.md** (14 perguntas, ~15 min)
2. 📤 Envia respostas ou edita o arquivo

**Eu faço:**
3. 📊 Sistematizo respostas em **DECISÕES FORMAIS** (documento):
   - Decisões que ficam **FECHADAS IMEDIATAMENTE** (A.2, B.2, B.3, C.3, E.1)
   - Decisões que viram **TICKETS DE ABERTURA FORMAL** (F.1, F.2, etc.)
   - Decisões que viram **EMENDAS** (GPR-001, CEM-001)

4. 📋 Crio **MATRIZ DE IMPACTO POR DECISÃO**:
   ```
   Se J-001 = [sua resposta] → afeta CCM-001, SPEC-003, gates
   Se Fractal = [sua resposta] → afeta Elliott-Specs, CONSTITUTION, schemas
   ```

---

### DIAS 2–3: EMENDAS CRÍTICAS

**Tarefas paralelas (delegáveis):**

#### TAREFA 1: GPR-001 Compatibilidade
- **O quê:** Criar emenda que marca:
  - ✅ Conviction **8D** (não 4D) — Q-008 vigente
  - ✅ Conviction **≥70%** (não ≥60%) — Q-002 vigente
  - ✅ Thresholds operacionais como `PILOT` (até CCM-001)
  - ✅ Preservar texto histórico (INV-07)
- **Arquivo:** `governance/GPR-001_emenda_compatibilidade.md` ou marcar inline
- **Gate:** Revisor confere semântica; Andraus homologa
- **Bloqueia:** Specs futuras herdam norma corrigida
- **Tempo:** 2–3 horas

#### TAREFA 2: Status CEM-001
- **O quê:** Unificar status entre Catálogo (BASELINED) e arquivo (Candidato)
  - ✅ Atualizar cabeçalho de `canon/CEM-001` para refletir Catálogo
  - ✅ Adicionar referência a `governance/CATALOGO-OFICIAL.md`
- **Gate:** Revisor verifica consistência
- **Tempo:** 30 min

#### TAREFA 3: Sincronizar carimbos .claude/agents/
- **O quê:** Atualizar:
  - `especificador.md`: `last_sync_dhr = DHR-EUA-E19a`
  - `revisor.md`: `last_sync_catalog_date = 2026-09-25`
  - Adicionar `required_sources = [ROADMAP.md, ATOMIC-SPEC.md, CATALOGO-OFICIAL.md]`
- **Gate:** Controlador verifica (passo 7 de RMR)
- **Tempo:** 30 min

---

### DIAS 4–5: METADADOS E SEPARAÇÃO DE GERAÇÕES

#### TAREFA 4: Marcar Specs GEN-1
- **O quê:** Adicionar em cada arquivo `specs/*.spec.md`:
  ```
  ---
  generation: GEN-1_REFERENCE
  status: SUPERSEDED_BY
  successor: [SPEC-00X quando houver, ou TBD]
  normative_authority: NONE — referência histórica
  do_not_create_components_by_analogy: true
  ---
  ```
- **Arquivos:** `specs/elliott-wave.spec.md`, `fibonacci.spec.md`, `smc.spec.md`, `ict.spec.md`, `synthesis.spec.md`
- **Efeito:** Lint, agentes, futuras Specs saibam que são referência
- **Tempo:** 1 hora

#### TAREFA 5: Adicionar versionamento a RAG chunks
- **O quê:** Cada arquivo em `rag/` recebe cabeçalho:
  ```
  ---
  rag_chunks:
    - id: synthesis-score-structural
      status: SUPERSEDED
      effective_until: [data de Q-008 homologação]
      authority: GPR-001 (antigo) → Q-008 (novo)
      do_not_use_if: "conviction_vector_8d"
      successor_chunk: synthesis-conviction-8d
  
    - id: synthesis-conviction-8d
      status: ACTIVE_PILOT
      effective_from: DHR-EUA-E19a
      authority: ATOMIC-SPEC, Q-008, CCM-001
      open_decisions: [J-001 formula]
  ---
  ```
- **Efeito:** RAG retrieval sabe quais chunks usar; agente não herda obsolescências
- **Tempo:** 2–3 horas

#### TAREFA 6: Corrigir lint-specs.js
- **O quê:** Atualizar `tests/lint-specs.js` para:
  - ✅ Percorrer recursivamente `specs/features/SPEC-*`
  - ✅ Validar `plan.md` e `checks.md`
  - ✅ Ignorar ou marcar `GEN-1_REFERENCE`
  - ✅ Testar que `features/` são cobertas por CI
- **Teste:** `npm run lint` deve cobrir tanto `specs/*.spec.md` quanto `specs/features/*/plan.md`
- **Tempo:** 1–2 horas

---

### DIAS 6–7: DECISÕES ABERTAS + PLANO FINAL

#### TAREFA 7: Abrir Decisões Formais
- **O quê:** Criar `governance/DECISAO-ABERTA-XXX.md` para cada uma:
  - **GOV-ORCH-001:** Identidade de Orchestrator (Master/Decision/Cognitive/nenhum)
  - **FRACTAL-ARCH-001:** Fractal como agente, skill, dimensão ou futuro
  - **J-001-FINALIZE:** Fórmula/pesos do Conviction Vector (se sua resposta foi "piloto itinerário", registrar e datar)
  - **SCORE-09-DECISION:** Score 0–9 continuará ou será CCM-001 (se houve mudança de rumo)

- **Conteúdo mínimo de cada:**
  ```
  # Decisão: [nome]
  
  ## Contexto
  [Por que está aberta; qual Spec depende]
  
  ## Opções consideradas
  [A, B, C com prós/contras]
  
  ## Intenção original (per você)
  [Resposta do Questionário]
  
  ## Recomendação
  [baseado em auditorias]
  
  ## Próximos passos
  [Quando fecha; quem decide; artefatos afetados]
  ```

- **Gate:** Revisor lê proposta; Andraus decide
- **Tempo:** 1–2 horas (estrutura; conteúdo iterativo)

#### TAREFA 8: Gerar Relatório de Conformidade
- **O quê:** Documento final:
  ```
  ## Resolução (Sept 25–Oct 2)
  
  ✅ FECHADAS (com autoridade):
  - [Lista de decisões que ficaram fechadas]
  - [Emendas criadas]
  - [Tarefas de metadados]
  
  🔴 ABERTAS FORMALMENTE (para Andraus):
  - [Lista de DECISAO-ABERTA-XXX criadas]
  - [Sequência de homologação esperada]
  
  📊 IMPACTO:
  - Specs que herdam: [lista]
  - Bloqueadores removidos: [lista]
  - Risco residual: [baixo/médio]
  ```

- **Tempo:** 1 hora (compilar)

---

## MATRIZ DE RESPONSABILIDADES

| Tarefa | Responsável | Deadline | Bloqueado por | Bloqueia |
|---|---|---|---|---|
| **Responder Questionário** | **Você** | **Hoje** | — | Todas as tarefas abaixo |
| **Sistematizar decisões** | Claude (eu) | Amanhã | Questionário | Emendas |
| **1. GPR-001 emenda** | Especificador | 48h | Questionário | PAP/CIC, SPEC-002 |
| **2. CEM-001 status** | Especificador | 24h | Questionário | Continuidade canônica |
| **3. Sincronizar carimbos** | Controlador | 24h | — | Próxima DHR |
| **4. Marcar GEN-1** | Especificador | 3–5 dias | — | Lint, agentes |
| **5. Versionamento RAG** | Especificador | 3–5 dias | — | RAG retrieval, runtime |
| **6. Corrigir lint** | Tooling | 3–5 dias | — | CI coverage futuro |
| **7. Abrir decisões** | Especificador/Revisor | 5–7 dias | Questionário | Próximas Specs |
| **8. Relatório final** | Claude (eu) | 7 dias | Todas acima | Encerramento desta fase |

---

## GANHOS ESPERADOS AO FIM DE 7 DIAS

### Antes (estado atual — 25 set)
```
❌ CEM-001 status ambíguo → agente não sabe se é vinculante
❌ GPR-001 com Conviction 4D → próxima Spec herda norma obsoleta
❌ RAG chunks sem versionamento → runtime lê instrução antigo
❌ GEN-1 sem marcação → agente confunde referência com norma
❌ Lint não cobre features/ → SPEC-002 pode passar com gap
❌ Carimbos divergentes → Especificador/Revisor em versões diferentes
❌ Fractal não decidido → Elliott Spec bloqueada ou cria por inferência
❌ Master Orchestrator em Constituição → novo componente criado por analogia
```

### Depois (estado alinhado — 2 out)
```
✅ CEM-001 status unificado e referenciado
✅ GPR-001 emendado com Q-008/Q-009 vigentes; histórico preservado
✅ RAG chunks com `status`, `authority`, `supersedes` → retrieval limpo
✅ GEN-1 marcado `_REFERENCE`; agentes não confundem
✅ Lint recursivo cobrindo `specs/features/`
✅ Carimbos sincronizados: `.claude/agents/` operam com mesma versão
✅ Fractal decidido → Elliott Spec pode prosseguir
✅ Orchestrator formal decidido ou marcado UNRESOLVED → sem analogia perigosa
✅ 5–7 decisões formais abertas ou fechadas (rastreáveis em DHR)
```

### Impacto em Specs futuras
- **SPEC-002, SPEC-019, SPEC-020:** Herdam norma corrigida (não Conviction 4D)
- **SPEC-003 (Conviction Engine):** Sabe se J-001 está piloto ou fechado
- **Elliott/Fibonacci/Fractal Specs:** Sabem o status arquitetural de Fractal
- **SPEC-004 (Blackboard):** Sabe se Orchestrator é componente ou não
- **Risk-Specs:** Sabe que TMP é interno, Signal Package é fronteira

---

## RISCOS RESIDUAIS

| Risco | Mitigação | Aceitável? |
|---|---|---|
| Você não responde o Questionário | Usaremos ATOMIC-SPEC + ROADMAP como default | Sim, mas não ideal |
| Emendas ficam em "diferido incorporado" | Catálogo e DHR apontarão; agentes lerão DHR | Sim; temporário |
| Decisões ficam abertas | Ficarão EXPLICITAMENTE abertas (não implícitas) | Sim; necessário para E2E |
| Specs futuras ainda confundem termos | Glossário + tabela de aliases reduzem em 70% | Sim; restante viaja por Revisor |

---

## COMO VOCÊ PARTICIPA

### Opção 1: Entrevista Estruturada (Recomendado)
```
Você: Responde QUESTIONARIO-ENTREVISTA-RAPIDA.md (14 perguntas, ~15 min)
↓
Eu: Sistematizo em 5–7 decisões
↓
Você: Revê decisões, aprova ou itera
↓
Eu: Crio emendas + plano de execução
↓
Execução paralela (7 dias)
```

### Opção 2: Rápida (sem entrevista)
```
Eu: Executar tarefas 1–6 baseado em ATOMIC-SPEC + auditorias
↓
Você: Revê ao final; decide sobre decisões abertas
↓
Menos iteração, mas menor alineamento inicial
```

**Recomendação:** Opção 1 (15 min agora = 2–3 horas de alinhamento perfeito depois).

---

## PRÓXIMOS PASSOS

### Agora:
1. ✅ Você respondeu o QUESTIONARIO-ENTREVISTA-RAPIDA.md
2. ✅ Você leu DIAGNOSTICO-EXECUTIVO-DEPENDENCIAS.md
3. ✅ Você confirmou que aceita este plano

### Amanhã:
4. Eu compilo respostas em **DECISOES-SISTEMATIZADAS.md** (documento)
5. Compartilho para você revisar

### Dias 2–7:
6. Execução paralela das 8 tarefas conforme cronograma
7. Relatório final de conformidade

---

**Está pronto para começar?** Indique abaixo qual opção você escolhe e qualquer ajuste no cronograma.

---
