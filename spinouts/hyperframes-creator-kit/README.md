# HyperFrames Creator Kit

<p align="center">
Languages: <a href="#zh-cn">简体中文</a> · <a href="#english">English</a>
</p>

<a id="zh-cn"></a>

## 简体中文

**把 HyperFrames、AI agent skills、真实录屏和发布前审稿流程，组织成可复用的教程视频生产系统。**

这个包不是另一个松散的素材清单。它的目标是帮创作者做出可以被收藏、复现、二创和开源协作的技术教程：先证明一个真实案例，再用 HyperFrames 做结构化合成、字幕、动效、音频和多平台交付。

### 为什么现在做

2026-06-01 的 GitHub 调研显示，高星教程仓库反复命中同一组模式：

- 明确学习承诺：`build-your-own-x`、`developer-roadmap`、`system-design-primer`、`coding-interview-university`。
- 可收藏目录：按语言、路径、主题、课程周或学习任务组织。
- 可执行进度：任务清单、lesson、代码样例、练习、Anki、项目实作。
- 社区入口：贡献指南、issue、讨论、翻译、good first contribution。
- 视觉信任：README 顶部说明、表格、图片、徽章、license、示例输出。

HyperFrames 的机会不是只发一个剪辑模板，而是开源一套“从真实证据到教程视频”的工作流。

### 这个目录提供什么

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 可复制到 Codex/agent skills 的 HyperFrames creator workflow skill |
| `research/github-tutorial-repo-patterns-2026-06-01.md` | 50k+ 星教程仓库调研、委员会设计和首版定位 |
| `templates/tutorial-repo-blueprint.md` | 爆款教程 repo 的 README、目录和发布节奏模板 |

### 推荐开源定位

仓库名首选：`hyperframes-creator-kit`

一句话：**Build AI tutorial videos with HyperFrames, real proof assets, and agent-run production gates.**

第一版不要做成大而全的框架。先交付三个能被立刻理解的东西：

1. 一个 `SKILL.md`，让 agent 知道如何制作 HyperFrames 教程视频。
2. 一个可跑的 lesson：从素材、字幕、动效到 `npm run check`。
3. 一个 publishing pack：封面、SRT、发布文案、风险审稿清单。

### 委员会

| 委员会 | 负责什么 | 通过标准 |
|---|---|---|
| Repo Positioning | 名字、承诺、受众、首屏 README | 30 秒内知道为谁解决什么问题 |
| Tutorial Design | lesson 顺序、练习、可收藏点 | 新手能按步骤复现 |
| Proof Director | 真实录屏、截图、输出物、失败修复 | 每个教学 claims 都有证据 |
| HyperFrames Engineer | composition、timing、字幕、动效、音频 | `npm run check` 通过，预览不空白 |
| Growth Analyst | 参考仓库、关键词、外部传播 | 标题和目录命中搜索需求 |
| OSS Maintainer | license、贡献入口、issue 模板 | 陌生贡献者知道怎么帮忙 |
| Integrity Reviewer | 版权、AI 标注、夸张承诺、平台风险 | 不用虚假结果换增长 |

### 首周发布节奏

Day 1: 发布 skill、研究报告、README 蓝图。

Day 2: 补第一个完整 lesson：`build a 30s tutorial clip from a real screen recording`。

Day 3: 补示例视频截图、SRT、cover、publish pack。

Day 4: 发英文 launch post 和中文拆解帖。

Day 5: 收集 issue 里的缺口，决定第二个 lesson。

<a id="english"></a>

## English

**A reusable agent skill and tutorial-repo blueprint for producing proof-driven HyperFrames creator videos.**

HyperFrames Creator Kit turns real screen recordings, proof assets, subtitles, motion cards, audio, and review gates into a repeatable tutorial-video workflow.

The first public version is intentionally small:

- `SKILL.md` teaches an agent how to run the workflow.
- `research/github-tutorial-repo-patterns-2026-06-01.md` summarizes what high-star GitHub tutorial repos have in common.
- `templates/tutorial-repo-blueprint.md` gives a README and launch structure for a standalone tutorial repo.

Recommended standalone repo name: `hyperframes-creator-kit`.

One-line promise: **Build AI tutorial videos with HyperFrames, real proof assets, and agent-run production gates.**

The core rule: do not ship decorative AI video as a tutorial. Every lesson needs a real proof asset, a runnable check, and a clear publishing handoff.
