# Checklist Generation Protocol

Use this protocol for every checklist-generation request.

## Two-Step Flow

### Step 1: Scope Clarification

Before generating a checklist:

1. Read the task description, acceptance criteria, and available context.
2. Inspect relevant files under `knowledge/`.
3. Select base knowledge modules that clearly match the task.
4. Identify candidate knowledge modules whose questions may expand or narrow the testing scope.
5. Classify candidate questions as blocking or non-blocking.

Ask clarifying questions when an answer may change at least one of:

- selected knowledge modules;
- checklist sections;
- checklist items;
- concrete affected object wording needed to make an item testable;
- whether a missing area should be reported as a knowledge gap.

When any blocking scope question exists, return only clarifying questions. Do not generate a partial checklist. Do not move blocking questions into `Open Questions`.

Do not ask questions whose answers would only:

- provide proper names or class names when the task already gives a usable object category, such as "the new add-on screens";
- confirm checks already required by selected knowledge modules, such as themes, right-to-left mode, localization, or practical sizes;
- collect nice-to-have metadata that would not change selected modules, checklist content, item wording, or knowledge gaps.

Use general expertise only to identify useful clarifying questions and missing knowledge areas. Do not use it to create checklist items.

### Step 2: Checklist Draft

Generate the checklist only after:

- the user has answered the scope questions; or
- no blocking scope-changing questions are needed.

If task facts are enough to select modules and produce useful knowledge-backed checks, generate the checklist. Put only non-blocking uncertainties under `Open Questions`.

Generate only clarifying questions when missing information blocks module selection, gates the checklist sections that would make the result useful, or all available checklist items would be generic or non-testable.

A valid checklist may also contain zero items if, after applying knowledge grounding, no module-traced item applies to the task. Returning a short result with the selected modules and any clarifying questions that produced real value is preferred over padding the output with invented coverage.

Do not fill missing scope with assumptions. Return a short "Knowledge Base Result" only when no useful checklist can be generated or the user explicitly asks to proceed without answering blockers.

## Knowledge-Grounded Output

The assistant must stay knowledge-grounded for every checklist-generation request.

- Do not generate checklist items from general Jmix experience, industry QA practice, or assumptions.
- Use only:
  - facts explicitly provided by the user;
  - checklist items from selected `knowledge/` modules;
  - risks from selected `knowledge/` modules.
- If an important scenario is not covered by selected modules, report it as a knowledge gap, not as a checklist item.

Generated checklist items must be traceable to the task input or to selected `knowledge/` modules.

Before emitting any checklist item, the assistant must internally name the specific selected `knowledge/` module path that justifies it. If no such path exists, the item is dropped — not softened, not generalized, not kept "for completeness". Dropping an item is always preferred over inventing one.

The assistant must not add checklist items only because they are generally good QA practice. If the repository does not contain knowledge for an area, ask a clarifying question or report a knowledge gap instead of inventing coverage.

## Clarification Gates

Clarifying questions are a way to change the generated result, not a way to collect nice-to-have metadata.

Treat a module question as a gate when the answer decides whether another knowledge module, checklist section, or checklist item applies. If a gate is unanswered, ask the question before generating the gated checklist content.

Do not include gated content by using conditional wording such as "For field components..." or "If the component exposes events...".

## Noise Control

Checklist items must be task-specific and knowledge-backed.

- Do not include a checklist item unless it is clearly relevant to the task facts or selected module triggers.
- Prefer fewer high-signal items over a complete-looking generic checklist.
- Omit module items that require conditions not present in the task.
- Do not include conditional checklist items that ask QA to decide whether the item applies. Ask the gating question first or omit the gated item.
- Do not teach QA how to test. Avoid explanatory wording, generic reminders, and broad "check common scenarios" items.
- Every checklist item should name the concrete affected object when known.
- If the exact affected object is unknown but the task gives a usable object category, use that category in checklist wording, for example "the new add-on screens".
- Ask for the affected object only when the missing object makes a checklist item non-testable or changes module selection.

## Knowledge Gaps

When the assistant sees an important repeatable area that is not covered by `knowledge/`, it must not silently include it in the checklist.

Instead, add a short section:

~~~md
## Knowledge Gaps
- `add-on-packaging`: no selected module covers add-on installation, starter metadata, auto-configuration, or packaging checks.
~~~

Suggest updating the knowledge base only after the current result is shown.

## Regression Breadcrumbs

Selected `knowledge/regressions/` modules contribute breadcrumb links to past tickets, not checklist items.

- Render breadcrumb entries in a separate `## Regression Breadcrumbs` section of the output.
- Use the link list from the module verbatim, preserving issue numbers and titles.
- Do not turn breadcrumbs into `[ ]` checkbox items.
- Do not derive additional checks from the linked tickets — the linked content is for QA to review manually.
- See [knowledge-base.md](knowledge-base.md) and [regressions.md](regressions.md) for the regression knowledge format and roadmap.

## Checklist Style

Generated checklists must be concise, task-specific, and action-oriented.

- When returning a checklist in chat, output the checklist as raw Markdown inside a fenced `markdown` code block so the QA engineer can copy the source markup into a ticket with interactive GitHub checkboxes.
- When writing a checklist to a file or stdout, write plain Markdown without wrapping it in an extra code fence.
- Prefer concrete checks over educational explanations.
- Avoid teaching QA how to test in general.
- Avoid generic items unless they are clearly relevant to the task.
- Avoid long lists by default.
- Length is determined by what selected knowledge modules justify, not by a quota. A typical output has a few to roughly fifteen items; zero items is a valid result when no module-traced item applies.
- Use direct checklist wording such as "Verify that...", "Check that...", "Confirm that...".
- Each item should be testable by a QA engineer.
- Treat generated checklists as editable drafts: highlight non-obvious risks and likely regressions, but do not try to replace QA judgment with exhaustive test design.
- If an item is only a reminder or risk note, put it under a separate "Focus Areas" section.
- Do not include internal reasoning in the final checklist.

Recommended output sections:

~~~md
# QA Checklist

## Scope
- ...

## Open Questions
- ...

## Checks
### Section From Module 1
- [ ] ...

### Section From Module 2
- [ ] ...

## Regression Breadcrumbs
- [#1234 issue title](https://github.com/jmix-framework/jmix/issues/1234)
- [#1567 issue title](https://github.com/jmix-framework/jmix/issues/1567)

## Focus Areas
- ...
~~~
