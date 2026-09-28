# DHR-SPEC046-001 — Ata de Homologação — Abertura da SPEC-046 (Spec-Time Context Caching Harness — Especificador/Revisor)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | SPEC-046 — Parecer do Revisor sobre o gate de ABERTURA: CONFORME (2026-09-28) — `specs/features/SPEC-046/PROPOSTA-ABERTURA.md` + `DOSSIE-PESQUISA.md` + `sources/SRC-01..07` |
| Data | 2026-09-28 |
| Status | **ABERTURA HOMOLOGADA** — Dossiê de Pesquisa + Proposta de Abertura homologados. **NÃO é baseline** — o Plan (`plan.md`/`checks.md`, via `tlc-spec-lean`) ainda não foi escrito; esse é o próximo gate. |
| Compatibilidade | Minor (não toca modelo canônico nem decisão aberta) |

---

## 1. Decisão

A **abertura da SPEC-046 — "Spec-Time Context Caching Harness (Especificador/Revisor)" está HOMOLOGADA.**

Trata-se de abertura **fora da ordem de dependência do ROADMAP** — o próximo trabalho autorizado pela ordem regular permanece **SPEC-002** (Evidence & Evidence Provenance Harness, Trilha B; nenhum slot indicativo 002-045 cobre caching). A SPEC-046 é uma linha de trabalho **paralela**, aberta por decisão direta de Andraus nesta sessão (2026-09-28), sob a faculdade de RULE-ECC-01 de revisar a ordem de dependência entre slots com justificativa homologada. Não substitui nem adia SPEC-002.

**Escopo homologado — restrito ao Grupo B:** caching de spec-time para os agentes **Especificador** e **Revisor** (prompt/contexto — releitura de ROADMAP.md, atomic-spec.md, governance/RULES.md, governance/CATALOGO-OFICIAL.md, backlog/RMR-001 e afins). O **Grupo A** (agentes cognitivos internos — estrutural/institucional/operacional/manager/risco, regidos por CHM-001/CEM-001) permanece **explicitamente fora de escopo**, adiado para quando os agentes analíticos (SPEC-010..014) existirem como Spec. O ACHADO-M2 do parecer de auditoria de `CACHING SOT.MD` (Revisor, 2026-09-28) — precondição de estado CHM-001 antes de cache HIT — não se aplica a este escopo; permanece registrado para a abertura futura do Grupo A.

Fluxo cumprido até este ato: proposta de origem (`reference/externo/CACHING SOT.MD`, RPIR/HOD-001) → parecer de auditoria do Revisor sobre a proposta (CONFORME COM RESSALVAS, ACHADO-C1/M1/M2) → item de backlog BL-024 (RMR-001) → decisão de Andraus de abrir Spec dedicada, fora de ordem, restrita ao Grupo B → Especificador produz Dossiê de Pesquisa (RULE-ECC-02, 7 fontes `[EXTERNO]`, captura verbatim RULE-ECC-04) + Proposta de Abertura (número/nome/fronteira/justificativa/Enforcement Contract) → Revisor audita o gate de abertura → **CONFORME** (2 achados Menores, não bloqueantes) → esta homologação.

---

## 2. Efeitos imediatos desta homologação

1. **SPEC-046 — número atribuído, monotônico, nunca reutilizado.** Nome: "Spec-Time Context Caching Harness (Especificador/Revisor)". Registrada como slot **aberto** (não baseline) em `ROADMAP.md` §26, fora da sequência 002-045, com nota de posição paralela/exceção.
2. **EC-SPEC046-01 — Enforcement Contract vigente para o Plan.** Precondição de cache HIT = hash de conteúdo (SHA-256) ou mtime/commit git inalterado desde a leitura; fail-closed → reler do disco. Classe **H** (Híbrido, RULE-MECH-01..04); nível **E2**.
3. **Grupo A permanece fora de escopo — registrado, não descartado (INV-07).** BL-024 é atualizado para refletir "abertura do Grupo B formalizada"; a abertura futura do Grupo A é matéria de novo Dossiê/proposta, quando os agentes analíticos existirem.
4. **Próximo gate: o Plan.** O Especificador prossegue para `specs/features/SPEC-046/plan.md` + `checks.md` (skill `tlc-spec-lean`), sanando antes os dois achados Menores do parecer de abertura (item 3 abaixo). `validate_spec_sot.py` incide nesse gate (não neste).
5. **DHR-SPEC046-001 — este documento.** Ata oficial de homologação da abertura. Registrado no histórico de DHRs.

---

## 3. Achados do parecer de abertura — encaminhamento

| ID | Severidade | Descrição | Encaminhamento |
|---|---|---|---|
| ACH-MEN-01 | Menor | Proposta cita "RULE-ECC-01 item 5" — a regra não tem itens numerados no texto de `RULES.md`; substância correta, forma imprecisa | Corrigir no Plan: citar `RULE-ECC-01` sem "item 5" |
| ACH-MEN-02 | Menor | 3 de 7 fontes (SRC-02, SRC-04, SRC-05) carregam alegação (adaptar/adiar) sem trecho entre aspas no corpo do Dossiê — arquivos verbatim existem e têm o trecho, falta a citação no texto | Corrigir no Plan: inserir trecho entre aspas de cada uma das 3 fontes na alegação correspondente |
| ACH-OBS-01 | Observação (pré-existente, não gerado por esta abertura) | BL-008 permanece `ATIVADO` desde DHR-EUA-E15 (2026-09-21) — piloto de auditoria retroativa da SPEC-001, ainda não formalmente Absorvido | **Não resolvido nesta ata** — é pré-existente e independente da SPEC-046. Fica para confirmação de Andraus em ato separado ou no próximo gate regular. |

Nenhum achado Crítico ou Médio. Nenhuma decisão aberta (J-001, M-001, ECC-VAL-001 etc.) fechada por este ato — CONS-01 preservado. Nenhum modelo canônico baseline tocado — CONST-01 preservado.

---

## 4. Registro do Controlador (efeitos a aplicar)

- [x] `governance/DHR-SPEC046-001_...md` — este documento.
- [ ] `ROADMAP.md` — nova linha para SPEC-046 em §26 (capacidades exigidas), marcada "Aberta (fora de ordem) — Dossiê homologado; Plan pendente"; nota no bloco "Estado atual do ciclo" (§Estado atual, linha do "Próximo trabalho autorizado") esclarecendo que SPEC-002 continua sendo a linha mainline e SPEC-046 é paralela/exceção.
- [ ] `governance/CATALOGO-OFICIAL.md` — nova linha de ata (§ atas) referenciando esta DHR; `specs/features/SPEC-046/` listado como Trilha B (harness de especificação) aberto.
- [ ] `backlog/RMR-001_Painel_Backlog.md` — BL-024 atualizado: "abertura do Grupo B formalizada (DHR-SPEC046-001)"; nota narrativa "Homologação direta de Andraus fora do gate de Spec (2026-09-28, DHR-SPEC046-001)".
- [ ] `python scripts/check_refs.py` + `python scripts/build_map.py` — rodar após as edições acima.

**Pendências abertas (fora deste registro):** confirmação de status de BL-008 (ACH-OBS-01); abertura do Grupo A da capacidade de caching (fase futura, sem número atribuído); o Plan da SPEC-046 (`plan.md`/`checks.md`) é o próximo passo do fluxo, com ACH-MEN-01/02 sanados antes do reenvio ao Revisor.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
