# DHR-ARQ-002 — Ata de Unificação: Manager Agent absorve o Synthesis Agent (propagação do ADR-MANAGER-001 §2.1)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Instrução direta de Andraus (chat, 2026-10-01): "AGENTE MANAGER ABSORVE AGENTE SÍNTESE" |
| Data | 2026-10-01 |
| Status | **HOMOLOGADA por instrução direta de Andraus em chat; propaga ADR-MANAGER-001 (HOMOLOGADO 2026-09-26) §2.1 l.58-59 / §2.3 Fase 2** |
| Compatibilidade | Minor — não redefine modelo canônico baselined; consolida/propaga decisão já homologada no ADR. Nada é apagado (INV-07) |
| Autoridade-fonte | `governance/ADR-MANAGER-001_Manager_Agent_Architecture.md` §2.1 ("~~Agente de Síntese~~ → absorvido (Fase 2)"), §2.3 (Fase 2: Conviction — "Forma Convicção Global; Gera TMP"), §2.5; `GLOSSARIO.md` §2-bis l.56; `DHR-ARQ-001` (unificação Manager/Conviction, mesma família) |

---

## 1. Problema (drift documental detectado)

O **ADR-MANAGER-001** (HOMOLOGADO por Andraus, 2026-09-26) **já absorveu** o "Agente de Síntese" no **Manager Agent — Fase 2 (Conviction)**:

- `governance/ADR-MANAGER-001_...md` §2.1 l.59: *"~~Agente de Síntese~~ → absorvido (Fase 2)"*; **FATO NORMATIVO** (l.61): *"Nenhum destes nomes deve aparecer em specs futuras como componente independente."*
- §2.3 (Fase 2: Conviction): *"Lê Vetores de Convicção do Blackboard; Arbitra conflitos entre agentes; Forma Convicção Global; Gera Trading Mission Package (TMP)"* — que é exatamente a função do antigo Synthesis Agent (árbitro final → TMP).
- `GLOSSARIO.md` §2-bis l.56: *"`Synthesis Agent` (árbitro LLM) → Manager Agent (Fase 2: Conviction) — ADR-MANAGER-001 — ... será substituído pelo Manager Agent conforme SPEC-015."*
- `governance/DHR-ADR-HOC003_...md` já registra que o ADR-MANAGER-001 "elimina ... Agente de Síntese".

**Mas** o Synthesis Agent permanecia escrito como **agente autônomo vigente** em: `ROADMAP.md` (slot **SPEC-014 — Synthesis Agent**, FASE 6, §9/§21/§26); `GLOSSARIO.md` (§2 tabela l.31 "Synthesis Agent (mantido)"; §3 definição l.89 "Árbitro final (LLM)"); `docs/MATRIZ-WORKFLOW-SPEC.md` (WF-06 "Spec dona primária SPEC-014 (Synthesis Agent)"). Drift semântico entre o baseline (ADR) e os documentos operacionais/direção.

**Instrução de Andraus (2026-10-01):** "AGENTE MANAGER ABSORVE AGENTE SÍNTESE" — propagar o fato já homologado no ADR para os documentos vivos.

## 2. Decisão (propagação — NÃO é nova norma de mérito)

1. **O "Synthesis Agent" deixa de designar agente autônomo.** Suas responsabilidades (arbitragem final de convicções; `Evidence→Hypothesis→Conviction→Decision→Mission/TMP`; geração do TMP interno) são **a Fase 2 (Conviction/Síntese) do Manager Agent** (ADR §2.3). Nenhuma Spec futura deve introduzi-lo como agente/componente separado (ADR §2.1 FATO NORMATIVO).

2. **Preservação de escopo (nada se perde).** O escopo do antigo slot **SPEC-014 (Synthesis Agent)** é **migrado** para a **Fase 2 do Manager**. Destino item-a-item:

   | Escopo do antigo SPEC-014 (ROADMAP §9) | Destino |
   |---|---|
   | Arbitragem/síntese dos outputs analíticos (árbitro final) | **Manager — Fase 2 (Convicção & Síntese)** |
   | Cadeia `Conviction → Decision → Mission / TMP` | **Manager — Fase 2** (decisão de síntese) + **Fase 0** (Mission Lifecycle) |
   | Cálculo do Conviction Vector / Global Conviction | **mecanismo da SPEC-003/CCM-001** invocado pela Fase 2 (DHR-ARQ-001) — não reescrito |
   | Contrato do objeto TMP (snapshot imutável, handoff interno) | **SPEC-016** (já repurposada — ROADMAP §9; EUA-E19a) |
   | Fechamento da lente `decision traceability` da SPEC-020 | permanece — fecha na **Spec do Manager-Fase-2** (SPEC-014 repurposado), não num "Synthesis" autônomo |

   O **número do slot SPEC-014 NÃO é renumerado nem apagado** (INV-07): é **repurposado** como a Spec "Manager — Convicção & Síntese" que a **EUA-E23** (Frente 2) venha a definir na abertura (RULE-ECC-01). A decomposição final (2 ou 3 Specs do Manager) é decisão de Andraus via EUA-E23 — **não fechada aqui**.

3. **Escopo do que NÃO é decidido aqui (CONS-01):** esta ata **não** fecha SPEC-015-SCOPE, **não** decide a quantidade de Specs do Manager (2 vs 3 — matéria da EUA-E23), **não** fecha J-001/N-001/M-001/WF-D03, **não** renumera slots e **não** edita o `WORKFLOW.md` (soberano de Andraus). O TMP permanece artefato **interno** (EUA-E19a); o **Signal Package** segue sendo o artefato de fronteira (INV-05 — SOT não executa).

## 3. Efeitos aplicados (propagação mínima e rastreável — Controlador, 2026-10-01)

| Arquivo | Mudança | Natureza |
|---|---|---|
| `ROADMAP.md` §9 (slot SPEC-014) | Slot anotado: "Synthesis Agent **ABSORVIDO pelo Manager — Fase 2 (Convicção & Síntese)**; escopo migra para a Spec do Manager que a EUA-E23 definir; slot NÃO renumerado" | Direção/registro |
| `ROADMAP.md` §21 (caminho crítico) e §26 (tabela de capacidades) | Nota de absorção no ponto "014 Synthesis"; capacidade preservada (não descartada) | Direção/registro |
| `GLOSSARIO.md` §2 (l.31) e §3 (l.89) | Linha/definição "Synthesis Agent" anotadas: agora **Fase 2 do Manager** (não agente autônomo); consistente com §2-bis l.56 | Terminologia |
| `GLOSSARIO.md` §2-bis (l.56) | Referência "conforme SPEC-015" precisada: destino = **Fase 2 do Manager**, Spec definida pela EUA-E23 (SPEC-014 repurposado) | Terminologia |
| `AGENTS.md` §6 item 9 | Parêntese: "a Síntese = Manager — Fase 2 (Convicção & Síntese); DHR-ARQ-002" | Operacional (não-baselined) |
| `.claude/agents/especificador.md` + carimbo | `sincronizado-até` += DHR-ARQ-002; SYNC-DATE 2026-10-01; linha de nota | RPSA |
| `.claude/agents/revisor.md` + carimbo | `sincronizado-até` += DHR-ARQ-002; SYNC-DATE 2026-10-01; linha de nota | RPSA |
| `governance/CATALOGO-OFICIAL.md` §7.3 | Linha DHR-ARQ-002 (REGISTRADO) | SSoT |
| `docs/MATRIZ-WORKFLOW-SPEC.md` | WF-06: "Spec dona" = Manager — Fase 2 (SPEC-014 repurposado, absorve Synthesis); nota de absorção | Matriz derivada (não-normativa) |

**Não tocado (baselined / soberano):**
- `canon/CEM-001-...md` — **já** usa "Manager Agent (Fase 2: Conviction)" nas tabelas de produtor/consumidor (DIV-CEM-3/DIV-CEM-4); **não menciona** "Synthesis Agent" como componente → **nenhuma edição nem DIV necessária** (verificado: grep de "Synthesis/Síntese" em `canon/` só retorna CEE-001 l.107, uso genérico de "Síntese e julgamento", não o agente).
- `specs/*.spec.md` (harness de 1ª geração — `synthesis.spec.md`, `elliott-wave.spec.md` etc.), `schemas/synthesis.*.json`, `rag/synthesis.knowledge.md` — artefatos **GEN-1** (harness de 5 agentes, superseded como referência; ROADMAP §2). **Listados, não editados** nesta ata: pertencem à camada de referência histórica/1ª geração, não ao texto normativo vivo; sua reconciliação, se desejada, é trabalho separado (candidato a RPIR/HOD-001, não propagação de decisão).
- `WORKFLOW.md` — soberano de Andraus (WF-06 fala de "Manager" formando convicção global, já consistente com esta ata).

## 4. Guardas de sincronização (detector `check_doc_sync.py`)

- **D1/D2:** nenhuma decisão aberta é fechada nem flipada. B-001 segue FECHADA (DHR-ARQ-001). SPEC-015-SCOPE segue ABERTA. A quantidade de Specs do Manager permanece matéria **aberta** da EUA-E23 (não decidida aqui).
- **D6 (WORKFLOW.md):** nenhuma `WF-Dxx` aberta é declarada fechada; nenhum `WF-xx` inexistente é citado; `WORKFLOW.md` não é editado.
- **Slots:** SPEC-014 **repurposado, não renumerado nem apagado** (INV-07).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
