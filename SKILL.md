---
name: agent-skill-radar
description: Use when the user wants to scan GitHub for AI agent skills, MCP servers, prompt systems, context engineering tools, or agent-native CLI opportunities; generate daily opportunity reports; choose a two-week open-source project; or turn GitHub trend research into build briefs, fake-door probes, and launch content.
---

# Agent Skill Radar

Use this skill to find project opportunities from GitHub evidence instead of brainstorming from scratch.

## Workflow

1. Run the radar CLI.
2. Read the top-scoring repos and issue samples.
3. Pick one opportunity with a narrow companion-tool shape.
4. Generate a build brief, fake-door probe, README angle, and launch post.
5. Save the report under `reports/` and keep the data under `data/`.

## Commands

Run the default daily scan:

```bash
agent-skill-radar run
```

Collect a custom scan:

```bash
agent-skill-radar collect \
  --query "agent memory coding assistant stars:>100 created:>=2025-01-01" \
  --limit-per-query 12 \
  --issue-limit 6 \
  --out data/custom.json
```

Render a report:

```bash
agent-skill-radar report --input data/custom.json --out reports/custom.md
```

## Interpretation Rules

- Treat `build-now` as a proof-of-concept signal, not permission to build a large product.
- Prefer a companion tool, plugin, skill pack, template, benchmark, or CLI wrapper over a fork.
- Avoid topics where the only signal is stars. Look for issue comments, reactions, recurring workarounds, and ecosystem gaps.
- For giant repositories, build around the ecosystem edge: docs, config, migration, compatibility, monitoring, security, or publishing workflows.
- If the same gap appears across 3 or more repos, promote it to a standalone project idea.

## Output Template

For each shortlisted idea, write:

```text
Project:
Target user:
Observed demand:
Repo evidence:
Why upstream will not solve it:
Smallest useful artifact:
Distribution wedge:
Two-week scope:
Fake-door question:
```

## Probe Template

Use a neutral validation comment. Do not pitch too early.

```text
I have seen this come up in a few agent-tooling repos. My current workaround is <specific workaround>.

I am considering a small standalone <CLI / skill / MCP server / template> that does <specific job> without requiring upstream changes.

Before building it: would this solve your case, or is the real blocker different?
```

