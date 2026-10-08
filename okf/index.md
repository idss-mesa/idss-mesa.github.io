---
okf_version: "0.2"
title: "MESA knowledge bundle"
description: "Open Knowledge Format (OKF) bundle indexing the MESA (Multidisciplinary Environment for Scientific Advancement) website, documentation, and software for human and agentic AI consumption"
---

# idss-mesa.github.io

This is the root of an [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle describing MESA — the Multidisciplinary Environment for Scientific
Advancement, an open-source, agentic AI platform for scientific data (NSF
IDSS Category II, University of New Mexico). Each page of
<https://idss-mesa.github.io/> has a concept here that is its Markdown twin.

All content on this origin, including the
[/docs/](https://idss-mesa.github.io/docs/) and
[/neon-mcp/](https://idss-mesa.github.io/neon-mcp/) sub-sites, is open to AI
crawlers under <https://idss-mesa.github.io/robots.txt>. The agent guide is
[For AI agents](concepts/ai-agents.md); the whole bundle in one file is
<https://idss-mesa.github.io/llms-full.txt>. Related bundles:
<https://carc.unm.edu/docs/llms.txt> and
<https://tyson-swetnam.github.io/okf/index.md>.

# Site
* [MESA — Multidisciplinary Environment for Scientific Advancement](concepts/home.md) - MESA is an open-source, agentic AI platform that connects scientific data through curated, indexed metadata — a data lakehouse, a federated data mesh, and AI agents that speak both. NSF IDSS Category II project at the University of New Mexico
* [MESA Hiring](concepts/hiring.md) - MESA and CARC are hiring at the University of New Mexico — full-time positions at the Center for Advanced Research Computing in Albuquerque
* [For AI agents](concepts/ai-agents.md) - How agents and harnesses should read idss-mesa.github.io — robots.txt, llms.txt, Markdown twins with OKF v0.2 frontmatter, and trust signals — and why to call the MESA MCP servers for data

# Documentation
* [MESA Documentation](concepts/docs.md) - MESA documentation: the MESA Portal at mesa.cyverse.org and its featured CyVerse apps, the one-line install of the MESA MCP stack (mesa-mcp, mesa-ducklake, irods-mcp-server) for Claude Code, Codex CLI, Antigravity, and OpenCode, and CyVerse's hosted Formation MCP server, also available as a claude.ai connector

# Software
* [mesa-mcp](concepts/mesa-mcp.md) - MCP server bridging the CyVerse Data Store (iRODS) with OBO/OLS ontology AVU tools, DataCite metadata, and DuckLake metadata history
* [mesa-ducklake](concepts/mesa-ducklake.md) - AVU metadata-history library for MESA projects (DuckLake: Postgres/DuckDB catalog plus Parquet in iRODS)
* [irods-mcp-server](concepts/irods-mcp-server.md) - Reference MCP server for the CyVerse Data Store (iRODS), written in Go
* [Formation (hosted MCP server)](concepts/formation-mcp.md) - CyVerse's hosted MCP server for the Discovery Environment at https://de.cyverse.org/formation/mcp: launch apps, manage analyses, and read and write Data Store files after signing in with a CyVerse account, from claude.ai, Claude Desktop, or Claude Code (Codex, OpenCode, and Antigravity can also be configured; their sign-in is not yet confirmed)
* [neon-mcp](concepts/neon-mcp.md) - MCP (2026-07-28) server for the NEON Data API: discover, check availability, list, download and cite NEON ecological data
* [mesa-sandbox](concepts/mesa-sandbox.md) - AI sandboxes for CyVerse VICE: a sudo-free multi-arch image family, sandbox profiles P0–P4, an OpenBao credential broker and egress proxy, and agent-sandbox pods for autonomous agents
* [mesa-portal](concepts/mesa-portal.md) - The MESA Portal at mesa.cyverse.org: a web portal for the CyVerse Data Store, Discovery Environment apps, and analyses, built on the CyVerse Terrain API
* [MESA CLI](concepts/cli.md) - CyVerse Cloud Shell CLI with MESA tools
* [MESA JupyterLab](concepts/jupyterlab.md) - JupyterLab data-science workbench (Python, R, Julia) for CyVerse VICE with RStudio, Shiny, VS Code, AI coding-agent CLIs, and the MESA MCP servers
* [MESA RStudio Geospatial](concepts/rstudio.md) - RStudio Server on the Rocker geospatial stack for CyVerse VICE, with AI coding-agent CLIs and the MESA MCP servers
* [MESA VS Code](concepts/vscode.md) - VS Code in the browser (code-server) for CyVerse VICE with Python, Jupyter, and Cline extensions, AI coding-agent CLIs, and the MESA MCP servers
* [MESA KASM Ubuntu Desktop](concepts/kasm.md) - A full Ubuntu 24.04 XFCE desktop in the browser (KasmVNC) for CyVerse VICE, with AI coding-agent CLIs and the MESA MCP servers
* [mesa-forge](concepts/mesa-forge.md) - A metadata extraction tool generation and management library
