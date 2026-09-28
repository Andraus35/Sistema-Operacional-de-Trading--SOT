# DHR-EUA-E09 — Ata de Homologação da Emenda EUA-E09 (Camada Causal)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E09 |
| Objeto | Emenda enxuta **EUA-E09** — RULE-CAU-01/02/03 (mecanismo obrigatório; regime de validade; guard pós-hoc) + nó **N12 (Causal)** no MAN-001 + classificação do MCC-001 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E09_Camada_Causal_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (proporcionalidade verificada; Anexo A) |
| Trilha | B (método) + transversal (MAN-001) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E09, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q5 da proposta §7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | MCC-001 = referência externa não-normativa | **APROVADO** |
| Q2 | Nó **N12 (Causal)** no MAN-001 (preenche §68 "Causalidade") | **APROVADO** |
| Q3 | RULE-CAU-01..03 (mecanismo; regime; guard pós-hoc), sob CC-09 | **APROVADO** |
| Q4 | Intervenção/contrafactual e vocabulário estatístico diferidos (nó Contrafactuais / CCM) | **APROVADO** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E08) | **APROVADO** |

## 3. Vigência e incorporação

- **Vigência imediata** da EUA-E09 a partir de 2026-09-20. RULE-CAU-01..03 aplicam-se às specs novas (SPEC-002+); verificação sob CC-09.
- **Incorporação diferida**: seção "Regras Causais (RULE-CAU)" no `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04/E05/E06/E07/E08.
- **Nó N12 (Causal)** registrado no MAN-001 v1.0 §2 (vigência imediata).
- **Diferidos:** observar-vs-intervir/intervenção hipotética (§28/§58 do MCC) → nó futuro **Contrafactuais**; vocabulário estatístico (mediação/moderação/confounder, §17) → CCM-001.

## 4. Achado do parecer — estado

| ID | Estado |
|---|---|
| A-01 (K-MAN-08 registro futuro) | **RESOLVIDO** — K-MAN-08 registrado no CONFLICT-MAP nesta efetivação. |

## 5. Classificação do MCC-001 (Q1 — fechada)

**MCC-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/GEH). Importadas só mecanismo obrigatório (§3/§54), regime de validade (§45) e guard pós-hoc (§47–48). **Não adotar:** §53 (= RULE-EPI-02/RULE-ONT/AP-02); §28/§58 (→ Contrafactuais + backtest/CCM); §17 (→ CCM-001). Registro K-MAN-08 no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. EUA-E09 adicionada ao CATÁLOGO OFICIAL.
2. MCC-001 registrado no CATÁLOGO como referência externa; camada futura "Causalidade" (§68) deixa de ser pendente (nó N12).
3. Nó **N12 (Causal)** acrescentado ao MAN-001 §2.
4. Registro K-MAN-08 no CONFLICT-MAP.

## 7. Próximos passos

1. Piloto em **SPEC-002** exercita EUA-E04 + E05 + E06 + E07 + E08 + E09 juntas.
2. Se CONFORME → Controlador incorpora as seis ao `atomic-spec` **v1.5** + seções RULE-HD/RULE-EPI/RULE-SEM/RULE-ONT/RULE-INQ/RULE-CAU no `RULES.md`.

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
