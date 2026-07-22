# CLAUDE.md — Watercolor Sketch Style Skill

This repository is a skill package: given an article or a one-line brief, produce unified-style **watercolor reportage sketch** illustrations (ink outlines + watercolor washes + pastel palette + handwritten annotations).

## Read first

1. `SKILL.md` — canonical workflow (article mode + brief mode + generation/fallback rules).
2. `references/style-guide.md` — verbatim EN/CN prompt anchors, negative constraints, scene-translation table. Do not paraphrase the anchor; copy it exactly.
3. `AGENTS.md` — backend priority, hard rules, conventions (applies to you too).

## Quick path

- Assemble a prompt: `python scripts/build_prompt.py --scene "<场景中文描述>" [--scene-en "<English scene>"] [--ratio 16:9]`
- Slash command available: `/illustrate` (see `.claude/commands/illustrate.md`).
- Run tests: `python tests/test_build_prompt.py`.

## Non-negotiables

- Anchor verbatim on every image; same palette + ratio across a batch; negative constraints always appended.
- No real artist names in prompts (copyright moderation, HTTP 403). Lock style with `assets/example-watercolor-sketch.jpeg` as a reference image instead.
- No artist signature, date, or timestamp in generated images — inspect every output.
- If no image-generation backend is available, output the full detailed bilingual prompt list for the user — never fake a generated image.
