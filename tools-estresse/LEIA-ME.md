# Teste de estresse — Auditor Externo × Revisor interno

Pasta local (fora do Git, via `.git/info/exclude`). Nada daqui entra no repositório nem no commit que o auditor lê.

## O que é cada coisa
- `base/` — 3 documentos de teste com 45 "slots" (cada um tem uma versão correta e uma defeituosa).
- `gen.py` — sorteia, pela SUA semente secreta, 10 slots defeituosos por documento (30 defeitos). Os 15 slots que sobram ficam corretos e viram **iscas limpas**. Soma os defeitos que VOCÊ escrever.
- `score.py` — confere as respostas contra o gabarito e imprime só números agregados.

## Passo a passo (você faz os passos 1–3 sozinho; eu não vejo)
1. **Ler a versão limpa** para escrever os seus defeitos:
   `python gen.py --clean --out limpo` e abra `limpo/SPEC-EX-A.md` (B, C).
2. **Escrever 3 a 5 defeitos de sentido**, em `extras.json` (guarde longe de mim):
   ```json
   [{"id": "AND-01", "class": "SEM", "file": "SPEC-EX-A.md",
     "find": "texto exato que existe 1 vez", "replace": "texto defeituoso, sem quebra de linha"}]
   ```
   Regra: `find` aparece **exatamente 1 vez** no arquivo (o gerador recusa se não) e, de preferência, em texto fora dos trechos que mudam entre as versões (compare `limpo/` com uma geração de teste) para o seu defeito não se sobrepor a um sorteado.
3. **Gerar** com a sua semente (invente uma frase longa e não a conte):
   `python gen.py --seed "<sua frase>" --extra extras.json --out saida --key gabarito.json`
   Anote o **sha256 do gabarito** que ele imprime e cole no chat (lacre). Guarde `gabarito.json`, `extras.json` e a semente fora do alcance do Orquestrador.
4. **Publicar os documentos** (copiar `saida/*.md` para `estresse/` numa branch de teste a partir do `main` e dar commit **sem abrir os arquivos**). O Orquestrador faz isso quando você disser "pode publicar".
5. **Revisor (3 rodadas):** o Revisor SOT é chamado 3 vezes, em sessões separadas, com o mesmo texto de `PROMPT-REVISOR.txt`, apontando só para a pasta `estresse/` da branch de teste. A resposta é salva sem edição.
6. **Auditor (3 rodadas):** `workflow_dispatch` de `auditor-externo.yml` no commit da branch de teste, `kind=auditoria`, 3 pedidos (gasta 3 das 6 consultas do dia). Os achados `[AEX]` são salvos como JSON.
7. **Conferir:**
   `python score.py --key gabarito.json --run revisor1=r1.txt --run revisor2=r2.txt --run revisor3=r3.txt --run auditor1=a1.json --run auditor2=a2.json --run auditor3=a3.json --detail detalhe.json`
   O terminal mostra só contagens. O `detalhe.json` (quem achou o quê, iscas tocadas) é seu: use para a adjudicação cega das iscas tocadas e dos achados que não casaram com nada.

## Limites que ficam declarados
- O Orquestrador escreveu o conjunto de 45 slots (não sabe quais foram sorteados nem os seus extras, mas conhece o conjunto). Os 3–5 extras seus são a parte livre desse viés.
- O Revisor e o Orquestrador são o mesmo tipo de modelo; o Revisor roda em sessão separada, sem contexto meu.
- O casamento é por `arquivo:linha` ou trecho literal ≥ 12 caracteres. O Revisor precisa citar `arquivo:linha` (já faz parte do protocolo dele); achado sem citação não conta e vai para a sua adjudicação.
- Com 30 defeitos, diferença menor que ~15 pontos percentuais não é conclusiva; o número que decide é o **valor marginal**.
- Mede defeitos plantados, não defeitos reais.
