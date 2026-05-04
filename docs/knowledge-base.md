# Knowledge Base Protocol

Use this protocol when the user asks to improve the knowledge base.

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
