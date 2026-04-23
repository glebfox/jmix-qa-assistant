---
id: common-hotspots
title: Common Jmix regression hotspots
applies_to: all
triggers: flow-ui, entity, security, data, view, save
always: false
---
## Questions
- Which previously stable user path is most likely to be accidentally affected?
- Does the change touch one of the usual Jmix hotspots: save cycle, visibility, loading, or role behavior?

## Checklist
### Hotspot Regression
- Reopen the affected screen and confirm the new state is stable after reload.
- Check one neighboring scenario that uses the same entity or view but is not the main target of the task.
- Verify that visibility, save behavior, and loaded data stay aligned after repeated actions.

## Risks
- Regressions in Jmix frequently appear in reopen/reload cycles and in neighboring flows that share the same entity or view.
