# Parecer do Revisor — rodada 9 — SPEC-006 plan v1.8 — 2026-10-18

> Registro condensado pelo Orquestrador a partir do retorno do Revisor SOT (texto integral não versionado). Dado de estado; não homologa. Linhas = `plan.md` v1.8.

**VEREDITO: NÃO CONFORME — 0 Críticas · 4 Médias (R9-1..R9-4) · 11 Menores (r9-a..r9-k).** Teto mesmo sem Médias: CONFORME condicional (H-001; ROADMAP:177 × Q-ABERTURA-3). Nenhuma Média exige decisão de Andraus. **R8-1..R8-4: todas SANADAS** (D4.0 l.653-663; D4.19 l.682-712; registros derivados l.665/678/681; `GATE_RECORD_UNRESOLVED` l.665). As 4 Médias novas vêm de elementos que a v1.8 introduziu.

Gate: `revisor_gate` PASSOU_D, sinais H = 0 (rodado pelo Orquestrador; o Revisor não tem a ferramenta em nuvem).

## Médias
- **R9-1** (D4.9 l.672, D4.10 l.673, D4.0 l.663, D4.13, EARS 24, T26): NO_OP do passo 8 (`SIMILAR_A` vigente) engole a submissão divergente antes do ramo "divergente" de D4.9 (passo 9); "mesmo payload" ignora `valid_to`/`provenance_ref` (fora do `payload`); "vigente" nunca é definido (ARCHIVED/SUPERSEDED). *Conferido pelo Orquestrador (l.672-673 e l.663).*
- **R9-2** (schema l.1110-1119, D4.5 l.668, EC-001/003 EVIDENCE): `kg_gate_decision` não guarda a identidade do solicitante, embora EC-003 prometa "identidade"; reexecução ENF-07 depende de estado/allowlist/`mapa_produtor` na época, e a alegação "executável a partir do log" só vale para DENY sem estado.
- **R9-3** (D4.1 l.664, D4.3 l.666, D4.19 l.696-697, T17 l.838): sem predicado/código para `from_node`/`to_node`/`target_relation_id` inexistente; integridade referencial reivindicada sem predicado.
- **R9-4** (D4.18 l.681, D4.13 l.676, T21 l.878-888): D4.4 é revalidada no commit, D4.9/D4.13 não; duas unidades concorrentes `CONFIRMA(A→B)`/`REFUTA(A→B)` comitam sem `collision`; sem serialização declarada nem reparo para par perdido.

## Menores (resumo)
r9-a "classe" com dois sentidos (operação × Classe D/C/H); BASpec-011 Classe D com comportamento constitutivo sem GATE DE SAÍDA · r9-b D4.0: "tentar gravar" sem predicado, operação desconhecida sem desfecho, leitura do log sem operação · r9-c assimetria `valid_to == valid_from` (invalidation × creation; EARS 19) · r9-d completude do log × exceções, sem mapa passo→`gate_id`, PASS de CKG-003 sem vínculo à aresta, ordem de `collision_pair`, typo "∧ —" · r9-e `input_snapshot` irrevogável sem limite/segredos/acesso (soma-se à pendência de volume do log) · r9-f D4.19 sem `node_type`; DADO do T16 incompleto · r9-g `mapa_produtor`/`school` sem versão por `schema_version` · r9-h faltam checks de `kg_record` indevido e PASS órfão (BASpec-010/009) · r9-i justificativa do EC-006 em E1 sem mecanismo · r9-j restatements de D4.0 fora de D4 (D6 l.738, BASpec-006 l.480, EARS 6, D4.15) · r9-k homonímia R-05/R-06 (BL-011 × BL-012).

## Pendências de Andraus (não decididas)
r8-l (R-04..R-06 CONFORME × ADIADOS) · volume/acesso do log (`input_snapshot`) · "ato de governança" (K-001 aberta) · H-001 e demais.

## Interpelações (11)
NO_OP × divergente e "vigente" · "mesmo payload" · identidade do solicitante no log · reexecução ENF-07 com estado de `decided_at` · extremidade inexistente · serialização/revalidação no commit e reparo de collision perdido · operação desconhecida / "tentar gravar" / leitura do log · assimetria `valid_to` · mapa passo→`gate_id` · versionamento do `mapa_produtor` · auditoria de `kg_record` indevido e PASS órfão.
