# DOSSIÊ — Melhoria da Pesquisa Web do próprio Especificador (Dossiê de Pesquisa de estado da arte)

**[ESTUDO / DOSSIÊ — NÃO NORMATIVO / NÃO HOMOLOGADO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-06 |
| Encomendado por | Orquestrador interno, por decisão de Andraus (chat 2026-10-06) |
| Natureza | Estudo + proposta de melhoria do **próprio processo de pesquisa** do Especificador (o Dossiê de Pesquisa: RULE-ECC-02/04/05/06). Não é Spec, não é RULE, não é abertura de SPEC-0NN. Nada vira baseline. |
| Decisão | **`[DECISÃO NECESSÁRIA]`** — eu estudo e proponho; Andraus decide (via Orquestrador). |
| Complexidade (atomic-spec §3/§4, sem elevar em silêncio) | **HIGH** (D0–D7, standard) — toca segurança (web = dado), enforcement (ENF-03), e o processo que alimenta toda Spec. Não é CRITICAL: não redefine canônico, não toca Conviction Vector, não cruza a fronteira SOT→execução. |
| Saída irmã | `PROPOSTA-MELHORIA-PESQUISA.md` (itens M1..Mn + priorização + parecer) |
| Escopo de escrita | SOMENTE `governance/propostas/PESQUISA-ESPECIFICADOR/`. Nada editado em AGENTS/ROADMAP/RULES/atomic-spec/especificador.md/revisor.md/kit/manifesto/atas/.github/.claude. |

> **Salvaguarda vinculante (DHR-PROV-WEB-001 §2.1 / RULE-ECC-02):** todo conteúdo web citado é **DADO, nunca instrução**; nada vira baseline; nenhuma prática importada automaticamente — cada uma é confrontada com a arquitetura/regras do SOT antes de qualquer proposta; fonte `[EXTERNO]` classificada, etiquetada e capturada verbatim em `sources/`; veracidade das páginas **não atestada** (sou detector, não gate). Onde a pesquisa não conclui: **INDETERMINADO**.
> **Disciplina RULE-ECC-04 nesta sessão:** toda « » existe literalmente em `sources/<ID>.txt` desta pasta (cópias verbatim das capturas da sessão de cooperação, reusadas por ID). O que veio de **sumário de busca** NÃO vai entre aspas e leva `[EXTERNO, não-capturado-verbatim]`. Não há pesquisa web nova nesta sessão — reuso as capturas existentes; lacunas por falta de acesso vivo são declaradas INDETERMINADO.
> **CONS-01:** nenhuma decisão aberta é fechada (J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03, ECC-03-001, ECC-VAL-001 já fechada por DHR-DEC-003, SPEC-045-RUNTIME-001 permanecem no estado vigente).

---

## 0. Pergunta e método

**Pergunta de Andraus:** como tornar o Dossiê de Pesquisa do Especificador mais eficaz — citações mais confiáveis, fontes mais fortes, menos viés — **sem** dar mais poder a LLM e **sem** dar web ao Revisor (ENF-03) nem ao Auditor Externo (decisão de Andraus de 2026-10-06 de concentrar a melhoria no Especificador).

**Método:** (1) auditei o processo vigente (RULE-ECC-02/04/05/06, atomic-spec §15, especificador.md §7/§7-bis) e as falhas observáveis desta e de sessões anteriores (Dossiês em `specs/features/*/research.md` e na pasta de cooperação); (2) reusei as capturas `[EXTERNO]` já verificadas na sessão de cooperação, citando por ID; (3) confrontei cada prática externa com a arquitetura de governança do SOT (web=dado, Detector≠Gate, fail-closed) **antes** de propor. A proposta operacional está na saída irmã.

**Pesquisa Multi-Lente (RULE-ECC-05): NÃO INCIDE.** Este estudo é meta-harness (o processo de especificar), não toca comportamento de agente de trading, Conviction/Fusion Engine, Manager ou Risk Agent. Registrado explicitamente para o Revisor (mesma exclusão que SPEC-019/020/021/002).

---

## 1. E1 — Em que o processo de pesquisa falha hoje (evidência)

Cada falha abaixo tem **evidência observável** (in-repo = `[FONTE]`; externa = `[EXTERNO]` por ID) e é a base de um item Mn na Proposta.

### F-1 — Citação de sumário de busca tratada como se fosse a página (falha de proveniência)
- **Evidência in-repo `[FONTE]`:** nesta linha de trabalho, Dossiês registram explicitamente a correção de material que veio de **resultado de busca**, não da página: `DOSSIE-PESQUISA-COOPERACAO.md` §2 — "Dados numéricos vistos em *resultados de busca* mas **não** capturados verbatim de página ... **não** sustentam nenhuma proposta"; e §8 "C-02 resolvido ... a frase 'N-rollout' **não** está na página de SRC-REPRO-01 (veio de sumário de busca)". Isso só foi corrigido **após** o Revisor reprovar.
- **Por que importa `[EXTERNO, SRC-CITE-01]`:** agentes de pesquisa inflam a aparência de rigor — «the density of citations performs a rigour the links don't always have.» O sumário de busca é exatamente onde a "densidade" aparente excede o que a página sustenta.
- **Diagnóstico `[INFERÊNCIA]`:** o WebSearch devolve trechos sintetizados; o WebFetch é mediado por um modelo pequeno que resume a página. Nenhum dos dois é a página literal. Hoje a única barreira contra confundir os dois é a disciplina manual do autor + a reprovação a posteriori do Revisor. Falha recorrente, não pontual.

### F-2 — Citações entre « »/aspas sem captura verbatim correspondente (RULE-ECC-04 violada 3× nesta sessão)
- **Evidência in-repo `[FONTE]`:** o enunciado da tarefa e o rastro desta sessão registram **três reprovações** do Revisor por citação entre « » sem captura verbatim. O `DOSSIE-PESQUISA-COOPERACAO.md` §8 documenta pelo menos duas correções pós-NÃO CONFORME (C-01 elipse sem os dois lados literais; C-02 aspas sobre frase inexistente na página).
- **Diagnóstico `[INFERÊNCIA]`:** a RULE-ECC-04 é verificada pelo Revisor por string-match **depois** da entrega. Não há, do lado do Especificador, um passo determinístico que **antes de submeter** reprove toda « » cujo conteúdo não esteja literalmente num `sources/<ID>.txt`. O custo disso é ciclo de revisão desperdiçado e risco de "citation theatre" `[EXTERNO, SRC-CITE-01]` entrar na entrega.

### F-3 — Elipses dentro de aspas sem os dois lados literais
- **Evidência in-repo `[FONTE]`:** `DOSSIE-PESQUISA-COOPERACAO.md` §8 "C-01 resolvido ... citação corrigida para o literal sem elipse". A elipse (`...`) dentro de « » corta a verificação por string: o verificador não encontra a string contígua e ou falha (falso-negativo) ou é obrigado a aceitar sem checar.
- **Diagnóstico `[INFERÊNCIA]`:** a regra tácita "elipse só com ambos os lados literais" não é checável por string simples; exige partir a citação em dois trechos e checar cada um. Hoje isso é manual e foi fonte de reprovação.

### F-4 — Fontes fracas × fortes sem graduação formal obrigatória
- **Evidência in-repo `[FONTE]`:** a classificação por *tipo* (Padrão/Prática/Benchmark/Evidência/Experimento/Opinião) existe (atomic-spec §15), mas o *nível de evidência* e o *conflito de interesse* aparecem de forma ad hoc. Ex.: `DOSSIE-PESQUISA-AUDITOR-HIBRIDO.md` §2 mistura "blog reconhecido, não revisado", "preprint", "doc oficial de fornecedor" numa coluna de texto livre, sem régua de peso.
- **Por que importa `[EXTERNO, SRC-CITE-01]` + `[EXTERNO, SRC-JUDGE-01]`:** fontes secundárias (blog que resume estudo) carregam números que «generated more citations per query than ordinary search-augmented chat — and hallucinated them at higher rates.»; e referências de autoridade enviesam o juízo — «when we added automatically generated fake references to Assistant B's answer, the judge model considered Assistant B's quality to be superior.» Sem régua explícita de nível, uma conclusão carregada pode repousar numa fonte fraca sem que isso salte aos olhos.
- **Diagnóstico `[INFERÊNCIA]`:** falta um campo obrigatório e padronizado de **nível de evidência** + **conflito de interesse** (ex.: doc de fornecedor que vende o produto) por fonte, e uma regra de que **nenhuma alegação carregada repousa só em fonte fraca** (a prática já é seguida informalmente — `DOSSIE-PESQUISA-COOPERACAO.md` §2 "Nenhuma conclusão carregada repousa só em blog" — mas não é verificável).

### F-5 — Viés de seleção e falta de triangulação (uma fonte por alegação)
- **Evidência in-repo `[FONTE]`:** vários achados carregados dos Dossiês existentes repousam em **uma** fonte (ex.: Q7 em `DOSSIE-PESQUISA-COOPERACAO.md` §4 é `[INFERÊNCIA]` "por analogia interna", sem fonte externa dedicada — honestamente declarado, mas é exatamente o ponto: não há triangulação).
- **Por que importa `[EXTERNO, SRC-JUDGE-01]`:** o viés de autoridade e o bandwagon — «The tendency to give stronger preference to the majority's beliefs regardless of whether they are correct or not.» — operam quando o autor escolhe as fontes que confirmam a tese. Uma única fonte confirmatória é indistinguível de viés de seleção.
- **Diagnóstico `[INFERÊNCIA]`:** o §7-bis (Bloco A adversarial) do especificador.md ataca viés de confirmação nas BASpecs, mas **não** há exigência análoga para o Dossiê: "para cada alegação carregada, qual fonte a NEGA ou qual o limite dela". Falta triangulação (≥2 fontes independentes para alegação carregada) e um registro do que foi descartado.

### F-6 — Capturas curtas / no limiar e sem data de acesso consistente
- **Evidência in-repo `[FONTE]`:** a régua é ≥100 caracteres (RULE-ECC-04). `DOSSIE-PESQUISA-AUDITOR-HIBRIDO.md` §3-H7d registra o risco Goodhart: "esticar citação para ≥20 chars" — ou seja, otimizar a captura para passar o limiar em vez de capturar o contexto que sustenta a alegação. A data de acesso existe nas capturas, mas não há verificação de que ela está presente e dentro da validade (ECC-VAL-001: 90 dias HIGH/CRITICAL).
- **Diagnóstico `[INFERÊNCIA]`:** captura no limiar mínimo é "forma sem mérito": casa o string-match do Revisor sem garantir que o trecho realmente sustenta a alegação. O limiar protege a *forma*, não o *mérito* (mesmo problema do gate do auditor — `DOSSIE-PESQUISA-AUDITOR-HIBRIDO.md` §3-H7d).

### F-7 — Repositórios (RULE-ECC-06) quase sempre "NÃO CONFIRMADA" por falta de acesso vivo — e INCONSISTENTE entre sessões
- **Evidência in-repo `[FONTE]`, as duas pontas:**
  - Falha: `cooperacao/sources/REPO-guardrails-01.txt` — "Último commit: INDETERMINADO ... Alertas de segurança graves abertos: INDETERMINADO ... Veredito: NÃO CONFIRMADO — 2 dos 6 critérios ... não foram verificaveis a partir do conteúdo obtido". O resultado é um repositório potencialmente bom descartado por **limite técnico de acesso**, não por mérito.
  - Acerto (prova de que dá para fazer melhor): `specs/features/SPEC-006/sources/REPO-mem0.txt` e irmãos usam **a API pública do GitHub** como proxy — "Último commit: 2026-10-05 (proxy: campo pushed_at da API pública = 2026-10-05T04:18:38Z)" e "Alertas ... 0 (proxy público; Dependabot privado = INDETERMINADO)". Aqui o veredito foi **ELEGÍVEL**, com o resíduo privado honestamente marcado.
- **Diagnóstico `[INFERÊNCIA]`:** a régua ECC-06 exige dados (data do último commit, alertas) que **não aparecem no HTML renderizado** da página do repo, mas **aparecem em campos objetivos da API pública** (`pushed_at`, licença, estrelas, `archived`). Sessões que lembraram de usar a API confirmaram elegibilidade; a sessão de cooperação, não — e descartou por fail-closed. Resultado: o fail-closed da ECC-06, sem um caminho padronizado de coleta por API, produz **falso-negativo técnico** (bom repositório marcado NÃO CONFIRMADO) de forma dependente da sessão — exatamente o problema que Andraus apontou ("quase sempre NÃO CONFIRMADA por falta de acesso vivo"). A assimetria entre SPEC-006 (API) e cooperação (sem API) prova que o gap é **de método, não de régua**.

### F-8 — Datas e recência não verificadas contra a validade do Dossiê
- **Evidência in-repo `[FONTE]`:** ECC-VAL-001 foi FECHADA (DHR-DEC-003: LOW 180 / MEDIUM 120 / HIGH-CRITICAL 90 dias a contar da data de acesso). Mas não há verificação de que (a) toda captura tem data de acesso e (b) ela está dentro da janela da complexidade da Spec. Hoje é confiança no autor.

**Síntese E1 `[INFERÊNCIA]`:** as falhas são de **duas naturezas** — (i) proveniência/verificação (F-1,F-2,F-3,F-6,F-8: a citação não é garantidamente a página, e a verificação é só a posteriori pelo Revisor) e (ii) qualidade epistêmica (F-4,F-5,F-7: força de fonte, triangulação, falso-negativo técnico de repositório). Nenhuma exige dar mais poder a LLM; todas são tratáveis por **disciplina checada por código determinístico** (Detector, ENF-03) + pequenos ajustes de regra.

---

## 2. E2 — Estado da arte para melhorar (confrontado com a arquitetura SOT)

> Regra: achado externo ≠ fato SOT (TRACE-06). Cada prática é confrontada com invariantes/regras vigentes **antes** de virar proposta.

### E2.1 — Pesquisa agêntica / "deep research" com verificação de citação
- `[EXTERNO, SRC-CITE-01]` o alerta central: «the deep research agents, the tools built to be exhaustive, generated more citations per query than ordinary search-augmented chat — and hallucinated them at higher rates.» e «they found 3–13% were hallucinated (no record in the Internet Archive; in their words, they 'likely never existed') and 5–18% did not resolve at all.»
- **Confronto SOT `[INFERÊNCIA]`:** o SOT **não** deve adotar "deep research" que maximiza volume de citações — contraria o princípio fundador do especificador.md ("não maximize quantidade ... maximize Eficácia"). O que se adota é o **corolário defensivo**: se uma URL pode ser alucinada em 3–18% dos casos, **toda URL carregada tem de resolver e a citação tem de casar a página literalmente** antes de entrar. → **ADOTAR** verificação determinística de citação (M1/M2 na Proposta); **REJEITAR** aumento de volume de pesquisa.

### E2.2 — Triangulação de múltiplas fontes
- `[EXTERNO, SRC-JUDGE-01]` o viés de autoridade e o bandwagon mostram que uma só fonte (sobretudo de autoridade) distorce o juízo.
- **Confronto SOT `[INFERÊNCIA]`:** compatível com o §7-bis (redução de viés) e com RULE-INQ (evidência discriminante). → **ADOTAR** como regra de processo: **alegação carregada (adotar/adaptar/rejeitar/adiar) exige ≥2 fontes independentes OU marcação explícita `[INFERÊNCIA]`/INDETERMINADO quando só há uma** (M4). Não exige LLM novo — é disciplina + checagem de contagem.

### E2.3 — Graduação de evidência (nível, recência, conflito de interesse)
- `[EXTERNO, SRC-CITE-01]`/`[EXTERNO, SRC-JUDGE-01]` acima sustentam que nem toda fonte pesa igual.
- **Confronto SOT `[INFERÊNCIA]`:** o SOT já classifica por *tipo*; falta *nível*+*recência*+*conflito de interesse*. → **ADAPTAR** a tabela de fontes do §15 para campos padronizados e **ADOTAR** a invariante de processo "nenhuma alegação carregada repousa só em fonte fraca" (M3). Sistemas formais de graduação (ex.: hierarquias de evidência tipo GRADE em saúde baseada em evidências) são **referência de analogia** — **ADIAR** importação literal: o domínio é diferente; basta uma régua de 3 níveis (Forte/Média/Fraca) ancorada no tipo já existente.

### E2.4 — Registro de buscas (queries, resultados descartados) para reprodutibilidade
- `[EXTERNO, SRC-REPRO-01]` «sampling determinism is not the same thing as system determinism.» e «temperature=0 makes only the token selection rule deterministic. It does not guarantee that the entire inference system will produce exactly the same logits every time.»
- **Confronto SOT `[INFERÊNCIA]`:** a lição é **honestidade sobre reprodutibilidade** (RULE-MET-01): não se promete repetir a busca bit-a-bit, mas se **registra o contexto** (queries exatas, data, o que foi descartado e por quê) para que a decisão seja reconstruível (P13). → **ADOTAR** uma seção "Registro de buscas" no Dossiê (M5): termos usados, fontes examinadas e **descartadas** com motivo. Ataca o viés de seleção (F-5): o que foi descartado fica visível. Baixo custo, alto valor de auditabilidade.

### E2.5 — Tratamento de fontes secundárias / blog
- `[EXTERNO, SRC-CITE-01]` é ele próprio um blog que resume estudos — e o Dossiê de cooperação já o tratou como secundário, "dado, não atestado".
- **Confronto SOT `[INFERÊNCIA]`:** já é prática; falta torná-la **regra verificável**: fonte secundária (blog/resumo) nunca é a única base de alegação carregada e deve ser marcada como tal no campo de nível (M3/M4). → **ADOTAR**.

### E2.6 — Benchmark de repositórios GitHub/GitLab com critérios objetivos verificados por dados vivos (API)
- **Confronto SOT `[FONTE]`+`[INFERÊNCIA]`:** a régua ECC-06 (estrelas/licença/commit/arquivado/alertas/dono) já é objetiva. O gap (F-7) é **coleta**: os campos vêm da **API pública** (`pushed_at`, `license`, `stargazers_count`, `archived`), não do HTML. SPEC-006 já provou o caminho (proxy `pushed_at`). → **ADOTAR** como método padronizado: coletar os metadados por **API oficial pública** e registrar o campo-fonte na captura `REPO-*.txt`; marcar como **INDETERMINADO** apenas o que é genuinamente privado (estado de Dependabot privado), nunca o que a API expõe. Isso converte "NÃO CONFIRMADA por falta de acesso" em "ELEGÍVEL/NÃO ELEGÍVEL com resíduo privado nomeado". **Importante (ENF-03):** a coleta por API é **do Especificador** (que já tem WebSearch/WebFetch), não do Revisor nem do auditor; o Revisor continua conferindo por string sobre a captura.

### E2.7 — Verificação ao vivo tri-estado (já desenhada na Opção C) aplicada ao Especificador
- **Confronto SOT `[FONTE]`:** a `PROPOSTA-AUDITOR-HIBRIDO.md` §Opção C já descreve um verificador determinístico tri-estado — `VERIFICADO` / `DIVERGENTE` / `INACESSÍVEL-TÉCNICO` — para conferir ao vivo as fontes do `sources/` do **Especificador**, sem dar web a LLM nenhum. → **ADOTAR por reuso** (M7): é exatamente o instrumento que fecha F-1/F-2/F-7 do lado do Especificador. O tri-estado resolve o falso-negativo técnico (bloqueio/JS/paywall ≠ fonte ruim).

---

## 3. E3 — Ferramentas determinísticas que ajudariam SEM dar mais poder a LLM

Todas são **Detectores** (ENF-03): código que re-checa o que o LLM produziu; nenhuma decide nem homologa. `[EXTERNO, SRC-HITL-01]` sustenta o princípio: «Use deterministic logic (policy engines, rule-based classifiers) as the authoritative signal, with LLM-assisted classification as an optional input that a deterministic layer re-checks.»

### O que JÁ existe no repo `[FONTE]`
- `scripts/check_repo_research.py` + check `[STRUCT-12]` em `validate_spec_sot.py` + CI — gate estrutural da ECC-06: confere a seção "Pesquisa em repositórios", a presença de captura `REPO-*.txt` por URL, e aplica a **régua sobre os números capturados** (estrelas, licença, idade do commit, arquivado, alertas, dono). Limite declarado no próprio script: "NÃO verifica a veracidade dos números (sem web — ENF-03)". Ou seja: confere forma e aritmética da régua, não a coleta.
- `check_refs.py`, `check_doc_sync.py`, `check_rpsa.py`, `backlog_triggers.py`, `build_map.py` — família de Detectores no mesmo molde (informativo/CI), que são o **padrão de desenho** a reusar.
- RULE-ECC-04 verificada pelo Revisor por string-match (sem web).

### O que FALTARIA (candidatos, detalhados na Proposta)
1. **Verificador mecânico de captura (M1)** — um script que lê o Dossiê, extrai toda « »/citação e **reprova se o trecho não existe literalmente** em algum `sources/<ID>.txt` da Spec; trata elipse exigindo os dois lados literais (F-2/F-3). É o análogo, do lado do Especificador e **antes** da entrega, do string-match que o Revisor faz depois. **Não existe hoje** (o Revisor faz isso a posteriori). Puramente determinístico, sem web.
2. **Coletor de metadados de repositório por API pública (M6)** — um script/rotina que consulta a API oficial do GitHub/GitLab (`pushed_at`, `license.spdx_id`, `stargazers_count`, `archived`) e **preenche a captura `REPO-*.txt`** com o campo-fonte explícito. Fecha F-7. A chamada de rede é do Especificador (não do Revisor/auditor). Risco: rate-limit/rot → registrar como INDETERMINADO só o genuinamente indisponível.
3. **Verificador de fontes ao vivo tri-estado (M7)** — reuso direto da Opção C (`PROPOSTA-AUDITOR-HIBRIDO.md`): `VERIFICADO`/`DIVERGENTE`/`INACESSÍVEL-TÉCNICO`, saída versionada por fonte (URL + data + hash do conteúdo baixado + trecho que casou/não casou). Só `DIVERGENTE` é sinal de problema; `INACESSÍVEL-TÉCNICO` não reprova (declara limite). **Transferência de confiança** honesta: o Revisor passa a confiar na saída do fetcher (artefato inspecionável), não na web.
4. **Checador de datas/validade (M8)** — verifica que toda captura tem data de acesso e que está dentro da janela ECC-VAL-001 pela complexidade declarada (F-8). Trivial, determinístico.
5. **Checador de nível de evidência e triangulação (M3/M4)** — confere que a tabela de fontes tem o campo "nível" preenchido por enum {Forte,Média,Fraca} e que alegações marcadas como carregadas têm ≥2 fontes OU marcação `[INFERÊNCIA]`/INDETERMINADO. Semi-determinístico (a marcação de "carregada" é do autor; o código confere a contagem e o enum).

**Limite honesto `[INFERÊNCIA]`:** nenhum destes mede **mérito** (se a página sustenta de fato a tese) — medem **forma e proveniência**. O mérito permanece com o Revisor semântico + Andraus. Isso é por desenho (ENF-03: o gate é necessário, não suficiente), e é a mesma honestidade já registrada em `DOSSIE-PESQUISA-AUDITOR-HIBRIDO.md` §3-H7d.

---

## 4. E4 — Limites de segurança (web = dado)

- **Injeção indireta `[EXTERNO, SRC-OWASP-01]`:** «Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files.» + mitigação «Separate and clearly denote untrusted content to limit its influence on user prompts.» → o Dossiê já trata web como DADO (DHR-PROV-WEB-001 §2.1); a melhoria **não** pode afrouxar isso. Qualquer coletor por API/fetcher trata o retorno como dado inerte (não executa, não segue instruções da página).
- **Viés de autoridade / referências falsas `[EXTERNO, SRC-JUDGE-01]`:** «when we added automatically generated fake references to Assistant B's answer, the judge model considered Assistant B's quality to be superior.» → a verificação determinística de citação (M1/M7) é **exatamente** a contramedida: referência que não resolve/não casa não entra, logo não pode enviesar. Reforça F-4/F-5.
- **Citações alucinadas `[EXTERNO, SRC-CITE-01]`:** 3–18% de URLs problemáticas (número de fonte secundária, `[EXTERNO]` indicativo, não fato SOT) → M2/M7 (URL tem de resolver) é a defesa.
- **Least-privilege e lethal trifecta `[EXTERNO, SRC-OWASP-01]`/`[EXTERNO, SRC-TRIFECTA-01]`:** «Restrict the model's access privileges to the minimum necessary for its intended operations.» e «If your agent combines these three features, an attacker can easily trick it into accessing your private data and sending it to that attacker.» → o Especificador já tem leitura do repo + web; **não** se deve adicionar escrita automática guiada por conteúdo web nem exfiltração. A proposta **não** adiciona nenhum vértice novo da trifecta: os coletores rodam sem segredos, tratam retorno como dado, e nenhum dado sensível do projeto vai em query/URL (DHR-PROV-WEB-001 §2.1).
- **Reutilização de fontes:** todas as fontes citadas aqui já foram capturadas e reusadas por ID (`sources/` desta pasta). Nenhuma pesquisa nova foi feita, logo nenhuma nova superfície foi aberta nesta sessão.

---

## 5. E5 — Impacto nas regras (APENAS descrição — nada editado)

> Nada abaixo é editado. Descrição do que *exigiria* mudar e onde. Toda RULE nova é `[PROPOSTA]` até registro (RULE-HG-02).

- **`especificador.md` §7 (Autopré-check):** acrescentar itens de auto-verificação **antes** do Revisor: (a) "toda « » casa um `sources/<ID>.txt`" (M1); (b) "metadados de repositório coletados por API, resíduo privado nomeado" (M6); (c) "nível de evidência {Forte/Média/Fraca} por fonte + ≥2 fontes por alegação carregada" (M3/M4); (d) "seção Registro de buscas presente" (M5); (e) "datas dentro de ECC-VAL-001" (M8). **Exige homologação de Andraus** (o arquivo tem cabeçalho "NÃO altere sem emenda homologada").
- **`atomic-spec.md` §15 (método do Dossiê):** acrescentar os campos padronizados à tabela de fontes (nível de evidência, conflito de interesse, data de acesso, primário/secundário) e a seção "Registro de buscas"; descrever o tri-estado do verificador ao vivo (M7) como método de verificação do próprio Especificador. **Exige emenda homologada** (atomic-spec é baseline v1.5).
- **RULES / nova família (ex.: RULE-ECC-07 "verificação determinística de captura" e RULE-ECC-08 "coleta de metadados de repositório por API"):** seriam `[PROPOSTA]` até registro físico em `RULES.md` (RULE-HG-02: sem registro = proposta, não vinculante; detector `check_doc_sync.py` D(b) já vigia isso). Poderiam entrar como **refinamento** de ECC-04/06, não família nova, para menor custo.
- **Custo no Revisor (ENF-03: sem web):** **nenhum poder novo** ao Revisor. Ao contrário — os Detectores do Especificador fazem **antes** o que hoje o Revisor pega **depois** (as 3 reprovações por verbatim desta sessão), reduzindo o ciclo. O Revisor continua conferindo por string sobre `sources/` e sobre a saída versionada do fetcher (M7), dentro do seu mandato. A "transferência de confiança" (Revisor passa a confiar na saída do fetcher) é declarada e mitigada por artefato inspecionável (reuso de `PROPOSTA-AUDITOR-HIBRIDO.md` §OBS-03).
- **O que exige homologação de Andraus:** toda mudança em `especificador.md`/`atomic-spec.md`/`RULES.md`; a adoção de qualquer script como **gate** (vs. Detector informativo); a ativação de qualquer rede nova (API de repositório) como passo padrão. Nada disso é feito aqui — é `[DECISÃO NECESSÁRIA]`.

---

## 6. E6 — 4Es e proporcionalidade (ordenado por Eficácia/custo)

Ordem da proposta = maior Eficácia com menor custo primeiro (detalhe e justificativa 4Es por item na Proposta):

1. **M1 Verificador mecânico de captura** — mata diretamente as 3 reprovações desta sessão (F-2/F-3); custo baixo (script no molde `check_refs.py`); Economicidade alta.
2. **M6 Coletor de metadados de repositório por API** — fecha F-7 (o problema que Andraus nomeou); reusa o método já provado em SPEC-006; custo baixo-médio (rede do Especificador, rate-limit a tratar).
3. **M5 Registro de buscas** — ataca viés de seleção (F-5) e reprodutibilidade; custo quase zero (seção no Dossiê); alto valor de auditabilidade (P13).
4. **M3/M4 Nível de evidência + triangulação** — eleva a força das conclusões (F-4/F-5); custo baixo (campos + regra); parte verificável por contagem.
5. **M8 Checador de datas/validade** — trivial; fecha F-8.
6. **M7 Verificador de fontes ao vivo tri-estado** — maior Eficácia contra citação fabricada/sumário-como-página (F-1), mas maior custo (fetcher, rede, URL rot, transferência de confiança); por isso **depois** dos itens baratos, e como passo informativo antes de gate.

**Princípio 4Es `[FONTE: especificador.md §6.4]`:** Economicidade nunca passa por cima de Eficácia. Aqui a Eficácia dominante é **confiabilidade da fonte** (reduzir erro que chega ao Revisor/Andraus); o custo é baixo porque tudo é determinístico e reusa padrões existentes. Nenhum item aumenta poder de LLM — todos são Detectores.

---

## 7. Lacunas / INDETERMINADO (honestidade — RULE-MET-01)

- **Viabilidade técnica dos scripts:** não tenho Bash nesta sessão; **não** executei nem escrevi nenhum script. Se os coletores por API respeitam rate-limit da VM, se o fetcher tri-estado roda no ambiente de CI, e o custo real = **INDETERMINADO** (exige teste — mesma honestidade da `PROPOSTA-AUDITOR-HIBRIDO.md` H6).
- **Magnitude das citações alucinadas (3–18%):** fonte **secundária** (SRC-CITE-01 resume estudos não capturados na origem) → `[EXTERNO]` indicativo, não fato SOT; a magnitude exata para o modelo do Especificador é INDETERMINADA.
- **Não fiz pesquisa web nova:** reusei capturas da sessão de cooperação. Pode haver estado-da-arte mais recente (ex.: padrões de "citation grounding", provenance em RAG) que eu não capturei — declarado INDETERMINADO, não afirmado.
- **Nenhuma decisão aberta tocada/fechada (CONS-01):** J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001 permanecem no estado vigente. ECC-VAL-001 está FECHADA (DHR-DEC-003) e é usada apenas como parâmetro de verificação, não reaberta.

## 8. Etiquetagem / status epistemológico
- Fontes web = `[EXTERNO]` (captura em `sources/` desta pasta, veracidade não atestada, TRACE-06).
- Fatos do repo (scripts, Dossiês, atas, RULE): `[FONTE]`/`[FATO]` quando homologados.
- Derivações minhas: `[INFERÊNCIA]`. Propostas: `[PROPOSTA]`. Dependências de Andraus: `[DECISÃO NECESSÁRIA]` (na Proposta).
- `INDETERMINADO` usado onde a pesquisa/execução não conclui (§7).
