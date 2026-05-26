# Contributing

Languages: [简体中文](#zh-cn) · [English](#english)

<a id="zh-cn"></a>

## 简体中文

Agent Skill Radar 最需要的是带公开证据的建议。

好的贡献包括：

- 应该加入 radar 的 GitHub 仓库；
- 能找到更好 agent-native 工具的搜索 query；
- 需要过滤的噪音结果；
- 能提升构建判断质量的评分信号；
- 能显示真实需求的 issue 样本。

### 推荐仓库

请开 issue，并提供：

```text
Repository:
Why it matters:
Demand evidence:
Suggested category:
```

有效的 demand evidence 可以是 issue thread、discussion、release、star 增长模式，或用户反复提出的请求。

### 本地开发

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agent-skill-radar run --limit-per-query 8 --issue-limit 4
```

提交 PR 前运行：

```bash
python3 -m compileall agent_skill_radar
```

<a id="english"></a>

## English

Agent Skill Radar works best when suggestions are tied to public evidence.

Good contributions include:

- a GitHub repository that belongs in the radar;
- a query that finds better agent-native tools;
- a noisy result that should be filtered;
- a scoring signal that improves build-decision quality;
- a short issue sample that shows real developer demand.

### Suggest A Repository

Open an issue with:

```text
Repository:
Why it matters:
Demand evidence:
Suggested category:
```

Useful demand evidence can be an issue thread, discussion, release, star growth pattern, or repeated request from users.

### Local Development

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agent-skill-radar run --limit-per-query 8 --issue-limit 4
```

Before opening a pull request, run:

```bash
python3 -m compileall agent_skill_radar
```
