# Knowledge Base Protocol

Use this protocol when the user asks to improve the knowledge base.

## What the Knowledge Base Is For (MVP 1)

The MVP 1 knowledge base feeds the assistant only two things:

- `knowledge/jmix/` — **reminder modules** with non-obvious scenarios for a specific Jmix topic. These produce checklist items.
- `knowledge/regressions/` — **breadcrumb entries** for regression-prone areas. These produce links to past tickets, not checklist items. See [regressions.md](regressions.md) for the format and roadmap.

When in doubt about which folder a piece of knowledge belongs in: if it produces a check item, it goes in `knowledge/jmix/`; if it points the QA engineer at past cases for re-verification, it goes in `knowledge/regressions/`.

## Non-Obvious Filter for Authors

A module item belongs in the knowledge base only if it captures something **non-obvious** — a scenario that QA engineers and developers commonly miss when focused on the main task, even when they are experienced.

This filter is applied **by authors at PR review time, not by the assistant at generation time**. The assistant must not drop or add items based on its own judgment of obviousness — its only filter is whether an item is grounded in a selected module (see [checklist-generation.md](checklist-generation.md)).

Do not add module items that:

- Repeat standard QA training (for example, "verify the form submits with valid data").
- Restate the task's acceptance criteria.
- Describe generic best practice not specific to Jmix.
- Are reminders an experienced engineer would always remember without prompting.
- Teach QA how to test rather than what to test.

Do add module items that:

- Capture footguns specific to Jmix internals (lifecycle, facets, data loaders, etc.).
- Capture cross-feature interactions that are easy to forget when working on one feature.
- Capture conditions, states, or combinations that history shows are routinely missed.

If a single item is hard to classify, leave it out of the module and start a discussion. The cost of a missing item is small; the cost of a noisy item is large because it dilutes the signal of every other item.

## Updating Knowledge

1. Understand whether the new knowledge is a repeatable pattern, Jmix-specific scenario, risk area, or recurring regression.
2. Update an existing module before creating a new one when the topic already belongs there.
3. Add a new module only when the knowledge has a clear reusable scope.
4. Keep modules small and practical.
5. Do not add knowledge that does not improve future checklist generation.

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
- Filter module questions through the clarification gate in `docs/checklist-generation.md` before asking them.
- Prefer a separate module over conditional checklist sections when a topic has a clear gate, such as field component behavior, extension points, or built-in UI text.
- `Checklist` should contain reusable checks, not project documentation.
- Checklist items should be directly applicable when the module is selected. Avoid item wording that starts with conditions such as "For field components" or "If built-in text exists".
- `Risks` should explain why this area deserves attention.

## Jmix-Specific Focus Areas

Prefer knowledge that helps with repeatable Jmix QA risks, including:

- Flow UI views, actions, dialogs, navigation, and component state.
- Security roles, policies, action visibility, and enforcement.
- Entity persistence, save cycles, reload behavior, optimistic locking, audit fields, and soft delete.
- Data loading, filters, fetch plans, pagination, sorting, and related entities.
- Configuration, add-ons, framework regressions, and compatibility behavior.
