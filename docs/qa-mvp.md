# `qa_mvp.py`

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
