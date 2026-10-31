# DHR-AUDITOR-EXTERNO-008 — Ata — Reforço do Revisor interno (pacote de evidências, linter de invariantes e banco de regressão)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-11 |
| Status | **MESCLADA na `main` por Andraus (PR #103) — vigente; itens que a ata declara diferidos seguem diferidos.** *[texto anterior preservado — INV-07: "PROPOSTA — vira vigente só com o merge de Andraus."]* Depende da DHR-AUDITOR-EXTERNO-007 (pausa do auditor). Não fecha nem abre decisão; **não altera** o arquivo do Revisor, checklist, método nem regra. |
| Compatibilidade | Aditiva (INV-07). Cada item autorizado é implementado depois, em PR próprio. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Autoriza scripts, testes e um banco de regressao de apoio ao Revisor; nao altera .claude/agents/revisor.md, checklist, metodo nem regra. Mudanca no arquivo do Revisor fica para ata propria com RPSA (item R4). |

## 1. Contexto `[FATO: teste de estresse cego, 2026-10-11 — ver DHR-007 §1–2]`
O Revisor (modelo `claude-sonnet-4-6`, esforço alto, somente leitura) achou **27–28 de 30** defeitos por rodada (**29/30** na união de 3 rodadas), incluindo as 3 referências a documentos inexistentes que o Auditor não viu. Pontos fracos observados: (i) **o gate determinístico não foi executado nas 3 rodadas** (o Revisor não tem Bash — ENF-03; e os documentos de teste estavam fora de `specs/features/<SPEC>/plan.md`, único caminho que o `validate_spec_sot.py` alcança); (ii) até 3 defeitos perdidos, concentrados em **valores numéricos**; (iii) sem prova de que a perda seja sistemática (n = 30; ver limites da DHR-007 §2). **Nenhuma troca de modelo é proposta**: o resultado não a justifica.

## 2. Itens `[PROPOSTA — Andraus aprova; nada é aplicado por esta ata]`
- **R1 — Pacote de evidências de gates para o Revisor.** O Orquestrador (ou o CI) roda os gates determinísticos e entrega o `evidence.json` ao Revisor como entrada; o Revisor segue **somente leitura** (ENF-03) e cita o resultado. Reaproveita `governance/propostas/AUDITOR-EXTERNO/kit/run_gates.py` (hoje no kit do auditor, que está em pausa). Aberta: o que fazer com documentos fora de `specs/features/` (hoje sem gate de estrutura).
- **R2 — Linter de invariantes numéricos e de regra** (`scripts/check_invariants.py`), no mesmo molde do `check_doc_sync.py`: **detector, informativo, não-bloqueante** (ENF-03; encaminhamento é do Revisor/Andraus). Confere em textos de Spec: R:R mínimo 3.0 · convicção 70% e score 7/9 (limiares de Fase Piloto) · 8 dimensões do Conviction Vector, sem "custo" · hierarquia Elliott → Fibonacci → Fractal → SMC → ICT · 7 estados do CHM-001 e ausência de PROPOSED/VALIDATED · ordem dos 4Es · validade do Dossiê por complexidade (ECC-VAL-001). **Não duplica** o que o `validate_spec_sot.py` já faz: a checagem de decisão aberta tratada como fechada (STRUCT-10, que lê o ROADMAP) e a do Conviction Vector fechado (STRUCT-07) já existem — mas só rodam em `specs/features/<SPEC>/plan.md`; o R2 cobre os **valores numéricos e de ordem**, que hoje nenhum script confere, e pode rodar em qualquer `.md` indicado. Cada constante cita sua fonte (`AGENTS.md` §6/§7) e um teste verifica que a fonte ainda diz o mesmo (alarme de deriva), para o linter **não virar segunda fonte da verdade**.
- **R3 — Banco de regressão do Revisor.** Guardar o gerador de defeitos e o conferidor do teste de estresse para repetir após qualquer mudança no Revisor, **com semente nova e defeitos escritos por Andraus**. Local do material **a decidir por Andraus** (o Revisor lê o repositório; o gabarito e a base com as versões defeituosas não podem estar no que ele audita): (A) só na máquina de Andraus; (B) branch separada `ferramentas-estresse`, nunca mesclada no `main` — **recomendado**; (C) repositório privado à parte.
- **R4 — Alteração do `.claude/agents/revisor.md` — DIFERIDA, NÃO INCLUÍDA.** Ex.: "se houver `evidence.json`, cite-o; se ausente, declare o gate como limitação". Exige ata própria, autorização expressa de Andraus e classificação RPSA (muda texto de agente).

## 3. Como saber se funcionou `[PROPOSTA]`
Após R1 e R2, rodar o banco (R3) com semente nova e defeitos de Andraus. Metas propostas, a definir por Andraus: Revisor + linter ≥ 29/30 por rodada **sem aumentar as iscas tocadas**; relatório com falsos alarmes adjudicados por Andraus. **Limite honesto:** o linter e o teste partem da mesma fonte (`AGENTS.md` §6), então o banco o mede de forma otimista; os defeitos de sentido escritos por Andraus são a parte que não pode ser cobrada pelo linter.

## 4. Limites
O linter por texto pode errar para mais (falso alarme) e para menos; por isso é informativo e passa pelo Revisor. O Revisor continua com o Passo 0 e todo o protocolo GRE/HRE; nada aqui o substitui. Custo: scripts e testes locais, sem chamadas de modelo adicionais.

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 6. Registro
- [x] Esta ata · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] R1 · [ ] R2 · [ ] R3 (local a decidir) · [ ] R4 (ata própria)

---

**Andraus** — *decisão de direção em chat, 2026-10-11; registro feito pelo Orquestrador interno. Assinatura = merge desta ata.*
