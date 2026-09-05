# Contributing to Agent Skill Radar

[README](README.md) · [简体中文](README.zh-CN.md) · [Fixed-date case](docs/cases/2026-08-25-fixed-date-radar.md) · [Signal-to-brief case](docs/cases/signal-to-build-brief.md)

Agent Skill Radar is useful only when a reader can inspect why a signal was recorded and what it does not prove. Contributions should improve that evidence trail.

## Good contributions

- a public repository, issue, discussion, release, or documentation source that belongs in the radar;
- a search query that reduces noise or finds a clear agent-native workflow;
- a correction to a score, stage, evidence link, or build-brief interpretation;
- a small test, fixture, or documentation improvement that makes rendering or provenance easier to check.

## Before opening an issue

Use one of the issue templates:

- **Recommend a signal** for a new public source or query;
- **Improve a build brief** for a dated report, score, stage, or conclusion that needs evidence-based correction.

Include a public URL, the observed fact, why it matters, and what the evidence does **not** establish. Do not submit personal data, private URLs, credentials, customer material, unlicensed screenshots, or a marketing claim presented as research.

## Local checks

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python3 -m compileall agent_skill_radar
agent-skill-radar report \
  --input data/2026-08-25.json \
  --out /tmp/agent-skill-radar-check.md
```

For a documentation-only change, verify the changed local Markdown links and make sure the text preserves the distinction between a recorded signal and an unproven outcome.

## Scope boundary

This repository records public research material. It does not automate outreach, public posting, purchases, data collection behind authentication, upstream contributions, or business decisions. Those actions require their own review and authorisation.
