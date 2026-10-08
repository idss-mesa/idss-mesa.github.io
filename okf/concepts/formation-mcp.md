---
type: MCP Server
title: "Formation (hosted MCP server)"
description: "CyVerse's hosted MCP server for the Discovery Environment at https://de.cyverse.org/formation/mcp: launch apps, manage analyses, and read and write Data Store files from claude.ai, Claude Code, Codex, OpenCode, or Antigravity after signing in with a CyVerse account"
resource: https://de.cyverse.org/formation/mcp
tags: [software, mcp, hosted, connector, discovery-environment, cyverse]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: formation
    resource: https://github.com/cyverse-de/formation
    title: "Formation source repository (README and landing page)"
    author: "team:cyverse-de"
  - id: formation-docs
    resource: https://idss-mesa.github.io/docs/servers/formation-mcp/
    title: "Formation (hosted) — MESA documentation"
    author: "team:idss-mesa"
---

# Formation (hosted MCP server)

Formation is the CyVerse Discovery Environment's own Model Context Protocol
server, hosted by CyVerse at <https://de.cyverse.org/formation/mcp>
(Streamable HTTP). Clients sign in with a CyVerse account through standard MCP
OAuth (authorization code with PKCE against CyVerse's Keycloak, with automatic
client registration); every tool then acts as that user.[^formation]

- **Tools:** `whoami`, `list_apps`, `get_app_parameters`,
  `launch_app_and_wait`, `get_analysis_status`, `list_running_analyses`,
  `stop_analysis`, `browse_data`, `create_directory`, `upload_file`,
  `set_metadata`, `delete_data`.
- **Clients:** a custom connector on claude.ai and in Claude Desktop, Claude
  Code, Codex CLI, OpenCode, and Antigravity. The MESA installer registers it
  with every client it finds, and the MESA featured apps ship with it.
- **History:** it replaced the stdio server formation-mcp
  (<https://github.com/idss-mesa/formation-mcp>), which called Formation's
  former REST API; CyVerse removed that API on 2026-06-11.

Setup for each client: <https://idss-mesa.github.io/docs/servers/formation-mcp/>
and <https://idss-mesa.github.io/docs/claude-ai/>.[^formation-docs]

Part of MESA (Multidisciplinary Environment for Scientific Advancement), an
NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^formation]: Formation source repository (README and landing page)
[^formation-docs]: Formation (hosted) — MESA documentation
