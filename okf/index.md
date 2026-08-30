---
okf_version: "0.2"
title: "MESA knowledge bundle"
description: "Open Knowledge Format (OKF) bundle indexing the MESA (Multidisciplinary Environment for Scientific Advancement) website, documentation, and software for human and agentic AI consumption"
---

# idss-mesa.github.io

This is the root of an [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle describing MESA — the Multidisciplinary Environment for Scientific
Advancement, an open-source, agentic AI platform for scientific data (NSF
IDSS Category II, University of New Mexico).

All content on this origin, including the [/docs/](https://idss-mesa.github.io/docs/)
sub-site, is open for agentic AI crawlers to read; see
[/robots.txt](/robots.txt) for the site-wide permissive policy. Related
bundles: <https://tyson-swetnam.github.io/okf/index.md> and the
agent-ready site at <https://unm-carc.github.io/>.

# Site
* [MESA — Multidisciplinary Environment for Scientific Advancement](concepts/home.md) - MESA is an open-source, agentic AI platform that connects scientific data through curated, indexed metadata — a data lakehouse, a federated data mesh, and AI agents that speak both. NSF IDSS Category II project at the University of New Mexico
* [MESA Hiring](concepts/hiring.md) - MESA and CARC are hiring at the University of New Mexico — full-time positions at the Center for Advanced Research Computing in Albuquerque

# Documentation
* [MESA MCP Stack Documentation](concepts/docs.md) - One-line install of the CyVerse MESA MCP stack (mesa-mcp, mesa-ducklake, irods, formation) for Claude Code

# Software
* [mesa-mcp](concepts/mesa-mcp.md) - MCP server bridging the CyVerse Data Store (iRODS) with OBO/OLS ontology AVU tools, DataCite metadata, and DuckLake metadata history
* [mesa-ducklake](concepts/mesa-ducklake.md) - AVU metadata-history library for MESA projects (DuckLake: Postgres/DuckDB catalog plus Parquet in iRODS)
* [irods-mcp-server](concepts/irods-mcp-server.md) - Reference MCP server for the CyVerse Data Store (iRODS), written in Go
* [formation-mcp](concepts/formation-mcp.md) - MCP server for the CyVerse Discovery Environment (Formation API): launch apps and manage analyses, written in Go
* [MESA CLI](concepts/cli.md) - CyVerse Cloud Shell CLI with MESA tools
* [mesa-portal](concepts/mesa-portal.md) - Portal based on the CyVerse Terrain API
* [mesa-forge](concepts/mesa-forge.md) - A metadata extraction tool generation and management library
