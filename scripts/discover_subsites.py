#!/usr/bin/env python3
"""Find idss-mesa repositories that publish an llms.txt and update subsites.yml.

A repository counts as a sub-site when it is public, not archived, has GitHub
Pages, and https://idss-mesa.github.io/<repo>/llms.txt returns 200 with a
Markdown heading. For each sub-site the script also records whether the
agent guide (<path>about/ai-agents/) and sitemap.xml exist.

It changes subsites.yml in three ways, and prints each change:

  - adds a newly published repository, with a placeholder `name` and an
    `outline` taken from the first sentence of its llms.txt summary (edit
    both by hand in the pull request);
  - removes an entry whose llms.txt no longer loads;
  - refreshes the `guide` and `sitemap` flags.

It never rewrites a hand-edited `name` or `outline`. Run
scripts/gen_agent_surface.py afterwards to regenerate llms.txt and friends.

Usage: python3 scripts/discover_subsites.py [--check]
  --check   change nothing; exit 1 if subsites.yml is out of date
Environment: GITHUB_TOKEN (optional) raises the GitHub API rate limit.
Needs PyYAML; network access to api.github.com and idss-mesa.github.io.
"""

from __future__ import annotations

import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "subsites.yml"
ORG = "idss-mesa"
BASE = "https://idss-mesa.github.io/"
UA = "idss-mesa-subsite-discovery"


def http_get(url: str, accept: str = "*/*", token: str | None = None) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except (urllib.error.URLError, TimeoutError):
        return 0, ""


def org_repos(token: str | None) -> list[dict]:
    repos, page = [], 1
    while True:
        status, body = http_get(
            f"https://api.github.com/orgs/{ORG}/repos?type=public&per_page=100&page={page}",
            "application/vnd.github+json", token)
        if status != 200:
            raise SystemExit(f"GitHub API returned {status} listing {ORG} repositories")
        batch = json.loads(body)
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def summary_sentence(llms: str) -> str:
    """First sentence of the llms.txt blockquote summary."""
    m = re.search(r"^>\s*(.+)$", llms, re.MULTILINE)
    if not m:
        return ""
    text = m.group(1).strip()
    m2 = re.match(r"(.+?[.!?])(\s|$)", text)
    return (m2.group(1) if m2 else text).rstrip(".")


def probe(repo: str) -> dict | None:
    path = f"{repo}/"
    status, llms = http_get(f"{BASE}{path}llms.txt")
    if status != 200 or not llms.lstrip().startswith("# "):
        return None
    guide = http_get(f"{BASE}{path}about/ai-agents/")[0] == 200
    sitemap = http_get(f"{BASE}{path}sitemap.xml")[0] == 200
    return {"path": path, "repo": repo, "guide": guide, "sitemap": sitemap,
            "summary": summary_sentence(llms)}


def dump(header: str, subsites: list[dict]) -> str:
    """Write entries in the hand-edited layout so unchanged files diff clean."""
    def scalar(v) -> str:
        if isinstance(v, bool):
            return "true" if v else "false"
        s = str(v)
        plain = yaml.safe_dump(s, default_style=None, width=10_000).strip()
        if plain.endswith("\n...") or plain.endswith("..."):
            plain = plain.rsplit("\n", 1)[0] if "\n" in plain else plain[:-3].strip()
        return plain

    out = [header.rstrip("\n"), "", "subsites:"]
    for s in subsites:
        out.append(f"  - path: {s['path']}")
        for key in ("repo", "name", "outline", "guide", "sitemap"):
            v = s.get(key)
            if key == "outline" and len(f"    outline: {v}") > 76:
                out.append("    outline: >-")
                out += ["      " + ln for ln in textwrap.wrap(str(v), 72)]
            else:
                out.append(f"    {key}: {scalar(v)}")
    return "\n".join(out) + "\n"


def main() -> int:
    check = "--check" in sys.argv[1:]
    token = os.environ.get("GITHUB_TOKEN") or None
    text = REGISTRY.read_text(encoding="utf-8")
    header = text[: text.index("\nsubsites:")]
    current = (yaml.safe_load(text) or {}).get("subsites") or []

    candidates = [r["name"] for r in org_repos(token)
                  if not r.get("archived") and r.get("has_pages")
                  and r["name"] != f"{ORG}.github.io"]
    with ThreadPoolExecutor(max_workers=8) as pool:
        found = {p["repo"]: p for p in pool.map(probe, sorted(candidates)) if p}

    changes: list[str] = []
    result: list[dict] = []
    for s in current:
        live = found.pop(s["repo"], None)
        if live is None:
            changes.append(f"removed {s['path']}: {BASE}{s['path']}llms.txt no longer loads")
            continue
        for flag in ("guide", "sitemap"):
            if bool(s.get(flag)) != live[flag]:
                changes.append(f"{s['path']}: {flag} {bool(s.get(flag))} -> {live[flag]}")
                s[flag] = live[flag]
        result.append(s)
    for repo, live in sorted(found.items()):
        outline = (f"the {repo} documentation: {live['summary']}" if live["summary"]
                   else f"the {repo} documentation")
        result.append({"path": live["path"], "repo": repo, "name": f"{repo} docs",
                       "outline": outline, "guide": live["guide"], "sitemap": live["sitemap"]})
        changes.append(f"added {live['path']} (check its name and outline)")

    new_text = dump(header, result)
    for c in changes:
        print(c)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("## Sub-site discovery\n\n")
            fh.write("".join(f"- {c}\n" for c in changes) or "No changes.\n")
    if new_text == text:
        print(f"subsites.yml: up to date ({len(result)} sub-sites)")
        return 0
    if check:
        print("subsites.yml: out of date", file=sys.stderr)
        return 1
    REGISTRY.write_text(new_text, encoding="utf-8")
    print(f"subsites.yml: updated ({len(result)} sub-sites)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
