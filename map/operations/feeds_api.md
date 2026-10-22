<!-- Generated file — do not edit; regenerated with the SDK. -->

# FeedsApi — operations

Accessor: `client.feeds_api` · Source: `walmart_apis/apis/feeds_api.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.feeds_api.get_all_feed_statuses

- **Route**: `GET /v3/feeds`
- **Auth**: `access_token`
- **Signature**: `def get_all_feed_statuses(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, feed_id: str | None = None, feed_type: str | None = None, feed_status: FeedStatus1OrStr | None = None, offset: str | None = "0", limit: str | None = "50", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `feed_id` — query `feedId` · `feed_type` — query `feedType` · `feed_status` — query `feedStatus` · `offset` — query · `limit` — query · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `FeedRecordResponse`
- **Returns (raw)**: `ApiResult[FeedRecordResponse, GetAllFeedStatusesErrorBody]`
- **Error**: `GetAllFeedStatusesErrorBody` — **Case A (typed)**
- **Error arms**: `FeedRecordResponse` [404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `FeedStatus1OrStr` | `walmart_apis/models/enums/feed_status1.py` |
| `FeedRecordResponse` | `walmart_apis/models/feed_record_response.py` |
| `GetAllFeedStatusesErrorBody` | `walmart_apis/errors/get_all_feed_statuses_error.py` |

### client.feeds_api.get_feed_error_report

- **Route**: `GET /v3/feeds/{feedId}/errorReport`
- **Auth**: `access_token`
- **Signature**: `def get_feed_error_report(feed_id: str, feed_type: FeedTypeOrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_id`, `feed_type`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `feed_id` — path `feedId` · `feed_type` — query `feedType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FeedTypeOrStr` | `walmart_apis/models/enums/feed_type.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |

### client.feeds_api.get_feed_item_status

- **Route**: `GET /v3/feeds/{feedId}`
- **Auth**: `access_token`
- **Signature**: `def get_feed_item_status(feed_id: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, include_details: str | None = "false", offset: str | None = "0", limit: str | None = "50", wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_id`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `feed_id` — path `feedId` · `include_details` — query `includeDetails` · `offset` — query · `limit` — query · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3FeedsResponse1`
- **Returns (raw)**: `ApiResult[V3FeedsResponse1, GetFeedItemStatusErrorBody]`
- **Error**: `GetFeedItemStatusErrorBody` — **Case A (typed)**
- **Error arms**: `V3Feeds404Error21` [404] · `V3Feeds500Error21` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FeedsResponse1` | `walmart_apis/models/v3_feeds_response1.py` |
| `GetFeedItemStatusErrorBody` | `walmart_apis/errors/get_feed_item_status_error.py` |
| `V3Feeds404Error21` | `walmart_apis/models/v3_feeds404_error21.py` |
| `V3Feeds500Error21` | `walmart_apis/models/v3_feeds500_error21.py` |

