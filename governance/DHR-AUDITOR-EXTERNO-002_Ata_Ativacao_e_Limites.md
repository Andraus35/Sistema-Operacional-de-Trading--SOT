# DHR-AUDITOR-EXTERNO-002 — Ata — Ativação do canal do Auditor Externo (piloto) e limites conhecidos

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisões e atos de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-06 |
| Status | **ASSINADA por Andraus (chat, 2026-10-06) — ver Adendo.** Registra fatos de ativação executados por Andraus (chat, 2026-10-05/06) e os limites que ficaram. Não altera `AGENTS.md`, o Revisor, o ROADMAP nem decisão aberta. |
| Compatibilidade | n/a (registro operacional do piloto de DHR-AUDITOR-EXTERNO-001; nenhuma BASpec, regra ou decisão aberta alterada) |
| Regime | Piloto controlado (DHR-AUDITOR-EXTERNO-001 §1). Aditivo (INV-07): nenhuma ata anterior editada. |

## 1. Decisões de Andraus `[FATO: chat, 2026-10-05/06]`
1. **Via de acesso:** num repositório de conta pessoal não existe colaborador somente-leitura (verificado na documentação oficial do GitHub); Andraus escolheu **token fine-grained próprio**, escopo mínimo, restrito a este repositório (emenda ao item 6 de DHR-AUDITOR-EXTERNO-001 §1, que previa conta dedicada com papel Read).
2. **Ativação:** Andraus criou os 7 rótulos e as variáveis `AUDITOR_EXTERNO_LOGINS=Andraus35` e `AUDITOR_EXTERNO_ENABLED=true` (declarado por Andraus; **as variáveis não são legíveis pela API desta sessão**, mas o efeito é comprovado em §2.3).
3. **Ambiente do auditor:** Codex em nuvem, token em `SOT_AUDITOR_TOKEN` (variável de ambiente), domínios `api.github.com` e `github.com` liberados.

## 2. Evidências `[FATO]`
1. **Rótulos:** os 7 existem (`auditoria-externa`, `homologacao-final`, `aex-valido`, `aex-invalido`, `aex-duplicado`, `aex-aguarda-revisor`, `aex-fila-cheia`) — conferidos por `get_label`.
2. **Escopo do token:** tela do GitHub mostrou Contents = Read-only e Metadata = Read-only, repositório único. **Issues** aparecia como Read-only; Andraus foi orientado a mudá-lo para Read and write — **a mudança não foi confirmada por imagem**.
3. **Teste do canal (PRs descartáveis #10 e #13, fechados sem merge):** a chave está ligada; o job `pedido` criou as Issues `[AEX-REQ]` #11 e #14 com os rótulos corretos. Na 1ª rodada o comentário no PR falhou com 403 (`pull-requests: read`); corrigido por `pull-requests: write` (PR #12); na 2ª rodada o comentário foi postado e o job concluiu sem erro. Issues #11 e #14 fechadas como não planejadas.
4. **Verificador:** `kit/verify_access.py` — duas sondas de escrita deram **falso positivo** contra a API real (POST vazio → 422; blob válido → 201 com Contents Read-only na tela); o script passou a ser **fail-closed** e só passa com `--confirmo-escopo` (PR #9). Com a flag, o Codex relatou `PASS`.

5. **Primeiro atendimento real (Codex), 2026-10-06:** parou **corretamente** sem auditar — o passo 0 do procedimento exigia `MANIFEST.sha256`, que não existia no repositório (defeito do procedimento, não do auditor); o passo 1 também omitia `--confirmo-escopo`. Corrigidos: `governance/propostas/AUDITOR-EXTERNO/MANIFEST.sha256` gerado (kit + diretivas + AGENTE + BRIEFING) e procedimento ajustado.

## 3. Limites conhecidos `[FATO]` (declarar ≠ verificar)
- **Escopo do token declarado, não provado:** a API não permite verificá-lo para token do dono; vale a conferência manual na tela do GitHub.
- **Identidade:** as ações do auditor aparecem com o login de Andraus; `AUDITOR_EXTERNO_LOGINS=Andraus35` não distingue o auditor do dono (a separação é por prefixo `[AEX]` e validação do kit).
- **O auditor (GPT/Codex) ainda não atendeu nenhum pedido real:** o teste cobriu o lado do repositório (workflow, rótulos, Issue, comentário), não `poll_requests`/`setup_auditor.sh`/`submit_finding`/`--ack`.
- **Fechamento por merge** (aviso de consenso do Auditor) não foi exercitado.
- **Manifesto no mesmo repositório:** `MANIFEST.sha256` detecta corrupção/divergência acidental, não um repositório comprometido; âncora = hash do manifesto informado ao auditor por canal fora do repositório (chat de Andraus). Deve ser regenerado a cada mudança nos arquivos cobertos.
- **Validade do token** não registrada: renovar antes de expirar; revogar se houver suspeita de vazamento.

## 4. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**; o papel do auditor segue **piloto** (normatização só por decisão posterior de Andraus).

**Erratum aditivo (2026-10-10, achado AEX-20261010-004 — proposto pelo orquestrador; **RATIFICADO por Andraus no chat, 2026-10-10**):** em `SPEC-038-DATASRC-001`, o **recorte "TradingView como uma das fontes, via adapter"** foi **DECIDIDO** por Andraus em `DHR-DEC-004` §1.2 (2026-10-03); permanece **ABERTA** a **escolha do provedor de dados de máquina** (order flow, futuros, BTC multi-exchange), diferida ao Discovery/benchmark do MASTER (BL-033). A lista acima é o registro à data da assinatura; esta nota não fecha a decisão inteira (CONS-01).

## 5. Classificação RPSA `[INFERÊNCIA do orquestrador — a ratificar por Andraus]`
Fora de escopo dos agentes (§4.1): é registro operacional de ativação de fluxo já decidido em DHR-AUDITOR-EXTERNO-001 (classificada em escopo, `fonte-unica`); não altera checklist, método nem regra. Registrada no livro-razão como `em_escopo=false`.

## 6. Registro
- [x] Esta ata · [x] `governance/rpsa-ledger.json` · [x] `governance/CATALOGO-OFICIAL.md` · [x] `build_map.py` + `--check` · [ ] **assinatura de Andraus — pendente**.

## Adendo (2026-10-06, antes da assinatura) — fatos posteriores que SUPERAM itens de §2/§3 `[FATO]`
- **§3, "o auditor ainda não atendeu nenhum pedido real" — SUPERADO.** O bot agendado (DHR-AUDITOR-EXTERNO-003) atendeu pedidos reais na VM Oracle: ciclo 1 (Issue #17): 3 achados postados e 2 descartados pela validação determinística (comando de reprodução com `|` entre aspas); ciclo 2 (Issue #24, após correção do prompt, PR #23): **5 postados, 0 descartados**, veredito `NAO_OK`. Contra o documento de teste `TESTE-PILOTO-001.md` (5 defeitos plantados + 1 item limpo): **5/5 achados, nenhum falso alarme no item limpo**. O workflow validou e rotulou os achados, deduplicou os repetidos e avisou o PR de teste (#16).
- **§2.2, escopo do token:** Andraus declarou em chat (2026-10-06) que a tela do GitHub mostra **Issues = Read and write**; segue **declarado, não provado** pela API. Os achados e o ACK foram de fato postados com o token, o que é coerente com a declaração.
- **§3, "fechamento por merge não exercitado":** continua válido.
- **Encerramento do teste:** PR #16 fechado sem merge; Issues #17, #20–22, #24–29 fechadas como não planejadas; a branch remota `auditor-teste-piloto-001` fica para Andraus apagar (a sessão não tem permissão de delete remoto).
- Nenhuma decisão aberta foi fechada; a classificação RPSA de §5 **não foi ratificada por esta assinatura** (permanece a ratificar).

---

**Andraus** — *assinada por decisão direta em chat, 2026-10-06 ("assinar atas"); registro feito pelo Orquestrador interno a pedido de Andraus.*
