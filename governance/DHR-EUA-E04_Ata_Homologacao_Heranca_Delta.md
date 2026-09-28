# DHR-EUA-E04 — Ata de Homologação da Emenda EUA-E04 (Bloco Herança/Delta)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E04 |
| Objeto | Emenda **EUA-E04** ao `atomic-spec.md` — bloco §8.3 "Herança/Delta" + Constitution Check CC-08 + RULE-HD-01..04 |
| Data | 2026-09-20 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E04_Heranca_Delta_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (Anexo A da proposta) |
| Trilha | B (Harness Cognitivo) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E04, 2026-09-20)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-20)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-20
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

Os três critérios de congelamento (parecer conforme + consenso de Andraus + registro do Controlador) estão satisfeitos.

## 2. Decisões homologadas (P1–P4 da proposta §9)

| # | Questão | Decisão |
|---|---|---|
| P1 | Código EUA-E04 + inserção §8.3 e CC-08 | **APROVADO** |
| P2 | Escopo prospectivo vs. retroativo | **HÍBRIDO** — prospectivo-obrigatório para specs novas (SPEC-002+); retroativo-como-auditoria (Harness Debt no CIC-001) para specs já homologadas. Igual a D-DHR-PAP-001-01. |
| P3 | RULE-HD-04 referência vs. cópia | **REFERÊNCIA por ID+VERSÃO**; cópia proibida. |
| P4 | Autorizar piloto em SPEC-002 antes da v1.5 | **AUTORIZADO**. |

## 3. Vigência e incorporação (A-03)

- **Vigência imediata** da emenda EUA-E04 a partir de 2026-09-20. O bloco §8.3 e o gate **CC-08** aplicam-se às specs novas (SPEC-002 em diante).
- **Incorporação diferida**: a fusão do texto no corpo do `atomic-spec` (→ **v1.5**) e a nova seção "Regras de Herança/Delta (RULE-HD)" no `RULES.md` ocorrem **após o piloto** em SPEC-002 ser auditado como CONFORME pelo Revisor (CC-08). Até lá, a autoridade literal da emenda é esta ata + a proposta homologada.

## 4. Achados do parecer — estado

| ID | Estado |
|---|---|
| A-01 (registro formal do HCH-001) | **RESOLVIDO** neste ciclo — HCH-001 registrado no CATÁLOGO como referência externa não-normativa; colisão de rótulos anotada no CONFLICT-MAP. |
| A-02 (destino no RULES.md) | Acatado na proposta §4 (nova seção RULE-HD). Incorporação efetiva na v1.5. |
| A-03 (piloto × homologação) | Acatado na proposta §7; consolidado no item 3 desta ata. |

## 5. Classificação do HCH-001 (pendência-mãe — fechada)

**HCH-001 (`CAMADA DE HARNESS.MD`) = referência externa / pano de fundo conceitual, NÃO-NORMATIVA** (mesmo status do GEH-001). Importada apenas a mecânica de herança-por-delta (esta emenda). **Fora de adoção** por colisão com baselines: H0–H4; "3Es+Economicidade" (§43-44, conflita com 4Es do CEE-001 §12); L0–L4 (§29, colide com Quality Gates L1–L4 e harness-score); M0–M7 (§53, colide com Marcos).

## 6. Próximos passos

1. Especificador redige **SPEC-002** já com o bloco §8.3 (piloto).
2. Revisor aplica **CC-08** no parecer de SPEC-002.
3. Se CONFORME → Controlador incorpora ao `atomic-spec` **v1.5** + seção RULE-HD no `RULES.md` + nova ata de incorporação.
4. Se atrito de granularidade → calibração antes da v1.5.

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado.*
