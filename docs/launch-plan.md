# Launch Plan

## Pilot Goal

Validate that a simple QA checklist generator helps the Jmix QA team remember important scenarios and provides practical value without heavy infrastructure.

## Included In The First Wave

- Feature tasks with `Flow UI` changes.
- Bugfix tasks in `Flow UI`, security, and persistence.
- Tasks with clear acceptance criteria and recurring risk patterns.

## Intentionally Out Of Scope

- Very large architectural changes.
- Tasks without a clear description or acceptance criteria.
- Rare edge-case areas where the team does not yet have stable QA patterns.
- Any attempt to infer the whole change set automatically without human input.

## Rollout Plan

1. Prepare an initial knowledge base with 6-8 modules.
2. Select 5-10 recent real QA tasks.
3. For each task:
   - fill in `task.md`;
   - collect clarifying questions;
   - add `answers.md` when needed;
   - generate the checklist;
   - compare it with the actual manual QA checklist.
4. Record for each task:
   - which items were useful;
   - which items were noisy;
   - which important checks were still missing.
5. Update only the knowledge modules that improve repeatable output quality.

## How To Evaluate The Pilot

### Usefulness

- QA used the draft with minimal prompting.
- The draft saves time at the start of test preparation.
- It surfaces at least a few scenarios that could otherwise be missed.

### Quality

- The checklist does not explode into 80+ items without a good reason.
- There is a clear connection between the task and the included sections.
- The clarifying questions genuinely help narrow the testing scope.

### Maintainability

- New knowledge can be added with a single Markdown file.
- The team can identify which module to update when it produces noise or false positives.

## Next Step After A Successful Pilot

If the MVP proves valuable, add one LLM layer on top of the existing knowledge base:

- input: task description, answers to clarifying questions, and selected knowledge modules;
- output: a better phrased and better prioritized checklist.

Important: this is the next stage, not a prerequisite for launching version one.
