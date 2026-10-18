# Parecer do Revisor SOT — SPEC-006 Plan v1.4 (rodada 5) — 2026-10-17

> **Guarda pós-Revisor (DHR-AUDITOR-EXTERNO-018):** o hook do subagente não é honrado em nuvem; o Orquestrador rodou `python scripts/revisor_gate.py specs/features/SPEC-006/plan.md` sobre o commit `88eb5c6` **antes** do parecer e o entregou ao Revisor (que o citou na seção 3): `VEREDITO D: PASSOU_D`, sinais H: 0, `validate_spec_sot` PASS 12/12; 3 verificações informativas apontam para OUTROS arquivos (GEN-1/BL-011), fora do escopo. Reconferido na reaplicação da guarda (mesmo resultado). Nenhum achado do parecer vem do gate (todos são de Classe P/semânticos): nada a confirmar ou descartar.

> **Não-normativo; não é baseline.** Registro do parecer do Revisor SOT (somente leitura) sobre `plan.md` v1.4 (1652 linhas) e `checks.md` (194 linhas), commit `88eb5c6`. Resumo fiel para continuidade entre sessões; o texto integral foi entregue ao Orquestrador. Gate de código informado pelo Orquestrador: `VEREDITO D: PASSOU_D` (≠ CONFORME ≠ homologação); o Revisor não teve a ferramenta `revisor_gate` nesta sessão (registrado como "gate não verificado por mim").

## Veredito: NÃO CONFORME — 2 Críticas · 10 Médias (M1–M10) · 8 Menores (m1–m8) · 1 pendência de gate (G)
Não é CONFORME condicional: o bloqueio vem de defeitos do Plan, não de decisão aberta. Conferiram: contagens (13 BASpecs · 6 EC · 13 EARS · 19 cenários · 22 adversariais · 2 invariantes · 5 EC em E3), V1/V2(a)/V3/V4/R1/R2/R3/R5/R6 internos, enums por baseline (CHM l.329, CEM l.258-262, CCM l.58), invariantes (ICT não cria hipótese, custo fora da convicção, sem execução de ordem), nenhuma decisão aberta fechada, sem autodeclaração de homologação.

## Críticas
- **C1** — "preservar TODAS as versões" (CEM-001 l.612) está em INHERITS (plan l.85-86), mas o Bloco B (l.1523-1538) não tem evidência; não há aresta/campo que ligue versões do mesmo canônico nem `successor_ref` no payload de `canonical_state_transition` (l.1334-1340). Ação: mecanismo + teste, ou PARCIAL/[DECISÃO NECESSÁRIA].
- **C2** — CEE-001 l.111 ("entra no KG como métrica de calibração") declarada satisfeita por ADV-05 (isolamento, não armazenamento), enquanto RULE-CKG-010 (l.406-407) nega o caminho de entrada de `calibration_metric` (`ENTRY_PATH_UNDEFINED`). Ação: PARCIAL/[DECISÃO NECESSÁRIA]; corrigir ADV-05 e Bloco B.

## Médias
- **M1** o padrão eliminado em (a) persiste em (b) (selo SPEC-007 indefinido → gate vacuoso, l.815-816, 1361, 1514-1516) e na allowlist (mantenedor indefinido, l.391, 1385): tratar como (a) — pendência = DENY.
- **M2** caminho de entrada indefinido para **relações** (SAS-001 l.924) e para `structure`/`narrative`/`mission`/`learning`; T11/ADV-02/ADV-18 dependem de REFUTA que não chega ao passo 7.
- **M3** `ENTRY_PATH_UNDEFINED` e `SCHOOL_UNDERIVABLE` sem EARS/cenário negativo; hoje toda hipótese SMC/Fibonacci cai em `SCHOOL_UNDERIVABLE` (só Elliott tem `producer_id` conhecido, SPEC-001 l.203).
- **M4** colisão INVALIDA × relação-alvo (§D2.2 linha 2, l.511) não executa: escopo exige mesmo (from,to) (l.505/907) e INVALIDA mira relação via `target_relation_id` (l.471).
- **M5** escopo do gate CKG-008 diverge: RULE/EC dizem "toda relação CAUSA"; BASpec/EARS 8/D6.6 dizem "proposta por juízo".
- **M6** bounded loop: memoização/registro de resultados sem schema nem store, sem invalidação; ADV-20 "variando a redação" é tautológico.
- **M7** "lote" (e fim de `PENDING_ANCESTOR`) sem definição; mecanismo inalcançável hoje (evidence DERIVED só entra por (a)).
- **M8** divergências de envelope e `gate_record`: `envelope_completo` (D4 l.899) não exige `valid_from`/`valid_to`/`publication`; EC-002/003 exigem `gate_record` de gate do próprio KG vs T12; checks.md §7 ("proveniência condicional idêntica", "um só formato") falsas como escritas.
- **M9** guard de CKG-007/EC-004 ("origem com propriedade de custo/confiança") sem campo no schema — não determinístico como declarado (CC-11).
- **M10** função de projeção de estado subespecificada: sem precedência SUPERSEDED/INVALIDATED_IN_TIME/ARCHIVED; `version`/`supersedes` de `invalidation`/`archival`/`canonical_state_transition` indefinidos.

## Menores
m1 citação CONSTITUTION l.191 não sustenta "evidence, não observation" · m2 T01 não é o cenário da VERIFICAÇÃO da CKG-001; nomes de verificação variam · m3 envelope sem digest/hash (mutação in-place não detectada) · m4 sem gate de `valid_to < valid_from` · m5 gates de presença aceitam qualquer token (limite não dito) · m6 `canonical_state_transition` sem checar legalidade (CEM l.460-475; CHM l.767-769) · m7 cobertura CKG-010→ADV-08 não nega o QUANDO · m8 volume 1428→1652 linhas vs Q-ABERTURA-5 (voltar a Andraus se grande demais).

## G — pendência de gate (não é defeito do autor)
O Plan diz satisfazer o ramo `spec:SPEC-006` de BL-003 e BL-011 (l.43-44), mas ambos seguem `Em espera` (RMR-001 l.102/110). `backlog_triggers.py` confirma: **"DISPARADOS SEM REGISTRO (2): BL-003, BL-011"** — promoção a `ATIVADO` é de Andraus (RMR-001 §5). Também decide Andraus se o Plan que adia COL-EXP-05 e R-04..R-06 "à ativação" (CLASSIFICACAO l.62) é a própria ativação.

## Interpelações ao Especificador (responder com âncora arquivo:linha)
1) mecanismo/teste de "preservar TODAS as versões" · 2) verificador que torne (b) não vacuoso sem o selo · 3) caminho de entrada de relações de agente e de REFUTA em T11, e dos node_types sem caminho · 4) definição, dono e fechamento de "lote" · 5) onde persiste/invalida o resultado do bounded loop; por que ADV-20 é satisfeito pelo KG · 6) semântica de INVALIDA × `invalidation`; como §D2.2 linha 2 satisfaz o escopo de D4 · 7) campos que tornam "custo/confiança" determinístico · 8) o gate do KG gera `gate_record` em toda escrita ou não (EC-002/003 × T12)?

## Não provado
Escrita positiva fim a fim no KG; trace completo sobre dados efetivamente admitidos (T10 usa fixture); veracidade das fontes web (sem web); integridade física/mutação in-place (m3).
