# Propostas de boas práticas para o repositório e o projeto — rodada 2 (2026-11-17)

> **PROPOSTAS, NÃO NORMATIVAS.** Respostas de Andraus ao 2º questionário automatizado (AskUserQuestion, 2026-11-17). **Nada é aplicado:** cada item só vira mecanismo por ordem expressa dele, com `governance/MECANISMOS.json` no mesmo PR (COE-14) e ata completa se tocar arquivo selado ou `AGENTS.md`. Continua `PROPOSTAS-REPO-BOAS-PRATICAS-2026-11-17.md` (H1–H3).

## H4 — Proteção da `main` (resposta: "Me dê o script completo para o Termux")
- **Problema:** CODEOWNERS só bloqueia merge se a proteção da branch exigir revisão de Code Owners (configuração do GitHub, fora do repositório); sem isso o selo do gate depende só da disciplina do fluxo.
- **Entrega:** `governance/propostas/MELHORIAS-PROCESSO/termux/proteger_main.sh` — executado por Andraus, não pelo Orquestrador (que não tem acesso a essa configuração). Por padrão só **lê** a proteção atual e mostra o payload; `--aplicar` pede confirmação digitada. Liga: CI obrigatório (`Validate SOT Harness`, branch em dia), PR obrigatório e, com `CODEOWNERS=1`, revisão de Code Owners; mantém `enforce_admins=false`, sem force-push nem exclusão.
- **Risco declarado `[FATO]` do GitHub:** os PRs desta sessão são abertos pela conta `Andraus35`, e o autor não aprova o próprio PR; com Code Owners ligado, PR que toque arquivo selado só mescla por bypass de admin ("Merge without waiting for requirements"). Se isso atrapalhar o fluxo, `CODEOWNERS=0` mantém só CI + PR obrigatórios. Desfazer: `gh api -X DELETE repos/<dono>/<repo>/branches/main/protection`.
- **4Es:** Conformidade ↑↑. **Custo:** pequeno; a decisão de ligar é só dele.

## H5 — Ciclo de feedback do CI (resposta: "Redigir proposta de otimização")
- **Problema:** a suíte local leva ~139 s (594 testes); o CI roda de 3 a 4 minutos.
- **Evidência medida** (`python -m unittest discover -s tests --durations 15`, 2026-11-17): **1 teste = 66 s (47% do total)** — `test_revisor_gate.TestRodar.test_todas_as_specs_vigentes_sem_falso_alarme` (roda o gate em todas as Specs vigentes); depois 11,6 s (`test_revisor_gate_mcp…modo_completo_inclui_detectores`), 11,3 s (`test_revisor_guard…hook_como_processo`) e `test_pre_entrega` (3 testes de ~4,5 s, um deles copia o repositório). Os 10 mais lentos somam ~115 s; os outros 584 testes, ~25 s.
- **Proposta (em ordem de retorno):** (a) tirar os 3 testes pesados do passo geral e dar-lhes passo próprio no `ci.yml`, em **paralelo** com o resto (`needs` independente) — o tempo de relógio cai para ~max(66 s, resto); (b) no teste de 66 s, rodar o gate por Spec em `concurrent.futures` (cada Spec é independente) — alvo ≈ 66/nº de núcleos; (c) em `test_pre_entrega`, trocar `shutil.copytree` do repositório inteiro por cópia só de `scripts/` + a Spec alvo. **Não** pular nem enfraquecer teste algum: o objetivo é o mesmo conjunto, mais cedo.
- **Limite honesto:** (a) mexe em `ci.yml` (COE-02 exige que todo teste continue sendo executado — conferir com `check_coesao`); (b) e (c) mexem em testes de arquivos selados (`revisor_gate`, `pre_entrega`): ata e selo só se o script mudar, o teste não é selado.
- **4Es:** Eficiência ↑↑, Economicidade ↑ (minutos de CI). **Custo:** pequeno–médio.

## H6 — "Leitura obrigatória" que reflita o uso real (resposta: "Proposta de resumo gerado")
- **Problema:** `AGENTS.md` §1 manda ler `ROADMAP.md` e `atomic-spec.md` antes de qualquer entrega, mas a medição do A5 (`PROPOSTA-A5` §5; pauta item 4) achou que **nenhum agente os leu inteiros** (Grep e trechos); a regra literal não é cumprida e o custo de cumpri-la seria alto (ROADMAP > 500 linhas longas).
- **Proposta:** `scripts/ficha_roadmap.py` (Detector/gerador somente leitura; **saída gerada, não versionada**, como o mapa e o ledger) imprime uma **ficha curta e não normativa**: Spec autorizada (§25), decisões abertas ativas e FECHADAS recentes (as linhas "Decisões abertas ativas"/"FECHADAS"), versão vigente do `WORKFLOW.md` e do `atomic-spec.md`, com o número de linha de cada fonte. O agente lê a ficha e **abre a fonte pelo ID** quando precisar; a ficha nunca substitui o ROADMAP (em divergência, o ROADMAP prevalece — INV-09). A mudança do texto de `AGENTS.md` §1 ("leia a ficha + abra a fonte pelo ID citado; o Revisor confere a Spec contra o ROADMAP por Grep") **só é redigida aqui**, não aplicada: `AGENTS.md` é reservado a Andraus.
- **Salvaguardas:** a ficha traz o hash do ROADMAP lido e `check_ficha` (informativo) avisa se ela está defasada; não resume o conteúdo normativo, só indica **onde está**.
- **4Es:** Eficácia ↑ (regra cumprível e verificável), Economicidade ↑ (menos leitura). **Custo:** médio (script + teste + registro).
- **Pendente de Andraus:** aprovar o desenho; depois, ordem expressa para o script e, em ata separada, para mudar o texto do `AGENTS.md`.

## Mescla do PR #197 e C-001
Andraus escolheu "Mesclar #197 com CI verde". **C-001** segue `[a confirmar]` no quadro da pauta: assim que ele disser o enunciado (ou que já foi fechada), o Orquestrador corrige a linha em PR próprio.
