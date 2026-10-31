# DHR-AUDITOR-EXTERNO-009 — Ata — Gate fundido (Classe D) como ferramenta oficial do Revisor, sem Bash

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-11 |
| Status | **MESCLADA na `main` por Andraus (PR #103) — vigente, nos pontos mesclados; itens que a ata declara diferidos (ex.: R4, emenda F3) seguem diferidos.** *[texto anterior preservado — INV-07: "PROPOSTA — vira vigente só com o merge de Andraus."]* Continua a DHR-AUDITOR-EXTERNO-008 (R1/R2 já mesclados; R4 diferido). **Não altera** `.claude/agents/revisor.md`: a emenda do arquivo do Revisor (F3) exige texto aprovado por Andraus em ata própria. Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Proposta de desenho e de plano de fases; nenhum arquivo de agente e alterado por esta ata. A emenda do revisor.md (fase F3) sera ata propria com RPSA em escopo e sincronizacao dos agentes. |

## 1. Decisão de direção de Andraus `[FATO: chat, 2026-10-11]`
1. O Revisor deve ser **completo em si**, sem depender de mecanismos da nuvem; o **gate determinístico é a ferramenta oficial dele**.
2. O script cobre **somente o que não é objeto de julgamento do LLM**, em harmonia com o princípio determinístico × probabilístico do repositório (atomic-spec §10.6, CLASSE-MECH-001, PE-04/GPR-001): **todas** as funções determinísticas do Revisor, por **fusão e ampliação** dos scripts existentes.
3. Mecanismo de execução escolhido: **ferramenta estreita, somente leitura, sem Bash**.

## 2. Diagnóstico `[FATO]`
- **Contradição no arquivo do Revisor:** `.claude/agents/revisor.md` §3 manda rodar `python scripts/validate_spec_sot.py` como primeiro passo obrigatório (exit 1 ⇒ NÃO CONFORME Crítica sem análise semântica), mas o frontmatter dá ao Revisor só `Read · Grep · Glob`. Nas 3 rodadas do teste cego de 2026-10-11 ele declarou "gate não executado" e seguiu para o julgamento. Hoje a garantia do gate está no CI (bloqueante em todo `plan.md`), não no Revisor.
- **O princípio D/H/P/C existe e é aplicado às BASpecs das Specs novas** (CC-11, SPEC-002 em diante), **mas não foi aplicado aos 8 passos do próprio Revisor nem aos scripts do harness.** Este desenho é a primeira aplicação ao próprio harness.
- **Por que não Bash** `[FATO: documentação oficial de subagentes do Claude Code, lida em 2026-10-11]`: o campo `tools` aceita nomes de ferramenta, **não** restringe o Bash por padrão de comando; só um gancho `PreToolUse` na definição do subagente pode filtrar comandos, e a própria documentação o descreve como filtro de texto ("guardrail, não sandbox"), que **não é aplicado** quando a pasta não é confiável e **falha aberto** se o script do gancho não for executável. Bash completo quebraria a garantia estrutural de que o Revisor não escreve (ENF-03), e o Revisor lê texto de Spec como dado (superfície de injeção). Ferramentas MCP **podem** ser listadas no `tools` do subagente e escopadas a ele; sem a ferramenta, o Revisor não a tem (falha fechada).

## 3. Classificação dos passos do Revisor `[PROPOSTA — verificar item a item na fase F1]`
D = código decide (entra no gate fundido) · H = código levanta candidato, o Revisor confirma (seção "sinais") · P = julgamento do Revisor (fora do script). "Hoje" = onde já existe checagem determinística (a confirmar nos testes da F1).

| Passo | Verificação | Classe | Hoje |
|---|---|---|---|
| 0 | ROADMAP/atomic-spec/RULES presentes na raiz | D | não há (Revisor lê) → incorporar |
| 0 | RMR-001: item `ATIVADO` pendente | D | `backlog_triggers.py` (informativo) → incorporar |
| 0 | Carimbo `sincronizado-até` × livro-razão | D | `check_rpsa.py` → incorporar |
| 0 | Entrega corresponde à Spec autorizada | H | não há |
| 1 | Complexidade × profundidade-alvo | D | STRUCT-09 |
| 2 | R:R, score/convicção de Fase Piloto, 8 dimensões, hierarquia, 7 estados, 4Es, validade do Dossiê | D | `check_invariants.py` (informativo) |
| 2 | "SOT executa ordem", "ICT cria hipótese", "custo entra", apagar/remover histórico, "fonte de verdade" | H | não há → sinais por palavra-chave |
| 2 | Evidência ≠ Observação; sentido das salvaguardas | P | — |
| 3 | Bloco Constitution Check; CC-08 Herança; CC-11 Classe por BASpec; CC-12 estrutura do `PD-xx` | D | STRUCT-02 (parcial) → ampliar |
| 3 | CC-01..CC-12 quanto à verdade; disciplinas N8–N17 | P | — |
| 4 | Etiquetas e status epistemológico presentes | D | STRUCT-03/08 |
| 4 | IDs citados (RULE, DHR, CHM/CEM…) existem; cadeia Spec→Plan→Tasks sem órfãos | D | `check_refs.py` / `check_doc_sync.py` (parcial) → ampliar |
| 4 | CONS-01: decisão aberta tratada como fechada | D | STRUCT-07/10 |
| 4-bis | Dossiê presente; repositórios seguros | D | STRUCT-11/12 |
| 5 | BASpec com os 5 campos; PORQUE cita RULE/princípio | D / H | STRUCT-05 (parcial) → ampliar |
| 5 | Profundidade atinge o alvo; qualidade da BASpec | P | — |
| 5-bis | Adversarial e verificação epistêmica N8–N17 | P | sem gate possível (já reconhecido no arquivo) |
| 6 | EARS presente / lint | D | STRUCT-04 + `npm run lint` |
| 6 | Anti-vibe, 4Es na qualidade, latência, maturidade | P | — |
| 7 | Enforcement Contract com os 8 campos; nível ≥ piso do tipo (ENF-02); ENF-04..08 declarados | D | STRUCT-06 (parcial) → ampliar |
| 7 | Adequação do contrato ao efeito; ENF-03 na prática | P | — |
| 8 | Dependências a montante homologadas; downstream de bloqueador aberto ⇒ no máximo condicional | D / H | não há → ampliar |

**Regra de composição:** falha em item **D bloqueante** ⇒ NÃO CONFORME Crítica automática (já é a regra do arquivo, §3); itens **H** viram "candidatos a confirmar" no relatório; itens **P** ficam integralmente com o Revisor. Detector ≠ Gate (ENF-03) preservado: o código decide forma e valor; o Revisor decide sentido.

## 4. Desenho `[PROPOSTA]`
- **Gate fundido** (`scripts/revisor_gate.py`, nome indicativo): reúne `validate_spec_sot.py` e `check_invariants.py` e chama em bateria fixa os demais detectores D; saída `evidence` estruturada (commit, exit codes, hash da saída, seção D bloqueante, seção D informativa, seção H "sinais"). `run_gates.py` (R1) continua como runner para CI/Orquestrador.
- **Ferramenta estreita** (servidor local, sem rede): uma ferramenta `revisor_gate(spec)` cujo **único argumento** é o identificador/caminho de Spec validado por padrão fixo dentro de `specs/features/`; **sem shell**, só leitura, árvore de trabalho deve permanecer limpa; qualquer argumento fora do padrão é recusado. Ausente a ferramenta ⇒ o Revisor declara "gate não verificado" e o parecer fica **no máximo CONFORME condicional** (falha fechada).
- **Revisor:** `tools` ganha **apenas** a ferramenta estreita (sem Write, Edit ou Bash); §3 do arquivo é reescrita para refletir isso (fase F3).

## 5. Fases e critérios `[PROPOSTA]`
- **F0 — Prova de viabilidade:** um subagente de teste com o servidor escopado aceita a ferramenta; sem ela, declara "gate não verificado" e limita o parecer.
- **F1 — Gate fundido:** testes de regressão (as Specs vigentes passam; os defeitos do banco de estresse, branch `ferramentas-estresse`, são detectados na classe D) e verificação item a item da tabela §3.
- **F2 — Ferramenta estreita:** testes de recusa (argumentos com metacaracteres, caminhos fora de `specs/features/`, `..`, tentativa de escrita).
- **F3 — Emenda do `revisor.md`:** ata própria com o **texto exato** para aprovação de Andraus; RPSA em escopo, sincronização dos agentes antes da próxima Spec.
- **F4 — Medição:** repetir o teste de estresse com semente nova e defeitos de Andraus; comparar Revisor + gate contra o resultado de 2026-10-11 (29/30 na união de 3 rodadas).

Nada das fases F1–F4 começa antes do merge desta ata; F3 exige nova aprovação.

## 6. Limites
O gate nunca cobre sentido: nos 9 defeitos de sentido do teste cego o verificador de valores achou 0 de 9. A tabela §3 é proposta e será corrigida pelos testes da F1. A viabilidade da ferramenta no arquivo do Revisor está **a provar na F0**; se falhar, volta a Andraus.

## 7. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** Os 60% de CONFLICT-MAP/PP-PAP-001/RULE-EW-002 seguem adiados até o backtest da J-001. A abertura da SPEC-006 segue **não homologada**.

## 8. Registro
- [x] Esta ata · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [x] F0 · [x] F1 · [x] F2 · [ ] F3 (ata própria) · [ ] F4

**Resultado da F0 `[FATO: execução de 2026-10-11, agente isolado via CLI]`:** aprovada. Servidor de teste (fora do repositório) com a ferramenta `revisor_gate`: (a) o agente que a declara a vê e executa o validador (`exit_code=0` na SPEC-001); (b) o agente de controle sem a ferramenta responde "indisponível" e não improvisa (falha fechada); (c) com o servidor definido **dentro** do agente (`mcpServers` como lista), o agente principal não enxerga a ferramenta; (d) entrada maliciosa (`../x; echo hacked`) chega ao servidor e é recusada **lá**. **Não provado:** recusa observada de escrita (o agente não tem a ferramenta, não tentou) e o comportamento com um arquivo de agente real na pasta de agentes (possível exigência de pasta confiável) — a cobrir na F3. Agente sem lista `tools` herda todas as ferramentas: a lista do Revisor deve permanecer explícita.

**Resultado da F1 `[FATO]`:** `scripts/revisor_gate.py` (gate fundido) + `tests/test_revisor_gate.py` (10 testes). Nas 10 Specs vigentes: **0 reprovação em D e 0 sinal H** (calibração; dois falsos alarmes reais corrigidos — IDs abreviados como `RULE-CEE-003` e contexto adversarial). No material cego do teste de estresse: D 12/30 e H 10/30, união **22/30** (tipos: números 6/8 em D; sentido 7/9 em H), **0 além do que o Revisor já achou** (Revisor ∪ gate = 29/30). **Medição otimista:** os sinais H foram escritos depois de conhecer as classes de defeito; o valor real só aparece na F4 (semente nova, defeitos de Andraus).

**Resultado da F2 `[FATO: execução de 2026-10-11]`:** `scripts/revisor_gate_mcp.py` (servidor MCP local, stdio, **uma única ferramenta** `revisor_gate(spec, rapido?)`) + `tests/test_revisor_gate_mcp.py` (10 testes). Garantias testadas: argumento `spec` só aceito por `^SPEC-[0-9]{3}$` (19 formas de entrada maliciosa ou malformada recusadas, incluindo `;`, `&&`, `$()`, crases, quebra de linha, byte nulo, caminho completo e `..`); tipos errados e argumentos extras recusados; Spec inexistente recusada; **nenhum efeito colateral de comando injetado** (arquivo-marcador não é criado); **symlink para fora de `specs/features/` barrado**; método e ferramenta desconhecidos retornam erro; árvore de trabalho comparada antes/depois (mudança ⇒ resultado descartado); `git status` idêntico após execução. Prova ponta a ponta com o Claude Code: agente com `mcpServers` embutido e `tools` explícita viu apenas `Read · Grep · Glob · mcp__sot-revisor-gate__revisor_gate`, rodou o gate na SPEC-001 e na SPEC-002 (`PASSOU_D`) e teve a injeção `SPEC-001; echo hacked` recusada pelo servidor. **Segue não provado** (F3): comportamento com o arquivo de agente real na pasta de agentes (pasta confiável) e recusa observada de escrita (o agente simplesmente não tem a ferramenta). **O arquivo do Revisor NÃO foi alterado.**

**Achados da preparação da F3 `[FATO: execuções de 2026-10-11 com arquivo de agente real]`:**
1. **Defeito real corrigido:** o servidor quebrava no Windows ("Connection closed") no caminho feliz, porque a saída padrão usa cp1252 e o relatório tem "≠", "→", "—". Passou despercebido na F2 porque os testes forçavam UTF-8 por variável de ambiente. Correção no servidor (UTF-8 forçado + JSON em ASCII) e 2 testes de regressão que **falham no servidor antigo e passam no corrigido** (12 testes no total).
2. **Armadilha de teste:** `--strict-mcp-config` **bloqueia** servidores embutidos em arquivos de agente (só não filtra os passados por `--agents`); testes de arquivo com essa flag dão falso negativo.
3. **Agente de arquivo (nível de usuário), servidor embutido via `mcpServers`:** o agente viu só `Read · Grep · Glob · mcp__sot-revisor-gate__revisor_gate`, rodou o gate (`PASSOU_D`, 0 sinais H), teve a injeção `SPEC-001 && echo x` recusada e não criou arquivo (sem ferramenta de escrita).
4. **Confiança de pasta `[FATO: documentação oficial lida em 2026-10-11]`:** servidores embutidos em arquivos de **`.claude/agents/` do projeto só carregam depois que a pasta é confiável**; em sessões não interativas (`-p`, CI) isso não conta. Servidores embutidos em `~/.claude/agents/` ou passados por `--agents` carregam sem essa verificação. **Consequência para a F3:** o Revisor do projeto funcionará com a ferramenta em sessão interativa com a pasta confiável; fora disso ele fica **sem a ferramenta e falha fechado** ("gate não verificado", parecer no máximo condicional). A F3 precisa decidir se isso basta ou se o Revisor também deve existir como agente de usuário.

---

**Andraus** — *decisão de direção em chat, 2026-10-11; registro feito pelo Orquestrador interno. Assinatura = merge desta ata.*
