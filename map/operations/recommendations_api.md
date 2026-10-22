<!-- Generated file — do not edit; regenerated with the SDK. -->

# RecommendationsApi — operations

Accessor: `client.recommendations_api` · Source: `walmart_apis/apis/recommendations_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.recommendations_api.get_fulfill_with_wfs_recommendations

- **Route**: `GET /v3/wfs/recommendation/fulfil-with-wfs`
- **Signature**: `def get_fulfill_with_wfs_recommendations(content_type: str, accept: str, wm_global_version: str, wm_market: str, wm_audit_origin_source: str, *, customer_favorite: bool | None = None, show_insights: bool | None = False, limit: int | None = 30, offset: int | None = 0, sort_by: str | None = "estimatedSalesLift", sort_order: SortOrderOrStr | None = SortOrder.DESC, show_hidden_records_only: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `accept`, `wm_global_version`, `wm_market`, `wm_audit_origin_source`
- **Params**: `customer_favorite` — query `customerFavorite` · `show_insights` — query `showInsights` · `limit` — query · `offset` — query · `sort_by` — query · `sort_order` — query · `show_hidden_records_only` — query `showHiddenRecordsOnly` · `content_type` — header `Content-Type` · `accept` — header `Accept` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_audit_origin_source` — header `wm_audit.origin_source`
- **Returns (parsed)**: `V3WfsRecommendationFulfilWithWfsResponse`
- **Returns (raw)**: `ApiResult[V3WfsRecommendationFulfilWithWfsResponse, GetFulfillWithWfsrecommendationsErrorBody]`
- **Error**: `GetFulfillWithWfsrecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse2` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `walmart_apis/models/enums/sort_order.py` |
| `V3WfsRecommendationFulfilWithWfsResponse` | `walmart_apis/models/v3_wfs_recommendation_fulfil_with_wfs_response.py` |
| `GetFulfillWithWfsrecommendationsErrorBody` | `walmart_apis/errors/get_fulfill_with_wfsrecommendations_error.py` |
| `ErrorResponse2` | `walmart_apis/models/error_response2.py` |

### client.recommendations_api.get_restock_recommendations

- **Route**: `GET /v3/wfs/recommendation/restock`
- **Signature**: `def get_restock_recommendations(authorization: str, content_type: str, accept: str, wm_global_version: str, wm_market: str, wm_audit_origin_source: str, *, customer_favorite: bool | None = None, show_insights: bool | None = True, limit: int | None = 30, offset: int | None = 0, sort_by: str | None = "forecastedSalesLift", sort_order: SortOrderOrStr | None = SortOrder.DESC, show_hidden_records_only: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `authorization`, `content_type`, `accept`, `wm_global_version`, `wm_market`, `wm_audit_origin_source`
- **Params**: `customer_favorite` — query `customerFavorite` · `show_insights` — query `showInsights` · `limit` — query · `offset` — query · `sort_by` — query · `sort_order` — query · `show_hidden_records_only` — query `showHiddenRecordsOnly` · `authorization` — header `Authorization` · `content_type` — header `Content-Type` · `accept` — header `Accept` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_audit_origin_source` — header `wm_audit.origin_source`
- **Returns (parsed)**: `V3WfsRecommendationRestockResponse`
- **Returns (raw)**: `ApiResult[V3WfsRecommendationRestockResponse, GetRestockRecommendationsErrorBody]`
- **Error**: `GetRestockRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse2` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `walmart_apis/models/enums/sort_order.py` |
| `V3WfsRecommendationRestockResponse` | `walmart_apis/models/v3_wfs_recommendation_restock_response.py` |
| `GetRestockRecommendationsErrorBody` | `walmart_apis/errors/get_restock_recommendations_error.py` |
| `ErrorResponse2` | `walmart_apis/models/error_response2.py` |

### client.recommendations_api.get_shipment_quantity_recommendations

- **Route**: `POST /v3/wfs/recommendation/shipment-quantity`
- **Signature**: `def get_shipment_quantity_recommendations(authorization: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, accept: str, wm_global_version: str, wm_market: str, body: V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `authorization`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `accept`, `wm_global_version`, `wm_market`, `body`
- **Params**: `authorization` — header `Authorization` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `accept` — header `Accept` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3WfsRecommendationShipmentQuantityResponse`
- **Returns (raw)**: `ApiResult[V3WfsRecommendationShipmentQuantityResponse, GetShipmentQuantityRecommendationsErrorBody]`
- **Error**: `GetShipmentQuantityRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse2` [400, 500] · `NotFoundResponse` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V3WfsRecommendationShipmentQuantityRequest` | `walmart_apis/models/v3_wfs_recommendation_shipment_quantity_request.py` |
| `V3WfsRecommendationShipmentQuantityRequestDict` | `walmart_apis/models/v3_wfs_recommendation_shipment_quantity_request.py` |
| `V3WfsRecommendationShipmentQuantityResponse` | `walmart_apis/models/v3_wfs_recommendation_shipment_quantity_response.py` |
| `GetShipmentQuantityRecommendationsErrorBody` | `walmart_apis/errors/get_shipment_quantity_recommendations_error.py` |
| `ErrorResponse2` | `walmart_apis/models/error_response2.py` |
| `NotFoundResponse` | `walmart_apis/models/not_found_response.py` |

### client.recommendations_api.get_unpublished_recommendations

- **Route**: `GET /v3/wfs/recommendation/unpublished`
- **Signature**: `def get_unpublished_recommendations(content_type: str, accept: str, wm_global_version: str, wm_market: str, wm_audit_origin_source: str, *, customer_favorite: bool | None = None, show_insights: bool | None = False, limit: int | None = 30, offset: int | None = 0, sort_by: str | None = "estimatedSalesLift", sort_order: SortOrderOrStr | None = SortOrder.DESC, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `accept`, `wm_global_version`, `wm_market`, `wm_audit_origin_source`
- **Params**: `customer_favorite` — query `customerFavorite` · `show_insights` — query `showInsights` · `limit` — query · `offset` — query · `sort_by` — query · `sort_order` — query · `content_type` — header `Content-Type` · `accept` — header `Accept` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_audit_origin_source` — header `wm_audit.origin_source`
- **Returns (parsed)**: `V3WfsRecommendationUnpublishedResponse`
- **Returns (raw)**: `ApiResult[V3WfsRecommendationUnpublishedResponse, GetUnpublishedRecommendationsErrorBody]`
- **Error**: `GetUnpublishedRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse2` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `walmart_apis/models/enums/sort_order.py` |
| `V3WfsRecommendationUnpublishedResponse` | `walmart_apis/models/v3_wfs_recommendation_unpublished_response.py` |
| `GetUnpublishedRecommendationsErrorBody` | `walmart_apis/errors/get_unpublished_recommendations_error.py` |
| `ErrorResponse2` | `walmart_apis/models/error_response2.py` |

