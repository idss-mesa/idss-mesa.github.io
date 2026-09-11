# Bundle Update Log

## 2026-09-10
* **Update**: Rewrote [MESA](concepts/home.md) and [MESA Hiring](concepts/hiring.md) as full Markdown twins of their pages — layers, goals, stack, connectors, team, news, and every open position — with `sources` and `stale_after` (the hiring twin goes stale on 2026-12-10).
* **Creation**: Added [For AI agents](concepts/ai-agents.md), the agent guide rendered at <https://idss-mesa.github.io/about/ai-agents/>, modelled on the CARC and neon-mcp guides.
* **Creation**: Added the public [neon-mcp](concepts/neon-mcp.md) and [mesa-sandbox](concepts/mesa-sandbox.md) repositories.
* **Update**: Marked [mesa-portal](concepts/mesa-portal.md) and [mesa-forge](concepts/mesa-forge.md) `visibility: private`: their repositories are not public, so their links return 404.
* **Update**: Refreshed [MESA MCP Stack Documentation](concepts/docs.md) for its four agent clients and its agent endpoints.
* **Update**: Links to files outside the bundle are now absolute URLs (a leading `/` is bundle-relative under OKF §6.1, so `/robots.txt` pointed inside `okf/`), and links between concepts are plain relative paths, which resolve both as bundle paths and over HTTP.
* **Update**: `robots.txt` now follows the CARC agent-ready policy (named AI fetchers, sub-site sitemaps, agent pointers); `llms.txt`, `llms-full.txt`, `sitemap.xml`, and each page's `okf:*` head tags are generated from this bundle by `scripts/gen_agent_surface.py` and checked in CI along with `scripts/okf_validate.py`.

## 2026-08-30
* **Creation**: Established this OKF v0.2 bundle at [index.md](index.md), with concept documents for the MESA site, documentation, and software repositories under `okf/concepts/`.
* **Creation**: Added a site-wide permissive [robots.txt](https://idss-mesa.github.io/robots.txt) explicitly welcoming AI and agentic crawlers to all content on this origin.
