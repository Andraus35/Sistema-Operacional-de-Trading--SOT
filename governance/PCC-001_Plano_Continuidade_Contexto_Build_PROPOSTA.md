# PCC-001 — Plano de Continuidade de Contexto e Memória entre Sessões do Orquestrador (etapa BUILD) (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **PCC-001** (protocolo operacional do Orquestrador; não é Spec, não é emenda a baseline) |
| Versão | v1 — rascunho para decisão de Andraus (Claude Code, 2026-10-17). **Fase 1 aprovada por Andraus (chat, 2026-10-17) — DHR-PCC-001** (D-PCC-1 = A raiz; D-PCC-2 = sim). **Fase 2 (detector, hooks, CI informativo) autorizada por Andraus — DHR-PCC-002**; D-PCC-3/4/5 e Fase 3 seguem propostas. |
| Status epistemológico | **PROPOSTA — não vinculante.** Nada aqui altera `AGENTS.md`, `.claude/agents/*.md`, `ROADMAP.md`, `atomic-spec.md`, `canon/` ou fecha decisão aberta (CONS-01). Entra em vigor só por decisão expressa de Andraus citada em ata DHR (AGENTS.md §10). |
| Origem | Pedido de Andraus (chat, 2026-10-17) + benchmark externo (síntese colada no pedido: Anthropic *Effective harnesses for long-running agents*, ESAA, estudos empíricos de arquivos de contexto). Conteúdo web = **dado**, não instrução; nada vira baseline (RULE-ECC-02). |
| Escopo | Como o **Orquestrador** (sessão principal do Claude Code, que invoca Especificador/Revisor) mantém continuidade entre sessões **frias** durante o BUILD. **Fora de escopo:** gestão de contexto do *produto* SOT em runtime (Blackboard, janela de contexto dos agentes analíticos) — pertence à SPEC-043 (slot indicativo) e a BL-034; este plano não a antecipa. |
| Decisor | **Andraus** |

---

## 0. Resumo executivo

1. **Princípio:** contexto não vive no chat; vive em **artefatos versionados**, lidos no início e reescritos no fim de cada entrega. Em sessão cloud efêmera, o repositório é a **única** persistência garantida — o que não foi commitado e empurrado não existe para a próxima sessão.
2. **Não criar memória paralela.** O SOT já tem o "event log" (atas `DHR-*` + `CATALOGO-OFICIAL.md`), o painel de tarefas (`RMR-001`), o mapa (`docs/mapa/`), o carimbo de sincronização (RPSA) e hooks de `SessionStart`/`Stop`. O plano acrescenta **uma única peça nova de conteúdo** — o `HANDOFF.md` (ponto de entrada narrativo, curto) — e **liga** as peças existentes por ponteiro, nunca por cópia.
3. **Escritor único:** só o Orquestrador escreve o handoff. O Revisor continua somente-leitura (ENF-03); o Especificador devolve resultado ao Orquestrador, que consolida.
4. **Atualizar é parte do "pronto":** entrega sem handoff atualizado no mesmo commit é incompleta. Garantia em camadas, como o BL-019: hook (aviso) → CI (bloqueio gradual) → Revisor (auditoria).
5. **Detector ≠ Gate (ENF-03):** o verificador de handoff **detecta** defasagem e avisa; nunca promove item, fecha decisão ou registra homologação.
6. **Implantação em 3 fases**, a 2ª e 3ª atreladas a gatilhos, para não construir antes de haver o que preservar (§7).

---

## 1. Diagnóstico — o que já existe e o que falta `[FATO ESTRUTURAL, verificado no repo em 2026-10-17]`

| Necessidade de continuidade | Já coberto por | Lacuna |
|---|---|---|
| Regras estáveis | `AGENTS.md`, `governance/CONSTITUTION.md`, `RULES.md` | — |
| Sequência/Spec autorizada/decisões abertas | `ROADMAP.md` (tabela "Estado atual do ciclo") | Linhas enormes (uma célula com > 1 000 palavras); bom como livro-razão, ruim como ponto de entrada de 30 s |
| Decisões duráveis (event log) | `governance/DHR-*` + `CATALOGO-OFICIAL.md` | — (equivale ao `decisions.md` do ESAA) |
| Backlog/gatilhos | `backlog/RMR-001_Painel_Backlog.md` + `scripts/backlog_triggers.py` | — |
| "Onde está o quê" | `docs/mapa/MAPA-PROJETO.md` (gerado) | Não-normativo; não diz **estado de trabalho** |
| Defasagem de agentes | RPSA / `scripts/check_rpsa.py` | Cobre atas × agentes, não **sessão × sessão** |
| Início de sessão | Hooks `SessionStart` (`map-sync`, `doc-sync-check`) | Nenhum injeta estado de trabalho |
| Fim de sessão | Hooks `Stop`/`SubagentStop` | Nenhum cobra registro do que foi feito/falhou |
| **Estado da tarefa em curso, becos sem saída, "não tocar", próximo passo, reverificar ao vivo** | **nada** | **É a lacuna que este plano fecha** |
| Raiz do repo | Whitelist HOD-001 §6b.1 | Um `.md` novo na raiz exige emenda de whitelist (precedente: `WORKFLOW.md`) |

Consequência: não se cria `state.md`, `decisions.md` e `tasks.json` paralelos (duplicariam DHR/CATALOGO/RMR-001 e gerariam divergência — pior que ausência). O handoff **aponta** para eles.

### 3.5 Anexo de tarefa (DHR-PCC-003, 2026-10-19) — extensão do handoff, sem memória paralela

Para trabalho grande entre sessões (ex.: o Plan de uma Spec CRITICAL) que não cabe nas 150 linhas do handoff: **um** anexo `tipo: anexo-de-tarefa`, `status: ATIVO`, citado pelo campo `anexo:` do frontmatter do handoff; **só ponteiros** (ID/linha), ≤80 linhas, cabeçalho padrão (`anexo_id`, `tarefa`, `serve_handoff`, `base_commit`, `status`); ao terminar, `CONSUMIDO` e movido para `docs/handoffs/anexos/` (INV-07). Não confundir com o *brief de decisão* (`BRIEFING-DECISAO-*`, para Andraus decidir) nem com passagens de sessão antigas (histórico). Verificação informativa: `check_handoff.py` HO-11..HO-15; a promoção a bloqueante é a D-PCC-4 (aberta). *[Texto aditivo — INV-07; nada acima foi alterado.]*

---

## 2. Arquitetura de memória em camadas

```
L0  Regras estáveis        AGENTS.md · CONSTITUTION · RULES            (muda por DHR, raramente)
L1  Ponto de entrada       HANDOFF.md  (≤150 linhas, reescrito a cada entrega)   ← NOVO
L2  Decisões duráveis      DHR-* · CATALOGO-OFICIAL · ROADMAP (livro-razão)      (append-only, existente)
L3  Tarefas / continuidade RMR-001 · specs/features/<SPEC>/{plan,checks}.md
                           [BUILD] BUILD-LEDGER (§6) — só na Fase 3
L4  Histórico              handoffs arquivados, encadeados por `previous`        (monotônico, INV-07)
L5  Evidência bruta        git log · CI · transcrições  → NUNCA ponte principal
```

Regras de leitura da sessão fria (ordem, com atalho de economia — 4Es: Eficácia > Economicidade):
1. `AGENTS.md` (já carregado pelo harness) → 2. `HANDOFF.md` → 3. só o que o handoff apontar em "Reverificar ao vivo" e "Ponteiros" → 4. `ROADMAP.md`/`atomic-spec.md` quando o trabalho tocar Spec (leitura obrigatória do AGENTS.md §1 continua valendo para entrega/revisão).
Short-circuit análogo ao RPSA: se `base_commit` do handoff == `HEAD` e a árvore está limpa, **não** reler L2 inteiro.

---

## 3. O artefato HANDOFF.md

### 3.1 Localização — decisão D-PCC-1 (recomendação: A)

| Opção | Caminho | Prós | Contras |
|---|---|---|---|
| **A (recomendada)** | `HANDOFF.md` na raiz | Caminho fixo, óbvio para qualquer agente/ferramenta (inclusive Cline); precedente `WORKFLOW.md` | Exige emenda do whitelist HOD-001 §6b.1 + ata |
| B | docs/handoff/HANDOFF.md (opção não adotada; o handoff vive na raiz) | Não toca o whitelist | Caminho menos descobrível; `docs/` é "referência/histórica" |

### 3.2 Contrato de campos (obrigatórios; o verificador checa presença, data e hash)

Frontmatter YAML:

```yaml
handoff_id: HO-2026-10-17-01     # monotônico por dia
previous: HO-2026-10-16-02       # elo da cadeia (null só no primeiro)
data: 2026-10-17
branch: <ramo de trabalho>
base_commit: <sha curto do HEAD no momento da escrita>
spec_autorizada: SPEC-006        # copiado do ROADMAP; o ROADMAP prevalece
fase: spec-first | build
autor: Orquestrador
```

Seções (nesta ordem; ausente = "n/a" explícito, nunca omitida):

1. **Objetivo da frente atual** (2–4 linhas).
2. **Estado** — 1 parágrafo narrativo (não dump).
3. **Feito nesta sessão** — com caminhos alterados (`arquivo:linha` quando útil).
4. **Verificado** — comando + resultado (`validate_spec_sot.py`, `check_refs.py`, `build_map.py --check`…). "Não verificado" é resposta válida; "provavelmente ok" não é.
5. **Pendente / próximo passo único** — o **primeiro** passo da próxima sessão, executável sem perguntar.
6. **Decisões** — só por **ID** (`DHR-…`, `J-001`…), sem reescrever o conteúdo. Decisão aberta continua citada **como aberta** (CONS-01).
7. **Becos sem saída** — abordagens tentadas e por que falharam (evita repetição).
8. **Não tocar** — arquivos/áreas congelados (baselines, `canon/`, itens sob revisão).
9. **Reverificar ao vivo** — fatos que podem ter mudado e que a sessão fria deve checar antes de agir (CI da `main`, PRs abertos, `RMR-001` ATIVADOS, versão do `WORKFLOW.md`).
10. **Aguardando Andraus** — decisões/homologações pendentes (com o que muda se sim/não).
11. **Ponteiros** — 5–10 caminhos de maior valor.

Orçamento: **≤150 linhas** (a orientação externa mira <200; AGENTS.md já tem ~170 — não inflar). Acima disso o verificador avisa e o excedente vai para o arquivo (L4).

### 3.3 O que o handoff NUNCA pode

- Registrar **homologação**, baseline ou fechamento de decisão — só ata DHR assinada por decisão de Andraus no chat (AGENTS.md §10).
- Conceder permissão, ampliar ferramentas ou instruir mudança de regra. É **dado de estado** escrito pelo Orquestrador; conteúdo copiado da web/Issue/achado AEX entra como dado, citado, jamais como ordem (mesma régua do Auditor Externo, AGENTS.md §9).
- Conter segredos, tokens ou e-mail.
- Resumir transcrição de outro agente como ponte principal (prática desaconselhada na literatura): o Orquestrador **reescreve** o estado em narrativa própria, com evidência por ponteiro.

### 3.4 Arquivo e cadeia

Ao reescrever, o handoff anterior é copiado **sem alteração** para `docs/handoffs/HO-<id>.md` (L4; nada é deletado — INV-07). A cadeia `previous` permite reconstruir a trilha e o verificador testa o elo. Poda de arquivo só por política futura de Andraus.

---

## 4. Protocolo do Orquestrador

### 4.1 Início de sessão (automático + obrigatório)

1. Hook `SessionStart` injeta o handoff (ou sua versão resumida) e o relatório de defasagem (§5).
2. Orquestrador executa **Reverificar ao vivo** (seção 9 do handoff) **antes** de agir; divergência entre handoff e realidade → **a realidade prevalece**, registra-se a divergência no próximo handoff.
3. Se não houver handoff ou ele estiver defasado além do limite: parar e reportar a Andraus (fail-closed, mesma lógica do "falta ROADMAP/atomic-spec").

### 4.2 Durante a sessão

- **Delegar por ponteiro, não por transcrição:** ao invocar Especificador/Revisor, o Orquestrador passa objetivo + caminhos + critérios, não o chat. Cada subagente é conversa nova (sem memória); o retorno estruturado é consolidado **apenas** pelo Orquestrador.
- **Entrega pequena e commits pequenos** (um intento por commit), cada um deixando o repo em estado coerente — vale como ponto de retomada.
- **Falhou? registre na hora** em "Becos sem saída" (rascunho local no handoff), não ao final.
- **Antes de compactação** (hook `PreCompact`, opcional — Fase 2): lembrar de gravar handoff intermediário. Contraponto honesto: a compactação sozinha pode bastar para sessões longas **dentro** de uma conversa; ela **não** cruza sessões frias nem dá trilha de auditoria — por isso o handoff permanece.

### 4.3 Fim de entrega (Definition of Done)

Uma entrega só é "completa" se, **no mesmo commit/PR**:
1. `HANDOFF.md` foi reescrito (novo `handoff_id`, `base_commit`, `previous` correto);
2. o anterior foi arquivado em `docs/handoffs/`;
3. `python scripts/build_map.py --check` passa (se `.md` mudou);
4. tudo foi **commitado e empurrado** ao ramo designado (ambiente efêmero; PR como meio, sem push direto à `main` — AGENTS.md §10).

### 4.4 Papéis

| Papel | Escreve handoff? | Papel no protocolo |
|---|---|---|
| Orquestrador (Claude Code nativo) | **Sim — único** | Lê, reverifica, delega, consolida, reescreve, arquiva |
| Especificador (RW) | Não | Devolve ao Orquestrador: o que fez, caminhos, o que falhou, o que verificou |
| Revisor (RO, ENF-03) | Não | **Audita** o handoff (§5.3); emite achado, não corrige |
| Andraus | Não precisa | Decide; sua decisão registrada em ata é o que torna algo "fechado" |

---

## 5. Enforcement em camadas (mesmo molde do BL-019 e do `check_doc_sync.py`)

### 5.1 Detector — `scripts/check_handoff.py` `[PROPOSTA — a implementar na Fase 2]`

Verificações determinísticas (exit 0 ok · exit 1 achado; **informativo** no início):

| ID | Verificação | Severidade inicial |
|---|---|---|
| HO-01 | Arquivo existe, frontmatter e 11 seções presentes | Erro |
| HO-02 | `base_commit` existe no histórico e é ancestral de `HEAD` | Erro |
| HO-03 | **Staleness:** arquivos fora de `docs/handoffs/` mudaram em commits posteriores a `base_commit` sem novo handoff | Aviso → Erro (Fase 3) |
| HO-04 | Cadeia: `previous` existe em `docs/handoffs/` e o arquivo arquivado é idêntico (hash) ao handoff que ele substituiu | Erro |
| HO-05 | ≤150 linhas | Aviso |
| HO-06 | IDs citados (`DHR-…`, `J-001`…) existem; decisão aberta do ROADMAP **não** aparece como fechada (reusa lógica de `check_doc_sync.py`) | Erro |
| HO-07 | `spec_autorizada` coincide com a linha "Próximo trabalho autorizado" do ROADMAP (ROADMAP prevalece) | Aviso |
| HO-08 | Padrões de segredo (varredura simples) | Erro |
| HO-09 | Linguagem de homologação indevida ("homologado", "baseline") sem ID DHR ao lado | Aviso |

### 5.2 Hooks (`.claude/settings.json`)

- `SessionStart` → `node scripts/handoff-hook.js session-start` — imprime handoff + resultado do detector; **não-bloqueante**.
- `Stop`/`SubagentStop` (Orquestrador) → `handoff-hook.js stop` — se HO-03 dispara, injeta lembrete "atualize o handoff antes de encerrar"; **não-bloqueante** (padrão `doc-sync-check`).
- Reutilizar `scripts/hook-io.js`. Falha do hook nunca derruba a sessão.

### 5.3 CI e Revisor

- CI: `python scripts/check_handoff.py` como passo **informativo** (`continue-on-error`) → promovido a **bloqueante** só por decisão de Andraus após N PRs limpos (régua de introdução gradual já usada por `check_refs.py`/`check_doc_sync.py`).
- Revisor (somente leitura): novo item no Passo 0 — "o handoff está presente, coerente com o diff e sem homologação indevida?". Achado do Revisor é matéria de auditoria; encaminhamento é de Andraus.

### 5.4 Garantia pelo próprio plano

| Falha possível | Camada que pega |
|---|---|
| Esquecer de atualizar | Hook `Stop` (aviso) → CI HO-03 → Revisor |
| Edição por Bash/outra ferramenta | Detector compara git, não o hook de ferramenta |
| Handoff mentindo sobre estado | "Reverificar ao vivo" + realidade prevalece + Revisor |
| Handoff que vira log append-only | HO-05 (≤150) + reescrita (não append) + arquivo |
| Conflito de merge entre sessões paralelas | Escritor único + um ramo ativo por vez; se ocorrer, vence o `handoff_id` mais novo e o outro vai para L4 com nota |

---

## 6. Etapa BUILD — ledger de implementação `[PROPOSTA — só na Fase 3, gatilho: 1º BUILD autorizado no ROADMAP]`

Hoje o BUILD/VERIFY-de-código está **adiado** (AGENTS.md §1). Quando for autorizado, a continuidade precisa de um equivalente do `feature_list.json` da Anthropic, **ancorado no que o SOT já tem** (BASpec + Enforcement Contract), não em lista inventada:

- `build/BUILD-LEDGER.json` (ou `.md` tabular — D-PCC-3): uma entrada por **BASpec** homologada a implementar: `{baspec_id, spec, classe (D/C/H/P), enforcement_contract, status: pendente|em_curso|implementado|verificado, passes: bool, evidencia: comando+commit, bloqueio}`.
- `passes` só vira `true` com **evidência executável** (teste/CI) — Classe D por script; Classe H/P por critério do `checks.md`. O Orquestrador **não** marca `verificado` por conta própria: VERIFY da skill ≠ CONFORME do Revisor ≠ homologação (AGENTS.md §5).
- Regra de ouro herdada do harness longo: **uma BASpec por sessão/PR**, estado limpo ao final (testes passam, sem meia-implementação), `init`/comando único de verificação documentado no ledger.
- Os limiares-piloto (convicção ≥70%, score ≥7/9) e J-001/N-001 abertas **não** podem ser tratados como definitivos em código: o ledger registra o parâmetro como "piloto" (CONS-01).
- Interação com BL-034/SPEC-040 (observabilidade) e SPEC-043: o ledger é artefato de **desenvolvimento**; quando essas Specs forem abertas, decidem se absorvem ou substituem — sem pré-empção (EUA-E21).

---

## 7. Implantação em fases

| Fase | Conteúdo | Gatilho | Reversível? |
|---|---|---|---|
| **1 — Manual** (imediata, após ata) | `HANDOFF.md` + template; arquivo `docs/handoffs/`; seção em AGENTS.md; Orquestrador cumpre à mão | Decisão de Andraus (D-PCC-1, D-PCC-2) | Sim (remover arquivos) |
| **2 — Automática** | `check_handoff.py`, `handoff-hook.js`, hooks, passo CI informativo, item no Passo 0 do Revisor, registro no CATALOGO/mapa/testes | Fase 1 usada por ≥3 sessões reais sem fricção grave | Sim |
| **3 — BUILD** | `BUILD-LEDGER`, HO-03 bloqueante | `milestone:` 1º BUILD autorizado (ROADMAP) | Sim |

Critérios de aceitação por fase:
- **F1:** sessão fria nova retoma sem perguntar "onde paramos?" (teste de aceitação, §8); handoff ≤150 linhas; nenhum arquivo normativo alterado fora do escopo da ata.
- **F2:** `check_handoff.py` com testes (handoff válido, `base_commit` inexistente, cadeia quebrada, seção ausente, segredo, decisão aberta tratada como fechada); hooks não-bloqueantes comprovadamente (falha do script ⇒ sessão segue).
- **F3:** ledger consistente com os `checks.md`; nenhum `passes: true` sem evidência.

---

## 8. Como medir se funciona (não presumir) `[RULE-MET-01]`

Há evidência empírica de que arquivos de contexto servem a práticas não padrão mas **não melhoram desempenho por si só**; logo, medir. Piloto leve na Fase 1→2:

| Métrica | Como coletar | Meta indicativa |
|---|---|---|
| Tempo/tokens até 1ª ação útil na sessão fria | Contagem de leituras de arquivo antes da 1ª edição | ↓ vs. linha de base (3 sessões sem handoff, se houver registro) |
| Perguntas "onde estávamos?" feitas a Andraus | Contagem manual | → 0 |
| Retrabalho de beco sem saída repetido | Revisor/Orquestrador anota | → 0 |
| Divergências handoff × realidade | Registradas em "Reverificar ao vivo" | Tendência ↓ |
| Custo do protocolo | Linhas escritas por entrega; tempo | ≤ ~5% da entrega (4Es: Economicidade nunca acima de Eficácia, mas sem desperdício) |

Teste de aceitação cego: abrir sessão nova, apenas com "continue", e verificar se o Orquestrador (a) identifica a Spec autorizada, (b) não reabre decisão fechada nem fecha aberta, (c) executa o "próximo passo único" corretamente.
Se após 5 sessões não houver ganho mensurável, o plano é revisto ou reduzido — decisão de Andraus.

---

## 9. Riscos e mitigação

| Risco | Prob. | Impacto | Mitigação |
|---|---|---|---|
| Handoff defasado (pior que nenhum) | Alta | Alto | DoD + hooks + HO-03 + "realidade prevalece" |
| Duplicar ROADMAP/CATALOGO e divergir | Média | Alto | Handoff cita por ID/ponteiro; HO-06/HO-07 |
| Handoff tratado como autoridade normativa (homologação por engano) | Média | Crítico | §3.3 + HO-09 + Revisor + AGENTS.md §10 |
| Inchaço (vira log) | Alta | Médio | ≤150 linhas, reescrita, arquivo |
| Injeção via conteúdo web/Issue copiado para o handoff | Baixa | Alto | Conteúdo externo = dado citado; Revisor audita; sem permissões no handoff |
| Overhead desproporcional | Média | Médio | Fase 1 manual enxuta; métricas §8; poda se sem ganho |
| Sessão cloud perde trabalho não empurrado | Média | Alto | DoD item 4 (commit + push ao ramo designado) |
| Conflito entre sessões paralelas | Baixa | Médio | Escritor único; `handoff_id` mais novo vence |

---

## 10. Decisões pedidas a Andraus

| ID | Pergunta | Recomendação |
|---|---|---|
| **D-PCC-1** | Localização do handoff: raiz (emenda de whitelist) ou `docs/handoff/`? | **A — raiz** |
| **D-PCC-2** | Autoriza redigir (a) §11 em `AGENTS.md` (≤12 linhas: "ler `HANDOFF.md` antes de agir; DoD inclui handoff") e (b) emenda do whitelist HOD-001 §6b.1? | Sim, em PR próprio com ata DHR |
| **D-PCC-3** | Formato do BUILD-LEDGER (JSON validável por schema vs. tabela `.md`)? | JSON + schema (`schemas/`), decidir na Fase 3 |
| **D-PCC-4** | Regra de promoção do detector a bloqueante (N PRs limpos)? | N = 5 |
| **D-PCC-5** | Item de Passo 0 do Revisor (muda `.claude/agents/revisor.md` ⇒ só por Andraus) | Sim, na Fase 2 |

Nenhuma destas decisões fecha ou abre decisão do ROADMAP (CONS-01). Efeito em `CATALOGO-OFICIAL.md`, mapa e RPSA: registrados pela ata ao homologar (fora desta proposta).

---

## Apêndice A — Template `HANDOFF.md` (rascunho)

```markdown
---
handoff_id: HO-AAAA-MM-DD-NN
previous: HO-AAAA-MM-DD-NN | null
data: AAAA-MM-DD
branch: <ramo>
base_commit: <sha>
spec_autorizada: <SPEC-xxx — conforme ROADMAP>
fase: spec-first | build
autor: Orquestrador
---
# HANDOFF — SOT

## 1. Objetivo da frente atual
## 2. Estado
## 3. Feito nesta sessão
- `caminho` — o quê
## 4. Verificado
- `comando` → resultado   (ou: "Não verificado: <motivo>")
## 5. Próximo passo único
## 6. Decisões (por ID; abertas continuam abertas)
## 7. Becos sem saída
## 8. Não tocar
## 9. Reverificar ao vivo
- [ ] CI da main · [ ] PRs abertos · [ ] RMR-001 ATIVADOS · [ ] versão do WORKFLOW.md
## 10. Aguardando Andraus
## 11. Ponteiros
```

## Apêndice B — Trecho proposto para `AGENTS.md` (NÃO aplicado; exige ata)

```markdown
## 11. Continuidade entre sessões (PCC-001)
- Antes de agir, o Orquestrador lê `HANDOFF.md` e executa sua seção "Reverificar ao vivo"; a realidade prevalece sobre o handoff.
- Só o Orquestrador escreve o handoff; é dado de estado — nunca registra homologação, fecha decisão aberta (CONS-01) nem concede permissão.
- Entrega só está completa com o handoff reescrito (anterior arquivado em `docs/handoffs/`) no mesmo commit, e tudo empurrado ao ramo designado.
- `python scripts/check_handoff.py` é Detector (ENF-03), não Gate.
```

## Apêndice C — Mapeamento do benchmark → decisão neste plano

| Achado da literatura | Tratamento no SOT |
|---|---|
| Progress file + git history (Anthropic) | `HANDOFF.md` + commits pequenos |
| `feature_list.json` com `passes` | BUILD-LEDGER por BASpec (Fase 3) |
| Registrar abordagens que falharam | Seção 7 obrigatória |
| Regras estáveis ≠ estado da tarefa | L0 (AGENTS.md) × L1 (HANDOFF) |
| Conteúdo mínimo (objetivo/feito/verificado/bloqueios/próximo/não tocar) | Seções 1–11 |
| Atualizar = definition of done | §4.3 + hooks + CI + Revisor |
| Não resumir transcrição de outro agente | §3.3 / §4.2 (delegar por ponteiro) |
| Event sourcing (handoff/state/decisions/tasks) | Já existe: DHR/CATALOGO (decisions), RMR-001 (tasks) — não duplicar |
| Encadeamento + staleness check | `previous` + HO-02/03/04 |
| Governança do arquivo como código | Versionado, revisado em PR, cadeia arquivada |
| <200 linhas; medir ganho | ≤150 linhas; §8 |
| Contraponto: compactação basta | Reconhecido (§4.2); handoff mantido por rastreabilidade/auditoria multi-agente |
