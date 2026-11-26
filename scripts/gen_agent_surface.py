#!/usr/bin/env python3
"""Regenerate the agent surface of idss-mesa.github.io from its OKF bundle.

The landing site is static HTML deployed straight from the branch, with no
build step, so everything an agent reads is generated here and committed. CI
fails when any of it drifts from okf/ (`git diff --exit-code`).

  llms.txt                  linked outline (llmstxt.org) of every concept, in
                            okf/index.md order, linking the Markdown twins
  llms-full.txt             the whole bundle in one file, frontmatter included
  sitemap.xml               pages, twins, and agent entry points
  about/ai-agents/index.md  copy of okf/concepts/ai-agents.md, so that page
                            also honors the sub-sites' "page URL + index.md"
  okf:begin ... okf:end     a block in each page's <head>: <link
                            rel="alternate" type="text/markdown"> to its twin
                            plus okf:* meta tags from the twin's frontmatter

It refuses to write anything when okf/index.md and the concepts disagree: a
concept that is not listed, a listing with no file, or a listed description
that differs from the concept's frontmatter.

Usage: python3 scripts/gen_agent_surface.py   (from the repository root; needs PyYAML)
"""

from __future__ import annotations

import datetime
import html
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "okf"
BASE = "https://idss-mesa.github.io/"

# Each HTML page and the concept that is its Markdown twin.
PAGES = {
    "index.html": "concepts/home.md",
    "portal.html": "concepts/portal.md",
    "stack.html": "concepts/stack.md",
    "team.html": "concepts/team.md",
    "news.html": "concepts/news.md",
    "hiring.html": "concepts/hiring.md",
    "about/ai-agents/index.html": "concepts/ai-agents.md",
}
# Twins also copied next to their page, where page URL + index.md serves them.
MIRRORS = {"concepts/ai-agents.md": "about/ai-agents/index.md"}

# The documentation sub-sites on this origin, each its own OKF bundle; see
# subsites.yml (kept current by scripts/discover_subsites.py).
SUBSITES_FILE = ROOT / "subsites.yml"
RELATED = [
    ("CARC documentation", "https://carc.unm.edu/docs/llms.txt",
     "UNM Center for Advanced Research Computing user documentation, an OKF v0.2 "
     "bundle with the same agent conventions; agent guide "
     "https://carc.unm.edu/docs/about/ai-agents/"),
    ("UNM CARC website", "https://carc.unm.edu/llms.txt",
     "the Center for Advanced Research Computing, MESA's home at UNM"),
    ("Tyson Swetnam knowledge bundle", "https://tyson-swetnam.github.io/okf/index.md",
     "OKF bundle of the MESA principal investigator"),
]

BLOCK_RE = re.compile(r"<!-- okf:begin.*?<!-- okf:end -->\n?", re.DOTALL)
BULLET_RE = re.compile(r"^\*\s+\[([^\]]+)\]\(([^)]+)\)\s+-\s+(.*)$")


def split(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return {}, text
    data = yaml.safe_load(m.group(1)) or {}
    return (data if isinstance(data, dict) else {}), text[m.end():]


def iso(value) -> str:
    """Frontmatter timestamps may parse as datetimes; emit them as ISO 8601 UTC."""
    if isinstance(value, datetime.datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        return value.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if isinstance(value, datetime.date):
        return value.isoformat()
    return str(value) if value else ""


def trust_tier(fm: dict) -> str:
    """OKF §5.3: unverified | machine-confirmed | human-reviewed."""
    v = fm.get("verified")
    if not v:
        return "unverified"
    entries = v if isinstance(v, list) else [v]
    actors = [str(e.get("by", "")) for e in entries if isinstance(e, dict)]
    if any(a.startswith("human:") for a in actors):
        return "human-reviewed"
    return "machine-confirmed" if actors else "unverified"


def generated(fm: dict) -> dict:
    gen = fm.get("generated")
    return gen if isinstance(gen, dict) else {}


def sentence(text) -> str:
    t = " ".join(str(text or "").split()).rstrip(".")
    return t + "." if t else ""


def read_index() -> list[tuple[str, list[tuple[str, str, str]]]]:
    """okf/index.md -> [(section heading, [(title, concept path, description)])]."""
    sections: list[tuple[str, list]] = []
    for line in (BUNDLE / "index.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            sections.append((line[2:].strip(), []))
        elif sections and (m := BULLET_RE.match(line)):
            sections[-1][1].append(m.groups())
    return [s for s in sections if s[1]]


def check_index(sections, concepts: dict) -> list[str]:
    problems = []
    listed = {rel for _, items in sections for _, rel, _ in items}
    for rel in sorted(set(concepts) - listed):
        problems.append(f"okf/{rel}: not listed in okf/index.md")
    for _, items in sections:
        for _, rel, desc in items:
            fm = concepts.get(rel)
            if fm is None:
                problems.append(f"okf/index.md: lists {rel}, which does not exist")
            elif " ".join(desc.split()) != " ".join(str(fm.get("description", "")).split()):
                problems.append(f"okf/index.md: description of {rel} differs from its frontmatter")
    for page, rel in PAGES.items():
        if not (ROOT / page).exists():
            problems.append(f"{page}: listed in PAGES but missing")
        if rel not in concepts:
            problems.append(f"{page}: twin okf/{rel} missing")
    return problems


def page_url(page: str) -> str:
    return BASE + (page[: -len("index.html")] if page.endswith("index.html") else page)


def twin_href(page: str, rel: str) -> str:
    target = ROOT / MIRRORS[rel] if rel in MIRRORS else BUNDLE / rel
    return os.path.relpath(target, (ROOT / page).parent).replace(os.sep, "/")


def head_block(page: str, rel: str, fm: dict) -> str:
    lines = [
        f"<!-- okf:begin — generated by scripts/gen_agent_surface.py from okf/{rel}; do not edit -->",
        '<meta name="robots" content="index, follow, max-snippet:-1, '
        'max-image-preview:large, max-video-preview:-1" />',
        '<link rel="alternate" type="text/markdown" title="Markdown source (OKF v0.2 frontmatter)" '
        f'href="{twin_href(page, rel)}" />',
    ]

    def meta(name, value):
        if value:
            lines.append(f'<meta name="{name}" content="{html.escape(str(value), quote=True)}" />')

    meta("okf:type", fm.get("type"))
    meta("okf:status", fm.get("status") or "stable")
    meta("okf:trust-tier", trust_tier(fm))
    meta("okf:generated-at", iso(generated(fm).get("at")))
    meta("okf:generated-by", generated(fm).get("by"))
    meta("okf:stale-after", iso(fm.get("stale_after")))
    lines.append("<!-- okf:end -->")
    return "\n".join(lines) + "\n"


def write(path: Path, text: str, changed: list[str]) -> None:
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))


def load_subsites() -> list[dict]:
    data = yaml.safe_load(SUBSITES_FILE.read_text(encoding="utf-8")) or {}
    subs = data.get("subsites") or []
    for s in subs:
        missing = [k for k in ("path", "repo", "name", "outline") if not s.get(k)]
        if missing:
            raise SystemExit(f"subsites.yml: {s.get('path', '?')} lacks {', '.join(missing)}")
        if not s["path"].endswith("/"):
            raise SystemExit(f"subsites.yml: path {s['path']} needs a trailing slash")
    return subs


def replace_block(text: str, begin: str, end: str, body: str, where: str) -> str:
    """Swap the lines between two marker lines; the markers stay."""
    i, j = text.find(begin), text.find(end)
    if i < 0 or j < i:
        raise SystemExit(f"{where}: markers {begin!r} ... {end!r} not found")
    i = text.index("\n", i) + 1
    j = text.rfind("\n", 0, j) + 1  # keep the end marker's indentation
    return text[:i] + body + text[j:]


def robots_block(subsites: list[dict]) -> str:
    return "".join(f"Sitemap: {BASE}{s['path']}sitemap.xml\n"
                   for s in subsites if s.get("sitemap"))


def robots_bundles(subsites: list[dict]) -> str:
    return "".join(f"#     {BASE}{s['path']}llms.txt\n" for s in subsites)


def agent_guide_table(subsites: list[dict]) -> str:
    rows = ["| Site | Outline | Full corpus | Agent guide |",
            "| ---- | ------- | ----------- | ----------- |"]
    for s in subsites:
        b = BASE + s["path"]
        guide = f"<{b}about/ai-agents/>" if s.get("guide") else "—"
        rows.append(f"| {s['name']}, <{b}> | <{b}llms.txt> | <{b}llms-full.txt> | {guide} |")
    return "\n".join(rows) + "\n"


def agent_guide_rows(subsites: list[dict]) -> str:
    out = []
    for s in subsites:
        b = html.escape(BASE + s["path"], quote=True)
        name, path = html.escape(s["name"]), html.escape("/" + s["path"])
        guide = (f'<a href="{b}about/ai-agents/">For AI agents</a>' if s.get("guide") else "—")
        out.append(f'          <tr><td><a href="{b}">{name}</a> <code>{path}</code></td>'
                   f'<td><a href="{b}llms.txt"><code>llms.txt</code></a></td>'
                   f'<td><a href="{b}llms-full.txt"><code>llms-full.txt</code></a></td>'
                   f"<td>{guide}</td></tr>\n")
    return "".join(out)


def llms_txt(sections, concepts: dict, subsites: list[dict]) -> str:
    home = concepts[PAGES["index.html"]]
    lines = [
        "# MESA — Multidisciplinary Environment for Scientific Advancement",
        "",
        f"> {sentence(home.get('description'))} This origin is published for people and "
        "for AI agents: its content is an Open Knowledge Format (OKF v0.2) bundle whose "
        "documents carry YAML frontmatter with type, provenance (generated/sources), trust "
        "(verified), and lifecycle (status/stale_after) fields.",
        "",
        f"Full corpus for ingestion: {BASE}llms-full.txt",
        "",
        "Links below point at each document's Markdown, OKF frontmatter included; every "
        "rendered page declares the same twin with <link rel=\"alternate\" "
        f"type=\"text/markdown\"> in its <head>. OKF bundle root: {BASE}okf/index.md. "
        f"Agent guide: {BASE}about/ai-agents/",
        "",
        "MESA's software is a set of MCP servers: for scientific data, connect to them "
        "(the agent guide explains how) rather than scraping these pages.",
        "",
    ]
    for heading, items in sections:
        lines += [f"## {heading}", ""]
        for title, rel, _ in items:
            fm = concepts[rel]
            entry = f"- [{title}]({BASE}okf/{rel}): {sentence(fm.get('description'))}"
            if fm.get("resource"):
                entry += f" Canonical: {fm['resource']}"
            if fm.get("visibility") == "private":
                entry += " (private repository; not publicly readable)"
            if fm.get("status") == "deprecated":
                entry += " (deprecated; kept for history)"
            elif fm.get("status") == "draft":
                entry += " (draft)"
            lines.append(entry)
        lines.append("")
    lines += ["## Sub-site bundles", ""]
    for s in subsites:
        name, path = s["name"], s["path"]
        lines += [
            f"- [{name}: llms.txt]({BASE}{path}llms.txt): outline of {sentence(s['outline'])[:-1]}",
            f"- [{name}: llms-full.txt]({BASE}{path}llms-full.txt): every page's Markdown "
            "with OKF frontmatter in one file",
        ]
        if s.get("guide"):
            lines.append(
                f"- [{name}: agent guide]({BASE}{path}about/ai-agents/): endpoints and trust "
                "signals; any page URL + index.md returns that page's Markdown")
    lines += ["", "## Related bundles", ""]
    lines += [f"- [{name}]({url}): {desc}" for name, url, desc in RELATED]
    lines += [
        "",
        "## Meta",
        "",
        f"- [OKF bundle index]({BASE}okf/index.md): the bundle root, every concept grouped by section",
        f"- [Bundle update log]({BASE}okf/log.md): dated history of changes to this bundle",
        f"- [robots.txt]({BASE}robots.txt): crawl policy for the whole origin, including "
        "every sub-site above",
    ]
    return "\n".join(lines).rstrip() + "\n"


def llms_full_txt(order: list[str]) -> str:
    full = [
        "# MESA — full corpus",
        "",
        "Every document in the idss-mesa.github.io OKF v0.2 bundle. Each begins with its "
        "canonical URL followed by its original Markdown, OKF frontmatter included. "
        "Relative links resolve against that document's URL.",
        "",
    ]
    for rel in ["index.md", *order, "log.md"]:
        text = (BUNDLE / rel).read_text(encoding="utf-8").rstrip()
        full += [f"---8<--- {BASE}okf/{rel}", "", text, ""]
    return "\n".join(full).rstrip() + "\n"


def sitemap_xml(order: list[str], concepts: dict) -> str:
    def lastmod(rel):
        return iso(generated(concepts[rel]).get("at"))[:10]

    urls = [(page_url(page), lastmod(rel)) for page, rel in PAGES.items()]
    urls += [(BASE + mirror, lastmod(rel)) for rel, mirror in MIRRORS.items()]
    urls += [(BASE + p, "") for p in ("llms.txt", "llms-full.txt", "okf/index.md", "okf/log.md")]
    urls += [(f"{BASE}okf/{rel}", lastmod(rel)) for rel in order]
    body = "".join(
        f"  <url><loc>{html.escape(loc)}</loc>"
        + (f"<lastmod>{mod}</lastmod>" if mod else "")
        + "</url>\n"
        for loc, mod in urls
    )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{body}</urlset>\n")


def main() -> int:
    concepts = {
        str(p.relative_to(BUNDLE)): split(p)[0]
        for p in sorted(BUNDLE.rglob("*.md"))
        if p.name not in ("index.md", "log.md")
    }
    sections = read_index()
    problems = check_index(sections, concepts)
    if problems:
        for p in problems:
            print(f"ERROR {p}", file=sys.stderr)
        return 1
    order = [rel for _, items in sections for _, rel, _ in items]

    subsites = load_subsites()
    changed: list[str] = []
    # Generated blocks inside hand-written files come first, so the corpus
    # files below see the updated agent guide.
    robots = ROOT / "robots.txt"
    text = robots.read_text(encoding="utf-8")
    text = replace_block(text, "# subsites:sitemaps:begin", "# subsites:sitemaps:end",
                         robots_block(subsites), "robots.txt")
    text = replace_block(text, "# subsites:bundles:begin", "# subsites:bundles:end",
                         robots_bundles(subsites), "robots.txt")
    write(robots, text, changed)
    guide = BUNDLE / "concepts" / "ai-agents.md"
    write(guide, replace_block(guide.read_text(encoding="utf-8"),
                               "<!-- subsites:begin", "<!-- subsites:end",
                               agent_guide_table(subsites), "okf/concepts/ai-agents.md"),
          changed)
    page = ROOT / "about" / "ai-agents" / "index.html"
    write(page, replace_block(page.read_text(encoding="utf-8"),
                              "<!-- subsites:begin", "<!-- subsites:end",
                              agent_guide_rows(subsites), "about/ai-agents/index.html"),
          changed)
    write(ROOT / "llms.txt", llms_txt(sections, concepts, subsites), changed)
    write(ROOT / "llms-full.txt", llms_full_txt(order), changed)
    write(ROOT / "sitemap.xml", sitemap_xml(order, concepts), changed)
    for rel, mirror in MIRRORS.items():
        write(ROOT / mirror, (BUNDLE / rel).read_text(encoding="utf-8"), changed)
    for page, rel in PAGES.items():
        path = ROOT / page
        text = path.read_text(encoding="utf-8")
        block = head_block(page, rel, concepts[rel])
        if BLOCK_RE.search(text):
            new = BLOCK_RE.sub(lambda _: block, text, count=1)
        else:
            new = text.replace("</head>", block + "</head>", 1)
        write(path, new, changed)

    print(f"agent surface: {len(concepts)} concepts, {len(PAGES)} pages; "
          f"{'updated ' + ', '.join(changed) if changed else 'no changes'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
