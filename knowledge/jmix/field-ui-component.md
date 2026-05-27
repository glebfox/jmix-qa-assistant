---
id: field-ui-component
title: Flow UI field component changes
applies_to: feature, bugfix
triggers: field, field component, input, picker, datepicker, rich text editor, richtexteditor, required indicator, helper text, error message, placeholder, prefix, suffix, read-only, disabled
always: false
---
## Questions
- Which states does the field component support (required, read-only, disabled)?
- Which slot decorations does the field component support — prefix, suffix, both, or neither?
- Which other decorations does the field component expose (helper text, error message, placeholder)?

## Checklist
### Field Behavior
- Verify label-click focus behavior.
- Verify required indicator appearance in both Aura and Lumo.
- Verify field behavior and rendering in read-only and disabled states.
- Verify helper text, error message, prefix, and suffix rendering when the field is in read-only or disabled state.
- Verify prefix and suffix slot content renders correctly and stays usable across field states.

## Risks
- Field state transitions (editable → read-only → disabled) often regress because developers typically test only the default editable state.
- Field decorations (prefix, suffix, required indicator) are easy to forget because they are optional and frequently absent in the developer's test scenario.
