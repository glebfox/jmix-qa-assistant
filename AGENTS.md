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
5. Generate a QA checklist draft only after enough context is available.
6. Keep the checklist editable by a QA engineer.

When the user asks to improve the knowledge base:

1. Understand whether the new knowledge is a repeatable pattern, Jmix-specific scenario, risk area, or recurring regression.
2. Update an existing module before creating a new one when the topic already belongs there.
3. Add a new module only when the knowledge has a clear reusable scope.
4. Keep modules small and practical.
5. Do not add knowledge that does not improve future checklist generation.

## Knowledge-Grounded Output

The assistant must stay knowledge-grounded for every checklist-generation request.

- Do not generate checklist items from general Jmix experience, industry QA practice, or assumptions.
- Use only:
  - facts explicitly provided by the user;
  - checklist items from selected `knowledge/` modules;
  - risks from selected `knowledge/` modules.
- If an important scenario is not covered by selected modules, report it as a knowledge gap, not as a checklist item.
- The assistant may use general expertise only to ask clarifying questions and identify missing knowledge areas.

## Checklist Source Policy

Generated checklist items must be traceable to the task input or to selected `knowledge/` modules.

The assistant must not add checklist items only because they are generally good QA practice. If the repository does not contain knowledge for an area, the assistant should ask a clarifying question or report a knowledge gap instead of inventing coverage.

## Clarification Gate

Clarifying questions are a way to change the generated result, not a way to collect nice-to-have metadata.

Ask a clarifying question only when the answer would materially change at least one of:

- selected knowledge modules;
- whether a specific checklist item from a selected module applies;
- the concrete object wording needed to make an item testable;
- whether a missing area should be reported as a knowledge gap.

Do not ask questions whose answers would only:

- provide proper names or class names when the task already gives a usable object category, such as "the new add-on screens";
- confirm checks already required by selected knowledge modules, such as themes, right-to-left mode, localization, or practical sizes;
- explore areas that have no checklist content in the current knowledge base, unless the answer changes module selection or a knowledge gap.

If the task facts are enough to select modules and produce at least one knowledge-backed check, generate the checklist and put non-blocking uncertainties under `Open Questions`.

Generate only clarifying questions when missing information blocks module selection or all available checklist items would be generic or non-testable.

Do not fill missing scope with assumptions. Return a short "Knowledge Base Result" only when no useful checklist can be generated or the user explicitly asks to proceed without answering blockers.

## Noise Control

Checklist items must be task-specific and knowledge-backed.

- Do not include a checklist item unless it is clearly relevant to the task facts or selected module triggers.
- Prefer fewer high-signal items over a complete-looking generic checklist.
- Omit module items that require conditions not present in the task.
- Do not teach QA how to test. Avoid explanatory wording, generic reminders, and broad "check common scenarios" items.
- Every checklist item should name the concrete affected object when known.
- If the exact affected object is unknown but the task gives a usable object category, use that category in checklist wording, for example "the new add-on screens".
- Ask for the affected object only when the missing object makes a checklist item non-testable or changes module selection.

## Knowledge Gaps

When the assistant sees an important repeatable area that is not covered by `knowledge/`, it must not silently include it in the checklist.

Instead, add a short section:

```md
## Knowledge Gaps
- `add-on-packaging`: no selected module covers add-on installation, starter metadata, auto-configuration, or packaging checks.
```

Suggest updating the knowledge base only after the current result is shown.

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
- `Questions` should help narrow the testing scope, but they are candidate prompts, not mandatory output.
- Filter module questions through the clarification gate before asking them.
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
