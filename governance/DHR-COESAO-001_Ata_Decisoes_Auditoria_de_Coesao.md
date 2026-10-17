# DHR-COESAO-001 — Ata — Decisões de Andraus sobre a auditoria de coesão dos mecanismos

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-17 |
| Status | **Decisões de Andraus registradas (chat, 2026-10-17, quatro respostas a AskUserQuestion: "Mesclar após CI verde", "Sim, só esses 4", "Criar como PROPOSTA com detector", "Sim, exigir CI + dono")**. O merge desta ata por Andraus é a ratificação. Não fecha nem abre decisão aberta (CONS-01). |
| Compatibilidade | Aditiva (INV-07). A correção nos agentes é só de caixa (`roadmap.md` → `ROADMAP.md`). Reversível por `git revert`. |
| RPSA-escopo | sim |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Corrige apenas a caixa do nome ROADMAP.md nos textos dos dois agentes; nao altera instrucao, checklist, metodo nem regra. |

## 1. Decisões `[FATO]`
1. **Mesclar o PR #111** (relatório `AUDITORIA-COESAO-MECANISMOS-2026-10-17.md`, estudo `ESTUDO-GARANTIAS-DETERMINISTICAS-2026-10-17.md`, detector, correções operacionais, ata `DHR-ASK-002` como PROPOSTA) após CI verde.
2. **Promover a bloqueantes no CI só os 4 checks sem falso positivo:** COE-01 (hook sem script), COE-02 (teste fora do CI), COE-04 (ata inexistente), COE-05 (caixa de nome de arquivo). Os demais (WARN/INFO) seguem informativos. Para isso, Andraus autorizou **no mesmo ato** corrigir `roadmap.md` → `ROADMAP.md` nos arquivos dos dois agentes (única alteração em `.claude/agents/*.md`: a caixa do nome do arquivo; nenhuma instrução muda).
3. **Registro de mecanismos como dado** (`governance/MECANISMOS.json` + `MECANISMOS.schema.json`), **como PROPOSTA** e com detector (COE-14). O `AGENTS.md` **não** é alterado: só passará a apontar para o registro quando Andraus assinar o registro como VIGENTE.
4. **Proteger a `main`:** exigir o check do CI e a revisão do dono. Isso é **configuração do repositório que só Andraus faz** (Settings → Branches); o Orquestrador completou o `CODEOWNERS` com os 7 arquivos selados que estavam sem dono (COE-07).

## 2. Efeitos
`scripts/check_coesao.py` (COE-14 novo) e `tests/test_check_coesao.py`; passo bloqueante-só-em-ERRO no `ci.yml`; `.github/CODEOWNERS` (+7 linhas); `.claude/agents/{especificador,revisor}.md` (caixa); `governance/MECANISMOS.json` e `.schema.json` (PROPOSTA); `AGENTS.md`, selo `GATE-MANIFEST.sha256`, `canon/`, `ROADMAP.md` e `atomic-spec.md` **não** são tocados.

## 3. Nota de risco `[FATO]` — proteção da `main` com revisão de dono
Os PRs deste repositório são abertos sob a conta de Andraus. O GitHub não permite que o autor aprove o próprio PR; com "Require review from Code Owners" ativo e Andraus como único dono e autor, **o merge só prossegue se Andraus puder ignorar a regra como administrador** (opção de bypass da proteção) ou se houver um segundo revisor. Configurar a proteção com essa opção de bypass, ou exigir apenas o check do CI, evita travar o fluxo.

## 4. Permanecem ABERTAS (CONS-01)
Nenhuma decisão aberta fechada ou aberta por este ato; o estado é o do `ROADMAP.md`. Seguem sem decisão: estado do Auditor Externo no `AGENTS.md` §9; `AGENTS.md` §3/§8; camadas inertes do Revisor em nuvem; pre-commit (`gate-check` no-op); skills soltas; regras `RULE-COESAO-01..03`.

## 5. Registro
- [x] Esta ata · [x] relatório e estudo · [ ] merge de Andraus (ratificação) · [ ] proteção da `main` (Settings, só Andraus) · [ ] `CATALOGO-OFICIAL.md` (governance normativo — só após decisão de Andraus)

---

**Andraus** — *decisão em chat, 2026-10-17; registro pelo Orquestrador interno.*
