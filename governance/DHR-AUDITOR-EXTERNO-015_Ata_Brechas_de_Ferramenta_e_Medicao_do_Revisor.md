# DHR-AUDITOR-EXTERNO-015 — Ata — Brechas de ferramenta dos subagentes de revisão, selo do gate e medição do Revisor no banco de estresse

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-17: "Fechar as duas brechas e rodar o banco de estresse")**. O merge desta ata por Andraus é a ratificação. Altera `.claude/agents/sot-spec-reviewer.md` e `sot-schema-validator.md` (só o campo `tools`), `scripts/revisor_gate_mcp.py` e adiciona um selo de integridade. **Não altera `revisor.md`, `especificador.md`, método, regra nem decisão aberta.** |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert`. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Restringe ferramentas de dois subagentes auxiliares e adiciona selo de integridade aos scripts do gate; nao altera o texto do Revisor nem do Especificador, checklist, metodo nem regra. |

## 1. Origem `[FATO]`
Auditoria do Revisor (2026-10-17): o Revisor SOT não tem Bash/Write/Edit (decisão de Andraus, DHR-009 §1, mantida na DHR-014). Duas brechas ao redor dele ficaram abertas: (a) `sot-spec-reviewer` e `sot-schema-validator` não declaravam `tools` e herdavam todas as ferramentas, Bash e Write incluídos; (b) os scripts do gate que julgam o trabalho do Especificador ficam no mesmo repositório em que ele tem Write/Edit.

## 2. O que muda `[FATO]`
1. **Subagentes somente leitura:** `tools: Read, Grep, Glob` nos dois (ENF-03).
2. **Selo de integridade do gate:** `scripts/gate_manifest.py` + `governance/GATE-MANIFEST.sha256` (sha256 de 10 scripts do gate). `revisor_gate_mcp.py` **recusa rodar** se um script diferir do selo ou o selo faltar (falha fechada); o CI reprova o mesmo caso (`gate_manifest.py --check`, bloqueante, passo independente do servidor).
3. **`.github/CODEOWNERS`:** scripts do gate, selo e `.claude/agents/` com Andraus como dono.
4. **Testes:** `tests/test_gate_manifest.py` (selo, fim de linha, e trava que impede `tools` ausente/escrita/Bash nos três revisores) e 2 casos novos em `tests/test_revisor_gate_mcp.py`. 32 testes passam.
**Limites declarados:** o selo **detecta**, não impede; quem altera script e selo no mesmo commit só é pego pela revisão do diff. O efeito de bloqueio do CODEOWNERS depende de "Require review from Code Owners" na proteção da `main` (configuração do repositório, ato de Andraus, **não** feita aqui). Regravar o selo (`gate_manifest.py --write`) exige decisão expressa de Andraus (AGENTS.md §10); `AGENTS.md` §8 **não** foi editado (não pedido).

## 3. Medição do Revisor no banco de estresse `[FATO: execução de 2026-10-17]`
Banco: `origin/ferramentas-estresse` (`tools-estresse/`, gerador + conferidor; 45 slots em 3 documentos). Semente sorteada pelo Orquestrador (sha256 do gabarito: `1bb06addf8ff59c43e180446da980e1b70681e5d27159d560aaab483887b5a3e`); **30 defeitos** (NUM 5 · REF 4 · REG 9 · SEM 12) e **15 iscas limpas**; **0 defeitos escritos por Andraus**. Revisor SOT (`claude-sonnet-5-5`) chamado 3× em sessões separadas, mesmo prompt. Gabarito, semente e respostas **não** foram para o repositório.
- `score.py` (padrão do banco): **30/30 nas 3 rodadas**, iscas tocadas 14/15, 9/15, 14/15. **Esse número está inflado e não é o resultado:** os documentos têm 99 linhas e os relatórios citam quase todas (inclusive linhas que declaram "conferido e OK"); 8 dos 30 defeitos têm texto defeituoso curto (<12 caracteres) e só casam por linha.
- Medida mais estrita (texto defeituoso transcrito **e** linha citada): **20, 17 e 18 de 30** (≈ 57–67%); só linha citada: 28–29 de 30; só texto defeituoso transcrito: 19–21 de 30.
- Veredito nas 3 rodadas: NÃO CONFORME (Crítica) nos 3 documentos — correto, todos têm defeitos plantados.
- **Achado operacional (maior):** nas 3 rodadas o Revisor declarou **"GATE NÃO VERIFICADO — a ferramenta `revisor_gate` não está disponível nesta sessão"**. O servidor responde fora do agente (testado), mas **não carregou no Revisor invocado neste ambiente** (sessão em nuvem via ferramenta Agent). Falha fechada funcionou (o Revisor não fingiu o gate), porém o gate determinístico **não participou desta medição**; os documentos de teste, fora de `specs/features/<SPEC>/plan.md`, seriam recusados de qualquer modo (R1 aberto da DHR-008). Causa não diagnosticada; precisa de teste em sessão local do Claude Code.
- Outros limites: o Orquestrador sorteou a semente e conhece o conjunto de slots (viés declarado no `LEIA-ME`); sem defeitos de Andraus não há a parte livre do viés; um único conjunto de 3 rodadas; recall estrito ≈ 60% mede só este banco; relatórios dos 3 Revisores não leram `atomic-spec.md` integralmente (declarado por eles).

## 4. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001. **Nenhuma fechada por este ato.** Decisões pendentes de Andraus: ativar "Require review from Code Owners"; escrever 3–5 defeitos próprios e repetir o banco; diagnosticar por que o MCP do Revisor não carrega no ambiente em nuvem.

## 5. Registro
- [x] Esta ata · [x] `.claude/agents/sot-*.md` · [x] selo + CI + CODEOWNERS · [x] testes · [ ] merge (assinatura) · [ ] RPSA automático

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno. Assinatura = merge deste PR.*
