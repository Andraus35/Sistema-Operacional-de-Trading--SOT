# PLANO — Fechar a H-001 sem quebra documental + roteamento de modelos por tarefa (economia de rodadas)

> **[PROPOSTA] — nada aqui é decisão, ata ou baseline.** Pedido de Andraus (chat, 2026-10-18): (1) fechar a H-001 completamente, incluindo a tecnologia, sem pendências nem quebras documentais; (2) antes, medir a eficácia do **hash** (`spec_delta.py`) e da **data de última sincronização** (carimbo RPSA) para economizar releitura; (3) o Orquestrador agrupa tarefas por modelo (Opus 5.5 × Sonnet 5.5) e faz sozinho as correções mínimas, seguindo à risca os relatórios de não conformidade do Revisor. Números de tokens = soma do que cada subagente consumiu nesta sessão (medidos); estimativas futuras = [INFERÊNCIA].

## 0. Medição já disponível (esta sessão)
| Chamada | Tokens | Observação |
|---|---|---|
| Revisor, revisão **integral** v1.7 (rodada 8) | ~218 mil | 4 Médias |
| Revisor, revisão **integral** v1.8 (rodada 9) | ~203 mil | 4 Médias novas |
| Revisor, revisão **por delta** v1.11 (10 de 122 blocos) | ~151 mil | 0 Médias; **−26% a −31%** vs integral |
| Especificador, edição só do cabeçalho (5 linhas) | ~58 mil | tarefa **mínima**: custo desproporcional |
| Especificador, correção N-08 + menores | ~106 mil | tarefa **mecânica com localização exata** |
| Especificador, Plan v1.7 / v1.8 / proposta de divisão | 313 / 240 / 241 mil | desenho — pertence ao Opus |
| Orquestrador, correção n-d e citação do changelog | poucos mil | 2 edições de 1 linha cada, validadas pelo gate |
**Leitura:** o hash (delta) economiza ~30% — bem menos que os "84% inalterado" do indicador, porque o Revisor ainda lê dependentes, a amostra anti-leniência (≥5 blocos) e os blocos sempre integrais. O carimbo de sincronização evita reabrir ~15 atas (EUA-E04..E18) por rodada (o Revisor declarou "não reabri"). **O maior desperdício medido não é a leitura: são tarefas mínimas entregues a um agente caro (58–106 mil tokens para o que o Orquestrador fez em poucos mil).**

## Fase 0 — Medir e fixar a régua (barato, ~30 mil tokens, sem mudar nenhum arquivo normativo)
1. Registrar a tabela acima como dado de estado (`governance/propostas/`), com a regra de coleta (tokens por chamada).
2. Conferir o carimbo `sincronizado-até`: `check_rpsa.py` já alinha (`--write`); medir quantas atas o agente deixaria de reabrir.
3. Régua de decisão: manter hash/carimbo se a economia por rodada ≥ 25% **sem** perder achados (calibrar com o banco de defeitos plantados já existente).

## Fase 1 — Roteamento determinístico por tarefa (Orquestrador antes de chamar o agente)
**Classes de tarefa (regra em código, não em juízo):**
- **M — mínima/mecânica (o Orquestrador faz):** o achado do parecer traz *arquivo:linha* + ação prescrita (texto → texto) + condição de aceitação verificável por assertiva; toca ≤ N linhas / ≤ 2 blocos; **não cria regra, predicado, código, campo nem mecanismo**. Execução: aplica a ficha de correção, roda os gates (validate, revisor_gate, invariantes, `spec_delta` — o delta deve mostrar **só** as linhas listadas), registra no commit a lista de achados atendidos. Falhou qualquer gate ou o delta saiu do previsto ⇒ **escala** (não improvisa).
- **S — auditoria/conferência (Sonnet 5.5):** revisão por delta, conferência de citações, banco de regressão.
- **O — desenho (Opus 5.5):** redação de regra/BASpec novos, dossiê, proposta de opções, mudança que cria mecanismo.
**Agrupamento:** o Orquestrador monta a fila de achados da rodada e a divide em **um lote por modelo** (M: ele; S: 1 chamada ao Revisor; O: 1 chamada ao Especificador com TODOS os achados de desenho) — troca "N rodadas pequenas" por "1 chamada por lote".
**Regra de congelamento (a "catraca"):** nas rodadas 5–9 cada correção criou um mecanismo novo que gerou a Média seguinte. Correção de classe M/S **não pode** criar mecanismo; se precisar, vira lote O e vai a Andraus antes.
**Como garantir "modelos diferentes por tarefa" (REVISADO por Andraus, 2026-10-18: 2 agentes, não 4).** Cada chamada a um agente começa com contexto do zero, com 2 ou 4 arquivos de agente — a releitura só cai com **menos chamadas**, hash/delta, carimbo, caminhos em vez de texto colado e **continuação do mesmo agente por `SendMessage`** quando o modelo for o mesmo (vale para o Especificador e rodadas curtas; no Revisor pesa o risco de ancoragem). Portanto: **mantém-se `especificador` (Opus 5.5) e `revisor` (Sonnet 5.5) como padrão no frontmatter** e o **hook roteador passa a aceitar `model` por chamada SOMENTE se for igual ao valor da tabela da classe da tarefa** (S1/S2 → Sonnet 5.5; S3/O → Opus 5.5), negando qualquer outro; classificação que falhe ⇒ **nega o override e vale o frontmatter (fail-closed)** — hoje o hook é fail-open. Sem arquivos de agente novos.
**Esforço (`effort`):** coluna **reservada** na tabela, **desligada** (continua negada) até um **piloto** (~150–200 mil tokens, uma vez): mesma revisão por delta com defeitos plantados em 2 níveis de esforço, comparando achados e tokens. Motivo: rebaixar o Revisor já custou achados (DHR-AUDITOR-EXTERNO-014: Sonnet 4.6 achou 0/18 × 14/18 do 5.5); 4Es — Eficácia antes de Economicidade. Se o piloto confirmar economia sem perda, ativa-se só para S1 (conferência mecânica).
**Requer ordem/ata de Andraus:** emenda à `DHR-ROTEAMENTO-003` (R-AC deixa de negar `model` e passa a validar contra a tabela), `scripts/roteador_modelos.py` + testes (CI), regravação do selo (script selado) — **sem** mexer em `.claude/agents/*`, `AGENTS.md` §3, `docs/agentes/INDICE-AGENTES.md` nem carimbos RPSA (texto dos agentes não muda ⇒ RPSA `nao`). Ressalvas a registrar na ata: o **Revisor continua independente** (nunca revisa o que ele próprio corrigiu; M é auditado no delta da rodada seguinte); ENF-03/ENF-07; o Orquestrador **não** altera semântica de Spec — só aplica a ficha do Revisor.
Custo estimado: ~40–70 mil tokens + 1 ata (menor que os 4 agentes). Ganho esperado [INFERÊNCIA]: tarefas M deixam de custar 60–100 mil cada.

## Fase 2 — Fechar a H-001 por inteiro (tecnologia incluída), sem quebra
**Passo 1 — Estudo (1 chamada Opus, reaproveitando o Dossiê válido até 2027-01-03):** opções (grafo/property graph · grafo temporal estilo Graphiti · estrutura em memória/relacional + log append-only · híbrido), critérios do SOT (imutabilidade INV-07; E3 fail-closed; trace completo CEM-001; auditoria; Eficácia antes de custo — 4Es; SOT não executa ordem), o que cada uma exige do BUILD, riscos e gatilho de revisão. Rotulado [PROPOSTA].
**Passo 2 — Andraus escolhe a tecnologia** (AskUserQuestion; recomendação primeiro).
**Passo 3 — Mapa de sincronização determinístico (pré-voo):** `grep` + script lista cada ocorrência de H-001 (hoje: ROADMAP 6 · AGENTS 1 · atomic-spec 6 · revisor.md 3 · especificador.md 4 · CATALOGO 23 · RULES 6 · RMR-001 20 · CIC-001 · plan.md/checks.md da SPEC-006). O `check_doc_sync.py` já cruza decisões abertas/fechadas do ROADMAP contra os registros — **é o detector que impede a quebra**.
**Passo 4 — Um PR único e atômico** (com sua ordem expressa para cada arquivo protegido): ata nova (decisão + tecnologia + cláusula de revisão por gatilho) · ROADMAP (tira H-001 de "ativas", entra em "FECHADAS"; linhas 177/508) · `AGENTS.md` §7 · `atomic-spec.md` §12 (linha H-001) · `revisor.md` §8 (tabela de bloqueadores e remoção do teto "condicional" **só** da SPEC-006 — H-001 era o único bloqueador dela) · `especificador.md` · RULES/RMR-001 (BL-003: gatilho `spec:SPEC-006 em redação` já consumido; reavaliar encaminhamento; G-001 permanece ABERTA) · CATALOGO/CIC · RPSA. **Errata da SPEC-006** (estado "INDETERMINADO" do mecanismo físico → decisão; limites "integridade física sem digest" e "travessia = H-001/BUILD" passam a referenciar a escolha) — tarefa mista: M para troca de referência, O para qualquer regra nova; **Revisor por delta** só nos blocos alterados; ata de homologação (hash novo registrado).
**Passo 5 — Verificação:** `check_doc_sync`, `check_refs`, `check_rpsa`, `check_invariants`, `check_coesao`, `check_handoff`, gate, suíte completa, mapa; CI verde; **só então** mesclar.
**Não fecha:** G-001 (estado persistente por agente — SPEC-009), K-001, M-001, J-001, N-001, C-001, WF-D03 (continuam abertas; ficam fora do PR).
Custo estimado [INFERÊNCIA]: estudo ~150–250 mil (Opus) + sincronização documental ~40–60 mil (Orquestrador, classe M) + errata/Revisor por delta ~200 mil ⇒ **~400–500 mil** em vez de ~700 mil+ no ritmo anterior (rodadas integrais e Especificador para ajustes mínimos).

## Ordem recomendada e pontos de parada
1. **Fase 0** (medir) → 2. **Fase 1** (roteador + 2 agentes por papel + ata) → 3. **Fase 2** (H-001), já usando o roteamento. Cada fase termina com PR e CI verde; Andraus pode parar entre elas.
**Riscos:** (a) fechar a tecnologia em spec-first pode envelhecer — mitigar com cláusula de revisão por gatilho (ex.: início do BUILD); (b) 4 arquivos protegidos tocados — exige ordem expressa; (c) classe M mal classificada — mitigada por escalada automática quando gate/delta divergem; (d) mais agentes = mais carimbos RPSA para manter.

## Decisões que são só de Andraus
Aprovar o plano e a ordem das fases · emendar a DHR-ROTEAMENTO-003 (hook valida `model` contra a tabela; 2 agentes, sem criar outros) · a tecnologia da H-001 · autorizar a edição dos arquivos protegidos listados · destino dos 12 ramos e abertura da SPEC-007.

## Resultado da Fase 0 (2026-10-18) — medição, sem mudar nenhum arquivo normativo
| Mecanismo | Medido | Veredito (proposta) |
|---|---|---|
| **Hash / delta por bloco** (`spec_delta.py`) | Revisão integral 203–218 mil tokens × por delta 151 mil (10 de 122 blocos): **−26% a −31%** | **Manter.** Só vale quando < 50% dos blocos mudam, sem mudança de Complexidade e com parecer anterior (já é a regra do `revisor.md` §3-bis) |
| **Carimbo de última sincronização** (`sincronizado-até` × livro-razão RPSA) | Dispensa reabrir 15 atas EUA-E04..E18 (≈ 15 mil tokens de leitura por agente, por rodada); o Revisor registrou "não reabri" | **Manter.** Custo ≈ 0 (verificação de 1 linha pelo `check_rpsa`) |
| **Ficha de correção mínima feita por agente caro** | Cabeçalho (5 linhas): 58 mil; N-08 + menores: 106 mil; o Orquestrador fez correções equivalentes de 1 linha com poucos mil | **Mudar** → Fase 1 (classe M) |
| **Rodada integral repetida** | Rodadas 8 e 9 integrais: 218 + 203 mil, cada uma abriu 4 Médias novas ("catraca") | **Mudar** → regra de congelamento (Fase 1) |
**Régua adotada para decidir:** manter um mecanismo se economiza ≥ 25% por rodada sem perder achado; reavaliar na próxima Spec CRITICAL. Limite da medição: n = 1 delta (v1.11) e 2 integrais; confirmar com o banco de defeitos plantados antes de tornar a régua norma.

## Revisão 2026-10-18 (Andraus): 2 agentes + modelo validado pelo hook; esforço só após piloto
Substitui "4 agentes" nas Fases 1/2 acima. Menos arquivos protegidos tocados (apenas ata do roteador, script e selo), mesmo custo de contexto por chamada.
