# Parecer do Revisor SOT — R3 (delta) — errata aditiva ao Plan v1.2 da SPEC-008 (4 condições)

> **Transcrição pelo Orquestrador** do relatório do Revisor (somente leitura; subagente `aafa175283e3c7fac`, 2026-11-27), preservando veredicto, achados e os blocos `ACHADOS-ESTRUTURADOS` e `FICHA-M`. Não é homologação.

- **Modo:** delta · **SHA256-ALVO:** `61bb8c6764f60b0e5c0544d50b53f0c300779585d1a66819ec3ead0b12e796b7` (commit `1e20263`; base `6f77b87`) · CRITICAL D0–D8 · **TOKENS:** não medidos. Gate: não se aplica (errata); `check_refs` ERRO=0 é dado do Orquestrador, não verificado pelo Revisor.
- **Veredicto: CONFORME** — 3 Menores, nenhum bloqueante. Vai à homologação de Andraus. Nenhum bloqueador novo; J-001 e as demais abertas não são tocadas.
- **R2-M1 resolvido:** Grep de `MDC_CYCLE_OPENED`, `AGUARDANDO`, `F01`, `F37`, `3.1-bis`: nenhuma afirmação da ordem antiga fora de `[antes]`; §3.1-bis = "sem alteração"; ADV-12 (d) exige só o que D4.1 SAÍDA/D4.2 (7)–(8)/D5 vigentes produzem (recusa gravada; `dispatch_request(ESTRUTURAL)` = 0; `STAGE_TIMER` = 0; zero PUBLISH_OWN/TIME_REQUEST EXECUTED no `capability_audit_record`; `notice` = 0) e declara `fsm_row`, `from_state`, abertura e `cycle_closed` como NÃO verificados.
- **Lacuna residual §3.0-bis:** fiel ao Plan (L1: F01 não aplicada ⇒ F29; L2: abertura gravada ⇒ F37 de AGUARDANDO); nenhuma decisão aberta fechada; `[DECISÃO NECESSÁRIA]` sem ID novo.
- **R2-m01/R2-m02 resolvidos** (§2.3, §1, §6 Minor mantido, §8, §10 consistentes). E-1..E-5 coerentes. RULE-SEM-03 preservada. Passos 2–8 PASS; adversarial ADV-12 (d): detectável pelo `capability_audit_record`; gap de observabilidade do estado de origem já declarado.
- **Risco residual:** sem Bash, hashes das fontes e `check_refs` não verificados pelo Revisor; auditoria semântica sobre o texto lido.

## Achados (Menores)
- **R3-m01 [C08] (classe O):** a frase "a construção não pode adotar a leitura híbrida" (§3.0-bis) soa como obrigação normativa sem âncora de regra, e não aparece em §8/§6. Reformular como risco derivado de INV-MDC-01 (a leitura híbrida deixaria a chave `asset`+`mission_id` ocupada, em contradição com o encerramento sem efeito), ou declarar a restrição nomeada no §1 e §6. Não bloqueia.
- **R3-m02 [C07] (M):** ADV-12 (d) cita "D4.1 SAÍDA" para "recusa gravada no livro"; a fonte é INV-MDC-01 (plan l.349–350).
- **R3-m03 [C02]:** a linha "Rodada" do cabeçalho cita §1/§10 para R2-m02, mas §6/§8 também foram tocados. Editorial, sem ação obrigatória.

<!-- ACHADOS-ESTRUTURADOS
R3-m01|MENOR|C08|proibição "leitura híbrida" apresentada sem âncora de regra nem declaração em §1/§6/§8|toda restrição à construção deve ser nomeada como exceção/regra ou apresentada como risco derivado de uma regra citada
R3-m02|MENOR|C07|ADV-12 (d) cita D4.1 SAÍDA para "recusa gravada no livro", mas a fonte é INV-MDC-01|conferir a âncora de cada obrigação da VERIFICAÇÃO contra o texto exato da fonte
R3-m03|MENOR|C06|linha Rodada do cabeçalho lista §1/§10 para R2-m02, mas §6/§8 também foram tocados|listar todas as seções tocadas por cada achado corrigido
-->

<!-- FICHA-M {"achados":[{"id":"R3-m02","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-PLAN-SPEC008-4-CONDICOES-PROPOSTA-2026-11-27.md","antigo":"(d) recusa gravada no livro (D4.1 SAÍDA;","novo":"(d) recusa gravada no livro (INV-MDC-01;","condicao":"a recusa gravada é de INV-MDC-01 (plan l.349-350), não da D4.1 SAÍDA"}]} -->
