---
id: localization
title: Localization
applies_to: feature, bugfix
triggers: localization, locale, language, i18n, message key, message keys, message bundle, built-in text, builtin text, component text, label, action caption, validation message, empty state, hard-coded text
always: false
---
## Questions
- Does the change add or modify any user-visible text (component labels, view labels, action captions, validation messages, empty states, built-in component UI text)?

## Checklist
### Localization
- Confirm that all user-visible text (view labels, action captions, validation messages, empty states, component built-in text) uses message keys instead of hard-coded text.
- Verify available localizations for known supported languages.

## Risks
- Built-in component text can bypass application message bundles and appear as hard-coded text in localized applications.
- View-level text added during a feature change is often committed as a hard-coded string and missed by translation passes.
