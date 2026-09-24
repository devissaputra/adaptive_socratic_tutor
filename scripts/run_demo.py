import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from adaptive_socratic_tutor.core import hint_level, tutor_move

attempts, mastery = 3, 0.4
print(f"Hint level: {hint_level(attempts, mastery)}")
print(f"Tutor move: {tutor_move('Solve x+3=7', attempts, mastery)}")
