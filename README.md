<sub>🌐 中文 · [English](README.en.md)</sub>

<div align="center">

# watercolor-sketch-style

> *给任何文章配「水彩速写风」新闻纪实插画 —— 一个跨 Agent 通用的 AI 配图技能*  
> *Watercolor reportage-sketch illustrations for any article — an agent-agnostic AI illustration skill.*

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet.svg)](#)
[![skills.sh Compatible](https://img.shields.io/badge/skills.sh-Compatible-green.svg)](#)

**丢给它一篇文章，或一句简短需求，它就能产出一整套风格统一的插图：**  
黑色墨水速写勾线 · 透明水彩薄涂 · 粉彩色板 · 现场纪实抓拍感 · 手绘场景标注  
法庭、财经、科技、文化、社会、人物报道 —— 任何有「人和瞬间」的题材都能入画。

```bash
npx skills add serenashenn3-art/watercolor-sketch-style
```

Claude Code / Codex / Kimi / Hermes —— 任何支持 Skill 目录的 AI Agent 都能用。

[安装](#安装) · [能做什么](#能做什么) · [核心机制](#核心机制) · [项目结构](#项目结构)

</div>

---

<p align="center">
  <img src="assets/example-watercolor-sketch.jpeg" width="100%" alt="风格锚定样本：新闻纪实水彩速写">
</p>

<sub>风格锚定样本：一张现场新闻速写。**风格不限于法庭场景** —— 任何题材都能套用这套视觉语言。</sub>

## 案例：一篇《Deep Listening》文章的全套配图

**下面 4 张图全部由本 skill 的工作流产出** —— 从文章中提取关键场景，逐张生成，风格严格统一（无签名、无日期）：

<p align="center">
  <img src="examples/deep-listening-fig1.png" width="100%" alt="场景一">
</p>

<sub>场景一 · 开篇人物时刻：倾听者与被倾听者的安静对坐</sub>

<p align="center">
  <img src="examples/deep-listening-fig2.png" width="100%" alt="场景二">
</p>

<sub>场景二 · 核心动作：深度倾听中的互动瞬间</sub>

<p align="center">
  <img src="examples/deep-listening-fig3.png" width="100%" alt="场景三">
</p>

<sub>场景三 · 关系与氛围：倾听建立起的连接</sub>

<p align="center">
  <img src="examples/deep-listening-fig4.png" width="100%" alt="场景四">
</p>

<sub>场景四 · 收束与升华：倾听之后的改变</sub>

每张图对应的提示词和文章段落见 [examples/deep-listening-prompts.md](examples/deep-listening-prompts.md)。

## 安装

### 方式一：skills.sh（推荐）

```bash
npx skills add serenashenn3-art/watercolor-sketch-style
```

### 方式二：手动安装

克隆或下载本仓库，把整个 `watercolor-sketch-style/` 目录复制到以下任一位置：

| Agent | 安装路径 |
|---|---|
| Claude Code / Codex / 通用 | `~/.config/agents/skills/` |
| Kimi | `~/.kimi/skills/` |
| 项目级（任何 Agent） | 项目根目录 `.agents/skills/` |

装好后直接说「帮这篇文章配水彩速写风的插图」即可触发。

## 能做什么

| 输入 | 输出 |
|---|---|
| 📄 一篇文章（上传或粘贴全文） | 通读全文 → 提取 2–4 个关键场景 → 逐张生成风格统一的插图（含每张图建议插入位置） |
| ✏️ 一句话简短需求 | 直接生成一张同风格插画 |
| 🎨 没有出图工具时 | 输出完整、可直接粘贴的中英双语提示词清单，方便你自行修改后丢给任何出图工具 |

出图后端自动适配：GPT image2 / gpt-image、nano banana（Gemini）、Kimi `image_generation` 插件、即梦、Midjourney —— 有什么用什么，一个都没有就优雅降级为提示词。

## 核心机制

**风格统一靠三条铁律：**

1. **锚定段逐字复用** —— 每次生成都带完整风格锚定段（见 [references/style-guide.md](references/style-guide.md)），绝不缩写、不凭记忆改写；
2. **参考图锁风格** —— 以 `assets/example-watercolor-sketch.jpeg` 作为参考图传入生成工具，整套图（含手写标注质感）高度统一；
3. **负面约束内置** —— `no photorealism / no 3D render / no anime / no artist signature / no dates` 每次必带：**生成图中永远不会出现画师签名、日期、时间**。

**提示词组装脚本**（无依赖，标准库即可运行）：

```bash
python scripts/build_prompt.py \
  --scene "深夜办公室里，两名交易员隔着堆满报表的桌子争论"
```

输出 = 英文主提示词 + 负面约束 + 中文提示词，可直接粘贴使用。测试：

```bash
python tests/test_build_prompt.py
```

## 项目结构

```
watercolor-sketch-style/
├── SKILL.md                        # 技能主入口（文章模式 + 简报模式 + 降级规则）
├── AGENTS.md                       # AI Agent 操作指南（Codex / Hermes 等）
├── CLAUDE.md                       # Claude Code 速查
├── .claude/commands/illustrate.md  # Claude Code 斜杠命令：/illustrate
├── references/
│   └── style-guide.md              # 风格拆解、中英锚定段、负面约束、场景转译表
├── scripts/
│   └── build_prompt.py             # 提示词组装器（双语输出，零依赖）
├── tests/
│   └── test_build_prompt.py        # 标准库测试套件
├── assets/
│   └── example-watercolor-sketch.jpeg  # 风格锚定样本（用作参考图）
└── examples/                       # 真实产出：4 张成品图 + 生成它们的提示词清单
```

## License

MIT —— 随意使用、修改、分发。
