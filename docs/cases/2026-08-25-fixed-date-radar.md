# Case: fixed-date Agent Skill Radar run — 2026-08-25

[README](../../README.md) · [中文说明](../../README.zh-CN.md) · [Committed report](../../reports/2026-08-25.md) · [Committed data](../../data/2026-08-25.json)

## Problem

A public GitHub recommendation is difficult to review if its inputs disappear behind a changing search page. This case keeps a report and the JSON that produced it under the same fixed date, so the reader can distinguish a historical record from a fresh collection.

## Input

- [Query configuration](../../config/queries.json)
- [Collected JSON dated 2026-08-25](../../data/2026-08-25.json)
- Public repository and issue URLs recorded inside that JSON

The committed data records `generated_at` as `2026-08-25T03:16:35.456411+00:00`. This is the generation timestamp of that stored payload, not a claim about the current state of any listed repository.

## Method

The CLI collects configured searches, normalizes repositories, samples recent issues when available, scores the records, and writes a JSON payload. The report command renders a Markdown report from that payload. The implementation is visible in [the CLI](../../agent_skill_radar/cli.py), [scoring module](../../agent_skill_radar/scoring.py), and [report renderer](../../agent_skill_radar/report.py).

## Reproducible output

Render the committed data locally:

```bash
python -m pip install -e .
agent-skill-radar report \
  --input data/2026-08-25.json \
  --out /tmp/agent-skill-radar-2026-08-25.md
```

The resulting file is a replay of the committed dataset. Compare it with [the committed report](../../reports/2026-08-25.md). A live collection is deliberately a different operation because GitHub search results, repository metadata, and issue discussions change over time.

## Evidence links

- [Fixed-date report](../../reports/2026-08-25.md)
- [Fixed-date JSON](../../data/2026-08-25.json)
- [Current report alias](../../reports/latest.md)
- [Radar configuration](../../config/queries.json)

## What it does not prove

- It does not prove that any score predicts future demand, adoption, revenue, quality, or business success.
- It does not prove that a repository deserves a fork, a product, a public post, or a financial commitment.
- It does not reproduce the external GitHub state from 2026-08-25 when run today.
- It does not turn issue comments or stars into permission to contact, publish, or build.

## Three-minute try

Use the command under **Reproducible output**, then open the generated file and click one recorded source link. Check whether the report keeps the date, score, stage, and source distinction clear enough for your own research decision.
