# DHR-SPEC002-VERBATIM-001 — Ata de Decisão — Captura Verbatim Diferida (RULE-ECC-04) na Abertura da SPEC-002

| Campo | Valor |
|---|---|
| De | Andraus — Decisor Final / Consensus Authority |
| Para | Especificador SOT / Revisor SOT / Controlador |
| Ref | `specs/features/SPEC-002/DOSSIE-PESQUISA.md` §0/§6 — `[DECISÃO NECESSÁRIA: SPEC-002-VERBATIM-001]` |
| Data | 2026-09-28 |
| Status | **DECIDIDO — Opção A** |
| Natureza | Decisão de governança pontual sobre RULE-ECC-04 (Captura Verbatim de Fonte), não homologação de baseline nem da abertura da SPEC-002 como um todo |

---

## 1. Contexto

A SPEC-002 é a **primeira Spec sob RULE-ECC-04** (prospectiva desde SPEC-002, DHR-VERBATIM-SRC-001). Nesta sessão, **WebSearch operou normalmente** (pesquisa real, 7 fontes com URLs reais), mas **WebFetch está bloqueado por política de egresso** (EGRESS_BLOCKED — não-retryável nesta sessão). Consequência: os 7 registros em `specs/features/SPEC-002/sources/SRC-01..07-*.txt` documentam honestamente URL + data + método (WebSearch) + trecho retornado pelo buscador — **não são captura verbatim canônica** (que exigiria *fetch* real da página, como feito em SPEC-046). Nenhuma fonte foi inventada (RULE-MET-01); a limitação está registrada em `sources/_LIMITACAO-WEBFETCH.txt`.

O Dossiê apresentou três opções (§6): **(A)** homologar a definição agora e diferir a captura verbatim para sessão com WebFetch liberado, antes do gate do Plan; **(B)** exceção via RULE-HG-07; **(C)** suspender a abertura até o WebFetch voltar.

## 2. Decisão

**Opção A — ACEITA.**

1. A **avaliação de conteúdo** do Dossiê de Pesquisa e da Proposta de Abertura da SPEC-002 **prossegue normalmente** para o parecer do Revisor sobre o gate de abertura (ROADMAP §23 passo 1-bis) — RULE-ECC-02 (pesquisa de fato realizada) está satisfeita e não é bloqueada por este ato.
2. **RULE-ECC-04 (captura verbatim canônica) fica formalmente DIFERIDA**, não dispensada: as 7 fontes em `sources/` permanecem etiquetadas como baseadas em WebSearch (não-verbatim) até que uma sessão com WebFetch operacional refaça a captura real das páginas citadas.
3. **Condição de fail-closed reposicionada:** a captura verbatim real é **pré-condição para o gate do Plan** (`plan.md`/`checks.md`) — não para o gate de abertura (Dossiê/Proposta) em curso agora. Ou seja: o Especificador pode prosseguir com a abertura e, mais adiante, com a redação do Plan, mas o Plan **não pode ser submetido ao Revisor para o protocolo semântico completo enquanto RULE-ECC-04 não estiver satisfeita** para as fontes que sustentam alegações carregadas.
4. Nenhuma fonte com captura pendente pode ser citada no Plan como `[FONTE]` com força probatória de verbatim; até a recaptura, permanece `[PROPOSTA]`/`[INFERÊNCIA]` conforme já etiquetado no Dossiê.

## 3. Efeitos imediatos

1. Este documento — registrado no histórico de DHRs.
2. `specs/features/SPEC-002/sources/_LIMITACAO-WEBFETCH.txt` permanece como registro de honestidade metodológica; não é substituído até a recaptura.
3. O próximo gate segue seu curso: **parecer do Revisor SOT sobre o Dossiê/Proposta de Abertura** (conteúdo, Constitution Check preliminar, RULE-ECC-01/02, RULE-MECH-01) — não bloqueado por esta decisão.
4. Item de acompanhamento (não é decisão aberta CONS-01, é pendência operacional): **recaptura verbatim das 7 fontes SRC-01..07 em sessão com WebFetch liberado**, antes de submeter `plan.md` ao protocolo semântico do Revisor.
5. Nenhum modelo canônico tocado (CONST-01); nenhuma decisão aberta (J-001 etc.) fechada (CONS-01); SPEC-002 continua sendo o próximo trabalho autorizado pela ordem regular (ROADMAP §25).

---

**Andraus**
*Decisor Final — SOT SISTEMA TRADING*
