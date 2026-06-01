# Tutorial Repo Blueprint

Use this when turning HyperFrames Creator Kit into a standalone public repository.

## README Skeleton

````markdown
# HyperFrames Creator Kit

<p align="center">
Languages: <a href="#zh-cn">简体中文</a> · <a href="#english">English</a>
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![HyperFrames](https://img.shields.io/badge/HyperFrames-video-blue)](https://hyperframes.heygen.com/introduction)

<a id="zh-cn"></a>

## 简体中文

一句话：用 HyperFrames、真实录屏和 agent skills，把技术流程做成可复现、可发布、可收藏的 AI 教程视频。

### 你能做什么

- 把一次真实操作录屏变成 30-90 秒教程视频。
- 自动生成字幕、步骤卡、动效提示和发布包。
- 用委员会流程检查证据、版权、平台风险和可教学性。

### 5 分钟开始

```bash
git clone https://github.com/<owner>/hyperframes-creator-kit.git
cd hyperframes-creator-kit/lessons/01-real-screen-recording-to-tutorial-video
npm install
npm run check
```

### Lessons

| Lesson | What you build | Proof asset | Status |
|---|---|---|---|
| 01 | Real screen recording to tutorial video | Screen recording + subtitles | Ready |
| 02 | Add BGM/SFX without covering narration | Audio stems | Planned |
| 03 | Package for X, Bilibili, and Xiaohongshu | Cover + SRT + copy | Planned |

### Why this exists

Most AI video demos look polished but do not prove anything. This repo starts from real evidence, then uses HyperFrames for deterministic composition and agent skills for repeatable production.

### Contributing

Good first contributions:

- Add a missing platform publish checklist.
- Add a small HyperFrames lesson.
- Report a render/check failure with a minimal example.
- Improve a subtitle style or motion card pattern.

<a id="english"></a>

## English

One line: use HyperFrames, real screen recordings, and agent skills to make reproducible AI tutorial videos.
````

## Folder Plan

```text
lessons/
  01-real-screen-recording-to-tutorial-video/
    README.md
    index.html
    package.json
    assets/
      README.md
    publish-pack.md
committees/
  proof-director.md
  tutorial-design.md
  integrity-review.md
templates/
  lesson-brief.md
  publish-pack.md
research/
  github-tutorial-repo-patterns-2026-06-01.md
```

## First Issue Templates

### Missing Lesson Request

```markdown
## What do you want to learn?

## What real proof asset can show the workflow?

## Target platform

## What should the final video/package include?
```

### Render Failure Report

```markdown
## What command failed?

## Minimal reproduction

## Expected output

## Actual output

## Screenshot or terminal excerpt
```

## Launch Post

```text
I kept seeing AI video tutorials that looked impressive but did not prove the workflow.

So I started HyperFrames Creator Kit: a small open-source skill and lesson system for turning real screen proof into tutorial videos.

It does three things:
1. Captures proof first.
2. Builds deterministic HyperFrames compositions.
3. Packages subtitles, cover, copy, and review gates for publishing.

First version:
<repo link>
Research notes:
<research link>
```

## Readiness Gate

Do not call the repo launch-ready until:

- README first screen states the promise and quick start.
- License exists.
- Lesson 01 runs through check.
- At least one screenshot or output sample is visible.
- Contribution path exists.
- Research note explains why the repo shape was chosen.
