# Research protocol

## Project

Adaptive Socratic Tutor

## Questions

1. Can a tutoring policy provide useful help without revealing answers too early?
2. How should hint depth respond to attempt history and estimated mastery?
3. Which policy constraints best preserve productive struggle?

## Baseline methods

- hint depth policy
- mastery aware scaffolding
- Socratic prompt templates
- answer reveal guardrails
- policy trace review

## Evidence to collect

Start from the current transparent baseline and record every transformation needed to produce a support level from 0 to 3 and a corresponding tutoring move. Keep a clear boundary between synthetic demonstration data and any future empirical dataset.

## Validation

Compare policy variants on the same tasks and learner groups. Report downstream task success, hint use, unnecessary help, and qualitative examples where the policy helped or interfered.

## What counts as a useful result

I would next compare this policy with a fixed hint baseline and a stronger adaptive policy. The study should measure hint usefulness, unnecessary help, learner success after a hint, and whether learners still do meaningful work themselves.

## Threats to validity

Mastery estimates can be wrong, attempt counts ignore strategy quality, and a useful hint policy may vary by subject, task difficulty, and learner experience.
