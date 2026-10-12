# DHR-ASSINATURA-001 — Ata — A assinatura de Andraus passa a ser a decisão registrada no chat, não o merge

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-12 |
| Status | **PROPOSTA preparada a pedido de Andraus.** É mudança de governança: **só vale com a ordem expressa de Andraus** ("mescla o #N" ou equivalente no chat) — exatamente o tipo de mudança que esta própria ata mantém sob decisão dele. Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07): atas anteriores permanecem como estão; a regra vale daqui em diante. Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Altera convencao de governanca (quem assina e como) e o AGENTS.md; nenhum texto de arquivo de agente e alterado. |

## 1. Origem `[FATO]`
Andraus, em chat (2026-10-12): *"A ideia do Merge ser minha assinatura se justificava quando havia auditor externo. Agora que não é mais necessário podemos reverter isso."* O auditor externo está **pausado** (DHR-AUDITOR-EXTERNO-007). Perguntado sobre o alcance, escolheu: **"Delegar o operacional, manter decisões com você"**.

## 2. Regra nova `[PROPOSTA]`
1. **Assinatura = decisão de Andraus registrada no chat e citada na ata** (data + trecho). O **merge deixa de ser assinatura**. Novas atas citam a decisão no campo de assinatura; o texto "Assinatura = merge" das atas anteriores é histórico e fica como está (INV-07).
2. **O Orquestrador pode mesclar, sem nova ordem, e informar Andraus depois**, quando **todas** as condições valerem: (a) o conteúdo é **operacional** — scripts de apoio, testes, mapa gerado, atas de registro de decisão que Andraus já tomou no chat; (b) Andraus **aprovou expressamente aquele conteúdo** no chat (escolher "propor" não é aprovar); (c) CI verde na cabeça do PR; (d) sem conflito não resolvido; (e) o PR é o meio (nada de push direto à `main`) — mantém histórico, CI e o registro automático do RPSA.
3. **Continuam só por decisão expressa de Andraus no chat**, citada na ata: homologação de Spec ou baseline; qualquer mudança em `AGENTS.md`, `.claude/agents/*.md`, `governance/` normativo (CONSTITUTION, RULES, CONFLICT-MAP), `canon/`, `ROADMAP.md` e `atomic-spec.md`; fechar ou abrir decisão aberta (CONS-01); mudar esta regra.
4. **Freios:** o Orquestrador confere CI e `check_rpsa` depois de cada merge e relata a Andraus; se algo falhar, reverte (`git revert`) e avisa. A ata de qualquer mudança mesclada cita a decisão de Andraus que a autoriza; **sem decisão citada, não se mescla**.
5. O registro automático do RPSA continua rodando no merge; a **autoridade** da classificação declarada na ata passa a ser a decisão de Andraus citada nela (não o ato de mesclar).

## 3. Efeitos sobre o que está em aberto `[FATO]`
Os PRs #94/#95 (Revisor reforçado) mudam `.claude/agents/revisor.md`: **item 3 desta regra — não são delegados**; seguem aguardando "mescla o #95". Esta ata também: só entra com a ordem de Andraus.

## 4. Reversão `[PROPOSTA]`
`git revert` do commit deste PR restaura "assinatura = merge" como convenção (nota do `AGENTS.md` §10 removida).

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 6. Registro
- [x] Esta ata · [x] `AGENTS.md` §10 (nota) · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] ordem expressa de Andraus (vigência) · [ ] RPSA automático (sem escopo de agente)

---

**Andraus** — *decisão e escolha de alcance em chat, 2026-10-12; registro pelo Orquestrador interno. Vigência = ordem expressa de Andraus.*
