#!/usr/bin/env python3
"""Regenerate the profile stats cards (assets/stats.svg, assets/langs.svg).

Data comes straight from the GitHub API so the cards can never drift from
reality. Run locally or from .github/workflows/stats.yml.

Usage:
    GITHUB_TOKEN=... python3 scripts/generate_stats.py
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OWNER = "NetVar1337"
ORGS = ("BitterSecurity", "hashward-io")
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

API = "https://api.github.com"

# --- palette (matches the existing banner / card style) -----------------------
BG = "#0B0F14"
STROKE = "#1E293B"
FG = "#E2E8F0"
MUTED = "#94A3B8"
ACCENT = "#A78BFA"
ACCENT2 = "#22D3EE"

LANG_COLORS = {
    "Python": "#3776AB", "Rust": "#DEA584", "JavaScript": "#F7DF1E",
    "TypeScript": "#3178C6", "Go": "#00ADD8", "C": "#555555", "C++": "#00599C",
    "Java": "#B07219", "Shell": "#89E051", "Zig": "#F7A41D", "Solidity": "#AA6746",
    "Ruby": "#701516", "HTML": "#E34C26", "CSS": "#563D7C", "Assembly": "#6E4C13",
    "Lua": "#000080", "PowerShell": "#012456", "Vue": "#41B883", "Elixir": "#6E4A7E",
    "Haskell": "#5E5086", "Kotlin": "#A97BFF", "Swift": "#F05138", "Dart": "#00B4AB",
    "Objective-C": "#438eff", "Nix": "#7e7eff", "CMake": "#DA3434", "Makefile": "#427819",
    "Dockerfile": "#384d54", "Batchfile": "#C1F12E", "EJS": "#a91e50",
}


# --- tiny HTTP helper --------------------------------------------------------
def token() -> str:
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        return tok.strip()
    try:
        out = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True
        ).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    sys.exit("No GitHub token found (set GITHUB_TOKEN or run `gh auth login`).")


TOK = token()


def api(path: str, accept: str = "application/vnd.github+json") -> object:
    req = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Authorization": f"Bearer {TOK}",
            "Accept": accept,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "profile-stats-generator",
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429) and attempt < 2:
                import time
                time.sleep(3 * (attempt + 1))
                continue
            raise
    raise RuntimeError(f"unreachable: {path}")


def graphql(query: str) -> dict:
    req = urllib.request.Request(
        f"{API}/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={
            "Authorization": f"Bearer {TOK}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        payload = json.loads(resp.read().decode())
    if payload.get("errors"):
        raise RuntimeError(payload["errors"])
    return payload["data"]


# --- collection --------------------------------------------------------------
def collect_repos() -> list[dict]:
    repos: list[dict] = []
    for owner in (OWNER, *ORGS):
        base = (f"/users/{owner}/repos?per_page=100&page={{page}}&type=owner"
                if owner == OWNER
                else f"/orgs/{owner}/repos?per_page=100&page={{page}}")
        for page in range(1, 6):
            batch = api(base.format(page=page))
            if not batch:
                break
            repos.extend(batch)
            if len(batch) < 100:
                break
    return [r for r in repos if not r.get("fork") and not r.get("archived")]


def collect_stats(repos: list[dict]) -> dict:
    # profile + follower counts
    prof = graphql(f'''query {{ user(login:"{OWNER}") {{
        followers {{ totalCount }}
        following {{ totalCount }}
        repositories(first:1) {{ totalCount }}
    }} }}''')["user"]

    # contributions, summed per calendar year (GraphQL caps a query at 1 year)
    commits = prs = issues = 0
    now = datetime.now(timezone.utc).year
    for year in range(2015, now + 1):
        data = graphql(f'''query {{ user(login:"{OWNER}") {{
            contributionsCollection(from:"{year}-01-01T00:00:00Z",
                                    to:"{year}-12-31T00:00:00Z") {{
                totalCommitContributions
                totalPullRequestContributions
                totalIssueContributions
            }} }} }}''')["user"]["contributionsCollection"]
        commits += data["totalCommitContributions"]
        prs += data["totalPullRequestContributions"]
        issues += data["totalIssueContributions"]

    owned = [r for r in repos if r["owner"]["login"].lower() == OWNER.lower()]
    org = [r for r in repos if r["owner"]["login"].lower() != OWNER.lower()]

    # `repositories.totalCount` from GraphQL counts private repos too, so the
    # public figure is derived from the REST listing instead.
    public_owned = 0
    for page in range(1, 6):
        batch = api(f"/users/{OWNER}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        public_owned += sum(1 for r in batch if not r.get("private"))
        if len(batch) < 100:
            break

    return {
        "stars": sum(r["stargazers_count"] for r in repos),
        "own_stars": sum(r["stargazers_count"] for r in owned),
        "followers": prof["followers"]["totalCount"],
        "following": prof["following"]["totalCount"],
        "public_repos": public_owned,
        "total_repos": prof["repositories"]["totalCount"],
        "owned_repos": len(owned),
        "org_repos": len(org),
        "commits": commits,
        "prs": prs,
        "issues": issues,
        "projects": len(repos),
    }


def collect_langs(repos: list[dict]) -> list[tuple[str, int]]:
    totals: dict[str, int] = {}
    for repo in repos:
        try:
            langs = api(f"/repos/{repo['full_name']}/languages")
        except Exception:
            continue
        for name, size in langs.items():
            totals[name] = totals.get(name, 0) + int(size)
    return sorted(totals.items(), key=lambda kv: -kv[1])


# --- rendering ---------------------------------------------------------------
def esc(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def human(n: int) -> str:
    if n >= 1000:
        val = n / 1000
        return f"{val:.1f}k".replace(".0k", "k")
    return str(n)


def render_stats(s: dict) -> str:
    # Two columns of stacked value/label pairs; a footer carries the secondary
    # counters so nothing collides horizontally.
    left = [
        (human(s["stars"]), "Stars earned"),
        (human(s["commits"]), "Commits"),
        (human(s["prs"]), "Merged PRs"),
    ]
    right = [
        (human(s["followers"]), "Followers"),
        (str(s["public_repos"]), "Public repos"),
        (str(s["projects"]), "OSS projects"),
    ]
    w, h = 460, 224
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="GitHub stats for {OWNER}">',
        f'  <rect width="{w}" height="{h}" rx="12" fill="{BG}" stroke="{STROKE}" stroke-width="1"/>',
        f'  <rect x="0" y="0" width="{w}" height="4" rx="2" fill="{ACCENT}"/>',
        f'  <text x="22" y="36" font-family="Noto Sans, sans-serif" font-size="16" '
        f'font-weight="700" fill="{ACCENT}">GitHub activity</text>',
        f'  <text x="438" y="36" text-anchor="end" font-family="Noto Sans Mono, monospace" '
        f'font-size="11" fill="{MUTED}">@{OWNER}</text>',
    ]
    for col, cells in ((0, left), (1, right)):
        x = 22 + col * 216
        for row, (value, label) in enumerate(cells):
            y = 78 + row * 40
            out.append(
                f'  <text x="{x}" y="{y}" font-family="Noto Sans Mono, monospace" font-size="19" '
                f'font-weight="700" fill="{FG}">{esc(value)}</text>'
            )
            out.append(
                f'  <text x="{x}" y="{y + 16}" font-family="Noto Sans, sans-serif" font-size="11" '
                f'fill="{MUTED}">{esc(label)}</text>'
            )
    footer = (
        f"{s['own_stars']} stars on personal repos · {s['issues']} issues · "
        f"{s['org_repos']} repos under BitterSecurity & hashward-io"
    )
    out.append(f'  <line x1="22" y1="198" x2="438" y2="198" stroke="{STROKE}" stroke-width="1"/>')
    out.append(
        f'  <text x="22" y="213" font-family="Noto Sans, sans-serif" font-size="9.5" '
        f'fill="{MUTED}" opacity=".9">{esc(footer)}</text>'
    )
    out.append("</svg>")
    return "\n".join(out) + "\n"


def render_langs(langs: list[tuple[str, int]], stats: dict) -> str:
    top = langs[:6]
    total = sum(size for _, size in top) or 1
    w, h = 360, 200
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="Top languages">',
        f'  <rect width="{w}" height="{h}" rx="12" fill="{BG}" stroke="{STROKE}" stroke-width="1"/>',
        f'  <rect x="0" y="0" width="{w}" height="4" rx="2" fill="{ACCENT2}"/>',
        f'  <text x="22" y="36" font-family="Noto Sans, sans-serif" font-size="16" '
        f'font-weight="700" fill="{ACCENT}">Top languages</text>',
        f'  <text x="338" y="36" text-anchor="end" font-family="Noto Sans Mono, monospace" '
        f'font-size="11" fill="{MUTED}">{stats["projects"]} repos</text>',
    ]
    bar_x, bar_w = 132, 206
    for idx, (name, size) in enumerate(top):
        y = 62 + idx * 22
        pct = size / total
        color = LANG_COLORS.get(name, "#8B949E")
        out.append(
            f'  <text x="22" y="{y + 11}" font-family="Noto Sans, sans-serif" font-size="12" '
            f'fill="{FG}">{esc(name)}</text>'
        )
        out.append(
            f'  <rect x="{bar_x}" y="{y}" width="{bar_w}" height="10" rx="5" fill="{STROKE}"/>'
        )
        out.append(
            f'  <rect x="{bar_x}" y="{y}" width="{max(3, round(bar_w * pct))}" height="10" '
            f'rx="5" fill="{color}"/>'
        )
        out.append(
            f'  <text x="338" y="{y + 9}" text-anchor="end" font-family="Noto Sans Mono, '
            f'monospace" font-size="10" fill="{MUTED}">{pct * 100:.0f}%</text>'
        )
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main() -> int:
    ASSETS.mkdir(parents=True, exist_ok=True)
    repos = collect_repos()
    stats = collect_stats(repos)
    langs = collect_langs(repos)

    (ASSETS / "stats.svg").write_text(render_stats(stats), encoding="utf-8")
    (ASSETS / "langs.svg").write_text(render_langs(langs, stats), encoding="utf-8")

    print(json.dumps(stats, indent=2))
    print("languages:", [(n, s) for n, s in langs[:8]])
    print(f"wrote {ASSETS/'stats.svg'} and {ASSETS/'langs.svg'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
