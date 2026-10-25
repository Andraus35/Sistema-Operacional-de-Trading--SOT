# DHR-ROTEAMENTO-005 — Ata de Decisão — O Orquestrador não corrige achados do Revisor (nenhuma severidade)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | Correção de Andraus (chat, 2026-10-25): "Achados menores não são corrigidos pelo orquestrador" · `DHR-ROTEAMENTO-003` (§7/§8, classe M) · `DHR-ROTEAMENTO-004` (R-AC5/R-AC6) · `DHR-LOOP-001` (passo 0) · `AGENTS.md` §12 |
| Data | 2026-10-25 |
| Status | **REGRA DE PROCESSO ADOTADA** (ordem direta de Andraus em chat; assinatura = decisão registrada no chat e citada nesta ata, AGENTS.md §10). O **alinhamento do código do roteador** está PROPOSTO (§3) e depende da aprovação de novo selo por Andraus. |
| Compatibilidade | Minor (restringe regra operacional do Orquestrador; não toca modelo canônico nem Spec) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra operacional do Orquestrador: não altera texto de agente de construção nem método. |

## 1. Decisão de Andraus `[FATO]`
**Achados do Revisor — inclusive os Menores — NÃO são corrigidos pelo Orquestrador.** Eles são corrigidos pelo **Especificador** (ordem classe O). Isto **restringe** o passo 0 da `DHR-LOOP-001` e o uso da classe M da `DHR-ROTEAMENTO-003`: a classe M deixa de se aplicar a achado de parecer e fica para falhas do **próprio Orquestrador/gates** (mapa, contagem do handoff, placeholder detectado por `check_refs`, selo, etc.).

## 2. Desvio reconhecido e efeito
- Em 2026-10-24 o Orquestrador aplicou **6 correções de Menores (n-08, n-09(a))** do Plan da SPEC-048 pela classe M (`governance/propostas/SPEC-048/FICHA-M-PLAN-R3.json`, `conferir` OK). Foi **contra** esta regra, que Andraus agora explicita. As 6 linhas já foram auditadas pelo Revisor na R4 do Plan (presentes e intactas, sem regressão) e **permanecem** (reverter geraria nova rodada); o desvio fica registrado em `governance/aprendizado/RETROSPECTIVAS.md` (Orquestrador, individual) e a ficha vira histórico. Não se repete.
- **Economia de rodada permitida:** Menores **não abrem rodada sozinhos** — seguem no mesmo envio ao Especificador da próxima correção necessária ou ficam como **condição da homologação**, à escolha de Andraus.

## 3. Alinhamento do código do roteador (PROPOSTO — requer novo selo de Andraus)
`scripts/roteador_modelos.py` é arquivo selado (GATE-MANIFEST). Hoje R-AC5 aceita classe M na ficha de parecer (exige que esteja aplicada). Proposta: R-AC5 passa a **NEGAR ficha que classifique como M achado de PARECER** (M reservada ao que o Orquestrador gera sozinho) e a exigir só a cobertura de todos os IDs como O/S. Não aplicado: depende de aprovação de Andraus do novo hash do selo.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · mecanismo da autenticação dos atos de Andraus (BUILD). **Nenhuma decisão aberta foi fechada por esta ata.**

## 5. Registro
- [x] Esta ata · [x] AGENTS.md §12 · [x] DHR-LOOP-001 (passo 0 superado) · [x] RETROSPECTIVAS (desvio) · [ ] código do roteador (aguarda selo) · [ ] merge (assinatura)

---

**Andraus** — *correção em chat, 2026-10-25; registro pelo Orquestrador.*
