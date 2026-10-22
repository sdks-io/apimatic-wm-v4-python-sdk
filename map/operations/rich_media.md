<!-- Generated file — do not edit; regenerated with the SDK. -->

# RichMedia — operations

Accessor: `client.rich_media` · Source: `walmart_apis/apis/rich_media.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.rich_media.get_all_assets

- **Route**: `GET /v3/items/assets`
- **Auth**: `access_token`
- **Signature**: `def get_all_assets(wm_qos_correlation_id: str, wm_svc_name: str, *, page: int | None = 1, limit: int | None = 25, linked_gtins: list[str] | None = None, rich_media_title: str | None = None, rich_media_type: RichMediaTypeOrStr | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`
- **Params**: `page` — query · `limit` — query · `linked_gtins` — query `linkedGtins` · `rich_media_title` — query `richMediaTitle` · `rich_media_type` — query `richMediaType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `AssetsResponse`
- **Returns (raw)**: `ApiResult[AssetsResponse, GetAllAssetsErrorBody]`
- **Error**: `GetAllAssetsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `RichMediaTypeOrStr` | `walmart_apis/models/enums/rich_media_type.py` |
| `AssetsResponse` | `walmart_apis/models/assets_response.py` |
| `GetAllAssetsErrorBody` | `walmart_apis/errors/get_all_assets_error.py` |

### client.rich_media.rich_media_operation

- **Route**: `POST /v3/feeds?feedType=OMNI_RICH_MEDIA`
- **Auth**: `access_token`
- **Signature**: `def rich_media_operation(wm_qos_correlation_id: str, wm_svc_name: str, body: RichMediaFeedRequest | RichMediaFeedRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `body`
- **Params**: `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `FeedId1`
- **Returns (raw)**: `ApiResult[FeedId1, RichMediaOperationErrorBody]`
- **Error**: `RichMediaOperationErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 403, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `RichMediaFeedRequest` | `walmart_apis/models/rich_media_feed_request.py` |
| `RichMediaFeedRequestDict` | `walmart_apis/models/rich_media_feed_request.py` |
| `FeedId1` | `walmart_apis/models/feed_id1.py` |
| `RichMediaOperationErrorBody` | `walmart_apis/errors/rich_media_operation_error.py` |

