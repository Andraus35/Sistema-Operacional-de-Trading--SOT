# Parecer do Revisor SOT — SPEC-006 Plan v1.5 (rodada 6) — 2026-10-17

> **Não-normativo; não é baseline.** Resumo fiel do parecer do Revisor SOT (somente leitura) sobre `plan.md` v1.5 (1641 linhas) e `checks.md` (209 linhas), ramo `spec006-plan` @ `24c1ab9`. Gate de código (rodado pelo Orquestrador antes do parecer, repetido na guarda pós-Revisor): `VEREDITO D: PASSOU_D`, sinais H: 0, validate_spec_sot 12/12, lint 22 ok; aviso `estado_backlog` (plan:1585) **procedente**, ver N1. O Revisor não teve a ferramenta `revisor_gate` (gate "não verificado por mim").

## Veredito: NÃO CONFORME — 0 Críticas · 11 Médias (N1–N11) · 9 Menores (n1–n9). O bloqueio vem de defeitos do Plan, não de decisão aberta.
Rodada 5 → 6: **fechados** C2, M1, M3, M4, M5, M7, M10; **parcialmente** C1 (→N6), M2 (→N5/n4), M6 (→n9), M8 (→N2/N4), M9 (→N8). Contagens conferem (13 BASpec · 20 cenários · 22 ADV · 6 EC · 15 EARS · 2 invariantes · 5 EC em E3). Honestidade confirmada: o Plan declara que hoje o KG não admite nenhuma escrita; nenhum caminho pendente é chamado verificável; nenhuma decisão aberta fechada; sem autodeclaração de homologação.

## Médias
- **N1** Plan e checks.md afirmam que a ata `DHR-BACKLOG-001` "não consta do checkout" e que BL-011 está "Em espera" (plan 43, 53, 1574, 1585, 1618; checks 127, 136, 171) — falso no estado atual (ata e RMR-001 l.102/110/191 existem, `ATIVADO`). O encaminhamento de R-01..R-07/X-04 ao gate da SPEC-006 é obrigatório (RMR-001 §4) e o Plan nunca nomeia o que são R-04..R-06. *(Origem: o Orquestrador mandou citar a ata antes de ela entrar na `main`; o Especificador registrou o que o checkout mostrava.)*
- **N2** condicionais de proveniência sem campo discriminante: nada distingue evidence DERIVED de PRIMARY nem "resulta de gate"; ADV-06/INV-CKG-02 não são determinísticos (D4:893; schema 1305-1323).
- **N3** `producer_id` (entrada de `school`) não existe no schema; o espelho de INV-02 é só de forma (D4:904; schema 1313-1323; CHM l.361).
- **N4** log `kg_gate_decision` (evidência dos EC E3) sem imutabilidade, sem EC próprio, `decision_id` não definido; T17 não resolve `gate_record`.
- **N5** colisão gravada (passo 7) antes da validação do envelope (passo 8): falha parcial deixa `collision` permanente com ref pendurada; sem regra de atomicidade multi-registro (SPEC-004 homologou publicação atômica).
- **N6** C1 (versões): `successor_ref` obrigatório estendido a CHM/CCM sem fonte (só CEM l.450); elos não precisam resolver; "obrigatório sse o canônico declara" depende de ler o objeto canônico.
- **N7** `posthoc_flag` opcional e "quando aplicável" autodeclarado: ADV-04 não é implementável (RULE-CAU-03).
- **N8** guard de INV-04 diverge: RULE/BASpec/EARS/D4 falam só de "confiança"; ADV-05/EC-004/schema falam "confiança/custo"; campos vedados não enumerados.
- **N9** `ANCESTOR_NOT_ADMITTED`, `VERSION_LINK_MISSING`, `CANONICAL_TRANSITION_ILLEGAL`, `VALIDITY_WINDOW_INVALID` sem EARS; regra de `version`/`supersedes` sem código nem negação.
- **N10** "preservar todos os estados/versões" de hipótese/convicção apresentado como herdado de CHM/CCM, mas só o CEM (Evidência) o diz; conflita com a [PROPOSTA] que exclui EMERGENT/CANDIDATE.
- **N11** `colide` usa `valid_to` bruto (sempre nulo na criação); janelas "disjuntas" só existem com `valid_to_efetivo` (D4:896/903; ADV-18b).

## Menores
n1 busca "transi" em CCM-001 (checks:86) imprecisa · n2 `estado(v,T)` para T<valid_from; sem monotonicidade de `recorded_at` · n3 destino "relation" fora do enum de `node_type` · n4 escritor dos registros internos (collision/invalidation/archival) indefinido · n5 checks:95 diz que BASpec-005 não repete a regra, mas repete · n6 "allowlist de fixture" de T16 só declarada para colisão/school · n7 EC-006: autorização de leitura e log de consulta sem regra · n8 `status_from≠corrente` trava a cadeia após uma transição perdida · n9 limite "≤1 invocação" vale por submissão; host do juízo indefinido.

## Volume (Q-ABERTURA-5) — decisão de Andraus
1641 linhas é o maior Plan do repositório (SPEC-004 1325 · 003 1200 · 005 1091 · 002 953 · 038 945). O Plan só cita a regra e delega. Causa observada: a mesma regra é copiada em RULE, BASpec, EARS, D4, D6, EC, schema e §7-bis — quase todos os achados da rodada 6 (N2, N3, N8, N11, n5) são divergências entre essas cópias. Remédio de menor custo antes de qualquer divisão: reduzir cópias a referências a D4.

## Interpelações (responder com arquivo:linha)
1) encaminhamento de R-01..R-07/X-04 (BL-011 ativado); o que são R-04..R-06? · 2) campo que distingue DERIVED/PRIMARY e "resulta de gate" · 3) onde o gate lê `producer_id` · 4) garantia de imutabilidade do `kg_gate_decision`; como T17 resolve `gate_record` · 5) o que impede `collision` persistido se o passo 8 reprova; regra de atomicidade · 6) fonte de `successor_ref` para CHM/CCM; os elos precisam resolver? · 7) o que torna ADV-04 e o guard de custo verificáveis sem enumerar campos · 8) volume: proposta de divisão ou justificativa.

## Não provado
Admissão positiva fim a fim (todo caminho DENY); persistência real/atomicidade; veracidade das fontes web; integridade física (sem digest, limite declarado); completude da cadeia de versões em runtime; determinismo dos condicionais de proveniência; execução do `revisor_gate` pelo Revisor.
