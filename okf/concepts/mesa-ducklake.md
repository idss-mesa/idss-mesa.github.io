---
type: Software Repository
title: "mesa-ducklake"
description: "AVU metadata-history library for MESA projects: a Postgres or DuckDB catalog plus one plain Parquet file per snapshot in each project's .mesa/ducklake/ collection (the DuckLake pattern, not the DuckDB ducklake extension)"
resource: https://github.com/idss-mesa/mesa-ducklake
tags: [software, ducklake, metadata-history, irods, python]
status: stable
generated: { by: "claude/opus-5.5", at: "2026-11-24T00:00:00Z" }
sources:
  - id: mesa-ducklake-repo
    resource: https://github.com/idss-mesa/mesa-ducklake
    title: "idss-mesa/mesa-ducklake repository"
    author: "team:idss-mesa"
  - id: mesa-ducklake-docs-page
    resource: https://idss-mesa.github.io/docs/servers/mesa-ducklake/
    title: "mesa-ducklake page in the MESA documentation"
    author: "team:idss-mesa"
---

# mesa-ducklake

The Python library that records the history of AVU (attribute–value–unit)
metadata changes for MESA-enabled iRODS projects, and that
[mesa-mcp](mesa-mcp.md) imports in-process.[^mesa-ducklake-repo] Every change
is an append-only row with provenance (actor, source, ticket, rule), which
makes time-travel reads possible: the AVUs on a path as of any past moment.

It follows the DuckLake *pattern*, a SQL catalog indexing immutable Parquet
snapshots. It does **not** use the DuckDB `ducklake` extension:

- The catalog is Postgres, or one DuckDB file for a local install. It is not
  stored in iRODS.
- Each snapshot is a plain `snapshot_<id>.parquet` in the project's
  `.mesa/ducklake/` collection. Every row carries its `project_id`,
  `snapshot_id`, `ts`, `actor`, `source` and `op`, so `read_parquet` reads
  the history without the catalog. `ATTACH 'ducklake:…'` does not open it.
- Files are written to a local cache, pushed to iRODS with a checksum check,
  and only then committed in the catalog, because DuckDB can't write to iRODS.

A project can also hold its own extension-format DuckLake of science data,
such as [neon-ducklake](neon-ducklake.md)'s `ducklake/neon_catalog.ducklake`.
That lake is separate from the project's `.mesa/ducklake/` history.

Documentation: the repository's `docs/`, in particular
<https://github.com/idss-mesa/mesa-ducklake/blob/main/docs/dev/architecture.md>
(including porting the history to the extension) and
<https://github.com/idss-mesa/mesa-ducklake/blob/main/docs/deploy/per-project-storage.md>
(reading a project's history without the catalog), plus the summary page at
<https://idss-mesa.github.io/docs/servers/mesa-ducklake/>.[^mesa-ducklake-docs-page]

Part of MESA (Multidisciplinary Environment for Scientific Advancement),
an NSF IDSS Category II project at the University of New Mexico; see
[MESA](home.md). Organization: <https://github.com/idss-mesa>.

[^mesa-ducklake-repo]: idss-mesa/mesa-ducklake repository
[^mesa-ducklake-docs-page]: mesa-ducklake page in the MESA documentation
