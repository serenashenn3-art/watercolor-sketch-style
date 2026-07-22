#!/usr/bin/env python3
"""组装水彩速写风新闻纪实插画提示词（中英双语），题材不限。

用法:
    python build_prompt.py --scene "深夜办公室里，两名交易员隔着堆满报表的桌子争论"
    python build_prompt.py --scene "..." --scene-en "Two traders arguing across a desk..."
    python build_prompt.py --scene "..." --ratio "3:2"

--scene     场景中文描述（必填）：谁、在哪、做什么、什么情绪
--scene-en  场景英文描述（可选，缺省时英文提示词内嵌中文原文并提示补译）
--ratio     画幅，默认 16:9
"""
import argparse

EN_ANCHOR = (
    "Reportage sketch illustration, traditional news sketch artist's hand-drawn ink "
    "and watercolor on paper. "
    "Loose black ink pen outlines with visible hand-drawn sketchy strokes, contour lines "
    "not fully closed, occasional searching repeat lines. Transparent watercolor washes "
    "layered over the ink, thin color layers with visible paper texture and soft bleeding "
    "edges. Pastel palette: pale yellow, dusty pink, lavender purple, sky blue, warm wood "
    "brown, rosy skin tones. Background rendered as a soft monochrome watercolor wash with "
    "generous white space. Figures slightly exaggerated in a lively reportage manner, "
    "expressive faces and captured gestures, on-the-spot documentary journalism feel. "
    "Handwritten-style scene annotations, but no readable artist signature and no dates "
    "or timestamps anywhere in the image. "
    "Horizontal {ratio} composition, observer's viewpoint."
)

CN_ANCHOR = (
    "新闻速写水彩插画，传统新闻速写画师的纸本钢笔水彩手绘。黑色墨水钢笔松动勾线，速写笔触明显，"
    "轮廓线不完全闭合，偶有试探性重复线。墨线上罩透明水彩薄涂，色层轻薄可见纸纹，"
    "边缘自然洇开。粉彩色板：淡黄、灰粉、薰衣草紫、天蓝、暖木棕、玫瑰肤色。背景为"
    "单色水彩大面积晕染并大量留白。人物略带速写式夸张，表情生动、动作有抓拍感，"
    "现场新闻纪实气质。画面可有手写体场景标注，但不出现任何画师签名、日期或时间。"
    "横版 {ratio}，旁观者视角。"
)

NEGATIVE = (
    "no photorealism, no photography, no 3D render, no CGI, no digital smooth gradients, "
    "no anime or manga style, no oil painting, no thick impasto, no neon colors, "
    "no sharp vector lines, no flat cartoon fill, "
    "no artist signature, no readable signature, no dates, no timestamps, no watermark"
)


def main() -> None:
    ap = argparse.ArgumentParser(description="组装水彩速写风新闻纪实插画提示词")
    ap.add_argument("--scene", required=True, help="场景中文描述")
    ap.add_argument("--scene-en", default=None, help="场景英文描述")
    ap.add_argument("--ratio", default="16:9", help="画幅比例，默认 16:9")
    args = ap.parse_args()

    scene_en = args.scene_en or args.scene
    warn = "" if args.scene_en else (
        "\n[提示] 未提供 --scene-en，英文提示词的场景段为中文原文；"
        "用于英文出图工具前请先补译。\n"
    )

    en_prompt = EN_ANCHOR.format(ratio=args.ratio) + f"\nScene: {scene_en}"
    cn_prompt = CN_ANCHOR.format(ratio=args.ratio) + f"\n场景：{args.scene}"

    print("=" * 60)
    print("【英文提示词 · EN PROMPT】")
    print("=" * 60)
    print(en_prompt)
    print()
    print("【负面约束 · NEGATIVE】")
    print(NEGATIVE)
    print()
    print("=" * 60)
    print("【中文提示词 · CN PROMPT】")
    print("=" * 60)
    print(cn_prompt)
    print()
    print("【负面约束 · 中文工具同样适用】")
    print("不要照片写实、不要摄影感、不要 3D 渲染、不要数码平滑渐变、"
          "不要动漫风、不要厚涂油画、不要霓虹色、不要矢量锐线、不要平涂卡通、"
          "不要画师签名、不要日期时间、不要水印")
    print(warn)


if __name__ == "__main__":
    main()
