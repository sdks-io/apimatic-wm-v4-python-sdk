<!-- Generated file — do not edit; regenerated with the SDK. -->

# Prices — operations

Accessor: `client.prices` · Source: `walmart_apis/apis/prices.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.prices.create_strategy

- **Route**: `POST /v3/repricer/strategy`
- **Auth**: `access_token`
- **Signature**: `def create_strategy(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3RepricerStrategyRequest1 | V3RepricerStrategyRequest1Dict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3RepricerStrategyResponse2`
- **Returns (raw)**: `ApiResult[V3RepricerStrategyResponse2, CreateStrategyErrorBody]`
- **Error**: `CreateStrategyErrorBody` — **Case A (typed)**
- **Error arms**: `V3RepricerStrategy400Error1` [400] · `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3RepricerStrategyRequest1` | `walmart_apis/models/v3_repricer_strategy_request1.py` |
| `V3RepricerStrategyRequest1Dict` | `walmart_apis/models/v3_repricer_strategy_request1.py` |
| `V3RepricerStrategyResponse2` | `walmart_apis/models/v3_repricer_strategy_response2.py` |
| `CreateStrategyErrorBody` | `walmart_apis/errors/create_strategy_error.py` |
| `V3RepricerStrategy400Error1` | `walmart_apis/models/v3_repricer_strategy400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.delete_strategy

- **Route**: `DELETE /v3/repricer/strategy/{strategyCollectionId}`
- **Auth**: `access_token`
- **Signature**: `def delete_strategy(strategy_collection_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `strategy_collection_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `strategy_collection_id` — path `strategyCollectionId` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `RejectRecommendationsResponsePayload`
- **Returns (raw)**: `ApiResult[RejectRecommendationsResponsePayload, DeleteStrategyErrorBody]`
- **Error**: `DeleteStrategyErrorBody` — **Case A (typed)**
- **Error arms**: `V3RepricerStrategy400Error1` [400] · `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `RejectRecommendationsResponsePayload` | `walmart_apis/models/reject_recommendations_response_payload.py` |
| `DeleteStrategyErrorBody` | `walmart_apis/errors/delete_strategy_error.py` |
| `V3RepricerStrategy400Error1` | `walmart_apis/models/v3_repricer_strategy400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.get_all_incentives

- **Route**: `GET /v3/price/incentives`
- **Auth**: `access_token`
- **Signature**: `def get_all_incentives(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, incentive_status: IncentiveStatusOrStr = IncentiveStatus.ELIGIBLE, limit: int | None = 25, offset: int | None = 0, sort_by: SortBy1OrStr | None = SortBy1.EXPIRATION_DATE, sort_order: OrderOrStr | None = Order.DESC, incentive_type: IncentiveTypeOrStr | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `incentive_status` — query `incentiveStatus` · `limit` — query · `offset` — query · `sort_by` — query `sortBy` · `sort_order` — query `sortOrder` · `incentive_type` — query `incentiveType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3PriceIncentivesResponse`
- **Returns (raw)**: `ApiResult[V3PriceIncentivesResponse, GetAllIncentivesErrorBody]`
- **Error**: `GetAllIncentivesErrorBody` — **Case A (typed)**
- **Error arms**: `V3PriceIncentives400Error1` [400] · `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `IncentiveStatusOrStr` | `walmart_apis/models/enums/incentive_status.py` |
| `SortBy1OrStr` | `walmart_apis/models/enums/sort_by1.py` |
| `OrderOrStr` | `walmart_apis/models/enums/order.py` |
| `IncentiveTypeOrStr` | `walmart_apis/models/enums/incentive_type.py` |
| `V3PriceIncentivesResponse` | `walmart_apis/models/v3_price_incentives_response.py` |
| `GetAllIncentivesErrorBody` | `walmart_apis/errors/get_all_incentives_error.py` |
| `V3PriceIncentives400Error1` | `walmart_apis/models/v3_price_incentives400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.get_repricer_feed

- **Route**: `POST /v3/repricerFeeds`
- **Auth**: `access_token`
- **Signature**: `def get_repricer_feed(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3RepricerFeedsRequest | V3RepricerFeedsRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId1`
- **Returns (raw)**: `ApiResult[FeedId1, GetRepricerFeedErrorBody]`
- **Error**: `GetRepricerFeedErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3RepricerFeedsRequest` | `walmart_apis/models/v3_repricer_feeds_request.py` |
| `V3RepricerFeedsRequestDict` | `walmart_apis/models/v3_repricer_feeds_request.py` |
| `FeedId1` | `walmart_apis/models/feed_id1.py` |
| `GetRepricerFeedErrorBody` | `walmart_apis/errors/get_repricer_feed_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.get_strategies

- **Route**: `GET /v3/repricer/strategies`
- **Auth**: `access_token`
- **Signature**: `def get_strategies(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, offset: str | None = "0", limit: str | None = "10", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `offset` — query · `limit` — query · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3RepricerStrategiesResponse`
- **Returns (raw)**: `ApiResult[V3RepricerStrategiesResponse, GetStrategiesErrorBody]`
- **Error**: `GetStrategiesErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3RepricerStrategiesResponse` | `walmart_apis/models/v3_repricer_strategies_response.py` |
| `GetStrategiesErrorBody` | `walmart_apis/errors/get_strategies_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.price_and_promotion_bulk_uploads

- **Route**: `POST /v3/feeds?feedType=PRICE_AND_PROMOTION`
- **Auth**: `access_token`
- **Signature**: `def price_and_promotion_bulk_uploads(feed_type: FeedType21OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsFeedTypePriceAndPromotionRequest | V3FeedsFeedTypePriceAndPromotionRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `feed_type` — query `feedType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId`
- **Returns (raw)**: `ApiResult[FeedId, PriceAndPromotionBulkUploadsErrorBody]`
- **Error**: `PriceAndPromotionBulkUploadsErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedType21OrStr` | `walmart_apis/models/enums/feed_type21.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsFeedTypePriceAndPromotionRequest` | `walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request.py` |
| `V3FeedsFeedTypePriceAndPromotionRequestDict` | `walmart_apis/models/v3_feeds_feed_type_price_and_promotion_request.py` |
| `FeedId` | `walmart_apis/models/feed_id.py` |
| `PriceAndPromotionBulkUploadsErrorBody` | `walmart_apis/errors/price_and_promotion_bulk_uploads_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.reduced_referral_fee_incentives_enrollment

- **Route**: `POST /v3/feeds?feedType=INCENTIVE_ENROLLMENT`
- **Auth**: `access_token`
- **Signature**: `def reduced_referral_fee_incentives_enrollment(feed_type: FeedType11OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsFeedTypeIncentiveEnrollmentRequest | V3FeedsFeedTypeIncentiveEnrollmentRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `feed_type` — query `feedType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3FeedsFeedTypeIncentiveEnrollmentResponse`
- **Returns (raw)**: `ApiResult[V3FeedsFeedTypeIncentiveEnrollmentResponse, ReducedReferralFeeIncentivesEnrollmentErrorBody]`
- **Error**: `ReducedReferralFeeIncentivesEnrollmentErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedType11OrStr` | `walmart_apis/models/enums/feed_type11.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsFeedTypeIncentiveEnrollmentRequest` | `walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_request.py` |
| `V3FeedsFeedTypeIncentiveEnrollmentRequestDict` | `walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_request.py` |
| `V3FeedsFeedTypeIncentiveEnrollmentResponse` | `walmart_apis/models/v3_feeds_feed_type_incentive_enrollment_response.py` |
| `ReducedReferralFeeIncentivesEnrollmentErrorBody` | `walmart_apis/errors/reduced_referral_fee_incentives_enrollment_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.update_price

- **Route**: `POST /v3/price`
- **Auth**: `access_token`
- **Signature**: `def update_price(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3PriceRequest | V3PriceRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3PriceResponse`
- **Returns (raw)**: `ApiResult[V3PriceResponse, UpdatePriceErrorBody]`
- **Error**: `UpdatePriceErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3PriceRequest` | `walmart_apis/models/v3_price_request.py` |
| `V3PriceRequestDict` | `walmart_apis/models/v3_price_request.py` |
| `V3PriceResponse` | `walmart_apis/models/v3_price_response.py` |
| `UpdatePriceErrorBody` | `walmart_apis/errors/update_price_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.update_strategy

- **Route**: `PUT /v3/repricer/strategy/{strategyCollectionId}`
- **Auth**: `access_token`
- **Signature**: `def update_strategy(strategy_collection_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3RepricerStrategyRequest | V3RepricerStrategyRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `strategy_collection_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `strategy_collection_id` — path `strategyCollectionId` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3RepricerStrategyResponse`
- **Returns (raw)**: `ApiResult[V3RepricerStrategyResponse, UpdateStrategyErrorBody]`
- **Error**: `UpdateStrategyErrorBody` — **Case A (typed)**
- **Error arms**: `V3RepricerStrategy400Error1` [400] · `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3RepricerStrategyRequest` | `walmart_apis/models/v3_repricer_strategy_request.py` |
| `V3RepricerStrategyRequestDict` | `walmart_apis/models/v3_repricer_strategy_request.py` |
| `V3RepricerStrategyResponse` | `walmart_apis/models/v3_repricer_strategy_response.py` |
| `UpdateStrategyErrorBody` | `walmart_apis/errors/update_strategy_error.py` |
| `V3RepricerStrategy400Error1` | `walmart_apis/models/v3_repricer_strategy400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.update_walmart_funded_incentives_enrollment_status

- **Route**: `PUT /v3/price/incentives/wfpreference`
- **Auth**: `access_token`
- **Signature**: `def update_walmart_funded_incentives_enrollment_status(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, auto_enroll_enabled: bool = True, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `auto_enroll_enabled` — query `autoEnrollEnabled` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3PriceIncentivesWfpreferenceResponse`
- **Returns (raw)**: `ApiResult[V3PriceIncentivesWfpreferenceResponse, UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody]`
- **Error**: `UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3PriceIncentivesWfpreferenceResponse` | `walmart_apis/models/v3_price_incentives_wfpreference_response.py` |
| `UpdateWalmartFundedIncentivesEnrollmentStatusErrorBody` | `walmart_apis/errors/update_walmart_funded_incentives_enrollment_status_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

### client.prices.walmart_funded_incentives_enrollment

- **Route**: `POST /v3/feeds?feedType=WALMART_FUNDED_INCENTIVES_ENROLLMENT`
- **Auth**: `access_token`
- **Signature**: `def walmart_funded_incentives_enrollment(feed_type: FeedType2OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest | V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `feed_type` — query `feedType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId`
- **Returns (raw)**: `ApiResult[FeedId, WalmartFundedIncentivesEnrollmentErrorBody]`
- **Error**: `WalmartFundedIncentivesEnrollmentErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [403, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedType2OrStr` | `walmart_apis/models/enums/feed_type2.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequest` | `walmart_apis/models/v3_feeds_feed_type_walmart_funded_incentives_enrollment_request.py` |
| `V3FeedsFeedTypeWalmartFundedIncentivesEnrollmentRequestDict` | `walmart_apis/models/v3_feeds_feed_type_walmart_funded_incentives_enrollment_request.py` |
| `FeedId` | `walmart_apis/models/feed_id.py` |
| `WalmartFundedIncentivesEnrollmentErrorBody` | `walmart_apis/errors/walmart_funded_incentives_enrollment_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |

