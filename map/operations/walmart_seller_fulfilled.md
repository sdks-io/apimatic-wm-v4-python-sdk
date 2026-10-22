<!-- Generated file — do not edit; regenerated with the SDK. -->

# WalmartSellerFulfilled — operations

Accessor: `client.walmart_seller_fulfilled` · Source: `walmart_apis/apis/walmart_seller_fulfilled.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.walmart_seller_fulfilled.walmart_plus_enrollment

- **Route**: `POST /v3/feeds?feedType=PROGRAM_ACTIONS&requestType=WALMART_PLUS_SFF`
- **Signature**: `def walmart_plus_enrollment(feed_type: FeedType3OrStr, request_type: RequestTypeOrStr, wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarketOrStr, file_name: FileInput, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `request_type`, `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `file_name`
- **Params**: `feed_type` — query `feedType` · `request_type` — query `requestType` · `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `file_name` — multipart file `fileName`
- **Returns (parsed)**: `V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse`
- **Returns (raw)**: `ApiResult[V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse, WalmartPlusEnrollmentErrorBody]`
- **Error**: `WalmartPlusEnrollmentErrorBody` — **Case A (typed)**
- **Error arms**: `V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1` [400] · `V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedType3OrStr` | `walmart_apis/models/enums/feed_type3.py` |
| `RequestTypeOrStr` | `walmart_apis/models/enums/request_type.py` |
| `WmMarketOrStr` | `walmart_apis/models/enums/wm_market.py` |
| `V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSffResponse` | `walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff_response.py` |
| `WalmartPlusEnrollmentErrorBody` | `walmart_apis/errors/walmart_plus_enrollment_error.py` |
| `V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff400Error1` | `walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff400_error1.py` |
| `V3FeedsFeedTypeProgramActionsRequestTypeWalmartPlusSff500Error1` | `walmart_apis/models/v3_feeds_feed_type_program_actions_request_type_walmart_plus_sff500_error1.py` |

