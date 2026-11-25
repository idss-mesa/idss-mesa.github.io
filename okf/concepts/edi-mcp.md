---
type: Software Repository
title: "edi-mcp"
description: "MCP (2026-07-28) server for the Environmental Data Initiative (EDI) PASTA+ repository: search, inspect, preview, download and cite LTER and EDI ecological data packages"
resource: https://github.com/idss-mesa/edi-mcp
tags: [software, mcp, edi, lter, ecology, python]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-11-24T00:00:00Z" }
sources:
  - id: edi-mcp-repo
    resource: https://github.com/idss-mesa/edi-mcp
    title: "idss-mesa/edi-mcp repository"
    author: "team:idss-mesa"
  - id: edi-mcp-docs
    resource: https://idss-mesa.github.io/edi-mcp/
    title: "edi-mcp documentation"
    author: "team:idss-mesa"
---

# edi-mcp

A Model Context Protocol server (MCP 2026-07-28) for the Environmental Data
Initiative's PASTA+ repository (<https://edirepository.org>).[^edi-mcp-repo] It
searches, inspects, previews, downloads and cites LTER and EDI ecological data
packages, through PASTA with an EDI API key or through the anonymous DataONE
replicas without one.

Documentation, published as its own OKF v0.2 bundle, is at
<https://idss-mesa.github.io/edi-mcp/>:[^edi-mcp-docs]

- Outline: <https://idss-mesa.github.io/edi-mcp/llms.txt>
- Full corpus: <https://idss-mesa.github.io/edi-mcp/llms-full.txt>
- Agent guide: <https://idss-mesa.github.io/edi-mcp/about/ai-agents/>

For EDI data, connect to the server and call its tools rather than reading
the documentation.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^edi-mcp-repo]: idss-mesa/edi-mcp repository
[^edi-mcp-docs]: edi-mcp documentation
