<!-- Generated file — do not edit; regenerated with the SDK. -->

# WsrAttributionReports — operations

Accessor: `client.wsr_attribution_reports` · Source: `walmart_apis/apis/wsr_attribution_reports.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wsr_attribution_reports.get_tag_templates

- **Route**: `GET /v3/advertising/wsr/attribution/tag-templates/{templateType}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_tag_templates(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, *, template_type: TemplateTypeOrStr = TemplateType.NON_MACRO, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_svc_name`, `wm_qos_correlation_id`
- **Params**: `template_type` — path `templateType` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `WsrTagTemplatesResponse`
- **Returns (raw)**: `ApiResult[WsrTagTemplatesResponse, GetTagTemplatesErrorBody]`
- **Error**: `GetTagTemplatesErrorBody` — **Case A (typed)**
- **Error arms**: `WsrErrorResponse` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateTypeOrStr` | `walmart_apis/models/enums/template_type.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `WsrTagTemplatesResponse` | `walmart_apis/models/wsr_tag_templates_response.py` |
| `GetTagTemplatesErrorBody` | `walmart_apis/errors/get_tag_templates_error.py` |
| `WsrErrorResponse` | `walmart_apis/models/wsr_error_response.py` |

### client.wsr_attribution_reports.get_wsr_item_report

- **Route**: `POST /v3/advertising/wsr/attribution/item-report`
- **Auth**: `bearer_auth`
- **Signature**: `def get_wsr_item_report(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, body: WsrReportRequest | WsrReportRequestDict, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_svc_name`, `wm_qos_correlation_id`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `WsrItemReportResponse`
- **Returns (raw)**: `ApiResult[WsrItemReportResponse, GetWsrItemReportErrorBody]`
- **Error**: `GetWsrItemReportErrorBody` — **Case A (typed)**
- **Error arms**: `WsrErrorResponse` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WsrReportRequest` | `walmart_apis/models/wsr_report_request.py` |
| `WsrReportRequestDict` | `walmart_apis/models/wsr_report_request.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `WsrItemReportResponse` | `walmart_apis/models/wsr_item_report_response.py` |
| `GetWsrItemReportErrorBody` | `walmart_apis/errors/get_wsr_item_report_error.py` |
| `WsrErrorResponse` | `walmart_apis/models/wsr_error_response.py` |

### client.wsr_attribution_reports.get_wsr_performance_report

- **Route**: `POST /v3/advertising/wsr/attribution/performance-report`
- **Auth**: `bearer_auth`
- **Signature**: `def get_wsr_performance_report(wm_sec_access_token: str, wm_svc_name: str, wm_qos_correlation_id: str, body: WsrReportRequest | WsrReportRequestDict, *, wm_global_version: WmGlobalVersionOrStr = WmGlobalVersion._3_1, wm_market: WmMarketOrStr = WmMarket.US, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_svc_name`, `wm_qos_correlation_id`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `WsrPerformanceReportResponse`
- **Returns (raw)**: `ApiResult[WsrPerformanceReportResponse, GetWsrPerformanceReportErrorBody]`
- **Error**: `GetWsrPerformanceReportErrorBody` — **Case A (typed)**
- **Error arms**: `WsrErrorResponse` [400, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WsrReportRequest` | `walmart_apis/models/wsr_report_request.py` |
| `WsrReportRequestDict` | `walmart_apis/models/wsr_report_request.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `WsrPerformanceReportResponse` | `walmart_apis/models/wsr_performance_report_response.py` |
| `GetWsrPerformanceReportErrorBody` | `walmart_apis/errors/get_wsr_performance_report_error.py` |
| `WsrErrorResponse` | `walmart_apis/models/wsr_error_response.py` |

