---
type: Software Repository
title: "mesa-clm"
description: "Calibrated, ontology-grounded AVU proposals for the MESA stack with Contrastive LM (CLM): rank-first decisions with an abstain anchor over mesa-mcp's OBO/OLS tools, each recorded in a provenance sidecar next to the mesa-ducklake AVU history"
resource: https://github.com/idss-mesa/mesa-clm
tags: [software, ontology, metadata, machine-learning, python]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-11-24T00:00:00Z" }
sources:
  - id: mesa-clm-repo
    resource: https://github.com/idss-mesa/mesa-clm
    title: "idss-mesa/mesa-clm repository"
    author: "team:idss-mesa"
  - id: mesa-clm-docs
    resource: https://idss-mesa.github.io/mesa-clm/
    title: "mesa-clm documentation"
    author: "team:idss-mesa"
---

# mesa-clm

Proposes calibrated, ontology-grounded AVUs for the MESA stack with
Contrastive LM (CLM).[^mesa-clm-repo] Decisions are rank-first with a fixed
abstain anchor over [mesa-mcp](mesa-mcp.md)'s OBO/OLS ontology tools, scored
by a frozen Qwen3-8B encoder and CLM's projection heads, fingerprinted and
pre-registered. Every decision is recorded in a provenance sidecar next to the
[mesa-ducklake](mesa-ducklake.md) AVU history.

Documentation, published as its own OKF v0.2 bundle, is at
<https://idss-mesa.github.io/mesa-clm/>:[^mesa-clm-docs]

- Outline: <https://idss-mesa.github.io/mesa-clm/llms.txt>
- Full corpus: <https://idss-mesa.github.io/mesa-clm/llms-full.txt>
- Agent guide: <https://idss-mesa.github.io/mesa-clm/about/ai-agents/>

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^mesa-clm-repo]: idss-mesa/mesa-clm repository
[^mesa-clm-docs]: mesa-clm documentation
