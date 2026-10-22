<!-- Generated file — do not edit; regenerated with the SDK. -->

# LagTimeApi — operations

Accessor: `client.lag_time_api` · Source: `walmart_apis/apis/lag_time_api.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.lag_time_api.get_lag_time

- **Route**: `GET /v3/lagtime`
- **Auth**: `access_token`
- **Signature**: `def get_lag_time(sku: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `sku` — query · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `LagTimeResponse`
- **Returns (raw)**: `ApiResult[LagTimeResponse, GetLagTimeErrorBody]`
- **Error**: `GetLagTimeErrorBody` — **Case A (typed)**
- **Error arms**: `V3Lagtime400Error1` [400] · `V3Lagtime404Error1` [404] · `V3Lagtime500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `LagTimeResponse` | `walmart_apis/models/lag_time_response.py` |
| `GetLagTimeErrorBody` | `walmart_apis/errors/get_lag_time_error.py` |
| `V3Lagtime400Error1` | `walmart_apis/models/v3_lagtime400_error1.py` |
| `V3Lagtime404Error1` | `walmart_apis/models/v3_lagtime404_error1.py` |
| `V3Lagtime500Error1` | `walmart_apis/models/v3_lagtime500_error1.py` |

### client.lag_time_api.update_lag_time_bulk

- **Route**: `POST /v3/feeds`
- **Auth**: `access_token`
- **Signature**: `def update_lag_time_bulk(feed_type: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsRequest | V3FeedsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `feed_type` — query `feedType` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId1`
- **Returns (raw)**: `ApiResult[FeedId1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsRequest` | `walmart_apis/models/v3_feeds_request.py` |
| `V3FeedsRequestDict` | `walmart_apis/models/v3_feeds_request.py` |
| `FeedId1` | `walmart_apis/models/feed_id1.py` |

