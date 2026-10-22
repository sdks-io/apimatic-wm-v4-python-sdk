<!-- Generated file — do not edit; regenerated with the SDK. -->

# Promotions — operations

Accessor: `client.promotions` · Source: `walmart_apis/apis/promotions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.promotions.get_promotional_prices

- **Route**: `GET /v3/promo/sku/{sku}`
- **Signature**: `def get_promotional_prices(sku: str, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `sku` — path · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3PromoSkuResponse`
- **Returns (raw)**: `ApiResult[V3PromoSkuResponse, GetPromotionalPricesErrorBody]`
- **Error**: `GetPromotionalPricesErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token500Error1` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3PromoSkuResponse` | `walmart_apis/models/v3_promo_sku_response.py` |
| `GetPromotionalPricesErrorBody` | `walmart_apis/errors/get_promotional_prices_error.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

### client.promotions.price_bulk_uploads

- **Route**: `POST /v3/feeds?feedType=PRICE_AND_PROMOTION`
- **Signature**: `def price_bulk_uploads(feed_type: FeedType21OrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, body: V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `feed_type` — query `feedType` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId1`
- **Returns (raw)**: `ApiResult[FeedId1, PriceBulkUploadsErrorBody]`
- **Error**: `PriceBulkUploadsErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token500Error1` [401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedType21OrStr` | `walmart_apis/models/enums/feed_type21.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsFeedTypePriceAndPromotionRequest1` | `walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request1.py` |
| `V3FeedsFeedTypePriceAndPromotionRequest1Dict` | `walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request1.py` |
| `FeedId1` | `walmart_apis/models/feed_id1.py` |
| `PriceBulkUploadsErrorBody` | `walmart_apis/errors/price_bulk_uploads_error.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

### client.promotions.update_promotional_prices

- **Route**: `POST /v3/price`
- **Signature**: `def update_promotional_prices(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3PriceRequest | V3PriceRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3PriceResponse`
- **Returns (raw)**: `ApiResult[V3PriceResponse, UpdatePromotionalPricesErrorBody]`
- **Error**: `UpdatePromotionalPricesErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token500Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3PriceRequest` | `walmart_apis/models/v3_price_request.py` |
| `V3PriceRequestDict` | `walmart_apis/models/v3_price_request.py` |
| `V3PriceResponse` | `walmart_apis/models/v3_price_response.py` |
| `UpdatePromotionalPricesErrorBody` | `walmart_apis/errors/update_promotional_prices_error.py` |
| `V3Token500Error1` | `walmart_apis/models/v3_token500_error1.py` |

