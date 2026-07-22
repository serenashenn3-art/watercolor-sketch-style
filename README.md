# watercolor-sketch-style

**Watercolor reportage-sketch illustration skill — works with any article, any topic.**

[中文文档](README.zh-CN.md)

Feed it an article or a one-line brief, and it produces a set of unified-style **watercolor sketch** illustrations: loose black-ink pen outlines, transparent watercolor washes, a pastel palette, on-the-spot documentary feel, handwritten scene annotations — but never any artist signature or date in the output. Courtroom, business, tech, finance, society, culture, profile pieces — anything with people and a moment.

![Style sample](assets/example-watercolor-sketch.jpeg)

> Style anchor sample: a live news reportage sketch. The style is not limited to courtroom scenes.

## Features

- **Article mode** — reads any article, picks 2–4 key scenes, assembles a style-locked prompt per scene, then generates the images. All illustrations in one article share one style.
- **Brief mode** — one sentence in, one same-style illustration out.
- **Generate or degrade gracefully** — calls an available image backend (GPT image2 / gpt-image, nano banana / Gemini, Kimi `image_generation` plugin, etc.); if none is available, outputs complete, detailed bilingual prompts ready to paste into any tool.

## Repository layout

```
watercolor-sketch-style/
├── SKILL.md                        # Canonical workflow (article mode + brief mode + fallback rules)
├── AGENTS.md                       # Operating guide for AI coding agents (Codex, Hermes, …)
├── CLAUDE.md                       # Claude-specific quick guide
├── .claude/commands/illustrate.md  # Claude Code slash command: /illustrate
├── references/
│   └── style-guide.md              # Style breakdown, EN/CN anchors, negatives, scene-translation table
├── scripts/
│   └── build_prompt.py             # Prompt assembler (bilingual output, stdlib only)
├── tests/
│   └── test_build_prompt.py        # Stdlib unittest suite
├── assets/
│   └── example-watercolor-sketch.jpeg  # Style anchor sample (use as reference image)
└── examples/                       # Real outputs + the prompt sheet that produced them
```

## Quick start

Assemble one prompt:

```bash
python scripts/build_prompt.py \
  --scene "深夜办公室里，两名交易员隔着堆满报表的桌子争论" \
  --scene-en "Two traders arguing across a desk stacked with reports in a late-night office"
```

Output: English main prompt + negative constraints + Chinese prompt — paste into GPT-image, nano banana, Midjourney, 即梦, or any image tool.

Run tests:

```bash
python tests/test_build_prompt.py
```

## Install as a Kimi skill

Copy the whole `watercolor-sketch-style/` directory to one of:

- `~/.config/agents/skills/` (recommended)
- `~/.kimi/skills/`
- Project-level `.agents/skills/`

Then say "帮这篇文章配水彩速写风的插图" / "generate a watercolor-sketch style illustration" to trigger it.

## Style-consistency rules

1. Reuse the style anchor **verbatim** on every generation.
2. One batch = one palette + one aspect ratio; only the scene description changes.
3. Always append the negative constraints (`no photorealism / no 3D render / no anime …`).
4. Never put a real artist's name in the prompt — it triggers copyright moderation. Lock the style with the reference image instead.

## Verified generation settings

- 2K + 16:9 (2048×1152) works well for WeChat official-account covers.
- Passing `assets/example-watercolor-sketch.jpeg` as a reference image keeps a whole batch visually unified (handwritten annotations included).

## License

MIT
