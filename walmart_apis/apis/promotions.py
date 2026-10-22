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
from ..errors.get_promotional_prices_error import GetPromotionalPricesErrorBody, get_promotional_prices_error_mapper
from ..errors.price_bulk_uploads_error import PriceBulkUploadsErrorBody, price_bulk_uploads_error_mapper
from ..errors.update_promotional_prices_error import (
    UpdatePromotionalPricesErrorBody,
    update_promotional_prices_error_mapper,
)
from ..models.enums.feed_type21 import FeedType21OrStr
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.feed_id1 import FeedId1
from ..models.v3_feeds_feed_type_price_and_promotion_request1 import (
    V3FeedsFeedTypePriceAndPromotionRequest1,
    V3FeedsFeedTypePriceAndPromotionRequest1Dict,
)
from ..models.v3_price_request import V3PriceRequest, V3PriceRequestDict
from ..models.v3_price_response import V3PriceResponse
from ..models.v3_promo_sku_response import V3PromoSkuResponse
from ..server.server import Server


class Promotions:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = PromotionsWithRawResponse(client, server)

    def get_promotional_prices(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PromoSkuResponse:
        """Retrieves a list of promotional prices for a single SKU.<br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', as well as '%'
                itself. Other characters don't need to be encoded.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized ``error`` is ``V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_promotional_prices(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def price_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """The price and promotional price API allows you to creates, updates, or deletes promotional prices for
        multiple SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type. <br><b style='color:green;'>Market availability: Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Internal Server Error ``error`` is ``V3Token500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.price_bulk_uploads(
                feed_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    def update_promotional_prices(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceResponse:
        """The update a promotional price API allows you to creates, updates, or deletes promotional prices for single
        SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            body: The request body consists of a Feed file attached to the request.<br><b style='color:green;'>Market
                availability: CA | MX | CL</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token500Error1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.update_promotional_prices(
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
    def with_raw_response(self) -> PromotionsWithRawResponse:
        return self._with_raw_response


class AsyncPromotions:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncPromotionsWithRawResponse(client, server)

    async def get_promotional_prices(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PromoSkuResponse:
        """Retrieves a list of promotional prices for a single SKU.<br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', as well as '%'
                itself. Other characters don't need to be encoded.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized ``error`` is ``V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_promotional_prices(
                sku,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def price_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """The price and promotional price API allows you to creates, updates, or deletes promotional prices for
        multiple SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type. <br><b style='color:green;'>Market availability: Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Unauthorized Internal Server Error ``error`` is ``V3Token500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.price_bulk_uploads(
                feed_type,
                wm_sec_access_token,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                body=body,
                request_options=request_options,
            ),
        )

    async def update_promotional_prices(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3PriceResponse:
        """The update a promotional price API allows you to creates, updates, or deletes promotional prices for single
        SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            body: The request body consists of a Feed file attached to the request.<br><b style='color:green;'>Market
                availability: CA | MX | CL</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Forbidden - Unsupported Market Internal Server Error ``error`` is ``V3Token500Error1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.update_promotional_prices(
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
    def with_raw_response(self) -> AsyncPromotionsWithRawResponse:
        return self._with_raw_response


class PromotionsWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_promotional_prices(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PromoSkuResponse, GetPromotionalPricesErrorBody]:
        """Retrieves a list of promotional prices for a single SKU.<br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', as well as '%'
                itself. Other characters don't need to be encoded.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/promo/sku/{sku}"),
            path_params=[param[str]("sku", sku)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=json_decoder[V3PromoSkuResponse],
            error_mapper=get_promotional_prices_error_mapper,
            request_options=request_options,
        )

    def price_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, PriceBulkUploadsErrorBody]:
        """The price and promotional price API allows you to creates, updates, or deletes promotional prices for
        multiple SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type. <br><b style='color:green;'>Market availability: Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=PRICE_AND_PROMOTION"),
            query_params=[param[FeedType21OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None
            ](body),
            decoder=json_decoder[FeedId1],
            error_mapper=price_bulk_uploads_error_mapper,
            request_options=request_options,
        )

    def update_promotional_prices(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceResponse, UpdatePromotionalPricesErrorBody]:
        """The update a promotional price API allows you to creates, updates, or deletes promotional prices for single
        SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            body: The request body consists of a Feed file attached to the request.<br><b style='color:green;'>Market
                availability: CA | MX | CL</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/price"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3PriceRequest | V3PriceRequestDict](body),
            decoder=json_decoder[V3PriceResponse],
            error_mapper=update_promotional_prices_error_mapper,
            request_options=request_options,
        )


class AsyncPromotionsWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_promotional_prices(
        self,
        sku: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PromoSkuResponse, GetPromotionalPricesErrorBody]:
        """Retrieves a list of promotional prices for a single SKU.<br><b style='color:green;'>Market availability:
        Global</b>

        Args:
            sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be
                used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding
                are: ':', '?', '#', '[', ']', '@', '!', '$', '&', "'", '(', ')', '*', '+', ',', ';', '=', as well as '%'
                itself. Other characters don't need to be encoded.<br><b style='color:green;'>Market availability:
                Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/promo/sku/{sku}"),
            path_params=[param[str]("sku", sku)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            decoder=async_json_decoder[V3PromoSkuResponse],
            error_mapper=get_promotional_prices_error_mapper,
            request_options=request_options,
        )

    async def price_bulk_uploads(
        self,
        feed_type: FeedType21OrStr,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        body: V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, PriceBulkUploadsErrorBody]:
        """The price and promotional price API allows you to creates, updates, or deletes promotional prices for
        multiple SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: The feed Type. <br><b style='color:green;'>Market availability: Global</b>
            wm_sec_access_token: The access token retrieved in the Token API call. <br><b style='color:green;'>Market
                availability: Global</b>
            wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a
                random generated GUID for this ID. <br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Walmart Service Name. <br><b style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <br><b style='color:green;'>Market availability: Global</b>
            body: The request body consists of a Feed file attached to the request based on the feedType selected
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=PRICE_AND_PROMOTION"),
            query_params=[param[FeedType21OrStr]("feedType", feed_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[
                V3FeedsFeedTypePriceAndPromotionRequest1 | V3FeedsFeedTypePriceAndPromotionRequest1Dict | None
            ](body),
            decoder=async_json_decoder[FeedId1],
            error_mapper=price_bulk_uploads_error_mapper,
            request_options=request_options,
        )

    async def update_promotional_prices(
        self,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3PriceRequest | V3PriceRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3PriceResponse, UpdatePromotionalPricesErrorBody]:
        """The update a promotional price API allows you to creates, updates, or deletes promotional prices for single
        SKUs

        To set a new promotional price, set the "promotionSettingAction" attribute to "Create". To update an existing
        one, set the "promotionSettingAction" attribute to "Create" with promoId. To delete a promotional price, set the
        "promotionSettingAction" attribute to "Delete". To delete all promotions for a SKU, set the
        "promotionSettingAction" attribute to "Replace All"

         Please Note:
        - The effective start date for a given promotion should be within 365 days from the current date and time.
        - The end date of a given promotion should be within 180 days from the start date and time. Any promotions
            beyond 180 days will result in an error <br><b style='color:green;'>Market availability: CA | MX | CL</b>

        Args:
            wm_sec_access_token: Access token obtained from the Token API. Required for authenticating requests to
                Walmart Marketplace APIs.<br><b style='color:green;'>Market availability: Global</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID.<br><b style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called.<br><b style='color:green;'>Market
                availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Global Version is set to 3.1 by default. <br><b style='color:green;'>Market availability:
                Global</b>
            body: The request body consists of a Feed file attached to the request.<br><b style='color:green;'>Market
                availability: CA | MX | CL</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel.<br><b
                style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/price"),
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3PriceRequest | V3PriceRequestDict](body),
            decoder=async_json_decoder[V3PriceResponse],
            error_mapper=update_promotional_prices_error_mapper,
            request_options=request_options,
        )
