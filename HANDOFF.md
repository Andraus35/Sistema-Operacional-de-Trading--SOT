---
handoff_id: HO-2026-10-17-25
previous: HO-2026-10-17-24
data: 2026-10-17
branch: ccr-7917ac44-2l55cz
base_commit: db32790
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
- **Revisão independente de outro modelo (critério L3) na SPEC-006 v1.3 (Plan candidato no ramo `spec006-plan`, fora da main):** 2 modelos externos **sem repositório** → 10 achados: 2 falsos, 4 lacunas já declaradas pelo autor, 4 reais (todos já no Revisor interno); **0 defeito real exclusivo de externo**; Revisor interno achou ≥9 que nenhum externo viu. Registro em `governance/AVALIACAO-MECANISMOS-REVISOR-2026-10-17.md` §7 e §7.1. Conclusão: independência sem leitura do repositório rende pouco.
- **Próxima rodada (Andraus faz no VS Code com Copilot COM acesso ao repo em nuvem):** prompt pronto em `revisao-independente/PEDIDO-COPILOT-COM-REPO.txt` (autoriza leitura, indica o ramo/caminho do Plan, proíbe abrir pastas do Revisor para preservar independência). Andraus cola o JSON de volta aqui; conferir cada achado contra o texto real e comparar com o Revisor interno (2 rodadas já feitas; achados A-01..A-10 / F-01..F-14, 1 crítico: herança "preservar todos os estados" × admissão INDETERMINADA × CEM-001:494).
- **Decisões de Andraus (4 AskUserQuestion, ata `DHR-COESAO-001`):** (1) mesclar #111 após CI verde; (2) COE-01/02/04/05 viram bloqueantes no CI — feito, com `roadmap.md`→`ROADMAP.md` nos dois agentes (autorizado); (3) registro de mecanismos `governance/MECANISMOS.json`+schema como **PROPOSTA** com detector COE-14 (AGENTS não alterado); (4) proteger a `main` exigindo CI + dono — **configuração só de Andraus** (risco: autor=dono bloqueia o próprio merge sem bypass, ata §3); CODEOWNERS +7 linhas feito; selo **não** regravado.
- **Auditoria de coesão (a pedido de Andraus):** suíte verde (226 py + 4 hook-js + schemas + lint). 6 achados de duas verdades, 6 de ociosidade; corrigido o operacional (HANDOFF, README, CI com os testes que faltavam, ata DHR-ASK-002 PROPOSTA) + **detector `scripts/check_coesao.py` (COE-01..13, 17 testes, CI informativo)** e estudo `governance/ESTUDO-GARANTIAS-DETERMINISTICAS-2026-10-17.md` (hooks×CI×pre-commit×selo×schema×policy; 8 propostas que dependem de Andraus, ex.: registro de mecanismos como dado e promover COE-01/02/04/05 a bloqueantes); nada em AGENTS/agentes/CODEOWNERS/canon/ROADMAP. Copilot: **mantido pendente** por Andraus.
- **Copilot COM repo (§7.2 da avaliação) recebido e conferido:** NAO_CONFORME, 4 achados, 0 falsos, citações todas corretas. A-01 (D6.5 incondicional × CKG-005/T12) e A-02 (CKG-010(a) INDETERMINADO × cobertura "13 BASpecs verificáveis", plan.md:1310-1311 + EC-CKG-001) procedem e já estavam no Revisor (A-02 com ângulo novo na 1310-1311); A-03 (`collision_record`/`canonical_state_transition_record` sem version/supersedes/proveniência) procede, A-04 (bounded loop sem valor) procede em parte — ambos **não classificáveis** sem o texto integral dos achados do Revisor (não versionado). Severidade inflada; recall baixo; 0 exclusivo de externo. Andraus: **avançar com o que há** (sem rodada 2). Prompt da rodada 2 foi entregue no chat (não versionado).
- Entrada §11 reverificada: CI da `main` verde (run #147); `gate_manifest --check` íntegro; check_refs/doc_sync/handoff sem ERRO; PRs abertos = #31 e #2 (inalterados); WORKFLOW v2.1; DHR-AGENTES-001 e DHR-ROTEAMENTO-001 **já mescladas** (PR #106).
- **Guarda do Revisor testada ao vivo (SPEC-005, pré-gate `PASSOU_D`):** G1 ok (abriu ROADMAP/atomic-spec/RULES/RMR-001); **G2 falhou** — `mcp__sot-revisor-gate__revisor_gate` **continua ausente** da lista do Revisor em nuvem e o hook SubagentStop **não forçou retorno** (transcript: 18 usos, encerrou por `SubagentHandback` sem retorno forçado); G3 amostra (plan.md:39, RMR-001:107, ROADMAP:507, WORKFLOW:55, SAS-001:914/917) existe. Reprodução manual do hook sobre o mesmo transcript: `exit 2` com G2 — o script funciona; falta o disparo no harness em nuvem (causa não diagnosticada; hipótese: SubagentStop não roda no encerramento por `SubagentHandback`).
- Parecer do Revisor (observação): CONFORME condicional, 3 Menores (plan.md:39 errata contraditória; checks.md:3 "candidato" defasado; etiquetas [PROPOSTA] no corpo) + 1 Info. Nada corrigido (Spec homologada).
- Telemetria onda 0: linha adicionada (72430 tokens, 18 chamadas).

- **Sondas temporárias (autorizadas por Andraus, revertidas; `settings.json` limpo):** o `SubagentStop` **dispara** em nuvem, inclusive para "Revisor SOT" (`agent_type` exato) e em encerramento por `SubagentHandback`; `last_assistant_message` chega **vazio** nesse caso. Reproduzindo o evento real na guarda: `exit 2` (G1+G2) — mas o Revisor encerrou sem retorno forçado. Conclusão: o `exit 2` **não é honrado** pelo harness em nuvem para subagente que entrega por `SubagentHandback` (ou o script não roda no ambiente do hook — não separado; a 3ª sonda foi bloqueada pelo classificador). Hipótese de matcher refutada.

- **Conserto (ordem de Andraus: "ir direto à ata"):** `governance/DHR-AUDITOR-EXTERNO-018_*` + `scripts/revisor_posguarda.py`/`revisor-posguarda.js` (hook **Stop** do Orquestrador reaplica G1/G2/G3 ao parecer do Revisor, 1 vez por agente) + `tests/test_revisor_posguarda.py` (3 OK; no CI). Testado no transcript real. **Registrado** em `.claude/settings.json` (Stop) e selo regravado (15 arquivos) após autorização de Andraus no chat; vale em sessão NOVA.

- **Guarda pós-Revisor CONFIRMADA AO VIVO (2026-10-17, mesma sessão):** logo após registrar o hook Stop, o primeiro fim de turno foi bloqueado pela `revisor-posguarda.js` listando os 2 Revisores anteriores (G2 no parecer da SPEC-005; G1+G2 na sonda mínima). O `settings.json` recarrega sem reiniciar a sessão. Bloqueio é 1 vez por agente (estado em pasta temporária). Limite: cobre só Revisor→Orquestrador; a ferramenta MCP do gate continua ausente no Revisor em nuvem.

- **Troca do Especificador para `claude-opus-5-5` (ordem expressa de Andraus, "quero trocar agora"; ata `DHR-ROTEAMENTO-002`):** só a linha `model:` de `.claude/agents/especificador.md`; excepciona D5/D6 da DHR-ROTEAMENTO-001, sem teste prévio. Teste A vira **verificação posterior** (só com ordem + limite de cota); reversão a `claude-opus-4-8` por nova ata se houver perda em Crítico/Alto. Revisor inalterado (`claude-sonnet-5-5`). Vale a partir do merge e de sessão nova. Decisões abertas intactas.

- **Roteador determinístico de modelos (Andraus: "vamos a isso"; ata `DHR-ROTEAMENTO-003`):** `scripts/roteador_modelos.py` + `roteador-modelos.js` (hook PreToolUse/Agent) + 6 testes (CI). Nega `model`/`effort` por invocação em Especificador/Revisor, Haiku em gate/soberano, modelo fora da tabela. **Registrado** em `.claude/settings.json` e selo regravado (17 arquivos) após autorização de Andraus; **confirmado ao vivo** (Revisor + `model=haiku` negado pelo hook). Limite: classificação por palavra-chave (forma, não mérito).

## 4. Verificado
Ver §3. Nada de código alterado.

## 5. Próximo passo único
Andraus: (a) configurar a proteção da `main` (Settings → Branches; ata DHR-COESAO-001 §3), (b) assinar o registro de mecanismos como VIGENTE quando quiser que o AGENTS.md aponte para ele. Andraus decide sobre o PR da auditoria de coesão (`governance/AUDITORIA-COESAO-MECANISMOS-2026-10-17.md`): ratificar a ata `DHR-ASK-002` e decidir D1/D5/D6/O1/O3/O4/O5 (só dele). Depois: Teste A como verificação posterior só com ordem + limite de cota. Plan da SPEC-006 só por ordem de Andraus.

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
- **Auditoria de coesão (HO-24):** relatório em `governance/AUDITORIA-COESAO-MECANISMOS-2026-10-17.md`; ata `DHR-ASK-002` é PROPOSTA (regra de fim de turno já em hook, sem ata). Decisões só de Andraus: status do Auditor Externo (D1), AGENTS §3/§8 (D6), `roadmap.md` nos agentes (D5), camadas inertes do Revisor em nuvem (O1), CODEOWNERS 10/17 (O3), skills soltas (O4), triplo gate (O5).
- Decidir (Andraus) o destino do resultado do Copilot: reativar o Auditor Externo, rodar a rodada 2 (prompt no chat da sessão HO-22), ou escrever 3–5 defeitos próprios. Colar a lista completa A-01..A-10/F-01..F-14 do Revisor para classificar A-03/A-04.
- Ordem expressa + limite de cota para a onda 1 do roteamento (piloto pequeno). (As atas DHR-AGENTES-001/ROTEAMENTO-001/002/003 já estão mescladas: PR #106, #108, #109.)
- DHR-AUDITOR-EXTERNO-016 já mesclada (PR #104). Decisão anterior: **manter só o selo** (sem exigir review de dono na `main`).
- Decidir: schemas sem `additionalProperties:false`, `fibonacci.output.json` sem score e os 8 desalinhamentos produtor×consumidor dos schemas (ata 016 §4).
- Opcional: escrever 3–5 defeitos próprios (parte livre do viés; o novo sorteio automático já foi feito).
- Diagnosticar por que o MCP do Revisor não carrega em nuvem (testar em sessão local).
- Próximos reforços propostos: verificadores D novos (contagens, cobertura, citação §/linha), ferramenta `verifica_citacao`, k=3 passes adversariais em modo cego.
- D-PCC-3/4/5; prioridade: Plan da SPEC-006 · 2 itens de backlog disparados sem registro.

## 11. Ponteiros
`governance/DHR-ROTEAMENTO-001_*` · `governance/DHR-AGENTES-001_*` · `docs/agentes/INDICE-AGENTES.md` · `governance/DHR-AUDITOR-EXTERNO-016_Ata_Fusao_dos_Subagentes_Antigos_no_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-015_Ata_Brechas_de_Ferramenta_e_Medicao_do_Revisor.md` · `governance/DHR-AUDITOR-EXTERNO-009_*` · `AGENTS.md` §11 · `ROADMAP.md` · `backlog/RMR-001_Painel_Backlog.md` · `docs/mapa/MAPA-PROJETO.md`
