---
id: smoke-regression
title: Minimal smoke and regression checks
applies_to: all
triggers: smoke, regression
always: true
---
## Questions
- Which existing flow is most likely to regress because of this change?
- Is there a minimal smoke path the QA engineer should always execute after the change?

## Checklist
### Quick Regression
- The affected screen or API still opens without framework-level errors.
- Save, refresh, reopen, or reload behavior remains stable after the change.
- Existing data that predates the change is still handled correctly.

### Environment Sanity
- The target scenario is checked on the main browser or environment used by the team.

## Risks
- Small local changes in Jmix often surface as regressions only after reload, reopen, or repeated use.
