---
handoff_id: HO-2026-10-18-55
previous: HO-2026-10-18-54
data: 2026-10-18
branch: claude/blissful-pasteur-gkiz2m
base_commit: 0de7534
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATA v1.11 HOMOLOGADAS (DHR-SPEC006-002/-003); H-001 ABERTA — Andraus quer levá-la à decisão final (tecnologia incluída) após medir hash/sincronização e criar o roteamento por tarefa; próxima Spec do ROADMAP = SPEC-007 (abertura pendente)
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual — necessidades e prioridades de Andraus (chat, 2026-10-18)
Ordem de execução pedida por Andraus (**nada abaixo foi executado, exceto a medição**):
- **P0 — Medir antes** a eficácia do **hash** (`spec_delta`) e da **data de última sincronização** (carimbo RPSA) para economizar releitura. **FEITO (Fase 0):** hash/delta −26% a −31% por rodada (151 mil × 203–218 mil tokens), manter; carimbo dispensa ≈ 15 atas (≈ 15 mil tokens/rodada), manter. Desperdício real = agente caro em ajuste mínimo + rodada integral repetida. Registro: final de `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md`.
- **P1 — Roteamento de modelos por criticidade/tarefa (Fase 1).** Vontade de Andraus: o **Orquestrador organiza as tarefas e AGRUPA as que exigem um mesmo modelo** (Opus 5.5 × Sonnet 5.5) e resolve cada lote **na chamada dos agentes**; **Especificador e Revisor devem usar modelos diferentes conforme a tarefa**; tudo **garantido de forma determinística pelo Orquestrador ANTES de chamar os agentes**. **Tarefas de alteração mínima o próprio Orquestrador executa, em estrita observância determinística dos relatórios de não conformidade do Revisor** — objetivo: **prevenir rodadas caras de agentes internos para tarefas mínimas**. Desenho (revisado por Andraus em 2026-10-18 — **2 agentes, não 4**): classes **M** (Orquestrador: achado com arquivo:linha + texto antigo→novo + condição verificável, sem criar regra/campo/mecanismo; o delta deve mostrar só as linhas listadas; falha de gate ⇒ escala), **S** (Sonnet 5.5: auditoria por delta), **O** (Opus 5.5: desenho); **regra de congelamento** (correção não cria mecanismo). Mantêm-se `especificador` (Opus 5.5) e `revisor` (Sonnet 5.5) no frontmatter; o **hook roteador aceita `model` por chamada só se igual ao da tabela da classe** e é **fail-closed** no override (classificação falhou ⇒ vale o frontmatter). Continuar o **mesmo agente por `SendMessage`** quando o modelo for o mesmo (menos releitura). **Esforço (`effort`): coluna reservada e DESLIGADA até um piloto** (~150–200 mil tokens: mesma revisão por delta em 2 níveis com defeitos plantados); motivo: rebaixar o Revisor já custou achados (Sonnet 4.6: 0/18 × 14/18).
- **P2 — H-001: decisão final, tecnologia incluída, sem pendência nem quebra documental (Fase 2)**, só depois da P1 (para já usar o roteamento). Um **PR atômico** + `check_doc_sync` etc.
- **P3 — Processo:** menos PRs (**um por frente de trabalho**; mesclar documentos sozinho com CI verde — `AGENTS.md` §10), **detector de ramos órfãos** na abertura da sessão (entra com a Fase 1), e **Andraus liga "apagar ramo após o merge"** no GitHub. Os 12 ramos já contidos na main continuam a apagar (lista no §2).
- **Regras de Andraus para o PR:** o PR do plano + handoff **vai JUNTO com a Fase 1, num PR só**. Enquanto isso, tudo fica no ramo `claude/blissful-pasteur-gkiz2m`.
- **Autorização:** a Fase 1 mexe em arquivos protegidos (emenda à `DHR-ROTEAMENTO-003`, `scripts/roteador_modelos.py`, selo; **não** mais agentes novos nem `AGENTS.md` §3) e **Andraus NÃO autorizou iniciá-la nesta sessão** (pediu deixar tudo descrito e pronto). A próxima sessão deve abrir com **UMA** pergunta (AskUserQuestion) pedindo a ordem expressa da Fase 1, já com o checklist do §5.

## 2. Estado (fatos conferidos em 2026-10-18)
- `main` = `0de7534` (PRs #118, #119, #120 mesclados). CI verde; verificadores sem ERRO (resíduo herdado: `check_refs` 1 ERRO em `governance/propostas/AUDITORIA-INDEPENDENTE-SPEC006/RELATORIO.md:227`; COE-14 WARN: `gate_extra.py`/`spec_delta.py` fora de `governance/MECANISMOS.json`).
- **SPEC-006 (13 funções `CKG-001..013`, nomes e regras fixos) = baseline v1.7 + errata v1.11 (Major, condicionada)**; plan.md sha256 `0f461e88…` (auditado `8527addb…`; adendo na ata). Parecer do Revisor = CONFORME condicional (teto: H-001 aberta).
- **Não foi subdividida em Specs numeradas.** A "divisão" escolhida (Opção 2, mesmo número em etapas) vivia só no Plan v1.8 da linha `spec006-plan`, **arquivado** em `governance/propostas/SPEC-006/linha-spec006-plan/` (INV-07). Ata da Opção 2 renomeada `DHR-SPEC006-OPCAO2-001`. ROADMAP:177 já diz "H-001 permanece ABERTA".
- PRs #31 e #2 **fechados**. Seguem **12 ramos remotos totalmente contidos na main (0 commits próprios) NÃO apagados** (a sessão não exclui ramo remoto): assinatura-delegacao-merge, ccr-63ea68aa-ks4bkd, ccr-7917ac44-2l55cz, ccr-a5f30778-9nezl9, ccr-d43bf9b0-h336k5, claude/new-session-ch6cqa, f3-aplicacao, gate-detectores, revisor-modelo-metodo-v2, revisor-passo8-i001-l001, rpsa-registra-013-assinatura, spec006-abertura-homologada. Os 8 ramos com commits próprios estão na lista `governance/propostas/SPEC-006/LISTA-RAMOS-E-PRS-OBSOLETOS-2026-10-18.md` (intocados).

## 3. Histórico resumido (HO-34..51; cópias integrais em `docs/handoffs/`)
- Linha da `main` refez a SPEC-006 (Plan v1.6→v1.8, rodadas 5–9) sem saber que a v1.7 já fora homologada (2026-10-13) no ramo `ccr-63ea68aa-ks4bkd`; descoberto e reconciliado no PR #118 (Andraus: "conciliar e integrar"). Ferramentas trazidas: `spec_delta.py`, `gate_extra.py`, atas `DHR-BACKLOG-ABERTURA-001` e `DHR-REVISOR-DELTA-001` (edições aplicadas em `especificador.md`/`revisor.md`; selo regravado; RPSA ok).
- Errata v1.11 (N-08 + menores) → Revisor por delta CONFORME condicional → homologada por Andraus (`DHR-SPEC006-003`; negação de `conviction` por padrão registrada com condição de reversão; **não fecha M-001**). Registrada em ROADMAP/CATALOGO (#120).
- Lições: não empurrar WIP enquanto o Especificador edita (CI vermelho pelo mapa/gate); ao reescrever o handoff, arquivar o anterior como **cópia exata** (`check_handoff` HO-04) e não citar ata inexistente (HO-06); heredoc sem aspas expande crases — usar `'EOF'`.

## 4. Verificado
Ver §2. Nenhum código alterado nesta rodada (só documentos).

## 5. Próximo passo único (checklist pronto para a próxima sessão)
**0. Reverificar (§9) e ler o plano** `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md`. **1. Pedir a ordem expressa da Fase 1** (uma pergunta). Com ela:
**Fase 1 (um PR):** (a) `scripts/roteador_modelos.py`: classificador M/S/O em código (critérios objetivos: nº de linhas/blocos, presença de arquivo:linha + ação prescrita, ausência de regra/campo novo) + tabela classe→modelo; hook passa a **validar `model` contra a tabela** (aceita igual, nega diferente; fail-closed no override; `effort` segue negado) + testes (`tests/test_roteador_modelos.py`, CI); (b) rotina do Orquestrador para classe M (ficha de correção → aplicar → gates → `spec_delta` só nas linhas listadas → escala se divergir); (c) `scripts/check_branches.py` (ramos à frente da main não citados no handoff; informativo) ligado ao SessionStart + registro em `governance/MECANISMOS.json` (evita WARN COE-14); (d) emenda à `DHR-ROTEAMENTO-003` (RPSA `nao`: texto dos agentes não muda); (e) selo (`gate_manifest.py --write`) **só com a autorização**; (f) suíte, CI, PR único com plano+handoff. **Piloto de esforço** à parte, depois (não bloqueia a Fase 1).
**Fase 2 (H-001), depois:** (1) Especificador-Opus: estudo [PROPOSTA] (opções: property graph · grafo temporal tipo Graphiti · estrutura em memória/relacional + log append-only · híbrido; critérios INV-07, E3 fail-closed, trace CEM-001, 4Es; reusar Dossiê válido até 2027-01-03); (2) Andraus escolhe a tecnologia (AskUserQuestion); (3) mapa determinístico de ocorrências (ROADMAP 6 · AGENTS 1 · atomic-spec 6 · revisor.md 3 · especificador.md 4 · CATALOGO 23 · RULES 6 · RMR-001 20 · CIC-001 · plan/checks da SPEC-006); (4) PR atômico com ata nova, ROADMAP (seção de decisões), `AGENTS.md` §7, `atomic-spec.md` §12, `revisor.md` §8 (remove o teto "condicional" só da SPEC-006 — H-001 era o único bloqueador dela), RMR-001 (BL-003), CATALOGO/CIC, errata da SPEC-006 (referências do mecanismo físico) com Revisor **por delta**; (5) verificadores + CI verde + mescla. **Seguem como estão (abertas):** G-001, K-001, M-001, J-001, N-001, C-001, WF-D03.
Pendências só de Andraus: ligar "apagar ramo após o merge"; abertura da SPEC-007 (ROADMAP §23 passo 1-bis); demais decisões abertas. Lembrete vigente: assinar o registro de mecanismos como VIGENTE [PRAZO: 2026-10-24].

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
- `DHR-SPEC006-001` (abertura), `-002` (baseline v1.7), `-003` (errata v1.11), `DHR-SPEC006-OPCAO2-001` (intenção Opção 2; registro histórico). Decisões abertas/fechadas: ler "Decisões abertas ativas" e "Decisões FECHADAS" do `ROADMAP.md`. **Nenhuma fechada nesta sessão.**

## 7. Becos sem saída
- Dar Bash ao Revisor: rejeitado (DHR-AUDITOR-EXTERNO-009 §2). Não reabrir sem Andraus.
- Refazer a SPEC-006 do zero na linha `spec006-plan`: já foi (HO-34..40) e é redundante; a baseline é a v1.7+v1.11.
- Dividir a SPEC-006 em Specs numeradas: **não decidido**; a ata de 13/10 diz "não dividida". Só por Andraus.

## 8. Não tocar
- `canon/` BASELINED, specs homologadas (`plan.md` da SPEC-006 só por errata/ordem), `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/*`, `AGENTS.md` (só por Andraus). Não regravar `GATE-MANIFEST.sha256` sem decisão dele.

## 9. Reverificar ao vivo
- [ ] `git log -1` == `base_commit` (0de7534) ou posterior; se posterior, ler o diff
- [ ] CI da `main`; `python scripts/gate_manifest.py --check`; `check_refs.py`/`check_doc_sync.py`/`check_handoff.py`
- [ ] `python scripts/backlog_triggers.py` (BL-003/BL-011 ATIVADOS; BL-010/BL-029 em espera)
- [ ] PRs abertos (esperado: nenhum além de novos); ramos remotos (12 contidos ainda existem?)
- [ ] ROADMAP: "Decisões abertas ativas" ainda lista H-001; linha 177 diz "permanece ABERTA"
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)

## 10. Aguardando Andraus
- H-001 (esta frente) · apagar os 12 ramos · SPEC-007 · demais decisões abertas (§5).
- Registro de mecanismos VIGENTE [PRAZO: 2026-10-24]; destino do Auditor Externo (PAUSADO), schemas sem `additionalProperties:false`, roteamento de modelos (onda 1), D-PCC-3/4/5 — ver `docs/handoffs/HO-2026-10-17-34.md` §10 (histórico).

## 11. Ponteiros
`governance/DHR-ROTEAMENTO-001_*` · `governance/DHR-AGENTES-001_*` · `docs/agentes/INDICE-AGENTES.md` · `governance/DHR-AUDITOR-EXTERNO-016_Ata_Fusao_dos_Subagentes_Antigos_no_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-015_Ata_Brechas_de_Ferramenta_e_Medicao_do_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-009_*` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
