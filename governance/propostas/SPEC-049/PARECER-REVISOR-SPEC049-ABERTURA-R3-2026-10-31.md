# Parecer do Revisor — Proposta de Abertura da SPEC-049 (WikiRAG Reading View) — R3 por delta (S2, sonnet) — 2026-10-31

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). Alvo: `specs/features/SPEC-049/ABERTURA.md` (revisão 3) + `research.md`.
> MODO: delta
> SHA256-ALVO: 452a4a0ef76bd73b67ea1c3783f193890866525ad732fbce0d15cee973f9f87f (valor recebido; o Revisor não calculou — sem Bash)
> SHA256 research.md: a597804cea044efaa9e5264a0be54643b8fc104017ddcbc33b675a562cda793b (recebido)
> TOKENS: 105622
> **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 1 Menor novo (R3-m01). R2-m01 e R2-m02 resolvidos.

## 1. Veredito
Condicional por: `revisor_gate` não chamado pelo Revisor (gates do Orquestrador = dado de estado); P-1..P-7 e C-1..C-4 dependem do ato de homologação de Andraus; teto do Revisor numa abertura. Sem homologação nem autorização de Plan; nenhuma decisão aberta fechada.

## 2. Passo 0 e passos
Passo 0 mantido do R2 (ROADMAP l.192-193 e 523: slot "Indicativo, NÃO aberta"; RULES l.518-531: 1.600 exige confirmação de Andraus). Passos 2, 3, 4/4-bis, 7, 8: PASS. Passos 5/5-bis/6 não incidem. Bloco C: EPI com a premissa de janela de validade etiquetada `[INFERÊNCIA]`; demais disciplinas sem achados; nenhuma BASpec cruza para execução.

## 3. Conferência das mudanças da R3 (fontes abertas agora)
- **R2-m01: resolvido.** SPEC-006 plan l.1419-1420 (`valid_from` "nós também têm validade — CKG-012"; `valid_to` em `record_kind=invalidation`), l.718 e l.1073 (`INVALIDATED_IN_TIME` = invalidação com `valid_to` SEM sucessora), SPEC-007 l.683-685 (RULE-KFH-009, extensão local [PROPOSTA]); relação × nó: SPEC-006 l.322, 395-400, 710. Cond. 13 do §15: derivar a janela da SPEC-006/007 "sem inventar campo"; sem origem ⇒ "validade não informada" (fallback de S6 evita vigência falsa).
- **R2-m02: resolvido.** research §3.5 (l.109) e §3.8 (l.122) repetem S5 (a)/(b); SPEC-007 l.1678 (EC-KFH-010), 873, 2066 conferem; cond. 14 manda declarar reutilização ou código próprio `WRV`.
- **Respostas de Andraus: registro, não homologação.** Grep por `homologad` no ABERTURA: nenhuma ocorrência afirma "HOMOLOGADA" como fato (l.3 e l.10: "NÃO é homologação"; §12 é redação futura proposta; l.216 e cond. 8 no futuro condicional). 12 marcas `RESPONDIDA/CONFIRMADA` (P-1..P-7, C-1..C-4 + cabeçalho §13). CONS-01: nota final da §13 (l.258) mantém abertas J-001, G-001, K-001, C-001, M-001, N-001, SPEC-045-RUNTIME-001, ECC-03-001, WF-D03, CKG-STRUCT-ORIGIN-001; P-2 diz que SPEC-045-RUNTIME-001 segue ABERTA. As respostas aparecem só como relato do Orquestrador: o chat de Andraus não está no repositório; a ata é que deve fixá-las.
- **Dimensionamento:** ≈1.570 (HIGH, faixa 1.420-1.620, proporcional ≈1.610) e ≈1.380 (MEDIUM) consistentes em §1, §3, §13 P-1/P-7, §16 e research §8.2; sem resíduo de ≈1.250/≈880 fora de `[antes:]`. RULES l.526-527 confere.
- **Cascata `valid_at`/quatro campos:** 9 ocorrências no ABERTURA; "quatro campos" em S7 e cond. 2; `valid_from`/`valid_to` só em S1 (iv) e S6, ancorados; "único tempo" só dentro de `[antes:]`.
- **Referências SPEC-048:** Grep de `SPEC-049|reading_view_ref` = 34 linhas = 31 + 3 (l.1103/1267/1439), como o research §8.3 declara.
- **sources/:** blocos alterados do research acrescentam só texto do SOT; os verbatim `[EXTERNO]` são idênticos aos do R2 por inspeção; os 14 SRC e 6 REPO não foram reabertos (declaração do Orquestrador de que `sources/` não mudou; conclusão ECC-04/06 HERDADA do R1/R2).

## 4. Achado novo
**R3-m01 (MENOR, C06/C02):** `research.md` cabeçalho, linha da "Validade do Dossiê" (l.10) ficou condicional e ainda lista as duas datas ("Se Andraus confirmar MEDIUM … 2027-02-28. Se confirmar HIGH … 2027-01-29"); a l.9 do mesmo cabeçalho e o ABERTURA §1 já registram HIGH decidido (validade 2027-01-29). Resíduo de "a confirmar" depois da resposta de Andraus; não é contradição. Ação: alinhar a l.10 a "HIGH decidido, validade 2027-01-29" e preservar o texto antigo em `[antes:]`. Não bloqueia.
Observação sem severidade (herdada do R2, não reaberta): ABERTURA §4 (l.124) cita "SPEC-007 l.433-436" para as definições de efeito permanente/externo — correto (os caminhos E3 estão em l.438-441).

<!-- ACHADOS-ESTRUTURADOS
ID|SEV|CATEGORIA|CAUSA|PREVENCAO
R3-m01|MENOR|C06|Ao registrar a resposta de Andraus (HIGH), a linha de validade do cabeçalho do research manteve a alternativa MEDIUM/2027-02-28 como condicional|Ao registrar uma resposta de Andraus, fazer Grep do mesmo conceito (aqui: complexidade e data de validade) em todas as células do cabeçalho de ambos os arquivos
-->

<!-- FICHA-M {"achados":[]} -->
(R3-m01 exige reescrever uma frase condicional: fica com o Especificador. Zero achados M.)

## 5. Cobertura por bloco
ABERTURA (20 blocos; 8 alterados): cabeçalho, §1, §2 S1-S11, §3, §6, §11, §13, §15 = conferido agora; Status/Complexidade, contagens, decisões abertas (§10), tabela de decisões abertas (§13 nota final) e Constitution Check = conferidos integralmente; §2 contratos, §4, §8, §9 = amostra (SPEC-007 l.1224/1225/1228 literais; l.432-447; 34 linhas na SPEC-048; BL-003/010/011/017/029/035 no painel RMR-001 e `spec:SPEC-049` = 0 ocorrências); §7, §12, §14, §16 = HERDADOS do R2. Amostra anti-leniência (≥5 inalterados): §2 contratos, §4, §8, §9, RULES l.518-531, ROADMAP l.192-193 e 523 — sem achados.
research (27 blocos; 6 alterados): §3.1, §3.3, §3.5, §3.8, §8.1 e cabeçalho conferidos agora (R3-m01 no cabeçalho); §0 e §8.2 como dependentes; §3.2, §3.4, §3.6, §3.7, §3.9, §3.10, §7, §8.3, §8.4, §9 lidos e coerentes (aspas `[EXTERNO]` HERDADAS do R2); §4 e `sources/` HERDADOS (R1/R2), sem releitura nem hash.

## 6. Não pude verificar
Resultado de qualquer gate · sha256 do alvo e do research (sem Bash) · veracidade das páginas web e números dos repositórios; adulteração de `sources/` (risco residual) · as respostas de Andraus no chat (fonte primária fora do repositório) · se um nó `learning` carrega de fato janela de validade no desenho final da SPEC-006/007 (cond. 13 trata no Plan) · interpelação formal ao Especificador.

## 7. Encaminhamento
Abertura pronta para a homologação de Andraus (ato dele; ata a registrar P-1..P-7 e C-1..C-4). O R3-m01 é Menor e não bloqueia: pode ir ao Especificador (classe O) com a próxima correção ou ficar como condição da homologação, à escolha de Andraus (AGENTS §12). CONFORME condicional não é homologação nem autorização do Plan.
