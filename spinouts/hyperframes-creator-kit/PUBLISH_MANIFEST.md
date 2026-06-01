# Publish Manifest

Date: 2026-06-01

Published location:

- Public repository: https://github.com/soarsky1991/skill-radar
- Directory: https://github.com/soarsky1991/skill-radar/tree/main/spinouts/hyperframes-creator-kit

Published files:

- `README.md` - overview, positioning, committee, first-week plan.
- `START_HERE.zh-CN.md` - 10-minute first-run learning path.
- `SKILL.md` - reusable HyperFrames creator workflow skill.
- `skills/hyperframes-creator-kit/SKILL.md` - install-friendly mirrored skill path.
- `lessons/lesson-01-proof-driven-30s-video/README.md` - first proof-driven lesson.
- `CONTRIBUTING.md` - contribution rules and small first contribution ideas.
- `ROADMAP.md` - 8-week MVP and 16-week standalone growth path.
- `GROWTH_PLAYBOOK.zh-CN.md` - high-star tutorial repo growth patterns and launch strategy.
- `research/github-tutorial-repo-patterns-2026-06-01.md` - high-star tutorial repo research and committee design.
- `templates/tutorial-repo-blueprint.md` - standalone repo README and launch blueprint.
- `templates/publishing-pack.md` - video publishing pack template.

Initial GitHub commits:

- `3409b0701b17d8d7ae941291ec5c4fc695d871fa` - Add HyperFrames creator kit overview.
- `89d461615afe30cc7682811eb542905860680e32` - Add HyperFrames creator kit skill.
- `b97bc320cdfbc74dc4c4a248dac002e713f19ab3` - Add HyperFrames tutorial repo research notes.
- `4216ec22a33ac4e4347e7d3f740700618ececaa7` - Add HyperFrames tutorial repo blueprint.
- `8e9fcea7d593a3a25d3d5348717a9d9c08b5de99` - Add HyperFrames creator kit publish manifest.

Validation:

- Pulled `soarsky1991/skill-radar` after publication.
- Confirmed local artifact folder and pulled GitHub folder have no file diffs.
- Ran `git diff --check` over the published HyperFrames commit range with no whitespace errors.
- Confirmed the public GitHub directory is reachable in browser.

Limitation:

- The GitHub connector available in this session can write to existing repositories, but did not expose a create-new-repository action. This first public version was therefore published as a spinout directory inside the existing public `skill-radar` repo. The standalone repo name recommendation remains `hyperframes-creator-kit`.

2026-06-01 expansion:

- Added a tutorial-repo skeleton on top of the first spinout: Start Here, Lesson 01, Contributing, Roadmap, Growth Playbook, Publishing Pack, and install-friendly skill path.
- Standalone repository creation is still blocked on GitHub CLI login or a connector action that can create repositories.
