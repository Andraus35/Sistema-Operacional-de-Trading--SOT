# Parecer do Revisor — Proposta de errata R3-m07 ao MMC-001 — R1 — 2026-11-08

> Transcrição pelo Orquestrador do retorno do Revisor SOT (somente leitura; classe S3, âncora de complexidade `ABERTURA.md`). Objeto: `ERRATA-MMC-001-R3-m07-PROPOSTA-2026-11-08.md`. **NÃO CONFORME (1 Média).** Nada foi aplicado ao baseline.

RELATÓRIO DE REVISÃO: Proposta de errata R3-m07 ao MMC-001 v1.0. Data: 2026-11-08. Autor: Revisor de Especificação SOT.

SHA256-ALVO: não recebido · MODO: integral (1ª rodada da errata)
Arquivos: proposta revisada em /home/user/Sistema-Operacional-de-Trading--SOT/governance/propostas/SPEC-008/ERRATA-MMC-001-R3-m07-PROPOSTA-2026-11-08.md · baseline em /home/user/Sistema-Operacional-de-Trading--SOT/governance/MMC-001_Manager_Contract.md · âncora em /home/user/Sistema-Operacional-de-Trading--SOT/specs/features/SPEC-008/ABERTURA.md

**Veredito: NÃO CONFORME. Há 1 achado Médio. Ele é recuperável, não toca o texto proposto para o contrato e está só na análise de compatibilidade.**

## 1. Objeto e classificação
- **Artefato:** proposta de errata aditiva ao MMC-001 v1.0, que é baseline (DHR-SPEC008-002).
- **Complexidade:** a âncora é CRITICAL (ABERTURA.md l.22).
- **Escopo:** só a errata, não o contrato inteiro.
- **Posição:** condição da homologação, DHR-SPEC008-002 §4 (l.40-42).

## 2. Gate determinístico e limites
- **GATE NÃO VERIFICADO.** O artefato não é plan.md, a ferramenta revisor_gate não está disponível e o pedido não trouxe linha GATE-D. Por isso o teto do parecer seria, de qualquer forma, CONFORME condicional.
- **Limites:** não tenho Bash nem git. Não executei check_refs nem build_map. O texto foi comparado por leitura direta da árvore de trabalho, não por diff. Não verifiquei o chat de Andraus de 2026-11-08.

## 3. Conferência de cada ponto pedido (M1: afirmação, fonte aberta, resultado)

**(1) Os trechos "texto antigo" batem com as fontes: CONFERE.**
- §2.1 da proposta (l.41) é idêntico a MMC-001 l.72, caractere a caractere, incluindo os dois `[antes]`.
- §2.2 (l.60) é idêntico a MMC-001 l.169.
- ABERTURA l.25, l.140 e l.144 citadas na proposta (l.20-22) conferem literalmente.
- A observação de que a l.25 fica no §1 e não no §3/§4 está correta (ABERTURA l.16-25). Ela corrige a citação do parecer R3 e da própria ata.
- O bloco `[antes]` da l.179 do MMC fica intacto. A proposta só acrescenta um bloco novo abaixo dele.

**(2) A modalidade é preservada (RULE-SEM-03, RULES.md l.689): CONFERE.**
- A parte firme ("nenhuma BASpec H/P…; volta a Andraus") continua rotulada como Obrigação, com o mesmo alcance vertical. A linha dividida do §8.2-bis repete, na coluna de alcance, o texto exato da l.169: SPEC-008 + Spec de Tempo; para SPEC-014/015, só o limite do ADR §2.5.
- D/C passa a ser orientação, alinhada a ABERTURA l.25 e à DHR-EUA-E23 l.32. Essa citação confere literalmente.
- A firmeza vem da DHR-SPEC008-002 §4, l.41 ("só 'nenhuma H/P ⇒ volta a Andraus' é firme"). Confere.
- A afirmação de que §3.1.1/§3.1.4 e §5.1–5.5/§6.4/§7 alcançam todas as filhas confere com MMC l.167.

**(3) Caráter aditivo (INV-07) e nada criado: CONFERE, com uma ressalva de forma (ER1-m04).**
- O texto substituído fica preservado em `[antes]`.
- Não cria regra, campo, estado, transição, ID normativo nem agente de trading. A linha nova do §8.2-bis é um desdobramento de leitura. Os rótulos "Obrigação" e "Orientação" já são usados no contrato (l.56, l.63, l.68, l.168).
- A frase "a Classe de cada BASpec é declarada no Plan (RULE-MECH-01)" repete o que a v1.0 já dizia na coluna de etiqueta da l.72.

**(4) Nenhuma outra seção alterada e nenhuma decisão aberta fechada (CONS-01): CONFERE.**
- A lista do §5 da proposta (l.112) coincide com a DHR-SPEC008-002 §5 (l.45).
- A afirmação "Plan pendente" confere com ROADMAP l.524.

**(5) Classificação Patch × Minor e análise RULE-HG-04: NÃO CONFERE (ER1-M01, abaixo).**
- A Análise de Impacto está presente (schemas, RAG, Skills, testes, modelos), como exige RULES.md l.382-384.

**(6) §8.3 l.230 e a coluna "não herdável" do §3:**
- A coluna do §3 fica sem contradição: a l.56 e a l.168 ganham o mesmo regime da l.59.
- A l.230 fica com resíduo (ER1-m02). Ela está em ADDED (c), "leituras de alcance do §8.2-bis", e continua dizendo que D/C vale "só para SPEC-008/Tempo". Depois da errata, a tabela que essa linha resume diz alcance "nenhuma". A frase pode ser lida como restrição verdadeira, como argumenta a proposta, mas o bloco Herança/Delta passa a listar como acréscimo de alcance algo que deixou de ter alcance.

**(7) Erro "condição R3-m07 na ata §3": CONFIRMADO.**
- MMC-001 l.3 cita "ata §3", mas a condição está na DHR-SPEC008-002 §4 (l.40-42). O §3 da ata é "O que esta ata NÃO afirma".
- Como o MMC-001 já é baseline, a correção não pode ser feita por FICHA-M direto no contrato: o próprio l.3 diz "mudança só por errata homologada" (INV-09). A sugestão da proposta (§6, l.122) de tratá-la como "FICHA-M do Orquestrador" sobre o baseline contraria isso (ER1-m03).

## 4. Achados

**ER1-M01 — Média — proposta §3 (l.78-85)**
- **Constatação:** a classificação diverge da taxonomia canônica que a RULE-HG-04 manda aplicar. Pela CR-001 (canon/CR-001-compliance-record.md):
  - Patch = "Correções exclusivamente editoriais … notas sem efeito normativo", com efeito "Não altera a versão" (l.439).
  - Minor = "adicionam comportamento sem invalidar" (l.440).
  - Major = "removem, invalidam ou alteram comportamento normativo vigente" (l.441).
- **Contradições na proposta:**
  - Ela declara "O único efeito material é deixar de exigir como obrigação" (l.82), um efeito normativo, e mesmo assim recomenda Patch.
  - Propõe o marcador "v1.0.1", que a CR-001 não prevê para Patch.
  - Não analisa a hipótese Major, embora o precedente que ela mesma cita, DHR-SPEC006-005 l.10, tenha classificado uma errata com efeito normativo como Major.
  - Minor também não se encaixa na definição canônica, porque a errata relaxa uma obrigação em vez de acrescentar comportamento.
- **Linha de defesa possível, que a proposta não usou:** a regra de leitura do MMC §1 (l.23: "Se algum item daqui divergir do texto-fonte citado, vale o texto-fonte e a divergência é achado a corrigir aqui"). Por ela, a obrigação D/C nunca teria prevalecido sobre a fonte, e a errata seria uma correção de transcrição. Isso sustentaria Patch, sem mudança de versão.
- **Ação:**
  - Reescrever o §3 com as três hipóteses (Patch, Minor, Major) contra as definições literais da CR-001 l.437-441.
  - Retirar "v1.0.1" ou justificá-lo contra a CR-001 l.439.
  - Apresentar a leitura pelo §1 do MMC, se for a base do Patch.
  - Manter a escolha com Andraus.
- **Condição para nova revisão:** o §3 cita a CR-001 l.437-441 e trata das três classes.

**ER1-m01 — Menor, mecânico (FICHA-M)**
- Na nova célula da 3.1.3 (l.47 da proposta), o trecho "parte firme = `[FATO]` DHR-SPEC008-002 §4 e parecer R3 l.19" etiqueta um parecer como `[FATO]`.
- Pela definição de etiqueta do próprio MMC (l.14), `[FATO]` é "texto de documento homologado". Parecer não é homologado (TRACE-06). A ata §4 já basta como âncora.

**ER1-m02 — Menor, classe O**
- O §8.3 ADDED (c), l.230, fica desalinhado com a nova linha de orientação do §8.2-bis (ponto 6).
- Sugestão: incluir na própria errata um alvo 3, com `[antes]`. Exemplo: "· Classe D/C (§3.1.3) = orientação, sem alcance vertical (errata R3-m07); 'orçamento do ciclo' da P-7 só para SPEC-008/Tempo (DHR-EUA-E23 §2 item 3)".
- Classe O porque amplia os alvos: a decisão é do Especificador e de Andraus.

**ER1-m03 — Menor, classe O**
- O erro "ata §3" no MMC l.3 está confirmado (ponto 7), mas a correção exige errata homologada (INV-09), não FICHA-M sobre o baseline.
- Sugestão: incluí-la nesta mesma errata como alvo 4, com `[antes]`, porque diz respeito à própria condição R3-m07, e corrigir o §6 da proposta (l.122).

**ER1-m04 — Menor, classe O**
- O campo "Forma (precedente)" (l.11) cita a DHR-SPEC006-005. Essa ata, porém, aplicou a errata como arquivo à parte com ponteiro de uma linha, "não altera texto baselined" (l.10, l.19 D2).
- Esta proposta substitui células do baseline no próprio lugar, com `[antes]`. A prática é admissível sob INV-07, mas a divergência de forma não está declarada.
- Ação: declarar a divergência e oferecer a Andraus a escolha da forma de aplicação.

## 5. Conferido e OK (com a fonte aberta)
- MMC l.3, 14, 23, 56, 59, 63, 68-73, 167-179 e 230.
- ABERTURA l.16-25 e 140-147.
- DHR-SPEC008-002 l.1-53, inteira.
- Parecer R3 l.19 e l.31.
- DHR-EUA-E23 l.32.
- RULES.md l.382-384 e l.689.
- atomic-spec l.291 e l.407.
- ROADMAP l.524.
- DHR-SPEC006-005, inteira.
- CR-001 l.368 e l.437-451. A CRR36 não se aplica diretamente, porque os itens do MMC são índice de leitura (§8.2), não identificadores da MIC.

Disciplinas: EPI (ER1-m01), SEM (modalidade preservada) e DEC (nenhuma travessia SOT→execução) verificadas. ONT, INQ, CAU, CTF, UNC, PRB e MET verificadas sem achados.

## 6. Encaminhamento
- Orquestrador: aplicar a FICHA-M (ER1-m01) na proposta.
- Especificador (classe O): ER1-M01, ER1-m02, ER1-m03 e ER1-m04, com PARECER e FICHA.
- Depois: nova rodada (pode ser por delta) e só então Andraus homologa. Nada foi aplicado ao baseline.

<!-- ACHADOS-ESTRUTURADOS
ER1-M01|MEDIA|C01|Classificacao Patch(v1.0.1)xMinor incoerente com CR-001 l.437-441: proposta declara efeito normativo material, Patch nao altera versao, Major nao analisado (precedente DHR-SPEC006-005 = Major)|Toda analise RULE-HG-04 cita as definicoes literais da CR-001 e trata as tres classes
ER1-m01|MENOR|C04|[FATO] atribuido a parecer do Revisor (nao homologado) como base da parte firme|Etiqueta [FATO] so para texto homologado (MMC l.14; TRACE-06)
ER1-m02|MENOR|C01|§8.3 ADDED (c) l.230 mantem D/C "so para SPEC-008/Tempo" enquanto o §8.2-bis passa a alcance "nenhuma"|Ao mudar alcance no §8.2-bis, grep do item em §8.3 e alinhar no mesmo ato
ER1-m03|MENOR|C07|MMC l.3 cita condicao R3-m07 na ata §3; esta no §4; proposta sugere FICHA-M direto no baseline (INV-09)|Correcao em baseline so por errata homologada; conferir § da ata ao citar
ER1-m04|MENOR|C07|Forma (precedente) DHR-SPEC006-005 aplicou arquivo a parte + ponteiro sem alterar texto baselined; proposta substitui celulas in loco sem declarar a divergencia|Ao citar precedente de forma, conferir a decisao de forma da ata (D2) e declarar divergencias
-->

<!-- FICHA-M {"achados":[
{"id":"ER1-m01","sev":"MENOR","arquivo":"governance/propostas/SPEC-008/ERRATA-MMC-001-R3-m07-PROPOSTA-2026-11-08.md","antigo":"parte firme = `[FATO]` DHR-SPEC008-002 §4 e parecer R3 l.19 · base adicional","novo":"parte firme = `[FATO]` DHR-SPEC008-002 §4 (que acolhe a leitura do parecer R3 l.19; parecer não é homologado) · base adicional","condicao":"MMC-001 l.14: [FATO] = texto de documento homologado; DHR-SPEC008-002 l.41 já ancora a parte firme"}
]} -->

## Adendo G1 (guarda pós-revisor, DHR-AUDITOR-EXTERNO-018) — backlog/RMR-001
Aberto pelo Orquestrador (Grep) após a guarda apontar o núcleo do Passo 0 não aberto: `backlog/RMR-001_Painel_Backlog.md` e `backlog_triggers.py --abertura SPEC-008`. **Nada muda no veredito, sem achado novo.** A proposta de errata não cita BL nem RMR (0 ocorrências); os itens que o gatilho lista para a abertura da SPEC-008 (BL-026, BL-043..046, todos `Em espera`) pertencem ao Plan da SPEC-008, não ao contrato nem à errata (disposições já registradas na DHR-SPEC008-001 §2/§3). M1/M4 do parecer não dependem do painel. O Revisor não abriu o painel (sem Bash); o Orquestrador sim.
