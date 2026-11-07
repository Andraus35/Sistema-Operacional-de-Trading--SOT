# Triagem dos ramos remotos antigos (nada apagado)

> **Não normativo.** Pedido de Andraus (chat, 2026-11-07). Medido com o **histórico completo** (`git fetch --unshallow`). **Correção:** os "101/175/120 commits à frente" dos avisos do hook e do meu relatório anterior vinham de clone **raso**; o `merge-base` das ramas antigas ficava vazio e o número inflava. Os valores abaixo são os reais. Decisão de apagar/arquivar é de Andraus; eu levo 403 em exclusão.

## Grupo A — contidos na `main` (0 commits exclusivos): apagar
`ccr-599f6762-60qbvg`, `claude/amazing-fermat-dnbjtz`, `ccr-60575b67-ffmqlh`, `ccr-f02efedf-w33g38`.
(Eram 2 na lista do hook; os outros 2 só aparecem como contidos com o histórico completo.)

## Grupo B — só handoff e mapa gerado, handoffs já arquivados na `main`: apagar
| Ramo | Commits | Conteúdo | Prova |
|---|---|---|---|
| `ccr-3235944c-duo3sl` | 1 | `HANDOFF.md` + mapa | HO-2026-10-25-87 existe na `main` |
| `ccr-166207a9-473jhk` | 1 | `HANDOFF.md` + mapa | HO-2026-10-31-94 existe na `main` |
| `ccr-1c561451-dsk356` | 6 | `HANDOFF.md` + mapa ("histórico já mesclado em #150") | HO-2026-10-31-128 existe na `main` |

## Grupo C — conteúdo próprio ou histórico: **tag `arquivo/<ramo>` antes de qualquer remoção**
| Ramo | Commits | O que tem de próprio | Observação |
|---|---|---|---|
| `ccr-3a0d581c-6cj4ig` | 2 | `TESTE-A-PROTOCOLO-4ES.md` (proposta de teste A pelas lentes dos 4Es) | **não está na `main`** |
| `ferramentas-estresse` | 1 | `tools-estresse/` (8 arquivos: gerador de defeitos e conferidor) | mensagem do commit: "NUNCA mesclar no main"; **não está na `main`** |
| `spec006-plan` | 10 | pareceres das rodadas 6/7 e Plan v1.6 candidato da SPEC-006 | a v1.7 (baseline) e a pasta `linha-spec006-plan` já estão na `main` |
| `ccr-e3c0fb7e-63d2l9` | 17 | Plan e homologação da SPEC-002, capturas verbatim da SPEC-003 | `SPEC-002/plan.md` existe na `main` em versão posterior; capturas a conferir |
| `auditor-externo-integracao` | 9 | piloto do Auditor Externo (51 arquivos) | Auditor arquivado em `docs/_legacy`; versões antigas |
| `spec-006-abertura` | 1 | `ABERTURA.md` da SPEC-006 (rascunho "PROPOSTA, não homologada") | 10 dos 13 arquivos já idênticos na `main`; a abertura homologada é posterior |

## Como executar (Termux, só com a sua decisão)
`arquivar-ramos.sh` (nesta pasta, sintaxe validada, **não testado contra o GitHub**): `bash arquivar-ramos.sh A`, `B` ou `C`. Pergunta ramo a ramo; no grupo C cria a tag e **só apaga se a tag conferir com o SHA**; no grupo A recusa ramo com commits exclusivos.
SHAs dos ramos do grupo C na data: `ccr-3a0d581c-6cj4ig` 62f8cac · `ferramentas-estresse` c345d8f · `spec006-plan` 0fbfb89 · `ccr-e3c0fb7e-63d2l9` 32d45b2 · `auditor-externo-integracao` ef7baa1 · `spec-006-abertura` 4a7d14e.

## Limites
Conteúdo "idêntico" foi medido por blob exato; um arquivo editado depois na `main` aparece como "diferente" sem ser perda. O grupo B depende do que a coluna "Prova" mostra (handoffs arquivados), não de leitura commit a commit.
