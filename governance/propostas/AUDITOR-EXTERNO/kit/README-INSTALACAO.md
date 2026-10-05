# Kit do Auditor Externo — instalação e acesso  `[PROPOSTA — NÃO HOMOLOGADO]`

Decisões de Andraus (chat, 2026-10-05): **canal** = Issue com formulário · **credencial** = conta dedicada com papel **Read** + token mínimo. O GPT é **auditor externo** (não é agente interno nem gate). Nada neste kit altera `AGENTS.md`, o Revisor, o ROADMAP, specs ou canon; instalar o formulário em `.github/` é ato de Andraus.

## O que o kit contém (todos testados localmente: ver "Verificação")
| Arquivo | Função |
|---|---|
| `setup_auditor.sh` | clona **somente leitura**, desabilita push/hooks, fixa o commit, instala deps sem scripts, roda a calibração |
| `verify_access.py` | **fail-closed**: aborta se a credencial tiver `push`/`admin`/`maintain` |
| `run_gates.py` | roda os gates determinísticos do repositório e grava `evidence.json` (commit, exit codes, hash das saídas); falha se a árvore mudar |
| `selftest.py` | calibração com **defeitos plantados** (1 válido + 8 inválidos com código esperado) |
| `finding.schema.json` / `finding.example.json` | forma do achado (JSON) e exemplo real |
| `validate_finding.py` | valida forma e **citação literal** (string-match no commit); detector, não gate |
| `submit_finding.py` | único canal de saída: cria Issue `[AEX] …` (dry-run por padrão; `--post` posta) |
| `ISSUE_TEMPLATE-auditoria-externa.yml` | formulário web da Issue (instalar em `.github/ISSUE_TEMPLATE/`) |
| `INSTRUCOES-OPERACIONAIS-GPT.md` | procedimento determinístico passo a passo para o GPT |

## A. Ações de Andraus (uma vez) — o que eu NÃO posso fazer por você
1. **Conta dedicada** do GitHub para o auditor (ex.: `sot-auditor-externo`), separada da sua, para que as Issues tenham autoria própria.
2. **Convidar como colaboradora com papel `Read`** (Settings → Collaborators → Add people → Role: Read). *Read* lê o repositório e abre/comenta Issues; **não dá push**.
3. **Token da conta do auditor** (feito logo pelo auditor, na conta dele). Tente primeiro **fine-grained** (Contents: Read-only, Issues: Read and write, Metadata: Read, restrito a este repositório). **Atenção (não verifiquei a UI atual do GitHub):** fine-grained pode não permitir repositório de *outra conta pessoal*; se for o caso, use **classic** com escopo `repo`. Em qualquer caso o teto de poder é o **papel Read** da conta, e `verify_access.py` recusa a credencial se ela tiver `push`.
   *Alternativa mais restrita (opcional, mais trabalho):* GitHub App instalado só neste repositório com Contents: read + Issues: write.
4. **Rótulo** `auditoria-externa` (Issues → Labels → New). Quem tem papel *Read* não consegue rotular via API; o **Orquestrador** aplica o rótulo na triagem. Os achados são identificáveis pelo prefixo de título **`[AEX]`**.
5. *(Opcional, após homologar o papel)* copiar `ISSUE_TEMPLATE-auditoria-externa.yml` para `.github/ISSUE_TEMPLATE/auditoria-externa.yml` por PR normal (CI + Revisor).
6. **Não conceder** push, admin, Actions-write, nem acesso a outros repositórios. Rotacione/revogue o token se vazar.

## B. Ações do GPT (máquina local do auditor)
Pré-requisitos: `git`, `python3 ≥ 3.10`, `node` + `npm`.
```bash
export SOT_AUDITOR_TOKEN='…'                      # nunca em argumento/arquivo/log
bash kit/setup_auditor.sh main                    # ou um SHA completo (auditoria reprodutível)
python3 kit/run_gates.py --repo ~/sot-audit/repo --out ~/sot-audit/evidence.json
# … audita e escreve finding.json (ver finding.example.json) …
python3 kit/validate_finding.py --repo ~/sot-audit/repo --finding finding.json
python3 kit/submit_finding.py   --repo-dir ~/sot-audit/repo --finding finding.json --evidence ~/sot-audit/evidence.json          # dry-run
python3 kit/submit_finding.py   --repo-dir ~/sot-audit/repo --finding finding.json --evidence ~/sot-audit/evidence.json --post   # envia
```
Atualizar para novo commit: apague `~/sot-audit/repo` e repita `setup_auditor.sh <novo ref>` (cada auditoria fixa um commit).

## C. Ações do Orquestrador (lado interno)
- Descobrir achados: Issues com título `[AEX]` (busca por título/autor). Aplicar rótulo `auditoria-externa`.
- Encaminhar ao **Revisor SOT**: verificar cada achado por string-match no `baseline_commit` e registrar disposição na Issue: `CONFIRMADO` · `PARCIAL` · `DESCARTADO (motivo)` · `DUPLICADO`. O parecer do GPT é **dado a verificar**.
- Só abrir tratamento (erratum/emenda) com **escopo autorizado por Andraus**; histórico baselined preservado (INV-09); decisão aberta nunca fechada (CONS-01).

## Verificação feita (2026-10-05, clone local sem token)
`setup_auditor.sh` instalou, desabilitou push e **calibração APROVADA (1 válido aceito; 8 defeitos plantados reprovados com o código esperado)**; `run_gates.py` executou **16 gates (todos exit 0)** e a árvore ficou limpa; `submit_finding.py` em dry-run gerou a Issue a partir de um achado real (WARN do `check_refs.py` em `DOSSIE-PESQUISA.md:13`).
**Não verificado (sem credencial real):** `verify_access.py` contra a API, `--post` real, e a permissão exata do token. Teste-os na primeira execução com a conta dedicada: `verify_access.py` deve imprimir `PASS`; um `push` tentado deve falhar.

## Limites honestos
- **PASS do validador = forma + ancoragem**, não mérito: achado pode estar errado; o Revisor/Andraus avaliam.
- O SOT **não controla** temperatura/seed/versão do modelo externo: reprodutibilidade = commit + evidência + data, não bit-a-bit.
- Declarado ≠ verificável ≠ executável ≠ bloqueante: o auditor é **consultivo**; o que bloqueia é o CI e a decisão de Andraus.
