# Parecer do Revisor SOT — SPEC-006 errata v1.11 (rodada por delta) — 2026-10-18

> Registro condensado pelo Orquestrador a partir do retorno do Revisor SOT (somente leitura; texto integral não versionado). Dado de estado; **não é homologação** (só Andraus homologa). Base do delta: `ae3b819` (v1.10). `plan.md` sha256 `8527addb878d7585dbebdf66d376161af91d217c5f0f26c5355eb94a806beba6`. Gate rodado pelo Orquestrador (o Revisor não tem Bash/MCP): validate_spec_sot 13/13 PASS, revisor_gate PASSOU_D, 0 sinais H, check_invariants 0.

## 1. Veredito
**CONFORME condicional** (teto: H-001 ABERTA; gate não rodou dentro da sessão do Revisor). 0 Críticas · 0 Médias · 2 Menores novas (n-d, n-e).
**N-08 FECHADA** (núcleo causal com `outcome_ref`/`no_outcome` em BASpec-008 GATE DE SAÍDA plan.md:913, EC-CKG-005 PRECOND E3 plan.md:1505, esquema `causal` plan.md:1433; alinhado a RULE-CKG-008 plan.md:438-440 e ADV-04(h)). **m-A, m-B, n-b FECHADOS. n-c** fechado como texto (plan.md:54/146/1646: negação de `conviction` por padrão = decisão de Andraus no chat 2026-10-17, **sem ata ainda**). **n-a ACEITA** com ressalva Menor: os `assert-absent` usam variantes das frases porque as literais existem no changelog (INV-07).

## 2. Cobertura
Delta 10 de 122 blocos (ADV-CKG-21, BASpec-CKG-008, EC-CKG-005, autopré-check, cabeçalho, etiquetagem, herança/delta, histórico, I/O schema, nota de gate) conferidos integralmente; dependentes lidos; 112 inalterados HERDADOS; amostra anti-leniência (RULE-CKG-010, BASpec-010/013, EC-001..004, CC-01..CC-12, EARS 1..13, D4, D6, T09, T16). Contagens (13 BASpec / 13 EARS / 6 EC / 19 T / 23 ADV) conferem. Nenhuma decisão aberta fechada (CONS-01).

## 3. Menores novas
- **n-d** (checks.md:274): diz que EARS-8 e D6 foram alinhados "por referência", mas o D6 passo 6 (plan.md:1104) só lista presença de campos, sem `CAUSAL_CORE_IMMUTABLE_IN_CHAIN`. Sem contradição, mas a alegação de resolução não confere para o D6. *Conferido pelo Orquestrador: procede.* Ação: corrigir o texto do checks.md ou referenciar o D6.
- **n-e** (plan.md:1457): PRECOND de EC-CKG-001 cita o núcleo causal sem o marcador m-A (consistente por referência); a negação de `conviction` ali é implícita. Sem ação obrigatória.

## 4. Encaminhamento (só Andraus)
Homologar a errata (ata nova, p.ex. DHR-SPEC006-003) registrando a negação de `conviction` e a classificação Minor/aditiva; dona de H-001 (divergência ROADMAP × ata de abertura). Recomendado: corrigir n-d antes da ata.
