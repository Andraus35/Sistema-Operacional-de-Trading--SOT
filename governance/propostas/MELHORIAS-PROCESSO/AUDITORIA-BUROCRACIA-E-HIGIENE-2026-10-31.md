# Auditoria — burocracia excessiva (método, ferramentas, agentes) e higiene de arquivos

> **Não normativo. PROPOSTA/RELATÓRIO** (AGENTS.md §12 passo 5). Nada aqui foi aplicado nem decide nada (CONS-01). Pedido de Andraus (chat, 2026-10-31). Base: ramo `ccr-599f6762-60qbvg`, histórico de 2026-10-16 a 2026-10-31 (276 commits, 43 merges). **Complementa** `AUDITORIA-HIGIENE-E-ECONOMICIDADE-2026-10-31.md` (custo de leitura H1–H8, mecanismos M1–M8) e não repete seus itens; remete a eles por ID.
>
> **Regra de equilíbrio dos 4Es (Andraus, 2026-10-31):** Conformidade > Eficácia > Efetividade > Eficiência > Economicidade. Toda alternativa abaixo preserva a prova (git, hash, gate bloqueante) e troca *trabalho humano/agêntico repetido* por *derivação determinística*. Onde há risco de Eficácia, está dito.
> **Convenção:** "medido" = contado por mim neste repositório; "inferido" = leitura do desenho; "não verifiquei" = lacuna declarada no §4.

---

## 1. Diagnóstico em três números

| Medida | Valor | Fonte |
|---|---|---|
| Código de produto (agentes de trading) | **0 linhas** (fase spec-first) | AGENTS.md §1 |
| Código do aparato de governança | **7.588 linhas** em `scripts/` (42 arquivos) + ~272 KB de testes + 53 mecanismos registrados (42 ativos) | `wc`, `MECANISMOS.json` |
| Documentos de governança/estado | 148 atas DHR, 109 cópias de HANDOFF, 38 pareceres, 113 arquivos em `propostas/` | `ls` |
| Rodadas de revisão no ledger | **35 rodadas, 0 Críticas, 39 Médias, 138 Menores** | `LEDGER-ACHADOS.md` |
| Custo de **uma abertura** de Spec (SPEC-049, sem Plan) | **906.237 tokens** em 6 chamadas (Esp. 250k+133k+110k; Rev. 172k+135k+106k) | `TELEMETRIA-ONDA0.md` |
| Specs com Plan vs. slots indicativos | 13 Plans (17.095 linhas) de ~45 slots (SPEC-002…045) | `specs/features`, ROADMAP |

Leitura: o método **funciona** (nenhuma Crítica chega ao fim; Médias caem rodada a rodada), mas o custo por unidade de Spec é alto e o aparato cresceu em volume comparável ao produto especificado. O gargalo não é falta de controle: é **controle repetido pelo mesmo fato em vários lugares, por agentes caros, mais um ritual manual de fechamento para cada mudança**.

---

## 2. FRENTE A — Burocracia, por ordem de criticidade (celeridade + 4Es)

Escala: **C1** trava o fluxo todo · **C2** custo recorrente grande · **C3** custo recorrente moderado · **C4** ruído/baixo ganho.

### A1 — C1 · O laço Especificador↔Revisor não tem critério de parada por valor
- **Evidência (medida):** SPEC-007 Plan = 6 rodadas, 22 Médias, 55 Menores, Plan com 3.851 linhas. SPEC-049 só na *abertura* = 3 rodadas (1 Média, 11 Menores). Nas 35 rodadas, **0 Críticas**; categorias dominantes C07 citação/âncora (34), C01 contradição interna (21–24), C02 vocabulário (20–21) — todas **verificáveis por script**. O relatório de 24/10 já nomeia a causa-raiz: o mesmo fato escrito em 5–7 lugares; "quase toda Média da rodada N+1 nasceu da correção da rodada N".
- **Por que é burocracia:** o Revisor (≈105–172 mil tokens/rodada) e o Especificador Opus (≈110–250 mil) gastam rodadas caras em conferência de coerência que um índice gerado resolveria; Menores seguem abrindo rodada.
- **Mitigação alternativa (sem afrouxar a prova):**
  1. **Fonte única por fato:** o Plan declara cada fato (limiar, ID, contagem, versão) uma vez em bloco estruturado; as demais ocorrências são *geradas* ou checadas por script (P3/P7 das retrospectivas já apontam isso). Remove a cascata na origem.
  2. **Regra de parada:** parecer só com Menores ⇒ não abre rodada; vão como condição de homologação ou ficha M (o AGENTS §12 passo 0 já permite parte; falta formalizar "CONFORME condicional ⇒ homologar").
  3. **Delta por hash obrigatório da R2 em diante** (hoje: 3/35 rodadas com `SHA256-ALVO`; 13/35 por delta). Tornar o hash campo do pedido, não cortesia.
  4. **Teto de rodadas por perfil** (LOW 2 · MEDIUM 3 · HIGH 4 · CRITICAL 5), com escalonamento a Andraus em vez de nova rodada.
- **Quem decide:** Andraus (muda `revisor.md`/AGENTS §12). **Risco 4Es:** baixo em Eficácia se Críticas/Médias continuarem bloqueando; ganho principal em Eficiência/Economicidade.

### A2 — C1 · Ritual de fechamento manual duplica o que o git já prova
- **Evidência (medida):** a cada entrega o Orquestrador reescreve `HANDOFF.md` e copia o anterior para `docs/handoffs/` (**109 arquivos, 1,4 MB**, 111 rastreados); atualiza `rpsa-ledger.json` (37 toques), `CATALOGO-OFICIAL.md` (23), `MECANISMOS.json` (22), `GATE-MANIFEST.sha256` (18), `LEDGER-ACHADOS.md` (22) e o mapa (**98 dos 233 commits** sem merge tocam `MAPA-PROJETO.md` + `mapa-projeto.json` de 1,36 MB). O commit de homologação da abertura da SPEC-049 alterou **48 arquivos / +3.206 linhas**, 23 deles `.txt` de fontes.
- **Por que é burocracia:** INV-07 ("nada é deletado") é cumprido **literalmente por arquivo**, mas o git já é um livro-razão monotônico, assinado por hash. O carimbo RPSA ("sincronizado-até") reimplementa à mão `git diff <hash>`. O handoff reescrito inteiro reconta o que `git log` diz.
- **Mitigação alternativa:**
  1. **HANDOFF = só delta + ponteiros** (≤40 linhas); o "estado" (PRs mesclados, base_commit, contagens) é gerado por script (`check_handoff` já lê o frontmatter). Preservação INV-07 via *tag git por handoff* em vez de cópia de arquivo.
  2. **RPSA derivado do git:** o carimbo vira o hash do último commit que tocou o conjunto monitorado; `check_rpsa` compara hashes e o `rpsa-auto.yml` deixa de existir como etapa humana.
  3. **`mapa-projeto.json` fora da árvore** (artefato de CI) — ver B1.
  4. **Ata curta em tabela única** para mudança operacional (ver A7).
- **Quem decide:** Andraus (INV-07, PCC-001, RPSA). **Risco 4Es:** Conformidade preservada se a tag/hash substituir a cópia com verificação (`check_handoff` ganha teste "tag existe"). Nenhum conteúdo normativo perdido.

### A3 — C1 · O gargalo real é a fila de decisões de Andraus
- **Evidência (medida/lida):** HANDOFF §10 lista pendências só dele: P7–P9 (retrospectivas), H1–H8 e M1–M8 (auditoria de ontem), check de dimensionamento, errata SPEC-007, erratum F2 SPEC-020, CATALOGO/RMR-001 (BL-017), CONFLICT-MAP, 9 decisões abertas do ROADMAP, destino do Auditor Externo, D-PCC-3/4/5; `backlog_triggers` com BL-003/BL-011 ATIVADOS e 4 "disparados sem registro". AGENTS §10 reserva a ele homologação, mudanças em `AGENTS.md`, `.claude/agents/*`, `governance/` normativo, `canon/`, ROADMAP, atomic-spec.
- **Por que é burocracia:** a produção de propostas (por agentes) é muito mais rápida que a decisão; propostas viram dívida e cada gate reimprime o mesmo aviso.
- **Mitigação alternativa:**
  1. **Decisão em lote com formulário binário**: uma página de decisão por sessão (aprovar/recusar/adiar por item, recomendação do Orquestrador marcada) — não uma ata por item.
  2. **Classes de decisão:** *operacional* (script/detector informativo/higiene não normativa) = Orquestrador decide e informa (AGENTS §10 já abre essa porta; estender a detectores e higiene); *normativa* = Andraus.
  3. **Validade da proposta:** proposta sem decisão em N dias vai para o fim da fila com "recomendação padrão" explícita, nunca silêncio.
- **Quem decide:** Andraus. **Risco:** controle humano é escolha de desenho; a mitigação reduz *quantidade* de pedidos, não retira a autoridade.

### A4 — C2 · Dois ciclos completos de revisão por Spec (abertura + Plan) sem proporcionalidade
- **Evidência (medida):** cada Spec passa por Dossiê (`research.md`) + `ABERTURA.md` + `sources/` (SPEC-049: 23 arquivos) → revisão (3 rodadas) → homologação de abertura → *depois* Plan + `checks.md` → revisão (5–6 rodadas) → homologação. SPEC-002/046 ainda têm `DOSSIE-PESQUISA.md` **e** `PROPOSTA-ABERTURA.md` **e** `research.md`.
- **Mitigação alternativa:** proporcionalidade pelo perfil já pinado (AGENTS §4): LOW/MEDIUM = abertura e Plan num só ciclo de revisão, Dossiê enxuto; HIGH/CRITICAL mantêm os dois. `sources/` fica como evidência arquivada, **fora da conferência do Revisor** (que audita o *processo* do Dossiê, não a veracidade das páginas — já é a regra). Padronizar nomes (B8).
- **Quem decide:** Andraus (atomic-spec §15, ROADMAP §23). **Risco 4Es:** Eficácia preservada onde há complexidade; economia concentrada em Specs pequenas.

### A5 — C2 · Leitura obrigatória inflada e duplicada (≈47–49 mil tokens por chamada)
- **Evidência:** ver H1–H4 da auditoria anterior. **Acréscimos meus (medidos):** `ROADMAP.md` tem células de tabela com até **9.894 caracteres** ("Estado atual do ciclo" é um *log de homologações*, não um roteiro); `AGENTS.md` §7 (5,9 KB) **repete** o estado de decisões que o próprio texto manda ler no ROADMAP ("em divergência, o ROADMAP prevalece") e depois mantém um detector (`check_doc_sync`) para policiar a duplicação; há 6 marcas "texto anterior preservado" no AGENTS e 12 no ROADMAP.
- **Mitigação alternativa:** **remover a duplicação em vez de policiá-la** — §7 do AGENTS vira ponteiro; histórico de células vai para `docs/_legacy/` (INV-07 por arquivo+hash, ou tag git) e o ROADMAP mantém só estado atual por linha. O detector `check_doc_sync` perde a classe (a)/(b) inteira.
- **Quem decide:** Andraus (AGENTS/ROADMAP). **Risco:** exige check de equivalência (hash por seção) — já proposto em H1.

### A6 — C2 · Camada de mecanismos pesa mais do que protege
- **Evidência (medida):** 53 mecanismos; **12 hooks** (9 em Stop/SubagentStop a cada fim de turno); **15 detectores**, a maioria *informativa* (não bloqueia) e re-executada em hook **e** em CI (`continue-on-error` em 7 passos); 2 inertes em nuvem (`mcp.revisor-gate`, `hook.revisor-guard`) mas o Revisor é instruído a usá-los; Auditor Externo PAUSADO (workflow de 326 linhas + `route_aex.py` + testes + AGENTS §9 + 18 atas DHR-AUDITOR-EXTERNO); selo `GATE-MANIFEST.sha256` regravado 18× embora `.github/CODEOWNERS` já exista; `andraus-ask-*` = 3 scripts + `merge_ready.py` para um comportamento (perguntar a Andraus). Avisos permanentes (HO-03 hoje; doc-sync WARN de `SPEC-007/plan.md:2650` em todo SessionStart) → fadiga de alerta.
- **Mitigação alternativa:**
  1. **Três camadas, não doze hooks:** (i) *bloqueantes* (≤6: validate_spec, schemas, gate_manifest, refs ERRO, invariantes, testes) em CI; (ii) *um* `run_gates.py` informativo, chamado **uma vez** antes de PR/merge (não a cada turno); (iii) o resto arquivado.
  2. **Cláusula de caducidade por detector:** sem achado novo em N execuções, vai para `docs/_legacy/` com motivo (INV-07 por tag).
  3. **Aposentar de fato** o Auditor Externo (decisão D-PCC-3) e os dois inertes, ou reativá-los; o "meio-termo" custa em toda sessão (AGENTS §9 é lido por todos).
  4. Silenciar o WARN repetido **mostrando só quando o conjunto de achados mudar** (mantém visibilidade — mesma ressalva da M6 anterior).
- **Quem decide:** Andraus (MECANISMOS vigente, COE-14). **Risco:** Eficácia só se a camada (i) for mal escolhida — calibrar com os testes de calibração que já existem.

### A7 — C3 · Ata completa para tudo
- **Evidência (medida):** 148 DHR (mediana 49 linhas; mínimas de 24), muitas para mudança operacional (ex.: detector que casa ID inteiro, aviso "pronto para mesclar", lembretes datados no handoff, atas ASK/MERGE/CHECKS-INFO). 3 atas ainda dizem "PROPOSTA — vira vigente só com o merge" (COE-11).
- **Mitigação alternativa:** **registro único um arquivo único de log de decisões (a criar; nome a definir)** (1 linha por decisão operacional: ID, data, ordem de Andraus citada, arquivos, hash do commit); ata completa só para baseline, norma e fechamento de decisão aberta. Mantém a rastreabilidade (assinatura = decisão citada, AGENTS §10).
- **Quem decide:** Andraus. **Risco:** baixo, desde que a linha cite a ordem.

### A8 — C3 · Roteamento por classe (M/S1/S2/S3/O) e hook R-AC1…R-AC7
- **Evidência:** `roteador_modelos.py` 491 linhas + hook + testes + 7 atas DHR-ROTEAMENTO; revertido/reajustado várias vezes; "~8 chamadas de Revisor recusadas ou refeitas" (relatório de 24/10); telemetria de tokens com ~10 linhas e **sem teste de não-inferioridade registrado** (auditoria anterior §5).
- **Mitigação alternativa:** fixar `model:` no frontmatter de cada agente (Revisor=sonnet, Especificador=opus), manter só a regra "classe M = Orquestrador" (que é determinística), e **medir antes de reintroduzir roteamento dinâmico** (ledger 2-ter já mede tokens). Se a não-inferioridade for provada, voltar ao roteador com dado.
- **Quem decide:** Andraus (`.claude/agents/*`). **Risco:** Economicidade só melhora com medição; hoje decide-se por opinião.

### A9 — C3 · Checklist duplicado entre Especificador (autopré-check) e Revisor (8 passos)
- **Evidência (medida):** `especificador.md` 345 linhas (§7 + §7-bis A–D) e `revisor.md` 423 linhas (Passos 0–8, 4-bis, 4-ter, 5-bis) verificam os mesmos blocos (invariantes, constitution check, rastreabilidade, adversarial EUA-E18), e `validate_spec_sot.py` (553 linhas) + `revisor_gate.py` (490) + `revisor_detectores.py` + `gate_extra.py` + `check_invariants.py` já automatizam parte.
- **Mitigação alternativa:** **uma lista de verificação legível por máquina** (YAML/JSON) com cada item marcado D (determinístico — roda no gate), H (julgamento — fica com o Revisor); o Especificador roda os D antes de entregar; o Revisor só lê o relatório D e gasta tokens nos H. Os agentes passam a referenciar IDs de item em vez de reescrever prosa.
- **Quem decide:** Andraus. **Risco:** exige calibração (já existe infraestrutura de calibração nos Plans homologados).

### A10 — C4 · Ferramentas sem consumidor
- `eslint`/`prettier`/`tsconfig`/`pre-commit` não são invocados por `package.json`, CI ou hooks (COE-09 INFO); `harness-score` é `npx` opcional; `revisao-independente/` é um procedimento ad hoc da SPEC-006 (ramo `spec006-plan`, "já usada 2x"). Custo: ruído e manutenção de arquivos que o `check_coesao` precisa explicar. Detalhe em B5.

---

## 3. FRENTE B — Higiene de documentos e arquivos

Ordenada por ganho de clareza/risco de erro por unidade de esforço. **Nenhum item exige apagar** (INV-07): mover para `docs/_legacy/` ou gerar fora da árvore, com `check_refs` validando.

| # | Item | Evidência (medida) | Ação sugerida | Esforço/risco |
|---|---|---|---|---|
| B1 | **Artefatos gerados versionados** | `docs/mapa/mapa-projeto.json` 1,36 MB e `MAPA-PROJETO.md` 106 KB regenerados em **98 de 233 commits**; `docs/handoffs/` 1,4 MB de cópias | `.json` como artefato de CI (M8, verificar consumidores); handoffs por tag git (A2) | baixo; verificar `build_map`/`check_*` |
| B2 | **HANDOFF contraditório e fora de padrão** | §1 diz "Próximo: Andraus decide P-1..P-7" e depois "Homologação feita"; é um parágrafo único de ~4,7 KB com cronologia misturada; cabeçalho `base_commit: 3a1208b` × §9 `base_commit (2917341)`; WARN HO-03 ativo | reescrever em "Frente / Estado / Próximo passo" (≤40 linhas); gerar base_commit e lista de PRs por script | baixo; só Orquestrador |
| B3 | **Logs dentro de documento normativo** | ROADMAP: células de até 9.894 caracteres, 12 marcas de texto preservado; AGENTS: 6 marcas; `CATALOGO-OFICIAL.md` 96 KB | histórico → `docs/_legacy/` + tag; documento quente só com estado atual (A5/H1–H3) | exige ordem de Andraus |
| B4 | **Status que mente no nome** | 33 arquivos `_PROPOSTA` em `governance/` (17 já HOMOLOGADAS, H6); 3 atas "PROPOSTA — vira vigente só com o merge" (COE-11) | campo `Status:` na 1ª linha + índice; não renomear (referências por caminho) | baixo |
| B5 | **Raiz e config órfãs** | `.eslintrc.json`, `.prettierrc`, `tsconfig.json` sem JS/TS a processar (COE-09); `.pre-commit-config.yaml` = proposta não instalada; `package-lock.json` 214 B sem dependências; `.agents/.skill-lock.json` (1 skill local, 2026-09-09); `revisao-independente/` (ad hoc SPEC-006); `RETOMADA/GEH-001` é guia **genérico** citado por 31 arquivos mas fora do mapa de pastas do AGENTS §2 | decidir: instalar ou arquivar cada config; mover `revisao-independente/` para `docs/_legacy/`; incluir/relocar `RETOMADA/` em `canon/` ou `reference/` com o mover script reescrevendo referências | médio (referências); decidir caso a caso |
| B6 | **`docs/UPGRADES/` (340 KB)** | 1 arquivo o cita fora de mapa/handoffs; relatórios únicos de 2026-09-26 + `understand-anything-graph` (192 KB) + `claude-code-setup-audit` (104 KB) | mover para `docs/_legacy/UPGRADES/` | baixo |
| B7 | **Nomes de arquivo hostis** | `reference/camadas/CAMADA MEMÓRIA.MD`, `CAMADA EPISTÊMICA.MD`, `reference/externo/Uso de Logs por Agentes de IA.MD`, `CACHING SOT.MD` (espaços, acentos, `.MD` maiúsculo) | normalizar (`camada-memoria.md`) com mover-e-reescrever-referências; senão links/globs falham em shells e `.md` minúsculo em casos | médio (31 referências a `reference/camadas`) |
| B8 | **Artefatos de Spec com nomes inconsistentes** | SPEC-002/046: `DOSSIE-PESQUISA.md`+`PROPOSTA-ABERTURA.md`+`research.md`; SPEC-003: `research-Q-A9-regime.md`; SPEC-004+: `ABERTURA.md`+`research.md`; SPEC-001/019: só plan+checks | padrão único (`research.md`, `ABERTURA.md`, `plan.md`, `checks.md`) e um `INDEX.md` por Spec (gerado) | baixo; só prospectivo |
| B9 | **`governance/` plano e misto** | 213 itens na raiz de `governance/`: normativos (CONSTITUTION, RULES, CATALOGO) + 148 atas + 6 `AUDITORIA-*` + ADRs + propostas | subpastas `atas/`, `auditorias/` com script de mover + `check_refs` (39.382 arestas serão revalidadas); ou, no mínimo, índice por tipo/estado | médio-alto; só com script |
| B10 | **Detectores com falso positivo** | `check_refs`: 6 WARN, 323 INFO; falsos: o README do proxy do ambiente, `wc -l specs/...plan.md` lido como caminho; placeholders `RULE-CKG-0NN`/`RULE-KFH-0NN` | ignorar placeholders `0NN` e blocos de código; senão o WARN vira ruído | baixo |
| B11 | **Citação de versão vencida em baseline** | `SPEC-007/plan.md:2650` cita versão antiga do `WORKFLOW.md` (a vigente é outra) | só por erratum homologado (baseline) — juntar à errata SPEC-007 já pendente | baixo, depende de Andraus |
| B12 | **Geração-1 do produto** | `specs/*.spec.md` (5), `rag/` (5), `schemas/` (11), `.clinerules/` (4): "nenhum implementado", CI valida schemas mas não há consumidor | marcar `Status: GEN-1` no topo e dizer qual SPEC-0xx os supera; **não verifiquei** divergência de conteúdo (§4) | baixo |
| B13 | **Pareceres e propostas por rodada** | `governance/propostas/` 113 arquivos (1,4 MB), 38 pareceres, incluindo `linha-spec006-plan/parecer-revisor-rodada5..9` sem achados extraídos | `propostas/<X>/arquivo-rodadas/` após homologação; ledger já lê o caminho se o script aceitar subpasta | baixo |

---

## 4. O que NÃO verifiquei

- **Tokens reais**: usei apenas os valores do `TELEMETRIA-ONDA0.md` (subagent_tokens) e bytes÷4 da auditoria anterior; economias estimadas são ordem de grandeza.
- **Consumidores** de `mapa-projeto.json`, `.agents/`, `schemas/`, `rag/`, `.clinerules/` (B1, B5, B12): não rodei busca de uso em scripts/CI; confirmar antes de mover. (Uma busca textual por `.agents` casa também `.claude/agents` — não é evidência de uso.)
- **Efeito causal** das mitigações A1/A4: o ledger mostra correlação (cascata de Médias) mas não há experimento controlado; testar numa próxima Spec (por ex. SPEC-049 Plan) antes de institucionalizar.
- **Conteúdo** interno de `reference/` e `docs/UPGRADES/` além do tamanho e dos nomes.
- Não executei a suíte (`unittest discover`) nem `build_map --check`; usei os detectores `check_refs`, `check_doc_sync`, `check_coesao`, `check_handoff` (somente leitura).

## 5. Ordem de ataque proposta (para Andraus escolher; nada foi aplicado)

1. **Sem ordem normativa (Orquestrador, risco ~zero):** B2 (reescrever HANDOFF), B6, B10, B13, B8 prospectivo, status em B4.
2. **Experimento medido:** A1 itens 2–4 na SPEC-049 Plan (regra de parada + hash obrigatório + teto de rodadas); registrar tokens/rodada no ledger 2-ter.
3. **Com ordem de Andraus, ganho alto:** A2 (HANDOFF por delta + tag, RPSA derivado do git, mapa fora da árvore), A5/H1–H3 (tirar logs dos arquivos quentes), A3 (decisão em lote + classes).
4. **Com ordem de Andraus, ganho médio:** A6 (3 camadas de mecanismos + caducidade), A7 (DECISOES-LOG), A8 (modelo fixo + medir), A4 (proporcionalidade por perfil), A9 (checklist único D/H).
5. **Fechar** com retrospectiva (LOOP-001 passo 5), medindo A1: rodadas e tokens por Spec antes/depois.

## 6. Correção posterior (2026-10-31) — configs da raiz NÃO são órfãs por descuido
Os itens **A10 / B5** trataram `.eslintrc.json`, `.prettierrc`, `tsconfig.json` e `.pre-commit-config.yaml` como configurações sem consumidor a arquivar. **Isso estava incompleto:** `governance/MECANISMOS.json` registra `cfg.eslintrc` e `cfg.prettierrc` como estado `legado` **"MANTIDO de propósito: marcador de sensor (SNS-02/SNS-04) do harness-score; nenhuma ferramenta de lint/format roda; arquivar baixaria o score de maturidade"** (decisão registrada na `DHR-COESAO-002`), e `scripts/check_coesao.py` as referencia. `cfg.pre-commit` está registrado como `proposta` (nunca instalado). Nenhuma foi movida. O que resta de real aqui é só o **trade-off de Andraus**: manter por causa da nota do `harness-score` (custo: 4 arquivos de raiz sem ferramenta) ou arquivar e aceitar a queda do score. Lição: ler o registro de mecanismos **antes** de classificar arquivo como órfão.

### 6.1 Correção do item B4 (33 `_PROPOSTA`)
Conferidos os 33 arquivos: **a maioria já declara o status por dentro** ("HOMOLOGADA — FATO NORMATIVO", com a ata citada); só o **nome** diz `_PROPOSTA`, e renomear quebraria referências por caminho. Os realmente desatualizados eram **3**, corrigidos com texto anterior preservado (`DHR-HIGIENE-002`): `EUA-E20` e `EUA-E23` (atas `DHR-EUA-E20/E23` existem e o ROADMAP/AGENTS os tratam como vigentes) e `PCC-001` (Fases 1–2 e anexo autorizados). **Correção desta correção (releitura dos títulos):** `EMENDA-SPEC001-001` está **HOMOLOGADA** (banner no título) e `REAUDITORIA-SPEC002-001`, `MANIFESTO-DE-ESCOPO` e `PROTOCOLO-AUDITOR-EXTERNO` já dizem "PROPOSTA — NÃO HOMOLOGADO" — nada a mudar nesses quatro. Só o `ERRATUM-SPEC019-001` tem status ambíguo e recebeu nota neutra "status não confirmado" (`DHR-HIGIENE-002`); depende de Andraus confirmar.
