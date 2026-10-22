<!-- Generated file — do not edit; regenerated with the SDK. -->

# AssortmentRecommendations — operations

Accessor: `client.assortment_recommendations` · Source: `walmart_apis/apis/assortment_recommendations.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.assortment_recommendations.get_assortment_recommendation_trends

- **Route**: `GET /v3/growth/assortment/recommendations/trends`
- **Signature**: `def get_assortment_recommendation_trends(recommendation_unique_id: str, wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, trend_types: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `recommendation_unique_id`, `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `recommendation_unique_id` — query `recommendationUniqueId` · `trend_types` — query `trendTypes` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3GrowthAssortmentRecommendationsTrendsResponse`
- **Returns (raw)**: `ApiResult[V3GrowthAssortmentRecommendationsTrendsResponse, GetAssortmentRecommendationTrendsErrorBody]`
- **Error**: `GetAssortmentRecommendationTrendsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse1` [400, 500] · `V3Token500Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthAssortmentRecommendationsTrendsResponse` | `walmart_apis/models/v3_growth_assortment_recommendations_trends_response.py` |
| `GetAssortmentRecommendationTrendsErrorBody` | `walmart_apis/errors/get_assortment_recommendation_trends_error.py` |
| `ErrorResponse1` | `walmart_apis/models/error_response1.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

### client.assortment_recommendations.get_assortment_recommendation_variants

- **Route**: `GET /v3/growth/assortment/recommendations/variants`
- **Signature**: `def get_assortment_recommendation_variants(primary_variant_item_id: str, wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, next_cursor: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `primary_variant_item_id`, `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `primary_variant_item_id` — query `primaryVariantItemId` · `next_cursor` — query `nextCursor` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3GrowthAssortmentRecommendationsVariantsResponse`
- **Returns (raw)**: `ApiResult[V3GrowthAssortmentRecommendationsVariantsResponse, GetAssortmentRecommendationVariantsErrorBody]`
- **Error**: `GetAssortmentRecommendationVariantsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse1` [400, 500] · `V3Token500Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthAssortmentRecommendationsVariantsResponse` | `walmart_apis/models/v3_growth_assortment_recommendations_variants_response.py` |
| `GetAssortmentRecommendationVariantsErrorBody` | `walmart_apis/errors/get_assortment_recommendation_variants_error.py` |
| `ErrorResponse1` | `walmart_apis/models/error_response1.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

### client.assortment_recommendations.get_assortment_recommendations

- **Route**: `POST /v3/growth/assortment/recommendations`
- **Signature**: `def get_assortment_recommendations(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthAssortmentRecommendationsRequest | V3GrowthAssortmentRecommendationsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `body`
- **Params**: `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3GrowthAssortmentRecommendationsResponse`
- **Returns (raw)**: `ApiResult[V3GrowthAssortmentRecommendationsResponse, GetAssortmentRecommendationsErrorBody]`
- **Error**: `GetAssortmentRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse1` [400, 500] · `V3Token500Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthAssortmentRecommendationsRequest` | `walmart_apis/models/v3_growth_assortment_recommendations_request.py` |
| `V3GrowthAssortmentRecommendationsRequestDict` | `walmart_apis/models/v3_growth_assortment_recommendations_request.py` |
| `V3GrowthAssortmentRecommendationsResponse` | `walmart_apis/models/v3_growth_assortment_recommendations_response.py` |
| `GetAssortmentRecommendationsErrorBody` | `walmart_apis/errors/get_assortment_recommendations_error.py` |
| `ErrorResponse1` | `walmart_apis/models/error_response1.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

### client.assortment_recommendations.get_categorization_details_of_assortment_recommendations

- **Route**: `POST /v3/growth/assortment/recommendations/categorization/counts`
- **Signature**: `def get_categorization_details_of_assortment_recommendations(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3GrowthAssortmentRecommendationsCategorizationCountsRequest | V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3GrowthAssortmentRecommendationsCategorizationCountsResponse`
- **Returns (raw)**: `ApiResult[V3GrowthAssortmentRecommendationsCategorizationCountsResponse, GetCategorizationDetailsOfAssortmentRecommendationsErrorBody]`
- **Error**: `GetCategorizationDetailsOfAssortmentRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse1` [400, 500] · `V3Token500Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3GrowthAssortmentRecommendationsCategorizationCountsRequest` | `walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_request.py` |
| `V3GrowthAssortmentRecommendationsCategorizationCountsRequestDict` | `walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_request.py` |
| `V3GrowthAssortmentRecommendationsCategorizationCountsResponse` | `walmart_apis/models/v3_growth_assortment_recommendations_categorization_counts_response.py` |
| `GetCategorizationDetailsOfAssortmentRecommendationsErrorBody` | `walmart_apis/errors/get_categorization_details_of_assortment_recommendations_error.py` |
| `ErrorResponse1` | `walmart_apis/models/error_response1.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

### client.assortment_recommendations.reject_assortment_recommendations

- **Route**: `PUT /v3/growth/assortment/recommendations/rejections`
- **Signature**: `def reject_assortment_recommendations(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthAssortmentRecommendationsRejectionsRequest | V3GrowthAssortmentRecommendationsRejectionsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `body`
- **Params**: `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3GrowthAssortmentRecommendationsRejectionsResponse`
- **Returns (raw)**: `ApiResult[V3GrowthAssortmentRecommendationsRejectionsResponse, RejectAssortmentRecommendationsErrorBody]`
- **Error**: `RejectAssortmentRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse1` [400, 500] · `V3Token500Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthAssortmentRecommendationsRejectionsRequest` | `walmart_apis/models/v3_growth_assortment_recommendations_rejections_request.py` |
| `V3GrowthAssortmentRecommendationsRejectionsRequestDict` | `walmart_apis/models/v3_growth_assortment_recommendations_rejections_request.py` |
| `V3GrowthAssortmentRecommendationsRejectionsResponse` | `walmart_apis/models/v3_growth_assortment_recommendations_rejections_response.py` |
| `RejectAssortmentRecommendationsErrorBody` | `walmart_apis/errors/reject_assortment_recommendations_error.py` |
| `ErrorResponse1` | `walmart_apis/models/error_response1.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

