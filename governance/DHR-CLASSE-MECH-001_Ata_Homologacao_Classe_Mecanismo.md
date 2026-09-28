# DHR-CLASSE-MECH-001 — Ata de Homologação — Taxonomia de Classe/Mecanismo de Implementação

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | Análise de acoplamento (2026-09-27, sessão de governança) — proposta CLASSE-MECH-001, BL-023 (RMR-001) |
| Data | 2026-09-27 |
| Status | **HOMOLOGADA — vigência imediata, prospectiva** |
| Compatibilidade | Minor (emenda de refinamento — não redefine nenhum invariante ou modelo canônico) |

---

## 1. Decisão

**CLASSE-MECH-001 está HOMOLOGADA**, com o desenho fechado nesta mesma sessão (2026-09-27):

- Taxonomia: **Classe D** (Determinístico) · **Classe H** (Híbrido) · **Classe P** (Probabilístico com Gate) · **Classe C** (Constitutivo — renomeada de "Classe E" para não colidir com "Engine"/PE-04 nem com a escala de risco E0–E3).
- Natureza: **emenda de refinamento a PE-04** (GPR-001) — D/C são variantes de Skill (determinísticas); H/P são variantes de Engine (probabilísticas). Não é taxonomia paralela, não redefine PE-04.
- Granularidade: declaração **por BASpec/Engineering Card**, nunca por Spec inteira — mesma granularidade dos Enforcement Contracts (atomic-spec §10.3) — preserva SES-001 §50 (nenhum agente cognitivo reduzido a checklist/executor por uma única Classe).
- Vigência: **prospectiva — NÃO retroage** sobre Specs já homologadas (SPEC-001, SPEC-019, SPEC-020). Incide a partir de SPEC-002 (primeira Spec de agente de domínio a abrir).

---

## 2. Efeitos imediatos desta homologação

1. **RULE-MECH-01..04 — FATO NORMATIVO com vigência imediata.** Registradas em `governance/RULES.md`, nova seção "Regras de Classe/Mecanismo (RULE-MECH)".
2. **GPR-001 — EMENDA CLASSE-MECH-001** aplicada (refinamento de PE-04); texto original de PE-04 preservado (INV-07). Novo item no checklist §15.
3. **atomic-spec.md** — emenda registrada no cabeçalho; §9 ganhou nota de refinamento; §10.5 ganhou **CC-11**; nova seção **§10.6** (Declaração de Classe/Mecanismo, extensão da BASpec). Sem bump de versão (v1.4 permanece pinada para a FASE GOV, DHR-EUA-E17 §3) — mesmo padrão da Emenda EUA-E21.
4. **`.claude/agents/especificador.md`** — CC-11 incorporado ao checklist do §7 Autopré-check; novo item de autopré-check (determinar Classe antes do corpo de cada BASpec, a partir de SPEC-002).
5. **`.claude/agents/revisor.md`** — CC-11 incorporado ao Passo 3 (Constitution Check) e à referência de leitura obrigatória.
6. **CC-11 só incide em Specs que citam RULE-MECH-01 no próprio texto** (SPEC-002 em diante) — não é achado retroativo em SPEC-001/019/020.
7. **`scripts/validate_spec_sot.py`** — check estrutural automatizado (STRUCT-12) **DIFERIDO**: sem Spec concreta usando Classe ainda, um check automatizado agora seria engenharia prematura. Registrar como item de tooling quando SPEC-002 entrar em redação (mesmo padrão do BL-021 para EUA-E21).
8. **PRINC-BID-001 (BL-022) permanece separada e aberta** — CLASSE-MECH-001 não a resolve nem depende dela tecnicamente; ambas compartilham só o ponto de inserção no template e a meta de fechar antes de SPEC-002.

---

## 3. Pendências registradas (não bloqueiam esta homologação)

| ID | Descrição | Encaminhamento |
|---|---|---|
| P-01 | STRUCT-12 (check determinístico de Classe/CC-11 em `validate_spec_sot.py`) diferido | Implementar quando SPEC-002 entrar em redação e houver BASpec real para validar |
| P-02 | CC-08/09/10 (EUA-E04/05/06) — achado incidental: citadas em `revisor.md`/`especificador.md`/pareceres, mas **nunca haviam sido fisicamente inseridas** em `atomic-spec.md` §10.5 (só existiam nas PROPOSTAs originais) | **TRATADO** (Andraus, 2026-09-27, mesmo dia — ver Adendo §5) |

---

## 5. Adendo — Regularização de P-02 (2026-09-27, mesmo dia)

Por instrução de Andraus, CC-08 (EUA-E04, texto de `EUA-E04_Heranca_Delta_PROPOSTA.md` §5), CC-09 (EUA-E05, `EUA-E05_Epistemic_Check_PROPOSTA.md` §5) e CC-10 (EUA-E06, `EUA-E06_Camada_Semantica_PROPOSTA.md` §6) foram inseridos fisicamente em `atomic-spec.md` §10.5, com os textos originais das respectivas PROPOSTAs homologadas (sem alteração de conteúdo — INV-07). Nota explícita no arquivo: esta é **regularização retroativa**, não nova obrigação — os três itens já eram vigentes e citados como tal desde suas homologações originais (2026-09-20); SPEC-019 e SPEC-020 já foram avaliadas sob CC-08/09/10 nos seus próprios pareceres do Revisor, então não há reabertura de gate para elas.

- [x] `atomic-spec.md` §10.5 — CC-08/09/10 inseridos com texto original; cabeçalho anotado.
- [x] Ordem física da tabela corrigida (CC-08→09→10→11, sequencial).
- [x] Confirmado por `check_refs.py` (0 ERRO/0 WARN), `backlog_triggers.py` (0 disparos indevidos), gate determinístico revalidado em SPEC-019/020 (PASS, sem regressão), 47/47 testes Python + 11/11 schemas Node.

---

## 4. Registro do Controlador (efeitos aplicados — 2026-09-27)

- [x] `atomic-spec.md` — emenda no cabeçalho; §9 nota de refinamento; §10.5 CC-11 + nota de aplicabilidade; §10.6 novo (Declaração de Classe/Mecanismo).
- [x] `governance/GPR-001_Guia_Principios_Relacoes_SOT.md` — nova seção "EMENDA — CLASSE-MECH-001 (Refinamento de PE-04)"; novo item no checklist §15.
- [x] `governance/RULES.md` — comentário de cabeçalho; nova seção "Regras de Classe/Mecanismo (RULE-MECH)" com RULE-MECH-01..04.
- [x] `.claude/agents/especificador.md` — CC-11 no checklist §7; novo item de autopré-check.
- [x] `.claude/agents/revisor.md` — CC-11 no Passo 3; referência CC-01..CC-11 atualizada.
- [x] `ROADMAP.md` — CLASSE-MECH-001 movida de "Decisões abertas ativas" para "Decisões FECHADAS".
- [x] `governance/CATALOGO-OFICIAL.md` — nova linha de ata registrada.
- [x] `backlog/RMR-001_Painel_Backlog.md` — BL-023 → `Absorvido`; passo 11-bis registrado.
- [x] `docs/mapa/` regenerado e verificado (`--check`).
- [x] Suíte de testes (Python + Node) revalidada; gate determinístico revalidado em SPEC-019/020 (não afetadas retroativamente).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
