from __future__ import annotations

import math
from datetime import datetime, timezone
from typing import Any


EXTENSION_KEYWORDS = {
    "skill": 4,
    "skills": 4,
    "agent": 3,
    "agents": 3,
    "mcp": 4,
    "plugin": 3,
    "plugins": 3,
    "cli": 3,
    "command": 2,
    "workflow": 2,
    "prompt": 3,
    "prompts": 3,
    "template": 2,
    "templates": 2,
    "automation": 2,
    "context": 2,
}

CREATOR_FIT_KEYWORDS = {
    "markdown": 3,
    "content": 3,
    "creator": 3,
    "publishing": 3,
    "wechat": 3,
    "obsidian": 3,
    "docs": 2,
    "documentation": 2,
    "research": 2,
    "design": 2,
    "slides": 2,
    "video": 2,
    "image": 2,
}

DEMAND_WORDS = (
    "support",
    "feature",
    "request",
    "integrate",
    "integration",
    "plugin",
    "mcp",
    "skill",
    "export",
    "workflow",
    "automation",
    "template",
    "docs",
    "documentation",
    "roadmap",
    "支持",
    "希望",
    "适配",
    "集成",
    "插件",
    "导出",
    "文档",
    "工作流",
    "需求",
)

NEGATIVE_ISSUE_WORDS = (
    "bug",
    "error",
    "failed",
    "failure",
    "crash",
    "exception",
    "not working",
    "broken",
    "报错",
    "错误",
    "失败",
    "闪退",
    "闪烁",
    "无法",
)


def score_repo(repo: dict[str, Any], issues: list[dict[str, Any]]) -> dict[str, Any]:
    stars = int(repo.get("stars") or 0)
    forks = int(repo.get("forks") or 0)
    open_issues = int(repo.get("open_issues") or 0)
    age_days = max(days_since(repo.get("created_at")), 1)
    pushed_days = days_since(repo.get("pushed_at"))
    text = searchable_text(repo)

    heat = min(25.0, math.log10(stars + 1) * 6.0 + math.log10(forks + 1) * 2.0)
    freshness = max(0.0, 10.0 - min(pushed_days, 120) / 12.0)
    velocity_proxy = min(18.0, (stars / age_days) * 18.0)
    issue_demand = score_issue_demand(issues)
    extensibility = min(14.0, keyword_score(text, EXTENSION_KEYWORDS))
    creator_fit = min(10.0, keyword_score(text, CREATOR_FIT_KEYWORDS))
    open_surface = min(8.0, math.log10(open_issues + 1) * 4.0)
    novelty = novelty_score(age_days, stars)
    saturation_penalty = penalty_score(age_days, stars)

    raw = (
        heat
        + freshness
        + velocity_proxy
        + issue_demand
        + extensibility
        + creator_fit
        + open_surface
        + novelty
        - saturation_penalty
    )
    score = max(0.0, min(100.0, raw))
    signals = build_signals(
        repo=repo,
        issues=issues,
        heat=heat,
        freshness=freshness,
        velocity_proxy=velocity_proxy,
        issue_demand=issue_demand,
        extensibility=extensibility,
        creator_fit=creator_fit,
        novelty=novelty,
        saturation_penalty=saturation_penalty,
    )

    return {
        "score": round(score, 1),
        "stage": classify(score),
        "angle": opportunity_angle(repo, issues),
        "scores": {
            "heat": round(heat, 1),
            "freshness": round(freshness, 1),
            "velocity_proxy": round(velocity_proxy, 1),
            "issue_demand": round(issue_demand, 1),
            "extensibility": round(extensibility, 1),
            "creator_fit": round(creator_fit, 1),
            "open_surface": round(open_surface, 1),
            "novelty": round(novelty, 1),
            "saturation_penalty": round(saturation_penalty, 1),
        },
        "signals": signals,
        "top_issues": rank_demand_issues(issues)[:5],
    }


def score_issue_demand(issues: list[dict[str, Any]]) -> float:
    total = 0.0
    for issue in rank_demand_issues(issues)[:5]:
        title = (issue.get("title") or "").lower()
        demand_bonus = 3.0 if is_demand_issue(issue) else 0.0
        total += min(6.0, issue.get("comments", 0) * 0.45 + issue.get("reactions", 0) * 0.8 + demand_bonus)
    return min(18.0, total)


def rank_demand_issues(issues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [issue for issue in rank_issues(issues) if is_demand_issue(issue)]


def rank_issues(issues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        issues,
        key=lambda issue: (
            issue.get("comments", 0) * 2
            + issue.get("reactions", 0) * 3
            + keyword_issue_bonus(issue)
        ),
        reverse=True,
    )


def keyword_issue_bonus(issue: dict[str, Any]) -> int:
    title = (issue.get("title") or "").lower()
    return 5 if any(word in title for word in DEMAND_WORDS) else 0


def is_demand_issue(issue: dict[str, Any]) -> bool:
    title = (issue.get("title") or "").lower()
    has_demand = any(word in title for word in DEMAND_WORDS)
    has_negative = any(word in title for word in NEGATIVE_ISSUE_WORDS)
    return has_demand and not has_negative


def keyword_score(text: str, weights: dict[str, int]) -> float:
    score = 0.0
    padded = f" {text.lower()} "
    for word, weight in weights.items():
        if word in padded:
            score += weight
    return score


def novelty_score(age_days: int, stars: int) -> float:
    if age_days <= 180 and stars >= 200:
        return 10.0
    if age_days <= 365 and stars >= 500:
        return 8.0
    if age_days <= 730 and stars >= 1000:
        return 5.0
    return 2.0


def penalty_score(age_days: int, stars: int) -> float:
    penalty = 0.0
    if stars >= 100_000:
        penalty += 10.0
    elif stars >= 50_000:
        penalty += 6.0
    if age_days >= 3650:
        penalty += 4.0
    return penalty


def classify(score: float) -> str:
    if score >= 80:
        return "build-now"
    if score >= 65:
        return "probe-this-week"
    if score >= 45:
        return "content-first"
    return "archive"


def opportunity_angle(repo: dict[str, Any], issues: list[dict[str, Any]]) -> str:
    text = searchable_text(repo)
    issue_text = " ".join(issue.get("title", "") for issue in issues).lower()
    combined = f"{text} {issue_text}"

    if "skill" in combined:
        return "Build a cross-agent skill index, installer, or quality benchmark around this ecosystem."
    if "mcp" in combined:
        return "Build an MCP registry, security checker, config generator, or compatibility layer."
    if "cli" in combined or "terminal" in combined:
        return "Build an agent-native CLI wrapper with JSON output, examples, and deterministic workflows."
    if "markdown" in combined or "obsidian" in combined or "content" in combined:
        return "Build a creator workflow plugin that turns existing content into publish-ready assets."
    if "context" in combined or "memory" in combined:
        return "Build a local context, memory, or compression add-on for coding agents."
    return "Build a narrow companion tool that solves one recurring issue outside the upstream roadmap."


def build_signals(
    repo: dict[str, Any],
    issues: list[dict[str, Any]],
    heat: float,
    freshness: float,
    velocity_proxy: float,
    issue_demand: float,
    extensibility: float,
    creator_fit: float,
    novelty: float,
    saturation_penalty: float,
) -> list[str]:
    signals: list[str] = []
    if heat >= 18:
        signals.append("large existing audience")
    if freshness >= 8:
        signals.append("recently active")
    if velocity_proxy >= 10:
        signals.append("strong stars-per-day proxy")
    if issue_demand >= 10:
        signals.append("issue discussion shows demand")
    if extensibility >= 8:
        signals.append("extension-shaped ecosystem")
    if creator_fit >= 6:
        signals.append("matches creator/tooling distribution")
    if novelty >= 8:
        signals.append("young enough for ecosystem gaps")
    if saturation_penalty >= 8:
        signals.append("high saturation risk")
    if not issues:
        signals.append("no issue sample collected")
    return signals


def searchable_text(repo: dict[str, Any]) -> str:
    topics = " ".join(repo.get("topics") or [])
    return " ".join(
        [
            repo.get("full_name") or "",
            repo.get("description") or "",
            repo.get("language") or "",
            topics,
        ]
    ).lower()


def days_since(iso_value: str | None) -> int:
    if not iso_value:
        return 9999
    try:
        parsed = datetime.fromisoformat(iso_value.replace("Z", "+00:00"))
    except ValueError:
        return 9999
    now = datetime.now(timezone.utc)
    return max(0, (now - parsed).days)
