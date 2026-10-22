<!-- Generated file — do not edit; regenerated with the SDK. -->

# ShipWithWalmart — operations

Accessor: `client.ship_with_walmart` · Source: `walmart_apis/apis/ship_with_walmart.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.ship_with_walmart.create_label

- **Route**: `POST /v3/shipping/labels`
- **Auth**: `access_token`
- **Signature**: `def create_label(accept: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ShippingLabelsRequest | V3ShippingLabelsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `accept`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `accept` — header `Accept` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3ShippingLabelsResponse`
- **Returns (raw)**: `ApiResult[V3ShippingLabelsResponse, CreateLabelErrorBody]`
- **Error**: `CreateLabelErrorBody` — **Case A (typed)**
- **Error arms**: `V3ShippingLabels500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingLabelsRequest` | `walmart_apis/models/v3_shipping_labels_request.py` |
| `V3ShippingLabelsRequestDict` | `walmart_apis/models/v3_shipping_labels_request.py` |
| `V3ShippingLabelsResponse` | `walmart_apis/models/v3_shipping_labels_response.py` |
| `CreateLabelErrorBody` | `walmart_apis/errors/create_label_error.py` |
| `V3ShippingLabels500Error1` | `walmart_apis/models/v3_shipping_labels500_error1.py` |

### client.ship_with_walmart.create_label_mps

- **Route**: `POST /v3/shipping/multi-package/labels`
- **Auth**: `access_token`
- **Signature**: `def create_label_mps(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, body: V3ShippingMultiPackageLabelsRequest | V3ShippingMultiPackageLabelsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3ShippingMultiPackageLabelsResponse`
- **Returns (raw)**: `ApiResult[V3ShippingMultiPackageLabelsResponse, CreateLabelMpsErrorBody]`
- **Error**: `CreateLabelMpsErrorBody` — **Case A (typed)**
- **Error arms**: `list[Error5]` [400] · `V3ShippingMultiPackageLabels500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket11OrStr` | `walmart_apis/models/enums/wm_market11.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingMultiPackageLabelsRequest` | `walmart_apis/models/v3_shipping_multi_package_labels_request.py` |
| `V3ShippingMultiPackageLabelsRequestDict` | `walmart_apis/models/v3_shipping_multi_package_labels_request.py` |
| `V3ShippingMultiPackageLabelsResponse` | `walmart_apis/models/v3_shipping_multi_package_labels_response.py` |
| `CreateLabelMpsErrorBody` | `walmart_apis/errors/create_label_mps_error.py` |
| `Error5` | `walmart_apis/models/error5.py` |
| `V3ShippingMultiPackageLabels500Error1` | `walmart_apis/models/v3_shipping_multi_package_labels500_error1.py` |

### client.ship_with_walmart.discard_label

- **Route**: `DELETE /v3/shipping/labels/carriers/{carrierShortName}/trackings/{trackingNo}`
- **Auth**: `access_token`
- **Signature**: `def discard_label(carrier_short_name: str, tracking_no: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket6OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `carrier_short_name`, `tracking_no`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `carrier_short_name` — path `carrierShortName` · `tracking_no` — path `trackingNo` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3ShippingLabelsCarriersTrackingsResponse`
- **Returns (raw)**: `ApiResult[V3ShippingLabelsCarriersTrackingsResponse, DiscardLabelErrorBody]`
- **Error**: `DiscardLabelErrorBody` — **Case A (typed)**
- **Error arms**: `list[V3ShippingLabelsCarriersTrackings400Error1]` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket6OrStr` | `walmart_apis/models/enums/wm_market6.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingLabelsCarriersTrackingsResponse` | `walmart_apis/models/v3_shipping_labels_carriers_trackings_response.py` |
| `DiscardLabelErrorBody` | `walmart_apis/errors/discard_label_error.py` |
| `V3ShippingLabelsCarriersTrackings400Error1` | `walmart_apis/models/v3_shipping_labels_carriers_trackings400_error1.py` |

### client.ship_with_walmart.get_carrier_package_types

- **Route**: `GET /v3/shipping/labels/carriers/{carrierShortName}/package-types`
- **Auth**: `access_token`
- **Signature**: `def get_carrier_package_types(carrier_short_name: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `carrier_short_name`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `carrier_short_name` — path `carrierShortName` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3ShippingLabelsCarriersPackageTypesResponse`
- **Returns (raw)**: `ApiResult[V3ShippingLabelsCarriersPackageTypesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket11OrStr` | `walmart_apis/models/enums/wm_market11.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingLabelsCarriersPackageTypesResponse` | `walmart_apis/models/v3_shipping_labels_carriers_package_types_response.py` |

### client.ship_with_walmart.get_carriers

- **Route**: `GET /v3/shipping/labels/carriers`
- **Auth**: `access_token`
- **Signature**: `def get_carriers(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3ShippingLabelsCarriersResponse`
- **Returns (raw)**: `ApiResult[V3ShippingLabelsCarriersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket11OrStr` | `walmart_apis/models/enums/wm_market11.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingLabelsCarriersResponse` | `walmart_apis/models/v3_shipping_labels_carriers_response.py` |

### client.ship_with_walmart.get_label

- **Route**: `GET /v3/shipping/labels/purchase-orders/{purchaseOrderId}`
- **Auth**: `access_token`
- **Signature**: `def get_label(purchase_order_id: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3ShippingLabelsPurchaseOrdersResponse`
- **Returns (raw)**: `ApiResult[V3ShippingLabelsPurchaseOrdersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket11OrStr` | `walmart_apis/models/enums/wm_market11.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingLabelsPurchaseOrdersResponse` | `walmart_apis/models/v3_shipping_labels_purchase_orders_response.py` |

### client.ship_with_walmart.get_label_by_tracking_and_carrier

- **Route**: `GET /v3/shipping/labels/carriers/{carrierShortName}/trackings/{trackingNo}`
- **Auth**: `access_token`
- **Signature**: `def get_label_by_tracking_and_carrier(carrier_short_name: str, tracking_no: str, accept: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `carrier_short_name`, `tracking_no`, `accept`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `carrier_short_name` — path `carrierShortName` · `tracking_no` — path `trackingNo` · `accept` — header · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarket11OrStr` | `walmart_apis/models/enums/wm_market11.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |

### client.ship_with_walmart.get_scan_form_by_manifest_id

- **Route**: `GET /v3/shipping/scan-form`
- **Auth**: `access_token`
- **Signature**: `def get_scan_form_by_manifest_id(manifest_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarketOrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `manifest_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`
- **Params**: `manifest_id` — query `manifestId` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |

### client.ship_with_walmart.get_shipping_estimate

- **Route**: `POST /v3/shipping/labels/shipping-estimates`
- **Auth**: `access_token`
- **Signature**: `def get_shipping_estimate(accept: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket11OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ShippingLabelsShippingEstimatesRequest | V3ShippingLabelsShippingEstimatesRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `accept`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `accept` — header `Accept` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3ShippingLabelsShippingEstimatesResponse`
- **Returns (raw)**: `ApiResult[V3ShippingLabelsShippingEstimatesResponse, GetShippingEstimateErrorBody]`
- **Error**: `GetShippingEstimateErrorBody` — **Case A (typed)**
- **Error arms**: `list[V3ShippingLabelsShippingEstimates400Error1]` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket11OrStr` | `walmart_apis/models/enums/wm_market11.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingLabelsShippingEstimatesRequest` | `walmart_apis/models/v3_shipping_labels_shipping_estimates_request.py` |
| `V3ShippingLabelsShippingEstimatesRequestDict` | `walmart_apis/models/v3_shipping_labels_shipping_estimates_request.py` |
| `V3ShippingLabelsShippingEstimatesResponse` | `walmart_apis/models/v3_shipping_labels_shipping_estimates_response.py` |
| `GetShippingEstimateErrorBody` | `walmart_apis/errors/get_shipping_estimate_error.py` |
| `V3ShippingLabelsShippingEstimates400Error1` | `walmart_apis/models/v3_shipping_labels_shipping_estimates400_error1.py` |

### client.ship_with_walmart.scan_form

- **Route**: `POST /v3/shipping/scan-form`
- **Auth**: `access_token`
- **Signature**: `def scan_form(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarketOrStr, wm_global_version: WmGlobalVersionOrStr, accept: str, body: V3ShippingScanFormRequest | V3ShippingScanFormRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `accept`, `body`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `accept` — header `Accept` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3ShippingScanFormResponse`
- **Returns (raw)**: `ApiResult[V3ShippingScanFormResponse, ScanFormErrorBody]`
- **Error**: `ScanFormErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 409, anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ShippingScanFormRequest` | `walmart_apis/models/v3_shipping_scan_form_request.py` |
| `V3ShippingScanFormRequestDict` | `walmart_apis/models/v3_shipping_scan_form_request.py` |
| `V3ShippingScanFormResponse` | `walmart_apis/models/v3_shipping_scan_form_response.py` |
| `ScanFormErrorBody` | `walmart_apis/errors/scan_form_error.py` |

