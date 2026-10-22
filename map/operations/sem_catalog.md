<!-- Generated file — do not edit; regenerated with the SDK. -->

# SemCatalog — operations

Accessor: `client.sem_catalog` · Source: `walmart_apis/apis/sem_catalog.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sem_catalog.get_eligible_items

- **Route**: `POST /v3/advertising/sem/items/eligibility`
- **Auth**: `bearer_auth`
- **Signature**: `def get_eligible_items(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: SemItemEligibilityRequest | SemItemEligibilityRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `SemCatalogueResponse`
- **Returns (raw)**: `ApiResult[SemCatalogueResponse, GetEligibleItemsErrorBody]`
- **Error**: `GetEligibleItemsErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemItemEligibilityRequest` | `walmart_apis/models/sem_item_eligibility_request.py` |
| `SemItemEligibilityRequestDict` | `walmart_apis/models/sem_item_eligibility_request.py` |
| `SemCatalogueResponse` | `walmart_apis/models/sem_catalogue_response.py` |
| `GetEligibleItemsErrorBody` | `walmart_apis/errors/get_eligible_items_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_catalog.get_item_recommendations

- **Route**: `GET /v3/advertising/sem/items/recommendations`
- **Auth**: `bearer_auth`
- **Signature**: `def get_item_recommendations(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, limit: int | None = 100, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `limit` — query · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `SemCatalogueResponse`
- **Returns (raw)**: `ApiResult[SemCatalogueResponse, GetItemRecommendationsErrorBody]`
- **Error**: `GetItemRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemCatalogueResponse` | `walmart_apis/models/sem_catalogue_response.py` |
| `GetItemRecommendationsErrorBody` | `walmart_apis/errors/get_item_recommendations_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

