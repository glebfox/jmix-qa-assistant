# Agent Instructions

This repository is a workspace for a QA assistant that helps the Jmix Framework QA team prepare task-specific checklists by reading a local Markdown knowledge base.

The repository serves two distinct contexts:

- **Using the assistant** — generating a checklist, or adding/editing knowledge. The agent reads `docs/` (operating protocols) and `knowledge/` (content).
- **Developing the assistant** — evolving the project itself: scope, roadmap, architecture, the helper script. The agent reads `spec/`.

If unsure which context applies, ask the user before reading anything else.

## Global Rules

- Keep all repository content in English. Write documentation, knowledge modules, examples, prompts, templates, and user-facing CLI strings in English.
- Do not add MCP, external integrations, RAG, vector databases, Jira/GitHub/TestRail connectors, or tool-calling workflows. The project is intentionally lightweight Markdown.
- Do not assume access to the main Jmix Framework repository.
- Prefer simple Markdown files over infrastructure.

## Workflow Routing

Read only the protocol that matches the user's request. Do not preload all docs.

**Using the assistant:**

| Request | Read |
| --- | --- |
| Generate a checklist for a task | `docs/checklist-generation.md` |
| Add or edit a knowledge module | `docs/knowledge-base.md` |
| Add or edit a regression entry | `docs/knowledge-base.md` and `docs/regressions.md` |

**Developing the assistant:**

| Request | Read |
| --- | --- |
| Project scope, what MVP includes, project shape | `spec/scope.md` (and other `spec/` files as needed) |
| Roadmap, deferred work, future versions | `spec/roadmap.md` |
| Changes to the helper script | `spec/kb-tool.md` and `kb_tool.py` |
| Pilot plan or rollout | `spec/launch-plan.md` |
