# DHR-SPEC007-007 — Ata de Decisão — Diretriz de autenticação criptográfica dos atos de Andraus (ACTREC)

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-007/plan.md` v2.3 (RULE-KFH-020, tipos de ato ACTREC/RIGHTS/EXT_TRANSMISSION/LOCAL_EXECUTOR/ISSUER_LIST/INVALIDATION; "forma de confirmar a identidade de Andraus = BUILD") · `DHR-SPEC007-003/004/005/006` · SPEC-004 RULE-CBP-014 (identidade autenticada) |
| Data | 2026-10-24 |
| Status | **DIRETRIZ DE POLÍTICA REGISTRADA** (decisão direta de Andraus em chat, 2026-10-24: "Vamos seguir sua recomendação de autenticação criptográfica"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Decide o PRINCÍPIO, não o mecanismo** (§3). Não altera nenhum Plan nem implementa nada (fase spec-first). |
| Compatibilidade | Minor (não toca modelo canônico baselined nem Spec baselined) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Diretriz de política de identidade para a construção: não altera texto de agente nem método. |

## 1. Decisão de Andraus `[FATO]` (chat, 2026-10-24)
**Cada ato de Andraus que o sistema precisa reconhecer (liberar uso de fonte, liberar envio externo, confirmar modelo "de casa", aprovar lista de quem carimba, aprovar lote, autorizar troca, invalidar conhecimento) será um registro com ASSINATURA CRIPTOGRÁFICA feita com uma chave de Andraus.** Diretriz adotada (recomendação do Orquestrador, aceita):
1. **Assinatura digital** sobre o registro do ato (aprovador, escopo, hash do material ou lote, data), verificável pela máquina; "está na ata" ou "foi dito no chat" **não bastam** para o gate.
2. **Chave privada em dispositivo físico** de Andraus (token de segurança de hardware, tipo chave FIDO2/YubiKey), **nunca** no repositório, na sessão de um agente, em variável de ambiente nem em arquivo; a máquina só guarda e confere a **chave pública**.
3. **Nenhum agente (AC ou AT) assina por Andraus**; um registro sem assinatura válida de chave autorizada **não vale** (fail-closed, já previsto no Plan).

## 2. Efeitos `[FATO]`
- Resolve o **princípio** do item "forma de confirmar a identidade de Andraus (BUILD)" da lista de decisões abertas: passa a ser **"assinatura criptográfica com chave em dispositivo físico"**. O **mecanismo** continua para a construção (§3).
- `ROADMAP.md` ("Decisões FECHADAS") e `governance/CATALOGO-OFICIAL.md`: registro desta ata, texto anterior preservado. **Não alterados:** Plan da SPEC-007 (baseline) e demais Specs; o texto "forma de confirmar a identidade = BUILD" dos Plans passa a ser lido como "mecanismo, conforme a diretriz desta ata".

## 3. O que esta ata NÃO decide (segue para a construção, como [DECISÃO NECESSÁRIA] a especificar e revisar)
Algoritmo e formato da assinatura e do registro; como a chave pública é cadastrada e conferida na primeira vez (cerimônia de registro da chave); **perda ou roubo do dispositivo** (revogação, chave reserva, quem pode revogar sem criar autoridade nova); rotação de chaves; relógio e anti-repetição (um ato assinado não pode ser reenviado fora do escopo e da data); assinatura em lote; onde fica o repositório de chaves públicas e atos (append-only, INV-07); se algum ato de menor risco pode usar fator mais leve; compatibilidade com SPEC-004 RULE-CBP-014 / SPEC-042 (runtime guardrails). Tudo isso exige Spec/Plan próprio (candidato natural: SPEC-042 ou a Spec de identidade que a abertura propuser) e **ordem de Andraus**.

## 4. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · **mecanismo** da autenticação (§3). **Nenhuma outra decisão aberta foi fechada.**

## 5. Registro
- [x] Esta ata · [x] ROADMAP · [x] CATALOGO · [ ] merge (assinatura) · [ ] especificação do mecanismo (só por ordem de Andraus)

---

**Andraus** — *decisão em chat, 2026-10-24; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
