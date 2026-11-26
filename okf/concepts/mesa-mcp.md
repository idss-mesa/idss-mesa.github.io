---
type: Software Repository
title: "mesa-mcp"
description: "MCP server bridging the CyVerse Data Store (iRODS) with OBO/OLS ontology AVU tools, DataCite metadata, and DuckLake metadata history"
resource: https://github.com/idss-mesa/mesa-mcp
tags: [software, mcp, irods, ontology, metadata, python]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-11-26T00:00:00Z" }
sources:
  - id: mesa-mcp-repo
    resource: https://github.com/idss-mesa/mesa-mcp
    title: "idss-mesa/mesa-mcp repository"
    author: "team:idss-mesa"
  - id: mesa-mcp-docs
    resource: https://idss-mesa.github.io/mesa-mcp/
    title: "mesa-mcp documentation"
    author: "team:idss-mesa"
---

# mesa-mcp

A Model Context Protocol server that bridges the CyVerse Data Store (iRODS)
with OBO/OLS ontology tools.[^mesa-mcp-repo] It reads and writes Data Store
files, AVU metadata and tickets; turns ontology terms into AVUs (the
attribute is `<ontology>.<label>`, the unit is the term's CURIE); exports
and validates DataCite records stored as `datacite.*` AVUs; and mirrors every
AVU change it makes into the project's history through
[mesa-ducklake](mesa-ducklake.md), which it imports in-process. The history
tools are `mesa_ducklake_init_project`, `mesa_ducklake_history` and
`mesa_ducklake_time_travel`. It runs over stdio or HTTP.

Documentation, published as its own OKF v0.2 bundle, is at
<https://idss-mesa.github.io/mesa-mcp/>:[^mesa-mcp-docs]

- Outline: <https://idss-mesa.github.io/mesa-mcp/llms.txt>
- Full corpus: <https://idss-mesa.github.io/mesa-mcp/llms-full.txt>
- Agent guide: <https://idss-mesa.github.io/mesa-mcp/about/ai-agents/>

For Data Store files and metadata, connect to the server and call its tools
rather than reading the documentation.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^mesa-mcp-repo]: idss-mesa/mesa-mcp repository
[^mesa-mcp-docs]: mesa-mcp documentation
