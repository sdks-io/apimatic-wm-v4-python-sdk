from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..errors.get_lag_time_error import GetLagTimeErrorBody, get_lag_time_error_mapper
from ..models.enums.wm_global_version import WmGlobalVersionOrStr
from ..models.enums.wm_market1 import WmMarket1OrStr
from ..models.feed_id1 import FeedId1
from ..models.lag_time_response import LagTimeResponse
from ..models.v3_feeds_request import V3FeedsRequest, V3FeedsRequestDict
from ..server.server import Server


class LagTimeApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LagTimeApiWithRawResponse(client, server, auth)

    def get_lag_time(
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
    ) -> LagTimeResponse:
        """Use this API to retrieve the lag time for a specific item using its SKU.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</strong>

        Args:
            sku: A unique alphanumeric ID assigned by the seller to identify each item. The seller uses this ID in the
                XSD file to reference specific items. If the SKU contains any of the following special characters — :,
                /, ?, #, [, ], @, !, $, &, ', (, ), *, +, ,, ;, =, space, {, }, or % — they must be URL-encoded. For
                example, encode spaces as %20. No encoding is required for other characters. <strong style="color:
                green;">Market availability: Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``V3Lagtime400Error1 | V3Lagtime404Error1
                | V3Lagtime500Error1 | RawError``."""
        return unwrap(
            self._with_raw_response.get_lag_time(
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

    def update_lag_time_bulk(
        self,
        feed_type: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest | V3FeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """Use this API to update lag time for multiple items at once.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: Indicates the feed type. Use 'lagtime'. <strong style="color: green;">Market availability:
                Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_lag_time_bulk(
                feed_type,
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
    def with_raw_response(self) -> LagTimeApiWithRawResponse:
        return self._with_raw_response


class AsyncLagTimeApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLagTimeApiWithRawResponse(client, server, auth)

    async def get_lag_time(
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
    ) -> LagTimeResponse:
        """Use this API to retrieve the lag time for a specific item using its SKU.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</strong>

        Args:
            sku: A unique alphanumeric ID assigned by the seller to identify each item. The seller uses this ID in the
                XSD file to reference specific items. If the SKU contains any of the following special characters — :,
                /, ?, #, [, ], @, !, $, &, ', (, ), *, +, ,, ;, =, space, {, }, or % — they must be URL-encoded. For
                example, encode spaces as %20. No encoding is required for other characters. <strong style="color:
                green;">Market availability: Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``V3Lagtime400Error1 | V3Lagtime404Error1
                | V3Lagtime500Error1 | RawError``."""
        return unwrap(
            await self._with_raw_response.get_lag_time(
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

    async def update_lag_time_bulk(
        self,
        feed_type: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest | V3FeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """Use this API to update lag time for multiple items at once.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: Indicates the feed type. Use 'lagtime'. <strong style="color: green;">Market availability:
                Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful Operation

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_lag_time_bulk(
                feed_type,
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
    def with_raw_response(self) -> AsyncLagTimeApiWithRawResponse:
        return self._with_raw_response


class LagTimeApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_lag_time(
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
    ) -> ApiResult[LagTimeResponse, GetLagTimeErrorBody]:
        """Use this API to retrieve the lag time for a specific item using its SKU.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</strong>

        Args:
            sku: A unique alphanumeric ID assigned by the seller to identify each item. The seller uses this ID in the
                XSD file to reference specific items. If the SKU contains any of the following special characters — :,
                /, ?, #, [, ], @, !, $, &, ', (, ), *, +, ,, ;, =, space, {, }, or % — they must be URL-encoded. For
                example, encode spaces as %20. No encoding is required for other characters. <strong style="color:
                green;">Market availability: Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/lagtime"),
            query_params=[param[str]("sku", sku)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[LagTimeResponse],
            error_mapper=get_lag_time_error_mapper,
            request_options=request_options,
        )

    def update_lag_time_bulk(
        self,
        feed_type: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest | V3FeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, RawError]:
        """Use this API to update lag time for multiple items at once.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: Indicates the feed type. Use 'lagtime'. <strong style="color: green;">Market availability:
                Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds"),
            query_params=[param[str]("feedType", feed_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsRequest | V3FeedsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedId1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLagTimeApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_lag_time(
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
    ) -> ApiResult[LagTimeResponse, GetLagTimeErrorBody]:
        """Use this API to retrieve the lag time for a specific item using its SKU.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</strong>

        Args:
            sku: A unique alphanumeric ID assigned by the seller to identify each item. The seller uses this ID in the
                XSD file to reference specific items. If the SKU contains any of the following special characters — :,
                /, ?, #, [, ], @, !, $, &, ', (, ), *, +, ,, ;, =, space, {, }, or % — they must be URL-encoded. For
                example, encode spaces as %20. No encoding is required for other characters. <strong style="color:
                green;">Market availability: Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/lagtime"),
            query_params=[param[str]("sku", sku)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[LagTimeResponse],
            error_mapper=get_lag_time_error_mapper,
            request_options=request_options,
        )

    async def update_lag_time_bulk(
        self,
        feed_type: str,
        wm_sec_access_token: str,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        wm_market: WmMarket1OrStr,
        wm_global_version: WmGlobalVersionOrStr,
        body: V3FeedsRequest | V3FeedsRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, RawError]:
        """Use this API to update lag time for multiple items at once.

        Lag Time represents the number of days between when an item is ordered and when it is shipped. Approval
        thresholds and exemption processes for higher lag times vary by market. For more details, refer to the relevant
        market-specific knowledge article. <br><b style='color:green;'>Market availability: Global</b>

        Args:
            feed_type: Indicates the feed type. Use 'lagtime'. <strong style="color: green;">Market availability:
                Global</strong>
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
            wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel
                Type received during onboarding. <strong style="color: green;">Market availability: Global</strong>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds"),
            query_params=[param[str]("feedType", feed_type)],
            headers=[
                param[str]("WM_SEC.ACCESS_TOKEN", wm_sec_access_token),
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[WmMarket1OrStr]("WM_MARKET", wm_market),
                param[WmGlobalVersionOrStr]("WM_GLOBAL_VERSION", wm_global_version),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[V3FeedsRequest | V3FeedsRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedId1],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
