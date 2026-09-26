# Calculation guide

## Question and evidence

How much help should a transparent tutoring policy offer?

Supplied mastery and attempt counts; small synthetic examples.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Apply explicit thresholds to choose monitoring, a question, a concept hint, or a worked sub-step.

## Calculation and interpretation

`Hint level ∈ {0,1,2,3}; lower mastery or more attempts can increase support.`

Mastery is an input, not inferred by this tutor. Thresholds are authored policy choices. Returning a template does not establish correctness, learning benefit, or a conversational language model.

## Evidence table

Worked example — illustrative, not a measured research result. Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| hint level (2 attempts, mastery .5) | 2 | unitless | `outputs.hint level (2 attempts, mastery .5)` |
| hint level (0 attempts, mastery .9) | 0 | unitless | `outputs.hint level (0 attempts, mastery .9)` |

Source: [results/review_examples.json](results/review_examples.json). Values resolve directly from this file when figures are regenerated.

This compact tutoring policy selects a level of support from supplied mastery and attempt counts. Its rules escalate from a focused question to a worked sub-step while keeping the full answer outside the main response policy. The synthetic examples make the decision boundaries easy to inspect, but the package neither estimates mastery nor demonstrates improved learning.

## Verification performed in this review

6 existing unittest checks passed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

For the explicitly illustrative example:

```bash
python scripts/review_examples.py
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`hint_level`](src/adaptive_socratic_tutor/core.py#L12) | Return 0 to 3, from monitoring to a worked sub-step. |
| [`tutor_move`](src/adaptive_socratic_tutor/core.py#L28) | Select a restrained tutoring move without revealing a full answer. |

## What remains before a stronger research claim

Mastery is an input, not inferred by this tutor. Thresholds are authored policy choices. Returning a template does not establish correctness, learning benefit, or a conversational language model. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
