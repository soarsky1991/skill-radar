# Lesson 01: 从真实录屏到 30 秒教程视频

目标：用 HyperFrames 把一个真实操作过程做成 30 秒教程视频。第一课不追求复杂动画，只追求可信、清楚、可复现。

## 成品结构

| 时间 | 画面 | 教学任务 |
|---:|---|---|
| 0-3s | 最终结果或 before/after | 先告诉观众能得到什么 |
| 3-8s | 输入素材或问题现场 | 让问题具体化 |
| 8-20s | 真实录屏 + 步骤卡片 | 展示关键操作 |
| 20-26s | 输出结果 + 检查命令 | 证明流程跑通 |
| 26-30s | 可复制清单 | 给观众下一步 |

## 输入

至少准备一种真实 proof asset：

- 录屏：展示一个操作、一次预览、一次渲染或一次检查。
- 截图：展示输入、过程、输出。
- 终端输出：展示 lint、preview、render 或其它检查结果。

不要用虚构终端、假数据、未授权素材或含密钥的截图。

## 制作步骤

### 1. 写一句话承诺

模板：

```text
用 HyperFrames 把 [输入素材] 做成 [可发布的视频/片段/模板]，并用 [检查方式] 证明它跑通。
```

示例：

```text
用 HyperFrames 把一段真实屏幕录制做成 30 秒教程短片，并用本地检查命令证明 composition 没有结构错误。
```

### 2. 标注 proof asset

| 文件 | 用途 | 是否可公开 | 风险 |
|---|---|---|---|
| `proof-screen-recording.mp4` | 展示真实操作 | 是/否 | 检查是否含账号、密钥、通知 |
| `screenshot-after.png` | 展示最终结果 | 是/否 | 检查版权和个人信息 |
| `check-output.txt` | 展示检查结果 | 是/否 | 不要包含本地 secret 路径 |

### 3. 设计 5 张信息卡

- Result：这个视频最后做出什么。
- Input：原始素材或问题是什么。
- Steps：关键操作 1-2-3。
- Check：如何确认跑通。
- Reuse：观众下一步怎么复制。

### 4. 交给 HyperFrames agent

```text
Using the HyperFrames Creator Kit workflow, build a 30-second tutorial composition.

Requirements:
- Use the real proof asset as the trust anchor.
- Add 5 timed text cards: Result, Input, Steps, Check, Reuse.
- Keep all visible timed elements as clips.
- Add subtitles or an SRT handoff.
- Run the local check command after editing.
- Produce a publishing pack with title, cover direction, and risk review.
```

### 5. 检查

最低检查清单：

- 首屏 3 秒能看到结果。
- 真实 proof asset 出现在视频主体里。
- 字幕不遮挡关键操作。
- 每个大 claim 都有截图、录屏、输出或检查支撑。
- 检查命令已运行，失败原因已记录。
- 发布包没有密钥、账号、临时链接、未授权素材。

## 常见失败

| 失败 | 原因 | 修复 |
|---|---|---|
| 看起来像广告，不像教程 | 结果太多，操作太少 | 把 45% 以上时长留给真实操作 |
| 动效很多但没信息 | 装饰性 B-roll 过量 | 每个生成镜头必须承担解释、转场、对比或复盘 |
| 观众不知道怎么复现 | 缺少输入和检查 | 加素材清单、命令、输出截图 |
| 平台发布风险高 | 截图含隐私或夸张承诺 | 做风险审稿，删掉账号、密钥、绝对化说法 |

## 通过标准

标记为 `ready` 需要同时满足：

- 有真实 proof asset。
- 有 30 秒内完整教学闭环。
- 有检查记录。
- 有发布包。
- 有风险审稿。

否则标记为：

- `needs_proof_asset`
- `needs_check`
- `needs_rewrite`
- `draft_only`
