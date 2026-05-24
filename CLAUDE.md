# Agent Instructions

This repository helps the Jmix Framework QA team generate better task-specific QA checklists through conversation with an AI assistant.

The main user-facing workflow is agent-first: a QA engineer describes a task in chat, the assistant reads the local knowledge base, asks clarifying questions to determine the testing scope, and only then produces a concise checklist draft. The local script `qa_mvp.py` is only a deterministic helper for validating the file format and producing a basic fallback draft.

## Global Rules

- Keep all repository content in English.
- Write documentation, knowledge modules, examples, prompts, generated templates, and user-facing CLI strings in English.
- Do not add non-English content to repository files.
- Focus the MVP on generating QA checklists from task descriptions.
- Keep the solution lightweight and practical.
- Do not add MCP, external integrations, RAG, vector databases, Jira/GitHub/TestRail connectors, or tool-calling workflows for version one.
- Do not assume access to the main Jmix Framework repository.
- Prefer simple Markdown files over infrastructure.

## Workflow Routing

Read only the protocol that matches the user's request:

- Checklist generation: read `docs/checklist-generation.md`.
- Knowledge base improvements: read `docs/knowledge-base.md`.
- Changes to `qa_mvp.py`: read `docs/qa-mvp.md`.

## Critical Checklist Protocol

Every checklist-generation request uses this flow:

1. The user gives initial information about what needs testing.
2. The assistant inspects relevant `knowledge/` modules and asks clarifying questions needed to determine the testing scope.
3. The assistant generates the checklist only after the testing scope is clear enough.

If any unanswered question can change selected modules, checklist sections, checklist items, concrete object wording, or whether an area is a knowledge gap, ask questions only. Do not generate a partial checklist and do not move scope-changing questions into `Open Questions`.

`Open Questions` in a final checklist are only for non-blocking uncertainties that do not change the selected testing scope.
