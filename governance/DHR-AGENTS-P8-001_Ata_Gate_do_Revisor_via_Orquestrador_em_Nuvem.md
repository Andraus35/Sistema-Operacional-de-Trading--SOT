# DHR-AGENTS-P8-001 — Ata de Decisão — Gate determinístico do Revisor: canal `GATE-D` do Orquestrador em nuvem (proposta P8)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Controlador / Revisor SOT |
| Ref | Ordem de Andraus (chat, 2026-10-31): P8 → "Formalizar: Orquestrador roda o gate" · `governance/aprendizado/RETROSPECTIVAS.md` (P8) · `governance/MECANISMOS.json` (`mcp.revisor-gate` e `hook.revisor-guard` inertes em nuvem) · `DHR-AUDITOR-EXTERNO-009/010/011` · `AGENTS.md` §10 |
| Data | 2026-10-31 |
| Status | **APLICADA por ordem de Andraus** (emenda ao `.claude/agents/revisor.md`, arquivo reservado — AGENTS.md §10). Não fecha nem abre decisão (CONS-01). |
| Compatibilidade | Minor |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Emenda ao texto do §3 do Revisor (segundo canal do gate); o Especificador não depende do gate do Revisor e não é alterado. |

## 1. Problema `[FATO]`
O Revisor é instruído a chamar a ferramenta MCP `revisor_gate` em toda rodada, mas **em nuvem o MCP inline não carrega** (`MECANISMOS.json`: `mcp.revisor-gate` e `hook.revisor-guard` = inertes). Resultado: a chamada falha, o Revisor declara "GATE NÃO VERIFICADO" e o parecer fica no máximo condicional, embora o Orquestrador já rode o mesmo gate por Bash (`revisor_gate.py`) e registre `PASSOU_D` na telemetria. A retrospectiva (P8) registrou G1/G2 "sempre pendentes".

## 2. Decisão de Andraus `[FATO]`
Formalizar o que já ocorre: o Orquestrador roda `python scripts/revisor_gate.py <doc> [--rapido]` e entrega o resultado ao Revisor na linha **`GATE-D: <PASSOU_D|REPROVADO_D> | cmd: <comando> | SHA256-ALVO: <64 hex> | data: AAAA-MM-DD`** do pedido. A ferramenta MCP continua sendo o canal 1 quando carregada; `GATE-D` é o canal 2.

## 3. Salvaguardas (a falha fechada NÃO foi enfraquecida) `[FATO]`
- `GATE-D` só vale se **todos os campos** estiverem presentes e o `SHA256-ALVO` dele for **igual** ao `SHA256-ALVO:` do pedido (amarra o resultado à versão revisada); senão conta como **ferramenta ausente** ⇒ "GATE NÃO VERIFICADO" e **no máximo CONFORME condicional**.
- `REPROVADO_D` vindo do canal 2 produz NÃO CONFORME Crítica **sem análise semântica**, como no canal 1.
- O Revisor **não** confirma o gate por conta própria (continua sem Bash — ENF-03 intacto); o parecer reporta `VEREDITO D: <valor> (via GATE-D do Orquestrador, sha256 conferido)`, texto que o guarda `revisor_guard.py` (G2) já exige (`VEREDITO D`).
- **Achado do pré-teste adversarial:** a primeira redação tratava um `GATE-D` incompleto como "ferramenta ausente" (⇒ no máximo condicional), o que **descartaria um `REPROVADO_D`** por formato. Corrigido antes de entrar: resultado `REPROVADO_D`, mesmo incompleto ou com sha divergente, **impede qualquer CONFORME** e devolve ao Orquestrador para regerar o gate.
- Limite honesto: o Orquestrador é a fonte do resultado e o Revisor não o reproduz; a integridade do script do gate continua protegida por `gate_manifest.py` (selo) e `CODEOWNERS`.

## 4. Mudança `[FATO]`
`.claude/agents/revisor.md`: comentário do frontmatter, §3 (frase de abertura, novo item "Canal 2 — `GATE-D:`", item de falha fechada) e a linha do formulário de saída. Carimbo RPSA alinhado por `check_rpsa.py --register`. **Não** foram alterados: lista de ferramentas do frontmatter, `mcpServers`, método, checklist, severidades nem regra.

## 5. Pré-teste `[FATO]`
Cenários adversariais sobre o §3 novo (valor correto, sha divergente, `GATE-D` ausente, `REPROVADO_D`) e a suíte completa — ver o registro no `HANDOFF.md` e em `governance/propostas/MELHORIAS-PROCESSO/EQUIVALENCIA/TESTE-AB-AGENTS/`.

## 6. Permanecem ABERTAS (CONS-01)
O estado vem do `ROADMAP.md`. Nenhuma decisão foi fechada ou aberta por esta ata.

## 7. Registro
- [x] Esta ata · [x] emenda no `revisor.md` · [x] carimbo RPSA · [ ] merge (assinatura de Andraus)
