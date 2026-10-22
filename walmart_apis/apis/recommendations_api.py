from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_fulfill_with_wfsrecommendations_error import (
    GetFulfillWithWfsrecommendationsErrorBody,
    get_fulfill_with_wfsrecommendations_error_mapper,
)
from ..errors.get_restock_recommendations_error import (
    GetRestockRecommendationsErrorBody,
    get_restock_recommendations_error_mapper,
)
from ..errors.get_shipment_quantity_recommendations_error import (
    GetShipmentQuantityRecommendationsErrorBody,
    get_shipment_quantity_recommendations_error_mapper,
)
from ..errors.get_unpublished_recommendations_error import (
    GetUnpublishedRecommendationsErrorBody,
    get_unpublished_recommendations_error_mapper,
)
from ..models.enums.sort_order import SortOrder, SortOrderOrStr
from ..models.v3_wfs_recommendation_fulfil_with_wfs_response import V3WfsRecommendationFulfilWithWfsResponse
from ..models.v3_wfs_recommendation_restock_response import V3WfsRecommendationRestockResponse
from ..models.v3_wfs_recommendation_shipment_quantity_request import (
    V3WfsRecommendationShipmentQuantityRequest,
    V3WfsRecommendationShipmentQuantityRequestDict,
)
from ..models.v3_wfs_recommendation_shipment_quantity_response import V3WfsRecommendationShipmentQuantityResponse
from ..models.v3_wfs_recommendation_unpublished_response import V3WfsRecommendationUnpublishedResponse
from ..server.server import Server


class RecommendationsApi:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = RecommendationsApiWithRawResponse(client, server)

    def get_fulfill_with_wfs_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationFulfilWithWfsResponse:
        """Use **Fulfill With WFS Recommendations** to identify which seller-fulfilled items in your catalog Walmart
        suggests could potentially perform best when fulfilled by WFS. These suggestions are available on demand, and
        suggestions are refreshed the 1st and 15th of each month.

        Key attributes include:

        - **estimatedSalesLift**: The estimated increase in sales you could see if you converted the suggested items
            from seller-fulfilled to WFS.

        - **sellerFulfilledPast30DaysSales**: A historical view of your seller-fulfilled sales for the past 30 days.
        - **walmartFulfilledEstimatedSales**: An estimated view of your potential sales if the suggested items were
            fulfilled by WFS.

        You can use these suggestions to determine which items to convert to WFS.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - INTERNAL_SERVER_ERROR Internal Server Error ``error`` is ``ErrorResponse2 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_fulfill_with_wfs_recommendations(
                content_type,
                accept,
                wm_global_version,
                wm_market,
                wm_audit_origin_source,
                customer_favorite=customer_favorite,
                show_insights=show_insights,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                show_hidden_records_only=show_hidden_records_only,
                request_options=request_options,
            ),
        )

    def get_restock_recommendations(
        self,
        authorization: str,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = True,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "forecastedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationRestockResponse:
        """Use **Restock Recommendations** to get Walmart-generated suggestions for the items you should restock with
        WFS based on your current inventory and forecasted sales demand. These suggestions are available on demand. Key
        attributes include:

        - **suggestedUnits**: The number of units we suggest you send of this item to WFS
        - **forecastedSalesLift**: The estimated increase in sales you may see if your items are restocked according to
            our suggestions
        - **totalForecastedSalesLost**: How much money you're estimated to lose out on if you don't restock your
            inventory

        Once you determine which suggested items to restock, you can use the Create inbound shipment API to create a
        shipping plan to send inventory to WFS.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - INTERNAL_SERVER_ERROR Internal Server Error ``error`` is ``ErrorResponse2 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_restock_recommendations(
                authorization,
                content_type,
                accept,
                wm_global_version,
                wm_market,
                wm_audit_origin_source,
                customer_favorite=customer_favorite,
                show_insights=show_insights,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                show_hidden_records_only=show_hidden_records_only,
                request_options=request_options,
            ),
        )

    def get_shipment_quantity_recommendations(
        self,
        authorization: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        body: V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationShipmentQuantityResponse:
        """Use this API to get recommended shipment quantities for the items that you plan to send to Walmart
        Fulfillment Services (WFS) in order to achieve optimal inventory levels.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            wm_sec_access_token: The access token retrieved in the Token API call <b style='color: green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <b style='color: green;'>Market availability: US only</b>
            wm_svc_name: Walmart Service Name. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Market identifier. <b style='color: green;'>Market availability: US only</b>
            body: Request body containing GTINs or SKUs to retrieve the quantity limit. <b style='color: green;'>Market
                availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - GTIN/SKU is required attribute Not Found - Invalid route Internal Server Error - All
                GTINs are invalid for the seller ``error`` is ``ErrorResponse2 | NotFoundResponse | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment_quantity_recommendations(
                authorization,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                accept,
                wm_global_version,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_unpublished_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationUnpublishedResponse:
        """This call helps you identify the estimated storage fees with Walmart for your unpublished WFS items.

        Use **Unpublish Recommendations** to fetch a current list of your unpublished WFS items. This is available on
        demand.

        Key data attributes include:

        - **unpublishedIssue**: The reason your item is currently unpublished with Walmart.
        - **estimatedStorageFee**: The estimated storage costs associated with your unpublished WFS inventory.
        - **totalunpublishedunitsstored**: The total quantity of units in WFS fulfillment centers for unpublished items.

        Use this data to identify the reason these items are unpublished and the estimated costs associated with these
        unpublished items. By default, these suggestions will only include items that are active with an Available to
        Sell (ATS) quantity of 0.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - INTERNAL_SERVER_ERROR Internal Server Error ``error`` is ``ErrorResponse2 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_unpublished_recommendations(
                content_type,
                accept,
                wm_global_version,
                wm_market,
                wm_audit_origin_source,
                customer_favorite=customer_favorite,
                show_insights=show_insights,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> RecommendationsApiWithRawResponse:
        return self._with_raw_response


class AsyncRecommendationsApi:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncRecommendationsApiWithRawResponse(client, server)

    async def get_fulfill_with_wfs_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationFulfilWithWfsResponse:
        """Use **Fulfill With WFS Recommendations** to identify which seller-fulfilled items in your catalog Walmart
        suggests could potentially perform best when fulfilled by WFS. These suggestions are available on demand, and
        suggestions are refreshed the 1st and 15th of each month.

        Key attributes include:

        - **estimatedSalesLift**: The estimated increase in sales you could see if you converted the suggested items
            from seller-fulfilled to WFS.

        - **sellerFulfilledPast30DaysSales**: A historical view of your seller-fulfilled sales for the past 30 days.
        - **walmartFulfilledEstimatedSales**: An estimated view of your potential sales if the suggested items were
            fulfilled by WFS.

        You can use these suggestions to determine which items to convert to WFS.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - INTERNAL_SERVER_ERROR Internal Server Error ``error`` is ``ErrorResponse2 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_fulfill_with_wfs_recommendations(
                content_type,
                accept,
                wm_global_version,
                wm_market,
                wm_audit_origin_source,
                customer_favorite=customer_favorite,
                show_insights=show_insights,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                show_hidden_records_only=show_hidden_records_only,
                request_options=request_options,
            ),
        )

    async def get_restock_recommendations(
        self,
        authorization: str,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = True,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "forecastedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationRestockResponse:
        """Use **Restock Recommendations** to get Walmart-generated suggestions for the items you should restock with
        WFS based on your current inventory and forecasted sales demand. These suggestions are available on demand. Key
        attributes include:

        - **suggestedUnits**: The number of units we suggest you send of this item to WFS
        - **forecastedSalesLift**: The estimated increase in sales you may see if your items are restocked according to
            our suggestions
        - **totalForecastedSalesLost**: How much money you're estimated to lose out on if you don't restock your
            inventory

        Once you determine which suggested items to restock, you can use the Create inbound shipment API to create a
        shipping plan to send inventory to WFS.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - INTERNAL_SERVER_ERROR Internal Server Error ``error`` is ``ErrorResponse2 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_restock_recommendations(
                authorization,
                content_type,
                accept,
                wm_global_version,
                wm_market,
                wm_audit_origin_source,
                customer_favorite=customer_favorite,
                show_insights=show_insights,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                show_hidden_records_only=show_hidden_records_only,
                request_options=request_options,
            ),
        )

    async def get_shipment_quantity_recommendations(
        self,
        authorization: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        body: V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationShipmentQuantityResponse:
        """Use this API to get recommended shipment quantities for the items that you plan to send to Walmart
        Fulfillment Services (WFS) in order to achieve optimal inventory levels.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            wm_sec_access_token: The access token retrieved in the Token API call <b style='color: green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <b style='color: green;'>Market availability: US only</b>
            wm_svc_name: Walmart Service Name. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Market identifier. <b style='color: green;'>Market availability: US only</b>
            body: Request body containing GTINs or SKUs to retrieve the quantity limit. <b style='color: green;'>Market
                availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - GTIN/SKU is required attribute Not Found - Invalid route Internal Server Error - All
                GTINs are invalid for the seller ``error`` is ``ErrorResponse2 | NotFoundResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment_quantity_recommendations(
                authorization,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                accept,
                wm_global_version,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_unpublished_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3WfsRecommendationUnpublishedResponse:
        """This call helps you identify the estimated storage fees with Walmart for your unpublished WFS items.

        Use **Unpublish Recommendations** to fetch a current list of your unpublished WFS items. This is available on
        demand.

        Key data attributes include:

        - **unpublishedIssue**: The reason your item is currently unpublished with Walmart.
        - **estimatedStorageFee**: The estimated storage costs associated with your unpublished WFS inventory.
        - **totalunpublishedunitsstored**: The total quantity of units in WFS fulfillment centers for unpublished items.

        Use this data to identify the reason these items are unpublished and the estimated costs associated with these
        unpublished items. By default, these suggestions will only include items that are active with an Available to
        Sell (ATS) quantity of 0.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request - INTERNAL_SERVER_ERROR Internal Server Error ``error`` is ``ErrorResponse2 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_unpublished_recommendations(
                content_type,
                accept,
                wm_global_version,
                wm_market,
                wm_audit_origin_source,
                customer_favorite=customer_favorite,
                show_insights=show_insights,
                limit=limit,
                offset=offset,
                sort_by=sort_by,
                sort_order=sort_order,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncRecommendationsApiWithRawResponse:
        return self._with_raw_response


class RecommendationsApiWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_fulfill_with_wfs_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationFulfilWithWfsResponse, GetFulfillWithWfsrecommendationsErrorBody]:
        """Use **Fulfill With WFS Recommendations** to identify which seller-fulfilled items in your catalog Walmart
        suggests could potentially perform best when fulfilled by WFS. These suggestions are available on demand, and
        suggestions are refreshed the 1st and 15th of each month.

        Key attributes include:

        - **estimatedSalesLift**: The estimated increase in sales you could see if you converted the suggested items
            from seller-fulfilled to WFS.

        - **sellerFulfilledPast30DaysSales**: A historical view of your seller-fulfilled sales for the past 30 days.
        - **walmartFulfilledEstimatedSales**: An estimated view of your potential sales if the suggested items were
            fulfilled by WFS.

        You can use these suggestions to determine which items to convert to WFS.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wfs/recommendation/fulfil-with-wfs"),
            query_params=[
                param[bool | None]("customerFavorite", customer_favorite),
                param[bool | None]("showInsights", show_insights),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("sort_by", sort_by),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[bool | None]("showHiddenRecordsOnly", show_hidden_records_only),
            ],
            headers=[
                param[str]("Content-Type", content_type),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("wm_audit.origin_source", wm_audit_origin_source),
            ],
            decoder=json_decoder[V3WfsRecommendationFulfilWithWfsResponse],
            error_mapper=get_fulfill_with_wfsrecommendations_error_mapper,
            request_options=request_options,
        )

    def get_restock_recommendations(
        self,
        authorization: str,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = True,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "forecastedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationRestockResponse, GetRestockRecommendationsErrorBody]:
        """Use **Restock Recommendations** to get Walmart-generated suggestions for the items you should restock with
        WFS based on your current inventory and forecasted sales demand. These suggestions are available on demand. Key
        attributes include:

        - **suggestedUnits**: The number of units we suggest you send of this item to WFS
        - **forecastedSalesLift**: The estimated increase in sales you may see if your items are restocked according to
            our suggestions
        - **totalForecastedSalesLost**: How much money you're estimated to lose out on if you don't restock your
            inventory

        Once you determine which suggested items to restock, you can use the Create inbound shipment API to create a
        shipping plan to send inventory to WFS.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wfs/recommendation/restock"),
            query_params=[
                param[bool | None]("customerFavorite", customer_favorite),
                param[bool | None]("showInsights", show_insights),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("sort_by", sort_by),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[bool | None]("showHiddenRecordsOnly", show_hidden_records_only),
            ],
            headers=[
                param[str]("Authorization", authorization),
                param[str]("Content-Type", content_type),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("wm_audit.origin_source", wm_audit_origin_source),
            ],
            decoder=json_decoder[V3WfsRecommendationRestockResponse],
            error_mapper=get_restock_recommendations_error_mapper,
            request_options=request_options,
        )

    def get_shipment_quantity_recommendations(
        self,
        authorization: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        body: V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationShipmentQuantityResponse, GetShipmentQuantityRecommendationsErrorBody]:
        """Use this API to get recommended shipment quantities for the items that you plan to send to Walmart
        Fulfillment Services (WFS) in order to achieve optimal inventory levels.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            wm_sec_access_token: The access token retrieved in the Token API call <b style='color: green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <b style='color: green;'>Market availability: US only</b>
            wm_svc_name: Walmart Service Name. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Market identifier. <b style='color: green;'>Market availability: US only</b>
            body: Request body containing GTINs or SKUs to retrieve the quantity limit. <b style='color: green;'>Market
                availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/wfs/recommendation/shipment-quantity"),
            headers=[
                param[str]("Authorization", authorization),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict](
                body
            ),
            decoder=json_decoder[V3WfsRecommendationShipmentQuantityResponse],
            error_mapper=get_shipment_quantity_recommendations_error_mapper,
            request_options=request_options,
        )

    def get_unpublished_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationUnpublishedResponse, GetUnpublishedRecommendationsErrorBody]:
        """This call helps you identify the estimated storage fees with Walmart for your unpublished WFS items.

        Use **Unpublish Recommendations** to fetch a current list of your unpublished WFS items. This is available on
        demand.

        Key data attributes include:

        - **unpublishedIssue**: The reason your item is currently unpublished with Walmart.
        - **estimatedStorageFee**: The estimated storage costs associated with your unpublished WFS inventory.
        - **totalunpublishedunitsstored**: The total quantity of units in WFS fulfillment centers for unpublished items.

        Use this data to identify the reason these items are unpublished and the estimated costs associated with these
        unpublished items. By default, these suggestions will only include items that are active with an Available to
        Sell (ATS) quantity of 0.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wfs/recommendation/unpublished"),
            query_params=[
                param[bool | None]("customerFavorite", customer_favorite),
                param[bool | None]("showInsights", show_insights),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("sort_by", sort_by),
                param[SortOrderOrStr | None]("sort_order", sort_order),
            ],
            headers=[
                param[str]("Content-Type", content_type),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("wm_audit.origin_source", wm_audit_origin_source),
            ],
            decoder=json_decoder[V3WfsRecommendationUnpublishedResponse],
            error_mapper=get_unpublished_recommendations_error_mapper,
            request_options=request_options,
        )


class AsyncRecommendationsApiWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_fulfill_with_wfs_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationFulfilWithWfsResponse, GetFulfillWithWfsrecommendationsErrorBody]:
        """Use **Fulfill With WFS Recommendations** to identify which seller-fulfilled items in your catalog Walmart
        suggests could potentially perform best when fulfilled by WFS. These suggestions are available on demand, and
        suggestions are refreshed the 1st and 15th of each month.

        Key attributes include:

        - **estimatedSalesLift**: The estimated increase in sales you could see if you converted the suggested items
            from seller-fulfilled to WFS.

        - **sellerFulfilledPast30DaysSales**: A historical view of your seller-fulfilled sales for the past 30 days.
        - **walmartFulfilledEstimatedSales**: An estimated view of your potential sales if the suggested items were
            fulfilled by WFS.

        You can use these suggestions to determine which items to convert to WFS.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wfs/recommendation/fulfil-with-wfs"),
            query_params=[
                param[bool | None]("customerFavorite", customer_favorite),
                param[bool | None]("showInsights", show_insights),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("sort_by", sort_by),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[bool | None]("showHiddenRecordsOnly", show_hidden_records_only),
            ],
            headers=[
                param[str]("Content-Type", content_type),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("wm_audit.origin_source", wm_audit_origin_source),
            ],
            decoder=async_json_decoder[V3WfsRecommendationFulfilWithWfsResponse],
            error_mapper=get_fulfill_with_wfsrecommendations_error_mapper,
            request_options=request_options,
        )

    async def get_restock_recommendations(
        self,
        authorization: str,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = True,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "forecastedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        show_hidden_records_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationRestockResponse, GetRestockRecommendationsErrorBody]:
        """Use **Restock Recommendations** to get Walmart-generated suggestions for the items you should restock with
        WFS based on your current inventory and forecasted sales demand. These suggestions are available on demand. Key
        attributes include:

        - **suggestedUnits**: The number of units we suggest you send of this item to WFS
        - **forecastedSalesLift**: The estimated increase in sales you may see if your items are restocked according to
            our suggestions
        - **totalForecastedSalesLost**: How much money you're estimated to lose out on if you don't restock your
            inventory

        Once you determine which suggested items to restock, you can use the Create inbound shipment API to create a
        shipping plan to send inventory to WFS.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            show_hidden_records_only: Shows insights you have hidden. <b style='color: green;'>Market availability: US
                only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wfs/recommendation/restock"),
            query_params=[
                param[bool | None]("customerFavorite", customer_favorite),
                param[bool | None]("showInsights", show_insights),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("sort_by", sort_by),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[bool | None]("showHiddenRecordsOnly", show_hidden_records_only),
            ],
            headers=[
                param[str]("Authorization", authorization),
                param[str]("Content-Type", content_type),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("wm_audit.origin_source", wm_audit_origin_source),
            ],
            decoder=async_json_decoder[V3WfsRecommendationRestockResponse],
            error_mapper=get_restock_recommendations_error_mapper,
            request_options=request_options,
        )

    async def get_shipment_quantity_recommendations(
        self,
        authorization: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        body: V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationShipmentQuantityResponse, GetShipmentQuantityRecommendationsErrorBody]:
        """Use this API to get recommended shipment quantities for the items that you plan to send to Walmart
        Fulfillment Services (WFS) in order to achieve optimal inventory levels.

        Args:
            authorization: Basic authorization header. Base 64 encodes the Client ID and Client Secret retrieved in step
                two of the integration steps. <b style='color: green;'>Market availability: US only</b>
            wm_sec_access_token: The access token retrieved in the Token API call <b style='color: green;'>Market
                availability: US only</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <b style='color: green;'>Market availability: US only</b>
            wm_svc_name: Walmart Service Name. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Market identifier. <b style='color: green;'>Market availability: US only</b>
            body: Request body containing GTINs or SKUs to retrieve the quantity limit. <b style='color: green;'>Market
                availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/wfs/recommendation/shipment-quantity"),
            headers=[
                param[str]("Authorization", authorization),
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3WfsRecommendationShipmentQuantityRequest | V3WfsRecommendationShipmentQuantityRequestDict](
                body
            ),
            decoder=async_json_decoder[V3WfsRecommendationShipmentQuantityResponse],
            error_mapper=get_shipment_quantity_recommendations_error_mapper,
            request_options=request_options,
        )

    async def get_unpublished_recommendations(
        self,
        content_type: str,
        accept: str,
        wm_global_version: str,
        wm_market: str,
        wm_audit_origin_source: str,
        *,
        customer_favorite: bool | None = None,
        show_insights: bool | None = False,
        limit: int | None = 30,
        offset: int | None = 0,
        sort_by: str | None = "estimatedSalesLift",
        sort_order: SortOrderOrStr | None = SortOrder.DESC,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3WfsRecommendationUnpublishedResponse, GetUnpublishedRecommendationsErrorBody]:
        """This call helps you identify the estimated storage fees with Walmart for your unpublished WFS items.

        Use **Unpublish Recommendations** to fetch a current list of your unpublished WFS items. This is available on
        demand.

        Key data attributes include:

        - **unpublishedIssue**: The reason your item is currently unpublished with Walmart.
        - **estimatedStorageFee**: The estimated storage costs associated with your unpublished WFS inventory.
        - **totalunpublishedunitsstored**: The total quantity of units in WFS fulfillment centers for unpublished items.

        Use this data to identify the reason these items are unpublished and the estimated costs associated with these
        unpublished items. By default, these suggestions will only include items that are active with an Available to
        Sell (ATS) quantity of 0.

        Args:
            content_type: Specifies the literal **application/json**. This value identifies the content type of the
                request body. <b style='color: green;'>Market availability: US only</b>
            accept: Only supported Media Type : application/json. <b style='color: green;'>Market availability: US
                only</b>
            wm_global_version: Global version for API compatibility. <b style='color: green;'>Market availability: US
                only</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default. <b style='color: green;'>Market availability: US only</b>
            wm_audit_origin_source: Seller identifier. <b style='color: green;'>Market availability: US only</b>
            customer_favorite: Filters items by customer favorite status. When set to ``true``, only customer favorites
                are returned. When set to ``false``, only non-favorites are returned. If omitted, all items are
                returned.
            show_insights: Shows aggregate recommendation values for all items. <b style='color: green;'>Market
                availability: US only</b>
            limit: The maximum number of SKUs to include in the response (1–300). If you omit this parameter, Walmart
                returns up to 30 SKUs. <b style='color: green;'>Market availability: US only</b>
            offset: The number of SKUs to skip before Walmart starts listing results. Set to 0 to start at the first
                SKU. <b style='color: green;'>Market availability: US only</b>
            sort_by: The attribute to be used in sorting the response. <b style='color: green;'>Market availability: US
                only</b>
            sort_order: The order in which the response should be sorted. This can be in set to "ASC" or "DESC" order of
                value. Default is "DESC. <b style='color: green;'>Market availability: US only</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wfs/recommendation/unpublished"),
            query_params=[
                param[bool | None]("customerFavorite", customer_favorite),
                param[bool | None]("showInsights", show_insights),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
                param[str | None]("sort_by", sort_by),
                param[SortOrderOrStr | None]("sort_order", sort_order),
            ],
            headers=[
                param[str]("Content-Type", content_type),
                param[str]("Accept", accept),
                param[str]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_MARKET", wm_market),
                param[str]("wm_audit.origin_source", wm_audit_origin_source),
            ],
            decoder=async_json_decoder[V3WfsRecommendationUnpublishedResponse],
            error_mapper=get_unpublished_recommendations_error_mapper,
            request_options=request_options,
        )
