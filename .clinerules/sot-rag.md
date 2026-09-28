---
description: Rules for editing RAG knowledge base files in rag/ directory.
globs: ["rag/**/*.md"]
paths: ["rag/**/*.md"]
alwaysApply: false
---

# SOT RAG Knowledge Base Rules

## Chunk frontmatter format

Every RAG chunk MUST have YAML frontmatter with ALL fields:
```
---
chunk_id: <AGENT-NNN>
agente: <AgentClassName>
topico: <snake_case_topic>
prioridade: critica | alta | media | baixa
quando_consultar: <when to retrieve this chunk>
---
```

## Chunk ID naming convention

- EW-NNN: Elliott Wave chunks
- FB-NNN: Fibonacci chunks
- SM-NNN: SMC chunks
- ICT-NNN: ICT chunks
- SY-NNN: Synthesis chunks

## Content requirements per chunk

- Lead with the concept name in bold
- Include at least one concrete rule or decision criterion
- For score-related chunks: always include the full 0-3 scale definition
- For antiescopo chunks: use a bullet list of "NUNCA faz X → responsabilidade de Y"

## Chunk size limits

- Maximum 300 words per chunk
- A chunk that exceeds 300 words must be split into two focused sub-chunks

## Antiescopo chunk is mandatory

Every agent knowledge base MUST have a chunk with `topico: antiescopo_absoluto` as the final chunk.
