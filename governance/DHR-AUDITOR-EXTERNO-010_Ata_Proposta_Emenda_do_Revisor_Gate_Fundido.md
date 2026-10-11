# DHR-AUDITOR-EXTERNO-010 — Ata — Proposta de emenda do `.claude/agents/revisor.md` (gate fundido como ferramenta oficial, sem Bash)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-11 |
| Status | **PROPOSTA DE TEXTO — nada é aplicado ao arquivo do Revisor por esta ata.** O merge desta ata aprova o **texto** da §3; a **aplicação** ao `.claude/agents/revisor.md` é um passo seguinte e separado, só com autorização expressa de Andraus ("aplique a emenda do Revisor") e ata de aplicação própria com RPSA em escopo. Continua a DHR-AUDITOR-EXTERNO-009 (fase F3). Não fecha nem abre decisão. |
| Compatibilidade | Aditiva (INV-07); substitui apenas o §3 do Revisor, quando aplicada. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Esta ata propoe o texto da emenda mas nao altera nenhum arquivo de agente; a aplicacao ao revisor.md sera feita em PR proprio, com ata de aplicacao declarando escopo sim e sincronizacao propagado. |

## 1. Por quê `[FATO]`
`revisor.md` §3 manda o Revisor rodar `python scripts/validate_spec_sot.py` primeiro, mas o frontmatter só lhe dá `Read · Grep · Glob`: a ordem é inexequível (nas 3 rodadas do teste cego de 2026-10-11 ele declarou "gate não executado"). A DHR-009 (F0–F2, mescladas) entregou o gate fundido (Classe D) e a **ferramenta estreita** `revisor_gate` (MCP local, somente leitura, sem Bash). Esta ata propõe o texto que faz o Revisor usá-la.

## 2. Texto exato proposto (quatro trechos de `.claude/agents/revisor.md`)

### 2.1 Frontmatter — ferramentas (linhas 9–14 atuais)
**Antes:**
```yaml
tools:
  - Read
  - Grep
  - Glob
# Write e Edit são INTENCIONALMENTE AUSENTES.
# Isso torna estruturalmente impossível o Revisor reescrever a Spec (ENF-03).
```
**Depois:**
```yaml
tools:
  - Read
  - Grep
  - Glob
  - mcp__sot-revisor-gate__revisor_gate
# Write, Edit e Bash são INTENCIONALMENTE AUSENTES.
# Isso torna estruturalmente impossível o Revisor reescrever a Spec (ENF-03).
# A ÚNICA exceção de execução é a ferramenta estreita abaixo (DHR-AUDITOR-EXTERNO-009/010): servidor MCP local, somente leitura,
# argumento único validado (SPEC-NNN) no próprio servidor, sem shell. Ausente a ferramenta (ex.: pasta não confiável) = falha fechada (§3).
mcpServers:
  - sot-revisor-gate:
      type: stdio
      command: python
      args: ["scripts/revisor_gate_mcp.py"]
```

### 2.2 §3 inteiro (linhas 68–79 atuais)
**Antes:**
```markdown
## 3. Gate determinístico (primeiro passo — obrigatório)

**Antes de qualquer análise semântica**, execute:

​```bash
python scripts/validate_spec_sot.py specs/features/<SPEC-00x>/plan.md
​```

- **Exit 0:** estrutura válida → prossiga com o protocolo semântico (§4).
- **Exit 1:** falha de estrutura → emita NÃO CONFORME Crítica imediatamente, **sem análise semântica**. O script decide; você não negocia com a falha de estrutura.

Este é o **Detector ≠ Gate (ENF-03):** o script é o gate determinístico; sua análise semântica é o detector. Nunca inverta os papéis.
```
**Depois:**
```markdown
## 3. Gate determinístico (primeiro passo — obrigatório)

**Antes de qualquer análise semântica**, chame a ferramenta `revisor_gate` (MCP, somente leitura) com o identificador da Spec:

​```
revisor_gate(spec="SPEC-00x")      # opcional: rapido=true pula os detectores do repositório inteiro
​```

Você **não tem Bash**: não tente executar scripts. A ferramenta roda o **gate fundido (Classe D)** — estrutura (`validate_spec_sot.py`), baselines na raiz, IDs de modelo canônico, valores e ordem das regras, referências, sincronização, backlog `ATIVADO`, RPSA e mapa — e devolve também **sinais H** (candidatos por palavra-chave).

- **`VEREDITO D: PASSOU_D`:** prossiga com o protocolo semântico (§4). Cada **sinal H** é só um candidato: confirme ou descarte com prova (arquivo:linha); nunca o trate como achado sem confirmar.
- **`VEREDITO D: REPROVADO_D`:** emita NÃO CONFORME Crítica imediatamente, **sem análise semântica**. O código decide; você não negocia com a falha determinística.
- **Ferramenta ausente, recusada ou com erro** (sessão em pasta não confiável, servidor fora do ar, argumento recusado): declare **GATE NÃO VERIFICADO** no relatório; o parecer fica **no máximo CONFORME condicional** (falha fechada). Nunca deduza o resultado do gate nem finja tê-lo executado.

Este é o **Detector ≠ Gate (ENF-03):** o código é o gate determinístico (forma, valor, existência — Classe D); sua análise é o detector (sentido, adversarial, epistêmico — Classe P). Nunca inverta os papéis. O resultado do gate **nunca** é parecer nem homologação.
```

### 2.3 §4, abertura (linha 83 atual)
**Antes:** `**Após o gate determinístico passar (exit 0):**`
**Depois:** `**Após o gate determinístico passar (`PASSOU_D`):**`

### 2.4 Formato do relatório, item 3 (linhas 315–317 atuais)
**Antes:**
```
3. GATE DETERMINÍSTICO
   validate_spec_sot.py: [PASS (exit 0) / FAIL (exit 1)]
   [Se FAIL: NÃO CONFORME Crítica — encerrado aqui]
```
**Depois:**
```
3. GATE DETERMINÍSTICO
   revisor_gate: [PASSOU_D / REPROVADO_D / GATE NÃO VERIFICADO (ferramenta ausente → no máximo CONFORME condicional)]
   Sinais H confirmados/descartados: [lista com arquivo:linha]
   [Se REPROVADO_D: NÃO CONFORME Crítica — encerrado aqui]
```

## 3. O que NÃO muda
Modelo, esforço, Passos 0–8, interpelação, veredito, `required_sources`, carimbo `sincronizado-até` (alinhado automaticamente pelo RPSA após a ata de aplicação) e a ausência de **Write, Edit e Bash**. O Revisor continua sem escrever em nada; a ferramenta só lê e recusa, no servidor, qualquer argumento fora de `^SPEC-[0-9]{3}$`.

## 4. Riscos e provas `[FATO: execuções de 2026-10-11]`
- **Provas já feitas** (DHR-009 §8): ferramenta visível só ao agente que a declara; gate roda e devolve `PASSOU_D`; injeção `SPEC-001 && echo x` recusada no servidor; sem ferramenta de escrita; **arquivo de agente real** (nível de usuário) funcionou de ponta a ponta com o servidor corrigido para Windows.
- **Pasta confiável (documentação oficial):** servidores embutidos em `.claude/agents/` **do projeto** só carregam depois que a pasta é confiável; em sessões não interativas (`-p`, CI) isso não conta. **Consequência:** nessas sessões o Revisor fica **sem a ferramenta** e cumpre a regra de falha fechada (**GATE NÃO VERIFICADO**, no máximo condicional). Aceitar essa consequência faz parte da aprovação desta ata.
- **Caminho relativo** (`scripts/revisor_gate_mcp.py`): vale para sessões abertas na raiz do repositório; em outra pasta a ferramenta não conecta (também falha fechada).
- **Windows:** depende da correção de UTF-8 do servidor (PR de correção da DHR-009), que **deve estar mesclada antes da aplicação**.
- **Não provado ainda:** o Revisor **de projeto** (arquivo em `.claude/agents/` do repositório) com a ferramenta carregada em sessão interativa com pasta confiável. Verificação **obrigatória** logo após a aplicação, em sessão nova: o Revisor lista as 4 ferramentas e roda o gate na SPEC-001; se não, **reverter** (um commit de reversão restaura o texto anterior).

## 5. Reversão
Se a verificação pós-aplicação falhar ou o Revisor se comportar mal, um `git revert` do commit de aplicação restaura exatamente o texto atual de `revisor.md`. O carimbo RPSA é realinhado pela ata de reversão.

## 6. Decisão pedida a Andraus
Aprovar este texto (merge) **e**, separadamente, autorizar a aplicação ("aplique a emenda do Revisor"). Quem aplica não altera o texto aprovado.

## 7. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** Os 60% de CONFLICT-MAP/PP-PAP-001/RULE-EW-002 seguem adiados até o backtest da J-001. A abertura da SPEC-006 segue **não homologada**.

## 8. Registro
- [x] Esta ata (texto exato) · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] aprovação do texto (merge) · [ ] autorização de aplicação · [ ] aplicação ao `revisor.md` + ata de aplicação (RPSA sim/propagado) · [ ] verificação pós-aplicação em sessão nova · [ ] F4 (medição)

---

**Andraus** — *proposta de texto, 2026-10-11; registro feito pelo Orquestrador interno a pedido de Andraus. Assinatura = merge desta ata (aprova o texto, não aplica).*
