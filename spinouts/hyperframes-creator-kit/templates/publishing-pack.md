# Publishing Pack Template

用这个模板给每个教程视频配发布包。它的目标是让视频从“能看”变成“能发、能审、能复盘”。

## Title

中文标题：

```text
用 HyperFrames 把真实录屏做成 30 秒教程视频
```

英文标题：

```text
Build a 30-second proof-driven tutorial video with HyperFrames
```

## Hook

前 3 秒要回答：

- 结果是什么？
- 为什么值得看？
- 这个结果是否真实可复现？

## Cover Direction

- 展示 before/after。
- 放 1 个大结果，不放 6 个小截图。
- 不用绝对化词：最强、永久免费、必爆、零成本。
- 保留平台安全区域。

## Caption / SRT

内部字幕：

- 字幕不遮挡关键操作。
- 每行不超过 18-22 个中文字符。
- 参数、命令、文件名使用等宽或高对比样式。

外部 SRT：

- 文件名：`<video-slug>.zh-CN.srt` 或 `<video-slug>.en.srt`
- UTF-8 编码。
- 时间戳和最终剪辑一致。

## Publish Copy

```text
这条视频拆解一个更靠谱的 AI 教程视频流程：

真实录屏 -> HyperFrames 合成 -> 字幕/步骤卡 -> 检查命令 -> 发布包

我把 skill 和教程仓库开源出来了，适合想做 AI 视频教程、产品更新视频、数据动画和技术讲解的人复用。
```

## Risk Review

| 项目 | 状态 | 备注 |
|---|---|---|
| 无密钥/token/验证码 | pass/fail |  |
| 无个人账号后台敏感信息 | pass/fail |  |
| 素材可公开使用 | pass/fail |  |
| AI 生成内容已按需标注 | pass/fail |  |
| 结果 claim 有 proof asset | pass/fail |  |
| 无夸张商业承诺 | pass/fail |  |
| SRT 与最终视频同步 | pass/fail |  |

## Post-publish Retrospective

- 哪个标题/封面最有效？
- 哪一段最值得收藏？
- 评论区问了什么？
- 哪个步骤不够清楚？
- 下一个 lesson 应该补什么？
