---
type: Webpage
title: "MESA Portal and featured apps"
description: "The MESA Portal page: sign in at mesa.cyverse.org with a free CyVerse account to manage Data Store files and analyses, and launch the five featured apps — MESA Cloud Shell, JupyterLab, RStudio Geospatial, VS Code, and KASM Ubuntu Desktop — with your Data Store mounted"
resource: https://idss-mesa.github.io/portal.html
tags: [site, portal, cyverse, apps, data-store]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-10-19T00:00:00Z" }
stale_after: "2027-03-10T00:00:00Z"
sources:
  - id: portal-src
    resource: https://github.com/idss-mesa/idss-mesa.github.io/blob/main/portal.html
    title: "MESA Portal page source (portal.html)"
    author: "team:idss-mesa"
  - id: portal
    resource: https://mesa.cyverse.org/
    title: "MESA Portal"
    author: "team:idss-mesa"
  - id: portal-docs
    resource: https://idss-mesa.github.io/docs/portal/
    title: "MESA Portal guides (MESA documentation)"
    author: "team:idss-mesa"
---

# MESA Portal and featured apps

**The MESA Portal. Sign in and start.**

Sign in to <https://mesa.cyverse.org> with a free CyVerse account to browse,
share, and describe your Data Store files, launch apps, and follow your
analyses.[^portal] The featured apps start from the portal with your Data
Store mounted and the MESA MCP servers already registered for Claude Code,
Codex, OpenCode, and Antigravity.[^portal-src]

This document is the Markdown twin of
<https://idss-mesa.github.io/portal.html>. The portal software itself is the
concept [mesa-portal](mesa-portal.md).

## Featured apps

| Featured app | What it is | Source |
|--------------|------------|--------|
| [MESA Cloud Shell](https://idss-mesa.github.io/docs/apps/cli/) | A terminal in the browser with five AI coding-agent CLIs | [MESA CLI](cli.md) |
| [MESA JupyterLab](https://idss-mesa.github.io/docs/apps/jupyterlab/) | Python, R, and Julia notebooks, with RStudio and VS Code in the Launcher | [MESA JupyterLab](jupyterlab.md) |
| [MESA RStudio Geospatial](https://idss-mesa.github.io/docs/apps/rstudio/) | RStudio on the Rocker geospatial stack | [MESA RStudio Geospatial](rstudio.md) |
| [MESA VS Code](https://idss-mesa.github.io/docs/apps/vscode/) | VS Code in the browser, with Cline wired to the MESA MCP servers | [MESA VS Code](vscode.md) |
| [MESA KASM Ubuntu Desktop](https://idss-mesa.github.io/docs/apps/kasm/) | A full Ubuntu desktop in the browser | [MESA KASM Ubuntu Desktop](kasm.md) |

Each app also has a GPU build with CUDA PyTorch and a local Ollama server.
Step-by-step guides with screenshots cover
[managing data](https://idss-mesa.github.io/docs/portal/data/),
[starting applications](https://idss-mesa.github.io/docs/portal/applications/),
and [managing analyses](https://idss-mesa.github.io/docs/portal/analyses/).[^portal-docs]

The rest of the site starts at [MESA](home.md).

[^portal-src]: MESA Portal page source (portal.html)
[^portal]: MESA Portal
[^portal-docs]: MESA Portal guides (MESA documentation)
