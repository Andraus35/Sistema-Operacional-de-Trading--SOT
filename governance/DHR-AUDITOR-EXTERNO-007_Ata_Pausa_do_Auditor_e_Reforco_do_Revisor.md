# DHR-AUDITOR-EXTERNO-007 — Ata — Pausa do Auditor Externo e reforço do Revisor interno

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-11 |
| Status | **VIGENTE — mesclada na `main`; ratificada por Andraus em 2026-10-17 (DHR-COESAO-002).** *(Marca original: "PROPOSTA — vira vigente só com o merge de Andraus.")* Decisão de direção registrada (chat, 2026-10-11, após o teste de estresse). Não fecha nem abre decisão; não altera checklist, método, regra nem o Revisor. |
| Compatibilidade | Suspende, enquanto durar a pausa, o uso rotineiro previsto nas DHR-AUDITOR-EXTERNO-001..005; não as revoga (INV-07). Reversível. |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda a composicao do consenso de homologacao durante a pausa (auditor opcional) e define melhorias operacionais do Revisor ainda nao aplicadas; nao altera checklist, metodo nem regra dos agentes. Reclassificar se o reforco alterar arquivos dos agentes. |

## 1. Resultado do teste de estresse `[FATO: execução de 2026-10-11, gabarito lacrado]`
Lacre (sha256 do gabarito): `d437701080cd956bd540e92d15994b37067e0a28551f61b5b9f1d890b61c2c74`. 3 documentos de teste, **30 defeitos sorteados por semente que o Orquestrador não leu** e 15 iscas corretas; Revisor (3 rodadas, sessões separadas) e Auditor (3 rodadas, pedidos reais) sobre o mesmo material.

| | Rodada 1 | Rodada 2 | Rodada 3 | União |
|---|---|---|---|---|
| Revisor interno | 27/30 | 27/30 | 28/30 | **29/30** |
| Auditor externo | 25/30 | 26/30 | 25/30 | **26/30** |

Por tipo (melhor rodada): números 7/8 (Revisor) × 8/8 (Auditor); regras do SOT 10/10 × 9/10; sentido 8/9 × 9/9; **referências a documentos inexistentes 3/3 × 0/3**. Achados por ambos: 25; só o Revisor: 4; só o Auditor: 1; nenhum dos dois: 0.

## 2. Limites do resultado `[FATO]`
Não entraram defeitos escritos por Andraus (parte livre de viés). Falsos alarmes **não adjudicados**: 4–8 de 15 iscas foram "tocadas" por citações de linha que misturam defeito e trecho correto — número superestimado, julgamento pendente de Andraus no `detalhe.json`. Respostas do Revisor comparadas em formato reduzido (localização e trecho). O Auditor lê a mudança do commit (duas rodadas iniciais, com commit vazio, foram invalidadas e refeitas). Com 30 defeitos, a diferença entre os dois está dentro do ruído; o valor marginal do Auditor (1 defeito em 30) é o dado que pesou.

## 3. Decisão de Andraus `[FATO: chat, 2026-10-11]`
**Reforçar o Revisor interno e pausar o Auditor Externo.**

## 4. Pausa do Auditor `[PROPOSTA]`
- **Consenso de homologação durante a pausa:** Especificador + Revisor + Andraus. O Auditor é **opcional, por pedido de Andraus** (`workflow_dispatch`), nunca rotina. As DHR-001..005 permanecem como registro e como procedimento para quando o Auditor for chamado.
- **Como pausar (ações de Andraus):** definir a variável de repositório `AUDITOR_EXTERNO_ENABLED=false` (chave de desligamento já prevista no workflow) e, se quiser, parar o timer na VM Oracle por SSH. Nada é apagado: kit, manifesto e VM ficam como estão.
- **Condições para reativar (qualquer uma, por decisão de Andraus):** teste de estresse completado com defeitos escritos por Andraus e iscas adjudicadas; Spec de risco muito alto (CRITICAL) em que uma segunda opinião de outro modelo seja desejada; mudança relevante no Revisor que exija comparação.

## 5. Reforço do Revisor `[PROPOSTA — nada aplicado por esta ata]`
O teste mostrou pontos concretos, não um defeito geral do Revisor:
1. **Gate determinístico não executado nas 3 rodadas** (o Revisor só lê, sem Bash — ENF-03). Proposta: o Orquestrador (ou o CI) roda `validate_spec_sot.py` e os demais gates **antes** e entrega a saída ao Revisor como evidência, sem dar a ele ferramenta de escrita.
2. **Usar este teste como régua do Revisor:** guardar o gerador de defeitos e o conferidor para reexecutar após qualquer mudança no Revisor (regressão), com semente nova e defeitos de Andraus.
3. **Casos perdidos pelo Revisor** (até 3 de 30, concentrados em números): Andraus indica no `detalhe.json` quais foram, e o reforço vira checagem objetiva (ex.: conferência aritmética de limiares contra o `AGENTS.md` §6).
Qualquer mudança nos arquivos do Revisor segue o fluxo habitual (RPSA) e **não** é feita por esta ata.

## 6. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 7. Registro
- [x] Esta ata · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] variável `AUDITOR_EXTERNO_ENABLED=false` (Andraus) · [ ] `OPERACAO.md` e `AGENTS.md` §9 (atualizar após o merge, com autorização de Andraus) · [ ] reforço do Revisor (a propor em ata própria)

---

**Andraus** — *decisão de direção em chat, 2026-10-11; registro feito pelo Orquestrador interno. Assinatura = merge desta ata.*
