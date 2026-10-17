# DHR-ROTEAMENTO-002 — Ata — Troca do modelo do Especificador SOT de claude-opus-4-8 para claude-opus-5-5 (ordem expressa, teste posterior)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "Quero trocar para o opus 5.5 agora")**. O merge desta ata por Andraus é a ratificação. **Altera só a linha `model:` de `.claude/agents/especificador.md`.** Não toca `revisor.md`, `AGENTS.md`, `canon/`, método, regra nem decisão aberta. |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert` (ou restaurando `model: claude-opus-4-8`). |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda o modelo declarado no frontmatter do Especificador; nao altera o texto de instrucoes, checklist, metodo nem regra. |

## 1. Decisão `[FATO]`
Andraus ordena trocar **agora** o Especificador para `claude-opus-5-5` (preço 0,8 do Opus 4.8; proposta `AUDITORIA-ROTEAMENTO-MODELOS_PROPOSTA.md` §8.2/§9). Esta ata **excepciona** a sequência da DHR-ROTEAMENTO-001 (D5/D6: formalização e frontmatter só após a onda 1) **por decisão expressa de Andraus**, e não a revoga: as demais decisões D1–D4 continuam.

## 2. Risco aceito e salvaguarda `[FATO]`
- **Sem evidência prévia** de não-inferioridade do 5.5 no Especificador. O Revisor titular (Sonnet 5.5) e o gate D continuam sendo a barreira: nada vira baseline sem Revisor + homologação.
- **Teste A passa a ser verificação posterior**, com o desenho da DHR-ROTEAMENTO-001 §3 (≥3 repetições, zero perda em Crítico/Alto, sem aumento de falso alarme, métrica = tokens por defeito confirmado), executado só com ordem expressa e limite de cota de Andraus.
- **Reversão:** se o Teste A (ou qualquer revisão) mostrar perda em Crítico/Alto atribuível ao modelo, volta-se a `claude-opus-4-8` por nova ata. O Revisor **não** muda (`claude-sonnet-5-5`, DHR-AUDITOR-EXTERNO-014).
- `effort` não é definido aqui (D6 mantida: só após a varredura de esforço).

## 3. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.**

## 4. Registro
- [x] Esta ata · [x] `model:` do Especificador · [ ] merge (assinatura) · [ ] RPSA (carimbo do Especificador) · [ ] Teste A posterior

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
