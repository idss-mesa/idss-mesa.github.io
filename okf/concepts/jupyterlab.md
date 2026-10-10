---
type: Software Repository
title: "MESA JupyterLab"
description: "JupyterLab data-science workbench (Python, R, Julia) for CyVerse VICE with RStudio, Shiny, VS Code, AI coding-agent CLIs, and the MESA MCP servers"
resource: https://github.com/idss-mesa/jupyterlab
tags: [software, vice, jupyterlab, python, r, julia, gpu]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: jupyterlab-readme
    resource: https://github.com/idss-mesa/jupyterlab/blob/main/README.md
    title: "MESA JupyterLab README"
    author: "team:idss-mesa"
  - id: app-docs
    resource: https://idss-mesa.github.io/docs/apps/jupyterlab/
    title: "MESA JupyterLab (MESA documentation)"
    author: "team:idss-mesa"
---

# MESA JupyterLab

A [JupyterLab](https://jupyterlab.readthedocs.io/) workbench built on the
Project Jupyter datascience-notebook image (Python, R, and Julia), run as a
CyVerse Discovery Environment (VICE) app. RStudio Server, Shiny Server, and VS
Code open from the JupyterLab Launcher; Claude Code, Codex, OpenCode, and
Antigravity are installed with the `irods`, `mesa`, `formation`, and
`filesystem` MCP servers registered.[^jupyterlab-readme]

- **Image:** `harbor.cyverse.org/vice/mesa-jupyterlab:latest`; GPU build
  `:gpu` adds CUDA PyTorch, ML libraries, NVDashboard, Jupyter AI, and a local
  Ollama server.
- **Port and working directory:** 8888; `/home/jovyan/data-store` (the Data
  Store mount).

Launch it from the [MESA Portal](mesa-portal.md) at
<https://mesa.cyverse.org/applications/> (MESA Apps tab) or from the CyVerse
Discovery Environment. User guide:
<https://idss-mesa.github.io/docs/apps/jupyterlab/>.[^app-docs] Every MESA
app shares the agent setup described at
<https://idss-mesa.github.io/docs/apps/agents/>.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^jupyterlab-readme]: MESA JupyterLab README
[^app-docs]: MESA JupyterLab (MESA documentation)
