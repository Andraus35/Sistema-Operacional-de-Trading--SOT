# DHR-PRINC-BID-001 — Ata de Homologação — Herança Principiológica Bidirecional

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Auditoria da homologação da SPEC-020 (2026-09-27) — proposta PRINC-BID-001, BL-022 (RMR-001) |
| Data | 2026-09-27 |
| Status | **HOMOLOGADA — vigência imediata, prospectiva** |
| Compatibilidade | Minor (nova categoria de princípio — não redefine nenhuma existente) |

---

## 1. Decisão

**PRINC-BID-001 está HOMOLOGADA.**

- **Cláusula 1 — Declaração:** toda Spec que define escopo de especialidade DEVE declarar seus sub-princípios operacionais de domínio no namespace **`PD-<domínio>-NN`** — nunca cópia de PC-xx/PB-xx/PE-xx/PO-xx/PS-xx/PCO-xx existente.
- **Cláusula 2 — Fundamentação por pesquisa:** cada `PD-xx` DEVE vir com pesquisa web direcionada, fontes classificadas e etiquetadas `[EXTERNO]` — nunca por intuição do Especificador.
- **Granularidade:** por Spec (não por BASpec, ao contrário de CLASSE-MECH-001) — domínio de especialidade é propriedade do componente inteiro.
- **Ordenação com CLASSE-MECH-001:** a(s) Classe(s) das BASpecs do domínio (RULE-MECH-01) DEVEM ser declaradas ANTES dos `PD-xx` correspondentes — a Classe condiciona quais princípios de domínio fazem sentido (RULE-PD-01).
- **Registro:** `PD-xx` homologado é incorporado aditivamente ao catálogo `GPR-001 §2.7` (INV-07 — nunca apagado), hoje vazio ("nenhum PD-xx declarado ainda").
- **Vigência:** prospectiva — NÃO retroage sobre SPEC-001/019/020. Incide a partir de SPEC-002.

---

## 2. Efeitos imediatos desta homologação

1. **RULE-PD-01..03 — FATO NORMATIVO com vigência imediata.** Registradas em `governance/RULES.md`, nova seção "Regras de Herança Principiológica Bidirecional (RULE-PD)".
2. **GPR-001 — EMENDA PRINC-BID-001** aplicada: novo **§2.7** (catálogo aditivo de `PD-xx`, hoje vazio); regra de ordenação com PE-04/RULE-MECH-01 no §14; novo item no checklist §15.
3. **atomic-spec.md** — emenda no cabeçalho; §10.5 ganhou **CC-12**; nova seção **§10.6→§10.7** (Declaração de Princípios de Domínio, extensão da Spec — não da BASpec); §8 (template mestre) ganhou o passo "Princípios de Domínio". Sem bump de versão (v1.4 permanece pinada para a FASE GOV).
4. **`.claude/agents/especificador.md`** — CC-12 no checklist §7; novo item de autopré-check (pesquisar e propor `PD-xx` depois da Classe).
5. **`.claude/agents/revisor.md`** — CC-12 no Passo 3; referência CC-01..CC-12 atualizada.
6. **CC-12 só incide em Specs de especialidade que citam RULE-PD-01** (SPEC-002 em diante) — não é achado retroativo em SPEC-001/019/020 (nenhuma delas define escopo de especialidade de domínio de mercado; SPEC-020 é meta-harness).

---

## 3. Pendências registradas (não bloqueiam esta homologação)

| ID | Descrição | Encaminhamento |
|---|---|---|
| P-03 | `scripts/validate_spec_sot.py` — check estrutural (STRUCT-13) para CC-12 **DIFERIDO**, mesmo padrão de P-01 (CLASSE-MECH-001): sem Spec concreta ainda usando `PD-xx`, um check automatizado agora seria prematuro | Implementar junto com STRUCT-12 (P-01), quando SPEC-002 entrar em redação |

---

## 4. Registro do Controlador (efeitos aplicados — 2026-09-27)

- [x] `governance/GPR-001_Guia_Principios_Relacoes_SOT.md` — nova seção "EMENDA — PRINC-BID-001"; novo §2.7 (catálogo `PD-xx`); novo item no checklist §15.
- [x] `atomic-spec.md` — emenda no cabeçalho; §10.5 CC-12; §10.7 novo; §8 template mestre atualizado.
- [x] `governance/RULES.md` — comentário de cabeçalho; nova seção "Regras de Herança Principiológica Bidirecional (RULE-PD)" com RULE-PD-01..03.
- [x] `.claude/agents/especificador.md` — CC-12 no checklist §7; novo item de autopré-check.
- [x] `.claude/agents/revisor.md` — CC-12 no Passo 3; referência CC-01..CC-12 atualizada.
- [x] `ROADMAP.md` — PRINC-BID-001 movida de "Decisões abertas ativas" para "Decisões FECHADAS".
- [x] `governance/CATALOGO-OFICIAL.md` — nova linha de ata registrada.
- [x] `backlog/RMR-001_Painel_Backlog.md` — BL-022 → `Absorvido`; passo 11-bis registrado.
- [x] `docs/mapa/` regenerado e verificado (`--check`).
- [x] `scripts/check_refs.py` (0 ERRO/0 WARN), `scripts/backlog_triggers.py` (0 disparos indevidos), gate determinístico revalidado em SPEC-019/020 (sem regressão), suíte de testes (Python + Node) revalidada.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
