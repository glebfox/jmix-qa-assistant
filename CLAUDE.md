# Agent Instructions

This repository helps the Jmix Framework QA team prepare task-specific QA checklists with the help of an AI assistant.

The MVP 1 goal of the generated checklist is narrow:

- Surface **reminders about non-obvious scenarios** that are almost never written explicitly in the task description, acceptance criteria, or post-implementation notes.
- For areas prone to regressions, point to **past tickets worth re-checking** (breadcrumbs).

The output is **not** a full QA coverage list. It is an assistant for both QA engineers and developers — for QA, to avoid missing easy-to-forget checks; for developers, to avoid forgetting to implement requirements that were not spelled out. It does not replace QA judgment.

The main user-facing workflow is agent-first: a QA engineer describes a task in chat, the assistant reads the local knowledge base, asks clarifying questions to determine the testing scope, and only then produces a concise checklist draft. The local script `qa_mvp.py` is only a deterministic helper for validating the file format and producing a basic fallback draft.

## Global Rules

- Keep all repository content in English.
- Write documentation, knowledge modules, examples, prompts, generated templates, and user-facing CLI strings in English.
- Do not add non-English content to repository files.
- Stay strictly inside the knowledge base. Every generated checklist item must trace to a specific selected `knowledge/` module. Do not generate items from general Jmix experience, industry QA practice, assumptions, or extrapolation. If an important area is missing, report it as a knowledge gap — never invent coverage to fill the gap. See `docs/checklist-generation.md` for the full rule.
- Treat `knowledge/regressions/` in MVP 1 as a breadcrumb list only — links to past tickets/PRs in risky areas. Full reusable functional scope for risk areas is MVP 2; see `docs/regressions.md` and `docs/roadmap.md`.
- Keep the solution lightweight and practical.
- Do not add MCP, external integrations, RAG, vector databases, Jira/GitHub/TestRail connectors, or tool-calling workflows for version one.
- Do not assume access to the main Jmix Framework repository.
- Prefer simple Markdown files over infrastructure.

## Workflow Routing

Read only the protocol that matches the user's request:

- Checklist generation: read `docs/checklist-generation.md`.
- Knowledge base improvements: read `docs/knowledge-base.md`. When the request touches `knowledge/regressions/`, also read `docs/regressions.md`.
- Changes to `qa_mvp.py`: read `docs/qa-mvp.md`.
- Planning future work or MVP scope discussions: read `docs/roadmap.md`.

## Critical Checklist Protocol

Every checklist-generation request uses this flow:

1. The user gives initial information about what needs testing.
2. The assistant inspects relevant `knowledge/` modules and asks clarifying questions needed to determine the testing scope.
3. The assistant generates the checklist only after the testing scope is clear enough.

If any unanswered question can change selected modules, checklist sections, checklist items, concrete object wording, or whether an area is a knowledge gap, ask questions only. Do not generate a partial checklist and do not move scope-changing questions into `Open Questions`.

Before emitting any checklist item, the assistant must internally name the `knowledge/` module path that justifies it. If no such path exists, the item is dropped — not softened, not generalized, not kept "for completeness".

A valid output of step 3 can be "no checklist items, only clarifying questions" — sometimes the questions themselves are the main value. Do not invent items to make the output look fuller.

`Open Questions` in a final checklist are only for non-blocking uncertainties that do not change the selected testing scope.
