# DHR-PAP-001 — Ata de Homologação da Camada de Princípios do SOT

**Declaração formal de homologação por Andraus. Produz efeito normativo imediato.**

| Campo | Valor |
|---|---|
| ID | DHR-PAP-001 |
| Versão | 1.0 — BASELINE HOMOLOGADA |
| Autoridade homologadora | Andraus (Decisor Final / Consensus Authority do SOT) |
| Data de homologação | 2026-09-15 |
| Sessão | Claude Cowork — SOT SISTEMA TRADING |
| Registrado por | Revisor de Especificação (registro de ato declarado por Andraus) |

---

## 1. Declaração de Homologação

Andraus, na qualidade de Decisor Final e única autoridade de homologação do SOT, declara em 2026-09-15:

> **"Homologo."**

Esta declaração abrange os três documentos produzidos e submetidos nesta sessão, listados no §2, os quais passam imediatamente ao status **HOMOLOGADO — BASELINE**.

---

## 2. Documentos homologados

| ID | Nome | Versão | Status anterior | Status a partir de 2026-09-15 |
|---|---|---|---|---|
| **GPR-001** | Guia de Princípios, Relações e Organicidade do SOT | 1.0 | PROPOSTA | **HOMOLOGADO — BASELINE** |
| **PP-PAP-001** | Pacote de Partida — Protocolo de Adesão Progressiva ao GPR-001 | 1.0 | PROPOSTA | **HOMOLOGADO — BASELINE** |
| **PE-PR-PAP-001** | Prompts de Invocação do Especificador e do Revisor para o PAP-001 | 1.0 | PROPOSTA | **HOMOLOGADO — BASELINE** |

Localização canônica de cada documento:
- `claude/GPR-001_Guia_Principios_Relacoes_SOT.md`
- `claude/PP-PAP-001_Pacote_Partida_Protocolo_Adesao_Progressiva.md`
- `claude/PE-PR-PAP-001_Prompts_Especificador_Revisor_PAP001.md`
- Cópias locais: `governance/` do SOT-Harness

---

## 3. O que a homologação estabelece

### 3.1 GPR-001 como camada normativa de princípios

O GPR-001 v1.0 torna-se a **camada de princípios normativa do SOT**. A partir desta data:

- Os **44 princípios** organizados em 6 classes (PC-01..PC-08, PB-01..PB-10, PE-01..PE-08, PCO-01..PCO-07, PO-01..PO-07, PS-01..PS-04) são referência de governança para o projeto.
- O **algoritmo cognitivo do SOT** em 19 passos, o **modelo de organicidade** e os **12 anti-padrões** (AP-01..AP-12) passam a integrar o corpo normativo.
- A **Constitution Check** de 14 itens do GPR-001 é o checklist de referência para qualquer novo documento normativo do SOT.
- Os princípios do GPR-001 são a fonte primária para o Revisor verificar conformidade principiológica a partir de agora.

### 3.2 PP-PAP-001 como contrato de escopo do PAP-001

O PP-PAP-001 v1.0 torna-se o **contrato de escopo** contra o qual o PAP-001 será produzido e revisado:

- Os **6 blocos obrigatórios** (§2 do PP-PAP-001) são o escopo mínimo do PAP-001.
- As **5 decisões abertas K-PAP-001..005** (§8 do PP-PAP-001) são as únicas questões em aberto — o Especificador as expõe, Andraus as resolve na homologação do PAP-001.
- As **fronteiras** do §3 e os **invariantes** do §4 são invioláveis na redação do PAP-001.

### 3.3 PE-PR-PAP-001 como protocolo operacional de invocação

Os dois prompts (Bloco A — Especificador; Bloco B — Revisor) do PE-PR-PAP-001 v1.0 tornam-se os **prompts operacionais** para a produção e revisão do PAP-001:

- O **Bloco A** é o prompt a colar na sessão do Especificador para iniciar a redação do PAP-001.
- O **Bloco B** é o prompt a colar na sessão do Revisor para auditar o PAP-001.
- A tabela de verificação de blocos (§4, Passo 3) do Bloco B é o checklist de revisão específico do PAP-001.

---

## 4. Decisões implícitas desta homologação

| Decisão | Conteúdo |
|---|---|
| D-DHR-PAP-001-01 | O regime de aplicabilidade de princípios é progressivo por classe: PC-* retroativo-como-auditoria; PB-*/PE-* prospectivo a partir do PAP-001 homologado; PCO-*/PO-*/PS-* ativado-por-contexto. |
| D-DHR-PAP-001-02 | O Manual Universal de Engenharia de Princípios Agênticos v2.0 (`governance/MANUAL_UNIVERSAL_ENGENHARIA_DE_PRINCIPIOS_AGENTICOS (1).md`) é referência externa classificável — não é normativo por si mesmo; todo princípio importado requer ficha quadripartite + justificativa + homologação de Andraus. |
| D-DHR-PAP-001-03 | O SOT opera atualmente no **Tier 2 (Risk-Informed)** do NIST AI RMF. O objetivo da camada de princípios é atingir o **Tier 3 (Repeatable)** — processos formalizados, implementados consistentemente, revisados periodicamente. |
| D-DHR-PAP-001-04 | O Revisor fica autorizado a aplicar o GPR-001 como checklist de conformidade principiológica a partir desta data, usando o regime de classes definido em D-DHR-PAP-001-01. |
| D-DHR-PAP-001-05 | O PAP-001 é pré-condição para homologação do SPEC-001, mas não bloqueia o **início** de redação do SPEC-001. Ambos podem ser escritos em paralelo. |

---

## 5. O que permanece em aberto (não resolvido por esta homologação)

As 5 decisões K-PAP-001..005 do PP-PAP-001 §8 permanecem abertas — serão resolvidas na sessão de homologação do PAP-001:

- **K-PAP-001**: localização do Inventário de Conformidade (separado vs. embutido no GPR-001)
- **K-PAP-002**: frequência do ciclo de Hygiene
- **K-PAP-003**: autoridade de proposta de novo princípio
- **K-PAP-004**: escopo de aplicação do PAP-001 (specs de componente vs. também documentos de governança)
- **K-PAP-005**: mapeamento dos open decisions J-001..L-001 vs. GPR-001 no inventário inicial

---

## 6. Efeito imediato no Road Map

Com esta homologação, o Road Map do SOT acrescenta:

- **M1-PRE** (novo marco pré-M1): Camada de Princípios Estabelecida
  - GPR-001 HOMOLOGADO ✓
  - PP-PAP-001 HOMOLOGADO ✓
  - PE-PR-PAP-001 HOMOLOGADO ✓
  - PAP-001 — **A PRODUZIR** (próximo entregável; Especificador usa Bloco A do PE-PR-PAP-001)

Sequência autorizada a partir de agora:
1. Especificador produz o PAP-001 (usando Bloco A do PE-PR-PAP-001)
2. Revisor audita o PAP-001 (usando Bloco B do PE-PR-PAP-001)
3. Andraus homologa o PAP-001 (resolve K-PAP-001..005)
4. SPEC-001 pode ser homologado (pós PAP-001 homologado)

---

## 7. Princípio de Não-Regressão

Esta homologação não altera nenhum documento previamente baselined:
- Unidade Atômica v1.2 — inalterada
- GEH-001 — inalterado
- Road Map — inalterado (adicionado marco M1-PRE por registro, não por emenda)
- PEP-001 v1.2 — inalterado
- PRE-001 v1.1 — inalterado
- HRE-001 v2.1 / GRE-001 v2.1 — inalterados (o PE-PR-PAP-001 ESTENDE, não substitui)
- Decisões abertas J-001..L-001 / K-001 / C-001 — permanecem abertas

---

*Fim do DHR-PAP-001 v1.0. Ato declarado por Andraus em 2026-09-15. Registrado pelo Revisor de Especificação na sessão Claude Cowork — SOT SISTEMA TRADING.*

---

## Anexo A — Nota de Correção de Localização Canônica (2026-09-15)

**Natureza:** correção de rastreabilidade (INV-07 — não altera o ato de homologação nem o conteúdo normativo; o texto original do §2 é preservado como registro histórico).

A lista "Localização canônica" do §2 (linhas 34-38) referencia caminhos sob `claude/` (`claude/GPR-001…`, `claude/PP-PAP-001…`, `claude/PE-PR-PAP-001…`) anteriores à reorganização do repositório (ref.: `docs/arranque/MANIFESTO-reorganizacao.md`). Essa pasta `claude/` **não existe** no repositório atual. A localização canônica **vigente** dos documentos homologados é:

| Documento | Localização canônica vigente |
|---|---|
| GPR-001 | `governance/GPR-001_Guia_Principios_Relacoes_SOT.md` |
| PP-PAP-001 | `governance/PP-PAP-001_Pacote_Partida_Protocolo_Adesao_Progressiva.md` |
| PE-PR-PAP-001 | `governance/PE-PR-PAP-001_Prompts_Especificador_Revisor_PAP001.md` (v1.1) |
| Manual Universal | `governance/MANUAL_UNIVERSAL_ENGENHARIA_DE_PRINCIPIOS_AGENTICOS (1).md` |
| GEH-001 | `RETOMADA/GEH-001_Guia_Agente_Especificacoes_Harness.md` (v1.1) |

As cópias-duplicadas de GPR-001 e do Manual Universal na raiz do repositório foram removidas em 2026-09-15 (consolidação de baseline; cópias eram byte-idênticas às de `governance/`, sem referências vivas). Correlato: a correção equivalente de caminhos no PE-PR-PAP-001 está registrada em seu §0 (v1.1, re-homologado por DHR-PAP-001-A).

*Anexo A registrado pelo Revisor de Especificação em 2026-09-15.*
