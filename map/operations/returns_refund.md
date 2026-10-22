<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReturnsRefund — operations

Accessor: `client.returns_refund` · Source: `walmart_apis/apis/returns_refund.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.returns_refund.get_returns

- **Route**: `GET /v3/returns`
- **Auth**: `access_token`
- **Signature**: `def get_returns(query_params: QueryParams | QueryParamsDict, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query_params`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `query_params` — query `Query Params` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `ReturnOrderResponse`
- **Returns (raw)**: `ApiResult[ReturnOrderResponse, GetReturnsErrorBody]`
- **Error**: `GetReturnsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse3` [400] · `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `ErrorResponses` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `QueryParams` | `walmart_apis/models/query_params.py` |
| `QueryParamsDict` | `walmart_apis/models/query_params.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `ReturnOrderResponse` | `walmart_apis/models/return_order_response.py` |
| `GetReturnsErrorBody` | `walmart_apis/errors/get_returns_error.py` |
| `ErrorResponse3` | `walmart_apis/models/error_response3.py` |
| `Unauthorized1` | `walmart_apis/models/unauthorized1.py` |
| `Forbidden1` | `walmart_apis/models/forbidden1.py` |
| `TooManyRequests1` | `walmart_apis/models/too_many_requests1.py` |
| `ErrorResponses` | `walmart_apis/models/error_responses.py` |

### client.returns_refund.refund_request

- **Route**: `POST /v3/returns/{returnOrderId}/refund`
- **Auth**: `access_token`
- **Signature**: `def refund_request(return_order_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket3OrStr, wm_global_version: WmGlobalVersionOrStr, body: RefundRequest | RefundRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `return_order_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `return_order_id` — path `returnOrderId` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `Request`
- **Returns (raw)**: `ApiResult[Request, RefundRequestErrorBody]`
- **Error**: `RefundRequestErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse3` [400] · `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `ErrorResponses` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket3OrStr` | `walmart_apis/models/enums/wm_market3.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `RefundRequest` | `walmart_apis/models/refund_request.py` |
| `RefundRequestDict` | `walmart_apis/models/refund_request.py` |
| `Request` | `walmart_apis/models/request.py` |
| `RefundRequestErrorBody` | `walmart_apis/errors/refund_request_error.py` |
| `ErrorResponse3` | `walmart_apis/models/error_response3.py` |
| `Unauthorized1` | `walmart_apis/models/unauthorized1.py` |
| `Forbidden1` | `walmart_apis/models/forbidden1.py` |
| `TooManyRequests1` | `walmart_apis/models/too_many_requests1.py` |
| `ErrorResponses` | `walmart_apis/models/error_responses.py` |

### client.returns_refund.return_order_cursor

- **Route**: `GET /v3/returns/cursor`
- **Auth**: `access_token`
- **Signature**: `def return_order_cursor(query_params: QueryParamsMx | QueryParamsMxDict, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket21OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query_params`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `query_params` — query `Query Params` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `ReturnOrdersResponses`
- **Returns (raw)**: `ApiResult[ReturnOrdersResponses, ReturnOrderCursorErrorBody]`
- **Error**: `ReturnOrderCursorErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse3` [400] · `Unauthorized1` [401] · `Forbidden1` [403] · `TooManyRequests1` [429] · `ErrorResponses` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `QueryParamsMx` | `walmart_apis/models/query_params_mx.py` |
| `QueryParamsMxDict` | `walmart_apis/models/query_params_mx.py` |
| `WmMarket21OrStr` | `walmart_apis/models/enums/wm_market21.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `ReturnOrdersResponses` | `walmart_apis/models/return_orders_responses.py` |
| `ReturnOrderCursorErrorBody` | `walmart_apis/errors/return_order_cursor_error.py` |
| `ErrorResponse3` | `walmart_apis/models/error_response3.py` |
| `Unauthorized1` | `walmart_apis/models/unauthorized1.py` |
| `Forbidden1` | `walmart_apis/models/forbidden1.py` |
| `TooManyRequests1` | `walmart_apis/models/too_many_requests1.py` |
| `ErrorResponses` | `walmart_apis/models/error_responses.py` |

