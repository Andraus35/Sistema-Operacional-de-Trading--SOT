# DHR-AUDITOR-EXTERNO-017 — Ata — Detectores determinísticos adicionais no gate e guarda de fim do Revisor (hook SubagentStop)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "elevar necessariamente para nível máximo; avalie uso de rules, guardrails, hooks, policy e mecanismos determinísticos")**. O merge desta ata por Andraus é a ratificação. **Não altera `revisor.md`, `especificador.md`, `AGENTS.md`, método, regra nem decisão aberta; não atribui nível oficial de maturidade (RULE-MM-02).** |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta detectores de codigo ao gate e um hook de fim de turno para o Revisor; nao altera o texto do Revisor nem do Especificador, checklist, metodo nem regra. |

## 1. Origem `[FATO]`
Auditoria por testes do Revisor (relatório `governance/AUDITORIA-REVISOR-MATURIDADE-2026-10-17.md`): gate de código = 0/14 defeitos sutis plantados em Spec real; o Revisor declarava "não verificado" em vez de abrir ROADMAP/RMR-001/RULES; o gate MCP não carrega no Revisor em nuvem.

## 2. O que muda `[FATO]`
1. `scripts/revisor_detectores.py`: `mapeamento_conflitante`, `id_norma_inexistente` (ENF/INV/CC acima do registrado), `contagem_declarada`, `spec_nome_incoerente`, `valor_fonte`, `dhr_backlog` e `comparar_versoes` (referência removida/acrescentada, valor trocado, pendência `[ ]`→`[x]`, fonte trocada). Integrados ao `revisor_gate` (informativos; o diff usa `git show HEAD:<plan>` quando há versão anterior). Calibrados em 10 Plans homologados (1 achado, genuíno) e testados por mutação.
2. **Guarda do Revisor:** `scripts/revisor_guard.py` + `scripts/revisor-guard.js`, hook `SubagentStop` (matcher `Revisor`) em `.claude/settings.json`. Ao fim do Revisor o código confere: **G1** as 4 fontes do núcleo do Passo 0 foram abertas; **G2** o gate de código foi rodado **pelo harness** sobre o artefato e entra no parecer (independe da ferramenta MCP); **G3** citações `arquivo:linha` + trecho existem. Violação ⇒ exit 2 e o Revisor continua uma vez (`stop_hook_active` evita laço). Falha do script ⇒ libera (fail-open).
3. `gate_manifest.py` ganha os 3 arquivos novos; CI roda `test_revisor_detectores.py` e `test_revisor_guard.py` (bloqueantes).

## 3. Resultado medido `[FATO: 2026-10-17]`
SPEC-021 com 14 defeitos plantados por outro agente, 9 rodadas do Revisor (`claude-sonnet-5-5`): sozinho 48–55% por rodada (união 9/14); com a guarda 69% por rodada (união 11/14). Ganho atribuível: 2 defeitos (fronteira SPEC-024×041 e DHR do BL-021) vindos do gate injetado. Gate de código sozinho: 0/14 → 6/14 (9/14 com versão anterior). **Limites:** o hook **não estava ligado** na sessão do teste (hooks são lidos na abertura da sessão); a mensagem do hook foi entregue ao Revisor por equivalência; os Revisores abriram a cópia homologada da SPEC-021 do repositório (teto, não média); o Revisor reemitiu com contexto da 1ª passada.

## 4. Achados para Andraus (não corrigidos) `[FATO]`
- **SPEC-003 (baseline):** o Autopré-check declara "Critérios em EARS (10)" e a seção lista 11 (`specs/features/SPEC-003/plan.md:1164` × 331–341). Baseline: só erratum por decisão de Andraus (INV-07).
- BL-020 aparece no Plan da SPEC-021 como `ATIVADO` e no painel RMR-001:135 como `Descartado 2026-09-28` (achado do Revisor na rodada com guarda).

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.** Pendentes de Andraus: política `RULE-REV-xx` + emenda do `revisor.md`; Auditor Externo em Spec CRITICAL; defeitos escritos por Andraus; aprovação/medição contínua para o L4 (ver `AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md` §5).

## 6. Registro
- [x] Esta ata · [x] detectores + guarda + testes · [ ] hook confirmado ao vivo (reiniciar sessão) · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
