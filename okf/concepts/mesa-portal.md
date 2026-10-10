---
type: Software Repository
title: "mesa-portal"
description: "The MESA Portal at mesa.cyverse.org: a web portal for the CyVerse Data Store, Discovery Environment apps, and analyses, built on the CyVerse Terrain API"
resource: https://github.com/idss-mesa/mesa-portal
visibility: private
tags: [software, portal, web, cyverse, terrain, vice]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: portal
    resource: https://mesa.cyverse.org/
    title: "MESA Portal"
    author: "team:idss-mesa"
  - id: portal-docs
    resource: https://idss-mesa.github.io/docs/portal/
    title: "MESA Portal guides (MESA documentation)"
    author: "team:idss-mesa"
---

# mesa-portal

The source of the **MESA Portal**, live at <https://mesa.cyverse.org>: a web
portal, built on the CyVerse Terrain API, where people sign in with their
CyVerse account to work with the CyVerse Data Store and the Discovery
Environment from a browser.[^portal]

- **Data Browser** (`/data/`): browse My Files, Shared, User Shared, the MESA
  Community folder, and public data; upload, move, trash, and share files;
  read and edit AVU metadata.
- **Applications** (`/applications/`): the MESA featured apps and the whole
  Discovery Environment catalog, with Instant Launch, Launch with Options, and
  CPU or GPU builds of the MESA apps.
- **Analyses** (`/analyses/`): open running apps, extend their time limits,
  watch logs, share, save and exit, terminate, and find results.

End-user guides with screenshots are in the MESA documentation:
<https://idss-mesa.github.io/docs/portal/>.[^portal-docs] The featured apps it
launches are [MESA CLI](cli.md), [MESA JupyterLab](jupyterlab.md),
[MESA RStudio Geospatial](rstudio.md), [MESA VS Code](vscode.md), and
[MESA KASM Ubuntu Desktop](kasm.md).

The repository is **private**: its `resource` URL returns 404 outside the
idss-mesa organization, so do not send users there; send them to the portal
and its guides instead.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^portal]: MESA Portal
[^portal-docs]: MESA Portal guides (MESA documentation)
