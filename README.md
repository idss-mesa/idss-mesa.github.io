# idss-mesa.github.io

Landing site for **MESA — Multidisciplinary Environment for Scientific Advancement** (NSF Award [#2632685](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2632685), Integrated Data Systems & Services).

Static HTML/CSS, no build step.

- `index.html` — landing page
- `hiring.html` — open positions at UNM
- `about/ai-agents/` — the For AI agents guide
- `styles.css` — Modernist design tokens + components
- `assets/team/` — team headshots

## Agent-ready

The site is published for people and for AI agents, following the
[UNM CARC documentation](https://carc.unm.edu/docs/about/ai-agents/) conventions:

- `robots.txt` — fully permissive, names AI fetchers; it governs the whole origin, including the `/docs/` and `/neon-mcp/` sub-sites
- `okf/` — an [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundle; each page's Markdown twin lives in `okf/concepts/`
- `llms.txt`, `llms-full.txt`, `sitemap.xml`, and the `okf:*` tags in each page's `<head>` — generated from `okf/` by `scripts/gen_agent_surface.py`

```bash
pip install pyyaml
python3 scripts/okf_validate.py okf    # OKF conformance
python3 scripts/gen_agent_surface.py   # regenerate the agent surface after editing okf/
```

CI (`.github/workflows/okf.yml`) runs both and fails on drift. Coding agents: see [AGENTS.md](AGENTS.md).

## Deploy on GitHub Pages

For the org home page, name the repo `idss-mesa/idss-mesa.github.io` and enable Pages (deploy from branch, root). The site serves at https://idss-mesa.github.io/.
(If the repo is `idss-mesa/idss-mesa` instead, Pages serves at https://idss-mesa.github.io/idss-mesa/ — page links are relative, so both work, but the absolute URLs in `robots.txt`, `llms.txt`, and `okf/` assume the org home page.)

## Local preview

```bash
python3 -m http.server   # http://localhost:8000
```
