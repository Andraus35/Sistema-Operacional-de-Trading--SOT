# PARECER — Camada hierárquica principiológica: necessidade de adiantamento como FASE de governança?

| Campo | Valor |
|---|---|
| Autor | Claude Code (Especificador/operador) |
| Data | 2026-09-22 |
| Ref | Auditoria a pedido de Andraus — analogia com SPEC-019 (harness hierárquico) |
| Status | `[PROPOSTA]` — não-normativo (TRACE-06). Registro de raciocínio. |
| Decisão de Andraus | **Não adiantar como FASE.** Ações (a)+(b)+(c) autorizadas. SPEC-020-PRINC-001 registrada. |

---

## 1. O conceito no repo
O metamodelo é o **CMHP-001** (`reference/camadas/CAMADA PRINCIPIOLÓGICA.MD`) — *Master Contract Principiológico*: governança hierárquica, convergência e propagação principiológica macro→micro (CMHP-001 §1).

**Achado central:** a hierarquia principiológica **já está homologada**, distribuída em três baselines que cobrem as três facetas do CMHP-001:

| Faceta CMHP-001 | Baseline que a cobre | Status |
|---|---|---|
| Conteúdo + hierarquia + precedência (classes PC>PB>PE>PCO>PO>PS; matriz de conflito §6; inversões §3.6) | **GPR-001** §2/§3.2/§5/§6/§3.6 | HOMOLOGADO (2026-09-15, DHR-PAP-001) |
| Convergência horizontal (nós, interfaces, sensor de drift) | **MAN-001** (importa "só a mecânica" do CMHP-001 §11–16/§38–39/§66–68/§79–81) | HOMOLOGADO (2026-09-20) |
| Propagação/herança vertical macro→micro (CMHP-001 §81) | **SPEC-019 / RULE-HV-01..04** | HOMOLOGADO (2026-09-22) |

CMHP-001 já classificado **referência externa não-normativa** (MAN-001 Q1); rótulos L0–L6 / I-01..I-12 rejeitados (K-MAN-02; CATALOGO l.107).

## 2. Por que a analogia com SPEC-019 NÃO se sustenta
Os dois gatilhos que justificaram adiantar a SPEC-019 estão **ausentes**:
1. **Sem decisão aberta bloqueadora** (não há "L-principiológico"; nenhuma decisão aberta ativa é bloqueador da hierarquia de princípios).
2. **Elo vertical já preenchido** — pela própria SPEC-019: RULE-HV-03 já opera `PC > PB/PE > regra local`. A propagação macro→micro dos princípios **é** a RULE-HV.

## 3. Delta real (declarativo → verificável)
GPR-001 é auto-avaliado L0–L1 (§11); precedência/conflito são gramática, não gate com Enforcement Contract; §68 defere observabilidade a "(SPEC a atribuir)". **Mas não pede FASE nova:**
- Enforcement spec-time já existe (CC-01..CC-10 + GPR-001 §15 + Revisor §14).
- **SPEC-020 núcleo A** (próximo trabalho) já cobre role adherence/correctness — operacionaliza o enforcement principiológico.
- Enforcement runtime é distribuído por design (GPR-001 §13/§15). Centralizar cedo feriria ROADMAP §24 e CC-02.

## 4. Recomendação (homologada por Andraus)
**NÃO adiantar como FASE.** O delta converge para a **SPEC-020 (núcleo A)** via **[DECISÃO NECESSÁRIA: SPEC-020-PRINC-001]**. Se enforcement formal de conflito for desejado depois, o veículo é **emenda ao GPR-001** (Enforcement Contracts na Matriz de Conflito §6), não uma FASE.

## 5. Ponto de atenção
CMHP-001 não tinha item de backlog dedicado (≠ BL-010..016). Como seus deltas já foram absorvidos (MAN-001 + SPEC-019 + GPR-001), registrar no RMR-001 §5 como "absorvido — sem delta residual" fecha o loop (ação (c)).

---

*Parecer do Claude Code. Decisão de Andraus 2026-09-22: não adiantar; registrar SPEC-020-PRINC-001; persistir parecer; rastrear CMHP-001. Próximo trabalho: SPEC-020 núcleo A.*
