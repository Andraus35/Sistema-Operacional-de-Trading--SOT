---
handoff_id: HO-2026-10-18-53
previous: HO-2026-10-18-52
data: 2026-10-18
branch: claude/blissful-pasteur-gkiz2m
base_commit: 0de7534
spec_autorizada: SPEC-006 = BASELINE v1.7 + ERRATA v1.11 HOMOLOGADAS (DHR-SPEC006-002/-003); H-001 ABERTA — Andraus quer levá-la à decisão final (tecnologia incluída) após medir hash/sincronização e criar o roteamento por tarefa; próxima Spec do ROADMAP = SPEC-007 (abertura pendente)
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual
**HO-53 (Andraus, AskUserQuestion, 2026-10-18):** (1) plano APROVADO para começar pela **Fase 0 — CONCLUÍDA** (medição no próprio plano: hash/delta −26% a −31% por rodada, manter; carimbo ≈ 15 mil tokens/rodada, manter; desperdício real = agente caro em ajuste mínimo e rodada integral repetida). (2) **Processo — escolhidos:** detector de ramos órfãos na abertura da sessão (entra com a Fase 1), **menos PRs: um por frente de trabalho** (mesclar documentos sozinho com CI verde, como o `AGENTS.md` §10 já permite), e **Andraus liga "apagar ramo após o merge" no GitHub** (Settings; a sessão não exclui ramo remoto). (3) **O PR do plano + handoff NÃO foi aberto: vai junto com a Fase 1, num PR só.** Plano e handoff ficam no ramo `claude/blissful-pasteur-gkiz2m`. **Fase 1 depende de ordem expressa de Andraus** (novos `.claude/agents/*`, `AGENTS.md` §3, emenda à DHR-ROTEAMENTO-003, RPSA, selo) — não iniciada.

(Texto anterior HO-52:)
**ATUALIZAÇÃO HO-52 (ordem de Andraus, 2026-10-18):** em vez de só "abrir", levar a H-001 à **decisão final por inteiro, tecnologia incluída, sem pendência nem quebra documental**, depois de (a) medir a eficácia do hash (`spec_delta`) e do carimbo de sincronização (RPSA) e (b) implantar o **roteamento determinístico por tarefa** (Orquestrador agrupa por modelo: Opus 5.5 desenho × Sonnet 5.5 auditoria; faz sozinho as correções mínimas seguindo os relatórios do Revisor). **Plano (PROPOSTA): `governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md` — aguardando aprovação de Andraus.** Andraus pediu para **aguardar o plano antes de abrir o PR do handoff**. Nada do plano foi executado; nenhuma decisão alterada.

(Texto anterior HO-51:)
**Abrir a H-001** (ordem de Andraus no chat, 2026-10-18: "vamos abrir H-001"). H-001 = *"Knowledge Graph: grafo real ou estrutura em memória?"* (`atomic-spec.md` §12 l.378), dona nominal SPEC-006, hoje **ABERTA**. "Abrir" = levar a decisão a Andraus com estudo e perguntas; **NÃO é fechar**. Fechar exige decisão expressa dele + ata + atualizar `ROADMAP.md` ("Decisões FECHADAS") e `AGENTS.md` §7.

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

## 5. Próximo passo único
**Aprovação do plano por Andraus** (`governance/propostas/PLANO-FECHAR-H001-E-ROTEAR-MODELOS-2026-10-18.md`): Fase 0 medir → Fase 1 roteador/2 agentes por papel (ordem+ata) → Fase 2 decisão final da H-001. Detalhe do estudo da H-001 (antes "abrir"):
1. Ler: `atomic-spec.md` §12 l.378; `governance/DHR-SPEC006-001_*` (Q-ABERTURA-3: regras do contrato FECHADAS, tecnologia de armazenamento EM ABERTO — "Opção A"); `specs/features/SPEC-006/research.md` (conclusão: "Knowledge Graph" no SOT = memória semântica permanente, **não** necessariamente banco de grafos; KERNEL-V2 l.1101-1104) e `specs/features/SPEC-006/sources/REPO-{graphiti,cognee,graphrag,mem0}.txt`, `SRC-ZEP-01.txt`, `SRC-MEMVSKG-01.txt`; `plan.md` (limites declarados "integridade física sem digest", "eficiência de travessia ampla = H-001/BUILD").
2. Acionar o **Especificador SOT** para uma **PROPOSTA** de estudo da H-001: opções (p.ex. grafo real/property graph · grafo temporal estilo Graphiti · estrutura em memória/relacional + log append-only), critérios (imutabilidade INV-07, auditoria E3 fail-closed, trace completo CEM-001, custo/Economicidade só depois de Eficácia — 4Es, SOT não executa ordem), o que cada opção exige de BUILD, gatilhos e dependências. **Rotular [PROPOSTA]; nada vira baseline.**
3. Levar a Andraus por **AskUserQuestion** (linguagem simples; recomendação primeiro). Só se ele mandar encerrar a H-001: ata nova (`DHR-…`), registro em `ROADMAP.md` e `AGENTS.md` §7, tratamento do teto "CONFORME condicional" e reavaliação do BL-003 (gatilho SPEC-006/SPEC-009) — **só por ordem expressa**; as outras decisões abertas seguem como estão.
Gatilhos que a H-001 destrava/toca: **BL-003** (persistência física; SPEC-009/G-001), **K-001/SPEC-018** (allowlist de escritores, host do juízo causal, timeout), **SPEC-007** (selo de publicação/entrada, CKG-010), **SPEC-005** (eventos), **M-001** (conviction no KG).
Pendências só de Andraus: apagar os 12 ramos; autorizar a abertura da SPEC-007 (ROADMAP §23 passo 1-bis); demais decisões abertas (J-001, N-001, G-001, K-001, C-001, M-001, WF-D03, ECC-03-001, SPEC-045-RUNTIME-001, CKG-STRUCT-ORIGIN-001). Lembrete vigente: assinar o registro de mecanismos como VIGENTE [PRAZO: 2026-10-24].

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
