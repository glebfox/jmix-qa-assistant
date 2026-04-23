# Answers

- Roles and permissions: only `admin` can deactivate; manager and regular user must not see the action.
- Affected views: user detail view and user browse view.
- Regression scope: existing create/edit/save flow for user entity must keep working.
- Environment: validate on Chrome; database is PostgreSQL for the pilot.
- Out of scope: bulk deactivation from browse view is not part of this task.
