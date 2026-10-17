# Avaliação dos mecanismos (regras, guardrails, hooks, policy, determinísticos) para elevar a maturidade do Revisor SOT

> **Não-normativa.** Relatório do Orquestrador (2026-10-17) a pedido de Andraus ("elevar necessariamente para nível máximo; avalie uso de rules, guardrails, hooks, policy e mecanismos determinísticos"). Não homologa, não fecha decisão aberta (CONS-01), não atribui nível oficial (RULE-MM-02). Sequência de `AUDITORIA-REVISOR-MATURIDADE-2026-10-17.md`.

## 1. Resposta curta
**Nível indicativo agora: L3 (Testável) em substância, ainda não declarável em forma; L4 (Expert) não é alcançável sem a aprovação registrada de Andraus e sem medição contínua.** O que se construiu sobe a eficácia e fecha as lacunas mensuráveis; os dois critérios que faltam para L3 formal e os dois para L4 estão na §5. Eu não me concedo nível: quem atribui é o gate determinístico e Andraus (RULE-MM-02/MM-05).

## 2. O que foi medido (Spec real SPEC-021 com 14 defeitos sutis plantados por outro agente, 9 rodadas)
| Condição | Defeitos achados por rodada (de 14) | Média | União das 3 rodadas |
|---|---|---|---|
| Revisor sozinho (rodada 1) | 5 · 6 · 9 | 6,7 (48%) | 9 |
| Revisor sozinho (réplica) | 7 · 9 · 7 | 7,7 (55%) | 9 |
| **Revisor + guarda (G1+G2+G3)**, mensagem do hook entregue ao Revisor | 10 · 11 · 8 | **9,7 (69%)** | **11 (79%)** |
- O ganho atribuível à guarda são **2 defeitos que nenhuma das 6 rodadas sem guarda achou, e que as 3 com guarda acharam**: fronteira errada com Spec vizinha (SPEC-024 no lugar da SPEC-041) e DHR errada de item de backlog. Vieram do gate injetado (G2), são determinísticos. O resto da diferença está dentro do ruído de réplica. Além disso, com G1 o Revisor abriu as 4 fontes do núcleo do Passo 0 (antes: 1 de 4) e achou um defeito real que ninguém tinha visto (BL-020 desatualizado no painel).
- **Gate de código sozinho na mesma Spec:** 0/14 antes → **6/14** agora (valor, ID inexistente, contagem, mapeamento contraditório, nome de Spec, DHR de backlog) e **9/14** quando há versão anterior para comparar (referência removida, fonte trocada, pendência marcada como feita).
- **Calibração:** nos 10 Plans homologados os detectores novos dão **1 achado, genuíno** (SPEC-003 declara 10 critérios EARS e lista 11).
- Nunca achados em 9 rodadas: atribuição falsa a baseline com fonte fora do alcance (D4, 0/9), obrigação normativa removida em silêncio (D14, 0/9), obrigação não representável no schema (D12, 1/9). D4 e D14 só caem com **diff contra a versão anterior** (existe no gate; não houve versão anterior neste desenho de teste).
- Interpelação com provas falsas (teste anterior): 6/6.

## 3. Avaliação por tipo de mecanismo
| Mecanismo | O que impõe | Evidência neste repositório | Limite / risco | Veredito |
|---|---|---|---|---|
| **Detectores determinísticos (Classe D)** | Forma, valor, existência, contradição interna | 7 novos + diff; 62+ testes; calibrados em 10 Plans; mutação por detector | Só acham o que é objetivo; sentido continua do Revisor (ENF-03) | **Alto ganho, baixo custo. Fazer sempre** |
| **Hook SubagentStop (guarda do Revisor)** | O código confere o fim do Revisor: fontes do Passo 0 abertas, gate rodado pelo harness, citações existentes; 1 retorno forçado | `revisor_guard.py` + 13 testes; efeito medido (§2) | **Hooks são lidos na abertura da sessão: precisa reiniciar para valer.** Fail-open por padrão (hook que quebra não bloqueia); `onFailure:"block"` existe só a partir do Claude Code 2.1.295 e não foi ligado. Cobre FORMA/EXISTÊNCIA, não o mérito de cada achado | **Maior alavanca isolada. Ligar e confirmar ao vivo** |
| **Guardrail de ferramenta (`tools` somente leitura)** | Revisor e auditores não escrevem nem executam | Já em vigor; teste falha se algum agente de revisão tiver Bash/Write | `mcpServers` declarado em `.claude/agents/` é ignorado em pasta não confiável (causa provável de o gate MCP não carregar em nuvem) | Manter. A guarda do hook **contorna** o problema (o harness roda o gate) |
| **Selo de integridade + CODEOWNERS** | Detecta adulteração dos scripts do gate | `GATE-MANIFEST.sha256` + passo de CI + recusa do servidor | Detecta, não impede; CODEOWNERS só bloqueia se a `main` exigir (decisão de Andraus: manter só o selo) | Manter |
| **Regras (RULE-REV-xx) / policy escrita** | Torna obrigatório por norma o que hoje é prompt: ex. "Passo 0 só vale com as 4 fontes abertas", "parecer inclui VEREDITO D do harness" | Nenhuma criada | Mudança em norma e em `revisor.md` exige ata + RPSA + decisão de Andraus; regra sem verificador é só texto | **Propor** (§6, item 3); só tem força junto com a guarda |
| **Policy de modelo/esforço (pin)** | Revisor em `claude-sonnet-5-5` | Já em vigor (DHR-AUDITOR-EXTERNO-014) | Mesma família do Especificador: pontos cegos correlacionados | Manter; complementar com revisão de outra família (Auditor Externo) em CRITICAL |
| **k passes + união** | Sobe o recall (+24 p.p. em medição anterior) | Medido | 3× tokens; não resolve o que o Revisor não consegue conferir | Opcional, para CRITICAL |
| **CI bloqueante** | Testes, selo, detectores | `ci.yml` | Não roda modelo (custo/segredo): a medição do Revisor segue manual | Manter; medição do Revisor fica fora do CI |

## 4. Descobertas que mudam a conduta
1. **A causa provável de o gate MCP não carregar em nuvem é conhecida** (servidor inline em `.claude/agents/` não carrega em pasta não confiável). Corrigir exigiria mexer no frontmatter do `revisor.md` (ata + RPSA). A guarda por hook torna isso **desnecessário para ter o gate no parecer**.
2. **Todos os Revisores abriram a cópia homologada da SPEC-021 do repositório** como referência (vazamento do desenho do teste) e, numa rodada, o próprio relatório de maturidade no repositório (continha "ENF-09"). Os números são **teto** para defeitos detectáveis por comparação. Medições futuras precisam de Spec que não exista no repositório.
3. O hook é **detector de forma**: um Revisor pode cumpri-lo e ainda errar o mérito. Nenhuma guarda substitui a defesa em profundidade (Revisor → Andraus).

## 5. O que falta para cada nível (RULE-MM-03: staged, fail-closed)
**L3 formal (Testável) — falta:**
1. **Prova ao vivo de que o hook dispara** (reiniciar a sessão; rodar um Revisor; ver o retorno forçado no transcript). Hoje o efeito foi medido por entrega equivalente da mensagem, **não** pelo hook ligado.
2. **Revisão independente de outra família** (Auditor Externo reativado em uma Spec CRITICAL) e/ou defeitos escritos por Andraus. Sem isso o critério "revisão independente" do L3 fica parcial.
3. (Opcional, recomendado) meta de recall definida por Andraus (hoje: 69% por rodada, 79% na união, em Spec que vaza).

**L4 (Expert) — falta, e não é do Orquestrador:**
1. **Aprovação registrada de Andraus** (atomic-spec §7: "aprovação registrada").
2. **Medição contínua/automática** (backtest de comportamento): regressão do Revisor a cada mudança, com defeitos escritos por Andraus. Precisa de agendamento com modelo (custo, segredo/ambiente) — decisão de Andraus; não cabe no CI sem chamadas de modelo.

## 6. Próximos passos propostos (nenhum aplicado além do já commitado)
1. Reiniciar a sessão e confirmar o hook ao vivo (§5 L3.1).
2. Ligar `onFailure:"block"` no hook se a versão do Claude Code ≥ 2.1.295 (passa a fail-closed).
3. Ata de política: `RULE-REV-01..03` (parecer com VEREDITO D do harness; núcleo do Passo 0 aberto; citação verificada) + emenda do `revisor.md` — **decisão de Andraus**.
4. Reativar o Auditor Externo numa Spec CRITICAL e/ou Andraus escrever 3–5 defeitos (L3.2).
5. Erratum da SPEC-003 (10 × 11 critérios EARS) — baseline, só Andraus (INV-07).

## 7. Teste de revisão independente de outro modelo (critério L3) — SPEC-006 Plan v1.3, 2026-10-17
**Desenho.** O mesmo Plan candidato (SPEC-006 v1.3, ramo `spec006-plan`, fora da `main`; 1428 linhas) foi auditado por (a) outro modelo LLM de outra empresa, **sem acesso ao repositório**, com prompt de rigor adversarial e saída em JSON (Andraus executou), e (b) o Revisor interno (`claude-sonnet-5-5`), 2 rodadas, **com** acesso ao repositório. Os achados foram conferidos por mim contra o texto real.

| | Outro modelo (sem repositório) | Revisor interno (2 rodadas, com repositório) |
|---|---|---|
| Achados | 6 (2 críticos, 4 médios) | 1 crítico + 9 médios (1ª rodada); 1 crítico + 10 médios + 10 menores (2ª) — grande sobreposição entre as duas |
| Procedem ao conferir no texto | **0 críticos procedem.** Os 2 críticos (K-01/F-01) são **leitura errada**: o T01 é o cenário **negativo** que usa `school=ICT` para provar que o gate rejeita (plan.md:872 "Violação de integridade → rejeição"); 3 médios apontam lacunas **declaradas** como INDETERMINADO/gap aberto; 1 média coincide com o defeito real da herança | **Todos os que conferi procedem** (≥10 verificados no texto: D6 exige `gate_record` incondicional contra CKG-005; campo `ref` ausente do schema; `PENDING_ANCESTOR` fora do D5 apesar de "resolvido"; `COL-EXP` só em 1 linha; `REFUTED` inexistente no CEM-001; `school` sem origem canônica e Fractal ausente da enumeração; etc.) |
| Defeito real principal (herança "preservar todos os estados" × admissão INDETERMINADA × CEM-001:494) | achou como **média** (M-01) | achou como **crítico** nas 2 rodadas |
| Defeitos reais que só um achou | 0 | ≥9 |

**Leitura.**
1. **Não há evidência de ponto cego do Revisor interno nesta Spec:** o outro modelo não achou nenhum defeito real que o Revisor interno tenha perdido (o único real que achou, o Revisor achou com severidade maior).
2. **A independência sem acesso ao repositório tem baixo valor e custo de ruído:** sem poder abrir CEM-001, SPEC-001, RULES ou o RMR-001, o modelo externo não confere atribuições nem estados e **erra por leitura** (2 críticos falsos). Para a "revisão independente" do L3 ser útil, o auditor de outra família precisa de **acesso somente leitura ao repositório** (como o desenho do Auditor Externo / Codex em `governance/propostas/AUDITOR-EXTERNO/`), não só do texto.
3. Reforça a regra de uso do JSON externo: **achado de outro modelo é dado a verificar** (DIR-002), nunca veredito. Aqui 2 de 6 eram falsos e 3 de 6 eram lacunas já declaradas.
4. **Limites:** uma Spec, um modelo externo, uma execução; severidades não comparáveis; o Revisor interno também rodou sem o gate (hook não ativo na sessão) e sem diff de versão anterior.

**Consequência para o L3 formal:** o teste cumpre "revisão por outra família" **no formato texto-só**, e o resultado é *consistente* com o Revisor interno (sem divergência real), mas **não** valida o Revisor contra um auditor com repositório. Para fechar a lacuna: Auditor Externo reativado em Spec CRITICAL, ou defeitos escritos por Andraus.

### 7.1 Segundo modelo externo (mesmo pedido, outra execução, também sem repositório)
4 achados (3 críticos, 1 médio); **todas as citações literais conferem** com o texto e **nenhum é falso**, ao contrário do primeiro modelo externo.
| Achado do 2º modelo | Situação ao conferir | Equivalente no Revisor interno |
|---|---|---|
| H-01 (crítico) EC-CKG-004 em E2 sobre a escrita permanente do KG | **Procede** (plan.md:1201; o guard de INV-04 fica abaixo do piso E3 da escrita). A linha que ele cita como contraste (1165) é de **outro** EC (EC-CKG-001), mas a tese é a mesma | F-07 / A-10 (**média**) — o externo inflou a severidade |
| H-02 (crítico) EC-CKG-001 admite o caminho canônico enquanto CKG-010(a) é INDETERMINADO | **Procede** (plan.md:1162 × 711) | F-02 / A-01 |
| H-03 (crítico) evidência depende de amostragem ENF-07 sem limiar | Lacuna **já declarada** pelo autor (plan.md:1166); procede só como "não declare E3 pleno" | m-03 (menor) |
| H-04 (médio) validadores não executados | **Declarado** pelo autor (plan.md:1401); não é defeito do Plan | Passo 3 (gate não verificado) |
**Resultado agregado dos dois externos:** 10 achados; 2 falsos (ambos do 1º modelo), 4 que apenas repetem lacunas já declaradas, 4 reais — **todos os 4 reais já estavam no Revisor interno**, com severidade igual ou maior (exceto a inflação do H-01/H-02 do 2º). **Defeitos reais achados só por um externo: 0.** Defeitos reais achados só pelo Revisor interno: ≥ 9 (D6 `gate_record`, schema sem `ref`/`valid_to` de nó, `PENDING_ANCESTOR`, `REFUTED` inexistente no CEM-001, `school` sem origem canônica, COL-EXP, SIMILAR_A sem gate, etc.).
**Conclusão sobre o L3:** em duas tentativas com modelos de outra família e **sem** repositório, a revisão independente **não encontrou ponto cego** do Revisor interno nesta Spec, e rendeu menos que ele (recall ≈ 1/3 dos reais, precisão 4/10 a 4/6 conforme o modelo). Isso **não** prova que o Revisor interno seja suficiente (a lacuna é a ausência de auditor independente **com acesso ao repositório**), mas **reduz** a probabilidade de um defeito material sistemático passando despercebido por correlação de família.
