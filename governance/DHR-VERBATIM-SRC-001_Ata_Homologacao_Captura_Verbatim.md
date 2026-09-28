# DHR-VERBATIM-SRC-001 — Ata de Homologação — Captura Verbatim de Fonte (RULE-ECC-04)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | BL-020 (RMR-001) — reavaliação do acesso web do Revisor após o piloto da EUA-E21 |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — vigência imediata, prospectiva** |
| Compatibilidade | Minor (nova regra na família RULE-ECC existente; não redefine RULE-ECC-01/02/03) |

---

## 1. Decisão

**BL-020 é DECLINADO** — o Revisor **não** recebe `WebSearch`/`WebFetch`. Justificativa: o mandato do Revisor (atomic-spec §15, "Verificação") é estrutural/de governança, não de conteúdo; dar-lhe acesso web (a) confundiria detector com gate (mesmo princípio de ENF-03 aplicado noutro contexto: o Revisor viraria árbitro de fato externo sem mecanismo determinístico por trás); (b) abriria superfície de prompt injection que hoje não existe (uma página maliciosa lida durante auditoria); (c) o mandato de conteúdo já é do Especificador, que tem WebSearch/WebFetch sob as salvaguardas de DHR-PROV-WEB-001 §2.1.

**Em substituição, HOMOLOGA-SE `RULE-ECC-04` — Captura Verbatim de Fonte:**

1. **Captura obrigatória.** Cada fonte `[EXTERNO]` citada num Dossiê de Pesquisa (RULE-ECC-02) que sustenta uma alegação carregada (comparação adotar/adaptar/rejeitar/adiar) DEVE ter um arquivo companheiro em `specs/features/SPEC-0NN/sources/<ID-da-fonte>.txt` com: URL, data de acesso, e um **trecho literal capturado no momento do fetch** (não resumo, não paráfrase) — mínimo 100 caracteres.
2. **Citação literal no Dossiê.** Toda alegação carregada que se apoia numa fonte externa DEVE citar, entre aspas, um trecho literal dela — mesmo princípio de **PC-06/RCN-001** (transcrição literal, proibição de paráfrase não autorizada), estendido de documentos-baseline para fontes de pesquisa.
3. **Verificação determinística (Revisor, sem web).** O trecho citado entre aspas no `research.md` DEVE aparecer **verbatim** no arquivo de captura correspondente — checagem de string (`grep`), sem julgamento semântico, dentro do mandato estrutural já existente do Revisor. Divergência = achado; ausência do arquivo de captura para fonte carregada = achado Crítico (fail-closed, mesmo padrão de RULE-ECC-02).
4. **Risco residual reconhecido, não eliminado.** Isto não prova que o arquivo de captura reflete fielmente a página real — mas transforma uma alegação infalsificável em uma alegação falsificável e auditável a qualquer momento por quem tiver acesso à web (Andraus, auditoria externa, Revisor futuro). Categoria de risco menor que a anterior.
5. **Prospectiva.** Incide a partir da próxima abertura de Spec sob RULE-ECC-01/02 (SPEC-002 em diante) — **não retroage** sobre os Dossiês já homologados (SPEC-020, SPEC-021).

---

## 2. Efeitos imediatos desta homologação

1. **RULE-ECC-04 — FATO NORMATIVO com vigência imediata.** Registrada em `governance/RULES.md`, dentro da seção existente "Regras de Especificação Emergente (RULE-ECC)".
2. **atomic-spec.md §15** — parágrafo "Verificação" emendado com a exigência de captura verbatim e o mecanismo de checagem do Revisor.
3. **`.claude/agents/especificador.md`** — novo item no autopré-check: capturar e citar literalmente fontes carregadas.
4. **`.claude/agents/revisor.md`** — Passo 4-bis emendado: checagem de correspondência verbatim entre citação e arquivo de captura.
5. **BL-020 — DESCARTADO** (RMR-001, com justificativa — permanece no registro histórico, INV-07). Substituído por RULE-ECC-04.

---

## 3. Registro do Controlador (efeitos aplicados — 2026-09-28)

- [x] `governance/RULES.md` — RULE-ECC-04 adicionada à família RULE-ECC; cabeçalho anotado.
- [x] `atomic-spec.md` — §15 "Verificação" emendado; cabeçalho anotado.
- [x] `.claude/agents/especificador.md` — novo item de autopré-check.
- [x] `.claude/agents/revisor.md` — Passo 4-bis emendado.
- [x] `backlog/RMR-001_Painel_Backlog.md` — BL-020 → `Descartado` (substituído por RULE-ECC-04); passo 11-bis registrado.
- [x] `governance/CATALOGO-OFICIAL.md` — nova linha de ata.
- [x] Mapa do projeto, referências cruzadas e testes revalidados.

**Pendências (não bloqueiam):** nenhuma. RULE-ECC-04 é prospectiva; SPEC-020/021 não precisam de retrofit.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
