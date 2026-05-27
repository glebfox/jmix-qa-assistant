# MVP 1 Scope

The MVP 1 goal of the assistant is narrow:

- Surface **reminders about non-obvious scenarios** that are almost never written explicitly in the task description, acceptance criteria, or post-implementation notes.
- For areas prone to regressions, point to **past tickets worth re-checking** (breadcrumbs to past PRs and issues).

The output is **not** a full QA coverage list. It is an assistant for both QA engineers and developers — for QA, to avoid missing easy-to-forget checks; for developers, to avoid forgetting to implement requirements that were not spelled out. It does not replace QA judgment.

## What the assistant does in MVP 1

- Reads a local Markdown knowledge base under [../knowledge/](../knowledge/).
- Asks clarifying questions needed to determine the testing scope for a specific task.
- Produces a concise checklist draft grounded strictly in selected knowledge modules. Items are dropped if they are not traceable to a module — see [../docs/checklist-generation.md](../docs/checklist-generation.md) for the full grounding rule.
- For regression-prone areas, lists breadcrumb links to past tickets without inventing additional checks. See [../docs/regressions.md](../docs/regressions.md) for the breadcrumb authoring format.

## What is out of scope for MVP 1

- Full reusable QA scope per risk area. Today, regressions are link lists; full per-area scope is deferred to MVP 2. See [roadmap.md](roadmap.md).
- MCP, external integrations, RAG, vector databases, Jira/GitHub/TestRail connectors, tool-calling workflows.
- Automatic diff reading from the main Jmix Framework repository.
- Replacing QA judgment with exhaustive test design.

## Project shape

The project is intentionally lightweight:

- [../knowledge/](../knowledge/) — the operating knowledge base (Markdown modules and regression breadcrumb entries).
- [../docs/](../docs/) — operating protocols for the assistant and authors.
- [.](.) — this directory; project specification.
- [../kb_tool.py](../kb_tool.py) — a deterministic helper CLI for validating the knowledge format and producing a basic fallback draft. See [kb-tool.md](kb-tool.md).
- [../examples/](../examples/) and [../templates/](../templates/) — task templates and examples for the file-based fallback workflow.
