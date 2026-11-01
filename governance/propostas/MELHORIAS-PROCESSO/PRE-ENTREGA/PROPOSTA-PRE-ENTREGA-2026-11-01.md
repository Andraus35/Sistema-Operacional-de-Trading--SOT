---
tipo: proposta-pre-testada
status: PROPOSTA (não vigente; nada instalado nem aplicado)
data: 2026-11-01
origem: AUDITORIA-ESPECIFICADOR-PRECHECK-2026-11-01.md (itens P-A e P-F)
---
# P-A + P-F — pré-gate unificado e higiene do especificador.md

Decisões de Andraus (chat, 2026-11-01): começar por P-F(1–5)+P-A; o pré-gate é rodado pelo Orquestrador/hook (o Especificador continua sem Bash); detectores informativos até P-E medir falso alarme; PR sem mesclar.

## Conteúdo
| Arquivo | O que é | Estado |
|---|---|---|
| `pre_entrega.py` | Compõe `validate_spec_sot`, `check_repo_research`, `build_map --check` (bloqueantes, como no CI) e `check_invariants`, `check_dimensionamento`, `check_refs`, `backlog_triggers` + 13 detectores de `gate_extra`/`revisor_detectores` (informativos). Emite `pre-entrega.json` com sha256 de plan/checks. Sem lógica nova. | Testado (`test_pre_entrega.py`, 3 testes OK); **não instalado** |
| `PATCH-ESPECIFICADOR-P-F-2026-11-01.patch` | (1) TMP→Signal Package; (2) `AGENTS.md §3`→`§4`; (3) CCM-001 BASELINED e J-001 sem "trava SPEC-003"; (4) CC-01..CC-12; (5) §9 vira ponteiro ao ROADMAP; (6) item do Autopré-check: o Orquestrador roda `pre_entrega.py` e anexa o JSON. | `git apply --check` OK; **não aplicado** |

## Para instalar (só por ordem expressa de Andraus)
1. Mover `pre_entrega.py` para `scripts/` e o teste para `tests/`; registrar em `governance/MECANISMOS.json` (COE-14) e no `GATE-MANIFEST.sha256`.
2. `git apply` do patch (emenda homologada ao `.claude/agents/especificador.md`; carimbo RPSA via `check_rpsa.py --register`).
3. Fluxo: Especificador edita → Orquestrador roda `pre_entrega.py` → devolve o JSON → corrige até zero bloqueante → Revisor recebe o mesmo JSON (casado por `SHA256-ALVO`).

## Medir antes de promover (4Es)
Contar Médias do R1 com e sem pré-gate em 5 rodadas; P-E (mutação) para recall e falso alarme; detectores só viram bloqueantes por ordem de Andraus.

## Limites
O pré-gate não acrescenta recall: o backtest da auditoria deu 0/3 Médias com os detectores atuais. Seu ganho imediato é **prova anexa e antecipação** (o autor vê antes do Revisor). O recall vem de P-B, C-1/C-2 e P-D.

## Avanço (2026-11-01, "Avançar"): P-E, C-1 e C-2 como protótipos medidos — nada instalado
Arquivos: `detectores_novos.py` (C-1a, C-1b, C-2), `mutacao_pe.py` (bateria de mutação), `test_detectores_novos.py` (5 testes). Rodar: `python -B mutacao_pe.py specs/features/SPEC-049`.

**Mutação (5 defeitos plantados no Plan SPEC-049 baselined):** pegou 4/5 — M1 definição de código apagada (C-1a), M2 grafia divergente (C-1a), M3 recusa sem código (C-1b), M4 número trocado em 1 local (C-2); **escapou M5** (✔ novo em `checks.md` sem evidência — C-4 ainda não escrito). Detectores já existentes (`gate_extra`, `revisor_detectores`): **0/5** nesta bateria.

**Falsos alarmes no Plan baselined:** `gate_extra`/`revisor_detectores` 0; C-1b 0; C-2 (renomeação) 0; **C-1a 1** (`CONTRADICTION_SIDE_OMITTED`, 1 uso sem prefixo `WRV_`; não verifiquei se é erro real ou código de outra Spec). Na 1ª versão, C-1a dava 35 (enums contados como códigos); a restrição às famílias de prefixo da própria tabela cortou para 1.

**Backtest no histórico real (SPEC-049 v1.0→v1.1→v1.2):**
- C-1b achou 1 linha na v1.0 (INV-WRV-01, recusa sem código) — relacionada ao achado R1-M01 do Revisor, mas esse achado cobria outras recusas que o detector **não** viu. Recall parcial. 0 na v1.1/v1.2.
- C-1a: só o 1 caso acima, em todas as versões; **não** reproduziu nenhum achado do Revisor.
- **C-2: não viável ainda.** Versão larga (qualquer token retirado) = 8–9 achados por transição, quase todos ruído (`SPEC-007` em 129 locais). Versão estrita (renomeação 1↔1) = 1 achado na v1.0→v1.1 (provável falso alarme: o código ainda é legítimo em outros pontos) e **0 na v1.1→v1.2, onde o Revisor achou resíduos reais** ("medida 1.540 em F6/§1.8" no `checks.md`) — a linha tinha vários tokens trocados de uma vez e a regra 1↔1 não dispara. Precisaria casar tokens por posição na linha, tratar menção histórica "(v1.1)" como legítima e ignorar IDs genéricos. **Não promover.**

**Leitura honesta:** C-1a/C-1b são viáveis como INFORMATIVOS (baixo falso alarme, pegam mutação sintética), mas o recall sobre achados reais do Revisor foi **pequeno** (≈1 parcial em 3 Médias da v1.0). C-2 não passou. O ganho esperado de P-B (rastro por item) e P-D (gabaritos) segue sendo o maior; detector sozinho não substitui o Revisor. Amostra: 1 Spec, 3 versões.

## P-B + C-4 (ordem de Andraus, 2026-11-01: "Escrever P-B + C-4") — protótipos medidos; nada instalado
Arquivos: `autoprecheck_catalogo.json` (32 caixas do §7/§7-bis: 16 tipo D com ids do `pre-entrega.json`, 16 ATESTADO), `lint_autoprecheck.py` (linter + `--template`), `test_lint_autoprecheck.py` (11 testes), e `checks_ancorado` em `detectores_novos.py` (+3 testes). Total da pasta: 19 testes OK.

**P-B — o que faz.** O Orquestrador gera o rascunho (`lint_autoprecheck.py <spec> --template --pre-entrega pre-entrega.json --contexto alta`): itens tipo D saem marcados `[x]` com `PE:<id>` se o pré-gate deu OK; itens ATESTADO saem `[ ]` pedindo âncora `arquivo:linha «trecho literal ≥100 caracteres»`. O linter reprova: item ausente; `[ ]`; D sem evidência ou com `PE:` fora do catálogo; bloqueante vermelho; achado informativo sem `justificado:`; âncora que não consta literalmente na linha; `N/A` indevido ou sem `motivo:`; `pre-entrega.json` de outra versão do `plan.md`.
**Medida (SPEC-049, contexto "alta"):** hoje **0 de 32** itens têm rastro (não existe `autoprecheck.md`). Com o rascunho: **13 itens comprovados pelo pré-gate**, **12 ATESTADO** a ancorar, 6 N/A (abertura/trading/especialidade). Ou seja, o Revisor passa a ver **onde** o autor só afirma.
**Limites:** confere forma e âncora, nunca o sentido — âncora literal prova que o trecho existe, não que a conclusão do autor está certa; 100 caracteres é calibração a decidir; não testado com Especificador real; os 13 itens "D" valem tanto quanto os detectores por trás (recall 0/3 no backtest).

**C-4 — resultado, incluindo o que NÃO funcionou.**
- Versão larga ("✔/PASS sem âncora de ID"): **455 alarmes** nos 14 `checks.md` baselined (linhas de checklist de profundidade não têm âncora por construção) e **12 idênticos** nas 3 versões da SPEC-049 (não discrimina nada). **Descartada.**
- "Âncora citada que não existe": 38 alarmes, quase todos legítimos (`ENF-0n` do método, placeholders `0NN`, IDs herdados de outra Spec).
- **Versão estreita adotada:** ID da *própria família* da Spec (a mais frequente no Plan) citado num ✔ e ausente do Plan. **0 falsos alarmes nos 14 baselines**; pega o defeito plantado M5 (ID inexistente). **Mas o caso que mais importa — ✔ sem nenhuma evidência (M6, o achado R1-M01 do Revisor) — ESCAPA**, e 0 achados nas 3 versões reais da SPEC-049. Esse caso só se resolve por evidência por linha (P-B no próprio `checks.md`) e por revisão humana; não por detector de âncora.

**Para instalar (só por ordem de Andraus, ata nova):** mover `lint_autoprecheck.py` + catálogo para `scripts/` e os testes para `tests/`; selar em `GATE-MANIFEST.sha256` e CODEOWNERS; `MECANISMOS.json` (COE-14); incluir o rascunho no fluxo do Orquestrador; decidir os 100 caracteres. C-4 estreito entra como informativo em `pre_entrega.py` (hoje fora dele).

## Decisão de Andraus (chat, 2026-11-01): "Testar antes de instalar" — protocolo de medição
P-B e C-4 estreito **não são instalados** até haver medida em rodada real. Gatilho: o próximo Plan que Andraus mandar abrir (o mesmo do experimento P10, se ele quiser combinar). Protocolo, para o Orquestrador:
1. Antes de cada entrega ao Revisor: `python scripts/pre_entrega.py specs/features/<SPEC>` e anexar o `pre-entrega.json`; zerar bloqueantes.
2. Gerar o rascunho (`lint_autoprecheck.py … --template`) e preencher só os itens ATESTADO; rodar o linter. Anotar quantos itens exigiram âncora e quantos o linter reprovou.
3. Anotar por rodada: Médias/Menores do parecer; quantos **o pré-gate e o linter já tinham acusado** antes (acerto) e quantos escaparam (recall real); alarmes que não eram defeito (falso alarme).
4. Comparar o R1 com a base histórica (SPEC-049 Plan R1 = 3 Médias, ≈1,39 M tokens em 3 rodadas; SPEC-048 Plan R1 = 3 Médias) — n pequeno, declarar como tal.
5. Critério de instalar (proposto; Andraus decide): o pré-gate+linter acusaram ≥1 Média real antes do Revisor **e** falso alarme ≤ 2 por rodada; senão, rever o catálogo antes de selar.
