<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReportsApi — operations

Accessor: `client.reports_api` · Source: `walmart_apis/apis/reports_api.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reports_api.get_available_recon_report_dates

- **Route**: `GET /v3/report/reconreport/availableReconFiles`
- **Auth**: `access_token`
- **Signature**: `def get_available_recon_report_dates(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `ReconReportDateResponse`
- **Returns (raw)**: `ApiResult[ReconReportDateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReconReportDateResponse` | `walmart_apis/models/recon_report_date_response.py` |

### client.reports_api.get_available_v1_recon_report_as_json

- **Route**: `GET /v3/report/reconreport/reconFileJson`
- **Auth**: `access_token`
- **Signature**: `def get_available_v1_recon_report_as_json(report_date: str, offset: int, no_of_records: int, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_date`, `offset`, `no_of_records`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `report_date` — query `reportDate` · `offset` — query · `no_of_records` — query `noOfRecords` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `ReconReportV1AsJsonResponse`
- **Returns (raw)**: `ApiResult[ReconReportV1AsJsonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReconReportV1AsJsonResponse` | `walmart_apis/models/recon_report_v1_as_json_response.py` |

### client.reports_api.get_available_v1_recon_report_dates

- **Route**: `GET /v3/report/reconreport/availableReconFiles?reportVersion=v1`
- **Auth**: `access_token`
- **Signature**: `def get_available_v1_recon_report_dates(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `ReconReportDateResponse`
- **Returns (raw)**: `ApiResult[ReconReportDateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReconReportDateResponse` | `walmart_apis/models/recon_report_date_response.py` |

### client.reports_api.get_partner_performance

- **Route**: `GET /v3/report/payment/performance`
- **Auth**: `access_token`
- **Signature**: `def get_partner_performance(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `PartnerProgramPerformanceRes`
- **Returns (raw)**: `ApiResult[PartnerProgramPerformanceRes, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerProgramPerformanceRes` | `walmart_apis/models/partner_program_performance_res.py` |

### client.reports_api.get_partner_statement

- **Route**: `GET /v3/report/payment/statement`
- **Auth**: `access_token`
- **Signature**: `def get_partner_statement(wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `PartnerProgramStatementRes`
- **Returns (raw)**: `ApiResult[PartnerProgramStatementRes, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PartnerProgramStatementRes` | `walmart_apis/models/partner_program_statement_res.py` |

### client.reports_api.get_recon_report

- **Route**: `GET /v3/report/reconreport/reconFile`
- **Auth**: `access_token`
- **Signature**: `def get_recon_report(report_date: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_date`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `report_date` — query `reportDate` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, GetReconReportErrorBody]`
- **Error**: `GetReconReportErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `GetReconReportErrorBody` | `walmart_apis/errors/get_recon_report_error.py` |

### client.reports_api.get_recon_report_v1

- **Route**: `GET /v3/report/reconreport/reconFile?reportVersion=v1`
- **Auth**: `access_token`
- **Signature**: `def get_recon_report_v1(report_date: str, report_version: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_date`, `report_version`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `report_date` — query `reportDate` · `report_version` — query `reportVersion` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, GetReconReportV1ErrorBody]`
- **Error**: `GetReconReportV1ErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, anything unmapped]

| Type | Source |
| --- | --- |
| `GetReconReportV1ErrorBody` | `walmart_apis/errors/get_recon_report_v1_error.py` |

