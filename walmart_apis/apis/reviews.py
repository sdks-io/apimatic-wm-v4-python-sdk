from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.bulk_update_item_status_error import BulkUpdateItemStatusErrorBody, bulk_update_item_status_error_mapper
from ..errors.get_irp_categories_error import GetIrpCategoriesErrorBody, get_irp_categories_error_mapper
from ..errors.get_irp_items_error import GetIrpItemsErrorBody, get_irp_items_error_mapper
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.v3_growth_reviews_accelerator_categories_request import (
    V3GrowthReviewsAcceleratorCategoriesRequest,
    V3GrowthReviewsAcceleratorCategoriesRequestDict,
)
from ..models.v3_growth_reviews_accelerator_categories_response import V3GrowthReviewsAcceleratorCategoriesResponse
from ..models.v3_growth_reviews_accelerator_items_request import (
    V3GrowthReviewsAcceleratorItemsRequest,
    V3GrowthReviewsAcceleratorItemsRequestDict,
)
from ..models.v3_growth_reviews_accelerator_items_response import V3GrowthReviewsAcceleratorItemsResponse
from ..models.v3_growth_reviews_accelerator_items_status_request import (
    V3GrowthReviewsAcceleratorItemsStatusRequest,
    V3GrowthReviewsAcceleratorItemsStatusRequestDict,
)
from ..models.v3_growth_reviews_accelerator_items_status_response import V3GrowthReviewsAcceleratorItemsStatusResponse
from ..server.server import Server


class Reviews:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReviewsWithRawResponse(client, server, auth)

    def bulk_update_item_status(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthReviewsAcceleratorItemsStatusResponse:
        """Use this API to enroll or disenroll items in the Review Accelerator Program (RAP).<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal server error ``error`` is
                ``V3GrowthReviewsAcceleratorItemsStatus400Error1 | V3GrowthReviewsAcceleratorItemsStatus401Error1 |
                V3GrowthReviewsAcceleratorItemsStatus403Error1 | V3GrowthReviewsAcceleratorItemsStatus500Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.bulk_update_item_status(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_irp_categories(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthReviewsAcceleratorCategoriesResponse:
        """Use this API to get the set of categories the RAP post-purchase items belong to.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal server error ``error`` is
                ``V3GrowthReviewsAcceleratorCategories400Error1 | V3GrowthReviewsAcceleratorCategories401Error1 |
                V3GrowthReviewsAcceleratorCategories403Error1 | V3InsightsItemsListingQualityItems500Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_irp_categories(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def get_irp_items(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict,
        *,
        scroll_id: str = "*",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthReviewsAcceleratorItemsResponse:
        """To get all eligible products that can be enrolled in the Reviews Accelerator post-purchase program, as well
        as to retrieve all products currently enrolled in the program, and all products that have attained target
        reviews after enrollment, you can use the following criteria: <li>Filter products by category and price.
        <li>Sort products by Walmart-recommended item priorities. <li>Search using wildcards to match the product name
        and SKU.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.1<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            scroll_id: Optional parameter specifying the scrollId to return the next set of results.<br><b
                style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal server error ``error`` is
                ``V3GrowthReviewsAcceleratorItems400Error1 | V3GrowthReviewsAcceleratorItems401Error1 |
                V3GrowthReviewsAcceleratorItems403Error1 | V3InsightsItemsListingQualityItems500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_irp_items(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                scroll_id=scroll_id,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ReviewsWithRawResponse:
        return self._with_raw_response


class AsyncReviews:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReviewsWithRawResponse(client, server, auth)

    async def bulk_update_item_status(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthReviewsAcceleratorItemsStatusResponse:
        """Use this API to enroll or disenroll items in the Review Accelerator Program (RAP).<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal server error ``error`` is
                ``V3GrowthReviewsAcceleratorItemsStatus400Error1 | V3GrowthReviewsAcceleratorItemsStatus401Error1 |
                V3GrowthReviewsAcceleratorItemsStatus403Error1 | V3GrowthReviewsAcceleratorItemsStatus500Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_update_item_status(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_irp_categories(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthReviewsAcceleratorCategoriesResponse:
        """Use this API to get the set of categories the RAP post-purchase items belong to.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal server error ``error`` is
                ``V3GrowthReviewsAcceleratorCategories400Error1 | V3GrowthReviewsAcceleratorCategories401Error1 |
                V3GrowthReviewsAcceleratorCategories403Error1 | V3InsightsItemsListingQualityItems500Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_irp_categories(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def get_irp_items(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict,
        *,
        scroll_id: str = "*",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3GrowthReviewsAcceleratorItemsResponse:
        """To get all eligible products that can be enrolled in the Reviews Accelerator post-purchase program, as well
        as to retrieve all products currently enrolled in the program, and all products that have attained target
        reviews after enrollment, you can use the following criteria: <li>Filter products by category and price.
        <li>Sort products by Walmart-recommended item priorities. <li>Search using wildcards to match the product name
        and SKU.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.1<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            scroll_id: Optional parameter specifying the scrollId to return the next set of results.<br><b
                style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Unauthorized Forbidden - Unsupported Market Internal server error ``error`` is
                ``V3GrowthReviewsAcceleratorItems400Error1 | V3GrowthReviewsAcceleratorItems401Error1 |
                V3GrowthReviewsAcceleratorItems403Error1 | V3InsightsItemsListingQualityItems500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_irp_items(
                wm_global_version,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                body,
                scroll_id=scroll_id,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncReviewsWithRawResponse:
        return self._with_raw_response


class ReviewsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_update_item_status(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthReviewsAcceleratorItemsStatusResponse, BulkUpdateItemStatusErrorBody]:
        """Use this API to enroll or disenroll items in the Review Accelerator Program (RAP).<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/growth/reviews-accelerator/items/status"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict
            ](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3GrowthReviewsAcceleratorItemsStatusResponse],
            error_mapper=bulk_update_item_status_error_mapper,
            request_options=request_options,
        )

    def get_irp_categories(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthReviewsAcceleratorCategoriesResponse, GetIrpCategoriesErrorBody]:
        """Use this API to get the set of categories the RAP post-purchase items belong to.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/reviews-accelerator/categories"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict
            ](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3GrowthReviewsAcceleratorCategoriesResponse],
            error_mapper=get_irp_categories_error_mapper,
            request_options=request_options,
        )

    def get_irp_items(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict,
        *,
        scroll_id: str = "*",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthReviewsAcceleratorItemsResponse, GetIrpItemsErrorBody]:
        """To get all eligible products that can be enrolled in the Reviews Accelerator post-purchase program, as well
        as to retrieve all products currently enrolled in the program, and all products that have attained target
        reviews after enrollment, you can use the following criteria: <li>Filter products by category and price.
        <li>Sort products by Walmart-recommended item priorities. <li>Search using wildcards to match the product name
        and SKU.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.1<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            scroll_id: Optional parameter specifying the scrollId to return the next set of results.<br><b
                style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/reviews-accelerator/items"),
            query_params=[param[str]("scrollId", scroll_id)],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[V3GrowthReviewsAcceleratorItemsResponse],
            error_mapper=get_irp_items_error_mapper,
            request_options=request_options,
        )


class AsyncReviewsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_update_item_status(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthReviewsAcceleratorItemsStatusResponse, BulkUpdateItemStatusErrorBody]:
        """Use this API to enroll or disenroll items in the Review Accelerator Program (RAP).<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request fields
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v3/growth/reviews-accelerator/items/status"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3GrowthReviewsAcceleratorItemsStatusRequest | V3GrowthReviewsAcceleratorItemsStatusRequestDict
            ](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3GrowthReviewsAcceleratorItemsStatusResponse],
            error_mapper=bulk_update_item_status_error_mapper,
            request_options=request_options,
        )

    async def get_irp_categories(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthReviewsAcceleratorCategoriesResponse, GetIrpCategoriesErrorBody]:
        """Use this API to get the set of categories the RAP post-purchase items belong to.<br><b
        style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/reviews-accelerator/categories"),
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3GrowthReviewsAcceleratorCategoriesRequest | V3GrowthReviewsAcceleratorCategoriesRequestDict
            ](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3GrowthReviewsAcceleratorCategoriesResponse],
            error_mapper=get_irp_categories_error_mapper,
            request_options=request_options,
        )

    async def get_irp_items(
        self,
        wm_global_version: WmGlobalVersionOrStr,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        body: V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict,
        *,
        scroll_id: str = "*",
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3GrowthReviewsAcceleratorItemsResponse, GetIrpItemsErrorBody]:
        """To get all eligible products that can be enrolled in the Reviews Accelerator post-purchase program, as well
        as to retrieve all products currently enrolled in the program, and all products that have attained target
        reviews after enrollment, you can use the following criteria: <li>Filter products by category and price.
        <li>Sort products by Walmart-recommended item priorities. <li>Search using wildcards to match the product name
        and SKU.<br><b style='color:green;'>Market availability: US only</b>

        Args:
            wm_global_version: Indicates the global version of the API. The default is set to 3.1.1<br><b
                style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            body: Request payload
            scroll_id: Optional parameter specifying the scrollId to return the next set of results.<br><b
                style='color:green;'>Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/growth/reviews-accelerator/items"),
            query_params=[param[str]("scrollId", scroll_id)],
            headers=[
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3GrowthReviewsAcceleratorItemsRequest | V3GrowthReviewsAcceleratorItemsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[V3GrowthReviewsAcceleratorItemsResponse],
            error_mapper=get_irp_items_error_mapper,
            request_options=request_options,
        )
