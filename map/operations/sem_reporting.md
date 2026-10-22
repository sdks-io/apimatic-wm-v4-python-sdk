<!-- Generated file — do not edit; regenerated with the SDK. -->

# SemReporting — operations

Accessor: `client.sem_reporting` · Source: `walmart_apis/apis/sem_reporting.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sem_reporting.get_billing_history

- **Route**: `POST /v3/advertising/sem/billing-history`
- **Auth**: `bearer_auth`
- **Signature**: `def get_billing_history(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, body: SemBillingHistoryRequest | SemBillingHistoryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `SemBillingHistoryResponse`
- **Returns (raw)**: `ApiResult[SemBillingHistoryResponse, GetBillingHistoryErrorBody]`
- **Error**: `GetBillingHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemBillingHistoryRequest` | `walmart_apis/models/sem_billing_history_request.py` |
| `SemBillingHistoryRequestDict` | `walmart_apis/models/sem_billing_history_request.py` |
| `SemBillingHistoryResponse` | `walmart_apis/models/sem_billing_history_response.py` |
| `GetBillingHistoryErrorBody` | `walmart_apis/errors/get_billing_history_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_reporting.get_campaign_level_summary

- **Route**: `POST /v3/advertising/sem/campaigns/performance-summary`
- **Auth**: `bearer_auth`
- **Signature**: `def get_campaign_level_summary(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, body: SemReportRequest | SemReportRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `SemCampaignLevelReportResponse`
- **Returns (raw)**: `ApiResult[SemCampaignLevelReportResponse, GetCampaignLevelSummaryErrorBody]`
- **Error**: `GetCampaignLevelSummaryErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemReportRequest` | `walmart_apis/models/sem_report_request.py` |
| `SemReportRequestDict` | `walmart_apis/models/sem_report_request.py` |
| `SemCampaignLevelReportResponse` | `walmart_apis/models/sem_campaign_level_report_response.py` |
| `GetCampaignLevelSummaryErrorBody` | `walmart_apis/errors/get_campaign_level_summary_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

### client.sem_reporting.get_item_level_summary

- **Route**: `POST /v3/advertising/sem/campaigns/{campaignId}/item-level-summary`
- **Auth**: `bearer_auth`
- **Signature**: `def get_item_level_summary(campaign_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, body: SemReportRequest | SemReportRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `campaign_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `campaign_id` — path `campaignId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `SemItemLevelReportResponse`
- **Returns (raw)**: `ApiResult[SemItemLevelReportResponse, GetItemLevelSummaryErrorBody]`
- **Error**: `GetItemLevelSummaryErrorBody` — **Case A (typed)**
- **Error arms**: `SemErrorResponse400` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SemReportRequest` | `walmart_apis/models/sem_report_request.py` |
| `SemReportRequestDict` | `walmart_apis/models/sem_report_request.py` |
| `SemItemLevelReportResponse` | `walmart_apis/models/sem_item_level_report_response.py` |
| `GetItemLevelSummaryErrorBody` | `walmart_apis/errors/get_item_level_summary_error.py` |
| `SemErrorResponse400` | `walmart_apis/models/sem_error_response400.py` |

