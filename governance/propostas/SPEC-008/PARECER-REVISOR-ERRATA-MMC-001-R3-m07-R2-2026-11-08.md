# Parecer do Revisor — Proposta de errata R3-m07 ao MMC-001 — R2 — 2026-11-08

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura; classe S3, âncora `ABERTURA.md`). **CONFORME condicional** (0 Crítica/Média; 1 Menor classe O não bloqueante). Guarda G1 feita pelo próprio Revisor (abriu o painel de backlog).

RELATÓRIO DE REVISÃO: Proposta de errata R3-m07 ao MMC-001 v1.0, rodada R2. Data: 2026-11-08. Autor: Revisor de Especificação SOT, somente leitura.

SHA256-ALVO: não recebido · MODO: delta sobre o parecer R1. Mais o núcleo integral (cabeçalho, §3, §6, §7, pendências) e uma amostra de blocos que não mudaram.

Arquivos:
- Proposta: /home/user/Sistema-Operacional-de-Trading--SOT/governance/propostas/SPEC-008/ERRATA-MMC-001-R3-m07-PROPOSTA-2026-11-08.md
- Baseline: /home/user/Sistema-Operacional-de-Trading--SOT/governance/MMC-001_Manager_Contract.md
- Âncora: /home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/ABERTURA.md
- Parecer anterior: /home/user/Sistema-Operacional-de-Trading--SOT/governance/propostas/SPEC-008/PARECER-REVISOR-ERRATA-MMC-001-R3-m07-R1-2026-11-08.md

**Veredito: CONFORME condicional.** Não há achado Crítico nem Médio, e os 5 achados do R1 estão resolvidos. Há 1 Menor novo, de classe O e não bloqueante. O veredito é condicional por dois motivos:
- O gate não foi verificado (a peça não é plan.md, e o pedido não trouxe revisor_gate nem GATE-D).
- A proposta só fica completa quando Andraus decidir E-1 (Patch, Minor ou Major) e E-2 (forma de aplicação).

## 1. Objeto
- **Artefato:** errata aditiva ao MMC-001 v1.0, que é baseline (DHR-SPEC008-002).
- **Complexidade:** a âncora é CRITICAL (ABERTURA l.22).
- **Origem:** a condição da DHR-SPEC008-002 §4 (l.40-42).

## 2. Gate e limites
- **GATE NÃO VERIFICADO:** a peça não é plan.md e não houve ferramenta nem GATE-D. Por isso o teto do parecer é CONFORME condicional.
- **Sem Bash e sem git:** não rodei check_refs nem build_map. Os trechos foram comparados por leitura da árvore de trabalho, não por diff.
- **Não verificados:** o chat de Andraus de 2026-11-08 e o hash do MMC-001 no momento da aplicação. O Orquestrador precisa conferir que as linhas 3, 72, 169 e 230 ainda têm o texto citado.

## 3. Conferência dos achados do R1 (fonte aberta nesta sessão)

**ER1-M01: RESOLVIDO.**
- O §3 traz as três hipóteses, Patch, Minor e Major.
- As definições transcritas batem literalmente com a CR-001 l.439-441. Também conferem os trechos citados da CRR52 (l.447), da CE2 (l.443), da CRR54 (l.449) e da CRR56 (l.451).
- O marcador "v1.0.1" foi retirado. Ele só aparece como contexto no §3.4 e na linha E-1, e no `[antes]` da redação R1.
- Minor está declarado como fora da definição literal. Major está analisado com o precedente DHR-SPEC006-005 l.10, que conferi: "Major".
- A leitura pelo MMC §1 l.23, que sustentaria Patch, aparece com os riscos dela declarados.
- O Especificador não recomenda nenhuma das três. A resposta anterior "Patch v1.0.1" ficou pendente de reconfirmação e não foi registrada como decisão. Ninguém decidiu no lugar de Andraus.
- Citações conferidas: DHR-SPEC008-002 l.10 ("Minor"), l.41 e l.42; RULES l.382-384.

**ER1-m02: RESOLVIDO.**
- O §2.3 cita como "antigo" a linha 230 do MMC literalmente, com o mesmo recuo de 13 espaços.
- O texto novo alinha a Classe D/C com a nova linha de orientação do §8.2-bis ("sem alcance vertical") e mantém o "orçamento do ciclo" da P-7 só para SPEC-008/Spec de Tempo.
- O `[antes]` fica dentro do bloco de código. O texto continua recuperável (INV-07); a escolha está declarada na l.81 da proposta.
- O §4 da proposta foi atualizado, com o `[antes]` da leitura antiga.

**ER1-m03: RESOLVIDO.**
- O alvo 4 é o trecho "condição R3-m07 na ata §3" do MMC l.3, que existe literalmente. A correção para §4 confere com a DHR-SPEC008-002 §4 (l.40-42); o §3 da ata é "O que esta ata NÃO afirma".
- O §6 da proposta (l.193) não sugere mais FICHA-M sobre o baseline e cita a INV-09, com `[antes]`.

**ER1-m04: RESOLVIDO.**
- O campo "Forma" (l.12) declara a divergência em relação à DHR-SPEC006-005. Conferi a citação da l.10 ("não altera texto baselined do plan.md/checks.md") e a da D2, l.19.
- A linha E-2 do §7 oferece as opções (A), no próprio lugar, e (B), arquivo à parte com ponteiro. A escolha fica com Andraus `[DECISÃO NECESSÁRIA]`.

**ER1-m01 (FICHA-M do R1): MANTIDO.** O texto novo da FICHA está na l.50 da proposta, sem alteração.

## 4. A rodada não introduziu defeito novo

**Trechos "antigo" literais:**
- §2.1 = MMC l.72; §2.2 = l.169; §2.3 = l.230; §2.4 é um trecho da l.3. Todos conferem.
- ABERTURA l.25, l.140 e l.144 conferem.
- DHR-EUA-E23 l.32 confere ("orientação não-vinculante").
- RULES l.689 confere (RULE-SEM-03).

**Aditiva (INV-07):**
- Todo texto substituído fica em `[antes]`.
- As reticências nos `[antes]` só omitem partes que não mudaram, o mesmo padrão que o MMC já usa na l.179.

**Nada novo criado:**
- Nenhuma regra, campo, estado, transição, ID normativo ou agente de trading novo.
- "Obrigação" e "Orientação" já são rótulos do contrato (l.43, l.56, l.63, l.168).
- A linha nova do §8.2-bis só desdobra a linha existente.

**Parte firme preservada:** "nenhuma H/P ⇒ volta a Andraus" continua com o mesmo alcance (SPEC-008/Spec de Tempo; para SPEC-014/015, só o limite do ADR §2.5).

**Sem resíduo de D/C como obrigação no MMC:** o Grep de "D/C", "3.1.3" e "trava constitutiva" acha só as linhas 59, 72, 169, 179 e 230, mais as tabelas de histórico §13/§14 (l.318, 327, 344), que são registro e não se editam.

**Análise de impacto:** o Grep de MMC-001/MANAGER-CONTRACT em tests/, scripts/ e schemas/ não acha nada, o que confirma "nenhum teste". "Plan pendente" confere com ROADMAP l.524.

**CONS-01:** a lista do §5 da proposta coincide com a DHR-SPEC008-002 §5 (l.45). Nenhuma decisão aberta foi fechada.

## 5. Guarda G1 (backlog/RMR-001): confirmada
- Abri /home/user/Sistema-Operacional-de-Trading--SOT/backlog/RMR-001_Painel_Backlog.md.
- A proposta não cita BL nem RMR (Grep: 0 ocorrências).
- O painel não cita MMC-001, R3-m07 nem DHR-SPEC008-002 (Grep: 0).
- Os itens ligados à SPEC-008 (BL-026 na l.133, BL-043..046 nas l.150-153) estão todos `Em espera`. Eles pertencem ao Plan da SPEC-008, não à errata.
- Não há ATIVADO pendente relacionado à errata. Os itens ATIVADO históricos (BL-008, BL-012, BL-019) não têm relação com ela.

## 6. Passos e disciplinas
- Os Passos 2 e 3 (invariantes e Constitution Check) passam: nenhum invariante é tocado e não há cruzamento SOT→execução (DEC).
- **SEM:** a modalidade é preservada, que é o objetivo da errata.
- **EPI:** as etiquetas estão corretas. As hipóteses do §3 estão marcadas `[INFERÊNCIA]`; a parte firme cita o parecer como não homologado.
- **CAU, ONT, INQ, CTF, UNC, PRB e MET:** verificadas, sem achados.

## 7. Achado

**ER2-m01 — Menor, classe O, não bloqueante (C04, rastreabilidade):**
- **Constatação:** na forma (A), aplicação no próprio lugar, o cabeçalho do MMC (l.3) continua citando só a DHR-SPEC008-002. Em Patch, a versão não muda (§3.1). Quem ler o baseline não encontra a ata que homologar a errata, só as marcas `[antes … R3-m07]` espalhadas no texto.
- **Por que a forma (B) não tem o problema:** ela já prevê o ponteiro no cabeçalho.
- **Sugestão:** na linha E-2 (A), ou no §6, prever um ponteiro de uma linha para a ata da errata no cabeçalho (l.3), com `[antes]`, independentemente da forma escolhida.

**Observação, sem achado:** a nova etiqueta da 3.1.3 cita a DHR-SPEC008-002 §4, que não está no INHERITS do §8.3. Isso é aceitável, porque é a ata de homologação do próprio contrato, citada como âncora e não como herança.

## 8. Cobertura (por bloco)

| Bloco | Situação |
|---|---|
| Cabeçalho l.11-12 | Conferido agora |
| §1 l.27-33 | Conferido agora |
| §2.1 | Amostra |
| §2.2 | Amostra |
| §2.3 | Conferido agora |
| §2.4 | Conferido agora |
| §3 inteiro | Conferido agora |
| §4 (tabela) | Amostra |
| §4 l.171 | Conferido agora |
| §5 | Conferido agora |
| §6 | Conferido agora |
| §7 | Conferido agora |

A amostra de blocos que não mudaram cobre: §2.1 e §2.2 (os trechos "antigo"), a citação da ABERTURA no §1, a tabela do §4, a lista CONS-01 do §5 e DHR-EUA-E23 l.32. Nenhum achado nela.

## 9. Encaminhamento
- **Andraus:** decidir E-1 (Patch v1.0, Minor v1.1 ou Major v2.0) e E-2 (forma A ou B). Só depois disso vem a homologação, por ata própria.
- **Especificador:** ER2-m01, se Andraus quiser; o achado não bloqueia.
- **Orquestrador, na aplicação:** conferir que as linhas 3, 72, 169 e 230 do MMC ainda têm o texto citado. Nada foi aplicado ao baseline.

<!-- ACHADOS-ESTRUTURADOS
ER2-m01|MENOR|C04|Na forma (A) em Patch, cabecalho do MMC (l.3) nao aponta a ata que homologar a errata; so marcas [antes] dispersas localizam a mudanca|Toda errata aplicada in loco a baseline acrescenta ponteiro de uma linha a ata homologadora no cabecalho
-->

<!-- FICHA-M {"achados":[]} -->

Os achados ER1-M01 e ER1-m02..m04 foram resolvidos nesta rodada. Não há Menor mecânico, por isso a FICHA-M está vazia.
