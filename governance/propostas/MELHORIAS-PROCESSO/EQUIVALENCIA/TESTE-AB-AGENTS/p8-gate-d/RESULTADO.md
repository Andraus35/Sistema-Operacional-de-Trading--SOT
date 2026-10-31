# Pré-teste adversarial do canal `GATE-D` (P8, `DHR-AGENTS-P8-001`)

> **Não normativo. Evidência.** 2026-10-31. Sonnet (o modelo do próprio Revisor), só `Read` do §3 do `revisor.md` + cenários; 2 réplicas; gabarito por script. O Haiku foi barrado pelo roteador (R-GATE: tarefa de gate/revisão não roda em Haiku) e **não** contornei a regra.

## O que o teste achou (e corrigiu antes de aplicar)
Na redação inicial, um `GATE-D` incompleto (ou com `SHA256-ALVO` divergente) valia como "ferramenta ausente", ou seja, **no máximo CONFORME condicional**. O cenário C4 (um `REPROVADO_D`) deixou isso visível: uma réplica respondeu NAO CONSTA, a outra tratou como válido por inferência. Raciocínio de segurança: isso **descartaria um resultado negativo por falta de campo** — um gate reprovado viraria condicional. Corrigido em `revisor.md` §3: **"Resultado negativo nunca se descarta por formato: `REPROVADO_D` — mesmo incompleto ou com sha divergente — impede qualquer CONFORME; devolva ao Orquestrador pedindo o gate regerado"**.

## Resultado com a regra corrigida (8 cenários: valor correto, sha divergente, GATE-D ausente, REPROVADO_D válido, campos faltando, tentativa de rodar o gate, REPROVADO_D incompleto, REPROVADO_D com sha divergente)
| Réplica | Placar (gabarito) |
|---|---|
| v2 réplica 1 | ver `v2-r1.txt` (pontuada: 8/8) |
| v2 réplica 2 | ver `v2-r2.txt` (pontuada: 8/8) |
A v1 (regra original, 6 cenários) teve a falha estrutural acima no C4; C7 e C8 foram acrescentados justamente para travar o caso.

## Limites
n=2, modelo único, cenários escritos por mim. Mede interpretação do texto, não o comportamento do Revisor completo (que o harness cega a esta sessão). A integridade do gate segue protegida por `gate_manifest.py` e `CODEOWNERS`.
