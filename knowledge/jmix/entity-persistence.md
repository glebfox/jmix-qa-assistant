---
id: entity-persistence
title: Entity persistence changes
applies_to: feature, bugfix
triggers: entity, persistence, save, database, soft delete, audit, optimistic lock, active flag
always: false
---
## Questions
- Which entity fields are expected to change after the action?
- Should the change create a new record or update an existing one?
- Are soft delete, audit fields, versioning, or default values relevant here?

## Checklist
### Persistence
- The expected entity fields are actually persisted after save or action execution.
- Reloading the entity shows the same final state as the UI reported.
- Repeating the scenario does not create duplicate or inconsistent records.

### Data Integrity
- Existing records that should remain unchanged are not accidentally modified.
- Default values, audit fields, and version-sensitive updates still behave correctly.

## Risks
- UI changes around entity state often look correct before reload but fail at actual persistence.
