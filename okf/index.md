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
* [MESA MCP Stack Documentation](concepts/docs.md) - One-line install of the CyVerse MESA MCP stack (mesa-mcp, mesa-ducklake, irods-mcp-server, formation-mcp) for Claude Code, Codex CLI, Antigravity, and OpenCode

# Software
* [mesa-mcp](concepts/mesa-mcp.md) - MCP server bridging the CyVerse Data Store (iRODS) with OBO/OLS ontology AVU tools, DataCite metadata, and DuckLake metadata history
* [mesa-ducklake](concepts/mesa-ducklake.md) - AVU metadata-history library for MESA projects (DuckLake: Postgres/DuckDB catalog plus Parquet in iRODS)
* [irods-mcp-server](concepts/irods-mcp-server.md) - Reference MCP server for the CyVerse Data Store (iRODS), written in Go
* [formation-mcp](concepts/formation-mcp.md) - MCP server for the CyVerse Discovery Environment (Formation API): launch apps and manage analyses, written in Go
* [neon-mcp](concepts/neon-mcp.md) - MCP (2026-07-28) server for the NEON Data API: discover, check availability, list, download and cite NEON ecological data
* [mesa-sandbox](concepts/mesa-sandbox.md) - AI sandboxes for CyVerse VICE: a sudo-free multi-arch image family, sandbox profiles P0–P4, an OpenBao credential broker and egress proxy, and agent-sandbox pods for autonomous agents
* [MESA CLI](concepts/cli.md) - CyVerse Cloud Shell CLI with MESA tools
* [mesa-portal](concepts/mesa-portal.md) - Portal based on the CyVerse Terrain API
* [mesa-forge](concepts/mesa-forge.md) - A metadata extraction tool generation and management library
