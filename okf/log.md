# Bundle Update Log

## 2026-10-08
* **Update**: [MESA](concepts/home.md) and its page: the stack says Formation asks for a CyVerse sign-in once in each agent client; "Featured connectors" notes that the public Data Store connector needs no sign-in, that the Free plan allows one custom connector, and that claude.ai connectors reach Claude Code only when it is signed in with a claude.ai subscription; the `claude mcp add` lead-in covers an older local formation entry, and the connector steps name the Register automatically OAuth client for Formation. [Formation (hosted MCP server)](concepts/formation-mcp.md) says its Codex, OpenCode, and Antigravity sign-in is not yet confirmed.
* **Update**: [Formation (hosted MCP server)](concepts/formation-mcp.md) (formerly formation-mcp) now describes CyVerse's hosted Discovery Environment server at <https://de.cyverse.org/formation/mcp>, its CyVerse sign-in, tools, and clients; the stdio formation-mcp it replaced stopped working when CyVerse removed Formation's REST API in mid-2026 (Formation release v2026.07.07).
* **Update**: [MESA](concepts/home.md) and its page: the stack table lists Formation as hosted by CyVerse, and "Featured connectors" gives the real endpoints (`https://de.cyverse.org/formation/mcp`, `https://mcp-public.cyverse.ai/mcp`), the current claude.ai menu (Customize → Connectors), and working `claude mcp add` commands in place of placeholders.
* **Update**: [For AI agents](concepts/ai-agents.md) and its page name the hosted Formation endpoint; [MESA Documentation](concepts/docs.md) covers Formation and the claude.ai connector guide.
* **Update**: [MESA](concepts/home.md) and its page gained an "In your browser" section for the MESA Portal at <https://mesa.cyverse.org> and its five featured apps, an **Open the MESA Portal** button, and a **Portal** anchor in the navigation.
* **Update**: [mesa-portal](concepts/mesa-portal.md) now describes the live portal at <https://mesa.cyverse.org> (Data Browser, Applications, Analyses) and points to its end-user guides at <https://idss-mesa.github.io/docs/portal/>; the repository stays private.
* **Creation**: Added the featured-app repositories [MESA JupyterLab](concepts/jupyterlab.md), [MESA RStudio Geospatial](concepts/rstudio.md), [MESA VS Code](concepts/vscode.md), and [MESA KASM Ubuntu Desktop](concepts/kasm.md), and expanded [MESA CLI](concepts/cli.md), each linking its user guide under <https://idss-mesa.github.io/docs/apps/>.
* **Update**: Renamed [MESA Documentation](concepts/docs.md) (formerly MESA MCP Stack Documentation) now that the docs also cover the portal and the featured apps.

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
