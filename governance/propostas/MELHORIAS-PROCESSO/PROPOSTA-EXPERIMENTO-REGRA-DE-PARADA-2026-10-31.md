# Proposta — experimento da regra de parada de rodadas (A1 da auditoria de burocracia)

> **Não normativo. PROPOSTA.** Nada foi aplicado em `AGENTS.md`, `revisor.md`, `especificador.md` nem em scripts. Não fecha decisão aberta (CONS-01). Segue `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` (A1) e responde à escolha de Andraus (chat, 2026-10-31): "preparar experimento". **Premissa corrigida:** o Plan da SPEC-049 já foi homologado (`DHR-SPEC049-002`), então o experimento vale para o **próximo Plan** que Andraus mandar abrir, não para o da SPEC-049.

## 1. Hipótese
Boa parte das rodadas e dos tokens do laço Especificador↔Revisor é gasta em **Menores de coerência** (citação/âncora C07, contradição C01, vocabulário C02), verificáveis por script, sem que o número de **Críticas/Médias** que chega à homologação mude. Parar de abrir rodada só por Menores, tornar o delta por hash obrigatório e limitar rodadas por perfil reduz tokens por Spec **sem reduzir a Eficácia** (Médias/Críticas pegas).

## 2. Baseline medido (para comparar)
- Ledger (`governance/aprendizado/LEDGER-ACHADOS.md`, até a SPEC-049 abertura): 35 rodadas, **0 Críticas, 39 Médias, 138 Menores**; hash do alvo declarado em 3/35 rodadas; delta em 13/35.
- **SPEC-049 completa (tokens de subagentes, do HANDOFF da `main`):** abertura **906.237** (Esp. 250.105+132.967+110.274; Rev. 172.341+134.928+105.622) + Plan **1.389.735** (Esp. 408.246+222.488+156.058 = 786.792; Rev. 234.891+188.916+179.136 = 602.943) = **≈ 2,30 milhões**. Delta custou 20–40% menos que integral (n pequeno).
- Rodadas do Plan da SPEC-049: 3 (R1 integral, R2 e R3 por delta); 4 Menores finais deixados "na construção" (ata `DHR-SPEC049-002` §3) — ou seja, o corte "Menores não abrem rodada" já foi praticado de fato no fim.

## 3. A regra a testar (3 partes, todas reversíveis)
1. **Parada por severidade:** parecer sem Crítica e sem Média (só Menores) **não abre nova rodada**; os Menores mecânicos vão por ficha M (já existe: `aplicar_ficha_m.py`), os demais viram condição de homologação ou ficam para a construção, à escolha de Andraus.
2. **Hash obrigatório do delta da R2 em diante:** o pedido ao Revisor traz `BASE`/`SHA256-ALVO`/`DELTA` (`delta_pacote.py`); sem hash, a rodada é integral e registrada como tal. (Hoje é cortesia: 3/35.)
3. **Teto de rodadas por perfil:** LOW 2 · MEDIUM 3 · HIGH 4 · CRITICAL 5. Ao atingir o teto com Média aberta, **escala a Andraus** (decisão dele), nunca abre rodada extra sozinha.

## 4. O que NÃO muda (guarda de Eficácia)
Crítica e Média **sempre** abrem rodada; Dossiê de Pesquisa, revisão adversarial (EUA-E18) e o gate determinístico (`validate_spec_sot`, `revisor_gate`) ficam como estão; nenhum Menor é descartado — todo Menor fica registrado no parecer e no ledger. Nenhuma regra de método é afrouxada.

## 5. O que medir (já medível com o que existe)
Por Spec: rodadas; Médias por rodada; Menores restantes na homologação; **tokens por papel e por rodada** (`telemetria_tokens.py` / `TELEMETRIA-ONDA0.md`); fração de rodadas por delta com hash; e, para Eficácia, **qualquer Média/Crítica achada depois da homologação** (em erratum ou na construção) atribuível a um Menor não corrigido.

## 6. Critério de sucesso e de parada do experimento
- **Sucesso:** tokens totais da Spec ≥ 20% abaixo do baseline do mesmo perfil **e** nenhuma Média/Crítica pós-homologação atribuível à regra.
- **Falha (reverter):** uma Média/Crítica pós-homologação atribuível a Menor deixado de lado, ou rodada extra pedida por Andraus por qualidade.
- **Limite honesto:** n=1 Spec; a variância entre Specs (tamanho, perfil) é grande — por isso comparar também por **linhas de corpo** (seção 2-bis do ledger) e repetir em 2–3 Specs antes de institucionalizar.

## 7. Para executar (por ordem de Andraus, quando mandar abrir o próximo Plan)
1. Ordem de Andraus citando este experimento (ata curta); 2. incluir a regra no **pedido** ao Especificador/Revisor daquele Plan (sem editar `.claude/agents/*` nem `AGENTS.md` ainda); 3. registrar métricas do §5 no ledger/telemetria; 4. retrospectiva no fechamento (LOOP-001 passo 5) decide se a regra vira texto normativo, com `MECANISMOS.json`/`COE-14` no mesmo PR se virar mecanismo.

## 8. Decisão de Andraus (chat, 2026-10-31; `DHR-RETRO-003`)
**Aprovado como experimento (P10)** para o próximo Plan que ele mandar abrir. Sem esse comando, nada é executado. Ao abrir o Plan, o Orquestrador inclui a regra do §3 e as métricas do §5 no pedido ao Especificador e ao Revisor e registra o baseline; o fechamento (retrospectiva) decide se a regra vira texto normativo.

