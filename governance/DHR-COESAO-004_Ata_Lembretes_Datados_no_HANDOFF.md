# DHR-COESAO-004 — Ata — Lembretes datados no HANDOFF (HO-10) para que melhorias combinadas não se percam entre sessões

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "Vamos conforme sua sugestão. Só temo esquecer de dar melhorias… tem alguma sugestão para isso não ocorrer em uma nova sessão?")**. O merge desta ata por Andraus é a ratificação. Não fecha nem abre decisão aberta (CONS-01). |
| Compatibilidade | Aditiva (INV-07). Acrescenta uma checagem informativa ao detector do HANDOFF; não altera `AGENTS.md`, agentes, hooks nem selo. Reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Acrescenta apenas a checagem HO-10 ao detector check_handoff.py e lembretes no HANDOFF; nenhum arquivo de agente, checklist, metodo nem regra e alterado. |

## 1. Problema e decisão `[FATO]`
Melhorias combinadas em chat (proteger a `main`, assinar o registro de mecanismos) dependem de alguém lembrar numa sessão nova. Decisão: **tornar o lembrete um dado verificável**, não memória. Linha do `HANDOFF.md` com `[PRAZO: AAAA-MM-DD]` passa a gerar **HO-10 (WARN)** quando a data chega; como o hook `SessionStart` já exibe os WARN/ERRO do `check_handoff.py` a cada abertura de sessão, o lembrete reaparece sozinho até a linha ser resolvida (apagada) ou remarcada. É **Detector, não Gate** (ENF-03): nunca bloqueia, nunca decide.

## 2. Lembretes criados nesta ata (HANDOFF HO-28 §10)
Proteger a `main` exigindo só o CI — 2026-10-18 · assinar o registro de mecanismos como VIGENTE se não houver falso alarme — 2026-10-24 · proteção com revisão de dono (com bypass de administrador) — 2026-10-31. As ações em *Settings* e a assinatura do registro seguem **só de Andraus**.

## 3. Efeitos e limites
`scripts/check_handoff.py` (HO-10, `--hoje` para testes) e `tests/test_check_handoff.py` (+1); HANDOFF. Limite: só funciona se o Orquestrador mantiver os `[PRAZO]` no HANDOFF a cada reescrita (o `check_handoff` já exige reescrita quando há defasagem, HO-03). Sessão sem hooks (outra ferramenta) não vê o aviso automático, mas o HANDOFF continua sendo lido por regra (`AGENTS.md` §11).

## 4. Permanecem ABERTAS (CONS-01)
Nenhuma decisão aberta fechada ou aberta; o estado é o do `ROADMAP.md`.

## 5. Registro
- [x] Esta ata · [x] detector HO-10 · [x] lembretes no HANDOFF · [ ] merge de Andraus (ratificação)

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
