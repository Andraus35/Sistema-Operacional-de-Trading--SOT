# Estudo — garantias determinísticas para prevenir os erros de coesão (hooks, rules, schema, policy)

> **Não-normativo.** Estado atualizado após as decisões da `DHR-COESAO-001`. Estudo do Orquestrador (2026-10-17), a pedido de Andraus ("como regra geral: criar mecanismos determinísticos para prevenir esses mesmos erros; estude hooks, rules, schema, policy"). Sequência de `AUDITORIA-COESAO-MECANISMOS-2026-10-17.md`. Não homologa, não fecha decisão aberta (CONS-01), não altera `AGENTS.md`, agentes, `CODEOWNERS`, `canon/`, `ROADMAP.md`. Implementado neste PR: **só o detector** (`scripts/check_coesao.py`, informativo). O resto é proposta para Andraus.

## 1. Princípio
Um erro de coesão só é prevenível por código quando a "verdade" envolvida é um **fato ancorável**: um ID, um caminho, um enum, um conjunto, uma contagem, um status declarado. Texto livre que diz a mesma coisa de dois jeitos **não** é detectável por regex sem falso alarme. Logo, a regra geral é: **transformar a verdade em dado (uma única fonte) e fazer o resto apontar para ela**; onde não der, aceitar que a defesa é o Revisor e Andraus (defesa em profundidade).

## 2. Camadas de garantia — o que cada uma realmente dá (evidência neste repositório)
| Camada | Dá | Não dá | Evidência |
|---|---|---|---|
| **Hook do Claude Code** (PreToolUse/PostToolUse/Stop/SubagentStop) | Feedback imediato **na sessão**; PreToolUse/Stop podem bloquear | Roda só em sessão Claude Code; lido na abertura; **fail-open** por padrão; `SubagentStop` com `exit 2` **não foi honrado** em nuvem; agente em outra ferramenta (Cline) não o executa | `AVALIACAO-MECANISMOS-REVISOR…` §3; HANDOFF HO-21 §3; `.clinerules/sot-map.md` |
| **CI** (`ci.yml`) | A **única** camada fora do ambiente do agente; reproduzível | Só avisa se o passo é `continue-on-error` (hoje todos os detectores são informativos); só **impede** com proteção de branch exigindo o check | `ci.yml`; `CODEOWNERS` linha 2 (depende de config do repositório, não verificável daqui) |
| **pre-commit** | Barra o commit local | Exige `pre-commit install` (não há hook instalado em `.git/hooks` neste clone) e o `gate-check` lá é **no-op** (lê stdin do hook; vazio ⇒ `exit 0`) — COE-03 | `.pre-commit-config.yaml`; teste manual de `gate-check.js` com stdin vazio |
| **Selo (`GATE-MANIFEST.sha256`) + CODEOWNERS** | Detecta adulteração do gate; dono por arquivo | Selo não impede; CODEOWNERS só bloqueia com proteção de branch; hoje cobre 10 de 17 selados (COE-07) | `gate_manifest.py`; `.github/CODEOWNERS` |
| **Schema (JSON Schema)** | Garante **forma** de um dado estruturado | Não garante coerência entre documentos | `schemas/*.json` (só cobre os agentes de trading GEN-1; nenhum para mecanismos/atas/status) |
| **Rule/policy escrita** | Torna a obrigação citável | Sem verificador é só texto (RULE-HG-02: sem registro = `[PROPOSTA]`) | `AGENTS.md` §5; o caso da `DHR-ASK-002` (regra ativa por hook, sem ata) |
| **Detector Classe D** (`check_*.py`) | Cruza fatos entre arquivos, determinístico, testável, calibrável | Detector ≠ Gate (ENF-03): só previne quando alguém o liga como bloqueante | `check_doc_sync`, `check_handoff`, `check_refs`; **novo** `check_coesao` |

Conclusão: **hook + detector dão detecção; só CI bloqueante + proteção de branch dão prevenção.** Hoje o desenho é "detectar e avisar" em todos os pontos — escolha deliberada e coerente com ENF-03, mas significa que nenhuma das duas verdades listadas na auditoria seria *impedida* de entrar na `main`.

## 3. Mapa erro → controle
| Erro da auditoria | Causa-raiz | Controle determinístico | Estado |
|---|---|---|---|
| Teste existe e o CI não roda (O2) | Lista de testes mantida à mão no `ci.yml` | **COE-02**: todo `tests/test_*.py`/`test-*.js` precisa ser executado (nome, `discover`, ou `npm run` que o CI chama) | Implementado (informativo) |
| Hook sem script / script ocioso (O1) | Nada cruza `settings.json` × `scripts/` | **COE-01** | Implementado |
| "Proteção" que é no-op (O7: `gate-check` no pre-commit) | Script escrito para um canal, plugado em outro | **COE-03** (script que lê `readToolInput` não pode ser `entry` do pre-commit sem adaptador) | Implementado |
| Ata citada que não existe (D3) | ID usado em código, sem checar `governance/` | **COE-04** (estende o que `check_refs` faz para `.md` aos scripts/`.claude`/`.github`) | Implementado |
| `roadmap.md` × `ROADMAP.md` (D4/D5) | Windows ignora caixa; Linux não | **COE-05** | Implementado |
| Tabela do `AGENTS.md` × frontmatter do agente (D6) | Duas cópias da mesma lista de ferramentas | **COE-06** | Implementado |
| Selo sem dono (O3) | Duas listas (manifesto, CODEOWNERS) à mão | **COE-07** | Implementado |
| Skill solta (O4) | Convenção de pasta/`SKILL.md` não verificada | **COE-08** | Implementado |
| Config ociosa (`.eslintrc`, `.prettierrc`) | — | **COE-09** | Implementado (INFO) |
| Auditor "pausado" × "piloto" × "inerte" (D1) | O estado não é um dado | **COE-10** cobre o caso "workflow diz INERTE e o AGENTS não" | Parcial — a causa-raiz é o §4.1 abaixo |
| Pendência de merge já resolvida no HANDOFF (D2) | Relato escrito à mão | **COE-12** (compara com `origin/main`) | Implementado |
| README declara a Spec autorizada (D4) | Duplica o ROADMAP | **COE-13** | Implementado |
| Status textual "PROPOSTA" residual (D1) | Convenção "merge = assinatura" não atualiza o texto | **COE-11** (INFO) | Implementado |
| Camadas do Revisor inertes em nuvem (O1) | Mecanismo declarado ≠ mecanismo comprovado | §4.1 (campo `verificado_em`) | Proposta |
| Dois "gates de estrutura" (O5), skills legadas com "Synthesis Agent" | Duplicidade semântica | Não detectável por regex; exige decisão de arquivar (Andraus) | Fora do alcance |

## 4. Propostas — decisões de Andraus de 2026-10-17 (ata `DHR-COESAO-001`) marcadas
1. **[DECIDIDO: criar como PROPOSTA com detector — `governance/MECANISMOS.json`, schema e COE-14 entregues; `AGENTS.md` só aponta quando Andraus assinar VIGENTE]** **Registro de mecanismos como dado.** `governance/MECANISMOS.json` + `schemas/mecanismo.schema.json`: um item por hook/script/workflow/agente com `id`, `tipo`, `enforca` (norma/ata), `estado` ∈ {`ativo`, `inerte-em-nuvem`, `pausado`, `legado`, `proposta`}, `ata`, `verificado_em` (data + como), `selado`, `dono`. O detector passa a checar **os dois sentidos** (item sem arquivo; arquivo sem item) e o `AGENTS.md` §8/§9 deixa de repetir lista: aponta para o registro. Cura D1, D6, O1, O5 na raiz.
2. **[DECIDIDO E APLICADO: COE-01/02/04/05 bloqueiam no CI; `roadmap.md`→`ROADMAP.md` corrigido nos dois agentes]** **Promover a bloqueante** só o que não tem falso positivo comprovado: COE-01 (hook→script), COE-02 (teste fora do CI), COE-04 (ata inexistente), COE-05 (caixa). Hoje: após a calibração deste PR, o repositório atual não produz falso positivo nesses quatro (os ERRO restantes são os achados reais D5 e COE-05 e se resolvem editando os agentes). Exige decisão (como D-PCC-4 do handoff).
3. **[DECIDIDO: exigir CI + dono — configuração só de Andraus; ver risco de autor=dono na ata §3]** **Proteção de branch** na `main` exigindo o check "Validate SOT Harness" e revisão de dono (hoje o `CODEOWNERS` e o selo só detectam). É configuração do repositório, não código.
4. **[APLICADO: 7 linhas acrescentadas ao `CODEOWNERS`; selo não regravado]** **Completar o `CODEOWNERS`** com os 7 arquivos selados sem dono (COE-07), junto com a regravação do selo se algum arquivo mudar.
5. **Regra RULE-COESAO-01..03** (em `RULES.md`, junto do `RPSA`): (01) todo mecanismo ativo tem linha no registro e ata; (02) todo teste de mecanismo roda no CI; (03) workflow/hook "inerte" ou "pausado" precisa dizê-lo na norma que o descreve. Sem registro em `RULES.md`, é só `[PROPOSTA]` (RULE-HG-02).
6. **Adaptador de pre-commit** para o `gate-check` (passar os arquivos staged como payload) **ou** retirá-lo do `.pre-commit-config.yaml`: hoje dá falsa sensação de proteção (COE-03).
7. **Hook PostToolUse** (opcional) que roda `check_coesao.py --json` quando o arquivo editado é `settings.json`, `.claude/agents/*`, `ci.yml`, `AGENTS.md`, `README.md` ou `CODEOWNERS` e devolve o achado ao modelo na hora (feedback, fail-open, só em sessão Claude Code).
8. **Gate de ata para hook novo:** `COE-04` já impede citar ata inexistente; falta a regra inversa (hook registrado sem ata citada no cabeçalho do script) — fácil de acrescentar quando Andraus quiser exigir.

## 5. O que este estudo NÃO garante
Detector não elimina "duas verdades" em prosa livre (ex.: descrições do mesmo fluxo em `AGENTS.md`, README e ROADMAP com palavras diferentes); só os fatos ancoráveis. Por isso a proposta 1 move a verdade para dado e manda o resto apontar. O ganho comprovável é de **detecção contínua e barata** (a auditoria feita à mão hoje roda em ~1 s); a **prevenção** depende das decisões 2 e 3.
