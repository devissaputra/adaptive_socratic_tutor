"""Reproduce the labeled worked example; this is not an empirical study."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from adaptive_socratic_tutor import core
outputs={'hint level (2 attempts, mastery .5)': core.hint_level(2,.5), 'hint level (0 attempts, mastery .9)': core.hint_level(0,.9)}
result={'kind':'illustrative_calculation','note':'Supplied policy inputs; no learner outcome.','outputs':outputs}
(ROOT/'results/review_examples.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
