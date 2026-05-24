# Launch Plan

## Goal

Validate that an agent-guided workflow helps the Jmix QA team and developers catch non-obvious scenarios they would routinely miss, and re-check regression-prone areas via breadcrumbs to past tickets. The goal is to prove the assistant adds real signal — not to produce full QA coverage.

## Pilot Workflow

1. QA opens this repository in an AI assistant such as Codex.
2. QA describes a real task in chat using the task description, acceptance criteria, and any available context.
3. The assistant reads `AGENTS.md`, the checklist protocol, and relevant files under `knowledge/`.
4. The assistant asks clarifying questions needed to determine the testing scope.
5. The assistant generates a concise checklist draft only after the scope is clear enough.
6. QA reviews the result and asks for corrections in chat.
7. When the assistant misses a repeatable pattern, QA asks it to update the knowledge base.

## Task Selection

Start with 5-10 recent real QA tasks.

Prefer:

- Feature tasks with `Flow UI` changes.
- Bugfix tasks in `Flow UI`, security, and persistence.
- Tasks with clear acceptance criteria and recurring risk patterns.
- Tasks where QA can compare the generated checklist with an existing or expected manual checklist.

Avoid in the first pilot:

- Very large architectural changes.
- Tasks without a clear description or acceptance criteria.
- Rare edge-case areas where the team does not yet have stable QA patterns.
- Tasks that require automatic analysis of the full change set.

## Rollout

1. Select pilot tasks.
2. Run one checklist-generation conversation per task.
3. Record useful checks, noisy checks, and missing checks.
4. Ask the assistant to update `knowledge/` only for repeatable patterns.
5. Review the updated knowledge modules before using them in the next task.
6. Keep a short pilot log with task type, usefulness, noise, and missing scenarios.

## Evaluation

Continue after the pilot only if there is evidence that the workflow helps on real tasks:

- QA can use the checklist as a real starting point.
- The checklist regularly surfaces scenarios that could otherwise be missed.
- The conversation feels faster than preparing the checklist from scratch.
- The checklist is concise, roughly 8-15 items for a normal task.
- The checklist is specific to the task, not generic QA training.
- Knowledge updates are small, reviewable, and driven by real tasks, defects, or regressions.
- The team can name concrete task categories where the workflow already helps.

If the result is mostly generic or too noisy, improve the knowledge base before adding any infrastructure.

## Version One Boundaries

See [roadmap.md](roadmap.md) for items deliberately deferred from MVP 1.
