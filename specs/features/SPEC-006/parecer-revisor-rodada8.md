# Parecer do Revisor — rodada 8 — SPEC-006 plan v1.7 (núcleo, Opção 2) — 2026-10-18

> Registro condensado pelo Orquestrador a partir do retorno do Revisor SOT (texto integral não versionado). Dado de estado; não homologa. Citações = `plan.md` v1.7.

**VEREDITO: NÃO CONFORME — 0 Críticas · 4 Médias (R8-1..R8-4) · 13 Menores (r8-a..r8-m).** Teto mesmo sem Médias: CONFORME condicional (H-001 aberta; ROADMAP:177 × DHR-SPEC006-001 Q-ABERTURA-3; DHR-SPEC006-002 §2). Nenhuma Média exige decisão de Andraus. Gate determinístico não verificado pelo Revisor (MCP ausente); resultado vem do Orquestrador.

R7-3 e R7-4 **sanadas**; R7-1 e R7-2 **sanadas em parte** (resíduos = R8-4 e R8-2). Nenhuma alucinação de linha nas ~20 afirmações conferidas (CEM/CHM/CCM/SPEC-001/004/005).

## Médias
- **R8-1** (l.634, 637, 642, 667, ADV-07/14, EC-006): `RECORD_MUTATION_FORBIDDEN`, `QUERY_WRITE_FORBIDDEN`, `ONTOLOGY_CHANGE_NOT_GOVERNED` não têm posição em D4.0 (que ordena só submissão de `kg_record`); `ONTOLOGY_CHANGE_NOT_GOVERNED` inalcançável (allowlist indefinida; nada identifica "ato de governança"); ADV-07/14 sem `reason`; nenhum T01..T22 exercita os dois; EC-006 em E1 discutível e sem dizer se a negação vai ao log. *Conferido pelo Orquestrador (D4.0 l.634).*
- **R8-2** (l.26, 653-665, 976-986): CEM-001 l.428 (timestamp/origem/justificativa da transição) está só no schema (l.982), sem predicado em D4; idem `from_node`, `relation_type`, `reason`/`relevance` (invalidation/archival), `contradiction_pair`, `overlap_window`, `detected_at`. *Conferido (único hit de `transition_timestamp` = schema).*
- **R8-3** (l.649, 651, 652, 636, 941): `collision` e `DERIVA_DE` materializada (`kg_internal`) não têm caminho em D4.15 nem passam por D4.2; Bloco B superestima "Satisfeita no mecanismo" para o trace.
- **R8-4** (l.639, 636, 637, 781, 991): resolução do `gate_record` do collision é "DEVE" sem predicado/código/posição; T17 só positivo; PASS de CKG-013 não distingue "com colisão" de "sem colisão".

## Menores (resumo)
r8-a EARS não autocontidos (D4.15 prevalece) · r8-b `no-op`/ausência de log fora do enum e da D4.0 · r8-c 2ª `creation` divergente sem `supersedes`; `valid_to` ignorado por D4.6 · r8-d sem separação identidade de serviço × allowlist · r8-e log sem política de inundação/completude · r8-f ENF-07 não executável só com `input_digest` · r8-g `publication.origin` autodeclarado · r8-h restrição "ancestral do Lineage" sem negativo; afirmação "Garante…" forte · r8-i D4.12(ii) só barra `calibration_metric→conviction` · r8-j "school ≠ ICT" ambíguo; fixture T01; T17 sem timestamps · r8-k T21 artificial · r8-l R-04..R-06 "CONFORME" × CLASSIFICACAO l.62 "ADIADOS" (decisão de Andraus) · r8-m `FIELD_PRESENCE_VIOLATION` também em D4.16.

## Interpelações ao Especificador (11)
Posição em D4.0 dos 3 códigos de operação e "ato de governança"; negação de consulta no log × "zero registros" e E1 do EC-006; quem exige os 3 campos de CEM l.428; contrato de `collision`/`DERIVA_DE`; predicado/código do `gate_record`; separação de funções; reexecução ENF-07; teste negativo do Lineage; `supersedes` em 2ª creation; `valid_to` × S14; divergência CONFORME × ADIADOS de R-04..R-06.
