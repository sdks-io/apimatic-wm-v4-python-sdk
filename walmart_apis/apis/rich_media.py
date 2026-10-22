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
from ..errors.get_all_assets_error import GetAllAssetsErrorBody, get_all_assets_error_mapper
from ..errors.rich_media_operation_error import RichMediaOperationErrorBody, rich_media_operation_error_mapper
from ..models.assets_response import AssetsResponse
from ..models.enums.rich_media_type import RichMediaTypeOrStr
from ..models.feed_id1 import FeedId1
from ..models.rich_media_feed_request import RichMediaFeedRequest, RichMediaFeedRequestDict
from ..server.server import Server


class RichMedia:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RichMediaWithRawResponse(client, server, auth)

    def get_all_assets(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        page: int | None = 1,
        limit: int | None = 25,
        linked_gtins: list[str] | None = None,
        rich_media_title: str | None = None,
        rich_media_type: RichMediaTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssetsResponse:
        """Use this API to retrieve rich media assets, including 360-spin images and videos, from the seller catalog.
        Assets can be created in seller center media library or programmatically through the API. Use this endpoint to
        retrieve the asset hash, which uniquely identifies each media asset for future management.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            page: Indicates the page number to return in the paginated result set. Use this parameter to navigate
                through multiple pages of results. The value should be a positive integer. For example, 1 for the first
                page, 2 for the second, and so on. <b style="color: green;">Market availability: US only</b>
            limit: Defines the maximum number of items to return per page when retrieving paginated data. Use this
                parameter to control the number of results included in a single page. The value should be a positive
                integer. <b style="color: green;">Market availability: US only</b>
            linked_gtins: Filters assets by linked GTIN. Provide multiple GTINs as a list. If omitted, all assets are
                returned. <b style="color: green;">Market availability: US only</b>
            rich_media_title: Filters assets by rich media title or asset title. If omitted, all assets are returned. <b
                style="color: green;">Market availability: US only</b>
            rich_media_type: Filters assets by rich media type. Allowed values: ``IMAGES360``, ``VIDEO``. <b
                style="color: green;">Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation. Returns matching rich media assets. When no items match the query, the response
            contains an empty payload and total records as 0.

        Raises:
            ApiError: Bad request — A required parameter is missing or a supplied value is invalid. Unauthorized —
                Missing, invalid, or expired bearer token. Forbidden — Seller access is not authorized Not found - No
                asset matched the provided filter. Rate limit exceeded - Too many requests that exceeds limit. Internal
                server error ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_all_assets(
                wm_qos_correlation_id,
                wm_svc_name,
                page=page,
                limit=limit,
                linked_gtins=linked_gtins,
                rich_media_title=rich_media_title,
                rich_media_type=rich_media_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    def rich_media_operation(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: RichMediaFeedRequest | RichMediaFeedRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """Use this API to create, update, or delink rich media assets for items in the seller catalog. Supported asset
        types are ``IMAGES360`` and ``VIDEO``. Use this API to 1) add new rich media, 2) update associations for
        existing rich media, or 3) delink item association on existing rich media. Provide accessible media URLs and
        related metadata in the request body. Video assets require one video URL. 360-spin image assets require 24 image
        URLs.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            body: Rich media feed payload containing asset metadata, item associations, and media URLs.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful — The feed accepted and queued for processing

        Raises:
            ApiError: Bad request — The feed payload is invalid or a required field is missing. Unauthorized — Missing,
                invalid, or expired bearer token. Forbidden — Seller access is not authorized Rate limit exceeded - Too
                many requests that exceeds limit. Internal server error ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.rich_media_operation(
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> RichMediaWithRawResponse:
        return self._with_raw_response


class AsyncRichMedia:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRichMediaWithRawResponse(client, server, auth)

    async def get_all_assets(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        page: int | None = 1,
        limit: int | None = 25,
        linked_gtins: list[str] | None = None,
        rich_media_title: str | None = None,
        rich_media_type: RichMediaTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssetsResponse:
        """Use this API to retrieve rich media assets, including 360-spin images and videos, from the seller catalog.
        Assets can be created in seller center media library or programmatically through the API. Use this endpoint to
        retrieve the asset hash, which uniquely identifies each media asset for future management.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            page: Indicates the page number to return in the paginated result set. Use this parameter to navigate
                through multiple pages of results. The value should be a positive integer. For example, 1 for the first
                page, 2 for the second, and so on. <b style="color: green;">Market availability: US only</b>
            limit: Defines the maximum number of items to return per page when retrieving paginated data. Use this
                parameter to control the number of results included in a single page. The value should be a positive
                integer. <b style="color: green;">Market availability: US only</b>
            linked_gtins: Filters assets by linked GTIN. Provide multiple GTINs as a list. If omitted, all assets are
                returned. <b style="color: green;">Market availability: US only</b>
            rich_media_title: Filters assets by rich media title or asset title. If omitted, all assets are returned. <b
                style="color: green;">Market availability: US only</b>
            rich_media_type: Filters assets by rich media type. Allowed values: ``IMAGES360``, ``VIDEO``. <b
                style="color: green;">Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation. Returns matching rich media assets. When no items match the query, the response
            contains an empty payload and total records as 0.

        Raises:
            ApiError: Bad request — A required parameter is missing or a supplied value is invalid. Unauthorized —
                Missing, invalid, or expired bearer token. Forbidden — Seller access is not authorized Not found - No
                asset matched the provided filter. Rate limit exceeded - Too many requests that exceeds limit. Internal
                server error ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_all_assets(
                wm_qos_correlation_id,
                wm_svc_name,
                page=page,
                limit=limit,
                linked_gtins=linked_gtins,
                rich_media_title=rich_media_title,
                rich_media_type=rich_media_type,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    async def rich_media_operation(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: RichMediaFeedRequest | RichMediaFeedRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FeedId1:
        """Use this API to create, update, or delink rich media assets for items in the seller catalog. Supported asset
        types are ``IMAGES360`` and ``VIDEO``. Use this API to 1) add new rich media, 2) update associations for
        existing rich media, or 3) delink item association on existing rich media. Provide accessible media URLs and
        related metadata in the request body. Video assets require one video URL. 360-spin image assets require 24 image
        URLs.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            body: Rich media feed payload containing asset metadata, item associations, and media URLs.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful — The feed accepted and queued for processing

        Raises:
            ApiError: Bad request — The feed payload is invalid or a required field is missing. Unauthorized — Missing,
                invalid, or expired bearer token. Forbidden — Seller access is not authorized Rate limit exceeded - Too
                many requests that exceeds limit. Internal server error ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.rich_media_operation(
                wm_qos_correlation_id,
                wm_svc_name,
                body,
                wm_consumer_channel_type=wm_consumer_channel_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncRichMediaWithRawResponse:
        return self._with_raw_response


class RichMediaWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_all_assets(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        page: int | None = 1,
        limit: int | None = 25,
        linked_gtins: list[str] | None = None,
        rich_media_title: str | None = None,
        rich_media_type: RichMediaTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssetsResponse, GetAllAssetsErrorBody]:
        """Use this API to retrieve rich media assets, including 360-spin images and videos, from the seller catalog.
        Assets can be created in seller center media library or programmatically through the API. Use this endpoint to
        retrieve the asset hash, which uniquely identifies each media asset for future management.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            page: Indicates the page number to return in the paginated result set. Use this parameter to navigate
                through multiple pages of results. The value should be a positive integer. For example, 1 for the first
                page, 2 for the second, and so on. <b style="color: green;">Market availability: US only</b>
            limit: Defines the maximum number of items to return per page when retrieving paginated data. Use this
                parameter to control the number of results included in a single page. The value should be a positive
                integer. <b style="color: green;">Market availability: US only</b>
            linked_gtins: Filters assets by linked GTIN. Provide multiple GTINs as a list. If omitted, all assets are
                returned. <b style="color: green;">Market availability: US only</b>
            rich_media_title: Filters assets by rich media title or asset title. If omitted, all assets are returned. <b
                style="color: green;">Market availability: US only</b>
            rich_media_type: Filters assets by rich media type. Allowed values: ``IMAGES360``, ``VIDEO``. <b
                style="color: green;">Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/items/assets"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[list[str] | None]("linkedGtins", linked_gtins),
                param[str | None]("richMediaTitle", rich_media_title),
                param[RichMediaTypeOrStr | None]("richMediaType", rich_media_type),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[AssetsResponse],
            error_mapper=get_all_assets_error_mapper,
            request_options=request_options,
        )

    def rich_media_operation(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: RichMediaFeedRequest | RichMediaFeedRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, RichMediaOperationErrorBody]:
        """Use this API to create, update, or delink rich media assets for items in the seller catalog. Supported asset
        types are ``IMAGES360`` and ``VIDEO``. Use this API to 1) add new rich media, 2) update associations for
        existing rich media, or 3) delink item association on existing rich media. Provide accessible media URLs and
        related metadata in the request body. Video assets require one video URL. 360-spin image assets require 24 image
        URLs.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            body: Rich media feed payload containing asset metadata, item associations, and media URLs.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=OMNI_RICH_MEDIA"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[RichMediaFeedRequest | RichMediaFeedRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=json_decoder[FeedId1],
            error_mapper=rich_media_operation_error_mapper,
            request_options=request_options,
        )


class AsyncRichMediaWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_all_assets(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        *,
        page: int | None = 1,
        limit: int | None = 25,
        linked_gtins: list[str] | None = None,
        rich_media_title: str | None = None,
        rich_media_type: RichMediaTypeOrStr | None = None,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssetsResponse, GetAllAssetsErrorBody]:
        """Use this API to retrieve rich media assets, including 360-spin images and videos, from the seller catalog.
        Assets can be created in seller center media library or programmatically through the API. Use this endpoint to
        retrieve the asset hash, which uniquely identifies each media asset for future management.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            page: Indicates the page number to return in the paginated result set. Use this parameter to navigate
                through multiple pages of results. The value should be a positive integer. For example, 1 for the first
                page, 2 for the second, and so on. <b style="color: green;">Market availability: US only</b>
            limit: Defines the maximum number of items to return per page when retrieving paginated data. Use this
                parameter to control the number of results included in a single page. The value should be a positive
                integer. <b style="color: green;">Market availability: US only</b>
            linked_gtins: Filters assets by linked GTIN. Provide multiple GTINs as a list. If omitted, all assets are
                returned. <b style="color: green;">Market availability: US only</b>
            rich_media_title: Filters assets by rich media title or asset title. If omitted, all assets are returned. <b
                style="color: green;">Market availability: US only</b>
            rich_media_type: Filters assets by rich media type. Allowed values: ``IMAGES360``, ``VIDEO``. <b
                style="color: green;">Market availability: US only</b>
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/items/assets"),
            query_params=[
                param[int | None]("page", page),
                param[int | None]("limit", limit),
                param[list[str] | None]("linkedGtins", linked_gtins),
                param[str | None]("richMediaTitle", rich_media_title),
                param[RichMediaTypeOrStr | None]("richMediaType", rich_media_type),
            ],
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
            ],
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[AssetsResponse],
            error_mapper=get_all_assets_error_mapper,
            request_options=request_options,
        )

    async def rich_media_operation(
        self,
        wm_qos_correlation_id: str,
        wm_svc_name: str,
        body: RichMediaFeedRequest | RichMediaFeedRequestDict,
        *,
        wm_consumer_channel_type: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FeedId1, RichMediaOperationErrorBody]:
        """Use this API to create, update, or delink rich media assets for items in the seller catalog. Supported asset
        types are ``IMAGES360`` and ``VIDEO``. Use this API to 1) add new rich media, 2) update associations for
        existing rich media, or 3) delink item association on existing rich media. Provide accessible media URLs and
        related metadata in the request body. Video assets require one video URL. 360-spin image assets require 24 image
        URLs.

        <b style="color: green;">Market availability: US only</b>

        Args:
            wm_qos_correlation_id: A unique ID that identifies each API call and is used to track and debug issues. Use
                a randomly generated GUID for this ID. <b style="color: green;">Market availability: Global</b>
            wm_svc_name: Specifies the name of the Walmart service being called. <b style="color: green;">Market
                availability: Global</b>
            body: Rich media feed payload containing asset metadata, item associations, and media URLs.
            wm_consumer_channel_type: A unique ID to identify the consumer request by channel. Use the consumer channel
                type received during onboarding. <b style="color: green;">Market availability: Global</b>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v3/feeds?feedType=OMNI_RICH_MEDIA"),
            headers=[
                param[str]("WM_QOS.CORRELATION_ID", wm_qos_correlation_id),
                param[str]("WM_SVC.NAME", wm_svc_name),
                param[str | None]("WM_CONSUMER.CHANNEL.TYPE", wm_consumer_channel_type),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[RichMediaFeedRequest | RichMediaFeedRequestDict](body),
            auth_scheme=self._auth.access_token,
            decoder=async_json_decoder[FeedId1],
            error_mapper=rich_media_operation_error_mapper,
            request_options=request_options,
        )
