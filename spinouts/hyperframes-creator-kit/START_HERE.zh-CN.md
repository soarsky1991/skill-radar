# Start Here: 10 分钟做出第一个可信教程视频

这个仓库的目标不是教你堆特效，而是让你用 HyperFrames 做出一个别人能相信、能复现、愿意收藏的教程视频。

第一条路线只做一件事：用真实证据做一个 30 秒教程短片。

## 你会得到什么

- 一个 30 秒教程视频结构。
- 一个真实 proof asset 清单：录屏、截图、终端输出或渲染结果。
- 一个 HyperFrames composition 的制作检查表。
- 一个发布包：标题、封面方向、SRT、平台风险审稿。

## 适合谁

- 想把技术流程讲成短视频的开发者。
- 想让 AI agent 帮忙做视频，但不想产出空洞素材的人。
- 想围绕 HyperFrames 做教程、模板、课程或开源项目的人。

## 快速路线

1. 先读第一课：
   `lessons/lesson-01-proof-driven-30s-video/README.md`

2. 准备一个 proof asset：
   - 一段 10-20 秒真实屏幕录制，展示你真的做了某个操作。
   - 或 2-3 张截图，展示输入、操作、输出。
   - 或一段终端输出，证明检查命令通过。

3. 用 `SKILL.md` 指挥 agent：

```text
Use the HyperFrames Creator Kit workflow.
Create a 30-second proof-driven tutorial video from this screen recording.
The viewer should understand the input, operation, output, and check result.
```

4. 做完后用这个判断能不能发布：
   - 前 3 秒是否看到结果？
   - 是否有真实操作证据？
   - 是否有字幕或步骤卡片？
   - 是否跑过检查？
   - 是否有发布包和风险审稿？

## 最小目录建议

```text
my-video/
├─ index.html
├─ assets/
│  ├─ proof-screen-recording.mp4
│  ├─ screenshot-before.png
│  └─ screenshot-after.png
├─ captions/
│  └─ zh-CN.srt
├─ publish/
│  ├─ title.md
│  ├─ cover-brief.md
│  └─ risk-review.md
└─ README.md
```

## 成功标准

这个项目的第一课通过，不是因为视频看起来很炫，而是因为陌生人能回答：

- 这人在教什么？
- 我能不能照着做？
- 他有没有真的跑过？
- 我下一步该点哪里或改哪里？

如果四个答案都清楚，就已经比大多数“AI 视频 demo”更像教程产品了。
