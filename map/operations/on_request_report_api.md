<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnRequestReportApi — operations

Accessor: `client.on_request_report_api` · Source: `walmart_apis/apis/on_request_report_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_request_report_api.download_report

- **Route**: `GET /v3/reports/downloadReport`
- **Auth**: `access_token`
- **Signature**: `def download_report(request_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `request_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`
- **Params**: `request_id` — query `requestId` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `DownloadReportResponse`
- **Returns (raw)**: `ApiResult[DownloadReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `DownloadReportResponse` | `walmart_apis/models/download_report_response.py` |

### client.on_request_report_api.get_requests_status

- **Route**: `GET /v3/reports/reportRequests`
- **Auth**: `access_token`
- **Signature**: `def get_requests_status(report_type: ReportType4OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, report_version: str | None = None, request_status: RequestStatus4OrStr | None = None, request_submission_start_date: str | None = None, request_submission_end_date: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_type`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`
- **Params**: `report_type` — query `reportType` · `report_version` — query `reportVersion` · `request_status` — query `requestStatus` · `request_submission_start_date` — query `requestSubmissionStartDate` · `request_submission_end_date` — query `requestSubmissionEndDate` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `RequestsStatusResponse`
- **Returns (raw)**: `ApiResult[RequestsStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReportType4OrStr` | `walmart_apis/models/enums/report_type4.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `RequestStatus4OrStr` | `walmart_apis/models/enums/request_status4.py` |
| `RequestsStatusResponse` | `walmart_apis/models/requests_status_response.py` |

### client.on_request_report_api.get_single_request_status

- **Route**: `GET /v3/reports/reportRequests/{requestId}`
- **Auth**: `access_token`
- **Signature**: `def get_single_request_status(request_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `request_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`
- **Params**: `request_id` — path `requestId` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `RequestStatusResponse`
- **Returns (raw)**: `ApiResult[RequestStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `RequestStatusResponse` | `walmart_apis/models/request_status_response.py` |

