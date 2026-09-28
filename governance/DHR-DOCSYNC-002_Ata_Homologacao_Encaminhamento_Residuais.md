# DHR-DOCSYNC-002 — Ata de Homologação — Encaminhamento dos Residuais de DHR-DOCSYNC-001

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | DHR-DOCSYNC-001 (residuais RULE-REG-001 e RMR-EST-001) |
| Data | 2026-09-28 |
| Status | **HOMOLOGADA — vigência imediata** |
| Compatibilidade | Minor (correção de dado + correção de escopo de decisão aberta; nenhum modelo canônico redefinido) |

---

## 1. Decisão

**1.1 — RMR-EST-001: FECHADA.** Investigação confirmou que `Diferido` nunca foi um estado formal do enum do `RMR-001` §2 (`Proposto`/`Em espera`/`ATIVADO`/`Absorvido`/`Descartado`) — foi a palavra usada por Andraus na nota de encaminhamento do Passo 11-bis (gate DHR-SPEC019-001, 2026-09-22) para descrever a re-priorização do BL-013 (de "resíduo de L-001" para "aguarda SPEC-018/K-001"). A própria definição de `Em espera` no §2 ("validado; gatilho ainda não disparou") já descrevia exatamente essa situação. Estado do BL-013 corrigido para `Em espera`; toda a narrativa da re-priorização foi preservada no campo, nada foi apagado (INV-07).

**1.2 — RULE-REG-001: permanece ABERTA — escopo corrigido (não é achado isolado).** Auditoria dos textos-fonte de EUA-E13 (`RULE-DEC`) e EUA-E04 (`RULE-HD`) revelou que a "incorporação ao RULES.md" das duas famílias foi **explicitamente diferida ao piloto da SPEC-002 sob atomic-spec v1.5** pelas próprias atas de homologação ("junto com EUA-E04..E12") — e o mesmo padrão se confirma para `RULE-EPI` (EUA-E05), `RULE-SEM` (EUA-E06), `RULE-ONT` (EUA-E07), `RULE-INQ` (EUA-E08), `RULE-CAU` (EUA-E09), `RULE-CTF` (EUA-E10), `RULE-UNC` (EUA-E11), `RULE-PRB` (EUA-E12) e `RULE-MET` (EUA-E14): nenhuma das 9 existe em `RULES.md` hoje, e todas têm o mesmo status epistemológico ("HOMOLOGADA — FATO NORMATIVO... incorporação diferida ao piloto SPEC-002"). Ou seja: **RULE-REG-001 não é um esquecimento de 3 famílias** (como descrito em DHR-DOCSYNC-001) — **é um lote de 11 famílias (10 de EUA-E04–E13 + RULE-MET de EUA-E14) com registro deliberadamente agendado para a abertura da SPEC-002**, ainda não iniciada (falta o Dossiê de Pesquisa, RULE-ECC-01/02).

**Por isso, esta ata NÃO registra as 11 famílias agora.** Registrá-las isoladamente, antes da SPEC-002 abrir, romperia o plano de lote já homologado nas próprias atas de origem — o tipo de adiantamento que o harness pede para evitar (economicidade não justifica pular a sequência já decidida). RULE-REG-001 é reescrita para refletir o escopo correto e recebe **gatilho de ativação** (`spec:SPEC-002 em redação`) nos moldes do RMR-001 §3, para que o registro em lote aconteça no momento certo sem depender de alguém lembrar manualmente.

---

## 2. Efeitos imediatos desta homologação

1. `backlog/RMR-001_Painel_Backlog.md` — BL-013 Estado: `Diferido para SPEC-018` → `Em espera` (re-diferido, narrativa preservada).
2. `ROADMAP.md`, `AGENTS.md` §7, `governance/CATALOGO-OFICIAL.md` §5, `governance/CIC-001` §5.2/§5.3 — RMR-EST-001 movida de aberta para fechada; RULE-REG-001 com descrição corrigida (11 famílias, gatilho `spec:SPEC-002 em redação`) e permanece aberta.
3. `governance/CATALOGO-OFICIAL.md` §7.3 — nova linha de ata (abaixo).

---

## 3. Registro do Controlador (efeitos aplicados — 2026-09-28)

- [x] `backlog/RMR-001_Painel_Backlog.md` — BL-013 Estado corrigido.
- [x] `ROADMAP.md` — RMR-EST-001 movida para "Decisões FECHADAS"; RULE-REG-001 reescrita em "Decisões abertas ativas" (escopo de 11 famílias + gatilho).
- [x] `AGENTS.md` §7 — mesma correção.
- [x] `governance/CATALOGO-OFICIAL.md` §5 — RMR-EST-001 riscada/fechada; RULE-REG-001 reescrita.
- [x] `governance/CIC-001_Inventario_Conformidade.md` §5.2/§5.3/§8/§9 — RMR-EST-001 movida; RULE-REG-001 reescrita; contagens atualizadas.
- [x] `governance/DHR-DOCSYNC-001_...md` — não reescrito (INV-07); esta ata é aditiva/corretiva sobre ele.

**Pendência (objeto do gatilho `spec:SPEC-002 em redação`):** registrar em lote, na abertura da SPEC-002, as 11 famílias de RULE-REG-001 (`RULE-HD`, `RULE-EPI`, `RULE-SEM`, `RULE-ONT`, `RULE-INQ`, `RULE-CAU`, `RULE-CTF`, `RULE-UNC`, `RULE-PRB`, `RULE-DEC`, `RULE-MET`) em `governance/RULES.md`, usando os blocos de texto já homologados em EUA-E04 a EUA-E14 (nenhuma autoria nova necessária — é transcrição, como já ocorreu com RULE-EV em DHR-DOCSYNC-001).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
