<!-- Generated file — do not edit; regenerated with the SDK. -->

# InventoryApi — operations

Accessor: `client.inventory_api` · Source: `walmart_apis/apis/inventory_api.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.inventory_api.get_inventory

- **Route**: `GET /v3/inventory`
- **Auth**: `access_token`
- **Signature**: `def get_inventory(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `sku` — query · `ship_node` — query `shipNode` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `Inventory1`
- **Returns (raw)**: `ApiResult[Inventory1, GetInventoryErrorBody]`
- **Error**: `GetInventoryErrorBody` — **Case A (typed)**
- **Error arms**: `Inventory1` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `Inventory1` | `walmart_apis/models/inventory1.py` |
| `GetInventoryErrorBody` | `walmart_apis/errors/get_inventory_error.py` |

### client.inventory_api.get_multi_node_inventory_for_all_sku_and_all_ship_nodes

- **Route**: `GET /v3/inventories`
- **Auth**: `access_token`
- **Signature**: `def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, limit: str | None = "10", next_cursor: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `limit` — query · `next_cursor` — query `nextCursor` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `MultiNodeInventoryFetchResponseDto`
- **Returns (raw)**: `ApiResult[MultiNodeInventoryFetchResponseDto, GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody]`
- **Error**: `GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody` — **Case A (typed)**
- **Error arms**: `V3Inventories403Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `MultiNodeInventoryFetchResponseDto` | `walmart_apis/models/multi_node_inventory_fetch_response_dto.py` |
| `GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody` | `walmart_apis/errors/get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error.py` |
| `V3Inventories403Error1` | `walmart_apis/models/v3_inventories403_error1.py` |

### client.inventory_api.get_multi_node_inventory_for_sku_and_all_shipnodes

- **Route**: `GET /v3/inventories/{sku}`
- **Auth**: `access_token`
- **Signature**: `def get_multi_node_inventory_for_sku_and_all_shipnodes(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `sku` — path · `ship_node` — query `shipNode` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `InventoriesDto`
- **Returns (raw)**: `ApiResult[InventoriesDto, GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody]`
- **Error**: `GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody` — **Case A (typed)**
- **Error arms**: `InventoriesDto` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `InventoriesDto` | `walmart_apis/models/inventories_dto.py` |
| `GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody` | `walmart_apis/errors/get_multi_node_inventory_for_sku_and_all_shipnodes_error.py` |

### client.inventory_api.get_wfs_inventory

- **Route**: `GET /v3/fulfillment/inventory`
- **Auth**: `access_token`
- **Signature**: `def get_wfs_inventory(wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, *, sku: str | None = None, from_modified_date: str | None = None, to_modified_date: str | None = None, limit: str | None = "10", offset: str | None = "0", ship_node_type: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`
- **Params**: `sku` — query · `from_modified_date` — query `fromModifiedDate` · `to_modified_date` — query `toModifiedDate` · `limit` — query · `offset` — query · `ship_node_type` — query `shipNodeType` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE`
- **Returns (parsed)**: `V3FulfillmentInventoryResponse`
- **Returns (raw)**: `ApiResult[V3FulfillmentInventoryResponse, GetWfsinventoryErrorBody]`
- **Error**: `GetWfsinventoryErrorBody` — **Case A (typed)**
- **Error arms**: `V3FulfillmentInventory403Error1` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3FulfillmentInventoryResponse` | `walmart_apis/models/v3_fulfillment_inventory_response.py` |
| `GetWfsinventoryErrorBody` | `walmart_apis/errors/get_wfsinventory_error.py` |
| `V3FulfillmentInventory403Error1` | `walmart_apis/models/v3_fulfillment_inventory403_error1.py` |

### client.inventory_api.update_bulk_inventory

- **Route**: `POST /v3/feeds`
- **Auth**: `access_token`
- **Signature**: `def update_bulk_inventory(feed_type: FeedType1OrStr, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, file: FileInput, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `file`
- **Params**: `feed_type` — query `feedType` · `ship_node` — query `shipNode` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `file` — multipart file
- **Returns (parsed)**: `FeedId`
- **Returns (raw)**: `ApiResult[FeedId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FeedType1OrStr` | `walmart_apis/models/enums/feed_type1.py` |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `FeedId` | `walmart_apis/models/feed_id.py` |

### client.inventory_api.update_inventory_for_an_item

- **Route**: `PUT /v3/inventory`
- **Auth**: `access_token`
- **Signature**: `def update_inventory_for_an_item(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3InventoryRequest | V3InventoryRequestDict, *, ship_node: str | None = None, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `sku` — query · `ship_node` — query `shipNode` · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `Inventory1`
- **Returns (raw)**: `ApiResult[Inventory1, UpdateInventoryForAnItemErrorBody]`
- **Error**: `UpdateInventoryForAnItemErrorBody` — **Case A (typed)**
- **Error arms**: `Inventory1` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3InventoryRequest` | `walmart_apis/models/v3_inventory_request.py` |
| `V3InventoryRequestDict` | `walmart_apis/models/v3_inventory_request.py` |
| `Inventory1` | `walmart_apis/models/inventory1.py` |
| `UpdateInventoryForAnItemErrorBody` | `walmart_apis/errors/update_inventory_for_an_item_error.py` |

### client.inventory_api.update_multi_node_inventory

- **Route**: `PUT /v3/inventories/{sku}`
- **Auth**: `access_token`
- **Signature**: `def update_multi_node_inventory(sku: str, wm_qos_correlation_id: str, wm_svc_name: str, wm_market: WmMarket1OrStr, wm_global_version: WmGlobalVersionOrStr, body: V3InventoriesRequest | V3InventoriesRequestDict, *, wm_consumer_channel_type: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `wm_qos_correlation_id`, `wm_svc_name`, `wm_market`, `wm_global_version`, `body`
- **Params**: `sku` — path · `wm_qos_correlation_id` — header `WM_QOS.CORRELATION_ID` · `wm_svc_name` — header `WM_SVC.NAME` · `wm_market` — header `WM_MARKET` · `wm_global_version` — header `WM_GLOBAL_VERSION` · `wm_consumer_channel_type` — header `WM_CONSUMER.CHANNEL.TYPE` · `body` — JSON body
- **Returns (parsed)**: `MultiNodeInventoryUpdateResponseDto`
- **Returns (raw)**: `ApiResult[MultiNodeInventoryUpdateResponseDto, UpdateMultiNodeInventoryErrorBody]`
- **Error**: `UpdateMultiNodeInventoryErrorBody` — **Case A (typed)**
- **Error arms**: `MultiNodeInventoryUpdateResponseDto` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `WmMarket1OrStr` | `walmart_apis/models/enums/wm_market1.py` |
| `WmGlobalVersionOrStr` | `walmart_apis/models/enums/wm_global_version.py` |
| `V3InventoriesRequest` | `walmart_apis/models/v3_inventories_request.py` |
| `V3InventoriesRequestDict` | `walmart_apis/models/v3_inventories_request.py` |
| `MultiNodeInventoryUpdateResponseDto` | `walmart_apis/models/multi_node_inventory_update_response_dto.py` |
| `UpdateMultiNodeInventoryErrorBody` | `walmart_apis/errors/update_multi_node_inventory_error.py` |

