# PROPOSTA — Melhoria da Pesquisa Web do Especificador: itens M1..M8, priorização e parecer

**[PROPOSTA — NÃO NORMATIVO / NÃO HOMOLOGADO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-06 |
| Base | `DOSSIE-MELHORIA-PESQUISA.md` (+ `sources/`) · `PROPOSTA-AUDITOR-HIBRIDO.md` (Opção C, reuso) · scripts vigentes |
| Decisão | **`[DECISÃO NECESSÁRIA]`** — eu proponho; Andraus decide via Orquestrador. Nada vira baseline; sem código escrito. |
| Parecer global | **VIÁVEL COM CONDIÇÕES** — todos os itens são Detectores (ENF-03), não dão poder novo a LLM, não dão web ao Revisor/auditor; a viabilidade técnica de execução é INDETERMINADA (sem Bash nesta sessão). |

> **Regra de leitura:** cada item declara problema (com evidência desta/de outras sessões), solução, evidência com ID, 4Es, arquivo-alvo, se exige homologação de Andraus, e custo. Toda RULE nova citada é `[PROPOSTA]` até registro físico (RULE-HG-02). Nenhuma decisão aberta é fechada (CONS-01).

---

## M1 — Verificador mecânico de captura (toda « » existe em sources/)
- **Problema (evidência):** 3 reprovações do Revisor nesta sessão por citação entre « » sem captura verbatim; correções pós-NÃO CONFORME em `DOSSIE-PESQUISA-COOPERACAO.md` §8 (C-01/C-02). Falha F-2/F-3.
- **Solução:** script Detector (molde `check_refs.py`) que, sobre o Dossiê/`research.md`, extrai toda citação entre « »/aspas e **reprova se o trecho não existe literalmente** em algum `sources/<ID>.txt` da mesma Spec; para elipse, exige que **ambos os lados** existam como substrings literais. Roda **antes** da entrega ao Revisor (Autopré-check) e como passo CI informativo. Puramente determinístico, sem web.
- **Evidência `[EXTERNO]`:** SRC-CITE-01 «the density of citations performs a rigour the links don't always have.» (por que verificar e não confiar na densidade); SRC-HITL-01 «Use deterministic logic ... as the authoritative signal ... that a deterministic layer re-checks.»
- **4Es:** Eficácia alta (fecha a falha mais recorrente por construção); Efetividade alta; Eficiência alta; Economicidade alta (barato; evita ciclo de revisão perdido).
- **Arquivo-alvo:** novo `scripts/check_sources_verbatim.py` (não coberto por manifesto); item no Autopré-check de `especificador.md` §7; menção de método em `atomic-spec.md` §15.
- **Homologação de Andraus:** SIM para virar item do Autopré-check/método e para virar gate; como Detector informativo em `scripts/`, menor cerimônia, mas a edição de `especificador.md`/`atomic-spec.md` exige emenda homologada.
- **Custo:** baixo.

## M2 — Regra "sumário de busca ≠ página" explícita e verificável
- **Problema (evidência):** F-1 — `DOSSIE-PESQUISA-COOPERACAO.md` §2/§8 registra material que veio de **resultado de busca** sendo corrigido depois. O WebSearch/WebFetch devolvem síntese, não a página literal.
- **Solução:** regra de processo (já praticada, torná-la verificável): conteúdo obtido de WebSearch ou de WebFetch mediado **nunca** vai entre aspas; só o que foi colado literalmente numa captura `sources/<ID>.txt` (via WebFetch pedindo o trecho literal, conferido pelo autor) pode ser citado. O que vier de sumário leva `[EXTERNO, não-capturado-verbatim]` e **não** sustenta alegação carregada sozinho. M1 é o detector que o impõe (aspas sem captura = reprova).
- **Evidência `[EXTERNO]`:** SRC-CITE-01 (deep research «hallucinated them at higher rates.»).
- **4Es:** Eficácia alta; custo quase zero (é disciplina + M1).
- **Arquivo-alvo:** `atomic-spec.md` §15 (texto de método) + Autopré-check.
- **Homologação:** SIM (edita método baseline).
- **Custo:** baixo (acoplado a M1).

## M3 — Graduação de evidência por fonte (nível + conflito de interesse + primário/secundário)
- **Problema (evidência):** F-4 — níveis heterogêneos em coluna de texto livre (`DOSSIE-PESQUISA-AUDITOR-HIBRIDO.md` §2). Fontes fracas podem sustentar conclusões sem salto aos olhos.
- **Solução:** padronizar a tabela de fontes do §15 com campos: `tipo` (já existe), `nível` {Forte/Média/Fraca}, `primário/secundário`, `conflito de interesse` (ex.: doc de fornecedor que vende o produto), `data de acesso`. Invariante de processo: **nenhuma alegação carregada repousa só em fonte Fraca**. Checável por enum + marcação.
- **Evidência `[EXTERNO]`:** SRC-JUDGE-01 «when we added automatically generated fake references to Assistant B's answer, the judge model considered Assistant B's quality to be superior.» (autoridade/referência enviesa); SRC-CITE-01 (secundárias inflam).
- **4Es:** Eficácia média-alta (qualidade epistêmica); Economicidade alta.
- **Arquivo-alvo:** `atomic-spec.md` §15 (tabela) + Autopré-check.
- **Homologação:** SIM.
- **Custo:** baixo.

## M4 — Triangulação mínima (≥2 fontes independentes por alegação carregada)
- **Problema (evidência):** F-5 — alegações sobre uma só fonte; viés de seleção (Q7 em `DOSSIE-PESQUISA-COOPERACAO.md` §4 é `[INFERÊNCIA]` sem fonte dedicada — honesto, mas ilustra a ausência de triangulação).
- **Solução:** regra: toda alegação **carregada** (adotar/adaptar/rejeitar/adiar) exige ≥2 fontes independentes **ou** marcação explícita `[INFERÊNCIA]`/INDETERMINADO quando só há uma. Pergunta adversarial obrigatória por alegação carregada (análogo ao §7-bis Bloco A): "qual fonte NEGA ou limita esta alegação?". Detector confere a contagem de IDs por alegação marcada.
- **Evidência `[EXTERNO]`:** SRC-JUDGE-01 «The tendency to give stronger preference to the majority's beliefs regardless of whether they are correct or not.» (bandwagon — por que não bastar uma fonte confirmatória).
- **4Es:** Eficácia alta (reduz viés de confirmação); Eficiência média (mais busca); Economicidade boa.
- **Arquivo-alvo:** `especificador.md` §7-bis (estender ao Dossiê) + `atomic-spec.md` §15.
- **Homologação:** SIM.
- **Custo:** médio (exige mais fontes; reusa capturas quando possível).

## M5 — Seção "Registro de buscas" (queries + descartados + motivo)
- **Problema (evidência):** F-5 e reprodutibilidade — não há registro do que foi buscado e **descartado**; o viés de seleção fica invisível.
- **Solução:** seção obrigatória no Dossiê: termos de busca exatos, data, fontes examinadas e **descartadas com motivo** (fraca/irrelevante/não resolve/duplicada). Torna a decisão reconstruível (P13) e expõe a seleção.
- **Evidência `[EXTERNO]`:** SRC-REPRO-01 «sampling determinism is not the same thing as system determinism.» (não se promete repetir a busca bit-a-bit; registra-se o contexto — honestidade RULE-MET-01).
- **4Es:** Eficácia média (auditabilidade/anti-viés); Economicidade alta (quase zero custo).
- **Arquivo-alvo:** `atomic-spec.md` §15 (conteúdo mínimo do Dossiê).
- **Homologação:** SIM.
- **Custo:** baixo.

## M6 — Coletor de metadados de repositório por API pública (fecha o "NÃO CONFIRMADA" da ECC-06)
- **Problema (evidência):** F-7 — `cooperacao/sources/REPO-guardrails-01.txt` "NÃO CONFIRMADO ... 2 dos 6 critérios não foram verificaveis". Mas `specs/features/SPEC-006/sources/REPO-mem0.txt` **resolveu** via API: "proxy: campo pushed_at da API pública = 2026-10-05...". A inconsistência entre sessões prova que o gap é de **método, não de régua**.
- **Solução:** método padronizado (e, opcionalmente, script auxiliar) para coletar da **API oficial pública** do GitHub/GitLab os campos objetivos — `stargazers_count`, `license.spdx_id`, `pushed_at` (proxy de último commit), `archived` — e preencher a captura `REPO-*.txt` registrando o **campo-fonte** de cada número. Marcar INDETERMINADO **apenas** o genuinamente privado (estado de Dependabot privado), nunca o que a API expõe. Converte falso-negativo técnico em veredito real. **ENF-03:** a rede é do Especificador (que já tem WebFetch), não do Revisor/auditor; `check_repo_research.py` continua conferindo a régua sobre os números capturados.
- **Evidência `[FONTE]`:** SPEC-006 REPO-* (método provado); `scripts/check_repo_research.py` (gate que consome a captura).
- **4Es:** Eficácia alta (resolve o problema nomeado por Andraus); Efetividade alta; Eficiência média; Economicidade alta (poucos campos, API pública).
- **Arquivo-alvo:** `atomic-spec.md` §15 (método ECC-06) + Autopré-check; opcional `scripts/collect_repo_meta.py` (auxiliar do Especificador, não gate).
- **Homologação:** SIM para fixar como método obrigatório; o padrão já é compatível com a régua vigente.
- **Custo:** baixo-médio (rate-limit da API a tratar; URL rot → INDETERMINADO honesto).

## M7 — Verificador de fontes ao vivo tri-estado (reuso da Opção C)
- **Problema (evidência):** F-1/F-2 — a veracidade da página citada é "não verificável sem web" pelo Revisor; citação pode ser fabricada (SRC-CITE-01).
- **Solução:** reuso direto da Opção C de `PROPOSTA-AUDITOR-HIBRIDO.md`: script determinístico (não-LLM, sem segredos) que busca as URLs do `sources/` do Especificador e confere a citação verbatim, com resultado **tri-estado** por fonte — `VERIFICADO` / `DIVERGENTE` (página acessível mas citação não casa → achado candidato a Crítica) / `INACESSÍVEL-TÉCNICO` (bloqueio/JS/rot/paywall → **não reprova**, registra motivo). Saída versionada: URL + data + hash do conteúdo baixado + trecho que casou/não casou + tri-estado. Passo informativo (não gate por conta própria — ENF-03; quem bloqueia é Andraus).
- **Evidência `[EXTERNO]`:** SRC-HITL-01 «Risk classification itself can't rely on an LLM exposed to the same untrusted content as the request being evaluated, because adversarial content could influence the classifier into marking the request as low-risk.» (verificação por código, não por LLM); SRC-CITE-01 (3–13%/5–18% de URLs problemáticas — indicativo).
- **Transferência de confiança (honestidade):** o Revisor passa a confiar na saída do fetcher (artefato inspecionável por string), não na web — risco residual declarado: o hash prova o que o fetcher baixou, não que a origem não foi adulterada nem que um humano veria o mesmo (reuso de `PROPOSTA-AUDITOR-HIBRIDO.md` §OBS-03).
- **4Es:** Eficácia alta (mata citação fabricada/sumário-como-página); Efetividade alta; Eficiência média; Economicidade média (fetch, rot, manutenção).
- **Arquivo-alvo:** `scripts/check_sources_live.py` (reuso Opção C) + método em `atomic-spec.md` §15.
- **Homologação:** SIM (ativa rede nova como passo de processo; decisão de Andraus).
- **Custo:** médio (o mais caro da lista; por isso priorizado depois dos baratos).

## M8 — Checador de datas/validade do Dossiê (ECC-VAL-001)
- **Problema (evidência):** F-8 — não se verifica que toda captura tem data de acesso dentro da janela ECC-VAL-001 (DHR-DEC-003: HIGH/CRITICAL 90 dias).
- **Solução:** Detector que confere presença de "Data de acesso: AAAA-MM-DD" em cada `sources/<ID>.txt` e que a diferença para a data da entrega está dentro da janela da complexidade declarada. Reprova (informativo) captura vencida.
- **Evidência `[FONTE]`:** ECC-VAL-001 (DHR-DEC-003, já FECHADA — usada só como parâmetro).
- **4Es:** Eficácia média; Economicidade alta (trivial).
- **Arquivo-alvo:** `scripts/` (pode acoplar a M1) + Autopré-check.
- **Homologação:** SIM para item do Autopré-check.
- **Custo:** baixo.

---

## Priorização (maior Eficácia / menor custo primeiro)

| Ordem | Item | Fecha falha | Custo | Depende de Andraus |
|---|---|---|---|---|
| 1 | **M1** Verificador de captura verbatim | F-2, F-3 | baixo | edição de método/Autopré-check: sim |
| 2 | **M2** Sumário≠página (acoplado a M1) | F-1 | baixo | sim (método) |
| 3 | **M6** Metadados de repo por API | F-7 | baixo-médio | sim (método) |
| 4 | **M5** Registro de buscas | F-5 (seleção) | ~zero | sim (método) |
| 5 | **M3** Graduação de evidência | F-4 | baixo | sim (método) |
| 6 | **M4** Triangulação ≥2 fontes | F-5 | médio | sim (método/§7-bis) |
| 7 | **M8** Datas/validade | F-8 | baixo | sim (Autopré-check) |
| 8 | **M7** Verificador ao vivo tri-estado | F-1, F-2 | médio | sim (ativa rede) |

**Lógica da ordem:** M1+M2 primeiro porque fecham, com custo mínimo e sem rede, as reprovações observadas nesta sessão. M6 em seguida porque resolve o problema que Andraus nomeou explicitamente, reusando método já provado. M5/M3/M4 elevam qualidade epistêmica a custo baixo. M8 trivial. M7 por último: maior Eficácia contra fabricação, mas é o único que abre rede e carrega transferência de confiança — entra como passo informativo, não gate, e só se Andraus quiser cobrir a veracidade ao vivo.

## Opções de abrangência (Andraus escolhe)
- **Opção mínima:** M1+M2+M8 (puramente verbatim/forma; sem rede nova). Captura a correção das reprovações recorrentes ao menor custo.
- **Opção equilibrada (recomendada):** mínima + M6 + M5 + M3. Fecha F-7 e eleva qualidade epistêmica sem o custo/risco do fetcher ao vivo.
- **Opção completa:** tudo + M4 + M7. Cobre também veracidade ao vivo e triangulação; maior custo e única com rede nova.

## Parecer
**VIÁVEL COM CONDIÇÕES.** Condições inegociáveis:
1. Todos os itens são **Detectores** (ENF-03): nenhum decide, homologa ou vira gate sem decisão de Andraus; nenhum dá web ao Revisor ou ao Auditor Externo.
2. Web permanece **DADO** (DHR-PROV-WEB-001 §2.1); nenhum coletor executa/segue instruções de página; nenhum dado sensível vai em query/URL; nenhum vértice novo da lethal trifecta é adicionado `[EXTERNO, SRC-TRIFECTA-01]`.
3. Toda edição de `especificador.md`/`atomic-spec.md`/`RULES.md` exige **emenda homologada**; RULE nova é `[PROPOSTA]` até registro (RULE-HG-02).
4. Viabilidade técnica de execução dos scripts (rate-limit, CI, custo) = **INDETERMINADO** — exige teste antes de adotar como gate.

**Recomendação:** começar pela **Opção equilibrada** (M1, M2, M6, M5, M3, M8), deixando M4 e M7 para uma segunda rodada após medir custo. `[DECISÃO NECESSÁRIA]` — Andraus decide via Orquestrador.
