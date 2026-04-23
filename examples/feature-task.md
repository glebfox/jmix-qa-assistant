# Task
Title: Add deactivate action to user detail view
Type: feature
Labels: flow-ui, security, entity, data

## Description
Add a new "Deactivate" action to the user detail view in Flow UI.
Only administrators can deactivate a user.
Deactivation should set the `active` flag to `false` and save the entity.
The user browse view should hide inactive users by default and allow showing them with a filter.

## Acceptance Criteria
- Administrator sees the "Deactivate" action in the user detail view when the user is active.
- Clicking "Deactivate" changes `active=false` and persists the change.
- Non-admin users do not see the deactivate action.
- Inactive users are hidden by default in the browse view.
- A filter allows showing inactive users in the browse view.

## Changed Areas
- flow-ui
- security
- entity persistence
- data loading

## Known Risks
- Action may be visible for the wrong role.
- User list filter may break existing browse behavior.
- Deactivation may update UI but not persist the entity.

## Context
The task changes the existing user detail view and browse view.
The `User` entity already has the `active` flag.
The team mainly tests on PostgreSQL and Chrome.
