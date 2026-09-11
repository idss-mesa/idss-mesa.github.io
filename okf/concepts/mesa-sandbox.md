---
type: Software Repository
title: "mesa-sandbox"
description: "AI sandboxes for CyVerse VICE: a sudo-free multi-arch image family, sandbox profiles P0–P4, an OpenBao credential broker and egress proxy, and agent-sandbox pods for autonomous agents"
resource: https://github.com/idss-mesa/mesa-sandbox
tags: [software, sandboxing, vice, kubernetes, agents]
status: stable
generated: { by: "claude/opus-5", at: "2026-09-10T00:00:00Z" }
stale_after: "2026-12-10T00:00:00Z"
sources:
  - id: mesa-sandbox-readme
    resource: https://github.com/idss-mesa/mesa-sandbox/blob/main/README.md
    title: "mesa-sandbox README"
    author: "team:idss-mesa"
    last_modified: "2026-09-06T00:00:00Z"
---

# mesa-sandbox

AI sandboxes for CyVerse VICE, the Discovery Environment's interactive
Kubernetes pods (JupyterLab, RStudio Server, VS Code Server, a Kasm Ubuntu
desktop, a tmux CLI). Those images carry AI coding agents and the MESA MCP
servers; this repository is the plan and implementation for running the
agents **with the user's permissions but without the user's secrets**,
autonomously, at explicit sandbox levels.[^mesa-sandbox-readme]

- **Design.** The VICE analysis pod stays the human's workbench; each
  autonomous agent job runs as a separate pod with its own UID, service
  account, lifetime, credentials, and egress policy, sharing only the
  workspace volume. An OpenBao broker issues short-lived credentials and an
  egress-proxy sidecar injects them only for allow-listed hosts.
- **Profiles.** A normative sandbox taxonomy, P0–P4, fixes runtime, egress,
  credentials, autonomy, and data class per level.
- **Images.** One hardened, sudo-free, digest-pinned image family for amd64
  and arm64, published to `harbor.cyverse.org/vice/mesa-*`.
- **Status (2026-09-06).** Phase 0 complete, Phase 2 mostly built, Phase 3
  drafted; the Kubernetes profiles are untested on a cluster. Re-check the
  README after this document's `stale_after` date.

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^mesa-sandbox-readme]: mesa-sandbox README
