# HOD-001 — Plano de Higiene e Organização Documental (PROPOSTA)

| Campo | Valor |
|---|---|
| Código candidato | **HOD-001** (plano de higiene documental — operação de manutenção governada) |
| Natureza | (1) Plano de reorganização de pastas + arquivamento de obsoletos + reparo de referências; (2) **Regra Permanente de Intake e Higiene da Raiz (RPIR)** — todo doc que chega à raiz e é tratado vai SEMPRE para sua pasta, ou é excluído da circulação quando não incorporado. Visa findability dos agentes e equilíbrio dos 4Es na busca |
| Status epistemológico | **HOMOLOGADA — FATO NORMATIVO** (Andraus, 2026-09-21; ata `DHR-HOD-001`). RPIR instalada (RCH-001 passo 8). **F1 EXECUTADA** (Ciclo Hygiene #2, RCH-001: 16 refs externas → `reference/camadas/`; raiz enxuta; CATALOGO §0 Mapa de Pastas). **F2/F3 diferidas** (HYG2-F01: INV-07 vs atas congeladas — Mapa de Pastas resolve). |
| Autoria | Especificador (Claude Code, Opus 4.8) |
| Data | 2026-09-21 |
| Alvo | Estrutura de pastas do repo; `governance/CATALOGO-OFICIAL.md` (mapa/índice); referências por caminho em vários docs |
| Fundamento no baseline | **INV-07** (nunca deleta — obsoleto vai para arquivo, não é apagado); MAN-001 §6 / RCH-001 (mecanismo de Hygiene); RULE-HD-04 (referência por ID+versão); 4Es (CEE-001 §12); EUA-E16/RPSA (mover caminhos = escopo de agente → agent-sync) |
| Princípio-guia | **Root enxuto = busca eficiente.** Separar o **caminho-quente** (o que os agentes leem sempre) do **acervo de consulta** (referências externas, atas, emendas) e do **arquivo** (obsoletos). Nada é deletado (INV-07); o que sai de circulação vai para pasta de arquivo com ponteiro no CATALOGO. |

---

## 1. Objetivo `[INFERÊNCIA]`

Hoje a **raiz** acumula ~22 `.md/.MD`, dos quais **16 são referências externas não-normativas** (12 `CAMADA *.MD` + 4 Master Contracts) que os agentes **raramente** leem no fluxo de Spec — só sob demanda em auditoria/incorporação. Isso polui exatamente o lugar onde o agente procura `roadmap.md`/`atomic-spec.md`. A `governance/` cresceu para ~55 arquivos misturando **normas vivas**, **atas (DHR)** e **emendas (EUA)**.

**Meta (4Es aplicados à busca dos agentes):**
- **Eficácia** — o agente encontra o documento **certo** (a norma viva, não uma referência-externa parecida: ex.: não confundir `CAMADA METACOGNIÇÃO.MD`/MC-001 com a norma RULE-MET).
- **Efetividade** — encontra **a tempo**: caminho-quente em `raiz`/`governance` raiz; acervo em subpastas.
- **Eficiência** — **menos itens** a varrer por busca (raiz enxuta; governance foldered).
- **Economicidade** — **menos custo/tokens** por busca: um único índice (CATALOGO) + taxonomia previsível.

---

## 2. Taxonomia-alvo `[PROPOSTA]`

```
/ (RAIZ — só caminho-quente)
  AGENTS.md · atomic-spec.md · ROADMAP.md · GLOSSARIO.md · README.md · LICENSE · (configs)

governance/ (NORMAS VIVAS + índice)
  CONSTITUTION · RULES · GPR-001 · PAP-001 · SES-001 · MAN-001 ·
  CONFLICT-MAP · CATALOGO-OFICIAL · CIC-001 · RCH-001
  governance/emendas/   ← EUA-E04..E16 (propostas homologadas)  [ponte até v1.5]
  governance/atas/      ← DHR-*  (trilha de auditoria — INV-07)
  governance/partida/   ← PP-PAP-001 · PE-PR-PAP-001  (pacote de partida/prompts)

backlog/ (RMR-001)
canon/  (CEM/CHM/CCM… · GMC/SAS/CEE/PPQ/SDD/CR — modelos canônicos)
specs/ · rag/ · schemas/ · scripts/   (inalterados)

reference/ (NÃO-NORMATIVO — consulta sob demanda)
  reference/camadas/    ← as 12 CAMADA *.MD + os 4 MC-*.md (referências externas classificadas)
  reference/externo/    ← MANUAL_UNIVERSAL… · GEH-001 (guias de fundo)

docs/ (já organizado)
  docs/_legacy/   ← ARQUIVO (obsoleto/superado — INV-07, nunca deletado)
  docs/arranque/  · docs/fundamentos/  (fontes de origem: ENGENHARIA-GERAL, ARIA, KERNEL)
```

---

## 3. Classificação dos documentos (por categoria) `[PROPOSTA]`

| Categoria | Documentos | Destino | Risco de referência |
|---|---|---|---|
| **Caminho-quente (raiz)** | AGENTS, atomic-spec, ROADMAP, GLOSSARIO, README | **fica na raiz** | — |
| **Normas vivas (governance raiz)** | CONSTITUTION, RULES, GPR-001, PAP-001, SES-001, MAN-001, CONFLICT-MAP, CATALOGO, CIC-001, RCH-001 | **fica em governance/** | — |
| **Emendas homologadas** | EUA-E04..E16 (13) | `governance/emendas/` | **Alto** — citadas por caminho em CATALOGO, DHR, MAN-001 |
| **Atas** | DHR-* (25) | `governance/atas/` | Médio — citadas entre si e no CATALOGO |
| **Pacote de partida** | PP-PAP-001, PE-PR-PAP-001 | `governance/partida/` | Baixo |
| **Referências externas (camadas)** | 12× `CAMADA *.MD` + MC-COG-001 + MC-RAG-001 + CAMADA MEMÓRIA(MC-EXP) + CAMADA GOVERNANÇA(MC-GOV) | `reference/camadas/` | **Alto** — CATALOGO/CONFLICT-MAP/EUA-Exx citam "`CAMADA X.MD`, raiz" |
| **Referências externas (fundo)** | `MANUAL_UNIVERSAL…(1).md`, `RETOMADA/GEH-001…` | `reference/externo/` | Médio — GEH-001 citado em MAN-001/memória |
| **Fontes de origem** | docs/fundamentos/* (ENGENHARIA-GERAL, ARIA, KERNEL) | **fica** (já ok) | — |
| **Arquivo/obsoleto** | docs/_legacy/* (já lá); triar `MANUAL_UNIVERSAL(1)` (o "(1)" sugere cópia de download) | `docs/_legacy/` se superado | — |
| **PENDENTE DE TRIAGEM** | **`CAMADA APRENDIZADO.MD`** (camada de Learning — recém-chegada, NÃO auditada) | manter na raiz até triagem; depois `reference/camadas/` | — |

---

## 4. Regra de movimentação (INV-07 + reparo de referências) `[PROPOSTA]`

**Toda movimentação obedece:**
1. **Nada é deletado** (INV-07). Obsoleto/superado → `docs/_legacy/` (arquivo), não removido.
2. **Reparo de referências obrigatório e determinístico:** para cada arquivo movido, `grep` do caminho/nome antigo em todo o repo → atualizar cada ocorrência para o novo caminho. Nenhuma movimentação fecha sem o grep de verificação retornar zero referências pendentes ao caminho antigo.
3. **CATALOGO-OFICIAL vira o índice único** ("mapa de onde encontrar o quê") — ganha uma seção **"Mapa de Pastas"** no topo, para o agente resolver localização em uma leitura.
4. **Referência por ID+versão (RULE-HD-04)** permanece a forma canônica de citar; o caminho é secundário e reparável.
5. **Impacto em agentes (EUA-E16/RPSA):** mover caminhos toca a **lista de leitura obrigatória** dos agentes (escopo §4.1) → dispara **agent-sync** (carimbo `sincronizado-até`).

---

## 5. Fases de execução (proporcional — maior valor / menor risco primeiro) `[PROPOSTA]`

| Fase | Ação | Valor | Risco | Reparo |
|---|---|---|---|---|
| **F1** | Root → `reference/camadas/`: mover as 16 referências externas (12 CAMADA + 4 MC) | **Alto** (root enxuto) | Médio | CATALOGO + CONFLICT-MAP + campo "Origem" das EUA-Exx |
| **F2** | `governance/emendas/` (EUA-E04..E16) + `governance/atas/` (DHR-*) + `governance/partida/` | Alto (governance legível) | Alto | CATALOGO + refs cruzadas entre atas/emendas |
| **F3** | `reference/externo/`: MANUAL_UNIVERSAL, GEH-001 (de RETOMADA/) | Médio | Médio | MAN-001, memória |
| **F4** | Triagem de `MANUAL_UNIVERSAL(1)` e de `CAMADA APRENDIZADO.MD` (esta via backlog, como as outras camadas) | Médio | Baixo | — |
| **F5** | CATALOGO ganha "Mapa de Pastas"; varredura final de referências (grep zero-pendências) | Alto (findability) | — | — |

Cada fase é um **passo do ciclo de Hygiene (RCH-001)** com Plan/Do/Check/Act e disposições ancoradas em `arquivo:§`.

---

## 6. Governança da operação `[PROPOSTA]`

- **Execução = Ciclo de Hygiene #2 (RCH-001)**, conduzido pelo Controlador sob supervisão do Revisor (Check), homologação de Andraus para o plano.
- **Não altera conteúdo normativo** — só localização + índice. Nenhuma norma é reescrita (INV-09).
- **CAMADA APRENDIZADO.MD**: entra no backlog (RMR-001) para triagem por auditoria como as demais camadas (BL-014 candidato), antes de ser movida.
- Ao final: **carimbo de agent-sync** atualizado (EUA-E16), pois a lista de leitura muda de caminho.

---

## 6-bis. Regra Permanente de Intake e Higiene da Raiz (RPIR) — a garantia `[PROPOSTA]`

Extensão permanente do HOD-001 (paralela à RPSA da EUA-E16). Torna a raiz uma **zona de intake que é sempre drenada**.

### 6b.1 Raiz = zona de intake, não de repouso
A raiz só **repousa** o **whitelist de caminho-quente** (explícito — A-01):
- **Docs:** `AGENTS.md · atomic-spec.md · ROADMAP.md · GLOSSARIO.md · README.md · LICENSE · WORKFLOW.md · HANDOFF.md` *(WORKFLOW.md acrescido por decisão de Andraus, 2026-10-01 — emenda de whitelist; registrar em DHR. HANDOFF.md acrescido por decisão de Andraus, 2026-10-17 — DHR-PCC-001)*
- **Config (por extensão/nome):** `package.json · package-lock.json · tsconfig.json · .eslintrc.json · .prettierrc · .gitignore · .pre-commit-config.yaml` e dotfiles/dotdirs de tooling (`.claude/`, `.github/`, `.agents/`, `.clinerules/`, `.harness-eval/`)

Qualquer outro `.md/.MD` na raiz é um **intake não-tratado** (transitório). A regra de whitelist incide sobre documentos (`.md/.MD`); arquivos de config e dotfiles ficam fora do escopo de intake.

### 6b.2 Estados terminais de um doc de intake (após "tratamento")
"Tratado" = passou por triagem/auditoria (uma DHR, admissão em backlog, ou parecer). Após o tratamento, o doc tem **exatamente um** destino terminal — **nunca permanece solto na raiz**:

| Resultado do tratamento | Destino terminal |
|---|---|
| **Incorporado** (normativo, ref. externa, canônico, emenda, ata…) | **arquivado na pasta respectiva** conforme a taxonomia §2 (com reparo de referências §4) |
| **Não incorporado** (rejeitado, superado, duplicado, fora de escopo) | **excluído da circulação** — ver 6b.3 |

### 6b.3 "Excluir" conciliado com INV-07
- **Padrão = exclusão lógica (arquivamento):** doc não incorporado vai para `docs/_legacy/` com nota de motivo. Sai de circulação, **mas não é deletado** (INV-07 preservado; história auditável).
- **Exclusão física (delete real):** permitida **apenas** para **duplicata exata confirmada** (ex.: `arquivo (1).md` idêntico ao `arquivo.md`) ou lixo sem qualquer valor normativo/histórico, e **somente com autorização explícita de Andraus, item a item**. Nunca automática.
> Assim atende-se "excluídos quando não incorporados" sem violar o INV-07: o default é arquivar; o delete físico é exceção autorizada e restrita a duplicata/lixo.

### 6b.4 Garantia tripla (reusa maquinário homologado)
1. **Gate de intake (efeito do Controlador):** toda DHR/admissão/parecer que **trata** um doc de raiz DEVE, nos "Efeitos de registro", **arquivar-o na pasta** ou **excluí-lo** (6b.3). Um doc **tratado mas ainda solto na raiz** = **achado de gate**.
2. **Item de intake no RMR-001:** um doc **novo e não-tratado** na raiz abre item **ATIVADO** (gatilho `hygiene:próximo ciclo`, ação "triar → arquivar/excluir") — surface para não ser esquecido.
3. **Sensor no Hygiene (RCH-001 — passo 8):**
```
8. higiene da raiz (HOD-001/RPIR): conferir que a raiz contém SOMENTE o whitelist de caminho-quente
   (6b.1). Qualquer doc fora do whitelist → FLAG no RCH-001 + item no CIC-001:
     - se não-tratado  → abrir item de intake no RMR-001 (triar);
     - se tratado      → violação de higiene: arquivar na pasta respectiva ou excluir (6b.3).
```

### 6b.5 Detecção determinística
Whitelist explícito de raiz (6b.1) = teste determinístico: `ls raiz \ whitelist ≠ ∅` → há intake pendente ou violação. Sem julgamento subjetivo.


- Não deleta nada por padrão (INV-07); obsoleto/não-incorporado = **arquivado** em `docs/_legacy/`. Delete físico só para **duplicata exata/lixo confirmado, com autorização item-a-item de Andraus** (6b.3) — nunca automático.
- Não reescreve norma (INV-09); só move e indexa.
- Não reclassifica o status normativo de nenhum doc (ref. externa continua ref. externa).
- Não move `specs/`, `rag/`, `schemas/`, `scripts/`, `canon/`, `docs/fundamentos/` (já bem organizados).

---

## 8. `[DECISÃO NECESSÁRIA]` — Andraus

| # | Questão | Recomendação |
|---|---|---|
| Q1 | Aprovar a **taxonomia-alvo** (§2) | **Sim** |
| Q2 | Executar F1 (root → `reference/camadas/`) — maior ganho de findability | **Sim** |
| Q3 | Executar F2 (`governance/emendas/` + `atas/` + `partida/`) | **Sim** |
| Q4 | Regra de reparo de referências (grep zero-pendências) + CATALOGO como "Mapa de Pastas" | **Sim** |
| Q5 | Executar como **Ciclo de Hygiene #2 (RCH-001)**, com agent-sync (EUA-E16) ao final | **Sim** |
| Q6 | `CAMADA APRENDIZADO.MD` → backlog (BL-014) para triagem antes de mover | **Sim** |
| **Q7** | Instituir a **RPIR** (§6-bis): raiz = zona de intake; todo doc tratado → pasta respectiva ou excluído (arquivar por padrão; delete físico só duplicata/lixo com autorização); garantia tripla (gate Controlador + item RMR-001 + sensor Hygiene passo 8) | **Sim** |

---

## 9. Fluxo de autoridade

```
[feito] Especificador redige o Plano (este)
   ↓
Revisor emite parecer (CONFORME / NÃO CONFORME) contra INV-07/09, RCH-001, MAN-001 §6, EUA-E16/RPSA, 4Es
   ↓
Andraus homologa (decide Q1–Q6)
   ↓
Controlador executa como Ciclo de Hygiene #2 (RCH-001): F1..F5, com reparo de referências (grep zero-pendências) + agent-sync
```

---

## Anexo A — Autopré-check do Especificador (2026-09-21)

- [x] TRACE-06; status = PROPOSTA (CONS-01).
- [x] INV-07 respeitado (obsoleto arquivado, nunca deletado); INV-09 (não reescreve norma).
- [x] Reparo de referências determinístico (grep zero-pendências) — evita links quebrados.
- [x] 4Es aplicados à findability dos agentes (root enxuto; índice único).
- [x] Reusa RCH-001 (Hygiene) e EUA-E16/RPSA (agent-sync) — sem maquinário novo.
- [x] `CAMADA APRENDIZADO.MD` (recém-chegada, não auditada) surfaced para triagem (honestidade — RULE-MET-01).
- [x] Inventário real conferido (raiz, governance, docs, canon, schemas, rag, scripts, RETOMADA).
- [x] RPIR (§6-bis) concilia "excluídos quando não incorporados" com INV-07: arquivar por padrão; delete físico só duplicata/lixo com autorização item-a-item. Garantia tripla reusa gate/RMR/Hygiene.
- [x] Whitelist de raiz = detecção determinística de intake pendente/violação.

## Anexo B — Parecer do Revisor SOT (2026-09-21)

**Veredito: CONFORME** — 1 achado Menor (A-01, acatado). Acesso ao `RULES.md` v1.1 confirmado (M-02).

**Baselines auditados:** RULES.md v1.1 · RCH-001 (Ciclo #1 fechado) · MAN-001 §6 · RMR-001 §4 · EUA-E16 (RPSA, tie-in) · CATALOGO-OFICIAL · atomic-spec v1.4 (INV-07/09, 4Es) · inventário real (raiz ~22 .md; governance ~55).

**Verificações-chave:** (1) INV-07×"excluir" — conciliação segura: arquivar por padrão em docs/_legacy; delete físico só duplicata/lixo com autorização item-a-item (PC-08 intacto); nunca automático — PASS; (2) **reparo de referências — grep confirmou 48 ocorrências de `CAMADA*.MD` em 20 arquivos + 24 de `governance/EUA-E` em 13 arquivos**; a regra "grep zero-pendências" é necessária e suficiente; F2 corretamente sinalizado como alto risco — PASS; (3) RPIR garantia tripla sem furo (doc nunca-tratado coberto por sensor Hygiene passo 8 + item RMR ATIVADO) — PASS; (4) reusa RMR-001 §4/RCH-001/efeitos do Controlador, PC-08 intacto, sem autoridade nova — PASS; (5) taxonomia melhora findability/4Es, nenhuma norma viva movida para acervo frio — PASS; (6) fases proporcionais — PASS; (7) CAMADA APRENDIZADO.MD e MANUAL(1) não movidos às cegas (BL-014/triagem) — PASS; (8) INV-09 (não reescreve norma) — PASS; (9) non-goals/Q1–Q7 coerentes — PASS.

**Achado:**

| ID | Severidade | Constatação | Tratamento |
|---|---|---|---|
| A-01 | Menor | Whitelist §6b.1 usava "(configs)" genérico | **ACATADO** — §6b.1 explicita docs + config por extensão/nome + dotfiles fora de escopo. |

Nenhum achado Crítico ou Médio.

**Recomendação (Q1–Q7):** Sim para todas (Q7/RPIR: garantia tripla suficiente, reusa maquinário homologado, PC-08 preservado, INV-07 respeitado). **Encaminhamento:** CONFORME → homologação de Andraus. O parecer não homologa; atesta integridade.
