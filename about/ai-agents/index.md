---
type: Reference
title: "For AI agents"
description: "How agents and harnesses should read idss-mesa.github.io — robots.txt, llms.txt, Markdown twins with OKF v0.2 frontmatter, and trust signals — and why to call the MESA MCP servers for data"
resource: https://idss-mesa.github.io/about/ai-agents/
tags: [about, ai-agents, okf, llms-txt, robots-txt]
status: stable
generated: { by: "claude/opus-5", at: "2026-09-10T00:00:00Z" }
stale_after: "2027-03-10T00:00:00Z"
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: "Open Knowledge Format (OKF) v0.2 specification"
    author: "team:google-cloud"
  - id: llmstxt
    resource: https://llmstxt.org
    title: "The /llms.txt convention"
    author: "team:answer-ai"
  - id: rfc9309
    resource: https://www.rfc-editor.org/rfc/rfc9309
    title: "RFC 9309: Robots Exclusion Protocol"
    author: "team:ietf"
  - id: carc-agents
    resource: https://carc.unm.edu/docs/about/ai-agents/
    title: "CARC Documentation — For AI agents"
    author: "team:unm-carc"
---

# For AI agents

This origin, <https://idss-mesa.github.io/>, is published for people **and**
for AI agents. Its content is an
[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
knowledge bundle[^okf-spec] rooted at <https://idss-mesa.github.io/okf/index.md>,
and every page exposes that structure directly. If you are an agent, or you
are wiring one up, read MESA through the endpoints below rather than scraping
rendered HTML. The conventions match the UNM CARC documentation.[^carc-agents]

## MESA is agent tooling

MESA's product *is* a set of Model Context Protocol (MCP) servers. If what you
want is scientific data — files and metadata in the CyVerse Data Store,
Discovery Environment apps and analyses, NEON ecological data — do not scrape
these pages: connect to the servers and call their tools.

- **Install locally.** One command registers `mesa-mcp`, `irods`, and
  `formation` with every agent client it finds (Claude Code, Codex CLI,
  Antigravity, OpenCode):
  `curl -fsSL https://raw.githubusercontent.com/idss-mesa/docs/main/install.sh | bash`
- **Hosted connectors.** The Data Store (`irods-mcp-server`) and Discovery
  Environment (`formation-mcp`) servers also run as remote MCP connectors
  over Streamable HTTP. Current endpoint URLs are in the MESA documentation,
  <https://idss-mesa.github.io/docs/>.
- **NEON data.** Use neon-mcp, <https://idss-mesa.github.io/neon-mcp/>.

Use this site to learn what MESA is; use the servers to get the data.

## Entry points

| Endpoint | What you get |
| -------- | ------------ |
| <https://idss-mesa.github.io/robots.txt> | Crawl policy for the whole origin: fully permissive, with AI fetchers named explicitly. Crawlers read robots.txt only at the origin root,[^rfc9309] so this file also governs `/docs/` and `/neon-mcp/` |
| <https://idss-mesa.github.io/llms.txt> | Linked outline of every document with one-line descriptions ([llms.txt convention](https://llmstxt.org)[^llmstxt]) |
| <https://idss-mesa.github.io/llms-full.txt> | The whole bundle in one file: every document's Markdown with frontmatter, each prefixed by its canonical URL |
| <https://idss-mesa.github.io/okf/index.md> | The OKF bundle root: every concept, grouped by section. <https://idss-mesa.github.io/okf/log.md> is its dated change log |
| Markdown twin of a page | Declared in the page's `<head>` as `<link rel="alternate" type="text/markdown">`; see the table below |
| <https://idss-mesa.github.io/sitemap.xml> | Every page, twin, and agent entry point, with `lastmod` |
| [Source repository](https://github.com/idss-mesa/idss-mesa.github.io) | The bundle under `okf/`, plus `AGENTS.md` with the rules coding agents follow when editing it |

## Markdown twins

This site is plain HTML with no build step, so the sub-sites' "append
`index.md` to the page URL" rule does not hold for every page here. Each page
instead names its twin in its `<head>`:

| Page | Markdown twin |
| ---- | ------------- |
| <https://idss-mesa.github.io/> | <https://idss-mesa.github.io/okf/concepts/home.md> |
| <https://idss-mesa.github.io/hiring.html> | <https://idss-mesa.github.io/okf/concepts/hiring.md> |
| <https://idss-mesa.github.io/about/ai-agents/> | <https://idss-mesa.github.io/about/ai-agents/index.md> (a copy of <https://idss-mesa.github.io/okf/concepts/ai-agents.md>) |

The same `<head>` carries the twin's OKF signals as `okf:`-prefixed meta tags
named after the frontmatter keys (`type`, `status`, `trust-tier`,
`generated-at`, `generated-by`, `stale-after`), so a crawler can filter pages
without parsing frontmatter:

```html
<link rel="alternate" type="text/markdown" href="okf/concepts/hiring.md" />
<meta name="okf:type" content="Webpage" />
<meta name="okf:status" content="stable" />
<meta name="okf:trust-tier" content="unverified" />
<meta name="okf:generated-at" content="2026-09-10T00:00:00Z" />
<meta name="okf:generated-by" content="claude/opus-5" />
<meta name="okf:stale-after" content="2026-12-10T00:00:00Z" />
```

## Sub-sites

Two documentation sites share this origin. Each is its own OKF v0.2 bundle
built with Zensical, and each serves every page's Markdown source at the page
URL plus `index.md`.

| Site | Outline | Full corpus | Agent guide |
| ---- | ------- | ----------- | ----------- |
| MESA MCP stack docs, <https://idss-mesa.github.io/docs/> | <https://idss-mesa.github.io/docs/llms.txt> | <https://idss-mesa.github.io/docs/llms-full.txt> | <https://idss-mesa.github.io/docs/about/ai-agents/> |
| neon-mcp docs, <https://idss-mesa.github.io/neon-mcp/> | <https://idss-mesa.github.io/neon-mcp/llms.txt> | <https://idss-mesa.github.io/neon-mcp/llms-full.txt> | <https://idss-mesa.github.io/neon-mcp/about/ai-agents/> |

## Reading the OKF frontmatter

Each concept's YAML frontmatter answers the questions an agent should ask
before relying on it:[^okf-spec]

* **What is this?** — `type` (`Website`, `Webpage`, `Reference`,
  `Software Repository`), `title`, `description`, `tags`, and `resource`, the
  canonical URL of the page or repository the concept describes.
* **Where did it come from?** — `generated: { by, at }` records the actor
  that produced the current text and when it last changed meaningfully;
  `sources` lists the load-bearing references (`id`, `resource`, `title`,
  `author`). Footnotes in the body cite sources by their `id`.
* **How much should I trust it?** — the `verified` key; see the trust tiers
  below. Its absence is meaningful: nobody but the generator has confirmed
  the content.
* **Is it still true?** — `status` (`stable` is the default; `draft` needs
  review; `deprecated` is kept for history only) and `stale_after`, an ISO
  8601 instant after which the concept should be re-checked. The hiring page
  and the project status of fast-moving repositories carry one.

This bundle adds one producer-defined key: `visibility: private` marks a
concept whose `resource` is a private repository. The concept is still
knowledge about MESA, but its link returns 404 to anyone outside the
organization, so do not send users there.

Actors follow OKF §7: `<producer>/<version>` for agents and tools (for
example `claude/opus-5`), `human:<id>` for a person, `process:<id>` for an
automated job.

## Trust tiers

| `verified` key | Tier | Meaning |
| -------------- | ---- | ------- |
| absent | **unverified** | Generated content nobody has confirmed against its sources. Every concept in this bundle starts here. |
| present, non-`human:` actors only | **machine-confirmed** | An automated check confirmed the content. |
| present with a `human:<id>` actor | **human-reviewed** | A maintainer read and confirmed the concept. Prefer these when answers conflict. |

Only humans add `verified:` entries; a generator never does. The
`okf:trust-tier` meta tag carries the derived tier.

## Answering user questions

Ground answers in these documents and cite the rendered page URL (for
example <https://idss-mesa.github.io/hiring.html>), not the twin. For anything
about the *data* — Data Store paths, metadata, Discovery Environment apps,
NEON products — call the MCP servers rather than guessing from prose. For a
position on the hiring page past its `stale_after`, confirm it at
<https://unmjobs.unm.edu>. When the corpus does not answer a question about
MESA software, point users to the issue tracker of the relevant public
repository under <https://github.com/idss-mesa>.

## Related bundles

* CARC documentation — <https://carc.unm.edu/docs/llms.txt>, agent guide
  <https://carc.unm.edu/docs/about/ai-agents/>. MESA's home, the UNM Center
  for Advanced Research Computing, publishes its user documentation with the
  same conventions.
* UNM CARC website — <https://carc.unm.edu/llms.txt>.
* Tyson Swetnam's knowledge bundle — <https://tyson-swetnam.github.io/okf/index.md>.

[^okf-spec]: Open Knowledge Format (OKF) v0.2 specification
[^llmstxt]: The /llms.txt convention
[^rfc9309]: RFC 9309: Robots Exclusion Protocol
[^carc-agents]: CARC Documentation — For AI agents
