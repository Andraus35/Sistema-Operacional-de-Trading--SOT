# SPEC-EX-B — Ciclo de vida da hipótese (documento de teste)

| Campo | Valor |
|---|---|
| Complexidade | MEDIUM |
| Profundidade | D0–D5 |
| Profile | light → standard |
| Baselines de referência | <<REF-03|CHM-001|CHM-009>>, <<REF-04|CEM-001|CEM-004>> |

## 1. Hierarquia
A hierarquia é inviolável: <<REG-07|Elliott → Fibonacci → Fractal → SMC → ICT|Elliott → SMC → Fibonacci → Fractal → ICT>>. São <<NUM-08|cinco|quatro>> camadas. A camada inferior <<SEM-07|não sobrepõe|pode sobrepor, se tiver maior confiança,>> a superior.

## 2. Criação de hipóteses
- <<REG-08|Somente o Elliott cria a hipótese PRIMARY.|O Elliott ou o SMC criam a hipótese PRIMARY.>>
- SMC e Fibonacci criam sub-hipóteses <<REG-09|com `parent_id` apontando para a PRIMARY|sem necessidade de `parent_id`>>.
- <<REG-13|O ICT não cria hipótese de nenhum tipo.|O ICT cria sub-hipóteses quando detecta uma killzone.>>
- O tipo de hipótese por especialista (SPEC-010/011/012) <<REG-11|permanece em aberto|já está definido: PRIMARY para o Elliott e SUB para todos os demais>>.

## 3. Estados
Existem <<NUM-07|sete|nove>> estados canônicos, definidos no CHM-001:
<<REG-10|EMERGENT → CANDIDATE → ACTIVE → DOMINANT → SUPERSEDED → REFUTED → ARCHIVED|PROPOSED → VALIDATED → ACTIVE → DOMINANT → SUPERSEDED → REFUTED → ARCHIVED>>.

REFUTED é terminal para fins de decisão. Versionamento é monotônico: <<SEM-04|nada é deletado, e a hipótese refutada segue para ARCHIVED|hipóteses ARCHIVED são removidas após 30 dias>>.

## 4. Conflito direcional
Se Elliott e SMC divergem em direção, a hierarquia manda: <<SEM-06|o resultado é NEUTRO (`directional_conflict = true`)|prevalece o Elliott e o conflito é ignorado>>.

## 5. Sinal
- Uma hipótese REFUTED <<SEM-05|não gera sinal|pode gerar sinal se o score for ≥ 7/9>>.
- A promoção a sinal exige convicção mínima de Fase Piloto de <<NUM-09|70%|85%>>.
- Estados do Blackboard para objetos que não são hipótese (M-001) <<REG-12|seguem em aberto|foram fechados na SPEC-004>>.

## 6. Fora de escopo
Cálculo do Conviction Vector e envio do Signal Package.
