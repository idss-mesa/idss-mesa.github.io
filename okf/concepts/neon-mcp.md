---
type: Software Repository
title: "neon-mcp"
description: "MCP (2026-07-28) server for the NEON Data API: discover, check availability, list, download and cite NEON ecological data"
resource: https://github.com/idss-mesa/neon-mcp
tags: [software, mcp, neon, ecology, python]
status: stable
generated: { by: "claude/opus-5", at: "2026-09-10T00:00:00Z" }
sources:
  - id: neon-mcp-repo
    resource: https://github.com/idss-mesa/neon-mcp
    title: "idss-mesa/neon-mcp repository"
    author: "team:idss-mesa"
  - id: neon-mcp-docs
    resource: https://idss-mesa.github.io/neon-mcp/
    title: "neon-mcp documentation"
    author: "team:idss-mesa"
---

# neon-mcp

A Model Context Protocol server (MCP 2026-07-28) that gives AI agents
structured, rate-limit-aware access to the NEON Data API: data products,
sites, locations, data availability, releases, taxonomy, samples, and data
downloads.[^neon-mcp-repo] It runs over stdio or stateless Streamable HTTP.
Discovery, availability, taxonomy, release, and location tools work
anonymously; listing and downloading data files needs a NEON API token.

Documentation, published as its own OKF v0.2 bundle, is at
<https://idss-mesa.github.io/neon-mcp/>:[^neon-mcp-docs]

- Outline: <https://idss-mesa.github.io/neon-mcp/llms.txt>
- Full corpus: <https://idss-mesa.github.io/neon-mcp/llms-full.txt>
- Agent guide: <https://idss-mesa.github.io/neon-mcp/about/ai-agents/>

For NEON data, connect to the server and call its tools rather than reading
the documentation.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^neon-mcp-repo]: idss-mesa/neon-mcp repository
[^neon-mcp-docs]: neon-mcp documentation
