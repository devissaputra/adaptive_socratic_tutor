# Analytic system card

## System

Adaptive Socratic Tutor

## Purpose

Inspectable Socratic tutoring baseline that selects restrained hints from attempt history and an explicit mastery estimate.

## Current maturity

Working research prototype. The bundled example checks the software path with synthetic inputs. It does not establish validity for real learners, instructors, courses, or workplaces.

## Inputs

See `../data/README.md` for the current synthetic schema and the documentation expected before real data are connected.

## Outputs

The current code produces a support level from 0 to 3 and a corresponding tutoring move. These outputs are research signals and should be interpreted with the educational context that produced them.

## Evidence needed before real use

Compare policy variants on the same tasks and learner groups. Report downstream task success, hint use, unnecessary help, and qualitative examples where the policy helped or interfered.

## Main limitation

This prototype does not estimate mastery from real learner data and it does not generate domain answers. It should be treated as a policy baseline for tutoring research, not as a deployable tutor.

## Human oversight

A person must review any output before it can affect a learner, instructor, applicant, or employee.
