<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reviews — operations

Accessor: `client.reviews` · Source: `walmart_apis/apis/reviews.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reviews.bulk_update_item_status

- **Route**: `PUT /v3/growth/reviews-accelerator/items/status`
- **Auth**: `access_token`
- **Signature**: `def bulk_update_item_status(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `body`
- **Params**: `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3GrowthReviewsAcceleratorItemsStatusResponse`
- **Returns (raw)**: `ApiResult[V3GrowthReviewsAcceleratorItemsStatusResponse, BulkUpdateItemStatusErrorBody]`
- **Error**: `BulkUpdateItemStatusErrorBody` — **Case A (typed)**
- **Error arms**: `V3GrowthReviewsAcceleratorItemsStatus400Error1` [400] · `V3GrowthReviewsAcceleratorItemsStatus401Error1` [401] · `V3GrowthReviewsAcceleratorItemsStatus403Error1` [403] · `V3GrowthReviewsAcceleratorItemsStatus500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthReviewsAcceleratorItemsStatusRequest` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status_request.py` |
| `V3GrowthReviewsAcceleratorItemsStatusRequestDict` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status_request.py` |
| `V3GrowthReviewsAcceleratorItemsStatusResponse` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status_response.py` |
| `BulkUpdateItemStatusErrorBody` | `walmart_apis/errors/bulk_update_item_status_error.py` |
| `V3GrowthReviewsAcceleratorItemsStatus400Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status400_error1.py` |
| `V3GrowthReviewsAcceleratorItemsStatus401Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status401_error1.py` |
| `V3GrowthReviewsAcceleratorItemsStatus403Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status403_error1.py` |
| `V3GrowthReviewsAcceleratorItemsStatus500Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items_status500_error1.py` |

### client.reviews.get_irp_categories

- **Route**: `POST /v3/growth/reviews-accelerator/categories`
- **Auth**: `access_token`
- **Signature**: `def get_irp_categories(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `body`
- **Params**: `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3GrowthReviewsAcceleratorCategoriesResponse`
- **Returns (raw)**: `ApiResult[V3GrowthReviewsAcceleratorCategoriesResponse, GetIrpCategoriesErrorBody]`
- **Error**: `GetIrpCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `V3GrowthReviewsAcceleratorCategories400Error1` [400] · `V3GrowthReviewsAcceleratorCategories401Error1` [401] · `V3GrowthReviewsAcceleratorCategories403Error1` [403] · `V3InsightsItemsListingQualityItems500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthReviewsAcceleratorCategoriesRequest` | `walmart_apis/models/v3_growth_reviews_accelerator_categories_request.py` |
| `V3GrowthReviewsAcceleratorCategoriesRequestDict` | `walmart_apis/models/v3_growth_reviews_accelerator_categories_request.py` |
| `V3GrowthReviewsAcceleratorCategoriesResponse` | `walmart_apis/models/v3_growth_reviews_accelerator_categories_response.py` |
| `GetIrpCategoriesErrorBody` | `walmart_apis/errors/get_irp_categories_error.py` |
| `V3GrowthReviewsAcceleratorCategories400Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_categories400_error1.py` |
| `V3GrowthReviewsAcceleratorCategories401Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_categories401_error1.py` |
| `V3GrowthReviewsAcceleratorCategories403Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_categories403_error1.py` |
| `V3InsightsItemsListingQualityItems500Error1` | `walmart_apis/models/v3_insights_items_listing_quality_items500_error1.py` |

### client.reviews.get_irp_items

- **Route**: `POST /v3/growth/reviews-accelerator/items`
- **Auth**: `access_token`
- **Signature**: `def get_irp_items(wm_global_version: WmGlobalVersionOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, body: V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict, *, scroll_id: str = "*", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_global_version`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `body`
- **Params**: `scroll_id` — query `scrollId` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3GrowthReviewsAcceleratorItemsResponse`
- **Returns (raw)**: `ApiResult[V3GrowthReviewsAcceleratorItemsResponse, GetIrpItemsErrorBody]`
- **Error**: `GetIrpItemsErrorBody` — **Case A (typed)**
- **Error arms**: `V3GrowthReviewsAcceleratorItems400Error1` [400] · `V3GrowthReviewsAcceleratorItems401Error1` [401] · `V3GrowthReviewsAcceleratorItems403Error1` [403] · `V3InsightsItemsListingQualityItems500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `V3GrowthReviewsAcceleratorItemsRequest` | `walmart_apis/models/v3_growth_reviews_accelerator_items_request.py` |
| `V3GrowthReviewsAcceleratorItemsRequestDict` | `walmart_apis/models/v3_growth_reviews_accelerator_items_request.py` |
| `V3GrowthReviewsAcceleratorItemsResponse` | `walmart_apis/models/v3_growth_reviews_accelerator_items_response.py` |
| `GetIrpItemsErrorBody` | `walmart_apis/errors/get_irp_items_error.py` |
| `V3GrowthReviewsAcceleratorItems400Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items400_error1.py` |
| `V3GrowthReviewsAcceleratorItems401Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items401_error1.py` |
| `V3GrowthReviewsAcceleratorItems403Error1` | `walmart_apis/models/v3_growth_reviews_accelerator_items403_error1.py` |
| `V3InsightsItemsListingQualityItems500Error1` | `walmart_apis/models/v3_insights_items_listing_quality_items500_error1.py` |

