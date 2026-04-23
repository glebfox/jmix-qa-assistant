---
id: data-loading
title: Data loading and filtering
applies_to: feature, bugfix
triggers: data, loading, loader, fetch plan, relation, filter, browse view, list, hidden by default, inactive
always: false
---
## Questions
- Did the change affect how the list or screen loads data?
- Are filters, default conditions, pagination, or sorting part of the expected behavior?
- Could related entities or fetch plans change what the user sees?

## Checklist
### Default Loading Behavior
- The screen loads the expected dataset on first open.
- Default filters and visibility conditions are applied exactly as described.
- Previously existing records still appear or stay hidden according to the new rules.

### Filtering And Consistency
- Changing the filter updates the dataset correctly without stale rows.
- Returning to the screen or reloading preserves the intended default behavior.
- Sorting, pagination, or relation-backed values still behave correctly if present.

## Risks
- Changes in default filters and loaders often cause subtle regressions in browse views and lookup screens.
