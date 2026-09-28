# DHR-EUA-E21 — Ata de Homologação: Especificação Emergente (ROADMAP como direção e restrições; Specs definidas na abertura após Dossiê de Pesquisa web)

| Campo | Valor |
|---|---|
| Código | **DHR-EUA-E21** |
| Objeto | Homologação da emenda **EUA-E21 v2** (`governance/EUA-E21_Especificacao_Emergente_Pesquisa_Web_PROPOSTA.md`) — **RULE-ECC-01** (definição emergente das Specs) e **RULE-ECC-02** (Dossiê de Pesquisa obrigatório na abertura); **RULE-ECC-03 RESERVADA** |
| Natureza | Emenda **normativa de método** — muda o significado normativo da lista de Specs do ROADMAP (de lista fechada para direção + restrições). **Nenhuma Spec homologada é reescrita.** |
| Compatibilidade | **Major-leve** (semântica do ROADMAP; nenhum objeto removido — INV-07) |
| Data | 2026-09-26 |
| Vigência | **Imediata.** |
| Status | **HOMOLOGADA — BASELINE** |

---

## 1. Fluxo de autoridade (RULE-HG-01 / RULE-HG-08; GMC-001 Cap.5)

```
Etapa 1 — Diretiva de Andraus (chat, 2026-09-26) ........... ✅ ROADMAP não pré-determina Specs/quantidades; definição na abertura após pesquisa web de estado da arte pelo Especificador
Etapa 2 — Formalização (EUA-E21 v1) ........................ ✅ Especificador — NADA aplicado a baseline
Etapa 3 — Parecer do Revisor (v1) .......................... ✅ NÃO CONFORME RECUPERÁVEL (M-01 · M-02 · M-03 + Me-01..Me-05; nenhum Crítico; §1 verificado)
Etapa 3b — v2 + revisão reduzida ........................... ✅ CONFORME (todos resolvidos; 1 Menor editorial novo, Me-06, corrigido no registro)
Etapa 4 — Consenso ......................................... ✅ Andraus (Decisor Final), 2026-09-26 — "implementar as decisões Q1–Q9" (ver §2)
Etapa 5 — Registro Oficial / aplicação ...................... ✅ EFETIVADO (Controlador) — esta ata + edições de baseline (§4)
```

Os três critérios de congelamento (GMC-001 Cap.5) satisfeitos: parecer CONFORME + consenso do Usuário + registro pelo Controlador. **Ordem respeitada: nada foi aplicado antes do parecer CONFORME.**

## 2. Decisões de Andraus (Q1–Q9) — e o que foi interpretado

Andraus ordenou, em chat, *"implementar as decisões Q1–Q9 com segurança, governança e melhores práticas"*, sem enunciar respostas individuais. **Interpretação registrada (e reversível por emenda aditiva):** adoção das **recomendações da §8 da proposta**. Onde a recomendação era "Andraus define", a decisão **permanece aberta** — nenhuma resposta foi inventada.

| # | Questão | Decisão registrada |
|---|---|---|
| **Q1** | Adotar RULE-ECC-01 (ROADMAP = direção e restrições) | **SIM** |
| **Q2** | Adotar RULE-ECC-02 (Dossiê obrigatório, fail-closed, auditado pelo Revisor) | **SIM** |
| **Q3** | Números SPEC-002…045 = slots indicativos (nunca apagados; SPEC-001/019 preservadas) | **SIM** |
| **Q4** | SPEC-020 núcleo A | **PILOTO** — 1ª aplicação do Dossiê; a autorização de posição permanece |
| **Q5** | Profundidade proporcional à complexidade; validade do Dossiê | **Proporcional: SIM.** **Validade: NÃO definida** → decisão aberta **ECC-VAL-001** (Andraus) |
| **Q6** | RULE-ECC-03 / "modelo de especialização" | **NÃO respondida** → RULE-ECC-03 **RESERVADA**; decisão aberta **ECC-03-001** (a sigla ECC não é expandida no repositório) |
| **Q7** | Revisor com web só-leitura | **NÃO agora** → **BL-020** (`Proposto`; reavaliar após o piloto) |
| **Q8** | "Passo 1 — Proposta de Redistribuição" | **ADIADO / SUPERSEDIDO** — redistribuição abertura-a-abertura; ata DHR-PROV-WEB-001 intacta (INV-07) |
| **Q9** | Código EUA-E21 e RULE-ECC-01/02 | **SIM** |

## 3. Objeto homologado

- **RULE-ECC-01:** o ROADMAP fixa direção e restrições; número, quantidade, fronteira e decomposição de cada Spec são definidos **na abertura**, por proposta do Especificador e homologação de Andraus, **antes do Plan**. Slots indicativos nunca apagados; número definitivo monotônico e nunca reutilizado; capacidade exigida sem Spec = achado de gate; gatilho do RMR-001 para slot alterado exige **re-apontamento homologado**.
- **RULE-ECC-02:** **Dossiê de Pesquisa** obrigatório (pelo próprio Especificador; questões e estratégia; fontes classificadas `[EXTERNO]`; comparação adotar/adaptar/rejeitar/adiar; lacunas; escopo resultante). **Fail-closed**: sem Dossiê, sem proposta; o Revisor emite NÃO CONFORME Crítica. Salvaguardas da DHR-PROV-WEB-001 mantidas.
- **RULE-ECC-03:** RESERVADA, sem texto.

## 4. Efeitos registrados (edições de baseline)

| Documento | Alteração (aditiva) | Estado |
|---|---|---|
| `ROADMAP.md` | Emenda vigente adicional (cabeçalho) · banner de vigência (slots indicativos) · linha "Próximo trabalho autorizado" (SPEC-020 = piloto) · linha "Decisões abertas ativas" (+ECC-VAL-001, +ECC-03-001) · §21 (orientação de dependência) · §22 (quantidade não pré-determinada) · §23 (**passo 1-bis**) · **§26 Capacidades exigidas** (derivada dos títulos dos slots) | ✅ aplicado |
| `atomic-spec.md` | Emenda EUA-E21 no cabeçalho + **§15 Abertura de Spec e Dossiê de Pesquisa** | ✅ aplicado |
| `governance/RULES.md` | RULE-ECC-01, RULE-ECC-02, RULE-ECC-03 (RESERVADA) | ✅ aplicado |
| `.claude/agents/especificador.md` | §4 item 2 (pesquisa **obrigatória** na abertura) · §2.1 atualizado · item no Autopré-check §7 · `sincronizado-até` → **DHR-EUA-E21** · `required_sources` | ✅ aplicado |
| `.claude/agents/revisor.md` | **Passo 4-bis** (auditoria do Dossiê: ausente/importação automática = Crítica; incompleto = Médio; classificação/etiqueta = Menor; declara não navegar na web) · `sincronizado-até` → **DHR-EUA-E21** · `required_sources` | ✅ aplicado |
| `backlog/RMR-001_Painel_Backlog.md` | Regra de **re-apontamento de gatilhos** (§3) · **BL-020** e **BL-021** (`Proposto`) · Passo 11-bis desta homologação | ✅ aplicado |
| `governance/CATALOGO-OFICIAL.md` | Linha EUA-E21 (emendas) + linha DHR-EUA-E21 (atas) | ✅ aplicado |
| `AGENTS.md` | §5 (princípio da abertura de Spec) + §7 (duas decisões abertas novas) — *consequente; não constava do §4 da proposta, registrado por coerência com CONS-01* | ✅ aplicado |
| `governance/EUA-E21_..._PROPOSTA.md` | Status → HOMOLOGADA + notas (Me-06 corrigido) | ✅ aplicado |
| `governance/RCH-001_Registro_Ciclos_Hygiene.md` | Adendo (aditivo) | ✅ aplicado |

## 5. NÃO aplicado (deliberadamente)

- **Ferramental** (`check_refs`, `backlog_triggers`, `build_map`, `validate_spec_sot`): a proposta (§7) exigia **aprovação própria** → **BL-021** (`Proposto`; gatilho `spec:SPEC-020 em redação`). Consequência conhecida: o mapa ainda rotula os slots como "Planejada (ROADMAP)" e os verificadores continuam assumindo numeração estável até o BL-021.
- **Nenhum slot foi reclassificado por Spec** além do banner e do §26; nenhuma Spec foi aberta ou dividida.
- **GLOSSARIO:** os termos "slot indicativo" e "Dossiê de Pesquisa" não foram inseridos (fora do §4 da proposta); ficam definidos em RULE-ECC-01/02 e atomic-spec §15.

## 6. Invariantes preservados

- **CONS-01:** nenhuma decisão aberta fechada. **Duas novas abertas** (ECC-VAL-001, ECC-03-001). SPEC-020-PRINC-001 e SPEC-045-RUNTIME-001 seguem abertas e, se o escopo/número da Spec a que estão atreladas mudar, **migram com a Spec** (regra da §5 da EUA-E21).
- **INV-07/INV-09:** nada deletado; atas e propostas anteriores intocadas; a pesquisa nunca vira baseline.
- **ENF-03:** `revisor.md` continua sem Write/Edit e **sem acesso web**.
- **RPSA (EUA-E16):** `sincronizado-até` de ambos os agentes → **DHR-EUA-E21** (última DHR em escopo).
- **EUA-E19/E22:** roteamento de modelo e regra R-MAPA inalterados. **SPEC-001 e SPEC-019:** baseline, sem reabertura.
- **RULE-MET-01:** riscos residuais da EUA-E21 (§6) aceitos como decisão consciente — o Revisor não verifica a veracidade das fontes; injeção via web mitigada, não eliminada; pesquisa é probabilística (só a estrutura do Dossiê é verificável).

## 7. Encaminhamento

1. **Passo 11-bis (ROADMAP §23):** consultado `backlog/RMR-001` — nenhum item existente disparou; BL-008 segue `ATIVADO` (independente); BL-020/BL-021 criados como `Proposto`.
2. **Pendências de Andraus:** definir **ECC-VAL-001** (validade do Dossiê) e o escopo da **RULE-ECC-03** (**ECC-03-001**).
3. **Próximo trabalho autorizado:** SPEC-020 — núcleo A, agora como **piloto do Dossiê de Pesquisa** (passo 1-bis do §23).

**Nota de registro (correção do Controlador, mesma data):** a seção de capacidades exigidas foi inicialmente numerada §24 no ROADMAP, colidindo com a §24 "Princípio central" já existente; foi renumerada para **§26** (§24 e §25 preexistentes intactas) e todas as citações foram corrigidas antes da entrega.

---

*Ata registrada pelo Controlador (Claude Code) a partir da homologação de Andraus (Decisor Final), 2026-09-26, comunicada em chat — a decisão é de Andraus; este registro não a substitui. Parecer do Revisor: CONFORME (v2). Nenhum registro anterior removido — apenas aditado (INV-07/INV-09).*
