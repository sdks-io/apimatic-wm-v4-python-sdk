<!-- Generated file — do not edit; regenerated with the SDK. -->

# Disputes — operations

Accessor: `client.disputes` · Source: `walmart_apis/apis/disputes.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.disputes.post_contest

- **Route**: `POST /v3/items/dispute/duplicates/contest`
- **Signature**: `def post_contest(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ItemsDisputeDuplicatesContestRequest | V3ItemsDisputeDuplicatesContestRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `DisputeContestResponses`
- **Returns (raw)**: `ApiResult[DisputeContestResponses, PostContestErrorBody]`
- **Error**: `PostContestErrorBody` — **Case A (typed)**
- **Error arms**: `V3ItemsDisputeDuplicatesContest403Error1` [403] · `V3ItemsDisputeDuplicatesContest404Error1` [404] · `V3ItemsDisputeDuplicatesContest500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ItemsDisputeDuplicatesContestRequest` | `walmart_apis/models/v3_items_dispute_duplicates_contest_request.py` |
| `V3ItemsDisputeDuplicatesContestRequestDict` | `walmart_apis/models/v3_items_dispute_duplicates_contest_request.py` |
| `DisputeContestResponses` | `walmart_apis/models/dispute_contest_responses.py` |
| `PostContestErrorBody` | `walmart_apis/errors/post_contest_error.py` |
| `V3ItemsDisputeDuplicatesContest403Error1` | `walmart_apis/models/v3_items_dispute_duplicates_contest403_error1.py` |
| `V3ItemsDisputeDuplicatesContest404Error1` | `walmart_apis/models/v3_items_dispute_duplicates_contest404_error1.py` |
| `V3ItemsDisputeDuplicatesContest500Error1` | `walmart_apis/models/v3_items_dispute_duplicates_contest500_error1.py` |

### client.disputes.post_status

- **Route**: `POST /v3/items/dispute/duplicates/status`
- **Signature**: `def post_status(wm_sec_access_token: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3ItemsDisputeDuplicatesStatusRequest | V3ItemsDisputeDuplicatesStatusRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_sec_access_token`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `wm_sec_access_token` — header `WM_SEC.ACCESS_TOKEN` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `V3ItemsDisputeDuplicatesStatusResponse`
- **Returns (raw)**: `ApiResult[V3ItemsDisputeDuplicatesStatusResponse, PostStatusErrorBody]`
- **Error**: `PostStatusErrorBody` — **Case A (typed)**
- **Error arms**: `V3ItemsDisputeDuplicatesStatus403Error1` [403] · `V3ItemsDisputeDuplicatesStatus404Error1` [404] · `V3ItemsDisputeDuplicatesStatus500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3ItemsDisputeDuplicatesStatusRequest` | `walmart_apis/models/v3_items_dispute_duplicates_status_request.py` |
| `V3ItemsDisputeDuplicatesStatusRequestDict` | `walmart_apis/models/v3_items_dispute_duplicates_status_request.py` |
| `V3ItemsDisputeDuplicatesStatusResponse` | `walmart_apis/models/v3_items_dispute_duplicates_status_response.py` |
| `PostStatusErrorBody` | `walmart_apis/errors/post_status_error.py` |
| `V3ItemsDisputeDuplicatesStatus403Error1` | `walmart_apis/models/v3_items_dispute_duplicates_status403_error1.py` |
| `V3ItemsDisputeDuplicatesStatus404Error1` | `walmart_apis/models/v3_items_dispute_duplicates_status404_error1.py` |
| `V3ItemsDisputeDuplicatesStatus500Error1` | `walmart_apis/models/v3_items_dispute_duplicates_status500_error1.py` |

