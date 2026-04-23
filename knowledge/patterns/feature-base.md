---
id: feature-base
title: Generic feature checks
applies_to: feature
triggers: feature
always: true
---
## Questions
- What exact user outcome should prove that the feature works?
- Which roles or actors are allowed to use the new behavior?
- What existing behavior must remain unchanged after this feature?

## Checklist
### Acceptance Coverage
- Each acceptance criterion is covered by at least one explicit test step.

### Core Flow
- The main happy path works from the expected entry point to the expected result.
- The UI state after successful completion is clear and consistent.
- Cancel, close, or back navigation does not leave partial changes behind.

### Negative Scenarios
- Invalid or incomplete input is handled with a clear validation or user-facing message.
- The feature behaves predictably when the user repeats the same action.

## Risks
- New feature logic often breaks neighboring existing flows rather than the happy path itself.
