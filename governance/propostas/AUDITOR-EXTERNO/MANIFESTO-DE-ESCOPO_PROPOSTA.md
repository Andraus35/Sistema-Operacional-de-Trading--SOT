# MANIFESTO DE ESCOPO — Auditor Externo LLM ("GPT")

**[PROPOSTA — NÃO HOMOLOGADO]**

| Campo | Valor |
|---|---|
| Autor | Especificador Principal SOT (Claude Code, Opus 4.8) |
| Data | 2026-10-05 |
| Natureza | Registro de escopo. Não-normativo. Não homologa, não fecha decisão (CONS-01). |

## 1. Arquivos CRIADOS (todos novos, em `governance/propostas/AUDITOR-EXTERNO/`)

```
governance/propostas/AUDITOR-EXTERNO/
├── DOSSIE-PESQUISA.md                       (A)
├── PROTOCOLO-AUDITOR-EXTERNO_PROPOSTA.md     (B)
├── BRIEFING-GPT_PROMPT.md                    (C)
├── MANIFESTO-DE-ESCOPO_PROPOSTA.md           (D) — este arquivo
└── sources/
    ├── SRC-JUDGE-01.txt      (arXiv 2411.15594 — LLM-as-a-Judge survey)
    ├── SRC-OWASP-01.txt      (OWASP LLM01:2025 Prompt Injection)
    ├── SRC-MSIPI-01.txt      (Microsoft Learn — indirect prompt injection)
    ├── SRC-HALLUC-01.txt     (Claude Platform Docs — reduce hallucinations)
    ├── SRC-AGENTSMD-01.txt   (agents.md)
    ├── SRC-CIREV-01.txt      (G-Research — LLM code review patterns)
    ├── REPO-promptfoo.txt    (github.com/promptfoo/promptfoo — ELEGÍVEL)
    ├── REPO-garak.txt        (github.com/NVIDIA/garak — ELEGÍVEL)
    └── REPO-evals.txt        (github.com/openai/evals — ELEGÍVEL)
```

Total: 4 documentos + 9 capturas de fonte. Todos `[PROPOSTA — NÃO HOMOLOGADO]`.

## 2. O que NÃO foi tocado (intencionalmente)

Nenhum destes foi lido-para-alterar nem modificado:
- `AGENTS.md` — não alterado.
- `.claude/agents/especificador.md`, `.claude/agents/revisor.md` — não alterados.
- `atomic-spec.md` — não alterado.
- `governance/RULES.md`, `governance/CATALOGO-OFICIAL.md`, `governance/CONFLICT-MAP.md` — não alterados.
- `ROADMAP.md` — não alterado.
- `specs/**`, `canon/**`, `backlog/**`, `schemas/**`, `rag/**`, `scripts/**`, `tests/**`, `.github/**`, `WORKFLOW.md`, `GLOSSARIO.md` — não alterados.
- `docs/mapa/**` — não editado à mão (saída gerada; BL-019/INV-09).

Nenhum commit foi feito. Nenhum script foi executado (o Especificador não tem Bash).

## 3. Pendências operacionais (para quem orquestra — tem Bash)

**[PROPOSTA]** Como o Especificador não tem Bash, rodar por fora:
- `python scripts/build_map.py` e depois `python scripts/build_map.py --check` — porque foram criados arquivos `.md` novos (o mapa pode ter defasado; os hooks normalmente regeneram, mas confirme).
- `python scripts/check_refs.py` — integridade de referências (estes documentos citam arquivos do repo por nome).
- `python scripts/check_repo_research.py governance/propostas/AUDITOR-EXTERNO` (ou o caminho que a convenção definir) — validar as capturas `sources/REPO-*.txt` contra a régua RULE-ECC-06.

Observação: estes documentos vivem em `governance/propostas/` (proposta), não em `specs/features/` — o gate `validate_spec_sot.py` não se aplica (não há `plan.md` de Spec).

## 4. [DECISÃO NECESSÁRIA]

1. **Instituir o papel de Auditor Externo LLM é decisão de Andraus.** Esta entrega é proposta; não cria papel, RULE nem altera o fluxo de 3 posições sem homologação.
2. **Onde o papel, se homologado, deve ser normatizado** (ex.: nova RULE em `governance/RULES.md`, emenda ao fluxo em AGENTS.md, ou documento de governança próprio) — decisão de Andraus. O Especificador não decide isto.
3. **Nome/escopo de acesso do colaborador "GPT"** e ambiente em que roda (fora do Claude Code) — a orquestração e Andraus definem; o SOT não controla temperatura/seed/versão.

## 5. Status epistemológico e limites honestos (RULE-MET-01)

- Tudo aqui é `[PROPOSTA]`, exceto citações de fatos vigentes do SOT (`[FATO]`) e achados externos (`[EXTERNO]`).
- Não pude verificar: a veracidade das páginas web citadas (DADO); o estado privado de segurança dos repositórios (proxy público); a reprodutibilidade de um modelo externo.
- É `[INFERÊNCIA]`: o mapeamento das práticas externas aos mecanismos internos do SOT (ENF-03, RULE-ECC-04, CONS-01, fluxo de 3 posições) — proposto por analogia, a confirmar por Andraus/Revisor.
- Nenhuma decisão aberta foi tocada ou fechada (CONS-01). Nenhum canônico foi redefinido (CONST-01). Nenhum histórico foi alterado (INV-07/INV-09).

## 6. Kit operacional (adicionado pelo orquestrador, 2026-10-05) `[PROPOSTA — NÃO HOMOLOGADO]`
Decisões de Andraus (chat): canal = Issue com formulário; credencial = conta dedicada, papel Read, token mínimo; o auditor **não é agente interno nem gate**.
Arquivos novos em `governance/propostas/AUDITOR-EXTERNO/kit/`: `README-INSTALACAO.md`, `INSTRUCOES-OPERACIONAIS-GPT.md`, `setup_auditor.sh`, `verify_access.py`, `run_gates.py`, `validate_finding.py`, `submit_finding.py`, `selftest.py`, `finding.schema.json`, `finding.example.json`, `ISSUE_TEMPLATE-auditoria-externa.yml`.
Arquivos revisados (marcados no texto): `BRIEFING-GPT_PROMPT.md` (execução, esquema, canal) e `PROTOCOLO-AUDITOR-EXTERNO_PROPOSTA.md` (3 linhas + nota de revisão), reconciliando a premissa original "auditor sem Bash" com a decisão de rodar os gates localmente pelo kit; `DOSSIE-PESQUISA.md` e `sources/REPO-*.txt` (URLs com `https://` e datas ISO, para o verificador da RULE-ECC-06).
**Verificações executadas pelo orquestrador:** `build_map.py --check` OK; `check_refs.py` sem ERRO; `check_doc_sync.py` sem achados; `check_repo_research.py` sobre cópia do dossiê = OK (estrutura); citações do dossiê conferidas por string-match contra as capturas (as que usam elisão "..." têm cada trecho presente); kit testado em clone local (calibração aprovada; 16 gates exit 0; dry-run de achado real).
**Não verificado:** veracidade das páginas web (DADO); `verify_access.py` e `--post` contra a API real (sem credencial); permissões exatas do token; números de estrelas/commit (mediados por WebFetch).
**Não tocado:** `.github/**` (o formulário fica em `kit/` até decisão de Andraus), `AGENTS.md`, `.claude/agents/*`, `scripts/**`, `specs/**`, `canon/**`, CATALOGO, ROADMAP, RULES.

## 7. Loop automatizado e hierarquia (adicionado pelo orquestrador, 2026-10-05) `[PROPOSTA — NÃO HOMOLOGADO]`
Decisões de Andraus (chat): auditor **subordinado ao Orquestrador, reporta-se só a ele** (o Orquestrador a Andraus; nunca o auditor a Andraus/Especificador/Revisor); postura **só por diretiva** do Orquestrador após consulta a Andraus; tudo em **nuvem**; `git pull` **só** em PR candidato a homologação final de Spec completa; **consenso = Especificador + Revisor + Auditor externo + Andraus** (decisão de Andraus; o Orquestrador coordena e não é parte). Papel em **piloto controlado**, alvo SPEC-006 (ainda não aberta).
Arquivos novos: `.github/workflows/auditor-externo.yml` (inerte até `AUDITOR_EXTERNO_ENABLED=true`; sem LLM; sem chave), `DIRETIVAS-AO-AUDITOR.md` (DIR-001 SUPERADA; DIR-002 VIGENTE), `kit/loop_tools.py`, `kit/poll_requests.py`, `kit/test_loop.py`. Alterados: validador/esquema/exemplo/selftest (`directive_version`, `E-DIRETIVA`), README, instruções, briefing, protocolo, formulário (linha de reporte única).
**Verificado localmente:** selftest 10/10 (1 válido, 9 defeitos plantados); `test_loop.py` 8/8 (servidor HTTP falso); cadeia do job `achado` simulada (válido/inválido/sem JSON); YAML válido; sintaxe JS dos 5 blocos `github-script`; nenhuma interpolação de texto livre em `run:`; gates do repositório verdes.
**NÃO verificado:** execução real no GitHub Actions (só no merge/uso); `verify_access.py` e `--post` contra a API; comportamento dos rótulos `aex-req-…`/`aex-fp-…` (criados sob demanda); permissão de Read para abrir Issues.
**Limite honesto:** "reportar-se só ao Orquestrador" é regra de **endereçamento e conduta**, não controle de acesso: o dono do repositório enxerga todas as Issues. O Orquestrador usa a mesma conta GitHub do dono; a separação é por protocolo (sem menções/atribuições, e Andraus recebe a consolidação).

## 8. Pacote de instalação do auditor (2026-10-05)
`AGENTE-AUDITOR-EXTERNO.md` — documento único e autocontido (instruções + instalação em nuvem + procedimento + esquema + proibições), derivado do briefing, das diretivas (DIR-002) e do kit; em conflito vale a diretiva vigente. O pacote `.tar.gz` entregue contém esta pasta (`git archive` do commit registrado) + `MANIFEST.sha256` para verificação de integridade antes de qualquer execução. **Não verificado:** instalação em ambiente em nuvem real do auditor.
