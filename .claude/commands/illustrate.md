---
description: 为文章或一句话需求生成水彩速写风插图（或出图提示词）
---

Use the watercolor-sketch-style skill in this repository.

1. Read `SKILL.md` and `references/style-guide.md`.
2. Determine the mode:
   - If the user supplied an article → Article mode: pick 2–4 key scenes, then for each scene run `python scripts/build_prompt.py --scene "<场景中文描述>" --scene-en "<English scene description>"`.
   - If the user supplied a one-line story/request → Brief mode: assemble a single prompt the same way.
3. Generate images with an available backend (user-named tool first: GPT image2, nano banana, etc.; then the Kimi image_generation plugin with `--reference-image` pointing to the uploaded style sample). Reuse the style anchor verbatim and append the negative constraints on every image.
4. If no backend is available, output the complete detailed bilingual prompt list (anchor + scene + negative constraints per image) so the user can edit and paste it into any image tool.

User input: $ARGUMENTS
