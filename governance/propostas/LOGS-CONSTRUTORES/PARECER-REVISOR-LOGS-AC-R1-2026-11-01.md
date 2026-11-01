# PARECER DO REVISOR — Logs dos Construtores (proposta + pesquisa + plano F2 + F1) — R1 — 2026-11-01

> Transcrição pelo Orquestrador do relatório do Revisor SOT (`CLASSE-TAREFA: S2`, `model: sonnet`). Alvo: `PROPOSTA-LOGS-CONSTRUTORES-2026-11-01.md` (Complexidade MEDIUM, proposta de processo, não Spec). `SHA256-ALVO: 47820379c6917c3f563a2b8279713691e540aa9a489a16fc5e882daea5503440`. `GATE-D: PASSOU_D` (do Orquestrador; forma, não parecer). Revisão integral, 1ª rodada; Passo 0 declarado parcial; testes não reexecutados pelo Revisor (sem Bash). **Veredito: NÃO CONFORME** (nenhum Crítico; Médios A01–A10 voltam ao Especificador, classe O). Nada homologado; nenhuma decisão aberta fechada (CONS-01).
> **Conferido pelo Orquestrador no código:** A01 (a chamada de log ficaria dentro do `try` de `hook()`; `except Exception: return 0` acontece antes do `deny`) e A02 (`.claude/settings.json` registra `"timeout": 15` para o roteador; o plano citava 110 s do wrapper) — **confirmados**.

## Resumo dos achados
| ID | SEV | Tema |
|---|---|---|
| A01 | MÉDIA | Fail-open do plano F2 só cobre `OSError`; exceção de `log_ac` faria um DENY virar ALLOW. |
| A02 | MÉDIA | Timeout real do hook = 15 s (não 110 s); `acrescenta` lê o arquivo inteiro (O(n)); estouro de tempo é fail-open. |
| A03 | MÉDIA | Cadeia de hash sem lock/append atômico; L3 em cadeia única conflita entre ramos; truncamento do fim/cabeça não detectado; âncora git só prometida. |
| A04 | MÉDIA | Varredor de segredos: não varre chaves de `metrics`; `path` e campos sem limite; padrões ausentes; falso positivo descarta o evento de DENY; testes só positivos. |
| A05 | MÉDIA | `session_id` bruto pode ir ao git; ajuste da pesquisa não implementado; `reason` herda motivo livre. |
| A06 | MÉDIA | Plano lista só 2 arquivos selados; manifesto sela também `revisor_guard.py`, `revisor_posguarda.*`, `gate_manifest.py`, `check_*`. |
| A07 | MÉDIA | L2 incoerente: arquivo único × por sessão × lote diário × por linha (proposta/pesquisa/plano). |
| A08 | MÉDIA | Plano desatualizado (pesquisa "em produção", 22 testes); proposta §4.2 usa ALLOW/DENY; §1 cita página OTel esvaziada como oficial. |
| A09 | MÉDIA | Afirmações sem comando/data: "grep em scripts/", 98/233 commits, 157 atas, 131 cópias, A2/A3/A6/A7, contagem dupla. |
| A10 | MÉDIA | `approval.decided` sem emissor; cadeia prova integridade, não autoria; exigir ata citada. |
| A11 | MENOR | Omissões do plano: Stop hook de não-commitado, RPSA/CATALOGO, CI do `--verify`, custo de `agent_version`, reversão sob INV-07. |
| A12 | MENOR | Proposta §4.4 promete WARN em falha de gravação, mas `registrar()` faz `pass`; falta o canal. |
| A13 | MENOR | Regex com `$` aceita `\n` final; chaves de `metrics` sem exigência ASCII. |

**Condição para nova revisão (delta):** plano F2 revisado que (a) isole o log da decisão e teste exceções não-`OSError`, (b) declare orçamento de latência contra 15 s, (c) resolva lock e merge das cadeias (L2 e L3), (d) endureça varredor e esquema, (e) liste todos os arquivos selados afetados, (f) torne coerentes proposta, pesquisa, plano e protótipo, (g) marque "não medido" o que não tiver comando e data.

<!-- ACHADOS-ESTRUTURADOS
A01|MEDIA|C05|log do hook de politica dentro do try/except externo do roteador; excecao do log cai no return 0 e elimina o deny; teste previsto cobre so OSError|isolar a chamada de log em try/except proprio apos fixar a decisao; testar com ValueError/KeyError
A02|MEDIA|C05|plano mede timeout de 110 s; settings.json registra 15 s; estouro de tempo do hook e fail-open; acrescenta le o arquivo inteiro a cada anexo|declarar orcamento de latencia contra 15 s, medir p95, ler so a cauda ou guardar hash-cabeca
A03|MEDIA|C10|encadeamento sem lock gera bifurcacao e falso adulterado; L3 em cadeia unica conflita entre ramos; truncamento do fim e da cabeca nao detectados; ancora git so prometida|lock/append atomico, regra de merge por segmento tambem em L3, ancora do hash-cabeca, declarar limite de autenticidade
A04|MEDIA|C09|varredor so varre valores; chaves de metrics, path e campos sem maxLength passam; padroes ausentes; falso positivo descarta o evento de DENY; testes so positivos|varrer chaves, fechar metrics, limitar campos, ampliar padroes, testes de bypass/falso positivo, fallback de evento minimo
A05|MEDIA|C09|session_id bruto pode ir ao git em L2/L3; ajuste da pesquisa nao implementado nem exigido como teste; reason herda motivo livre|esquema com hash curto de session_id em L2/L3 e teste que falha se bruto; teste com dados reais
A06|MEDIA|C04|plano lista como selados so roteador e revisor-guard.js; manifesto sela tambem revisor_guard.py, revisor_posguarda.*, gate_manifest.py e check_*|tabela arquivo x selado x muda antes da decisao de Andraus
A07|MEDIA|C01|plano linha 14 (arquivo unico) contradiz plano secao 4 (segmentado por sessao) e proposta 4.3/4.5 (unico, lote diario) e pesquisa (por linha)|fixar uma forma de L2 e alinhar proposta, pesquisa, plano e MECANISMOS
A08|MEDIA|C06|plano ainda diz pesquisa em producao e 22 testes; proposta 4.2 usa ALLOW/DENY e 1 cita pagina OTel esvaziada como oficial|atualizar plano e proposta 4.2/1 para o estado atual (26 testes, vocabulario allow/deny/ask/defer, S1 movida)
A09|MEDIA|C06|grep em scripts/ sem cobrir settings.json/gate-check.js; 98/233 commits, 157 atas, 131 copias e A2/A3/A6/A7 sem comando nem data|citar comando e data das medicoes ou marcar nao medido
A10|MEDIA|C05|approval.decided sem emissor de hook; cadeia de hash prova integridade e nao autoria; qualquer agente pode escrever approver=Andraus|declarar limite, exigir ata citada em approval.decided, nao chamar de trilha de auditoria sem ressalva
A11|MENOR|C05|plano omite Stop hook de nao commitado, registro RPSA/CATALOGO, CI do verify, custo de agent_version/harness_version, reversao sob INV-07|completar a lista de mudancas e provas do plano
A12|MENOR|C02|proposta 4.4 diz WARN de falha de gravacao mas registrar() faz pass silencioso e o canal do WARN nao existe|definir canal (stderr nao bloqueante + L1 local)
A13|MENOR|C07|regex com $ aceita newline final em ts/sha256; chaves de metrics sem exigencia ASCII|usar fullmatch e padrao de chave ASCII
-->

<!-- FICHA-M {"achados":[]} -->

## Nota do Orquestrador — guarda pós-revisor (DHR-AUDITOR-EXTERNO-018), 2026-11-01
A guarda acusou G1 e G3 sobre este parecer (o hook do subagente não é honrado em nuvem). Conferência ao vivo:
- **G3 (citações) — falso positivo do parser:** `scripts/andraus-ask-mark.js:30` contém `fs.writeFileSync(file, JSON.stringify(st));`; `scripts/andraus-ask-guard.js:183` contém `fs.writeFileSync(file, JSON.stringify(estado))`; `.claude/settings.json:18-19` contém `"command": "node scripts/roteador-modelos.js"` e `"timeout": 15`. As frases "registra o hook com" e a lista "ask-mark.js:30, ask-guard.js:183" eram prosa do relatório, não trechos literais. Nenhum achado é retirado.
- **G1 (núcleo do Passo 0):** o próprio Revisor declarou o Passo 0 **parcial**. O Orquestrador conferiu o que a proposta usa dessas fontes: `ROADMAP.md` §18 (SPEC-040/041 "Indicativo — não aberta", linhas 365–377 e 546–547), `backlog/RMR-001_Painel_Backlog.md` (BL-034 linha 141; BL-038), `atomic-spec.md` (ENF-03 linhas 95 e 269) e `INV-04` em `atomic-spec.md`/`governance/RULES.md`. Sem divergência. Não foi feita releitura integral do ROADMAP/atomic-spec/RULES; a próxima rodada (delta) deve declarar o escopo do Passo 0.
- Rodar `python scripts/revisor_gate.py` no `plan.md` não se aplica: o alvo é proposta de processo, não Spec (o `GATE-D: PASSOU_D` já foi anotado no pedido).
