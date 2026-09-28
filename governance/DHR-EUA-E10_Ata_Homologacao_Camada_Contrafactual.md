# DHR-EUA-E10 — Ata de Homologação da Emenda EUA-E10 (Camada Contrafactual)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E10 |
| Objeto | Emenda enxuta **EUA-E10** — RULE-CTF-01/02/03 (baseline+intervenção mínima+anti-hindsight; condicional+gradação; contrafactual de invalidação) + nó **N13 (Contrafactual)** no MAN-001 + classificação do MCF-001 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E10_Camada_Contrafactual_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (proporcionalidade verificada; Anexo A) |
| Trilha | B (método) + transversal (MAN-001) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E10, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q5 da proposta §7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | MCF-001 = referência externa não-normativa | **APROVADO** |
| Q2 | Nó **N13 (Contrafactual)** no MAN-001 (preenche §68 "Contrafactuais") | **APROVADO** |
| Q3 | RULE-CTF-01..03 (baseline/intervenção mínima/anti-hindsight; condicional+gradação; invalidação), sob CC-09 | **APROVADO** |
| Q4 | Qualificação probabilística e árvores diferidas (nós Incerteza/Probabilística + backtest) | **APROVADO** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04..E09) | **APROVADO** |

## 3. Vigência e incorporação

- **Vigência imediata** da EUA-E10 a partir de 2026-09-20. RULE-CTF-01..03 aplicam-se às specs novas (SPEC-002+); verificação sob CC-09 + GES.
- **Incorporação diferida**: seção "Regras Contrafactuais (RULE-CTF)" no `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04..E09.
- **Nó N13 (Contrafactual)** registrado no MAN-001 v1.0 §2 (vigência imediata); acolhe o diferimento da EUA-E09 (observar-vs-intervir / intervenção hipotética).
- **Diferidos:** qualificação por incerteza/probabilidade (§31/§32 do MCF) → nós futuros Incerteza/Probabilística; propagação/árvores/simulação (§16–18) → specs de backtest.

## 4. Achado do parecer — estado

| ID | Estado |
|---|---|
| A-01 (nota "camadas restantes" imprecisa) | **RESOLVIDO** — §3 corrigido: as quatro restantes ainda sem emenda; Metacognição sem documento. |

## 5. Classificação do MCF-001 (Q1 — fechada)

**MCF-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/GEH). Importadas só baseline/intervenção mínima/anti-hindsight (§3/§13/§20), gradação da consequência (§14) e contrafactual de invalidação (§25/§38). **Não adotar:** §20/§57 (= RULE-CAU-03); §31/§32 (→ Incerteza/Probabilística); §16–18 (→ backtest). Registro K-MAN-09 no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. EUA-E10 adicionada ao CATÁLOGO OFICIAL.
2. MCF-001 registrado no CATÁLOGO como referência externa; camada futura "Contrafactuais" (§68) deixa de ser pendente (nó N13).
3. Nó **N13 (Contrafactual)** acrescentado ao MAN-001 §2.
4. Registro K-MAN-09 no CONFLICT-MAP.

## 7. Próximos passos

1. Piloto em **SPEC-002** exercita EUA-E04..E10 (7 emendas) juntas.
2. Se CONFORME → Controlador incorpora ao `atomic-spec` **v1.5** + seções RULE-HD/RULE-EPI/RULE-SEM/RULE-ONT/RULE-INQ/RULE-CAU/RULE-CTF no `RULES.md`.
3. Camadas restantes (§68): Incerteza · Probabilística · Decisional · Metacognição (Metacognição sem documento no repo).

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
