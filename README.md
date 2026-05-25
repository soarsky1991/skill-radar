# Agent Skill Radar

**Daily GitHub radar for AI agent skills, MCP servers, prompts, and agent-native developer tools.**

[![Daily Radar](https://github.com/soarsky1991/skill-radar/actions/workflows/daily-radar.yml/badge.svg)](https://github.com/soarsky1991/skill-radar/actions/workflows/daily-radar.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/soarsky1991/skill-radar?style=social)](https://github.com/soarsky1991/skill-radar/stargazers)

Most builders do not need another giant awesome list. They need a repeatable way to notice where developer demand is forming, decide what is worth building, and publish evidence before opening another random repo.

Agent Skill Radar turns public GitHub signals into a daily build brief:

| Step | What happens | Output |
|---|---|---|
| Scan | Search GitHub for agent skills, MCP servers, prompts, context tools, and agent-native CLIs. | Raw repo and issue data |
| Score | Rank by heat, freshness, issue demand, extensibility, creator fit, novelty, and saturation. | Opportunity score and stage |
| Brief | Convert the top repos into concrete companion-tool angles. | Build briefs with issue evidence |
| Publish | Commit a dated report every day. | Markdown reports for GitHub, blogs, and short posts |
| Build | Use the strongest repeat signals to choose the next small repo. | Less random shipping |

## Latest Radar

The current public report lives at [reports/latest.md](reports/latest.md).

Example signal from the first run:

| Rank | Opportunity | Build angle |
|---:|---|---|
| 1 | `addyosmani/agent-skills` | Cross-agent skill index, installer, or quality benchmark |
| 2 | `getsentry/XcodeBuildMCP` | MCP registry, security checker, config generator, or compatibility layer |
| 3 | `HKUDS/CLI-Anything` | Agent-native CLI wrapper with JSON output and deterministic workflows |

## Who This Is For

- Developers building tools around Codex, Claude Code, Copilot, Cursor, Gemini CLI, or MCP.
- Indie hackers who want evidence before committing to a new open-source idea.
- Maintainers who want to understand demand patterns around skills, prompts, and agent workflows.
- Technical creators who turn GitHub research into useful public reports.

## Quick Start

```bash
git clone https://github.com/soarsky1991/skill-radar.git
cd skill-radar
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agent-skill-radar run --limit-per-query 8 --issue-limit 4
```

Set a token for higher GitHub API limits:

```bash
export GITHUB_TOKEN=github_token_here
```

Outputs:

```text
data/YYYY-MM-DD.json
data/latest.json
reports/YYYY-MM-DD.md
reports/latest.md
```

## CLI

Collect scored JSON:

```bash
agent-skill-radar collect \
  --limit-per-query 12 \
  --issue-limit 6 \
  --days 45 \
  --out data/latest.json
```

Render a report:

```bash
agent-skill-radar report \
  --input data/latest.json \
  --out reports/latest.md
```

Run the daily pipeline:

```bash
agent-skill-radar run
```

Add a custom GitHub search query:

```bash
agent-skill-radar collect \
  --query "agent memory coding assistant stars:>100 created:>=2025-01-01" \
  --out data/custom.json
```

## Scoring Model

The score is a practical build signal, not an investment metric.

- Heat: stars, forks, and existing audience.
- Freshness: recent repository activity.
- Velocity proxy: stars per day since creation.
- Issue demand: comments, reactions, and demand-shaped titles.
- Extensibility: whether the repo naturally supports plugins, skills, MCP, CLI, prompts, or templates.
- Creator fit: whether it can become a visible workflow, tutorial, benchmark, or content series.
- Novelty: whether the ecosystem is young enough to have gaps.
- Saturation penalty: whether a giant ecosystem is already too mature.

Stages:

- `build-now`: create a proof of concept immediately.
- `probe-this-week`: publish a fake-door README, issue reply, or demo post.
- `content-first`: cover the topic, watch responses, then build.
- `archive`: keep for reference.

## Operating Loop

This repo is built to be run in public.

- Daily: commit one radar report.
- Twice weekly: turn one high-score gap into a short public breakdown.
- Weekly: publish a trend note and ask for missing repos.
- Every two weeks: decide whether the strongest repeated signal deserves a companion project.

## Roadmap

- Star delta snapshots.
- Repo allowlist and denylist.
- Issue clustering by demand type.
- Compatibility fields for Codex, Claude Code, Copilot, Cursor, Gemini CLI, and MCP.
- GitHub Pages dashboard.
- One-click brief template for validating a companion repo.

## Contributing

Open an issue with:

- a repo or ecosystem you think should be tracked;
- a noisy result that should be filtered;
- a scoring signal that would make the radar more useful.

Small, evidence-backed suggestions are more useful than broad category requests.

## License

MIT
