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
from ..errors.get_returns_error import GetReturnsErrorBody, get_returns_error_mapper
from ..errors.refund_request_error import RefundRequestErrorBody, refund_request_error_mapper
from ..errors.return_order_cursor_error import ReturnOrderCursorErrorBody, return_order_cursor_error_mapper
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.enums.wm_market3 import WmMarket3OrStr
from ..models.enums.wm_market21 import WmMarket21OrStr
from ..models.query_params import QueryParams, QueryParamsDict
from ..models.query_params_mx import QueryParamsMx, QueryParamsMxDict
from ..models.refund_request import RefundRequest, RefundRequestDict
from ..models.request import Request
from ..models.return_order_response import ReturnOrderResponse
from ..models.return_orders_responses import ReturnOrdersResponses
from ..server.server import Server


class ReturnsRefund:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReturnsRefundWithRawResponse(client, server, auth)

    def get_returns(
        self,
        query_params: QueryParams | QueryParamsDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReturnOrderResponse:
        """Retrieves the details of all return orders for the specified filter criteria.

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: BadRequest Unauthorized Forbidden Too Many Requests Internal Server ``error`` is ``ErrorResponse3
                | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError``."""
        return unwrap(
            self._with_raw_response.get_returns(
                query_params,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def refund_request(
        self,
        return_order_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket3OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: RefundRequest | RefundRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Request:
        """Refunds one or more order lines that have been shipped. The response to a successful call contains the order
        with the refunded line item.

        <br><b style='color:green;'>Market availability: US | MX</b>

        Args:
            return_order_id: Return order identifier of the return order object as part of array. This is the same as
                RMA number.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: US | MX</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: US | MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: BadRequest Unauthorized Forbidden Too Many Requests Internal Server ``error`` is ``ErrorResponse3
                | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError``."""
        return unwrap(
            self._with_raw_response.refund_request(
                return_order_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def return_order_cursor(
        self,
        query_params: QueryParamsMx | QueryParamsMxDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket21OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReturnOrdersResponses:
        """This API retrieves the details of all return orders based on the specified filter criteria and returns all
        orders in the response. It returns a nextCursorMark for the next 100 orders, and continues in this manner until
        the last order. The same API can also be used to search for a single order based on returnOrderId or
        customerOrderId.<br><b style='color:green;'>Market availability: MX</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request.<br><b style='color:green;'>Market
                availability: MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: BadRequest Unauthorized Forbidden Too Many Requests Internal Server ``error`` is ``ErrorResponse3
                | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError``."""
        return unwrap(
            self._with_raw_response.return_order_cursor(
                query_params,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ReturnsRefundWithRawResponse:
        return self._with_raw_response


class AsyncReturnsRefund:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReturnsRefundWithRawResponse(client, server, auth)

    async def get_returns(
        self,
        query_params: QueryParams | QueryParamsDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReturnOrderResponse:
        """Retrieves the details of all return orders for the specified filter criteria.

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: BadRequest Unauthorized Forbidden Too Many Requests Internal Server ``error`` is ``ErrorResponse3
                | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError``."""
        return unwrap(
            await self._with_raw_response.get_returns(
                query_params,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def refund_request(
        self,
        return_order_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket3OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: RefundRequest | RefundRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Request:
        """Refunds one or more order lines that have been shipped. The response to a successful call contains the order
        with the refunded line item.

        <br><b style='color:green;'>Market availability: US | MX</b>

        Args:
            return_order_id: Return order identifier of the return order object as part of array. This is the same as
                RMA number.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: US | MX</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: US | MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: BadRequest Unauthorized Forbidden Too Many Requests Internal Server ``error`` is ``ErrorResponse3
                | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError``."""
        return unwrap(
            await self._with_raw_response.refund_request(
                return_order_id,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def return_order_cursor(
        self,
        query_params: QueryParamsMx | QueryParamsMxDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket21OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReturnOrdersResponses:
        """This API retrieves the details of all return orders based on the specified filter criteria and returns all
        orders in the response. It returns a nextCursorMark for the next 100 orders, and continues in this manner until
        the last order. The same API can also be used to search for a single order based on returnOrderId or
        customerOrderId.<br><b style='color:green;'>Market availability: MX</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request.<br><b style='color:green;'>Market
                availability: MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            success

        Raises:
            ApiError: BadRequest Unauthorized Forbidden Too Many Requests Internal Server ``error`` is ``ErrorResponse3
                | Unauthorized1 | Forbidden1 | TooManyRequests1 | ErrorResponses | RawError``."""
        return unwrap(
            await self._with_raw_response.return_order_cursor(
                query_params,
                wm_qos_correlation_id,
                wm_svc_name,
                wm_market,
                wm_global_version,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncReturnsRefundWithRawResponse:
        return self._with_raw_response


class ReturnsRefundWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_returns(
        self,
        query_params: QueryParams | QueryParamsDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReturnOrderResponse, GetReturnsErrorBody]:
        """Retrieves the details of all return orders for the specified filter criteria.

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/returns"),
            query_params=[param[QueryParams | QueryParamsDict]("Query Params", query_params)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[ReturnOrderResponse],
            error_mapper=get_returns_error_mapper,
            request_options=request_options,
        )

    def refund_request(
        self,
        return_order_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket3OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: RefundRequest | RefundRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Request, RefundRequestErrorBody]:
        """Refunds one or more order lines that have been shipped. The response to a successful call contains the order
        with the refunded line item.

        <br><b style='color:green;'>Market availability: US | MX</b>

        Args:
            return_order_id: Return order identifier of the return order object as part of array. This is the same as
                RMA number.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: US | MX</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: US | MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/returns/{returnOrderId}/refund"),
            path_params=[param[str]("returnOrderId", return_order_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket3OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[RefundRequest | RefundRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[Request],
            error_mapper=refund_request_error_mapper,
            request_options=request_options,
        )

    def return_order_cursor(
        self,
        query_params: QueryParamsMx | QueryParamsMxDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket21OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReturnOrdersResponses, ReturnOrderCursorErrorBody]:
        """This API retrieves the details of all return orders based on the specified filter criteria and returns all
        orders in the response. It returns a nextCursorMark for the next 100 orders, and continues in this manner until
        the last order. The same API can also be used to search for a single order based on returnOrderId or
        customerOrderId.<br><b style='color:green;'>Market availability: MX</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request.<br><b style='color:green;'>Market
                availability: MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/returns/cursor"),
            query_params=[param[QueryParamsMx | QueryParamsMxDict]("Query Params", query_params)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket21OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[ReturnOrdersResponses],
            error_mapper=return_order_cursor_error_mapper,
            request_options=request_options,
        )


class AsyncReturnsRefundWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_returns(
        self,
        query_params: QueryParams | QueryParamsDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReturnOrderResponse, GetReturnsErrorBody]:
        """Retrieves the details of all return orders for the specified filter criteria.

        <br><b style='color:green;'>Market availability: Global</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: Global</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: Global</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: Global</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/returns"),
            query_params=[param[QueryParams | QueryParamsDict]("Query Params", query_params)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[ReturnOrderResponse],
            error_mapper=get_returns_error_mapper,
            request_options=request_options,
        )

    async def refund_request(
        self,
        return_order_id: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket3OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: RefundRequest | RefundRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Request, RefundRequestErrorBody]:
        """Refunds one or more order lines that have been shipped. The response to a successful call contains the order
        with the refunded line item.

        <br><b style='color:green;'>Market availability: US | MX</b>

        Args:
            return_order_id: Return order identifier of the return order object as part of array. This is the same as
                RMA number.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: US | MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request. If not specified, US is used by
                default.<br><b style='color:green;'>Market availability: US | MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: US | MX</b>
            body: The request body.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: US | MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/returns/{returnOrderId}/refund"),
            path_params=[param[str]("returnOrderId", return_order_id)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket3OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[RefundRequest | RefundRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[Request],
            error_mapper=refund_request_error_mapper,
            request_options=request_options,
        )

    async def return_order_cursor(
        self,
        query_params: QueryParamsMx | QueryParamsMxDict,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket21OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReturnOrdersResponses, ReturnOrderCursorErrorBody]:
        """This API retrieves the details of all return orders based on the specified filter criteria and returns all
        orders in the response. It returns a nextCursorMark for the next 100 orders, and continues in this manner until
        the last order. The same API can also be used to search for a single order based on returnOrderId or
        customerOrderId.<br><b style='color:green;'>Market availability: MX</b>

        Args:
            query_params: Value sent with the request.
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. Example: b3261d2d-028a-4ef7-8602-633c23200af6<br><b
                style='color:green;'>Market availability: MX</b>
            wm_svc_name: Specifies the name of the Walmart service being called. Example: Walmart Marketplace<br><b
                style='color:green;'>Market availability: MX</b>
            wm_market: Identifies the Walmart Marketplace region for the request.<br><b style='color:green;'>Market
                availability: MX</b>
            wm_global_version: Indicates the global version of the API. The value must be set to 3.1.<br><b
                style='color:green;'>Market availability: MX</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the Consumer Channel
                Type received during onboarding.<br><b style='color:green;'>Market availability: MX</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/returns/cursor"),
            query_params=[param[QueryParamsMx | QueryParamsMxDict]("Query Params", query_params)],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket21OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[ReturnOrdersResponses],
            error_mapper=return_order_cursor_error_mapper,
            request_options=request_options,
        )
