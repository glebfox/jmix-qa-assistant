---
id: flow-ui-view
title: Flow UI view changes
applies_to: feature, bugfix
triggers: flow-ui, view, detail view, list view, browse view, dialog, route, navigation, screen, page
always: false
---
## Questions
- Are there any non-standard view modes, entry points, or size constraints that should narrow the default Flow UI view checks?

## Checklist
### Layout And Size
- Check the view at different practical sizes, including a narrow layout and a large desktop layout.
- Confirm that actions, filters, forms, and dialogs remain usable without clipped labels or overlapping controls.
- Verify that the view still opens correctly from its expected entry point: menu item, route, action, or dialog.

## Risks
- View changes often regress at non-standard practical sizes (narrow layouts, large desktop) that the developer did not test.
- New views can quietly break entry-point paths if accessed through a different route than the one used during development.
