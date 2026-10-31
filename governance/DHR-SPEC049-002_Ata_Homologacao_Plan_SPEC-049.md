# DHR-SPEC049-002 — Ata de Homologação — Plan da SPEC-049 v1.2 (WikiRAG Reading View)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-049/plan.md` v1.2 (1.583 linhas de corpo) + `checks.md` v1.2 · pareceres do Revisor em `governance/propostas/SPEC-049/`: R1 (NÃO CONFORME, 3 Médias + 8 Menores), R2 (CONFORME condicional, 0 Média, 7 Menores, por delta) e R3 (CONFORME condicional, 0 Média, 4 Menores, por delta); gates do Orquestrador = PASSOU_D, `validate_spec_sot` 13/13 · `DHR-SPEC049-001` (abertura) · `DHR-DIMENSIONAMENTO-001` (RULE-ECC-07) · `DHR-DELTA-HASH-001` |
| Data | 2026-10-31 |
| Status | **PLAN v1.2 HOMOLOGADO — BASELINE** (decisão direta de Andraus em chat, 2026-10-31, por AskUserQuestion: "Homologar com 3 condições"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). Homologação **CONDICIONADA** (§4). *[Estado anterior preservado — INV-07: "PROPOSTA — CANDIDATA; aguarda Revisor (rodada 3, por delta) e homologação de Andraus. NÃO é baseline"]* |
| Compatibilidade | Minor (não toca modelo canônico baselined nem Spec baselined) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Homologação de Plan de Spec em redação: não altera texto de agente nem método. |

## 1. Pontos decididos por Andraus `[FATO]` (chat, 2026-10-31)
| # | Ponto | Decisão |
|---|---|---|
| O-1 | Ordem do Plan | **Registrada nesta ata**: Andraus ordenou o Plan da SPEC-049 em chat, 2026-10-31 ("Iniciar o Plan da SPEC-049"); a correção das rodadas R1–R3 foi coberta pela mesma ordem |
| P-1 | Fonte com liberação retirada depois do corte | **Não entregar a página** (motivo registrado; Andraus pede outra com data mais recente). É o lado seguro já escrito no Plan |
| P-2 | Separar por ativo | **Só pela ligação ESTATISTICA_DE** (a única não causal); o que não a tiver vai para "sem classificação"; CAUSA não agrupa |
| Atos 4 e 5 | Ciência | **Tomada**: (4) "escola indeterminada" não aparece na versão 1 porque escola não é chave de agrupamento; (5) o formato da página e o programa que a codifica ficam fixados na construção, na versão 1 da regra; mudar depois exige nova versão da regra, com aprovação de Andraus por errata |
| Q-A | Quem aprova o 1º registro do formato da página (versão 1 da regra de montagem) | **Decidir na construção** — pergunta de Andraus **pendente e não bloqueante** (errata ao Plan ou ato próprio). **Nada decidido aqui.** Enquanto não houver registro, o Plan já recusa todo pedido (`WRV_RULE_VERSION_UNREGISTERED`) |
| Menores R3 | m01, m03, m04 | **Condições obrigatórias** (§3), não corrigidas antes |
| Homologação | Plan v1.2 | **Homologar com 3 condições** |

## 2. Efeitos da homologação
- Plan v1.2 da SPEC-049 (1 INV, 10 RULE-WRV, 11 EARS, 11 BASpec, 3 EC, 18 cenários; HIGH D0–D7, D6 N/A; 10 BASpecs Classe D e 1 Classe C — a trava E3) é **BASELINE** da SPEC-049; `plan.md` e `checks.md` com histórico preservado (INV-07).
- `ROADMAP.md` (slot da SPEC-049 e tabela do §25), `governance/CATALOGO-OFICIAL.md` e `plan.md` (cabeçalho) atualizados, texto anterior preservado. Estados do painel de backlog **não mudam** (sem promoção — só Andraus; `backlog_triggers --abertura SPEC-049` = 0 itens).

## 3. Condições da homologação (Menores do R3 — a cumprir por errata aditiva ao Plan, em passo à parte por ordem de Andraus, ou na construção/Tasks, o que vier primeiro)
1. **R3-m01:** acrescentar ao quadro de pré-requisitos, à frase do trader e à nota do T01 o lado seguro "versão 1 não registrada ⇒ todo pedido recusado" e a aprovação do 1º registro como decisão pendente de Andraus (sem decidir por ele).
2. **R3-m03:** reescrever no contrato `compilation_rule_record` "recorded_at — NÃO gravado pela compilação" para marcar a restrição no registro, não no campo.
3. **R3-m04:** dizer onde `compilation_rule_record` e os registros anteriores do próprio registro são lidos (KG ou registro próprio) e incluir essa leitura na allowlist da INV-WRV-01/EC-003.
O Plan **não** é editado por esta ata além do cabeçalho de status (INV-09 aplica-se a partir daqui: mudança só por errata homologada).

## 4. Condições de conformidade (o que a homologação NÃO afirma)
- O Revisor não executou o gate dentro da sessão (teto CONFORME condicional); o Orquestrador rodou os gates (PASSOU_D) e o harness também (PASSOU_D). Veracidade das fontes web do Dossiê e a possível adulteração de `sources/` são risco residual declarado; o Benchmark não foi lido.
- Os positivos dependem de **BUILD** (fase spec-first): horizonte de leitura do KG, papel PESSOA no runtime, `render_profile` v1 e seu registro, autenticação dos atos de Andraus. **Não há BUILD**.
- `git diff` de Spec baselined não foi verificado pelo Revisor (sem Bash); as Specs SPEC-006/007/048 não foram editadas (conferência do Orquestrador: só `specs/features/SPEC-049/` e `research.md` l.10 foram tocados).

## 5. Permanecem ABERTAS (CONS-01)
J-001 · G-001 · K-001 · C-001 · M-001 · N-001 · SPEC-045-RUNTIME-001 · ECC-03-001 · WF-D03 (residual) · CKG-STRUCT-ORIGIN-001 (BL-035) · "produtor/gatilho de promoção" · forma de confirmar a identidade de Andraus (BUILD) · aprovação do 1º registro do formato da página (Q-A). **Nenhuma decisão aberta é fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] Confirmação de Andraus (chat 2026-10-31) · [x] ROADMAP · [x] CATALOGO · [x] plan.md (cabeçalho) · [ ] merge (PR, CI verde — assinatura) · [ ] **retrospectiva de fechamento da SPEC-049 (LOOP-001 passo 5; antes de abrir outra Spec)** · [ ] errata aditiva com as 3 condições (passo à parte, por ordem de Andraus) · [ ] decisão Q-A (na construção)

---

**Andraus** — *homologação dada em chat, 2026-10-31; registro pelo Orquestrador.*
