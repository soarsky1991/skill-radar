# Agent Skill Radar

<p align="center">
Languages: <a href="#zh-cn">简体中文</a> · <a href="#english">English</a>
</p>

[![Daily Radar](https://github.com/soarsky1991/skill-radar/actions/workflows/daily-radar.yml/badge.svg)](https://github.com/soarsky1991/skill-radar/actions/workflows/daily-radar.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/soarsky1991/skill-radar?style=social)](https://github.com/soarsky1991/skill-radar/stargazers)

<a id="zh-cn"></a>

## 简体中文

**面向 AI agent skills、MCP servers、prompts 和 agent-native developer tools 的每日 GitHub 雷达。**

大多数开发者不缺另一个 awesome list，真正缺的是一套可重复的方法：发现需求正在哪里形成，判断什么值得做，并在开新仓库之前先发布证据。

Agent Skill Radar 把公开 GitHub 信号变成每日 build brief。中文用户是这个项目优先服务的人群：开发者、技术创作者、AI 工具训练营、独立开发者和小团队，都可以用它做选题、选型、内容和产品化验证。

### 它怎么工作

| 步骤 | 做什么 | 输出 |
|---|---|---|
| 扫描 | 搜索 agent skills、MCP servers、prompts、context tools、agent-native CLIs。 | 原始仓库和 issue 数据 |
| 评分 | 按热度、活跃度、issue 需求、扩展性、创作者适配度、新颖度和饱和度排序。 | 机会分数和阶段 |
| 简报 | 把高分仓库转成可执行的 companion-tool 角度。 | 带 issue 证据的 build brief |
| 发布 | 每天提交一份 Markdown 报告。 | GitHub、博客、图文和短视频都能引用的报告 |
| 构建 | 用重复出现的强信号决定下一个小工具。 | 更少随机开坑 |

### 最新雷达

当前公开报告：[reports/latest.md](reports/latest.md)

首批信号示例：

| 排名 | 机会 | 构建角度 |
|---:|---|---|
| 1 | `addyosmani/agent-skills` | 跨 agent 的 skill index、installer 或 quality benchmark |
| 2 | `getsentry/XcodeBuildMCP` | MCP registry、security checker、config generator 或 compatibility layer |
| 3 | `HKUDS/CLI-Anything` | 带 JSON 输出和确定性工作流的 agent-native CLI wrapper |

### 适合谁

- 想围绕 Codex、Claude Code、Copilot、Cursor、Gemini CLI 或 MCP 做工具的开发者。
- 想先看证据再决定开源项目方向的独立开发者。
- 想把 GitHub 研究变成公众号、小红书、视频、社群选题的技术创作者。
- 想筛选 MCP/Agent 工具、做内部培训或产品化验证的小团队。

### 快速开始

```bash
git clone https://github.com/soarsky1991/skill-radar.git
cd skill-radar
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agent-skill-radar run --limit-per-query 8 --issue-limit 4
```

提高 GitHub API 限额：

```bash
export GITHUB_TOKEN=github_token_here
```

输出：

```text
data/YYYY-MM-DD.json
data/latest.json
reports/YYYY-MM-DD.md
reports/latest.md
```

### CLI

采集评分 JSON：

```bash
agent-skill-radar collect \
  --limit-per-query 12 \
  --issue-limit 6 \
  --days 45 \
  --out data/latest.json
```

从 JSON 渲染报告：

```bash
agent-skill-radar report \
  --input data/latest.json \
  --out reports/latest.md
```

运行每日流水线：

```bash
agent-skill-radar run
```

添加自定义 GitHub 搜索：

```bash
agent-skill-radar collect \
  --query "agent memory coding assistant stars:>100 created:>=2025-01-01" \
  --out data/custom.json
```

### 评分模型

这个分数是实用的构建信号，不是投资指标。

- Heat：stars、forks 和已有受众。
- Freshness：近期仓库活跃度。
- Velocity proxy：按创建时间估算的 stars/day。
- Issue demand：comments、reactions 和需求型 issue 标题。
- Extensibility：是否自然适合 plugin、skill、MCP、CLI、prompt 或 template。
- Creator fit：是否适合做教程、benchmark、公开报告或内容系列。
- Novelty：生态是否足够新，还有明显空位。
- Saturation penalty：生态是否已经太成熟、太拥挤。

阶段：

- `build-now`：可以立刻做 proof of concept。
- `probe-this-week`：先发 fake-door README、issue reply 或 demo post。
- `content-first`：先做内容观察反馈，再决定要不要构建。
- `archive`：保留为参考。

### 运营节奏

- 每日：提交一份 radar report。
- 每周两次：把一个高分 gap 拆成公开内容。
- 每周：发布趋势笔记，请社区补充遗漏仓库。
- 每两周：判断最强重复信号是否值得孵化成 companion project。

### 路线图

- Star delta snapshots。
- Repo allowlist / denylist。
- Issue demand 聚类。
- Codex、Claude Code、Copilot、Cursor、Gemini CLI、MCP 兼容性字段。
- GitHub Pages dashboard。
- Companion repo 验证模板。

### 贡献

欢迎开 issue 提供：

- 应该被追踪的 repo 或生态；
- 需要过滤的噪音结果；
- 更有用的评分信号；
- 能证明真实需求的 issue、discussion 或 release 证据。

小而具体、有证据的建议最有价值。

<a id="english"></a>

## English

**Daily GitHub radar for AI agent skills, MCP servers, prompts, and agent-native developer tools.**

Most builders do not need another giant awesome list. They need a repeatable way to notice where developer demand is forming, decide what is worth building, and publish evidence before opening another repo.

Agent Skill Radar turns public GitHub signals into a daily build brief. Chinese-speaking builders are the first audience for monetization and community growth, while the English version stays complete so the project can connect with the global open-source and AI agent ecosystem.

### How It Works

| Step | What happens | Output |
|---|---|---|
| Scan | Search GitHub for agent skills, MCP servers, prompts, context tools, and agent-native CLIs. | Raw repo and issue data |
| Score | Rank by heat, freshness, issue demand, extensibility, creator fit, novelty, and saturation. | Opportunity score and stage |
| Brief | Convert the top repos into concrete companion-tool angles. | Build briefs with issue evidence |
| Publish | Commit a dated Markdown report every day. | Reports for GitHub, blogs, newsletters, and short-form content |
| Build | Use repeated strong signals to choose the next small tool. | Less random shipping |

### Latest Radar

The current public report lives at [reports/latest.md](reports/latest.md).

Example signal from the first run:

| Rank | Opportunity | Build angle |
|---:|---|---|
| 1 | `addyosmani/agent-skills` | Cross-agent skill index, installer, or quality benchmark |
| 2 | `getsentry/XcodeBuildMCP` | MCP registry, security checker, config generator, or compatibility layer |
| 3 | `HKUDS/CLI-Anything` | Agent-native CLI wrapper with JSON output and deterministic workflows |

### Who This Is For

- Developers building tools around Codex, Claude Code, Copilot, Cursor, Gemini CLI, or MCP.
- Indie hackers who want evidence before committing to a new open-source idea.
- Technical creators turning GitHub research into articles, videos, newsletters, or community discussions.
- Small teams evaluating MCP tools, agent workflows, and productization paths.

### Quick Start

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

### CLI

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

### Scoring Model

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

### Operating Loop

- Daily: commit one radar report.
- Twice weekly: turn one high-score gap into a public breakdown.
- Weekly: publish a trend note and ask for missing repos.
- Every two weeks: decide whether the strongest repeated signal deserves a companion project.

### Roadmap

- Star delta snapshots.
- Repo allowlist and denylist.
- Issue clustering by demand type.
- Compatibility fields for Codex, Claude Code, Copilot, Cursor, Gemini CLI, and MCP.
- GitHub Pages dashboard.
- One-click brief template for validating a companion repo.

### Contributing

Open an issue with:

- a repo or ecosystem you think should be tracked;
- a noisy result that should be filtered;
- a scoring signal that would make the radar more useful;
- issue, discussion, or release evidence that shows real demand.

Small, evidence-backed suggestions are more useful than broad category requests.

## License

MIT
