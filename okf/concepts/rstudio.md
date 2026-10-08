---
type: Software Repository
title: "MESA RStudio Geospatial"
description: "RStudio Server on the Rocker geospatial stack for CyVerse VICE, with AI coding-agent CLIs and the MESA MCP servers"
resource: https://github.com/idss-mesa/rstudio
tags: [software, vice, rstudio, r, geospatial, gpu]
status: stable
generated: { by: "claude-code/2.1.294", at: "2026-10-08T00:00:00Z" }
stale_after: "2027-04-08T00:00:00Z"
sources:
  - id: rstudio-readme
    resource: https://github.com/idss-mesa/rstudio/blob/main/README.md
    title: "MESA RStudio Geospatial README"
    author: "team:idss-mesa"
  - id: app-docs
    resource: https://idss-mesa.github.io/docs/apps/rstudio/
    title: "MESA RStudio Geospatial (MESA documentation)"
    author: "team:idss-mesa"
---

# MESA RStudio Geospatial

[RStudio Server](https://posit.co/products/open-source/rstudio-server/) on
the Rocker geospatial stack (R, tidyverse, sf, terra, stars, GDAL, PROJ,
GEOS), run as a CyVerse Discovery Environment (VICE) app, with Claude Code,
Codex, OpenCode, and Antigravity installed and the `irods`, `mesa`,
`formation`, and `filesystem` MCP servers registered.[^rstudio-readme]

- **Image:** `harbor.cyverse.org/vice/mesa-rstudio:latest`; GPU build `:gpu`
  adds R torch, GPU xgboost, reticulate/keras3, and a local Ollama server with
  the ollamar, ellmer, and mall R packages.
- **Port and working directory:** 80 (nginx in front of RStudio);
  `/home/rstudio/data-store`.

Launch it from the [MESA Portal](mesa-portal.md) at
<https://mesa.cyverse.org/applications/> (MESA Apps tab) or from the CyVerse
Discovery Environment. User guide:
<https://idss-mesa.github.io/docs/apps/rstudio/>.[^app-docs] Every MESA
app shares the agent setup described at
<https://idss-mesa.github.io/docs/apps/agents/>.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^rstudio-readme]: MESA RStudio Geospatial README
[^app-docs]: MESA RStudio Geospatial (MESA documentation)
