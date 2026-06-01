---
name: hyperframes-creator-kit
description: Build proof-driven HyperFrames tutorial videos and open-source learning repos with real screen evidence, agent-run production gates, publishing packs, and GitHub tutorial-repo structure.
---

# HyperFrames Creator Kit

Use this skill when the task is to turn a technical workflow into a teachable HyperFrames video or an open-source tutorial repo.

The goal is not "make a pretty AI video." The goal is a lesson someone can trust, reproduce, bookmark, and share.

## Required Inputs

Collect or infer:

- Target learner: beginner, working developer, creator, operator, or agent builder.
- Promise: one concrete result the learner gets.
- Proof assets: screen recording, screenshot, terminal output, rendered video, repo diff, or dataset.
- Output format: GitHub lesson, short video, Bilibili/X/Xiaohongshu package, or all of them.
- Risk boundaries: secrets, accounts, paid APIs, private clips, copyright, platform claims.

If proof assets are missing, mark the work `needs_proof_asset` and build a capture plan before making the final lesson.

## Committee Flow

Run the smallest useful set of committees:

1. Repo Positioning Committee
   - Choose a searchable name and one-line promise.
   - The first README screen must answer: who is this for, what can they build, how fast can they try it?

2. Tutorial Design Committee
   - Convert the workflow into steps, checkpoints, and a final artifact.
   - Prefer "build X from scratch" or "fix a real failure" over abstract feature tours.

3. Proof Director
   - Require visible evidence for each teaching claim.
   - Record terminal/browser moments, before/after output, and failure/fix points.

4. HyperFrames Engineer
   - Compose with deterministic HTML, timed clips, subtitles, motion cards, and audio.
   - After editing `.html` compositions, run the project check command before calling it complete.

5. Growth Analyst
   - Compare against high-star tutorial patterns: roadmap, build-your-own, primer, university, for-beginners, project-based.
   - Make the repo saveable: tables, indexes, lesson map, progress checklist, examples, contribution path.

6. OSS Maintainer
   - Confirm license, contribution notes, issue prompts, and small first contributions.
   - Keep the first version narrow enough for strangers to understand and improve.

7. Integrity Reviewer
   - Remove unverifiable claims, hidden sponsorship wording, unsafe account details, and unlicensed assets.
   - Label AI-generated visuals when the target platform or audience needs that context.

## HyperFrames Rules

- Every visible timed element in a composition needs `class="clip"`.
- Timed elements need `data-start`, `data-duration`, and `data-track-index`.
- GSAP timelines must be paused and registered on `window.__timelines`.
- Use muted video plus a separate audio element when audio needs timeline control.
- Keep logic deterministic: no current time, random values, or network fetches during render.
- Run the local HyperFrames check after editing composition HTML.

## Tutorial Repo Rules

The repo must include:

- A README with a clear promise, quick start, demo/output, lesson map, and contribution path.
- At least one complete runnable lesson or verifiable workflow.
- A license.
- A small issue/contribution surface.
- Evidence links or screenshots for any impressive claim.

Avoid:

- Huge "awesome list" scope on day one.
- Placeholder videos that do not teach an operation.
- Claims like "production ready" without a passing check or example.
- Burying the quick start below theory.

## Output Contract

For a new lesson or repo, produce:

- `README.md` or README section.
- Lesson plan with steps, checks, proof assets, and final artifact.
- HyperFrames composition or capture plan.
- Publishing pack: title, cover direction, SRT/subtitle needs, platform notes, risk review.
- Committee score: `ready`, `needs_proof_asset`, `needs_check`, `needs_rewrite`, or `draft_only`.

Read `research/github-tutorial-repo-patterns-2026-06-01.md` when deciding why a GitHub tutorial repo might spread.

Read `templates/tutorial-repo-blueprint.md` when creating the public README or repo structure.
