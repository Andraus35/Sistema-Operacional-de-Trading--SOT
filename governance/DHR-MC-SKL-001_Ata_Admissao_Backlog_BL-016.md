# DHR-MC-SKL-001 — Ata de Homologação da Admissão ao Backlog (BL-016 · Camada de Skills)

| Campo | Valor |
|---|---|
| Código | DHR-MC-SKL-001 |
| Objeto | Admissão do **MC-SKL-001** (Master Contract da Camada de Skills) ao backlog como **BL-016**; promoção `Proposto → Em espera`; classificação como **referência externa não-normativa**; registro de colisão **K-MAN-19** |
| Data | 2026-09-21 |
| Autoridade | **Andraus** (Decisor Final) |
| Triagem | Especificador — auditoria de conformidade inicial (2026-09-21) |
| Parecer | Revisor SOT — **CONFORME** (A-01/R-ARCH Médio diferido; A-02/A-03/A-04 menores) |
| Trilha | B + canon; classificação em Trilha A (ref. externa) |
| Fonte | `reference/camadas/CAMADAS SKILLS.MD` (MC-SKL-001); `backlog/RMR-001` (BL-016) |

---

## 1. Ato de Homologação

```
Etapa 1 — Triagem ......... ✅ Especificador (auditoria inicial, 2026-09-21)
Etapa 2 — Registro ........ ✅ BL-016 `Proposto` + arquivo movido raiz→reference/camadas/ (RPIR)
Etapa 3 — Parecer ......... ✅ CONFORME (Revisor SOT)
Etapa 4 — Consenso ........ ✅ Andraus, 2026-09-21
Etapa 5 — Registro ........ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas

| # | Questão | Decisão |
|---|---|---|
| Q1 | MC-SKL-001 = **PROPOSTA / referência externa** (X-01 sem efeito — INV-09) | **APROVADO** |
| Q2 | Admitir **BL-016** e **promover `Proposto → Em espera`** (gatilho `spec:SPEC-025 ∨ decisao:I-001`) | **APROVADO** |
| Q3 | **R-ARCH (achado central):** Skill≠agente **REJEITADO como reenquadramento imediato**; prevalecem CC-01/hierarquia/RULE-EW-SM-ICT; decisão **diferida a SPEC-025/I-001** | **APROVADO** |
| Q4 | R-01 (G0–G13 locais), **R-02b (Skill Depth LEVEL 0–5 locais)**, R-03 (I-SKL/SKL-P locais ancorados), R-05 (calibração→CCM-001/J-001 — não fecha), X-01/X-02 | **APROVADO** |
| Q5 | Mover `CAMADAS SKILLS.MD` → `reference/camadas/` (RPIR — feito) | **APROVADO** |
| Q6 | Registrar **K-MAN-19** no CONFLICT-MAP | **APROVADO** |

## 3. Estado e vigência

- **BL-016 = `Em espera`**. Ativa quando SPEC-025 entrar em redação ou I-001 for resolvida.
- **MC-SKL-001 = referência externa não-normativa** (`reference/camadas/`); não é baseline nem nó. Rótulos "MASTER SPECIFICATION"/"MASTER CONTRACT BASELINE" sem efeito (INV-09).
- **R-ARCH (fronteira soberana):** a arquitetura de agentes vigente permanece intacta — **Elliott/SMC/ICT continuam agentes** (RULE-EW/SM/ICT, hierarquia CC-01/RULE-001/RULE-008); a proposta "Skill≠agente" é **matéria de SPEC-025/I-001**, sem reenquadramento automático agora.
- **Fronteiras:** J-001/INV-03 abertos (calibração de confiança → CCM-001; não fecha); CC-02 (Skill não redefine CEM/CHM/CCM/CDM/CNM); INV-07/09 (Learning/Governança sobre a Skill via MC-LRN/MC-GOV — SKL-P14/P21, I-SKL-13/15).
- **Coerência com a família (§37):** Skill usa RAG/COG/EXP/LRN/GOV sem criar autoridade própria (SKL-P11/P12); Learning propõe, Governança decide.

## 4. Achados do parecer — estado

| ID | Sev. | Estado |
|---|---|---|
| A-01 (R-ARCH) | Médio | **DIFERIDO** a SPEC-025/I-001 (registrado em K-MAN-19; não toca CC-01/agentes agora). |
| A-02 (X-01) | Menor | **TRATADO** — status sem efeito normativo (INV-09). |
| A-03 (R-01/R-02b) | Menor | **REGISTRADO** (K-MAN-19) — G0–G13 e LEVEL 0–5 = namespaces locais. |
| A-04 (K-MAN-19) | Menor | **EFETIVADO** nesta homologação (fluxo correto — não era defeito de triagem). |

Nenhum achado Crítico. Nenhuma violação de invariante/salvaguarda no estado atual (doc não-normativo, não toca Conviction nem produz sinal).

## 5. Classificação do MC-SKL-001 (Q1/Q6 — fechada)

**MC-SKL-001 = referência externa não-normativa** (`reference/camadas/`; mesmo status dos demais). Fonte de requisitos de **SPEC-025** (Skills, I-001). **Não adotar sem tratamento:** Skill≠agente (→ SPEC-025, sem tocar CC-01); Quality Gates G0–G13 e Skill Depth LEVEL 0–5 (→ locais); I-SKL-01..20 / SKL-P01..P24 (locais ancorados); calibração (→ CCM-001/J-001). **K-MAN-19** no CONFLICT-MAP.

## 6. Efeitos de registro (Controlador)

1. ✅ **BL-016** promovido `Proposto → Em espera` no RMR-001.
2. ✅ **K-MAN-19** registrado no CONFLICT-MAP.
3. ✅ **MC-SKL-001** classificado no CATÁLOGO como referência externa (`reference/camadas/`).
4. ✅ Arquivo movido (RPIR) — correlato já efetivado na triagem.

## 7. Próximos passos

1. Na ativação (SPEC-025/I-001): resolver Skill-vs-agente (R-ARCH); mapear SKL-SPEC-001..095; aplicar R-01/R-02b/R-03/R-05 + X-01/X-02.
2. **Família de Master Contracts COMPLETA** no backlog: RAG (BL-010) · Experiência/Memória (BL-011) · Cognição (BL-012) · Governança (BL-013) · Learning (BL-015) · Skills (BL-016). Todas ref. externas `Em espera`; nenhuma dependência sem doc.
3. Próximo passo estrutural permanece o **piloto SPEC-001 (EUA-E15) → atomic-spec v1.5** (Mapa de Auditoria das 11 emendas).

---

*Ata registrada pelo Controlador. INV-07 preservado; nada removido, apenas adicionado.*
