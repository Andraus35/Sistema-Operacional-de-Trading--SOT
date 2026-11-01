# PROPOSTA — Automação do Auditor Externo por GitHub Action (caminho B)

| Campo | Valor |
|---|---|
| Status | **PROPOSTA — NÃO HOMOLOGADA. Nada aqui foi implementado.** Depende de decisão de Andraus (§8). |
| Data | 2026-10-06 |
| De | Orquestrador interno |
| Para | Andraus (Decisor Final) |
| Contexto | O caminho A (tarefa agendada do ChatGPT/Codex) não produziu efeito no repositório; o Codex não encontrou agendador utilizável. O workflow atual cria o pedido `[AEX-REQ]`, mas **não inicia** o auditor. |
| Rótulos | `[FATO]` verificado em fonte · `[INFERÊNCIA]` raciocínio do orquestrador · `[NÃO VERIFICADO]` precisa de teste real |

## 1. O que muda `[INFERÊNCIA]`
O auditor (modelo da OpenAI) passa a rodar **dentro do workflow**, logo depois de o job `pedido` criar o `[AEX-REQ]`, com o gatilho já existente (rótulo `homologacao-final`). O ciclo pedido → auditoria → achado → validação fecha **sem intervenção manual**.

## 2. Fatos da documentação oficial `[FATO]`
Fonte: documentação da Codex GitHub Action (`openai/codex-action@v1`), lida em 2026-10-06.
- Autenticação **somente por chave de API** (`openai-api-key`); não há login por conta ChatGPT. Logo, o plano Plus **não** cobre este caminho.
- A Action instala o CLI e roda `codex exec`; aceita `prompt-file`, `output-file`, `output-schema(-file)`, `model`, `effort`, `sandbox`/`permission-profile`, `safety-strategy` (`drop-sudo` padrão).
- No sandbox `read-only` o modelo não altera arquivos **nem usa a rede**.
- Quem pode iniciar: por padrão, quem tem acesso de escrita ao repositório (`allow-users`/`allow-bots` ampliam).
- Recomendações oficiais: limitar quem inicia; **sanitizar** textos de PR/Issue contra injeção de prompt; manter `drop-sudo`; **rotacionar a chave** se houver suspeita; no `read-only`, o modelo "poderia ler a chave se alcançar a memória do processo".
- O exemplo oficial usa **dois jobs**: o que roda o Codex tem só `contents: read`; um segundo job, com `issues: write`, posta a saída.
- Eventos criados pelo `GITHUB_TOKEN` **não disparam outros workflows** (regra do GitHub) — por isso a Issue criada pelo job `pedido` não aciona o job `achado` sozinha.

## 3. Desenho proposto `[INFERÊNCIA]`
```
rótulo homologacao-final ──> job pedido (já existe: cria [AEX-REQ])
                                 │ needs
                                 v
                      job auditar  (contents: read, SEM write; chave OpenAI)
                        - checkout do commit do pedido (persist-credentials: false)
                        - ferramentas/kit da branch padrão (nunca do commit auditado)
                        - codex-action: sandbox read-only, drop-sudo,
                          prompt-file = prompt do auditor, output-schema = achados
                                 │ saída = JSON de achados (DADO)
                                 v
                      job postar  (issues: write, GITHUB_TOKEN, sem chave OpenAI)
                        - validate_finding.py (forma + citação literal no commit)
                        - só os que passam: Issue [AEX] + labels; --ack com veredito
```
Pontos de projeto:
1. **O modelo nunca tem token de escrita nem rede.** Lê o checkout e devolve JSON. Quem escreve é código determinístico (kit) em outro job.
2. **Sem `SOT_AUDITOR_TOKEN`.** O token pessoal deixa de ser necessário (pode ser revogado); as ações passam a aparecer como `github-actions[bot]`, não como Andraus — resolve dois limites da ata `-002`.
3. **A validação roda no mesmo run** (a Issue `[AEX]` do bot não dispararia o job `achado`); o job `achado` por `issues: opened` permanece para achados postados manualmente.
4. **Limite de custo por desenho:** só roda quando Andraus rotula o PR (como hoje), no máximo 3 rodadas por PR (`MAX_ROUNDS`), `effort` e `model` fixados no workflow.
5. **Interruptor:** `AUDITOR_EXTERNO_ENABLED` continua sendo a chave; remover o segredo `OPENAI_API_KEY` também desliga.

## 4. O que precisa ser criado/alterado `[INFERÊNCIA]`
- Nova ata (reverte "nenhum LLM no workflow, nenhuma chave de API guardada" de DHR-AUDITOR-EXTERNO-001) e **DIR-003** (diretiva: o auditor passa a operar no CI, sem ferramentas, saída em JSON).
- `kit/PROMPT-AUDITOR-CI.md` (derivado do `AGENTE-AUDITOR-EXTERNO.md` e da diretiva vigente) e esquema de saída (lista de achados sobre `finding.schema.json`).
- Adaptar `submit_finding.py`/`poll_requests.py` para o `GITHUB_TOKEN` e para rodar em Actions; testes unitários novos; regenerar `MANIFEST.sha256`.
- `auditor-externo.yml`: jobs `auditar` e `postar`, `needs`, permissões mínimas por job, Action **fixada por SHA de commit** (cadeia de suprimentos).
- Teste de ponta a ponta no PR #16 / Issue #17 (gabarito de 5 defeitos plantados) e medição de recall e falsos alarmes.

## 5. Riscos `[INFERÊNCIA]`
| Risco | Mitigação | Resíduo |
|---|---|---|
| Injeção de prompt via texto do PR/Issue | sandbox read-only; sem rede; sem token de escrita; saída validada e postada por código | o modelo pode produzir achados enganosos — são DADO consultivo, o Orquestrador verifica |
| Vazamento da chave OpenAI | `drop-sudo`; chave só no job `auditar`; chave dedicada com **limite de gasto**; rotação | a documentação admite leitura da chave na memória do processo no read-only |
| Custo | gatilho manual (rótulo), 3 rodadas, `effort`/`model` fixos, limite de gasto na conta OpenAI | **não sei estimar** o custo por execução |
| Cadeia de suprimentos da Action | fixar por SHA; revisar atualizações | depende de revisão humana |
| Hierarquia (reporte só ao Orquestrador) | Issue endereçada ao Orquestrador; veredito só em `--ack` | o dono do repositório vê tudo (como hoje) |

## 6. `[NÃO VERIFICADO]` (precisa de teste real)
- Custo por execução e modelo/`effort` adequados.
- Se `read-only` + `output-schema` funcionam juntos nesta versão da Action e no runner.
- Se o modelo consegue auditar sem rede (lê só o checkout) com a qualidade necessária.
- Comportamento real do `drop-sudo` no runner e do aviso de Node 20 descontinuado.
- Limites de uso/taxa da chave de API.

## 7. Alternativas
- **D — semi-automático (custo zero):** o GitHub já notifica Andraus quando o `[AEX-REQ]` nasce; Andraus abre uma sessão do Codex e cola um prompt de um clique. Sem decisão nova, sem chave.
- **A — tarefa agendada:** sem efeito comprovado; não recomendada sem verificação.

## 8. Decisões que são de Andraus (nenhuma tomada)
1. Autoriza **reverter** a regra "nenhum LLM no workflow / nenhuma chave de API"? (nova ata + DIR-003)
2. Cria uma **chave de API dedicada** na OpenAI, com **limite de gasto** definido por Andraus, e a guarda como segredo `OPENAI_API_KEY`?
3. Modelo e `effort` (decisão técnica a validar no teste).
4. Mantém D como contingência?
5. Mantém o token pessoal (`SOT_AUDITOR_TOKEN`) ou o revoga após o B funcionar?

## 9. Fontes
- Documentação da Codex GitHub Action — https://learn.chatgpt.com/docs/github-action (redirecionada de developers.openai.com/codex/github-action)
- Repositório da Action — https://github.com/openai/codex-action
- Ata `DHR-AUDITOR-EXTERNO-001` e `DHR-AUDITOR-EXTERNO-002` (este repositório).
