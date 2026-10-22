<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnRequestReport — operations

Accessor: `client.on_request_report` · Source: `walmart_apis/apis/on_request_report.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_request_report.generate_report

- **Route**: `POST /v3/reports/reportRequests`
- **Auth**: `access_token`
- **Signature**: `def generate_report(report_type: ReportType4OrStr, report_version: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, body: V3ReportsReportRequestsRequest | V3ReportsReportRequestsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_type`, `report_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`
- **Params**: `report_type` — query `reportType` · `report_version` — query `reportVersion` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3ReportsReportRequestsResponse1`
- **Returns (raw)**: `ApiResult[V3ReportsReportRequestsResponse1, GenerateReportErrorBody]`
- **Error**: `GenerateReportErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `ReportType4OrStr` | `walmart_apis/models/enums/report_type4.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ReportsReportRequestsRequest` | `walmart_apis/models/v3_reports_report_requests_request.py` |
| `V3ReportsReportRequestsRequestDict` | `walmart_apis/models/v3_reports_report_requests_request.py` |
| `V3ReportsReportRequestsResponse1` | `walmart_apis/models/v3_reports_report_requests_response1.py` |
| `GenerateReportErrorBody` | `walmart_apis/errors/generate_report_error.py` |

