---
handoff_id: HO-2026-10-17-18
previous: HO-2026-10-17-17
data: 2026-10-17
branch: ccr-3a0d581c-6cj4ig
base_commit: 89262bd
spec_autorizada: SPEC-006 (abertura homologada, DHR-SPEC006-001; Plan pendente — só por ordem de Andraus) — ROADMAP prevalece
fase: spec-first
autor: Orquestrador
---
# HANDOFF — SOT

> Ponto de entrada de sessão fria (PCC-001). **Dado de estado**, não autoridade: não registra homologação, não fecha decisão aberta (CONS-01), não concede permissão. Em divergência com a realidade, a realidade prevalece.

## 1. Objetivo da frente atual
Reforçar o Revisor SOT (independente, determinístico + adversarial/probabilístico) sem dar Bash a ele. DHR-AUDITOR-EXTERNO-015 (brechas + medição) está na `main` (PR #103). Agora: fundir no Revisor o que era útil dos 2 subagentes antigos e aposentá-los (DHR-AUDITOR-EXTERNO-016).

## 2. Estado
Fase spec-first; BUILD/VERIFY-de-código adiados. Última Spec homologada: SPEC-005; SPEC-006 com abertura homologada e Plan não iniciado. PCC-001 Fases 1 e 2 em vigor na `main` (D-PCC-3/4/5 em aberto).

## 3. Feito nesta sessão
- Entrada §11 reverificada: CI da `main` verde (run #147); `gate_manifest --check` íntegro; check_refs/doc_sync/handoff sem ERRO; PRs abertos = #31 e #2 (inalterados); WORKFLOW v2.1; DHR-AGENTES-001 e DHR-ROTEAMENTO-001 **já mescladas** (PR #106).
- **Guarda do Revisor testada ao vivo (SPEC-005, pré-gate `PASSOU_D`):** G1 ok (abriu ROADMAP/atomic-spec/RULES/RMR-001); **G2 falhou** — `mcp__sot-revisor-gate__revisor_gate` **continua ausente** da lista do Revisor em nuvem e o hook SubagentStop **não forçou retorno** (transcript: 18 usos, encerrou por `SubagentHandback` sem retorno forçado); G3 amostra (plan.md:39, RMR-001:107, ROADMAP:507, WORKFLOW:55, SAS-001:914/917) existe. Reprodução manual do hook sobre o mesmo transcript: `exit 2` com G2 — o script funciona; falta o disparo no harness em nuvem (causa não diagnosticada; hipótese: SubagentStop não roda no encerramento por `SubagentHandback`).
- Parecer do Revisor (observação): CONFORME condicional, 3 Menores (plan.md:39 errata contraditória; checks.md:3 "candidato" defasado; etiquetas [PROPOSTA] no corpo) + 1 Info. Nada corrigido (Spec homologada).
- Telemetria onda 0: linha adicionada (72430 tokens, 18 chamadas).

- **Sondas temporárias (autorizadas por Andraus, revertidas; `settings.json` limpo):** o `SubagentStop` **dispara** em nuvem, inclusive para "Revisor SOT" (`agent_type` exato) e em encerramento por `SubagentHandback`; `last_assistant_message` chega **vazio** nesse caso. Reproduzindo o evento real na guarda: `exit 2` (G1+G2) — mas o Revisor encerrou sem retorno forçado. Conclusão: o `exit 2` **não é honrado** pelo harness em nuvem para subagente que entrega por `SubagentHandback` (ou o script não roda no ambiente do hook — não separado; a 3ª sonda foi bloqueada pelo classificador). Hipótese de matcher refutada.

- **Conserto (ordem de Andraus: "ir direto à ata"):** `governance/DHR-AUDITOR-EXTERNO-018_*` + `scripts/revisor_posguarda.py`/`revisor-posguarda.js` (hook **Stop** do Orquestrador reaplica G1/G2/G3 ao parecer do Revisor, 1 vez por agente) + `tests/test_revisor_posguarda.py` (3 OK; no CI). Testado no transcript real. **Registrado** em `.claude/settings.json` (Stop) e selo regravado (15 arquivos) após autorização de Andraus no chat; vale em sessão NOVA.

- **Guarda pós-Revisor CONFIRMADA AO VIVO (2026-10-17, mesma sessão):** logo após registrar o hook Stop, o primeiro fim de turno foi bloqueado pela `revisor-posguarda.js` listando os 2 Revisores anteriores (G2 no parecer da SPEC-005; G1+G2 na sonda mínima). O `settings.json` recarrega sem reiniciar a sessão. Bloqueio é 1 vez por agente (estado em pasta temporária). Limite: cobre só Revisor→Orquestrador; a ferramenta MCP do gate continua ausente no Revisor em nuvem.

- **Troca do Especificador para `claude-opus-5-5` (ordem expressa de Andraus, "quero trocar agora"; ata `DHR-ROTEAMENTO-002`):** só a linha `model:` de `.claude/agents/especificador.md`; excepciona D5/D6 da DHR-ROTEAMENTO-001, sem teste prévio. Teste A vira **verificação posterior** (só com ordem + limite de cota); reversão a `claude-opus-4-8` por nova ata se houver perda em Crítico/Alto. Revisor inalterado (`claude-sonnet-5-5`). Vale a partir do merge e de sessão nova. Decisões abertas intactas.

## 4. Verificado
Ver §3. Nada de código alterado.

## 5. Próximo passo único
Andraus mescla a ata 002 (troca do Especificador). Depois: Teste A como verificação posterior, só com ordem expressa e limite de cota. Plan da SPEC-006 só por ordem de Andraus.

## 6. Decisões (por ID — NÃO copiar lista; o ROADMAP prevalece)
- DHR-AUDITOR-EXTERNO-015 (na `main`) e -016 (fusão/aposentadoria dos subagentes antigos) — decisões de Andraus em chat, 2026-10-17.
- Decisões abertas/fechadas: ler "Decisões abertas ativas" e "Decisões FECHADAS" do `ROADMAP.md`. Nenhuma alterada.

## 7. Becos sem saída
- Dar Bash ao Revisor: rejeitado (DHR-AUDITOR-EXTERNO-009 §2). Não reabrir sem Andraus.
- Pontuar o banco só com `score.py` em documentos curtos: infla; usar arquivo:linha + texto defeituoso junto da citação (transcrição literal pura subestima).

## 8. Não tocar
- `canon/` BASELINED, specs homologadas, `ROADMAP.md`, `atomic-spec.md`, `.claude/agents/revisor.md`/`especificador.md`, `AGENTS.md` (só por Andraus). Não regravar `GATE-MANIFEST.sha256` sem decisão de Andraus.

## 9. Reverificar ao vivo
- [x] Hook do Revisor ao vivo testado em 2026-10-17: **não disparou** (ver §3); repetir após qualquer correção
- [ ] CI da `main` e do ramo
- [ ] `python scripts/gate_manifest.py --check` e `check_refs.py`/`check_doc_sync.py`
- [ ] PRs abertos (#31 Auditor externo, #2 capturas SPEC-003 na última checagem)
- [ ] `python scripts/backlog_triggers.py`
- [ ] Versão vigente de `WORKFLOW.md` (cabeçalho)
- [ ] `git log -1` == `base_commit` ou posterior; se posterior, ler o diff

## 10. Aguardando Andraus
- Merge das atas DHR-AGENTES-001 e DHR-ROTEAMENTO-001; ordem expressa + limite de cota para a onda 1 (piloto pequeno).
- Merge da DHR-AUDITOR-EXTERNO-016 (PR aberto; só mesclar com ordem de Andraus). Decidiu antes: **manter só o selo**.
- Decidir: schemas sem `additionalProperties:false`, `fibonacci.output.json` sem score e os 8 desalinhamentos produtor×consumidor dos schemas (ata 016 §4).
- Opcional: escrever 3–5 defeitos próprios (parte livre do viés; o novo sorteio automático já foi feito).
- Diagnosticar por que o MCP do Revisor não carrega em nuvem (testar em sessão local).
- Próximos reforços propostos: verificadores D novos (contagens, cobertura, citação §/linha), ferramenta `verifica_citacao`, k=3 passes adversariais em modo cego.
- D-PCC-3/4/5; prioridade: Plan da SPEC-006 · 2 itens de backlog disparados sem registro.

## 11. Ponteiros
`governance/DHR-ROTEAMENTO-001_*` · `governance/DHR-AGENTES-001_*` · `docs/agentes/INDICE-AGENTES.md` · `governance/DHR-AUDITOR-EXTERNO-016_Ata_Fusao_dos_Subagentes_Antigos_no_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-015_Ata_Brechas_de_Ferramenta_e_Medicao_do_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-009_*` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
