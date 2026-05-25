# Contributing

Agent Skill Radar works best when suggestions are tied to public evidence.

Good contributions include:

- a GitHub repository that belongs in the radar;
- a query that finds better agent-native tools;
- a noisy result that should be filtered;
- a scoring signal that improves build-decision quality;
- a short issue sample that shows real developer demand.

## Suggest A Repository

Open an issue with:

```text
Repository:
Why it matters:
Demand evidence:
Suggested category:
```

Useful demand evidence can be an issue thread, discussion, release, star growth pattern, or repeated request from users.

## Local Development

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agent-skill-radar run --limit-per-query 8 --issue-limit 4
```

Before opening a pull request, run:

```bash
python3 -m compileall agent_skill_radar
```
