# Propostas de melhoria — retrospectiva da SPEC-008 (2026-11-15)

> **PROPOSTAS, NÃO NORMATIVAS.** Redigidas por pedido de Andraus (AskUserQuestion 2026-11-15, `DHR-AVALIACAO-002`). **Nada é aplicado:** cada uma só vira mecanismo por ordem expressa dele, com `governance/MECANISMOS.json` no mesmo PR (COE-14) e, se tocar arquivo selado, ata completa. Formato (RETROSPECTIVAS.md, roteiro item 6): problema → evidência → proposta → 4Es → custo. Dados: `governance/aprendizado/AVALIACOES/AVALIACAO-SPEC-008.md`, pareceres R1–R3 do Plan, `CAUSAS-PREVENCAO.md`, telemetria pelo transcript (`DHR-TELEMETRIA-002`).

## P13 — Conferidor fato→locais (BP-04; estende a P7 aprovada em `DHR-RETRO-002`)
- **Problema:** o mesmo fato escrito em N lugares é corrigido em um e esquecido nos outros (C01).
- **Evidência:** C01 = 41 achados em 23 rodadas no ledger (recorrente desde a SPEC-007); no Plan da SPEC-008, R1-m06, R2-m02 e R3-m01/m02/m03 são o mesmo defeito (cenário × algoritmo; EARS/BASpec sem a cláusula de uma RULE nova).
- **Proposta:** `scripts/fato_locais.py` (Detector informativo): dado um ID de RULE/código `MDC_*`/evento, lista todos os blocos do Plan que o citam (RULE, EARS, BASpec, cenário, ADV, D5, checks) e destaca quem **não** cita uma alínea nova; roda no `pre_entrega`. Sem julgamento semântico.
- **4Es:** Conformidade ↑, Eficiência ↑. **Custo:** pequeno (Grep estruturado; reaproveita a tabela do `HISTORICO`); risco de falso positivo moderado (informativo).

## P14 — Citação por identificador e histórico gerado do diff (BP-05 e BP-06)
- **Problema:** número de linha deriva a cada edição (C07); histórico `[antes]` copiado à mão infla o plan e falha (C06 sem prevenção registrada).
- **Evidência:** C07 = 49 achados; C06 = 25 achados e prevenção **AUSENTE**; no Plan, o R2-m10 achou o `HISTORICO.md` incompleto e a recuperação precisou do `git diff` (`DIFF-PLAN-V1.0-ATUAL-2026-11-14.patch`).
- **Proposta:** (a) `check_refs` aceitar âncora `ID+hash curto` (ex.: `RULE-MDC-005#a1f3`) e avisar citação por linha em Plan novo; (b) `scripts/historico_do_diff.py`: gera a tabela "texto anterior" do `HISTORICO.md` a partir do diff git entre duas versões (o agente não escreve o histórico à mão; o Orquestrador roda).
- **4Es:** Conformidade ↑, Eficiência ↑↑ (o Especificador gastou 8,7 M de tokens novos incluindo reconstrução manual de histórico — parte atribuível). **Custo:** médio; (b) é determinístico e testável por mutante.

## P15 — Revisão só do delta, em entregas menores (BP-03)
- **Problema:** correção grande vira revisão integral (>50% dos blocos alterados).
- **Evidência:** R2 do Plan foi integral (82 de 126 blocos alterados; 276 mil tokens novos) enquanto a R3 por delta (38 de 127) custou 296 mil mas só porque o Revisor leu inteiros os blocos dependentes — o delta só vale se a entrega for pequena.
- **Proposta:** quando o `delta_pacote` indicar > 50% alterado, o Orquestrador devolve ao Especificador para dividir a correção em duas entregas (Médias primeiro; Menores depois) e commitar cada uma antes do pedido ao Revisor; `SHA256-ALVO` + `DELTA` obrigatórios em **todo** Plan (hoje só no experimento P10, que está encerrado).
- **4Es:** Eficiência ↑, Eficácia neutra. **Custo:** baixo (regra no pedido + hook existente `experimentos-ativos` como veículo).

## P16 — Máquina de estados em tabela verificada por script (BP-07)
- **Problema:** transição sem linha, falha sem estado, guarda inalcançável (C10); a simulação da D4.2 foi feita à mão e falhou 3 rodadas seguidas.
- **Evidência:** C10 = 14 achados; Plan: R1-M-01, R1-M-02, R2-M-02, R3-m04, R3-m05; "simular a D4.2 passo a passo" aparece como prevenção em R1-m06, R2-m02 e R3-m01.
- **Proposta:** `scripts/fsm_check.py`: lê a tabela D5 (estado × evento → estado, guarda) e o conjunto de cenários T/ADV e verifica (i) todo (estado, evento) citado por cenário/ADV tem linha D5; (ii) todo código de passo esperado por cenário é alcançável na ordem da D4.2; (iii) todo efeito com falha possível tem linha de falha. Requer uma convenção de tabela legível por máquina (BL-045).
- **4Es:** Eficácia ↑↑ (é onde estavam as Médias). **Custo:** alto (convenção + script + mutantes); maior retorno entre as propostas.

## P17 — Detectores para categorias sem prevenção (BP-08)
- **Problema:** C06 (contagem/histórico) e C03 (pré-condição de teste) sem prevenção; e o detector `contagens_declaradas` do gate deu **2 falsos positivos** no Plan ("~6 EC" = estimativa da abertura; "§10.3 EC" = número de seção), corrigidos só na redação.
- **Proposta:** (a) C06 → cobre-se por P14(b); (b) C03 → detector "todo cenário cita fixture/pré-condição declarada"; (c) afinar `contagens_declaradas` para ignorar aproximações (`~N`, "estimativa") e números de seção — **arquivo selado** (`revisor_detectores.py`): exigiria ata completa e selo regravado.
- **4Es:** Efetividade ↑. **Custo:** médio; (c) é pequeno mas selado.

## P18 — Pré-entrega legível por máquina (BP-12; liga BL-044/BL-045)
- **Problema:** o gate estrutural (14/14, PASSOU_D) passou na v1.0 que tinha 5 Médias semânticas.
- **Evidência:** Plan R1: 5 Médias (C10 ×2, C05, C04, C02), nenhuma pega por `validate_spec_sot`/`revisor_gate`.
- **Proposta:** `pre_entrega.py` passar a rodar P13/P16 (quando existirem) e uma checklist D/H legível por máquina (BL-046/A9); o Especificador cita a checklist por ID em vez de reescrever invariantes.
- **4Es:** Eficácia ↑, Eficiência ↑ (menos rodada de Média). **Custo:** depende de P13/P16 (dependência, não independente).

## Já em vigor (sem proposta nova)
- **BP-10 custo por rodada:** `TOKENS:` no parecer via `telemetria_tokens.py tokens <agent_id>` (procedimento do Orquestrador, `DHR-TELEMETRIA-002`).
- **Experimentos por código e teto 3:** `DHR-PROCESSO-EXPERIMENTOS-001`.

## Ordem sugerida (do Orquestrador, `[INFERÊNCIA]`; decisão de Andraus)
P16 (maior retorno, maior custo) e P14(b) (determinístico, barato, evita reconstrução manual) primeiro; P13 e P15 depois; P17(c) só com ata completa; P18 por último, depende das anteriores.

## Status de aplicação (2026-11-17, `DHR-RETRO-004`)
Aplicadas por ordem de Andraus (AskUserQuestion 2026-11-17): P13, P14(a)(b), P15, P16, P17(b)(c), P18 — ver a ata para arquivo, teste e limites. Pendente de decisão à parte: integrar a âncora `ID#hhhh` ao `check_refs.py` (selado) e a checklist D/H legível por máquina (BL-046/A9).
