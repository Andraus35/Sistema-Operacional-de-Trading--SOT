# EUA-E25 — Enforcement do Fluxo de Runtime (RULE-ECC-07) — PROPOSTA

| Campo | Valor |
|---|---|
| ID | **EUA-E25** (próximo livre — E24 é a última homologada; E20 permanece reservada à autorização da família RISK) |
| Título | Enforcement do fluxo de orquestração cognitiva (E1→E8) — Tabela vinculante + `RULE-ECC-07` |
| Tipo | Emenda de método (mesmo padrão EUA-E21..E24) |
| Autor | Especificador SOT (Claude Opus 4.8, skill `tlc-spec-lean`, overlay GUS-TLC-001) |
| Data | 2026-09-29 |
| Status | **HOMOLOGADA — BASELINE** (Andraus, "SIM", 2026-09-29; DHR-EUA-E25). Parecer do Revisor: CONFORME condicional (0 achados Crítico/Médio; 1 Menor F-01 não-bloqueante — WARNs de `check_refs.py` por INV-RISK-08/12 citados de `reference/SOT-RISK-MASTER-001_Consolidado.md`, fora da cobertura do script, não fabricados). RULE-ECC-07 vigente em `governance/RULES.md`; §7-bis.2 do `WORKFLOW.md` com força vinculante efetiva. |
| Origem `[FONTE]` | Diretiva de Andraus em chat (2026-09-29): *"SIM POIS O WORKFLOW PODE SER ATUALIZADO ATÉ O FIM DO PROJETO. IMPORTANTE AGORA MESMO É CONDUZIR O DOSSIE POR ESSAS LENTES. PODE RASCUNHAR E VINCULAR."* |
| Compatibilidade (RULE-HG-04) | **Minor** — aditiva; não altera baseline anterior (INV-07); nenhuma decisão aberta fechada (CONS-01); nenhum canônico redefinido (CONST-01). |
| Artefatos tocados | `WORKFLOW.md` (nova §7-bis — já rascunhada, `[PROPOSTA]`) · `governance/RULES.md` (nova `RULE-ECC-07` — **a inserir na homologação**, não antes — RULE-HG-02) · `atomic-spec.md §15` (nota de vínculo — **a inserir na homologação**) · `governance/CATALOGO-OFICIAL.md §4` (linha EUA-E25 — **registro do Controlador na homologação**) |

---

## 1. Diagnóstico `[FONTE]`/`[INFERÊNCIA]`

O `WORKFLOW.md` (raiz, EUA-E24) descreve a orquestração cognitiva em 8 etapas (E1–E8) e é acompanhado de **5 JSON Schemas** (`schemas/runtime-workflow.*.json`, §5, `[PROPOSTA]`) que descrevem a **FORMA** de cada handoff. **O que falta** — e que Andraus pediu explicitamente (2026-09-29) — é o **Enforcement** do fluxo: **quem valida cada transição, o que bloqueia/permite avançar, o que acontece na falha, e onde a checagem vive**.

`[FONTE]` O projeto já possui o instrumento canônico para isto: o **Enforcement Contract** (`atomic-spec.md §10`, ENF-01..08), com a distinção **Detector ≠ Gate (ENF-03)** — o LLM nunca é o gate de aprovação sozinho; é sinal. O gate é determinístico e/ou homologação humana.

`[INFERÊNCIA]` Duas lacunas específicas:
1. **Falta a Tabela de Enforcement por transição** — desenhada agora em `WORKFLOW.md §7-bis.2` (`[PROPOSTA]`).
2. **Falta força vinculante** — `WORKFLOW.md` é **não-normativo por natureza** (§0); uma seção descritiva nele não obriga Specs futuras. Precisa de uma regra normativa que dê força a essa parte específica.

## 2. Decisão de desenho — mecanismo de vínculo `[PROPOSTA]` (com justificativa)

Opções avaliadas (a diretiva deixou a escolha normativa ao Especificador):

| Opção | Avaliação |
|---|---|
| **(a)** Só uma seção em `WORKFLOW.md` com frase de vínculo | **Insuficiente.** `WORKFLOW.md` é não-normativo (§0); não pode auto-conferir vinculatividade. |
| **(b)** Estender a `RULE-ECC-06` (já homologada) | **Rejeitada.** A RULE-ECC-06 vincula a **obrigação de LER e considerar** o `WORKFLOW.md` no Dossiê. O Enforcement é obrigação **diferente**: que a **própria Spec declare seus Enforcement Contracts compatíveis** com a Tabela. Sobrecarregar a ECC-06 misturaria "ler o workflow" com "declarar enforcement" — dois deveres distintos; má separação de responsabilidades. |
| **(c) [ESCOLHIDA]** Nova regra `RULE-ECC-07` | **Adotada.** Replica **exatamente o padrão provado da RULE-ECC-06**: uma regra normativa em `RULES.md` cria a obrigação e **referencia** o documento não-normativo (`WORKFLOW.md §7-bis`). Separa claramente "ler" (ECC-06) de "declarar enforcement compatível" (ECC-07). Próximo livre da família ECC (ECC-03 permanece RESERVADA — não colide). |

**A Tabela vive em `WORKFLOW.md §7-bis`** (co-locada com o fluxo que ela governa, findability/4Es); **a força vinculante vem da `RULE-ECC-07`** em `RULES.md` (normativa). Mesma arquitetura documento-não-normativo + regra-que-vincula da EUA-E23/E24.

## 3. Regra proposta (texto a inserir em `governance/RULES.md`, seção "Regras de Especificação Emergente (RULE-ECC)", na homologação) `[PROPOSTA]`

```
RULE-ECC-07: Toda Spec (SPEC-002 em diante) que especifique um AGENTE do fluxo de runtime
             (estrutural, institucional, operacional, manager/contexto/orquestrador ou de risco)
             ou uma TRANSIÇÃO entre etapas do fluxo (E1→E8 de WORKFLOW.md §3) DEVE declarar seu
             próprio Enforcement Contract (atomic-spec §10.3, ENF-01..08) para cada handoff/efeito
             correspondente, e esse contrato DEVE ser COMPATÍVEL com a Tabela de Enforcement do
             fluxo de runtime (WORKFLOW.md §7-bis.2): a Spec ADOTA a linha aplicável da Tabela,
             ADAPTA-a com justificativa, ou JUSTIFICA o desvio — NUNCA a ignora em silêncio.
             A compatibilidade preserva, no mínimo: (i) Detector ≠ Gate (ENF-03) — validação
             determinística de forma é Detector; convicção/qualidade reportada por LLM é sinal,
             nunca gate; (ii) as duas classes de falha (forma = hard-stop determinístico;
             ausência de oportunidade/convicção insuficiente = fluxo normal, não falha); (iii)
             fail-closed em efeito crítico irreversível (ENF-04) — emissão externa (E8) é E3.
             A RULE-ECC-07 vincula a OBRIGAÇÃO de declarar enforcement compatível, NÃO o conteúdo
             substantivo da Spec; NÃO fecha nenhuma decisão aberta (CONS-01) — limiares de convicção
             usados em gates permanecem em J-001 (Fase Piloto interino); estados de alarme em
             M-001/SPEC-008; contrato do Signal Package em D-RISK-SP-001; convicção de risco em
             RISK-CONV-001; localização em RISK-ARR-LOC-001; camada hospedeira em ENF-LOC-001
             (proposta). O Revisor verifica PRESENÇA e COMPATIBILIDADE declarada (Detector), não o
             mérito de runtime; ausência de Enforcement Contract onde exigível = NÃO CONFORME
             Crítica (fail-closed); desvio da Tabela sem justificativa = Médio. Prospectiva —
             incide a partir de SPEC-002; não retroage sobre SPEC-001/019/020/021/046 (INV-07).
             NOTA: WORKFLOW.md §7-bis é não-normativa por natureza (herda o status do documento);
             sua força vinculante decorre DESTA regra (mesmo padrão da RULE-ECC-06).
             [Fonte: diretiva de Andraus 2026-09-29 ("PODE VINCULAR"); atomic-spec §10 (ENF-01..08);
              ENF-03/ENF-04; RULE-ECC-06 (padrão de vínculo); WORKFLOW.md §7-bis; CONS-01; RULE-MET-01]
```

## 4. Nota a inserir em `atomic-spec.md §15` (na homologação) `[PROPOSTA]`

> **Enforcement de orquestração (EUA-E25 / RULE-ECC-07).** Quando a Spec especifica um agente do fluxo (estrutural/institucional/operacional/manager/risco) ou uma transição E1→E8, além de considerar o `WORKFLOW.md` no Dossiê (RULE-ECC-06), a Spec DEVE declarar Enforcement Contracts (§10.3) compatíveis com a Tabela de `WORKFLOW.md §7-bis.2` (adotar/adaptar/justificar desvio — nunca ignorar). Não fecha decisão aberta (CONS-01).

## 5. Autopré-check EUA-E18 (proporcional — esta emenda é método, tratada como HIGH)

**Bloco A — pergunta adversarial:** *Se a RULE-ECC-07 estivesse errada, o que seria observável?* Uma Spec de agente do fluxo emitindo efeito (publicação/dispatch/emissão) **sem** Enforcement Contract, ou com contrato que deixa o LLM auto-autorizar emissão externa (viola ENF-03/ENF-04) passaria no gate. A regra é verificável por observador independente (Revisor confere presença + declaração adotar/adaptar/justificar). *Condição em que o QUANDO se satisfaz mas o ENTÃO não deve ocorrer:* Spec fora do fluxo de runtime (ex.: infraestrutura pura, governança) — coberto: a regra só incide sobre agentes/transições do fluxo (fail-closed seletivo, análogo à RULE-ECC-05).

**Bloco B — herança/CC-08:** esta emenda não herda de canônico; deriva de `atomic-spec §10` (ENF) e do padrão RULE-ECC-06. Nenhuma obrigação herdada suprimida.

**Bloco C — epistêmico (RULE-EPI/CAU/PRB, CC-09):** nenhuma afirmação causal nova; nenhum limiar numérico fixado (todos remetidos a J-001/Fase Piloto). Incerteza declarada via `[PROPOSTA]`/`[DECISÃO NECESSÁRIA]`. Sem falsa precisão.

**Bloco D — escopo:** a Tabela produz **desenho de validação/recomendação**, não execução (INV-05/RULE-DEC-01); nenhuma BASpec cruza a fronteira SOT→execução downstream (E8 = decidir emitir/não-emitir; a execução é do bot externo). Dependências de decisão de Andraus marcadas `[DECISÃO NECESSÁRIA]`.

## 6. Decisões que esta emenda NÃO fecha (CONS-01)

`J-001` · `M-001` · `SPEC-008`/`SPEC-045-RUNTIME-001`/`K-001` · `RISK-CONV-001` · `RISK-LEV-001` · `D-RISK-SP-001` · `RISK-ARR-LOC-001` · `ENF-LOC-001` (`[PROPOSTA]` de identificador — só Andraus cunha) · reconciliação editorial dos rótulos E-antigos nos `$comment` dos 5 schemas (`[DECISÃO NECESSÁRIA]` editorial).

## 7. Fluxo de autoridade

```
Etapa 1 — Diretiva de Andraus (chat, 2026-09-29, "PODE RASCUNHAR E VINCULAR") ...... ✅
Etapa 2 — Formalização (esta proposta + §7-bis rascunhada no WORKFLOW.md) .......... ✅ Especificador — nada aplicado a baseline
Etapa 3 — Parecer do Revisor ...................................................... ✅ CONFORME condicional (0 Crítico/Médio; 1 Menor F-01 não-bloqueante)
Etapa 4 — Decisão de Andraus (pergunta única: homologar RULE-ECC-07 + §7-bis.2) ... ✅ "SIM" (2026-09-29)
Etapa 5 — Registro Oficial / aplicação ........................................... ✅ EFETIVADO — DHR-EUA-E25 + RULE-ECC-07 em RULES.md + nota em atomic-spec §15
                                                                                     + status vinculante da §7-bis do WORKFLOW.md + linha em CATALOGO §4/§7.3
                                                                                     + sincronizado-até de ambos os agentes → DHR-EUA-E25 (RPSA)
```

**Parecer CONFORME do Revisor ≠ vigência (RULE-HG-03). Só Andraus homologa — e homologou ("SIM", 2026-09-29).** `RULE-ECC-07` e a exigência de compatibilidade da `WORKFLOW.md §7-bis.2` são agora vinculantes (SPEC-002 em diante).

---

*EUA-E25 — HOMOLOGADA (DHR-EUA-E25, 2026-09-29). Enforcement do fluxo de runtime + mecanismo de vínculo (RULE-ECC-07), por diretiva de Andraus (2026-09-29, "PODE RASCUNHAR E VINCULAR") e homologação ("SIM"). Corpo da proposta preservado (INV-07).*
