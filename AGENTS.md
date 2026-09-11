# Agent guide — idss-mesa.github.io

This repository is the landing site for **MESA** (Multidisciplinary
Environment for Scientific Advancement), served at https://idss-mesa.github.io/
straight from the `main` branch: static HTML and CSS, no build step. It also
holds the origin's agent surface. `okf/` is an **Open Knowledge Format (OKF)
v0.2 knowledge bundle**
([spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)):
every concept under `okf/concepts/` carries YAML frontmatter with `type`,
`title`, `description`, `resource`, `tags`, provenance (`generated`,
`sources`), and lifecycle (`status`, `stale_after`) fields. `okf/index.md` is
the OKF §8 bundle-root listing and `okf/log.md` the OKF §9 dated change log.

`robots.txt` here is the only one crawlers honor on this origin, so it also
governs the project sub-sites `/docs/` (repo `idss-mesa/docs`) and
`/neon-mcp/` (repo `idss-mesa/neon-mcp`), which are separate OKF bundles.

## Reading the corpus

- `llms.txt` — linked outline of every concept with descriptions.
- `llms-full.txt` — the whole bundle in one file, frontmatter included.
- Each HTML page's Markdown twin is a concept, declared in the page's
  `<head>` as `<link rel="alternate" type="text/markdown">`. The agent guide,
  `about/ai-agents/`, also serves its twin at `about/ai-agents/index.md`.
- Trust: concepts without a `verified:` key are **unverified** (OKF §5.3).
  `visibility: private` marks a concept whose repository is not public.

## Commands

```bash
pip install pyyaml
python3 scripts/okf_validate.py okf      # OKF conformance (CI-enforced; 0 errors required)
python3 scripts/gen_agent_surface.py     # regenerate llms.txt, llms-full.txt, sitemap.xml,
                                         # about/ai-agents/index.md, and each page's okf:* head block
python3 -m http.server                   # preview at http://localhost:8000
```

## Editing rules

1. **Pages and twins change together.** `index.html` ↔ `okf/concepts/home.md`,
   `hiring.html` ↔ `okf/concepts/hiring.md`, `about/ai-agents/index.html` ↔
   `okf/concepts/ai-agents.md`. When you change a page's content, update its
   twin in the same commit, bump `generated.at`, and set `generated.by`.
2. **A new page** gets a twin concept, an entry in the `PAGES` map of
   `scripts/gen_agent_surface.py`, a bullet in `okf/index.md`, and the
   `<!-- okf:begin --><!-- okf:end -->` marker in its `<head>`.
3. **Never hand-edit generated files:** `llms.txt`, `llms-full.txt`,
   `sitemap.xml`, `about/ai-agents/index.md`, and the `okf:begin` … `okf:end`
   blocks. Run `gen_agent_surface.py` and commit its output; CI fails on drift.
4. **Every concept** starts with frontmatter: a non-empty `type`, plus
   `title`, `description` (one sentence), `resource`, `tags`,
   `generated: { by, at }`, and `sources` (`id`, `resource`, `title`,
   `author`) with body footnotes keyed by `id`. Add `stale_after` when the
   concept states facts that expire (open positions, project status).
5. **`okf/index.md`** carries only `okf_version`, `title`, and `description`
   as frontmatter. Its bullets must list every concept, and each bullet's
   description must match the concept's frontmatter; the generator refuses
   to run otherwise.
6. **Links:** between concepts, use plain relative paths (`hiring.md` from
   another concept, `concepts/hiring.md` from `okf/index.md` or `okf/log.md`).
   They resolve both as OKF bundle paths and over HTTP. Don't use a leading
   `/`: OKF §6.1 reads it as the bundle root (`okf/`), but a browser or agent
   fetching the file reads it as the origin root, and the link 404s. Link
   anything outside `okf/` (robots.txt, pages, sub-sites) by absolute URL.
7. **`okf/log.md`** gets a dated entry (`## YYYY-MM-DD`, newest first;
   `* **Creation**:` / `* **Update**:` / `* **Deprecation**:`) for every
   substantive change.
8. **Actors** (OKF §7): `<producer>/<version>` for an agent or tool (for
   example `claude/opus-5`), `human:<id>` for a person, `process:<id>` for an
   automated job.
9. **Never add `verified:`.** Only a human maintainer does that, as
   `verified: { by: "human:<id>", at: <ISO 8601> }`.
10. **Pages** use `styles.css` for tokens and components and keep their
    layout in a page-level `<style>`. Check new layouts at phone width
    (~400px): the nav drops its section anchors below 480px.
11. **robots.txt** stays fully permissive. Keep its AI-fetcher list aligned
    with the UNM-CARC/docs and neon-mcp lists, and keep the `Sitemap:` lines
    for the sub-sites.
