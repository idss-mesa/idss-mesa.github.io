---
type: Webpage
title: "MESA MCP stack"
description: "The MESA stack page: a one-line install of the MESA MCP servers for Claude Code, Codex CLI, Antigravity, and OpenCode, and CyVerse's hosted Formation and public Data Store connectors for claude.ai, Claude Desktop, and Claude Code"
resource: https://idss-mesa.github.io/stack.html
tags: [site, mcp, install, connectors, formation, cyverse]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-10-19T00:00:00Z" }
stale_after: "2027-03-10T00:00:00Z"
sources:
  - id: stack-src
    resource: https://github.com/idss-mesa/idss-mesa.github.io/blob/main/stack.html
    title: "MESA stack page source (stack.html)"
    author: "team:idss-mesa"
  - id: install-sh
    resource: https://github.com/idss-mesa/docs/blob/main/install.sh
    title: "MESA MCP stack installer (install.sh)"
    author: "team:idss-mesa"
  - id: formation
    resource: https://github.com/cyverse-de/formation
    title: "Formation source repository (hosted Discovery Environment MCP server)"
    author: "team:cyverse-de"
---

# MESA MCP stack

**One line. Four servers. Your CyVerse sign-in.**

MESA is not a promise — the MCP stack is public and installs now. One command
clones, builds, and registers the CyVerse servers in Claude Code, Codex CLI,
Antigravity, and OpenCode, and connects them to CyVerse's hosted Formation
server. Anonymous public access to the Data Store works out of the box;
Formation asks you to sign in with your CyVerse account once in each agent
client.[^install-sh]

This document is the Markdown twin of
<https://idss-mesa.github.io/stack.html>.[^stack-src] The full install guide is
the [MESA Documentation](docs.md).

## Install it in one line

```bash
curl -fsSL https://raw.githubusercontent.com/idss-mesa/docs/main/install.sh | bash
```

| Server | Language | Role |
|--------|----------|------|
| [mesa-mcp](mesa-mcp.md) | Python | iRODS Data Store + OBO/OLS ontology metadata, DataCite, DuckLake history |
| [mesa-ducklake](mesa-ducklake.md) | Python | AVU metadata-history library backing mesa-mcp |
| [irods-mcp-server](irods-mcp-server.md) | Go | Reference iRODS Data Store server |
| [Formation](formation-mcp.md) | Hosted by CyVerse | CyVerse Discovery Environment — launch apps, manage analyses |

## Featured connectors. Nothing to install.

CyVerse runs the Discovery Environment server, Formation, as a hosted MCP
server, and serves public Data Store collections the same way — no local
build, no toolchain.[^formation] On claude.ai or in Claude Desktop, open
Customize → Connectors → Add custom connector, name the connector, paste its
endpoint URL, and for Formation choose Register automatically under OAuth
client and sign in with your CyVerse account (the public Data Store connector
needs no sign-in). The Free plan allows one custom
connector, so add the one you need. A connector on your claude.ai account
follows you to Claude Desktop and the Claude mobile apps, and to Claude Code
when Claude Code is signed in with your claude.ai subscription (not an API key
or another model provider).

| Connector | Endpoint | What it opens |
|-----------|----------|---------------|
| [CyVerse Formation](https://idss-mesa.github.io/docs/claude-ai/) | https://de.cyverse.org/formation/mcp | Discovery Environment — launch apps, track analyses, read and write your Data Store files, as you |
| cyverse-irods-shared | https://mcp-public.cyverse.ai/mcp | CyVerse Data Store — public collections under `/iplant/home/shared`, anonymous read |

The installer already registers formation. Without it, Claude Code registers
the same endpoints from the terminal; if an older MESA install left a local
formation entry, run `claude mcp remove formation -s user` first (see
[Moving from the local formation-mcp](https://idss-mesa.github.io/docs/servers/formation-mcp/#moving-from-the-local-formation-mcp)).
Run `/mcp` afterwards to sign in to Formation:

```bash
claude mcp add --transport http --scope user formation https://de.cyverse.org/formation/mcp
claude mcp add --transport http --scope user irods-public https://mcp-public.cyverse.ai/mcp
```

The [Formation docs](https://idss-mesa.github.io/docs/servers/formation-mcp/)
cover Codex, OpenCode, and Antigravity, and the
[connector guide](https://idss-mesa.github.io/docs/claude-ai/) covers Team and
Enterprise organizations.

The rest of the site starts at [MESA](home.md).

[^stack-src]: MESA stack page source (stack.html)
[^install-sh]: MESA MCP stack installer (install.sh)
[^formation]: Formation source repository (hosted Discovery Environment MCP server)
