# PROPOSTA DE EMENDAS — pacote equilibrado de melhoria da pesquisa do Especificador (M1, M2, M3, M5, M6, M8)

**[PROPOSTA — NÃO HOMOLOGADO / NÃO EDITA NENHUMA REGRA]** Autor: Orquestrador interno, 2026-10-06. Base: `PROPOSTA-MELHORIA-PESQUISA.md` (processo CONFORME pelo Revisor SOT) e escolha de Andraus (chat, 2026-10-06): **pacote equilibrado** (M1, M2, M6, M5, M3, M8; M4 e M7 ficam para uma 2ª rodada).
Este arquivo traz o **texto exato** que `especificador.md` §7 (Autopré-check) e `atomic-spec.md` §15 (método do Dossiê) receberiam **se e quando Andraus homologar**. Até lá, nada aqui é regra (RULE-HG-02: sem registro = `[PROPOSTA]`, não vinculante).

## 1. O que JÁ foi implementado (Detectores auxiliares, sem rede nas regras, fora do manifesto do auditor)
| Item | Artefato | Natureza | Testes |
|---|---|---|---|
| M1 + M2 + M8 | `scripts/check_sources_verbatim.py` | Detector (ENF-03): toda « » existe literalmente em `sources/` (ou é citação INTERNA do repositório → INFO); rótulo `não-capturado` colado a uma citação → WARN; `Data de acesso` presente e dentro da janela (padrão 90 dias, ECC-VAL-001) → WARN; Specs anteriores à regra → INFO | `tests/test_check_sources_verbatim.py` (13) |
| M6 | `scripts/collect_repo_meta.py` | Auxiliar (não gate): lê a **API pública** do GitHub **sem credencial** e gera rascunho `REPO-*.txt` com o campo-fonte de cada número; alertas = `INDETERMINADO` (nunca `0`); não decide elegibilidade | `tests/test_collect_repo_meta.py` (11) |
| — | **não ligados ao CI** | Entrar no CI (passo informativo) ou no Autopré-check é **mudança de processo = decisão de Andraus** (§2). | |
**Defeito encontrado e corrigido durante o desenvolvimento do M1:** a 1ª versão do detector contava o próprio documento verificado como "citação interna" e deixava passar qualquer citação inventada; o teste de citação inexistente o revelou. Hoje o corpus interno exclui os `.md` da própria unidade.
**Medição no repositório (2026-10-06):** `check_sources_verbatim.py` sem argumentos → 11 unidades, **ERRO=0, WARN=0, INFO=10** (as 3 reprovações recorrentes desta sessão já estavam corrigidas).

## 2. Texto proposto — `especificador.md` §7 (Autopré-check), a homologar
> - **[PROPOSTA] Captura verbatim (M1/M2):** antes de entregar Dossiê/`research.md`, confira que **toda citação entre « » existe literalmente** em `sources/<ID>.txt` (elipse só com **ambos os lados** literais). Conteúdo vindo de **resultado de busca ou de WebFetch mediado não vai entre aspas**: leva `[EXTERNO, não-capturado-verbatim]` e não sustenta sozinho alegação carregada. *Evidência do Orquestrador: `python scripts/check_sources_verbatim.py <pasta>` (o Especificador não tem Bash; o Orquestrador o executa e anexa a saída).*
> - **[PROPOSTA] Validade (M8):** toda captura tem `Data de acesso: AAAA-MM-DD` dentro da janela da complexidade (ECC-VAL-001: LOW 180 / MEDIUM 120 / HIGH-CRITICAL 90 dias).

## 3. Texto proposto — `atomic-spec.md` §15 (método do Dossiê), a homologar
> - **[PROPOSTA] Graduação de evidência por fonte (M3):** cada fonte declara **nível** (documentação oficial / padrão / artigo revisado / preprint / blog-prática / sumário secundário), **primária ou secundária** e **interesse do emissor** (fornecedor × independente). Fonte secundária ou de fornecedor não sustenta sozinha alegação carregada.
> - **[PROPOSTA] Registro de buscas (M5):** seção **"Registro de buscas"** no Dossiê: consultas feitas, fontes **descartadas** e **motivo**, data. (Reprodutibilidade e controle de viés de seleção.)
> - **[PROPOSTA] Repositórios por API oficial (M6):** os campos objetivos da régua ECC-06 (`stargazers_count`, `license.spdx_id`, `pushed_at` como proxy de último commit, `archived`, dono) são coletados da **API pública** e registrados **com o campo-fonte**; `INDETERMINADO` só para o que a API pública **não** expõe (ver decisão pendente abaixo). Helper: `scripts/collect_repo_meta.py`.

## 4. DECISÕES de Andraus pendentes (não tomadas por esta proposta)
1. **Homologar (ou não)** as emendas das seções 2 e 3 e **quando** (entram em `especificador.md`/`atomic-spec.md` por RPSA/ata).
2. **Ligar `check_sources_verbatim.py` ao CI** como passo **informativo** (`continue-on-error`, molde `check_refs.py`)? Recomendação do estudo: sim, informativo; promover a bloqueante só depois de medir.
3. **Alertas de segurança graves (RULE-ECC-06) quando a API pública não os expõe.** O precedente da SPEC-006 (`REPO-mem0.txt`) registrou **`0` "conservadoramente"** com Dependabot privado = INDETERMINADO — registrar 0 para dado desconhecido **não é conservador** e conflita com a captura do `guardrails-ai`, descartada por fail-closed. `check_repo_research.py` exige número. Opções (Andraus escolhe; nenhuma foi aplicada): **(a)** manter fail-closed — INDETERMINADO = NÃO CONFIRMADO (consistente com `guardrails-ai`; a SPEC-006, ainda não homologada, teria de rever o `mem0`); **(b)** aceitar um **proxy público explícito** (ex.: advisories publicados da API) com rótulo `proxy` e limite declarado; **(c)** exigir conferência manual por Andraus do que a API não expõe. O coletor **não** escolhe: grava `INDETERMINADO`.
4. **M4 (triangulação ≥2 fontes) e M7 (verificador ao vivo tri-estado, único com rede nova)** — 2ª rodada, após medir o custo do pacote equilibrado.

## 5. O que esta proposta NÃO faz
Não edita `especificador.md`, `atomic-spec.md`, `RULES.md`, CI nem `AGENTS.md`; não dá web ao Revisor nem ao Auditor Externo; não fecha decisão aberta (CONS-01: J-001, N-001, M-001, H-001, G-001, K-001, C-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001 seguem como estão); não altera `canon/`.
