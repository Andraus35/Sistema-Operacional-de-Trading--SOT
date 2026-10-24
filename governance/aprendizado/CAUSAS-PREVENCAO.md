# CAUSAS E PREVENÇÃO DOS ACHADOS RECORRENTES (LOOP-001 / DHR-LOOP-001)

> Registro **manual e append-only** do Orquestrador (INV-07: nada se apaga; correção = nova linha datada). Lido por `python scripts/loop_ledger.py`: toda categoria **recorrente** (≥2 rodadas ou ≥2 linhas de trabalho) sem linha aqui, ou com prevenção `AUSENTE`, aparece como **LACUNA DE PREVENÇÃO** no `LEDGER-ACHADOS.md`. Propostas de gate/processo daqui só viram mecanismo por **ordem expressa de Andraus** (relatório de origem: `governance/propostas/MELHORIAS-PROCESSO/RELATORIO-MELHORIAS-AGENTES-E-GATES-2026-10-24.md`). Hierarquia dos 4Es: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade.

Colunas: **Cod** | Categoria | Causa-raiz (hipótese do Orquestrador, a validar) | **Prevenção atual** (`AUSENTE` se nenhuma) | Gate/processo candidato (proposta, não vigente) | 4Es afetados | Registrado em

| Cod | Categoria | Causa-raiz | Prevenção atual | Gate/processo candidato | 4Es | Registrado em |
|---|---|---|---|---|---|---|
| C01 | contradicao_interna | O mesmo fato é escrito em 5-7 lugares (RULE, BASpec, EC, EARS, D5, cenário, contrato); a correção acerta um e deixa os outros | AUSENTE | G-B fechamento de códigos de erro; G-C matriz de rastreio; G-D varredura de impacto | Eficácia, Eficiência | 2026-10-24 |
| C02 | ambiguidade_vocabulario | Nomes homônimos entre Specs (campos e rótulos) sem registro de acepção obrigatório por campo novo | Parcial: RULE-SEM-01 / CC-10 (Revisor confere à mão) | G-C estendido: campo novo exige linha de acepção; busca de homônimo nos baselines | Efetividade | 2026-10-24 |
| C03 | precondicao_teste | Cenário positivo depende de estado injetado (fixture) que o Especificador esquece de declarar | AUSENTE | G-C: todo ADV/cenário cita fixture existente | Eficácia | 2026-10-24 |
| C04 | heranca_rastreabilidade | Obrigação herdada some quando o comportamento muda de Spec (divisão) sem tabela obrigação a obrigação | Parcial: RULE-HD-01..04 e Bloco B (Revisor confere à mão) | G-C + G-D: toda obrigação herdada tem destino; impact_sweep por ID | Conformidade | 2026-10-24 |
| C05 | observabilidade_enforcement | Guarda/E3 especificada sem campo de registro que prove a execução (não representável) | Parcial: ENF-01..08 e Passo 7 (Revisor) | G-B/G-C: EVIDENCE de cada EC cita campos que existem no contrato | Eficácia | 2026-10-24 |
| C06 | contagem_historico_anexo | Histórico (INV-07) copiado à mão dentro do plan.md, infla o arquivo e dispara detectores de contagem/citação | AUSENTE | Histórico em `HISTORICO.md` + G-G fidelidade de anexo + G-I regiões históricas | Eficiência, Economicidade | 2026-10-24 |
| C07 | citacao_ancora | Âncora por número de linha deriva a cada edição | Parcial: `check_refs.py` (arquivos/IDs), não linhas | G-H âncora por ID+hash | Eficiência | 2026-10-24 |
| C08 | decisao_aberta_escopo | Especificador amplia escopo e abre decisões novas; risco de fechar de fato decisão aberta | Parcial: CONS-01, `check_doc_sync.py`, Revisor | Régua de escopo na ordem de serviço do Especificador | Conformidade | 2026-10-24 |
| C09 | seguranca_guarda | Efeito externo irreversível (envio, reenvio, publicação) por caminho não coberto pela guarda | Parcial: pisos E3, ADV D8, Revisor | Lista de caminhos de efeito por Spec (INV de alcance) + ADV por caminho | Conformidade | 2026-10-24 |
| C10 | estado_maquina | Tabela de estados em prosa, contradição só vista por leitura | AUSENTE | G-F máquina de estados em tabela verificável | Eficácia | 2026-10-24 |
| C99 | outros | Classificação heurística não casou; revisar manualmente e, se recorrente, propor categoria nova | AUSENTE | Revisar taxonomia | Efetividade | 2026-10-24 |
