---
id: theme-and-direction
title: Theme and direction
applies_to: feature, bugfix
triggers: theme, themes, dark mode, light mode, color scheme, rtl, right-to-left, direction, lumo, aura, view, screen, page, component, ui component, visual component
always: false
---
## Questions
- Does the change affect anything that is rendered visually (layout, colors, theme styles, component appearance, view content)?

## Checklist
### Theme And Direction
- Verify the change in both Lumo and Aura themes.
- Verify the change in both light and dark theme variants.
- Verify the change with right-to-left direction (`dir="rtl"`).

## Risks
- Changes can look correct in the default theme while regressing in another theme, color scheme, or direction. Developers typically build in a single theme and direction and miss the others.

## References
- Vaadin right-to-left mode documentation: https://vaadin.com/docs/latest/flow/advanced/i18n-localization#supporting-right-to-left-mode
