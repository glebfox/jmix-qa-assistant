---
id: security
title: Security and permissions
applies_to: feature, bugfix
triggers: security, role, permission, policy, access, visible, hidden, admin, restricted
always: false
---
## Questions
- Which roles should have access, and which must not?
- Is the requirement about visibility, actual permission enforcement, or both?
- What should happen if a user without permission reaches the screen or action indirectly?

## Checklist
### Role Coverage
- Allowed roles can see and execute the intended action.
- Disallowed roles do not see the action or cannot execute it.
- Permission behavior is consistent across direct navigation and indirect access paths.

### Enforcement
- The system does not rely only on UI visibility when backend enforcement is expected.
- Error or access-denied behavior is clear and does not expose partial state changes.

## Risks
- Security regressions often hide in mismatches between UI visibility and actual permission enforcement.
