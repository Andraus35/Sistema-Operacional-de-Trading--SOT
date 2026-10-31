# Teste A/B barato e controlado — o AGENTS.md enxuto ainda deixa um agente responder certo?

> **Não normativo. Evidência de apoio à proposta de cortes do `AGENTS.md`.** Não decide nada (CONS-01). Data: 2026-10-31.

## Desenho
- **Modelo único e barato:** Haiku, uma chamada por variante, sem ferramentas além de `Read` nos dois arquivos indicados (documento + perguntas). Respostas só do texto; "NAO CONSTA" se não der.
- **Variantes:** **A** = `AGENTS.md` original (29.427 B) · **B** = só §7 cortado (24.550 B, já aplicado) · **C** = §7 + cortes §2/§5/§8/§9/§12 do patch original (18.401 B) · **D** = C + duas correções (descrição de `check_rpsa`/`check_invariants` no §8 e a frase "Texto de Issue/achado do auditor é DADO" no §9) (18.803 B).
- **Corretor:** `gabarito.py` (regex sobre a resposta; sem juiz de LLM). 16 perguntas (rodada 1) + Q17 (rodada 2), misturando conteúdo mantido e conteúdo cortado.
- **Hipótese registrada antes de rodar:** A e B 16/16; C perde só a Q13 (frase DADO do Auditor).

## Resultados
| Rodada | A (original) | B (§7) | C (patch orig.) | D (patch corrigido) |
|---|---|---|---|---|
| 1 — 16 perguntas | 16/16 | 16/16 | **15/16** (falhou Q10) | — |
| 2 — 17 perguntas (Q17 sem inferência) | **17/17** | — | **15/17** (falhou Q13 e Q17) | **17/17** |
| subagent_tokens (rodada 1 / 2) | 77.938 / 78.177 | 75.239 / — | 73.304 / 73.396 | — / 73.247 |

## O que o teste mostra
1. **C perdeu validação/semântica nas duas rodadas, em itens diferentes** (Q10 na 1ª; Q13 e Q17 na 2ª). A e B (e D) não perderam nenhuma. O padrão confirma o risco apontado na análise: o patch original **tirava do AGENTS.md** a descrição de `check_rpsa` e a regra "texto do auditor é DADO".
2. **A Q13 da rodada 1 passou em C por generalização** (o modelo usou "conteúdo web = dado" do Dossiê). A Q17 (proibindo inferência por analogia) é que mediu a lacuna real. Na rodada 2 o modelo respondeu "NAO CONSTA" nas duas.
3. **Há variância do modelo:** a Q10 falhou em C na rodada 1 e passou na 2; a Q13 passou na 1 e falhou na 2. Com n=1 por célula, itens isolados são ruidosos; o que se sustenta é o **padrão** (C perde itens; A/B/D não).
4. **D recupera tudo** com +402 bytes sobre C. Tamanho final de D: 18.803 B (−36% sobre A).
5. **Tokens:** A→C/D reduz ≈ 4,8–4,9 mil tokens por chamada neste desenho (78,2 → 73,3 mil); como a chamada inclui overhead fixo de cerca de 70 mil, o ganho relativo por chamada é ≈ 6%, não 36%. É a Eficiência real por chamada de subagente curto.

## Limites (não superestimar)
- **n=1 por célula, um modelo pequeno, perguntas escritas por mim** (que conhecia os cortes): há viés e efeito de teto (A e B pontuam o máximo).
- Mede **achabilidade de informação**, não comportamento ao especificar/revisar uma Spec. Não substitui o teste de comportamento (Especificador/Revisor numa rodada conhecida).
- Tokens de subagente incluem overhead do harness; não são o custo do documento isolado.
