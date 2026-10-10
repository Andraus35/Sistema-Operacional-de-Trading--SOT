# DHR-RPSA-002 — Ata — Classificação RPSA automática após a aprovação de Andraus

| Campo | Valor |
|---|---|
| De | Orquestrador interno (registro) — decisão de Andraus — Decisor Final / Consensus Authority |
| Para | Orquestrador interno / Especificador SOT / Revisor SOT |
| Data | 2026-10-10 |
| Status | **Decisão de Andraus registrada (chat, 2026-10-10: "Classificação RPSA precisa ser automatizada após minha homologação e/ou aprovação")**. O merge desta ata por Andraus é a ratificação do mecanismo e da classificação abaixo. Não altera checklist, método, regra, o Revisor nem decisão aberta. |
| Compatibilidade | n/a (aditiva — INV-07; as entradas existentes do livro-razão não são reescritas) |
| RPSA-escopo | nao |
| RPSA-sync | fonte-unica |
| RPSA-motivo | Muda o procedimento de manutencao do livro-razao RPSA (classificacao declarada na ata e registrada por codigo apos o merge); nao altera checklist embutido, metodo nem regra dos agentes. |

## 1. Decisão de Andraus `[FATO: chat, 2026-10-10]`
A classificação RPSA de cada DHR nova (EUA-E16 §4.1/§4.3) não deve mais depender de uma inferência do Orquestrador "a ratificar" numa rodada manual extra: ela deve ser **registrada automaticamente depois da homologação/aprovação de Andraus**.

## 2. Desenho `[INFERÊNCIA do orquestrador — a ratificar por Andraus no merge desta ata]`
- **A ata declara** a classificação em três linhas da tabela de cabeçalho: `RPSA-escopo` (`sim`/`nao`), `RPSA-sync` (`fonte-unica`/`propagado`/`pendente`) e `RPSA-motivo` (≥ 20 caracteres). O julgamento de escopo continua humano e fica **na ata**; o **merge de Andraus é a ratificação**.
- Após o merge no `main`, o workflow `rpsa-auto.yml` roda `scripts/rpsa_auto.py`: lê a declaração, valida a forma, **barra contradições óbvias** com os arquivos do próprio merge e registra no `governance/rpsa-ledger.json` (append-only) alinhando os carimbos dos agentes. Idempotente; ordem cronológica.
- **Contradições barradas** (fail-closed, nada é registrado e abre-se uma Issue para humano): C1 `escopo=nao` mas o merge alterou `atomic-spec.md`, `governance/RULES.md` ou `governance/CONSTITUTION.md`; C2 `sync=propagado` sem alteração em `.claude/agents/*.md`; C3 `escopo=nao` mas o merge alterou `.claude/agents/*.md`. Ata sem declaração ou com declaração inválida também **não** é registrada (continua "NÃO CLASSIFICADA" — R2 do `check_rpsa.py`).
- `sync=pendente` é registrado, e o **gate §4.5 continua valendo** (R3: a próxima Spec não inicia com Agent-Sync pendente). A automação nunca propaga texto aos agentes.
- **Inerte por padrão:** só funciona com a variável de repositório `RPSA_AUTO_ENABLED = true` (ato de Andraus; apagar ou pôr `false` desliga). O commit do bot afeta apenas o livro-razão e as linhas de carimbo dos agentes (conferido antes do commit).
- Atas **anteriores** a esta continuam classificadas como hoje; a ratificação das atas 002–005 do Auditor Externo permanece nas atas 004/005. A partir desta ata, **toda ata nova deve trazer as três linhas `RPSA-*`**.

## 3. Limites `[FATO/INFERÊNCIA]`
O código **não decide** se uma mudança toca o escopo dos agentes: itens como "fluxo ou piloto" ou "decisões abertas" (§4.1) não se reconhecem por caminho de arquivo, por isso a declaração é da ata. Um erro de julgamento **consistente** (declaração errada sem contradição de caminho) passa pelo código e só é pego por Andraus/Revisor na leitura da ata. O workflow ainda **não foi exercitado ao vivo** (depende de `RPSA_AUTO_ENABLED`). Push do bot ao `main` pode ser recusado se houver proteção de branch (então vira falha visível, sem efeito silencioso).

## 4. Classificação RPSA desta ata
Declarada acima (`nao` / `fonte-unica`): muda o procedimento de manutenção do livro-razão, não o checklist embutido nem o método. **Caso limítrofe**: se Andraus entender que mudar o fluxo do gate RPSA é "fluxo" do §4.1, a classificação deve ser `sim` — nesse caso o carimbo dos agentes avança para `DHR-RPSA-002` (decisão dele; não bloqueia o resto).

## 5. Permanecem ABERTAS (CONS-01)
M-001 · J-001 · N-001 · H-001 · G-001 · K-001 · C-001 · WF-D03 (residual) · ECC-03-001 · SPEC-038-DATASRC-001 (provedor de máquina) · SPEC-045-RUNTIME-001 · pendência herdada do tipo de hipótese por especialista (SPEC-010/011/012). **Nenhuma fechada por este ato.** A abertura da SPEC-006 segue **não homologada**.

## 6. Registro
- [x] Esta ata · [x] `scripts/rpsa_auto.py` + `tests/test_rpsa_auto.py` · [x] `.github/workflows/rpsa-auto.yml` (inerte) · [x] CI · [x] `rpsa-ledger.json` · [x] `CATALOGO-OFICIAL.md` · [x] mapa

---

**Andraus** — *decisão direta em chat, 2026-10-10; registro feito pelo Orquestrador interno a pedido de Andraus. Assinatura = merge desta ata.*
