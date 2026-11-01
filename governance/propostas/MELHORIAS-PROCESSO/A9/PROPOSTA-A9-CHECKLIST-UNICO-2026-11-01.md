# Proposta A9 — Checklist duplicado entre Especificador e Revisor (medida antes de cortar)

> **Não normativo. Estado atualizado em 2026-11-01: A9-teste APLICADO por ordem de Andraus (DHR-A9TESTE-001); A9-completo NÃO decidido.** Texto original: PROPOSTA — NADA APLICADO. Fonte: `AUDITORIA-BUROCRACIA-E-HIGIENE-2026-10-31.md` §A9. Editar `.claude/agents/*` (reservados) exige ordem de Andraus, ata e carimbo RPSA. Não fecha decisão aberta (CONS-01).

## 1. Medição ao vivo (HEAD `e3c2e95`)
| Item | Dado |
|---|---|
| `revisor.md` / `especificador.md` | 424 / 336 linhas |
| Revisor, Passos 0–8 (§5) | 185 linhas |
| Especificador, Autopré-check §7 + §7-bis | 102 linhas; invariantes §8: 19 linhas |
| Invariantes reescritos em mais de um arquivo vivo | "ICT NÃO cria hipótese", "Custo NUNCA entra no Conviction Vector", "Sem baseline informal": **4 arquivos** (`AGENTS.md`, `atomic-spec.md`, os dois agentes); "Versionamento monotônico" e "dimensionalidade": **5** (+ `ROADMAP.md`) |
| Lado Especificador já legível por máquina | `PRE-ENTREGA/autoprecheck_catalogo.json`: **31** itens (16 D, 15 ATESTADO) — proposta, não instalada |
| Lado Revisor legível por máquina | não existe |

## 2. Evidência de deriva (o custo real da duplicação)
- `revisor.md:162` ainda diz "SOT não executa ordem — **produz TMP**" (AGENTS §6.9 / EUA-E19a: o produto é o Signal Package). O mesmo erro estava no Especificador e só foi corrigido hoje (`DHR-PRE-ENTREGA-001`).
- `especificador.md:96` ainda diz "Constitution Check (**CC-01..CC-10**)". **Eu mesma deixei passar no P-F** (corrigi só a linha do §7); o teste abaixo é que achou.
- Antes: lista de decisões abertas copiada de `AGENTS.md §7` para ordens de serviço, contra o ROADMAP (achado C08, parecer SPEC-020).
**Correção minha:** na proposta P-B eu escrevi "32 caixas"; o catálogo tem **31** (16 D + 15 ATESTADO). Corrigi o documento.

## 3. Pré-teste (feito, nada instalado)
`tests/test_agentes_sem_fatos_defasados.py` (estava em `A9/` na proposta; movido ao ser aplicado, DHR-A9TESTE-001): 2 testes; lista fechada de 5 frases defasadas, cada uma com a autoridade que a corrigiu, mais um teste de mutação (o detector não pode ficar mudo). Resultado: **no estado atual falha em 2 linhas** (`revisor.md:162`, `especificador.md:96`); **com `PATCH-AGENTES-FATOS-DEFASADOS-2026-11-01.patch` aplicado numa cópia, passa** (patch: `git apply --check` OK; originais restaurados).

## 4. Opções
| Opção | Ganho | Risco/custo |
|---|---|---|
| **A9-teste** (este pré-teste) | Impede reincidência dos 5 fatos já conhecidos, sem mecanismo novo (é só um teste do CI) e sem reescrever os agentes além de 2 linhas | Baixo. Pega **só deriva conhecida**; deriva nova exige acrescentar a frase. Edita 2 arquivos reservados (2 linhas) → ata curta + carimbo RPSA |
| **A9-completo** (checklist único D/H, agentes citam IDs) | Elimina a causa (texto repetido) | Alto: reescreve ~290 linhas de dois agentes reservados; exige calibração; o ganho em tokens por rodada **não foi medido**. Seu insumo (catálogo AP) só será validado na medição do próximo Plan |
| Não fazer | 0 | Deriva continua (2 casos achados hoje em 760 linhas) |

## 5. Recomendação
**A9-teste agora; A9-completo só depois da medição do próximo Plan** (a mesma que decide instalar P-B/C-4 e mede o P10). Para instalar o A9-teste: ordem de Andraus; aplicar o patch aos dois agentes; mover o teste para `tests/`; ata curta (modelo A7-lite) com `RPSA-escopo: sim` e carimbo.

## 6. Declarado
Lista de 5 frases escolhida por mim a partir de decisões já registradas (AGENTS §6, DHR-SPEC003-001, EUA-E19a); outras derivas existentes podem não estar nela. Contagem de arquivos por `grep` literal (variações de redação não contam). Não medi tokens por rodada economizados.
