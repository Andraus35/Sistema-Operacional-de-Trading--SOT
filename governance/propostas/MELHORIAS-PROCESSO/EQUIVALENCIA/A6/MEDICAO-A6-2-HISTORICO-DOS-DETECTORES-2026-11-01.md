# Medição A6.2 — o que os detectores acharam nos últimos 30 merges da `main`

> **Não normativo. Medição; NENHUM mecanismo criado ou alterado.** Andraus escolheu o A6.2 como próxima frente (AskUserQuestion, 2026-11-01). Antes de criar um contador permanente, medi o passado: `historico_detectores.py` (esta pasta) roda 7 detectores em `git worktree` de cada um dos 30 últimos merges (`--first-parent`, 2026-10-18 → 2026-10-31); dados brutos em `HISTORICO-DETECTORES-30-MERGES-2026-11-01.json`. Não fecha decisão aberta (CONS-01).

## 1. Resultado (30 merges)
| Detector | Mudou de resultado | Com achado | Com ERRO | Leitura |
|---|---:|---:|---:|---|
| `check_refs` | 3 | **30/30** (WARN 1–7) | 0 | aviso permanente, nunca ERRO |
| `check_doc_sync` | 3 | 25/30 (WARN 1–2) | 0 | aviso quase permanente |
| `check_handoff` | **9** | 9/30 | **4** | o mais ativo; pegou erro real |
| `check_coesao` | 4 | 2/30 | 0 | raro |
| `check_rpsa` | 2 | 1/30 | 0 | raro (1 divergência) |
| `check_invariants` | 0 | 0/30 | 0 | silencioso |
| `gate_manifest` | 0 | 0/30 | 0 | silencioso |

## 2. O que isso muda na proposta A6.2
1. **"Sem achado em N execuções → aposentar" está errado para sentinelas.** `check_invariants` e `gate_manifest` ficaram 30/30 sem achado, e esse é o resultado **esperado** de um gate que funciona (ele só dispara se alguém alterar o selo ou um valor fixo). Uma regra de caducidade por silêncio os aposentaria justamente quando estão cumprindo o papel. Caducidade só faz sentido para **detectores de drift informativos**, e mesmo nesses o silêncio é bom sinal, não prova de inutilidade.
2. **O problema real é o inverso: aviso que nunca muda.** `check_refs` (30/30) e `check_doc_sync` (25/30) mostram o mesmo conjunto de avisos por semanas. É fadiga de alerta, e é o que o A6.4 já atacou no hook de `doc-sync`. Falta o mesmo para o `check_refs` (hoje sem hook; aparece no CI e nos relatórios) e tratar a causa: corrigir ou aceitar os avisos históricos.
3. **Contador permanente não se justifica agora.** Exigiria guardar histórico (custo de arquivo/commit, o mesmo churn que o A2 removeu) para responder uma pergunta que o `git` + este script já respondem sob demanda em ~5 min.

## 3. Limites declarados
- Amostra de merges: o estado **depois** de cada merge. Achados que a sessão corrigiu antes de mesclar não aparecem, então os detectores "silenciosos" podem ter agido antes do merge (subestima a utilidade deles).
- 30 merges em 13 dias; um detector raro pode não ter disparado neste período.
- Contagens `E<n>W<n>` são as do próprio detector; `exit0/exit1` para os que não imprimem contagem.
- Não medi tempo por detector nem custo de tokens.

## 4. Recomendação (decisão de Andraus)
**Reformular o A6.2:** não criar contador; manter `historico_detectores.py` como utilitário de proposta (sob demanda). Caducidade, se vier, só para detectores de drift informativos e baseada em "mesmo conjunto de avisos por N merges" (já é o A6.4), nunca em silêncio. Próximo corte de maior retorno: tratar os avisos permanentes do `check_refs` e `check_doc_sync`.
