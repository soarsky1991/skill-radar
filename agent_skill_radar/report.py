from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def render_markdown(payload: dict[str, Any], max_items: int = 25) -> str:
    generated_at = payload.get("generated_at") or datetime.now(timezone.utc).isoformat()
    rows = sorted(payload.get("repos", []), key=lambda item: item["radar"]["score"], reverse=True)
    lines: list[str] = []
    lines.append("# Agent Skill Radar")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("A daily GitHub radar for AI agent skills, MCP servers, prompts, and agent-native developer tools.")
    lines.append("")
    lines.append("## Top Opportunities")
    lines.append("")
    lines.append("| Rank | Repo | Score | Stage | Stars | Signal | Angle |")
    lines.append("|---:|---|---:|---|---:|---|---|")
    for index, item in enumerate(rows[:max_items], start=1):
        repo = item["repo"]
        radar = item["radar"]
        signal = ", ".join(radar.get("signals", [])[:2]) or "n/a"
        lines.append(
            "| {rank} | [{name}]({url}) | {score} | {stage} | {stars} | {signal} | {angle} |".format(
                rank=index,
                name=repo["full_name"],
                url=repo["url"],
                score=radar["score"],
                stage=radar["stage"],
                stars=repo["stars"],
                signal=escape_table(signal),
                angle=escape_table(radar["angle"]),
            )
        )

    lines.append("")
    lines.append("## Build Briefs")
    lines.append("")
    for item in rows[: min(8, max_items)]:
        repo = item["repo"]
        radar = item["radar"]
        lines.append(f"### {repo['full_name']}")
        lines.append("")
        lines.append(f"- URL: {repo['url']}")
        lines.append(f"- Score: {radar['score']} ({radar['stage']})")
        lines.append(f"- Why now: {', '.join(radar.get('signals', [])) or 'No strong signal.'}")
        lines.append(f"- Project angle: {radar['angle']}")
        lines.append(f"- Fast validation: publish a one-page demo README, ask maintainers/users if the companion tool should exist, then open 3 fake-door comments or posts.")
        if item.get("issue_error"):
            lines.append("- Issue sample: skipped because GitHub API rate limited or rejected the request.")
        top_issues = radar.get("top_issues", [])
        if top_issues:
            lines.append("- Issue sample:")
            for issue in top_issues[:3]:
                lines.append(
                    f"  - [{issue.get('title')}]({issue.get('url')}) "
                    f"({issue.get('comments', 0)} comments, {issue.get('reactions', 0)} reactions)"
                )
        elif not item.get("issue_error"):
            lines.append("- Issue sample: no demand-shaped issue found in the sampled window.")
        lines.append("")

    lines.append("## Operator Notes")
    lines.append("")
    lines.append("- Prefer narrow companion tools over upstream forks.")
    lines.append("- Stars follow utility plus repeated distribution: daily report, demo GIF, issue replies, and short-form posts.")
    lines.append("- Treat a high score as a reason to probe, not as proof that a full product should be built.")
    lines.append("")
    return "\n".join(lines)


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
