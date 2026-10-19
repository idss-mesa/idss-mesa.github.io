---
type: Website
title: "MESA — Multidisciplinary Environment for Scientific Advancement"
description: "MESA is an open-source, agentic AI platform that connects scientific data through curated, indexed metadata — a data lakehouse, a federated data mesh, and AI agents that speak both. NSF IDSS Category II project at the University of New Mexico"
resource: https://idss-mesa.github.io/
tags: [site, mesa, agentic-ai, data-lakehouse, data-mesh, mcp, cyverse]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-10-19T00:00:00Z" }
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
<https://idss-mesa.github.io/docs/>; code at <https://github.com/idss-mesa>; the
MESA Portal at <https://mesa.cyverse.org>.

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

## Explore MESA

The rest of the site has a page each; every page has its own Markdown twin.

| # | Page | Twin | What is on it |
|---|------|------|---------------|
| 01 | [Portal](https://idss-mesa.github.io/portal.html) | [MESA Portal and featured apps](portal.md) | Sign in at mesa.cyverse.org and launch the featured apps with your Data Store mounted |
| 02 | [Stack](https://idss-mesa.github.io/stack.html) | [MESA MCP stack](stack.md) | One line installs the MESA MCP servers; CyVerse's hosted connectors need no install |
| 03 | [Team](https://idss-mesa.github.io/team.html) | [MESA team](team.md) | Investigators, staff, and students at UNM, Arizona, and UNC-CH/RENCI |
| 04 | [News](https://idss-mesa.github.io/news.html) | [MESA news](news.md) | The July 2026 kick-off with NSF IDSS, and CK Chan's black-hole simulations with OpenAI |
| 05 | [We're hiring](https://idss-mesa.github.io/hiring.html) | [MESA Hiring](hiring.md) | Open positions at the UNM Center for Advanced Research Computing in Albuquerque |

## Funding

MESA is supported by the U.S. National Science Foundation under Award
#2632685 (Integrated Data Systems & Services, 2026–2029).[^nsf-award] Any
opinions, findings, and conclusions are those of the authors and do not
necessarily reflect the views of the NSF. Partner institutions: University of
New Mexico, University of Arizona, UNC-Chapel Hill / RENCI.

Agents: see [For AI agents](ai-agents.md) for how to read this
origin, and connect to the MCP servers on the [stack page](stack.md) for the
data itself.

[^landing-src]: MESA landing page source (index.html)
[^nsf-award]: NSF Award #2632685 — MESA
