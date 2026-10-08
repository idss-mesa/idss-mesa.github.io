---
type: Software Repository
title: "MESA VS Code"
description: "VS Code in the browser (code-server) for CyVerse VICE with Python, Jupyter, and Cline extensions, AI coding-agent CLIs, and the MESA MCP servers"
resource: https://github.com/idss-mesa/vscode
tags: [software, vice, vscode, code-server, cline, gpu, cuda]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: vscode-readme
    resource: https://github.com/idss-mesa/vscode/blob/main/README.md
    title: "MESA VS Code README"
    author: "team:idss-mesa"
  - id: app-docs
    resource: https://idss-mesa.github.io/docs/apps/vscode/
    title: "MESA VS Code (MESA documentation)"
    author: "team:idss-mesa"
---

# MESA VS Code

Visual Studio Code in the browser
([code-server](https://github.com/coder/code-server)), run as a CyVerse
Discovery Environment (VICE) app, with the Python, Jupyter, and Cline
extensions (Cline pre-loaded with the MESA MCP servers), Globus Connect
Server, Claude Code, Codex, OpenCode, and Antigravity.[^vscode-readme]

- **Image:** `harbor.cyverse.org/vice/mesa-vscode:latest`; GPU build `:gpu`
  adds the CUDA 12.5 toolkit, a PyTorch environment, Nsight, clangd, CMake
  Tools, Continue, and a local Ollama server.
- **Port and working directory:** 8080; the user's Data Store home folder.

Launch it from the [MESA Portal](mesa-portal.md) at
<https://mesa.cyverse.org/applications/> (MESA Apps tab) or from the CyVerse
Discovery Environment. User guide:
<https://idss-mesa.github.io/docs/apps/vscode/>.[^app-docs] Every MESA
app shares the agent setup described at
<https://idss-mesa.github.io/docs/apps/agents/>.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^vscode-readme]: MESA VS Code README
[^app-docs]: MESA VS Code (MESA documentation)
