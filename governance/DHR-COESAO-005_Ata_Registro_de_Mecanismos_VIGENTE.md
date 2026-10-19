# DHR-COESAO-005 — Ata — Registro de mecanismos (`governance/MECANISMOS.json`) passa a VIGENTE

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | `DHR-COESAO-001` (origem do registro), `DHR-COESAO-003` (AGENTS §8 e RULE-COESAO), minuta `governance/propostas/MINUTA-ATA-REGISTRO-MECANISMOS-VIGENTE-2026-10-18.md`, auditoria `governance/AUDITORIA-COESAO-MECANISMOS-2026-10-17.md` |
| Data | 2026-10-19 |
| Status | **DECISÃO DE ANDRAUS REGISTRADA** (chat, 2026-10-19, AskUserQuestion: "Assinar como VIGENTE agora"). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). **Autoriza expressamente** a nota de `AGENTS.md` §8 (arquivo protegido). Não homologa Spec, não fecha decisão aberta. |
| Compatibilidade | Aditiva (INV-07). Reversível por `git revert` (basta voltar `status_do_registro` para `PROPOSTA`). |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda o status de um registro de estado e uma nota de AGENTS §8; nenhum arquivo de agente, checklist nem método é alterado. |

## 1. Decisão `[FATO]`
`status_do_registro` passa de **PROPOSTA** para **VIGENTE**; `versao` 0.1 → 1.0; `aviso` reescrito. O registro continua **dado de estado, não autoridade**: não homologa nada nem fecha decisão aberta (CONS-01); em divergência com a realidade, **a realidade prevalece** e o detector COE-14 acusa a divergência.

## 2. Evidência `[FATO]` (conferida em 2026-10-19)
48 mecanismos: 37 ativo · 6 legado · 2 inerte-em-nuvem · 2 pausado · 1 proposta. **46 verificados ao vivo** (campo `verificado_em` por item, 2026-10-18); **2 sem exercício ao vivo**: `wf.auditor-externo` (pausado, DHR-AUDITOR-EXTERNO-007) e `cfg.pre-commit` (só vale após `pre-commit install`). `check_coesao.py`: ERRO=0 WARN=0 INFO=5; suíte de testes completa verde.

## 3. Consequência prática a registrar `[FATO]`
Com o registro **VIGENTE**, os achados COE-14 deixam de ser só aviso: o `check_coesao.py` os trata como **ERRO** (docstring do script: "WARN (registro PROPOSTA) / ERRO (VIGENTE)") — e o CI bloqueia ERRO. Logo, **quem criar, mover ou aposentar um script/hook/workflow/guarda atualiza `MECANISMOS.json` no mesmo PR**, ou o CI falha. Isso é o efeito desejado da vigência (registro como fonte única de *estado*).

## 4. O que NÃO muda `[FATO]`
Os itens `inerte-em-nuvem` e `pausado` **não** são reativados por esta ata. Auditor Externo continua PAUSADO (AGENTS §9). O detector continua informativo para o que não é ERRO (Detector ≠ Gate, ENF-03).

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001. **Nenhuma fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] `MECANISMOS.json` VIGENTE · [x] `AGENTS.md` §8 (nota) · [x] HANDOFF (lembrete `[PRAZO]` removido) · [ ] merge (assinatura)

---

**Andraus** — *decisão em chat, 2026-10-19; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
