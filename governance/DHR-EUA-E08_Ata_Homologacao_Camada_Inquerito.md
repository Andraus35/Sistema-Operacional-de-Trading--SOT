# DHR-EUA-E08 — Ata de Homologação da Emenda EUA-E08 (Camada de Inquérito)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E08 |
| Objeto | Emenda enxuta **EUA-E08** — RULE-INQ-01/02/03 (questão→método; evidência discriminante; critério de encerramento) + nó **N11 (Inquérito)** no MAN-001 + correção da lista §68 + classificação do MIQG-001 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E08_Camada_Inquerito_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (proporcionalidade + conflito 4Es verificados; Anexo A) |
| Trilha | B (método) + transversal (MAN-001) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E08, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q5 da proposta §7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | MIQG-001 = referência externa não-normativa | **APROVADO** |
| Q2 | Nó **N11 (Inquérito)** no MAN-001 + correção da lista §68 (omitia "Inquérito") | **APROVADO** |
| Q3 | RULE-INQ-01..03 (questão→método; evidência discriminante; critério de encerramento), sob CC-09 | **APROVADO** |
| Q4 | Sensores INV-INQ/INQ-S/GATE-INQ diferidos ao harness-eval/GEH | **APROVADO** |
| Q5 | Incorporar à v1.5 no piloto SPEC-002 (com EUA-E04/E05/E06/E07) | **APROVADO** |

## 3. Vigência e incorporação

- **Vigência imediata** da EUA-E08 a partir de 2026-09-20. RULE-INQ-01..03 aplicam-se às specs novas (SPEC-002+); verificação sob CC-09 + dial GES.
- **Incorporação diferida**: seção "Regras de Inquérito (RULE-INQ)" no `RULES.md` na **v1.5**, no piloto SPEC-002, junto com EUA-E04/E05/E06/E07.
- **Nó N11 (Inquérito)** registrado no MAN-001 v1.0 §2 (vigência imediata); lista de nós futuros §68 corrigida.
- **Sensores operacionais** (INV-INQ/INQ-S/GATE-INQ) permanecem responsabilidade do harness-eval/GEH-001 (runtime), fora desta emenda.

## 4. Achado do parecer — estado

| ID | Estado |
|---|---|
| A-01 (versão da EUA-E08 no nó N11) | **Aceito** — emenda não versiona; formato uniforme dos nós enxutos mantido. |

## 5. Classificação do MIQG-001 (Q1 — fechada)

**MIQG-001 = referência externa não-normativa** (igual HCH/CMHP/MEG/MSC/MOC/GEH). Importadas só a classificação de questão→método (§9/§14), a evidência discriminante (§20) e o critério de encerramento (§37). **Não adotar:** catálogo operacional §62–66 (runtime → harness-eval/GEH); ordem "3Es" do §87 (conflita com 4Es CEE-001 §12). Registro K-MAN-07 no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. EUA-E08 adicionada ao CATÁLOGO OFICIAL.
2. MIQG-001 registrado no CATÁLOGO como referência externa; camada futura "Inquérito" (§68) deixa de ser pendente (nó N11).
3. Nó **N11 (Inquérito)** acrescentado ao MAN-001 §2; lista §68 corrigida.
4. Registro K-MAN-07 no CONFLICT-MAP (ordem 3Es do MIQG §87).

## 7. Próximos passos

1. Piloto em **SPEC-002** exercita EUA-E04 + E05 + E06 + E07 + E08 juntas.
2. Se CONFORME → Controlador incorpora as cinco ao `atomic-spec` **v1.5** + seções RULE-HD/RULE-EPI/RULE-SEM/RULE-ONT/RULE-INQ no `RULES.md`.

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
