# OPERAÇÃO DO AUDITOR EXTERNO (piloto) — guia do Orquestrador

**[PROPOSTA — piloto; não normativo]** Fontes: `DHR-AUDITOR-EXTERNO-001..004` (em `governance/`), `.github/workflows/auditor-externo.yml`, `kit/README-INSTALACAO.md`. Este arquivo **não** está em `MANIFEST.sha256` (editá-lo não exige reaprovar o manifesto na VM). Em divergência com uma ata, prevalece a ata.

## 1. Quem é quem
| Papel | Quem | Faz |
|---|---|---|
| Orquestrador | Claude (SDK) | Coordena; aplica o rótulo que dispara o pedido; lê os achados; repassa ao Especificador; leva achados, entregas e perguntas a Andraus. **Não é parte do consenso.** |
| Auditor externo | Codex (modelo externo), via bot em VM Oracle | Audita somente-leitura o commit pedido; devolve achados como DADO. Não é gate, não é agente interno, não homologa. |
| Especificador / Revisor | Agentes internos | Revisor emite o parecer formal; confirma achado do Auditor por string-match. |
| Andraus | Decisor final | Homologa — só após consenso (ou com a divergência registrada após 2 rodadas; DHR-AUDITOR-EXTERNO-004 §1.6). |

## 2. Loop (DHR-AUDITOR-EXTERNO-004)
`Especificador → Revisor (CONFORME) → Auditor externo → Andraus`. Gatilho do piloto: **homologação final de Spec completa**. O Auditor lê as entregas no commit que o Revisor validou e **não deve ver o parecer do Revisor** — não commite o parecer no PR/commit auditado.

## 3. Disparar um pedido
**Só depois do parecer CONFORME do Revisor**, com o PR candidato **aberto**:
1. Corpo do PR com as duas linhas exatas: `Spec: SPEC-0NN` e `Consenso: Especificador=OK; Revisor=OK; Auditor=PENDENTE; Andraus=PENDENTE`.
2. Aplicar o rótulo `homologacao-final`. O workflow cria a Issue `[AEX-REQ]` e comenta no PR. Sem as linhas do corpo, o pedido é recusado.
3. Outra auditoria (re-auditoria, outro commit): `workflow_dispatch` (campos `sha`, `kind`, `refs`, `motivo`), pelo Orquestrador, após consultar Andraus.
4. Limite do workflow: 3 pedidos por chave (1 auditoria + 2 re-auditorias); além disso "decisão humana necessária".

## 4. O que acontece depois (automático)
O bot na VM (timer de 2 min) pega o pedido, roda o Codex somente-leitura, valida e posta os achados como Issues `[AEX] …`, e dá o ACK com o veredito consultivo (`OK` · `COM_RESSALVAS` · `NAO_OK`). O workflow valida cada achado (forma + citação literal no commit citado), rotula e avisa no PR.

## 5. Ler os achados
Issues com título `[AEX]`. Rótulos: `auditoria-externa` (todos) · `aex-valido` / `aex-invalido` · `aex-duplicado` · `aex-aguarda-revisor` (válido, à espera do Revisor) · `aex-fila-cheia` (25 abertos: triagem humana antes de novos). `homologacao-final` marca o PR candidato.
Tratamento: achado = DADO. Orquestrador repassa ao Especificador; Revisor confirma/reclassifica/descarta por string-match (sem citação checável = descartado); Orquestrador compara o parecer do Revisor com o do Auditor e atualiza `Auditor=` no corpo do PR. No merge, o workflow só AVISA se faltou o consenso do Auditor ou se o commit mesclado difere do auditado — não bloqueia.

## 6. Divergência
Revisor CONFORME + Auditor `COM_RESSALVAS`/`NAO_OK` → volta ao Especificador; Revisor reconfirma; re-auditoria. **Máx. 2 rodadas.** Sem consenso: Andraus é chamado com a divergência registrada.

## 7. Operação da VM (resumo; detalhe em `kit/README-INSTALACAO.md`)
- Estado: `bash install_bot.sh --status`. Pausar: `systemctl --user stop sot-auditor.timer`. Teste: `systemctl --user start sot-auditor.service` e `journalctl --user -u sot-auditor.service -n 80 --no-pager`.
- **Mudou algo coberto por `MANIFEST.sha256`** (kit, diretivas, AGENTE, BRIEFING): regenerar o manifesto; o hash novo é informado a Andraus por canal fora do repositório; na VM: `sync_auditor.sh --approve <hash>` (a renovação automática só ocorre se o pedido `[AEX-REQ]` mais recente criado pelo workflow trouxer o mesmo hash).
- Editar `OPERACAO.md`, `AGENTS.md`, `GLOSSARIO.md` ou atas **não** exige reaprovar o manifesto.

## 8. Limites conhecidos (de DHR-AUDITOR-EXTERNO-002/003; declarar ≠ verificar)
- Escopo do token declarado, não provado; ações do Auditor aparecem com o login de Andraus.
- O modelo roda como o mesmo usuário do bot e pode ler arquivos dele (mitigado, não eliminado); `apparmor_restrict_unprivileged_userns=0` afrouxado na VM.
- Oracle pode recuperar instância ociosa (timer de 2 min reduz, não elimina); custo/limite de uso do plano ChatGPT não medido; relato aberto de `token_invalidated` não reproduzido, mas não descartado.
- Não exercitado: fechamento por merge com aviso de consenso; independência do Auditor depende de o parecer do Revisor não estar no commit auditado.
- Precisão medida só contra defeitos plantados (5/5, sem falso alarme no item limpo) — não contra Spec real.
