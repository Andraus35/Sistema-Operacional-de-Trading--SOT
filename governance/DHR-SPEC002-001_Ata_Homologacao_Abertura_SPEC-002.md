# DHR-SPEC002-001 — Ata de Homologação — Abertura da SPEC-002 (Evidence & Evidence Provenance Harness)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | SPEC-002 — Parecer do Revisor sobre o gate de ABERTURA: **CONFORME (sem achados)** — `specs/features/SPEC-002/research.md` (Dossiê de Pesquisa + Proposta de Abertura) + `specs/features/SPEC-002/sources/SRC-01..05.txt` |
| Data | 2026-09-29 |
| Status | **ABERTURA HOMOLOGADA** — Dossiê de Pesquisa + definição da Spec (nome/número/complexidade/profundidade/fronteira) homologados. **NÃO é baseline** — o Plan (`plan.md`/`checks.md`, via `tlc-spec-lean`) ainda não foi escrito; esse é o próximo gate (ROADMAP §23 passo 5 em diante). |
| Compatibilidade | Minor (não redefine modelo canônico — CONST-01; não fecha decisão aberta de mérito de outra Spec — CONS-01) |
| Convenção | Mesma da `DHR-SPEC046-001` (ata de abertura separada da ata de homologação do Plan) — ROADMAP §23 passo 1-bis exige homologação da DEFINIÇÃO antes do Plan. A homologação do Plan da SPEC-002 será uma DHR subsequente (`DHR-SPEC002-002`). |

---

## 1. Decisão

A **abertura da SPEC-002 — "Evidence & Evidence Provenance Harness" está HOMOLOGADA.**

**Fluxo de autoridade cumprido até este ato:**
```
Especificador produz Dossiê de Pesquisa (RULE-ECC-02: 5 fontes [EXTERNO] carregadas com
  captura verbatim RULE-ECC-04; 6 lentes de domínio declaradas RULE-ECC-05; WORKFLOW.md lido
  reforçado RULE-ECC-06; Enforcement antecipado RULE-ECC-07; Classe RULE-MECH-01 e PD-xx
  RULE-PD-01 determinados; DN-1/2/3 marcados [DECISÃO NECESSÁRIA])
   → Revisor audita o gate de abertura → CONFORME (sem achados)
   → Andraus decide DN-1/DN-2/DN-3 (chat, 2026-09-29), sob a instrução explícita
     "mantendo simetria com o SOT como um todo", adotando as recomendações do coordenador
   → Abertura HOMOLOGADA (este ato)
```

**Definição homologada da SPEC-002:**
- **Número:** SPEC-002 (slot indicativo confirmado; monotônico, nunca reutilizado — RULE-ECC-01). Sem divisão/fusão/renome; sem re-apontamento de gatilho do RMR-001 (nenhum slot alterado).
- **Nome:** "Evidence & Evidence Provenance Harness".
- **Complexidade:** **CRITICAL** (ROADMAP §4).
- **Profundidade-alvo:** **D0–D8** (DN-2 — ver §2). Nível de maturidade-alvo **L3** (teto de spec-first para CRITICAL — RULE-MM-04).
- **Fronteira/escopo:** camada Harness/operacional **sobre CEM-001** (baseline — **não redefinir**, CONST-01). Escopo IN e Non-goals conforme `research.md` §7.2/§7.3, atualizados pelas resoluções DN-1/DN-3 (§2 desta ata).

---

## 2. As três decisões de Andraus (DN-1 / DN-2 / DN-3)

Registro verbatim + leitura, sob a instrução transversal **"mantendo simetria com o SOT como um todo"**. Detalhamento completo em `specs/features/SPEC-002/research.md §8.4` (aditivo — INV-07; as perguntas originais de §8.2 preservadas).

### DN-1 — Confiabilidade histórica do produtor de evidência
**Decisão (verbatim):** entra como **extensão formal do CEM-001 via GMC-001** (Categoria A — aditiva, sem mudar semântica existente), **não** como metadado solto na camada Harness.
- **Justificativa:** confiabilidade de fonte é **propriedade intrínseca da evidência** (pertence ao CEM-001), não do harness que a processa; a doutrina Admiralty (SRC-02) já trata isso como **eixo independente** da acurácia de conteúdo.
- **Trava constitucional:** o campo é **só metadado descritivo/filtro** — **NUNCA** dimensão do Conviction Vector (**INV-04 intocado**; J-001 não tocado — CONS-01). Extensão **Categoria A (aditiva)** via GMC-001/RULE-GMC-005 — não redefine campo existente do CEM-001 (**CONST-01 preservado**). Modelagem física no Plan.

### DN-2 — Profundidade
**Decisão (verbatim):** **D0–D8** (não D0–D7 como o ROADMAP indicava).
- **Justificativa:** `AGENTS.md` §4 tem a tabela **PINADA** CRITICAL → D0–D8 (standard + adversarial); a SPEC-002 é CRITICAL; usar D7 seria **exceção silenciosa** a tabela pinada. O *blast radius* da camada de evidência (consumida por todo agente downstream) pede D8 adversarial (integridade/anti-adulteração de proveniência). Confirma como D0–D8 pleno a antecipação `[PROPOSTA]` "D8 adversarial seletivo" do Dossiê.

### DN-3 — "Evidência de ausência"
**Decisão (verbatim):** **só o gancho de extensibilidade agora** — a SPEC-002 entrega o tipo/estado "ausente" na taxonomia de evidência (CEM-001/camada Harness) sem fechar a porta; a **semântica de quando a ausência é significativa fica DEFERIDA** para o Dossiê de cada Spec consumidora (SPEC-010 em diante).
- **Padrão:** mesmo de **RISK-LEV-001** — decisão de **timing**, não de mérito. Nenhuma regra de "quando ausência importa" fixada aqui (**CONS-01**).

---

## 3. Efeitos imediatos desta homologação

1. **SPEC-002 — abertura formal CONCLUÍDA.** Definição (nome/número/CRITICAL/D0–D8/fronteira sobre CEM-001) homologada. Registrada como **ABERTA — Dossiê homologado, Plan em elaboração** em `ROADMAP.md` (§4 e painel §26).
2. **Próximo gate: o Plan.** O Especificador prossegue para `specs/features/SPEC-002/plan.md` + `checks.md` (skill `tlc-spec-lean`). `validate_spec_sot.py` incide nesse gate (não neste). No Plan: modelagem física da extensão Categoria A do CEM-001 via GMC-001 (DN-1); Enforcement Contracts por BASpec (ENF-01); Classe por BASpec (RULE-MECH-01, predominância D/H antecipada); §7-bis (redução de viés) obrigatório (HIGH/CRITICAL).
3. **RULE-REG-001 — gatilho `spec:SPEC-002 em redação` disparado por esta abertura** → registro em lote das 10+1 famílias RULE executado (ver §4 e `DHR-SPEC002-001` efeito de Controlador). Consequência mandatória (AGENTS.md §7; ROADMAP "Decisões abertas ativas"), não decisão nova.
4. **BL-012 (MC-COG-001)** — gatilho `spec:SPEC-002 homologada (consolidação cognitiva v1.5)` dispara **na homologação do Plan** (não desta abertura). Registrar como IMINENTE, não ATIVADO por este ato.
5. **DHR-SPEC002-001 — este documento.** Ata oficial de homologação da abertura, registrada no histórico de DHRs.

Nenhum modelo canônico baseline tocado (**CONST-01**). Nenhuma decisão aberta de mérito fechada: J-001, G-001, H-001, K-001, C-001, M-001, N-001, ECC-VAL-001, ECC-03-001, RISK-* permanecem **ABERTAS** (**CONS-01**). A confiabilidade-de-fonte (DN-1) é metadado descritivo — **não** toca J-001 nem INV-04.

---

## 4. Registro do Controlador (efeitos a aplicar)

- [x] `governance/DHR-SPEC002-001_...md` — este documento.
- [x] `specs/features/SPEC-002/research.md` — §8.4 (resolução DN-1/2/3, aditivo INV-07) + frontmatter Profundidade-alvo → D0–D8.
- [x] `ROADMAP.md` — SPEC-002: "Indicativo — não aberta" → "**ABERTA** — Dossiê homologado, Plan em elaboração" (§26); profundidade D0–D7 → **D0–D8** (§4 linha 139 + painel §32); nota da abertura em "Estado atual do ciclo".
- [x] `governance/CATALOGO-OFICIAL.md` — nova linha de ata (§7.3) referenciando esta DHR; entrada de estado da SPEC-002.
- [x] **RULE-REG-001 (lote de 10+1 famílias)** — `governance/RULES.md` recebe as seções RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET (texto verbatim das atas EUA-E04..E14); `atomic-spec.md` promovido a **v1.5** (piloto SPEC-002 executado). Ver `DHR-SPEC002-002-REG` embutido nesta abertura via §5.
- [ ] **Pendências para o coordenador (sem Bash neste agente):** `python scripts/validate_spec_sot.py` (incide no Plan, não nesta abertura), `python scripts/check_refs.py`, `python scripts/check_doc_sync.py` (deve deixar de acusar F-01/RULE-HG-02 para RULE-DEC-01/HD-02/HD-03/MET-01 após o registro §5), `python scripts/backlog_triggers.py`, `python scripts/build_map.py` (novos/alterados `.md`).
- [ ] **Registro correlato NÃO executado nesta ata (fora do escopo desta tarefa — recomendado ao Controlador):** nós **N8–N17** no `governance/MAN-001` e chaves **K-MAN-03/05/06/07/08/09/10/11/12/13** no `governance/CONFLICT-MAP.md`, que as atas EUA-E04..E14 preveem na "efetivação" junto da incorporação. Não fazem parte do escopo estrito de RULE-REG-001 (que é a incorporação ao `RULES.md`), mas são a mesma família de efeitos — encaminhados para ato do Controlador.

---

## 5. Registro em lote RULE-REG-001 — homologação da incorporação física (piloto SPEC-002)

Por força do gatilho `spec:SPEC-002 em redação` (disparado por esta abertura) e das próprias atas de origem (EUA-E04..E14, todas **HOMOLOGADAS — FATO NORMATIVO** desde 2026-09-20/21, com incorporação física **diferida ao piloto SPEC-002 sob atomic-spec v1.5**), homologa-se agora a **incorporação física** ao `governance/RULES.md` das **10+1 famílias**:

| Família | Regras | Ata de origem | DHR |
|---|---|---|---|
| RULE-HD | 01–04 | EUA-E04 | DHR-EUA-E04 (2026-09-20) |
| RULE-EPI | 01–03 (+INV-EPI-01..10) | EUA-E05 | DHR-EUA-E05 (2026-09-20) |
| RULE-SEM | 01–04 | EUA-E06 | DHR-EUA-E06 (2026-09-20) |
| RULE-ONT | 01–02 | EUA-E07 | DHR-EUA-E07 (2026-09-20) |
| RULE-INQ | 01–03 | EUA-E08 | DHR-EUA-E08 (2026-09-20) |
| RULE-CAU | 01–03 | EUA-E09 | DHR-EUA-E09 (2026-09-20) |
| RULE-CTF | 01–03 | EUA-E10 | DHR-EUA-E10 (2026-09-20) |
| RULE-UNC | 01–03 | EUA-E11 | DHR-EUA-E11 (2026-09-20) |
| RULE-PRB | 01–02 | EUA-E12 | DHR-EUA-E12 (2026-09-20) |
| RULE-DEC | 01–03 | EUA-E13 | DHR-EUA-E13 (2026-09-21) |
| RULE-MET | 01–03 | EUA-E14 | DHR-EUA-E14 (2026-09-21) |

O texto normativo registrado no `RULES.md` é **transcrição das atas de origem** (não reescrito). `atomic-spec.md` promovido a **v1.5**.

**Status de RULE-REG-001:** o **único** conteúdo pendente de RULE-REG-001 era a **incorporação física** ao `RULES.md` (as atas de origem já eram FATO NORMATIVO com vigência imediata — o mérito nunca esteve em aberto; ver DHR-DOCSYNC-002). Com o registro físico executado por este ato, essa pendência está **SANADA**. RULE-REG-001 é declarada **RESOLVIDA por execução** nesta abertura.

> **Nota de cautela (RULE-MET-01 / CONS-01):** a declaração acima trata **apenas** do escopo estrito de RULE-REG-001 (incorporação ao `RULES.md` + subida do método a v1.5). Os registros correlatos em MAN-001 (N8–N17) e CONFLICT-MAP (K-MAN-*) previstos pelas atas **não** integram RULE-REG-001 e permanecem como ato pendente do Controlador (§4). Não há mérito remanescente das 10+1 famílias em aberto — todas homologadas em 2026-09-20/21.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
