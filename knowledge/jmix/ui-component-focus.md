---
id: ui-component-focus
title: Flow UI component focus behavior
applies_to: feature, bugfix
triggers: focus, focus-ring, keyboard, tab navigation, interactive, user interaction
always: false
---
## Questions
- Which user interactions can move focus to the component?

## Checklist
### Focus And Keyboard
- Check focus-ring behavior by keyboard tab navigation in Lumo.
- Check focus-ring behavior by any focus interaction in Aura.
- Confirm that keyboard focus is visible and does not produce unexpected layout shifts.

## Risks
- Focus regressions often appear only in keyboard navigation, theme-specific focus-ring behavior, or interactive states.
