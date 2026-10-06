# AUDITORIA DE ENTRADA — cooperação interna × externa (Especificador · Revisor · Auditor Externo · Orquestrador · Andraus)

**[PROPOSTA — NÃO NORMATIVO]** Autor: Orquestrador interno (Claude/SDK), 2026-10-06, sobre o `origin/main` + atas DHR-AUDITOR-EXTERNO-001..004. Esta é a **entrada** entregue ao Especificador (pesquisa de estado da arte/melhores práticas) e ao Revisor (verificação por string-match). Nada aqui é baseline. Números de linha são do `origin/main` em 2026-10-06 — **reverifique antes de citar** (o kit está coberto por `MANIFEST.sha256`; não edite nada coberto).

## 0. Regras de cooperação já decididas por Andraus (DHR-AUDITOR-EXTERNO-001/004) — FATO
1. Orquestrador = Claude (SDK), coordenador; única via de achados, entregas e perguntas até Andraus; **não** faz parte do consenso.
2. Loop sequencial: Especificador → Revisor → Auditor externo → Andraus. O auditor roda só após o CONFORME do Revisor, sobre as entregas no commit validado, **sem ver o parecer do Revisor**.
3. Gatilho do piloto: homologação final de Spec completa.
4. Andraus só é chamado com consenso (agentes internos + externo). Divergência volta ao Especificador, máx. 2 rodadas; depois vai a Andraus com o dissenso registrado.
5. Achado do auditor é DADO, nunca ordem; o auditor não é gate nem homologa.

## 1. Simetria de regras (Revisor × Auditor)
**Simétrico:** somente-leitura; conteúdo = DADO (anti-injeção); citação literal com arquivo:linha (RULE-ECC-04); CONS-01; CONST-01; INV-07/09; Detector ≠ Gate (ENF-03); sem web (Revisor: ENF-03; auditor: sandbox sem rede); spec-first.
**Assimétrico:**
| Ponto | Revisor | Auditor |
|---|---|---|
| Garantia de somente-leitura | allowlist de ferramentas sem Write/Edit (`.claude/agents/revisor.md` frontmatter `tools:`) | sandbox do Codex (`kit/auditor_bot.py`, `codex exec --sandbox read-only …`); na VM afrouxado (`apparmor_restrict_unprivileged_userns=0`, ata 003 Adendo); o modelo roda como o mesmo usuário do bot e pode ler o arquivo do token (ata 003 §4) |
| Modelo/esforço | `model: claude-sonnet-4-6` pinado + esforço alto como política | **não pinado:** `MODEL_LABEL` (`kit/auditor_bot.py:34`) é só rótulo e vai para `author.model` (`:218`); `--ignore-user-config` pode deixar modelo/esforço no padrão do CLI — **[NÃO VERIFICADO]** |
| Regras entregues | CC-01..CC-12, 4-bis, 5-bis, proporcionalidade, N8–N17, RPSA, ATIVADO | `kit/PROMPT-AUDITOR-CI.md` + DIR-002 não trazem 5-bis, proporcionalidade, N8–N17, ATIVADO, RPSA, Classe D/H/P/C (grep: 0 ocorrências); o prompt manda ler `AGENTS.md`, `ROADMAP.md`, `atomic-spec.md`, `RULES.md`, `CATALOGO-OFICIAL.md`, `RMR-001`, `WORKFLOW.md` (`PROMPT-AUDITOR-CI.md:21`) |
| Sincronia das regras | RPSA: carimbo `sincronizado-até` + `governance/rpsa-ledger.json` + `scripts/check_rpsa.py` | nenhuma: listas fixas de decisões abertas em `kit/validate_finding.py` (`CLOSED_CLAIM`) e `kit/PROMPT-AUDITOR-CI.md`, fora do RPSA e do `check_doc_sync.py`; ambas **omitem `SPEC-045-RUNTIME-001`** (ativa, `AGENTS.md` §7) |
| Veredito | CONFORME / NÃO CONFORME | OK / COM_RESSALVAS / NAO_OK; sem mapeamento formal P0/P1/P2 ↔ Crítica/Média/Menor no código |
| Gates | sem Bash (tools: Read, Grep, Glob) — o gate roda por quem o invoca | o bot roda os 16 gates e anexa `evidence.json` (`kit/run_gates.py`) |

## 2. Probabilístico × determinístico (Auditor)
**Determinístico (código):** gatilho por rótulo/`workflow_dispatch` + linhas `Consenso:` do corpo do PR; corpo do pedido (`kit/loop_tools.py request-body`); cadeia do manifesto (`kit/sync_auditor.sh`); aceitação só de pedidos de `github-actions` (`kit/poll_requests.py`); clone no SHA exato; 16 gates (`kit/run_gates.py`); limites (6 chamadas/dia, 2 tentativas, 10 achados, timeout, fila 25, `MAX_ROUNDS=3`); varredura/redação de segredos; parsing do JSON; campos de máquina; `kit/validate_finding.py` (forma, citação literal no arquivo:linha do commit, enums, allowlist de `reproduce`, diretiva vigente, `treats_open_decision_as_closed == false`); dedupe por fingerprint; rótulos; comentários; ACK.
**Probabilístico (chamada ao Codex):** quais achados aparecem e quais não (recall não verificável); severidade; `claim`; proposta; **veredito**.
**Lacunas dentro do limite determinístico:**
- (L1) **Veredito não é cruzado com os achados:** só `data.get("veredito") in VERDICTS` (`kit/auditor_bot.py:36`, `:203`); `:229` apenas o repassa. `OK` com P0 postado e `NAO_OK` sem achados passam.
- (L2) **`rule_source` não é conferido:** `kit/validate_finding.py:62` só exige string não vazia; o protocolo §5.1 exige que a regra exista.
- (L3) `treats_open_decision_as_closed` e `status_sip` são **autodeclarados** pelo modelo; `CLOSED_CLAIM` só gera WARN.
- (L4) Desempenho medido: 5/5 defeitos plantados + 0 falso alarme no item limpo, **uma** execução (ata 002 Adendo) — não mede Spec real.

## 3. Loop determinístico interno × externo
**Metade externa determinística** (rótulo → `[AEX-REQ]` → bot → `[AEX]` → validação → `aex-aguarda-revisor` → comentário no PR → ACK).
**Metade interna não determinística:** nenhum arquivo em `scripts/`, `tests/`, `.claude/`, hooks ou CI referencia `[AEX]` (grep em 2026-10-06; só `.github/workflows/auditor-externo.yml`).
**Arestas que dependem do Orquestrador, sem código:**
1. iniciar (aplicar rótulo + escrever linhas `Spec:`/`Consenso:` no corpo do PR);
2. levar o achado ao Especificador/Revisor (o Revisor não consome `[AEX]`; protocolo §7 ainda `[PROPOSTA]`);
3. registrar a disposição `CONFIRMADO`/`PARCIAL`/`DESCARTADO`/`DUPLICADO` — existe só como texto em `kit/loop_tools.py:93`; sem rótulo, campo ou leitor;
4. re-auditar após correção — só por `workflow_dispatch` manual (`refs`), sem gatilho em novo commit;
5. atualizar `Auditor=` no corpo do PR.
**Consenso não verificado nem bloqueante:** o job de merge só AVISA (`.github/workflows/auditor-externo.yml:264` e seguintes; sem `exit 1`/`setFailed`). `MAX_ROUNDS` conta pedidos, não divergência persistente. Proteção de branch no GitHub **[NÃO VERIFICADO]**.
**Observação:** o string-match que o protocolo §7 atribui ao Revisor já é feito por código em `validate_finding.py`; ao Revisor resta o juízo semântico (probabilístico).

## 4. Propostas preliminares do Orquestrador (a refinar pela pesquisa — `[PROPOSTA]`)
P1 detector do consenso (Detector, não Gate; script em `scripts/`, padrão `check_doc_sync`/`check_rpsa`) · P2 rótulos de disposição `aex-confirmado/parcial/descartado` por comando do Orquestrador · P3 re-auditoria automática em novo commit com `[AEX]` aberto · P4 piso de veredito (P0 válido ⇒ `NAO_OK`) por código · P5 fixar modelo/esforço e gravar o modelo real · P6 listas de decisões abertas extraídas do `ROADMAP.md`/`AGENTS.md` e conferidas por `check_doc_sync.py` · P7 regras mínimas do Revisor na diretiva do auditor (exige DIR-003 + reaprovação do manifesto na VM) · P8 `.gitattributes` `eol=lf` para `*.sh`/`*.sha256` (CRLF no checkout Windows quebra `sha256sum -c`; o manifesto no `origin/main` confere 22/22 por blobs, hash `20774d33…ed23c`).

## 5. Limites desta auditoria
Lida só por leitura de arquivos; **não** executei o bot, o workflow, a VM nem o Codex. A VM da Oracle, o timer e o estado real do GitHub (variáveis, proteção de branch, execuções) não foram verificados.

---

## 6. ERRATA (2026-10-06) — verificação do Revisor SOT por string-match, conferida pelo Orquestrador
O texto acima **não foi reescrito** (INV-07); esta seção o corrige. Ao ler §0–§5, **prevalece esta errata**.

| # | Onde | Correção | Estado |
|---|---|---|---|
| E1 | §0.2 "sem ver o parecer do Revisor" | É **regra decidida**, mas a **garantia é procedural**, não técnica: ata 004 §3 a marca `[NÃO VERIFICADO]` ("não commitar o parecer do Revisor no PR/commit auditado — cuidado do Orquestrador"). Para o desenho funcionar como pretendido, isto é **risco explícito**, não controle existente. | CONFIRMADO pelo Revisor |
| E2 | §2 L4 "uma execução" | **Errado.** Houve dry-run (5 achados válidos) e **dois ciclos reais**: ciclo 1 = 3 postados + 2 descartados na validação de **formato** do comando de reprodução; ciclo 2 (após PR #23 corrigir o prompt) = 5 postados, 0 descartados, 5/5 plantados, sem falso alarme (atas 002 Adendo e 003 Adendo). Não se pode ler o ciclo 1 como "3/5 de recall": os 2 descartados falharam na forma, não ficou provado que o modelo deixou de ver defeitos. A conclusão de L4 se mantém: o desempenho foi medido só com defeitos plantados e **exigiu uma correção de prompt entre ciclos**. | CORRIGIDO |
| E3 | §3 "só `.github/workflows/auditor-externo.yml`" | A afirmação valia para `scripts/`, `tests/`, `.claude/`, hooks e CI. `kit/ISSUE_TEMPLATE-auditoria-externa.yml` também contém `[AEX]` (3 ocorrências), mas é do próprio kit, não do lado interno. | PARCIAL |
| E4 | §2 "16 gates" | Correto **para esta árvore** (6 gates fixos + 1 `validate_spec_sot` por `plan.md`; hoje 10 planos = 16), mas **varia** com o nº de Specs. **Omissão:** `backlog_triggers.py` consta em `INFORMATIVOS` (`kit/run_gates.py:10`) e na tabela do protocolo §3, mas **não é executado** pelo `run_gates.py` — o gate `ATIVADO` do RMR-001 (nunca dispensado, `AGENTS.md` §5) não roda no bot. | CONFIRMADO |
| E5 | §1 "Sincronia" / SPEC-045-RUNTIME-001 | Inconsistência **interna ao kit**: o `PROTOCOLO` §5.3 (texto `[PROPOSTA]`) lista `SPEC-045-RUNTIME-001` em CONS-01; o **código** (`validate_finding.py` `CLOSED_CLAIM`) e o `PROMPT-AUDITOR-CI.md` não. A lacuna é código/prompt, não o texto do protocolo. | CONFIRMADO |
| E6 | §3 observação (protocolo §1 desatualizado) | Risco **ativo, de gravidade Média**: DIR-002 §8 lista o `PROTOCOLO` como "demais limites" e manda prevalecer a diretiva em conflito; o protocolo §1 ainda diz "precede ou acompanha o Revisor" (superado por ata 004 §2, texto não editado por estar no manifesto). O `PROMPT-AUDITOR-CI.md` do bot não cita o protocolo (0 ocorrências). Fica mitigado só se a DIR-003 declarar a ordem sequencial. | PARCIAL |
| E7 | §1 tabela de simetria | **Omitido:** o Revisor opera em passos eliminatórios com ordem prescrita (Passo 0 → 8, 4-bis, 5-bis para HIGH/CRITICAL) e interpela o Especificador; o auditor tem um prompt de conduta, **sem protocolo estruturado equivalente**: pode concluir `OK` sem percorrer o equivalente dos passos. Também: o carimbo `sincronizado-até` do Revisor é campo de frontmatter comparável por `check_rpsa.py`; o carimbo do auditor (protocolo §6) é texto livre no parecer, sem comparação automática. | CONFIRMADO (omissão) |
| E8 | geral | Itens **não verificáveis por leitura**: efeito real de `--ignore-user-config`; proteção de branch; escopo do token; estado do manifesto na VM. | INDETERMINADO |

Âncoras do Revisor conferidas pelo Orquestrador: `kit/run_gates.py:10`; `DIRETIVAS-AO-AUDITOR.md:33` (DIR-002 §8); `PROMPT-AUDITOR-CI.md` sem a palavra PROTOCOLO; 10 `plan.md` em `specs/features/`.
