<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReportScheduler — operations

Accessor: `client.report_scheduler` · Source: `walmart_apis/apis/report_scheduler.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.report_scheduler.delete_report_schedule

- **Route**: `DELETE /v3/reports/schedules/{scheduleId}`
- **Auth**: `access_token`
- **Signature**: `def delete_report_schedule(schedule_id: str, wm_svc_name: str, wm_qos_correlation_id: str, wm_sec_access_token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `schedule_id`, `wm_svc_name`, `wm_qos_correlation_id`, `wm_sec_access_token`
- **Params**: `schedule_id` — path `scheduleId` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN`
- **Returns (parsed)**: `RejectRecommendationsResponsePayload`
- **Returns (raw)**: `ApiResult[RejectRecommendationsResponsePayload, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RejectRecommendationsResponsePayload` | `walmart_apis/models/reject_recommendations_response_payload.py` |

### client.report_scheduler.get_all_report_schedules

- **Route**: `GET /v3/reports/schedules`
- **Auth**: `access_token`
- **Signature**: `def get_all_report_schedules(report_type: ReportType10OrStr, wm_svc_name: str, wm_qos_correlation_id: str, wm_sec_access_token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_type`, `wm_svc_name`, `wm_qos_correlation_id`, `wm_sec_access_token`
- **Params**: `report_type` — query `reportType` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN`
- **Returns (parsed)**: `V3ReportsSchedulesResponse`
- **Returns (raw)**: `ApiResult[V3ReportsSchedulesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReportType10OrStr` | `walmart_apis/models/enums/report_type10.py` |
| `V3ReportsSchedulesResponse` | `walmart_apis/models/v3_reports_schedules_response.py` |

### client.report_scheduler.get_report_schedule

- **Route**: `GET /v3/reports/schedules/{scheduleId}`
- **Auth**: `access_token`
- **Signature**: `def get_report_schedule(schedule_id: str, wm_svc_name: str, wm_qos_correlation_id: str, wm_sec_access_token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `schedule_id`, `wm_svc_name`, `wm_qos_correlation_id`, `wm_sec_access_token`
- **Params**: `schedule_id` — path `scheduleId` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN`
- **Returns (parsed)**: `V3ReportsSchedulesResponse1`
- **Returns (raw)**: `ApiResult[V3ReportsSchedulesResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V3ReportsSchedulesResponse1` | `walmart_apis/models/v3_reports_schedules_response1.py` |

### client.report_scheduler.update_report_schedule

- **Route**: `PUT /v3/reports/schedules/{scheduleId}`
- **Auth**: `access_token`
- **Signature**: `def update_report_schedule(schedule_id: str, wm_svc_name: str, wm_qos_correlation_id: str, wm_sec_access_token: str, *, body: V3ReportsSchedulesRequest | V3ReportsSchedulesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `schedule_id`, `wm_svc_name`, `wm_qos_correlation_id`, `wm_sec_access_token`
- **Params**: `schedule_id` — path `scheduleId` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `body` — JSON body
- **Returns (parsed)**: `V3ReportsSchedulesResponse1`
- **Returns (raw)**: `ApiResult[V3ReportsSchedulesResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V3ReportsSchedulesRequest` | `walmart_apis/models/v3_reports_schedules_request.py` |
| `V3ReportsSchedulesRequestDict` | `walmart_apis/models/v3_reports_schedules_request.py` |
| `V3ReportsSchedulesResponse1` | `walmart_apis/models/v3_reports_schedules_response1.py` |

