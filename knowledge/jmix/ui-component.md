---
id: ui-component
title: Flow UI component changes
applies_to: feature, bugfix
triggers: component, ui component, field, input, picker, datepicker, rich text editor, richtexteditor, focus, focus-ring, theme variant, listener, handler, subscribe, install, lumo, aura, rtl, localization, i18n
always: false
---
## Questions
- Is the changed component a field component?
- Does the component support theme variants?
- Does the component provide built-in text that requires i18n?
- Does the component expose events, listeners, handlers, or XML subscriptions?

## Checklist
### Theme And Variant
- Verify the component in both Lumo and Aura themes when the task changes visual appearance or interaction state.
- Check light and dark theme variants when color, contrast, icon, error, disabled, or read-only state can be affected.
- Check component-specific theme variants when the component supports them.
- Check right-to-left mode with `dir="rtl"` when the component has directional layout, icons, prefix or suffix content, or inline controls.

### Focus And Keyboard
- Check focus-ring behavior by keyboard tab navigation in Lumo.
- Check focus-ring behavior by any focus interaction in Aura.
- Confirm that keyboard focus is visible and does not produce unexpected layout shifts.

### Field Behavior
- For field components, verify label rendering and that clicking the label focuses the input when applicable.
- For field components, verify required indicator appearance in both Aura and Lumo because the visual behavior differs by theme.
- For field components, verify helper text, error message, read-only state, disabled state, and placeholder when supported.
- For field components, verify prefix and suffix components when they are part of the component design.

### Extension Points And I18n
- Verify `@Subscribe` and `@Install` availability when the component provides listeners, delegates, generators, or handlers.
- If the component has built-in UI text, verify message keys and available localization for known supported languages.

## Risks
- Component changes often regress only in non-default themes, focus paths, RTL mode, or field states that are easy to skip manually.

## References
- Vaadin right-to-left mode documentation: https://vaadin.com/docs/latest/flow/advanced/i18n-localization#supporting-right-to-left-mode
