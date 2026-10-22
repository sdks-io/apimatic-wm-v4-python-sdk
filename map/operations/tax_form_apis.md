<!-- Generated file — do not edit; regenerated with the SDK. -->

# TaxFormApis — operations

Accessor: `client.tax_form_apis` · Source: `walmart_apis/apis/tax_form_apis.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.tax_form_apis.download_tax_form

- **Route**: `GET /v1/settings/downloadtaxformprofile`
- **Auth**: `access_token`
- **Signature**: `def download_tax_form(payout_year: str, tax_form_type: str, form_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_global_version: WmGlobalVersionOrStr, wm_market: str, wm_partner_id: str, wm_tenant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payout_year`, `tax_form_type`, `form_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_global_version`, `wm_market`, `wm_partner_id`, `wm_tenant_id`
- **Params**: `payout_year` — query `payoutYear` · `tax_form_type` — query `taxFormType` · `form_id` — query `formId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_partner_id` — header `WM_PARTNER_ID` · `wm_tenant_id` — header `WM.TENANT_ID`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DownloadTaxFormErrorBody]`
- **Error**: `DownloadTaxFormErrorBody` — **Case A (typed)**
- **Error arms**: `V1SettingsDownloadtaxformprofile400Error1` [400] · `V1SettingsDownloadtaxformprofile404Error1` [404] · `V1SettingsDownloadtaxformprofile500Error1` [500] · `V1SettingsDownloadtaxformprofile502Error1` [502] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `DownloadTaxFormErrorBody` | `walmart_apis/errors/download_tax_form_error.py` |
| `V1SettingsDownloadtaxformprofile400Error1` | `walmart_apis/models/v1_settings_downloadtaxformprofile400_error1.py` |
| `V1SettingsDownloadtaxformprofile404Error1` | `walmart_apis/models/v1_settings_downloadtaxformprofile404_error1.py` |
| `V1SettingsDownloadtaxformprofile500Error1` | `walmart_apis/models/v1_settings_downloadtaxformprofile500_error1.py` |
| `V1SettingsDownloadtaxformprofile502Error1` | `walmart_apis/models/v1_settings_downloadtaxformprofile502_error1.py` |

### client.tax_form_apis.get_tax_forms

- **Route**: `GET /v1/settings/gettaxformprofile`
- **Auth**: `access_token`
- **Signature**: `def get_tax_forms(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_global_version: WmGlobalVersionOrStr, wm_market: str, wm_partner_id: str, wm_tenant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_global_version`, `wm_market`, `wm_partner_id`, `wm_tenant_id`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_market` — header `WM_MARKET` · `wm_partner_id` — header `WM_PARTNER_ID` · `wm_tenant_id` — header `WM.TENANT_ID`
- **Returns (parsed)**: `V1SettingsGettaxformprofileResponse`
- **Returns (raw)**: `ApiResult[V1SettingsGettaxformprofileResponse, GetTaxFormsErrorBody]`
- **Error**: `GetTaxFormsErrorBody` — **Case A (typed)**
- **Error arms**: `V1SettingsGettaxformprofile400Error1` [400] · `V1SettingsGettaxformprofile404Error1` [404] · `V1SettingsGettaxformprofile500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V1SettingsGettaxformprofileResponse` | `walmart_apis/models/v1_settings_gettaxformprofile_response.py` |
| `GetTaxFormsErrorBody` | `walmart_apis/errors/get_tax_forms_error.py` |
| `V1SettingsGettaxformprofile400Error1` | `walmart_apis/models/v1_settings_gettaxformprofile400_error1.py` |
| `V1SettingsGettaxformprofile404Error1` | `walmart_apis/models/v1_settings_gettaxformprofile404_error1.py` |
| `V1SettingsGettaxformprofile500Error1` | `walmart_apis/models/v1_settings_gettaxformprofile500_error1.py` |

