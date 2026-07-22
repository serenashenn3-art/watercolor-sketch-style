# AGENTS.md — Watercolor Sketch Style Skill

Guidance for AI coding agents (Codex, Claude Code, Gemini CLI, Hermes, etc.) working in or with this repository.

## What this repo is

A reusable **skill package** that turns an article (or a one-line brief) into a set of unified-style **watercolor reportage sketch** illustrations: loose black-ink pen outlines + transparent watercolor washes + pastel palette + handwritten annotations, on-the-spot journalism feel. Style anchor sample: `assets/example-watercolor-sketch.jpeg`.

## Entry points

| File | Role |
|------|------|
| `SKILL.md` | Canonical workflow (Chinese). Read this first for the operating procedure. |
| `references/style-guide.md` | Full style breakdown, verbatim prompt anchors (EN/CN), negative constraints, scene-translation table. |
| `scripts/build_prompt.py` | Deterministic prompt assembler. CLI: `--scene` (required, CN), `--scene-en` (optional EN), `--ratio` (default `16:9`). Prints EN prompt + negative constraints + CN prompt. |
| `tests/test_build_prompt.py` | Stdlib unittest suite. Run: `python tests/test_build_prompt.py` from repo root. |
| `examples/` | Real outputs (4 illustrations for a sample article) and the prompt sheet that produced them. |

## The two workflows (summary; details in SKILL.md)

1. **Article mode** — user supplies an article → read it, pick 2–4 key scenes (conflict/turning point > person in action > relationship/atmosphere > abstract idea translated into concrete people doing things) → for each scene run `scripts/build_prompt.py` → generate images one by one.
2. **Brief mode** — user supplies a one-line story/request → assemble a single prompt the same way → generate one image.

## Image generation backends

After prompts are assembled, generate images with whatever backend is available, in this priority:

1. A backend the **user explicitly named** (e.g. GPT image2 / gpt-image API, nano banana / Gemini image generation).
2. The Kimi `image_generation` plugin (`scripts/image_generation_tool.py` in that plugin): supports `--reference-image`, which is the strongest style-locking mechanism — upload `assets/example-watercolor-sketch.jpeg` via its `image-to-url` command first, then pass the public URL to every `generate` call.
3. Any other local image tool (即梦, Midjourney, etc.).

**If no backend is available**: do NOT pretend to generate. Output the complete, detailed bilingual prompt list (anchor + scene + negative constraints, one block per image) so the user can edit and paste it into any tool themselves.

## Hard rules (do not break)

1. Reuse the style anchor **verbatim** on every generation; never paraphrase or shorten it.
2. All images in one batch share the same palette and aspect ratio; only the scene description changes.
3. Always append the negative constraints: `no photorealism, no photography, no 3D render, no CGI, no digital smooth gradients, no anime or manga style, no oil painting, no thick impasto, no neon colors, no sharp vector lines, no flat cartoon fill, no artist signature, no readable signature, no dates, no timestamps, no watermark`.
4. **The generated image must not contain any artist signature, date, or timestamp.** The style sample itself carries a signature and date, and models tend to mimic them — visually inspect every output and regenerate with tightened negatives if they appear.
5. **Never put a real artist's name in the prompt** — it triggers copyright moderation (observed HTTP 403). Use the generic anchor text; style fidelity comes from the reference image, not the name.
6. After each generation, verify: ink outlines + thin watercolor + pastel palette + documentary feel, no photorealism. Regenerate with tightened negatives if it drifts.

## Conventions

- Prompts are assembled in English for generation; the Chinese prompt is for CN-native tools and human review.
- Default aspect ratio `16:9` (WeChat official-account cover); `3:2` is the supported alternative.
- Scripts are stdlib-only Python 3; no dependencies to install.
