# MVP 2 Regression Seed Material

This file holds early drafts of full functional QA scope for regression-prone areas. The content here is **not read by the assistant** during checklist generation and is **not part of the MVP 1 knowledge base**.

Its only purpose is to preserve detailed reusable check content discovered during MVP 1 work, so MVP 2 has a starting point. Do not link from this file into `knowledge/` and do not let MVP 1 outputs derive from it.

When the MVP 2 format is decided (see [regressions.md](regressions.md) and [roadmap.md](roadmap.md)), this material is migrated into the new format.

---

## URL Query Parameters

Source: extracted from the original `knowledge/regressions/url-query-parameters.md` during the MVP 1 framing pass on 2026-05-25.

Candidate reusable checks for the full QA scope of the URL Query Parameters area:

- Verify URL Query Parameters after changing more than one participating component or facet in the same view.
- Check browser refresh and Back/Forward navigation after URL Query Parameters are applied.
- Check repeated navigation to the same view with different URL Query Parameters from menu items or route links.
- Check the scenario with the Settings facet enabled when filters or view settings are involved.
- Check the scenario with a non-root context path.
- Check data loading when `dataLoadCoordinator` loads data in `ReadyEvent`.
- Confirm that views opened in `DIALOG` mode do not add or handle URL Query Parameters.

These were captured before the MVP 1 framing made `knowledge/regressions/` a breadcrumb-only zone. They are kept here to seed MVP 2; some may eventually move into individual `knowledge/jmix/` modules if they pass the non-obvious filter for MVP 1.
