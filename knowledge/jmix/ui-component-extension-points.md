---
id: ui-component-extension-points
title: Flow UI component extension points
applies_to: feature, bugfix
triggers: event, listener, handler, subscribe, install, generator, delegate, xml subscription, extension point
always: false
---
## Questions
- Which events, listeners, handlers, delegates, or generators does the component expose?

## Checklist
### Extension Points
- Verify `@Subscribe` availability for the component events.
- Verify `@Install` availability for component delegates, generators, or handlers.

## Risks
