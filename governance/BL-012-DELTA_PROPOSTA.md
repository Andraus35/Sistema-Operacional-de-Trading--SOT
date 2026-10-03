# BL-012 (MC-COG-001) — Reavaliação do DELTA — [PROPOSTA]

| Campo | Valor |
|---|---|
| Documento | BL-012-DELTA_PROPOSTA |
| Tipo | **[PROPOSTA]** / reavaliação de item de backlog (NÃO-normativo; NÃO abre Spec; NÃO promove item; NÃO fecha decisão aberta; NÃO edita RMR-001/ROADMAP/CATALOGO) |
| Autor | Especificador Principal (Claude Code, Opus 4.8) |
| Data | 2026-10-03 |
| Mandato | Andraus (chat, 2026-10-03, **DHR-DEC-003**): "reavaliar só o delta" do BL-012 — schemas §6/§19 e integração §18; **REJEITAR** estados §7 que conflitam com CHM-001 |
| Base | `backlog/RMR-001_Painel_Backlog.md` (linha BL-012, `ATIVADO`); `governance/CLASSIFICACAO-COLISOES-BL010-011-012.md` §3 (COL-COG-01..05, **HOMOLOGADAS** DHR-BL010-011-012-001); `reference/camadas/MC-COG-001_Master_Contract_Camada_Cognicao.md` (ref. externa não-normativa) |
| Salvaguardas | CONS-01 (nenhuma decisão aberta fechada), CC-02/CONST-01 (nenhum canônico redefinido), INV-05 (cognição analisa, não decide/executa), INV-09 (status/ref. externa ≠ baseline), INV-07 (aditivo) |

> **Status epistemológico (TRACE-06).** O MC-COG-001 é **referência externa não-normativa** [FONTE: RMR-001 BL-012; CLASSIFICACAO-COLISOES §3]. As colisões COL-COG-01..05 já estão **homologadas** e inseridas no `CONFLICT-MAP.md`. Este documento **não** re-classifica aquilo que já foi homologado — apenas reavalia o **resíduo** (o "delta") que a classificação de 2026-09-28 havia **ADIADO à consolidação cognitiva**: os schemas §6/§19 e os contratos de integração §18. A conclusão é **[PROPOSTA]** — a decisão (Absorver / absorver parcialmente / voltar a Em espera) é de Andraus.

---

## 1. O que é o "delta" (recorte de Andraus)

[FONTE: DHR-DEC-003; RMR-001 BL-012 — coluna encaminhamento: "aproveitar §6/§18/§19 como schemas/contratos de fronteira"]

A classificação homologada (DHR-BL010-011-012-001) resolveu as **5 colisões de conteúdo/namespace**:

- **COL-COG-01 / R-05** — estados cognitivos **§7** → **REJEITAR**, usar CHM-001 (protege CC-02). *Confirmado aqui, sem reabertura.*
- **COL-COG-02 / R-01** — Quality Gates G0–G9 (§22) → REJEITAR global, gate LOCAL.
- **COL-COG-03 / R-02/03** — I-COG-01..12 (§21) / COG-P01..P15 (§4) → ADAPTAR como locais que referenciam N8–N17.
- **COL-COG-04 / R-06** — calibração/bayes/risco §15/§16 → **ADIAR** ao CCM-001 (J-001 aberto).
- **COL-COG-05 / X-01** — status "Baseline" (l.6) → REJEITAR efeito, ref. externa.

O que ficou **ADIADO** ("mapeamento: aproveitar §6/§18/§19 como schemas/contratos de fronteira") é exatamente o que Andraus mandou reavaliar agora. São **três blocos**:

- **§6** — *Unidade Cognitiva* (`cognitive_unit`, MC-COG l.171-197).
- **§19** — *Saída Cognitiva / Cognitive Output Contract* (COG-SPEC-055, MC-COG l.509-534).
- **§18** — *Integração* (COG-SPEC-050..054: Cognition-to-RAG / Experience / Learning / Governance / Skill-to-Cognition, MC-COG l.488-506).

---

## 2. Tabela item-a-item do delta

**Convenção da coluna "Tratamento":** **ADAPTAR** = admitir como elemento local/projeção que referencia o canônico, sem norma nova; **REJEITAR** = não adotar; **ADIAR** = reconciliar na ativação da Spec-dona. Prevalência sempre do **SOT canônico** (igual à classificação homologada).

### 2.1 — §6 Unidade Cognitiva (`cognitive_unit`) — MC-COG l.171-197

Cada campo do `cognitive_unit` é um *projeção* (CC-02) de objeto/regra já existente. Nenhum campo é conteúdo normativo novo.

| Campo (§6) | Já coberto por (arquivo:linha) | Lacuna real? | Tratamento | Spec dona / gatilho |
|---|---|---|---|---|
| `hypotheses`, `alternatives`, `contradictions` (entre hipóteses) | CHM-001 `hypothesis_id`/`hypothesis_type`/`parent_hypothesis_id`/`competing_hypothesis_ids` (`canon/CHM-001...md` l.283-317, l.403-415); **SPEC-001** (Hypothesis Harness, baseline) | Não — já normativo | **ADAPTAR** (projeção de CHM-001) | SPEC-001 (baseline) |
| `evidence`, `counterevidence` | CEM-001 Cap.3 `Observation`/`Interpretation`/`Technical Rationale`/`Evidence Strength`/`Lineage` (`canon/CEM-001...md` l.287-364); CHM-001 `supporting_evidence_ids`/`refuting_evidence_ids` (l.369-377); **SPEC-002** (Evidence & Provenance, baseline) | Não — já normativo | **ADAPTAR** (projeção de CEM-001/CHM-001) | SPEC-002 (baseline) |
| `observations` (distinta de `evidence`) | INV-06 Observação (Skill) ≠ Evidência (Agente); SPEC-004 CC-10 (`specs/features/SPEC-004/plan.md` l.60) | Não | **ADAPTAR** | SPEC-002/SPEC-004 |
| `facts`, `assumptions`, `inferences`, `relationships` | RULE-EPI-01/03 (`governance/RULES.md` l.660-662); CEM-001 Lineage/Knowledge Graph (l.351-364, l.562-606) | Não — status epistêmico já regido por RULE-EPI; relações = KG | **ADAPTAR** | SPEC-006 (KG/H-001) |
| `uncertainty` | RULE-UNC-01/02 localizar+não-contaminação (`governance/RULES.md` l.690-691) | Não | **ADAPTAR** | N14/baseline |
| `confidence` (calibração/valor numérico) | COL-COG-04 (calibração → CCM-001); **J-001 ABERTA** | Não é lacuna de BL-012 — é **J-001** | **ADIAR** | SPEC-003/CCM-001 · **J-001** |
| `conclusion`, `metacognitive_assessment`, `limitations` | RULE-MET-01 honestidade/não-fabricação/abstenção (N17); INV-05 (análise ≠ decisão) | Parcial — ver §2.2 (output) | **ADIAR → §19** | CDM-001/CNM-001 (ver §2.2) |
| `objective`, `question`, `context` (representação do problema) | RULE-INQ-01 classificar tipo de questão + método (`governance/RULES.md` l.675) | Parcial — RULE-INQ exige classificar a questão, mas **não** há objeto-contêiner "problem representation" (objetivo/contexto/restrições/incógnitas) especificado | **ADIAR** (ver pergunta Q2) | Consolidação cognitiva futura / Manager |
| `provenance` | CEM-001 `Source Reference`/`Lineage` (l.347-364); **SPEC-004** `computed_by`/`gate_record` + reconstrução por replay (`specs/features/SPEC-004/plan.md` l.39-41); TRACE-06 | Não | **ADAPTAR** | SPEC-002/SPEC-004 |
| `version` | Versionamento monotônico — CEM-001 (l.251, l.402-443), CHM-001 (`version`/`previous_version_id` l.283) | Não | **ADAPTAR** | canônicos (baseline) |
| `cognitive_unit_id` (contêiner agregador) | — (não existe objeto canônico "unidade cognitiva" agregadora) | **Lacuna potencial** — mas pode colidir com liberdade cognitiva (MC-COG §3) e com o objeto de working memory | **ADIAR** (ver pergunta Q1) | SPEC-004 (Blackboard) / consolidação cognitiva |

> [INFERÊNCIA] Dos 20 campos do `cognitive_unit`, **17 são projeção direta de canônico/regra já normativos** (ADAPTAR, sem norma nova), **1 é J-001** (`confidence`, ADIAR), e **2 tocam resíduo real** (`objective/question/context` como objeto de representação do problema; `cognitive_unit_id` como contêiner agregador) — ambos ADIADOS a pergunta de Andraus (Q1/Q2), não resolvidos aqui.

### 2.2 — §19 Saída Cognitiva / Cognitive Output Contract (COG-SPEC-055) — MC-COG l.509-534

O schema de saída repete os campos do §6 e acrescenta `interpretation`, `analysis` e `open_questions`. É o **produto analítico** da cognição — isto é, a **síntese** que o Manager Agent (Fase 2) produz e que, nos Modelos Canônicos, pertence ao **CDM-001 (Decisão)** e **CNM-001 (Narrativa)** — **ambos pendentes** (não baselined).

| Elemento (§19) | Já coberto por | Lacuna real? | Tratamento | Spec/modelo dono |
|---|---|---|---|---|
| `analysis`, `interpretation`, `conclusion` | CEM-001 `Interpretation` por evidência (l.307); **síntese do Manager Fase 2** (ADR-MANAGER-001) — **não especificada ainda**; CDM-001/CNM-001 **pendentes** | **Sim** — não há contrato de saída da síntese; pertence a CDM/CNM | **ADIAR** | **CDM-001 / CNM-001** (pendentes; não acionam CONST-01) |
| `open_questions` | RULE-INQ-03 encerramento → INDETERMINADO (`governance/RULES.md` l.677); RULE-UNC | Parcial — a *disciplina* existe; o *campo de saída* não | **ADIAR** | CDM-001/CNM-001 |
| `metacognitive_assessment`, `limitations` | RULE-MET-01 (N17) | Parcial (idem) | **ADIAR** | CDM-001/CNM-001 |
| demais campos (`hypotheses`/`evidence`/`uncertainty`/`provenance`/`version`...) | idem §6 (§2.1 acima) | Não | **ADAPTAR** | SPEC-001/002/003/004 |

> [INFERÊNCIA] O "Cognitive Output Contract" **não é lacuna do BL-012**: é o contrato de saída da síntese/decisão, que o roadmap já destina aos **modelos canônicos pendentes CDM-001 (Decisão) e CNM-001 (Narrativa)**. ADIAR a eles é o encaminhamento consistente — **não** criar um contrato de saída paralelo (risco futuro de CC-02 quando CDM/CNM forem redigidos).

### 2.3 — §18 Integração (COG-SPEC-050..054) — MC-COG l.488-506

Cada contrato de fronteira tem **dono já admitido no backlog** (os 6 Master Contracts). Nenhum é resíduo próprio do BL-012.

| Contrato (§18) | Invariante externo | Dono no backlog / SOT | Tratamento | Gatilho da Spec-dona |
|---|---|---|---|---|
| COG-SPEC-050 — Cognition-to-RAG ("pode pedir evidência, não altera proveniência", l.493) | = imutabilidade CEM-001 (l.402-428, l.646) + RULE-EPI | **BL-010** (MC-RAG-001) → SPEC-007 | **ADIAR** | `spec:SPEC-007` |
| COG-SPEC-051 — Cognition-to-Experience | memória histórica imutável | **BL-011** (MC-EXP-001) → SPEC-006/009 | **ADIAR** | `spec:SPEC-006/009` |
| COG-SPEC-052 — Cognition-to-Learning | erros/descobertas → candidatos de aprendizado | **BL-015** (MC-LRN-001; Learning propõe, Governance decide) | **ADIAR** | gatilho BL-015 |
| COG-SPEC-053 — Cognition-to-Governance ("resultados podem gerar propostas de mudança") | INV-09 (feedback/proposta ≠ baseline) | **BL-013** (MC-GOV-001) → SPEC-018 | **ADIAR** | `spec:SPEC-018` |
| COG-SPEC-054 — Skill-to-Cognition ("skill introduz domínio sem dominar cognição geral") | = RULE-PD/COG-P14/I-COG-10 (especialização não elimina geral) | **BL-016** (MC-SKL-001; **Skill≠agente DIFERIDO a SPEC-025**) | **ADIAR** | `spec:SPEC-025` |

> [FONTE: MEMORY.md — MC-RAG→BL-010/SPEC-007; MC-EXP→BL-011/SPEC-006/009; MC-GOV→BL-013/SPEC-018; MC-LRN→BL-015; MC-SKL→BL-016/SPEC-025.] [INFERÊNCIA] Toda a integração §18 já está **distribuída** aos donos corretos — o BL-012 não guarda resíduo de integração.

---

## 3. Conclusão e recomendação — [PROPOSTA]

**Resultado da reavaliação do delta:**

- **§6 (`cognitive_unit`):** 17/20 campos = **ADAPTAR** (projeção de canônico/regra já normativos — CEM/CHM/CCM + N8–N17); 1 = **J-001** (ADIAR); 2 = resíduo real levado a Andraus (Q1/Q2). **Nenhuma norma nova a especificar.**
- **§19 (Cognitive Output Contract):** **ADIAR** integralmente aos **modelos canônicos pendentes CDM-001 / CNM-001** (contrato de saída da síntese/decisão). Não é resíduo autônomo do BL-012.
- **§18 (Integração):** **ADIAR** — já **distribuída** aos donos BL-010/011/013/015/016 (SPEC-007/006/009/018/025). Não é resíduo autônomo do BL-012.
- **§7 (estados):** **REJEITADO** (confirmado — usar CHM-001, CC-02 protegido).

> [INFERÊNCIA] Após remover (a) o que já é normativo, (b) o que foi rejeitado e (c) o que pertence a outros donos com gatilho próprio, **o BL-012 não retém trabalho de especificação independente**. O seu valor residual é **documental**: servir de *checklist de cobertura cognitiva* (§31 Critério de Prontidão) a ser conferido quando CDM-001/CNM-001 e as Specs de integração forem redigidas.

### Recomendação: **ABSORVIDO** (parcialmente, com ponteiros) — preferencialmente **Absorvido**

[PROPOSTA] Recomendo marcar **BL-012 como `Absorvido`**, com a seguinte motivação registrada na ata (ato do Controlador/Andraus, não deste documento):

1. MC-COG-001 permanece **referência externa não-normativa** (COL-COG-05 / X-01) — nada vira baseline (INV-09).
2. Estados §7 **REJEITADOS** (COL-COG-01) — CHM-001 prevalece.
3. Schemas §6 = **projeção** já coberta por CEM-001/CHM-001/CCM-001 + SPEC-001/002/003/004 + N8–N17 — **ADAPTAR, sem norma nova**.
4. §19 (output) **ADIADO a CDM-001/CNM-001** (ponteiro, não resíduo do BL-012).
5. §18 (integração) **ADIADO/distribuído** a BL-010/011/013/015/016 (ponteiro, não resíduo do BL-012).
6. `confidence`/calibração permanecem em **J-001** (ABERTA).

**Por que "Absorvido" e não "voltar a Em espera":** não há condição futura própria que "destrave" o BL-012 — todo o conteúdo útil ou já é norma, ou foi rejeitado, ou foi herdado por outro item com gatilho próprio. Mantê-lo `Em espera`/`ATIVADO` criaria um item sem trabalho próprio (ruído de backlog). [INFERÊNCIA]

**Ressalva (por que "parcialmente"/com ponteiros e não absorção cega):** dois pontos do §6/§19 (**Q1** contêiner `cognitive_unit`; **Q2** objeto "representação do problema") são resíduos reais mas **menores e opcionais** — dependem de uma escolha de Andraus (abaixo). Se Andraus quiser que qualquer um deles vire trabalho de Spec, então o tratamento correto é **absorção parcial** com um ponteiro explícito para a Spec-dona (CDM/CNM ou consolidação cognitiva), em vez de `Absorvido` pleno.

**CONS-01:** nenhuma decisão aberta fechada — **J-001, N-001, M-001, H-001, G-001, WF-D03, K-001, I-001** permanecem **ABERTAS**. **CC-02:** nenhum canônico redefinido. **INV-05/INV-09:** preservados.

---

## 4. Perguntas a Andraus (linguagem de trader)

**Q1 — Vale a pena guardar um "dossiê único por análise"?**
O material externo sugere empacotar cada análise num único "dossiê" (hipóteses + evidências + incertezas + conclusão juntas, com um número de série). Hoje o SOT já guarda cada peça no lugar certo: a tese no registro de hipóteses, a prova na evidência, o placar de convicção no modelo de convicção, e tudo versionado no quadro de trabalho (Blackboard).
- **Recomendação:** **não criar** esse dossiê agora — ele duplicaria o que o Blackboard já junta por `trade`/ciclo, e engessaria a liberdade de análise. Deixar como está.
- Alternativa: se você quiser um "resumo de uma folha por operação" para leitura humana, isso entra como saída do Manager (síntese), não como nova estrutura de dados.

**Q2 — Fechar a "ficha do problema" antes de analisar?**
O material pede uma "ficha de abertura" (objetivo, contexto, restrições, o que não se sabe) antes de o sistema começar a pensar. Hoje a regra já obriga classificar o tipo de pergunta e o método (RULE-INQ), mas não existe uma ficha padronizada.
- **Recomendação:** **adiar** para quando formalizarmos a síntese/decisão (modelos CDM/CNM, ainda pendentes) — é lá que essa ficha faz sentido, não num item solto de backlog.

**Q3 — Pode arquivar o item BL-012?**
Reavaliado o que faltava (os schemas e os contratos de integração), **nada sobrou de trabalho exclusivo desse item**: ou já é regra, ou foi rejeitado (os estados que brigavam com o nosso ciclo de hipótese), ou já pertence a outros itens que têm gatilho próprio (RAG, Memória, Governança, Aprendizado, Skills).
- **Recomendação:** **marcar como "Absorvido"** — o documento externo continua como material de consulta, e deixamos ponteiros para onde cada pedaço será tratado no futuro. Só mantenha "em aberto" se você quiser que o Q1 ou o Q2 virem tarefa agora.

---

## 5. Comandos a rodar (não tenho Bash neste contexto)

Após a criação/edição deste `.md`, o mapa do projeto precisa ser reconciliado e a sincronização documental conferida:

```bash
python scripts/build_map.py            # regenera docs/mapa/ (BL-019) após novo .md em governance/
python scripts/build_map.py --check    # deve retornar "Mapa em dia"
python scripts/check_doc_sync.py        # confere drift (CONS-01, decisões abertas, enum de Estado do RMR-001)
```

> Observação: este documento **não** altera `RMR-001`, `ROADMAP.md` nem `CATALOGO-OFICIAL.md` — a mudança de Estado de BL-012 (para `Absorvido`) e o registro em ata são atos do **Controlador/Andraus**. Enquanto o Estado no painel não mudar, `check_doc_sync.py` não deve acusar drift por este arquivo (ele é `[PROPOSTA]`, não registro de Estado).

---

## 6. Notas de conformidade

- **[PROPOSTA]/reavaliação:** não abre Spec, não promove item, não aplica tratamento, não fecha decisão. A mudança de Estado e o registro em ata são de Andraus/Controlador.
- **CONS-01:** J-001, N-001, M-001, H-001, G-001, I-001, K-001, WF-D03, ECC-03-001 permanecem **abertas**.
- **CC-02/CONST-01:** nenhum canônico (CEM-001/CHM-001/CCM-001) redefinido; §7 rejeitado protege CHM-001.
- **INV-05:** cognição analisa; não decide nem executa. **INV-09:** MC-COG-001 e seus status = ref. externa, sem efeito de baseline. **INV-07:** aditivo — nada removido.
- Classificação homologada DHR-BL010-011-012-001 **não** reaberta; este documento trata apenas do resíduo ("delta") que aquela classificação havia ADIADO.
