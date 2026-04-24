# Launch Plan

## Goal

Validate that an agent-guided QA checklist workflow helps the Jmix QA team prepare task-specific checks faster and miss fewer important scenarios.

## Pilot Scope

- QA opens this repository in an AI assistant such as Codex.
- QA describes a real task in chat using the task description, acceptance criteria, and any available context.
- The assistant reads `AGENTS.md` and relevant files under `knowledge/`.
- The assistant asks clarifying questions when the testing scope is unclear.
- The assistant generates a concise checklist draft.
- QA reviews the result and asks for corrections in chat.
- When the assistant misses a repeatable pattern, QA asks it to update the knowledge base.

## Included In The First Wave

- Feature tasks with `Flow UI` changes.
- Bugfix tasks in `Flow UI`, security, and persistence.
- Tasks with clear acceptance criteria and recurring risk patterns.
- Tasks where QA can compare the generated checklist with an existing or expected manual checklist.

## Intentionally Out Of Scope

- Very large architectural changes.
- Tasks without a clear description or acceptance criteria.
- Rare edge-case areas where the team does not yet have stable QA patterns.
- Automatic inference of the full change set.
- Integrations with Jira, GitHub, TestRail, or the main Jmix Framework repository.

## Rollout

1. Select 5-10 recent real QA tasks.
2. Open this repository in the chosen AI assistant.
3. For each task, provide the task description and acceptance criteria in chat.
4. Answer the assistant's clarifying questions.
5. Review the generated checklist and mark:
   - useful checks;
   - noisy checks;
   - missing checks.
6. Ask the assistant to update `knowledge/` only for repeatable patterns.
7. Keep a short pilot log with task type, usefulness, noise, and missing scenarios.

## Evaluation Criteria

### Usefulness

- QA can use the checklist as a real starting point.
- The checklist surfaces scenarios that could otherwise be missed.
- The conversation feels faster than preparing the checklist from scratch.

### Quality

- The checklist is concise, roughly 8-15 items for a normal task.
- The checklist is specific to the task, not generic QA training.
- Clarifying questions help narrow the scope instead of creating extra work.

### Maintainability

- Knowledge updates are small and reviewable.
- The team can identify which knowledge module should be changed when output is noisy.
- New knowledge comes from real tasks, defects, and regressions.

## Decision Point

Continue after the pilot only if there is evidence that the workflow helps on real tasks:

- QA actually uses it during test preparation, not only for demos.
- The checklist regularly reminds people about 1-3 important scenarios.
- Time spent preparing a test pass goes down.
- Knowledge base updates are driven by real defects and regressions.
- The team can name concrete task categories where the workflow already helps.

If the result is mostly generic or too noisy, improve the knowledge base before adding any infrastructure.

## Do Not Build In Version One

- Jira, GitHub, or TestRail connectors.
- MCP and tool calling.
- A complex UI platform.
- RAG or vector storage.
- Automatic diff reading from the main Jmix Framework repository.
- An attempt to cover every possible Jmix task type from day one.
- Complex scoring, prioritization, or analytics.
