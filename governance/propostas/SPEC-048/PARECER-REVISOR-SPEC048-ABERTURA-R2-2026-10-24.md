# Parecer do Revisor — Abertura da SPEC-048 (Revisão 3 do Especificador), rodada 2 (S3) — 2026-10-24

> Transcrição pelo Orquestrador do relatório do Revisor SOT (somente leitura). **Veredito: CONFORME condicional** — 0 Críticas, 0 Médias, 7 Menores (r2-m01..r2-m07), 1 observação. Condição: gate não executado pelo Revisor (o Orquestrador rodou `revisor_gate.py` completo = PASSOU_D). Não é homologação; não autoriza Plan; nenhuma decisão aberta fechada (CONS-01). Recomenda corrigir por delta r2-m01 (principal), r2-m02 e r2-m03 antes de homologar.

## Conferido
Menores do R1 sem regressão (m-01 critério de busca em ABERTURA §8 l.145 e research §8.2 l.193; m-03 transcrição literal de SPEC-007 plan l.1224; m-05 lacuna analista↔modelo; m-06 ECC-05 não incide; m-07 inventário; §15 com as 8 condições do Plan). Recorte do Anexo T entre 048 e 049 confere com a SPEC-007 (Anexo T l.1948-2519): regras 7 na 048 / RULE-KFH-015 na 049; 4 cláusulas (2 vão à 049: "compilação WikiRAG" da INV-KFH-02, "lado a lado na WikiRAG" da RULE-KFH-016); EARS 7 / 1; BASpec 7 / 1; EC 3 + parte do EC-010 / EC-009 (E1); cenários 7 + parte da T25 / T21; ADV 9 inteiros + partes de 4 / partes de 2. SPEC-048 coerente sozinha sem a WikiRAG; §2-bis declara escopo/peso/Classe da SPEC-049 como [PROPOSTA] (número e nome de Andraus). Divisão BL-010/BL-017 consistente com DHR-SPEC007-002/005. Q-1..Q-8 fiéis às respostas; C-1 e C-2 bem formadas. SPEC-049 livre (só ocorre em `reference/camadas/`, outro espaço de nomes). Nenhuma decisão aberta fechada.

## Menores
- **r2-m01 (principal; corrigir antes de homologar)** falta propor a correção de endereço criada pela divisão: a SPEC-007 BASELINE ainda aponta a WikiRAG para a SPEC-048 (plan.md l.63, 64, 71, 308, 319, 359, 443, 711, 1731, 1801 e título do Anexo T l.1948), a ata DHR-SPEC007-002 (tabela l.34) e o ROADMAP l.189/l.517. Ação: acrescentar ao critério de §8 "toda menção a SPEC-048 junto de WikiRAG/página de leitura, em Spec baselined ou ata → SPEC-049 (nota aditiva, INV-09)", listar ROADMAP l.189/l.517 em §12, opcionalmente C-3 a Andraus. Base: atomic-spec §15 itens (5)(6).
- **r2-m02** research.md com texto defasado (l.207 "até Andraus decidir a Q-ABERTURA-6"; l.222; l.119; l.9 "Complexidade proposta"; l.136 graphrag "WikiRAG por regra fixa"): atualizar com texto anterior entre colchetes.
- **r2-m03** inventário "ficam na 048" omite T.3 (códigos de erro), T.6 (D6 Consulta), T.7 (contratos `evidence_packet`, `feedback_record`), T.13 (R-3, R-4, Bloco B, etiquetagem, roteamento, P-9); risco R-8 do T.13 deve ser dividido (parte de consumo fica na 048 = R-7 da ABERTURA) e desambiguado do R-8 de ABERTURA §11.
- **r2-m04** tabela §15 numerada fora de ordem (1,2,3,4,5,8,6,7). · **r2-m05** §8 l.147 diz "registrada na ata" mas a ata ainda não existe (ajustar tempo verbal). · **r2-m06** C-2 recomenda MEDIUM D0–D5 para a SPEC-049, mas ela herda a cláusula "compilação WikiRAG" da INV-KFH-02 (natureza E3 na SPEC-007): a recomendação deve dizer isso. · **r2-m07** BL-017 aparece duas vezes em §9 (l.153 e l.155): fundir.
- Observação: validade do Dossiê segue até 2027-01-22; Dossiê próprio da SPEC-049 continua obrigatório.

## Pendências de registro (Orquestrador/Andraus)
m-09 do R1 (ordem de abrir em ata); registro do slot SPEC-049 no ROADMAP; edição aditiva dos gatilhos de BL-010/BL-017 (Q-6 autorizada); ata registrando Q-1..Q-8.

## Não verificável
Gate (feito pelo Orquestrador); decisões de Andraus em chat (ainda sem ata); veracidade das fontes web.
