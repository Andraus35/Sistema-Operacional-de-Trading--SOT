# ERRATUM-SPEC020-002 — Dimensão B "RAG faithfulness", metade F1 (fidelidade do conhecimento formado) — erratum ADITIVO (PROPOSTA)

| Campo | Valor |
|---|---|
| Código | **ERRATUM-SPEC020-002** — número **proposto**; a atribuição final é de Andraus na homologação (Q-6). |
| Versão | **v1.2** (2026-10-30, curta). Corrige o parecer R2 (`governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R2-2026-10-30.md`, NÃO CONFORME): N-1 (Média), m-1 e m-3 (Menores). m-2 já foi aplicado pelo Orquestrador por ficha M e está mantido. Mudanças: "Registro de mudanças v1.1 → v1.2"; trechos da v1.1 trocados: "Anexo V1.1"; a v1.1 inteira está no commit `9a3f0bf`. *[v1.1: "**v1.1** (2026-10-30). Corrige o parecer R1 …" — continua abaixo.]* **v1.1** (2026-10-30). Corrige o parecer R1 (`governance/propostas/SPEC-020/PARECER-REVISOR-ERRATUM-SPEC020-002-R1-2026-10-30.md`, NÃO CONFORME): M-1..M-4 (Médias) e m-5 (Menor). m-1..m-4 já tinham sido aplicados pelo Orquestrador por ficha M e estão mantidos. Mudanças por achado: "Registro de mudanças v1.0 → v1.1". Trechos da v1.0 trocados: "Anexo V1.0"; a v1.0 inteira está no commit `ca724ed`. *[v1.0 (2026-10-30) — primeira entrega.]* |
| Spec afetada | SPEC-020 — Harness Evaluation Specification (núcleo A), **HOMOLOGADA — BASELINE** (DHR-SPEC020-001) + ERRATUM-SPEC020-001 (DHR-SPEC038-002). **Este erratum NÃO edita texto baselined** (INV-07/INV-09): `specs/features/SPEC-020/plan.md` e `specs/features/SPEC-020/checks.md` ficam como estão. |
| Natureza | **HOMOLOGADO — ERRATUM-SPEC020-002 (Minor, prospectivo, aditivo), DHR-SPEC020-002** (Andraus, chat 2026-10-30; Revisor R3 CONFORME condicional). *[Texto anterior preservado — INV-07: "PROPOSTA de erratum aditivo. Aguarda o Revisor e a homologação de Andraus. Não é baseline. Nada nele vale antes da homologação (RULE-HG-01/02/03)."]* |
| Ordem | Ordem de Andraus transmitida pelo Orquestrador (chat, 2026-10-30: "Emenda da SPEC-020"), em execução da DHR-RETRO-001 §1 ("Próxima frente", item (2): "emenda à SPEC-020 (metade F1; F2 vai com a SPEC-048)") e §2 ("Uma de cada vez, nesta ordem, cada uma com Revisor e homologação própria de Andraus. Nenhum baseline é editado antes da homologação da respectiva errata"). A errata da SPEC-006, item (1), já foi homologada (DHR-SPEC006-005). `[FONTE — FATO NORMATIVO: DHR-RETRO-001; a ordem de 2026-10-30 ainda não está registrada em ata — registro do Orquestrador (parecer R1, O-2)]` |
| Fonte do estado das decisões | **Só o `ROADMAP.md`**, linhas "Decisões abertas ativas" e "Decisões FECHADAS" (o ROADMAP prevalece — AGENTS.md §7). Cada ID foi conferido na fonte citada ao lado dele (M-1). |
| Origem do conteúdo | `specs/features/SPEC-007/plan.md` v2.3 (BASELINE, DHR-SPEC007-005), seção "Proposta de emenda pontual à SPEC-020 (dimensão B \"RAG faithfulness\") — metade F1"; RULE-KFH-005; RULE-KFH-006; INV-KFH-01; BASpec-KFH-005/006; EC-KFH-003/004; Cenário-KFH-T06..T09; ADV-KFH-01/03/04/05/13/24. SPEC-020: D5, D6, I/O Schema "Resultado de avaliação de lente". Atas: DHR-SPEC007-001 Q5; DHR-SPEC007-002 §3/§4; DHR-SPEC007-003 P-5; DHR-SPEC007-005 H-3; DHR-SPEC048-001 (condição m-10); DHR-SPEC048-002 §3/§5; DHR-SPEC020-001. `[FONTE]` |
| Âncoras | **Por ID + texto literal entre aspas, nunca por número de linha** (prática P2 em vigor; P3 ainda a especificar — DHR-RETRO-001 §1). |
| Complexidade | CRITICAL (a da SPEC-020; não muda) · D0–D8 focado no que o erratum toca · profile standard + adversarial. |
| Respostas de Andraus incorporadas | DHR-RETRO-001 §7 (Adendo 4, chat 2026-10-30): **Q-3** = só daqui em diante (prospectiva); **Q-2** = critério definido, limiares INDETERMINADO, Revisor dá o veredito como detector até existir gate; **Q-4** = arquivo à parte + uma linha no plano da SPEC-020; **Q-7** = só registrar a lacuna (dependência de futura errata da SPEC-007). Q-1, Q-5, Q-6 e Q-9 seguem para a homologação. `[FONTE — FATO NORMATIVO: ata]` |
| Compatibilidade proposta | **Minor**, com aplicação **prospectiva** — o alcance prospectivo foi decidido por Andraus (Q-3, DHR-RETRO-001 §7); a classificação Minor é proposta do Especificador, **a confirmar na homologação**. Justificativa na seção 8. `[PROPOSTA]` *[v1.1: "**Minor**, com aplicação **prospectiva** (recomendação; decisão de Andraus — Q-3). Justificativa na seção 8."]* |
| Status epistemológico | `[FONTE]` = conferido nos arquivos citados; `[INFERÊNCIA]` = leitura do Especificador, a conferir pelo Revisor; `[PROPOSTA]` = o que se pede a Andraus; `[DECISÃO NECESSÁRIA]` = lacuna que o Especificador não resolve. |
| Autor | Especificador Principal SOT (Claude Code, Opus 5.5) |
| Data | 2026-10-30 |

---

## 0. O que este erratum faz, em uma frase

A SPEC-020 deixou a dimensão B "RAG faithfulness" **DIFERIDA** até o componente-alvo existir. A divisão da SPEC-007 partiu essa dimensão em duas metades: **F1** (o conhecimento formado não inventa o que a fonte não diz — SPEC-007) e **F2** (cada frase entregue tem apoio no trecho citado — SPEC-048) (DHR-SPEC007-002 §4; DHR-SPEC007-003 P-5). A SPEC-007 já está homologada. Este erratum diz **como a metade F1 passa a ser verificada**: pela **conformidade a F1 da SPEC-007** (RULE-KFH-005 primeiro, RULE-KFH-006 depois), com **limiares INDETERMINADO** até calibração com amostra. `[FONTE: DHR-SPEC007-001 Q5; DHR-SPEC007-003 P-5; SPEC-007 plan.md, seção "Proposta de emenda pontual à SPEC-020 … metade F1"]`

**Não faz:** não trata da metade F2 (fica para um erratum à parte, da SPEC-048). Não mexe em *decision traceability* (segue DIFERIDA, SPEC-014). Não fecha a dimensão "RAG faithfulness" inteira. Não fecha o BL-017. Não fecha nenhuma decisão aberta. Não cria lente nova, RULE, BASpec, EC, cenário nem ADV. Não muda o enum `lente` do schema lógico da SPEC-020 nem a máquina de estados do D5. Não cria gate determinístico. Não fixa número. Não retroage sobre Specs já homologadas. Não edita o plan.md da SPEC-020, da SPEC-007 nem da SPEC-048. `[FONTE: DHR-RETRO-001 §2-§3; DHR-SPEC007-005 H-3; DHR-SPEC048-002 §3]`

---

## 1. Texto do erratum `[PROPOSTA]`

> **ERRATUM-SPEC020-002 — dimensão B "RAG faithfulness", metade F1 (conhecimento formado).**
>
> **1.1 Critério.** Na dimensão B **"RAG faithfulness"** da SPEC-020 (classe dependente-de-upstream; Non-goal "Dimensões **classe B** (RAG faithfulness / tool correctness / decision traceability)"), a parte que trata da **fidelidade do conhecimento formado** (metade **F1**) passa a ter **critério verificável definido**: a **conformidade a F1 da SPEC-007** (BASELINE v2.3, DHR-SPEC007-005) — **RULE-KFH-005** ("VALIDAÇÃO F1 — parte DETERMINÍSTICA (roda ANTES de qualquer juízo por modelo)") e **RULE-KFH-006** ("VALIDAÇÃO F1 — JUÍZO (Classe H), só após RULE-KFH-005 passar"), nesta ordem.
>
> **1.2 Quem fica sujeito, e a que (aplicação prospectiva).** O critério incide **só** sobre Spec, Plan ou errata **homologados depois deste erratum** (molde da CC-11/RULE-MECH-01 e da CC-12/RULE-PD-01: "prospectiva"). **Não há reconferência** das Specs já homologadas (SPEC-006, SPEC-007, SPEC-048): elas não ganham nem perdem conformidade por este erratum (decidido por Andraus: "só daqui em diante" — DHR-RETRO-001 §7, Q-3). Andraus registrou a intenção de uma **etapa futura de revisão das specs pretéritas** ("Teremos uma etapa futura de revisão das specs pretéritas"), **sem ordem nem escopo definidos**: não é decisão aberta nova, não foi ordenada e não é reconferência por este erratum. Ficam sujeitas, e só elas:
> - **(A) Formação:** Spec/errata cujo escopo inclua **formar conhecimento a partir de fonte registrada com destino ao KG pelo caminho (b) da RULE-CKG-010** (via selo), ou **mudar esse caminho** (ex.: futura errata da SPEC-007). Conferem-se os itens 1–6 abaixo.
> - **(B) Admissão ou consumo:** Spec/errata **cujo escopo inclua admitir** conhecimento carimbado no KG pelo caminho (b) (ex.: errata futura da SPEC-006 que trate dessa admissão) **ou consumir** conhecimento carimbado (ex.: errata futura da SPEC-048 que trate desse consumo; slot SPEC-049, quando aberto), **ou mudar esse caminho de admissão/consumo**. Uma errata dessas Specs que não toque admissão nem consumo **não é sujeita**. Confere-se só o item 5 (não cria caminho que contorne F1). A fidelidade do que ela **entrega** é matéria da metade F2, fora deste erratum.
> - **Demais Specs:** **nenhuma obrigação nova** — não registram nada sobre F1 (seção 1.4).
>
> **Itens conferidos** (todos "manter, sem enfraquecer"):
> 1. **Parte determinística antes do juízo:** citação resolve, trecho existe, literais preservados ("números, sinais, unidades, percentuais e marcadores de negação"), cobertura e tipo — falha ⇒ `KC_REPROVADO`, sem chamar juiz (RULE-KFH-005; BASpec-KFH-005; Cenário-KFH-T06/T07; ADV-KFH-05).
> 2. **Juízo por modelo independente:** `judge_model_id ≠ former_model_id`, IDs gravados pela CIM, juiz em ponto separado e sem escrita; "mesmo modelo em contexto novo NÃO é independente" (RULE-KFH-006; Cenário-KFH-T09; ADV-KFH-04/24).
> 3. **VALIDADO só pela expressão única da RULE-KFH-006** ("repetida com as MESMAS seis conjunções"), com a precedência da regra ("qualquer FALHA ⇒ `KC_REPROVADO` (prevalece); senão, qualquer INDETERMINADO ⇒ `KC_INDETERMINADO` (não sela)") (RULE-KFH-006; BASpec-KFH-006 GATE DE SAÍDA; EC-KFH-003 PRECOND).
> 4. **O juízo nunca é o gate final:** "Conformidade > Eficácia — o juízo nunca é o gate final" (BASpec-KFH-006, CRITÉRIO 4Es).
> 5. **Sem caminho que contorne F1:** "Nada chega ao KG pelo caminho (b) da RULE-CKG-010 sem SELO válido … o selo exige registro de validação com resultado VALIDADO" (INV-KFH-01; ADV-KFH-01).
> 6. **Limiares INDETERMINADO:** "Limiares/métricas agregadas de fidelidade = INDETERMINADO até calibração com amostra (nenhum número externo importado)" (RULE-KFH-006; ADV-KFH-13 `EXTERNAL_THRESHOLD_IMPORTED`).
>
> **1.3 Fora de F1 (sem decidir decisão aberta).** F1 trata **só** de conhecimento formado a partir de **fonte registrada** e publicado pelo **caminho (b)** (selo). Ficam **fora** deste critério: (i) os objetos canônicos admitidos pelo **caminho (a)** da RULE-CKG-010 ("OBJETOS CANÔNICOS e suas transições via CICLO DE VIDA canônico (já validados por SPEC-001/002/003)"); (ii) conhecimento **de experiência** ou de aprendizado do próprio sistema (memória de experiência — SPEC-009/017; ciclo de evolução do conhecimento — K-001, **aberta**). Se e como esses ganham critério de fidelidade **não é decidido aqui** (CONS-01). `[FONTE: SPEC-006 RULE-CKG-010; ROADMAP "Decisões abertas ativas" (K-001)]`
>
> **1.4 Como se confere em tempo de Spec — parte literal, parte de julgamento, e quem dá o veredito.**
> - **Parte literal** (busca de texto possível), **por grupo** — a mesma divisão de 1.2 e 1.5:
>   - **Grupo (A)** (itens 1–6): presença, na Spec, das referências RULE-KFH-005, RULE-KFH-006 e INV-KFH-01 (ou de texto equivalente que as transcreva); presença da expressão `judge_model_id ≠ former_model_id` e dos códigos `KC_REPROVADO`, `KC_INDETERMINADO`, `JUDGE_NOT_INDEPENDENT`, `MODEL_ID_UNAUTHENTICATED`; ausência de número declarado como limiar de fidelidade (ADV-KFH-13).
>   - **Grupo (B)** (só o item 5): presença, na Spec, da referência INV-KFH-01 (ou de texto equivalente que a transcreva). Nada mais é exigido no literal: a Spec do grupo (B) não precisa citar RULE-KFH-005/006, a expressão do juiz nem os códigos `KC_*`.
>   *[v1.1: parte literal única "na Spec sujeita", sem divisão por grupo — Anexo V1.1]*
> - **Parte de julgamento** (não é busca): se a Spec está mesmo em (A) ou (B); **nos dois grupos**, se há **caminho que contorne o selo** (item 5 em substância — ex.: um atalho de escrita no KG fora do selo, citado ou não INV-KFH-01); **só no grupo (A)**, se alguma regra nova **enfraquece** os itens 1–4 e 6 em substância e se a ordem "parte D antes do juízo" é preservada no comportamento. *[v1.1: "se alguma regra nova **enfraquece** os itens 1–6 em substância (ex.: um atalho de escrita que contorna o selo sem citar INV-KFH-01); se a ordem \"parte D antes do juízo\" é preservada no comportamento."]*
> - **Quem dá o veredito:** **hoje não existe gate determinístico para F1 em tempo de Spec** (nenhum script do repositório confere os itens 1–6) — **lacuna registrada, não resolvida aqui** (seção 3; Q-9). Por isso: a parte literal é conferida por busca de texto feita pelo Revisor ou pelo Orquestrador; a parte de julgamento é do **Revisor como detector** (SPEC-020 D6 passo 7: "Revisor … audita o resultado das lentes como parte do parecer (detector, não gate)"; RULE-EV-02). O campo `veredito_por` usa o valor que o schema já tem: `revisor` (o D5 já admite "Gate determinístico/Revisor confirmou"). **Esse veredito não aprova a Spec:** a vigência é só da homologação de Andraus (D6 passo 8; RULE-HG-03). A tensão "D5 aceita veredito do Revisor × D6 passo 7 chama o Revisor de detector" é **herdada** da SPEC-020, não criada aqui. `[INFERÊNCIA]`
>
> **1.5 Estados e registro (reuso do D5, sem estado nem transição nova).**
> - **Caminho de estados** de uma Spec sujeita (A ou B), só com transições que o D5 já tem: `NOT_EVALUATED → DETECTED` (a busca literal e a leitura do Revisor produzem o sinal) `→ PASS | FAIL | INDETERMINADO`; `INDETERMINADO → PASS | FAIL` (após o adversarial); `FAIL → REGRESSED` (RULE-EV-04).
> - **Spec não sujeita** (nem A nem B): **não recebe estado F1** — não há linha a registrar. Não é PASS e não é "não aplicável" como estado: o D5 não tem esse estado e este erratum não o cria.
> - **Lugar do registro:** uma linha **"Dimensão B — F1"** no `checks.md` da Spec sujeita, com: estado (do D5); `veredito_por`; os itens conferidos (1–6 em (A); só 5 em (B)), cada um com âncora; e `codigo_achado` quando houver. Usa os **nomes de campo** do schema "Resultado de avaliação de lente", mas **não é instância** dele: o enum `lente` continua com 9 valores (F1 não é 10ª lente). Esta forma de registro é **ADDED** (seção 5).
>
> **1.6 O que vale em tempo de execução (runtime) — sem antecipar tooling.** A prova de fidelidade de **cada** item publicado é o `validation_record` com resultado VALIDADO, ligado ao `material_hash` e ao selo (EC-KFH-003/EC-KFH-004), reconstruível. **Métricas agregadas** (taxas, limiares, amostragem) = **INDETERMINADO até calibração com amostra**; nenhum número é fixado por este erratum (R-5 da SPEC-007; CC-09). O tooling de avaliação em runtime segue fora da SPEC-020 (Non-goal "Tooling de avaliação de **runtime**"; SPEC-045-RUNTIME-001 segue ABERTA).
>
> **1.7 Limite declarado (RULE-MET-01).** F1 mede se o conhecimento formado **se apoia na fonte citada** — não mede se a fonte é verdadeira, nem relevância. IDs de modelo diferentes provam independência de **identidade**, não de **erro** (RULE-KFH-006, "LIMITE (RULE-MET-01)"). Se o juiz independente também for enganado, a afirmação passa — risco residual RU-1 da SPEC-007 (ADV-KFH-03, "eficácia = INDETERMINADA até calibração"). Conformidade a F1 é o **critério de verificação**; não é garantia de fidelidade.
>
> **1.8 Compatibilidade com as regras de avaliação da SPEC-020.** RULE-EV-02 ("O LLM NUNCA é o gate de aprovação de uma Spec") e RULE-EV-03 seguem intactas: em spec-time nenhum resultado F1 aprova Spec (1.4); em runtime, o juiz F1 é etapa de Classe H cujo resultado passa pelo gate determinístico da RULE-KFH-006 (item 4). RULE-EV-05: F1 não tem campo de convicção nem limiar de convicção. RULE-EV-07: as fontes externas da SPEC-007 (research §2 — SRC-RAGAS-01, SRC-FAITHJUDGE-01, SRC-ALCE-01) seguem DADO, nunca baseline.
>
> **1.9 Estado das dimensões B depois deste erratum.**
> - **RAG faithfulness — metade F1:** critério verificável definido (acima); limiares INDETERMINADO.
> - **RAG faithfulness — metade F2:** segue **DIFERIDA** até a homologação do erratum à parte da metade F2 (SPEC-048 — DHR-SPEC048-002 §3).
> - **A dimensão "RAG faithfulness" como um todo** só deixa de ser diferida quando as duas metades tiverem critério homologado.
> - **tool correctness:** encerrada pelo ERRATUM-SPEC020-001 — não muda.
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

## 3. Coordenação com a metade F2 (DHR-SPEC048-001, condição m-10) e lacunas `[FONTE + PROPOSTA]`

**Fronteira.** F1 = fidelidade do **conhecimento formado** à fonte (SPEC-007: RULE-KFH-005/006). F2 = suporte de **cada item/frase entregue** no trecho que cita (SPEC-048: RULE-RET-009/010/011). A SPEC-048 já define, no "Termo 4": "suporte de cada coisa entregue no trecho que ela cita (frase entregue × trecho) ≠ \"F1\" (fidelidade do conhecimento formado — SPEC-007)" e "F2 mede **suporte**, não **dependência** nem **verdade**" (SPEC-048 plan.md). Nada deste erratum fala de frase entregue, pacote ou síntese. `[FONTE: DHR-SPEC007-002 §3; SPEC-048 plan.md "Termo 4"]`

**Texto único por linha (proposto pela SPEC-048).** O Plan da SPEC-048 (seção "Texto único por linha da SPEC-020 — coordenado com a metade F1") propôs uma nota igual para as duas metades e disse que a metade F1 "pode usar este texto sem alteração". Este erratum **adota o conteúdo** dessa nota, com **um ajuste**:

- **Divergência registrada.** A nota diz "F2: na homologação do Plan da SPEC-048". Isso não aconteceu: a DHR-SPEC048-002 §3 registra: "**Não aplicados nesta ata** (passos à parte, por ordem expressa de Andraus): errata aditiva à SPEC-006 (E-1..E-4); emenda de fidelidade F2 à SPEC-020; …". Por isso a seção 1.9 diz "F2: DIFERIDA até a homologação do erratum à parte da metade F2 (DHR-SPEC048-002 §3)". O texto da SPEC-048 (baseline) **não é editado** aqui. Proposta: o erratum da metade F2 usa a mesma redação ajustada (Q-5). `[FONTE: DHR-SPEC048-002 §3; INFERÊNCIA quanto ao ajuste]`
- **Nada se contradiz** entre a seção 1 deste erratum e a "Proposta de emenda pontual à SPEC-020 … metade F2" da SPEC-048: as duas usam "limiares INDETERMINADO até calibração com amostra", mantêm *decision traceability* com a SPEC-014 e não editam a SPEC-020. `[INFERÊNCIA — conferido lendo as duas seções]`
- **Nota sobre o ERRATUM-SPEC020-001.** A frase dele "**RAG faithfulness ↔ SPEC-007** … permanecem **DIFERIDAS**" (seção "O que NÃO muda") **não é editada** (homologado; INV-09). Leitura vigente: "a dimensão 'RAG faithfulness' divide-se em F1 (SPEC-007) e F2 (SPEC-048); a metade F1 tem critério por este erratum; a metade F2 segue diferida até a homologação do seu erratum". Mesmo texto que a SPEC-048 propôs para essa linha, com o ajuste acima. `[FONTE: SPEC-048 plan.md, linha da tabela de re-apontamento sobre `governance/ERRATUM-SPEC020-001_Fechamento_tool_correctness.md`]`

**Lacuna 1 — calibração (não resolvida).** Para F2 existe auditoria amostral de falso-ACEITE do juiz (SPEC-048, RULE-RET-011). Para F1, a SPEC-007 **não** traz auditoria amostral de falso-CLEAR do juiz F1: há só o risco residual RU-1 ("eficácia = INDETERMINADA até calibração"; mitigações declaradas no ADV-KFH-03: visto de lote para definições/regras (P-2) e marca de contradição) e a auditoria amostral do `record_hash` (EC-KFH-004), que confere identidade, não qualidade. Logo, "calibração com amostra" da metade F1 **não tem dono nem método definidos**. Este erratum não cria um (seria regra nova na SPEC-007). **Decidido por Andraus (Q-7, DHR-RETRO-001 §7): só registrar a lacuna**, como **dependência de futura errata da SPEC-007** (sem ordem dada para essa errata). `[FONTE: DHR-RETRO-001 §7]` *[v1.1: "`[DECISÃO NECESSÁRIA — Q-7]`"]*

**Lacuna 2 — sem gate determinístico para F1 em tempo de Spec (não resolvida).** Nenhum script do repositório confere os itens 1–6 (1.4). A parte literal poderia virar gate (busca de IDs/códigos/expressão), mas criar mecanismo é proposta de processo, com `governance/MECANISMOS.json` no mesmo PR e só por ordem de Andraus (AGENTS.md §12, passo 5). Até lá, o veredito é do Revisor como detector e a vigência é de Andraus (confirmado por Andraus como estado da metade F1 — Q-2, DHR-RETRO-001 §7). O que fazer com a lacuna segue pendente. `[DECISÃO NECESSÁRIA — Q-9]`

---

## 4. O que NÃO muda (CONS-01)

- **BL-017** segue com **Disposição PARCIAL** (SPEC-007 plan.md v2.3, nota de gate: "**Disposição: PARCIAL** — motivo: a dimensão **RAG faithfulness** divide-se (DHR-SPEC007-002 §4; DHR-SPEC007-003 P-5): **F1 aqui** (RULE-KFH-005/006 — fidelidade do conhecimento formado; limiares INDETERMINADO), fechando a metade F1 por emenda pontual à SPEC-020 …; **F2 na SPEC-048** …"; *decision traceability* com a SPEC-014). Estado no painel **inalterado** (`Em espera`); só Andraus promove ou encerra (RMR-001 §5). O BL-017 **não fecha** por este erratum: restam a metade F2 e *decision traceability*. `[FONTE: RMR-001 BL-017; SPEC-007 plan.md "Nota de gate"]`
- Nenhuma lente, RULE-EV, BASpec-EV, EC-EV, cenário, ADV, schema ou estado do D5 da SPEC-020 é alterado. O núcleo A e a 9ª lente seguem como homologados.
- Nenhuma regra da SPEC-007 é alterada; RULE-KFH-005/006 são **usadas por referência**.
- **Permanecem ABERTAS** (nenhuma fechada por este erratum), conforme o `ROADMAP.md`, linha "Decisões abertas ativas": J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WORKFLOW-SOT-001 (residual: só WF-D03). `[FONTE: ROADMAP.md "Decisões abertas ativas"]`
- **Também abertas, registradas em ata (não constam da linha do ROADMAP):** CKG-STRUCT-ORIGIN-001 (BL-035) e "produtor/gatilho de promoção" `[FONTE: DHR-SPEC048-002 §5]`; o **mecanismo** de assinatura dos atos de Andraus (o princípio foi decidido; "o MECANISMO … segue ABERTO para a construção") `[FONTE: ROADMAP.md "Decisões FECHADAS", item "Autenticação dos atos de Andraus"]`.
  - *Nota de divergência (registrada, não resolvida):* SPEC-020-PRINC-001 (FECHADA, segundo o ROADMAP, linha "Decisões FECHADAS": "SPEC-020 homologada, 2026-09-27, DHR-SPEC020-001"; e EFETIVA segundo a própria ata DHR-SPEC020-001, item 1: "SPEC-020-PRINC-001 — EFETIVA"). O AGENTS.md §7 a listava entre as ativas (defasado); a v1.0 deste erratum repetiu esse erro porque a ordem de serviço copiou o AGENTS.md §7 (parecer R1, M-1). Saneado por Andraus em 2026-10-30 (DHR-DOCSYNC-003, item a). *[v1.1: "O AGENTS.md §7 ainda a lista entre as ativas: está **defasado**. … O saneamento é de Andraus: AGENTS.md é arquivo protegido (AGENTS.md §10)."]* Este erratum **não toca** a decisão: só deixa de listá-la como aberta. `[FONTE: ROADMAP.md "Decisões FECHADAS"; DHR-SPEC020-001; AGENTS.md §7; DHR-DOCSYNC-003 — Q-8]`
- **Linha de montagem da SPEC-007 segue parada** até as liberações de Andraus (DHR-SPEC007-005 §3). Este erratum define critério; não libera nada.

---

## 5. Herança/Delta (CC-08; RULE-HD-02/03/04)

- **INHERITS** (ID + versão): SPEC-020 v1.0 (BASELINE, DHR-SPEC020-001): RULE-EV-01/02/03/04/05/07; D5 (estados, transições e invariante "o estado nunca transita de DETECTED direto a PASS/FAIL **por juízo do LLM**"); D6 (passos 7 e 8); Non-goals (classe B; limiar de convicção; tooling de runtime); ADV-EV-06; schema lógico "Resultado de avaliação de lente" (campos e enum `lente`). ERRATUM-SPEC020-001 (DHR-SPEC038-002): padrão de forma; *tool correctness* encerrada. SPEC-007 v2.3 (BASELINE, DHR-SPEC007-005): RULE-KFH-005; RULE-KFH-006; INV-KFH-01; BASpec-KFH-005/006; EC-KFH-003/004; ADV-KFH-01/03/04/05/13/24; Cenário-KFH-T06..T09. SPEC-006 (BASELINE v1.7 + erratas): RULE-CKG-010 (caminhos (a) e (b)). SPEC-048 v1.4 (BASELINE, DHR-SPEC048-002): "Termo 4" (fronteira F1×F2); RULE-RET-011 (só como comparação). Método: CC-11/RULE-MECH-01 e CC-12/RULE-PD-01 (molde de aplicação prospectiva).
- **ADDED:** critério verificável da metade F1 (1.1–1.3); separação literal × julgamento e atribuição do veredito (1.4); forma e lugar do registro "Dimensão B — F1" no `checks.md` da Spec sujeita (1.5); leitura vigente (seção 2); nota de coordenação F1×F2 e lacunas (seção 3).
- **MODIFIED:** nenhum texto, nenhum estado e nenhuma transição do D5; enum `lente` intacto. O estado da metade F1 passa de "DIFERIDA" a "critério definido" **pela condição que o próprio baseline já escreveu** ("fecha em SPEC-007"; ADV-EV-06 "antes do componente-alvo"). É realização de condição prevista, não mudança de regra. `[INFERÊNCIA — a conferir pelo Revisor]`
- **REMOVED:** vazio.

**Evidência obrigação a obrigação (§7-bis Bloco B):**

| Obrigação herdada | Onde este erratum a cumpre |
|---|---|
| SPEC-020 Non-goal: classe B "não fechadas antes do componente-alvo (CONS-01)" | Só a metade F1, cujo componente-alvo (SPEC-007) está homologado; F2 e *decision traceability* seguem DIFERIDAS (1.9) |
| ADV-EV-06: rejeitar `CLASS_B_PREMATURE` | 1.9 mantém a rejeição para F2 e *decision traceability*; a dimensão inteira não é fechada |
| RULE-EV-02: "O LLM NUNCA é o gate de aprovação de uma Spec" | 1.4 (Revisor como detector; vigência só de Andraus) e 1.8 |
| D6 passo 7: Revisor "(detector, não gate)"; passo 8: "Andraus homologa … A avaliação NÃO homologa" | 1.4 |
| RULE-EV-03: hallucination é detector | Não mexida; F1 não substitui a lente hallucination |
| D5: estados e transições; DETECTED→PASS/FAIL nunca por juízo do LLM | 1.5 usa só transições existentes; DETECTED→PASS/FAIL nunca pelo detector: veredito do Revisor (valor `revisor` já admitido pelo D5) e vigência só de Andraus; tensão com o invariante do D5 herdada e declarada em 1.4 |
| RULE-EV-04: FAIL adversarial → caso versionado | 1.5 (`FAIL → REGRESSED`) |
| RULE-EV-05: sem limiar de convicção | 1.8; F1 não tem convicção (J-001 intocada) |
| RULE-EV-07: externo subordinado, nunca baseline | 1.8; nenhuma métrica externa importada (ADV-KFH-13) |
| SPEC-020 Non-goal: tooling de runtime fora; SPEC-045-RUNTIME-001 não antecipada | 1.6 (só a prova por item, já da SPEC-007; métricas agregadas INDETERMINADO) |
| Schema lógico: enum `lente` com 9 valores | 1.5: enum não muda; o registro usa os nomes de campo, sem ser instância |
| RULE-KFH-005: parte D "ANTES de qualquer juízo por modelo" | 1.2 item 1 |
| RULE-KFH-006: independência, IDs pela CIM, expressão de seis conjunções, precedência, limite RULE-MET-01, limiares INDETERMINADO | 1.2 itens 2, 3, 6; 1.7 |
| BASpec-KFH-006: "o juízo nunca é o gate final" | 1.2 item 4; 1.8 |
| INV-KFH-01 / ADV-KFH-01: sem selo/VALIDADO, nada chega ao KG pelo caminho (b) | 1.2 item 5 e grupo (B) |
| EC-KFH-003/004: registro de validação e selo reconstruíveis | 1.6 |
| RULE-CKG-010: caminho (a) ≠ caminho (b) | 1.3 (F1 só no caminho (b)) |
| CC-11/CC-12: aplicação prospectiva | 1.2 (sem reconferência das homologadas) |
| ERRATUM-SPEC020-001: demais B "fecham nos pontos de dependência próprios" | 1.9; seção 3 (nota de leitura, sem editar) |
| SPEC-048 "Termo 4": F2 ≠ F1 | Seção 3; grupo (B) remete a entrega à F2 |

Nenhuma obrigação herdada foi removida ou enfraquecida. `[INFERÊNCIA — conferido lendo os textos citados]`

---

## 6. Constitution Check (CC-01..CC-12) — só o que o erratum toca

| CC | Resultado | Por quê |
|---|---|---|
| CC-01 | PASS | Hierarquia não muda; F1 só admite `learning` (herdado da SPEC-007); nenhuma hipótese criada |
| CC-02 | PASS | Não redefine CEM/CHM/CCM/CDM/CNM; conhecimento formado não é Evidência (INV-06/INV-10 da SPEC-007 intactos); objetos canônicos do caminho (a) ficam fora (1.3) |
| CC-03 | PASS | Nenhum campo de convicção; J-001 intocada |
| CC-04 | PASS | Nenhuma Salvaguarda tocada; custo fora (INV-04) |
| CC-05 | PASS | CRITICAL (da SPEC-020) |
| CC-06/CC-07 | N/A | Não é Engineering Card |
| CC-08 | PASS | Seção 5, com evidência obrigação a obrigação |
| CC-09 | PASS | Limiares INDETERMINADO; limite RULE-MET-01 declarado (1.7); lacuna de calibração registrada por decisão de Andraus (Q-7) e lacuna de gate marcada [DECISÃO NECESSÁRIA] (seção 3); nenhum número; veredito não atribuído a gate inexistente (1.4) |
| CC-10 | PASS | "faithfulness" externo (SRC-RAGAS-01) ≠ F1 do SOT (fidelidade do formado à fonte citada) ≠ F2 (suporte do entregue) ≠ verdade; declarado em 1.7 e seção 3 |
| CC-11 | N/A | O erratum não cria BASpec com efeito; as Classes D (KFH-005) e H (KFH-006) são herdadas da SPEC-007 |
| CC-12 | N/A | Meta-harness sem escola (como a SPEC-020) |

---

## 7. §7-bis — Redução de viés (CRITICAL)

**Bloco A — pergunta adversarial (o critério da seção 1, única parte com efeito de avaliação):**
- *Se o critério estivesse errado, o que se veria?* (1) Uma Spec futura do grupo (A) que pula a parte D, aceita juiz igual ao formador ou fixa limiar de paper sairia com F1 = PASS no `checks.md`. Observável pelos casos herdados: Cenário-KFH-T06/T07 (literais), T09 e ADV-KFH-04/24 (independência), ADV-KFH-13 (limiar externo). (2) Uma Spec do grupo (B) que abre escrita no KG fora do selo sem ser apanhada: observável por ADV-KFH-01. (3) O erratum lido como fechamento da "RAG faithfulness" inteira: o BL-017 encerrado ou a F2 tratada como fechada no ROADMAP/RMR-001. (4) Leitura retroativa: alguém reabrindo a SPEC-006/007/048 por F1 com base neste erratum, sem ordem de Andraus — observável como pedido de reconferência, contrário a 1.2 (a etapa futura de revisão das specs pretéritas, se Andraus a ordenar, é ato à parte).
- *O ENTÃO pode ser conferido por um observador independente?* **Em parte.** A parte literal (1.4) é conferível por qualquer um com busca de texto. A parte de julgamento ("enfraquece em substância?") **não** é determinística: depende do Revisor como detector e da homologação de Andraus. Isso está declarado como lacuna (seção 3, Lacuna 2), não escondido.
- *Existe QUANDO satisfeito sem que o ENTÃO deva acontecer?* Sim, coberto: (a) Spec do grupo (B) — confere-se só o item 5; (b) Spec fora de (A) e (B) — não recebe estado F1 (1.5); (c) conhecimento do caminho (a) ou de experiência — fora de F1 (1.3).

**Bloco B — herança:** seção 5 (tabela obrigação a obrigação). Nenhuma obrigação sem evidência.

**Bloco C — epistêmico:**
- Não se afirma "conformidade a F1 garante fidelidade". Afirma-se só que ela é o critério de verificação; o mecanismo (parte D literal + juízo independente + gate determinístico em runtime) e o seu limite (RU-1; independência de identidade ≠ de erro) estão declarados (1.7). Não é afirmação causal nova.
- Não se afirma verificação determinística em tempo de Spec que não existe (1.4).
- INDETERMINADO usado em vez de número: limiares, métricas agregadas, eficácia do juiz.
- Nenhuma probabilidade nem precisão numérica declarada.
- Premissa que pode estar errada: que "fecha em SPEC-007" do baseline autoriza um critério por metade. Base: DHR-SPEC007-002 §4 ("a dimensão se **divide**") e DHR-SPEC007-003 P-5 ("Uma emenda por metade"). `[FONTE]`

**Bloco D:** o erratum avalia; não executa nada nem cruza para a execução (INV-05). Toda dependência de Andraus está marcada como pergunta ou [DECISÃO NECESSÁRIA] (seções 3, 4 e 10).

---

## 8. Análise de impacto (RULE-HG-04) e compatibilidade proposta

**Quem passa a ter obrigação nova (prospectiva — não retroage):**

| Quem | Obrigação nova | Desde quando |
|---|---|---|
| Spec/errata do grupo (A) — formação pelo caminho (b), ou mudança desse caminho (ex.: futura errata da SPEC-007) | Itens 1–6 e linha "Dimensão B — F1" no próprio `checks.md` | Homologada depois deste erratum |
| Spec/errata do grupo (B) — cujo escopo inclua admitir ou consumir carimbado, ou mudar esse caminho (ex.: futuras erratas da SPEC-006/SPEC-048 que tratem disso; slot SPEC-049, se aberto); errata alheia à admissão/consumo não é sujeita *[v1.1: "admite ou consome carimbado (ex.: futuras erratas da SPEC-006/SPEC-048; slot SPEC-049, se aberto)"]* | Item 5 (literal: só INV-KFH-01 ou equivalente) e a mesma linha no `checks.md` | Homologada depois deste erratum |
| Revisor | Conferir essa linha nas Specs dos grupos (A)/(B), como detector (1.4) | Pareceres sobre essas Specs |
| SPEC-006, SPEC-007, SPEC-048 homologadas | **Nenhuma** — sem reconferência | — |
| Demais Specs | **Nenhuma** | — |

| Alvo | Impacto |
|---|---|
| Schemas | Nenhum. O enum `lente` e os estados do D5 não mudam |
| RAG / KG | Nenhum. Usa por referência RULE-KFH-005/006, INV-KFH-01 e RULE-CKG-010; não altera SPEC-006/007 |
| Skills | Nenhuma |
| Testes | Nenhum teste nem script novo. Só Specs dos grupos (A)/(B) registram a linha "Dimensão B — F1" no próprio `checks.md` |
| Modelos dependentes | SPEC-020, SPEC-007, SPEC-048, ERRATUM-SPEC020-001: texto não alterado. ROADMAP §12 (linha das dimensões B) e caminho crítico ("007 RAG (fecha 020: RAG faithfulness)"), RMR-001 (nota em BL-017) e CATALOGO: atualização aditiva **pelo Orquestrador, na homologação**, não por este erratum |
| Re-apontamentos em SPEC-021/SPEC-038 | Fora deste erratum: são da errata de re-apontamento (DHR-RETRO-001 §1, item (3)) |

**Alcance decidido:** prospectivo — "só daqui em diante" (Andraus, Q-3, DHR-RETRO-001 §7). A "etapa futura de revisão das specs pretéritas" é intenção de Andraus **sem ordem nem escopo**; não entra nesta análise. `[FONTE]`

**Compatibilidade proposta: Minor** — proposta do Especificador, **a confirmar na homologação** (DHR-RETRO-001 §7). `[PROPOSTA]`
- *A favor de Minor:* (1) a aplicação é **prospectiva** e **não retroage** — nenhuma Spec homologada ganha ou perde conformidade; (2) o critério cai numa dimensão que **não era avaliada** (DIFERIDA), então nada que antes passava passa a reprovar; (3) não muda regra, lente, estado, transição nem schema; (4) precedentes de critérios novos e prospectivos foram Minor: CLASSE-MECH-001 (RULE-MECH-01..04, "compatibilidade Minor", "prospectiva desde SPEC-002") e PRINC-BID-001 (RULE-PD-01..03, "compatibilidade Minor", "prospectiva desde SPEC-002") — registros no topo do `governance/RULES.md`; e o ERRATUM-SPEC020-001, na homologação Minor da DHR-SPEC038-002.
- *A favor de Major (para Andraus pesar):* cria obrigação nova para Specs futuras dos grupos (A)/(B) e mais um item para o Revisor. As erratas restritivas da SPEC-006 (v1.11 e v1.13) foram Major (DHR-SPEC006-003 D3; DHR-SPEC006-005). A diferença: lá o KG passava a **recusar o que aceitava**, com efeito sobre o baseline vigente; aqui não há efeito sobre nada já homologado. `[INFERÊNCIA]` *[v1.1 tinha um 3º item, "Se Andraus preferir reconferência … Major" — ramo encerrado pela resposta Q-3; texto no Anexo V1.1]*

---

## 9. Forma de aplicação (depois da homologação) — decidida (Q-4 = forma A, DHR-RETRO-001 §7)

**Arquivo à parte + uma linha no plano** (mesmo padrão do ERRATUM-SPEC020-001 e da Q-8 da errata v1.13 da SPEC-006): este arquivo **é** o erratum. O plan.md da SPEC-020 recebe **uma linha** ao final, logo depois da linha "**Errata aditiva (2026-10-03, DHR-SPEC038-002)**", apontando para este arquivo. Texto proposto da linha:

> **Errata aditiva (data da homologação, ata a atribuir):** dimensão B "RAG faithfulness", **metade F1** (conhecimento formado) — critério verificável = conformidade a F1 da SPEC-007 (RULE-KFH-005/006), aplicação prospectiva, limiares INDETERMINADO — ver `governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md`. Texto acima não alterado (INV-09); metade F2 (SPEC-048) e decision traceability (SPEC-014) permanecem diferidas.

O `checks.md` da SPEC-020 **não** é editado: este erratum o cobre por referência. A "data da homologação" e a ata da linha acima são preenchidas pelo Orquestrador no ato. *[v1.1 descrevia também a "Forma B" (notas em cada enunciado, proposta no Plan da SPEC-048) — ramo encerrado pela resposta Q-4; texto no Anexo V1.1]*

---

## 10. Perguntas para Andraus

**Respondidas (DHR-RETRO-001 §7, Adendo 4, chat 2026-10-30) — incorporadas acima, sem ramo condicional:**
- **Q-2:** critério definido, limiares INDETERMINADO; o Revisor dá o veredito como detector até existir gate → 1.4, 1.9, seção 3 (Lacuna 2).
- **Q-3:** só daqui em diante (prospectiva); "Teremos uma etapa futura de revisão das specs pretéritas" = intenção futura, sem ordem nem escopo, não é decisão aberta nova → 1.2, seção 8. Classificação Minor = proposta, a confirmar na homologação → cabeçalho, seção 8.
- **Q-4:** arquivo à parte + uma linha no plano da SPEC-020 → seção 9.
- **Q-7:** só registrar a lacuna (dependência de futura errata da SPEC-007) → seção 3 (Lacuna 1).
- **Q-8:** ver linha abaixo.

*[v1.1: as linhas Q-2, Q-3, Q-4 e Q-7 eram perguntas com opções — texto no Anexo V1.1]*

**Pendentes para a homologação** (premissa usada no texto até a resposta; a linha Q-8 fica só como registro — já respondida, DHR-DOCSYNC-003):

| # | Pergunta | Premissa / recomendação |
|---|---|---|
| Q-1 | Homologar o texto da seção 1 (critério da metade F1)? | Premissa: sim — o texto está escrito como vai valer |
| Q-5 | Aceitar o ajuste ao "texto único" da SPEC-048 ("F2: DIFERIDA até o erratum à parte — DHR-SPEC048-002 §3", no lugar de "na homologação do Plan da SPEC-048") e pedir que o erratum da metade F2 use a mesma redação? | Premissa: sim — seções 1.9 e 3 já usam a redação ajustada |
| Q-6 | Confirmar o código ERRATUM-SPEC020-002? | Premissa: sim — o arquivo e a linha da seção 9 usam esse código |
| Q-8 | **Respondida** (Andraus, 2026-10-30, DHR-DOCSYNC-003, item a: AGENTS.md §7 saneado); nada a decidir neste erratum. *[v1.1: "O AGENTS.md §7 ainda lista SPEC-020-PRINC-001 entre as ativas, contra o ROADMAP e a DHR-SPEC020-001 (efetiva desde 2026-09-27). Sanear o AGENTS.md §7 (arquivo protegido — só por decisão sua) em ato à parte?"]* | — (segue valendo: a ordem de serviço tira o estado das decisões só do ROADMAP) |
| Q-9 | Gate determinístico para a parte literal de F1 em tempo de Spec (seção 3, Lacuna 2): (a) só registrar; (b) pedir proposta em `governance/propostas/MELHORIAS-PROCESSO/` (com MECANISMOS.json no PR, se virar mecanismo) | Premissa: (a) — o texto só registra a lacuna; (b) se aparecer a primeira Spec do grupo (A) |

---

## 11. Tabela fato → locais (P2) — cada fato que se repete e onde ele aparece

Numa correção futura, corrigir **todos** os locais da linha. (O Anexo V1.0 é texto preservado e não entra nesta tabela.)

| Fato | Locais neste erratum | Âncoras no baseline (não editadas) |
|---|---|---|
| Metade F1 = conformidade a RULE-KFH-005 (antes) e RULE-KFH-006 (depois) | §0; 1.1; 1.2 itens 1–3; Herança INHERITS/tabela; linha proposta (§9); Q-1 | SPEC-007: RULE-KFH-005, RULE-KFH-006, seção "Proposta de emenda pontual à SPEC-020 … metade F1"; SPEC-020: D0 "O que a Missão NÃO é", D1 Non-goals |
| Aplicação prospectiva; sem reconferência das SPEC-006/007/048; grupos (A)/(B); demais sem obrigação | §0; 1.2; 1.5 (Spec não sujeita); §7-bis Bloco A (4); seção 8 (tabela "Quem" e Minor/Major); linha proposta (§9); Q-3 | RULES.md, registros de CLASSE-MECH-001 e PRINC-BID-001 ("prospectiva") |
| Fora de F1: caminho (a) e conhecimento de experiência (K-001 aberta) | 1.3; CC-02; Herança tabela (RULE-CKG-010); §7-bis Bloco A (c) | SPEC-006: RULE-CKG-010; ROADMAP "Decisões abertas ativas" (K-001) |
| Parte literal × parte de julgamento, **divididas por grupo** — literal (A) = RULE-KFH-005/006, INV-KFH-01, `judge_model_id ≠ former_model_id`, códigos `KC_*`/`JUDGE_NOT_INDEPENDENT`/`MODEL_ID_UNAUTHENTICATED`, sem limiar numérico; literal (B) = só INV-KFH-01 ou equivalente; "sem caminho que contorne o selo" = julgamento nos dois grupos; veredito do Revisor como detector; vigência só de Andraus | 1.2 (itens e grupos); 1.4; 1.5 ("1–6 em (A); só 5 em (B)"); 1.8; Herança (D6, RULE-EV-02; linha D5); seção 8 (tabela "Quem"); CC-09; §7-bis Bloco A/C; Q-2 | SPEC-020: D6 passos 7 e 8; D5 tabela de estados; schema `veredito_por`; RULE-EV-02 |
| Sem gate determinístico para F1 em spec-time (lacuna) | 1.4; seção 3 (Lacuna 2); CC-09; §7-bis Bloco A; Q-9 | — |
| Estados só do D5, sem estado/transição nova; Spec não sujeita não recebe estado; registro "Dimensão B — F1" no `checks.md` | §0; 1.5; Herança ADDED/MODIFIED/tabela; seção 8 (Testes, Schemas) | SPEC-020: D5 (estados e transições); I/O Schema "Resultado de avaliação de lente" |
| Enum `lente` inalterado; F1 não é 10ª lente | §0; 1.5; Herança tabela; seção 8 (Schemas) | SPEC-020: I/O Schema |
| Limiares/métricas agregadas = INDETERMINADO até calibração com amostra; nenhum número | §0; 1.2 item 6; 1.6; CC-09; §7-bis Bloco C; linha proposta (§9) | SPEC-007: RULE-KFH-006 ("Limiares/métricas agregadas …"), ADV-KFH-13; DHR-SPEC007-001 Q5; DHR-SPEC007-003 P-5 |
| Juízo nunca é gate final (runtime) | 1.2 item 4; 1.8; Herança tabela | SPEC-007: BASpec-KFH-006 CRITÉRIO 4Es |
| Metade F2 fora deste erratum; DIFERIDA até erratum à parte | §0; 1.2 grupo (B); 1.9; seção 3; §4 BL-017; linha proposta (§9); Q-5 | SPEC-048: "Proposta de emenda pontual à SPEC-020 … metade F2"; DHR-SPEC048-002 §3 |
| *decision traceability* DIFERIDA (SPEC-014) | §0; 1.9; seção 2; §4; linha proposta (§9) | SPEC-020: D0, D1, lista final, errata ao fim; ERRATUM-SPEC020-001 |
| A dimensão "RAG faithfulness" inteira não fecha; BL-017 não fecha (PARCIAL; `Em espera`) | §0; 1.9; seção 2 (Riscos); §4; §7-bis Bloco A (3) | RMR-001 BL-017; SPEC-007 "Nota de gate" (Disposição PARCIAL) |
| ADV-EV-06 vale para F2 e *decision traceability*; não para F1 | 1.9; seção 2; Herança tabela | SPEC-020: ADV-EV-06; Riscos "Classe B tratada como fechada" |
| Limite: F1 ≠ verdade da fonte ≠ relevância; independência de identidade ≠ de erro; RU-1 | 1.7; CC-10; §7-bis Bloco C | SPEC-007: RULE-KFH-006 "LIMITE (RULE-MET-01)", ADV-KFH-03 |
| Respostas de Andraus Q-2/Q-3/Q-4/Q-7 (DHR-RETRO-001 §7); Q-1/Q-5/Q-6/Q-9 pendentes com premissa; intenção futura de revisão das specs pretéritas (sem ordem nem escopo) | Cabeçalho ("Respostas de Andraus incorporadas"; "Compatibilidade proposta"); 1.2; seção 3 (Lacunas 1 e 2); CC-09; seção 8; seção 9; seção 10 | DHR-RETRO-001 §7 |
| Lacuna de calibração: sem auditoria amostral do juiz F1; só registrada (Q-7), dependência de futura errata da SPEC-007 | Seção 3 (Lacuna 1); CC-09; Q-7 (respondida) | SPEC-007: ADV-KFH-03 (RU-1), EC-KFH-004; SPEC-048: RULE-RET-011 (só F2) |
| Ajuste ao "texto único" da SPEC-048 | Seção 3; 1.9; Q-5 | SPEC-048: "Texto único por linha da SPEC-020 — coordenado com a metade F1"; DHR-SPEC048-002 §3 |
| Leitura vigente da frase do ERRATUM-SPEC020-001 | Seção 3; Herança tabela | ERRATUM-SPEC020-001, "O que NÃO muda" |
| Estado das decisões tirado só do ROADMAP; SPEC-020-PRINC-001 (FECHADA, efetiva) fora da lista de abertas; AGENTS.md §7 saneado (DHR-DOCSYNC-003) *[v1.1: "AGENTS.md §7 defasado"]* | Cabeçalho "Fonte do estado das decisões"; §4 (lista e nota); Q-8 (respondida); registro de mudanças (M-1; m-1 do R2) | ROADMAP "Decisões abertas ativas" e "Decisões FECHADAS"; DHR-SPEC020-001 item 1; AGENTS.md §7; DHR-DOCSYNC-003 item a |
| Abertas registradas só em ata (CKG-STRUCT-ORIGIN-001; produtor/gatilho de promoção) e mecanismo de assinatura | §4 | DHR-SPEC048-002 §5; ROADMAP "Decisões FECHADAS" (Autenticação dos atos) |
| Compatibilidade proposta Minor | Cabeçalho; seção 8; Q-3 | RULES.md (CLASSE-MECH-001, PRINC-BID-001); DHR-SPEC038-002; DHR-SPEC006-003 D3; DHR-SPEC006-005 |
| Forma A: uma linha ao fim do plan.md | Seção 9; Q-4; seção 14 (assertivas) | SPEC-020: linha "**Errata aditiva (2026-10-03, DHR-SPEC038-002)**" |

---

## 12. Pesquisa (RULE-ECC-02) — não aplicável a este ato

Este erratum não é abertura de Spec: aplica um critério já pesquisado e homologado no Dossiê da SPEC-007 (research §2/§3.5 — SRC-RAGAS-01, SRC-FAITHJUDGE-01, SRC-ALCE-01; classificação e capturas lá). Nenhuma fonte externa nova foi consultada nem importada; as citadas seguem `[EXTERNO]`, DADO, nunca baseline (RULE-EV-07; DHR-PROV-WEB-001 §2.1). `[FONTE: SPEC-007 plan.md "Dependências técnicas"]`

---

## 13-A. Registro de mudanças v1.1 → v1.2 (parecer R2 e DHR-RETRO-001 §7)

| Achado / decisão | O que mudou |
|---|---|
| N-1 (Média) | 1.4 "Parte literal" dividida por grupo: (A) = conjunto da v1.1; (B) = só INV-KFH-01 ou equivalente. "Sem caminho que contorne o selo" passou à parte de julgamento, nos dois grupos. Propagado: tabela do §8 (coluna "Obrigação nova" do grupo (B)) e linha "Parte literal × parte de julgamento" do §11. Conferidas as demais seções que enumeram o que se confere (1.2, 1.5, §7-bis Bloco A): já estavam divididas |
| m-1 (Menor) | Nota do §4, [FONTE] da nota, Q-8 (Respondida) e linha do §11: AGENTS.md §7 saneado por Andraus (DHR-DOCSYNC-003, item a); texto da v1.1 entre colchetes |
| m-2 (Menor) | Aplicado pelo Orquestrador (ficha M) na v1.1 e mantido (linha D5 da tabela de herança) |
| m-3 (Menor) | Grupo (B) com o mesmo gatilho de escopo do (A) ("cujo escopo inclua admitir … ou consumir …"), em 1.2 e na tabela do §8; errata alheia à admissão/consumo não é sujeita |
| Adendo 4 (DHR-RETRO-001 §7) | Q-2, Q-3, Q-4 e Q-7 respondidas e incorporadas sem ramo condicional: cabeçalho (nova linha "Respostas de Andraus incorporadas"; "Compatibilidade proposta"), 1.2 (prospectiva decidida; intenção futura de revisão das specs pretéritas, sem ordem nem escopo, sem decisão aberta nova), seção 3 (Lacuna 1 só registrada; Lacuna 2 com o estado confirmado), CC-09, seção 8 (alcance decidido; ramo "reconferência → Major" retirado), seção 9 (forma A decidida; "Forma B" retirada), seção 10 (Q-1, Q-5, Q-6, Q-9 pendentes com premissa), §11 (linha nova) |

## 13. Registro de mudanças v1.0 → v1.1 (parecer R1)

| Achado | O que mudou |
|---|---|
| M-1 (Média) | §4: a lista de abertas sai só do ROADMAP ("Decisões abertas ativas"), com [FONTE] por linha; CKG-STRUCT-ORIGIN-001 e "produtor/gatilho de promoção" ficam com fonte de ata (DHR-SPEC048-002 §5); mecanismo de assinatura com fonte no ROADMAP. SPEC-020-PRINC-001 saiu da lista de abertas; a nota de divergência foi reescrita (fechada no ROADMAP e efetiva na DHR-SPEC020-001; AGENTS.md §7 defasado; saneamento de Andraus). Cabeçalho "Fonte do estado das decisões"; Q-8 refeita. Redação "ID (FECHADA, …)" para não disparar o `check_doc_sync` |
| M-2 (Média) | Nova 1.4: parte literal × parte de julgamento; Revisor como detector (D6 passo 7); `veredito_por = revisor`; vigência só de Andraus; lacuna "sem gate determinístico" (seção 3, Lacuna 2; Q-9). Saíram "nunca de um LLM" (antiga 1.5) e "sem juízo de LLM" (§7-bis Bloco A) |
| M-3 (Média) | Nova 1.5: caminho de estados só com transições do D5; Spec não sujeita não recebe estado (sai "não aplicável" como estado); registro "Dimensão B — F1" no `checks.md` da Spec sujeita, sem ser instância do schema (ADDED); MODIFIED declara "nenhum estado/transição" |
| M-4 (Média) | Nova 1.2: aplicação prospectiva (molde CC-11/CC-12), sem reconferência das SPEC-006/007/048; grupos (A)/(B) enumerados; demais Specs sem obrigação. §8: tabela "Quem passa a ter obrigação nova" e análise Minor/Major refeita (precedentes CLASSE-MECH-001/PRINC-BID-001); Q-3 inclui o alcance |
| m-5 (Menor) | Nova 1.3: caminho (a) e conhecimento de experiência fora de F1, sem decidir K-001 |
| m-1..m-4 | Aplicados pelo Orquestrador (ficha M) na v1.0 e mantidos (Q-2; INHERITS com ADV-KFH-01 e EC-KFH-004; "admite ou consome" — agora no grupo (B) de 1.2; mitigações do ADV-KFH-03 na Lacuna 1) |
| Renumeração | Antigas 1.3/1.4/1.5/1.6 viraram 1.6/1.7/1.8/1.9; referências internas atualizadas |

---

## 14. Verificação de spec deste erratum (feedback interno — NÃO é parecer do Revisor nem homologação)

- As âncoras foram conferidas por busca de texto (Grep/Read): SPEC-020 plan.md (D0, D1 Non-goals, D5, D6 passos 7–8, ADV-EV-06, Riscos, Etiquetagem, lista final, errata ao fim, I/O Schemas), `checks.md` e `research.md`; SPEC-007 plan.md (RULE-KFH-005/006, INV-KFH-01, BASpec-KFH-005/006, EC-KFH-003/004, T06–T09, ADV-KFH-01/03/04/05/13/24, seção da proposta F1, nota de gate do BL-017); SPEC-006 plan.md (RULE-CKG-010); SPEC-048 plan.md ("Termo 4", texto único, proposta F2, RULE-RET-009/010/011); `ROADMAP.md` ("Decisões abertas ativas", "Decisões FECHADAS", §12); `governance/RULES.md` (registros de CLASSE-MECH-001/PRINC-BID-001; RULE-EV-01..07); atas DHR-SPEC007-001/002/003/005, DHR-SPEC048-001/002, DHR-SPEC038-002, DHR-SPEC006-005, DHR-SPEC020-001, DHR-RETRO-001; RMR-001 BL-017; `scripts/check_doc_sync.py` (regra inline do D1).
- Nenhum ID novo de RULE/BASpec/EC/T/ADV; nenhum placeholder de ata com formato de ID; nenhum ID de decisão aberta seguido de "— FECHADA"/": FECHADA".
- **Assertivas para o Orquestrador/Revisor.** **Antes** da homologação: o `specs/features/SPEC-020/plan.md` não contém `ERRATUM-SPEC020-002` (assert-absent) e o `checks.md` não muda. **Depois** (Forma A): assert-present de **uma** linha nova ao final do plan.md apontando para este arquivo; nenhuma outra linha alterada.
- **Gates — o Especificador NÃO os executou (não tem Bash). Ficam para o Orquestrador:**
  - `python scripts/check_doc_sync.py` (detector já corrigido por DHR-DOCSYNC-003 item b; ERRO deve ser 0)
  - `python scripts/check_refs.py`
  - `python scripts/check_invariants.py governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md`
  - `python scripts/revisor_gate.py governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md`
  - `python scripts/validate_spec_sot.py specs/features/SPEC-020/plan.md` (o plan não muda)
  - `python scripts/backlog_triggers.py` (BL-017 deve seguir `Em espera`)
  - `python scripts/build_map.py` + `python scripts/build_map.py --check`
  - `python -m unittest discover -s tests`

"VERIFY" interno ≠ CONFORME ≠ homologação.

**Pronto para revisão (v1.2).** *[v1.1: "Pronto para revisão (v1.1)."]*

---

## Anexo V1.1 — trechos da v1.1 trocados na v1.2 (preservados — INV-07; NÃO VALEM MAIS)

A v1.1 inteira está no commit `9a3f0bf`. Trechos substituídos (os demais estão entre colchetes no próprio local):

- **1.4, Parte literal (N-1):** "**Parte literal** (busca de texto possível): presença, na Spec sujeita, das referências RULE-KFH-005, RULE-KFH-006 e INV-KFH-01 (ou de texto equivalente que as transcreva); presença da expressão `judge_model_id ≠ former_model_id` e dos códigos `KC_REPROVADO`, `KC_INDETERMINADO`, `JUDGE_NOT_INDEPENDENT`, `MODEL_ID_UNAUTHENTICATED`; ausência de número declarado como limiar de fidelidade (ADV-KFH-13)."
- **1.2, grupo (B) (m-3):** "**(B) Admissão ou consumo:** Spec/errata que **admite** (ex.: errata futura da SPEC-006, caminho (b)) ou **consome** (ex.: errata futura da SPEC-048; slot SPEC-049, quando aberto) conhecimento carimbado."
- **§8, 3º item (Adendo 4, Q-3):** "*Se Andraus preferir reconferência* (aplicar F1 também às SPEC-006/007/048 homologadas), a classificação deveria ser revista para Major, porque passaria a haver efeito retroativo possível. Recomendação: prospectiva (Q-3)."
- **§8, cabeçalho da compatibilidade (Adendo 4):** "**Compatibilidade proposta: Minor** `[PROPOSTA — Q-3]`."
- **§9 (Adendo 4, Q-4):** título "Forma de aplicação proposta (depois da homologação) `[PROPOSTA — Q-4]`"; "**Forma A (recomendada — …)**"; e "**Forma B (alternativa, proposta no Plan da SPEC-048):** notas aditivas em cada um dos enunciados da seção 2. Desvantagem: mais pontos de edição no baseline e mais chance de contradição entre eles (C01 recorrente — RETROSPECTIVAS, Especificador)."
- **§10, linhas Q-2/Q-3/Q-4/Q-7 (Adendo 4):** Q-2 "(a) critério definido … ou (b) fechável, mas só fechada depois da calibração com amostra e de um gate determinístico?" — rec. (a); Q-3 "Minor com aplicação prospectiva … ou reconferência das homologadas (e então Major)?" — rec. Minor, prospectiva; Q-4 "A … ou B …?" — rec. A; Q-7 "(a) só registrar …; (b) futura errata da SPEC-007 …; (c) BUILD" — rec. (a) com (b) anotada. Q-1/Q-5/Q-6 tinham só "Recomendação: Sim".
- **Seção 3, Lacuna 1 (Adendo 4, Q-7):** terminava em "`[DECISÃO NECESSÁRIA — Q-7]`".
- **CC-09 (Adendo 4):** "lacunas de calibração e de gate marcadas [DECISÃO NECESSÁRIA] (seção 3)".

---

## Anexo V1.0 — trechos da v1.0 trocados na v1.1 (preservados — INV-07; NÃO VALEM MAIS)

A v1.0 inteira está no commit `ca724ed`. Trechos substituídos:

- **§1.2, parágrafo final (M-3/M-4):** "Uma Spec que não toca conhecimento formado registra a metade F1 como **não aplicável, com justificativa** (como os N/A do Constitution Check) — não aplicável ≠ PASS. O resultado da conferência usa os estados do D5 da SPEC-020 (`NOT_EVALUATED | DETECTED | PASS | FAIL | INDETERMINADO | REGRESSED`) e é registrado no `checks.md` da Spec avaliada. **O enum `lente` do schema lógico não muda** (a metade F1 não é uma 10ª lente)."
- **§1.2, abertura (M-4):** "Uma Spec cujo escopo inclua **formar conhecimento a partir de fonte com destino à memória permanente**, ou **mudar esse caminho**, satisfaz a metade F1 se — e só se — mantiver, sem enfraquecer:"
- **§1.5 (M-2):** "RULE-EV-02 (…) e RULE-EV-03 seguem intactas: em spec-time, a conferência dos itens 1–6 é do gate determinístico/Revisor, nunca de um LLM; em runtime, o juiz F1 é etapa de Classe H cujo resultado passa pelo gate determinístico da RULE-KFH-006 (item 4)."
- **§4, lista de abertas (M-1):** "**Permanecem ABERTAS** (nenhuma fechada por este erratum): K-001 · J-001 · M-001 · N-001 · G-001 · C-001 · WF-D03 · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · SPEC-020-PRINC-001 (nos termos da ordem de serviço desta tarefa e da linha \"Decisões abertas ativas\" do AGENTS.md §7; o ROADMAP prevalece em divergência — ver nota). Também abertos: \"produtor/gatilho de promoção\" e o mecanismo de assinatura dos atos de Andraus (BUILD). `[FONTE: DHR-RETRO-001 §3; DHR-SPEC048-002 §5; DHR-SPEC006-005 §4]`"
- **§4, nota de divergência (M-1):** dizia que a linha "Decisões FECHADAS" do ROADMAP lista a SPEC-020-PRINC-001 como fechada (com a citação literal do ROADMAP — *omitida aqui porque a forma "ID + travessão + FECHADA" dispara o `check_doc_sync`; texto literal no commit `ca724ed`*), "enquanto o AGENTS.md §7 e a ordem de serviço a listam como aberta. Este erratum **não toca** SPEC-020-PRINC-001 em nenhum dos dois sentidos."
- **§7-bis Bloco A, 2º item (M-2):** "Sim. Os itens 1–6 da seção 1.2 são presença/ausência de regras literais (busca de texto + leitura do gate de saída), sem juízo de LLM."
- **§8, "A favor de Minor" (M-4):** "acrescenta critério a uma dimensão que **não era avaliada** (estava DIFERIDA); nada que antes passava passa a reprovar. Não muda regra, lente nem schema. A única Spec hoje no escopo (SPEC-007) já cumpre os itens 1–6 por construção. Precedente direto: o ERRATUM-SPEC020-001, que fez o mesmo para *tool correctness*, entrou numa homologação classificada como Minor (DHR-SPEC038-002, \"Compatibilidade\")."
- **§8, linha "Testes" (M-4):** "Nenhum teste novo. Specs que formam conhecimento passam a registrar a conferência F1 no próprio `checks.md` (a SPEC-007 já o faz)"
- **Q-8 (M-1):** "Saneamento da divergência sobre SPEC-020-PRINC-001 (aberta no AGENTS.md §7 e na ordem de serviço; FECHADA no ROADMAP): tratar em ato à parte? | Sim, fora deste erratum"
