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
