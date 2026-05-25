# Scoring Reference

Agent Skill Radar scores project opportunities from public GitHub metadata and a small issue sample.

## Dimensions

| Dimension | Meaning | Why it matters |
|---|---|---|
| Heat | Stars and forks | Existing audience and social proof |
| Freshness | Recent pushes | The ecosystem is alive |
| Velocity proxy | Stars per day since creation | Fast adoption, even without historical star data |
| Issue demand | Comments, reactions, demand keywords | Users are asking for something |
| Extensibility | Skill, MCP, CLI, plugin, prompt, template signals | A small companion project can exist |
| Creator fit | Docs, content, markdown, publishing, design signals | Easier to distribute through tutorials and demos |
| Novelty | Young enough to have gaps | Less likely to be fully captured |
| Saturation penalty | Very large or old ecosystems | Harder for a small project to stand out |

## Decision Thresholds

- 80+: build a proof of concept now.
- 65-79: validate this week.
- 45-64: make content first and watch responses.
- <45: archive.

## Manual Override

Override upward when:

- Multiple repos show the same issue.
- Users share scripts or multi-step workarounds.
- Maintainers explicitly say the feature is out of scope.
- The idea has a clear demo GIF.

Override downward when:

- The repo is mostly hype with few real users.
- The idea requires deep upstream changes.
- There is no credible distribution channel.
- The problem is a bug, not a durable workflow.

