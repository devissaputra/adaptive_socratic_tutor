import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from adaptive_socratic_tutor import core


class CoreTests(unittest.TestCase):
    def test_support_increases_when_learner_is_stuck(self):
        self.assertEqual(core.hint_level(5, 0.2, True), 3)
        self.assertIn("sub-step", core.tutor_move("x", 5, 0.2))

    def test_invalid_mastery_is_rejected(self):
        with self.assertRaises(ValueError):
            core.hint_level(1, 1.2)


if __name__ == "__main__":
    unittest.main()
