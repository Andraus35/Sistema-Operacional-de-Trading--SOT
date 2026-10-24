# Parecer do Revisor — Plan reduzido da SPEC-007 v2.0 (CANDIDATA), rodada 4 (S3) — 2026-10-24

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). **Veredito: NÃO CONFORME** — 0 Críticas, 2 Médias (R4-M1, R4-M2), 11 Menores (r4-n1..r4-n11). Não é homologação; nenhuma decisão aberta fechada (CONS-01). Teto após corrigir as Médias: CONFORME condicional (gate não executado pelo Revisor; casos positivos dependem da Fixture F0, ou seja, de P-10/BUILD, dos atos de Andraus e de SPEC-007-LOCUS-001). Base do delta: commit 54fa53a (v1.2); 81 alterados/40 adicionados/38 removidos/39 inalterados; revisão integral do corpo vigente (l.1–1743) e checks.md; Anexos T/R/H por amostra.

## R3 corrigidas
R3-M1 (Fixture F0, l.1132-1138), R3-M2 (serialização única l.471-488, materialização pelo pipeline l.562-568, ADV-30), R3-M3 (quadro l.339-353, Roteamento l.1581), R3-M5 (CIM por `content_ref`, D4.5, ADV-32) corrigidas; R3-M4 corrigida na forma (ver R4-M1). r3-n1..n5 corrigidas; r3-n6 transferida à SPEC-048.

## Divisão e incorporação
Coerente sozinha; nenhum ID transferido reutilizado nem vigente; Interface com a SPEC-048 declarada (l.1063-1075); obrigações herdadas aparecem na nota l.243/Bloco B (não é supressão RULE-HD-03). P-10, P-4a, P-4b, P-11, P-1, P-2, P-3, P-8, P-5, P-6, P-9 conferem com DHR-SPEC007-003. SPEC-007-LOCUS-001 (P-12), P-13, P-14 bem formadas. Contagens 12 RULE/2 INV/12 BASpec/12 EARS/9 EC/18 cenários/22 ADV conferem.

## Médias
- **R4-M1** O rótulo de impacto não chega ao juiz F1 pelo envelope da CIM: o eixo `KIND_MISCLASSIFIED` (RULE-KFH-006 l.494-497) julga `knowledge_kind`, mas RULE-KFH-019 (f1)-(f3) só aceita `semantic_unit_ref`, `claim_ref@candidate_version`, `published_ref@version`; F0.3 obriga executor EXTERNO; T25 chama o juiz sem o rótulo. ENTÃO de ADV-31(a) inalcançável; `h_result` (contrato l.1095) indefinido; RU-4 subestimado. Ação (uma de três): tipo `candidate_ref@version` (afirmações + `knowledge_kind` + `target_node_type`, permissão = conjunção das origens-raiz); ou `claim_ref` resolve o rótulo; ou enum fechado como parâmetro do template. Ajustar D4.5, T25, ADV-31(a), contrato.
- **R4-M2** "Vale também para o pode usar" (P-4a/P-11) não é aplicado a executor LOCAL: D4.5 (4) l.1025, GATE DE SAÍDA da BASpec-KFH-019 l.976-977 e EC-KFH-011 l.1506-1507 só checam `rights_status` efetivo para EXTERNO; ADV-32(d) l.1374 aceita texto livre para LOCAL sem ato RIGHTS. Latente (LOCUS-001 fail-closed), abre se Andraus aprovar P-12. Ação: exigir `rights_status` efetivo ≠ INDETERMINADO para qualquer executor; decidir texto livre para LOCAL (proibir, ou aceitar com risco residual declarado); corrigir ADV-32(d) e acrescentar negativo LOCAL sem ato RIGHTS.

## Menores
r4-n1 `seal_request` sem campo de lista de registros (l.514-517) × RULE-KFH-007 (ii)/ADV-21(d)/D4.3(c). · r4-n2 ordem do gate: EARS 7/EC-004 "(i)-(vii-bis)" × ordem do D4.2 ((5-bis) antes de (6)); tabela de correspondência. · r4-n3 afirmação a1 da F0 ("índice calculado sobre o fechamento diário") é definição rotulada `fato_de_fonte` (encarna RU-4): trocar por fato inequívoco. · r4-n4 `succession_of?` só admite um valor; dois registros colidindo não representável. · r4-n5 função M não leva `formed_inference` ao registro publicado (RULE-EPI-01). · r4-n6 rótulos "I-1..I-6" colidem com I-xx (CONFLICT-MAP l.9, K-MAN-02): renomear. · r4-n7 texto da errata E-1 (l.1558) × A-bis (l.326): precisar o que a P-1 decidiu da l.482. · r4-n8 "só Andraus" para INVALIDATION é extensão da P-8/P-10: etiquetar [PROPOSTA] ou perguntar. · r4-n9 ADV-28(a') existe (l.1365) mas tabela de mapeamento (l.74) e BASpec-KFH-019 citam só (c)(d). · r4-n10 chamada fora da CIM não deixa rastro; meio de detecção a declarar (pode ficar para BUILD). · r4-n11 ordem de Andraus para o Plan reduzido só citada como chat (l.7); registrar na ata.

## Não verificável
Fidelidade dos Anexos T e R ao commit 54fa53a palavra por palavra (sem git); 7 citações `inteligencia-sot@0abd22e` (clone ausente); veracidade das fontes web; gates do Orquestrador; sha256.

## Encaminhamento
Devolver ao Especificador: R4-M1, R4-M2 (+ Menores na mesma passada). Rodada 5 por delta: RULE-KFH-006/007/019, D4.2, D4.3, D4.5, F0, T25, ADV-21/28/31/32, BASpec-019, EC-004, EC-011, errata E-1, tabelas de Incorporação e Interface, checks.md.
