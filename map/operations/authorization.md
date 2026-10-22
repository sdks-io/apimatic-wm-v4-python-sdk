<!-- Generated file — do not edit; regenerated with the SDK. -->

# Authorization — operations

Accessor: `client.authorization` · Source: `walmart_apis/apis/authorization.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authorization.get_token_detail

- **Route**: `GET /v3/token/detail`
- **Signature**: `def get_token_detail(wm_sec_access_token: str, wm_market: str, content_type: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_market`, `content_type`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_market` — header `WM_MARKET` · `content_type` — header `Content-Type` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `TokenDetailResponse`
- **Returns (raw)**: `ApiResult[TokenDetailResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TokenDetailResponse` | `walmart_apis/models/token_detail_response.py` |

### client.authorization.token_api

- **Route**: `POST /v3/token`
- **Auth**: `basic_auth`
- **Signature**: `def token_api(wm_market: str, wm_qos_correlation_id: str, wm_svc_name: str, *, wm_partner_id: str | None = None, wm_consumer_channel_type: str | None = None, grant_type: GrantType1OrStr = GrantType1.CLIENT_CREDENTIALS, code: str | None = None, redirect_uri: str | None = None, refresh_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_market`, `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `wm_market` — header `WM_MARKET` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_partner_id` — header `WM_PARTNER.ID` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `grant_type` — form field · `code` — form field · `redirect_uri` — form field · `refresh_token` — form field
- **Returns (parsed)**: `OauthTokenModel`
- **Returns (raw)**: `ApiResult[OauthTokenModel, TokenApiErrorBody]`
- **Error**: `TokenApiErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [400] · `V3Token401Error1` [401] · `V3Token500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantType1OrStr` | `walmart_apis/models/enums/grant_type1.py` |
| `OauthTokenModel` | `walmart_apis/models/oauth_token_model.py` |
| `TokenApiErrorBody` | `walmart_apis/errors/token_api_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3Token401Error1` | `walmart_apis/models/v3_token401_error1.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

