# Case: from a recorded signal to a bounded build brief

[README](../../README.md) · [Fixed-date report](../../reports/2026-08-25.md) · [Source data](../../data/2026-08-25.json)

## Problem

An AI-agent repository can be prominent without telling a builder what to test next. A useful radar should translate a documented signal into one bounded question, while preserving enough evidence to reject the idea later.

## Input

The fixed-date report records [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) at rank 1 with a score of 88.8 and the `build-now` stage. Its brief records two linked issue samples and proposes a narrow angle: a cross-agent skill index, installer, or quality benchmark. See the [fixed-date report](../../reports/2026-08-25.md) and search it for the repository name.

## Method

1. Keep the repository URL, score, stage, and issue samples together in the fixed-date report.
2. State one possible build angle rather than a product conclusion.
3. Turn the angle into a reversible question: can a small index, installer, or benchmark solve a specific compatibility problem better than existing documentation?
4. Require separate evidence before any external contact, publication, expense, or product commitment.

## Reproducible output

Render the same committed data:

```bash
python -m pip install -e .
agent-skill-radar report \
  --input data/2026-08-25.json \
  --out /tmp/agent-skill-radar-brief.md
```

Search the rendered file for `addyosmani/agent-skills`. The output contains the recorded rank, score, stage, angle, and issue links from the committed JSON. That is the reproducible build brief, not a reproduction of the upstream repository's current state.

## Evidence links

- [Recorded report](../../reports/2026-08-25.md)
- [Recorded JSON payload](../../data/2026-08-25.json)
- [Upstream repository](https://github.com/addyosmani/agent-skills)
- [Issue sample 445](https://github.com/addyosmani/agent-skills/issues/445)
- [Issue sample 432](https://github.com/addyosmani/agent-skills/issues/432)

## What it does not prove

- The recorded score does not prove an unmet market need or that a companion tool should be built.
- The issue samples do not prove demand is broad, current, paid, or attributable to a particular audience.
- The proposed angle does not prove technical feasibility, legal compatibility, maintainer approval, or user benefit.
- This repository does not automate outreach, posting, spending, or upstream contribution.

## Three-minute try

Render the committed data, read the brief, then inspect one of its upstream issue links. Write one sentence that separates the observed fact from the next hypothesis. If you cannot make that separation, the brief needs more evidence before it becomes an action.
