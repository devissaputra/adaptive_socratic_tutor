import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from adaptive_socratic_tutor import core


class CoreTests(unittest.TestCase):
    def test_low_support_for_high_mastery_first_attempt(self):
        self.assertEqual(core.hint_level(1, 0.9), 0)

    def test_support_increases_when_learner_is_stuck(self):
        self.assertEqual(core.hint_level(5, 0.2, True), 3)
        self.assertIn("sub-step", core.tutor_move("x", 5, 0.2))

    def test_requested_answer_escalates_without_exceeding_limit(self):
        self.assertEqual(core.hint_level(1, 0.6, True), 2)
        self.assertEqual(core.hint_level(5, 0.2, True), 3)

    def test_invalid_mastery_is_rejected(self):
        with self.assertRaises(ValueError):
            core.hint_level(1, 1.2)

    def test_negative_attempts_are_rejected(self):
        with self.assertRaises(ValueError):
            core.hint_level(-1, 0.5)

    def test_empty_problem_is_rejected(self):
        with self.assertRaises(ValueError):
            core.tutor_move("   ", 1, 0.5)


if __name__ == "__main__":
    unittest.main()
