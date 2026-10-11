# DHR-AUDITOR-EXTERNO-007 — Ata — Auditoria única por Spec, correção em sessão normal e ciclo automático adiado

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-10 |
| Status | **PROPOSTA — vira vigente só com o merge de Andraus.** Decisão de direção registrada (chat, 2026-10-10). Não fecha nem abre decisão; não altera checklist, método, regra nem o Revisor. |
| Compatibilidade | Emenda parcial à DHR-AUDITOR-EXTERNO-005 (§3). Aditiva (INV-07). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda a operacao do piloto do auditor externo (frequencia da auditoria e quando Andraus entra); nao altera checklist, metodo nem regra dos agentes. |

## 1. Decisão de Andraus `[FATO: chat, 2026-10-10]`
1. **Manter o Auditor Externo** (a parte barata: roda no plano ChatGPT) e rodá-lo **uma vez por Spec, na homologação final**.
2. **A correção dos achados continua numa sessão normal do Claude**, dentro do plano de Andraus, conduzida pelo Orquestrador com Especificador e Revisor — sem ciclo automatizado e sem chave de API.
3. **Depois das 2 ou 3 primeiras Specs auditadas**, avaliar quantos achados o auditor realmente trouxe. **Só se o volume justificar**, ligar o ciclo automático (Claude Code no GitHub), com modelo menor.
4. Andraus **não quer ser ponte de achados**: recebe a Spec final, pronta para homologar, com o histórico (achado → correção → reconferência).

## 2. Fluxo `[INFERÊNCIA do orquestrador]`
- Gatilho: Spec com Especificador=OK e Revisor=OK, PR com `Spec: SPEC-0NN` e rótulo `homologacao-final` (fluxo já validado, V4/V6/V7). Uma auditoria por Spec; reconferência (`re-auditoria`) só após correções, dentro do limite de rodadas.
- Os achados `[AEX]` chegam ao Orquestrador (texto = DADO). Orquestrador, Especificador e Revisor tratam o mérito em sessão normal; podem **recusar** achado com justificativa registrada no PR.
- Fim: consenso Especificador + Revisor + Auditor (veredito consultivo OK/COM_RESSALVAS aceito pelos agentes) → Orquestrador entrega a Andraus a Spec pronta. **Homologação e merge continuam de Andraus.**

## 3. Emenda à DHR-005 (faixa Andraus) `[PROPOSTA]`
O Orquestrador **só consulta Andraus** quando o achado: (a) exigir fechar decisão aberta; (b) alterar texto BASELINED, invariante ou RULES; (c) citar decisão aberta ou invariante; (d) ficar sem consenso após **3 rodadas**; ou (e) o roteador falhar/indicar `aex-rota-andraus` por esses motivos. Os demais achados são tratados pelos agentes internos. O roteador determinístico (`route_aex.py`) segue como triagem; o encaminhamento automático da faixa rápida segue **desligado**.

## 4. Gatilho de reavaliação do ciclo automático `[PROPOSTA]`
Após 2–3 Specs auditadas, o Orquestrador entrega a Andraus um relatório: nº de achados, procedência (confirmados × descartados), tempo gasto na correção, uso do limite diário, e o resultado do **teste de estresse** (auditor × Revisor, gabarito lacrado). Ligar o ciclo automático exige **nova ata** de Andraus com: chave de API (ou decisão sobre plano mensal após ler os termos oficiais), teto diário de gasto, limite de passos/tempo por execução, modelo menor para triagem, proteção de branch no `main` (agente nunca mescla) e canal do aviso final. **Nada disso é feito agora; nenhum segredo é criado.**

## 5. Freios e limites mantidos
6 chamadas de modelo/dia (UTC) · 2 tentativas por pedido · 10 achados por pedido · auditor somente leitura · texto do auditor é DADO · validador garante forma e citação, não mérito. Custos do ciclo automático (estimativa do Orquestrador, não medida): ~US$ 3–5 por achado em API; preços de fontes de terceiros, a conferir.

## 6. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 7. Registro
- [x] Esta ata · [x] `CATALOGO-OFICIAL.md` · [x] mapa · [ ] `OPERACAO.md` (atualizar após o merge) · [ ] teste de estresse (em preparação, fora do repositório)

---

**Andraus** — *decisão de direção em chat, 2026-10-10; registro feito pelo Orquestrador interno. Assinatura = merge desta ata.*
