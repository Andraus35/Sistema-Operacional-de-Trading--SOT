# ERRATUM-SPEC020-002 — Dimensão B "RAG faithfulness", metade F1 (fidelidade do conhecimento formado) — erratum ADITIVO (PROPOSTA)

| Campo | Valor |
|---|---|
| Código | **ERRATUM-SPEC020-002** — número **proposto**; a atribuição final é de Andraus na homologação (Q-6). |
| Versão | v1.0 (2026-10-30) — primeira entrega. |
| Spec afetada | SPEC-020 — Harness Evaluation Specification (núcleo A), **HOMOLOGADA — BASELINE** (DHR-SPEC020-001) + ERRATUM-SPEC020-001 (DHR-SPEC038-002). **Este erratum NÃO edita texto baselined** (INV-07/INV-09): `specs/features/SPEC-020/plan.md` e `specs/features/SPEC-020/checks.md` ficam como estão. |
| Natureza | **PROPOSTA de erratum aditivo.** Aguarda o Revisor e a homologação de Andraus. Não é baseline. Nada nele vale antes da homologação (RULE-HG-01/02/03). |
| Ordem | Ordem de Andraus transmitida pelo Orquestrador (chat, 2026-10-30: "Emenda da SPEC-020"), em execução da DHR-RETRO-001 §1 ("Próxima frente", item (2): "emenda à SPEC-020 (metade F1; F2 vai com a SPEC-048)") e §2 ("Uma de cada vez, nesta ordem, cada uma com Revisor e homologação própria de Andraus. Nenhum baseline é editado antes da homologação da respectiva errata"). A errata da SPEC-006, item (1), já foi homologada (DHR-SPEC006-005). `[FONTE — FATO NORMATIVO: DHR-RETRO-001; a ordem de 2026-10-30 ainda não está registrada em ata — registro do Orquestrador]` |
| Origem do conteúdo | `specs/features/SPEC-007/plan.md` v2.3 (BASELINE, DHR-SPEC007-005), seção "Proposta de emenda pontual à SPEC-020 (dimensão B \"RAG faithfulness\") — metade F1"; RULE-KFH-005; RULE-KFH-006; INV-KFH-01; BASpec-KFH-005/006; EC-KFH-003; Cenário-KFH-T06..T09; ADV-KFH-03/04/05/13/24. Atas: DHR-SPEC007-001 Q5; DHR-SPEC007-002 §3/§4; DHR-SPEC007-003 P-5; DHR-SPEC007-005 H-3; DHR-SPEC048-001 (condição m-10); DHR-SPEC048-002 §3. `[FONTE]` |
| Âncoras | **Por ID + texto literal entre aspas, nunca por número de linha** (prática P2 em vigor; P3 ainda a especificar — DHR-RETRO-001 §1). Números de linha, quando aparecem entre parênteses, só ajudam a achar o trecho. |
| Complexidade | CRITICAL (a da SPEC-020; não muda) · D0–D8 focado no que o erratum toca · profile standard + adversarial. |
| Compatibilidade proposta | **Minor** (recomendação; decisão de Andraus — Q-3). Justificativa na seção 8. `[PROPOSTA]` |
| Status epistemológico | `[FONTE]` = conferido nos arquivos citados; `[INFERÊNCIA]` = leitura do Especificador, a conferir pelo Revisor; `[PROPOSTA]` = o que se pede a Andraus; `[DECISÃO NECESSÁRIA]` = lacuna que o Especificador não resolve. |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Data | 2026-10-30 |

---

## 0. O que este erratum faz, em uma frase

A SPEC-020 deixou a dimensão B "RAG faithfulness" **DIFERIDA** até o componente-alvo existir. A divisão da SPEC-007 partiu essa dimensão em duas metades: **F1** (o conhecimento formado não inventa o que a fonte não diz — SPEC-007) e **F2** (cada frase entregue tem apoio no trecho citado — SPEC-048) (DHR-SPEC007-002 §4; DHR-SPEC007-003 P-5). A SPEC-007 já está homologada. Este erratum diz **como a metade F1 passa a ser verificada**: pela **conformidade a F1 da SPEC-007** (RULE-KFH-005 primeiro, RULE-KFH-006 depois), com **limiares INDETERMINADO** até calibração com amostra. `[FONTE: DHR-SPEC007-001 Q5; DHR-SPEC007-003 P-5; SPEC-007 plan.md, seção "Proposta de emenda pontual à SPEC-020 … metade F1"]`

**Não faz:** não trata da metade F2 (fica para um erratum à parte, da SPEC-048). Não mexe em *decision traceability* (segue DIFERIDA, SPEC-014). Não fecha a dimensão "RAG faithfulness" inteira. Não fecha o BL-017. Não fecha nenhuma decisão aberta. Não cria lente nova, RULE, BASpec, EC, cenário nem ADV. Não muda o enum `lente` do schema lógico da SPEC-020. Não fixa número. Não edita o plan.md da SPEC-020, da SPEC-007 nem da SPEC-048. `[FONTE: DHR-RETRO-001 §2-§3; DHR-SPEC007-005 H-3; DHR-SPEC048-002 §3]`

---

## 1. Texto do erratum `[PROPOSTA]`

> **ERRATUM-SPEC020-002 — dimensão B "RAG faithfulness", metade F1 (conhecimento formado).**
>
> **1.1 Critério.** Na dimensão B **"RAG faithfulness"** da SPEC-020 (classe dependente-de-upstream; Non-goal "Dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability)"), a parte que trata da **fidelidade do conhecimento formado** (metade **F1**) passa a ter **critério verificável definido**: a **conformidade a F1 da SPEC-007** (BASELINE v2.3, DHR-SPEC007-005) — **RULE-KFH-005** ("VALIDAÇÃO F1 — parte DETERMINÍSTICA (roda ANTES de qualquer juízo por modelo)") e **RULE-KFH-006** ("VALIDAÇÃO F1 — JUÍZO (Classe H), só após RULE-KFH-005 passar"), nesta ordem.
>
> **1.2 O que se confere em tempo de Spec (spec-time — escopo da SPEC-020).** Uma Spec cujo escopo inclua **formar conhecimento a partir de fonte com destino à memória permanente**, ou **mudar esse caminho**, satisfaz a metade F1 se — e só se — mantiver, sem enfraquecer:
> 1. **Parte determinística antes do juízo:** citação resolve, trecho existe, literais preservados ("números, sinais, unidades, percentuais e marcadores de negação"), cobertura e tipo — falha ⇒ `KC_REPROVADO`, sem chamar juiz (RULE-KFH-005; BASpec-KFH-005; Cenário-KFH-T06/T07; ADV-KFH-05).
> 2. **Juízo por modelo independente:** `judge_model_id ≠ former_model_id`, IDs gravados pela CIM, juiz em ponto separado e sem escrita; "mesmo modelo em contexto novo NÃO é independente" (RULE-KFH-006; Cenário-KFH-T09; ADV-KFH-04/24).
> 3. **VALIDADO só pela expressão única da RULE-KFH-006** ("repetida com as MESMAS seis conjunções"), com a precedência da regra ("qualquer FALHA ⇒ `KC_REPROVADO` (prevalece); senão, qualquer INDETERMINADO ⇒ `KC_INDETERMINADO` (não sela)") (RULE-KFH-006; BASpec-KFH-006 GATE DE SAÍDA; EC-KFH-003 PRECOND).
> 4. **O juízo nunca é o gate final:** "Conformidade > Eficácia — o juízo nunca é o gate final" (BASpec-KFH-006, CRITÉRIO 4Es).
> 5. **Sem caminho que contorne F1:** "Nada chega ao KG pelo caminho (b) da RULE-CKG-010 sem SELO válido … o selo exige registro de validação com resultado VALIDADO" (INV-KFH-01; ADV-KFH-01).
> 6. **Limiares INDETERMINADO:** "Limiares/métricas agregadas de fidelidade = INDETERMINADO até calibração com amostra (nenhum número externo importado)" (RULE-KFH-006; ADV-KFH-13 `EXTERNAL_THRESHOLD_IMPORTED`).
>
> Uma Spec que só **consome** conhecimento carimbado (ex.: SPEC-006, SPEC-048) é conferida aqui apenas no item 5 (não cria caminho que contorne F1); a fidelidade do que ela **entrega** é matéria da metade F2, fora deste erratum. Uma Spec que não toca conhecimento formado registra a metade F1 como **não aplicável, com justificativa** (como os N/A do Constitution Check) — não aplicável ≠ PASS. O resultado da conferência usa os estados do D5 da SPEC-020 (`NOT_EVALUATED | DETECTED | PASS | FAIL | INDETERMINADO | REGRESSED`) e é registrado no `checks.md` da Spec avaliada. **O enum `lente` do schema lógico não muda** (a metade F1 não é uma 10ª lente).
>
> **1.3 O que vale em tempo de execução (runtime) — sem antecipar tooling.** A prova de fidelidade de **cada** item publicado é o `validation_record` com resultado VALIDADO, ligado ao `material_hash` e ao selo (EC-KFH-003/EC-KFH-004), reconstruível. **Métricas agregadas** (taxas, limiares, amostragem) = **INDETERMINADO até calibração com amostra**; nenhum número é fixado por este erratum (R-5 da SPEC-007; CC-09). O tooling de avaliação em runtime segue fora da SPEC-020 (Non-goal "Tooling de avaliação de **runtime**"; SPEC-045-RUNTIME-001 segue ABERTA).
>
> **1.4 Limite declarado (RULE-MET-01).** F1 mede se o conhecimento formado **se apoia na fonte citada** — não mede se a fonte é verdadeira, nem relevância. IDs de modelo diferentes provam independência de **identidade**, não de **erro** (RULE-KFH-006, "LIMITE (RULE-MET-01)"). Se o juiz independente também for enganado, a afirmação passa — risco residual RU-1 da SPEC-007 (ADV-KFH-03, "eficácia = INDETERMINADA até calibração"). Conformidade a F1 é o **critério de verificação**; não é garantia de fidelidade.
>
> **1.5 Compatibilidade com as regras de avaliação da SPEC-020.** RULE-EV-02 ("O LLM NUNCA é o gate de aprovação de uma Spec") e RULE-EV-03 seguem intactas: em spec-time, a conferência dos itens 1–6 é do gate determinístico/Revisor, nunca de um LLM; em runtime, o juiz F1 é etapa de Classe H cujo resultado passa pelo gate determinístico da RULE-KFH-006 (item 4). RULE-EV-05: F1 não tem campo de convicção nem limiar de convicção. RULE-EV-07: as fontes externas da SPEC-007 (research §2 — SRC-RAGAS-01, SRC-FAITHJUDGE-01, SRC-ALCE-01) seguem DADO, nunca baseline.
>
> **1.6 Estado das dimensões B depois deste erratum.**
> - **RAG faithfulness — metade F1:** critério verificável definido (acima); limiares INDETERMINADO.
> - **RAG faithfulness — metade F2:** segue **DIFERIDA** até a homologação do erratum à parte da metade F2 (SPEC-048 — DHR-SPEC048-002 §3).
> - **A dimensão "RAG faithfulness" como um todo** só deixa de ser diferida quando as duas metades tiverem critério homologado.
> - **tool correctness:** FECHADA (ERRATUM-SPEC020-001) — não muda.
> - **decision traceability:** segue **DIFERIDA** (SPEC-014) — não muda.
> - **ADV-EV-06 (`CLASS_B_PREMATURE`)** continua valendo para a metade F2 e para *decision traceability*. Para a metade F1, a condição dele ("antes do componente-alvo") deixou de existir: o componente-alvo (SPEC-007) foi homologado (DHR-SPEC007-005).
>
> Texto da SPEC-020 não alterado (INV-09).

---

## 2. Leitura vigente dos enunciados da SPEC-020 (sem editá-los) `[PROPOSTA]`

Os enunciados abaixo continuam no baseline como estão. Depois da homologação, leem-se assim:

| Âncora (SPEC-020, por texto) | Enunciado original (resumo) | Leitura vigente |
|---|---|---|
| D0, "O que a Missão NÃO é": "Não fecha as dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability) → **SPEC-007/038/014 (BL-017)**" | A SPEC-020 não fecha a classe B | **Continua verdadeiro**: a SPEC-020 não fechou nada sozinha; a metade F1 passa a ter critério pelo erratum, na forma que o próprio texto previa |
| D1, Non-goals: "Dimensões **classe B** … DIFERIDAS por EUA-E17 + BL-017; não fechadas antes do componente-alvo (CONS-01)" | RAG faithfulness diferida | F1: critério definido (componente-alvo SPEC-007 homologado). F2: segue DIFERIDA (SPEC-048). *decision traceability*: DIFERIDA |
| ADV-EV-06: "rejeitar `CLASS_B_PREMATURE`; classe B permanece DIFERIDA (SPEC-007/038/014; BL-017)" | Rejeitar fechamento prematuro | Continua valendo para F2 e *decision traceability*; para F1 a condição "antes do componente-alvo" não existe mais |
| Riscos: "Classe B tratada como fechada \| Non-goal explícito; ADV-EV-06; BL-017 intocado" | Salvaguarda | Continua valendo; "BL-017 intocado" lê-se: estado do BL-017 não muda por este erratum (só Andraus promove) |
| Etiquetagem: "Classe B (RAG faithfulness/tool correctness/decision traceability) \| [FONTE] \| DIFERIDA (BL-017) — não fechada" | Status | F1: critério definido (este erratum); F2 e *decision traceability*: DIFERIDAS |
| Lista final "[DECISÃO NECESSÁRIA] em aberto": "**Classe B** … — DIFERIDA (BL-017); fecha em SPEC-007/038/014" | Aberta | "fecha em SPEC-007" lê-se: **metade F1** (este erratum); metade F2 → SPEC-048 (DHR-SPEC007-002 §4) |
| Errata aditiva ao fim do plan.md: "RAG faithfulness (SPEC-007) e decision traceability (SPEC-014) permanecem diferidas" | Diferidas | F1: critério definido; F2: DIFERIDA (SPEC-048); *decision traceability*: DIFERIDA |

**Registros de estágio preservados (não são erros; descrevem o estado à data da entrega):** "Nota de gate" ("BL-017 … permanece `Proposto`"); §7-bis Bloco D ("classe B marcados [DECISÃO NECESSÁRIA]/DIFERIDO"); Autopré-check ("classe B DIFERIDA"); `checks.md` ("Classe B DIFERIDA (BL-017); não fechada (ADV-EV-06)"); `research.md` (GAP-3, Q-A5). Este erratum não os corrige. `[INFERÊNCIA — mesmo critério do ERRATUM-SPEC019-001 §1, "Registros de estágio preservados"]`

---

## 3. Coordenação com a metade F2 (DHR-SPEC048-001, condição m-10) `[FONTE + PROPOSTA]`

**Fronteira.** F1 = fidelidade do **conhecimento formado** à fonte (SPEC-007: RULE-KFH-005/006). F2 = suporte de **cada item/frase entregue** no trecho que cita (SPEC-048: RULE-RET-009/010/011). A SPEC-048 já define, no "Termo 4": "suporte de cada coisa entregue no trecho que ela cita (frase entregue × trecho) ≠ \"F1\" (fidelidade do conhecimento formado — SPEC-007)" e "F2 mede **suporte**, não **dependência** nem **verdade**" (SPEC-048 plan.md). Nada deste erratum fala de frase entregue, pacote ou síntese. `[FONTE: DHR-SPEC007-002 §3; SPEC-048 plan.md "Termo 4"]`

**Texto único por linha (proposto pela SPEC-048).** O Plan da SPEC-048 (seção "Texto único por linha da SPEC-020 — coordenado com a metade F1") propôs uma nota igual para as duas metades e disse que a metade F1 "pode usar este texto sem alteração". Este erratum **adota o conteúdo** dessa nota, com **um ajuste**:

- **Divergência registrada.** A nota diz "F2: na homologação do Plan da SPEC-048". Isso não aconteceu: a DHR-SPEC048-002 §3 registra: "**Não aplicados nesta ata** (passos à parte, por ordem expressa de Andraus): errata aditiva à SPEC-006 (E-1..E-4); emenda de fidelidade F2 à SPEC-020; …". Por isso a seção 1.6 diz "F2: DIFERIDA até a homologação do erratum à parte da metade F2 (DHR-SPEC048-002 §3)". O texto da SPEC-048 (baseline) **não é editado** aqui. Proposta: o erratum da metade F2 usa a mesma redação ajustada (Q-5). `[FONTE: DHR-SPEC048-002 §3; INFERÊNCIA quanto ao ajuste]`
- **Nada se contradiz** entre a seção 1 deste erratum e a "Proposta de emenda pontual à SPEC-020 … metade F2" da SPEC-048: as duas usam "limiares INDETERMINADO até calibração com amostra", mantêm *decision traceability* com a SPEC-014 e não editam a SPEC-020. `[INFERÊNCIA — conferido lendo as duas seções]`
- **Nota sobre o ERRATUM-SPEC020-001.** A frase dele "**RAG faithfulness ↔ SPEC-007** … permanecem **DIFERIDAS**" (seção "O que NÃO muda") **não é editada** (homologado; INV-09). Leitura vigente: "a dimensão 'RAG faithfulness' divide-se em F1 (SPEC-007) e F2 (SPEC-048); a metade F1 tem critério por este erratum; a metade F2 segue diferida até a homologação do seu erratum". Mesmo texto que a SPEC-048 propôs para essa linha, com o ajuste acima. `[FONTE: SPEC-048 plan.md, linha da tabela de re-apontamento sobre `governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md`]`

**Lacuna registrada (não resolvida).** Para F2 existe auditoria amostral de falso-ACEITE do juiz (SPEC-048, RULE-RET-011). Para F1, a SPEC-007 **não** traz auditoria amostral de falso-CLEAR do juiz F1: há só o risco residual RU-1 ("eficácia = INDETERMINADA até calibração") e a auditoria amostral do `record_hash` (EC-KFH-004), que confere identidade, não qualidade. Logo, "calibração com amostra" da metade F1 **não tem dono nem método definidos**. Este erratum não cria um (seria regra nova na SPEC-007). `[DECISÃO NECESSÁRIA — Q-7]`

---

## 4. O que NÃO muda (CONS-01)

- **BL-017** segue com **Disposição PARCIAL** (SPEC-007 plan.md v2.3, nota de gate: "**Disposição: PARCIAL** — motivo: a dimensão **RAG faithfulness** divide-se (DHR-SPEC007-002 §4; DHR-SPEC007-003 P-5): **F1 aqui** (RULE-KFH-005/006 — fidelidade do conhecimento formado; limiares INDETERMINADO), fechando a metade F1 por emenda pontual à SPEC-020 …; **F2 na SPEC-048** …"; *decision traceability* com a SPEC-014). Estado no painel **inalterado** (`Em espera`); só Andraus promove ou encerra (RMR-001 §5). O BL-017 **não fecha** por este erratum: restam a metade F2 e *decision traceability*. `[FONTE: RMR-001 BL-017; SPEC-007 plan.md "Nota de gate"]`
- Nenhuma lente, RULE-EV, BASpec-EV, EC-EV, cenário, ADV ou schema da SPEC-020 é alterado. O núcleo A e a 9ª lente seguem como homologados.
- Nenhuma regra da SPEC-007 é alterada; RULE-KFH-005/006 são **usadas por referência**.
- **Permanecem ABERTAS** (nenhuma fechada por este erratum): K-001 · J-001 · M-001 · N-001 · G-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · SPEC-020-PRINC-001 (nos termos da ordem de serviço desta tarefa e da linha "Decisões abertas ativas" do AGENTS.md §7; o ROADMAP prevalece em divergência — ver nota). Também abertos: "produtor/gatilho de promoção" e o mecanismo de assinatura dos atos de Andraus (BUILD). `[FONTE: DHR-RETRO-001 §3; DHR-SPEC048-002 §5; DHR-SPEC006-005 §4]`
  - *Nota de divergência (registrada, não resolvida):* a linha "Decisões FECHADAS" do `ROADMAP.md` lista "**SPEC-020-PRINC-001 — FECHADA (SPEC-020 homologada, 2026-09-27, DHR-SPEC020-001)**", enquanto o AGENTS.md §7 e a ordem de serviço a listam como aberta. Este erratum **não toca** SPEC-020-PRINC-001 em nenhum dos dois sentidos. `[FONTE: ROADMAP.md "Decisões FECHADAS"; AGENTS.md §7 — DECISÃO NECESSÁRIA de saneamento, fora deste erratum]`
- **Linha de montagem da SPEC-007 segue parada** até as liberações de Andraus (DHR-SPEC007-005 §3). Este erratum define critério; não libera nada.

---

## 5. Herança/Delta (CC-08; RULE-HD-02/03/04)

- **INHERITS** (ID + versão): SPEC-020 v1.0 (BASELINE, DHR-SPEC020-001): RULE-EV-01/02/03/05/07; D5 (estados e invariante "o estado nunca transita de DETECTED direto a PASS/FAIL **por juízo do LLM**"); Non-goals (classe B; limiar de convicção; tooling de runtime); ADV-EV-06; schema lógico "Resultado de avaliação de lente". ERRATUM-SPEC020-001 (DHR-SPEC038-002): padrão de forma; *tool correctness* FECHADA. SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005): RULE-KFH-005; RULE-KFH-006; INV-KFH-01; BASpec-KFH-005/006; EC-KFH-003; ADV-KFH-03/04/05/13/24; Cenário-KFH-T06..T09. SPEC-048 v1.4 (BASELINE, DHR-SPEC048-002): "Termo 4" (fronteira F1×F2).
- **ADDED:** critério verificável da metade F1 (seção 1); leitura vigente (seção 2); nota de coordenação F1×F2 (seção 3).
- **MODIFIED:** nenhum texto. O estado da metade F1 passa de "DIFERIDA" a "critério definido" **pela condição que o próprio baseline já escreveu** ("fecha em SPEC-007"; ADV-EV-06 "antes do componente-alvo"). É realização de condição prevista, não mudança de regra. `[INFERÊNCIA — a conferir pelo Revisor]`
- **REMOVED:** vazio.

**Evidência obrigação a obrigação (§7-bis Bloco B):**

| Obrigação herdada | Onde este erratum a cumpre |
|---|---|
| SPEC-020 Non-goal: classe B "não fechadas antes do componente-alvo (CONS-01)" | Só a metade F1, cujo componente-alvo (SPEC-007) está homologado; F2 e *decision traceability* seguem DIFERIDAS (1.6) |
| ADV-EV-06: rejeitar `CLASS_B_PREMATURE` | 1.6 mantém a rejeição para F2 e *decision traceability*; a dimensão inteira não é fechada |
| RULE-EV-02: "O LLM NUNCA é o gate de aprovação de uma Spec" | 1.2 (conferência pelo gate/Revisor) e 1.5 |
| RULE-EV-03: hallucination é detector | Não mexida; F1 não substitui a lente hallucination |
| D5: transição DETECTED→PASS/FAIL nunca por juízo do LLM | 1.2 usa os mesmos estados, sem transição nova |
| RULE-EV-05: sem limiar de convicção | 1.5; F1 não tem convicção (J-001 intocada) |
| RULE-EV-07: externo subordinado, nunca baseline | 1.5; nenhuma métrica externa importada (ADV-KFH-13) |
| SPEC-020 Non-goal: tooling de runtime fora; SPEC-045-RUNTIME-001 não antecipada | 1.3 (só a prova por item, já da SPEC-007; métricas agregadas INDETERMINADO) |
| Schema lógico: enum `lente` com 9 valores | 1.2: enum não muda |
| RULE-KFH-005: parte D "ANTES de qualquer juízo por modelo" | 1.2 item 1 |
| RULE-KFH-006: independência, IDs pela CIM, expressão de seis conjunções, precedência, limite RULE-MET-01, limiares INDETERMINADO | 1.2 itens 2, 3, 6; 1.4 |
| BASpec-KFH-006: "o juízo nunca é o gate final" | 1.2 item 4; 1.5 |
| INV-KFH-01: sem selo/VALIDADO, nada chega ao KG pelo caminho (b) | 1.2 item 5 |
| ERRATUM-SPEC020-001: *tool correctness* FECHADA; demais B "fecham nos pontos de dependência próprios" | 1.6; seção 3 (nota de leitura, sem editar) |
| SPEC-048 "Termo 4": F2 ≠ F1 | Seção 3; nada de frase entregue neste erratum |

Nenhuma obrigação herdada foi removida ou enfraquecida. `[INFERÊNCIA — conferido lendo os textos citados]`

---

## 6. Constitution Check (CC-01..CC-12) — só o que o erratum toca

| CC | Resultado | Por quê |
|---|---|---|
| CC-01 | PASS | Hierarquia não muda; F1 só admite `learning` (herdado da SPEC-007); nenhuma hipótese criada |
| CC-02 | PASS | Não redefine CEM/CHM/CCM/CDM/CNM; conhecimento formado não é Evidência (INV-06/INV-10 da SPEC-007 intactos) |
| CC-03 | PASS | Nenhum campo de convicção; J-001 intocada |
| CC-04 | PASS | Nenhuma Salvaguarda tocada; custo fora (INV-04) |
| CC-05 | PASS | CRITICAL (da SPEC-020) |
| CC-06/CC-07 | N/A | Não é Engineering Card |
| CC-08 | PASS | Seção 5, com evidência obrigação a obrigação |
| CC-09 | PASS | Limiares INDETERMINADO; limite RULE-MET-01 declarado (1.4); lacuna de calibração marcada [DECISÃO NECESSÁRIA] (seção 3); nenhum número |
| CC-10 | PASS | "faithfulness" externo (SRC-RAGAS-01) ≠ F1 do SOT (fidelidade do formado à fonte citada) ≠ F2 (suporte do entregue) ≠ verdade; declarado em 1.4 e seção 3 |
| CC-11 | N/A | O erratum não cria BASpec com efeito; as Classes D (KFH-005) e H (KFH-006) são herdadas da SPEC-007 |
| CC-12 | N/A | Meta-harness sem escola (como a SPEC-020) |

---

## 7. §7-bis — Redução de viés (CRITICAL)

**Bloco A — pergunta adversarial (o critério da seção 1, única parte com efeito de avaliação):**
- *Se o critério estivesse errado, o que se veria?* (1) Uma Spec futura que pula a parte D, aceita juiz igual ao formador ou fixa limiar de paper seria aprovada na avaliação da SPEC-020. Isso se observa pelos casos herdados: Cenário-KFH-T06/T07 (literais), T09 e ADV-KFH-04/24 (independência), ADV-KFH-13 (limiar externo). (2) O erratum lido como fechamento da "RAG faithfulness" inteira: o BL-017 encerrado ou a F2 tratada como fechada no ROADMAP/RMR-001. Observável no painel e no ROADMAP §12. (3) Número declarado como meta: observável por busca de limiar no texto.
- *O ENTÃO pode ser conferido por um observador independente?* Sim. Os itens 1–6 da seção 1.2 são presença/ausência de regras literais (busca de texto + leitura do gate de saída), sem juízo de LLM.
- *Existe QUANDO satisfeito sem que o ENTÃO deva acontecer?* Sim, em dois casos, cobertos: (a) Spec que só consome conhecimento carimbado — confere-se só o item 5; a fidelidade do que ela entrega é F2 (1.2); (b) Spec que não toca conhecimento formado — não aplicável com justificativa, não PASS (1.2).

**Bloco B — herança:** seção 5 (tabela obrigação a obrigação). Nenhuma obrigação sem evidência.

**Bloco C — epistêmico:**
- Não se afirma "conformidade a F1 garante fidelidade". Afirma-se só que ela é o critério de verificação; o mecanismo (parte D literal + juízo independente + gate determinístico) e o seu limite (RU-1; independência de identidade ≠ de erro) estão declarados (1.4). Não é afirmação causal nova.
- INDETERMINADO usado em vez de número: limiares, métricas agregadas, eficácia do juiz.
- Nenhuma probabilidade nem precisão numérica declarada.
- Premissa que pode estar errada: que "fecha em SPEC-007" do baseline autoriza um critério por metade. Base: DHR-SPEC007-002 §4 ("a dimensão se **divide**") e DHR-SPEC007-003 P-5 ("Uma emenda por metade"). `[FONTE]`

**Bloco D:** o erratum avalia; não executa nada nem cruza para a execução (INV-05). Toda dependência de Andraus está marcada como pergunta ou [DECISÃO NECESSÁRIA] (seções 3, 4 e 10).

---

## 8. Análise de impacto (RULE-HG-04) e compatibilidade proposta

| Alvo | Impacto |
|---|---|
| Schemas | Nenhum. O enum `lente` não muda |
| RAG / KG | Nenhum. Usa por referência RULE-KFH-005/006 e INV-KFH-01; não altera SPEC-006/007 |
| Skills | Nenhuma |
| Testes | Nenhum teste novo. Specs que formam conhecimento passam a registrar a conferência F1 no próprio `checks.md` (a SPEC-007 já o faz) |
| Modelos dependentes | SPEC-020, SPEC-007, SPEC-048, ERRATUM-SPEC020-001: texto não alterado. ROADMAP §12 (linha das dimensões B) e caminho crítico ("007 RAG (fecha 020: RAG faithfulness)"), RMR-001 (nota em BL-017) e CATALOGO: atualização aditiva **pelo Orquestrador, na homologação**, não por este erratum |
| Re-apontamentos em SPEC-021/SPEC-038 | Fora deste erratum: são da errata de re-apontamento (DHR-RETRO-001 §1, item (3)) |

**Compatibilidade proposta: Minor** `[PROPOSTA — Q-3]`.
- *A favor de Minor:* acrescenta critério a uma dimensão que **não era avaliada** (estava DIFERIDA); nada que antes passava passa a reprovar. Não muda regra, lente nem schema. A única Spec hoje no escopo (SPEC-007) já cumpre os itens 1–6 por construção. Precedente direto: o ERRATUM-SPEC020-001, que fez o mesmo para *tool correctness*, entrou numa homologação classificada como Minor (DHR-SPEC038-002, "Compatibilidade").
- *A favor de Major (para Andraus pesar):* o critério passa a **restringir Specs futuras** que formem conhecimento (não podem enfraquecer F1). As erratas restritivas da SPEC-006 (v1.11 e v1.13) foram Major (DHR-SPEC006-003 D3; DHR-SPEC006-005). A diferença: lá o KG passava a **recusar o que aceitava**; aqui nenhuma Spec homologada perde conformidade. `[INFERÊNCIA]`

---

## 9. Forma de aplicação proposta (depois da homologação) `[PROPOSTA — Q-4]`

**Forma A (recomendada — mesmo padrão do ERRATUM-SPEC020-001 e da Q-8 da errata v1.13 da SPEC-006):** este arquivo **é** o erratum. O plan.md da SPEC-020 recebe **uma linha** ao final, logo depois da linha "**Errata aditiva (2026-10-03, DHR-SPEC038-002)**", apontando para este arquivo. Texto proposto da linha:

> **Errata aditiva (data da homologação, ata a atribuir):** dimensão B "RAG faithfulness", **metade F1** (conhecimento formado) — critério verificável = conformidade a F1 da SPEC-007 (RULE-KFH-005/006), limiares INDETERMINADO — ver `governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md`. Texto acima não alterado (INV-09); metade F2 (SPEC-048) e decision traceability (SPEC-014) permanecem diferidas.

O `checks.md` da SPEC-020 **não** é editado: este erratum o cobre por referência.

**Forma B (alternativa, proposta no Plan da SPEC-048):** notas aditivas em cada um dos enunciados da seção 2. Desvantagem: mais pontos de edição no baseline e mais chance de contradição entre eles (C01 recorrente — RETROSPECTIVAS, Especificador).

---

## 10. Perguntas para Andraus

| # | Pergunta | Recomendação |
|---|---|---|
| Q-1 | Homologar o texto da seção 1 (critério da metade F1)? | Sim |
| Q-2 | Estado da metade F1 depois do erratum: (a) "critério definido, limiares INDETERMINADO" (como o ERRATUM-SPEC020-001 fez com *tool correctness*) ou (b) "fechável, mas só fechada depois da calibração com amostra"? | (a) |
| Q-3 | Compatibilidade: Minor ou Major (seção 8)? | Minor |
| Q-4 | Forma de aplicação: A (arquivo à parte + uma linha ao fim do plan.md) ou B (nota em cada enunciado)? | A |
| Q-5 | Aceitar o ajuste ao "texto único" da SPEC-048 ("F2: DIFERIDA até o erratum à parte — DHR-SPEC048-002 §3", no lugar de "na homologação do Plan da SPEC-048") e pedir que o erratum da metade F2 use a mesma redação? | Sim |
| Q-6 | Confirmar o código ERRATUM-SPEC020-002? | Sim |
| Q-7 | Calibração com amostra da metade F1 sem dono nem método (seção 3): (a) só registrar a lacuna agora; (b) encaminhar a uma futura errata da SPEC-007 (auditoria amostral de falso-CLEAR do juiz F1, análoga à RULE-RET-011); (c) deixar para o BUILD | (a) agora, com (b) anotada como dependência — mesmo tratamento que a DHR-SPEC006-005 D4 deu às dependências da SPEC-007 |
| Q-8 | Saneamento da divergência sobre SPEC-020-PRINC-001 (aberta no AGENTS.md §7 e na ordem de serviço; FECHADA no ROADMAP): tratar em ato à parte? | Sim, fora deste erratum |

---

## 11. Tabela fato → locais (P2) — cada fato que se repete e onde ele aparece

Numa correção futura, corrigir **todos** os locais da linha.

| Fato | Locais neste erratum | Âncoras no baseline (não editadas) |
|---|---|---|
| Metade F1 = conformidade a RULE-KFH-005 (antes) e RULE-KFH-006 (depois) | §0; 1.1; 1.2 itens 1–3; Herança INHERITS/tabela; linha proposta (§9); Q-1 | SPEC-007: RULE-KFH-005, RULE-KFH-006, seção "Proposta de emenda pontual à SPEC-020 … metade F1"; SPEC-020: D0 "O que a Missão NÃO é", D1 Non-goals |
| Limiares/métricas agregadas = INDETERMINADO até calibração com amostra; nenhum número | §0; 1.2 item 6; 1.3; CC-09; §7-bis Bloco C; linha proposta (§9); Q-2 | SPEC-007: RULE-KFH-006 ("Limiares/métricas agregadas …"), ADV-KFH-13, Riscos "R-5 número inventado"; DHR-SPEC007-001 Q5; DHR-SPEC007-003 P-5 |
| Juízo nunca é gate final; LLM nunca aprova Spec | 1.2 item 4; 1.5; Herança (RULE-EV-02, D5, BASpec-KFH-006); §7-bis Bloco A | SPEC-020: RULE-EV-02/03, D5 "Invariante de estado"; SPEC-007: BASpec-KFH-006 CRITÉRIO 4Es |
| Metade F2 fora deste erratum; DIFERIDA até erratum à parte | §0; 1.2 (consumidor); 1.6; seção 3; §4 BL-017; linha proposta (§9); Q-5 | SPEC-048: "Proposta de emenda pontual à SPEC-020 … metade F2"; DHR-SPEC048-002 §3 |
| *decision traceability* DIFERIDA (SPEC-014) | §0; 1.6; seção 2; §4; linha proposta (§9) | SPEC-020: D0, D1, lista final, errata ao fim; ERRATUM-SPEC020-001 |
| A dimensão "RAG faithfulness" inteira não fecha; BL-017 não fecha (PARCIAL; `Em espera`) | §0; 1.6; seção 2 (Riscos); §4; §7-bis Bloco A (2) | RMR-001 BL-017; SPEC-007 "Nota de gate" (Disposição PARCIAL) |
| ADV-EV-06 vale para F2 e *decision traceability*; não para F1 | 1.6; seção 2; Herança tabela | SPEC-020: ADV-EV-06; Riscos "Classe B tratada como fechada" |
| Limite: F1 ≠ verdade da fonte ≠ relevância; independência de identidade ≠ de erro; RU-1 | 1.4; CC-10; §7-bis Bloco C | SPEC-007: RULE-KFH-006 "LIMITE (RULE-MET-01)", ADV-KFH-03 |
| Lacuna: sem auditoria amostral do juiz F1 | Seção 3; CC-09; Q-7 | SPEC-007: ADV-KFH-03 (RU-1), EC-KFH-004; SPEC-048: RULE-RET-011 (só F2) |
| Ajuste ao "texto único" da SPEC-048 | Seção 3; 1.6; Q-5 | SPEC-048: "Texto único por linha da SPEC-020 — coordenado com a metade F1"; DHR-SPEC048-002 §3 |
| Leitura vigente da frase do ERRATUM-SPEC020-001 | Seção 3; Herança tabela | ERRATUM-SPEC020-001, "O que NÃO muda" |
| Enum `lente` inalterado; F1 não é 10ª lente | §0; 1.2; Herança tabela; Impacto (Schemas) | SPEC-020: I/O Schemas, "Resultado de avaliação de lente" |
| Não aplicável ≠ PASS para Spec que não toca formado | 1.2; §7-bis Bloco A | SPEC-020: D5 (estados) |
| Compatibilidade proposta Minor | Cabeçalho; seção 8; Q-3 | DHR-SPEC038-002 ("Compatibilidade"); DHR-SPEC006-003 D3; DHR-SPEC006-005 |
| Forma A: uma linha ao fim do plan.md | Seção 9; Q-4; seção 13 (assertivas) | SPEC-020: linha "**Errata aditiva (2026-10-03, DHR-SPEC038-002)**" |
| Decisões abertas listadas, nenhuma fechada | §4; §7-bis Bloco D | ROADMAP "Decisões abertas ativas"; DHR-RETRO-001 §3 |

---

## 12. Pesquisa (RULE-ECC-02) — não aplicável a este ato

Este erratum não é abertura de Spec: aplica um critério já pesquisado e homologado no Dossiê da SPEC-007 (research §2/§3.5 — SRC-RAGAS-01, SRC-FAITHJUDGE-01, SRC-ALCE-01; classificação e capturas lá). Nenhuma fonte externa nova foi consultada nem importada; as citadas seguem `[EXTERNO]`, DADO, nunca baseline (RULE-EV-07; DHR-PROV-WEB-001 §2.1). `[FONTE: SPEC-007 plan.md "Dependências técnicas"]`

---

## 13. Verificação de spec deste erratum (feedback interno — NÃO é parecer do Revisor nem homologação)

- As âncoras foram conferidas por busca de texto (Grep/Read): SPEC-020 plan.md (D0, D1 Non-goals, D5, ADV-EV-06, Riscos, Etiquetagem, lista final, errata ao fim, I/O Schemas), `checks.md` e `research.md`; SPEC-007 plan.md (RULE-KFH-005/006, INV-KFH-01, BASpec-KFH-005/006, EC-KFH-003, T06–T09, ADV-KFH-03/04/05/13/24, seção da proposta F1, nota de gate do BL-017); SPEC-048 plan.md ("Termo 4", texto único, proposta F2, RULE-RET-009/010/011); atas DHR-SPEC007-001/002/003/005, DHR-SPEC048-001/002, DHR-SPEC038-002, DHR-SPEC006-005, DHR-RETRO-001; RMR-001 BL-017; ROADMAP §12.
- Nenhum ID novo de RULE/BASpec/EC/T/ADV; nenhum placeholder de ata com formato de ID.
- **Assertivas para o Orquestrador/Revisor.** **Antes** da homologação: o `specs/features/SPEC-020/plan.md` não contém `ERRATUM-SPEC020-002` (assert-absent) e o `checks.md` não muda. **Depois** (Forma A): assert-present de **uma** linha nova ao final do plan.md apontando para este arquivo; nenhuma outra linha alterada.
- **Gates — o Especificador NÃO os executou (não tem Bash). Ficam para o Orquestrador:**
  - `python scripts/check_refs.py`
  - `python scripts/check_invariants.py governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md`
  - `python scripts/revisor_gate.py governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md` (pode reprovar por estrutura de Plan — este arquivo não é um Plan; mesma observação da errata v1.13)
  - `python scripts/validate_spec_sot.py specs/features/SPEC-020/plan.md` (o plan não muda; confirma que segue verde)
  - `python scripts/check_doc_sync.py` (atenção à divergência SPEC-020-PRINC-001 registrada no §4)
  - `python scripts/backlog_triggers.py` (BL-017 deve seguir `Em espera`)
  - `python scripts/build_map.py` + `python scripts/build_map.py --check`
  - `python -m unittest discover -s tests`

"VERIFY" interno ≠ CONFORME ≠ homologação.

**Pronto para revisão (v1.0).**
