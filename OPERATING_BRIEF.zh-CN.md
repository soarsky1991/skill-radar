# Agent Skill Radar 首个项目运营 Brief

## 结论

第一个项目做 `Agent Skill Radar`，不是直接做一个具体插件。

原因：你现在最大的瓶颈不是代码能力，而是持续找到高需求题材、判断该不该做、以及把研究过程转化成 GitHub 更新和传播内容。这个项目本身就是“选题机器”，同时也是一个可公开涨星的工具。

## 对标拆解

`geekjourneyx` 的有效模式不是单仓库爆发，而是围绕一个明确主线持续铺生态：

- 个人主页负责定位。
- 主产品负责承接需求。
- 插件、MCP、Obsidian、飞书等周边仓库负责覆盖不同入口。
- README、截图、教程和社区入口负责转化。
- 小仓库之间互相导流，形成项目矩阵。

我们要学这个结构，但不要复制同一个题材。对方围绕“公众号发布基础设施”，我们先围绕“AI Agent 生态选题和需求雷达”建立主线。

## 多维度判断

### 1. 需求维度

AI Agent skills、MCP、agent-native CLI、context engineering 都在快速增长。开发者每天都在找：

- 哪些技能/插件值得安装？
- 哪些 MCP 服务器可靠？
- 哪些 Agent 周边工具有真实需求？
- 下一个开源项目该做什么？

这个项目直接解决“选题和判断”的前置需求。

### 2. 传播维度

这个方向天然适合传播：

- 每日榜单。
- 每周趋势报告。
- “我扫了 100 个 Agent 项目，发现 7 个机会”这类内容。
- 可视化表格和 GitHub issue 证据。
- 容易被其他开发者收藏。

### 3. 构建维度

MVP 不需要复杂模型，先用 GitHub API + 规则评分就能跑起来。后续可以逐步加：

- 星标增长快照。
- README 解析。
- issue 聚类。
- 兼容性矩阵。
- GitHub Pages Dashboard。
- LLM 生成 build brief。

### 4. 差异化维度

已有项目多是 curated list 或单一需求雷达。我们的差异化是：

- 自动采集，不只手工列表。
- 面向“该做什么项目”，不是只看热门。
- 同时输出数据、报告、build brief 和 fake-door probe。
- 兼容 Codex / Claude Code / Copilot / MCP 生态，而不是押注单一平台。

### 5. 运营维度

这个项目适合日常维护：

- 每天跑一次报告。
- 每天从报告里挑 1 个发现发帖。
- 每周沉淀一篇周报。
- 每两周从最高分机会里孵化一个新 repo。

它能把“学习和爬取题材至少占一半”变成固定流程。

### 6. 风险维度

主要风险：

- GitHub 搜索结果有噪音。
- 评分容易被 star 数放大。
- issue 采样会遇到 API 限流。
- 只做榜单容易变成低价值搬运。

当前已经处理：

- 用 `gh auth token` 自动提升 API 限额。
- 单仓库 issue 采样失败时降级不中断。
- 只把需求型 issue 纳入需求评分。
- 输出 build brief，避免只做列表。

## 两周执行节奏

### 第 1-2 天

- 完成 CLI、README、首份报告。
- 创建 GitHub 仓库。
- 设置 topics、description、Actions。

### 第 3-4 天

- 加 `latest.md` 和 GitHub Pages 首页。
- README 放首屏榜单截图或报告摘要。
- 发第一条内容：为什么要做 Agent Skill Radar。

### 第 5-7 天

- 每天发布一份趋势报告。
- 每天选 1 个高分仓库做拆解。
- 去相关 issue 下做中立验证，不直接推销。

### 第 8-10 天

- 加入 star delta 快照。
- 加入 repo allowlist / denylist。
- 增加“兼容 Codex / Claude / Copilot / Gemini / MCP”的字段。

### 第 11-14 天

- 从报告里挑最高确定性的子机会，孵化第二个仓库。
- 如果第一周反馈好，继续加强 radar；如果反馈弱，就把 radar 当内部选题系统，转向它发现的具体工具。

## 第一个可衍生项目候选

从首份报告看，优先考虑：

1. `cross-agent-skill-index`
   - 做跨 Codex / Claude Code / Copilot / Gemini 的 skill 兼容性索引。
   - 适合从 `addyosmani/agent-skills`、`pro-workflow`、`marketingskills` 这类仓库切入。

2. `mcp-config-doctor`
   - 检查 MCP 配置、权限、可用性和安全风险。
   - 适合从 `XcodeBuildMCP`、`headroom`、`hexstrike-ai` 等仓库切入。

3. `agent-cli-json-harness`
   - 给 agent-native CLI 统一包一层 JSON 输出和可测试协议。
   - 适合从 `CLI-Anything`、`DeepSeek-Reasonix`、`rmux` 等方向切入。

当前建议：先把 `Agent Skill Radar` 运营 7 天，不急着开第二个仓库。第 7 天用数据选一个最强衍生项目。

