# DHR-EUA-E12 — Ata de Homologação da Emenda EUA-E12 (Camada Probabilística)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E12 |
| Objeto | Emenda enxuta **EUA-E12** — RULE-PRB-01/02 (evento probabilístico bem-formado; não quantificar sem base) + nó **N15 (Probabilística)** no MAN-001 + classificação do MPB-001 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E12_Camada_Probabilistica_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (zero achados; fronteira J-001 preservada; Anexo A) |
| Trilha | B (método) + transversal (MAN-001) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E12, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q5 da proposta §7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | MPB-001 = referência externa não-normativa | **APROVADO** |
| Q2 | Nó **N15 (Probabilística)** no MAN-001 (preenche §68; par de N14) | **APROVADO** |
| Q3 | RULE-PRB-01/02 (evento bem-formado; não quantificar sem base), sob CC-09 | **APROVADO** |
| Q4 | Diferir ao CCM-001/Conviction (J-001 aberto): calibração/risco/valor esperado/priors/distribuição; decisão → Decisional; backtest → specs | **APROVADO** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E11) | **APROVADO** |

## 3. Vigência e incorporação

- **Vigência imediata** da EUA-E12 a partir de 2026-09-20. RULE-PRB-01/02 aplicam-se às specs novas (SPEC-002+); verificação sob CC-09.
- **Incorporação diferida**: seção "Regras Probabilísticas (RULE-PRB)" no `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E11.
- **Nó N15 (Probabilística)** registrado no MAN-001 v1.0 §2 (vigência imediata); par de N14 (Incerteza).
- **Fronteira J-001 preservada:** a emenda **não** define fórmula/pesos/limiares/calibração/distribuição do Conviction Vector (INV-03/J-001 abertos). Calibração/risco/cauda/valor esperado/priors/distribuição → Conviction Engine/CCM-001 (SPEC-003); probabilidade≠decisão → nó futuro Decisional; backtest → specs de backtest.

## 4. Achados do parecer — estado

Nenhum achado (Crítico/Médio/Menor). Nada a tratar.

## 5. Classificação do MPB-001 (Q1 — fechada)

**MPB-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/MCF/MUN/GEH). Importadas só evento bem-formado (§4/§5) e não-quantificar-sem-base (§10/§57/§59). **Não adotar:** distinções (= RULE-UNC-03/RULE-EPI/PB-10); calibração/risco/valor esperado/priors/distribuição (→ CCM-001/Conviction, J-001 aberto); decisão (→ Decisional); backtest (→ specs). Registro K-MAN-11 no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. EUA-E12 adicionada ao CATÁLOGO OFICIAL.
2. MPB-001 registrado no CATÁLOGO como referência externa; camada futura "Probabilística" (§68) deixa de ser pendente (nó N15).
3. Nó **N15 (Probabilística)** acrescentado ao MAN-001 §2.
4. Registro K-MAN-11 no CONFLICT-MAP.

## 7. Próximos passos

1. Piloto em **SPEC-002** exercita EUA-E04..E12 (9 emendas) juntas.
2. Se CONFORME → Controlador incorpora ao `atomic-spec` **v1.5** + seções RULE-HD/RULE-EPI/RULE-SEM/RULE-ONT/RULE-INQ/RULE-CAU/RULE-CTF/RULE-UNC/RULE-PRB no `RULES.md`.
3. Camadas restantes (§68): Decisional · Metacognição (esta sem documento no repo).

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
