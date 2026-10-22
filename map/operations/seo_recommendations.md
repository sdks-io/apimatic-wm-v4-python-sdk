<!-- Generated file — do not edit; regenerated with the SDK. -->

# SeoRecommendations — operations

Accessor: `client.seo_recommendations` · Source: `walmart_apis/apis/seo_recommendations.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.seo_recommendations.get_seo_recommendations

- **Route**: `POST /v3/seo/recommendation/getItems`
- **Auth**: `access_token`
- **Signature**: `def get_seo_recommendations(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, accept: str, *, status: Status2OrStr | None = None, limit: str | None = None, next_cursor: str | None = None, previous_cursor: str | None = None, wm_consumer_channel_type: str | None = None, body: V3SeoRecommendationGetItemsRequest | V3SeoRecommendationGetItemsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `accept`
- **Params**: `status` — query · `limit` — query · `next_cursor` — query · `previous_cursor` — query · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3SeoRecommendationGetItemsResponse`
- **Returns (raw)**: `ApiResult[V3SeoRecommendationGetItemsResponse, GetSeoRecommendationsErrorBody]`
- **Error**: `GetSeoRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `V3SeoRecommendationGetItems400Error1` [400] · `V3SeoRecommendationGetItems500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Status2OrStr` | `walmart_apis/models/enums/status2.py` |
| `V3SeoRecommendationGetItemsRequest` | `walmart_apis/models/v3_seo_recommendation_get_items_request.py` |
| `V3SeoRecommendationGetItemsRequestDict` | `walmart_apis/models/v3_seo_recommendation_get_items_request.py` |
| `V3SeoRecommendationGetItemsResponse` | `walmart_apis/models/v3_seo_recommendation_get_items_response.py` |
| `GetSeoRecommendationsErrorBody` | `walmart_apis/errors/get_seo_recommendations_error.py` |
| `V3SeoRecommendationGetItems400Error1` | `walmart_apis/models/v3_seo_recommendation_get_items400_error1.py` |
| `V3SeoRecommendationGetItems500Error1` | `walmart_apis/models/v3_seo_recommendation_get_items500_error1.py` |

### client.seo_recommendations.update_seo_recommendations

- **Route**: `POST /v3/seo/recommendation/updateItems/{itemId}/{decision}`
- **Auth**: `access_token`
- **Signature**: `def update_seo_recommendations(item_id: str, decision: DecisionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, accept: str, *, wm_consumer_channel_type: str | None = None, body: V3SeoRecommendationUpdateItemsRequest | V3SeoRecommendationUpdateItemsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `item_id`, `decision`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `accept`
- **Params**: `item_id` — path `itemId` · `decision` — path · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3SeoRecommendationUpdateItemsResponse`
- **Returns (raw)**: `ApiResult[V3SeoRecommendationUpdateItemsResponse, UpdateSeoRecommendationsErrorBody]`
- **Error**: `UpdateSeoRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `V3SeoRecommendationUpdateItems400Error1` [400] · `V3SeoRecommendationUpdateItems404Error1` [404] · `V3SeoRecommendationUpdateItems500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DecisionOrStr` | `walmart_apis/models/enums/decision.py` |
| `V3SeoRecommendationUpdateItemsRequest` | `walmart_apis/models/v3_seo_recommendation_update_items_request.py` |
| `V3SeoRecommendationUpdateItemsRequestDict` | `walmart_apis/models/v3_seo_recommendation_update_items_request.py` |
| `V3SeoRecommendationUpdateItemsResponse` | `walmart_apis/models/v3_seo_recommendation_update_items_response.py` |
| `UpdateSeoRecommendationsErrorBody` | `walmart_apis/errors/update_seo_recommendations_error.py` |
| `V3SeoRecommendationUpdateItems400Error1` | `walmart_apis/models/v3_seo_recommendation_update_items400_error1.py` |
| `V3SeoRecommendationUpdateItems404Error1` | `walmart_apis/models/v3_seo_recommendation_update_items404_error1.py` |
| `V3SeoRecommendationUpdateItems500Error1` | `walmart_apis/models/v3_seo_recommendation_update_items500_error1.py` |

