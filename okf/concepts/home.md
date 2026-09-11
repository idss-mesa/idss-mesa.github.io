---
type: Website
title: "MESA — Multidisciplinary Environment for Scientific Advancement"
description: "MESA is an open-source, agentic AI platform that connects scientific data through curated, indexed metadata — a data lakehouse, a federated data mesh, and AI agents that speak both. NSF IDSS Category II project at the University of New Mexico"
resource: https://idss-mesa.github.io/
tags: [site, mesa, agentic-ai, data-lakehouse, data-mesh, mcp, cyverse]
status: stable
generated: { by: "claude/opus-5", at: "2026-09-10T00:00:00Z" }
stale_after: "2027-03-10T00:00:00Z"
sources:
  - id: landing-src
    resource: https://github.com/idss-mesa/idss-mesa.github.io/blob/main/index.html
    title: "MESA landing page source (index.html)"
    author: "team:idss-mesa"
  - id: nsf-award
    resource: https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2632685
    title: "NSF Award #2632685 — MESA"
    author: "team:nsf"
  - id: install-sh
    resource: https://github.com/idss-mesa/docs/blob/main/install.sh
    title: "MESA MCP stack installer (install.sh)"
    author: "team:idss-mesa"
  - id: openai-black-holes
    resource: https://openai.com/index/creating-new-simulations-black-holes/
    title: "Creating new simulations of black holes (OpenAI)"
    author: "team:openai"
---

# MESA — Multidisciplinary Environment for Scientific Advancement

**Ask the question. MESA finds the data.**

MESA — the Multidisciplinary Environment for Scientific Advancement — is an
open-source, agentic AI platform that connects scientific data through
curated, indexed metadata. A data lakehouse, a federated data mesh, and AI
agents that speak both, running on national research infrastructure
today.[^landing-src]

This document is the Markdown twin of the landing page at
<https://idss-mesa.github.io/>. Documentation lives at
<https://idss-mesa.github.io/docs/>; code at <https://github.com/idss-mesa>.

## Five integrated layers

| # | Layer | Technologies |
|---|-------|--------------|
| 01 | User interface | Laptop · Desktop · K8s container |
| 02 | Agentic AI | MCP · RAG · Agents · Reasoning · Sandboxing |
| 03 | Data management | Data Lakehouse (DuckLake) · Data Mesh (iRODS) |
| 04 | Compute | CyVerse · TACC · ACCESS-CI · NAIRR |
| 05 | Object storage | S3 · OSN · VAST · Lustre |

## Three innovation goals

1. **Open-source data lakehouse.** Analytical tables over open formats —
   DuckLake, Apache Iceberg, Parquet — with time-travel versioning built in.
   Query five petabytes like a database, and rewind any table to the state it
   held when the paper was submitted.
2. **Federated iRODS data mesh.** One policy engine across the CyVerse Data
   Store and its federated peers, with CILogon, Globus Auth, and ORCID
   handling identity. The lakehouse and the mesh interoperate — your data
   stays where it lives, and still shows up where you work.
3. **Agentic AI orchestration.** Self-hosted LLM serving on vLLM, RAG
   pipelines over curated metadata, and an MCP server framework with
   sandboxed, multi-agent orchestration. Agents that find, describe, and move
   scientific data — with the guardrails written first.

## The stack, today

One line. Four servers. No credentials required.

MESA is not a promise — the MCP stack is public and installs now. One command
clones, builds, and registers four CyVerse servers in Claude Code (and in
Codex CLI, Antigravity, and OpenCode); anonymous public access to the Data
Store works out of the box.[^install-sh]

```bash
curl -fsSL https://raw.githubusercontent.com/idss-mesa/docs/main/install.sh | bash
```

| Server | Language | Role |
|--------|----------|------|
| [mesa-mcp](mesa-mcp.md) | Python | iRODS Data Store + OBO/OLS ontology metadata, DataCite, DuckLake history |
| [mesa-ducklake](mesa-ducklake.md) | Python | AVU metadata-history library backing mesa-mcp |
| [irods-mcp-server](irods-mcp-server.md) | Go | Reference iRODS Data Store server |
| [formation-mcp](formation-mcp.md) | Go | CyVerse Discovery Environment — launch apps, manage analyses |

### Featured connectors. Nothing to install.

The Data Store and Discovery Environment servers also run hosted, as remote
MCP connectors — no local build, no toolchain. In Claude Desktop or
claude.ai, open Settings → Connectors → Add custom connector, name the
connector, paste its endpoint URL, and authenticate when prompted. A
connector added to a claude.ai organization follows you everywhere Claude
runs: Claude Desktop, claude.ai, and Claude Code on the web.

| Connector | Server | What it opens |
|-----------|--------|---------------|
| cyverse-irods-shared | [irods-mcp-server](irods-mcp-server.md) | CyVerse Data Store — public collections under `/iplant/home/shared`, anonymous read |
| cyverse-formation | [formation-mcp](formation-mcp.md) | Discovery Environment — browse data, launch apps, track analyses |

Claude Code registers the same endpoints from the terminal (swap in the
current endpoint URLs from the [documentation](docs.md), which also
covers credentialed access, running either server locally in Claude Desktop
via `claude_desktop_config.json`, and self-hosting the endpoints):

```bash
claude mcp add --transport http irods https://IRODS-ENDPOINT/mcp
claude mcp add --transport http formation https://FORMATION-ENDPOINT/mcp
```

## The team

| Name | Role |
|------|------|
| Tyson L. Swetnam, Ph.D. | Principal Investigator · UNM |
| Arthur B. Maccabe, Ph.D. | Co-PI · Arizona site lead |
| David Ebert, Ph.D. | Co-PI · Chief AI & Data Science Officer · Arizona |
| Lei Cao, Ph.D. | Co-PI · Lakehouse lead · Arizona |
| Terrell Russell, Ph.D. | Co-PI · Data Mesh Lead · RENCI Site Lead |
| Illyoung Choi, Ph.D. | Research Software Engineer · Arizona |
| Kory Draughn | Chief Technologist · RENCI |
| Alan King | Senior Software Developer · RENCI |
| Justin James | Applications Engineer · RENCI |
| Sarah Roberts | Research Software Engineer · Arizona |
| Tony Edgin | Data Curator · Arizona |
| Edwin Skidmore | Cloud Orchestration / Infrastructure · CyVerse |
| Greg Chism, Ph.D. | EOT Lead · Senior Personnel · Arizona |
| Jingdi Chen, Ph.D. | 5G/6G Networking · Arizona |
| CK Chan, Ph.D. | Astronomer · Arizona |
| Wolfgang Jentner, Ph.D. | Human-Computer Interaction · Arizona |
| Junjia Guo | PhD Student · Arizona |
| Pengxin Wang | PhD Student · Arizona |
| Junyong Zhao | PhD Student · Arizona |
| Linan Zheng | PhD Student · Arizona |

MESA is hiring; see [MESA Hiring](hiring.md).

## News

- **MESA kicks off with NSF IDSS, July 2026.** The project team convenes with
  the NSF Integrated Data Systems & Services program for the MESA kick-off
  meeting — the University of New Mexico, the University of Arizona, and
  UNC-CH/RENCI, setting the two-year prototype baseline in motion.
- **Creating new simulations of black holes, with OpenAI.** Co-investigator
  CK Chan, Ph.D. worked with OpenAI on creating new simulations of black
  holes — a look at agentic coding against Event Horizon Telescope
  science.[^openai-black-holes]

## Funding

MESA is supported by the U.S. National Science Foundation under Award
#2632685 (Integrated Data Systems & Services, 2026–2029).[^nsf-award] Any
opinions, findings, and conclusions are those of the authors and do not
necessarily reflect the views of the NSF. Partner institutions: University of
New Mexico, University of Arizona, UNC-Chapel Hill / RENCI.

Agents: see [For AI agents](ai-agents.md) for how to read this
origin, and connect to the MCP servers above for the data itself.

[^landing-src]: MESA landing page source (index.html)
[^nsf-award]: NSF Award #2632685 — MESA
[^install-sh]: MESA MCP stack installer (install.sh)
[^openai-black-holes]: Creating new simulations of black holes (OpenAI)
