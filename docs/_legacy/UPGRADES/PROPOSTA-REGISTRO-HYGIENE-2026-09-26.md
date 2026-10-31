# PROPOSTA — texto pronto para registro no próximo Ciclo de Hygiene (RCH-001)

**Data:** 2026-09-26 · **Status:** RASCUNHO NÃO-NORMATIVO — nada aqui foi aplicado a `governance/`.
**Regra:** RCH-001 é append-only (INV-07); Andraus aprova antes de o Controlador anexar.

---

## Entrada 1 — Achado K-REF-01: citação sem lastro `DHR-PRA-001` (agentes do trio)

| Campo | Valor |
|---|---|
| Origem | `scripts/check_refs.py` (verificador de referências), execução 2026-09-26 |
| Objeto | `.claude/agents/especificador.md` (§6.2) e `.claude/agents/revisor.md` (cabeçalho e Passo 7) |
| Achado | Três citações a uma ata de prefixo DHR "PRA-001" **sem arquivo, sem linha no CATALOGO-OFICIAL e sem menção em qualquer outro documento** (incluindo `docs/_legacy/`). |
| Natureza | Citação sem lastro (provável sigla mal digitada ou identificador que nunca virou arquivo). **Não** há evidência de ata perdida. |
| Ação já aplicada (2026-09-26) | Citação removida dos títulos; autoridade do Enforcement Contract = **EUA-E02 v1.2 + tabela ENF-01…08 do `atomic-spec.md`**. Nota de rastro no cabeçalho do `revisor.md`. Comportamento dos agentes inalterado. |
| Não feito (por segurança) | Nenhuma ata retroativa foi criada (RULE-MET-01, INV-07). Carimbo `sincronizado-até` inalterado (não houve DHR nova). |
| Pendência de Andraus | (a) Confirmar, fora do repositório (backup, Notion, chats antigos), se existiu alguma ata com esse nome. Se existir → restaurar em `governance/` no padrão `DHR-*.md` e reverter a nota do `revisor.md`. (b) Se não existir → fechar o achado com a frase: *"citação sem lastro, removida; autoridade = EUA-E02 v1.2 + ENF-01…08"*. |
| Disposição sugerida | Fechar no Hygiene #2/#3 após (a)/(b). |

## Entrada 2 — Passo 7 (RPSA) do ciclo: correção de citação nos agentes

> Sync de agentes (EUA-E16 — RPSA): `especificador.md` e `revisor.md` foram editados em 2026-09-26 **apenas para corrigir uma citação** (K-REF-01), sem mudança de comportamento e sem DHR nova. O carimbo `sincronizado-até` **não** foi alterado porque não houve homologação em escopo. Registrar aqui a divergência editorial conhecida; o Revisor confirma no ciclo, por releitura dos dois arquivos, que o comportamento é o mesmo. Disposição: sem FLAG de Harness Debt, se a releitura confirmar.

## Entrada 3 — Ferramental adicionado (informativo)

- `scripts/check_refs.py` (integridade de referências; somente leitura; exit 1 só em ERRO) e `tests/test_check_refs.py`.
- Hooks `gate-check.js` / `post-edit-check.js` corrigidos para o contrato real do Claude Code (stdin JSON, exit 2) + `tests/test-hooks.js`.
- STRUCT-10 (`validate_spec_sot.py`) corrigido para reconhecer decisões FECHADAS declaradas no ROADMAP + `tests/test_struct10.py`.
- CI: etapa informativa do `check_refs.py` (`continue-on-error`), sem bloquear.
- Relacionado: BL-019 (mapa de grafo) e BL-006 (script que "informa" ativações) no RMR-001 — o gatilho do BL-006 ("existência de tooling de governança em `scripts/`") pode já estar satisfeito; **decisão de ativação é de Andraus**.

## Item de acompanhamento sugerido (promoção do CI)

Promover o `check_refs.py` de informativo para bloqueante **somente no nível ERRO** após algumas semanas estáveis. Nunca `--strict`/`--info` no CI (WARN/INFO têm falsos positivos históricos por natureza — INV-07).
