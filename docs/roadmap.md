# Roadmap

This document captures work that is **out of scope for MVP 1** but worth recording. It is not consulted during checklist generation. Update it when scope discussions produce decisions.

## MVP 1 — current

MVP 1 produces a narrow output:

- Reminders about non-obvious scenarios that are almost never written into task descriptions, acceptance criteria, or post-implementation notes.
- For risk areas, breadcrumb links to past tickets and pull requests worth re-checking.

The full goal, format, and rules of MVP 1 live in [CLAUDE.md](../CLAUDE.md), [docs/checklist-generation.md](checklist-generation.md), and [docs/knowledge-base.md](knowledge-base.md).

## MVP 2 — regression knowledge base

The main MVP 2 goal is to turn `knowledge/regressions/` from a link list into a reusable functional QA scope per risk area.

Today, when a task touches a risky area, the assistant can only point the QA engineer at past tickets ("see PR #1234, PR #1567"). The QA engineer still has to open each link and reconstruct what was tested.

The MVP 2 target is: when a task touches a risky area, the assistant returns the full reusable QA scope for that area — what scenarios to run end-to-end, not just hints. The verification covers the whole functionality, not only the diff of the current task.

This is a different artifact from MVP 1 reminders and requires its own format and process. See [docs/regressions.md](regressions.md) for the development plan.

Seed material for MVP 2 — content that already exists but is too detailed for MVP 1 — is collected in [docs/mvp2-regression-seeds.md](mvp2-regression-seeds.md). The seeds are not read by the assistant.

## Smaller deferred items

- Render `Regression Breadcrumbs` in `qa_mvp.py` fallback output. The script today does not surface `Linked Regression Issues` sections from `knowledge/regressions/` modules. The agent workflow handles this directly, so this is a small follow-up for the script.
- Allow `qa_mvp.py` to skip non-module Markdown files (for example, README files) under `knowledge/`. Today the loader requires front matter on every `*.md` it finds.

## Out of scope — version one and likely beyond

Do not add these without an explicit scope discussion:

- Jira, GitHub, or TestRail connectors.
- MCP and tool calling.
- A complex UI platform.
- RAG or vector storage.
- Automatic diff reading from the main Jmix Framework repository.
- An attempt to cover every possible Jmix task type.
- Complex scoring, prioritization, or analytics.
