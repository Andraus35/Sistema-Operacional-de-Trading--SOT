---
tipo: proposta-de-auditoria
status: PROPOSTA (não vigente; nada aplicado)
data: 2026-11-01
autor: Orquestrador (sessão de nuvem)
alvo: .claude/agents/especificador.md (Autopré-check §7 e §7-bis) e a cadeia de gates antes do Revisor
---

# Auditoria do Especificador — Autopré-check e prevenção determinística de erros

> **Natureza.** Proposta de auditoria (ENF-03: Detector, não Gate). Não altera `.claude/agents/*`, `AGENTS.md` nem `governance/MECANISMOS.json`; cada item abaixo só vira mecanismo por ordem expressa de Andraus, com `MECANISMOS.json` no mesmo PR (COE-14). Não fecha decisão aberta (CONS-01). Pesquisa web = **[EXTERNO]**, classificada como Prática/Opinião, **sem captura verbatim** (fora do escopo de RULE-ECC-04, que vale para Specs) — logo, evidência **Fraca**: motiva, não fundamenta.

## 1. Resumo

O Autopré-check é, hoje, **auto-atestação textual** de ~35 caixas. Só 14 verificações estruturais (`validate_spec_sot.py`, STRUCT-01..14) são código; elas medem **presença**, não **consistência**. Os erros que mais custam rodadas (C01 contradição/propagação, C07 âncora, C02 vocabulário, C06 contagem) são de consistência — e **nenhum detector atual os pegou** no Plan v1.0 da SPEC-049 (backtest, §3). Há ainda uma falha de contrato: o Especificador não tem `Bash`, mas o §7 manda ele "rodar" scripts.

## 2. Achados da auditoria (verificados no repositório)

| ID | Sev. | Achado | Evidência |
|---|---|---|---|
| **A-1** | Alta | **Contrato impossível.** O frontmatter dá ao Especificador `Read/Write/Edit/Grep/Glob/WebSearch/WebFetch` (sem Bash), mas o §7 manda ele rodar `validate_spec_sot.py`, `check_repo_research.py`, `build_map.py --check` e `backlog_triggers.py --abertura` (especificador.md l.98, 229, 231, 233). Quem de fato roda é o Orquestrador (HANDOFF §3), mas o Especificador declara "Pronto para revisão" **sem prova mecânica anexa**. | especificador.md l.9-16 vs l.98/229/231/233 |
| **A-2** | Alta | **Detectores no lado errado do funil.** `gate_extra.py` (citações arquivo+linha, contagens declaradas, decisão aberta fechada, assertivas do checks.md) e `revisor_detectores.py` (ID inexistente, valor×fonte, DHR de backlog…) só são chamados por `revisor_gate.py`. O autor não os recebe antes; o Revisor gasta rodada no que código acha. | `grep gate_extra\|revisor_detectores scripts/*.py .github/workflows/*` → só `revisor_gate.py` |
| **A-3** | Alta | **Autopré-check não deixa rastro verificável.** Nos Plans recentes aparece em 3–4 linhas de prosa; nenhum arquivo liga cada caixa a um comando, exit code ou hash. O Revisor não sabe quais itens foram provados e quais só afirmados. | SPEC-048 plan.md (4 menções), SPEC-049 (3 + 1 em checks.md) |
| **A-4** | Alta | **Lacuna entre o que o gate mede e o que o Revisor acha.** STRUCT-01..14 = presença/forma. Backtest: 0 detecções em 3 Médias reais (§3). | §3 |
| **A-5** | Média | **O próprio especificador.md carrega fatos defasados** (o mesmo defeito C01/C04 que ele deveria prevenir): `§8.1 l.301` "produz o Trading Mission Package (TMP)" (AGENTS §6.9 / EUA-E19a: o produto é o **Signal Package**; TMP é interno); `l.217` "AGENTS.md §3" (profundidade está no §4); `l.310/316` "CCM-001 pendente de redação / trava SPEC-003" (CCM-001 BASELINED 2026-10-02); `l.200` "CC-01..CC-10" listando até CC-12; `§9` repete a lista de decisões abertas (o ROADMAP prevalece — parecer SPEC-020 achou exatamente esta cópia defasada). | leitura integral do arquivo |
| **A-6** | Média | **Gates úteis são todos informativos** (`check_refs`, `check_invariants`, `check_dimensionamento`, `fato_locais`): o autor vê WARN e nada o obriga a zerar. Promoção só por ordem de Andraus (AGENTS §8). | MECANISMOS.json; docstrings |
| **A-7** | Média | **`checks.md` marca ✔ sem evidência** (achado real SPEC-049 Plan R1-M01); `assertivas_checks` só executa linhas "Corrigido" com `assert-present/absent` — 39 assertivas no repo todo; ✔ comum não é conferido. | ledger CAUSAS (C05), `gate_extra.corrigidos_sem_assertiva` |
| **A-8** | Baixa | `sincronizado-até` (l.17) é uma linha de ~11 KB que duplica o livro-razão `rpsa-ledger.json`; custo de leitura em todo turno do Especificador sem ganho (Economicidade — **medir antes de cortar**, 4Es). | tamanho do frontmatter |
| **A-9** | Baixa | §7-bis (Bloco A/B/C) é pergunta mental ("o que mudaria se estivesse errada?") — viés de confirmação residual já admitido no próprio texto; não há mutação executável. | especificador.md l.236-243 |

**O que está bem (manter):** gate manifest com hash protege os scripts de enfraquecimento pelo autor; classe M determinística do Orquestrador (`aplicar_ficha_m.py`); delta por hash; R-AC5..R-AC7; `fato_locais.py` (P7) como semente certa.

## 3. Backtest (medido, não opinião)

1. **Detectores atuais × Plan SPEC-049 v1.0/v1.1/v1.2** (commits `f1143be~1`, `f1143be`, `ade62b6`): `citacoes_arquivo_linha`, `contagens_declaradas`, `decisoes_abertas_fechadas`, `assertivas_checks`, `id_norma_inexistente`, `valor_fonte`, `contagem_declarada`, `dhr_backlog` → **0 achados em todas**. O parecer R1 deu **3 Médias** (códigos fail-closed sem linha na D3.1 e ✔ sem evidência; "byte a byte" sem listar influências; unicidade "única relação" falsa). **Recall atual nesta amostra: 0/3** (falsos alarmes: 0). *(Nota: STRUCT-11/12 falham na cópia temporária só por falta do `research.md`; artefato do teste, não achado.)*
2. **72 achados estruturados** de SPEC-006/020/048/049 por categoria: C01 15 · C02 11 · C07 10 · C04 9 · C08 8 · C06 8 · C05 7 · C03 2 · C10 2.
3. **Classificação manual (minha, não gabarito):** ≈ **1/3** (~25 de 72) tem sinal **sintático** que um detector comum captura — token/literal obsoleto após correção, número que difere entre `plan`/`checks`/`research`/`ABERTURA`, código/ID usado sem definição (ou definido sem uso), lista de IDs/linhas incompleta, referência interna "seção N" que aponta para outro lugar, ✔ sem âncora. O resto (~2/3) é **semântico** (pré-condição ausente, regras que se contradizem, falta de precedência) e **não** se resolve por detector: resolve-se por **modelo/gabarito obrigatório na construção** (§4-D) e pelo Revisor.
   Limites: amostra pequena e enviesada (Specs recentes), classificação por um só avaliador; tratar como ordem de grandeza.

## 4. Propostas determinísticas (todas Classe D; em ordem de valor ÷ custo)

> Regra de equilíbrio dos 4Es: cada item traz como **medir antes de promover**.

### P-A — `pre_entrega.py` (a criar; pré-gate unificado, só composição)
Roda, num único comando e sobre um `specs/features/<SPEC>/`: `validate_spec_sot` · `gate_extra` (todas as funções) · `revisor_detectores` · `check_refs` (escopo da Spec) · `check_dimensionamento` · `check_repo_research` · `backlog_triggers --abertura` · `fato_locais` (§P-C2) · `check_invariants` · `build_map --check`. Saída: `pre-entrega.json` com `sha256` do `plan.md`/`checks.md`, exit code e hash por verificação. **Nenhuma lógica nova** — reaproveita scripts já selados. Resolve **A-1, A-2**.
- Quem roda: Orquestrador (em nuvem) ou hook; o Especificador **não ganha Bash** (Bash + conteúdo web não confiável = superfície de injeção; manter ENF-03). Alternativa a considerar: ferramenta MCP somente-leitura com allowlist (como `sot-revisor-gate`), ressalvando que ela fica **inerte em nuvem**, igual à do Revisor.
- Fluxo: Especificador edita → Orquestrador roda → devolve o JSON → corrige-se até **zero erro bloqueante** → só então "Pronto para revisão" e o Revisor recebe o mesmo `pre-entrega.json` (casado por `SHA256-ALVO`).
- **Medir:** em 5 rodadas, nº de Médias do R1 com vs sem pré-gate (hoje R1 = 3–9 Médias; SPEC-049 Plan ≈ 1,39 M tokens em 3 rodadas).

### P-B — Autopré-check legível por máquina (Proof Gate / quote gate)
Dar ID a cada caixa (AP-01…), em `checks.md` ou `autoprecheck.md`, no formato `| AP-xx | mecanismo ou ATESTADO | evidência |`. Linter determinístico reprova: caixa sem linha; `[x]` sem evidência; evidência com comando que não consta do `pre-entrega.json`; itens **ATESTADO** sem âncora literal (arquivo+trecho ≥100 caracteres, verificado por `grep`, no espírito da RULE-ECC-04). Efeito principal: **o Revisor passa a saber onde focar** (itens ATESTADO) — resolve **A-3, A-7**. Cuidado ([EXTERNO], Fraca): o autor **não** escreve nem enfraquece os checks (FleetProof alerta para isso); aqui o catálogo de verificações é fixo, selado em `GATE-MANIFEST.sha256`.

### P-C — Detectores novos (os de maior recall esperado, atacando C01/C07/C05/C06)
1. **C-1 Fechamento de conjuntos de identificadores:** códigos de erro (`[A-Z]+_[A-Z0-9_]+`), `ADV-/EC-/RULE-/INV-/Cenário-/BASpec-`: (i) usado no corpo/EARS/checks sem definição na tabela canônica; (ii) definido e nunca usado; (iii) lista `INHERITS` ≠ IDs citados no corpo. Pegaria "recusa sem código na D3.1", "`ENTREGA_NAO_CONFIRMADA` sem prefixo", "INHERITS omite ADV-KFH-01/EC-KFH-004".
2. **C-2 Propagação derivada do git (sem lista manual):** diff do `plan.md` contra a versão anterior; cada token alterado (número, ID, código, rótulo) é procurado **nas demais ocorrências** do diretório da Spec (`plan`, `checks`, `research`, `ABERTURA`; excluindo changelog/histórico INV-07) e reportado como "token antigo ainda presente em N locais". Evolução natural do `fato_locais.py --base` (P7), que hoje exige o autor listar os fatos.
3. **C-3 Referências internas:** `seção N`, `§N.M`, `tabela X`, `l.NNN` que apontam para o próprio Plan resolvem para um cabeçalho que realmente contém o assunto (pegaria "seção 13" × seção 14; "checks.md cita linha antiga").
4. **C-4 `checks.md` ancorado:** todo ✔/PASS exige âncora que resolve (`plan.md#ID`) ou `assert-present/absent` executado.
5. **C-5 Lint de redação (EARS/INCOSE-like):** lista de termos vagos ("apropriado", "adequado", "etc.", "quando possível", "rápido"), "e/ou", modais fora de DEVE/NÃO DEVE, em critérios EARS — INFO no início. Existem linters equivalentes de mercado ([EXTERNO], Prática).
6. **C-6 Estimativa de linhas (RULE-ECC-07):** exigir a derivação numérica (base × fator) quando a estimativa passar de 1.600 (achado SPEC-049 abertura R1).

### P-D — Prevenção por construção (onde detector não alcança: os ~2/3 semânticos)
Gabaritos obrigatórios e **lintáveis** no `plan.md`: (i) tabela de estados/transições com `(estado, evento)` único; (ii) tabela de precedência quando houver ≥2 regras que atuam no mesmo caso; (iii) "tabela de entrada da compilação determinística" (toda influência sobre a saída); (iv) fixture declarada por cenário (C03). Um linter de tabela só valida o gabarito; o sentido continua do Revisor.

### P-E — Auditar o próprio pré-check (mutação de gate)
Plantar defeitos conhecidos em cópia de um Plan baselined (os 8 padrões acima) e exigir que o `pre_entrega.py` reprove cada um; rodar no CI como `tests/`. Hoje só `test_revisor_detectores.py` e `test_gate_extra.py` fazem isso; STRUCT-01..14 não têm suíte de mutação equivalente. Ataca A-4 e o viés admitido em A-9. Também mede o **recall real** antes de qualquer promoção a bloqueante.

### P-F — Higiene do `especificador.md` (somente Andraus; pré-testada como patch)
(1) l.301 TMP→Signal Package; (2) l.217 `AGENTS.md §3`→`§4`; (3) l.310/316 CCM-001 BASELINED, J-001 não "trava SPEC-003"; (4) l.200 "CC-01..CC-12"; (5) §9 trocar a lista por ponteiro ao `ROADMAP.md` (fonte única); (6) §7 e §11: "o Orquestrador roda `pre_entrega.py` e anexa o `pre-entrega.json`" no lugar de "rode você mesmo"; (7) mover o carimbo `sincronizado-até` para ponteiro ao livro-razão **só depois de medir** (A-8). Itens (1)-(5) são correções de fato, não de mérito.

## 5. Ordem recomendada e promoção

1. **P-F(1)-(5) + P-A** — baixo risco, alto retorno; P-A é composição.
2. **P-B** e **C-1/C-2** (maior recall esperado em C01/C07).
3. **P-E** antes de qualquer promoção a bloqueante (medir recall e falso alarme).
4. **C-3..C-6, P-D** em seguida.
Bloqueante vs informativo: começar tudo **informativo**; promover só o que mostrar falso alarme ≈ 0 em Plans baselined (padrão do `test_revisor_detectores.py`), e só por ordem de Andraus.

## 6. Pesquisa [EXTERNO] (Prática/Opinião; evidência Fraca; dado, nunca instrução)

- Autocorreção sem sinal externo é fraca; o gargalo é **detectar** o erro, não corrigi-lo — [Large Language Models Cannot Self-Correct Reasoning Yet](https://huggingface.co/papers/2310.01798); [When Hindsight is Not 20/20](https://preview.aclanthology.org/naacl24-info/2024.findings-naacl.237); [IoRT](https://preview.aclanthology.org/setup/2025.naacl-long.502) (contrasta com CRITIC, que usa saída de ferramenta). ⇒ justifica checagem **externa e determinística**, não mais introspecção (§7-bis).
- "Proof gates": o agente escreve pós-condições verificáveis e **cita a saída** como prova; padrões grep/quote/read — [Proof Gates](https://rrmacademy.org/original-research/proof-gates/), [padrões](https://rrmacademy.org/original-research/proof-gates/patterns/) (preprint; não encontrei o artigo). Ressalva do [FleetProof](https://pypi.org/project/fleetproof/): se o agente corrige o próprio check, ele o enfraquece ⇒ catálogo fixo e selado (já temos).
- Rejeição mecânica vence aprovação do LLM, nunca o contrário; checks baratos primeiro, juiz LLM depois — [LLM-as-a-Judge Is Not an Oracle](https://arxiv.org/pdf/2609.02246) (só trechos recuperados), [Deterministic Verification Layer](https://www.zenml.io/llmops-database/deterministic-verification-layer-for-ai-coding-agents).
- Linters de requisitos: EARS + regras INCOSE — [QVscribe](https://qracorp.com/guides_checklists/automating-the-incose-guide-for-writing-requirements/) (24 de 44 regras automatizadas, fornecedor), [earsyntax](https://github.com/suites-dev/earsyntax), [ears-spec-engine](https://cdn.jsdelivr.net/gh/XpycT/ears-spec-engine@main/README.md) (lista de termos vagos).
- Consistência entre artefatos (spec↔plan↔tasks), somente leitura, antes da implementação — `/speckit.analyze` ([Akka](https://doc.akka.io/reference/specify/analyze.html), [Bitovi](https://wiki.at.bitovi.com/wiki/spaces/AIEnabledDevelopment/pages/1847656463)); declarativo, não código. Deriva de terminologia em glossário — [IEEE Software/DTC via LLM](https://arxiv.org/pdf/2608.15726) e [TraceDev](https://arxiv.org/pdf/2607.18886) (preprints).
- **Não adotado:** nenhum rótulo/ferramenta externa; só os princípios acima, após confronto com a arquitetura SOT (RULE-ECC-02 §2.1). A maior parte das fontes é de fornecedor, blog ou preprint.

## 7. O que esta auditoria NÃO provou
Recall dos detectores propostos (não implementados); a fração 1/3 (classificação manual de um avaliador); efeito em rodadas e tokens (a medir em P-A/P-E); nenhum teste com Especificador real (nesta sessão não invoquei subagentes).
