# DHR-ROTEAMENTO-004 — Ata de Decisão — Roteamento determinístico de ACHADOS (ordem de correção) e via SendMessage

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority (registro pelo Orquestrador) |
| Para | Orquestrador / Especificador SOT / Revisor SOT / Controlador |
| Ref | Pedido de Andraus (chat, 2026-10-24): "Tratar deterministicamente a regra da ata de roteamento de modelo se ainda não houver e garantir tratamento de achados pelos agentes corretos incluindo o orquestrador" · `DHR-ROTEAMENTO-003` (§7, §8: classes M/S1/S2/S3/O, R-AC1..R-AC4) · `DHR-LOOP-001` (passo 0 economia de rodada) · `scripts/roteador_modelos.py` · `.claude/settings.json` |
| Data | 2026-10-24 |
| Status | **EMENDA 2 À DHR-ROTEAMENTO-003 ADOTADA** (ordem direta de Andraus em chat). Assinatura = decisão registrada no chat e citada nesta ata (AGENTS.md §10). |
| Compatibilidade | Minor (acrescenta regras R-AC5/R-AC6 ao roteador existente; não toca modelo canônico nem Spec) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Regra de roteamento do Orquestrador/hook: não altera texto de agente de construção nem método. |

## 1. Lacunas encontradas (o que a DHR-ROTEAMENTO-003 NÃO garantia) `[FATO]`
1. A classe M existia (`classificar`/`conferir`), mas **nada obrigava** o Orquestrador a classificar os achados de um parecer antes de mandá-los ao Especificador: o roteador só conferia modelo/classe do agente, não a **cobertura da classificação**. Resultado observado: achados mecânicos foram enviados a agente em modelo caro.
2. O hook cobria só a ferramenta `Agent`. A **continuação de um agente por `SendMessage`** (via usada nas correções) **contornava** o roteador.

## 2. Regras novas (determinísticas; código em `scripts/roteador_modelos.py`, testes em `tests/test_roteador_modelos.py`)
- **R-AC5 (ordem de correção):** prompt/mensagem ao **Especificador** com `PARECER: <arquivo>` exige `FICHA: <json>` que **classifique todos** os IDs do bloco `ACHADOS-ESTRUTURADOS` do parecer (cobertura total; id com sufixo `n-08(1)` cobre `n-08`) e **NEGA** se restar achado **classe M não aplicado** (o texto novo ainda não está nas linhas prescritas). Parecer sem o bloco ⇒ NEGA (LOOP-001 passo 1). Ou seja: **o Orquestrador aplica a classe M primeiro; só o resto (O) vai ao Especificador.**
- **R-AC6 (SendMessage):** o hook passa a cobrir `SendMessage` (`.claude/settings.json`: matcher `Agent|SendMessage`). Mensagem com `PARECER:` exige `CLASSE-TAREFA:` válida e única; `CLASSE-TAREFA: M` ⇒ NEGA (R-AC3); `O` ⇒ aplica R-AC5. Mensagem sem `PARECER:`/`CLASSE-TAREFA:` passa.
- **Ferramenta:** `python scripts/roteador_modelos.py esqueleto <parecer.md>` gera a ficha com todos os achados (natureza `desenho` ⇒ O) para o Orquestrador classificar/preencher os mecânicos (arquivo, linha, antigo→novo, condição).
- **Tabela de quem trata o quê (inalterada, agora com cobertura obrigatória):** **M → Orquestrador** (ficha + `conferir`, teto 10 linhas/2 arquivos, sem criar regra/campo/ID/mecanismo); **S1/S2 → Revisor sonnet** (conferência/delta; produz a ficha M quando o parecer não a traz); **S3 → Revisor opus** (integral CRITICAL); **O → Especificador opus** (desenho, regra nova, semântica). Independência preservada: o Orquestrador **não altera semântica**, o Revisor nunca revisa o que ele mesmo corrigiu, e a classe M é auditada no delta da rodada seguinte.

## 3. Limites honestos (RULE-UNC-01)
- A regra é de **forma**: confere cobertura e aplicação, não julga o mérito da classificação (o Orquestrador pode classificar mal como O para fugir da M; o Revisor audita no delta; ENF-03).
- Só vale onde o hook roda (Claude Code com `.claude/settings.json`); fora disso (Cline, outra ferramenta) a regra é de processo (`AGENTS.md` §12).
- Em fail-closed, parecer sem bloco estruturado bloqueia a ordem de correção: transcrever o parecer com o bloco passa a ser pré-condição (LOOP-001).

## 4. Efeitos aplicados
`scripts/roteador_modelos.py` (R-AC5/R-AC6/esqueleto), `tests/test_roteador_modelos.py` (+8 testes, 38 no total), `.claude/settings.json` (matcher), `AGENTS.md` §12 (passo 0), `governance/MECANISMOS.json` (entradas do roteador atualizadas), `governance/CATALOGO-OFICIAL.md`. Teste ao vivo do hook: `SendMessage` com `PARECER:` sem `FICHA` ⇒ deny; mensagem comum ⇒ permitida.

## 4-bis. Selo do gate (aprovação de Andraus, chat 2026-10-24/25)
`scripts/roteador_modelos.py` é arquivo selado em `governance/GATE-MANIFEST.sha256` (DHR-AUDITOR-EXTERNO-015); a mudança de selo é decisão de Andraus (AGENTS.md §10). **Andraus aprovou o novo selo** ("Aprovar o novo selo", por AskUserQuestion). Selo regravado com `python scripts/gate_manifest.py --write`: **somente** a linha de `scripts/roteador_modelos.py` mudou — `72769199…ba42` → `0b177009…1dd6` (sha256 completo: `0b1770098a9bdb9378c1f3245b98e37fe4ccc58e6f8c0fcf74249ac6b3a21dd6`); `gate_manifest.py --check` = "Gate íntegro".

## 5. Permanecem ABERTAS (CONS-01)
G-001 · K-001 · M-001 · J-001 · N-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-045-RUNTIME-001 · CKG-STRUCT-ORIGIN-001 · produtor/gatilho de promoção · mecanismo da autenticação dos atos de Andraus (BUILD). **Nenhuma decisão aberta foi fechada por esta ata.**

## 6. Registro
- [x] Esta ata · [x] roteador + testes · [x] settings.json · [x] AGENTS.md · [x] MECANISMOS.json · [x] CATALOGO · [x] selo do gate regravado (aprovado por Andraus) · [ ] merge (assinatura)

---

**Andraus** — *ordem em chat, 2026-10-24; registro pelo Orquestrador. Assinatura = decisão registrada e citada nesta ata.*
