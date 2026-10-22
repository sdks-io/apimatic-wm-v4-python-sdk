<!-- Generated file — do not edit; regenerated with the SDK. -->

# SemItemDiagnostics — operations

Accessor: `client.sem_item_diagnostics` · Source: `walmart_apis/apis/sem_item_diagnostics.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sem_item_diagnostics.get_issue_types

- **Route**: `GET /v3/advertising/sem/item-issues/issue-types`
- **Auth**: `access_token`
- **Signature**: `def get_issue_types(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_svc_name`, `wm_qos_correlation_id`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `dict[str, IssueMetadata]`
- **Returns (raw)**: `ApiResult[dict[str, IssueMetadata], GetIssueTypesErrorBody]`
- **Error**: `GetIssueTypesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [401, 403, 500, 503] · `ErrorResponse429` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `IssueMetadata` | `walmart_apis/models/issue_metadata.py` |
| `GetIssueTypesErrorBody` | `walmart_apis/errors/get_issue_types_error.py` |
| `ErrorResponse` | `walmart_apis/models/error_response.py` |
| `ErrorResponse429` | `walmart_apis/models/error_response429.py` |

### client.sem_item_diagnostics.search_item_issues

- **Route**: `POST /v3/advertising/sem/item-issues/search`
- **Auth**: `access_token`
- **Signature**: `def search_item_issues(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, accept: AcceptOrStr = Accept.APPLICATION_JSON, wm_consumer_channel_type: str | None = None, body: ItemDiagnosticSearchRequest | ItemDiagnosticSearchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_svc_name`, `wm_qos_correlation_id`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `ItemDiagnosticSearchResponse`
- **Returns (raw)**: `ApiResult[ItemDiagnosticSearchResponse, SearchItemIssuesErrorBody]`
- **Error**: `SearchItemIssuesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400, 401, 403, 422, 500, 503] · `ErrorResponse429` [429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `AcceptOrStr` | `walmart_apis/models/enums/accept.py` |
| `ItemDiagnosticSearchRequest` | `walmart_apis/models/item_diagnostic_search_request.py` |
| `ItemDiagnosticSearchRequestDict` | `walmart_apis/models/item_diagnostic_search_request.py` |
| `ItemDiagnosticSearchResponse` | `walmart_apis/models/item_diagnostic_search_response.py` |
| `SearchItemIssuesErrorBody` | `walmart_apis/errors/search_item_issues_error.py` |
| `ErrorResponse` | `walmart_apis/models/error_response.py` |
| `ErrorResponse429` | `walmart_apis/models/error_response429.py` |

