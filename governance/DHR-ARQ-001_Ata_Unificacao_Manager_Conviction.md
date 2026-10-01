# DHR-ARQ-001 — Ata de Unificação: Manager Agent absorve o Conviction Engine (propagação do ADR-MANAGER-001 / CEM-001 DIV-CEM-4)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Instrução direta de Andraus (chat, 2026-10-01): "Conviction Engine é taxonomia legada de arquitetura-para-código; UNIFICAR EM MANAGER" |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA por instrução direta de Andraus em chat; propaga ADR-MANAGER-001 (HOMOLOGADO 2026-09-26) / CEM-001 DIV-CEM-4 (BASELINED, DHR-TAX-001)** |
| Compatibilidade | Minor — não redefine modelo canônico baselined; consolida/propaga decisão já homologada. B-001 não é apagada (INV-07) |
| Autoridade-fonte | `governance/ADR-MANAGER-001_Manager_Agent_Architecture.md` §2.1/§2.3 (HOMOLOGADO); `canon/CEM-001-canonical-evidence-model.md` notas DIV-CEM-3/DIV-CEM-4 (BASELINED); `GLOSSARIO.md` §2-bis |

---

## 1. Problema (drift documental detectado)

O ADR-MANAGER-001 (HOMOLOGADO por Andraus, 2026-09-26) e as correções DIV-CEM-3/DIV-CEM-4 do CEM-001 (BASELINED, DHR-TAX-001, 2026-09-26) **já absorveram** o "Conviction Engine" e o "Agente de Síntese/Decisor" no **Manager Agent — Fase 2 (Conviction)**:

- `canon/CEM-001-canonical-evidence-model.md` l.183: *"Manager Agent (Fase 2: Conviction) — avaliação de força cognitiva. `DIV-CEM-4 (2026-09-26): 'Conviction Engine' eliminado; absorvido pelo Manager Agent Fase 2 — ADR-MANAGER-001`"*.
- `canon/CEM-001-...md` l.496: tabela de consumidores de estado — *"Manager Agent (Fase 2: Conviction) | Apenas ACTIVE | `DIV-CEM-4: era 'Conviction Engine'`"*.
- `canon/CEM-001-...md` l.679: CONSUMER autorizado — *"Manager Agent (Fase 2: Conviction) ... `'Conviction Engine' e 'Decision Orchestrator' absorvidos pelo Manager Agent`"*.
- `governance/ADR-MANAGER-001_...md` l.59: *"~~Agente de Síntese~~ → absorvido (Fase 2)"*; l.84-89: Fase 2 (Conviction) *"Lê Vetores de Convicção ... Forma Convicção Global ... Gera TMP"*.
- `GLOSSARIO.md` §2-bis l.55: *"`Conviction Engine` (motor separado) → Manager Agent (Fase 2: Conviction) — ADR-MANAGER-001 — Funcionalidade absorvida"*.

**Mas** a decisão **B-001** ("Conviction Engine SEPARADO do Synthesis", Questionário v1, 2026-09-14) permanecia escrita como FECHADA vigente, com a acepção de **componente/agente arquitetural independente**, em: `AGENTS.md` §7; `atomic-spec.md` (l.384); `.claude/agents/especificador.md` (l.316); `.claude/agents/revisor.md` (l.280/l.383); `.claude/skills/SKILL.md` (l.170/l.357/l.374); `ROADMAP.md` (título/descrição do slot SPEC-003, l.30/l.143-146, e linha de FECHADAS l.33); `GLOSSARIO.md` (l.30/l.88); e a **SPEC-003 candidata v1.1** adotou a acepção (a) "componente separado" (CONFLITO-1 / CC-10). Drift semântico entre baseline (ADR/CEM) e documentos operacionais/metodológicos.

## 2. Decisão (propagação — NÃO é nova norma de mérito)

1. **"Conviction Engine" deixa de designar entidade arquitetural independente.** Passa a ser **rótulo de MECANISMO** (legado/taxonomia de arquitetura-para-código) — Classe **D/H** do CCM-001 (SPEC-003) — **invocado pelo Manager Agent — Fase 2 (Conviction)**. Nenhuma Spec futura deve introduzi-lo como agente/componente separado (consistente com ADR-MANAGER-001 §2.1 "FATO NORMATIVO: nenhum destes nomes deve aparecer em specs futuras como componente independente").

2. **B-001 é parcialmente SUPERSEDIDA (INV-07 — não apagada).** B-001 (Q-007) continua **FECHADA** como registro histórico; fica **SUPERSEDIDA por ADR-MANAGER-001 NA PARTE "Conviction Engine como agente/componente separado"**. O texto de B-001 e o versionamento monotônico são preservados; nada é deletado.

3. **O que B-001 trazia de válido é PRESERVADO.** Permanece a **separação lógica de ETAPAS/MECANISMOS** (não de agentes):
   `Fusão (Evidência ACTIVE → DERIVED, CEM-001) → cálculo do Conviction Vector 8D → decisão/síntese`.
   Essas etapas agora são **mecanismos invocados pelo Manager Agent — Fase 2**, não agentes autônomos. O **Fusion Engine permanece** como engine determinístico (CEM-001, inalterado). A **dimensionalidade = 8** (Q-008) permanece FECHADA e intocada.

4. **Escopo do que NÃO é decidido aqui (CONS-01):** esta ata **não** fecha J-001 (fórmula/pesos/limiares definitivos), **não** fecha N-001 (pesos por ativo), **não** fecha `WF-D03`/`WORKFLOW-SOT-001` (reconciliação da leitura macro×global, nº de invocações 1x/2x, dimensão do regime Q-A9), **não** decide a fronteira SPEC-008 × SPEC-015 do Manager (matéria de proposta EUA-E23, Frente B), e **não** altera o `WORKFLOW.md` (soberano de Andraus).

## 3. Efeitos aplicados (propagação mínima e rastreável — Controlador, 2026-10-01)

| Arquivo | Mudança | Natureza |
|---|---|---|
| `AGENTS.md` §7 (linha FECHADAS) | B-001 anotada como "SUPERSEDIDA na parte componente-separado por ADR-MANAGER-001; DHR-ARQ-001" | Texto de decisão já-fechada (D1/D2-safe) |
| `atomic-spec.md` cabeçalho + l.384 (nota B-001) | Emenda DHR-ARQ-001 no cabeçalho; nota B-001 anotada (mecanismo invocado pelo Manager Fase 2) | Método/registro |
| `.claude/agents/especificador.md` l.316 + carimbo | Linha B-001 anotada; `sincronizado-até` += DHR-ARQ-001; SYNC-DATE 2026-10-01 | RPSA |
| `.claude/agents/revisor.md` l.280/l.383 + carimbo | Linhas B-001 anotadas; `sincronizado-até` += DHR-ARQ-001; SYNC-DATE 2026-10-01 | RPSA |
| `.claude/skills/SKILL.md` l.88/l.170/l.357/l.374 | B-001 deixa de ser tratada como pergunta aberta/CE-vs-SA; Conviction Engine = mecanismo (Manager Fase 2) | Skill (não-normativa) |
| `ROADMAP.md` l.30/l.33/l.143-146 | Título/descrição do slot SPEC-003 anotados; linha FECHADAS: B-001 → superseded-em-parte; slots NÃO renumerados | Direção/registro |
| `GLOSSARIO.md` §2/§3 (l.30/l.88) | Conviction Engine = mecanismo legado invocado pelo Manager Fase 2 (consistente com §2-bis l.55) | Terminologia |
| `governance/CATALOGO-OFICIAL.md` §7.3 | Linha DHR-ARQ-001 (REGISTRADO) | SSoT |
| `specs/features/SPEC-003/plan.md` | Delta **v1.2**: acepção CC-10 → mecanismo invocado pelo Manager Fase 2; CONFLITO-1 resolvido; BASpecs NÃO renumeradas; WF-D03 segue ABERTA | Spec candidata |
| `specs/features/SPEC-003/{checks,research}.md` | Notas de delta v1.2 (resolução CONFLITO-1/CC-10) | Spec candidata |
| `docs/MATRIZ-WORKFLOW-SPEC.md` | Conflito C-1 (acepção Conviction Engine) resolvido; "Manager" = ator único; C-2 remetido a esta ata | Matriz derivada (não-normativa) |

**Não tocado:** `WORKFLOW.md` (soberano de Andraus). Decisões abertas inalteradas (J-001, N-001, WF-D03, M-001 etc.).

## 4. Guardas de sincronização (detector `check_doc_sync.py`)

- **D1/D2:** B-001 **já era** decisão fechada; esta ata **não** a declara aberta nem flipa estado — apenas **anota** a supersedação parcial no próprio registro fechado. Nenhuma decisão aberta é fechada.
- **D6 (WORKFLOW.md):** nenhuma `WF-Dxx` aberta é declarada fechada; nenhum `WF-xx` inexistente é citado; `WORKFLOW.md` não é editado.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
