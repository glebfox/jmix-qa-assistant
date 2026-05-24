# Regression Knowledge Base

This document defines the rules and roadmap for `knowledge/regressions/`. Read it whenever you add, edit, or rewrite a file under that folder.

## Purpose

When a task touches a functional area that has had recurring regressions, the assistant should make the QA engineer aware of the area's risk history and point at concrete past cases.

The reason regressions are not just "another knowledge module" is that they require a different artifact over time: instead of short reminder items, the long-term goal is to give back a reusable functional QA scope for the whole area.

## MVP 1 — breadcrumb format

In MVP 1, an entry in `knowledge/regressions/` is a short Markdown file that does only two things:

1. Names the functional area and the triggers that should pull this entry into a task.
2. Lists links to past tickets, pull requests, or issues that demonstrate the regression risk.

That is the entire content. Do not include structured reusable check items in MVP 1 entries — those belong in `knowledge/jmix/` modules if they are non-obvious reminders, or in [mvp2-regression-seeds.md](mvp2-regression-seeds.md) if they are early drafts of MVP 2 scope.

Minimal MVP 1 entry:

~~~md
---
id: short-stable-id
title: Human-readable title
applies_to: feature, bugfix
triggers: comma-separated terms likely to appear in task descriptions
always: false
---
## Questions
- Optional clarifying questions about whether this risky area is in scope.

## Linked Regression Issues
- Check [#1234 Short issue title](https://github.com/jmix-framework/jmix/issues/1234).
- Check [#1567 Short issue title](https://github.com/jmix-framework/jmix/issues/1567).

## Risks
- One short paragraph explaining why this area is regression-prone.
~~~

The assistant renders the breadcrumbs in a `Regression Breadcrumbs` section of the generated output (see [checklist-generation.md](checklist-generation.md)). It does not invent additional checklist items from these links.

## What does not belong in MVP 1 entries

- Concrete reusable check items. If a single check is a non-obvious reminder that applies to many tasks in this area, move it into a regular `knowledge/jmix/` module instead.
- Reconstructed full QA scope for the area. That is MVP 2 material — record it in [mvp2-regression-seeds.md](mvp2-regression-seeds.md).
- Implementation post-mortems or root-cause notes. Authors describe the *area*, not the *cause* of past bugs.

## MVP 2 — reusable functional scope

The MVP 2 goal is to turn each entry from a list of links into a reusable end-to-end QA scope for the area: the set of scenarios that should be re-run any time that area is touched.

The MVP 2 format is intentionally not designed yet. It will be decided once at least three or four areas have accumulated enough seed material in [mvp2-regression-seeds.md](mvp2-regression-seeds.md) to make the right structure obvious.

Do not start writing MVP 2 entries in `knowledge/regressions/` before the format is decided. Drop early drafts into the seeds file instead.

## Authoring workflow

When the team discovers a new regression-prone area:

1. Add a short MVP 1 breadcrumb entry under `knowledge/regressions/` with the area triggers and the relevant past tickets.
2. If reusable check items emerge from analysis, add them to the appropriate `knowledge/jmix/` module, not to the regression entry.
3. If a draft of the full QA scope emerges, append it to [mvp2-regression-seeds.md](mvp2-regression-seeds.md) under a clear heading.
