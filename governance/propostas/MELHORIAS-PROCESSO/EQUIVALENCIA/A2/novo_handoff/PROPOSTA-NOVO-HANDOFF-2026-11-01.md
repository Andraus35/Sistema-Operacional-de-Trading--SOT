# Proposta pré-testada — `novo_handoff` (utilitário do ritual de handoff)

> **Não normativo. NADA INSTALADO** (os arquivos desta pasta não estão em `scripts/` nem em `MECANISMOS.json`). Pré-teste autorizado por Andraus (AskUserQuestion, 2026-11-01). Instalar exige nova ordem dele e `MECANISMOS.json` no mesmo PR (COE-14). Não decide conteúdo do handoff, não fecha decisão aberta (CONS-01).

## O que faz (só passos mecânicos, atômico)
Copia o `HANDOFF.md` atual byte a byte para `docs/handoffs/HO-<id>.md` (ou `ramo-<ramo>/` com `--ramo`), troca `handoff_id` (+1, data nova), `previous`, `data` e `base_commit`, e aplica trocas de texto `--trocar 'ANTIGO=>NOVO'`. **Recusa sem escrever nada** (exit 2) se: a âncora existir 0× ou mais de 1×; a cópia já existir e divergir; o frontmatter faltar; o id for inválido.

## Por que existe
Erros desta sessão, todos mecânicos e todos pegos por gate antes da `main`: `HO-04` por editar o handoff sem trocar o id; cópia arquivada diferente da versão commitada; `replace` em Python que não achava o texto e **não avisava**; cadeia colidindo entre ramos. O utilitário elimina esses passos manuais; o conteúdo do handoff continua sendo do Orquestrador.

## Pré-teste
- `test_novo_handoff.py`: **8 testes OK** (id/previous/data/base, cópia exata, âncora ausente e repetida sem escrita, cópia divergente recusada, `--ramo`, frontmatter/id inválidos, largura do número).
- **Mutantes: 4 de 5 mortos.** O M4 ("reescreve a cópia mesmo existindo") **sobrevive e é equivalente**: só ocorre quando a cópia existente é idêntica (a divergente já é recusada antes), então o resultado observável é o mesmo.
- Fumaça com o `HANDOFF.md` real em cópia: só as 4 linhas do frontmatter mudam; cópia byte a byte; âncora ausente → exit 2.
- Usado de verdade para gravar o handoff HO-162 desta entrega.

## Limites declarados
Não roda `build_map`/`check_handoff` sozinho (imprime o comando). Não resolve conflito de merge do handoff nem escolhe a cadeia (`--ramo` é decisão do chamador). Não testado em Windows. `base_commit` vem de `git rev-parse --short HEAD` se não for passado.

## Para instalar (por ordem de Andraus)
Mover os 2 arquivos para `scripts/` e `tests/`, ligar o teste ao CI, registrar `util.novo-handoff` em `MECANISMOS.json`, atualizar o texto do §11 do `AGENTS.md` só se ele quiser (reservado).
