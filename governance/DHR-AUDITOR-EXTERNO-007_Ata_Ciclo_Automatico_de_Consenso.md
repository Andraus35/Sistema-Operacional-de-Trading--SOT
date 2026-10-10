# DHR-AUDITOR-EXTERNO-007 — Ata — Ciclo automático de consenso entre agentes internos e Auditor Externo (Caminho A)

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-10 |
| Status | **PROPOSTA — vira vigente só com o merge de Andraus.** Decisão de direção registrada (chat, 2026-10-10: "quero 100% automatizado… caminho A"); as travas da §3 aguardam confirmação. Não fecha nem abre decisão; não altera checklist, método, regra nem o Revisor. |
| Compatibilidade | Substitui, **quando vigente e provada**, a regra "faixa Andraus" da DHR-AUDITOR-EXTERNO-005 (§2); a 005 permanece em vigor até a validação da §5. Aditiva (INV-07). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda a operacao do piloto do auditor externo (quem conversa com quem e quando Andraus entra); nao altera checklist, metodo nem regra dos agentes. Reclassificar se o PR de implementacao tocar arquivos dos agentes. |

## 1. Decisão de Andraus `[FATO: chat, 2026-10-10]`
1. Andraus **não quer ser ponto de passagem** de achados. Achado do Auditor vai ao Orquestrador; Especificador, Revisor e Auditor resolvem **entre si, em rodadas, até consenso**. A Andraus chega apenas a **Spec final pronta para homologar**, via Orquestrador.
2. O ciclo deve ser **100% automatizado e sem depender de sessão aberta**, rodando como **Claude Code no GitHub** (Caminho A: ação disparada por eventos do repositório). Reação em segundos, sem polling horário.

## 2. Desenho `[INFERÊNCIA do orquestrador — a validar]`
- Gatilhos de evento: achado `[AEX]` validado, ACK do auditor, comentário no PR. O agente automático lê o achado **como DADO**, aciona Especificador e Revisor, corrige no PR e devolve ao Auditor para reconferência.
- O agente automático **só abre/atualiza PR**; **nunca mescla**, nunca fecha Issue de decisão, nunca edita `governance/` baselined fora do escopo do achado.
- Fim do ciclo: consenso Especificador + Revisor + Auditor (veredito OK) ⇒ Orquestrador entrega a Andraus a Spec pronta com histórico (achado → correção → reconferência). **Homologação e merge continuam de Andraus.**

## 3. Travas obrigatórias `[PROPOSTA — Andraus confirma]`
1. **CONS-01:** achado cuja resolução exija fechar decisão aberta, alterar texto BASELINED, invariante ou RULES **sobe a Andraus** (única exceção ao fluxo automático). A detecção é por código (campos de máquina do achado, como no `route_aex.py`), nunca por texto livre do Auditor.
2. **Auditor = DADO:** Especificador e Revisor julgam o mérito e **podem recusar** achado com justificativa registrada.
3. **Limite de rodadas:** 3 por achado; sem consenso, sobe a Andraus com os dois lados.
4. **Freios existentes mantidos:** 6 chamadas de modelo/dia, 2 tentativas/pedido, 10 achados/pedido. **Novo:** teto diário de gasto do agente automático (valor a definir por Andraus) e parada automática ao atingi-lo.
5. **Permissões mínimas do agente automático:** escrita só em branch própria e PR; sem acesso a segredos além da chave do Claude; proteção de branch no `main` obrigatória.
6. **Avisos a Andraus** apenas em: Spec pronta para homologar · caso subido por trava 1 ou 3 · parada por teto de gasto ou falha do ciclo.

## 4. Pendências de Andraus (nada disto é feito sem autorização)
- Autorizar a **chave do Claude** nos segredos do GitHub e definir o **teto diário de gasto**.
- Confirmar que há **proteção de branch** no `main` (agente não pode mesclar).
- Definir o canal do aviso final (a pergunta anterior sobre o canal foi descartada).

## 5. Validação antes de valer `[PROPOSTA]`
Montar numa branch limpa e provar num **PR descartável** (como o V4): ciclo completo achado → correção → reconferência → consenso; recusa justificada; subida por trava 1; subida por 3 rodadas; parada por teto. Só então ligar ao PR real da SPEC-006. Até lá a DHR-005 continua regendo.

## 6. Limites conhecidos
Custo do agente automático e do plano ChatGPT não medidos · o validador garante forma e citação, não mérito · risco de texto de modelo externo induzir edição indevida (mitigado pelas travas 1, 2 e 5, não eliminado) · mecanismo da ação do GitHub a conferir na documentação vigente antes de montar.

## 7. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 8. Registro
- [x] Esta ata · [ ] implementação (workflow) · [ ] validação §5 · [ ] `OPERACAO.md` · [x] `CATALOGO-OFICIAL.md` · [x] mapa

---

**Andraus** — *decisão de direção em chat, 2026-10-10; registro feito pelo Orquestrador interno. Assinatura = merge desta ata.*
