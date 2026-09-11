---
type: Website
title: "MESA MCP Stack Documentation"
description: "One-line install of the CyVerse MESA MCP stack (mesa-mcp, mesa-ducklake, irods-mcp-server, formation-mcp) for Claude Code, Codex CLI, Antigravity, and OpenCode"
resource: https://idss-mesa.github.io/docs/
tags: [documentation, mcp, install, cyverse]
status: stable
generated: { by: "claude/opus-5", at: "2026-09-10T00:00:00Z" }
sources:
  - id: docs-repo
    resource: https://github.com/idss-mesa/docs
    title: "idss-mesa/docs repository"
    author: "team:idss-mesa"
---

# MESA MCP Stack Documentation

One-line install of the CyVerse MESA MCP stack — [mesa-mcp](mesa-mcp.md),
[mesa-ducklake](mesa-ducklake.md),
[irods-mcp-server](irods-mcp-server.md), and
[formation-mcp](formation-mcp.md) — for Claude Code, Codex CLI,
Antigravity, and OpenCode.[^docs-repo]

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
