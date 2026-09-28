# DHR-EUA-E11 — Ata de Homologação da Emenda EUA-E11 (Camada de Incerteza)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E11 |
| Objeto | Emenda enxuta **EUA-E11** — RULE-UNC-01/02/03 (localizar/tipificar; não-contaminação; incerteza≠probabilidade) + nó **N14 (Incerteza)** no MAN-001 + classificação do MUN-001 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E11_Camada_Incerteza_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (fronteira J-001 verificada; Anexo A) |
| Trilha | B (método) + transversal (MAN-001) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E11, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q5 da proposta §7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | MUN-001 = referência externa não-normativa | **APROVADO** |
| Q2 | Nó **N14 (Incerteza)** no MAN-001 (preenche §68 "Incerteza") | **APROVADO** |
| Q3 | RULE-UNC-01..03 (localizar/tipificar; não-contaminação; incerteza≠probabilidade), sob CC-09 | **APROVADO** |
| Q4 | Calibração/sensibilidade → Conviction/CCM (J-001 aberto); quantificação → Probabilística | **APROVADO** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E10) | **APROVADO** |

## 3. Vigência e incorporação

- **Vigência imediata** da EUA-E11 a partir de 2026-09-20. RULE-UNC-01..03 aplicam-se às specs novas (SPEC-002+); verificação sob CC-09.
- **Incorporação diferida**: seção "Regras de Incerteza (RULE-UNC)" no `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E10.
- **Nó N14 (Incerteza)** registrado no MAN-001 v1.0 §2 (vigência imediata).
- **Fronteira J-001 preservada:** a emenda **não** define fórmula/pesos/limiares do Conviction Vector (INV-03/J-001 permanecem abertos). Calibração/sensibilidade → Conviction Engine/CCM-001; quantificação probabilística → nó futuro Probabilística.

## 4. Achado do parecer — estado

| ID | Estado |
|---|---|
| A-01 (K-MAN-10 registro futuro) | **RESOLVIDO** — K-MAN-10 registrado no CONFLICT-MAP nesta efetivação. |

## 5. Classificação do MUN-001 (Q1 — fechada)

**MUN-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/MCF/GEH). Importadas só localização/tipificação (§5/§15), não-contaminação (§18) e incerteza≠probabilidade (§30/§31). **Não adotar:** preservação/abstenção/hipóteses concorrentes (= PB-10/INDETERMINADO/PCO); falsa precisão (= RULE-EPI); calibração/sensibilidade (→ Conviction/CCM, J-001 aberto); quantificação (→ Probabilística). Registro K-MAN-10 no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. EUA-E11 adicionada ao CATÁLOGO OFICIAL.
2. MUN-001 registrado no CATÁLOGO como referência externa; camada futura "Incerteza" (§68) deixa de ser pendente (nó N14).
3. Nó **N14 (Incerteza)** acrescentado ao MAN-001 §2.
4. Registro K-MAN-10 no CONFLICT-MAP.

## 7. Próximos passos

1. Piloto em **SPEC-002** exercita EUA-E04..E11 (8 emendas) juntas.
2. Se CONFORME → Controlador incorpora ao `atomic-spec` **v1.5** + seções RULE-HD/RULE-EPI/RULE-SEM/RULE-ONT/RULE-INQ/RULE-CAU/RULE-CTF/RULE-UNC no `RULES.md`.
3. Camadas restantes (§68): Probabilística · Decisional · Metacognição (esta sem documento no repo).

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
