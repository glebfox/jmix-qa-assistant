---
id: ui-component
title: Flow UI component changes
applies_to: feature, bugfix
triggers: component, ui component, visual component
always: false
---
## Questions
- Is the changed component a field component?
- Does the component support theme variants?
- Does the component provide built-in text that requires i18n?
- Does the component expose events, listeners, handlers, or XML subscriptions?
- Does the component receive keyboard focus or support direct user interaction?

## Checklist
### Theme And Variant
- Verify the affected component in both Lumo and Aura themes.
- Check the affected component in light and dark theme variants.
- Check right-to-left mode with `dir="rtl"` for the affected component.

## Risks
- Component changes often regress only in non-default themes, RTL mode, or state combinations that are easy to skip manually.

## References
- Vaadin right-to-left mode documentation: https://vaadin.com/docs/latest/flow/advanced/i18n-localization#supporting-right-to-left-mode
