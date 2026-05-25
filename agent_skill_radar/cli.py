from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .github import GitHubAPIError, GitHubClient, normalize_repo
from .report import read_json, render_markdown, write_json
from .scoring import score_repo


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "queries.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Daily radar for AI agent skills and developer-tool opportunities.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    collect = subparsers.add_parser("collect", help="Collect and score GitHub repositories.")
    collect.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="JSON query config.")
    collect.add_argument("--query", action="append", default=[], help="Extra GitHub repository search query.")
    collect.add_argument("--limit-per-query", type=int, default=12, help="Repositories to fetch per query.")
    collect.add_argument("--issue-limit", type=int, default=6, help="Issues to sample per repository.")
    collect.add_argument("--days", type=int, default=45, help="Issue lookback window.")
    collect.add_argument("--out", type=Path, required=True, help="Output JSON path.")
    collect.add_argument("--no-issues", action="store_true", help="Skip issue sampling.")
    collect.set_defaults(func=cmd_collect)

    report = subparsers.add_parser("report", help="Render a Markdown report from collected JSON.")
    report.add_argument("--input", type=Path, required=True, help="Input JSON path.")
    report.add_argument("--out", type=Path, required=True, help="Output Markdown path.")
    report.add_argument("--max-items", type=int, default=25, help="Rows to include.")
    report.set_defaults(func=cmd_report)

    run = subparsers.add_parser("run", help="Collect data and render a dated report.")
    run.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="JSON query config.")
    run.add_argument("--limit-per-query", type=int, default=12)
    run.add_argument("--issue-limit", type=int, default=6)
    run.add_argument("--days", type=int, default=45)
    run.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    run.add_argument("--data-dir", type=Path, default=ROOT / "data")
    run.add_argument("--report-dir", type=Path, default=ROOT / "reports")
    run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    args.func(args)


def cmd_collect(args: argparse.Namespace) -> None:
    payload = collect_payload(
        config_path=args.config,
        extra_queries=args.query,
        limit_per_query=args.limit_per_query,
        issue_limit=args.issue_limit,
        days=args.days,
        with_issues=not args.no_issues,
    )
    write_json(args.out, payload)
    print(f"Wrote {args.out}")


def cmd_report(args: argparse.Namespace) -> None:
    payload = read_json(args.input)
    markdown = render_markdown(payload, max_items=args.max_items)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(markdown, encoding="utf-8")
    print(f"Wrote {args.out}")


def cmd_run(args: argparse.Namespace) -> None:
    data_path = args.data_dir / f"{args.date}.json"
    report_path = args.report_dir / f"{args.date}.md"
    latest_data_path = args.data_dir / "latest.json"
    latest_report_path = args.report_dir / "latest.md"
    payload = collect_payload(
        config_path=args.config,
        extra_queries=[],
        limit_per_query=args.limit_per_query,
        issue_limit=args.issue_limit,
        days=args.days,
        with_issues=True,
    )
    write_json(data_path, payload)
    write_json(latest_data_path, payload)
    markdown = render_markdown(payload)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(markdown, encoding="utf-8")
    latest_report_path.write_text(markdown, encoding="utf-8")
    print(f"Wrote {data_path}")
    print(f"Wrote {report_path}")
    print(f"Wrote {latest_data_path}")
    print(f"Wrote {latest_report_path}")


def collect_payload(
    config_path: Path,
    extra_queries: list[str],
    limit_per_query: int,
    issue_limit: int,
    days: int,
    with_issues: bool,
) -> dict[str, Any]:
    config = load_config(config_path)
    queries = list(config.get("queries", []))
    for index, query in enumerate(extra_queries, start=1):
        queries.append({"label": f"extra-{index}", "q": query})

    client = GitHubClient(sleep_seconds=2.2)
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    seen: set[str] = set()
    scored: list[dict[str, Any]] = []

    for query in queries:
        label = query["label"]
        search = query["q"]
        repos = client.search_repositories(search, limit=limit_per_query)
        for item in repos:
            repo = normalize_repo(item, query_label=label)
            full_name = repo.get("full_name")
            if not full_name or full_name in seen:
                continue
            seen.add(full_name)
            issue_error = ""
            if with_issues and issue_limit > 0:
                try:
                    issues = client.search_issues(full_name, since=since, limit=issue_limit)
                except GitHubAPIError as exc:
                    issues = []
                    issue_error = str(exc)
            else:
                issues = []
            scored.append(
                {
                    "repo": repo,
                    "issues": issues,
                    "issue_error": issue_error,
                    "radar": score_repo(repo, issues),
                }
            )

    scored.sort(key=lambda item: item["radar"]["score"], reverse=True)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "since": since,
        "queries": queries,
        "repos": scored,
    }


def load_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
