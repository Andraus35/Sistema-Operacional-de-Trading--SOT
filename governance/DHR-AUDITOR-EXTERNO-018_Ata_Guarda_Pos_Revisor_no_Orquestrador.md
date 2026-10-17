# DHR-AUDITOR-EXTERNO-018 — Ata — Guarda pós-Revisor no Orquestrador (hook Stop), porque o SubagentStop não é honrado em nuvem

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "Ir direto à ata de conserto")**. O merge por Andraus é a ratificação. **Não altera `revisor.md`, `especificador.md`, `AGENTS.md`, método, regra nem decisão aberta; não atribui nível de maturidade (RULE-MM-02).** |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta uma guarda de codigo no Orquestrador para conferir o parecer do Revisor; nao altera o texto do Revisor nem do Especificador, checklist, metodo nem regra. |

## 1. Origem `[FATO: sondas de 2026-10-17, sessão nova pós-merge da DHR-017]`
- Revisão curta da SPEC-005: o Revisor não teve `mcp__sot-revisor-gate__revisor_gate` na lista (só Read/Grep/Glob/SubagentHandback), declarou "GATE NÃO VERIFICADO" e **não houve retorno forçado**.
- Sonda temporária (hook que grava o evento, revertida): o `SubagentStop` **dispara** em nuvem, inclusive com `agent_type` = "Revisor SOT", `stop_hook_active=false`, e `last_assistant_message` **vazio** quando o subagente entrega por `SubagentHandback`.
- Reproduzindo esse evento real em `revisor_guard.py`: **exit 2** (G1+G2). Mesmo assim o Revisor encerrou. Conclusão `[FATO]`: o harness em nuvem não faz o subagente continuar por exit 2 nesse tipo de encerramento. `[NÃO COMPROVADO]`: se o script chega a rodar no ambiente do hook (a 3ª sonda, que separaria os casos, não foi autorizada pelo classificador).

## 2. O que muda `[FATO]`
1. `scripts/revisor_posguarda.py` + `scripts/revisor-posguarda.js` (hook **Stop** do Orquestrador): para cada hand-back de um agente cujo `agentType` seja Revisor e que ainda não foi conferido (estado em pasta temporária), reaplica `revisor_guard.avaliar` (G1 núcleo aberto, G2 gate rodado pelo harness e presente no parecer, G3 citações) sobre o transcript do subagente e o texto do `SubagentHandback`. Violação ⇒ `{"decision":"block"}` **uma vez por agente**; o Orquestrador devolve ao Revisor ou roda o gate e anota. `stop_hook_active` e qualquer falha ⇒ libera (fail-open). Detector ≠ Gate (ENF-03).
2. `tests/test_revisor_posguarda.py` (3 testes) no CI. Verificado contra o transcript real da sessão: sinaliza os dois Revisores desta sessão (G2 no 1º; G1+G2 na sonda mínima).
3. Limite honesto: protege o caminho Orquestrador←Revisor; não obriga o Revisor a usar o gate dentro do subagente; quem lê o parecer sem passar pelo Stop do Orquestrador (ex.: Andraus direto) não é coberto.

## 3. Pendências que exigem Andraus `[FATO]`
- **Registrar o hook** em `.claude/settings.json` (`hooks.Stop`, `node scripts/revisor-posguarda.js`) — o classificador de permissões da sessão bloqueou a edição; sem isso o código existe mas **não roda**.
- **Regravar o selo** (`python scripts/gate_manifest.py --write` após incluir os 2 scripts novos em `ARQUIVOS`) — perímetro do selo, também bloqueado/dependente de decisão expressa.
- Registro do MCP do gate no nível do projeto: **não feito** (ata própria; fora desta).

## 4. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.** Piloto da onda 1 só depois da guarda confirmada ao vivo.

## 5. Registro
- [x] Esta ata · [x] script + wrapper + testes · [ ] hook registrado no settings · [ ] selo regravado · [ ] confirmado ao vivo · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
