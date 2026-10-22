<!-- Generated file — do not edit; regenerated with the SDK. -->

# Notifications — operations

Accessor: `client.notifications` · Source: `walmart_apis/apis/notifications.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.notifications.create_subscription

- **Route**: `POST /v3/webhooks/subscriptions`
- **Auth**: `access_token`
- **Signature**: `def create_subscription(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3WebhooksSubscriptionsRequest | V3WebhooksSubscriptionsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3WebhooksSubscriptionsResponse1`
- **Returns (raw)**: `ApiResult[V3WebhooksSubscriptionsResponse1, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket2OrStr` | `walmart_apis/models/enums/wm_market2.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3WebhooksSubscriptionsRequest` | `walmart_apis/models/v3_webhooks_subscriptions_request.py` |
| `V3WebhooksSubscriptionsRequestDict` | `walmart_apis/models/v3_webhooks_subscriptions_request.py` |
| `V3WebhooksSubscriptionsResponse1` | `walmart_apis/models/v3_webhooks_subscriptions_response1.py` |

### client.notifications.delete_subscription

- **Route**: `DELETE /v3/webhooks/subscriptions/{subscriptionId}`
- **Auth**: `access_token`
- **Signature**: `def delete_subscription(subscription_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `subscription_id` — path `subscriptionId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3WebhooksSubscriptionsResponse2`
- **Returns (raw)**: `ApiResult[V3WebhooksSubscriptionsResponse2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket2OrStr` | `walmart_apis/models/enums/wm_market2.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3WebhooksSubscriptionsResponse2` | `walmart_apis/models/v3_webhooks_subscriptions_response2.py` |

### client.notifications.get_all_subscriptions

- **Route**: `GET /v3/webhooks/subscriptions`
- **Auth**: `access_token`
- **Signature**: `def get_all_subscriptions(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, *, subscription_id: str | None = None, event_type: str | None = None, resource_name: str | None = None, status: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `subscription_id` — query `subscriptionId` · `event_type` — query `eventType` · `resource_name` — query `resourceName` · `status` — query · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3WebhooksSubscriptionsResponse`
- **Returns (raw)**: `ApiResult[V3WebhooksSubscriptionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket2OrStr` | `walmart_apis/models/enums/wm_market2.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3WebhooksSubscriptionsResponse` | `walmart_apis/models/v3_webhooks_subscriptions_response.py` |

### client.notifications.get_event_types

- **Route**: `GET /v3/webhooks/eventTypes`
- **Auth**: `access_token`
- **Signature**: `def get_event_types(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3WebhooksEventTypesResponse`
- **Returns (raw)**: `ApiResult[V3WebhooksEventTypesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket2OrStr` | `walmart_apis/models/enums/wm_market2.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3WebhooksEventTypesResponse` | `walmart_apis/models/v3_webhooks_event_types_response.py` |

### client.notifications.test_notification

- **Route**: `POST /v3/webhooks/test`
- **Auth**: `access_token`
- **Signature**: `def test_notification(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3WebhooksTestRequest | V3WebhooksTestRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `RejectRecommendationsResponsePayload`
- **Returns (raw)**: `ApiResult[RejectRecommendationsResponsePayload, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket2OrStr` | `walmart_apis/models/enums/wm_market2.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3WebhooksTestRequest` | `walmart_apis/models/v3_webhooks_test_request.py` |
| `V3WebhooksTestRequestDict` | `walmart_apis/models/v3_webhooks_test_request.py` |
| `RejectRecommendationsResponsePayload` | `walmart_apis/models/reject_recommendations_response_payload.py` |

### client.notifications.update_subscription

- **Route**: `PATCH /v3/webhooks/subscriptions/{subscriptionId}`
- **Auth**: `access_token`
- **Signature**: `def update_subscription(subscription_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket2OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3WebhooksSubscriptionsRequest1 | V3WebhooksSubscriptionsRequest1Dict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `subscription_id` — path `subscriptionId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3WebhooksSubscriptionsResponse3`
- **Returns (raw)**: `ApiResult[V3WebhooksSubscriptionsResponse3, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket2OrStr` | `walmart_apis/models/enums/wm_market2.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3WebhooksSubscriptionsRequest1` | `walmart_apis/models/v3_webhooks_subscriptions_request1.py` |
| `V3WebhooksSubscriptionsRequest1Dict` | `walmart_apis/models/v3_webhooks_subscriptions_request1.py` |
| `V3WebhooksSubscriptionsResponse3` | `walmart_apis/models/v3_webhooks_subscriptions_response3.py` |

