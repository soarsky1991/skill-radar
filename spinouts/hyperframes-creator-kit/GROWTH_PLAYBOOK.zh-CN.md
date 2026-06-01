# 爆款教程仓库增长手册

调研日期：2026-06-01

参考对象：`build-your-own-x`、`freeCodeCamp/freeCodeCamp`、`developer-roadmap`、`system-design-primer`、`coding-interview-university`、Microsoft `*-For-Beginners` 课程，以及中文的算法、面试、AI-agent 教程仓库。

## 为什么 50k+ star 教程仓库会传播

### 1. 名字就是搜索词

强仓库名字直接回答用户正在搜什么：

- `build-your-own-x`：我想自己造一个东西。
- `developer-roadmap`：我不知道该学什么。
- `system-design-primer`：我要准备系统设计。
- `coding-interview-university`：我需要一整套面试学习计划。
- `generative-ai-for-beginners`：我是新手，但想开始做生成式 AI。

HyperFrames 方向不要叫泛泛的 `video-tools`。更好的命名是：

- `hyperframes-creator-kit`
- `hyperframes-skillbook`
- `build-your-own-ai-video-workflow`

### 2. 它们解决昂贵焦虑

高星教程仓库通常不只是“有趣”，而是在解决会让人焦虑的问题：

- 找工作、面试、转行。
- 学 AI 不掉队。
- 做出真实项目，而不是只看概念。
- 第一次给开源项目提 PR。

本项目的焦虑点应该是：

> 我想用 AI 做教程视频，但不想产出看起来很假、不能复现、没有证据的东西。

### 3. README 先让人收藏

很多 star 发生在用户真正使用之前。README 第一屏必须让人觉得“这东西以后用得上”：

- 一句话承诺。
- 成品图或 GIF。
- 10 分钟 Quickstart。
- 学习路径。
- 模板和 lesson 表格。
- 贡献入口。

### 4. 有第一成功体验

真正的增长点不是章节数量，而是用户第一次成功：

- `rustlings` 给即时练习反馈。
- Microsoft 课程用固定周数、lesson 表格、代码样例降低心理负担。
- `build-your-own-x` 用“从零做一个真实系统”让内容天然可分享。

HyperFrames 的第一成功体验应该是：

```text
我拿到一段真实录屏 -> 生成 30 秒教程视频 -> 跑过检查 -> 有发布包
```

### 5. 贡献被拆得足够小

要让陌生人能帮忙，不要只写“欢迎贡献”。要列出小任务：

- 添加一个 proof asset 检查项。
- 添加一个失败案例。
- 添加一个 lesson 的截图。
- 补一个 SRT 示例。
- 翻译一个摘要段落。

## 本项目的增长打法

### GitHub 内

- README 首屏保留 5 个元素：承诺、成品、Quickstart、lesson map、contribution path。
- issue 模板围绕 lesson request、failed render、proof asset review。
- 每周 release note 写“本周你能做出什么视频”。
- 所有 lesson 都给 `ready / draft_only / needs_check` 状态。

### 中文内容

- 知乎：写“为什么 AI 视频教程必须先有真实 proof asset”。
- 掘金：写“用 HyperFrames 做第一个 30 秒教程视频”。
- B 站：先发成品，再拆解制作过程。
- 小红书：只发成品和清单，避免把 GitHub 当唯一入口。

### 英文扩散

- X：发 before/after GIF 和模板 thread。
- Reddit/HN：等第一个 demo 足够稳再发，不要早期空投。
- Upstream：把稳定经验回流到 HyperFrames issue/PR 或 showcase。

## 最危险的失败路径

- 写成 API 文档，没有第一课。
- 全是 AI 生成画面，没有真实操作证据。
- README 很长，但没有 10 分钟成功路径。
- 贡献者不知道能做什么。
- 声称“production ready”，但没有检查记录。

## 90 天指标

- 5 个 lesson。
- 3 个可复制模板。
- 1 个完整公开视频案例。
- 20 个小 issue。
- 5 个外部贡献。
- 1 个英文 Quickstart。
- 1 次与 HyperFrames 官方生态的公开互动。
