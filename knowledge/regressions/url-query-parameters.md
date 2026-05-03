---
id: url-query-parameters
title: URL Query Parameters regressions
applies_to: feature, bugfix
triggers: url query parameters, urlqueryparameters, query parameters, route query, genericFilterUrlQueryParametersFacet, propertyFilterUrlQueryParametersFacet, settings facet, context path, dialog mode
always: false
---
## Questions
- Does the task add, change, or depend on URL Query Parameters?
- Does the view combine URL Query Parameters with filters, pagination, settings, menu navigation, or context path changes?
- Should the scenario work after browser refresh, Back/Forward navigation, or repeated menu navigation?

## Checklist
### URL Query Parameters
- Verify URL Query Parameters after changing more than one participating component or facet in the same view.
- Check browser refresh and Back/Forward navigation after URL Query Parameters are applied.
- Check repeated navigation to the same view with different URL Query Parameters from menu items or route links.
- Check the scenario with the Settings facet enabled when filters or view settings are involved.
- Check the scenario with a non-root context path.
- Check data loading when `dataLoadCoordinator` loads data in `ReadyEvent`.
- Confirm that views opened in `DIALOG` mode do not add or handle URL Query Parameters.

### Linked Regression Issues
- Check [#3802 Only last change to UrlQueryParametersFacet is applied](https://github.com/jmix-framework/jmix/issues/3802).
- Check [#3420 Problem with URL changing in browser address bar when using urlQueryParameters in the menu](https://github.com/jmix-framework/jmix/issues/3420).
- Check [#3345 URL query parameters are applied multiple times](https://github.com/jmix-framework/jmix/issues/3345).
- Check [#3654 URL not updating after navigation](https://github.com/jmix-framework/jmix/issues/3654).
- Check [#3661 Unexpected behavior of the view with different URL query parameters](https://github.com/jmix-framework/jmix/issues/3661).
- Check [#4235 Simultaneous use of UrlQueryParameters facets for filters breaks URL](https://github.com/jmix-framework/jmix/issues/4235).
- Check [#4981 URL query parameters for pagination ignores data loader refreshing](https://github.com/jmix-framework/jmix/issues/4981).
- Check [#5046 The filter configuration from the URL query parameters should have priority over the default configuration](https://github.com/jmix-framework/jmix/issues/5046).

## TODO
- Replace linked issue references with detailed reusable regression scenarios after the cases are reviewed and summarized.

## Risks
- URL Query Parameters behavior is especially regression-prone because it combines routing, browser history, facets, filters, loaders, pagination, and view lifecycle.
