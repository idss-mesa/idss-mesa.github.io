---
type: Software Repository
title: "ameriflux-mcp"
description: "MCP (2026-07-28) server for AmeriFlux and FLUXNET eddy-covariance data: find flux tower sites, check product and year availability, describe variables and QC flags, cite under the right data policy, download with consent, and preview files"
resource: https://github.com/idss-mesa/ameriflux-mcp
tags: [software, mcp, ameriflux, fluxnet, eddy-covariance, python]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-11-24T00:00:00Z" }
sources:
  - id: ameriflux-mcp-repo
    resource: https://github.com/idss-mesa/ameriflux-mcp
    title: "idss-mesa/ameriflux-mcp repository"
    author: "team:idss-mesa"
  - id: ameriflux-mcp-docs
    resource: https://idss-mesa.github.io/ameriflux-mcp/
    title: "ameriflux-mcp documentation"
    author: "team:idss-mesa"
---

# ameriflux-mcp

A Model Context Protocol server (MCP 2026-07-28) for AmeriFlux and FLUXNET
eddy-covariance data.[^ameriflux-mcp-repo] It finds flux tower sites, checks
which products and years exist, explains FLUXNET variable names and QC flags,
cites data under the CC-BY-4.0, Legacy or Tier 2 policy, downloads through
AmeriFlux's logged route with the user's consent, and previews AmeriFlux BASE
and BADM, AmeriFlux FLUXNET (FLUXNET-1F) and FLUXNET2015 files. Version
0.1.0. The AmeriFlux API is undocumented, so the server checks the shape of
every response and reports drift instead of guessing.

Documentation, published as its own OKF v0.2 bundle, is at
<https://idss-mesa.github.io/ameriflux-mcp/>:[^ameriflux-mcp-docs]

- Outline: <https://idss-mesa.github.io/ameriflux-mcp/llms.txt>
- Full corpus: <https://idss-mesa.github.io/ameriflux-mcp/llms-full.txt>
- Agent guide: <https://idss-mesa.github.io/ameriflux-mcp/about/ai-agents/>

For flux data, connect to the server and call its tools rather than reading
the documentation.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^ameriflux-mcp-repo]: idss-mesa/ameriflux-mcp repository
[^ameriflux-mcp-docs]: ameriflux-mcp documentation
