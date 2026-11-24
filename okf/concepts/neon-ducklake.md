---
type: Software Repository
title: "neon-ducklake"
description: "NEON Data API metadata lakehouse and fully annotated NEON site data as one MESA project on the CyVerse Data Store, published read-only: DuckDB ducklake-extension lakes plus the project's mesa-ducklake AVU history"
resource: https://github.com/idss-mesa/neon-ducklake
tags: [software, dataset, neon, ecology, ducklake, irods, python]
status: stable
stale_after: "2027-05-24T00:00:00Z"
generated: { by: "claude/opus-5.5", at: "2026-11-24T00:00:00Z" }
sources:
  - id: neon-ducklake-repo
    resource: https://github.com/idss-mesa/neon-ducklake
    title: "idss-mesa/neon-ducklake repository"
    author: "team:idss-mesa"
  - id: neon-ducklake-collection
    resource: https://data.cyverse.org/dav-anon/iplant/home/tswetnam/neon-ducklake/
    title: "neon-ducklake project collection on the CyVerse Data Store (anonymous read)"
    author: "team:idss-mesa"
---

# neon-ducklake

A pipeline and its published output.[^neon-ducklake-repo] It harvests the
NEON Data API into a DuckLake (Phase 1, the catalog lake: products, sites,
releases, availability, locations, taxonomy and an inventory of about 3.2
million data files). It then downloads, stacks and fully annotates NEON site
data into one DuckLake per site (Phase 2), all inside a single MESA project
on the CyVerse Data Store. Version 0.1.0: Phase 1 is complete, and Phase 2
has run for some sites. Built with DuckDB 1.5.5 and the `ducklake`
extension. MIT licence. It is not affiliated with NEON, Battelle or NSF.

The project collection is readable without an account at
<https://data.cyverse.org/dav-anon/iplant/home/tswetnam/neon-ducklake/>.[^neon-ducklake-collection]
It holds two different kinds of "ducklake":

- `ducklake/neon_catalog.ducklake` plus `ducklake/data/`, and
  `sites/<SITE>/ducklake/neon_<site>.ducklake` plus `data/`, are DuckDB
  `ducklake`-extension lakes. Attach them read-only, in place over HTTPS
  (`ATTACH 'ducklake:<url>' (READ_ONLY, DATA_PATH '<url>/data/',
  OVERRIDE_DATA_PATH true)`), or from a local copy that keeps each
  `.ducklake` file with its `data/`.
- `.mesa/ducklake/snapshot_<id>.parquet` is the project's AVU history,
  written by [mesa-ducklake](mesa-ducklake.md). It is plain Parquet, read
  with `read_parquet`, and is not an extension lake.

Every lake is built locally and then uploaded: `CHECKPOINT; DETACH`, then
`data/**` with checksum verification, then the `.ducklake` file last. The
repository README's "Reading the published lakes" section has tested
examples.

For live NEON data rather than this snapshot of it, use
[neon-mcp](neon-mcp.md).

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^neon-ducklake-repo]: idss-mesa/neon-ducklake repository
[^neon-ducklake-collection]: neon-ducklake project collection on the CyVerse Data Store (anonymous read)
