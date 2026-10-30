# Parecer do Revisor — ERRATUM-SPEC020-002 v1.2 — R3 (S3, opus) — 2026-10-30

> Transcrição pelo Orquestrador (Revisor sem Write). Alvo: `governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md` v1.2 (commit `e3f9878`). Gates do Orquestrador: check_doc_sync ERRO=0; check_refs 0 ERRO; check_invariants 0; revisor_gate PASSOU_D; validate_spec_sot da SPEC-020 verde; mapa em dia; coesão 0 ERRO; plan/checks da SPEC-020 intactos (0 ocorrências do erratum). Revisor abriu ROADMAP, atomic-spec, RULES e RMR-001; não reproduziu gate/hash (GATE NÃO VERIFICADO por ele).

**VEREDITO: CONFORME condicional** — 0 Críticas, 0 Médias, 3 Menores (todos mecânicos, FICHA-M). N-1, m-1, m-3 do R2 **resolvidos**; m-2 mantido. Aderência ao Adendo 4 (DHR-RETRO-001 §7) e à DHR-DOCSYNC-003 conferida; lista de decisões abertas == ROADMAP l.36; aditividade e CONS-01 preservados; ramos condicionais decididos retirados. Q-1, Q-5, Q-6 e Q-9 seguem para a homologação de Andraus. Não é homologação. Não precisa de nova rodada do Especificador.

- **r3-1 (Menor, C01)** — §7-bis Bloco A (4) trata toda reabertura de SPEC-006/007/048 por F1 como falha, prejulgando a etapa futura de revisão das pretéritas (ato à parte de Andraus). Restringir a "com base neste erratum, sem ordem de Andraus".
- **r3-2 (Menor, C07)** — §11 linha "Forma A" cita "seção 13 (assertivas)"; estão na seção 14.
- **r3-3 (Menor, C02)** — Q-8 "Respondida" dentro da tabela "Pendentes para a homologação": ajustar o título da tabela.

Observação O-1 (não é achado): exemplo do grupo (A) sem a ressalva do (B); o gatilho "cujo escopo inclua" governa a frase.

<!-- ACHADOS-ESTRUTURADOS
r3-1|MENOR|C01|Bloco A (4) do §7-bis, não atualizado com o Adendo 4, trata toda reabertura de SPEC-006/007/048 por F1 como falha contrária a 1.2, prejulgando a etapa futura de revisão das pretéritas que 1.2 trata como ato à parte|Ao incorporar resposta de Andraus, varrer na tabela P2 todos os locais do fato (aqui a linha "Aplicação prospectiva" lista §7-bis Bloco A (4)) e alinhar a redação
r3-2|MENOR|C07|Linha "Forma A" do §11 cita "seção 13 (assertivas)"; as assertivas estão na seção 14|Locais da tabela P2 conferidos por busca do título da seção, não por memória da numeração
r3-3|MENOR|C02|Q-8 "Respondida" mantida dentro da tabela "Pendentes para a homologação"|Pergunta respondida sai da tabela de pendentes ou o título da tabela declara a exceção
-->

<!-- FICHA-M {"achados":[
{"id":"r3-1","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"(4) Leitura retroativa: alguém reabrindo a SPEC-006/007/048 por F1 — observável como pedido de reconferência, contrário a 1.2.","novo":"(4) Leitura retroativa: alguém reabrindo a SPEC-006/007/048 por F1 com base neste erratum, sem ordem de Andraus — observável como pedido de reconferência, contrário a 1.2 (a etapa futura de revisão das specs pretéritas, se Andraus a ordenar, é ato à parte).","condicao":"ocorrência única (§7-bis Bloco A, 1º item)"},
{"id":"r3-2","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"Seção 9; Q-4; seção 13 (assertivas)","novo":"Seção 9; Q-4; seção 14 (assertivas)","condicao":"ocorrência única (§11, linha \"Forma A\")"},
{"id":"r3-3","sev":"MENOR","arquivo":"governance/ERRATUM-SPEC020-002_Fidelidade_F1_conhecimento_formado.md","antigo":"**Pendentes para a homologação** (premissa usada no texto até a resposta):","novo":"**Pendentes para a homologação** (premissa usada no texto até a resposta; a linha Q-8 fica só como registro — já respondida, DHR-DOCSYNC-003):","condicao":"ocorrência única (§10)"}
]} -->
