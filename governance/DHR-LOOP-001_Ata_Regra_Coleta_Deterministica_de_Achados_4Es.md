# DHR-LOOP-001 — Ata de Decisão — Regra determinística de coleta de achados do loop dos construtores (4Es)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | Pedido de Andraus (chat, 2026-10-24): "Adicione essa regra determinística ao seu chat orquestrador. A necessidade de coletar deterministicamente a partir das rodadas entre agentes construtores inconsistências, conflitos e ambiguidades recorrentes, as causas dos achados, ausência de prevenção de erros. O loop de trabalho dos construtores precisa ser constantemente melhorado e refinado visando a aplicação do framework 4Es" · `governance/propostas/MELHORIAS-PROCESSO/RELATORIO-MELHORIAS-AGENTES-E-GATES-2026-10-24.md` · `scripts/loop_ledger.py` · `governance/aprendizado/` |
| Data | 2026-10-24 |
| Status | **REGRA ADOTADA** (ordem direta de Andraus em chat). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10); a edição de `AGENTS.md` (§8 e novo §12) decorre desta ordem expressa. |
| Compatibilidade | Minor (acrescenta regra operacional do Orquestrador e um detector informativo; não toca modelo canônico nem Spec) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra operacional do Orquestrador e detector: não altera texto de agente de construção nem método. |

## 1. A regra (resumo; texto operacional em `AGENTS.md` §12)
**Após cada parecer do Revisor, o Orquestrador DEVE, nesta ordem:**
0. **[SUPERADO em 2026-10-25 por DHR-ROTEAMENTO-005 — o Orquestrador NÃO corrige achados do Revisor, de nenhuma severidade; Menores não abrem rodada sozinhos]** *(texto anterior preservado — INV-07)* **Economia de rodada (acrescentado em 2026-10-24, a pedido de Andraus):** classificar os achados em M/S/O (DHR-ROTEAMENTO-003) e aplicar os **mecânicos pela classe M** (ficha + `roteador_modelos.py conferir`) em vez de reenviá-los a agente caro; o restante segue ao Especificador. *(Primeira aplicação: `governance/propostas/SPEC-048/FICHA-M-PLAN-R3.json`, 6 substituições, `conferir` OK.)*
1. **Transcrever** o parecer com o bloco `<!-- ACHADOS-ESTRUTURADOS ... -->` (linhas `ID|SEV|CATEGORIA|CAUSA|PREVENCAO`, categoria da taxonomia fixa C01..C10/C99) — fonte determinística e prevalente sobre a heurística.
2. **Rodar** `python scripts/loop_ledger.py` (gera `governance/aprendizado/LEDGER-ACHADOS.md`: achados por linha e rodada, categorias, recorrência, tendência de Médias, lacunas de prevenção) e commitar o ledger no mesmo commit do parecer.
3. **Registrar** em `governance/aprendizado/CAUSAS-PREVENCAO.md` (append-only) a **causa-raiz** e a **prevenção** (existente, ausente ou proposta) de toda **Média** e de toda **categoria recorrente** (≥2 rodadas ou ≥2 linhas de trabalho) apontada como **LACUNA DE PREVENÇÃO** no ledger.
4. **Informar** no HANDOFF as 3 categorias mais recorrentes e as lacunas abertas.
5. **Tratamento de melhoria no FECHAMENTO da Spec e ANTES de abrir outra** (esclarecimento de Andraus, chat 2026-10-24: "O tratamento de melhoria individual e de loop coletivo entre agentes deve ocorrer ao fim de um trabalho completo de Spec e antes de abrir outra spec"): retrospectiva individual (Especificador, Revisor, Orquestrador) e coletiva (o loop) em `governance/aprendizado/RETROSPECTIVAS.md`; propostas de gate/processo em `governance/propostas/MELHORIAS-PROCESSO/`, que **só viram mecanismo por ordem expressa de Andraus** (com `governance/MECANISMOS.json` no mesmo PR, COE-14). Antes de abrir outra Spec: `python scripts/loop_ledger.py --retro-check SPEC-nnn` da Spec fechada (sem `FEITA`, não abre, salvo dispensa expressa de Andraus). Os passos 0-4 (coleta e economia de rodada) seguem a cada parecer.

## 2. Enquadramento nos 4Es (ordem de precedência: Conformidade > Eficácia > Efetividade > Eficiência > Economicidade)
- **Conformidade:** nenhuma decisão aberta fechada pelo ledger (Detector, ENF-03); a categoria C08 mede deriva de escopo/CONS-01.
- **Eficácia:** Médias por rodada por linha de trabalho (o ledger mostra a tendência).
- **Efetividade:** recorrência por categoria entre linhas — prevenção que não funciona reaparece.
- **Eficiência:** nº de rodadas até 0 Média+Crítica.
- **Economicidade:** **INDETERMINADO** (tokens/custo não medidos no repositório); nunca rebaixa nível de enforcement.

## 3. O que esta ata NÃO faz
- Não implementa nenhum dos gates do relatório de melhorias (G-A..G-I) nem muda `revisor.md`/agentes.
- A classificação por palavra-chave é **indicativa**; a categoria estruturada do parecer prevalece; arquivos sem achado extraído são listados (não são prova de ausência). Pareceres antigos (SPEC-006, abertura da SPEC-007) estão fora do padrão e saem com 0 extraídos até serem transcritos no formato novo, se Andraus ordenar.
- Não fecha decisão aberta (CONS-01).

## 4. Efeitos aplicados
`scripts/loop_ledger.py` e `tests/test_loop_ledger.py` (no CI); `governance/aprendizado/` (`CAUSAS-PREVENCAO.md`, `LEDGER-ACHADOS.md` gerado); `AGENTS.md` §8 (comando) e novo §12; `governance/MECANISMOS.json` (detector `det.loop-ledger`); `.github/workflows/ci.yml` (teste bloqueante + ledger informativo); `governance/CATALOGO-OFICIAL.md` (registro).

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · mecanismo da autenticação dos atos de Andraus (BUILD). **Nenhuma decisão aberta foi fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] AGENTS.md · [x] MECANISMOS.json · [x] CI · [x] CATALOGO · [ ] merge (assinatura)

---

**Andraus** — *ordem em chat, 2026-10-24; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
