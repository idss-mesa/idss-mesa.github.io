#!/usr/bin/env python3
"""Check that each repository's question bank can be answered from the hub.

An agent that knows only https://idss-mesa.github.io/llms.txt should be able
to answer the questions MESA's users ask, about the software and about the
data. Each repository keeps those questions in docs/agent-questions.yml
(format below). This script crawls outward from the hub llms.txt the way an
agent would, and for every question looks for one reachable document that
contains all of the question's facts.

Crawl rules: start at the hub llms.txt and follow links in fetched text,
breadth first, up to --max-depth hops. Only these are fetched:
  - https://idss-mesa.github.io/... ending in .txt or .md, or in "/" (read as
    the page's Markdown twin, "/index.md");
  - https://raw.githubusercontent.com/idss-mesa/...;
  - https://github.com/idss-mesa/<repo>/blob/<ref>/<path> (read as raw) and
    https://github.com/idss-mesa/<repo> (read as its README.md).
Relative links resolve against the document they appear in.

Question bank (docs/agent-questions.yml):

  repo: idss-mesa/<name>
  questions:
    - id: short-kebab-id
      kind: engineering          # engineering | data
      q: "The question as a user would ask it."
      answer: "Reference answer, true according to the code."
      must_find:                 # all groups must match inside ONE document
        - ['push[- ]before[- ]commit']   # a group lists alternatives
        - ['checksum']                   # (Python regex, case-insensitive)
      where: docs/dev/architecture.md    # page meant to answer it

An llms-full.txt corpus is split at its "---8<--- <url>" markers and each
page is matched on its own. The report says whether the matching page is the
question's `where` page; "no" usually means the must_find groups are loose.
A pass means the facts are reachable, not that an agent will find them; the
reference answers exist so an LLM-graded run can be added on top.

Usage:
  python3 scripts/answerability.py                 # banks of every sub-site repo
  python3 scripts/answerability.py --repo mesa-mcp --repo neon-ducklake
  python3 scripts/answerability.py --bank path/or/url.yml
  python3 scripts/answerability.py --assume-published neon-ducklake=../neon-ducklake/docs \\
      --bank ../neon-ducklake/docs/agent-questions.yml
      (adds a repository's local docs/ as if already published at
      https://idss-mesa.github.io/<repo>/, two hops from the hub; for testing
      a docs change before it merges)
Options: --max-depth N (default 3), --json FILE, --strict (exit 1 on any miss).
Needs PyYAML and network access to idss-mesa.github.io and GitHub.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
HUB = "https://idss-mesa.github.io/llms.txt"
BASE = "https://idss-mesa.github.io/"
ORG = "idss-mesa"
UA = "idss-mesa-answerability-check"
MAX_BYTES = 4_000_000
URL_RE = re.compile(r"https?://[^\s)<>\]\"'`|]+")
MD_LINK_RE = re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
GH_BLOB = re.compile(rf"^https://github\.com/{ORG}/([^/]+)/blob/([^/]+)/(.+)$")
GH_REPO = re.compile(rf"^https://github\.com/{ORG}/([^/#?]+)/?$")


def fetch(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200:
                return None
            data = r.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                return None
            return data.decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError, ValueError):
        return None


def normalize(url: str) -> str | None:
    """Map a link to the URL an agent would fetch, or None to skip it."""
    url = url.split("#", 1)[0].rstrip(".,;:")
    if not url:
        return None
    if m := GH_BLOB.match(url):
        return f"https://raw.githubusercontent.com/{ORG}/{m[1]}/{m[2]}/{m[3]}"
    if m := GH_REPO.match(url):
        return f"https://raw.githubusercontent.com/{ORG}/{m[1]}/HEAD/README.md"
    if url.startswith(f"https://raw.githubusercontent.com/{ORG}/"):
        return url
    if url.startswith(BASE):
        path = urllib.parse.urlparse(url).path
        if path.endswith("/"):
            return url.split("?", 1)[0] + "index.md"
        if path.endswith((".md", ".txt")):
            return url.split("?", 1)[0]
    return None


def links(url: str, text: str) -> set[str]:
    out = set(URL_RE.findall(text))
    for target in MD_LINK_RE.findall(text):
        if not target.startswith(("http://", "https://", "mailto:", "#")):
            out.add(urllib.parse.urljoin(url, target))
    return {n for u in out if (n := normalize(u))}


CUT_RE = re.compile(r"^---8<--- (\S+)[ \t]*$", re.MULTILINE)


def pages(url: str, text: str) -> list[tuple[str, str]]:
    """Split an llms-full.txt corpus into its pages, so that a question's facts
    must come from one page and not from unrelated pages joined in one file.
    Each page is keyed by the Markdown URL an agent would fetch for it."""
    if not url.endswith("llms-full.txt") or not CUT_RE.search(text):
        return [(url, text)]
    cuts = list(CUT_RE.finditer(text))
    out = []
    for i, m in enumerate(cuts):
        end = cuts[i + 1].start() if i + 1 < len(cuts) else len(text)
        page = m[1] + "index.md" if m[1].endswith("/") else m[1]
        out.append((page, text[m.end():end]))
    return out


def crawl(start: str, max_depth: int, extra: dict[str, str]) -> dict[str, tuple[int, str]]:
    """BFS from start; returns url -> (depth, text). `extra` docs sit at depth 2."""
    docs: dict[str, tuple[int, str]] = {}

    def add(url: str, depth: int, text: str) -> None:
        for page, body in pages(url, text):
            if page not in docs or depth < docs[page][0]:
                docs[page] = (depth, body)

    for u, t in extra.items():
        add(u, 2, t)
    frontier, seen = [start], {start, *extra}
    for depth in range(max_depth + 1):
        with ThreadPoolExecutor(max_workers=8) as pool:
            texts = list(pool.map(fetch, frontier))
        nxt = []
        for url, text in zip(frontier, texts):
            if text is None:
                continue
            add(url, depth, text)
            for link in links(url, text):
                if link not in seen:
                    seen.add(link)
                    nxt.append(link)
        if depth == 1 and extra:  # local docs link onward like published ones
            for url, text in extra.items():
                for link in links(url, text):
                    if link not in seen:
                        seen.add(link)
                        nxt.append(link)
        frontier = nxt
        if not frontier:
            break
    return docs


def load_bank(ref: str) -> tuple[str, dict]:
    if ref.startswith(("http://", "https://")):
        text = fetch(ref)
        if text is None:
            raise FileNotFoundError(ref)
    else:
        text = Path(ref).read_text(encoding="utf-8")
    bank = yaml.safe_load(text) or {}
    problems = []
    for i, q in enumerate(bank.get("questions") or []):
        for key in ("id", "kind", "q", "answer", "must_find"):
            if not q.get(key):
                problems.append(f"question {i} lacks {key}")
        if q.get("kind") not in ("engineering", "data"):
            problems.append(f"{q.get('id')}: kind must be engineering or data")
        for group in q.get("must_find") or []:
            for pat in group if isinstance(group, list) else [group]:
                try:
                    re.compile(pat)
                except re.error as e:
                    problems.append(f"{q.get('id')}: bad regex {pat!r}: {e}")
    if not bank.get("questions"):
        problems.append("no questions")
    if problems:
        raise ValueError(f"{ref}: " + "; ".join(problems))
    return ref, bank


def is_where(url: str, where: str | None) -> bool:
    """Is url the published (or raw) form of the bank's `where` page?"""
    if not where:
        return False
    rel = where[len("docs/"):] if where.startswith("docs/") else where
    forms = ["/" + rel]
    if rel.endswith(".md") and not rel.endswith("index.md"):
        forms.append("/" + rel[: -len(".md")] + "/index.md")
    return any(url.endswith(f) for f in forms)


def answer(q: dict, docs: dict[str, tuple[int, str]]) -> tuple[str | None, int | None, bool]:
    """Best matching page: the `where` page if it matches, else the shallowest."""
    groups = [[re.compile(p, re.I) for p in (g if isinstance(g, list) else [g])]
              for g in q["must_find"]]
    best = None
    for url, (depth, text) in docs.items():
        if all(any(p.search(text) for p in g) for g in groups):
            key = (not is_where(url, q.get("where")), depth)
            if best is None or key < best[0]:
                best = (key, url, depth)
    if best is None:
        return None, None, False
    return best[1], best[2], not best[0][0]


def local_docs(spec: str) -> dict[str, str]:
    repo, _, d = spec.partition("=")
    root = Path(d)
    out = {}
    for p in sorted(root.rglob("*")):
        if p.suffix in (".md", ".txt") and p.is_file():
            rel = p.relative_to(root).as_posix()
            out[f"{BASE}{repo}/{rel}"] = p.read_text(encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--bank", action="append", default=[])
    ap.add_argument("--repo", action="append", default=[])
    ap.add_argument("--assume-published", action="append", default=[])
    ap.add_argument("--max-depth", type=int, default=3)
    ap.add_argument("--json")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    refs = list(args.bank)
    repos = list(args.repo)
    if not refs and not repos:
        reg = yaml.safe_load((ROOT / "subsites.yml").read_text(encoding="utf-8"))
        repos = [s["repo"] for s in reg.get("subsites") or []]
    refs += [f"https://raw.githubusercontent.com/{ORG}/{r}/HEAD/docs/agent-questions.yml"
             for r in repos]

    banks = []
    for ref in refs:
        try:
            banks.append(load_bank(ref))
        except FileNotFoundError:
            print(f"skip {ref}: no question bank", file=sys.stderr)
        except ValueError as e:
            print(f"ERROR {e}", file=sys.stderr)
            return 2
    if not banks:
        print("no question banks found", file=sys.stderr)
        return 2

    extra: dict[str, str] = {}
    for spec in args.assume_published:
        extra.update(local_docs(spec))
    local_prefixes = tuple(f"{BASE}{s.partition('=')[0]}/" for s in args.assume_published)
    docs = crawl(HUB, args.max_depth, extra)
    print(f"crawled {len(docs)} documents from {HUB} (max depth {args.max_depth}"
          + (f", {len(extra)} local docs assumed published" if extra else "") + ")")

    results, misses = [], 0
    lines = ["| repo | id | kind | result | depth | where page | document |",
             "|---|---|---|---|---|---|---|"]
    for ref, bank in banks:
        repo = bank.get("repo", ref)
        for q in bank["questions"]:
            url, depth, on_where = answer(q, docs)
            ok = url is not None
            misses += not ok
            local = " (local)" if url and url.startswith(local_prefixes) else ""
            results.append({"repo": repo, "id": q["id"], "kind": q["kind"], "q": q["q"],
                            "pass": ok, "depth": depth, "document": url,
                            "where": q.get("where"), "on_where_page": on_where})
            lines.append(f"| {repo} | {q['id']} | {q['kind']} | {'pass' if ok else 'MISS'} | "
                         f"{'' if depth is None else depth} | {'yes' if on_where else ('no' if ok else '')} | "
                         f"{(url or '') + local} |")
    total = len(results)
    by = {}
    for r in results:
        k = (r["repo"], r["kind"])
        by.setdefault(k, [0, 0])
        by[k][0] += r["pass"]
        by[k][1] += 1
    summary = [f"{repo} {kind}: {p}/{n}" for (repo, kind), (p, n) in sorted(by.items())]
    report = "\n".join(lines) + "\n\n" + "\n".join(summary) + \
        f"\n\nanswerable: {total - misses}/{total}\n"
    print(report)
    if args.json:
        Path(args.json).write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write("## Answerability from the hub llms.txt\n\n" + report)
    return 1 if (args.strict and misses) else 0


if __name__ == "__main__":
    sys.exit(main())
