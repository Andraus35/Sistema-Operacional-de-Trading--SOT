# DHR-MC-LRN-001 — Ata de Homologação da Admissão ao Backlog (BL-015 · Camada de Learning)

| Campo | Valor |
|---|---|
| Código | DHR-MC-LRN-001 |
| Objeto | Admissão do **MC-LRN-001** (Master Contract da Camada de Learning) ao backlog como **BL-015**; promoção `Proposto → Em espera`; classificação como **referência externa não-normativa**; registro de colisão **K-MAN-18**. Correlato: fecho de **BL-014** (Absorvido) + movimentação RPIR do arquivo. |
| Data | 2026-09-21 |
| Autoridade | **Andraus** (Decisor Final) |
| Triagem | Especificador — auditoria de conformidade inicial (2026-09-21) |
| Parecer | Revisor SOT — **CONFORME** (nenhum Crítico/Médio; menores M-01/M-02/M-03; M-02 corrigido) |
| Trilha | B + canon; classificação em Trilha A (ref. externa) |
| Fonte | `reference/camadas/CAMADA APRENDIZADO.MD` (MC-LRN-001); `backlog/RMR-001` (BL-015) |

---

## 1. Ato de Homologação

```
Etapa 1 — Triagem ......... ✅ Especificador (auditoria inicial, 2026-09-21)
Etapa 2 — Registro ........ ✅ BL-015 `Proposto` + BL-014 Absorvido + arquivo movido (RPIR)
Etapa 3 — Parecer ......... ✅ CONFORME (Revisor SOT; M-02 corrigido)
Etapa 4 — Consenso ........ ✅ Andraus, 2026-09-21
Etapa 5 — Registro ........ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas

| # | Questão | Decisão |
|---|---|---|
| Q1 | MC-LRN-001 = **PROPOSTA / referência externa** (X-01 sem efeito normativo — INV-09) | **APROVADO** |
| Q2 | Admitir **BL-015** e **promover `Proposto → Em espera`** (gatilho `spec:SPEC-018 ∨ decisao:K-001 ∨ evento:governança de runtime`) | **APROVADO** |
| Q3 | **R-05:** parameter learning/calibration (§28/§43) e avaliação estatística (§41) → produzem Learning Candidate (proposta); calibração de parâmetros do Conviction (**N-001, parte de J-001**) diferida ao CCM-001/J-001/N-001 — não fecha | **APROVADO** |
| Q4 | **R-01** (G0–G10 locais), **R-02/03** (I-LRN/LRN-P locais ancorados: I-LRN-02=RULE-CAU, I-LRN-11=INV-07/RULE-BB-004, I-LRN-12=INV-09), **X-02** (estados §9 = Learning Candidate; mapear a MC-GOV §13 na fronteira; sem conflito com CHM-001) | **APROVADO** |
| Q5 | **BL-014 fechado (Absorvido)**: `CAMADA APRENDIZADO.MD` → `reference/camadas/` (obrigação RPIR/HOD-001) | **APROVADO** |
| Q6 | Registrar **K-MAN-18** no CONFLICT-MAP | **APROVADO** |

## 3. Estado e vigência

- **BL-015 = `Em espera`**. Ativa quando SPEC-018 entrar em redação, K-001 for resolvida, ou por evento de governança de runtime.
- **MC-LRN-001 = referência externa não-normativa** (`reference/camadas/`); não é baseline nem nó. Autodeclarações "BASELINE"/"BASELINE PROPOSTA" sem efeito (INV-09).
- **Face inversa do MC-GOV (CONFORME):** Learning **propõe**, Governance **decide** (LRN-P08/P14, I-LRN-12) — reforça INV-09/I-GOV-13/RULE-GMC-005/trio; **sem dupla autoridade**.
- **Fronteiras:** J-001/N-001 (calibração de parâmetros → CCM-001; MC-LRN não fecha); INV-07 (não reescreve experiência — reforça); CC-02 (Learning Candidate projeta CEM/CHM, não redefine).
- **Redundância reconhecida:** grande parte já é FATO NORMATIVO (N8–N17 + INV-07/09 + governança viva). Delta útil = operacional: Learning Candidate schema (§8), Experiment Contract (§15/LRN-SPEC-018..027: baseline/A-B/backtest/replay/OOS), overfitting/regression/OOS (§30/§23), parameter drift (LRN-SPEC-041..045 → CCM-001).

## 4. Achados do parecer — estado

| ID | Sev. | Estado |
|---|---|---|
| M-01 | Menor | **TRATADO** — status divergente registrado como "sem efeito normativo" (K-MAN-18/§5). |
| M-02 | Menor | **CORRIGIDO** — CATALOGO §0 Mapa de Pastas atualizado (BL-014 Absorvido; sem intake pendente). |
| M-03 | Informativo | Não-achado — BL-015 `Proposto` e K-MAN-18 no ato de homologação = fluxo correto (Revisor elogiou não antecipar). |

Nenhum achado Crítico ou Médio. **Diferente do MC-COG, o MC-LRN não repete o conflito grave da família** (não inventa lifecycle canônico concorrente).

## 5. Classificação do MC-LRN-001 (Q1/Q6 — fechada)

**MC-LRN-001 = referência externa não-normativa** (`reference/camadas/`; mesmo status de HCH/CMHP/MEG/MSC/MOC/MIQG/MCC/MCF/MUN/MPB/MDC/MC/MC-RAG/MC-EXP/MC-COG/MC-GOV). Fonte de requisitos de SPEC-018 (Learning/L-001) + K-001 (P12) + specs de backtest. **Não adotar sem tratamento:** status "BASELINE" (sem efeito); Quality Gates G0–G10 (→ L1–L4); I-LRN-01..15 / LRN-P01..P14 (locais); estados §9 (mapear a MC-GOV/GMC); parameter calibration (→ CCM-001/J-001/N-001). **K-MAN-18** no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. ✅ **BL-015** promovido `Proposto → Em espera` no RMR-001.
2. ✅ **K-MAN-18** registrado no CONFLICT-MAP.
3. ✅ **MC-LRN-001** classificado no CATÁLOGO como referência externa (`reference/camadas/`).
4. ✅ **BL-014 Absorvido** + arquivo em `reference/camadas/` (correlato, já efetivado na triagem).

## 7. Próximos passos

1. Na ativação (SPEC-018): mapear LRN-SPEC-001..055; aplicar R-01/R-02/R-03/R-05 + X-01/X-02; **explicitar R-05** (saída sempre Learning Candidate, nunca calibração automática do Conviction).
2. **Família de Master Contracts completa** no backlog: RAG (BL-010) · Experiência/Memória (BL-011) · Cognição (BL-012) · Governança (BL-013) · Learning (BL-015). Skills = dependência citada, **sem doc MC-SKL** no repo.
3. **SPEC-002/atomic-spec v1.5** (piloto SPEC-001, EUA-E15) e **Mapa de Auditoria** permanecem o próximo passo estrutural.

---

*Ata registrada pelo Controlador. INV-07 preservado; nada removido, apenas adicionado.*
