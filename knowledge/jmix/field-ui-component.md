---
id: field-ui-component
title: Flow UI field component changes
applies_to: feature, bugfix
triggers: field, field component, input, picker, datepicker, rich text editor, richtexteditor, required indicator, helper text, error message, placeholder, prefix, suffix, read-only, disabled
always: false
---
## Questions
- Which field states and decorations are supported by the changed field component?

## Checklist
### Field Behavior
- Verify label rendering.
- Verify label-click focus behavior.
- Verify required indicator appearance in both Aura and Lumo.
- Verify helper text, error message, read-only state, disabled state, and placeholder.
- Verify prefix and suffix components.

## Risks
- Field components can look correct in the default state while label behavior, required markers, helper text, error state, read-only state, disabled state, placeholder, prefix content, or suffix content regresses.
