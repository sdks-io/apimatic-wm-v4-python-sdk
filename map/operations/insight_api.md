<!-- Generated file — do not edit; regenerated with the SDK. -->

# InsightApi — operations

Accessor: `client.insight_api` · Source: `walmart_apis/apis/insight_api.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.insight_api.get_categories_list

- **Route**: `GET /v3/insights/items/listingQuality/count`
- **Auth**: `access_token`
- **Signature**: `def get_categories_list(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, view_trending_items: bool | None = True, wfs_flag: bool | None = None, has_issue: int | None = 0, type_: Type3OrStr | None = None, in_demand_indicator: bool | None = None, limit: int | None = None, offset: int | None = 0, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `view_trending_items` — query `viewTrendingItems` · `wfs_flag` — query `wfsFlag` · `has_issue` — query `hasIssue` · `type_` — query `type` · `in_demand_indicator` — query `inDemandIndicator` · `limit` — query · `offset` — query · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3InsightsItemsListingQualityCountResponse`
- **Returns (raw)**: `ApiResult[V3InsightsItemsListingQualityCountResponse, GetCategoriesListErrorBody]`
- **Error**: `GetCategoriesListErrorBody` — **Case A (typed)**
- **Error arms**: `V3InsightsItemsListingQualityCount400Error1` [400] · `V3Token400Error1` [401, 403] · `V3InsightsItemsListingQualityCount500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `Type3OrStr` | `walmart_apis/models/enums/type3.py` |
| `V3InsightsItemsListingQualityCountResponse` | `walmart_apis/models/v3_insights_items_listing_quality_count_response.py` |
| `GetCategoriesListErrorBody` | `walmart_apis/errors/get_categories_list_error.py` |
| `V3InsightsItemsListingQualityCount400Error1` | `walmart_apis/models/v3_insights_items_listing_quality_count400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsItemsListingQualityCount500Error1` | `walmart_apis/models/v3_insights_items_listing_quality_count500_error1.py` |

### client.insight_api.get_listing_quality_score

- **Route**: `GET /v3/insights/items/listingQuality/score`
- **Auth**: `access_token`
- **Signature**: `def get_listing_quality_score(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, view_trending_items: bool | None = None, wfs_flag: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `view_trending_items` — query `viewTrendingItems` · `wfs_flag` — query `wfsFlag` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3InsightsItemsListingQualityScoreResponse`
- **Returns (raw)**: `ApiResult[V3InsightsItemsListingQualityScoreResponse, GetListingQualityScoreErrorBody]`
- **Error**: `GetListingQualityScoreErrorBody` — **Case A (typed)**
- **Error arms**: `V3InsightsItemsListingQualityScore400Error1` [400] · `V3Token400Error1` [401, 403] · `V3InsightsItemsListingQualityScore500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3InsightsItemsListingQualityScoreResponse` | `walmart_apis/models/v3_insights_items_listing_quality_score_response.py` |
| `GetListingQualityScoreErrorBody` | `walmart_apis/errors/get_listing_quality_score_error.py` |
| `V3InsightsItemsListingQualityScore400Error1` | `walmart_apis/models/v3_insights_items_listing_quality_score400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsItemsListingQualityScore500Error1` | `walmart_apis/models/v3_insights_items_listing_quality_score500_error1.py` |

### client.insight_api.get_pro_seller_badge_info

- **Route**: `GET /v3/insights/prosellerbadge`
- **Auth**: `access_token`
- **Signature**: `def get_pro_seller_badge_info(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3InsightsProsellerbadgeResponse`
- **Returns (raw)**: `ApiResult[V3InsightsProsellerbadgeResponse, GetProSellerBadgeInfoErrorBody]`
- **Error**: `GetProSellerBadgeInfoErrorBody` — **Case A (typed)**
- **Error arms**: `V3InsightsProsellerbadge400Error1` [400] · `V3Token400Error1` [401, 403] · `V3InsightsProsellerbadge500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3InsightsProsellerbadgeResponse` | `walmart_apis/models/v3_insights_prosellerbadge_response.py` |
| `GetProSellerBadgeInfoErrorBody` | `walmart_apis/errors/get_pro_seller_badge_info_error.py` |
| `V3InsightsProsellerbadge400Error1` | `walmart_apis/models/v3_insights_prosellerbadge400_error1.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsProsellerbadge500Error1` | `walmart_apis/models/v3_insights_prosellerbadge500_error1.py` |

### client.insight_api.get_seller_incentives_info

- **Route**: `GET /v3/insights/sellerIncentives`
- **Auth**: `access_token`
- **Signature**: `def get_seller_incentives_info(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3InsightsSellerIncentivesResponse`
- **Returns (raw)**: `ApiResult[V3InsightsSellerIncentivesResponse, GetSellerIncentivesInfoErrorBody]`
- **Error**: `GetSellerIncentivesInfoErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [401, 403] · `V3InsightsSellerIncentives500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3InsightsSellerIncentivesResponse` | `walmart_apis/models/v3_insights_seller_incentives_response.py` |
| `GetSellerIncentivesInfoErrorBody` | `walmart_apis/errors/get_seller_incentives_info_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsSellerIncentives500Error1` | `walmart_apis/models/v3_insights_seller_incentives500_error1.py` |

### client.insight_api.get_unpublished_item_count

- **Route**: `GET /v3/insights/items/unpublished/counts`
- **Auth**: `access_token`
- **Signature**: `def get_unpublished_item_count(from_date: str, wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_date`, `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `from_date` — query `fromDate` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3InsightsItemsUnpublishedCountsResponse`
- **Returns (raw)**: `ApiResult[V3InsightsItemsUnpublishedCountsResponse, GetUnpublishedItemCountErrorBody]`
- **Error**: `GetUnpublishedItemCountErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [401, 403] · `V3InsightsItemsUnpublishedCounts500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3InsightsItemsUnpublishedCountsResponse` | `walmart_apis/models/v3_insights_items_unpublished_counts_response.py` |
| `GetUnpublishedItemCountErrorBody` | `walmart_apis/errors/get_unpublished_item_count_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsItemsUnpublishedCounts500Error1` | `walmart_apis/models/v3_insights_items_unpublished_counts500_error1.py` |

### client.insight_api.get_unpublished_items

- **Route**: `GET /v3/insights/items/unpublished/items`
- **Auth**: `access_token`
- **Signature**: `def get_unpublished_items(from_date: str, wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, *, unpublished_reason_code: str | None = "all", limit: str | None = "20", offer_lifecycle_status: str | None = "all", market_trending: str | None = "true", items_with_inventory: str | None = "true", is_customer_favorite: bool | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_date`, `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`
- **Params**: `from_date` — query `fromDate` · `unpublished_reason_code` — query `unpublishedReasonCode` · `limit` — query · `offer_lifecycle_status` — query `offerLifecycleStatus` · `market_trending` — query `marketTrending` · `items_with_inventory` — query `itemsWithInventory` · `is_customer_favorite` — query `isCustomerFavorite` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3InsightsItemsUnpublishedItemsResponse`
- **Returns (raw)**: `ApiResult[V3InsightsItemsUnpublishedItemsResponse, GetUnpublishedItemsErrorBody]`
- **Error**: `GetUnpublishedItemsErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [400, 401, 403] · `V3InsightsItemsUnpublishedItems500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3InsightsItemsUnpublishedItemsResponse` | `walmart_apis/models/v3_insights_items_unpublished_items_response.py` |
| `GetUnpublishedItemsErrorBody` | `walmart_apis/errors/get_unpublished_items_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsItemsUnpublishedItems500Error1` | `walmart_apis/models/v3_insights_items_unpublished_items500_error1.py` |

### client.insight_api.items_details_for_listing

- **Route**: `POST /v3/insights/items/listingQuality/items`
- **Auth**: `access_token`
- **Signature**: `def items_details_for_listing(wm_global_version: WmGlobalVersionOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3InsightsItemsListingQualityItemsRequest | V3InsightsItemsListingQualityItemsRequestDict, *, limit: str | None = "200", next_cursor: str | None = None, offset: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `body`
- **Params**: `limit` — query · `next_cursor` — query `nextCursor` · `offset` — query · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3InsightsItemsListingQualityItemsResponse`
- **Returns (raw)**: `ApiResult[V3InsightsItemsListingQualityItemsResponse, ItemsDetailsForListingErrorBody]`
- **Error**: `ItemsDetailsForListingErrorBody` — **Case A (typed)**
- **Error arms**: `V3Token400Error1` [401, 403] · `V3InsightsItemsListingQualityItems500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3InsightsItemsListingQualityItemsRequest` | `walmart_apis/models/v3_insights_items_listing_quality_items_request.py` |
| `V3InsightsItemsListingQualityItemsRequestDict` | `walmart_apis/models/v3_insights_items_listing_quality_items_request.py` |
| `V3InsightsItemsListingQualityItemsResponse` | `walmart_apis/models/v3_insights_items_listing_quality_items_response.py` |
| `ItemsDetailsForListingErrorBody` | `walmart_apis/errors/items_details_for_listing_error.py` |
| `V3Token400Error1` | `walmart_apis/models/v3_token400_error1.py` |
| `V3InsightsItemsListingQualityItems500Error1` | `walmart_apis/models/v3_insights_items_listing_quality_items500_error1.py` |

