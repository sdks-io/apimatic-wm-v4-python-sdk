from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    file_part,
    json_body,
    json_decoder,
    multipart_body,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.get_inventory_error import GetInventoryErrorBody, get_inventory_error_mapper
from ..errors.get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error import (
    GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody,
    get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error_mapper,
)
from ..errors.get_multi_node_inventory_for_sku_and_all_shipnodes_error import (
    GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody,
    get_multi_node_inventory_for_sku_and_all_shipnodes_error_mapper,
)
from ..errors.get_wfsinventory_error import GetWfsinventoryErrorBody, get_wfsinventory_error_mapper
from ..errors.update_inventory_for_an_item_error import (
    UpdateInventoryForAnItemErrorBody,
    update_inventory_for_an_item_error_mapper,
)
from ..errors.update_multi_node_inventory_error import (
    UpdateMultiNodeInventoryErrorBody,
    update_multi_node_inventory_error_mapper,
)
from ..models.enums.feed_type1 import FeedType1OrStr
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.feed_id import FeedId
from ..models.inventories_dto import InventoriesDto
from ..models.inventory1 import Inventory1
from ..models.multi_node_inventory_fetch_response_dto import MultiNodeInventoryFetchResponseDto
from ..models.multi_node_inventory_update_response_dto import MultiNodeInventoryUpdateResponseDto
from ..models.v3_fulfillment_inventory_response import V3FulfillmentInventoryResponse
from ..models.v3_inventories_request import V3InventoriesRequest, V3InventoriesRequestDict
from ..models.v3_inventory_request import V3InventoryRequest, V3InventoryRequestDict
from ..server.server import Server


class InventoryApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InventoryApiWithRawResponse(client, server, auth)

    def get_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Inventory1:
        """You can use this API to get the inventory for a given item. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: The shipNode for which the inventory is requested. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Bad Request ``error`` is ``Inventory1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_inventory(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        limit: str | None = "10",
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiNodeInventoryFetchResponseDto:
        """This API will retrieve the inventory count for all of a seller's items across all ship nodes by item to ship
        node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be
        passed on from the previous call to next call. <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            limit: The number of items returned. Cannot be more than 50. <strong style="color: green;">Market
                availability: US only</strong>
            next_cursor: String returned from initial API call to indicate pagination. Specify nextCursor value to
                retrieve the next 50 items. <strong style="color: green;">Market availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found ``error`` is ``V3Inventories403Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                limit=limit,
                next_cursor=next_cursor,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_multi_node_inventory_for_sku_and_all_shipnodes(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InventoriesDto:
        """This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You
        can specify the ship node for which you want to fetch the inventory <br><b style='color:green;'>Market
        availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: ShipNode Id of the ship node for which the inventory is requested <strong style="color:
                green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``InventoriesDto | RawError``."""
        return unwrap(
            self._with_raw_response.get_multi_node_inventory_for_sku_and_all_shipnodes(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_wfs_inventory(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        sku: str | None = None,
        from_modified_date: str | None = None,
        to_modified_date: str | None = None,
        limit: str | None = "10",
        offset: str | None = "0",
        ship_node_type: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FulfillmentInventoryResponse:
        """You can use this API to get the current Available to Sell inventory quantities for all WFS items in your
        catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to
        reduce the response size. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            from_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            to_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            limit: Number of Sku to be returned. Cannot be larger than 300. <strong style="color: green;">Market
                availability: Global</strong>
            offset: Offset is the number of records you wish to skip before selecting records. <strong style="color:
                green;">Market availability: Global</strong>
            ship_node_type: Currently supported: multichannel. This param is enabled only for multi channel sellers. sku
                becomes mandatory and other params are ineffective while using this param. sku can either contain one
                item or list of sku's separated by comma (example: sku1,sku2) <strong style="color: green;">Market
                availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found ``error`` is ``V3FulfillmentInventory403Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_wfs_inventory(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                sku=sku,
                from_modified_date=from_modified_date,
                to_modified_date=to_modified_date,
                limit=limit,
                offset=offset,
                ship_node_type=ship_node_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_bulk_inventory(
        self,
        feed_type: FeedType1OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        file: FileInput,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId:
        """Updates inventory for items in bulk. Seller Can either use feed type "inventory" or "MP_INVENTORY"
        * Inventory spec 1.4 feed type: inventory
        * Inventory spec 1.5 feed type: MP_INVENTORY

        Note: Multi Node Inventory Update Feed (feedType=MP_INVENTORY) only supports JSON Request and Responses.

         Refer to the throttling limits before uploading the Feed Files.

        <b>Download the request body sample from </b>

         <a href="/file/mp/us/inventory-samples.zip">US Samples JSON</a>
        <a href="/file/mp/ca/inventory-samples.zip">CA Samples JSON</a> <a href="/file/mp/mx/inventory-samples.zip">MX
        Samples JSON</a> <a href="/file/mp/cl/inventory-samples.zip">CL Samples JSON</a> <br><b
        style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type Inventory: Global MP_Inventory: US | MX | CA <strong style="color: green;">Market
                availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            file: Feed file to upload <strong style="color: green;">Market availability: Global</strong>
            ship_node: The shipNode for which the inventory is to be updated. Not required in case of Multi Node
                Inventory Update Feed (feedType=MP_INVENTORY) <strong style="color: green;">Market availability: US
                only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_bulk_inventory(
                feed_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                file,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_inventory_for_an_item(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoryRequest | V3InventoryRequestDict,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Inventory1:
        """Updates the inventory for a given item. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: File fields
            ship_node: The shipNode for which the inventory is to be updated. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``Inventory1 | RawError``."""
        return unwrap(
            self._with_raw_response.update_inventory_for_an_item(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def update_multi_node_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoriesRequest | V3InventoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiNodeInventoryUpdateResponseDto:
        """This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.
        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Request fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``MultiNodeInventoryUpdateResponseDto | RawError``."""
        return unwrap(
            self._with_raw_response.update_multi_node_inventory(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> InventoryApiWithRawResponse:
        return self._with_raw_response


class AsyncInventoryApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInventoryApiWithRawResponse(client, server, auth)

    async def get_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Inventory1:
        """You can use this API to get the inventory for a given item. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: The shipNode for which the inventory is requested. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Bad Request ``error`` is ``Inventory1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_inventory(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        limit: str | None = "10",
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiNodeInventoryFetchResponseDto:
        """This API will retrieve the inventory count for all of a seller's items across all ship nodes by item to ship
        node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be
        passed on from the previous call to next call. <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            limit: The number of items returned. Cannot be more than 50. <strong style="color: green;">Market
                availability: US only</strong>
            next_cursor: String returned from initial API call to indicate pagination. Specify nextCursor value to
                retrieve the next 50 items. <strong style="color: green;">Market availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found ``error`` is ``V3Inventories403Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                limit=limit,
                next_cursor=next_cursor,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_multi_node_inventory_for_sku_and_all_shipnodes(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> InventoriesDto:
        """This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You
        can specify the ship node for which you want to fetch the inventory <br><b style='color:green;'>Market
        availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: ShipNode Id of the ship node for which the inventory is requested <strong style="color:
                green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``InventoriesDto | RawError``."""
        return unwrap(
            await self._with_raw_response.get_multi_node_inventory_for_sku_and_all_shipnodes(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_wfs_inventory(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        sku: str | None = None,
        from_modified_date: str | None = None,
        to_modified_date: str | None = None,
        limit: str | None = "10",
        offset: str | None = "0",
        ship_node_type: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3FulfillmentInventoryResponse:
        """You can use this API to get the current Available to Sell inventory quantities for all WFS items in your
        catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to
        reduce the response size. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            from_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            to_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            limit: Number of Sku to be returned. Cannot be larger than 300. <strong style="color: green;">Market
                availability: Global</strong>
            offset: Offset is the number of records you wish to skip before selecting records. <strong style="color:
                green;">Market availability: Global</strong>
            ship_node_type: Currently supported: multichannel. This param is enabled only for multi channel sellers. sku
                becomes mandatory and other params are ineffective while using this param. sku can either contain one
                item or list of sku's separated by comma (example: sku1,sku2) <strong style="color: green;">Market
                availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Not Found ``error`` is ``V3FulfillmentInventory403Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_wfs_inventory(
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                sku=sku,
                from_modified_date=from_modified_date,
                to_modified_date=to_modified_date,
                limit=limit,
                offset=offset,
                ship_node_type=ship_node_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_bulk_inventory(
        self,
        feed_type: FeedType1OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        file: AsyncFileInput,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId:
        """Updates inventory for items in bulk. Seller Can either use feed type "inventory" or "MP_INVENTORY"
        * Inventory spec 1.4 feed type: inventory
        * Inventory spec 1.5 feed type: MP_INVENTORY

        Note: Multi Node Inventory Update Feed (feedType=MP_INVENTORY) only supports JSON Request and Responses.

         Refer to the throttling limits before uploading the Feed Files.

        <b>Download the request body sample from </b>

         <a href="/file/mp/us/inventory-samples.zip">US Samples JSON</a>
        <a href="/file/mp/ca/inventory-samples.zip">CA Samples JSON</a> <a href="/file/mp/mx/inventory-samples.zip">MX
        Samples JSON</a> <a href="/file/mp/cl/inventory-samples.zip">CL Samples JSON</a> <br><b
        style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type Inventory: Global MP_Inventory: US | MX | CA <strong style="color: green;">Market
                availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            file: Feed file to upload <strong style="color: green;">Market availability: Global</strong>
            ship_node: The shipNode for which the inventory is to be updated. Not required in case of Multi Node
                Inventory Update Feed (feedType=MP_INVENTORY) <strong style="color: green;">Market availability: US
                only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_bulk_inventory(
                feed_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                file,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_inventory_for_an_item(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoryRequest | V3InventoryRequestDict,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Inventory1:
        """Updates the inventory for a given item. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: File fields
            ship_node: The shipNode for which the inventory is to be updated. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``Inventory1 | RawError``."""
        return unwrap(
            await self._with_raw_response.update_inventory_for_an_item(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                ship_node=ship_node,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def update_multi_node_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoriesRequest | V3InventoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiNodeInventoryUpdateResponseDto:
        """This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.
        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Request fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found ``error`` is ``MultiNodeInventoryUpdateResponseDto | RawError``."""
        return unwrap(
            await self._with_raw_response.update_multi_node_inventory(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncInventoryApiWithRawResponse:
        return self._with_raw_response


class InventoryApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Inventory1, GetInventoryErrorBody]:
        """You can use this API to get the inventory for a given item. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: The shipNode for which the inventory is requested. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/inventory"),
            query_params=[param[str]("sku", sku), param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[Inventory1],
            error_mapper=get_inventory_error_mapper,
            request_options=request_options,
        )

    def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        limit: str | None = "10",
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiNodeInventoryFetchResponseDto, GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody]:
        """This API will retrieve the inventory count for all of a seller's items across all ship nodes by item to ship
        node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be
        passed on from the previous call to next call. <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            limit: The number of items returned. Cannot be more than 50. <strong style="color: green;">Market
                availability: US only</strong>
            next_cursor: String returned from initial API call to indicate pagination. Specify nextCursor value to
                retrieve the next 50 items. <strong style="color: green;">Market availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/inventories"),
            query_params=[param[str | None]("limit", limit), param[str | None]("nextCursor", next_cursor)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[MultiNodeInventoryFetchResponseDto],
            error_mapper=get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error_mapper,
            request_options=request_options,
        )

    def get_multi_node_inventory_for_sku_and_all_shipnodes(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InventoriesDto, GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody]:
        """This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You
        can specify the ship node for which you want to fetch the inventory <br><b style='color:green;'>Market
        availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: ShipNode Id of the ship node for which the inventory is requested <strong style="color:
                green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/inventories/{sku}"),
            path_params=[param[str]("sku", sku)],
            query_params=[param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[InventoriesDto],
            error_mapper=get_multi_node_inventory_for_sku_and_all_shipnodes_error_mapper,
            request_options=request_options,
        )

    def get_wfs_inventory(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        sku: str | None = None,
        from_modified_date: str | None = None,
        to_modified_date: str | None = None,
        limit: str | None = "10",
        offset: str | None = "0",
        ship_node_type: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FulfillmentInventoryResponse, GetWfsinventoryErrorBody]:
        """You can use this API to get the current Available to Sell inventory quantities for all WFS items in your
        catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to
        reduce the response size. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            from_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            to_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            limit: Number of Sku to be returned. Cannot be larger than 300. <strong style="color: green;">Market
                availability: Global</strong>
            offset: Offset is the number of records you wish to skip before selecting records. <strong style="color:
                green;">Market availability: Global</strong>
            ship_node_type: Currently supported: multichannel. This param is enabled only for multi channel sellers. sku
                becomes mandatory and other params are ineffective while using this param. sku can either contain one
                item or list of sku's separated by comma (example: sku1,sku2) <strong style="color: green;">Market
                availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/fulfillment/inventory"),
            query_params=[
                param[str | None]("sku", sku),
                param[str | None]("fromModifiedDate", from_modified_date),
                param[str | None]("toModifiedDate", to_modified_date),
                param[str | None]("limit", limit),
                param[str | None]("offset", offset),
                param[str | None]("shipNodeType", ship_node_type),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3FulfillmentInventoryResponse],
            error_mapper=get_wfsinventory_error_mapper,
            request_options=request_options,
        )

    def update_bulk_inventory(
        self,
        feed_type: FeedType1OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        file: FileInput,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId, RawError]:
        """Updates inventory for items in bulk. Seller Can either use feed type "inventory" or "MP_INVENTORY"
        * Inventory spec 1.4 feed type: inventory
        * Inventory spec 1.5 feed type: MP_INVENTORY

        Note: Multi Node Inventory Update Feed (feedType=MP_INVENTORY) only supports JSON Request and Responses.

         Refer to the throttling limits before uploading the Feed Files.

        <b>Download the request body sample from </b>

         <a href="/file/mp/us/inventory-samples.zip">US Samples JSON</a>
        <a href="/file/mp/ca/inventory-samples.zip">CA Samples JSON</a> <a href="/file/mp/mx/inventory-samples.zip">MX
        Samples JSON</a> <a href="/file/mp/cl/inventory-samples.zip">CL Samples JSON</a> <br><b
        style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type Inventory: Global MP_Inventory: US | MX | CA <strong style="color: green;">Market
                availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            file: Feed file to upload <strong style="color: green;">Market availability: Global</strong>
            ship_node: The shipNode for which the inventory is to be updated. Not required in case of Multi Node
                Inventory Update Feed (feedType=MP_INVENTORY) <strong style="color: green;">Market availability: US
                only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds"),
            query_params=[param[FeedType1OrStr]("feedType", feed_type), param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(file_part("file", file)),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_inventory_for_an_item(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoryRequest | V3InventoryRequestDict,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Inventory1, UpdateInventoryForAnItemErrorBody]:
        """Updates the inventory for a given item. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: File fields
            ship_node: The shipNode for which the inventory is to be updated. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/inventory"),
            query_params=[param[str]("sku", sku), param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3InventoryRequest | V3InventoryRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[Inventory1],
            error_mapper=update_inventory_for_an_item_error_mapper,
            request_options=request_options,
        )

    def update_multi_node_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoriesRequest | V3InventoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiNodeInventoryUpdateResponseDto, UpdateMultiNodeInventoryErrorBody]:
        """This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.
        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Request fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/inventories/{sku}"),
            path_params=[param[str]("sku", sku)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3InventoriesRequest | V3InventoriesRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[MultiNodeInventoryUpdateResponseDto],
            error_mapper=update_multi_node_inventory_error_mapper,
            request_options=request_options,
        )


class AsyncInventoryApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Inventory1, GetInventoryErrorBody]:
        """You can use this API to get the inventory for a given item. <br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: The shipNode for which the inventory is requested. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/inventory"),
            query_params=[param[str]("sku", sku), param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[Inventory1],
            error_mapper=get_inventory_error_mapper,
            request_options=request_options,
        )

    async def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        limit: str | None = "10",
        next_cursor: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiNodeInventoryFetchResponseDto, GetMultiNodeInventoryForAllSkuAndAllShipNodesErrorBody]:
        """This API will retrieve the inventory count for all of a seller's items across all ship nodes by item to ship
        node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be
        passed on from the previous call to next call. <br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            limit: The number of items returned. Cannot be more than 50. <strong style="color: green;">Market
                availability: US only</strong>
            next_cursor: String returned from initial API call to indicate pagination. Specify nextCursor value to
                retrieve the next 50 items. <strong style="color: green;">Market availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/inventories"),
            query_params=[param[str | None]("limit", limit), param[str | None]("nextCursor", next_cursor)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[MultiNodeInventoryFetchResponseDto],
            error_mapper=get_multi_node_inventory_for_all_sku_and_all_ship_nodes_error_mapper,
            request_options=request_options,
        )

    async def get_multi_node_inventory_for_sku_and_all_shipnodes(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[InventoriesDto, GetMultiNodeInventoryForSkuAndAllShipnodesErrorBody]:
        """This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You
        can specify the ship node for which you want to fetch the inventory <br><b style='color:green;'>Market
        availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            ship_node: ShipNode Id of the ship node for which the inventory is requested <strong style="color:
                green;">Market availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/inventories/{sku}"),
            path_params=[param[str]("sku", sku)],
            query_params=[param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[InventoriesDto],
            error_mapper=get_multi_node_inventory_for_sku_and_all_shipnodes_error_mapper,
            request_options=request_options,
        )

    async def get_wfs_inventory(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        sku: str | None = None,
        from_modified_date: str | None = None,
        to_modified_date: str | None = None,
        limit: str | None = "10",
        offset: str | None = "0",
        ship_node_type: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3FulfillmentInventoryResponse, GetWfsinventoryErrorBody]:
        """You can use this API to get the current Available to Sell inventory quantities for all WFS items in your
        catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to
        reduce the response size. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            from_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            to_modified_date: last inventory modified date - starting range. <strong style="color: green;">Market
                availability: Global</strong>
            limit: Number of Sku to be returned. Cannot be larger than 300. <strong style="color: green;">Market
                availability: Global</strong>
            offset: Offset is the number of records you wish to skip before selecting records. <strong style="color:
                green;">Market availability: Global</strong>
            ship_node_type: Currently supported: multichannel. This param is enabled only for multi channel sellers. sku
                becomes mandatory and other params are ineffective while using this param. sku can either contain one
                item or list of sku's separated by comma (example: sku1,sku2) <strong style="color: green;">Market
                availability: US only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/fulfillment/inventory"),
            query_params=[
                param[str | None]("sku", sku),
                param[str | None]("fromModifiedDate", from_modified_date),
                param[str | None]("toModifiedDate", to_modified_date),
                param[str | None]("limit", limit),
                param[str | None]("offset", offset),
                param[str | None]("shipNodeType", ship_node_type),
            ],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3FulfillmentInventoryResponse],
            error_mapper=get_wfsinventory_error_mapper,
            request_options=request_options,
        )

    async def update_bulk_inventory(
        self,
        feed_type: FeedType1OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        file: AsyncFileInput,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId, RawError]:
        """Updates inventory for items in bulk. Seller Can either use feed type "inventory" or "MP_INVENTORY"
        * Inventory spec 1.4 feed type: inventory
        * Inventory spec 1.5 feed type: MP_INVENTORY

        Note: Multi Node Inventory Update Feed (feedType=MP_INVENTORY) only supports JSON Request and Responses.

         Refer to the throttling limits before uploading the Feed Files.

        <b>Download the request body sample from </b>

         <a href="/file/mp/us/inventory-samples.zip">US Samples JSON</a>
        <a href="/file/mp/ca/inventory-samples.zip">CA Samples JSON</a> <a href="/file/mp/mx/inventory-samples.zip">MX
        Samples JSON</a> <a href="/file/mp/cl/inventory-samples.zip">CL Samples JSON</a> <br><b
        style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type Inventory: Global MP_Inventory: US | MX | CA <strong style="color: green;">Market
                availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            file: Feed file to upload <strong style="color: green;">Market availability: Global</strong>
            ship_node: The shipNode for which the inventory is to be updated. Not required in case of Multi Node
                Inventory Update Feed (feedType=MP_INVENTORY) <strong style="color: green;">Market availability: US
                only</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds"),
            query_params=[param[FeedType1OrStr]("feedType", feed_type), param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(file_part("file", file)),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedId],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_inventory_for_an_item(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoryRequest | V3InventoryRequestDict,
        *,
        ship_node: str | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Inventory1, UpdateInventoryForAnItemErrorBody]:
        """Updates the inventory for a given item. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’, '{',
                '}' as well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters
                don't need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: File fields
            ship_node: The shipNode for which the inventory is to be updated. <strong style="color: green;">Market
                availability: Global</strong>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/inventory"),
            query_params=[param[str]("sku", sku), param[str | None]("shipNode", ship_node)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3InventoryRequest | V3InventoryRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[Inventory1],
            error_mapper=update_inventory_for_an_item_error_mapper,
            request_options=request_options,
        )

    async def update_multi_node_inventory(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3InventoriesRequest | V3InventoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiNodeInventoryUpdateResponseDto, UpdateMultiNodeInventoryErrorBody]:
        """This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.
        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '/', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', ‘ ’ as
                well as '%' itself if it's a part of sku. Make sure to encode space with %20. Other characters don't
                need to be encoded. <strong style="color: green;">Market availability: Global</strong>
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs. <strong style="color: green;">Market availability: Global</strong>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <strong style="color: green;">Market availability: Global</strong>
            wm_svc_name: Specifies the name of the Walmart service being called. <strong style="color: green;">Market
                availability: Global</strong>
            wm_market: The target market of the API call. <strong style="color: green;">Market availability:
                Global</strong>
            wm_global_version: The version of the global API used. <strong style="color: green;">Market availability:
                Global</strong>
            body: Request fields
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/inventories/{sku}"),
            path_params=[param[str]("sku", sku)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3InventoriesRequest | V3InventoriesRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[MultiNodeInventoryUpdateResponseDto],
            error_mapper=update_multi_node_inventory_error_mapper,
            request_options=request_options,
        )
