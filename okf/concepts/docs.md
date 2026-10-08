---
type: Website
title: "MESA Documentation"
description: "MESA documentation: the MESA Portal at mesa.cyverse.org and its featured CyVerse apps, the one-line install of the MESA MCP stack (mesa-mcp, mesa-ducklake, irods-mcp-server) for Claude Code, Codex CLI, Antigravity, and OpenCode, and CyVerse's hosted Formation MCP server, also available as a claude.ai connector"
resource: https://idss-mesa.github.io/docs/
tags: [documentation, mcp, install, cyverse, portal, vice]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
sources:
  - id: docs-repo
    resource: https://github.com/idss-mesa/docs
    title: "idss-mesa/docs repository"
    author: "team:idss-mesa"
---

# MESA Documentation

User guides for the [MESA Portal](mesa-portal.md) at <https://mesa.cyverse.org>
(managing data, starting applications, managing analyses, with screenshots)
and for the MESA featured apps — [MESA CLI](cli.md),
[MESA JupyterLab](jupyterlab.md), [MESA RStudio Geospatial](rstudio.md),
[MESA VS Code](vscode.md), and [MESA KASM Ubuntu Desktop](kasm.md) — at
<https://idss-mesa.github.io/docs/portal/> and
<https://idss-mesa.github.io/docs/apps/>.

It also documents the one-line install of the CyVerse MESA MCP stack — [mesa-mcp](mesa-mcp.md),
[mesa-ducklake](mesa-ducklake.md), and
[irods-mcp-server](irods-mcp-server.md), plus CyVerse's hosted
[Formation](formation-mcp.md) server — for Claude Code, Codex CLI,
Antigravity, and OpenCode, and how to add Formation as a custom connector on
claude.ai and in Claude Desktop.[^docs-repo]

```bash
curl -fsSL https://raw.githubusercontent.com/idss-mesa/docs/main/install.sh | bash
```

The site covers a quickstart, the full installer reference (flags,
environment overrides, on-disk layout, uninstall), one integration page per
agent client, credentials for authenticated CyVerse access, a page per
server, and troubleshooting.

## For agents

The documentation is its own OKF v0.2 bundle, built with Zensical from the
[idss-mesa/docs](https://github.com/idss-mesa/docs) repository:

- Outline: <https://idss-mesa.github.io/docs/llms.txt>
- Full corpus: <https://idss-mesa.github.io/docs/llms-full.txt>
- Any page's Markdown source: its URL plus `index.md`
- Agent guide: <https://idss-mesa.github.io/docs/about/ai-agents/>

Crawling of `/docs/` is governed by this origin's
<https://idss-mesa.github.io/robots.txt>.

[^docs-repo]: idss-mesa/docs repository
