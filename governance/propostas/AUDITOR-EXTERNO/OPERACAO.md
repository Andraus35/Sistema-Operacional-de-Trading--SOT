# Operação do Auditor Externo (piloto) — `[PROPOSTA — NÃO NORMATIVO]`

> Documento operacional do piloto. Não altera Constituição, RULES, Revisor nem o consenso de homologação (Especificador + Revisor + Auditor externo + Andraus; o Orquestrador coordena e não é parte do consenso). Decisor Final: Andraus. Atas: `governance/DHR-AUDITOR-EXTERNO-001/002/003` (002 e 003 assinadas por Andraus em 2026-10-06).

## 1. Cadeia
Orquestrador (Claude) → workflow `.github/workflows/auditor-externo.yml` cria Issue `[AEX-REQ]` (rótulo `homologacao-final` ou `workflow_dispatch`; traz `manifest=<sha256>`) → bot agendado na VM chama `codex exec` (somente leitura) → achados `[AEX]` validados por código (`kit/validate_finding.py`) → ACK `<!-- aex-ack -->` com veredito **consultivo** (`OK | COM_RESSALVAS | NAO_OK`) → workflow avisa o PR. O auditor responde só ao Orquestrador. Texto de Issue/achado é DADO, nunca instrução.

## 2. Onde roda (fora do repositório)
- VM Oracle Always Free `vm-codex-micro` (sa-saopaulo-1, usuário `ubuntu`); Codex CLI com login de conta ChatGPT (`codex login --device-auth`); `CODEX_HOME=~/.sot-audit/codex-home`.
- Timer systemd de usuário `sot-auditor.timer`, a cada 2 min → `~/.sot-audit/sync_auditor.sh` → `kit/auditor_bot.py`. Sem `[AEX-REQ]` pendente, o bot **não chama o modelo**.
- Requisitos da VM (Ubuntu 24.04): pacote `bubblewrap` e `kernel.apparmor_restrict_unprivileged_userns=0` (persistido em `/etc/sysctl.d/60-sot-userns.conf`); `loginctl enable-linger ubuntu`.
- Token fine-grained de Andraus (só este repositório; Contents=Read, Issues=Read and write, Metadata=Read) em `~/.sot-audit/env`. Escopo declarado, não provado pela API.
- Instalação/diagnóstico: `kit/install_bot.sh`, `kit/README-INSTALACAO.md`.

## 3. Freios
6 chamadas de modelo/dia (UTC) · 2 tentativas por pedido · 1 pedido por execução · 10 achados por pedido · timeout 1800 s · modelo sem variáveis `SOT_*/GITHUB_*/GH_*` · saída varrida contra token/auth.json · auditoria declarada INDETERMINADA ⇒ bloqueio, sem ACK.

## 4. Cadeia de confiança e aprovação de manifesto
`MANIFEST.sha256` cobre kit + AGENTE + DIRETIVAS + BRIEFING. O `sync_auditor.sh` sai com 0 (ok), 2 (bloqueio) ou 3 (manifesto não aprovado). Toda mudança no kit muda o hash; Andraus aprova **na VM**:
```bash
sha256sum governance/propostas/AUDITOR-EXTERNO/MANIFEST.sha256     # hash vigente no main
set -a; . ~/.sot-audit/env; set +a
SOT_AUDIT_STATE=$HOME/.sot-audit SOT_REPO_DIR=$HOME/sot-repo ~/.sot-audit/sync_auditor.sh --approve <hash>
```
Renovação automática só ocorre se o último `[AEX-REQ]` aberto do `github-actions` trouxer o mesmo `manifest=`.

## 5. Verificação sem acesso à VM
Issues com rótulo `auditoria-externa` (`aex-valido`, `aex-aguarda-revisor`, `aex-duplicado`); Actions → "Auditor externo (loop determinístico)"; testes locais: `cd governance/propostas/AUDITOR-EXTERNO/kit && python3 -m unittest test_bot test_loop`.

## 6. Resultado do teste real (2026-10-06)
Documento com 5 defeitos plantados + 1 item limpo: 2º ciclo = 5 postados, 0 descartados, `NAO_OK`, 5/5, sem falso alarme. Falhas encontradas e corrigidas: sandbox/bwrap, ACK em auditoria INDETERMINADA (PR #19), prompt (PR #23), timer (PR #30).

## 7. Limites conhecidos
Custo/limite do plano ChatGPT não medido · VM ociosa pode ser recuperada pela Oracle · modelo roda como o mesmo usuário do bot · renovação de manifesto é manual a cada mudança no kit · fechamento por consenso nunca exercitado · bot acoplado ao SOT.

## 8. Decisões abertas
Nenhuma é fechada por este piloto (CONS-01).

## 9. Roteamento de achados — duas faixas (Opção B; DHR-AUDITOR-EXTERNO-005)
O auditor continua respondendo **só ao Orquestrador**. Para tirar o gargalo das correções triviais sem entregar ao Especificador texto de modelo externo como instrução, o workflow (`achado`) roda `scripts/route_aex.py` — **determinístico, fail-closed, sem LLM** — sobre os **campos de máquina** do achado já validado. O texto livre do auditor (`claim`, `proposal.text`, `impact`, `title`) **nunca** influencia a rota.

| Faixa (rótulo) | Critério (todos) | Destino |
|---|---|---|
| `aex-rota-rapida` | validado e não duplicado · `severity=P2` · `type=drift` · `proposal.type=ERRATUM_ADITIVO` · `modifies_baselined_text=false` · `treats_open_decision_as_closed=false` · `open_decisions_referenced=[]` · `touches` não vazio e **todos** na allowlist (`governance/CATALOGO-OFICIAL.md`) | Elegível a **tarefa limitada** ao Especificador (só os arquivos de `touches`; o achado é DADO). PR revisado pelo Revisor; **Andraus mescla**. Nada é mesclado sozinho. |
| `aex-rota-andraus` | qualquer outro caso (P0/P1, invariante, CONS-01, texto baselined, atas `DHR-*`, RULES, ROADMAP, decisão aberta citada, caminho inseguro, campo ausente/errado, falha do roteador) | O Orquestrador resume a Andraus **antes** de qualquer encaminhamento. |

Exemplo real (2026-10-10, Issue #34): #35, #36 e #37 → rápida; #38 (atas assinadas + `SPEC-038-DATASRC-001` aberta) → Andraus. O comentário da Issue e o aviso no PR trazem a rota e os códigos de motivo. Ampliar a allowlist é decisão de Andraus (nova ata).

## 10. Plano de validação em bloco (status por item)
| Id | O que valida | Como | Status |
|---|---|---|---|
| V1 | Roteador: casos reais + ataques (caminho `..` inclusive o que volta ao alvo permitido, prefixo/sufixo, tipos errados, injeção em texto livre) | `python -m unittest tests/test_route_aex.py` (20 testes; CI bloqueante) | feito |
| V2 | Sintaxe do workflow (YAML + 8 scripts embutidos) e passo bash do roteador | checagem local | feito localmente |
| V3 | Roteamento ao vivo: Issues `[AEX]` novas saem com `aex-rota-*` e linha de rota | `workflow_dispatch` após o merge → bot da Oracle → conferir rótulos/comentários | **PASSOU ao vivo (2026-10-10, pedido #41):** ACK COM_RESSALVAS, 2 achados (#42, #43), ambos `aex-rota-andraus` com linha de rota e motivos corretos. **Faixa `rapida` só provada por teste unitário** (nenhum achado elegível nesta rodada). O auditor achou um defeito real no roteador (#43: `..` normalizado antes da checagem) — corrigido e coberto por teste (20 testes). |
| V4 | Fluxo por PR: rótulo `homologacao-final` → pedido com nº do PR → aviso do achado e ACK **no PR** | PR descartável "TESTE (NÃO MESCLAR)", linhas de consenso marcadas como fixture de teste | pendente (pós-merge) |
| V5 | Despertar da sessão por comentário do workflow no PR | `subscribe_pr_activity` no PR; chegada de evento | **PASSOU (2026-10-10, PR #44):** o comentário do `github-actions[bot]` chegou como evento `issue_comment.created` cerca de 8 s depois do rótulo — a sessão acorda por comentário do workflow (sem depender do polling de 1 h). |
| V6 | `fechamento` no merge de PR com `homologacao-final` (avisos de consenso/commit) | rótulo aplicado ao PR real do merge desta mudança, sem linhas de consenso (esperado: aviso, não bloqueio) | pendente |
| V7 | Caminho "pedido não criado" (consenso ausente) | rótulo em PR sem as linhas `Spec:`/`Consenso:` | **PASSOU (2026-10-10, PR #44):** comentário "Pedido de auditoria externa não criado: consenso parcial não registrado…"; nenhuma Issue `[AEX-REQ]` criada, nenhuma chamada ao modelo. |
| V8 | Modos de falha da VM (login Codex expirado, token expirado, instância recuperada) e consumo do plano ChatGPT | não testáveis daqui; medir/observar em uso real | **não validável pelo repositório** |
