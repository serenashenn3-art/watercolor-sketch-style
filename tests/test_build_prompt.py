#!/usr/bin/env python3
"""build_prompt.py 的单元测试（stdlib unittest，无第三方依赖）。

运行方式（仓库根目录）：
    python tests/test_build_prompt.py
"""
import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "build_prompt.py"

spec = importlib.util.spec_from_file_location("build_prompt", SCRIPT)
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

SCENE_CN = "深夜办公室里，两名交易员隔着堆满报表的桌子争论"
SCENE_EN = "Two traders arguing across a desk stacked with paper reports"


class AnchorTest(unittest.TestCase):
    """锚定段内容完整性约束。"""

    def test_en_anchor_core_phrases(self):
        for phrase in ("ink", "watercolor", "Pastel palette", "{ratio}"):
            self.assertIn(phrase, bp.EN_ANCHOR)

    def test_cn_anchor_core_phrases(self):
        for phrase in ("水彩", "速写", "{ratio}"):
            self.assertIn(phrase, bp.CN_ANCHOR)

    def test_no_real_artist_names(self):
        # 真实画师姓名会触发出图工具版权审核，锚定段必须保持通用描述
        joined = (bp.EN_ANCHOR + bp.CN_ANCHOR).lower()
        self.assertNotIn("behringer", joined)

    def test_negative_constraints_present(self):
        for phrase in ("no photorealism", "no 3D render", "no anime"):
            self.assertIn(phrase, bp.NEGATIVE)


class CliTest(unittest.TestCase):
    """CLI 端到端输出约束。"""

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, check=True,
        ).stdout

    def test_full_output_with_translation(self):
        out = self.run_cli("--scene", SCENE_CN, "--scene-en", SCENE_EN)
        self.assertIn("EN PROMPT", out)
        self.assertIn("CN PROMPT", out)
        self.assertIn("NEGATIVE", out)
        self.assertIn("Scene: " + SCENE_EN, out)
        self.assertIn("场景：" + SCENE_CN, out)
        self.assertIn("16:9", out)
        self.assertNotIn("未提供 --scene-en", out)

    def test_ratio_override(self):
        out = self.run_cli("--scene", SCENE_CN, "--scene-en", SCENE_EN, "--ratio", "3:2")
        self.assertIn("3:2", out)
        self.assertNotIn("16:9 composition", out)

    def test_missing_translation_warns(self):
        out = self.run_cli("--scene", SCENE_CN)
        self.assertIn("未提供 --scene-en", out)

    def test_scene_required(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], capture_output=True, text=True
        )
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
