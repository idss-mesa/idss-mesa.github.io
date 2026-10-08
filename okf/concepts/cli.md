---
type: Software Repository
title: "MESA CLI"
description: "CyVerse Cloud Shell CLI with MESA tools"
resource: https://github.com/idss-mesa/cli
tags: [software, vice, cli, cloud-shell, terminal, agents, gpu]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: cli-readme
    resource: https://github.com/idss-mesa/cli/blob/main/README.md
    title: "MESA CLI README"
    author: "team:idss-mesa"
  - id: app-docs
    resource: https://idss-mesa.github.io/docs/apps/cli/
    title: "MESA CLI (Cloud Shell) (MESA documentation)"
    author: "team:idss-mesa"
---

# MESA CLI

CyVerse Cloud Shell CLI with MESA tools: a browser terminal (ttyd, with
`bash` inside `tmux`) run as a CyVerse Discovery Environment (VICE) app,
listed in the MESA Portal as **MESA Cloud Shell**. It bundles Claude Code,
Codex, OpenCode, Goose, and Antigravity with the `irods`, `mesa`,
`formation`, and `filesystem` MCP servers registered, GoCommands and other
CyVerse Data Store tools, and a geospatial conda environment.[^cli-readme]

- **Image:** `harbor.cyverse.org/vice/mesa-cli:latest` (`:arm64` for Apple
  Silicon); GPU build `:gpu` adds CUDA PyTorch, transformers, and a local
  Ollama server.
- **Port and working directory:** 7681; `/home/jovyan/data-store`.

Launch it from the [MESA Portal](mesa-portal.md) at
<https://mesa.cyverse.org/applications/> (MESA Apps tab) or from the CyVerse
Discovery Environment. User guide:
<https://idss-mesa.github.io/docs/apps/cli/>.[^app-docs]

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico. Canonical
resource: <https://github.com/idss-mesa/cli>. Organization: <https://github.com/idss-mesa>.

Agentic AI crawlers are welcome to read all content on this origin; see
the site-wide permissive policy in <https://idss-mesa.github.io/robots.txt>
and the agent guide at <https://idss-mesa.github.io/about/ai-agents/>.

[^cli-readme]: MESA CLI README
[^app-docs]: MESA CLI (Cloud Shell) (MESA documentation)
