---
type: Software Repository
title: "MESA KASM Ubuntu Desktop"
description: "A full Ubuntu 24.04 XFCE desktop in the browser (KasmVNC) for CyVerse VICE, with AI coding-agent CLIs and the MESA MCP servers"
resource: https://github.com/idss-mesa/kasm
tags: [software, vice, kasm, desktop, ubuntu, gpu, opengl]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: kasm-readme
    resource: https://github.com/idss-mesa/kasm/blob/main/README.md
    title: "MESA KASM Ubuntu Desktop README"
    author: "team:idss-mesa"
  - id: app-docs
    resource: https://idss-mesa.github.io/docs/apps/kasm/
    title: "MESA KASM Ubuntu Desktop (MESA documentation)"
    author: "team:idss-mesa"
---

# MESA KASM Ubuntu Desktop

A complete Ubuntu 24.04 XFCE desktop streamed to the browser with
[KasmVNC](https://kasmweb.com/kasmvnc), run as a CyVerse Discovery
Environment (VICE) app, with Chrome, Firefox, VS Code, Claude Code, Codex,
OpenCode, and Antigravity, and the `irods`, `mesa`, `formation`, and
`filesystem` MCP servers registered.[^kasm-readme]

- **Image:** `harbor.cyverse.org/vice/mesa-kasm:latest`; GPU build `:gpu`
  renders the desktop with OpenGL on the GPU and adds VirtualGL, PyTorch, and
  a local Ollama server.
- **Port and working directory:** 6901; `/home/kasm-user/data-store`.

Launch it from the [MESA Portal](mesa-portal.md) at
<https://mesa.cyverse.org/applications/> (MESA Apps tab) or from the CyVerse
Discovery Environment. User guide:
<https://idss-mesa.github.io/docs/apps/kasm/>.[^app-docs] Every MESA
app shares the agent setup described at
<https://idss-mesa.github.io/docs/apps/agents/>.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^kasm-readme]: MESA KASM Ubuntu Desktop README
[^app-docs]: MESA KASM Ubuntu Desktop (MESA documentation)
