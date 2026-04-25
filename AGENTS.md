# Agent Instructions

This repository exists to help the Jmix Framework QA team generate better task-specific QA checklists through conversation with an AI assistant.

The main user-facing workflow is agent-first: a QA engineer describes a task in chat, the assistant reads the local knowledge base, asks clarifying questions when needed, and produces a concise checklist draft. The local script `qa_mvp.py` is only a deterministic helper for validating the file format and producing a basic fallback draft.

## Language

- Keep all repository content in English.
- Write documentation, knowledge modules, examples, prompts, generated templates, and user-facing CLI strings in English.
- Do not add non-English content to repository files.

## MVP Boundaries

- Focus on generating QA checklists from task descriptions.
- Keep the solution lightweight and practical.
- Do not add MCP, external integrations, RAG, vector databases, Jira/GitHub/TestRail connectors, or tool-calling workflows for version one.
- Do not assume access to the main Jmix Framework repository.
- Prefer simple Markdown files over infrastructure.

## Expected Agent Workflow

When the user asks for a checklist:

1. Read the task description, acceptance criteria, and available context.
2. Inspect relevant files under `knowledge/`.
3. Select only knowledge modules that are relevant to the task.
4. Ask clarifying questions if the scope is ambiguous or important risk areas are missing.
5. Generate a QA checklist draft after enough context is available.
6. Keep the checklist editable by a QA engineer.

When the user asks to improve the knowledge base:

1. Understand whether the new knowledge is a repeatable pattern, Jmix-specific scenario, risk area, or recurring regression.
2. Update an existing module before creating a new one when the topic already belongs there.
3. Add a new module only when the knowledge has a clear reusable scope.
4. Keep modules small and practical.
5. Do not add knowledge that does not improve future checklist generation.

## Checklist Style

Generated checklists must be concise, task-specific, and action-oriented.

- When returning a checklist in chat, output the checklist as raw Markdown inside a fenced `markdown` code block so the QA engineer can copy the source markup into a ticket with interactive GitHub checkboxes.
- When writing a checklist to a file or stdout, write plain Markdown without wrapping it in an extra code fence.
- Prefer concrete checks over educational explanations.
- Avoid teaching QA how to test in general.
- Avoid generic items unless they are clearly relevant to the task.
- Avoid long lists by default.
- Aim for 8-15 checklist items for a normal task unless the task is explicitly broad.
- Use direct checklist wording such as "Verify that...", "Check that...", "Confirm that...".
- Each item should be testable by a QA engineer.
- Treat generated checklists as editable drafts: highlight non-obvious risks and likely regressions, but do not try to replace QA judgment with exhaustive test design.
- If an item is only a reminder or risk note, put it under a separate "Focus Areas" section.
- Do not include internal reasoning in the final checklist.

Recommended output sections:

```md
# QA Checklist

## Scope
- ...

## Open Questions
- ...

## Checks
### Main Flow
- [ ] ...

### Regression
- [ ] ...

## Focus Areas
- ...
```

## Knowledge Module Format

Use Markdown files with lightweight front matter:

```md
---
id: short-stable-id
title: Human-readable title
applies_to: feature, bugfix
triggers: trigger one, trigger two
always: false
---
## Questions
- ...

## Checklist
### Section Name
- ...

## Risks
- ...
```

Guidelines:

- `id` must be stable and lowercase with hyphens.
- `triggers` should contain terms that are likely to appear in task descriptions.
- `Questions` should help narrow the testing scope.
- `Checklist` should contain reusable checks, not project documentation.
- `Risks` should explain why this area deserves attention.

## Jmix-Specific Focus Areas

Prefer knowledge that helps with repeatable Jmix QA risks, including:

- Flow UI views, actions, dialogs, navigation, and component state.
- Security roles, policies, action visibility, and enforcement.
- Entity persistence, save cycles, reload behavior, optimistic locking, audit fields, and soft delete.
- Data loading, filters, fetch plans, pagination, sorting, and related entities.
- Configuration, add-ons, framework regressions, and compatibility behavior.

## `qa_mvp.py`

`qa_mvp.py` is intentionally simple.

It:

- parses a task Markdown file;
- loads Markdown knowledge modules;
- selects modules by `applies_to`, `triggers`, and `always`;
- merges module questions, checklist items, and risks;
- writes a Markdown draft.

It does not:

- call an LLM;
- reason deeply about the task;
- replace the agent workflow;
- replace QA judgment.

Use it as a smoke test for the knowledge format and as a fallback draft generator. The preferred experience is still an agent reading the same files and producing a more focused checklist.
