---
id: bugfix-base
title: Generic bugfix checks
applies_to: bugfix
triggers: bugfix, fix, regression
always: true
---
## Questions
- What was the exact broken behavior before the fix?
- How can we prove the original defect no longer reproduces?
- Which nearby behavior could regress because of this fix?

## Checklist
### Reproduction
- The original problem is clearly reproducible on the old scenario or data conditions.
- The fix prevents the original defect in the main reproduction path.

### Regression
- Nearby flows that use the same screen, entity, or service still work.
- Error handling and validation did not silently change in unrelated cases.

## Risks
- A bugfix may solve the reported case but keep failing on adjacent variations of the same scenario.
