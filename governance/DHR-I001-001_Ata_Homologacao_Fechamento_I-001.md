# DHR-I001-001 — Ata de Homologação — Fechamento de I-001 (Skills como unidades formais separadas?)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador de Especificação do SOT / Revisor / Controlador |
| Ref | `governance/BRIEFING-DECISAO-I-001.md` (brief de decisão, 2026-09-28) |
| Data | 2026-09-28 |
| Status | **I-001 — FECHADA (direção)** |
| Compatibilidade | Minor (decisão de princípio; detalhe de plataforma diferido ao Dossiê de SPEC-025) |

---

## 1. Decisão

**I-001 — "Skills como unidades formais separadas?" — FECHADA.** Direção escolhida: **Opção C (híbrida por Classe)** do brief — Skills Classe D (determinísticas, certificáveis, reutilizáveis) são formalizadas como unidades separadas; competências Classe P (julgamento qualitativo — ex.: leitura estrutural Elliott, narrativa institucional SMC) permanecem comportamento interno do agente, não uma "Skill" separada.

**Não fechado por este ato (CONS-01):** o critério de corte exato entre o que é Classe D isolável e o que não é — isso é matéria do Dossiê de Pesquisa na abertura formal da SPEC-025, não desta decisão de princípio.

**Confirmações:**
- **CC-01** (hierarquia Elliott→Fibonacci→Fractal→SMC→ICT) permanece intocada — nenhuma opção do brief a tocava, e a Opção C não introduz exceção.
- Compatível com **RULE-MECH-01..04** (CLASSE-MECH-001) — o eixo de corte D-vs-P já existe na taxonomia homologada; I-001 aproveita esse eixo em vez de criar um novo.
- Achado **R-ARCH** do BL-016 (Skill≠agente) é respeitado — a Opção C não colapsa Skill em agente nem o inverso.

---

## 2. Efeitos imediatos

1. `atomic-spec.md` §12 — I-001 marcada FECHADA (linha da tabela + bloco "FECHADA por Andraus").
2. `ROADMAP.md` — "Decisões abertas ativas" (Estado atual) e §15 (SPEC-025) atualizados.
3. `governance/CATALOGO-OFICIAL.md` §7 — lista de decisões abertas/fechadas atualizada.
4. `backlog/RMR-001_Painel_Backlog.md` — **BL-016** (MC-SKL-001): gatilho `decisao:I-001 resolvida` DISPARA → `Em espera` → `ATIVADO`. Encaminhamento (per a própria "Ação ao ativar" do item): mapear SKL-SPEC-001..095 contra R-ARCH; aplicar G0–G13/LEVEL 0–5 locais; classificar ref. externa (já feito) + K-MAN-19 (já registrado). Isso NÃO abre SPEC-025 — é o encaminhamento de análise que o próprio BL-016 previu para quando I-001 fechasse.
5. Sliver Bloco S de SPEC-025 (template/plataforma, per `governance/AUDITORIA-ADIANTAMENTO-SLOTS-ROADMAP-2026-09-28.md`) sobe a candidato a Dossiê antecipado/linha paralela (modelo SPEC-046) — decisão de abrir ou não permanece de Andraus, em ato separado.

---

## 3. Registro do Controlador (a aplicar)

- [x] `governance/DHR-I001-001_...md` — este documento.
- [x] `atomic-spec.md` §12 — I-001 FECHADA.
- [ ] `ROADMAP.md` — Estado atual + §15.
- [ ] `governance/CATALOGO-OFICIAL.md` §7.
- [ ] `backlog/RMR-001_Painel_Backlog.md` — BL-016 → `ATIVADO`.
- [ ] `python scripts/check_refs.py` + `python scripts/build_map.py --check`.

**Pendência (fora deste registro):** decisão de Andraus sobre abrir Dossiê antecipado de SPEC-025 (sliver S) como linha paralela — não decidida agora.

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
