# Jmix QA Checklist Agent Workspace

A lightweight agent workspace for the Jmix Framework QA team. A QA engineer opens this repository in an AI coding assistant, describes a task in natural language, answers clarifying questions, and receives a concise checklist draft.

The product is the agent-guided workflow, not the CLI. The local `qa_mvp.py` script is a small deterministic helper for validating the knowledge format and generating a basic fallback draft.

## What It Is

This is not a platform and not an integration-heavy system. It is a separate repository that gives an AI assistant enough local context to help QA engineers prepare task-specific checklists.

It has four simple parts:

1. A Markdown knowledge base with QA patterns, Jmix-specific scenarios, risk areas, and recurring regressions.
2. `AGENTS.md` with instructions for how the assistant should use and maintain the repository.
3. Optional task and answer templates for more structured input.
4. A small local CLI helper for validating the knowledge format and producing fallback drafts.

## MVP Concept

### Workflow

1. QA opens this repository in an AI assistant such as Codex.
2. QA describes the task, acceptance criteria, and available context in chat.
3. The assistant reads `AGENTS.md` and the relevant files under `knowledge/`.
4. The assistant asks clarifying questions when the scope is ambiguous.
5. The assistant generates a concise checklist draft.
6. QA asks follow-up questions or requests edits in chat.
7. When a repeatable pattern is discovered, the assistant updates the knowledge base.

The optional script workflow is:

```bash
python3 qa_mvp.py ask examples/feature-task.md
python3 qa_mvp.py generate examples/feature-task.md --answers examples/feature-answers.md --out output/checklist.md
```

### What Powers It

- `knowledge/patterns/` for generic QA patterns such as feature, bugfix, and smoke coverage.
- `knowledge/jmix/` for Jmix-specific scenarios.
- `knowledge/regressions/` for recurring hotspots and regression reminders.

Each knowledge module contains:

- applicability triggers;
- clarifying questions;
- structured checklist items;
- risk notes.

## Minimal Repository Structure

```text
.
├── README.md
├── AGENTS.md
├── qa_mvp.py
├── knowledge/
│   ├── patterns/
│   ├── jmix/
│   └── regressions/
├── templates/
│   ├── task.md
│   └── answers.md
├── examples/
│   ├── feature-task.md
│   └── feature-answers.md
└── docs/
    └── launch-plan.md
```

## Knowledge Base Format

For the MVP, Markdown with lightweight front matter is enough:

```md
---
id: flow-ui-view
title: Flow UI view changes
applies_to: feature, bugfix
triggers: flow-ui, view, detail view, list view, action
always: false
---
## Questions
- Which views are affected?

## Checklist
### Core Flow
- The view opens from the expected entry point.

## Risks
- Navigation or route parameters may break.
```

Why this format:

- QA engineers and developers can update it without generators or IDE-specific tooling.
- It is easy to review in GitHub.
- It is easy to start with 5-10 files instead of building an oversized knowledge system.

## Input Format

The preferred input format is natural language in the assistant chat. For repeatable runs or examples, the first version can also use one Markdown task file:

```md
# Task
Title: Add deactivate action to user detail view
Type: feature
Labels: flow-ui, security, entity

## Description
...

## Acceptance Criteria
- ...

## Changed Areas
- flow-ui
- security

## Known Risks
- ...

## Context
...
```

`answers.md` is optional and can be added after the first pass of clarifying questions when a file-based flow is useful.

## Output Format

The result is a plain Markdown checklist that can be used in a PR, issue, or personal QA notes.

Expected style:

- short task summary;
- applied knowledge modules;
- clarifications or open questions;
- sectioned checklist;
- focus areas and risks.
- concise, task-specific checks instead of generic QA training.
- roughly 8-15 checklist items for a normal task.

## Simple Script Usage

```bash
python3 qa_mvp.py ask examples/feature-task.md
python3 qa_mvp.py generate examples/feature-task.md --answers examples/feature-answers.md --out output/checklist.md
```

## Pilot Plan

See [docs/launch-plan.md](docs/launch-plan.md) for the first pilot rollout.

## MVP Limitations

- The checklist does not replace QA analysis.
- Output quality depends on input quality.
- The MVP covers only the most common and repeatable task types.
- Without an LLM, the logic remains heuristic, so some wording will stay generic.
- Some questions will still depend on team knowledge and domain context.
