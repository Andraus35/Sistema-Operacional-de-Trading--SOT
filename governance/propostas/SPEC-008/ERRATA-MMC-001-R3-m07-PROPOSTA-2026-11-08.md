# Errata aditiva ao MMC-001 v1.0 — condição R3-m07 (orientação × obrigação na Classe da Fase 1) — PROPOSTA

| Campo | Valor |
|---|---|
| Alvo | `governance/MMC-001_Manager_Contract.md` — **MMC-001 v1.0, BASELINE** (Andraus, 2026-11-08, `DHR-SPEC008-002`) |
| Origem | Condição da homologação: `DHR-SPEC008-002` §4 (opção (a), errata aditiva "em passo à parte e por ordem de Andraus"); achado **R3-m07** (Menor, C02, classe O, não bloqueante) em `governance/propostas/SPEC-008/PARECER-REVISOR-MANAGER-CONTRACT-R3-2026-11-07.md` l.19 e l.31 |
| Ordem | Andraus, chat 2026-11-08: "Aplicar a errata do R3-m07" (repassada pelo Orquestrador, CLASSE-TAREFA O) |
| Autor | Especificador Principal SOT |
| Data | 2026-11-08 |
| Status | **PROPOSTA** — não aplicada ao baseline. Só vigora com homologação de Andraus (INV-09; RULE-HG-02/03). Nenhuma decisão aberta é fechada (CONS-01). |
| Forma (precedente) | `DHR-SPEC006-005` (errata aditiva; texto anterior recuperável; compatibilidade declarada; condição explícita do que a homologação não afirma) |

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

**Nada mais é tocado:** cabeçalho, §3 (tabela e coluna), §3.1.1/§3.1.2/§3.1.4, §3.2, §4–§8.2, demais linhas do §8.2-bis, §8.3, §9–§14 ficam como estão. `[PROPOSTA]`

---

## 2. Texto antigo → texto novo (aditivo; `[antes]` no próprio lugar — INV-07)

### 2.1 Linha 3.1.3 (MMC-001 l.72)

**Antigo (literal, linha inteira):**

```
| 3.1.3 | Na abertura homologada da SPEC-008: Classe **D** em tudo + **C** na trava constitutiva; **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus. **Alcance:** só SPEC-008 e Spec de Tempo (filha — A-2 DECIDIDO, Andraus, chat 2026-11-07; §8.2-bis). *[antes: "**Alcance:** só SPEC-008 e, se A-2 = sim, Spec de Tempo (§8.2-bis)."]* | `[FATO]` DHR-SPEC008-001 §1 (frase de abertura: respostas "confirmadas pela homologação da `ABERTURA.md` como está") e §4 (homologa a abertura); texto em ABERTURA.md §4 (não-baseline — ver cabeçalho) — a declaração por BASpec continua sendo do Plan *[antes: "`[FATO]` ABERTURA.md §4, homologada 'como está' (DHR-SPEC008-001 §1) — a declaração por BASpec continua sendo do Plan" (R1-M03)]* |
```

**Novo (proposto):**

```
| 3.1.3 | **Obrigação:** **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus. **Orientação (não vinculante — CC-11 por BASpec; não é obrigação):** na abertura homologada da SPEC-008, Classe **D** em tudo + **C** na trava constitutiva; a Classe de cada BASpec é declarada no Plan (RULE-MECH-01). **Alcance:** só SPEC-008 e Spec de Tempo (filha — A-2 DECIDIDO, Andraus, chat 2026-11-07; §8.2-bis). *[antes: "Na abertura homologada da SPEC-008: Classe **D** em tudo + **C** na trava constitutiva; **nenhuma** BASpec H/P na Fase 1; se o Plan precisar de julgamento, o escopo está errado e volta a Andraus." — orientação D/C lida como obrigação (R3-m07; RULE-SEM-03)]* *[antes: "**Alcance:** só SPEC-008 e, se A-2 = sim, Spec de Tempo (§8.2-bis)."]* | `[FATO]` DHR-SPEC008-001 §1 (frase de abertura: respostas "confirmadas pela homologação da `ABERTURA.md` como está") e §4 (homologa a abertura); texto em ABERTURA.md l.25 ("orientação, não vinculante — CC-11 por BASpec") e §4 ("orientação por tipo de BASpec"; l.144 para a parte firme) (não-baseline — ver cabeçalho); parte firme = `[FATO]` DHR-SPEC008-002 §4 e parecer R3 l.19 · base adicional: ADR-MANAGER-001 §2.5 (Fase 1 "sem julgamento analítico") — a declaração por BASpec continua sendo do Plan *[antes: "…; texto em ABERTURA.md §4 (não-baseline — ver cabeçalho) — a declaração por BASpec continua sendo do Plan"]* *[antes: "`[FATO]` ABERTURA.md §4, homologada 'como está' (DHR-SPEC008-001 §1) — a declaração por BASpec continua sendo do Plan" (R1-M03)]* |
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

---

## 3. Compatibilidade (RULE-HG-04) — `[PROPOSTA]`

**Classificação recomendada: Patch.** Justificativa `[INFERÊNCIA]`:
- A errata **alinha o texto do contrato à modalidade da fonte** que a DHR-SPEC008-001 homologou "como está" (orientação). Não cria regra, campo, estado, transição, ID normativo nem agente de trading; não muda nenhuma fronteira, invariante ou alcance de outra seção.
- O único efeito material é **deixar de exigir como obrigação** uma Classe que a fonte nunca exigiu. Nenhum consumidor foi construído sobre a leitura antiga: o Plan da SPEC-008 e o da Spec de Tempo **não começaram** (ROADMAP l.524: "Plan pendente, só por ordem de Andraus"); SPEC-014/015 não estão abertas.
- **Análise de impacto:** schemas — nenhum; RAG — nenhum; Skills — nenhuma; testes — nenhum (nenhum teste cita §3.1.3); modelos dependentes — nenhum. Gates do Plan: CC-11 e `[STRUCT-14]` continuam exigindo Classe por BASpec — inalterados.

**Alternativa: Minor.** Leitura possível: o v1.0 é baseline e o texto homologado dizia "obrigação"; afrouxar uma obrigação baselined, mesmo sem consumidor, pode ser contado como mudança de conteúdo normativo. Escolha entre Patch e Minor = **Andraus**. Marcador de versão proposto: **MMC-001 v1.0.1** (Patch) ou **v1.1** (Minor) — `[PROPOSTA]`; a atualização do cabeçalho do MMC-001 não está nesta errata (§6).

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

**Compatibilidade com o §8.3 (não tocado):** o ADDED (c), l.230, diz "Classe D/C (§3.1.3) e 'orçamento do ciclo' da P-7 só para SPEC-008/Tempo". É frase de **restrição** de alcance ("só para"); não afirma que D/C é obrigação. Continua verdadeira depois da errata — `[INFERÊNCIA]`; não precisa de edição. Se Andraus quiser a redação explícita também ali, é outra errata.

---

## 5. Autopré-check (curto)

- [x] ROADMAP.md (l.524: estado SPEC-008/MMC-001) e atomic-spec.md (CC-10/RULE-SEM-03, l.291) consultados; ata DHR-SPEC008-002 §4, parecer R3 (l.19, l.31), ABERTURA.md (l.25, l.140, l.144) e precedente DHR-SPEC006-005 lidos.
- [x] Só §3.1.3 (l.72) e §8.2-bis (l.169, + uma linha desdobrada e um `[antes]` acrescentado) — nenhuma outra seção.
- [x] Texto antigo citado literalmente; texto substituído preservado em `[antes: …]` (INV-07).
- [x] Sem regra, campo, estado, transição, ID normativo ou agente de trading novo. "Orientação"/"Obrigação" são rótulos de modalidade já usados no contrato (§3 l.56, l.63; §8.2-bis l.168).
- [x] Parte firme mantida firme e com o mesmo alcance (§4).
- [x] CONS-01: nenhuma decisão aberta fechada (J-001, G-001, K-001, C-001, M-001, N-001, SPEC-015-SCOPE, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, D-PCC-4, P-11, P-13, dono do Signal Package — intocados).
- [x] Etiquetas `[FATO]`/`[INFERÊNCIA]`/`[PROPOSTA]` aplicadas; Patch × Minor deixado a Andraus.
- [ ] `validate_spec_sot.py` não se aplica (não é plan.md). `check_refs.py` / `build_map.py --check` — a rodar pelo Orquestrador (o Especificador não tem Bash).

---

## 6. Limites (o que esta proposta não faz)

- **Não aplica** nada ao baseline; aplicar é do Orquestrador, depois da homologação de Andraus (ata própria, como DHR-SPEC006-005).
- **Não atualiza** o cabeçalho/versão do MMC-001 nem o CATALOGO/ROADMAP — dependem da escolha Patch × Minor (§3).
- **Não corrige** outra imprecisão vista na leitura, fora do escopo: o cabeçalho do MMC-001 (l.3) diz "condição R3-m07 na ata §3", mas a condição está no **§4** da DHR-SPEC008-002 `[FATO]`. Candidata a FICHA-M do Orquestrador, se Andraus quiser.
- **Não revisa** a firmeza da l.144 da ABERTURA (que está sob título de "orientação"): segue a leitura já acolhida pela ata §4.
- Não verificado: o chat de Andraus de 2026-11-08 (só o repasse do Orquestrador); hash do MMC-001 no momento da aplicação (o Orquestrador deve conferir que as l.72 e l.169 ainda têm o texto citado no §2).
