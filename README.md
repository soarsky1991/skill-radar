# Agent Skill Radar

[简体中文](README.zh-CN.md) · [Fixed-date case](docs/cases/2026-08-25-fixed-date-radar.md) · [Signal-to-brief case](docs/cases/signal-to-build-brief.md) · [Contributing](CONTRIBUTING.md)

![A single radar circle sits beside one plain signal card with two signal bars and one highlighted dot / 一个雷达圆旁放置一张极简信号卡，卡上有两条信号线和一个高亮点。](docs/assets/social-preview.png)

> **A small, reproducible GitHub research loop for AI agent skills, MCP servers, prompts, and agent-native developer tools.**

Start here: run the three-minute replay below, then compare its Markdown with the [fixed-date report for 2026-08-25](reports/2026-08-25.md) and its [source data](data/2026-08-25.json). The project does not claim to predict markets or business outcomes. It preserves the evidence behind a research decision so a reader can inspect it, challenge it, or reuse the method.

## What it does

Agent Skill Radar turns public GitHub repository and issue signals into a dated build brief.

| Step | Input | Output |
|---|---|---|
| Collect | configured GitHub search queries and recent issue samples | dated JSON with repository metadata, sampled issues, and scoring fields |
| Score | heat, freshness, issue demand, extensibility, creator fit, novelty, and saturation | a score plus a working stage |
| Render | one collected JSON file | a bilingual Markdown report with ranked opportunities and evidence links |
| Review | report, source links, and local context | a small next experiment, a rejection, or a request for more evidence |

The score is a research aid. It is not a forecast, investment signal, market-size estimate, product recommendation, or proof that a build brief should become a product.

## Three-minute replay

This replay is offline after installation: it renders the committed fixed-date data, rather than pretending to regenerate history from today's GitHub state.

![A real macOS Terminal run shows the fixed-date data rendered into Markdown, a byte-for-byte report match, and the replay-only boundary / 真实 macOS Terminal 运行显示固定日期数据被渲染为 Markdown、报告逐字节一致，并明确仅为回放。](docs/assets/terminal-fixed-date-replay.png)

The screenshot records a local replay on 2026-08-25. It supports only that the committed input rendered into the committed report in this environment; it is not a live GitHub collection, forecast, adoption metric, or business result. See the [media register](docs/evidence/media-register.yaml).

```bash
git clone https://github.com/soarsky1991/skill-radar.git
cd skill-radar
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agent-skill-radar report \
  --input data/2026-08-25.json \
  --out /tmp/agent-skill-radar-2026-08-25.md
```

Open `/tmp/agent-skill-radar-2026-08-25.md` and compare it with [the committed report](reports/2026-08-25.md). The output should preserve the same ranked items and evidence links because both are rendered from the same committed data file.

To collect a new live run, use a new date. GitHub access is required; `GITHUB_TOKEN` is optional but raises the API limit.

```bash
export GITHUB_TOKEN=github_token_here
agent-skill-radar run \
  --date "$(date -u +%F)" \
  --data-dir data \
  --report-dir reports
```

The live command writes four files: `data/<date>.json`, `reports/<date>.md`, `data/latest.json`, and `reports/latest.md`. Review the result before treating any ranked item as a real opportunity.

## Two complete, inspectable cases

### Case 1 — a fixed-date radar run

The [2026-08-25 fixed-date case](docs/cases/2026-08-25-fixed-date-radar.md) traces one committed run from the query configuration and JSON input to its rendered report. It identifies what can be reproduced locally and what cannot be reconstructed later, such as the external GitHub state at collection time.

### Case 2 — signal to build brief

The [signal-to-build-brief case](docs/cases/signal-to-build-brief.md) follows `addyosmani/agent-skills` in that report: a recorded score and issue samples lead to one bounded build angle. It shows how a signal becomes a question for a future experiment, not a claim that the experiment succeeded.

## How to read a build brief

A useful brief should answer six questions:

1. What is the specific problem or observed developer signal?
2. Which public repository, issue, discussion, or release supports it?
3. Which inputs and scoring fields were used?
4. What narrow build or research angle follows from those facts?
5. What would a small, reversible test look like?
6. What does the evidence **not** prove?

If the answer to the last question is missing, the brief is incomplete. Popularity, a recent commit, or one issue thread is not enough to establish durable demand.

## Scoring model

- **Heat:** visible repository attention.
- **Freshness:** recent activity in public metadata.
- **Velocity proxy:** a rough stars-per-day proxy, not growth verification.
- **Issue demand:** sampled issue titles, comments, and reactions.
- **Extensibility:** whether a repo plausibly supports a skill, plugin, MCP server, CLI, prompt, or template.
- **Creator fit:** whether the subject supports a useful public explanation or benchmark.
- **Novelty and saturation:** a reason to inspect an ecosystem's gaps and crowding.

Stages are intentionally modest: `build-now`, `probe-this-week`, `content-first`, and `archive`. They are working labels for research priority, not instructions to publish, spend money, contact maintainers, or make a business commitment.

## Evidence and media

The [media evidence inventory](docs/assets/README.md) and [machine-readable register](docs/evidence/media-register.yaml) separate the real terminal replay from the generated Social Preview. Existing report, JSON, configuration and outbound links remain the primary evidence; the screenshot only makes one local replay visible.

## Contribute

Recommend a signal, challenge a score, or propose a clearer build brief through the [contribution guide](CONTRIBUTING.md). Use the repository's issue templates to include public evidence and to state what a suggestion does **not** establish.

## Related public work

- [Zhichen Ma profile](https://github.com/soarsky1991)
- [Evidence-First Patent Skill](https://github.com/soarsky1991/evidence-first-patent-skill)
- [XHS Cover Committee Skill](https://github.com/soarsky1991/xhs-cover-committee-skill)
- [rebuild-editable-ppt-from-image](https://github.com/soarsky1991/rebuild-editable-ppt-from-image)

## License

[MIT](LICENSE)
