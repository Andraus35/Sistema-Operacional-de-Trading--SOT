# DHR-AUDITOR-EXTERNO-001 — Ata — Auditor externo (GPT): piloto controlado, hierarquia e composição do consenso

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-05 |
| Status | **ORDEM DIRETA DE ANDRAUS** (chat, 2026-10-05; respostas às perguntas de instituição do papel, alvo piloto e consenso). Registra as decisões; **não** altera `AGENTS.md`, o Revisor, o ROADMAP nem decisão aberta. |
| Compatibilidade | n/a (ata de registro de piloto; nenhuma BASpec, regra ou decisão aberta alterada) |
| Regime | Piloto controlado. Qualquer normatização definitiva (RULE em `RULES.md`, emenda ao fluxo em `AGENTS.md`) depende de **decisão posterior de Andraus**, após o piloto. |

## 1. Decisões de Andraus `[FATO: respostas em chat, 2026-10-05]`
1. **Instituir o papel de Auditor Externo LLM ("GPT") como PILOTO CONTROLADO.** Sem poder decisório, não é agente interno, não é gate. O fluxo de três posições permanece; o auditor não se interpõe entre elas.
2. **Hierarquia:** o auditor é **subordinado ao Orquestrador interno** e se reporta **somente a ele**; o Orquestrador se reporta a Andraus. O auditor nunca se reporta a Andraus, ao Especificador ou ao Revisor. Instruções e ajustes de postura **só por diretiva versionada** (`governance/propostas/AUDITOR-EXTERNO/DIRETIVAS-AO-AUDITOR.md`), emitida pelo Orquestrador **após consultar Andraus**.
3. **Nuvem:** tudo roda em ambiente em nuvem. O `git pull` do auditor ocorre **apenas** em pedido gerado quando um PR de **homologação final de Spec completa** fica candidato (ou por solicitação do Orquestrador após consulta a Andraus).
4. **Composição do consenso da homologação final:** **Especificador + Revisor + Auditor externo + Andraus.** O **Orquestrador coordena e não é parte do consenso.** O veredito do auditor é **consultivo** (`OK` · `COM_RESSALVAS` · `NAO_OK`) e chega **só ao Orquestrador**, que o relaya.
5. **Alvo piloto:** auditoria de **SPEC-006** (Cognitive Knowledge Graph) no fechamento do ciclo dela.
6. **Canal e credencial:** Issue `[AEX]`; conta dedicada com papel **Read** + token mínimo; o PR do kit é mesclado **como proposta** (workflow inerte até `AUDITOR_EXTERNO_ENABLED=true`).

## 2. Fatos e limites que esta ata registra `[FATO]`
- **SPEC-006 ainda não foi aberta** (ROADMAP: "abertura pendente de autorização de Andraus" e do passo 1-bis do §23). Logo **não há pedido nem auditoria piloto agora**; o piloto só começa no fechamento do ciclo da SPEC-006.
- Sem alvo com resposta conhecida, a **precisão do auditor não é mensurável no piloto**; a calibração disponível hoje é o `selftest.py` do kit (defeitos plantados). Medir contra gabarito (ex.: SPEC-001 v1.2) é opção futura, não decidida.
- "Reportar só ao Orquestrador" é regra de **endereçamento e conduta**, não controle de acesso (o dono do repositório vê todas as Issues).
- Tensão registrada: o auditor integra o consenso mas é **consultivo**. Resolução: o veredito dele é **insumo ao Orquestrador**; só Andraus homologa. O pedido nasce com o PR **aberto** (antes da homologação) para o veredito existir antes do consenso.

## 3. Permanecem ABERTAS (CONS-01)
M-001 (enum) · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.**

## 4. Critérios de avaliação do piloto `[PROPOSTA — Andraus decide]`
Proporção de achados `CONFIRMADO` pelo Revisor; proporção de falsos alarmes e duplicatas; achados sem citação checável (devem ser zero); respeito à linha de reporte (zero contatos diretos); tempo do ciclo. Ao final, Andraus decide: encerrar, estender ou normatizar.

## 5. Registro
- [x] Esta ata · [x] `DIRETIVAS-AO-AUDITOR.md` (DIR-002 VIGENTE; DIR-001 SUPERADA) · [x] kit e workflow em `governance/propostas/AUDITOR-EXTERNO/` e `.github/workflows/auditor-externo.yml` (proposta; workflow inerte) · [ ] ativação (`AUDITOR_EXTERNO_ENABLED`, conta dedicada, token, rótulos) — atos de Andraus.

---

**Andraus** *(ordem direta em chat, 2026-10-05)*
