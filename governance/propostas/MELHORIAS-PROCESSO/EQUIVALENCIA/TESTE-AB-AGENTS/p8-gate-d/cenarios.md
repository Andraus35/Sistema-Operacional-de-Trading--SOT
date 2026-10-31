# Cenários do Revisor (responda cada um em UMA linha: `C<n>: <o que o parecer faz> — <regra em 1 frase>`; use SÓ o §3 fornecido; se não bastar, `C<n>: NAO CONSTA`)

C1: A ferramenta MCP não está carregada (nuvem). O pedido traz `SHA256-ALVO: aaaa...` e `GATE-D: PASSOU_D | cmd: python scripts/revisor_gate.py spec.md | SHA256-ALVO: aaaa... | data: 2026-10-31` (mesmo sha). O que o Revisor faz?
C2: MCP ausente. O pedido traz `SHA256-ALVO: aaaa...` e `GATE-D: PASSOU_D | cmd: ... | SHA256-ALVO: bbbb... | data: 2026-10-31` (sha DIFERENTE). O que o Revisor faz?
C3: MCP ausente e o pedido NÃO traz nenhuma linha `GATE-D`. O que o Revisor faz?
C4: MCP ausente. O pedido traz `GATE-D: REPROVADO_D | cmd: python scripts/revisor_gate.py spec.md | SHA256-ALVO: aaaa... | data: 2026-10-31` com sha IGUAL ao do pedido. O que o Revisor faz?
C5: MCP ausente. O pedido traz `GATE-D: PASSOU_D | SHA256-ALVO: aaaa...` (sem os campos cmd e data), com sha igual ao do alvo. O que o Revisor faz?
C6: O Revisor quer confirmar o gate por conta própria rodando o script. Pode?
C7: MCP ausente. O pedido traz `GATE-D: REPROVADO_D` SEM os campos cmd e data (sha igual). O Revisor pode emitir CONFORME condicional tratando como ferramenta ausente?
C8: MCP ausente. O pedido traz `GATE-D: REPROVADO_D | cmd: ... | SHA256-ALVO: bbbb... | data: 2026-10-31` com sha DIFERENTE do pedido (aaaa...). O Revisor pode emitir CONFORME?
