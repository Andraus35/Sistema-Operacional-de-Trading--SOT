# DHR-AUDITOR-EXTERNO-005 — Ata — Pacote 1 do Auditor Externo: coerência do parecer (veredito derivado, regra citada existe, gate de gatilhos)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisões de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-06 |
| Status | **IMPLEMENTADO NO KIT, NÃO ATIVO NA VM.** Registra as decisões de Andraus (chat, 2026-10-06) e a mudança de código do Pacote 1. **Só vale na VM depois de merge na `main` e da reaprovação do manifesto por Andraus.** Não altera `AGENTS.md`, o Revisor, o ROADMAP nem decisão aberta. |
| Compatibilidade | n/a (operação do piloto; nenhuma BASpec, RULE, método ou decisão aberta alterada) |
| Regime | Piloto controlado; aditivo (INV-07): nenhuma ata anterior editada. Origem: Proposta `cooperacao/PROPOSTA-COOPERACAO-INTERNO-EXTERNO.md` (PN1/P4, PN2, PN10), processo CONFORME pelo Revisor SOT. |

## 1. Decisões de Andraus aplicadas `[FATO: chat, 2026-10-06]`
1. **Pacotes 1, 2 e 3 em sequência, antes da primeira auditoria real** (este ato = Pacote 1).
2. Veredito consultivo **calculado por código** dos achados **válidos**: achado **P0 ⇒ `NAO_OK`**; **P1 ou P2 ⇒ `COM_RESSALVAS`**; **nenhum achado válido ⇒ `OK`**.
3. Se o modelo apontar problemas e **todos** forem descartados na validação ⇒ **bloquear, sem nota e sem ACK**.
4. **Liberdade cognitiva** do modelo na gravidade de cada achado (sem piso por tipo, sem piso por gate vermelho — não escolhidos por Andraus); as exigências do SOT ficam **no gate** (forma, citação literal, regra existente).

## 2. O que mudou no kit (7 arquivos, todos cobertos por `MANIFEST.sha256`) `[FATO: diff do commit]`
| Item | Arquivo | Mudança |
|---|---|---|
| PN1 / P4 | `kit/loop_tools.py` (`derive_verdict`), `kit/auditor_bot.py` | O bot calcula o veredito pela regra do item 1.2 sobre as gravidades dos achados que **passaram** na validação; gravidade desconhecida conta como P0 (fail-closed). O veredito do modelo vira **dado comparado**: o ACK registra se coincide ou **diverge** do calculado. O texto `Veredito consultivo: X` que o workflow lê (`auditor-externo.yml` regex) foi **preservado**. |
| Regra 1.3 | `kit/auditor_bot.py` | `postados == 0` e `descartados > 0` ⇒ nota de bloqueio (uma por motivo), **sem ACK**, código de saída 2; consome uma tentativa (limite de 2 por pedido). |
| PN2 | `kit/validate_finding.py` | Todo **ID normativo** citado em `rule_source` (RULE-/INV-/CC-/ENF-/DHR-/EUA-/ADR-/BL-/SPEC-/WF-/RISK-/GRE-/HRE-/PN-/CONS-/CONST-) deve **existir** no commit auditado (`git grep`); máx. 10 IDs. **Texto livre sem ID continua permitido.** Novo código de erro `E-RULESRC`. Só barra regra **inventada**; não julga se a regra se aplica ao caso. |
| PN10 | `kit/run_gates.py` | `backlog_triggers.py` passa a rodar como gate **informativo** (o gate `ATIVADO` do RMR-001 é "nunca dispensado", `AGENTS.md` §5). |
| Testes | `kit/test_bot.py` (+4), `kit/test_loop.py` (+2), `kit/selftest.py` (+2 casos) | Cobrem o veredito derivado, a divergência registrada, o bloqueio com tudo descartado, a regra inventada e o texto livre. |

## 3. Evidência e limites `[FATO]` / `[NÃO VERIFICADO]`
- **Executado nesta sessão (Windows, sem a VM):** `test_bot` + `test_loop` = **29 testes OK** com um executor local que (a) simula `fcntl` (módulo só de Linux) e (b) normaliza caminhos/UTF-8; **antes** das mudanças a mesma base dava 23/23. O executor **não** faz parte do repositório. **Não** executei na VM Linux, no GitHub nem com o Codex real.
- `[NÃO VERIFICADO]` o efeito de `--ignore-user-config`/`--ignore-rules`; o comportamento do bot com o Codex real após a mudança; o desempenho do PN2 em achados reais (risco de falso-positivo: ID citado em formato que o `git grep -F` não encontra → o achado é descartado e o modelo precisa repostar).
- **Reaprovação:** o manifesto mudou em exatamente os 7 arquivos acima. Andraus aprova o novo hash **na VM** (`sync_auditor.sh --approve <hash>`); o hash é informado a Andraus **fora do repositório** (âncora, ata 002 §3) **depois do merge na `main`**, conferido contra o `MANIFEST.sha256` da `main`.
- **Não mudaram:** `PROMPT-AUDITOR-CI.md`, `DIRETIVAS-AO-AUDITOR.md` (DIR-003 **não** é necessária para este pacote), sandbox, rede, workflow.

## 4. Seguem pendentes `[FATO]`
**Pacote 2** (barreira contra viés: PN12–PN15 — mexe no prompt/diretiva e em `setup_auditor.sh`; exige DIR-003) · **Pacote 3** (rastreio do consenso: P1/P2/PN3 + detector D7 — em `scripts/`, sem custo de manifesto) · liberdade de skills/subagentes (INDETERMINADA — Dossiê H7) · estudo de melhoria da pesquisa web do **Especificador** (em curso).

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** `SPEC-038-DATASRC-001`: decidida neste recorte (DHR-DEC-004), resíduo = provedor de máquina após Discovery do MASTER (BL-033) — nem aberta nem fechada aqui. A abertura da SPEC-006 segue não homologada; o papel do auditor segue **piloto**.

## 6. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
Fora de escopo dos agentes (§4.1): muda a operação do piloto (código do kit), não checklist, método nem regra; `fonte-unica`.

## 7. Registro
- [x] Esta ata · [x] código + testes do kit · [x] `MANIFEST.sha256` regenerado a partir dos blobs LF · [x] `CATALOGO-OFICIAL.md` · [x] `rpsa-ledger.json` · [x] `OPERACAO.md` · [x] `build_map.py` + `--check`
- [ ] merge na `main` · [ ] **reaprovação do novo hash do manifesto por Andraus na VM** · [ ] teste na VM (`--dry-run`) antes do `--go-live`

---

**Andraus** *(decisões em chat, 2026-10-06; registro pelo Orquestrador interno)*
