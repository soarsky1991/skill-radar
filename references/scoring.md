# Scoring Reference

Languages: [简体中文](#zh-cn) · [English](#english)

<a id="zh-cn"></a>

## 简体中文

Agent Skill Radar 使用公开 GitHub metadata 和少量 issue 样本，为项目机会评分。

### 评分维度

| 维度 | 含义 | 为什么重要 |
|---|---|---|
| Heat | Stars 和 forks | 已有受众与社会证明 |
| Freshness | 近期 push | 生态仍然活跃 |
| Velocity proxy | 按创建时间估算的 stars/day | 即使没有历史 star 数据，也能粗略判断增长速度 |
| Issue demand | Comments、reactions、需求关键词 | 用户正在提出具体需求 |
| Extensibility | Skill、MCP、CLI、plugin、prompt、template 信号 | 小型 companion project 有存在空间 |
| Creator fit | Docs、content、markdown、publishing、design 信号 | 更容易通过教程和 demo 分发 |
| Novelty | 生态足够新，仍有空位 | 不太可能已经被完全占领 |
| Saturation penalty | 特别大或特别老的生态 | 小项目更难脱颖而出 |

### 决策阈值

- 80+：现在做 proof of concept。
- 65-79：本周验证。
- 45-64：先做内容，观察反馈。
- <45：归档。

### 人工调整

满足这些条件时，可以上调：

- 多个 repo 出现同类 issue。
- 用户分享脚本或多步骤 workaround。
- 维护者明确表示该功能不在上游范围内。
- 这个想法有清晰 demo GIF。

满足这些条件时，可以下调：

- repo 主要是热闹，真实用户很少。
- 想法需要深度改上游。
- 没有可信分发渠道。
- 问题只是 bug，不是持久工作流。

<a id="english"></a>

## English

Agent Skill Radar scores project opportunities from public GitHub metadata and a small issue sample.

### Dimensions

| Dimension | Meaning | Why it matters |
|---|---|---|
| Heat | Stars and forks | Existing audience and social proof |
| Freshness | Recent pushes | The ecosystem is alive |
| Velocity proxy | Stars per day since creation | Fast adoption, even without historical star data |
| Issue demand | Comments, reactions, demand keywords | Users are asking for something |
| Extensibility | Skill, MCP, CLI, plugin, prompt, template signals | A small companion project can exist |
| Creator fit | Docs, content, markdown, publishing, design signals | Easier to distribute through tutorials and demos |
| Novelty | Young enough to have gaps | Less likely to be fully captured |
| Saturation penalty | Very large or old ecosystems | Harder for a small project to stand out |

### Decision Thresholds

- 80+: build a proof of concept now.
- 65-79: validate this week.
- 45-64: make content first and watch responses.
- <45: archive.

### Manual Override

Override upward when:

- Multiple repos show the same issue.
- Users share scripts or multi-step workarounds.
- Maintainers explicitly say the feature is out of scope.
- The idea has a clear demo GIF.

Override downward when:

- The repo is mostly hype with few real users.
- The idea requires deep upstream changes.
- There is no credible distribution channel.
- The problem is a bug, not a durable workflow.
