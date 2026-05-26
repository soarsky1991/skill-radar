from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SIGNAL_ZH = {
    "large existing audience": "已有大受众",
    "recently active": "近期活跃",
    "strong stars-per-day proxy": "stars/day 代理指标强",
    "issue discussion shows demand": "issue 讨论显示需求",
    "extension-shaped ecosystem": "生态具备扩展形态",
    "matches creator/tooling distribution": "适合创作者/工具分发",
    "young enough for ecosystem gaps": "生态仍新，存在空位",
    "high saturation risk": "饱和风险高",
    "no issue sample collected": "未采集 issue 样本",
}

ANGLE_ZH = {
    "Build a cross-agent skill index, installer, or quality benchmark around this ecosystem.": "围绕该生态构建跨 agent skill index、installer 或质量 benchmark。",
    "Build an MCP registry, security checker, config generator, or compatibility layer.": "构建 MCP registry、security checker、config generator 或 compatibility layer。",
    "Build an agent-native CLI wrapper with JSON output, examples, and deterministic workflows.": "构建带 JSON 输出、示例和确定性工作流的 agent-native CLI wrapper。",
    "Build a creator workflow plugin that turns existing content into publish-ready assets.": "构建创作者工作流插件，把现有内容转成可发布资产。",
    "Build a local context, memory, or compression add-on for coding agents.": "为 coding agents 构建本地 context、memory 或 compression add-on。",
    "Build a narrow companion tool that solves one recurring issue outside the upstream roadmap.": "构建窄而实用的 companion tool，解决上游路线图之外的高频问题。",
}


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
    lines.append('<p align="center">')
    lines.append('Languages: <a href="#zh-cn">简体中文</a> · <a href="#english">English</a>')
    lines.append("</p>")
    lines.append("")
    lines.append('<a id="zh-cn"></a>')
    lines.append("")
    lines.append("## 简体中文")
    lines.append("")
    lines.append(f"生成时间：`{generated_at}`")
    lines.append("")
    lines.append("面向 AI agent skills、MCP servers、prompts 和 agent-native developer tools 的每日 GitHub 雷达。")
    lines.append("")
    lines.append("### 机会榜")
    lines.append("")
    lines.append("| 排名 | 仓库 | 分数 | 阶段 | Stars | 信号 | 构建角度 |")
    lines.append("|---:|---|---:|---|---:|---|---|")
    for index, item in enumerate(rows[:max_items], start=1):
        repo = item["repo"]
        radar = item["radar"]
        signal = "，".join(translate_signal(signal) for signal in radar.get("signals", [])[:2]) or "n/a"
        lines.append(
            "| {rank} | [{name}]({url}) | {score} | {stage} | {stars} | {signal} | {angle} |".format(
                rank=index,
                name=repo["full_name"],
                url=repo["url"],
                score=radar["score"],
                stage=radar["stage"],
                stars=repo["stars"],
                signal=escape_table(signal),
                angle=escape_table(translate_angle(radar["angle"])),
            )
        )

    lines.append("")
    lines.append("### 构建简报")
    lines.append("")
    for item in rows[: min(8, max_items)]:
        repo = item["repo"]
        radar = item["radar"]
        signals = "，".join(translate_signal(signal) for signal in radar.get("signals", [])) or "暂无强信号。"
        lines.append(f"#### {repo['full_name']}")
        lines.append("")
        lines.append(f"- URL: {repo['url']}")
        lines.append(f"- Score: {radar['score']} ({radar['stage']})")
        lines.append(f"- 为什么现在值得看：{signals}")
        lines.append(f"- 构建角度：{translate_angle(radar['angle'])}")
        lines.append("- 快速验证：发布一页 demo README，询问维护者/用户这个 companion tool 是否应该存在，再发 3 条中立的 fake-door 评论或帖子。")
        if item.get("issue_error"):
            lines.append("- Issue 样本：因 GitHub API 限流或拒绝请求而跳过。")
        top_issues = radar.get("top_issues", [])
        if top_issues:
            lines.append("- Issue 样本：")
            for issue in top_issues[:3]:
                lines.append(
                    f"  - [{issue.get('title')}]({issue.get('url')}) "
                    f"({issue.get('comments', 0)} comments, {issue.get('reactions', 0)} reactions)"
                )
        elif not item.get("issue_error"):
            lines.append("- Issue 样本：采样窗口内没有找到需求型 issue。")
        lines.append("")

    lines.append("### 运营备注")
    lines.append("")
    lines.append("- 优先做窄的 companion tools，而不是直接 fork 上游项目。")
    lines.append("- Stars 来自实用性和重复分发：每日报告、demo、issue 回复和短内容。")
    lines.append("- 高分只是 probe 的理由，不是立刻做大产品的证明。")
    lines.append("")
    lines.append('<a id="english"></a>')
    lines.append("")
    lines.append("## English")
    lines.append("")
    lines.append(f"Generated: `{generated_at}`")
    lines.append("")
    lines.append("A daily GitHub radar for AI agent skills, MCP servers, prompts, and agent-native developer tools.")
    lines.append("")
    lines.append("### Top Opportunities")
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
    lines.append("### Build Briefs")
    lines.append("")
    for item in rows[: min(8, max_items)]:
        repo = item["repo"]
        radar = item["radar"]
        lines.append(f"#### {repo['full_name']}")
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

    lines.append("### Operator Notes")
    lines.append("")
    lines.append("- Prefer narrow companion tools over upstream forks.")
    lines.append("- Stars follow utility plus repeated distribution: daily report, demo GIF, issue replies, and short-form posts.")
    lines.append("- Treat a high score as a reason to probe, not as proof that a full product should be built.")
    lines.append("")
    return "\n".join(lines)


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def translate_signal(value: str) -> str:
    return SIGNAL_ZH.get(value, value)


def translate_angle(value: str) -> str:
    return ANGLE_ZH.get(value, value)
