# DHR-EUA-E15 — Ata de Homologação da Redesignação do Piloto de Incorporação (SPEC-001, auditoria retroativa)

| Campo | Valor |
|---|---|
| Código | DHR-EUA-E15 |
| Objeto | Emenda aditiva **EUA-E15** — redesignação do piloto de incorporação das 11 emendas (EUA-E04..E14) de "SPEC-002" para **auditoria retroativa da SPEC-001**; regime auditoria-não-reescrita; Plano de Auditoria (mapa 11 emendas + BL-008 × SPEC-001); derivação da atomic-spec v1.5 |
| Data | 2026-09-21 |
| Autoridade | **Andraus** (Decisor Final / homologação) |
| Proposta | `governance/EUA-E15_Redesignacao_Piloto_SPEC-001_PROPOSTA.md` |
| Parecer | Revisor SOT — **CONFORME** (1 achado Menor MEN-01, acatado; Anexo B) |
| Trilha | B (método/processo de incorporação) |

---

## 1. Ato de Homologação (GMC-001 Cap.5)

```
Etapa 1 — Redação da proposta ......... ✅ Especificador (EUA-E15, 2026-09-21)
Etapa 2 — Parecer de integridade ...... ✅ CONFORME (Revisor SOT, 2026-09-21; MEN-01 acatado)
Etapa 3 — Consenso .................... ✅ Andraus (Decisor Final), 2026-09-21
Etapa 4 — Registro Oficial ............ ✅ EFETIVADO (Controlador)
```

## 2. Decisões homologadas (Q1–Q4 da proposta §7)

| # | Questão | Decisão |
|---|---|---|
| Q1 | Redesignar o piloto de incorporação para **auditoria retroativa da SPEC-001** (aditivo às atas EUA-E04..E14; INV-07) | **APROVADO** |
| Q2 | Regime = **auditoria, não reescrita** (achados→CIC-001; Crítico→re-homologação por fluxo; SPEC-001 permanece baseline) | **APROVADO** |
| Q3 | Executar o **Mapa de Auditoria** (11 emendas + BL-008) e derivar a **atomic-spec v1.5** | **APROVADO** |
| Q4 | Ativar/absorver **BL-008** neste piloto; aposentar **SPEC-002** como pré-requisito | **APROVADO** |

## 3. Efeitos e vigência

- **Redesignação aditiva (INV-07):** as atas DHR-EUA-E04..E14 permanecem inalteradas; a Q5 original ("piloto SPEC-002") é preservada como registro histórico. Esta ata **acrescenta** a decisão de que o piloto de incorporação passa a ser a **auditoria retroativa da SPEC-001**.
- **Regime (D-DHR-PAP-001-01):** aplicação das emendas a spec homologada = **auditoria**, não reescrita. SPEC-001 permanece **BASELINE** (INV-09); achados não-Críticos → **CIC-001 (Harness Debt)**; achado **Crítico** → re-homologação de SPEC-001 pelo fluxo Especificador→Revisor→Andraus (nunca reescrita silenciosa).
- **BL-008** (Reavaliar SPEC-001 sob SES-001 §67) → **ATIVADO** (gatilho "antes da 1ª Engineering Card" satisfeito); será **Absorvido** por este piloto (12ª linha do mapa). Estado atualizado no RMR-001.
- **SPEC-002** deixa de ser pré-requisito do piloto (pode ser retomada futuramente para conteúdo prospectivo).
- **Consolidação:** os achados PASS/Debt derivam a **atomic-spec v1.5** + seções RULE-HD/EPI/SEM/ONT/INQ/CAU/CTF/UNC/PRB/DEC/MET no `RULES.md`, medindo o gap v1.3→v1.5.
- **Fronteiras preservadas:** J-001 não fechado; CEM/CHM não redefinidos (CC-02); baseline não reescrito (INV-09).

## 4. Achado do parecer — estado

| ID | Severidade | Constatação | Estado |
|---|---|---|---|
| MEN-01 | Menor | Schema de saída do mapa não previa "N/A (sem superfície)" para emenda sem incidência na SPEC-001 | **ACATADO** — §4 da proposta atualizado com o veredito `N/A`. |

Nenhum achado Crítico ou Médio.

## 5. Efeitos de registro (Controlador)

1. ✅ EUA-E15 marcada HOMOLOGADA na proposta; adicionada ao CATÁLOGO OFICIAL.
2. ✅ Redesignação do piloto registrada (aditiva às atas EUA-E04..E14; Q5 original preservada — INV-07).
3. ✅ **BL-008** → `ATIVADO` no RMR-001 (será `Absorvido` ao término do piloto).
4. ✅ SPEC-002 anotada como não-pré-requisito do piloto.

## 6. Próximos passos

1. **Especificador** produz o **Mapa de Auditoria** — as 11 emendas (EUA-E04..E14) + reavaliação SES-001 (BL-008) aplicadas à SPEC-001, com veredito por linha (`PASS`/`Debt`/`Crítico`/`N/A`) e âncora `arquivo:§`.
2. **Revisor** audita o mapa (CONFORME/NÃO CONFORME) e valida a classificação dos achados.
3. Achados → **CIC-001** (Debt) ou re-homologação (Crítico).
4. **Controlador** consolida a **atomic-spec v1.5** + seções RULE-* no `RULES.md`; marca **BL-008 Absorvido**.

---

*Ata registrada pelo Controlador. Registros anteriores preservados (INV-07); nada removido, apenas adicionado. A redesignação é aditiva; a SPEC-001 permanece baseline e não é reescrita — apenas auditada.*
