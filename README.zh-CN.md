# watercolor-sketch-style

**水彩速写风 · 公众号配图生成 Skill（题材不限）**

[English README](README.md)

输入**任何题材**的文章或一句简短需求，生成风格统一的水彩速写新闻纪实插画——黑色墨水速写勾线 + 透明水彩薄涂 + 粉彩色板 + 现场纪实抓拍感 + 手写场景标注（生成图中不出现画师签名、日期、时间）。法庭、商业、科技、财经、社会、文化、人物稿皆可配图。

![风格案例](assets/example-watercolor-sketch.jpeg)

> 风格案例：新闻现场速写（证词场景），本 skill 的风格锚定样本。风格不限于法庭场景。

## 功能

- **文章配图模式**：通读任意文章，自动选出 2–4 个关键内容场景，为每个场景生成同风格插图提示词并出图，全文插图风格统一
- **简报模式**：一句简短描述或一段故事，直接生成同风格单图
- **出图 / 降级**：环境中有图像生成工具（GPT image2、nano banana、Kimi image_generation 插件等）时直接调用出图；没有时输出完整详细的中英双语提示词，方便自行修改后粘贴到任何出图工具

## 目录结构

```
watercolor-sketch-style/
├── SKILL.md                        # skill 主文件（触发描述 + 工作流 + 实测经验）
├── AGENTS.md                       # AI 编码代理（Codex / Hermes 等）使用指南
├── CLAUDE.md                       # Claude 专用速览
├── .claude/commands/illustrate.md  # Claude Code 斜杠命令：/illustrate
├── references/
│   └── style-guide.md              # 风格拆解、中英锚定段、负面约束、场景转译表
├── scripts/
│   └── build_prompt.py             # 提示词组装脚本（中英双语输出，零依赖）
├── tests/
│   └── test_build_prompt.py        # 单元测试（stdlib unittest）
├── assets/
│   └── example-watercolor-sketch.jpeg  # 风格锚定样本（用作参考图）
└── examples/                       # 真实产出示例 + 对应提示词清单
```

## 快速使用

组装一条提示词：

```bash
python scripts/build_prompt.py \
  --scene "深夜办公室里，两名交易员隔着堆满报表的桌子争论" \
  --scene-en "Two traders arguing across a desk stacked with reports in a late-night office"
```

运行测试：

```bash
python tests/test_build_prompt.py
```

## 安装为 Kimi Skill

将整个 `watercolor-sketch-style/` 目录复制到以下任一位置：

- `~/.config/agents/skills/`（推荐）
- `~/.kimi/skills/`
- 项目级 `.agents/skills/`

之后对 Kimi 说「帮这篇文章配水彩速写风的插图」或「生成一张水彩速写风格的图」即可触发。

## 风格统一的三条铁律

1. 锚定段逐字复用，每次生成都带完整锚定段
2. 同一批插图共用同一色板与画幅，只换场景描述
3. 负面约束每次必带（no photorealism / no 3D render / no anime …）

## 实测提示

- prompt 中避免使用真实画师姓名（会触发出图工具的版权审核），用通用风格描述 + 参考图（`--reference-image`）锁定风格即可
- 2K + 16:9（2048×1152）已验证适合公众号头图

## License

MIT
