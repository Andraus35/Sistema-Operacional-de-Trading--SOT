# Parecer do Revisor — Proposta de Abertura da SPEC-008 (Manager — Orquestração Mecânica, Fase 1) — R1 integral (S3, opus) — 2026-11-07

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura; resumo fiel — as seções 1–5 foram condensadas). Alvo: `specs/features/SPEC-008/ABERTURA.md` (+ `research.md`, `sources/`).
> MODO: integral
> SHA256-ALVO: ad973a83ffc9f3990855679f0428629951ddceca8ac02cedf6de5fc99831431a (valor recebido do Orquestrador; o Revisor não recalculou)
> **Veredito: NÃO CONFORME** — 0 Críticas, 5 Médias (R1-M01..M05), 7 Menores (R1-m01..m07). Teto, mesmo corrigido: CONFORME condicional (GATE NÃO VERIFICADO — ferramenta MCP não carregada e sem linha `GATE-D:`; pendência J-001/N-001 para o valor do limiar macro).

## 1. Síntese
- Processo do Dossiê quase todo certo: estrutura, captura literal (14 SRC conferidas letra a letra), repositórios (transitions NÃO ELEGÍVEL, 424 dias, coerente), três lentes, validade (2027-02-05) e conta de tamanho (2.547 / 1.895 / 1.439 refeitas e conferem).
- Invariantes, 4Es, pisos de enforcement e decisões abertas (J-001, N-001, G-001, M-001, C-001, K-001, WF-D03…): PASS; nenhuma decisão aberta fechada.
- Os Médios estão na fronteira de dono e no re-apontamento.

## 2. Achados Médios
- **R1-M01 — Fibonacci/Fractal (SPEC-011) ausentes do despacho.** S2 promete "ordem = hierarquia", mas o grafo só despacha Estrutural, Institucional e Operacional. Declarar se o Fibonacci Validator é nó despachado (condição) ou chamado dentro do Estrutural; registrar a lacuna WORKFLOW×hierarquia e perguntar a Andraus.
- **R1-M02 — Re-apontamento da SPEC-003 incompleto.** Só l.46 e l.224; há também l.98, l.191, l.1149, l.33 (histórico), `research.md` e `checks.md`. Dar lista completa ou propor regra de busca na ata (padrão Q-7 da SPEC-048).
- **R1-M03 — WF-K02 nomeia SPEC-008/015 como dona da Killzone** (WORKFLOW l.38); a divisão move abrir/fechar para a Spec de Tempo sem registrar a divergência. Registrar como conflito a Andraus (estilo C-1), incluir em §12 e listar a MATRIZ-WORKFLOW-SPEC.
- **R1-M04 — Dono da FSM do ciclo após `EM_SÍNTESE` não declarado.** S7/C-1 dão a FSM WF-F02 inteira à SPEC-008, mas a fronteira com a SPEC-014 corta em `EM_SÍNTESE`. Declarar dono por transição e interface; C-1 deve ter três lados (EUA-E23 PROPOSTA l.115 lista WF-F02 sob a SPEC-014).
- **R1-M05 — "Reset do alarme" (WF-F01 ramos 3 e 5) não cabe na FSM fechada WF-A02.** Registrar como ambiguidade do WORKFLOW a decidir por Andraus (ex.: reset = alarme encerrado + novo alarme ligado à mesma hipótese-origem); sem estado novo.

## 3. Achados Menores
R1-m01 referência C-3→C-4 (mecânico) · R1-m02 IDs C-n homônimos em dois arquivos · R1-m03 prefixos de "SPEC-050" (mecânico) · R1-m04 faixa de tamanho vs. alerta de 1.900 e ajuste de errata; P-3 deve avisar do teto 2.000 · R1-m05 gatilho da Inversão #1 sem evento publicado · R1-m06 nota [INFERÊNCIA] do CONFLICT-MAP promovida a fato normativo · R1-m07 visibilidade: BL-003 (ATIVADO) e Specs 006/007/048 fornecedoras de interface.

## 4. Encaminhamento
Médios e Menores m02, m04, m05, m06, m07 → Especificador (classe O). m01 e m03 → FICHA-M (Orquestrador). Próxima rodada: trazer linha `GATE-D:` com o mesmo SHA256-ALVO. Este parecer não homologa nada; a homologação é só de Andraus.

<!-- ACHADOS-ESTRUTURADOS
R1-M01|MEDIA|C08|Escopo do despacho derivado só do pipeline WF, sem conferir a hierarquia INV-01 inteira (Fibonacci/Fractal, SPEC-011)|Ao afirmar "ordem = hierarquia", mapear cada nível de INV-01 a um nó do grafo ou justificar a ausência
R1-M02|MEDIA|C07|Lista de re-apontamento feita por amostra (l.46/l.224), não por varredura completa da Spec baselined|Grep exaustivo do slot na Spec baselined (plan/research/checks) antes de declarar linhas; ou propor regra de busca
R1-M03|MEDIA|C04|A divisão mudou o dono de capacidade que o WORKFLOW nomeia por número de Spec (WF-K02), e a lente 3 não foi refeita após a divisão|Após propor divisão, refazer a lente 3 procurando "SPEC-<slot>" no WORKFLOW e na MATRIZ
R1-M04|MEDIA|C10|FSM do ciclo atribuída inteira à SPEC-008 enquanto a fronteira com a SPEC-014 corta no meio dela|Para FSM que cruza fronteira de Spec, declarar o dono por transição e a interface de evento
R1-M05|MEDIA|C10|"Reset" de WF-F01 usado sem conferir contra a FSM fechada WF-A02|Toda ação sobre a FSM deve mapear para uma transição listada; se não houver, registrar como pergunta
R1-m01|MENOR|C07|Referência cruzada a ID errado (C-3 em vez de C-4)|Conferir referências internas a IDs após renumerar listas
R1-m02|MENOR|C02|Mesma série de IDs (C-n) usada com sentidos diferentes em dois arquivos|Prefixos distintos por tipo de item
R1-m03|MENOR|C07|Busca de número livre resumida com omissão de prefixos existentes|Relatar todos os prefixos encontrados na busca
R1-m04|MENOR|C06|Faixa da estimativa comparada ao alerta só pelo valor central; ajuste de errata aplicado de forma inconsistente|Comparar faixa e central com o alerta e o teto; ajuste de errata coerente com onde a errata cai
R1-m05|MENOR|C05|Obrigação herdada (Inversão #1) sem fonte de evento observável para o despachante mecânico|Para todo gatilho herdado, declarar o evento publicado que o dispara
R1-m06|MENOR|C04|Nota [INFERÊNCIA] do CONFLICT-MAP promovida a FATO NORMATIVO junto com a linha homologada|Etiquetar cada trecho citado pela etiqueta da sua fonte
R1-m07|MENOR|C04|Lista de visibilidade de backlog e de montante não varreu itens ATIVADO nem Specs fornecedoras de interface|Varrer ATIVADO e Specs que citam o slot ao montar §9/§10
-->

<!-- FICHA-M {"achados":[{"id":"R1-m01","sev":"MENOR","arquivo":"specs/features/SPEC-008/research.md","antigo":"§9.3 registrada (§6, C-3).","novo":"§9.3 registrada (§6, C-4).","condicao":"research.md §0(g) remete a C-4 da tabela §6 (linha 'C-4 | CEE-001 §9.3 ... §10 S2')"},{"id":"R1-m03","sev":"MENOR","arquivo":"specs/features/SPEC-008/ABERTURA.md","antigo":"e \"COG-SPEC-050\" é outro espaço de nomes, do MC-COG-001)","novo":"e \"COG-SPEC-050\" (MC-COG-001) e \"GOV-/EXP-/SKL-/LRN-SPEC-050\" (reference/camadas) são outros espaços de nomes, todos com prefixo)","condicao":"Grep 'SPEC-050' fora de SPEC-008 e tests/ só retorna ocorrências prefixadas (COG/GOV/EXP/SKL/LRN-)"}]} -->
