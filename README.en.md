<sub>🌐 [中文](README.md) · English</sub>

<div align="center">

# watercolor-sketch-style

> *Watercolor reportage-sketch illustrations for any article — an agent-agnostic AI illustration skill.*  
> *给任何文章配「水彩速写风」新闻纪实插画 —— 一个跨 Agent 通用的 AI 配图技能。*

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet.svg)](#)
[![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-green.svg)](#)

**Feed it an article or a one-line brief, and it produces a set of unified-style illustrations:**  
loose black-ink pen outlines · transparent watercolor washes · pastel palette · on-the-spot documentary feel · handwritten scene annotations  
Courtroom, business, tech, finance, society, culture, profile pieces — anything with people and a moment.

```bash
npx skills add serenashenn3-art/watercolor-sketch-style
```

Works with Claude Code, Codex, Kimi, Hermes — any AI agent that supports a skills directory.

[Install](#install) · [What it does](#what-it-does) · [How it works](#how-it-works) · [Project layout](#project-layout)

</div>

---

<p align="center">
  <img src="assets/example-watercolor-sketch.jpeg" width="100%" alt="Style anchor sample: a live news reportage sketch">
</p>

<sub>Style anchor sample: a live news reportage sketch. **The style is not limited to courtroom scenes** — any topic can use this visual language.</sub>

## Case study: a full illustration set for one article

**All 4 images below were produced by this skill's own workflow** — key scenes extracted from the article, generated one by one, style strictly unified (no signature, no date):

<p align="center">
  <img src="examples/deep-listening-fig1.png" width="100%" alt="Scene 1">
</p>

<sub>Scene 1 · The opening character moment: a quiet, attentive exchange</sub>

<p align="center">
  <img src="examples/deep-listening-fig2.png" width="100%" alt="Scene 2">
</p>

<sub>Scene 2 · The core action: a moment inside deep listening</sub>

<p align="center">
  <img src="examples/deep-listening-fig3.png" width="100%" alt="Scene 3">
</p>

<sub>Scene 3 · Relationship and atmosphere: the connection listening builds</sub>

<p align="center">
  <img src="examples/deep-listening-fig4.png" width="100%" alt="Scene 4">
</p>

<sub>Scene 4 · Resolution: what changes after being heard</sub>

See [examples/deep-listening-prompts.md](examples/deep-listening-prompts.md) for the prompt behind each image and its matching article section.

## Install

### Option 1: skills.sh (recommended)

```bash
npx skills add serenashenn3-art/watercolor-sketch-style
```

### Option 2: manual

Clone or download this repo, then copy the whole `watercolor-sketch-style/` directory to one of:

| Agent | Install path |
|---|---|
| Claude Code / Codex / generic | `~/.config/agents/skills/` |
| Kimi | `~/.kimi/skills/` |
| Project-level (any agent) | `.agents/skills/` in your project root |

Then say *"generate watercolor-sketch style illustrations for this article"* to trigger it.

## What it does

| Input | Output |
|---|---|
| 📄 An article (upload or paste) | Reads it → picks 2–4 key scenes → generates unified-style illustrations one by one (with suggested insert positions) |
| ✏️ A one-line brief | One same-style illustration |
| 🎨 No image backend available | Complete, ready-to-paste bilingual (EN/CN) prompt sheets you can edit and feed to any image tool |

Image backends adapt automatically: GPT image2 / gpt-image, nano banana (Gemini), Kimi `image_generation` plugin, 即梦, Midjourney — uses whatever is available; if none, it degrades gracefully to prompts.

## How it works

**Three rules keep every batch visually unified:**

1. **Style anchor reused verbatim** — every generation carries the full anchor paragraph (see [references/style-guide.md](references/style-guide.md)), never abbreviated, never rewritten from memory;
2. **Reference image locks the style** — `assets/example-watercolor-sketch.jpeg` passed as a reference image keeps a whole batch unified (handwritten annotations included);
3. **Built-in negative constraints** — `no photorealism / no 3D render / no anime / no artist signature / no dates` on every run: **no artist signature, date, or timestamp ever appears in generated images**.

**Prompt assembler** (stdlib only, zero dependencies):

```bash
python scripts/build_prompt.py \
  --scene "Two traders arguing across a desk stacked with reports in a late-night office"
```

Output = English main prompt + negative constraints + Chinese prompt, ready to paste. Tests:

```bash
python tests/test_build_prompt.py
```

## Project layout

```
watercolor-sketch-style/
├── SKILL.md                        # Canonical workflow (article mode + brief mode + fallback rules)
├── AGENTS.md                       # Operating guide for AI coding agents (Codex, Hermes, …)
├── CLAUDE.md                       # Claude Code quick guide
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

## License

MIT — use, modify, and distribute freely.
