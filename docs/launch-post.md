# Launch Post Draft

I kept seeing the same problem around AI agent tools:

There are more skills, MCP servers, prompts, context tools, and agent-native CLIs every week, but it is hard to tell which gaps are real enough to build for.

So I built **Agent Skill Radar**.

It scans public GitHub signals and turns them into a daily build brief:

1. search agent-skill, MCP, prompt, context-engineering, and agent CLI repos;
2. score them by heat, freshness, issue demand, extensibility, creator fit, novelty, and saturation;
3. publish a Markdown report with concrete companion-tool angles.

The first version is intentionally small: GitHub API, transparent scoring, daily Markdown reports.

Repo: https://github.com/soarsky1991/skill-radar
Latest report: https://github.com/soarsky1991/skill-radar/blob/main/reports/latest.md

If you know a repo or ecosystem that should be tracked, open an issue and I will add it to the radar.
