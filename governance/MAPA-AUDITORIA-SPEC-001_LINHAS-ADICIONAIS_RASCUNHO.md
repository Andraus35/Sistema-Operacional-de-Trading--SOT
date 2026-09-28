# Mapa de Auditoria da SPEC-001 (BL-008) — linhas adicionais EUA-E21 e EUA-E22 (RASCUNHO)

> **[ABSORVIDO — 2026-09-28]** Este rascunho foi **absorvido e tornado canônico** por `governance/MAPA-AUDITORIA-SPEC-001.md` (Mapa de Auditoria completo, 14 linhas). Preservado aqui como registro histórico (INV-07); **não deletar**. As linhas 13ª/14ª e as recomendações Q1–Q4 abaixo foram migradas e reavaliadas no documento canônico (Q4 superada: o mapa agora existe → recomenda-se BL-008 → Absorvido).

| Campo | Valor |
|---|---|
| Natureza | **RASCUNHO de material de staging** para o **Mapa de Auditoria** aprovado na EUA-E15 (Q3), **ainda não produzido**. Não é o mapa; não é norma. |
| Status epistemológico | **RASCUNHO — nada aplicado; nenhum baseline alterado.** `[FATO]` = verificado em arquivo; `[INFERÊNCIA]` = análise do Especificador. Vereditos são **pré-análise** sujeita a parecer do Revisor. |
| Regime | **Auditoria ≠ reescrita** (D-DHR-PAP-001-01; EUA-E15): o piloto produz achados/Harness Debt; a SPEC-001 (v1.1, HOMOLOGADA — BASELINE) **não é reescrita**. |
| Autoria / data | Especificador (Claude Code), 2026-09-27 |
| Relação com o backlog | **BL-008** permanece `ATIVADO` (EUA-E15: será absorvido pelo piloto, "12ª linha do mapa"). Este rascunho **não altera** o estado do BL-008 nem o texto do RMR-001. |

---

## 0. Situação `[FATO]`

- O Mapa de Auditoria (11 emendas EUA-E04..E14 + reavaliação SES-001 §59/§60 como 12ª linha) **não existe** no repositório (busca em `governance/`, `specs/`, `backlog/`): a EUA-E15 (Q3) aprovou produzi-lo, e o RMR-001 mantém BL-008 `ATIVADO` aguardando.
- As emendas **EUA-E21** (Especificação Emergente) e **EUA-E22** (R-MAPA) foram homologadas em 2026-09-26, **depois** do desenho do mapa. Não constam das 11+1 linhas.
- **Escopo:** este rascunho propõe **2 linhas adicionais** (13ª e 14ª), na mesma forma das anteriores (EUA · regra · pergunta · veredito · âncora arquivo:§ · ação). Outras emendas posteriores à E14 (EUA-E15..E19a) e as RULE-HG/HV da SPEC-019 **não** estão no escopo aprovado do mapa — ampliá-lo é decisão de Andraus (Q3).

## 1. Linhas propostas

| Ref | Emenda / regra | Pergunta ao SPEC-001 | Veredito (pré-análise) | Âncora | Ação |
|---|---|---|---|---|---|
| **13ª** | **EUA-E21** — RULE-ECC-01 (definição emergente das Specs) / RULE-ECC-02 (Dossiê) | (a) Alguma obrigação da SPEC-001 depende de **lista fechada, número ou quantidade** de Specs, ou da ausência de Dossiê? (b) As **referências a slots downstream** continuam interpretáveis se um slot for dividido, fundido, renumerado ou descartado? | **(a) PASS** — a RULE-ECC-01 (item 2) preserva a SPEC-001 como baseline; a Dossiê só vale para *abertura* de Spec. **(b) Debt leve — D-ECC-1** `[INFERÊNCIA]` | `plan.md`:70 (SPEC-003) · :72 (SPEC-004/006) · :73 (SPEC-002) · :74 (SPEC-004; M-001) · :75 (SPEC-005) · :263 (SPEC-003) · :587 (SPEC-004) — *ao menos 16 referências a SPEC-002..005 (SPEC-003 6×; SPEC-004 5×; SPEC-005 4×; SPEC-002 1×)* | **(a)** nenhuma. **(b)** registrar **D-ECC-1** (Harness Debt, CIC-001) e tratar **na abertura de cada slot referenciado** (ver §2). |
| **14ª** | **EUA-E22** — R-MAPA (manutenção do mapa do projeto por hooks/CI) | As obrigações, o ciclo de verificação ou os critérios da SPEC-001 são afetados pelos hooks, pelo `map-sync` ou pelo CI do mapa? | **PASS (N/A por natureza)** — ferramental do harness de especificação, não conteúdo da Spec. **Verificado `[FATO]`:** sem menção a hooks/mapa/`.claude` no `plan.md` (única ocorrência de "gate-check" é o conceito não relacionado "gate-checkável", :262); `gate-check.js` simulado sobre `plan.md` e `checks.md` = **0 bloqueios**; `validate_spec_sot.py` = **10/10**. | `plan.md`:262 · `scripts/gate-check.js` · `scripts/validate_spec_sot.py` | Nenhuma. |

**Distinção usada (não misturar):** *enforcement das Specs* (contratos ENF do SOT em operação — inalterado) ≠ *enforcement do harness de especificação* (hooks, verificadores, CI — corrigido/ampliado em 2026-09-26). A SPEC-001 trata do primeiro.

## 2. Achado que merece decisão: **D-ECC-1 — lacuna na EUA-E21** `[INFERÊNCIA]`

A EUA-E21 prevê o **re-apontamento** de gatilhos do RMR-001 e a **migração de decisões abertas** quando um slot é alterado. **Não prevê o mesmo para referências de Specs BASELINED a slots futuros** (como as da SPEC-001 a SPEC-002..005 e as que a SPEC-019 possa ter). Hoje, se um slot for dividido/fundido/renumerado na abertura, a referência da SPEC-001 aponta para um identificador que pode deixar de existir ou mudar de escopo.

**Tratamento sugerido (aditivo, sem reescrever a SPEC-001):** na **abertura de cada slot**, o Dossiê lista as referências de Specs baselined ao slot e propõe um **erratum aditivo de re-apontamento** (mesmo padrão do ERRATUM-SPEC019-001). Isso pode ser feito **por prática**, ou formalizado por **emenda aditiva à EUA-E21** (uma frase em `atomic-spec.md` §15 e na RULE-ECC-01) — via trio.

## 3. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Incorporar as linhas **13ª e 14ª** ao Mapa de Auditoria quando o Especificador o produzir (EUA-E15 Q3)? | Sim |
| Q2 | **D-ECC-1:** tratar por **prática** (Dossiê de abertura + erratum aditivo) ou por **emenda aditiva à EUA-E21**? | Emenda aditiva mínima (1 frase em RULE-ECC-01/atomic-spec §15), para não depender de memória |
| Q3 | Ampliar o escopo do mapa às emendas **EUA-E15..E19a** e às **RULE-HG/HV**? (hoje fora do escopo aprovado) | Não agora; reavaliar ao produzir o mapa |
| Q4 | Manter o **BL-008 `ATIVADO`** até o mapa ser produzido (sem alterar o RMR-001 por este rascunho)? | Sim |

## 4. Evidências

`specs/features/SPEC-001/plan.md` (:70, :72–75, :262–263, :587, :645) · `governance/EUA-E15_Redesignacao_Piloto_SPEC-001_PROPOSTA.md` (§4 tabela das 11 emendas; §5 fusão com BL-008; Q3) · `governance/DHR-EUA-E15_Ata_Homologacao_Redesignacao_Piloto_SPEC-001.md` (:30, :37) · `governance/DHR-EUA-E21_Ata_Homologacao_Especificacao_Emergente.md` · `governance/DHR-EUA-E22_Ata_Homologacao_Manutencao_Mapa_Projeto.md` · `backlog/RMR-001_Painel_Backlog.md` (BL-008).
