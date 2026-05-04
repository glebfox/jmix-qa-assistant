---
id: flow-ui-view
title: Flow UI view changes
applies_to: feature, bugfix
triggers: flow-ui, view, detail view, list view, browse view, dialog, route, navigation, screen, page, lumo, aura, theme, rtl, localization, i18n, language
always: false
---
## Questions
- Are there any non-standard view modes, entry points, locales, or size constraints that should narrow the default Flow UI view checks?

## Checklist
### Theme And Direction
- Verify the affected view in both Lumo and Aura themes when the change is visual or layout-related.
- Check both light and dark theme variants when the task can affect colors, contrast, icons, or component state.
- Check right-to-left mode with `dir="rtl"` when the view contains aligned content, directional icons, or horizontal layout.

### Layout And Size
- Check the view at different practical sizes, including a narrow layout and a large desktop layout.
- Confirm that actions, filters, forms, and dialogs remain usable without clipped labels or overlapping controls.
- Verify that the view still opens correctly from its expected entry point: menu item, route, action, or dialog.

### Localization
- Confirm that view labels, action captions, validation messages, and empty states use message keys instead of hard-coded text.
- Verify available localizations for known supported languages when the task changes user-facing text.

## Risks
- View changes can look correct in the default theme while failing in another theme, variant, locale, direction, or size.

## References
- Vaadin right-to-left mode documentation: https://vaadin.com/docs/latest/flow/advanced/i18n-localization#supporting-right-to-left-mode
