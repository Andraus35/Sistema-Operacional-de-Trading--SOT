# Teste A (Especificador: Opus 4.8 → 5.5) — protocolo pré-registrado pelas lentes dos 4Es — PROPOSTA

> Não normativo (`[PROPOSTA]`). Base: `DHR-ROTEAMENTO-001` D2–D4 e `AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md` §8.1–8.2; troca já vigente por `DHR-ROTEAMENTO-002` (teste **posterior**, com reversão). **Pré-registro: nada abaixo muda depois de a primeira rodada começar.** Execução só com ordem expressa e **limite de cota fixado por Andraus** (campo §7).

## 1. Pergunta e hipótese `[PROPOSTA]`
**H0 (reverter):** o Especificador em `claude-opus-5-5` perde defeitos Crítico/Alto ou produz mais falso alarme/reabertura que em `claude-opus-4-8`. **H1 (manter):** não-inferior em Eficácia, com menor custo de cota.

## 2. Ordem dos 4Es = ordem das comportas (lexicográfica; Economicidade nunca acima de Eficácia — CONST/Q-009)
Uma comporta reprovada **encerra** o teste: reverter (ou investigar), sem "compensar" com custo menor.

| # | E | Pergunta | Métrica (fonte) | Aprova se |
|---|---|---|---|---|
| 1 | **Conformidade** | O teste e o braço obedeceram às regras? | (a) 0 edição de texto normativo/baseline fora do pedido (diff); (b) 0 violação do roteador (`uso.jsonl` sem `negar` inesperado); (c) pré-registro intacto (hash deste arquivo no 1º dia); (d) entrada congelada idêntica nos braços; (e) nada fora de scratchpad | tudo = 0 violações; senão **braço reprovado** (CONST-01/INV-07) |
| 2 | **Eficácia** | Entrega o que se pede, sem perder defeito grave? | por tarefa: defeitos do gabarito corrigidos/total, **perda em Crítico/Alto**, defeitos novos introduzidos (gate D + Revisor cego + conferência no repositório), falsos alarmes | **0 perda em Crítico/Alto**; Menor: tolerância ≤1 de 18 (D4); falso alarme não aumenta; gate D ≥ controle |
| 3 | **Efetividade** | Serve ao propósito a jusante (Spec que o Revisor aceita)? | rodadas até CONFORME; taxa de reabertura pelo Revisor titular (cego ao braço); mesma taxa de CONFORME na mesma rodada | ≥ controle (não pior) |
| 4 | **Eficiência** | Quanto de trabalho por resultado? | tokens, chamadas e duração **por defeito confirmado corrigido** (relatório do `Agent`; ausente = `n/m`, nunca estimado) | ≤ controle |
| 5 | **Economicidade** | Cabe na cota? | cota consumida vs. limite de Andraus (§7); referência de preço 0,8× | dentro do limite; **só desempata**, nunca reverte comporta 1–3 |

## 3. Desenho `[PROPOSTA]`
- **Braços:** C = `claude-opus-4-8` (controle congelado: prompt/versão do agente do commit `89262bd`) · T = `claude-opus-5-5` (efeito padrão). Varredura de `effort` (5.5/medium|high|xhigh) **só depois**, se T passar (D6).
- **Tarefa congelada:** lote de correções de achados sobre texto-base **idêntico** nos dois braços (entrada = Spec-alvo + lista de achados confirmados; saída = texto corrigido). Gabarito = achados confirmados no repositório (juiz ≠ LLM, DHR-AUDITOR-EXTERNO-014). **Pendência de dado:** o gabarito de 18 defeitos da SPEC-006 v1.0 **não está no repositório** (só o resumo na DHR-AUDITOR-EXTERNO-014; o Plan SPEC-006 não existe — só `ABERTURA.md`); sugerido montar lote novo e congelado (ex.: defeitos plantados em cópia da SPEC-005 homologada, no molde do banco de estresse da DHR-015, sorteio fora do braço).
- **Repetições:** ≥3 por braço (variação medida em reexecução ≈5%); ordem dos braços sorteada; Revisor titular **cego** ao braço (arquivos anonimizados).
- **Juiz:** gate D (`revisor_gate`, pelo harness/Orquestrador) + conferência `arquivo:linha` no repositório + Revisor titular. Resultado final, não caminho.
- **Isolamento:** todas as saídas em scratchpad/cópia; **nenhuma** escrita em Spec homologada, `canon/`, `governance/` normativo.

## 4. Riscos e limites declarados `[FATO/INFERÊNCIA]`
1. **Seleção do modelo:** o parâmetro `model` do `Agent` aceita apenas aliases (`opus|sonnet|haiku|fable`), sem fixar 4.8 × 5.5; e o **roteador (DHR-ROTEAMENTO-003) nega `model`/`effort` por invocação no Especificador** por desenho. Como o braço C será servido é decisão aberta ao dono (§7, opção 1/2/3).
2. Circularidade de família (Revisor Sonnet 5.5 × executor Opus) é menor que na DHR-AUDITOR-EXTERNO-014, mas existe; Auditor Externo (outra família) permanece opcional.
3. Poder estatístico baixo (3 repetições × 1 lote): o teste detecta regressão grosseira, não equivalência fina — por isso a comporta 2 exige **0 perda** em Crítico/Alto e a decisão final fica com Andraus.
4. Custo do juiz: um passe do Revisor ≈275 mil tokens (DHR-AUDITOR-EXTERNO-014) — o limite de cota precisa cobrir 6 revisões + 6 execuções.

## 5. Regra de decisão `[PROPOSTA]`
Comportas 1→2→3 aprovadas ⇒ **manter 5.5** (próximo: varredura de esforço, depois EUA-E24 aditiva). Qualquer reprovação em 1–3 ⇒ **reverter** a `claude-opus-4-8` por nova ata (ou investigar o lote). 4–5 só informam. Andraus decide; este protocolo não homologa nada.

## 6. Telemetria
Uma linha por rodada em `TELEMETRIA-ONDA0.md` (+ coluna de braço/repetição); `uso.jsonl` do roteador anexado como dado; `n/m` quando o `Agent` não reportar.

## 7. Parâmetros que dependem de Andraus
- Limite de cota para o teste: ______ (tokens ou % da cota)
- Como servir o braço de controle (4.8): ______
- Lote congelado: ______
