# Parecer do Revisor — ERRATUM-SPEC020-002 v1.0 (metade F1 da dimensão B) — R1 integral (S3, opus) — 2026-10-30

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md` v1.0 (commit `ca724ed`). Gates do Orquestrador: check_refs 0 ERRO; check_invariants 0; revisor_gate PASSOU_D; mapa em dia; plan/checks da SPEC-020 intactos; `check_doc_sync` ERRO=1 = **falso positivo do detector** (substring "C-001" em "SPEC-020-PRINC-001", `check_doc_sync.py` l.253–260, confirmado pelo Revisor). Revisor abriu ROADMAP, atomic-spec, RULES e RMR-001; não reproduziu gate/hash.

**VEREDITO: NÃO CONFORME** — 0 Críticas, 4 Médias, 5 Menores. Aditividade e CONS-01 (nenhuma decisão fechada) confirmados; 6 verificações de F1 batem com o texto literal de RULE-KFH-005/006; limiares INDETERMINADO sem número (R-5); BL-017 PARCIAL/`Em espera` conferido.

- **M-1 (C08)** — SPEC-020-PRINC-001 listada como "Permanecem ABERTAS", mas o ROADMAP (que prevalece) a dá FECHADA (l.37) e a DHR-SPEC020-001 l.28 a declara EFETIVA; as atas citadas como [FONTE] não a listam (CONS-01 invertido). A causa foi a **ordem de serviço do Orquestrador** ter copiado a lista do AGENTS.md §7 (defasado). Retirar da lista de abertas; reescrever a Nota (FECHADA no ROADMAP/DHR-SPEC020-001; AGENTS.md §7 defasado; saneamento é de Andraus — Q-8); corrigir [FONTE]; evitar "— FECHADA" colado ao ID.
- **M-2 (C05)** — afirma verificação determinística dos itens 1–6 ("nunca de um LLM", "sem juízo de LLM") que não existe; o Revisor é detector (SPEC-020 D6 passo 7, RULE-EV-02). Separar parte literal (busca) de parte semântica (detector), declarar quem dá o veredito e registrar a lacuna de gate determinístico para F1.
- **M-3 (C10)** — usa estados do D5 sem mapear "não aplicável", sem caminho NOT_EVALUATED→PASS e sem lugar no schema (enum `lente` inalterado). Mapear a estado/transição existentes ou declarar MODIFIED; declarar a forma do registro.
- **M-4 (C01)** — §1.2 obriga toda Spec a registrar F1; §8 diz só as que formam conhecimento; retroatividade não declarada; o argumento Minor depende disso. Alinhar, declarar prospectiva × reconferência e refazer a análise Minor/Major.
- **m-1..m-4 (mecânicos, FICHA-M)** — Q-2 cita ERRATUM-001 com formato errado; INHERITS omite ADV-KFH-01 e EC-KFH-004; SPEC-006 "só consome" (admite pelo caminho (b)); lacuna da Q-7 omite mitigações do ADV-KFH-03.
- **m-5 (C08, não mecânico)** — declarar a fronteira para conhecimento formado de experiência / caminho (a) (K-001 aberta) sem decidi-la.

Observações: O-1 detector `check_doc_sync.py` sem limite de palavra (proposta de melhoria; arquivo é de Andraus); O-2 a ordem de 2026-10-30 ainda não está em ata. Condição de nova revisão: 4 Médias resolvidas sem novo ID de RULE/BASpec/EC/ADV, sem editar baseline; `check_doc_sync` sem o ERRO da l.100. Teto pós-correção: CONFORME condicional (gate não reproduzido pelo Revisor).

<!-- ACHADOS-ESTRUTURADOS
M-1|MEDIA|C08|Lista de decisões abertas copiada do AGENTS.md §7 (defasado) via ordem de serviço, contra o ROADMAP que prevalece; [FONTE] cita atas que não contêm o ID|Ordem de serviço e Especificador devem extrair abertas/fechadas só do ROADMAP l.36/l.37 e conferir cada ID na fonte citada
M-2|MEDIA|C05|Erratum afirmou verificação determinística ("nunca de um LLM", "sem juízo de LLM") inexistente; Revisor é detector (SPEC-020 D6 passo 7, RULE-EV-02)|Para todo critério novo, declarar a parte literal (gate possível) separada da parte semântica (detector) e quem dá o veredito
M-3|MEDIA|C10|Uso dos estados do D5 da SPEC-020 sem mapear "não aplicável", sem caminho de transição e sem lugar no schema (enum lente inalterado)|Ao reutilizar uma máquina de estados herdada, mapear cada resultado novo a um estado e a uma transição existentes, ou declarar como MODIFIED
M-4|MEDIA|C01|§1.2 obriga toda Spec a registrar F1; §8 diz só as que formam; retroatividade não declarada; argumento Minor depende disso|Na análise de impacto, enumerar quem passa a ter obrigação nova e se retroage, antes de argumentar a compatibilidade
m-1|MENOR|C07|Q-2 atribui ao ERRATUM-SPEC020-001 formato que ele não usou ("FECHÁVEL e FECHADA")|Conferir citação de precedente pelo texto literal
m-2|MENOR|C04|INHERITS omite ADV-KFH-01 e EC-KFH-004, citados no corpo|Gerar INHERITS a partir de todos os IDs citados no corpo
m-3|MENOR|C02|SPEC-006 descrita como "só consome" o carimbado; ela admite pelo caminho (b)|Usar o verbo do papel da Spec vizinha conforme o plan dela
m-4|MENOR|C07|Lacuna Q-7 omite mitigações declaradas no ADV-KFH-03|Ao declarar lacuna, citar o que já existe
m-5|MENOR|C08|Fronteira de F1 para conhecimento de experiência / caminho (a) (K-001 aberta) não declarada|Declarar exclusões de escopo que tocam decisão aberta sem decidi-la
-->

<!-- FICHA-M {"achados":[
{"id":"m-1","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"(como o ERRATUM-SPEC020-001 fez com *tool correctness*)","novo":"(o ERRATUM-SPEC020-001, diferentemente, declarou *tool correctness* \"FECHÁVEL e FECHADA\")","condicao":"ocorrência única (linha da Q-2)"},
{"id":"m-2","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"EC-KFH-003; ADV-KFH-03/04/05/13/24; Cenário-KFH-T06..T09. SPEC-048","novo":"EC-KFH-003/004; ADV-KFH-01/03/04/05/13/24; Cenário-KFH-T06..T09. SPEC-048","condicao":"ocorrência única (INHERITS, §5)"},
{"id":"m-3","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"Uma Spec que só **consome** conhecimento carimbado (ex.: SPEC-006, SPEC-048) é conferida","novo":"Uma Spec que só **admite ou consome** conhecimento carimbado (ex.: SPEC-006, que o admite pelo caminho (b); SPEC-048, que o consome) é conferida","condicao":"ocorrência única (§1.2)"},
{"id":"m-4","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"há só o risco residual RU-1 (\"eficácia = INDETERMINADA até calibração\")","novo":"há só o risco residual RU-1 (\"eficácia = INDETERMINADA até calibração\"; mitigações declaradas no ADV-KFH-03: visto de lote para definições/regras (P-2) e marca de contradição)","condicao":"ocorrência única (§3, Lacuna registrada)"}
]} -->
