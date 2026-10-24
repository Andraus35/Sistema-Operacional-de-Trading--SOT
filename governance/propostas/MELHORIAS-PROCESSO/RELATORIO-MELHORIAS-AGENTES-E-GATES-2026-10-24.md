# Relatório — pontos fracos dos agentes construtores (Especificador e Revisor) e melhorias de gates

> **Não normativo. PROPOSTA.** Observações do Orquestrador na sessão de 2026-10-23/24 (SPEC-007 reduzida e SPEC-048), pedidas por Andraus no chat e salvas para a próxima sessão **abrir** as melhorias. Nada aqui altera gate, agente, `revisor.md`, `MECANISMOS.json` ou Spec; qualquer mudança exige **ordem expressa de Andraus** (AGENTS.md §10), e criar/mover/aposentar mecanismo exige atualizar `governance/MECANISMOS.json` no mesmo PR (COE-14).

## 1. Evidência da sessão (para medir se as melhorias funcionam)
- Plan da SPEC-007: 6 pareceres; Médias por rodada **9 → 5 → 5 → 2 → 1 → 0** (CONFORME condicional só na R6, após divisão da Spec). Abertura da SPEC-048: 2 rodadas (CONFORME condicional, 10 e 7 Menores). Plan da SPEC-048: R1 = 3 Médias/14 Menores; R2 = 1 Média/5 Menores; v1.2 em redação.
- Quase toda Média da rodada N+1 nasceu da correção da rodada N (cascata): R3-M4 → R4-M1 → R5-M1; M-03 → N-01.
- Falhas pegas só depois pelo Orquestrador: placeholder com formato de ID (`DHR-XYZ`) quebrando `check_refs`; contagens históricas de anexo quebrando o teste de calibração dos detectores (suíte só rodada tarde); cópia truncada do ADV-28 no Anexo R.12; tabela com `||`.
- Custo: o Plan da SPEC-007 chegou a mais de 3.400 linhas (anexos de texto anterior); 3 paradas por limite de uso e 1 compactação de contexto no Especificador; ~8 chamadas de Revisor recusadas ou refeitas pelo roteador de modelos (classe declarada ≠ derivada).

## 2. Pontos fracos do Especificador
1. **O mesmo fato escrito em 5-7 lugares** (RULE, BASpec, EC, EARS, estado D5, cenário, contrato): a correção acerta um lugar e deixa os outros. Causa-raiz das cascatas.
2. **Cada correção cria nova falha**; a convergência existe, mas é lenta.
3. **Sem Bash, não vê o próprio erro** (ver §1); dependia do Orquestrador para gates e suíte.
4. **"Texto anterior preservado" copiado à mão** (INV-07), sem prova de fidelidade; infla o plan.md e gera ruído em detectores.
5. **Pré-condições dos cenários positivos esquecidas** (estado injetado/fixture), recorrente em R3-M1, r5, N-01, m-09.
6. **Escopo que cresce** (decisões novas P-12, LOCUS-001; refinamentos de segurança de mecanismos sem construção).
7. **Perde estado** (limite de uso, compactação), reescrevendo de memória.
8. **Âncoras por número de linha** que derivam (várias Menores "linha desatualizada").

## 3. Pontos fracos do Revisor
1. **Teto permanente em "CONFORME condicional"** por não rodar o gate; a guarda pós-revisor (G1/G2/G3) exige reconferência e gera adendos quase sempre falso-positivo (contagens em texto histórico de anexo; caminhos abreviados).
2. **Não é delta de verdade**: sem `spec_delta`/sha256 e sem git, lê integral a cada rodada (só passei a commitar versões intermediárias no meio da sessão).
3. **Severidade sem régua escrita**: Média real (reenvio furando a trava E3) e Média cosmética ("idêntica" × "equivalente") custam a mesma rodada.
4. **Não verifica**: fidelidade dos anexos, fontes web, citações do Benchmark (clone ausente) nem o resultado dos gates (relato do Orquestrador).
5. **Reabre matéria já decidida em ata** em algumas Menores.
6. **Roteador de modelos**: classe declarada ≠ derivada (S2/S3) causou retries.

## 4. Gates propostos (novos ou reforçados)
| # | Gate | O que checa (determinístico) | Teria evitado |
|---|---|---|---|
| G-A | **Recibo de gate** | Hook roda a bateria completa (validate_spec_sot, revisor_gate completo, check_invariants/refs/doc_sync/coesao, check_repo_research, backlog_triggers, build_map --check, suíte unittest + npm test + lint) e grava arquivo-recibo com sha256 do plan.md + saídas; `revisor.md` aceita o recibo (hash confere) como "gate verificado" | Teto de CONFORME condicional por gate; adendos da guarda G1/G2/G3; suíte rodada tarde |
| G-B | **Fechamento de códigos de erro** | Todo código usado em regra/BASpec/EC/cenário/ADV existe no catálogo (§D3.1) com pai único, e todo código do catálogo é usado; um desfecho por condição | N-01, vários Menores |
| G-C | **Matriz de rastreio** | Toda RULE tem ≥1 EARS, BASpec, EC, cenário positivo e negativo; todo ADV cita fixture existente; toda BASpec Classe H tem laço e gate | R3-M1, R5-M1, m-09 |
| G-D | **Varredura de impacto** (`impact_sweep.py <id\|predicado>`) | Lista todas as ocorrências de um identificador/predicado; Especificador marca as tocadas; Revisor confere a lista | Cascata R3-M4→R4-M1→R5-M1 |
| G-E | **Conjunções etiquetadas** | Condição de saída com C1..Cn: RULE, BASpec e EC citam o mesmo conjunto | R5-M1, r6-n1 |
| G-F | **Máquina de estados em tabela** | D5 em formato legível por máquina: alcançabilidade, sem contradição, estados citados em testes existem | M-02, n-04 |
| G-G | **Fidelidade de anexo** | Compara cada bloco "texto anterior preservado" com o texto do commit anterior (`spec_delta --verify-preserved`) | R.12 truncado |
| G-H | **Âncora estável** | Referência por ID de regra + hash, não por número de linha; gate resolve a âncora | "linha desatualizada" |
| G-I | **Regiões históricas** | Marcação explícita (ex.: bloco `HIST`) que os detectores de contagem/citação ignoram | Falsos positivos de contagem e RULE-CKG-008 em anexo |

## 5. Mudanças de processo propostas
1. **Histórico fora do plano normativo**: texto anterior (INV-07) em `HISTORICO.md` ao lado, com hash conferido (G-G); o git garante a versão. O `plan.md` fica pequeno.
2. **Régua de severidade escrita** (em `revisor.md`/`atomic-spec.md`): Média só se mudar comportamento ou for contradição verificável; redação, rótulo e vocabulário = Menor, sem custar rodada.
3. **Parada por convergência**: após a 3ª rodada com ≤1 Média de natureza editorial, o Revisor emite o parecer e a decisão sobe a Andraus (aceitar condicional ou mandar corrigir).
4. **Commit de cada versão antes do Revisor** (delta real) e `spec_delta` entregue junto ao pedido.
5. **Especificador com gates de leitura**: se não puder rodar Bash, hook roda os gates quando ele devolve e reenvia a saída antes do Revisor.
6. **Notas de progresso** do Especificador em arquivo (scratchpad) a cada seção, para retomar após limite de uso/compactação sem reescrever de memória.
7. **Roteador**: documentar a regra de derivação da classe no prompt-modelo para o Orquestrador acertar S2/S3 de primeira.
8. **Hook de fim de turno** (`andraus-ask-guard`): hoje exige pergunta a cada entrega, mesmo sem decisão; avaliar agrupar entregas em lote para reduzir ruído.

## 6. Prioridade recomendada
1. G-A (recibo de gate) → 2. G-B + G-C (códigos e rastreio) → 3. G-D (varredura de impacto) → 4. histórico fora do plano + G-G + G-I. Em seguida a régua de severidade e a parada por convergência (mudança de `revisor.md`, ordem de Andraus).

## 7. Como abrir na próxima sessão (sugestão)
1. Andraus ordena a abertura da melhoria (qual lote: G-A..G-I e/ou processo §5).
2. Tratar como **mecanismo/gate novo**: Especificador redige a proposta (`governance/propostas/...`) com contrato de cada gate (entrada, saída, falsos positivos, testes), Revisor audita, Andraus homologa; atualizar `governance/MECANISMOS.json` no mesmo PR (COE-14) e `AGENTS.md` §8 só por ordem dele.
3. Medir com a evidência do §1: Médias por rodada, nº de rodadas por Plan, falhas pegas só pelo Orquestrador, retries do roteador.
4. Mudanças em `revisor.md`/`.claude/agents/*` e `AGENTS.md` seguem só por decisão expressa de Andraus.

## 8. Limites desta análise
Base: uma sessão (SPEC-007 reduzida e SPEC-048), sem medição formal de tokens por rodada; as correlações causa→efeito são do Orquestrador. Nenhum gate foi implementado ou testado.
