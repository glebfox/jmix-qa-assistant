---
id: flow-ui-view
title: Flow UI view changes
applies_to: feature, bugfix
triggers: flow-ui, view, detail view, list view, browse view, dialog, action, datagrid, form
always: false
---
## Questions
- Which view or views are directly affected?
- What is the expected entry point: menu, navigation, action, button, dialog, or route?
- Should the changed action be visible, enabled, or hidden under specific conditions?

## Checklist
### Navigation And Visibility
- The affected view opens from the intended entry point without broken navigation.
- The changed action or component is visible only when it should be visible.
- Labels, captions, and button states reflect the expected business state.

### User Interaction
- The updated action works with normal user interaction from open to save or close.
- Cancel or close flow keeps the screen in a consistent state.
- Refreshing or reopening the view shows the persisted state correctly.

### Validation And Errors
- Validation and user-facing messages are understandable and appear at the right moment.
- The UI does not show stale values after the action changes the entity state.

## Risks
- Navigation, route parameters, and component visibility are common regression hotspots in Flow UI changes.
