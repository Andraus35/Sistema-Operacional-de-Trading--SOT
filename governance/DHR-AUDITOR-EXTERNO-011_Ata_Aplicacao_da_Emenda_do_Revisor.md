# DHR-AUDITOR-EXTERNO-011 — Ata — Aplicação ao `.claude/agents/revisor.md` da emenda aprovada na DHR-AUDITOR-EXTERNO-010

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-11 |
| Status | **Aplicação autorizada por Andraus (chat, 2026-10-11: "aplique a emenda do Revisor").** O merge desta ata e do arquivo alterado é a ratificação. Executa **o texto já aprovado** na DHR-AUDITOR-EXTERNO-010 (merge de 2026-10-11); não inventa texto novo. Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07); reversível por `git revert` do commit de aplicação. |
| RPSA-escopo | sim |
| RPSA-sync | propagado |
| RPSA-motivo | Aplica ao revisor.md a emenda ja aprovada na DHR-AUDITOR-EXTERNO-010: o Revisor passa a usar a ferramenta revisor_gate (sem Bash, falha fechada) e muda o protocolo da secao 3 e o formato do relatorio; o Especificador nao e afetado. |

## 1. O que foi aplicado `[FATO]`
Os quatro trechos do `.claude/agents/revisor.md` **idênticos** ao texto "Depois" da DHR-010 §2 (22 linhas incluídas, 10 removidas): (1) frontmatter — `tools` ganha `mcp__sot-revisor-gate__revisor_gate` e o bloco `mcpServers` (servidor local `scripts/revisor_gate_mcp.py`); **Write, Edit e Bash seguem ausentes**; (2) §3 inteiro; (3) abertura do §4 (`PASSOU_D`); (4) item 3 do formato do relatório. **Prova por código:** os blocos "Depois" da ata 010 foram extraídos e comparados com o arquivo — o §3 completo (15 linhas), o frontmatter, o item do relatório e a linha do §4 são iguais ao texto aprovado. O restante do arquivo (modelo, esforço, Passos 0–8, interpelação, veredito, `required_sources`, carimbo `sincronizado-até`) **não foi tocado**.

## 2. Verificações já feitas `[FATO]`
Cabeçalho YAML válido (`tools`: `Read · Grep · Glob · mcp__sot-revisor-gate__revisor_gate`; `mcpServers` com um servidor `stdio`); nenhuma ferramenta de escrita ou terminal na lista; `npm test` (11/11 schemas) e `npm run lint` (20 aprovados, 5 pulados) sem regressão; `check_rpsa.py` em sincronia antes da aplicação. Servidor e gate: 12 testes de servidor + 10 testes de gate no CI; prova ponta a ponta com arquivo de agente real (DHR-009 §8).

## 3. Verificação pós-merge — OBRIGATÓRIA, em sessão nova `[PENDENTE]`
Agentes são lidos na abertura da sessão; este arquivo só vale numa sessão aberta **depois** do merge, na raiz do repositório e com a pasta confiável:
1. Chamar o **Revisor SOT** e pedir que liste as ferramentas: devem ser exatamente `Read · Grep · Glob · mcp__sot-revisor-gate__revisor_gate`.
2. Pedir `revisor_gate(spec="SPEC-001", rapido=true)`: esperado `PASSOU_D`, 0 sinais H.
3. Pedir uma chamada com `"SPEC-001 && echo x"`: esperado `RECUSADO`.
**Se qualquer item falhar** (ferramenta ausente, conexão caída, resposta inesperada): **reverter** — ver §4. Ferramenta ausente por pasta não confiável não é defeito do texto: o Revisor deve declarar **GATE NÃO VERIFICADO** e limitar o parecer a CONFORME condicional (é a regra de falha fechada).

## 4. Reversão `[PROPOSTA]`
`git revert <commit de aplicação>` restaura exatamente o texto anterior do `revisor.md` (o §3 antigo manda executar um script que o Revisor não consegue rodar — contradição conhecida, DHR-009 §2). O RPSA realinha o carimbo pela ata de reversão.

## 5. Classificação RPSA desta ata
Declarada no cabeçalho (`sim` / `propagado`): altera o checklist/protocolo embutido no Revisor. Após o merge, `rpsa_auto` registra a classificação e alinha os carimbos `sincronizado-até` de `revisor.md` e `especificador.md`; o Especificador não recebe texto novo (sua linha de carimbo avança só para manter a sincronia).

## 6. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** Os 60% de CONFLICT-MAP/PP-PAP-001/RULE-EW-002 seguem adiados até o backtest da J-001. A abertura da SPEC-006 segue **não homologada**.

## 7. Registro
- [x] Esta ata · [x] `.claude/agents/revisor.md` (aplicado) · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] merge (ratificação) · [ ] RPSA automático · [ ] verificação pós-merge em sessão nova · [ ] F4 (medição com semente nova e defeitos de Andraus)

---

**Andraus** — *aplicação autorizada em chat, 2026-10-11; registro feito pelo Orquestrador interno a pedido de Andraus. Assinatura = merge desta ata.*
