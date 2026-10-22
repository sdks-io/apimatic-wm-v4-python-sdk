<!-- Generated file — do not edit; regenerated with the SDK. -->

# SemCampaignManagement — operations

Accessor: `client.sem_campaign_management` · Source: `walmart_apis/apis/sem_campaign_management.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sem_campaign_management.create_campaign

- **Route**: `POST /v3/advertising/sem/campaigns`
- **Auth**: `bearer_auth`
- **Signature**: `def create_campaign(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: SemCampaignCreateRequest | SemCampaignCreateRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `SemCampaignResponse`
- **Returns (raw)**: `ApiResult[SemCampaignResponse, CreateCampaignErrorBody]`
- **Error**: `CreateCampaignErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemCampaignCreateRequest` | `walmart_apis/models/sem_campaign_create_request.py` |
| `SemCampaignCreateRequestDict` | `walmart_apis/models/sem_campaign_create_request.py` |
| `SemCampaignResponse` | `walmart_apis/models/sem_campaign_response.py` |
| `CreateCampaignErrorBody` | `walmart_apis/errors/create_campaign_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_campaign_management.delete_campaign

- **Route**: `DELETE /v3/advertising/sem/campaigns/{campaignId}`
- **Auth**: `bearer_auth`
- **Signature**: `def delete_campaign(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `campaign_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `campaign_id` — path `campaignId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `SemCampaignResponse`
- **Returns (raw)**: `ApiResult[SemCampaignResponse, DeleteCampaignErrorBody]`
- **Error**: `DeleteCampaignErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemCampaignResponse` | `walmart_apis/models/sem_campaign_response.py` |
| `DeleteCampaignErrorBody` | `walmart_apis/errors/delete_campaign_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_campaign_management.get_campaign_details

- **Route**: `GET /v3/advertising/sem/campaigns/{campaignId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_campaign_details(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `campaign_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `campaign_id` — path `campaignId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `SemCampaign`
- **Returns (raw)**: `ApiResult[SemCampaign, GetCampaignDetailsErrorBody]`
- **Error**: `GetCampaignDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemCampaign` | `walmart_apis/models/sem_campaign.py` |
| `GetCampaignDetailsErrorBody` | `walmart_apis/errors/get_campaign_details_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_campaign_management.search_campaign_recommendations

- **Route**: `POST /v3/advertising/sem/campaigns/recommendations/search`
- **Auth**: `access_token`
- **Signature**: `def search_campaign_recommendations(wm_svc_name: str, wm_qos_correlation_id: str, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, accept: AcceptOrStr = Accept.APPLICATION_JSON, wm_consumer_channel_type: str | None = None, body: CampaignRecommendationsSearchRequest | CampaignRecommendationsSearchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_svc_name`, `wm_qos_correlation_id`
- **Params**: `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `CampaignRecommendationsSearchResponse`
- **Returns (raw)**: `ApiResult[CampaignRecommendationsSearchResponse, SearchCampaignRecommendationsErrorBody]`
- **Error**: `SearchCampaignRecommendationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400, 401, 403, 422, 500, 503] · `ErrorResponse429` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `AcceptOrStr` | `walmart_apis/models/enums/accept.py` |
| `CampaignRecommendationsSearchRequest` | `walmart_apis/models/campaign_recommendations_search_request.py` |
| `CampaignRecommendationsSearchRequestDict` | `walmart_apis/models/campaign_recommendations_search_request.py` |
| `CampaignRecommendationsSearchResponse` | `walmart_apis/models/campaign_recommendations_search_response.py` |
| `SearchCampaignRecommendationsErrorBody` | `walmart_apis/errors/search_campaign_recommendations_error.py` |
| `ErrorResponse` | `walmart_apis/models/error_response.py` |
| `ErrorResponse429` | `walmart_apis/models/error_response429.py` |

### client.sem_campaign_management.stop_campaign

- **Route**: `PUT /v3/advertising/sem/campaigns/{campaignId}/stop`
- **Auth**: `bearer_auth`
- **Signature**: `def stop_campaign(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `campaign_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `campaign_id` — path `campaignId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `SemCampaignResponse`
- **Returns (raw)**: `ApiResult[SemCampaignResponse, StopCampaignErrorBody]`
- **Error**: `StopCampaignErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemCampaignResponse` | `walmart_apis/models/sem_campaign_response.py` |
| `StopCampaignErrorBody` | `walmart_apis/errors/stop_campaign_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_campaign_management.update_campaign

- **Route**: `PUT /v3/advertising/sem/campaigns/{campaignId}`
- **Auth**: `bearer_auth`
- **Signature**: `def update_campaign(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, body: SemCampaignUpdateRequest | SemCampaignUpdateRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `campaign_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `body`
- **Params**: `campaign_id` — path `campaignId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `SemCampaignResponse`
- **Returns (raw)**: `ApiResult[SemCampaignResponse, UpdateCampaignErrorBody]`
- **Error**: `UpdateCampaignErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemCampaignUpdateRequest` | `walmart_apis/models/sem_campaign_update_request.py` |
| `SemCampaignUpdateRequestDict` | `walmart_apis/models/sem_campaign_update_request.py` |
| `SemCampaignResponse` | `walmart_apis/models/sem_campaign_response.py` |
| `UpdateCampaignErrorBody` | `walmart_apis/errors/update_campaign_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

