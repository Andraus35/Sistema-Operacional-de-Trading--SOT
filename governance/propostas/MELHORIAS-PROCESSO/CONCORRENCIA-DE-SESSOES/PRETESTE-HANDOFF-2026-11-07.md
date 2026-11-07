# Pré-teste da regra do handoff (nada aplicado)

> **Não normativo. RESULTADO DE PRÉ-TESTE.** Andraus aprovou a direção e autorizou o pré-teste (chat, 2026-11-07). Proposta: `../PROPOSTA-HANDOFF-ENTRADA-E-CICLO-DE-VIDA-2026-11-06.md`. Aplicar `AGENTS.md` §11 ou instalar M1/M2 exige ordem expressa dele e ata. Não fecha decisão aberta (CONS-01).

## 1. Resultados (repositório temporário e worktree da `main`; scripts reais)
| # | Cenário | Resultado |
|---|---|---|
| S1a | 2 ramos, cada um cria só o próprio `handoffs/<ramo>.md` | merge **limpo** |
| S1b | 2 ramos, cada um **acrescenta uma linha no fim da tabela** do índice da raiz (R1 como escrita) | **CONFLITO** em `HANDOFF.md` |
| S1c | 2 ramos inserem a linha em posições **não adjacentes** | merge limpo (frágil: adjacentes conflitam) |
| C1 | raiz estática, **ramo novo sem handoff próprio** | `check_handoff` ERRO=0, `WARN HO-03` (empurra a criar o arquivo próprio) |
| C2 | ramo com `handoffs/<ramo>.md` e ID no formato novo | ERRO=0, sem aviso |
| C3 | `handoffs/` de ramo morto presente | **nenhum aviso hoje** (falta o M1) |
| M1/M2 | protótipo HO-16 (ramo morto) e HO-17 (formato do ID), só INFO | `tests.test_check_handoff` **31/31**; **4 mutantes mortos**; `gate_manifest` íntegro; `git apply --check` limpo na `main` |
Efeito do protótipo na `main` real: `HO-16` e `HO-17` acusam só `handoffs/ccr-4bd4e8a0-d92lc7.md` (ramo morto, ID antigo `HO-2026-11-01-152`); ERRO=0.

## 2. O que muda na proposta (correção)
**R1 estava errada num ponto:** a "tabela de frentes ativas" na raiz **ainda conflita** (S1b). Recomendação revista: **a raiz não lista frentes**. Ela vira texto estático curto ("o estado de cada frente é um arquivo em `handoffs/`; use `ls handoffs/`") + o roteiro "Reverificar ao vivo". Quem abre ramo novo cria só o próprio arquivo; nenhum arquivo compartilhado é editado. O `WARN HO-03` do C1 já serve de empurrão. Descoberta por `ls handoffs/` (e o `SessionStart` pode listar, sem arquivo gerado). M3 (índice gerado) deixa de ser necessário.

## 3. Patch (proposto, **não instalado**)
`PATCH-HO16-HO17-check-handoff-2026-11-07.patch` (`scripts/check_handoff.py` + 3 testes). Para aplicar: ordem de Andraus; `git apply`; suíte completa; `governance/MECANISMOS.json` (COE-14).

## 4. Limites
- HO-16 usa os refs `heads` e `remotes/origin` do clone: em clone raso ou sem fetch pode acusar ramo vivo; por isso é só INFO.
- Não testei o hook `SessionStart` em ramo novo na nuvem real, só o `check_handoff` por linha de comando.
- Migrar o `HANDOFF.md` atual da raiz (frente de logs/pauta) para handoffs/ccr-a79e19ef-2zl738.md (arquivo ainda a criar) mexe no trabalho de outra sessão: combinar antes.

## 5. Decisões que cabem a Andraus
1. Texto da §3 da proposta no `AGENTS.md` §11, **já com a R1 revista** (ata). 2. Instalar M1/M2 (patch). 3. Migrar a raiz para índice estático.
