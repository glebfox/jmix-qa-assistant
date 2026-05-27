# `kb_tool.py`

`kb_tool.py` is the deterministic helper CLI for the knowledge base. It is intentionally simple.

It:

- parses a task Markdown file;
- loads Markdown knowledge modules under [../knowledge/](../knowledge/);
- selects modules by `applies_to`, `triggers`, and `always`;
- merges module questions, checklist items, and risks;
- writes a Markdown draft.

It does not:

- call an LLM;
- reason deeply about the task;
- replace the agent workflow;
- replace QA judgment.

Use it as a smoke test for the knowledge format and as a fallback draft generator. The preferred experience is still an agent reading the same files and producing a more focused checklist.

## Subcommands

- `python3 kb_tool.py ask <task.md>` — render clarifying questions for the task.
- `python3 kb_tool.py generate <task.md> [--answers <answers.md>] [--out <path>]` — render a checklist draft.

## Known gaps

See [roadmap.md](roadmap.md) for the small follow-ups (rendering regression breadcrumbs, skipping non-module Markdown files under `knowledge/`).
