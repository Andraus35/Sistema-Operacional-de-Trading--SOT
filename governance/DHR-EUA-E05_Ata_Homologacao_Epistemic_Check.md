# DHR-EUA-E05 — Ata de Homologação da Emenda EUA-E05 (Epistemic Check)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E05 |
| Objeto | Emenda **EUA-E05** ao `atomic-spec.md` §11 (Epistemic Check) + CC-09 + RULE-EPI-01..03 + INV-EPI-01..10 + registro do nó **N8 (Epistêmico)** no MAN-001 + classificação do MEG-001 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E05_Epistemic_Check_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (Anexo A da proposta) |
| Trilha | B (método/atomic-spec) + transversal (MAN-001) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E05, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q5 da proposta §8)

| # | Questão | Decisão |
|---|---|---|
| Q1 | MEG-001 = referência externa não-normativa | **APROVADO** |
| Q2 | Registrar nó **N8 (Epistêmico)** no MAN-001 | **APROVADO** |
| Q3 | Emenda EUA-E05 (Epistemic Check §11 + CC-09 + RULE-EPI + INV-EPI) | **APROVADO** |
| Q4 | Diferir guardrails de contaminação (RAG/multiagente) às specs correspondentes | **APROVADO** |
| Q5 | Incorporar ao atomic-spec v1.5 junto com EUA-E04 no piloto SPEC-002 | **APROVADO** |

## 3. Vigência e incorporação

- **Vigência imediata** da EUA-E05 a partir de 2026-09-20. O Epistemic Check e o gate **CC-09** aplicam-se às specs novas (SPEC-002+); estado **INDETERMINADO** formalizado como HOLD de 1ª classe.
- **Incorporação diferida**: fusão no corpo do `atomic-spec` (→ **v1.5**) e criação da seção "Regras Epistêmicas (RULE-EPI)" no `RULES.md` ocorrem **após o piloto** em SPEC-002 (CC-08 + CC-09), **junto com a EUA-E04**. Até lá, a autoridade literal é esta ata + a proposta homologada.
- **Nó N8 (Epistêmico)** registrado no MAN-001 v1.0 §2 (vigência imediata).

## 4. Achados do parecer — estado

| ID | Estado |
|---|---|
| A-01 (versão inline no nó N8) | **RESOLVIDO** — `atomic-spec v1.4 §11 (TRACE-06) + EUA-E05`. |
| A-02 (precisão "SES-001 §60") | **RESOLVIDO** — INV-EPI-07 corrigido. |

## 5. Classificação do MEG-001 (Q1 — fechada)

**MEG-001 (`CAMADA EPISTÊMICA.MD`) = referência externa não-normativa** (igual HCH-001/CMHP-001/GEH-001). Importada só a mecânica de verificação epistêmica (esta emenda). **Fora de adoção:** maturidade "Nível 0–6" (§106, colide com Quality Gates L1–L4 / harness-score L0–L4 / maturidade GPR-001 §11 L0–L5) e unidade EPI-ID (§100, já coberta por BASpec/Enforcement Contract). Registro K-MAN-04 no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. EUA-E05 adicionada ao CATÁLOGO OFICIAL.
2. MEG-001 registrado no CATÁLOGO como referência externa não-normativa.
3. Nó **N8 (Epistêmico)** acrescentado ao MAN-001 §2.
4. Colisão do MEG-001 anotada no CONFLICT-MAP (K-MAN-04).

## 7. Próximos passos

1. Piloto em **SPEC-002** exercita EUA-E04 (Herança/Delta) **e** EUA-E05 (Epistemic Check) juntas.
2. Se CONFORME → Controlador incorpora ambas ao `atomic-spec` **v1.5** + seções RULE-HD e RULE-EPI no `RULES.md`.

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
