# DHR-AUDITOR-EXTERNO-014 — Ata — Revisor SOT: modelo elevado e Passo 4-ter (inventário e conferência de afirmações)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-12 |
| Status | **PROPOSTA**, preparada por escolha de Andraus em chat (2026-10-12: "Propor modelo novo + método V2"); a assinatura é o merge do PR. Altera `.claude/agents/revisor.md`. Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07): um passo novo (4-ter) e a troca de uma linha de configuração; reversível por `git revert`. |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Altera o arquivo do Revisor: eleva o modelo do frontmatter (revertendo o roteamento economico da EUA-E19) e acrescenta o Passo 4-ter ao protocolo de revisao; o Especificador nao e afetado. |

## 1. Origem `[FATO]`
Medição do Revisor na SPEC-006 (Plan v1.0/v1.1/v1.2, 2026-10-11/12): o Revisor titular (modelo `claude-sonnet-4-6`, fixado na EUA-E19 por custo) deu CONFORME condicional nas três rodadas (4, 4 e 2 achados Menores); um revisor de controle independente deu NÃO CONFORME (22, 27 e 18 achados) e o Orquestrador confirmou no repositório os achados que usou como gabarito, sem falso alarme.

## 2. Teste de regressão (v1.0 congelada, gabarito de 18 defeitos confirmados) `[FATO]`
| Braço | Modelo | Método | Achou (de 18) | Veredito |
|---|---|---|---|---|
| Revisor titular (original) | sonnet-4-6 | atual | 0 | CONFORME condicional |
| B | modelo mais novo | atual | 14 | NÃO CONFORME |
| C | claude-sonnet-5-5 | V2 (este Passo 4-ter) | 16 | NÃO CONFORME |
| D | claude-sonnet-5-5 | V2, sem checks.md nem autoavaliação do Especificador | 14,5 | NÃO CONFORME |
Leitura: o salto veio do modelo; o método V2 soma ~2 defeitos (dentro do ruído de uma execução); retirar o `checks.md` não melhorou o resultado.
**Replicação nas versões v1.1 e v1.2 do Plan (mesmo método V2 + modelo novo; gabarito de 13 e 11 defeitos confirmados):** v1.1 → 8 de 13; v1.2 → 9 de 11. O Revisor original (modelo antigo, método atual) tinha achado 0 de 13 e 1 de 11 (um Menor "ambíguo"). **Placar consolidado sobre as 3 versões (42 defeitos):** original 1 (≈2%) × modelo novo + V2 33 (≈79%). Custo: ≈275–280 mil tokens e ~50 chamadas por revisão (original ≈120–138 mil e ~20). Perdas recorrentes: campo/linha/ID citado que não existe (cobertos em parte pelos detectores do PR #94) e omissões de obrigação do CEM-001.
**Variância (v1.0, mesmo braço C repetido 3×):** 16, 17 e 16 de 18 (média ≈ 91%, amplitude 1) — resultado estável nesta Spec; o defeito que escapa sempre é a ausência do tipo `observation` no nó.
**Limites:** uma Spec; uma execução por braço; gabarito derivado do controle (mesma família de modelo → possível circularidade); a versão exata do modelo do braço B não foi confirmada; o gabarito não é exaustivo.

## 3. O que muda `[FATO]`
1. Frontmatter: `model: claude-sonnet-4-6` → `claude-sonnet-5-5` (comentário atualizado com a evidência). Custo: cerca de 2× tokens por revisão (120–230 mil); 4Es: Eficácia > Economicidade.
2. §0: a nota de esforço deixa de dizer que o esforço compensa o modelo econômico.
3. **Passo 4-ter (obrigatório, antes do Passo 5):** M1 inventário de afirmações (atribuição, estado/contagem, cobertura, resolução, norma herdada) com tabela "afirmação | fonte aberta | resultado" no relatório; M2 passe de contradição interna; M3 obrigações herdadas (representável e verificável?); M4 fronteiras com Specs vizinhas; M5 postura (PASS só com evidência aberta nesta sessão; "✔" do Plan não é evidência).
Nenhuma ferramenta é acrescentada ao Revisor (Write/Edit/Bash seguem ausentes; ENF-03 intacto).

## 4. Reversão `[PROPOSTA]`
`git revert` do commit deste PR restaura o modelo e remove o Passo 4-ter. O RPSA realinha o carimbo pela ata de reversão.

## 5. Classificação RPSA desta ata
Declarada no cabeçalho (`sim` / `propagado`): altera o protocolo embutido no Revisor. Após o merge, `rpsa_auto` registra a classificação e alinha os carimbos `sincronizado-até` de `revisor.md` e `especificador.md`.

## 6. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 7. Registro
- [x] Esta ata · [x] `.claude/agents/revisor.md` · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [x] replicação v1.1/v1.2 anexada · [ ] merge (assinatura) · [ ] RPSA automático · [ ] verificação em sessão nova (o modelo novo só vale numa sessão aberta depois do merge)

---

**Andraus** — *escolha em chat, 2026-10-12; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
