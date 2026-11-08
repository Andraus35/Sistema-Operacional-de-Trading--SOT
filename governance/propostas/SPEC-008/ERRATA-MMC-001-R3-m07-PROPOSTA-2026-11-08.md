# Errata aditiva ao MMC-001 v1.0 — condição R3-m07 (orientação × obrigação na Classe da Fase 1) — PROPOSTA

| Campo | Valor |
|---|---|
| Alvo | `governance/MMC-001_Manager_Contract.md` — **MMC-001 v1.0, BASELINE** (Andraus, 2026-11-08, `DHR-SPEC008-002`) |
| Origem | Condição da homologação: `DHR-SPEC008-002` §4 (opção (a), errata aditiva "em passo à parte e por ordem de Andraus"); achado **R3-m07** (Menor, C02, classe O, não bloqueante) em `governance/propostas/SPEC-008/PARECER-REVISOR-MANAGER-CONTRACT-R3-2026-11-07.md` l.19 e l.31 |
| Ordem | Andraus, chat 2026-11-08: "Aplicar a errata do R3-m07" (repassada pelo Orquestrador, CLASSE-TAREFA O) |
| Autor | Especificador Principal SOT |
| Data | 2026-11-08 |
| Status | **PROPOSTA** — não aplicada ao baseline. Só vigora com homologação de Andraus (INV-09; RULE-HG-02/03). Nenhuma decisão aberta é fechada (CONS-01). |
| Rodada | R2 — correção do parecer R1 (`PARECER-REVISOR-ERRATA-MMC-001-R3-m07-R1-2026-11-08.md`, NÃO CONFORME, 1 Média): ER1-M01 (§3), ER1-m02 (alvo 3), ER1-m03 (alvo 4 e §6), ER1-m04 (forma). ER1-m01 aplicado pelo Orquestrador (FICHA-M) na R1→R2, mantido. |
| Forma (precedente) | `DHR-SPEC006-005` (errata aditiva; texto anterior recuperável; compatibilidade declarada; condição explícita do que a homologação não afirma). **Divergência de forma declarada (ER1-m04):** aquela ata aplicou a errata como **arquivo à parte + ponteiro de uma linha** no Status, que "não altera texto baselined do plan.md/checks.md" (DHR-SPEC006-005 l.10; D2, l.19). Esta proposta, como redigida no §2, substitui células **no próprio lugar**, com `[antes]` (INV-07). As duas formas estão no §7; a escolha é de **Andraus** `[DECISÃO NECESSÁRIA]`. *[antes: "`DHR-SPEC006-005` (errata aditiva; texto anterior recuperável; compatibilidade declarada; condição explícita do que a homologação não afirma)"]* |

---

## 1. Escopo e alvo

`[FATO]` Achado R3-m07 (parecer R3, l.19): "§3.1.3/§8.2-bis tratam como obrigação a Classe D/C que `ABERTURA.md` §4 (l.140, l.25) chama de orientação; só 'nenhuma H/P ⇒ volta a Andraus' (l.144) é firme; tensão com a coluna 'não herdável' do §3." Prevenção registrada (l.31): "Ao citar fonte nao-baseline, preservar a modalidade (orientacao x obrigacao) — RULE-SEM-03".

`[FATO]` Texto da fonte (`specs/features/SPEC-008/ABERTURA.md`, redação homologada "como está" por DHR-SPEC008-001; não-baseline):
- l.25 (§1, tabela de identificação — o pedido do Orquestrador e o parecer dizem "§3"/"§4"; a linha fica no §1): "| **Classe predominante** (orientação, não vinculante — CC-11 por BASpec) | **D** em tudo + **C** na trava constitutiva · **H/P: nenhuma** | ADR-MANAGER-001 §2.5 (Fase 1 mecânica). Ver §4. |"
- l.140 (título do §4): "## 4. Classe RULE-MECH-01 (CC-11) — orientação por tipo de BASpec"
- l.144: "**Classe H/P: nenhuma** — julgamento leve é das Fases 0/2 (ADR §2.5). Se o Plan precisar de julgamento, é sinal de escopo errado ⇒ volta a Andraus."

`[FATO]` Base da orientação não-vinculante: DHR-EUA-E23 l.32 — "\"Classe predominante\" é **orientação não-vinculante** (RULE-MECH-01/CLASSE-MECH-001 — a declaração normativa de Classe é por BASpec, SES-001 §50)". RULE-SEM-03 (RULES.md l.689): transformação semântica "NÃO DEVE eliminar modalidade/nuance material ('pode' ≠ 'será')".

**Alvos (únicos):**
1. MMC-001 §3.1 (tabela "Fase 1 é mecânica"), **linha 3.1.3** (arquivo l.72).
2. MMC-001 §8.2-bis (tabela de alcance), **linha "§3.1.3 (Classe D/C da Fase 1) · §6.6 — parte 'orçamento do ciclo' da P-7"** (arquivo l.169).
3. MMC-001 §8.3, bloco ADDED (c), **item "Classe D/C (§3.1.3) e 'orçamento do ciclo' da P-7 só para SPEC-008/Tempo"** (arquivo l.230) — alinhamento à nova linha de orientação do §8.2-bis (ER1-m02).
4. MMC-001 **cabeçalho** (arquivo l.3), trecho "condição R3-m07 na ata §3" → §4 (ER1-m03; a condição está na DHR-SPEC008-002 §4, l.40-42).

**Nada mais é tocado:** o restante do cabeçalho, §3 (tabela e coluna), §3.1.1/§3.1.2/§3.1.4, §3.2, §4–§8.2, demais linhas do §8.2-bis, demais itens do §8.3, §9–§14 ficam como estão. `[PROPOSTA]` *[antes: "**Nada mais é tocado:** cabeçalho, §3 (tabela e coluna), §3.1.1/§3.1.2/§3.1.4, §3.2, §4–§8.2, demais linhas do §8.2-bis, §8.3, §9–§14 ficam como estão."]*

---

## 2. Texto antigo → texto novo (aditivo; `[antes]` no próprio lugar — INV-07)

### 2.1 Linha 3.1.3 (MMC-001 l.72)

**Antigo (literal, linha inteira):**

```
| 3.1.3 | Na abertura homologada da SPEC-008: Classe **D** em tudo + **C** na trava constitutiva; **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus. **Alcance:** só SPEC-008 e Spec de Tempo (filha — A-2 DECIDIDO, Andraus, chat 2026-11-07; §8.2-bis). *[antes: "**Alcance:** só SPEC-008 e, se A-2 = sim, Spec de Tempo (§8.2-bis)."]* | `[FATO]` DHR-SPEC008-001 §1 (frase de abertura: respostas "confirmadas pela homologação da `ABERTURA.md` como está") e §4 (homologa a abertura); texto em ABERTURA.md §4 (não-baseline — ver cabeçalho) — a declaração por BASpec continua sendo do Plan *[antes: "`[FATO]` ABERTURA.md §4, homologada 'como está' (DHR-SPEC008-001 §1) — a declaração por BASpec continua sendo do Plan" (R1-M03)]* |
```

**Novo (proposto):**

```
| 3.1.3 | **Obrigação:** **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus. **Orientação (não vinculante — CC-11 por BASpec; não é obrigação):** na abertura homologada da SPEC-008, Classe **D** em tudo + **C** na trava constitutiva; a Classe de cada BASpec é declarada no Plan (RULE-MECH-01). **Alcance:** só SPEC-008 e Spec de Tempo (filha — A-2 DECIDIDO, Andraus, chat 2026-11-07; §8.2-bis). *[antes: "Na abertura homologada da SPEC-008: Classe **D** em tudo + **C** na trava constitutiva; **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus." — orientação D/C lida como obrigação (R3-m07; RULE-SEM-03)]* *[antes: "**Alcance:** só SPEC-008 e, se A-2 = sim, Spec de Tempo (§8.2-bis)."]* | `[FATO]` DHR-SPEC008-001 §1 (frase de abertura: respostas "confirmadas pela homologação da `ABERTURA.md` como está") e §4 (homologa a abertura); texto em ABERTURA.md l.25 ("orientação, não vinculante — CC-11 por BASpec") e §4 ("orientação por tipo de BASpec"; l.144 para a parte firme) (não-baseline — ver cabeçalho); parte firme = `[FATO]` DHR-SPEC008-002 §4 (que acolhe a leitura do parecer R3 l.19; parecer não é homologado) · base adicional: ADR-MANAGER-001 §2.5 (Fase 1 "sem julgamento analítico") — a declaração por BASpec continua sendo do Plan *[antes: "…; texto em ABERTURA.md §4 (não-baseline — ver cabeçalho) — a declaração por BASpec continua sendo do Plan"]* *[antes: "`[FATO]` ABERTURA.md §4, homologada 'como está' (DHR-SPEC008-001 §1) — a declaração por BASpec continua sendo do Plan" (R1-M03)]* |
```

Notas `[INFERÊNCIA]`:
- A célula fica numa coluna chamada "Obrigação"; por isso a parte de orientação é rotulada **dentro** da célula como "não é obrigação" — sem criar coluna nova.
- A l.144 da ABERTURA está sob o título "orientação por tipo de BASpec". A firmeza do "nenhuma H/P ⇒ volta a Andraus" vem da leitura do Revisor (R3 l.19) acolhida pela ata DHR-SPEC008-002 §4 ("só 'nenhuma H/P ⇒ volta a Andraus' é firme") e já decorre do ADR §2.5, que o §3.1.1/§3.1.4 herdam para todas as filhas. A errata não cria essa firmeza: só a mantém como estava no v1.0.
- O conteúdo do que a trava nega (não analisar, não criar hipótese, não calcular convicção, não mudar classe de modelo, não montar TMP/Signal Package, não emitir ordem) continua obrigação pelos §5.1–§5.5, §6.4 e §7, que já alcançam todas as filhas (§8.2-bis l.167). Só a **Classe C** como rótulo de mecanismo passa a ser orientação.

### 2.2 Linha do §8.2-bis (MMC-001 l.169)

**Antigo (literal):**

```
| §3.1.3 (Classe D/C da Fase 1) · §6.6 — parte "orçamento do ciclo" da P-7 | DHR-SPEC008-001 §1 (abertura "como está"; P-4..P-9) | **SPEC-008 e Spec de Tempo** (filha — A-2). Para SPEC-014/015: só o limite que já decorre do ADR §2.5 (não levar julgamento para a Fase 1), não as Classes de suas próprias BASpecs | `[INFERÊNCIA]` DHR-EUA-E23 §2 item 3 + DHR-SPEC008-001 §4 ("homologa a **abertura**" da SPEC-008) · filiação da Spec de Tempo = `[FATO]` A-2, Andraus, chat 2026-11-07 |
```

**Novo (proposto) — a mesma linha, mais uma linha logo abaixo (desdobramento da mesma linha; nenhum item novo do contrato):**

```
| §3.1.3 — parte **obrigação** ("nenhuma BASpec H/P na Fase 1; se o Plan precisar de julgamento, volta a Andraus") · §6.6 — parte "orçamento do ciclo" da P-7 | DHR-SPEC008-001 §1 (abertura "como está"; P-4..P-9) | **SPEC-008 e Spec de Tempo** (filha — A-2). Para SPEC-014/015: só o limite que já decorre do ADR §2.5 (não levar julgamento para a Fase 1), não as Classes de suas próprias BASpecs | `[INFERÊNCIA]` DHR-EUA-E23 §2 item 3 + DHR-SPEC008-001 §4 ("homologa a **abertura**" da SPEC-008) · filiação da Spec de Tempo = `[FATO]` A-2, Andraus, chat 2026-11-07 · parte firme = `[FATO]` DHR-SPEC008-002 §4 |
| §3.1.3 — parte **orientação** (Classe D em tudo + C na trava constitutiva) | ABERTURA.md l.25 e §4 (orientação por tipo de BASpec; não-baseline), homologada "como está" (DHR-SPEC008-001 §1) | **nenhuma** — orientação não-vinculante, não entra na conservação (mesmo regime da coluna "Classe predominante" do §3); a Classe é declarada por BASpec no Plan da SPEC-008 e no da Spec de Tempo (RULE-MECH-01; CC-11) | `[FATO]` ABERTURA.md l.25 ("orientação, não vinculante — CC-11 por BASpec") e l.140 · DHR-EUA-E23 l.32 (nota *) |
```

Preservação (INV-07), logo abaixo da tabela, junto ao bloco `[antes]` já existente (l.179) — **acréscimo**, sem alterar o bloco atual:

```
*[antes (errata R3-m07, linha §3.1.3 · §6.6-orçamento): "| §3.1.3 (Classe D/C da Fase 1) · §6.6 — parte \"orçamento do ciclo\" da P-7 | … | **SPEC-008 e Spec de Tempo** (filha — A-2). … | `[INFERÊNCIA]` DHR-EUA-E23 §2 item 3 + DHR-SPEC008-001 §4 … · filiação da Spec de Tempo = `[FATO]` A-2, Andraus, chat 2026-11-07 |" — a Classe D/C (orientação na fonte) entrava no alcance como obrigação (R3-m07; RULE-SEM-03)]*
```

### 2.3 §8.3 ADDED (c), item da Classe D/C (MMC-001 l.230) — alvo 3 (ER1-m02)

O item fica dentro do bloco cercado por ` ``` ` (MMC-001 l.183–l.240); a marca `[antes]` entra como linha de continuação, com o mesmo recuo, sem sair do bloco.

**Antigo (literal, linha inteira, com o recuo original):**

```
             · Classe D/C (§3.1.3) e "orçamento do ciclo" da P-7 só para SPEC-008/Tempo (DHR-EUA-E23 §2 item 3)
```

**Novo (proposto):**

```
             · Classe D/C (§3.1.3) = orientação, sem alcance vertical (errata R3-m07; ABERTURA.md l.25;
               DHR-EUA-E23 l.32); "orçamento do ciclo" da P-7 só para SPEC-008/Tempo (DHR-EUA-E23 §2 item 3)
               *[antes: "Classe D/C (§3.1.3) e "orçamento do ciclo" da P-7 só para SPEC-008/Tempo
               (DHR-EUA-E23 §2 item 3)" — D/C listada como alcance; R3-m07, ER1-m02]*
```

Notas `[INFERÊNCIA]`:
- O item continua no grupo (c) (`[INFERÊNCIA]` de alcance do §8.2-bis): "sem alcance" é leitura de alcance, com o mesmo fundamento da l.233 ("coluna 'Classe predominante' não herdável", base DHR-EUA-E23 §2 item 1, nota *). Não cria item novo no grupo; reescreve o existente.
- A parte "orçamento do ciclo" da P-7 fica com o texto e o alcance de antes.

### 2.4 Cabeçalho do MMC-001 (l.3) — alvo 4 (ER1-m03)

**Antigo (trecho literal):** `condição R3-m07 na ata §3`

**Novo (proposto):** `condição R3-m07 na ata §4 *[antes: "condição R3-m07 na ata §3" — a condição está na DHR-SPEC008-002 §4 (l.40-42); o §3 da ata é "O que esta ata NÃO afirma"]*`

Nota `[FATO]`: DHR-SPEC008-002 §4 (l.40-42) traz a condição; confirmado pelo parecer R1, ponto (7). Correção de referência cruzada. Como o MMC-001 é baseline, só entra por errata homologada (INV-09; o próprio l.3: "mudança só por errata homologada"), não por FICHA-M.

---

## 3. Compatibilidade (RULE-HG-04) — três hipóteses; escolha de Andraus `[DECISÃO NECESSÁRIA]`

`[FATO]` RULE-HG-04 (RULES.md l.382-384): "Toda proposta de alteração DEVE conter Análise de Impacto explícita sobre schemas, RAG, Skills, testes e modelos dependentes, e classificação de compatibilidade (Patch/Minor/Major)."

`[FATO]` Taxonomia canônica (canon/CR-001-compliance-record.md §7.7, l.437-441), literal:

| Nível | Definição (CR-001) | Efeito na Baseline (CR-001) |
|---|---|---|
| **Patch** | "Correções exclusivamente editoriais (ortografia, formatação, referências cruzadas, notas sem efeito normativo)" | "Não altera a versão" (l.439; CRR52, l.447: "Mudanças Patch Não Alteram Baseline") |
| **Minor** | "Mudanças compatíveis que adicionam comportamento sem invalidar comportamento anterior" | "Incremento Minor (ex.: 1.0 → 1.1)" (l.440) |
| **Major** | "Mudanças que removem, invalidam ou alteram comportamento normativo vigente" | "Nova baseline major (ex.: 1.0 → 2.0)" (l.441); CRR56 (l.451): quebra "deve ser explicitamente declarada como Major" |

**Análise de impacto (igual nas três hipóteses)** `[INFERÊNCIA]`: schemas — nenhum; RAG — nenhum; Skills — nenhuma; testes — nenhum (nenhum teste cita §3.1.3, §8.3 (c) ou o cabeçalho); modelos dependentes — nenhum. Consumidores do texto: o Plan da SPEC-008 e o da Spec de Tempo **não começaram** (ROADMAP l.524: "Plan pendente, só por ordem de Andraus"); SPEC-014/015 não estão abertas. Gates do Plan: CC-11 e `[STRUCT-14]` continuam exigindo Classe por BASpec — inalterados. A parte firme ("nenhuma H/P ⇒ volta a Andraus") não muda nem de modalidade nem de alcance (§4).

**Alvo 4 (cabeçalho l.3, "ata §3" → §4):** é correção de **referência cruzada** — cabe literalmente em Patch em qualquer das hipóteses abaixo `[INFERÊNCIA]`. As hipóteses tratam dos alvos 1–3 (modalidade da Classe D/C).

### 3.1 Hipótese Patch (sem mudança de versão)

- **Base possível — regra de leitura do MMC-001 §1 (l.23):** "Se algum item daqui divergir do texto-fonte citado, vale o texto-fonte e a divergência é achado a corrigir aqui". O texto-fonte citado pela l.72 é a ABERTURA (l.25: "orientação, não vinculante — CC-11 por BASpec"; l.140: "orientação por tipo de BASpec"). Por essa regra, já no v1.0 a obrigação D/C **nunca prevaleceu** sobre a fonte: o que valia era a orientação. A errata, então, só corrige a **transcrição** ("achado a corrigir aqui") e não altera comportamento normativo vigente — encaixe em "referências cruzadas, notas sem efeito normativo" (CR-001 l.439) `[INFERÊNCIA]`.
- **Reforço:** a própria ata que tornou o texto vigente já registrou a condição: DHR-SPEC008-002 §4 (l.41-42) diz que §3.1.3/§8.2-bis "tratam como obrigação a Classe D/C que `ABERTURA.md` §4 (l.140, l.25) chama de orientação" e manda errata "preservando a modalidade (orientação × obrigação, RULE-SEM-03)" `[FATO]`. A homologação não acolheu a leitura "obrigação" sem reserva `[INFERÊNCIA]`.
- **Efeito na versão:** **nenhum** — continua **MMC-001 v1.0** (CR-001 l.439; CRR52). A errata é identificada pela ata que a homologar, não por número de versão. O marcador **"v1.0.1" é retirado**: a CR-001 não o prevê para Patch.
- **Riscos da leitura** `[INFERÊNCIA]`: (i) a regra do §1 se justifica por "RULE-HD-02/RULE-HV-03 — o herdado prevalece sobre o local", e a ABERTURA é **contexto, nunca herança** (MMC-001 l.15); a letra da regra ("texto-fonte citado") a alcança, mas a justificativa entre parênteses fala de herança — pode-se ler a regra como restrita a fontes herdadas; (ii) o texto homologado dizia "obrigação" em coluna chamada "Obrigação"; quem lê o baseline isolado viu uma obrigação. Se Andraus der peso a (i) ou (ii), a hipótese Patch fica fraca.

### 3.2 Hipótese Minor (1.0 → 1.1)

- **Encaixe na definição literal:** **não encaixa** `[INFERÊNCIA]`. Minor = "adicionam comportamento sem invalidar comportamento anterior" (l.440). A errata **não acrescenta** comportamento; ela **tira** da Classe D/C a força de obrigação (alvos 1–3). Os rótulos "Obrigação"/"Orientação" e a linha desdobrada do §8.2-bis não são comportamento novo.
- **Por que aparece:** a própria DHR-SPEC008-002 (l.10) classificou a homologação do MMC-001 como Minor; e a rodada R1 desta proposta a ofereceu como alternativa. Pela CR-001, essa alternativa não se sustenta para esta errata. Fica registrada para Andraus, sem recomendação.
- **Efeito na versão:** seria MMC-001 v1.1.

### 3.3 Hipótese Major (1.0 → 2.0)

- **Base possível:** se o **texto baselined** do v1.0 é lido como o comportamento normativo vigente (INV-09: mudança só por errata homologada), então a l.72 e a l.169 exigiam Classe D/C como obrigação para SPEC-008 e Spec de Tempo; passar isso a orientação **remove/altera** comportamento normativo vigente — encaixe literal em Major (l.441) `[INFERÊNCIA]`.
- **Precedente:** DHR-SPEC006-005 (l.9-10) classificou como **Major** uma errata aditiva com efeito normativo ("restringe o que o KG aceita") `[FATO]`. Aqui o efeito vai no sentido contrário (afrouxa), mas "alteram comportamento normativo vigente" cobre os dois sentidos `[INFERÊNCIA]`.
- **Cláusula CE2 / CRR54 (l.443, l.449):** Major opera "exclusivamente por sucessão — criação de identificadores novos"; redefinir texto de identificador `Vigente` é proibido por CRR36. O parecer R1 (§5, l.105) registra que a CRR36 não se aplica diretamente porque os itens do MMC são índice de leitura (§8.2), não identificadores da MIC. Mesmo assim, se Andraus escolher Major, a forma "arquivo à parte + ponteiro" (§7, opção B) fica mais próxima do espírito da sucessão do que a troca de células no lugar `[INFERÊNCIA]`.
- **Efeito na versão:** MMC-001 **v2.0**, com declaração explícita de Major (CRR56); cabeçalho, CATALOGO-OFICIAL e ROADMAP mudam na aplicação (fora desta errata — §6).
- **Contra a hipótese** `[INFERÊNCIA]`: nenhum consumidor existe (Plans não começaram), e a ata de homologação já registrava a reserva (§3.1, reforço). Major tem custo de nova baseline para corrigir uma transcrição que a própria ata apontou.

### 3.4 Estado da escolha

`[DECISÃO NECESSÁRIA]` **Andraus escolhe** Patch (v1.0 mantida), Minor (v1.1) ou Major (v2.0). O Especificador **não recomenda** nenhuma.

Contexto (segundo o repasse do Orquestrador; o chat não foi visto pelo Especificador): Andraus respondeu por AskUserQuestion "Patch v1.0.1 (Recomendado)", com base na descrição da R1 desta proposta. O parecer R1 (ER1-M01) mostrou que aquela descrição estava inconsistente com a CR-001 (Patch "não altera a versão"; Major não analisado). Por isso a resposta fica **pendente de reconfirmação** com as hipóteses corrigidas acima; ela não é registrada aqui como decisão.

*[antes (§3 da R1, integral): "## 3. Compatibilidade (RULE-HG-04) — `[PROPOSTA]` / **Classificação recomendada: Patch.** Justificativa `[INFERÊNCIA]`: - A errata **alinha o texto do contrato à modalidade da fonte** que a DHR-SPEC008-001 homologou \"como está\" (orientação). Não cria regra, campo, estado, transição, ID normativo nem agente de trading; não muda nenhuma fronteira, invariante ou alcance de outra seção. - O único efeito material é **deixar de exigir como obrigação** uma Classe que a fonte nunca exigiu. Nenhum consumidor foi construído sobre a leitura antiga: o Plan da SPEC-008 e o da Spec de Tempo **não começaram** (ROADMAP l.524: \"Plan pendente, só por ordem de Andraus\"); SPEC-014/015 não estão abertas. - **Análise de impacto:** schemas — nenhum; RAG — nenhum; Skills — nenhuma; testes — nenhum (nenhum teste cita §3.1.3); modelos dependentes — nenhum. Gates do Plan: CC-11 e `[STRUCT-14]` continuam exigindo Classe por BASpec — inalterados. / **Alternativa: Minor.** Leitura possível: o v1.0 é baseline e o texto homologado dizia \"obrigação\"; afrouxar uma obrigação baselined, mesmo sem consumidor, pode ser contado como mudança de conteúdo normativo. Escolha entre Patch e Minor = **Andraus**. Marcador de versão proposto: **MMC-001 v1.0.1** (Patch) ou **v1.1** (Minor) — `[PROPOSTA]`; a atualização do cabeçalho do MMC-001 não está nesta errata (§6)." — classificação incoerente com CR-001 l.437-441 (ER1-M01)]*

---

## 4. Verificação de alcance vertical — `[INFERÊNCIA]`

| Parte | Antes (v1.0) | Depois (errata) | Mudou? |
|---|---|---|---|
| "nenhuma BASpec H/P na Fase 1; se o Plan precisar de julgamento, volta a Andraus" | obrigação; SPEC-008 + Spec de Tempo; SPEC-014/015 só o limite do ADR §2.5 | **idem** (rotulada "Obrigação") | **não** — continua firme, mesmo alcance |
| Limite "não levar julgamento para a Fase 1" para SPEC-014/015 | via §3.1.1/§3.1.4 (todas as filhas) e §8.2-bis l.169 | **idem** | **não** |
| Classe D em tudo + C na trava | obrigação para SPEC-008 + Spec de Tempo | orientação; alcance "nenhuma" (como a coluna do §3) | **sim, só a modalidade** — correção para a da fonte (R3-m07) |
| Conteúdo negado pela trava (S12) | §5.1–§5.5, §6.4, §7 — todas as filhas | **idem** | **não** |
| Coluna "Classe predominante" (§3) | não herdável | **idem** | **não** — a tensão apontada pelo R3 deixa de existir, porque o §3.1.3 passa a dar à D/C o mesmo regime |

Conclusão: nada que permanece obrigação perde ou ganha alcance; a única mudança é de modalidade, no sentido da fonte (RULE-SEM-03). Nenhuma obrigação herdada do ADR, CEE-001, INV ou WORKFLOW é suprimida (RULE-HV-02/RULE-HD-03): a Classe D/C não vem de nenhum desses pais, vem da ABERTURA, que é só contexto (§8.3, "CONTEXTO (citado, NÃO herdado)").

**Compatibilidade com o §8.3:** o ADDED (c), l.230, passa a ser alvo 3 (§2.3): depois da errata, a Classe D/C aparece ali como "orientação, sem alcance vertical", igual à nova linha do §8.2-bis; a parte "orçamento do ciclo" da P-7 mantém o alcance SPEC-008/Tempo. O bloco Herança/Delta deixa de listar como acréscimo de alcance algo que não tem alcance (ER1-m02) `[INFERÊNCIA]`. *[antes: "**Compatibilidade com o §8.3 (não tocado):** o ADDED (c), l.230, diz \"Classe D/C (§3.1.3) e 'orçamento do ciclo' da P-7 só para SPEC-008/Tempo\". É frase de **restrição** de alcance (\"só para\"); não afirma que D/C é obrigação. Continua verdadeira depois da errata — `[INFERÊNCIA]`; não precisa de edição. Se Andraus quiser a redação explícita também ali, é outra errata."]*

---

## 5. Autopré-check (curto)

- [x] ROADMAP.md (l.524: estado SPEC-008/MMC-001) e atomic-spec.md (CC-10/RULE-SEM-03, l.291) consultados; ata DHR-SPEC008-002 §4, parecer R3 (l.19, l.31), ABERTURA.md (l.25, l.140, l.144) e precedente DHR-SPEC006-005 lidos.
- [x] Só §3.1.3 (l.72), §8.2-bis (l.169, + uma linha desdobrada e um `[antes]` acrescentado), §8.3 ADDED (c) (l.230) e o trecho "ata §3" do cabeçalho (l.3) — nenhuma outra seção. *[antes: "Só §3.1.3 (l.72) e §8.2-bis (l.169, + uma linha desdobrada e um `[antes]` acrescentado) — nenhuma outra seção."]*
- [x] Compatibilidade: três hipóteses contra CR-001 l.437-441 literal; sem "v1.0.1"; escolha com Andraus (§3.4). Forma de aplicação com Andraus (§7).
- [x] Texto antigo citado literalmente; texto substituído preservado em `[antes: …]` (INV-07).
- [x] Sem regra, campo, estado, transição, ID normativo ou agente de trading novo. "Orientação"/"Obrigação" são rótulos de modalidade já usados no contrato (§3 l.56, l.63; §8.2-bis l.168).
- [x] Parte firme mantida firme e com o mesmo alcance (§4).
- [x] CONS-01: nenhuma decisão aberta fechada (J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4, P-11, P-13, dono do Signal Package — intocados).
- [x] Etiquetas `[FATO]`/`[INFERÊNCIA]`/`[PROPOSTA]`/`[DECISÃO NECESSÁRIA]` aplicadas; Patch × Minor × Major deixado a Andraus. *[antes: "Etiquetas `[FATO]`/`[INFERÊNCIA]`/`[PROPOSTA]` aplicadas; Patch × Minor deixado a Andraus."]*
- [ ] `validate_spec_sot.py` não se aplica (não é plan.md). `check_refs.py` / `build_map.py --check` — a rodar pelo Orquestrador (o Especificador não tem Bash).

---

## 6. Limites (o que esta proposta não faz)

- **Não aplica** nada ao baseline; aplicar é do Orquestrador, depois da homologação de Andraus (ata própria, como DHR-SPEC006-005).
- **Não atualiza** a versão do MMC-001 nem o CATALOGO/ROADMAP — dependem da escolha Patch × Minor × Major (§3.4); em Patch a versão não muda. *[antes: "**Não atualiza** o cabeçalho/versão do MMC-001 nem o CATALOGO/ROADMAP — dependem da escolha Patch × Minor (§3)."]*
- **Corrige**, como alvo 4 (§2.4), o trecho "condição R3-m07 na ata §3" do cabeçalho (l.3) → §4 (DHR-SPEC008-002 §4, l.40-42) `[FATO]`. Não é FICHA-M: o MMC-001 é baseline, e mudança nele só entra por errata homologada (INV-09; MMC-001 l.3). *[antes: "**Não corrige** outra imprecisão vista na leitura, fora do escopo: o cabeçalho do MMC-001 (l.3) diz \"condição R3-m07 na ata §3\", mas a condição está no **§4** da DHR-SPEC008-002 `[FATO]`. Candidata a FICHA-M do Orquestrador, se Andraus quiser." — contrariava INV-09 (ER1-m03)]*
- **Não revisa** a firmeza da l.144 da ABERTURA (que está sob título de "orientação"): segue a leitura já acolhida pela ata §4.
- Não verificado: o chat de Andraus de 2026-11-08 (só o repasse do Orquestrador); hash do MMC-001 no momento da aplicação (o Orquestrador deve conferir que as l.3, l.72, l.169 e l.230 ainda têm o texto citado no §2). *[antes: "…(o Orquestrador deve conferir que as l.72 e l.169 ainda têm o texto citado no §2)."]*

---

## 7. Pendências de Andraus (nada decidido aqui) — `[DECISÃO NECESSÁRIA]`

| # | Ponto | Opções | Observação |
|---|---|---|---|
| E-1 | Compatibilidade (RULE-HG-04) | **Patch** (v1.0 mantida) · **Minor** (v1.1) · **Major** (v2.0) | Análise no §3. Resposta anterior "Patch v1.0.1" pendente de reconfirmação (§3.4): "v1.0.1" não existe na CR-001 (l.439). |
| E-2 | Forma de aplicação (ER1-m04) | **(A) No próprio lugar**, com `[antes]` (como o §2 está redigido; admissível sob INV-07) · **(B) Arquivo à parte** com o texto do §2 + **ponteiro de uma linha** no cabeçalho do MMC-001, sem alterar as células baselined (forma da DHR-SPEC006-005 D2, l.19) | Em (B), o próprio ponteiro é a única linha tocada no baseline (como no precedente, "editorial"); nome e lugar do arquivo ficam para a aplicação, depois da escolha. Em Major (E-1), (B) fica mais próxima da cláusula CE2 (§3.3). |
