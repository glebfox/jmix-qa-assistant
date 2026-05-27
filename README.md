# Jmix QA Checklist Agent Workspace

A lightweight agent workspace for the Jmix Framework QA team. A QA engineer opens this repository in an AI coding assistant, describes a task in natural language, answers clarifying questions, and receives a concise checklist draft.

The MVP 1 output is narrow on purpose: **reminders about non-obvious scenarios** that are almost never written into task descriptions, plus **breadcrumb links to past tickets** for regression-prone areas. It is an assistant for both QA engineers and developers — not a full QA coverage list and not a replacement for QA judgment.

The product is the agent-guided workflow, not the CLI. The local `kb_tool.py` script is a small deterministic helper for validating the knowledge format and generating a basic fallback draft.

## What It Is

This is not a platform and not an integration-heavy system. It is a separate repository that gives an AI assistant enough local context to help QA engineers prepare task-specific checklists.

It has six simple parts:

1. A Markdown knowledge base under [`knowledge/`](knowledge/) with Jmix-specific reminder modules and regression breadcrumb entries.
2. [`CLAUDE.md`](CLAUDE.md) (with [`AGENTS.md`](AGENTS.md) symlinked to it) as the short routing entry point for the assistant.
3. Operating protocols under [`docs/`](docs/) — how the assistant generates checklists, how authors add knowledge.
4. Project specification under [`spec/`](spec/) — what the project is, what the MVP includes, what is deferred, how the helper script works.
5. Optional task and answer templates under [`templates/`](templates/) and [`examples/`](examples/) for more structured input.
6. A small local CLI helper, [`kb_tool.py`](kb_tool.py), for validating the knowledge format and producing fallback drafts.

## Workflow Contexts

The repository serves two contexts:

- **Using the assistant** — generating a checklist for a task, or adding/editing knowledge. Read [`CLAUDE.md`](CLAUDE.md) → it routes to [`docs/`](docs/) and [`knowledge/`](knowledge/).
- **Developing the assistant** — evolving the project (scope, roadmap, helper script). Read [`CLAUDE.md`](CLAUDE.md) → it routes to [`spec/`](spec/).

## MVP Concept

### Workflow

1. QA opens this repository in an AI assistant such as Codex or Claude Code.
2. QA describes the task, acceptance criteria, and available context in chat.
3. The assistant reads `CLAUDE.md`, the checklist protocol, and the relevant files under `knowledge/`.
4. The assistant asks clarifying questions needed to determine the testing scope.
5. The assistant generates a concise checklist draft only after the scope is clear enough.
6. QA asks follow-up questions or requests edits in chat.
7. When a repeatable pattern is discovered, the assistant updates the knowledge base.

The optional script workflow is:

```bash
python3 kb_tool.py ask examples/feature-task.md
python3 kb_tool.py generate examples/feature-task.md --answers examples/feature-answers.md --out output/checklist.md
```

### What Powers It

- [`knowledge/jmix/`](knowledge/jmix/) for Jmix-specific non-obvious reminder modules.
- [`knowledge/regressions/`](knowledge/regressions/) for breadcrumb entries (links to past tickets in risk areas).

Each knowledge module contains:

- applicability triggers;
- clarifying questions;
- structured checklist items;
- risk notes.

Conditional topics should be split into narrower modules when the answer changes checklist content. For example, base UI component checks, field component behavior, extension points, and built-in UI text should not live as conditional checklist items in one broad module.

## Repository Structure

```text
.
├── README.md
├── CLAUDE.md
├── AGENTS.md                   # symlink to CLAUDE.md
├── kb_tool.py
├── spec/                       # project specification
│   ├── README.md
│   ├── scope.md
│   ├── roadmap.md
│   ├── launch-plan.md
│   ├── kb-tool.md
│   └── mvp2-regression-seeds.md
├── docs/                       # operating protocols
│   ├── checklist-generation.md
│   ├── knowledge-base.md
│   └── regressions.md
├── knowledge/
│   ├── jmix/
│   └── regressions/
├── templates/
│   ├── task.md
│   └── answers.md
└── examples/
    ├── feature-task.md
    └── feature-answers.md
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
- It keeps gated checks in focused modules instead of asking QA to filter conditional checklist items manually.

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
- regression breadcrumbs (links to past tickets) when relevant;
- focus areas and risks.
- concise, task-specific checks instead of generic QA training.
- length determined by what knowledge modules justify, not by a quota; zero items is a valid result.
- an editable draft that highlights non-obvious risks without replacing QA judgment.

## Simple Script Usage

```bash
python3 kb_tool.py ask examples/feature-task.md
python3 kb_tool.py generate examples/feature-task.md --answers examples/feature-answers.md --out output/checklist.md
```

## Pilot Plan

See [spec/launch-plan.md](spec/launch-plan.md) for the first pilot rollout.

## Roadmap

See [spec/roadmap.md](spec/roadmap.md) for work deferred to MVP 2 and beyond, including the development plan for the regression knowledge base in [docs/regressions.md](docs/regressions.md).

## MVP Limitations

- The checklist does not replace QA analysis.
- Output quality depends on input quality.
- The MVP covers only the most common and repeatable task types.
- Without an LLM, the logic remains heuristic, so some wording will stay generic.
- Some questions will still depend on team knowledge and domain context.
