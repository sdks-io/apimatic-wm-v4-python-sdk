<!-- Generated file — do not edit; regenerated with the SDK. -->

# SimplifiedShippingSettings — operations

Accessor: `client.simplified_shipping_settings` · Source: `walmart_apis/apis/simplified_shipping_settings.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.simplified_shipping_settings.bulk_migrate_offers_for_simplified_shipping_settings

- **Route**: `POST /v3/feeds`
- **Signature**: `def bulk_migrate_offers_for_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsRequest1 | V3FeedsRequest1Dict, *, feed_type: str = "PROGRAM_ACTIONS", request_type: str = "SHIPPING_CONFIG", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `feed_type` — query `feedType` · `request_type` — query `requestType` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId1`
- **Returns (raw)**: `ApiResult[FeedId1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsRequest1` | `walmart_apis/models/v3_feeds_request1.py` |
| `V3FeedsRequest1Dict` | `walmart_apis/models/v3_feeds_request1.py` |
| `FeedId1` | `walmart_apis/models/feed_id1.py` |

### client.simplified_shipping_settings.create_simplified_shipping_settings

- **Route**: `POST /v3/settings/shipping/simplifiedshippingsettings/account`
- **Signature**: `def create_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3SettingsShippingSimplifiedshippingsettingsAccountRequest1 | V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1]`
- **Returns (raw)**: `ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse1], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3SettingsShippingSimplifiedshippingsettingsAccountRequest1` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request1.py` |
| `V3SettingsShippingSimplifiedshippingsettingsAccountRequest1Dict` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request1.py` |
| `V3SettingsShippingSimplifiedshippingsettingsAccountResponse1` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_response1.py` |

### client.simplified_shipping_settings.get_simplified_shipping_settings

- **Route**: `GET /v3/settings/shipping/simplifiedshippingsettings`
- **Signature**: `def get_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `list[V3SettingsShippingSimplifiedshippingsettingsResponse]`
- **Returns (raw)**: `ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3SettingsShippingSimplifiedshippingsettingsResponse` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_response.py` |

### client.simplified_shipping_settings.update_fc_level_simplified_shipping_settings

- **Route**: `PUT /v3/settings/shipping/simplifiedshippingsettings/fulfillmentcenter`
- **Signature**: `def update_fc_level_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest | V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse]`
- **Returns (raw)**: `ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequest` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_request.py` |
| `V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterRequestDict` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_request.py` |
| `V3SettingsShippingSimplifiedshippingsettingsFulfillmentcenterResponse` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_fulfillmentcenter_response.py` |

### client.simplified_shipping_settings.update_simplified_shipping_settings

- **Route**: `PUT /v3/settings/shipping/simplifiedshippingsettings/account`
- **Signature**: `def update_simplified_shipping_settings(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3SettingsShippingSimplifiedshippingsettingsAccountRequest | V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse]`
- **Returns (raw)**: `ApiResult[list[V3SettingsShippingSimplifiedshippingsettingsAccountResponse], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3SettingsShippingSimplifiedshippingsettingsAccountRequest` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request.py` |
| `V3SettingsShippingSimplifiedshippingsettingsAccountRequestDict` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_request.py` |
| `V3SettingsShippingSimplifiedshippingsettingsAccountResponse` | `walmart_apis/models/v3_settings_shipping_simplifiedshippingsettings_account_response.py` |

