# Proposta pré-testada — LEDGER-ACHADOS.md: gerado, não versionado

> **Não normativo. PROPOSTA — NADA APLICADO.** Terceira frente da Camada A (Andraus, chat 2026-11-01: "proposta pré-testada do ledger"). Aplicar exige ordem expressa dele; a regra está em `AGENTS.md` §12 passo 2 (mudança por ata). Não fecha decisão aberta (CONS-01).

## 1. Diagnóstico
- `governance/aprendizado/LEDGER-ACHADOS.md` (155 linhas) foi alterado 28 vezes em 30 dias na `main`. Todo parecer novo obriga a regerá-lo e commitá-lo (`AGENTS.md` §12.2), então toda sessão que recebe parecer toca o mesmo arquivo.
- `loop_ledger.py` é **função pura** dos pareceres (`governance/**/PARECER*.md`, `parecer-revisor-*.md`) e de `CAUSAS-PREVENCAO.md`/`RETROSPECTIVAS.md`: "mesma entrada ⇒ mesmo texto", sem relógio nem aleatoriedade. Os pareceres já são **um arquivo por parecer** — são os fragmentos naturais; o ledger é só a agregação.
- Logo, conflito no ledger nunca é semântico: sempre se resolve regerando. Fragmentar por sessão (a ideia original da Camada A, item 3) seria desnecessário e criaria um segundo formato.

## 2. Proposta
1. `git rm --cached governance/aprendizado/LEDGER-ACHADOS.md` e `.gitignore` do arquivo (mesmo padrão do `mapa-projeto.json`, A2.1).
2. Nenhum script muda: `loop_ledger.py` gera sob demanda (`--stdout`/padrão) e `--retro-check` já não lê o ledger.
3. `AGENTS.md` §12 passo 2: trocar "rodar e commitar o ledger" por "o ledger é gerado; o parecer é a fonte" (ata de Andraus). O passo 4 (3 categorias recorrentes no HANDOFF) continua usando a saída do script.
4. `loop_ledger.py --check` perde sentido enquanto o arquivo não é versionado; não existe chamada dele em `ci.yml`/hooks (verificado por busca), então nada quebra.

## 3. Pré-teste (`TESTE-LEDGER-gerado-vs-commitado.sh`, repositório temporário, scripts e pareceres reais)
Dois ramos, cada um com um parecer diferente da SPEC-048 (R3 e R4) e o ledger regerado:
| Modelo | Resultado |
|---|---|
| A) ledger **commitado** (atual) | `CONFLICT`: `governance/aprendizado/LEDGER-ACHADOS.md` |
| B) ledger **gerado, não versionado** | merge limpo; duas gerações idênticas (determinístico); o ledger regerado contém os achados dos **dois** pareceres |

## 4. Limites e riscos
- Quem lê o ledger no GitHub passa a precisar gerá-lo (`python scripts/loop_ledger.py --stdout`). A informação continua inteira nos pareceres.
- Teste usa 2 pareceres reais, não o conjunto completo; o determinismo vale para o conjunto por construção do script, mas não foi medido em todos os ~19 pareceres.
- Mesmo padrão do mapa (`PROPOSTA-CAMADA-A-2026-11-01.md` §3): trocar arquivo versionado por geração sob demanda muda uma regra do `AGENTS.md`, por isso depende de ata.

## 5. Para aplicar (por ordem de Andraus)
1. `git rm --cached` + `.gitignore`; 2. suíte; 3. ata + ajuste do `AGENTS.md` §12.2; 4. `governance/MECANISMOS.json` (nota de `loop_ledger`, COE-14).
