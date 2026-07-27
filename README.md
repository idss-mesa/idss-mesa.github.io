# idss-mesa.github.io

Landing site for **MESA — Multidisciplinary Environment for Scientific Advancement** (NSF Award [#2632685](https://www.nsf.gov/awardsearch/show-award/?AWD_ID=2632685), Integrated Data Systems & Services).

Static HTML/CSS, no build step.

- `index.html` — landing page
- `hiring.html` — open positions at UNM
- `styles.css` — Modernist design tokens + components
- `assets/team/` — team headshots

## Deploy on GitHub Pages

For the org home page, name the repo `idss-mesa/idss-mesa.github.io` and enable Pages (deploy from branch, root). The site serves at https://idss-mesa.github.io/.
(If the repo is `idss-mesa/idss-mesa` instead, Pages serves at https://idss-mesa.github.io/idss-mesa/ — links are relative, so both work.)

## Local preview

```bash
python3 -m http.server   # http://localhost:8000
```
