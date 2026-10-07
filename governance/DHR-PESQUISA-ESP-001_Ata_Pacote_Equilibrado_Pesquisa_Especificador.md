# DHR-PESQUISA-ESP-001 — Ata — Pacote equilibrado de melhoria da pesquisa do Especificador: detectores implementados, emendas PROPOSTAS

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-06 |
| Status | **DECISÃO DE ANDRAUS (chat, 2026-10-06): "Pacote equilibrado".** Detectores auxiliares **implementados**; **nenhuma regra editada** — as emendas ficam **PROPOSTAS** (`governance/propostas/PESQUISA-ESPECIFICADOR/PROPOSTA-EMENDAS-PESQUISA.md`) até homologação. Não altera `AGENTS.md`, `especificador.md`, `revisor.md`, `atomic-spec.md`, `RULES.md`, o ROADMAP nem decisão aberta. |
| Compatibilidade | n/a (ferramentas auxiliares + proposta; nenhuma BASpec, RULE, método ou decisão aberta alterada) |
| Regime | Aditivo (INV-07). Origem: estudo do Especificador (processo **CONFORME** pelo Revisor SOT) a pedido de Andraus (ata DHR-AUDITOR-EXTERNO-004 §3-quater: pesquisa web do auditor = "não mudar por enquanto"; "estudar melhoria da pesquisa do Especificador"). |

## 1. Decisão `[FATO: chat, 2026-10-06]`
Pacote **equilibrado**: **M1** verificador mecânico de captura verbatim · **M2** regra "sumário de busca ≠ página" · **M6** coleta de metadados de repositório pela API pública · **M5** registro de buscas · **M3** graduação de evidência · **M8** checagem de datas. **M4** (triangulação ≥2 fontes) e **M7** (verificador ao vivo, único com rede nova) ficam para 2ª rodada, após medir o custo.

## 2. O que foi feito e o que NÃO foi `[FATO: arquivos e testes desta sessão]`
- **Implementado:** `scripts/check_sources_verbatim.py` (M1+M2+M8; 13 testes) e `scripts/collect_repo_meta.py` (M6; 11 testes; **sem credencial**; alertas = `INDETERMINADO`, nunca `0`). Medição no repositório: ERRO=0, WARN=0.
- **Proposto, não aplicado:** M2/M3/M5/M6/M8 como texto de método e de Autopré-check (`PROPOSTA-EMENDAS-PESQUISA.md` §2–§3). **Não** ligado ao CI. O Especificador **não tem Bash**: quem executa os detectores é o Orquestrador (ou o CI, se Andraus decidir).
- **Defeito do meu 1º M1, corrigido:** o corpus de "citação interna" incluía o próprio documento verificado e deixava passar citação inventada (revelado por teste).

## 3. Pendências de Andraus (ver `PROPOSTA-EMENDAS-PESQUISA.md` §4)
Homologar as emendas · ligar o M1/M8 ao CI como informativo · **como tratar "alertas de segurança graves" que a API pública não expõe** (o precedente da SPEC-006 registrou `0` "conservadoramente" — incoerente com a captura do `guardrails-ai`; opções a/b/c, nenhuma aplicada) · M4/M7 na 2ª rodada.

## 4. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** `ECC-VAL-001` (FECHADA, DHR-DEC-003) é usada só como parâmetro da janela do M8.

## 5. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
Fora de escopo dos agentes (§4.1) **por ora**: nenhum texto embutido em `especificador.md`/`revisor.md` muda; reclassificar quando as emendas forem homologadas.

## 6. Registro
- [x] Esta ata · [x] `scripts/check_sources_verbatim.py` + testes · [x] `scripts/collect_repo_meta.py` + testes · [x] `PROPOSTA-EMENDAS-PESQUISA.md` · [x] `CATALOGO-OFICIAL.md` · [x] `rpsa-ledger.json` · [x] `build_map.py` + `--check`
- [ ] homologação das emendas por Andraus · [ ] decisão sobre CI · [ ] decisão sobre alertas INDETERMINADOS

---

**Andraus** *(decisão em chat, 2026-10-06; registro pelo Orquestrador interno)*
